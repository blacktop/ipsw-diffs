## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.1.18.101.0
-  __TEXT.__text: 0xa8e364
-  __TEXT.__auth_stubs: 0x5570
+4557.1.19.106.0
+  __TEXT.__text: 0xa91794
+  __TEXT.__auth_stubs: 0x5590
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb7e68
-  __TEXT.__const: 0x12ed0
-  __TEXT.__oslogstring: 0x5e373
-  __TEXT.__cstring: 0x7d134
-  __TEXT.__gcc_except_tab: 0x19544
+  __TEXT.__objc_methlist: 0xb8020
+  __TEXT.__const: 0x12f40
+  __TEXT.__oslogstring: 0x5e3ba
+  __TEXT.__cstring: 0x7d1d7
+  __TEXT.__gcc_except_tab: 0x19690
   __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2c4b0
+  __TEXT.__unwind_info: 0x2c590
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x221ca
-  __TEXT.__objc_methname: 0x1d093c
-  __TEXT.__objc_methtype: 0x4cd26
-  __TEXT.__objc_stubs: 0xf45c0
-  __DATA_CONST.__got: 0xa2b8
-  __DATA_CONST.__const: 0x1caf0
-  __DATA_CONST.__objc_classlist: 0x5268
-  __DATA_CONST.__objc_catlist: 0x350
+  __TEXT.__objc_classname: 0x2220f
+  __TEXT.__objc_methname: 0x1d13eb
+  __TEXT.__objc_methtype: 0x4d12c
+  __TEXT.__objc_stubs: 0xf4d00
+  __DATA_CONST.__got: 0xa2e0
+  __DATA_CONST.__const: 0x1cb58
+  __DATA_CONST.__objc_classlist: 0x5278
+  __DATA_CONST.__objc_catlist: 0x368
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ad50
+  __DATA_CONST.__objc_selrefs: 0x4af30
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x3fa0
-  __DATA_CONST.__objc_arraydata: 0x1888
-  __AUTH_CONST.__auth_got: 0x2ad0
-  __AUTH_CONST.__const: 0x10bd8
-  __AUTH_CONST.__cfstring: 0x6f100
-  __AUTH_CONST.__objc_const: 0x26aa80
-  __AUTH_CONST.__objc_arrayobj: 0x17a0
-  __AUTH_CONST.__objc_doubleobj: 0x760
+  __DATA_CONST.__objc_arraydata: 0x1868
+  __AUTH_CONST.__auth_got: 0x2ae0
+  __AUTH_CONST.__const: 0x10c58
+  __AUTH_CONST.__cfstring: 0x6f140
+  __AUTH_CONST.__objc_const: 0x26b5f0
+  __AUTH_CONST.__objc_arrayobj: 0x1770
+  __AUTH_CONST.__objc_doubleobj: 0x770
   __AUTH_CONST.__objc_intobj: 0x2ce8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x106d0
-  __DATA.__objc_ivar: 0xf420
+  __AUTH.__objc_data: 0x10770
+  __DATA.__objc_ivar: 0xf474
   __DATA.__data: 0x1f8b8
-  __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xab0
+  __DATA.__bss: 0xaa0
   __DATA.__common: 0xa40
   __DATA_DIRTY.__objc_data: 0x23140
   __DATA_DIRTY.__data: 0x180

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/IAP.framework/IAP
+  - /System/Library/PrivateFrameworks/IconRendering.framework/IconRendering
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/IdleTimerHosting.framework/IdleTimerHosting
   - /System/Library/PrivateFrameworks/IdleTimerServices.framework/IdleTimerServices

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 86ABB2F9-A8C0-38BD-BA50-85514C91A95A
-  Functions: 70194
-  Symbols:   237415
-  CStrings:  104367
+  UUID: E0CB9C34-EC30-31F6-9D54-D2B52A8C85E4
+  Functions: 70249
+  Symbols:   237648
+  CStrings:  104480
 
