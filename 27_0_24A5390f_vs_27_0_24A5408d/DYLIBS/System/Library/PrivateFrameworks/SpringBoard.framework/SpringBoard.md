## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4630.1.102.0.0
-  __TEXT.__text: 0xaf7f74
+4636.102.1.0.0
+  __TEXT.__text: 0xb07b50
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xbcab8
-  __TEXT.__const: 0x112a0
-  __TEXT.__oslogstring: 0x6312a
-  __TEXT.__cstring: 0x8435f
-  __TEXT.__gcc_except_tab: 0x181f4
+  __TEXT.__objc_methlist: 0xbd8d0
+  __TEXT.__const: 0x112c0
+  __TEXT.__oslogstring: 0x64e36
+  __TEXT.__cstring: 0x84d46
+  __TEXT.__gcc_except_tab: 0x184fc
   __TEXT.__ustring: 0xd04
   __TEXT.__dlopen_cstrs: 0x373
-  __TEXT.__unwind_info: 0x2e170
+  __TEXT.__unwind_info: 0x2e4d8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d730
-  __DATA_CONST.__objc_classlist: 0x5478
+  __DATA_CONST.__const: 0x1d940
+  __DATA_CONST.__objc_classlist: 0x54c0
   __DATA_CONST.__objc_catlist: 0x338
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2a90
+  __DATA_CONST.__objc_protolist: 0x2ad0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e198
-  __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__objc_superrefs: 0x4048
-  __DATA_CONST.__objc_arraydata: 0x18a0
-  __DATA_CONST.__got: 0xa8b8
-  __AUTH_CONST.__const: 0x10af8
-  __AUTH_CONST.__cfstring: 0x73ca0
-  __AUTH_CONST.__objc_const: 0x285030
+  __DATA_CONST.__objc_selrefs: 0x4e7d0
+  __DATA_CONST.__objc_protorefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x4080
+  __DATA_CONST.__objc_arraydata: 0x1888
+  __DATA_CONST.__got: 0xa8f0
+  __AUTH_CONST.__const: 0x10b88
+  __AUTH_CONST.__cfstring: 0x744e0
+  __AUTH_CONST.__objc_const: 0x287848
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x1758
-  __AUTH_CONST.__objc_doubleobj: 0x820
-  __AUTH_CONST.__objc_intobj: 0x2c88
+  __AUTH_CONST.__objc_arrayobj: 0x1728
+  __AUTH_CONST.__objc_doubleobj: 0x850
+  __AUTH_CONST.__objc_intobj: 0x2ca0
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH_CONST.__auth_got: 0x2bc0
-  __AUTH.__objc_data: 0xe010
-  __DATA.__objc_ivar: 0xfaa4
-  __DATA.__data: 0x20bc0
-  __DATA.__bss: 0xa28
+  __AUTH.__objc_data: 0xe3d0
+  __DATA.__objc_ivar: 0xfc10
+  __DATA.__data: 0x20ec0
+  __DATA.__bss: 0xa80
   __DATA.__common: 0xa40
-  __DATA_DIRTY.__objc_data: 0x26ca0
+  __DATA_DIRTY.__objc_data: 0x26bb0
   __DATA_DIRTY.__data: 0x140
-  __DATA_DIRTY.__bss: 0x18d8
+  __DATA_DIRTY.__bss: 0x18c8
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/MultipeerConnectivity.framework/MultipeerConnectivity
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/NotificationCenter.framework/NotificationCenter
+  - /System/Library/Frameworks/PencilKit.framework/PencilKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/SafariServices.framework/SafariServices
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/SplashBoard.framework/SplashBoard
   - /System/Library/PrivateFrameworks/SpotlightUI.framework/SpotlightUI
   - /System/Library/PrivateFrameworks/SpringBoardDisplay.framework/SpringBoardDisplay
+  - /System/Library/PrivateFrameworks/SpringBoardDisplayServices.framework/SpringBoardDisplayServices
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation
   - /System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome
   - /System/Library/PrivateFrameworks/SpringBoardIntents.framework/SpringBoardIntents

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  Functions: 73090
-  Symbols:   151251
-  CStrings:  23326
+  Functions: 73431
+  Symbols:   151928
+  CStrings:  23474
 
