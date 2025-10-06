## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.1.8.105.0
-  __TEXT.__text: 0xa77c18
-  __TEXT.__auth_stubs: 0x5560
+4557.1.15.102.0
+  __TEXT.__text: 0xa90268
+  __TEXT.__auth_stubs: 0x5580
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb7150
-  __TEXT.__const: 0x12e50
-  __TEXT.__oslogstring: 0x5e4d4
-  __TEXT.__cstring: 0x7cce2
-  __TEXT.__gcc_except_tab: 0x17ff0
+  __TEXT.__objc_methlist: 0xb7eb8
+  __TEXT.__const: 0x12ed0
+  __TEXT.__oslogstring: 0x5e373
+  __TEXT.__cstring: 0x7d213
+  __TEXT.__gcc_except_tab: 0x198a4
   __TEXT.__ustring: 0xd0a
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2c090
+  __TEXT.__unwind_info: 0x2c558
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x21f96
-  __TEXT.__objc_methname: 0x1ce4ec
-  __TEXT.__objc_methtype: 0x4c7cf
-  __TEXT.__objc_stubs: 0xf3720
-  __DATA_CONST.__got: 0xa100
-  __DATA_CONST.__const: 0x1c928
-  __DATA_CONST.__objc_classlist: 0x51f0
+  __TEXT.__objc_classname: 0x221df
+  __TEXT.__objc_methname: 0x1d0727
+  __TEXT.__objc_methtype: 0x4ccfd
+  __TEXT.__objc_stubs: 0xf45a0
+  __DATA_CONST.__got: 0xa2f0
+  __DATA_CONST.__const: 0x1cb80
+  __DATA_CONST.__objc_classlist: 0x5268
   __DATA_CONST.__objc_catlist: 0x350
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2930
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a8a8
+  __DATA_CONST.__objc_selrefs: 0x4ad20
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3f30
-  __DATA_CONST.__objc_arraydata: 0x1878
-  __AUTH_CONST.__auth_got: 0x2ac8
-  __AUTH_CONST.__const: 0x109e8
-  __AUTH_CONST.__cfstring: 0x6ee60
-  __AUTH_CONST.__objc_const: 0x267ba0
-  __AUTH_CONST.__objc_arrayobj: 0x1788
-  __AUTH_CONST.__objc_doubleobj: 0x670
-  __AUTH_CONST.__objc_intobj: 0x2c28
+  __DATA_CONST.__objc_superrefs: 0x3fa8
+  __DATA_CONST.__objc_arraydata: 0x1888
+  __AUTH_CONST.__auth_got: 0x2ad8
+  __AUTH_CONST.__const: 0x10bf8
+  __AUTH_CONST.__cfstring: 0x6f4e0
+  __AUTH_CONST.__objc_const: 0x26a7a8
+  __AUTH_CONST.__objc_arrayobj: 0x17a0
+  __AUTH_CONST.__objc_doubleobj: 0x760
+  __AUTH_CONST.__objc_intobj: 0x2c70
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x10540
-  __DATA.__objc_ivar: 0xf20c
+  __AUTH.__objc_data: 0x106d0
+  __DATA.__objc_ivar: 0xf408
   __DATA.__data: 0x1f918
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xac0
+  __DATA.__bss: 0xab0
   __DATA.__common: 0xa40
-  __DATA_DIRTY.__objc_data: 0x22e20
+  __DATA_DIRTY.__objc_data: 0x23140
   __DATA_DIRTY.__data: 0x180
-  __DATA_DIRTY.__bss: 0x1a78
+  __DATA_DIRTY.__bss: 0x1a88
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 841F60C0-8A48-3E49-B5CB-F511B233B2C9
-  Functions: 69819
-  Symbols:   236230
-  CStrings:  104019
+  UUID: 2D7CE51C-146B-3FA3-AC83-D9057127E474
+  Functions: 70202
+  Symbols:   237446
+  CStrings:  104411
 