Symbols:
+ +[SBPinDesktopSpaceDisplayItemsSwitcherModifier modifierForGestureWithSelectedDisplayItem:context:]
+ +[SBPinDesktopSpaceDisplayItemsSwitcherModifier modifierForTransitionToAppLayout:context:]
+ +[SBSwitcherGenieAttributes genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:minimizedScale:containerSize:minimumOutsetSize:genieScale:multiplier:active:glassHighlight:layoutSettings:]
+ +[SBUpdateLayoutSwitcherEventResponse setNeedsLayout]
+ +[_SBSDFElementView layerClass]
+ +[_SBSDFView layerClass]
+ -[CALayer(IsIconLayer) isICRIconLayer]
+ -[ICRIconLayer(IsIconLayer) isICRIconLayer]
+ -[SBActivityBannerObserver _dismissBannerWithActivityIdentifier:forceDismissal:]
+ -[SBActivityBannerObserver _dismissBannerWithActivityIdentifier:forceDismissal:].cold.1
+ -[SBAppViewController applicationSceneViewController:statusBarDoubleTapped:]
+ -[SBContinuousExposeToHomeSwitcherModifier adjustedSpaceAccessoryViewScale:forAppLayout:]
+ -[SBContinuousExposeToHomeSwitcherModifier contentOffsetForIndex:alignment:]
+ -[SBContinuousExposeToHomeSwitcherModifier footerViewIconAlignmentForAppLayout:]
+ -[SBContinuousExposeToHomeSwitcherModifier handleScrollEvent:]
+ -[SBContinuousExposeToHomeSwitcherModifier initWithTransitionID:direction:exposeModifier:]
+ -[SBContinuousExposeToHomeSwitcherModifier initWithTransitionID:direction:exposeModifier:].cold.1
+ -[SBContinuousExposeToHomeSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:]
+ -[SBContinuousExposeToHomeSwitcherModifier titleAndIconOpacityForIndex:]
+ -[SBContinuousExposeToHomeSwitcherModifier transitionWillBegin]
+ -[SBContinuousExposeToHomeSwitcherModifier visibleAppLayouts]
+ -[SBContinuousExposeWindowDragContainerSwitcherModifier responseForProposedChildResponse:childModifier:event:]
+ -[SBContinuousExposeWindowDropSwitcherModifier didMoveToParentModifier:]
+ -[SBCoverSheetToAppSwitcherModifier initWithTransitionID:appLayout:progress:velocity:supportsBlur:]
+ -[SBCoverSheetToAppSwitcherModifier initWithTransitionID:appLayout:progress:velocity:supportsBlur:].cold.1
+ -[SBDashBoardCameraPageViewController _handlePrelaunchForTransitionToVisible:mode:]
+ -[SBDashBoardCameraPageViewController _handlePrelaunchForTransitionToVisible:mode:].cold.1
+ -[SBDashBoardCameraPageViewController _handlePrewarmForTransitionToVisible:mode:]
+ -[SBDashBoardCameraPageViewController _passesHasVisibleWindowTest]
+ -[SBDashBoardCameraPageViewController canWarmRealCamera]
+ -[SBDashBoardCameraPageViewController enforcesViewWindowRequirements]
+ -[SBDashBoardCameraPageViewController hostedEntityViewController]
+ -[SBDashBoardCameraPageViewController setCanWarmRealCamera:]
+ -[SBDashBoardCameraPageViewController setEnforcesViewWindowRequirements:]
+ -[SBDashBoardCameraPageViewController setHostedEntityViewController:]
+ -[SBDefaultImplementationsSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[SBDefaultImplementationsSwitcherModifier isPendingInvalidatablesForAcceleratedHomeGesture]
+ -[SBDeviceApplicationSceneViewController _statusBarDoubleTapTop:]
+ -[SBDeviceApplicationSceneViewController gestureRecognizer:shouldRequireFailureOfGestureRecognizer:]
+ -[SBDeviceApplicationSceneViewController gestureRecognizerShouldBegin:]
+ -[SBExposeWindowingModifier windowingConfigurationForInterfaceOrientation:]
+ -[SBFluidSwitcherIconOverlayView _alphaForIconOverlayView:crossfadeFraction:]
+ -[SBFluidSwitcherIndirectPanGestureRecognizer .cxx_destruct]
+ -[SBFluidSwitcherIndirectPanGestureRecognizer leafAppLayout]
+ -[SBFluidSwitcherIndirectPanGestureRecognizer setLeafAppLayout:]
+ -[SBFluidSwitcherViewController __updateImplicitpersonalityInvalidatables]
+ -[SBFluidSwitcherViewController _icrIconLayerIfAnyInLayer:]
+ -[SBFluidSwitcherViewController _layoutSubviews_updateVisibleItemsAccessoryViewsLayoutAndStyleWithCompletion:]
+ -[SBFluidSwitcherViewController currentTargetVelocityValueForVisibleAppLayout:key:]
+ -[SBFluidSwitcherViewController homeScreenGlassHighlightForAppLayout:]
+ -[SBFluidSwitcherViewController windowingConfigurationForInterfaceOrientation:]
+ -[SBFullScreenSwitcherLiveContentOverlayCoordinator fullScreenSwitcherSceneLiveContentOverlay:doubleTappedStatusBar:]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay applicationSceneViewController:statusBarDoubleTapped:]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay medusaDecoratedDeviceApplicationSceneViewController:statusBarDoubleTapped:]
+ -[SBFullScreenToHomeIconZoomSwitcherModifier setSupportsGlassHighlight:]
+ -[SBFullScreenToHomeIconZoomSwitcherModifier supportsGlassHighlight]
+ -[SBHomeGestureRootSwitcherModifier handleTransitionEvent:]
+ -[SBHomeGestureRootSwitcherModifier isPendingInvalidatablesForAcceleratedHomeGesture]
+ -[SBIconBadgeView(IsIconBadgeView) isIconBadgeView]
+ -[SBIconView(IsIconView) isIconView]
+ -[SBLiquidGlassLegibilityMetric handleEvent:withContext:]
+ -[SBMainDisplayPolicyAggregator _allowsCapabilityLockScreenCameraSwipeWithExplanation:]
+ -[SBMainSwitcherControllerCoordinator desktopSpaceItemsForSwitcherContentController:]
+ -[SBMainSwitcherControllerCoordinator slideOverItemForSwitcherContentController:]
+ -[SBMedusaDecoratedDeviceApplicationSceneViewController applicationSceneViewController:statusBarDoubleTapped:]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier .cxx_destruct]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier appLayoutContainingAppLayout:]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier appLayoutToPin]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier appLayoutsToCacheFullsizeSnapshots]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier appLayoutsToCacheSnapshots]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier cornerRadiiForIndex:]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier frameForIndex:]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier fullScreenModifier]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier initWithAppLayoutToPin:]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier setAppLayoutToPin:]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier setFullScreenModifier:]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier shadowOpacityForLayoutRole:atIndex:]
+ -[SBPinDesktopSpaceDisplayItemsSwitcherModifier visibleAppLayouts]
+ -[SBRoutingSwitcherModifier isPendingInvalidatablesForAcceleratedHomeGesture]
+ -[SBScheduledAlarmObserver _alarmFiringChanged:]
+ -[SBScheduledAlarmObserver _updateAlarmFiringChangedWithAlarm:]
+ -[SBSwitcherGenieAttributes glassHighlight]
+ -[SBSwitcherGenieAttributes setGlassHighlight:]
+ -[SBSwitcherGenieEffectView _addAndReturnPortaledContentView:]
+ -[SBSwitcherGenieEffectView _addPortaledNotificationBadgeForContentViewIfNeeded:]
+ -[SBSwitcherGenieEffectView _continuousCornerRadius]
+ -[SBSwitcherGenieEffectView _iconBadgeViewIfAnyInView:]
+ -[SBSwitcherGenieEffectView _iconViewIfAnyInView:]
+ -[SBSwitcherGenieEffectView _setContinuousCornerRadius:]
+ -[SBSwitcherGenieEffectView _setGlassHighlight:]
+ -[SBSwitcherModifier(SharedModifierUtilities) defaultMultitaskingLayoutAttributesForDisplayItem:layoutAttributes:layoutGrid:]
+ -[SBSwitcherModifier(SharedModifierUtilities) windowingConfiguration]
+ -[SBSwitcherWindowingSettings setWindowDragRubberBandedTranslationDetachmentThreshold:]
+ -[SBSwitcherWindowingSettings setWindowDragRubberBandedTranslationRange:]
+ -[SBSwitcherWindowingSettings windowDragRubberBandedTranslationDetachmentThreshold]
+ -[SBSwitcherWindowingSettings windowDragRubberBandedTranslationRange]
+ -[SBTodayViewController viewDidDisappear:]
+ -[SBTodayViewController viewWillAppear:]
+ -[SBTodayViewSpotlightPresenter containerViewDidDisappear]
+ -[SBTodayViewSpotlightPresenter containerViewWillAppear]
+ -[SBTopAffordanceViewController _createAlphaAnimatableProperty]
+ -[SBWindowingModifier windowingConfiguration]
+ -[SBWorkspaceApplicationSceneTransitionContext requestedPIPEntity]
+ -[SBWorkspaceApplicationSceneTransitionContext setRequestedPIPEntity:]
+ -[SBWorkspaceCoverSheetFlyInContext initWithProgress:velocity:supportsBlur:]
+ -[SBWorkspaceCoverSheetFlyInContext supportsBlur]
+ -[UIView(IsIconBadgeView) isIconBadgeView]
+ -[UIView(IsIconView) isIconView]
+ -[_SBSDFElementView layer]
+ -[_SBSDFView layer]
+ GCC_except_table1001
+ GCC_except_table1003
+ GCC_except_table221
+ GCC_except_table264
+ GCC_except_table321
+ GCC_except_table343
+ GCC_except_table399
+ GCC_except_table403
+ GCC_except_table417
+ GCC_except_table483
+ GCC_except_table518
+ GCC_except_table525
+ GCC_except_table527
+ GCC_except_table530
+ GCC_except_table534
+ GCC_except_table549
+ GCC_except_table553
+ GCC_except_table559
+ GCC_except_table563
+ GCC_except_table587
+ GCC_except_table633
+ GCC_except_table668
+ GCC_except_table740
+ GCC_except_table764
+ GCC_except_table767
+ GCC_except_table808
+ GCC_except_table848
+ GCC_except_table850
+ GCC_except_table899
+ GCC_except_table945
+ GCC_except_table984
+ GCC_except_table995
+ GCC_except_table997
+ GCC_except_table999
+ _CFBundleGetBundleWithIdentifier
+ _CFBundleGetFunctionPointerForName
+ _MTAlarmManagerAlarmsKey
+ _OBJC_CLASS_$_CASDFGlassHighlightEffect
+ _OBJC_CLASS_$_ICRIconLayer
+ _OBJC_CLASS_$_SBFluidSwitcherIndirectPanGestureRecognizer
+ _OBJC_CLASS_$_SBLiquidGlassLegibilityMetric
+ _OBJC_CLASS_$_SBPinDesktopSpaceDisplayItemsSwitcherModifier
+ _OBJC_CLASS_$__SBSDFElementView
+ _OBJC_CLASS_$__SBSDFView
+ _OBJC_IVAR_$_SBContinuousExposeToHomeSwitcherModifier._exposeModifier
+ _OBJC_IVAR_$_SBContinuousExposeWindowDragContainerSwitcherModifier._selectedDisplayItemWasInitiallyFullScreen
+ _OBJC_IVAR_$_SBCoverSheetIconFlyInAnimator._flyZCurveFactor
+ _OBJC_IVAR_$_SBCoverSheetIconFlyInAnimator._flyZResponse
+ _OBJC_IVAR_$_SBCoverSheetIconFlyInAnimator._iconAlphaResponse
+ _OBJC_IVAR_$_SBCoverSheetToAppSwitcherModifier._supportsBlur
+ _OBJC_IVAR_$_SBDashBoardCameraPageViewController._canWarmRealCamera
+ _OBJC_IVAR_$_SBDashBoardCameraPageViewController._enforcesViewWindowRequirements
+ _OBJC_IVAR_$_SBDashBoardCameraPageViewController._hasPendingHostedEntityGoLiveRequest
+ _OBJC_IVAR_$_SBDashBoardCameraPageViewController._presentationProgress
+ _OBJC_IVAR_$_SBDeviceApplicationSceneHandle._interfaceOrientationFromUserResizeIfAny
+ _OBJC_IVAR_$_SBDeviceApplicationSceneViewController._doubleTapTopGestureRecognizer
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._detachmentThreshold
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._initialLocation
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._prefersInitialLayout
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._rubberBandedTranslation
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._rubberBandingRange
+ _OBJC_IVAR_$_SBFluidSwitcherIndirectPanGestureRecognizer._leafAppLayout
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._isPendingInvalidatablesForAcceleratedHomeGesture
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._layoutSubviews_completionBlock
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._layoutSubviews_skipLayoutNotification
+ _OBJC_IVAR_$_SBFullScreenToHomeIconZoomSwitcherModifier._homeScreenIconIsSmallWidget
+ _OBJC_IVAR_$_SBFullScreenToHomeIconZoomSwitcherModifier._isWaitingForGlassHighlightDelay
+ _OBJC_IVAR_$_SBFullScreenToHomeIconZoomSwitcherModifier._supportsGlassHighlight
+ _OBJC_IVAR_$_SBHomeGestureRootSwitcherModifier._shouldAccelerateHomeGesture
+ _OBJC_IVAR_$_SBPinDesktopSpaceDisplayItemsSwitcherModifier._appLayoutToPin
+ _OBJC_IVAR_$_SBPinDesktopSpaceDisplayItemsSwitcherModifier._fullScreenModifier
+ _OBJC_IVAR_$_SBSwitcherGenieAttributes._glassHighlight
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._contentNotificationBadgePortalViews
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._glassHighlight
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._keyFillHighlightSDFView
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._rimHighlightSDFView
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._sdfElementView
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._windowDragRubberBandedTranslationDetachmentThreshold
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._windowDragRubberBandedTranslationRange
+ _OBJC_IVAR_$_SBTodayViewSpotlightPresenter._containerViewIsVisible
+ _OBJC_IVAR_$_SBTopAffordanceViewController._alphaAnimatableProperty
+ _OBJC_IVAR_$_SBWorkspaceApplicationSceneTransitionContext._requestedPIPEntity
+ _OBJC_IVAR_$_SBWorkspaceCoverSheetFlyInContext._supportsBlur
+ _OBJC_METACLASS_$_SBFluidSwitcherIndirectPanGestureRecognizer
+ _OBJC_METACLASS_$_SBLiquidGlassLegibilityMetric
+ _OBJC_METACLASS_$_SBPinDesktopSpaceDisplayItemsSwitcherModifier
+ _OBJC_METACLASS_$__SBSDFElementView
+ _OBJC_METACLASS_$__SBSDFView
+ _SBEqualSwitcherGenieGlassHighlightDirections
+ _SBEqualSwitcherGenieGlassHighlights
+ _SBLockScreenUIWillPerformTransitionLowLuminanceKey
+ _SBSwitcherGenieGlassHighlightDirectionMake
+ _SBSwitcherGenieGlassHighlightDirectionNone
+ _SBSwitcherGenieGlassHighlightIsNone
+ _SBSwitcherGenieGlassHighlightMake
+ _SBSwitcherGenieGlassHighlightNone
+ _SBSwitcherGenieGlassHighlightWidgets
+ __OBJC_$_CATEGORY_CALayer_$_IsIconLayer
+ __OBJC_$_CATEGORY_ICRIconLayer_$_IsIconLayer
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CALayer_$_IsIconLayer
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_ICRIconLayer_$_IsIconLayer
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_SBIconBadgeView_$_IsIconBadgeView
+ __OBJC_$_CATEGORY_SBIconBadgeView_$_IsIconBadgeView
+ __OBJC_$_CLASS_METHODS_SBPinDesktopSpaceDisplayItemsSwitcherModifier
+ __OBJC_$_CLASS_METHODS_SBUpdateLayoutSwitcherEventResponse
+ __OBJC_$_CLASS_METHODS_UIView(FBSDisplayConfiguration|SBSAGeometricTypeAnimationDecomposing|SBSAC2PropertyAnimating|SBClassicLayout|SBSystemActionPreviewPresentable|SBSpotlightBackgroundWeighting|SBWindowScene|SpringBoardAdditions|SBSystemApertureIDCornerCurve|SBPIPAdditions|SBPIPVibrancyEffects|SBSnapshoting|IsIconView|IsIconBadgeView)
+ __OBJC_$_CLASS_METHODS__SBSDFElementView
+ __OBJC_$_CLASS_METHODS__SBSDFView
+ __OBJC_$_INSTANCE_METHODS_SBFluidSwitcherIndirectPanGestureRecognizer
+ __OBJC_$_INSTANCE_METHODS_SBIconView(SwitcherIconZooming|IsIconView)
+ __OBJC_$_INSTANCE_METHODS_SBLiquidGlassLegibilityMetric
+ __OBJC_$_INSTANCE_METHODS_SBPinDesktopSpaceDisplayItemsSwitcherModifier
+ __OBJC_$_INSTANCE_METHODS_UIView(FBSDisplayConfiguration|SBSAGeometricTypeAnimationDecomposing|SBSAC2PropertyAnimating|SBClassicLayout|SBSystemActionPreviewPresentable|SBSpotlightBackgroundWeighting|SBWindowScene|SpringBoardAdditions|SBSystemApertureIDCornerCurve|SBPIPAdditions|SBPIPVibrancyEffects|SBSnapshoting|IsIconView|IsIconBadgeView)
+ __OBJC_$_INSTANCE_METHODS__SBSDFElementView
+ __OBJC_$_INSTANCE_METHODS__SBSDFView
+ __OBJC_$_INSTANCE_VARIABLES_SBFluidSwitcherIndirectPanGestureRecognizer
+ __OBJC_$_INSTANCE_VARIABLES_SBPinDesktopSpaceDisplayItemsSwitcherModifier
+ __OBJC_$_PROP_LIST_SBFluidSwitcherIndirectPanGestureRecognizer
+ __OBJC_$_PROP_LIST_SBLiquidGlassLegibilityMetric
+ __OBJC_$_PROP_LIST_SBPinDesktopSpaceDisplayItemsSwitcherModifier
+ __OBJC_CLASS_PROTOCOLS_$_SBLiquidGlassLegibilityMetric
+ __OBJC_CLASS_PROTOCOLS_$_UIView(FBSDisplayConfiguration|SBSAGeometricTypeAnimationDecomposing|SBSAC2PropertyAnimating|SBClassicLayout|SBSystemActionPreviewPresentable|SBSpotlightBackgroundWeighting|SBWindowScene|SpringBoardAdditions|SBSystemApertureIDCornerCurve|SBPIPAdditions|SBPIPVibrancyEffects|SBSnapshoting|IsIconView|IsIconBadgeView)
+ __OBJC_CLASS_RO_$_SBFluidSwitcherIndirectPanGestureRecognizer
+ __OBJC_CLASS_RO_$_SBLiquidGlassLegibilityMetric
+ __OBJC_CLASS_RO_$_SBPinDesktopSpaceDisplayItemsSwitcherModifier
+ __OBJC_CLASS_RO_$__SBSDFElementView
+ __OBJC_CLASS_RO_$__SBSDFView
+ __OBJC_METACLASS_RO_$_SBFluidSwitcherIndirectPanGestureRecognizer
+ __OBJC_METACLASS_RO_$_SBLiquidGlassLegibilityMetric
+ __OBJC_METACLASS_RO_$_SBPinDesktopSpaceDisplayItemsSwitcherModifier
+ __OBJC_METACLASS_RO_$__SBSDFElementView
+ __OBJC_METACLASS_RO_$__SBSDFView
+ ___102-[SBPinDesktopSpaceDisplayItemsSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:]_block_invoke
+ ___107-[SBFluidSwitcherGestureWorkspaceTransaction handleTransitionRequestForGestureComplete:fromGestureManager:]_block_invoke_4
+ ___110-[SBContinuousExposeWindowDragContainerSwitcherModifier responseForProposedChildResponse:childModifier:event:]_block_invoke
+ ___110-[SBFluidSwitcherViewController _layoutSubviews_updateVisibleItemsAccessoryViewsLayoutAndStyleWithCompletion:]_block_invoke
+ ___111-[SBCoverSheetPresentationManager _setTransitionProgress:animated:gestureActive:coverSheetProgress:completion:]_block_invoke_2.236
+ ___113-[SBFluidSwitcherViewController initWithPersonality:liveContentOverlayCoordinator:dataSource:delegate:debugName:]_block_invoke.210
+ ___27-[SBLockScreenManager init]_block_invoke.223
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1210
+ ___47-[SBLockScreenManager handleTransitionRequest:]_block_invoke.254
+ ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.92
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.395
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.394
+ ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.791
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1781
+ ___57-[SBLiquidGlassLegibilityMetric handleEvent:withContext:]_block_invoke
+ ___61-[SBContinuousExposeToHomeSwitcherModifier visibleAppLayouts]_block_invoke
+ ___62-[SBContinuousExposeToHomeSwitcherModifier handleScrollEvent:]_block_invoke
+ ___63-[SBLockScreenManager lockUIFromSource:withOptions:completion:]_block_invoke.245
+ ___63-[SBPinDesktopSpaceDisplayItemsSwitcherModifier frameForIndex:]_block_invoke
+ ___63-[SBTopAffordanceViewController _createAlphaAnimatableProperty]_block_invoke
+ ___65-[SBFullScreenToHomeIconZoomSwitcherModifier transitionWillBegin]_block_invoke_6
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.687
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.689
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.690
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.691
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.692
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_2.698
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_3.710
+ ___69-[SBPinDesktopSpaceDisplayItemsSwitcherModifier cornerRadiiForIndex:]_block_invoke
+ ___72-[SBContinuousExposeToHomeSwitcherModifier titleAndIconOpacityForIndex:]_block_invoke
+ ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.401
+ ___73-[SBFluidSwitcherViewController _updateImplicitpersonalityInvalidatables]_block_invoke
+ ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1114
+ ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.423
+ ___76-[SBContinuousExposeToHomeSwitcherModifier contentOffsetForIndex:alignment:]_block_invoke
+ ___77-[SBRoutingSwitcherModifier isPendingInvalidatablesForAcceleratedHomeGesture]_block_invoke
+ ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.453
+ ___84-[SBPinDesktopSpaceDisplayItemsSwitcherModifier shadowOpacityForLayoutRole:atIndex:]_block_invoke
+ ___85-[SBContinuousExposeToHomeSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:]_block_invoke
+ ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.88
+ ___89-[SBContinuousExposeToHomeSwitcherModifier adjustedSpaceAccessoryViewScale:forAppLayout:]_block_invoke
+ ___90+[SBPinDesktopSpaceDisplayItemsSwitcherModifier modifierForTransitionToAppLayout:context:]_block_invoke
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1633
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1635
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1637
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1641
+ ___92-[SBFluidSwitcherGestureWorkspaceTransaction _copiedTransitionRequestFromTransitionRequest:]_block_invoke_2
+ ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke.404
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1764
+ ___99+[SBPinDesktopSpaceDisplayItemsSwitcherModifier modifierForGestureWithSelectedDisplayItem:context:]_block_invoke
+ ___blockIMPFromContextSignature104_block_invoke
+ ___blockIMPFromContextSignature105_block_invoke
+ ___blockIMPFromEventSignature104_block_invoke
+ ___blockIMPFromEventSignature105_block_invoke
+ ___blockIMPFromQuerySignature104_block_invoke
+ ___blockIMPFromQuerySignature105_block_invoke
+ ___block_descriptor_48_e109_{SBSwitcherGenieGlassHighlight=Q{SBSwitcherGenieGlassHighlightDirection=ddd}d}24?0"SBChainableModifier"816l
+ ___block_descriptor_48_e32_24?0"SBChainableModifier"8q16l
+ ___block_descriptor_49_e42_v16?0"SBMainWorkspaceTransitionRequest"8l
+ ___block_descriptor_49_e54_v16?0"SBWorkspaceApplicationSceneTransitionContext"8l
+ ___block_literal_global.1056
+ ___block_literal_global.1065
+ ___block_literal_global.1101
+ ___block_literal_global.1128
+ ___block_literal_global.1153
+ ___block_literal_global.1156
+ ___block_literal_global.1161
+ ___block_literal_global.1167
+ ___block_literal_global.1460
+ ___block_literal_global.1607
+ ___block_literal_global.1611
+ ___block_literal_global.1643
+ ___block_literal_global.1652
+ ___block_literal_global.1654
+ ___block_literal_global.1656
+ ___block_literal_global.1658
+ ___block_literal_global.1674
+ ___block_literal_global.1790
+ ___block_literal_global.1813
+ ___block_literal_global.1822
+ ___block_literal_global.1838
+ ___block_literal_global.257
+ ___block_literal_global.261
+ ___block_literal_global.299
+ ___block_literal_global.305
+ ___block_literal_global.320
+ ___block_literal_global.336
+ ___block_literal_global.387
+ ___block_literal_global.507
+ ___block_literal_global.516
+ ___block_literal_global.519
+ ___block_literal_global.612
+ ___block_literal_global.684
+ ___block_literal_global.700
+ ___block_literal_global.738
+ ___block_literal_global.764
+ _blockIMPFromContextSignature104
+ _blockIMPFromContextSignature105
+ _blockIMPFromEventSignature104
+ _blockIMPFromEventSignature105
+ _blockIMPFromQuerySignature104
+ _blockIMPFromQuerySignature105
+ _kCAFilterLinear
+ _objc_msgSend$__updateImplicitpersonalityInvalidatables
+ _objc_msgSend$_addAndReturnPortaledContentView:
+ _objc_msgSend$_addPortaledNotificationBadgeForContentViewIfNeeded:
+ _objc_msgSend$_allowsCapabilityLockScreenCameraSwipeWithExplanation:
+ _objc_msgSend$_alphaForIconOverlayView:crossfadeFraction:
+ _objc_msgSend$_createAlphaAnimatableProperty
+ _objc_msgSend$_dismissBannerWithActivityIdentifier:forceDismissal:
+ _objc_msgSend$_handlePrelaunchForTransitionToVisible:mode:
+ _objc_msgSend$_handlePrewarmForTransitionToVisible:mode:
+ _objc_msgSend$_iconBadgeViewIfAnyInView:
+ _objc_msgSend$_iconViewIfAnyInView:
+ _objc_msgSend$_icrIconLayerIfAnyInLayer:
+ _objc_msgSend$_layoutSubviews_updateVisibleItemsAccessoryViewsLayoutAndStyleWithCompletion:
+ _objc_msgSend$_passesHasVisibleWindowTest
+ _objc_msgSend$_setGlassHighlight:
+ _objc_msgSend$_targetVelocityForKey:
+ _objc_msgSend$_updateAlarmFiringChangedWithAlarm:
+ _objc_msgSend$appLayoutToPin
+ _objc_msgSend$applicationSceneViewController:statusBarDoubleTapped:
+ _objc_msgSend$containerViewDidDisappear
+ _objc_msgSend$containerViewWillAppear
+ _objc_msgSend$defaultMultitaskingLayoutAttributesForDisplayItem:layoutAttributes:layoutGrid:
+ _objc_msgSend$desktopSpaceItemsForSwitcherContentController:
+ _objc_msgSend$fullScreenModifier
+ _objc_msgSend$fullScreenSwitcherSceneLiveContentOverlay:doubleTappedStatusBar:
+ _objc_msgSend$genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:minimizedScale:containerSize:minimumOutsetSize:genieScale:multiplier:active:glassHighlight:layoutSettings:
+ _objc_msgSend$glassHighlight
+ _objc_msgSend$hasGlass
+ _objc_msgSend$hasTintColor
+ _objc_msgSend$homeScreenGlassHighlightForAppLayout:
+ _objc_msgSend$iconFlyZCurveFactor
+ _objc_msgSend$iconFlyZResponse
+ _objc_msgSend$inPlaceDamping
+ _objc_msgSend$inPlaceResponse
+ _objc_msgSend$initWithAppLayoutToPin:
+ _objc_msgSend$initWithProgress:velocity:supportsBlur:
+ _objc_msgSend$initWithTransitionID:appLayout:progress:velocity:supportsBlur:
+ _objc_msgSend$isFiring
+ _objc_msgSend$isICRIconLayer
+ _objc_msgSend$isIconBadgeView
+ _objc_msgSend$isIconView
+ _objc_msgSend$isPendingInvalidatablesForAcceleratedHomeGesture
+ _objc_msgSend$isSnoozed
+ _objc_msgSend$lightDirection
+ _objc_msgSend$lightIntensity
+ _objc_msgSend$medusaDecoratedDeviceApplicationSceneViewController:statusBarDoubleTapped:
+ _objc_msgSend$modifierForGestureWithSelectedDisplayItem:context:
+ _objc_msgSend$modifierForTransitionToAppLayout:context:
+ _objc_msgSend$requestedPIPEntity
+ _objc_msgSend$setAmount:
+ _objc_msgSend$setAngle:
+ _objc_msgSend$setFillHeightOffset:
+ _objc_msgSend$setFillHeightScale:
+ _objc_msgSend$setFillSpreadOffset:
+ _objc_msgSend$setFillSpreadScale:
+ _objc_msgSend$setGlassHighlight:
+ _objc_msgSend$setKeyHeightOffset:
+ _objc_msgSend$setKeyHeightScale:
+ _objc_msgSend$setKeySpreadOffset:
+ _objc_msgSend$setKeySpreadScale:
+ _objc_msgSend$setMinificationFilterBias:
+ _objc_msgSend$setRequestedPIPEntity:
+ _objc_msgSend$setSpread:
+ _objc_msgSend$setSupportsGlassHighlight:
+ _objc_msgSend$setWindowDragRubberBandedTranslationDetachmentThreshold:
+ _objc_msgSend$setWindowDragRubberBandedTranslationRange:
+ _objc_msgSend$shouldAutoPIPEnteringBackgroundForRequest:foundEntity:
+ _objc_msgSend$slideOverItemForSwitcherContentController:
+ _objc_msgSend$supportsBlur
+ _objc_msgSend$windowDragRubberBandedTranslationDetachmentThreshold
+ _objc_msgSend$windowDragRubberBandedTranslationRange
+ _objc_msgSend$windowingConfigurationForInterfaceOrientation:
- +[SBSwitcherGenieAttributes genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:minimizedScale:containerSize:minimumOutsetSize:genieScale:multiplier:active:layoutSettings:]
- -[SBActivityBannerObserver _dismissBannerWithActivityIdentifier:].cold.1
- -[SBAppExposeContinuousExposeSwitcherModifier .cxx_destruct]
- -[SBAppExposeContinuousExposeSwitcherModifier _canShowReopenClosedWindowsButton]
- -[SBAppExposeContinuousExposeSwitcherModifier _updateReopenClosedWindowsButtonPresence]
- -[SBAppExposeContinuousExposeSwitcherModifier adjustedAppLayoutsForAppLayouts:]
- -[SBAppExposeContinuousExposeSwitcherModifier adjustedContinuousExposeIdentifiersInSwitcherFromPreviousIdentifiersInSwitcher:identifiersInStrip:]
- -[SBAppExposeContinuousExposeSwitcherModifier appExposeAccessoryButtonsBundleIdentifier]
- -[SBAppExposeContinuousExposeSwitcherModifier appExposeAccessoryButtonsOverrideUserInterfaceStyle]
- -[SBAppExposeContinuousExposeSwitcherModifier appLayoutToScrollToBeforeReopeningClosedWindows]
- -[SBAppExposeContinuousExposeSwitcherModifier bundleIdentifier]
- -[SBAppExposeContinuousExposeSwitcherModifier copyWithZone:]
- -[SBAppExposeContinuousExposeSwitcherModifier cornerRadiiForIndex:]
- -[SBAppExposeContinuousExposeSwitcherModifier descriptionBuilderWithMultilinePrefix:]
- -[SBAppExposeContinuousExposeSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:]
- -[SBAppExposeContinuousExposeSwitcherModifier handleInsertionEvent:]
- -[SBAppExposeContinuousExposeSwitcherModifier handleRemovalEvent:]
- -[SBAppExposeContinuousExposeSwitcherModifier handleTimerEvent:]
- -[SBAppExposeContinuousExposeSwitcherModifier handleTransitionEvent:]
- -[SBAppExposeContinuousExposeSwitcherModifier headerStyleForIndex:]
- -[SBAppExposeContinuousExposeSwitcherModifier homeScreenAlpha]
- -[SBAppExposeContinuousExposeSwitcherModifier homeScreenBackdropBlurProgress]
- -[SBAppExposeContinuousExposeSwitcherModifier homeScreenBackdropBlurType]
- -[SBAppExposeContinuousExposeSwitcherModifier homeScreenDimmingAlpha]
- -[SBAppExposeContinuousExposeSwitcherModifier initWithBundleIdentifier:]
- -[SBAppExposeContinuousExposeSwitcherModifier initWithBundleIdentifier:].cold.1
- -[SBAppExposeContinuousExposeSwitcherModifier isHomeScreenContentRequired]
- -[SBAppExposeContinuousExposeSwitcherModifier isLayoutRoleDraggable:inAppLayout:]
- -[SBAppExposeContinuousExposeSwitcherModifier isResizeGrabberVisibleForAppLayout:]
- -[SBAppExposeContinuousExposeSwitcherModifier isWallpaperRequiredForSwitcher]
- -[SBAppExposeContinuousExposeSwitcherModifier plusButtonAlpha]
- -[SBAppExposeContinuousExposeSwitcherModifier plusButtonStyle]
- -[SBAppExposeContinuousExposeSwitcherModifier reopenClosedWindowsButtonAlpha]
- -[SBAppExposeContinuousExposeSwitcherModifier reopenClosedWindowsButtonScale]
- -[SBAppExposeContinuousExposeSwitcherModifier shadowStyleForLayoutRole:inAppLayout:]
- -[SBAppExposeContinuousExposeSwitcherModifier shouldAccessoryDrawShadowForAppLayout:]
- -[SBAppExposeContinuousExposeSwitcherModifier wallpaperStyle]
- -[SBAppSwitcherContinuousExposeSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
- -[SBContinuousExposeToAppExposeSwitcherModifier .cxx_destruct]
- -[SBContinuousExposeToAppExposeSwitcherModifier animationAttributesForLayoutElement:]
- -[SBContinuousExposeToAppExposeSwitcherModifier appExposeBundleID]
- -[SBContinuousExposeToAppExposeSwitcherModifier descriptionBuilderWithMultilinePrefix:]
- -[SBContinuousExposeToAppExposeSwitcherModifier direction]
- -[SBContinuousExposeToAppExposeSwitcherModifier frameForIndex:]
- -[SBContinuousExposeToAppExposeSwitcherModifier handleTimerEvent:]
- -[SBContinuousExposeToAppExposeSwitcherModifier initWithTransitionID:appExposeBundleID:direction:appExposeModifier:]
- -[SBContinuousExposeToAppExposeSwitcherModifier initWithTransitionID:appExposeBundleID:direction:appExposeModifier:].cold.1
- -[SBContinuousExposeToAppExposeSwitcherModifier initWithTransitionID:appExposeBundleID:direction:appExposeModifier:].cold.2
- -[SBContinuousExposeToAppExposeSwitcherModifier transitionWillBegin]
- -[SBContinuousExposeToAppExposeSwitcherModifier transitionWillUpdate]
- -[SBContinuousExposeToAppExposeSwitcherModifier visibleAppLayouts]
- -[SBContinuousExposeToHomeSwitcherModifier initWithTransitionID:direction:continuousExposeModifier:]
- -[SBContinuousExposeToHomeSwitcherModifier initWithTransitionID:direction:continuousExposeModifier:].cold.1
- -[SBCoverSheetToAppSwitcherModifier initWithTransitionID:appLayout:progress:velocity:]
- -[SBCoverSheetToAppSwitcherModifier initWithTransitionID:appLayout:progress:velocity:].cold.1
- -[SBDashBoardCameraPageViewController updateTransitionToVisible:progress:mode:].cold.1
- -[SBDashBoardPolicyBasedBehaviorProvider _cameraRestrictions]
- -[SBDeckFloatingSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
- -[SBDeckSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
- -[SBDoubleTapSystemGestureRecognizer _commonInit]
- -[SBDoubleTapSystemGestureRecognizer initWithCoder:]
- -[SBDoubleTapSystemGestureRecognizer initWithTarget:action:]
- -[SBDoubleTapSystemGestureRecognizer init]
- -[SBExposeWindowingModifier transitionWillBegin:]
- -[SBExposeWindowingModifier windowingConfiguration]
- -[SBFlexibleWindowingItemResizeGestureSwitcherModifier appLayoutsToCacheFullsizeSnapshots]
- -[SBFlexibleWindowingItemResizeGestureSwitcherModifier appLayoutsToCacheSnapshots]
- -[SBFlexibleWindowingItemResizeGestureSwitcherModifier didMoveToParentModifier:]
- -[SBFlexibleWindowingItemResizeGestureSwitcherModifier frameForIndex:]
- -[SBFlexibleWindowingItemResizeGestureSwitcherModifier visibleAppLayouts]
- -[SBFluidSwitcherGestureManager _handleDoubleTapGesture:]
- -[SBFluidSwitcherGestureManager _handleScrollToTopGesture:]
- -[SBFluidSwitcherGestureManager _shouldBeginWindowTopRegionTapGesture:]
- -[SBFluidSwitcherGestureManager _shouldTopRegionDoubleTapGesture:receiveTouch:]
- -[SBFluidSwitcherGestureManager _shouldTopRegionScrollToTopGesture:receiveTouch:]
- -[SBFluidSwitcherGestureManager setWindowTopRegionDoubleTapGestureRecognizer:]
- -[SBFluidSwitcherGestureManager setWindowTopRegionScrollToTopTapGestureRecognizer:]
- -[SBFluidSwitcherGestureManager windowTopRegionDoubleTapGestureRecognizer]
- -[SBFluidSwitcherGestureManager windowTopRegionScrollToTopTapGestureRecognizer]
- -[SBIndirectPanGestureRecognizer lastTrackpadActivationTimestamp]
- -[SBIndirectPanGestureRecognizer leafAppLayout]
- -[SBIndirectPanGestureRecognizer setLastTrackpadActivationTimestamp:]
- -[SBIndirectPanGestureRecognizer setLeafAppLayout:]
- -[SBMainSwitcherRootSwitcherModifier handleGestureEvent:]
- -[SBShelfCarouselSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
- -[SBSystemApertureProvidedContentElement minimumCustomElementHeightUnderSensor]
- -[SBSystemApertureProvidedContentElement minimumCustomElementHeightUnderSensor].cold.1
- -[SBWorkspaceCoverSheetFlyInContext initWithProgress:velocity:]
- -[_SBActiveAppFloorFloatingSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
- -[_SBFullScreenAppFloorSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
- -[_SBGridFloorSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
- -[_SBHomeScreenFloorSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
- GCC_except_table116
- GCC_except_table143
- GCC_except_table155
- GCC_except_table223
- GCC_except_table233
- GCC_except_table269
- GCC_except_table306
- GCC_except_table319
- GCC_except_table337
- GCC_except_table393
- GCC_except_table401
- GCC_except_table415
- GCC_except_table475
- GCC_except_table509
- GCC_except_table519
- GCC_except_table522
- GCC_except_table524
- GCC_except_table526
- GCC_except_table541
- GCC_except_table545
- GCC_except_table551
- GCC_except_table555
- GCC_except_table579
- GCC_except_table625
- GCC_except_table660
- GCC_except_table732
- GCC_except_table756
- GCC_except_table759
- GCC_except_table800
- GCC_except_table840
- GCC_except_table879
- GCC_except_table935
- GCC_except_table974
- GCC_except_table981
- GCC_except_table983
- GCC_except_table985
- GCC_except_table987
- GCC_except_table989
- _OBJC_CLASS_$_SBAppExposeContinuousExposeSwitcherModifier
- _OBJC_CLASS_$_SBContinuousExposeToAppExposeSwitcherModifier
- _OBJC_CLASS_$_SBDoubleTapSystemGestureRecognizer
- _OBJC_IVAR_$_SBAppExposeContinuousExposeSwitcherModifier._bundleIdentifier
- _OBJC_IVAR_$_SBAppExposeContinuousExposeSwitcherModifier._isScrollingForward
- _OBJC_IVAR_$_SBAppExposeContinuousExposeSwitcherModifier._isShowingReopenClosedWindowsButton
- _OBJC_IVAR_$_SBAppExposeContinuousExposeSwitcherModifier._numberOfHiddenAppLayouts
- _OBJC_IVAR_$_SBAppExposeContinuousExposeSwitcherModifier._previousContentOffset
- _OBJC_IVAR_$_SBContinuousExposeToAppExposeSwitcherModifier._appExposeBundleID
- _OBJC_IVAR_$_SBContinuousExposeToAppExposeSwitcherModifier._appExposeModifier
- _OBJC_IVAR_$_SBContinuousExposeToAppExposeSwitcherModifier._appLayoutsVisibleBeforeTransition
- _OBJC_IVAR_$_SBContinuousExposeToAppExposeSwitcherModifier._direction
- _OBJC_IVAR_$_SBContinuousExposeToAppExposeSwitcherModifier._timerReason
- _OBJC_IVAR_$_SBContinuousExposeToHomeSwitcherModifier._continuousExposeModifier
- _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._desktopSpaceAppLayout
- _OBJC_IVAR_$_SBFluidSwitcherGestureManager._windowTopRegionDoubleTapGestureRecognizer
- _OBJC_IVAR_$_SBFluidSwitcherGestureManager._windowTopRegionScrollToTopTapGestureRecognizer
- _OBJC_IVAR_$_SBFluidSwitcherViewController._hasAnyUnadjustedAppLayoutsInDuality
- _OBJC_IVAR_$_SBIndirectPanGestureRecognizer._lastTrackpadActivationTimestamp
- _OBJC_IVAR_$_SBIndirectPanGestureRecognizer._leafAppLayout
- _OBJC_IVAR_$_SBMainSwitcherRootSwitcherModifier._isInPeekState
- _OBJC_METACLASS_$_SBAppExposeContinuousExposeSwitcherModifier
- _OBJC_METACLASS_$_SBContinuousExposeToAppExposeSwitcherModifier
- _OBJC_METACLASS_$_SBDoubleTapSystemGestureRecognizer
- _SBStringForSBContinuousExposeToAppExposeSwitcherModifierDirection
- __OBJC_$_CATEGORY_INSTANCE_METHODS_SBIconView_$_SwitcherIconZooming
- __OBJC_$_CLASS_METHODS_UIView(FBSDisplayConfiguration|SBSAGeometricTypeAnimationDecomposing|SBSAC2PropertyAnimating|SBClassicLayout|SBSystemActionPreviewPresentable|SBSpotlightBackgroundWeighting|SBWindowScene|SpringBoardAdditions|SBSystemApertureIDCornerCurve|SBPIPAdditions|SBPIPVibrancyEffects|SBSnapshoting)
- __OBJC_$_INSTANCE_METHODS_SBAppExposeContinuousExposeSwitcherModifier
- __OBJC_$_INSTANCE_METHODS_SBContinuousExposeToAppExposeSwitcherModifier
- __OBJC_$_INSTANCE_METHODS_SBDoubleTapSystemGestureRecognizer
- __OBJC_$_INSTANCE_METHODS_UIView(FBSDisplayConfiguration|SBSAGeometricTypeAnimationDecomposing|SBSAC2PropertyAnimating|SBClassicLayout|SBSystemActionPreviewPresentable|SBSpotlightBackgroundWeighting|SBWindowScene|SpringBoardAdditions|SBSystemApertureIDCornerCurve|SBPIPAdditions|SBPIPVibrancyEffects|SBSnapshoting)
- __OBJC_$_INSTANCE_VARIABLES_SBAppExposeContinuousExposeSwitcherModifier
- __OBJC_$_INSTANCE_VARIABLES_SBContinuousExposeToAppExposeSwitcherModifier
- __OBJC_$_PROP_LIST_SBAppExposeContinuousExposeSwitcherModifier
- __OBJC_$_PROP_LIST_SBContinuousExposeToAppExposeSwitcherModifier
- __OBJC_CLASS_PROTOCOLS_$_UIView(FBSDisplayConfiguration|SBSAGeometricTypeAnimationDecomposing|SBSAC2PropertyAnimating|SBClassicLayout|SBSystemActionPreviewPresentable|SBSpotlightBackgroundWeighting|SBWindowScene|SpringBoardAdditions|SBSystemApertureIDCornerCurve|SBPIPAdditions|SBPIPVibrancyEffects|SBSnapshoting)
- __OBJC_CLASS_RO_$_SBAppExposeContinuousExposeSwitcherModifier
- __OBJC_CLASS_RO_$_SBContinuousExposeToAppExposeSwitcherModifier
- __OBJC_CLASS_RO_$_SBDoubleTapSystemGestureRecognizer
- __OBJC_METACLASS_RO_$_SBAppExposeContinuousExposeSwitcherModifier
- __OBJC_METACLASS_RO_$_SBContinuousExposeToAppExposeSwitcherModifier
- __OBJC_METACLASS_RO_$_SBDoubleTapSystemGestureRecognizer
- __ZL11SBEmitEvent21SBSAnalyticsEventType
- ___113-[SBFluidSwitcherViewController initWithPersonality:liveContentOverlayCoordinator:dataSource:delegate:debugName:]_block_invoke.207
- ___27-[SBLockScreenManager init]_block_invoke.220
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1209
- ___47-[SBLockScreenManager handleTransitionRequest:]_block_invoke.251
- ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.86
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.389
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.391
- ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.785
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1780
- ___63-[SBLockScreenManager lockUIFromSource:withOptions:completion:]_block_invoke.242
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.681
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.683
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.684
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.685
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.686
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_2.692
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_3.704
- ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.398
- ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1108
- ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.420
- ___77-[SBDisplayItemLayoutAttributesProvider layoutAttributesEntriesForAppLayout:]_block_invoke_2
- ___79-[SBSystemApertureProvidedContentElement minimumCustomElementHeightUnderSensor]_block_invoke
- ___80-[SBFlexibleWindowingItemResizeGestureSwitcherModifier didMoveToParentModifier:]_block_invoke
- ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.450
- ___87-[SBAppExposeContinuousExposeSwitcherModifier _updateReopenClosedWindowsButtonPresence]_block_invoke
- ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.82
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1632
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1634
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1636
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1640
- ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke.401
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1763
- ___block_descriptor_48_e42_v16?0"SBMainWorkspaceTransitionRequest"8l
- ___block_literal_global.1055
- ___block_literal_global.1064
- ___block_literal_global.1100
- ___block_literal_global.1122
- ___block_literal_global.1152
- ___block_literal_global.1155
- ___block_literal_global.1160
- ___block_literal_global.1166
- ___block_literal_global.1459
- ___block_literal_global.1606
- ___block_literal_global.1610
- ___block_literal_global.1642
- ___block_literal_global.1651
- ___block_literal_global.1653
- ___block_literal_global.1655
- ___block_literal_global.1657
- ___block_literal_global.1673
- ___block_literal_global.1789
- ___block_literal_global.1812
- ___block_literal_global.1821
- ___block_literal_global.1837
- ___block_literal_global.254
- ___block_literal_global.258
- ___block_literal_global.302
- ___block_literal_global.306
- ___block_literal_global.341
- ___block_literal_global.354
- ___block_literal_global.384
- ___block_literal_global.496
- ___block_literal_global.508
- ___block_literal_global.511
- ___block_literal_global.678
- ___block_literal_global.688
- ___block_literal_global.732
- ___block_literal_global.758
- _gCRAnnotations
- _minimumCustomElementHeightUnderSensor.__minimumCustomElementHeightUnderSensor
- _minimumCustomElementHeightUnderSensor.onceToken
- _objc_msgSend$_cameraRestrictions
- _objc_msgSend$_shouldBeginWindowTopRegionTapGesture:
- _objc_msgSend$_shouldTopRegionDoubleTapGesture:receiveTouch:
- _objc_msgSend$_shouldTopRegionScrollToTopGesture:receiveTouch:
- _objc_msgSend$friction
- _objc_msgSend$genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:minimizedScale:containerSize:minimumOutsetSize:genieScale:multiplier:active:layoutSettings:
- _objc_msgSend$inPlaceFriction
- _objc_msgSend$inPlaceTension
- _objc_msgSend$initWithProgress:velocity:
- _objc_msgSend$initWithStartingEnvironmentMode:selectedAppLayout:mixedGridModifier:
- _objc_msgSend$initWithTransitionID:appLayout:progress:velocity:
- _objc_msgSend$initWithTransitionID:direction:continuousExposeModifier:
- _objc_msgSend$minimumCustomElementHeightUnderSensor
- _objc_msgSend$tension
CStrings:
+ "%{public}@ recieved %{public}@ notification with %lu alarms in payload, expect one alarm only."
+ "%{public}@ recieved alarm firing changed with alarmID: %{public}@; isFire %d; isSnoozed %d"
+ "@\"SBDisplayItem\"24@0:8@\"<SBSwitcherContentViewControlling>\"16"
+ "@\"SBFluidSwitcherIndirectPanGestureRecognizer\""
+ "@\"SBWindowingModifier\""
+ "@\"UIView\"24@0:8@\"NCNotificationViewController\"16"
+ "@\"_SBSDFElementView\""
+ "@\"_SBSDFView\""
+ "@212@0:8{CGPoint=dd}16{CGPoint=dd}32{CGPoint=dd}48{CGSize=dd}64{CGSize=dd}80d96{CGSize=dd}104{CGSize=dd}120d136{CGPoint=dd}144B160{SBSwitcherGenieGlassHighlight=Q{SBSwitcherGenieGlassHighlightDirection=ddd}d}164@204"
+ "@24@?0@\"SBChainableModifier\"8q16"
+ "@36@0:8d16d24B32"
+ "@52@0:8@16@24d32d40B48"
+ "IsIconBadgeView"
+ "IsIconLayer"
+ "IsIconView"
+ "Overflow"
+ "Rubber-Banded Translation Detachment Threshold"
+ "Rubber-Banded Translation Range"
+ "SBContinuousExposeWindowDropSwitcherModifierKeyPinDesktopSpaceDisplayItems"
+ "SBFluidSwitcherIndirectPanGestureRecognizer"
+ "SBLiquidGlassLegibilityMetric"
+ "SBLockScreenCameraSwipeEnabled"
+ "SBLockScreenUIWillPerformTransitionLowLuminanceKey"
+ "SBPinDesktopSpaceDisplayItemsSwitcherModifier"
+ "T@\"CSHostedEntityViewController\",&,N,V_hostedEntityViewController"
+ "T@\"SBAppLayout\",&,N,V_appLayoutToPin"
+ "T@\"SBApplicationSceneEntity\",&,N,V_requestedPIPEntity"
+ "T@\"SBFluidSwitcherIndirectPanGestureRecognizer\",&,N,V_indirectDismissFloatingApplicationGestureRecognizer"
+ "T@\"SBFullScreenContinuousExposeSwitcherModifier\",&,N,V_fullScreenModifier"
+ "TB,N,V_canWarmRealCamera"
+ "TB,N,V_enforcesViewWindowRequirements"
+ "TB,N,V_supportsGlassHighlight"
+ "TB,R,N,V_supportsBlur"
+ "Td,V_windowDragRubberBandedTranslationDetachmentThreshold"
+ "Td,V_windowDragRubberBandedTranslationRange"
+ "T{SBSwitcherGenieGlassHighlight=Q{SBSwitcherGenieGlassHighlightDirection=ddd}d},N,V_glassHighlight"
+ "UIViewGlassGetLegibilitySetting"
+ "_SBSDFElementView"
+ "_SBSDFView"
+ "__updateImplicitpersonalityInvalidatables"
+ "_addAndReturnPortaledContentView:"
+ "_addPortaledNotificationBadgeForContentViewIfNeeded:"
+ "_alarmFiringChanged:"
+ "_allowsCapabilityLockScreenCameraSwipeWithExplanation:"
+ "_alphaAnimatableProperty"
+ "_alphaForIconOverlayView:crossfadeFraction:"
+ "_appLayoutToPin"
+ "_canWarmRealCamera"
+ "_containerViewIsVisible"
+ "_contentNotificationBadgePortalViews"
+ "_createAlphaAnimatableProperty"
+ "_detachmentThreshold"
+ "_dismissBannerWithActivityIdentifier:forceDismissal:"
+ "_doubleTapTopGestureRecognizer"
+ "_enforcesViewWindowRequirements"
+ "_flyZCurveFactor"
+ "_flyZResponse"
+ "_glassHighlight"
+ "_handlePrelaunchForTransitionToVisible:mode:"
+ "_handlePrewarmForTransitionToVisible:mode:"
+ "_hasPendingHostedEntityGoLiveRequest"
+ "_homeScreenIconIsSmallWidget"
+ "_iconAlphaResponse"
+ "_iconBadgeViewIfAnyInView:"
+ "_iconViewIfAnyInView:"
+ "_icrIconLayerIfAnyInLayer:"
+ "_interfaceOrientationFromUserResizeIfAny"
+ "_isPendingInvalidatablesForAcceleratedHomeGesture"
+ "_isWaitingForGlassHighlightDelay"
+ "_keyFillHighlightSDFView"
+ "_layoutSubviews_completionBlock"
+ "_layoutSubviews_skipLayoutNotification"
+ "_layoutSubviews_updateVisibleItemsAccessoryViewsLayoutAndStyleWithCompletion:"
+ "_passesHasVisibleWindowTest"
+ "_prefersInitialLayout"
+ "_requestedPIPEntity"
+ "_rimHighlightSDFView"
+ "_rubberBandedTranslation"
+ "_rubberBandingRange"
+ "_sdfElementView"
+ "_selectedDisplayItemWasInitiallyFullScreen"
+ "_setGlassHighlight:"
+ "_shouldAccelerateHomeGesture"
+ "_statusBarDoubleTapTop:"
+ "_supportsBlur"
+ "_supportsGlassHighlight"
+ "_targetVelocityForKey:"
+ "_updateAlarmFiringChangedWithAlarm:"
+ "_windowDragRubberBandedTranslationDetachmentThreshold"
+ "_windowDragRubberBandedTranslationRange"
+ "appLayoutToPin"
+ "applicationSceneViewController:statusBarDoubleTapped:"
+ "canWarmRealCamera"
+ "com.apple.SpringBoard.genie.badgePortalView.matchOpacity"
+ "com.apple.UIKit"
+ "com.apple.liquid_glass_legibility"
+ "containerViewDidDisappear"
+ "containerViewWillAppear"
+ "coverSheetViewController:didWakeForSource:"
+ "currentTargetVelocityValueForVisibleAppLayout:key:"
+ "defaultMultitaskingLayoutAttributesForDisplayItem:layoutAttributes:layoutGrid:"
+ "desktopSpaceItemsForSwitcherContentController:"
+ "enforcesViewWindowRequirements"
+ "fullScreenSwitcherSceneLiveContentOverlay:doubleTappedStatusBar:"
+ "genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:minimizedScale:containerSize:minimumOutsetSize:genieScale:multiplier:active:glassHighlight:layoutSettings:"
+ "glassHighlight"
+ "hasGlass"
+ "hasTintColor"
+ "homeScreenGlassHighlightForAppLayout:"
+ "iconFlyZCurveFactor"
+ "iconFlyZResponse"
+ "inPlaceDamping"
+ "inPlaceResponse"
+ "initWithAppLayoutToPin:"
+ "initWithProgress:velocity:supportsBlur:"
+ "initWithTransitionID:appLayout:progress:velocity:supportsBlur:"
+ "isFiring"
+ "isICRIconLayer"
+ "isIconBadgeView"
+ "isIconView"
+ "isPendingInvalidatablesForAcceleratedHomeGesture"
+ "isSnoozed"
+ "kSBFullScreenToHomeGlassHighlightDelayReason"
+ "lightDirection"
+ "lightIntensity"
+ "lockScreenCamera: %d, swipeAllowed: %d"
+ "medusaDecoratedDeviceApplicationSceneViewController:statusBarDoubleTapped:"
+ "modifierForGestureWithSelectedDisplayItem:context:"
+ "modifierForTransitionToAppLayout:context:"
+ "notificationViewControllerRequestCustomPlatterBackgroundView:"
+ "requestedPIPEntity"
+ "setAmount:"
+ "setAngle:"
+ "setAppLayoutToPin:"
+ "setCanWarmRealCamera:"
+ "setEnforcesViewWindowRequirements:"
+ "setFillHeightOffset:"
+ "setFillHeightScale:"
+ "setFillSpreadOffset:"
+ "setFillSpreadScale:"
+ "setFullScreenModifier:"
+ "setGlassHighlight:"
+ "setHostedEntityViewController:"
+ "setKeyHeightOffset:"
+ "setKeyHeightScale:"
+ "setKeySpreadOffset:"
+ "setKeySpreadScale:"
+ "setMinificationFilterBias:"
+ "setRequestedPIPEntity:"
+ "setSpread:"
+ "setSupportsGlassHighlight:"
+ "setWindowDragRubberBandedTranslationDetachmentThreshold:"
+ "setWindowDragRubberBandedTranslationRange:"
+ "setting"
+ "slideOverItemForSwitcherContentController:"
+ "supportsBlur"
+ "supportsGlassHighlight"
+ "v28@0:8@\"CSCoverSheetViewController\"16i24"
+ "v32@0:8@\"SBDeviceApplicationSceneViewController\"16@\"UITapGestureRecognizer\"24"
+ "v32@0:8@\"SBFullScreenSwitcherSceneLiveContentOverlay\"16@\"UITapGestureRecognizer\"24"
+ "v32@0:8@\"SBMedusaDecoratedDeviceApplicationSceneViewController\"16@\"UITapGestureRecognizer\"24"
+ "v56@0:8{SBSwitcherGenieGlassHighlight=Q{SBSwitcherGenieGlassHighlightDirection=ddd}d}16"
+ "windowDragRubberBandedTranslationDetachmentThreshold"
+ "windowDragRubberBandedTranslationRange"
+ "windowingConfigurationForInterfaceOrientation:"
+ "{?=\"switcherGestureManagerForSwitcherContentController\"b1\"sceneRelevancyManagerForSwitcherContentController\"b1\"switcherIconZoomContextProviderForSwitcherContentController\"b1\"homeGestureSettingsForSwitcherContentController\"b1\"maximumNumberOfScenesOnStageForSwitcherContentController\"b1\"activeTransientOverlayPresentedAppLayoutForSwitcherContentController\"b1\"appLayoutForWorkspaceTransientOverlay\"b1\"viewControllerForTransientOverlayAppLayout\"b1\"createWorkspaceTransientOverlayForAppLayout\"b1\"matchingIconViewForIconView\"b1\"prioritizesSortOrderForAppLayout\"b1\"switcherContentControllerFrameForFloatingAppLayoutInInterfaceOrientationFloatingConfiguration\"b1\"switcherContentControllerFrameForCenterItemWithConfigurationInterfaceOrientation\"b1\"homeScreenInterfaceOrientationForContentController\"b1\"backdropInterfaceStyleForContentController\"b1\"switcherContentControllerShouldMorphToPIPForTransitionContext\"b1\"switcherContentControllerShouldMorphFromPIPForTransitionContext\"b1\"isInAppStatusBarRequestedHiddenForSwitcherContentController\"b1\"leadingStatusBarPartFrameForSwitcherContentController\"b1\"trailingStatusBarPartFrameForSwitcherContentController\"b1\"switcherContentControllerVisibleAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerVisibleDisplayItemsForBundleIdentifier\"b1\"switcherContentControllerHiddenAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerReloadsSnapshotsForActiveInterfaceOrientationChange\"b1\"switcherContentControllerHasMultipleDisplays\"b1\"switcherContentControllerSupportsTitleItemsForAppLayout\"b1\"switcherContentControllerSupportsKillingOfAppLayout\"b1\"switcherContentControllerDisplayItemSupportsCenterRole\"b1\"switcherContentControllerIsKeyboardHomeAffordanceAssertionCurrentlyBeingTaken\"b1\"switcherContentControllerDeviceApplicationSceneHandleForDisplayItem\"b1\"isDisplayEmbeddedForSwitcherContentController\"b1\"windowManagementContextForSwitcherContentController\"b1\"draggingAppLayoutsForWindowDragForSwitcherContentController\"b1\"proposedAppLayoutsForWindowDragForSwitcherContentController\"b1\"isSwitcherContentControllerEphemeral\"b1\"displayConfigurationsOfOtherDisplaysForSwitcherContentController\"b1\"guardedForegroundDisplayItemsForSwitcherContentController\"b1\"desktopSpaceItemsForSwitcherContentController\"b1\"slideOverItemForSwitcherContentController\"b1\"windowingConfigurationForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1\"appLayoutForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1}"
+ "{SBSwitcherGenieGlassHighlight=\"style\"Q\"direction\"{SBSwitcherGenieGlassHighlightDirection=\"x\"d\"y\"d\"z\"d}\"intensity\"d}"
+ "{SBSwitcherGenieGlassHighlight=Q{SBSwitcherGenieGlassHighlightDirection=ddd}d}16@0:8"
+ "{SBSwitcherGenieGlassHighlight=Q{SBSwitcherGenieGlassHighlightDirection=ddd}d}24@0:8@\"SBAppLayout\"16"
+ "{SBSwitcherGenieGlassHighlight=Q{SBSwitcherGenieGlassHighlightDirection=ddd}d}24@0:8@16"
+ "{SBSwitcherGenieGlassHighlight=Q{SBSwitcherGenieGlassHighlightDirection=ddd}d}24@?0@\"SBChainableModifier\"8@16"
+ "\x95"
+ "\xf0a"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa2\xf0\xf01"
- "\t$)"
- "%{public}@ should begin: touch (%@) hit-tested to item container (%@) and was inside edge swipe hit test rect (%@)"
- "-[SBDoubleTapSystemGestureRecognizer initWithCoder:]"
- "11\xf1"
- "@\"SBAppExposeContinuousExposeSwitcherModifier\""
- "@\"SBDoubleTapSystemGestureRecognizer\""
- "@\"SBExposeWindowingModifier\""
- "@\"SBSwitcherWindowingConfiguration\"16@0:8"
- "@172@0:8{CGPoint=dd}16{CGPoint=dd}32{CGPoint=dd}48{CGSize=dd}64{CGSize=dd}80d96{CGSize=dd}104{CGSize=dd}120d136{CGPoint=dd}144B160@164"
- "@48@0:8@16@24d32d40"
- "SBAppExposeContinuousExposeSwitcherModifier"
- "SBAppExposeContinuousExposeSwitcherModifier.m"
- "SBContinuousExposeToAppExposeSwitcherModifier"
- "SBContinuousExposeToAppExposeSwitcherModifier.m"
- "SBContinuousExposeToAppExposeSwitcherModifier:%@"
- "SBDoubleTapSystemGestureRecognizer"
- "SBDoubleTapSystemGestureRecognizer.m"
- "T@\"NSString\",R,C,N,V_appExposeBundleID"
- "T@\"SBDoubleTapSystemGestureRecognizer\",&,N,V_windowTopRegionDoubleTapGestureRecognizer"
- "T@\"SBIndirectPanGestureRecognizer\",&,N,V_indirectDismissFloatingApplicationGestureRecognizer"
- "T@\"UITapGestureRecognizer\",&,N,V_windowTopRegionScrollToTopTapGestureRecognizer"
- "Td,N,V_lastTrackpadActivationTimestamp"
- "ToAppExpose"
- "ToSwitcher"
- "Window Scroll-to-Top Tap"
- "Window Top Region Double Tap"
- "_appExposeBundleID"
- "_cameraRestrictions"
- "_continuousExposeModifier"
- "_desktopSpaceAppLayout"
- "_handleDoubleTapGesture:"
- "_handleScrollToTopGesture:"
- "_hasAnyUnadjustedAppLayoutsInDuality"
- "_isInPeekState"
- "_lastTrackpadActivationTimestamp"
- "_shouldBeginWindowTopRegionTapGesture:"
- "_shouldTopRegionDoubleTapGesture:receiveTouch:"
- "_shouldTopRegionScrollToTopGesture:receiveTouch:"
- "_statusBarDoubleTapGestureRecognizer"
- "_statusBarScrollToTopTapGestureRecognizer"
- "_windowTopRegionDoubleTapGestureRecognizer"
- "_windowTopRegionScrollToTopTapGestureRecognizer"
- "coverSheetViewControllerDidWakeForSource:"
- "e"
- "friction"
- "genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:minimizedScale:containerSize:minimumOutsetSize:genieScale:multiplier:active:layoutSettings:"
- "inPlaceFriction"
- "inPlaceTension"
- "initWithProgress:velocity:"
- "initWithTransitionID:appExposeBundleID:direction:appExposeModifier:"
- "initWithTransitionID:appLayout:progress:velocity:"
- "initWithTransitionID:direction:continuousExposeModifier:"
- "kSBAppExposeContinuousExposeReopenReason"
- "lastTrackpadActivationTimestamp"
- "minimumCustomElementHeightUnderSensor"
- "note: dispatching switcher event with duality app layouts"
- "note: performing implicit switcher layout with duality app layouts"
- "setLastTrackpadActivationTimestamp:"
- "setWindowTopRegionDoubleTapGestureRecognizer:"
- "setWindowTopRegionScrollToTopTapGestureRecognizer:"
- "tension"
- "windowTopRegionDoubleTapGestureRecognizer"
- "windowTopRegionScrollToTopTapGestureRecognizer"
- "{?=\"switcherGestureManagerForSwitcherContentController\"b1\"sceneRelevancyManagerForSwitcherContentController\"b1\"switcherIconZoomContextProviderForSwitcherContentController\"b1\"homeGestureSettingsForSwitcherContentController\"b1\"maximumNumberOfScenesOnStageForSwitcherContentController\"b1\"activeTransientOverlayPresentedAppLayoutForSwitcherContentController\"b1\"appLayoutForWorkspaceTransientOverlay\"b1\"viewControllerForTransientOverlayAppLayout\"b1\"createWorkspaceTransientOverlayForAppLayout\"b1\"matchingIconViewForIconView\"b1\"prioritizesSortOrderForAppLayout\"b1\"switcherContentControllerFrameForFloatingAppLayoutInInterfaceOrientationFloatingConfiguration\"b1\"switcherContentControllerFrameForCenterItemWithConfigurationInterfaceOrientation\"b1\"homeScreenInterfaceOrientationForContentController\"b1\"backdropInterfaceStyleForContentController\"b1\"switcherContentControllerShouldMorphToPIPForTransitionContext\"b1\"switcherContentControllerShouldMorphFromPIPForTransitionContext\"b1\"isInAppStatusBarRequestedHiddenForSwitcherContentController\"b1\"leadingStatusBarPartFrameForSwitcherContentController\"b1\"trailingStatusBarPartFrameForSwitcherContentController\"b1\"switcherContentControllerVisibleAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerVisibleDisplayItemsForBundleIdentifier\"b1\"switcherContentControllerHiddenAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerReloadsSnapshotsForActiveInterfaceOrientationChange\"b1\"switcherContentControllerHasMultipleDisplays\"b1\"switcherContentControllerSupportsTitleItemsForAppLayout\"b1\"switcherContentControllerSupportsKillingOfAppLayout\"b1\"switcherContentControllerDisplayItemSupportsCenterRole\"b1\"switcherContentControllerIsKeyboardHomeAffordanceAssertionCurrentlyBeingTaken\"b1\"switcherContentControllerDeviceApplicationSceneHandleForDisplayItem\"b1\"isDisplayEmbeddedForSwitcherContentController\"b1\"windowManagementContextForSwitcherContentController\"b1\"draggingAppLayoutsForWindowDragForSwitcherContentController\"b1\"proposedAppLayoutsForWindowDragForSwitcherContentController\"b1\"isSwitcherContentControllerEphemeral\"b1\"displayConfigurationsOfOtherDisplaysForSwitcherContentController\"b1\"guardedForegroundDisplayItemsForSwitcherContentController\"b1\"windowingConfigurationForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1\"appLayoutForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1}"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x92\xf0\xf01"

```
