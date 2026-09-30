## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-  __TEXT.__text: 0xae8878
+  __TEXT.__text: 0xaf3d70
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xbbbf8
-  __TEXT.__const: 0x11250
-  __TEXT.__cstring: 0x83663
-  __TEXT.__oslogstring: 0x61caf
-  __TEXT.__gcc_except_tab: 0x181c0
+  __TEXT.__objc_methlist: 0xbc5e8
+  __TEXT.__const: 0x112a0
+  __TEXT.__oslogstring: 0x6286e
+  __TEXT.__cstring: 0x83fbd
+  __TEXT.__gcc_except_tab: 0x1823c
   __TEXT.__ustring: 0xd04
   __TEXT.__dlopen_cstrs: 0x373
-  __TEXT.__unwind_info: 0x2de40
+  __TEXT.__unwind_info: 0x2e090
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d550
-  __DATA_CONST.__objc_classlist: 0x5420
+  __DATA_CONST.__const: 0x1d6a8
+  __DATA_CONST.__objc_classlist: 0x5450
   __DATA_CONST.__objc_catlist: 0x338
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2a80
+  __DATA_CONST.__objc_protolist: 0x2a90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4daf0
-  __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x4010
-  __DATA_CONST.__objc_arraydata: 0x18c0
-  __DATA_CONST.__got: 0xa860
-  __AUTH_CONST.__const: 0x109f8
-  __AUTH_CONST.__cfstring: 0x73160
-  __AUTH_CONST.__objc_const: 0x2824c8
+  __DATA_CONST.__objc_selrefs: 0x4df50
+  __DATA_CONST.__objc_protorefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0x4030
+  __DATA_CONST.__objc_arraydata: 0x18a0
+  __DATA_CONST.__got: 0xa8c0
+  __AUTH_CONST.__const: 0x10ad8
+  __AUTH_CONST.__cfstring: 0x73a40
+  __AUTH_CONST.__objc_const: 0x283c68
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1758
-  __AUTH_CONST.__objc_doubleobj: 0x800
+  __AUTH_CONST.__objc_doubleobj: 0x820
   __AUTH_CONST.__objc_intobj: 0x2c88
-  __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH_CONST.__auth_got: 0x2b78
-  __AUTH.__objc_data: 0xfa00
-  __DATA.__objc_ivar: 0xf960
-  __DATA.__data: 0x20b10
-  __DATA.__bss: 0xb20
+  __AUTH_CONST.__objc_dictobj: 0x2f8
+  __AUTH_CONST.__auth_got: 0x2ba8
+  __AUTH.__objc_data: 0xde80
+  __DATA.__objc_ivar: 0xfa5c
+  __DATA.__data: 0x20bc0
+  __DATA.__bss: 0xa00
   __DATA.__common: 0xa40
