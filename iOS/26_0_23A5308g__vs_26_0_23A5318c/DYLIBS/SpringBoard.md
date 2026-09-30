## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.0.9.100.0
-  __TEXT.__text: 0xa7df44
-  __TEXT.__auth_stubs: 0x5500
+4557.0.10.106.0
+  __TEXT.__text: 0xa85294
+  __TEXT.__auth_stubs: 0x5530
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb74c0
-  __TEXT.__const: 0x12c20
-  __TEXT.__oslogstring: 0x5d829
-  __TEXT.__cstring: 0x7ca15
-  __TEXT.__gcc_except_tab: 0x16d98
+  __TEXT.__objc_methlist: 0xb7a20
+  __TEXT.__const: 0x12cd0
+  __TEXT.__oslogstring: 0x5e455
+  __TEXT.__cstring: 0x7cdcb
+  __TEXT.__gcc_except_tab: 0x17890
   __TEXT.__ustring: 0xcac
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2be40
+  __TEXT.__unwind_info: 0x2c0e8
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x220e5
-  __TEXT.__objc_methname: 0x1cd603
-  __TEXT.__objc_methtype: 0x4c52c
-  __TEXT.__objc_stubs: 0xf2e60
-  __DATA_CONST.__got: 0xa0f8
-  __DATA_CONST.__const: 0x1ca58
-  __DATA_CONST.__objc_classlist: 0x5240
+  __TEXT.__objc_classname: 0x220c0
+  __TEXT.__objc_methname: 0x1ced6a
+  __TEXT.__objc_methtype: 0x4c859
+  __TEXT.__objc_stubs: 0xf38a0
+  __DATA_CONST.__got: 0xa120
+  __DATA_CONST.__const: 0x1cca8
+  __DATA_CONST.__objc_classlist: 0x5238
   __DATA_CONST.__objc_catlist: 0x348
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a5d8
+  __DATA_CONST.__objc_selrefs: 0x4a8f0
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3f80
-  __DATA_CONST.__objc_arraydata: 0x1830
-  __AUTH_CONST.__auth_got: 0x2a98
-  __AUTH_CONST.__const: 0x108e8
-  __AUTH_CONST.__cfstring: 0x6eb00
-  __AUTH_CONST.__objc_const: 0x2684f8
-  __AUTH_CONST.__objc_arrayobj: 0x1740
+  __DATA_CONST.__objc_superrefs: 0x3f70
+  __DATA_CONST.__objc_arraydata: 0x1850
+  __AUTH_CONST.__auth_got: 0x2ab0
+  __AUTH_CONST.__const: 0x10958
+  __AUTH_CONST.__cfstring: 0x6ee00
+  __AUTH_CONST.__objc_const: 0x2691e0
+  __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x680
-  __AUTH_CONST.__objc_intobj: 0x2bb0
+  __AUTH_CONST.__objc_intobj: 0x2bc8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x10450
-  __DATA.__objc_ivar: 0xf290
+  __AUTH.__objc_data: 0x10400
+  __DATA.__objc_ivar: 0xf320
   __DATA.__data: 0x1f8b8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xa98
+  __DATA.__bss: 0xaa0
   __DATA.__common: 0xa40
   __DATA_DIRTY.__objc_data: 0x23230
   __DATA_DIRTY.__data: 0x180
-  __DATA_DIRTY.__bss: 0x1a80
+  __DATA_DIRTY.__bss: 0x1a78
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: E710F3EB-903D-3F2E-A529-283E621C7850
-  Functions: 69871
-  Symbols:   236265
-  CStrings:  103821
+  UUID: 125455D2-E42B-3BE0-AD84-4ACF04907FFC
+  Functions: 70023
+  Symbols:   236758
+  CStrings:  104059
 
