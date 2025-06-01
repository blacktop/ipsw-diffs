## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4416.132.102.1.0
-  __TEXT.__text: 0x88fb28
-  __TEXT.__auth_stubs: 0x4f30
+4416.306.103.0.0
+  __TEXT.__text: 0x89d94c
+  __TEXT.__auth_stubs: 0x4fc0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x84a24
-  __TEXT.__const: 0x12620
-  __TEXT.__oslogstring: 0x486d4
-  __TEXT.__cstring: 0x6a19d
-  __TEXT.__gcc_except_tab: 0xe200
-  __TEXT.__ustring: 0x146e
+  __TEXT.__objc_methlist: 0x85374
+  __TEXT.__const: 0x12700
+  __TEXT.__oslogstring: 0x4962f
+  __TEXT.__cstring: 0x6ac2c
+  __TEXT.__gcc_except_tab: 0xe54c
+  __TEXT.__ustring: 0x15b4
   __TEXT.__dlopen_cstrs: 0x2e6
-  __TEXT.__unwind_info: 0x2487c
+  __TEXT.__unwind_info: 0x24c68
   __TEXT.__eh_frame: 0xd48
-  __TEXT.__objc_classname: 0x1bb0b
-  __TEXT.__objc_methname: 0x185c2c
-  __TEXT.__objc_methtype: 0x3ef75
-  __TEXT.__objc_stubs: 0xcf560
-  __DATA_CONST.__got: 0x2798
-  __DATA_CONST.__const: 0x18e70
-  __DATA_CONST.__objc_classlist: 0x4498
+  __TEXT.__objc_classname: 0x1bce9
+  __TEXT.__objc_methname: 0x1874f8
+  __TEXT.__objc_methtype: 0x3f2fb
+  __TEXT.__objc_stubs: 0xd0420
+  __DATA_CONST.__got: 0x27d8
+  __DATA_CONST.__const: 0x19090
+  __DATA_CONST.__objc_classlist: 0x44e8
   __DATA_CONST.__objc_catlist: 0x2b0
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x21e0
+  __DATA_CONST.__objc_protolist: 0x2200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1db380
-  __DATA_CONST.__objc_selrefs: 0x3e5d0
+  __DATA_CONST.__objc_const: 0x1de398
+  __DATA_CONST.__objc_selrefs: 0x3ea38
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_classrefs: 0x63e8
-  __DATA_CONST.__objc_superrefs: 0x3558
-  __DATA_CONST.__objc_arraydata: 0x14d8
-  __AUTH_CONST.__objc_const: 0x2e6b0
-  __AUTH_CONST.__cfstring: 0x60520
-  __AUTH_CONST.__const: 0xe9f8
-  __AUTH_CONST.__objc_arrayobj: 0x1578
+  __DATA_CONST.__objc_classrefs: 0x6478
+  __DATA_CONST.__objc_superrefs: 0x35a0
+  __DATA_CONST.__objc_arraydata: 0x14e0
+  __AUTH_CONST.__objc_const: 0x2eaa0
+  __AUTH_CONST.__cfstring: 0x61040
+  __AUTH_CONST.__const: 0xea98
+  __AUTH_CONST.__objc_arrayobj: 0x1590
   __AUTH_CONST.__objc_intobj: 0x24f0
   __AUTH_CONST.__objc_doubleobj: 0x530
   __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH_CONST.__auth_got: 0x27b0
-  __AUTH.__objc_data: 0xc530
-  __DATA.__objc_ivar: 0xc7e4
-  __DATA.__data: 0x1aa28
+  __AUTH_CONST.__auth_got: 0x27f8
+  __AUTH.__objc_data: 0xc490
+  __DATA.__objc_ivar: 0xc920
+  __DATA.__data: 0x1aba8
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x9e8
+  __DATA.__bss: 0xa68
   __DATA.__common: 0x78
-  __DATA_DIRTY.__objc_data: 0x1e8c0
+  __DATA_DIRTY.__objc_data: 0x1ec80
   __DATA_DIRTY.__data: 0x150
-  __DATA_DIRTY.__bss: 0x16c8
+  __DATA_DIRTY.__bss: 0x1690
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: D138ADA5-2CD1-3B9F-AB21-5AFA9D93DDF4
-  Functions: 56306
-  Symbols:   191833
-  CStrings:  88866
+  UUID: 2641B910-A30A-3EC9-8918-14BA9119E023
+  Functions: 56649
+  Symbols:   192951
+  CStrings:  89362
 