-  __DATA_DIRTY.__objc_data: 0x24f40
-  __DATA_DIRTY.__data: 0x130
-  __DATA_DIRTY.__bss: 0x1738
+  __DATA_DIRTY.__objc_data: 0x26ca0
+  __DATA_DIRTY.__data: 0x140
+  __DATA_DIRTY.__bss: 0x18d8
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  Functions: 72722
-  Symbols:   246745
-  CStrings:  37844
+  Functions: 72987
+  Symbols:   247423
+  CStrings:  38025
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_nlcatlist : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
Symbols:
+ +[SBCompanionSceneForegroundConstraint foregroundConstraint]
+ +[SBCompanionScenePresentationContext defaultLifecycleConstraints]
+ +[SBKeyboardFocusLockReason transientOverlayOwningKeyboard]
+ +[SBKeyboardFocusRequestReason switcherAddedMultipleApps]
+ +[SBKeyboardFocusRequestReason switcherAddedSingleApp]
+ +[SBKeyboardFocusRequestReason switcherFocusedWindowClosed]
+ +[SBKeyboardFocusRequestReason switcherLayoutChangeRequests]
+ +[SBKeyboardFocusRequestReason switcherUpdateTopmostApp]
+ +[SBResizableAppHostingWindowSceneDelegate _individuallyManagedRoles]
+ -[FBSScene(SBHostProxyClientComponent) updateDisplayConfiguration:fence:]
+ -[SBAccessoryWindowSceneDelegate _windowSceneShouldResizeWindowsForScreenBoundsChange:]
+ -[SBAppResizingCoordinator _notifyResizingChangedIfNeeded]
+ -[SBAppResizingCoordinator _setLastInteractedResizableSceneHandle:]
+ -[SBAppResizingCoordinator initWithSceneManager:displayProfileManager:windowSceneManager:startupInterfaceOrientation:]
+ -[SBAppResizingCoordinator resizableApplication]
+ -[SBAppResizingCoordinator resizingAvailability]
+ -[SBAppResizingCoordinator resizingService]
+ -[SBAppResizingService _isAnySceneLocked]
+ -[SBAppResizingService _sendResizingStatusToConnection:]
+ -[SBAppResizingService _setUnavailabilityReasons:]
+ -[SBAppResizingService _startObservingLockEvents:]
+ -[SBAppResizingService activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:]
+ -[SBAppResizingService activeInterfaceOrientationWillChangeToOrientation:]
+ -[SBAppResizingService currentRemoteSession]
+ -[SBAppResizingService initWithCoordinator:displayProfileManager:windowSceneManager:startupInterfaceOrientation:]
+ -[SBAppResizingService lockStateProvider:didUpdateIsUILocked:]
+ -[SBAppResizingService remoteAppResizingSessionDidInvalidate:]
+ -[SBAppResizingService resizingCoordinator:didUpdateAvailability:preferredSize:]
+ -[SBAppResizingService unavailabilityReasons]
+ -[SBAppResizingService windowSceneDidConnect:]
+ -[SBAppResizingService windowSceneDidDisconnect:]
+ -[SBAppResizingSession _calculateResolvedSize:constraintHelper:]
+ -[SBAppResizingSession _effectivePreferredSize]
+ -[SBAppResizingSession initWithWindowSceneManager:displayUniqueId:resizingCornerRadius:]
+ -[SBAppResizingSession isActive]
+ -[SBAppResizingSession prepareForDisplayWithBounds:]
+ -[SBApplication(SwitcherCapabilitiesProvidedByClassic) resizingAvailabilityOnResizableDisplays]
+ -[SBApplicationSceneHandle _finalizeLaunchSignpostState]
+ -[SBAssistantIslandStageController _postAssistantIslandLayoutUpdate]
+ -[SBAssistantIslandStageController ambientPresentationController:willUpdatePresented:]
+ -[SBAssistantIslandStageCoordinator _ambientPresentationControllerDidConnect:]
+ -[SBAssistantIslandStageCoordinator ambientPresentationController:willUpdatePresented:]
+ -[SBAssistantIslandWorkspace _coverSheetSecureAppChanged:]
+ -[SBAssistantIslandWorkspace _updateMapsShowingOnLockScreen]
+ -[SBBannerManager _assistantIslandFrameDidChange:]
+ -[SBBannerManager _invalidateOrDeferPreferredMinimumTopInsetInteractive:]
+ -[SBBannerManager _invalidatePreferredMinimumTopInsetInteractive:]
+ -[SBBannerManager _mainDisplayWindowScene]
+ -[SBBannerManager _updateAssistantIslandDodgeWithFrame:state:gestureInteractive:]
+ -[SBBannerManager _updateEffectiveTopInsetInteractive:]
+ -[SBBannerManager _updateTransientOverlayPresence]
+ -[SBBannerManager transientOverlayScenePresenter:didDismissViewController:wasTopmostPresentation:]
+ -[SBBannerManager transientOverlayScenePresenter:willPresentViewController:]
+ -[SBBluetoothController _applyCBDeviceLoss:]
+ -[SBBluetoothController _applyCBDeviceUpdate:]
+ -[SBBluetoothController _cbDeviceGlyphPropertiesDifferBetween:and:]
+ -[SBBluetoothController _indexOfCBDeviceWithIdentifier:]
+ -[SBBluetoothController _startCBDiscovery]
+ -[SBBluetoothController cbDeviceForAudioRoute:]
+ -[SBCaptureApplicationLaunchSimulator simulateLaunchFromSource:bundleIdentifier:coverSheetViewController:completion:]
+ -[SBCaptureHardwareButton(Testing) simulateClickActivationLaunchForBundleIdentifier:completion:]
+ -[SBCompanionSceneConstraintContext .cxx_destruct]
+ -[SBCompanionSceneConstraintContext appendDescriptionToStream:]
+ -[SBCompanionSceneConstraintContext description]
+ -[SBCompanionSceneConstraintContext hostScene]
+ -[SBCompanionSceneConstraintContext initWithHostScene:sceneUpdate:]
+ -[SBCompanionSceneConstraintContext sceneUpdate]
+ -[SBCompanionSceneForegroundConstraint copyWithZone:]
+ -[SBCompanionSceneForegroundConstraint description]
+ -[SBCompanionSceneForegroundConstraint hash]
+ -[SBCompanionSceneForegroundConstraint isConstrainedByContext:]
+ -[SBCompanionSceneForegroundConstraint isEqual:]
+ -[SBCompanionSceneForegroundConstraint shouldEvaluateConstraintForSceneUpdate:]
+ -[SBCompanionSceneHostComponent _anyRegisteredPresentationsMayBeConstrainedByUpdate:]
+ -[SBCompanionSceneHostComponent _presentation:isConstrainedByContext:]
+ -[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:]
+ -[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:update:]
+ -[SBCompanionScenePresentationContext hash]
+ -[SBCompanionScenePresentationContext initWithSceneSpecification:parameters:]
+ -[SBCompanionScenePresentationContext lifecycleConstraints]
+ -[SBCompanionScenePresentationContext sceneSpecification]
+ -[SBContinuitySession _isUniversalResizabilityEnabled]
+ -[SBContinuitySession resizingCoordinator:didUpdateAvailability:preferredSize:]
+ -[SBContinuitySession resizingSession:didCompleteResizingTransactionWithFrame:success:]
+ -[SBCoverSheetGrabberViewController _leadingStatusBarPartFrameInWindow:]
+ -[SBCoverSheetGrabberViewController _updateVisibilityForFrame:]
+ -[SBCoverSheetSlidingViewController _setHiddenStatusBarParts:]
+ -[SBCoverSheetSlidingViewController _updateClockMorphForProgress:velocity:forPresentationValue:]
+ -[SBCoverSheetSlidingViewController _updateStatusBarRevealForProgress:]
+ -[SBCoverSheetSlidingViewController hasTranslationBaseline]
+ -[SBCoverSheetSlidingViewController hiddenStatusBarParts]
+ -[SBCoverSheetSlidingViewController setHasTranslationBaseline:]
+ -[SBCoverSheetSlidingViewController setHiddenStatusBarParts:]
+ -[SBDashBoardSetupViewController _presentSIMSetupFlowWithFlowType:reason:]
+ -[SBDashBoardSetupViewController _unlockIfNecessaryAndPresentSIMSetupFlowWithFlowType:reason:unlockName:]
+ -[SBElasticValueViewController _hardwareButtonPressedStateDidChange]
+ -[SBElasticValueViewController noteDownButtonPressed:]
+ -[SBElasticValueViewController noteUpButtonPressed:]
+ -[SBFluidSwitcherSpaceTitleItemController _headerIconImageInfo]
+ -[SBFluidSwitcherViewController _statusBarStyleAttributesForAppOwningStatusBarPart:]
+ -[SBFluidSwitcherViewController appLeadingStatusBarStyleAttributes]
+ -[SBFluidSwitcherViewController appTrailingStatusBarStyleAttributes]
+ -[SBHomeScreenController iconImagePrecacheInfosForIconManager:]
+ -[SBHomeScreenViewController isWallpaperEditorPresented]
+ -[SBHomeScreenViewController setWallpaperEditorPresented:]
+ -[SBHostProxyClientComponent _updateDisplayConfiguration:fence:]
+ -[SBInCallPresentationSession _acquireSuspensionUnderLockExemptionIfNeeded]
+ -[SBKeyboardFocusCoordinator _isFocusRequestReasonBlocked:]
+ -[SBKeyboardFocusCoordinator userFocusRequestForScene:requestReason:completion:]
+ -[SBKeyboardFocusLockReason _initReasonWithName:strength:avoidOverridingAppFocusOnOtherDisplays:ignoreModalitiesOnSelectionChange:imposesConstraint:blocksFocusRequestsForReasons:]
+ -[SBKeyboardFocusLockReason blocksFocusRequestsForReasons]
+ -[SBKeyboardFocusLockReason imposesConstraint]
+ -[SBKeyboardFocusRequestReason .cxx_destruct]
+ -[SBKeyboardFocusRequestReason description]
+ -[SBKeyboardFocusRequestReason hash]
+ -[SBKeyboardFocusRequestReason initWithName:]
+ -[SBKeyboardFocusRequestReason isEqual:]
+ -[SBKeyboardFocusRequestReason matchesReason:]
+ -[SBKeyboardFocusRequestReason name]
+ -[SBLockScreenService simulateCaptureLaunchFromSource:bundleIdentifier:completion:]
+ -[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:completion:]
+ -[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:completion:]
+ -[SBMenuBarMainMenuView isDismissingMenuForPointerHoverOrDrag]
+ -[SBMenuBarMainMenuView isDismissingMenuForTouchDrag]
+ -[SBMenuBarMainMenuView isPresentingMenuForPointerHoverOrDrag]
+ -[SBMenuBarMainMenuView isPresentingMenuForTouchDrag]
+ -[SBMenuBarMainMenuView isTransitioningMenuForInteraction]
+ -[SBMenuBarMainMenuView setDismissingMenuForPointerHoverOrDrag:]
+ -[SBMenuBarMainMenuView setDismissingMenuForTouchDrag:]
+ -[SBMenuBarMainMenuView setPresentingMenuForPointerHoverOrDrag:]
+ -[SBMenuBarMainMenuView setPresentingMenuForTouchDrag:]
+ -[SBMenuBarManager _handleMenuBarActivationLongPressGesture:]
+ -[SBMenuBarManager _handleMenuBarActivationPanGesture:]
+ -[SBMenuBarManager appStatusBarLongPressActivationGesture]
+ -[SBMenuBarManager appStatusBarPanActivationGesture]
+ -[SBMenuBarManager currentMenuBarApplicationName]
+ -[SBMenuBarManager currentMenuBarRecipientSceneHandle]
+ -[SBMenuBarManager menuBarStatusBarFollowingAppLeadingStyle]
+ -[SBMenuBarManager setAppStatusBarLongPressActivationGesture:]
+ -[SBMenuBarManager setAppStatusBarPanActivationGesture:]
+ -[SBMenuBarManager setCurrentMenuBarApplicationName:]
+ -[SBMenuBarManager setCurrentMenuBarRecipientSceneHandle:]
+ -[SBMenuBarManager setMenuBarStatusBarFollowingAppLeadingStyle:]
+ -[SBMenuBarManager setSystemStatusBarLongPressActivationGesture:]
+ -[SBMenuBarManager setSystemStatusBarPanActivationGesture:]
+ -[SBMenuBarManager systemStatusBarLongPressActivationGesture]
+ -[SBMenuBarManager systemStatusBarPanActivationGesture]
+ -[SBMenuBarTrackingOngoingTouchPanGestureRecognizer .cxx_destruct]
+ -[SBMenuBarTrackingOngoingTouchPanGestureRecognizer initWithMenuBarViewController:]
+ -[SBMenuBarTrackingOngoingTouchPanGestureRecognizer menuBarViewController]
+ -[SBMenuBarTrackingOngoingTouchPanGestureRecognizer setMenuBarViewController:]
+ -[SBMenuBarTrackingOngoingTouchPanGestureRecognizer touchesEnded:withEvent:]
+ -[SBMenuBarTrackingOngoingTouchPanGestureRecognizer touchesMoved:withEvent:]
+ -[SBMenuBarViewController _adjustPresentedMenuForGestureOverViewInContainer:forPanGesture:isDirectTouch:]
+ -[SBMenuBarViewController _performMainMenuCommandInvocationRequestForCommand:withSystemAuthenticationServiceMessage:session:]
+ -[SBMenuBarViewController _presentMenuViewNonInteractively:forPointerHover:forKeyPress:]
+ -[SBMenuBarViewController adjustPresentedMenuForInteractionOverView:]
+ -[SBMenuBarViewController didPresentContextMenuForMainMenuView:forDirectTouchPan:]
+ -[SBMenuBarViewController handleDirectTouchPanOrLongPressReleased:]
+ -[SBMenuBarViewController handleMenuPanOrLongPressGesture:isDirectTouch:]
+ -[SBMinimumViableSwitcherTableViewController appLayouts]
+ -[SBMinimumViableSwitcherTableViewController appLeadingStatusBarStyleAttributes]
+ -[SBMinimumViableSwitcherTableViewController appTrailingStatusBarStyleAttributes]
+ -[SBMutableCompanionScenePresentationContext lifecycleConstraints]
+ -[SBMutableCompanionScenePresentationContext setLifecycleConstraints:]
+ -[SBMutableStatusBarSettings setAlpha:forParts:]
+ -[SBMutableStatusBarSettings setPartAlphas:]
+ -[SBPolicyAggregator _allowsCapabilitySearchOnLockScreenWithExplanation:]
+ -[SBRecordingIndicatorManager _createOrResetPreventSystemSleepAssertion]
+ -[SBRecordingIndicatorManager _releasePreventSystemSleepAssertion]
+ -[SBRecordingIndicatorManager _scheduleReleaseOfPreventSystemSleepAssertion]
+ -[SBRecordingIndicatorManager preventSystemSleepAssertionID]
+ -[SBRecordingIndicatorManager preventSystemSleepAssertionName]
+ -[SBRecordingIndicatorManager releasePreventSystemSleepAssertionTimer]
+ -[SBRecordingIndicatorManager setPreventSystemSleepAssertionID:]
+ -[SBRecordingIndicatorManager setPreventSystemSleepAssertionName:]
+ -[SBRecordingIndicatorManager setReleasePreventSystemSleepAssertionTimer:]
+ -[SBRemoteAppResizingSession initWithResizingSession:connection:delegate:]
+ -[SBRemoteAppResizingSession invalidateForClient]
+ -[SBRemoteAppResizingSession invalidateForServer]
+ -[SBRemoteAppResizingSession isActive]
+ -[SBRemoteAppResizingSession isValid]
+ -[SBRemoteAppResizingSession managesResizingSession:]
+ -[SBRemoteAppResizingSession updatePreferredSize:forAssertionWithIdentifier:]
+ -[SBResizableAppHostingRegionOfInterestViewController .cxx_destruct]
+ -[SBResizableAppHostingRegionOfInterestViewController initWithView:]
+ -[SBResizableAppHostingRegionOfInterestViewController resizingCoordinator:didUpdateActiveSession:]
+ -[SBResizableAppHostingRegionOfInterestViewController resizingSession:didBeginResizingTransactionWithFrame:]
+ -[SBResizableAppHostingRegionOfInterestViewController viewDidLoad]
+ -[SBResizableAppHostingRegionOfInterestViewController viewWillLayoutSubviews]
+ -[SBResizableAppHostingRegionOfInterestWindow _supportedInterfaceOrientationsForRootViewController]
+ -[SBResizableAppHostingRegionOfInterestWindow initWithWindowScene:]
+ -[SBResizableAppHostingWindowSceneDelegate _configureForConnectingWindowScene:windowSceneContext:]
+ -[SBResizableAppHostingWindowSceneDelegate _createShieldWindowForWindowScene:]
+ -[SBResizableAppHostingWindowSceneDelegate _displayLayoutPublisherForConnectingWindowScene:]
+ -[SBResizableAppHostingWindowSceneDelegate _pipelineManager]
+ -[SBResizableAppHostingWindowSceneDelegate _removeShieldWindowForWindowScene:]
+ -[SBResizableAppHostingWindowSceneDelegate _shouldManageParticipantWithRole:]
+ -[SBResizableAppHostingWindowSceneDelegate _traitsDelegateForWindowRole:]
+ -[SBResizableAppHostingWindowSceneDelegate _uiSceneConnected:]
+ -[SBResizableAppHostingWindowSceneDelegate _uiSceneDisconnected:]
+ -[SBResizableAppHostingWindowSceneDelegate init]
+ -[SBResizableAppHostingWindowSceneDelegate resizingShieldWindowDidTapButton:]
+ -[SBRingerAlertElement _applyVolumeLimitedSizeLayout:]
+ -[SBRingerAlertElement _buildVolumeLeadingContentProviderForRingerSilent:]
+ -[SBRingerAlertElement _buildVolumeTrailingContentProvider]
+ -[SBRingerAlertElement defaultVolumeConstraints]
+ -[SBRingerAlertElement limitedSizeVolumeConstraints]
+ -[SBRingerAlertElement setDefaultVolumeConstraints:]
+ -[SBRingerAlertElement setDisplayedWithLimitedSize:]
+ -[SBRingerAlertElement setLimitedSizeVolumeConstraints:]
+ -[SBRingerAlertElement setVolumeBellImageView:]
+ -[SBRingerAlertElement setVolumeLabel:]
+ -[SBRingerAlertElement volumeBellImageView]
+ -[SBRingerAlertElement volumeLabel]
+ -[SBSAContainerViewDescription _setContentBorderWidth:]
+ -[SBSAContainerViewDescription contentBorderWidth]
+ -[SBSAContainerViewDescriptionMutator contentBorderWidth]
+ -[SBSAContainerViewDescriptionMutator setContentBorderWidth:]
+ -[SBSAElementContext _setDisplayedWithLimitedSize:]
+ -[SBSAElementContext _setPreferredSystemClipPadding:]
+ -[SBSAElementContext init]
+ -[SBSAElementContext isDisplayedWithLimitedSize]
+ -[SBSAElementContext preferredSystemClipPadding]
+ -[SBSAElementContextMutator isDisplayedWithLimitedSize]
+ -[SBSAElementContextMutator preferredSystemClipPadding]
+ -[SBSAElementContextMutator setDisplayedWithLimitedSize:]
+ -[SBSAElementContextMutator setPreferredSystemClipPadding:]
+ -[SBSAIndicatorElementContext _setPreferredSystemClipPadding:]
+ -[SBSAIndicatorElementContext preferredSystemClipPadding]
+ -[SBSAIndicatorElementContextMutator preferredSystemClipPadding]
+ -[SBSAIndicatorElementContextMutator setPreferredSystemClipPadding:]
+ -[SBSSKDisplayProfileManager setResizableDisplayUUID:initialFrame:]
+ -[SBSpotlightTransientOverlayViewController wantsInitialKeyboardFocus]
+ -[SBStatusBarSettings partAlphas]
+ -[SBSwitcherController appLeadingStatusBarStyleAttributes]
+ -[SBSwitcherController appTrailingStatusBarStyleAttributes]
+ -[SBSwitcherController isStatusBarUnderlappedByAnyAppWindowControls]
+ -[SBSwitcherController menuBarRecipientSceneHandle]
+ -[SBSystemApertureContainerView _updateContentBorderAppearance]
+ -[SBSystemApertureContainerView contentBorderWidth]
+ -[SBSystemApertureContainerView setContentBorderWidth:]
+ -[SBSystemApertureSceneElement _setWantsLayoutPassForClientUpdate:reason:]
+ -[SBSystemApertureSceneElement didConsumeLayoutUpdateRequestForHostedClient]
+ -[SBSystemApertureSettings contentBorderDebugColorsEnabled]
+ -[SBSystemApertureSettings contentBorderEnabledForCompactLayout]
+ -[SBSystemApertureSettings contentBorderEnabledForCustomLayout]
+ -[SBSystemApertureSettings contentBorderEnabledForLimitedSize]
+ -[SBSystemApertureSettings contentBorderEnabledForMinimalLayout]
+ -[SBSystemApertureSettings contentBorderEnabledForNonLimitedSize]
+ -[SBSystemApertureSettings contentBorderEnabled]
+ -[SBSystemApertureSettings contentBorderWidth]
+ -[SBSystemApertureSettings setContentBorderDebugColorsEnabled:]
+ -[SBSystemApertureSettings setContentBorderEnabled:]
+ -[SBSystemApertureSettings setContentBorderEnabledForCompactLayout:]
+ -[SBSystemApertureSettings setContentBorderEnabledForCustomLayout:]
+ -[SBSystemApertureSettings setContentBorderEnabledForLimitedSize:]
+ -[SBSystemApertureSettings setContentBorderEnabledForMinimalLayout:]
+ -[SBSystemApertureSettings setContentBorderEnabledForNonLimitedSize:]
+ -[SBSystemApertureSettings setContentBorderWidth:]
+ -[SBSystemApertureSettings setWantsLayoutPassForClientUpdateEnabled:]
+ -[SBSystemApertureSettings wantsLayoutPassForClientUpdateEnabled]
+ -[SBSystemApertureStatusBarPillElement systemApertureLayoutCustomizingOptions]
+ -[SBSystemApertureViewController _updateQueryIterationLabelVisibility]
+ -[SBTelephonyManager supportsDynamicSIMConfiguration]
+ -[SBTraitsResizableDisplayPipelineManager .cxx_destruct]
+ -[SBTraitsResizableDisplayPipelineManager _noteInputsNeedUpdateWithAnimationSettings:fence:reason:]
+ -[SBTraitsResizableDisplayPipelineManager _updateInputsForCurrentUserInterfaceStyle]
+ -[SBTraitsResizableDisplayPipelineManager ambientPresentationStageRoles]
+ -[SBTraitsResizableDisplayPipelineManager didChangeSettingsForParticipant:context:]
+ -[SBTraitsResizableDisplayPipelineManager initWithArbiter:sceneDelegate:userInterfaceStyleProvider:]
+ -[SBTraitsResizableDisplayPipelineManager inputs]
+ -[SBTraitsResizableDisplayPipelineManager orientationStageRoles]
+ -[SBTraitsResizableDisplayPipelineManager setupDefaultPipelineForArbiter:]
+ -[SBTraitsResizableDisplayPipelineManager supportsLiveDeviceRotation]
+ -[SBTraitsResizableDisplayPipelineManager updatePreferencesForParticipant:updater:]
+ -[SBTraitsResizableDisplayPipelineManager userInterfaceStyleDidUpdateWithAnimationSettings:fence:]
+ -[SBTraitsResizableDisplayPipelineManager userInterfaceStyleStageRoles]
+ -[SBTraitsResizableDisplayPipelineManager zOrderStageRoles]
+ -[SBTransientOverlayViewController wantsInitialKeyboardFocus]
+ -[_SBSystemApertureContentBorderView _updateBorderColor]
+ -[_SBSystemApertureContentBorderView borderCornerRadius]
+ -[_SBSystemApertureContentBorderView borderWidth]
+ -[_SBSystemApertureContentBorderView initWithFrame:]
+ -[_SBSystemApertureContentBorderView isDebugColorsEnabled]
+ -[_SBSystemApertureContentBorderView setBorderCornerRadius:]
+ -[_SBSystemApertureContentBorderView setBorderWidth:]
+ -[_SBSystemApertureContentBorderView setDebugColorsEnabled:]
+ GCC_except_table1043
+ GCC_except_table1062
+ GCC_except_table165
+ GCC_except_table194
+ GCC_except_table196
+ GCC_except_table219
+ GCC_except_table259
+ GCC_except_table263
+ GCC_except_table287
+ GCC_except_table301
+ GCC_except_table315
+ GCC_except_table353
+ GCC_except_table371
+ GCC_except_table396
+ GCC_except_table407
+ GCC_except_table447
+ GCC_except_table509
+ GCC_except_table543
+ GCC_except_table550
+ GCC_except_table553
+ GCC_except_table560
+ GCC_except_table575
+ GCC_except_table576
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
+ GCC_except_table900
+ GCC_except_table939
+ GCC_except_table950
+ GCC_except_table96
+ GCC_except_table997
+ OBJC_IVAR_$_SBCompanionScenePresentationContext._lifecycleConstraints
+ _NSStringFromCompanionScenePresentationMode
+ _OBJC_CLASS_$_CBDiscovery
+ _OBJC_CLASS_$_SBAccessoryWindowSceneDelegate
+ _OBJC_CLASS_$_SBCaptureApplicationLaunchSimulator
+ _OBJC_CLASS_$_SBCompanionSceneConstraintContext
+ _OBJC_CLASS_$_SBCompanionSceneForegroundConstraint
+ _OBJC_CLASS_$_SBHIconImagePrecacheInfo
+ _OBJC_CLASS_$_SBKeyboardFocusRequestReason
+ _OBJC_CLASS_$_SBMenuBarTrackingOngoingTouchPanGestureRecognizer
+ _OBJC_CLASS_$_SBResizableAppHostingRegionOfInterestViewController
+ _OBJC_CLASS_$_SBResizableAppHostingRegionOfInterestWindow
+ _OBJC_CLASS_$_SBSAppResizingServiceStatus
+ _OBJC_CLASS_$_SBTraitsResizableDisplayPipelineManager
+ _OBJC_CLASS_$__SBSystemApertureContentBorderView
+ _OBJC_CLASS_$__UISceneAccessoryContainerSpecification
+ _OBJC_IVAR_$_SBAppResizingCoordinator._lastNotifiedAvailability
+ _OBJC_IVAR_$_SBAppResizingCoordinator._lastNotifiedResizableApplication
+ _OBJC_IVAR_$_SBAppResizingCoordinator._lastNotifiedResizingPossible
+ _OBJC_IVAR_$_SBAppResizingCoordinator._resizingAvailability
+ _OBJC_IVAR_$_SBAppResizingService._allRemoteSessions
+ _OBJC_IVAR_$_SBAppResizingService._unavailabilityReasons
+ _OBJC_IVAR_$_SBAppResizingService._windowSceneManager
+ _OBJC_IVAR_$_SBAppResizingSession._reportedResolvedSize
+ _OBJC_IVAR_$_SBApplicationSceneUpdateTransaction._exitedProcess
+ _OBJC_IVAR_$_SBAssistantIslandStageCoordinator._ambientOrientationPolicyTokensByWindowScene
+ _OBJC_IVAR_$_SBAssistantIslandStageCoordinator._windowSceneByAmbientPresentationController
+ _OBJC_IVAR_$_SBBannerManager._assistantIslandDodgeLatchedOff
+ _OBJC_IVAR_$_SBBannerManager._assistantIslandTopInset
+ _OBJC_IVAR_$_SBBannerManager._pendingMinimumTopInsetInvalidationInteractive
+ _OBJC_IVAR_$_SBBannerManager._systemApertureTopInset
+ _OBJC_IVAR_$_SBBannerManager._transientOverlayPresented
+ _OBJC_IVAR_$_SBBluetoothController._cbDevices
+ _OBJC_IVAR_$_SBBluetoothController._cbDiscovery
+ _OBJC_IVAR_$_SBCompanionSceneConstraintContext._hostScene
+ _OBJC_IVAR_$_SBCompanionSceneConstraintContext._sceneUpdate
+ _OBJC_IVAR_$_SBCompanionScenePresentationContext._sceneSpecification
+ _OBJC_IVAR_$_SBCoverSheetSlidingViewController._hasTranslationBaseline
+ _OBJC_IVAR_$_SBCoverSheetSlidingViewController._hiddenStatusBarParts
+ _OBJC_IVAR_$_SBElasticValueViewController._downButtonPressed
+ _OBJC_IVAR_$_SBElasticValueViewController._upButtonPressed
+ _OBJC_IVAR_$_SBFluidSwitcherSpaceTitleItemController._headerIconImageInfo
+ _OBJC_IVAR_$_SBHomeScreenViewController._wallpaperEditorPresented
+ _OBJC_IVAR_$_SBKeyboardFocusCoordinator._blockedRequestReasons
+ _OBJC_IVAR_$_SBKeyboardFocusLockReason._blocksFocusRequestsForReasons
+ _OBJC_IVAR_$_SBKeyboardFocusLockReason._imposesConstraint
+ _OBJC_IVAR_$_SBKeyboardFocusRequestReason._name
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._dismissingMenuForPointerHoverOrDrag
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._dismissingMenuForTouchDrag
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._presentingMenuForPointerHoverOrDrag
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._presentingMenuForTouchDrag
+ _OBJC_IVAR_$_SBMenuBarManager._appStatusBarLongPressActivationGesture
+ _OBJC_IVAR_$_SBMenuBarManager._appStatusBarPanActivationGesture
+ _OBJC_IVAR_$_SBMenuBarManager._currentMenuBarApplicationName
+ _OBJC_IVAR_$_SBMenuBarManager._currentMenuBarRecipientSceneHandle
+ _OBJC_IVAR_$_SBMenuBarManager._menuBarStatusBarFollowingAppLeadingStyle
+ _OBJC_IVAR_$_SBMenuBarManager._systemStatusBarLongPressActivationGesture
+ _OBJC_IVAR_$_SBMenuBarManager._systemStatusBarPanActivationGesture
+ _OBJC_IVAR_$_SBMenuBarTrackingOngoingTouchPanGestureRecognizer._menuBarViewController
+ _OBJC_IVAR_$_SBMenuBarViewController._pendingAuthenticatedCommandSession
+ _OBJC_IVAR_$_SBRecordingIndicatorManager._preventSystemSleepAssertionID
+ _OBJC_IVAR_$_SBRecordingIndicatorManager._preventSystemSleepAssertionName
+ _OBJC_IVAR_$_SBRecordingIndicatorManager._releasePreventSystemSleepAssertionTimer
+ _OBJC_IVAR_$_SBRemoteAppResizingSession._clientInvalidated
+ _OBJC_IVAR_$_SBRemoteAppResizingSession._delegate
+ _OBJC_IVAR_$_SBResizableAppHostingRegionOfInterestViewController._regionOfInterestFrame
+ _OBJC_IVAR_$_SBResizableAppHostingRegionOfInterestViewController._regionOfInterestView
+ _OBJC_IVAR_$_SBResizableAppHostingWindowSceneDelegate._displayLayoutPublisher
+ _OBJC_IVAR_$_SBResizableAppHostingWindowSceneDelegate._resizingService
+ _OBJC_IVAR_$_SBResizableAppHostingWindowSceneDelegate._roiWindow
+ _OBJC_IVAR_$_SBResizableAppHostingWindowSceneDelegate._traitsPipelineManager
+ _OBJC_IVAR_$_SBResizableAppHostingWindowSceneDelegate._traitsWindowParticipantsDelegate
+ _OBJC_IVAR_$_SBResizableAppHostingWindowSceneDelegate._windowSceneContext
+ _OBJC_IVAR_$_SBResizableAppHostingWindowSceneDelegate._windowSceneIdentifiersToShieldWindows
+ _OBJC_IVAR_$_SBRingerAlertElement._defaultVolumeConstraints
+ _OBJC_IVAR_$_SBRingerAlertElement._limitedSizeVolumeConstraints
+ _OBJC_IVAR_$_SBRingerAlertElement._volumeBellImageView
+ _OBJC_IVAR_$_SBRingerAlertElement._volumeLabel
+ _OBJC_IVAR_$_SBSAContainerViewDescription._contentBorderWidth
+ _OBJC_IVAR_$_SBSAElementContext._displayedWithLimitedSize
+ _OBJC_IVAR_$_SBSAElementContext._preferredSystemClipPadding
+ _OBJC_IVAR_$_SBSAIndicatorElementContext._preferredSystemClipPadding
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._darklightSDFView
+ _OBJC_IVAR_$_SBSwitcherGenieEffectView._diffuseHighlightSDFView
+ _OBJC_IVAR_$_SBSystemApertureContainerView._contentBorderView
+ _OBJC_IVAR_$_SBSystemApertureContainerView._contentBorderWidth
+ _OBJC_IVAR_$_SBSystemApertureSettings._contentBorderDebugColorsEnabled
+ _OBJC_IVAR_$_SBSystemApertureSettings._contentBorderEnabled
+ _OBJC_IVAR_$_SBSystemApertureSettings._contentBorderEnabledForCompactLayout
+ _OBJC_IVAR_$_SBSystemApertureSettings._contentBorderEnabledForCustomLayout
+ _OBJC_IVAR_$_SBSystemApertureSettings._contentBorderEnabledForLimitedSize
+ _OBJC_IVAR_$_SBSystemApertureSettings._contentBorderEnabledForMinimalLayout
+ _OBJC_IVAR_$_SBSystemApertureSettings._contentBorderEnabledForNonLimitedSize
+ _OBJC_IVAR_$_SBSystemApertureSettings._contentBorderWidth
+ _OBJC_IVAR_$_SBSystemApertureSettings._wantsLayoutPassForClientUpdateEnabled
+ _OBJC_IVAR_$_SBSystemApertureViewController._systemApertureUnderAutomationTesting
+ _OBJC_IVAR_$_SBTelephonyManager._supportsDynamicSIMConfiguration
+ _OBJC_IVAR_$_SBTraitsResizableDisplayPipelineManager._activeOrientationParticipant
+ _OBJC_IVAR_$_SBTraitsResizableDisplayPipelineManager._inputs
+ _OBJC_IVAR_$_SBTraitsResizableDisplayPipelineManager._rolesAndDefaultPoliciesProvider
+ _OBJC_IVAR_$_SBTransientOverlayViewController._wantsInitialKeyboardFocus
+ _OBJC_IVAR_$__SBSystemApertureContentBorderView._borderCornerRadius
+ _OBJC_IVAR_$__SBSystemApertureContentBorderView._borderWidth
+ _OBJC_IVAR_$__SBSystemApertureContentBorderView._debugColorsEnabled
+ _OBJC_METACLASS_$_SBAccessoryWindowSceneDelegate
+ _OBJC_METACLASS_$_SBCaptureApplicationLaunchSimulator
+ _OBJC_METACLASS_$_SBCompanionSceneConstraintContext
+ _OBJC_METACLASS_$_SBCompanionSceneForegroundConstraint
+ _OBJC_METACLASS_$_SBKeyboardFocusRequestReason
+ _OBJC_METACLASS_$_SBMenuBarTrackingOngoingTouchPanGestureRecognizer
+ _OBJC_METACLASS_$_SBResizableAppHostingRegionOfInterestViewController
+ _OBJC_METACLASS_$_SBResizableAppHostingRegionOfInterestWindow
+ _OBJC_METACLASS_$_SBTraitsResizableDisplayPipelineManager
+ _OBJC_METACLASS_$__SBSystemApertureContentBorderView
+ _SBAmbientPresentationControllerDidConnectNotification
+ _SBAssistantIslandLayoutDidChangeNotification
+ _SBAssistantIslandLayoutIsInteractiveKey
+ _SBBluetoothAccessoryStateChangedNotification
+ _SBResizingAvailabilityDescription
+ _SBResizingAvailabilityIsResizingPossible
+ _SBSAPreferredSystemClipPaddingUnspecified
+ _SBSAppResizingUnavailabilityReasonsDescription
+ _SBSCaptureLaunchSimulationErrorDomain
+ _SBSimulateCaptureLaunchEntitlement
+ _SBStatusBarDataLocalNetworkDebugName
+ _SBSwitcherGenieGlassHighlightDirectionDefault
+ _SBTraitsParticipantRoleAppHostingRegionOfInterest
+ _STStatusBarDataEntryMenuBarKey
+ _STUIStatusBarPartIdentifierBackNavigation
+ _UISceneWillConnectNotification
+ __OBJC_$_CLASS_METHODS_SBCompanionSceneForegroundConstraint
+ __OBJC_$_CLASS_METHODS_SBCompanionScenePresentationContext
+ __OBJC_$_CLASS_METHODS_SBKeyboardFocusRequestReason
+ __OBJC_$_CLASS_METHODS_SBResizableAppHostingWindowSceneDelegate
+ __OBJC_$_INSTANCE_METHODS_SBAccessoryWindowSceneDelegate
+ __OBJC_$_INSTANCE_METHODS_SBCaptureApplicationLaunchSimulator
+ __OBJC_$_INSTANCE_METHODS_SBCaptureHardwareButton(Testing)
+ __OBJC_$_INSTANCE_METHODS_SBChainableModifierEventResponse(SBWindowingModifierResponse|SBSwitcherModifierEventResponse)
+ __OBJC_$_INSTANCE_METHODS_SBCompanionSceneConstraintContext
+ __OBJC_$_INSTANCE_METHODS_SBCompanionSceneForegroundConstraint
+ __OBJC_$_INSTANCE_METHODS_SBKeyboardFocusRequestReason
+ __OBJC_$_INSTANCE_METHODS_SBMenuBarTrackingOngoingTouchPanGestureRecognizer
+ __OBJC_$_INSTANCE_METHODS_SBResizableAppHostingRegionOfInterestViewController
+ __OBJC_$_INSTANCE_METHODS_SBResizableAppHostingRegionOfInterestWindow
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherModifier(WindowingModifier|SharedModifierUtilities)
+ __OBJC_$_INSTANCE_METHODS_SBTraitsResizableDisplayPipelineManager
+ __OBJC_$_INSTANCE_METHODS__SBSystemApertureContentBorderView
+ __OBJC_$_INSTANCE_VARIABLES_SBCompanionSceneConstraintContext
+ __OBJC_$_INSTANCE_VARIABLES_SBKeyboardFocusRequestReason
+ __OBJC_$_INSTANCE_VARIABLES_SBMenuBarTrackingOngoingTouchPanGestureRecognizer
+ __OBJC_$_INSTANCE_VARIABLES_SBResizableAppHostingRegionOfInterestViewController
+ __OBJC_$_INSTANCE_VARIABLES_SBTraitsResizableDisplayPipelineManager
+ __OBJC_$_INSTANCE_VARIABLES__SBSystemApertureContentBorderView
+ __OBJC_$_PROP_LIST_SBAccessoryWindowSceneDelegate
+ __OBJC_$_PROP_LIST_SBCompanionSceneConstraintContext
+ __OBJC_$_PROP_LIST_SBCompanionSceneForegroundConstraint
+ __OBJC_$_PROP_LIST_SBKeyboardFocusRequestReason
+ __OBJC_$_PROP_LIST_SBMenuBarTrackingOngoingTouchPanGestureRecognizer
+ __OBJC_$_PROP_LIST_SBResizableAppHostingRegionOfInterestViewController
+ __OBJC_$_PROP_LIST_SBTraitsResizableDisplayPipelineManager
+ __OBJC_$_PROP_LIST__SBSystemApertureContentBorderView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBCompanionSceneConstraint
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBCompanionSceneConstraint
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBRemoteAppResizingSessionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBCompanionSceneConstraint
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBRemoteAppResizingSessionDelegate
+ __OBJC_$_PROTOCOL_REFS_SBCompanionSceneConstraint
+ __OBJC_$_PROTOCOL_REFS_SBRemoteAppResizingSessionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SBAccessoryWindowSceneDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SBCompanionSceneConstraintContext
+ __OBJC_CLASS_PROTOCOLS_$_SBCompanionSceneForegroundConstraint
+ __OBJC_CLASS_PROTOCOLS_$_SBResizableAppHostingRegionOfInterestViewController
+ __OBJC_CLASS_PROTOCOLS_$_SBTraitsResizableDisplayPipelineManager
+ __OBJC_CLASS_RO_$_SBAccessoryWindowSceneDelegate
+ __OBJC_CLASS_RO_$_SBCaptureApplicationLaunchSimulator
+ __OBJC_CLASS_RO_$_SBCompanionSceneConstraintContext
+ __OBJC_CLASS_RO_$_SBCompanionSceneForegroundConstraint
+ __OBJC_CLASS_RO_$_SBKeyboardFocusRequestReason
+ __OBJC_CLASS_RO_$_SBMenuBarTrackingOngoingTouchPanGestureRecognizer
+ __OBJC_CLASS_RO_$_SBResizableAppHostingRegionOfInterestViewController
+ __OBJC_CLASS_RO_$_SBResizableAppHostingRegionOfInterestWindow
+ __OBJC_CLASS_RO_$_SBTraitsResizableDisplayPipelineManager
+ __OBJC_CLASS_RO_$__SBSystemApertureContentBorderView
+ __OBJC_LABEL_PROTOCOL_$_SBCompanionSceneConstraint
+ __OBJC_LABEL_PROTOCOL_$_SBRemoteAppResizingSessionDelegate
+ __OBJC_METACLASS_RO_$_SBAccessoryWindowSceneDelegate
+ __OBJC_METACLASS_RO_$_SBCaptureApplicationLaunchSimulator
+ __OBJC_METACLASS_RO_$_SBCompanionSceneConstraintContext
+ __OBJC_METACLASS_RO_$_SBCompanionSceneForegroundConstraint
+ __OBJC_METACLASS_RO_$_SBKeyboardFocusRequestReason
+ __OBJC_METACLASS_RO_$_SBMenuBarTrackingOngoingTouchPanGestureRecognizer
+ __OBJC_METACLASS_RO_$_SBResizableAppHostingRegionOfInterestViewController
+ __OBJC_METACLASS_RO_$_SBResizableAppHostingRegionOfInterestWindow
+ __OBJC_METACLASS_RO_$_SBTraitsResizableDisplayPipelineManager
+ __OBJC_METACLASS_RO_$__SBSystemApertureContentBorderView
+ __OBJC_PROTOCOL_$_SBCompanionSceneConstraint
+ __OBJC_PROTOCOL_$_SBRemoteAppResizingSessionDelegate
+ __SBJSONNumberOrNull
+ __SBPartAlphasForSettings
+ __UIClamp
+ __UILerp
+ __UIMap
+ __UIStatusBarDataEntryBackNavigationKey
+ __UIUnlerp
+ ___105-[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:update:]_block_invoke
+ ___105-[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:update:]_block_invoke_2
+ ___105-[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:update:]_block_invoke_3
+ ___105-[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:update:]_block_invoke_4
+ ___105-[SBDashBoardSetupViewController _unlockIfNecessaryAndPresentSIMSetupFlowWithFlowType:reason:unlockName:]_block_invoke
+ ___105-[SBMenuBarViewController _adjustPresentedMenuForGestureOverViewInContainer:forPanGesture:isDirectTouch:]_block_invoke
+ ___113-[SBAppResizingService initWithCoordinator:displayProfileManager:windowSceneManager:startupInterfaceOrientation:]_block_invoke
+ ___117-[SBCaptureApplicationLaunchSimulator simulateLaunchFromSource:bundleIdentifier:coverSheetViewController:completion:]_block_invoke
+ ___117-[SBCaptureApplicationLaunchSimulator simulateLaunchFromSource:bundleIdentifier:coverSheetViewController:completion:]_block_invoke_2
+ ___117-[SBCaptureApplicationLaunchSimulator simulateLaunchFromSource:bundleIdentifier:coverSheetViewController:completion:]_block_invoke_3
+ ___30-[SBSAElementContext isEqual:]_block_invoke_24
+ ___30-[SBSAElementContext isEqual:]_block_invoke_25
+ ___31-[SBStatusBarSettings isEqual:]_block_invoke_6
+ ___39-[SBSAIndicatorElementContext isEqual:]_block_invoke_9
+ ___40-[SBSAContainerViewDescription isEqual:]_block_invoke_14
+ ___42-[SBBluetoothController _startCBDiscovery]_block_invoke
+ ___42-[SBBluetoothController _startCBDiscovery]_block_invoke_2
+ ___42-[SBBluetoothController _startCBDiscovery]_block_invoke_3
+ ___42-[SBBluetoothController _startCBDiscovery]_block_invoke_4
+ ___42-[SBBluetoothController _startCBDiscovery]_block_invoke_5
+ ___47-[SBBluetoothController cbDeviceForAudioRoute:]_block_invoke
+ ___47-[SBCompanionScenePresentationContext isEqual:]_block_invoke_2
+ ___47-[SBCompanionScenePresentationContext isEqual:]_block_invoke_3
+ ___53-[SBApplicationSceneUpdateTransaction _performCommit]_block_invoke_3
+ ___53-[SBApplicationSceneUpdateTransaction _performCommit]_block_invoke_4
+ ___54+[SBKeyboardFocusRequestReason switcherAddedSingleApp]_block_invoke
+ ___54-[SBIconController _registerLabelCacheMaintenanceTask]_block_invoke_3
+ ___56+[SBKeyboardFocusRequestReason switcherUpdateTopmostApp]_block_invoke
+ ___56-[SBBluetoothController _indexOfCBDeviceWithIdentifier:]_block_invoke
+ ___56-[SBCompanionSceneRestrictor appendDescriptionToStream:]_block_invoke_4
+ ___57+[SBKeyboardFocusRequestReason switcherAddedMultipleApps]_block_invoke
+ ___58-[SBCompanionScenePresentation appendDescriptionToStream:]_block_invoke_5
+ ___58-[SBCompanionScenePresentation appendDescriptionToStream:]_block_invoke_6
+ ___59+[SBKeyboardFocusRequestReason switcherFocusedWindowClosed]_block_invoke
+ ___60+[SBCompanionSceneForegroundConstraint foregroundConstraint]_block_invoke
+ ___60+[SBKeyboardFocusRequestReason switcherLayoutChangeRequests]_block_invoke
+ ___60-[SBAssistantIslandWorkspace _updateMapsShowingOnLockScreen]_block_invoke
+ ___62-[SBCoverSheetSlidingViewController _setHiddenStatusBarParts:]_block_invoke
+ ___62-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]_block_invoke_5
+ ___63-[SBCoverSheetGrabberViewController _updateVisibilityForFrame:]_block_invoke
+ ___63-[SBHomeScreenController iconImagePrecacheInfosForIconManager:]_block_invoke
+ ___64-[SBHostProxyClientComponent _updateDisplayConfiguration:fence:]_block_invoke
+ ___65-[SBCompanionScenePresentationContext appendDescriptionToStream:]_block_invoke
+ ___65-[SBCompanionScenePresentationContext appendDescriptionToStream:]_block_invoke_2
+ ___68-[SBSwitcherController isStatusBarUnderlappedByAnyAppWindowControls]_block_invoke
+ ___69+[SBResizableAppHostingWindowSceneDelegate _individuallyManagedRoles]_block_invoke
+ ___71-[SBCoverSheetSlidingViewController _updateStatusBarRevealForProgress:]_block_invoke
+ ___76-[SBBannerManager presenter:willTransitionToSize:withTransitionCoordinator:]_block_invoke_2
+ ___76-[SBRecordingIndicatorManager _scheduleReleaseOfPreventSystemSleepAssertion]_block_invoke
+ ___83-[SBLockScreenService simulateCaptureLaunchFromSource:bundleIdentifier:completion:]_block_invoke
+ ___83-[SBLockScreenService simulateCaptureLaunchFromSource:bundleIdentifier:completion:]_block_invoke_2
+ ___83-[SBTraitsResizableDisplayPipelineManager updatePreferencesForParticipant:updater:]_block_invoke
+ ___83-[SBTraitsResizableDisplayPipelineManager updatePreferencesForParticipant:updater:]_block_invoke_2
+ ___87-[SBAssistantIslandStageCoordinator ambientPresentationController:willUpdatePresented:]_block_invoke
+ ___87-[SBMenuBarManager _setupTransitionHelperStatusBarIfNeededForTransitioningToPresented:]_block_invoke
+ ___87-[SBResizableAppHostingWindowSceneDelegate resizingCoordinator:didUpdateActiveSession:]_block_invoke
+ ___92-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:completion:]_block_invoke
+ ___92-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:completion:]_block_invoke_2
+ ___92-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:completion:]_block_invoke_3
+ ___92-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:completion:]_block_invoke_4
+ ___92-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:completion:]_block_invoke_5
+ ___92-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:completion:]_block_invoke_6
+ ___92-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:completion:]_block_invoke_7
+ ___94-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:completion:]_block_invoke
+ ___94-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:completion:]_block_invoke_2
+ ___94-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:completion:]_block_invoke_3
+ ___94-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:completion:]_block_invoke_4
+ ___94-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:completion:]_block_invoke_5
+ ___94-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:completion:]_block_invoke_6
+ ___94-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:completion:]_block_invoke_7
+ ___94-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:completion:]_block_invoke_8
+ ___98-[SBResizableAppHostingWindowSceneDelegate _configureForConnectingWindowScene:windowSceneContext:]_block_invoke
+ ___98-[SBWindowSceneStatusBarAssertionManager _statusBarUpdatedFromSettings:toSettings:withAnimations:]_block_invoke_10
+ ___98-[SBWindowSceneStatusBarAssertionManager _statusBarUpdatedFromSettings:toSettings:withAnimations:]_block_invoke_7
+ ___98-[SBWindowSceneStatusBarAssertionManager _statusBarUpdatedFromSettings:toSettings:withAnimations:]_block_invoke_8
+ ___98-[SBWindowSceneStatusBarAssertionManager _statusBarUpdatedFromSettings:toSettings:withAnimations:]_block_invoke_9
+ ___99-[SBTraitsResizableDisplayPipelineManager _noteInputsNeedUpdateWithAnimationSettings:fence:reason:]_block_invoke
+ ____SBPartAlphaChangesFromSettings_block_invoke
+ ____SBPartAlphasForSettings_block_invoke
+ ___block_descriptor_32_e53_v24?0"NSArray"8"TRAPreferencesResolutionContext"16l
+ ___block_descriptor_40_e8_32s_e25_B32?0"CBDevice"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e38_v16?0"<SBCompanionSceneConstraint>"8ls32l8
+ ___block_descriptor_40_e8_32w_e18_v16?0"CBDevice"8lw32l8
+ ___block_descriptor_48_e8_32bs40w_e31_v24?0"FBProcess"8"NSError"16ls32l8w40l8
+ ___block_descriptor_48_e8_32s40s_e21_v16?0"UIStatusBar"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e69_v24?0"FBSMutableSceneClientSettings"8"FBSSceneTransitionContext"16ls32l8s40l8
+ ___block_descriptor_51_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56w_e20_v24?08"NSError"16lw56l8s32l8s40l8s48l8
+ __createOrResetPreventSystemSleepAssertion.count
+ __softClampNormalized
+ _alm_app_will_launch_with_signpost_id_and_metrics_payload
+ _foregroundConstraint.foregroundConstraint
+ _foregroundConstraint.onceToken
+ _objc_msgSend$_acquireSuspensionUnderLockExemptionIfNeeded
+ _objc_msgSend$_adjustPresentedMenuForGestureOverViewInContainer:forPanGesture:isDirectTouch:
+ _objc_msgSend$_allowsCapabilitySearchOnLockScreenWithExplanation:
+ _objc_msgSend$_anyRegisteredPresentationsMayBeConstrainedByUpdate:
+ _objc_msgSend$_applyCBDeviceLoss:
+ _objc_msgSend$_applyCBDeviceUpdate:
+ _objc_msgSend$_applyVolumeLimitedSizeLayout:
+ _objc_msgSend$_buildVolumeLeadingContentProviderForRingerSilent:
+ _objc_msgSend$_buildVolumeTrailingContentProvider
+ _objc_msgSend$_calculateResolvedSize:constraintHelper:
+ _objc_msgSend$_cbDeviceGlyphPropertiesDifferBetween:and:
+ _objc_msgSend$_createOrResetPreventSystemSleepAssertion
+ _objc_msgSend$_effectivePreferredSize
+ _objc_msgSend$_finalizeLaunchSignpostState
+ _objc_msgSend$_hardwareButtonPressedStateDidChange
+ _objc_msgSend$_headerIconImageInfo
+ _objc_msgSend$_indexOfCBDeviceWithIdentifier:
+ _objc_msgSend$_invalidateOrDeferPreferredMinimumTopInsetInteractive:
+ _objc_msgSend$_invalidatePreferredMinimumTopInsetInteractive:
+ _objc_msgSend$_isAnySceneLocked
+ _objc_msgSend$_isFocusRequestReasonBlocked:
+ _objc_msgSend$_isUniversalResizabilityEnabled
+ _objc_msgSend$_leadingStatusBarPartFrameInWindow:
+ _objc_msgSend$_notifyResizingChangedIfNeeded
+ _objc_msgSend$_performMainMenuCommandInvocationRequestForCommand:withSystemAuthenticationServiceMessage:session:
+ _objc_msgSend$_postAssistantIslandLayoutUpdate
+ _objc_msgSend$_presentMenuViewNonInteractively:forPointerHover:forKeyPress:
+ _objc_msgSend$_presentSIMSetupFlowWithFlowType:reason:
+ _objc_msgSend$_presentation:isConstrainedByContext:
+ _objc_msgSend$_releasePreventSystemSleepAssertion
+ _objc_msgSend$_scheduleReleaseOfPreventSystemSleepAssertion
+ _objc_msgSend$_sendResizingStatusToConnection:
+ _objc_msgSend$_setContentBorderWidth:
+ _objc_msgSend$_setDisplayedWithLimitedSize:
+ _objc_msgSend$_setHiddenStatusBarParts:
+ _objc_msgSend$_setLastInteractedResizableSceneHandle:
+ _objc_msgSend$_setPreferredSystemClipPadding:
+ _objc_msgSend$_setUnavailabilityReasons:
+ _objc_msgSend$_setWantsLayoutPassForClientUpdate:reason:
+ _objc_msgSend$_startCBDiscovery
+ _objc_msgSend$_statusBarStyleAttributesForAppOwningStatusBarPart:
+ _objc_msgSend$_unlockIfNecessaryAndPresentSIMSetupFlowWithFlowType:reason:unlockName:
+ _objc_msgSend$_updateAssistantIslandDodgeWithFrame:state:gestureInteractive:
+ _objc_msgSend$_updateBorderColor
+ _objc_msgSend$_updateClockMorphForProgress:velocity:forPresentationValue:
+ _objc_msgSend$_updateCompanionScenesForInterestedModes:registeredPresentations:
+ _objc_msgSend$_updateCompanionScenesForInterestedModes:registeredPresentations:update:
+ _objc_msgSend$_updateContentBorderAppearance
+ _objc_msgSend$_updateDisplayConfiguration:fence:
+ _objc_msgSend$_updateEffectiveTopInsetInteractive:
+ _objc_msgSend$_updateMapsShowingOnLockScreen
+ _objc_msgSend$_updateQueryIterationLabelVisibility
+ _objc_msgSend$_updateStatusBarRevealForProgress:
+ _objc_msgSend$_updateSystemApertureBehaviorSettings
+ _objc_msgSend$_updateTransientOverlayPresence
+ _objc_msgSend$_updateVisibilityForFrame:
+ _objc_msgSend$actionForPartWithIdentifier:
+ _objc_msgSend$addPropagatedProperty:
+ _objc_msgSend$adjustPresentedMenuForInteractionOverView:
+ _objc_msgSend$appLeadingStatusBarStyleAttributes
+ _objc_msgSend$appStatusBarThatContainsActivationView
+ _objc_msgSend$appTrailingStatusBarStyleAttributes
+ _objc_msgSend$backNavigationEntry
+ _objc_msgSend$beginCoordinatingSwitcherController:options:completion:
+ _objc_msgSend$blocksFocusRequestsForReasons
+ _objc_msgSend$btAddressData
+ _objc_msgSend$captureHardwareButton
+ _objc_msgSend$cbDeviceForAudioRoute:
+ _objc_msgSend$contentBorderDebugColorsEnabled
+ _objc_msgSend$contentBorderEnabled
+ _objc_msgSend$contentBorderEnabledForCompactLayout
+ _objc_msgSend$contentBorderEnabledForCustomLayout
+ _objc_msgSend$contentBorderEnabledForLimitedSize
+ _objc_msgSend$contentBorderEnabledForMinimalLayout
+ _objc_msgSend$contentBorderEnabledForNonLimitedSize
+ _objc_msgSend$contentBorderWidth
+ _objc_msgSend$currentRemoteSession
+ _objc_msgSend$dataByApplyingUpdate:keys:
+ _objc_msgSend$defaultLifecycleConstraints
+ _objc_msgSend$deviceType
+ _objc_msgSend$didConsumeLayoutUpdateRequestForHostedClient
+ _objc_msgSend$didPresentContextMenuForMainMenuView:forDirectTouchPan:
+ _objc_msgSend$displayProfileManager
+ _objc_msgSend$endCoordinatingSwitcherController:options:completion:
+ _objc_msgSend$existingEntryKeys
+ _objc_msgSend$foregroundConstraint
+ _objc_msgSend$handleDirectTouchPanOrLongPressReleased:
+ _objc_msgSend$handleMenuPanOrLongPressGesture:isDirectTouch:
+ _objc_msgSend$imposesConstraint
+ _objc_msgSend$initWithBundleIdentifiers:iconImageInfo:iconImageLoadPriority:
+ _objc_msgSend$initWithCoordinator:displayProfileManager:windowSceneManager:startupInterfaceOrientation:
+ _objc_msgSend$initWithDisplayBounds:
+ _objc_msgSend$initWithHostScene:sceneUpdate:
+ _objc_msgSend$initWithResizingSession:connection:delegate:
+ _objc_msgSend$initWithSceneManager:displayProfileManager:windowSceneManager:startupInterfaceOrientation:
+ _objc_msgSend$initWithSceneSpecification:parameters:
+ _objc_msgSend$initWithUnavailabilityReasons:resizableApplication:
+ _objc_msgSend$initWithWindowSceneManager:displayUniqueId:resizingCornerRadius:
+ _objc_msgSend$invalidateForClient
+ _objc_msgSend$invalidateForServer
+ _objc_msgSend$isConstrainedByContext:
+ _objc_msgSend$isDismissingMenuForPointerHoverOrDrag
+ _objc_msgSend$isPresentingMenuForPointerHoverOrDrag
+ _objc_msgSend$isStatusBarUnderlappedByAnyAppWindowControls
+ _objc_msgSend$isTransitioningMenuForInteraction
+ _objc_msgSend$isWallpaperEditorPresented
+ _objc_msgSend$launchCaptureApplication:
+ _objc_msgSend$lifecycleConstraints
+ _objc_msgSend$managesResizingSession:
+ _objc_msgSend$menuBarRecipientSceneHandle
+ _objc_msgSend$needOwnershipWarning:error:
+ _objc_msgSend$noteDownButtonPressed:
+ _objc_msgSend$noteUpButtonPressed:
+ _objc_msgSend$partAlphas
+ _objc_msgSend$placementMode
+ _objc_msgSend$preferredMinimumTopInsetDidInvalidateInteractive:
+ _objc_msgSend$preferredSystemClipPadding
+ _objc_msgSend$prepareForDisplayWithBounds:
+ _objc_msgSend$preventSystemSleepAssertionName
+ _objc_msgSend$primaryPlacement
+ _objc_msgSend$productID
+ _objc_msgSend$remoteAppResizingSessionDidInvalidate:
+ _objc_msgSend$requestAuthenticationMessageForSecureNamespace:context:clientVersionedPID:completion:
+ _objc_msgSend$resizableApplication
+ _objc_msgSend$resizingAvailability
+ _objc_msgSend$resizingAvailabilityOnResizableDisplays
+ _objc_msgSend$resizingCoordinator:didUpdateAvailability:preferredSize:
+ _objc_msgSend$resizingService
+ _objc_msgSend$sb_isDisplayResizable
+ _objc_msgSend$sceneSpecification
+ _objc_msgSend$sceneUpdate
+ _objc_msgSend$secondaryPlacement
+ _objc_msgSend$secureNamespace
+ _objc_msgSend$serverDidUpdateStatus:
+ _objc_msgSend$setAlpha:forParts:
+ _objc_msgSend$setBorderCornerRadius:
+ _objc_msgSend$setContentBorderDebugColorsEnabled:
+ _objc_msgSend$setContentBorderEnabled:
+ _objc_msgSend$setContentBorderEnabledForCompactLayout:
+ _objc_msgSend$setContentBorderEnabledForCustomLayout:
+ _objc_msgSend$setContentBorderEnabledForLimitedSize:
+ _objc_msgSend$setContentBorderEnabledForMinimalLayout:
+ _objc_msgSend$setContentBorderEnabledForNonLimitedSize:
+ _objc_msgSend$setContentBorderWidth:
+ _objc_msgSend$setCurrentMenuBarApplicationName:
+ _objc_msgSend$setDebugColorsEnabled:
+ _objc_msgSend$setDeviceFoundHandler:
+ _objc_msgSend$setDeviceLostHandler:
+ _objc_msgSend$setDiscoveryFlags:
+ _objc_msgSend$setDismissingMenuForPointerHoverOrDrag:
+ _objc_msgSend$setDismissingMenuForTouchDrag:
+ _objc_msgSend$setIsMapsOnLockScreen:
+ _objc_msgSend$setLifecycleConstraints:
+ _objc_msgSend$setMenuBarStatusBarFollowingAppLeadingStyle:
+ _objc_msgSend$setPartAlphas:
+ _objc_msgSend$setPreferredSystemClipPadding:
+ _objc_msgSend$setPresentingMenuForPointerHoverOrDrag:
+ _objc_msgSend$setPresentingMenuForTouchDrag:
+ _objc_msgSend$setReleasePreventSystemSleepAssertionTimer:
+ _objc_msgSend$setResizableDisplayUUID:initialFrame:
+ _objc_msgSend$setSystemAuthenticationServiceMessage:
+ _objc_msgSend$setWallpaperEditorPresented:
+ _objc_msgSend$setWantsLayoutPassForClientUpdateEnabled:
+ _objc_msgSend$shouldEvaluateConstraintForSceneUpdate:
+ _objc_msgSend$showQueryIterationLabel
+ _objc_msgSend$simulateClickActivationLaunchForBundleIdentifier:completion:
+ _objc_msgSend$simulateLaunchFromSource:bundleIdentifier:coverSheetViewController:completion:
+ _objc_msgSend$supportsDynamicSIMConfiguration
+ _objc_msgSend$switcherAddedMultipleApps
+ _objc_msgSend$switcherAddedSingleApp
+ _objc_msgSend$switcherFocusedWindowClosed
+ _objc_msgSend$switcherLayoutChangeRequests
+ _objc_msgSend$switcherUpdateTopmostApp
+ _objc_msgSend$transientOverlayOwningKeyboard
+ _objc_msgSend$updateBackgroundGlassEffectForDraggingProgress:usingGlassEffects:
+ _objc_msgSend$updateDisplayConfiguration:fence:
+ _objc_msgSend$updatePreferredSize:forAssertionWithIdentifier:
+ _objc_msgSend$userFocusRequestForScene:requestReason:completion:
+ _objc_msgSend$wantsInitialKeyboardFocus
+ _objc_msgSend$wantsLayoutPassForClientUpdateEnabled
+ _switcherAddedMultipleApps.onceToken
+ _switcherAddedMultipleApps.reason
+ _switcherAddedSingleApp.onceToken
+ _switcherAddedSingleApp.reason
+ _switcherFocusedWindowClosed.onceToken
+ _switcherFocusedWindowClosed.reason
+ _switcherLayoutChangeRequests.onceToken
+ _switcherLayoutChangeRequests.reasons
+ _switcherUpdateTopmostApp.onceToken
+ _switcherUpdateTopmostApp.reason
- +[SBAppResizingSession _constraintHelperForWindowSceneManager:sceneHandle:]
- -[SBAppResizingCoordinator _setLastInteractedResizableSceneHandle:provider:]
- -[SBAppResizingCoordinator initWithSceneManager:windowSceneManager:displayProfileManager:]
- -[SBAppResizingService initWithCoordinator:displayProfileManager:]
- -[SBAppResizingSession _calculateResolvedSize:]
- -[SBAppResizingSession addWindowScene:]
- -[SBAppResizingSession hostingWindowScene]
- -[SBAppResizingSession initWithWindowSceneManager:displayUniqueId:resizingCornerRadius:windowScenes:]
- -[SBAppResizingSession removeWindowScene:]
- -[SBBannerManager _invalidateOrDeferPreferredMinimumTopInset]
- -[SBBannerManager _invalidatePreferredMinimumTopInset]
- -[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:foreground:]
- -[SBCompanionScenePresentation initWithIdentifier:presenter:supportedModes:availableModes:context:]
- -[SBCompanionScenePresentationContext initWithDisplayConfiguration:frame:]
- -[SBContinuityDisplayRegionOfInterestViewController .cxx_destruct]
- -[SBContinuityDisplayRegionOfInterestViewController initWithView:]
- -[SBContinuityDisplayRegionOfInterestViewController resizingCoordinator:didUpdateActiveSession:]
- -[SBContinuityDisplayRegionOfInterestViewController resizingSession:didBeginResizingTransactionWithFrame:]
- -[SBContinuityDisplayRegionOfInterestViewController viewDidLoad]
- -[SBContinuityDisplayRegionOfInterestViewController viewWillLayoutSubviews]
- -[SBContinuityDisplayRegionOfInterestWindow initWithWindowScene:]
- -[SBContinuitySession resizingCoordinator:didUpdateResizability:preferredSize:]
- -[SBCoverSheetGrabberViewController _updateSpaceConstrainedAlpha]
- -[SBCoverSheetGrabberViewController setSystemApertureAvailable:]
- -[SBCoverSheetGrabberViewController systemApertureAvailable]
- -[SBCoverSheetSlidingViewController _setRealStatusBarHiddenIfApplicable:]
- -[SBCoverSheetSlidingViewController _updateClockMorphForProgress:forPresentationValue:]
- -[SBFluidSwitcherSpaceTitleItemController _iconImageForDisplayItem:]
- -[SBFluidSwitcherViewController statusBarStyleAttributesForScene:]
- -[SBIconController appSwitcherHeaderIconImageCache]
- -[SBMenuBarMainMenuView isDismissingMenuForPointerHover]
- -[SBMenuBarMainMenuView isPresentingMenuForPointerHover]
- -[SBMenuBarMainMenuView isTransitioningMenuForPointerInteraction]
- -[SBMenuBarMainMenuView setDismissingMenuForPointerHover:]
- -[SBMenuBarMainMenuView setPresentingMenuForPointerHover:]
- -[SBMenuBarManager currentMenuBarRecipientScene]
- -[SBMenuBarManager setCurrentMenuBarRecipientScene:]
- -[SBMenuBarPointerTrackingPanGestureRecognizer .cxx_destruct]
- -[SBMenuBarPointerTrackingPanGestureRecognizer initWithMenuBarViewController:]
- -[SBMenuBarPointerTrackingPanGestureRecognizer menuBarViewController]
- -[SBMenuBarPointerTrackingPanGestureRecognizer setMenuBarViewController:]
- -[SBMenuBarPointerTrackingPanGestureRecognizer touchesMoved:withEvent:]
- -[SBMenuBarViewController _adjustPresentedMenuForPointerOverViewInContainer:forPanGesture:]
- -[SBMenuBarViewController _handleMenuPanGesture:]
- -[SBMenuBarViewController _performMainMenuCommandInvocationRequestForCommand:withAuthenticationMessage:]
- -[SBMenuBarViewController _presentMenuViewNonInteractively:forPointerHover:]
- -[SBMenuBarViewController adjustPresentedMenuForPointerOverViewInContainer:]
- -[SBMenuBarViewController didPresentContextMenuForMainMenuView:]
- -[SBMinimumViableSwitcherTableViewController statusBarStyleAttributesForScene:]
- -[SBMutableCompanionScenePresentationContext setDisplayConfiguration:]
- -[SBMutableCompanionScenePresentationContext setFrame:]
- -[SBRemoteAppResizingSession _startObservingLockEvents:]
- -[SBRemoteAppResizingSession _stopObservingLockEvents:]
- -[SBRemoteAppResizingSession activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:]
- -[SBRemoteAppResizingSession activeInterfaceOrientationWillChangeToOrientation:]
- -[SBRemoteAppResizingSession initWithResizingSession:connection:]
- -[SBRemoteAppResizingSession invalidate]
- -[SBRemoteAppResizingSession lockStateProvider:didUpdateIsUILocked:]
- -[SBRemoteAppResizingSession resizingSession:didAddWindowScene:]
- -[SBRemoteAppResizingSession resizingSession:didRemoveWindowScene:]
- -[SBRemoteAppResizingSession resizingSession]
- -[SBResizableAppHostingViewController .cxx_destruct]
- -[SBResizableAppHostingViewController _createShieldWindowForWindowScene:]
- -[SBResizableAppHostingViewController _removeShieldWindowForWindowScene:]
- -[SBResizableAppHostingViewController _restoreSceneToSwitcher]
- -[SBResizableAppHostingViewController _setDebugUIEnabled:]
- -[SBResizableAppHostingViewController _setResizingSession:]
- -[SBResizableAppHostingViewController _showShieldWindows:]
- -[SBResizableAppHostingViewController _takeSceneFromSwitcher]
- -[SBResizableAppHostingViewController addChildViewController:]
- -[SBResizableAppHostingViewController initWithResizingSession:initialRegionOfInterestFrame:updateRegionOfInterestOnTransactionBegin:showShieldUI:]
- -[SBResizableAppHostingViewController initWithResizingSession:updateRegionOfInterestOnTransactionBegin:]
- -[SBResizableAppHostingViewController regionOfInterestView]
- -[SBResizableAppHostingViewController resizingSession:didAddWindowScene:]
- -[SBResizableAppHostingViewController resizingSession:didBeginResizingTransactionWithFrame:]
- -[SBResizableAppHostingViewController resizingSession:didCompleteResizingTransactionWithFrame:success:]
- -[SBResizableAppHostingViewController resizingSession:didRemoveWindowScene:]
- -[SBResizableAppHostingViewController resizingSession:didUpdateSceneHandle:]
- -[SBResizableAppHostingViewController resizingSessionDidInvalidate:]
- -[SBResizableAppHostingViewController resizingSession]
- -[SBResizableAppHostingViewController resizingShieldWindowDidTapButton:]
- -[SBResizableAppHostingViewController setRegionOfInterestView:]
- -[SBResizableAppHostingViewController setResizingSession:]
- -[SBResizableAppHostingViewController viewDidLoad]
- -[SBResizableAppHostingViewController viewWillLayoutSubviews]
- -[SBResizableAppHostingWindowSceneDelegate scene:willConnectToSession:options:]
- -[SBRingerAlertElement _leadingContentViewProviderForVolume]
- -[SBSAElementContext encodeWithCoder:]
- -[SBSSKDisplayProfileManager resizableDisplayUUID]
- -[SBSSKDisplayProfileManager setResizableDisplayUUID:]
- -[SBSwitcherController _sceneHandleForAppResize]
- -[SBSwitcherController _warmUpIconsForAppLayout:]
- -[SBSwitcherController _warmUpIconsForRecentAppLayouts]
- -[SBSwitcherController menuBarRecipientScene]
- -[SBSwitcherController moveLiveOverlayContentViewControllerFromAppHostingViewController:]
- -[SBSwitcherController moveLiveOverlayContentViewControllerToResizableAppHostingViewController:]
- -[SBSwitcherController statusBarStyleAttributesForScene:]
- GCC_except_table1041
- GCC_except_table1048
- GCC_except_table169
- GCC_except_table182
- GCC_except_table197
- GCC_except_table201
- GCC_except_table207
- GCC_except_table241
- GCC_except_table285
- GCC_except_table298
- GCC_except_table313
- GCC_except_table347
- GCC_except_table349
- GCC_except_table351
- GCC_except_table394
- GCC_except_table405
- GCC_except_table435
- GCC_except_table507
- GCC_except_table541
- GCC_except_table548
- GCC_except_table549
- GCC_except_table554
- GCC_except_table571
- GCC_except_table574
- GCC_except_table578
- GCC_except_table584
- GCC_except_table588
- GCC_except_table618
- GCC_except_table672
- GCC_except_table707
- GCC_except_table785
- GCC_except_table811
- GCC_except_table814
- GCC_except_table854
- GCC_except_table896
- GCC_except_table937
- GCC_except_table948
- GCC_except_table995
- OBJC_IVAR_$_SBCompanionScenePresentationContext._displayConfiguration
- OBJC_IVAR_$_SBCompanionScenePresentationContext._frame
- _BluetoothAccessoryInEarStatusNotification
- _OBJC_CLASS_$_CASDFGlassHighlightEffect
- _OBJC_CLASS_$_SBContinuityDisplayRegionOfInterestViewController
- _OBJC_CLASS_$_SBContinuityDisplayRegionOfInterestWindow
- _OBJC_CLASS_$_SBMenuBarPointerTrackingPanGestureRecognizer
- _OBJC_CLASS_$_SBResizableAppHostingViewController
- _OBJC_CLASS_$__UICompanionContainerSceneSpecification
- _OBJC_IVAR_$_SBAppResizingCoordinator._lastInteractedResizableSceneHandleProvider
- _OBJC_IVAR_$_SBCompanionSceneHostComponent._lock_isHostSceneForeground
- _OBJC_IVAR_$_SBContinuityDisplayRegionOfInterestViewController._regionOfInterestFrame
- _OBJC_IVAR_$_SBContinuityDisplayRegionOfInterestViewController._regionOfInterestView
- _OBJC_IVAR_$_SBCoverSheetGrabberViewController._systemApertureAvailable
- _OBJC_IVAR_$_SBIconController._appSwitcherHeaderIconImageCache
- _OBJC_IVAR_$_SBMenuBarMainMenuView._dismissingMenuForPointerHover
- _OBJC_IVAR_$_SBMenuBarMainMenuView._presentingMenuForPointerHover
- _OBJC_IVAR_$_SBMenuBarManager.__useStatusBarDataForMenu
- _OBJC_IVAR_$_SBMenuBarManager._currentMenuBarRecipientScene
- _OBJC_IVAR_$_SBMenuBarPointerTrackingPanGestureRecognizer._menuBarViewController
- _OBJC_IVAR_$_SBRemoteAppResizingSession._locallyInvalidated
- _OBJC_IVAR_$_SBResizableAppHostingViewController._appDefaults
- _OBJC_IVAR_$_SBResizableAppHostingViewController._initialRegionOfInterestFrame
- _OBJC_IVAR_$_SBResizableAppHostingViewController._regionOfInterestFrame
- _OBJC_IVAR_$_SBResizableAppHostingViewController._regionOfInterestView
- _OBJC_IVAR_$_SBResizableAppHostingViewController._resizingSession
- _OBJC_IVAR_$_SBResizableAppHostingViewController._shouldShowShieldUI
- _OBJC_IVAR_$_SBResizableAppHostingViewController._updateRegionOfInterestOnTransactionBegin
- _OBJC_IVAR_$_SBResizableAppHostingViewController._windowSceneIdentifiersToShieldWindows
- _OBJC_IVAR_$_SBResizableAppHostingWindowSceneDelegate._hostingVC
- _OBJC_IVAR_$_SBResizableAppHostingWindowSceneDelegate._hostingWindow
- _OBJC_IVAR_$_SBSSKDisplayProfileManager._resizableDisplayUUID
- _OBJC_IVAR_$_SBSwitcherGenieEffectView._rimHighlightSDFView
- _OBJC_METACLASS_$_SBContinuityDisplayRegionOfInterestViewController
- _OBJC_METACLASS_$_SBContinuityDisplayRegionOfInterestWindow
- _OBJC_METACLASS_$_SBMenuBarPointerTrackingPanGestureRecognizer
- _OBJC_METACLASS_$_SBResizableAppHostingViewController
- __OBJC_$_CLASS_METHODS_SBAppResizingSession
- __OBJC_$_INSTANCE_METHODS_SBCaptureHardwareButton
- __OBJC_$_INSTANCE_METHODS_SBChainableModifierEventResponse(SBSwitcherModifierEventResponse|SBWindowingModifierResponse)
- __OBJC_$_INSTANCE_METHODS_SBContinuityDisplayRegionOfInterestViewController
- __OBJC_$_INSTANCE_METHODS_SBContinuityDisplayRegionOfInterestWindow
- __OBJC_$_INSTANCE_METHODS_SBMenuBarPointerTrackingPanGestureRecognizer
- __OBJC_$_INSTANCE_METHODS_SBResizableAppHostingViewController
- __OBJC_$_INSTANCE_METHODS_SBSwitcherModifier(SharedModifierUtilities|WindowingModifier)
- __OBJC_$_INSTANCE_VARIABLES_SBContinuityDisplayRegionOfInterestViewController
- __OBJC_$_INSTANCE_VARIABLES_SBMenuBarPointerTrackingPanGestureRecognizer
- __OBJC_$_INSTANCE_VARIABLES_SBResizableAppHostingViewController
- __OBJC_$_PROP_LIST_SBContinuityDisplayRegionOfInterestViewController
- __OBJC_$_PROP_LIST_SBMenuBarPointerTrackingPanGestureRecognizer
- __OBJC_$_PROP_LIST_SBResizableAppHostingViewController
- __OBJC_CLASS_PROTOCOLS_$_SBContinuityDisplayRegionOfInterestViewController
- __OBJC_CLASS_PROTOCOLS_$_SBResizableAppHostingViewController
- __OBJC_CLASS_RO_$_SBContinuityDisplayRegionOfInterestViewController
- __OBJC_CLASS_RO_$_SBContinuityDisplayRegionOfInterestWindow
- __OBJC_CLASS_RO_$_SBMenuBarPointerTrackingPanGestureRecognizer
- __OBJC_CLASS_RO_$_SBResizableAppHostingViewController
- __OBJC_METACLASS_RO_$_SBContinuityDisplayRegionOfInterestViewController
- __OBJC_METACLASS_RO_$_SBContinuityDisplayRegionOfInterestWindow
- __OBJC_METACLASS_RO_$_SBMenuBarPointerTrackingPanGestureRecognizer
- __OBJC_METACLASS_RO_$_SBResizableAppHostingViewController
- __OBJC_PROTOCOL_REFERENCE_$_SBFullScreenSwitcherSceneLiveContentOverlay
- ___109-[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:foreground:]_block_invoke
- ___109-[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:foreground:]_block_invoke_2
- ___109-[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:foreground:]_block_invoke_3
- ___109-[SBCompanionSceneHostComponent _updateCompanionScenesForInterestedModes:registeredPresentations:foreground:]_block_invoke_4
- ___146-[SBResizableAppHostingViewController initWithResizingSession:initialRegionOfInterestFrame:updateRegionOfInterestOnTransactionBegin:showShieldUI:]_block_invoke
- ___49-[SBSwitcherController _warmUpIconsForAppLayout:]_block_invoke
- ___55-[SBMutableCompanionScenePresentationContext setFrame:]_block_invoke
- ___58-[SBHostProxyClientComponent _updateDisplayConfiguration:]_block_invoke
- ___58-[SBUserNotificationAlert updateWithMessage:requestFlags:]_block_invoke_4
- ___58-[SBUserNotificationAlert updateWithMessage:requestFlags:]_block_invoke_5
- ___63-[SBUserNotificationAlert _cleanupCustomContentViewControllers]_block_invoke
- ___65-[SBCoverSheetGrabberViewController _updateSpaceConstrainedAlpha]_block_invoke
- ___66-[SBAppResizingService initWithCoordinator:displayProfileManager:]_block_invoke
- ___69-[SBMenuBarManager _updateMenuBarActivationViewsWithApplicationName:]_block_invoke_4
- ___70-[SBMutableCompanionScenePresentationContext setDisplayConfiguration:]_block_invoke
- ___73-[SBSceneDestructionConfirmationViewController _presentConfirmationAlert]_block_invoke_4
- ___73-[SBSceneDestructionConfirmationViewController _presentConfirmationAlert]_block_invoke_5
- ___74-[SBCompanionScenePresentationContext initWithDisplayConfiguration:frame:]_block_invoke
- ___74-[SBCompanionScenePresentationContext initWithDisplayConfiguration:frame:]_block_invoke_2
- ___81-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:]_block_invoke
- ___81-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:]_block_invoke_2
- ___81-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:]_block_invoke_3
- ___81-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:]_block_invoke_4
- ___81-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:]_block_invoke_5
- ___81-[SBMainSwitcherControllerCoordinator endCoordinatingSwitcherController:options:]_block_invoke_6
- ___83-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:]_block_invoke
- ___83-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:]_block_invoke_2
- ___83-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:]_block_invoke_3
- ___83-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:]_block_invoke_4
- ___83-[SBMainSwitcherControllerCoordinator beginCoordinatingSwitcherController:options:]_block_invoke_5
- ___91-[SBMenuBarViewController _adjustPresentedMenuForPointerOverViewInContainer:forPanGesture:]_block_invoke
- ___block_descriptor_40_e8_32w_e23_v16?0"UIAlertAction"8lw32l8
- ___block_descriptor_48_e8_32s40w_e54_v24?0"BKSHIDEventAuthenticationMessage"8"NSError"16lw40l8s32l8
- ___block_descriptor_49_e8_32s40s_e21_v16?0"UIStatusBar"8ls32l8s40l8
- ___block_descriptor_65_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s_e35_v16?0"FBSMutableSceneParameters"8ls32l8
- _objc_msgSend$_adjustPresentedMenuForPointerOverViewInContainer:forPanGesture:
- _objc_msgSend$_calculateResolvedSize:
- _objc_msgSend$_constraintHelperForWindowSceneManager:sceneHandle:
- _objc_msgSend$_handleMenuPanGesture:
- _objc_msgSend$_hasShownSiriHeaderViewControllerDuringCurrentCarDNDSession
- _objc_msgSend$_invalidateOrDeferPreferredMinimumTopInset
- _objc_msgSend$_invalidatePreferredMinimumTopInset
- _objc_msgSend$_leadingContentViewProviderForVolume
- _objc_msgSend$_performMainMenuCommandInvocationRequestForCommand:withAuthenticationMessage:
- _objc_msgSend$_presentMenuViewNonInteractively:forPointerHover:
- _objc_msgSend$_requestSecurePasteAuthenticationMessageWithContext:forClientVersionedPID:completionBlock:
- _objc_msgSend$_restoreSceneToSwitcher
- _objc_msgSend$_sceneHandleForAppResize
- _objc_msgSend$_setDebugUIEnabled:
- _objc_msgSend$_setHasShownSiriHeaderViewControllerDuringCurrentCarDNDSession:
- _objc_msgSend$_setLastInteractedResizableSceneHandle:provider:
- _objc_msgSend$_setRealStatusBarHiddenIfApplicable:
- _objc_msgSend$_setResizingSession:
- _objc_msgSend$_showShieldWindows:
- _objc_msgSend$_stopObservingLockEvents:
- _objc_msgSend$_takeSceneFromSwitcher
- _objc_msgSend$_updateClockMorphForProgress:forPresentationValue:
- _objc_msgSend$_updateCompanionScenesForInterestedModes:registeredPresentations:foreground:
- _objc_msgSend$_updateSpaceConstrainedAlpha
- _objc_msgSend$_warmUpIconsForAppLayout:
- _objc_msgSend$addWindowScene:
- _objc_msgSend$adjustPresentedMenuForPointerOverViewInContainer:
- _objc_msgSend$appSwitcherHeaderIconImageCache
- _objc_msgSend$cacheImageForIcon:compatibleWithTraitCollection:options:completionHandler:
- _objc_msgSend$contentColor
- _objc_msgSend$contentProvider
- _objc_msgSend$didPresentContextMenuForMainMenuView:
- _objc_msgSend$encodeCGRect:forKey:
- _objc_msgSend$encodeDouble:forKey:
- _objc_msgSend$hostingWindowScene
- _objc_msgSend$inEarDetectEnabled
- _objc_msgSend$inEarStatusPrimary:secondary:
- _objc_msgSend$initWithCoordinator:displayProfileManager:
- _objc_msgSend$initWithResizingSession:connection:
- _objc_msgSend$initWithResizingSession:initialRegionOfInterestFrame:updateRegionOfInterestOnTransactionBegin:showShieldUI:
- _objc_msgSend$initWithResizingSession:updateRegionOfInterestOnTransactionBegin:
- _objc_msgSend$initWithSceneManager:windowSceneManager:displayProfileManager:
- _objc_msgSend$initWithWindowSceneManager:displayUniqueId:resizingCornerRadius:windowScenes:
- _objc_msgSend$isAppleAudioDevice
- _objc_msgSend$isDismissingMenuForPointerHover
- _objc_msgSend$isOverlayDisappearing
- _objc_msgSend$isPresentingMenuForPointerHover
- _objc_msgSend$isTransitioningMenuForPointerInteraction
- _objc_msgSend$menuBarRecipientScene
- _objc_msgSend$moveLiveOverlayContentViewControllerForSceneHandle:toViewController:
- _objc_msgSend$moveLiveOverlayContentViewControllerFromAppHostingViewController:
- _objc_msgSend$moveLiveOverlayContentViewControllerToResizableAppHostingViewController:
- _objc_msgSend$needsAuthenticationMessage
- _objc_msgSend$removeWindowScene:
- _objc_msgSend$resizingCoordinator:didUpdateResizability:preferredSize:
- _objc_msgSend$resizingSession
- _objc_msgSend$resizingSession:didAddWindowScene:
- _objc_msgSend$resizingSession:didRemoveWindowScene:
- _objc_msgSend$restoreLiveOverlayContentViewControllerToSwitcherForSceneHandle:
- _objc_msgSend$setAmount:
- _objc_msgSend$setAngle:
- _objc_msgSend$setAuthenticationMessage:
- _objc_msgSend$setContentDistribution:
- _objc_msgSend$setContentSpacing:
- _objc_msgSend$setDismissingMenuForPointerHover:
- _objc_msgSend$setOverlayDisappearing:
- _objc_msgSend$setPresentingMenuForPointerHover:
- _objc_msgSend$setResizingSession:
- _objc_msgSend$setShowSiriHeaderViewController:
- _objc_msgSend$setSpread:
- _objc_msgSend$shouldShowCarDNDUseSiriHeaderViewController
- _objc_msgSend$showRegionOfInterest
- _objc_msgSend$statusBarStyleAttributesForScene:
- _objc_msgSend$updateDisplayConfiguration:
- _objc_msgSend$updateMenuBar
- _objc_msgSend$updateRegionOfInterestOnTransactionBeginForResizingService
CStrings:
+ "%02X:%02X:%02X:%02X:%02X:%02X"
+ "%@ is not a known capture application"
+ "%{public}@ wantsLayoutPassForClientUpdate %{BOOL}u -> %{BOOL}u (reason: %{public}@)"
+ "-[SBAppResizingCoordinator _notifyResizingChangedIfNeeded]"
+ "-[SBAppResizingCoordinator _setLastInteractedResizableSceneHandle:]"
+ "-[SBAppResizingCoordinator resizableApplication]"
+ "-[SBAppResizingCoordinator resizingAvailability]"
+ "-[SBAppResizingCoordinator resizingService]"
+ "-[SBAppResizingSession isActive]"
+ "-[SBAppResizingSession prepareForDisplayWithBounds:]"
+ "-[SBBluetoothController _applyCBDeviceLoss:]"
+ "-[SBBluetoothController _applyCBDeviceUpdate:]"
+ "; associatedSystemApertureElementID: %@; contentScale: %@; contentBounds: %@; contentCenter: %@; keyLineMode: %@; keyLineTintColor: %@; sampledBackgroundLuminanceLevel: %@; shadowStyle: %@, renderingConfiguration: %@; elevationStyle: %@; isContentClippingEnabled: %@; isUserInteractionEnabled: %@; contentBorderWidth: %f;"
+ "<%@: %p; clientIdentifier: %@; elementIdentifier: %@; indicatorNeedsDisplayWellKnownLocation: %@; indicatorSize: %@; preferredEdgeOutsets: %@; interfaceOrientation: %@; preferredSystemClipPadding: %f; activeLayoutDirection: %@>"
+ "<%@: %p; clientIdentifier: %@; elementIdentifier: %@; layoutMode: %@; preferredEdgeOutsets: %@; interfaceOrientation: %@; systemApertureCustomLayout: %@; systemApertureCustomLayoutCustomAnimationStyle: %@; systemApertureLayoutCustomizingOptions: %@; activeDynamicAnimation: %@; keyColor: %@; preferredLeadingBounds: %@; preferredTrailingBounds: %@; preferredMinimalBounds: %@; viewControllerAppearState: %@; requestingMenuPresentation: %@; isLimitedSizeSupported: %@; isDisplayedWithLimitedSize: %@; preferredAvoidanceRect: %@; preferredAvoidanceCornerRadius: %f; activeLayoutDirection: %@; preferredSystemClipPadding: %f;>"
+ "<%p> Created extension content host view controller %p (extension: %{public}@)."
+ "<%p> Created legacy view service content host view controller %p (class: %{public}@, bundle: %{public}@)."
+ "<%p> Invalidate completion fired for extension content host view controller; disconnecting."
+ "<%p> Tearing down extension content host view controller: invalidating."
+ "<%p> Tearing down legacy view service content host view controller: disconnecting."
+ "<%{public}@> viewDidMoveToWindow, bailing on configuring scene entity because we don't have switcher controller"
+ "AppResizing"
+ "B32@?0@\"CBDevice\"8Q16^B24"
+ "Banner dodge latched off: Assistant Island frame %{public}@ exceeds half the display (%.0f)"
+ "Camera Control not available on this device"
+ "Capture application launch failed"
+ "Content Border"
+ "Content Border Debug Colors"
+ "Content bounds property changed and element is requesting a layout update for hosted client; consuming request and invalidating preferred component view size. element: %{public}@"
+ "DeviceUnsupported"
+ "Dropping suspended app launch for %{public}@ — scene %{public}@ is already live on lock screen"
+ "Enable For Compact Layout"
+ "Enable For Custom Layout"
+ "Enable For Limited Size"
+ "Enable For Minimal Layout"
+ "Enable For Non-Limited Size"
+ "Ethernet"
+ "Failed to beginCoordinating switcher. Tearing down resizing display"
+ "Failed to gather warning strings with error: %{public}@"
+ "Hardware button pressed"
+ "Hardware button pressed state changed: anyPressed=%{BOOL}u up=%{BOOL}u down=%{BOOL}u state=%{public}@"
+ "Hardware button released"
+ "Home Screen wallpaper editor presentation changed"
+ "Keyboard will be hosted outside app scene - app is not full screen"
+ "Keyboard will be hosted outside app scene - app is resizable (windowed apps)"
+ "Layout Pass For Client Update"
+ "LegacyApplication"
+ "NSString * _Nonnull SBResizingAvailabilityDescription(SBResizingAvailability)"
+ "No resizable app because %{public}@"
+ "No resizable app because %{public}@ isn't resizable: %{public}@"
+ "NoApplication"
+ "PreventSystemSleepSecurityIndicator"
+ "Process did exit due to FairPlay. Failing transaction."
+ "Process failed to bootstrap"
+ "Process failed to bootstrap %li"
+ "Process is nil on the scene's clientHandle and FBProcessManager, falling back to cached error from process exit"
+ "ResizingAvailable"
+ "SBAmbientPresentationControllerDidConnectNotification"
+ "SBApplication+SwitcherCapabilities.m"
+ "SBAssistantIslandLayoutDidChangeNotification"
+ "SBAssistantIslandLayoutIsInteractive"
+ "SBBluetoothAccessoryStateChangedNotification"
+ "SBBluetoothController CBDiscovery activate failed: %{public}@"
+ "SBCaptureApplicationLaunchSimulator.m"
+ "SBCompanionSceneConstraintContext.m"
+ "SBLockScreenService: insufficient authorization to simulate capture launch for client: %{public}@"
+ "SBResizableAppHostingWindowSceneDelegate connecting; screen bounds: %{public}@; coordinateSpace bounds: %{public}@"
+ "SBResizableAppHostingWindowSceneDelegate disconnected"
+ "SBStatusBarWholeBar"
+ "SBTraitsParticipantRoleAppHostingRegionOfInterest"
+ "Search is disallowed on the lock screen by the user's Allow Access When Locked settings"
+ "Starting with ROI initial frame: %@"
+ "Unlock for SIM Configuration"
+ "Updating %{public}@ via proxy with displayConfiguration: %{public}@ fence: %{public}@"
+ "[%@-%p] Skipping reconnection of remnant for unknown application: %@"
+ "[%@] Host scene is not active. Invalidating all companion scenes."
+ "[%{public}@] %{public}@ requiresPreflight: %{bool}u %{bool}u %{public}@"
+ "[%{public}@] Presentation \"%{public}@\" constrained by \"%{public}@\""
+ "[ActivityID: %{public}@] re-posted activity banner successfully"
+ "[Recording Indicator] Acquiring prevent system sleep assertion: %{public}@"
+ "[Recording Indicator] Extending prevent system sleep assertion: %{public}@"
+ "[Recording Indicator] MOT is not satisfied; resetting prevent system sleep assertion: %{public}@"
+ "[Recording Indicator] MOT is satisfied; allowing release of prevent system sleep assertion: %{public}@"
+ "[Recording Indicator] Releasing prevent system sleep assertion: %{public}@"
+ "[Recording Indicator] Scheduling release of prevent system sleep assertion: %{public}@"
+ "[Recording Indicator] Unable to acquire prevent system sleep assertion: %{public}@ - returned %#x"
+ "[SBTelephonyManager] Failed to query supportsDynamicSIMConfiguration: %{public}@"
+ "[coordinator] userFocusRequestForScene: %{public}@ -- (%{public}@) blocked request due to focus lock"
+ "[probe] lastInteracted cb: scene=%{public}@ ownsHandle=%d continuity=%d session=%{public}@"
+ "[unknown]"
+ "_UISystemAuthenticationService"
+ "_layoutHostMayNotPerformLayoutUpdate (applying transition parameters)"
+ "blockedFocusRequestReasons"
+ "blockedRequestReasons"
+ "bundleIdentifier != nil"
+ "calling continuitySession:didUpdateSceneSize: on %{public}@; size: %{public}@"
+ "capture hardware button refused launch"
+ "capture-launch simulation (%@)"
+ "cbDevice"
+ "clientSettings update: active accessory size change broke compact-layout symmetry"
+ "clientSettings update: preferred padding for compact layout changed"
+ "com.apple.springboard.recording-indicator.%d"
+ "com.apple.springboard.simulateCaptureLaunch"
+ "contentBorderDebugColorsEnabled"
+ "contentBorderEnabled"
+ "contentBorderEnabledForCompactLayout"
+ "contentBorderEnabledForCustomLayout"
+ "contentBorderEnabledForLimitedSize"
+ "contentBorderEnabledForMinimalLayout"
+ "contentBorderEnabledForNonLimitedSize"
+ "contentBorderWidth"
+ "contentProviderWillTransitionToSize (normal layout entry point)"
+ "cover sheet refused camera activation"
+ "device"
+ "didConsumeLayoutUpdateRequestForHostedClient (host consumed request)"
+ "failed to get authentication message for %{public}@: %{public}@"
+ "failing to acquire assertion as resizing is unavailable for reasons: %{public}@"
+ "fetchOrCreateNewStageController: refusing .activitySearch — device is locked and lock-screen access is disabled"
+ "hostScene"
+ "hostScene != ((void *)0)"
+ "invalidating"
+ "lifecycleConstraints"
+ "local network changed to %{public}@"
+ "no active cover sheet"
+ "no active lock screen manager"
+ "no icon manager found"
+ "nonInteractiveDisplay"
+ "partAlphas"
+ "requestReason"
+ "resize ended; restoring switcher."
+ "resizing"
+ "route"
+ "scene %@ for application %@ is already live on lock screen"
+ "scene update failed due to fairplay"
+ "sceneHandle is nil"
+ "sceneHandle's application is nil"
+ "sceneUpdate"
+ "setUnavailabilityReasons: added=%{public}@ removed=%{public}@ now=%{public}@"
+ "swipe source only supports com.apple.camera"
+ "switcher failed to restore; tearing down scene"
+ "switcher restored; tearing down scene"
+ "transientOverlayOwningKeyboard"
+ "transientOverlayPrefersKeyboardFocus"
+ "unexpected type: %@"
+ "unhandled SBResizingAvailability: %ld"
+ "v16@?0@\"<SBCompanionSceneConstraint>\"8"
+ "v16@?0@\"CBDevice\"8"
+ "v24@?0@8@\"NSError\"16"
+ "wantsLayoutPassForClientUpdateEnabled"
+ "\x91!\xb1"
+ "\xf0\xf0Q"
+ "\xf0\xf0\xd1"
+ "\xf0\xf0\xd1$"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0q"
- "-[SBAppResizingCoordinator _setLastInteractedResizableSceneHandle:provider:]"
- "-[SBAppResizingSession addWindowScene:]"
- "-[SBAppResizingSession removeWindowScene:]"
- "-[SBResizableAppHostingViewController _setResizingSession:]"
- "-[SBResizableAppHostingViewController resizingSession:didAddWindowScene:]"
- "-[SBResizableAppHostingViewController resizingSession:didRemoveWindowScene:]"
- "-[SBResizableAppHostingViewController resizingSession:didUpdateSceneHandle:]"
- "-[SBResizableAppHostingViewController resizingSessionDidInvalidate:]"
- "-[SBResizableAppHostingViewController resizingShieldWindowDidTapButton:]"
- "; associatedSystemApertureElementID: %@; contentScale: %@; contentBounds: %@; contentCenter: %@; keyLineMode: %@; keyLineTintColor: %@; sampledBackgroundLuminanceLevel: %@; shadowStyle: %@, renderingConfiguration: %@; elevationStyle: %@; isContentClippingEnabled: %@; isUserInteractionEnabled: %@;"
- "<%@: %p; clientIdentifier: %@; elementIdentifier: %@; indicatorNeedsDisplayWellKnownLocation: %@; indicatorSize: %@; preferredEdgeOutsets: %@; interfaceOrientation: %@; activeLayoutDirection: %@>"
- "<%@: %p; clientIdentifier: %@; elementIdentifier: %@; layoutMode: %@; preferredEdgeOutsets: %@; interfaceOrientation: %@; systemApertureCustomLayout: %@; systemApertureCustomLayoutCustomAnimationStyle: %@; systemApertureLayoutCustomizingOptions: %@; activeDynamicAnimation: %@; keyColor: %@; preferredLeadingBounds: %@; preferredTrailingBounds: %@; preferredMinimalBounds: %@; viewControllerAppearState: %@; requestingMenuPresentation: %@; isLimitedSizeSupported: %@; preferredAvoidanceRect: %@; preferredAvoidanceCornerRadius: %f; activeLayoutDirection: %@;>"
- "Already tracking UIWindowScene"
- "At begin: updating ROI frame to %{public}@"
- "At complete: updating ROI frame to %{public}@"
- "Dropping suspended-activation for %{public}@ — already live on lock screen"
- "Keyboard will be hosted outside app scene - !appSceneIsFullScreen: %{BOOL}d, appSceneAllowResizing: %{BOOL}d"
- "Not tracking UIWindowScene"
- "Not tracking session"
- "RR"
- "SBResizableAppHostingViewController.m"
- "System Aperture Query Iteration: "
- "Today overlay firing synchronous bs_beginAppearanceTransition:NO; oldProgress=%f appearState=%ld"
- "Unexpected scene type: %@"
- "Updating %{public}@ via proxy with displayConfiguration: %{public}@"
- "[%@] Host scene is background or not active. Invalidating all companion scenes."
- "[%{public}@] %{public}@ requiresPreflight: %{bool}u"
- "[%{public}@] setting _regionOfInterestView frame: %{public}@"
- "added multiple apps to stage"
- "added single app to stage"
- "appSwitcherHeaderIcon"
- "application %@ is already live on lock screen"
- "failed to get paste authentication request for %{public}@: %{public}@"
- "ignoring nil lastInteractedScene transition, as we're latched to: %p"
- "menuBarEntry"
- "preferredAvoidanceCornerRadius"
- "showRegionOfInterest"
- "update top most app on existing stage"
- "updating with resolved size: %{public}@"
- "v24@?0@\"BKSHIDEventAuthenticationMessage\"8@\"NSError\"16"
- "\x81!\xb1"
- "\xf0\xf0\xb1$"
- "\xf0\xf0\xe1"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb1"

```
