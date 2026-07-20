## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_nlcatlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-4626.103.0.0.0
-  __TEXT.__text: 0xaf3d70
+4630.1.102.0.0
+  __TEXT.__text: 0xaf7f74
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xbc5e8
+  __TEXT.__objc_methlist: 0xbcab8
   __TEXT.__const: 0x112a0
-  __TEXT.__oslogstring: 0x6286e
-  __TEXT.__cstring: 0x83fbd
-  __TEXT.__gcc_except_tab: 0x1823c
+  __TEXT.__oslogstring: 0x6312a
+  __TEXT.__cstring: 0x8435f
+  __TEXT.__gcc_except_tab: 0x181f4
   __TEXT.__ustring: 0xd04
   __TEXT.__dlopen_cstrs: 0x373
-  __TEXT.__unwind_info: 0x2e090
+  __TEXT.__unwind_info: 0x2e170
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d6a8
-  __DATA_CONST.__objc_classlist: 0x5450
+  __DATA_CONST.__const: 0x1d730
+  __DATA_CONST.__objc_classlist: 0x5478
   __DATA_CONST.__objc_catlist: 0x338
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2a90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4df50
+  __DATA_CONST.__objc_selrefs: 0x4e198
   __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__objc_superrefs: 0x4030
+  __DATA_CONST.__objc_superrefs: 0x4048
   __DATA_CONST.__objc_arraydata: 0x18a0
-  __DATA_CONST.__got: 0xa8c0
-  __AUTH_CONST.__const: 0x10ad8
-  __AUTH_CONST.__cfstring: 0x73a40
-  __AUTH_CONST.__objc_const: 0x283c68
+  __DATA_CONST.__got: 0xa8b8
+  __AUTH_CONST.__const: 0x10af8
+  __AUTH_CONST.__cfstring: 0x73ca0
+  __AUTH_CONST.__objc_const: 0x285030
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1758
   __AUTH_CONST.__objc_doubleobj: 0x820
   __AUTH_CONST.__objc_intobj: 0x2c88
   __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH_CONST.__auth_got: 0x2ba8
-  __AUTH.__objc_data: 0xde80
-  __DATA.__objc_ivar: 0xfa5c
+  __AUTH_CONST.__auth_got: 0x2bc0
+  __AUTH.__objc_data: 0xe010
+  __DATA.__objc_ivar: 0xfaa4
   __DATA.__data: 0x20bc0
-  __DATA.__bss: 0xa00
+  __DATA.__bss: 0xa28
   __DATA.__common: 0xa40
   __DATA_DIRTY.__objc_data: 0x26ca0
   __DATA_DIRTY.__data: 0x140

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  Functions: 72987
-  Symbols:   151020
-  CStrings:  23279
+  Functions: 73090
+  Symbols:   151251
+  CStrings:  23326
 
