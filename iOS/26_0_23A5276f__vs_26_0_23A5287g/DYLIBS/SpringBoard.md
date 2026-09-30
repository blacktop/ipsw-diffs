## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4556.102.0.0.0
-  __TEXT.__text: 0xa66238
-  __TEXT.__auth_stubs: 0x5520
+4557.0.3.103.0
+  __TEXT.__text: 0xa77db4
+  __TEXT.__auth_stubs: 0x5550
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb5c40
-  __TEXT.__const: 0x12b80
-  __TEXT.__oslogstring: 0x5d059
-  __TEXT.__cstring: 0x7bb14
-  __TEXT.__gcc_except_tab: 0x168b8
+  __TEXT.__objc_methlist: 0xb6c28
+  __TEXT.__const: 0x12ba0
+  __TEXT.__oslogstring: 0x5d375
+  __TEXT.__cstring: 0x7c54f
+  __TEXT.__gcc_except_tab: 0x16da0
   __TEXT.__ustring: 0xcac
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2ac78
+  __TEXT.__unwind_info: 0x2bcb8
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x21dcc
-  __TEXT.__objc_methname: 0x1c9729
-  __TEXT.__objc_methtype: 0x4c00a
-  __TEXT.__objc_stubs: 0xf11a0
-  __DATA_CONST.__got: 0xa0a0
-  __DATA_CONST.__const: 0x1c5d0
-  __DATA_CONST.__objc_classlist: 0x51c8
+  __TEXT.__objc_classname: 0x21ed7
+  __TEXT.__objc_methname: 0x1cb865
+  __TEXT.__objc_methtype: 0x4c18f
+  __TEXT.__objc_stubs: 0xf1e00
+  __DATA_CONST.__got: 0xa0f0
+  __DATA_CONST.__const: 0x1c938
+  __DATA_CONST.__objc_classlist: 0x5208
   __DATA_CONST.__objc_catlist: 0x348
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x49ce0
-  __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x3f00
-  __DATA_CONST.__objc_arraydata: 0x17e0
-  __AUTH_CONST.__auth_got: 0x2aa8
-  __AUTH_CONST.__const: 0x10718
-  __AUTH_CONST.__cfstring: 0x6e0a0
-  __AUTH_CONST.__objc_const: 0x263b00
-  __AUTH_CONST.__objc_arrayobj: 0x1728
-  __AUTH_CONST.__objc_doubleobj: 0x600
-  __AUTH_CONST.__objc_intobj: 0x2b68
-  __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH.__objc_data: 0x104f0
-  __DATA.__objc_ivar: 0xf040
+  __DATA_CONST.__objc_selrefs: 0x4a130
+  __DATA_CONST.__objc_protorefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0x3f50
+  __DATA_CONST.__objc_arraydata: 0x1858
+  __AUTH_CONST.__auth_got: 0x2ac0
+  __AUTH_CONST.__const: 0x10828
+  __AUTH_CONST.__cfstring: 0x6e5a0
+  __AUTH_CONST.__objc_const: 0x266518
+  __AUTH_CONST.__objc_arrayobj: 0x1770
+  __AUTH_CONST.__objc_doubleobj: 0x680
+  __AUTH_CONST.__objc_intobj: 0x2b98
+  __AUTH_CONST.__objc_dictobj: 0x320
+  __AUTH.__objc_data: 0x107c0
+  __DATA.__objc_ivar: 0xf1a0
   __DATA.__data: 0x1f680
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xac8
   __DATA.__common: 0xa40
-  __DATA_DIRTY.__objc_data: 0x22ce0
+  __DATA_DIRTY.__objc_data: 0x22c90
   __DATA_DIRTY.__data: 0x180
   __DATA_DIRTY.__bss: 0x1a50
   __DATA_DIRTY.__common: 0x50

   - /System/Library/PrivateFrameworks/PosterBoardUI.framework/PosterBoardUI
   - /System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices
   - /System/Library/PrivateFrameworks/PosterKit.framework/PosterKit
+  - /System/Library/PrivateFrameworks/PosterLegibilityKit.framework/PosterLegibilityKit
   - /System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: D614885C-607B-39E1-B91F-A3C41176BC1B
-  Functions: 69268
-  Symbols:   234385
-  CStrings:  103107
+  UUID: 7D7351AA-49A5-3547-B6DD-EDD0FAA51107
+  Functions: 69678
+  Symbols:   235573
+  CStrings:  103450
 