Symbols:
+ +[SBKeyboardFocusArbitrationReason controlCenterDidAppear]
+ +[SBKeyboardFocusArbitrationReason quickCameraDidAppear]
+ +[SBSDFElementView layerClass]
+ +[SBSDFView layerClass]
+ +[SBSwitcherCoordinatedLayoutStateTransitionContext coordinatedLayoutStateTransitionContextForMovingDisplayItems:toSwitcherController:toAppLayout:withApplicationController:].cold.1
+ +[SBSwitcherCoordinatedLayoutStateTransitionContext coordinatedLayoutStateTransitionContextForMovingDisplayItems:toSwitcherController:toAppLayout:withApplicationController:].cold.2
+ +[SBSwitcherCoordinatedLayoutStateTransitionContext coordinatedLayoutStateTransitionContextForMovingDisplayItems:toSwitcherController:toAppLayout:withApplicationController:].cold.3
+ +[SBSwitcherCoordinatedLayoutStateTransitionContext coordinatedLayoutStateTransitionContextForMovingDisplayItems:toSwitcherController:toAppLayout:withApplicationController:].cold.4
+ +[_SBSlideOverGlassMaterialBackgroundView layerClass]
+ -[SBAppSwitcherPageView _inSlideOver]
+ -[SBAppSwitcherPageView _updateSlideOverGlass]
+ -[SBAppSwitcherPageView setSlideOverBorderWidth:]
+ -[SBAppSwitcherPageView setSlideOverTonguePortalSourceView:]
+ -[SBAppSwitcherPageView slideOverBorderWidth]
+ -[SBAppSwitcherPageView slideOverTonguePortalSourceView]
+ -[SBAppSwitcherSystemService systemServiceServer:requestUpdateWindowingMode:forClient:completion:]
+ -[SBAssistantSceneController isOccludingSystemContent]
+ -[SBBannerManager _windowSceneForZStackParticipant:]
+ -[SBContinuityDisplayDelayedUIWindowSceneDelegate continuitySessionDidUpdateState:].cold.10
+ -[SBContinuitySession initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:storeDemoModeController:]
+ -[SBContinuitySession initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:storeDemoModeController:].cold.1
+ -[SBContinuitySession initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:storeDemoModeController:].cold.2
+ -[SBContinuitySession initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:storeDemoModeController:].cold.3
+ -[SBContinuitySession initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:storeDemoModeController:].cold.4
+ -[SBContinuitySession noteStoreDemoLockFailed]
+ -[SBContinuitySessionStoreDemoController .cxx_destruct]
+ -[SBContinuitySessionStoreDemoController continuitySessionDidUpdateState:]
+ -[SBContinuitySessionStoreDemoController initWithSystemEventMonitor:]
+ -[SBContinuitySessionStoreDemoController initWithSystemEventMonitor:].cold.1
+ -[SBContinuitySessionSystemEventMonitor isInStoreDemoMode]
+ -[SBContinuitySessionSystemEventMonitor isPresentingStoreDemoLoop]
+ -[SBContinuousExposeHomeGestureSwitcherModifier adjustedAppLayoutsForAppLayouts:]
+ -[SBContinuousExposeHomeGestureSwitcherModifier appLayoutToAttachSlideOverTongue]
+ -[SBContinuousExposeHomeGestureSwitcherModifier hiddenContentStatusBarPartsForLayoutRole:inAppLayout:]
+ -[SBContinuousExposeHomeGestureSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]
+ -[SBContinuousExposeRootSwitcherModifier displayItemsToExcludeFromStrip]
+ -[SBContinuousExposeRootSwitcherModifier handleSlideOverEdgeProtectTongueEvent:]
+ -[SBContinuousExposeSwitcherToAppModifier appLayoutToAttachSlideOverTongue]
+ -[SBContinuousExposeSwitcherToAppModifier transitionWillUpdate]
+ -[SBContinuousExposeWindowDragContainerSwitcherModifier slideOverTongueModifierForRoutingModifier:]
+ -[SBContinuousExposeWindowDragContentSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:wantsSlideOverTongue:slideOverTongueState:slideOverTongueDirection:]
+ -[SBContinuousExposeWindowDragContentSwitcherModifier slideOverTongueDirection]
+ -[SBContinuousExposeWindowDragContentSwitcherModifier slideOverTongueState]
+ -[SBContinuousExposeWindowDragContentSwitcherModifier wantsSlideOverTongue]
+ -[SBControlCenterController controlCenterViewController:significantPresentationProgressChange:].cold.1
+ -[SBCoverSheetPresentationManager coverSheetSlidingViewControllerDidEndDismissGestureOverInterstitial:]
+ -[SBCoverSheetPresentationManager coverSheetSlidingViewControllerIsInterstitialDismissalAllowed:]
+ -[SBCoverSheetToAppsWorkspaceTransaction _logForInterruptAttemptReason:]
+ -[SBDashBoardHostableEntityHostingFluidSwitcherViewController activatingHostableEntity]
+ -[SBDashBoardHostableEntityHostingFluidSwitcherViewController currentHostableEntity]
+ -[SBDashBoardHostableEntityPresentationManager presentEntityWithRequest:]
+ -[SBDashBoardHostableEntityPresentationRequest .cxx_destruct]
+ -[SBDashBoardHostableEntityPresentationRequest animated]
+ -[SBDashBoardHostableEntityPresentationRequest dismissGestureEnabled]
+ -[SBDashBoardHostableEntityPresentationRequest entity]
+ -[SBDashBoardHostableEntityPresentationRequest initWithEntity:transitionRequest:animated:isEphemeralSwitcher:dismissGestureEnabled:presentationCompletion:]
+ -[SBDashBoardHostableEntityPresentationRequest isEphemeralSwitcher]
+ -[SBDashBoardHostableEntityPresentationRequest presentationCompletion]
+ -[SBDashBoardHostableEntityPresentationRequest transitionRequest]
+ -[SBDefaultImplementationsSwitcherModifier _slideOverAppLayoutIfAny]
+ -[SBDefaultImplementationsSwitcherModifier appLayoutToAttachSlideOverTongue]
+ -[SBDefaultImplementationsSwitcherModifier cornerRadiusForSlideOverTongueAppLayout]
+ -[SBDefaultImplementationsSwitcherModifier frameForIndexOffsetToCounteractSwitcherWindowMatchMoveForIndex:]
+ -[SBDefaultImplementationsSwitcherModifier frameForSlideOverTongueAppLayout]
+ -[SBDefaultImplementationsSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]
+ -[SBDefaultImplementationsSwitcherModifier slideOverMarginForLayoutRole:inAppLayout:]
+ -[SBDefaultImplementationsSwitcherModifier slideOverTongueDirection]
+ -[SBDefaultImplementationsSwitcherModifier slideOverTongueState]
+ -[SBDefaultImplementationsSwitcherModifier wantsSlideOverTongue]
+ -[SBDeviceApplicationSceneHandle _computeActiveAppearance]
+ -[SBDeviceApplicationSceneHandle _reevaluateActiveAppearanceFromAssertions]
+ -[SBDeviceApplicationSceneHandle _safeAreaCornerInsetResolverForApplicationFrame:screenBounds:activationSettings:]
+ -[SBDeviceApplicationSceneHandle _updateInterfaceActiveAppearance]
+ -[SBDeviceApplicationSceneHandle acquireActiveAppearanceAssertionWithReason:activeAppearance:priority:]
+ -[SBDeviceApplicationSceneHandle safeAreaEdgeInsetResolverForApplicationFrame:screenBounds:activationSettings:]
+ -[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:]
+ -[SBDisplayItemLayoutAttributes _initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:slideOverConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:]
+ -[SBDisplayItemLayoutAttributes _sizeForAttributedSize:inBounds:defaultSize:screenEdgePadding:]
+ -[SBDisplayItemLayoutAttributes attributesByModifyingSlideOverConfiguration:]
+ -[SBDisplayItemLayoutAttributes centerInBounds:]
+ -[SBDisplayItemLayoutAttributes initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:slideOverConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:]
+ -[SBDisplayItemLayoutAttributes sizeInBounds:defaultSize:screenEdgePadding:]
+ -[SBDisplayItemLayoutAttributes slideOverConfiguration]
+ -[SBDisplayItemLayoutAttributesCalculator _appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:layoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:]
+ -[SBDisplayItemLayoutAttributesCalculator _appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:usingNewLayoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:]
+ -[SBDisplayItemLayoutAttributesCalculator appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:options:containerOrientation:floatingDockHeight:screenScale:bounds:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:]
+ -[SBDisplayItemLayoutAttributesCalculator appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:usingLayoutAttributes:options:containerOrientation:windowScene:source:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:]
+ -[SBDisplayItemLayoutAttributesCalculator centerForLayoutAttributes:windowingConfiguration:]
+ -[SBDisplayItemLayoutAttributesCalculator flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:floatingDockHeight:screenScale:bounds:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
+ -[SBDisplayItemLayoutAttributesCalculator flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:floatingDockHeight:screenScale:bounds:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:newLayoutAttributes:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:]
+ -[SBDisplayItemLayoutAttributesCalculator frameForLayoutRole:inAppLayout:containerBounds:containerOrientation:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
+ -[SBDisplayItemLayoutAttributesCalculator sizeForLayoutAttributes:windowingConfiguration:]
+ -[SBDisplayItemLayoutAttributesCalculator sizeForSlideOverConfiguration:windowingConfiguration:]
+ -[SBDisplayItemLayoutAttributesCalculator updatedSlideOverConfigurationForItemWithSize:center:slideOverConfiguration:windowingConfiguration:]
+ -[SBDisplayItemLayoutAttributesProvider lastInteractedDisplayItemsInAppLayout:orientation:]
+ -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:displayOrdinal:orientation:]
+ -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:displayOrdinal:orientation:].cold.1
+ -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:displayOrdinal:orientation:].cold.2
+ -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:displayOrdinal:orientation:].cold.3
+ -[SBExposeWindowingModifier _effectiveIndexInRecencyOfAppLayout:]
+ -[SBExposeWindowingModifier displayItemsToExcludeFromStrip]
+ -[SBFilteringSwitcherModifier slideOverTongueModifierForRoutingModifier:]
+ -[SBFinishUnstashingSlideOverItemAnimationModifier .cxx_destruct]
+ -[SBFinishUnstashingSlideOverItemAnimationModifier animationAttributesForItem:]
+ -[SBFinishUnstashingSlideOverItemAnimationModifier frameForLayoutRole:inAppLayout:withBounds:]
+ -[SBFinishUnstashingSlideOverItemAnimationModifier shouldInterruptForActivity:]
+ -[SBFinishUnstashingSlideOverItemAnimationModifier transitionDidComplete:]
+ -[SBFinishUnstashingSlideOverItemAnimationModifier transitionWillBegin:]
+ -[SBFlexibleWindowingAutoLayoutController _effectiveStageAreaForSnappingItem:inSpace:configuration:]
+ -[SBFlexibleWindowingAutoLayoutController _isDockVisibleForBoundingBox:configuration:slideOverItem:]
+ -[SBFlexibleWindowingAutoLayoutController _isStripVisibleForBoundingBox:configuration:effectiveStripWidth:slideOverItem:]
+ -[SBFlexibleWindowingAutoLayoutController _snapPositionOfItem:ifNecessaryInSpace:autoLayoutConfiguration:snappedEdgesMask:]
+ -[SBFlexibleWindowingAutoLayoutController _snapPositionOfItem:toRect:inSpace:autoLayoutConfiguration:considerAdjacency:snappedEdgesMask:itemForPotentialPairing:]
+ -[SBFlexibleWindowingAutoLayoutController _snapSizeOfItem:ifNecessaryForSpace:configuration:snappedEdgesMask:]
+ -[SBFlexibleWindowingAutoLayoutController _snapSizeOfItem:toRect:inSpace:windowingConfiguration:considerAdjacency:snappedEdgesMask:newFrame:]
+ -[SBFlexibleWindowingAutoLayoutController _stageAreaForBoundingBox:configuration:effectiveStripWidth:slideOverItem:]
+ -[SBFlexibleWindowingAutoLayoutController spaceByPerformingFlexibleAutoLayoutWithSpace:configuration:options:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:]
+ -[SBFlexibleWindowingAutoLayoutItem isInSlideOver]
+ -[SBFlexibleWindowingAutoLayoutItem sceneRelevancyHint]
+ -[SBFlexibleWindowingAutoLayoutItem setInSlideOver:]
+ -[SBFlexibleWindowingAutoLayoutItem setSceneRelevancyHint:]
+ -[SBFlexibleWindowingAutoLayoutSpace isDockVisible]
+ -[SBFlexibleWindowingAutoLayoutSpace setDockVisible:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier appLayoutToAttachSlideOverTongue]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier hiddenContentStatusBarPartsForLayoutRole:inAppLayout:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier _draggingItemScreenCenterForSize:scale:]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier _shouldLockYPosition]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier _slideOverCenterExitingTimerWaitingWhileStillCloseWithCenter:]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutToAttachSlideOverTongue]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutsToCacheFullsizeSnapshots]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutsToCacheSnapshots]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier handleTimerEvent:]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:wantsSlideOverTongue:slideOverTongueState:slideOverTongueDirection:]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:wantsSlideOverTongue:slideOverTongueState:slideOverTongueDirection:].cold.1
+ -[SBFlexibleWindowingWindowDragSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:wantsSlideOverTongue:slideOverTongueState:slideOverTongueDirection:].cold.2
+ -[SBFlexibleWindowingWindowDragSwitcherModifier slideOverIsCenterExiting]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier slideOverTongueDirection]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier slideOverTongueState]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier wantsSlideOverTongue]
+ -[SBFluidSwitcherGestureManager _currentSlideOverConfiguration]
+ -[SBFluidSwitcherGestureManager _innerLeftEdgeDragHitTestRectForItemContainer:forPointerTouch:]
+ -[SBFluidSwitcherGestureManager _innerRightEdgeDragHitTestRectForItemContainer:forPointerTouch:]
+ -[SBFluidSwitcherGestureManager _isUnpinGestureAllowedToMoveWindowsAtLocationInReferenceCoordinateSpace:withinUnstashLocationOnHomeScreen:]
+ -[SBFluidSwitcherGestureManager _slideOverDisplayItem]
+ -[SBFluidSwitcherGestureManager _slideOverLeafAppLayout]
+ -[SBFluidSwitcherGestureManager _touchIsWithinUnstashRegionOnHomeScreen:]
+ -[SBFluidSwitcherGestureManager _touchLocationIsWithinSlideOverTongue:]
+ -[SBFluidSwitcherGestureManager _touchLocationIsWithinUnstashRegion:]
+ -[SBFluidSwitcherGestureManager indirectPanGestureSettings]
+ -[SBFluidSwitcherGestureManager setIndirectPanGestureSettings:]
+ -[SBFluidSwitcherItemContainer setSlideOverMargin:]
+ -[SBFluidSwitcherItemContainer setSlideOverTonguePortalSourceView:]
+ -[SBFluidSwitcherItemContainer slideOverMargin]
+ -[SBFluidSwitcherItemContainer slideOverTonguePortalSourceView]
+ -[SBFluidSwitcherViewController _modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]
+ -[SBFluidSwitcherViewController _performToggleSlideOverForDisplayItemResponse:]
+ -[SBFluidSwitcherViewController defaultWindowControlsLayoutForDisplayItem:frame:containerBounds:]
+ -[SBFluidSwitcherViewController displayItemInSlideOver]
+ -[SBFluidSwitcherViewController displayItemsToExcludeFromStrip]
+ -[SBFluidSwitcherViewController hitTestedToHomeAffordance:window:ofItemContainer:]
+ -[SBFluidSwitcherViewController hitTestedToSlideOverTongue:window:]
+ -[SBFluidSwitcherViewController lastInteractedItemsInAppLayout:]
+ -[SBFluidSwitcherViewController updateLayoutAttributes:ofDisplayItem:]
+ -[SBFullScreenContinuousExposeSwitcherModifier handleTapSlideOverTongueEvent:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier .cxx_destruct]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier adjustedAppLayoutsForAppLayouts:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier animationAttributesForItem:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier cornersForItem:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier didComplete]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier frameForItem:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier initWithFromAppLayout:toAppLayout:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier initWithFromAppLayout:toAppLayout:].cold.1
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier initWithFromAppLayout:toAppLayout:].cold.2
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier opacityForLayoutRole:inAppLayout:atIndex:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier perspectiveAngleForIndex:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier shouldInterruptForActivity:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier timerFired:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier titleStyleForItem:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier transitionDidComplete:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier transitionDidUpdate:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier transitionWillBegin:]
+ -[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier willBegin]
+ -[SBFullScreenToHomeIconZoomSwitcherModifier frameForIndexOffsetToCounteractSwitcherWindowMatchMoveForIndex:]
+ -[SBFullScreenToHomeIconZoomSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]
+ -[SBHomeGrabberView _effectiveHomeAffordanceViewFrame]
+ -[SBHomeGrabberView pointerWillExitRegion]
+ -[SBHomePeekToFullScreenTransitionModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]
+ -[SBHomePeekWindowingModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]
+ -[SBHomeScreenContinuousExposeSwitcherModifier handleSwitcherShortcutActionEvent:]
+ -[SBHomeScreenContinuousExposeSwitcherModifier handleTapSlideOverTongueEvent:]
+ -[SBHomeScreenController layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:]
+ -[SBIconController configureIconManager:]
+ -[SBIndirectPanGestureRecognizer lastTrackpadActivationTimestamp]
+ -[SBIndirectPanGestureRecognizer leafAppLayout]
+ -[SBIndirectPanGestureRecognizer setLastTrackpadActivationTimestamp:]
+ -[SBIndirectPanGestureRecognizer setLeafAppLayout:]
+ -[SBIndirectPanGestureRecognizer setShouldActivateWithThresholdForMouse:]
+ -[SBIndirectPanGestureRecognizer setShouldActivateWithThresholdForTrackpad:]
+ -[SBIndirectPanGestureRecognizer shouldActivateWithThresholdForMouse]
+ -[SBIndirectPanGestureRecognizer shouldActivateWithThresholdForTrackpad]
+ -[SBKeyboardFocusPolicy suppressCameraButtonDeferringToApplications]
+ -[SBKeyboardFocusResolutionContext .cxx_destruct]
+ -[SBKeyboardFocusResolutionContext zStackResolver]
+ -[SBLockScreenDeviceMotionEffectController _updateClientWantsMotionEventState]
+ -[SBLockScreenDeviceMotionEffectController posterClientDeviceMotionMode]
+ -[SBLockScreenDeviceMotionEffectController setPosterClientDeviceMotionMode:]
+ -[SBLockScreenManager posterDidUpdateDeviceMotionMode:]
+ -[SBMainSwitcherControllerCoordinator slideOverConfigurationOnAnySwitcherForDisplayItem:]
+ -[SBMainSwitcherControllerCoordinator switcherContentController:moveDisplayItemOutOfSlideOver:]
+ -[SBMainSwitcherControllerCoordinator switcherContentController:moveDisplayItemToSlideOver:]
+ -[SBMainSwitcherRoutingSwitcherModifier slideOverTongueModifierForRoutingModifier:]
+ -[SBMainWorkspace dismissTransientOverlayPresentationsAnimated:windowScene:filter:]
+ -[SBMenuBarMainMenuView touchesBegan:withEvent:]
+ -[SBMenuBarManager isMenuBarBecomingVisible]
+ -[SBMenuBarManager setMenuBarBecomingVisible:]
+ -[SBMenuBarPointerTrackingPanGestureRecognizer .cxx_destruct]
+ -[SBMenuBarPointerTrackingPanGestureRecognizer initWithMenuBarViewController:]
+ -[SBMenuBarPointerTrackingPanGestureRecognizer menuBarViewController]
+ -[SBMenuBarPointerTrackingPanGestureRecognizer setMenuBarViewController:]
+ -[SBMenuBarPointerTrackingPanGestureRecognizer touchesMoved:withEvent:]
+ -[SBMenuBarViewController _adjustPresentedMenuForPointerOverViewInContainer:forPanGesture:]
+ -[SBMenuBarViewController _handleMenuPanGesture:]
+ -[SBMoveDisplaysTransitionSwitcherModifier fromAppLayout]
+ -[SBMutableKeyboardFocusPolicy setSuppressCameraButtonDeferringToApplications:]
+ -[SBMutableKeyboardFocusResolutionContext setZStackResolver:]
+ -[SBMutableSwitcherTransitionRequest .cxx_destruct]
+ -[SBMutableSwitcherTransitionRequest bundleIdentifierOfAppToKillGracefully]
+ -[SBMutableSwitcherTransitionRequest setBundleIdentifierOfAppToKillGracefully:]
+ -[SBPBDisplayItemLayoutAttributes .cxx_destruct]
+ -[SBPBDisplayItemLayoutAttributes setSlideOverConfiguration:]
+ -[SBPBDisplayItemLayoutAttributes slideOverConfiguration]
+ -[SBPBDisplayItemLayoutAttributes writeTo:].cold.1
+ -[SBPBSlideOverConfiguration copyTo:]
+ -[SBPBSlideOverConfiguration copyWithZone:]
+ -[SBPBSlideOverConfiguration description]
+ -[SBPBSlideOverConfiguration dictionaryRepresentation]
+ -[SBPBSlideOverConfiguration hash]
+ -[SBPBSlideOverConfiguration isEqual:]
+ -[SBPBSlideOverConfiguration mergeFrom:]
+ -[SBPBSlideOverConfiguration readFrom:]
+ -[SBPBSlideOverConfiguration setSlideOverCorner:]
+ -[SBPBSlideOverConfiguration setSlideOverDodgesDock:]
+ -[SBPBSlideOverConfiguration setSlideOverIsActive:]
+ -[SBPBSlideOverConfiguration setSlideOverIsStashed:]
+ -[SBPBSlideOverConfiguration setSlideOverSizeHeight:]
+ -[SBPBSlideOverConfiguration setSlideOverSizeWidth:]
+ -[SBPBSlideOverConfiguration setSlideOverYOffsetFromCorner:]
+ -[SBPBSlideOverConfiguration slideOverCorner]
+ -[SBPBSlideOverConfiguration slideOverDodgesDock]
+ -[SBPBSlideOverConfiguration slideOverIsActive]
+ -[SBPBSlideOverConfiguration slideOverIsStashed]
+ -[SBPBSlideOverConfiguration slideOverSizeHeight]
+ -[SBPBSlideOverConfiguration slideOverSizeWidth]
+ -[SBPBSlideOverConfiguration slideOverYOffsetFromCorner]
+ -[SBPBSlideOverConfiguration writeTo:]
+ -[SBPIPController _keyboardInsetsForWindowScene:]
+ -[SBPeekSplitViewRoutingSwitcherModifier slideOverTongueModifierForRoutingModifier:]
+ -[SBRoutingSwitcherModifier cornerRadiusForSlideOverTongueAppLayout]
+ -[SBRoutingSwitcherModifier frameForIndexOffsetToCounteractSwitcherWindowMatchMoveForIndex:]
+ -[SBRoutingSwitcherModifier frameForSlideOverTongueAppLayout]
+ -[SBRoutingSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]
+ -[SBRoutingSwitcherModifier slideOverMarginForLayoutRole:inAppLayout:]
+ -[SBSDFElementView layer]
+ -[SBSDFView layer]
+ -[SBSceneHandleActiveAppearanceAssertion activeAppearance]
+ -[SBSceneHandleActiveAppearanceAssertion descriptionBuilderWithMultilinePrefix:]
+ -[SBSceneHandleActiveAppearanceAssertion initWithReason:activeAppearance:priority:invalidationBlock:]
+ -[SBSceneHandleActiveAppearanceAssertion initWithReason:activeAppearance:priority:invalidationBlock:].cold.1
+ -[SBSceneHandleActiveAppearanceAssertion priority]
+ -[SBSlideOverGlassMaterialView .cxx_destruct]
+ -[SBSlideOverGlassMaterialView _darkGlassBackgroundFilterParameters]
+ -[SBSlideOverGlassMaterialView _darkKeyFillVibrantColorMatrix]
+ -[SBSlideOverGlassMaterialView _increaseContrastDidChange:]
+ -[SBSlideOverGlassMaterialView _lightGlassBackgroundFilterParameters]
+ -[SBSlideOverGlassMaterialView _lightKeyFillVibrantColorMatrix]
+ -[SBSlideOverGlassMaterialView _reduceTransparencyDidChange:]
+ -[SBSlideOverGlassMaterialView _updateWithInterfaceStyle:]
+ -[SBSlideOverGlassMaterialView addSDFElementView:]
+ -[SBSlideOverGlassMaterialView dealloc]
+ -[SBSlideOverGlassMaterialView initWithFrame:]
+ -[SBSlideOverGlassMaterialView layoutSubviews]
+ -[SBSlideOverGlassMaterialView traitCollectionDidChange:]
+ -[SBSlideOverGlassMaterialView willMoveToWindow:]
+ -[SBSlideOverTongueView _continuousCornerRadius]
+ -[SBSlideOverTongueView _setContinuousCornerRadius:]
+ -[SBSplitDisplayItemSwitcherModifier topMostLayoutElements]
+ -[SBStashSlideOverItemAnimationModifier .cxx_destruct]
+ -[SBStashSlideOverItemAnimationModifier _layOutSlideOverItemFullyOffscreen]
+ -[SBStashSlideOverItemAnimationModifier _slideOverAppLayout]
+ -[SBStashSlideOverItemAnimationModifier adjustedAppLayoutsForAppLayouts:]
+ -[SBStashSlideOverItemAnimationModifier animationAttributesForItem:]
+ -[SBStashSlideOverItemAnimationModifier appLayoutToAttachSlideOverTongue]
+ -[SBStashSlideOverItemAnimationModifier appLayoutsToEnsureExistForMainTransitionEvent:]
+ -[SBStashSlideOverItemAnimationModifier cornersForItem:]
+ -[SBStashSlideOverItemAnimationModifier didComplete]
+ -[SBStashSlideOverItemAnimationModifier frameForItem:]
+ -[SBStashSlideOverItemAnimationModifier frameForLayoutRole:inAppLayout:withBounds:]
+ -[SBStashSlideOverItemAnimationModifier initWithDirection:]
+ -[SBStashSlideOverItemAnimationModifier isHomeScreenContentRequired]
+ -[SBStashSlideOverItemAnimationModifier isSwitcherWindowVisible]
+ -[SBStashSlideOverItemAnimationModifier opacityForLayoutRole:inAppLayout:atIndex:]
+ -[SBStashSlideOverItemAnimationModifier shouldInterruptForActivity:]
+ -[SBStashSlideOverItemAnimationModifier shouldUseAnchorPointToPinLayoutRolesToSpace:]
+ -[SBStashSlideOverItemAnimationModifier topMostItems]
+ -[SBStashSlideOverItemAnimationModifier transitionDidComplete:]
+ -[SBStashSlideOverItemAnimationModifier transitionDidUpdate:]
+ -[SBStashSlideOverItemAnimationModifier transitionWillBegin:]
+ -[SBStashSlideOverItemAnimationModifier visibleItems]
+ -[SBStashSlideOverItemAnimationModifier willBegin]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier .cxx_destruct]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier _responseForGestureEnd:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier _slideOverAppLayout]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier adjustedAppLayoutsForAppLayouts:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier animationAttributesForItem:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier appLayoutToAttachSlideOverTongue]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier appLayoutsToCacheFullsizeSnapshots]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier appLayoutsToCacheSnapshots]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier cornersForItem:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier didComplete]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier frameForItem:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier frameForLayoutRole:inAppLayout:withBounds:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier gestureDidComplete:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier gestureDidUpdate:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier gestureWillBegin:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier isLayoutRoleMatchMovedToScene:inAppLayout:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier isSwitcherWindowVisible]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier opacityForLayoutRole:inAppLayout:atIndex:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier shouldUseAnchorPointToPinLayoutRolesToSpace:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier slideOverTongueDirection]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier slideOverTongueState]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier topMostItems]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier transitionDidComplete:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier transitionWillBegin:]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier visibleItems]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier wantsSlideOverTongue]
+ -[SBStashSlideOverItemIndirectGestureWindowingModifier willBegin]
+ -[SBStripLayoutWindowingModifier _flexibleAutoLayoutSpaceForStripAppLayout:]
+ -[SBStripLayoutWindowingModifier adjustedAppLayoutsForAppLayouts:]
+ -[SBStripLayoutWindowingModifier frameForLayoutRole:inAppLayout:withBounds:]
+ -[SBStripLayoutWindowingModifier transitionWillBegin:]
+ -[SBSwitcherController _handleLeftSlideOverCommand:]
+ -[SBSwitcherController _handleRightSlideOverCommand:]
+ -[SBSwitcherController _handleToggleStashSlideOverCommand:]
+ -[SBSwitcherController _initializeSlideOverDisplayItemIfNeededForcingStashed:]
+ -[SBSwitcherController _managedMainDisplayItems]
+ -[SBSwitcherController _moveDisplayItemOutOfSlideOver:]
+ -[SBSwitcherController _moveDisplayItemToSlideOver:]
+ -[SBSwitcherController _slideOverDisplayItem]
+ -[SBSwitcherController windowControlsViewController:didRequestSlideOverAction:]
+ -[SBSwitcherModifier(SharedModifierUtilities) flexibleAutoLayoutSpaceForAppLayout:calculatedUsingNewLayoutAttributesMap:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:]
+ -[SBSwitcherTransitionRequest prefersZoomDownAnimation]
+ -[SBSwitcherTransitionRequest setPrefersZoomDownAnimation:]
+ -[SBSwitcherWindowingConfiguration setSlideOverBorderWidth:]
+ -[SBSwitcherWindowingConfiguration setSlideOverEnterCenterRegionThreshold:]
+ -[SBSwitcherWindowingConfiguration setSlideOverExitCenterRegionThreshold:]
+ -[SBSwitcherWindowingConfiguration setSlideOverThresholdToForegroundUnstashingApp:]
+ -[SBSwitcherWindowingConfiguration slideOverBorderWidth]
+ -[SBSwitcherWindowingConfiguration slideOverEnterCenterRegionThreshold]
+ -[SBSwitcherWindowingConfiguration slideOverExitCenterRegionThreshold]
+ -[SBSwitcherWindowingConfiguration slideOverThresholdToForegroundUnstashingApp]
+ -[SBSwitcherWindowingSettings setSlideOverEnterCenterRegionThreshold:]
+ -[SBSwitcherWindowingSettings setSlideOverExitCenterRegionThreshold:]
+ -[SBSwitcherWindowingSettings slideOverEnterCenterRegionThreshold]
+ -[SBSwitcherWindowingSettings slideOverExitCenterRegionThreshold]
+ -[SBSwitcherWindowingSettings windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:]
+ -[SBSwitcherWindowingSettings windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:]
+ -[SBSystemApertureContinuityDelayedUIWindowSceneDelegate continuitySessionDidUpdateState:].cold.13
+ -[SBSystemServiceServer _handleRequestAppSwitcherUpdateWindowingMode:fromClient:]
+ -[SBToggleSlideOverForDisplayItemSwitcherEventResponse .cxx_destruct]
+ -[SBToggleSlideOverForDisplayItemSwitcherEventResponse direction]
+ -[SBToggleSlideOverForDisplayItemSwitcherEventResponse displayItem]
+ -[SBToggleSlideOverForDisplayItemSwitcherEventResponse initWithDisplayItem:direction:]
+ -[SBToggleSlideOverForDisplayItemSwitcherEventResponse initWithDisplayItem:direction:].cold.1
+ -[SBToggleSlideOverForDisplayItemSwitcherEventResponse type]
+ -[SBTopAffordanceViewController enterSlideOverAction]
+ -[SBTopAffordanceViewController exitSlideOverAction]
+ -[SBTopAffordanceViewController slideOverMenu]
+ -[SBTopAffordanceViewController windowControlsViewController:didRequestSlideOverAction:]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier .cxx_destruct]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier _collapseAndPrepareForDismiss]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier _collapseSettlingDuration]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier didEdgeProtectSlideOverTongue:]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier gestureWillBegin:]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier initWithTonguePresentationReason:]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier isSwitcherWindowUserInteractionEnabled]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier isSwitcherWindowVisible]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier slideOverTongueState]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier timerFired:]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier transitionWillBegin:]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier wantsSlideOverTongue]
+ -[SBTransientlyVisibleSlideOverTongueWindowingModifier willBegin]
+ -[SBTransitionSwitcherModifierEvent isUnstashFromHomeTransition]
+ -[SBTransitionSwitcherModifierEvent prefersZoomDownAnimation]
+ -[SBTransitionSwitcherModifierEvent setPrefersZoomDownAnimation:]
+ -[SBTransitionSwitcherModifierEvent setUnstashFromHomeTransition:]
+ -[SBUserNotificationAlert alertAccessibilityIdentifier]
+ -[SBUserNotificationAlert alternateButtonAccessibilityIdentifier]
+ -[SBUserNotificationAlert defaultButtonAccessibilityIdentifier]
+ -[SBUserNotificationAlert otherButtonAccessibilityIdentifier]
+ -[SBUserNotificationAlert setAlertAccessibilityIdentifier:]
+ -[SBUserNotificationAlert setAlternateButtonAccessibilityIdentifier:]
+ -[SBUserNotificationAlert setDefaultButtonAccessibilityIdentifier:]
+ -[SBUserNotificationAlert setOtherButtonAccessibilityIdentifier:]
+ -[SBWallpaperController posterDeviceMotionMode]
+ -[SBWindowDragGestureWorkspaceTransaction selectedEdge]
+ -[SBWindowDragGestureWorkspaceTransaction unstashingFromHome]
+ -[SBWindowDragSwitcherModifierEvent selectedEdge]
+ -[SBWindowDragSwitcherModifierEvent setSelectedEdge:]
+ -[SBWindowDragSwitcherModifierEvent setUnstashingFromHome:]
+ -[SBWindowDragSwitcherModifierEvent unstashingFromHome]
+ -[SBWindowingModifier didEdgeProtectSlideOverTongue:]
+ -[SBWorkspaceApplicationSceneTransitionContext prefersZoomDownAnimation]
+ -[SBWorkspaceApplicationSceneTransitionContext setPrefersZoomDownAnimation:]
+ -[SpringBoard _handleLeftSlideOverCommand:]
+ -[SpringBoard _handleRightSlideOverCommand:]
+ -[SpringBoard _handleToggleStashSlideOverCommand:]
+ -[SpringBoard(StatusBar) statusBarShouldDisableRegionActions:]
+ -[_SBContinuitySessionStateMachine initWithStoreDemoPrepState:blockedState:preparingForRemoteUnlockState:waitingForRemoteUnlockState:waitingForScenesState:waitingForHIDServicesState:activatingState:updatingActiveDisplayState:launchingState:flushingState:activeState:]
+ -[_SBContinuitySessionStateMachine initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:inStoreDemoMode:]
+ -[_SBContinuitySessionStateMachine noteStoreDemoLockFailed]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep .cxx_destruct]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep _evaluateSystemEvents]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep _reevaluateStateForReason:]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep appendDescriptionToStream:]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep clientExternallyBlockedReasonsProvider]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep continuityDisplayAuthenticationCoordinatorDidUpdateLockState:]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep continuitySessionSystemEventMonitor:eventOccurred:]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep description]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep enteredStateFrom:]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep exitedStateTo:]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep invalidStateHandler]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep invalidate]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep noteClientDidUpdateExternallyBlockedReasons]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep noteStoreDemoLockFailed]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep setClientExternallyBlockedReasonsProvider:]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep setInvalidStateHandler:]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep setStateTransitionHandler:]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep setStateUpdateHandler:]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep stateTransitionHandler]
+ -[_SBContinuitySessionStateMachineStateStoreDemoPrep stateUpdateHandler]
+ -[_SBSlideOverGlassMaterialBackgroundView layer]
+ GCC_except_table136
+ GCC_except_table143
+ GCC_except_table155
+ GCC_except_table192
+ GCC_except_table223
+ GCC_except_table233
+ GCC_except_table269
+ GCC_except_table289
+ GCC_except_table306
+ GCC_except_table319
+ GCC_except_table325
+ GCC_except_table337
+ GCC_except_table393
+ GCC_except_table401
+ GCC_except_table415
+ GCC_except_table451
+ GCC_except_table457
+ GCC_except_table463
+ GCC_except_table475
+ GCC_except_table491
+ GCC_except_table504
+ GCC_except_table506
+ GCC_except_table508
+ GCC_except_table509
+ GCC_except_table514
+ GCC_except_table516
+ GCC_except_table522
+ GCC_except_table524
+ GCC_except_table526
+ GCC_except_table531
+ GCC_except_table541
+ GCC_except_table545
+ GCC_except_table551
+ GCC_except_table555
+ GCC_except_table579
+ GCC_except_table625
+ GCC_except_table660
+ GCC_except_table732
+ GCC_except_table756
+ GCC_except_table759
+ GCC_except_table800
+ GCC_except_table840
+ GCC_except_table889
+ GCC_except_table935
+ GCC_except_table96
+ GCC_except_table974
+ GCC_except_table985
+ GCC_except_table987
+ GCC_except_table989
+ GCC_except_table991
+ GCC_except_table993
+ OBJC_IVAR_$_SBPBDisplayItemLayoutAttributes._slideOverConfiguration
+ OBJC_IVAR_$_SBPBSlideOverConfiguration._slideOverCorner
+ OBJC_IVAR_$_SBPBSlideOverConfiguration._slideOverDodgesDock
+ OBJC_IVAR_$_SBPBSlideOverConfiguration._slideOverIsActive
+ OBJC_IVAR_$_SBPBSlideOverConfiguration._slideOverIsStashed
+ OBJC_IVAR_$_SBPBSlideOverConfiguration._slideOverSizeHeight
+ OBJC_IVAR_$_SBPBSlideOverConfiguration._slideOverSizeWidth
+ OBJC_IVAR_$_SBPBSlideOverConfiguration._slideOverYOffsetFromCorner
+ _NSStringFromDisplayItemSlideOverConfiguration
+ _NSStringFromDisplayItemSlideOverCorner
+ _NSStringFromUIUserInterfaceActiveAppearance
+ _OBJC_CLASS_$_CASDFElementLayer
+ _OBJC_CLASS_$_CASDFKeyFillHighlightEffect
+ _OBJC_CLASS_$_CASDFLayer
+ _OBJC_CLASS_$_CASDFOutputEffect
+ _OBJC_CLASS_$_SBContinuitySessionStoreDemoController
+ _OBJC_CLASS_$_SBDashBoardHostableEntityPresentationRequest
+ _OBJC_CLASS_$_SBFinishUnstashingSlideOverItemAnimationModifier
+ _OBJC_CLASS_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier
+ _OBJC_CLASS_$_SBMenuBarPointerTrackingPanGestureRecognizer
+ _OBJC_CLASS_$_SBPBSlideOverConfiguration
+ _OBJC_CLASS_$_SBSDFElementView
+ _OBJC_CLASS_$_SBSDFView
+ _OBJC_CLASS_$_SBSceneHandleActiveAppearanceAssertion
+ _OBJC_CLASS_$_SBSlideOverGlassMaterialView
+ _OBJC_CLASS_$_SBStashSlideOverItemAnimationModifier
+ _OBJC_CLASS_$_SBStashSlideOverItemIndirectGestureWindowingModifier
+ _OBJC_CLASS_$_SBToggleSlideOverForDisplayItemSwitcherEventResponse
+ _OBJC_CLASS_$_SBTransientlyVisibleSlideOverTongueWindowingModifier
+ _OBJC_CLASS_$__SBContinuitySessionStateMachineStateStoreDemoPrep
+ _OBJC_CLASS_$__SBSlideOverGlassMaterialBackgroundView
+ _OBJC_CLASS_$__UISceneSafeAreaCornerInsetConcreteResolver
+ _OBJC_CLASS_$__UISceneSafeAreaEdgeInsetConcreteResolver
+ _OBJC_IVAR_$_SBAppSwitcherPageView._destinationSDFElementView
+ _OBJC_IVAR_$_SBAppSwitcherPageView._glassView
+ _OBJC_IVAR_$_SBAppSwitcherPageView._sdfElementContainerView
+ _OBJC_IVAR_$_SBAppSwitcherPageView._slideOverBorderWidth
+ _OBJC_IVAR_$_SBAppSwitcherPageView._slideOverTonguePortalView
+ _OBJC_IVAR_$_SBContinuitySession._storeDemoModeController
+ _OBJC_IVAR_$_SBContinuitySessionStoreDemoController._systemEventMonitor
+ _OBJC_IVAR_$_SBContinuousExposeArcSwipeSwitcherModifier._initialVisibleDisplayItems
+ _OBJC_IVAR_$_SBContinuousExposeWindowDragContentSwitcherModifier._slideOverTongueDirection
+ _OBJC_IVAR_$_SBContinuousExposeWindowDragContentSwitcherModifier._slideOverTongueState
+ _OBJC_IVAR_$_SBContinuousExposeWindowDragContentSwitcherModifier._wantsSlideOverTongue
+ _OBJC_IVAR_$_SBContinuousExposeWindowDragDestinationSwitcherModifier._selectedItemIsInSlideOver
+ _OBJC_IVAR_$_SBContinuousExposeWindowDragDestinationSwitcherModifier._translation
+ _OBJC_IVAR_$_SBDashBoardHostableEntityHostingFluidSwitcherViewController._activatingHostableEntity
+ _OBJC_IVAR_$_SBDashBoardHostableEntityHostingFluidSwitcherViewController._currentHostableEntity
+ _OBJC_IVAR_$_SBDashBoardHostableEntityPresentationManager._isDismissingEntity
+ _OBJC_IVAR_$_SBDashBoardHostableEntityPresentationManager._pendingPresentationRequests
+ _OBJC_IVAR_$_SBDashBoardHostableEntityPresentationRequest._animated
+ _OBJC_IVAR_$_SBDashBoardHostableEntityPresentationRequest._dismissGestureEnabled
+ _OBJC_IVAR_$_SBDashBoardHostableEntityPresentationRequest._entity
+ _OBJC_IVAR_$_SBDashBoardHostableEntityPresentationRequest._isEphemeralSwitcher
+ _OBJC_IVAR_$_SBDashBoardHostableEntityPresentationRequest._presentationCompletion
+ _OBJC_IVAR_$_SBDashBoardHostableEntityPresentationRequest._transitionRequest
+ _OBJC_IVAR_$_SBDeviceApplicationSceneHandle._activeAppearanceAssertions
+ _OBJC_IVAR_$_SBDeviceApplicationSceneHandle._computedActiveAppearance
+ _OBJC_IVAR_$_SBDisplayItemLayoutAttributes._slideOverConfiguration
+ _OBJC_IVAR_$_SBFinishUnstashingSlideOverItemAnimationModifier._transitionID
+ _OBJC_IVAR_$_SBFlexibleWindowingAutoLayoutItem._inSlideOver
+ _OBJC_IVAR_$_SBFlexibleWindowingAutoLayoutItem._sceneRelevancyHint
+ _OBJC_IVAR_$_SBFlexibleWindowingAutoLayoutSpace._dockVisible
+ _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._inLeftPinnedSlideOver
+ _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._inRightPinnedSlideOver
+ _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._selectedItemIsInSlideOver
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._hasUnstashed
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._initialSlideOverConfiguration
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._lastCenterYBeforeStashingOrUnstashingBegan
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._layOutSlideOverItemFullyOffscreen
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._slideOverCenterExitingUpdateGeneration
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._slideOverCenterExitingUpdateReason
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._slideOverCenterSettledPosition
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._slideOverIsCenterExiting
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._slideOverTongueDirection
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._slideOverTongueState
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._startedStashed
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._translation
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._wantsSlideOverTongue
+ _OBJC_IVAR_$_SBFluidSwitcherGestureManager._indirectPanGestureSettings
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._adjustedFromAppLayout
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._adjustedToAppLayout
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._animationPhase
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._fromAppLayout
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._slideOverAppLayout
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._timerReason
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._toAppLayout
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._toAppLayoutInitialBounds
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._toAppLayoutInitialCornerRadius
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._toAppLayoutInitialPosition
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._toAppLayoutInitialScale
+ _OBJC_IVAR_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier._transitionID
+ _OBJC_IVAR_$_SBFullScreenSwitcherSceneLiveContentOverlay._activeAppearanceAssertion
+ _OBJC_IVAR_$_SBInCallPresentationSession._activeAppearanceAssertion
+ _OBJC_IVAR_$_SBIndirectPanGestureRecognizer._lastTrackpadActivationTimestamp
+ _OBJC_IVAR_$_SBIndirectPanGestureRecognizer._leafAppLayout
+ _OBJC_IVAR_$_SBIndirectPanGestureRecognizer._shouldActivateWithThresholdForMouse
+ _OBJC_IVAR_$_SBIndirectPanGestureRecognizer._shouldActivateWithThresholdForTrackpad
+ _OBJC_IVAR_$_SBKeyboardFocusPolicy._suppressCameraButtonDeferringToApplications
+ _OBJC_IVAR_$_SBKeyboardFocusResolutionContext._zStackResolver
+ _OBJC_IVAR_$_SBLockScreenDeviceMotionEffectController._posterClientDeviceMotionMode
+ _OBJC_IVAR_$_SBMenuBarManager._menuBarBecomingVisible
+ _OBJC_IVAR_$_SBMenuBarPointerTrackingPanGestureRecognizer._menuBarViewController
+ _OBJC_IVAR_$_SBMoveDisplaysTransitionSwitcherModifier._fromAppLayout
+ _OBJC_IVAR_$_SBMutableSwitcherTransitionRequest._bundleIdentifierOfAppToKillGracefully
+ _OBJC_IVAR_$_SBSceneHandleActiveAppearanceAssertion._activeAppearance
+ _OBJC_IVAR_$_SBSceneHandleActiveAppearanceAssertion._priority
+ _OBJC_IVAR_$_SBSlideOverGlassMaterialView._backgroundSDFView
+ _OBJC_IVAR_$_SBSlideOverGlassMaterialView._backgroundView
+ _OBJC_IVAR_$_SBSlideOverGlassMaterialView._specularSDFView
+ _OBJC_IVAR_$_SBSlideOverTongueView._contentView
+ _OBJC_IVAR_$_SBSlideOverTongueView._destinationSDFElementView
+ _OBJC_IVAR_$_SBSlideOverTongueView._glassView
+ _OBJC_IVAR_$_SBSlideOverTongueView._sdfElementContainerView
+ _OBJC_IVAR_$_SBSlideOverTongueView._sourceSDFElementView
+ _OBJC_IVAR_$_SBSlideOverTongueView._tongueSize
+ _OBJC_IVAR_$_SBStashSlideOverItemAnimationModifier._direction
+ _OBJC_IVAR_$_SBStashSlideOverItemAnimationModifier._slideOverDisplayItem
+ _OBJC_IVAR_$_SBStashSlideOverItemAnimationModifier._transitionID
+ _OBJC_IVAR_$_SBStashSlideOverItemAnimationModifier._transitioningToHome
+ _OBJC_IVAR_$_SBStashSlideOverItemIndirectGestureWindowingModifier._gestureID
+ _OBJC_IVAR_$_SBStashSlideOverItemIndirectGestureWindowingModifier._initialAppLayout
+ _OBJC_IVAR_$_SBStashSlideOverItemIndirectGestureWindowingModifier._initialFrame
+ _OBJC_IVAR_$_SBStashSlideOverItemIndirectGestureWindowingModifier._initialSlideOverConfiguration
+ _OBJC_IVAR_$_SBStashSlideOverItemIndirectGestureWindowingModifier._slideOverDisplayItem
+ _OBJC_IVAR_$_SBStashSlideOverItemIndirectGestureWindowingModifier._slideOverTongueDirection
+ _OBJC_IVAR_$_SBStashSlideOverItemIndirectGestureWindowingModifier._slideOverTongueState
+ _OBJC_IVAR_$_SBStashSlideOverItemIndirectGestureWindowingModifier._translation
+ _OBJC_IVAR_$_SBStashSlideOverItemIndirectGestureWindowingModifier._wantsSlideOverTongue
+ _OBJC_IVAR_$_SBSwitcherController._slideOverDisplayItem
+ _OBJC_IVAR_$_SBSwitcherTransitionRequest._prefersZoomDownAnimation
+ _OBJC_IVAR_$_SBSwitcherWindowingConfiguration._slideOverBorderWidth
+ _OBJC_IVAR_$_SBSwitcherWindowingConfiguration._slideOverEnterCenterRegionThreshold
+ _OBJC_IVAR_$_SBSwitcherWindowingConfiguration._slideOverExitCenterRegionThreshold
+ _OBJC_IVAR_$_SBSwitcherWindowingConfiguration._slideOverThresholdToForegroundUnstashingApp
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._cachedWindowingConfiguration_prototypingSlideOverBorderWidth
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._cachedWindowingConfiguration_prototypingSlideOverEnterCenterRegionThreshold
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._cachedWindowingConfiguration_prototypingSlideOverExitCenterRegionThreshold
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._slideOverEnterCenterRegionThreshold
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._slideOverExitCenterRegionThreshold
+ _OBJC_IVAR_$_SBToggleSlideOverForDisplayItemSwitcherEventResponse._direction
+ _OBJC_IVAR_$_SBToggleSlideOverForDisplayItemSwitcherEventResponse._displayItem
+ _OBJC_IVAR_$_SBTopAffordanceViewController._enterSlideOverAction
+ _OBJC_IVAR_$_SBTopAffordanceViewController._exitSlideOverAction
+ _OBJC_IVAR_$_SBTopAffordanceViewController._slideOverMenu
+ _OBJC_IVAR_$_SBTransientlyVisibleSlideOverTongueWindowingModifier._didCollapseSlideOverTongue
+ _OBJC_IVAR_$_SBTransientlyVisibleSlideOverTongueWindowingModifier._finishedReason
+ _OBJC_IVAR_$_SBTransientlyVisibleSlideOverTongueWindowingModifier._hasBegunEdgeProtect
+ _OBJC_IVAR_$_SBTransientlyVisibleSlideOverTongueWindowingModifier._tonguePresentationReason
+ _OBJC_IVAR_$_SBTransitionSwitcherModifierEvent._prefersZoomDownAnimation
+ _OBJC_IVAR_$_SBTransitionSwitcherModifierEvent._unstashFromHomeTransition
+ _OBJC_IVAR_$_SBUserNotificationAlert._alertAccessibilityIdentifier
+ _OBJC_IVAR_$_SBUserNotificationAlert._alternateButtonAccessibilityIdentifier
+ _OBJC_IVAR_$_SBUserNotificationAlert._defaultButtonAccessibilityIdentifier
+ _OBJC_IVAR_$_SBUserNotificationAlert._otherButtonAccessibilityIdentifier
+ _OBJC_IVAR_$_SBWindowDragGestureWorkspaceTransaction._selectedEdge
+ _OBJC_IVAR_$_SBWindowDragGestureWorkspaceTransaction._unstashingFromHome
+ _OBJC_IVAR_$_SBWindowDragSwitcherModifierEvent._selectedEdge
+ _OBJC_IVAR_$_SBWindowDragSwitcherModifierEvent._unstashingFromHome
+ _OBJC_IVAR_$_SBWorkspaceApplicationSceneTransitionContext._prefersZoomDownAnimation
+ _OBJC_IVAR_$__SBContinuitySessionStateMachine._storeDemoPrepState
+ _OBJC_IVAR_$__SBContinuitySessionStateMachineStateStoreDemoPrep._authenticationCoordinator
+ _OBJC_IVAR_$__SBContinuitySessionStateMachineStateStoreDemoPrep._blockOnUIUnlock
+ _OBJC_IVAR_$__SBContinuitySessionStateMachineStateStoreDemoPrep._clientExternallyBlockedReasonsProvider
+ _OBJC_IVAR_$__SBContinuitySessionStateMachineStateStoreDemoPrep._invalidStateHandler
+ _OBJC_IVAR_$__SBContinuitySessionStateMachineStateStoreDemoPrep._isCurrentState
+ _OBJC_IVAR_$__SBContinuitySessionStateMachineStateStoreDemoPrep._stateTransitionHandler
+ _OBJC_IVAR_$__SBContinuitySessionStateMachineStateStoreDemoPrep._stateUpdateHandler
+ _OBJC_IVAR_$__SBContinuitySessionStateMachineStateStoreDemoPrep._systemEventMonitor
+ _OBJC_IVAR_$__SBContinuitySessionStateMachineStateStoreDemoPrep._uiLocked
+ _OBJC_METACLASS_$_SBContinuitySessionStoreDemoController
+ _OBJC_METACLASS_$_SBDashBoardHostableEntityPresentationRequest
+ _OBJC_METACLASS_$_SBFinishUnstashingSlideOverItemAnimationModifier
+ _OBJC_METACLASS_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier
+ _OBJC_METACLASS_$_SBMenuBarPointerTrackingPanGestureRecognizer
+ _OBJC_METACLASS_$_SBPBSlideOverConfiguration
+ _OBJC_METACLASS_$_SBSDFElementView
+ _OBJC_METACLASS_$_SBSDFView
+ _OBJC_METACLASS_$_SBSceneHandleActiveAppearanceAssertion
+ _OBJC_METACLASS_$_SBSlideOverGlassMaterialView
+ _OBJC_METACLASS_$_SBStashSlideOverItemAnimationModifier
+ _OBJC_METACLASS_$_SBStashSlideOverItemIndirectGestureWindowingModifier
+ _OBJC_METACLASS_$_SBToggleSlideOverForDisplayItemSwitcherEventResponse
+ _OBJC_METACLASS_$_SBTransientlyVisibleSlideOverTongueWindowingModifier
+ _OBJC_METACLASS_$__SBContinuitySessionStateMachineStateStoreDemoPrep
+ _OBJC_METACLASS_$__SBSlideOverGlassMaterialBackgroundView
+ _SBDemoLoopBundleIdentifier
+ _SBDisplayItemDescendingInteractionTimeComparator
+ _SBDisplayItemSlideOverConfigurationIsValid
+ _SBDisplayItemSlideOverConfigurationMake
+ _SBDisplayItemSlideOverConfigurationNone
+ _SBDisplayItemSlideOverIsLeftSided
+ _SBDisplayItemSlideOverIsTopAligned
+ _SBEqualDisplayItemSlideOverConfigurations
+ _SBFIsSlideOverAvailable
+ _SBFloatingConfigurationFromSlideOverConfiguration
+ _SBInactiveDisplayItemSlideOverConfigurationFromSlideOverConfiguration
+ _SBPBSlideOverConfigurationReadFrom
+ _SBSceneRelevancyHintDescription
+ _UIAccessibilityDarkerSystemColorsEnabled
+ _UIAccessibilityDarkerSystemColorsStatusDidChangeNotification
+ __OBJC_$_CLASS_METHODS_SBSDFElementView
+ __OBJC_$_CLASS_METHODS_SBSDFView
+ __OBJC_$_CLASS_METHODS__SBSlideOverGlassMaterialBackgroundView
+ __OBJC_$_INSTANCE_METHODS_FBSSceneSettings(SBTransientLocal|SBApplicationSceneHandle|Frame)
+ __OBJC_$_INSTANCE_METHODS_SBContinuitySessionStoreDemoController
+ __OBJC_$_INSTANCE_METHODS_SBDashBoardHostableEntityPresentationRequest
+ __OBJC_$_INSTANCE_METHODS_SBFinishUnstashingSlideOverItemAnimationModifier
+ __OBJC_$_INSTANCE_METHODS_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier
+ __OBJC_$_INSTANCE_METHODS_SBMenuBarPointerTrackingPanGestureRecognizer
+ __OBJC_$_INSTANCE_METHODS_SBMutableSwitcherTransitionRequest
+ __OBJC_$_INSTANCE_METHODS_SBPBSlideOverConfiguration
+ __OBJC_$_INSTANCE_METHODS_SBSDFElementView
+ __OBJC_$_INSTANCE_METHODS_SBSDFView
+ __OBJC_$_INSTANCE_METHODS_SBSceneHandleActiveAppearanceAssertion
+ __OBJC_$_INSTANCE_METHODS_SBSlideOverGlassMaterialView
+ __OBJC_$_INSTANCE_METHODS_SBStashSlideOverItemAnimationModifier
+ __OBJC_$_INSTANCE_METHODS_SBStashSlideOverItemIndirectGestureWindowingModifier
+ __OBJC_$_INSTANCE_METHODS_SBToggleSlideOverForDisplayItemSwitcherEventResponse
+ __OBJC_$_INSTANCE_METHODS_SBTransientlyVisibleSlideOverTongueWindowingModifier
+ __OBJC_$_INSTANCE_METHODS__SBContinuitySessionStateMachineStateStoreDemoPrep
+ __OBJC_$_INSTANCE_METHODS__SBSlideOverGlassMaterialBackgroundView
+ __OBJC_$_INSTANCE_VARIABLES_SBContinuitySessionStoreDemoController
+ __OBJC_$_INSTANCE_VARIABLES_SBDashBoardHostableEntityPresentationRequest
+ __OBJC_$_INSTANCE_VARIABLES_SBFinishUnstashingSlideOverItemAnimationModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBMenuBarPointerTrackingPanGestureRecognizer
+ __OBJC_$_INSTANCE_VARIABLES_SBMutableSwitcherTransitionRequest
+ __OBJC_$_INSTANCE_VARIABLES_SBPBSlideOverConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SBSceneHandleActiveAppearanceAssertion
+ __OBJC_$_INSTANCE_VARIABLES_SBSlideOverGlassMaterialView
+ __OBJC_$_INSTANCE_VARIABLES_SBStashSlideOverItemAnimationModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBStashSlideOverItemIndirectGestureWindowingModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBToggleSlideOverForDisplayItemSwitcherEventResponse
+ __OBJC_$_INSTANCE_VARIABLES_SBTransientlyVisibleSlideOverTongueWindowingModifier
+ __OBJC_$_INSTANCE_VARIABLES__SBContinuitySessionStateMachineStateStoreDemoPrep
+ __OBJC_$_PROP_LIST_FBSSceneSettings_$_SBTransientLocal
+ __OBJC_$_PROP_LIST_SBContinuitySessionStoreDemoController
+ __OBJC_$_PROP_LIST_SBDashBoardHostableEntityPresentationRequest
+ __OBJC_$_PROP_LIST_SBMenuBarPointerTrackingPanGestureRecognizer
+ __OBJC_$_PROP_LIST_SBSceneHandleActiveAppearanceAssertion
+ __OBJC_$_PROP_LIST_SBToggleSlideOverForDisplayItemSwitcherEventResponse
+ __OBJC_$_PROP_LIST__SBContinuitySessionStateMachineStateStoreDemoPrep
+ __OBJC_CLASS_PROTOCOLS_$_SBContinuitySessionStoreDemoController
+ __OBJC_CLASS_PROTOCOLS_$_SBPBSlideOverConfiguration
+ __OBJC_CLASS_PROTOCOLS_$__SBContinuitySessionStateMachineStateStoreDemoPrep
+ __OBJC_CLASS_RO_$_SBContinuitySessionStoreDemoController
+ __OBJC_CLASS_RO_$_SBDashBoardHostableEntityPresentationRequest
+ __OBJC_CLASS_RO_$_SBFinishUnstashingSlideOverItemAnimationModifier
+ __OBJC_CLASS_RO_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier
+ __OBJC_CLASS_RO_$_SBMenuBarPointerTrackingPanGestureRecognizer
+ __OBJC_CLASS_RO_$_SBPBSlideOverConfiguration
+ __OBJC_CLASS_RO_$_SBSDFElementView
+ __OBJC_CLASS_RO_$_SBSDFView
+ __OBJC_CLASS_RO_$_SBSceneHandleActiveAppearanceAssertion
+ __OBJC_CLASS_RO_$_SBSlideOverGlassMaterialView
+ __OBJC_CLASS_RO_$_SBStashSlideOverItemAnimationModifier
+ __OBJC_CLASS_RO_$_SBStashSlideOverItemIndirectGestureWindowingModifier
+ __OBJC_CLASS_RO_$_SBToggleSlideOverForDisplayItemSwitcherEventResponse
+ __OBJC_CLASS_RO_$_SBTransientlyVisibleSlideOverTongueWindowingModifier
+ __OBJC_CLASS_RO_$__SBContinuitySessionStateMachineStateStoreDemoPrep
+ __OBJC_CLASS_RO_$__SBSlideOverGlassMaterialBackgroundView
+ __OBJC_METACLASS_RO_$_SBContinuitySessionStoreDemoController
+ __OBJC_METACLASS_RO_$_SBDashBoardHostableEntityPresentationRequest
+ __OBJC_METACLASS_RO_$_SBFinishUnstashingSlideOverItemAnimationModifier
+ __OBJC_METACLASS_RO_$_SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier
+ __OBJC_METACLASS_RO_$_SBMenuBarPointerTrackingPanGestureRecognizer
+ __OBJC_METACLASS_RO_$_SBPBSlideOverConfiguration
+ __OBJC_METACLASS_RO_$_SBSDFElementView
+ __OBJC_METACLASS_RO_$_SBSDFView
+ __OBJC_METACLASS_RO_$_SBSceneHandleActiveAppearanceAssertion
+ __OBJC_METACLASS_RO_$_SBSlideOverGlassMaterialView
+ __OBJC_METACLASS_RO_$_SBStashSlideOverItemAnimationModifier
+ __OBJC_METACLASS_RO_$_SBStashSlideOverItemIndirectGestureWindowingModifier
+ __OBJC_METACLASS_RO_$_SBToggleSlideOverForDisplayItemSwitcherEventResponse
+ __OBJC_METACLASS_RO_$_SBTransientlyVisibleSlideOverTongueWindowingModifier
+ __OBJC_METACLASS_RO_$__SBContinuitySessionStateMachineStateStoreDemoPrep
+ __OBJC_METACLASS_RO_$__SBSlideOverGlassMaterialBackgroundView
+ __SBHIDMediaKeyEventDescriptorSet
+ __UIConvertPointFromOrientationToOrientation
+ ___101-[SBSceneHandleActiveAppearanceAssertion initWithReason:activeAppearance:priority:invalidationBlock:]_block_invoke
+ ___102-[SBFluidSwitcherGestureManager _hitTestStageItemContainerForUnpinGestureWithTouch:atGestureLocation:]_block_invoke_3
+ ___102-[SBInCallPresentationSession layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:]_block_invoke_4
+ ___103-[SBDeviceApplicationSceneHandle acquireActiveAppearanceAssertionWithReason:activeAppearance:priority:]_block_invoke
+ ___103-[SBDeviceApplicationSceneHandle acquireActiveAppearanceAssertionWithReason:activeAppearance:priority:]_block_invoke_2
+ ___105-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:displayOrdinal:orientation:]_block_invoke
+ ___105-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:displayOrdinal:orientation:]_block_invoke_2
+ ___105-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:displayOrdinal:orientation:]_block_invoke_3
+ ___106-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:]_block_invoke
+ ___106-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:]_block_invoke_2
+ ___106-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:]_block_invoke_3
+ ___106-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:]_block_invoke_4
+ ___107-[SBHomePeekToFullScreenTransitionModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]_block_invoke
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.315
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.316
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.317
+ ___110-[SBInCallPresentationSession _updateVisibilityInSwitcherForPrefersHiddenWhenDismissedIfNeededForLayoutState:]_block_invoke.248
+ ___119-[SBDashBoardApplicationLauncher _activateCameraEntity:animated:asOverlay:viaSwitcherModal:request:actions:completion:]_block_invoke.65
+ ___119-[SBDashBoardApplicationLauncher _activateCameraEntity:animated:asOverlay:viaSwitcherModal:request:actions:completion:]_block_invoke_2.69
+ ___119-[SBDashBoardApplicationLauncher _activateCameraEntity:animated:asOverlay:viaSwitcherModal:request:actions:completion:]_block_invoke_3.70
+ ___119-[SBDashBoardApplicationLauncher _activateCameraEntity:animated:asOverlay:viaSwitcherModal:request:actions:completion:]_block_invoke_4.72
+ ___122-[SBFluidSwitcherViewController _modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]_block_invoke
+ ___122-[_SBContinuitySessionStateMachine initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:inStoreDemoMode:]_block_invoke
+ ___124-[SBDashBoardHostableEntityHostingFluidSwitcherViewController activateDisplayItemForEntity:fromRequest:animated:completion:]_block_invoke_3
+ ___129-[SBTopAffordanceViewController updateTopAffordanceContextMenuWithOptions:selectedActionType:layout:hidden:interfaceOrientation:]_block_invoke_20
+ ___129-[SBTopAffordanceViewController updateTopAffordanceContextMenuWithOptions:selectedActionType:layout:hidden:interfaceOrientation:]_block_invoke_21
+ ___141-[SBPIPController _updatePictureInPictureOverlayInsetsOnWindowScene:withCurrentLayoutState:toHomeScreen:toInterfaceOrientation:shouldUpdate:]_block_invoke
+ ___144-[SBFluidSwitcherLayoutContext shouldAddAppLayoutToFront:forTransitionWithContext:recentAppLayouts:transitionCompleted:windowManagementContext:]_block_invoke
+ ___144-[SBFluidSwitcherLayoutContext shouldAddAppLayoutToFront:forTransitionWithContext:recentAppLayouts:transitionCompleted:windowManagementContext:]_block_invoke_2
+ ___173+[SBSwitcherCoordinatedLayoutStateTransitionContext coordinatedLayoutStateTransitionContextForMovingDisplayItems:toSwitcherController:toAppLayout:withApplicationController:]_block_invoke_2
+ ___38-[SBIconController _registerAnalytics]_block_invoke.221
+ ___399-[SBDisplayItemLayoutAttributesCalculator _appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:usingNewLayoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:]_block_invoke
+ ___399-[SBDisplayItemLayoutAttributesCalculator _appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:usingNewLayoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:]_block_invoke_2
+ ___42-[SBStripModelWindowingModifier didUpdate]_block_invoke_13
+ ___42-[SBStripModelWindowingModifier didUpdate]_block_invoke_14
+ ___47-[SBLockScreenManager handleTransitionRequest:]_block_invoke.248
+ ___49-[SBRoutingSwitcherModifier slideOverTongueState]_block_invoke_2
+ ___49-[SBRoutingSwitcherModifier wantsSlideOverTongue]_block_invoke_2
+ ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.91
+ ___53-[SBRoutingSwitcherModifier slideOverTongueDirection]_block_invoke_2
+ ___53-[SBStashSlideOverItemAnimationModifier visibleItems]_block_invoke
+ ___53-[SBStripModelWindowingModifier transitionDidUpdate:]_block_invoke
+ ___53-[SBStripModelWindowingModifier transitionDidUpdate:]_block_invoke_2
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.386
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.389
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.388
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.293
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.293.cold.1
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.297
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.298
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.298.cold.1
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.301
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.301.cold.1
+ ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.780
+ ___56-[SBFluidSwitcherGestureManager _slideOverLeafAppLayout]_block_invoke
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1793
+ ___58-[SBSlideOverGlassMaterialView _updateWithInterfaceStyle:]_block_invoke
+ ___59-[SBIconController _updateUninstallingSystemAppsRestricted]_block_invoke.220
+ ___59-[SBMainSwitcherControllerCoordinator _buildAppLayoutCache]_block_invoke_12
+ ___59-[SBSplitDisplayItemSwitcherModifier topMostLayoutElements]_block_invoke
+ ___60-[SBStashSlideOverItemAnimationModifier _slideOverAppLayout]_block_invoke
+ ___61-[SBRoutingSwitcherModifier appLayoutToAttachSlideOverTongue]_block_invoke_2
+ ___61-[SBRoutingSwitcherModifier frameForSlideOverTongueAppLayout]_block_invoke
+ ___61-[SBRoutingSwitcherModifier frameForSlideOverTongueAppLayout]_block_invoke_2
+ ___62-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]_block_invoke_5
+ ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.247
+ ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.247.cold.1
+ ___65-[SBExposeWindowingModifier _effectiveIndexInRecencyOfAppLayout:]_block_invoke
+ ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke.213
+ ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke_2.216
+ ___65-[SBMoveDisplaysTransitionSwitcherModifier topMostLayoutElements]_block_invoke
+ ___65-[SBTransientlyVisibleSlideOverTongueWindowingModifier willBegin]_block_invoke
+ ___66-[SBDeviceApplicationSceneHandle _updateInterfaceActiveAppearance]_block_invoke
+ ___66-[SBFlexibleWindowingWindowDragSwitcherModifier handleTimerEvent:]_block_invoke
+ ___66-[SBStripLayoutWindowingModifier adjustedAppLayoutsForAppLayouts:]_block_invoke
+ ___66-[SBStripLayoutWindowingModifier adjustedAppLayoutsForAppLayouts:]_block_invoke_2
+ ___66-[SBStripLayoutWindowingModifier adjustedAppLayoutsForAppLayouts:]_block_invoke_3
+ ___67-[SBContinuousExposeArcSwipeSwitcherModifier topMostLayoutElements]_block_invoke
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.676
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.678
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.679
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.680
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.681
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_2.687
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_3.699
+ ___68-[SBDefaultImplementationsSwitcherModifier _slideOverAppLayoutIfAny]_block_invoke
+ ___68-[SBRoutingSwitcherModifier cornerRadiusForSlideOverTongueAppLayout]_block_invoke
+ ___68-[SBRoutingSwitcherModifier cornerRadiusForSlideOverTongueAppLayout]_block_invoke_2
+ ___68-[SBStashSlideOverItemIndirectGestureWindowingModifier visibleItems]_block_invoke
+ ___70-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier willBegin]_block_invoke
+ ___70-[SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier willBegin]_block_invoke_2
+ ___70-[SBRoutingSwitcherModifier slideOverMarginForLayoutRole:inAppLayout:]_block_invoke
+ ___71-[SBFluidSwitcherViewController _layoutSlideoverTonguesWithCompletion:]_block_invoke_2
+ ___71-[SBFluidSwitcherViewController _layoutSlideoverTonguesWithCompletion:]_block_invoke_3
+ ___71-[SBFluidSwitcherViewController _layoutSlideoverTonguesWithCompletion:]_block_invoke_4
+ ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.395
+ ___72-[SBSwitcherController _ancillaryTransitionRequestForTransitionRequest:]_block_invoke_10
+ ___72-[SBSwitcherController _ancillaryTransitionRequestForTransitionRequest:]_block_invoke_9
+ ___73-[SBDashBoardHostableEntityPresentationManager dismissEntity:completion:]_block_invoke
+ ___73-[SBDashBoardHostableEntityPresentationManager presentEntityWithRequest:]_block_invoke
+ ___73-[SBDashBoardHostableEntityPresentationManager presentEntityWithRequest:]_block_invoke_2
+ ___73-[SBDashBoardHostableEntityPresentationManager presentEntityWithRequest:]_block_invoke_3
+ ___73-[SBDashBoardHostableEntityPresentationManager presentEntityWithRequest:]_block_invoke_4
+ ___73-[SBStashSlideOverItemAnimationModifier adjustedAppLayoutsForAppLayouts:]_block_invoke
+ ___73-[SBStashSlideOverItemIndirectGestureWindowingModifier gestureDidUpdate:]_block_invoke
+ ___73-[_SBFullScreenAppFloorSwitcherModifier adjustedAppLayoutsForAppLayouts:]_block_invoke_2
+ ___74-[SBContinuitySessionStoreDemoController continuitySessionDidUpdateState:]_block_invoke
+ ___74-[SBContinuitySessionStoreDemoController continuitySessionDidUpdateState:]_block_invoke_2
+ ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1103
+ ___75-[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutsToCacheSnapshots]_block_invoke
+ ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.417
+ ___75-[SBStashSlideOverItemIndirectGestureWindowingModifier _slideOverAppLayout]_block_invoke
+ ___75-[_SBFullScreenAppFloorSwitcherModifier handleSwitcherShortcutActionEvent:]_block_invoke_8
+ ___77-[SBWorkspaceApplicationSceneTransitionContext _setRequestedFrontmostEntity:]_block_invoke_5
+ ___77-[SBWorkspaceApplicationSceneTransitionContext _setRequestedFrontmostEntity:]_block_invoke_6
+ ___78-[SBContinuousExposeWindowDragContainerSwitcherModifier topMostLayoutElements]_block_invoke
+ ___78-[SBContinuousExposeWindowDragDestinationSwitcherModifier handleGestureEvent:]_block_invoke_4
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke.131
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke.36
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_2.133
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_2.43
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_3.63
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_35
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_36
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_4.66
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_5.70
+ ___80-[_SBContinuitySessionStateMachineStateStoreDemoPrep appendDescriptionToStream:]_block_invoke
+ ___80-[_SBContinuitySessionStateMachineStateStoreDemoPrep appendDescriptionToStream:]_block_invoke_2
+ ___81-[SBContinuousExposeHomeGestureSwitcherModifier adjustedAppLayoutsForAppLayouts:]_block_invoke
+ ___81-[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutToAttachSlideOverTongue]_block_invoke
+ ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.447
+ ___81-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:]_block_invoke_5
+ ___81-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:]_block_invoke_6
+ ___81-[SBSystemServiceServer _handleRequestAppSwitcherUpdateWindowingMode:fromClient:]_block_invoke
+ ___81-[SBSystemServiceServer _handleRequestAppSwitcherUpdateWindowingMode:fromClient:]_block_invoke_2
+ ___82-[SBStashSlideOverItemIndirectGestureWindowingModifier appLayoutsToCacheSnapshots]_block_invoke
+ ___83-[SBContinuousExposeRootSwitcherModifier transitionModifierForMainTransitionEvent:]_block_invoke_6
+ ___83-[SBContinuousExposeRootSwitcherModifier transitionModifierForMainTransitionEvent:]_block_invoke_7
+ ___83-[SBFlexibleWindowingWindowDragSwitcherModifier appLayoutsToCacheFullsizeSnapshots]_block_invoke
+ ___83-[SBIconController _obtainSmartStackForWidgetDiscoverabilityWithCompletionHandler:]_block_invoke.254
+ ___83-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:]_block_invoke_2
+ ___83-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:]_block_invoke_3
+ ___83-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:]_block_invoke_4
+ ___83-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:]_block_invoke_5
+ ___83-[SBMainWorkspace dismissTransientOverlayPresentationsAnimated:windowScene:filter:]_block_invoke
+ ___83-[SBMainWorkspace dismissTransientOverlayPresentationsAnimated:windowScene:filter:]_block_invoke_2
+ ___83-[SBMainWorkspace dismissTransientOverlayPresentationsAnimated:windowScene:filter:]_block_invoke_3
+ ___85-[SBTransientlyVisibleSlideOverTongueWindowingModifier _collapseAndPrepareForDismiss]_block_invoke
+ ___86-[SBDeviceApplicationSceneHandle setStatusBarForceHidden:forReason:animationSettings:]_block_invoke.38
+ ___86-[SBFluidSwitcherViewController _performKeyboardShortcutAction:targetSceneIdentifier:]_block_invoke
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.373
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.374
+ ___87-[SBContinuousExposeArcSwipeSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:]_block_invoke
+ ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.87
+ ___88-[SBStashSlideOverItemIndirectGestureWindowingModifier adjustedAppLayoutsForAppLayouts:]_block_invoke
+ ___89-[SBMainSwitcherControllerCoordinator slideOverConfigurationOnAnySwitcherForDisplayItem:]_block_invoke
+ ___90-[SBHomePeekToFullScreenTransitionModifier appLayoutsToEnsureExistForMainTransitionEvent:]_block_invoke_3
+ ___90-[SBHomePeekToFullScreenTransitionModifier appLayoutsToEnsureExistForMainTransitionEvent:]_block_invoke_4
+ ___90-[SBHomePeekToFullScreenTransitionModifier appLayoutsToEnsureExistForMainTransitionEvent:]_block_invoke_5
+ ___90-[SBHomePeekToFullScreenTransitionModifier appLayoutsToEnsureExistForMainTransitionEvent:]_block_invoke_6
+ ___90-[SBStashSlideOverItemIndirectGestureWindowingModifier appLayoutsToCacheFullsizeSnapshots]_block_invoke
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1645
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1647
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1649
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1653
+ ___91-[SBMenuBarViewController _adjustPresentedMenuForPointerOverViewInContainer:forPanGesture:]_block_invoke
+ ___92-[SBRoutingSwitcherModifier frameForIndexOffsetToCounteractSwitcherWindowMatchMoveForIndex:]_block_invoke
+ ___92-[SBRoutingSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:]_block_invoke
+ ___93-[SBBannerManager _acquireGestureRecognizerPriorityAssertionWithPriority:windowScene:reason:]_block_invoke.228
+ ___93-[SBBannerManager _acquireGestureRecognizerPriorityAssertionWithPriority:windowScene:reason:]_block_invoke_2.229
+ ___95-[SBSwitcherController _buildWindowArrangementMenuForKeyCommandRegistration:additionalOptions:]_block_invoke_8
+ ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke.398
+ ___97-[SBSwitcherController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:]_block_invoke
+ ___97-[SBSwitcherController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:]_block_invoke_2
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1776
+ ___98-[SBAppSwitcherSystemService systemServiceServer:requestUpdateWindowingMode:forClient:completion:]_block_invoke
+ ___SBDisplayItemDescendingInteractionTimeComparator_block_invoke
+ ____SBHIDDispatchPredicateExcludingAssociatedDisplays_block_invoke
+ ___blockIMPFromContextSignature103_block_invoke
+ ___blockIMPFromEventSignature103_block_invoke
+ ___blockIMPFromQuerySignature103_block_invoke
+ ___block_descriptor_137_e8_32s40s48s56s64s72s80s88s96s_e38_B16?0"SBFluidSwitcherItemContainer"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_144_e8_32s40s48s56s_e33_v16?0?<?<v?BB>?"NSString">8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_160_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_184_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_224_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_32_e39_B16?0"SBDisplayItemLayoutAttributes"8l
+ ___block_descriptor_32_e42_B16?0"SBTransientOverlayViewController"8l
+ ___block_descriptor_40_e21_B16?0"SBAppLayout"8l
+ ___block_descriptor_40_e33_v16?0"FBSMutableSceneSettings"8l
+ ___block_descriptor_40_e8_32r_e25_B16?0"SBLayoutElement"8lr32l8
+ ___block_descriptor_40_e8_32s_e25_16?0"SBLayoutElement"8ls32l8
+ ___block_descriptor_40_e8_32w_e48_v16?0"SBSceneHandleActiveAppearanceAssertion"8lw32l8
+ ___block_descriptor_48_e138_{SBWindowControlsLayout=qB{CGPoint=dd}}88?0"SBChainableModifier"816{CGRect={CGPoint=dd}{CGSize=dd}}24{CGRect={CGPoint=dd}{CGSize=dd}}56l
+ ___block_descriptor_48_e60_{CGPoint=dd}48?0"SBChainableModifier"8q1624{CGPoint=dd}32l
+ ___block_descriptor_48_e8_32r_e55_v32?0"SBSceneHandleActiveAppearanceAssertion"8Q16^B24lr32l8
+ ___block_descriptor_48_e8_32s40s_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e34_v24?0"SBSwitcherController"8^B16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e21_16?0"SBAppLayout"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e28_v32?0"SBAppLayout"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48bs_e42_B16?0"SBMainWorkspaceTransitionRequest"8ls48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e17_v16?0"NSArray"8lr48l8s32l8s40l8r56l8r64l8
+ ___block_descriptor_73_e8_32s40s48r56r64r_e8_v16?0q8ls32l8s40l8r48l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40bs48r_e36_v32?0"SBChainableModifier"8Q16^B24ls40l8s32l8r48l8
+ ___block_descriptor_80_e8_32s40s48r56r64r72r_e8_v16?0q8ls32l8s40l8r48l8r56l8r64l8r72l8
+ ___block_descriptor_80_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e34_v24?0"SBSwitcherController"8^B16ls32l8s40l8s48l8s56l8s64l8r72l8
+ ___block_descriptor_96_e8_32s40s_e76_v24?0"SBDisplayItemLayoutAttributesKey"8"SBDisplayItemLayoutAttributes"16ls32l8s40l8
+ ___block_literal_global.1117
+ ___block_literal_global.1195
+ ___block_literal_global.1243
+ ___block_literal_global.129
+ ___block_literal_global.141
+ ___block_literal_global.143
+ ___block_literal_global.159
+ ___block_literal_global.161
+ ___block_literal_global.1619
+ ___block_literal_global.1623
+ ___block_literal_global.165
+ ___block_literal_global.1655
+ ___block_literal_global.1664
+ ___block_literal_global.1666
+ ___block_literal_global.1668
+ ___block_literal_global.167
+ ___block_literal_global.1670
+ ___block_literal_global.1686
+ ___block_literal_global.1802
+ ___block_literal_global.1825
+ ___block_literal_global.1834
+ ___block_literal_global.1850
+ ___block_literal_global.194
+ ___block_literal_global.198
+ ___block_literal_global.210
+ ___block_literal_global.218
+ ___block_literal_global.245
+ ___block_literal_global.255
+ ___block_literal_global.264
+ ___block_literal_global.278
+ ___block_literal_global.287
+ ___block_literal_global.293
+ ___block_literal_global.300
+ ___block_literal_global.303
+ ___block_literal_global.332
+ ___block_literal_global.338
+ ___block_literal_global.339
+ ___block_literal_global.348
+ ___block_literal_global.350
+ ___block_literal_global.354
+ ___block_literal_global.359
+ ___block_literal_global.366
+ ___block_literal_global.371
+ ___block_literal_global.381
+ ___block_literal_global.392
+ ___block_literal_global.399
+ ___block_literal_global.493
+ ___block_literal_global.496
+ ___block_literal_global.505
+ ___block_literal_global.508
+ ___block_literal_global.552
+ ___block_literal_global.557
+ ___block_literal_global.561
+ ___block_literal_global.592
+ ___block_literal_global.600
+ ___block_literal_global.605
+ ___block_literal_global.607
+ ___block_literal_global.609
+ ___block_literal_global.622
+ ___block_literal_global.673
+ ___block_literal_global.683
+ ___block_literal_global.689
+ ___block_literal_global.727
+ ___block_literal_global.74
+ ___block_literal_global.753
+ ___block_literal_global.765
+ __sceneManagerForDisplayIdentity:creatingIfNecessary:.___once.86
+ _blockIMPFromContextSignature103
+ _blockIMPFromEventSignature103
+ _blockIMPFromQuerySignature103
+ _kCAFilterGlassBackground
+ _kCAFilterInputBleedAmount
+ _kCAFilterInputBleedBlurRadius
+ _kCAFilterInputBleedColorMatrixBlack
+ _kCAFilterInputBleedColorMatrixFillColor
+ _kCAFilterInputBleedColorMatrixSaturation
+ _kCAFilterInputBleedColorMatrixWhite
+ _kCAFilterInputBleedDarkenBlend
+ _kCAFilterInputBleedDistance0
+ _kCAFilterInputBleedDistance1
+ _kCAFilterInputBleedHeight
+ _kCAFilterInputBleedOpacity
+ _kCAFilterInputBlurDistance0
+ _kCAFilterInputBlurDistance1
+ _kCAFilterInputBlurDistance2
+ _kCAFilterInputBlurDistance3
+ _kCAFilterInputBlurDistance4
+ _kCAFilterInputBlurOpacity0
+ _kCAFilterInputBlurOpacity1
+ _kCAFilterInputBlurOpacity2
+ _kCAFilterInputBlurOpacity3
+ _kCAFilterInputBlurOpacity4
+ _kCAFilterInputBlurRadius
+ _kCAFilterInputFaceColorMatrixBlack
+ _kCAFilterInputFaceColorMatrixFillColor
+ _kCAFilterInputFaceColorMatrixSaturation
+ _kCAFilterInputFaceColorMatrixWhite
+ _kCAFilterInputFaceOpacity
+ _kCAFilterInputInnerRefractionAmount
+ _kCAFilterInputInnerRefractionHeight
+ _kCAFilterInputOuterRefractionAmount
+ _kCAFilterInputOuterRefractionHeight
+ _kCAFilterInputRefractionDistance0
+ _kCAFilterInputRefractionDistance1
+ _kCAFilterInputRefractionOpacity
+ _kCAFilterInputShadowOpacity
+ _kCFUserNotificationAlertAccessibilityIdentifierKey
+ _kCFUserNotificationAlternateButtonAccessibilityIdentifierKey
+ _kCFUserNotificationDefaultButtonAccessibilityIdentifierKey
+ _kCFUserNotificationOtherButtonAccessibilityIdentifierKey
+ _kSBSAppSwitcherServiceWindowingMode
+ _objc_msgSend$_adjustPresentedMenuForPointerOverViewInContainer:forPanGesture:
+ _objc_msgSend$_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:layoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:
+ _objc_msgSend$_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:usingNewLayoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:
+ _objc_msgSend$_collapseAndPrepareForDismiss
+ _objc_msgSend$_collapseSettlingDuration
+ _objc_msgSend$_computeActiveAppearance
+ _objc_msgSend$_currentSlideOverConfiguration
+ _objc_msgSend$_draggingItemScreenCenterForSize:scale:
+ _objc_msgSend$_effectiveHomeAffordanceViewFrame
+ _objc_msgSend$_effectiveIndexInRecencyOfAppLayout:
+ _objc_msgSend$_effectiveStageAreaForSnappingItem:inSpace:configuration:
+ _objc_msgSend$_flexibleAutoLayoutSpaceForStripAppLayout:
+ _objc_msgSend$_handleMenuPanGesture:
+ _objc_msgSend$_handleRequestAppSwitcherUpdateWindowingMode:fromClient:
+ _objc_msgSend$_inSlideOver
+ _objc_msgSend$_initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:slideOverConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:
+ _objc_msgSend$_initializeSlideOverDisplayItemIfNeededForcingStashed:
+ _objc_msgSend$_innerLeftEdgeDragHitTestRectForItemContainer:forPointerTouch:
+ _objc_msgSend$_innerRightEdgeDragHitTestRectForItemContainer:forPointerTouch:
+ _objc_msgSend$_isDockVisibleForBoundingBox:configuration:slideOverItem:
+ _objc_msgSend$_isStripVisibleForBoundingBox:configuration:effectiveStripWidth:slideOverItem:
+ _objc_msgSend$_isUnpinGestureAllowedToMoveWindowsAtLocationInReferenceCoordinateSpace:withinUnstashLocationOnHomeScreen:
+ _objc_msgSend$_keyboardInsetsForWindowScene:
+ _objc_msgSend$_layOutSlideOverItemFullyOffscreen
+ _objc_msgSend$_lightGlassBackgroundFilterParameters
+ _objc_msgSend$_lightKeyFillVibrantColorMatrix
+ _objc_msgSend$_managedMainDisplayItems
+ _objc_msgSend$_modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:
+ _objc_msgSend$_moveDisplayItemOutOfSlideOver:
+ _objc_msgSend$_moveDisplayItemToSlideOver:
+ _objc_msgSend$_performToggleSlideOverForDisplayItemResponse:
+ _objc_msgSend$_reevaluateActiveAppearanceFromAssertions
+ _objc_msgSend$_responseForGestureEnd:
+ _objc_msgSend$_safeAreaCornerInsetResolverForApplicationFrame:screenBounds:activationSettings:
+ _objc_msgSend$_shouldLockYPosition
+ _objc_msgSend$_sizeForAttributedSize:inBounds:defaultSize:screenEdgePadding:
+ _objc_msgSend$_slideOverAppLayout
+ _objc_msgSend$_slideOverAppLayoutIfAny
+ _objc_msgSend$_slideOverCenterExitingTimerWaitingWhileStillCloseWithCenter:
+ _objc_msgSend$_slideOverDisplayItem
+ _objc_msgSend$_slideOverLeafAppLayout
+ _objc_msgSend$_snapPositionOfItem:ifNecessaryInSpace:autoLayoutConfiguration:snappedEdgesMask:
+ _objc_msgSend$_snapPositionOfItem:toRect:inSpace:autoLayoutConfiguration:considerAdjacency:snappedEdgesMask:itemForPotentialPairing:
+ _objc_msgSend$_snapSizeOfItem:ifNecessaryForSpace:configuration:snappedEdgesMask:
+ _objc_msgSend$_snapSizeOfItem:toRect:inSpace:windowingConfiguration:considerAdjacency:snappedEdgesMask:newFrame:
+ _objc_msgSend$_stageAreaForBoundingBox:configuration:effectiveStripWidth:slideOverItem:
+ _objc_msgSend$_touchIsWithinUnstashRegionOnHomeScreen:
+ _objc_msgSend$_touchLocationIsWithinSlideOverTongue:
+ _objc_msgSend$_touchLocationIsWithinUnstashRegion:
+ _objc_msgSend$_updateClientWantsMotionEventState
+ _objc_msgSend$_updateInterfaceActiveAppearance
+ _objc_msgSend$_updateSlideOverGlass
+ _objc_msgSend$_updateWithInterfaceStyle:
+ _objc_msgSend$_windowSceneForZStackParticipant:
+ _objc_msgSend$acquireActiveAppearanceAssertionWithReason:activeAppearance:priority:
+ _objc_msgSend$addSDFElementView:
+ _objc_msgSend$allowCameraButtonDeferringWhileFocusLocked
+ _objc_msgSend$allowsKeyboardArbiterToDetermineFocusTarget
+ _objc_msgSend$appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:options:containerOrientation:floatingDockHeight:screenScale:bounds:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:
+ _objc_msgSend$appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:usingLayoutAttributes:options:containerOrientation:windowScene:source:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:
+ _objc_msgSend$beginNewRootFolderContentSession
+ _objc_msgSend$centerForLayoutAttributes:windowingConfiguration:
+ _objc_msgSend$configureIconManager:
+ _objc_msgSend$controlCenterDidAppear
+ _objc_msgSend$cornerRadiusForSlideOverTongueAppLayout
+ _objc_msgSend$coverSheetSlidingViewControllerDidEndDismissGestureOverInterstitial:
+ _objc_msgSend$coverSheetSlidingViewControllerIsInterstitialDismissalAllowed:
+ _objc_msgSend$defaultWindowControlsLayoutForDisplayItem:frame:containerBounds:
+ _objc_msgSend$didEdgeProtectSlideOverTongue:
+ _objc_msgSend$dismissGestureEnabled
+ _objc_msgSend$dismissTransientOverlayPresentationsAnimated:windowScene:filter:
+ _objc_msgSend$displayItemInSlideOver
+ _objc_msgSend$displayItemsToExcludeFromStrip
+ _objc_msgSend$entityForIdentifier:
+ _objc_msgSend$flexibleAutoLayoutSpaceForAppLayout:calculatedUsingNewLayoutAttributesMap:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:
+ _objc_msgSend$flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:floatingDockHeight:screenScale:bounds:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
+ _objc_msgSend$flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:floatingDockHeight:screenScale:bounds:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:newLayoutAttributes:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:
+ _objc_msgSend$frameForIndexOffsetToCounteractSwitcherWindowMatchMoveForIndex:
+ _objc_msgSend$frameForLayoutRole:inAppLayout:containerBounds:containerOrientation:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
+ _objc_msgSend$frameForSlideOverTongueAppLayout
+ _objc_msgSend$hitTestedToHomeAffordance:window:ofItemContainer:
+ _objc_msgSend$hitTestedToSlideOverTongue:window:
+ _objc_msgSend$initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:storeDemoModeController:
+ _objc_msgSend$initWithDisplayItem:direction:
+ _objc_msgSend$initWithEntity:transitionRequest:animated:isEphemeralSwitcher:dismissGestureEnabled:presentationCompletion:
+ _objc_msgSend$initWithFromAppLayout:toAppLayout:
+ _objc_msgSend$initWithGestureID:initialAppLayout:selectedDisplayItem:wantsSlideOverTongue:slideOverTongueState:slideOverTongueDirection:
+ _objc_msgSend$initWithMenuBarViewController:
+ _objc_msgSend$initWithReason:activeAppearance:priority:invalidationBlock:
+ _objc_msgSend$initWithSafeAreaCornerInsets:
+ _objc_msgSend$initWithSafeAreaEdgeInsets:
+ _objc_msgSend$initWithSafeAreaEdgeInsetsForPortrait:landscape:
+ _objc_msgSend$initWithStoreDemoPrepState:blockedState:preparingForRemoteUnlockState:waitingForRemoteUnlockState:waitingForScenesState:waitingForHIDServicesState:activatingState:updatingActiveDisplayState:launchingState:flushingState:activeState:
+ _objc_msgSend$initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:inStoreDemoMode:
+ _objc_msgSend$initWithTonguePresentationReason:
+ _objc_msgSend$isDockVisible
+ _objc_msgSend$isInSlideOver
+ _objc_msgSend$isInStoreDemoMode
+ _objc_msgSend$isMenuBarBecomingVisible
+ _objc_msgSend$isOccludingSystemContent
+ _objc_msgSend$isRotationTransition
+ _objc_msgSend$isUnstashFromHomeTransition
+ _objc_msgSend$knownCameraCaptureApplicationsByBundleIdentifier
+ _objc_msgSend$lastInteractedDisplayItemsInAppLayout:orientation:
+ _objc_msgSend$lastInteractedItemsInAppLayout:
+ _objc_msgSend$noteStoreDemoLockFailed
+ _objc_msgSend$overrideKeyboardFocusTarget
+ _objc_msgSend$perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:
+ _objc_msgSend$posterDeviceMotionMode
+ _objc_msgSend$prefersZoomDownAnimation
+ _objc_msgSend$prepareForTransitionToPresented:reversingTransition:forUserGesture:
+ _objc_msgSend$presentEntityWithRequest:
+ _objc_msgSend$presentationCompletion
+ _objc_msgSend$previousEntityForIdentifier:
+ _objc_msgSend$quickCameraDidAppear
+ _objc_msgSend$safeAreaCornerInsetResolver
+ _objc_msgSend$safeAreaEdgeInsetResolver
+ _objc_msgSend$safeAreaEdgeInsetResolverForApplicationFrame:screenBounds:activationSettings:
+ _objc_msgSend$safeAreaEdgeInsetsForOrientation:
+ _objc_msgSend$sceneRelevancyHint
+ _objc_msgSend$setAlertAccessibilityIdentifier:
+ _objc_msgSend$setAllowsKeyboardArbiterToDetermineFocusTarget:
+ _objc_msgSend$setAlternateButtonAccessibilityIdentifier:
+ _objc_msgSend$setCurvature:
+ _objc_msgSend$setDefaultButtonAccessibilityIdentifier:
+ _objc_msgSend$setDeviceMotionMode:
+ _objc_msgSend$setDockVisible:
+ _objc_msgSend$setFillAmount:
+ _objc_msgSend$setFillAngle:
+ _objc_msgSend$setFillHeight:
+ _objc_msgSend$setFillSpread:
+ _objc_msgSend$setGlobal:
+ _objc_msgSend$setGradientOvalization:
+ _objc_msgSend$setInSlideOver:
+ _objc_msgSend$setKeyAmount:
+ _objc_msgSend$setKeyAngle:
+ _objc_msgSend$setKeyHeight:
+ _objc_msgSend$setKeySpread:
+ _objc_msgSend$setLimitsWidgetStackPageControlFlashesToSession:
+ _objc_msgSend$setMenuBarBecomingVisible:
+ _objc_msgSend$setNeedsUpdateZStackPreferencesWithReason:
+ _objc_msgSend$setOtherButtonAccessibilityIdentifier:
+ _objc_msgSend$setOverrideKeyboardFocusTarget:
+ _objc_msgSend$setPasscodeLockVisible:animated:showBackground:forceBiometricPresentation:completion:
+ _objc_msgSend$setPosterClientDeviceMotionMode:
+ _objc_msgSend$setPrefersZoomDownAnimation:
+ _objc_msgSend$setSafeAreaCornerInsetResolver:
+ _objc_msgSend$setSafeAreaEdgeInsetResolver:
+ _objc_msgSend$setSceneRelevancyHint:
+ _objc_msgSend$setShouldActivateWithThresholdForTrackpad:
+ _objc_msgSend$setSlideOverBorderWidth:
+ _objc_msgSend$setSlideOverEnterCenterRegionThreshold:
+ _objc_msgSend$setSlideOverExitCenterRegionThreshold:
+ _objc_msgSend$setSlideOverMargin:
+ _objc_msgSend$setSlideOverThresholdToForegroundUnstashingApp:
+ _objc_msgSend$setSlideOverTonguePortalSourceView:
+ _objc_msgSend$setSmoothness:
+ _objc_msgSend$setSuppressCameraButtonDeferringToApplications:
+ _objc_msgSend$setUnstashFromHomeTransition:
+ _objc_msgSend$setUnstashingFromHome:
+ _objc_msgSend$shouldIgnoreReducedMotionChange
+ _objc_msgSend$shouldSuppressAlertContentOnHostApplication
+ _objc_msgSend$sizeForLayoutAttributes:windowingConfiguration:
+ _objc_msgSend$sizeForSlideOverConfiguration:windowingConfiguration:
+ _objc_msgSend$slideOverBorderWidth
+ _objc_msgSend$slideOverConfigurationOnAnySwitcherForDisplayItem:
+ _objc_msgSend$slideOverEnterCenterRegionThreshold
+ _objc_msgSend$slideOverExitCenterRegionThreshold
+ _objc_msgSend$slideOverIsCenterExiting
+ _objc_msgSend$slideOverMargin
+ _objc_msgSend$slideOverMarginForLayoutRole:inAppLayout:
+ _objc_msgSend$slideOverThresholdToForegroundUnstashingApp
+ _objc_msgSend$slideOverTongueModifierForRoutingModifier:
+ _objc_msgSend$slideOverTonguePortalSourceView
+ _objc_msgSend$sourceLayer
+ _objc_msgSend$spaceByPerformingFlexibleAutoLayoutWithSpace:configuration:options:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:
+ _objc_msgSend$suppressCameraButtonDeferringToApplications
+ _objc_msgSend$switcherContentController:moveDisplayItemOutOfSlideOver:
+ _objc_msgSend$switcherContentController:moveDisplayItemToSlideOver:
+ _objc_msgSend$systemServiceServer:requestUpdateWindowingMode:forClient:completion:
+ _objc_msgSend$unstashingFromHome
+ _objc_msgSend$updateLayoutAttributes:ofDisplayItem:
+ _objc_msgSend$updateLayoutAttributes:ofDisplayItem:displayOrdinal:orientation:
+ _objc_msgSend$updatedSlideOverConfigurationForItemWithSize:center:slideOverConfiguration:windowingConfiguration:
+ _objc_msgSend$windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:
+ _objc_msgSend$windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:
+ _objc_msgSend$windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:
- +[SBTransientlyVisibleSlideOverTongueSwitcherModifier slideOverTongueTransientlyVisibleModeForEvent:]
- -[FBSSceneSettings(SBUISceneSafeAreaSettings) sb_safeAreaSettings]
- -[SBAppSwitcherContinuousExposeSwitcherModifier appLayoutToAttachSlideOverTongue]
- -[SBAppSwitcherContinuousExposeSwitcherModifier slideOverTongueDirection]
- -[SBAppSwitcherContinuousExposeSwitcherModifier slideOverTongueState]
- -[SBAppSwitcherContinuousExposeSwitcherModifier wantsSlideOverTongue]
- -[SBContinuitySession initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:]
- -[SBContinuitySession initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:].cold.1
- -[SBContinuitySession initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:].cold.2
- -[SBContinuitySession initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:].cold.3
- -[SBContinuitySession initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:].cold.4
- -[SBContinuousExposeHomeGestureSwitcherModifier isContentStatusBarVisibleForIndex:]
- -[SBContinuousExposeRootSwitcherModifier _topMostDisplayItemInDisplayItemLayoutAttributesMap:]
- -[SBContinuousExposeWindowDragContentSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:]
- -[SBCoverSheetPresentationManager coverSheetSlidingViewControllerCleanupInterstitialWhileOffScreen:]
- -[SBCoverSheetPresentationManager coverSheetSlidingViewControllerIsInterstitialAllowed:]
- -[SBDashBoardHostableEntityHostingFluidSwitcherViewController entity]
- -[SBDashBoardHostableEntityPresentationManager presentEntity:fromRequest:animated:withEphemeralSwitcher:dismissGestureEnabled:completion:]
- -[SBDeckFloatingSwitcherModifier appLayoutToAttachSlideOverTongue]
- -[SBDeckFloatingSwitcherModifier slideOverTongueDirection]
- -[SBDeckFloatingSwitcherModifier slideOverTongueState]
- -[SBDeckFloatingSwitcherModifier wantsSlideOverTongue]
- -[SBDeckSwitcherModifier appLayoutToAttachSlideOverTongue]
- -[SBDeckSwitcherModifier slideOverTongueDirection]
- -[SBDeckSwitcherModifier slideOverTongueState]
- -[SBDeckSwitcherModifier wantsSlideOverTongue]
- -[SBDefaultImplementationsSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:]
- -[SBDeviceApplicationSceneHandle _safeAreaCornerInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]
- -[SBDeviceApplicationSceneHandle _updateInterfaceAppearance]
- -[SBDeviceApplicationSceneHandle activeAppearance]
- -[SBDeviceApplicationSceneHandle safeAreaEdgeInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]
- -[SBDeviceApplicationSceneHandle setActiveAppearance:]
- -[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]
- -[SBDisplayItemLayoutAttributes _initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:]
- -[SBDisplayItemLayoutAttributes _sizeForAttributedSize:inBounds:defaultSize:screenEdgePadding:sizingPolicy:dockHeightWithPadding:interItemSpacing:]
- -[SBDisplayItemLayoutAttributes centerInBounds:dockHeightIncludingPadding:interItemSpacing:]
- -[SBDisplayItemLayoutAttributes initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:]
- -[SBDisplayItemLayoutAttributes sizeInBounds:defaultSize:screenEdgePadding:dockHeightIncludingPadding:interItemSpacing:]
- -[SBDisplayItemLayoutAttributesCalculator _appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:layoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
- -[SBDisplayItemLayoutAttributesCalculator _appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:usingNewLayoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
- -[SBDisplayItemLayoutAttributesCalculator appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
- -[SBDisplayItemLayoutAttributesCalculator appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:usingLayoutAttributes:options:containerOrientation:windowScene:source:]
- -[SBDisplayItemLayoutAttributesCalculator flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
- -[SBDisplayItemLayoutAttributesCalculator flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:newLayoutAttributes:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
- -[SBDisplayItemLayoutAttributesCalculator frameForLayoutRole:inAppLayout:containerBounds:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
- -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]
- -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.1
- -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.2
- -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.3
- -[SBDockToStageZoomWindowingModifier _topMostDisplayItemInDisplayItemLayoutAttributesMap:]
- -[SBExposeWindowingModifier appLayoutToAttachSlideOverTongue]
- -[SBExposeWindowingModifier slideOverTongueDirection]
- -[SBExposeWindowingModifier slideOverTongueState]
- -[SBExposeWindowingModifier wantsSlideOverTongue]
- -[SBFlexibleWindowingAutoLayoutController _effectiveStageAreaForSnappingForSpace:configuration:]
- -[SBFlexibleWindowingAutoLayoutController _isStripVisibleForBoundingBox:configuration:effectiveStripWidth:]
- -[SBFlexibleWindowingAutoLayoutController _snapPositionOfTopMostItemIfNecessaryInSpace:autoLayoutConfiguration:snappedEdgesMask:]
- -[SBFlexibleWindowingAutoLayoutController _snapPositionOfTopMostItemToRect:inSpace:autoLayoutConfiguration:considerAdjacency:snappedEdgesMask:itemForPotentialPairing:]
- -[SBFlexibleWindowingAutoLayoutController _snapSizeOfResizingDisplayItemIfNecessaryForSpace:configuration:snappedEdgesMask:]
- -[SBFlexibleWindowingAutoLayoutController _snapSizeOfResizingDisplayItemToRect:inSpace:windowingConfiguration:considerAdjacency:snappedEdgesMask:newFrame:]
- -[SBFlexibleWindowingAutoLayoutController _stageAreaForBoundingBox:configuration:effectiveStripWidth:]
- -[SBFlexibleWindowingAutoLayoutController spaceByPerformingFlexibleAutoLayoutWithSpace:configuration:options:source:]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier isContentStatusBarVisibleForIndex:]
- -[SBFlexibleWindowingHomeGestureSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:]
- -[SBFlexibleWindowingWindowDragSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:]
- -[SBFlexibleWindowingWindowDragSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:].cold.1
- -[SBFlexibleWindowingWindowDragSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:].cold.2
- -[SBFluidSwitcherGestureManager _floatingConfigurationForActivatedEdge:]
- -[SBFluidSwitcherGestureManager _isUnpinGestureAllowedToMoveWindowsAtLocationInReferenceCoordinateSpace:]
- -[SBFluidSwitcherViewController _modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:]
- -[SBFluidSwitcherViewController defaultWindowControlsLayoutForDisplayItem:frame:containerBounds:interfaceOrientation:]
- -[SBFluidSwitcherViewController updateLayoutAttributes:ofDisplayItem:inAppLayout:]
- -[SBHomePeekToFullScreenTransitionModifier perspectiveAngleForLayoutRole:inAppLayout:]
- -[SBHomePeekWindowingModifier perspectiveAngleForLayoutRole:inAppLayout:]
- -[SBInCallPresentationSession assistantDidDisappear:windowScene:]
- -[SBIndirectPanGestureRecognizer setShouldActivateWithThreshold:]
- -[SBIndirectPanGestureRecognizer shouldActivateWithThreshold]
- -[SBKeyboardFocusPolicy cameraIsHosted]
- -[SBKeyboardFocusResolutionContext isSiriVisible]
- -[SBKeyboardFocusResolutionContext isSpotlightVisible]
- -[SBKeyboardFocusSceneController activeTransientOverlayPresentationCanBecomeFirstResponder]
- -[SBKeyboardFocusSceneController activeTransientOverlayPresentationShouldUseSceneBasedKeyboardFocus]
- -[SBKeyboardFocusSceneController focusTargetForActiveTransientOverlayPresentation]
- -[SBKeyboardFocusSceneController focusTargetForCoverSheetHostedAppGetCameraIsHosted:]
- -[SBKeyboardFocusSceneController hasActiveTransientOverlayPresentation]
- -[SBKeyboardFocusSceneController isActiveTransientOverlayPresentationFromSceneWithIdentityTokenString:]
- -[SBKeyboardFocusSceneController isBannerKitHostingSceneWithIdentityTokenString:]
- -[SBKeyboardFocusSceneController isSpolightPresentedAsTransientOverlay]
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.1
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.10
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.11
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.12
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.13
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.14
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.15
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.16
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.17
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.18
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.19
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.2
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.20
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.21
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.22
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.23
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.24
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.25
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.26
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.27
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.28
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.29
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.3
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.30
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.31
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.32
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.33
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.34
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.35
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.36
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.37
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.38
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.4
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.5
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.6
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.7
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.8
- -[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:].cold.9
- -[SBMenuBarMainMenuView _handleTapOnClosedMenu:]
- -[SBMenuBarMainMenuView alongsidePresentTapRecognizer]
- -[SBMenuBarMainMenuView setAlongsidePresentTapRecognizer:]
- -[SBMenuBarManager systemQuitMenuWithOptions:]
- -[SBMutableKeyboardFocusPolicy setCameraIsHosted:]
- -[SBMutableKeyboardFocusResolutionContext setSiriVisible:]
- -[SBMutableKeyboardFocusResolutionContext setSpotlightVisible:]
- -[SBRoutingSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:]
- -[SBShelfCarouselSwitcherModifier appLayoutToAttachSlideOverTongue]
- -[SBShelfCarouselSwitcherModifier slideOverTongueDirection]
- -[SBShelfCarouselSwitcherModifier slideOverTongueState]
- -[SBShelfCarouselSwitcherModifier wantsSlideOverTongue]
- -[SBSlideOverTongueView _updateContainerPosition]
- -[SBSpringBoardFocusLockResolutionStage resolveKeyboardFocusPolicy:context:stop:].cold.1
- -[SBSpringBoardFocusLockResolutionStage resolveKeyboardFocusPolicy:context:stop:].cold.2
- -[SBSpringBoardFocusLockResolutionStage resolveKeyboardFocusPolicy:context:stop:].cold.3
- -[SBSpringBoardFocusLockResolutionStage resolveKeyboardFocusPolicy:context:stop:].cold.4
- -[SBSpringBoardFocusLockResolutionStage resolveKeyboardFocusPolicy:context:stop:].cold.5
- -[SBSwitcherController _buildQuitMenuWithAdditionalOptions:]
- -[SBSwitcherController quitMenuWithOptions:]
- -[SBSwitcherModifier(SharedModifierUtilities) flexibleAutoLayoutSpaceForAppLayout:calculatedUsingNewLayoutAttributesMap:flexibleAutoLayoutSource:]
- -[SBSwitcherTransitionRequest bundleIdentifierOfAppToKillGracefully]
- -[SBSwitcherTransitionRequest setBundleIdentifierOfAppToKillGracefully:]
- -[SBSwitcherWindowingSettings windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:]
- -[SBTransientlyVisibleSlideOverTongueSwitcherModifier handleGestureEvent:]
- -[SBTransientlyVisibleSlideOverTongueSwitcherModifier handleSlideOverEdgeProtectTongueEvent:]
- -[SBTransientlyVisibleSlideOverTongueSwitcherModifier handleTimerEvent:]
- -[SBTransientlyVisibleSlideOverTongueSwitcherModifier handleTransitionEvent:]
- -[SBTransientlyVisibleSlideOverTongueSwitcherModifier initWithMode:]
- -[SBTransientlyVisibleSlideOverTongueSwitcherModifier initWithMode:].cold.1
- -[SBTransientlyVisibleSlideOverTongueSwitcherModifier mode]
- -[SBTransientlyVisibleSlideOverTongueSwitcherModifier slideOverTongueDirection]
- -[SBTransientlyVisibleSlideOverTongueSwitcherModifier slideOverTongueState]
- -[SpringBoard _handleRemoveAllWindowFromSetAndQuitShortcut:]
- -[_SBActiveAppFloorFloatingSwitcherModifier appLayoutToAttachSlideOverTongue]
- -[_SBActiveAppFloorFloatingSwitcherModifier slideOverTongueDirection]
- -[_SBActiveAppFloorFloatingSwitcherModifier slideOverTongueState]
- -[_SBActiveAppFloorFloatingSwitcherModifier wantsSlideOverTongue]
- -[_SBContinuitySessionStateMachine initWithBlockedState:preparingForRemoteUnlockState:waitingForRemoteUnlockState:waitingForScenesState:waitingForHIDServicesState:activatingState:updatingActiveDisplayState:launchingState:flushingState:activeState:]
- -[_SBContinuitySessionStateMachine initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:]
- -[_SBFullScreenAppFloorSwitcherModifier appLayoutToAttachSlideOverTongue]
- -[_SBFullScreenAppFloorSwitcherModifier slideOverTongueDirection]
- -[_SBFullScreenAppFloorSwitcherModifier slideOverTongueState]
- -[_SBFullScreenAppFloorSwitcherModifier wantsSlideOverTongue]
- -[_SBGridFloorSwitcherModifier appLayoutToAttachSlideOverTongue]
- -[_SBGridFloorSwitcherModifier slideOverTongueDirection]
- -[_SBGridFloorSwitcherModifier slideOverTongueState]
- -[_SBGridFloorSwitcherModifier wantsSlideOverTongue]
- -[_SBHomeScreenFloorSwitcherModifier appLayoutToAttachSlideOverTongue]
- -[_SBHomeScreenFloorSwitcherModifier slideOverTongueDirection]
- -[_SBHomeScreenFloorSwitcherModifier slideOverTongueState]
- -[_SBHomeScreenFloorSwitcherModifier wantsSlideOverTongue]
- -[_SBKeyboardFocusContinuitySceneControllerDependencies focusTargetForCoverSheetHostedAppGetCameraIsHosted:]
- -[_SBKeyboardFocusSceneControllerDependenciesBase activeTransientOverlayPresentationCanBecomeFirstResponder]
- -[_SBKeyboardFocusSceneControllerDependenciesBase activeTransientOverlayPresentationShouldUseSceneBasedKeyboardFocus]
- -[_SBKeyboardFocusSceneControllerDependenciesBase focusTargetForActiveTransientOverlayPresentation]
- -[_SBKeyboardFocusSceneControllerDependenciesBase focusTargetForCoverSheetHostedAppGetCameraIsHosted:]
- -[_SBKeyboardFocusSceneControllerDependenciesBase hasActiveTransientOverlayPresentation]
- -[_SBKeyboardFocusSceneControllerDependenciesBase isActiveTransientOverlayPresentationIsFromSceneWithIdentityTokenString:]
- -[_SBKeyboardFocusSceneControllerDependenciesBase isBannerKitHostingSceneWithIdentityTokenString:]
- -[_SBKeyboardFocusSceneControllerDependenciesBase isSpolightPresentedAsTransientOverlay]
- GCC_except_table153
- GCC_except_table161
- GCC_except_table184
- GCC_except_table205
- GCC_except_table221
- GCC_except_table255
- GCC_except_table370
- GCC_except_table407
- GCC_except_table452
- GCC_except_table456
- GCC_except_table458
- GCC_except_table461
- GCC_except_table462
- GCC_except_table464
- GCC_except_table485
- GCC_except_table489
- GCC_except_table515
- GCC_except_table530
- GCC_except_table534
- GCC_except_table538
- GCC_except_table544
- GCC_except_table548
- GCC_except_table572
- GCC_except_table618
- GCC_except_table653
- GCC_except_table723
- GCC_except_table747
- GCC_except_table750
- GCC_except_table791
- GCC_except_table831
- GCC_except_table870
- GCC_except_table92
- GCC_except_table925
- GCC_except_table964
- GCC_except_table971
- GCC_except_table973
- GCC_except_table975
- GCC_except_table977
- GCC_except_table979
- _OBJC_CLASS_$_SBTransientlyVisibleSlideOverTongueSwitcherModifier
- _OBJC_IVAR_$_SBContinuousExposeArcSwipeSwitcherModifier._initialVisibleAppLayouts
- _OBJC_IVAR_$_SBDashBoardHostableEntityHostingFluidSwitcherViewController._displayItem
- _OBJC_IVAR_$_SBDashBoardHostableEntityHostingFluidSwitcherViewController._entity
- _OBJC_IVAR_$_SBDeviceApplicationSceneHandle._activeAppearance
- _OBJC_IVAR_$_SBFullScreenContinuousExposeSwitcherModifier._bundleIDShowingInlineAppExpose
- _OBJC_IVAR_$_SBIndirectPanGestureRecognizer._shouldActivateWithThreshold
- _OBJC_IVAR_$_SBKeyboardFocusPolicy._cameraIsHosted
- _OBJC_IVAR_$_SBKeyboardFocusResolutionContext._siriVisible
- _OBJC_IVAR_$_SBKeyboardFocusResolutionContext._spotlightVisible
- _OBJC_IVAR_$_SBMenuBarMainMenuView._alongsidePresentTapRecognizer
- _OBJC_IVAR_$_SBSlideOverTongueView._bitmapMaskSize
- _OBJC_IVAR_$_SBSlideOverTongueView._materialView
- _OBJC_IVAR_$_SBSlideOverTongueView._tongueContainerView
- _OBJC_IVAR_$_SBSlideOverTongueView._tongueMaskView
- _OBJC_IVAR_$_SBSwitcherTransitionRequest._bundleIdentifierOfAppToKillGracefully
- _OBJC_IVAR_$_SBTransientlyVisibleSlideOverTongueSwitcherModifier._edgeProtectEdge
- _OBJC_IVAR_$_SBTransientlyVisibleSlideOverTongueSwitcherModifier._mode
- _OBJC_IVAR_$_SBTransientlyVisibleSlideOverTongueSwitcherModifier._rightEdgeHintState
- _OBJC_METACLASS_$_SBTransientlyVisibleSlideOverTongueSwitcherModifier
- _SBDisplayItemSizeIsUnspecified.cold.1
- _SBFloatingConfigurationForMovingFloatingApplication.cold.1
- _SBFloatingConfigurationForMovingFloatingApplication.cold.2
- _SBFloatingConfigurationForMovingFloatingApplication.cold.3
- _UIMenuQuit
- __MTCoreMaterialRecipeNameForMaterialRecipeAndUserInterfaceStyle
- __OBJC_$_CLASS_METHODS_SBTransientlyVisibleSlideOverTongueSwitcherModifier
- __OBJC_$_INSTANCE_METHODS_FBSSceneSettings(SBTransientLocal|SBUISceneSafeAreaSettings|SBApplicationSceneHandle|Frame)
- __OBJC_$_INSTANCE_METHODS_SBTransientlyVisibleSlideOverTongueSwitcherModifier
- __OBJC_$_INSTANCE_VARIABLES_SBTransientlyVisibleSlideOverTongueSwitcherModifier
- __OBJC_$_PROP_LIST_SBTransientlyVisibleSlideOverTongueSwitcherModifier
- __OBJC_CLASS_RO_$_SBTransientlyVisibleSlideOverTongueSwitcherModifier
- __OBJC_METACLASS_RO_$_SBTransientlyVisibleSlideOverTongueSwitcherModifier
- ___101-[SBFluidSwitcherViewController _modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:]_block_invoke
- ___106-[_SBContinuitySessionStateMachine initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:]_block_invoke
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.318
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.319
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.320
- ___110-[SBInCallPresentationSession _updateVisibilityInSwitcherForPrefersHiddenWhenDismissedIfNeededForLayoutState:]_block_invoke.245
- ___111-[SBMainSwitcherControllerCoordinator switcherContentController:performTransitionWithRequest:gestureInitiated:]_block_invoke_3
- ___117-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]_block_invoke
- ___117-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]_block_invoke_2
- ___119-[SBDashBoardApplicationLauncher _activateCameraEntity:animated:asOverlay:viaSwitcherModal:request:actions:completion:]_block_invoke.60
- ___119-[SBDashBoardApplicationLauncher _activateCameraEntity:animated:asOverlay:viaSwitcherModal:request:actions:completion:]_block_invoke_2.68
- ___119-[SBDashBoardApplicationLauncher _activateCameraEntity:animated:asOverlay:viaSwitcherModal:request:actions:completion:]_block_invoke_3.69
- ___119-[SBDashBoardApplicationLauncher _activateCameraEntity:animated:asOverlay:viaSwitcherModal:request:actions:completion:]_block_invoke_4.71
- ___121-[SBContinuousExposeDragAndDropGestureRootSwitcherModifier gestureChildModifierForGestureEvent:activeTransitionModifier:]_block_invoke
- ___127-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]_block_invoke
- ___127-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]_block_invoke_2
- ___127-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]_block_invoke_3
- ___127-[SBDeviceApplicationSceneHandle windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:]_block_invoke_4
- ___138-[SBDashBoardHostableEntityPresentationManager presentEntity:fromRequest:animated:withEphemeralSwitcher:dismissGestureEnabled:completion:]_block_invoke
- ___138-[SBDashBoardHostableEntityPresentationManager presentEntity:fromRequest:animated:withEphemeralSwitcher:dismissGestureEnabled:completion:]_block_invoke_2
- ___138-[SBDashBoardHostableEntityPresentationManager presentEntity:fromRequest:animated:withEphemeralSwitcher:dismissGestureEnabled:completion:]_block_invoke_3
- ___138-[SBDashBoardHostableEntityPresentationManager presentEntity:fromRequest:animated:withEphemeralSwitcher:dismissGestureEnabled:completion:]_block_invoke_4
- ___370-[SBDisplayItemLayoutAttributesCalculator _appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:usingNewLayoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]_block_invoke
- ___370-[SBDisplayItemLayoutAttributesCalculator _appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:usingNewLayoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]_block_invoke_2
- ___38-[SBIconController _registerAnalytics]_block_invoke.219
- ___47-[SBLockScreenManager handleTransitionRequest:]_block_invoke.244
- ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.90
- ___53-[SBSlideOverTongueView setDirection:state:animated:]_block_invoke_3
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.382
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.385
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.384
- ___54-[SBSwitcherModifierQuerySnapshot _buildFromModifier:]_block_invoke_157
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.291
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.291.cold.1
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.295
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.296
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.296.cold.1
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.299
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.299.cold.1
- ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.772
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1786
- ___59-[SBIconController _updateUninstallingSystemAppsRestricted]_block_invoke.218
- ___60-[SBDeviceApplicationSceneHandle _updateInterfaceAppearance]_block_invoke
- ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.245
- ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.245.cold.1
- ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke.210
- ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke_2.213
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.668
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.670
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.671
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.672
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.673
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_2.679
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_3.691
- ___71-[SBRoutingSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:]_block_invoke
- ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.391
- ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1093
- ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.413
- ___76-[SBMenuBarViewController adjustPresentedMenuForPointerOverViewInContainer:]_block_invoke
- ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke.123
- ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_2.125
- ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.443
- ___83-[SBIconController _obtainSmartStackForWidgetDiscoverabilityWithCompletionHandler:]_block_invoke.250
- ___86-[SBDeviceApplicationSceneHandle setStatusBarForceHidden:forReason:animationSettings:]_block_invoke.37
- ___86-[SBHomePeekToFullScreenTransitionModifier perspectiveAngleForLayoutRole:inAppLayout:]_block_invoke
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.376
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.377
- ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.86
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1638
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1640
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1642
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1646
- ___93-[SBBannerManager _acquireGestureRecognizerPriorityAssertionWithPriority:windowScene:reason:]_block_invoke.227
- ___93-[SBBannerManager _acquireGestureRecognizerPriorityAssertionWithPriority:windowScene:reason:]_block_invoke_2.228
- ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke.394
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1769
- ___98-[_SBKeyboardFocusSceneControllerDependenciesBase isBannerKitHostingSceneWithIdentityTokenString:]_block_invoke
- ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s_e38_B16?0"SBFluidSwitcherItemContainer"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_152_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_176_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
- ___block_descriptor_184_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_40_e8_32r_e49_v32?0"SBTransientOverlayViewController"8Q16^B24lr32l8
- ___block_descriptor_48_e138_{SBWindowControlsLayout=qB{CGPoint=dd}}88?0"SBChainableModifier"8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80l
- ___block_descriptor_48_e8_32s_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16ls32l8
- ___block_descriptor_48_e8_32w40w_e8_v12?0B8lw32l8w40l8
- ___block_descriptor_56_e8_32s40s48s_e23_16?0"SBDisplayItem"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40bs48r_e36_v32?0"SBChainableModifier"8Q16^B24ls40l8s32l8r48l8
- ___block_descriptor_72_e8_32s40r48r56r64r_e17_v16?0"NSArray"8lr40l8s32l8r48l8r56l8r64l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e34_v24?0"SBSwitcherController"8^B16ls32l8s40l8s48l8s56l8r64l8
- ___block_descriptor_88_e8_32s40s48r56r64r72r80r_e8_v16?0q8ls32l8s40l8r48l8r56l8r64l8r72l8r80l8
- ___block_literal_global.1107
- ___block_literal_global.117
- ___block_literal_global.1193
- ___block_literal_global.1241
- ___block_literal_global.132
- ___block_literal_global.134
- ___block_literal_global.140
- ___block_literal_global.1612
- ___block_literal_global.1616
- ___block_literal_global.1648
- ___block_literal_global.1657
- ___block_literal_global.1659
- ___block_literal_global.1661
- ___block_literal_global.1663
- ___block_literal_global.1679
- ___block_literal_global.1795
- ___block_literal_global.1818
- ___block_literal_global.1827
- ___block_literal_global.1843
- ___block_literal_global.197
- ___block_literal_global.207
- ___block_literal_global.233
- ___block_literal_global.269
- ___block_literal_global.270
- ___block_literal_global.272
- ___block_literal_global.285
- ___block_literal_global.335
- ___block_literal_global.345
- ___block_literal_global.351
- ___block_literal_global.353
- ___block_literal_global.362
- ___block_literal_global.372
- ___block_literal_global.377
- ___block_literal_global.489
- ___block_literal_global.494
- ___block_literal_global.503
- ___block_literal_global.506
- ___block_literal_global.537
- ___block_literal_global.542
- ___block_literal_global.546
- ___block_literal_global.580
- ___block_literal_global.591
- ___block_literal_global.593
- ___block_literal_global.595
- ___block_literal_global.598
- ___block_literal_global.616
- ___block_literal_global.62
- ___block_literal_global.665
- ___block_literal_global.675
- ___block_literal_global.681
- ___block_literal_global.719
- ___block_literal_global.745
- ___block_literal_global.759
- ___block_literal_global.84
- __sceneManagerForDisplayIdentity:creatingIfNecessary:.___once.83
- _objc_msgSend$_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:layoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
- _objc_msgSend$_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:usingNewLayoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
- _objc_msgSend$_buildQuitMenuWithAdditionalOptions:
- _objc_msgSend$_deviceApplicationSceneEntityForFloatingApplicationGrabberTongue
- _objc_msgSend$_effectiveStageAreaForSnappingForSpace:configuration:
- _objc_msgSend$_floatingConfigurationForActivatedEdge:
- _objc_msgSend$_initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:
- _objc_msgSend$_isStripVisibleForBoundingBox:configuration:effectiveStripWidth:
- _objc_msgSend$_isUnpinGestureAllowedToMoveWindowsAtLocationInReferenceCoordinateSpace:
- _objc_msgSend$_modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:
- _objc_msgSend$_safeAreaCornerInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:
- _objc_msgSend$_sizeForAttributedSize:inBounds:defaultSize:screenEdgePadding:sizingPolicy:dockHeightWithPadding:interItemSpacing:
- _objc_msgSend$_snapPositionOfTopMostItemIfNecessaryInSpace:autoLayoutConfiguration:snappedEdgesMask:
- _objc_msgSend$_snapPositionOfTopMostItemToRect:inSpace:autoLayoutConfiguration:considerAdjacency:snappedEdgesMask:itemForPotentialPairing:
- _objc_msgSend$_snapSizeOfResizingDisplayItemIfNecessaryForSpace:configuration:snappedEdgesMask:
- _objc_msgSend$_snapSizeOfResizingDisplayItemToRect:inSpace:windowingConfiguration:considerAdjacency:snappedEdgesMask:newFrame:
- _objc_msgSend$_stageAreaForBoundingBox:configuration:effectiveStripWidth:
- _objc_msgSend$_updateInterfaceAppearance
- _objc_msgSend$activeTransientOverlayPresentationCanBecomeFirstResponder
- _objc_msgSend$activeTransientOverlayPresentationShouldUseSceneBasedKeyboardFocus
- _objc_msgSend$appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
- _objc_msgSend$appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:usingLayoutAttributes:options:containerOrientation:windowScene:source:
- _objc_msgSend$bundleIdentifierOfAppToKillGracefully
- _objc_msgSend$cameraIsHosted
- _objc_msgSend$canActivePresentationBecomeFirstResponder
- _objc_msgSend$coverSheetSlidingViewControllerCleanupInterstitialWhileOffScreen:
- _objc_msgSend$coverSheetSlidingViewControllerIsInterstitialAllowed:
- _objc_msgSend$defaultWindowControlsLayoutForDisplayItem:frame:containerBounds:interfaceOrientation:
- _objc_msgSend$flexibleAutoLayoutSpaceForAppLayout:calculatedUsingNewLayoutAttributesMap:flexibleAutoLayoutSource:
- _objc_msgSend$flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
- _objc_msgSend$flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:newLayoutAttributes:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
- _objc_msgSend$focusTargetForActiveTransientOverlayPresentation
- _objc_msgSend$focusTargetForCoverSheetHostedAppGetCameraIsHosted:
- _objc_msgSend$frameForLayoutRole:inAppLayout:containerBounds:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
- _objc_msgSend$hasActiveTransientOverlayPresentation
- _objc_msgSend$initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:
- _objc_msgSend$initWithBlockedState:preparingForRemoteUnlockState:waitingForRemoteUnlockState:waitingForScenesState:waitingForHIDServicesState:activatingState:updatingActiveDisplayState:launchingState:flushingState:activeState:
- _objc_msgSend$initWithGestureID:initialAppLayout:selectedDisplayItem:
- _objc_msgSend$initWithMode:
- _objc_msgSend$isActiveTransientOverlayPresentationFromSceneWithIdentityTokenString:
- _objc_msgSend$isActiveTransientOverlayPresentationIsFromSceneWithIdentityTokenString:
- _objc_msgSend$isBannerKitHostingSceneWithIdentityTokenString:
- _objc_msgSend$isSiriVisible
- _objc_msgSend$isSpolightPresentedAsTransientOverlay
- _objc_msgSend$keyboardFocusTargetForSBWindowScene:
- _objc_msgSend$knownCaptureApplicationsByBundleIdentifier
- _objc_msgSend$perspectiveAngleForLayoutRole:inAppLayout:
- _objc_msgSend$presentEntity:fromRequest:animated:withEphemeralSwitcher:dismissGestureEnabled:completion:
- _objc_msgSend$quitMenuWithOptions:
- _objc_msgSend$removeCurrentSelectedApplication
- _objc_msgSend$rightEdgePeekDelay
- _objc_msgSend$rightEdgePeekTimeout
- _objc_msgSend$safeAreaCornerInsets
- _objc_msgSend$safeAreaEdgeInsets
- _objc_msgSend$safeAreaEdgeInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:
- _objc_msgSend$sb_safeAreaSettings
- _objc_msgSend$setBundleIdentifierOfAppToKillGracefully:
- _objc_msgSend$setCameraIsHosted:
- _objc_msgSend$setPasscodeLockVisible:animated:showBackground:completion:
- _objc_msgSend$setSafeAreaCornerInsets:
- _objc_msgSend$setSafeAreaEdgeInsets:
- _objc_msgSend$setSiriVisible:
- _objc_msgSend$setSpotlightVisible:
- _objc_msgSend$slideOverTongueTransientlyVisibleModeForEvent:
- _objc_msgSend$spaceByPerformingFlexibleAutoLayoutWithSpace:configuration:options:source:
- _objc_msgSend$systemQuitMenuWithOptions:
- _objc_msgSend$transientlyVisibleSlideOverTongueModifier
- _objc_msgSend$updateLayoutAttributes:ofDisplayItem:inAppLayout:
- _objc_msgSend$updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:
- _objc_msgSend$windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:
- _objc_msgSend$windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:
CStrings:
+ "%@ yOffsetFromCorner=%f size=%@ isActive=%@ isStashed=%@ dodgesDock=%@"
+ "%@-SlideOverCenterExitingUpdate-%ld"
+ "%@_%p"
+ "-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:displayOrdinal:orientation:]"
+ "-[SBPBDisplayItemLayoutAttributes writeTo:]"
+ ".storeDemoPrep"
+ "<%@:%p> not waiting for scene updates and not animating, so not interrupting for Cover Sheet fly-in"
+ "<invalid:%d>"
+ "@\"<_UISceneSafeAreaSettings>\""
+ "@\"SBContinuitySessionStoreDemoController\""
+ "@\"SBPBSlideOverConfiguration\""
+ "@\"SBSDFElementView\""
+ "@\"SBSDFView\""
+ "@\"SBSceneHandleActiveAppearanceAssertion\""
+ "@\"SBSlideOverGlassMaterialView\""
+ "@\"_SBContinuitySessionStateMachineStateStoreDemoPrep\""
+ "@\"_SBSlideOverGlassMaterialBackgroundView\""
+ "@104@0:8@16@24@32@40@48@56@64@72@80@88@96"
+ "@156@0:8@16q24d32d40{CGRect={CGPoint=dd}{CGSize=dd}}48B80B84B88{CGRect={CGPoint=dd}{CGSize=dd}}92{CGRect={CGPoint=dd}{CGSize=dd}}124"
+ "@156@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80d88d96d104d112d120d128B136B140B144B148B152"
+ "@180@0:8@16q24d32d40{CGRect={CGPoint=dd}{CGSize=dd}}48B80B84B88@92{CGRect={CGPoint=dd}{CGSize=dd}}100{CGRect={CGPoint=dd}{CGSize=dd}}132@164@172"
+ "@196@0:8@16@24Q32q40d48d56{CGRect={CGPoint=dd}{CGSize=dd}}64B96B100B104q108{CGRect={CGPoint=dd}{CGSize=dd}}116{CGRect={CGPoint=dd}{CGSize=dd}}148@180@188"
+ "@208@0:8@16@24@32Q40q48@56d64d72{CGRect={CGPoint=dd}{CGSize=dd}}80B112B116q120{CGRect={CGPoint=dd}{CGSize=dd}}128{CGRect={CGPoint=dd}{CGSize=dd}}160@192@200"
+ "@272@0:8q16q24q32{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}40{SBDisplayItemTileConfiguration=q{CGSize=dd}}96{SBDisplayItemSlideOverConfiguration=qd{CGSize=dd}BBB}120{CGPoint=dd}160B176q180{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}188{CGPoint=dd}244B260q264"
+ "@48@0:8@16q24q32@?40"
+ "@52@0:8@16@24B32B36B40@?44"
+ "@56@0:8@?16q24@32{CGPoint=dd}40"
+ "@60@0:8@16@24@32B40Q44Q52"
+ "@84@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48d56B64B68B72B76B80"
+ "@88@0:8@16@24@32Q40q48@56q64@72@80"
+ "@88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48@80"
+ "B16@?0@\"SBDisplayItemLayoutAttributes\"8"
+ "B16@?0@\"SBTransientOverlayViewController\"8"
+ "B36@0:8B16@20@?28"
+ "B64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56"
+ "B72@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48d56@64"
+ "Between switcher controllers: %{public}@"
+ "CarPlay"
+ "EXIT_SLIDE_OVER_DISCOVERABILITY"
+ "InAppSwitcher"
+ "Invalid cross display transition context setup"
+ "Invalid cross display transition with no moving items. fromDisplayItems: %{public}@. toDisplayItems: %{public}@"
+ "LEFT_SLIDE_OVER_DISCOVERABILITY"
+ "Moving displayItems: %{public}@"
+ "Moving to state Ended because the trackpad threshold was reached"
+ "NoSlideOverDisplayItem"
+ "Preventing the floating app move gesture because there's no slideover app."
+ "Preventing the floating app present gesture because the slideover app is not stashed."
+ "Preventing the floating app present gesture from the left edge because the slideover app is not stashed on the left."
+ "Preventing the floating app present gesture from the right edge because the slideover app is not stashed on the right."
+ "Q1q"
+ "RIGHT_SLIDE_OVER_DISCOVERABILITY"
+ "Ra"
+ "RadioHID"
+ "SB target %@"
+ "SBContinuitySessionStoreDemoController"
+ "SBContinuitySessionStoreDemoController.m"
+ "SBDashBoardHostableEntityPresentationRequest"
+ "SBDisplayItemLayoutAttributesCalculator.m"
+ "SBFinishUnstashingSlideOverItemAnimationModifier"
+ "SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier"
+ "SBFullScreenCrossBlurBehindSlideOverItemWindowingModifier.m"
+ "SBMenuBarPointerTrackingPanGestureRecognizer"
+ "SBPBDisplayItemLayoutAttributes.m"
+ "SBPBSlideOverConfiguration"
+ "SBSDFElementView"
+ "SBSDFView"
+ "SBSceneHandleActiveAppearanceAssertion"
+ "SBSceneHandleActiveAppearanceAssertion.m"
+ "SBSlideOverGlassMaterialView"
+ "SBSlideOverTongueDisappearanceReason"
+ "SBSlideOverTongueFinishedReason"
+ "SBStashSlideOverItemAnimationModifier"
+ "SBStashSlideOverItemIndirectGestureWindowingModifier"
+ "SBToggleSlideOverForDisplayItemSwitcherEventResponse"
+ "SBToggleSlideOverForDisplayItemSwitcherEventResponse.m"
+ "SBTransientlyVisibleSlideOverTongueWindowingModifier"
+ "SDF Output"
+ "STASH_SLIDE_OVER_DISCOVERABILITY"
+ "Scene handle active appearance assertion was acquired: %{public}@"
+ "Scene handle active appearance assertion was invalidated: %{public}@"
+ "Slide Over Enter Center Region Threshold"
+ "Slide Over Exit Center Region Threshold"
+ "Stash Slide Over Indirect Gesture Modifier"
+ "State is storeDemoPrep but we already created UI"
+ "T@\"<CSHostableEntity>\",R,N,V_activatingHostableEntity"
+ "T@\"<CSHostableEntity>\",R,N,V_currentHostableEntity"
+ "T@\"<_UISceneSafeAreaSettings>\",&,N,V_preferredSafeAreaSettings"
+ "T@\"NSString\",&,V_alertAccessibilityIdentifier"
+ "T@\"NSString\",&,V_alternateButtonAccessibilityIdentifier"
+ "T@\"NSString\",&,V_defaultButtonAccessibilityIdentifier"
+ "T@\"NSString\",&,V_otherButtonAccessibilityIdentifier"
+ "T@\"SBFZStackResolver\",&,D,N"
+ "T@\"SBIndirectPanGestureSettings\",&,N,V_indirectPanGestureSettings"
+ "T@\"SBMainWorkspaceTransitionRequest\",R,N,V_transitionRequest"
+ "T@\"SBMenuBarViewController\",W,N,V_menuBarViewController"
+ "T@\"UIAction\",R,N,V_enterSlideOverAction"
+ "T@\"UIAction\",R,N,V_exitSlideOverAction"
+ "T@\"UIAction\",R,N,V_slideOverMenu"
+ "T@\"UIView\",&,N,V_slideOverTonguePortalView"
+ "T@?,R,C,N,V_presentationCompletion"
+ "TB,D,N,GisDockVisible"
+ "TB,D,N,GisInSlideOver"
+ "TB,N,GisDockVisible,V_dockVisible"
+ "TB,N,GisInSlideOver,V_inSlideOver"
+ "TB,N,GisMenuBarBecomingVisible,V_menuBarBecomingVisible"
+ "TB,N,GisUnstashFromHomeTransition,V_unstashFromHomeTransition"
+ "TB,N,V_prefersZoomDownAnimation"
+ "TB,N,V_shouldActivateWithThresholdForMouse"
+ "TB,N,V_shouldActivateWithThresholdForTrackpad"
+ "TB,N,V_unstashingFromHome"
+ "TB,R,N,GisInStoreDemoMode"
+ "TB,R,N,GisOccludingSystemContent"
+ "TB,R,N,GisPresentingStoreDemoLoop"
+ "TB,R,N,V_dismissGestureEnabled"
+ "TB,R,N,V_isEphemeralSwitcher"
+ "TB,R,N,V_unstashingFromHome"
+ "TB,R,N,V_wantsSlideOverTongue"
+ "TOP_AFFORDANCE_MENU_TITLE_ENTER_SLIDE_OVER"
+ "TOP_AFFORDANCE_MENU_TITLE_EXIT_SLIDE_OVER"
+ "TQ,N,V_posterClientDeviceMotionMode"
+ "TQ,R,N,V_slideOverTongueDirection"
+ "TQ,R,N,V_slideOverTongueState"
+ "Td,N,V_lastTrackpadActivationTimestamp"
+ "Td,N,V_slideOverBorderWidth"
+ "Td,N,V_slideOverEnterCenterRegionThreshold"
+ "Td,N,V_slideOverExitCenterRegionThreshold"
+ "Td,N,V_slideOverThresholdToForegroundUnstashingApp"
+ "ToggleSlideOverForDisplayItem"
+ "Tq,N,V_sceneRelevancyHint"
+ "Tq,R,N,V_activeAppearance"
+ "UNSTASH_SLIDE_OVER_DISCOVERABILITY"
+ "UnstashFromHome"
+ "[Session] storeDemoPrep"
+ "[State.Blocked] --> moving to %@"
+ "[State.StoreDemoPrep] --> moving to .blocked"
+ "[State.StoreDemoPrep] Re-evaluating state for reason: %{public}@"
+ "[State.StoreDemoPrep] still blocked by %{public}@"
+ "^{_SBAppLayoutAutoLayoutSpaceCacheKeyDisplayItemRecord={CGSize=dd}{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}{CGPoint=dd}qqq{SBDisplayItemTileConfiguration=q{CGSize=dd}}{SBDisplayItemSlideOverConfiguration=qd{CGSize=dd}BBB}q}"
+ "_SBContinuitySessionStateMachineStateStoreDemoPrep"
+ "_SBSlideOverGlassMaterialBackgroundView"
+ "_activatingHostableEntity"
+ "_activeAppearanceAssertion"
+ "_activeAppearanceAssertions"
+ "_adjustPresentedMenuForPointerOverViewInContainer:forPanGesture:"
+ "_adjustedFromAppLayout"
+ "_adjustedToAppLayout"
+ "_alertAccessibilityIdentifier"
+ "_alternateButtonAccessibilityIdentifier"
+ "_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:layoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:"
+ "_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:usingNewLayoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:"
+ "_backgroundSDFView"
+ "_blockOnUIUnlock"
+ "_cachedWindowingConfiguration_prototypingSlideOverBorderWidth"
+ "_cachedWindowingConfiguration_prototypingSlideOverEnterCenterRegionThreshold"
+ "_cachedWindowingConfiguration_prototypingSlideOverExitCenterRegionThreshold"
+ "_collapseAndPrepareForDismiss"
+ "_collapseSettlingDuration"
+ "_computeActiveAppearance"
+ "_computedActiveAppearance"
+ "_currentHostableEntity"
+ "_currentHostableEntity changed"
+ "_currentSlideOverConfiguration"
+ "_darkGlassBackgroundFilterParameters"
+ "_darkKeyFillVibrantColorMatrix"
+ "_defaultButtonAccessibilityIdentifier"
+ "_destinationSDFElementView"
+ "_didCollapseSlideOverTongue"
+ "_dockVisible"
+ "_draggingItemScreenCenterForSize:scale:"
+ "_effectiveHomeAffordanceViewFrame"
+ "_effectiveIndexInRecencyOfAppLayout:"
+ "_effectiveStageAreaForSnappingItem:inSpace:configuration:"
+ "_enterSlideOverAction"
+ "_exitSlideOverAction"
+ "_finishedReason"
+ "_flexibleAutoLayoutSpaceForStripAppLayout:"
+ "_handleLeftSlideOverCommand:"
+ "_handleMenuPanGesture:"
+ "_handleRequestAppSwitcherUpdateWindowingMode:fromClient:"
+ "_handleRightSlideOverCommand:"
+ "_handleToggleStash:"
+ "_handleToggleStashSlideOverCommand:"
+ "_hasBegunEdgeProtect"
+ "_hasUnstashed"
+ "_inLeftPinnedSlideOver"
+ "_inRightPinnedSlideOver"
+ "_inSlideOver"
+ "_increaseContrastDidChange:"
+ "_indirectPanGestureSettings"
+ "_initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:slideOverConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:"
+ "_initialSlideOverConfiguration"
+ "_initialVisibleDisplayItems"
+ "_initializeSlideOverDisplayItemIfNeededForcingStashed:"
+ "_innerLeftEdgeDragHitTestRectForItemContainer:forPointerTouch:"
+ "_innerRightEdgeDragHitTestRectForItemContainer:forPointerTouch:"
+ "_isDismissingEntity"
+ "_isDockVisibleForBoundingBox:configuration:slideOverItem:"
+ "_isEphemeralSwitcher"
+ "_isStripVisibleForBoundingBox:configuration:effectiveStripWidth:slideOverItem:"
+ "_isUnpinGestureAllowedToMoveWindowsAtLocationInReferenceCoordinateSpace:withinUnstashLocationOnHomeScreen:"
+ "_keyboardInsetsForWindowScene:"
+ "_lastCenterYBeforeStashingOrUnstashingBegan"
+ "_lastTrackpadActivationTimestamp"
+ "_layOutSlideOverItemFullyOffscreen"
+ "_lightGlassBackgroundFilterParameters"
+ "_lightKeyFillVibrantColorMatrix"
+ "_managedMainDisplayItems"
+ "_menuBarBecomingVisible"
+ "_modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:"
+ "_moveDisplayItemOutOfSlideOver:"
+ "_moveDisplayItemToSlideOver:"
+ "_otherButtonAccessibilityIdentifier"
+ "_pendingPresentationRequests"
+ "_performToggleSlideOverForDisplayItemResponse:"
+ "_posterClientDeviceMotionMode"
+ "_prefersZoomDownAnimation"
+ "_presentationCompletion"
+ "_reevaluateActiveAppearanceFromAssertions"
+ "_responseForGestureEnd:"
+ "_safeAreaCornerInsetResolverForApplicationFrame:screenBounds:activationSettings:"
+ "_sceneRelevancyHint"
+ "_sdfElementContainerView"
+ "_selectedItemIsInSlideOver"
+ "_shouldActivateWithThresholdForMouse"
+ "_shouldActivateWithThresholdForTrackpad"
+ "_shouldLockYPosition"
+ "_sizeForAttributedSize:inBounds:defaultSize:screenEdgePadding:"
+ "_slideOverAppLayoutIfAny"
+ "_slideOverBorderWidth"
+ "_slideOverCenterExitingTimerWaitingWhileStillCloseWithCenter:"
+ "_slideOverCenterExitingUpdateGeneration"
+ "_slideOverCenterExitingUpdateReason"
+ "_slideOverCenterSettledPosition"
+ "_slideOverConfiguration"
+ "_slideOverCorner"
+ "_slideOverDisplayItem"
+ "_slideOverDodgesDock"
+ "_slideOverEnterCenterRegionThreshold"
+ "_slideOverExitCenterRegionThreshold"
+ "_slideOverIsActive"
+ "_slideOverIsCenterExiting"
+ "_slideOverIsStashed"
+ "_slideOverLeafAppLayout"
+ "_slideOverMenu"
+ "_slideOverSizeHeight"
+ "_slideOverSizeWidth"
+ "_slideOverThresholdToForegroundUnstashingApp"
+ "_slideOverTongueDirection"
+ "_slideOverTonguePortalView"
+ "_slideOverTongueState"
+ "_slideOverYOffsetFromCorner"
+ "_snapPositionOfItem:ifNecessaryInSpace:autoLayoutConfiguration:snappedEdgesMask:"
+ "_snapPositionOfItem:toRect:inSpace:autoLayoutConfiguration:considerAdjacency:snappedEdgesMask:itemForPotentialPairing:"
+ "_snapSizeOfItem:ifNecessaryForSpace:configuration:snappedEdgesMask:"
+ "_snapSizeOfItem:toRect:inSpace:windowingConfiguration:considerAdjacency:snappedEdgesMask:newFrame:"
+ "_sourceSDFElementView"
+ "_specularSDFView"
+ "_stageAreaForBoundingBox:configuration:effectiveStripWidth:slideOverItem:"
+ "_startedStashed"
+ "_storeDemoModeController"
+ "_storeDemoPrepState"
+ "_suppressCameraButtonDeferringToApplications"
+ "_toAppLayoutInitialBounds"
+ "_toAppLayoutInitialPosition"
+ "_tonguePresentationReason"
+ "_tongueSize"
+ "_touchIsWithinUnstashRegionOnHomeScreen:"
+ "_touchLocationIsWithinSlideOverTongue:"
+ "_touchLocationIsWithinUnstashRegion:"
+ "_transitioningToHome"
+ "_unpinSplitViewApplicationGestureRecognizer receiving touch (%@): hit-tested to slideover tongue region with a stashed slideover item"
+ "_unstashFromHomeTransition"
+ "_unstashingFromHome"
+ "_updateClientWantsMotionEventState"
+ "_updateInterfaceActiveAppearance"
+ "_updateSlideOverGlass"
+ "_updateWithInterfaceStyle:"
+ "_wantsSlideOverTongue"
+ "_windowSceneForZStackParticipant:"
+ "acquireActiveAppearanceAssertionWithReason:activeAppearance:priority:"
+ "activatingHostableEntity"
+ "activeAppearanceAssertions"
+ "addSDFElementView:"
+ "alertAccessibilityIdentifier"
+ "allowCameraButtonDeferringWhileFocusLocked"
+ "allowsKeyboardArbiterToDetermineFocusTarget"
+ "alternateButtonAccessibilityIdentifier"
+ "appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:options:containerOrientation:floatingDockHeight:screenScale:bounds:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:"
+ "appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:usingLayoutAttributes:options:containerOrientation:windowScene:source:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:"
+ "arrowtriangle.backward.inset.filled.trailingthird.rectangle"
+ "arrowtriangle.forward.inset.filled.trailingthird.rectangle"
+ "beginNewRootFolderContentSession"
+ "centerForLayoutAttributes:windowingConfiguration:"
+ "com.apple.ist.demoloop"
+ "configureIconManager:"
+ "controlCenterDidAppear"
+ "cornerRadiusForSlideOverTongueAppLayout"
+ "coverSheetSlidingViewControllerDidEndDismissGestureOverInterstitial:"
+ "coverSheetSlidingViewControllerIsInterstitialDismissalAllowed:"
+ "coverSheetViewControllerDidWakeForSource:"
+ "currentHostableEntity"
+ "defaultButtonAccessibilityIdentifier"
+ "defaultWindowControlsLayoutForDisplayItem:frame:containerBounds:"
+ "didEdgeProtectSlideOverTongue:"
+ "dismissTransientOverlayPresentationsAnimated:windowScene:filter:"
+ "displayItemInSlideOver"
+ "displayItemsToExcludeFromStrip"
+ "dockVisible"
+ "enterSlideOverAction"
+ "exitSlideOverAction"
+ "flexibleAutoLayoutSpaceForAppLayout:calculatedUsingNewLayoutAttributesMap:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:"
+ "flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:floatingDockHeight:screenScale:bounds:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
+ "flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:floatingDockHeight:screenScale:bounds:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:newLayoutAttributes:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:"
+ "focus lock found"
+ "frameForIndexOffsetToCounteractSwitcherWindowMatchMoveForIndex:"
+ "frameForLayoutRole:inAppLayout:containerBounds:containerOrientation:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:isEmbeddedDisplay:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
+ "frameForSlideOverTongueAppLayout"
+ "fromAppLayout: %{public}@, toAppLayout: %{public}@"
+ "hitTestedToHomeAffordance:window:ofItemContainer:"
+ "hitTestedToSlideOverTongue:window:"
+ "in call presentation session"
+ "inSlideOver"
+ "indirectPanGestureSettings"
+ "initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:storeDemoModeController:"
+ "initWithDisplayItem:direction:"
+ "initWithEntity:transitionRequest:animated:isEphemeralSwitcher:dismissGestureEnabled:presentationCompletion:"
+ "initWithFromAppLayout:toAppLayout:"
+ "initWithGestureID:initialAppLayout:selectedDisplayItem:wantsSlideOverTongue:slideOverTongueState:slideOverTongueDirection:"
+ "initWithMenuBarViewController:"
+ "initWithReason:activeAppearance:priority:invalidationBlock:"
+ "initWithSafeAreaCornerInsets:"
+ "initWithSafeAreaEdgeInsets:"
+ "initWithSafeAreaEdgeInsetsForPortrait:landscape:"
+ "initWithStoreDemoPrepState:blockedState:preparingForRemoteUnlockState:waitingForRemoteUnlockState:waitingForScenesState:waitingForHIDServicesState:activatingState:updatingActiveDisplayState:launchingState:flushingState:activeState:"
+ "initWithSystemEventMonitor:continuityDisplayAuthenticationCoordinator:inStoreDemoMode:"
+ "initWithTonguePresentationReason:"
+ "inputClamp"
+ "isDockVisible"
+ "isInSlideOver"
+ "isInStoreDemoMode"
+ "isMenuBarBecomingVisible"
+ "isOccludingSystemContent"
+ "isPresentingStoreDemoLoop"
+ "isUnstashFromHomeTransition"
+ "knownCameraCaptureApplicationsByBundleIdentifier"
+ "lastInteractedDisplayItemsInAppLayout:orientation:"
+ "lastInteractedItemsInAppLayout:"
+ "lastTrackpadActivationTimestamp"
+ "menuBarBecomingVisible"
+ "need window scene plz"
+ "noteStoreDemoLockFailed"
+ "occludingSystemContent"
+ "otherButtonAccessibilityIdentifier"
+ "outcome:%@"
+ "overrideKeyboardFocusTarget"
+ "overrideTarget:%@"
+ "perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:"
+ "policy: focus lock -- allow KA to set target"
+ "policy: focus lock -- sbTarget:%{public}@ suppressRemoteDeferring:%{BOOL}u"
+ "policy: using override target: %{public}@"
+ "posterClientDeviceMotionMode"
+ "posterDeviceMotionMode"
+ "posterDidUpdateDeviceMotionMode:"
+ "prefersZoomDownAnimation"
+ "prepareForTransitionToPresented:reversingTransition:forUserGesture:"
+ "presentEntityWithRequest:"
+ "presentationCompletion"
+ "presentingStoreDemoLoop"
+ "q48@0:8@16@24@32q40"
+ "q92@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24@56@64B72q76@84"
+ "q92@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24@56@64B72q76^{CGRect={CGPoint=dd}{CGSize=dd}}84"
+ "quickCameraDidAppear"
+ "remote deferring suppresssd"
+ "safeAreaCornerInsetResolver"
+ "safeAreaEdgeInsetResolver"
+ "safeAreaEdgeInsetResolverForApplicationFrame:screenBounds:activationSettings:"
+ "safeAreaEdgeInsetsForOrientation:"
+ "sceneRelevancyHint"
+ "self->_slideOverConfiguration != nil"
+ "setAlertAccessibilityIdentifier:"
+ "setAllowsKeyboardArbiterToDetermineFocusTarget:"
+ "setAlternateButtonAccessibilityIdentifier:"
+ "setCurvature:"
+ "setDefaultButtonAccessibilityIdentifier:"
+ "setDeviceMotionMode:"
+ "setDockVisible:"
+ "setFillAmount:"
+ "setFillAngle:"
+ "setFillHeight:"
+ "setFillSpread:"
+ "setGlobal:"
+ "setGradientOvalization:"
+ "setInSlideOver:"
+ "setIndirectPanGestureSettings:"
+ "setKeyAmount:"
+ "setKeyAngle:"
+ "setKeyHeight:"
+ "setKeySpread:"
+ "setLastTrackpadActivationTimestamp:"
+ "setLimitsWidgetStackPageControlFlashesToSession:"
+ "setMenuBarBecomingVisible:"
+ "setOtherButtonAccessibilityIdentifier:"
+ "setOverrideKeyboardFocusTarget:"
+ "setPasscodeLockVisible:animated:showBackground:forceBiometricPresentation:completion:"
+ "setPosterClientDeviceMotionMode:"
+ "setPrefersZoomDownAnimation:"
+ "setSafeAreaCornerInsetResolver:"
+ "setSafeAreaEdgeInsetResolver:"
+ "setSceneRelevancyHint:"
+ "setShouldActivateWithThresholdForMouse:"
+ "setShouldActivateWithThresholdForTrackpad:"
+ "setSlideOverBorderWidth:"
+ "setSlideOverEnterCenterRegionThreshold:"
+ "setSlideOverExitCenterRegionThreshold:"
+ "setSlideOverMargin:"
+ "setSlideOverThresholdToForegroundUnstashingApp:"
+ "setSlideOverTonguePortalSourceView:"
+ "setSmoothness:"
+ "setSuppressCameraButtonDeferringToApplications:"
+ "setUnstashFromHomeTransition:"
+ "setUnstashingFromHome:"
+ "shouldActivateWithThresholdForMouse"
+ "shouldActivateWithThresholdForTrackpad"
+ "shouldIgnoreReducedMotionChange"
+ "shouldSuppressAlertContentOnHostApplication"
+ "sizeForLayoutAttributes:windowingConfiguration:"
+ "sizeForSlideOverConfiguration:windowingConfiguration:"
+ "slideOverBorderWidth"
+ "slideOverConfigSize"
+ "slideOverConfiguration"
+ "slideOverConfigurationOnAnySwitcherForDisplayItem:"
+ "slideOverCorner"
+ "slideOverDodgesDock"
+ "slideOverEnterCenterRegionThreshold"
+ "slideOverExitCenterRegionThreshold"
+ "slideOverIsActive"
+ "slideOverIsCenterExiting"
+ "slideOverIsStashed"
+ "slideOverMargin"
+ "slideOverMarginForLayoutRole:inAppLayout:"
+ "slideOverMenu"
+ "slideOverSizeHeight"
+ "slideOverSizeWidth"
+ "slideOverThresholdToForegroundUnstashingApp"
+ "slideOverTongue layout"
+ "slideOverTongue position"
+ "slideOverTongueModifierForRoutingModifier:"
+ "slideOverTonguePortalSourceView"
+ "slideOverYOffsetFromCorner"
+ "slideover-corner-bottom-left"
+ "slideover-corner-bottom-right"
+ "slideover-corner-top-left"
+ "slideover-corner-top-right"
+ "sourceLayer"
+ "spaceByPerformingFlexibleAutoLayoutWithSpace:configuration:options:itemsNeedingPositionSnapping:itemsNeedingSizeSnapping:"
+ "storeDemoMode"
+ "suppressCameraButtonDeferringToApplications"
+ "switcher style update"
+ "switcherContentController:moveDisplayItemOutOfSlideOver:"
+ "switcherContentController:moveDisplayItemToSlideOver:"
+ "systemEventMonitor"
+ "systemServiceServer:requestUpdateWindowingMode:forClient:completion:"
+ "top-affordance-enter-slide-over"
+ "top-affordance-exit-slide-over"
+ "unstashFromHomeTransition"
+ "unstashingFromHome"
+ "update slide over tongue"
+ "updateActiveAppearanceReason != nil"
+ "updateLayoutAttributes:ofDisplayItem:"
+ "updateLayoutAttributes:ofDisplayItem:displayOrdinal:orientation:"
+ "updatedSlideOverConfigurationForItemWithSize:center:slideOverConfiguration:windowingConfiguration:"
+ "v16@?0@\"SBSceneHandleActiveAppearanceAssertion\"8"
+ "v32@0:8@\"SBDisplayItemLayoutAttributes\"16@\"SBDisplayItem\"24"
+ "v32@?0@\"SBSceneHandleActiveAppearanceAssertion\"8Q16^B24"
+ "v44@0:8@\"SBSystemServiceServer\"16i24@\"<FBSServiceFacilityClientHandle>\"28@?<v@?>36"
+ "v44@0:8@16i24@28@?36"
+ "v48@0:8@\"SBDisplayItemLayoutAttributes\"16@\"SBDisplayItem\"24q32q40"
+ "windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:"
+ "windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:"
+ "windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:"
+ "{?=\"switcherContentControllerBringAppLayoutToFront\"b1\"switcherContentControllerActivatedBestAppSuggestion\"b1\"updateUserInteractionEnabledForSwitcherContentController\"b1\"updateWindowVisibilityForSwitcherContentController\"b1\"switcherContentControllerSetHomeScreenScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenAlphaWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenDimmingAlphaWithSettingsAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurProgressWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurType\"b1\"switcherContentControllerSetHomeScreenBackdropBlurMaterialRecipeNameWithAnimationModeCompletion\"b1\"switcherContentControllerControlsWallpaper\"b1\"switcherContentControllerSetWallpaperScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetWallpaperStyle\"b1\"switcherContentControllerSetInterfaceOrientation\"b1\"switcherContentControllerSetInterfaceOrientationFromUserResizingForDisplayItem\"b1\"switcherContentControllerRequestNewWindowForBundleIdentifier\"b1\"switcherContentControllerSetContainerStatusBarHiddenPartsHiddenAnimationDuration\"b1\"switcherContentControllerWantsToDismissMenuBar\"b1\"switcherContentControllerWantsToPeekMenuBar\"b1\"switcherContentControllerWantsToUpdateMenuBarVisibility\"b1\"switcherContentControllerDemoLayoutAttributesForDisplayItem\"b1\"switcherContentControllerSetPointerInteractionsEnabled\"b1\"switcherContentControllerShouldResignActiveForStartOfTransition\"b1\"switcherContentControllerControlsHomeScreenContents\"b1\"switcherContentControllerSetCacheAsynchronousRenderingSurfaces\"b1\"cancelActiveGestureForSwitcherContentController\"b1\"switcherContentControllerReopenHiddenAppLayoutsWithBundleIdentifier\"b1\"switcherContentControllerLayoutStateTransitionDidEndWithTransitionContext\"b1\"switcherContentControllerTransformForCardUnderSheetForBoundsSize\"b1\"switcherContentControllerMoveDisplayItemFromOtherDisplay\"b1\"presentContinuousExposeStripRevealGrabberTongueImmediatelyForSwitcherContentController\"b1\"tickleContinuousExposeStripRevealGrabberTongueIfVisibleForSwitcherContentController\"b1\"switcherContentControllerDidUpdateVisibleHomeAffordances\"b1\"switcherContentControllerRemoveDisplayItemsFromDesktop\"b1\"switcherContentControllerRequestDismissalForHomeScreenBackgroundTaps\"b1\"switcherContentControllerMoveDisplayItemToSlideOver\"b1\"switcherContentControllerMoveDisplayItemOutOfSlideOver\"b1}"
+ "{CGPoint=dd}40@0:8{CGSize=dd}16d32"
+ "{CGPoint=dd}48@0:8q16@\"SBAppLayout\"24{CGPoint=dd}32"
+ "{CGPoint=dd}48@0:8q16@24{CGPoint=dd}32"
+ "{CGPoint=dd}48@?0@\"SBChainableModifier\"8q16@24{CGPoint=dd}32"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}168@0:8q16@24{CGRect={CGPoint=dd}{CGSize=dd}}32q64d72d80B88B92B96B100{CGRect={CGPoint=dd}{CGSize=dd}}104{CGRect={CGPoint=dd}{CGSize=dd}}136"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}40@0:8@16@24@32"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}72@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48d56@64"
+ "{CGSize=dd}128@0:8{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}16{CGRect={CGPoint=dd}{CGSize=dd}}72{CGSize=dd}104d120"
+ "{CGSize=dd}64@0:8{SBDisplayItemSlideOverConfiguration=qd{CGSize=dd}BBB}16@56"
+ "{SBDisplayItemSlideOverConfiguration=\"corner\"q\"yOffsetFromCorner\"d\"size\"{CGSize=\"width\"d\"height\"d}\"isActive\"B\"isStashed\"B\"dodgesDock\"B}"
+ "{SBDisplayItemSlideOverConfiguration=qd{CGSize=dd}BBB}16@0:8"
+ "{SBDisplayItemSlideOverConfiguration=qd{CGSize=dd}BBB}24@0:8@16"
+ "{SBDisplayItemSlideOverConfiguration=qd{CGSize=dd}BBB}96@0:8{CGSize=dd}16{CGPoint=dd}32{SBDisplayItemSlideOverConfiguration=qd{CGSize=dd}BBB}48@88"
+ "{SBWindowControlsLayout=qB{CGPoint=dd}}88@0:8@\"SBDisplayItem\"16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGRect={CGPoint=dd}{CGSize=dd}}56"
+ "{SBWindowControlsLayout=qB{CGPoint=dd}}88@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGRect={CGPoint=dd}{CGSize=dd}}56"
+ "{SBWindowControlsLayout=qB{CGPoint=dd}}88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48@80"
+ "{SBWindowControlsLayout=qB{CGPoint=dd}}88@?0@\"SBChainableModifier\"8@16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGRect={CGPoint=dd}{CGSize=dd}}56"
+ "\xb4\xd1"
+ "\xf0\xf0r"
+ "\xf0\xf0\xc11!"
- "-[SBDisplayItemLayoutAttributesProvider updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:]"
- "@\"<SBUISceneSafeAreaSettings>\""
- "@\"SBKeyboardFocusTarget\"24@0:8o^B16"
- "@140@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80d88d96d104d112B120B124B128B132B136"
- "@160@0:8@16q24@32d40d48{CGRect={CGPoint=dd}{CGSize=dd}}56B88B92{CGRect={CGPoint=dd}{CGSize=dd}}96{CGRect={CGPoint=dd}{CGSize=dd}}128"
- "@176@0:8@16q24@32d40d48{CGRect={CGPoint=dd}{CGSize=dd}}56B88B92@96q104{CGRect={CGPoint=dd}{CGSize=dd}}112{CGRect={CGPoint=dd}{CGSize=dd}}144"
- "@184@0:8@16@24Q32q40@48d56d64{CGRect={CGPoint=dd}{CGSize=dd}}72B104B108q112{CGRect={CGPoint=dd}{CGSize=dd}}120{CGRect={CGPoint=dd}{CGSize=dd}}152"
- "@200@0:8@16@24@32Q40q48@56d64d72{CGRect={CGPoint=dd}{CGSize=dd}}80B112B116q120q128{CGRect={CGPoint=dd}{CGSize=dd}}136{CGRect={CGPoint=dd}{CGSize=dd}}168"
- "@232@0:8q16q24q32{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}40{SBDisplayItemTileConfiguration=q{CGSize=dd}}96{CGPoint=dd}120B136q140{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}148{CGPoint=dd}204B220q224"
- "@40@0:8@?16q24@32"
- "@48@0:8@16@24Q32q40"
- "@72@0:8@16@24@32Q40q48@56q64"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "B64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48d56"
- "Called into the flexible autolayout controller when not in flexible windowing."
- "CommandQKeyboardShortcut"
- "NoFloatingAppLayouts"
- "Preventing the floating app move gesture because there's no floating app."
- "Preventing the floating app present gesture because the floating app is not stashed / undefined."
- "Preventing the floating app present gesture from the left edge because the floating app is not stashed on the left."
- "Preventing the floating app present gesture from the right edge because the floating app is not stashed on the right."
- "Q!q"
- "QUIT_APP_DISCOVERABILITY"
- "QUIT_DISCOVERABILITY"
- "SBDisplayItemLayoutAttributes.m"
- "SBFloatingConfigurationForMovingFloatingApplication"
- "SBMoveFloatingApplicationUtilities.m"
- "SBSlideOverTongueRightEdgeHintStartPeekingTimerReason"
- "SBSlideOverTongueRightEdgeHintStopPeekingTimerReason"
- "SBTransientlyVisibleSlideOverTongueSwitcherModifier"
- "SBTransientlyVisibleSlideOverTongueSwitcherModifier.m"
- "SBUISceneSafeAreaSettings"
- "T@\"<SBUISceneSafeAreaSettings>\",&,N,V_preferredSafeAreaSettings"
- "T@\"<SBUISceneSafeAreaSettings>\",R,N"
- "T@\"UITapGestureRecognizer\",&,N,V_alongsidePresentTapRecognizer"
- "TB,D,N,GisSiriVisible"
- "TB,D,N,GisSpotlightVisible"
- "TB,N,V_shouldActivateWithThreshold"
- "TB,R,N,GisSpolightPresentedAsTransientOverlay"
- "TQ,R,N,V_mode"
- "[State.Blocked] --> moving to .preparing"
- "^{_SBAppLayoutAutoLayoutSpaceCacheKeyDisplayItemRecord={CGSize=dd}{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}{CGPoint=dd}qqq{SBDisplayItemTileConfiguration=q{CGSize=dd}}q}"
- "_alongsidePresentTapRecognizer"
- "_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:layoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
- "_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:usingNewLayoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
- "_buildQuitMenuWithAdditionalOptions:"
- "_bundleIDShowingInlineAppExpose"
- "_cameraIsHosted"
- "_edgeProtectEdge"
- "_effectiveStageAreaForSnappingForSpace:configuration:"
- "_floatingConfigurationForActivatedEdge:"
- "_handleTapOnClosedMenu:"
- "_initWithContentOrientation:lastInteractionTime:sizingPolicy:attributedSize:tileConfiguration:normalizedCenter:cascaded:occlusionState:attributedUserSizeBeforeOverlapping:unoccludedPeekingCenter:positionIsSystemManaged:version:"
- "_initialVisibleAppLayouts"
- "_isStripVisibleForBoundingBox:configuration:effectiveStripWidth:"
- "_isUnpinGestureAllowedToMoveWindowsAtLocationInReferenceCoordinateSpace:"
- "_modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:"
- "_rightEdgeHintState"
- "_safeAreaCornerInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:"
- "_shouldActivateWithThreshold"
- "_siriVisible"
- "_sizeForAttributedSize:inBounds:defaultSize:screenEdgePadding:sizingPolicy:dockHeightWithPadding:interItemSpacing:"
- "_snapPositionOfTopMostItemIfNecessaryInSpace:autoLayoutConfiguration:snappedEdgesMask:"
- "_snapPositionOfTopMostItemToRect:inSpace:autoLayoutConfiguration:considerAdjacency:snappedEdgesMask:itemForPotentialPairing:"
- "_snapSizeOfResizingDisplayItemIfNecessaryForSpace:configuration:snappedEdgesMask:"
- "_snapSizeOfResizingDisplayItemToRect:inSpace:windowingConfiguration:considerAdjacency:snappedEdgesMask:newFrame:"
- "_spotlightVisible"
- "_stageAreaForBoundingBox:configuration:effectiveStripWidth:"
- "_updateInterfaceAppearance"
- "accepting policy: secret scene - banner hosted"
- "accepting policy: secret scene - siri above coversheet"
- "accepting policy: secret scene - transient overlay hosted"
- "accepting policy: secret scene - transient overlay hosted above coversheet"
- "accepting policy: spotlight visible (non-transient overlay)"
- "activeTransientOverlayPresentationCanBecomeFirstResponder"
- "activeTransientOverlayPresentationShouldUseSceneBasedKeyboardFocus"
- "alongsidePresentTapRecognizer"
- "appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
- "appLayoutByPerformingAutoLayoutForAppLayout:previousAppLayout:usingLayoutAttributes:options:containerOrientation:windowScene:source:"
- "cameraIsHosted"
- "centerInBounds:dockHeightIncludingPadding:interItemSpacing:"
- "chamois or flexible windowing is enabled"
- "coverSheetSlidingViewControllerCleanupInterstitialWhileOffScreen:"
- "coverSheetSlidingViewControllerIsInterstitialAllowed:"
- "defaultWindowControlsLayoutForDisplayItem:frame:containerBounds:interfaceOrientation:"
- "deferring events to coversheet hosted app %@ - camera is hosted: %@"
- "deferring events to coversheet hosted app but scene doesn't exist yet - camera is hosted: %@"
- "effectiveMinCenterX < effectiveMaxCenterX"
- "flexibleAutoLayoutSpaceForAppLayout:calculatedUsingNewLayoutAttributesMap:flexibleAutoLayoutSource:"
- "flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
- "flexibleWindowingAutoLayoutSpaceForAppLayout:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:newLayoutAttributes:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
- "focusTargetForActiveTransientOverlayPresentation"
- "focusTargetForCoverSheetHostedAppGetCameraIsHosted:"
- "frameForLayoutRole:inAppLayout:containerBounds:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:isChamoisWindowingUIEnabled:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
- "has"
- "hasActiveTransientOverlayPresentation"
- "initWithAuthenticationCoordinator:stateMachine:buttonActionsFactory:displayLinkController:launchEventExecutor:uiFlusher:multiDisplayUserInteractionCoordinator:userInterfaceStyleProvider:screenshotManager:"
- "initWithBlockedState:preparingForRemoteUnlockState:waitingForRemoteUnlockState:waitingForScenesState:waitingForHIDServicesState:activatingState:updatingActiveDisplayState:launchingState:flushingState:activeState:"
- "initWithGestureID:initialAppLayout:selectedDisplayItem:"
- "initWithMode:"
- "is NOT"
- "isActiveTransientOverlayPresentationFromSceneWithIdentityTokenString:"
- "isActiveTransientOverlayPresentationIsFromSceneWithIdentityTokenString:"
- "isBannerKitHostingSceneWithIdentityTokenString:"
- "isSpolightPresentedAsTransientOverlay"
- "kill application for keyboard shortcut"
- "knownCaptureApplicationsByBundleIdentifier"
- "mode != SBSlideOverTongueTransientlyVisibleModeNone"
- "negativeVelocity < 0.0f"
- "perspectiveAngleForLayoutRole:inAppLayout:"
- "policy: %{public}@ is not a banner kit hosted secret scene"
- "policy: %{public}@ not siri secret scene"
- "policy: Siri -- not deferring to SB"
- "policy: active transient overlay presentation but doesn't want scene based focus or is outvoted by a more recent SB focus lock"
- "policy: activeTransientOverlay is not %{public}@ and has no keyboardFocusTarget; ignoring request."
- "policy: activeTransientOverlay is not %{public}@. Using topmost: %{public}@."
- "policy: activeTransientOverlay with scene-based deferring above coversheet -- not deferring to SB"
- "policy: activeTransientOverlay with scene-based deferring is arbiter target -- not deferring to SB"
- "policy: arbiter target %{public}@ is scene-backed banner, not deferring to SB"
- "policy: control center is visible"
- "policy: control center is visible and overriding transient overlays"
- "policy: coversheet %s hosting an app and %s active transient overlay presentation"
- "policy: deferring events from SpringBoard to CoverSheet hosted app, but scene doesn't exist yet (camera is hosted:%{BOOL}u)"
- "policy: deferring events from SpringBoard to CoverSheet hosted app: %{public}@ (camera is hosted:%{BOOL}u)"
- "policy: preferSpringBoardFocus for reasons:(%{public}@)"
- "policy: spotlight visible (non-transient overlay)"
- "positiveVelocity > 0.0f"
- "presentEntity:fromRequest:animated:withEphemeralSwitcher:dismissGestureEnabled:completion:"
- "q84@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56B64q68@76"
- "q84@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48@56B64q68^{CGRect={CGPoint=dd}{CGSize=dd}}76"
- "quitMenuWithOptions:"
- "rejecting target: preferring SB for reasons: %@"
- "safeAreaCornerInsets"
- "safeAreaEdgeInsets"
- "safeAreaEdgeInsetsForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:"
- "sb_safeAreaSettings"
- "setAlongsidePresentTapRecognizer:"
- "setCameraIsHosted:"
- "setPasscodeLockVisible:animated:showBackground:completion:"
- "setSafeAreaCornerInsets:"
- "setSafeAreaEdgeInsets:"
- "setShouldActivateWithThreshold:"
- "setSiriVisible:"
- "setSpotlightVisible:"
- "shouldActivateWithThreshold"
- "slideOverTongueTransientlyVisibleModeForEvent:"
- "spaceByPerformingFlexibleAutoLayoutWithSpace:configuration:options:source:"
- "spotlightPresentedAsTransientOverlay"
- "systemQuitMenuWithOptions:"
- "updateLayoutAttributes:ofDisplayItem:inAppLayout:"
- "updateLayoutAttributes:ofDisplayItem:inAppLayout:displayOrdinal:orientation:"
- "v32@?0@\"SBTransientOverlayViewController\"8Q16^B24"
- "v40@0:8@\"SBDisplayItemLayoutAttributes\"16@\"SBDisplayItem\"24@\"SBAppLayout\"32"
- "v52@0:8@16@24B32B36B40@?44"
- "v56@0:8@\"SBDisplayItemLayoutAttributes\"16@\"SBDisplayItem\"24@\"SBAppLayout\"32q40q48"
- "windowControlsLayoutForApplicationFrame:screenBounds:activationSettings:interfaceOrientation:"
- "windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:"
- "{?=\"switcherContentControllerBringAppLayoutToFront\"b1\"switcherContentControllerActivatedBestAppSuggestion\"b1\"updateUserInteractionEnabledForSwitcherContentController\"b1\"updateWindowVisibilityForSwitcherContentController\"b1\"switcherContentControllerSetHomeScreenScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenAlphaWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenDimmingAlphaWithSettingsAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurProgressWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurType\"b1\"switcherContentControllerSetHomeScreenBackdropBlurMaterialRecipeNameWithAnimationModeCompletion\"b1\"switcherContentControllerControlsWallpaper\"b1\"switcherContentControllerSetWallpaperScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetWallpaperStyle\"b1\"switcherContentControllerSetInterfaceOrientation\"b1\"switcherContentControllerSetInterfaceOrientationFromUserResizingForDisplayItem\"b1\"switcherContentControllerRequestNewWindowForBundleIdentifier\"b1\"switcherContentControllerSetContainerStatusBarHiddenPartsHiddenAnimationDuration\"b1\"switcherContentControllerWantsToDismissMenuBar\"b1\"switcherContentControllerWantsToPeekMenuBar\"b1\"switcherContentControllerWantsToUpdateMenuBarVisibility\"b1\"switcherContentControllerDemoLayoutAttributesForDisplayItem\"b1\"switcherContentControllerSetPointerInteractionsEnabled\"b1\"switcherContentControllerShouldResignActiveForStartOfTransition\"b1\"switcherContentControllerControlsHomeScreenContents\"b1\"switcherContentControllerSetCacheAsynchronousRenderingSurfaces\"b1\"cancelActiveGestureForSwitcherContentController\"b1\"switcherContentControllerReopenHiddenAppLayoutsWithBundleIdentifier\"b1\"switcherContentControllerLayoutStateTransitionDidEndWithTransitionContext\"b1\"switcherContentControllerTransformForCardUnderSheetForBoundsSize\"b1\"switcherContentControllerMoveDisplayItemFromOtherDisplay\"b1\"presentContinuousExposeStripRevealGrabberTongueImmediatelyForSwitcherContentController\"b1\"tickleContinuousExposeStripRevealGrabberTongueIfVisibleForSwitcherContentController\"b1\"switcherContentControllerDidUpdateVisibleHomeAffordances\"b1\"switcherContentControllerRemoveDisplayItemsFromDesktop\"b1\"switcherContentControllerRequestDismissalForHomeScreenBackgroundTaps\"b1}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}172@0:8q16@24{CGRect={CGPoint=dd}{CGSize=dd}}32q64@72d80d88B96B100B104{CGRect={CGPoint=dd}{CGSize=dd}}108{CGRect={CGPoint=dd}{CGSize=dd}}140"
- "{CGSize=dd}152@0:8{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}16{CGRect={CGPoint=dd}{CGSize=dd}}72{CGSize=dd}104d120q128d136d144"
- "{SBWindowControlsLayout=qB{CGPoint=dd}}88@?0@\"SBChainableModifier\"8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80"
- "{SBWindowControlsLayout=qB{CGPoint=dd}}96@0:8@\"SBDisplayItem\"16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGRect={CGPoint=dd}{CGSize=dd}}56q88"
- "{SBWindowControlsLayout=qB{CGPoint=dd}}96@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGRect={CGPoint=dd}{CGSize=dd}}56q88"
- "{SBWindowControlsLayout=qB{CGPoint=dd}}96@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48@80q88"
- "{UIEdgeInsets=dddd}96@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48@80q88"
- "{_UICornerInsets={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}}96@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48@80q88"
- "\xa4\xd1"
- "\xf0\xf02"
- "\xf0\xf0\xb11!"
- "\xf0\xf0\xc1"

```
