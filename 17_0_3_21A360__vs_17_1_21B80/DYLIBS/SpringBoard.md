## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4416.11.7.0.0
-  __TEXT.__text: 0x86f260
-  __TEXT.__auth_stubs: 0x4e00
+4416.25.105.0.0
+  __TEXT.__text: 0x876628
+  __TEXT.__auth_stubs: 0x4e70
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x84044
-  __TEXT.__const: 0x10c20
-  __TEXT.__cstring: 0x6956d
-  __TEXT.__gcc_except_tab: 0xde2c
-  __TEXT.__oslogstring: 0x46c90
+  __TEXT.__objc_methlist: 0x84474
+  __TEXT.__const: 0x10c40
+  __TEXT.__cstring: 0x69add
+  __TEXT.__gcc_except_tab: 0xe0b4
+  __TEXT.__oslogstring: 0x4765c
   __TEXT.__ustring: 0x146e
   __TEXT.__dlopen_cstrs: 0x2e6
-  __TEXT.__unwind_info: 0x23578
+  __TEXT.__unwind_info: 0x2376c
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x1b829
-  __TEXT.__objc_methname: 0x1821ee
-  __TEXT.__objc_methtype: 0x3e74a
-  __TEXT.__objc_stubs: 0xcde20
+  __TEXT.__objc_classname: 0x1b92a
+  __TEXT.__objc_methname: 0x1835b2
+  __TEXT.__objc_methtype: 0x3e960
+  __TEXT.__objc_stubs: 0xce700
   __DATA_CONST.__got: 0x2748
-  __DATA_CONST.__const: 0x19210
-  __DATA_CONST.__objc_classlist: 0x4470
+  __DATA_CONST.__const: 0x19230
+  __DATA_CONST.__objc_classlist: 0x4488
   __DATA_CONST.__objc_catlist: 0x2a0
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2170
+  __DATA_CONST.__objc_protolist: 0x2190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1d81b0
-  __DATA_CONST.__objc_selrefs: 0x3de70
-  __DATA_CONST.__objc_arraydata: 0x14f8
-  __AUTH_CONST.__cfstring: 0x5fbc0
-  __AUTH_CONST.__objc_const: 0x2e438
-  __AUTH_CONST.__const: 0xe0a0
-  __AUTH_CONST.__objc_arrayobj: 0x15a8
-  __AUTH_CONST.__objc_intobj: 0x2460
-  __AUTH_CONST.__objc_doubleobj: 0x520
+  __DATA_CONST.__objc_const: 0x1d9028
+  __DATA_CONST.__objc_selrefs: 0x3e100
+  __DATA_CONST.__objc_arraydata: 0x14e0
+  __AUTH_CONST.__cfstring: 0x600c0
+  __AUTH_CONST.__objc_const: 0x2e558
+  __AUTH_CONST.__const: 0xdfa0
+  __AUTH_CONST.__objc_arrayobj: 0x1590
+  __AUTH_CONST.__objc_intobj: 0x2418
+  __AUTH_CONST.__objc_doubleobj: 0x530
   __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH_CONST.__auth_got: 0x2718
-  __AUTH.__objc_data: 0xf000
+  __AUTH_CONST.__auth_got: 0x2750
+  __AUTH.__objc_data: 0xf140
   __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0x6330
-  __DATA.__objc_superrefs: 0x3548
-  __DATA.__objc_ivar: 0xc678
-  __DATA.__data: 0x1a4a8
+  __DATA.__objc_classrefs: 0x6370
+  __DATA.__objc_superrefs: 0x3560
+  __DATA.__objc_ivar: 0xc6f8
+  __DATA.__data: 0x1a628
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0xb70
+  __DATA.__bss: 0xba0
   __DATA.__common: 0x58
-  __DATA_DIRTY.__objc_data: 0x1bc60
+  __DATA_DIRTY.__objc_data: 0x1bc10
   __DATA_DIRTY.__data: 0x138
   __DATA_DIRTY.__bss: 0x1510
   __DATA_DIRTY.__common: 0x40

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 08F086A2-FB24-3D29-AEF5-C344B7CB5A3E
-  Functions: 55923
-  Symbols:   190534
-  CStrings:  88184
+  UUID: 0999BB61-D20B-3B37-9CD8-90A29A4E3B49
+  Functions: 56059
+  Symbols:   190992
+  CStrings:  88452
 
