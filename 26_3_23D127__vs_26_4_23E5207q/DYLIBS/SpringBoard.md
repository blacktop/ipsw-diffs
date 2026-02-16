## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.3.9.102.0
-  __TEXT.__text: 0xa9d810
-  __TEXT.__auth_stubs: 0x55a0
+4557.4.7.100.0
+  __TEXT.__text: 0xb1ca3c
+  __TEXT.__auth_stubs: 0x5590
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb8830
-  __TEXT.__const: 0x12ec0
-  __TEXT.__oslogstring: 0x5e94c
-  __TEXT.__cstring: 0x7d88c
-  __TEXT.__gcc_except_tab: 0x19c34
+  __TEXT.__objc_methlist: 0xb9878
+  __TEXT.__const: 0x13040
+  __TEXT.__oslogstring: 0x5f14b
+  __TEXT.__cstring: 0x7e5fb
+  __TEXT.__gcc_except_tab: 0x194c8
   __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2c840
-  __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x22338
-  __TEXT.__objc_methname: 0x1d2b60
-  __TEXT.__objc_methtype: 0x4d3e0
-  __TEXT.__objc_stubs: 0xf5600
-  __DATA_CONST.__got: 0xa338
-  __DATA_CONST.__const: 0x1cc10
-  __DATA_CONST.__objc_classlist: 0x52b8
-  __DATA_CONST.__objc_catlist: 0x370
+  __TEXT.__unwind_info: 0x30320
+  __TEXT.__objc_classname: 0x2254f
+  __TEXT.__objc_methname: 0x1d563e
+  __TEXT.__objc_methtype: 0x4d774
+  __TEXT.__objc_stubs: 0xf6640
+  __DATA_CONST.__got: 0xa3d0
+  __DATA_CONST.__const: 0x1cea0
+  __DATA_CONST.__objc_classlist: 0x5310
+  __DATA_CONST.__objc_catlist: 0x358
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2928
+  __DATA_CONST.__objc_protolist: 0x2938
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b1e8
-  __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3fd8
+  __DATA_CONST.__objc_selrefs: 0x4b700
+  __DATA_CONST.__objc_protorefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0x4010
   __DATA_CONST.__objc_arraydata: 0x1870
-  __AUTH_CONST.__auth_got: 0x2ae8
-  __AUTH_CONST.__const: 0x10cd8
-  __AUTH_CONST.__cfstring: 0x6f880
-  __AUTH_CONST.__objc_const: 0x26c630
+  __AUTH_CONST.__auth_got: 0x2ae0
+  __AUTH_CONST.__const: 0x111c0
+  __AUTH_CONST.__cfstring: 0x702c0
+  __AUTH_CONST.__objc_const: 0x26f178
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x790
   __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x109f0
-  __DATA.__objc_ivar: 0xf564
-  __DATA.__data: 0x1f8b8
+  __AUTH.__objc_data: 0x10860
+  __DATA.__objc_ivar: 0xf6d8
+  __DATA.__data: 0x1fb68
   __DATA.__bss: 0xac0
-  __DATA.__common: 0xa40
-  __DATA_DIRTY.__objc_data: 0x23140
-  __DATA_DIRTY.__data: 0x180
+  __DATA.__common: 0xa48
+  __DATA_DIRTY.__objc_data: 0x23640
+  __DATA_DIRTY.__data: 0x188
   __DATA_DIRTY.__bss: 0x1a88
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 7212C633-68AD-3517-9B45-C0DF6E3DF731
-  Functions: 70452
-  Symbols:   238272
-  CStrings:  104788
+  UUID: 17346862-3005-3A07-AC95-15D705B33EE7
+  Functions: 71452
+  Symbols:   241701
+  CStrings:  105282
 