Symbols:
+ +[SBApplication(Classic) restrictedClassicModeDisplayConfigurationForDisplayConfiguration:classicMode:].cold.1
+ +[SBApplication(Classic_Internal) _classicModeReplacingMoreSpaceWithEquivalentStandardCanvasForClassicMode:]
+ +[SBApplication(Classic_Internal) _standardCanvasSizeForClassicMode:]
+ +[SBRecordingIndicatorManager _supportsSecureIndicator]
+ +[SBRecordingIndicatorView layerClass]
+ +[SBScreenLongevityController _sharedInstanceCreateIfNeeded:]
+ +[SBScreenLongevityController sharedInstanceIfExists]
+ +[SBScreenLongevityController sharedInstance]
+ +[SBScreenLongevityDomain domainGroupName]
+ +[SBScreenLongevityDomain domainName]
+ +[SBScreenLongevityDomain rootSettingsClass]
+ +[SBScreenLongevityDomain rootSettings]
+ +[SBScreenLongevitySettings settingsControllerModule]
+ +[SBStatusBarWindow _isSecure]
+ -[SBActivitySystemApertureElementObserver _shouldSwapActivityItem:withOtherItem:itemAlerting:]
+ -[SBActivitySystemApertureElementObserver _swapItemWithRegisteredItemIfNecessary:itemAlerting:]
+ -[SBAppResizeGrabberView _grabberCurve]
+ -[SBAppResizeGrabberView _grabberPathForLength:curve:rotation:]
+ -[SBAppResizeGrabberView _grabberRotation]
+ -[SBAppResizeGrabberView _pillViewContainerViewFrame]
+ -[SBAppResizeGrabberView _pillViewContainerViewOffset]
+ -[SBAppResizeGrabberView _pointerRegionRect]
+ -[SBAppResizeGrabberView _updateGrabberPathAnimated:]
+ -[SBAppResizeGrabberView cornerRadius]
+ -[SBAppResizeGrabberView initWithCorner:cornerRadius:]
+ -[SBAppResizeGrabberView setCornerRadius:]
+ -[SBApplication _isNewEnoughToKnowAboutJ7xx]
+ -[SBApplicationController _applicationRestrictionMonitoringServer]
+ -[SBApplicationRestrictionController allAllowedAppBundleIdentifiers]
+ -[SBApplicationRestrictionController allRestrictedAppBundleIdentifiers]
+ -[SBApplicationRestrictionController isAllowlistActiveAndTransient]
+ -[SBApplicationRestrictionMonitoringServer .cxx_destruct]
+ -[SBApplicationRestrictionMonitoringServer _didFinishProcessingAppRestrictionUpdateWithUUID:]
+ -[SBApplicationRestrictionMonitoringServer _postAppRestrictionChangeWithState:]
+ -[SBApplicationRestrictionMonitoringServer acquireApplicationRestrictionUpdatePendingAssertionForReason:]
+ -[SBApplicationRestrictionMonitoringServer applicationRestrictionController:didUpdateVisibleTags:hiddenTags:]
+ -[SBApplicationRestrictionMonitoringServer applicationRestrictionControllerDidPostAppVisibilityUpdate:]
+ -[SBApplicationRestrictionMonitoringServer applicationRestrictionControllerWillPostAppVisibilityUpdate:]
+ -[SBApplicationRestrictionMonitoringServer authenticator]
+ -[SBApplicationRestrictionMonitoringServer connections]
+ -[SBApplicationRestrictionMonitoringServer init]
+ -[SBApplicationRestrictionMonitoringServer listener:didReceiveConnection:withContext:]
+ -[SBApplicationRestrictionMonitoringServer listener:didReceiveConnection:withContext:].cold.1
+ -[SBApplicationRestrictionMonitoringServer listener]
+ -[SBApplicationRestrictionMonitoringServer pendingRestrictionUpdateAssertion]
+ -[SBApplicationRestrictionMonitoringServer pendingRestrictionUpdateUUID]
+ -[SBApplicationRestrictionMonitoringServer queue]
+ -[SBApplicationRestrictionMonitoringServer removeConnection:]
+ -[SBApplicationRestrictionMonitoringServer restrictionControllerDidFinishNotifyingObserversAssertion]
+ -[SBApplicationRestrictionMonitoringServer setPendingRestrictionUpdateAssertion:]
+ -[SBApplicationRestrictionMonitoringServer setPendingRestrictionUpdateUUID:]
+ -[SBApplicationRestrictionMonitoringServer setRestrictionControllerDidFinishNotifyingObserversAssertion:]
+ -[SBAttentionAwarenessStreamerClient .cxx_destruct]
+ -[SBAttentionAwarenessStreamerClient _handleAttentionAwarenessEvent:]
+ -[SBAttentionAwarenessStreamerClient attentionAwarenessClient]
+ -[SBAttentionAwarenessStreamerClient configuration]
+ -[SBAttentionAwarenessStreamerClient delegate]
+ -[SBAttentionAwarenessStreamerClient identifier]
+ -[SBAttentionAwarenessStreamerClient init]
+ -[SBAttentionAwarenessStreamerClient invalidate]
+ -[SBAttentionAwarenessStreamerClient queue]
+ -[SBAttentionAwarenessStreamerClient resume]
+ -[SBAttentionAwarenessStreamerClient setAttentionAwarenessClient:]
+ -[SBAttentionAwarenessStreamerClient setConfiguration:]
+ -[SBAttentionAwarenessStreamerClient setConfiguration:shouldReset:]
+ -[SBAttentionAwarenessStreamerClient setDelegate:]
+ -[SBAttentionAwarenessStreamerClient setIdentifier:]
+ -[SBAttentionAwarenessStreamerClient setQueue:]
+ -[SBBannerSourceListenerHostedPresentableViewController _updateAppStatusBarSettingsAssertion]
+ -[SBBannerSourceListenerHostedPresentableViewController presentableDidAppearAsBanner:]
+ -[SBBannerSourceListenerHostedPresentableViewController presentableDidDisappearAsBanner:withReason:]
+ -[SBCommandTabController _effectiveSettingsChangedNotification:]
+ -[SBControlCenterController _policyAggregatorCapabilitiesDidChange:]
+ -[SBFluidSwitcherGestureManager _setUpChamoisGestureRecognizers]
+ -[SBFluidSwitcherGestureManager _setUpFloatingApplicationGestureRecognizers]
+ -[SBFluidSwitcherGestureManager _setUpScrunchGestureRecognizerIfNeeded]
+ -[SBFluidSwitcherGestureManager _tearDownChamoisGestureRecognizers]
+ -[SBFluidSwitcherGestureManager _tearDownFloatingApplicationGestureRecognizers]
+ -[SBFluidSwitcherGestureManager _updateChamoisGestureRecognizerPresenceForWindowManagementStyle:]
+ -[SBFluidSwitcherGestureManager _updateFloatingApplicationGestureRecognizerPresenceForWindowManagementStyle:]
+ -[SBFluidSwitcherGestureManager _updateFluidDragAndDropManagerPresenceForWindowManagementStyle:]
+ -[SBFluidSwitcherGestureManager _updateIndirectBottomEdgePanGesturePresence]
+ -[SBFluidSwitcherViewController viewDidDisappear:]
+ -[SBFluidSwitcherViewController viewDidLayoutSubviews]
+ -[SBHomeScreenConfigurationManager .cxx_destruct]
+ -[SBHomeScreenConfigurationManager applyDockItems:toFocusMode:iconModel:rootFolder:]
+ -[SBHomeScreenConfigurationManager applyHomeScreenItems:toFocusMode:iconModel:rootFolder:]
+ -[SBHomeScreenConfigurationManager configurationServer:didReceiveConfiguration:completion:]
+ -[SBHomeScreenConfigurationManager configurationServerDidBeginConfigurationSession:completion:]
+ -[SBHomeScreenConfigurationManager configurationServerDidEndConfigurationSession:completion:]
+ -[SBHomeScreenConfigurationManager focusModeFromConfiguration:]
+ -[SBHomeScreenConfigurationManager focusModeFromConfiguration:].cold.1
+ -[SBHomeScreenConfigurationManager focusModeManager]
+ -[SBHomeScreenConfigurationManager iconForApp:iconModel:rootFolder:]
+ -[SBHomeScreenConfigurationManager iconForApp:iconModel:rootFolder:].cold.1
+ -[SBHomeScreenConfigurationManager iconForItem:iconModel:rootFolder:]
+ -[SBHomeScreenConfigurationManager iconForItem:iconModel:rootFolder:].cold.1
+ -[SBHomeScreenConfigurationManager init]
+ -[SBHomeScreenConfigurationManager server]
+ -[SBHomeScreenConfigurationManager teardownFocusMode]
+ -[SBHomeScreenConfigurationServer .cxx_destruct]
+ -[SBHomeScreenConfigurationServer activate]
+ -[SBHomeScreenConfigurationServer applyConfiguration:completion:]
+ -[SBHomeScreenConfigurationServer authenticator]
+ -[SBHomeScreenConfigurationServer beginConfigurationSessionWithCompletion:]
+ -[SBHomeScreenConfigurationServer configurationSessionConnection]
+ -[SBHomeScreenConfigurationServer connections]
+ -[SBHomeScreenConfigurationServer delegate]
+ -[SBHomeScreenConfigurationServer endConfigurationSessionWithCompletion:]
+ -[SBHomeScreenConfigurationServer init]
+ -[SBHomeScreenConfigurationServer listener:didReceiveConnection:withContext:]
+ -[SBHomeScreenConfigurationServer listener:didReceiveConnection:withContext:].cold.1
+ -[SBHomeScreenConfigurationServer listener]
+ -[SBHomeScreenConfigurationServer makeErrorWithCode:]
+ -[SBHomeScreenConfigurationServer queue]
+ -[SBHomeScreenConfigurationServer removeConnection:]
+ -[SBHomeScreenConfigurationServer setConfigurationSessionConnection:]
+ -[SBHomeScreenConfigurationServer setDelegate:]
+ -[SBIconController _analyticsLoggingForDisplayZoomMode]
+ -[SBIconController _iconModel:wantsToRevealAnyApplicationFromIdentifiers:]
+ -[SBIconController _policyAggregatorCapabilitiesDidChange:]
+ -[SBIconController applicationRestrictionControllerDidPostAppVisibilityUpdate:]
+ -[SBIconController applicationRestrictionControllerWillPostAppVisibilityUpdate:]
+ -[SBInCallPresentationSession _isProximityReaderPresented]
+ -[SBInCallPresentationSession initWithSceneHandle:workspace:bannerManager:lockScreenManager:deactivationManager:mainSwitcherCoordinator:backlightController:keyboardFocusController:springBoard:setupManager:uiController:pipCoordinator:lockoutStateProvider:]
+ -[SBLockScreenManager _shouldPlayLockSound]
+ -[SBLockScreenManager playLockSoundIfPermitted]
+ -[SBMediaController playingMediaType]
+ -[SBMousePointerManager _updateScenesForPointerWithHardwareAttached:]
+ -[SBPencilSqueezeActionControl .cxx_destruct]
+ -[SBPencilSqueezeActionControl _runnerClientDidFinish:withResult:cancelled:]
+ -[SBPencilSqueezeActionControl _runnerClientForAction:timestamp:]
+ -[SBPencilSqueezeActionControl _shouldPerformAction:withReason:]
+ -[SBPencilSqueezeActionControl _updateSelectedAction]
+ -[SBPencilSqueezeActionControl _updateSelectedAction].cold.1
+ -[SBPencilSqueezeActionControl initWithDefaults:]
+ -[SBPencilSqueezeActionControl initWithDefaults:].cold.1
+ -[SBPencilSqueezeActionControl performSqueezeActionWithTimestamp:]
+ -[SBPencilSqueezeActionControl performSqueezeActionWithTimestamp:].cold.1
+ -[SBPencilSqueezeActionControl workflowRunnerClient:didFinishRunningWorkflowWithOutput:error:cancelled:]
+ -[SBReadOnlyDefaultIconModelStore deleteCurrentIconStateWithOptions:error:]
+ -[SBReadOnlyDefaultIconModelStore deleteDesiredIconStateWithOptions:error:]
+ -[SBReadOnlyDefaultIconModelStore loadCurrentIconState:]
+ -[SBReadOnlyDefaultIconModelStore loadDesiredIconState:]
+ -[SBReadOnlyDefaultIconModelStore saveCurrentIconState:error:]
+ -[SBReadOnlyDefaultIconModelStore saveDesiredIconState:error:]
+ -[SBRecordingIndicatorManager _createRecordingIndicatorForSecureIndicator]
+ -[SBRecordingIndicatorSettings delayBeforeFadeIn180]
+ -[SBRecordingIndicatorSettings delayBeforeFadeIn90]
+ -[SBRecordingIndicatorSettings delayBeforeFadeOut180]
+ -[SBRecordingIndicatorSettings delayBeforeFadeOut90]
+ -[SBRecordingIndicatorSettings fadeInDuration180]
+ -[SBRecordingIndicatorSettings fadeInDuration90]
+ -[SBRecordingIndicatorSettings fadeOutDuration180]
+ -[SBRecordingIndicatorSettings fadeOutDuration90]
+ -[SBRecordingIndicatorSettings setDelayBeforeFadeIn180:]
+ -[SBRecordingIndicatorSettings setDelayBeforeFadeIn90:]
+ -[SBRecordingIndicatorSettings setDelayBeforeFadeOut180:]
+ -[SBRecordingIndicatorSettings setDelayBeforeFadeOut90:]
+ -[SBRecordingIndicatorSettings setFadeInDuration180:]
+ -[SBRecordingIndicatorSettings setFadeInDuration90:]
+ -[SBRecordingIndicatorSettings setFadeOutDuration180:]
+ -[SBRecordingIndicatorSettings setFadeOutDuration90:]
+ -[SBRecordingIndicatorView _resetSecureLayerIndicatorType]
+ -[SBRecordingIndicatorView initWithCoder:]
+ -[SBRecordingIndicatorView initWithFrame:]
+ -[SBRecordingIndicatorViewController _hasMedinaPadBehaviors]
+ -[SBRecordingIndicatorViewController _hasProminentIdleState]
+ -[SBRecordingIndicatorViewController _ignoresActiveInterfaceOrientation]
+ -[SBRecordingIndicatorViewController _isOnExtendedDesktop]
+ -[SBRecordingIndicatorViewController _secureRenderingSupported]
+ -[SBRecordingIndicatorViewController _updateCenterWithoutAnimationForOrientation:]
+ -[SBRecordingIndicatorViewController _updateToOrientation:withDuration:]
+ -[SBRecordingIndicatorViewController _usesSpringAnimationsWithContainerView]
+ -[SBRecordingIndicatorViewController initForLocation:windowScene:]
+ -[SBRecordingIndicatorViewController setActiveInterfaceOrientation:withDuration:]
+ -[SBRecordingIndicatorViewController windowScene]
+ -[SBSceneViewStatusBarAssertion descriptionBuilderWithMultilinePrefix:]
+ -[SBSceneViewStatusBarAssertion descriptionWithMultilinePrefix:]
+ -[SBSceneViewStatusBarAssertion description]
+ -[SBSceneViewStatusBarAssertion succinctDescriptionBuilder]
+ -[SBSceneViewStatusBarAssertion succinctDescription]
+ -[SBScreenLongevityController .cxx_destruct]
+ -[SBScreenLongevityController _beginMonitoringAttentionAwarenessFeaturesEnablement]
+ -[SBScreenLongevityController _checkFaceAttentionAwareness]
+ -[SBScreenLongevityController _clientDidResetForUserAttention:]
+ -[SBScreenLongevityController _dim]
+ -[SBScreenLongevityController _endMonitoringAttentionAwarenessFeaturesEnablement]
+ -[SBScreenLongevityController _hasCameraAttributions]
+ -[SBScreenLongevityController _isAutoLockSetToNever]
+ -[SBScreenLongevityController _isDimmed]
+ -[SBScreenLongevityController _isValidCurrentTimer:]
+ -[SBScreenLongevityController _mediaNowPlayingChanged]
+ -[SBScreenLongevityController _observeDefaults]
+ -[SBScreenLongevityController _screenBacklightStateChanged]
+ -[SBScreenLongevityController _shouldEnable]
+ -[SBScreenLongevityController _startDimTimer]
+ -[SBScreenLongevityController _toggleBacklightAdaptiveDimming:]
+ -[SBScreenLongevityController _undim]
+ -[SBScreenLongevityController _updateCachedDefaults]
+ -[SBScreenLongevityController activityDidChangeForSensorActivityDataProvider:]
+ -[SBScreenLongevityController client:attentionLostTimeoutDidExpire:forConfigurationGeneration:withAssociatedObject:]
+ -[SBScreenLongevityController clientDidResetForUserAttention:]
+ -[SBScreenLongevityController dealloc]
+ -[SBScreenLongevityController dimTimerDidExpireForTimer:]
+ -[SBScreenLongevityController evaluateEnablement]
+ -[SBScreenLongevityController faceDetectionTimerDidExpire:]
+ -[SBScreenLongevityController faceStreamAwarenessConfiguration]
+ -[SBScreenLongevityController init]
+ -[SBScreenLongevityController isAdaptiveDimmingEnabled]
+ -[SBScreenLongevityController isUnderAutoDimThreshold]
+ -[SBScreenLongevityController profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:]
+ -[SBScreenLongevityController resetTimerForReason:]
+ -[SBScreenLongevityController setAdaptiveDimmingEnabled:]
+ -[SBScreenLongevityController setEnabled:]
+ -[SBScreenLongevityController settings:changedValueForKey:]
+ -[SBScreenLongevityController streamerClientDidResetForUserAttention:]
+ -[SBScreenLongevitySettings attentionScoreThreshold]
+ -[SBScreenLongevitySettings dimInterval]
+ -[SBScreenLongevitySettings dimmingAnimationLength]
+ -[SBScreenLongevitySettings enablement]
+ -[SBScreenLongevitySettings faceDetectionScoreThreshold]
+ -[SBScreenLongevitySettings ignoreAutoLockSetToNever]
+ -[SBScreenLongevitySettings minimalFaceDetectionInterval]
+ -[SBScreenLongevitySettings noOpButLogOnEnablementUpdate]
+ -[SBScreenLongevitySettings noisyLogging]
+ -[SBScreenLongevitySettings overrideEnablement]
+ -[SBScreenLongevitySettings setAttentionScoreThreshold:]
+ -[SBScreenLongevitySettings setDefaultValues]
+ -[SBScreenLongevitySettings setDimInterval:]
+ -[SBScreenLongevitySettings setDimmingAnimationLength:]
+ -[SBScreenLongevitySettings setEnablement:]
+ -[SBScreenLongevitySettings setFaceDetectionScoreThreshold:]
+ -[SBScreenLongevitySettings setIgnoreAutoLockSetToNever:]
+ -[SBScreenLongevitySettings setMinimalFaceDetectionInterval:]
+ -[SBScreenLongevitySettings setNoOpButLogOnEnablementUpdate:]
+ -[SBScreenLongevitySettings setNoisyLogging:]
+ -[SBScreenLongevitySettings setOverrideEnablement:]
+ -[SBScreenLongevitySettings setTouchAttentionLostTimeout:]
+ -[SBScreenLongevitySettings setUndimFaceDetectionInterval:]
+ -[SBScreenLongevitySettings setUndimmingAnimationLength:]
+ -[SBScreenLongevitySettings setWaitInterval:]
+ -[SBScreenLongevitySettings touchAttentionLostTimeout]
+ -[SBScreenLongevitySettings undimFaceDetectionInterval]
+ -[SBScreenLongevitySettings undimmingAnimationLength]
+ -[SBScreenLongevitySettings waitInterval]
+ -[SBScreenLongevityTimer .cxx_destruct]
+ -[SBScreenLongevityTimer _isValidCurrentTimer:]
+ -[SBScreenLongevityTimer dealloc]
+ -[SBScreenLongevityTimer delegate]
+ -[SBScreenLongevityTimer dimInterval]
+ -[SBScreenLongevityTimer dimTimerFired]
+ -[SBScreenLongevityTimer elapsedTime]
+ -[SBScreenLongevityTimer init]
+ -[SBScreenLongevityTimer invalidate]
+ -[SBScreenLongevityTimer isValid]
+ -[SBScreenLongevityTimer minimalFaceDetectionInterval]
+ -[SBScreenLongevityTimer scheduleFaceDetection]
+ -[SBScreenLongevityTimer setDelegate:]
+ -[SBScreenLongevityTimer setDimInterval:]
+ -[SBScreenLongevityTimer setMinimalFaceDetectionInterval:]
+ -[SBScreenLongevityTimer setWaitInterval:]
+ -[SBScreenLongevityTimer startFaceDetection]
+ -[SBScreenLongevityTimer start]
+ -[SBScreenLongevityTimer waitInterval]
+ -[SBStripContinuousExposeSwitcherModifier _cachedOrFallbackFrameForIndex:cacheValidityToken:]
+ -[SBStripContinuousExposeSwitcherModifier _cachedOrFallbackScaleForIndex:cacheValidityToken:]
+ -[SBSwitcherModifier(SharedModifierUtilities) appLayoutContainsFullScreenDisplayItem:]
+ -[SBSystemGestureManager _pencilInteraction:didReceiveSqueeze:]
+ -[SBSystemNotesManager _addContentViewControllerToPIPHierarchy:contentViewLayoutSettings:animated:]
+ -[SBSystemShellExtendedDisplayControllerPolicy _windowManagementStyleDidChange:]
+ -[SBSystemShellExtendedDisplayControllerPolicy initWithExternalDisplayDefaults:appSwitcherDefaults:externalDisplayService:mousePointerManager:runtimeAvailabilitySettings:sceneManager:windowSceneManager:]
+ -[SBSystemShellExtendedDisplayControllerPolicy reevaluateMirroringEnablement]
+ -[SBSystemShellExtendedDisplayControllerPolicyFactory initWithExternalDisplayService:externalDisplayDefaults:appSwitcherDefaults:mousePointerManager:runtimeAvailabilitySettings:sceneManager:windowSceneManager:]
+ -[SBTodayViewController _managedConfigurationEffectiveSettingsDidChange:]
+ -[SBVideoOutController _main_clearScreenSharingBackgroundActivityAssertion]
+ -[SBVideoOutController _main_clearVideoOutBackgroundActivityAssertion]
+ -[SBVideoOutController _main_startVideoOutBackgroundActivityAssertion]
+ -[SBVideoOutController _main_updateScreenSharingBackgroundActivityAssertionSuppressionPreference:]
+ -[SBVideoOutController _main_updateScreenSharingBackgroundActivityAssertion]
+ -[SBVideoOutController _main_updateVideoOutBackgroundActivityAssertion]
+ -[SBWallpaperController profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:]
+ -[SpringBoard _hideSpotlightOnPolicyChange]
+ -[SpringBoard _policyAggregatorCapabilitiesDidChange:]
+ -[SpringBoard pencilSqueezeActionControl]
+ -[SpringBoard updateHardwareKeyboardAttached]
+ -[_SBStatusBarWindowRootViewController _canShowWhileLocked]
+ GCC_except_table120
+ GCC_except_table131
+ GCC_except_table162
+ GCC_except_table174
+ GCC_except_table179
+ GCC_except_table191
+ GCC_except_table259
+ GCC_except_table295
+ GCC_except_table320
+ GCC_except_table332
+ GCC_except_table377
+ GCC_except_table405
+ GCC_except_table415
+ GCC_except_table449
+ GCC_except_table455
+ GCC_except_table464
+ GCC_except_table499
+ GCC_except_table525
+ GCC_except_table535
+ GCC_except_table561
+ GCC_except_table572
+ GCC_except_table574
+ GCC_except_table578
+ GCC_except_table601
+ GCC_except_table640
+ GCC_except_table66
+ GCC_except_table707
+ GCC_except_table741
+ GCC_except_table744
+ GCC_except_table749
+ _BKSHIDEventGetSmartCoverAttributes
+ _CAPrivacyIndicatorTypeForIndicatorType
+ _CARenderServerFlushIRDC
+ _CGPathEqualToPath
+ _OBJC_CLASS_$_BKSHIDEventGenericGestureDescriptor
+ _OBJC_CLASS_$_CASecureIndicatorLayer
+ _OBJC_CLASS_$_SBApplicationRestrictionMonitoringServer
+ _OBJC_CLASS_$_SBAttentionAwarenessStreamerClient
+ _OBJC_CLASS_$_SBHomeScreenConfigurationManager
+ _OBJC_CLASS_$_SBHomeScreenConfigurationServer
+ _OBJC_CLASS_$_SBPencilSqueezeActionControl
+ _OBJC_CLASS_$_SBReadOnlyDefaultIconModelStore
+ _OBJC_CLASS_$_SBSApplicationRestrictionMonitoringServiceInterfaceSpecification
+ _OBJC_CLASS_$_SBSApplicationRestrictionState
+ _OBJC_CLASS_$_SBSHomeScreenConfigurationServiceInterfaceSpecification
+ _OBJC_CLASS_$_SBScreenLongevityController
+ _OBJC_CLASS_$_SBScreenLongevityDomain
+ _OBJC_CLASS_$_SBScreenLongevitySettings
+ _OBJC_CLASS_$_SBScreenLongevityTimer
+ _OBJC_CLASS_$_UIPencilInteraction
+ _OBJC_CLASS_$_WFConfiguredSystemAction
+ _OBJC_CLASS_$_WFPencilSqueezeWorkflowRunnerClient
+ _OBJC_IVAR_$_SBAppResizeGrabberView._cornerRadius
+ _OBJC_IVAR_$_SBAppResizeGrabberView._grabberPath
+ _OBJC_IVAR_$_SBAppResizeGrabberView._pillViewContainerView
+ _OBJC_IVAR_$_SBApplicationController._restrictionMonitoringServer
+ _OBJC_IVAR_$_SBApplicationRestrictionMonitoringServer._authenticator
+ _OBJC_IVAR_$_SBApplicationRestrictionMonitoringServer._connections
+ _OBJC_IVAR_$_SBApplicationRestrictionMonitoringServer._listener
+ _OBJC_IVAR_$_SBApplicationRestrictionMonitoringServer._pendingRestrictionUpdateAssertion
+ _OBJC_IVAR_$_SBApplicationRestrictionMonitoringServer._pendingRestrictionUpdateUUID
+ _OBJC_IVAR_$_SBApplicationRestrictionMonitoringServer._queue
+ _OBJC_IVAR_$_SBApplicationRestrictionMonitoringServer._restrictionControllerDidFinishNotifyingObserversAssertion
+ _OBJC_IVAR_$_SBAttentionAwarenessStreamerClient._attentionAwarenessClient
+ _OBJC_IVAR_$_SBAttentionAwarenessStreamerClient._delegate
+ _OBJC_IVAR_$_SBAttentionAwarenessStreamerClient._identifier
+ _OBJC_IVAR_$_SBAttentionAwarenessStreamerClient._queue
+ _OBJC_IVAR_$_SBAttentionAwarenessStreamerClient._queue_configuration
+ _OBJC_IVAR_$_SBAttentionAwarenessStreamerClient._settings
+ _OBJC_IVAR_$_SBBannerSourceListenerHostedPresentableViewController._appStatusBarSettingsAssertion
+ _OBJC_IVAR_$_SBFluidSwitcherViewController._applicationRestrictionUpdatePendingAssertion
+ _OBJC_IVAR_$_SBHomeScreenConfigurationManager._server
+ _OBJC_IVAR_$_SBHomeScreenConfigurationServer._authenticator
+ _OBJC_IVAR_$_SBHomeScreenConfigurationServer._configurationSessionConnection
+ _OBJC_IVAR_$_SBHomeScreenConfigurationServer._connections
+ _OBJC_IVAR_$_SBHomeScreenConfigurationServer._delegate
+ _OBJC_IVAR_$_SBHomeScreenConfigurationServer._listener
+ _OBJC_IVAR_$_SBHomeScreenConfigurationServer._queue
+ _OBJC_IVAR_$_SBIconController._isAppAllowlistActiveAndTransient
+ _OBJC_IVAR_$_SBInCallPresentationSession._lockoutStateProvider
+ _OBJC_IVAR_$_SBLockScreenManager._hasPlayedSoundForLock
+ _OBJC_IVAR_$_SBMainWorkspace._homeScreenConfigurationManager
+ _OBJC_IVAR_$_SBPIPContainerViewController._wantsDisplayLayoutElement
+ _OBJC_IVAR_$_SBPencilSqueezeActionControl._defaults
+ _OBJC_IVAR_$_SBPencilSqueezeActionControl._runningRunnerClients
+ _OBJC_IVAR_$_SBPencilSqueezeActionControl._selectedAction
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._delayBeforeFadeIn180
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._delayBeforeFadeIn90
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._delayBeforeFadeOut180
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._delayBeforeFadeOut90
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._fadeInDuration180
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._fadeInDuration90
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._fadeOutDuration180
+ _OBJC_IVAR_$_SBRecordingIndicatorSettings._fadeOutDuration90
+ _OBJC_IVAR_$_SBRecordingIndicatorViewController._windowScene
+ _OBJC_IVAR_$_SBScreenLongevityController._attentionAwarenessFeatureMonitoringToken
+ _OBJC_IVAR_$_SBScreenLongevityController._brightnessSystemClient
+ _OBJC_IVAR_$_SBScreenLongevityController._defaultsObserver
+ _OBJC_IVAR_$_SBScreenLongevityController._dimTimer
+ _OBJC_IVAR_$_SBScreenLongevityController._enabled
+ _OBJC_IVAR_$_SBScreenLongevityController._faceStreamAwarenessClient
+ _OBJC_IVAR_$_SBScreenLongevityController._faceStreamAwarenessConfiguration
+ _OBJC_IVAR_$_SBScreenLongevityController._idleTouchAwarenessClient
+ _OBJC_IVAR_$_SBScreenLongevityController._idleTouchAwarenessConfiguration
+ _OBJC_IVAR_$_SBScreenLongevityController._settings
+ _OBJC_IVAR_$_SBScreenLongevityController._undimTimer
+ _OBJC_IVAR_$_SBScreenLongevitySettings._attentionScoreThreshold
+ _OBJC_IVAR_$_SBScreenLongevitySettings._dimInterval
+ _OBJC_IVAR_$_SBScreenLongevitySettings._dimmingAnimationLength
+ _OBJC_IVAR_$_SBScreenLongevitySettings._enablement
+ _OBJC_IVAR_$_SBScreenLongevitySettings._faceDetectionScoreThreshold
+ _OBJC_IVAR_$_SBScreenLongevitySettings._ignoreAutoLockSetToNever
+ _OBJC_IVAR_$_SBScreenLongevitySettings._minimalFaceDetectionInterval
+ _OBJC_IVAR_$_SBScreenLongevitySettings._noOpButLogOnEnablementUpdate
+ _OBJC_IVAR_$_SBScreenLongevitySettings._noisyLogging
+ _OBJC_IVAR_$_SBScreenLongevitySettings._overrideEnablement
+ _OBJC_IVAR_$_SBScreenLongevitySettings._touchAttentionLostTimeout
+ _OBJC_IVAR_$_SBScreenLongevitySettings._undimFaceDetectionInterval
+ _OBJC_IVAR_$_SBScreenLongevitySettings._undimmingAnimationLength
+ _OBJC_IVAR_$_SBScreenLongevitySettings._waitInterval
+ _OBJC_IVAR_$_SBScreenLongevityTimer._currentFaceDetectionTimerInterval
+ _OBJC_IVAR_$_SBScreenLongevityTimer._delegate
+ _OBJC_IVAR_$_SBScreenLongevityTimer._dimInterval
+ _OBJC_IVAR_$_SBScreenLongevityTimer._minimalFaceDetectionInterval
+ _OBJC_IVAR_$_SBScreenLongevityTimer._settings
+ _OBJC_IVAR_$_SBScreenLongevityTimer._startTime
+ _OBJC_IVAR_$_SBScreenLongevityTimer._timer
+ _OBJC_IVAR_$_SBScreenLongevityTimer._waitInterval
+ _OBJC_IVAR_$_SBSystemGestureManager._systemPencilInteraction
+ _OBJC_IVAR_$_SBSystemShellExtendedDisplayControllerPolicy._appSwitcherDefaults
+ _OBJC_IVAR_$_SBSystemShellExtendedDisplayControllerPolicy._requiredHardwareAvailable
+ _OBJC_IVAR_$_SBSystemShellExtendedDisplayControllerPolicy._windowSceneManager
+ _OBJC_IVAR_$_SBSystemShellExtendedDisplayControllerPolicyFactory._appSwitcherDefaults
+ _OBJC_IVAR_$_SBSystemShellExtendedDisplayControllerPolicyFactory._windowSceneManager
+ _OBJC_IVAR_$_SpringBoard._pencilSqueezeActionControl
+ _OBJC_METACLASS_$_SBApplicationRestrictionMonitoringServer
+ _OBJC_METACLASS_$_SBAttentionAwarenessStreamerClient
+ _OBJC_METACLASS_$_SBHomeScreenConfigurationManager
+ _OBJC_METACLASS_$_SBHomeScreenConfigurationServer
+ _OBJC_METACLASS_$_SBPencilSqueezeActionControl
+ _OBJC_METACLASS_$_SBReadOnlyDefaultIconModelStore
+ _OBJC_METACLASS_$_SBScreenLongevityController
+ _OBJC_METACLASS_$_SBScreenLongevityDomain
+ _OBJC_METACLASS_$_SBScreenLongevitySettings
+ _OBJC_METACLASS_$_SBScreenLongevityTimer
+ _SBApplicationClassicModeRepresentsMoreSpace
+ _SBApplicationRestrictionMonitoringEntitlement
+ _SBFIsIRDCResetAvailable
+ _SBFIsScreenLongevityAvailable
+ _SBHAnalyticsDisplayZoomMode
+ _SBHAnalyticsDisplayZoomModeDisplay
+ _SBHAnalyticsDisplayZoomModeDisplayMode
+ _SBHScreenTypeIsZoomed
+ _SBHomeScreenConfigurationEntitlement
+ _SBLogApplicationRestrictionMonitoring
+ _SBLogHomeScreenConfiguration
+ _SBLogPencilSqueeze
+ _SBLogPencilSqueeze.__logObj
+ _SBLogPencilSqueeze.onceToken
+ _SBLogScreenLongevityController
+ _SBLogScreenLongevityController.__logObj
+ _SBLogScreenLongevityController.onceToken
+ _SBLogSystemGesturePencilSqueeze
+ _SBLogSystemGesturePencilSqueeze.__logObj
+ _SBLogSystemGesturePencilSqueeze.onceToken
+ _SBSHomeScreenConfigurationErrorDomain
+ __AXSAttentionAwarenessFeaturesEnabled
+ __OBJC_$_CLASS_METHODS_SBRecordingIndicatorManager
+ __OBJC_$_CLASS_METHODS_SBRecordingIndicatorView
+ __OBJC_$_CLASS_METHODS_SBScreenLongevityController
+ __OBJC_$_CLASS_METHODS_SBScreenLongevityDomain
+ __OBJC_$_CLASS_METHODS_SBScreenLongevitySettings
+ __OBJC_$_CLASS_PROP_LIST_SBRecordingIndicatorManager
+ __OBJC_$_INSTANCE_METHODS_SBApplicationRestrictionMonitoringServer
+ __OBJC_$_INSTANCE_METHODS_SBAttentionAwarenessStreamerClient
+ __OBJC_$_INSTANCE_METHODS_SBHomeScreenConfigurationManager
+ __OBJC_$_INSTANCE_METHODS_SBHomeScreenConfigurationServer
+ __OBJC_$_INSTANCE_METHODS_SBPencilSqueezeActionControl
+ __OBJC_$_INSTANCE_METHODS_SBReadOnlyDefaultIconModelStore
+ __OBJC_$_INSTANCE_METHODS_SBScreenLongevityController
+ __OBJC_$_INSTANCE_METHODS_SBScreenLongevitySettings
+ __OBJC_$_INSTANCE_METHODS_SBScreenLongevityTimer
+ __OBJC_$_INSTANCE_VARIABLES_SBApplicationRestrictionMonitoringServer
+ __OBJC_$_INSTANCE_VARIABLES_SBAttentionAwarenessStreamerClient
+ __OBJC_$_INSTANCE_VARIABLES_SBHomeScreenConfigurationManager
+ __OBJC_$_INSTANCE_VARIABLES_SBHomeScreenConfigurationServer
+ __OBJC_$_INSTANCE_VARIABLES_SBPencilSqueezeActionControl
+ __OBJC_$_INSTANCE_VARIABLES_SBScreenLongevityController
+ __OBJC_$_INSTANCE_VARIABLES_SBScreenLongevitySettings
+ __OBJC_$_INSTANCE_VARIABLES_SBScreenLongevityTimer
+ __OBJC_$_PROP_LIST_SBApplicationRestrictionMonitoringServer
+ __OBJC_$_PROP_LIST_SBAttentionAwarenessStreamerClient
+ __OBJC_$_PROP_LIST_SBHomeScreenConfigurationManager
+ __OBJC_$_PROP_LIST_SBHomeScreenConfigurationServer
+ __OBJC_$_PROP_LIST_SBPencilSqueezeActionControl
+ __OBJC_$_PROP_LIST_SBReadOnlyDefaultIconModelStore
+ __OBJC_$_PROP_LIST_SBScreenLongevityController
+ __OBJC_$_PROP_LIST_SBScreenLongevitySettings
+ __OBJC_$_PROP_LIST_SBScreenLongevityTimer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBApplicationRestrictionObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBAttentionAwarenessStreamerClientDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSHomeScreenConfigurationClientToServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSHomeScreenConfigurationServerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBScreenLongevityTimerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBAttentionAwarenessStreamerClientDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSHomeScreenConfigurationClientToServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSHomeScreenConfigurationServerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBScreenLongevityTimerDelegate
+ __OBJC_$_PROTOCOL_REFS_SBAttentionAwarenessStreamerClientDelegate
+ __OBJC_$_PROTOCOL_REFS_SBSHomeScreenConfigurationClientToServerInterface
+ __OBJC_$_PROTOCOL_REFS_SBSHomeScreenConfigurationServerDelegate
+ __OBJC_$_PROTOCOL_REFS_SBScreenLongevityTimerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SBApplicationRestrictionMonitoringServer
+ __OBJC_CLASS_PROTOCOLS_$_SBAttentionAwarenessStreamerClient
+ __OBJC_CLASS_PROTOCOLS_$_SBHomeScreenConfigurationManager
+ __OBJC_CLASS_PROTOCOLS_$_SBHomeScreenConfigurationServer
+ __OBJC_CLASS_PROTOCOLS_$_SBPencilSqueezeActionControl
+ __OBJC_CLASS_PROTOCOLS_$_SBReadOnlyDefaultIconModelStore
+ __OBJC_CLASS_PROTOCOLS_$_SBScreenLongevityController
+ __OBJC_CLASS_PROTOCOLS_$_SBScreenLongevityTimer
+ __OBJC_CLASS_RO_$_SBApplicationRestrictionMonitoringServer
+ __OBJC_CLASS_RO_$_SBAttentionAwarenessStreamerClient
+ __OBJC_CLASS_RO_$_SBHomeScreenConfigurationManager
+ __OBJC_CLASS_RO_$_SBHomeScreenConfigurationServer
+ __OBJC_CLASS_RO_$_SBPencilSqueezeActionControl
+ __OBJC_CLASS_RO_$_SBReadOnlyDefaultIconModelStore
+ __OBJC_CLASS_RO_$_SBScreenLongevityController
+ __OBJC_CLASS_RO_$_SBScreenLongevityDomain
+ __OBJC_CLASS_RO_$_SBScreenLongevitySettings
+ __OBJC_CLASS_RO_$_SBScreenLongevityTimer
+ __OBJC_LABEL_PROTOCOL_$_SBAttentionAwarenessStreamerClientDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBSHomeScreenConfigurationClientToServerInterface
+ __OBJC_LABEL_PROTOCOL_$_SBSHomeScreenConfigurationServerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBScreenLongevityTimerDelegate
+ __OBJC_METACLASS_RO_$_SBApplicationRestrictionMonitoringServer
+ __OBJC_METACLASS_RO_$_SBAttentionAwarenessStreamerClient
+ __OBJC_METACLASS_RO_$_SBHomeScreenConfigurationManager
+ __OBJC_METACLASS_RO_$_SBHomeScreenConfigurationServer
+ __OBJC_METACLASS_RO_$_SBPencilSqueezeActionControl
+ __OBJC_METACLASS_RO_$_SBReadOnlyDefaultIconModelStore
+ __OBJC_METACLASS_RO_$_SBScreenLongevityController
+ __OBJC_METACLASS_RO_$_SBScreenLongevityDomain
+ __OBJC_METACLASS_RO_$_SBScreenLongevitySettings
+ __OBJC_METACLASS_RO_$_SBScreenLongevityTimer
+ __OBJC_PROTOCOL_$_SBAttentionAwarenessStreamerClientDelegate
+ __OBJC_PROTOCOL_$_SBSHomeScreenConfigurationClientToServerInterface
+ __OBJC_PROTOCOL_$_SBSHomeScreenConfigurationServerDelegate
+ __OBJC_PROTOCOL_$_SBScreenLongevityTimerDelegate
+ ___104-[SBApplicationRestrictionMonitoringServer applicationRestrictionControllerWillPostAppVisibilityUpdate:]_block_invoke
+ ___104-[SBApplicationRestrictionMonitoringServer applicationRestrictionControllerWillPostAppVisibilityUpdate:]_block_invoke_2
+ ___104-[SBApplicationRestrictionMonitoringServer applicationRestrictionControllerWillPostAppVisibilityUpdate:]_block_invoke_3
+ ___108-[SBActivitySystemApertureElementObserver _createAndActivateSystemApertureElementWithScene:item:completion:]_block_invoke.63
+ ___108-[SBActivitySystemApertureElementObserver _createAndActivateSystemApertureElementWithScene:item:completion:]_block_invoke.65
+ ___108-[SBSystemShellExtendedDisplayControllerPolicy mousePointerManager:hardwarePointingDeviceAttachedDidChange:]_block_invoke
+ ___112-[SBHideSharePlayContentFromSharedScreenController mousePointerManager:hardwarePointingDeviceAttachedDidChange:]_block_invoke
+ ___133-[SBSystemShellExtendedDisplayControllerPolicy displayController:updatePresentationWithSceneManager:displayConfiguration:completion:]_block_invoke.86
+ ___133-[SBSystemShellExtendedDisplayControllerPolicy displayController:updatePresentationWithSceneManager:displayConfiguration:completion:]_block_invoke.86.cold.1
+ ___255-[SBInCallPresentationSession initWithSceneHandle:workspace:bannerManager:lockScreenManager:deactivationManager:mainSwitcherCoordinator:backlightController:keyboardFocusController:springBoard:setupManager:uiController:pipCoordinator:lockoutStateProvider:]_block_invoke
+ ___31-[SBScreenLongevityTimer start]_block_invoke
+ ___31-[SBScreenLongevityTimer start]_block_invoke_2
+ ___31-[SBScreenLongevityTimer start]_block_invoke_3
+ ___31-[SBScreenLongevityTimer start]_block_invoke_4
+ ___35-[SBScreenLongevityController _dim]_block_invoke
+ ___35-[SBScreenLongevityController init]_block_invoke
+ ___35-[SBScreenLongevityController init]_block_invoke_2
+ ___37-[SBScreenLongevityController _undim]_block_invoke
+ ___38-[SBIconController _registerAnalytics]_block_invoke.290
+ ___39-[SBHomeScreenConfigurationServer init]_block_invoke
+ ___42-[SBAttentionAwarenessStreamerClient init]_block_invoke
+ ___42-[SBAttentionAwarenessStreamerClient init]_block_invoke_2
+ ___42-[SBScreenLongevityController setEnabled:]_block_invoke
+ ___42-[SBScreenLongevityController setEnabled:]_block_invoke.cold.1
+ ___42-[SBScreenLongevityController setEnabled:]_block_invoke.cold.2
+ ___42-[SBScreenLongevityController setEnabled:]_block_invoke.cold.3
+ ___42-[SBScreenLongevityController setEnabled:]_block_invoke.cold.4
+ ___43-[SpringBoard _hideSpotlightOnPolicyChange]_block_invoke
+ ___44-[SBAttentionAwarenessStreamerClient resume]_block_invoke
+ ___44-[SBAttentionAwarenessStreamerClient resume]_block_invoke.cold.1
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1106
+ ___45-[SBScreenLongevityController _startDimTimer]_block_invoke
+ ___45-[SBSystemGestureManager _evaluateEnablement]_block_invoke.62
+ ___47-[SBLockScreenManager handleTransitionRequest:]_block_invoke.212
+ ___47-[SBScreenLongevityController _observeDefaults]_block_invoke
+ ___47-[SBScreenLongevityTimer scheduleFaceDetection]_block_invoke
+ ___47-[SBScreenLongevityTimer scheduleFaceDetection]_block_invoke_2
+ ___48-[SBApplicationRestrictionMonitoringServer init]_block_invoke
+ ___48-[SBAttentionAwarenessStreamerClient invalidate]_block_invoke
+ ___48-[SBAttentionAwarenessStreamerClient invalidate]_block_invoke.cold.1
+ ___49-[SBPencilSqueezeActionControl initWithDefaults:]_block_invoke
+ ___50-[SBVideoOutController _updateDisplayMonitorState]_block_invoke
+ ___51-[SBAttentionAwarenessStreamerClient configuration]_block_invoke
+ ___52-[SBHomeScreenConfigurationServer removeConnection:]_block_invoke
+ ___52-[SBLockScreenManager _setPasscodeVisible:animated:]_block_invoke.350
+ ___53-[SBScreenLongevityController _hasCameraAttributions]_block_invoke
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.631
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.662
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.693
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.797
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.686
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.799
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.341
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.344
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.343
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.245
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.245.cold.1
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.250
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.250.cold.1
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.253
+ ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.253.cold.1
+ ___55+[SBRecordingIndicatorManager _supportsSecureIndicator]_block_invoke
+ ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.513
+ ___55-[SBIconController _analyticsLoggingForDisplayZoomMode]_block_invoke
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1599
+ ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.483
+ ___57-[SBMediaController _mediaRemoteNowPlayingInfoDidChange:]_block_invoke.69
+ ___57-[SBMediaController _mediaRemoteNowPlayingInfoDidChange:]_block_invoke.69.cold.1
+ ___57-[SBScreenLongevityController dimTimerDidExpireForTimer:]_block_invoke
+ ___57-[SBScreenLongevityController dimTimerDidExpireForTimer:]_block_invoke.48
+ ___57-[SBScreenLongevityController dimTimerDidExpireForTimer:]_block_invoke.cold.1
+ ___57-[SBSystemNotesManager _dismissNotesWithReason:animated:]_block_invoke.84
+ ___58-[SBMousePointerManager _updatePointerAssertionsAndScenes]_block_invoke
+ ___59-[SBIconController _updateUninstallingSystemAppsRestricted]_block_invoke.240
+ ___61+[SBScreenLongevityController _sharedInstanceCreateIfNeeded:]_block_invoke
+ ___62-[SBActivitySystemApertureElementObserver _removePendingItem:]_block_invoke
+ ___63-[SBLockScreenManager lockUIFromSource:withOptions:completion:]_block_invoke.206
+ ___63-[SBScreenLongevityController _clientDidResetForUserAttention:]_block_invoke
+ ___64-[SBCommandTabController _effectiveSettingsChangedNotification:]_block_invoke
+ ___64-[SBFluidSwitcherGestureManager _setUpChamoisGestureRecognizers]_block_invoke
+ ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.327
+ ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.327.cold.1
+ ___65-[SBFluidSwitcherViewController _reevaluateWindowManagementStyle]_block_invoke.910
+ ___65-[SBPencilSqueezeActionControl _runnerClientForAction:timestamp:]_block_invoke
+ ___67-[SBAttentionAwarenessStreamerClient setConfiguration:shouldReset:]_block_invoke
+ ___67-[SBVideoOutController displayPortObserver:connectionStateChanged:]_block_invoke
+ ___69-[SBFluidSwitcherGestureManager initWithSwitcherController:delegate:]_block_invoke_2
+ ___69-[SBIconController _performWidgetMigrationIfNecessaryForApplication:]_block_invoke.361
+ ___69-[SBIconController _performWidgetMigrationIfNecessaryForApplication:]_block_invoke.362
+ ___70-[SBVideoOutController _main_startVideoOutBackgroundActivityAssertion]_block_invoke
+ ___70-[SBVideoOutController _main_startVideoOutBackgroundActivityAssertion]_block_invoke.42
+ ___70-[SBVideoOutController _main_startVideoOutBackgroundActivityAssertion]_block_invoke_2
+ ___70-[SBVideoOutController _main_startVideoOutBackgroundActivityAssertion]_block_invoke_3
+ ___70-[SBVideoOutController _main_startVideoOutBackgroundActivityAssertion]_block_invoke_4
+ ___71-[SBSceneViewStatusBarAssertion descriptionBuilderWithMultilinePrefix:]_block_invoke
+ ___72-[SBRecordingIndicatorViewController _updateToOrientation:withDuration:]_block_invoke
+ ___72-[SBRecordingIndicatorViewController _updateToOrientation:withDuration:]_block_invoke_2
+ ___72-[SBRecordingIndicatorViewController _updateToOrientation:withDuration:]_block_invoke_3
+ ___73-[SBTodayViewController _managedConfigurationEffectiveSettingsDidChange:]_block_invoke
+ ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.369
+ ___76-[SBCommandTabController viewController:selectedApplicationWithDisplayItem:]_block_invoke.66
+ ___76-[SBFluidSwitcherGestureManager _setUpFloatingApplicationGestureRecognizers]_block_invoke
+ ___76-[SBFluidSwitcherGestureManager _updateIndirectBottomEdgePanGesturePresence]_block_invoke
+ ___76-[SBVideoOutController _main_updateScreenSharingBackgroundActivityAssertion]_block_invoke
+ ___76-[SBVideoOutController _main_updateScreenSharingBackgroundActivityAssertion]_block_invoke.36
+ ___76-[SBVideoOutController _main_updateScreenSharingBackgroundActivityAssertion]_block_invoke_2
+ ___76-[SBVideoOutController _main_updateScreenSharingBackgroundActivityAssertion]_block_invoke_3
+ ___76-[SBVideoOutController _main_updateScreenSharingBackgroundActivityAssertion]_block_invoke_4
+ ___77-[SBHomeScreenConfigurationServer listener:didReceiveConnection:withContext:]_block_invoke
+ ___77-[SBHomeScreenConfigurationServer listener:didReceiveConnection:withContext:]_block_invoke_2
+ ___77-[SBHomeScreenConfigurationServer listener:didReceiveConnection:withContext:]_block_invoke_3
+ ___79-[SBMainWorkspace _removeApplicationEntities:withDestructionIntent:completion:]_block_invoke.458
+ ___81-[SBHomeGrabberView mousePointerManager:hardwarePointingDeviceAttachedDidChange:]_block_invoke
+ ___81-[SBInCallTransientOverlayViewController _inCallSceneClientSettingsDiffInspector]_block_invoke_2
+ ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.404
+ ___83-[SBIconController _obtainSmartStackForWidgetDiscoverabilityWithCompletionHandler:]_block_invoke.337
+ ___83-[SBIconController _obtainSmartStackForWidgetDiscoverabilityWithCompletionHandler:]_block_invoke.339
+ ___83-[SBScreenLongevityController _beginMonitoringAttentionAwarenessFeaturesEnablement]_block_invoke
+ ___84-[SBHomeScreenConfigurationManager applyDockItems:toFocusMode:iconModel:rootFolder:]_block_invoke
+ ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke.27
+ ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke_2.28
+ ___86-[SBApplicationRestrictionMonitoringServer listener:didReceiveConnection:withContext:]_block_invoke
+ ___86-[SBApplicationRestrictionMonitoringServer listener:didReceiveConnection:withContext:]_block_invoke_2
+ ___86-[SBApplicationRestrictionMonitoringServer listener:didReceiveConnection:withContext:]_block_invoke_3
+ ___90-[SBHomeScreenConfigurationManager applyHomeScreenItems:toFocusMode:iconModel:rootFolder:]_block_invoke
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1457
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1459
+ ___91-[SBHomeScreenConfigurationManager configurationServer:didReceiveConfiguration:completion:]_block_invoke
+ ___93-[SBHomeScreenConfigurationManager configurationServerDidEndConfigurationSession:completion:]_block_invoke
+ ___93-[SBStripContinuousExposeSwitcherModifier _cachedOrFallbackFrameForIndex:cacheValidityToken:]_block_invoke
+ ___93-[SBStripContinuousExposeSwitcherModifier _cachedOrFallbackScaleForIndex:cacheValidityToken:]_block_invoke
+ ___94-[SBActivitySystemApertureElementObserver _invalidateSystemApertureElementForItem:completion:]_block_invoke.69
+ ___94-[SBActivitySystemApertureElementObserver _invalidateSystemApertureElementForItem:completion:]_block_invoke_2.70
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.600
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.618
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.633
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.635
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.643
+ ___96-[SBSystemShellExtendedDisplayControllerPolicy connectToDisplayController:displayConfiguration:]_block_invoke.69
+ ___96-[SBSystemShellExtendedDisplayControllerPolicy connectToDisplayController:displayConfiguration:]_block_invoke.73
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1582
+ ___SBLogPencilSqueeze_block_invoke
+ ___SBLogScreenLongevityController_block_invoke
+ ___SBLogSystemGesturePencilSqueeze_block_invoke
+ ___SBVideoOutController_DisplayPortAccessoryConnected_block_invoke
+ ___block_descriptor_32_e40_B16?0"<SBFSensorActivityAttribution>"8l
+ ___block_descriptor_40_e8_32s_e25_B16?0"SBActivityAlert"8ls32l8
+ ___block_descriptor_40_e8_32s_e45_B16?0"WFPencilSqueezeWorkflowRunnerClient"8ls32l8
+ ___block_descriptor_40_e8_32w_e21_v24?0"NSString"816lw32l8
+ ___block_descriptor_48_e8_32s40w_e29_v16?0"BSServiceConnection"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e8_v12?0B8lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e35_"SBIcon"16?0"SBSHomeScreenItem"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40w_e8_v16?0q8lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56w_e36_v16?0"<BSCompoundAssertionState>"8lw56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56w_e42_v16?0"<BSServiceConnectionConfiguring>"8ls32l8w56l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0ls32l8s40l8w56l8s48l8
+ ___block_literal_global.1049
+ ___block_literal_global.1052
+ ___block_literal_global.1057
+ ___block_literal_global.1063
+ ___block_literal_global.1162
+ ___block_literal_global.1207
+ ___block_literal_global.131
+ ___block_literal_global.1354
+ ___block_literal_global.1464
+ ___block_literal_global.1473
+ ___block_literal_global.1475
+ ___block_literal_global.1477
+ ___block_literal_global.1479
+ ___block_literal_global.1495
+ ___block_literal_global.1608
+ ___block_literal_global.1631
+ ___block_literal_global.1640
+ ___block_literal_global.1657
+ ___block_literal_global.215
+ ___block_literal_global.239
+ ___block_literal_global.252
+ ___block_literal_global.255
+ ___block_literal_global.287
+ ___block_literal_global.296
+ ___block_literal_global.336
+ ___block_literal_global.340
+ ___block_literal_global.343
+ ___block_literal_global.346
+ ___block_literal_global.367
+ ___block_literal_global.394
+ ___block_literal_global.410
+ ___block_literal_global.414
+ ___block_literal_global.419
+ ___block_literal_global.424
+ ___block_literal_global.427
+ ___block_literal_global.432
+ ___block_literal_global.457
+ ___block_literal_global.465
+ ___block_literal_global.489
+ ___block_literal_global.510
+ ___block_literal_global.512
+ ___block_literal_global.689
+ ___block_literal_global.716
+ ___block_literal_global.722
+ ___block_literal_global.727
+ ___block_literal_global.729
+ ___block_literal_global.731
+ ___block_literal_global.735
+ ___block_literal_global.737
+ ___block_literal_global.739
+ ___block_literal_global.746
+ ___block_literal_global.751
+ ___block_literal_global.753
+ ___block_literal_global.755
+ ___block_literal_global.758
+ ___block_literal_global.801
+ ___block_literal_global.878
+ ___block_literal_global.962
+ ___block_literal_global.994
+ __supportsSecureIndicator.onceToken
+ __supportsSecureIndicator.supportsSecureIndicator
+ __unnamed_array_storage.138
+ __unnamed_array_storage.1605
+ __unnamed_array_storage.1744
+ __unnamed_array_storage.1753
+ __unnamed_array_storage.242
+ __unnamed_array_storage.372
+ __unnamed_array_storage.376
+ __unnamed_array_storage.379
+ __unnamed_array_storage.382
+ __unnamed_array_storage.449
+ __unnamed_array_storage.467
+ __unnamed_array_storage.479
+ __unnamed_array_storage.495
+ __unnamed_array_storage.501
+ __unnamed_array_storage.507
+ __unnamed_array_storage.522
+ __unnamed_array_storage.528
+ __unnamed_array_storage.534
+ __unnamed_array_storage.540
+ __unnamed_array_storage.749
+ __unnamed_array_storage.755
+ __unnamed_array_storage.77
+ __unnamed_array_storage.85
+ _kAXSAttentionAwarenessFeaturesEnabledNotification
+ _kCAContextDisplayId
+ _kCAPrivacyIndicatorTypeCamera
+ _kCAPrivacyIndicatorTypeMicrophone
+ _kCAPrivacyIndicatorTypeMicrophoneAccessibility
+ _kMRMediaRemoteNowPlayingInfoMediaType
+ _kMRMediaRemoteNowPlayingInfoTypeVideo
+ _objc_msgSend$_addContentViewControllerToPIPHierarchy:contentViewLayoutSettings:animated:
+ _objc_msgSend$_analyticsLoggingForDisplayZoomMode
+ _objc_msgSend$_applicationRestrictionMonitoringServer
+ _objc_msgSend$_beginMonitoringAttentionAwarenessFeaturesEnablement
+ _objc_msgSend$_cachedOrFallbackFrameForIndex:cacheValidityToken:
+ _objc_msgSend$_cachedOrFallbackScaleForIndex:cacheValidityToken:
+ _objc_msgSend$_checkFaceAttentionAwareness
+ _objc_msgSend$_classicModeReplacingMoreSpaceWithEquivalentStandardCanvasForClassicMode:
+ _objc_msgSend$_clientDidResetForUserAttention:
+ _objc_msgSend$_createRecordingIndicatorForSecureIndicator
+ _objc_msgSend$_dim
+ _objc_msgSend$_display
+ _objc_msgSend$_endMonitoringAttentionAwarenessFeaturesEnablement
+ _objc_msgSend$_grabberCurve
+ _objc_msgSend$_grabberPathForLength:curve:rotation:
+ _objc_msgSend$_grabberRotation
+ _objc_msgSend$_hasCameraAttributions
+ _objc_msgSend$_hideSpotlightOnPolicyChange
+ _objc_msgSend$_iconModel:wantsToRevealAnyApplicationFromIdentifiers:
+ _objc_msgSend$_isAutoLockSetToNever
+ _objc_msgSend$_isDimmed
+ _objc_msgSend$_isProximityReaderPresented
+ _objc_msgSend$_isValidCurrentTimer:
+ _objc_msgSend$_main_clearScreenSharingBackgroundActivityAssertion
+ _objc_msgSend$_main_clearVideoOutBackgroundActivityAssertion
+ _objc_msgSend$_main_startVideoOutBackgroundActivityAssertion
+ _objc_msgSend$_main_updateScreenSharingBackgroundActivityAssertion
+ _objc_msgSend$_main_updateScreenSharingBackgroundActivityAssertionSuppressionPreference:
+ _objc_msgSend$_main_updateVideoOutBackgroundActivityAssertion
+ _objc_msgSend$_nativeBounds
+ _objc_msgSend$_observeDefaults
+ _objc_msgSend$_phase
+ _objc_msgSend$_pillViewContainerViewFrame
+ _objc_msgSend$_pillViewContainerViewOffset
+ _objc_msgSend$_pointerRegionRect
+ _objc_msgSend$_preferredSqueezeAction
+ _objc_msgSend$_privateNotificationOccurred:atLocation:senderID:
+ _objc_msgSend$_setUpChamoisGestureRecognizers
+ _objc_msgSend$_setUpFloatingApplicationGestureRecognizers
+ _objc_msgSend$_setUpScrunchGestureRecognizerIfNeeded
+ _objc_msgSend$_shouldEnable
+ _objc_msgSend$_shouldPlayLockSound
+ _objc_msgSend$_shouldSwapActivityItem:withOtherItem:itemAlerting:
+ _objc_msgSend$_standardCanvasSizeForClassicMode:
+ _objc_msgSend$_startDimTimer
+ _objc_msgSend$_supportsSecureIndicator
+ _objc_msgSend$_swapItemWithRegisteredItemIfNecessary:itemAlerting:
+ _objc_msgSend$_tearDownChamoisGestureRecognizers
+ _objc_msgSend$_tearDownFloatingApplicationGestureRecognizers
+ _objc_msgSend$_timestamp
+ _objc_msgSend$_toggleBacklightAdaptiveDimming:
+ _objc_msgSend$_undim
+ _objc_msgSend$_updateCachedDefaults
+ _objc_msgSend$_updateChamoisGestureRecognizerPresenceForWindowManagementStyle:
+ _objc_msgSend$_updateFloatingApplicationGestureRecognizerPresenceForWindowManagementStyle:
+ _objc_msgSend$_updateFluidDragAndDropManagerPresenceForWindowManagementStyle:
+ _objc_msgSend$_updateGrabberPathAnimated:
+ _objc_msgSend$_updateIndirectBottomEdgePanGesturePresence
+ _objc_msgSend$_updateScenesForPointerWithHardwareAttached:
+ _objc_msgSend$acquireApplicationRestrictionUpdatePendingAssertionForReason:
+ _objc_msgSend$addAdditionalIconMatchingIcon:
+ _objc_msgSend$allAllowedAppBundleIdentifiers
+ _objc_msgSend$allRestrictedAppBundleIdentifiers
+ _objc_msgSend$appLayoutContainsFullScreenDisplayItem:
+ _objc_msgSend$applicationRestrictionControllerDidPostAppVisibilityUpdate:
+ _objc_msgSend$applicationRestrictionControllerWillPostAppVisibilityUpdate:
+ _objc_msgSend$attentionScore
+ _objc_msgSend$attentionScoreThreshold
+ _objc_msgSend$configurationServer:didReceiveConfiguration:completion:
+ _objc_msgSend$configurationServerDidBeginConfigurationSession:completion:
+ _objc_msgSend$configurationServerDidEndConfigurationSession:completion:
+ _objc_msgSend$copyPropertyForKey:
+ _objc_msgSend$delayBeforeFadeIn180
+ _objc_msgSend$delayBeforeFadeIn90
+ _objc_msgSend$delayBeforeFadeOut180
+ _objc_msgSend$delayBeforeFadeOut90
+ _objc_msgSend$descriptorWithGenericGestureType:
+ _objc_msgSend$dimInterval
+ _objc_msgSend$dimTimerDidExpireForTimer:
+ _objc_msgSend$dimTimerFired
+ _objc_msgSend$dimmingAnimationLength
+ _objc_msgSend$dockItems
+ _objc_msgSend$dockList
+ _objc_msgSend$donateFocusMode:fromSource:
+ _objc_msgSend$elapsedTime
+ _objc_msgSend$enablement
+ _objc_msgSend$evaluateEnablement
+ _objc_msgSend$faceDetectionScore
+ _objc_msgSend$faceDetectionScoreThreshold
+ _objc_msgSend$faceDetectionTimerDidExpire:
+ _objc_msgSend$faceStreamAwarenessConfiguration
+ _objc_msgSend$fadeInDuration180
+ _objc_msgSend$fadeInDuration90
+ _objc_msgSend$fadeOutDuration180
+ _objc_msgSend$fadeOutDuration90
+ _objc_msgSend$ignoreAutoLockSetToNever
+ _objc_msgSend$indexPathForIcon:includingPlaceholders:
+ _objc_msgSend$initForLocation:windowScene:
+ _objc_msgSend$initWithAllowedIdentifiers:restrictedIdentifiers:
+ _objc_msgSend$initWithCorner:cornerRadius:
+ _objc_msgSend$initWithExternalDisplayDefaults:appSwitcherDefaults:externalDisplayService:mousePointerManager:runtimeAvailabilitySettings:sceneManager:windowSceneManager:
+ _objc_msgSend$initWithExternalDisplayService:externalDisplayDefaults:appSwitcherDefaults:mousePointerManager:runtimeAvailabilitySettings:sceneManager:windowSceneManager:
+ _objc_msgSend$initWithFloat:
+ _objc_msgSend$initWithInt:
+ _objc_msgSend$initWithSceneHandle:workspace:bannerManager:lockScreenManager:deactivationManager:mainSwitcherCoordinator:backlightController:keyboardFocusController:springBoard:setupManager:uiController:pipCoordinator:lockoutStateProvider:
+ _objc_msgSend$initWithSystemAction:preciseTimeStamp:
+ _objc_msgSend$invalidateRestrictionCache
+ _objc_msgSend$isAdaptiveDimmingEnabled
+ _objc_msgSend$isAllowlistActiveAndTransient
+ _objc_msgSend$isAutoDimAllowed
+ _objc_msgSend$isBeingShownAboveCoverSheet
+ _objc_msgSend$isCommandTabAllowed
+ _objc_msgSend$isControlCenterAllowed
+ _objc_msgSend$isDisabledByMediaPlayback
+ _objc_msgSend$isHomeScreenEditingAllowed
+ _objc_msgSend$isSpotlightAllowed
+ _objc_msgSend$isUnderAutoDimThreshold
+ _objc_msgSend$isWallpaperAllowed
+ _objc_msgSend$loadCurrentIconState:
+ _objc_msgSend$loadDesiredIconState:
+ _objc_msgSend$minimalFaceDetectionInterval
+ _objc_msgSend$noOpButLogOnEnablementUpdate
+ _objc_msgSend$noisyLogging
+ _objc_msgSend$observePrefersLockedIdleDurationOnCoversheet:
+ _objc_msgSend$observeUpdateWithApplicationRestrictState:
+ _objc_msgSend$overrideEnablement
+ _objc_msgSend$pencilDefaults
+ _objc_msgSend$pencilSqueezeActionControl
+ _objc_msgSend$playLockSoundIfPermitted
+ _objc_msgSend$playingMediaType
+ _objc_msgSend$prefersLockedIdleDurationOnCoversheet
+ _objc_msgSend$privacyIndicatorType
+ _objc_msgSend$reevaluateMirroringEnablement
+ _objc_msgSend$registerNotificationBlock:forProperties:
+ _objc_msgSend$removeList:
+ _objc_msgSend$resetTimerForReason:
+ _objc_msgSend$scheduleFaceDetection
+ _objc_msgSend$screenLongevityDefaults
+ _objc_msgSend$setActiveInterfaceOrientation:withDuration:
+ _objc_msgSend$setAdaptiveDimmingEnabled:
+ _objc_msgSend$setContinuousFaceDetectMode:
+ _objc_msgSend$setDelayBeforeFadeIn180:
+ _objc_msgSend$setDelayBeforeFadeIn90:
+ _objc_msgSend$setDelayBeforeFadeOut180:
+ _objc_msgSend$setDelayBeforeFadeOut90:
+ _objc_msgSend$setDockList:
+ _objc_msgSend$setEventStreamerWithQueue:block:
+ _objc_msgSend$setFadeInDuration180:
+ _objc_msgSend$setFadeInDuration90:
+ _objc_msgSend$setFadeOutDuration180:
+ _objc_msgSend$setFadeOutDuration90:
+ _objc_msgSend$setIcons:
+ _objc_msgSend$setPrivacyIndicatorType:
+ _objc_msgSend$setUnityStream:
+ _objc_msgSend$speedMultiplierForMagicKeyboardExtended
+ _objc_msgSend$squeezeConfiguredActionArchive
+ _objc_msgSend$startFaceDetection
+ _objc_msgSend$startWithPreciseTimeStamp:
+ _objc_msgSend$streamerClientDidResetForUserAttention:
+ _objc_msgSend$touchAttentionLostTimeout
+ _objc_msgSend$undimFaceDetectionInterval
+ _objc_msgSend$undimmingAnimationLength
+ _objc_msgSend$updateHardwareKeyboardAttached
+ _objc_msgSend$waitInterval
+ _objc_msgSend$wakeAnimationStyle
- -[SBActivitySystemApertureElementObserver _shouldSwapActivityItem:withOtherItem:]
- -[SBActivitySystemApertureElementObserver _swapItemWithRegisteredItemIfNecessary:]
- -[SBAppResizeGrabberView _resizeGrabberPathForSize:curve:lineWidth:rotation:]
- -[SBFluidSwitcherGestureManager _configureClickDownToBringItemContainerForwardGesture]
- -[SBFluidSwitcherGestureManager _configureFloatingApplicationGestureRecognizers]
- -[SBFluidSwitcherGestureManager _configureScrunchGesture]
- -[SBFluidSwitcherGestureManager _configureTapToBringItemContainerForwardGesture]
- -[SBFluidSwitcherGestureManager _setUpChamoisGestureRecognizersIfNeeded]
- -[SBFluidSwitcherGestureManager _tearDownChamoisGestureRecognizersIfNeeded]
- -[SBFluidSwitcherGestureManager configureIndirectBottomEdgePanGestureRecognizer]
- -[SBInCallPresentationSession initWithSceneHandle:workspace:bannerManager:lockScreenManager:deactivationManager:mainSwitcherCoordinator:backlightController:keyboardFocusController:springBoard:setupManager:uiController:pipCoordinator:]
- -[SBLockScreenManager shouldPlayLockSound]
- -[SBMainSwitcherControllerCoordinator _supportsFloatingApplicationForSwitcherController:]
- -[SBMainSwitcherControllerCoordinator fluidSwitcherGestureManagerSupportsFloatingApplication:]
- -[SBRecordingIndicatorViewController _updateToOrientation:]
- -[SBRecordingIndicatorViewController initForLocation:]
- -[SBRecordingIndicatorViewController setActiveInterfaceOrientation:]
- -[SBSleepWakeHardwareButtonInteraction didPlayLockSound]
- -[SBSleepWakeHardwareButtonInteraction setDidPlayLockSound:]
- -[SBSwitcherController fluidSwitcherGestureManagerSupportsFloatingApplication:]
- -[SBSystemNotesManager _addContentViewControllerToPIPHierarchy:contentViewLayoutSettings:]
- -[SBSystemShellExtendedDisplayControllerPolicy initWithExternalDisplayDefaults:externalDisplayService:mousePointerManager:runtimeAvailabilitySettings:sceneManager:]
- -[SBSystemShellExtendedDisplayControllerPolicyFactory initWithExternalDisplayService:externalDisplayDefaults:mousePointerManager:runtimeAvailabilitySettings:sceneManager:]
- -[SBVideoOutController _clearScreenSharingBackgroundActivityAssertion]
- -[SBVideoOutController _clearVideoOutBackgroundActivityAssertion]
- -[SBVideoOutController _startVideoOutBackgroundActivityAssertion]
- -[SBVideoOutController _updateScreenSharingBackgroundActivityAssertionSuppressionPreference:]
- -[SBVideoOutController _updateVideoOutBackgroundActivityAssertion]
- -[SpringBoard _updateHardwareKeyboardAttached]
- GCC_except_table158
- GCC_except_table177
- GCC_except_table183
- GCC_except_table189
- GCC_except_table223
- GCC_except_table229
- GCC_except_table261
- GCC_except_table297
- GCC_except_table316
- GCC_except_table328
- GCC_except_table359
- GCC_except_table375
- GCC_except_table389
- GCC_except_table403
- GCC_except_table409
- GCC_except_table411
- GCC_except_table441
- GCC_except_table452
- GCC_except_table453
- GCC_except_table462
- GCC_except_table497
- GCC_except_table523
- GCC_except_table531
- GCC_except_table555
- GCC_except_table566
- GCC_except_table568
- GCC_except_table570
- GCC_except_table599
- GCC_except_table638
- GCC_except_table705
- GCC_except_table739
- GCC_except_table742
- GCC_except_table747
- OBJC_IVAR_$_SpringBoard._didPlayLockSound
- _OBJC_IVAR_$_SBAppResizeGrabberView._maskPath
- _OBJC_IVAR_$_SBSleepWakeHardwareButtonInteraction._didPlayLockSound
- _OBJC_IVAR_$_SBSystemShellExtendedDisplayControllerPolicy._userMirroringPreference
- ___108-[SBActivitySystemApertureElementObserver _createAndActivateSystemApertureElementWithScene:item:completion:]_block_invoke.61
- ___108-[SBActivitySystemApertureElementObserver _createAndActivateSystemApertureElementWithScene:item:completion:]_block_invoke.64
- ___133-[SBSystemShellExtendedDisplayControllerPolicy displayController:updatePresentationWithSceneManager:displayConfiguration:completion:]_block_invoke.78
- ___133-[SBSystemShellExtendedDisplayControllerPolicy displayController:updatePresentationWithSceneManager:displayConfiguration:completion:]_block_invoke.78.cold.1
- ___234-[SBInCallPresentationSession initWithSceneHandle:workspace:bannerManager:lockScreenManager:deactivationManager:mainSwitcherCoordinator:backlightController:keyboardFocusController:springBoard:setupManager:uiController:pipCoordinator:]_block_invoke
- ___38-[SBIconController _registerAnalytics]_block_invoke.288
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1099
- ___45-[SBSystemGestureManager _evaluateEnablement]_block_invoke.60
- ___47-[SBLockScreenManager handleTransitionRequest:]_block_invoke.210
- ___52-[SBLockScreenManager _setPasscodeVisible:animated:]_block_invoke.348
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.628
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.659
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.690
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.794
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.683
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.795
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.339
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.342
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.341
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.244
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.244.cold.1
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.248
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.249.cold.1
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.252
- ___54-[SBWallpaperController updatePosterSwitcherSnapshots]_block_invoke.252.cold.1
- ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.506
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1592
- ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.482
- ___57-[SBMediaController _mediaRemoteNowPlayingInfoDidChange:]_block_invoke.66
- ___57-[SBMediaController _mediaRemoteNowPlayingInfoDidChange:]_block_invoke.66.cold.1
- ___57-[SBStripContinuousExposeSwitcherModifier frameForIndex:]_block_invoke
- ___57-[SBStripContinuousExposeSwitcherModifier scaleForIndex:]_block_invoke
- ___57-[SBStripContinuousExposeSwitcherModifier scaleForIndex:]_block_invoke_2
- ___57-[SBSystemNotesManager _dismissNotesWithReason:animated:]_block_invoke.83
- ___59-[SBIconController _updateUninstallingSystemAppsRestricted]_block_invoke.238
- ___63-[SBLockScreenManager lockUIFromSource:withOptions:completion:]_block_invoke.204
- ___63-[SBStripContinuousExposeSwitcherModifier anchorPointForIndex:]_block_invoke
- ___63-[SBStripContinuousExposeSwitcherModifier anchorPointForIndex:]_block_invoke.7
- ___63-[SBStripContinuousExposeSwitcherModifier anchorPointForIndex:]_block_invoke.cold.1
- ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.324
- ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.324.cold.1
- ___65-[SBFluidSwitcherViewController _reevaluateWindowManagementStyle]_block_invoke.903
- ___65-[SBVideoOutController _startVideoOutBackgroundActivityAssertion]_block_invoke
- ___65-[SBVideoOutController _startVideoOutBackgroundActivityAssertion]_block_invoke.43
- ___65-[SBVideoOutController _startVideoOutBackgroundActivityAssertion]_block_invoke_2
- ___69-[SBIconController _performWidgetMigrationIfNecessaryForApplication:]_block_invoke.358
- ___69-[SBIconController _performWidgetMigrationIfNecessaryForApplication:]_block_invoke.359
- ___70-[SBVideoOutController updateScreenSharingBackgroundActivityAssertion]_block_invoke.36
- ___70-[SBVideoOutController updateScreenSharingBackgroundActivityAssertion]_block_invoke_2
- ___72-[SBFluidSwitcherGestureManager _setUpChamoisGestureRecognizersIfNeeded]_block_invoke
- ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.367
- ___76-[SBCommandTabController viewController:selectedApplicationWithDisplayItem:]_block_invoke.64
- ___79-[SBMainWorkspace _removeApplicationEntities:withDestructionIntent:completion:]_block_invoke.457
- ___80-[SBFluidSwitcherGestureManager _configureFloatingApplicationGestureRecognizers]_block_invoke
- ___80-[SBFluidSwitcherGestureManager configureIndirectBottomEdgePanGestureRecognizer]_block_invoke
- ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.402
- ___83-[SBIconController _obtainSmartStackForWidgetDiscoverabilityWithCompletionHandler:]_block_invoke.334
- ___83-[SBIconController _obtainSmartStackForWidgetDiscoverabilityWithCompletionHandler:]_block_invoke.336
- ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke.24
- ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke_2.25
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1450
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1452
- ___94-[SBActivitySystemApertureElementObserver _invalidateSystemApertureElementForItem:completion:]_block_invoke.68
- ___94-[SBActivitySystemApertureElementObserver _invalidateSystemApertureElementForItem:completion:]_block_invoke_2.69
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.599
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.617
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.632
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.634
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.642
- ___96-[SBSystemShellExtendedDisplayControllerPolicy connectToDisplayController:displayConfiguration:]_block_invoke.61
- ___96-[SBSystemShellExtendedDisplayControllerPolicy connectToDisplayController:displayConfiguration:]_block_invoke.65
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1575
- ___block_descriptor_40_e5_d8?0l
- ___block_literal_global.1042
- ___block_literal_global.1045
- ___block_literal_global.1050
- ___block_literal_global.1056
- ___block_literal_global.1159
- ___block_literal_global.1204
- ___block_literal_global.1347
- ___block_literal_global.1457
- ___block_literal_global.1466
- ___block_literal_global.1468
- ___block_literal_global.1470
- ___block_literal_global.1472
- ___block_literal_global.1488
- ___block_literal_global.1601
- ___block_literal_global.1625
- ___block_literal_global.1634
- ___block_literal_global.1651
- ___block_literal_global.213
- ___block_literal_global.243
- ___block_literal_global.251
- ___block_literal_global.284
- ___block_literal_global.364
- ___block_literal_global.393
- ___block_literal_global.409
- ___block_literal_global.411
- ___block_literal_global.416
- ___block_literal_global.417
- ___block_literal_global.42
- ___block_literal_global.420
- ___block_literal_global.425
- ___block_literal_global.456
- ___block_literal_global.458
- ___block_literal_global.460
- ___block_literal_global.482
- ___block_literal_global.686
- ___block_literal_global.706
- ___block_literal_global.719
- ___block_literal_global.728
- ___block_literal_global.730
- ___block_literal_global.732
- ___block_literal_global.734
- ___block_literal_global.736
- ___block_literal_global.745
- ___block_literal_global.752
- ___block_literal_global.757
- ___block_literal_global.759
- ___block_literal_global.797
- ___block_literal_global.874
- ___block_literal_global.958
- ___block_literal_global.990
- __unnamed_array_storage.105
- __unnamed_array_storage.118
- __unnamed_array_storage.1598
- __unnamed_array_storage.1738
- __unnamed_array_storage.1747
- __unnamed_array_storage.375
- __unnamed_array_storage.378
- __unnamed_array_storage.381
- __unnamed_array_storage.446
- __unnamed_array_storage.461
- __unnamed_array_storage.476
- __unnamed_array_storage.492
- __unnamed_array_storage.498
- __unnamed_array_storage.504
- __unnamed_array_storage.510
- __unnamed_array_storage.525
- __unnamed_array_storage.531
- __unnamed_array_storage.537
- __unnamed_array_storage.743
- __unnamed_array_storage.752
- __unnamed_array_storage.80
- __unnamed_array_storage.97
- _objc_msgSend$_addBlurFilterToLayer:withBlurRadius:
- _objc_msgSend$_addContentViewControllerToPIPHierarchy:contentViewLayoutSettings:
- _objc_msgSend$_alphaForStateIdleOn
- _objc_msgSend$_animateLayer:forKeyPath:fromValue:toValue:persistingToValue:duration:
- _objc_msgSend$_clearScreenSharingBackgroundActivityAssertion
- _objc_msgSend$_clearVideoOutBackgroundActivityAssertion
- _objc_msgSend$_configureClickDownToBringItemContainerForwardGesture
- _objc_msgSend$_configureFloatingApplicationGestureRecognizers
- _objc_msgSend$_configureRootLayer
- _objc_msgSend$_configureScrunchGesture
- _objc_msgSend$_configureTapToBringItemContainerForwardGesture
- _objc_msgSend$_interchangesViewAndLayer
- _objc_msgSend$_resizeGrabberPathForSize:curve:lineWidth:rotation:
- _objc_msgSend$_screenTypeForcesFastFadeAnimations
- _objc_msgSend$_setUpChamoisGestureRecognizersIfNeeded
- _objc_msgSend$_shouldForceViewToShowForBacklightLuminance:
- _objc_msgSend$_shouldForceViewToShowForCurrentBacklightLuminance
- _objc_msgSend$_shouldSwapActivityItem:withOtherItem:
- _objc_msgSend$_sizeForStateIdleOn
- _objc_msgSend$_springAnimationForKeyPath:fromValue:toValue:duration:
- _objc_msgSend$_startVideoOutBackgroundActivityAssertion
- _objc_msgSend$_stopAllAnimations
- _objc_msgSend$_supportsFloatingApplicationForSwitcherController:
- _objc_msgSend$_swapItemWithRegisteredItemIfNecessary:
- _objc_msgSend$_tearDownChamoisGestureRecognizersIfNeeded
- _objc_msgSend$_updateHardwareKeyboardAttached
- _objc_msgSend$_updateIndicatorForBacklightLuminance:previousBacklightLuminance:
- _objc_msgSend$_updateIndicatorLayerSize:opacity:
- _objc_msgSend$_updateIndicatorLayerWithBounds:andCenter:
- _objc_msgSend$_updateIndicatorViewSize:alpha:
- _objc_msgSend$_updateIndicatorVisibilityWithSpringAnimation:
- _objc_msgSend$_updateScreenSharingBackgroundActivityAssertionSuppressionPreference:
- _objc_msgSend$_updateToOrientation:
- _objc_msgSend$_updateVideoOutBackgroundActivityAssertion
- _objc_msgSend$_usesSpringAnimations
- _objc_msgSend$calculateInitialIndicatorPositionAndSize
- _objc_msgSend$configureIndirectBottomEdgePanGestureRecognizer
- _objc_msgSend$fluidSwitcherGestureManagerSupportsFloatingApplication:
- _objc_msgSend$initForLocation:
- _objc_msgSend$initWithExternalDisplayDefaults:externalDisplayService:mousePointerManager:runtimeAvailabilitySettings:sceneManager:
- _objc_msgSend$initWithExternalDisplayService:externalDisplayDefaults:mousePointerManager:runtimeAvailabilitySettings:sceneManager:
- _objc_msgSend$initWithSceneHandle:workspace:bannerManager:lockScreenManager:deactivationManager:mainSwitcherCoordinator:backlightController:keyboardFocusController:springBoard:setupManager:uiController:pipCoordinator:
- _objc_msgSend$setActiveInterfaceOrientation:
- _objc_msgSend$setIndicatorState:
- _objc_msgSend$setLineCapStyle:
- _objc_msgSend$setLineJoinStyle:
- _objc_msgSend$shouldPlayLockSound
CStrings:
+ "\x01\x1b"
+ "\x01b3\x18\x13\x15\x12\x1b\x17O\x01\x15\x1a\x1f\x03\x19\x18\x1f\x0f\a"
+ "\x02\x17"
+ "\x03Q\x14\x13\x13\x12\"!\x11"
+ "\x04?\x05S!\x15\x14\x1c\x7f\x03\x16\x111/\v\x14"
+ "\n\x1e:A1"
+ "\f\x14\x11"
+ "\x0f\x01\x1f\x0f\x05\x159\x13\x1f\x06\x14'\x11"
+ "\x11\x1f\r"
+ "\x19\x14\x11\x11\x11"
+ "%@ is empty! %@"
+ "(%{public}@) Disallowing action (%{public}@); action: %{private}@"
+ "(%{public}@) Error unarchiving squeeze action: %{public}@"
+ "(%{public}@) No archived squeeze action found"
+ "(%{public}@) Selecting squeeze action %{private}@"
+ "(%{public}@) found active runner %{public}@ to use for action: %{private}@"
+ "(%{public}@) performing action '%{private}@' with runner client '%{public}@'"
+ "(%{public}@) requested to perform action with timestamp: %{public}@"
+ "(%{public}@) runner '%{public}@' did finish successfully: %{BOOL}u\n    cancelled: %{BOOL}u\n    error: %{public}@"
+ "(%{public}@) skipping finished result from no-longer-tracked runner client '%{public}@'"
+ "(unknown %lu)"
+ "17.5"
+ "@\"<SBAttentionAwarenessStreamerClientDelegate>\""
+ "@\"<SBSHomeScreenConfigurationServerDelegate>\""
+ "@\"<SBScreenLongevityTimerDelegate>\""
+ "@\"CASecureIndicatorLayer\""
+ "@\"SBApplicationRestrictionMonitoringServer\""
+ "@\"SBAttentionAwarenessStreamerClient\""
+ "@\"SBHomeScreenConfigurationManager\""
+ "@\"SBHomeScreenConfigurationServer\""
+ "@\"SBIcon\"16@?0@\"SBSHomeScreenItem\"8"
+ "@\"SBPencilDefaults\""
+ "@\"SBPencilSqueezeActionControl\""
+ "@\"SBScreenLongevitySettings\""
+ "@\"SBScreenLongevityTimer\""
+ "@\"UIPencilInteraction\""
+ "@\"WFConfiguredSystemAction\""
+ "AWFaceDetectAttentionEvent"
+ "AmbientAdaptiveDimming"
+ "AmbientAdaptiveDimmingEnable"
+ "AmbientAdaptiveDimmingPeriod"
+ "App restriction update will occur. Tracking with ID=%@"
+ "App restriction update with ID=%@ was ingested by restriction observers. Now waiting for %lu outstanding assertions…"
+ "App visibility updates will be treated as transient. Updating icon model store."
+ "App visibility updates will no longer be treated as transient. Updating icon model store."
+ "Attention Score Threshold"
+ "Attention awarenesss feature enablement changed"
+ "B16@?0@\"<SBFSensorActivityAttribution>\"8"
+ "B16@?0@\"SBActivityAlert\"8"
+ "B16@?0@\"WFPencilSqueezeWorkflowRunnerClient\"8"
+ "BNSceneClientSettings"
+ "Back light adaptive dimming enable -> %u"
+ "Beginning configuration session"
+ "CABackdropLayer"
+ "CBBrightnessIsUnderAutoDimThreshold"
+ "Configured new connection: %{public}@"
+ "Core Brightness"
+ "Creating icon for app with bundle identifier: %{public}@"
+ "Debug"
+ "Delay Before Fade-in"
+ "Delay Before Fade-out"
+ "Dim Duration"
+ "Dim timer expire with a valid undim timer"
+ "Dim timer remains valid after expire"
+ "Dimming Animation Length"
+ "Dimming timer invalidate %{public}@"
+ "Dimming timer start %{public}@"
+ "Dimming timer start face detection %{public}@"
+ "Enable, old dim timer still valid"
+ "Enablement"
+ "Enablement Overrides"
+ "Ending configuration session"
+ "Error building custom display mode: %{public}@"
+ "Face Detection Score"
+ "Face Detection Score Threshold"
+ "Fade-in Duration"
+ "Fade-out Duration"
+ "Failed to construct focus mode from configuration: icon model was nil"
+ "Finished configuring %ld pages, %ld unused pages will be deleted"
+ "Firing switcher haptic for type %ld, senderID %llu"
+ "Ignore Auto Lock Set To Never"
+ "In dimmed state without a valid undim timer"
+ "In undimmed state with a valid undim timer"
+ "In undimmed state without a valid dim timer"
+ "ManagedConfiguration policy states: no command-tab allowed"
+ "ManagedConfiguration policy states: no control center"
+ "ManagedConfiguration policy states: no home screen editing"
+ "ManagedConfiguration policy states: no spotlight"
+ "Management configuration profile settings updated"
+ "Media now playing state changed"
+ "Minimal Face Detection Time Interval"
+ "No Op But Log When Enablement Update"
+ "Noisy Logging"
+ "Notified %{public}ld active connection(s) of restrictions update"
+ "Outstanding layout work for switcher"
+ "Override Enablement"
+ "Override Sensor State"
+ "PencilSqueeze"
+ "Pending application restriction controller app visibility update broadcast"
+ "Pending restriction update compound assertion with ID=%@ was finally invalidated"
+ "PolicyChangedDismissalAnimation"
+ "Profile connection settings changed, isWallpaperAllowed: %{bool}u"
+ "Received configuration %{public}@"
+ "Received connection invalidation: %{public}@"
+ "Removing connection: %{public}@"
+ "Reset for user attention: %@"
+ "Restore"
+ "SBApplicationRestrictionMonitoringServer"
+ "SBApplicationRestrictionMonitoringServer.pendingRestrictionUpdate.%@"
+ "SBAttentionAwarenessStreamerClient"
+ "SBAttentionAwarenessStreamerClientDelegate"
+ "SBHomeScreenConfigurationManager"
+ "SBHomeScreenConfigurationServer"
+ "SBPencilSqueezeActionControl"
+ "SBPencilSqueezeActionControl.m"
+ "SBReadOnlyDefaultIconModelStore"
+ "SBSHomeScreenConfigurationClientToServerInterface"
+ "SBSHomeScreenConfigurationServerDelegate"
+ "SBScreenLongevityController"
+ "SBScreenLongevityDomain"
+ "SBScreenLongevitySettings"
+ "SBScreenLongevityTimer"
+ "SBScreenLongevityTimerDelegate"
+ "SBSystemGestureManager did receive pencil squeeze"
+ "Screen Longevity"
+ "Screen backlight state changed"
+ "ScreenLongevityController"
+ "Sensor activity updated"
+ "SpringBoardShouldConsiderAppAllowlistAsTransient"
+ "Start undim timer"
+ "SystemGesturePencilSqueeze"
+ "T@\"<BSInvalidatable>\",&,N,V_restrictionControllerDidFinishNotifyingObserversAssertion"
+ "T@\"<SBAttentionAwarenessStreamerClientDelegate>\",W,N,V_delegate"
+ "T@\"<SBScreenLongevityTimerDelegate>\",W,N,V_delegate"
+ "T@\"BSCompoundAssertion\",&,N,V_pendingRestrictionUpdateAssertion"
+ "T@\"NSMutableArray\",R,N,V_connections"
+ "T@\"NSSet\",?,R,C,N"
+ "T@\"NSUUID\",&,N,V_pendingRestrictionUpdateUUID"
+ "T@\"SBPencilSqueezeActionControl\",R,N,V_pencilSqueezeActionControl"
+ "TB,N,V_enablement"
+ "TB,N,V_ignoreAutoLockSetToNever"
+ "TB,N,V_noOpButLogOnEnablementUpdate"
+ "TB,N,V_noisyLogging"
+ "TB,N,V_overrideEnablement"
+ "TB,R,N,G_supportsSecureIndicator"
+ "Td,N,V_attentionScoreThreshold"
+ "Td,N,V_dimmingAnimationLength"
+ "Td,N,V_faceDetectionScoreThreshold"
+ "Td,N,V_minimalFaceDetectionInterval"
+ "Td,N,V_touchAttentionLostTimeout"
+ "Td,N,V_undimFaceDetectionInterval"
+ "Td,N,V_undimmingAnimationLength"
+ "Td,N,V_waitInterval"
+ "Td,V_delayBeforeFadeIn180"
+ "Td,V_delayBeforeFadeIn90"
+ "Td,V_delayBeforeFadeOut180"
+ "Td,V_delayBeforeFadeOut90"
+ "Td,V_fadeInDuration180"
+ "Td,V_fadeInDuration90"
+ "Td,V_fadeOutDuration180"
+ "Td,V_fadeOutDuration90"
+ "Tearing down focus mode and restoring original state"
+ "Touch Attention Lost Timeout"
+ "Tq,R,N,V_activeInterfaceOrientation"
+ "Unable to create app icon for suggested bundle identifier: %{public}@"
+ "Undim Face Detection Time Interval"
+ "Undimming Animation Length"
+ "Unsupported home screen item type: %{public}@"
+ "Using read-only variant of default icon model store because app allowlist is being treated as transient"
+ "Wait Duration Before Face Detection Kicks In"
+ "[ActivityID: %{public}@] removed from pending alert for this item"
+ "[Recording Indicator] updating secure indicator type for layer-dot to %@"
+ "[Recording Indicator] updating secure indicator type for view-dot to %@"
+ "[Swapping Activity: %{public}@, Swapped Activity: %{public}@] Checking relevance scores for swapping decision: Swapping Activity Relevance Score: %f, Swapped Activity Relevance Score: %f"
+ "[Swapping Activity: %{public}@, Swapped Activity: %{public}@] Not swapping because items can't be found"
+ "[Swapping Activity: %{public}@, Swapped Activity: %{public}@] Not swapping items because bundle identifiers doesn't match"
+ "[Swapping Activity: %{public}@, Swapped Activity: %{public}@] Not swapping items because no element found for registered item"
+ "[Swapping Activity: %{public}@, Swapped Activity: %{public}@] Swapping items because alert is pending"
+ "_addContentViewControllerToPIPHierarchy:contentViewLayoutSettings:animated:"
+ "_analyticsLoggingForDisplayZoomMode"
+ "_applicationRestrictionMonitoringServer"
+ "_applicationRestrictionUpdatePendingAssertion"
+ "_attentionAwarenessFeatureMonitoringToken"
+ "_attentionScoreThreshold"
+ "_beginMonitoringAttentionAwarenessFeaturesEnablement"
+ "_cachedOrFallbackFrameForIndex:cacheValidityToken:"
+ "_cachedOrFallbackScaleForIndex:cacheValidityToken:"
+ "_checkFaceAttentionAwareness"
+ "_classicModeReplacingMoreSpaceWithEquivalentStandardCanvasForClassicMode:"
+ "_clientDidResetForUserAttention:"
+ "_configurationSessionConnection"
+ "_createRecordingIndicatorForSecureIndicator"
+ "_currentFaceDetectionTimerInterval"
+ "_defaultsObserver"
+ "_delayBeforeFadeIn180"
+ "_delayBeforeFadeIn90"
+ "_delayBeforeFadeOut180"
+ "_delayBeforeFadeOut90"
+ "_dim"
+ "_dimTimer"
+ "_dimmingAnimationLength"
+ "_effectiveSettingsChangedNotification:"
+ "_enablement"
+ "_endMonitoringAttentionAwarenessFeaturesEnablement"
+ "_faceDetectionScoreThreshold"
+ "_faceStreamAwarenessClient"
+ "_faceStreamAwarenessConfiguration"
+ "_fadeInDuration180"
+ "_fadeInDuration90"
+ "_fadeOutDuration180"
+ "_fadeOutDuration90"
+ "_grabberCurve"
+ "_grabberPath"
+ "_grabberPathForLength:curve:rotation:"
+ "_grabberRotation"
+ "_hasCameraAttributions"
+ "_hasPlayedSoundForLock"
+ "_hideSpotlightOnPolicyChange"
+ "_homeScreenConfigurationManager"
+ "_iconModel:wantsToRevealAnyApplicationFromIdentifiers:"
+ "_idleTouchAwarenessConfiguration"
+ "_ignoreAutoLockSetToNever"
+ "_isAppAllowlistActiveAndTransient"
+ "_isAutoLockSetToNever"
+ "_isDimmed"
+ "_isProximityReaderPresented"
+ "_isValidCurrentTimer:"
+ "_lockoutStateProvider"
+ "_main_clearScreenSharingBackgroundActivityAssertion"
+ "_main_clearVideoOutBackgroundActivityAssertion"
+ "_main_startVideoOutBackgroundActivityAssertion"
+ "_main_updateScreenSharingBackgroundActivityAssertion"
+ "_main_updateScreenSharingBackgroundActivityAssertionSuppressionPreference:"
+ "_main_updateVideoOutBackgroundActivityAssertion"
+ "_managedConfigurationEffectiveSettingsDidChange:"
+ "_mediaNowPlayingChanged"
+ "_minimalFaceDetectionInterval"
+ "_nativeBounds"
+ "_noOpButLogOnEnablementUpdate"
+ "_noisyLogging"
+ "_observeDefaults"
+ "_overrideEnablement"
+ "_pencilInteraction:didReceiveSqueeze:"
+ "_pencilSqueezeActionControl"
+ "_pendingRestrictionUpdateAssertion"
+ "_pendingRestrictionUpdateUUID"
+ "_pillViewContainerView"
+ "_pillViewContainerViewFrame"
+ "_pillViewContainerViewOffset"
+ "_playLockSound couldn't play the lock sound"
+ "_pointerRegionRect"
+ "_policyAggregatorCapabilitiesDidChange:"
+ "_preferredSqueezeAction"
+ "_privateNotificationOccurred:atLocation:senderID:"
+ "_requiredHardwareAvailable"
+ "_restrictionControllerDidFinishNotifyingObserversAssertion"
+ "_restrictionMonitoringServer"
+ "_runningRunnerClients"
+ "_screenBacklightStateChanged"
+ "_setUpChamoisGestureRecognizers"
+ "_setUpFloatingApplicationGestureRecognizers"
+ "_setUpScrunchGestureRecognizerIfNeeded"
+ "_shouldEnable"
+ "_shouldPlayLockSound"
+ "_shouldSwapActivityItem:withOtherItem:itemAlerting:"
+ "_standardCanvasSizeForClassicMode:"
+ "_startDimTimer"
+ "_supportsSecureIndicator"
+ "_swapItemWithRegisteredItemIfNecessary:itemAlerting:"
+ "_systemPencilInteraction"
+ "_tearDownChamoisGestureRecognizers"
+ "_tearDownFloatingApplicationGestureRecognizers"
+ "_toggleBacklightAdaptiveDimming:"
+ "_touchAttentionLostTimeout"
+ "_undim"
+ "_undimFaceDetectionInterval"
+ "_undimTimer"
+ "_undimmingAnimationLength"
+ "_updateCachedDefaults"
+ "_updateChamoisGestureRecognizerPresenceForWindowManagementStyle:"
+ "_updateFloatingApplicationGestureRecognizerPresenceForWindowManagementStyle:"
+ "_updateFluidDragAndDropManagerPresenceForWindowManagementStyle:"
+ "_updateGrabberPathAnimated:"
+ "_updateIndirectBottomEdgePanGesturePresence"
+ "_updateScenesForPointerWithHardwareAttached:"
+ "_waitInterval"
+ "_wantsDisplayLayoutElement"
+ "acquireApplicationRestrictionUpdatePendingAssertionForReason:"
+ "addAdditionalIconMatchingIcon:"
+ "allAllowedAppBundleIdentifiers"
+ "allRestrictedAppBundleIdentifiers"
+ "appLayoutContainsFullScreenDisplayItem:"
+ "appResizeGesture"
+ "appSwitcher"
+ "applicationRestrictionControllerDidPostAppVisibilityUpdate:"
+ "applicationRestrictionControllerWillPostAppVisibilityUpdate:"
+ "applyConfiguration:completion:"
+ "attentionScore"
+ "attentionScoreThreshold"
+ "beginConfigurationSessionWithCompletion:"
+ "com.apple.SpringBoard.SBHomeScreenConfigurationServer.queue"
+ "com.apple.springboard.AttentionAwareStreamerQueue"
+ "com.apple.springboard.SBApplicationRestrictionMonitoringServer.queue"
+ "com.apple.springboard.application-restriction-monitoring"
+ "com.apple.springboard.home-screen-configuration"
+ "com.apple.springboard.homeScreenConfigurationService.configuration"
+ "configurationServer:didReceiveConfiguration:completion:"
+ "configurationServerDidBeginConfigurationSession:completion:"
+ "configurationServerDidEndConfigurationSession:completion:"
+ "copyPropertyForKey:"
+ "d32@0:8Q16@24"
+ "delayBeforeFadeIn180"
+ "delayBeforeFadeIn90"
+ "delayBeforeFadeOut180"
+ "delayBeforeFadeOut90"
+ "descriptorWithGenericGestureType:"
+ "device is proximity reader blocked out"
+ "didn't play lock sound, have already played sound for this locking"
+ "dimTimerDidExpireForTimer:"
+ "dimTimerFired"
+ "dimmingAnimationLength"
+ "dockItems"
+ "dockList"
+ "donateFocusMode:fromSource:"
+ "dragAndDrop"
+ "elapsedTime"
+ "enablement"
+ "endConfigurationSessionWithCompletion:"
+ "entityCreationAnimation"
+ "entityRemovalAnimation"
+ "evaluateEnablement"
+ "faceDetectionScore"
+ "faceDetectionScoreThreshold"
+ "faceDetectionTimerDidExpire:"
+ "faceStreamAwarenessConfiguration"
+ "fadeInDuration180"
+ "fadeInDuration90"
+ "fadeOutDuration180"
+ "fadeOutDuration90"
+ "ignoreAutoLockSetToNever"
+ "indexPathForIcon:includingPlaceholders:"
+ "initForLocation:windowScene:"
+ "initWithAllowedIdentifiers:restrictedIdentifiers:"
+ "initWithCorner:cornerRadius:"
+ "initWithExternalDisplayDefaults:appSwitcherDefaults:externalDisplayService:mousePointerManager:runtimeAvailabilitySettings:sceneManager:windowSceneManager:"
+ "initWithExternalDisplayService:externalDisplayDefaults:appSwitcherDefaults:mousePointerManager:runtimeAvailabilitySettings:sceneManager:windowSceneManager:"
+ "initWithFloat:"
+ "initWithInt:"
+ "initWithSceneHandle:workspace:bannerManager:lockScreenManager:deactivationManager:mainSwitcherCoordinator:backlightController:keyboardFocusController:springBoard:setupManager:uiController:pipCoordinator:lockoutStateProvider:"
+ "initWithSystemAction:preciseTimeStamp:"
+ "invalidateRestrictionCache"
+ "isAdaptiveDimmingEnabled"
+ "isAllowlistActiveAndTransient"
+ "isAutoDimAllowed"
+ "isBeingShownAboveCoverSheet"
+ "isCommandTabAllowed"
+ "isControlCenterAllowed"
+ "isHomeScreenEditingAllowed"
+ "isSpotlightAllowed"
+ "isUnderAutoDimThreshold"
+ "isWallpaperAllowed"
+ "magic keyboard (extended wake)"
+ "mediaType"
+ "minimalFaceDetectionInterval"
+ "moveFloatingApplicationGesture"
+ "no action to perform"
+ "noOpButLogOnEnablementUpdate"
+ "noisyLogging"
+ "nubHidden"
+ "observePrefersLockedIdleDurationOnCoversheet:"
+ "observeUpdateWithApplicationRestrictState:"
+ "overrideEnablement"
+ "pencilDefaults"
+ "pencilInteraction:didReceiveSqueeze:"
+ "pencilInteraction:didReceiveTap:"
+ "pencilSqueezeActionControl"
+ "pendingRestrictionUpdateAssertion"
+ "pendingRestrictionUpdateUUID"
+ "performSqueezeActionWithTimestamp:"
+ "playLockSoundIfPermitted"
+ "playingMediaType"
+ "prefersLockedIdleDurationOnCoversheet"
+ "privacyIndicatorType"
+ "reevaluateMirroringEnablement"
+ "registerNotificationBlock:forProperties:"
+ "removeList:"
+ "resetTimerForReason:"
+ "restrictionControllerDidFinishNotifyingObserversAssertion"
+ "sceneOverlay"
+ "scheduleFaceDetection"
+ "screen-longevity-face-stream"
+ "screen-longevity-idle-touch"
+ "screenLongevityDefaults"
+ "set enabled -> %{BOOL}u"
+ "setActiveInterfaceOrientation:withDuration:"
+ "setAdaptiveDimmingEnabled:"
+ "setAttentionScoreThreshold:"
+ "setContinuousFaceDetectMode:"
+ "setDelayBeforeFadeIn180:"
+ "setDelayBeforeFadeIn90:"
+ "setDelayBeforeFadeOut180:"
+ "setDelayBeforeFadeOut90:"
+ "setDimmingAnimationLength:"
+ "setDockList:"
+ "setEnablement:"
+ "setEventStreamerWithQueue:block:"
+ "setFaceDetectionScoreThreshold:"
+ "setFadeInDuration180:"
+ "setFadeInDuration90:"
+ "setFadeOutDuration180:"
+ "setFadeOutDuration90:"
+ "setIcons:"
+ "setIgnoreAutoLockSetToNever:"
+ "setMinimalFaceDetectionInterval:"
+ "setNoOpButLogOnEnablementUpdate:"
+ "setNoisyLogging:"
+ "setOverrideEnablement:"
+ "setPendingRestrictionUpdateAssertion:"
+ "setPendingRestrictionUpdateUUID:"
+ "setPrivacyIndicatorType:"
+ "setRestrictionControllerDidFinishNotifyingObserversAssertion:"
+ "setTouchAttentionLostTimeout:"
+ "setUndimFaceDetectionInterval:"
+ "setUndimmingAnimationLength:"
+ "setUnityStream:"
+ "setWaitInterval:"
+ "shouldEnable=%{BOOL}u from override"
+ "shouldEnable=%{BOOL}u, isDeviceAllowedByManagedConfiguration=%{BOOL}u, isCameraInUse=%{BOOL}u, isAutoLockDisabled=%{BOOL}u, shouldIgnoreAutoLockDisable=%{BOOL}u, isMediaNowPlaying=%{BOOL}u, isProbablyAudioOnly=%{BOOL}u, isIdleTimerDisabledByMediaPlayback=%{BOOL}u, isIdleTimerOffForAnyReason=%{BOOL}u isAutoDimThresholdPassed=%{BOOL}u"
+ "speedMultiplierForMagicKeyboardExtended"
+ "squeezeConfiguredActionArchive"
+ "startFaceDetection"
+ "startWithPreciseTimeStamp:"
+ "streamerClientDidResetForUserAttention:"
+ "supportsSecureIndicator"
+ "touchAttentionLostTimeout"
+ "trackpadSwitcherGesturesEnabled"
+ "undimFaceDetectionInterval"
+ "undimmingAnimationLength"
+ "updateHardwareKeyboardAttached"
+ "v24@0:8@\"SBApplicationRestrictionController\"16"
+ "v24@0:8@\"SBAttentionAwarenessStreamerClient\"16"
+ "v24@0:8@\"SBScreenLongevityTimer\"16"
+ "v24@?0@\"NSString\"8@16"
+ "v32@0:8@\"SBHomeScreenConfigurationServer\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"SBSHomeScreenConfiguration\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@\"UIPencilInteraction\"16@\"UIPencilInteractionSqueeze\"24"
+ "v32@0:8@\"UIPencilInteraction\"16@\"UIPencilInteractionTap\"24"
+ "v32@0:8@\"UIPencilInteraction\"16@\"_UIPencilInteractionSqueeze\"24"
+ "v40@0:8@\"SBHomeScreenConfigurationServer\"16@\"SBSHomeScreenConfiguration\"24@?<v@?@\"NSError\">32"
+ "waitInterval"
+ "wakeAnimationStyle"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8Q16@24"
+ "\xf0B"
+ "\xf0Q\x11"
+ "\xf0\xa1a\x12"
+ "\xf0\xf0\xa11!"
+ "\xf0\xf0\xf0\xf0\xa1"
+ "\xf0\xf0\xf0\xf0\xf0\xf0r!\xf0\xb1"
- "\x01\x1a"
- "\x01b3\x18\x13%\x12\x1b\x17O\x01\x15\x1a\x1f\x03\x19\x17\x1f\x0f\a"
- "\x03Q\x14\x13\x15\"!\x11"
- "\x04?\x05S!\x15\x14\x1c\x7f\x03\x161/\v\x14"
- "\n\x1d:A1"
- "\f\x13\x11"
- "\x0f\x01\x1f\x0f\n9\x13\x1f\x06\x14'\x11"
- "\x11\x1f\f"
- "\x17\x14\x11\x11\x11"
- "@56@0:8{CGSize=dd}16d32d40d48"
- "B24@0:8@\"SBFluidSwitcherGestureManager\"16"
- "Reloading and rendering all application icons."
- "TB,N,V_didPlayLockSound"
- "Tq,N,V_activeInterfaceOrientation"
- "ZULU %@ is empty! %@"
- "_addBlurFilterToLayer:withBlurRadius:"
- "_addContentViewControllerToPIPHierarchy:contentViewLayoutSettings:"
- "_alphaForStateIdleOn"
- "_animateLayer:forKeyPath:fromValue:toValue:persistingToValue:duration:"
- "_clearScreenSharingBackgroundActivityAssertion"
- "_clearVideoOutBackgroundActivityAssertion"
- "_configureClickDownToBringItemContainerForwardGesture"
- "_configureFloatingApplicationGestureRecognizers"
- "_configureRootLayer"
- "_configureScrunchGesture"
- "_configureTapToBringItemContainerForwardGesture"
- "_didPlayLockSound"
- "_interchangesViewAndLayer"
- "_maskPath"
- "_resizeGrabberPathForSize:curve:lineWidth:rotation:"
- "_screenTypeForcesFastFadeAnimations"
- "_setUpChamoisGestureRecognizersIfNeeded"
- "_shouldForceViewToShowForBacklightLuminance:"
- "_shouldForceViewToShowForCurrentBacklightLuminance"
- "_shouldSwapActivityItem:withOtherItem:"
- "_sizeForStateIdleOn"
- "_springAnimationForKeyPath:fromValue:toValue:duration:"
- "_startVideoOutBackgroundActivityAssertion"
- "_stopAllAnimations"
- "_supportsFloatingApplicationForSwitcherController:"
- "_swapItemWithRegisteredItemIfNecessary:"
- "_tearDownChamoisGestureRecognizersIfNeeded"
- "_updateHardwareKeyboardAttached"
- "_updateIndicatorForBacklightLuminance:previousBacklightLuminance:"
- "_updateIndicatorLayerSize:opacity:"
- "_updateIndicatorLayerWithBounds:andCenter:"
- "_updateIndicatorViewSize:alpha:"
- "_updateIndicatorVisibilityWithSpringAnimation:"
- "_updateScreenSharingBackgroundActivityAssertionSuppressionPreference:"
- "_updateToOrientation:"
- "_updateVideoOutBackgroundActivityAssertion"
- "_userMirroringPreference"
- "_usesSpringAnimations"
- "calculateInitialIndicatorPositionAndSize"
- "configureIndirectBottomEdgePanGestureRecognizer"
- "didPlayLockSound"
- "fluidSwitcherGestureManagerSupportsFloatingApplication:"
- "group frame not in cache"
- "initForLocation:"
- "initWithExternalDisplayDefaults:externalDisplayService:mousePointerManager:runtimeAvailabilitySettings:sceneManager:"
- "initWithExternalDisplayService:externalDisplayDefaults:mousePointerManager:runtimeAvailabilitySettings:sceneManager:"
- "initWithSceneHandle:workspace:bannerManager:lockScreenManager:deactivationManager:mainSwitcherCoordinator:backlightController:keyboardFocusController:springBoard:setupManager:uiController:pipCoordinator:"
- "setActiveInterfaceOrientation:"
- "setDidPlayLockSound:"
- "setIndicatorState:"
- "setLineCapStyle:"
- "setLineJoinStyle:"
- "shouldPlayLockSound"
- "v60@0:8@16@24@32@40B48d52"
- "v64@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGPoint=dd}48"
- "\xf02"
- "\xf0\x91a\x12"
- "\xf0\xf0\x911!"
- "\xf0\xf0\xf0\xf0\x91"
- "\xf0\xf0\xf0\xf0\xf0\xf0R!\xf0\xb1"

```