Symbols:
+ +[SBSwitcherGenieAttributes genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:minimizedScale:containerSize:minimumOutsetSize:genieScale:multiplier:active:layoutSettings:]
+ -[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:]
+ -[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewFrame:forAppLayout:]
+ -[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewPerspectiveAngle:forAppLayout:]
+ -[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewScale:forAppLayout:]
+ -[SBAppExposeToAppWindowingModifier animationAttributesForLayoutRole:inAppLayout:withAnimationAttributes:]
+ -[SBAppExposeToAppWindowingModifier cornersForItem:]
+ -[SBAppExposeToAppWindowingModifier opacityForLayoutRole:inAppLayout:atIndex:]
+ -[SBAppExposeToAppWindowingModifier perspectiveAngleForItem:]
+ -[SBAppExposeToAppWindowingModifier stripDidChange:]
+ -[SBAppExposeToAppWindowingModifier titleStyleForItem:]
+ -[SBAppSwitcherContinuousExposeSwitcherModifier _forwardingTargetForUpdate]
+ -[SBAppSwitcherSystemService initWithSwitcherCoordinator:commandTabController:]
+ -[SBAppSwitcherSystemService systemServiceServer:resetLayoutAttributesForClient:completion:]
+ -[SBAppViewController applicationSceneViewController:didUpdateStatusBarHidden:]
+ -[SBApplication clearLastWindowLayoutAttributes]
+ -[SBApplication lastWindowLayoutAttributesForDisplayOrdinal:]
+ -[SBApplication setLastWindowLayoutAttributes:forDisplayOrdinal:]
+ -[SBApplicationDropSession allowsCommandeering]
+ -[SBApplicationPlaceholderController _finishPlaceholder:].cold.1
+ -[SBApplicationPlaceholderController _finishPlaceholder:].cold.2
+ -[SBAssistantController notifyAssistantOfApplicationTransition]
+ -[SBAssistantController notifyAssistantOfApplicationTransition].cold.1
+ -[SBAssistantSceneController invalidate]
+ -[SBAssistantSceneController isObservingLayoutStateTransitions]
+ -[SBAssistantSceneController setObservingLayoutStateTransitions:]
+ -[SBBiomeAppearanceChangeObserver .cxx_destruct]
+ -[SBBiomeAppearanceChangeObserver _startObserving]
+ -[SBBiomeAppearanceChangeObserver appearancePublisher]
+ -[SBBiomeAppearanceChangeObserver cancellable]
+ -[SBBiomeAppearanceChangeObserver dealloc]
+ -[SBBiomeAppearanceChangeObserver init]
+ -[SBBiomeAppearanceChangeObserver invalidate]
+ -[SBBiomeAppearanceChangeObserver isObserving]
+ -[SBBiomeAppearanceChangeObserver lastAppearanceChangeTimestamp]
+ -[SBBiomeAppearanceChangeObserver setCancellable:]
+ -[SBBiomeAppearanceChangeObserver setLastAppearanceChangeTimestamp:]
+ -[SBBiomeAppearanceChangeObserver setObserving:]
+ -[SBContinuousExposeAppDragAndDropGestureSwitcherModifier isHitTestBlockingViewVisible]
+ -[SBContinuousExposeRootSwitcherModifier handleTimerEvent:]
+ -[SBContinuousExposeWindowDropSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:]
+ -[SBContinuousExposeWindowDropSwitcherModifier fullyPresentedFrameForIndex:frame:]
+ -[SBContinuousExposeWindowDropSwitcherModifier initWithTransitionID:selectedDisplayItem:toAppLayout:initialAppLayout:liftOffVelocity:]
+ -[SBContinuousExposeWindowDropSwitcherModifier initWithTransitionID:selectedDisplayItem:toAppLayout:initialAppLayout:liftOffVelocity:].cold.1
+ -[SBContinuousExposeWindowDropSwitcherModifier liftOffVelocity]
+ -[SBCoverSheetPresentationManager _isIconFlyInAnimationAllowed]
+ -[SBCoverSheetPresentationManager _isIconFlyInAnimationAllowed].cold.1
+ -[SBCoverSheetPresentationManager coverSheetSlidingViewControllerIsInterstitialAllowed:]
+ -[SBCoverSheetSlidingViewController isPresentingDismissableOffScreenInterstitial]
+ -[SBDashBoardLockScreenEnvironment _handleCoverSheetTranslationForPasscodeLockVisible:blockingForOtherReasons:ignoringPreflightRequirementsForPresentation:]
+ -[SBDashBoardLockScreenEnvironment setPasscodeLockVisible:intent:ignoringPreflightRequirementsForPresentation:animated:completion:]
+ -[SBDashBoardSetupView _canStartGlassCursiveTitleAnimation]
+ -[SBDashBoardSetupView _startupDidFinish:]
+ -[SBDeckFloatingSwitcherModifier _forwardingTargetForUpdate]
+ -[SBDeckSwitcherModifier _forwardingTargetForUpdate]
+ -[SBDefaultImplementationsSwitcherModifier contentPageViewScaleForLayoutRole:inAppLayout:withContentPageViewScale:]
+ -[SBDefaultImplementationsSwitcherModifier isPendingViewsForAcceleratedHomeGesture]
+ -[SBDefaultImplementationsSwitcherModifier useItemContainerFooterViewsForAppLayout:]
+ -[SBDeviceApplicationSceneHandle(SwitcherCapabilities) _updateDisableMultitaskingWhileForegroundAssertionIfNeeded]
+ -[SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager .cxx_destruct]
+ -[SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager _updateMedusaMultitaskingEnabled]
+ -[SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager acquireDisableMultitaskingAssertionForSceneHandle:]
+ -[SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager acquireDisableMultitaskingAssertionForSceneHandle:].cold.1
+ -[SBDisplayItemLayoutAttributesProvider updateEntriesWithBlock:]
+ -[SBDisplayItemLayoutAttributesStorage updateEntriesWithBlock:]
+ -[SBExposeWindowingModifier contentPageViewScaleForLayoutRole:inAppLayout:withContentPageViewScale:]
+ -[SBExposeWindowingModifier useItemContainerFooterViewsForAppLayout:]
+ -[SBFlexibleWindowingExposeToHomePeekWindowingModifier titleStyleForItem:]
+ -[SBFluidSwitcherAnimationSettings genieCornerRadiusToAppResetDelay]
+ -[SBFluidSwitcherAnimationSettings genieCornerRadiusToHomeResetDelay]
+ -[SBFluidSwitcherAnimationSettings homeGestureZoomDownScaleMultiplierWidgets]
+ -[SBFluidSwitcherAnimationSettings homeGestureZoomDownScaleMultiplier]
+ -[SBFluidSwitcherAnimationSettings setGenieCornerRadiusToAppResetDelay:]
+ -[SBFluidSwitcherAnimationSettings setGenieCornerRadiusToHomeResetDelay:]
+ -[SBFluidSwitcherAnimationSettings setHomeGestureZoomDownScaleMultiplier:]
+ -[SBFluidSwitcherAnimationSettings setHomeGestureZoomDownScaleMultiplierWidgets:]
+ -[SBFluidSwitcherGestureManager _handleScrollToTopGesture:]
+ -[SBFluidSwitcherGestureManager _shouldBeginWindowTopRegionTapGesture:]
+ -[SBFluidSwitcherGestureManager _shouldTopRegionScrollToTopGesture:receiveTouch:]
+ -[SBFluidSwitcherGestureManager setWindowTopRegionScrollToTopTapGestureRecognizer:]
+ -[SBFluidSwitcherGestureManager windowTopRegionScrollToTopTapGestureRecognizer]
+ -[SBFluidSwitcherItemContainer _setWantsOverlayPortalView:]
+ -[SBFluidSwitcherItemContainer _updateFooterAnimated:]
+ -[SBFluidSwitcherItemContainer _updateFooterVisibility]
+ -[SBFluidSwitcherItemContainer drawsFooter]
+ -[SBFluidSwitcherItemContainer footerStyle]
+ -[SBFluidSwitcherItemContainer genieEffectViewDidBegin:]
+ -[SBFluidSwitcherItemContainer gestureRecognizer:shouldRequireFailureOfGestureRecognizer:]
+ -[SBFluidSwitcherItemContainer iconAlignment]
+ -[SBFluidSwitcherItemContainer iconHitTestOutset]
+ -[SBFluidSwitcherItemContainer iconOpacity]
+ -[SBFluidSwitcherItemContainer itemContainerFooterView:didSelectTitleItem:]
+ -[SBFluidSwitcherItemContainer overlayPortalView]
+ -[SBFluidSwitcherItemContainer setDrawsFooter:]
+ -[SBFluidSwitcherItemContainer setFooterStyle:]
+ -[SBFluidSwitcherItemContainer setIconAlignment:]
+ -[SBFluidSwitcherItemContainer setIconHitTestOutset:]
+ -[SBFluidSwitcherItemContainer setIconOpacity:]
+ -[SBFluidSwitcherItemContainer setOverlayPortalView:]
+ -[SBFluidSwitcherItemContainer setTitleAndIconOpacity:]
+ -[SBFluidSwitcherItemContainer setTitleItems:]
+ -[SBFluidSwitcherItemContainer setTitleItems:animated:]
+ -[SBFluidSwitcherItemContainer setTitleOpacity:]
+ -[SBFluidSwitcherItemContainer setUniqueIconsOnly:]
+ -[SBFluidSwitcherItemContainer setWantsPointerInteractions:]
+ -[SBFluidSwitcherItemContainer titleAndIconOpacity]
+ -[SBFluidSwitcherItemContainer titleItems]
+ -[SBFluidSwitcherItemContainer titleOpacity]
+ -[SBFluidSwitcherItemContainer uniqueIconsOnly]
+ -[SBFluidSwitcherItemContainer wantsOverlayPortal]
+ -[SBFluidSwitcherItemContainer wantsPointerInteractions]
+ -[SBFluidSwitcherItemContainerFooterView tapGestureRecognizer]
+ -[SBFluidSwitcherPersonality shouldDeferVisibleOverlayAndUnderlayViewsUpdate]
+ -[SBFluidSwitcherSpaceOverlayAccessoryView genieEffectViewDidBegin:]
+ -[SBFluidSwitcherSpaceTitleItemController initWithAppLayout:applicationSceneHandleProvider:displayIdentity:showCanvasTitles:isChamoisOrFlexibleWindowingEnabled:isFooterViewOfItemContainer:]
+ -[SBFluidSwitcherSpaceTitleItemController initWithAppLayout:applicationSceneHandleProvider:displayIdentity:showCanvasTitles:isChamoisOrFlexibleWindowingEnabled:isFooterViewOfItemContainer:].cold.1
+ -[SBFluidSwitcherSpaceTitleItemController isFooterViewOfItemContainer]
+ -[SBFluidSwitcherViewController _didSelectHeaderForLayoutRole:inAppLayout:]
+ -[SBFluidSwitcherViewController _forLoggingOnly_enumerateQueryResponderChainStartingAtModifier:usingBlock:]
+ -[SBFluidSwitcherViewController _forLoggingOnly_enumerateQueryResponderChainStartingAtModifier:usingBlock:].cold.1
+ -[SBFluidSwitcherViewController _isFrameValid:]
+ -[SBFluidSwitcherViewController _isPointValid:]
+ -[SBFluidSwitcherViewController _modifierViolatingTest:forAnchorPointForIndex:]
+ -[SBFluidSwitcherViewController _modifierViolatingTest:forFrameForIndex:]
+ -[SBFluidSwitcherViewController _modifierViolatingTest:forFrameForLayoutRole:inAppLayout:withBounds:]
+ -[SBFluidSwitcherViewController _modifierViolatingTest:forPerspectiveAngleForIndex:]
+ -[SBFluidSwitcherViewController _modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:]
+ -[SBFluidSwitcherViewController _modifierViolatingValidFloatForScaleForIndex:]
+ -[SBFluidSwitcherViewController _modifierViolatingValidFloatForScaleForLayoutRole:inAppLayout:]
+ -[SBFluidSwitcherViewController _performModifierIconOverlayVisibilityUpdateResponse:].cold.1
+ -[SBFluidSwitcherViewController _updateAccessoryTitlePresenceForAdjustedAppLayout:]
+ -[SBFluidSwitcherViewController _updateItemContainerTitlePresenceForLeafAppLayout:]
+ -[SBFluidSwitcherViewController _updateTitlePresenceOnItemContainersForAdjustedAppLayout:]
+ -[SBFluidSwitcherViewController currentGenieFrameForVisibleAppLayout:]
+ -[SBFluidSwitcherViewController displayItemPrefersStatusBarHidden:]
+ -[SBFluidSwitcherViewController gestureHandlingModifierReleasePendingViews:]
+ -[SBFluidSwitcherViewController homeScreenIconBadgeOffsetForAppLayout:]
+ -[SBFluidSwitcherViewController homeScreenIconBadgeSizeForAppLayout:]
+ -[SBFluidSwitcherViewController isStatusBarPartPreferredHiddenByApp:]
+ -[SBFluidSwitcherViewController itemContainer:didSelectTitleForRole:]
+ -[SBFluidSwitcherViewController itemContainer:didSelectTitleForRole:].cold.1
+ -[SBFluidSwitcherViewController itemContainerDidUpdateWantsOverlayPortal:]
+ -[SBFluidSwitcherViewController liveContentOverlay:didUpdateStatusBarHiddenSceneSettings:]
+ -[SBFluidSwitcherViewController performDeferredUpdateVisibleOverlayAndUnderlayViews]
+ -[SBFluidSwitcherViewController prioritizesSortOrderForAppLayout:]
+ -[SBFullScreenContinuousExposeSwitcherModifier _responseForDismissingStrip]
+ -[SBFullScreenContinuousExposeSwitcherModifier _updateStripModifierIfNeeded]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay applicationSceneViewController:didUpdateStatusBarHidden:]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay medusaDecoratedApplicationSceneViewController:didUpdateStatusBarHidden:]
+ -[SBFullScreenToHomeIconZoomSwitcherModifier canAddVelocityKickToHurdleDock]
+ -[SBFullScreenToHomeIconZoomSwitcherModifier setCanAddVelocityKickToHurdleDock:]
+ -[SBFullScreenToHomeIconZoomSwitcherModifier wallpaperScale]
+ -[SBGestureInitiatedIconZoomAnimationAttributesSwitcherModifier genieAttributesForAppLayout:]
+ -[SBGlassBannerTransitionAnimator _addGaussianBlurToViewIfNeeded:]
+ -[SBGlassBannerTransitionAnimator _removeGaussianBlurFromViewIfNeeded:]
+ -[SBGridLayoutSwitcherModifier _forwardingTargetForUpdate]
+ -[SBHomeGestureSwitcherModifier isPendingViewsForAcceleratedHomeGesture]
+ -[SBHomeGestureToZoomDownSwitcherModifier initWithTransitionID:appLayout:nonGestureInitiatedZoomModifier:effectiveStartingEnvironmentMode:liftOffVelocity:adjustAnimationAttributes:showingOrAnimatingCardsForFlyIn:]
+ -[SBHomeGestureToZoomDownSwitcherModifier initWithTransitionID:appLayout:nonGestureInitiatedZoomModifier:effectiveStartingEnvironmentMode:liftOffVelocity:adjustAnimationAttributes:showingOrAnimatingCardsForFlyIn:].cold.1
+ -[SBHomePeekWindowingModifier titleStyleForItem:]
+ -[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]
+ -[SBLockScreenManager setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]
+ -[SBLockScreenViewControllerBase setPasscodeLockVisible:intent:ignoringPreflightRequirementsForPresentation:animated:completion:]
+ -[SBMainSwitcherControllerCoordinator prioritizesSortOrderForAppLayout:]
+ -[SBMainSwitcherControllerCoordinator resetLayoutAttributesWithCompletion:]
+ -[SBMedusaDecoratedDeviceApplicationSceneViewController applicationSceneViewController:didUpdateStatusBarHidden:]
+ -[SBMenuBarManager cancelMenuBarRevealForHeldModifierKey]
+ -[SBMenuBarManager heldModifierKeyRevealTimer]
+ -[SBMenuBarManager scheduleMenuBarRevealForHeldModifierKey]
+ -[SBMenuBarManager setHeldModifierKeyRevealTimer:]
+ -[SBMenuBarSettings menuRevealExtraYThresholdForPointerWhenUnderExternalDisplay]
+ -[SBMenuBarSettings setMenuRevealExtraYThresholdForPointerWhenUnderExternalDisplay:]
+ -[SBMinimumViableSwitcherTableViewController isStatusBarPartPreferredHiddenByApp:]
+ -[SBMixedGridSwitcherModifier _forwardingTargetForUpdate]
+ -[SBPosterBoardUpdateManager _schedulerQueue_submitTaskRequestForUpdate:updateIdentifier:]
+ -[SBPosterBoardUpdateManager executeUpdate:forBackgroundTask:updateIdentifier:]
+ -[SBPowerAlertElement _primaryTextFontSize]
+ -[SBPowerAlertElement _primaryTextFontSize].cold.1
+ -[SBPowerAlertElement customEdgeSpacing]
+ -[SBPowerAlertElement dodgeSensorAreaOnIntrinsicContentSize]
+ -[SBPowerAlertElement horizontalSpacingBetweenLeadingAndCenter]
+ -[SBPowerAlertElement horizontalSpacingBetweenTrailingAndCenter]
+ -[SBPowerAlertElement verticalItemSpacing]
+ -[SBPowerAlertElement verticalSpacingBetweenPrimaryAndSecondary]
+ -[SBPowerAlertElement verticalSpacingBetweenPrimaryAndSecondary].cold.1
+ -[SBRecordingIndicatorViewController _shouldReverseScaleWhenDisplayZoomedInLocation:]
+ -[SBRoutingSwitcherModifier _forwardingTargetForUpdate]
+ -[SBRoutingSwitcherModifier contentPageViewScaleForLayoutRole:inAppLayout:withContentPageViewScale:]
+ -[SBRoutingSwitcherModifier isPendingViewsForAcceleratedHomeGesture]
+ -[SBRoutingSwitcherModifier useItemContainerFooterViewsForAppLayout:]
+ -[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:context:]
+ -[SBSceneManagerCoordinator sceneHandleDisableMultitaskingAssertionManager]
+ -[SBSceneSnapshotRequestContext lastAppearanceChangeTimestamp]
+ -[SBSceneSnapshotRequestContext setLastAppearanceChangeTimestamp:]
+ -[SBShelfCarouselSwitcherModifier _forwardingTargetForUpdate]
+ -[SBStripDismissalAnimationModifier topMostItems]
+ -[SBStripLayoutWindowingModifier .cxx_destruct]
+ -[SBStripLayoutWindowingModifier _appLayout:isContainedInStrip:]
+ -[SBStripLayoutWindowingModifier _applyAnimationAttributes:forAppLayout:]
+ -[SBStripLayoutWindowingModifier _highlightScaleForAppLayout:pileIndex:]
+ -[SBStripLayoutWindowingModifier _isGroupForAppLayoutHighlightedFromHover:]
+ -[SBStripLayoutWindowingModifier _isGroupForAppLayoutHighlightedFromTouch:]
+ -[SBStripLayoutWindowingModifier _isStripStashed]
+ -[SBStripLayoutWindowingModifier _positionForPositionIn3DContainerSpace:layerPosition:layerSize:layerAnchorPoint:layerTransform:containerPerspective:]
+ -[SBStripLayoutWindowingModifier _stripIdentifierForAppLayout:]
+ -[SBStripLayoutWindowingModifier _stripItems]
+ -[SBStripLayoutWindowingModifier _stripOriginX]
+ -[SBStripLayoutWindowingModifier _visibleStripItems]
+ -[SBStripLayoutWindowingModifier _wallpaperDimmingForAppLayout:row:pileIndex:]
+ -[SBStripLayoutWindowingModifier _wallpaperGradientAttributesForAppLayout:viewModel:row:pileIndex:]
+ -[SBStripLayoutWindowingModifier didUpdate]
+ -[SBStripLayoutWindowingModifier frameForItem:]
+ -[SBStripLayoutWindowingModifier gestureDidComplete:]
+ -[SBStripLayoutWindowingModifier gestureWillBegin:]
+ -[SBStripLayoutWindowingModifier highlightDidChange:]
+ -[SBStripLayoutWindowingModifier init]
+ -[SBStripLayoutWindowingModifier layoutViewModelsIfNeeded]
+ -[SBStripLayoutWindowingModifier topMostItems]
+ -[SBStripLayoutWindowingModifier transitionDidUpdate:]
+ -[SBStripLayoutWindowingModifier visibleItems]
+ -[SBStripLayoutWindowingModifier willBegin]
+ -[SBSwitcherController _stopObservingSceneHandles]
+ -[SBSwitcherController isLeadingStatusBarRegionPreferredHiddenByApp]
+ -[SBSwitcherController isTrailingStatusBarRegionPreferredHiddenByApp]
+ -[SBSwitcherGenieAttributes meshContainerOutset]
+ -[SBSwitcherGenieAttributes minimizedScale]
+ -[SBSwitcherGenieAttributes minimumOutsetSize]
+ -[SBSwitcherGenieAttributes setMinimizedScale:]
+ -[SBSwitcherGenieAttributes setMinimumOutsetSize:]
+ -[SBSwitcherGenieEffectView _layoutContentAndContainerViewWithAttributes:]
+ -[SBSwitcherGenieEffectView _updateGenieMeshTransformForPresentationLayer:properties:boundsProperty:attributes:]
+ -[SBSwitcherGenieEffectView addPortaledContentView:]
+ -[SBSwitcherGenieEffectView pointInside:withEvent:]
+ -[SBSwitcherGenieEffectView portaledContentShouldMatchSource]
+ -[SBSwitcherGenieEffectView setChildContentView:]
+ -[SBSwitcherGenieEffectView setPortaledContentShouldMatchSource:]
+ -[SBSwitcherGenieEffectView setPortaledContentViews:]
+ -[SBSwitcherLayoutTransitionNotes isRotation]
+ -[SBSystemApertureProvidedContentElement customEdgeSpacing]
+ -[SBSystemApertureProvidedContentElement dodgeSensorAreaOnIntrinsicContentSize]
+ -[SBSystemApertureProvidedContentElement horizontalSpacingBetweenLeadingAndCenter]
+ -[SBSystemApertureProvidedContentElement horizontalSpacingBetweenTrailingAndCenter]
+ -[SBSystemApertureProvidedContentElement verticalItemSpacing]
+ -[SBSystemApertureProvidedContentElement verticalSpacingBetweenPrimaryAndSecondary]
+ -[SBSystemServiceServer _handleRequestAppSwitcherResetLayoutAttributes:fromClient:]
+ -[SBWindowingModifier _forwardingTargetForUpdate]
+ -[SBWindowingStrip containsDisplayItem:]
+ -[SBWindowingStrip initWithAppLayoutsInStrip:]
+ -[SBWindowingStrip initWithAppLayoutsInStrip:].cold.1
+ -[SBWindowingSwitcherPersonality shouldDeferVisibleOverlayAndUnderlayViewsUpdate]
+ -[SpringBoard hasCompletedStartup]
+ -[_SBGridFloorSwitcherModifier _forwardingTargetForUpdate]
+ -[_SBSwitcherGenieEffectContentView hitTest:withEvent:]
+ -[_SBSwitcherGenieEffectContentView pointInside:withEvent:]
+ GCC_except_table114
+ GCC_except_table159
+ GCC_except_table161
+ GCC_except_table201
+ GCC_except_table217
+ GCC_except_table223
+ GCC_except_table233
+ GCC_except_table249
+ GCC_except_table255
+ GCC_except_table267
+ GCC_except_table277
+ GCC_except_table300
+ GCC_except_table303
+ GCC_except_table312
+ GCC_except_table315
+ GCC_except_table329
+ GCC_except_table346
+ GCC_except_table367
+ GCC_except_table381
+ GCC_except_table384
+ GCC_except_table390
+ GCC_except_table393
+ GCC_except_table403
+ GCC_except_table423
+ GCC_except_table438
+ GCC_except_table467
+ GCC_except_table475
+ GCC_except_table479
+ GCC_except_table494
+ GCC_except_table499
+ GCC_except_table507
+ GCC_except_table509
+ GCC_except_table512
+ GCC_except_table514
+ GCC_except_table516
+ GCC_except_table531
+ GCC_except_table535
+ GCC_except_table541
+ GCC_except_table545
+ GCC_except_table569
+ GCC_except_table615
+ GCC_except_table650
+ GCC_except_table720
+ GCC_except_table744
+ GCC_except_table747
+ GCC_except_table78
+ GCC_except_table788
+ GCC_except_table828
+ GCC_except_table867
+ GCC_except_table876
+ GCC_except_table920
+ GCC_except_table959
+ GCC_except_table966
+ GCC_except_table968
+ GCC_except_table970
+ GCC_except_table972
+ GCC_except_table974
+ GCC_except_table976
+ GCC_except_table978
+ _CAFrameRateRangeIsEqualToRange
+ _OBJC_CLASS_$_MSDKDemoState
+ _OBJC_CLASS_$_SBBiomeAppearanceChangeObserver
+ _OBJC_CLASS_$_SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager
+ _OBJC_CLASS_$_SBSUIRetailDemoSupportSceneExtension
+ _OBJC_CLASS_$_SBStripLayoutWindowingModifier
+ _OBJC_CLASS_$__SBSwitcherGenieEffectContentView
+ _OBJC_IVAR_$_SBAppExposeToAppWindowingModifier._hasForwardedUpdate
+ _OBJC_IVAR_$_SBAppSwitcherSystemService._switcherCoordinator
+ _OBJC_IVAR_$_SBApplication._cachedLastWindowLayoutAttributesPerDisplayOrdinal
+ _OBJC_IVAR_$_SBAssistantSceneController._observingLayoutStateTransitions
+ _OBJC_IVAR_$_SBBiomeAppearanceChangeObserver._appearancePublisher
+ _OBJC_IVAR_$_SBBiomeAppearanceChangeObserver._cancellable
+ _OBJC_IVAR_$_SBBiomeAppearanceChangeObserver._lastAppearanceChangeTimestamp
+ _OBJC_IVAR_$_SBBiomeAppearanceChangeObserver._observing
+ _OBJC_IVAR_$_SBContinuousExposeWindowDragRootSwitcherModifier._velocity
+ _OBJC_IVAR_$_SBContinuousExposeWindowDropSwitcherModifier._initialFrameOfMinimizingItem
+ _OBJC_IVAR_$_SBContinuousExposeWindowDropSwitcherModifier._liftOffVelocity
+ _OBJC_IVAR_$_SBContinuousExposeWindowDropSwitcherModifier._minimizingItem
+ _OBJC_IVAR_$_SBDashBoardSetupView._isCursiveTitleAnimationDesired
+ _OBJC_IVAR_$_SBDeviceApplicationSceneHandle._disableMultitaskingAssertion
+ _OBJC_IVAR_$_SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager._assertion
+ _OBJC_IVAR_$_SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager._shouldReenableChamoisWhenAssertionInvalidates
+ _OBJC_IVAR_$_SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager._shouldReenableMultitaskingWhenAssertionInvalidates
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._averageVelocity
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._initialLayoutAttributes
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._selectedAppLayoutWasInitiallyFullScreen
+ _OBJC_IVAR_$_SBFluidSwitcherAnimationSettings._genieCornerRadiusToAppResetDelay
+ _OBJC_IVAR_$_SBFluidSwitcherAnimationSettings._genieCornerRadiusToHomeResetDelay
+ _OBJC_IVAR_$_SBFluidSwitcherAnimationSettings._homeGestureZoomDownScaleMultiplier
+ _OBJC_IVAR_$_SBFluidSwitcherAnimationSettings._homeGestureZoomDownScaleMultiplierWidgets
+ _OBJC_IVAR_$_SBFluidSwitcherGestureManager._windowTopRegionScrollToTopTapGestureRecognizer
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._contentContainerView
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._drawsFooter
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._footerStyle
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._iconAlignment
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._iconAndLabelFooter
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._iconHitTestOutset
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._iconOpacity
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._overlayPortalView
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._titleAndIconOpacity
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._titleItems
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._titleOpacity
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._uniqueIconsOnly
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._wantsOverlayPortal
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainer._wantsPointerInteractions
+ _OBJC_IVAR_$_SBFluidSwitcherSpaceTitleItemController._isFooterViewOfItemContainer
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._isPendingViewsForAcceleratedHomeGesture
+ _OBJC_IVAR_$_SBFullScreenToHomeIconZoomSwitcherModifier._canAddVelocityKickToHurdleDock
+ _OBJC_IVAR_$_SBFullScreenToHomeIconZoomSwitcherModifier._hasResetCornerRadius
+ _OBJC_IVAR_$_SBHomeGestureSwitcherModifier._isPendingViewsForAcceleratedHomeGesture
+ _OBJC_IVAR_$_SBHomeGestureToZoomDownSwitcherModifier._showingOrAnimatingCardsForFlyIn
+ _OBJC_IVAR_$_SBMenuBarManager._externalDisplayConnectionObserver
+ _OBJC_IVAR_$_SBMenuBarManager._externalDisplayDefaults
+ _OBJC_IVAR_$_SBMenuBarManager._heldModifierKeyRevealTimer
+ _OBJC_IVAR_$_SBMenuBarManager._isOnEmbeddedDisplayWithExternalConnected
+ _OBJC_IVAR_$_SBMenuBarSettings._menuRevealExtraYThresholdForPointerWhenUnderExternalDisplay
+ _OBJC_IVAR_$_SBPosterBoardUpdateManager._schedulerQueue
+ _OBJC_IVAR_$_SBSAIndicatorMitosisTransitionProvider._pendingPhaseTransitionTimerIdentity
+ _OBJC_IVAR_$_SBSceneManager._appearanceChangeObserver
+ _OBJC_IVAR_$_SBSceneManagerCoordinator._sceneHandleDisableMultitaskingAssertionManager
+ _OBJC_IVAR_$_SBSceneSnapshotRequestContext._lastAppearanceChangeTimestamp
+ _OBJC_IVAR_$_SBStripLayoutWindowingModifier._appLayoutsPerformingInitialLayout
+ _OBJC_IVAR_$_SBStripLayoutWindowingModifier._highlightedByHoverAppLayouts
+ _OBJC_IVAR_$_SBStripLayoutWindowingModifier._highlightedByTouchAppLayouts
+ _OBJC_IVAR_$_SBStripLayoutWindowingModifier._isTrackingInteractiveStripGesture
+ _OBJC_IVAR_$_SBStripLayoutWindowingModifier._stripOriginX
+ _OBJC_IVAR_$_SBStripModelWindowingModifier._upcomingAppLayoutForExitingAppExpose
+ _OBJC_IVAR_$_SBSwitcherGenieAttributes._minimizedScale
+ _OBJC_IVAR_$_SBSwitcherGenieAttributes._minimumOutsetSize
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._boundsProperty
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._c2_lock
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._c2_presentationUpdatePaused
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._childContentView
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._contentView
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._displayScale
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._modelUpdatesPaused
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._portaledContentShouldMatchSource
+ _OBJC_IVAR_$_SBSwitcherLayoutTransitionNotes._isRotation
+ _OBJC_IVAR_$_SBWindowingSwitcherPersonality._shouldDeferVisibleOverlayAndUnderlayViewsUpdate
+ _OBJC_METACLASS_$_SBBiomeAppearanceChangeObserver
+ _OBJC_METACLASS_$_SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager
+ _OBJC_METACLASS_$_SBStripLayoutWindowingModifier
+ _OBJC_METACLASS_$__SBSwitcherGenieEffectContentView
+ _SBFactoryBarcodeScannerBundleIdentifier
+ _SBHIconListLayoutIconAccessoryOffset
+ _SBHIconListLayoutIconAccessorySize
+ _SBReverseScaleTransformForScreen
+ _SBStartupDidCompleteNotification
+ _SBStringFromDisplayOrdinal
+ __OBJC_$_INSTANCE_METHODS_SBBiomeAppearanceChangeObserver
+ __OBJC_$_INSTANCE_METHODS_SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager
+ __OBJC_$_INSTANCE_METHODS_SBStripLayoutWindowingModifier
+ __OBJC_$_INSTANCE_METHODS__SBSwitcherGenieEffectContentView
+ __OBJC_$_INSTANCE_VARIABLES_SBBiomeAppearanceChangeObserver
+ __OBJC_$_INSTANCE_VARIABLES_SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager
+ __OBJC_$_INSTANCE_VARIABLES_SBStripLayoutWindowingModifier
+ __OBJC_$_PROP_LIST_SBBiomeAppearanceChangeObserver
+ __OBJC_CLASS_RO_$_SBBiomeAppearanceChangeObserver
+ __OBJC_CLASS_RO_$_SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager
+ __OBJC_CLASS_RO_$_SBStripLayoutWindowingModifier
+ __OBJC_CLASS_RO_$__SBSwitcherGenieEffectContentView
+ __OBJC_METACLASS_RO_$_SBBiomeAppearanceChangeObserver
+ __OBJC_METACLASS_RO_$_SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager
+ __OBJC_METACLASS_RO_$_SBStripLayoutWindowingModifier
+ __OBJC_METACLASS_RO_$__SBSwitcherGenieEffectContentView
+ __UIWindowRoleHintHitTesting
+ __UIWindowRoleHintPrinting
+ __UIWindowRoleHintSnapshotting
+ __UIWindowRoleHintSoftwareDimming
+ __UIWindowRoleHintSubterraneanTextureHosting
+ ___100-[SBRoutingSwitcherModifier contentPageViewScaleForLayoutRole:inAppLayout:withContentPageViewScale:]_block_invoke
+ ___101-[SBFluidSwitcherViewController _modifierViolatingTest:forFrameForLayoutRole:inAppLayout:withBounds:]_block_invoke
+ ___101-[SBFluidSwitcherViewController _modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:]_block_invoke
+ ___107-[SBAbstractWindowSceneDelegate windowScene:didUpdateCoordinateSpace:interfaceOrientation:traitCollection:]_block_invoke
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.314
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.315
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.316
+ ___117-[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:context:]_block_invoke
+ ___117-[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:context:]_block_invoke.cold.1
+ ___117-[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:context:]_block_invoke.cold.2
+ ___117-[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:context:]_block_invoke.cold.3
+ ___117-[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:context:]_block_invoke.cold.4
+ ___117-[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:context:]_block_invoke.cold.5
+ ___117-[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:context:]_block_invoke.cold.6
+ ___117-[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:context:]_block_invoke.cold.7
+ ___119-[SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager acquireDisableMultitaskingAssertionForSceneHandle:]_block_invoke
+ ___119-[SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager acquireDisableMultitaskingAssertionForSceneHandle:]_block_invoke_2
+ ___119-[SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager acquireDisableMultitaskingAssertionForSceneHandle:]_block_invoke_3
+ ___184-[SBSceneRelevancyManager configureWithZOrderedDeviceApplicationSceneEntities:deviceApplicationSceneEntitiesToOcclusionStates:firstMaximizedDeviceApplicationSceneEntity:isStageInPeek:]_block_invoke
+ ___40-[SBMenuBarManager initWithWindowScene:]_block_invoke.28
+ ___40-[SBWindowingStrip containsDisplayItem:]_block_invoke
+ ___40-[SBWindowingStrip containsDisplayItem:]_block_invoke_2
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1213
+ ___46-[SBAppExposeToAppWindowingModifier willBegin]_block_invoke_3
+ ___47-[SBPosterBoardUpdateManager _registerForWork:]_block_invoke_2
+ ___49-[SBAppExposeToAppWindowingModifier visibleItems]_block_invoke
+ ___49-[SBAppExposeToAppWindowingModifier visibleItems]_block_invoke_2
+ ___49-[SBPosterBoardUpdateManager _unregisterForWork:]_block_invoke
+ ___50-[SBBiomeAppearanceChangeObserver _startObserving]_block_invoke
+ ___50-[SBBiomeAppearanceChangeObserver _startObserving]_block_invoke.5
+ ___50-[SBBiomeAppearanceChangeObserver _startObserving]_block_invoke_2
+ ___50-[SBBiomeAppearanceChangeObserver _startObserving]_block_invoke_2.6
+ ___50-[SBBiomeAppearanceChangeObserver _startObserving]_block_invoke_2.cold.1
+ ___51-[SBActionHandler _reportAndKillInsecureProcesses:]_block_invoke.114
+ ___51-[SBActionHandler _reportAndKillInsecureProcesses:]_block_invoke.83
+ ___51-[SBActionHandler _reportAndKillInsecureProcesses:]_block_invoke.88
+ ___51-[SBActionHandler _reportAndKillInsecureProcesses:]_block_invoke.94
+ ___51-[SBActionHandler _reportAndKillInsecureProcesses:]_block_invoke_2.93
+ ___51-[SBActionHandler handleActions:origin:withResult:]_block_invoke.37
+ ___51-[SBActionHandler handleActions:origin:withResult:]_block_invoke.55
+ ___51-[SBActionHandler handleActions:origin:withResult:]_block_invoke_2.38
+ ___51-[SBActionHandler handleActions:origin:withResult:]_block_invoke_8
+ ___51-[SBActionHandler handleActions:origin:withResult:]_block_invoke_9
+ ___52-[SBAppExposeToAppWindowingModifier cornersForItem:]_block_invoke
+ ___52-[SBAppExposeToAppWindowingModifier stripDidChange:]_block_invoke
+ ___52-[SBSceneManager assertBackgroundedStatusForScenes:]_block_invoke.73
+ ___52-[SBStripLayoutWindowingModifier _visibleStripItems]_block_invoke
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.754
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.785
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.816
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.922
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.809
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.926
+ ___55-[SBAppExposeToAppWindowingModifier titleStyleForItem:]_block_invoke
+ ___55-[SBFluidSwitcherItemContainer _updateFooterVisibility]_block_invoke
+ ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.772
+ ___55-[SBRoutingSwitcherModifier _forwardingTargetForUpdate]_block_invoke
+ ___56-[SBAssistantController _updateControlWidgetEligibility]_block_invoke.270
+ ___56-[SBGlassBannerTransitionAnimator prepareForTransition:]_block_invoke
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1758
+ ___57-[SBActivityBannerObserver _handleActivityAlert:present:]_block_invoke
+ ___58-[SBStripLayoutWindowingModifier layoutViewModelsIfNeeded]_block_invoke
+ ___59-[SBIconController _updateUninstallingSystemAppsRestricted]_block_invoke_2
+ ___59-[SBIconController _updateUninstallingSystemAppsRestricted]_block_invoke_2.cold.1
+ ___59-[SBMenuBarManager scheduleMenuBarRevealForHeldModifierKey]_block_invoke
+ ___59-[SBSwitcherGenieEffectView setAttributes:mode:completion:]_block_invoke_2
+ ___61-[SBAppExposeToAppWindowingModifier perspectiveAngleForItem:]_block_invoke
+ ___62-[SBGlassBannerTransitionAnimator _viewHasGaussianBlurFilter:]_block_invoke
+ ___64-[SBActivityManager _activityStartedOrUpdatedWithContentUpdate:]_block_invoke.43
+ ___65-[SBFullScreenToHomeIconZoomSwitcherModifier transitionWillBegin]_block_invoke_5
+ ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke.210
+ ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke_2.213
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.668
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.670
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.671
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.672
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.673
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_2.679
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_3.691
+ ___67-[SBSAIndicatorMitosisTransitionProvider _advancePhaseWithContext:]_block_invoke
+ ___68-[SBRoutingSwitcherModifier isPendingViewsForAcceleratedHomeGesture]_block_invoke
+ ___69-[SBRoutingSwitcherModifier useItemContainerFooterViewsForAppLayout:]_block_invoke
+ ___70-[SBContinuousExposeWindowDropSwitcherModifier handleTransitionEvent:]_block_invoke
+ ___70-[SBContinuousExposeWindowDropSwitcherModifier handleTransitionEvent:]_block_invoke_2
+ ___70-[SBSceneManager transferOwnershipOfSceneWithIdentity:toSceneManager:]_block_invoke.68
+ ___71-[SBGlassBannerTransitionAnimator _removeGaussianBlurFromViewIfNeeded:]_block_invoke
+ ___73-[SBFluidSwitcherViewController _applyStyleToAppLayout:roles:completion:]_block_invoke_5
+ ___73-[SBFluidSwitcherViewController _modifierViolatingTest:forFrameForIndex:]_block_invoke
+ ___73-[SBSwitcherGenieEffectView _performGenieWithAttributes:mode:completion:]_block_invoke_10
+ ___73-[SBSwitcherGenieEffectView _performGenieWithAttributes:mode:completion:]_block_invoke_7
+ ___73-[SBSwitcherGenieEffectView _performGenieWithAttributes:mode:completion:]_block_invoke_8
+ ___73-[SBSwitcherGenieEffectView _performGenieWithAttributes:mode:completion:]_block_invoke_9
+ ___74-[SBFlexibleWindowingExposeToHomePeekWindowingModifier titleStyleForItem:]_block_invoke
+ ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1092
+ ___74-[SBFluidSwitcherViewController itemContainerDidUpdateWantsOverlayPortal:]_block_invoke
+ ___74-[SBSwitcherGenieEffectView _layoutContentAndContainerViewWithAttributes:]_block_invoke
+ ___75-[SBFullScreenContinuousExposeSwitcherModifier _responseForDismissingStrip]_block_invoke
+ ___75-[SBMainSwitcherControllerCoordinator resetLayoutAttributesWithCompletion:]_block_invoke
+ ___75-[SBMainSwitcherControllerCoordinator resetLayoutAttributesWithCompletion:]_block_invoke.124
+ ___75-[SBMainSwitcherControllerCoordinator resetLayoutAttributesWithCompletion:]_block_invoke_2
+ ___75-[SBMainSwitcherControllerCoordinator resetLayoutAttributesWithCompletion:]_block_invoke_3
+ ___75-[SBMainSwitcherControllerCoordinator resetLayoutAttributesWithCompletion:]_block_invoke_4
+ ___75-[SBMainSwitcherControllerCoordinator resetLayoutAttributesWithCompletion:]_block_invoke_5
+ ___78-[SBDashBoardSetupView prepareSolariumCursiveTextViewWithDelegate:completion:]_block_invoke.19
+ ___78-[SBDashBoardSetupView prepareSolariumCursiveTextViewWithDelegate:completion:]_block_invoke_2.21
+ ___78-[SBDashBoardSetupView prepareSolariumCursiveTextViewWithDelegate:completion:]_block_invoke_2.21.cold.1
+ ___78-[SBFluidSwitcherViewController _modifierViolatingValidFloatForScaleForIndex:]_block_invoke
+ ___79-[SBFluidSwitcherViewController _modifierViolatingTest:forAnchorPointForIndex:]_block_invoke
+ ___79-[SBPosterBoardUpdateManager executeUpdate:forBackgroundTask:updateIdentifier:]_block_invoke
+ ___79-[SBPosterBoardUpdateManager executeUpdate:forBackgroundTask:updateIdentifier:]_block_invoke.8
+ ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_11
+ ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_12
+ ___82-[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewFrame:forAppLayout:]_block_invoke
+ ___82-[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewScale:forAppLayout:]_block_invoke
+ ___83-[SBFluidSwitcherViewController _updateAccessoryTitlePresenceForAdjustedAppLayout:]_block_invoke
+ ___83-[SBFluidSwitcherViewController _updateAccessoryTitlePresenceForAdjustedAppLayout:]_block_invoke_2
+ ___83-[SBFluidSwitcherViewController _updateItemContainerTitlePresenceForLeafAppLayout:]_block_invoke
+ ___83-[SBSystemServiceServer _handleRequestAppSwitcherResetLayoutAttributes:fromClient:]_block_invoke
+ ___83-[SBSystemServiceServer _handleRequestAppSwitcherResetLayoutAttributes:fromClient:]_block_invoke_2
+ ___84-[SBFluidSwitcherViewController _modifierViolatingTest:forPerspectiveAngleForIndex:]_block_invoke
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.372
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.373
+ ___88-[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:]_block_invoke
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1610
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1612
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1614
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1618
+ ___92-[SBAppSwitcherSystemService systemServiceServer:resetLayoutAttributesForClient:completion:]_block_invoke
+ ___93-[SBAppExposeToAppWindowingModifier adjustedSpaceAccessoryViewPerspectiveAngle:forAppLayout:]_block_invoke
+ ___95-[SBFluidSwitcherViewController _modifierViolatingValidFloatForScaleForLayoutRole:inAppLayout:]_block_invoke
+ ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke
+ ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke.392
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1741
+ ___blockIMPFromContextSignature101_block_invoke
+ ___blockIMPFromEventSignature101_block_invoke
+ ___blockIMPFromQuerySignature101_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96s_e44_v16?0"BSTransaction<SBStartupTransition>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_104_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_137_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_160_e8_32s40s48s56s64s72s80s88bs_e33_v16?0?<?<v?BB>?"NSString">8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_200_e8_32s40s_e33_v16?0?<?<v?BB>?"NSString">8ls32l8s40l8
+ ___block_descriptor_273_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_32_e107_"SBDisplayItemLayoutAttributes"24?0"SBDisplayItemLayoutAttributesKey"8"SBDisplayItemLayoutAttributes"16l
+ ___block_descriptor_32_e18_B16?0"CAFilter"8l
+ ___block_descriptor_32_e47_v32?0"SBDeviceApplicationSceneEntity"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e37_v32?0"SBSwitcherController"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32bs_e40_B32?0"BSAction"8"NSString"16?<v?>24ls32l8
+ ___block_descriptor_40_e8_32bs_e5_B8?0ls32l8
+ ___block_descriptor_40_e8_32s_e19_B24?0{CGPoint=dd}8ls32l8
+ ___block_descriptor_40_e8_32s_e38_B16?0"<SBSAElapsedTimerDescribing>"8ls32l8
+ ___block_descriptor_40_e8_32s_e39_B40?0{CGRect={CGPoint=dd}{CGSize=dd}}8ls32l8
+ ___block_descriptor_40_e8_32s_e66_B24?0"SBAppLayout"8"SBFluidSwitcherSpaceOverlayAccessoryView"16ls32l8
+ ___block_descriptor_41_e8_32r_e34_v24?0"SBSwitcherController"8^B16lr32l8
+ ___block_descriptor_41_e8_32w_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16lw32l8
+ ___block_descriptor_48_e38_d40?0"SBChainableModifier"8q1624d32l
+ ___block_descriptor_48_e8_32r_e36_v32?0"SBChainableModifier"8Q16^B24lr32l8
+ ___block_descriptor_48_e8_32s40bs_e40_B32?0"BSAction"8"NSString"16?<B?>24ls32l8s40l8
+ ___block_descriptor_48_e8_32w40w_e8_v12?0B8lw32l8w40l8
+ ___block_descriptor_49_e8_32s_e21_16?0"SBAppLayout"8ls32l8
+ ___block_descriptor_56_e8_32bs40r_e36_v32?0"SBChainableModifier"8Q16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32s40r_e36_v32?0"SBChainableModifier"8Q16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48w_e11_v16?0B8B12ls32l8w48l8s40l8
+ ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8s32l8w48l8
+ ___block_descriptor_64_e8_32s40bs48r_e36_v32?0"SBChainableModifier"8Q16^B24ls40l8s32l8r48l8
+ ___block_descriptor_64_e8_32s40s48s_e22_v16?0"BGSystemTask"8ls32l8s40l8s48l8
+ ___block_descriptor_64_ea8_32r40r48r56r_e5_v8?0lr32l8r40l8r48l8r56l8
+ ___block_descriptor_66_e8_32s40bs48bs56w_e42_B16?0"SBMainWorkspaceTransitionRequest"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_66_e8_32s40s48s56w_e8_v12?0B8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r_e17_v16?0"NSError"8ls32l8s40l8s48l8r56l8
+ ___block_descriptor_96_e8_32s40bs48r_e36_v32?0"SBChainableModifier"8Q16^B24ls40l8s32l8r48l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e75_v24?0"BSTransactionBlockObserver"8"BSTransaction<SBStartupTransition>"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.1059
+ ___block_literal_global.1068
+ ___block_literal_global.1104
+ ___block_literal_global.1105
+ ___block_literal_global.1159
+ ___block_literal_global.1164
+ ___block_literal_global.1170
+ ___block_literal_global.1463
+ ___block_literal_global.1584
+ ___block_literal_global.1588
+ ___block_literal_global.1620
+ ___block_literal_global.1629
+ ___block_literal_global.1631
+ ___block_literal_global.1633
+ ___block_literal_global.1635
+ ___block_literal_global.1651
+ ___block_literal_global.173
+ ___block_literal_global.1767
+ ___block_literal_global.1790
+ ___block_literal_global.1799
+ ___block_literal_global.1815
+ ___block_literal_global.197
+ ___block_literal_global.207
+ ___block_literal_global.233
+ ___block_literal_global.242
+ ___block_literal_global.255
+ ___block_literal_global.287
+ ___block_literal_global.291
+ ___block_literal_global.347
+ ___block_literal_global.360
+ ___block_literal_global.363
+ ___block_literal_global.365
+ ___block_literal_global.368
+ ___block_literal_global.494
+ ___block_literal_global.506
+ ___block_literal_global.637
+ ___block_literal_global.665
+ ___block_literal_global.675
+ ___block_literal_global.681
+ ___block_literal_global.719
+ ___block_literal_global.745
+ ___block_literal_global.759
+ ___block_literal_global.928
+ __sceneManagerForDisplayIdentity:creatingIfNecessary:.___once.83
+ _blockIMPFromContextSignature101
+ _blockIMPFromEventSignature101
+ _blockIMPFromQuerySignature101
+ _kWindowDragVelocityAveragingDuration
+ _objc_msgSend$_addGaussianBlurToViewIfNeeded:
+ _objc_msgSend$_canStartGlassCursiveTitleAnimation
+ _objc_msgSend$_didSelectHeaderForLayoutRole:inAppLayout:
+ _objc_msgSend$_forLoggingOnly_enumerateQueryResponderChainStartingAtModifier:usingBlock:
+ _objc_msgSend$_forwardingTargetForUpdate
+ _objc_msgSend$_handleCoverSheetTranslationForPasscodeLockVisible:blockingForOtherReasons:ignoringPreflightRequirementsForPresentation:
+ _objc_msgSend$_handleRequestAppSwitcherResetLayoutAttributes:fromClient:
+ _objc_msgSend$_inverseScaleTransformFactor
+ _objc_msgSend$_isFrameValid:
+ _objc_msgSend$_isIconFlyInAnimationAllowed
+ _objc_msgSend$_isPointValid:
+ _objc_msgSend$_layoutContentAndContainerViewWithAttributes:
+ _objc_msgSend$_modifierViolatingTest:forAnchorPointForIndex:
+ _objc_msgSend$_modifierViolatingTest:forFrameForIndex:
+ _objc_msgSend$_modifierViolatingTest:forFrameForLayoutRole:inAppLayout:withBounds:
+ _objc_msgSend$_modifierViolatingTest:forPerspectiveAngleForIndex:
+ _objc_msgSend$_modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:
+ _objc_msgSend$_modifierViolatingValidFloatForScaleForIndex:
+ _objc_msgSend$_modifierViolatingValidFloatForScaleForLayoutRole:inAppLayout:
+ _objc_msgSend$_primaryTextFontSize
+ _objc_msgSend$_removeGaussianBlurFromViewIfNeeded:
+ _objc_msgSend$_responseForDismissingStrip
+ _objc_msgSend$_schedulerQueue_submitTaskRequestForUpdate:updateIdentifier:
+ _objc_msgSend$_setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:
+ _objc_msgSend$_setWantsOverlayPortalView:
+ _objc_msgSend$_shouldBeginWindowTopRegionTapGesture:
+ _objc_msgSend$_shouldTopRegionScrollToTopGesture:receiveTouch:
+ _objc_msgSend$_startObserving
+ _objc_msgSend$_stopObservingSceneHandles
+ _objc_msgSend$_updateAccessoryTitlePresenceForAdjustedAppLayout:
+ _objc_msgSend$_updateDisableMultitaskingWhileForegroundAssertionIfNeeded
+ _objc_msgSend$_updateGenieMeshTransformForPresentationLayer:properties:boundsProperty:attributes:
+ _objc_msgSend$_updateItemContainerTitlePresenceForLeafAppLayout:
+ _objc_msgSend$_updateMedusaMultitaskingEnabled
+ _objc_msgSend$_updateStripModifierIfNeeded
+ _objc_msgSend$_updateTitlePresenceOnItemContainersForAdjustedAppLayout:
+ _objc_msgSend$_updatedPreferencesAddingMilestonesIfNeededWithPreferences:context:
+ _objc_msgSend$acquireDisableMultitaskingAssertionForSceneHandle:
+ _objc_msgSend$addPortaledContentView:
+ _objc_msgSend$allowsCommandeering
+ _objc_msgSend$allowsTestingStoreDemoMode
+ _objc_msgSend$applicationSceneViewController:didUpdateStatusBarHidden:
+ _objc_msgSend$cancelMenuBarRevealForHeldModifierKey
+ _objc_msgSend$clearLastWindowLayoutAttributes
+ _objc_msgSend$contentPageViewScaleForLayoutRole:inAppLayout:withContentPageViewScale:
+ _objc_msgSend$coverSheetSlidingViewControllerIsInterstitialAllowed:
+ _objc_msgSend$currentAccessoryType
+ _objc_msgSend$currentGenieFrameForVisibleAppLayout:
+ _objc_msgSend$customEdgeSpacing
+ _objc_msgSend$disableIconFlyInAnimation
+ _objc_msgSend$disablesMultitaskingWhileForeground
+ _objc_msgSend$displayItemPrefersStatusBarHidden:
+ _objc_msgSend$dodgeSensorAreaOnIntrinsicContentSize
+ _objc_msgSend$executeUpdate:forBackgroundTask:updateIdentifier:
+ _objc_msgSend$genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:minimizedScale:containerSize:minimumOutsetSize:genieScale:multiplier:active:layoutSettings:
+ _objc_msgSend$genieCornerRadiusToAppResetDelay
+ _objc_msgSend$genieCornerRadiusToHomeResetDelay
+ _objc_msgSend$genieEffectViewDidBegin:
+ _objc_msgSend$gestureHandlingModifierReleasePendingViews:
+ _objc_msgSend$hasCompletedStartup
+ _objc_msgSend$homeGestureZoomDownScaleMultiplier
+ _objc_msgSend$homeGestureZoomDownScaleMultiplierWidgets
+ _objc_msgSend$homeScreenIconBadgeOffsetForAppLayout:
+ _objc_msgSend$homeScreenIconBadgeSizeForAppLayout:
+ _objc_msgSend$horizontalSpacingBetweenLeadingAndCenter
+ _objc_msgSend$horizontalSpacingBetweenTrailingAndCenter
+ _objc_msgSend$initWithAppLayout:applicationSceneHandleProvider:displayIdentity:showCanvasTitles:isChamoisOrFlexibleWindowingEnabled:isFooterViewOfItemContainer:
+ _objc_msgSend$initWithAppLayoutsInStrip:
+ _objc_msgSend$initWithSwitcherCoordinator:commandTabController:
+ _objc_msgSend$initWithText:style:font:textColor:
+ _objc_msgSend$initWithTransitionID:appLayout:nonGestureInitiatedZoomModifier:effectiveStartingEnvironmentMode:liftOffVelocity:adjustAnimationAttributes:showingOrAnimatingCardsForFlyIn:
+ _objc_msgSend$initWithTransitionID:selectedDisplayItem:toAppLayout:initialAppLayout:liftOffVelocity:
+ _objc_msgSend$isFooterViewOfItemContainer
+ _objc_msgSend$isLeadingStatusBarRegionPreferredHiddenByApp
+ _objc_msgSend$isPendingViewsForAcceleratedHomeGesture
+ _objc_msgSend$isPresentingDismissableOffScreenInterstitial
+ _objc_msgSend$isPressDemoModeEnabled:
+ _objc_msgSend$isRotation
+ _objc_msgSend$isStatusBarPartPreferredHiddenByApp:
+ _objc_msgSend$isStoreDemoModeEnabled:
+ _objc_msgSend$isTrailingStatusBarRegionPreferredHiddenByApp
+ _objc_msgSend$itemContainer:didSelectTitleForRole:
+ _objc_msgSend$itemContainerDidUpdateWantsOverlayPortal:
+ _objc_msgSend$lastAppearanceChangeTimestamp
+ _objc_msgSend$lastWindowLayoutAttributesForDisplayOrdinal:
+ _objc_msgSend$listLayout
+ _objc_msgSend$liveContentOverlay:didUpdateStatusBarHiddenSceneSettings:
+ _objc_msgSend$medusaDecoratedApplicationSceneViewController:didUpdateStatusBarHidden:
+ _objc_msgSend$menuRevealExtraYThresholdForPointerWhenUnderExternalDisplay
+ _objc_msgSend$meshContainerOutset
+ _objc_msgSend$minimizedScale
+ _objc_msgSend$minimumOutsetSize
+ _objc_msgSend$noteApplicationTransition
+ _objc_msgSend$overlayPortalView
+ _objc_msgSend$performDeferredUpdateVisibleOverlayAndUnderlayViews
+ _objc_msgSend$prioritizesSortOrderForAppLayout:
+ _objc_msgSend$removeApplicationPlaceholder:pruneEmptyIcons:
+ _objc_msgSend$replaceObjectsInRange:withObjectsFromArray:
+ _objc_msgSend$resetLayoutAttributesWithCompletion:
+ _objc_msgSend$sbh_dockGlassUserInterfaceStyleFromTraitCollection:
+ _objc_msgSend$sceneHandleDisableMultitaskingAssertionManager
+ _objc_msgSend$scheduleMenuBarRevealForHeldModifierKey
+ _objc_msgSend$setApplicationRelationship:
+ _objc_msgSend$setCanAddVelocityKickToHurdleDock:
+ _objc_msgSend$setChildContentView:
+ _objc_msgSend$setCustomPillShapePath:animated:
+ _objc_msgSend$setExcludingShadow:
+ _objc_msgSend$setHeldModifierKeyRevealTimer:
+ _objc_msgSend$setLastAppearanceChangeTimestamp:
+ _objc_msgSend$setLastWindowLayoutAttributes:forDisplayOrdinal:
+ _objc_msgSend$setMedusaMultitaskingEnabled:
+ _objc_msgSend$setMinimizedScale:
+ _objc_msgSend$setMinimumOutsetSize:
+ _objc_msgSend$setOverlayPortalView:
+ _objc_msgSend$setPasscodeLockVisible:intent:ignoringPreflightRequirementsForPresentation:animated:completion:
+ _objc_msgSend$setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:
+ _objc_msgSend$setPortaledContentShouldMatchSource:
+ _objc_msgSend$setPortaledContentViews:
+ _objc_msgSend$setPreallocatesBounds:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$shouldDeferVisibleOverlayAndUnderlayViewsUpdate
+ _objc_msgSend$systemServiceServer:resetLayoutAttributesForClient:completion:
+ _objc_msgSend$tapGestureRecognizer
+ _objc_msgSend$updateEntriesWithBlock:
+ _objc_msgSend$useItemContainerFooterViewsForAppLayout:
+ _objc_msgSend$verticalItemSpacing
+ _objc_msgSend$verticalSpacingBetweenPrimaryAndSecondary
+ _objc_msgSend$wantsOverlayPortal
+ _objc_terminate
- +[SBSwitcherGenieAttributes genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:containerSize:genieScale:multiplier:active:layoutSettings:]
- -[SBActivityBannerObserver _postBannerWithAlert:]
- -[SBActivityBannerObserver presentFallbackAlert:]
- -[SBActivityManager alertPresentationFailed:]
- -[SBActivitySystemApertureElementObserver presentFallbackAlert:]
- -[SBAppExposeToAppWindowingModifier opacityForItem:]
- -[SBAppSwitcherSystemService initWithRecentAppLayoutsController:commandTabController:]
- -[SBApplication lastWindowLayoutAttributes]
- -[SBApplication setLastWindowLayoutAttributes:]
- -[SBApplicationPlaceholderController _finishSwappingPlaceholderAfterCachingIcon:]
- -[SBApplicationPlaceholderController _finishSwappingPlaceholderAfterCachingIcon:].cold.1
- -[SBApplicationPlaceholderController _finishSwappingPlaceholderAfterCachingIcon:].cold.2
- -[SBAssistantSceneController windowSceneDidDisconnect:]
- -[SBCollapsedStripLayoutWindowingModifier .cxx_destruct]
- -[SBCollapsedStripLayoutWindowingModifier _appLayout:isContainedInStrip:]
- -[SBCollapsedStripLayoutWindowingModifier _applyAnimationAttributes:forAppLayout:]
- -[SBCollapsedStripLayoutWindowingModifier _highlightScaleForAppLayout:pileIndex:]
- -[SBCollapsedStripLayoutWindowingModifier _isGroupForAppLayoutHighlightedFromHover:]
- -[SBCollapsedStripLayoutWindowingModifier _isGroupForAppLayoutHighlightedFromTouch:]
- -[SBCollapsedStripLayoutWindowingModifier _isStripStashed]
- -[SBCollapsedStripLayoutWindowingModifier _positionForPositionIn3DContainerSpace:layerPosition:layerSize:layerAnchorPoint:layerTransform:containerPerspective:]
- -[SBCollapsedStripLayoutWindowingModifier _stripIdentifierForAppLayout:]
- -[SBCollapsedStripLayoutWindowingModifier _stripItems]
- -[SBCollapsedStripLayoutWindowingModifier _stripOriginX]
- -[SBCollapsedStripLayoutWindowingModifier _visibleStripItems]
- -[SBCollapsedStripLayoutWindowingModifier _wallpaperDimmingForAppLayout:row:pileIndex:]
- -[SBCollapsedStripLayoutWindowingModifier _wallpaperGradientAttributesForAppLayout:viewModel:row:pileIndex:]
- -[SBCollapsedStripLayoutWindowingModifier didUpdate]
- -[SBCollapsedStripLayoutWindowingModifier frameForItem:]
- -[SBCollapsedStripLayoutWindowingModifier gestureDidComplete:]
- -[SBCollapsedStripLayoutWindowingModifier gestureWillBegin:]
- -[SBCollapsedStripLayoutWindowingModifier highlightDidChange:]
- -[SBCollapsedStripLayoutWindowingModifier init]
- -[SBCollapsedStripLayoutWindowingModifier layoutViewModelsIfNeeded]
- -[SBCollapsedStripLayoutWindowingModifier stripDidChange:]
- -[SBCollapsedStripLayoutWindowingModifier stripWillChange:]
- -[SBCollapsedStripLayoutWindowingModifier topMostItems]
- -[SBCollapsedStripLayoutWindowingModifier transitionDidUpdate:]
- -[SBCollapsedStripLayoutWindowingModifier visibleItems]
- -[SBContinuousExposeRootSwitcherModifier responseForProposedChildResponse:childModifier:event:]
- -[SBContinuousExposeWindowDropSwitcherModifier initWithTransitionID:selectedDisplayItem:toAppLayout:initialAppLayout:]
- -[SBContinuousExposeWindowDropSwitcherModifier initWithTransitionID:selectedDisplayItem:toAppLayout:initialAppLayout:].cold.1
- -[SBCoverSheetSlidingViewController isPresentingInterstitialWhileOffScreen]
- -[SBDashBoardLockScreenEnvironment _handleCoverSheetTranslationForPasscodeLockVisible:blockingForOtherReasons:]
- -[SBDashBoardLockScreenEnvironment setPasscodeLockVisible:intent:animated:completion:]
- -[SBExpandedStripLayoutWindowingModifier .cxx_destruct]
- -[SBExpandedStripLayoutWindowingModifier _appLayout:isContainedInStrip:]
- -[SBExpandedStripLayoutWindowingModifier _applyAnimationAttributes:forAppLayout:]
- -[SBExpandedStripLayoutWindowingModifier _highlightScaleForAppLayout:pileIndex:]
- -[SBExpandedStripLayoutWindowingModifier _isGroupForAppLayoutHighlightedFromHover:]
- -[SBExpandedStripLayoutWindowingModifier _isGroupForAppLayoutHighlightedFromTouch:]
- -[SBExpandedStripLayoutWindowingModifier _isStripStashed]
- -[SBExpandedStripLayoutWindowingModifier _positionForPositionIn3DContainerSpace:layerPosition:layerSize:layerAnchorPoint:layerTransform:containerPerspective:]
- -[SBExpandedStripLayoutWindowingModifier _stripCardScale]
- -[SBExpandedStripLayoutWindowingModifier _stripIdentifierForAppLayout:]
- -[SBExpandedStripLayoutWindowingModifier _stripItems]
- -[SBExpandedStripLayoutWindowingModifier _stripOrderedItems]
- -[SBExpandedStripLayoutWindowingModifier _stripOriginX]
- -[SBExpandedStripLayoutWindowingModifier _wallpaperDimmingForAppLayout:row:pileIndex:]
- -[SBExpandedStripLayoutWindowingModifier _wallpaperGradientAttributesForAppLayout:viewModel:row:pileIndex:]
- -[SBExpandedStripLayoutWindowingModifier adjustedAppLayoutsForAppLayouts:]
- -[SBExpandedStripLayoutWindowingModifier appLayoutToAttachStripDivider]
- -[SBExpandedStripLayoutWindowingModifier didUpdate]
- -[SBExpandedStripLayoutWindowingModifier frameForItem:]
- -[SBExpandedStripLayoutWindowingModifier frameForLayoutRole:inAppLayout:withBounds:]
- -[SBExpandedStripLayoutWindowingModifier gestureDidComplete:]
- -[SBExpandedStripLayoutWindowingModifier gestureWillBegin:]
- -[SBExpandedStripLayoutWindowingModifier init]
- -[SBExpandedStripLayoutWindowingModifier isScrollEnabled]
- -[SBExpandedStripLayoutWindowingModifier layoutViewModelsIfNeeded]
- -[SBExpandedStripLayoutWindowingModifier plusButtonAlpha]
- -[SBExpandedStripLayoutWindowingModifier plusButtonStyle]
- -[SBExpandedStripLayoutWindowingModifier restingOffsetForScrollOffset:velocity:]
- -[SBExpandedStripLayoutWindowingModifier scrollViewAttributes]
- -[SBExpandedStripLayoutWindowingModifier shouldScrollViewBlockTouches]
- -[SBExpandedStripLayoutWindowingModifier stripDidChange:]
- -[SBExpandedStripLayoutWindowingModifier stripWillChange:]
- -[SBExpandedStripLayoutWindowingModifier topMostItems]
- -[SBExpandedStripLayoutWindowingModifier transitionDidUpdate:]
- -[SBExpandedStripLayoutWindowingModifier visibleItems]
- -[SBFluidSwitcherGestureManager _shouldBeginWindowTopRegionDoubleTapGesture:]
- -[SBFluidSwitcherItemContainer appLayoutForIconOverlay]
- -[SBFluidSwitcherItemContainer configureOverlayForAppLayout:iconZoomWithView:crossfadeViews:]
- -[SBFluidSwitcherItemContainer removeIconOverlay]
- -[SBFluidSwitcherSpaceTitleItemController initWithAppLayout:applicationSceneHandleProvider:displayIdentity:showCanvasTitles:isChamoisOrFlexibleWindowingEnabled:]
- -[SBFluidSwitcherSpaceTitleItemController initWithAppLayout:applicationSceneHandleProvider:displayIdentity:showCanvasTitles:isChamoisOrFlexibleWindowingEnabled:].cold.1
- -[SBFluidSwitcherViewController _updateTitlePresenceForAdjustedAppLayout:]
- -[SBFluidSwitcherViewController itemContainer:didUpdateShowingIconOverlay:]
- -[SBFullScreenToHomeIconZoomSwitcherModifier transactionCompletionOptions]
- -[SBGlassBannerTransitionAnimator _addGaussianBlurToViewIfNeeded:inputRadius:]
- -[SBGlassBannerTransitionAnimator settings]
- -[SBHomeGestureToZoomDownSwitcherModifier initWithTransitionID:appLayout:nonGestureInitiatedZoomModifier:effectiveStartingEnvironmentMode:liftOffVelocity:adjustAnimationAttributes:]
- -[SBHomeGestureToZoomDownSwitcherModifier initWithTransitionID:appLayout:nonGestureInitiatedZoomModifier:effectiveStartingEnvironmentMode:liftOffVelocity:adjustAnimationAttributes:].cold.1
- -[SBLockScreenManager _setPasscodeVisible:animated:]
- -[SBLockScreenViewControllerBase setPasscodeLockVisible:intent:animated:completion:]
- -[SBMainSwitcherControllerCoordinator _shouldPrioritizeSortOrderForAppLayout:]
- -[SBPhoneSceneSnapshotRequestStrategy .cxx_destruct]
- -[SBPhoneSceneSnapshotRequestStrategy _handleRealTimeAppearanceChange:]
- -[SBPhoneSceneSnapshotRequestStrategy _loadLastAppearanceChangeWithCompletion:]
- -[SBPhoneSceneSnapshotRequestStrategy _startObservingAppearanceChanges]
- -[SBPhoneSceneSnapshotRequestStrategy _stopObservingAppearanceChanges]
- -[SBPhoneSceneSnapshotRequestStrategy _subscribeToAppearanceChanges]
- -[SBPhoneSceneSnapshotRequestStrategy _updateLastAppearanceTimestamp:]
- -[SBPhoneSceneSnapshotRequestStrategy appearancePublisher]
- -[SBPhoneSceneSnapshotRequestStrategy appearanceQueue]
- -[SBPhoneSceneSnapshotRequestStrategy dealloc]
- -[SBPhoneSceneSnapshotRequestStrategy init]
- -[SBPhoneSceneSnapshotRequestStrategy isObserving]
- -[SBPhoneSceneSnapshotRequestStrategy lastAppearanceTimestamp]
- -[SBPhoneSceneSnapshotRequestStrategy setAppearancePublisher:]
- -[SBPhoneSceneSnapshotRequestStrategy setAppearanceQueue:]
- -[SBPhoneSceneSnapshotRequestStrategy setIsObserving:]
- -[SBPhoneSceneSnapshotRequestStrategy setLastAppearanceTimestamp:]
- -[SBPhoneSceneSnapshotRequestStrategy snapshotRequestsForSceneHandle:settings:snapshotRequestContext:].cold.1
- -[SBPosterBoardUpdateManager _submitTaskRequestForUpdate:]
- -[SBPosterBoardUpdateManager _submitTaskRequestForUpdate:].cold.1
- -[SBPosterBoardUpdateManager executeUpdate:]
- -[SBRecordingIndicatorViewController _doesHighLevelLayerRequireReverseZoomScale]
- -[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:]
- -[SBStripExpansionAnimationModifier .cxx_destruct]
- -[SBStripExpansionAnimationModifier _fromItemSet]
- -[SBStripExpansionAnimationModifier _performTransactionWithTemporaryChildModifier:strip:usingBlock:]
- -[SBStripExpansionAnimationModifier _toItemSet]
- -[SBStripExpansionAnimationModifier didScroll:]
- -[SBStripExpansionAnimationModifier inUpdatePhase]
- -[SBStripExpansionAnimationModifier initWithFromSteadyStateModifier:toSteadyStateModifier:fromStrip:toStrip:]
- -[SBStripExpansionAnimationModifier initWithFromSteadyStateModifier:toSteadyStateModifier:fromStrip:toStrip:].cold.1
- -[SBStripExpansionAnimationModifier initWithFromSteadyStateModifier:toSteadyStateModifier:fromStrip:toStrip:].cold.2
- -[SBStripExpansionAnimationModifier initWithFromSteadyStateModifier:toSteadyStateModifier:fromStrip:toStrip:].cold.3
- -[SBStripExpansionAnimationModifier initWithFromSteadyStateModifier:toSteadyStateModifier:fromStrip:toStrip:].cold.4
- -[SBStripExpansionAnimationModifier layoutViewModelsIfNeeded]
- -[SBStripExpansionAnimationModifier stripDidChange:]
- -[SBStripExpansionAnimationModifier stripWillChange:]
- -[SBStripExpansionAnimationModifier strip]
- -[SBStripExpansionAnimationModifier timerFired:]
- -[SBStripExpansionAnimationModifier topMostItems]
- -[SBStripExpansionAnimationModifier visibleItems]
- -[SBStripLayoutRootWindowingModifier _updateChildModifiersIfNeeded]
- -[SBStripLayoutRootWindowingModifier didUpdate]
- -[SBStripLayoutRootWindowingModifier stripDidChange:]
- -[SBStripLayoutRootWindowingModifier timerFired:]
- -[SBStripLayoutRootWindowingModifier willUpdate]
- -[SBStripModelWindowingModifier appExposeAccessoryButtonsBundleIdentifier]
- -[SBStripModelWindowingModifier tappedOutsideToDismiss:]
- -[SBStripPresentWhileMinimizingItemThenDismissAnimationModifier .cxx_destruct]
- -[SBStripPresentWhileMinimizingItemThenDismissAnimationModifier _stripOriginX]
- -[SBStripPresentWhileMinimizingItemThenDismissAnimationModifier animationAttributesForItem:]
- -[SBStripPresentWhileMinimizingItemThenDismissAnimationModifier didScroll:]
- -[SBStripPresentWhileMinimizingItemThenDismissAnimationModifier didUpdate]
- -[SBStripPresentWhileMinimizingItemThenDismissAnimationModifier gestureWillBegin:]
- -[SBStripPresentWhileMinimizingItemThenDismissAnimationModifier init]
- -[SBStripPresentWhileMinimizingItemThenDismissAnimationModifier timerFired:]
- -[SBStripPresentWhileMinimizingItemThenDismissAnimationModifier willBegin]
- -[SBSwitcherGenieEffectView _updateGenieMeshTransformForPresentationLayer:properties:attributes:]
- -[SBSwitcherGenieEffectView addContentView:]
- -[SBSwitcherGenieEffectView setContentViews:]
- -[SBWindowingStrip expansionMode]
- -[SBWindowingStrip initWithAppLayoutsInStrip:expansionMode:isInlineAppExpose:]
- -[SBWindowingStrip initWithAppLayoutsInStrip:expansionMode:isInlineAppExpose:].cold.1
- -[SBWindowingStrip isInlineAppExpose]
- GCC_except_table176
- GCC_except_table215
- GCC_except_table231
- GCC_except_table247
- GCC_except_table274
- GCC_except_table297
- GCC_except_table301
- GCC_except_table313
- GCC_except_table321
- GCC_except_table323
- GCC_except_table325
- GCC_except_table347
- GCC_except_table368
- GCC_except_table382
- GCC_except_table391
- GCC_except_table401
- GCC_except_table437
- GCC_except_table442
- GCC_except_table447
- GCC_except_table483
- GCC_except_table485
- GCC_except_table491
- GCC_except_table493
- GCC_except_table515
- GCC_except_table519
- GCC_except_table525
- GCC_except_table529
- GCC_except_table553
- GCC_except_table598
- GCC_except_table633
- GCC_except_table701
- GCC_except_table725
- GCC_except_table728
- GCC_except_table768
- GCC_except_table808
- GCC_except_table848
- GCC_except_table857
- GCC_except_table900
- GCC_except_table939
- _CGPathEqualToPath
- _OBJC_CLASS_$_SBCollapsedStripLayoutWindowingModifier
- _OBJC_CLASS_$_SBExpandedStripLayoutWindowingModifier
- _OBJC_CLASS_$_SBStripExpansionAnimationModifier
- _OBJC_CLASS_$_SBStripLayoutRootWindowingModifier
- _OBJC_CLASS_$_SBStripPresentWhileMinimizingItemThenDismissAnimationModifier
- _OBJC_IVAR_$_SBApplication._cachedLastWindowLayoutAttributesOrNSNull
- _OBJC_IVAR_$_SBApplicationPlaceholderController._removingPlaceholderProxies
- _OBJC_IVAR_$_SBCollapsedStripLayoutWindowingModifier._appLayoutsPerformingInitialLayout
- _OBJC_IVAR_$_SBCollapsedStripLayoutWindowingModifier._highlightedByHoverAppLayouts
- _OBJC_IVAR_$_SBCollapsedStripLayoutWindowingModifier._highlightedByTouchAppLayouts
- _OBJC_IVAR_$_SBCollapsedStripLayoutWindowingModifier._isTrackingInteractiveStripGesture
- _OBJC_IVAR_$_SBCollapsedStripLayoutWindowingModifier._stripOriginX
- _OBJC_IVAR_$_SBCommandTabViewController._backgroundMaterialView
- _OBJC_IVAR_$_SBCommandTabViewController._backgroundShadowView
- _OBJC_IVAR_$_SBExpandedStripLayoutWindowingModifier._bottomAppFinalMaxY
- _OBJC_IVAR_$_SBExpandedStripLayoutWindowingModifier._bottomAppInitialMinY
- _OBJC_IVAR_$_SBExpandedStripLayoutWindowingModifier._contentSize
- _OBJC_IVAR_$_SBExpandedStripLayoutWindowingModifier._highlightedByHoverAppLayouts
- _OBJC_IVAR_$_SBExpandedStripLayoutWindowingModifier._highlightedByTouchAppLayouts
- _OBJC_IVAR_$_SBExpandedStripLayoutWindowingModifier._isTrackingInteractiveStripGesture
- _OBJC_IVAR_$_SBExpandedStripLayoutWindowingModifier._stripCardScale
- _OBJC_IVAR_$_SBExpandedStripLayoutWindowingModifier._stripOrderedItems
- _OBJC_IVAR_$_SBExpandedStripLayoutWindowingModifier._stripOriginX
- _OBJC_IVAR_$_SBExpandedStripLayoutWindowingModifier._topAppFinalMinY
- _OBJC_IVAR_$_SBExpandedStripLayoutWindowingModifier._topAppInitialMaxY
- _OBJC_IVAR_$_SBFluidSwitcherItemContainer._appLayoutForIconOverlay
- _OBJC_IVAR_$_SBPhoneSceneSnapshotRequestStrategy._appearancePublisher
- _OBJC_IVAR_$_SBPhoneSceneSnapshotRequestStrategy._appearanceQueue
- _OBJC_IVAR_$_SBPhoneSceneSnapshotRequestStrategy._isObserving
- _OBJC_IVAR_$_SBPhoneSceneSnapshotRequestStrategy._lastAppearanceTimestamp
- _OBJC_IVAR_$_SBStripExpansionAnimationModifier._fromSteadyStateModifier
- _OBJC_IVAR_$_SBStripExpansionAnimationModifier._fromStrip
- _OBJC_IVAR_$_SBStripExpansionAnimationModifier._stripOverride
- _OBJC_IVAR_$_SBStripExpansionAnimationModifier._toExpansionMode
- _OBJC_IVAR_$_SBStripExpansionAnimationModifier._toSteadyStateModifier
- _OBJC_IVAR_$_SBStripExpansionAnimationModifier._toStrip
- _OBJC_IVAR_$_SBStripModelWindowingModifier._bundleIdShowingAppExpose
- _OBJC_IVAR_$_SBStripModelWindowingModifier._expansionMode
- _OBJC_IVAR_$_SBStripPresentWhileMinimizingItemThenDismissAnimationModifier._stripOriginX
- _OBJC_IVAR_$_SBStripPresentWhileMinimizingItemThenDismissAnimationModifier._uniqueDismissalDelayReason
- _OBJC_IVAR_$_SBWindowingStrip._expansionMode
- _OBJC_IVAR_$_SBWindowingStrip._isInlineAppExpose
- _OBJC_METACLASS_$_SBCollapsedStripLayoutWindowingModifier
- _OBJC_METACLASS_$_SBExpandedStripLayoutWindowingModifier
- _OBJC_METACLASS_$_SBStripExpansionAnimationModifier
- _OBJC_METACLASS_$_SBStripLayoutRootWindowingModifier
- _OBJC_METACLASS_$_SBStripPresentWhileMinimizingItemThenDismissAnimationModifier
- __OBJC_$_INSTANCE_METHODS_SBCollapsedStripLayoutWindowingModifier
- __OBJC_$_INSTANCE_METHODS_SBExpandedStripLayoutWindowingModifier
- __OBJC_$_INSTANCE_METHODS_SBStripExpansionAnimationModifier
- __OBJC_$_INSTANCE_METHODS_SBStripLayoutRootWindowingModifier
- __OBJC_$_INSTANCE_METHODS_SBStripPresentWhileMinimizingItemThenDismissAnimationModifier
- __OBJC_$_INSTANCE_VARIABLES_SBCollapsedStripLayoutWindowingModifier
- __OBJC_$_INSTANCE_VARIABLES_SBExpandedStripLayoutWindowingModifier
- __OBJC_$_INSTANCE_VARIABLES_SBPhoneSceneSnapshotRequestStrategy
- __OBJC_$_INSTANCE_VARIABLES_SBStripExpansionAnimationModifier
- __OBJC_$_INSTANCE_VARIABLES_SBStripPresentWhileMinimizingItemThenDismissAnimationModifier
- __OBJC_CLASS_RO_$_SBCollapsedStripLayoutWindowingModifier
- __OBJC_CLASS_RO_$_SBExpandedStripLayoutWindowingModifier
- __OBJC_CLASS_RO_$_SBStripExpansionAnimationModifier
- __OBJC_CLASS_RO_$_SBStripLayoutRootWindowingModifier
- __OBJC_CLASS_RO_$_SBStripPresentWhileMinimizingItemThenDismissAnimationModifier
- __OBJC_METACLASS_RO_$_SBCollapsedStripLayoutWindowingModifier
- __OBJC_METACLASS_RO_$_SBExpandedStripLayoutWindowingModifier
- __OBJC_METACLASS_RO_$_SBStripExpansionAnimationModifier
- __OBJC_METACLASS_RO_$_SBStripLayoutRootWindowingModifier
- __OBJC_METACLASS_RO_$_SBStripPresentWhileMinimizingItemThenDismissAnimationModifier
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.302
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.303
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.304
- ___109-[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:]_block_invoke
- ___109-[SBSAIndicatorAppearanceStateTransitionProvider _updatedPreferencesAddingMilestonesIfNeededWithPreferences:]_block_invoke.cold.1
- ___42-[SBStripModelWindowingModifier didUpdate]_block_invoke_13
- ___42-[SBStripModelWindowingModifier didUpdate]_block_invoke_14
- ___42-[SBStripModelWindowingModifier didUpdate]_block_invoke_15
- ___42-[SBStripModelWindowingModifier didUpdate]_block_invoke_16
- ___44-[SBPosterBoardUpdateManager executeUpdate:]_block_invoke
- ___44-[SBPosterBoardUpdateManager executeUpdate:]_block_invoke.6
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1210
- ___47-[SBStripExpansionAnimationModifier _toItemSet]_block_invoke
- ___49-[SBActivityBannerObserver _postBannerWithAlert:]_block_invoke
- ___49-[SBStripExpansionAnimationModifier _fromItemSet]_block_invoke
- ___51-[SBActionHandler _reportAndKillInsecureProcesses:]_block_invoke.60
- ___51-[SBActionHandler _reportAndKillInsecureProcesses:]_block_invoke.65
- ___51-[SBActionHandler _reportAndKillInsecureProcesses:]_block_invoke.68
- ___51-[SBActionHandler _reportAndKillInsecureProcesses:]_block_invoke.71
- ___51-[SBActionHandler _reportAndKillInsecureProcesses:]_block_invoke_2.70
- ___51-[SBActionHandler handleActions:origin:withResult:]_block_invoke.17
- ___51-[SBActionHandler handleActions:origin:withResult:]_block_invoke.32
- ___51-[SBActionHandler handleActions:origin:withResult:]_block_invoke_2.19
- ___52-[SBLockScreenManager _setPasscodeVisible:animated:]_block_invoke
- ___52-[SBLockScreenManager _setPasscodeVisible:animated:]_block_invoke.392
- ___52-[SBSceneManager assertBackgroundedStatusForScenes:]_block_invoke.72
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.751
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.782
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.813
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.919
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.806
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.923
- ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.759
- ___56-[SBAssistantController _updateControlWidgetEligibility]_block_invoke.268
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1755
- ___59-[SBIconController _updateUninstallingSystemAppsRestricted]_block_invoke.cold.1
- ___59-[SBMainSwitcherControllerCoordinator _buildAppLayoutCache]_block_invoke_12
- ___61-[SBCollapsedStripLayoutWindowingModifier _visibleStripItems]_block_invoke
- ___61-[SBStripExpansionAnimationModifier layoutViewModelsIfNeeded]_block_invoke
- ___61-[SBStripExpansionAnimationModifier layoutViewModelsIfNeeded]_block_invoke_2
- ___61-[SBStripExpansionAnimationModifier layoutViewModelsIfNeeded]_block_invoke_3
- ___61-[SBStripExpansionAnimationModifier layoutViewModelsIfNeeded]_block_invoke_4
- ___61-[SBStripExpansionAnimationModifier layoutViewModelsIfNeeded]_block_invoke_5
- ___64-[SBActivityManager _activityStartedOrUpdatedWithContentUpdate:]_block_invoke.45
- ___65-[SBFullScreenContinuousExposeSwitcherModifier handleHoverEvent:]_block_invoke
- ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke.209
- ___65-[SBMainDisplaySceneManager _appSceneClientSettingsDiffInspector]_block_invoke_2.212
- ___66-[SBExpandedStripLayoutWindowingModifier layoutViewModelsIfNeeded]_block_invoke
- ___67-[SBCollapsedStripLayoutWindowingModifier layoutViewModelsIfNeeded]_block_invoke
- ___67-[SBFluidSwitcherItemContainer setGenieAttributes:mode:completion:]_block_invoke
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_29
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_30
- ___68-[SBFlexibleWindowingWindowDragSwitcherModifier handleGestureEvent:]_block_invoke_3
- ___68-[SBPhoneSceneSnapshotRequestStrategy _subscribeToAppearanceChanges]_block_invoke
- ___68-[SBPhoneSceneSnapshotRequestStrategy _subscribeToAppearanceChanges]_block_invoke.69
- ___68-[SBPhoneSceneSnapshotRequestStrategy _subscribeToAppearanceChanges]_block_invoke.cold.1
- ___69-[SBApplicationPlaceholderController _removePlaceholders:forInstall:]_block_invoke
- ___70-[SBPhoneSceneSnapshotRequestStrategy _updateLastAppearanceTimestamp:]_block_invoke
- ___70-[SBSceneManager transferOwnershipOfSceneWithIdentity:toSceneManager:]_block_invoke.67
- ___70-[SBSplitDisplayItemSwitcherModifier adjustedAppLayoutsForAppLayouts:]_block_invoke_2
- ___71-[SBMainSwitcherControllerCoordinator appLayoutsForSwitcherController:]_block_invoke_3
- ___71-[SBPhoneSceneSnapshotRequestStrategy _startObservingAppearanceChanges]_block_invoke
- ___74-[SBExpandedStripLayoutWindowingModifier adjustedAppLayoutsForAppLayouts:]_block_invoke
- ___74-[SBExpandedStripLayoutWindowingModifier adjustedAppLayoutsForAppLayouts:]_block_invoke_2
- ___74-[SBExpandedStripLayoutWindowingModifier adjustedAppLayoutsForAppLayouts:]_block_invoke_3
- ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1076
- ___74-[SBFluidSwitcherViewController _updateTitlePresenceForAdjustedAppLayout:]_block_invoke
- ___74-[SBFluidSwitcherViewController _updateTitlePresenceForAdjustedAppLayout:]_block_invoke_2
- ___78-[SBDashBoardSetupView prepareSolariumCursiveTextViewWithDelegate:completion:]_block_invoke.16
- ___78-[SBDashBoardSetupView prepareSolariumCursiveTextViewWithDelegate:completion:]_block_invoke_2.18
- ___78-[SBDashBoardSetupView prepareSolariumCursiveTextViewWithDelegate:completion:]_block_invoke_2.18.cold.1
- ___78-[SBFluidSwitcherGestureManager _shouldBeginSplitViewApplicationUnpinGesture:]_block_invoke
- ___78-[SBFluidSwitcherGestureManager _shouldBeginSplitViewApplicationUnpinGesture:]_block_invoke_2
- ___79-[SBPhoneSceneSnapshotRequestStrategy _loadLastAppearanceChangeWithCompletion:]_block_invoke
- ___79-[SBPhoneSceneSnapshotRequestStrategy _loadLastAppearanceChangeWithCompletion:]_block_invoke.67
- ___79-[SBPhoneSceneSnapshotRequestStrategy _loadLastAppearanceChangeWithCompletion:]_block_invoke.cold.1
- ___85-[SBFluidSwitcherViewController _performModifierIconOverlayVisibilityUpdateResponse:]_block_invoke_2
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.360
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.361
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1607
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1609
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1611
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1615
- ___95-[SBContinuousExposeRootSwitcherModifier responseForProposedChildResponse:childModifier:event:]_block_invoke
- ___95-[SBContinuousExposeRootSwitcherModifier responseForProposedChildResponse:childModifier:event:]_block_invoke_2
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1738
- ___block_descriptor_160_e8_32s_e33_v16?0?<?<v?BB>?"NSString">8ls32l8
- ___block_descriptor_272_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_40_e8_32s_e67_v32?0"<SBWindowingItem>"8"SBMutableWindowingItemViewModel"16^B24ls32l8
- ___block_descriptor_41_e8_32s_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16ls32l8
- ___block_descriptor_48_e8_32r40w_e22_B16?0"BMStoreEvent"8lw40l8r32l8
- ___block_descriptor_48_e8_32s40bs_e40_B32?0"BSAction"8"NSString"16?<v?>24ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e31_v24?0"<SBWindowingItem>"8^B16ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e34_v24?0"SBSwitcherController"8^B16lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e45_v16?0"<SBHIconImageCacheResultDescribing>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e76_"SBChainableModifierEventResponse"16?0"SBChainableModifierEventResponse"8ls32l8s40l8
- ___block_descriptor_48_e8_32s_e22_v16?0"BGSystemTask"8ls32l8
- ___block_descriptor_56_e8_32bs40r48w_e23_v16?0"BPSCompletion"8lw48l8s32l8r40l8
- ___block_descriptor_56_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
- ___block_descriptor_57_e8_32s40r48r_e24_v32?0"NSArray"8Q16^B24ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32r40r48r56r_e5_v8?0lr32l8r40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40bs48r56r_e11_v16?0B8B12ls40l8r48l8r56l8s32l8
- ___block_descriptor_64_e8_32s40s48s56w_e11_v16?0B8B12ls32l8w56l8s40l8s48l8
- ___block_descriptor_74_e8_32s40s48s56bs64bs_e42_B16?0"SBMainWorkspaceTransitionRequest"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_74_e8_32s40s48s56s64w_e8_v12?0B8lw64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e75_v24?0"BSTransactionBlockObserver"8"BSTransaction<SBStartupTransition>"16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e44_v16?0"BSTransaction<SBStartupTransition>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_literal_global.1056
- ___block_literal_global.1065
- ___block_literal_global.1089
- ___block_literal_global.1101
- ___block_literal_global.1153
- ___block_literal_global.1161
- ___block_literal_global.1167
- ___block_literal_global.1460
- ___block_literal_global.1581
- ___block_literal_global.1585
- ___block_literal_global.1617
- ___block_literal_global.1626
- ___block_literal_global.1628
- ___block_literal_global.1630
- ___block_literal_global.1632
- ___block_literal_global.1648
- ___block_literal_global.1764
- ___block_literal_global.1787
- ___block_literal_global.1796
- ___block_literal_global.1812
- ___block_literal_global.194
- ___block_literal_global.201
- ___block_literal_global.243
- ___block_literal_global.275
- ___block_literal_global.279
- ___block_literal_global.335
- ___block_literal_global.342
- ___block_literal_global.348
- ___block_literal_global.351
- ___block_literal_global.353
- ___block_literal_global.356
- ___block_literal_global.490
- ___block_literal_global.500
- ___block_literal_global.595
- ___block_literal_global.634
- ___block_literal_global.662
- ___block_literal_global.664
- ___block_literal_global.669
- ___block_literal_global.693
- ___block_literal_global.706
- ___block_literal_global.732
- ___block_literal_global.925
- __sceneManagerForDisplayIdentity:creatingIfNecessary:.___once.82
- _objc_msgSend$_finishSwappingPlaceholderAfterCachingIcon:
- _objc_msgSend$_fromItemSet
- _objc_msgSend$_handleCoverSheetTranslationForPasscodeLockVisible:blockingForOtherReasons:
- _objc_msgSend$_handleRealTimeAppearanceChange:
- _objc_msgSend$_loadLastAppearanceChangeWithCompletion:
- _objc_msgSend$_performTransactionWithTemporaryChildModifier:strip:usingBlock:
- _objc_msgSend$_postBannerWithAlert:
- _objc_msgSend$_shouldBeginWindowTopRegionDoubleTapGesture:
- _objc_msgSend$_shouldPrioritizeSortOrderForAppLayout:
- _objc_msgSend$_stopObservingAppearanceChanges
- _objc_msgSend$_stripCardScale
- _objc_msgSend$_submitTaskRequestForUpdate:
- _objc_msgSend$_subscribeToAppearanceChanges
- _objc_msgSend$_toItemSet
- _objc_msgSend$_updateGenieMeshTransformForPresentationLayer:properties:attributes:
- _objc_msgSend$_updateLastAppearanceTimestamp:
- _objc_msgSend$_updateTitlePresenceForAdjustedAppLayout:
- _objc_msgSend$_updatedPreferencesAddingMilestonesIfNeededWithPreferences:
- _objc_msgSend$alertPresentationFailed:
- _objc_msgSend$appearancePublisher
- _objc_msgSend$cacheImageForIcon:imageAppearance:options:completionHandler:
- _objc_msgSend$executeUpdate:
- _objc_msgSend$expansionMode
- _objc_msgSend$genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:containerSize:genieScale:multiplier:active:layoutSettings:
- _objc_msgSend$hasBackgroundBlur
- _objc_msgSend$inUpdatePhase
- _objc_msgSend$initWithActiveAppLayout:appExposeBundleIdentifier:
- _objc_msgSend$initWithAppLayout:applicationSceneHandleProvider:displayIdentity:showCanvasTitles:isChamoisOrFlexibleWindowingEnabled:
- _objc_msgSend$initWithAppLayoutsInStrip:expansionMode:isInlineAppExpose:
- _objc_msgSend$initWithRecentAppLayoutsController:commandTabController:
- _objc_msgSend$initWithTransitionID:appExposeBundleID:direction:appExposeModifier:
- _objc_msgSend$initWithTransitionID:appLayout:nonGestureInitiatedZoomModifier:effectiveStartingEnvironmentMode:liftOffVelocity:adjustAnimationAttributes:
- _objc_msgSend$initWithTransitionID:direction:activeAppLayout:appExposeBundleIdentifier:
- _objc_msgSend$initWithTransitionID:selectedDisplayItem:toAppLayout:initialAppLayout:
- _objc_msgSend$isInlineAppExpose
- _objc_msgSend$isPresentingInterstitialWhileOffScreen
- _objc_msgSend$itemContainer:didUpdateShowingIconOverlay:
- _objc_msgSend$lastAppearanceTimestamp
- _objc_msgSend$lastWindowLayoutAttributes
- _objc_msgSend$presentFallbackAlert:
- _objc_msgSend$setContentViews:
- _objc_msgSend$setIsObserving:
- _objc_msgSend$setLastAppearanceTimestamp:
- _objc_msgSend$setLastWindowLayoutAttributes:
- _objc_msgSend$setOverrideLegibilitySettings:
- _objc_msgSend$setPasscodeLockVisible:intent:animated:completion:
CStrings:
+ "%@-SchedulerQueue"
+ "%{public}@ should begin: touch (%@) hit-tested to item container (%@) and was inside edge swipe hit test rect (%@)"
+ "@\"<BPSCancellable>\""
+ "@\"SBBiomeAppearanceChangeObserver\""
+ "@\"SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager\""
+ "@\"SBDisplayItemLayoutAttributes\"24@?0@\"SBDisplayItemLayoutAttributesKey\"8@\"SBDisplayItemLayoutAttributes\"16"
+ "@\"_SBSwitcherGenieEffectContentView\""
+ "@172@0:8{CGPoint=dd}16{CGPoint=dd}32{CGPoint=dd}48{CGSize=dd}64{CGSize=dd}80d96{CGSize=dd}104{CGSize=dd}120d136{CGPoint=dd}144B160@164"
+ "@40@0:8@?16q24@32"
+ "@52@0:8@16@24@32B40B44B48"
+ "@64@0:8@16@24@32@40{CGPoint=dd}48"
+ "@72@0:8@16@24@32q40{CGPoint=dd}48B64B68"
+ "@72@0:8@?16q24@32{CGRect={CGPoint=dd}{CGSize=dd}}40"
+ "B16@?0@\"<SBSAElapsedTimerDescribing>\"8"
+ "B16@?0@\"CAFilter\"8"
+ "B24@?0@\"SBAppLayout\"8@\"SBFluidSwitcherSpaceOverlayAccessoryView\"16"
+ "B28@0:8B16B20B24"
+ "B32@?0@\"BSAction\"8@\"NSString\"16@?<B@?>24"
+ "B40@?0{CGRect={CGPoint=dd}{CGSize=dd}}8"
+ "Corner Reset Delay To App"
+ "Corner Reset Delay To Home"
+ "CoverSheet dismiss gesture began while in presentation state: %@, forcing to fully presented"
+ "CoverSheet present gesture began while in presentation state: %@, forcing to dismissed"
+ "Display appearance stream error: %@"
+ "Got an invalid anchorPointForIndex: %{public}@ from modifier: %{public}@ for appLayout: %{public}@ atIndex: %lu"
+ "Got an invalid frameForIndex: %{public}@ from modifier: %{public}@ for appLayout: %{public}@ atIndex: %lu"
+ "Got an invalid frameForLayoutRole: %{public}@ from modifier: %{public}@ for layoutRole: %lu in appLayout: %{public}@ atIndex: %lu item: %{public}@"
+ "Got an invalid perspectiveAngleForIndex: %{public}@ from modifier: %{public}@ for appLayout: %{public}@ atIndex: %lu"
+ "Got an invalid perspectiveAngleForLayoutRole: %{public}@ from modifier: %{public}@ for layoutRole: %lu in appLayout: %{public}@ atIndex: %lu item: %{public}@"
+ "Got an invalid scaleForIndex: %f from modifier: %{public}@ for appLayout: %{public}@ atIndex: %lu"
+ "Got an invalid scaleForLayoutRole: %f from modifier: %{public}@ for layoutRole: %lu in appLayout: %{public}@ item: %{public}@"
+ "Menu Reveal Extra Y Threshold When External Display Above"
+ "New transition requested"
+ "Notifying Siri of application transition"
+ "ResetLayoutAttributes"
+ "SBApplicationLastWindowSizePerDisplayOrdinalKey"
+ "SBBeginAnimatedStripDismissalReason"
+ "SBBiomeAppearanceChangeObserver"
+ "SBCoverSheetPresentationManager disableIconFlyInAnimation: %{BOOL}u"
+ "SBDeviceAppSHDisableMultitaskingAssertionManager"
+ "SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager"
+ "SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager-%@"
+ "SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager.m"
+ "SBGenieEffectViewMatchMoveAnimation"
+ "SBStartupDidCompleteNotification"
+ "SBStripLayoutWindowingModifier"
+ "Stopped before continuing on to SBDefaultImplementationsSwitcherModifier"
+ "T@\"<BPSCancellable>\",&,N,V_cancellable"
+ "T@\"BPSPublisher\",R,N,V_appearancePublisher"
+ "T@\"CAMeshTransform\",C,N,V_meshTransform"
+ "T@\"NSDate\",&,N,V_lastAppearanceChangeTimestamp"
+ "T@\"NSDate\",C,D,N"
+ "T@\"NSDate\",C,N,V_lastAppearanceChangeTimestamp"
+ "T@\"NSTimer\",&,N,V_heldModifierKeyRevealTimer"
+ "T@\"SBDeviceApplicationSceneHandleDisableMultitaskingAssertionManager\",R,N,V_sceneHandleDisableMultitaskingAssertionManager"
+ "T@\"SBSwitcherCoordinatedLayoutStateTransitionContext\",R,W,N,V_coordinatedLayoutStateTransitionContext"
+ "T@\"UITapGestureRecognizer\",&,N,V_windowTopRegionScrollToTopTapGestureRecognizer"
+ "T@\"UITapGestureRecognizer\",R,N,V_tapGestureRecognizer"
+ "T@\"UIView\",&,N,V_overlayPortalView"
+ "TB,N,GisObserving,V_observing"
+ "TB,N,GisObservingLayoutStateTransitions,V_observingLayoutStateTransitions"
+ "TB,N,V_canAddVelocityKickToHurdleDock"
+ "TB,N,V_portaledContentShouldMatchSource"
+ "TB,R,N,V_isFooterViewOfItemContainer"
+ "TB,R,N,V_isRotation"
+ "TB,R,N,V_wantsOverlayPortal"
+ "Td,N,V_genieCornerRadiusToAppResetDelay"
+ "Td,N,V_genieCornerRadiusToHomeResetDelay"
+ "Td,N,V_homeGestureZoomDownScaleMultiplier"
+ "Td,N,V_homeGestureZoomDownScaleMultiplierWidgets"
+ "Td,N,V_menuRevealExtraYThresholdForPointerWhenUnderExternalDisplay"
+ "Td,N,V_minimizedScale"
+ "T{CGPoint=dd},R,N,V_liftOffVelocity"
+ "T{CGSize=dd},N,V_minimumOutsetSize"
+ "Window Scroll-to-Top Tap"
+ "Zoom Down Scale Multiplier"
+ "Zoom Down Scale Multiplier Widgets"
+ "[%{public}@ _registerForWork] Handling launch for posters task: [%{public}@:%{public}@]"
+ "[%{public}@ _schedulerQueue_submitTaskRequestForUpdate] About to submit posters task: [%{public}@:%{public}@]"
+ "[%{public}@ _schedulerQueue_submitTaskRequestForUpdate] Failed to submit posters task: [%{public}@:%{public}@], error: %{public}@"
+ "[%{public}@ _schedulerQueue_submitTaskRequestForUpdate] Successfully submitted posters task: [%{public}@:%{public}@], error: %{public}@"
+ "[%{public}@ executeUpdate] PosterBoardUpdate completed. Background Task: [%{public}@:%{public}@]"
+ "[%{public}lu] Advancing from phase %@ to %@ because: (milestone completed: %{BOOL}u - %@, timer completed: %{BOOL}u - %@)"
+ "[%{public}lu] Change InterSensor indicator state to appeared from: %@"
+ "[%{public}lu] Change InterSensor indicator state to appearing from: %@"
+ "[%{public}lu] Change InterSensor indicator state to disappeared from: %@"
+ "[%{public}lu] Change InterSensor indicator state to disappearing from: %@"
+ "[%{public}lu] Change Micro indicator state to accepting from: %@"
+ "[%{public}lu] Change Micro indicator state to appearing from: %@"
+ "[%{public}lu] Change Micro indicator state to disappearing from: %@"
+ "[%{public}lu] Change Micro indicator state to ejecting from: %@"
+ "[%{public}lu] Change micro indicator ejecting state to accepted from: %@"
+ "[%{public}lu] Change micro indicator ejecting state to ejected from: %@"
+ "[%{public}lu] Change micro indicator state to appeared from: %@"
+ "[%{public}lu] Change micro indicator state to disappeared from: %@"
+ "[%{public}lu] Creating appearance milestone for intersensor region: disappearance milestone does not exist"
+ "[%{public}lu] Creating appearance milestone for intersensor region: disappearance milestone exists"
+ "[%{public}lu] Creating appearance milestone for micro region: disappearance milestone does not exist"
+ "[%{public}lu] Creating appearance milestone for micro region: disappearance milestone exists"
+ "[%{public}lu] Creating appearance milestone for micro region: ejected milestone does not exist"
+ "[%{public}lu] Creating appearance milestone for micro region: ejected milestone exists"
+ "[%{public}lu] Creating disappearance milestone for intersensor region: appearance milestone does not exist"
+ "[%{public}lu] Creating disappearance milestone for intersensor region: appearance milestone exists"
+ "[%{public}lu] Creating disappearance milestone for micro region: accepted milestone does not exist"
+ "[%{public}lu] Creating disappearance milestone for micro region: accepted milestone exists"
+ "[%{public}lu] Creating disappearance milestone for micro region: appearance milestone does not exist"
+ "[%{public}lu] Creating disappearance milestone for micro region: appearance milestone exists"
+ "[%{public}lu] It is unexpected to have a timer running when there isn't a milestone being tracked. Tossing: %@"
+ "[%{public}lu] The associated phase transition identity changed, indicating something is very wrong in the stack and we should skip this phase: %@; Property ID: %@; timer ID: %@; new property ID: %@"
+ "[Glass Cursive] Pending transition for startup"
+ "[Glass Cursive] Started transition on time"
+ "[Glass Cursive] Startup completed, beginning pended animation"
+ "_SBSwitcherGenieEffectContentView"
+ "__SBExtendedDisplayMenuBarManagerPresenceChangedNotification"
+ "_addGaussianBlurToViewIfNeeded:"
+ "_appearanceChangeObserver"
+ "_averageVelocity"
+ "_boundsProperty"
+ "_c2_lock"
+ "_c2_presentationUpdatePaused"
+ "_cachedLastWindowLayoutAttributesPerDisplayOrdinal"
+ "_canAddVelocityKickToHurdleDock"
+ "_canStartGlassCursiveTitleAnimation"
+ "_cancellable"
+ "_childContentView"
+ "_didSelectHeaderForLayoutRole:inAppLayout:"
+ "_disableMultitaskingAssertion"
+ "_externalDisplayConnectionObserver"
+ "_forLoggingOnly_enumerateQueryResponderChainStartingAtModifier:usingBlock:"
+ "_forwardingTargetForUpdate"
+ "_genieCornerRadiusToAppResetDelay"
+ "_genieCornerRadiusToHomeResetDelay"
+ "_handleCoverSheetTranslationForPasscodeLockVisible:blockingForOtherReasons:ignoringPreflightRequirementsForPresentation:"
+ "_handleRequestAppSwitcherResetLayoutAttributes:fromClient:"
+ "_handleScrollToTopGesture:"
+ "_hasForwardedUpdate"
+ "_hasResetCornerRadius"
+ "_heldModifierKeyRevealTimer"
+ "_homeGestureZoomDownScaleMultiplier"
+ "_homeGestureZoomDownScaleMultiplierWidgets"
+ "_iconAndLabelFooter"
+ "_initialFrameOfMinimizingItem"
+ "_initialLayoutAttributes"
+ "_isCursiveTitleAnimationDesired"
+ "_isFooterViewOfItemContainer"
+ "_isFrameValid:"
+ "_isIconFlyInAnimationAllowed"
+ "_isOnEmbeddedDisplayWithExternalConnected"
+ "_isPendingViewsForAcceleratedHomeGesture"
+ "_isPointValid:"
+ "_isRotation"
+ "_lastAppearanceChangeTimestamp"
+ "_layoutContentAndContainerViewWithAttributes:"
+ "_menuRevealExtraYThresholdForPointerWhenUnderExternalDisplay"
+ "_minimizedScale"
+ "_minimizingItem"
+ "_minimumOutsetSize"
+ "_modelUpdatesPaused"
+ "_modifierViolatingTest:forAnchorPointForIndex:"
+ "_modifierViolatingTest:forFrameForIndex:"
+ "_modifierViolatingTest:forFrameForLayoutRole:inAppLayout:withBounds:"
+ "_modifierViolatingTest:forPerspectiveAngleForIndex:"
+ "_modifierViolatingTest:forPerspectiveAngleForLayoutRole:inAppLayout:"
+ "_modifierViolatingValidFloatForScaleForIndex:"
+ "_modifierViolatingValidFloatForScaleForLayoutRole:inAppLayout:"
+ "_observingLayoutStateTransitions"
+ "_overlayPortalView"
+ "_pendingPhaseTransitionTimerIdentity"
+ "_portaledContentShouldMatchSource"
+ "_primaryTextFontSize"
+ "_removeGaussianBlurFromViewIfNeeded:"
+ "_responseForDismissingStrip"
+ "_sceneHandleDisableMultitaskingAssertionManager"
+ "_schedulerQueue"
+ "_schedulerQueue_submitTaskRequestForUpdate:updateIdentifier:"
+ "_selectedAppLayoutWasInitiallyFullScreen"
+ "_setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:"
+ "_setWantsOverlayPortalView:"
+ "_shouldBeginWindowTopRegionTapGesture:"
+ "_shouldDeferVisibleOverlayAndUnderlayViewsUpdate"
+ "_shouldReenableChamoisWhenAssertionInvalidates"
+ "_shouldReenableMultitaskingWhenAssertionInvalidates"
+ "_shouldTopRegionScrollToTopGesture:receiveTouch:"
+ "_startObserving"
+ "_startupDidFinish:"
+ "_statusBarScrollToTopTapGestureRecognizer"
+ "_stopObservingSceneHandles"
+ "_upcomingAppLayoutForExitingAppExpose"
+ "_updateAccessoryTitlePresenceForAdjustedAppLayout:"
+ "_updateDisableMultitaskingWhileForegroundAssertionIfNeeded"
+ "_updateGenieMeshTransformForPresentationLayer:properties:boundsProperty:attributes:"
+ "_updateItemContainerTitlePresenceForLeafAppLayout:"
+ "_updateMedusaMultitaskingEnabled"
+ "_updateStripModifierIfNeeded"
+ "_updateTitlePresenceOnItemContainersForAdjustedAppLayout:"
+ "_updatedPreferencesAddingMilestonesIfNeededWithPreferences:context:"
+ "_wantsOverlayPortal"
+ "_windowTopRegionScrollToTopTapGestureRecognizer"
+ "acquireDisableMultitaskingAssertionForSceneHandle:"
+ "addPortaledContentView:"
+ "allowsCommandeering"
+ "allowsTestingStoreDemoMode"
+ "applicationSceneViewController:didUpdateStatusBarHidden:"
+ "canAddVelocityKickToHurdleDock"
+ "cancelMenuBarRevealForHeldModifierKey"
+ "cancellable"
+ "clearLastWindowLayoutAttributes"
+ "com.apple.QRCode"
+ "contentPageViewScaleForLayoutRole:inAppLayout:withContentPageViewScale:"
+ "coverSheetSlidingViewControllerIsInterstitialAllowed:"
+ "currentAccessoryType"
+ "currentGenieFrameForVisibleAppLayout:"
+ "customEdgeSpacing"
+ "d40@0:8q16@\"SBAppLayout\"24d32"
+ "d40@0:8q16@24d32"
+ "d40@?0@\"SBChainableModifier\"8q16@24d32"
+ "disableIconFlyInAnimation"
+ "disablesMultitaskingWhileForeground"
+ "displayItemPrefersStatusBarHidden:"
+ "dodgeSensorAreaOnIntrinsicContentSize"
+ "dummy"
+ "executeUpdate:forBackgroundTask:updateIdentifier:"
+ "first"
+ "genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:minimizedScale:containerSize:minimumOutsetSize:genieScale:multiplier:active:layoutSettings:"
+ "genieCornerRadiusToAppResetDelay"
+ "genieCornerRadiusToHomeResetDelay"
+ "genieEffectViewDidBegin:"
+ "genieLayout"
+ "gestureHandlingModifierReleasePendingViews:"
+ "hasCompletedStartup"
+ "heldModifierKeyRevealTimer"
+ "homeGestureZoomDownScaleMultiplier"
+ "homeGestureZoomDownScaleMultiplierWidgets"
+ "homeScreenIconBadgeOffsetForAppLayout:"
+ "homeScreenIconBadgeSizeForAppLayout:"
+ "horizontalSpacingBetweenLeadingAndCenter"
+ "horizontalSpacingBetweenTrailingAndCenter"
+ "initWithAppLayout:applicationSceneHandleProvider:displayIdentity:showCanvasTitles:isChamoisOrFlexibleWindowingEnabled:isFooterViewOfItemContainer:"
+ "initWithAppLayoutsInStrip:"
+ "initWithSwitcherCoordinator:commandTabController:"
+ "initWithText:style:font:textColor:"
+ "initWithTransitionID:appLayout:nonGestureInitiatedZoomModifier:effectiveStartingEnvironmentMode:liftOffVelocity:adjustAnimationAttributes:showingOrAnimatingCardsForFlyIn:"
+ "initWithTransitionID:selectedDisplayItem:toAppLayout:initialAppLayout:liftOffVelocity:"
+ "isFooterViewOfItemContainer"
+ "isLeadingStatusBarRegionPreferredHiddenByApp"
+ "isObservingLayoutStateTransitions"
+ "isPendingViewsForAcceleratedHomeGesture"
+ "isPresentingDismissableOffScreenInterstitial"
+ "isPressDemoModeEnabled:"
+ "isRotation"
+ "isStatusBarPartPreferredHiddenByApp:"
+ "isStoreDemoModeEnabled:"
+ "isTrailingStatusBarRegionPreferredHiddenByApp"
+ "item container title and icon opacity"
+ "itemContainer:didSelectTitleForRole:"
+ "itemContainerDidUpdateWantsOverlayPortal:"
+ "kSBFullScreenToHomeCornerRadiusDelayReason"
+ "lastAppearanceChangeTimestamp"
+ "lastWindowLayoutAttributesForDisplayOrdinal:"
+ "liftOffVelocity"
+ "listLayout"
+ "liveContentOverlay:didUpdateStatusBarHiddenSceneSettings:"
+ "medusaDecoratedApplicationSceneViewController:didUpdateStatusBarHidden:"
+ "menuRevealExtraYThresholdForPointerWhenUnderExternalDisplay"
+ "meshContainerOutset"
+ "minimizedScale"
+ "minimumOutsetSize"
+ "no visible appLayout for selected item container: %{public}@"
+ "noteApplicationTransition"
+ "notifyAssistantOfApplicationTransition"
+ "observing"
+ "observingLayoutStateTransitions"
+ "overlayPortalView"
+ "performDeferredUpdateVisibleOverlayAndUnderlayViews"
+ "portaledContentShouldMatchSource"
+ "prioritizesSortOrderForAppLayout:"
+ "removeApplicationPlaceholder:pruneEmptyIcons:"
+ "replaceObjectsInRange:withObjectsFromArray:"
+ "resetLayoutAttributesWithCompletion:"
+ "sbh_dockGlassUserInterfaceStyleFromTraitCollection:"
+ "scale.x"
+ "scale.y"
+ "sceneHandleDisableMultitaskingAssertionManager"
+ "scheduleMenuBarRevealForHeldModifierKey"
+ "second"
+ "setApplicationRelationship:"
+ "setCanAddVelocityKickToHurdleDock:"
+ "setCancellable:"
+ "setChildContentView:"
+ "setCustomPillShapePath:animated:"
+ "setExcludingShadow:"
+ "setGenieCornerRadiusToAppResetDelay:"
+ "setGenieCornerRadiusToHomeResetDelay:"
+ "setHeldModifierKeyRevealTimer:"
+ "setHomeGestureZoomDownScaleMultiplier:"
+ "setHomeGestureZoomDownScaleMultiplierWidgets:"
+ "setLastAppearanceChangeTimestamp:"
+ "setLastWindowLayoutAttributes:forDisplayOrdinal:"
+ "setMedusaMultitaskingEnabled:"
+ "setMenuRevealExtraYThresholdForPointerWhenUnderExternalDisplay:"
+ "setMinimizedScale:"
+ "setMinimumOutsetSize:"
+ "setObserving:"
+ "setObservingLayoutStateTransitions:"
+ "setOverlayPortalView:"
+ "setPasscodeLockVisible:intent:ignoringPreflightRequirementsForPresentation:animated:completion:"
+ "setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:"
+ "setPortaledContentShouldMatchSource:"
+ "setPortaledContentViews:"
+ "setPreallocatesBounds:"
+ "setTaskCompleted"
+ "setWindowTopRegionScrollToTopTapGestureRecognizer:"
+ "shouldDeferVisibleOverlayAndUnderlayViewsUpdate"
+ "stewieStateDidChangeForStateProvider:usingStewieForSOS:isInactiveSOSEnabled:usingStewieConnection:usingStewieConnectionOverInternet:"
+ "systemServiceServer:resetLayoutAttributesForClient:completion:"
+ "tapGestureRecognizer"
+ "updateEntriesWithBlock:"
+ "useItemContainerFooterViewsForAppLayout:"
+ "v24@0:8@?<@\"SBDisplayItemLayoutAttributes\"@?@\"SBDisplayItemLayoutAttributesKey\"@\"SBDisplayItemLayoutAttributes\">16"
+ "v28@0:8@\"<SBSwitcherLiveContentOverlay>\"16B24"
+ "v28@0:8@\"SBDeviceApplicationSceneViewController\"16B24"
+ "v28@0:8@\"SBMedusaDecoratedDeviceApplicationSceneViewController\"16B24"
+ "v28@0:8B16B20B24"
+ "v32@?0@\"SBSwitcherController\"8Q16^B24"
+ "v40@0:8@\"SBSystemServiceServer\"16@\"<FBSServiceFacilityClientHandle>\"24@?<v@?>32"
+ "v40@0:8@\"STTelephonyStateProvider\"16B24B28B32B36"
+ "v40@0:8@16B24B28B32B36"
+ "v40@0:8B16i20B24B28@?32"
+ "v40@0:8B16i20B24B28@?<v@?>32"
+ "v44@0:8B16@20@28@36"
+ "verticalItemSpacing"
+ "verticalSpacingBetweenPrimaryAndSecondary"
+ "wantsOverlayPortal"
+ "windowTopRegionScrollToTopTapGestureRecognizer"
+ "{?=\"switcherGestureManagerForSwitcherContentController\"b1\"sceneRelevancyManagerForSwitcherContentController\"b1\"switcherIconZoomContextProviderForSwitcherContentController\"b1\"homeGestureSettingsForSwitcherContentController\"b1\"maximumNumberOfScenesOnStageForSwitcherContentController\"b1\"activeTransientOverlayPresentedAppLayoutForSwitcherContentController\"b1\"appLayoutForWorkspaceTransientOverlay\"b1\"viewControllerForTransientOverlayAppLayout\"b1\"createWorkspaceTransientOverlayForAppLayout\"b1\"matchingIconViewForIconView\"b1\"prioritizesSortOrderForAppLayout\"b1\"switcherContentControllerFrameForFloatingAppLayoutInInterfaceOrientationFloatingConfiguration\"b1\"switcherContentControllerFrameForCenterItemWithConfigurationInterfaceOrientation\"b1\"homeScreenInterfaceOrientationForContentController\"b1\"backdropInterfaceStyleForContentController\"b1\"switcherContentControllerShouldMorphToPIPForTransitionContext\"b1\"switcherContentControllerShouldMorphFromPIPForTransitionContext\"b1\"isInAppStatusBarRequestedHiddenForSwitcherContentController\"b1\"leadingStatusBarPartFrameForSwitcherContentController\"b1\"trailingStatusBarPartFrameForSwitcherContentController\"b1\"switcherContentControllerVisibleAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerVisibleDisplayItemsForBundleIdentifier\"b1\"switcherContentControllerHiddenAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerReloadsSnapshotsForActiveInterfaceOrientationChange\"b1\"switcherContentControllerHasMultipleDisplays\"b1\"switcherContentControllerSupportsTitleItemsForAppLayout\"b1\"switcherContentControllerSupportsKillingOfAppLayout\"b1\"switcherContentControllerDisplayItemSupportsCenterRole\"b1\"switcherContentControllerIsKeyboardHomeAffordanceAssertionCurrentlyBeingTaken\"b1\"switcherContentControllerDeviceApplicationSceneHandleForDisplayItem\"b1\"isDisplayEmbeddedForSwitcherContentController\"b1\"windowManagementContextForSwitcherContentController\"b1\"draggingAppLayoutsForWindowDragForSwitcherContentController\"b1\"proposedAppLayoutsForWindowDragForSwitcherContentController\"b1\"isSwitcherContentControllerEphemeral\"b1\"displayConfigurationsOfOtherDisplaysForSwitcherContentController\"b1\"guardedForegroundDisplayItemsForSwitcherContentController\"b1\"windowingConfigurationForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1\"appLayoutForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1}"
+ "{CGSize=dd}24@0:8@\"SBAppLayout\"16"
+ "\xc1Q"
+ "\xf0\xf01\xa1"
+ "\xf0\xf0a"
- "\"q"
- "@\"SBWindowingModifier\""
- "@148@0:8{CGPoint=dd}16{CGPoint=dd}32{CGPoint=dd}48{CGSize=dd}64{CGSize=dd}80{CGSize=dd}96d112{CGPoint=dd}120B136@140"
- "@48@0:8@16@24@32B40B44"
- "@68@0:8@16@24@32q40{CGPoint=dd}48B64"
- "Can't read Display.Appearance stream with error: %@"
- "Display appearance live stream error: %@"
- "Failed to submit Posters prewarm task with error: %{public}@"
- "SBApplicationLastWindowSizeKey"
- "SBCollapsedStripLayoutWindowingModifier"
- "SBExpandedStripLayoutWindowingModifier"
- "SBExpansionAnimationCompleteReason"
- "SBFlexibleWindowingStripSteadyStateModifierKey"
- "SBFullScreenContinuousExposeSwitcherModifierBeginAnimatedStripDismissalReason"
- "SBStripDismissalDelayReason"
- "SBStripExpansionAnimationModifier"
- "SBStripExpansionAnimationModifier.m"
- "SBStripLayoutRootWindowingModifier"
- "SBStripPresentWhileMinimizingItemThenDismissAnimationModifier"
- "Submitted Posters prewarm task with error: %{public}@"
- "T@\"BPSPublisher\",&,N,V_appearancePublisher"
- "T@\"CAMeshTransform\",N,V_meshTransform"
- "T@\"NSDate\",&,V_lastAppearanceTimestamp"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_appearanceQueue"
- "T@\"SBDisplayItemLayoutAttributes\",&,N"
- "T@\"SBSwitcherController\",R,N,V_switcherController"
- "T@\"SBSwitcherCoordinatedLayoutStateTransitionContext\",R,N,V_coordinatedLayoutStateTransitionContext"
- "TB,R,N,V_isInlineAppExpose"
- "TB,V_isObserving"
- "Tq,R,N,V_expansionMode"
- "UserInterfaceStyleBoth"
- "UserInterfaceStyleCurrent"
- "Using %s mode for snapshots"
- "[%{public}lu] Change InterSensor indicator state to appeared"
- "[%{public}lu] Change InterSensor indicator state to appearing"
- "[%{public}lu] Change InterSensor indicator state to disappeared"
- "[%{public}lu] Change InterSensor indicator state to disappearing"
- "[%{public}lu] Change Micro indicator state to accepting"
- "[%{public}lu] Change Micro indicator state to appearing"
- "[%{public}lu] Change Micro indicator state to disappearing"
- "[%{public}lu] Change Micro indicator state to ejecting"
- "[%{public}lu] Change micro indicator ejecting state to accepted"
- "[%{public}lu] Change micro indicator ejecting state to ejected"
- "[%{public}lu] Change micro indicator state to appeared"
- "[%{public}lu] Change micro indicator state to disappeared"
- "[%{public}lu] The associated phase transition identity changed, indicating something is very wrong in the stack and we should skip this phase: %@"
- "[ActivityID: %{public}@] alert presentation failed for original destination. Looking for fallback destination."
- "[ActivityID: %{public}@] posting banner as fallback alert"
- "[ActivityID: %{public}@] posting fallback alert"
- "_appearanceQueue"
- "_backgroundShadowView"
- "_bottomAppFinalMaxY"
- "_bottomAppInitialMinY"
- "_bundleIdShowingAppExpose"
- "_cachedLastWindowLayoutAttributesOrNSNull"
- "_expansionMode"
- "_finishSwappingPlaceholderAfterCachingIcon:"
- "_fromItemSet"
- "_fromSteadyStateModifier"
- "_fromStrip"
- "_handleCoverSheetTranslationForPasscodeLockVisible:blockingForOtherReasons:"
- "_handleRealTimeAppearanceChange:"
- "_isInlineAppExpose"
- "_isObserving"
- "_lastAppearanceTimestamp"
- "_loadLastAppearanceChangeWithCompletion:"
- "_performTransactionWithTemporaryChildModifier:strip:usingBlock:"
- "_postBannerWithAlert:"
- "_removingPlaceholderProxies"
- "_shouldBeginWindowTopRegionDoubleTapGesture:"
- "_shouldPrioritizeSortOrderForAppLayout:"
- "_stopObservingAppearanceChanges"
- "_stripOrderedItems"
- "_stripOverride"
- "_submitTaskRequestForUpdate:"
- "_subscribeToAppearanceChanges"
- "_toExpansionMode"
- "_toItemSet"
- "_toSteadyStateModifier"
- "_toStrip"
- "_topAppFinalMinY"
- "_topAppInitialMaxY"
- "_uniqueDismissalDelayReason"
- "_updateGenieMeshTransformForPresentationLayer:properties:attributes:"
- "_updateLastAppearanceTimestamp:"
- "_updateTitlePresenceForAdjustedAppLayout:"
- "_updatedPreferencesAddingMilestonesIfNeededWithPreferences:"
- "_windowTopRegionDoubleTapGestureRecognizer should begin: touch (%@) hit-tested to item container (%@) and was inside edge swipe hit test rect (%@)"
- "alertPresentationFailed:"
- "appLayoutToAttachStripDivider"
- "appearanceQueue"
- "cacheImageForIcon:imageAppearance:options:completionHandler:"
- "com.example.SBPhoneSceneSnapshotRequestStrategy.appearance"
- "executeUpdate:"
- "expansionMode"
- "fromSteadyStateModifier"
- "fromStrip"
- "genieAttributesForIconPosition:windowPosition:initialVelocity:windowSize:minimizedSize:containerSize:genieScale:multiplier:active:layoutSettings:"
- "inUpdatePhase"
- "initWithAppLayout:applicationSceneHandleProvider:displayIdentity:showCanvasTitles:isChamoisOrFlexibleWindowingEnabled:"
- "initWithAppLayoutsInStrip:expansionMode:isInlineAppExpose:"
- "initWithFromSteadyStateModifier:toSteadyStateModifier:fromStrip:toStrip:"
- "initWithRecentAppLayoutsController:commandTabController:"
- "initWithTransitionID:appLayout:nonGestureInitiatedZoomModifier:effectiveStartingEnvironmentMode:liftOffVelocity:adjustAnimationAttributes:"
- "initWithTransitionID:selectedDisplayItem:toAppLayout:initialAppLayout:"
- "isInlineAppExpose"
- "isPresentingInterstitialWhileOffScreen"
- "itemContainer:didUpdateShowingIconOverlay:"
- "lastAppearanceTimestamp"
- "lastWindowLayoutAttributes"
- "presentFallbackAlert:"
- "setAppearancePublisher:"
- "setAppearanceQueue:"
- "setContentViews:"
- "setIsObserving:"
- "setLastAppearanceTimestamp:"
- "setLastWindowLayoutAttributes:"
- "setOverrideLegibilitySettings:"
- "setPasscodeLockVisible:intent:animated:completion:"
- "stewieStateDidChangeForStateProvider:usingStewieForSOS:isInactiveSOSEnabled:usingStewieConnection:"
- "toSteadyStateModifier"
- "toStrip"
- "v24@?0@\"<SBWindowingItem>\"8^B16"
- "v32@?0@\"<SBWindowingItem>\"8@\"SBMutableWindowingItemViewModel\"16^B24"
- "v36@0:8@\"STTelephonyStateProvider\"16B24B28B32"
- "v36@0:8@16B24B28B32"
- "v36@0:8B16i20B24@?28"
- "v36@0:8B16i20B24@?<v@?>28"
- "{?=\"switcherGestureManagerForSwitcherContentController\"b1\"sceneRelevancyManagerForSwitcherContentController\"b1\"switcherIconZoomContextProviderForSwitcherContentController\"b1\"homeGestureSettingsForSwitcherContentController\"b1\"maximumNumberOfScenesOnStageForSwitcherContentController\"b1\"activeTransientOverlayPresentedAppLayoutForSwitcherContentController\"b1\"appLayoutForWorkspaceTransientOverlay\"b1\"viewControllerForTransientOverlayAppLayout\"b1\"createWorkspaceTransientOverlayForAppLayout\"b1\"matchingIconViewForIconView\"b1\"switcherContentControllerFrameForFloatingAppLayoutInInterfaceOrientationFloatingConfiguration\"b1\"switcherContentControllerFrameForCenterItemWithConfigurationInterfaceOrientation\"b1\"homeScreenInterfaceOrientationForContentController\"b1\"backdropInterfaceStyleForContentController\"b1\"switcherContentControllerShouldMorphToPIPForTransitionContext\"b1\"switcherContentControllerShouldMorphFromPIPForTransitionContext\"b1\"isInAppStatusBarRequestedHiddenForSwitcherContentController\"b1\"leadingStatusBarPartFrameForSwitcherContentController\"b1\"trailingStatusBarPartFrameForSwitcherContentController\"b1\"switcherContentControllerVisibleAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerVisibleDisplayItemsForBundleIdentifier\"b1\"switcherContentControllerHiddenAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerReloadsSnapshotsForActiveInterfaceOrientationChange\"b1\"switcherContentControllerHasMultipleDisplays\"b1\"switcherContentControllerSupportsTitleItemsForAppLayout\"b1\"switcherContentControllerSupportsKillingOfAppLayout\"b1\"switcherContentControllerDisplayItemSupportsCenterRole\"b1\"switcherContentControllerIsKeyboardHomeAffordanceAssertionCurrentlyBeingTaken\"b1\"switcherContentControllerDeviceApplicationSceneHandleForDisplayItem\"b1\"isDisplayEmbeddedForSwitcherContentController\"b1\"windowManagementContextForSwitcherContentController\"b1\"draggingAppLayoutsForWindowDragForSwitcherContentController\"b1\"proposedAppLayoutsForWindowDragForSwitcherContentController\"b1\"isSwitcherContentControllerEphemeral\"b1\"displayConfigurationsOfOtherDisplaysForSwitcherContentController\"b1\"guardedForegroundDisplayItemsForSwitcherContentController\"b1\"windowingConfigurationForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1\"appLayoutForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1}"
- "\xc1A"
- "\xc5S"
- "\xf0\xf0Q"
- "\xf0\xf0\xe1"

```