Symbols:
+ +[SBSiriHUDSceneController _setupInfo]
+ -[SBAssistantSceneController _beginObservingLayoutStateTransitionsIfNeeded]
+ -[SBAssistantSceneController _disablesHomeAffordanceDoubleTapGestureInLandscape]
+ -[SBAssistantSceneController _endObservingLayoutStateTransitionsIfNeeded]
+ -[SBAssistantSceneController _lastKnownInterfaceOrientationIsLandscape]
+ -[SBAssistantSceneController _notifiesAssistantOfApplicationTransitions]
+ -[SBAssistantSceneController _reevaluateHomeAffordanceDoubleTapGestureEnablement]
+ -[SBAssistantSceneController _setHomeAffordanceDoubleTapGestureEnabled:withReason:]
+ -[SBAssistantSceneController lastKnownInterfaceOrientation]
+ -[SBAssistantSceneController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:]
+ -[SBAssistantSceneController layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:]
+ -[SBAssistantSceneController setLastKnownInterfaceOrientation:]
+ -[SBCameraViewfinderMonitorToken cancel].cold.1
+ -[SBDefaultImplementationsSwitcherModifier alphaForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier backgroundForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier bounceIconCenterForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier bounceIconScaleForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier centerForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier contentAlphaForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier contentBlurRadiusForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier contentScaleForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier hiddenWindowsPillModeForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier hiddenWindowsPills]
+ -[SBDefaultImplementationsSwitcherModifier pillOffsetForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier pillScaleForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier shouldBounceIconPresentForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier transformForHiddenWindowsPill:]
+ -[SBDefaultImplementationsSwitcherModifier wantsKeyboardInputEvents]
+ -[SBDeviceApplicationSceneViewController groupOpacityRequiredForContentAnimation]
+ -[SBDisplayItemLayoutAttributesProvider _layoutAttributesForDisplayItem:displayOrdinal:orientation:]
+ -[SBDisplayItemLayoutAttributesProvider layoutAttributesForDisplayItem:displayOrdinal:orientation:]
+ -[SBDisplayItemLayoutAttributesProvider layoutAttributesForDisplayItem:displayOrdinal:orientation:].cold.1
+ -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributesMap:forDisplayOrdinal:orientation:]
+ -[SBEntityRemovalCrossblurSwitcherModifier initWithTransitionID:appLayout:layoutRole:multitaskingModifier:]
+ -[SBEntityRemovalCrossblurSwitcherModifier shouldAllowGroupOpacityForAppLayout:]
+ -[SBFloatingDockRemoteContentManager _updateRemoteContentOverlayFrame:]
+ -[SBFloatingDockRemoteContentManager clientRequestToUpdateFileStackIcon:contentOverlayFrame:]
+ -[SBFloatingDockRemoteContentManager clientRequestToUpdateFileStackIcon:preferredDisplayName:]
+ -[SBFloatingDockRemoteContentManager clientWillDeactivateWithContext:]
+ -[SBFloatingDockRemoteContentManager closingFileStackIcon]
+ -[SBFloatingDockRemoteContentManager remoteContentOverlayFrame]
+ -[SBFloatingDockRemoteContentManager setClosingFileStackIcon:]
+ -[SBFluidSwitcherRootSwitcherModifier hiddenWindowsPillModifierForTransitionEvent:]
+ -[SBFluidSwitcherViewController _applyStyleToHiddenWindowsPill:completion:]
+ -[SBFluidSwitcherViewController _applyStyleToHiddenWindowsPillsWithCompletion:]
+ -[SBFluidSwitcherViewController _currentLayoutAttributesOrientationForSwitcherCorrespondingToDisplayOrdinal:]
+ -[SBFluidSwitcherViewController _hitTestedToTransientUIAtLocation:window:]
+ -[SBFluidSwitcherViewController _layoutHiddenWindowsPill:completion:]
+ -[SBFluidSwitcherViewController _layoutHiddenWindowsPillBounceIcon:completion:]
+ -[SBFluidSwitcherViewController _layoutHiddenWindowsPillsWithCompletion:]
+ -[SBFluidSwitcherViewController _updateHiddenWindowsPillsViews]
+ -[SBFluidSwitcherViewController _updateKeyboardAttentionAwarenessClient]
+ -[SBFluidSwitcherViewController _visibleDisplayItemsForBundleIdentifier:]
+ -[SBFluidSwitcherViewController bounceIconViewsForHiddenWindowsPills]
+ -[SBFluidSwitcherViewController client:attentionLostTimeoutDidExpire:forConfigurationGeneration:withAssociatedObject:]
+ -[SBFluidSwitcherViewController clientDidResetForUserAttention:withEvent:]
+ -[SBFluidSwitcherViewController floatingDockIconFrameForAppLayout:]
+ -[SBFluidSwitcherViewController floatingDockIconScaleForAppLayout:]
+ -[SBFluidSwitcherViewController groupOpacityRequiredWhenRemovingItemContainerForLeafAppLayout:]
+ -[SBFluidSwitcherViewController hiddenWindowsPillHeight]
+ -[SBFluidSwitcherViewController hiddenWindowsPillIconPortals]
+ -[SBFluidSwitcherViewController hiddenWindowsPillViewWasTapped:]
+ -[SBFluidSwitcherViewController hiddenWindowsPills]
+ -[SBFluidSwitcherViewController isHiddenWindowsPillSupported]
+ -[SBFluidSwitcherViewController layoutAttributesForDisplayItem:]
+ -[SBFluidSwitcherViewController layoutAttributesForDisplayItem:displayOrdinal:]
+ -[SBFluidSwitcherViewController numberOfOccludedOrOffStageDisplayItemsForBundleIdentifier:]
+ -[SBFluidSwitcherViewController setBounceIconViewsForHiddenWindowsPills:]
+ -[SBFluidSwitcherViewController setHiddenWindowsPillIconPortals:]
+ -[SBFluidSwitcherViewController setHiddenWindowsPills:]
+ -[SBFluidSwitcherViewController transientUI:wasIndirectPannedToDismissFromGestureRecognizer:]
+ -[SBFluidSwitcherViewController transientUIHandledTouch:withSystemGestureRecognizer:]
+ -[SBFluidSwitcherViewController updateLayoutAttributes:ofDisplayItem:displayOrdinal:]
+ -[SBFluidSwitcherViewController updateLayoutAttributesMap:forDisplayOrdinal:]
+ -[SBFluidSwitcherViewController(Common) _floatingDockIconViewForDisplayItem:isVisible:]
+ -[SBFluidSwitcherViewController(Common) floatingDockIconImageFrameForAppLayout:]
+ -[SBFluidSwitcherViewController(Common) floatingDockIconViewForAppLayout:]
+ -[SBFocusActivityManager isActivityPickerPresented]
+ -[SBFullScreenFluidSwitcherRootSwitcherModifier hiddenWindowsPillModifierForTransitionEvent:]
+ -[SBFullScreenSwitcherLiveContentOverlayCoordinator groupOpacityRequiredWhenRemovingItemContainerForLeafAppLayout:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier .cxx_destruct]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier animationAttributesForLayoutElement:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier bounceIconCenterForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier bounceIconScaleForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier centerForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier dockWindowLevelPriority]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier dockWindowLevel]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier handleTimerEvent:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier handleTransitionEvent:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier hiddenWindowsPillModeForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier hiddenWindowsPill]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier initWithHiddenWindowsPill:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier initWithHiddenWindowsPill:].cold.1
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier pillOffsetForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier pillScaleForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier shouldBounceIconPresentForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier switcherHitTestsAsOpaque]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier transformForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillDismissAnimationSwitcherModifier wantsDockWindowLevelAssertion]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier .cxx_destruct]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier animationAttributesForLayoutElement:]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier backgroundForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier contentAlphaForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier contentBlurRadiusForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier contentScaleForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier direction]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier handleTimerEvent:]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier handleTransitionEvent:]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier hiddenWindowsPill]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier initWithHiddenWindowsPill:direction:]
+ -[SBHiddenWindowsPillMaterializeAnimationSwitcherModifier initWithHiddenWindowsPill:direction:].cold.1
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier .cxx_destruct]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier alphaForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier animationAttributesForLayoutElement:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier bounceIconCenterForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier bounceIconScaleForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier centerForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier dockWindowLevelPriority]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier dockWindowLevel]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier handleTimerEvent:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier handleTransitionEvent:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier hiddenWindowsPillModeForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier hiddenWindowsPill]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier iconFrame]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier initWithHiddenWindowsPill:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier initWithHiddenWindowsPill:].cold.1
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier pillScaleForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier shouldBounceIconPresentForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier switcherHitTestsAsOpaque]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier transformForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillPresentAnimationSwitcherModifier wantsDockWindowLevelAssertion]
+ -[SBHiddenWindowsPillRootSwitcherModifier .cxx_destruct]
+ -[SBHiddenWindowsPillRootSwitcherModifier _dismissalTransitionRequest]
+ -[SBHiddenWindowsPillRootSwitcherModifier _shouldDematerialize]
+ -[SBHiddenWindowsPillRootSwitcherModifier _shouldMaterialize]
+ -[SBHiddenWindowsPillRootSwitcherModifier _willDockBeVisibleAtEndOfTransition]
+ -[SBHiddenWindowsPillRootSwitcherModifier handleGestureEvent:]
+ -[SBHiddenWindowsPillRootSwitcherModifier handleKeyboardInputEvent:]
+ -[SBHiddenWindowsPillRootSwitcherModifier handleTapHiddenWindowsPill:]
+ -[SBHiddenWindowsPillRootSwitcherModifier handleTransientUIIndirectPannedToDismissSwitcherModifierEvent:]
+ -[SBHiddenWindowsPillRootSwitcherModifier handleTransientUITapToDismissSwitcherModifierEvent:]
+ -[SBHiddenWindowsPillRootSwitcherModifier handleTransitionEvent:]
+ -[SBHiddenWindowsPillRootSwitcherModifier hiddenWindowsPill]
+ -[SBHiddenWindowsPillRootSwitcherModifier hiddenWindowsPills]
+ -[SBHiddenWindowsPillRootSwitcherModifier initWithHiddenWindowsPill:]
+ -[SBHiddenWindowsPillRootSwitcherModifier initWithHiddenWindowsPill:].cold.1
+ -[SBHiddenWindowsPillRootSwitcherModifier removeChildModifier:]
+ -[SBHiddenWindowsPillRootSwitcherModifier topMostLayoutElements]
+ -[SBHiddenWindowsPillRootSwitcherModifier wantsKeyboardInputEvents]
+ -[SBHiddenWindowsPillSwitcherModifier .cxx_destruct]
+ -[SBHiddenWindowsPillSwitcherModifier _willDockBeVisibleAtEndOfTransition]
+ -[SBHiddenWindowsPillSwitcherModifier alphaForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillSwitcherModifier backgroundForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillSwitcherModifier centerForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillSwitcherModifier contentAlphaForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillSwitcherModifier contentBlurRadiusForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillSwitcherModifier contentScaleForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillSwitcherModifier handleTransitionEvent:]
+ -[SBHiddenWindowsPillSwitcherModifier hiddenWindowsPillModeForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillSwitcherModifier hiddenWindowsPill]
+ -[SBHiddenWindowsPillSwitcherModifier iconFrame]
+ -[SBHiddenWindowsPillSwitcherModifier initWithHiddenWindowsPill:]
+ -[SBHiddenWindowsPillSwitcherModifier initWithHiddenWindowsPill:].cold.1
+ -[SBHiddenWindowsPillSwitcherModifier pillOffsetForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillSwitcherModifier pillScaleForHiddenWindowsPill:]
+ -[SBHiddenWindowsPillSwitcherModifier transformForHiddenWindowsPill:]
+ -[SBHomeScreenController _iconImageCacheConfigurationFromPosterIconConfiguration:]
+ -[SBHomeScreenController _iconImageCacheConfigurationFromPosterIconConfiguration:].cold.1
+ -[SBHomeScreenController _iconImageCacheConfigurationFromPosterIconConfiguration:].cold.2
+ -[SBHomeScreenController _iconImageCacheConfigurationFromPosterIconConfiguration:].cold.3
+ -[SBHomeScreenController iconManager:extraIconImageCacheConfigurationsForPrecachingWithCompletion:]
+ -[SBHomeScreenController isWallpaperDimmed]
+ -[SBHomeScreenService addFileStackWithURL:preferredDisplayName:]
+ -[SBHomeScreenService addFileStackWithURL:preferredDisplayName:].cold.1
+ -[SBHomeScreenService isWallpaperDimmed]
+ -[SBHomeScreenService isWallpaperDimmed].cold.1
+ -[SBKeyboardInputSwitcherModifierEvent type]
+ -[SBLockScreenBiometricAuthenticationCoordinator _shouldShowAlertForSeed]
+ -[SBMainSwitcherControllerCoordinator isHiddenWindowsPillSupportedForSwitcherContentController:]
+ -[SBMainWorkspaceApplicationSceneLayoutElementViewController groupOpacityRequiredForContentAnimation]
+ -[SBMedusaDecoratedDeviceApplicationSceneViewController groupOpacityRequiredForContentAnimation]
+ -[SBMenuBarManager systemHideMenuWithOptions:clientName:]
+ -[SBMenuBarViewController clientName]
+ -[SBMenuBarViewController setClientName:]
+ -[SBMixedGridSwitcherModifier _cachedCenterCardFrame]
+ -[SBMixedGridSwitcherModifier _isIndexFullScreenOrCenterModal:]
+ -[SBMixedGridSwitcherModifier setSupportsCenterModalAppLayouts:]
+ -[SBMixedGridSwitcherModifier supportsCenterModalAppLayouts]
+ -[SBNotificationCarPlayDestination _cancelCurrentPreprocessedSiriSession]
+ -[SBNotificationCarPlayDestination _clearCurrentPreprocessRequest]
+ -[SBNotificationCarPlayDestination _flushPreprocessRequests]
+ -[SBNotificationCarPlayDestination _hasRequestPreprocessed]
+ -[SBNotificationCarPlayDestination _hasRequestPreprocessing]
+ -[SBNotificationCarPlayDestination _invalidatePreprocessTimeoutTimer]
+ -[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:shouldPreprocess:]
+ -[SBNotificationCarPlayDestination _preprocessNotificationRequest:]
+ -[SBNotificationCarPlayDestination _preprocessTimeoutTimer]
+ -[SBNotificationCarPlayDestination _presentBannerForRequest:]
+ -[SBNotificationCarPlayDestination _processNextPreprocessRequest]
+ -[SBNotificationCarPlayDestination _requestPreprocessForNotificationRequest:]
+ -[SBNotificationCarPlayDestination _setPreprocessTimeoutTimer:]
+ -[SBNotificationCarPlayDestination _shouldPreprocessNotificationRequest:]
+ -[SBNotificationCarPlayDestination _startPreprocessTimeoutTimer]
+ -[SBNotificationCarPlayDestination canActivateChangedTo:]
+ -[SBRecordingIndicatorSettings alwaysSuppressBacklightChanges]
+ -[SBRecordingIndicatorSettings setAlwaysSuppressBacklightChanges:]
+ -[SBRoutingSwitcherModifier alphaForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier backgroundForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier bounceIconCenterForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier bounceIconScaleForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier centerForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier contentAlphaForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier contentBlurRadiusForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier contentScaleForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier hiddenWindowsPillModeForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier hiddenWindowsPills]
+ -[SBRoutingSwitcherModifier pillOffsetForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier pillScaleForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier shouldBounceIconPresentForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier transformForHiddenWindowsPill:]
+ -[SBRoutingSwitcherModifier wantsKeyboardInputEvents]
+ -[SBSwitcherAnimationAttributes bouncePositionSettings]
+ -[SBSwitcherAnimationAttributes bounceScaleSettings]
+ -[SBSwitcherAnimationAttributes pillContentAlphaSettings]
+ -[SBSwitcherAnimationAttributes pillContentBlurSettings]
+ -[SBSwitcherAnimationAttributes pillContentScaleSettings]
+ -[SBSwitcherAnimationAttributes pillMaterializationSettings]
+ -[SBSwitcherAnimationAttributes pillOffsetSettings]
+ -[SBSwitcherAnimationAttributes pillScaleSettings]
+ -[SBSwitcherAnimationAttributes setBouncePositionSettings:]
+ -[SBSwitcherAnimationAttributes setBounceScaleSettings:]
+ -[SBSwitcherAnimationAttributes setPillContentAlphaSettings:]
+ -[SBSwitcherAnimationAttributes setPillContentBlurSettings:]
+ -[SBSwitcherAnimationAttributes setPillContentScaleSettings:]
+ -[SBSwitcherAnimationAttributes setPillMaterializationSettings:]
+ -[SBSwitcherAnimationAttributes setPillOffsetSettings:]
+ -[SBSwitcherAnimationAttributes setPillScaleSettings:]
+ -[SBSwitcherController _buildHideMenuWithAdditionalOptions:clientName:]
+ -[SBSwitcherController hideMenuWithOptions:clientName:]
+ -[SBSwitcherController isHiddenWindowsPillSupported]
+ -[SBSwitcherHiddenWindowsPill .cxx_destruct]
+ -[SBSwitcherHiddenWindowsPill appLayout]
+ -[SBSwitcherHiddenWindowsPill bundleIdentifier]
+ -[SBSwitcherHiddenWindowsPill copyWithZone:]
+ -[SBSwitcherHiddenWindowsPill hash]
+ -[SBSwitcherHiddenWindowsPill initWithBundleIdentifier:numberOfHiddenWindows:]
+ -[SBSwitcherHiddenWindowsPill isAppLayout]
+ -[SBSwitcherHiddenWindowsPill isEqual:]
+ -[SBSwitcherHiddenWindowsPill numberOfHiddenWindows]
+ -[SBSwitcherHiddenWindowsPill switcherLayoutElementType]
+ -[SBSwitcherHiddenWindowsPillView .cxx_destruct]
+ -[SBSwitcherHiddenWindowsPillView _effectiveGlassViewMaterial]
+ -[SBSwitcherHiddenWindowsPillView _handleTap:]
+ -[SBSwitcherHiddenWindowsPillView _makeContentView]
+ -[SBSwitcherHiddenWindowsPillView _makeGlassView]
+ -[SBSwitcherHiddenWindowsPillView _makeGlass]
+ -[SBSwitcherHiddenWindowsPillView _makeImageView]
+ -[SBSwitcherHiddenWindowsPillView _makeMaskProgressAnimatableProperty]
+ -[SBSwitcherHiddenWindowsPillView _makeMaskView]
+ -[SBSwitcherHiddenWindowsPillView _makeSubtitleLabel]
+ -[SBSwitcherHiddenWindowsPillView _makeTitleLabel]
+ -[SBSwitcherHiddenWindowsPillView accessibilityIdentifier]
+ -[SBSwitcherHiddenWindowsPillView background]
+ -[SBSwitcherHiddenWindowsPillView contentAlpha]
+ -[SBSwitcherHiddenWindowsPillView contentBlurRadius]
+ -[SBSwitcherHiddenWindowsPillView contentScale]
+ -[SBSwitcherHiddenWindowsPillView dealloc]
+ -[SBSwitcherHiddenWindowsPillView delegate]
+ -[SBSwitcherHiddenWindowsPillView didMoveToSuperview]
+ -[SBSwitcherHiddenWindowsPillView hiddenWindowsPill]
+ -[SBSwitcherHiddenWindowsPillView initWithHiddenWindowsPill:delegate:]
+ -[SBSwitcherHiddenWindowsPillView intrinsicContentSize]
+ -[SBSwitcherHiddenWindowsPillView layoutSubviews]
+ -[SBSwitcherHiddenWindowsPillView pillMode]
+ -[SBSwitcherHiddenWindowsPillView pillOffset]
+ -[SBSwitcherHiddenWindowsPillView pillScale]
+ -[SBSwitcherHiddenWindowsPillView setBackground:]
+ -[SBSwitcherHiddenWindowsPillView setContentAlpha:]
+ -[SBSwitcherHiddenWindowsPillView setContentBlurRadius:]
+ -[SBSwitcherHiddenWindowsPillView setContentScale:]
+ -[SBSwitcherHiddenWindowsPillView setPillMode:]
+ -[SBSwitcherHiddenWindowsPillView setPillOffset:]
+ -[SBSwitcherHiddenWindowsPillView setPillScale:]
+ -[SBSwitcherHiddenWindowsPillView sizeThatFits:]
+ -[SBSwitcherHiddenWindowsPillView updateProperties]
+ -[SBSwitcherModifier handleKeyboardInputEvent:]
+ -[SBSwitcherModifier handleTapHiddenWindowsPill:]
+ -[SBSwitcherModifier handleTransientUIIndirectPannedToDismissSwitcherModifierEvent:]
+ -[SBSwitcherModifier handleTransientUITapToDismissSwitcherModifierEvent:]
+ -[SBSwitcherModifier(SharedModifierUtilities) dummyAppLayoutWithBundleIdentifier:sceneIdentifier:]
+ -[SBSwitcherWindowingConfiguration interfaceOrientation]
+ -[SBSwitcherWindowingConfiguration setInterfaceOrientation:]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimateDismissCenterYSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimateDismissLayoutSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimateDismissScaleSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimateDismissTranslateYSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimatePillContentAlphaSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimatePillContentBlurSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimatePillContentScaleSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimatePillMaterializationSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimatePresentLayoutSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimatePresentOpacitySettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimatePresentPillScaleSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimatePresentPositionSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimatePresentScaleSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimationDelay]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimationInitialScale]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillAnimationStartDelay]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillBounceAnimationMoveDownSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillBounceAnimationMoveUpSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillBounceAnimationScaleSettings]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillIconBounceHeight]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillNoDockOffscreenOffset]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillVerticalOffsetAboveDock]
+ -[SBSwitcherWindowingSettings hiddenWindowsPillVerticalOffsetNoDock]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimateDismissCenterYSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimateDismissLayoutSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimateDismissScaleSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimateDismissTranslateYSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimatePillContentAlphaSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimatePillContentBlurSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimatePillContentScaleSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimatePillMaterializationSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimatePresentLayoutSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimatePresentOpacitySettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimatePresentPillScaleSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimatePresentPositionSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimatePresentScaleSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimationDelay:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimationInitialScale:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillAnimationStartDelay:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillBounceAnimationMoveDownSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillBounceAnimationMoveUpSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillBounceAnimationScaleSettings:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillIconBounceHeight:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillNoDockOffscreenOffset:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillVerticalOffsetAboveDock:]
+ -[SBSwitcherWindowingSettings setHiddenWindowsPillVerticalOffsetNoDock:]
+ -[SBSystemActionCoachingController focusActivityManager]
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:bannerManager:]
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:bannerManager:].cold.1
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:bannerManager:].cold.2
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:bannerManager:].cold.3
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:bannerManager:].cold.4
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:bannerManager:].cold.5
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:bannerManager:].cold.6
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:bannerManager:].cold.7
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:bannerManager:].cold.8
+ -[SBSystemActionCoachingHUDViewController focusActivityManager]
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:]
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:].cold.1
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:].cold.2
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:].cold.3
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:].cold.4
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:].cold.5
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:].cold.6
+ -[SBSystemActionCoachingHUDViewController setNeedsUpdateCoachingText]
+ -[SBSystemUIScenesCoordinator setSiriHUDSceneController:]
+ -[SBSystemUIScenesCoordinator siriHUDSceneController]
+ -[SBTapHiddenWindowsPillSwitcherModifierEvent .cxx_destruct]
+ -[SBTapHiddenWindowsPillSwitcherModifierEvent hiddenWindowsPill]
+ -[SBTapHiddenWindowsPillSwitcherModifierEvent initWithHiddenWindowsPill:]
+ -[SBTapHiddenWindowsPillSwitcherModifierEvent type]
+ -[SBTransientUIIndirectPanToDismissSwitcherModifierEvent type]
+ -[SBTransientUITapToDismissSwitcherModifierEvent type]
+ -[SBWallpaperController fetchAllPosterIconConfigurationsForPrecaching:]
+ GCC_except_table1033
+ GCC_except_table1040
+ GCC_except_table1042
+ GCC_except_table1044
+ GCC_except_table1046
+ GCC_except_table1048
+ GCC_except_table1050
+ GCC_except_table1052
+ GCC_except_table190
+ GCC_except_table267
+ GCC_except_table270
+ GCC_except_table272
+ GCC_except_table276
+ GCC_except_table278
+ GCC_except_table287
+ GCC_except_table299
+ GCC_except_table311
+ GCC_except_table316
+ GCC_except_table318
+ GCC_except_table345
+ GCC_except_table350
+ GCC_except_table354
+ GCC_except_table356
+ GCC_except_table358
+ GCC_except_table360
+ GCC_except_table362
+ GCC_except_table364
+ GCC_except_table366
+ GCC_except_table368
+ GCC_except_table370
+ GCC_except_table379
+ GCC_except_table381
+ GCC_except_table385
+ GCC_except_table391
+ GCC_except_table393
+ GCC_except_table397
+ GCC_except_table417
+ GCC_except_table423
+ GCC_except_table450
+ GCC_except_table452
+ GCC_except_table456
+ GCC_except_table458
+ GCC_except_table462
+ GCC_except_table464
+ GCC_except_table479
+ GCC_except_table491
+ GCC_except_table520
+ GCC_except_table525
+ GCC_except_table526
+ GCC_except_table528
+ GCC_except_table530
+ GCC_except_table532
+ GCC_except_table534
+ GCC_except_table536
+ GCC_except_table538
+ GCC_except_table540
+ GCC_except_table541
+ GCC_except_table542
+ GCC_except_table544
+ GCC_except_table546
+ GCC_except_table548
+ GCC_except_table550
+ GCC_except_table553
+ GCC_except_table555
+ GCC_except_table573
+ GCC_except_table577
+ GCC_except_table583
+ GCC_except_table587
+ GCC_except_table617
+ GCC_except_table672
+ GCC_except_table707
+ GCC_except_table782
+ GCC_except_table806
+ GCC_except_table809
+ GCC_except_table891
+ GCC_except_table893
+ GCC_except_table932
+ GCC_except_table943
+ GCC_except_table96
+ GCC_except_table989
+ _CGAffineTransformDecompose
+ _CGAffineTransformMakeWithComponents
+ _OBJC_CLASS_$_AFPreferences
+ _OBJC_CLASS_$_SBHIconImageCacheConfiguration
+ _OBJC_CLASS_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier
+ _OBJC_CLASS_$_SBHiddenWindowsPillMaterializeAnimationSwitcherModifier
+ _OBJC_CLASS_$_SBHiddenWindowsPillPresentAnimationSwitcherModifier
+ _OBJC_CLASS_$_SBHiddenWindowsPillRootSwitcherModifier
+ _OBJC_CLASS_$_SBHiddenWindowsPillSwitcherModifier
+ _OBJC_CLASS_$_SBKeyboardInputSwitcherModifierEvent
+ _OBJC_CLASS_$_SBScreenTimeTrackingController
+ _OBJC_CLASS_$_SBSiriHUDSceneController
+ _OBJC_CLASS_$_SBSwitcherHiddenWindowsPill
+ _OBJC_CLASS_$_SBSwitcherHiddenWindowsPillView
+ _OBJC_CLASS_$_SBTapHiddenWindowsPillSwitcherModifierEvent
+ _OBJC_CLASS_$_SBTransientUIIndirectPanToDismissSwitcherModifierEvent
+ _OBJC_CLASS_$_SBTransientUITapToDismissSwitcherModifierEvent
+ _OBJC_CLASS_$_SiriActivationService
+ _OBJC_CLASS_$_UIFontMetrics
+ _OBJC_CLASS_$__UIMainMenuBaseMenuRequest
+ _OBJC_IVAR_$_SBAssistantSceneController._homeAffordanceDoubleTapGestureEnabled
+ _OBJC_IVAR_$_SBAssistantSceneController._lastKnownInterfaceOrientation
+ _OBJC_IVAR_$_SBContinuousExposeWindowDragDestinationSwitcherModifier._initialSelectedDisplayItemLayoutAttributesOnThisSwitcher
+ _OBJC_IVAR_$_SBEntityRemovalCrossblurSwitcherModifier._removalAppLayout
+ _OBJC_IVAR_$_SBFloatingDockRemoteContentManager._closingFileStackIcon
+ _OBJC_IVAR_$_SBFloatingDockRemoteContentManager._remoteContentOverlayFrame
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._bounceIconViewsForHiddenWindowsPills
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._cachedHiddenWindowsPillHeight
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._hiddenWindowsPillIconPortals
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._hiddenWindowsPills
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._keyboardAttentionAwarenessClient
+ _OBJC_IVAR_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier._hiddenWindowsPill
+ _OBJC_IVAR_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier._iconAppLayout
+ _OBJC_IVAR_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier._iconBounceAnimationPhase
+ _OBJC_IVAR_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier._iconBounceGenerationCount
+ _OBJC_IVAR_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier._iconScaleAnimationPhase
+ _OBJC_IVAR_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier._iconScaleGenerationCount
+ _OBJC_IVAR_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier._pillAnimationPhase
+ _OBJC_IVAR_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier._pillGenerationCount
+ _OBJC_IVAR_$_SBHiddenWindowsPillMaterializeAnimationSwitcherModifier._animationPhase
+ _OBJC_IVAR_$_SBHiddenWindowsPillMaterializeAnimationSwitcherModifier._direction
+ _OBJC_IVAR_$_SBHiddenWindowsPillMaterializeAnimationSwitcherModifier._generationCount
+ _OBJC_IVAR_$_SBHiddenWindowsPillMaterializeAnimationSwitcherModifier._hiddenWindowsPill
+ _OBJC_IVAR_$_SBHiddenWindowsPillPresentAnimationSwitcherModifier._generationCount
+ _OBJC_IVAR_$_SBHiddenWindowsPillPresentAnimationSwitcherModifier._hiddenWindowsPill
+ _OBJC_IVAR_$_SBHiddenWindowsPillPresentAnimationSwitcherModifier._iconAppLayout
+ _OBJC_IVAR_$_SBHiddenWindowsPillPresentAnimationSwitcherModifier._iconFrame
+ _OBJC_IVAR_$_SBHiddenWindowsPillPresentAnimationSwitcherModifier._phase
+ _OBJC_IVAR_$_SBHiddenWindowsPillRootSwitcherModifier._hiddenWindowsPill
+ _OBJC_IVAR_$_SBHiddenWindowsPillRootSwitcherModifier._iconAppLayout
+ _OBJC_IVAR_$_SBHiddenWindowsPillRootSwitcherModifier._isPendingDismissal
+ _OBJC_IVAR_$_SBHiddenWindowsPillRootSwitcherModifier._isPresented
+ _OBJC_IVAR_$_SBHiddenWindowsPillRootSwitcherModifier._toAppLayout
+ _OBJC_IVAR_$_SBHiddenWindowsPillSwitcherModifier._hiddenWindowsPill
+ _OBJC_IVAR_$_SBHiddenWindowsPillSwitcherModifier._iconAppLayout
+ _OBJC_IVAR_$_SBHiddenWindowsPillSwitcherModifier._iconFrame
+ _OBJC_IVAR_$_SBHiddenWindowsPillSwitcherModifier._toAppLayout
+ _OBJC_IVAR_$_SBMainWorkspaceApplicationSceneLayoutElementViewController.groupOpacityRequiredForContentAnimation
+ _OBJC_IVAR_$_SBMenuBarViewController._clientName
+ _OBJC_IVAR_$_SBMixedGridSwitcherModifier._cachedCenterCardFrame
+ _OBJC_IVAR_$_SBMixedGridSwitcherModifier._supportsCenterModalAppLayouts
+ _OBJC_IVAR_$_SBNotificationCarPlayDestination._canActivateSiri
+ _OBJC_IVAR_$_SBNotificationCarPlayDestination._notificationRequestPreprocessed
+ _OBJC_IVAR_$_SBNotificationCarPlayDestination._notificationRequestsPendingPreprocess
+ _OBJC_IVAR_$_SBNotificationCarPlayDestination._preprocessCompleted
+ _OBJC_IVAR_$_SBNotificationCarPlayDestination._preprocessTimeoutTimer
+ _OBJC_IVAR_$_SBNotificationCarPlayDestination._siriNotificationBannerActivationSource
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._alwaysSuppressBacklightChanges
+ _OBJC_IVAR_$_SBSwitcherAnimationAttributes._bouncePositionSettings
+ _OBJC_IVAR_$_SBSwitcherAnimationAttributes._bounceScaleSettings
+ _OBJC_IVAR_$_SBSwitcherAnimationAttributes._pillContentAlphaSettings
+ _OBJC_IVAR_$_SBSwitcherAnimationAttributes._pillContentBlurSettings
+ _OBJC_IVAR_$_SBSwitcherAnimationAttributes._pillContentScaleSettings
+ _OBJC_IVAR_$_SBSwitcherAnimationAttributes._pillMaterializationSettings
+ _OBJC_IVAR_$_SBSwitcherAnimationAttributes._pillOffsetSettings
+ _OBJC_IVAR_$_SBSwitcherAnimationAttributes._pillScaleSettings
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPill._bundleIdentifier
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPill._numberOfHiddenWindows
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._background
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._contentAlpha
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._contentBlurRadius
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._contentScale
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._contentView
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._delegate
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._glassView
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._hiddenWindowsPill
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._imageView
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._maskProgressAnimatableProperty
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._maskView
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._pillMode
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._pillOffset
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._pillScale
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._subtitleLabel
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._tapGestureRecognizer
+ _OBJC_IVAR_$_SBSwitcherHiddenWindowsPillView._titleLabel
+ _OBJC_IVAR_$_SBSwitcherWindowingConfiguration._interfaceOrientation
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimateDismissCenterYSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimateDismissLayoutSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimateDismissScaleSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimateDismissTranslateYSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimatePillContentAlphaSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimatePillContentBlurSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimatePillContentScaleSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimatePillMaterializationSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimatePresentLayoutSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimatePresentOpacitySettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimatePresentPillScaleSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimatePresentPositionSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimatePresentScaleSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimationDelay
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimationInitialScale
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillAnimationStartDelay
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillBounceAnimationMoveDownSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillBounceAnimationMoveUpSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillBounceAnimationScaleSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillIconBounceHeight
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillNoDockOffscreenOffset
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillVerticalOffsetAboveDock
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._hiddenWindowsPillVerticalOffsetNoDock
+ _OBJC_IVAR_$_SBSystemActionCoachingController._focusActivityManager
+ _OBJC_IVAR_$_SBSystemActionCoachingHUDViewController._focusActivityManager
+ _OBJC_IVAR_$_SBSystemUIScenesCoordinator._siriHUDSceneController
+ _OBJC_IVAR_$_SBTapHiddenWindowsPillSwitcherModifierEvent._hiddenWindowsPill
+ _OBJC_IVAR_$_SpringBoard._screenTimeTrackingController
+ _OBJC_METACLASS_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier
+ _OBJC_METACLASS_$_SBHiddenWindowsPillMaterializeAnimationSwitcherModifier
+ _OBJC_METACLASS_$_SBHiddenWindowsPillPresentAnimationSwitcherModifier
+ _OBJC_METACLASS_$_SBHiddenWindowsPillRootSwitcherModifier
+ _OBJC_METACLASS_$_SBHiddenWindowsPillSwitcherModifier
+ _OBJC_METACLASS_$_SBKeyboardInputSwitcherModifierEvent
+ _OBJC_METACLASS_$_SBSiriHUDSceneController
+ _OBJC_METACLASS_$_SBSwitcherHiddenWindowsPill
+ _OBJC_METACLASS_$_SBSwitcherHiddenWindowsPillView
+ _OBJC_METACLASS_$_SBTapHiddenWindowsPillSwitcherModifierEvent
+ _OBJC_METACLASS_$_SBTransientUIIndirectPanToDismissSwitcherModifierEvent
+ _OBJC_METACLASS_$_SBTransientUITapToDismissSwitcherModifierEvent
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _SBFIsHiddenWindowsPillAvailable
+ _SBFloatingDockRemoteContentManagerRemoteContentOverlayFrameDidChangeNotification
+ _SBTraitsParticipantRoleSiriHUD
+ _UIFontTextStyleSubheadline
+ __OBJC_$_CLASS_METHODS_SBSiriHUDSceneController
+ __OBJC_$_INSTANCE_METHODS_SBHiddenWindowsPillDismissAnimationSwitcherModifier
+ __OBJC_$_INSTANCE_METHODS_SBHiddenWindowsPillMaterializeAnimationSwitcherModifier
+ __OBJC_$_INSTANCE_METHODS_SBHiddenWindowsPillPresentAnimationSwitcherModifier
+ __OBJC_$_INSTANCE_METHODS_SBHiddenWindowsPillRootSwitcherModifier
+ __OBJC_$_INSTANCE_METHODS_SBHiddenWindowsPillSwitcherModifier
+ __OBJC_$_INSTANCE_METHODS_SBKeyboardInputSwitcherModifierEvent
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherHiddenWindowsPill
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherHiddenWindowsPillView
+ __OBJC_$_INSTANCE_METHODS_SBTapHiddenWindowsPillSwitcherModifierEvent
+ __OBJC_$_INSTANCE_METHODS_SBTransientUIIndirectPanToDismissSwitcherModifierEvent
+ __OBJC_$_INSTANCE_METHODS_SBTransientUITapToDismissSwitcherModifierEvent
+ __OBJC_$_INSTANCE_VARIABLES_SBHiddenWindowsPillDismissAnimationSwitcherModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBHiddenWindowsPillMaterializeAnimationSwitcherModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBHiddenWindowsPillPresentAnimationSwitcherModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBHiddenWindowsPillRootSwitcherModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBHiddenWindowsPillSwitcherModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBSwitcherHiddenWindowsPill
+ __OBJC_$_INSTANCE_VARIABLES_SBSwitcherHiddenWindowsPillView
+ __OBJC_$_INSTANCE_VARIABLES_SBTapHiddenWindowsPillSwitcherModifierEvent
+ __OBJC_$_PROP_LIST_SBHiddenWindowsPillDismissAnimationSwitcherModifier
+ __OBJC_$_PROP_LIST_SBHiddenWindowsPillMaterializeAnimationSwitcherModifier
+ __OBJC_$_PROP_LIST_SBHiddenWindowsPillPresentAnimationSwitcherModifier
+ __OBJC_$_PROP_LIST_SBHiddenWindowsPillRootSwitcherModifier
+ __OBJC_$_PROP_LIST_SBHiddenWindowsPillSwitcherModifier
+ __OBJC_$_PROP_LIST_SBSwitcherHiddenWindowsPill
+ __OBJC_$_PROP_LIST_SBSwitcherHiddenWindowsPillView
+ __OBJC_$_PROP_LIST_SBTapHiddenWindowsPillSwitcherModifierEvent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SiriDirectActionSourceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSwitcherHiddenWindowsPillViewDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SiriDirectActionSourceDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSwitcherHiddenWindowsPillViewDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SiriDirectActionSourceDelegate
+ __OBJC_$_PROTOCOL_REFS_SBSwitcherHiddenWindowsPillViewDelegate
+ __OBJC_$_PROTOCOL_REFS_SiriDirectActionSourceDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SBSwitcherHiddenWindowsPill
+ __OBJC_CLASS_RO_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier
+ __OBJC_CLASS_RO_$_SBHiddenWindowsPillMaterializeAnimationSwitcherModifier
+ __OBJC_CLASS_RO_$_SBHiddenWindowsPillPresentAnimationSwitcherModifier
+ __OBJC_CLASS_RO_$_SBHiddenWindowsPillRootSwitcherModifier
+ __OBJC_CLASS_RO_$_SBHiddenWindowsPillSwitcherModifier
+ __OBJC_CLASS_RO_$_SBKeyboardInputSwitcherModifierEvent
+ __OBJC_CLASS_RO_$_SBSiriHUDSceneController
+ __OBJC_CLASS_RO_$_SBSwitcherHiddenWindowsPill
+ __OBJC_CLASS_RO_$_SBSwitcherHiddenWindowsPillView
+ __OBJC_CLASS_RO_$_SBTapHiddenWindowsPillSwitcherModifierEvent
+ __OBJC_CLASS_RO_$_SBTransientUIIndirectPanToDismissSwitcherModifierEvent
+ __OBJC_CLASS_RO_$_SBTransientUITapToDismissSwitcherModifierEvent
+ __OBJC_LABEL_PROTOCOL_$_SBSwitcherHiddenWindowsPillViewDelegate
+ __OBJC_LABEL_PROTOCOL_$_SiriDirectActionSourceDelegate
+ __OBJC_METACLASS_RO_$_SBHiddenWindowsPillDismissAnimationSwitcherModifier
+ __OBJC_METACLASS_RO_$_SBHiddenWindowsPillMaterializeAnimationSwitcherModifier
+ __OBJC_METACLASS_RO_$_SBHiddenWindowsPillPresentAnimationSwitcherModifier
+ __OBJC_METACLASS_RO_$_SBHiddenWindowsPillRootSwitcherModifier
+ __OBJC_METACLASS_RO_$_SBHiddenWindowsPillSwitcherModifier
+ __OBJC_METACLASS_RO_$_SBKeyboardInputSwitcherModifierEvent
+ __OBJC_METACLASS_RO_$_SBSiriHUDSceneController
+ __OBJC_METACLASS_RO_$_SBSwitcherHiddenWindowsPill
+ __OBJC_METACLASS_RO_$_SBSwitcherHiddenWindowsPillView
+ __OBJC_METACLASS_RO_$_SBTapHiddenWindowsPillSwitcherModifierEvent
+ __OBJC_METACLASS_RO_$_SBTransientUIIndirectPanToDismissSwitcherModifierEvent
+ __OBJC_METACLASS_RO_$_SBTransientUITapToDismissSwitcherModifierEvent
+ __OBJC_PROTOCOL_$_SBSwitcherHiddenWindowsPillViewDelegate
+ __OBJC_PROTOCOL_$_SiriDirectActionSourceDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_SBSwitcherLayoutElementProviding
+ __ZNSt3__114__split_bufferINS_6vectorI11BezierCurveNS_9allocatorIS2_EEEERNS3_IS5_EEE17__destruct_at_endB9fon210106EPS5_
+ __ZNSt3__114__split_bufferINS_6vectorI9PathPointNS_9allocatorIS2_EEEERNS3_IS5_EEE17__destruct_at_endB9fon210106EPS5_
+ __ZNSt3__119__allocate_at_leastB9fon210106INS_9allocatorI11BezierCurveEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB9fon210106INS_9allocatorI9PathPointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB9fon210106INS_9allocatorINS_6vectorI11BezierCurveNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB9fon210106INS_9allocatorINS_6vectorI9PathPointNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorI11BezierCurveNS_9allocatorIS1_EEE11__vallocateB9fon210106Em
+ __ZNSt3__16vectorI11BezierCurveNS_9allocatorIS1_EEE20__throw_length_errorB9fon210106Ev
+ __ZNSt3__16vectorI11BezierCurveNS_9allocatorIS1_EEEC2B9fon210106ERKS4_
+ __ZNSt3__16vectorI9PathPointNS_9allocatorIS1_EEE20__throw_length_errorB9fon210106Ev
+ __ZNSt3__16vectorINS0_I11BezierCurveNS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB9fon210106Ev
+ __ZNSt3__16vectorINS0_I11BezierCurveNS_9allocatorIS1_EEEENS2_IS4_EEE20__throw_length_errorB9fon210106Ev
+ __ZNSt3__16vectorINS0_I11BezierCurveNS_9allocatorIS1_EEEENS2_IS4_EEE5clearB9fon210106Ev
+ __ZNSt3__16vectorINS0_I9PathPointNS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB9fon210106Ev
+ __ZNSt3__16vectorINS0_I9PathPointNS_9allocatorIS1_EEEENS2_IS4_EEE20__throw_length_errorB9fon210106Ev
+ __ZNSt3__16vectorINS0_I9PathPointNS_9allocatorIS1_EEEENS2_IS4_EEE5clearB9fon210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9fon210106v
+ ___100-[SBContinuousExposeWindowDragDestinationSwitcherModifier _frameForSelectedAppLayout:addingToStage:]_block_invoke
+ ___104-[SBNotificationCarPlayDestination _cancelAnnounceForNotificationRequest:withReason:deactivateAnnounce:]_block_invoke.176
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.707
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.709
+ ___129-[SBHomeScreenService swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:]_block_invoke.174
+ ___37-[SBUIController updateBatteryState:]_block_invoke.231
+ ___37-[SBUIController updateBatteryState:]_block_invoke.239
+ ___37-[SBUIController updateBatteryState:]_block_invoke_2.241
+ ___39-[SBSwitcherHiddenWindowsPill isEqual:]_block_invoke
+ ___39-[SBSwitcherHiddenWindowsPill isEqual:]_block_invoke_2
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1262
+ ___47-[SBRoutingSwitcherModifier hiddenWindowsPills]_block_invoke
+ ___48-[SBSwitcherHiddenWindowsPillView _makeMaskView]_block_invoke
+ ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.93
+ ___53-[SBRoutingSwitcherModifier wantsKeyboardInputEvents]_block_invoke
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.806
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.837
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.868
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.974
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.861
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.978
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.296
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.296.cold.1
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.301
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.301.cold.1
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.304
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.304.cold.1
+ ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.832
+ ___55-[SBRoutingSwitcherModifier alphaForHiddenWindowsPill:]_block_invoke
+ ___56-[SBRoutingSwitcherModifier centerForHiddenWindowsPill:]_block_invoke
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1833
+ ___59-[SBFloatingDockRemoteContentManager iconView:performDrop:]_block_invoke.76
+ ___59-[SBFloatingDockRemoteContentManager iconView:performDrop:]_block_invoke.78
+ ___59-[SBRoutingSwitcherModifier pillScaleForHiddenWindowsPill:]_block_invoke
+ ___59-[SBRoutingSwitcherModifier transformForHiddenWindowsPill:]_block_invoke
+ ___60-[SBNotificationCarPlayDestination _flushPreprocessRequests]_block_invoke
+ ___60-[SBNotificationCarPlayDestination postNotificationRequest:]_block_invoke
+ ___60-[SBRoutingSwitcherModifier backgroundForHiddenWindowsPill:]_block_invoke
+ ___60-[SBRoutingSwitcherModifier pillOffsetForHiddenWindowsPill:]_block_invoke
+ ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.986
+ ___61-[SBNotificationCarPlayDestination _presentBannerForRequest:]_block_invoke
+ ___61-[SBNotificationCarPlayDestination _presentBannerForRequest:]_block_invoke.cold.1
+ ___61-[SBNotificationCarPlayDestination _presentBannerForRequest:]_block_invoke.cold.2
+ ___62-[SBRoutingSwitcherModifier contentAlphaForHiddenWindowsPill:]_block_invoke
+ ___62-[SBRoutingSwitcherModifier contentScaleForHiddenWindowsPill:]_block_invoke
+ ___63-[SBFlexibleWindowingWindowDragSwitcherModifier frameForIndex:]_block_invoke
+ ___63-[SBFluidSwitcherViewController _updateHiddenWindowsPillsViews]_block_invoke
+ ___63-[SBFluidSwitcherViewController _updateHiddenWindowsPillsViews]_block_invoke_2
+ ___63-[SBFluidSwitcherViewController _updateHiddenWindowsPillsViews]_block_invoke_3
+ ___64-[SBNotificationCarPlayDestination _startPreprocessTimeoutTimer]_block_invoke
+ ___64-[SBNotificationCarPlayDestination _startPreprocessTimeoutTimer]_block_invoke.cold.1
+ ___64-[SBUIController _accessoryEndpointAttached:reportToLockScreen:]_block_invoke.294
+ ___65-[SBRoutingSwitcherModifier bounceIconScaleForHiddenWindowsPill:]_block_invoke
+ ___65-[SBUIController fetchFormattedChargeTimeEstimateWithCompletion:]_block_invoke.280
+ ___66-[SBRoutingSwitcherModifier bounceIconCenterForHiddenWindowsPill:]_block_invoke
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.731
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.733
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.734
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.735
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.736
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_2.742
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_3.754
+ ___67-[SBRoutingSwitcherModifier contentBlurRadiusForHiddenWindowsPill:]_block_invoke
+ ___69-[SBFluidSwitcherViewController _layoutHiddenWindowsPill:completion:]_block_invoke
+ ___69-[SBFluidSwitcherViewController _layoutHiddenWindowsPill:completion:]_block_invoke_2
+ ___69-[SBFluidSwitcherViewController _layoutHiddenWindowsPill:completion:]_block_invoke_3
+ ___69-[SBFluidSwitcherViewController _layoutHiddenWindowsPill:completion:]_block_invoke_4
+ ___69-[SBFluidSwitcherViewController _layoutHiddenWindowsPill:completion:]_block_invoke_5
+ ___69-[SBFluidSwitcherViewController _layoutHiddenWindowsPill:completion:]_block_invoke_6
+ ___70-[SBSwitcherHiddenWindowsPillView _makeMaskProgressAnimatableProperty]_block_invoke
+ ___70-[SBSwitcherHiddenWindowsPillView _makeMaskProgressAnimatableProperty]_block_invoke_2
+ ___70-[SBSwitcherHiddenWindowsPillView _makeMaskProgressAnimatableProperty]_block_invoke_3
+ ___70-[SBSwitcherHiddenWindowsPillView _makeMaskProgressAnimatableProperty]_block_invoke_4
+ ___71-[SBRoutingSwitcherModifier hiddenWindowsPillModeForHiddenWindowsPill:]_block_invoke
+ ___71-[SBSwitcherController _buildHideMenuWithAdditionalOptions:clientName:]_block_invoke
+ ___71-[SBWallpaperController fetchAllPosterIconConfigurationsForPrecaching:]_block_invoke
+ ___71-[SBWallpaperController fetchAllPosterIconConfigurationsForPrecaching:]_block_invoke.cold.1
+ ___73-[SBFluidSwitcherViewController _layoutHiddenWindowsPillsWithCompletion:]_block_invoke
+ ___73-[SBRoutingSwitcherModifier shouldBounceIconPresentForHiddenWindowsPill:]_block_invoke
+ ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1186
+ ___75-[SBFluidSwitcherViewController _applyStyleToHiddenWindowsPill:completion:]_block_invoke
+ ___75-[SBFluidSwitcherViewController _applyStyleToHiddenWindowsPill:completion:]_block_invoke_2
+ ___75-[SBFluidSwitcherViewController _applyStyleToHiddenWindowsPill:completion:]_block_invoke_3
+ ___75-[SBFluidSwitcherViewController _applyStyleToHiddenWindowsPill:completion:]_block_invoke_4
+ ___75-[SBFluidSwitcherViewController _applyStyleToHiddenWindowsPill:completion:]_block_invoke_5
+ ___75-[SBFluidSwitcherViewController _applyStyleToHiddenWindowsPill:completion:]_block_invoke_6
+ ___75-[SBNotificationCarPlayDestination _requestAnnounceForNotificationRequest:]_block_invoke.174
+ ___79-[SBFluidSwitcherViewController _applyStyleToHiddenWindowsPillsWithCompletion:]_block_invoke
+ ___79-[SBFluidSwitcherViewController _layoutHiddenWindowsPillBounceIcon:completion:]_block_invoke
+ ___79-[SBFluidSwitcherViewController _layoutHiddenWindowsPillBounceIcon:completion:]_block_invoke_2
+ ___79-[SBFluidSwitcherViewController _layoutHiddenWindowsPillBounceIcon:completion:]_block_invoke_3
+ ___79-[SBNotificationCarPlayDestination didSelectBannerOfPresentableViewController:]_block_invoke.107
+ ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.412
+ ___83-[SBFluidSwitcherViewController performKeyboardShortcutAction:withSceneIdentifier:]_block_invoke_4
+ ___83-[SBFluidSwitcherViewController performKeyboardShortcutAction:withSceneIdentifier:]_block_invoke_5
+ ___83-[SBFluidSwitcherViewController performKeyboardShortcutAction:withSceneIdentifier:]_block_invoke_6
+ ___83-[SBFluidSwitcherViewController performKeyboardShortcutAction:withSceneIdentifier:]_block_invoke_7
+ ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.225
+ ___84-[SBMixedGridSwitcherModifier responseForProposedChildResponse:childModifier:event:]_block_invoke_2
+ ___85-[SBContinuousExposeToHomeSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:]_block_invoke_2
+ ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.89
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1685
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1687
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1689
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1693
+ ___91-[SBFluidSwitcherViewController numberOfOccludedOrOffStageDisplayItemsForBundleIdentifier:]_block_invoke
+ ___93-[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:shouldPreprocess:]_block_invoke
+ ___94-[SBFloatingDockRemoteContentManager clientRequestToUpdateFileStackIcon:preferredDisplayName:]_block_invoke
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1816
+ ___99-[SBHomeScreenController iconManager:extraIconImageCacheConfigurationsForPrecachingWithCompletion:]_block_invoke
+ ___blockIMPFromContextSignature106_block_invoke
+ ___blockIMPFromContextSignature107_block_invoke
+ ___blockIMPFromContextSignature108_block_invoke
+ ___blockIMPFromContextSignature109_block_invoke
+ ___blockIMPFromEventSignature106_block_invoke
+ ___blockIMPFromEventSignature107_block_invoke
+ ___blockIMPFromEventSignature108_block_invoke
+ ___blockIMPFromEventSignature109_block_invoke
+ ___blockIMPFromQuerySignature106_block_invoke
+ ___blockIMPFromQuerySignature107_block_invoke
+ ___blockIMPFromQuerySignature108_block_invoke
+ ___blockIMPFromQuerySignature109_block_invoke
+ ___block_descriptor_184_e8_32s40s48s56s64s72s_e33_v16?0?<?<v?BB>?"NSString">8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_32_e17_16?0"UIColor"8l
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e37_B16?0"SBSwitcherHiddenWindowsPill"8ls32l8
+ ___block_descriptor_40_e8_32s_e75_"SBChainableModifierEventResponse"16?0"SBSwitcherModifierEventResponse"8ls32l8
+ ___block_descriptor_48_e35_32?0"SBChainableModifier"816q24l
+ ___block_descriptor_48_e35_v32?0"SBChainableModifier"816q24l
+ ___block_descriptor_48_e38_v40?0"SBChainableModifier"81624q32l
+ ___block_descriptor_48_e57_{CGAffineTransform=dddddd}24?0"SBChainableModifier"816l
+ ___block_descriptor_48_e8_32bs40w_e37_v16?0"_UIMainMenuBaseMenuResponse"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e28_v32?0"SBAppLayout"8Q16^B24lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e23_v32?0"SBIcon"8Q16^B24ls32l8s40l8
+ ___block_descriptor_50_e8_32s40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_88_e8_32s40s48s_e33_v16?0?<?<v?BB>?"NSString">8ls32l8s40l8s48l8
+ ___block_literal_global.1108
+ ___block_literal_global.1117
+ ___block_literal_global.1153
+ ___block_literal_global.1200
+ ___block_literal_global.1205
+ ___block_literal_global.1208
+ ___block_literal_global.1213
+ ___block_literal_global.1219
+ ___block_literal_global.1512
+ ___block_literal_global.1659
+ ___block_literal_global.1695
+ ___block_literal_global.1704
+ ___block_literal_global.1706
+ ___block_literal_global.1708
+ ___block_literal_global.1710
+ ___block_literal_global.1726
+ ___block_literal_global.1842
+ ___block_literal_global.1865
+ ___block_literal_global.1874
+ ___block_literal_global.1890
+ ___block_literal_global.290
+ ___block_literal_global.303
+ ___block_literal_global.517
+ ___block_literal_global.521
+ ___block_literal_global.524
+ ___block_literal_global.530
+ ___block_literal_global.533
+ ___block_literal_global.593
+ ___block_literal_global.598
+ ___block_literal_global.603
+ ___block_literal_global.605
+ ___block_literal_global.607
+ ___block_literal_global.609
+ ___block_literal_global.611
+ ___block_literal_global.613
+ ___block_literal_global.62
+ ___block_literal_global.626
+ ___block_literal_global.628
+ ___block_literal_global.634
+ ___block_literal_global.684
+ ___block_literal_global.688
+ ___block_literal_global.690
+ ___block_literal_global.712
+ ___block_literal_global.728
+ ___block_literal_global.738
+ ___block_literal_global.739
+ ___block_literal_global.744
+ ___block_literal_global.745
+ ___block_literal_global.779
+ ___block_literal_global.805
+ ___block_literal_global.833
+ ___block_literal_global.864
+ ___block_literal_global.870
+ ___block_literal_global.894
+ ___block_literal_global.904
+ ___block_literal_global.940
+ ___block_literal_global.944
+ ___block_literal_global.946
+ ___block_literal_global.950
+ ___block_literal_global.956
+ ___block_literal_global.958
+ ___block_literal_global.962
+ ___block_literal_global.964
+ ___block_literal_global.968
+ ___block_literal_global.970
+ ___block_literal_global.974
+ ___block_literal_global.976
+ ___block_literal_global.980
+ ___block_literal_global.988
+ _blockIMPFromContextSignature106
+ _blockIMPFromContextSignature107
+ _blockIMPFromContextSignature108
+ _blockIMPFromContextSignature109
+ _blockIMPFromEventSignature106
+ _blockIMPFromEventSignature107
+ _blockIMPFromEventSignature108
+ _blockIMPFromEventSignature109
+ _blockIMPFromQuerySignature106
+ _blockIMPFromQuerySignature107
+ _blockIMPFromQuerySignature108
+ _blockIMPFromQuerySignature109
+ _objc_msgSend$_applyStyleToHiddenWindowsPill:completion:
+ _objc_msgSend$_applyStyleToHiddenWindowsPillsWithCompletion:
+ _objc_msgSend$_beginObservingLayoutStateTransitionsIfNeeded
+ _objc_msgSend$_buildHideMenuWithAdditionalOptions:clientName:
+ _objc_msgSend$_cachedCenterCardFrame
+ _objc_msgSend$_cancelCurrentPreprocessedSiriSession
+ _objc_msgSend$_clearCurrentPreprocessRequest
+ _objc_msgSend$_currentLayoutAttributesOrientationForSwitcherCorrespondingToDisplayOrdinal:
+ _objc_msgSend$_disablesHomeAffordanceDoubleTapGestureInLandscape
+ _objc_msgSend$_dismissalTransitionRequest
+ _objc_msgSend$_effectiveGlassViewMaterial
+ _objc_msgSend$_endObservingLayoutStateTransitionsIfNeeded
+ _objc_msgSend$_floatingDockIconViewForDisplayItem:isVisible:
+ _objc_msgSend$_flushPreprocessRequests
+ _objc_msgSend$_hasRequestPreprocessed
+ _objc_msgSend$_hasRequestPreprocessing
+ _objc_msgSend$_hitTestedToTransientUIAtLocation:window:
+ _objc_msgSend$_iconImageCacheConfigurationFromPosterIconConfiguration:
+ _objc_msgSend$_invalidatePreprocessTimeoutTimer
+ _objc_msgSend$_isIndexFullScreenOrCenterModal:
+ _objc_msgSend$_lastKnownInterfaceOrientationIsLandscape
+ _objc_msgSend$_layoutAttributesForDisplayItem:displayOrdinal:orientation:
+ _objc_msgSend$_layoutHiddenWindowsPill:completion:
+ _objc_msgSend$_layoutHiddenWindowsPillBounceIcon:completion:
+ _objc_msgSend$_layoutHiddenWindowsPillsWithCompletion:
+ _objc_msgSend$_makeContentView
+ _objc_msgSend$_makeGlass
+ _objc_msgSend$_makeGlassView
+ _objc_msgSend$_makeImageView
+ _objc_msgSend$_makeMaskProgressAnimatableProperty
+ _objc_msgSend$_makeMaskView
+ _objc_msgSend$_makeTitleLabel
+ _objc_msgSend$_notifiesAssistantOfApplicationTransitions
+ _objc_msgSend$_postNotificationRequest:shouldAnnounce:shouldPreprocess:
+ _objc_msgSend$_preprocessNotificationRequest:
+ _objc_msgSend$_presentBannerForRequest:
+ _objc_msgSend$_processNextPreprocessRequest
+ _objc_msgSend$_reevaluateHomeAffordanceDoubleTapGestureEnablement
+ _objc_msgSend$_requestPreprocessForNotificationRequest:
+ _objc_msgSend$_setHomeAffordanceDoubleTapGestureEnabled:withReason:
+ _objc_msgSend$_shouldDematerialize
+ _objc_msgSend$_shouldMaterialize
+ _objc_msgSend$_shouldPreprocessNotificationRequest:
+ _objc_msgSend$_shouldShowAlertForSeed
+ _objc_msgSend$_startPreprocessTimeoutTimer
+ _objc_msgSend$_updateHiddenWindowsPillsViews
+ _objc_msgSend$_updateKeyboardAttentionAwarenessClient
+ _objc_msgSend$_updateRemoteContentOverlayFrame:
+ _objc_msgSend$_visibleDisplayItemsForBundleIdentifier:
+ _objc_msgSend$_willDockBeVisibleAtEndOfTransition
+ _objc_msgSend$addFileStackWithURL:preferredDisplayName:
+ _objc_msgSend$alphaForHiddenWindowsPill:
+ _objc_msgSend$backgroundForHiddenWindowsPill:
+ _objc_msgSend$bounceIconCenterForHiddenWindowsPill:
+ _objc_msgSend$bounceIconScaleForHiddenWindowsPill:
+ _objc_msgSend$bouncePositionSettings
+ _objc_msgSend$bounceScaleSettings
+ _objc_msgSend$centerForHiddenWindowsPill:
+ _objc_msgSend$clientName
+ _objc_msgSend$closingFileStackIcon
+ _objc_msgSend$contentAlphaForHiddenWindowsPill:
+ _objc_msgSend$contentBlurRadiusForHiddenWindowsPill:
+ _objc_msgSend$contentScaleForHiddenWindowsPill:
+ _objc_msgSend$deactivationRequest:
+ _objc_msgSend$dummyAppLayoutWithBundleIdentifier:sceneIdentifier:
+ _objc_msgSend$fetchAllPosterIconConfigurationsForPrecaching:
+ _objc_msgSend$fetchLockScreenHomeScreenColorConfigurations:
+ _objc_msgSend$floatingDockIconFrameForAppLayout:
+ _objc_msgSend$floatingDockIconImageFrameForAppLayout:
+ _objc_msgSend$floatingDockIconScaleForAppLayout:
+ _objc_msgSend$floatingDockIconViewForAppLayout:
+ _objc_msgSend$getAnnounceNotificationsInCarPlayTemporarilyDisabledWithCompletion:
+ _objc_msgSend$groupOpacityRequiredForContentAnimation
+ _objc_msgSend$groupOpacityRequiredWhenRemovingItemContainerForLeafAppLayout:
+ _objc_msgSend$handleKeyboardInputEvent:
+ _objc_msgSend$handleTapHiddenWindowsPill:
+ _objc_msgSend$handleTransientUIIndirectPannedToDismissSwitcherModifierEvent:
+ _objc_msgSend$handleTransientUITapToDismissSwitcherModifierEvent:
+ _objc_msgSend$hiddenWindowsPill
+ _objc_msgSend$hiddenWindowsPillAnimateDismissCenterYSettings
+ _objc_msgSend$hiddenWindowsPillAnimateDismissLayoutSettings
+ _objc_msgSend$hiddenWindowsPillAnimateDismissScaleSettings
+ _objc_msgSend$hiddenWindowsPillAnimateDismissTranslateYSettings
+ _objc_msgSend$hiddenWindowsPillAnimatePillContentAlphaSettings
+ _objc_msgSend$hiddenWindowsPillAnimatePillContentBlurSettings
+ _objc_msgSend$hiddenWindowsPillAnimatePillContentScaleSettings
+ _objc_msgSend$hiddenWindowsPillAnimatePillMaterializationSettings
+ _objc_msgSend$hiddenWindowsPillAnimatePresentLayoutSettings
+ _objc_msgSend$hiddenWindowsPillAnimatePresentOpacitySettings
+ _objc_msgSend$hiddenWindowsPillAnimatePresentPillScaleSettings
+ _objc_msgSend$hiddenWindowsPillAnimatePresentPositionSettings
+ _objc_msgSend$hiddenWindowsPillAnimatePresentScaleSettings
+ _objc_msgSend$hiddenWindowsPillAnimationDelay
+ _objc_msgSend$hiddenWindowsPillAnimationInitialScale
+ _objc_msgSend$hiddenWindowsPillAnimationStartDelay
+ _objc_msgSend$hiddenWindowsPillBounceAnimationMoveDownSettings
+ _objc_msgSend$hiddenWindowsPillBounceAnimationMoveUpSettings
+ _objc_msgSend$hiddenWindowsPillBounceAnimationScaleSettings
+ _objc_msgSend$hiddenWindowsPillHeight
+ _objc_msgSend$hiddenWindowsPillIconBounceHeight
+ _objc_msgSend$hiddenWindowsPillModeForHiddenWindowsPill:
+ _objc_msgSend$hiddenWindowsPillModifierForTransitionEvent:
+ _objc_msgSend$hiddenWindowsPillNoDockOffscreenOffset
+ _objc_msgSend$hiddenWindowsPillVerticalOffsetAboveDock
+ _objc_msgSend$hiddenWindowsPillVerticalOffsetNoDock
+ _objc_msgSend$hiddenWindowsPillViewWasTapped:
+ _objc_msgSend$hiddenWindowsPills
+ _objc_msgSend$hideMenuWithOptions:clientName:
+ _objc_msgSend$initWithBundleIdentifier:numberOfHiddenWindows:
+ _objc_msgSend$initWithDeactivationOptions:animated:requestCancellationReason:dismissalReason:shouldTurnScreenOff:
+ _objc_msgSend$initWithHiddenWindowsPill:
+ _objc_msgSend$initWithHiddenWindowsPill:delegate:
+ _objc_msgSend$initWithHiddenWindowsPill:direction:
+ _objc_msgSend$initWithStyleConfiguration:iconSize:
+ _objc_msgSend$initWithTransitionID:appLayout:layoutRole:multitaskingModifier:
+ _objc_msgSend$initWithUNNotification:preprocess:
+ _objc_msgSend$isHiddenWindowsPillSupported
+ _objc_msgSend$isHiddenWindowsPillSupportedForSwitcherContentController:
+ _objc_msgSend$isObservingLayoutStateTransitions
+ _objc_msgSend$lastKnownInterfaceOrientation
+ _objc_msgSend$layoutAttributesForDisplayItem:
+ _objc_msgSend$layoutAttributesForDisplayItem:displayOrdinal:
+ _objc_msgSend$layoutAttributesForDisplayItem:displayOrdinal:orientation:
+ _objc_msgSend$numberOfHiddenWindows
+ _objc_msgSend$numberOfOccludedOrOffStageDisplayItemsForBundleIdentifier:
+ _objc_msgSend$performBaseMenuRequest:responseHandler:
+ _objc_msgSend$pillContentAlphaSettings
+ _objc_msgSend$pillContentBlurSettings
+ _objc_msgSend$pillContentScaleSettings
+ _objc_msgSend$pillMaterializationSettings
+ _objc_msgSend$pillOffsetForHiddenWindowsPill:
+ _objc_msgSend$pillOffsetSettings
+ _objc_msgSend$pillScaleForHiddenWindowsPill:
+ _objc_msgSend$pillScaleSettings
+ _objc_msgSend$removeFirstObject
+ _objc_msgSend$scaledValueForValue:
+ _objc_msgSend$setAdjustsImageSizeForAccessibilityContentSizeCategory:
+ _objc_msgSend$setAlwaysSuppressBacklightChanges:
+ _objc_msgSend$setBouncePositionSettings:
+ _objc_msgSend$setBounceScaleSettings:
+ _objc_msgSend$setClientName:
+ _objc_msgSend$setContentBlurRadius:
+ _objc_msgSend$setFlexible:
+ _objc_msgSend$setHiddenWindowsPillAnimationDelay:
+ _objc_msgSend$setHiddenWindowsPillAnimationInitialScale:
+ _objc_msgSend$setHiddenWindowsPillAnimationStartDelay:
+ _objc_msgSend$setHiddenWindowsPillIconBounceHeight:
+ _objc_msgSend$setHiddenWindowsPillNoDockOffscreenOffset:
+ _objc_msgSend$setHiddenWindowsPillVerticalOffsetAboveDock:
+ _objc_msgSend$setHiddenWindowsPillVerticalOffsetNoDock:
+ _objc_msgSend$setLastKnownInterfaceOrientation:
+ _objc_msgSend$setObservingLayoutStateTransitions:
+ _objc_msgSend$setPillContentAlphaSettings:
+ _objc_msgSend$setPillContentBlurSettings:
+ _objc_msgSend$setPillContentScaleSettings:
+ _objc_msgSend$setPillMaterializationSettings:
+ _objc_msgSend$setPillMode:
+ _objc_msgSend$setPillOffset:
+ _objc_msgSend$setPillOffsetSettings:
+ _objc_msgSend$setPillScale:
+ _objc_msgSend$setPillScaleSettings:
+ _objc_msgSend$setPreferredDisplayName:
+ _objc_msgSend$setSupportsCenterModalAppLayouts:
+ _objc_msgSend$sharedPreferences
+ _objc_msgSend$shouldBounceIconPresentForHiddenWindowsPill:
+ _objc_msgSend$startObservingAllNotifications
+ _objc_msgSend$stopObservingAllNotifications
+ _objc_msgSend$supportsCenterModalAppLayouts
+ _objc_msgSend$systemHideMenuWithOptions:clientName:
+ _objc_msgSend$transformForHiddenWindowsPill:
+ _objc_msgSend$updateLayoutAttributes:ofDisplayItem:displayOrdinal:
+ _objc_msgSend$updateLayoutAttributesMap:forDisplayOrdinal:
+ _objc_msgSend$updateLayoutAttributesMap:forDisplayOrdinal:orientation:
+ _objc_msgSend$updatePropertiesIfNeeded
+ _objc_msgSend$wantsKeyboardInputEvents
- +[SBDeviceEmulationController applicationInitializationContext]
- +[SBDeviceEmulationController deviceContext]
- +[SBDeviceEmulationController displayContext]
- -[SBApplication isDefaultWebBrowser]
- -[SBApplication(Classic_Internal) _calculateSupportedTypesLazilyIfNecessary].cold.1
- -[SBDisplayItemLayoutAttributesProvider _layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:]
- -[SBDisplayItemLayoutAttributesProvider layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:]
- -[SBDisplayItemLayoutAttributesProvider layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:].cold.1
- -[SBDisplayItemLayoutAttributesProvider updateLayoutAttributesMap:forAppLayout:displayOrdinal:orientation:]
- -[SBEntityRemovalCrossblurSwitcherModifier initWithTransitionID:appLayout:multitaskingModifier:]
- -[SBFloatingDockRemoteContentManager isContentReady]
- -[SBFloatingDockRemoteContentManager isRemoteViewVisible]
- -[SBFloatingDockRemoteContentManager setContentReady:]
- -[SBFloatingDockRemoteContentManager setRemoteViewVisible:]
- -[SBFluidSwitcherViewController isPartiallyOffscreenWindowsEnabled]
- -[SBFluidSwitcherViewController layoutAttributesForDisplayItem:inAppLayout:]
- -[SBFluidSwitcherViewController updateLayoutAttributesMap:forAppLayout:]
- -[SBHomeScreenService addFileStackWithURL:].cold.1
- -[SBMainDisplayConfigurationTransformer transformDisplayConfiguration:].cold.2
- -[SBMenuBarManager systemHideMenuWithOptions:]
- -[SBMixedGridSwitcherModifier _isIndexFullScreen:]
- -[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:]
- -[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:].cold.1
- -[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:].cold.2
- -[SBRootSceneWindow .cxx_destruct]
- -[SBRootSceneWindow _configureRootLayer:sceneTransformLayer:transformLayer:]
- -[SBRootSceneWindow _updateRootLayerBackgroundColor]
- -[SBRootSceneWindow backgroundColor]
- -[SBRootSceneWindow bezelLayer]
- -[SBRootSceneWindow initWithDisplayConfiguration:]
- -[SBRootSceneWindow layerForBackgroundColor]
- -[SBRootSceneWindow maskLayer]
- -[SBRootSceneWindow traitCollectionDidChange:]
- -[SBSwitcherController _buildHideMenuWithAdditionalOptions:]
- -[SBSwitcherController hideMenuWithOptions:]
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:bannerManager:]
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:bannerManager:].cold.1
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:bannerManager:].cold.2
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:bannerManager:].cold.3
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:bannerManager:].cold.4
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:bannerManager:].cold.5
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:bannerManager:].cold.6
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:bannerManager:].cold.7
- -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:]
- -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.1
- -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.2
- -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.3
- -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.4
- -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.5
- -[SBSystemActionControl performSelectedActionFromSource:withContext:].cold.4
- -[SBTopAffordanceViewController _createAlphaAnimatableProperty]
- -[UISMutableApplicationInitializationContext(DeviceEmulation) sb_configureForDeviceEmulation]
- -[UISMutableDeviceContext(DeviceEmulation) sb_configureForDeviceEmulation]
- -[UISMutableDisplayContext(DeviceEmulation) sb_configureForDeviceEmulation]
- GCC_except_table1001
- GCC_except_table1003
- GCC_except_table1005
- GCC_except_table108
- GCC_except_table173
- GCC_except_table217
- GCC_except_table221
- GCC_except_table223
- GCC_except_table240
- GCC_except_table261
- GCC_except_table271
- GCC_except_table273
- GCC_except_table277
- GCC_except_table292
- GCC_except_table298
- GCC_except_table300
- GCC_except_table317
- GCC_except_table327
- GCC_except_table334
- GCC_except_table344
- GCC_except_table346
- GCC_except_table351
- GCC_except_table355
- GCC_except_table357
- GCC_except_table361
- GCC_except_table367
- GCC_except_table369
- GCC_except_table380
- GCC_except_table396
- GCC_except_table398
- GCC_except_table410
- GCC_except_table416
- GCC_except_table418
- GCC_except_table422
- GCC_except_table424
- GCC_except_table425
- GCC_except_table451
- GCC_except_table457
- GCC_except_table463
- GCC_except_table472
- GCC_except_table473
- GCC_except_table478
- GCC_except_table480
- GCC_except_table484
- GCC_except_table486
- GCC_except_table490
- GCC_except_table501
- GCC_except_table529
- GCC_except_table531
- GCC_except_table537
- GCC_except_table547
- GCC_except_table551
- GCC_except_table561
- GCC_except_table586
- GCC_except_table632
- GCC_except_table667
- GCC_except_table740
- GCC_except_table764
- GCC_except_table767
- GCC_except_table808
- GCC_except_table848
- GCC_except_table889
- GCC_except_table900
- GCC_except_table946
- GCC_except_table986
- GCC_except_table993
- GCC_except_table995
- GCC_except_table997
- GCC_except_table999
- _FBSDisplayRotationFromRadians
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_SBDeviceEmulationController
- _OBJC_IVAR_$_SBContinuousExposeWindowDragDestinationSwitcherModifier._initialSelectedDisplayItemLayoutAttributes
- _OBJC_IVAR_$_SBContinuousExposeWindowDragDestinationSwitcherModifier._shouldConstrainToBottomEdge
- _OBJC_IVAR_$_SBContinuousExposeWindowDragDestinationSwitcherModifier._shouldConstrainToLeftEdge
- _OBJC_IVAR_$_SBContinuousExposeWindowDragDestinationSwitcherModifier._shouldConstrainToRightEdge
- _OBJC_IVAR_$_SBFloatingDockRemoteContentManager._contentReady
- _OBJC_IVAR_$_SBFloatingDockRemoteContentManager._remoteViewVisible
- _OBJC_IVAR_$_SBRootSceneWindow._backgroundColor
- _OBJC_IVAR_$_SBRootSceneWindow._bezelLayer
- _OBJC_IVAR_$_SBRootSceneWindow._layerForBackgroundColor
- _OBJC_IVAR_$_SBRootSceneWindow._maskLayer
- _OBJC_IVAR_$_SBTopAffordanceViewController._alphaAnimatableProperty
- _OBJC_METACLASS_$_SBDeviceEmulationController
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableApplicationInitializationContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDeviceContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDisplayContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_UISMutableApplicationInitializationContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_UISMutableDeviceContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_UISMutableDisplayContext_$_DeviceEmulation
- __OBJC_$_CLASS_METHODS_SBDeviceEmulationController
- __OBJC_$_CLASS_PROP_LIST_SBDeviceEmulationController
- __OBJC_$_INSTANCE_METHODS_SBRootSceneWindow
- __OBJC_$_INSTANCE_VARIABLES_SBRootSceneWindow
- __OBJC_$_PROP_LIST_SBRootSceneWindow
- __OBJC_CLASS_RO_$_SBDeviceEmulationController
- __OBJC_METACLASS_RO_$_SBDeviceEmulationController
- __ZNSt3__114__split_bufferINS_6vectorI11BezierCurveNS_9allocatorIS2_EEEERNS3_IS5_EEE17__destruct_at_endB8nn200100EPS5_
- __ZNSt3__114__split_bufferINS_6vectorI9PathPointNS_9allocatorIS2_EEEERNS3_IS5_EEE17__destruct_at_endB8nn200100EPS5_
- __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI11BezierCurveEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI9PathPointEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_6vectorI11BezierCurveNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_6vectorI9PathPointNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__16vectorI11BezierCurveNS_9allocatorIS1_EEE11__vallocateB8nn200100Em
- __ZNSt3__16vectorI11BezierCurveNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorI11BezierCurveNS_9allocatorIS1_EEEC2B8nn200100ERKS4_
- __ZNSt3__16vectorI9PathPointNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorINS0_I11BezierCurveNS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB8nn200100Ev
- __ZNSt3__16vectorINS0_I11BezierCurveNS_9allocatorIS1_EEEENS2_IS4_EEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorINS0_I11BezierCurveNS_9allocatorIS1_EEEENS2_IS4_EEE5clearB8nn200100Ev
- __ZNSt3__16vectorINS0_I9PathPointNS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB8nn200100Ev
- __ZNSt3__16vectorINS0_I9PathPointNS_9allocatorIS1_EEEENS2_IS4_EEE20__throw_length_errorB8nn200100Ev
- __ZNSt3__16vectorINS0_I9PathPointNS_9allocatorIS1_EEEENS2_IS4_EEE5clearB8nn200100Ev
- __ZSt28__throw_bad_array_new_lengthB8nn200100v
- ___104-[SBNotificationCarPlayDestination _cancelAnnounceForNotificationRequest:withReason:deactivateAnnounce:]_block_invoke.159
- ___107-[SBAbstractWindowSceneDelegate windowScene:didUpdateCoordinateSpace:interfaceOrientation:traitCollection:]_block_invoke
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.668
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.670
- ___129-[SBHomeScreenService swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:]_block_invoke.172
- ___37-[SBUIController updateBatteryState:]_block_invoke.230
- ___37-[SBUIController updateBatteryState:]_block_invoke.238
- ___37-[SBUIController updateBatteryState:]_block_invoke_2.240
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1219
- ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.92
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.763
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.794
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.825
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.931
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.818
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.935
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.295
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.295.cold.1
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.299
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.300.cold.1
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.303
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.303.cold.1
- ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.794
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1790
- ___58-[SBFocusActivityManager toggleActivityPickerPresentation]_block_invoke
- ___59-[SBFloatingDockRemoteContentManager iconView:performDrop:]_block_invoke.73
- ___59-[SBFloatingDockRemoteContentManager iconView:performDrop:]_block_invoke.75
- ___60-[SBSwitcherController _buildHideMenuWithAdditionalOptions:]_block_invoke
- ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.947
- ___63-[SBTopAffordanceViewController _createAlphaAnimatableProperty]_block_invoke
- ___64-[SBUIController _accessoryEndpointAttached:reportToLockScreen:]_block_invoke.293
- ___65-[SBUIController fetchFormattedChargeTimeEstimateWithCompletion:]_block_invoke.279
- ___66-[SBFlexibleWindowingWindowDragSwitcherModifier handleTimerEvent:]_block_invoke
- ___66-[SBSceneLayoutWorkspaceTransaction _prepareScenesForSceneUpdates]_block_invoke
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.690
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.692
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.693
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.694
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.695
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_2.701
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_3.713
- ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1117
- ___75-[SBNotificationCarPlayDestination _requestAnnounceForNotificationRequest:]_block_invoke.157
- ___76-[SBNotificationCarPlayDestination _postNotificationRequest:shouldAnnounce:]_block_invoke
- ___79-[SBNotificationCarPlayDestination didSelectBannerOfPresentableViewController:]_block_invoke.104
- ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.370
- ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.223
- ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.88
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1642
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1644
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1646
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1650
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1773
- ___block_descriptor_48_e8_32bs40w_e21_v16?0"_UIMainMenu"8lw40l8s32l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e30_v32?0q8"SBDisplayItem"16^B24ls32l8s40l8s48l8s56l8r64l8
- ___block_literal_global.1065
- ___block_literal_global.1074
- ___block_literal_global.1110
- ___block_literal_global.1131
- ___block_literal_global.1162
- ___block_literal_global.1165
- ___block_literal_global.1170
- ___block_literal_global.1176
- ___block_literal_global.1469
- ___block_literal_global.1616
- ___block_literal_global.1620
- ___block_literal_global.1652
- ___block_literal_global.1661
- ___block_literal_global.1665
- ___block_literal_global.1667
- ___block_literal_global.1683
- ___block_literal_global.170
- ___block_literal_global.1799
- ___block_literal_global.1822
- ___block_literal_global.1831
- ___block_literal_global.1847
- ___block_literal_global.206
- ___block_literal_global.291
- ___block_literal_global.294
- ___block_literal_global.296
- ___block_literal_global.302
- ___block_literal_global.305
- ___block_literal_global.510
- ___block_literal_global.519
- ___block_literal_global.522
- ___block_literal_global.554
- ___block_literal_global.589
- ___block_literal_global.595
- ___block_literal_global.600
- ___block_literal_global.602
- ___block_literal_global.604
- ___block_literal_global.606
- ___block_literal_global.608
- ___block_literal_global.610
- ___block_literal_global.612
- ___block_literal_global.625
- ___block_literal_global.645
- ___block_literal_global.646
- ___block_literal_global.648
- ___block_literal_global.651
- ___block_literal_global.673
- ___block_literal_global.697
- ___block_literal_global.700
- ___block_literal_global.703
- ___block_literal_global.706
- ___block_literal_global.741
- ___block_literal_global.767
- ___block_literal_global.794
- ___block_literal_global.821
- ___block_literal_global.831
- ___block_literal_global.855
- ___block_literal_global.865
- ___block_literal_global.896
- ___block_literal_global.901
- ___block_literal_global.905
- ___block_literal_global.911
- ___block_literal_global.913
- ___block_literal_global.917
- ___block_literal_global.919
- ___block_literal_global.923
- ___block_literal_global.925
- ___block_literal_global.929
- ___block_literal_global.931
- ___block_literal_global.937
- ___block_literal_global.941
- ___block_literal_global.949
- _colorForSpecifierString
- _mean_tetragon_orientation
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_buildHideMenuWithAdditionalOptions:
- _objc_msgSend$_createAlphaAnimatableProperty
- _objc_msgSend$_isIndexFullScreen:
- _objc_msgSend$_layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:
- _objc_msgSend$_postNotificationRequest:shouldAnnounce:
- _objc_msgSend$_updateRootLayerBackgroundColor
- _objc_msgSend$_updateTransformLayer
- _objc_msgSend$appLayoutForSwitcherContentControllerCorrespondingToDisplayOrdinal:
- _objc_msgSend$customScaleFactorX
- _objc_msgSend$customScaleFactorY
- _objc_msgSend$customTranslationOffsetX
- _objc_msgSend$customTranslationOffsetY
- _objc_msgSend$defaultApplicationForCategory:error:
- _objc_msgSend$deviceContext
- _objc_msgSend$displayContext
- _objc_msgSend$emulatedDeviceBezelImageName
- _objc_msgSend$emulatedDeviceBounds
- _objc_msgSend$emulatedDeviceClass
- _objc_msgSend$emulatedDeviceImageContainingBundle
- _objc_msgSend$emulatedDeviceMaskImageName
- _objc_msgSend$emulatedDisplayCornerRadius
- _objc_msgSend$emulatedHomeButtonType
- _objc_msgSend$getBaseMainMenu:
- _objc_msgSend$hasDifferentColorAppearanceComparedToTraitCollection:
- _objc_msgSend$hasEmulatedDeviceBounds
- _objc_msgSend$hideMenuWithOptions:
- _objc_msgSend$initWithTransitionID:appLayout:multitaskingModifier:
- _objc_msgSend$insertSublayer:below:
- _objc_msgSend$isDefaultWebBrowser
- _objc_msgSend$isEmulatedDevice
- _objc_msgSend$isPartiallyOffscreenWindowsEnabled
- _objc_msgSend$isRemoteViewVisible
- _objc_msgSend$layoutAttributesForDisplayItem:inAppLayout:
- _objc_msgSend$layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:
- _objc_msgSend$renderingCenter
- _objc_msgSend$rootLayerBackgroundColorString
- _objc_msgSend$sb_configureForDeviceEmulation
- _objc_msgSend$scalingStyle
- _objc_msgSend$setContentReady:
- _objc_msgSend$setDeviceContext:
- _objc_msgSend$setDisplayContext:
- _objc_msgSend$setRemoteViewVisible:
- _objc_msgSend$systemHideMenuWithOptions:
- _objc_msgSend$updateLayoutAttributesMap:forAppLayout:
- _objc_msgSend$updateLayoutAttributesMap:forAppLayout:displayOrdinal:orientation:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x7
- _sscanf
CStrings:
+ "#PreprocessNotification #AnnounceNotification CarPlay Requesting to post presentable: %{public}@"
+ "#PreprocessNotification CarPlay cancelling preprocess timeout timer"
+ "#PreprocessNotification CarPlay cancelling preprocessed Siri session for notification request %{public}@"
+ "#PreprocessNotification CarPlay notification request %{public}@ preprocessed. Presenting banner."
+ "#PreprocessNotification CarPlay requesting preprocessing for notification request %{public}@"
+ "#PreprocessNotification CarPlay starting preprocess timeout timer"
+ "#PreprocessNotification Flushing notification requests pending preprocessing."
+ "#PreprocessNotification No notification requests to preprocess"
+ "#PreprocessNotification Posting next queued up preprocess request"
+ "#PreprocessNotification Preprocessed notification %{public}@ finished"
+ "#PreprocessNotification Siri became available for activation while preprocessing. Putting request back in queue."
+ "#PreprocessNotification Siri is no longer available for activation."
+ "#PreprocessNotification Siri is now available for activation. Processing next preprocess request if needed."
+ "#PreprocessNotification Siri not available for activation. Queuing up notification %{public}@ for later preprocessing. Requests in queue: %lu"
+ "#PreprocessNotification Siri preprocessing notification request %{public}@ finished"
+ "#PreprocessNotification Starting preprocess of notification request %{public}@"
+ "#PreprocessNotification Timed out for preprocess to start for notification request: %{public}@."
+ "#PreprocessNotification User didn't interact with the banner for notification request %{public}@, deactivating Siri."
+ "-[SBDisplayItemLayoutAttributesProvider layoutAttributesForDisplayItem:displayOrdinal:orientation:]"
+ "-[SBHomeScreenService addFileStackWithURL:preferredDisplayName:]"
+ "-[SBHomeScreenService isWallpaperDimmed]"
+ "/AppleInternal/Library/BuildRoots/4~CIiIugCnJXU-d0VAnkCM3PoVA1jM58HgzQfq7W4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "@\"<SBSwitcherHiddenWindowsPillViewDelegate>\""
+ "@\"SBDisplayItemLayoutAttributes\"24@0:8@\"SBDisplayItem\"16"
+ "@\"SBDisplayItemLayoutAttributes\"32@0:8@\"SBDisplayItem\"16q24"
+ "@\"SBDisplayItemLayoutAttributes\"40@0:8@\"SBDisplayItem\"16q24q32"
+ "@\"SBGradientView\""
+ "@\"SBHFileStackIcon\""
+ "@\"SBScreenTimeTrackingController\""
+ "@\"SBSiriHUDSceneController\""
+ "@\"SBSwitcherHiddenWindowsPill\""
+ "@\"SiriDirectActionSource\""
+ "@\"UIMenu\"32@0:8Q16@\"NSString\"24"
+ "@16@?0@\"UIColor\"8"
+ "@32@?0@\"SBChainableModifier\"8@16q24"
+ "@48@0:8@16@24q32@40"
+ "A2"
+ "Adding unique extra cache configuration %@"
+ "Always Suppress Backlight Changes"
+ "Animation Delay"
+ "Animation Modifier"
+ "B16@?0@\"SBSwitcherHiddenWindowsPill\"8"
+ "B24@0:8@\"SBSwitcherHiddenWindowsPill\"16"
+ "Bounce Animation Move Down Settings"
+ "Bounce Animation Move Up Settings"
+ "Bounce Animation Scale Settings"
+ "CarPlay setting up deferred announce deactivation for %{public}@ on announce finish since this is the last notification to be announced"
+ "CarPlay withdrawing currently announcing notification request %{public}@ as it is starting announce for request %{public}@"
+ "CarPlay withdrawing notification request %{public}@ on announce finish while pending other announce notifications"
+ "Client finished closing animation."
+ "Client finished opening animation."
+ "Dismiss Center Y Settings"
+ "Dismiss Layout Settings"
+ "Dismiss Phase 3 Position Settings"
+ "Dismiss Scale Settings"
+ "Error fetching lock screen home screen icon configurations %@"
+ "Fetched %lu icon configurations from all posters"
+ "Fetched icon config: %@"
+ "HIDDEN_WINDOWS_PILL_SUBTITLE"
+ "HIDDEN_WINDOWS_PILL_TITLE_FORMAT"
+ "Hidden Windows Pill"
+ "HiddenWindowsPillDismissal"
+ "KeyboardInput"
+ "No Dock Animation Bounce Height"
+ "No Dock Dismiss Animation Start Animation Delay"
+ "No Dock Offscreen Offset"
+ "Not allowing a foreground launch in setup mode"
+ "Pill Content Alpha Settings"
+ "Pill Content Blur Radius Settings"
+ "Pill Content Transform Settings"
+ "Pill Materialize Settings"
+ "Present Layout Settings"
+ "Present Opacity Settings"
+ "Present Position Settings"
+ "Present Scale Settings"
+ "Q24@0:8@\"SBSwitcherHiddenWindowsPill\"16"
+ "SBFloatingDockRemoteContentManagerRemoteContentOverlayFrameDidChangeNotification"
+ "SBFluidSwitcherViewController (%@)"
+ "SBHiddenWindowsPillAnimationDelayCompleteReason-%@-%lu"
+ "SBHiddenWindowsPillAnimationSettlingCompleteReason-%@-%lu"
+ "SBHiddenWindowsPillBounceIconBounceUpReason-%@-%lu"
+ "SBHiddenWindowsPillBounceIconCompletionReason-%@-%lu"
+ "SBHiddenWindowsPillBounceIconFallDownReason-%@-%lu"
+ "SBHiddenWindowsPillBounceIconScaleDownReason-%@-%lu"
+ "SBHiddenWindowsPillBounceIconScaleUpReason-%@-%lu"
+ "SBHiddenWindowsPillDismissAnimationCompletionReason-%@-%lu"
+ "SBHiddenWindowsPillDismissAnimationPhase1StartReason-%@-%lu"
+ "SBHiddenWindowsPillDismissAnimationPhase2StartReason-%@-%lu"
+ "SBHiddenWindowsPillDismissAnimationPhase3StartReason-%@-%lu"
+ "SBHiddenWindowsPillDismissAnimationSwitcherModifier"
+ "SBHiddenWindowsPillDismissAnimationSwitcherModifier.m"
+ "SBHiddenWindowsPillMaterializeAnimationCompleteReasonFormat-%@-%lu"
+ "SBHiddenWindowsPillMaterializeAnimationStartReasonFormat-%@-%lu"
+ "SBHiddenWindowsPillMaterializeAnimationSwitcherModifier"
+ "SBHiddenWindowsPillMaterializeAnimationSwitcherModifier.m"
+ "SBHiddenWindowsPillPresentAnimationSwitcherModifier"
+ "SBHiddenWindowsPillPresentAnimationSwitcherModifier.m"
+ "SBHiddenWindowsPillPresentPhase1CompleteReason-%@-%lu"
+ "SBHiddenWindowsPillPresentPhase2CompleteReason-%@-%lu"
+ "SBHiddenWindowsPillRootSwitcherModifier"
+ "SBHiddenWindowsPillRootSwitcherModifier.m"
+ "SBHiddenWindowsPillSwitcherModifier"
+ "SBHiddenWindowsPillSwitcherModifier.m"
+ "SBKeyboardInputSwitcherModifierEvent"
+ "SBNotificationCarPlayDestination.preprocessTimeoutTimer"
+ "SBSiriHUDSceneController"
+ "SBSwitcherHiddenWindowsPill"
+ "SBSwitcherHiddenWindowsPillView"
+ "SBSwitcherHiddenWindowsPillViewDelegate"
+ "SBTapHiddenWindowsPillSwitcherModifierEvent"
+ "SBTraitsParticipantRoleSiriHUD"
+ "SBTransientUIIndirectPanToDismissSwitcherModifierEvent"
+ "SBTransientUITapToDismissSwitcherModifierEvent"
+ "SB_STARTUP_SCREEN_TIME_TRACKING_CONTROLLER"
+ "SYSTEM_ACTION_COACHING_HIDE_FOCUS_LIST"
+ "Setting homeAffordanceDoubleTapGestureEnabled to %{BOOL}u because %{public}@ (%{public}@)"
+ "SiriDirectActionSourceDelegate"
+ "Steady State Modifier"
+ "T@\"<SBSwitcherHiddenWindowsPillViewDelegate>\",R,W,N,V_delegate"
+ "T@\"BSAbsoluteMachTimer\",&,N,G_preprocessTimeoutTimer,S_setPreprocessTimeoutTimer:,V_preprocessTimeoutTimer"
+ "T@\"NSMutableDictionary\",&,N,V_bounceIconViewsForHiddenWindowsPills"
+ "T@\"NSMutableDictionary\",&,N,V_hiddenWindowsPillIconPortals"
+ "T@\"NSMutableDictionary\",&,N,V_hiddenWindowsPills"
+ "T@\"NSString\",&,N,V_clientName"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_bouncePositionSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_bounceScaleSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimateDismissCenterYSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimateDismissLayoutSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimateDismissScaleSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimateDismissTranslateYSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimatePillContentAlphaSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimatePillContentBlurSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimatePillContentScaleSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimatePillMaterializationSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimatePresentLayoutSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimatePresentOpacitySettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimatePresentPillScaleSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimatePresentPositionSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillAnimatePresentScaleSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillBounceAnimationMoveDownSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillBounceAnimationMoveUpSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_hiddenWindowsPillBounceAnimationScaleSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_pillContentAlphaSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_pillContentBlurSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_pillContentScaleSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_pillMaterializationSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_pillOffsetSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_pillScaleSettings"
+ "T@\"SBHFileStackIcon\",&,N,V_closingFileStackIcon"
+ "T@\"SBHFileStackIcon\",&,N,V_openedFileStackIcon"
+ "T@\"SBSiriHUDSceneController\",&,N,V_siriHUDSceneController"
+ "T@\"SBSwitcherHiddenWindowsPill\",R,N,V_hiddenWindowsPill"
+ "TB,N,V_supportsCenterModalAppLayouts"
+ "TB,R,N,GisHomeAffordanceDoubleTapGestureEnabled,V_homeAffordanceDoubleTapGestureEnabled"
+ "TB,R,N,GisWallpaperDimmed"
+ "TB,R,N,VgroupOpacityRequiredForContentAnimation"
+ "TB,V_alwaysSuppressBacklightChanges"
+ "TQ,N,V_background"
+ "TapHiddenWindowsPill"
+ "Td,N,V_contentBlurRadius"
+ "Td,N,V_hiddenWindowsPillAnimationDelay"
+ "Td,N,V_hiddenWindowsPillAnimationInitialScale"
+ "Td,N,V_hiddenWindowsPillAnimationStartDelay"
+ "Td,N,V_hiddenWindowsPillIconBounceHeight"
+ "Td,N,V_hiddenWindowsPillNoDockOffscreenOffset"
+ "Td,N,V_hiddenWindowsPillVerticalOffsetAboveDock"
+ "Td,N,V_hiddenWindowsPillVerticalOffsetNoDock"
+ "Td,N,V_pillScale"
+ "Tq,N,V_lastKnownInterfaceOrientation"
+ "Tq,N,V_pillMode"
+ "Tq,R,N,V_numberOfHiddenWindows"
+ "TransientUIIndirectPanToDismiss"
+ "TransientUITapToDismiss"
+ "T{CGPoint=dd},N,V_pillOffset"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_remoteContentOverlayFrame"
+ "Unhandled PRSPosterIconSize: %ld"
+ "Unhandled PRSPosterIconStyleType: %ld"
+ "Unhandled PRSPosterIconStyleVariant: %ld"
+ "Updated content overlay frame for %@: %@"
+ "Vertical Offset (Above Dock)"
+ "Vertical Offset (No Dock)"
+ "_alwaysSuppressBacklightChanges"
+ "_applyStyleToHiddenWindowsPill:completion:"
+ "_applyStyleToHiddenWindowsPillsWithCompletion:"
+ "_beginObservingLayoutStateTransitionsIfNeeded"
+ "_bounceIconViewsForHiddenWindowsPills"
+ "_bouncePositionSettings"
+ "_bounceScaleSettings"
+ "_buildHideMenuWithAdditionalOptions:clientName:"
+ "_cachedCenterCardFrame"
+ "_cachedHiddenWindowsPillHeight"
+ "_canActivateSiri"
+ "_cancelCurrentPreprocessedSiriSession"
+ "_clearCurrentPreprocessRequest"
+ "_clientName"
+ "_closingFileStackIcon"
+ "_contentBlurRadius"
+ "_currentLayoutAttributesOrientationForSwitcherCorrespondingToDisplayOrdinal:"
+ "_disablesHomeAffordanceDoubleTapGestureInLandscape"
+ "_dismissalTransitionRequest"
+ "_effectiveGlassViewMaterial"
+ "_endObservingLayoutStateTransitionsIfNeeded"
+ "_floatingDockIconViewForDisplayItem:isVisible:"
+ "_flushPreprocessRequests"
+ "_hasRequestPreprocessed"
+ "_hasRequestPreprocessing"
+ "_hiddenWindowsPill"
+ "_hiddenWindowsPillAnimateDismissCenterYSettings"
+ "_hiddenWindowsPillAnimateDismissLayoutSettings"
+ "_hiddenWindowsPillAnimateDismissScaleSettings"
+ "_hiddenWindowsPillAnimateDismissTranslateYSettings"
+ "_hiddenWindowsPillAnimatePillContentAlphaSettings"
+ "_hiddenWindowsPillAnimatePillContentBlurSettings"
+ "_hiddenWindowsPillAnimatePillContentScaleSettings"
+ "_hiddenWindowsPillAnimatePillMaterializationSettings"
+ "_hiddenWindowsPillAnimatePresentLayoutSettings"
+ "_hiddenWindowsPillAnimatePresentOpacitySettings"
+ "_hiddenWindowsPillAnimatePresentPillScaleSettings"
+ "_hiddenWindowsPillAnimatePresentPositionSettings"
+ "_hiddenWindowsPillAnimatePresentScaleSettings"
+ "_hiddenWindowsPillAnimationDelay"
+ "_hiddenWindowsPillAnimationInitialScale"
+ "_hiddenWindowsPillAnimationStartDelay"
+ "_hiddenWindowsPillBounceAnimationMoveDownSettings"
+ "_hiddenWindowsPillBounceAnimationMoveUpSettings"
+ "_hiddenWindowsPillBounceAnimationScaleSettings"
+ "_hiddenWindowsPillIconBounceHeight"
+ "_hiddenWindowsPillIconPortals"
+ "_hiddenWindowsPillNoDockOffscreenOffset"
+ "_hiddenWindowsPillVerticalOffsetAboveDock"
+ "_hiddenWindowsPillVerticalOffsetNoDock"
+ "_hiddenWindowsPills"
+ "_hitTestedToTransientUIAtLocation:window:"
+ "_iconAppLayout"
+ "_iconBounceAnimationPhase"
+ "_iconBounceGenerationCount"
+ "_iconImageCacheConfigurationFromPosterIconConfiguration:"
+ "_iconScaleAnimationPhase"
+ "_iconScaleGenerationCount"
+ "_initialSelectedDisplayItemLayoutAttributesOnThisSwitcher"
+ "_invalidatePreprocessTimeoutTimer"
+ "_isIndexFullScreenOrCenterModal:"
+ "_keyboardAttentionAwarenessClient"
+ "_lastKnownInterfaceOrientationIsLandscape"
+ "_layoutAttributesForDisplayItem:displayOrdinal:orientation:"
+ "_layoutHiddenWindowsPill:completion:"
+ "_layoutHiddenWindowsPillBounceIcon:completion:"
+ "_layoutHiddenWindowsPillsWithCompletion:"
+ "_makeContentView"
+ "_makeGlass"
+ "_makeGlassView"
+ "_makeImageView"
+ "_makeMaskProgressAnimatableProperty"
+ "_makeMaskView"
+ "_makeTitleLabel"
+ "_maskProgressAnimatableProperty"
+ "_notificationRequestPreprocessed"
+ "_notificationRequestsPendingPreprocess"
+ "_notifiesAssistantOfApplicationTransitions"
+ "_numberOfHiddenWindows"
+ "_pillAnimationPhase"
+ "_pillContentAlphaSettings"
+ "_pillContentBlurSettings"
+ "_pillContentScaleSettings"
+ "_pillGenerationCount"
+ "_pillMaterializationSettings"
+ "_pillMode"
+ "_pillOffset"
+ "_pillOffsetSettings"
+ "_pillScale"
+ "_pillScaleSettings"
+ "_postNotificationRequest:shouldAnnounce:shouldPreprocess:"
+ "_preprocessCompleted"
+ "_preprocessNotificationRequest:"
+ "_preprocessTimeoutTimer"
+ "_presentBannerForRequest:"
+ "_processNextPreprocessRequest"
+ "_reevaluateHomeAffordanceDoubleTapGestureEnablement"
+ "_remoteContentOverlayFrame"
+ "_removalAppLayout"
+ "_requestPreprocessForNotificationRequest:"
+ "_screenTimeTrackingController"
+ "_setHomeAffordanceDoubleTapGestureEnabled:withReason:"
+ "_setPreprocessTimeoutTimer:"
+ "_shouldDematerialize"
+ "_shouldMaterialize"
+ "_shouldPreprocessNotificationRequest:"
+ "_shouldShowAlertForSeed"
+ "_siriHUDSceneController"
+ "_siriNotificationBannerActivationSource"
+ "_startPreprocessTimeoutTimer"
+ "_supportsCenterModalAppLayouts"
+ "_updateHiddenWindowsPillsViews"
+ "_updateKeyboardAttentionAwarenessClient"
+ "_updateRemoteContentOverlayFrame:"
+ "_visibleDisplayItemsForBundleIdentifier:"
+ "_willDockBeVisibleAtEndOfTransition"
+ "activeChangedTo:"
+ "addFileStackWithURL:preferredDisplayName:"
+ "alphaForHiddenWindowsPill:"
+ "alwaysSuppressBacklightChanges"
+ "apply style to hidden windows pills"
+ "backgroundForHiddenWindowsPill:"
+ "bounce.position"
+ "bounce.scale"
+ "bounceIconCenterForHiddenWindowsPill:"
+ "bounceIconScaleForHiddenWindowsPill:"
+ "bounceIconViewsForHiddenWindowsPills"
+ "bouncePositionSettings"
+ "bounceScaleSettings"
+ "canActivateChangedTo:"
+ "centerForHiddenWindowsPill:"
+ "clientName"
+ "clientRequestToUpdateFileStackIcon:contentOverlayFrame:"
+ "clientRequestToUpdateFileStackIcon:preferredDisplayName:"
+ "clientWillDeactivateWithContext:"
+ "closingFileStackIcon"
+ "com.apple.SiriHUD"
+ "com.apple.SpringBoard.SceneWorkspace.SiriHUD"
+ "contentAlphaForHiddenWindowsPill:"
+ "contentBlurRadius"
+ "contentBlurRadiusForHiddenWindowsPill:"
+ "contentScaleForHiddenWindowsPill:"
+ "d24@0:8@\"SBSwitcherHiddenWindowsPill\"16"
+ "deactivationRequest:"
+ "disabled by preference or eligibility"
+ "disabled for Continuity display"
+ "disabled in landscape on iPhone"
+ "dummyAppLayoutWithBundleIdentifier:sceneIdentifier:"
+ "fetchAllPosterIconConfigurationsForPrecaching:"
+ "fetchLockScreenHomeScreenColorConfigurations:"
+ "floatingDockIconFrameForAppLayout:"
+ "floatingDockIconImageFrameForAppLayout:"
+ "floatingDockIconScaleForAppLayout:"
+ "floatingDockIconViewForAppLayout:"
+ "getAnnounceNotificationsInCarPlayTemporarilyDisabledWithCompletion:"
+ "groupOpacityRequiredForContentAnimation"
+ "groupOpacityRequiredWhenRemovingItemContainerForLeafAppLayout:"
+ "handleKeyboardInputEvent:"
+ "handleTapHiddenWindowsPill:"
+ "handleTransientUIIndirectPannedToDismissSwitcherModifierEvent:"
+ "handleTransientUITapToDismissSwitcherModifierEvent:"
+ "hidden windows pill bounce icon layout"
+ "hidden windows pill layout"
+ "hidden windows pill style"
+ "hidden windows pills"
+ "hidden-windows-pill:%@"
+ "hiddenWindowsPill"
+ "hiddenWindowsPill != ((void *)0)"
+ "hiddenWindowsPillAnimateDismissCenterYSettings"
+ "hiddenWindowsPillAnimateDismissLayoutSettings"
+ "hiddenWindowsPillAnimateDismissScaleSettings"
+ "hiddenWindowsPillAnimateDismissTranslateYSettings"
+ "hiddenWindowsPillAnimatePillContentAlphaSettings"
+ "hiddenWindowsPillAnimatePillContentBlurSettings"
+ "hiddenWindowsPillAnimatePillContentScaleSettings"
+ "hiddenWindowsPillAnimatePillMaterializationSettings"
+ "hiddenWindowsPillAnimatePresentLayoutSettings"
+ "hiddenWindowsPillAnimatePresentOpacitySettings"
+ "hiddenWindowsPillAnimatePresentPillScaleSettings"
+ "hiddenWindowsPillAnimatePresentPositionSettings"
+ "hiddenWindowsPillAnimatePresentScaleSettings"
+ "hiddenWindowsPillAnimationDelay"
+ "hiddenWindowsPillAnimationInitialScale"
+ "hiddenWindowsPillAnimationStartDelay"
+ "hiddenWindowsPillBounceAnimationMoveDownSettings"
+ "hiddenWindowsPillBounceAnimationMoveUpSettings"
+ "hiddenWindowsPillBounceAnimationScaleSettings"
+ "hiddenWindowsPillHeight"
+ "hiddenWindowsPillIconBounceHeight"
+ "hiddenWindowsPillIconPortals"
+ "hiddenWindowsPillModeForHiddenWindowsPill:"
+ "hiddenWindowsPillModifierForTransitionEvent:"
+ "hiddenWindowsPillNoDockOffscreenOffset"
+ "hiddenWindowsPillVerticalOffsetAboveDock"
+ "hiddenWindowsPillVerticalOffsetNoDock"
+ "hiddenWindowsPillViewWasTapped:"
+ "hiddenWindowsPills"
+ "hideMenuWithOptions:clientName:"
+ "iconManager:extraIconImageCacheConfigurationsForPrecachingWithCompletion:"
+ "initWithBundleIdentifier:numberOfHiddenWindows:"
+ "initWithDeactivationOptions:animated:requestCancellationReason:dismissalReason:shouldTurnScreenOff:"
+ "initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:bannerManager:"
+ "initWithHiddenWindowsPill:"
+ "initWithHiddenWindowsPill:delegate:"
+ "initWithHiddenWindowsPill:direction:"
+ "initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:focusActivityManager:"
+ "initWithStyleConfiguration:iconSize:"
+ "initWithTransitionID:appLayout:layoutRole:multitaskingModifier:"
+ "initWithUNNotification:preprocess:"
+ "isHiddenWindowsPillSupported"
+ "isHiddenWindowsPillSupportedForSwitcherContentController:"
+ "lastKnownInterfaceOrientation"
+ "layoutAttributesForDisplayItem:"
+ "layoutAttributesForDisplayItem:displayOrdinal:"
+ "layoutAttributesForDisplayItem:displayOrdinal:orientation:"
+ "macwindow.on.rectangle"
+ "not disabled"
+ "numberOfHiddenWindows"
+ "numberOfOccludedOrOffStageDisplayItemsForBundleIdentifier:"
+ "performBaseMenuRequest:responseHandler:"
+ "pill.content.alpha"
+ "pill.content.blur"
+ "pill.content.scale"
+ "pill.glass"
+ "pill.opacity"
+ "pillContentAlphaSettings"
+ "pillContentBlurSettings"
+ "pillContentScaleSettings"
+ "pillMaterializationSettings"
+ "pillMode"
+ "pillOffset"
+ "pillOffsetForHiddenWindowsPill:"
+ "pillOffsetSettings"
+ "pillScale"
+ "pillScaleForHiddenWindowsPill:"
+ "pillScaleSettings"
+ "preprocessTimeoutTimer"
+ "q24@0:8@\"SBSwitcherHiddenWindowsPill\"16"
+ "remoteContentOverlayFrame"
+ "removeFirstObject"
+ "scaledValueForValue:"
+ "setAdjustsImageSizeForAccessibilityContentSizeCategory:"
+ "setAlwaysSuppressBacklightChanges:"
+ "setBounceIconViewsForHiddenWindowsPills:"
+ "setBouncePositionSettings:"
+ "setBounceScaleSettings:"
+ "setClientName:"
+ "setClosingFileStackIcon:"
+ "setContentBlurRadius:"
+ "setFlexible:"
+ "setHiddenWindowsPillAnimateDismissCenterYSettings:"
+ "setHiddenWindowsPillAnimateDismissLayoutSettings:"
+ "setHiddenWindowsPillAnimateDismissScaleSettings:"
+ "setHiddenWindowsPillAnimateDismissTranslateYSettings:"
+ "setHiddenWindowsPillAnimatePillContentAlphaSettings:"
+ "setHiddenWindowsPillAnimatePillContentBlurSettings:"
+ "setHiddenWindowsPillAnimatePillContentScaleSettings:"
+ "setHiddenWindowsPillAnimatePillMaterializationSettings:"
+ "setHiddenWindowsPillAnimatePresentLayoutSettings:"
+ "setHiddenWindowsPillAnimatePresentOpacitySettings:"
+ "setHiddenWindowsPillAnimatePresentPillScaleSettings:"
+ "setHiddenWindowsPillAnimatePresentPositionSettings:"
+ "setHiddenWindowsPillAnimatePresentScaleSettings:"
+ "setHiddenWindowsPillAnimationDelay:"
+ "setHiddenWindowsPillAnimationInitialScale:"
+ "setHiddenWindowsPillAnimationStartDelay:"
+ "setHiddenWindowsPillBounceAnimationMoveDownSettings:"
+ "setHiddenWindowsPillBounceAnimationMoveUpSettings:"
+ "setHiddenWindowsPillBounceAnimationScaleSettings:"
+ "setHiddenWindowsPillIconBounceHeight:"
+ "setHiddenWindowsPillIconPortals:"
+ "setHiddenWindowsPillNoDockOffscreenOffset:"
+ "setHiddenWindowsPillVerticalOffsetAboveDock:"
+ "setHiddenWindowsPillVerticalOffsetNoDock:"
+ "setHiddenWindowsPills:"
+ "setLastKnownInterfaceOrientation:"
+ "setPillContentAlphaSettings:"
+ "setPillContentBlurSettings:"
+ "setPillContentScaleSettings:"
+ "setPillMaterializationSettings:"
+ "setPillMode:"
+ "setPillOffset:"
+ "setPillOffsetSettings:"
+ "setPillScale:"
+ "setPillScaleSettings:"
+ "setPreferredDisplayName:"
+ "setSiriHUDSceneController:"
+ "setSupportsCenterModalAppLayouts:"
+ "sharedPreferences"
+ "shouldBounceIconPresentForHiddenWindowsPill:"
+ "siriHUDSceneController"
+ "startObservingAllNotifications"
+ "stopObservingAllNotifications"
+ "supportsCenterModalAppLayouts"
+ "systemHideMenuWithOptions:clientName:"
+ "transformForHiddenWindowsPill:"
+ "updateLayoutAttributes:ofDisplayItem:displayOrdinal:"
+ "updateLayoutAttributesMap:forDisplayOrdinal:"
+ "updateLayoutAttributesMap:forDisplayOrdinal:orientation:"
+ "updateProperties"
+ "updatePropertiesIfNeeded"
+ "v16@?0@\"_UIMainMenuBaseMenuResponse\"8"
+ "v24@0:8@\"FBSSceneTransitionContext\"16"
+ "v24@0:8@\"SBSwitcherHiddenWindowsPillView\"16"
+ "v32@0:8@\"NSDictionary\"16q24"
+ "v32@0:8@\"NSURL\"16@\"NSString\"24"
+ "v32@0:8@\"SBHIconManager\"16@?<v@?@\"NSArray\">24"
+ "v32@?0@\"SBChainableModifier\"8@16q24"
+ "v40@0:8@\"NSDictionary\"16q24q32"
+ "v40@0:8@\"SBDisplayItemLayoutAttributes\"16@\"SBDisplayItem\"24q32"
+ "v40@?0@\"SBChainableModifier\"8@16@24q32"
+ "wantsKeyboardInputEvents"
+ "{?=\"cachedIndexOfFirstMainAppLayoutIsValid\"b1\"cachedFullScreenCardScaleIsValid\"b1\"cachedContentSizeIsValid\"b1\"cachedFrameForIndexIsValid\"b1\"cachedCenterCardFrameIsValid\"b1}"
+ "{?=\"switcherGestureManagerForSwitcherContentController\"b1\"sceneRelevancyManagerForSwitcherContentController\"b1\"switcherIconZoomContextProviderForSwitcherContentController\"b1\"homeGestureSettingsForSwitcherContentController\"b1\"maximumNumberOfScenesOnStageForSwitcherContentController\"b1\"activeTransientOverlayPresentedAppLayoutForSwitcherContentController\"b1\"appLayoutForWorkspaceTransientOverlay\"b1\"viewControllerForTransientOverlayAppLayout\"b1\"createWorkspaceTransientOverlayForAppLayout\"b1\"matchingIconViewForIconView\"b1\"prioritizesSortOrderForAppLayout\"b1\"switcherContentControllerFrameForFloatingAppLayoutInInterfaceOrientationFloatingConfiguration\"b1\"switcherContentControllerFrameForCenterItemWithConfigurationInterfaceOrientation\"b1\"homeScreenInterfaceOrientationForContentController\"b1\"backdropInterfaceStyleForContentController\"b1\"switcherContentControllerShouldMorphToPIPForTransitionContext\"b1\"switcherContentControllerShouldMorphFromPIPForTransitionContext\"b1\"isInAppStatusBarRequestedHiddenForSwitcherContentController\"b1\"leadingStatusBarPartFrameForSwitcherContentController\"b1\"trailingStatusBarPartFrameForSwitcherContentController\"b1\"switcherContentControllerVisibleAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerVisibleDisplayItemsForBundleIdentifier\"b1\"switcherContentControllerHiddenAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerReloadsSnapshotsForActiveInterfaceOrientationChange\"b1\"switcherContentControllerHasMultipleDisplays\"b1\"switcherContentControllerSupportsTitleItemsForAppLayout\"b1\"switcherContentControllerSupportsKillingOfAppLayout\"b1\"switcherContentControllerDisplayItemSupportsCenterRole\"b1\"switcherContentControllerIsKeyboardHomeAffordanceAssertionCurrentlyBeingTaken\"b1\"switcherContentControllerDeviceApplicationSceneHandleForDisplayItem\"b1\"isDisplayEmbeddedForSwitcherContentController\"b1\"windowManagementContextForSwitcherContentController\"b1\"draggingAppLayoutsForWindowDragForSwitcherContentController\"b1\"proposedAppLayoutsForWindowDragForSwitcherContentController\"b1\"isSwitcherContentControllerEphemeral\"b1\"displayConfigurationsOfOtherDisplaysForSwitcherContentController\"b1\"guardedForegroundDisplayItemsForSwitcherContentController\"b1\"desktopSpaceItemsForSwitcherContentController\"b1\"slideOverItemForSwitcherContentController\"b1\"windowingConfigurationForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1\"appLayoutForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1\"genieGlassHighlightForSwitcherContentController\"b1\"isHiddenWindowsPillSupportedForSwitcherContentController\"b1}"
+ "{CGAffineTransform=dddddd}24@0:8@\"SBSwitcherHiddenWindowsPill\"16"
+ "{CGAffineTransform=dddddd}24@?0@\"SBChainableModifier\"8@16"
+ "{CGPoint=dd}24@0:8@\"SBSwitcherHiddenWindowsPill\"16"
+ "\x81!\xb1"
+ "\xf0\xf0\x82"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc2\xf0\xf0Q"
- "%@Color"
- "%x"
- "([\\dA-F]{6})"
- "-[SBDisplayItemLayoutAttributesProvider layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:]"
- "-[SBHomeScreenService addFileStackWithURL:]"
- "@\"SBDisplayItemLayoutAttributes\"48@0:8@\"SBDisplayItem\"16@\"SBAppLayout\"24q32q40"
- "Carplay setting up deferred announce deactivation for %{public}@ on announce finish since this is the last notification to be announced"
- "Carplay withdrawing currently announcing notification request %{public}@ as it is starting announce for request %{public}@"
- "Carplay withdrawing notification request %{public}@ on announce finish while pending other announce notifications"
- "Client finishes closing animation."
- "Client finishes opening animation."
- "DeviceEmulation"
- "PartiallyOffscreenWindows"
- "SBDeviceEmulationController"
- "T@\"CALayer\",R,N,V_bezelLayer"
- "T@\"CALayer\",R,N,V_layerForBackgroundColor"
- "T@\"CALayer\",R,N,V_maskLayer"
- "T@\"SBIcon\",&,N,V_openedFileStackIcon"
- "T@\"UIColor\",R,N,V_backgroundColor"
- "T@\"UISApplicationInitializationContext\",R,C,N"
- "T@\"UISDeviceContext\",R,C,N"
- "T@\"UISDisplayContext\",R,C,N"
- "TB,N,GisContentReady,V_contentReady"
- "TB,N,GisRemoteViewVisible,V_remoteViewVisible"
- "TB,R,N,GisDefaultWebBrowser"
- "Unable to create redacted display configuration: %@ from configuration:%@"
- "_alphaAnimatableProperty"
- "_bezelLayer"
- "_buildHideMenuWithAdditionalOptions:"
- "_configureRootLayer:sceneTransformLayer:transformLayer:"
- "_contentReady"
- "_createAlphaAnimatableProperty"
- "_initialSelectedDisplayItemLayoutAttributes"
- "_isIndexFullScreen:"
- "_layerForBackgroundColor"
- "_layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:"
- "_maskLayer"
- "_postNotificationRequest:shouldAnnounce:"
- "_remoteViewVisible"
- "_shouldConstrainToBottomEdge"
- "_shouldConstrainToLeftEdge"
- "_shouldConstrainToRightEdge"
- "_updateRootLayerBackgroundColor"
- "_updateTransformLayer"
- "applicationInitializationContext"
- "bezelLayer"
- "contentReady"
- "customScaleFactorX"
- "customScaleFactorY"
- "customTranslationOffsetX"
- "customTranslationOffsetY"
- "defaultApplicationForCategory:error:"
- "defaultWebBrowser"
- "deviceContext"
- "displayContext"
- "emulatedDeviceBezelImageName"
- "emulatedDeviceBounds"
- "emulatedDeviceClass"
- "emulatedDeviceImageContainingBundle"
- "emulatedDeviceMaskImageName"
- "emulatedDisplayCornerRadius"
- "emulatedHomeButtonType"
- "getBaseMainMenu:"
- "hasDifferentColorAppearanceComparedToTraitCollection:"
- "hasEmulatedDeviceBounds"
- "hideMenuWithOptions:"
- "initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:bannerManager:"
- "initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:"
- "initWithTransitionID:appLayout:multitaskingModifier:"
- "insertSublayer:below:"
- "isDefaultWebBrowser"
- "isEmulatedDevice"
- "isPartiallyOffscreenWindowsEnabled"
- "isRemoteViewVisible"
- "layerForBackgroundColor"
- "layoutAttributesForDisplayItem:inAppLayout:"
- "layoutAttributesForDisplayItem:inAppLayout:displayOrdinal:orientation:"
- "maskLayer"
- "remoteViewVisible"
- "renderingCenter"
- "rootLayerBackgroundColorString"
- "sb_configureForDeviceEmulation"
- "scalingStyle"
- "setContentReady:"
- "setDeviceContext:"
- "setDisplayContext:"
- "setRemoteViewVisible:"
- "systemHideMenuWithOptions:"
- "updateLayoutAttributesMap:forAppLayout:"
- "updateLayoutAttributesMap:forAppLayout:displayOrdinal:orientation:"
- "v16@?0@\"_UIMainMenu\"8"
- "v32@0:8@\"NSDictionary\"16@\"SBAppLayout\"24"
- "v48@0:8@\"NSDictionary\"16@\"SBAppLayout\"24q32q40"
- "{?=\"cachedIndexOfFirstMainAppLayoutIsValid\"b1\"cachedFullScreenCardScaleIsValid\"b1\"cachedContentSizeIsValid\"b1\"cachedFrameForIndexIsValid\"b1}"
- "{?=\"switcherGestureManagerForSwitcherContentController\"b1\"sceneRelevancyManagerForSwitcherContentController\"b1\"switcherIconZoomContextProviderForSwitcherContentController\"b1\"homeGestureSettingsForSwitcherContentController\"b1\"maximumNumberOfScenesOnStageForSwitcherContentController\"b1\"activeTransientOverlayPresentedAppLayoutForSwitcherContentController\"b1\"appLayoutForWorkspaceTransientOverlay\"b1\"viewControllerForTransientOverlayAppLayout\"b1\"createWorkspaceTransientOverlayForAppLayout\"b1\"matchingIconViewForIconView\"b1\"prioritizesSortOrderForAppLayout\"b1\"switcherContentControllerFrameForFloatingAppLayoutInInterfaceOrientationFloatingConfiguration\"b1\"switcherContentControllerFrameForCenterItemWithConfigurationInterfaceOrientation\"b1\"homeScreenInterfaceOrientationForContentController\"b1\"backdropInterfaceStyleForContentController\"b1\"switcherContentControllerShouldMorphToPIPForTransitionContext\"b1\"switcherContentControllerShouldMorphFromPIPForTransitionContext\"b1\"isInAppStatusBarRequestedHiddenForSwitcherContentController\"b1\"leadingStatusBarPartFrameForSwitcherContentController\"b1\"trailingStatusBarPartFrameForSwitcherContentController\"b1\"switcherContentControllerVisibleAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerVisibleDisplayItemsForBundleIdentifier\"b1\"switcherContentControllerHiddenAppLayoutsForBundleIdentifier\"b1\"switcherContentControllerReloadsSnapshotsForActiveInterfaceOrientationChange\"b1\"switcherContentControllerHasMultipleDisplays\"b1\"switcherContentControllerSupportsTitleItemsForAppLayout\"b1\"switcherContentControllerSupportsKillingOfAppLayout\"b1\"switcherContentControllerDisplayItemSupportsCenterRole\"b1\"switcherContentControllerIsKeyboardHomeAffordanceAssertionCurrentlyBeingTaken\"b1\"switcherContentControllerDeviceApplicationSceneHandleForDisplayItem\"b1\"isDisplayEmbeddedForSwitcherContentController\"b1\"windowManagementContextForSwitcherContentController\"b1\"draggingAppLayoutsForWindowDragForSwitcherContentController\"b1\"proposedAppLayoutsForWindowDragForSwitcherContentController\"b1\"isSwitcherContentControllerEphemeral\"b1\"displayConfigurationsOfOtherDisplaysForSwitcherContentController\"b1\"guardedForegroundDisplayItemsForSwitcherContentController\"b1\"desktopSpaceItemsForSwitcherContentController\"b1\"slideOverItemForSwitcherContentController\"b1\"windowingConfigurationForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1\"appLayoutForSwitcherContentControllerCorrespondingToDisplayOrdinal\"b1\"genieGlassHighlightForSwitcherContentController\"b1}"
- "\x81!\xa1"
- "\x82"
- "\xf0\xf0r"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa2\xf0\xf01"

```