Symbols:
+ +[SBResourceConditionsAssistantIslandHostExtension hostComponents]
+ +[SBResourceConditionsSceneHostExtension hostComponents]
+ -[SBActivationInfoViewController _displayLabelForKey:]
+ -[SBActivationInfoViewController _repinActivationTableHeight]
+ -[SBActivationInfoViewController activateForESIMSetupButton]
+ -[SBAlertItemsController presentedAlertItems]
+ -[SBAppViewController containerDidUpdateTraitsParticipant:]
+ -[SBApplicationSceneUpdateTransaction _createSceneAndRunPreflight]
+ -[SBApplicationSceneUpdateTransaction _isScenePendingRemovalFromWorkspace]
+ -[SBAssistantIslandStageController transientOverlayPresentationManager:willPresentViewController:]
+ -[SBBluetoothController firstCBDeviceToReportBatteryLevel]
+ -[SBBluetoothController hasConnectedDevice]
+ -[SBBluetoothController indexOfDevice:]
+ -[SBCompanionSceneHostComponent _requestDismissalForCompanionScene:ofPresentation:invalidateCompanionScene:]
+ -[SBCompanionSceneHostComponent scene:willUpdateSettings:]
+ -[SBCompanionScenePresentation _willRequestDismissalForCompanionScene:]
+ -[SBDashBoardCameraContainerViewController _acquireTraitsParticipant]
+ -[SBDashBoardCameraPageViewController _acquireTraitsParticipant]
+ -[SBDashBoardCameraPageViewController setTraitsParticipant:]
+ -[SBDashBoardCameraPageViewController traitsParticipant]
+ -[SBDashBoardHostedAppViewController containerDidUpdateTraitsParticipant:]
+ -[SBDashBoardPearlUnlockBehavior _armMatchPasscodeFallbackTimerIfNeeded]
+ -[SBDashBoardPearlUnlockBehavior _handleMatchPasscodeFallbackForEvent:]
+ -[SBDashBoardPearlUnlockBehavior _invalidateMatchPasscodeFallbackTimer]
+ -[SBDashBoardPearlUnlockBehavior _matchPasscodeFallbackFailureSettings]
+ -[SBDashBoardPearlUnlockBehavior _matchPasscodeFallbackInterval]
+ -[SBDashBoardPearlUnlockBehavior _matchPasscodeFallbackTimerFired]
+ -[SBDashBoardPearlUnlockBehavior _matchPasscodeFallbackTimer]
+ -[SBDashBoardPearlUnlockBehavior dealloc]
+ -[SBDashBoardSetupViewController _activateForESIMSetupButtonTapped:]
+ -[SBDelayedPressInfo isLongClick]
+ -[SBDelayedPressInfo setLongClick:]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _preflightSupportedInterfaceOrientations]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider constrainsContainingSceneOrientation]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider contentWantsSimplifiedOrientationBehavior]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider scene:didUpdateClientSettings:]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider shouldFollowSceneOrientation]
+ -[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider supportedInterfaceOrientations]
+ -[SBDeviceApplicationSceneHandle(TraitsSceneDelegateStateTracking) _overlayInterfaceOrientationConstraint]
+ -[SBDeviceApplicationSceneHandle(TraitsSceneDelegateStateTracking) _setOverlayInterfaceOrientationConstraint:]
+ -[SBDeviceApplicationSceneOverlayViewProvider constrainsContainingSceneOrientation]
+ -[SBDeviceApplicationSceneViewController _updateOverlayInterfaceOrientationConstraint]
+ -[SBDeviceApplicationSceneViewController overlayViewProviderDidChangeSupportedInterfaceOrientations:]
+ -[SBDynamicFlashlightActivityElement preferredSystemClipPadding]
+ -[SBDynamicMemoryLimitApplicationSceneHostComponent _invalidateMemoryLimitAssertionForUpcomingSettingsUpdate:]
+ -[SBDynamicMemoryLimitApplicationSceneHostComponent _reconcileApplicationSceneAssertionForForegroundStateChange:upcomingSettingsUpdate:]
+ -[SBDynamicMemoryLimitApplicationSceneHostComponent scene:willUpdateSettings:]
+ -[SBFluidSwitcherViewController isTransitioningToEnvironmentWithoutStatusBar]
+ -[SBFullScreenSwitcherLiveContentOverlayCoordinator traitsParticipantForFullScreenSwitcherSceneLiveContentOverlay:]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay setSwitcherSceneLiveContentOverlayDelegate:]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay switcherSceneLiveContentOverlayDelegate]
+ -[SBLongPressGestureRecognizer _updateHardwareLongPressRegistration]
+ -[SBLongPressGestureRecognizer beginsOnHardwareLongPress]
+ -[SBLongPressGestureRecognizer dealloc]
+ -[SBLongPressGestureRecognizer setBeginsOnHardwareLongPress:]
+ -[SBLongPressGestureRecognizer setState:]
+ -[SBMainSwitcherControllerCoordinator switcherContentControllerWantsToUpdateMenuBarVisibility:preserveMenuBarIfInteractionOngoing:]
+ -[SBMenuBarActivationView _updateLabelFromStyleAttributesWithApplicationNameChange:]
+ -[SBMenuBarHeaderContainerView animateToPresented:fadeAppMenu:completion:]
+ -[SBMenuBarManager _isPointerOverMenuBarRegion]
+ -[SBMenuBarManager _menuBarProvidingAppExists]
+ -[SBMenuBarManager _scheduleDismissPeekedMenuBarTimerIfNecessary]
+ -[SBMenuBarManager _updateMenuBarVisibilityWithRequestedVisibility:preserveMenuBarIfInteractionOngoing:]
+ -[SBMenuBarManager updateMenuBarVisibilityPreserveIfInteractionOngoing:]
+ -[SBMenuBarViewController dismissAnimated:fadeAppMenu:alongsideAnimations:completion:]
+ -[SBMinimumViableSwitcherTableViewController isTransitioningToEnvironmentWithoutStatusBar]
+ -[SBNotificationCarPlayDestination _drainPendingFallbackBannerRequestsIfPossible]
+ -[SBNotificationCarPlayDestination _enqueueFallbackBannerForRequest:]
+ -[SBNotificationCarPlayDestination _handleAnnounceTimeoutForLinwoodPreprocess]
+ -[SBNotificationCarPlayDestination _postCarPlayBannerForRequest:]
+ -[SBNotificationCarPlayDestination _presentSuccessBannerForRequest:]
+ -[SBNotificationCarPlayDestination _registerBannerPresentedForRequest:skipReasonForLogging:]
+ -[SBPressGestureRecognizer latestPressWasLongClick]
+ -[SBRecordingIndicatorSystemApertureElement _indicatorContentSide]
+ -[SBRecordingIndicatorSystemApertureElement indicatorContentRendersAsSquare]
+ -[SBResourceConditionsAssistantIslandHostComponent _updateActiveState:]
+ -[SBResourceConditionsAssistantIslandHostComponent _updateActiveStateWithClientSettings:]
+ -[SBResourceConditionsAssistantIslandHostComponent invalidate]
+ -[SBResourceConditionsAssistantIslandHostComponent scene:didUpdateClientSettings:]
+ -[SBResourceConditionsAssistantIslandHostComponent setScene:]
+ -[SBResourceConditionsCoordinator .cxx_destruct]
+ -[SBResourceConditionsCoordinator _recomputeMemoryPressure]
+ -[SBResourceConditionsCoordinator addObserver:]
+ -[SBResourceConditionsCoordinator init]
+ -[SBResourceConditionsCoordinator memoryPressure]
+ -[SBResourceConditionsCoordinator removeObserver:]
+ -[SBResourceConditionsCoordinator scene:didChangeAssistantIslandActiveStateTo:]
+ -[SBResourceConditionsCoordinator scene:didChangeForegroundStateTo:]
+ -[SBResourceConditionsCoordinator scene:didChangeParentSceneTo:]
+ -[SBResourceConditionsSceneHostComponent .cxx_destruct]
+ -[SBResourceConditionsSceneHostComponent _updateSceneMemoryPressure]
+ -[SBResourceConditionsSceneHostComponent invalidate]
+ -[SBResourceConditionsSceneHostComponent resourceConditionsCoordinator:memoryPressureDidChange:]
+ -[SBResourceConditionsSceneHostComponent scene:didUpdateSettings:]
+ -[SBResourceConditionsSceneHostComponent setScene:]
+ -[SBRingerAlertElement _accessibilityLabelForRingerSilent:]
+ -[SBSAContainerResizeBehaviorProvider _detachedCustomResizedFrameForContainerViewDescription:resizedWithGestureDescription:initialContainerViewFrame:context:]
+ -[SBSAIndicatorElementContext _setIndicatorContentRendersAsSquare:]
+ -[SBSAIndicatorElementContext indicatorContentRendersAsSquare]
+ -[SBSAIndicatorElementContextMutator indicatorContentRendersAsSquare]
+ -[SBSAIndicatorElementContextMutator setIndicatorContentRendersAsSquare:]
+ -[SBSAPlatformMetricsContext _setDisplayCornerRadiusIgnoringZoom:]
+ -[SBSAPlatformMetricsContext copyBySettingDisplayCornerRadiusIgnoringZoom:]
+ -[SBSAPlatformMetricsContext displayCornerRadiusIgnoringZoom]
+ -[SBSAPlatformMetricsContextMutator displayCornerRadiusIgnoringZoom]
+ -[SBSAPlatformMetricsContextMutator setDisplayCornerRadiusIgnoringZoom:]
+ -[SBSwitcherController menuBarCanBeShownNow]
+ -[SBSwitcherController shouldMenuBarDismissToEnvironmentWithHiddenStatusBar]
+ -[SBSystemApertureSettings colorDifferentiateMinimumContainerOutset]
+ -[SBSystemApertureSettings cornerIndicatorEdgeInset]
+ -[SBSystemApertureSettings detachedCustomResizeDragFactor]
+ -[SBSystemApertureSettings detachedCustomResizeRangeBeginTracking]
+ -[SBSystemApertureSettings detachedCustomResizeRangeEndTracking]
+ -[SBSystemApertureSettings detachedCustomResizeRubberbandingCompress]
+ -[SBSystemApertureSettings detachedCustomResizeRubberbandingStretch]
+ -[SBSystemApertureSettings detachedCustomResizeWidthCollapseFactor]
+ -[SBSystemApertureSettings limitedSizeCompactIntraPaddingPerpendicular]
+ -[SBSystemApertureSettings limitedSizeCompactIntraPadding]
+ -[SBSystemApertureSettings minimumIndicatorSize]
+ -[SBSystemApertureSettings setColorDifferentiateMinimumContainerOutset:]
+ -[SBSystemApertureSettings setCornerIndicatorEdgeInset:]
+ -[SBSystemApertureSettings setDetachedCustomResizeDragFactor:]
+ -[SBSystemApertureSettings setDetachedCustomResizeRangeBeginTracking:]
+ -[SBSystemApertureSettings setDetachedCustomResizeRangeEndTracking:]
+ -[SBSystemApertureSettings setDetachedCustomResizeRubberbandingCompress:]
+ -[SBSystemApertureSettings setDetachedCustomResizeRubberbandingStretch:]
+ -[SBSystemApertureSettings setDetachedCustomResizeWidthCollapseFactor:]
+ -[SBSystemApertureSettings setLimitedSizeCompactIntraPadding:]
+ -[SBSystemApertureSettings setLimitedSizeCompactIntraPaddingPerpendicular:]
+ -[SBSystemApertureSettings setMinimumIndicatorSize:]
+ -[SBTelephonyManager activateForEsimSetupInBuddy]
+ -[SBTelephonyManager isSharingIdentitySupported]
+ -[SpringBoard _shouldHandleHardwareButtonsForDisplay:]
+ -[SpringBoard resourceConditionsCoordinator]
+ GCC_except_table1044
+ GCC_except_table1051
+ GCC_except_table1053
+ GCC_except_table1055
+ GCC_except_table1057
+ GCC_except_table1059
+ GCC_except_table1061
+ GCC_except_table1063
+ GCC_except_table167
+ GCC_except_table178
+ GCC_except_table199
+ GCC_except_table271
+ GCC_except_table283
+ GCC_except_table355
+ GCC_except_table429
+ GCC_except_table433
+ GCC_except_table503
+ GCC_except_table529
+ GCC_except_table531
+ GCC_except_table552
+ GCC_except_table554
+ GCC_except_table557
+ GCC_except_table559
+ GCC_except_table561
+ GCC_except_table577
+ GCC_except_table581
+ GCC_except_table587
+ GCC_except_table591
+ GCC_except_table621
+ GCC_except_table675
+ GCC_except_table710
+ GCC_except_table788
+ GCC_except_table814
+ GCC_except_table817
+ GCC_except_table857
+ GCC_except_table899
+ GCC_except_table901
+ GCC_except_table940
+ GCC_except_table951
+ GCC_except_table998
+ _OBJC_CLASS_$_CSLockScreenBiometricFailureSettings
+ _OBJC_CLASS_$_SBResourceConditionsAssistantIslandHostComponent
+ _OBJC_CLASS_$_SBResourceConditionsAssistantIslandHostExtension
+ _OBJC_CLASS_$_SBResourceConditionsCoordinator
+ _OBJC_CLASS_$_SBResourceConditionsSceneHostComponent
+ _OBJC_CLASS_$_SBResourceConditionsSceneHostExtension
+ _OBJC_IVAR_$_SBActivationInfoViewController._activateForESIMSetupButton
+ _OBJC_IVAR_$_SBBluetoothController._couldReportBatteryLevel
+ _OBJC_IVAR_$_SBBluetoothController._devices
+ _OBJC_IVAR_$_SBBluetoothController._discovery
+ _OBJC_IVAR_$_SBBluetoothController._latestBatteryLevel
+ _OBJC_IVAR_$_SBBluetoothController._tetheringConnected
+ _OBJC_IVAR_$_SBDashBoardPearlUnlockBehavior._matchPasscodeFallbackTimer
+ _OBJC_IVAR_$_SBDelayedPressInfo._longClick
+ _OBJC_IVAR_$_SBDeviceApplicationRemoteTransientOverlayViewProvider._needsCounterRotationReevaluationForFirstSupportedOrientationsUpdate
+ _OBJC_IVAR_$_SBDeviceApplicationSceneHandle._overlayInterfaceOrientationConstraint
+ _OBJC_IVAR_$_SBDeviceApplicationSceneOverlayViewProvider._reportedSupportedInterfaceOrientations
+ _OBJC_IVAR_$_SBDynamicMemoryLimitApplicationSceneHostComponent._isManagingApplicationSceneAssertion
+ _OBJC_IVAR_$_SBFullScreenSwitcherSceneLiveContentOverlay._switcherSceneLiveContentOverlayDelegate
+ _OBJC_IVAR_$_SBLongPressGestureRecognizer._beginsOnHardwareLongPress
+ _OBJC_IVAR_$_SBLongPressGestureRecognizer._hardwareLongPressActive
+ _OBJC_IVAR_$_SBNotificationCarPlayDestination._fallbackBannerInFlight
+ _OBJC_IVAR_$_SBNotificationCarPlayDestination._notificationIdentifiersWithPresentedBanner
+ _OBJC_IVAR_$_SBNotificationCarPlayDestination._pendingFallbackBannerRequests
+ _OBJC_IVAR_$_SBPressGestureRecognizer._latestDispatchedPressWasLongClick
+ _OBJC_IVAR_$_SBResourceConditionsAssistantIslandHostComponent._assistantIslandActive
+ _OBJC_IVAR_$_SBResourceConditionsCoordinator._assistantIslandActiveScenes
+ _OBJC_IVAR_$_SBResourceConditionsCoordinator._foregroundScenes
+ _OBJC_IVAR_$_SBResourceConditionsCoordinator._memoryPressure
+ _OBJC_IVAR_$_SBResourceConditionsCoordinator._observers
+ _OBJC_IVAR_$_SBResourceConditionsSceneHostComponent._parentScene
+ _OBJC_IVAR_$_SBSAIndicatorElementContext._indicatorContentRendersAsSquare
+ _OBJC_IVAR_$_SBSystemApertureSettings._colorDifferentiateMinimumContainerOutset
+ _OBJC_IVAR_$_SBSystemApertureSettings._cornerIndicatorEdgeInset
+ _OBJC_IVAR_$_SBSystemApertureSettings._detachedCustomResizeDragFactor
+ _OBJC_IVAR_$_SBSystemApertureSettings._detachedCustomResizeRangeBeginTracking
+ _OBJC_IVAR_$_SBSystemApertureSettings._detachedCustomResizeRangeEndTracking
+ _OBJC_IVAR_$_SBSystemApertureSettings._detachedCustomResizeRubberbandingCompress
+ _OBJC_IVAR_$_SBSystemApertureSettings._detachedCustomResizeRubberbandingStretch
+ _OBJC_IVAR_$_SBSystemApertureSettings._detachedCustomResizeWidthCollapseFactor
+ _OBJC_IVAR_$_SBSystemApertureSettings._limitedSizeCompactIntraPadding
+ _OBJC_IVAR_$_SBSystemApertureSettings._limitedSizeCompactIntraPaddingPerpendicular
+ _OBJC_IVAR_$_SBSystemApertureSettings._minimumIndicatorSize
+ _OBJC_IVAR_$_SBTelephonyManager._isSharingIdentitySupported
+ _OBJC_IVAR_$_SBTransitionSwitcherModifier._fromAppLayout
+ _OBJC_IVAR_$_SBTransitionSwitcherModifier._toAppLayout
+ _OBJC_IVAR_$_SpringBoard._resourceConditionsCoordinator
+ _OBJC_METACLASS_$_SBResourceConditionsAssistantIslandHostComponent
+ _OBJC_METACLASS_$_SBResourceConditionsAssistantIslandHostExtension
+ _OBJC_METACLASS_$_SBResourceConditionsCoordinator
+ _OBJC_METACLASS_$_SBResourceConditionsSceneHostComponent
+ _OBJC_METACLASS_$_SBResourceConditionsSceneHostExtension
+ _SBFloatCeilForScale
+ _SBLogResourceConditions
+ _SBLogResourceConditions.__logObj
+ _SBLogResourceConditions.onceToken
+ _SBLogShipMode
+ _SBLogShipMode.__logObj
+ _SBLogShipMode.onceToken
+ _SBTraitsParticipantRoleAppResizingShield
+ _SBWorkspaceTransitionEventLabelContinuityScreenConnect
+ __NSStringFromUISceneResourceConditionsMemoryPressure
+ __OBJC_$_CLASS_METHODS_SBResourceConditionsAssistantIslandHostExtension
+ __OBJC_$_CLASS_METHODS_SBResourceConditionsSceneHostExtension
+ __OBJC_$_INSTANCE_METHODS_SBChainableModifierEventResponse(SBSwitcherModifierEventResponse|SBWindowingModifierResponse)
+ __OBJC_$_INSTANCE_METHODS_SBResourceConditionsAssistantIslandHostComponent
+ __OBJC_$_INSTANCE_METHODS_SBResourceConditionsCoordinator
+ __OBJC_$_INSTANCE_METHODS_SBResourceConditionsSceneHostComponent
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherModifier(SharedModifierUtilities|WindowingModifier)
+ __OBJC_$_INSTANCE_VARIABLES_SBResourceConditionsAssistantIslandHostComponent
+ __OBJC_$_INSTANCE_VARIABLES_SBResourceConditionsCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_SBResourceConditionsSceneHostComponent
+ __OBJC_$_PROP_LIST_SBResourceConditionsAssistantIslandHostComponent
+ __OBJC_$_PROP_LIST_SBResourceConditionsCoordinator
+ __OBJC_$_PROP_LIST_SBResourceConditionsSceneHostComponent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBCompanionScenePresenting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBResourceConditionsCoordinatorObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBResourceConditionsCoordinatorObserver
+ __OBJC_$_PROTOCOL_REFS_SBResourceConditionsCoordinatorObserver
+ __OBJC_CLASS_PROTOCOLS_$_SBResourceConditionsAssistantIslandHostComponent
+ __OBJC_CLASS_PROTOCOLS_$_SBResourceConditionsSceneHostComponent
+ __OBJC_CLASS_RO_$_SBResourceConditionsAssistantIslandHostComponent
+ __OBJC_CLASS_RO_$_SBResourceConditionsAssistantIslandHostExtension
+ __OBJC_CLASS_RO_$_SBResourceConditionsCoordinator
+ __OBJC_CLASS_RO_$_SBResourceConditionsSceneHostComponent
+ __OBJC_CLASS_RO_$_SBResourceConditionsSceneHostExtension
+ __OBJC_LABEL_PROTOCOL_$_SBResourceConditionsCoordinatorObserver
+ __OBJC_METACLASS_RO_$_SBResourceConditionsAssistantIslandHostComponent
+ __OBJC_METACLASS_RO_$_SBResourceConditionsAssistantIslandHostExtension
+ __OBJC_METACLASS_RO_$_SBResourceConditionsCoordinator
+ __OBJC_METACLASS_RO_$_SBResourceConditionsSceneHostComponent
+ __OBJC_METACLASS_RO_$_SBResourceConditionsSceneHostExtension
+ __OBJC_PROTOCOL_$_SBResourceConditionsCoordinatorObserver
+ __SBHardwareButtonServiceIfAvailable
+ __SBSAMinimumIndicatorContainerSize
+ ___108-[SBCompanionSceneHostComponent _requestDismissalForCompanionScene:ofPresentation:invalidateCompanionScene:]_block_invoke
+ ___108-[SBCompanionSceneHostComponent _requestDismissalForCompanionScene:ofPresentation:invalidateCompanionScene:]_block_invoke_2
+ ___110-[SBDynamicMemoryLimitApplicationSceneHostComponent _invalidateMemoryLimitAssertionForUpcomingSettingsUpdate:]_block_invoke
+ ___110-[SBDynamicMemoryLimitApplicationSceneHostComponent _invalidateMemoryLimitAssertionForUpcomingSettingsUpdate:]_block_invoke_2
+ ___110-[SBDynamicMemoryLimitApplicationSceneHostComponent _invalidateMemoryLimitAssertionForUpcomingSettingsUpdate:]_block_invoke_3
+ ___39-[SBBluetoothController indexOfDevice:]_block_invoke
+ ___39-[SBSAIndicatorElementContext isEqual:]_block_invoke_10
+ ___48-[SBBluetoothController startWatchingForDevices]_block_invoke
+ ___48-[SBBluetoothController startWatchingForDevices]_block_invoke_2
+ ___48-[SBBluetoothController startWatchingForDevices]_block_invoke_3
+ ___48-[SBBluetoothController startWatchingForDevices]_block_invoke_4
+ ___49-[SBTelephonyManager activateForEsimSetupInBuddy]_block_invoke
+ ___50-[SBAppResizingSession _updateToFrame:completion:]_block_invoke_6
+ ___50-[SBAppResizingSession _updateToFrame:completion:]_block_invoke_7
+ ___50-[SBAppResizingSession _updateToFrame:completion:]_block_invoke_8
+ ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke_7
+ ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke_8
+ ___64-[SBDashBoardCameraPageViewController _acquireTraitsParticipant]_block_invoke
+ ___64-[SBDashBoardCameraPageViewController _acquireTraitsParticipant]_block_invoke_2
+ ___65-[SBMenuBarManager _scheduleDismissPeekedMenuBarTimerIfNecessary]_block_invoke
+ ___66-[SBApplicationSceneUpdateTransaction _createSceneAndRunPreflight]_block_invoke
+ ___66-[SBApplicationSceneUpdateTransaction _createSceneAndRunPreflight]_block_invoke_2
+ ___66-[SBApplicationSceneUpdateTransaction _createSceneAndRunPreflight]_block_invoke_3
+ ___69-[SBDashBoardCameraContainerViewController _acquireTraitsParticipant]_block_invoke
+ ___69-[SBDashBoardCameraContainerViewController _acquireTraitsParticipant]_block_invoke_2
+ ___69-[SBMenuBarManager _updateMenuBarActivationViewsWithApplicationName:]_block_invoke_4
+ ___72-[SBDashBoardPearlUnlockBehavior _armMatchPasscodeFallbackTimerIfNeeded]_block_invoke
+ ___74-[SBMenuBarHeaderContainerView animateToPresented:fadeAppMenu:completion:]_block_invoke
+ ___74-[SBMenuBarHeaderContainerView animateToPresented:fadeAppMenu:completion:]_block_invoke_2
+ ___74-[SBMenuBarHeaderContainerView animateToPresented:fadeAppMenu:completion:]_block_invoke_3
+ ___75-[SBSAPlatformMetricsContext copyBySettingDisplayCornerRadiusIgnoringZoom:]_block_invoke
+ ___81-[SBNotificationCarPlayDestination _drainPendingFallbackBannerRequestsIfPossible]_block_invoke
+ ___84-[SBMenuBarActivationView _updateLabelFromStyleAttributesWithApplicationNameChange:]_block_invoke
+ ___86-[SBMenuBarViewController dismissAnimated:fadeAppMenu:alongsideAnimations:completion:]_block_invoke
+ ___86-[SBMenuBarViewController dismissAnimated:fadeAppMenu:alongsideAnimations:completion:]_block_invoke_2
+ ___86-[SBMenuBarViewController dismissAnimated:fadeAppMenu:alongsideAnimations:completion:]_block_invoke_3
+ ___86-[SBMenuBarViewController dismissAnimated:fadeAppMenu:alongsideAnimations:completion:]_block_invoke_4
+ ___86-[SBMenuBarViewController dismissAnimated:fadeAppMenu:alongsideAnimations:completion:]_block_invoke_5
+ ___SBLogResourceConditions_block_invoke
+ ___SBLogShipMode_block_invoke
+ ____SBSendAggregatedHardwareLongPressRegistrations_block_invoke
+ ___block_descriptor_128_e8_32s40s48s56s64s72bs80bs88bs_e5_v8?0ls32l8s40l8s72l8s48l8s80l8s56l8s88l8s64l8
+ ___block_descriptor_144_e8_32s40s48s56s64s72bs80bs88bs96r_e8_v16?0d8lr96l8s32l8s40l8s72l8s48l8s80l8s56l8s88l8s64l8
+ ___block_descriptor_256_e8_32s_e15_v28?0Q8i16^B20ls32l8
+ ___block_descriptor_344_e8_32r_e45_v16?0"<SBPIPPositionHyperregionComposing>"8lr32l8
+ ___block_descriptor_65_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_80_e8_32bs40w_e23_v16?0"BSTransaction"8lw40l8s32l8
+ ___block_descriptor_80_e8_32bs40w_e36_v16?0"BSTransactionBlockObserver"8lw40l8s32l8
+ ___block_descriptor_80_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_80_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_96_e8_32s40s48bs56r_e8_v16?0d8lr56l8s32l8s40l8s48l8
+ _kMIBUClientPersonalizationLanguageKey
+ _objc_msgSend$_accessibilityLabelForRingerSilent:
+ _objc_msgSend$_acquireTraitsParticipant
+ _objc_msgSend$_armMatchPasscodeFallbackTimerIfNeeded
+ _objc_msgSend$_createSceneAndRunPreflight
+ _objc_msgSend$_detachedCustomResizedFrameForContainerViewDescription:resizedWithGestureDescription:initialContainerViewFrame:context:
+ _objc_msgSend$_displayLabelForKey:
+ _objc_msgSend$_drainPendingFallbackBannerRequestsIfPossible
+ _objc_msgSend$_enqueueFallbackBannerForRequest:
+ _objc_msgSend$_handleAnnounceTimeoutForLinwoodPreprocess
+ _objc_msgSend$_handleMatchPasscodeFallbackForEvent:
+ _objc_msgSend$_indicatorContentSide
+ _objc_msgSend$_invalidateMatchPasscodeFallbackTimer
+ _objc_msgSend$_invalidateMemoryLimitAssertionForUpcomingSettingsUpdate:
+ _objc_msgSend$_isPointerOverMenuBarRegion
+ _objc_msgSend$_isScenePendingRemovalFromWorkspace
+ _objc_msgSend$_matchPasscodeFallbackFailureSettings
+ _objc_msgSend$_matchPasscodeFallbackInterval
+ _objc_msgSend$_matchPasscodeFallbackTimerFired
+ _objc_msgSend$_menuBarProvidingAppExists
+ _objc_msgSend$_overlayInterfaceOrientationConstraint
+ _objc_msgSend$_postCarPlayBannerForRequest:
+ _objc_msgSend$_preflightSupportedInterfaceOrientations
+ _objc_msgSend$_presentSuccessBannerForRequest:
+ _objc_msgSend$_recomputeMemoryPressure
+ _objc_msgSend$_reconcileApplicationSceneAssertionForForegroundStateChange:upcomingSettingsUpdate:
+ _objc_msgSend$_registerBannerPresentedForRequest:skipReasonForLogging:
+ _objc_msgSend$_repinActivationTableHeight
+ _objc_msgSend$_requestDismissalForCompanionScene:ofPresentation:invalidateCompanionScene:
+ _objc_msgSend$_scheduleDismissPeekedMenuBarTimerIfNecessary
+ _objc_msgSend$_setDisplayCornerRadiusIgnoringZoom:
+ _objc_msgSend$_setIndicatorContentRendersAsSquare:
+ _objc_msgSend$_setOverlayInterfaceOrientationConstraint:
+ _objc_msgSend$_shouldHandleHardwareButtonsForDisplay:
+ _objc_msgSend$_updateActiveState:
+ _objc_msgSend$_updateActiveStateWithClientSettings:
+ _objc_msgSend$_updateHardwareLongPressRegistration
+ _objc_msgSend$_updateLabelFromStyleAttributesWithApplicationNameChange:
+ _objc_msgSend$_updateMenuBarVisibilityWithRequestedVisibility:preserveMenuBarIfInteractionOngoing:
+ _objc_msgSend$_updateOverlayInterfaceOrientationConstraint
+ _objc_msgSend$_updateSceneMemoryPressure
+ _objc_msgSend$_willRequestDismissalForCompanionScene:
+ _objc_msgSend$activateForESIMSetupButton
+ _objc_msgSend$activateForEsimSetupInBuddy
+ _objc_msgSend$allowedPressTypes
+ _objc_msgSend$ambientExtendedIdleTimer
+ _objc_msgSend$animateToPresented:fadeAppMenu:completion:
+ _objc_msgSend$batteryLevelMain
+ _objc_msgSend$batteryStateMain
+ _objc_msgSend$canShowMenuBar
+ _objc_msgSend$colorDifferentiateMinimumContainerOutset
+ _objc_msgSend$constrainsContainingSceneOrientation
+ _objc_msgSend$detachedCustomResizeDragFactor
+ _objc_msgSend$detachedCustomResizeRangeBeginTracking
+ _objc_msgSend$detachedCustomResizeRangeEndTracking
+ _objc_msgSend$detachedCustomResizeRubberbandingCompress
+ _objc_msgSend$detachedCustomResizeRubberbandingStretch
+ _objc_msgSend$detachedCustomResizeWidthCollapseFactor
+ _objc_msgSend$dismissAnimated:fadeAppMenu:alongsideAnimations:completion:
+ _objc_msgSend$displayCornerRadiusIgnoringZoom
+ _objc_msgSend$firstCBDeviceToReportBatteryLevel
+ _objc_msgSend$hasConnectedDevice
+ _objc_msgSend$indexOfDevice:
+ _objc_msgSend$indicatorContentRendersAsSquare
+ _objc_msgSend$initWithBookendType:onlyShowLanguages:callbacks:
+ _objc_msgSend$isLongClick
+ _objc_msgSend$isSharingIdentitySupported
+ _objc_msgSend$isTransitioningToEnvironmentWithoutStatusBar
+ _objc_msgSend$latestPressWasLongClick
+ _objc_msgSend$limitedSizeCompactIntraPadding
+ _objc_msgSend$limitedSizeCompactIntraPaddingPerpendicular
+ _objc_msgSend$memoryPressure
+ _objc_msgSend$menuBarCanBeShownNow
+ _objc_msgSend$minimumIndicatorSize
+ _objc_msgSend$overlayViewProviderDidChangeSupportedInterfaceOrientations:
+ _objc_msgSend$presentation:willRequestDismissalForCompanionScene:
+ _objc_msgSend$presentedAlertItems
+ _objc_msgSend$resourceConditionsCoordinator
+ _objc_msgSend$resourceConditionsCoordinator:memoryPressureDidChange:
+ _objc_msgSend$resourceConditionsHost
+ _objc_msgSend$scene:didChangeAssistantIslandActiveStateTo:
+ _objc_msgSend$scene:didChangeForegroundStateTo:
+ _objc_msgSend$scene:didChangeParentSceneTo:
+ _objc_msgSend$setActivateForEsimSetupInBuddy:
+ _objc_msgSend$setBeginsOnHardwareLongPress:
+ _objc_msgSend$setBluetoothStateChangedHandler:
+ _objc_msgSend$setColorDifferentiateMinimumContainerOutset:
+ _objc_msgSend$setCornerIndicatorEdgeInset:
+ _objc_msgSend$setDetachedCustomResizeDragFactor:
+ _objc_msgSend$setDetachedCustomResizeRangeBeginTracking:
+ _objc_msgSend$setDetachedCustomResizeRangeEndTracking:
+ _objc_msgSend$setDetachedCustomResizeRubberbandingCompress:
+ _objc_msgSend$setDetachedCustomResizeRubberbandingStretch:
+ _objc_msgSend$setDetachedCustomResizeWidthCollapseFactor:
+ _objc_msgSend$setDisplayCornerRadiusIgnoringZoom:
+ _objc_msgSend$setIndicatorContentRendersAsSquare:
+ _objc_msgSend$setJiggleLock:
+ _objc_msgSend$setLimitedSizeCompactIntraPadding:
+ _objc_msgSend$setLimitedSizeCompactIntraPaddingPerpendicular:
+ _objc_msgSend$setLongClick:
+ _objc_msgSend$setMemoryPressure:
+ _objc_msgSend$setMinimumIndicatorSize:
+ _objc_msgSend$setShowPasscode:
+ _objc_msgSend$setSwitcherSceneLiveContentOverlayDelegate:
+ _objc_msgSend$setVibrate:
+ _objc_msgSend$setWaitUntilButtonUp:
+ _objc_msgSend$shouldMenuBarDismissToEnvironmentWithHiddenStatusBar
+ _objc_msgSend$switcherContentControllerWantsToUpdateMenuBarVisibility:preserveMenuBarIfInteractionOngoing:
+ _objc_msgSend$traitsParticipantForFullScreenSwitcherSceneLiveContentOverlay:
+ _objc_msgSend$updateMenuBarVisibilityPreserveIfInteractionOngoing:
+ _sHardwareLongPressRegistrationsByOwner
- -[SBAppResizingShieldWindow delegate]
- -[SBAppResizingShieldWindow setDelegate:]
- -[SBBannerCustomTransitioningDelegate .cxx_destruct]
- -[SBBannerCustomTransitioningDelegate finalAnimationDidCommitHandler]
- -[SBBannerCustomTransitioningDelegate setFinalAnimationDidCommitHandler:]
- -[SBBannerManager _beginPresentInsetSuspensionWithCoordinator:]
- -[SBBannerManager _endPresentInsetSuspension]
- -[SBBannerManager _invalidateOrDeferPreferredMinimumTopInsetInteractive:]
- -[SBBluetoothController _applyCBDeviceLoss:]
- -[SBBluetoothController _applyCBDeviceUpdate:]
- -[SBBluetoothController _cbDeviceGlyphPropertiesDifferBetween:and:]
- -[SBBluetoothController _indexOfCBDeviceWithIdentifier:]
- -[SBBluetoothController _startCBDiscovery]
- -[SBBluetoothController addDeviceNotification:]
- -[SBBluetoothController batteryChanged:]
- -[SBBluetoothController connectionChanged:]
- -[SBBluetoothController deviceForAudioRoute:]
- -[SBBluetoothController firstBTDeviceToReportBatteryLevel]
- -[SBBluetoothController removeDeviceNotification:]
- -[SBCarDoNotDisturbController _hasShownSiriHeaderViewControllerDuringCurrentCarDNDSession]
- -[SBCarDoNotDisturbController _setHasShownSiriHeaderViewControllerDuringCurrentCarDNDSession:]
- -[SBCompanionSceneHostComponent _requestDismissalForCompanionScene:ofPresentation:]
- -[SBCompanionSceneHostComponent scene:didUpdateSettings:]
- -[SBCoverSheetPresentationManager setWallpaperFloatingLayerAlpha:]
- -[SBCoverSheetPresentationManager wallpaperFloatingLayerAlpha]
- -[SBDashBoardCameraContainerViewController _acquireTraitsParticipantIfNeeded]
- -[SBDashBoardCameraContainerViewController viewIsAppearing:]
- -[SBDashBoardCameraPageViewController _acquireTraitsParticipantIfNeeded]
- -[SBFullScreenSwitcherSceneLiveContentOverlay setStatusBarActionDelegate:]
- -[SBFullScreenSwitcherSceneLiveContentOverlay statusBarActionDelegate]
- -[SBGlassBannerTransitionAnimator finalAnimationDidCommitHandler]
- -[SBGlassBannerTransitionAnimator setFinalAnimationDidCommitHandler:]
- -[SBHomeGestureSwitcherModifier keyboardSuppressionMode]
- -[SBMainSwitcherControllerCoordinator switcherContentControllerWantsToUpdateMenuBarVisibility:]
- -[SBMenuBarActivationView _updateLabelFromStyleAttributes]
- -[SBMenuBarHeaderContainerView animateToPresented:completion:]
- -[SBMenuBarManager _menuBarCouldBeShownNow]
- -[SBMenuBarManager _scheduleDismissPeekedMenuBarTimer]
- -[SBMenuBarManager _updateMenuBarVisibilityWithRequestedVisibility:]
- -[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:]
- -[SBResizableAppHostingWindowSceneDelegate resizingShieldWindowDidTapButton:]
- -[SBSwitcherKeyboardSuppressionMode applyAssertionEvenIfAppIsHostingTheKeyboard]
- -[SBSwitcherKeyboardSuppressionMode setApplyAssertionEvenIfAppIsHostingTheKeyboard:]
- -[SBSystemApertureSettings indicatorContentMinimumScale]
- -[SBSystemApertureSettings setIndicatorContentMinimumScale:]
- GCC_except_table1043
- GCC_except_table1050
- GCC_except_table1052
- GCC_except_table1054
- GCC_except_table1056
- GCC_except_table1058
- GCC_except_table1060
- GCC_except_table1062
- GCC_except_table301
- GCC_except_table353
- GCC_except_table386
- GCC_except_table399
- GCC_except_table407
- GCC_except_table445
- GCC_except_table509
- GCC_except_table543
- GCC_except_table551
- GCC_except_table553
- GCC_except_table556
- GCC_except_table558
- GCC_except_table576
- GCC_except_table580
- GCC_except_table586
- GCC_except_table590
- GCC_except_table620
- GCC_except_table674
- GCC_except_table709
- GCC_except_table787
- GCC_except_table813
- GCC_except_table816
- GCC_except_table856
- GCC_except_table898
- GCC_except_table900
- GCC_except_table939
- GCC_except_table950
- GCC_except_table997
- OBJC_IVAR_$_SBBluetoothController._devices
- OBJC_IVAR_$_SBBluetoothController._tetheringConnected
- _BluetoothAvailabilityChangedNotification
- _BluetoothConnectionStatusChangedNotification
- _BluetoothDeviceBatteryChangedNotification
- _BluetoothDeviceConnectSuccessNotification
- _BluetoothDeviceDisconnectSuccessNotification
- _CBCentralManagerOptionReceiveSystemEvents
- _CBManagerNeedsRestrictedStateOperation
- _OBJC_CLASS_$_CBCentralManager
- _OBJC_IVAR_$_SBAppResizingSession._originalDisplayFrame
- _OBJC_IVAR_$_SBAppResizingShieldWindow._activationButton
- _OBJC_IVAR_$_SBAppResizingShieldWindow._delegate
- _OBJC_IVAR_$_SBBannerCustomTransitioningDelegate._finalAnimationDidCommitHandler
- _OBJC_IVAR_$_SBBannerManager._insetSuspendedForPresent
- _OBJC_IVAR_$_SBBannerManager._pendingMinimumTopInsetInvalidation
- _OBJC_IVAR_$_SBBannerManager._pendingMinimumTopInsetInvalidationInteractive
- _OBJC_IVAR_$_SBBluetoothController._cbDevices
- _OBJC_IVAR_$_SBBluetoothController._cbDiscovery
- _OBJC_IVAR_$_SBCarDoNotDisturbController._queue_hasShownSiriHeaderViewControllerDuringCurrentCarDNDSession
- _OBJC_IVAR_$_SBCoverSheetPresentationManager._wallpaperFloatingLayerAlpha
- _OBJC_IVAR_$_SBDeviceApplicationSceneOverlayViewProvider._needsCounterRotationReevaluationForFirstSupportedOrientationsUpdate
- _OBJC_IVAR_$_SBFullScreenSwitcherSceneLiveContentOverlay._statusBarActionDelegate
- _OBJC_IVAR_$_SBGlassBannerTransitionAnimator._finalAnimationDidCommitHandler
- _OBJC_IVAR_$_SBNotificationCarPlayDestination._announceRetryCountForNotificationRequest
- _OBJC_IVAR_$_SBStatusBarStateAggregator._connectedClassicBluetoothDevices
- _OBJC_IVAR_$_SBStatusBarStateAggregator._connectedLEBluetoothDevices
- _OBJC_IVAR_$_SBStatusBarStateAggregator._coreBluetoothManager
- _OBJC_IVAR_$_SBSwitcherKeyboardSuppressionMode._applyAssertionEvenIfAppIsHostingTheKeyboard
- _OBJC_IVAR_$_SBSystemApertureSettings._indicatorContentMinimumScale
- _OBJC_IVAR_$_SBTransientOverlayViewController._wantsInitialKeyboardFocus
- _SBSystemApertureApplyUnDisplayZoomScaleToWindowInWindowSceneIfNecessary
- __OBJC_$_INSTANCE_METHODS_SBChainableModifierEventResponse(SBWindowingModifierResponse|SBSwitcherModifierEventResponse)
- __OBJC_$_INSTANCE_METHODS_SBSwitcherModifier(WindowingModifier|SharedModifierUtilities)
- __OBJC_$_PROP_LIST_SBAppResizingShieldWindow
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBAppResizingShieldWindowDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBAppResizingShieldWindowDelegate
- __OBJC_$_PROTOCOL_REFS_SBAppResizingShieldWindowDelegate
- __OBJC_LABEL_PROTOCOL_$_SBAppResizingShieldWindowDelegate
- __OBJC_PROTOCOL_$_SBAppResizingShieldWindowDelegate
- ___42-[SBBluetoothController _startCBDiscovery]_block_invoke
- ___42-[SBBluetoothController _startCBDiscovery]_block_invoke_2
- ___42-[SBBluetoothController _startCBDiscovery]_block_invoke_3
- ___42-[SBBluetoothController _startCBDiscovery]_block_invoke_4
- ___42-[SBBluetoothController _startCBDiscovery]_block_invoke_5
- ___45-[SBBluetoothController deviceForAudioRoute:]_block_invoke
- ___49-[SBAppResizingShieldWindow initWithWindowScene:]_block_invoke
- ___49-[SBApplicationSceneUpdateTransaction _willBegin]_block_invoke_2
- ___49-[SBApplicationSceneUpdateTransaction _willBegin]_block_invoke_3
- ___54-[SBMenuBarManager _scheduleDismissPeekedMenuBarTimer]_block_invoke
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_44
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_45
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_46
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_47
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_48
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_49
- ___56-[SBBluetoothController _indexOfCBDeviceWithIdentifier:]_block_invoke
- ___62-[SBBannerManager postPresentable:withOptions:userInfo:error:]_block_invoke
- ___62-[SBMenuBarHeaderContainerView animateToPresented:completion:]_block_invoke
- ___62-[SBMenuBarHeaderContainerView animateToPresented:completion:]_block_invoke_2
- ___62-[SBMenuBarHeaderContainerView animateToPresented:completion:]_block_invoke_3
- ___63-[SBBannerManager _beginPresentInsetSuspensionWithCoordinator:]_block_invoke
- ___72-[SBCompanionSceneHostComponent _scene:didUpdateClientRenderingContent:]_block_invoke_3
- ___72-[SBDashBoardCameraPageViewController _acquireTraitsParticipantIfNeeded]_block_invoke
- ___72-[SBDashBoardCameraPageViewController _acquireTraitsParticipantIfNeeded]_block_invoke_2
- ___74-[SBCompanionSceneHostComponent _companionScene:didInvalidateWithContext:]_block_invoke
- ___74-[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:]_block_invoke
- ___74-[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:]_block_invoke_2
- ___74-[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:]_block_invoke_3
- ___74-[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:]_block_invoke_4
- ___74-[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:]_block_invoke_5
- ___77-[SBDashBoardCameraContainerViewController _acquireTraitsParticipantIfNeeded]_block_invoke
- ___77-[SBDashBoardCameraContainerViewController _acquireTraitsParticipantIfNeeded]_block_invoke_2
- ___83-[SBCompanionSceneHostComponent _requestDismissalForCompanionScene:ofPresentation:]_block_invoke
- ___90-[SBCarDoNotDisturbController _hasShownSiriHeaderViewControllerDuringCurrentCarDNDSession]_block_invoke
- ___94-[SBCarDoNotDisturbController _setHasShownSiriHeaderViewControllerDuringCurrentCarDNDSession:]_block_invoke
- ___block_descriptor_104_e8_32s40s48bs56bs64r_e8_v16?0d8lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_144_e8_32s40s48s56s64s72bs80bs88bs96bs104bs_e5_v8?0ls32l8s40l8s72l8s48l8s80l8s56l8s88l8s64l8s96l8s104l8
- ___block_descriptor_160_e8_32s40s48s56s64s72bs80bs88bs96bs104bs112r_e8_v16?0d8lr112l8s32l8s40l8s72l8s48l8s80l8s56l8s88l8s64l8s96l8s104l8
- ___block_descriptor_248_e8_32s_e15_v28?0Q8i16^B20ls32l8
- ___block_descriptor_328_e8_32r_e45_v16?0"<SBPIPPositionHyperregionComposing>"8lr32l8
- ___block_descriptor_40_e8_32s_e36_v16?0"SBStatusBarStateAggregator"8ls32l8
- ___block_descriptor_88_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- _objc_msgSend$_acquireTraitsParticipantIfNeeded
- _objc_msgSend$_applyCBDeviceLoss:
- _objc_msgSend$_applyCBDeviceUpdate:
- _objc_msgSend$_beginPresentInsetSuspensionWithCoordinator:
- _objc_msgSend$_cbDeviceGlyphPropertiesDifferBetween:and:
- _objc_msgSend$_endPresentInsetSuspension
- _objc_msgSend$_indexOfCBDeviceWithIdentifier:
- _objc_msgSend$_invalidateOrDeferPreferredMinimumTopInsetInteractive:
- _objc_msgSend$_menuBarCouldBeShownNow
- _objc_msgSend$_requestDismissalForCompanionScene:ofPresentation:
- _objc_msgSend$_scheduleDismissPeekedMenuBarTimer
- _objc_msgSend$_setObjectWithinCrudeProximity:
- _objc_msgSend$_startCBDiscovery
- _objc_msgSend$_updateLabelFromStyleAttributes
- _objc_msgSend$_updateMenuBarVisibilityWithRequestedVisibility:
- _objc_msgSend$animateToPresented:completion:
- _objc_msgSend$applyAssertionEvenIfAppIsHostingTheKeyboard
- _objc_msgSend$connected
- _objc_msgSend$deviceForAudioRoute:
- _objc_msgSend$dismissAnimated:alongsideAnimations:completion:
- _objc_msgSend$finalAnimationDidCommitHandler
- _objc_msgSend$firstBTDeviceToReportBatteryLevel
- _objc_msgSend$indicatorContentMinimumScale
- _objc_msgSend$initWithDelegate:queue:options:
- _objc_msgSend$isConnectedToSystem
- _objc_msgSend$pairedDevices
- _objc_msgSend$resizingShieldWindowDidTapButton:
- _objc_msgSend$retrieveConnectedPeripheralsWithServices:allowAll:
- _objc_msgSend$setApplyAssertionEvenIfAppIsHostingTheKeyboard:
- _objc_msgSend$setFinalAnimationDidCommitHandler:
- _objc_msgSend$setIndicatorContentMinimumScale:
- _objc_msgSend$setStatusBarActionDelegate:
- _objc_msgSend$setWallpaperFloatingLayerAlpha:
- _objc_msgSend$supportsBatteryLevel
- _objc_msgSend$switcherContentControllerWantsToUpdateMenuBarVisibility:
- _objc_msgSend$wallpaperFloatingLayerAlpha
CStrings:
+ "!AM"
+ "#AnnounceNotification CarPlay Requesting to post presentable: %{public}@"
+ "#AnnounceNotification CarPlay announce timeout enqueueing %lu fallback banner request(s)"
+ "#AnnounceNotification CarPlay drain skipped; another fallback banner is in flight (%lu pending)"
+ "#AnnounceNotification CarPlay drain skipped; banner already presented, waiting for dismiss (%lu pending)"
+ "#AnnounceNotification CarPlay drain: no pending fallback banner requests"
+ "#AnnounceNotification CarPlay presenting fallback banner for %{public}@; %lu remaining"
+ "#AnnounceNotification CarPlay presenting success banner for %{public}@"
+ "#AnnounceNotification CarPlay queued fallback banner for %{public}@; pending total %lu"
+ "#AnnounceNotification CarPlay skipping %{public}@ for %{public}@; already presented for this request"
+ "#AnnounceNotification CarPlay skipping %{public}@; nil notification request"
+ "#AnnounceNotification CarPlay skipping %{public}@; notification request has nil identifier"
+ "#PreprocessNotification Announce message banner never got surfaced. Queueing fallback banner for announce..."
+ "%{public}@ hardware long-press fix ACTIVE (BKSHardwareButtonService available); timeout:%.3gs"
+ "%{public}@ hardware long-press fix INACTIVE (BKSHardwareButtonService unavailable); using wall-clock long-press timing"
+ "%{public}@ hardware long-press fix present but no mapped HID usage; using wall-clock long-press timing"
+ "%{public}@ long press began (%{public}s timing)"
+ "-[SBAppResizingSession _updateToFrame:completion:]_block_invoke_6"
+ "-[SBAppResizingSession _updateToFrame:completion:]_block_invoke_8"
+ "-[SBBluetoothController startWatchingForDevices]_block_invoke"
+ "-[SBBluetoothController startWatchingForDevices]_block_invoke_2"
+ "-[SBBluetoothController startWatchingForDevices]_block_invoke_3"
+ "<%@: %p; clientIdentifier: %@; elementIdentifier: %@; indicatorNeedsDisplayWellKnownLocation: %@; indicatorContentRendersAsSquare: %@; indicatorSize: %@; preferredEdgeOutsets: %@; interfaceOrientation: %@; preferredSystemClipPadding: %f; activeLayoutDirection: %@>"
+ "<%@: %p> Created new keyboard suppression assertion %{public}@ and relinquished old keyboard suppression assertion %{public}@ for reason: %{public}@, with display identity: %{public}@"
+ "Acquiring SiriApp memory limit assertion ahead of foreground commit for %{public}@"
+ "Arming match passcode fallback timer"
+ "BKSHardwareButtonLongPressDescriptor"
+ "BKSHardwareButtonService"
+ "CBDiscovery activation failed: %@"
+ "Can't resolve hosting window scene"
+ "Cannot resume setup: no cover sheet presentation manager available."
+ "Color Differentiate Minimum Container Outset"
+ "Considering foreground scene %@ with handle=%@ (isApp=%{BOOL}d) and parentScene=%@"
+ "Corner Indicator Edge Inset"
+ "Dismissing Assistant Island because a transient overlay disallowing Siri (e.g. Apple Pay) is presenting."
+ "External assertion request on application scene memory limit extension"
+ "Ignoring flash button (down:%{BOOL}u): SpringBoard doesn't handle hardware buttons for display %{public}@"
+ "Invalidating SiriApp memory limit assertion as scene leaves foreground for %{public}@"
+ "Limited Compact Intra Padding"
+ "Limited Compact Intra Padding (Perpendicular)"
+ "Manage SIMs"
+ "Match passcode fallback fired, showing passcode UI while biometric match continues."
+ "Minimum Indicator Size"
+ "No connected window scenes while finalizing startup, continuing..."
+ "Preflight transaction beginning, but previous scene for identifier is invalid and not fully cleaned up in workspace."
+ "Requested an assertion when one is already present"
+ "ResourceConditions"
+ "SBDynamicMemoryLimitApplicationSceneHostExtension.m"
+ "SBLongPressGestureRecognizer.m"
+ "SBTraitsParticipantRoleAppResizingShield"
+ "Setting resource conditions for scene=%@ to memoryPressure=%@"
+ "ShipMode"
+ "Skipping displayConfiguration update as bounds haven't changed: %{public}@"
+ "Updated global memory pressure to %@ (visibleApps=%@ assistantIslandActive=%{BOOL}d)"
+ "[%@] Host foreground state will update: %{BOOL}u"
+ "[%{public}@] clientSettings and appInfo returned empty UIInterfaceOrientationMask. appInfo: %{public}@"
+ "[SBTelephonyManager] Failed to query isSharingIdentitySupported: %{public}@"
+ "[SBTelephonyManager] Failed to set ActivateForEsimSetupInBuddy: %{public}@"
+ "colorDifferentiateMinimumContainerOutset"
+ "conflicting hardware long-press durations for usage 0x%X: %.3gs vs %.3gs"
+ "cornerIndicatorEdgeInset"
+ "defaultPresenter preferredWindowLevel[%{public}f] presentationStyle[%{public}ld]"
+ "displayCornerRadiusIgnoringZoom"
+ "fallback banner enqueue"
+ "hardware"
+ "ignoring lastInteractedScene update as we are tracking a handle on a different window scene"
+ "ignoring lastInteractedScene update as we have a resizing session on a different window scene"
+ "ignoring lastInteractedScene update as we're expecting a remote session activation"
+ "ignoring lastInteractedScene update as we're expecting a session invalidation"
+ "ignoring lastInteractedScene update as we're observing only main or continuity displays"
+ "initWithPage:usage:timeout:"
+ "limitedSizeCompactIntraPadding"
+ "limitedSizeCompactIntraPaddingPerpendicular"
+ "localWindowsGraphForFocusedContextID[%{public}@] targetWindow[%{public}@] targetRootWindow[%{public}@]"
+ "minimumIndicatorSize"
+ "setLongPressTimeouts:"
+ "sharedInstance"
+ "software wall-clock"
+ "success banner present"
+ "transientOverlayWantsKeyboardFocusUponPresentation-1"
+ "transientOverlayWantsKeyboardFocusUponPresentation-2"
+ "void _SBSendAggregatedHardwareLongPressRegistrations(void)_block_invoke"
+ "\xf0\xd6"
+ "\xf0\xf0A"
+ "\xf0\xf0\xa2"
- "!A="
- "#PreprocessNotification #AnnounceNotification CarPlay Requesting to post presentable: %{public}@"
- "#Resetting retry dict for notification requests"
- "-[SBAppResizingSession _updateToFrame:completion:]_block_invoke_3"
- "-[SBAppResizingSession _updateToFrame:completion:]_block_invoke_5"
- "-[SBBluetoothController _applyCBDeviceLoss:]"
- "-[SBBluetoothController _applyCBDeviceUpdate:]"
- "-[SBBluetoothController addDeviceNotification:]"
- "-[SBBluetoothController batteryChanged:]"
- "-[SBBluetoothController connectionChanged:]"
- "-[SBBluetoothController removeDeviceNotification:]"
- "<%@: %p; clientIdentifier: %@; elementIdentifier: %@; indicatorNeedsDisplayWellKnownLocation: %@; indicatorSize: %@; preferredEdgeOutsets: %@; interfaceOrientation: %@; preferredSystemClipPadding: %f; activeLayoutDirection: %@>"
- "<%@: %p> Created new keyboard suppression assertion %{public}@ for reason: %{public}@, with display identity: %{public}@"
- "Can't resolve hosting window scene for handle: %@"
- "Can't resolve scene handle for entity: %@"
- "CarPlay announce retry count for %{public}@: %ld"
- "CarPlay skipping announce for notification %{public}@ - max retries (%ld) exceeded"
- "Cleaning up retry count for currently announcing notification when there is only one notification requests"
- "Cleaning up retry count for finished announce notification request"
- "Configure SIM"
- "End Resizing"
- "Ignoring flash button associated with a display other than the built-in one"
- "Minimum Content Scale"
- "SBBluetoothController CBDiscovery activate failed: %{public}@"
- "The button isn't down and it's been a while since it was supposed to recognize! This might be a hang-induced recognition. Bailing."
- "Withdrawing notification. Removing notification from retry count dictionary."
- "[%@] Host foreground state did update: %{BOOL}u"
- "[probe] lastInteracted cb: scene=%{public}@ ownsHandle=%d continuity=%d session=%{public}@"
- "considering abandonment, systemTime: %f \tpressTime: %f \tdifference: %f"
- "defaultPresenter preferredWindowLevel[%{public}f]"
- "device"
- "indicatorContentMinimumScale"
- "invalidating"
- "localWindowsGraphForFocusedContextID[%{public}@] targetWindow[%{public}@] targetRootWindow[%{public}@] targetPresentationStyle[%{public}ld]"
- "transientOverlayPrefersKeyboardFocus"
- "\xf0\xc6"
- "\xf0\xf0Q"
- "\xf0\xf0\x92"
```