Symbols:
+ +[SBAmbientTelemetryEmitter _ambientCoreAnalyticsActiveFaceDescription:screenOffDuration:sessionIdString:]
+ +[SBAmbientTelemetryEmitter _ambientPowerLogAmbientMotionToWakeEnabled:]
+ +[_SBAdaptiveColorMatrixView layerClass]
+ -[SBAbstractSystemActionExecutor _beginInteractiveExecutionWithContext:executionHandler:error:]
+ -[SBAbstractSystemActionExecutor _requiresAuthenticationAtLeastOnceSinceBootBeforeExecution]
+ -[SBAbstractSystemActionExecutor executeWithContext:executionHandler:completion:]
+ -[SBAbstractSystemActionExecutor executeWithContext:executionHandler:completion:].cold.1
+ -[SBAbstractSystemActionExecutor executeWithContext:executionHandler:completion:].cold.2
+ -[SBAbstractSystemActionExecutor executionGeneration]
+ -[SBAbstractSystemActionExecutor requiresAuthenticationAtLeastOnceSinceBootBeforeExecution]
+ -[SBActivityAmbientViewController setCompactOverlayHidden:]
+ -[SBActivityBannerObserver _isActivityOngoing:]
+ -[SBActivityBannerViewController _backgroundTintColorForUserInterfaceStyle:]
+ -[SBActivityBannerViewController _shouldSetDefaultBackground]
+ -[SBActivityBannerViewController userInterfaceStyleChangedForEnvironment:previousTraitCollection:]
+ -[SBActivitySystemApertureElementObserver _activatedElementItemForBundleIdentifier:]
+ -[SBAllowAmbientIdleTimerAttributeHandler countingTargetForEntry:]
+ -[SBAllowAmbientIdleTimerAttributeHandler countingTargetForEntry:].cold.1
+ -[SBAmbientIdleTimerController _isIdleTimerAllowedForAssertionsForSleepFocus]
+ -[SBAmbientIdleTimerController _setIdleTimerAllowedForAssertions:forSleepFocus:]
+ -[SBAmbientIdleTimerController _setIdleTimerAllowedForAssertionsForSleepFocus:]
+ -[SBAmbientIdleTimerController setSuppressForSleep:]
+ -[SBAmbientIdleTimerController suppressForSleep]
+ -[SBAmbientPresentationController _dismissAllOtherAmbientTransientOverlays]
+ -[SBAmbientPresentationController _displayTransientLockElementIfNecessaryForKeyBagState:]
+ -[SBAmbientPresentationController _effectiveAlwaysOnMode]
+ -[SBAmbientPresentationController _hideLockElement]
+ -[SBAmbientPresentationController _invalidateTransientOverlayWindowTraitsArbiterParticipantIfNeeded]
+ -[SBAmbientPresentationController _isCoverSheetPresentedByUserGesture]
+ -[SBAmbientPresentationController _isMotionToWakePermitted]
+ -[SBAmbientPresentationController _isNightModeSettingMandatory]
+ -[SBAmbientPresentationController _isNightModeUserSettingEffectivelyEnabled]
+ -[SBAmbientPresentationController _resetTransientLockSuppressionFlag]
+ -[SBAmbientPresentationController _setCoverSheetPresentedByUserGesture:]
+ -[SBAmbientPresentationController _shouldSuppressForSleep]
+ -[SBAmbientPresentationController _updateAmbientMountState:withReason:]
+ -[SBAmbientPresentationController _updateAmbientTriggerState:analogousTriggerEvents:withReason:]
+ -[SBAmbientPresentationController _updatePresentationPossibleForMountState:]
+ -[SBAmbientPresentationController _updateSleepSuppression]
+ -[SBAmbientPresentationController ambientPresentationManager:didUpdateMountState:]
+ -[SBAmbientPresentationController ambientPresentationManager:didUpdateTriggerState:analogousTriggerEvents:]
+ -[SBAmbientPresentationController conformsToCSEventHandling]
+ -[SBAmbientPresentationController coverSheetIdentifier]
+ -[SBAmbientPresentationController handleEvent:]
+ -[SBAmbientPresentationController keybag:extendedStateDidChange:]
+ -[SBAmbientPresentationController participantState]
+ -[SBAmbientPresentationController wouldHandleButtonEvent:]
+ -[SBAmbientPresentationController(Test) test_updateAmbientMountState:withReason:]
+ -[SBAmbientPresentationController(Test) test_updateAmbientTriggerState:withReason:]
+ -[SBAmbientProudLockViewController .cxx_destruct]
+ -[SBAmbientProudLockViewController _canShowWhileLocked]
+ -[SBAmbientProudLockViewController _dismissTransientProudLockAnimated]
+ -[SBAmbientProudLockViewController _prepareBlurForWrapperView]
+ -[SBAmbientProudLockViewController hasPasscodeSet]
+ -[SBAmbientProudLockViewController initWithBiometricResource:authenticationController:]
+ -[SBAmbientProudLockViewController init]
+ -[SBAmbientProudLockViewController isBiometricLockedOut]
+ -[SBAmbientProudLockViewController setAuthenticated:completion:]
+ -[SBAmbientProudLockViewController viewDidLoad]
+ -[SBAmbientTelemetryEmitter _updateActiveFaceScreenOffForBacklightState:forConfiguration:sessionIdString:]
+ -[SBAmbientTelemetryEmitter logTelemetryForAmbientPresented:withBacklightState:screenOffWithConfiguration:]
+ -[SBAmbientTelemetryEmitter logTelemetryForMotionToWakeEnabled:]
+ -[SBAmbientTransientOverlayViewController _addProudLockViewControllerIfNecessary]
+ -[SBAmbientTransientOverlayViewController _removeProudLockViewController]
+ -[SBAmbientTransientOverlayViewController _setProudLockAuthenticated:]
+ -[SBAmbientTransientOverlayViewController ambientViewController:isApplicationVisibleWithBundleIdentifier:]
+ -[SBAmbientTransientOverlayViewController displayTransientProudLock]
+ -[SBAmbientTransientOverlayViewController isForegroundActive]
+ -[SBAppExposeContinuousExposeSwitcherModifier adjustedContinuousExposeIdentifiersInSwitcherFromPreviousIdentifiersInSwitcher:identifiersInStrip:]
+ -[SBAppSwitcherContinuousExposeSwitcherModifier _heightForCardInSwitcherWithScaleFactor:]
+ -[SBBannerAuthority _isHealthFocusedEvaluationModeActive]
+ -[SBBannerAuthority _setHealthFocusedEvaluationModeActive:]
+ -[SBBlockSystemAction analyticsData]
+ -[SBBlockSystemActionExecutor _beginInteractiveExecutionWithContext:executionHandler:error:]
+ -[SBBlockSystemActionExecutor _handleExecutionBlockFinishedWithResult:]
+ -[SBBlockSystemActionExecutor _requiresAuthenticationAtLeastOnceSinceBootBeforeExecution]
+ -[SBCoverSheetPresentationManager coverSheetViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:]
+ -[SBCoverSheetSecureAppEnvironmentViewController _updateZStackPolicyAssistants]
+ -[SBCoverSheetSecureAppEnvironmentViewController audioCategoryZStackPolicyAssistantDidChange:]
+ -[SBCoverSheetSecureAppEnvironmentViewController physicalButtonZStackPolicyAssistantDidChange:]
+ -[SBDashBoardCameraPageViewController audioCategoryZStackPolicyAssistantDidChange:]
+ -[SBDashBoardCameraPageViewController audioCategoryZStackPolicyAssistant]
+ -[SBDashBoardCameraPageViewController setAudioCategoryZStackPolicyAssistant:]
+ -[SBDeviceApplicationRemoteTransientOverlayViewProvider wantsResignActiveAssertion]
+ -[SBFlashlightElement isMinimalPresentationPossible]
+ -[SBFluidSwitcherViewController _medusaCapabilityChanged:]
+ -[SBFluidSwitcherViewController _reevaluateWindowManagementStyle]
+ -[SBFluidSwitcherViewController isMedusaCapable]
+ -[SBFocusEnablementIndicatorSystemApertureActivityElement isMinimalPresentationPossible]
+ -[SBFullScreenToHomePIPSwitcherModifier initWithTransitionID:appLayout:layoutRole:]
+ -[SBHungApplicationInteractionObserver _lockStateDidChange:]
+ -[SBHungApplicationInteractionObserver _notifyInteractionWithPossiblyHungApplicationSceneEntities:withInteractionType:]
+ -[SBHungApplicationInteractionObserver _notifyInteractionWithPossiblyHungApplicationSceneEntities:withInteractionType:].cold.1
+ -[SBHungApplicationInteractionObserver _transitionContextRepresentsActivatingAppFromAppSwitcher:]
+ -[SBHungApplicationInteractionObserver _transitionContextRepresentsActivatingDynamicIslandApp:]
+ -[SBHungApplicationInteractionObserver _transitionContextRepresentsActivatingHomeScreen:]
+ -[SBHungApplicationInteractionObserver _transitionContextRepresentsArcSwipingToPreviousApp:]
+ -[SBHungApplicationInteractionObserver _transitionContextRepresentsTappingBreadcrumbToPreviousApp:]
+ -[SBHungApplicationInteractionObserver activate]
+ -[SBHungApplicationInteractionObserver activate].cold.1
+ -[SBHungApplicationInteractionObserver observeBackgroundingApplicationSceneEntities:withTransitionContext:]
+ -[SBHungApplicationInteractionObserver observeBackgroundingApplicationSceneEntities:withTransitionContext:].cold.1
+ -[SBHungApplicationInteractionObserver observeRemovedApplicationSceneEntity:]
+ -[SBHungApplicationInteractionObserver previousLockState]
+ -[SBHungApplicationInteractionObserver setPreviousLockState:]
+ -[SBIconController isIconVisibleForBundleIdentifier:]
+ -[SBLinkSystemActionExecutor _beginInteractiveExecutionWithContext:executionHandler:error:]
+ -[SBLinkSystemActionExecutor _requiresAuthenticationAtLeastOnceSinceBootBeforeExecution]
+ -[SBLockScreenManager coverSheetViewController:requestsPreArmDisabled:forReason:]
+ -[SBMainWorkspace _updateMedusaCapabilitySendingNotification:]
+ -[SBMainWorkspace isMedusaCapable]
+ -[SBMedusaDecoratedDeviceApplicationSceneViewController _medusaCapabilityChanged:]
+ -[SBPhysicalButtonSceneOverrideManager _canSendVolumeButtonEventsToScene:withConfiguration:activeVolumeCategoryName:isAudioSessionPlaying:]
+ -[SBPhysicalButtonSceneOverrideManager cache:didUpdateAudioSessionPlaying:]
+ -[SBPropertyAnimatingView .cxx_destruct]
+ -[SBPropertyAnimatingView _shouldAnimatePropertyWithKey:]
+ -[SBPropertyAnimatingView animatedLayerProperties]
+ -[SBPropertyAnimatingView setAnimatedLayerProperties:]
+ -[SBReachabilityBackgroundView _invertColorsChanged:]
+ -[SBReachabilityBackgroundView _invertColorsIsEnabled]
+ -[SBReachabilityBackgroundView _newWallpaperViewForVariant:]
+ -[SBReachabilityBackgroundView _setupColorInvertObservation]
+ -[SBReachabilityBackgroundView _setupCornerContentsImageForWallpaperView:]
+ -[SBReachabilityBackgroundView _updateColorMatrixAlpha:]
+ -[SBReachabilityBackgroundView _updateColorMatrixFilters]
+ -[SBReachabilityBackgroundView _updateWallpaperViewAnimated:]
+ -[SBReachabilityBackgroundView _updateWallpaperViewFilters]
+ -[SBReachabilityManager _invalidateJindoReason]
+ -[SBReachabilitySettings jindoInertDisableOffset]
+ -[SBReachabilitySettings jindoTintColorMatrixSettings]
+ -[SBReachabilitySettings setJindoInertDisableOffset:]
+ -[SBReachabilitySettings setJindoTintColorMatrixSettings:]
+ -[SBSAAcceptanceBounceBehaviorProvider removeFromParentProvider].cold.1
+ -[SBSAEjectStretchBehaviorProvider _isTimerExpired:].cold.1
+ -[SBSAEjectStretchBehaviorProvider _startTimerIfNecessary:context:]
+ -[SBSAEjectStretchBehaviorProvider _startTimerIfNecessary:context:].cold.1
+ -[SBSASettlingBehaviorProvider _overshootOutsetsForTransitionPhase:baseOutsets:elementContext:]
+ -[SBSceneResizeGestureRootSwitcherModifier handleTransitionEvent:]
+ -[SBSystemAction analyticsData]
+ -[SBSystemAction hostBundleRequiresValidation]
+ -[SBSystemActionAnalyticsTracker _logSignificantTimeChanged]
+ -[SBSystemActionAnalyticsTracker _sendEventToPowerLog:payload:]
+ -[SBSystemActionAnalyticsTracker init]
+ -[SBSystemActionAnalyticsTracker trackSelectedActionChanged:]
+ -[SBSystemActionCoachingController _canPresentCoachingForAction:]
+ -[SBSystemActionCoachingController activityManager]
+ -[SBSystemActionCoachingController delegate]
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:]
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.1
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.2
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.3
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.4
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.5
+ -[SBSystemActionCoachingController initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.6
+ -[SBSystemActionCoachingController setDelegate:]
+ -[SBSystemActionCoachingHUDViewController activityManager]
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:]
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.1
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.2
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.3
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.4
+ -[SBSystemActionCoachingHUDViewController initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.5
+ -[SBSystemActionControl _executionHandlerForExecutor:]
+ -[SBSystemActionControl authenticationStatusProvider]
+ -[SBSystemActionControl initWithDataSource:previewCoordinator:authenticationStatusProvider:coachingController:soundController:]
+ -[SBSystemActionControl initWithDataSource:previewCoordinator:authenticationStatusProvider:coachingController:soundController:].cold.1
+ -[SBSystemActionControl initWithDataSource:previewCoordinator:authenticationStatusProvider:coachingController:soundController:].cold.2
+ -[SBSystemActionControl initWithDataSource:previewCoordinator:authenticationStatusProvider:coachingController:soundController:].cold.3
+ -[SBSystemActionControl initWithDataSource:previewCoordinator:authenticationStatusProvider:coachingController:soundController:].cold.4
+ -[SBSystemActionControl initWithDataSource:previewCoordinator:authenticationStatusProvider:coachingController:soundController:].cold.5
+ -[SBSystemActionControl selectedActionAnalyticsData]
+ -[SBSystemActionControl systemActionCoachingController:canPresentCoachingForAction:]
+ -[SBSystemActionSimplePreviewElement isMinimalPresentationPossible]
+ -[SBSystemActionSimplePreviewElement shouldSuppressElementWhilePresentingAppWithBundleId:]
+ -[SBSystemActionSuppressionManager _queryPocketStateWithTimeout:]
+ -[SBSystemActionSuppressionManager systemActionInteractionDidStartWithLongPressTimeout:]
+ -[SBSystemApertureController overrideContainerRenderingStyleAssertion:]
+ -[SBSystemApertureSettings acceptanceSideBounceFinishingDelay]
+ -[SBSystemApertureSettings acceptanceUpBounceFinishingDelay]
+ -[SBSystemApertureSettings ejectionYUpOffset]
+ -[SBSystemApertureSettings setAcceptanceSideBounceFinishingDelay:]
+ -[SBSystemApertureSettings setAcceptanceUpBounceFinishingDelay:]
+ -[SBSystemApertureSettings setEjectionYUpOffset:]
+ -[SBSystemApertureViewController _activeElementInterfaceOrientation].cold.1
+ -[SBSystemApertureViewController _effectiveOverrideRenderingStyle]
+ -[SBSystemApertureViewController _handleHitTestingUpdatesWithContext:]
+ -[SBSystemApertureViewController overrideContainerRenderingStyleAssertion:]
+ -[SBSystemApertureViewController(Private) _updateElementOrientationTo:withTransitionCoordinator:]
+ -[SBSystemApertureViewController(Private) hostOrientationDidChangeTo:withPreviousOrientation:context:]
+ -[SBSystemApertureViewController(Private) hostOrientationDidChangeTo:withPreviousOrientation:context:].cold.1
+ -[SBVolumeControl _displaysVolumeForCategory:]
+ -[SBVolumeControl canChangeVolumeForActiveCategory:isAudioSessionPlaying:]
+ -[SBWallpaperController _updateForLockScreenPosterConfiguration:homeScreenPosterConfiguration:].cold.7
+ -[SBWorkspaceKeyboardFocusController setExternalSceneWithFocus:]
+ -[SpringBoard hungApplicationInteractionObserver]
+ -[WFConfiguredStaccatoAction sb_configuredIntentAction]
+ -[WFConfiguredStaccatoAction sb_configuredIntentAction].cold.1
+ -[_SBAdaptiveColorMatrixView backdropLayer]
+ GCC_except_table129
+ GCC_except_table179
+ GCC_except_table219
+ GCC_except_table299
+ GCC_except_table367
+ GCC_except_table409
+ GCC_except_table549
+ GCC_except_table564
+ GCC_except_table742
+ GCC_except_table745
+ GCC_except_table750
+ _AMStringForAmbientMountState
+ _AMStringForAmbientTriggerState
+ _NSStringFromSwitcherWindowManagementStyle
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_CLASS_$_SBAmbientProudLockViewController
+ _OBJC_CLASS_$_SBFCAColorMatrixSettings
+ _OBJC_CLASS_$_SBHungApplicationInteractionObserver
+ _OBJC_CLASS_$_SBPropertyAnimatingView
+ _OBJC_CLASS_$_SBUIProudLockContainerViewController
+ _OBJC_CLASS_$_UITraitUserInterfaceStyle
+ _OBJC_CLASS_$_WFApertureIconView
+ _OBJC_CLASS_$__SBAdaptiveColorMatrixView
+ _OBJC_IVAR_$_SBAbstractSystemActionExecutor._executionGeneration
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._idleTimerAllowedForAssertionsForSleepFocus
+ _OBJC_IVAR_$_SBAmbientIdleTimerController._suppressForSleep
+ _OBJC_IVAR_$_SBAmbientPresentationController._coverSheetPresentedByUserGesture
+ _OBJC_IVAR_$_SBAmbientPresentationController._lastKeyBagState
+ _OBJC_IVAR_$_SBAmbientPresentationController._shouldSuppressTransientLockIfKeyBagLocks
+ _OBJC_IVAR_$_SBAmbientProudLockViewController._authenticationCompletion
+ _OBJC_IVAR_$_SBAmbientProudLockViewController._authenticationController
+ _OBJC_IVAR_$_SBAmbientProudLockViewController._biometricResource
+ _OBJC_IVAR_$_SBAmbientProudLockViewController._proudLockContainerViewController
+ _OBJC_IVAR_$_SBAmbientProudLockViewController._proudLockWrapperView
+ _OBJC_IVAR_$_SBAmbientTelemetryEmitter._ambientActiveFaceSceenOffTimestamp
+ _OBJC_IVAR_$_SBAmbientTransientOverlayViewController._proudLockViewController
+ _OBJC_IVAR_$_SBBannerAuthority._healthFocusedEvaluationModeActive
+ _OBJC_IVAR_$_SBCoverSheetSecureAppEnvironmentViewController._audioCategoryZStackPolicyAssistant
+ _OBJC_IVAR_$_SBCoverSheetSecureAppEnvironmentViewController._physicalButtonZStackPolicyAssistant
+ _OBJC_IVAR_$_SBDashBoardCameraPageViewController._audioCategoryZStackPolicyAssistant
+ _OBJC_IVAR_$_SBHungApplicationInteractionObserver._previousLockState
+ _OBJC_IVAR_$_SBLockElementViewProvider._priorLayoutMode
+ _OBJC_IVAR_$_SBMainWorkspace._medusaCapable
+ _OBJC_IVAR_$_SBPropertyAnimatingView.animatedLayerProperties
+ _OBJC_IVAR_$_SBReachabilityBackgroundView._bottomWallpaperView
+ _OBJC_IVAR_$_SBReachabilityBackgroundView._colorMatrixOpacityAnimatableProperty
+ _OBJC_IVAR_$_SBReachabilityBackgroundView._colorMatrixView
+ _OBJC_IVAR_$_SBReachabilityBackgroundView._topWallpaperView
+ _OBJC_IVAR_$_SBReachabilityManager._jindoInertAssertion
+ _OBJC_IVAR_$_SBReachabilityManager._jindoInertTimer
+ _OBJC_IVAR_$_SBReachabilitySettings._jindoInertDisableOffset
+ _OBJC_IVAR_$_SBReachabilitySettings._jindoTintColorMatrixSettings
+ _OBJC_IVAR_$_SBSystemAction._analyticsData
+ _OBJC_IVAR_$_SBSystemAction._hostBundleRequiresValidation
+ _OBJC_IVAR_$_SBSystemActionAnalyticsTracker._lastQueriedParameterValueIdentifier
+ _OBJC_IVAR_$_SBSystemActionAnalyticsTracker._powerLogSendQueue
+ _OBJC_IVAR_$_SBSystemActionCoachingController._activityManager
+ _OBJC_IVAR_$_SBSystemActionCoachingController._delegate
+ _OBJC_IVAR_$_SBSystemActionCoachingHUDViewController._activityManager
+ _OBJC_IVAR_$_SBSystemActionControl._authenticationStatusProvider
+ _OBJC_IVAR_$_SBSystemApertureController._overrideRenderingStyleAssertion
+ _OBJC_IVAR_$_SBSystemApertureSettings._acceptanceSideBounceFinishingDelay
+ _OBJC_IVAR_$_SBSystemApertureSettings._acceptanceUpBounceFinishingDelay
+ _OBJC_IVAR_$_SBSystemApertureSettings._ejectionYUpOffset
+ _OBJC_IVAR_$_SBSystemApertureViewController._overrideRenderingStyleRequests
+ _OBJC_IVAR_$_SpringBoard._hungApplicationInteractionObserver
+ _OBJC_METACLASS_$_SBAmbientProudLockViewController
+ _OBJC_METACLASS_$_SBHungApplicationInteractionObserver
+ _OBJC_METACLASS_$_SBPropertyAnimatingView
+ _OBJC_METACLASS_$__SBAdaptiveColorMatrixView
+ _PBUIMaterialsIsLowQualityDevice
+ _SBLogHangTracer
+ _SBLogSystemActionCoaching
+ _SBLogSystemActionCoaching.__logObj
+ _SBLogSystemActionCoaching.onceToken
+ _SBLogSystemApertureOrientation
+ _SBLogSystemApertureOrientation.__logObj
+ _SBLogSystemApertureOrientation.onceToken
+ _SBRectEqualsRect
+ _SBSwitcherWallpaperGradientAttributesEqual
+ _SBSwitcherWallpaperGradientAttributesMakeEmpty
+ _SBWorkspaceMedusaCapabilityChangedNotification
+ _UIFloorToScale
+ _UIRectCenteredYInRect
+ __OBJC_$_CLASS_METHODS__SBAdaptiveColorMatrixView
+ __OBJC_$_INSTANCE_METHODS_SBAmbientProudLockViewController
+ __OBJC_$_INSTANCE_METHODS_SBHungApplicationInteractionObserver
+ __OBJC_$_INSTANCE_METHODS_SBPropertyAnimatingView
+ __OBJC_$_INSTANCE_METHODS__SBAdaptiveColorMatrixView
+ __OBJC_$_INSTANCE_VARIABLES_SBAmbientProudLockViewController
+ __OBJC_$_INSTANCE_VARIABLES_SBHungApplicationInteractionObserver
+ __OBJC_$_INSTANCE_VARIABLES_SBPropertyAnimatingView
+ __OBJC_$_PROP_LIST_SBAmbientProudLockViewController
+ __OBJC_$_PROP_LIST_SBFCustomImplicitPropertyAnimating
+ __OBJC_$_PROP_LIST_SBPropertyAnimatingView
+ __OBJC_$_PROP_LIST_SBUIProudLockContainerViewControllerLockStatusProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FCUISystemApertureElementProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBFCustomImplicitPropertyAnimating
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSystemActionCoachingControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSystemApertureHostOrientationObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBUIProudLockContainerViewControllerLockStatusProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBFCustomImplicitPropertyAnimating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSystemActionCoachingControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSystemApertureHostOrientationObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBUIProudLockContainerViewControllerLockStatusProvider
+ __OBJC_$_PROTOCOL_REFS_SBFCustomImplicitPropertyAnimating
+ __OBJC_$_PROTOCOL_REFS_SBSystemActionCoachingControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_SBSystemApertureHostOrientationObserving
+ __OBJC_$_PROTOCOL_REFS_SBUIProudLockContainerViewControllerLockStatusProvider
+ __OBJC_CLASS_PROTOCOLS_$_SBAmbientProudLockViewController
+ __OBJC_CLASS_PROTOCOLS_$_SBPropertyAnimatingView
+ __OBJC_CLASS_RO_$_SBAmbientProudLockViewController
+ __OBJC_CLASS_RO_$_SBHungApplicationInteractionObserver
+ __OBJC_CLASS_RO_$_SBPropertyAnimatingView
+ __OBJC_CLASS_RO_$__SBAdaptiveColorMatrixView
+ __OBJC_LABEL_PROTOCOL_$_SBFCustomImplicitPropertyAnimating
+ __OBJC_LABEL_PROTOCOL_$_SBSystemActionCoachingControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBSystemApertureHostOrientationObserving
+ __OBJC_LABEL_PROTOCOL_$_SBUIProudLockContainerViewControllerLockStatusProvider
+ __OBJC_METACLASS_RO_$_SBAmbientProudLockViewController
+ __OBJC_METACLASS_RO_$_SBHungApplicationInteractionObserver
+ __OBJC_METACLASS_RO_$_SBPropertyAnimatingView
+ __OBJC_METACLASS_RO_$__SBAdaptiveColorMatrixView
+ __OBJC_PROTOCOL_$_SBFCustomImplicitPropertyAnimating
+ __OBJC_PROTOCOL_$_SBSystemActionCoachingControllerDelegate
+ __OBJC_PROTOCOL_$_SBSystemApertureHostOrientationObserving
+ __OBJC_PROTOCOL_$_SBUIProudLockContainerViewControllerLockStatusProvider
+ __SBSAMinimumFrameForElementAtIndex
+ ___101-[SBActivityBannerObserver _postBannerWithActivityIdentifier:payloadIdentifier:prominent:completion:]_block_invoke.26
+ ___106+[SBAmbientTelemetryEmitter _ambientCoreAnalyticsActiveFaceDescription:screenOffDuration:sessionIdString:]_block_invoke
+ ___111-[SBCoverSheetPresentationManager _setTransitionProgress:animated:gestureActive:coverSheetProgress:completion:]_block_invoke.200
+ ___111-[SBCoverSheetPresentationManager _setTransitionProgress:animated:gestureActive:coverSheetProgress:completion:]_block_invoke.201
+ ___111-[SBCoverSheetPresentationManager _setTransitionProgress:animated:gestureActive:coverSheetProgress:completion:]_block_invoke.203
+ ___170-[SBFluidSwitcherViewController initWithSwitcherController:rootModifier:liveContentOverlayCoordinator:delegate:dataSource:shouldObserveChamoisWindowingChanges:debugName:]_block_invoke.108
+ ___38-[SBSystemActionAnalyticsTracker init]_block_invoke
+ ___39-[SBVolumeControl changeVolumeByDelta:]_block_invoke.150
+ ___43-[SBRecentAppLayoutsPersister _loadRecents]_block_invoke
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.863
+ ___47-[SBAmbientProudLockViewController viewDidLoad]_block_invoke
+ ___47-[SBAmbientProudLockViewController viewDidLoad]_block_invoke_2
+ ___47-[SBBannerAuthority _configureSinksIfNecessary]_block_invoke.23
+ ___47-[SBBannerAuthority _configureSinksIfNecessary]_block_invoke.23.cold.1
+ ___47-[SBBannerAuthority _configureSinksIfNecessary]_block_invoke.27
+ ___47-[SBBannerAuthority _configureSinksIfNecessary]_block_invoke.35
+ ___47-[SBBannerAuthority _configureSinksIfNecessary]_block_invoke.35.cold.1
+ ___47-[SBBannerAuthority _configureSinksIfNecessary]_block_invoke.38
+ ___48-[SBReachabilityManager canActivateReachability]_block_invoke.103
+ ___48-[SBReachabilityManager canActivateReachability]_block_invoke.117
+ ___48-[SBReachabilityManager canActivateReachability]_block_invoke.124
+ ___54-[SBSystemActionControl _executionHandlerForExecutor:]_block_invoke
+ ___54-[SBSystemActionControl _executionHandlerForExecutor:]_block_invoke.115
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.177
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.177.cold.1
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.181
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.185
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.185.cold.1
+ ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.513
+ ___55-[SBSystemActionSceneElementProvider previewForReason:]_block_invoke_6
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1356
+ ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.481
+ ___58-[SBActivitySystemApertureElementObserver activityDidEnd:]_block_invoke_2
+ ___59-[SBActivityAmbientViewController setCompactOverlayHidden:]_block_invoke
+ ___59-[SBSAEjectStretchBehaviorProvider preferencesFromContext:]_block_invoke.15
+ ___59-[SBSAEjectStretchBehaviorProvider preferencesFromContext:]_block_invoke.32
+ ___59-[SBSAEjectStretchBehaviorProvider preferencesFromContext:]_block_invoke.cold.1
+ ___59-[SBSAEjectStretchBehaviorProvider preferencesFromContext:]_block_invoke.cold.2
+ ___59-[SBSAEjectStretchBehaviorProvider preferencesFromContext:]_block_invoke.cold.3
+ ___60-[SBAmbientPresentationController _fetchDefaultWidgetStacks]_block_invoke.155
+ ___60-[SBAmbientPresentationController _fetchDefaultWidgetStacks]_block_invoke.155.cold.1
+ ___60-[SBMainWorkspace _preflightTransitionRequest:forExecution:]_block_invoke.365
+ ___61-[SBReachabilityBackgroundView _updateWallpaperViewAnimated:]_block_invoke
+ ___61-[SBReachabilityBackgroundView _updateWallpaperViewAnimated:]_block_invoke_2
+ ___61-[SBReachabilityBackgroundView _updateWallpaperViewAnimated:]_block_invoke_3
+ ___61-[SBReachabilityBackgroundView _updateWallpaperViewAnimated:]_block_invoke_4
+ ___63-[SBSystemActionAnalyticsTracker _sendEventToPowerLog:payload:]_block_invoke
+ ___65-[SBAmbientPresentationController keybag:extendedStateDidChange:]_block_invoke
+ ___65-[SBFluidSwitcherViewController _reevaluateWindowManagementStyle]_block_invoke
+ ___65-[SBFluidSwitcherViewController _reevaluateWindowManagementStyle]_block_invoke.913
+ ___65-[SBFluidSwitcherViewController _reevaluateWindowManagementStyle]_block_invoke_2
+ ___65-[SBFluidSwitcherViewController _reevaluateWindowManagementStyle]_block_invoke_3
+ ___65-[SBFluidSwitcherViewController _reevaluateWindowManagementStyle]_block_invoke_4
+ ___65-[SBFluidSwitcherViewController _reevaluateWindowManagementStyle]_block_invoke_5
+ ___65-[SBFluidSwitcherViewController _reevaluateWindowManagementStyle]_block_invoke_6
+ ___65-[SBSystemActionSuppressionManager _queryPocketStateWithTimeout:]_block_invoke
+ ___65-[SBSystemActionSuppressionManager _queryPocketStateWithTimeout:]_block_invoke.cold.1
+ ___66-[SBFluidSwitcherViewController _createChamoisWindowingUIObserver]_block_invoke_3
+ ___69-[SBActivitySystemApertureElementObserver _cleanUpAlertPresentation:]_block_invoke_2
+ ___70-[SBAmbientProudLockViewController _dismissTransientProudLockAnimated]_block_invoke
+ ___70-[SBAmbientProudLockViewController _dismissTransientProudLockAnimated]_block_invoke.84
+ ___70-[SBAmbientTransientOverlayViewController _setProudLockAuthenticated:]_block_invoke
+ ___70-[SBIconController iconManager:configurationDataForDataSource:ofIcon:]_block_invoke
+ ___70-[SBSystemActionPreviewCoordinator _showPreviewForAction:withContext:]_block_invoke.56
+ ___74-[SBReachabilityBackgroundView _setupCornerContentsImageForWallpaperView:]_block_invoke
+ ___75-[SBSystemApertureViewController overrideContainerRenderingStyleAssertion:]_block_invoke
+ ___76-[SBAmbientPresentationController _updatePresentationPossibleForMountState:]_block_invoke
+ ___77-[SBReachabilityManager _updateReachabilityWindowForYOffset:mode:completion:]_block_invoke_5
+ ___79-[SBMainWorkspace _removeApplicationEntities:withDestructionIntent:completion:]_block_invoke.456
+ ___80-[SBActivityAmbientViewController _fullOverlayViewControllerForItem:completion:]_block_invoke.29
+ ___81-[SBAmbientTransientOverlayViewController _addProudLockViewControllerIfNecessary]_block_invoke
+ ___81-[SBAmbientTransientOverlayViewController _addProudLockViewControllerIfNecessary]_block_invoke_2
+ ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.70
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1214
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1216
+ ___91-[SBLinkSystemActionExecutor _beginInteractiveExecutionWithContext:executionHandler:error:]_block_invoke
+ ___92-[SBBlockSystemActionExecutor _beginInteractiveExecutionWithContext:executionHandler:error:]_block_invoke
+ ___92-[SBBlockSystemActionExecutor _beginInteractiveExecutionWithContext:executionHandler:error:]_block_invoke_2
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.598
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.616
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.631
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.633
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.641
+ ___97-[SBSystemApertureViewController(Private) _updateElementOrientationTo:withTransitionCoordinator:]_block_invoke
+ ___97-[SBSystemApertureViewController(Private) _updateElementOrientationTo:withTransitionCoordinator:]_block_invoke_2
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1339
+ ___SBLogSystemActionCoaching_block_invoke
+ ___SBLogSystemApertureOrientation_block_invoke
+ ___block_descriptor_40_e8_32w_e15_"UIAction"8?0lw32l8
+ ___block_descriptor_40_e8_32w_e82_"PLPillContentItem"20?0"<BNTemplateTextProviding><BNTemplateViewProviding>"8B16lw32l8
+ ___block_descriptor_41_e8_32w_e15_"UIAction"8?0lw32l8
+ ___block_descriptor_48_e73_{SBSwitcherWallpaperGradientAttributes=dd}24?0"SBChainableModifier"8Q16l
+ ___block_descriptor_48_e8_32s40s_e25_v16?0?<v?B"NSError">8ls32l8s40l8
+ ___block_descriptor_48_e8_32w_e42_B16?0"SBMainWorkspaceTransitionRequest"8lw32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e8_v16?0q8ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40w_e40_v24?0"<SAInvalidatable>"8"NSString"16lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e55_v16?0"SBActivityAmbientCompactOverlayViewController"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e44_v16?0"BSTransaction<SBStartupTransition>"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.1111
+ ___block_literal_global.1158
+ ___block_literal_global.1203
+ ___block_literal_global.1221
+ ___block_literal_global.1230
+ ___block_literal_global.1232
+ ___block_literal_global.1234
+ ___block_literal_global.1236
+ ___block_literal_global.1252
+ ___block_literal_global.1365
+ ___block_literal_global.1389
+ ___block_literal_global.1398
+ ___block_literal_global.1415
+ ___block_literal_global.174
+ ___block_literal_global.179
+ ___block_literal_global.272
+ ___block_literal_global.328
+ ___block_literal_global.331
+ ___block_literal_global.424
+ ___block_literal_global.427
+ ___block_literal_global.432
+ ___block_literal_global.455
+ ___block_literal_global.459
+ ___block_literal_global.469
+ ___block_literal_global.473
+ ___block_literal_global.489
+ ___block_literal_global.515
+ ___block_literal_global.601
+ ___block_literal_global.634
+ ___block_literal_global.640
+ ___block_literal_global.652
+ ___block_literal_global.655
+ ___block_literal_global.683
+ ___block_literal_global.688
+ ___block_literal_global.694
+ ___block_literal_global.700
+ ___block_literal_global.706
+ ___block_literal_global.713
+ ___block_literal_global.724
+ ___block_literal_global.728
+ ___block_literal_global.744
+ ___block_literal_global.751
+ ___block_literal_global.758
+ ___block_literal_global.873
+ __unnamed_array_storage.100
+ __unnamed_array_storage.101
+ __unnamed_array_storage.110
+ __unnamed_array_storage.114
+ __unnamed_array_storage.115
+ __unnamed_array_storage.131
+ __unnamed_array_storage.135
+ __unnamed_array_storage.136
+ __unnamed_array_storage.1362
+ __unnamed_array_storage.143
+ __unnamed_array_storage.147
+ __unnamed_array_storage.148
+ __unnamed_array_storage.1502
+ __unnamed_array_storage.1511
+ __unnamed_array_storage.161
+ __unnamed_array_storage.172
+ __unnamed_array_storage.337
+ __unnamed_array_storage.342
+ __unnamed_array_storage.345
+ __unnamed_array_storage.353
+ __unnamed_array_storage.356
+ __unnamed_array_storage.359
+ __unnamed_array_storage.362
+ __unnamed_array_storage.365
+ __unnamed_array_storage.368
+ _objc_msgSend$DSLPublisher
+ _objc_msgSend$FocusedEvaluationMode
+ _objc_msgSend$Health
+ _objc_msgSend$_activatedElementItemForBundleIdentifier:
+ _objc_msgSend$_addProudLockViewControllerIfNecessary
+ _objc_msgSend$_ambientCoreAnalyticsActiveFaceDescription:screenOffDuration:sessionIdString:
+ _objc_msgSend$_ambientPowerLogAmbientMotionToWakeEnabled:
+ _objc_msgSend$_backgroundTintColorForUserInterfaceStyle:
+ _objc_msgSend$_beginInteractiveExecutionWithContext:executionHandler:error:
+ _objc_msgSend$_canSendVolumeButtonEventsToScene:withConfiguration:activeVolumeCategoryName:isAudioSessionPlaying:
+ _objc_msgSend$_dismissAllOtherAmbientTransientOverlays
+ _objc_msgSend$_displayTransientLockElementIfNecessaryForKeyBagState:
+ _objc_msgSend$_displaysVolumeForCategory:
+ _objc_msgSend$_effectiveAlwaysOnMode
+ _objc_msgSend$_effectiveOverrideRenderingStyle
+ _objc_msgSend$_handleExecutionBlockFinishedWithResult:
+ _objc_msgSend$_handleHitTestingUpdatesWithContext:
+ _objc_msgSend$_heightForCardInSwitcherWithScaleFactor:
+ _objc_msgSend$_invalidateJindoReason
+ _objc_msgSend$_invalidateTransientOverlayWindowTraitsArbiterParticipantIfNeeded
+ _objc_msgSend$_invertColorsIsEnabled
+ _objc_msgSend$_isCoverSheetPresentedByUserGesture
+ _objc_msgSend$_isHealthFocusedEvaluationModeActive
+ _objc_msgSend$_isMotionToWakePermitted
+ _objc_msgSend$_isNightModeSettingMandatory
+ _objc_msgSend$_isNightModeUserSettingEffectivelyEnabled
+ _objc_msgSend$_logSignificantTimeChanged
+ _objc_msgSend$_newWallpaperViewForVariant:
+ _objc_msgSend$_notifyInteractionWithPossiblyHungApplicationSceneEntities:withInteractionType:
+ _objc_msgSend$_overshootOutsetsForTransitionPhase:baseOutsets:elementContext:
+ _objc_msgSend$_prepareBlurForWrapperView
+ _objc_msgSend$_promote:gestureRecognizer:toSystemGestureWithManager:type:
+ _objc_msgSend$_queryPocketStateWithTimeout:
+ _objc_msgSend$_reevaluateWindowManagementStyle
+ _objc_msgSend$_removeProudLockViewController
+ _objc_msgSend$_requiresAuthenticationAtLeastOnceSinceBootBeforeExecution
+ _objc_msgSend$_resetTransientLockSuppressionFlag
+ _objc_msgSend$_sendEventToPowerLog:payload:
+ _objc_msgSend$_setCoverSheetPresentedByUserGesture:
+ _objc_msgSend$_setHealthFocusedEvaluationModeActive:
+ _objc_msgSend$_setIdleTimerAllowedForAssertions:forSleepFocus:
+ _objc_msgSend$_setIdleTimerAllowedForAssertionsForSleepFocus:
+ _objc_msgSend$_setProudLockAuthenticated:
+ _objc_msgSend$_setupColorInvertObservation
+ _objc_msgSend$_setupCornerContentsImageForWallpaperView:
+ _objc_msgSend$_shouldSetDefaultBackground
+ _objc_msgSend$_shouldSuppressForSleep
+ _objc_msgSend$_startTimerIfNecessary:context:
+ _objc_msgSend$_updateActiveFaceScreenOffForBacklightState:forConfiguration:sessionIdString:
+ _objc_msgSend$_updateAmbientMountState:withReason:
+ _objc_msgSend$_updateAmbientTriggerState:analogousTriggerEvents:withReason:
+ _objc_msgSend$_updateColorMatrixAlpha:
+ _objc_msgSend$_updateColorMatrixFilters
+ _objc_msgSend$_updateElementOrientationTo:withTransitionCoordinator:
+ _objc_msgSend$_updateMedusaCapabilitySendingNotification:
+ _objc_msgSend$_updatePresentationPossibleForMountState:
+ _objc_msgSend$_updateSleepSuppression
+ _objc_msgSend$_updateWallpaperViewAnimated:
+ _objc_msgSend$_updateWallpaperViewFilters
+ _objc_msgSend$acceptanceSideBounceFinishingDelay
+ _objc_msgSend$acceptanceUpBounceFinishingDelay
+ _objc_msgSend$activeModeIdentifier
+ _objc_msgSend$allowAmbientIdleTimerForSleepFocus
+ _objc_msgSend$alwaysOnMode
+ _objc_msgSend$analyticsData
+ _objc_msgSend$animatedLayerProperties
+ _objc_msgSend$attribute
+ _objc_msgSend$bundleRecordWithBundleIdentifier:allowPlaceholder:error:
+ _objc_msgSend$canChangeVolumeForActiveCategory:isAudioSessionPlaying:
+ _objc_msgSend$contentData
+ _objc_msgSend$defaultSymbolConfiguration
+ _objc_msgSend$displayTransientProudLock
+ _objc_msgSend$ejectionYUpOffset
+ _objc_msgSend$executeWithContext:executionHandler:completion:
+ _objc_msgSend$executionGeneration
+ _objc_msgSend$hostBundleRequiresValidation
+ _objc_msgSend$hostOrientationDidChangeTo:withPreviousOrientation:context:
+ _objc_msgSend$hungApplicationInteractionObserver
+ _objc_msgSend$initWithAuthenticationInformationProvider:
+ _objc_msgSend$initWithBiometricResource:authenticationController:
+ _objc_msgSend$initWithTransitionID:appLayout:layoutRole:
+ _objc_msgSend$isDepthEffectDisabled
+ _objc_msgSend$isForSleepFocus
+ _objc_msgSend$isForegroundActive
+ _objc_msgSend$isIconVisibleForBundleIdentifier:
+ _objc_msgSend$jindoInertDisableOffset
+ _objc_msgSend$jindoTintColorMatrixSettings
+ _objc_msgSend$logTelemetryForAmbientPresented:withBacklightState:screenOffWithConfiguration:
+ _objc_msgSend$logTelemetryForMotionToWakeEnabled:
+ _objc_msgSend$observeRemovedApplicationSceneEntity:
+ _objc_msgSend$overrideContainerRenderingStyleAssertion:
+ _objc_msgSend$overrideProudLockIconViewLayoutWithSize:offset:extent:
+ _objc_msgSend$pr_loadConfiguredPropertiesWithError:
+ _objc_msgSend$proudLockAssetSize
+ _objc_msgSend$reinitializeStatusBar
+ _objc_msgSend$requiresAuthenticationAtLeastOnceSinceBootBeforeExecution
+ _objc_msgSend$scrollAccessoryView
+ _objc_msgSend$setAcceptanceSideBounceFinishingDelay:
+ _objc_msgSend$setAcceptanceUpBounceFinishingDelay:
+ _objc_msgSend$setAudioCategoryZStackPolicyAssistant:
+ _objc_msgSend$setAuthenticated:completion:
+ _objc_msgSend$setCompactOverlayHidden:
+ _objc_msgSend$setDepthEffectDisabled:
+ _objc_msgSend$setEjectionYUpOffset:
+ _objc_msgSend$setFloatingLayerFullscreen:
+ _objc_msgSend$setJindoInertDisableOffset:
+ _objc_msgSend$setJindoTintColorMatrixSettings:
+ _objc_msgSend$setSuppressForSleep:
+ _objc_msgSend$shouldSuppressAlertContentOnLockScreen
+ _objc_msgSend$systemActionCoachingController:canPresentCoachingForAction:
+ _wakeGestureManager:didUpdateWakeGestureEvent:.secondsToTicksScaleFactor
- -[SBAbstractSystemActionExecutor _beginInteractiveExecutionWithContext:error:]
- -[SBAbstractSystemActionExecutor executeWithContext:completion:]
- -[SBAbstractSystemActionExecutor executeWithContext:completion:].cold.1
- -[SBAbstractSystemActionExecutor executeWithContext:completion:].cold.2
- -[SBActivityAmbientViewController _setCompactOverlayHidden:]
- -[SBActivityAmbientViewController swapPrimaryActivityWithItem:]
- -[SBActivityAmbientViewController swapSecondaryActivityWithItem:]
- -[SBActivityBannerViewController _shouldSetBlackBackground]
- -[SBActivitySystemApertureElementObserver _registeredElementForBundleIdentifier:]
- -[SBAmbientIdleTimerController isSuppressionMonitoringActive]
- -[SBAmbientIdleTimerController setSuppressionMonitoringActive:]
- -[SBAmbientPresentationController _updateAmbientPresentationState:analogousTriggerEvents:withReason:]
- -[SBAmbientPresentationController _updatePresentationPossibleForPresentationState:]
- -[SBAmbientPresentationController ambientPresentationManager:didUpdatePresentationState:analogousTriggerEvents:]
- -[SBAmbientTransientOverlayViewController _canSwapActivityItem:withOtherItem:]
- -[SBAmbientTransientOverlayViewController _canSwapPrimaryActivityWithItem:]
- -[SBAmbientTransientOverlayViewController _canSwapSecondaryActivityWithItem:]
- -[SBAppSwitcherContinuousExposeSwitcherModifier _heightForCardInSwitcher]
- -[SBBlockSystemAction analyticsIdentifier]
- -[SBBlockSystemActionExecutor _beginInteractiveExecutionWithContext:error:]
- -[SBCoverSheetSecureAppEnvironmentViewController _updateSystemApertureZStackPolicyAssistant]
- -[SBFluidSwitcherViewController _windowingStyleDefaultChangeHandler]
- -[SBFluidSwitcherViewController isMedusaEnabled]
- -[SBFocusActivityManager createFocusElementForActivityDescription:enabled:]
- -[SBFullScreenToHomePIPSwitcherModifier completesWhenChildrenComplete]
- -[SBFullScreenToHomePIPSwitcherModifier initWithTransitionID:zoomModifier:appLayout:layoutRole:]
- -[SBHungApplicationTransitionObserver _lockStateDidChange:]
- -[SBHungApplicationTransitionObserver _notifyUserSwitchedAwayFromApplicationSceneEntities:withTransitionType:]
- -[SBHungApplicationTransitionObserver _notifyUserSwitchedAwayFromApplicationSceneEntities:withTransitionType:].cold.1
- -[SBHungApplicationTransitionObserver _transitionContextRepresentsActivatingAppFromAppSwitcher:]
- -[SBHungApplicationTransitionObserver _transitionContextRepresentsActivatingDynamicIslandApp:]
- -[SBHungApplicationTransitionObserver _transitionContextRepresentsActivatingHomeScreen:]
- -[SBHungApplicationTransitionObserver _transitionContextRepresentsArcSwipingToPreviousApp:]
- -[SBHungApplicationTransitionObserver _transitionContextRepresentsTappingBreadcrumbToPreviousApp:]
- -[SBHungApplicationTransitionObserver activate]
- -[SBHungApplicationTransitionObserver activate].cold.1
- -[SBHungApplicationTransitionObserver observeBackgroundingApplicationSceneEntities:withTransitionContext:]
- -[SBHungApplicationTransitionObserver previousLockState]
- -[SBHungApplicationTransitionObserver setPreviousLockState:]
- -[SBLiftToWakeController wakeGestureManager:didUpdateWakeGesture:orientation:detectedAt:]
- -[SBLinkSystemActionExecutor _beginInteractiveExecutionWithContext:error:]
- -[SBMainWorkspace _updateMedusaEnablementAndNotify:]
- -[SBMainWorkspace isMedusaEnabled]
- -[SBMedusaDecoratedDeviceApplicationSceneViewController _medusaEnabledStateChanged:]
- -[SBPhysicalButtonSceneOverrideManager _canSendVolumeButtonEventsToScene:withConfiguration:activeVolumeCategoryName:]
- -[SBReachabilityBackgroundView _newWallpaperEffectViewForVariant:]
- -[SBReachabilityBackgroundView _setupCornerContentsImageForWallpaperEffectView:]
- -[SBReachabilityBackgroundView _updateWallpaperEffectViewAnimated:]
- -[SBRecentAppLayoutsPersister _loadRecents].cold.1
- -[SBRecentAppLayoutsPersister _queue_writeCompressedProtobufRepresentationToDisk:].cold.1
- -[SBRingerHardwareButtonSettings setViewObstructionEligibility:]
- -[SBRingerHardwareButtonSettings viewObstructionEligibility]
- -[SBSAAcceptanceBounceBehaviorProvider milestoneForPhase:]
- -[SBSAAcceptanceBounceBehaviorProvider milestoneForPhaseRequiresAnimationFinished:]
- -[SBSAEjectStretchBehaviorProvider _startTimerIfNecessary:]
- -[SBSASettlingBehaviorProvider _overshootOutsetsForTransitionPhase:baseOutsets:]
- -[SBSystemAction analyticsIdentifier]
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:]
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.1
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.2
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.3
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.4
- -[SBSystemActionCoachingController initWithHUDController:ringerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.5
- -[SBSystemActionCoachingHUDViewController initWithRingerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:]
- -[SBSystemActionCoachingHUDViewController initWithRingerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.1
- -[SBSystemActionCoachingHUDViewController initWithRingerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.2
- -[SBSystemActionCoachingHUDViewController initWithRingerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.3
- -[SBSystemActionCoachingHUDViewController initWithRingerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:].cold.4
- -[SBSystemActionControl initWithDataSource:previewCoordinator:coachingController:soundController:]
- -[SBSystemActionControl initWithDataSource:previewCoordinator:coachingController:soundController:].cold.1
- -[SBSystemActionControl initWithDataSource:previewCoordinator:coachingController:soundController:].cold.2
- -[SBSystemActionControl initWithDataSource:previewCoordinator:coachingController:soundController:].cold.3
- -[SBSystemActionControl initWithDataSource:previewCoordinator:coachingController:soundController:].cold.4
- -[SBSystemActionControl selectedActionAnalyticsIdentifier]
- -[SBSystemActionSceneElementProvider _configurePlaceholderContentProviders].cold.2
- -[SBSystemActionSuppressionManager _queryPocketState]
- -[SBSystemActionSuppressionManager setViewObstructionEligibility:]
- -[SBSystemActionSuppressionManager viewObstructionEligibility]
- -[SBSystemApertureController _applyOrientation:withPreviousOrientation:animationSettings:]
- -[SBSystemApertureController activeElementInterfaceOrientationForSystemApertureElementOrientationObserver:]
- -[SBSystemApertureController overrideRenderingStyle]
- -[SBSystemApertureController setOverrideRenderingStyle:]
- -[SBSystemApertureViewController _updateActiveElementInterfaceOrientation]
- -[SBSystemApertureViewController overrideRenderingStyle]
- -[SBSystemApertureViewController setOverrideRenderingStyle:]
- -[SBSystemApertureViewController(Private) elementOrientationAuthority]
- -[SBSystemApertureViewController(Private) elementOrientationDidChangeWithTransitionCoordinator:]
- -[SBSystemApertureViewController(Private) setElementOrientationAuthority:]
- -[SBTopAffordanceViewController _isChamoisWindowingUIEnabled]
- -[SBVolumeControl managesVolumeForCategory:]
- -[SpringBoard hungApplicationTransitionObserver]
- GCC_except_table141
- GCC_except_table167
- GCC_except_table176
- GCC_except_table191
- GCC_except_table215
- GCC_except_table311
- GCC_except_table312
- GCC_except_table326
- GCC_except_table407
- GCC_except_table547
- GCC_except_table558
- GCC_except_table741
- GCC_except_table752
- _OBJC_CLASS_$_SBHungApplicationTransitionObserver
- _OBJC_CLASS_$_SBUISystemApertureAspectFittingContentProvider
- _OBJC_IVAR_$_SBAmbientIdleTimerController._suppressionMonitoringActive
- _OBJC_IVAR_$_SBAmbientTransientOverlayViewController._mobileKeyBag
- _OBJC_IVAR_$_SBFullScreenToHomePIPSwitcherModifier._zoomModifier
- _OBJC_IVAR_$_SBHungApplicationTransitionObserver._previousLockState
- _OBJC_IVAR_$_SBMainWorkspace._medusaEnabled
- _OBJC_IVAR_$_SBReachabilityBackgroundView._bottomWallpaperEffectView
- _OBJC_IVAR_$_SBReachabilityBackgroundView._topWallpaperEffectView
- _OBJC_IVAR_$_SBRingerHardwareButtonSettings._viewObstructionEligibility
- _OBJC_IVAR_$_SBSystemApertureViewController._elementOrientationAuthority
- _OBJC_IVAR_$_SBSystemApertureViewController._overrideRenderingStyle
- _OBJC_IVAR_$_SpringBoard._hungApplicationTransitionObserver
- _OBJC_METACLASS_$_SBHungApplicationTransitionObserver
- _SBMedusaEnabledStateChangedNotification
- _SBSwitcherGradientWallpaperAttributesEqual
- _SBSwitcherGradientWallpaperAttributesMakeEmpty
- _SBSystemActionSimplePreviewImageSymbolConfiguration
- __OBJC_$_INSTANCE_METHODS_SBHungApplicationTransitionObserver
- __OBJC_$_INSTANCE_VARIABLES_SBHungApplicationTransitionObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FCUISystemApertureElementProviding
- __OBJC_CLASS_RO_$_SBHungApplicationTransitionObserver
- __OBJC_METACLASS_RO_$_SBHungApplicationTransitionObserver
- ___101-[SBActivityBannerObserver _postBannerWithActivityIdentifier:payloadIdentifier:prominent:completion:]_block_invoke.25
- ___111-[SBCoverSheetPresentationManager _setTransitionProgress:animated:gestureActive:coverSheetProgress:completion:]_block_invoke.195
- ___111-[SBCoverSheetPresentationManager _setTransitionProgress:animated:gestureActive:coverSheetProgress:completion:]_block_invoke.196
- ___111-[SBCoverSheetPresentationManager _setTransitionProgress:animated:gestureActive:coverSheetProgress:completion:]_block_invoke.198
- ___170-[SBFluidSwitcherViewController initWithSwitcherController:rootModifier:liveContentOverlayCoordinator:delegate:dataSource:shouldObserveChamoisWindowingChanges:debugName:]_block_invoke.106
- ___39-[SBVolumeControl changeVolumeByDelta:]_block_invoke.147
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.864
- ___47-[SBBannerAuthority _configureSinksIfNecessary]_block_invoke.20
- ___47-[SBBannerAuthority _configureSinksIfNecessary]_block_invoke.20.cold.1
- ___47-[SBBannerAuthority _configureSinksIfNecessary]_block_invoke.24
- ___48-[SBActionButtonMetric handleEvent:withContext:]_block_invoke_2
- ___48-[SBActionButtonMetric handleEvent:withContext:]_block_invoke_3
- ___48-[SBActionButtonMetric handleEvent:withContext:]_block_invoke_4
- ___48-[SBMainWorkspace _initializeAndObserveDefaults]_block_invoke_4
- ___48-[SBReachabilityManager canActivateReachability]_block_invoke.100
- ___48-[SBReachabilityManager canActivateReachability]_block_invoke.114
- ___48-[SBReachabilityManager canActivateReachability]_block_invoke.121
- ___52-[SBMainWorkspace _updateMedusaEnablementAndNotify:]_block_invoke
- ___52-[SBMainWorkspace _updateMedusaEnablementAndNotify:]_block_invoke_2
- ___53-[SBSystemActionSuppressionManager _queryPocketState]_block_invoke
- ___53-[SBSystemActionSuppressionManager _queryPocketState]_block_invoke.cold.1
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.174
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.174.cold.1
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.178
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.179
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.179.cold.1
- ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.514
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1357
- ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.487
- ___58+[SBSystemActionCoachingSettings settingsControllerModule]_block_invoke
- ___58+[SBSystemActionCoachingSettings settingsControllerModule]_block_invoke_2
- ___59-[SBSAEjectStretchBehaviorProvider preferencesFromContext:]_block_invoke_2
- ___59-[SBSAEjectStretchBehaviorProvider preferencesFromContext:]_block_invoke_3
- ___60-[SBActivityAmbientViewController _setCompactOverlayHidden:]_block_invoke
- ___60-[SBAmbientPresentationController _fetchDefaultWidgetStacks]_block_invoke.150
- ___60-[SBAmbientPresentationController _fetchDefaultWidgetStacks]_block_invoke.150.cold.1
- ___60-[SBMainWorkspace _preflightTransitionRequest:forExecution:]_block_invoke.366
- ___63-[SBActivityAmbientViewController swapPrimaryActivityWithItem:]_block_invoke
- ___65-[SBActivityAmbientViewController swapSecondaryActivityWithItem:]_block_invoke
- ___66-[SBFluidSwitcherViewController _createChamoisWindowingUIObserver]_block_invoke.153
- ___67-[SBReachabilityBackgroundView _updateWallpaperEffectViewAnimated:]_block_invoke
- ___67-[SBReachabilityBackgroundView _updateWallpaperEffectViewAnimated:]_block_invoke_2
- ___67-[SBReachabilityBackgroundView _updateWallpaperEffectViewAnimated:]_block_invoke_3
- ___68-[SBFluidSwitcherViewController _windowingStyleDefaultChangeHandler]_block_invoke
- ___68-[SBFluidSwitcherViewController _windowingStyleDefaultChangeHandler]_block_invoke_10
- ___68-[SBFluidSwitcherViewController _windowingStyleDefaultChangeHandler]_block_invoke_2
- ___68-[SBFluidSwitcherViewController _windowingStyleDefaultChangeHandler]_block_invoke_3
- ___68-[SBFluidSwitcherViewController _windowingStyleDefaultChangeHandler]_block_invoke_4
- ___68-[SBFluidSwitcherViewController _windowingStyleDefaultChangeHandler]_block_invoke_5
- ___68-[SBFluidSwitcherViewController _windowingStyleDefaultChangeHandler]_block_invoke_6
- ___68-[SBFluidSwitcherViewController _windowingStyleDefaultChangeHandler]_block_invoke_7
- ___68-[SBFluidSwitcherViewController _windowingStyleDefaultChangeHandler]_block_invoke_8
- ___68-[SBFluidSwitcherViewController _windowingStyleDefaultChangeHandler]_block_invoke_9
- ___70-[SBSystemActionPreviewCoordinator _showPreviewForAction:withContext:]_block_invoke.53
- ___75-[SBBlockSystemActionExecutor _beginInteractiveExecutionWithContext:error:]_block_invoke
- ___79-[SBMainWorkspace _removeApplicationEntities:withDestructionIntent:completion:]_block_invoke.462
- ___80-[SBActivityAmbientViewController _fullOverlayViewControllerForItem:completion:]_block_invoke.28
- ___80-[SBReachabilityBackgroundView _setupCornerContentsImageForWallpaperEffectView:]_block_invoke
- ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.67
- ___83-[SBAmbientPresentationController _updatePresentationPossibleForPresentationState:]_block_invoke
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1215
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1217
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.604
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.622
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.637
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.639
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.647
- ___96-[SBSystemApertureViewController(Private) elementOrientationDidChangeWithTransitionCoordinator:]_block_invoke
- ___96-[SBSystemApertureViewController(Private) elementOrientationDidChangeWithTransitionCoordinator:]_block_invoke_2
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1340
- ___block_descriptor_32_e27_B16?0"SBWorkspaceEntity"8l
- ___block_descriptor_32_e44_"SBWorkspaceEntity"16?0"SBLayoutElement"8l
- ___block_descriptor_40_e8_32s_e82_"PLPillContentItem"20?0"<BNTemplateTextProviding><BNTemplateViewProviding>"8B16ls32l8
- ___block_descriptor_40_e8_32w_e42_B16?0"SBMainWorkspaceTransitionRequest"8lw32l8
- ___block_descriptor_41_e8_32s_e15_"UIAction"8?0ls32l8
- ___block_descriptor_41_e8_32s_e18_v16?0"UIAction"8ls32l8
- ___block_descriptor_48_e73_{SBSwitcherGradientWallpaperAttributes=dd}24?0"SBChainableModifier"8Q16l
- ___block_descriptor_48_e8_32s40bs_e11_v16?0B8B12ls40l8s32l8
- ___block_descriptor_72_e8_32s40s48s56bs_e55_v16?0"SBActivityAmbientCompactOverlayViewController"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e44_v16?0"BSTransaction<SBStartupTransition>"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.102
- ___block_literal_global.1112
- ___block_literal_global.1163
- ___block_literal_global.1208
- ___block_literal_global.1222
- ___block_literal_global.1231
- ___block_literal_global.1233
- ___block_literal_global.1235
- ___block_literal_global.1237
- ___block_literal_global.1253
- ___block_literal_global.1366
- ___block_literal_global.1390
- ___block_literal_global.1399
- ___block_literal_global.1416
- ___block_literal_global.144
- ___block_literal_global.168
- ___block_literal_global.278
- ___block_literal_global.327
- ___block_literal_global.372
- ___block_literal_global.401
- ___block_literal_global.403
- ___block_literal_global.411
- ___block_literal_global.425
- ___block_literal_global.428
- ___block_literal_global.433
- ___block_literal_global.461
- ___block_literal_global.466
- ___block_literal_global.470
- ___block_literal_global.490
- ___block_literal_global.511
- ___block_literal_global.600
- ___block_literal_global.630
- ___block_literal_global.638
- ___block_literal_global.650
- ___block_literal_global.653
- ___block_literal_global.681
- ___block_literal_global.686
- ___block_literal_global.690
- ___block_literal_global.696
- ___block_literal_global.702
- ___block_literal_global.708
- ___block_literal_global.714
- ___block_literal_global.720
- ___block_literal_global.726
- ___block_literal_global.761
- ___block_literal_global.763
- ___block_literal_global.871
- ___block_literal_global.907
- ___block_literal_global.913
- ___block_literal_global.916
- ___block_literal_global.918
- ___block_literal_global.921
- ___block_literal_global.926
- __unnamed_array_storage.108
- __unnamed_array_storage.128
- __unnamed_array_storage.133
- __unnamed_array_storage.1363
- __unnamed_array_storage.140
- __unnamed_array_storage.145
- __unnamed_array_storage.1503
- __unnamed_array_storage.1512
- __unnamed_array_storage.153
- __unnamed_array_storage.158
- __unnamed_array_storage.165
- __unnamed_array_storage.169
- __unnamed_array_storage.336
- __unnamed_array_storage.341
- __unnamed_array_storage.344
- __unnamed_array_storage.349
- __unnamed_array_storage.352
- __unnamed_array_storage.355
- __unnamed_array_storage.358
- __unnamed_array_storage.361
- __unnamed_array_storage.364
- __unnamed_array_storage.367
- __unnamed_array_storage.97
- _objc_msgSend$_applyOrientation:withPreviousOrientation:animationSettings:
- _objc_msgSend$_beginInteractiveExecutionWithContext:error:
- _objc_msgSend$_canSendVolumeButtonEventsToScene:withConfiguration:activeVolumeCategoryName:
- _objc_msgSend$_canSwapActivityItem:withOtherItem:
- _objc_msgSend$_canSwapPrimaryActivityWithItem:
- _objc_msgSend$_canSwapSecondaryActivityWithItem:
- _objc_msgSend$_heightForCardInSwitcher
- _objc_msgSend$_isShowingFullActivityOverlay
- _objc_msgSend$_newWallpaperEffectViewForVariant:
- _objc_msgSend$_notifyUserSwitchedAwayFromApplicationSceneEntities:withTransitionType:
- _objc_msgSend$_overshootOutsetsForTransitionPhase:baseOutsets:
- _objc_msgSend$_queryPocketState
- _objc_msgSend$_registeredElementForBundleIdentifier:
- _objc_msgSend$_setCompactOverlayHidden:
- _objc_msgSend$_setupCornerContentsImageForWallpaperEffectView:
- _objc_msgSend$_shouldSetBlackBackground
- _objc_msgSend$_updateActiveElementInterfaceOrientation
- _objc_msgSend$_updateAmbientPresentationState:analogousTriggerEvents:withReason:
- _objc_msgSend$_updateMedusaEnablementAndNotify:
- _objc_msgSend$_updatePresentationPossibleForPresentationState:
- _objc_msgSend$_updateSystemApertureZStackPolicyAssistant
- _objc_msgSend$_updateWallpaperEffectViewAnimated:
- _objc_msgSend$_windowingStyleDefaultChangeHandler
- _objc_msgSend$alwaysOnEnabled
- _objc_msgSend$appIconAverageColor
- _objc_msgSend$createPersistentFocusElementForActivityDescription:enabled:
- _objc_msgSend$executeWithContext:completion:
- _objc_msgSend$hungApplicationTransitionObserver
- _objc_msgSend$initWithTransitionID:zoomModifier:appLayout:layoutRole:
- _objc_msgSend$insertSubview:above:
- _objc_msgSend$insertSubview:below:
- _objc_msgSend$isMedusaEnabled
- _objc_msgSend$managesVolumeForCategory:
- _objc_msgSend$setClipsSubviews:
- _objc_msgSend$setExplicitIntrinsicSize:
- _objc_msgSend$setSuppressionMonitoringActive:
- _objc_msgSend$swapPrimaryActivityWithItem:
- _objc_msgSend$swapSecondaryActivityWithItem:
- _objc_msgSend$wakeGestureManager:didUpdateWakeGesture:orientation:
CStrings:
+ "\x01\x13\x15\x1b\x13\x12\x122"
+ "\x01\x16\x11"
+ "\x0153"
+ "\x018\x13\x13"
+ "\x02\xf0\xf0\xf0\xa1"
+ "\x06\x13"
+ "\a$\x19"
+ "\x0f\x06"
+ "!\x17%"
+ "!UIInterfaceOrientationIsLandscape([associatedElementContext interfaceOrientation])"
+ "%{public}@ - Ignoring siri presentation request because device is locked out by liquid detection critical UI"
+ "%{public}@ - Ignoring siri presentation request because device is locked out by thermal trap"
+ "%{public}@ Couldn't derive app layout from Protobuf representation: %{public}@"
+ "%{public}@ Error compressing data: %@"
+ "%{public}@ Error decompressing recents: %{public}@"
+ "%{public}@ Error reading recents from %{public}@: %{public}@"
+ "%{public}@ Error removing faulty switcher model from %{public}@: %{public}@"
+ "%{public}@ Error writing recents to %@: %@"
+ "%{public}@ Removed faulty switcher model from %{public}@"
+ "%{public}@ Using empty switcher model to recover from error with persisted switcher model"
+ "%{public}@: fetched config data for key: %{public}@, result: %{public}@ bytes with keybag state: %{public}@."
+ "(%{public}@) Delegate denied presentation of coaching for action %{public}@"
+ "(%{public}@) Invalidating flashlight-unavailable alert for reason: '%{public}@'"
+ "(%{public}@) Suppressing action: %{public}@, suppression status: %{public}@"
+ "(%{public}@) requesting device authentication for executor '%{public}@'"
+ "(%{public}@) subscribing to VO"
+ "(%{public}@) unsubscribing from VO"
+ "@\"<BSInvalidatable>\"40@0:8@\"SBSystemActionInteractionContext\"16@?<v@?@?<v@?B@\"NSError\">>24@?<v@?@\"<SBSystemActionExecuting>\"@\"NSError\">32"
+ "@\"<SBSystemActionCoachingControllerDelegate>\""
+ "@\"SBAmbientProudLockViewController\""
+ "@\"SBFMobileKeyBagState\""
+ "@\"SBHungApplicationInteractionObserver\""
+ "@\"SBPropertyAnimatingView\""
+ "@\"SBUIProudLockContainerViewController\""
+ "@\"UIView\"40@0:8@\"SBHIconManager\"16q24@\"SBIconView\"32"
+ "@\"_SBAdaptiveColorMatrixView\""
+ "@40@0:8@16@?24@?32"
+ "@40@0:8@16@?24o^@32"
+ "AcceptanceBounceBehaviorProvider triggered block upon removal"
+ "ActionButtonUsePocketStateForSuppression"
+ "Ambient presentation allowed = %{BOOL}d [ enabled:%{BOOL}d ; lockedButNotBlocked:%{BOOL}d ; ignoreLockState:%{BOOL}d ; unlockedSinceBoot:%{BOOL}d ; carplay:%{BOOL}d ; screenOccludingAccessory:%{BOOL}d ; hostingApp:%{BOOL}d ; isInSetupMode:%{BOOL}d ; isOutOfPocket:%{BOOL}d ; isViewObstructed:%{BOOL}d ; listInteraction:%{BOOL}d ; pullDownCoverSheet:%{BOOL}d ; spotlight:%{BOOL}d ; todayView:%{BOOL}d ]"
+ "Ambient supression state updated. wasAmbientSuppressed = %{BOOL}u  isAmbientSuppressed = %{BOOL}u  [ _idleTimerAllowedForAssertions = %{BOOL}u _idleTimerAllowedForAssertionsForSleepFocus = %{BOOL}u _suppressForSleep = %{BOOL}u _idleTimerAllowedForSuppression = %{BOOL}u ]"
+ "AmbientModeMotionToWake"
+ "B32@0:8@\"AMUIAmbientViewController\"16@\"NSString\"24"
+ "B32@0:8@\"SBSystemActionCoachingController\"16@\"SBSystemAction\"24"
+ "Calling HTUserSwitchedAwayFromApp with pid %d, reason %@"
+ "Color matrix over content"
+ "Config data is accessible after first unlock."
+ "Configuring health focused evaluation mode sink"
+ "DSLPublisher"
+ "Error loading poster configured properties: %@"
+ "Failed to compute animation settings"
+ "FindMyPhone"
+ "FocusedEvaluationMode"
+ "Found untracked transient overlay instance %@. Dismissing."
+ "Health"
+ "Health focused evaluation mode is %{public}@"
+ "Health focused evaluation mode sink completion was unexpectely invoked (error: %{public}@)"
+ "Inert disable animation offset"
+ "InteractivePresentation-%@"
+ "Jindo"
+ "Miscellaneous"
+ "No longer completely suppressing System Aperture"
+ "Not applying orientation update to SBSystemApertureViewController because new orientation:(%@) matches current orientation"
+ "NotSleep"
+ "Observed backgrounding application scene(s) with interaction type %@"
+ "Only valid when this is known to be an Intent action."
+ "Participant's previous orientation:(%@) does not match our previous view controller orientation:(%@) "
+ "Post-boot authentication cancelled or failed"
+ "Posting not permitted during screen sharing or health focused evaluation mode"
+ "Preferences must be finalized before being applied; this method should only be used when applying preferences by the host"
+ "Q\xf0\xe1"
+ "Re-evaluating overrides with audioSessionPlaying: %{BOOL}u"
+ "Reachability Complete"
+ "SBAmbientIdleTimerController.m"
+ "SBAmbientProudLockViewController"
+ "SBFCustomImplicitPropertyAnimating"
+ "SBHungApplicationInteractionObserver"
+ "SBHungApplicationInteractionObserver.m"
+ "SBPropertyAnimatingView"
+ "SBSystemAction-"
+ "SBSystemActionCoachingControllerDelegate"
+ "SBSystemApertureHostOrientationObserving"
+ "SBUIProudLockContainerViewControllerLockStatusProvider"
+ "SBWorkspaceMedusaCapabilityChangedNotification"
+ "SYSTEM_ACTION_COACHING_SHOW_FOCUS_LIST"
+ "Side Finishing Delay"
+ "SingleApp"
+ "SuggestionsAppLibraryEnabled"
+ "System Aperture Orientation settings did change to: %@"
+ "SystemActionCoaching"
+ "SystemApertureOrientation"
+ "SystemApertureRelinquishSuppression"
+ "T@\"FBScene\",R"
+ "T@\"NSArray\",C,N,VanimatedLayerProperties"
+ "T@\"SBAudioCategoryZStackPolicyAssistant\",&,N,V_audioCategoryZStackPolicyAssistant"
+ "T@\"SBFCAColorMatrixSettings\",&,N,V_jindoTintColorMatrixSettings"
+ "T@\"SBHungApplicationInteractionObserver\",R,N,V_hungApplicationInteractionObserver"
+ "TB,G_isHealthFocusedEvaluationModeActive,S_setHealthFocusedEvaluationModeActive:,V_healthFocusedEvaluationModeActive"
+ "TB,N,G_isCoverSheetPresentedByUserGesture,S_setCoverSheetPresentedByUserGesture:,V_coverSheetPresentedByUserGesture"
+ "TB,N,G_isIdleTimerAllowedForAssertionsForSleepFocus,S_setIdleTimerAllowedForAssertionsForSleepFocus:,V_idleTimerAllowedForAssertionsForSleepFocus"
+ "TB,N,V_suppressForSleep"
+ "TB,R,N,GisMedusaCapable,V_medusaCapable"
+ "TB,R,N,V_hostBundleRequiresValidation"
+ "TQ,R,N,V_executionGeneration"
+ "Td,N,V_acceptanceSideBounceFinishingDelay"
+ "Td,N,V_acceptanceUpBounceFinishingDelay"
+ "Td,N,V_ejectionYUpOffset"
+ "Td,N,V_jindoInertDisableOffset"
+ "Timestamp"
+ "Trying to decrement nonexistant rendering request"
+ "T{SBSwitcherWallpaperGradientAttributes=dd},N,V_attributes"
+ "T{SBSwitcherWallpaperGradientAttributes=dd},N,V_wallpaperGradientAttributes"
+ "T{SBSystemActionAnalyticsData=@@},R,N,V_analyticsData"
+ "Up Finishing Delay"
+ "Updating ambient presentation mount state to '%{public}@' with reason: '%{public}@'"
+ "Updating ambient presentation trigger state to '%{public}@' with reason: '%{public}@' [ analogousTriggerEvents : %{BOOL}d ]"
+ "Use of interface orientation attempted (in layout?) before being set by traits arbiter"
+ "WindowManagementStyleChangedTo%@"
+ "Y Up Offset"
+ "[%{public}lu] [Eject] Aborting stretch due to active element."
+ "[%{public}lu] [Eject] Complete"
+ "[%{public}lu] [Eject] Moving to Contracting phase"
+ "[%{public}lu] [Eject] Stretching, starting timer"
+ "[%{public}lu] [Eject] Timer Expired"
+ "[ActivityID: %{public}@] Not handling activity prominence update because activity has a lockscreen UI visible"
+ "[ActivityID: %{public}@] activity has ended, not handling alert update"
+ "[ActivityID: %{public}@] activity has ended, not handling prominence update"
+ "[ActivityID: %{public}@] activity has ended, not posting a banner"
+ "[ActivityID: %{public}@] can present alert: %d,  isHostApplicationForeground: %d, isCoverSheetVisible: %d, allowAlertsOnCoverSheet: %d, allowAlertsOnHostApp: %d"
+ "[attribute isKindOfClass:[AMAllowAmbientIdleTimerAttribute class]]"
+ "_SBAdaptiveColorMatrixView"
+ "_acceptanceSideBounceFinishingDelay"
+ "_acceptanceUpBounceFinishingDelay"
+ "_activatedElementItemForBundleIdentifier:"
+ "_addProudLockViewControllerIfNecessary"
+ "_ambientActiveFaceSceenOffTimestamp"
+ "_ambientCoreAnalyticsActiveFaceDescription:screenOffDuration:sessionIdString:"
+ "_ambientPowerLogAmbientMotionToWakeEnabled:"
+ "_analyticsData"
+ "_audioCategoryZStackPolicyAssistant"
+ "_authenticationCompletion"
+ "_backgroundTintColorForUserInterfaceStyle:"
+ "_beginInteractiveExecutionWithContext:executionHandler:error:"
+ "_bottomWallpaperView"
+ "_canSendVolumeButtonEventsToScene:withConfiguration:activeVolumeCategoryName:isAudioSessionPlaying:"
+ "_colorMatrixOpacityAnimatableProperty"
+ "_colorMatrixView"
+ "_coverSheetPresentedByUserGesture"
+ "_dismissAllOtherAmbientTransientOverlays"
+ "_dismissTransientProudLockAnimated"
+ "_displayTransientLockElementIfNecessaryForKeyBagState:"
+ "_displaysVolumeForCategory:"
+ "_effectiveAlwaysOnMode"
+ "_effectiveOverrideRenderingStyle"
+ "_effectiveVolumeChanged for '%{public}@' but volume category is not displayed by SBVolumeControl"
+ "_effectiveVolumeChanged for '%{public}@' for reason: %{public}@/%p"
+ "_ejectionYUpOffset"
+ "_executionGeneration"
+ "_handleExecutionBlockFinishedWithResult:"
+ "_handleHitTestingUpdatesWithContext:"
+ "_healthFocusedEvaluationModeActive"
+ "_heightForCardInSwitcherWithScaleFactor:"
+ "_hideLockElement"
+ "_hostBundleRequiresValidation"
+ "_hungApplicationInteractionObserver"
+ "_idleTimerAllowedForAssertionsForSleepFocus"
+ "_invalidateJindoReason"
+ "_invalidateTransientOverlayWindowTraitsArbiterParticipantIfNeeded"
+ "_invertColorsIsEnabled"
+ "_isCoverSheetPresentedByUserGesture"
+ "_isHealthFocusedEvaluationModeActive"
+ "_isIdleTimerAllowedForAssertionsForSleepFocus"
+ "_isMotionToWakePermitted"
+ "_isNightModeSettingMandatory"
+ "_isNightModeUserSettingEffectivelyEnabled"
+ "_jindoInertAssertion"
+ "_jindoInertDisableOffset"
+ "_jindoInertTimer"
+ "_jindoTintColorMatrixSettings"
+ "_lastKeyBagState"
+ "_lastQueriedParameterValueIdentifier"
+ "_logSignificantTimeChanged"
+ "_medusaCapabilityChanged:"
+ "_medusaCapable"
+ "_newWallpaperViewForVariant:"
+ "_notifyInteractionWithPossiblyHungApplicationSceneEntities:withInteractionType:"
+ "_overrideRenderingStyleAssertion"
+ "_overrideRenderingStyleRequests"
+ "_overshootOutsetsForTransitionPhase:baseOutsets:elementContext:"
+ "_prepareBlurForWrapperView"
+ "_priorLayoutMode"
+ "_proudLockContainerViewController"
+ "_proudLockViewController"
+ "_proudLockWrapperView"
+ "_queryPocketStateWithTimeout:"
+ "_reevaluateWindowManagementStyle"
+ "_removeProudLockViewController"
+ "_requiresAuthenticationAtLeastOnceSinceBootBeforeExecution"
+ "_resetTransientLockSuppressionFlag"
+ "_sendEventToPowerLog:payload:"
+ "_setCoverSheetPresentedByUserGesture:"
+ "_setHealthFocusedEvaluationModeActive:"
+ "_setIdleTimerAllowedForAssertions:forSleepFocus:"
+ "_setIdleTimerAllowedForAssertionsForSleepFocus:"
+ "_setProudLockAuthenticated:"
+ "_setupColorInvertObservation"
+ "_setupCornerContentsImageForWallpaperView:"
+ "_shouldSetDefaultBackground"
+ "_shouldSuppressForSleep"
+ "_shouldSuppressTransientLockIfKeyBagLocks"
+ "_startTimerIfNecessary:context:"
+ "_suppressForSleep"
+ "_topWallpaperView"
+ "_updateActiveFaceScreenOffForBacklightState:forConfiguration:sessionIdString:"
+ "_updateAmbientMountState:withReason:"
+ "_updateAmbientTriggerState:analogousTriggerEvents:withReason:"
+ "_updateColorMatrixAlpha:"
+ "_updateColorMatrixFilters"
+ "_updateElementOrientationTo:withTransitionCoordinator:"
+ "_updateMedusaCapabilitySendingNotification:"
+ "_updatePresentationPossibleForMountState:"
+ "_updateSleepSuppression"
+ "_updateWallpaperViewAnimated:"
+ "_updateWallpaperViewFilters"
+ "acceptanceSideBounceFinishingDelay"
+ "acceptanceUpBounceFinishingDelay"
+ "activeFaceScreenOffDuration"
+ "activeModeIdentifier"
+ "activityManager != ((void *)0)"
+ "allowAmbientIdleTimerForSleepFocus"
+ "alwaysOnMode"
+ "ambientPresentationManager:didUpdateMountState:"
+ "ambientPresentationManager:didUpdateTriggerState:analogousTriggerEvents:"
+ "ambientViewController:isApplicationVisibleWithBundleIdentifier:"
+ "analyticsData"
+ "animatableProperty"
+ "animatedLayerProperties"
+ "attribute"
+ "audioCategoryZStackPolicyAssistant"
+ "authenticationStatusProvider != ((void *)0)"
+ "bundleRecordWithBundleIdentifier:allowPlaceholder:error:"
+ "canChangeVolumeForActiveCategory:isAudioSessionPlaying:"
+ "com.apple.NanoUniverse.AegirProxyApp.AegirPoster"
+ "com.apple.SBReachabilityManager.SystemApertureInertTimer"
+ "com.apple.springboard."
+ "com.apple.springboard.actionbutton.powerlog"
+ "com.apple.springboard.bannerauthority.HealthFocusedEvaluationMode"
+ "com.apple.suggestions"
+ "contentData"
+ "countingTargetForEntry:"
+ "coverSheetPresentedByUserGesture"
+ "coverSheetViewController:requestsPreArmDisabled:forReason:"
+ "coverSheetViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:"
+ "coversheet updated audio categories disabling the Volume HUD"
+ "defaultSymbolConfiguration"
+ "displayTransientProudLock"
+ "ejectionYUpOffset"
+ "executeWithContext:executionHandler:completion:"
+ "executionGeneration"
+ "filters.gaussianBlur"
+ "folderCancelableDidChange:"
+ "healthFocusedEvaluationModeActive"
+ "host bundle does not exist"
+ "hostBundleRequiresValidation"
+ "hostOrientationDidChangeTo:withPreviousOrientation:context:"
+ "hungApplicationInteractionObserver"
+ "icon-config for dataSource is '%{public}@'"
+ "iconManager:backgroundViewForComponentsOfType:forIconView:"
+ "iconManager:verticalMarginPercentageForConfigurationOfIconView:"
+ "idleTimerAllowedForAssertionsForSleepFocus"
+ "initWithAuthenticationInformationProvider:"
+ "initWithBiometricResource:authenticationController:"
+ "initWithDataSource:previewCoordinator:authenticationStatusProvider:coachingController:soundController:"
+ "initWithHUDController:ringerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:"
+ "initWithRingerControl:activityManager:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:"
+ "initWithTransitionID:appLayout:layoutRole:"
+ "isBiometricLockedOut"
+ "isDepthEffectDisabled"
+ "isForSleepFocus"
+ "isForegroundActive"
+ "isIconVisibleForBundleIdentifier:"
+ "isRecording"
+ "issuerBindingAuthenticationOccured"
+ "jindoInertDisableOffset"
+ "jindoTintColorMatrixSettings"
+ "kill-app-from-app-switcher"
+ "logTelemetryForAmbientPresented:withBacklightState:screenOffWithConfiguration:"
+ "logTelemetryForMotionToWakeEnabled:"
+ "medusaCapable"
+ "observeRemovedApplicationSceneEntity:"
+ "overrideContainerRenderingStyleAssertion:"
+ "overrideProudLockIconViewLayoutWithSize:offset:extent:"
+ "overrideRenderingStyle > SBSystemApertureContainerRenderingStyleUnspecified"
+ "param_value"
+ "policyClassName == %@"
+ "pr_loadConfiguredPropertiesWithError:"
+ "proudLockAssetSize"
+ "reinitializeStatusBar"
+ "requiresAuthenticationAtLeastOnceSinceBootBeforeExecution"
+ "sb_configuredIntentAction"
+ "scrollAccessoryView"
+ "setAcceptanceSideBounceFinishingDelay:"
+ "setAcceptanceUpBounceFinishingDelay:"
+ "setAudioCategoryZStackPolicyAssistant:"
+ "setAuthenticated:completion:"
+ "setCompactOverlayHidden:"
+ "setDepthEffectDisabled:"
+ "setEjectionYUpOffset:"
+ "setFloatingLayerFullscreen:"
+ "setJindoInertDisableOffset:"
+ "setJindoTintColorMatrixSettings:"
+ "setSuppressForSleep:"
+ "shouldSuppressAlertContentOnLockScreen"
+ "suppressForSleep"
+ "systemActionCoachingController:canPresentCoachingForAction:"
+ "test_updateAmbientMountState:withReason:"
+ "test_updateAmbientTriggerState:withReason:"
+ "userInterfaceStyleChangedForEnvironment:previousTraitCollection:"
+ "v16@?0@?<v@?B@\"NSError\">8"
+ "v32@0:8{SBSwitcherWallpaperGradientAttributes=dd}16"
+ "v40@0:8q16q24@\"TRASettingsActuationContext\"32"
+ "velocityUsableForVFD"
+ "verticalMarginPercentageForConfigurationOfIconView:"
+ "{SBSwitcherWallpaperGradientAttributes=\"leadingAlpha\"d\"trailingAlpha\"d}"
+ "{SBSwitcherWallpaperGradientAttributes=dd}16@0:8"
+ "{SBSwitcherWallpaperGradientAttributes=dd}24@0:8Q16"
+ "{SBSwitcherWallpaperGradientAttributes=dd}24@?0@\"SBChainableModifier\"8Q16"
+ "{SBSystemActionAnalyticsData=\"actionIdentifier\"@\"NSString\"\"parameterValueIdentifier\"@\"NSString\"}"
+ "{SBSystemActionAnalyticsData=@@}16@0:8"
+ "{UIEdgeInsets=dddd}64@0:8q16{UIEdgeInsets=dddd}24@56"
+ "\xf0\x84\x84RJa\x14R\"AT1"
- "\x01\x13\x15\x1b\x13\x12\x112"
- "\x01\x14\x11"
- "\x01%3"
- "\x018\x11\x13"
- "\x02\xf0\xf0\xf0\xb1"
- "\x04\x13"
- "\a$\x18"
- "\x0f\x05"
- "!\x16%"
- "%{public}@: fetched config data for key: %{public}@, result: %{public}@ bytes"
- "@\"<BSInvalidatable>\"32@0:8@\"SBSystemActionInteractionContext\"16@?<v@?@\"<SBSystemActionExecuting>\"@\"NSError\">24"
- "@\"FCUIFocusEnablementIndicatorSystemApertureElement\"28@0:8@\"<FCActivityDescribing>\"16B24"
- "@\"SBHungApplicationTransitionObserver\""
- "A leading image should be provided for this action"
- "Ambient presentation allowed = %{BOOL}d [ enabled:%{BOOL}d ; lockedButNotBlocked:%{BOOL}d ; ignoreLockState:%{BOOL}d ; unlockedSinceBoot:%{BOOL}d ; carplay:%{BOOL}d ; screenOccludingAccessory:%{BOOL}d ; hostingApp:%{BOOL}d ; isInSetupMode:%{BOOL}d ; isOutOfPocket:%{BOOL}d ; isViewObstructed:%{BOOL}d ; listInteraction:%{BOOL}d ; spotlight:%{BOOL}d ; todayView:%{BOOL}d ]"
- "Ambient supression state updated. wasAmbientSuppressed = %{BOOL}u  isAmbientSuppressed = %{BOOL}u  [ _idleTimerAllowedForAssertions = %{BOOL}u _idleTimerAllowedForSuppression = %{BOOL}u ]"
- "CarpeDiem"
- "ChamoisWindowingDisabled"
- "Error compressing recents for persistence: %@"
- "Error decompressing recents: %@"
- "MedusaMultitaskingDisabled"
- "Posting not permitted during screen sharing"
- "Q\xf0\xd1"
- "SBHungApplicationTransitionObserver"
- "SBHungApplicationTransitionObserver.m"
- "SBMedusaEnabledStateChangedNotification"
- "SBSearchBarPortalRequiredForInteractivePresentationReason"
- "SystemApetureRelinquishSuppression"
- "T@\"FBScene\",R,N,V_externalSceneWithFocus"
- "T@\"SBHungApplicationTransitionObserver\",R,N,V_hungApplicationTransitionObserver"
- "TB,N,GisSuppressionMonitoringActive,V_suppressionMonitoringActive"
- "TB,R,N,GisMedusaEnabled,V_medusaEnabled"
- "Tq,N,V_overrideRenderingStyle"
- "Tq,N,V_viewObstructionEligibility"
- "T{SBSwitcherGradientWallpaperAttributes=dd},N,V_attributes"
- "T{SBSwitcherGradientWallpaperAttributes=dd},N,V_wallpaperGradientAttributes"
- "Updating ambient presentation state to '%{public}@' with reason: '%{public}@' [ analogousTriggerEvents : %{BOOL}d ]"
- "View obstruction eligibility"
- "[ActivityID: %{public}@] Not handling activity item because activity has a lockscreen UI visible"
- "[ActivityID: %{public}@] ambient item swapping with primary item"
- "[ActivityID: %{public}@] ambient item swapping with secondary item"
- "[ActivityID: %{public}@] can present alert: %d,  isHostApplicationForeground: %d, isCoverSheetVisible: %d, allowAlertsOnHostApp: %d"
- "_applyOrientation:withPreviousOrientation:animationSettings:"
- "_beginInteractiveExecutionWithContext:error:"
- "_bottomWallpaperEffectView"
- "_canSendVolumeButtonEventsToScene:withConfiguration:activeVolumeCategoryName:"
- "_canSwapActivityItem:withOtherItem:"
- "_canSwapPrimaryActivityWithItem:"
- "_canSwapSecondaryActivityWithItem:"
- "_effectiveVolumeChanged for AVSystemController but volume category '%{public}@' is not managed by SBVolumeControl"
- "_effectiveVolumeChanged for AVSystemController reason: %{public}@/%p"
- "_heightForCardInSwitcher"
- "_hungApplicationTransitionObserver"
- "_medusaEnabled"
- "_medusaEnabledStateChanged:"
- "_newWallpaperEffectViewForVariant:"
- "_notifyUserSwitchedAwayFromApplicationSceneEntities:withTransitionType:"
- "_overshootOutsetsForTransitionPhase:baseOutsets:"
- "_queryPocketState"
- "_registeredElementForBundleIdentifier:"
- "_setCompactOverlayHidden:"
- "_setupCornerContentsImageForWallpaperEffectView:"
- "_shouldSetBlackBackground"
- "_suppressionMonitoringActive"
- "_topWallpaperEffectView"
- "_updateActiveElementInterfaceOrientation"
- "_updateAmbientPresentationState:analogousTriggerEvents:withReason:"
- "_updateMedusaEnablementAndNotify:"
- "_updatePresentationPossibleForPresentationState:"
- "_updateSystemApertureZStackPolicyAssistant"
- "_updateWallpaperEffectViewAnimated:"
- "_windowingStyleDefaultChangeHandler"
- "action_id"
- "animationSettings != nil"
- "appIconAverageColor"
- "com.apple.springboard.ActionButtonFastSuppressionStatusUpdate"
- "com.apple.springboard.ActionButtonInteraction"
- "com.apple.springboard.ActionButtonPerformedAction"
- "com.apple.springboard.ActionButtonSelection"
- "createFocusElementForActivityDescription:enabled:"
- "executeWithContext:completion:"
- "hungApplicationTransitionObserver"
- "icon-config for dataSource '%{public}@' is"
- "initWithDataSource:previewCoordinator:coachingController:soundController:"
- "initWithHUDController:ringerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:"
- "initWithRingerControl:applicationController:doNotDisturbStateMonitor:flashlightActivityManager:"
- "initWithTransitionID:zoomModifier:appLayout:layoutRole:"
- "insertSubview:above:"
- "insertSubview:below:"
- "isMedusaEnabled"
- "isSuppressionMonitoringActive"
- "managesVolumeForCategory:"
- "medusaEnabled"
- "setClipsSubviews:"
- "setExplicitIntrinsicSize:"
- "setSuppressionMonitoringActive:"
- "setViewObstructionEligibility:"
- "suppressionMonitoringActive"
- "swapPrimaryActivityWithItem:"
- "swapSecondaryActivityWithItem:"
- "v32@0:8{SBSwitcherGradientWallpaperAttributes=dd}16"
- "viewObstructionEligibility"
- "{SBSwitcherGradientWallpaperAttributes=\"leadingAlpha\"d\"trailingAlpha\"d}"
- "{SBSwitcherGradientWallpaperAttributes=dd}16@0:8"
- "{SBSwitcherGradientWallpaperAttributes=dd}24@0:8Q16"
- "{SBSwitcherGradientWallpaperAttributes=dd}24@?0@\"SBChainableModifier\"8Q16"
- "{UIEdgeInsets=dddd}56@0:8q16{UIEdgeInsets=dddd}24"
- "\xf0ttBJa\x14R\"AT1"

```