Symbols:
+ +[SBAssistantIslandWorkspace terminateNonIslandSpotlight]
+ +[SBCoreSmartPowerNapHIDCoordinator coordinatorForWindowSceneManager:]
+ +[SBInputUISceneControllerExtension settingsExtensions]
+ +[SBScreenBrightnessSceneExtension hostComponents]
+ -[FBScene(InputUISceneController) sb_disallowsKeyboardPresentationInDefaultInputUIPresenter]
+ -[FBScene(InputUISceneController) sb_setDisallowsKeyboardPresentationInDefaultInputUIPresenter:]
+ -[SBActivationInfoViewController _deviceIsChinaSKU]
+ -[SBActivityMetrics _metricsForWindowScene:]
+ -[SBActivityMetrics activeLayoutDirection]
+ -[SBActivityMetrics initWithConfiguration:windowScene:activeLayoutDirection:]
+ -[SBActivitySystemApertureElementObserver _forwardElementContextChangesFromElement:forActivityIdentifier:]
+ -[SBActivitySystemApertureElementObserver _sceneHandleForActivityIdentifier:]
+ -[SBActivitySystemApertureElementObserver _updateSceneHandleForActivityIdentifier:withDestinationToken:layoutDirection:]
+ -[SBActivitySystemApertureElementObserver systemApertureSceneElement:destinationTokenDidChange:]
+ -[SBActivitySystemApertureElementObserver systemApertureSceneElement:layoutDirectionDidChange:]
+ -[SBActivitySystemApertureSceneHandle activeLayoutDirection]
+ -[SBActivitySystemApertureSceneHandle setActiveLayoutDirection:]
+ -[SBActivitySystemApertureSceneHandle setActiveWindowScene:activeLayoutDirection:]
+ -[SBAmbientIdleTimerController _canPerformMotionWake]
+ -[SBAmbientIdleTimerController _handlePresenceMotion]
+ -[SBAmbientIdleTimerController _isMotionDetectionCapable]
+ -[SBAmbientIdleTimerController _isMotionToWakePermitted]
+ -[SBAmbientIdleTimerController _isSuppressionActive]
+ -[SBAmbientIdleTimerController _updateMotionDetectionCapability]
+ -[SBAmbientIdleTimerController _updateMotionDetectionIdleTimerAssertion]
+ -[SBAmbientIdleTimerController _updateMotionDetectionListening]
+ -[SBAmbientIdleTimerController _updateMotionDetectionWake]
+ -[SBAmbientIdleTimerController initWithWindowScene:]
+ -[SBAmbientIdleTimerController motionDetectionWakeAttributeMonitor:didUpdateShouldEnableMotionDetectionWake:]
+ -[SBAmbientIdleTimerController motionDetectionWakeController:motionDetectStateChanged:]
+ -[SBAmbientIdleTimerController refreshMotionDetectionWake]
+ -[SBAmbientIdleTimerController setOnAC:]
+ -[SBAppResizingService resizingCoordinator:didUpdateResizingPossible:preferredSize:]
+ -[SBApplication(SwitcherCapabilitiesProvidedByClassic) sceneResizingCapability]
+ -[SBApplication(SwitcherCapabilitiesProvidedByClassic) supportsSceneResizing]
+ -[SBApplicationInfo couldSupportMedusa]
+ -[SBAssistantIslandSettings floatingPresentationStatusBarOutset]
+ -[SBAssistantIslandSettings isHomeScreenTranslationEnabled]
+ -[SBAssistantIslandSettings listeningThinkingWaveActiveGaussianRadius]
+ -[SBAssistantIslandSettings listeningThinkingWaveInitialGaussianRadius]
+ -[SBAssistantIslandSettings listeningThinkingWaveLensingAmount]
+ -[SBAssistantIslandSettings listeningThinkingWaveLensingHeight]
+ -[SBAssistantIslandSettings listeningThinkingWaveVariableBlurLocation]
+ -[SBAssistantIslandSettings listeningThinkingWaveVariableBlurRadius]
+ -[SBAssistantIslandSettings setFloatingPresentationStatusBarOutset:]
+ -[SBAssistantIslandSettings setHomeScreenTranslationEnabled:]
+ -[SBAssistantIslandSettings setListeningThinkingWaveActiveGaussianRadius:]
+ -[SBAssistantIslandSettings setListeningThinkingWaveInitialGaussianRadius:]
+ -[SBAssistantIslandSettings setListeningThinkingWaveLensingAmount:]
+ -[SBAssistantIslandSettings setListeningThinkingWaveLensingHeight:]
+ -[SBAssistantIslandSettings setListeningThinkingWaveVariableBlurLocation:]
+ -[SBAssistantIslandSettings setListeningThinkingWaveVariableBlurRadius:]
+ -[SBAssistantIslandSettings setSystemApertureUnifiedAnimationEnabled:]
+ -[SBAssistantIslandSettings systemApertureUnifiedAnimationEnabled]
+ -[SBAssistantIslandStageController _applyListeningThinkingWaveSettings:]
+ -[SBAssistantIslandStageController _setHostWindowAlpha:]
+ -[SBAssistantIslandStageController _updateHostingDisplayBacklightStateActive]
+ -[SBAssistantIslandStageController _updateKeyboardFocusSuppression]
+ -[SBAssistantIslandStageController _updateListeningThinkingWaveSettings]
+ -[SBAssistantIslandStageController _updateResidentInactive]
+ -[SBAssistantIslandStageController _updateStatusBarWindowLevelOverride]
+ -[SBAssistantIslandStageController _updateSystemApertureAnimationStyle]
+ -[SBAssistantIslandStageController backlightController:didTransitionToBacklightState:source:]
+ -[SBAssistantIslandStageController currentKeyboardProxyOwner]
+ -[SBAssistantIslandStageController isResidentInactive]
+ -[SBAssistantIslandStageController settings:changedValueForKey:]
+ -[SBAssistantIslandStageController stageQuiescentPresentationState]
+ -[SBAssistantIslandStageController updateSpotlightInvocationSource:]
+ -[SBAssistantIslandStageCoordinator _assistantIslandEnablementDidChange:]
+ -[SBAssistantIslandStageCoordinator _deviceSupportsAppleIntelligence]
+ -[SBAssistantIslandStageCoordinator _invalidateAllSceneControllers]
+ -[SBAssistantIslandStageCoordinator _isAssistantIslandVisiblyPresentedOnWindowScene:]
+ -[SBAssistantIslandStageCoordinator _isPrewarmDisabledForClientCrashLoop]
+ -[SBAssistantIslandStageCoordinator _noteClientDidCrash]
+ -[SBAssistantIslandStageCoordinator _registerZOrderStageResolverForWindowSceneIfNeeded:]
+ -[SBAssistantIslandStageCoordinator _setupBackgroundKeepAlive]
+ -[SBAssistantIslandStageCoordinator _updateBackgroundAngelKeepAlive]
+ -[SBAssistantIslandStageCoordinator _updateResidentInactiveStageForWindowScene:]
+ -[SBAssistantIslandStageCoordinator _updateResidentInactiveStages]
+ -[SBAssistantIslandStageCoordinator fetchOrCreateNewStageControllerForWindowScene:state:chatSessionIdentifier:spotlightInvocationSource:dismissesControlCenterIfVisible:actions:completion:]
+ -[SBAssistantIslandStageCoordinator gestureManagerIsActivityResignedActive:]
+ -[SBAssistantIslandStageCoordinator keybag:extendedStateDidChange:]
+ -[SBAssistantIslandStageCoordinator processDidExit:]
+ -[SBAssistantIslandStageCoordinator processManager:didAddProcess:]
+ -[SBAssistantIslandStageCoordinator processManager:didRemoveProcess:]
+ -[SBAssistantIslandStageGestureManager _isSystemApertureGestureRecognizer:]
+ -[SBAssistantIslandStageGestureManager _systemApertureLayoutDidChange:]
+ -[SBAssistantVisionIntelligenceActivationRequestAction abortForUsageViolation:]
+ -[SBBacklightPlatformProvider noteSignificantEvent]
+ -[SBBacklightServicesPlatformProvider noteSignificantEvent]
+ -[SBBannerTransitionSettings customBannerTransitionStyleGlass_cornerAnchorYOffset]
+ -[SBBannerTransitionSettings customBannerTransitionStyleGlass_morphHandleCornerRadius]
+ -[SBBannerTransitionSettings customBannerTransitionStyleGlass_morphHandleCrossFadeStartFraction]
+ -[SBBannerTransitionSettings setCustomBannerTransitionStyleGlass_cornerAnchorYOffset:]
+ -[SBBannerTransitionSettings setCustomBannerTransitionStyleGlass_morphHandleCornerRadius:]
+ -[SBBannerTransitionSettings setCustomBannerTransitionStyleGlass_morphHandleCrossFadeStartFraction:]
+ -[SBContinuitySession resizingCoordinator:didUpdateResizingPossible:preferredSize:]
+ -[SBControlCenterController appNameMenuBarProviderForControlCenterViewController:]
+ -[SBControlCenterCoordinator beginObservingSystemState]
+ -[SBCoreSmartPowerNapHIDCoordinator .cxx_destruct]
+ -[SBCoreSmartPowerNapHIDCoordinator _acquireAssertion]
+ -[SBCoreSmartPowerNapHIDCoordinator _callbackQueue]
+ -[SBCoreSmartPowerNapHIDCoordinator _digitizerAssertion]
+ -[SBCoreSmartPowerNapHIDCoordinator _handleState:]
+ -[SBCoreSmartPowerNapHIDCoordinator _handleStateForTesting:]
+ -[SBCoreSmartPowerNapHIDCoordinator _handleStateOnMainQueue:]
+ -[SBCoreSmartPowerNapHIDCoordinator _noteSmartCoverDidOpenOnMain]
+ -[SBCoreSmartPowerNapHIDCoordinator _userPresenceLatch]
+ -[SBCoreSmartPowerNapHIDCoordinator initWithWindowSceneManager:cspn:]
+ -[SBCoreSmartPowerNapHIDCoordinator noteSmartCoverDidOpen]
+ -[SBCoreSmartPowerNapHIDCoordinator start]
+ -[SBCoreSmartPowerNapHIDCoordinator stop]
+ -[SBCoverSheetGrabberManager _beginWaitingForAppFlyInSettle]
+ -[SBCoverSheetGrabberManager _canPresentGrabberForHandoff]
+ -[SBCoverSheetGrabberManager _finishWaitingForAppFlyInSettle]
+ -[SBCoverSheetGrabberManager _handleCoverSheetAppFlyInDidSettleNotification:]
+ -[SBCoverSheetGrabberManager _handleCoverSheetDismissalNearlyCompleteNotification:]
+ -[SBCoverSheetGrabberManager appFlyInDidSettleTimestamp]
+ -[SBCoverSheetGrabberManager appFlyInDidSettle]
+ -[SBCoverSheetGrabberManager appFlyInSettleFallbackTimer]
+ -[SBCoverSheetGrabberManager bannerHandoffInstantAppear]
+ -[SBCoverSheetGrabberManager handoffBannerDismiss]
+ -[SBCoverSheetGrabberManager isWaitingForAppFlyInSettle]
+ -[SBCoverSheetGrabberManager newBannerMorphHandleView]
+ -[SBCoverSheetGrabberManager setAppFlyInDidSettle:]
+ -[SBCoverSheetGrabberManager setAppFlyInDidSettleTimestamp:]
+ -[SBCoverSheetGrabberManager setAppFlyInSettleFallbackTimer:]
+ -[SBCoverSheetGrabberManager setBannerHandoffInstantAppear:]
+ -[SBCoverSheetGrabberManager setIsWaitingForAppFlyInSettle:]
+ -[SBCoverSheetGrabberManager setSuppressTeachPulse:]
+ -[SBCoverSheetGrabberManager suppressTeachPulse]
+ -[SBCoverSheetGrabberManager targetGrabberFrameInCoordinateSpace:]
+ -[SBCoverSheetGrabberViewController _timeLabelFrameInWindow:statusBar:]
+ -[SBCoverSheetGrabberViewController newBannerMorphHandleViewWithLegibilitySettings:]
+ -[SBCoverSheetGrabberViewController targetGrabberFrameInCoordinateSpace:]
+ -[SBCoverSheetPresentationManager _checkAndPostDismissalNearlyCompleteNotificationWithProgress:isPresenting:isOverApp:]
+ -[SBCoverSheetPresentationManager dismissalCommitted]
+ -[SBCoverSheetPresentationManager hasPostedDismissalNearlyCompleteNotification]
+ -[SBCoverSheetPresentationManager lastSettledPresentedState]
+ -[SBCoverSheetPresentationManager setDismissalCommitted:]
+ -[SBCoverSheetPresentationManager setHasPostedDismissalNearlyCompleteNotification:]
+ -[SBCoverSheetPresentationManager setLastSettledPresentedState:]
+ -[SBCoverSheetPrimarySlidingViewController _didFinishOffscreenTransition]
+ -[SBCoverSheetPrimarySlidingViewController _updateDimmingViewMaskPositionForOffScreenWithBounds:]
+ -[SBCoverSheetSlidingViewController _didFinishOffscreenTransition]
+ -[SBCoverSheetToAppSwitcherModifier _beginObservingAppFlyInSettle]
+ -[SBCoverSheetToAppSwitcherModifier _displayLinkFired:]
+ -[SBCoverSheetToAppSwitcherModifier _stopObservingAppFlyInSettle]
+ -[SBCoverSheetToAppSwitcherModifier dealloc]
+ -[SBCoverSheetToAppSwitcherModifier didMoveToParentModifier:]
+ -[SBDeviceApplicationInputUIViewProvider contentWantsSimplifiedOrientationBehavior]
+ -[SBDeviceApplicationInputUIViewProvider shouldFollowSceneOrientation]
+ -[SBDeviceApplicationSceneClassicWrapperView contentFrame]
+ -[SBDeviceApplicationSceneHandle _fakedResizingDisplayConfigurationForFrame:]
+ -[SBDeviceApplicationSceneHandle(TraitsSceneDelegateStateTracking) _hasResizedSinceEnteringDisplay]
+ -[SBDeviceApplicationSceneView _contentFrameInSceneReferenceSpace]
+ -[SBDeviceApplicationSceneViewController _clearStatusBarPartAlphaOverridesIfNeeded]
+ -[SBExternalDisplayLayoutPublisherFactory invalidateLayoutPublisher:observer:]
+ -[SBExternalDisplayLayoutPublisherFactory newLayoutPublisherWithInstanceIdentifier:displayConfiguration:observer:]
+ -[SBExternalDisplayService _createLayoutPublisherForRootDisplayIdentityIfNeeded:displayConfiguration:]
+ -[SBExternalDisplayService _invalidateLayoutPublisherForRootDisplayIdentity:]
+ -[SBExternalDisplayService initWithServiceListenerFactory:connectedDisplayInfoFactory:layoutPublisherFactory:defaults:]
+ -[SBExternalDisplayService layoutPublisherForRootDisplayIdentity:]
+ -[SBExternalDisplayService publisher:didUpdateLayout:withTransition:]
+ -[SBFluidSwitcherViewController _centerStatusBarPartFrame]
+ -[SBFluidSwitcherViewController _leadingStatusBarPartFrameIncludingCenterPartIfNecessary]
+ -[SBFluidSwitcherViewController currentPresentationTransformForVisibleAppLayout:]
+ -[SBFluidSwitcherViewController displayItemIsDiscreteResizable:]
+ -[SBFluidSwitcherViewController newDisplayLinkWithTarget:selector:]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay setStatusBarPartAlphas:nubViewHidden:animator:]
+ -[SBGlassBannerTransitionAnimator _cornerCenterForContext:withFrame:scale:grabberHandoffFrame:]
+ -[SBGlassBannerTransitionAnimator _tearDownMorphHandle]
+ -[SBHIDUISensorModeAssertion proximitySuspensionMode]
+ -[SBHIDUISensorModeAssertion setProximitySuspensionMode:]
+ -[SBHIDUISensorModeController _isInCallOnReceiverRoute]
+ -[SBHomeScreenController _controlCenterWindowSceneDidConnect:]
+ -[SBHomeScreenController _dismissalCompletionLeavingGroup:foldingFinishedInto:]
+ -[SBHomeScreenController _requireGesturesToFail:forSearchGesture:]
+ -[SBHomeScreenController _requireGesturesToFail:forTodayViewController:]
+ -[SBHomeScreenService canSwapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]
+ -[SBHomeScreenService replaceApplicationIconsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]
+ -[SBHomeScreenService swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]
+ -[SBHomeScreenService tearDownAndResetRootIconLists]
+ -[SBInAppStatusBarHiddenAssertion initWithIdentifier:forReason:partAlphas:invalidationBlock:]
+ -[SBInAppStatusBarHiddenAssertion partAlphas]
+ -[SBInAppStatusBarHiddenAssertion setPartAlphas:]
+ -[SBInProcessSecureAppAction abortForUsageViolation:]
+ -[SBInputUISceneController pointInScreenFixedCoordinateSpace:isInsideKeyboardContentOnDisplay:]
+ -[SBInputUISceneController setCurrentlyFocusedOnEmbeddedRemoteAlert:]
+ -[SBLiftToWakeController acquireDisableLiftToWakeAssertionForReason:]
+ -[SBLockElementViewProvider _cancelPendingShake]
+ -[SBLockElementViewProvider _scheduleShake]
+ -[SBLockScreenManager _isThermalCriticalGlyphBloomEligibleDevice]
+ -[SBLockScreenManager _shouldBloomForThermalCriticalUnlock]
+ -[SBLockScreenManager _thermalConditionDidChange:]
+ -[SBLockScreenManager acquireDisableTapToWakeAssertionForReason:]
+ -[SBMainSwitcherControllerCoordinator _cancelDeferredMenuBarPeekTimerForSwitcherContentController:]
+ -[SBMainSwitcherControllerCoordinator centerStatusBarPartFrameForSwitcherContentController:]
+ -[SBMainSwitcherControllerCoordinator centerStatusBarPartFrameShouldBeConsideredInWindowingLayoutForSwitcherContentController:]
+ -[SBMainSwitcherControllerCoordinator inAppStatusBarPartAlphasForSwitcherContentController:]
+ -[SBMainSwitcherControllerCoordinator keyboardFocusController:didAddDeferringRuleForTarget:]
+ -[SBMainSwitcherControllerCoordinator switcherContentController:displayItemIsClassic:]
+ -[SBMainSwitcherControllerCoordinator switcherContentController:displayItemSupportsMedusa:]
+ -[SBMenuBarAppNameProvider .cxx_destruct]
+ -[SBMenuBarAppNameProvider initWithApplicationDisplayName:]
+ -[SBMenuBarAppNameProvider menuBarViewForStatusBar:]
+ -[SBMenuBarBackgroundGradientViewGradientLayerView .cxx_destruct]
+ -[SBMenuBarBackgroundGradientViewGradientLayerView layoutSubviews]
+ -[SBMenuBarHeaderContainerView contentOriginOffset]
+ -[SBMenuBarHeaderContainerView setContentOriginOffset:]
+ -[SBMenuBarManager _acquireHideSystemStatusBarAssertionIfNeeded]
+ -[SBMenuBarManager _applicationNameForOverlayStatusBar]
+ -[SBMenuBarManager _dismissMenuBarAnimated:clearStatusBarAssertions:]
+ -[SBMenuBarManager _dismissMenuBarAnimated:clearStatusBarAssertions:withCompletion:]
+ -[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:clearStatusBarAssertionsForDismissal:]
+ -[SBMenuBarManager _updateHideSystemStatusBarAssertionForCurrentContext]
+ -[SBMenuBarManager appNameMenuBarProvider]
+ -[SBMenuBarManager appNameStatusBarOverlayData]
+ -[SBMenuBarManager dismissWindowControlsMenuForMainMenuPresentation]
+ -[SBMenuBarManager leadingItemSpacingForMenuBarViewController:]
+ -[SBMenuBarManager menuBarUsesStatusBarCenterRegion]
+ -[SBMenuBarManager persistentMenuBarLeadingStyle]
+ -[SBMenuBarManager setPersistentMenuBarLeadingStyle:]
+ -[SBMenuBarManager updateMenuBarEnablementForAppRestrictionChange]
+ -[SBMenuBarManager windowControlsWillBeginPresentingMenuForSceneProvider:]
+ -[SBMenuBarViewController _baseContentOriginOffset]
+ -[SBMenuBarViewController _collapsedContentOriginOffset]
+ -[SBMenuBarViewController _expandedContentOriginOffset]
+ -[SBMenuBarViewController _setMenuViewEnabled:withProvidingAppRestricted:]
+ -[SBMenuBarViewController dismissPresentedMenu]
+ -[SBMenuBarViewController updateMenuEnablementForAppRestrictionChange]
+ -[SBNotificationCarPlayDestination _cleanupQueuesOnWithdrawForRequest:]
+ -[SBNotificationCarPlayDestination _tearDownAnnounceOnWithdrawForLinwoodPreprocessForRequest:]
+ -[SBNotificationCarPlayDestination _tearDownAnnounceOnWithdrawForRequest:revokeSucceeded:]
+ -[SBNotificationCarPlayDestination _withdrawNotificationRequest:tearDownAnnounceForLinwoodPreprocess:]
+ -[SBNotificationCarPlayDestination presentableWillNotAppearAsBanner:withReason:]
+ -[SBRecordingIndicatorSecureLayer _applyCornerRadius]
+ -[SBRecordingIndicatorSecureLayer _commonInit]
+ -[SBRecordingIndicatorSecureLayer _resetSecureIndicatorLayerIndicatorType]
+ -[SBRecordingIndicatorSecureLayer blurRadius]
+ -[SBRecordingIndicatorSecureLayer boundingBoxes]
+ -[SBRecordingIndicatorSecureLayer indicatorType]
+ -[SBRecordingIndicatorSecureLayer initWithCoder:]
+ -[SBRecordingIndicatorSecureLayer initWithLayer:]
+ -[SBRecordingIndicatorSecureLayer init]
+ -[SBRecordingIndicatorSecureLayer layoutSublayers]
+ -[SBRecordingIndicatorSecureLayer setBlurRadius:]
+ -[SBRecordingIndicatorSecureLayer setBounds:]
+ -[SBRecordingIndicatorSecureLayer setIndicatorType:]
+ -[SBRecordingIndicatorSettings observesProximityForBacklightChanges]
+ -[SBRecordingIndicatorSettings setObservesProximityForBacklightChanges:]
+ -[SBRecordingIndicatorSettings setUsesSecureIndicatorLayer:]
+ -[SBRecordingIndicatorSettings usesSecureIndicatorLayer]
+ -[SBRecordingIndicatorView .cxx_destruct]
+ -[SBRecordingIndicatorView _rebuildIndicatorLayer]
+ -[SBRecordingIndicatorView dealloc]
+ -[SBRecordingIndicatorView layoutSubviews]
+ -[SBRecordingIndicatorView setBackgroundColor:]
+ -[SBRecordingIndicatorView settings:changedValueForKey:]
+ -[SBRemoteTransientOverlayHostContentAdapter setShouldUseResizableViewController:]
+ -[SBRemoteTransientOverlayHostContentAdapter shouldUseResizableViewController]
+ -[SBRemoteTransientOverlayViewController isPresentedOnBehalfOfSiri]
+ -[SBRemoteTransientOverlayViewController prepareForActivationWithContext:presentationMode:presentEmbedded:shouldUseResizableViewController:windowScene:completion:]
+ -[SBSAContext _setRequestedIndicatorElevationStyle:]
+ -[SBSAContext requestedIndicatorElevationStyle]
+ -[SBSAContextMutator requestedIndicatorElevationStyle]
+ -[SBSAContextMutator setRequestedIndicatorElevationStyle:]
+ -[SBSafeAreaResolverUtility _windowControlsLayoutForApplicationFrame:screenBounds:application:switcherController:displayEdgeInfo:statusBarHidden:preferredWindowControlsPlacement:]
+ -[SBSafeAreaResolverUtility supportsSolariumSafeAreasRegardlessOfWindowingModeForApplication:switcherController:]
+ -[SBScreenBrightnessHostComponent .cxx_destruct]
+ -[SBScreenBrightnessHostComponent _applyPreferredBrightness:]
+ -[SBScreenBrightnessHostComponent _configureDisplayClientForDisplayConfiguration:]
+ -[SBScreenBrightnessHostComponent _flushPendingBrightnessToScene:]
+ -[SBScreenBrightnessHostComponent _scene:didUpdatePreferredScreenBrightness:]
+ -[SBScreenBrightnessHostComponent _scene:didUpdatePrefersContentProtection:]
+ -[SBScreenBrightnessHostComponent _tearDownDisplayClient]
+ -[SBScreenBrightnessHostComponent _updateScreenBrightness:]
+ -[SBScreenBrightnessHostComponent brightnessUpdate:]
+ -[SBScreenBrightnessHostComponent notifyQueue]
+ -[SBScreenBrightnessHostComponent scene:didUpdateClientSettings:]
+ -[SBScreenBrightnessHostComponent scene:didUpdateSettings:]
+ -[SBScreenBrightnessHostComponent sceneDidInvalidate:withContext:]
+ -[SBScreenBrightnessHostComponent setScene:]
+ -[SBScreenSharingOverlayUISceneController _clientPreferredRootWindowTransform]
+ -[SBScreenSharingOverlayUISceneController _setClientPreferredRootWindowTransform:]
+ -[SBScreenSharingOverlayUISceneController appliedRootWindowTransform]
+ -[SBScreenSharingOverlayUISceneController setAppliedRootWindowTransform:]
+ -[SBSecureIndicatorBacklightCoordinator settings:changedValueForKey:]
+ -[SBSecureIndicatorBacklightCoordinator systemSleepMonitorSleepRequestAborted:]
+ -[SBSecureIndicatorBacklightCoordinator systemSleepMonitorWillWakeFromSleep:]
+ -[SBSecureIndicatorElevationServer .cxx_destruct]
+ -[SBSecureIndicatorElevationServer _recomputeAggregateStyle]
+ -[SBSecureIndicatorElevationServer delegate]
+ -[SBSecureIndicatorElevationServer initWithDelegate:]
+ -[SBSecureIndicatorElevationServer invalidate]
+ -[SBSecureIndicatorElevationServer listener:didReceiveConnection:withContext:]
+ -[SBSecureIndicatorElevationServer requestedElevationStyle]
+ -[SBSuspendedSceneWorkspaceTransaction _addOutstandingProcessIdentity:]
+ -[SBSuspendedSceneWorkspaceTransaction createSceneForSceneEntity:]
+ -[SBSuspendedSceneWorkspaceTransaction main_processDidExit:]
+ -[SBSuspendedSceneWorkspaceTransaction processDidExit:]
+ -[SBSwitcherChamoisSnapPaddingSettings initWithDefaultValues]
+ -[SBSwitcherController _combinedInAppPartAlphas]
+ -[SBSwitcherController addWindowControlsPresentationObserver:]
+ -[SBSwitcherController inAppStatusBarPartAlphasForSwitcherContentController:]
+ -[SBSwitcherController initWithWindowScene:applicationController:supportsResizing:debugName:]
+ -[SBSwitcherController removeWindowControlsPresentationObserver:]
+ -[SBSwitcherController requestInAppStatusBarHiddenAssertionForReason:partAlphas:animated:]
+ -[SBSwitcherController requiresClassicTreatmentForApplication:]
+ -[SBSwitcherController sceneResizingCapabilityForApplication:]
+ -[SBSwitcherController supportsSceneResizingForApplication:]
+ -[SBSwitcherController supportsSceneResizing]
+ -[SBSwitcherController switcherContentController:displayItemIsClassic:]
+ -[SBSwitcherController switcherContentController:displayItemSupportsMedusa:]
+ -[SBSwitcherController updateInAppStatusBarHiddenAssertion:partAlphas:animated:]
+ -[SBSwitcherController windowControlsViewControllerWillBeginPresentingMenu:]
+ -[SBSwitcherFlexibleWindowingSnapPaddingSettings _statusBarHeight]
+ -[SBSwitcherFlexibleWindowingSnapPaddingSettings initWithDefaultValues]
+ -[SBSwitcherWindowingSettings embeddedDisplayChamoisSnapPaddingSettings]
+ -[SBSwitcherWindowingSettings externalDisplayChamoisSnapPaddingSettings]
+ -[SBSwitcherWindowingSettings setEmbeddedDisplayChamoisSnapPaddingSettings:]
+ -[SBSwitcherWindowingSettings setExternalDisplayChamoisSnapPaddingSettings:]
+ -[SBSwitcherWindowingSnapPaddingSettings fullScreenSnapPadding]
+ -[SBSwitcherWindowingSnapPaddingSettings interItemPadding]
+ -[SBSwitcherWindowingSnapPaddingSettings multiAppCenterPadding]
+ -[SBSwitcherWindowingSnapPaddingSettings setFullScreenSnapPadding:]
+ -[SBSwitcherWindowingSnapPaddingSettings setInterItemPadding:]
+ -[SBSwitcherWindowingSnapPaddingSettings setMultiAppCenterPadding:]
+ -[SBSwitcherWindowingSnapPaddingSettings setSingleAppCenterPadding:]
+ -[SBSwitcherWindowingSnapPaddingSettings singleAppCenterPadding]
+ -[SBSystemApertureController setRequestedIndicatorElevationStyle:]
+ -[SBSystemApertureControllerProxy dealloc]
+ -[SBSystemApertureControllerProxy isDisconnected]
+ -[SBSystemApertureControllerProxy setDisconnected:]
+ -[SBSystemApertureControllerProxy setRequestedIndicatorElevationStyle:]
+ -[SBSystemApertureCoordinator _updateRequestedIndicatorElevationStyleForAllControllerProxies]
+ -[SBSystemApertureCoordinator secureIndicatorElevationServer:didChangeRequestedElevationStyle:]
+ -[SBSystemApertureSceneElement delegate]
+ -[SBSystemApertureSceneElement destinationToken]
+ -[SBSystemApertureSceneElement setDelegate:]
+ -[SBSystemApertureViewController requestedIndicatorElevationStyle]
+ -[SBSystemApertureViewController setRequestedIndicatorElevationStyle:]
+ -[SBTapToWakeController acquireDisableTapToWakeAssertionForReason:]
+ -[SBTapToWakeController disableTapToWakeAssertions]
+ -[SBTapToWakeController setDisableTapToWakeAssertions:]
+ -[SBTraitsOrientedResizableContentViewController _canShowWhileLocked]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver .cxx_destruct]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver arbiter]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver componentOrder]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver dealloc]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver description]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver initWithStageResolverBlock:specifierDescription:componentOrder:arbiter:]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver invalidate]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver preferencesType]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver resolveStagePreferencesWithContext:preferencesTree:]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver setSpecifierDescription:]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver specifierDescription]
+ -[SBTraitsPipelineBlockBasedZOrderStageResolver stageResolverBlock]
+ -[SBTraitsPipelineManager newBlockBasedZOrderStageResolver:forRole:]
+ -[SBTransientOverlayViewController isPresentedOnBehalfOfSiri]
+ -[SBWalletPreArmController dealloc]
+ -[SBWalletPreArmController descriptionBuilderWithMultilinePrefix:]
+ -[SBWalletPreArmController descriptionWithMultilinePrefix:]
+ -[SBWalletPreArmController description]
+ -[SBWalletPreArmController succinctDescriptionBuilder]
+ -[SBWalletPreArmController succinctDescription]
+ -[SBWindowScene isResizableAppHostingWindowScene]
+ -[SpringBoard coverSheetGrabberManager]
+ -[_SBManualDisplayActivationShieldWindow _reconsiderButtonEnablement]
+ -[_SBManualDisplayActivationShieldWindow acquireDisableButtonsAssertionForReason:]
+ -[_SBSecureIndicatorElevationConnectionAssertion .cxx_destruct]
+ -[_SBSecureIndicatorElevationConnectionAssertion server]
+ -[_SBSecureIndicatorElevationConnectionAssertion setElevationStyleNum:]
+ -[_SBSecureIndicatorElevationConnectionAssertion setServer:]
+ -[_SBSecureIndicatorElevationConnectionAssertion setStyle:]
+ -[_SBSecureIndicatorElevationConnectionAssertion style]
+ GCC_except_table1043
+ GCC_except_table1050
+ GCC_except_table1052
+ GCC_except_table1054
+ GCC_except_table1056
+ GCC_except_table1058
+ GCC_except_table1060
+ GCC_except_table1062
+ GCC_except_table171
+ GCC_except_table197
+ GCC_except_table201
+ GCC_except_table211
+ GCC_except_table240
+ GCC_except_table265
+ GCC_except_table275
+ GCC_except_table290
+ GCC_except_table293
+ GCC_except_table321
+ GCC_except_table347
+ GCC_except_table349
+ GCC_except_table388
+ GCC_except_table401
+ GCC_except_table413
+ GCC_except_table437
+ GCC_except_table443
+ GCC_except_table449
+ GCC_except_table455
+ GCC_except_table509
+ GCC_except_table543
+ GCC_except_table551
+ GCC_except_table553
+ GCC_except_table556
+ GCC_except_table558
+ GCC_except_table566
+ GCC_except_table576
+ GCC_except_table579
+ GCC_except_table580
+ GCC_except_table586
+ GCC_except_table590
+ GCC_except_table620
+ GCC_except_table674
+ GCC_except_table709
+ GCC_except_table787
+ GCC_except_table813
+ GCC_except_table816
+ GCC_except_table856
+ GCC_except_table898
+ GCC_except_table900
+ GCC_except_table939
+ GCC_except_table950
+ GCC_except_table997
+ _NSStringFromSBProximitySensorSuspensionMode
+ _OBJC_CLASS_$_BLSInvalidOnSystemSleepAttribute
+ _OBJC_CLASS_$_SBCoreSmartPowerNapHIDCoordinator
+ _OBJC_CLASS_$_SBExternalDisplayLayoutPublisherFactory
+ _OBJC_CLASS_$_SBInputUISceneControllerExtension
+ _OBJC_CLASS_$_SBMenuBarAppNameProvider
+ _OBJC_CLASS_$_SBRecordingIndicatorSecureLayer
+ _OBJC_CLASS_$_SBSSecureIndicatorElevationAssertionServiceSpecification
+ _OBJC_CLASS_$_SBScreenBrightnessHostComponent
+ _OBJC_CLASS_$_SBScreenBrightnessSceneExtension
+ _OBJC_CLASS_$_SBSecureIndicatorElevationServer
+ _OBJC_CLASS_$_SBSwitcherChamoisSnapPaddingSettings
+ _OBJC_CLASS_$_SBSwitcherFlexibleWindowingSnapPaddingSettings
+ _OBJC_CLASS_$_SBTraitsPipelineBlockBasedZOrderStageResolver
+ _OBJC_CLASS_$_SBUISActivityMetrics
+ _OBJC_CLASS_$__PMCoreSmartPowerNap
+ _OBJC_CLASS_$__SBSecureIndicatorElevationConnectionAssertion
+ _OBJC_IVAR_$_SBActivityMetrics._activeLayoutDirection
+ _OBJC_IVAR_$_SBActivitySystemApertureSceneHandle._activeLayoutDirection
+ _OBJC_IVAR_$_SBAlwaysOnTelemetryEmitter._mq_currentPresentationBundleIdentifiers
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._alwaysOnInactivityTimeoutActive
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._alwaysOnInactivityTimer
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._alwaysOnSuppressed
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._ambientDefaults
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._lockScreenManager
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._motionDetected
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._motionDetectionIdleTimerAssertion
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._motionDetectionWakeAssertion
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._motionDetectionWakeAttributeMonitor
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._presenceDetectionController
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._presenceDetectionWakeAssertion
+ _OBJC_IVAR_$_SBAppResizingCoordinator._resizingPossible
+ _OBJC_IVAR_$_SBApplicationInfo._couldSupportMedusa
+ _OBJC_IVAR_$_SBAssistantIslandSettings._floatingPresentationStatusBarOutset
+ _OBJC_IVAR_$_SBAssistantIslandSettings._homeScreenTranslationEnabled
+ _OBJC_IVAR_$_SBAssistantIslandSettings._listeningThinkingWaveActiveGaussianRadius
+ _OBJC_IVAR_$_SBAssistantIslandSettings._listeningThinkingWaveInitialGaussianRadius
+ _OBJC_IVAR_$_SBAssistantIslandSettings._listeningThinkingWaveLensingAmount
+ _OBJC_IVAR_$_SBAssistantIslandSettings._listeningThinkingWaveLensingHeight
+ _OBJC_IVAR_$_SBAssistantIslandSettings._listeningThinkingWaveVariableBlurLocation
+ _OBJC_IVAR_$_SBAssistantIslandSettings._listeningThinkingWaveVariableBlurRadius
+ _OBJC_IVAR_$_SBAssistantIslandSettings._systemApertureUnifiedAnimationEnabled
+ _OBJC_IVAR_$_SBAssistantIslandStageController._currentKeyboardProxyOwner
+ _OBJC_IVAR_$_SBAssistantIslandStageController._hasStatusBarWindowLevelOverride
+ _OBJC_IVAR_$_SBAssistantIslandStageController._keyboardFocusSuppressionAssertion
+ _OBJC_IVAR_$_SBAssistantIslandStageController._residentInactiveSettleGenerationCount
+ _OBJC_IVAR_$_SBAssistantIslandStageController._stageQuiescentPresentationState
+ _OBJC_IVAR_$_SBAssistantIslandStageCoordinator._clientCrashCount
+ _OBJC_IVAR_$_SBAssistantIslandStageCoordinator._prewarmDisabledUntilUnlock
+ _OBJC_IVAR_$_SBAssistantIslandStageCoordinator._rapidClientCrashCount
+ _OBJC_IVAR_$_SBAssistantIslandStageCoordinator._zOrderStageResolverTokensByWindowScene
+ _OBJC_IVAR_$_SBAssistantIslandStageGestureManager._systemApertureIsEmpty
+ _OBJC_IVAR_$_SBAssistantIslandStagePlaceholderController._finalGestureState
+ _OBJC_IVAR_$_SBBannerTransitionSettings._customBannerTransitionStyleGlass_cornerAnchorYOffset
+ _OBJC_IVAR_$_SBBannerTransitionSettings._customBannerTransitionStyleGlass_morphHandleCornerRadius
+ _OBJC_IVAR_$_SBBannerTransitionSettings._customBannerTransitionStyleGlass_morphHandleCrossFadeStartFraction
+ _OBJC_IVAR_$_SBCoreSmartPowerNapHIDCoordinator._callbackQueue
+ _OBJC_IVAR_$_SBCoreSmartPowerNapHIDCoordinator._cspn
+ _OBJC_IVAR_$_SBCoreSmartPowerNapHIDCoordinator._digitizerAssertion
+ _OBJC_IVAR_$_SBCoreSmartPowerNapHIDCoordinator._lastState
+ _OBJC_IVAR_$_SBCoreSmartPowerNapHIDCoordinator._started
+ _OBJC_IVAR_$_SBCoreSmartPowerNapHIDCoordinator._userPresenceLatch
+ _OBJC_IVAR_$_SBCoreSmartPowerNapHIDCoordinator._windowSceneManager
+ _OBJC_IVAR_$_SBCoverSheetGrabberManager._appFlyInDidSettle
+ _OBJC_IVAR_$_SBCoverSheetGrabberManager._appFlyInDidSettleTimestamp
+ _OBJC_IVAR_$_SBCoverSheetGrabberManager._appFlyInSettleFallbackTimer
+ _OBJC_IVAR_$_SBCoverSheetGrabberManager._bannerHandoffInstantAppear
+ _OBJC_IVAR_$_SBCoverSheetGrabberManager._isWaitingForAppFlyInSettle
+ _OBJC_IVAR_$_SBCoverSheetGrabberManager._suppressTeachPulse
+ _OBJC_IVAR_$_SBCoverSheetPresentationManager._dismissalCommitted
+ _OBJC_IVAR_$_SBCoverSheetPresentationManager._hasPostedDismissalNearlyCompleteNotification
+ _OBJC_IVAR_$_SBCoverSheetPresentationManager._lastSettledPresentedState
+ _OBJC_IVAR_$_SBCoverSheetToAppSwitcherModifier._appFlyInPeakScaleVelocityMagnitude
+ _OBJC_IVAR_$_SBCoverSheetToAppSwitcherModifier._appFlyInSettleDeadline
+ _OBJC_IVAR_$_SBCoverSheetToAppSwitcherModifier._appFlyInSettleStartTime
+ _OBJC_IVAR_$_SBCoverSheetToAppSwitcherModifier._displayLink
+ _OBJC_IVAR_$_SBDeviceApplicationSceneHandle._lastResizeDisplayExtent
+ _OBJC_IVAR_$_SBDeviceApplicationSceneHandle._lastResizeDisplayIdentity
+ _OBJC_IVAR_$_SBDeviceApplicationSceneHandle._resizeDisplayGeneration
+ _OBJC_IVAR_$_SBDeviceApplicationSceneViewController._currentOverridePartAlphas
+ _OBJC_IVAR_$_SBExternalDisplayService._layoutPublisherFactory
+ _OBJC_IVAR_$_SBExternalDisplayService._rootToLayoutPublisher
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._lastCenterStatusBarFrame
+ _OBJC_IVAR_$_SBGlassBannerTransitionAnimator._morphFadedContentViews
+ _OBJC_IVAR_$_SBGlassBannerTransitionAnimator._morphHandleContainer
+ _OBJC_IVAR_$_SBHIDUISensorModeAssertion._proximitySuspensionMode
+ _OBJC_IVAR_$_SBInAppStatusBarHiddenAssertion._partAlphas
+ _OBJC_IVAR_$_SBInputUISceneController._currentlyFocusedOnEmbeddedRemoteAlert
+ _OBJC_IVAR_$_SBKeyboardFocusLockReason._creationOrder
+ _OBJC_IVAR_$_SBLiftToWakeController._disableLiftToWakeAssertions
+ _OBJC_IVAR_$_SBLockElementViewProvider._pendingShakeBlock
+ _OBJC_IVAR_$_SBMainSwitcherControllerCoordinator._activatingSwitcherTransitionScene
+ _OBJC_IVAR_$_SBMainSwitcherControllerCoordinator._menuBarDeferredPeekTimersByWindowScene
+ _OBJC_IVAR_$_SBMenuBarAppNameProvider._activationView
+ _OBJC_IVAR_$_SBMenuBarBackgroundGradientViewGradientLayerView._alphaFadeMaskLayer
+ _OBJC_IVAR_$_SBMenuBarBackgroundGradientViewGradientLayerView._menuBarSettings
+ _OBJC_IVAR_$_SBMenuBarHeaderContainerView._contentOriginOffset
+ _OBJC_IVAR_$_SBMenuBarManager._persistentMenuBarLeadingStyle
+ _OBJC_IVAR_$_SBRecordingIndicatorSecureLayer._blurRadius
+ _OBJC_IVAR_$_SBRecordingIndicatorSecureLayer._indicatorType
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._observesProximityForBacklightChanges
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._usesSecureIndicatorLayer
+ _OBJC_IVAR_$_SBRecordingIndicatorView._indicatorLayer
+ _OBJC_IVAR_$_SBRemoteTransientOverlayHostContentAdapter._shouldUseResizableViewController
+ _OBJC_IVAR_$_SBSAContext._requestedIndicatorElevationStyle
+ _OBJC_IVAR_$_SBSARenderingAndCloningPreferencesProvider._previousHighLevelCurtainRenderingStyle
+ _OBJC_IVAR_$_SBSASettlingBehaviorProvider._heldCollisionContainerDescriptions
+ _OBJC_IVAR_$_SBScreenBrightnessHostComponent._displayClient
+ _OBJC_IVAR_$_SBScreenBrightnessHostComponent._lastNotifiedBrightness
+ _OBJC_IVAR_$_SBScreenBrightnessHostComponent._notifyQueue
+ _OBJC_IVAR_$_SBScreenBrightnessHostComponent._pendingBrightness
+ _OBJC_IVAR_$_SBScreenSharingOverlayUISceneController._clientPreferredRootWindowTransform
+ _OBJC_IVAR_$_SBSecureIndicatorElevationServer._assertions
+ _OBJC_IVAR_$_SBSecureIndicatorElevationServer._assertionsLock
+ _OBJC_IVAR_$_SBSecureIndicatorElevationServer._connectionListener
+ _OBJC_IVAR_$_SBSecureIndicatorElevationServer._connectionQueue
+ _OBJC_IVAR_$_SBSecureIndicatorElevationServer._connections
+ _OBJC_IVAR_$_SBSecureIndicatorElevationServer._delegate
+ _OBJC_IVAR_$_SBSecureIndicatorElevationServer._requestedElevationStyle
+ _OBJC_IVAR_$_SBSwitcherController._supportsResizing
+ _OBJC_IVAR_$_SBSwitcherController._windowControlsPresentationObservers
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._embeddedDisplayChamoisSnapPaddingSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._externalDisplayChamoisSnapPaddingSettings
+ _OBJC_IVAR_$_SBSwitcherWindowingSnapPaddingSettings._fullScreenSnapPadding
+ _OBJC_IVAR_$_SBSwitcherWindowingSnapPaddingSettings._interItemPadding
+ _OBJC_IVAR_$_SBSwitcherWindowingSnapPaddingSettings._multiAppCenterPadding
+ _OBJC_IVAR_$_SBSwitcherWindowingSnapPaddingSettings._singleAppCenterPadding
+ _OBJC_IVAR_$_SBSystemApertureControllerProxy._disconnected
+ _OBJC_IVAR_$_SBSystemApertureCoordinator._requestedIndicatorElevationStyle
+ _OBJC_IVAR_$_SBSystemApertureCoordinator._secureIndicatorElevationServer
+ _OBJC_IVAR_$_SBSystemApertureSceneElement._delegate
+ _OBJC_IVAR_$_SBSystemApertureViewController._requestedIndicatorElevationStyle
+ _OBJC_IVAR_$_SBTapToWakeController._disableTapToWakeAssertions
+ _OBJC_IVAR_$_SBTraitsPipelineBlockBasedZOrderStageResolver._arbiter
+ _OBJC_IVAR_$_SBTraitsPipelineBlockBasedZOrderStageResolver._componentOrder
+ _OBJC_IVAR_$_SBTraitsPipelineBlockBasedZOrderStageResolver._isValid
+ _OBJC_IVAR_$_SBTraitsPipelineBlockBasedZOrderStageResolver._specifierDescription
+ _OBJC_IVAR_$_SBTraitsPipelineBlockBasedZOrderStageResolver._stageResolverBlock
+ _OBJC_IVAR_$_SBWalletPreArmController._stateCaptureAssertion
+ _OBJC_IVAR_$_SpringBoard._coreSmartPowerNapHIDCoordinator
+ _OBJC_IVAR_$__SBManualDisplayActivationShieldWindow._disableButtonsAssertions
+ _OBJC_IVAR_$__SBSecureIndicatorElevationConnectionAssertion._server
+ _OBJC_IVAR_$__SBSecureIndicatorElevationConnectionAssertion._style
+ _OBJC_METACLASS_$_SBCoreSmartPowerNapHIDCoordinator
+ _OBJC_METACLASS_$_SBExternalDisplayLayoutPublisherFactory
+ _OBJC_METACLASS_$_SBInputUISceneControllerExtension
+ _OBJC_METACLASS_$_SBMenuBarAppNameProvider
+ _OBJC_METACLASS_$_SBRecordingIndicatorSecureLayer
+ _OBJC_METACLASS_$_SBScreenBrightnessHostComponent
+ _OBJC_METACLASS_$_SBScreenBrightnessSceneExtension
+ _OBJC_METACLASS_$_SBSecureIndicatorElevationServer
+ _OBJC_METACLASS_$_SBSwitcherChamoisSnapPaddingSettings
+ _OBJC_METACLASS_$_SBSwitcherFlexibleWindowingSnapPaddingSettings
+ _OBJC_METACLASS_$_SBTraitsPipelineBlockBasedZOrderStageResolver
+ _OBJC_METACLASS_$__SBSecureIndicatorElevationConnectionAssertion
+ _SBCoverSheetAppFlyInDidSettleNotification
+ _SBCoverSheetDismissalNearlyCompleteIsOverAppKey
+ _SBCoverSheetDismissalNearlyCompleteNotification
+ _SBCoverSheetWillPresentForUserGestureKey
+ _SBFDIDeviceControlEntitlement
+ _SBMobileBarCodeFactoryApp
+ _SBRecordingIndicatorLayerApplyBlurRadius
+ _SBRecordingIndicatorLayerCreate
+ _SBSAResolvedIndicatorElevationStyle
+ _SBSceneResizingCapabilityDescription
+ _SBScreenBrightnessSharedCBClient.onceToken
+ _SBScreenBrightnessSharedCBClient.sharedClient
+ _SBScreenBrightnessUsesCBDisplayClient.onceToken
+ _SBScreenBrightnessUsesCBDisplayClient.usesCBDisplayClient
+ _SBSecureIndicatorElevationEntitlement
+ _UIApplicationSceneStringForInterfaceOrientationMode
+ __OBJC_$_CATEGORY_UIWindow_$_FBSDisplayConfiguration
+ __OBJC_$_CLASS_METHODS_SBApplication(SwitcherCapabilitiesProvidedByClassic|Classic|Classic_Private|Classic_Private_ForBaseClassAndSceneHandleOnly|Classic_PrivateForUnitTestsOnly|Classic_Internal|Snapshots|SnapshotSorting|ChamoisCapabilities|SwitcherCapabilities|SBWebApplication|DefaultImage|DefaultImage_Naming|DefaultImage_ManifestIngestion|Identity)
+ __OBJC_$_CLASS_METHODS_SBCoreSmartPowerNapHIDCoordinator
+ __OBJC_$_CLASS_METHODS_SBInputUISceneControllerExtension
+ __OBJC_$_CLASS_METHODS_SBScreenBrightnessSceneExtension
+ __OBJC_$_INSTANCE_METHODS_FBScene(SBVisibilitySceneExtension_ForSceneManager|SBSUIHomeScreenIconStyle|InputUISceneController|LocalSynchronous|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBProductivityGestureDestination|SafeAreaResolverExtensionDelegate|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
+ __OBJC_$_INSTANCE_METHODS_SBApplication(SwitcherCapabilitiesProvidedByClassic|Classic|Classic_Private|Classic_Private_ForBaseClassAndSceneHandleOnly|Classic_PrivateForUnitTestsOnly|Classic_Internal|Snapshots|SnapshotSorting|ChamoisCapabilities|SwitcherCapabilities|SBWebApplication|DefaultImage|DefaultImage_Naming|DefaultImage_ManifestIngestion|Identity)
+ __OBJC_$_INSTANCE_METHODS_SBChainableModifierEventResponse(SBWindowingModifierResponse|SBSwitcherModifierEventResponse)
+ __OBJC_$_INSTANCE_METHODS_SBCoreSmartPowerNapHIDCoordinator
+ __OBJC_$_INSTANCE_METHODS_SBExternalDisplayLayoutPublisherFactory
+ __OBJC_$_INSTANCE_METHODS_SBMenuBarAppNameProvider
+ __OBJC_$_INSTANCE_METHODS_SBRecordingIndicatorSecureLayer
+ __OBJC_$_INSTANCE_METHODS_SBScreenBrightnessHostComponent
+ __OBJC_$_INSTANCE_METHODS_SBSecureIndicatorElevationServer
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherChamoisSnapPaddingSettings
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherFlexibleWindowingSnapPaddingSettings
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherModifier(WindowingModifier|SharedModifierUtilities)
+ __OBJC_$_INSTANCE_METHODS_SBTraitsPipelineBlockBasedZOrderStageResolver
+ __OBJC_$_INSTANCE_METHODS_UIWindow(FBSDisplayConfiguration|SBWindowScene|SelfHosting|TRAArbiterExtensions|SBWindow)
+ __OBJC_$_INSTANCE_METHODS__SBSecureIndicatorElevationConnectionAssertion
+ __OBJC_$_INSTANCE_VARIABLES_SBCoreSmartPowerNapHIDCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_SBMenuBarAppNameProvider
+ __OBJC_$_INSTANCE_VARIABLES_SBRecordingIndicatorSecureLayer
+ __OBJC_$_INSTANCE_VARIABLES_SBRecordingIndicatorView
+ __OBJC_$_INSTANCE_VARIABLES_SBScreenBrightnessHostComponent
+ __OBJC_$_INSTANCE_VARIABLES_SBSecureIndicatorElevationServer
+ __OBJC_$_INSTANCE_VARIABLES_SBTraitsPipelineBlockBasedZOrderStageResolver
+ __OBJC_$_INSTANCE_VARIABLES__SBSecureIndicatorElevationConnectionAssertion
+ __OBJC_$_PROP_LIST_CBDisplayBrightnessClientObserver
+ __OBJC_$_PROP_LIST_SAUIContentTransitioning
+ __OBJC_$_PROP_LIST_SBCoreSmartPowerNapHIDCoordinator
+ __OBJC_$_PROP_LIST_SBInputUISceneControllerExtensionSettings
+ __OBJC_$_PROP_LIST_SBMenuBarAppNameProvider
+ __OBJC_$_PROP_LIST_SBRecordingIndicatorSecureLayer
+ __OBJC_$_PROP_LIST_SBScreenBrightnessHostComponent
+ __OBJC_$_PROP_LIST_SBSecureIndicatorElevationServer
+ __OBJC_$_PROP_LIST_SBSuspendedSceneWorkspaceTransaction
+ __OBJC_$_PROP_LIST_SBTraitsPipelineBlockBasedZOrderStageResolver
+ __OBJC_$_PROP_LIST_UITraitEnvironment
+ __OBJC_$_PROP_LIST__SBSecureIndicatorElevationConnectionAssertion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBDisplayBrightnessClientObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CBDisplayBrightnessClientObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBInputUISceneControllerExtensionSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBSystemApertureSceneElementDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UIKeyboardInputRehostingSceneHostObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UISceneRenderingEnvironmentHostObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBRecordingIndicatorLayering
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSSecureIndicatorElevationAssertionServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSecureIndicatorElevationServerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBWindowControlsPresentationObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_UITraitEnvironment
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UISceneRenderingEnvironmentHostObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBDisplayBrightnessClientObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBInputUISceneControllerExtensionSettings
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBRecordingIndicatorLayering
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSSecureIndicatorElevationAssertionServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSecureIndicatorElevationServerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSystemApertureSceneElementDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBWindowControlsPresentationObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UITraitEnvironment
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UISceneRenderingEnvironmentHostObserver
+ __OBJC_$_PROTOCOL_REFS_CBDisplayBrightnessClientObserver
+ __OBJC_$_PROTOCOL_REFS_SBInputUISceneControllerExtensionSettings
+ __OBJC_$_PROTOCOL_REFS_SBRecordingIndicatorLayering
+ __OBJC_$_PROTOCOL_REFS_SBSSecureIndicatorElevationAssertionServerInterface
+ __OBJC_$_PROTOCOL_REFS_SBSecureIndicatorElevationServerDelegate
+ __OBJC_$_PROTOCOL_REFS_SBSystemApertureSceneElementDelegate
+ __OBJC_$_PROTOCOL_REFS_SBWindowControlsPresentationObserver
+ __OBJC_$_PROTOCOL_REFS_UITraitEnvironment
+ __OBJC_$_PROTOCOL_REFS__UISceneRenderingEnvironmentHostObserver
+ __OBJC_CLASS_PROTOCOLS_$_FBScene(SBVisibilitySceneExtension_ForSceneManager|SBSUIHomeScreenIconStyle|InputUISceneController|LocalSynchronous|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBProductivityGestureDestination|SafeAreaResolverExtensionDelegate|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
+ __OBJC_CLASS_PROTOCOLS_$_SBApplication(SwitcherCapabilitiesProvidedByClassic|Classic|Classic_Private|Classic_Private_ForBaseClassAndSceneHandleOnly|Classic_PrivateForUnitTestsOnly|Classic_Internal|Snapshots|SnapshotSorting|ChamoisCapabilities|SwitcherCapabilities|SBWebApplication|DefaultImage|DefaultImage_Naming|DefaultImage_ManifestIngestion|Identity)
+ __OBJC_CLASS_PROTOCOLS_$_SBMenuBarAppNameProvider
+ __OBJC_CLASS_PROTOCOLS_$_SBRecordingIndicatorSecureLayer
+ __OBJC_CLASS_PROTOCOLS_$_SBScreenBrightnessHostComponent
+ __OBJC_CLASS_PROTOCOLS_$_SBSecureIndicatorElevationServer
+ __OBJC_CLASS_PROTOCOLS_$_SBSuspendedSceneWorkspaceTransaction
+ __OBJC_CLASS_PROTOCOLS_$_SBTraitsPipelineBlockBasedZOrderStageResolver
+ __OBJC_CLASS_PROTOCOLS_$__SBSecureIndicatorElevationConnectionAssertion
+ __OBJC_CLASS_RO_$_SBCoreSmartPowerNapHIDCoordinator
+ __OBJC_CLASS_RO_$_SBExternalDisplayLayoutPublisherFactory
+ __OBJC_CLASS_RO_$_SBInputUISceneControllerExtension
+ __OBJC_CLASS_RO_$_SBMenuBarAppNameProvider
+ __OBJC_CLASS_RO_$_SBRecordingIndicatorSecureLayer
+ __OBJC_CLASS_RO_$_SBScreenBrightnessHostComponent
+ __OBJC_CLASS_RO_$_SBScreenBrightnessSceneExtension
+ __OBJC_CLASS_RO_$_SBSecureIndicatorElevationServer
+ __OBJC_CLASS_RO_$_SBSwitcherChamoisSnapPaddingSettings
+ __OBJC_CLASS_RO_$_SBSwitcherFlexibleWindowingSnapPaddingSettings
+ __OBJC_CLASS_RO_$_SBTraitsPipelineBlockBasedZOrderStageResolver
+ __OBJC_CLASS_RO_$__SBSecureIndicatorElevationConnectionAssertion
+ __OBJC_LABEL_PROTOCOL_$_CBDisplayBrightnessClientObserver
+ __OBJC_LABEL_PROTOCOL_$_SBInputUISceneControllerExtensionSettings
+ __OBJC_LABEL_PROTOCOL_$_SBRecordingIndicatorLayering
+ __OBJC_LABEL_PROTOCOL_$_SBSSecureIndicatorElevationAssertionServerInterface
+ __OBJC_LABEL_PROTOCOL_$_SBSecureIndicatorElevationServerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBSystemApertureSceneElementDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBWindowControlsPresentationObserver
+ __OBJC_LABEL_PROTOCOL_$_UITraitEnvironment
+ __OBJC_LABEL_PROTOCOL_$__UISceneRenderingEnvironmentHostObserver
+ __OBJC_METACLASS_RO_$_SBCoreSmartPowerNapHIDCoordinator
+ __OBJC_METACLASS_RO_$_SBExternalDisplayLayoutPublisherFactory
+ __OBJC_METACLASS_RO_$_SBInputUISceneControllerExtension
+ __OBJC_METACLASS_RO_$_SBMenuBarAppNameProvider
+ __OBJC_METACLASS_RO_$_SBRecordingIndicatorSecureLayer
+ __OBJC_METACLASS_RO_$_SBScreenBrightnessHostComponent
+ __OBJC_METACLASS_RO_$_SBScreenBrightnessSceneExtension
+ __OBJC_METACLASS_RO_$_SBSecureIndicatorElevationServer
+ __OBJC_METACLASS_RO_$_SBSwitcherChamoisSnapPaddingSettings
+ __OBJC_METACLASS_RO_$_SBSwitcherFlexibleWindowingSnapPaddingSettings
+ __OBJC_METACLASS_RO_$_SBTraitsPipelineBlockBasedZOrderStageResolver
+ __OBJC_METACLASS_RO_$__SBSecureIndicatorElevationConnectionAssertion
+ __OBJC_PROTOCOL_$_CBDisplayBrightnessClientObserver
+ __OBJC_PROTOCOL_$_SBInputUISceneControllerExtensionSettings
+ __OBJC_PROTOCOL_$_SBRecordingIndicatorLayering
+ __OBJC_PROTOCOL_$_SBSSecureIndicatorElevationAssertionServerInterface
+ __OBJC_PROTOCOL_$_SBSecureIndicatorElevationServerDelegate
+ __OBJC_PROTOCOL_$_SBSystemApertureSceneElementDelegate
+ __OBJC_PROTOCOL_$_SBWindowControlsPresentationObserver
+ __OBJC_PROTOCOL_$_UITraitEnvironment
+ __OBJC_PROTOCOL_$__UISceneRenderingEnvironmentHostObserver
+ __OBJC_PROTOCOL_REFERENCE_$_SBInputUISceneControllerExtensionSettings
+ __SBF_Private_Is
+ ___101-[SBMainSwitcherControllerCoordinator _configureRequest:forSwitcherTransitionRequest:withEventLabel:]_block_invoke_6
+ ___106-[SBFluidSwitcherViewController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:]_block_invoke
+ ___125-[SBHomeScreenService swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]_block_invoke
+ ___125-[SBHomeScreenService swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]_block_invoke_2
+ ___179-[SBSafeAreaResolverUtility _windowControlsLayoutForApplicationFrame:screenBounds:application:switcherController:displayEdgeInfo:statusBarHidden:preferredWindowControlsPlacement:]_block_invoke
+ ___179-[SBSafeAreaResolverUtility _windowControlsLayoutForApplicationFrame:screenBounds:application:switcherController:displayEdgeInfo:statusBarHidden:preferredWindowControlsPlacement:]_block_invoke_2
+ ___179-[SBSafeAreaResolverUtility _windowControlsLayoutForApplicationFrame:screenBounds:application:switcherController:displayEdgeInfo:statusBarHidden:preferredWindowControlsPlacement:]_block_invoke_3
+ ___179-[SBSafeAreaResolverUtility _windowControlsLayoutForApplicationFrame:screenBounds:application:switcherController:displayEdgeInfo:statusBarHidden:preferredWindowControlsPlacement:]_block_invoke_4
+ ___188-[SBAssistantIslandStageCoordinator fetchOrCreateNewStageControllerForWindowScene:state:chatSessionIdentifier:spotlightInvocationSource:dismissesControlCenterIfVisible:actions:completion:]_block_invoke
+ ___188-[SBAssistantIslandStageCoordinator fetchOrCreateNewStageControllerForWindowScene:state:chatSessionIdentifier:spotlightInvocationSource:dismissesControlCenterIfVisible:actions:completion:]_block_invoke_2
+ ___23-[SBSAContext isEqual:]_block_invoke_36
+ ___42-[SBCoreSmartPowerNapHIDCoordinator start]_block_invoke
+ ___43-[SBLockElementViewProvider _scheduleShake]_block_invoke
+ ___48-[SBSwitcherController _combinedInAppPartAlphas]_block_invoke
+ ___50-[SBCoreSmartPowerNapHIDCoordinator _handleState:]_block_invoke
+ ___52-[SBAssistantIslandStageCoordinator processDidExit:]_block_invoke
+ ___52-[SBScreenBrightnessHostComponent brightnessUpdate:]_block_invoke
+ ___53-[SBSecureIndicatorElevationServer initWithDelegate:]_block_invoke
+ ___55-[SBSuspendedSceneWorkspaceTransaction processDidExit:]_block_invoke
+ ___56-[SBAssistantIslandStageCoordinator _noteClientDidCrash]_block_invoke
+ ___56-[SBAssistantIslandStageCoordinator _noteClientDidCrash]_block_invoke_2
+ ___59-[SBAssistantIslandStageController _coverSheetWillPresent:]_block_invoke
+ ___59-[SBAssistantIslandStageController _updateResidentInactive]_block_invoke
+ ___59-[SBAssistantIslandStageCoordinator windowSceneDidConnect:]_block_invoke
+ ___60-[SBAssistantIslandStageController _updateKeyboardPresenter]_block_invoke_4
+ ___60-[SBCoverSheetGrabberManager _beginWaitingForAppFlyInSettle]_block_invoke
+ ___60-[SBNotificationCarPlayDestination postNotificationRequest:]_block_invoke_2
+ ___60-[SBSecureIndicatorElevationServer _recomputeAggregateStyle]_block_invoke
+ ___63-[SBAssistantIslandStageController sceneContentStateDidChange:]_block_invoke
+ ___65-[SBAssistantIslandStageController _sceneClientSettingsDidUpdate]_block_invoke_6
+ ___65-[SBAssistantIslandStageController _sceneClientSettingsDidUpdate]_block_invoke_7
+ ___65-[SBLockScreenManager _isThermalCriticalGlyphBloomEligibleDevice]_block_invoke
+ ___66-[SBAssistantIslandStageCoordinator processManager:didAddProcess:]_block_invoke
+ ___66-[SBSuspendedSceneWorkspaceTransaction createSceneForSceneEntity:]_block_invoke
+ ___66-[SBSuspendedSceneWorkspaceTransaction createSceneForSceneEntity:]_block_invoke_2
+ ___66-[SBSuspendedSceneWorkspaceTransaction createSceneForSceneEntity:]_block_invoke_3
+ ___66-[SBSuspendedSceneWorkspaceTransaction createSceneForSceneEntity:]_block_invoke_4
+ ___66-[SBSuspendedSceneWorkspaceTransaction createSceneForSceneEntity:]_block_invoke_5
+ ___66-[SBSwitcherFlexibleWindowingSnapPaddingSettings _statusBarHeight]_block_invoke
+ ___67-[SBAssistantIslandStageCoordinator keybag:extendedStateDidChange:]_block_invoke
+ ___67-[SBTapToWakeController acquireDisableTapToWakeAssertionForReason:]_block_invoke
+ ___68-[SBAssistantIslandStageController updateSpotlightInvocationSource:]_block_invoke
+ ___69-[SBAssistantIslandStageCoordinator processManager:didRemoveProcess:]_block_invoke
+ ___69-[SBLiftToWakeController acquireDisableLiftToWakeAssertionForReason:]_block_invoke
+ ___71-[SBAssistantIslandStageController _updateSystemApertureAnimationStyle]_block_invoke
+ ___71-[SBHomeScreenController dismissHomeScreenOverlaysAnimated:completion:]_block_invoke_4
+ ___72-[SBAssistantIslandStageController _updateListeningThinkingWaveSettings]_block_invoke
+ ___72-[SBMenuBarManager _updateHideSystemStatusBarAssertionForCurrentContext]_block_invoke
+ ___73-[SBAssistantIslandStageCoordinator _assistantIslandEnablementDidChange:]_block_invoke
+ ___73-[SBWalletPreArmController initWithWalletPresentation:biometricResource:]_block_invoke
+ ___77-[SBAssistantIslandStageController _updateHostingDisplayBacklightStateActive]_block_invoke
+ ___78-[SBSecureIndicatorElevationServer listener:didReceiveConnection:withContext:]_block_invoke
+ ___78-[SBSecureIndicatorElevationServer listener:didReceiveConnection:withContext:]_block_invoke_2
+ ___79-[SBHomeScreenController _dismissalCompletionLeavingGroup:foldingFinishedInto:]_block_invoke
+ ___82-[SBAssistantIslandStagePlaceholderController _updatePlaceholderIgnoreEvaluation:]_block_invoke_5
+ ___82-[SBAssistantIslandStagePlaceholderController _updatePlaceholderIgnoreEvaluation:]_block_invoke_6
+ ___82-[_SBManualDisplayActivationShieldWindow acquireDisableButtonsAssertionForReason:]_block_invoke
+ ___83-[SBMainSwitcherControllerCoordinator switcherContentControllerWantsToPeekMenuBar:]_block_invoke
+ ___84-[SBDeviceApplicationSceneViewController _configureStatusBarWithCurrentStyleRequest]_block_invoke_3
+ ___84-[SBDeviceApplicationSceneViewController _configureStatusBarWithCurrentStyleRequest]_block_invoke_4
+ ___84-[SBMenuBarManager _dismissMenuBarAnimated:clearStatusBarAssertions:withCompletion:]_block_invoke
+ ___84-[SBMenuBarManager _dismissMenuBarAnimated:clearStatusBarAssertions:withCompletion:]_block_invoke_2
+ ___84-[SBMenuBarManager _dismissMenuBarAnimated:clearStatusBarAssertions:withCompletion:]_block_invoke_3
+ ___84-[SBMenuBarManager _dismissMenuBarAnimated:clearStatusBarAssertions:withCompletion:]_block_invoke_4
+ ___84-[SBMenuBarManager _dismissMenuBarAnimated:clearStatusBarAssertions:withCompletion:]_block_invoke_5
+ ___84-[SBMenuBarManager _dismissMenuBarAnimated:clearStatusBarAssertions:withCompletion:]_block_invoke_6
+ ___84-[SBMenuBarManager _dismissMenuBarAnimated:clearStatusBarAssertions:withCompletion:]_block_invoke_7
+ ___84-[SBMenuBarManager _dismissMenuBarAnimated:clearStatusBarAssertions:withCompletion:]_block_invoke_8
+ ___88-[SBAssistantIslandStageCoordinator _registerZOrderStageResolverForWindowSceneIfNeeded:]_block_invoke
+ ___88-[SBAssistantIslandStageCoordinator _registerZOrderStageResolverForWindowSceneIfNeeded:]_block_invoke_2
+ ___90-[SBSwitcherController requestInAppStatusBarHiddenAssertionForReason:partAlphas:animated:]_block_invoke
+ ___92-[SBMainSwitcherControllerCoordinator keyboardFocusController:didAddDeferringRuleForTarget:]_block_invoke
+ ___93-[SBFullScreenSwitcherSceneLiveContentOverlay setStatusBarPartAlphas:nubViewHidden:animator:]_block_invoke
+ ___93-[SBSwitcherController initWithWindowScene:applicationController:supportsResizing:debugName:]_block_invoke
+ ___96-[FBScene(InputUISceneController) sb_setDisallowsKeyboardPresentationInDefaultInputUIPresenter:]_block_invoke
+ ___99-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:clearStatusBarAssertionsForDismissal:]_block_invoke
+ ___99-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:clearStatusBarAssertionsForDismissal:]_block_invoke_2
+ ___99-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:clearStatusBarAssertionsForDismissal:]_block_invoke_3
+ ___99-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:clearStatusBarAssertionsForDismissal:]_block_invoke_4
+ ___99-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:clearStatusBarAssertionsForDismissal:]_block_invoke_5
+ ___SBRecordingIndicatorLayerApplyBlurRadius_block_invoke
+ ___SBScreenBrightnessSharedCBClient_block_invoke
+ ___SBScreenBrightnessUsesCBDisplayClient_block_invoke
+ ___blockIMPFromContextSignature111_block_invoke
+ ___blockIMPFromEventSignature111_block_invoke
+ ___blockIMPFromQuerySignature111_block_invoke
+ ___block_descriptor_112_e8_32s40bs48r56r64r72r80r_e8_v16?0d8lr48l8r56l8s40l8r64l8s32l8r72l8r80l8
+ ___block_descriptor_136_e8_32s40s48s56s64bs72bs80bs88r_e5_v8?0lr88l8s32l8s64l8s40l8s72l8s48l8s80l8s56l8
+ ___block_descriptor_144_e8_32s40s48s56s64bs72bs80bs88bs96r_e5_v8?0lr96l8s32l8s64l8s40l8s72l8s48l8s80l8s56l8s88l8
+ ___block_descriptor_152_e8_32s40s48s56s64bs72bs80bs88r96r_e8_v16?0d8lr88l8r96l8s32l8s64l8s40l8s72l8s48l8s80l8s56l8
+ ___block_descriptor_160_e8_32s40s48s56s64bs72bs80bs88bs96r104r_e8_v16?0d8lr96l8r104l8s32l8s64l8s40l8s72l8s48l8s80l8s56l8s88l8
+ ___block_descriptor_210_e8_32s40s48s56s64s72s80s88s96s104s112s120r128r136r144w_e33_v16?0?<?<v?BB>?"NSString">8lw144l8s32l8r120l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8r128l8r136l8s104l8s112l8
+ ___block_descriptor_33_e36_v16?0"SBMutableStatusBarSettings"8l
+ ___block_descriptor_40_e33_v16?0"FBSMutableSceneSettings"8l
+ ___block_descriptor_40_e8_32r_e8_v12?0B8lr32l8
+ ___block_descriptor_40_e8_32w_e8_v12?0C8lw32l8
+ ___block_descriptor_48_e35_32?0"SBChainableModifier"816:24l
+ ___block_descriptor_48_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16lr32l8r40l8
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_51_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48w_e11_v16?0B8B12ls32l8w48l8r40l8
+ ___block_descriptor_57_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_58_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32bs40r48r_e8_v16?0d8lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_72_e8_32r40r48r56w64w_e53_v24?0"NSArray"8"TRAPreferencesResolutionContext"16lw56l8w64l8r32l8r40l8r48l8
+ ___block_descriptor_72_e8_32s40bs48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0lr48l8r56l8r64l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40bs48r56r_e5_v8?0lr48l8s32l8r56l8s40l8
+ ___block_descriptor_80_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_83_e8_32s40s48s56s64s72w_e8_v12?0B8lw72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r80r_e39_v16?0"<FBSceneSnapshotConfigurator>"8ls32l8s40l8r64l8s48l8s56l8r72l8r80l8
+ ___block_descriptor_96_e8_32s40bs48r56r_e8_v16?0d8lr48l8r56l8s32l8s40l8
+ __initReasonWithName:strength:avoidOverridingAppFocusOnOtherDisplays:ignoreModalitiesOnSelectionChange:imposesConstraint:blocksFocusRequestsForReasons:.sNextCreationOrder
+ __isThermalCriticalGlyphBloomEligibleDevice.eligible
+ __isThermalCriticalGlyphBloomEligibleDevice.onceToken
+ _blockIMPFromContextSignature111
+ _blockIMPFromEventSignature111
+ _blockIMPFromQuerySignature111
+ _kCoverSheetGrabberFadeInDuration
+ _kCoverSheetGrabberHoldDuration
+ _kCoverSheetGrabberPulseTeachOutCount
+ _keyboardFocusController:didAddDeferringRuleForTarget:.onceToken
+ _keyboardFocusController:didAddDeferringRuleForTarget:.sEnabled
+ _objc_msgSend$_acquireAssertion
+ _objc_msgSend$_acquireHideSystemStatusBarAssertionIfNeeded
+ _objc_msgSend$_addOutstandingProcessIdentity:
+ _objc_msgSend$_applicationNameForOverlayStatusBar
+ _objc_msgSend$_applyListeningThinkingWaveSettings:
+ _objc_msgSend$_applyPreferredBrightness:
+ _objc_msgSend$_baseContentOriginOffset
+ _objc_msgSend$_beginObservingAppFlyInSettle
+ _objc_msgSend$_beginWaitingForAppFlyInSettle
+ _objc_msgSend$_canPerformMotionWake
+ _objc_msgSend$_canPresentGrabberForHandoff
+ _objc_msgSend$_cancelDeferredMenuBarPeekTimerForSwitcherContentController:
+ _objc_msgSend$_cancelPendingShake
+ _objc_msgSend$_centerStatusBarPartFrame
+ _objc_msgSend$_checkAndPostDismissalNearlyCompleteNotificationWithProgress:isPresenting:isOverApp:
+ _objc_msgSend$_cleanupQueuesOnWithdrawForRequest:
+ _objc_msgSend$_clearStatusBarPartAlphaOverridesIfNeeded
+ _objc_msgSend$_clientPreferredRootWindowTransform
+ _objc_msgSend$_collapsedContentOriginOffset
+ _objc_msgSend$_combinedInAppPartAlphas
+ _objc_msgSend$_configureDisplayClientForDisplayConfiguration:
+ _objc_msgSend$_contentFrameInSceneReferenceSpace
+ _objc_msgSend$_cornerCenterForContext:withFrame:scale:grabberHandoffFrame:
+ _objc_msgSend$_createLayoutPublisherForRootDisplayIdentityIfNeeded:displayConfiguration:
+ _objc_msgSend$_deviceIsChinaSKU
+ _objc_msgSend$_deviceSupportsAppleIntelligence
+ _objc_msgSend$_didFinishOffscreenTransition
+ _objc_msgSend$_dismissMenuBarAnimated:clearStatusBarAssertions:
+ _objc_msgSend$_dismissMenuBarAnimated:clearStatusBarAssertions:withCompletion:
+ _objc_msgSend$_dismissalCompletionLeavingGroup:foldingFinishedInto:
+ _objc_msgSend$_expandedContentOriginOffset
+ _objc_msgSend$_fakedResizingDisplayConfigurationForFrame:
+ _objc_msgSend$_finishWaitingForAppFlyInSettle
+ _objc_msgSend$_flushPendingBrightnessToScene:
+ _objc_msgSend$_forwardElementContextChangesFromElement:forActivityIdentifier:
+ _objc_msgSend$_handlePresenceMotion
+ _objc_msgSend$_handleState:
+ _objc_msgSend$_handleStateOnMainQueue:
+ _objc_msgSend$_hasResizedSinceEnteringDisplay
+ _objc_msgSend$_invalidateLayoutPublisherForRootDisplayIdentity:
+ _objc_msgSend$_isAssistantIslandVisiblyPresentedOnWindowScene:
+ _objc_msgSend$_isInCallOnReceiverRoute
+ _objc_msgSend$_isMotionDetectionCapable
+ _objc_msgSend$_isPrewarmDisabledForClientCrashLoop
+ _objc_msgSend$_isSuppressionActive
+ _objc_msgSend$_isSystemApertureGestureRecognizer:
+ _objc_msgSend$_isThermalCriticalGlyphBloomEligibleDevice
+ _objc_msgSend$_keyboardHostComponent
+ _objc_msgSend$_leadingStatusBarPartFrameIncludingCenterPartIfNecessary
+ _objc_msgSend$_metricsForWindowScene:
+ _objc_msgSend$_noteClientDidCrash
+ _objc_msgSend$_noteSmartCoverDidOpenOnMain
+ _objc_msgSend$_recomputeAggregateStyle
+ _objc_msgSend$_reconsiderButtonEnablement
+ _objc_msgSend$_registerZOrderStageResolverForWindowSceneIfNeeded:
+ _objc_msgSend$_requireGesturesToFail:forSearchGesture:
+ _objc_msgSend$_requireGesturesToFail:forTodayViewController:
+ _objc_msgSend$_sceneHandleForActivityIdentifier:
+ _objc_msgSend$_scheduleShake
+ _objc_msgSend$_setClientPreferredRootWindowTransform:
+ _objc_msgSend$_setHostWindowAlpha:
+ _objc_msgSend$_setMenuBarVisible:animated:userInitiated:clearStatusBarAssertionsForDismissal:
+ _objc_msgSend$_setMenuViewEnabled:withProvidingAppRestricted:
+ _objc_msgSend$_setObjectWithinCrudeProximity:
+ _objc_msgSend$_setRequestedIndicatorElevationStyle:
+ _objc_msgSend$_setupBackgroundKeepAlive
+ _objc_msgSend$_shouldBloomForThermalCriticalUnlock
+ _objc_msgSend$_stopObservingAppFlyInSettle
+ _objc_msgSend$_tearDownAnnounceOnWithdrawForLinwoodPreprocessForRequest:
+ _objc_msgSend$_tearDownAnnounceOnWithdrawForRequest:revokeSucceeded:
+ _objc_msgSend$_tearDownDisplayClient
+ _objc_msgSend$_tearDownMorphHandle
+ _objc_msgSend$_timeLabelFrameInWindow:statusBar:
+ _objc_msgSend$_updateBackgroundAngelKeepAlive
+ _objc_msgSend$_updateDimmingViewMaskPositionForOffScreenWithBounds:
+ _objc_msgSend$_updateHideSystemStatusBarAssertionForCurrentContext
+ _objc_msgSend$_updateHostingDisplayBacklightStateActive
+ _objc_msgSend$_updateKeyboardFocusSuppression
+ _objc_msgSend$_updateListeningThinkingWaveSettings
+ _objc_msgSend$_updateMotionDetectionCapability
+ _objc_msgSend$_updateMotionDetectionIdleTimerAssertion
+ _objc_msgSend$_updateMotionDetectionListening
+ _objc_msgSend$_updateMotionDetectionWake
+ _objc_msgSend$_updateRequestedIndicatorElevationStyleForAllControllerProxies
+ _objc_msgSend$_updateResidentInactive
+ _objc_msgSend$_updateResidentInactiveStageForWindowScene:
+ _objc_msgSend$_updateResidentInactiveStages
+ _objc_msgSend$_updateSceneHandleForActivityIdentifier:withDestinationToken:layoutDirection:
+ _objc_msgSend$_updateScreenBrightness:
+ _objc_msgSend$_updateStatusBarWindowLevelOverride
+ _objc_msgSend$_updateSystemApertureAnimationStyle
+ _objc_msgSend$_windowControlsLayoutForApplicationFrame:screenBounds:application:switcherController:displayEdgeInfo:statusBarHidden:preferredWindowControlsPlacement:
+ _objc_msgSend$_withdrawNotificationRequest:tearDownAnnounceForLinwoodPreprocess:
+ _objc_msgSend$acquireDisableTapToWakeAssertionForReason:
+ _objc_msgSend$activateWithError:
+ _objc_msgSend$addWindowControlsPresentationObserver:
+ _objc_msgSend$ambientDefaultMetrics
+ _objc_msgSend$ambientWidgetMetrics
+ _objc_msgSend$appFlyInDidSettle
+ _objc_msgSend$appFlyInDidSettleTimestamp
+ _objc_msgSend$appFlyInSettleFallbackTimer
+ _objc_msgSend$appNameMenuBarProvider
+ _objc_msgSend$appNameStatusBarOverlayData
+ _objc_msgSend$bannerHandoffInstantAppear
+ _objc_msgSend$brightnessClient
+ _objc_msgSend$brightnessWithError:
+ _objc_msgSend$canSwapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:
+ _objc_msgSend$centerStatusBarPartFrameForSwitcherContentController:
+ _objc_msgSend$centerStatusBarPartFrameShouldBeConsideredInWindowingLayoutForSwitcherContentController:
+ _objc_msgSend$contentOriginOffset
+ _objc_msgSend$coordinatorForWindowSceneManager:
+ _objc_msgSend$couldSupportMedusa
+ _objc_msgSend$coverSheetGrabberManager
+ _objc_msgSend$createSceneForSceneEntity:
+ _objc_msgSend$currentKeyboardProxyOwner
+ _objc_msgSend$currentPresentationTransformForVisibleAppLayout:
+ _objc_msgSend$customBannerTransitionStyleGlass_cornerAnchorYOffset
+ _objc_msgSend$customBannerTransitionStyleGlass_morphHandleCornerRadius
+ _objc_msgSend$customBannerTransitionStyleGlass_morphHandleCrossFadeStartFraction
+ _objc_msgSend$dismissExpandedModuleAnimated:completion:
+ _objc_msgSend$dismissMenuIfPresented
+ _objc_msgSend$dismissPresentedMenu
+ _objc_msgSend$dismissWindowControlsMenuForMainMenuPresentation
+ _objc_msgSend$displayItemIsDiscreteResizable:
+ _objc_msgSend$embeddedDisplayChamoisSnapPaddingSettings
+ _objc_msgSend$externalDisplayChamoisSnapPaddingSettings
+ _objc_msgSend$fetchOrCreateNewStageControllerForWindowScene:state:chatSessionIdentifier:spotlightInvocationSource:dismissesControlCenterIfVisible:actions:completion:
+ _objc_msgSend$floatingPresentationStatusBarOutset
+ _objc_msgSend$formatDateAsTimeStyle:
+ _objc_msgSend$fullScreenSnapPadding
+ _objc_msgSend$gestureManagerIsActivityResignedActive:
+ _objc_msgSend$handoffBannerDismiss
+ _objc_msgSend$hasGlass
+ _objc_msgSend$hasPostedDismissalNearlyCompleteNotification
+ _objc_msgSend$inAppStatusBarPartAlphasForSwitcherContentController:
+ _objc_msgSend$initWithClientID:
+ _objc_msgSend$initWithConfiguration:windowScene:activeLayoutDirection:
+ _objc_msgSend$initWithIdentifier:forReason:partAlphas:invalidationBlock:
+ _objc_msgSend$initWithServiceListenerFactory:connectedDisplayInfoFactory:layoutPublisherFactory:defaults:
+ _objc_msgSend$initWithStageResolverBlock:specifierDescription:componentOrder:arbiter:
+ _objc_msgSend$initWithWindowScene:allowsPortraitInAmbient:activeLayoutDirection:
+ _objc_msgSend$initWithWindowScene:applicationController:supportsResizing:debugName:
+ _objc_msgSend$initWithWindowSceneManager:cspn:
+ _objc_msgSend$interItemPadding
+ _objc_msgSend$invalidateLayoutPublisher:observer:
+ _objc_msgSend$invalidateOnSystemSleep
+ _objc_msgSend$invalidateOnSystemSleepAfterMinimumActiveInterval:
+ _objc_msgSend$isDeviceEligible
+ _objc_msgSend$isDisconnected
+ _objc_msgSend$isHomeScreenTranslationEnabled
+ _objc_msgSend$isPeriocularMatchingEnabled
+ _objc_msgSend$isPresentedOnBehalfOfSiri
+ _objc_msgSend$isResidentInactive
+ _objc_msgSend$isResizableAppHostingWindowScene
+ _objc_msgSend$isWaitingForAppFlyInSettle
+ _objc_msgSend$layoutPublisherForRootDisplayIdentity:
+ _objc_msgSend$leadingItemSpacingForMenuBarViewController:
+ _objc_msgSend$listeningThinkingWaveActiveGaussianRadius
+ _objc_msgSend$listeningThinkingWaveInitialGaussianRadius
+ _objc_msgSend$listeningThinkingWaveLensingAmount
+ _objc_msgSend$listeningThinkingWaveLensingHeight
+ _objc_msgSend$listeningThinkingWaveVariableBlurLocation
+ _objc_msgSend$listeningThinkingWaveVariableBlurRadius
+ _objc_msgSend$main_processDidExit:
+ _objc_msgSend$menuBarLeadingItemSpacing
+ _objc_msgSend$menuBarUsesStatusBarCenterRegion
+ _objc_msgSend$modalFullScreenMetrics
+ _objc_msgSend$multiAppCenterPadding
+ _objc_msgSend$newBannerMorphHandleView
+ _objc_msgSend$newBannerMorphHandleViewWithLegibilitySettings:
+ _objc_msgSend$newBlockBasedZOrderStageResolver:forRole:
+ _objc_msgSend$newDisplayClientForID:withError:
+ _objc_msgSend$newDisplayLinkWithTarget:selector:
+ _objc_msgSend$newLayoutPublisherWithInstanceIdentifier:displayConfiguration:observer:
+ _objc_msgSend$noteSignificantEvent
+ _objc_msgSend$noteSmartCoverDidOpen
+ _objc_msgSend$observesProximityForBacklightChanges
+ _objc_msgSend$overrideIconImageAppearance
+ _objc_msgSend$overrideIconImageStyleConfiguration
+ _objc_msgSend$performCustomTransitionToVisible:withAnimationSettings:completion:
+ _objc_msgSend$pointInScreenFixedCoordinateSpace:isInsideKeyboardContentOnDisplay:
+ _objc_msgSend$prepareForActivationWithContext:presentationMode:presentEmbedded:shouldUseResizableViewController:windowScene:completion:
+ _objc_msgSend$proxiedKeyboardOwner
+ _objc_msgSend$proximitySuspensionMode
+ _objc_msgSend$refreshMotionDetectionWake
+ _objc_msgSend$registerBrightnessObserver:
+ _objc_msgSend$registerWithCallback:callback:
+ _objc_msgSend$removeStageResolver:
+ _objc_msgSend$removeWindowControlsPresentationObserver:
+ _objc_msgSend$replaceApplicationIconsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:
+ _objc_msgSend$requestInAppStatusBarHiddenAssertionForReason:partAlphas:animated:
+ _objc_msgSend$requestedElevationStyle
+ _objc_msgSend$requestedIndicatorElevationStyle
+ _objc_msgSend$requiresClassicTreatmentForApplication:
+ _objc_msgSend$resizingCapabilityOverrideForApps
+ _objc_msgSend$resizingCoordinator:didUpdateResizingPossible:preferredSize:
+ _objc_msgSend$reversedOrderedSet
+ _objc_msgSend$sb_disallowsKeyboardPresentationInDefaultInputUIPresenter
+ _objc_msgSend$sb_setDisallowsKeyboardPresentationInDefaultInputUIPresenter:
+ _objc_msgSend$sbh_iconImageAppearanceFromTraitCollection:overrideIconImageAppearance:overrideIconImageStyleConfiguration:
+ _objc_msgSend$sceneResizingCapability
+ _objc_msgSend$sceneResizingCapabilityForApplication:
+ _objc_msgSend$screenBrightness
+ _objc_msgSend$secureIndicatorElevationServer:didChangeRequestedElevationStyle:
+ _objc_msgSend$setActiveWindowScene:activeLayoutDirection:
+ _objc_msgSend$setAppFlyInDidSettle:
+ _objc_msgSend$setAppFlyInDidSettleTimestamp:
+ _objc_msgSend$setAppFlyInSettleFallbackTimer:
+ _objc_msgSend$setBannerHandoffInstantAppear:
+ _objc_msgSend$setBrightness:error:
+ _objc_msgSend$setContentOriginOffset:
+ _objc_msgSend$setCustomBannerTransitionStyleGlass_cornerAnchorYOffset:
+ _objc_msgSend$setCustomBannerTransitionStyleGlass_morphHandleCornerRadius:
+ _objc_msgSend$setCustomBannerTransitionStyleGlass_morphHandleCrossFadeStartFraction:
+ _objc_msgSend$setDeviceCanBeTreatedAsEffectivelyLocked:
+ _objc_msgSend$setDismissalCommitted:
+ _objc_msgSend$setEmbeddedDisplayChamoisSnapPaddingSettings:
+ _objc_msgSend$setExternalDisplayChamoisSnapPaddingSettings:
+ _objc_msgSend$setFloatingPresentationStatusBarOutset:
+ _objc_msgSend$setFullScreenSnapPadding:
+ _objc_msgSend$setHasPostedDismissalNearlyCompleteNotification:
+ _objc_msgSend$setHomeScreenTranslationEnabled:
+ _objc_msgSend$setHostingDisplayBacklightStateActive:
+ _objc_msgSend$setInterItemPadding:
+ _objc_msgSend$setIsWaitingForAppFlyInSettle:
+ _objc_msgSend$setLastSettledPresentedState:
+ _objc_msgSend$setListeningThinkingWaveActiveGaussianRadius:
+ _objc_msgSend$setListeningThinkingWaveInitialGaussianRadius:
+ _objc_msgSend$setListeningThinkingWaveLensingAmount:
+ _objc_msgSend$setListeningThinkingWaveLensingHeight:
+ _objc_msgSend$setListeningThinkingWaveVariableBlurLocation:
+ _objc_msgSend$setListeningThinkingWaveVariableBlurRadius:
+ _objc_msgSend$setMultiAppCenterPadding:
+ _objc_msgSend$setObservesProximityForBacklightChanges:
+ _objc_msgSend$setOnAC:
+ _objc_msgSend$setPersistentMenuBarLeadingStyle:
+ _objc_msgSend$setProximitySuspensionMode:
+ _objc_msgSend$setRequestedIndicatorElevationStyle:
+ _objc_msgSend$setScreenBrightness:
+ _objc_msgSend$setShouldUseResizableViewController:
+ _objc_msgSend$setSingleAppCenterPadding:
+ _objc_msgSend$setStatusBarPartAlphas:nubViewHidden:animator:
+ _objc_msgSend$setSuppressTeachPulse:
+ _objc_msgSend$setSystemApertureAnimationStyle:
+ _objc_msgSend$setSystemApertureUnifiedAnimationEnabled:
+ _objc_msgSend$setUIKitMainLike
+ _objc_msgSend$setUsesSecureIndicatorLayer:
+ _objc_msgSend$shouldUseResizableViewController
+ _objc_msgSend$singleAppCenterPadding
+ _objc_msgSend$supportsSceneResizingForApplication:
+ _objc_msgSend$supportsSolariumSafeAreasRegardlessOfWindowingModeForApplication:switcherController:
+ _objc_msgSend$supportsiPhoneResizing
+ _objc_msgSend$suppressKeyboardFocusRequestsForReason:
+ _objc_msgSend$suppressTeachPulse
+ _objc_msgSend$swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:
+ _objc_msgSend$switcherContentController:displayItemIsClassic:
+ _objc_msgSend$switcherContentController:displayItemSupportsMedusa:
+ _objc_msgSend$syncState
+ _objc_msgSend$systemApertureAnimationStyle
+ _objc_msgSend$systemApertureSceneElement:destinationTokenDidChange:
+ _objc_msgSend$systemApertureSceneElement:layoutDirectionDidChange:
+ _objc_msgSend$systemApertureUnifiedAnimationEnabled
+ _objc_msgSend$targetGrabberFrameInCoordinateSpace:
+ _objc_msgSend$terminateNonIslandSpotlight
+ _objc_msgSend$ui_renderingEnvironment
+ _objc_msgSend$unregister
+ _objc_msgSend$unregisterBrightnessObserver:
+ _objc_msgSend$updateInAppStatusBarHiddenAssertion:partAlphas:animated:
+ _objc_msgSend$updateMenuBarEnablementForAppRestrictionChange
+ _objc_msgSend$updateMenuEnablementForAppRestrictionChange
+ _objc_msgSend$updateSpotlightInvocationSource:
+ _objc_msgSend$usesSecureIndicatorLayer
+ _objc_msgSend$windowControlsWillBeginPresentingMenuForSceneProvider:
- +[SBApplication(Classic) restrictedDisplayConfigurationForResizableAppWithDisplayConfiguration:size:]
- +[SBApplication(Classic) restrictedDisplayConfigurationForUIRequiresFullScreenAppWithDisplayConfiguration:size:]
- +[SBBrightnessLevelSceneExtension hostComponents]
- +[SBRecordingIndicatorView layerClass]
- -[SBActivityMetrics _ambientDefaultMetricsForWindowScene:]
- -[SBActivityMetrics _ambientWidgetMetricsForWindowScene:]
- -[SBActivityMetrics _defaultMetricsForWindowScene:]
- -[SBActivityMetrics _limitedWidthSystemApertureMetricsForWindowScene:]
- -[SBActivityMetrics _lockScreenNotificationListItemMetricsWithScaleFactor:screen:]
- -[SBActivityMetrics _modalFullScreenMetricsForWindowScene:]
- -[SBActivityMetrics _screenForWindowScene:]
- -[SBActivityMetrics _systemApertureMetricsForWindowScene:]
- -[SBActivityMetrics _systemApertureMetricsWithJindoMetricsProvider:maximumLeadingTrailingViewSize:uniformEdgeInsets:]
- -[SBActivitySystemApertureElementObserver updateSystemApertureMetricsForWindowScene:]
- -[SBAmbientIdleTimerController initWithWindowScene:backlightController:]
- -[SBAmbientPresentationController _isMotionToWakePermitted]
- -[SBAmbientPresentationController _isMotionToWakeUserSettingEnabled]
- -[SBAmbientPresentationController _updateMotionDetection]
- -[SBAmbientPresentationController motionDetectionWakeAttributeMonitor:didUpdateShouldEnableMotionDetectionWake:]
- -[SBAppResizingCoordinator resizingAvailability]
- -[SBAppResizingService resizingCoordinator:didUpdateAvailability:preferredSize:]
- -[SBApplication _isClassicAppRequiringScreenObscuringForScreenType:]
- -[SBApplication(ChamoisCapabilities) supportsSceneResizingOnDisplayConfiguration:]
- -[SBApplication(ChamoisCapabilities) supportsSceneResizing]
- -[SBApplication(Classic) requiresClassicTreatmentInSwitcherWindowManagementContext:]
- -[SBApplication(Classic) restrictedClassicModeDisplayConfigurationForDisplayConfiguration:windowManagementContext:]
- -[SBApplication(Classic_Internal) _isClassicViaOverride]
- -[SBApplication(Classic_PrivateForWebAppOnly) _setDefaultClassicModeOverride:]
- -[SBApplication(SwitcherCapabilitiesProvidedByClassic) isMedusaCapable]
- -[SBApplication(SwitcherCapabilitiesProvidedByClassic) isResizablePhoneAppOnPad]
- -[SBApplication(SwitcherCapabilitiesProvidedByClassic) isResizablePhoneAppOnResizableDisplays]
- -[SBApplication(SwitcherCapabilitiesProvidedByClassic) isResizableUIRequiresFullScreenAppOnPad]
- -[SBApplication(SwitcherCapabilitiesProvidedByClassic) resizingAvailabilityOnResizableDisplays]
- -[SBApplicationCompatibilityModeProvider .cxx_destruct]
- -[SBApplicationCompatibilityModeProvider _appRequiresClassicTreatmentInCurrentWindowManagementContext]
- -[SBApplicationCompatibilityModeProvider initWithApplication:windowManagementContext:]
- -[SBApplicationCompatibilityModeProvider isClassicAppFullScreen]
- -[SBApplicationCompatibilityModeProvider isClassicAppNonFullScreenWithHomeAffordance]
- -[SBApplicationCompatibilityModeProvider isClassicAppPhoneAppRunningOnPad]
- -[SBApplicationCompatibilityModeProvider isClassicAppRequiresHiDPI]
- -[SBApplicationCompatibilityModeProvider isClassicAppScaledWithAspectRatioCloseEnoughToBeTreatedAsFullScreen]
- -[SBApplicationCompatibilityModeProvider isClassicAppScaled]
- -[SBApplicationCompatibilityModeProvider isClassicAppWithRoundedCorners]
- -[SBApplicationCompatibilityModeProvider isClassicAppZoomedInOrRequiresHiDPI]
- -[SBApplicationCompatibilityModeProvider isClassicAppZoomedIn]
- -[SBApplicationCompatibilityModeProvider isClassic]
- -[SBApplicationCompatibilityModeProvider supportsSceneResizingOnDisplayConfiguration:]
- -[SBApplicationInfo wantsFullScreen]
- -[SBApplicationSceneHandle applicationCompatibilityModeProvider]
- -[SBAssistantIslandStageController _homeScreenOpacityForProgress:]
- -[SBAssistantIslandStageController _invalidateIfOrphaned]
- -[SBAssistantIslandStageController homeScreenAlpha]
- -[SBAssistantIslandStageCoordinator _containerBoundsForWindowScene:containerOrientation:]
- -[SBAssistantIslandStageCoordinator fetchOrCreateNewStageControllerForWindowScene:state:chatSessionIdentifier:spotlightInvocationSource:actions:completion:]
- -[SBAssistantIslandStageGestureManager _leftHitTestRectForFrame:]
- -[SBAssistantIslandStageGestureManager _rightHitTestRectForFrame:]
- -[SBAssistantIslandSwitcherModifier homeScreenAlpha]
- -[SBBannerTransitionSettings customBannerTransitionStyleGlass_dismissAlphaFraction]
- -[SBBannerTransitionSettings setCustomBannerTransitionStyleGlass_dismissAlphaFraction:]
- -[SBBrightnessLevelHostComponent scene:didUpdateClientSettings:]
- -[SBContinuitySession resizingCoordinator:didUpdateAvailability:preferredSize:]
- -[SBCoverSheetGrabberManager _handleCoverSheetDidDismissNotification:]
- -[SBDashBoardPearlUnlockBehavior _armMatchPasscodeFallbackTimerIfNeeded]
- -[SBDashBoardPearlUnlockBehavior _handleMatchPasscodeFallbackForEvent:]
- -[SBDashBoardPearlUnlockBehavior _invalidateMatchPasscodeFallbackTimer]
- -[SBDashBoardPearlUnlockBehavior _matchPasscodeFallbackFailureSettings]
- -[SBDashBoardPearlUnlockBehavior _matchPasscodeFallbackInterval]
- -[SBDashBoardPearlUnlockBehavior _matchPasscodeFallbackTimerFired]
- -[SBDashBoardPearlUnlockBehavior _matchPasscodeFallbackTimer]
- -[SBDashBoardPearlUnlockBehavior dealloc]
- -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider constrainsContainingSceneOrientation]
- -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider scene:didUpdateClientSettings:]
- -[SBExternalDisplayService initWithServiceListenerFactory:connectedDisplayInfoFactory:defaults:]
- -[SBFlexibleWindowingWindowDragSwitcherModifier _beginAnimatingExitSnapPointRampingPropertyX]
- -[SBFlexibleWindowingWindowDragSwitcherModifier _beginAnimatingExitSnapPointRampingPropertyY]
- -[SBFlexibleWindowingWindowDragSwitcherModifier _exitSnapPointRampingSettings]
- -[SBFlexibleWindowingWindowDragSwitcherModifier _initializeExitSnapRampingPropertyX]
- -[SBFlexibleWindowingWindowDragSwitcherModifier _initializeExitSnapRampingPropertyY]
- -[SBFlexibleWindowingWindowDragSwitcherModifier _shouldLayOutSelectedItemAtSnappedFrame]
- -[SBFlexibleWindowingWindowDragSwitcherModifier fadeInDelayForSplitViewHandles]
- -[SBFluidSwitcherViewController displayItemIsResizableUIRequiresFullScreen:]
- -[SBGlassBannerTransitionAnimator _leftCornerCenterForContext:withFrame:scale:]
- -[SBHIDUISensorModeAssertion setSuspendProximitySensor:]
- -[SBHIDUISensorModeAssertion suspendProximitySensor]
- -[SBHomeScreenService canSwapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:]
- -[SBHomeScreenService swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:]
- -[SBLockScreenManager _motionDetectionWakeController]
- -[SBLockScreenManager _setMotionDetectionWakeController:]
- -[SBLockScreenManager acquireMotionDetectionWakeEnableAssertionWithReason:]
- -[SBLockScreenManager motionDetectionWakeController:motionDetectStateChanged:]
- -[SBMainDisplaySystemGestureManager shouldSystemGestureReceiveTouchWithLocation:ignoringUCB:]
- -[SBMenuBarHeaderContainerView setWindowControlsAvoidanceOffset:]
- -[SBMenuBarHeaderContainerView windowControlsAvoidanceOffset]
- -[SBMenuBarManager _dismissMenuBarAnimated:]
- -[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]
- -[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]
- -[SBMenuBarManager menuBarSceneUpdateAssertion]
- -[SBMenuBarManager menuBarStatusBarFollowingAppLeadingStyle]
- -[SBMenuBarManager menuBarStatusBarFollowingSystemStyle]
- -[SBMenuBarManager setMenuBarSceneUpdateAssertion:]
- -[SBMenuBarManager setMenuBarStatusBarFollowingAppLeadingStyle:]
- -[SBMenuBarManager setMenuBarStatusBarFollowingSystemStyle:]
- -[SBRecordingIndicatorLayer _commonInit]
- -[SBRecordingIndicatorLayer _resetSecureIndicatorLayerIndicatorType]
- -[SBRecordingIndicatorLayer initWithCoder:]
- -[SBRecordingIndicatorLayer initWithLayer:]
- -[SBRecordingIndicatorLayer init]
- -[SBRecordingIndicatorView _recordingIndicatorLayer]
- -[SBRemoteTransientOverlayViewController prepareForActivationWithContext:presentationMode:presentEmbedded:windowScene:completion:]
- -[SBSafeAreaResolverUtility _windowControlsLayoutForApplicationFrame:screenBounds:application:windowManagementContext:displayEdgeInfo:statusBarHidden:displayConfiguration:preferredWindowControlsPlacement:]
- -[SBSafeAreaResolverUtility supportsSolariumSafeAreasRegardlessOfWindowingModeForApplication:windowManagementContext:]
- -[SBScreenSharingOverlayUISceneController rootWindowTransform]
- -[SBScreenSharingOverlayUISceneController setRootWindowTransform:]
- -[SBSwitcherAnimationAttributes positionXSettings]
- -[SBSwitcherAnimationAttributes positionYSettings]
- -[SBSwitcherAnimationAttributes setPositionXSettings:]
- -[SBSwitcherAnimationAttributes setPositionYSettings:]
- -[SBSwitcherController initWithWindowScene:applicationController:debugName:]
- -[SBSwitcherWindowingSnapPaddingSettings _statusBarHeight]
- -[SBSwitcherWindowingSnapPaddingSettings horizontalInterItemPadding]
- -[SBSwitcherWindowingSnapPaddingSettings setHorizontalInterItemPadding:]
- -[SBSwitcherWindowingSnapPaddingSettings setVerticalInterItemPadding:]
- -[SBSwitcherWindowingSnapPaddingSettings verticalInterItemPadding]
- -[SBSystemApertureViewController _boundsForAdjunctContainerViewWithPreferredEdgeOutsets:layoutDirection:]
- GCC_except_table1044
- GCC_except_table1051
- GCC_except_table1053
- GCC_except_table1055
- GCC_except_table1057
- GCC_except_table1059
- GCC_except_table1061
- GCC_except_table1063
- GCC_except_table110
- GCC_except_table157
- GCC_except_table159
- GCC_except_table184
- GCC_except_table199
- GCC_except_table215
- GCC_except_table235
- GCC_except_table263
- GCC_except_table271
- GCC_except_table283
- GCC_except_table315
- GCC_except_table341
- GCC_except_table355
- GCC_except_table369
- GCC_except_table429
- GCC_except_table433
- GCC_except_table441
- GCC_except_table503
- GCC_except_table529
- GCC_except_table531
- GCC_except_table550
- GCC_except_table552
- GCC_except_table554
- GCC_except_table557
- GCC_except_table559
- GCC_except_table561
- GCC_except_table573
- GCC_except_table575
- GCC_except_table577
- GCC_except_table587
- GCC_except_table591
- GCC_except_table621
- GCC_except_table675
- GCC_except_table710
- GCC_except_table788
- GCC_except_table814
- GCC_except_table817
- GCC_except_table857
- GCC_except_table899
- GCC_except_table901
- GCC_except_table940
- GCC_except_table951
- GCC_except_table98
- GCC_except_table998
- OBJC_IVAR_$_SBApplication._defaultClassicModeOverride
- _NCNotificationStructuredListViewControllerInsetMarginHorizontal
- _OBJC_CLASS_$_ACUISActivityItemMetricsRequest
- _OBJC_CLASS_$_ACUISActivityMetricsRequest
- _OBJC_CLASS_$_ACUISEdgeInsets
- _OBJC_CLASS_$_ACUISSizeDimensionRequest
- _OBJC_CLASS_$_ACUISSystemApertureMetricsRequest
- _OBJC_CLASS_$_CSLockScreenBiometricFailureSettings
- _OBJC_CLASS_$_SBApplicationCompatibilityModeProvider
- _OBJC_CLASS_$_SBBrightnessLevelHostComponent
- _OBJC_CLASS_$_SBBrightnessLevelSceneExtension
- _OBJC_CLASS_$_SBUISearchUtilities
- _OBJC_IVAR_$_SBAmbientPresentationController._motionDetectionWakeAttributeMonitor
- _OBJC_IVAR_$_SBAmbientPresentationController._motionToWakeEnableAssertion
- _OBJC_IVAR_$_SBAppResizingCoordinator._lastNotifiedAvailability
- _OBJC_IVAR_$_SBAppResizingCoordinator._resizingAvailability
- _OBJC_IVAR_$_SBApplicationCompatibilityModeProvider._application
- _OBJC_IVAR_$_SBApplicationCompatibilityModeProvider._windowManagementContext
- _OBJC_IVAR_$_SBApplicationInfo._wantsFullScreen
- _OBJC_IVAR_$_SBApplicationSceneHandle._currentApplicationCompatibilityModeProvider
- _OBJC_IVAR_$_SBApplicationSceneHandle._windowManagementContextForCurrentApplicationCompatibilityModeProvider
- _OBJC_IVAR_$_SBBannerTransitionSettings._customBannerTransitionStyleGlass_dismissAlphaFraction
- _OBJC_IVAR_$_SBDashBoardPearlUnlockBehavior._matchPasscodeFallbackTimer
- _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._exitSnapPointRampingPropertyX
- _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._exitSnapPointRampingPropertyY
- _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._hasDeterminedInitialSnapState
- _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._lastCenterBeforeSnapping
- _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._snappedX
- _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._snappedY
- _OBJC_IVAR_$_SBHIDUISensorModeAssertion._suspendProximitySensor
- _OBJC_IVAR_$_SBInputUISceneController._focusChangeCounter
- _OBJC_IVAR_$_SBInputUISceneController._lastPresentedFocusedSceneToken
- _OBJC_IVAR_$_SBLockScreenManager._motionDetectionIdleTimerAssertion
- _OBJC_IVAR_$_SBLockScreenManager._motionDetectionWakeController
- _OBJC_IVAR_$_SBMenuBarHeaderContainerView._windowControlsAvoidanceOffset
- _OBJC_IVAR_$_SBMenuBarManager._menuBarSceneUpdateAssertion
- _OBJC_IVAR_$_SBMenuBarManager._menuBarStatusBarFollowingAppLeadingStyle
- _OBJC_IVAR_$_SBMenuBarManager._menuBarStatusBarFollowingSystemStyle
- _OBJC_IVAR_$_SBSARenderingAndCloningPreferencesProvider._previousCurtainRenderingStyle
- _OBJC_IVAR_$_SBScreenSharingOverlayUISceneController._rootWindowTransform
- _OBJC_IVAR_$_SBSwitcherAnimationAttributes._positionXSettings
- _OBJC_IVAR_$_SBSwitcherAnimationAttributes._positionYSettings
- _OBJC_IVAR_$_SBSwitcherWindowingSnapPaddingSettings._horizontalInterItemPadding
- _OBJC_IVAR_$_SBSwitcherWindowingSnapPaddingSettings._verticalInterItemPadding
- _OBJC_IVAR_$_SBTraitsZOrderDefaultResolver._wasAssistantIslandAcquired
- _OBJC_IVAR_$_SBTraitsZOrderDefaultResolver._wasScreenshotAcquired
- _OBJC_METACLASS_$_SBApplicationCompatibilityModeProvider
- _OBJC_METACLASS_$_SBBrightnessLevelHostComponent
- _OBJC_METACLASS_$_SBBrightnessLevelSceneExtension
- _SBFIsResizableUIRequiresFullScreenAppAvailable
- _SBResizingAvailabilityDescription
- _SBResizingAvailabilityIsResizingPossible
- __OBJC_$_CATEGORY_UIWindow_$_TRAArbiterExtensions
- __OBJC_$_CLASS_METHODS_SBApplication(SwitcherCapabilitiesProvidedByClassic|Classic|Classic_Private|Classic_Private_ForBaseClassAndSceneHandleOnly|Classic_PrivateForWebAppOnly|Classic_PrivateForUnitTestsOnly|Classic_Internal|Snapshots|SnapshotSorting|ChamoisCapabilities|SwitcherCapabilities|SBWebApplication|DefaultImage|DefaultImage_Naming|DefaultImage_ManifestIngestion|Identity)
- __OBJC_$_CLASS_METHODS_SBBrightnessLevelSceneExtension
- __OBJC_$_CLASS_METHODS_SBRecordingIndicatorView
- __OBJC_$_INSTANCE_METHODS_FBScene(SBVisibilitySceneExtension_ForSceneManager|SBSUIHomeScreenIconStyle|LocalSynchronous|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBProductivityGestureDestination|SafeAreaResolverExtensionDelegate|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
- __OBJC_$_INSTANCE_METHODS_SBApplication(SwitcherCapabilitiesProvidedByClassic|Classic|Classic_Private|Classic_Private_ForBaseClassAndSceneHandleOnly|Classic_PrivateForWebAppOnly|Classic_PrivateForUnitTestsOnly|Classic_Internal|Snapshots|SnapshotSorting|ChamoisCapabilities|SwitcherCapabilities|SBWebApplication|DefaultImage|DefaultImage_Naming|DefaultImage_ManifestIngestion|Identity)
- __OBJC_$_INSTANCE_METHODS_SBApplicationCompatibilityModeProvider
- __OBJC_$_INSTANCE_METHODS_SBBrightnessLevelHostComponent
- __OBJC_$_INSTANCE_METHODS_SBChainableModifierEventResponse(SBSwitcherModifierEventResponse|SBWindowingModifierResponse)
- __OBJC_$_INSTANCE_METHODS_SBSwitcherModifier(SharedModifierUtilities|WindowingModifier)
- __OBJC_$_INSTANCE_METHODS_UIWindow(TRAArbiterExtensions|FBSDisplayConfiguration|SBWindowScene|SelfHosting|SBWindow)
- __OBJC_$_INSTANCE_VARIABLES_SBApplicationCompatibilityModeProvider
- __OBJC_$_INSTANCE_VARIABLES_SBTraitsZOrderDefaultResolver
- __OBJC_$_PROP_LIST_SBApplicationCompatibilityModeProvider
- __OBJC_$_PROP_LIST_SBApplicationCompatibilityModeProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBApplicationCompatibilityModeProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS__UIKeyboardInputRehostingSceneHostObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBApplicationCompatibilityModeProviding
- __OBJC_$_PROTOCOL_REFS_SBApplicationCompatibilityModeProviding
- __OBJC_CLASS_PROTOCOLS_$_FBScene(SBVisibilitySceneExtension_ForSceneManager|SBSUIHomeScreenIconStyle|LocalSynchronous|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBProductivityGestureDestination|SafeAreaResolverExtensionDelegate|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
- __OBJC_CLASS_PROTOCOLS_$_SBApplication(SwitcherCapabilitiesProvidedByClassic|Classic|Classic_Private|Classic_Private_ForBaseClassAndSceneHandleOnly|Classic_PrivateForWebAppOnly|Classic_PrivateForUnitTestsOnly|Classic_Internal|Snapshots|SnapshotSorting|ChamoisCapabilities|SwitcherCapabilities|SBWebApplication|DefaultImage|DefaultImage_Naming|DefaultImage_ManifestIngestion|Identity)
- __OBJC_CLASS_PROTOCOLS_$_SBApplicationCompatibilityModeProvider
- __OBJC_CLASS_RO_$_SBApplicationCompatibilityModeProvider
- __OBJC_CLASS_RO_$_SBBrightnessLevelHostComponent
- __OBJC_CLASS_RO_$_SBBrightnessLevelSceneExtension
- __OBJC_LABEL_PROTOCOL_$_SBApplicationCompatibilityModeProviding
- __OBJC_METACLASS_RO_$_SBApplicationCompatibilityModeProvider
- __OBJC_METACLASS_RO_$_SBBrightnessLevelHostComponent
- __OBJC_METACLASS_RO_$_SBBrightnessLevelSceneExtension
- __OBJC_PROTOCOL_$_SBApplicationCompatibilityModeProviding
- ___105-[SBLockScreenManager coverSheetViewController:requestsExternalPasscodePresentation:animated:completion:]_block_invoke
- ___105-[SBLockScreenManager coverSheetViewController:requestsExternalPasscodePresentation:animated:completion:]_block_invoke_2
- ___129-[SBHomeScreenService swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:]_block_invoke
- ___129-[SBHomeScreenService swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:]_block_invoke_2
- ___156-[SBAssistantIslandStageCoordinator fetchOrCreateNewStageControllerForWindowScene:state:chatSessionIdentifier:spotlightInvocationSource:actions:completion:]_block_invoke
- ___156-[SBAssistantIslandStageCoordinator fetchOrCreateNewStageControllerForWindowScene:state:chatSessionIdentifier:spotlightInvocationSource:actions:completion:]_block_invoke_2
- ___205-[SBSafeAreaResolverUtility _windowControlsLayoutForApplicationFrame:screenBounds:application:windowManagementContext:displayEdgeInfo:statusBarHidden:displayConfiguration:preferredWindowControlsPlacement:]_block_invoke
- ___205-[SBSafeAreaResolverUtility _windowControlsLayoutForApplicationFrame:screenBounds:application:windowManagementContext:displayEdgeInfo:statusBarHidden:displayConfiguration:preferredWindowControlsPlacement:]_block_invoke_2
- ___205-[SBSafeAreaResolverUtility _windowControlsLayoutForApplicationFrame:screenBounds:application:windowManagementContext:displayEdgeInfo:statusBarHidden:displayConfiguration:preferredWindowControlsPlacement:]_block_invoke_3
- ___205-[SBSafeAreaResolverUtility _windowControlsLayoutForApplicationFrame:screenBounds:application:windowManagementContext:displayEdgeInfo:statusBarHidden:displayConfiguration:preferredWindowControlsPlacement:]_block_invoke_4
- ___43-[SBRecordingIndicatorLayer setBlurRadius:]_block_invoke
- ___46-[SBSuspendedSceneWorkspaceTransaction _begin]_block_invoke
- ___46-[SBSuspendedSceneWorkspaceTransaction _begin]_block_invoke_2
- ___46-[SBSuspendedSceneWorkspaceTransaction _begin]_block_invoke_3
- ___46-[SBSuspendedSceneWorkspaceTransaction _begin]_block_invoke_4
- ___46-[SBSuspendedSceneWorkspaceTransaction _begin]_block_invoke_5
- ___57-[SBAssistantIslandStageController _invalidateIfOrphaned]_block_invoke
- ___58-[SBSwitcherWindowingSnapPaddingSettings _statusBarHeight]_block_invoke
- ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke
- ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke_2
- ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke_3
- ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke_4
- ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke_5
- ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke_6
- ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke_7
- ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke_8
- ___62-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]_block_invoke
- ___62-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]_block_invoke_2
- ___62-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]_block_invoke_3
- ___62-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]_block_invoke_4
- ___62-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]_block_invoke_5
- ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_20
- ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_21
- ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_22
- ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_23
- ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_24
- ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_25
- ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_26
- ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_27
- ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_28
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_28
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_29
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_30
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_31
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_32
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_33
- ___68-[SBScreenSharingOverlayUISceneController _applyRootWindowTransform]_block_invoke_3
- ___72-[SBDashBoardPearlUnlockBehavior _armMatchPasscodeFallbackTimerIfNeeded]_block_invoke
- ___76-[SBSwitcherController initWithWindowScene:applicationController:debugName:]_block_invoke
- ___79-[SBSwitcherController requestInAppStatusBarHiddenAssertionForReason:animated:]_block_invoke
- ___89-[SBFullScreenSwitcherSceneLiveContentOverlay setStatusBarHidden:nubViewHidden:animator:]_block_invoke_3
- ___92-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:completion:]_block_invoke_7
- ___93-[SBFlexibleWindowingWindowDragSwitcherModifier _beginAnimatingExitSnapPointRampingPropertyX]_block_invoke
- ___93-[SBFlexibleWindowingWindowDragSwitcherModifier _beginAnimatingExitSnapPointRampingPropertyX]_block_invoke_2
- ___93-[SBFlexibleWindowingWindowDragSwitcherModifier _beginAnimatingExitSnapPointRampingPropertyY]_block_invoke
- ___93-[SBFlexibleWindowingWindowDragSwitcherModifier _beginAnimatingExitSnapPointRampingPropertyY]_block_invoke_2
- ___94-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:completion:]_block_invoke_8
- ___block_descriptor_128_e8_32s40s48s56bs64bs72r80r_e8_v16?0d8lr72l8s32l8s40l8s56l8r80l8s48l8s64l8
- ___block_descriptor_128_e8_32s40s48s56s64s72bs80bs88bs_e5_v8?0ls32l8s40l8s72l8s48l8s80l8s56l8s88l8s64l8
- ___block_descriptor_136_e8_32s40s48s56s64s72bs80bs88bs96bs_e5_v8?0ls32l8s40l8s72l8s48l8s80l8s56l8s88l8s64l8s96l8
- ___block_descriptor_144_e8_32s40s48s56s64s72bs80bs88bs96r_e8_v16?0d8lr96l8s32l8s40l8s72l8s48l8s80l8s56l8s88l8s64l8
- ___block_descriptor_144_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_152_e8_32s40s48s56s64s72bs80bs88bs96bs104r_e8_v16?0d8lr104l8s32l8s40l8s72l8s48l8s80l8s56l8s88l8s64l8s96l8
- ___block_descriptor_178_e8_32s40s48s56s64s72s80s88s96s104s112s120s_e33_v16?0?<?<v?BB>?"NSString">8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8
- ___block_descriptor_44_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16l
- ___block_descriptor_51_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_65_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_74_e8_32s40s48s56s64w_e8_v12?0B8lw64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_74_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_80_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_82_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_88_e8_32s40s48s56s64r72r80r_e39_v16?0"<FBSceneSnapshotConfigurator>"8ls32l8s40l8r64l8s48l8r72l8s56l8r80l8
- ___block_descriptor_96_e8_32s40s48bs56r_e8_v16?0d8lr56l8s32l8s40l8s48l8
- __effectiveProgressForDismissProgress
- _kSnappedTrackingResponse
- _kWindowDragVelocityThresholdForMaintainingTightSpringsAroundSnapPoints
- _objc_msgSend$_ambientDefaultMetricsForWindowScene:
- _objc_msgSend$_ambientWidgetMetricsForWindowScene:
- _objc_msgSend$_appRequiresClassicTreatmentInCurrentWindowManagementContext
- _objc_msgSend$_armMatchPasscodeFallbackTimerIfNeeded
- _objc_msgSend$_beginAnimatingExitSnapPointRampingPropertyX
- _objc_msgSend$_beginAnimatingExitSnapPointRampingPropertyY
- _objc_msgSend$_containerBoundsForWindowScene:containerOrientation:
- _objc_msgSend$_defaultMetricsForWindowScene:
- _objc_msgSend$_dismissMenuBarAnimated:
- _objc_msgSend$_dismissMenuBarAnimated:withCompletion:
- _objc_msgSend$_exitSnapPointRampingSettings
- _objc_msgSend$_handleMatchPasscodeFallbackForEvent:
- _objc_msgSend$_homeScreenOpacityForProgress:
- _objc_msgSend$_initializeExitSnapRampingPropertyX
- _objc_msgSend$_initializeExitSnapRampingPropertyY
- _objc_msgSend$_invalidateIfOrphaned
- _objc_msgSend$_invalidateMatchPasscodeFallbackTimer
- _objc_msgSend$_isClassicViaOverride
- _objc_msgSend$_isMotionToWakeUserSettingEnabled
- _objc_msgSend$_leftCornerCenterForContext:withFrame:scale:
- _objc_msgSend$_leftHitTestRectForFrame:
- _objc_msgSend$_limitedWidthSystemApertureMetricsForWindowScene:
- _objc_msgSend$_lockScreenNotificationListItemMetricsWithScaleFactor:screen:
- _objc_msgSend$_matchPasscodeFallbackFailureSettings
- _objc_msgSend$_matchPasscodeFallbackInterval
- _objc_msgSend$_matchPasscodeFallbackTimerFired
- _objc_msgSend$_modalFullScreenMetricsForWindowScene:
- _objc_msgSend$_rightHitTestRectForFrame:
- _objc_msgSend$_screenForWindowScene:
- _objc_msgSend$_setMenuBarVisible:animated:userInitiated:
- _objc_msgSend$_shouldLayOutSelectedItemAtSnappedFrame
- _objc_msgSend$_systemApertureMetricsForWindowScene:
- _objc_msgSend$_systemApertureMetricsWithJindoMetricsProvider:maximumLeadingTrailingViewSize:uniformEdgeInsets:
- _objc_msgSend$_updateMotionDetection
- _objc_msgSend$_windowControlsLayoutForApplicationFrame:screenBounds:application:windowManagementContext:displayEdgeInfo:statusBarHidden:displayConfiguration:preferredWindowControlsPlacement:
- _objc_msgSend$acquireMotionDetectionWakeEnableAssertionWithReason:
- _objc_msgSend$activitySystemApertureElementObserver
- _objc_msgSend$addFileStackWithURL:
- _objc_msgSend$allVisiblePeripheralFrames
- _objc_msgSend$applicationCompatibilityModeProvider
- _objc_msgSend$canSwapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:
- _objc_msgSend$customBannerTransitionStyleGlass_dismissAlphaFraction
- _objc_msgSend$displayItemIsResizableUIRequiresFullScreen:
- _objc_msgSend$fetchOrCreateNewStageControllerForWindowScene:state:chatSessionIdentifier:spotlightInvocationSource:actions:completion:
- _objc_msgSend$fixed:
- _objc_msgSend$horizontalInterItemPadding
- _objc_msgSend$idealSearchPlatterWidth
- _objc_msgSend$initWithApplication:windowManagementContext:
- _objc_msgSend$initWithLockScreenMetrics:
- _objc_msgSend$initWithMinimum:maximum:
- _objc_msgSend$initWithObstructionSize:obstructionTopMargin:expandedMetricsRequest:compactLeadingMetricsRequest:compactTrailingMetricsRequest:minimalMetricsRequest:
- _objc_msgSend$initWithServiceListenerFactory:connectedDisplayInfoFactory:defaults:
- _objc_msgSend$initWithTop:leading:bottom:trailing:
- _objc_msgSend$initWithWidth:height:cornerRadius:edgeInsets:clipMargin:
- _objc_msgSend$initWithWidth:height:cornerRadius:edgeInsets:clipMargin:scaleFactor:
- _objc_msgSend$initWithWindowScene:applicationController:debugName:
- _objc_msgSend$initWithWindowScene:backlightController:
- _objc_msgSend$isMenuBarDismissing
- _objc_msgSend$isResizablePhoneAppOnPad
- _objc_msgSend$isResizablePhoneAppOnResizableDisplays
- _objc_msgSend$isResizableUIRequiresFullScreenAppOnPad
- _objc_msgSend$isTrailingStatusBarRegionPreferredHiddenByApp
- _objc_msgSend$logTelemetryForMotionToWakeEnabled:
- _objc_msgSend$minimumContinuousCornerRadius
- _objc_msgSend$positionXSettings
- _objc_msgSend$positionYSettings
- _objc_msgSend$prepareForActivationWithContext:presentationMode:presentEmbedded:windowScene:completion:
- _objc_msgSend$requiresClassicTreatmentInSwitcherWindowManagementContext:
- _objc_msgSend$resizingAvailability
- _objc_msgSend$resizingAvailabilityOnResizableDisplays
- _objc_msgSend$resizingCoordinator:didUpdateAvailability:preferredSize:
- _objc_msgSend$restrictedClassicModeDisplayConfigurationForDisplayConfiguration:windowManagementContext:
- _objc_msgSend$restrictedDisplayConfigurationForResizableAppWithDisplayConfiguration:size:
- _objc_msgSend$restrictedDisplayConfigurationForUIRequiresFullScreenAppWithDisplayConfiguration:size:
- _objc_msgSend$sb_supportsResizing
- _objc_msgSend$setAmbientMetrics:
- _objc_msgSend$setCustomBannerTransitionStyleGlass_dismissAlphaFraction:
- _objc_msgSend$setHorizontalInterItemPadding:
- _objc_msgSend$setJiggleLock:
- _objc_msgSend$setLeading:
- _objc_msgSend$setLimitedWidthSystemApertureMetrics:
- _objc_msgSend$setMenuBarStatusBarFollowingAppLeadingStyle:
- _objc_msgSend$setMenuBarStatusBarFollowingSystemStyle:
- _objc_msgSend$setPositionXSettings:
- _objc_msgSend$setPositionYSettings:
- _objc_msgSend$setShowPasscode:
- _objc_msgSend$setSuspendProximitySensor:
- _objc_msgSend$setSystemApertureMetrics:
- _objc_msgSend$setTrailing:
- _objc_msgSend$setTransitionOnlyHelperStatusBar:
- _objc_msgSend$setVerticalInterItemPadding:
- _objc_msgSend$setVibrate:
- _objc_msgSend$setWaitUntilButtonUp:
- _objc_msgSend$setWindowControlsAvoidanceOffset:
- _objc_msgSend$shouldPresentEmbeddedInTargetSceneIfRequested
- _objc_msgSend$shouldSystemGestureReceiveTouchWithLocation:ignoringUCB:
- _objc_msgSend$standBy
- _objc_msgSend$supportsSceneResizingOnDisplayConfiguration:
- _objc_msgSend$supportsSolariumSafeAreasRegardlessOfWindowingModeForApplication:windowManagementContext:
- _objc_msgSend$suspendProximitySensor
- _objc_msgSend$swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:
- _objc_msgSend$transitionOnlyHelperStatusBar
- _objc_msgSend$updateSystemApertureMetricsForWindowScene:
- _objc_msgSend$verticalInterItemPadding
- _objc_msgSend$wantsFullScreen
- _objc_msgSend$windowControlsAvoidanceOffset
- _objc_msgSend$windowSceneForDisplayConfigurationForClassicApps
- _objc_msgSend$withdrawNotificationRequest:
CStrings:
+ "#AnnounceNotification CarPlay presentable will not appear as banner for %{public}@ (reason: %{public}@); recovering fallback queue."
+ "#CarPlayDebug CarPlay skipping fallback banner for %{public}@; request was withdrawn before announce failure callback"
+ "#CarPlayDebug _cleanupQueuesOnWithdrawForRequest: request=%{public}@"
+ "#CarPlayDebug _handleAnnounceTimeoutForLinwoodPreprocess: announceCount=%lu"
+ "#CarPlayDebug _presentBannerForRequest: request=%{public}@"
+ "#CarPlayDebug _registerBannerPresentedForRequest: registered %{public}@ (context: %{public}@)"
+ "#CarPlayDebug _removeNotificationRequestFromPendingAVSessionWithIdentifier: identifier=%{public}@"
+ "#CarPlayDebug _shouldDeactivateSiriSessionForNotificationRequest: request=%{public}@ reason=%{public}@"
+ "#CarPlayDebug _shouldPreprocessNotificationRequest: request=%{public}@ result=NO (in call/FaceTime)"
+ "#CarPlayDebug _shouldPreprocessNotificationRequest: request=%{public}@ wantsSiriLaunch=%{BOOL}d result=%{BOOL}d"
+ "#CarPlayDebug _tearDownAnnounceOnWithdrawForLinwoodPreprocessForRequest: request=%{public}@"
+ "#CarPlayDebug _tearDownAnnounceOnWithdrawForRequest:revokeSucceeded: request=%{public}@ revokeSucceeded=%{BOOL}d"
+ "#CarPlayDebug _withdrawNotificationRequest:tearDownAnnounceForLinwoodPreprocess: request=%{public}@ tearDownAnnounce=%{BOOL}d"
+ "#PreprocessNotification CarPlay ignoring Cancelled for already-preprocessed notification request %{public}@; not a preprocess failure, skipping fallback banner."
+ "#PreprocessNotification preprocess was preempted by Siri activation; enqueueing fallback banner for %{public}@"
+ "%@-%lu"
+ "%{public}@ status bar window level override for stage %{public}@"
+ "-[SBHomeScreenService canSwapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]"
+ "-[SBHomeScreenService replaceApplicationIconsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]"
+ "-[SBHomeScreenService swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]"
+ "-[SBHomeScreenService tearDownAndResetRootIconLists]"
+ ".Continuous"
+ ".Discrete"
+ ".None"
+ "@32@0:8@16:24"
+ "@32@?0@\"SBChainableModifier\"8@16:24"
+ "AA\xf0!"
+ "Acquiring motion detection assertion"
+ "Active Gaussian Radius"
+ "Added disable wallet pre-arm assertion of type %{public}@ for reason: %{public}@"
+ "Ambient motion detection"
+ "Ambient motion wake"
+ "Assistant capability is disallowed by the current policy"
+ "AssistantIsland"
+ "AssistantIslandExternalKeyboardMatchMove"
+ "AssistantIslandStageDeviceLocked"
+ "CSPN HID: instantiated coordinator"
+ "CSPN HID: skipping (feature flag CoreSmartPowerNapHIDSuppression is off)"
+ "CSPN HID: skipping (not iPad)"
+ "CSPN HID: skipping (tap-to-wake not supported on this device)"
+ "CSPN: %{public}s; releasing assertion"
+ "CSPN: On (already held; idempotent)"
+ "CSPN: On but user-presence latch is held; not acquiring"
+ "CSPN: SmartCover OPEN observed (CSPN=%{public}s); no-op (not in On)"
+ "CSPN: SmartCover OPEN observed during On; flipping presence latch and releasing assertion"
+ "CSPN: acquiring digitizer-off assertion (source: CoreSmartPowerNap)"
+ "CSPN: sensor mode controller not yet available; will reconcile on next state callback"
+ "CSPN: starting; initial state=%{public}s"
+ "CSPN: starting; skipping initial reconciliation (no connection)"
+ "CSPN: state %{public}s → %{public}s (latch=%{BOOL}u, held=%{BOOL}u)"
+ "CSPN: stopping; assertion was held=%{BOOL}u"
+ "CarPlay ignoring announce Started for unmatched identifier %{public}@; keeping announce timeout armed for recovery"
+ "CarPlay skipping announce teardown for withdrawn notification request %{public}@; revoke failed (no presentable to dismiss)"
+ "Chamois Embedded Display Snap Padding Settings"
+ "Chamois External Display Snap Padding Settings"
+ "CoolOff"
+ "CoreSmartPowerNapHIDSuppression"
+ "Disabling motion detection wake"
+ "Disconnecting scene %{public}@ left %lu element assertion(s) still registered on the tearing-down proxy; invalidating them now to avoid aborting in -[SAUIElementAssertion dealloc]. Elements: %{public}@"
+ "Disconnecting scene %{public}@ transferred %lu of %lu registered element(s) to %{public}@"
+ "Dismissal completion handler was called more than once; dropping the extra call to avoid unbalancing dispatch_group_leave."
+ "Dismissing Assistant Island because Cover Sheet will present (stateQualifies: %{BOOL}d, forUserGesture: %{BOOL}d)."
+ "Dropped"
+ "Enabling motion detection wake (off-charger, AOD/Off state)"
+ "Error building faked resizing display configuration for %{public}@: %{public}@"
+ "Evaluating motion detection capability [ enableCapability:%{BOOL}d ; suppressionActive:%{BOOL}d ; suppressionRequestsWake:%{BOOL}d ; canPerformMotionWake:%{BOOL}d ; onAC:%{BOOL}d ; backlightState:%{public}@ ; assertion:%{BOOL}d ]"
+ "Evaluating motion detection listening [ shouldListen:%{BOOL}d ; suppressionRequestsWake:%{BOOL}d ; legacyRequestsWake:%{BOOL}d ; canPerformMotionWake:%{BOOL}d ; motionPermitted:%{BOOL}d ; motionToWakeUserSettingEnabled:%{BOOL}d ; userSleepPredicted:%{BOOL}d ; presentationRequested:%{BOOL}d ; motionDetectionCapable:%{BOOL}d ; assertion:%{BOOL}d ]"
+ "FBSDisplayIdentity"
+ "Failed to activate CBClient for screen brightness: %{public}@"
+ "Failed to create CBDisplayClient for display %{public}@: %{public}@"
+ "Failed to get initial brightness for display %{public}@: %{public}@"
+ "Failed to set preferred brightness %.2f: %{public}@"
+ "Full Screen Padding"
+ "Glass Corner Anchor Y Offset"
+ "Glass Morph Handle Corner Radius"
+ "Glass Morph Handle Cross Fade Start Fraction"
+ "Home Screen Style"
+ "Initial Gaussian Radius"
+ "Inter Item Padding"
+ "Invalidating motion detection assertion"
+ "Lensing Amount"
+ "Lensing Height"
+ "Lift to wake enablement changed to: %{BOOL}u (Available: %{BOOL}u, UserPref: %{BOOL}u, Bump: %{BOOL}u, Disabled: %{BOOL}u)"
+ "Listening Wave"
+ "Motion detected while backlight off"
+ "Motion while AlwaysOn active: resetting inactivity timer"
+ "Motion while AlwaysOn suppressed: restoring AlwaysOn"
+ "Motion while backlight off (not our own suppression): requesting screen wake"
+ "Multi App Center Padding"
+ "No CADisplay found matching hardware identifier %{public}@"
+ "No resizable app because %{public}@ isn't resizable"
+ "Observe Proximity For Backlight Changes"
+ "On"
+ "Refusing to adopt element %{public}@ on SBSystemApertureControllerProxy for scene %{public}@ whose window scene has already disconnected; ignoring to avoid stranding a still-valid assertion that would abort in -[SAUIElementAssertion dealloc]."
+ "Refusing to register element %{public}@ on SBSystemApertureControllerProxy for scene %{public}@ whose window scene has already disconnected; ignoring to avoid stranding a still-valid assertion that would abort in -[SAUIElementAssertion dealloc]."
+ "Removed disable wallet pre-arm assertion of type %{public}@ for reason: %{public}@"
+ "Removing stage controller %{public}@ in window scene: %{public}@ because the device locked"
+ "Requested indicator elevation style changed from: %{public}@ to: %{public}@"
+ "Retaining Assistant Island because Cover Sheet will present for a user gesture and state is thinking, response, or transient canvas."
+ "SBAssistantIslandStageEnteredSearch"
+ "SBAssistantIslandStageInactive"
+ "SBCoverSheetAppFlyInDidSettleNotification"
+ "SBCoverSheetDismissalNearlyCompleteIsOverAppKey"
+ "SBCoverSheetDismissalNearlyCompleteNotification"
+ "SBCoverSheetWillPresentForUserGestureKey"
+ "SBLiftToWakeController disabled assertion"
+ "SBScreenBrightnessUsesCBDisplayClient"
+ "SBSecureIndicatorElevationServer dropping connection %@"
+ "SBSecureIndicatorElevationServer ignoring out of range elevation style %ld from client"
+ "SBSecureIndicatorElevationServer invalidating connection because client process is missing required entitlement %@ ."
+ "SBSecureIndicatorElevationServer resolved elevation style %ld"
+ "SBSystemApertureControllerProxy deallocated"
+ "SBSystemApertureControllerProxy for scene %{public}@ deallocated with %lu still-valid element assertion(s) that were never swapped back or invalidated; invalidating now as a backstop. Elements: %{public}@"
+ "SBTapToWakeController disabled assertion"
+ "SBTraitsPipelineBlockBasedZOrderStageResolver was deallocated without being invalidated first."
+ "Secure Indicator Layer"
+ "Setting onAC: %{BOOL}d -> %{BOOL}d"
+ "Setting suppressForSleep: %{BOOL}d -> %{BOOL}d"
+ "Should system gesture receive touch with location:%@ <%@> touchIsInsideKeyboard:%@"
+ "Single App Center Padding"
+ "Skipping reveal of already-displayed icon: %@"
+ "Skipping root window inverse transform for overlay scene %{public}@: no hosting window established yet"
+ "SpringBoard - SBWalletPreArmController"
+ "Status Bar Part Outset"
+ "SwitcherTransitionDeferringRuleCreated"
+ "Terminating non-island Spotlight process because shouldShowEnhancedSiri is now YES"
+ "Took"
+ "Transitioning Assistant Island from transient canvas to response because Cover Sheet will present."
+ "Unable to use defaultPresenter for focused scene %{public}@: forbiddenByPresenter: %{BOOL}d, forbiddenByActivationState: %{BOOL}d, forbiddenBySceneConfiguration: %{BOOL}d"
+ "Unified Animation"
+ "Updating curtain and container rendering style to: %{public}@, high level curtain rendering style to: %{public}@, cloning style: %{public}@"
+ "Use Secure Indicator Layer"
+ "V64S"
+ "Variable Blur Location"
+ "Variable Blur Radius"
+ "Window scene disconnected with residual element"
+ "[%{public}@] Mirroring foreground=%{BOOL}u onto preflight scene %{public}@: targetFrame=%{public}@ preflightFrame=%{public}@ preflightContentState=%{public}@"
+ "[%{public}@] Scene frame became empty (was %{public}@) foreground=%{BOOL}u contentState=%{public}@"
+ "[%{public}@] Skipping snapshot request: backgrounding scene has empty frame. bundleID=%{public}@ contentState=%{public}@ isPreflightScene=%{BOOL}u targetScene=%{public}@ previousFrame=%{public}@ frameChangedThisUpdate=%{BOOL}u hasLayers=%{BOOL}u"
+ "[%{public}lu] Ejection is not viable, so ensure the intersensor region indicator is visible, and the micro is accepted. Reachability active: %{BOOL}u; Resolved elevation style: %{public}@; Backlight On: %{BOOL}u; Are there portrait elements in Jindo: %{BOOL}u; AppearanceStateContext: %@"
+ "[%{public}lu] Holding collision target for container description: %@"
+ "[DeviceSceneHandle] %{public}@ display=%{public}@ bounds=%{public}@ sceneFrame=%{public}@ capability=%{public}@"
+ "[Recording Indicator] re-requesting live-rendering assertion: %@"
+ "[Session] RESIZING - Ignoring continuity button event %{public}@"
+ "[_bs_assert_object isKindOfClass:FBSDisplayIdentityClass]"
+ "[rootIdentity isRootIdentity]"
+ "_SBManualDisplayActivationShieldWindow disable buttons assertion"
+ "_previousHighLevelCurtainRenderingStyle"
+ "_sceneClientSettingsDidUpdate: dismissing visible Control Center"
+ "client crash loop"
+ "client crashed involuntarily (rapid=%lu, total=%lu)"
+ "com.apple.SpringBoard.SBSecureIndicatorElevationServer.connectionQueue"
+ "com.apple.springboard.core-smart-power-nap-hid"
+ "com.apple.springboard.fdi-device-control"
+ "com.apple.springboard.screenbrightness"
+ "com.apple.springboard.screenbrightness.notify"
+ "com.apple.springboard.secure-indicator-elevation"
+ "core-smart-power-nap"
+ "created layout publisher instance: %{public}@ for root: %{public}@"
+ "creating a resident inactive stage for prewarming"
+ "customBannerTransitionStyleGlass_cornerAnchorYOffset"
+ "customBannerTransitionStyleGlass_morphHandleCornerRadius"
+ "customBannerTransitionStyleGlass_morphHandleCrossFadeStartFraction"
+ "device locked"
+ "disabledPreArmAssertions"
+ "disabledPreArmAssertionsByType"
+ "disabling prewarming until next unlock: client crashed %lu times"
+ "fetchOrCreateNewStageController: dismissing visible Control Center"
+ "fetchOrCreateNewStageController: refusing .activityVoice — assistant capability is disallowed (e.g. Apple Pay is up)"
+ "hard"
+ "homeScreenTranslationEnabled"
+ "invalidated layout publisher for root: %{public}@"
+ "invalidating stale scene %@ before recreating it"
+ "menu bar visible"
+ "not running"
+ "observesProximityForBacklightChanges"
+ "orientationMode=%{public}@ for %{public}@"
+ "preArmAllowed"
+ "preArmAvailable"
+ "preArmSuppressed"
+ "process %@ exited; recreating any scenes that were waiting on it"
+ "proximitySupensionMode"
+ "published layout for display: %{public}@ layout: %{public}@ transition: %{public}@"
+ "removing resident inactive stage %{public}@ for reason: %{public}@"
+ "requestedIndicatorElevationStyle"
+ "scene %@ has a process pending exit (%@); waiting for it to exit before recreating"
+ "scene adopting layout publisher %{public}@ for root: %{public}@ delegate: %p"
+ "soft"
+ "stageResolverBlock"
+ "systemApertureUnifiedAnimationEnabled"
+ "untracked window scene"
+ "usesSecureIndicatorLayer"
+ "v12@?0C8"
+ "wantsResidentInactiveStage: %{public}@ hasAnyStages: %{public}@ noResidentInactiveStageReason: %{public}@"
+ "won't remove stage %{public}@ for reason: %{public}@ because its not resident inactive"
+ "\xb31\xb1"
- "#PreprocessNotification clearing the current preprocess request"
- "-[SBAppResizingCoordinator resizingAvailability]"
- "-[SBHomeScreenService canSwapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:]"
- "-[SBHomeScreenService swapApplicationIconsInProminentPositionsWithBundleIdentifier:withApplicationIconsWithWithBundleIdentifier:]"
- "Added disable wallet pre-arm assertion of type %@ for reason: %@"
- "Arming match passcode fallback timer"
- "DeviceUnsupported"
- "Dismissing Assistant Island because Cover Sheet will present."
- "Glass Dismiss Alpha Fraction"
- "Horizontal Inter Item Padding"
- "LegacyApplication"
- "Lift to wake enablement changed to: %{public}@ (Available: %{public}@, UserPref: %{public}@, Bump: %{BOOL}u)"
- "Match passcode fallback fired, showing passcode UI while biometric match continues."
- "NSString * _Nonnull SBResizingAvailabilityDescription(SBResizingAvailability)"
- "No resizable app because %{public}@ isn't resizable: %{public}@"
- "NoApplication"
- "Removed disable wallet pre-arm assertion of type %@ for reason: %@"
- "ResizingAvailable"
- "SBActivityMetrics.m"
- "SBApplication+SwitcherCapabilities.m"
- "SBForceFullScreenKeyboardForAllApps"
- "Same scene re-evaluation with no external presenter: canFallbackToDefaultPresenter=%{BOOL}d previousPresenter=%{public}@ focusedScene=%{public}@"
- "Should system gesture receive touch with location:%@ <%@> ignoringUCB:%@ keyboardIsUCB:%@ touchIsInsideKeyboard:%@"
- "Updating container rendering style to: %{public}@, cloning style: %{public}@"
- "Updating curtain rendering style to: %{public}@, cloning style: %{public}@"
- "Updating system aperture metrics for all active elements due to window scene change"
- "Vertical Inter Item Padding"
- "[%{public}lu] Ejection is not viable, so ensure the intersensor region indicator is visible, and the micro is accepted. Reachability active: %{BOOL}u; Backlight On: %{BOOL}u; Are there portrait elements in Jindo: %{BOOL}u; AppearanceStateContext: %@"
- "[ActivityID: %{public}@] Updating alert system aperture metrics"
- "[ActivityID: %{public}@] Updating system aperture metrics"
- "[unknown]"
- "_previousCurtainRenderingStyle"
- "anchorPoint.x"
- "anchorPoint.y"
- "a\xf0\xf01"
- "customBannerTransitionStyleGlass_dismissAlphaFraction"
- "menu bar visible over wallpaper"
- "ndoherty -- campoAppSceneMayStealMyCommonUIScene update complete, success=%{public}@, launching campo app"
- "ndoherty -- stageState→app: setting campoAppSceneMayStealMyCommonUIScene=YES, stage=%{public}@"
- "q%Q\""
- "screen"
- "suspendProximitySensor"
- "unhandled SBResizingAvailability: %ld"
- "\x92"
- "\xa31\xb1"
- "\xf0\xf01"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc2\xf0\xf1"
- "\xf0\xf2\x81"
```
