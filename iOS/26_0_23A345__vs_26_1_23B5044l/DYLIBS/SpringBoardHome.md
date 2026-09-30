## SpringBoardHome

> `/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome`

```diff

-159.107.0.0.0
-  __TEXT.__text: 0x3229a4
+163.101.0.0.0
+  __TEXT.__text: 0x324eec
   __TEXT.__auth_stubs: 0x2cb0
-  __TEXT.__objc_methlist: 0x3b7dc
+  __TEXT.__objc_methlist: 0x3b994
   __TEXT.__const: 0x62a4
-  __TEXT.__cstring: 0x1b35f
-  __TEXT.__gcc_except_tab: 0x3d08
-  __TEXT.__oslogstring: 0xd710
+  __TEXT.__cstring: 0x1b1ff
+  __TEXT.__gcc_except_tab: 0x3e48
+  __TEXT.__oslogstring: 0xdd80
   __TEXT.__dlopen_cstrs: 0x4c6
   __TEXT.__ustring: 0x620
   __TEXT.__swift5_typeref: 0x179c

   __TEXT.__swift5_capture: 0xfb8
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0xe1b0
+  __TEXT.__unwind_info: 0xe270
   __TEXT.__eh_frame: 0x990
-  __TEXT.__objc_classname: 0x6d6d
-  __TEXT.__objc_methname: 0x987ad
-  __TEXT.__objc_methtype: 0x19113
-  __TEXT.__objc_stubs: 0x586e0
-  __DATA_CONST.__got: 0x2230
-  __DATA_CONST.__const: 0x9530
-  __DATA_CONST.__objc_classlist: 0x1258
-  __DATA_CONST.__objc_catlist: 0x120
+  __TEXT.__objc_classname: 0x6db6
+  __TEXT.__objc_methname: 0x98fc0
+  __TEXT.__objc_methtype: 0x19264
+  __TEXT.__objc_stubs: 0x58b80
+  __DATA_CONST.__got: 0x2250
+  __DATA_CONST.__const: 0x9668
+  __DATA_CONST.__objc_classlist: 0x1268
+  __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0xb28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b520
-  __DATA_CONST.__objc_protorefs: 0x140
-  __DATA_CONST.__objc_superrefs: 0xe20
+  __DATA_CONST.__objc_selrefs: 0x1b690
+  __DATA_CONST.__objc_protorefs: 0x148
+  __DATA_CONST.__objc_superrefs: 0xe38
   __DATA_CONST.__objc_arraydata: 0x6d8
   __AUTH_CONST.__auth_got: 0x1668
-  __AUTH_CONST.__const: 0x6270
-  __AUTH_CONST.__cfstring: 0x158e0
-  __AUTH_CONST.__objc_const: 0x54780
+  __AUTH_CONST.__const: 0x6230
+  __AUTH_CONST.__cfstring: 0x15aa0
+  __AUTH_CONST.__objc_const: 0x54ab0
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH.__objc_data: 0x6028
+  __AUTH.__objc_data: 0x6118
   __AUTH.__data: 0x568
-  __DATA.__objc_ivar: 0x3a84
+  __DATA.__objc_ivar: 0x3aac
   __DATA.__data: 0x8878
-  __DATA.__bss: 0x2208
+  __DATA.__bss: 0x21f8
   __DATA.__common: 0x58
-  __DATA_DIRTY.__objc_data: 0x5ca8
+  __DATA_DIRTY.__objc_data: 0x5c58
   __DATA_DIRTY.__data: 0xd8
   __DATA_DIRTY.__bss: 0x430
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/AACCore.framework/AACCore
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F3A89682-429D-3319-876B-46D2348E0DFD
-  Functions: 22292
-  Symbols:   63561
-  CStrings:  30303
+  UUID: 5E573D56-850E-3898-9108-DCB4B56C5EAE
+  Functions: 22366
+  Symbols:   63770
+  CStrings:  30427
 
Symbols:
+ +[SBAssessmentModeMonitor sharedInstance]
+ +[SBIconImageView defaultImageLoadingBehavior]
+ +[SBIconListView iconViewUserVisibilityStatusForContentVisibility:]
+ +[SBIconView updateAppearStateForViewController:forContentVisibility:]
+ -[SBAssessmentModeMonitor .cxx_destruct]
+ -[SBAssessmentModeMonitor _init]
+ -[SBAssessmentModeMonitor assessmentModeGestalt]
+ -[SBAssessmentModeMonitor dealloc]
+ -[SBAssessmentModeMonitor isActive]
+ -[SBAssessmentModeMonitor observeValueForKeyPath:ofObject:change:context:]
+ -[SBAssessmentModeMonitor setActive:]
+ -[SBAssessmentModeMonitor setAssessmentModeGestalt:]
+ -[SBFloatyFolderView iconFadeAnimator:wantsToApplyAlpha:]
+ -[SBFolderBackgroundView setUsesGlass:]
+ -[SBFolderBackgroundView updateGlass]
+ -[SBFolderBackgroundView usesGlass]
+ -[SBFolderController folderView:iconListView:willConfigureIconView:forIcon:]
+ -[SBFolderController pageViewControllerForPageIndex:]
+ -[SBFolderController shouldViewControllersAppearVisibleForIconView:]
+ -[SBFolderController updatePresentationModeFolderContextForIconView:]
+ -[SBFolderIconImageView setContentVisibility:]
+ -[SBFolderTitleTextField layoutSubviews]
+ -[SBFolderView iconListView:willConfigureIconView:forIcon:]
+ -[SBFolderView pageControlOverrideUserInterfaceStyle]
+ -[SBHAddWidgetDetailSheetViewController viewIsAppearing:]
+ -[SBHAddWidgetDetailsSheetPageViewController contentVisibility]
+ -[SBHAddWidgetDetailsSheetPageViewController setContentVisibility:]
+ -[SBHAddWidgetSheetViewController iconListView:willConfigureIconView:forIcon:]
+ -[SBHDefaultIconListLayoutProvider showsLabelsForScreenType:iconLocation:layoutOptions:]
+ -[SBHIconGridContiguousRegion enumerateGridCellIndexesNotContainedInGridRange:usingBlock:]
+ -[SBHIconGridContiguousRegion gridCellIndexesNotContainedInGridRange:]
+ -[SBHIconImageVariantCache _variantImageForIcon:imageAppearance:context:extraImageOptions:options:]
+ -[SBHIconImageVariantCache _variantImageForIcon:imageAppearance:context:extraImageOptions:options:].cold.1
+ -[SBHIconManager contextMenuManager:orderedActionContextMenuProvidersForIconView:]
+ -[SBHIconManager contextMenuManager:preferredMenuElementOrderForIconView:]
+ -[SBHIconMiniGridView contentVisibility]
+ -[SBHIconMiniGridView initWithFrame:]
+ -[SBHIconMiniGridView setContentVisibility:]
+ -[SBHIconStylePreviewManager initWithTraitOverridableObjects:iconListViews:additionalIconViews:]
+ -[SBHIconViewContextMenuManager orderedActionContextMenuProvidersForIconView:]
+ -[SBHLibraryCategoryStackView makeBackgroundView]
+ -[SBHLightSourceManager shouldUpdateLight]
+ -[SBHMultiplexingViewController viewIsAppearing:]
+ -[SBHMutablePresentationModeFolderContext copyWithZone:]
+ -[SBHMutablePresentationModeFolderContext setHasAssertionForLowResolutionSnapshotPresentationMode:]
+ -[SBHMutablePresentationModeFolderContext setHasAssertionForSnapshotPresentationMode:]
+ -[SBHPresentationModeFolderContext _initWithContext:]
+ -[SBHPresentationModeFolderContext copyWithZone:]
+ -[SBHPresentationModeFolderContext hasAssertionForLowResolutionSnapshotPresentationMode]
+ -[SBHPresentationModeFolderContext hasAssertionForSnapshotPresentationMode]
+ -[SBHPresentationModeFolderContext mutableCopyWithZone:]
+ -[SBHSearchTextField buildMenuWithBuilder:]
+ -[SBHTodayViewController _updatePresentationModeContextForIconViews]
+ -[SBHWidget logIdentifier]
+ -[SBHWidgetAddGalleryWidgetViewController .cxx_destruct]
+ -[SBHWidgetAddGalleryWidgetViewController _chuisWidgetPresentationModeFromIconPresentationMode:]
+ -[SBHWidgetAddGalleryWidgetViewController _configureBackgroundViewIfNecessary:]
+ -[SBHWidgetAddGalleryWidgetViewController _configureBackgroundViewIfNecessary]
+ -[SBHWidgetAddGalleryWidgetViewController _createBackgroundViewIfNecessary:]
+ -[SBHWidgetAddGalleryWidgetViewController _createBackgroundView]
+ -[SBHWidgetAddGalleryWidgetViewController _needsBackgroundView]
+ -[SBHWidgetAddGalleryWidgetViewController _setupStateCapture]
+ -[SBHWidgetAddGalleryWidgetViewController _teardownBackgroundView:]
+ -[SBHWidgetAddGalleryWidgetViewController _teardownBackgroundView]
+ -[SBHWidgetAddGalleryWidgetViewController _teardownStateCapture]
+ -[SBHWidgetAddGalleryWidgetViewController _updateContentViewControllerPresentationMode]
+ -[SBHWidgetAddGalleryWidgetViewController _updateEdgeAntialiasing]
+ -[SBHWidgetAddGalleryWidgetViewController backdropGroupNameForActiveDataSource:]
+ -[SBHWidgetAddGalleryWidgetViewController backgroundViewConfigurator]
+ -[SBHWidgetAddGalleryWidgetViewController backgroundViewProvider]
+ -[SBHWidgetAddGalleryWidgetViewController backgroundView]
+ -[SBHWidgetAddGalleryWidgetViewController contentViewController]
+ -[SBHWidgetAddGalleryWidgetViewController contentView]
+ -[SBHWidgetAddGalleryWidgetViewController continuousCornerRadius]
+ -[SBHWidgetAddGalleryWidgetViewController dealloc]
+ -[SBHWidgetAddGalleryWidgetViewController evaluateBackground]
+ -[SBHWidgetAddGalleryWidgetViewController forcesEdgeAntialiasing]
+ -[SBHWidgetAddGalleryWidgetViewController iconImageInfo]
+ -[SBHWidgetAddGalleryWidgetViewController icon]
+ -[SBHWidgetAddGalleryWidgetViewController initWithContentViewController:]
+ -[SBHWidgetAddGalleryWidgetViewController presentationMode]
+ -[SBHWidgetAddGalleryWidgetViewController setBackgroundView:]
+ -[SBHWidgetAddGalleryWidgetViewController setBackgroundViewConfigurator:]
+ -[SBHWidgetAddGalleryWidgetViewController setBackgroundViewProvider:]
+ -[SBHWidgetAddGalleryWidgetViewController setContentViewController:]
+ -[SBHWidgetAddGalleryWidgetViewController setForcesEdgeAntialiasing:]
+ -[SBHWidgetAddGalleryWidgetViewController setIconImageInfo:]
+ -[SBHWidgetAddGalleryWidgetViewController setPresentationMode:]
+ -[SBHWidgetAddGalleryWidgetViewController setShowsSquareCorners:]
+ -[SBHWidgetAddGalleryWidgetViewController showsSquareCorners]
+ -[SBHWidgetAddGalleryWidgetViewController snapshotViewScaleFactor]
+ -[SBHWidgetAddGalleryWidgetViewController snapshotView]
+ -[SBHWidgetAddGalleryWidgetViewController sourceView]
+ -[SBHWidgetAddGalleryWidgetViewController viewDidDisappear:]
+ -[SBHWidgetAddGalleryWidgetViewController viewDidLayoutSubviews]
+ -[SBHWidgetAddGalleryWidgetViewController viewDidLoad]
+ -[SBHWidgetAddGalleryWidgetViewController viewWillAppear:]
+ -[SBHWidgetAddGalleryWidgetViewController visibleBounds]
+ -[SBHWidgetAddGalleryWidgetViewController(SBHWidgetUtilitiesInternal) sbh_isCustomIconImageViewController]
+ -[SBHWidgetAddGalleryWidgetViewController(SBHWidgetUtilitiesInternal) sbh_underlyingAvocadoHostViewControllers]
+ -[SBHWidgetContainerView initWithGridSizeClass:iconImageInfo:applicationName:logIdentifier:]
+ -[SBHWidgetContainerViewController _updateEffectivePresentationMode]
+ -[SBHWidgetContainerViewController performBatchedUpdate:]
+ -[SBHWidgetContainerViewController viewIsAppearing:]
+ -[SBHWidgetStackViewController _createViewControllerForWidgetIfNecessary:usingIconImageInfo:].cold.1
+ -[SBHWidgetStackViewController _updateWidgetViewsWithAnimationUpdateMode:].cold.1
+ -[SBHWidgetStackViewController viewIsAppearing:]
+ -[SBHWidgetWrapperViewController _updateWidgetHostViewController]
+ -[SBHWidgetWrapperViewController _updateWidgetHostViewController].cold.1
+ -[SBHWidgetWrapperViewController contentVisibility]
+ -[SBHWidgetWrapperViewController setContentVisibility:]
+ -[SBIcon logIdentifier]
+ -[SBIconImageView pauseLightAngleUpdatesForIconLayer:]
+ -[SBIconImageView setImageLoadingBehavior:]
+ -[SBIconImageView setOverrideIconImageAppearance:]
+ -[SBIconImageView setOverrideIconImageStyleConfiguration:]
+ -[SBIconListModel _moveContainedIconWithinAffectedQuadsIfNecessary:toGridCellIndex:gridCellInfoOptions:mutationOptions:].cold.1
+ -[SBIconListModel gridCellIndexesForIconsIntersectingGridRange:gridCellInfo:]
+ -[SBIconListModel gridCellIndexesForIconsIntersectingGridRange:gridCellInfoOptions:]
+ -[SBIconListModel gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridCellIndexes:gridCellInfo:gridCellInfoOptions:mutationOptions:]
+ -[SBIconListModel hasPlaceholderIcons]
+ -[SBIconListModel layoutGenerationCount]
+ -[SBIconListModel setHasPlaceholderIcons:]
+ -[SBIconListModel simpleInsertionIconIndexForGridCellIndex:]
+ -[SBIconListModel updateHasPlaceholderIcons]
+ -[SBIconListView _updateVisibleIconViewsWithOldCellVisibility:oldVisibleGridCellIndexes:oldPrefetchedGridCellIndexes:metrics:]
+ -[SBIconListView contentVisibilityForIcon:metrics:]
+ -[SBIconListView displayedIconViewForCoordinate:]
+ -[SBIconListView displayedIconViewForGridCellIndex:]
+ -[SBIconListView iconContentVisibility]
+ -[SBIconListView iconViewUserVisibilityStatusForIcon:]
+ -[SBIconView _reevaluateLogIdentifier]
+ -[SBIconView _updatePresentationModeForReason:]
+ -[SBIconView _updatePresentationModeForReason:].cold.1
+ -[SBIconView _updatePresentationModeForReason:].cold.2
+ -[SBIconView _updatePresentationModeForReason:].cold.3
+ -[SBIconView _updatePresentationModeForReason:].cold.4
+ -[SBIconView _updatePresentationModeForReason:].cold.5
+ -[SBIconView _updatePresentationModeForReason:].cold.6
+ -[SBIconView _updatePresentationModeForReason:].cold.7
+ -[SBIconView borrowIconImageViewWithOptions:].cold.1
+ -[SBIconView configureBorrowingIconImageViewFromIconView:].cold.1
+ -[SBIconView configureMatchingIconView:].cold.1
+ -[SBIconView didDelayInsertingCustomImageViewDueToParentController]
+ -[SBIconView didMoveToSuperview]
+ -[SBIconView effectiveContentVisibility]
+ -[SBIconView overrideParentViewControllerForCustomIconImageViewController]
+ -[SBIconView parentViewControllerForCustomIconImageViewController]
+ -[SBIconView pendingIcon]
+ -[SBIconView presentationModeFolderContext]
+ -[SBIconView removeBorrowedIconImageViewAssertion:].cold.1
+ -[SBIconView setContentVisibility:].cold.1
+ -[SBIconView setCustomIconImageViewController:clearingOwner:].cold.1
+ -[SBIconView setDidDelayInsertingCustomImageViewDueToParentController:]
+ -[SBIconView setOverrideParentViewControllerForCustomIconImageViewController:]
+ -[SBIconView setPendingIcon:]
+ -[SBIconView setPresentationModeFolderContext:]
+ -[SBIconView updateContentVisibilityOnCurrentImageView]
+ -[SBRootFolderController pageViewControllerForPageIndex:]
+ -[SBWidgetIcon didChangeActiveDataSource:]
+ -[SBWidgetIconResizeBackdropView blurRadius]
+ -[SBWidgetIconResizeBackdropView initWithBlurRadius:]
+ -[SBWidgetIconResizeBackdropView setBlurRadius:]
+ -[SBWidgetIconResizeContainerView .cxx_destruct]
+ -[SBWidgetIconResizeContainerView blurView]
+ -[SBWidgetIconResizeContainerView contentSize]
+ -[SBWidgetIconResizeContainerView contentView]
+ -[SBWidgetIconResizeContainerView initWithBlurRadius:]
+ -[SBWidgetIconResizeContainerView layoutSubviews]
+ -[SBWidgetIconResizeContainerView setContentView:]
+ -[SBWidgetIconResizeTransitionViewController endingContainerView]
+ -[SBWidgetIconResizeTransitionViewController setEndingContainerView:]
+ -[SBWidgetIconResizeTransitionViewController setStartingContainerView:]
+ -[SBWidgetIconResizeTransitionViewController startingContainerView]
+ -[SBWidgetIconResizeTransitionViewController swapViewControllersAndClearEnding]
+ -[UITouch(SBIconViewUtilities) sbh_didExitIconView]
+ -[UITouch(SBIconViewUtilities) sbh_setDidExitIconView:]
+ GCC_except_table1019
+ GCC_except_table1042
+ GCC_except_table112
+ GCC_except_table119
+ GCC_except_table148
+ GCC_except_table169
+ GCC_except_table183
+ GCC_except_table19
+ GCC_except_table191
+ GCC_except_table205
+ GCC_except_table211
+ GCC_except_table223
+ GCC_except_table234
+ GCC_except_table238
+ GCC_except_table243
+ GCC_except_table251
+ GCC_except_table260
+ GCC_except_table272
+ GCC_except_table310
+ GCC_except_table325
+ GCC_except_table334
+ GCC_except_table335
+ GCC_except_table339
+ GCC_except_table343
+ GCC_except_table352
+ GCC_except_table358
+ GCC_except_table365
+ GCC_except_table378
+ GCC_except_table391
+ GCC_except_table395
+ GCC_except_table398
+ GCC_except_table401
+ GCC_except_table403
+ GCC_except_table405
+ GCC_except_table410
+ GCC_except_table428
+ GCC_except_table433
+ GCC_except_table441
+ GCC_except_table446
+ GCC_except_table462
+ GCC_except_table464
+ GCC_except_table484
+ GCC_except_table502
+ GCC_except_table504
+ GCC_except_table509
+ GCC_except_table531
+ GCC_except_table534
+ GCC_except_table553
+ GCC_except_table557
+ GCC_except_table572
+ GCC_except_table586
+ GCC_except_table627
+ GCC_except_table659
+ GCC_except_table673
+ GCC_except_table683
+ GCC_except_table686
+ GCC_except_table695
+ GCC_except_table697
+ GCC_except_table699
+ GCC_except_table706
+ GCC_except_table708
+ GCC_except_table710
+ GCC_except_table717
+ GCC_except_table720
+ GCC_except_table735
+ GCC_except_table737
+ GCC_except_table820
+ GCC_except_table86
+ GCC_except_table876
+ GCC_except_table90
+ GCC_except_table946
+ GCC_except_table966
+ GCC_except_table983
+ OBJC_IVAR_$_SBHPresentationModeFolderContext._hasAssertionForLowResolutionSnapshotPresentationMode
+ OBJC_IVAR_$_SBHPresentationModeFolderContext._hasAssertionForSnapshotPresentationMode
+ OBJC_IVAR_$_SBIcon._logIdentifier
+ _CHSWidgetFamilyDescription
+ _NSKeyValueChangeNewKey
+ _NSStringFromSBIconViewCustomIconImageViewControllerPresentationMode
+ _OBJC_CLASS_$_AEAssessmentModeGestalt
+ _OBJC_CLASS_$_SBAssessmentModeMonitor
+ _OBJC_CLASS_$_SBHMutablePresentationModeFolderContext
+ _OBJC_CLASS_$_SBHPresentationModeFolderContext
+ _OBJC_CLASS_$_SBHWidgetAddGalleryWidgetViewController
+ _OBJC_CLASS_$_SBWidgetIconResizeContainerView
+ _OBJC_IVAR_$_SBAssessmentModeMonitor._active
+ _OBJC_IVAR_$_SBAssessmentModeMonitor._assessmentModeGestalt
+ _OBJC_IVAR_$_SBFolderBackgroundView._usesGlass
+ _OBJC_IVAR_$_SBHAddWidgetDetailsSheetPageViewController._contentVisibility
+ _OBJC_IVAR_$_SBHIconImageCacheRequest._iconImageLoadContext
+ _OBJC_IVAR_$_SBHIconMiniGridView._contentVisibility
+ _OBJC_IVAR_$_SBHWidget._logIdentifier
+ _OBJC_IVAR_$_SBHWidgetAddGalleryWidgetViewController._backgroundView
+ _OBJC_IVAR_$_SBHWidgetAddGalleryWidgetViewController._backgroundViewConfigurator
+ _OBJC_IVAR_$_SBHWidgetAddGalleryWidgetViewController._backgroundViewProvider
+ _OBJC_IVAR_$_SBHWidgetAddGalleryWidgetViewController._contentViewController
+ _OBJC_IVAR_$_SBHWidgetAddGalleryWidgetViewController._forcesEdgeAntialiasing
+ _OBJC_IVAR_$_SBHWidgetAddGalleryWidgetViewController._icon
+ _OBJC_IVAR_$_SBHWidgetAddGalleryWidgetViewController._iconImageInfo
+ _OBJC_IVAR_$_SBHWidgetAddGalleryWidgetViewController._requestedPresentationMode
+ _OBJC_IVAR_$_SBHWidgetAddGalleryWidgetViewController._showsSquareCorners
+ _OBJC_IVAR_$_SBHWidgetAddGalleryWidgetViewController._stateCaptureInvalidatable
+ _OBJC_IVAR_$_SBHWidgetContainerView._logIdentifier
+ _OBJC_IVAR_$_SBHWidgetContainerViewController._batchUpdateCount
+ _OBJC_IVAR_$_SBHWidgetContainerViewController._effectivePresentationMode
+ _OBJC_IVAR_$_SBHWidgetContainerViewController._logIdentifier
+ _OBJC_IVAR_$_SBHWidgetContainerViewController._presentationModeDirty
+ _OBJC_IVAR_$_SBHWidgetContainerViewController._requestedPresentationMode
+ _OBJC_IVAR_$_SBHWidgetStackViewController._logIdentifier
+ _OBJC_IVAR_$_SBHWidgetWrapperViewController._contentVisibility
+ _OBJC_IVAR_$_SBIconImageView._imageLoadingBehavior
+ _OBJC_IVAR_$_SBIconImageView._overrideIconImageAppearance
+ _OBJC_IVAR_$_SBIconImageView._overrideIconImageStyleConfiguration
+ _OBJC_IVAR_$_SBIconListModel._hasPlaceholderIcons
+ _OBJC_IVAR_$_SBIconListModel._layoutGenerationCount
+ _OBJC_IVAR_$_SBIconView._didDelayInsertingCustomImageViewDueToParentController
+ _OBJC_IVAR_$_SBIconView._effectiveApplicationShortcutItems
+ _OBJC_IVAR_$_SBIconView._inConfigurationTransition
+ _OBJC_IVAR_$_SBIconView._logIdentifier
+ _OBJC_IVAR_$_SBIconView._overrideParentViewControllerForCustomIconImageViewController
+ _OBJC_IVAR_$_SBIconView._pendingIcon
+ _OBJC_IVAR_$_SBIconView._presentationModeFolderContext
+ _OBJC_IVAR_$_SBWidgetIconResizeBackdropView._blurRadius
+ _OBJC_IVAR_$_SBWidgetIconResizeContainerView._blurView
+ _OBJC_IVAR_$_SBWidgetIconResizeContainerView._contentSize
+ _OBJC_IVAR_$_SBWidgetIconResizeContainerView._contentView
+ _OBJC_IVAR_$_SBWidgetIconResizeTransitionViewController._endingContainerView
+ _OBJC_IVAR_$_SBWidgetIconResizeTransitionViewController._startingContainerView
+ _OBJC_METACLASS_$_SBAssessmentModeMonitor
+ _OBJC_METACLASS_$_SBHMutablePresentationModeFolderContext
+ _OBJC_METACLASS_$_SBHPresentationModeFolderContext
+ _OBJC_METACLASS_$_SBHWidgetAddGalleryWidgetViewController
+ _OBJC_METACLASS_$_SBWidgetIconResizeContainerView
+ _SBHContentVisibilityIsNotHidden
+ _SBHContentVisibilityIsVisible
+ _SBHIconGridRangeIsContainedInIndexSet
+ _SBHIconListLayoutFolderIconGridCellIconImageInfo
+ _SBHIconViewTouchDidExitKey
+ _SBLogAssessmentMode
+ _SBLogAssessmentMode.__logObj
+ _SBLogAssessmentMode.cold.1
+ _SBLogAssessmentMode.onceToken
+ _UIMenuAutoFill
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UITouch_$_SBIconViewUtilities
+ __OBJC_$_CATEGORY_UITouch_$_SBIconViewUtilities
+ __OBJC_$_CLASS_METHODS_SBAssessmentModeMonitor
+ __OBJC_$_INSTANCE_METHODS_SBAssessmentModeMonitor
+ __OBJC_$_INSTANCE_METHODS_SBHMutablePresentationModeFolderContext
+ __OBJC_$_INSTANCE_METHODS_SBHPresentationModeFolderContext
+ __OBJC_$_INSTANCE_METHODS_SBHWidgetAddGalleryWidgetViewController(SBHWidgetUtilitiesInternal)
+ __OBJC_$_INSTANCE_METHODS_SBWidgetIconResizeContainerView
+ __OBJC_$_INSTANCE_VARIABLES_SBAssessmentModeMonitor
+ __OBJC_$_INSTANCE_VARIABLES_SBHPresentationModeFolderContext
+ __OBJC_$_INSTANCE_VARIABLES_SBHWidgetAddGalleryWidgetViewController
+ __OBJC_$_INSTANCE_VARIABLES_SBWidgetIconResizeBackdropView
+ __OBJC_$_INSTANCE_VARIABLES_SBWidgetIconResizeContainerView
+ __OBJC_$_PROP_LIST_SBAssessmentModeMonitor
+ __OBJC_$_PROP_LIST_SBHMutablePresentationModeFolderContext
+ __OBJC_$_PROP_LIST_SBHPresentationModeFolderContext
+ __OBJC_$_PROP_LIST_SBHWidgetAddGalleryWidgetViewController
+ __OBJC_$_PROP_LIST_SBIconViewCustomImageViewControlling_Internal
+ __OBJC_$_PROP_LIST_SBWidgetIconResizeBackdropView
+ __OBJC_$_PROP_LIST_SBWidgetIconResizeContainerView
+ __OBJC_$_PROP_LIST_UITouch_$_SBIconViewUtilities
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBIconFadeAnimatorCrossfadeView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBIconViewCustomImageViewControlling_Internal
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBIconFadeAnimatorCrossfadeView
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBIconViewCustomImageViewControlling_Internal
+ __OBJC_$_PROTOCOL_REFS_SBIconFadeAnimatorCrossfadeView
+ __OBJC_$_PROTOCOL_REFS_SBIconViewCustomImageViewControlling_Internal
+ __OBJC_CLASS_PROTOCOLS_$_SBHIconMiniGridView
+ __OBJC_CLASS_PROTOCOLS_$_SBHPresentationModeFolderContext
+ __OBJC_CLASS_PROTOCOLS_$_SBHWidgetAddGalleryWidgetViewController
+ __OBJC_CLASS_RO_$_SBAssessmentModeMonitor
+ __OBJC_CLASS_RO_$_SBHMutablePresentationModeFolderContext
+ __OBJC_CLASS_RO_$_SBHPresentationModeFolderContext
+ __OBJC_CLASS_RO_$_SBHWidgetAddGalleryWidgetViewController
+ __OBJC_CLASS_RO_$_SBWidgetIconResizeContainerView
+ __OBJC_LABEL_PROTOCOL_$_SBIconFadeAnimatorCrossfadeView
+ __OBJC_LABEL_PROTOCOL_$_SBIconViewCustomImageViewControlling_Internal
+ __OBJC_METACLASS_RO_$_SBAssessmentModeMonitor
+ __OBJC_METACLASS_RO_$_SBHMutablePresentationModeFolderContext
+ __OBJC_METACLASS_RO_$_SBHPresentationModeFolderContext
+ __OBJC_METACLASS_RO_$_SBHWidgetAddGalleryWidgetViewController
+ __OBJC_METACLASS_RO_$_SBWidgetIconResizeContainerView
+ __OBJC_PROTOCOL_$_SBIconFadeAnimatorCrossfadeView
+ __OBJC_PROTOCOL_$_SBIconViewCustomImageViewControlling_Internal
+ __OBJC_PROTOCOL_REFERENCE_$_SBIconViewCustomImageViewControlling_Internal
+ __PROTOCOLS_SBHIconLayerView
+ __PROTOCOLS_SBHIconLayerView.1
+ ___106-[SBHWidgetStackViewController _removeWidgetWithUniqueIdentifier:widgetContainerViewControllers:animated:]_block_invoke.97
+ ___138-[SBIconListModel gridCellInfoByUsingTwoDimensionalMovementToInsertIcon:atGridCellIndex:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke
+ ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke.1085
+ ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke_2.1087
+ ___178-[SBIconListModel gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridCellIndexes:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke
+ ___178-[SBIconListModel gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridCellIndexes:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke_2
+ ___178-[SBIconListModel gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridCellIndexes:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke_3
+ ___178-[SBIconListModel gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridCellIndexes:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke_4
+ ___41+[SBAssessmentModeMonitor sharedInstance]_block_invoke
+ ___44-[SBHIconMiniGridView setContentVisibility:]_block_invoke
+ ___44-[SBHWidgetStyleManager updateConfiguration]_block_invoke
+ ___44-[SBIconListModel updateHasPlaceholderIcons]_block_invoke
+ ___44-[SBIconListView configureIconView:forIcon:]_block_invoke
+ ___47-[SBIconView resizeGestureRecognizerDidUpdate:]_block_invoke.968
+ ___51-[SBHIconManager _engageWallpaperTintColorDropper:]_block_invoke.962
+ ___54-[SBHWidgetStackViewController _logAllViewControllers]_block_invoke.151
+ ___54-[SBHWidgetStackViewController _logAllViewControllers]_block_invoke.151.cold.1
+ ___57-[SBFloatyFolderView iconFadeAnimator:wantsToApplyAlpha:]_block_invoke
+ ___57-[SBFloatyFolderView iconFadeAnimator:wantsToApplyAlpha:]_block_invoke_2
+ ___59-[SBIconListView layoutIconsIfNeededUsingAnimator:options:]_block_invoke.89
+ ___59-[SBIconListView layoutIconsIfNeededUsingAnimator:options:]_block_invoke_2.95
+ ___61-[SBHWidgetAddGalleryWidgetViewController _setupStateCapture]_block_invoke
+ ___61-[SBHWidgetAddGalleryWidgetViewController _setupStateCapture]_block_invoke_2
+ ___62-[SBIconListView regenerateTemporaryDisplayedModelIfNecessary]_block_invoke.46
+ ___62-[SBIconListView regenerateTemporaryDisplayedModelIfNecessary]_block_invoke_2.48
+ ___62-[SBIconListView regenerateTemporaryDisplayedModelIfNecessary]_block_invoke_3.49
+ ___68-[SBHTodayViewController _updatePresentationModeContextForIconViews]_block_invoke
+ ___70-[SBHIconGridContiguousRegion gridCellIndexesNotContainedInGridRange:]_block_invoke
+ ___74-[SBHWidgetStackViewController _updateWidgetViewsWithAnimationUpdateMode:]_block_invoke.121
+ ___74-[SBHWidgetStackViewController _updateWidgetViewsWithAnimationUpdateMode:]_block_invoke_2.122
+ ___77-[SBHFileWidgetExtensionProvider filesWidgetViewControllerWithConfiguration:]_block_invoke.129
+ ___77-[SBIconListModel gridCellIndexesForIconsIntersectingGridRange:gridCellInfo:]_block_invoke
+ ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.525
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.597
+ ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.600
+ ___90-[SBHIconGridContiguousRegion enumerateGridCellIndexesNotContainedInGridRange:usingBlock:]_block_invoke
+ ___93-[SBHWidgetStackViewController _createViewControllerForWidgetIfNecessary:usingIconImageInfo:]_block_invoke_2
+ ___93-[SBHWidgetStackViewController _createViewControllerForWidgetIfNecessary:usingIconImageInfo:]_block_invoke_3
+ ___93-[SBHWidgetStackViewController _createViewControllerForWidgetIfNecessary:usingIconImageInfo:]_block_invoke_4
+ ___96-[SBHWidgetStackViewController _updateBackgroundViewWithAnimationUpdateMode:allowingOutsetting:]_block_invoke.127
+ ___98-[SBHIconViewFileStackConfigurationContextMenuProvider contextMenuSectionsForIconView:atLocation:]_block_invoke.58
+ ___98-[SBHIconViewFileStackConfigurationContextMenuProvider contextMenuSectionsForIconView:atLocation:]_block_invoke_2.30
+ ___98-[SBHIconViewFileStackConfigurationContextMenuProvider contextMenuSectionsForIconView:atLocation:]_block_invoke_2.65
+ ___SBHIconGridRangeIsContainedInIndexSet_block_invoke
+ ___SBLogAssessmentMode_block_invoke
+ ___block_descriptor_113_e8_32s40s48s56s64s72r_e5_v8?0lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_129_e8_32s40s48s56s64s72s80s88r_e5_v8?0lr88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_177_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_32_e33_v32?0"SBHIconLayerView"8Q16^B24l
+ ___block_descriptor_33_e46_v24?0"SBFloatyFolderBackgroundClipView"8^B16l
+ ___block_descriptor_40_e31_v32?0"SBIcon"8"UIView"16^B24l
+ ___block_descriptor_40_e8_32r_e12_v24?0Q8^B16lr32l8
+ ___block_descriptor_40_e8_32s_e46_v32?0"NSNumber"8"NSMutableDictionary"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_60_e8_32bs_e12_v24?0Q8^B16ls32l8
+ ___block_descriptor_64_e8_32s40s_e12_v24?0Q8^B16ls32l8s40l8
+ ___block_descriptor_64_e8_32s_e12_B24?0Q8^B16ls32l8
+ ___block_descriptor_72_e8_32s40s48r_e23_v32?0"SBIcon"8Q16^B24ls32l8s40l8r48l8
+ ___block_descriptor_81_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_84_e8_32s40s48s56r_e23_v32?0"SBIcon"8Q16^B24ls32l8s40l8s48l8r56l8
+ ___block_literal_global.1007
+ ___block_literal_global.101
+ ___block_literal_global.1046
+ ___block_literal_global.106
+ ___block_literal_global.116
+ ___block_literal_global.1164
+ ___block_literal_global.1217
+ ___block_literal_global.1224
+ ___block_literal_global.136
+ ___block_literal_global.221
+ ___block_literal_global.23
+ ___block_literal_global.246
+ ___block_literal_global.25
+ ___block_literal_global.2718
+ ___block_literal_global.283
+ ___block_literal_global.312
+ ___block_literal_global.337
+ ___block_literal_global.362
+ ___block_literal_global.365
+ ___block_literal_global.367
+ ___block_literal_global.369
+ ___block_literal_global.399
+ ___block_literal_global.406
+ ___block_literal_global.599
+ ___block_literal_global.782
+ ___block_literal_global.808
+ ___block_literal_global.855
+ ___block_literal_global.87
+ ___block_literal_global.875
+ ___block_literal_global.99
+ _objc_msgSend$_chuisWidgetPresentationModeFromIconPresentationMode:
+ _objc_msgSend$_initWithContext:
+ _objc_msgSend$_reevaluateLogIdentifier
+ _objc_msgSend$_updateContentViewControllerPresentationMode
+ _objc_msgSend$_updateEffectivePresentationMode
+ _objc_msgSend$_updatePresentationModeContextForIconViews
+ _objc_msgSend$_updatePresentationModeForReason:
+ _objc_msgSend$_updateVisibleIconViewsWithOldCellVisibility:oldVisibleGridCellIndexes:oldPrefetchedGridCellIndexes:metrics:
+ _objc_msgSend$_updateWidgetHostViewController
+ _objc_msgSend$_variantImageForIcon:imageAppearance:context:extraImageOptions:options:
+ _objc_msgSend$appClips
+ _objc_msgSend$blurView
+ _objc_msgSend$bs_removeChildViewController:animated:transitionBlock:
+ _objc_msgSend$contentVisibilityForIcon:metrics:
+ _objc_msgSend$contextMenuManager:orderedActionContextMenuProvidersForIconView:
+ _objc_msgSend$contextMenuManager:preferredMenuElementOrderForIconView:
+ _objc_msgSend$didDelayInsertingCustomImageViewDueToParentController
+ _objc_msgSend$endingContainerView
+ _objc_msgSend$enumerateGridCellIndexesNotContainedInGridRange:usingBlock:
+ _objc_msgSend$folderView:iconListView:willConfigureIconView:forIcon:
+ _objc_msgSend$getIndexes:maxCount:inIndexRange:
+ _objc_msgSend$gridCellIndexesForIconsIntersectingGridRange:gridCellInfo:
+ _objc_msgSend$gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridCellIndexes:gridCellInfo:gridCellInfoOptions:mutationOptions:
+ _objc_msgSend$hasAssertionForLowResolutionSnapshotPresentationMode
+ _objc_msgSend$hasAssertionForSnapshotPresentationMode
+ _objc_msgSend$hasNonDefaultSizeClassIcons
+ _objc_msgSend$hasPlaceholderIcons
+ _objc_msgSend$iconContentVisibility
+ _objc_msgSend$iconFadeAnimator:wantsToApplyAlpha:
+ _objc_msgSend$iconManager:preferredMenuElementOrderForIconView:
+ _objc_msgSend$iconViewUserVisibilityStatusForContentVisibility:
+ _objc_msgSend$indexPassingTest:
+ _objc_msgSend$initWithBlurRadius:
+ _objc_msgSend$initWithGridSizeClass:iconImageInfo:applicationName:logIdentifier:
+ _objc_msgSend$initWithQueue:
+ _objc_msgSend$initWithTraitOverridableObjects:iconListViews:additionalIconViews:
+ _objc_msgSend$isOpaque
+ _objc_msgSend$largestGridSizeClass
+ _objc_msgSend$logIdentifier
+ _objc_msgSend$makeBackgroundView
+ _objc_msgSend$orderedActionContextMenuProvidersForIconView:
+ _objc_msgSend$overrideParentViewControllerForCustomIconImageViewController
+ _objc_msgSend$pageControlOverrideUserInterfaceStyle
+ _objc_msgSend$pageViewControllerForPageIndex:
+ _objc_msgSend$parentViewControllerForCustomIconImageViewController
+ _objc_msgSend$pauseLightAngleUpdatesForIconLayer:
+ _objc_msgSend$performBatchUpdate:
+ _objc_msgSend$performBatchedUpdate:
+ _objc_msgSend$presentationModeFolderContext
+ _objc_msgSend$removeMenuForIdentifier:
+ _objc_msgSend$sbh_didExitIconView
+ _objc_msgSend$sbh_setDidExitIconView:
+ _objc_msgSend$setBlurRadius:
+ _objc_msgSend$setDidDelayInsertingCustomImageViewDueToParentController:
+ _objc_msgSend$setHasAssertionForLowResolutionSnapshotPresentationMode:
+ _objc_msgSend$setHasAssertionForSnapshotPresentationMode:
+ _objc_msgSend$setHasPlaceholderIcons:
+ _objc_msgSend$setHighlightsDisplayAngle:
+ _objc_msgSend$setOverrideParentViewControllerForCustomIconImageViewController:
+ _objc_msgSend$setPendingIcon:
+ _objc_msgSend$setPresentationModeFolderContext:
+ _objc_msgSend$setUsesGlass:
+ _objc_msgSend$shouldUpdateLight
+ _objc_msgSend$showsLabelsForScreenType:iconLocation:layoutOptions:
+ _objc_msgSend$simpleInsertionIconIndexForGridCellIndex:
+ _objc_msgSend$startingContainerView
+ _objc_msgSend$swapViewControllersAndClearEnding
+ _objc_msgSend$symbolName
+ _objc_msgSend$updateAppearStateForViewController:forContentVisibility:
+ _objc_msgSend$updateContentVisibilityOnCurrentImageView
+ _objc_msgSend$updateGlass
+ _objc_msgSend$updateHasPlaceholderIcons
+ _objc_msgSend$updatePresentationModeFolderContextForIconView:
+ _objc_msgSend$usesGlass
- +[SBIconView activateShortcut:withBundleIdentifier:forIconView:]
- +[SBIconView activateShortcut:withBundleIdentifier:forIconView:].cold.1
- +[SBIconView activateShortcut:withBundleIdentifier:forIconView:].cold.2
- +[SBIconView applicationShortcutService]
- +[SBIconView applicationShortcutService].cold.1
- +[UITraitCollection(SpringBoardHome) sbh_traitCollectionWithIconTintColor:]
- +[UITraitCollection(SpringBoardHome) sbh_traitCollectionWithIconTintColor:userInterfaceStyle:]
- -[SBFolderController _removePageViewControllerAppearStateOverrideAssertion:]
- -[SBFolderController beginOverridingPageViewControllerAppearanceStateToRemainDisappearedForReason:]
- -[SBFolderController iconImageViewControllerPresentationModeForIconView:]
- -[SBFolderController iconListView:didAddIconView:].cold.2
- -[SBFolderController iconListView:didRemoveIconView:].cold.3
- -[SBFolderController iconListView:didRemoveIconView:].cold.4
- -[SBFolderController iconListView:didRemoveIconView:].cold.5
- -[SBFolderController isOverridingPageViewControllerAppearanceStateToRemainDisappeared]
- -[SBFolderController shouldViewControllersAppearVisibleForListView:]
- -[SBHIconImageVariantCache _variantImageForIcon:imageAppearance:extraImageOptions:options:].cold.1
- -[SBHIconManager containerViewForPresentingContextMenuForIconView:]
- -[SBHIconManager icon:touchMoved:]
- -[SBHIconManager iconView:willUseContextMenuStyle:]
- -[SBHIconManager iconViewShortcutsPresentationDidCancel:]
- -[SBHIconManager iconViewShortcutsPresentationWillBegin:]
- -[SBHIconManager iconViewShortcutsPresentationWillFinish:]
- -[SBHIconManager iconViewShouldBeginShortcutsPresentation:]
- -[SBHIconStylePreviewManager folderIconImageCache]
- -[SBHIconStylePreviewManager iconImageCache]
- -[SBHIconStylePreviewManager initWithTraitOverridableObjects:iconListViews:additionalIconViews:iconImageCache:folderIconImageCache:]
- -[SBHIconViewContextMenuManager orderedActionContextMenuProviders]
- -[SBHLibraryCategoryStackView _userInterfaceStyleDidChange]
- -[SBHLibraryCategoryStackView backgroundViewForIndex:compatibleWithTraitCollection:]
- -[SBHLibraryViewController shortcutsDelegateForIconView:]
- -[SBHMultiplexingViewController viewWillAppear:]
- -[SBHRecentsDocumentExtensionProvider canProvidePreviewContentForIconView:atLocation:]
- -[SBHRecentsDocumentExtensionProvider canShowRecentsDocumentExtensionProviderForBundleIdentifier:]
- -[SBHRecentsDocumentExtensionProvider previewContentForIconView:atLocation:]
- -[SBHRecentsDocumentExtensionProvider previewType]
- -[SBHRecentsDocumentExtensionProvider setUniqueIdentifier:]
- -[SBHRecentsDocumentExtensionProvider uniqueIdentifier]
- -[SBHStackConfigurationViewController shortcutsDelegateForIconView:]
- -[SBHTodayViewController _updatePresentationModeForIconViews]
- -[SBHWidgetContainerView initWithGridSizeClass:iconImageInfo:applicationName:]
- -[SBHWidgetViewController _invalidateBackgroundingAssertion:]
- -[SBHWidgetViewController acquirePreventSceneBackgroundingAssertionForReason:]
- -[SBHWidgetViewController setPresentationMode:]
- -[SBHWidgetViewController viewDidDisappear:]
- -[SBHWidgetViewController viewWillAppear:]
- -[SBHWidgetWrapperViewController _updateAvocadoHostViewController]
- -[SBHWidgetWrapperViewController _updateAvocadoHostViewController].cold.1
- -[SBIconListModelQueuedMovement .cxx_destruct]
- -[SBIconListModelQueuedMovement description]
- -[SBIconListModelQueuedMovement setDisplacingIconGridRanges:]
- -[SBIconListModelQueuedMovement setIcon:]
- -[SBIconListView _updateVisibleIconViewsWithOldVisibleGridCellIndexes:oldPrefetchedGridCellIndexes:metrics:]
- -[SBIconListView overrideIconImageAppearance]
- -[SBIconListView overrideIconImageStyleConfiguration]
- -[SBIconListView setOverrideIconImageAppearance:]
- -[SBIconListView setOverrideIconImageStyleConfiguration:]
- -[SBIconView _configureResizeAction:forGridSizeClass:withSelectedGridSizeClass:withIconSupportedGridSizeClasses:]
- -[SBIconView _hasPopover]
- -[SBIconView customIconImageViewControllerPresentationMode]
- -[SBIconView recentsDocumentExtensionProvider]
- -[SBIconView setCustomIconImageViewControllerPresentationMode:]
- -[SBIconView shortcutsDelegate]
- -[SBIconView shouldActivateApplicationShortcutItem:atIndex:]
- -[SBIconViewCustomImageViewController .cxx_destruct]
- -[SBIconViewCustomImageViewController _configureBackgroundViewIfNecessary:]
- -[SBIconViewCustomImageViewController _configureBackgroundViewIfNecessary]
- -[SBIconViewCustomImageViewController _createBackgroundViewIfNecessary:]
- -[SBIconViewCustomImageViewController _createBackgroundView]
- -[SBIconViewCustomImageViewController _needsBackgroundView]
- -[SBIconViewCustomImageViewController _setupStateCapture]
- -[SBIconViewCustomImageViewController _teardownBackgroundView:]
- -[SBIconViewCustomImageViewController _teardownBackgroundView]
- -[SBIconViewCustomImageViewController _teardownStateCapture]
- -[SBIconViewCustomImageViewController _updateEdgeAntialiasing]
- -[SBIconViewCustomImageViewController backdropGroupNameForActiveDataSource:]
- -[SBIconViewCustomImageViewController backgroundViewConfigurator]
- -[SBIconViewCustomImageViewController backgroundViewProvider]
- -[SBIconViewCustomImageViewController backgroundView]
- -[SBIconViewCustomImageViewController contentViewController]
- -[SBIconViewCustomImageViewController contentView]
- -[SBIconViewCustomImageViewController continuousCornerRadius]
- -[SBIconViewCustomImageViewController dealloc]
- -[SBIconViewCustomImageViewController evaluateBackground]
- -[SBIconViewCustomImageViewController forcesEdgeAntialiasing]
- -[SBIconViewCustomImageViewController iconImageInfo]
- -[SBIconViewCustomImageViewController icon]
- -[SBIconViewCustomImageViewController initWithContentViewController:]
- -[SBIconViewCustomImageViewController setBackgroundView:]
- -[SBIconViewCustomImageViewController setBackgroundViewConfigurator:]
- -[SBIconViewCustomImageViewController setBackgroundViewProvider:]
- -[SBIconViewCustomImageViewController setContentViewController:]
- -[SBIconViewCustomImageViewController setForcesEdgeAntialiasing:]
- -[SBIconViewCustomImageViewController setIconImageInfo:]
- -[SBIconViewCustomImageViewController setShowsSquareCorners:]
- -[SBIconViewCustomImageViewController showsSquareCorners]
- -[SBIconViewCustomImageViewController snapshotViewScaleFactor]
- -[SBIconViewCustomImageViewController snapshotView]
- -[SBIconViewCustomImageViewController sourceView]
- -[SBIconViewCustomImageViewController viewDidDisappear:]
- -[SBIconViewCustomImageViewController viewDidLayoutSubviews]
- -[SBIconViewCustomImageViewController viewDidLoad]
- -[SBIconViewCustomImageViewController viewWillAppear:]
- -[SBIconViewCustomImageViewController visibleBounds]
- -[SBIconViewCustomImageViewController(SBHWidgetUtilitiesInternal) sbh_isCustomIconImageViewController]
- -[SBIconViewCustomImageViewController(SBHWidgetUtilitiesInternal) sbh_underlyingAvocadoHostViewControllers]
- -[SBRootFolderController recentsDocumentExtensionProvider]
- -[SBRootFolderController setRecentsDocumentExtensionProvider:]
- -[SBRootFolderController viewControllersForPageIndex:]
- -[SBWidgetIconResizeTransitionViewController endingBlurView]
- -[SBWidgetIconResizeTransitionViewController setEndingBlurView:]
- -[SBWidgetIconResizeTransitionViewController setStartingBlurView:]
- -[SBWidgetIconResizeTransitionViewController startingBlurView]
- -[SBWidgetIconResizeTransitionViewController swapViewControllers]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion .cxx_destruct]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion dealloc]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion descriptionBuilderWithMultilinePrefix:]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion descriptionWithMultilinePrefix:]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion folderController]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion initWithFolderController:reason:]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion invalidate]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion isInvalidated]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion reason]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion setInvalidated:]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion succinctDescriptionBuilder]
- -[_SBFolderControllerPageViewControllerAppearStateOverrideAssertion succinctDescription]
- GCC_except_table1025
- GCC_except_table1048
- GCC_except_table121
- GCC_except_table143
- GCC_except_table158
- GCC_except_table182
- GCC_except_table185
- GCC_except_table204
- GCC_except_table207
- GCC_except_table210
- GCC_except_table225
- GCC_except_table233
- GCC_except_table239
- GCC_except_table244
- GCC_except_table255
- GCC_except_table273
- GCC_except_table28
- GCC_except_table280
- GCC_except_table297
- GCC_except_table309
- GCC_except_table332
- GCC_except_table333
- GCC_except_table337
- GCC_except_table341
- GCC_except_table350
- GCC_except_table362
- GCC_except_table377
- GCC_except_table387
- GCC_except_table393
- GCC_except_table396
- GCC_except_table399
- GCC_except_table400
- GCC_except_table407
- GCC_except_table429
- GCC_except_table431
- GCC_except_table447
- GCC_except_table450
- GCC_except_table471
- GCC_except_table473
- GCC_except_table485
- GCC_except_table505
- GCC_except_table510
- GCC_except_table511
- GCC_except_table532
- GCC_except_table542
- GCC_except_table558
- GCC_except_table559
- GCC_except_table570
- GCC_except_table591
- GCC_except_table625
- GCC_except_table657
- GCC_except_table679
- GCC_except_table689
- GCC_except_table692
- GCC_except_table705
- GCC_except_table707
- GCC_except_table709
- GCC_except_table714
- GCC_except_table716
- GCC_except_table718
- GCC_except_table729
- GCC_except_table732
- GCC_except_table740
- GCC_except_table742
- GCC_except_table826
- GCC_except_table882
- GCC_except_table93
- GCC_except_table952
- GCC_except_table972
- GCC_except_table989
- _DOCShouldApplicationShowRecentsPopover
- _OBJC_CLASS_$_SBIconListModelQueuedMovement
- _OBJC_CLASS_$_SBIconViewCustomImageViewController
- _OBJC_CLASS_$__SBFolderControllerPageViewControllerAppearStateOverrideAssertion
- _OBJC_IVAR_$_SBFolderController._appearanceTransitioningCustomImageViewControllers
- _OBJC_IVAR_$_SBFolderController._pageViewControllerAppearStateOverrideAssertions
- _OBJC_IVAR_$_SBFolderIconImageView._transitionToken
- _OBJC_IVAR_$_SBHIconStylePreviewManager._folderIconImageCache
- _OBJC_IVAR_$_SBHIconStylePreviewManager._iconImageCache
- _OBJC_IVAR_$_SBHRecentsDocumentExtensionProvider._uniqueIdentifier
- _OBJC_IVAR_$_SBHWidgetViewController._isInvalidatingBackgroundAssertion
- _OBJC_IVAR_$_SBHWidgetViewController._pendingAppearanceStateChange
- _OBJC_IVAR_$_SBHWidgetViewController._pendingStaticMode
- _OBJC_IVAR_$_SBHWidgetViewController._preventBackgroundingAssertions
- _OBJC_IVAR_$_SBIconListModelQueuedMovement._displacedIcons
- _OBJC_IVAR_$_SBIconListModelQueuedMovement._displacingIconGridRanges
- _OBJC_IVAR_$_SBIconListModelQueuedMovement._gridCellInfo
- _OBJC_IVAR_$_SBIconListModelQueuedMovement._icon
- _OBJC_IVAR_$_SBIconListModelQueuedMovement._movedIcons
- _OBJC_IVAR_$_SBIconListModelQueuedMovement._targetGridCellIndex
- _OBJC_IVAR_$_SBIconListView._overrideIconImageAppearance
- _OBJC_IVAR_$_SBIconListView._overrideIconImageStyleConfiguration
- _OBJC_IVAR_$_SBIconView._paused
- _OBJC_IVAR_$_SBIconView._reallyHasPopover
- _OBJC_IVAR_$_SBIconView._recentsDocumentExtensionProvider
- _OBJC_IVAR_$_SBIconViewCustomImageViewController._backgroundView
- _OBJC_IVAR_$_SBIconViewCustomImageViewController._backgroundViewConfigurator
- _OBJC_IVAR_$_SBIconViewCustomImageViewController._backgroundViewProvider
- _OBJC_IVAR_$_SBIconViewCustomImageViewController._contentViewController
- _OBJC_IVAR_$_SBIconViewCustomImageViewController._forcesEdgeAntialiasing
- _OBJC_IVAR_$_SBIconViewCustomImageViewController._icon
- _OBJC_IVAR_$_SBIconViewCustomImageViewController._iconImageInfo
- _OBJC_IVAR_$_SBIconViewCustomImageViewController._showsSquareCorners
- _OBJC_IVAR_$_SBIconViewCustomImageViewController._stateCaptureInvalidatable
- _OBJC_IVAR_$_SBRootFolderController._recentsDocumentExtensionProvider
- _OBJC_IVAR_$_SBWidgetIconResizeTransitionViewController._endingBlurView
- _OBJC_IVAR_$_SBWidgetIconResizeTransitionViewController._startingBlurView
- _OBJC_IVAR_$__SBFolderControllerPageViewControllerAppearStateOverrideAssertion._folderController
- _OBJC_IVAR_$__SBFolderControllerPageViewControllerAppearStateOverrideAssertion._invalidated
- _OBJC_IVAR_$__SBFolderControllerPageViewControllerAppearStateOverrideAssertion._reason
- _OBJC_METACLASS_$_SBIconListModelQueuedMovement
- _OBJC_METACLASS_$_SBIconViewCustomImageViewController
- _OBJC_METACLASS_$__SBFolderControllerPageViewControllerAppearStateOverrideAssertion
- _OUTLINED_FUNCTION_16
- __OBJC_$_INSTANCE_METHODS_SBIconListModelQueuedMovement
- __OBJC_$_INSTANCE_METHODS_SBIconViewCustomImageViewController(SBHWidgetUtilitiesInternal)
- __OBJC_$_INSTANCE_METHODS__SBFolderControllerPageViewControllerAppearStateOverrideAssertion
- __OBJC_$_INSTANCE_VARIABLES_SBIconListModelQueuedMovement
- __OBJC_$_INSTANCE_VARIABLES_SBIconViewCustomImageViewController
- __OBJC_$_INSTANCE_VARIABLES__SBFolderControllerPageViewControllerAppearStateOverrideAssertion
- __OBJC_$_PROP_LIST_SBHIconViewContextMenuPreviewProviding
- __OBJC_$_PROP_LIST_SBIconViewCustomImageViewController
- __OBJC_$_PROP_LIST__SBFolderControllerPageViewControllerAppearStateOverrideAssertion
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBHIconViewContextMenuPreviewProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBIconViewShortcutsDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBHIconViewContextMenuPreviewProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBHIconViewContextMenuPreviewProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBIconViewShortcutsDelegate
- __OBJC_$_PROTOCOL_REFS_SBHIconViewContextMenuPreviewProviding
- __OBJC_$_PROTOCOL_REFS_SBIconViewShortcutsDelegate
- __OBJC_CLASS_PROTOCOLS_$_SBIconViewCustomImageViewController
- __OBJC_CLASS_PROTOCOLS_$__SBFolderControllerPageViewControllerAppearStateOverrideAssertion
- __OBJC_CLASS_RO_$_SBIconListModelQueuedMovement
- __OBJC_CLASS_RO_$_SBIconViewCustomImageViewController
- __OBJC_CLASS_RO_$__SBFolderControllerPageViewControllerAppearStateOverrideAssertion
- __OBJC_LABEL_PROTOCOL_$_SBHIconViewContextMenuPreviewProviding
- __OBJC_LABEL_PROTOCOL_$_SBIconViewShortcutsDelegate
- __OBJC_METACLASS_RO_$_SBIconListModelQueuedMovement
- __OBJC_METACLASS_RO_$_SBIconViewCustomImageViewController
- __OBJC_METACLASS_RO_$__SBFolderControllerPageViewControllerAppearStateOverrideAssertion
- __OBJC_PROTOCOL_$_SBHIconViewContextMenuPreviewProviding
- __OBJC_PROTOCOL_$_SBIconViewShortcutsDelegate
- ___106-[SBHWidgetStackViewController _removeWidgetWithUniqueIdentifier:widgetContainerViewControllers:animated:]_block_invoke.86
- ___140-[SBIconListModel _moveContainedIconBySwappingVerticallyWithAdjacentIcons:toGridCellIndex:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke_2
- ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke.1095
- ___157-[SBHIconManager swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:inRootFolder:focusModeIdentifier:]_block_invoke_2.1097
- ___172-[SBIconListModel gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridRange:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke
- ___172-[SBIconListModel gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridRange:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke_2
- ___172-[SBIconListModel gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridRange:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke_2.cold.1
- ___172-[SBIconListModel gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridRange:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke_3
- ___172-[SBIconListModel gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridRange:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke_4
- ___172-[SBIconListModel gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridRange:gridCellInfo:gridCellInfoOptions:mutationOptions:]_block_invoke_5
- ___40+[SBIconView applicationShortcutService]_block_invoke
- ___44-[SBHWidgetViewController viewDidDisappear:]_block_invoke
- ___47-[SBIconView resizeGestureRecognizerDidUpdate:]_block_invoke.788
- ___49-[SBIconListView setOverrideIconImageAppearance:]_block_invoke
- ___51-[SBHIconManager _engageWallpaperTintColorDropper:]_block_invoke.972
- ___54-[SBHWidgetStackViewController _logAllViewControllers]_block_invoke.135
- ___54-[SBHWidgetStackViewController _logAllViewControllers]_block_invoke.135.cold.1
- ___57-[SBIconListView setOverrideIconImageStyleConfiguration:]_block_invoke
- ___57-[SBIconViewCustomImageViewController _setupStateCapture]_block_invoke
- ___57-[SBIconViewCustomImageViewController _setupStateCapture]_block_invoke_2
- ___59-[SBIconListView layoutIconsIfNeededUsingAnimator:options:]_block_invoke.88
- ___59-[SBIconListView layoutIconsIfNeededUsingAnimator:options:]_block_invoke_2.94
- ___61-[SBHTodayViewController _updatePresentationModeForIconViews]_block_invoke
- ___62-[SBIconListView regenerateTemporaryDisplayedModelIfNecessary]_block_invoke.45
- ___62-[SBIconListView regenerateTemporaryDisplayedModelIfNecessary]_block_invoke_2.47
- ___62-[SBIconListView regenerateTemporaryDisplayedModelIfNecessary]_block_invoke_3.48
- ___64+[SBIconView activateShortcut:withBundleIdentifier:forIconView:]_block_invoke
- ___64+[SBIconView activateShortcut:withBundleIdentifier:forIconView:]_block_invoke_2
- ___64+[SBIconView activateShortcut:withBundleIdentifier:forIconView:]_block_invoke_3
- ___64+[SBIconView activateShortcut:withBundleIdentifier:forIconView:]_block_invoke_3.cold.1
- ___74-[SBHWidgetStackViewController _updateWidgetViewsWithAnimationUpdateMode:]_block_invoke_3
- ___74-[SBHWidgetStackViewController _updateWidgetViewsWithAnimationUpdateMode:]_block_invoke_4
- ___75+[UITraitCollection(SpringBoardHome) sbh_traitCollectionWithIconTintColor:]_block_invoke
- ___77-[SBHFileWidgetExtensionProvider filesWidgetViewControllerWithConfiguration:]_block_invoke.149
- ___78-[SBHWidgetViewController acquirePreventSceneBackgroundingAssertionForReason:]_block_invoke
- ___79-[SBHIconManager pushExpandedIcon:location:context:animated:completionHandler:]_block_invoke.535
- ___81-[SBHIconManager replaceApplicationPlaceholderWithApplication:completionHandler:]_block_invoke
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.607
- ___86-[SBHIconManager _loadAndSaveDefaultIntentIfNecessaryForWidget:ofIcon:viewController:]_block_invoke.610
- ___94+[UITraitCollection(SpringBoardHome) sbh_traitCollectionWithIconTintColor:userInterfaceStyle:]_block_invoke
- ___96-[SBHWidgetStackViewController _updateBackgroundViewWithAnimationUpdateMode:allowingOutsetting:]_block_invoke.109
- ___98-[SBHIconViewFileStackConfigurationContextMenuProvider contextMenuSectionsForIconView:atLocation:]_block_invoke.65
- ___98-[SBHIconViewFileStackConfigurationContextMenuProvider contextMenuSectionsForIconView:atLocation:]_block_invoke_2.31
- ___98-[SBHIconViewFileStackConfigurationContextMenuProvider contextMenuSectionsForIconView:atLocation:]_block_invoke_2.78
- ___block_descriptor_112_e8_32s40s48s56s64s72s_e51_v32?0{SBHIconGridRange=Q{SBHIconGridSize=SS}}8^B24ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_169_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_32_e46_v32?0"NSNumber"8"NSMutableDictionary"16^B24l
- ___block_descriptor_32_e59_v32?0"NSString"8"SBHWidgetContainerViewController"16^B24l
- ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e45_v16?0"<SBHIconImageCacheResultDescribing>"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_76_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_81_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.1017
- ___block_literal_global.104
- ___block_literal_global.1056
- ___block_literal_global.1174
- ___block_literal_global.1205
- ___block_literal_global.1227
- ___block_literal_global.134
- ___block_literal_global.219
- ___block_literal_global.243
- ___block_literal_global.2553
- ___block_literal_global.289
- ___block_literal_global.309
- ___block_literal_global.347
- ___block_literal_global.372
- ___block_literal_global.377
- ___block_literal_global.379
- ___block_literal_global.397
- ___block_literal_global.400
- ___block_literal_global.416
- ___block_literal_global.50
- ___block_literal_global.609
- ___block_literal_global.673
- ___block_literal_global.68
- ___block_literal_global.798
- ___block_literal_global.824
- ___block_literal_global.885
- ___block_literal_global.90
- ___block_literal_global.96
- ___block_literal_global.98
- _activateShortcut:withBundleIdentifier:forIconView:.onceToken.76
- _applicationShortcutService._applicationShortcutService
- _applicationShortcutService.onceToken
- _objc_msgSend$_invalidateBackgroundingAssertion:
- _objc_msgSend$_removePageViewControllerAppearStateOverrideAssertion:
- _objc_msgSend$_resetAllPodBackgroundViews
- _objc_msgSend$_updateAvocadoHostViewController
- _objc_msgSend$_updateVisibleIconViewsWithOldVisibleGridCellIndexes:oldPrefetchedGridCellIndexes:metrics:
- _objc_msgSend$_widgetExtensionBundleIdentifier
- _objc_msgSend$backgroundViewForIndex:compatibleWithTraitCollection:
- _objc_msgSend$blurViewWithInputRadius:
- _objc_msgSend$cacheImagesForIcons:prioritizedImageAppearances:reason:options:completionHandler:
- _objc_msgSend$canShowRecentsDocumentExtensionProviderForBundleIdentifier:
- _objc_msgSend$endingBlurView
- _objc_msgSend$enumerateUniqueIconIndexesInGridRange:usingBlock:
- _objc_msgSend$iconImageViewControllerPresentationModeForIconView:
- _objc_msgSend$initWithGridSizeClass:iconImageInfo:applicationName:
- _objc_msgSend$initWithTraitOverridableObjects:iconListViews:additionalIconViews:iconImageCache:folderIconImageCache:
- _objc_msgSend$isOverridingPageViewControllerAppearanceStateToRemainDisappeared
- _objc_msgSend$lastUsedRow
- _objc_msgSend$log:
- _objc_msgSend$orderedActionContextMenuProviders
- _objc_msgSend$recentDocumentExtensionProviderForIconView:
- _objc_msgSend$recentsDocumentExtensionProvider
- _objc_msgSend$recentsDocumentViewControllerForBundleIdentifier:
- _objc_msgSend$sbh_SBHIconGridRangeValue
- _objc_msgSend$sbh_removeObjectsPassingTest:
- _objc_msgSend$sbh_valueWithSBHIconGridRange:
- _objc_msgSend$setCustomIconImageViewControllerPresentationMode:
- _objc_msgSend$setEndingBlurView:
- _objc_msgSend$setStartingBlurView:
- _objc_msgSend$shortcutsDelegate
- _objc_msgSend$shortcutsDelegateForIconView:
- _objc_msgSend$shouldViewControllersAppearVisibleForListView:
- _objc_msgSend$showsPopovers
- _objc_msgSend$startingBlurView
- _objc_msgSend$swapViewControllers
- _objc_msgSend$viewControllersForPageIndex:
- _objc_msgSend$visibleColumnRange
- _objc_msgSend$widgetViewControllerShouldTransitionSceneToBackground:
CStrings:
+ "!A"
+ "%@:%p"
+ "%@:%p [%@]"
+ "%@:%p widget=[%@:%@:%@]"
+ "<%@:%p>"
+ "<%@> updateMode: %@"
+ "<%@> updateMode: %@>"
+ "<%@> updateMode=%@"
+ "<%{public}@:%p> activateWithViewController: <%{public}@:%p>"
+ "<%{public}@:%p> deactivate"
+ "<%{public}@> %{public}s"
+ "<%{public}@> %{public}s. Widget content is ready? %{public}d"
+ "<%{public}@> %{public}s; acquiring 'widgetStack.disableImageUpdates' assertion %{public}@"
+ "<%{public}@> %{public}s; acquiring _imageUpdatesDisabledForContextMenuAssertion"
+ "<%{public}@> %{public}s; acquiring _imageUpdatesDisabledForNewListLayoutProviderAssertion"
+ "<%{public}@> %{public}s; invalidating 'widgetStack.disableImageUpdates' assertion %{public}@"
+ "<%{public}@> %{public}s; invalidating _imageUpdatesDisabledForContextMenuAssertion"
+ "<%{public}@> %{public}s; returning blank source view"
+ "<%{public}@> %{public}s; view controller '%{public}@' didn't exist; we need to remove it now."
+ "<%{public}@> Actually setting presentation mode to: %{public}@"
+ "<%{public}@> Adding SBIconView isDropping assertion: %@"
+ "<%{public}@> Changing active data source from %@ to %@: %@"
+ "<%{public}@> Changing active data source: %@"
+ "<%{public}@> Changing from data souce: %{public}@ to data source:%{public}@."
+ "<%{public}@> Configure new matching icon view: %p"
+ "<%{public}@> Configuring preview for icon '%@' w/ currentImageView '%@' contentContainerView '%@'"
+ "<%{public}@> Content visibility changed to: %{public}@"
+ "<%{public}@> Delegate does not want to handle tap, going to icon. launch enabled: %{BOOL}u"
+ "<%{public}@> Desired presentation mode via visibility: %{public}@"
+ "<%{public}@> Handle tap: modifiers: %lx, delegate: %p, window: %p"
+ "<%{public}@> Icon view s stealing icon image view controller from %{public}@ without anyone borrowing it"
+ "<%{public}@> Invalid SBHWidgetStackScrollView bounds size: %@, widget bounds: %@"
+ "<%{public}@> Not allowing accessory view (badge) tap gesture to begin because delegate said so."
+ "<%{public}@> Not allowing close box tap gesture to begin because delegate said so."
+ "<%{public}@> Not allowing tap gesture to begin because %{public}@"
+ "<%{public}@> Not allowing tap gesture to receive touch because the delegate (%{public}@) said so."
+ "<%{public}@> Overriding presentation mode because asserted low resolution snapshot: %{public}@"
+ "<%{public}@> Overriding presentation mode because asserted snapshot: %{public}@"
+ "<%{public}@> Overriding presentation mode because in configuration transition: %{public}@"
+ "<%{public}@> Overriding presentation mode to snapshot because we're not in a hierarchy: %{public}@"
+ "<%{public}@> Remove SBIconView isDropping assertion: %@"
+ "<%{public}@> Remove borrowedIconImageViewAssertion (custom VC: %{public}@)"
+ "<%{public}@> Removing widget with unique identifier %{public}@"
+ "<%{public}@> Scroll view _restingContentOffset:%@ for pageSize:%@ contentSize:%@"
+ "<%{public}@> Set custom icon view controller to: %@"
+ "<%{public}@> Set new icon from %{public}@ to %{public}@"
+ "<%{public}@> Setting visibility to %{public}s"
+ "<%{public}@> Skipping invalid background view bounds: %@"
+ "<%{public}@> Skipping invalid container view bounds: %@"
+ "<%{public}@> Snapshot view for screenTimeLockoutView was added to snapshotView's hierarchy: %{public}@"
+ "<%{public}@> Snapshot view requested for widget: %{public}@"
+ "<%{public}@> Touches began with event: %{public}@, tap gesture: %{public}@"
+ "<%{public}@> Unable to generate targeted preview, currentImageView is nil."
+ "<%{public}@> Unable to generate targeted preview, the view associated with the interaction was foreign."
+ "<%{public}@> Unable to set presentation mode bc customImageViewController doesn't allow setting presentation mode: %{public}@"
+ "<%{public}@> Unknown subview found in SBIconView when preparing for reuse! (53825790) %{public}@ %@"
+ "<%{public}@> Update presentation mode (%@) for widget view controllers: %@"
+ "<%{public}@> Updating blockedForScreenTimeExpiration to %{BOOL}u"
+ "<%{public}@> Widget configuration did begin"
+ "<%{public}@> Widget configuration did commit"
+ "<%{public}@> Widget configuration did end"
+ "<%{public}@> Widget configuration will begin"
+ "<%{public}@> Widget configuration will end"
+ "<%{public}@> [ViewControllerDebug] Beginning view controller enumeration ------------------------------------------"
+ "<%{public}@> [ViewControllerDebug] layout options %lu"
+ "<%{public}@> [ViewControllerDebug] widgetUniqueIdentifier: %@"
+ "<%{public}@> _updateWidgetViewsWithAnimationUpdateMode: CREATED widget VC in stack: widget=%@, %@"
+ "<%{public}@> _updateWidgetViewsWithAnimationUpdateMode: REMOVE container VC: %@, widget=%@"
+ "<%{public}@> _updateWidgetViewsWithAnimationUpdateMode: activeWidgetIndex: %@"
+ "<%{public}@> _updateWidgetViewsWithAnimationUpdateMode: relativeIndex: %@, minRelativeIndex: %@, maxRelativeIndex: %@"
+ "<%{public}@> borrowIconImageViewWithOptions (custom VC: %@)"
+ "<%{public}@> configureBorrowingIconImageViewFromIconView: fromIconView=%p"
+ "<%{public}@> create container view controller for widget: %@"
+ "<%{public}@> didChangeActiveDataSource:%{public}@"
+ "<%{public}@> iconListLayoutProvider changed to <%{public}@>"
+ "<%{public}@> received new iconListLayoutProvider. canReuseViewControllerFromLastFullyRenderedLayoutProvider: %{public}d"
+ "<%{public}@> viewDidAppear"
+ "<%{public}@> viewDidDisappear"
+ "<%{public}@> viewDidMoveToWindow (hasWindow=%@)"
+ "<%{public}@> viewIsAppearing"
+ "<%{public}@> viewWillAppear"
+ "<%{public}@> viewWillDisappear"
+ "<%{public}@>Unable to generate targeted preview, not contained within a window."
+ "<SBHWidget:%p [%@:%@]>"
+ "<SBHWidgetStack:%p count=%ld, activeWidget=%@>"
+ "<SBHWidgetStack:%p count=%ld>"
+ "<SBHWidgetStackScrollView:%@> received invalid contentOffset:%@"
+ "<SBHWidgetViewController:%p> Error waiting for non-placeholder content to appear: %{public}@"
+ "<SBLeafIcon:%p [%@]>"
+ "@\"AEAssessmentModeGestalt\""
+ "@\"NSArray\"32@0:8@\"SBHIconViewContextMenuManager\"16@\"SBIconView\"24"
+ "@\"SBHPresentationModeFolderContext\""
+ "@\"SBWidgetIconResizeBackdropView\""
+ "@\"SBWidgetIconResizeContainerView\""
+ "@\"UIView<SBIconFadeAnimatorCrossfadeView>\""
+ "@56@0:8@16@24@32Q40Q48"
+ "@64@0:8@16Q24@32@40Q48Q56"
+ "@72@0:8@16{SBIconImageInfo={CGSize=dd}dd}24@56@64"
+ "AssessmentMode"
+ "AssessmentMode %{BOOL}d -> %{BOOL}d"
+ "B24@?0Q8^B16"
+ "B40@0:8Q16@24Q32"
+ "Couldn't put icon into the pocket list model (%@)"
+ "Failed to initalize AssessmentModeGestalt"
+ "Initalized AssessmentModeGestalt"
+ "Live"
+ "LiveSnapshot"
+ "SBAssessmentModeMonitor"
+ "SBHIconViewTouchDidExitKey"
+ "SBHMutablePresentationModeFolderContext"
+ "SBHPresentationModeFolderContext"
+ "SBHWidgetAddGalleryWidgetViewController"
+ "SBIconFadeAnimatorCrossfadeView"
+ "SBIconViewCustomImageViewControlling_Internal"
+ "SBIconViewUtilities"
+ "SBWidgetIconResizeContainerView"
+ "Static"
+ "T@\"AEAssessmentModeGestalt\",&,N,V_assessmentModeGestalt"
+ "T@\"NSArray\",R,C,N,V_effectiveApplicationShortcutItems"
+ "T@\"NSString\",R,N,V_logIdentifier"
+ "T@\"SBWidgetIconResizeBackdropView\",R,N,V_blurView"
+ "T@\"SBWidgetIconResizeContainerView\",&,N,V_endingContainerView"
+ "T@\"SBWidgetIconResizeContainerView\",&,N,V_startingContainerView"
+ "T@\"UIViewController\",&,N,V_overrideParentViewControllerForCustomIconImageViewController"
+ "TB,N,Ssbh_setDidExitIconView:"
+ "TB,N,V_hasPlaceholderIcons"
+ "TB,N,V_usesGlass"
+ "TB,R,N,V_hasAssertionForLowResolutionSnapshotPresentationMode"
+ "TB,R,N,V_hasAssertionForSnapshotPresentationMode"
+ "TQ,N,V_imageLoadingBehavior"
+ "Td,N,V_blurRadius"
+ "Tq,N,V_presentationMode"
+ "T{CGSize=dd},R,N,V_contentSize"
+ "Unknown"
+ "_assessmentModeGestalt"
+ "_blurRadius"
+ "_chuisWidgetPresentationModeFromIconPresentationMode:"
+ "_didDelayInsertingCustomImageViewDueToParentController"
+ "_effectiveApplicationShortcutItems"
+ "_effectivePresentationMode"
+ "_endingContainerView"
+ "_hasAssertionForLowResolutionSnapshotPresentationMode"
+ "_hasAssertionForSnapshotPresentationMode"
+ "_hasPlaceholderIcons"
+ "_iconImageLoadContext"
+ "_inConfigurationTransition"
+ "_initWithContext:"
+ "_layoutGenerationCount"
+ "_logIdentifier"
+ "_overrideParentViewControllerForCustomIconImageViewController"
+ "_pendingIcon"
+ "_presentationModeDirty"
+ "_presentationModeFolderContext"
+ "_reevaluateLogIdentifier"
+ "_requestedPresentationMode"
+ "_startingContainerView"
+ "_updateContentViewControllerPresentationMode"
+ "_updateEffectivePresentationMode"
+ "_updatePresentationModeContextForIconViews"
+ "_updatePresentationModeForReason:"
+ "_updateVisibleIconViewsWithOldCellVisibility:oldVisibleGridCellIndexes:oldPrefetchedGridCellIndexes:metrics:"
+ "_updateWidgetHostViewController"
+ "_usesGlass"
+ "_variantImageForIcon:imageAppearance:context:extraImageOptions:options:"
+ "appClips"
+ "assessmentModeGestalt"
+ "attachedToHierarchy"
+ "blurRadius"
+ "blurView"
+ "bs_removeChildViewController:animated:transitionBlock:"
+ "buildMenuWithBuilder:"
+ "configuration did end"
+ "configuration will begin"
+ "configuration will end"
+ "content visibility changed"
+ "contentVisibilityForIcon:metrics:"
+ "contextMenuManager:orderedActionContextMenuProvidersForIconView:"
+ "contextMenuManager:preferredMenuElementOrderForIconView:"
+ "didDelayInsertingCustomImageViewDueToParentController"
+ "displayedIconViewForCoordinate:"
+ "displayedIconViewForGridCellIndex:"
+ "endingContainerView"
+ "enumerateGridCellIndexesNotContainedInGridRange:usingBlock:"
+ "folderView:iconListView:willConfigureIconView:forIcon:"
+ "getIndexes:maxCount:inIndexRange:"
+ "gridCellIndexesForIconsIntersectingGridRange:gridCellInfo:"
+ "gridCellIndexesForIconsIntersectingGridRange:gridCellInfoOptions:"
+ "gridCellIndexesNotContainedInGridRange:"
+ "gridCellInfoByUsingBruteForcedTwoDimensionalMovementToInsertIcon:atGridCellIndex:constrainedToGridCellIndexes:gridCellInfo:gridCellInfoOptions:mutationOptions:"
+ "hasAssertionForLowResolutionSnapshotPresentationMode"
+ "hasAssertionForSnapshotPresentationMode"
+ "hasPlaceholderIcons"
+ "icon image view added to window"
+ "iconContentVisibility"
+ "iconFadeAnimator:wantsToApplyAlpha:"
+ "iconManager:preferredMenuElementOrderForIconView:"
+ "iconViewUserVisibilityStatusForContentVisibility:"
+ "iconViewUserVisibilityStatusForIcon:"
+ "indexPassingTest:"
+ "initWithBlurRadius:"
+ "initWithGridSizeClass:iconImageInfo:applicationName:logIdentifier:"
+ "initWithQueue:"
+ "initWithTraitOverridableObjects:iconListViews:additionalIconViews:"
+ "layoutGenerationCount"
+ "logIdentifier"
+ "makeBackgroundView"
+ "new folder context"
+ "orderedActionContextMenuProvidersForIconView:"
+ "overrideParentViewControllerForCustomIconImageViewController"
+ "pageControlOverrideUserInterfaceStyle"
+ "pageViewControllerForPageIndex:"
+ "parentViewControllerForCustomIconImageViewController"
+ "pauseLightAngleUpdatesForIconLayer:"
+ "pendingIcon"
+ "performBatchUpdate:"
+ "performBatchedUpdate:"
+ "presentationModeFolderContext"
+ "q32@0:8@\"SBHIconViewContextMenuManager\"16@\"SBIconView\"24"
+ "removeMenuForIdentifier:"
+ "sbh_didExitIconView"
+ "sbh_setDidExitIconView:"
+ "set custom icon image view controller2"
+ "setAssessmentModeGestalt:"
+ "setBlurRadius:"
+ "setDidDelayInsertingCustomImageViewDueToParentController:"
+ "setEndingContainerView:"
+ "setHasAssertionForLowResolutionSnapshotPresentationMode:"
+ "setHasAssertionForSnapshotPresentationMode:"
+ "setHasPlaceholderIcons:"
+ "setHighlightsDisplayAngle:"
+ "setOverrideParentViewControllerForCustomIconImageViewController:"
+ "setPendingIcon:"
+ "setPresentationModeFolderContext:"
+ "setStartingContainerView:"
+ "setUsesGlass:"
+ "shouldUpdateLight"
+ "shouldViewControllersAppearVisibleForIconView:"
+ "showsLabelsForScreenType:iconLocation:layoutOptions:"
+ "simpleInsertionIconIndexForGridCellIndex:"
+ "startingContainerView"
+ "swapViewControllersAndClearEnding"
+ "symbolName"
+ "updateAppearStateForViewController:forContentVisibility:"
+ "updateContentVisibilityOnCurrentImageView"
+ "updateGlass"
+ "updateHasPlaceholderIcons"
+ "updatePresentationModeFolderContextForIconView:"
+ "usesGlass"
+ "v32@0:8@\"SBIconFadeAnimator\"16d24"
+ "v48@0:8@\"SBFolderView\"16@\"SBIconListView\"24@\"SBIconView\"32@\"SBIcon\"40"
+ "v48@0:8q16@24@32@40"
+ "viewIsAppearing:"
+ "visible (transitioning)"
+ "\xf0!b"
+ "\xf0QA"
+ "\xf0b"
- "!1"
- "%p: Adding SBIconView isDropping assertion: %@"
- "%p: Remove SBIconView isDropping assertion: %@"
- "%{public}s Error waiting for non-placeholder content to appear: %{public}@"
- "-[SBHMultiplexingViewController activateWithViewController:]"
- "-[SBHMultiplexingViewController deactivate]"
- "-[SBHWidgetStackViewController viewDidAppear:]"
- "-[SBHWidgetStackViewController viewDidDisappear:]"
- "-[SBHWidgetStackViewController viewDidMoveToWindow:shouldAppearOrDisappear:]"
- "-[SBHWidgetStackViewController viewWillAppear:]"
- "-[SBHWidgetStackViewController viewWillDisappear:]"
- "-[SBHWidgetViewController waitForContentReadyWithTimeout:completion:]_block_invoke"
- "<%@: %p updateMode: %@>"
- "<%@: %p, %@, %lu>"
- "<%{public}@:%p> %s"
- "<%{public}@:%p> %s <%{public}@:%p>"
- "<%{public}@:%p> %s. Widget content is ready? %{public}d"
- "<%{public}@:%p> %s; acquiring 'widgetStack.disableImageUpdates' assertion %{public}@"
- "<%{public}@:%p> %s; acquiring _imageUpdatesDisabledForContextMenuAssertion"
- "<%{public}@:%p> %s; acquiring _imageUpdatesDisabledForNewListLayoutProviderAssertion"
- "<%{public}@:%p> %s; invalidating 'widgetStack.disableImageUpdates' assertion %{public}@"
- "<%{public}@:%p> %s; invalidating _imageUpdatesDisabledForContextMenuAssertion"
- "<%{public}@:%p> %s; returning blank source view"
- "<%{public}@:%p> %s; view controller '%{public}@' didn't exist; we need to remove it now."
- "<%{public}@:%p> iconListLayoutProvider changed to <%{public}@>"
- "<%{public}@:%p> leafIcon:%{public}@ didChangeActiveDataSource:%{public}@"
- "<%{public}@:%p>; received new iconListLayoutProvider. canReuseViewControllerFromLastFullyRenderedLayoutProvider: %{public}d"
- "@\"<SBIconViewShortcutsDelegate>\"24@0:8@\"SBIconView\"16"
- "@\"SBHRecentsDocumentExtensionProvider\""
- "@\"SBHRecentsDocumentExtensionProvider\"24@0:8@\"SBIconView\"16"
- "@\"UIViewController\"40@0:8@\"SBIconView\"16{CGPoint=dd}24"
- "Begin overriding page view controller appearance state for reason: %{public}@"
- "Beginning appearance transition of %p to NO (beginOverridingPageViewControllerAppearanceStateToRemainDisappearedForReason)"
- "Beginning appearance transition of %p to NO (didRemoveIconView)"
- "Beginning appearance transition of %p to NO (folderViewWillBeginScrolling)"
- "Beginning appearance transition of %p to YES (_removePageViewControllerAppearStateOverrideAssertion)"
- "C$"
- "Changing active data source from %@ to %@: %@"
- "Changing active data source: %@"
- "Changing from data souce: %{public}@ to data source:%{public}@."
- "Denied transition to Static due to assertions."
- "End overriding page view controller appearance state for reason: %{public}@"
- "Ending appearance transition of %p to %{BOOL}u (didAddIconView)"
- "Ending appearance transition of %p to NO (beginOverridingPageViewControllerAppearanceStateToRemainDisappearedForReason)"
- "Ending appearance transition of %p to NO (didRemoveIconView)"
- "Ending appearance transition of %p to YES (_removePageViewControllerAppearStateOverrideAssertion)"
- "Handle tap: %@, modifiers: %lx, delegate: %p, window: %p"
- "Icon view %@ is stealing icon image view controller from %@ without anyone borrowing it"
- "Invalid SBHWidgetStackScrollView bounds size: %@, widget bounds: %@"
- "Invalidating preventSceneBackgroundingAssertion '%@'"
- "Last prevent scene background assertion invalidated.  Adjusting now to static mode."
- "New preventSceneBackgroundingAssertion acquired: %@"
- "Not allowing accessory view (badge) tap gesture to begin because delegate said so."
- "Not allowing close box tap gesture to begin because delegate said so."
- "Not allowing tap gesture to begin because %{public}@"
- "Not allowing tap gesture to receive touch because the delegate (%{public}@) said so."
- "Preventing transition to background; adding new preventBackgroundingAssertion; now %lu"
- "Removing widget with unique identifier %{public}@"
- "SBHIconViewContextMenuPreviewProviding"
- "SBHWidgetContainerViewController %{public}@ -- Snapshot view for screenTimeLockoutView was added to snapshotView's hierarchy: %{public}@"
- "SBHWidgetContainerViewController %{public}@ -- Snapshot view requested for widget: %{public}@"
- "SBHWidgetContainerViewController %{public}@ -- viewDidAppear"
- "SBHWidgetContainerViewController %{public}@ -- viewDidDisappear"
- "SBHWidgetContainerViewController %{public}@ -- viewWillAppear"
- "SBHWidgetContainerViewController %{public}@ -- viewWillDisappear"
- "SBHWidgetStackScrollView _restingContentOffset:%@ for pageSize:%@ contentSize:%@"
- "SBHWidgetStackScrollView:%@ received invalid contentOffset:%@"
- "SBIconListModelQueuedMovement"
- "SBIconView touches began with event: %{public}@, tap gesture: %{public}@"
- "SBIconViewCustomImageViewController"
- "SBIconViewShortcutsDelegate"
- "Setting visibility of widget %{public}@ to %{public}s"
- "Skipping invalid background view bounds: %@"
- "Skipping invalid container view bounds: %@"
- "T@\"SBHRecentsDocumentExtensionProvider\",&,N,V_recentsDocumentExtensionProvider"
- "T@\"UIView\",&,N,V_endingBlurView"
- "T@\"UIView\",&,N,V_startingBlurView"
- "TB,R,N,GisOverridingPageViewControllerAppearanceStateToRemainDisappeared"
- "Tq,?,N"
- "Tq,?,N,V_presentationMode"
- "Unknown subview found in SBIconView when preparing for reuse! (53825790) %{public}@ %@"
- "Updating blockedForScreenTimeExpiration to %{BOOL}u"
- "[ViewControllerDebug] Beginning view controller enumeration ------------------------------------------"
- "[ViewControllerDebug] layout options %lu"
- "[ViewControllerDebug] widgetUniqueIdentifier: %@"
- "_SBFolderControllerPageViewControllerAppearStateOverrideAssertion"
- "_appearanceTransitioningCustomImageViewControllers"
- "_configureResizeAction:forGridSizeClass:withSelectedGridSizeClass:withIconSupportedGridSizeClasses:"
- "_displacedIcons"
- "_displacingIconGridRanges"
- "_endingBlurView"
- "_hasPopover"
- "_invalidateBackgroundingAssertion:"
- "_isInvalidatingBackgroundAssertion"
- "_pageViewControllerAppearStateOverrideAssertions"
- "_pendingAppearanceStateChange"
- "_pendingStaticMode"
- "_preventBackgroundingAssertions"
- "_reallyHasPopover"
- "_recentsDocumentExtensionProvider"
- "_removePageViewControllerAppearStateOverrideAssertion:"
- "_startingBlurView"
- "_targetGridCellIndex"
- "_updateAvocadoHostViewController"
- "_updateVisibleIconViewsWithOldVisibleGridCellIndexes:oldPrefetchedGridCellIndexes:metrics:"
- "acquirePreventSceneBackgroundingAssertionForReason:"
- "applicationBundleURLForShortcutsWithIconView:"
- "applicationShortcutService"
- "backgroundViewForIndex:compatibleWithTraitCollection:"
- "beginOverridingPageViewControllerAppearanceStateToRemainDisappearedForReason:"
- "canProvidePreviewContentForIconView:atLocation:"
- "canShowRecentsDocumentExtensionProviderForBundleIdentifier:"
- "circle"
- "customIconImageViewControllerPresentationMode"
- "delegate does not want to handle tap, going to icon. launch enabled: %{BOOL}u"
- "endingBlurView"
- "iconImageViewControllerPresentationModeForIconView:"
- "iconViewShortcutsPresentationDidCancel:"
- "iconViewShortcutsPresentationDidFinish:"
- "iconViewShortcutsPresentationWillBegin:"
- "iconViewShortcutsPresentationWillFinish:"
- "initWithGridSizeClass:iconImageInfo:applicationName:"
- "initWithTraitOverridableObjects:iconListViews:additionalIconViews:iconImageCache:folderIconImageCache:"
- "isOverridingPageViewControllerAppearanceStateToRemainDisappeared"
- "log:"
- "orderedActionContextMenuProviders"
- "overridingPageViewControllerAppearanceStateToRemainDisappeared"
- "pageViewControllerAppearStateOverrideAssertions"
- "previewType"
- "recentDocumentExtensionProviderForIconView:"
- "recentsDocumentExtensionProvider"
- "replace app placeholder with app"
- "replace app placeholder with app (async)"
- "replace app placeholder with dummy icon (async)"
- "sbh_traitCollectionWithIconTintColor:"
- "sbh_traitCollectionWithIconTintColor:userInterfaceStyle:"
- "setCustomIconImageViewControllerPresentationMode:"
- "setEndingBlurView:"
- "setRecentsDocumentExtensionProvider:"
- "setStartingBlurView:"
- "shortcutsDelegate"
- "shortcutsDelegateForIconView:"
- "shouldActivateApplicationShortcutItem:atIndex:"
- "shouldViewControllersAppearVisibleForListView:"
- "startingBlurView"
- "swapViewControllers"
- "visibleColumns"
- "\xb1"
- "\xf0R"
- "\xf0qA"

```
