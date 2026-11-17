## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__ustring`

```diff

-4637.2.11.104.0
-  __TEXT.__text: 0xc4deec
+4637.2.17.3.0
+  __TEXT.__text: 0xc671dc
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xd38fc
-  __TEXT.__const: 0x11e60
-  __TEXT.__oslogstring: 0x79b76
-  __TEXT.__cstring: 0x92951
-  __TEXT.__gcc_except_tab: 0x1b0f0
+  __TEXT.__objc_methlist: 0xd4f04
+  __TEXT.__const: 0x11ef0
+  __TEXT.__oslogstring: 0x7b37a
+  __TEXT.__cstring: 0x93c21
+  __TEXT.__gcc_except_tab: 0x1b4fc
   __TEXT.__ustring: 0x102c
   __TEXT.__dlopen_cstrs: 0x373
-  __TEXT.__unwind_info: 0x40988
+  __TEXT.__unwind_info: 0x41180
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x202c0
-  __DATA_CONST.__objc_classlist: 0x5c30
+  __DATA_CONST.__const: 0x20618
+  __DATA_CONST.__objc_classlist: 0x5c90
   __DATA_CONST.__objc_catlist: 0x360
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2cb8
+  __DATA_CONST.__objc_protolist: 0x2ce8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x57018
+  __DATA_CONST.__objc_selrefs: 0x57b78
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x46e8
-  __DATA_CONST.__objc_arraydata: 0x1d90
-  __DATA_CONST.__got: 0xb448
-  __AUTH_CONST.__const: 0x11bc8
-  __AUTH_CONST.__cfstring: 0x81f40
-  __AUTH_CONST.__objc_const: 0x2c37a0
+  __DATA_CONST.__objc_superrefs: 0x4738
+  __DATA_CONST.__objc_arraydata: 0x1dc0
+  __DATA_CONST.__got: 0xb500
+  __AUTH_CONST.__const: 0x11d88
+  __AUTH_CONST.__cfstring: 0x831e0
+  __AUTH_CONST.__objc_const: 0x2c6ab0
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x1c08
-  __AUTH_CONST.__objc_doubleobj: 0xb40
-  __AUTH_CONST.__objc_intobj: 0x32d0
+  __AUTH_CONST.__objc_arrayobj: 0x1bf0
+  __AUTH_CONST.__objc_doubleobj: 0xba0
+  __AUTH_CONST.__objc_intobj: 0x32b8
   __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH_CONST.__auth_got: 0x2e98
-  __AUTH.__objc_data: 0x12200
-  __DATA.__objc_ivar: 0x11e44
-  __DATA.__data: 0x225d0
+  __AUTH_CONST.__auth_got: 0x2ed8
+  __AUTH.__objc_data: 0x12570
+  __DATA.__objc_ivar: 0x12080
+  __DATA.__data: 0x22820
   __DATA.__common: 0xa40
-  __DATA_DIRTY.__objc_data: 0x277e0
-  __DATA_DIRTY.__data: 0x170
+  __DATA_DIRTY.__objc_data: 0x27830
+  __DATA_DIRTY.__data: 0x168
   __DATA_DIRTY.__bss: 0x1a90
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  Functions: 82312
-  Symbols:   132277
-  CStrings:  26297
+  Functions: 82886
+  Symbols:   133127
+  CStrings:  26540
 
Symbols:
+ +[SBCompanionSceneForegroundConstraint foregroundOrUnderLockConstraint]
+ +[SBHomeScreenController _shouldDismissSpotlightForTransitionSource:previousHomeScreenRegion:newHomeScreenRegion:]
+ +[SBIconController proactiveStackInsertionIndexForScreenType:inIcons:]
+ +[SBLockOnFoldDomain domainGroupName]
+ +[SBLockOnFoldDomain domainName]
+ +[SBLockOnFoldDomain rootSettingsClass]
+ +[SBLockOnFoldDomain rootSettings]
+ +[SBLockOnFoldSettings settingsControllerModule]
+ +[SBSafeAreaResolverUtility mirrorsStatusBarSafeAreaForScreenRegion:]
+ +[SBSceneBarPositionResolverUtility barSizeClassResolverForScreenType:isPhone:systemProvidesVerticalBars:]
+ +[SBSceneBarPositionResolverUtility preferredLandscapeBarPositionForScreenRegion:]
+ +[SBSceneManager _shouldDenySceneRequestWithOptions:targetWindowScene:]
+ +[SBSceneManager _targetWindowSceneForSceneRequestFromWindowScene:activeWindowScene:]
+ +[SBSystemApertureBackgroundBlurView maskFalloffLength]
+ +[SBSystemApertureViewControllerRotationTransitionContext transformForRotationToInterfaceOrientation:]
+ -[FBMainDisplayLayoutPublisher(SpringBoard) SB_stopObservingDisplaysAndBacklight]
+ -[FBScene(SafeAreaResolverExtensionDelegate) sb_reevaluateSafeAreaResolverExtension]
+ -[FBScene(SafeAreaResolverExtensionDelegate) sb_safeAreaResolverExtensionScreenRegion]
+ -[FBScene(SafeAreaResolverExtensionDelegate) sb_safeAreaResolverHostComponent]
+ -[FBScene(SceneBarPositionResolverExtension) sb_reevaluateBarPositionResolverExtension]
+ -[SBActivityAlert priority]
+ -[SBActivityCoverSheetObserver shouldDropAlert:]
+ -[SBActivityManager _shouldDropAlert:]
+ -[SBActivityModalPresentationController _presentedEntity]
+ -[SBActivityModalPresentationController presentModalForAlert:completion:]
+ -[SBActivityModalPresentationController shouldDropAlert:]
+ -[SBAffordancePresenceController setAutoHideSuspended:forReason:]
+ -[SBAmbientIdleTimerController _suppressionRequestsMotionWake]
+ -[SBAnalyticsEventsControllerForIconController _analyticsLoggingForTodayViewLayout]
+ -[SBAnalyticsEventsControllerForIconController _defaultTodayList]
+ -[SBAnalyticsEventsControllerForIconController _isMediumWidgetStackIcon:]
+ -[SBAnalyticsEventsControllerForIconController _isTodayViewDefaultIconAvailable:]
+ -[SBAnalyticsEventsControllerForIconController _todayListInRootFolder:]
+ -[SBAnalyticsEventsControllerForIconController _todayViewLayoutStateForTodayList:defaultTodayList:]
+ -[SBAnalyticsEventsControllerForIconController _todayViewSignaturesForIcons:]
+ -[SBAnalyticsEventsControllerForIconController initWithIconModel:isWidgetContainerAvailable:proactiveStackInsertionIndex:]
+ -[SBAnalyticsEventsControllerForIconController isWidgetContainerAvailable]
+ -[SBAnalyticsEventsControllerForIconController proactiveStackInsertionIndex]
+ -[SBAppSwitcherContinuousExposeSwitcherModifier appSuggestionBannerRegionFrame]
+ -[SBApplicationRestrictionController _destroyRestrictedWebClipSceneHandles]
+ -[SBApplicationRestrictionController _updateAllowedWebClipIdentifiers]
+ -[SBApplicationRestrictionController allowedWebClipIdentifiers]
+ -[SBApplicationRestrictionController isWebClipAllowlistActive]
+ -[SBApplicationRestrictionController isWebClipIdentifierRestricted:]
+ -[SBAssistantIslandStageCoordinator _isOnLockScreenForWindowScene:]
+ -[SBAssistantIslandStageCoordinator _isPresentingResponseInIslandOnLockScreen]
+ -[SBAssistantIslandStageCoordinator _lockedIdleTimerCapDelay]
+ -[SBAssistantIslandStageCoordinator _lockedIdleTimerCapDidElapse]
+ -[SBAssistantIslandStageCoordinator _proposeIdleTimerBehaviorForReason:]
+ -[SBAssistantIslandStageCoordinator _resetLockedIdleTimerCapForReason:]
+ -[SBAssistantIslandStageCoordinator _updateLockedIdleTimerCapForReason:]
+ -[SBAssistantIslandStageCoordinator assistantIdleTimerStateDidChange:]
+ -[SBAssistantIslandStageCoordinator gestureManagerActivityDragRequiresResponseEditingAvoidance:]
+ -[SBAssistantIslandStageCoordinator stageControllerStageStateDidChange:]
+ -[SBAssistantIslandStageCoordinator suppressesQuickUnwarnExtension]
+ -[SBBLSAssertionWrapper _invokePendingSettledHandlersIfSettled]
+ -[SBBLSAssertionWrapper isSettled]
+ -[SBBLSAssertionWrapper pendingSettledHandlers]
+ -[SBBLSAssertionWrapper performWhenSettled:]
+ -[SBBLSAssertionWrapper setPendingSettledHandlers:]
+ -[SBBacklightController _callSupersededBacklightCompletions]
+ -[SBBacklightController performAfterAssertionTransitionsSettle:]
+ -[SBBiometricEventLogger biometricResource:observeEvent:forDeviceKind:]
+ -[SBBiometricMonitorPearlDataSource biometricResource:observeEvent:forDeviceKind:]
+ -[SBBiometricOcclusionMonitor _updateBioConvenienceSuppressionAssertion]
+ -[SBButterflyDeckLayoutModifier _frameForLeafAppLayout:spaceIndex:scrollProgress:]
+ -[SBButterflyDeckLayoutModifier appSuggestionBannerRegionFrame]
+ -[SBButterflyDefaultImplementationsWindowingModifier displayItemsAllowingSubtitlesInAppLayout:]
+ -[SBButterflyHomeGestureWindowingModifier _canEnterReduceMotionSwitcherDuringGesture]
+ -[SBButterflyHomeGestureWindowingModifier _hasPausedForAppSwitcherInReduceMotion]
+ -[SBButterflyHomeGestureWindowingModifier _isShowingSwitcherForReduceMotion]
+ -[SBButterflyHomeGestureWindowingModifier _reduceMotionSwitcherLayoutForFinalDestination:]
+ -[SBButterflyHomeGestureWindowingModifier _shouldFadeOutVisibleDividerElements]
+ -[SBButterflyHomeGestureWindowingModifier _skipsLayoutAnimationsForReduceMotionCrossfade]
+ -[SBButterflyHomeGestureWindowingModifier _throttledReduceMotionFinalDestinationForLiveFinalDestination:]
+ -[SBButterflyHomeGestureWindowingModifier _wantsVisibleDividerElements]
+ -[SBButterflyHomeGestureWindowingModifier(FinalDestination) _isInDropZoneForReduceMotionSwitcherWithScreenRegion:]
+ -[SBButterflyHomeGestureWindowingModifier(FinalDestination) _isWaitingForReduceMotionSwitcherToEnableDropZones]
+ -[SBCameraOverlayUISceneController _windowSceneForRequest:]
+ -[SBCloseToLockHostComponent .cxx_destruct]
+ -[SBCloseToLockHostComponent _invalidateCloseToLockDisabledAssertion]
+ -[SBCloseToLockHostComponent _updateCloseToLockDisabledAssertion]
+ -[SBCloseToLockHostComponent invalidate]
+ -[SBCloseToLockHostComponent scene:didUpdateClientSettings:]
+ -[SBCloseToLockHostComponent setScene:]
+ -[SBContinuityDisplayDelayedUIWindowSceneDelegate surfaceType]
+ -[SBContinuitySessionSystemEventMonitor _lockState]
+ -[SBContinuousFadeEffectViewController _initialContentMode]
+ -[SBContinuousFadeEffectViewController _updateDimForCurrentProgress]
+ -[SBContinuousFoldSnapshotCoordinator liftCloakWithoutAnimationForWindowScene:]
+ -[SBCoverSheetBiometricResourceObserver biometricResource:observeEvent:forDeviceKind:]
+ -[SBCoverSheetGrabberViewController _timeLabelFrameInWindow:statusBar:rightToLeft:]
+ -[SBCoverSheetPresentationManager _acquireKeyboardFocusAssertionIfNeeded]
+ -[SBCoverSheetPresentationManager _cleanupATransitionRelinquishingSystemAnimation:]
+ -[SBCoverSheetPresentationManager _queue_relinquishSystemAnimation]
+ -[SBCoverSheetPresentationManager _relinquishSystemAnimation]
+ -[SBCoverSheetSpotlightPresenter setWindowScene:]
+ -[SBCoverSheetSpotlightPresenter windowScene]
+ -[SBCrossfadeChangeSwitcherEventResponse .cxx_destruct]
+ -[SBCrossfadeChangeSwitcherEventResponse crossfadeDuration]
+ -[SBCrossfadeChangeSwitcherEventResponse initWithWrappedResponse:crossfadeDuration:]
+ -[SBCrossfadeChangeSwitcherEventResponse type]
+ -[SBCrossfadeChangeSwitcherEventResponse wrappedResponse]
+ -[SBDashBoardActivityModalHostableEntity activityItem]
+ -[SBDashBoardActivityModalHostableEntity alertPriority]
+ -[SBDashBoardActivityModalHostableEntity requiresDeliberateDismissGesture]
+ -[SBDashBoardActivityModalHostableEntity setAlertPriority:]
+ -[SBDashBoardBiometricUnlockController handleBiometricEvent:forDeviceKind:]
+ -[SBDashBoardBiometricUnlockController isBiometricMatchingPossible]
+ -[SBDashBoardBiometricUnlockController lastBioUnlockDeviceKind]
+ -[SBDashBoardHostableEntityHostingFluidSwitcherViewController _currentHostableEntityRequiresDeliberateDismissGesture]
+ -[SBDashBoardHostableEntityPresentationManager presentedEntity]
+ -[SBDashBoardLockScreenEnvironment handleBiometricEvent:forDeviceKind:]
+ -[SBDashBoardLockScreenEnvironment traitsParticipantForSceneHandle:]
+ -[SBDashBoardMesaUnlockBehavior handleBiometricEvent:forDeviceKind:]
+ -[SBDashBoardPearlUnlockBehavior handleBiometricEvent:forDeviceKind:]
+ -[SBDashBoardPosterSwitcherViewController traitsParticipantForSceneHandle:]
+ -[SBDashBoardSecureCaptureExtensionHostableEntity _hostingWindowScene]
+ -[SBDashBoardSecureCaptureExtensionHostableEntity _lockScreenManager]
+ -[SBDashBoardSecureCaptureExtensionHostableEntity captureApplicationSupportsSceneResizingInWindowScene:]
+ -[SBDashBoardSetupViewController _checkIfSecureEraseFailed]
+ -[SBDashBoardSetupViewController _presentSecureEraseFailedUI]
+ -[SBDashBoardSetupViewController dismissSecureEraseFailedUIAnimated:]
+ -[SBDashBoardSetupViewController fadeCursiveHelloToVisible:duration:]
+ -[SBDashBoardSetupViewController initWithCoverSheetViewController:telephonyManager:obliterationController:]
+ -[SBDashBoardSetupViewController secureEraseFailedViewControllerDidAcknowledgeFailure:]
+ -[SBDashBoardTraitsAwareAppHostingViewController traitsParticipantForSceneHandle:]
+ -[SBDeckSwitcherModifier _frameForIndex:scrollProgress:]
+ -[SBDeckSwitcherModifier _scaleForIndex:scrollProgress:]
+ -[SBDeckSwitcherModifier appSuggestionBannerRegionFrame]
+ -[SBDeckSwitcherViewController bannerRegionFrameForSuggestionViewController:]
+ -[SBDefaultAuthenticationPolicy didCachePassphrase]
+ -[SBDefaultAuthenticationPolicy setDidCachePassphrase:]
+ -[SBDefaultImplementationsSwitcherModifier displayItemsAllowingSubtitlesInAppLayout:]
+ -[SBDisplayContentModeCoordinator liftContinuousFoldCloakWithoutAnimationForWindowScene:]
+ -[SBDisplayLayoutPublisherCoordinator _acquireSpuriousTargetPublisherUpdatePreventionAssertion]
+ -[SBDisplayRegionBlankingLatencyTracker noteDisplayInactiveForRegion:]
+ -[SBFluidSwitcherAnimationSettings reduceMotionDropZoneCrossfadeDuration]
+ -[SBFluidSwitcherAnimationSettings setReduceMotionDropZoneCrossfadeDuration:]
+ -[SBFluidSwitcherItemContainerHeaderView _glyphBoundsForLabel:]
+ -[SBFluidSwitcherItemContainerHeaderView _hasSubtitleGivenSubtitleLabelView:]
+ -[SBFluidSwitcherItemContainerHeaderView _hasTitleGivenTitleLabel:]
+ -[SBFluidSwitcherItemContainerHeaderView _layoutMetricsForTitleLabel:subtitleLabelView:includingTitle:includingSubtitle:]
+ -[SBFluidSwitcherItemContainerHeaderView _multiWindowIndicatorAlphaForItem:]
+ -[SBFluidSwitcherItemContainerHeaderView _shouldUpdateIconImageViewCustomImageViewForItem:givenPreviousItem:]
+ -[SBFluidSwitcherItemContainerHeaderView _showsMultipleWindowsIndicatorGivenIndicatorView:item:]
+ -[SBFluidSwitcherItemContainerHeaderView _showsSubtitleGivenSubtitleLabelView:item:]
+ -[SBFluidSwitcherItemContainerHeaderView _subtitleAlphaForItem:]
+ -[SBFluidSwitcherItemContainerHeaderView _updateTallScriptMetrics]
+ -[SBFluidSwitcherSpaceTitleItem setShowsSubtitle:]
+ -[SBFluidSwitcherSpaceTitleItem showsSubtitle]
+ -[SBFluidSwitcherSpaceTitleItemController displayItemsAllowingSubtitles]
+ -[SBFluidSwitcherSpaceTitleItemController setDisplayItemsAllowingSubtitles:]
+ -[SBFluidSwitcherViewController _performCrossfadeIfNeededWithDuration:completion:]
+ -[SBFluidSwitcherViewController _performModifierCrossfadeChangeResponse:]
+ -[SBFluidSwitcherViewController _updateExclusiveKeyboardTouchRegionForKeyboardFrameNotification:]
+ -[SBFluidSwitcherViewController supportedReachabilityAxis]
+ -[SBFullScreenToHomeSystemApertureSwitcherModifier _narrowMesh:toAspectRatio:]
+ -[SBFullScreenToHomeSystemApertureSwitcherModifier _taperTopOfMesh:byWidthFactor:]
+ -[SBFullScreenToHomeSystemApertureSwitcherModifier _tuckInThreshold]
+ -[SBFullScreenToHomeSystemApertureSwitcherModifier _updateApproachHeadingForThroughPoint:equilibrium:startPosition:startVelocity:params:]
+ -[SBFullScreenToHomeSystemApertureSwitcherModifier _zoomToJindoPositionSettings]
+ -[SBHIDEventDispatchController _currentMainRootDispatchingRules]
+ -[SBHIDEventDispatchController _initWithDeliveryManager:pencilPreferredActionProvider:routeDoubleTapForVIEnabled:]
+ -[SBHIDEventDispatchController _pencilPreferredActionsDidChange]
+ -[SBHIDEventDispatchController _shouldRoutePencilDoubleTapToSystem]
+ -[SBHIDEventDispatchController _shouldRoutePencilSqueezeToSystem]
+ -[SBHIDUISensorModeController _isAnyBacklightOnOrTurningOn]
+ -[SBHomeScreenController _dismissSpotlightIfLaunchingFromItWithTransitionSource:previousHomeScreenRegion:newHomeScreenRegion:]
+ -[SBHomeScreenController _expandLibraryPodWithCategoryIdentifier:]
+ -[SBHomeScreenController _windowSceneDidUpdateReachabilityController:]
+ -[SBHomeScreenController handleReachabilityModeActivated]
+ -[SBHomeScreenController handleReachabilityModeDeactivated]
+ -[SBHomeScreenController latestTopEdgeTouchBeganInReachabilityVacatedRegion]
+ -[SBHomeScreenController pendingExpandedLibraryCategoryIdentifier]
+ -[SBHomeScreenController setPendingExpandedLibraryCategoryIdentifier:]
+ -[SBHomeScreenService addApplicationIconToHomeScreenIfAbsentWithBundleIdentifier:]
+ -[SBIconController _isWidgetContainerAvailable:]
+ -[SBIconModel placesPreinstalledApplicationsMissingFromDefaultIconStateOnIgnoredList]
+ -[SBIdleTimerBehavior suppressesQuickUnwarnExtension]
+ -[SBLockElementViewProvider _bioConvenienceMatchOperationDetectedFaceInView]
+ -[SBLockElementViewProvider _bioConvenienceMatchOperationEnded]
+ -[SBLockElementViewProvider _bioConvenienceMatchOperationStarted]
+ -[SBLockElementViewProvider _biometricDeviceKindForLockElementBiometrics]
+ -[SBLockElementViewProvider _cancelPendingBioConvenienceDisplayTimeout]
+ -[SBLockElementViewProvider _endBioConvenienceSearch]
+ -[SBLockElementViewProvider _isBioConvenienceAvailable]
+ -[SBLockElementViewProvider _isBioConvenienceOnly]
+ -[SBLockElementViewProvider _primaryBiometricsAvailable]
+ -[SBLockElementViewProvider _showsBioConvenienceGlyph]
+ -[SBLockElementViewProvider biometricResource:observeEvent:forDeviceKind:]
+ -[SBLockOnFoldCoordinator .cxx_destruct]
+ -[SBLockOnFoldCoordinator _animateFadeWindow:toVisible:dampingRatio:response:windowScene:]
+ -[SBLockOnFoldCoordinator _canCommitInPose:]
+ -[SBLockOnFoldCoordinator _commitOnCoverWindowScene:]
+ -[SBLockOnFoldCoordinator _establishHingeBaselineIfNeededWithPose:]
+ -[SBLockOnFoldCoordinator _fadeWindowForWindowScene:createIfNeeded:]
+ -[SBLockOnFoldCoordinator _handleDisplayContentModeChange]
+ -[SBLockOnFoldCoordinator _handlePostflightForContext:tracksFold:]
+ -[SBLockOnFoldCoordinator _hideStatusBarOnWindowScene:]
+ -[SBLockOnFoldCoordinator _holdFadeWindowsForCommit]
+ -[SBLockOnFoldCoordinator _isHingeAtCommitPositionInPose:]
+ -[SBLockOnFoldCoordinator _isHingeKnownInPose:]
+ -[SBLockOnFoldCoordinator _isHingeOpenInPose:]
+ -[SBLockOnFoldCoordinator _isLockOnFoldEnabled]
+ -[SBLockOnFoldCoordinator _liftFoldCloakOnWindowScene:]
+ -[SBLockOnFoldCoordinator _noteLockStartedForStatusBarHide]
+ -[SBLockOnFoldCoordinator _performCommit]
+ -[SBLockOnFoldCoordinator _releaseStatusBarHide]
+ -[SBLockOnFoldCoordinator _setArmed:reason:]
+ -[SBLockOnFoldCoordinator _setFadeWindow:triggered:]
+ -[SBLockOnFoldCoordinator _setFadeWindowVisible:animated:windowScene:]
+ -[SBLockOnFoldCoordinator _setFadeWindowsTriggered:]
+ -[SBLockOnFoldCoordinator _setFadeWindowsVisible:animated:]
+ -[SBLockOnFoldCoordinator _setPhase:]
+ -[SBLockOnFoldCoordinator _showFadeWindowOpaqueIfCloakedOnWindowScene:]
+ -[SBLockOnFoldCoordinator _sleepAndLock]
+ -[SBLockOnFoldCoordinator _suppressLiftToWake]
+ -[SBLockOnFoldCoordinator _transitionContextEndsWithContentOnCover:]
+ -[SBLockOnFoldCoordinator _transitionContextMovesContentToCover:]
+ -[SBLockOnFoldCoordinator acquireCloseToLockDisabledAssertionForReason:]
+ -[SBLockOnFoldCoordinator appendDescriptionToStream:]
+ -[SBLockOnFoldCoordinator dealloc]
+ -[SBLockOnFoldCoordinator description]
+ -[SBLockOnFoldCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:]
+ -[SBLockOnFoldCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:]
+ -[SBLockOnFoldCoordinator initWithSettings:displayContentModeCoordinator:devicePoseProvider:screenSleepCoordinator:securityDefaults:liveRenderingAssertionProvider:]
+ -[SBLockOnFoldCoordinator poseProvider:didUpdateFromPose:toPose:]
+ -[SBLockOnFoldCoordinator setWallpaperControllerCoordinator:]
+ -[SBLockOnFoldCoordinator statusBarAssertionManager:addStatusBarSettingsAssertion:]
+ -[SBLockOnFoldCoordinator triggerDidFire:]
+ -[SBLockOnFoldCoordinator wallpaperControllerCoordinator]
+ -[SBLockOnFoldFadeRootViewController _canShowWhileLocked]
+ -[SBLockOnFoldFadeTrigger .cxx_destruct]
+ -[SBLockOnFoldFadeTrigger _disarm]
+ -[SBLockOnFoldFadeTrigger _fire]
+ -[SBLockOnFoldFadeTrigger _noteVelocitySatisfied]
+ -[SBLockOnFoldFadeTrigger _updateForAngle:velocity:acceleration:]
+ -[SBLockOnFoldFadeTrigger arm]
+ -[SBLockOnFoldFadeTrigger dealloc]
+ -[SBLockOnFoldFadeTrigger delegate]
+ -[SBLockOnFoldFadeTrigger initWithSettings:]
+ -[SBLockOnFoldFadeTrigger initWithSettings:timerProvider:]
+ -[SBLockOnFoldFadeTrigger isTriggered]
+ -[SBLockOnFoldFadeTrigger poseProvider:didUpdateFromPose:toPose:]
+ -[SBLockOnFoldFadeTrigger poseProvider]
+ -[SBLockOnFoldFadeTrigger reset]
+ -[SBLockOnFoldFadeTrigger setDelegate:]
+ -[SBLockOnFoldFadeTrigger setPoseProvider:]
+ -[SBLockOnFoldFadeWindow isVisible]
+ -[SBLockOnFoldFadeWindow setVisible:]
+ -[SBLockOnFoldSettings commitWhenContentReachesCover]
+ -[SBLockOnFoldSettings contentFadeInDampingRatio]
+ -[SBLockOnFoldSettings contentFadeInDelay]
+ -[SBLockOnFoldSettings contentFadeInResponse]
+ -[SBLockOnFoldSettings contentFadeReversalDampingRatio]
+ -[SBLockOnFoldSettings contentFadeReversalResponse]
+ -[SBLockOnFoldSettings fadeStartHingeMonitoringAngleThreshold]
+ -[SBLockOnFoldSettings fadeStartHingeVelocityThreshold]
+ -[SBLockOnFoldSettings fadeWhenCoverSheetPresented]
+ -[SBLockOnFoldSettings liftToWakeSuppressionDuration]
+ -[SBLockOnFoldSettings setCommitWhenContentReachesCover:]
+ -[SBLockOnFoldSettings setContentFadeInDampingRatio:]
+ -[SBLockOnFoldSettings setContentFadeInDelay:]
+ -[SBLockOnFoldSettings setContentFadeInResponse:]
+ -[SBLockOnFoldSettings setContentFadeReversalDampingRatio:]
+ -[SBLockOnFoldSettings setContentFadeReversalResponse:]
+ -[SBLockOnFoldSettings setDefaultValues]
+ -[SBLockOnFoldSettings setFadeStartHingeMonitoringAngleThreshold:]
+ -[SBLockOnFoldSettings setFadeStartHingeVelocityThreshold:]
+ -[SBLockOnFoldSettings setFadeWhenCoverSheetPresented:]
+ -[SBLockOnFoldSettings setLiftToWakeSuppressionDuration:]
+ -[SBLockOnFoldSettings setStartFadeFromHingeVelocity:]
+ -[SBLockOnFoldSettings setVisualizeFadeTrigger:]
+ -[SBLockOnFoldSettings startFadeFromHingeVelocity]
+ -[SBLockOnFoldSettings visualizeFadeTrigger]
+ -[SBLockScreenBiometricAuthenticationCoordinator biometricResource:observeEvent:forDeviceKind:]
+ -[SBLockScreenCoordinator _publishUILockStateToOtherProcesses]
+ -[SBLockScreenCoordinator _sendUILockStateChangedNotification]
+ -[SBLockScreenCoordinator handleBiometricEvent:forDeviceKind:]
+ -[SBLockScreenCoordinator noteStartupTransitionDidComplete]
+ -[SBLockScreenManager _attemptPhoneUnlockWithRemoteDeviceIfNeededForUnlockRequest:]
+ -[SBLockScreenManager _phoneUnlockWithWatchController]
+ -[SBLockScreenManager isSecureAppAccessBlockedByLockOut]
+ -[SBLockScreenSessionAnalyticsTracker biometricResource:observeEvent:forDeviceKind:]
+ -[SBLockScreenViewControllerBase handleBiometricEvent:forDeviceKind:]
+ -[SBMainDisplaySceneLayoutStatusBarView _updatePreferredStatusBarAxisWithAnimationParameters:]
+ -[SBMainDisplaySceneLayoutStatusBarView sceneWithIdentifier:didChangeStatusBarAxisTo:withAnimationParameters:]
+ -[SBNonInteractiveDisplayController nonInteractivePresentationLegacyAppSceneBackgrounded:]
+ -[SBNonInteractivePresentation scene:didUpdateSettings:]
+ -[SBPIPController _coverSheetPresentationHidingDidChangeOnWindowScene:]
+ -[SBPIPPegasusContainerAdapter _classicAppZoomedInDidChange:]
+ -[SBPIPPegasusContainerAdapter _isApplicationZoomedInBeneathSplitPIP]
+ -[SBPIPPegasusContainerAdapter _isSplitPIPKeyboardCompact]
+ -[SBPIPPegasusContainerAdapter _wantsSplitPIPKeyboardCompactLayout]
+ -[SBPearlInterlockObserver biometricResource:observeEvent:forDeviceKind:]
+ -[SBPencilPreferredActionProvider .cxx_destruct]
+ -[SBPencilPreferredActionProvider dealloc]
+ -[SBPencilPreferredActionProvider init]
+ -[SBPencilPreferredActionProvider observeValueForKeyPath:ofObject:change:context:]
+ -[SBPencilPreferredActionProvider preferredActionsDidChangeHandler]
+ -[SBPencilPreferredActionProvider preferredSqueezeAction]
+ -[SBPencilPreferredActionProvider preferredTapAction]
+ -[SBPencilPreferredActionProvider setPreferredActionsDidChangeHandler:]
+ -[SBPrototypeAdvancedActivityElementViewProvider _isMinimalViewOval]
+ -[SBPrototypeAdvancedActivityElementViewProvider _updateMinimalView]
+ -[SBReachabilityController _topEdgeRegionSizeForOffset:bounds:]
+ -[SBReachabilityController _unreachablePointForScreenPoint:effectiveOffset:bounds:]
+ -[SBReachabilityController _updateTouchRegionsForHorizontalReachabilityOffset:mode:]
+ -[SBReachabilityController activateReachabilityOnScreenEdgeIfPossible:]
+ -[SBReachabilityController reachabilityAxis]
+ -[SBReachabilityController reachabilityTopEdgeRegionSize]
+ -[SBReachabilityController setReachabilityAxis:]
+ -[SBReachabilityController unreachablePointForScreenPoint:]
+ -[SBReachabilityController unreachableXForScreenX:]
+ -[SBReachabilityGestureRecognizer _clearHorizontalGestureTimer]
+ -[SBReachabilityGestureRecognizer _horizontalGestureTimeoutFired:]
+ -[SBReachabilityGestureRecognizer horizontalGestureCancelTimer]
+ -[SBReachabilityGestureRecognizer setHorizontalGestureCancelTimer:]
+ -[SBReachabilitySettings horizontalActivationMaxAngleForVerticalMovement]
+ -[SBReachabilitySettings horizontalActivationMinimumSpeed]
+ -[SBReachabilitySettings horizontalGestureAllowableEdgeMarginForCompletion]
+ -[SBReachabilitySettings horizontalGestureTouchHoldTimeout]
+ -[SBReachabilitySettings horizontalInteractiveKeepAlive]
+ -[SBReachabilitySettings setHorizontalActivationMaxAngleForVerticalMovement:]
+ -[SBReachabilitySettings setHorizontalActivationMinimumSpeed:]
+ -[SBReachabilitySettings setHorizontalGestureAllowableEdgeMarginForCompletion:]
+ -[SBReachabilitySettings setHorizontalGestureTouchHoldTimeout:]
+ -[SBReachabilitySettings setHorizontalInteractiveKeepAlive:]
+ -[SBRecentDisplayItemsController _removeDisplayItemsForRestrictedWebClips]
+ -[SBRecordingIndicatorLayer isRinged]
+ -[SBRecordingIndicatorLayer isSecure]
+ -[SBRecordingIndicatorLayer secureIndicatorLayer]
+ -[SBRecordingIndicatorRingedLayer .cxx_destruct]
+ -[SBRecordingIndicatorRingedLayer _layoutDotAndRing]
+ -[SBRecordingIndicatorRingedLayer blurRadius]
+ -[SBRecordingIndicatorRingedLayer boundingBoxes]
+ -[SBRecordingIndicatorRingedLayer indicatorType]
+ -[SBRecordingIndicatorRingedLayer initWithIndicatorType:secure:]
+ -[SBRecordingIndicatorRingedLayer initWithLayer:]
+ -[SBRecordingIndicatorRingedLayer isRinged]
+ -[SBRecordingIndicatorRingedLayer isSecure]
+ -[SBRecordingIndicatorRingedLayer layoutSublayers]
+ -[SBRecordingIndicatorRingedLayer secureIndicatorLayer]
+ -[SBRecordingIndicatorRingedLayer setBackgroundColor:]
+ -[SBRecordingIndicatorRingedLayer setBlurRadius:]
+ -[SBRecordingIndicatorRingedLayer setBounds:]
+ -[SBRecordingIndicatorSecureLayer isRinged]
+ -[SBRecordingIndicatorSecureLayer isSecure]
+ -[SBRecordingIndicatorSecureLayer secureIndicatorLayer]
+ -[SBRecordingIndicatorSettings guaranteedIndicatorContrastWidth]
+ -[SBRecordingIndicatorSettings setGuaranteedIndicatorContrastWidth:]
+ -[SBRecordingIndicatorView isRinged]
+ -[SBRecordingIndicatorView isSecure]
+ -[SBRecordingIndicatorView setRinged:]
+ -[SBRecordingIndicatorView setSecure:]
+ -[SBRecordingIndicatorVisualRepresentation dealloc]
+ -[SBRecordingIndicatorVisualRepresentation setUsesIndicatorRing:]
+ -[SBRecordingIndicatorVisualRepresentation setUsesSecureIndicatorLayer:]
+ -[SBRecordingIndicatorVisualRepresentation settings:changedValueForKey:]
+ -[SBRecordingIndicatorVisualRepresentation usesIndicatorRing]
+ -[SBRecordingIndicatorVisualRepresentation usesSecureIndicatorLayer]
+ -[SBRestToOpenSettings buttonWakeCoachingLeadIn]
+ -[SBRestToOpenSettings minimumCoachingVisibleDuration]
+ -[SBRestToOpenSettings minimumRemainingDurationForCoaching]
+ -[SBRestToOpenSettings pendingMatchRestToOpenDuration]
+ -[SBRestToOpenSettings setButtonWakeCoachingLeadIn:]
+ -[SBRestToOpenSettings setMinimumCoachingVisibleDuration:]
+ -[SBRestToOpenSettings setMinimumRemainingDurationForCoaching:]
+ -[SBRestToOpenSettings setPendingMatchRestToOpenDuration:]
+ -[SBRestToOpenSettings setShowCoachingDuringPendingMatch:]
+ -[SBRestToOpenSettings setSuppressCoachingNearRestToOpenFire:]
+ -[SBRestToOpenSettings setWakeRestToOpenDuration:]
+ -[SBRestToOpenSettings showCoachingDuringPendingMatch]
+ -[SBRestToOpenSettings suppressCoachingNearRestToOpenFire]
+ -[SBRestToOpenSettings wakeRestToOpenDuration]
+ -[SBRoutingSwitcherModifier appSuggestionBannerRegionFrame]
+ -[SBRoutingSwitcherModifier displayItemsAllowingSubtitlesInAppLayout:]
+ -[SBSAAcceptanceBounceBehaviorProvider _excursionDescriptionWithBounds:center:context:]
+ -[SBSAAcceptanceBounceBehaviorProvider _excursionRotationInContext:]
+ -[SBSAAcceptanceBounceBehaviorProvider _isVerticalExpansionForContainerViewDescription:context:]
+ -[SBSAAcceptanceBounceBehaviorProvider _preferencesBySuppressingKeyLinesInPreferences:]
+ -[SBSABlankingRegionLayoutProvider _rrRegionCoverageMilestoneForRegionElementContext:]
+ -[SBSAOrientationTransitionProvider .cxx_destruct]
+ -[SBSAOrientationTransitionProvider _preferencesByAvoidingSensorOfInterfaceOrientation:inPreferences:context:]
+ -[SBSAShadowPreferencesProvider _shadowStyleForContainerDescription:elementContext:useHeavyShadowForTransition:isFirstContainer:]
+ -[SBSAShakeBehaviorProvider _isNonCenterPillSensorVariantInContext:]
+ -[SBSAShakeBehaviorProvider _userHorizontalVectorFromContext:]
+ -[SBSafeAreaResolverHostComponent _screenRegionForScene:]
+ -[SBSafeAreaResolverHostComponent reevaluateSafeArea]
+ -[SBSafeAreaResolverUtility mirrorsStatusBarSafeArea]
+ -[SBSafeAreaResolverUtility setMirrorsStatusBarSafeArea:]
+ -[SBSceneRegionsUpdater _cutoutFrameWithUnpaddedFrame:]
+ -[SBSceneRegionsUpdater _padStatusBarOcclusionFrameForWindowScene:surfaceSize:settings:]
+ -[SBSceneRegionsUpdater _portraitTopSafeAreaInsetForScreenType:]
+ -[SBSceneRegionsUpdater _statusBarOcclusionFrameForSurfaceSize:settings:]
+ -[SBScreenSleepController _sleepAndLockUIFromSource:lockOptions:completion:]
+ -[SBSecureEraseFailedViewController .cxx_destruct]
+ -[SBSecureEraseFailedViewController _okButtonTapped:]
+ -[SBSecureEraseFailedViewController aggregateBehavior:]
+ -[SBSecureEraseFailedViewController delegate]
+ -[SBSecureEraseFailedViewController loadView]
+ -[SBSecureEraseFailedViewController messageLabel]
+ -[SBSecureEraseFailedViewController okButton]
+ -[SBSecureEraseFailedViewController presentationPriority]
+ -[SBSecureEraseFailedViewController presentationType]
+ -[SBSecureEraseFailedViewController setDelegate:]
+ -[SBSecureEraseFailedViewController viewDidLoad]
+ -[SBSecureIndicatorBacklightCoordinator noteIndicatorTypeWillChange]
+ -[SBShelfCarouselSwitcherModifier appSuggestionBannerRegionFrame]
+ -[SBSingleSceneController _discardClientSceneSession]
+ -[SBSpotlightMultiplexingViewController _reevaluateSafeAreaAndBarPosition]
+ -[SBSpotlightMultiplexingViewController screenRegionForSafeAreaScene:]
+ -[SBSwitcherSystemApertureSettings setZoomToJindoTrajectoryRotationCornerBackoff:]
+ -[SBSwitcherSystemApertureSettings setZoomToJindoTrajectoryRotationCornerFactor:]
+ -[SBSwitcherSystemApertureSettings setZoomToJindoTuckInCornerAspectRatio:]
+ -[SBSwitcherSystemApertureSettings setZoomToJindoTuckInCornerThreshold:]
+ -[SBSwitcherSystemApertureSettings setZoomToJindoTuckInCornerTopWidthFactor:]
+ -[SBSwitcherSystemApertureSettings zoomToJindoTrajectoryRotationCornerBackoff]
+ -[SBSwitcherSystemApertureSettings zoomToJindoTrajectoryRotationCornerFactor]
+ -[SBSwitcherSystemApertureSettings zoomToJindoTuckInCornerAspectRatio]
+ -[SBSwitcherSystemApertureSettings zoomToJindoTuckInCornerThreshold]
+ -[SBSwitcherSystemApertureSettings zoomToJindoTuckInCornerTopWidthFactor]
+ -[SBSystemApertureBackgroundBlurView _configureMaskView]
+ -[SBSystemApertureContainerView _setContentViewTransform:elementViewControllerInterfaceOrientation:]
+ -[SBSystemApertureContainerView _updateContentViewTransformImmediately]
+ -[SBSystemApertureContainerView activeElementInterfaceOrientationForSystemApertureElementOrientationObserver:]
+ -[SBSystemApertureContainerView elementOrientationAuthority]
+ -[SBSystemApertureContainerView elementOrientationDidChangeWithTransitionCoordinator:]
+ -[SBSystemApertureContainerView setElementOrientationAuthority:]
+ -[SBSystemApertureController animateTransitionAcceptanceBounceWithVelocityVector:inCoordinateSpace:triggeredBlock:]
+ -[SBSystemApertureControllerProxy animateTransitionAcceptanceBounceWithVelocityVector:inCoordinateSpace:triggeredBlock:]
+ -[SBSystemApertureSettings nonCenterPillShakeDisplacement]
+ -[SBSystemApertureSettings nonCenterPillShakeSensorExpansion]
+ -[SBSystemApertureSettings nonCenterPillShakeSensorOffset]
+ -[SBSystemApertureSettings setNonCenterPillShakeDisplacement:]
+ -[SBSystemApertureSettings setNonCenterPillShakeSensorExpansion:]
+ -[SBSystemApertureSettings setNonCenterPillShakeSensorOffset:]
+ -[SBSystemApertureViewController _axUnregisterForZoomUpdates]
+ -[SBSystemApertureViewController _refreshElementsLayoutDirection]
+ -[SBSystemApertureViewController _removeRunLoopObserverIfNecessary]
+ -[SBSystemApertureViewController _sensorVariantSupportsStackBasedOrientationUpdates]
+ -[SBSystemApertureViewController _updateLayoutDirectionAndLimitedSizeForElement:]
+ -[SBSystemApertureViewController activeElementInterfaceOrientationForSystemApertureElementOrientationObserver:]
+ -[SBSystemApertureViewController invalidate]
+ -[SBSystemApertureViewController(Private) _updateElementOrientationTo:withTransitionCoordinator:]
+ -[SBSystemApertureViewControllerRotationTransitionContext _affineTransform]
+ -[SBSystemApertureViewControllerRotationTransitionContext initWithTargetOrientation:]
+ -[SBSystemServiceServer _handleTestAutomationGetHomeScreenEditing:fromClient:]
+ -[SBSystemServiceServer _handleTestAutomationGetHomeScreenGridSize:fromClient:]
+ -[SBSystemServiceServer _handleTestAutomationOpenHomeScreenFolder:fromClient:]
+ -[SBSystemServiceServer _handleTestAutomationSetHomeScreenCurrentPageIndex:fromClient:]
+ -[SBSystemServiceServer _handleTestAutomationSetHomeScreenEditing:fromClient:]
+ -[SBTestAutomationService _closeAllFoldersWithIconManager:animated:remainingDepth:completion:]
+ -[SBTestAutomationService _folderViewForPageIndex:outViewPageIndex:]
+ -[SBTestAutomationService _rootFolderIconWithIdentifier:]
+ -[SBTestAutomationService systemServiceServer:client:getIsHomeScreenEditingWithCompletion:]
+ -[SBTestAutomationService systemServiceServer:client:homeScreenGridSizeForPageAtIndex:withCompletion:]
+ -[SBTestAutomationService systemServiceServer:client:openHomeScreenFolderWithIdentifier:animated:withCompletion:]
+ -[SBTestAutomationService systemServiceServer:client:setHomeScreenCurrentPageIndex:animated:withCompletion:]
+ -[SBTestAutomationService systemServiceServer:client:setHomeScreenEditing:]
+ -[SBTopAffordanceViewController _handleWindowControlsHover:]
+ -[SBTopAffordanceViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
+ -[SBTouchRegionManager _invalidateReachabilityRegistration:forDisplayIdentifier:]
+ -[SBTouchRegionManager _queue_exclusiveKeyboardHitTestRegionForLayout:]
+ -[SBTouchRegionManager _queue_reachabilityTransformForLayout:]
+ -[SBTouchRegionManager _queue_rectByExtendingRect:intoVacatedRegionWithinBounds:]
+ -[SBTouchRegionManager cachedTouchRegionBuffer]
+ -[SBTouchRegionManager registerReachabilityTransform:forDisplayIdentifier:]
+ -[SBTouchRegionManager setExclusiveKeyboardFrame:forDisplayIdentifier:]
+ -[SBTraitsOrientationDefaultResolutionPolicySpecifier _isParticipantAcquired:among:]
+ -[SBTransientOverlayScenePresenter _canUpdateStatusBar]
+ -[SBWallpaperControllerCoordinator _notifyWhenWallpaperAcknowledgesDisplayTransferWithCompletion:]
+ -[SBWallpaperControllerCoordinator _primaryWallpaperControllerForTransitionContext:]
+ -[SBWallpaperControllerCoordinator _transferWallpaperToPrimaryController:forTransitionContext:continuationLockProvider:]
+ -[SBWallpaperControllerCoordinator acquireWallpaperVisibleAssertionForReason:]
+ -[SBWebClipService _shouldRefuseLaunchOfWebClipIdentifier:]
+ -[SBWindowSceneManager windowSceneForBKSHIDEventDisplay:]
+ -[SBWindowScenePIPManager _lockScreenUIWillOrDidDismiss:]
+ -[SBWindowScenePIPManager _lockScreenUIWillPerformTransition:]
+ -[SBWindowScenePIPManager _setHidesPictureInPictureForCoverSheetPresentation:]
+ -[SBWindowScenePIPManager hidesPictureInPictureForCoverSheetPresentation]
+ -[SBZionUnlockTrigger _defaultRestToOpenDuration]
+ -[SBZionUnlockTrigger _inferFingerOnAtMatchIfNeeded]
+ -[SBZionUnlockTrigger _isMatchingPossible]
+ -[SBZionUnlockTrigger _shouldShowCoachingAfterMatchForRestToOpenDuration:]
+ -[SBZionUnlockTrigger _wasLastBioUnlockTouchID]
+ -[SpringBoard lockOnFoldCoordinator]
+ -[_SBDisplayRegionBlankingLatencyEpisode displayInactive]
+ -[_SBDisplayRegionBlankingLatencyEpisode setDisplayInactive:]
+ -[_SBFullScreenAppFloorSwitcherModifier appSuggestionBannerRegionFrame]
+ -[_SBGridFloorSwitcherModifier appSuggestionBannerRegionFrame]
+ -[_SBHomeScreenFloorSwitcherModifier appSuggestionBannerRegionFrame]
+ GCC_except_table1041
+ GCC_except_table1043
+ GCC_except_table1064
+ GCC_except_table1089
+ GCC_except_table1100
+ GCC_except_table1152
+ GCC_except_table1200
+ GCC_except_table1213
+ GCC_except_table1215
+ GCC_except_table1217
+ GCC_except_table1219
+ GCC_except_table159
+ GCC_except_table165
+ GCC_except_table167
+ GCC_except_table193
+ GCC_except_table199
+ GCC_except_table213
+ GCC_except_table259
+ GCC_except_table283
+ GCC_except_table289
+ GCC_except_table293
+ GCC_except_table316
+ GCC_except_table352
+ GCC_except_table355
+ GCC_except_table358
+ GCC_except_table362
+ GCC_except_table364
+ GCC_except_table367
+ GCC_except_table370
+ GCC_except_table392
+ GCC_except_table394
+ GCC_except_table404
+ GCC_except_table405
+ GCC_except_table413
+ GCC_except_table415
+ GCC_except_table426
+ GCC_except_table437
+ GCC_except_table440
+ GCC_except_table446
+ GCC_except_table449
+ GCC_except_table499
+ GCC_except_table505
+ GCC_except_table508
+ GCC_except_table511
+ GCC_except_table517
+ GCC_except_table520
+ GCC_except_table558
+ GCC_except_table570
+ GCC_except_table590
+ GCC_except_table593
+ GCC_except_table595
+ GCC_except_table606
+ GCC_except_table625
+ GCC_except_table633
+ GCC_except_table635
+ GCC_except_table638
+ GCC_except_table640
+ GCC_except_table642
+ GCC_except_table661
+ GCC_except_table668
+ GCC_except_table682
+ GCC_except_table687
+ GCC_except_table692
+ GCC_except_table704
+ GCC_except_table705
+ GCC_except_table707
+ GCC_except_table720
+ GCC_except_table733
+ GCC_except_table795
+ GCC_except_table832
+ GCC_except_table912
+ GCC_except_table948
+ GCC_except_table955
+ GCC_except_table996
+ _CGColorGetConstantColor
+ _CGImageSourceCreateImageAtIndex
+ _CGImageSourceCreateWithURL
+ _CTLineCreateWithAttributedString
+ _CTLineGetBoundsWithOptions
+ _MCFeatureAllowedWebClipIdentifiers
+ _NSStringFromSBActivityAlertPriority
+ _OBJC_CLASS_$_SBCloseToLockHostComponent
+ _OBJC_CLASS_$_SBCrossfadeChangeSwitcherEventResponse
+ _OBJC_CLASS_$_SBFObliterationController
+ _OBJC_CLASS_$_SBLockOnFoldCoordinator
+ _OBJC_CLASS_$_SBLockOnFoldDomain
+ _OBJC_CLASS_$_SBLockOnFoldFadeRootViewController
+ _OBJC_CLASS_$_SBLockOnFoldFadeTrigger
+ _OBJC_CLASS_$_SBLockOnFoldFadeWindow
+ _OBJC_CLASS_$_SBLockOnFoldSettings
+ _OBJC_CLASS_$_SBPencilPreferredActionProvider
+ _OBJC_CLASS_$_SBRecordingIndicatorRingedLayer
+ _OBJC_CLASS_$_SBSUICloseToLockSceneExtension
+ _OBJC_CLASS_$_SBSecureEraseFailedViewController
+ _OBJC_CLASS_$_SBSystemApertureViewControllerRotationTransitionContext
+ _OBJC_IVAR_$_SBAffordancePresenceController._autoHideSuspensionReasons
+ _OBJC_IVAR_$_SBAnalyticsEventsControllerForIconController._isWidgetContainerAvailable
+ _OBJC_IVAR_$_SBAnalyticsEventsControllerForIconController._proactiveStackInsertionIndex
+ _OBJC_IVAR_$_SBApplicationRestrictionController._allowedWebClipIdentifiers
+ _OBJC_IVAR_$_SBAssistantIslandStageCoordinator._assistantIsIdleAndQuiet
+ _OBJC_IVAR_$_SBAssistantIslandStageCoordinator._lockedIdleTimerCapArmed
+ _OBJC_IVAR_$_SBAssistantIslandStageCoordinator._lockedIdleTimerCapGeneration
+ _OBJC_IVAR_$_SBAssistantIslandStageCoordinator._lockedIdleTimerCapReached
+ _OBJC_IVAR_$_SBAssistantIslandStageCoordinator._wasPresentingResponseInIslandOnLockScreen
+ _OBJC_IVAR_$_SBBLSAssertionWrapper._pendingSettledHandlers
+ _OBJC_IVAR_$_SBBiometricOcclusionMonitor._bioConvenienceSuppressionAssertion
+ _OBJC_IVAR_$_SBButterflyHomeGestureWindowingModifier._hasTouchBeenInCenterRegionSinceEnteringReduceMotionSwitcher
+ _OBJC_IVAR_$_SBButterflyHomeGestureWindowingModifier._lastReduceMotionLayoutChangeTime
+ _OBJC_IVAR_$_SBCloseToLockHostComponent._closeToLockDisabledAssertion
+ _OBJC_IVAR_$_SBCompanionSceneForegroundConstraint._considersUnderLock
+ _OBJC_IVAR_$_SBCoverSheetIconFlyInAnimator._hasReportedNonFiniteCenterPoint
+ _OBJC_IVAR_$_SBCoverSheetSpotlightPresenter._windowScene
+ _OBJC_IVAR_$_SBCrossfadeChangeSwitcherEventResponse._crossfadeDuration
+ _OBJC_IVAR_$_SBCrossfadeChangeSwitcherEventResponse._wrappedResponse
+ _OBJC_IVAR_$_SBDashBoardActivityModalHostableEntity._alertPriority
+ _OBJC_IVAR_$_SBDashBoardBiometricUnlockController._biometricResource
+ _OBJC_IVAR_$_SBDashBoardHostableEntityHostingFluidSwitcherViewController._lastGestureTraveledFarEnoughForDeliberateDismissal
+ _OBJC_IVAR_$_SBDashBoardHostedAppViewController._hostContextProviderInvalidatesScene
+ _OBJC_IVAR_$_SBDashBoardSetupViewController._obliterationController
+ _OBJC_IVAR_$_SBDashBoardSetupViewController._secureEraseFailedViewController
+ _OBJC_IVAR_$_SBDefaultAuthenticationPolicy._didCachePassphrase
+ _OBJC_IVAR_$_SBFluidSwitcherAnimationSettings._reduceMotionDropZoneCrossfadeDuration
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainerHeaderView._accountsForTallScripts
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainerHeaderView._attributedTextToGlyphBounds
+ _OBJC_IVAR_$_SBFluidSwitcherItemContainerHeaderView._minimumLabelGlyphSpacing
+ _OBJC_IVAR_$_SBFluidSwitcherSpaceTitleItem._showsSubtitle
+ _OBJC_IVAR_$_SBFluidSwitcherSpaceTitleItemController._displayItemsAllowingSubtitles
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._systemApertureClonedDisplayVisibilityAssertionsByInvalidationUUID
+ _OBJC_IVAR_$_SBFullScreenToHomeSystemApertureSwitcherModifier._approachHeading
+ _OBJC_IVAR_$_SBHIDEventDispatchController._currentMainRootDispatchingRules
+ _OBJC_IVAR_$_SBHIDEventDispatchController._pencilDoubleTapSystemRule
+ _OBJC_IVAR_$_SBHIDEventDispatchController._pencilPreferredActionProvider
+ _OBJC_IVAR_$_SBHIDEventDispatchController._pencilSqueezeSystemRule
+ _OBJC_IVAR_$_SBHIDEventDispatchController._routeDoubleTapForVIEnabled
+ _OBJC_IVAR_$_SBHIDEventDispatchController._routesPencilDoubleTapToSystem
+ _OBJC_IVAR_$_SBHIDEventDispatchController._routesPencilSqueezeToSystem
+ _OBJC_IVAR_$_SBHomeScreenController._defaultSearchTopEdgeBlockingGestureEdgeRegionSize
+ _OBJC_IVAR_$_SBHomeScreenController._latestTopEdgeTouchBeganInReachabilityVacatedRegion
+ _OBJC_IVAR_$_SBHomeScreenController._pendingExpandedLibraryCategoryIdentifier
+ _OBJC_IVAR_$_SBIconController._restrictionsUpdatePendingAssertion
+ _OBJC_IVAR_$_SBIdleTimerBehavior._suppressesQuickUnwarnExtension
+ _OBJC_IVAR_$_SBLockElementViewProvider._faceInViewForBioConvenienceMatchOperation
+ _OBJC_IVAR_$_SBLockElementViewProvider._pendingBioConvenienceDisplayTimeoutBlock
+ _OBJC_IVAR_$_SBLockElementViewProvider._showingBioConvenienceMatchOperation
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._armed
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._closeToLockDisabledAssertion
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._devicePoseProvider
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._displayContentModeCoordinator
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._fadeTrigger
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._fadeWindows
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._foldWindowScenes
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._hasHingeBaseline
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._liftToWakeSuppressionGeneration
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._liftToWakeSuppressions
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._liveRenderingAssertionProvider
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._lockOnFoldPhase
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._screenSleepCoordinator
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._securityDefaults
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._settings
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._stateDumpHandle
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._statusBarAssertionManager
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._statusBarHideAssertion
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._statusBarHideGeneration
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._statusBarHideLockStarted
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._wallpaperControllerCoordinator
+ _OBJC_IVAR_$_SBLockOnFoldCoordinator._wallpaperVisibleAssertion
+ _OBJC_IVAR_$_SBLockOnFoldFadeTrigger._armed
+ _OBJC_IVAR_$_SBLockOnFoldFadeTrigger._delegate
+ _OBJC_IVAR_$_SBLockOnFoldFadeTrigger._observingPose
+ _OBJC_IVAR_$_SBLockOnFoldFadeTrigger._poseProvider
+ _OBJC_IVAR_$_SBLockOnFoldFadeTrigger._settings
+ _OBJC_IVAR_$_SBLockOnFoldFadeTrigger._timerProvider
+ _OBJC_IVAR_$_SBLockOnFoldFadeTrigger._triggerTimer
+ _OBJC_IVAR_$_SBLockOnFoldFadeTrigger._triggered
+ _OBJC_IVAR_$_SBLockOnFoldFadeTrigger._velocitySatisfied
+ _OBJC_IVAR_$_SBLockOnFoldFadeWindow._visible
+ _OBJC_IVAR_$_SBLockOnFoldSettings._commitWhenContentReachesCover
+ _OBJC_IVAR_$_SBLockOnFoldSettings._contentFadeInDampingRatio
+ _OBJC_IVAR_$_SBLockOnFoldSettings._contentFadeInDelay
+ _OBJC_IVAR_$_SBLockOnFoldSettings._contentFadeInResponse
+ _OBJC_IVAR_$_SBLockOnFoldSettings._contentFadeReversalDampingRatio
+ _OBJC_IVAR_$_SBLockOnFoldSettings._contentFadeReversalResponse
+ _OBJC_IVAR_$_SBLockOnFoldSettings._fadeStartHingeMonitoringAngleThreshold
+ _OBJC_IVAR_$_SBLockOnFoldSettings._fadeStartHingeVelocityThreshold
+ _OBJC_IVAR_$_SBLockOnFoldSettings._fadeWhenCoverSheetPresented
+ _OBJC_IVAR_$_SBLockOnFoldSettings._liftToWakeSuppressionDuration
+ _OBJC_IVAR_$_SBLockOnFoldSettings._startFadeFromHingeVelocity
+ _OBJC_IVAR_$_SBLockOnFoldSettings._visualizeFadeTrigger
+ _OBJC_IVAR_$_SBPencilPreferredActionProvider._preferredActionsDidChangeHandler
+ _OBJC_IVAR_$_SBPrototypeAdvancedActivityElementViewProvider._minimalView
+ _OBJC_IVAR_$_SBReachabilityController._reachabilityAffineTransform
+ _OBJC_IVAR_$_SBReachabilityController._touchRegionTransformRegistration
+ _OBJC_IVAR_$_SBReachabilityGestureRecognizer._horizontalGestureCancelTimer
+ _OBJC_IVAR_$_SBReachabilitySettings._horizontalActivationMaxAngleForVerticalMovement
+ _OBJC_IVAR_$_SBReachabilitySettings._horizontalActivationMinimumSpeed
+ _OBJC_IVAR_$_SBReachabilitySettings._horizontalGestureAllowableEdgeMarginForCompletion
+ _OBJC_IVAR_$_SBReachabilitySettings._horizontalGestureTouchHoldTimeout
+ _OBJC_IVAR_$_SBReachabilitySettings._horizontalInteractiveKeepAlive
+ _OBJC_IVAR_$_SBRecordingIndicatorRingedLayer._dotLayer
+ _OBJC_IVAR_$_SBRecordingIndicatorRingedLayer._ringLayer
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._guaranteedIndicatorContrastWidth
+ _OBJC_IVAR_$_SBRecordingIndicatorView._indicatorColor
+ _OBJC_IVAR_$_SBRecordingIndicatorView._ringed
+ _OBJC_IVAR_$_SBRecordingIndicatorView._secure
+ _OBJC_IVAR_$_SBRecordingIndicatorVisualRepresentation._usesIndicatorRing
+ _OBJC_IVAR_$_SBRecordingIndicatorVisualRepresentation._usesSecureIndicatorLayer
+ _OBJC_IVAR_$_SBRestToOpenSettings._buttonWakeCoachingLeadIn
+ _OBJC_IVAR_$_SBRestToOpenSettings._minimumCoachingVisibleDuration
+ _OBJC_IVAR_$_SBRestToOpenSettings._minimumRemainingDurationForCoaching
+ _OBJC_IVAR_$_SBRestToOpenSettings._pendingMatchRestToOpenDuration
+ _OBJC_IVAR_$_SBRestToOpenSettings._showCoachingDuringPendingMatch
+ _OBJC_IVAR_$_SBRestToOpenSettings._suppressCoachingNearRestToOpenFire
+ _OBJC_IVAR_$_SBRestToOpenSettings._wakeRestToOpenDuration
+ _OBJC_IVAR_$_SBSABlankingRegionLayoutProvider._circleCoversRRRegion
+ _OBJC_IVAR_$_SBSABlankingRegionLayoutProvider._circleReachedFullScale
+ _OBJC_IVAR_$_SBSABlankingRegionLayoutProvider._pendingFullScaleProperty
+ _OBJC_IVAR_$_SBSAOrientationTransitionProvider._renderedElementLayoutTransition
+ _OBJC_IVAR_$_SBSAOrientationTransitionProvider._renderedStatusBarAxis
+ _OBJC_IVAR_$_SBSafeAreaResolverUtility._mirrorsStatusBarSafeArea
+ _OBJC_IVAR_$_SBSecureEraseFailedViewController._delegate
+ _OBJC_IVAR_$_SBSecureEraseFailedViewController._iconView
+ _OBJC_IVAR_$_SBSecureEraseFailedViewController._messageLabel
+ _OBJC_IVAR_$_SBSecureEraseFailedViewController._okButton
+ _OBJC_IVAR_$_SBSwitcherSystemApertureSettings._zoomToJindoTrajectoryRotationCornerBackoff
+ _OBJC_IVAR_$_SBSwitcherSystemApertureSettings._zoomToJindoTrajectoryRotationCornerFactor
+ _OBJC_IVAR_$_SBSwitcherSystemApertureSettings._zoomToJindoTuckInCornerAspectRatio
+ _OBJC_IVAR_$_SBSwitcherSystemApertureSettings._zoomToJindoTuckInCornerThreshold
+ _OBJC_IVAR_$_SBSwitcherSystemApertureSettings._zoomToJindoTuckInCornerTopWidthFactor
+ _OBJC_IVAR_$_SBSystemApertureContainerView._activeContentRotationTransform
+ _OBJC_IVAR_$_SBSystemApertureContainerView._elementOrientationAuthority
+ _OBJC_IVAR_$_SBSystemApertureContainerView._previousContentTransform
+ _OBJC_IVAR_$_SBSystemApertureSettings._nonCenterPillShakeDisplacement
+ _OBJC_IVAR_$_SBSystemApertureSettings._nonCenterPillShakeSensorExpansion
+ _OBJC_IVAR_$_SBSystemApertureSettings._nonCenterPillShakeSensorOffset
+ _OBJC_IVAR_$_SBSystemApertureViewController._invalidated
+ _OBJC_IVAR_$_SBSystemApertureViewControllerRotationTransitionContext._targetTransform
+ _OBJC_IVAR_$_SBSystemGestureManager._systemKeyCommandOverlayEventDeferringRule
+ _OBJC_IVAR_$_SBTopAffordanceViewController._windowControlsHoverGestureRecognizer
+ _OBJC_IVAR_$_SBTouchRegionManager._cachedTouchRegionBuffer
+ _OBJC_IVAR_$_SBTouchRegionManager._queue_exclusiveKeyboardFramesByDisplay
+ _OBJC_IVAR_$_SBTouchRegionManager._queue_reachabilityRegistrationIdentifiersByDisplay
+ _OBJC_IVAR_$_SBTouchRegionManager._queue_reachabilityTransformsByDisplay
+ _OBJC_IVAR_$_SBTraitsOrientationDefaultResolutionPolicySpecifier._lastKeyboardFocusedParticipantUniqueIdentifier
+ _OBJC_IVAR_$_SBWallpaperControllerCoordinator._wallpaperVisibleAssertions
+ _OBJC_IVAR_$_SBWindowScenePIPManager._hidesPictureInPictureForCoverSheetPresentation
+ _OBJC_IVAR_$_SBZionUnlockTrigger._coachingSuppressed
+ _OBJC_IVAR_$_SBZionUnlockTrigger._fingerEventSinceWake
+ _OBJC_IVAR_$_SBZionUnlockTrigger._fingerOnInferred
+ _OBJC_IVAR_$_SBZionUnlockTrigger._fingerOnTime
+ _OBJC_IVAR_$_SBZionUnlockTrigger._matchedSinceFingerOn
+ _OBJC_IVAR_$_SBZionUnlockTrigger._pendingMatchCoachingActive
+ _OBJC_IVAR_$_SBZionUnlockTrigger._restToOpenElapsedAwaitingMatch
+ _OBJC_IVAR_$_SBZionUnlockTrigger._wakeTime
+ _OBJC_IVAR_$_SpringBoard._lockOnFoldCoordinator
+ _OBJC_IVAR_$__SBDisplayRegionBlankingLatencyEpisode._displayInactive
+ _OBJC_METACLASS_$_SBCloseToLockHostComponent
+ _OBJC_METACLASS_$_SBCrossfadeChangeSwitcherEventResponse
+ _OBJC_METACLASS_$_SBLockOnFoldCoordinator
+ _OBJC_METACLASS_$_SBLockOnFoldDomain
+ _OBJC_METACLASS_$_SBLockOnFoldFadeRootViewController
+ _OBJC_METACLASS_$_SBLockOnFoldFadeTrigger
+ _OBJC_METACLASS_$_SBLockOnFoldFadeWindow
+ _OBJC_METACLASS_$_SBLockOnFoldSettings
+ _OBJC_METACLASS_$_SBPencilPreferredActionProvider
+ _OBJC_METACLASS_$_SBRecordingIndicatorRingedLayer
+ _OBJC_METACLASS_$_SBSecureEraseFailedViewController
+ _OBJC_METACLASS_$_SBSystemApertureViewControllerRotationTransitionContext
+ _OBJC_METACLASS_$__UIViewControllerTransitionContext
+ _SBApplicationClassicAppZoomedInDidChangeNotification
+ _SBDisplayLayoutTransitionReasonFlush
+ _SBLogLockOnFold
+ _SBLogLockOnFold.__logObj
+ _SBLogLockOnFold.onceToken
+ _SBPencilPreferredActionProviderKVOContext
+ _SBReachabilityGestureEdgeMarginForActivationOnEdge
+ _SBReachabilityGestureShouldActivateFromEdgeCheckingVelocityAngle
+ _SBScreenRegionIsSplit
+ _SBSecureEraseFailedLocalizedString
+ _SBTraitsParticipantRoleLockOnFoldFade
+ _SBUIBiometricEventSuppressesFailureFeedback
+ _UTTypeHEIC
+ _UTTypeJPEG
+ _UTTypePNG
+ __NSStringFromUIRectEdge
+ __OBJC_$_CLASS_METHODS_SBChainableModifier(RuntimeProviding|SwitcherModifier|WindowingModifier)
+ __OBJC_$_CLASS_METHODS_SBLockOnFoldDomain
+ __OBJC_$_CLASS_METHODS_SBLockOnFoldSettings
+ __OBJC_$_CLASS_METHODS_SBSceneManager
+ __OBJC_$_CLASS_METHODS_SBSystemApertureViewControllerRotationTransitionContext
+ __OBJC_$_INSTANCE_METHODS_FBScene(SBVisibilitySceneExtension_ForSceneManager|SafeAreaResolverExtensionDelegate|SBSUIHomeScreenIconStyle|InputUISceneController|LocalSynchronous|SceneBarPositionResolverExtension|SBSceneRegionHost|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBScreenBrightnessHost|SBProductivityGestureDestination|SBSceneAccessoryContainer|SBSceneAccessoryContainer_Internal|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
+ __OBJC_$_INSTANCE_METHODS_SBChainableModifier(RuntimeProviding|SwitcherModifier|WindowingModifier)
+ __OBJC_$_INSTANCE_METHODS_SBChainableModifierEvent(SBSwitcherModifierEvent|SBWindowingModifierActivity)
+ __OBJC_$_INSTANCE_METHODS_SBChainableModifierEventResponse(SBSwitcherModifierEventResponse|SBWindowingModifierResponse)
+ __OBJC_$_INSTANCE_METHODS_SBCloseToLockHostComponent
+ __OBJC_$_INSTANCE_METHODS_SBCrossfadeChangeSwitcherEventResponse
+ __OBJC_$_INSTANCE_METHODS_SBLockOnFoldCoordinator
+ __OBJC_$_INSTANCE_METHODS_SBLockOnFoldFadeRootViewController
+ __OBJC_$_INSTANCE_METHODS_SBLockOnFoldFadeTrigger
+ __OBJC_$_INSTANCE_METHODS_SBLockOnFoldFadeWindow
+ __OBJC_$_INSTANCE_METHODS_SBLockOnFoldSettings
+ __OBJC_$_INSTANCE_METHODS_SBPencilPreferredActionProvider
+ __OBJC_$_INSTANCE_METHODS_SBRecordingIndicatorRingedLayer
+ __OBJC_$_INSTANCE_METHODS_SBSecureEraseFailedViewController
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherModifier(SharedModifierUtilities|WindowingModifier)
+ __OBJC_$_INSTANCE_METHODS_SBSystemApertureViewControllerRotationTransitionContext
+ __OBJC_$_INSTANCE_METHODS_SBWindowingModifierActivity(TransitionEvent|GestureEvent|StripChangedModifierActivity)
+ __OBJC_$_INSTANCE_VARIABLES_SBCloseToLockHostComponent
+ __OBJC_$_INSTANCE_VARIABLES_SBCompanionSceneForegroundConstraint
+ __OBJC_$_INSTANCE_VARIABLES_SBCrossfadeChangeSwitcherEventResponse
+ __OBJC_$_INSTANCE_VARIABLES_SBLockOnFoldCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_SBLockOnFoldFadeTrigger
+ __OBJC_$_INSTANCE_VARIABLES_SBLockOnFoldFadeWindow
+ __OBJC_$_INSTANCE_VARIABLES_SBLockOnFoldSettings
+ __OBJC_$_INSTANCE_VARIABLES_SBPencilPreferredActionProvider
+ __OBJC_$_INSTANCE_VARIABLES_SBRecordingIndicatorRingedLayer
+ __OBJC_$_INSTANCE_VARIABLES_SBSafeAreaResolverUtility
+ __OBJC_$_INSTANCE_VARIABLES_SBSecureEraseFailedViewController
+ __OBJC_$_INSTANCE_VARIABLES_SBSystemApertureViewControllerRotationTransitionContext
+ __OBJC_$_PROP_LIST_SBCrossfadeChangeSwitcherEventResponse
+ __OBJC_$_PROP_LIST_SBDashBoardHostableEntityDismissGestureCustomizing
+ __OBJC_$_PROP_LIST_SBLockOnFoldCoordinator
+ __OBJC_$_PROP_LIST_SBLockOnFoldFadeTrigger
+ __OBJC_$_PROP_LIST_SBLockOnFoldFadeWindow
+ __OBJC_$_PROP_LIST_SBLockOnFoldSettings
+ __OBJC_$_PROP_LIST_SBPencilPreferredActionProvider
+ __OBJC_$_PROP_LIST_SBPencilPreferredActionProviding
+ __OBJC_$_PROP_LIST_SBRecordingIndicatorRingedLayer
+ __OBJC_$_PROP_LIST_SBSafeAreaResolverUtility
+ __OBJC_$_PROP_LIST_SBSecureEraseFailedViewController
+ __OBJC_$_PROP_LIST_SBSystemApertureElementOrientationObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBDashBoardHostableEntityDismissGestureCustomizing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBSafeAreaResolverExtensionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBSystemApertureElementOrientationObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBLockOnFoldFadeTriggerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBPencilPreferredActionProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSecureEraseFailedViewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSystemApertureElementOrientationAuthority
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSystemApertureElementOrientationObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBDashBoardHostableEntityDismissGestureCustomizing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBLockOnFoldFadeTriggerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBPencilPreferredActionProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSecureEraseFailedViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSystemApertureElementOrientationAuthority
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSystemApertureElementOrientationObserving
+ __OBJC_$_PROTOCOL_REFS_SBDashBoardHostableEntityDismissGestureCustomizing
+ __OBJC_$_PROTOCOL_REFS_SBLockOnFoldFadeTriggerDelegate
+ __OBJC_$_PROTOCOL_REFS_SBPencilPreferredActionProviding
+ __OBJC_$_PROTOCOL_REFS_SBSecureEraseFailedViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_SBSystemApertureElementOrientationAuthority
+ __OBJC_$_PROTOCOL_REFS_SBSystemApertureElementOrientationObserving
+ __OBJC_CLASS_PROTOCOLS_$_FBScene(SBVisibilitySceneExtension_ForSceneManager|SafeAreaResolverExtensionDelegate|SBSUIHomeScreenIconStyle|InputUISceneController|LocalSynchronous|SceneBarPositionResolverExtension|SBSceneRegionHost|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBScreenBrightnessHost|SBProductivityGestureDestination|SBSceneAccessoryContainer|SBSceneAccessoryContainer_Internal|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
+ __OBJC_CLASS_PROTOCOLS_$_SBLockOnFoldCoordinator
+ __OBJC_CLASS_PROTOCOLS_$_SBLockOnFoldFadeTrigger
+ __OBJC_CLASS_PROTOCOLS_$_SBPencilPreferredActionProvider
+ __OBJC_CLASS_PROTOCOLS_$_SBRecordingIndicatorRingedLayer
+ __OBJC_CLASS_RO_$_SBCloseToLockHostComponent
+ __OBJC_CLASS_RO_$_SBCrossfadeChangeSwitcherEventResponse
+ __OBJC_CLASS_RO_$_SBLockOnFoldCoordinator
+ __OBJC_CLASS_RO_$_SBLockOnFoldDomain
+ __OBJC_CLASS_RO_$_SBLockOnFoldFadeRootViewController
+ __OBJC_CLASS_RO_$_SBLockOnFoldFadeTrigger
+ __OBJC_CLASS_RO_$_SBLockOnFoldFadeWindow
+ __OBJC_CLASS_RO_$_SBLockOnFoldSettings
+ __OBJC_CLASS_RO_$_SBPencilPreferredActionProvider
+ __OBJC_CLASS_RO_$_SBRecordingIndicatorRingedLayer
+ __OBJC_CLASS_RO_$_SBSecureEraseFailedViewController
+ __OBJC_CLASS_RO_$_SBSystemApertureViewControllerRotationTransitionContext
+ __OBJC_LABEL_PROTOCOL_$_SBDashBoardHostableEntityDismissGestureCustomizing
+ __OBJC_LABEL_PROTOCOL_$_SBLockOnFoldFadeTriggerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBPencilPreferredActionProviding
+ __OBJC_LABEL_PROTOCOL_$_SBSecureEraseFailedViewControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBSystemApertureElementOrientationAuthority
+ __OBJC_LABEL_PROTOCOL_$_SBSystemApertureElementOrientationObserving
+ __OBJC_METACLASS_RO_$_SBCloseToLockHostComponent
+ __OBJC_METACLASS_RO_$_SBCrossfadeChangeSwitcherEventResponse
+ __OBJC_METACLASS_RO_$_SBLockOnFoldCoordinator
+ __OBJC_METACLASS_RO_$_SBLockOnFoldDomain
+ __OBJC_METACLASS_RO_$_SBLockOnFoldFadeRootViewController
+ __OBJC_METACLASS_RO_$_SBLockOnFoldFadeTrigger
+ __OBJC_METACLASS_RO_$_SBLockOnFoldFadeWindow
+ __OBJC_METACLASS_RO_$_SBLockOnFoldSettings
+ __OBJC_METACLASS_RO_$_SBPencilPreferredActionProvider
+ __OBJC_METACLASS_RO_$_SBRecordingIndicatorRingedLayer
+ __OBJC_METACLASS_RO_$_SBSecureEraseFailedViewController
+ __OBJC_METACLASS_RO_$_SBSystemApertureViewControllerRotationTransitionContext
+ __OBJC_PROTOCOL_$_SBDashBoardHostableEntityDismissGestureCustomizing
+ __OBJC_PROTOCOL_$_SBLockOnFoldFadeTriggerDelegate
+ __OBJC_PROTOCOL_$_SBPencilPreferredActionProviding
+ __OBJC_PROTOCOL_$_SBSecureEraseFailedViewControllerDelegate
+ __OBJC_PROTOCOL_$_SBSystemApertureElementOrientationAuthority
+ __OBJC_PROTOCOL_$_SBSystemApertureElementOrientationObserving
+ __SBSAElementHangsOffCornerCircleSensor
+ ___102-[SBTestAutomationService systemServiceServer:client:homeScreenGridSizeForPageAtIndex:withCompletion:]_block_invoke
+ ___108-[SBTestAutomationService systemServiceServer:client:setHomeScreenCurrentPageIndex:animated:withCompletion:]_block_invoke
+ ___110-[SBSAOrientationTransitionProvider _preferencesByAvoidingSensorOfInterfaceOrientation:inPreferences:context:]_block_invoke
+ ___113-[SBTestAutomationService systemServiceServer:client:openHomeScreenFolderWithIdentifier:animated:withCompletion:]_block_invoke
+ ___113-[SBTestAutomationService systemServiceServer:client:openHomeScreenFolderWithIdentifier:animated:withCompletion:]_block_invoke_2
+ ___113-[SBTestAutomationService systemServiceServer:client:openHomeScreenFolderWithIdentifier:animated:withCompletion:]_block_invoke_3
+ ___113-[SBTestAutomationService systemServiceServer:client:openHomeScreenFolderWithIdentifier:animated:withCompletion:]_block_invoke_4
+ ___114-[SBHIDEventDispatchController _initWithDeliveryManager:pencilPreferredActionProvider:routeDoubleTapForVIEnabled:]_block_invoke
+ ___120-[SBWallpaperControllerCoordinator _transferWallpaperToPrimaryController:forTransitionContext:continuationLockProvider:]_block_invoke
+ ___120-[SBWallpaperControllerCoordinator _transferWallpaperToPrimaryController:forTransitionContext:continuationLockProvider:]_block_invoke_2
+ ___164-[SBLockOnFoldCoordinator initWithSettings:displayContentModeCoordinator:devicePoseProvider:screenSleepCoordinator:securityDefaults:liveRenderingAssertionProvider:]_block_invoke
+ ___194-[SBSafeAreaResolverUtility safeAreaCornerInsetResolverWithBucketedAvoidanceDetentsForScreenType:windowScene:suppressesStatusBarSafeArea:suppressVerticalAxisWhereDisfavored:supportsVerticalBar:]_block_invoke
+ ___29-[SBIconController setModel:]_block_invoke
+ ___29-[SBIconController setModel:]_block_invoke_2
+ ___31-[SBZionUnlockTrigger fingerOn]_block_invoke_2
+ ___40-[SBLockOnFoldCoordinator _sleepAndLock]_block_invoke
+ ___44-[SBLockOnFoldFadeTrigger initWithSettings:]_block_invoke
+ ___44-[SBLockOnFoldFadeTrigger initWithSettings:]_block_invoke_2
+ ___46-[SBLockOnFoldCoordinator _suppressLiftToWake]_block_invoke
+ ___48-[SBCompanionSceneForegroundConstraint isEqual:]_block_invoke
+ ___49-[SBLockOnFoldFadeTrigger _noteVelocitySatisfied]_block_invoke
+ ___51-[SBContinuitySessionSystemEventMonitor _lockState]_block_invoke
+ ___53-[SBLockOnFoldCoordinator appendDescriptionToStream:]_block_invoke
+ ___53-[SBLockOnFoldCoordinator appendDescriptionToStream:]_block_invoke_2
+ ___53-[SBLockOnFoldCoordinator appendDescriptionToStream:]_block_invoke_3
+ ___56-[SBButterflyHomeGestureWindowingModifier frameForItem:]_block_invoke_3
+ ___57-[SBTestAutomationService _rootFolderIconWithIdentifier:]_block_invoke
+ ___57-[SBWindowSceneManager windowSceneForBKSHIDEventDisplay:]_block_invoke
+ ___58-[SBButterflyHomeGestureWindowingModifier homeScreenAlpha]_block_invoke
+ ___59-[SBDashBoardSetupViewController _checkIfSecureEraseFailed]_block_invoke
+ ___59-[SBDashBoardSetupViewController _checkIfSecureEraseFailed]_block_invoke_2
+ ___59-[SBLockOnFoldCoordinator _noteLockStartedForStatusBarHide]_block_invoke
+ ___59-[SBRoutingSwitcherModifier appSuggestionBannerRegionFrame]_block_invoke
+ ___60-[SBButterflyHomeGestureWindowingModifier gestureDidUpdate:]_block_invoke_2
+ ___60-[SBSAOrientationTransitionProvider preferencesFromContext:]_block_invoke_2
+ ___61-[SBButterflyHomeGestureWindowingModifier titleStyleForItem:]_block_invoke
+ ___62-[SBLockScreenCoordinator _publishUILockStateToOtherProcesses]_block_invoke
+ ___63-[SBButterflyHomeGestureWindowingModifier dimmingAlphaForItem:]_block_invoke
+ ___64-[SBBacklightController performAfterAssertionTransitionsSettle:]_block_invoke
+ ___65-[SBButterflyHomeGestureWindowingModifier homeScreenDimmingAlpha]_block_invoke
+ ___65-[SBLockElementViewProvider _bioConvenienceMatchOperationStarted]_block_invoke
+ ___65-[SBLockOnFoldCoordinator _transitionContextMovesContentToCover:]_block_invoke
+ ___66-[SBHomeScreenController _expandLibraryPodWithCategoryIdentifier:]_block_invoke
+ ___67-[SBCoverSheetPresentationManager _queue_relinquishSystemAnimation]_block_invoke
+ ___68-[SBContinuousFadeEffectViewController _updateDimForCurrentProgress]_block_invoke
+ ___68-[SBLockOnFoldCoordinator _transitionContextEndsWithContentOnCover:]_block_invoke
+ ___69-[SBAppExposeToAppWindowingModifier adjustedAppLayoutsForAppLayouts:]_block_invoke_3
+ ___69-[SBAppExposeToAppWindowingModifier adjustedAppLayoutsForAppLayouts:]_block_invoke_4
+ ___69-[SBDashBoardPearlUnlockBehavior handleBiometricEvent:forDeviceKind:]_block_invoke
+ ___69-[SBDashBoardSetupViewController fadeCursiveHelloToVisible:duration:]_block_invoke
+ ___69-[SBDashBoardSetupViewController fadeCursiveHelloToVisible:duration:]_block_invoke_2
+ ___70+[SBIconController proactiveStackInsertionIndexForScreenType:inIcons:]_block_invoke
+ ___70+[SBIconController proactiveStackInsertionIndexForScreenType:inIcons:]_block_invoke_2
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke_10
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke_11
+ ___70-[SBFluidSwitcherViewController _updateVisibleSplitViewHandleNubViews]_block_invoke_12
+ ___70-[SBLockOnFoldCoordinator _setFadeWindowVisible:animated:windowScene:]_block_invoke
+ ___70-[SBRoutingSwitcherModifier displayItemsAllowingSubtitlesInAppLayout:]_block_invoke
+ ___71+[SBCompanionSceneForegroundConstraint foregroundOrUnderLockConstraint]_block_invoke
+ ___71-[SBTouchRegionManager setExclusiveKeyboardFrame:forDisplayIdentifier:]_block_invoke
+ ___72-[SBAssistantIslandStageCoordinator _updateLockedIdleTimerCapForReason:]_block_invoke
+ ___73-[SBActivityModalPresentationController presentModalForAlert:completion:]_block_invoke
+ ___73-[SBButterflyHomeGestureWindowingModifier homeScreenBackdropBlurProgress]_block_invoke
+ ___73-[SBFluidSwitcherViewController _performModifierCrossfadeChangeResponse:]_block_invoke
+ ___73-[SBFluidSwitcherViewController _performModifierCrossfadeChangeResponse:]_block_invoke_2
+ ___74-[SBRecentDisplayItemsController _removeDisplayItemsForRestrictedWebClips]_block_invoke
+ ___75-[SBApplicationRestrictionController _destroyRestrictedWebClipSceneHandles]_block_invoke
+ ___75-[SBApplicationRestrictionController _destroyRestrictedWebClipSceneHandles]_block_invoke_2
+ ___75-[SBTestAutomationService systemServiceServer:client:setHomeScreenEditing:]_block_invoke
+ ___75-[SBTouchRegionManager registerReachabilityTransform:forDisplayIdentifier:]_block_invoke
+ ___76-[SBScreenSleepController _sleepAndLockUIFromSource:lockOptions:completion:]_block_invoke
+ ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke_3
+ ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke_4
+ ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke_5
+ ___78-[SBSystemServiceServer _handleTestAutomationGetHomeScreenEditing:fromClient:]_block_invoke
+ ___78-[SBSystemServiceServer _handleTestAutomationGetHomeScreenEditing:fromClient:]_block_invoke_2
+ ___78-[SBSystemServiceServer _handleTestAutomationOpenHomeScreenFolder:fromClient:]_block_invoke
+ ___78-[SBSystemServiceServer _handleTestAutomationOpenHomeScreenFolder:fromClient:]_block_invoke_2
+ ___78-[SBSystemServiceServer _handleTestAutomationSetHomeScreenEditing:fromClient:]_block_invoke
+ ___78-[SBWindowScenePIPManager _setHidesPictureInPictureForCoverSheetPresentation:]_block_invoke
+ ___79-[SBContinuousFoldSnapshotCoordinator liftCloakWithoutAnimationForWindowScene:]_block_invoke
+ ___79-[SBReachabilityController _updateReachabilityWindowForOffset:mode:completion:]_block_invoke_6
+ ___79-[SBSystemServiceServer _handleTestAutomationGetHomeScreenGridSize:fromClient:]_block_invoke
+ ___79-[SBSystemServiceServer _handleTestAutomationGetHomeScreenGridSize:fromClient:]_block_invoke_2
+ ___80-[SBTestAutomationService systemServiceServer:client:resetToHomeScreenAnimated:]_block_invoke_7
+ ___81-[SBTouchRegionManager _invalidateReachabilityRegistration:forDisplayIdentifier:]_block_invoke
+ ___82-[SBFluidSwitcherViewController _performCrossfadeIfNeededWithDuration:completion:]_block_invoke
+ ___82-[SBFluidSwitcherViewController _performCrossfadeIfNeededWithDuration:completion:]_block_invoke_2
+ ___82-[SBPencilPreferredActionProvider observeValueForKeyPath:ofObject:change:context:]_block_invoke
+ ___83-[SBAnalyticsEventsControllerForIconController _analyticsLoggingForTodayViewLayout]_block_invoke
+ ___83-[SBLockOnFoldCoordinator statusBarAssertionManager:addStatusBarSettingsAssertion:]_block_invoke
+ ___84-[SBTraitsOrientationDefaultResolutionPolicySpecifier _isParticipantAcquired:among:]_block_invoke
+ ___86-[SBSystemApertureContainerView elementOrientationDidChangeWithTransitionCoordinator:]_block_invoke
+ ___86-[SBSystemApertureContainerView elementOrientationDidChangeWithTransitionCoordinator:]_block_invoke_2
+ ___87-[SBDashBoardSetupViewController secureEraseFailedViewControllerDidAcknowledgeFailure:]_block_invoke
+ ___87-[SBSAAcceptanceBounceBehaviorProvider _excursionDescriptionWithBounds:center:context:]_block_invoke
+ ___87-[SBSAAcceptanceBounceBehaviorProvider _preferencesBySuppressingKeyLinesInPreferences:]_block_invoke
+ ___87-[SBSAAcceptanceBounceBehaviorProvider _preferencesBySuppressingKeyLinesInPreferences:]_block_invoke_2
+ ___87-[SBSystemServiceServer _handleTestAutomationSetHomeScreenCurrentPageIndex:fromClient:]_block_invoke
+ ___87-[SBSystemServiceServer _handleTestAutomationSetHomeScreenCurrentPageIndex:fromClient:]_block_invoke_2
+ ___90-[SBBacklightController displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_4
+ ___90-[SBBacklightController displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_5
+ ___90-[SBLockOnFoldCoordinator _animateFadeWindow:toVisible:dampingRatio:response:windowScene:]_block_invoke
+ ___90-[SBLockOnFoldCoordinator _animateFadeWindow:toVisible:dampingRatio:response:windowScene:]_block_invoke_2
+ ___91-[SBTestAutomationService systemServiceServer:client:getIsHomeScreenEditingWithCompletion:]_block_invoke
+ ___92-[SBLockOnFoldCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke
+ ___92-[SBLockOnFoldCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_2
+ ___92-[SBLockOnFoldCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_3
+ ___94-[SBTestAutomationService _closeAllFoldersWithIconManager:animated:remainingDepth:completion:]_block_invoke
+ ___94-[SBWallpaperControllerCoordinator _notifyWhenWallpaperReadyToTransferWithTimeout:completion:]_block_invoke
+ ___94-[SBWallpaperControllerCoordinator _notifyWhenWallpaperReadyToTransferWithTimeout:completion:]_block_invoke_2
+ ___94-[SBWallpaperControllerCoordinator _notifyWhenWallpaperReadyToTransferWithTimeout:completion:]_block_invoke_3
+ ___95-[SBButterflyDefaultImplementationsWindowingModifier displayItemsAllowingSubtitlesInAppLayout:]_block_invoke
+ ___95-[SBLockScreenBiometricAuthenticationCoordinator biometricResource:observeEvent:forDeviceKind:]_block_invoke
+ ___97-[SBSystemApertureViewController(Private) _updateElementOrientationTo:withTransitionCoordinator:]_block_invoke
+ ___97-[SBSystemApertureViewController(Private) _updateElementOrientationTo:withTransitionCoordinator:]_block_invoke_2
+ ___98-[SBWallpaperControllerCoordinator _notifyWhenWallpaperAcknowledgesDisplayTransferWithCompletion:]_block_invoke
+ ___98-[SBWallpaperControllerCoordinator _notifyWhenWallpaperAcknowledgesDisplayTransferWithCompletion:]_block_invoke_2
+ ___99-[SBAnalyticsEventsControllerForIconController _todayViewLayoutStateForTodayList:defaultTodayList:]_block_invoke
+ ___99-[SBAnalyticsEventsControllerForIconController _todayViewLayoutStateForTodayList:defaultTodayList:]_block_invoke_2
+ ___99-[SBAnalyticsEventsControllerForIconController _todayViewLayoutStateForTodayList:defaultTodayList:]_block_invoke_3
+ ___SBEffectiveAllowedWebClipIdentifiers_block_invoke
+ ___SBLogLockOnFold_block_invoke
+ ___block_descriptor_120_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_248_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_32_e18_"NSString"16?08l
+ ___block_descriptor_32_e36_"<BSInvalidatable>"24?0d8?<v?>16l
+ ___block_descriptor_33_e79_{_UICornerInsets={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}}24?0{CGSize=dd}8l
+ ___block_descriptor_40_e8_32s_e13_v24?0{?=qq}8ls32l8
+ ___block_descriptor_40_e8_32s_e23_B32?0"SBIcon"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e23_v16?0"SBWindowScene"8ls32l8
+ ___block_descriptor_40_e8_32s_e33_B24?0"SBIcon"8"NSDictionary"16ls32l8
+ ___block_descriptor_40_e8_32w_e17_Q16?0"NSArray"8lw32l8
+ ___block_descriptor_40_e8_32w_e18_B16?0"NSString"8lw32l8
+ ___block_descriptor_40_e8_32w_e22_v16?0"NSDictionary"8lw32l8
+ ___block_descriptor_41_e8_32w_e96_v24?0"SBFDisplayContentModeTransitionContext"8"SBFDisplayContentModeTransitionLockProvider"16lw32l8
+ ___block_descriptor_48_e8_32r40r_e27_v24?0"SBWindowScene"8^B16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e29_v32?0"SBFolderIcon"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e45_B16?0"SBSwitcherSplitViewHandleNubElement"8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e11_v16?0B8B12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8w40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e12_v24?0Q8^B16ls32l8s40l8r48l8r56l8
+ ___block_descriptor_65_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e8_v12?0B8ls56l8s32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e27_v24?0"SBWindowScene"8^B16ls32l8r48l8s40l8r56l8r64l8
+ ___block_descriptor_73_e8_32s40s48s56r_e8_v16?08ls32l8r56l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56s64s_e42_v16?0"SBMainWorkspaceTransitionRequest"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_73_e8_32s40s48s_e8_v16?08ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8
+ __publishUILockStateToOtherProcesses.onceToken
+ __publishUILockStateToOtherProcesses.publishQueue
+ __publishUILockStateToOtherProcesses.token
+ _foregroundOrUnderLockConstraint.foregroundOrUnderLockConstraint
+ _foregroundOrUnderLockConstraint.onceToken
+ _kCGColorBlack
+ _kCGImageSourceAllowableTypes
+ _kSBSTestAutomationServiceMessageKeyHomeScreenErrorDescription
+ _kSBSTestAutomationServiceMessageKeyHomeScreenFolderIdentifier
+ _kSBSTestAutomationServiceMessageKeyHomeScreenGridColumns
+ _kSBSTestAutomationServiceMessageKeyHomeScreenGridRows
+ _kSBSTestAutomationServiceMessageKeyHomeScreenPageIndex
+ _kSBSTestAutomationServiceMessageKeySuccess
+ _realpath$DARWIN_EXTSN
+ _remainder
- +[SBHomeScreenController _shouldDismissSpotlightForTransitionSource:previousHomeScreenRegion:]
- +[SBSceneBarPositionResolverUtility barSizeClassResolverForScreenType:isPhone:]
- +[SBSystemApertureBackgroundBlurView haloExtent]
- -[SBActivityModalPresentationController presentModalForActivityItem:completion:]
- -[SBAnalyticsEventsControllerForIconController initWithIconModel:]
- -[SBBiometricEventLogger biometricResource:observeEvent:]
- -[SBBiometricMonitorPearlDataSource biometricResource:observeEvent:]
- -[SBCameraOverlayUISceneController _activeWindowScene]
- -[SBContinuousFadeEffectViewController _applyAngleProgress:]
- -[SBContinuousFadeEffectViewController _updateDimForCurrentAngleProgress]
- -[SBControlCenterController didDismissControlsGalleryForControlCenterViewController:]
- -[SBControlCenterController handleReachabilityYOffsetDidChange]
- -[SBControlCenterController reachabilityPointOffsetForControlCenterViewController:]
- -[SBControlCenterController willPresentControlsGalleryForControlCenterViewController:]
- -[SBCoverSheetBiometricResourceObserver biometricResource:observeEvent:]
- -[SBCoverSheetGrabberViewController _timeLabelFrameInWindow:statusBar:]
- -[SBDashBoardBiometricUnlockController handleBiometricEvent:]
- -[SBDashBoardLockScreenEnvironment handleBiometricEvent:]
- -[SBDashBoardMesaUnlockBehavior handleBiometricEvent:]
- -[SBDashBoardPearlUnlockBehavior handleBiometricEvent:]
- -[SBDashBoardSetupViewController initWithCoverSheetViewController:telephonyManager:]
- -[SBDefaultAuthenticationPolicy _secureBackupHelper]
- -[SBDefaultAuthenticationPolicy _setSecureBackupHelper:]
- -[SBDeviceContinuousFoldInteractionSettings isOrientationLockSettleEnabled]
- -[SBDeviceContinuousFoldInteractionSettings orientationLockSettleDuration]
- -[SBDeviceContinuousFoldInteractionSettings setOrientationLockSettleDuration:]
- -[SBDeviceContinuousFoldInteractionSettings setOrientationLockSettleEnabled:]
- -[SBFloatingDockController delegate]
- -[SBFloatingDockController setDelegate:]
- -[SBFluidSwitcherItemContainerHeaderView _labelLayoutMetricsForItem:]
- -[SBFluidSwitcherViewController _performCrossfadeIfNeededWithCompletion:]
- -[SBHomeScreenController _dismissSpotlightIfLaunchingFromItWithTransitionSource:previousHomeScreenRegion:]
- -[SBHomeScreenController minimumHomeScreenScaleForFloatingDockController:]
- -[SBLockElementViewProvider biometricResource:observeEvent:]
- -[SBLockScreenBiometricAuthenticationCoordinator biometricResource:observeEvent:]
- -[SBLockScreenCoordinator _sendUILockStateChangedNotificationIfNeeded]
- -[SBLockScreenCoordinator handleBiometricEvent:]
- -[SBLockScreenSessionAnalyticsTracker biometricResource:observeEvent:]
- -[SBLockScreenViewControllerBase handleBiometricEvent:]
- -[SBPearlInterlockObserver biometricResource:observeEvent:]
- -[SBReachabilityGestureRecognizer _shouldBeginBeforeTouchUpAtLocation:translation:]
- -[SBSAAcceptanceBounceBehaviorProvider _excursionDescriptionWithBounds:center:]
- -[SBSAAcceptanceBounceBehaviorProvider _excursionRotation]
- -[SBSAAcceptanceBounceBehaviorProvider _isVerticalExpansion]
- -[SBSABackgroundBlurDescription _setBlurElementCornerRadius:]
- -[SBSABackgroundBlurDescription _setBlurElementFrame:]
- -[SBSABackgroundBlurDescription blurElementCornerRadius]
- -[SBSABackgroundBlurDescription blurElementFrame]
- -[SBSABackgroundBlurDescription copyBySettingBlurElementCornerRadius:]
- -[SBSABackgroundBlurDescription copyBySettingBlurElementFrame:]
- -[SBSABackgroundBlurDescriptionMutator blurElementCornerRadius]
- -[SBSABackgroundBlurDescriptionMutator blurElementFrame]
- -[SBSABackgroundBlurDescriptionMutator setBlurElementCornerRadius:]
- -[SBSABackgroundBlurDescriptionMutator setBlurElementFrame:]
- -[SBSAShadowPreferencesProvider _shadowStyleForContainerDescription:elementContext:useHeavyShadowForTransition:isFirstContainer:suppressExpandedShadow:]
- -[SBSceneOrientationFollowingWindowRootViewController _edgeInsetsForChildViewController:insetsAreAbsolute:]
- -[SBSceneRegionsUpdater _statusBarOcclusionFrame]
- -[SBSystemApertureBackgroundBlurView .cxx_destruct]
- -[SBSystemApertureBackgroundBlurView _configureSDFHierarchy]
- -[SBSystemApertureBackgroundBlurView _newGradientEffect]
- -[SBSystemApertureBackgroundBlurView backdropLayer]
- -[SBSystemApertureBackgroundBlurView elementCornerRadius]
- -[SBSystemApertureBackgroundBlurView elementFrame]
- -[SBSystemApertureBackgroundBlurView setElementCornerRadius:]
- -[SBSystemApertureBackgroundBlurView setElementFrame:]
- -[SBSystemApertureController animateTransitionAcceptanceBounceWithVelocityVector:triggeredBlock:]
- -[SBSystemApertureControllerProxy animateTransitionAcceptanceBounceWithVelocityVector:triggeredBlock:]
- -[SBTraitsEmbeddedDisplayPipelineManager _continuousFoldPinNeedsPoseSettleWindow]
- -[SBTransientOverlayScenePresenter windowSceneDidDisconnect:]
- GCC_except_table1036
- GCC_except_table1038
- GCC_except_table1081
- GCC_except_table1092
- GCC_except_table1144
- GCC_except_table119
- GCC_except_table1192
- GCC_except_table1199
- GCC_except_table1201
- GCC_except_table1203
- GCC_except_table1205
- GCC_except_table161
- GCC_except_table227
- GCC_except_table281
- GCC_except_table287
- GCC_except_table291
- GCC_except_table315
- GCC_except_table327
- GCC_except_table353
- GCC_except_table356
- GCC_except_table357
- GCC_except_table359
- GCC_except_table368
- GCC_except_table371
- GCC_except_table386
- GCC_except_table388
- GCC_except_table402
- GCC_except_table406
- GCC_except_table409
- GCC_except_table411
- GCC_except_table427
- GCC_except_table438
- GCC_except_table441
- GCC_except_table444
- GCC_except_table447
- GCC_except_table450
- GCC_except_table453
- GCC_except_table460
- GCC_except_table501
- GCC_except_table506
- GCC_except_table509
- GCC_except_table512
- GCC_except_table515
- GCC_except_table518
- GCC_except_table521
- GCC_except_table605
- GCC_except_table624
- GCC_except_table632
- GCC_except_table634
- GCC_except_table637
- GCC_except_table639
- GCC_except_table641
- GCC_except_table660
- GCC_except_table664
- GCC_except_table670
- GCC_except_table683
- GCC_except_table688
- GCC_except_table700
- GCC_except_table701
- GCC_except_table703
- GCC_except_table716
- GCC_except_table728
- GCC_except_table790
- GCC_except_table827
- GCC_except_table907
- GCC_except_table943
- GCC_except_table950
- GCC_except_table991
- _OBJC_CLASS_$_CASDFGradientEffect
- _OBJC_IVAR_$_SBContinuousFadeEffectViewController._angleProgress
- _OBJC_IVAR_$_SBDefaultAuthenticationPolicy._secureBackupHelper
- _OBJC_IVAR_$_SBDeviceContinuousFoldInteractionSettings._orientationLockSettleDuration
- _OBJC_IVAR_$_SBDeviceContinuousFoldInteractionSettings._orientationLockSettleEnabled
- _OBJC_IVAR_$_SBFloatingDockController._delegate
- _OBJC_IVAR_$_SBReachabilityController._inverseReachabilityTransform
- _OBJC_IVAR_$_SBReachabilityController._reachabilityTransform
- _OBJC_IVAR_$_SBSABackgroundBlurDescription._blurElementCornerRadius
- _OBJC_IVAR_$_SBSABackgroundBlurDescription._blurElementFrame
- _OBJC_IVAR_$_SBSystemApertureBackgroundBlurView._elementCornerRadius
- _OBJC_IVAR_$_SBSystemApertureBackgroundBlurView._elementFrame
- _OBJC_IVAR_$_SBSystemApertureBackgroundBlurView._sdfElementView
- _OBJC_IVAR_$_SBSystemApertureBackgroundBlurView._sdfView
- _OBJC_IVAR_$_SBSystemApertureViewController._suppressTouchCancellationAssertion
- _OBJC_IVAR_$_SBTraitsEmbeddedDisplayPipelineManager._continuousFoldSettleGeneration
- _OBJC_IVAR_$_SBTraitsEmbeddedDisplayPipelineManager._isContinuousFoldSettleWindowActive
- _OBJC_IVAR_$_SBTransientOverlayScenePresenter._windowSceneDisconnected
- __AXSPearlAuthenticationHapticsEnabled
- __OBJC_$_CLASS_METHODS_SBChainableModifier(RuntimeProviding|WindowingModifier|SwitcherModifier)
- __OBJC_$_INSTANCE_METHODS_FBScene(SBVisibilitySceneExtension_ForSceneManager|SafeAreaResolverExtensionDelegate|SBSUIHomeScreenIconStyle|InputUISceneController|LocalSynchronous|SBSceneRegionHost|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBScreenBrightnessHost|SBProductivityGestureDestination|SBSceneAccessoryContainer|SBSceneAccessoryContainer_Internal|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
- __OBJC_$_INSTANCE_METHODS_SBChainableModifier(RuntimeProviding|WindowingModifier|SwitcherModifier)
- __OBJC_$_INSTANCE_METHODS_SBChainableModifierEvent(SBWindowingModifierActivity|SBSwitcherModifierEvent)
- __OBJC_$_INSTANCE_METHODS_SBChainableModifierEventResponse(SBWindowingModifierResponse|SBSwitcherModifierEventResponse)
- __OBJC_$_INSTANCE_METHODS_SBSwitcherModifier(WindowingModifier|SharedModifierUtilities)
- __OBJC_$_INSTANCE_METHODS_SBWindowingModifierActivity(TransitionEvent|StripChangedModifierActivity|GestureEvent)
- __OBJC_$_INSTANCE_VARIABLES_SBSystemApertureBackgroundBlurView
- __OBJC_$_PROP_LIST_SBSystemApertureBackgroundBlurView
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSafeAreaResolverExtensionDelegate
- __OBJC_CLASS_PROTOCOLS_$_FBScene(SBVisibilitySceneExtension_ForSceneManager|SafeAreaResolverExtensionDelegate|SBSUIHomeScreenIconStyle|InputUISceneController|LocalSynchronous|SBSceneRegionHost|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBScreenBrightnessHost|SBProductivityGestureDestination|SBSceneAccessoryContainer|SBSceneAccessoryContainer_Internal|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
- ___101-[SBWallpaperControllerCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_5
- ___101-[SBWallpaperControllerCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_6
- ___101-[SBWallpaperControllerCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_7
- ___101-[SBWallpaperControllerCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_8
- ___149-[SBHomeScreenController displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:]_block_invoke_5
- ___41-[SBSABackgroundBlurDescription isEqual:]_block_invoke_3
- ___41-[SBSABackgroundBlurDescription isEqual:]_block_invoke_4
- ___55-[SBDashBoardPearlUnlockBehavior handleBiometricEvent:]_block_invoke
- ___60-[SBContinuousFadeEffectViewController _applyAngleProgress:]_block_invoke
- ___61-[SBDashBoardSetupController quickFadeCursiveHelloToVisible:]_block_invoke
- ___63-[SBSABackgroundBlurDescription copyBySettingBlurElementFrame:]_block_invoke
- ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke_3
- ___65-[SBSwitcherController _applyBlankedStateForRegion:forBundleIDs:]_block_invoke_2
- ___68-[SBContinuitySessionSystemEventMonitor _aggregateLockStateChanged:]_block_invoke
- ___70-[SBLockScreenCoordinator _sendUILockStateChangedNotificationIfNeeded]_block_invoke
- ___70-[SBSABackgroundBlurDescription copyBySettingBlurElementCornerRadius:]_block_invoke
- ___73-[SBFluidSwitcherViewController _performCrossfadeIfNeededWithCompletion:]_block_invoke
- ___73-[SBFluidSwitcherViewController _performCrossfadeIfNeededWithCompletion:]_block_invoke_2
- ___79-[SBSAAcceptanceBounceBehaviorProvider _excursionDescriptionWithBounds:center:]_block_invoke
- ___80-[SBActivityModalPresentationController presentModalForActivityItem:completion:]_block_invoke
- ___81-[SBLockScreenBiometricAuthenticationCoordinator biometricResource:observeEvent:]_block_invoke
- ___88-[SBContinuousFadeEffectViewController prepareForTransitionWithMode:foldEffectProgress:]_block_invoke
- ___89-[SBDashBoardSetupController presentSetupViewIfNecessaryFromSourceController:completion:]_block_invoke_2
- ___95-[SBTraitsEmbeddedDisplayPipelineManager _releaseContinuousFoldDeviceOrientationLockValidator:]_block_invoke
- ___block_descriptor_136_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_40_e46_v16?0"SBSABackgroundBlurDescriptionMutator"8l
- ___block_descriptor_48_e8_32s40w_e22_v16?0"NSDictionary"8lw40l8s32l8
- ___block_descriptor_49_e8_32s_e8_v12?0B8ls32l8
- ___block_descriptor_56_e8_32s40w48w_e40_v24?0"<SAInvalidatable>"8"NSString"16lw40l8w48l8s32l8
- ___block_descriptor_74_e8_32s40s48s56r_e8_v16?08ls32l8r56l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48r56r64r72r_e27_v24?0"SBWindowScene"8^B16lr48l8s32l8r56l8s40l8r64l8r72l8
- __sendUILockStateChangedNotificationIfNeeded.token
- _kCASDFElementLayerModeBounds
- _kSecureBackupPassphraseKey
CStrings:
+ "\rcC\xf0!A"
+ "!CGAffineTransformIsIdentity(transform)"
+ "%@: %p"
+ "%@|%@"
+ "%{public}@ Refusing a web clip launch request that carried no identifier."
+ "%{public}@ Refusing to launch web clip with identifier:%{public}@ because it is restricted."
+ "(first)"
+ "-[SBAffordancePresenceController setAutoHideSuspended:forReason:]"
+ "-[SBHomeScreenService addApplicationIconToHomeScreenIfAbsentWithBundleIdentifier:]"
+ "<%@: %p; blurHidden: %@; blurFrame: %@>"
+ "@\"<BSInvalidatable>\"24@?0d8@?<v@?>16"
+ "@\"NSString\"16@?0@8"
+ "@[1-9]x$"
+ "Activation Allowed Distance from Screen Edge"
+ "Activation Max Angle For Vertical Movement"
+ "Activation Minimum Required Speed (in pts/s)"
+ "Activation Timeout for Held Touch Before Activating"
+ "Allowed web clip identifiers changed: %{public}@"
+ "Angle Threshold"
+ "AppSwitcherInReduceMotion"
+ "AssistantBusy"
+ "AssistantIdleAndQuiet"
+ "AssistantIslandLockedIdleTimerCapReached"
+ "AssistantIslandLockedIdleTimerCapReset"
+ "AssistantIslandLockedResponseChanged"
+ "AssistantIslandStageStateChanged"
+ "Attempted to launch restricted web clip scene %{public}@"
+ "B24@?0@\"SBIcon\"8@\"NSDictionary\"16"
+ "Biometric camera not facing user (device not closed)"
+ "Button Wake Coaching Lead-In"
+ "Camera container acquired participant"
+ "Can't open app clip with web clip identifier: '%@' because it is restricted."
+ "Cancelling in-flight press on outgoing windowScene: %{public}@"
+ "Cleared Reachability transform for display %{public}@"
+ "Cleared exclusive keyboard frame for display %{public}@"
+ "Coach During Pending Match"
+ "Coaching (Phone Only)"
+ "Commit When Content Reaches Cover"
+ "Content Fade In"
+ "Content Fade Reversal"
+ "ControlCenterOwnsTouch"
+ "Corner: Trajectory Rotation Backoff (deg)"
+ "Corner: Trajectory Rotation Factor"
+ "Corner: Tuck In Aspect Ratio (h/w)"
+ "Corner: Tuck In Threshold"
+ "Corner: Tuck In Top Width Factor"
+ "CrossfadeChange"
+ "CurrentLayoutBecauseMovedBackDownInReduceMotionSwitcher"
+ "DefaultTodayViewLayoutExcludingProactiveStackPlacementUnmodified"
+ "DefaultTodayViewLayoutIncludingProactiveStackPlacementUnmodified"
+ "DefaultTodayViewLayoutModified"
+ "DefaultTodayViewLayoutUnavailable"
+ "Deferring backlight layout update until the primary publisher's display content mode transition ends; reason: %{public}@"
+ "Denying new scene request from %{public}@: target window scene does not support multitasking: %{public}@"
+ "Detection"
+ "Dismissing Spotlight for transition source %{public}@ from home screen region %{public}@ to %{public}@"
+ "Display region blanking latency not reported for request %{public}@: display inactive"
+ "Display region blanking: not activating %{public}@ because it has no application process"
+ "DropZoneInReduceMotionFromSwitcher"
+ "DuoAuth"
+ "Duration (Pending Match)"
+ "Duration (Wake)"
+ "Face"
+ "Fade Trigger"
+ "Fade When CoverSheet Already Presented"
+ "Failed to compute animation settings"
+ "Failed to register for UI lock state publishing: %u"
+ "GardenGate"
+ "Guaranteed Indicator Contrast Width"
+ "Hangs Off Sensor"
+ "Ignoring non-Mesa biounlock for rest to open"
+ "Keep Alive After Touch"
+ "LayoutState"
+ "Lift To Wake Suppression"
+ "Loaded image from file path: %{public}@ at scale: %.0f"
+ "Lock on Fold"
+ "Lock screen idle timer cap armed: touches stop extending in %g s (reason: %{public}@)"
+ "Lock screen idle timer cap reached: touches no longer extend the idle timer"
+ "Lock screen idle timer cap reset (reason: %{public}@)"
+ "LockOnFold"
+ "LockOnFoldFade-%@"
+ "Match landed after pending rest to open timer elapsed, firing"
+ "Min Coaching Visible Dur"
+ "Min Remaining To Coach"
+ "NFC_ShowEdgeCompensationAlert"
+ "No lock screen manager for the window scene hosting capture application (%@): %@"
+ "No matching folder was found on the home screen."
+ "Not clearing Reachability transform for display %{public}@: registration %{public}@ was superseded by %{public}@"
+ "Not handling biometric event, its failure feedback is suppressed"
+ "Not starting Cover Sheet Spotlight transaction because Control Center is usurping gestures on content below"
+ "Pending icon model restrictions push"
+ "Postflight: transferring VC to primary scene %{public}@"
+ "Publishing UI lock state to other processes: %d"
+ "Q16@?0@\"NSArray\"8"
+ "RM Drop Zone Crossfade Duration"
+ "Reachability transform"
+ "Reachability transform for display %{public}@ is unchanged"
+ "Refusing asset catalog that is not on the system partition: %{public}@"
+ "Refusing to dismiss the cover sheet to a secure app because the device is blocked"
+ "Registered Reachability transform %{public}@ for display %{public}@"
+ "Registered exclusive keyboard frame %{public}@ for display %{public}@"
+ "Requesting destruction of restricted web clip scene handles with intent %{public}@: %{public}@"
+ "Requesting edge compensation for 3pp case"
+ "Requesting edge compensation for Apple case"
+ "Rest to open remaining at match: %f, minimum to coach: %f"
+ "Rest to open timer elapsed while match pending, waiting for match"
+ "Restricted web clip scene destruction completed with result: %{bool}u; error: %{public}@"
+ "RouteDoubleTapForVI"
+ "S"
+ "SB-Default dispatch rules: RouteDoubleTapForVI: %{BOOL}u, pencil squeeze rule: %{BOOL}u, pencil double tap rule: %{BOOL}u"
+ "SBApplicationClassicAppZoomedInDidChangeNotification"
+ "SBLockOnFoldCoordinator"
+ "SBLockOnFoldCoordinator.closeToLockDisabled"
+ "SBLockOnFoldCoordinator.m"
+ "SBLockOnFoldFadeTrigger"
+ "SBLockOnFoldFadeWindow"
+ "SBSystemApertureViewController %p deallocated without being invalidated"
+ "SBTopAffordanceAutoHideSuspensionReasonHover"
+ "SBTopAffordanceAutoHideSuspensionReasonMenu"
+ "SBTraitsParticipantRoleLockOnFoldFade"
+ "SBWallpaperControllerCoordinator wallpaper visible"
+ "SECURE_ERASE_FAILED_MESSAGE"
+ "SECURE_ERASE_FAILED_OK"
+ "Secure app launch restricted because the device is blocked"
+ "Shake Displacement"
+ "Shake Sensor Expand"
+ "Shake Sensor Offset"
+ "Skipping watch auto unlock because unlock request source is biometric failure."
+ "Snapshot wallpaper before transferring it to the primary display"
+ "SpringBoard refused or did not finish opening the folder."
+ "Start Delay"
+ "Suppress Coaching Near Fire"
+ "Suppressing edge compensation for 3pp case"
+ "Switcher Invalidated"
+ "Target does not support multitasking"
+ "The client does not have the required entitlement."
+ "Touch ID"
+ "Transfer: gave up waiting for the wallpaper to acknowledge the transfer after %.2f seconds"
+ "Unable to close the folder that's currently open."
+ "Use Hinge Velocity Threshold"
+ "Velocity Threshold"
+ "Visualizations"
+ "Wallpaper visibility: scene %{public}@ can show the wallpaper (an assertion says it is about to be shown)"
+ "[%@] begin rotation to %@"
+ "[%{public}@] No client process for %{public}@, leaving its scene session archived"
+ "[%{public}@] Scene backgrounding and not under lock, unhosting presentation"
+ "[ActivityID: %{public}@] Dropping alert with %{public}@ priority because a full screen alert with %{public}@ priority is presented (ActivityID: %{public}@)"
+ "[CoverSheet] hides picture-in-picture for cover sheet presentation: %{BOOL}u"
+ "[SBLockOnFoldCoordinator %p]: Setting fade window visible on scene %@ (preflight)"
+ "[SBLockOnFoldCoordinator %p]: _handlePostflightForContext:%{public}@ tracksFold:%{BOOL}u"
+ "[SBLockOnFoldCoordinator %p]: _performCommit"
+ "[SBLockOnFoldCoordinator %p]: armed: %{BOOL}u (%{public}@)"
+ "[SBLockOnFoldCoordinator %p]: cloak is up as the lock starts; showing fade window without animation on scene %@"
+ "[SBLockOnFoldCoordinator %p]: cloak still installed on cover; lifting it over the fade window"
+ "[SBLockOnFoldCoordinator %p]: completed sleep-and-lock"
+ "[SBLockOnFoldCoordinator %p]: content reached the cover with the hinge at commit position"
+ "[SBLockOnFoldCoordinator %p]: cover sheet did not hide the status bar within %.0f s of the lock starting; showing it again"
+ "[SBLockOnFoldCoordinator %p]: eliding lift-to-wake suppression for generation %lu because current generation is %lu"
+ "[SBLockOnFoldCoordinator %p]: ending lift-to-wake suppression for generation %lu"
+ "[SBLockOnFoldCoordinator %p]: hinge baseline established; fully closed: %{BOOL}u"
+ "[SBLockOnFoldCoordinator %p]: hinge reached commit position but cannot commit"
+ "[SBLockOnFoldCoordinator %p]: hinge reached commit position but primary is %@"
+ "[SBLockOnFoldCoordinator %p]: hinge reached commit position with cover primary"
+ "[SBLockOnFoldCoordinator %p]: initiating sleep-and-lock"
+ "[SBLockOnFoldCoordinator %p]: not locking on fold, Close to Lock is disabled: %{public}@"
+ "[SBLockOnFoldCoordinator %p]: setting all fade windows not visible (trigger)"
+ "[SBLockOnFoldCoordinator %p]: starting lift-to-wake suppression generation %lu on scenes: %{public}@"
+ "[SBLockOnFoldFadeTrigger %p] armed"
+ "[SBLockOnFoldFadeTrigger %p] armed && !velocitySatisfied update: angle=%.3f velocity=%.3f acceleration=%.3f"
+ "[SBLockOnFoldFadeTrigger %p] firing"
+ "[SBLockOnFoldFadeTrigger %p] velocity condition satisfied. starting timer for %.3f seconds"
+ "[SBTestAutomationService] Ignoring request to start editing: editing is not allowed"
+ "[SBTestAutomationService] Received client request to get the Home Screen editing state"
+ "[SBTestAutomationService] Received client request to get the Home Screen grid size for page %ld"
+ "[SBTestAutomationService] Received client request to open the Home Screen folder '%{public}@'"
+ "[SBTestAutomationService] Received client request to set the Home Screen editing state to %d"
+ "[SBTestAutomationService] Received client request to set the Home Screen page to %ld"
+ "[Secure Erase] Did not complete; presenting failure UI"
+ "[Secure Erase] Failure acknowledged"
+ "_reevaluteCameraOverlaySessionRequest(%{public}@) dropping request -- no window scene for %{public}@"
+ "_updateLayout transition reasons carry over: another transition holds the main display layout publisher; reason: %{public}@"
+ "anyBacklightOnOrTurningOn"
+ "behavior suppresses quick unwarn extension"
+ "buttonWakeCoachingLeadIn"
+ "closeToLockDisabledAssertion"
+ "com.apple.SpringBoard.TodayViewLayout"
+ "com.apple.springboard.cutout"
+ "com.apple.springboard.disableCloseToLock"
+ "com.apple.springboard.lockstate-publish"
+ "commitWhenContentReachesCover"
+ "committed"
+ "contentFadeInDampingRatio"
+ "contentFadeInDelay"
+ "contentFadeInResponse"
+ "contentFadeReversalDampingRatio"
+ "contentFadeReversalResponse"
+ "displayIdentifier != nil"
+ "displaySwap"
+ "emergency"
+ "end rotation to %@"
+ "fadeStartHingeMonitoringAngleThreshold"
+ "fadeStartHingeVelocityThreshold"
+ "fadeWhenCoverSheetPresented"
+ "fold closed"
+ "foldWindowScenes"
+ "folder:"
+ "foreground or under lock"
+ "got invalid request to activate reachability on screen edge %@, supported axis %lu"
+ "guaranteedIndicatorContrastWidth"
+ "hasHingeBaseline"
+ "hinge open at baseline"
+ "horizontal gesture timed out"
+ "horizontalActivationMaxAngleForVerticalMovement"
+ "horizontalActivationMinimumSpeed"
+ "horizontalGestureAllowableEdgeMarginForCompletion"
+ "horizontalGestureTouchHoldTimeout"
+ "horizontalInteractiveKeepAlive"
+ "icon animator: vertical dock center point is non-finite (%{public}@), using the screen center instead"
+ "liftToWakeSuppressionDuration"
+ "liftToWakeSuppressionGeneration"
+ "liftToWakeSuppressions"
+ "minimumCoachingVisibleDuration"
+ "minimumRemainingDurationForCoaching"
+ "no allowlist"
+ "nonCenterPillShakeDisplacement"
+ "nonCenterPillShakeSensorExpansion"
+ "nonCenterPillShakeSensorOffset"
+ "oval.fill"
+ "pendingMatchRestToOpenDuration"
+ "preferredSqueezeAction"
+ "preferredTapAction"
+ "q!"
+ "reduceMotionDropZoneCrossfadeDuration"
+ "relinquishSystemAnimation"
+ "secure-erase-failed-message"
+ "secure-erase-failed-ok-button"
+ "secure-erase-failed-view"
+ "securityDefaults"
+ "showCoachingDuringPendingMatch"
+ "slidePastTouchBlockingThreshold"
+ "startFadeFromHingeVelocity"
+ "startFadeFromHingeVelocity == YES"
+ "suppressCoachingNearRestToOpenFire"
+ "suppressesQuickUnwarnExtension"
+ "systemApertureVariableBlurMask"
+ "systemKeyCommandOverlay-Main"
+ "the caller covered the panel itself"
+ "touchesBlocked"
+ "tracking"
+ "transition ended with hinge open"
+ "v16@?0@\"SBWindowScene\"8"
+ "v24@?0{?=qq}8"
+ "variableBlurMask"
+ "visualizeFadeTrigger"
+ "wakeRestToOpenDuration"
+ "zh-Hans"
+ "zoomToJindoTrajectoryRotationCornerBackoff"
+ "zoomToJindoTrajectoryRotationCornerFactor"
+ "zoomToJindoTuckInCornerAspectRatio"
+ "zoomToJindoTuckInCornerThreshold"
+ "zoomToJindoTuckInCornerTopWidthFactor"
+ "{_UICornerInsets={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}}24@?0{CGSize=dd}8"
+ "\x92"
+ "\xf0R"
+ "\xf0\x82"
+ "\xf0\x91!"
+ "\xf0\xb1"
+ "\xf0\xf0\xe1"
+ "\xf0\xf0\xf0\x83A"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb2\xf0\xf0!"
- "\rcCQA"
- "<%@: %p; blurHidden: %@; blurFrame: %@; blurElementFrame: %@; blurElementCornerRadius: %g>"
- "Continuous fold pin held for settle on %{public}@ (%.0fms, pinned device %{public}@)"
- "Dismissing Spotlight for transition source %{public}@ from home screen region %{public}@"
- "Extend Ori. Lock (LL/LR)"
- "Lock extension duration"
- "Postflight: cancelled, transferring VC to primary scene %{public}@"
- "Prevent Spurious Updates"
- "SDF gradient"
- "Snapshot wallpaper before transferring it on cancellation"
- "Swipe HID event"
- "TouchID-Trailing-V68"
- "TouchId"
- "blurElementCornerRadius"
- "blurElementFrame"
- "horizontal reachability ignoring touch while the screen is off"
- "orientationLockSettleDuration"
- "orientationLockSettleEnabled"
- "variableBlurView.elementCornerRadius"
- "variableBlurView.elementFrame"
- "\xd2\xf0\xf0\xf0\xf0\xe1"
- "\xf02"
- "\xf0r"
- "\xf0\xa1!"
- "\xf0\xf0\xd1"
- "\xf0\xf0\xf0ACA"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa2\xf0\xf0!"
```