Symbols:
+ +[SBSplitViewHandleNubView nubHitTestSize]
+ -[SBActivationInfoViewController _adjustMobileEquipmentLayout:]
+ -[SBActivationInfoViewController _processMobileEquipmentInfo:forSlot:]
+ -[SBActivationInfoViewController _shouldGroupIMEIsForPrimary:secondary:]
+ -[SBActivityCoverSheetObserver _dismissAlertForItem:]
+ -[SBActivityCoverSheetObserver _dismissAlertForItem:].cold.1
+ -[SBAppExposeToAppWindowingModifier shouldInterruptForActivity:]
+ -[SBAppExposeToHomeWindowingModifier didComplete]
+ -[SBAppExposeToHomeWindowingModifier shouldInterruptForActivity:]
+ -[SBAppExposeWindowingModifier desktopSpaceDisplayItems]
+ -[SBAppSwitcherModel recentAppLayouts:didMoveAppLayoutToFront:]
+ -[SBApplicationInfo browserEngineIsRegionallyRestricted]
+ -[SBApplicationInfo embeddedBrowserEngineIsRegionallyRestricted]
+ -[SBApplicationInfo isAppLibraryOnlyByDefault]
+ -[SBAssistantController setShouldDismissForWorkspaceTransitions:]
+ -[SBAssistantController shouldDismissForWorkspaceTransitions]
+ -[SBAssistantController siriPresentation:didUpdateShouldDismissForWorkspaceTransitions:]
+ -[SBAssistantSceneController windowSceneDidDisconnect:]
+ -[SBContinuousExposeAppToAppModifier fadeInDelayForSplitViewHandles]
+ -[SBContinuousExposeArcSwipeSwitcherModifier fadeInDelayForSplitViewHandles]
+ -[SBContinuousExposeArcSwipeSwitcherModifier handleTimerEvent:]
+ -[SBContinuousExposeArcSwipeSwitcherModifier transitionWillUpdate]
+ -[SBContinuousExposeArcSwipeSwitcherModifier visibleSplitViewHandleDimmingViews]
+ -[SBContinuousExposeArcSwipeSwitcherModifier visibleSplitViewHandleNubViews]
+ -[SBContinuousExposeHomeGestureRootSwitcherModifier preferredAppLayoutToReuseAccessoryForAppLayout:fromAppLayouts:]
+ -[SBContinuousExposeHomeGestureSwitcherModifier _beginAnimatingExposeMultitaskingPropertyWithMode:settings:]
+ -[SBContinuousExposeHomeGestureSwitcherModifier _frameOffsetForTranslation:]
+ -[SBContinuousExposeHomeGestureSwitcherModifier _getActivePositionAndScaleForLayoutRole:inAppLayout:withBounds:outPosition:outScale:]
+ -[SBContinuousExposeHomeGestureSwitcherModifier contentOffsetForIndex:alignment:]
+ -[SBContinuousExposeHomeGestureSwitcherModifier initWithGestureID:selectedAppLayout:startingEnvironmentMode:multitaskingModifier:scrunchInitiated:continuingGesture:lastGestureWasAnArcSwipe:]
+ -[SBContinuousExposeHomeGestureSwitcherModifier visibleSplitViewHandleDimmingViews]
+ -[SBContinuousExposeHomeGestureSwitcherModifier visibleSplitViewHandleNubViews]
+ -[SBContinuousExposeSwitcherToAppModifier adjustedAppLayoutsForAppLayouts:]
+ -[SBContinuousExposeSwitcherToAppModifier appLayoutsToEnsureExistForMainTransitionEvent:]
+ -[SBContinuousExposeSwitcherToAppModifier didMoveToParentModifier:]
+ -[SBContinuousExposeSwitcherToAppModifier fadeInDelayForSplitViewHandles]
+ -[SBContinuousExposeToHomeSwitcherModifier adjustedAppLayoutsForAppLayouts:]
+ -[SBContinuousExposeWindowDragContainerSwitcherModifier visibleSplitViewHandleDimmingViews]
+ -[SBContinuousExposeWindowDragContainerSwitcherModifier visibleSplitViewHandleNubViews]
+ -[SBContinuousExposeWindowDropSwitcherModifier fadeInDelayForSplitViewHandles]
+ -[SBCoplanarSwitcherModifier ignoredAppLayout]
+ -[SBCoplanarSwitcherModifier setIgnoredAppLayout:]
+ -[SBCoverSheetPresentationManager coverSheetViewController:didObscureWallpaper:]
+ -[SBCoverSheetPresentationManager coverSheetViewController:didOccludeWallpaper:]
+ -[SBDefaultImplementationsSwitcherModifier fadeInDelayForSplitViewHandles]
+ -[SBDefaultImplementationsSwitcherModifier frameForSplitViewHandleDimmingView:]
+ -[SBDefaultImplementationsSwitcherModifier frameForSplitViewHandleNubView:]
+ -[SBDefaultImplementationsSwitcherModifier visibleSplitViewHandleDimmingViews]
+ -[SBDefaultImplementationsSwitcherModifier visibleSplitViewHandleNubViews]
+ -[SBDeviceApplicationSceneHandle _safeAreaCornerInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]
+ -[SBDeviceApplicationSceneHandle effectiveStatusBarStyleRequestForActivationSettings:]
+ -[SBDeviceApplicationSceneHandle isStatusBarHiddenForActivationSettings:withOrientation:]
+ -[SBDeviceApplicationSceneHandle safeAreaEdgeInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]
+ -[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]
+ -[SBDisplayItemLayoutAttributes _appendPropertiesToBuilder:]
+ -[SBDisplayItemLayoutAttributes _initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:]
+ -[SBDisplayItemLayoutAttributes attributesByModifyingCascaded:]
+ -[SBDisplayItemLayoutAttributes debugDescription]
+ -[SBDisplayItemLayoutAttributes initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:normalizedCenter:cascaded:]
+ -[SBDisplayItemLayoutAttributes initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:]
+ -[SBDisplayItemLayoutAttributes isCascaded]
+ -[SBDisplayItemLayoutAttributesDebugView .cxx_destruct]
+ -[SBDisplayItemLayoutAttributesDebugView initWithFrame:]
+ -[SBDisplayItemLayoutAttributesDebugView layoutAttributes]
+ -[SBDisplayItemLayoutAttributesDebugView setLayoutAttributes:]
+ -[SBDisplayItemLayoutAttributesProvider .cxx_destruct]
+ -[SBDisplayItemLayoutAttributesProvider _layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:]
+ -[SBDisplayItemLayoutAttributesProvider _shouldUpdateForDisplayOrdinal:]
+ -[SBDisplayItemLayoutAttributesProvider delegate]
+ -[SBDisplayItemLayoutAttributesProvider init]
+ -[SBDisplayItemLayoutAttributesProvider lastInteractedDisplayItemInAppLayout:orientation:passingTest:]
+ -[SBDisplayItemLayoutAttributesProvider layoutAttributesEntriesForAppLayout:]
+ -[SBDisplayItemLayoutAttributesProvider layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:]
+ -[SBDisplayItemLayoutAttributesProvider layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.1
+ -[SBDisplayItemLayoutAttributesProvider layoutAttributesMapForAppLayout:displayOrdinal:orientation:]
+ -[SBDisplayItemLayoutAttributesProvider setDelegate:]
+ -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:forKey:]
+ -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]
+ -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.1
+ -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.2
+ -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.3
+ -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributesMap:forAppLayout:displayOrdinal:orientation:]
+ -[SBDisplayItemLayoutAttributesProvider zOrderedItemsInAppLayout:orientation:]
+ -[SBDockToStageZoomWindowingModifier fadeInDelayForSplitViewHandles]
+ -[SBDockToStageZoomWindowingModifier initWithAppLayout:addingToStage:]
+ -[SBDockToStageZoomWindowingModifier initWithAppLayout:addingToStage:].cold.1
+ -[SBDockToStageZoomWindowingModifier launchingOverDesktopSpaceAppLayout]
+ -[SBDockToStageZoomWindowingModifier setLaunchingOverDesktopSpaceAppLayout:]
+ -[SBDynamicLightingController criticalThermalLevelDynamicLightingAssertion]
+ -[SBDynamicLightingController didChangeThermalLevel:]
+ -[SBDynamicLightingController thermalBlockStatusChanged:]
+ -[SBExposeWindowingModifier organicExposeAppLayout]
+ -[SBExposeWindowingModifier visibleSplitViewHandleDimmingViews]
+ -[SBExposeWindowingModifier visibleSplitViewHandleNubViews]
+ -[SBExternalDisplayEducationPillViewController init]
+ -[SBFileStackOpenIndicatorView iconImageInfo]
+ -[SBFileStackOpenIndicatorView setIconImageInfo:]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier _layoutSettings]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier adjustedAppLayoutsForAppLayouts:]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier animationAttributesForLayoutElement:]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier appLayoutsToCacheFullsizeSnapshots]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier appLayoutsToCacheSnapshots]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier appLayoutsToEnsureExistForMainTransitionEvent:]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier appLayoutsToResignActive]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier asyncRenderingAttributesForAppLayout:]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier cornerRadiiForIndex:]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier fadeInDelayForSplitViewHandles]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier handleTimerEvent:]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier homeScreenBackdropBlurType]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:pinSpaceCornerRadiiToDisplayCornerRadii:]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:pinSpaceCornerRadiiToDisplayCornerRadii:].cold.1
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier isContentStatusBarVisibleForIndex:]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier isHomeScreenContentRequired]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier isSwitcherWindowUserInteractionEnabled]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier isSwitcherWindowVisible]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier isWallpaperRequiredForSwitcher]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier keyboardSuppressionMode]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier shouldAsyncRenderUntilDelay:]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier shouldPerformCrossfadeForReduceMotion]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier transitionDidEnd]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier transitionWillBegin]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier transitionWillUpdate]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier visibleAppLayouts]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier visibleSplitViewHandleDimmingViews]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier visibleSplitViewHandleNubViews]
+ -[SBFlexibleWindowingArcSwipeSwitcherModifier wallpaperStyle]
+ -[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:fullScreenRectsIfAny:]
+ -[SBFlexibleWindowingAutoLayoutController _effectiveStageAreaForSnappingForSpace:configuration:]
+ -[SBFlexibleWindowingAutoLayoutController _updateOccupiedAreaForSpace:configuration:]
+ -[SBFlexibleWindowingAutoLayoutGroup intersectionHeight]
+ -[SBFlexibleWindowingAutoLayoutSpace occupiedAreaPercentage]
+ -[SBFlexibleWindowingAutoLayoutSpace setOccupiedAreaPercentage:]
+ -[SBFlexibleWindowingExposeToHomePeekWindowingModifier cornersForItem:]
+ -[SBFlexibleWindowingExposeToHomePeekWindowingModifier shouldInterruptForActivity:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier _beginAnimatingExposeMultitaskingPropertyWithMode:settings:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier _layoutSettingsForAppLayout:layoutSettings:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier _scaleForAdjacentCards]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier _updateStackedProgress]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier adjustedAppLayoutsForAppLayouts:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier contentOffsetForIndex:alignment:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier headerStyleForIndex:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier initWithGestureID:selectedAppLayout:startingEnvironmentMode:multitaskingModifier:scrunchInitiated:continuingGesture:lastGestureWasAnArcSwipe:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier isHitTestBlockingViewVisible]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier lighteningAlphaForIndex:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier perspectiveAngleForIndex:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier titleAndIconOpacityForIndex:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier titleOpacityForIndex:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier visibleSplitViewHandleDimmingViews]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier visibleSplitViewHandleNubViews]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier wallpaperOverlayAlphaForIndex:]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier appLayoutsToCacheFullsizeSnapshots]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier appLayoutsToCacheSnapshots]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier didMoveToParentModifier:]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier frameForIndex:]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier homeScreenDimmingAlpha]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier topMostLayoutElements]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier visibleAppLayouts]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier visibleSplitViewHandleDimmingViews]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier visibleSplitViewHandleNubViews]
+ -[SBFlexibleWindowingToAppExposeWindowingModifier didComplete]
+ -[SBFlexibleWindowingToAppExposeWindowingModifier shouldInterruptForActivity:]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier homeScreenDimmingAlpha]
+ -[SBFloatingDockRemoteContentManager handleFloatingDockFrameDidChange:]
+ -[SBFluidSwitcherAnimationSettings setSplitViewHandleFadeInSettings:]
+ -[SBFluidSwitcherAnimationSettings setSplitViewHandleFadeOutSettings:]
+ -[SBFluidSwitcherAnimationSettings splitViewHandleFadeInSettings]
+ -[SBFluidSwitcherAnimationSettings splitViewHandleFadeOutSettings]
+ -[SBFluidSwitcherGestureManager _isTouchLocationInSplitViewGutter:]
+ -[SBFluidSwitcherGestureWorkspaceTransaction _beginDeferringCompletionForReason:]
+ -[SBFluidSwitcherGestureWorkspaceTransaction _endDeferringCompletionForReason:]
+ -[SBFluidSwitcherGestureWorkspaceTransaction _isDeferringCompletionForAnyReason]
+ -[SBFluidSwitcherGestureWorkspaceTransaction _isDeferringCompletionForReason:]
+ -[SBFluidSwitcherGestureWorkspaceTransaction _shouldComplete]
+ -[SBFluidSwitcherGestureWorkspaceTransaction completionDeferralReasons]
+ -[SBFluidSwitcherGestureWorkspaceTransaction setCompletionDeferralReasons:]
+ -[SBFluidSwitcherLayoutContext userDidClickInApp]
+ -[SBFluidSwitcherLayoutContext wantsUserClickInAppInteractionEvent]
+ -[SBFluidSwitcherViewController _updateVisibleSplitViewHandleDimmingViews]
+ -[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]
+ -[SBFluidSwitcherViewController hitTestedToSplitViewHandle:window:]
+ -[SBFluidSwitcherViewController setVisibleSplitViewHandleDimmingViews:]
+ -[SBFluidSwitcherViewController setVisibleSplitViewHandleDimmingViewsWaitingForFadeIn:]
+ -[SBFluidSwitcherViewController setVisibleSplitViewHandleNubViews:]
+ -[SBFluidSwitcherViewController setVisibleSplitViewHandleNubViewsWaitingForFadeIn:]
+ -[SBFluidSwitcherViewController visibleSplitViewHandleDimmingViewsWaitingForFadeIn]
+ -[SBFluidSwitcherViewController visibleSplitViewHandleDimmingViews]
+ -[SBFluidSwitcherViewController visibleSplitViewHandleNubViewsWaitingForFadeIn]
+ -[SBFluidSwitcherViewController visibleSplitViewHandleNubViews]
+ -[SBFullScreenContinuousExposeSwitcherModifier frameForSplitViewHandleDimmingView:]
+ -[SBFullScreenContinuousExposeSwitcherModifier frameForSplitViewHandleNubView:]
+ -[SBFullScreenContinuousExposeSwitcherModifier visibleSplitViewHandleDimmingViews]
+ -[SBFullScreenContinuousExposeSwitcherModifier visibleSplitViewHandleNubViews]
+ -[SBFullScreenToHomeCenterZoomDownSwitcherModifier fadeInDelayForSplitViewHandles]
+ -[SBFullScreenToHomeIconZoomSwitcherModifier _flexibleAutoLayoutSpaceForZoomingAppLayout]
+ -[SBFullScreenToHomeIconZoomSwitcherModifier _numberOfPeekingItemsAboveDisplayItem:zOrderedItems:]
+ -[SBFullScreenToHomeIconZoomSwitcherModifier fadeInDelayForSplitViewHandles]
+ -[SBFullScreenToHomeIconZoomSwitcherModifier transitionWillUpdate]
+ -[SBFullScreenToPeekAnimationModifier .cxx_destruct]
+ -[SBFullScreenToPeekAnimationModifier fadeInDelayForSplitViewHandles]
+ -[SBFullScreenToPeekAnimationModifier shouldInterruptForActivity:]
+ -[SBHomePeekToFullScreenTransitionModifier animationAttributesForItem:]
+ -[SBHomePeekToFullScreenTransitionModifier completesWhenChildrenComplete]
+ -[SBHomePeekToFullScreenTransitionModifier fadeInDelayForSplitViewHandles]
+ -[SBHomePeekToFullScreenTransitionModifier frameForItem:]
+ -[SBHomePeekToFullScreenTransitionModifier frameForLayoutRole:inAppLayout:withBounds:]
+ -[SBHomePeekToFullScreenTransitionModifier initWithTransitionModifier:slidingOffPeekingAppLayout:fromPeekingConfiguration:]
+ -[SBHomePeekToFullScreenTransitionModifier initWithTransitionModifier:slidingOffPeekingAppLayout:fromPeekingConfiguration:].cold.1
+ -[SBHomePeekToFullScreenTransitionModifier opacityForItem:]
+ -[SBHomePeekToFullScreenTransitionModifier perspectiveAngleForLayoutRole:inAppLayout:]
+ -[SBHomePeekToFullScreenTransitionModifier scaleForLayoutRole:inAppLayout:]
+ -[SBHomePeekToFullScreenTransitionModifier shouldUseAnchorPointToPinLayoutRolesToSpace:]
+ -[SBHomePeekToFullScreenTransitionModifier topMostItems]
+ -[SBHomePeekToFullScreenTransitionModifier wantsSpaceAccessoryViewGenieForAppLayout:]
+ -[SBHomePeekToHomeTransitionModifier initWithFromAppLayout:fromConfiguration:]
+ -[SBHomePeekToHomeTransitionModifier initWithFromAppLayout:fromConfiguration:].cold.1
+ -[SBHomePeekToHomeTransitionModifier scaleForLayoutRole:inAppLayout:]
+ -[SBHomePeekToHomeTransitionModifier shouldInterruptForActivity:]
+ -[SBHomePeekWindowingModifier _updateForcePeekingEdgeIfNeeded]
+ -[SBHomePeekWindowingModifier initWithPeekingAppLayout:configuration:]
+ -[SBHomePeekWindowingModifier initWithPeekingAppLayout:configuration:].cold.1
+ -[SBHomePeekWindowingModifier initWithPeekingAppLayout:configuration:].cold.2
+ -[SBHomePeekWindowingModifier layoutViewModelsIfNeeded]
+ -[SBHomePeekWindowingModifier willBegin]
+ -[SBHomeScreenController iconManager:shouldPreviewOverlapMenuForIconView:]
+ -[SBHomeScreenController(AppearanceControlling) setHomeScreenDimmingAlpha:settings:behaviorMode:completion:]
+ -[SBHomeScreenService osMigrationDefaultHomeScreenLayout]
+ -[SBHomeScreenService osMigrationDefaultHomeScreenLayout].cold.1
+ -[SBHomeToSwitcherSwitcherModifier fadeInDelayForSplitViewHandles]
+ -[SBIconModel exportedOSMigrationDefaultHomeScreenLayout]
+ -[SBIconModel osMigrationHomeScreenLayoutForRootFolder:]
+ -[SBInCallPresentationManager isSceneHandleKillableInSwitcher:]
+ -[SBInCallPresentationSession isKillableInSwitcher]
+ -[SBInteractiveScreenshotGestureCropsView _didSetCompositingFilter]
+ -[SBInteractiveScreenshotGestureCropsView _didSetCornerAlpha]
+ -[SBInteractiveScreenshotGestureCropsView _didSetCornerColor]
+ -[SBInteractiveScreenshotGestureCropsView _didSetGrabberLineWidth]
+ -[SBInteractiveScreenshotGestureCropsView _setupUI]
+ -[SBInteractiveScreenshotGestureRootViewController _contentScaleForCommitProgress:contentInsets:additionalContentTranslation:]
+ -[SBInteractiveScreenshotGestureRoundedCropsView .cxx_destruct]
+ -[SBInteractiveScreenshotGestureRoundedCropsView _didSetCompositingFilter]
+ -[SBInteractiveScreenshotGestureRoundedCropsView _didSetCornerAlpha]
+ -[SBInteractiveScreenshotGestureRoundedCropsView _didSetCornerColor]
+ -[SBInteractiveScreenshotGestureRoundedCropsView _didSetGrabberLineWidth]
+ -[SBInteractiveScreenshotGestureRoundedCropsView _setPresentationValue:forKey:]
+ -[SBInteractiveScreenshotGestureRoundedCropsView _setupUI]
+ -[SBInteractiveScreenshotGestureRoundedCropsView _updateBorderViewMaskWithRect:]
+ -[SBInteractiveScreenshotGestureRoundedCropsView _updateGeometryForBounds:shouldUsePresentationValues:]
+ -[SBInteractiveScreenshotGestureRoundedCropsView _updateUI]
+ -[SBItemResizeTransitionSwitcherModifier fadeInDelayForSplitViewHandles]
+ -[SBKeyboardFocusLockReason _initReasonWithName:strength:avoidOverridingAppFocusOnOtherDisplays:]
+ -[SBKeyboardFocusLockReason avoidOverridingAppFocusOnOtherDisplays]
+ -[SBLockElementViewProvider _updateRequiredPriorityAssertion]
+ -[SBLockElementViewProvider isEmpty]
+ -[SBLockElementViewProvider requiredPriorityAssertion]
+ -[SBLockElementViewProvider setEmpty:].cold.1
+ -[SBLockElementViewProvider setRequiredPriorityAssertion:]
+ -[SBMainDisplaySceneManager wantsDisableIdleTimer]
+ -[SBMainDisplaySceneManager windowSceneDidDisconnect:]
+ -[SBMainSwitcherControllerCoordinator _windowManagementContextIsSingleAppModeForSwitcherCorrespondingToDisplayOrdinal:]
+ -[SBMainSwitcherControllerCoordinator appSwitcherModel:didMoveAppLayoutToFront:]
+ -[SBMainSwitcherControllerCoordinator shouldForceFullscreenForDisplayOrdinal:]
+ -[SBMainSwitcherControllerCoordinator shouldUpdateLayoutAttributesForDisplayOrdinal:]
+ -[SBMainSwitcherControllerCoordinator switcherContentController:setHomeScreenDimmingAlpha:withSettings:animationMode:completion:]
+ -[SBMainWorkspace _defaultSiriWorkspaceTransitionOptions]
+ -[SBMainWorkspace _defaultSiriWorkspaceTransitionOptions].cold.1
+ -[SBMainWorkspace _defaultSiriWorkspaceTransitionOptions].cold.2
+ -[SBMainWorkspace _siriWorkspaceTransitionOptionsFromOpenApplicationOptions:]
+ -[SBMenuBarMainMenuView _menuBarTitleFontFromStatusBarFont:]
+ -[SBMenuBarMainMenuView isDismissingMenuForPointerHover]
+ -[SBMenuBarMainMenuView prepareToPresentMenuForIndirectInput]
+ -[SBMenuBarMainMenuView presentingMenuForIndirectInput]
+ -[SBMenuBarMainMenuView setDismissingMenuForPointerHover:]
+ -[SBMenuBarMainMenuView setPresentingMenuForIndirectInput:]
+ -[SBMenuBarManager _dismissMenuBarWithCompletion:]
+ -[SBMenuBarManager _handleContentSizeCategoryDidChange:]
+ -[SBMenuBarManager _handleGuidedAccessActivationChanged:]
+ -[SBMenuBarManager _isMenuBarGenerallyDisabled]
+ -[SBMenuBarManager guidedAccessSystemGestureDisableAssertion]
+ -[SBMenuBarManager setGuidedAccessSystemGestureDisableAssertion:]
+ -[SBMenuBarManager toggleMenuBarVisibilityForSystemKeyboardShortcut]
+ -[SBMenuBarViewController _navigateToNextMenuHeaderForArrowKeyPress:]
+ -[SBMenuBarViewController _presentMenuViewNonInteractively:]
+ -[SBMenuBarViewController additionalKeyboardShortcutActionsForSession]
+ -[SBMenuBarViewController leftArrowNavigationAction]
+ -[SBMenuBarViewController openApplicationMenu]
+ -[SBMenuBarViewController rightArrowNavigationAction]
+ -[SBMenuBarViewController setLeftArrowNavigationAction:]
+ -[SBMenuBarViewController setRightArrowNavigationAction:]
+ -[SBPBDisplayItemLayoutAttributes cascaded]
+ -[SBPBDisplayItemLayoutAttributes setCascaded:]
+ -[SBPIPController _keyboardWillChangeFrame:]
+ -[SBPIPController _keyboardWillRotate:]
+ -[SBPIPController _keyboardWillShowOrHide:]
+ -[SBPIPControllerCoordinator acquireAssertionToPreventVideoCallPIPFromStartingUnderControlCenter:]
+ -[SBPhoneSceneSnapshotRequestStrategy .cxx_destruct]
+ -[SBPhoneSceneSnapshotRequestStrategy _handleRealTimeAppearanceChange:]
+ -[SBPhoneSceneSnapshotRequestStrategy _loadLastAppearanceChangeWithCompletion:]
+ -[SBPhoneSceneSnapshotRequestStrategy _startObservingAppearanceChanges]
+ -[SBPhoneSceneSnapshotRequestStrategy _stopObservingAppearanceChanges]
+ -[SBPhoneSceneSnapshotRequestStrategy _subscribeToAppearanceChanges]
+ -[SBPhoneSceneSnapshotRequestStrategy _updateLastAppearanceTimestamp:]
+ -[SBPhoneSceneSnapshotRequestStrategy appearancePublisher]
+ -[SBPhoneSceneSnapshotRequestStrategy appearanceQueue]
+ -[SBPhoneSceneSnapshotRequestStrategy dealloc]
+ -[SBPhoneSceneSnapshotRequestStrategy init]
+ -[SBPhoneSceneSnapshotRequestStrategy isObserving]
+ -[SBPhoneSceneSnapshotRequestStrategy lastAppearanceTimestamp]
+ -[SBPhoneSceneSnapshotRequestStrategy setAppearancePublisher:]
+ -[SBPhoneSceneSnapshotRequestStrategy setAppearanceQueue:]
+ -[SBPhoneSceneSnapshotRequestStrategy setIsObserving:]
+ -[SBPhoneSceneSnapshotRequestStrategy setLastAppearanceTimestamp:]
+ -[SBPhoneSceneSnapshotRequestStrategy snapshotRequestsForSceneHandle:settings:snapshotRequestContext:].cold.1
+ -[SBPuffAwayItemWindowingModifier shouldInterruptForActivity:]
+ -[SBRegionallyRestrictedAlertItem .cxx_destruct]
+ -[SBRegionallyRestrictedAlertItem initWithApplication:]
+ -[SBRestoreDesktopSpaceWindowingModifier .cxx_destruct]
+ -[SBRestoreDesktopSpaceWindowingModifier frameForItem:]
+ -[SBRestoreDesktopSpaceWindowingModifier launchingOverDesktopSpaceAppLayout]
+ -[SBRestoreDesktopSpaceWindowingModifier setLaunchingOverDesktopSpaceAppLayout:]
+ -[SBRestoreDesktopSpaceWindowingModifier shouldInterruptForActivity:]
+ -[SBRestoreDesktopSpaceWindowingModifier transitionDidComplete:]
+ -[SBRestoreDesktopSpaceWindowingModifier transitionWillBegin:]
+ -[SBRoutingSwitcherModifier fadeInDelayForSplitViewHandles]
+ -[SBRoutingSwitcherModifier frameForSplitViewHandleDimmingView:]
+ -[SBRoutingSwitcherModifier frameForSplitViewHandleNubView:]
+ -[SBRoutingSwitcherModifier visibleSplitViewHandleDimmingViews]
+ -[SBRoutingSwitcherModifier visibleSplitViewHandleNubViews]
+ -[SBSAElementRemovalTransitionProvider .cxx_destruct]
+ -[SBSAElementRemovalTransitionProvider description]
+ -[SBSAElementRemovalTransitionProvider preferencesFromContext:]
+ -[SBSAElementRemovalTransitionProvider preferencesFromContext:].cold.1
+ -[SBSAElementRemovalTransitionProvider preferencesFromContext:].cold.2
+ -[SBSAElementRemovalTransitionProvider preferencesFromContext:].cold.3
+ -[SBSAElementRemovalTransitionProvider preferencesFromContext:].cold.4
+ -[SBSAElementRemovalTransitionProvider preferencesFromContext:].cold.5
+ -[SBSAElementRemovalTransitionProvider removeFromParentProvider]
+ -[SBSALayoutModeSupportingProvider _firstElementLayoutModeSupportingProvider]
+ -[SBSALayoutModeSupportingProvider _transitionToLayoutModeIfNecessary:customLayoutCustomizingOptions:context:].cold.3
+ -[SBSALayoutModeSupportingProvider _transitionToLayoutModeIfNecessary:customLayoutCustomizingOptions:context:].cold.4
+ -[SBSceneManager sceneDidActivate:]
+ -[SBSceneManager windowSceneDidDisconnect:]
+ -[SBSceneManagerCoordinator sceneDidActivate:]
+ -[SBSceneSettingsUpdater cornerRadiusConfiguration]
+ -[SBSceneSettingsUpdater setCornerRadiusConfiguration:]
+ -[SBScheduledAlarmObserver alert:didBeginPlayingWithEvent:]
+ -[SBSensorActivityDataProvider(ControlCenterUI) mutedMicrophoneSensorActivityData]
+ -[SBSingleSceneController cornerRadiusConfiguration]
+ -[SBSingleSceneController setCornerRadiusConfiguration:]
+ -[SBSoundController _alert:didBeginPlayingWithEvent:]
+ -[SBSoundController alert:didBeginPlayingWithEvent:]
+ -[SBSplitResizeWindowingModifier frameForSplitViewHandleDimmingView:]
+ -[SBSplitResizeWindowingModifier frameForSplitViewHandleNubView:]
+ -[SBSplitViewHandleDimmingView .cxx_destruct]
+ -[SBSplitViewHandleDimmingView initWithFrame:]
+ -[SBSplitViewHandleDimmingView layoutSubviews]
+ -[SBSplitViewHandleNubView .cxx_destruct]
+ -[SBSplitViewHandleNubView dealloc]
+ -[SBSplitViewHandleNubView initWithFrame:systemPointerInteractionManager:]
+ -[SBSplitViewHandleNubView layoutSubviews]
+ -[SBSplitViewHandleNubView nubContainerView]
+ -[SBSplitViewHandleNubView pointerInteractionHitTestInsetsForView:]
+ -[SBSplitViewHandleNubView shouldBeginPointerInteractionRequest:atLocation:forView:]
+ -[SBSplitViewHandleNubView styleForRegion:forView:]
+ -[SBSplitViewResizePanSystemGestureRecognizer reset]
+ -[SBSpotlightPresentableViewController _ensureSearchAffordanceIsInstalledInView:]
+ -[SBSpotlightPresentableViewController searchAffordancePortalView]
+ -[SBSpotlightPresentableViewController setSearchAffordancePortalView:]
+ -[SBSpringBoardApplicationIconDataSource iconTypeIdentifierForImageForIcon:]
+ -[SBSwitcherAppSuggestionBannerView _updateIconViewImageForSuggestion:]
+ -[SBSwitcherAppSuggestionBannerView customConstraints]
+ -[SBSwitcherAppSuggestionBannerView setCustomConstraints:]
+ -[SBSwitcherController _areContinuousExposeStripsUnoccluded]
+ -[SBSwitcherController _isFloatingDockFullyPresented]
+ -[SBSwitcherController _maxScreenSizeWithDockAndStripInset]
+ -[SBSwitcherController _noteAppLayoutMovedToFront:]
+ -[SBSwitcherController _prefersStripHiddenAndDisabled]
+ -[SBSwitcherController _previousDesktopSpaceItems]
+ -[SBSwitcherController _restoreDesktopSpaceAfterClosingFullScreenSpace]
+ -[SBSwitcherController _windowingConfiguration]
+ -[SBSwitcherModifier(SharedModifierUtilities) topMostLayoutElementsByAddingAppLayoutAndAccessories:toTopMostLayoutElements:orderFront:]
+ -[SBSwitcherSplitViewHandleDimmingElement .cxx_destruct]
+ -[SBSwitcherSplitViewHandleDimmingElement appLayout]
+ -[SBSwitcherSplitViewHandleDimmingElement copyWithZone:]
+ -[SBSwitcherSplitViewHandleDimmingElement displayItems]
+ -[SBSwitcherSplitViewHandleDimmingElement hash]
+ -[SBSwitcherSplitViewHandleDimmingElement initWithDisplayItems:]
+ -[SBSwitcherSplitViewHandleDimmingElement initWithDisplayItems:].cold.1
+ -[SBSwitcherSplitViewHandleDimmingElement isAppLayout]
+ -[SBSwitcherSplitViewHandleDimmingElement isEqual:]
+ -[SBSwitcherSplitViewHandleDimmingElement switcherLayoutElementType]
+ -[SBSwitcherSplitViewHandleNubElement .cxx_destruct]
+ -[SBSwitcherSplitViewHandleNubElement appLayout]
+ -[SBSwitcherSplitViewHandleNubElement copyWithZone:]
+ -[SBSwitcherSplitViewHandleNubElement displayItems]
+ -[SBSwitcherSplitViewHandleNubElement hash]
+ -[SBSwitcherSplitViewHandleNubElement initWithDisplayItems:]
+ -[SBSwitcherSplitViewHandleNubElement initWithDisplayItems:].cold.1
+ -[SBSwitcherSplitViewHandleNubElement isAppLayout]
+ -[SBSwitcherSplitViewHandleNubElement isEqual:]
+ -[SBSwitcherSplitViewHandleNubElement switcherLayoutElementType]
+ -[SBSwitcherTransitionRequest minimizingDisplayItem]
+ -[SBSwitcherTransitionRequest setMinimizingDisplayItem:]
+ -[SBSwitcherWindowingConfiguration setSplitViewHandleDimmingWidth:]
+ -[SBSwitcherWindowingConfiguration setSplitViewHandleNubWidth:]
+ -[SBSwitcherWindowingConfiguration splitViewHandleDimmingWidth]
+ -[SBSwitcherWindowingConfiguration splitViewHandleNubWidth]
+ -[SBSwitcherWindowingSettings initialScaleForSplitViewHandles]
+ -[SBSwitcherWindowingSettings maxHomeScreenDimmingAlphaForNonFullscreen]
+ -[SBSwitcherWindowingSettings maxHomeScreenDimmingAlphaResponse]
+ -[SBSwitcherWindowingSettings minHomeScreenDimmingAlphaResponse]
+ -[SBSwitcherWindowingSettings percentageOfTransitionForSplitViewHandleFadeInDelay]
+ -[SBSwitcherWindowingSettings setInitialScaleForSplitViewHandles:]
+ -[SBSwitcherWindowingSettings setMaxHomeScreenDimmingAlphaForNonFullscreen:]
+ -[SBSwitcherWindowingSettings setMaxHomeScreenDimmingAlphaResponse:]
+ -[SBSwitcherWindowingSettings setMinHomeScreenDimmingAlphaResponse:]
+ -[SBSwitcherWindowingSettings setPercentageOfTransitionForSplitViewHandleFadeInDelay:]
+ -[SBSystemApertureController systemApertureViewController:isDisplayingAnyRequiredSecureElements:]
+ -[SBSystemAperturePlatformElementHost _requiredPriorityAssertionWithReason:creatingIfNecessary:]
+ -[SBSystemAperturePlatformElementHost requestRequiredPriorityAssertionWithReason:]
+ -[SBSystemAperturePlatformElementHost requiredPriorityAssertion]
+ -[SBSystemApertureSceneElement _updateRequiredPriorityAssertion]
+ -[SBSystemApertureSceneElement requiredPriorityAssertion]
+ -[SBSystemApertureSceneElement setRequiredPriorityAssertion:]
+ -[SBSystemApertureViewController _doesElementHaveValidRequiredPriorityAssertion:]
+ -[SBSystemApertureViewController systemApertureApertureElementAuthority:isElementPreferringToRemainVisible:]
+ -[SBSystemApertureViewController systemApertureApertureElementAuthority:isElementRequiredPriority:]
+ -[SBSystemShellExternalDisplaySceneManager _isExternalForegroundScene:]
+ -[SBSystemShellExternalDisplaySceneManager _proposeIdleTimerBehaviorForReason:]
+ -[SBSystemShellExternalDisplaySceneManager _resetIdleTimerIfNeededForUpdateToScene:withHandle:]
+ -[SBSystemShellExternalDisplaySceneManager _resetIdleTimerIfNeeded]
+ -[SBSystemShellExternalDisplaySceneManager _sceneHandlesDisablingIdleTimer]
+ -[SBSystemShellExternalDisplaySceneManager coordinatorRequestedIdleTimerBehavior:]
+ -[SBSystemShellExternalDisplaySceneManager existingSceneHandleForPersistenceIdentifier:]
+ -[SBSystemShellExternalDisplaySceneManager existingSceneHandleForScene:]
+ -[SBSystemShellExternalDisplaySceneManager existingSceneHandleForSceneIdentity:]
+ -[SBSystemShellExternalDisplaySceneManager externalForegroundApplicationSceneHandles]
+ -[SBSystemShellExternalDisplaySceneManager hasIdleTimerBehaviors]
+ -[SBSystemShellExternalDisplaySceneManager idleTimerProvider:didProposeBehavior:forReason:]
+ -[SBSystemShellExternalDisplaySceneManager sceneManager:didDestroyScene:]
+ -[SBSystemShellExternalDisplaySceneManager wantsDisableIdleTimer]
+ -[SBSystemShellExternalDisplaySceneManager windowSceneDidDisconnect:]
+ -[SBTransitionSwitcherModifierEvent minimizingDisplayItem]
+ -[SBTransitionSwitcherModifierEvent previousDesktopItems]
+ -[SBTransitionSwitcherModifierEvent setMinimizingDisplayItem:]
+ -[SBTransitionSwitcherModifierEvent setPreviousDesktopItems:]
+ -[SBUIController _updatesHomeScreenForAccessoryWithType:]
+ -[SBWindowingItemViewModel initWithItem:frame:corners:shadow:titleStyle:opacity:wallpaperGradientAttributes:perspectiveAngle:dimmingAlpha:animationAttributes:supportsHomeAffordance:spaceAccessoryViewModel:personalityDebugColorStyle:]
+ -[SBWindowingItemViewModel initWithItem:frame:corners:shadow:titleStyle:opacity:wallpaperGradientAttributes:perspectiveAngle:dimmingAlpha:animationAttributes:supportsHomeAffordance:spaceAccessoryViewModel:personalityDebugColorStyle:].cold.1
+ -[SBWindowingModifierBase topMostItemsByAddingAppLayoutAndAccessories:toTopMostItems:orderFront:]
+ -[SBWorkspaceApplicationSceneTransitionContext minimizingDisplayItem]
+ -[SBWorkspaceApplicationSceneTransitionContext setMinimizingDisplayItem:]
+ -[_SBAppLayoutsArray .cxx_destruct]
+ -[_SBAppLayoutsArray addObject:]
+ -[_SBAppLayoutsArray copyWithZone:]
+ -[_SBAppLayoutsArray count]
+ -[_SBAppLayoutsArray encodeWithCoder:]
+ -[_SBAppLayoutsArray indexOfObject:]
+ -[_SBAppLayoutsArray initWithCoder:]
+ -[_SBAppLayoutsArray initWithObjects:count:]
+ -[_SBAppLayoutsArray init]
+ -[_SBAppLayoutsArray insertObject:atIndex:]
+ -[_SBAppLayoutsArray mutableCopyWithZone:]
+ -[_SBAppLayoutsArray objectAtIndex:]
+ -[_SBAppLayoutsArray removeLastObject]
+ -[_SBAppLayoutsArray removeObjectAtIndex:]
+ -[_SBAppLayoutsArray replaceObjectAtIndex:withObject:]
+ GCC_except_table165
+ GCC_except_table169
+ GCC_except_table173
+ GCC_except_table176
+ GCC_except_table181
+ GCC_except_table185
+ GCC_except_table215
+ GCC_except_table225
+ GCC_except_table247
+ GCC_except_table258
+ GCC_except_table260
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table275
+ GCC_except_table296
+ GCC_except_table310
+ GCC_except_table313
+ GCC_except_table321
+ GCC_except_table325
+ GCC_except_table342
+ GCC_except_table344
+ GCC_except_table363
+ GCC_except_table365
+ GCC_except_table374
+ GCC_except_table376
+ GCC_except_table380
+ GCC_except_table382
+ GCC_except_table386
+ GCC_except_table391
+ GCC_except_table399
+ GCC_except_table434
+ GCC_except_table447
+ GCC_except_table483
+ GCC_except_table486
+ GCC_except_table488
+ GCC_except_table490
+ GCC_except_table491
+ GCC_except_table492
+ GCC_except_table493
+ GCC_except_table496
+ GCC_except_table498
+ GCC_except_table500
+ GCC_except_table515
+ GCC_except_table519
+ GCC_except_table525
+ GCC_except_table527
+ GCC_except_table529
+ GCC_except_table553
+ GCC_except_table598
+ GCC_except_table633
+ GCC_except_table701
+ GCC_except_table725
+ GCC_except_table728
+ GCC_except_table768
+ GCC_except_table807
+ GCC_except_table847
+ GCC_except_table856
+ GCC_except_table898
+ GCC_except_table937
+ OBJC_IVAR_$_SBPBDisplayItemLayoutAttributes._cascaded
+ _CGRegionCreateIntersectionWithRect
+ _CGRegionEnumeratorCreate
+ _CGRegionEnumeratorGetNextRect
+ _CGRegionEnumeratorRelease
+ _OBJC_CLASS_$_BMPublisherOptions
+ _OBJC_CLASS_$_PLKBackdropAwareTrait
+ _OBJC_CLASS_$_SBDisplayItemLayoutAttributesDebugView
+ _OBJC_CLASS_$_SBDisplayItemLayoutAttributesProvider
+ _OBJC_CLASS_$_SBInteractiveScreenshotGestureRoundedCropsView
+ _OBJC_CLASS_$_SBRestoreDesktopSpaceWindowingModifier
+ _OBJC_CLASS_$_SBSAElementRemovalTransitionProvider
+ _OBJC_CLASS_$_SBSplitViewHandleDimmingView
+ _OBJC_CLASS_$_SBSplitViewHandleNubView
+ _OBJC_CLASS_$_SBSwitcherSplitViewHandleDimmingElement
+ _OBJC_CLASS_$_SBSwitcherSplitViewHandleNubElement
+ _OBJC_CLASS_$__SBAppLayoutsArray
+ _OBJC_IVAR_$_SBActivationInfoViewController._eid
+ _OBJC_IVAR_$_SBActivityAmbientViewController._isCreatingFullScreenOverlay
+ _OBJC_IVAR_$_SBAppExposeToAppWindowingModifier._transitionID
+ _OBJC_IVAR_$_SBAppExposeToHomeWindowingModifier._transitionID
+ _OBJC_IVAR_$_SBApplicationInfo._appLibraryOnlyByDefault
+ _OBJC_IVAR_$_SBAssistantController._shouldDismissForWorkspaceTransitions
+ _OBJC_IVAR_$_SBContinuousExposeAppToAppModifier._stripWasInitiallyPresented
+ _OBJC_IVAR_$_SBContinuousExposeArcSwipeSwitcherModifier._hideSplitViewHandles
+ _OBJC_IVAR_$_SBContinuousExposeArcSwipeSwitcherModifier._uniqueTimerReason
+ _OBJC_IVAR_$_SBContinuousExposeHomeGestureSwitcherModifier._canEnterExposeMultitasking
+ _OBJC_IVAR_$_SBContinuousExposeHomeGestureSwitcherModifier._exposeModifier
+ _OBJC_IVAR_$_SBContinuousExposeHomeGestureSwitcherModifier._hideSplitViewHandles
+ _OBJC_IVAR_$_SBContinuousExposeHomeGestureSwitcherModifier._inExposeMultitasking
+ _OBJC_IVAR_$_SBContinuousExposeHomeGestureSwitcherModifier._inExposeMultitaskingChangedProperty
+ _OBJC_IVAR_$_SBContinuousExposeHomeGestureSwitcherModifier._selectedIndex
+ _OBJC_IVAR_$_SBContinuousExposeSwitcherToAppModifier._coplanarModifier
+ _OBJC_IVAR_$_SBCoplanarSwitcherModifier._ignoredAppLayout
+ _OBJC_IVAR_$_SBDisplayItemLayoutAttributes._cascaded
+ _OBJC_IVAR_$_SBDisplayItemLayoutAttributesDebugView._backgroundView
+ _OBJC_IVAR_$_SBDisplayItemLayoutAttributesDebugView._label
+ _OBJC_IVAR_$_SBDisplayItemLayoutAttributesDebugView._layoutAttributes
+ _OBJC_IVAR_$_SBDisplayItemLayoutAttributesProvider._delegate
+ _OBJC_IVAR_$_SBDisplayItemLayoutAttributesProvider._storage
+ _OBJC_IVAR_$_SBDockToStageZoomWindowingModifier._launchingOverDesktopSpaceAppLayout
+ _OBJC_IVAR_$_SBDynamicLightingController._criticalThermalLevelDynamicLightingAssertion
+ _OBJC_IVAR_$_SBDynamicLightingController._thermalController
+ _OBJC_IVAR_$_SBDynamicLightingController._underlyingUpdateQueue
+ _OBJC_IVAR_$_SBExternalDisplayEducationPillViewController._externalDisplayDefaults
+ _OBJC_IVAR_$_SBFileStackOpenIndicatorView._iconImageInfo
+ _OBJC_IVAR_$_SBFlexibleWindowingArcSwipeSwitcherModifier._hideSplitViewHandles
+ _OBJC_IVAR_$_SBFlexibleWindowingArcSwipeSwitcherModifier._pinSpaceCornerRadiiToDisplayCornerRadii
+ _OBJC_IVAR_$_SBFlexibleWindowingArcSwipeSwitcherModifier._systemApertureSuppressionIdentifier
+ _OBJC_IVAR_$_SBFlexibleWindowingArcSwipeSwitcherModifier._uniqueTimerReason
+ _OBJC_IVAR_$_SBFlexibleWindowingAutoLayoutGroup._intersectionHeight
+ _OBJC_IVAR_$_SBFlexibleWindowingAutoLayoutSpace._occupiedAreaPercentage
+ _OBJC_IVAR_$_SBFlexibleWindowingExposeToHomePeekWindowingModifier._direction
+ _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._canEnterExposeMultitasking
+ _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._coplanarLayoutModifier
+ _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._hasTriggeredCardFlyIn
+ _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._hideSplitViewHandles
+ _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._homeGestureXOffsetFactor
+ _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._inExposeMultitasking
+ _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._inExposeMultitaskingChangedProperty
+ _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._multitaskingModifier
+ _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._translationYWhenTriggeredCardFlyIn
+ _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._desktopSpaceAppLayout
+ _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._layoutRestrictionInfoForSelectedItem
+ _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._selectedItemWasInitiallyFullscreen
+ _OBJC_IVAR_$_SBFlexibleWindowingToAppExposeWindowingModifier._transitionID
+ _OBJC_IVAR_$_SBFluidSwitcherAnimationSettings._splitViewHandleFadeInSettings
+ _OBJC_IVAR_$_SBFluidSwitcherAnimationSettings._splitViewHandleFadeOutSettings
+ _OBJC_IVAR_$_SBFluidSwitcherGestureWorkspaceTransaction._completionDeferralReasons
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._homeScreenDimmingAlpha
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._splitViewHandleNubViewsToHitTestRects
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._visibleSplitViewHandleDimmingViews
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._visibleSplitViewHandleDimmingViewsWaitingForFadeIn
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._visibleSplitViewHandleNubViews
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._visibleSplitViewHandleNubViewsWaitingForFadeIn
+ _OBJC_IVAR_$_SBFullScreenToHomeIconZoomSwitcherModifier._isMinimizing
+ _OBJC_IVAR_$_SBFullScreenToPeekAnimationModifier._transitionID
+ _OBJC_IVAR_$_SBHomeGestureToSwitcherSwitcherModifier._fromPeekConfiguration
+ _OBJC_IVAR_$_SBHomePeekToFullScreenTransitionModifier._fromAppLayout
+ _OBJC_IVAR_$_SBHomePeekToFullScreenTransitionModifier._fromHomePeekModifier
+ _OBJC_IVAR_$_SBHomePeekToFullScreenTransitionModifier._slidingOffPeekingAppLayout
+ _OBJC_IVAR_$_SBHomePeekToFullScreenTransitionModifier._toAppLayout
+ _OBJC_IVAR_$_SBHomePeekToFullScreenTransitionModifier._toFullScreen
+ _OBJC_IVAR_$_SBHomePeekToHomeTransitionModifier._transitionID
+ _OBJC_IVAR_$_SBHomePeekWindowingModifier._forcePeekingTrailingEdge
+ _OBJC_IVAR_$_SBHomePeekWindowingModifier._hasUpdatedForcePeekingEdge
+ _OBJC_IVAR_$_SBInteractiveScreenshotGestureRootViewController._queue_contentCornerRadius
+ _OBJC_IVAR_$_SBInteractiveScreenshotGestureRoundedCropsView._borderView
+ _OBJC_IVAR_$_SBInteractiveScreenshotGestureRoundedCropsView._borderViewMask
+ _OBJC_IVAR_$_SBKeyboardFocusLockReason._avoidOverridingAppFocusOnOtherDisplays
+ _OBJC_IVAR_$_SBLockElementViewProvider._requiredPriorityAssertion
+ _OBJC_IVAR_$_SBMainSwitcherControllerCoordinator._defaults
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._dismissingMenuForPointerHover
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._presentingMenuForIndirectInput
+ _OBJC_IVAR_$_SBMenuBarManager._guidedAccessSystemGestureDisableAssertion
+ _OBJC_IVAR_$_SBMenuBarViewController._leftArrowNavigationAction
+ _OBJC_IVAR_$_SBMenuBarViewController._rightArrowNavigationAction
+ _OBJC_IVAR_$_SBPIPController._keyboardFrameInMainScreenFromNotifications
+ _OBJC_IVAR_$_SBPIPControllerCoordinator._preventPIPFromStartingUnderControllerCenterCompoundAssertion
+ _OBJC_IVAR_$_SBPhoneSceneSnapshotRequestStrategy._appearancePublisher
+ _OBJC_IVAR_$_SBPhoneSceneSnapshotRequestStrategy._appearanceQueue
+ _OBJC_IVAR_$_SBPhoneSceneSnapshotRequestStrategy._isObserving
+ _OBJC_IVAR_$_SBPhoneSceneSnapshotRequestStrategy._lastAppearanceTimestamp
+ _OBJC_IVAR_$_SBPuffAwayItemWindowingModifier._transitionID
+ _OBJC_IVAR_$_SBRegionallyRestrictedAlertItem._application
+ _OBJC_IVAR_$_SBRestoreDesktopSpaceWindowingModifier._launchingOverDesktopSpaceAppLayout
+ _OBJC_IVAR_$_SBRestoreDesktopSpaceWindowingModifier._transitionID
+ _OBJC_IVAR_$_SBSAElementRemovalTransitionProvider._didDisappear
+ _OBJC_IVAR_$_SBSAElementRemovalTransitionProvider._elementContentProvider
+ _OBJC_IVAR_$_SBSAElementRemovalTransitionProvider._pendingDismissalTransitionIdentifiers
+ _OBJC_IVAR_$_SBSAElementRemovalTransitionProvider._registeredContainerDismissalInterfacePropertyIdentifiers
+ _OBJC_IVAR_$_SBSALayoutModeSupportingProvider._elementRemovalTransitionProvider
+ _OBJC_IVAR_$_SBSceneManager._modernScenesPendingActivation
+ _OBJC_IVAR_$_SBSceneSettingsUpdater._cornerRadiusConfiguration
+ _OBJC_IVAR_$_SBSingleSceneController._cornerRadiusConfiguration
+ _OBJC_IVAR_$_SBSplitViewHandleDimmingView._dimmingView
+ _OBJC_IVAR_$_SBSplitViewHandleDimmingView._image
+ _OBJC_IVAR_$_SBSplitViewHandleNubView._backdropLayer
+ _OBJC_IVAR_$_SBSplitViewHandleNubView._nubContainerView
+ _OBJC_IVAR_$_SBSplitViewHandleNubView._systemPointerInteractionManager
+ _OBJC_IVAR_$_SBSpotlightPresentableViewController._searchAffordancePortalView
+ _OBJC_IVAR_$_SBSwitcherAppSuggestionBannerView._customConstraints
+ _OBJC_IVAR_$_SBSwitcherAppSuggestionBannerView._iconContainerView
+ _OBJC_IVAR_$_SBSwitcherController._previousDesktopSpaceItems
+ _OBJC_IVAR_$_SBSwitcherController._reentrantGuard_inNoteAppLayoutMovedToFront
+ _OBJC_IVAR_$_SBSwitcherController._restoreDesktopSpaceAfterClosingFullScreenSpace
+ _OBJC_IVAR_$_SBSwitcherSplitViewHandleDimmingElement._displayItems
+ _OBJC_IVAR_$_SBSwitcherSplitViewHandleDimmingElement._hash
+ _OBJC_IVAR_$_SBSwitcherSplitViewHandleNubElement._displayItems
+ _OBJC_IVAR_$_SBSwitcherSplitViewHandleNubElement._hash
+ _OBJC_IVAR_$_SBSwitcherTransitionRequest._minimizingDisplayItem
+ _OBJC_IVAR_$_SBSwitcherWindowingConfiguration._splitViewHandleDimmingWidth
+ _OBJC_IVAR_$_SBSwitcherWindowingConfiguration._splitViewHandleNubWidth
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._initialScaleForSplitViewHandles
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._maxHomeScreenDimmingAlphaForNonFullscreen
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._maxHomeScreenDimmingAlphaResponse
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._minHomeScreenDimmingAlphaResponse
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._percentageOfTransitionForSplitViewHandleFadeInDelay
+ _OBJC_IVAR_$_SBSystemApertureController._isDisplayingAnyRequiredSecureContent
+ _OBJC_IVAR_$_SBSystemAperturePlatformElementHost._reasonsToRequiredPriorityAssertions
+ _OBJC_IVAR_$_SBSystemAperturePlatformElementHost._requiredPriorityAssertion
+ _OBJC_IVAR_$_SBSystemApertureSceneElement._requiredPriorityAssertion
+ _OBJC_IVAR_$_SBSystemApertureViewController._secureDisplayRequired
+ _OBJC_IVAR_$_SBSystemShellExternalDisplaySceneManager._stateCaptureInvalidatable
+ _OBJC_IVAR_$_SBTransientOverlayScenePresenter._preventVideoCallPIPFromAppearingBelowControlCenterAssertion
+ _OBJC_IVAR_$_SBTransitionSwitcherModifierEvent._minimizingDisplayItem
+ _OBJC_IVAR_$_SBTransitionSwitcherModifierEvent._previousDesktopItems
+ _OBJC_IVAR_$_SBWorkspaceApplicationSceneTransitionContext._minimizingDisplayItem
+ _OBJC_IVAR_$__SBAppLayoutsArray._backing
+ _OBJC_IVAR_$__SBFullScreenAppFloorSwitcherModifier._layoutGrid
+ _OBJC_METACLASS_$_NSMutableArray
+ _OBJC_METACLASS_$_SBDisplayItemLayoutAttributesDebugView
+ _OBJC_METACLASS_$_SBDisplayItemLayoutAttributesProvider
+ _OBJC_METACLASS_$_SBInteractiveScreenshotGestureRoundedCropsView
+ _OBJC_METACLASS_$_SBRestoreDesktopSpaceWindowingModifier
+ _OBJC_METACLASS_$_SBSAElementRemovalTransitionProvider
+ _OBJC_METACLASS_$_SBSplitViewHandleDimmingView
+ _OBJC_METACLASS_$_SBSplitViewHandleNubView
+ _OBJC_METACLASS_$_SBSwitcherSplitViewHandleDimmingElement
+ _OBJC_METACLASS_$_SBSwitcherSplitViewHandleNubElement
+ _OBJC_METACLASS_$__SBAppLayoutsArray
+ _SBIdleTimerUpdateReasonSceneManagerPrefix
+ _SBLogDashBoardTelemetrySignposts
+ _UIContentSizeCategoryAccessibilityLarge
+ _UIContentSizeCategoryExtraLarge
+ _UIContentSizeCategoryLarge
+ __OBJC_$_CLASS_METHODS_SBSplitViewHandleNubView
+ __OBJC_$_INSTANCE_METHODS_SBDisplayItemLayoutAttributesDebugView
+ __OBJC_$_INSTANCE_METHODS_SBDisplayItemLayoutAttributesProvider
+ __OBJC_$_INSTANCE_METHODS_SBInteractiveScreenshotGestureRoundedCropsView
+ __OBJC_$_INSTANCE_METHODS_SBRestoreDesktopSpaceWindowingModifier
+ __OBJC_$_INSTANCE_METHODS_SBSAElementRemovalTransitionProvider
+ __OBJC_$_INSTANCE_METHODS_SBSplitViewHandleDimmingView
+ __OBJC_$_INSTANCE_METHODS_SBSplitViewHandleNubView
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherSplitViewHandleDimmingElement
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherSplitViewHandleNubElement
+ __OBJC_$_INSTANCE_METHODS__SBAppLayoutsArray
+ __OBJC_$_INSTANCE_VARIABLES_SBDisplayItemLayoutAttributesDebugView
+ __OBJC_$_INSTANCE_VARIABLES_SBDisplayItemLayoutAttributesProvider
+ __OBJC_$_INSTANCE_VARIABLES_SBInteractiveScreenshotGestureRoundedCropsView
+ __OBJC_$_INSTANCE_VARIABLES_SBPhoneSceneSnapshotRequestStrategy
+ __OBJC_$_INSTANCE_VARIABLES_SBRegionallyRestrictedAlertItem
+ __OBJC_$_INSTANCE_VARIABLES_SBRestoreDesktopSpaceWindowingModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBSAElementRemovalTransitionProvider
+ __OBJC_$_INSTANCE_VARIABLES_SBSplitViewHandleDimmingView
+ __OBJC_$_INSTANCE_VARIABLES_SBSplitViewHandleNubView
+ __OBJC_$_INSTANCE_VARIABLES_SBSwitcherSplitViewHandleDimmingElement
+ __OBJC_$_INSTANCE_VARIABLES_SBSwitcherSplitViewHandleNubElement
+ __OBJC_$_INSTANCE_VARIABLES__SBAppLayoutsArray
+ __OBJC_$_PROP_LIST_SBDisplayItemLayoutAttributes
+ __OBJC_$_PROP_LIST_SBDisplayItemLayoutAttributesDebugView
+ __OBJC_$_PROP_LIST_SBDisplayItemLayoutAttributesProvider
+ __OBJC_$_PROP_LIST_SBDockToStageZoomWindowingModifier
+ __OBJC_$_PROP_LIST_SBFileStackOpenIndicatorView
+ __OBJC_$_PROP_LIST_SBRestoreDesktopSpaceWindowingModifier
+ __OBJC_$_PROP_LIST_SBSoundController
+ __OBJC_$_PROP_LIST_SBSplitViewHandleNubView
+ __OBJC_$_PROP_LIST_SBSwitcherSplitViewHandleDimmingElement
+ __OBJC_$_PROP_LIST_SBSwitcherSplitViewHandleNubElement
+ __OBJC_$_PROP_LIST_SBWindowingItemViewModel.131
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CCUISensorActivityDataProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TLAlertPlaybackObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBDisplayItemLayoutAttributesProviderDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBDisplayItemLayoutAttributesProviderDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TLAlertPlaybackObserver
+ __OBJC_$_PROTOCOL_REFS_SBDisplayItemLayoutAttributesProviderDelegate
+ __OBJC_$_PROTOCOL_REFS_TLAlertPlaybackObserver
+ __OBJC_CLASS_PROTOCOLS_$_SBDisplayItemLayoutAttributesProvider
+ __OBJC_CLASS_PROTOCOLS_$_SBSoundController
+ __OBJC_CLASS_PROTOCOLS_$_SBSplitViewHandleNubView
+ __OBJC_CLASS_PROTOCOLS_$_SBSwitcherSplitViewHandleDimmingElement
+ __OBJC_CLASS_PROTOCOLS_$_SBSwitcherSplitViewHandleNubElement
+ __OBJC_CLASS_RO_$_SBDisplayItemLayoutAttributesDebugView
+ __OBJC_CLASS_RO_$_SBDisplayItemLayoutAttributesProvider
+ __OBJC_CLASS_RO_$_SBInteractiveScreenshotGestureRoundedCropsView
+ __OBJC_CLASS_RO_$_SBRestoreDesktopSpaceWindowingModifier
+ __OBJC_CLASS_RO_$_SBSAElementRemovalTransitionProvider
+ __OBJC_CLASS_RO_$_SBSplitViewHandleDimmingView
+ __OBJC_CLASS_RO_$_SBSplitViewHandleNubView
+ __OBJC_CLASS_RO_$_SBSwitcherSplitViewHandleDimmingElement
+ __OBJC_CLASS_RO_$_SBSwitcherSplitViewHandleNubElement
+ __OBJC_CLASS_RO_$__SBAppLayoutsArray
+ __OBJC_LABEL_PROTOCOL_$_SBDisplayItemLayoutAttributesProviderDelegate
+ __OBJC_LABEL_PROTOCOL_$_TLAlertPlaybackObserver
+ __OBJC_METACLASS_RO_$_SBDisplayItemLayoutAttributesDebugView
+ __OBJC_METACLASS_RO_$_SBDisplayItemLayoutAttributesProvider
+ __OBJC_METACLASS_RO_$_SBInteractiveScreenshotGestureRoundedCropsView
+ __OBJC_METACLASS_RO_$_SBRestoreDesktopSpaceWindowingModifier
+ __OBJC_METACLASS_RO_$_SBSAElementRemovalTransitionProvider
+ __OBJC_METACLASS_RO_$_SBSplitViewHandleDimmingView
+ __OBJC_METACLASS_RO_$_SBSplitViewHandleNubView
+ __OBJC_METACLASS_RO_$_SBSwitcherSplitViewHandleDimmingElement
+ __OBJC_METACLASS_RO_$_SBSwitcherSplitViewHandleNubElement
+ __OBJC_METACLASS_RO_$__SBAppLayoutsArray
+ __OBJC_PROTOCOL_$_SBDisplayItemLayoutAttributesProviderDelegate
+ __OBJC_PROTOCOL_$_TLAlertPlaybackObserver
+ __UISceneMainMenuKeyboardShortcutActionForNavigatingMenusWithHorizontalArrowKeyInput
+ ___101-[SBHomeScreenContinuousExposeSwitcherModifier responseForProposedChildResponse:childModifier:event:]_block_invoke_3
+ ___101-[SBHomeScreenContinuousExposeSwitcherModifier responseForProposedChildResponse:childModifier:event:]_block_invoke_4
+ ___102-[SBDisplayItemLayoutAttributesProvider lastInteractedDisplayItemInAppLayout:orientation:passingTest:]_block_invoke
+ ___103-[SBContinuousExposeHomeGestureSwitcherModifier _updateGestureTranslationVelocityAndProgressWithEvent:]_block_invoke
+ ___104-[SBFlexibleWindowingHomeGestureSwitcherModifier _updateGestureTranslationVelocityAndProgressWithEvent:]_block_invoke
+ ___108-[SBContinuousExposeHomeGestureSwitcherModifier _beginAnimatingExposeMultitaskingPropertyWithMode:settings:]_block_invoke
+ ___108-[SBContinuousExposeHomeGestureSwitcherModifier _beginAnimatingExposeMultitaskingPropertyWithMode:settings:]_block_invoke_2
+ ___108-[SBHomeScreenController(AppearanceControlling) setHomeScreenDimmingAlpha:settings:behaviorMode:completion:]_block_invoke
+ ___108-[SBHomeScreenController(AppearanceControlling) setHomeScreenDimmingAlpha:settings:behaviorMode:completion:]_block_invoke_2
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.303
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.304
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.305
+ ___109-[SBFlexibleWindowingHomeGestureSwitcherModifier _beginAnimatingExposeMultitaskingPropertyWithMode:settings:]_block_invoke
+ ___109-[SBFlexibleWindowingHomeGestureSwitcherModifier _beginAnimatingExposeMultitaskingPropertyWithMode:settings:]_block_invoke_2
+ ___112-[SBMainSwitcherControllerCoordinator layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:]_block_invoke_3
+ ___112-[SBMainSwitcherControllerCoordinator layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:]_block_invoke_4
+ ___113-[SBFluidSwitcherViewController initWithPersonality:liveContentOverlayCoordinator:dataSource:delegate:debugName:]_block_invoke.198
+ ___113-[SBSystemApertureElementAuthority elementsOrderedByPromotionFromTemporallyOrderedElements:withPreviousOrdering:]_block_invoke.73
+ ___115-[SBContinuousExposeHomeGestureRootSwitcherModifier preferredAppLayoutToReuseAccessoryForAppLayout:fromAppLayouts:]_block_invoke
+ ___117-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]_block_invoke
+ ___117-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]_block_invoke_2
+ ___119-[SBMainSwitcherControllerCoordinator _windowManagementContextIsSingleAppModeForSwitcherCorrespondingToDisplayOrdinal:]_block_invoke
+ ___120-[SBSystemShellExternalDisplaySceneManager initWithReference:sceneIdentityProvider:presentationBinder:snapshotBehavior:]_block_invoke
+ ___123-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:fullScreenRectsIfAny:]_block_invoke
+ ___123-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:fullScreenRectsIfAny:]_block_invoke_2
+ ___123-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:fullScreenRectsIfAny:]_block_invoke_3
+ ___123-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:fullScreenRectsIfAny:]_block_invoke_4
+ ___123-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:fullScreenRectsIfAny:]_block_invoke_5
+ ___123-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:fullScreenRectsIfAny:]_block_invoke_6
+ ___123-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:fullScreenRectsIfAny:]_block_invoke_7
+ ___127-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]_block_invoke
+ ___127-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]_block_invoke_2
+ ___127-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]_block_invoke_3
+ ___127-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]_block_invoke_4
+ ___133-[SBContinuousExposeHomeGestureSwitcherModifier _getActivePositionAndScaleForLayoutRole:inAppLayout:withBounds:outPosition:outScale:]_block_invoke
+ ___135-[SBSwitcherModifier(SharedModifierUtilities) topMostLayoutElementsByAddingAppLayoutAndAccessories:toTopMostLayoutElements:orderFront:]_block_invoke
+ ___135-[SBSwitcherModifier(SharedModifierUtilities) topMostLayoutElementsByAddingAppLayoutAndAccessories:toTopMostLayoutElements:orderFront:]_block_invoke_2
+ ___135-[SBSwitcherModifier(SharedModifierUtilities) topMostLayoutElementsByAddingAppLayoutAndAccessories:toTopMostLayoutElements:orderFront:]_block_invoke_3
+ ___135-[SBSwitcherModifier(SharedModifierUtilities) topMostLayoutElementsByAddingAppLayoutAndAccessories:toTopMostLayoutElements:orderFront:]_block_invoke_4
+ ___29-[SBWindowingModifier update]_block_invoke_3
+ ___36-[_SBAppLayoutsArray indexOfObject:]_block_invoke
+ ___43-[SBMainWorkspace _activeIdleTimerProvider]_block_invoke_2
+ ___44-[SBMainSwitcherControllerCoordinator _init]_block_invoke
+ ___44-[SBMainSwitcherControllerCoordinator _init]_block_invoke_2
+ ___46-[SBMenuBarViewController openApplicationMenu]_block_invoke
+ ___49-[SBCombinationHardwareButton _backlightChanged:]_block_invoke.cold.1
+ ___49-[SBDisplayItemLayoutAttributes debugDescription]_block_invoke
+ ___50-[SBMenuBarManager _dismissMenuBarWithCompletion:]_block_invoke
+ ___50-[SBMenuBarManager _dismissMenuBarWithCompletion:]_block_invoke_2
+ ___50-[SBMenuBarManager _dismissMenuBarWithCompletion:]_block_invoke_3
+ ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.83
+ ___51-[SBSwitcherController _noteAppLayoutMovedToFront:]_block_invoke
+ ___52-[SBLockScreenManager _setPasscodeVisible:animated:]_block_invoke.392
+ ___52-[SBMainDisplaySceneManager _resetIdleTimerIfNeeded]_block_invoke_2
+ ___53-[SBCoplanarSwitcherModifier _indexOfActiveAppLayout]_block_invoke
+ ___53-[SBSoundController _alert:didBeginPlayingWithEvent:]_block_invoke
+ ___53-[SBThermalController startListeningForThermalEvents]_block_invoke.41
+ ___53-[SBThermalController startListeningForThermalEvents]_block_invoke.43
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.383
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.382
+ ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.750
+ ___55-[SBSceneSettingsUpdater setCornerRadiusConfiguration:]_block_invoke
+ ___56-[SBAppExposeWindowingModifier desktopSpaceDisplayItems]_block_invoke
+ ___56-[SBIconModel osMigrationHomeScreenLayoutForRootFolder:]_block_invoke
+ ___56-[SBIconModel osMigrationHomeScreenLayoutForRootFolder:]_block_invoke_2
+ ___56-[SBIconModel osMigrationHomeScreenLayoutForRootFolder:]_block_invoke_3
+ ___56-[SBMenuBarManager _handleContentSizeCategoryDidChange:]_block_invoke
+ ___57-[SBContinuousExposeSwitcherToAppModifier frameForIndex:]_block_invoke_2
+ ___57-[SBDynamicLightingController thermalBlockStatusChanged:]_block_invoke
+ ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.505
+ ___59-[SBDockToStageZoomWindowingModifier topMostLayoutElements]_block_invoke
+ ___59-[SBDynamicLightingController initWithBacklightController:]_block_invoke_2
+ ___59-[SBFloatingDockRemoteContentManager iconView:performDrop:]_block_invoke.70
+ ___59-[SBMainSwitcherControllerCoordinator _buildAppLayoutCache]_block_invoke_10
+ ___59-[SBMainSwitcherControllerCoordinator _buildAppLayoutCache]_block_invoke_11
+ ___59-[SBMainSwitcherControllerCoordinator _buildAppLayoutCache]_block_invoke_8
+ ___59-[SBMainSwitcherControllerCoordinator _buildAppLayoutCache]_block_invoke_9
+ ___59-[SBRoutingSwitcherModifier fadeInDelayForSplitViewHandles]_block_invoke
+ ___59-[SBRoutingSwitcherModifier visibleSplitViewHandleNubViews]_block_invoke
+ ___59-[SBThermalController _updateThermalJetsamCPUSamplingState]_block_invoke.82
+ ___59-[SBThermalController _updateThermalJetsamCPUSamplingState]_block_invoke.87
+ ___59-[SBThermalController _updateThermalJetsamCPUSamplingState]_block_invoke.89
+ ___60-[SBMainWorkspace _preflightTransitionRequest:forExecution:]_block_invoke.380
+ ___60-[SBRoutingSwitcherModifier frameForSplitViewHandleNubView:]_block_invoke
+ ___63-[SBInCallPresentationManager isSceneHandleKillableInSwitcher:]_block_invoke
+ ___63-[SBRoutingSwitcherModifier visibleSplitViewHandleDimmingViews]_block_invoke
+ ___63-[SBSAElementRemovalTransitionProvider preferencesFromContext:]_block_invoke
+ ___63-[SBSAElementRemovalTransitionProvider preferencesFromContext:]_block_invoke.26
+ ___63-[SBSAElementRemovalTransitionProvider preferencesFromContext:]_block_invoke.26.cold.1
+ ___63-[SBSAElementRemovalTransitionProvider preferencesFromContext:]_block_invoke_2
+ ___63-[SBSAElementRemovalTransitionProvider preferencesFromContext:]_block_invoke_2.cold.1
+ ___63-[SBSAElementRemovalTransitionProvider preferencesFromContext:]_block_invoke_3
+ ___63-[SBSAElementRemovalTransitionProvider preferencesFromContext:]_block_invoke_3.cold.1
+ ___64-[SBCombinationHardwareButton _setScreenshotDisabled:forReason:]_block_invoke.cold.1
+ ___64-[SBFlexibleWindowingHomeGestureSwitcherModifier frameForIndex:]_block_invoke
+ ___64-[SBHomeGestureToSwitcherSwitcherModifier topMostLayoutElements]_block_invoke
+ ___64-[SBHomeGestureToSwitcherSwitcherModifier topMostLayoutElements]_block_invoke_2
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke_11
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke_12
+ ___64-[SBRoutingSwitcherModifier frameForSplitViewHandleDimmingView:]_block_invoke
+ ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke.209
+ ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke_2.212
+ ___66-[SBActivationInfoViewController tableView:cellForRowAtIndexPath:]_block_invoke
+ ___67-[SBSystemShellExternalDisplaySceneManager _resetIdleTimerIfNeeded]_block_invoke
+ ___68-[SBContinuousExposeAppToAppModifier fadeInDelayForSplitViewHandles]_block_invoke
+ ___68-[SBMenuBarManager toggleMenuBarVisibilityForSystemKeyboardShortcut]_block_invoke
+ ___68-[SBPhoneSceneSnapshotRequestStrategy _subscribeToAppearanceChanges]_block_invoke
+ ___68-[SBPhoneSceneSnapshotRequestStrategy _subscribeToAppearanceChanges]_block_invoke.69
+ ___68-[SBPhoneSceneSnapshotRequestStrategy _subscribeToAppearanceChanges]_block_invoke.cold.1
+ ___69-[SBFullScreenContinuousExposeSwitcherModifier topMostLayoutElements]_block_invoke
+ ___69-[SBFullScreenContinuousExposeSwitcherModifier topMostLayoutElements]_block_invoke_2
+ ___70-[SBDockToStageZoomWindowingModifier adjustedAppLayoutsForAppLayouts:]_block_invoke_2
+ ___70-[SBDockToStageZoomWindowingModifier adjustedAppLayoutsForAppLayouts:]_block_invoke_3
+ ___70-[SBFlexibleWindowingHomeGestureSwitcherModifier cornerRadiiForIndex:]_block_invoke
+ ___70-[SBFlexibleWindowingWindowDragSwitcherModifier topMostLayoutElements]_block_invoke
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke_2
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke_3
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke_4
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke_5
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke_6
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke_7
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke_8
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke_9
+ ___70-[SBPhoneSceneSnapshotRequestStrategy _updateLastAppearanceTimestamp:]_block_invoke
+ ___71-[SBCoverSheetIconFlyInAnimator _updateLabelAlphaForPresentationValue:]_block_invoke.45
+ ___71-[SBFlexibleWindowingExposeToHomePeekWindowingModifier cornersForItem:]_block_invoke
+ ___71-[SBFloatingDockRemoteContentManager handleFloatingDockFrameDidChange:]_block_invoke
+ ___71-[SBPhoneSceneSnapshotRequestStrategy _startObservingAppearanceChanges]_block_invoke
+ ___72-[SBCoverSheetIconFlyInAnimator _updateSpreadMultiplierForPresentation:]_block_invoke.39
+ ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.389
+ ___73-[SBFlexibleWindowingArcSwipeSwitcherModifier appLayoutsToCacheSnapshots]_block_invoke
+ ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1068
+ ___74-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleDimmingViews]_block_invoke
+ ___74-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleDimmingViews]_block_invoke_2
+ ___74-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleDimmingViews]_block_invoke_3
+ ___74-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleDimmingViews]_block_invoke_4
+ ___74-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleDimmingViews]_block_invoke_5
+ ___74-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleDimmingViews]_block_invoke_6
+ ___74-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleDimmingViews]_block_invoke_7
+ ___74-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleDimmingViews]_block_invoke_8
+ ___74-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleDimmingViews]_block_invoke_9
+ ___75-[SBContinuousExposeSwitcherToAppModifier adjustedAppLayoutsForAppLayouts:]_block_invoke
+ ___75-[SBHomePeekToFullScreenTransitionModifier scaleForLayoutRole:inAppLayout:]_block_invoke
+ ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.411
+ ___75-[SBSystemShellExternalDisplaySceneManager _sceneHandlesDisablingIdleTimer]_block_invoke
+ ___75-[SBSystemShellExternalDisplaySceneManager _sceneHandlesDisablingIdleTimer]_block_invoke.cold.1
+ ___76-[SBContinuousExposeToHomeSwitcherModifier adjustedAppLayoutsForAppLayouts:]_block_invoke
+ ___77-[SBDisplayItemLayoutAttributesProvider layoutAttributesEntriesForAppLayout:]_block_invoke
+ ___77-[SBDisplayItemLayoutAttributesProvider layoutAttributesEntriesForAppLayout:]_block_invoke_2
+ ___78-[SBFullScreenContinuousExposeSwitcherModifier visibleSplitViewHandleNubViews]_block_invoke
+ ___79-[SBFlexibleWindowingArcSwipeSwitcherModifier adjustedAppLayoutsForAppLayouts:]_block_invoke
+ ___79-[SBFullScreenContinuousExposeSwitcherModifier frameForSplitViewHandleNubView:]_block_invoke
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke.121
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_2.123
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_27
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_28
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_29
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_30
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_31
+ ___79-[SBMainWorkspace _removeApplicationEntities:withDestructionIntent:completion:]_block_invoke.472
+ ___79-[SBPhoneSceneSnapshotRequestStrategy _loadLastAppearanceChangeWithCompletion:]_block_invoke
+ ___79-[SBPhoneSceneSnapshotRequestStrategy _loadLastAppearanceChangeWithCompletion:]_block_invoke.67
+ ___79-[SBPhoneSceneSnapshotRequestStrategy _loadLastAppearanceChangeWithCompletion:]_block_invoke.cold.1
+ ___80-[SBFlexibleWindowingItemResizeGestureSwitcherModifier didMoveToParentModifier:]_block_invoke
+ ___80-[SBSystemShellExternalDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke_4
+ ___80-[SBSystemUISceneController _createOrRetrievePresenterForDisplayIdentity:level:]_block_invoke.113
+ ___81-[SBContinuousExposeHomeGestureSwitcherModifier contentOffsetForIndex:alignment:]_block_invoke
+ ___81-[SBContinuousExposeHomeGestureSwitcherModifier contentOffsetForIndex:alignment:]_block_invoke_2
+ ___81-[SBFlexibleWindowingArcSwipeSwitcherModifier appLayoutsToCacheFullsizeSnapshots]_block_invoke
+ ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.441
+ ___82-[SBFlexibleWindowingHomeGestureSwitcherModifier adjustedAppLayoutsForAppLayouts:]_block_invoke
+ ___82-[SBFlexibleWindowingHomeGestureSwitcherModifier contentOffsetForIndex:alignment:]_block_invoke
+ ___82-[SBFluidSwitcherViewController _scrollToAppLayout:animated:alignment:completion:]_block_invoke
+ ___82-[SBFullScreenContinuousExposeSwitcherModifier visibleSplitViewHandleDimmingViews]_block_invoke
+ ___82-[SBSensorActivityDataProvider(ControlCenterUI) mutedMicrophoneSensorActivityData]_block_invoke
+ ___82-[SBSystemAperturePlatformElementHost requestRequiredPriorityAssertionWithReason:]_block_invoke
+ ___82-[SBSystemShellExternalDisplaySceneManager coordinatorRequestedIdleTimerBehavior:]_block_invoke
+ ___83-[SBContinuousExposeRootSwitcherModifier transitionModifierForMainTransitionEvent:]_block_invoke_3
+ ___83-[SBContinuousExposeRootSwitcherModifier transitionModifierForMainTransitionEvent:]_block_invoke_4
+ ___83-[SBContinuousExposeRootSwitcherModifier transitionModifierForMainTransitionEvent:]_block_invoke_5
+ ___83-[SBFullScreenContinuousExposeSwitcherModifier frameForSplitViewHandleDimmingView:]_block_invoke
+ ___86-[SBFlexibleWindowingItemResizeGestureSwitcherModifier visibleSplitViewHandleNubViews]_block_invoke
+ ___86-[SBHomePeekToFullScreenTransitionModifier frameForLayoutRole:inAppLayout:withBounds:]_block_invoke
+ ___86-[SBHomePeekToFullScreenTransitionModifier perspectiveAngleForLayoutRole:inAppLayout:]_block_invoke
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.361
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.362
+ ___87-[SBContinuousExposeWindowDragContainerSwitcherModifier visibleSplitViewHandleNubViews]_block_invoke
+ ___87-[SBContinuousExposeWindowDragContainerSwitcherModifier visibleSplitViewHandleNubViews]_block_invoke_2
+ ___88-[SBHomePeekToFullScreenTransitionModifier shouldUseAnchorPointToPinLayoutRolesToSpace:]_block_invoke
+ ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.79
+ ___90-[SBFlexibleWindowingItemResizeGestureSwitcherModifier visibleSplitViewHandleDimmingViews]_block_invoke
+ ___91-[SBContinuousExposeWindowDragContainerSwitcherModifier visibleSplitViewHandleDimmingViews]_block_invoke
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.644
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.666
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.685
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.693
+ ___96-[SBSystemAperturePlatformElementHost _requiredPriorityAssertionWithReason:creatingIfNecessary:]_block_invoke
+ ___97-[SBWindowingModifierBase topMostItemsByAddingAppLayoutAndAccessories:toTopMostItems:orderFront:]_block_invoke
+ ___97-[SBWindowingModifierBase topMostItemsByAddingAppLayoutAndAccessories:toTopMostItems:orderFront:]_block_invoke_2
+ ___97-[SBWindowingModifierBase topMostItemsByAddingAppLayoutAndAccessories:toTopMostItems:orderFront:]_block_invoke_3
+ ___97-[SBWindowingModifierBase topMostItemsByAddingAppLayoutAndAccessories:toTopMostItems:orderFront:]_block_invoke_4
+ ___98-[SBPIPControllerCoordinator acquireAssertionToPreventVideoCallPIPFromStartingUnderControlCenter:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48r_e78_v32?0"SBSwitcherSplitViewHandleNubElement"8"SBSplitViewHandleNubView"16^B24lr48l8s32l8s40l8
+ ___block_descriptor_104_e8_32s40s_e49_v24?0"SBSwitcherSplitViewHandleNubElement"8^B16ls32l8s40l8
+ ___block_descriptor_104_e8_32s_e30_v32?0"SBDisplayItem"8Q16^B24ls32l8
+ ___block_descriptor_32_e44_16?0"SBFlexibleWindowingAutoLayoutGroup"8l
+ ___block_descriptor_32_e44_B16?0"<SBSwitcherLayoutElementProviding>"8l
+ ___block_descriptor_32_e45_16?0"SBSwitcherSplitViewHandleNubElement"8l
+ ___block_descriptor_40_e8_32r_e23_B16?0"SBDisplayItem"8lr32l8
+ ___block_descriptor_40_e8_32s_e21_B24?0"NSString"816ls32l8
+ ___block_descriptor_40_e8_32s_e45_B16?0"SBSwitcherSplitViewHandleNubElement"8ls32l8
+ ___block_descriptor_40_e8_32s_e48_B24?0"<SBSwitcherLayoutElementProviding>"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e49_B16?0"SBSwitcherSplitViewHandleDimmingElement"8ls32l8
+ ___block_descriptor_40_e8_32s_e49_v24?0"SBSwitcherSplitViewHandleNubElement"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e53_v24?0"SBSwitcherSplitViewHandleDimmingElement"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e74_B24?0"SBSwitcherSplitViewHandleNubElement"8"SBSplitViewHandleNubView"16ls32l8
+ ___block_descriptor_40_e8_32s_e82_B24?0"SBSwitcherSplitViewHandleDimmingElement"8"SBSplitViewHandleDimmingView"16ls32l8
+ ___block_descriptor_40_e8_32w_e18_v16?0"UIButton"8lw32l8
+ ___block_descriptor_40_e8_32w_e22_B16?0"BMStoreEvent"8lw32l8
+ ___block_descriptor_40_e8_32w_e23_v16?0"BPSCompletion"8lw32l8
+ ___block_descriptor_48_e8_32bs40w_e21_v16?0"_UIMainMenu"8lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e34_v16?0"_UIMainMenuStateResponse"8lw40l8s32l8
+ ___block_descriptor_48_e8_32bs40w_e36_v16?0"_UIMainMenuSessionResponse"8lw40l8s32l8
+ ___block_descriptor_48_e8_32r40w_e22_B16?0"BMStoreEvent"8lw40l8r32l8
+ ___block_descriptor_48_e8_32s40bs_e72_v20?0B8"SBDashBoardHostableEntityHostingFluidSwitcherViewController"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e49_v24?0"SBSwitcherSplitViewHandleNubElement"8^B16ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40r48w_e23_v16?0"BPSCompletion"8lw48l8s32l8r40l8
+ ___block_descriptor_56_e8_32s40s48s_e47_v32?0"SBDeviceApplicationSceneEntity"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e49_v24?0"SBSwitcherSplitViewHandleNubElement"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e78_v32?0"SBSwitcherSplitViewHandleNubElement"8"SBSplitViewHandleNubView"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e86_v32?0"SBSwitcherSplitViewHandleDimmingElement"8"SBSplitViewHandleDimmingView"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32r40r48r56w_e36_v16?0"<BSCompoundAssertionState>"8lw56l8r32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56w_e40_v24?0"<SAInvalidatable>"8"NSString"16lw56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48w_e78_v32?0"SBSwitcherSplitViewHandleNubElement"8"SBSplitViewHandleNubView"16^B24ls32l8s40l8w48l8
+ ___block_descriptor_64_e8_32s40s48w_e86_v32?0"SBSwitcherSplitViewHandleDimmingElement"8"SBSplitViewHandleDimmingView"16^B24ls32l8s40l8w48l8
+ ___block_descriptor_72_e8_32s40r48r56r_e5_v8?0lr40l8s32l8r48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s_e75_"SBChainableModifierEventResponse"16?0"SBSwitcherModifierEventResponse"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s_e23_v32?0"SBIcon"8Q16^B24ls32l8
+ ___block_descriptor_96_e8_32s40r_e61_v32?0"SBDisplayItem"8"SBDisplayItemLayoutAttributes"16^B24ls32l8r40l8
+ ___block_literal_global.1081
+ ___block_literal_global.117
+ ___block_literal_global.119
+ ___block_literal_global.1198
+ ___block_literal_global.1246
+ ___block_literal_global.201
+ ___block_literal_global.326
+ ___block_literal_global.336
+ ___block_literal_global.338
+ ___block_literal_global.354
+ ___block_literal_global.357
+ ___block_literal_global.380
+ ___block_literal_global.475
+ ___block_literal_global.482
+ ___block_literal_global.486
+ ___block_literal_global.491
+ ___block_literal_global.492
+ ___block_literal_global.494
+ ___block_literal_global.495
+ ___block_literal_global.577
+ ___block_literal_global.583
+ ___block_literal_global.588
+ ___block_literal_global.590
+ ___block_literal_global.592
+ ___block_literal_global.594
+ ___block_literal_global.596
+ ___block_literal_global.598
+ ___block_literal_global.600
+ ___block_literal_global.613
+ ___block_literal_global.654
+ ___block_literal_global.656
+ ___block_literal_global.661
+ ___block_literal_global.693
+ ___block_literal_global.697
+ ___block_literal_global.723
+ ___block_literal_global.804
+ ___block_literal_global.816
+ ___block_literal_global.818
+ ___block_literal_global.98
+ __appIsEligibleForDomainWithIdentifierAndPersona
+ _kCAFilterColorBrightness
+ _objc_msgSend$Appearance
+ _objc_msgSend$_adjustMobileEquipmentLayout:
+ _objc_msgSend$_alert:didBeginPlayingWithEvent:
+ _objc_msgSend$_appendPropertiesToBuilder:
+ _objc_msgSend$_beginAnimatingExposeMultitaskingPropertyWithMode:settings:
+ _objc_msgSend$_beginDeferringCompletionForReason:
+ _objc_msgSend$_clusterForExposeWithRects:count:stage:padding:screenScale:fullScreenRectsIfAny:
+ _objc_msgSend$_contentScaleForCommitProgress:contentInsets:additionalContentTranslation:
+ _objc_msgSend$_defaultSiriWorkspaceTransitionOptions
+ _objc_msgSend$_didSetCompositingFilter
+ _objc_msgSend$_didSetCornerAlpha
+ _objc_msgSend$_didSetCornerColor
+ _objc_msgSend$_didSetGrabberLineWidth
+ _objc_msgSend$_dismissAlertForItem:
+ _objc_msgSend$_dismissMenuBarWithCompletion:
+ _objc_msgSend$_doesElementHaveValidRequiredPriorityAssertion:
+ _objc_msgSend$_effectiveStageAreaForSnappingForSpace:configuration:
+ _objc_msgSend$_endDeferringCompletionForReason:
+ _objc_msgSend$_ensureSearchAffordanceIsInstalledInView:
+ _objc_msgSend$_firstElementLayoutModeSupportingProvider
+ _objc_msgSend$_flexibleAutoLayoutSpaceForZoomingAppLayout
+ _objc_msgSend$_handleRealTimeAppearanceChange:
+ _objc_msgSend$_initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:
+ _objc_msgSend$_isDeferringCompletionForAnyReason
+ _objc_msgSend$_isDeferringCompletionForReason:
+ _objc_msgSend$_isMenuBarGenerallyDisabled
+ _objc_msgSend$_isTouchLocationInSplitViewGutter:
+ _objc_msgSend$_layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:
+ _objc_msgSend$_loadLastAppearanceChangeWithCompletion:
+ _objc_msgSend$_maxScreenSizeWithDockAndStripInset
+ _objc_msgSend$_menuBarTitleFontFromStatusBarFont:
+ _objc_msgSend$_navigateToNextMenuHeaderForArrowKeyPress:
+ _objc_msgSend$_noteAppLayoutMovedToFront:
+ _objc_msgSend$_numberOfPeekingItemsAboveDisplayItem:zOrderedItems:
+ _objc_msgSend$_prefersStripHiddenAndDisabled
+ _objc_msgSend$_presentMenuViewNonInteractively:
+ _objc_msgSend$_previousDesktopSpaceItems
+ _objc_msgSend$_processMobileEquipmentInfo:forSlot:
+ _objc_msgSend$_requiredPriorityAssertionWithReason:creatingIfNecessary:
+ _objc_msgSend$_restoreDesktopSpaceAfterClosingFullScreenSpace
+ _objc_msgSend$_safeAreaCornerInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:
+ _objc_msgSend$_setupUI
+ _objc_msgSend$_shouldGroupIMEIsForPrimary:secondary:
+ _objc_msgSend$_shouldUpdateForDisplayOrdinal:
+ _objc_msgSend$_siriWorkspaceTransitionOptionsFromOpenApplicationOptions:
+ _objc_msgSend$_stopObservingAppearanceChanges
+ _objc_msgSend$_subscribeToAppearanceChanges
+ _objc_msgSend$_updateBorderViewMaskWithRect:
+ _objc_msgSend$_updateForcePeekingEdgeIfNeeded
+ _objc_msgSend$_updateIconViewImageForSuggestion:
+ _objc_msgSend$_updateLastAppearanceTimestamp:
+ _objc_msgSend$_updateOccupiedAreaForSpace:configuration:
+ _objc_msgSend$_updateRequiredPriorityAssertion
+ _objc_msgSend$_updateUI
+ _objc_msgSend$_updateVisibleSplitViewHandleDimmingViews
+ _objc_msgSend$_updateVisibleSplitViewHandleNubViews
+ _objc_msgSend$_updatesHomeScreenForAccessoryWithType:
+ _objc_msgSend$_windowManagementContextIsSingleAppModeForSwitcherCorrespondingToDisplayOrdinal:
+ _objc_msgSend$_windowingConfiguration
+ _objc_msgSend$acquireAssertionToPreventVideoCallPIPFromStartingUnderControlCenter:
+ _objc_msgSend$additionalKeyboardShortcutActionsForSession
+ _objc_msgSend$alert:didBeginPlayingWithEvent:
+ _objc_msgSend$appSwitcherModel:didMoveAppLayoutToFront:
+ _objc_msgSend$appearancePublisher
+ _objc_msgSend$audioSessionReporterID
+ _objc_msgSend$avoidOverridingAppFocusOnOtherDisplays
+ _objc_msgSend$browserEngineIsRegionallyRestricted
+ _objc_msgSend$completionDeferralReasons
+ _objc_msgSend$configureFileStackIcon:url:sortingBy:sortingOrderAscending:displayMode:anchorFrame:floatingDockFrame:sourceLayerRenderId:sourceContextId:openIndicatorLayerRenderId:openIndicatorContextId:iconImageInfoSize:iconImageInfoScale:iconImageContinuousCornerRadius:requestFromHost:fence:
+ _objc_msgSend$cornerColor
+ _objc_msgSend$cropsCompositingFilter
+ _objc_msgSend$darkTextColor
+ _objc_msgSend$didChangeThermalLevel:
+ _objc_msgSend$didUpdateAudioReporterId:
+ _objc_msgSend$effectiveStatusBarStyleRequestForActivationSettings:
+ _objc_msgSend$embeddedBrowserEngineIsRegionallyRestricted
+ _objc_msgSend$encodeWithCoder:
+ _objc_msgSend$exportedOSMigrationDefaultHomeScreenLayout
+ _objc_msgSend$fadeInDelayForSplitViewHandles
+ _objc_msgSend$frameForSplitViewHandleDimmingView:
+ _objc_msgSend$frameForSplitViewHandleNubView:
+ _objc_msgSend$grabberLineWidth
+ _objc_msgSend$hitTestedToSplitViewHandle:window:
+ _objc_msgSend$initWithAppLayout:addingToStage:
+ _objc_msgSend$initWithCoder:
+ _objc_msgSend$initWithFrame:systemPointerInteractionManager:
+ _objc_msgSend$initWithFromAppLayout:fromConfiguration:
+ _objc_msgSend$initWithItem:frame:corners:shadow:titleStyle:opacity:wallpaperGradientAttributes:perspectiveAngle:dimmingAlpha:animationAttributes:supportsHomeAffordance:spaceAccessoryViewModel:personalityDebugColorStyle:
+ _objc_msgSend$initWithPeekingAppLayout:configuration:
+ _objc_msgSend$initWithStartDate:endDate:maxEvents:lastN:reversed:
+ _objc_msgSend$initWithTransitionModifier:slidingOffPeekingAppLayout:fromPeekingConfiguration:
+ _objc_msgSend$initialScaleForSplitViewHandles
+ _objc_msgSend$intersectionHeight
+ _objc_msgSend$isAppLibraryOnlyByDefault
+ _objc_msgSend$isDismissingMenuForPointerHover
+ _objc_msgSend$isDownloading
+ _objc_msgSend$isKillableInSwitcher
+ _objc_msgSend$isObserving
+ _objc_msgSend$isSceneHandleKillableInSwitcher:
+ _objc_msgSend$isStatusBarHiddenForActivationSettings:withOrientation:
+ _objc_msgSend$lastAppearanceTimestamp
+ _objc_msgSend$lastIndex
+ _objc_msgSend$lastLayoutUnarchivedIdentifiers
+ _objc_msgSend$lastMultitaskingModeSwitchDate
+ _objc_msgSend$lsApplicationRecord
+ _objc_msgSend$maxHomeScreenDimmingAlphaForNonFullscreen
+ _objc_msgSend$maxHomeScreenDimmingAlphaResponse
+ _objc_msgSend$menuHeaderContainerView
+ _objc_msgSend$microphoneRecordingAttribution
+ _objc_msgSend$minHomeScreenDimmingAlphaResponse
+ _objc_msgSend$minimizingDisplayItem
+ _objc_msgSend$mutedMicrophoneRecordingActivityAttribution
+ _objc_msgSend$nubContainerView
+ _objc_msgSend$occupiedAreaPercentage
+ _objc_msgSend$openApplicationMenu
+ _objc_msgSend$organicExposeAppLayout
+ _objc_msgSend$osMigrationHomeScreenLayoutForRootFolder:
+ _objc_msgSend$percentageOfTransitionForSplitViewHandleFadeInDelay
+ _objc_msgSend$prepareToPresentMenuForIndirectInput
+ _objc_msgSend$previousDesktopItems
+ _objc_msgSend$publisherWithUseCase:options:
+ _objc_msgSend$recentAppLayouts:didMoveAppLayoutToFront:
+ _objc_msgSend$removeThermalObserver:
+ _objc_msgSend$requestRequiredPriorityAssertionWithReason:
+ _objc_msgSend$requiredPriorityAssertion
+ _objc_msgSend$safeAreaEdgeInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:
+ _objc_msgSend$sceneDidActivate:
+ _objc_msgSend$setArray:
+ _objc_msgSend$setCompletionDeferralReasons:
+ _objc_msgSend$setDismissingMenuForPointerHover:
+ _objc_msgSend$setHomeScreenDimmingAlpha:settings:behaviorMode:completion:
+ _objc_msgSend$setIgnoredAppLayout:
+ _objc_msgSend$setInitialScaleForSplitViewHandles:
+ _objc_msgSend$setIsObserving:
+ _objc_msgSend$setLastAppearanceTimestamp:
+ _objc_msgSend$setLastMultitaskingModeSwitchDate:
+ _objc_msgSend$setLaunchingOverDesktopSpaceAppLayout:
+ _objc_msgSend$setMaxHomeScreenDimmingAlphaForNonFullscreen:
+ _objc_msgSend$setMaxHomeScreenDimmingAlphaResponse:
+ _objc_msgSend$setMinHomeScreenDimmingAlphaResponse:
+ _objc_msgSend$setMinimizingDisplayItem:
+ _objc_msgSend$setOccupiedAreaPercentage:
+ _objc_msgSend$setPercentageOfTransitionForSplitViewHandleFadeInDelay:
+ _objc_msgSend$setPlaybackObserver:
+ _objc_msgSend$setPreferredMaximumMenuHeight:
+ _objc_msgSend$setPreviousDesktopItems:
+ _objc_msgSend$setShouldDismissForWorkspaceTransitions:
+ _objc_msgSend$setSplitViewHandleDimmingWidth:
+ _objc_msgSend$setSplitViewHandleNubWidth:
+ _objc_msgSend$setUnderlyingQueue:
+ _objc_msgSend$shouldForceFullscreenForDisplayOrdinal:
+ _objc_msgSend$shouldUpdateLayoutAttributesForDisplayOrdinal:
+ _objc_msgSend$sinkWithCompletion:shouldContinue:
+ _objc_msgSend$splitViewHandleDimmingWidth
+ _objc_msgSend$splitViewHandleFadeInSettings
+ _objc_msgSend$splitViewHandleFadeOutSettings
+ _objc_msgSend$splitViewHandleNubWidth
+ _objc_msgSend$switcherContentController:setHomeScreenDimmingAlpha:withSettings:animationMode:completion:
+ _objc_msgSend$systemApertureApertureElementAuthority:isElementPreferringToRemainVisible:
+ _objc_msgSend$systemApertureApertureElementAuthority:isElementRequiredPriority:
+ _objc_msgSend$systemApertureViewController:isDisplayingAnyRequiredSecureElements:
+ _objc_msgSend$toggleMenuBarVisibilityForSystemKeyboardShortcut
+ _objc_msgSend$topMostItemsByAddingAppLayoutAndAccessories:toTopMostItems:orderFront:
+ _objc_msgSend$topMostLayoutElementsByAddingAppLayoutAndAccessories:toTopMostLayoutElements:orderFront:
+ _objc_msgSend$unarchiveRootFolderFromArchive:withIconSource:
+ _objc_msgSend$underlyingQueue
+ _objc_msgSend$userDidClickInApp
+ _objc_msgSend$visibleInputViewFrame
+ _objc_msgSend$visibleSplitViewHandleDimmingViews
+ _objc_msgSend$visibleSplitViewHandleNubViews
+ _objc_msgSend$wantsDisableIdleTimer
+ _objc_msgSend$windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:
- -[SBActivationInfoViewController _processMobileEquipmentInfo:]
- -[SBActivationInfoViewController _processMobileSubscriptionInfo]
- -[SBActivationInfoViewController _titleForHeaderInSection:]
- -[SBActivityCoverSheetObserver _stopAlertingForActivityIdentifier:]
- -[SBAppExposeToHomeWindowingModifier gestureWillBegin:]
- -[SBApplicationInfo isRegionallyRestricted]
- -[SBArcSwipeCoplanarSessionWindowingModifier .cxx_destruct]
- -[SBArcSwipeCoplanarSessionWindowingModifier _coplanarSpacing]
- -[SBArcSwipeCoplanarSessionWindowingModifier _currentGestureIdentifier]
- -[SBArcSwipeCoplanarSessionWindowingModifier _edgeOfDisplayItem:]
- -[SBArcSwipeCoplanarSessionWindowingModifier _topMostDisplayItemInDisplayItemLayoutAttributesMap:]
- -[SBArcSwipeCoplanarSessionWindowingModifier appLayoutsToCacheFullsizeSnapshots]
- -[SBArcSwipeCoplanarSessionWindowingModifier complete]
- -[SBArcSwipeCoplanarSessionWindowingModifier frameForIndex:]
- -[SBArcSwipeCoplanarSessionWindowingModifier gestureDidComplete:]
- -[SBArcSwipeCoplanarSessionWindowingModifier gestureWillBegin:]
- -[SBArcSwipeCoplanarSessionWindowingModifier init]
- -[SBArcSwipeCoplanarSessionWindowingModifier scaleForIndex:]
- -[SBArcSwipeCoplanarSessionWindowingModifier scaleForLayoutRole:inAppLayout:]
- -[SBArcSwipeCoplanarSessionWindowingModifier stateModel]
- -[SBArcSwipeCoplanarSessionWindowingModifier timerFired:]
- -[SBArcSwipeCoplanarSessionWindowingModifier transitionDidComplete:]
- -[SBArcSwipeCoplanarSessionWindowingModifier transitionDidUpdate:]
- -[SBArcSwipeCoplanarSessionWindowingModifier transitionWillBegin:]
- -[SBArcSwipeCoplanarSessionWindowingModifier userDidInteractWithApp:]
- -[SBContinuousExposeHomeGestureSwitcherModifier animationAttributesForLayoutRole:inAppLayout:withAnimationAttributes:]
- -[SBContinuousExposeHomeGestureSwitcherModifier handleEvent:]
- -[SBContinuousExposeHomeGestureSwitcherModifier initWithGestureID:selectedAppLayout:startingEnvironmentMode:scrunchInitiated:continuingGesture:lastGestureWasAnArcSwipe:]
- -[SBCoverSheetPresentationManager coverSheetViewControllerDidObscureWallpaper:obscured:]
- -[SBCoverSheetPresentationManager coverSheetViewControllerDidOccludeWallpaper:occluded:]
- -[SBDefaultWindowingModifier resizeGrabberForItem:]
- -[SBDeviceApplicationSceneHandle _safeAreaCornerInsetsForApplicationFrame:screenBounds:interfaceOrientation:]
- -[SBDeviceApplicationSceneHandle effectiveStatusBarStyleRequestForActivation:]
- -[SBDeviceApplicationSceneHandle isStatusBarHiddenForActivation:forOrientation:]
- -[SBDeviceApplicationSceneHandle safeAreaEdgeInsetsForApplicationFrame:screenBounds:interfaceOrientation:]
- -[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:interfaceOrientation:]
- -[SBDisplayItemLayoutAttibutesProvider .cxx_destruct]
- -[SBDisplayItemLayoutAttibutesProvider init]
- -[SBDisplayItemLayoutAttibutesProvider lastInteractedDisplayItemInAppLayout:orientation:passingTest:]
- -[SBDisplayItemLayoutAttibutesProvider layoutAttributesEntriesForAppLayout:]
- -[SBDisplayItemLayoutAttibutesProvider layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:]
- -[SBDisplayItemLayoutAttibutesProvider layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.1
- -[SBDisplayItemLayoutAttibutesProvider layoutAttributesMapForAppLayout:displayOrdinal:orientation:]
- -[SBDisplayItemLayoutAttibutesProvider updateLayoutAttributes:forKey:]
- -[SBDisplayItemLayoutAttibutesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]
- -[SBDisplayItemLayoutAttibutesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.1
- -[SBDisplayItemLayoutAttibutesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.2
- -[SBDisplayItemLayoutAttibutesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.3
- -[SBDisplayItemLayoutAttibutesProvider updateLayoutAttributesMap:forAppLayout:displayOrdinal:orientation:]
- -[SBDisplayItemLayoutAttibutesProvider zOrderedItemsInAppLayout:orientation:]
- -[SBDisplayItemLayoutAttributes _initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:]
- -[SBDisplayItemLayoutAttributes initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:normalizedCenter:]
- -[SBDisplayItemLayoutAttributes initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:]
- -[SBDockToStageZoomWindowingModifier init]
- -[SBExposeWindowingModifier resizeGrabberForItem:]
- -[SBExternalDisplayEducationObserver _deviceConnectionWindowExpired:]
- -[SBExternalDisplayEducationObserver _deviceConnectionWindowExpired:].cold.1
- -[SBExternalDisplayEducationPillViewController initWithExtendedDisplayEnabled:]
- -[SBExternalDisplayEducationSession _dismissEducationAlert:]
- -[SBExternalDisplayEducationSession _presentBanner].cold.1
- -[SBExternalDisplayEducationSession _presentEducationAlert:]
- -[SBExternalDisplayEducationSession _presentEducationAlert:].cold.1
- -[SBExternalDisplayEducationSession _presentEducationAlert:].cold.2
- -[SBExternalDisplayEducationSession deviceConnectionWindowExpired]
- -[SBExternalDisplayEducationSession listener:shouldAcceptNewConnection:]
- -[SBExternalDisplayEducationSession listener:shouldAcceptNewConnection:].cold.1
- -[SBExternalDisplayEducationSession wakeUpConnection]
- -[SBFlexibleWindowingArcSwipeSwitcherModifier didMoveToParentModifier:]
- -[SBFlexibleWindowingArcSwipeSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:selectedAppLayout:selectedDisplayItem:]
- -[SBFlexibleWindowingArcSwipeSwitcherModifier initWithTransitionID:fromAppLayout:toAppLayout:selectedAppLayout:selectedDisplayItem:].cold.1
- -[SBFlexibleWindowingArcSwipeSwitcherModifier shouldPinLayoutRolesToSpace:]
- -[SBFlexibleWindowingArcSwipeSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:]
- -[SBFlexibleWindowingArcSwipeSwitcherModifier topMostLayoutElements]
- -[SBFlexibleWindowingArcSwipeSwitcherModifier topMostLayoutRolesForAppLayout:]
- -[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:]
- -[SBFlexibleWindowingExposeToHomePeekWindowingModifier willBegin]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier _frameOffsetForActiveCard]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier _frameOffsetForAdjacentCards]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier _layoutSettingsForLayoutRole:inAppLayout:layoutSettings:]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier adjustedSpaceAccessoryViewFrame:forAppLayout:]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier adjustedSpaceAccessoryViewScale:forAppLayout:]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier animationAttributesForLayoutRole:inAppLayout:withAnimationAttributes:]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier footerViewIconAlignmentForAppLayout:]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier initWithGestureID:selectedAppLayout:startingEnvironmentMode:scrunchInitiated:continuingGesture:lastGestureWasAnArcSwipe:]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier isHomeAffordanceSupportedForAppLayout:]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier isShowingMultitasking]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier selectedDisplayItem]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier topMostLayoutElements]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier topMostLayoutRolesForAppLayout:]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier visibleHomeAffordanceLayoutElements]
- -[SBFluidSwitcherItemContainer _layoutResizeGrabber]
- -[SBFluidSwitcherItemContainer _teardownResizeGrabberIfNeeded]
- -[SBFluidSwitcherItemContainer dealloc]
- -[SBFluidSwitcherItemContainer pointerInteractionHitTestInsetsForView:]
- -[SBFluidSwitcherItemContainer resizeGrabberCenterY]
- -[SBFluidSwitcherItemContainer resizeGrabberEdge]
- -[SBFluidSwitcherItemContainer setResizeGrabberCenterY:]
- -[SBFluidSwitcherItemContainer setResizeGrabberEdge:systemPointerInteractionManager:]
- -[SBFluidSwitcherItemContainer shouldBeginPointerInteractionRequest:atLocation:forView:]
- -[SBFluidSwitcherItemContainer styleForRegion:forView:]
- -[SBFluidSwitcherSpaceTitleItemController _loadIconForDisplayItem:]
- -[SBFluidSwitcherViewController hitTestedToResizeGrabber:window:ofItemContainer:]
- -[SBFluidSwitcherViewController setResizeGrabberHitTestRect:forView:]
- -[SBHomePeekToFullScreenTransitionModifier gestureWillBegin:]
- -[SBHomePeekToFullScreenTransitionModifier initWithTransitionModifier:]
- -[SBHomePeekToFullScreenTransitionModifier initWithTransitionModifier:].cold.1
- -[SBHomePeekToFullScreenTransitionModifier transitionDidComplete:]
- -[SBHomePeekToHomeTransitionModifier initWithFromAppLayout:]
- -[SBHomePeekToHomeTransitionModifier initWithFromAppLayout:].cold.1
- -[SBHomePeekWindowingModifier initWithPeekingAppLayout:]
- -[SBHomePeekWindowingModifier initWithPeekingAppLayout:].cold.1
- -[SBHomePeekWindowingModifier resizeGrabberForItem:]
- -[SBHomePeekWindowingModifier transitionDidComplete:]
- -[SBHomeScreenController(AppearanceControlling) setHomeScreenDimmingAlpha:behaviorMode:completion:]
- -[SBMainSwitcherControllerCoordinator switcherContentController:setHomeScreenDimmingAlpha:withAnimationMode:completion:]
- -[SBMainWorkspace createRequestWithOptions:displayConfiguration:].cold.1
- -[SBMainWorkspace createRequestWithOptions:displayConfiguration:].cold.2
- -[SBMenuBarMainMenuView prepareToPresentMenuForPointerHover]
- -[SBMenuBarMainMenuView presentingMenuForPointerHover]
- -[SBMenuBarMainMenuView setPresentingMenuForPointerHover:]
- -[SBSALayoutModeSupportingProvider preferencesFromContext:].cold.1
- -[SBSpotlightPresentableViewController _createSearchAffordanceReferenceBackgroundFadeProperty]
- -[SBSpotlightPresentableViewController supportsSolarium]
- -[SBSpringBoardApplicationIcon _generateImageWithInfo:traitCollection:options:]
- -[SBSpringBoardApplicationIcon makeIconImageWithInfo:traitCollection:options:]
- -[SBSpringBoardApplicationIconDataSource canGenerateIconsInBackgroundForIcon:]
- -[SBSpringBoardApplicationIconDataSource icon:layerWithInfo:traitCollection:options:]
- -[SBSwitcherModifier(WindowingModifier) resizeGrabberForItem:]
- -[SBSwitcherWindowingConfiguration resizeGrabberWidth]
- -[SBSwitcherWindowingConfiguration setResizeGrabberWidth:]
- -[SBSystemApertureViewController systemApertureApertureElementAuthority:isElementRequiredToRemainVisible:]
- -[SBWindowScenePIPManager _adjustPIPInsetsForKeyboardFrameChangeNotification:]
- -[SBWindowScenePIPManager _keyboardFrameInScreenSpaceFromNotification:]
- -[SBWindowScenePIPManager _keyboardWillChangeFrame:]
- -[SBWindowScenePIPManager _keyboardWillChangeFrame:].cold.1
- -[SBWindowScenePIPManager _keyboardWillRotate:]
- -[SBWindowScenePIPManager _keyboardWillShowOrHide:]
- -[SBWindowScenePIPManager _keyboardWillShowOrHide:].cold.1
- -[SBWindowScenePIPManager _keyboardWillShowOrHide:].cold.2
- -[SBWindowScenePIPManager _visualizeKeyboardFrameIfNeeded]
- -[SBWindowingItemViewModel initWithItem:frame:corners:shadow:resizeGrabber:titleStyle:opacity:wallpaperGradientAttributes:perspectiveAngle:dimmingAlpha:animationAttributes:supportsHomeAffordance:spaceAccessoryViewModel:personalityDebugColorStyle:]
- -[SBWindowingItemViewModel initWithItem:frame:corners:shadow:resizeGrabber:titleStyle:opacity:wallpaperGradientAttributes:perspectiveAngle:dimmingAlpha:animationAttributes:supportsHomeAffordance:spaceAccessoryViewModel:personalityDebugColorStyle:].cold.1
- -[SBWindowingItemViewModel resizeGrabber]
- -[SBWindowingItemViewModel setResizeGrabber:]
- -[SBWindowingItemViewModelModifier resizeGrabber]
- -[SBWindowingModifier resizeGrabberForItem:]
- GCC_except_table136
- GCC_except_table147
- GCC_except_table149
- GCC_except_table155
- GCC_except_table167
- GCC_except_table194
- GCC_except_table217
- GCC_except_table223
- GCC_except_table231
- GCC_except_table233
- GCC_except_table268
- GCC_except_table271
- GCC_except_table274
- GCC_except_table297
- GCC_except_table300
- GCC_except_table309
- GCC_except_table311
- GCC_except_table312
- GCC_except_table314
- GCC_except_table343
- GCC_except_table345
- GCC_except_table360
- GCC_except_table366
- GCC_except_table367
- GCC_except_table375
- GCC_except_table381
- GCC_except_table383
- GCC_except_table384
- GCC_except_table390
- GCC_except_table431
- GCC_except_table438
- GCC_except_table467
- GCC_except_table475
- GCC_except_table477
- GCC_except_table517
- GCC_except_table526
- GCC_except_table562
- GCC_except_table597
- GCC_except_table665
- GCC_except_table689
- GCC_except_table692
- GCC_except_table732
- GCC_except_table771
- GCC_except_table811
- GCC_except_table820
- GCC_except_table862
- GCC_except_table901
- _OBJC_CLASS_$_SBArcSwipeCoplanarSessionWindowingModifier
- _OBJC_CLASS_$_SBDisplayItemLayoutAttibutesProvider
- _OBJC_IVAR_$_SBActivationInfoViewController._mobileSubscriptionInfo
- _OBJC_IVAR_$_SBArcSwipeCoplanarSessionWindowingModifier._currentDisplayItemIndex
- _OBJC_IVAR_$_SBArcSwipeCoplanarSessionWindowingModifier._gestureCount
- _OBJC_IVAR_$_SBArcSwipeCoplanarSessionWindowingModifier._initialAppLayout
- _OBJC_IVAR_$_SBArcSwipeCoplanarSessionWindowingModifier._nextDisplayItem
- _OBJC_IVAR_$_SBArcSwipeCoplanarSessionWindowingModifier._orderedVisitedDisplayItems
- _OBJC_IVAR_$_SBArcSwipeCoplanarSessionWindowingModifier._pendingComplete
- _OBJC_IVAR_$_SBArcSwipeCoplanarSessionWindowingModifier._previousDisplayItem
- _OBJC_IVAR_$_SBArcSwipeCoplanarSessionWindowingModifier._selectedAppLayout
- _OBJC_IVAR_$_SBArcSwipeCoplanarSessionWindowingModifier._shouldUpdateLayoutAfterSettling
- _OBJC_IVAR_$_SBArcSwipeCoplanarSessionWindowingModifier._trailingDisplayItems
- _OBJC_IVAR_$_SBArcSwipeCoplanarSessionWindowingModifier._uniqueID
- _OBJC_IVAR_$_SBContinuousExposeHomeGestureSwitcherModifier._flexibleHomeGestureIsShowingMultitasking
- _OBJC_IVAR_$_SBContinuousExposeHomeGestureSwitcherModifier._flexibleHomeGestureModifier
- _OBJC_IVAR_$_SBContinuousExposeRootSwitcherModifier._arcSwipeModifier
- _OBJC_IVAR_$_SBDisplayItemLayoutAttibutesProvider._storage
- _OBJC_IVAR_$_SBExposeWindowingModifier._effectiveCurrentAppLayout
- _OBJC_IVAR_$_SBExposeWindowingModifier._hasLatchedOverflowPeekingOffset
- _OBJC_IVAR_$_SBExposeWindowingModifier._overflowPeekingOffset
- _OBJC_IVAR_$_SBExternalDisplayEducationPillViewController._extendedDisplayEnabled
- _OBJC_IVAR_$_SBExternalDisplayEducationSession._alertHandle
- _OBJC_IVAR_$_SBExternalDisplayEducationSession._listener
- _OBJC_IVAR_$_SBExternalDisplayEducationSession._previousPresentedReasons
- _OBJC_IVAR_$_SBExternalDisplayEducationSession._xpcConnection
- _OBJC_IVAR_$_SBFlexibleWindowingArcSwipeSwitcherModifier._arcSwipeModifier
- _OBJC_IVAR_$_SBFlexibleWindowingArcSwipeSwitcherModifier._selectedAppLayout
- _OBJC_IVAR_$_SBFlexibleWindowingArcSwipeSwitcherModifier._selectedDisplayItem
- _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._appSwitcherModifier
- _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._cached_autoLayoutSpaceWithDraggedItemExcluded
- _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._nextFullScreenAppLayout
- _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._nextFullScreenDisplayItem
- _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._postGestureTransitionDelay
- _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._previousFullScreenAppLayout
- _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._previousFullScreenDisplayItem
- _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._selectedDisplayItem
- _OBJC_IVAR_$_SBFlexibleWindowingHomeGestureSwitcherModifier._translationYWhenTriggeredMultitasking
- _OBJC_IVAR_$_SBFluidSwitcherItemContainer._resizeGrabber
- _OBJC_IVAR_$_SBFluidSwitcherItemContainer._resizeGrabberCenterY
- _OBJC_IVAR_$_SBFluidSwitcherItemContainer._resizeGrabberEdge
- _OBJC_IVAR_$_SBFluidSwitcherViewController._resizeGrabberViewsToHitTestRects
- _OBJC_IVAR_$_SBInteractiveScreenshotGestureRootViewController._queue_displayCornerRadius
- _OBJC_IVAR_$_SBMenuBarMainMenuView._presentingMenuForPointerHover
- _OBJC_IVAR_$_SBSpotlightPresentableViewController._supportsSolarium
- _OBJC_IVAR_$_SBSwitcherWindowingConfiguration._resizeGrabberWidth
- _OBJC_IVAR_$_SBWindowScenePIPManager._assumingKeyboardIsVisible
- _OBJC_IVAR_$_SBWindowingItemViewModel._resizeGrabber
- _OBJC_METACLASS_$_SBArcSwipeCoplanarSessionWindowingModifier
- _OBJC_METACLASS_$_SBDisplayItemLayoutAttibutesProvider
- _SBExternalDisplayEducationReasonMaskDescription
- _SBHGetGraphicIconLayerWithImageAppearance
- _SBHIconServicesOptionsForImageOptions
- _SBIdleTimerUpdateReasonMainDisplaySceneManagerPrefix
- _SBWindowingItemResizeGrabberMake
- _UIKeyboardEndIntersectionHeightIncludingAccessory
- __OBJC_$_INSTANCE_METHODS_SBArcSwipeCoplanarSessionWindowingModifier
- __OBJC_$_INSTANCE_METHODS_SBDisplayItemLayoutAttibutesProvider
- __OBJC_$_INSTANCE_VARIABLES_SBArcSwipeCoplanarSessionWindowingModifier
- __OBJC_$_INSTANCE_VARIABLES_SBDisplayItemLayoutAttibutesProvider
- __OBJC_$_PROP_LIST_SBDisplayItemLayoutAttibutesProvider
- __OBJC_$_PROP_LIST_SBWindowingItemViewModel.140
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBExternalDisplayHardwareRequirementsChangedProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBRemoteHandshakeProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBExternalDisplayHardwareRequirementsChangedProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBRemoteHandshakeProtocol
- __OBJC_CLASS_PROTOCOLS_$_SBDisplayItemLayoutAttibutesProvider
- __OBJC_CLASS_RO_$_SBArcSwipeCoplanarSessionWindowingModifier
- __OBJC_CLASS_RO_$_SBDisplayItemLayoutAttibutesProvider
- __OBJC_LABEL_PROTOCOL_$_SBExternalDisplayHardwareRequirementsChangedProtocol
- __OBJC_LABEL_PROTOCOL_$_SBRemoteHandshakeProtocol
- __OBJC_METACLASS_RO_$_SBArcSwipeCoplanarSessionWindowingModifier
- __OBJC_METACLASS_RO_$_SBDisplayItemLayoutAttibutesProvider
- __OBJC_PROTOCOL_$_SBExternalDisplayHardwareRequirementsChangedProtocol
- __OBJC_PROTOCOL_$_SBRemoteHandshakeProtocol
- __OBJC_PROTOCOL_REFERENCE_$_SBExternalDisplayHardwareRequirementsChangedProtocol
- __OBJC_PROTOCOL_REFERENCE_$_SBRemoteHandshakeProtocol
- ___101-[SBDisplayItemLayoutAttibutesProvider lastInteractedDisplayItemInAppLayout:orientation:passingTest:]_block_invoke
- ___102-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:]_block_invoke
- ___102-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:]_block_invoke_2
- ___102-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:]_block_invoke_3
- ___102-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:]_block_invoke_4
- ___102-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:]_block_invoke_5
- ___102-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:]_block_invoke_6
- ___102-[SBFlexibleWindowingAutoLayoutController _clusterForExposeWithRects:count:stage:padding:screenScale:]_block_invoke_7
- ___108-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:interfaceOrientation:]_block_invoke
- ___108-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:interfaceOrientation:]_block_invoke_2
- ___108-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:interfaceOrientation:]_block_invoke_3
- ___108-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:interfaceOrientation:]_block_invoke_4
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.297
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.298
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.299
- ___113-[SBFluidSwitcherViewController initWithPersonality:liveContentOverlayCoordinator:dataSource:delegate:debugName:]_block_invoke.163
- ___113-[SBSystemApertureElementAuthority elementsOrderedByPromotionFromTemporallyOrderedElements:withPreviousOrdering:]_block_invoke.61
- ___116-[SBDisplayItemLayoutAttibutesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]_block_invoke
- ___116-[SBDisplayItemLayoutAttibutesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]_block_invoke_2
- ___118-[SBContinuousExposeHomeGestureSwitcherModifier animationAttributesForLayoutRole:inAppLayout:withAnimationAttributes:]_block_invoke
- ___134-[SBFlexibleWindowingHomeGestureSwitcherModifier _getActivePositionAndScaleForLayoutRole:inAppLayout:withBounds:outPosition:outScale:]_block_invoke_2
- ___35-[SBMenuBarManager _dismissMenuBar]_block_invoke
- ___35-[SBMenuBarManager _dismissMenuBar]_block_invoke_2
- ___35-[SBMenuBarManager _dismissMenuBar]_block_invoke_3
- ___45-[SBActivityCoverSheetObserver presentAlert:]_block_invoke
- ___50-[SBIconModel exportedOSMigrationHomeScreenLayout]_block_invoke
- ___50-[SBIconModel exportedOSMigrationHomeScreenLayout]_block_invoke_2
- ___50-[SBIconModel exportedOSMigrationHomeScreenLayout]_block_invoke_3
- ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.85
- ___52-[SBLockScreenManager _setPasscodeVisible:animated:]_block_invoke.389
- ___53-[SBExternalDisplayEducationSession displayConnected]_block_invoke
- ___53-[SBExternalDisplayEducationSession displayConnected]_block_invoke.50
- ___53-[SBThermalController startListeningForThermalEvents]_block_invoke.20
- ___53-[SBThermalController startListeningForThermalEvents]_block_invoke.22
- ___54-[SBArcSwipeCoplanarSessionWindowingModifier complete]_block_invoke
- ___54-[SBDeckSwitcherPanGestureWorkspaceTransaction _begin]_block_invoke
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.377
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.379
- ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.716
- ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.501
- ___58-[SBDockToStageZoomWindowingModifier transitionWillBegin:]_block_invoke_3
- ___58-[SBDockToStageZoomWindowingModifier transitionWillBegin:]_block_invoke_4
- ___58-[SBWindowScenePIPManager _visualizeKeyboardFrameIfNeeded]_block_invoke
- ___59-[SBFloatingDockRemoteContentManager iconView:performDrop:]_block_invoke.66
- ___59-[SBThermalController _updateThermalJetsamCPUSamplingState]_block_invoke.61
- ___59-[SBThermalController _updateThermalJetsamCPUSamplingState]_block_invoke.66
- ___59-[SBThermalController _updateThermalJetsamCPUSamplingState]_block_invoke.68
- ___60-[SBExternalDisplayEducationSession _presentEducationAlert:]_block_invoke
- ___60-[SBExternalDisplayEducationSession _presentEducationAlert:]_block_invoke.cold.1
- ___60-[SBMainWorkspace _preflightTransitionRequest:forExecution:]_block_invoke.376
- ___61-[SBContinuousExposeHomeGestureSwitcherModifier handleEvent:]_block_invoke
- ___63-[SBContinuousExposeHomeGestureSwitcherModifier frameForIndex:]_block_invoke_2
- ___63-[SBContinuousExposeHomeGestureSwitcherModifier scaleForIndex:]_block_invoke_2
- ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke.207
- ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke_2.210
- ___66-[SBArcSwipeCoplanarSessionWindowingModifier transitionDidUpdate:]_block_invoke
- ___66-[SBArcSwipeCoplanarSessionWindowingModifier transitionWillBegin:]_block_invoke
- ___66-[SBArcSwipeCoplanarSessionWindowingModifier transitionWillBegin:]_block_invoke_2
- ___66-[SBExternalDisplayEducationSession deviceConnectionWindowExpired]_block_invoke
- ___67-[SBFluidSwitcherSpaceTitleItemController _loadIconForDisplayItem:]_block_invoke
- ___67-[SBFluidSwitcherSpaceTitleItemController _loadIconForDisplayItem:]_block_invoke_2
- ___68-[SBFlexibleWindowingArcSwipeSwitcherModifier topMostLayoutElements]_block_invoke
- ___68-[SBFlexibleWindowingArcSwipeSwitcherModifier topMostLayoutElements]_block_invoke_2
- ___68-[SBFlexibleWindowingArcSwipeSwitcherModifier topMostLayoutElements]_block_invoke_3
- ___69-[SBContinuousExposeHomeGestureSwitcherModifier anchorPointForIndex:]_block_invoke_2
- ___71-[SBCoverSheetIconFlyInAnimator _updateLabelAlphaForPresentationValue:]_block_invoke.47
- ___72-[SBCoverSheetIconFlyInAnimator _updateSpreadMultiplierForPresentation:]_block_invoke.41
- ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.386
- ___74-[SBExposeWindowingModifier _captureModelForOverflowAndManualModeIfNeeded]_block_invoke_7
- ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1025
- ___75-[SBFlexibleWindowingArcSwipeSwitcherModifier shouldPinLayoutRolesToSpace:]_block_invoke
- ___75-[SBFlexibleWindowingArcSwipeSwitcherModifier shouldPinLayoutRolesToSpace:]_block_invoke_2
- ___75-[SBFlexibleWindowingArcSwipeSwitcherModifier shouldPinLayoutRolesToSpace:]_block_invoke_3
- ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.408
- ___76-[SBDisplayItemLayoutAttibutesProvider layoutAttributesEntriesForAppLayout:]_block_invoke
- ___77-[SBContinuousExposeHomeGestureSwitcherModifier shouldPinLayoutRolesToSpace:]_block_invoke
- ___78-[SBFlexibleWindowingArcSwipeSwitcherModifier topMostLayoutRolesForAppLayout:]_block_invoke
- ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke.114
- ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_2.117
- ___79-[SBMainWorkspace _removeApplicationEntities:withDestructionIntent:completion:]_block_invoke.468
- ___80-[SBArcSwipeCoplanarSessionWindowingModifier appLayoutsToCacheFullsizeSnapshots]_block_invoke
- ___80-[SBArcSwipeCoplanarSessionWindowingModifier appLayoutsToCacheFullsizeSnapshots]_block_invoke_2
- ___80-[SBContinuousExposeHomeGestureSwitcherModifier scaleForLayoutRole:inAppLayout:]_block_invoke
- ___80-[SBSystemUISceneController _createOrRetrievePresenterForDisplayIdentity:level:]_block_invoke.111
- ___81-[SBFlexibleWindowingHomeGestureSwitcherModifier scaleForLayoutRole:inAppLayout:]_block_invoke
- ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.438
- ___83-[SBFlexibleWindowingHomeGestureSwitcherModifier _updateForGestureDidEndWithEvent:]_block_invoke
- ___83-[SBFlexibleWindowingHomeGestureSwitcherModifier _updateForGestureDidEndWithEvent:]_block_invoke_2
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.356
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.357
- ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.81
- ___89-[SBContinuousExposeHomeGestureSwitcherModifier occlusionStateForLayoutRole:inAppLayout:]_block_invoke
- ___89-[SBFlexibleWindowingHomeGestureSwitcherModifier _responseForActivatingFinalDestination:]_block_invoke
- ___90-[SBFlexibleWindowingHomeGestureSwitcherModifier occlusionStateForLayoutRole:inAppLayout:]_block_invoke
- ___91-[SBContinuousExposeHomeGestureSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:]_block_invoke_2
- ___91-[SBFlexibleWindowingArcSwipeSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:]_block_invoke
- ___91-[SBFlexibleWindowingArcSwipeSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:]_block_invoke_2
- ___91-[SBFlexibleWindowingArcSwipeSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:]_block_invoke_3
- ___92-[SBFlexibleWindowingHomeGestureSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:]_block_invoke
- ___93-[SBContinuousExposeHomeGestureSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:]_block_invoke
- ___94-[SBExternalDisplayEducationSession updateHardwareAvailability:withinDisplayConnectionWindow:]_block_invoke
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.640
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.662
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.677
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.689
- ___94-[SBSpotlightPresentableViewController _createSearchAffordanceReferenceBackgroundFadeProperty]_block_invoke
- ___94-[SBSpotlightPresentableViewController _createSearchAffordanceReferenceBackgroundFadeProperty]_block_invoke_2
- ___99-[SBHomeScreenController(AppearanceControlling) setHomeScreenDimmingAlpha:behaviorMode:completion:]_block_invoke
- ___99-[SBHomeScreenController(AppearanceControlling) setHomeScreenDimmingAlpha:behaviorMode:completion:]_block_invoke_2
- ___blockIMPFromContextSignature101_block_invoke
- ___blockIMPFromEventSignature101_block_invoke
- ___blockIMPFromQuerySignature101_block_invoke
- ___block_descriptor_32_e29_v24?0"SBPIPController"8^B16l
- ___block_descriptor_40_e8_32r_e45_v24?0"SBSwitcherModifierEventResponse"8^B16lr32l8
- ___block_descriptor_40_e8_32s_e18_v16?0"UIButton"8ls32l8
- ___block_descriptor_40_e8_32s_e47_v32?0"SBDeviceApplicationSceneEntity"8Q16^B24ls32l8
- ___block_descriptor_48_e64_{SBWindowingItemResizeGrabber=Qd}24?0"SBChainableModifier"816l
- ___block_descriptor_48_e8_32s_e8_v12?0i8ls32l8
- ___block_descriptor_56_e8_32s40bs48w_e21_v16?0"_UIMainMenu"8lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e34_v16?0"_UIMainMenuStateResponse"8lw48l8s40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e36_v16?0"_UIMainMenuSessionResponse"8lw48l8s40l8s32l8
- ___block_descriptor_56_e8_32s40bs_e26_v16?0"BSActionResponse"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s_e8_v12?0i8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e72_v20?0B8"SBDashBoardHostableEntityHostingFluidSwitcherViewController"12ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
- ___block_descriptor_72_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e45_v16?0"<SBHIconImageCacheResultDescribing>"8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.1038
- ___block_literal_global.114
- ___block_literal_global.1192
- ___block_literal_global.1240
- ___block_literal_global.210
- ___block_literal_global.215
- ___block_literal_global.254
- ___block_literal_global.270
- ___block_literal_global.272
- ___block_literal_global.314
- ___block_literal_global.330
- ___block_literal_global.332
- ___block_literal_global.344
- ___block_literal_global.372
- ___block_literal_global.447
- ___block_literal_global.457
- ___block_literal_global.461
- ___block_literal_global.467
- ___block_literal_global.485
- ___block_literal_global.490
- ___block_literal_global.493
- ___block_literal_global.536
- ___block_literal_global.574
- ___block_literal_global.580
- ___block_literal_global.585
- ___block_literal_global.589
- ___block_literal_global.591
- ___block_literal_global.593
- ___block_literal_global.595
- ___block_literal_global.610
- ___block_literal_global.620
- ___block_literal_global.627
- ___block_literal_global.663
- ___block_literal_global.689
- ___block_literal_global.731
- ___block_literal_global.800
- ___block_literal_global.805
- ___block_literal_global.807
- ___block_literal_global.812
- ___block_literal_global.814
- ___block_literal_global.833
- _blockIMPFromContextSignature101
- _blockIMPFromEventSignature101
- _blockIMPFromQuerySignature101
- _objc_msgSend$_clusterForExposeWithRects:count:stage:padding:screenScale:
- _objc_msgSend$_createSearchAffordanceReferenceBackgroundFadeProperty
- _objc_msgSend$_currentGestureIdentifier
- _objc_msgSend$_dismissEducationAlert:
- _objc_msgSend$_edgeOfDisplayItem:
- _objc_msgSend$_endpoint
- _objc_msgSend$_frameOffsetForActiveCard
- _objc_msgSend$_generateImageWithInfo:traitCollection:options:
- _objc_msgSend$_iconImageForDisplayItem:
- _objc_msgSend$_initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:
- _objc_msgSend$_layoutResizeGrabber
- _objc_msgSend$_layoutSettingsForLayoutRole:inAppLayout:layoutSettings:
- _objc_msgSend$_loadIconForDisplayItem:
- _objc_msgSend$_presentEducationAlert:
- _objc_msgSend$_processMobileEquipmentInfo:
- _objc_msgSend$_processMobileSubscriptionInfo
- _objc_msgSend$_safeAreaCornerInsetsForApplicationFrame:screenBounds:interfaceOrientation:
- _objc_msgSend$_secondarySubscriptionInfo
- _objc_msgSend$_teardownResizeGrabberIfNeeded
- _objc_msgSend$_titleForHeaderInSection:
- _objc_msgSend$activeTextEffectsWindowForWindowScene:
- _objc_msgSend$anonymousListener
- _objc_msgSend$appKeyboardShortcutActionsForSession
- _objc_msgSend$audioRecordingActivityAttribution
- _objc_msgSend$bottomPaddingToKeyboard
- _objc_msgSend$configureFileStackIcon:url:sortingBy:sortingOrderAscending:displayMode:anchorFrame:floatingDockFrame:sourceLayerRenderId:sourceContextId:openIndicatorLayerRenderId:openIndicatorContextId:requestFromHost:fence:
- _objc_msgSend$deviceConnectionWindowExpired
- _objc_msgSend$effectiveSpotlightSearchFieldAvoidanceHeight
- _objc_msgSend$effectiveStatusBarStyleRequestForActivation:
- _objc_msgSend$externalDisplayEducationReasons
- _objc_msgSend$externalDisplayHardwareRequirementsSatisfiedChanged:
- _objc_msgSend$hitTestedToResizeGrabber:window:ofItemContainer:
- _objc_msgSend$initWithExtendedDisplayEnabled:
- _objc_msgSend$initWithFrame:backgroundView:
- _objc_msgSend$initWithFromAppLayout:
- _objc_msgSend$initWithFromLeafAppLayout:throughLeafAppLayout:
- _objc_msgSend$initWithItem:frame:corners:shadow:resizeGrabber:titleStyle:opacity:wallpaperGradientAttributes:perspectiveAngle:dimmingAlpha:animationAttributes:supportsHomeAffordance:spaceAccessoryViewModel:personalityDebugColorStyle:
- _objc_msgSend$initWithPeekingAppLayout:
- _objc_msgSend$initWithTransitionID:fromAppLayout:toAppLayout:selectedAppLayout:selectedDisplayItem:
- _objc_msgSend$initWithTransitionModifier:
- _objc_msgSend$isRegionallyRestricted
- _objc_msgSend$isShowingMultitasking
- _objc_msgSend$isShownWithinWindowScene:
- _objc_msgSend$isStatusBarHiddenForActivation:forOrientation:
- _objc_msgSend$makeSearchAffordanceBackgroundCapturingView
- _objc_msgSend$menuState
- _objc_msgSend$newHomeScreenButtonBackgroundView
- _objc_msgSend$prepareToPresentMenuForPointerHover
- _objc_msgSend$resizeGrabber
- _objc_msgSend$resizeGrabberEdge
- _objc_msgSend$resizeGrabberForItem:
- _objc_msgSend$resizeGrabberWidth
- _objc_msgSend$safeAreaEdgeInsetsForApplicationFrame:screenBounds:interfaceOrientation:
- _objc_msgSend$searchAffordanceReferenceBackgroundView
- _objc_msgSend$selectedDisplayItem
- _objc_msgSend$setArcSwipeInitialAppLayout:
- _objc_msgSend$setArcSwipeNextDisplayItem:
- _objc_msgSend$setArcSwipePreviousDisplayItem:
- _objc_msgSend$setExternalDisplayEducationReasons:
- _objc_msgSend$setHomeScreenDimmingAlpha:behaviorMode:completion:
- _objc_msgSend$setInitialMenuStateIdentifier:
- _objc_msgSend$setNubStyle:
- _objc_msgSend$setPrefersEmbeddedDisplayPresentation:
- _objc_msgSend$setResizeGrabberCenterY:
- _objc_msgSend$setResizeGrabberEdge:systemPointerInteractionManager:
- _objc_msgSend$setResizeGrabberHitTestRect:forView:
- _objc_msgSend$setResizeGrabberWidth:
- _objc_msgSend$setXpcEndpoint:
- _objc_msgSend$switcherContentController:setHomeScreenDimmingAlpha:withAnimationMode:completion:
- _objc_msgSend$systemApertureApertureElementAuthority:isElementRequiredToRemainVisible:
- _objc_msgSend$uppercaseString
- _objc_msgSend$windowControlsLayoutForApplicationFrame:screenBounds:interfaceOrientation:
- _objc_msgSend$windowingViewModelForAppLayout:
CStrings:
+ "$!"
+ "%@ customSize=%@"
+ "%{public}@ display connected, presenting education banner now."
+ "%{public}@ display disconnected, dismissing education banner now."
+ "%{public}@ hardware become available during display connection window, presenting banner now."
+ "-[SBDisplayItemLayoutAttributesProvider layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:]"
+ "-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]"
+ "-[SBHomeScreenService osMigrationDefaultHomeScreenLayout]"
+ "<%@: %p; didDisappear: %@; elementContentProvider: %@; pendingDismissalTransitionIdentifiers: %@; registeredContainerDismissalInterfacePropertyIdentifiers: %@;>"
+ "@\"<SBDisplayItemLayoutAttributesProviderDelegate>\""
+ "@\"BPSPublisher\""
+ "@\"CABackdropLayer\""
+ "@\"SBSAElementRemovalTransitionProvider\""
+ "@16@?0@\"SBFlexibleWindowingAutoLayoutGroup\"8"
+ "@16@?0@\"SBSwitcherSplitViewHandleNubElement\"8"
+ "@232@0:8q16q24q32{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}40{SBDisplayItemTileConfiguration=q{CGSize=dd}}96{CGPoint=dd}120B136q140{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}148{CGPoint=dd}204B220q224"
+ "@292@0:8@16{SBWindowingItemFrame={CGRect={CGPoint=dd}{CGSize=dd}}{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}}24{SBWindowingItemCorners={UIRectCornerRadii=dddd}Q}120{SBWindowingItemShadow=dq}160{SBWindowingItemTitleStyle=dddqQ}176d216{SBSwitcherWallpaperGradientAttributes=dd}224{CGPoint=dd}240d256@264B272@276Q284"
+ "@32@0:8r^@16Q24"
+ "A split view handle can only be between exactly two items"
+ "All SBSAElementLayoutModeSupporting providers currently do not support LayoutModeNone."
+ "Appearance"
+ "ApplicationSnapshot"
+ "B16@?0@\"BMStoreEvent\"8"
+ "B16@?0@\"SBSwitcherSplitViewHandleDimmingElement\"8"
+ "B16@?0@\"SBSwitcherSplitViewHandleNubElement\"8"
+ "B24@?0@\"<SBSwitcherLayoutElementProviding>\"8^B16"
+ "B24@?0@\"NSString\"8@16"
+ "B24@?0@\"SBSwitcherSplitViewHandleDimmingElement\"8@\"SBSplitViewHandleDimmingView\"16"
+ "B24@?0@\"SBSwitcherSplitViewHandleNubElement\"8@\"SBSplitViewHandleNubView\"16"
+ "Backlight changed: newBacklightFactor=%@, disable SS=%{BOOL}u"
+ "Backlight notification received with nil newBacklightFactor"
+ "Blocking remote transient overlay activation request because it is blocked by proximity reader"
+ "Both elements required priority, element '%@' temporally after '%@'"
+ "Can't read Display.Appearance stream with error: %@"
+ "Changing lock provider empty state"
+ "Could not find registered milestone for: %@"
+ "Created required priority assertion (%{public}@) with reason '%{public}@' for element: %{public}@"
+ "Critical Thermal State"
+ "Disabling SS gesture recognizer, reason: %{public}@"
+ "Display appearance live stream error: %@"
+ "Dropping priority assertion, requested = %@"
+ "EID"
+ "EXTERNAL_DISPLAY_BANNER_TITLE"
+ "EXTERNAL_DISPLAY_EXTENDING_IPAD_DISPLAY"
+ "EXTERNAL_DISPLAY_SCREEN_MIRRORING_ON"
+ "Element '%@' is required priority while '%@' is not"
+ "Forcing System Aperture visible in order to display securely rendered element"
+ "IMEI%ld"
+ "IMEI2"
+ "IdleTimerDisableChangedForSceneManager - client:"
+ "Ignoring request to collapse SystemAperture to default layout due to element required secure visibility: (%{public}@-%{public}@)"
+ "Initial Scale For Split View Handles"
+ "Invalidating SS, reason: %{public}@"
+ "Invalidating required priority assertion (%{public}@) with reason '%{public}@' for element: %{public}@"
+ "Lock ELement no longer in secure state"
+ "Lock Element Secure State"
+ "Maximum Home Screen Dimming Alpha Response"
+ "Maximum Home Screen Dimming Alpha When Not Full Screen"
+ "Minimum Home Screen Dimming Alpha Response"
+ "No SS disable assertion found, reason: %{public}@"
+ "Percentage of Transition Layout Settling Duration for Split View Handle Fade-In Delay"
+ "Prevent PIP Under CC"
+ "Prioritizing '%{public}@' since it prefers visibility"
+ "Q\xc1\xf0!"
+ "REGIONALLY_RESTRICTION_BROWSER_ENGINE_BODY"
+ "REGIONALLY_RESTRICTION_EMBEDDED_BROWSER_ENGINE_BODY"
+ "Re-enabling SS gesture recognizer - no assertions"
+ "SBDisplayItemLayoutAttributesDebugView"
+ "SBDisplayItemLayoutAttributesProvider"
+ "SBDisplayItemLayoutAttributesProvider.m"
+ "SBDisplayItemLayoutAttributesProviderDelegate"
+ "SBDockToStageZoomWindowingModifier.m"
+ "SBFlexibleWindowingArcSwipeTimerReason"
+ "SBFluidSwitcherGestureWorkspaceTransactionCompletionDeferralReasonAwaitingGestureCancellation"
+ "SBHTraitIconPresentationStyle"
+ "SBIconVisibilityAppLibraryOnly"
+ "SBInteractiveScreenshotGestureRoundedCropsView"
+ "SBPeekConfigurationIsValid(configuration)"
+ "SBRestoreDesktopSpaceWindowingModifier"
+ "SBSAElementRemovalTransitionProvider"
+ "SBSAElementRemovalTransitionProvider.m"
+ "SBSALayoutModeSupportingProvider.m"
+ "SBSplitViewHandleDimmingView"
+ "SBSplitViewHandleNubView"
+ "SBSwitcherSplitViewHandleDimmingElement"
+ "SBSwitcherSplitViewHandleDimmingElement.m"
+ "SBSwitcherSplitViewHandleNubElement"
+ "SBSwitcherSplitViewHandleNubElement.m"
+ "SBSystemShellExternalDisplaySceneManager requested idle timer behavior disabled? %{BOOL}u%s%{public}@"
+ "SB_ICON_FLY_IN_ANIMATION"
+ "SB_ICON_FLY_IN_ANIMATION_CLEAN_UP"
+ "SB_ICON_FLY_IN_ANIMATION_LIFECYCLE"
+ "SB_ICON_FLY_IN_ANIMATION_PREPARATION"
+ "SN"
+ "SS assertion invalidated, reason: %{public}@"
+ "SS gesture already disabled, reason: %{public}@"
+ "SS gesture assertion invalidated but strongSelf is nil, reason: %{public}@"
+ "SS gesture still disabled - current assertions: %{public}@"
+ "SS is suppressed"
+ "Scene Element Secure State"
+ "Scene Element no longer Secure State"
+ "Setting SS disabled: %{BOOL}u, reason: %{public}@, current assertions: %{public}@"
+ "SplitViewDimming"
+ "SpringBoard - SBSystemShellExternalDisplaySceneManager"
+ "T@\"<BSInvalidatable>\",&,N,V_guidedAccessSystemGestureDisableAssertion"
+ "T@\"<SAInvalidatable>\",&,N,V_requiredPriorityAssertion"
+ "T@\"<SAInvalidatable>\",R,W,N,V_requiredPriorityAssertion"
+ "T@\"<SBDisplayItemLayoutAttributesProviderDelegate>\",W,N,V_delegate"
+ "T@\"BPSPublisher\",&,N,V_appearancePublisher"
+ "T@\"LSSAssertion\",R,N,V_criticalThermalLevelDynamicLightingAssertion"
+ "T@\"NSArray\",C,N,V_customConstraints"
+ "T@\"NSCountedSet\",&,N,V_completionDeferralReasons"
+ "T@\"NSDate\",&,N,V_lastAppearanceTimestamp"
+ "T@\"NSMutableDictionary\",&,N,V_visibleSplitViewHandleDimmingViews"
+ "T@\"NSMutableDictionary\",&,N,V_visibleSplitViewHandleNubViews"
+ "T@\"NSMutableSet\",&,N,V_visibleSplitViewHandleDimmingViewsWaitingForFadeIn"
+ "T@\"NSMutableSet\",&,N,V_visibleSplitViewHandleNubViewsWaitingForFadeIn"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_appearanceQueue"
+ "T@\"NSSet\",&,N,V_previousDesktopItems"
+ "T@\"NSSet\",?,R,N"
+ "T@\"SBAppLayout\",&,N,V_ignoredAppLayout"
+ "T@\"SBAppLayout\",&,N,V_launchingOverDesktopSpaceAppLayout"
+ "T@\"SBAppLayout\",R,N,V_organicExposeAppLayout"
+ "T@\"SBDisplayItem\",&,N,V_minimizingDisplayItem"
+ "T@\"SBDisplayItemLayoutAttributes\",W,N,V_layoutAttributes"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_splitViewHandleFadeInSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_splitViewHandleFadeOutSettings"
+ "T@\"UIAction\",&,N,V_leftArrowNavigationAction"
+ "T@\"UIAction\",&,N,V_rightArrowNavigationAction"
+ "T@\"UIView\",R,N,V_nubContainerView"
+ "T@\"_UIPortalView\",&,N,V_searchAffordancePortalView"
+ "TB,N,GisDismissingMenuForPointerHover,V_dismissingMenuForPointerHover"
+ "TB,N,SsetEmpty:,V_isEmpty"
+ "TB,N,V_presentingMenuForIndirectInput"
+ "TB,N,V_shouldDismissForWorkspaceTransitions"
+ "TB,R,N,GisAppLibraryOnlyByDefault,V_appLibraryOnlyByDefault"
+ "TB,R,N,V_avoidOverridingAppFocusOnOtherDisplays"
+ "TB,V_isObserving"
+ "TLAlertPlaybackObserver"
+ "Taking priority assertion, requested = %@"
+ "Td,N,V_occupiedAreaPercentage"
+ "Td,N,V_splitViewHandleDimmingWidth"
+ "Td,N,V_splitViewHandleNubWidth"
+ "Td,R,N,V_intersectionHeight"
+ "Td,V_initialScaleForSplitViewHandles"
+ "Td,V_maxHomeScreenDimmingAlphaForNonFullscreen"
+ "Td,V_maxHomeScreenDimmingAlphaResponse"
+ "Td,V_minHomeScreenDimmingAlphaResponse"
+ "Td,V_percentageOfTransitionForSplitViewHandleFadeInDelay"
+ "There are no more pending dismissal identifiers, but the provider has not transitioned to disappeared."
+ "There is another element content provider that this provider didn't know about. %@; other: %@; ours: %@"
+ "There is still an element content provider in the stack?"
+ "Thermal state is %{public}@, releasing assertion to disable dynamic lighting output"
+ "Thermal state is critical, acquiring assertion to disable dynamic lighting output"
+ "Timer Expired"
+ "T{SBIconImageInfo={CGSize=dd}dd},N,V_iconImageInfo"
+ "UserInterfaceStyleBoth"
+ "UserInterfaceStyleCurrent"
+ "Using %s mode for snapshots"
+ "[%{public}lu] Cleaning up ContainerDisappearanceTransitionProvider for change to layoutMode: %@; %@"
+ "[%{public}lu] Did reach collision threshold or steady state: %{BOOL}u or all containers finished animating: %{BOOL}u. Removing the disappearing element content provider: %@"
+ "[%{public}lu] This provider has already transitioned to a disappeared state, but there is an unexpected element content provider in the stack: %@"
+ "[ActivityID: %{public}@] Could not dismiss alert because it is not active"
+ "[ActivityID: %{public}@] did finish presenting modal full screen alert"
+ "_SBAppLayoutsArray"
+ "_adjustMobileEquipmentLayout:"
+ "_alert:didBeginPlayingWithEvent:"
+ "_appLibraryOnlyByDefault"
+ "_appearancePublisher"
+ "_appearanceQueue"
+ "_appendPropertiesToBuilder:"
+ "_avoidOverridingAppFocusOnOtherDisplays"
+ "_backing"
+ "_beginAnimatingExposeMultitaskingPropertyWithMode:settings:"
+ "_beginDeferringCompletionForReason:"
+ "_borderViewMask"
+ "_canEnterExposeMultitasking"
+ "_cascaded"
+ "_clusterForExposeWithRects:count:stage:padding:screenScale:fullScreenRectsIfAny:"
+ "_completionDeferralReasons"
+ "_contentScaleForCommitProgress:contentInsets:additionalContentTranslation:"
+ "_criticalThermalLevelDynamicLightingAssertion"
+ "_customConstraints"
+ "_defaultSiriWorkspaceTransitionOptions"
+ "_desktopSpaceAppLayout"
+ "_didDisappear"
+ "_didSetCompositingFilter"
+ "_didSetCornerAlpha"
+ "_didSetCornerColor"
+ "_didSetGrabberLineWidth"
+ "_dismissAlertForItem:"
+ "_dismissMenuBarWithCompletion:"
+ "_dismissingMenuForPointerHover"
+ "_doesElementHaveValidRequiredPriorityAssertion:"
+ "_effectiveStageAreaForSnappingForSpace:configuration:"
+ "_eid"
+ "_elementContentProvider"
+ "_elementRemovalTransitionProvider"
+ "_endDeferringCompletionForReason:"
+ "_ensureSearchAffordanceIsInstalledInView:"
+ "_firstElementLayoutModeSupportingProvider"
+ "_flexibleAutoLayoutSpaceForZoomingAppLayout"
+ "_forcePeekingTrailingEdge"
+ "_fromHomePeekModifier"
+ "_guidedAccessSystemGestureDisableAssertion"
+ "_handleContentSizeCategoryDidChange:"
+ "_handleGuidedAccessActivationChanged:"
+ "_handleRealTimeAppearanceChange:"
+ "_hasUpdatedForcePeekingEdge"
+ "_hideSplitViewHandles"
+ "_homeScreenDimmingAlpha"
+ "_iconImageInfo"
+ "_ignoredAppLayout"
+ "_inExposeMultitasking"
+ "_inExposeMultitaskingChangedProperty"
+ "_initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:"
+ "_initialScaleForSplitViewHandles"
+ "_intersectionHeight"
+ "_isCreatingFullScreenOverlay"
+ "_isDeferringCompletionForAnyReason"
+ "_isDeferringCompletionForReason:"
+ "_isDisplayingAnyRequiredSecureContent"
+ "_isFloatingDockFullyPresented"
+ "_isMenuBarGenerallyDisabled"
+ "_isMinimizing"
+ "_isObserving"
+ "_isTouchLocationInSplitViewGutter:"
+ "_keyboardFrameInMainScreenFromNotifications"
+ "_lastAppearanceTimestamp"
+ "_launchingOverDesktopSpaceAppLayout"
+ "_layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:"
+ "_layoutRestrictionInfoForSelectedItem"
+ "_leftArrowNavigationAction"
+ "_loadLastAppearanceChangeWithCompletion:"
+ "_maxHomeScreenDimmingAlphaForNonFullscreen"
+ "_maxHomeScreenDimmingAlphaResponse"
+ "_maxScreenSizeWithDockAndStripInset"
+ "_menuBarTitleFontFromStatusBarFont:"
+ "_minHomeScreenDimmingAlphaResponse"
+ "_minimizingDisplayItem"
+ "_modernScenesPendingActivation"
+ "_navigateToNextMenuHeaderForArrowKeyPress:"
+ "_noteAppLayoutMovedToFront:"
+ "_nubContainerView"
+ "_numberOfPeekingItemsAboveDisplayItem:zOrderedItems:"
+ "_occupiedAreaPercentage"
+ "_pendingDismissalTransitionIdentifiers"
+ "_percentageOfTransitionForSplitViewHandleFadeInDelay"
+ "_prefersStripHiddenAndDisabled"
+ "_presentMenuViewNonInteractively:"
+ "_presentingMenuForIndirectInput"
+ "_preventPIPFromStartingUnderControllerCenterCompoundAssertion"
+ "_preventVideoCallPIPFromAppearingBelowControlCenterAssertion"
+ "_previousDesktopItems"
+ "_previousDesktopSpaceItems"
+ "_processMobileEquipmentInfo:forSlot:"
+ "_queue_contentCornerRadius"
+ "_reasonsToRequiredPriorityAssertions"
+ "_reentrantGuard_inNoteAppLayoutMovedToFront"
+ "_registeredContainerDismissalInterfacePropertyIdentifiers"
+ "_requiredPriorityAssertion"
+ "_requiredPriorityAssertionWithReason:creatingIfNecessary:"
+ "_restoreDesktopSpaceAfterClosingFullScreenSpace"
+ "_rightArrowNavigationAction"
+ "_safeAreaCornerInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:"
+ "_searchAffordancePortalView"
+ "_secureDisplayRequired"
+ "_selectedItemWasInitiallyFullscreen"
+ "_setupUI"
+ "_shouldComplete"
+ "_shouldDismissForWorkspaceTransitions"
+ "_shouldGroupIMEIsForPrimary:secondary:"
+ "_shouldUpdateForDisplayOrdinal:"
+ "_siriWorkspaceTransitionOptionsFromOpenApplicationOptions:"
+ "_slidingOffPeekingAppLayout"
+ "_splitViewHandleDimmingWidth"
+ "_splitViewHandleFadeInSettings"
+ "_splitViewHandleFadeOutSettings"
+ "_splitViewHandleNubViewsToHitTestRects"
+ "_splitViewHandleNubWidth"
+ "_stopObservingAppearanceChanges"
+ "_stripWasInitiallyPresented"
+ "_subscribeToAppearanceChanges"
+ "_toFullScreen"
+ "_underlyingUpdateQueue"
+ "_uniqueTimerReason"
+ "_updateBorderViewMaskWithRect:"
+ "_updateForcePeekingEdgeIfNeeded"
+ "_updateIconViewImageForSuggestion:"
+ "_updateLastAppearanceTimestamp:"
+ "_updateOccupiedAreaForSpace:configuration:"
+ "_updateRequiredPriorityAssertion"
+ "_updateUI"
+ "_updateVisibleSplitViewHandleDimmingViews"
+ "_updateVisibleSplitViewHandleNubViews"
+ "_updatesHomeScreenForAccessoryWithType:"
+ "_visibleSplitViewHandleDimmingViews"
+ "_visibleSplitViewHandleDimmingViewsWaitingForFadeIn"
+ "_visibleSplitViewHandleNubViews"
+ "_visibleSplitViewHandleNubViewsWaitingForFadeIn"
+ "_windowManagementContextIsSingleAppModeForSwitcherCorrespondingToDisplayOrdinal:"
+ "a!\xa1"
+ "acquireAssertionToPreventVideoCallPIPFromStartingUnderControlCenter:"
+ "additionalKeyboardShortcutActionsForSession"
+ "alert:didBeginPlayingWithEvent:"
+ "alertDidBeginPlaying:"
+ "appLibraryOnlyByDefault"
+ "appSwitcherModel:didMoveAppLayoutToFront:"
+ "appearancePublisher"
+ "appearanceQueue"
+ "audioSessionReporterID"
+ "avoidOverridingAppFocusOnOtherDisplays"
+ "browserEngineIsRegionallyRestricted"
+ "cascaded"
+ "com.apple.SpringBoardFramework.SBDynamicLightingController.underlyingUpdateQueue"
+ "com.example.SBPhoneSceneSnapshotRequestStrategy.appearance"
+ "completionDeferralReasons"
+ "configureFileStackIcon:url:sortingBy:sortingOrderAscending:displayMode:anchorFrame:floatingDockFrame:sourceLayerRenderId:sourceContextId:openIndicatorLayerRenderId:openIndicatorContextId:iconImageInfoSize:iconImageInfoScale:iconImageContinuousCornerRadius:requestFromHost:fence:"
+ "coverSheetViewController:didChangeHasContentAbove:"
+ "coverSheetViewController:didObscureWallpaper:"
+ "coverSheetViewController:didOccludeWallpaper:"
+ "criticalThermalLevelDynamicLightingAssertion"
+ "customConstraints"
+ "darkTextColor"
+ "didChangeThermalLevel:"
+ "didUpdateAudioReporterId:"
+ "didn't find an SBSplitViewHandleNubView at location %@"
+ "dismissingMenuForPointerHover"
+ "effectiveStatusBarStyleRequestForActivationSettings:"
+ "embeddedBrowserEngineIsRegionallyRestricted"
+ "exportedOSMigrationDefaultHomeScreenLayout"
+ "fadeInDelayForSplitViewHandles"
+ "frameForSplitViewHandleDimmingView:"
+ "frameForSplitViewHandleNubView:"
+ "guidedAccessSystemGestureDisableAssertion"
+ "handleFloatingDockFrameDidChange:"
+ "hitTestedToSplitViewHandle:window:"
+ "iconManager:shouldPreviewOverlapMenuForIconView:"
+ "ignoredAppLayout"
+ "inExposeMultitasking"
+ "inExposeMultitaskingChangedProperty"
+ "inExposeMultitaskingChangedProperty.presentationValue"
+ "initWithAppLayout:addingToStage:"
+ "initWithFrame:systemPointerInteractionManager:"
+ "initWithFromAppLayout:fromConfiguration:"
+ "initWithItem:frame:corners:shadow:titleStyle:opacity:wallpaperGradientAttributes:perspectiveAngle:dimmingAlpha:animationAttributes:supportsHomeAffordance:spaceAccessoryViewModel:personalityDebugColorStyle:"
+ "initWithPeekingAppLayout:configuration:"
+ "initWithStartDate:endDate:maxEvents:lastN:reversed:"
+ "initWithTransitionModifier:slidingOffPeekingAppLayout:fromPeekingConfiguration:"
+ "initialScaleForSplitViewHandles"
+ "intersectionHeight"
+ "isAppLibraryOnlyByDefault"
+ "isDismissingMenuForPointerHover"
+ "isDownloading"
+ "isKillableInSwitcher"
+ "isObserving"
+ "isSceneHandleKillableInSwitcher:"
+ "isStatusBarHiddenForActivationSettings:withOrientation:"
+ "lastAppearanceTimestamp"
+ "lastIndex"
+ "lastLayoutUnarchivedIdentifiers"
+ "lastMultitaskingModeSwitchDate"
+ "launchingOverDesktopSpaceAppLayout"
+ "leftArrowNavigationAction"
+ "lsApplicationRecord"
+ "maxHomeScreenDimmingAlphaForNonFullscreen"
+ "maxHomeScreenDimmingAlphaResponse"
+ "menu bar disabled for guided access"
+ "microphoneRecordingAttribution"
+ "minHomeScreenDimmingAlphaResponse"
+ "minimizingDisplayItem"
+ "mutedMicrophoneRecordingActivityAttribution"
+ "mutedMicrophoneSensorActivityData"
+ "nubContainerView"
+ "occupiedAreaPercentage"
+ "openApplicationMenu"
+ "organicExposeAppLayout"
+ "osMigrationDefaultHomeScreenLayout"
+ "osMigrationHomeScreenLayoutForRootFolder:"
+ "percentageOfTransitionForSplitViewHandleFadeInDelay"
+ "prepareToPresentMenuForIndirectInput"
+ "presentingMenuForIndirectInput"
+ "previousDesktopItems"
+ "publisherWithUseCase:options:"
+ "recentAppLayouts:didMoveAppLayoutToFront:"
+ "requestRequiredPriorityAssertionWithReason:"
+ "requiredPriorityAssertion"
+ "rightArrowNavigationAction"
+ "safeAreaEdgeInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:"
+ "searchAffordancePortalView"
+ "setAppearancePublisher:"
+ "setAppearanceQueue:"
+ "setArray:"
+ "setCompletionDeferralReasons:"
+ "setCustomConstraints:"
+ "setDismissingMenuForPointerHover:"
+ "setEmpty should be changed when SBLockElementViewProvider is not registered with Jindo"
+ "setGuidedAccessSystemGestureDisableAssertion:"
+ "setHomeScreenDimmingAlpha:settings:behaviorMode:completion:"
+ "setIgnoredAppLayout:"
+ "setInitialScaleForSplitViewHandles:"
+ "setIsObserving:"
+ "setLastAppearanceTimestamp:"
+ "setLastMultitaskingModeSwitchDate:"
+ "setLaunchingOverDesktopSpaceAppLayout:"
+ "setLayoutAttributes:"
+ "setLeftArrowNavigationAction:"
+ "setMaxHomeScreenDimmingAlphaForNonFullscreen:"
+ "setMaxHomeScreenDimmingAlphaResponse:"
+ "setMinHomeScreenDimmingAlphaResponse:"
+ "setMinimizingDisplayItem:"
+ "setOccupiedAreaPercentage:"
+ "setPercentageOfTransitionForSplitViewHandleFadeInDelay:"
+ "setPlaybackObserver:"
+ "setPreferredMaximumMenuHeight:"
+ "setPresentingMenuForIndirectInput:"
+ "setPreviousDesktopItems:"
+ "setRequiredPriorityAssertion:"
+ "setRightArrowNavigationAction:"
+ "setSearchAffordancePortalView:"
+ "setShouldDismissForWorkspaceTransitions:"
+ "setSplitViewHandleDimmingWidth:"
+ "setSplitViewHandleFadeInSettings:"
+ "setSplitViewHandleFadeOutSettings:"
+ "setSplitViewHandleNubWidth:"
+ "setUnderlyingQueue:"
+ "setVisibleSplitViewHandleDimmingViews:"
+ "setVisibleSplitViewHandleDimmingViewsWaitingForFadeIn:"
+ "setVisibleSplitViewHandleNubViews:"
+ "setVisibleSplitViewHandleNubViewsWaitingForFadeIn:"
+ "shouldDismissForWorkspaceTransitions"
+ "shouldForceFullscreenForDisplayOrdinal:"
+ "shouldPreviewOverlapMenuForIconView:"
+ "shouldUpdateLayoutAttributesForDisplayOrdinal:"
+ "sinkWithCompletion:shouldContinue:"
+ "siriPresentation:didUpdateShouldDismissForWorkspaceTransitions:"
+ "splitViewHandleDimmingWidth"
+ "splitViewHandleFadeInSettings"
+ "splitViewHandleFadeOutSettings"
+ "splitViewHandleNubWidth"
+ "switcherContentController:setHomeScreenDimmingAlpha:withSettings:animationMode:completion:"
+ "systemApertureApertureElementAuthority:isElementPreferringToRemainVisible:"
+ "systemApertureApertureElementAuthority:isElementRequiredPriority:"
+ "systemApertureViewController:isDisplayingAnyRequiredSecureElements:"
+ "toggleMenuBarVisibilityForSystemKeyboardShortcut"
+ "topMostItemsByAddingAppLayoutAndAccessories:toTopMostItems:orderFront:"
+ "topMostLayoutElementsByAddingAppLayoutAndAccessories:toTopMostLayoutElements:orderFront:"
+ "unarchiveRootFolderFromArchive:withIconSource:"
+ "underlyingQueue"
+ "userDidClickInApp"
+ "v24@0:8@\"TLAlert\"16"
+ "v24@?0@\"SBSwitcherSplitViewHandleDimmingElement\"8^B16"
+ "v24@?0@\"SBSwitcherSplitViewHandleNubElement\"8^B16"
+ "v32@0:8@\"TLAlert\"16@\"TLAlertPlaybackBeginEvent\"24"
+ "v32@?0@\"SBSwitcherSplitViewHandleDimmingElement\"8@\"SBSplitViewHandleDimmingView\"16^B24"
+ "v32@?0@\"SBSwitcherSplitViewHandleNubElement\"8@\"SBSplitViewHandleNubView\"16^B24"
+ "v48@0:8d16@\"SBFFluidBehaviorSettings\"24q32@?<v@?BB>40"
+ "v48@0:8d16@24q32@?40"
+ "v48@0:8{SBIconImageInfo={CGSize=dd}dd}16"
+ "v56@0:8@\"<SBSwitcherContentViewControlling>\"16d24@\"SBFFluidBehaviorSettings\"32q40@?<v@?BB>48"
+ "v56@0:8@16d24@32q40@?48"
+ "v96@0:8^{CGRect={CGPoint=dd}{CGSize=dd}}16q24{CGRect={CGPoint=dd}{CGSize=dd}}32{CGSize=dd}64d80^B88"
+ "visibleInputViewFrame"
+ "visibleSplitViewHandleDimmingViews"
+ "visibleSplitViewHandleDimmingViewsWaitingForFadeIn"
+ "visibleSplitViewHandleNubViews"
+ "visibleSplitViewHandleNubViewsWaitingForFadeIn"
+ "wantsDisableIdleTimer"
+ "windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:"
+ "{?=\"switcherContentControllerBringAppLayoutToFront\"b1\"switcherContentControllerActivatedBestAppSuggestion\"b1\"updateUserInteractionEnabledForSwitcherContentController\"b1\"updateWindowVisibilityForSwitcherContentController\"b1\"switcherContentControllerSetHomeScreenScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenAlphaWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenDimmingAlphaWithSettingsAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurProgressWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurType\"b1\"switcherContentControllerSetHomeScreenBackdropBlurMaterialRecipeNameWithAnimationModeCompletion\"b1\"switcherContentControllerControlsWallpaper\"b1\"switcherContentControllerSetWallpaperScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetWallpaperStyle\"b1\"switcherContentControllerSetInterfaceOrientation\"b1\"switcherContentControllerSetInterfaceOrientationFromUserResizingForDisplayItem\"b1\"switcherContentControllerRequestNewWindowForBundleIdentifier\"b1\"switcherContentControllerSetContainerStatusBarHiddenPartsHiddenAnimationDuration\"b1\"switcherContentControllerWantsToDismissMenuBar\"b1\"switcherContentControllerWantsToPeekMenuBar\"b1\"switcherContentControllerDemoLayoutAttributesForDisplayItem\"b1\"switcherContentControllerSetPointerInteractionsEnabled\"b1\"switcherContentControllerShouldResignActiveForStartOfTransition\"b1\"switcherContentControllerControlsHomeScreenContents\"b1\"switcherContentControllerSetCacheAsynchronousRenderingSurfaces\"b1\"cancelActiveGestureForSwitcherContentController\"b1\"switcherContentControllerReopenHiddenAppLayoutsWithBundleIdentifier\"b1\"switcherContentControllerLayoutStateTransitionDidEndWithTransitionContext\"b1\"switcherContentControllerTransformForCardUnderSheetForBoundsSize\"b1\"switcherContentControllerMoveDisplayItemFromOtherDisplay\"b1\"presentContinuousExposeStripRevealGrabberTongueImmediatelyForSwitcherContentController\"b1\"tickleContinuousExposeStripRevealGrabberTongueIfVisibleForSwitcherContentController\"b1\"switcherContentControllerDidUpdateVisibleHomeAffordances\"b1\"switcherContentControllerRemoveDisplayItemFromDesktop\"b1\"switcherContentControllerRequestDismissalForHomeScreenBackgroundTaps\"b1}"
+ "{CGPoint=dd}72@0:8d16{UIEdgeInsets=dddd}24{CGPoint=dd}56"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@\"SBSwitcherSplitViewHandleDimmingElement\"16"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@\"SBSwitcherSplitViewHandleNubElement\"16"
+ "{SBIconImageInfo=\"size\"{CGSize=\"width\"d\"height\"d}\"scale\"d\"continuousCornerRadius\"d}"
+ "{SBIconImageInfo={CGSize=dd}dd}16@0:8"
+ "{SBWindowControlsLayout=qB{CGPoint=dd}}96@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48@80q88"
+ "{UIEdgeInsets=dddd}96@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48@80q88"
+ "{_UICornerInsets={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}}96@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48@80q88"
+ "\xf0q!"
+ "\xf0\xf0\""
+ "\xf0\xf0\xb1"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x92\xf0\xf01"
- "$C"
- "%@-%@-%ld"
- "%{public}@ _isHardwareAvailableDuringDisplayConnectionWindow: %{bool}u"
- "%{public}@ client connected "
- "%{public}@ client connected but our display is already gone. we're talking to a ghost."
- "%{public}@ counting as not satisfied alert"
- "%{public}@ counting as satisfied alert"
- "%{public}@ creating session with previous reasons: %{public}@"
- "%{public}@ device connection window expired"
- "%{public}@ dismissing alert for reason: %{public}@; via: alertHandle (%{public}@)"
- "%{public}@ dismissing alert for reason: %{public}@; via: xpcConnection (%{public}@)"
- "%{public}@ display connected"
- "%{public}@ hardwareReqs are not satisfied. have presented unsatisfied alert before. rolling banner now. previousReasons: %{public}@"
- "%{public}@ hardwareReqs are not satisfied. haven't presented unsatisfied alert before. presenting now. previousReasons: %{public}@"
- "%{public}@ hardwareReqs are satisfied. have presented satisfied alert before. rolling banner now. previousReasons: %{public}@"
- "%{public}@ hardwareReqs are satisfied. haven't presented satisfied alert before. presenting now. previousReasons: %{public}@"
- "%{public}@ have presented both alerts before. rolling banner now. previousReasons: %{public}@"
- "%{public}@ not counting as no user response"
- "%{public}@ received error back from education service: %{public}@"
- "%{public}@ received response from user. externalDisplayEnabled: %{bool}u"
- "%{public}@ telling remoteObject %{public}@; hardwareAvailable: %{bool}u; during window: %{bool}u"
- "%{public}@ we've not presented either alert before. presenting now. previousReasons: %{public}@"
- "-[SBDisplayItemLayoutAttibutesProvider layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:]"
- "-[SBDisplayItemLayoutAttibutesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]"
- "-[SBWindowScenePIPManager _adjustPIPInsetsForKeyboardFrameChangeNotification:]"
- "-[SBWindowScenePIPManager _keyboardWillChangeFrame:]"
- "-[SBWindowScenePIPManager _keyboardWillShowOrHide:]"
- "@\"SBArcSwipeCoplanarSessionWindowingModifier\""
- "@\"SBFlexibleWindowingHomeGestureSwitcherModifier\""
- "@228@0:8q16q24q32{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}40{SBDisplayItemTileConfiguration=q{CGSize=dd}}96{CGPoint=dd}120q136{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}144{CGPoint=dd}200B216q220"
- "@308@0:8@16{SBWindowingItemFrame={CGRect={CGPoint=dd}{CGSize=dd}}{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}}24{SBWindowingItemCorners={UIRectCornerRadii=dddd}Q}120{SBWindowingItemShadow=dq}160{SBWindowingItemResizeGrabber=Qd}176{SBWindowingItemTitleStyle=dddqQ}192d232{SBSwitcherWallpaperGradientAttributes=dd}240{CGPoint=dd}256d272@280B288@292Q300"
- "CurrentLayoutStateBySwipeUpAndPauseWhileInHomePeek"
- "EID:"
- "ICCID:"
- "IMEI:"
- "IdleTimerDisableChangedForMainDisplaySceneManager - client:"
- "Large"
- "MEID:"
- "PLKBackdropAwareTrait"
- "PRIMARY"
- "Prioritizing '%{public}@' since it requires visibility"
- "Q\xc1\xd1"
- "REGIONALLY_RESTRICTION_BODY"
- "SBArcSwipeCoplanarSessionWindowingModifier"
- "SBDisplayItemLayoutAttibutesProvider"
- "SBDisplayItemLayoutAttibutesProvider.m"
- "SBERemoteViewController"
- "SBExternalDisplayHardwareRequirementsChangedProtocol"
- "SBRemoteHandshakeProtocol"
- "SECONDARY"
- "SN:"
- "STAGE_MANAGER_EXTENDED_DISPLAY"
- "STAGE_MANAGER_EXTENDED_DISPLAY_OFF"
- "STAGE_MANAGER_EXTENDED_DISPLAY_ON"
- "SpringBoardAppIconiPad"
- "TB,N,V_presentingMenuForPointerHover"
- "TB,R,N,V_supportsSolarium"
- "TQ,R,N,V_resizeGrabberEdge"
- "Td,N,V_resizeGrabberCenterY"
- "Td,N,V_resizeGrabberWidth"
- "T{SBWindowingItemResizeGrabber=Qd},D,N"
- "T{SBWindowingItemResizeGrabber=Qd},N,V_resizeGrabber"
- "T{SBWindowingItemResizeGrabber=Qd},R,N"
- "[%{public}lu] No elements –\u00a0removing all transition and element providers"
- "_alertHandle"
- "_assumingKeyboardIsVisible"
- "_cached_autoLayoutSpaceWithDraggedItemExcluded"
- "_clusterForExposeWithRects:count:stage:padding:screenScale:"
- "_createSearchAffordanceReferenceBackgroundFadeProperty"
- "_currentDisplayItemIndex"
- "_currentGestureIdentifier"
- "_deviceConnectionWindowExpired:"
- "_dismissEducationAlert:"
- "_edgeOfDisplayItem:"
- "_effectiveCurrentAppLayout"
- "_endpoint"
- "_extendedDisplayEnabled"
- "_flexibleHomeGestureIsShowingMultitasking"
- "_flexibleHomeGestureModifier"
- "_frameOffsetForActiveCard"
- "_frameOffsetForAdjacentCards"
- "_generateImageWithInfo:traitCollection:options:"
- "_gestureCount"
- "_hasLatchedOverflowPeekingOffset"
- "_initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:"
- "_layoutResizeGrabber"
- "_layoutSettingsForLayoutRole:inAppLayout:layoutSettings:"
- "_loadIconForDisplayItem:"
- "_mobileSubscriptionInfo"
- "_nextDisplayItem"
- "_nextFullScreenAppLayout"
- "_nextFullScreenDisplayItem"
- "_orderedVisitedDisplayItems"
- "_overflowPeekingOffset"
- "_pendingComplete"
- "_postGestureTransitionDelay"
- "_presentEducationAlert:"
- "_presentingMenuForPointerHover"
- "_previousDisplayItem"
- "_previousFullScreenAppLayout"
- "_previousFullScreenDisplayItem"
- "_previousPresentedReasons"
- "_processMobileEquipmentInfo:"
- "_processMobileSubscriptionInfo"
- "_queue_displayCornerRadius"
- "_resizeGrabberCenterY"
- "_resizeGrabberEdge"
- "_resizeGrabberViewsToHitTestRects"
- "_resizeGrabberWidth"
- "_safeAreaCornerInsetsForApplicationFrame:screenBounds:interfaceOrientation:"
- "_shouldUpdateLayoutAfterSettling"
- "_supportsSolarium"
- "_teardownResizeGrabberIfNeeded"
- "_titleForHeaderInSection:"
- "_trailingDisplayItems"
- "_xpcConnection"
- "a1q"
- "activeTextEffectsWindowForWindowScene:"
- "anonymousListener"
- "audioRecordingActivityAttribution"
- "being told device connection window expired when we're not tracking a session for that display: %@"
- "bottomPaddingToKeyboard"
- "com.apple.SpringBoardEducation"
- "configureFileStackIcon:url:sortingBy:sortingOrderAscending:displayMode:anchorFrame:floatingDockFrame:sourceLayerRenderId:sourceContextId:openIndicatorLayerRenderId:openIndicatorContextId:requestFromHost:fence:"
- "coverSheetViewControllerDidObscureWallpaper:obscured:"
- "coverSheetViewControllerDidOccludeWallpaper:occluded:"
- "deviceConnectionWindowExpired"
- "displayport"
- "effectiveStatusBarStyleRequestForActivation:"
- "externalDisplayEducationReasons"
- "externalDisplayHardwareRequirementsSatisfiedChanged:"
- "hitTestedToResizeGrabber:window:ofItemContainer:"
- "initWithExtendedDisplayEnabled:"
- "initWithFrame:backgroundView:"
- "initWithFromAppLayout:"
- "initWithItem:frame:corners:shadow:resizeGrabber:titleStyle:opacity:wallpaperGradientAttributes:perspectiveAngle:dimmingAlpha:animationAttributes:supportsHomeAffordance:spaceAccessoryViewModel:personalityDebugColorStyle:"
- "initWithPeekingAppLayout:"
- "initWithTransitionID:fromAppLayout:toAppLayout:selectedAppLayout:selectedDisplayItem:"
- "initWithTransitionModifier:"
- "insets: %s %{public}@ newFrame: %@ intersectionWithContainer: %{public}@"
- "insets: %s ignoring %{public}@"
- "isRegionallyRestricted"
- "isShowingMultitasking"
- "isStatusBarHiddenForActivation:forOrientation:"
- "makeSearchAffordanceBackgroundCapturingView"
- "menuState"
- "prepareToPresentMenuForPointerHover"
- "presentingMenuForPointerHover"
- "resizeGrabber"
- "resizeGrabberCenterY"
- "resizeGrabberEdge"
- "resizeGrabberForItem:"
- "resizeGrabberWidth"
- "safeAreaEdgeInsetsForApplicationFrame:screenBounds:interfaceOrientation:"
- "setExternalDisplayEducationReasons:"
- "setHomeScreenDimmingAlpha:behaviorMode:completion:"
- "setInitialMenuStateIdentifier:"
- "setPrefersEmbeddedDisplayPresentation:"
- "setPresentingMenuForPointerHover:"
- "setResizeGrabber:"
- "setResizeGrabberCenterY:"
- "setResizeGrabberEdge:systemPointerInteractionManager:"
- "setResizeGrabberHitTestRect:forView:"
- "setResizeGrabberWidth:"
- "setXpcEndpoint:"
- "supportsSolarium"
- "switcherContentController:setHomeScreenDimmingAlpha:withAnimationMode:completion:"
- "systemApertureApertureElementAuthority:isElementRequiredToRemainVisible:"
- "uppercaseString"
- "v32@0:8{SBWindowingItemResizeGrabber=Qd}16"
- "v56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@\"UIView\"48"
- "v88@0:8^{CGRect={CGPoint=dd}{CGSize=dd}}16q24{CGRect={CGPoint=dd}{CGSize=dd}}32{CGSize=dd}64d80"
- "wakeUpConnection"
- "we can only show education banner / alert once per display connection session"
- "windowControlsLayoutForApplicationFrame:screenBounds:interfaceOrientation:"
- "{%@, %@}"
- "{?=\"switcherContentControllerBringAppLayoutToFront\"b1\"switcherContentControllerActivatedBestAppSuggestion\"b1\"updateUserInteractionEnabledForSwitcherContentController\"b1\"updateWindowVisibilityForSwitcherContentController\"b1\"switcherContentControllerSetHomeScreenScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenAlphaWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenDimmingAlphaWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurProgressWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurType\"b1\"switcherContentControllerSetHomeScreenBackdropBlurMaterialRecipeNameWithAnimationModeCompletion\"b1\"switcherContentControllerControlsWallpaper\"b1\"switcherContentControllerSetWallpaperScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetWallpaperStyle\"b1\"switcherContentControllerSetInterfaceOrientation\"b1\"switcherContentControllerSetInterfaceOrientationFromUserResizingForDisplayItem\"b1\"switcherContentControllerRequestNewWindowForBundleIdentifier\"b1\"switcherContentControllerSetContainerStatusBarHiddenPartsHiddenAnimationDuration\"b1\"switcherContentControllerWantsToDismissMenuBar\"b1\"switcherContentControllerWantsToPeekMenuBar\"b1\"switcherContentControllerDemoLayoutAttributesForDisplayItem\"b1\"switcherContentControllerSetPointerInteractionsEnabled\"b1\"switcherContentControllerShouldResignActiveForStartOfTransition\"b1\"switcherContentControllerControlsHomeScreenContents\"b1\"switcherContentControllerSetCacheAsynchronousRenderingSurfaces\"b1\"cancelActiveGestureForSwitcherContentController\"b1\"switcherContentControllerReopenHiddenAppLayoutsWithBundleIdentifier\"b1\"switcherContentControllerLayoutStateTransitionDidEndWithTransitionContext\"b1\"switcherContentControllerTransformForCardUnderSheetForBoundsSize\"b1\"switcherContentControllerMoveDisplayItemFromOtherDisplay\"b1\"presentContinuousExposeStripRevealGrabberTongueImmediatelyForSwitcherContentController\"b1\"tickleContinuousExposeStripRevealGrabberTongueIfVisibleForSwitcherContentController\"b1\"switcherContentControllerDidUpdateVisibleHomeAffordances\"b1\"switcherContentControllerRemoveDisplayItemFromDesktop\"b1\"switcherContentControllerRequestDismissalForHomeScreenBackgroundTaps\"b1}"
- "{SBWindowControlsLayout=qB{CGPoint=dd}}88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80"
- "{SBWindowingItemResizeGrabber=\"edge\"Q\"centerY\"d}"
- "{SBWindowingItemResizeGrabber=Qd}16@0:8"
- "{SBWindowingItemResizeGrabber=Qd}24@0:8@\"<SBWindowingItem>\"16"
- "{SBWindowingItemResizeGrabber=Qd}24@0:8@16"
- "{SBWindowingItemResizeGrabber=Qd}24@?0@\"SBChainableModifier\"8@16"
- "{UIEdgeInsets=dddd}88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80"
- "{_UICornerInsets={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}}88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80"
- "\xf0a!"
- "\xf0\xf0\xa1"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x82\xf0\xe1"

```
