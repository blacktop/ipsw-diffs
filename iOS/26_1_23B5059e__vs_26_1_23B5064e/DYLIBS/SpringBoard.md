## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.1.15.102.0
-  __TEXT.__text: 0xa90268
-  __TEXT.__auth_stubs: 0x5580
+4557.1.18.101.0
+  __TEXT.__text: 0xa8e364
+  __TEXT.__auth_stubs: 0x5570
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb7eb8
+  __TEXT.__objc_methlist: 0xb7e68
   __TEXT.__const: 0x12ed0
   __TEXT.__oslogstring: 0x5e373
-  __TEXT.__cstring: 0x7d213
-  __TEXT.__gcc_except_tab: 0x198a4
-  __TEXT.__ustring: 0xd0a
+  __TEXT.__cstring: 0x7d134
+  __TEXT.__gcc_except_tab: 0x19544
+  __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2c558
+  __TEXT.__unwind_info: 0x2c4b0
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x221df
-  __TEXT.__objc_methname: 0x1d0727
-  __TEXT.__objc_methtype: 0x4ccfd
-  __TEXT.__objc_stubs: 0xf45a0
-  __DATA_CONST.__got: 0xa2f0
-  __DATA_CONST.__const: 0x1cb80
+  __TEXT.__objc_classname: 0x221ca
+  __TEXT.__objc_methname: 0x1d093c
+  __TEXT.__objc_methtype: 0x4cd26
+  __TEXT.__objc_stubs: 0xf45c0
+  __DATA_CONST.__got: 0xa2b8
+  __DATA_CONST.__const: 0x1caf0
   __DATA_CONST.__objc_classlist: 0x5268
   __DATA_CONST.__objc_catlist: 0x350
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2930
+  __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4ad20
+  __DATA_CONST.__objc_selrefs: 0x4ad50
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3fa8
+  __DATA_CONST.__objc_superrefs: 0x3fa0
   __DATA_CONST.__objc_arraydata: 0x1888
-  __AUTH_CONST.__auth_got: 0x2ad8
-  __AUTH_CONST.__const: 0x10bf8
-  __AUTH_CONST.__cfstring: 0x6f4e0
-  __AUTH_CONST.__objc_const: 0x26a7a8
+  __AUTH_CONST.__auth_got: 0x2ad0
+  __AUTH_CONST.__const: 0x10bd8
+  __AUTH_CONST.__cfstring: 0x6f100
+  __AUTH_CONST.__objc_const: 0x26aa80
   __AUTH_CONST.__objc_arrayobj: 0x17a0
   __AUTH_CONST.__objc_doubleobj: 0x760
-  __AUTH_CONST.__objc_intobj: 0x2c70
+  __AUTH_CONST.__objc_intobj: 0x2ce8
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH.__objc_data: 0x106d0
-  __DATA.__objc_ivar: 0xf408
-  __DATA.__data: 0x1f918
+  __DATA.__objc_ivar: 0xf420
+  __DATA.__data: 0x1f8b8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xab0
   __DATA.__common: 0xa40

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 2D7CE51C-146B-3FA3-AC83-D9057127E474
-  Functions: 70202
-  Symbols:   237446
-  CStrings:  104411
+  UUID: 86ABB2F9-A8C0-38BD-BA50-85514C91A95A
+  Functions: 70194
+  Symbols:   237415
+  CStrings:  104367
 
Symbols:
+ +[SBGlitchHUDSceneController _setupInfo]
+ -[SBAppSwitcherReusableSnapshotView _contentModeForApplication:]
+ -[SBAppViewController applicationSceneViewController:didUpdateStatusBarHidden:withAnimation:]
+ -[SBCoverSheetIconFlyInAnimator _velocityForSpreadMultiplier:spreadMultiplierVelocity:point:]
+ -[SBCoverSheetPresentationManager _isGoingToSecureAppForSlidingViewController:]
+ -[SBCoverSheetPresentationManager _isInAlwaysOn]
+ -[SBCoverSheetPresentationManager _notifyDelegateWillPerformTransitionWithFinalValue:forUserGesture:withVelocity:animated:]
+ -[SBCoverSheetPresentationManager coverSheetSlidingViewController:willChangePresentationState:forUserGesture:withVelocity:animated:]
+ -[SBCoverSheetPresentationManager iconsIgnoreNextFlyRequest]
+ -[SBCoverSheetPresentationManager setCoverSheetTranslationToPresented:forcingTransition:ignoringPreflightRequirements:suppressingIconFly:animated:]
+ -[SBCoverSheetPresentationManager setIconsIgnoreNextFlyRequest:]
+ -[SBCoverSheetPrimarySlidingViewController _transitionToPresentationState:forUserGesture:withVelocity:animated:]
+ -[SBCoverSheetSlidingViewController _transitionToPresentationState:forUserGesture:withVelocity:animated:]
+ -[SBCoverSheetSlidingViewController _transitionToPresentationState:forUserGesture:withVelocity:animated:].cold.1
+ -[SBCoverSheetSlidingViewController _transitionToPresentationState:forUserGesture:withVelocity:animated:].cold.2
+ -[SBDashBoardHostedAppViewController providesIdleTimerDuration]
+ -[SBDashBoardHostedAppViewController setProvidesIdleTimerDuration:]
+ -[SBDashBoardLockScreenEnvironment isProcessingUnlockAttempt]
+ -[SBDashBoardSwitcherHostableEntityLiveContentOverlay updateWindowControlsLayout:]
+ -[SBDeviceApplicationSceneHandle _reevaluateSafeAreaSettingsForSceneSettings:]
+ -[SBDeviceApplicationSceneHandle reevaluateSafeAreaSettingsUsingAnimationSettings:]
+ -[SBFluidSwitcherAppClipLiveContentOverlay updateWindowControlsLayout:]
+ -[SBFluidSwitcherPortaledSceneLiveContentOverlay updateWindowControlsLayout:]
+ -[SBFluidSwitcherViewController _folderExpansionOrContractionAnimationWillBegin:]
+ -[SBFluidSwitcherViewController liveContentOverlay:didUpdateStatusBarHiddenSceneSettings:withAnimation:]
+ -[SBFullScreenAlwaysLiveLiveContentOverlay updateWindowControlsLayout:]
+ -[SBFullScreenSwitcherLiveContentOverlayCoordinator _calculateSBSDisplayLayoutElementRoleForDisplayItem:inAppLayout:zOrderIndex:layoutAttributesMap:]
+ -[SBFullScreenSwitcherLiveContentOverlayCoordinator _itemToZOrderIndexDictionaryForAppLayout:layoutAttributesMap:]
+ -[SBFullScreenSwitcherLiveContentOverlayCoordinator _updateFullScreenDisplayLayoutElementsForActiveAppLayouts:inAppLayout:layoutAttributesMap:]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay applicationSceneViewController:didUpdateStatusBarHidden:withAnimation:]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay medusaDecoratedApplicationSceneViewController:didUpdateStatusBarHidden:withAnimation:]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay updateWindowControlsLayout:]
+ -[SBHomeScreenController _controlCenterDidPresent:]
+ -[SBHomeScreenView iconContentView]
+ -[SBHomeScreenView setIconContentView:]
+ -[SBIdleTimerDescriptor samplingStartBeforeFirstTimeout]
+ -[SBIdleTimerDescriptor setSamplingStartBeforeFirstTimeout:]
+ -[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForPrototypeSettingsDisable:]
+ -[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForPrototypeSettingsOverride:]
+ -[SBIdleTimerGlobalCoordinator settings:changedValueForKey:]
+ -[SBIdleTimerSettings durationInterval]
+ -[SBIdleTimerSettings overrideIdleTimer]
+ -[SBIdleTimerSettings samplingStartBeforeFirstTimeout]
+ -[SBIdleTimerSettings setDurationInterval:]
+ -[SBIdleTimerSettings setOverrideIdleTimer:]
+ -[SBIdleTimerSettings setSamplingStartBeforeFirstTimeout:]
+ -[SBIdleTimerSettings setWarnInterval:]
+ -[SBIdleTimerSettings warnInterval]
+ -[SBLockScreenManager lockScreenViewControllerWillPerformTransitionToFinalValue:forUserGesture:withVelocity:animated:]
+ -[SBLockScreenViewControllerBase isProcessingUnlockAttempt]
+ -[SBMedusaDecoratedDeviceApplicationSceneViewController applicationSceneViewController:didUpdateStatusBarHidden:withAnimation:]
+ -[SBMedusaDecoratedDeviceApplicationSceneViewController updateWindowControlsLayout:]
+ -[SBShelfLiveContentOverlay updateWindowControlsLayout:]
+ -[SBSwitcherSnapshotImageView contentMode]
+ -[SBSwitcherSnapshotImageView setContentMode:]
+ -[SBSwitcherSnapshotImageView setContentMode:].cold.1
+ -[SBSystemUIScenesCoordinator glitchHUDUISceneController]
+ -[SBSystemUIScenesCoordinator setGlitchHUDUISceneController:]
+ -[SBTopAffordanceViewController updateWindowControlsLayout:]
+ GCC_except_table114
+ GCC_except_table153
+ GCC_except_table189
+ GCC_except_table215
+ GCC_except_table237
+ GCC_except_table278
+ GCC_except_table349
+ GCC_except_table429
+ GCC_except_table444
+ GCC_except_table481
+ GCC_except_table485
+ GCC_except_table532
+ _OBJC_CLASS_$_SBGlitchHUDSceneController
+ _OBJC_IVAR_$_SBCoverSheetPresentationManager._iconsIgnoreNextFlyRequest
+ _OBJC_IVAR_$_SBDashBoardHostedAppViewController._providesIdleTimerDuration
+ _OBJC_IVAR_$_SBDashBoardLockScreenEnvironment._isHandlingUnlockAttempt
+ _OBJC_IVAR_$_SBHomeScreenView._iconContentView
+ _OBJC_IVAR_$_SBIdleTimerDescriptor._samplingStartBeforeFirstTimeout
+ _OBJC_IVAR_$_SBIdleTimerGlobalCoordinator._idleTimerPrototypeSettings
+ _OBJC_IVAR_$_SBIdleTimerSettings._durationInterval
+ _OBJC_IVAR_$_SBIdleTimerSettings._overrideIdleTimer
+ _OBJC_IVAR_$_SBIdleTimerSettings._samplingStartBeforeFirstTimeout
+ _OBJC_IVAR_$_SBIdleTimerSettings._warnInterval
+ _OBJC_IVAR_$_SBSwitcherSnapshotImageView._contentMode
+ _OBJC_IVAR_$_SBSystemUIScenesCoordinator._glitchHUDUISceneController
+ _OBJC_METACLASS_$_SBGlitchHUDSceneController
+ _SBLockScreenUIWillPerformTransitionAnimatedKey
+ __OBJC_$_CLASS_METHODS_SBGlitchHUDSceneController
+ __OBJC_CLASS_RO_$_SBGlitchHUDSceneController
+ __OBJC_METACLASS_RO_$_SBGlitchHUDSceneController
+ ___106-[SBSystemApertureSceneElement contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:]_block_invoke.244
+ ___113-[SBFluidSwitcherViewController initWithPersonality:liveContentOverlayCoordinator:dataSource:delegate:debugName:]_block_invoke.207
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.659
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.661
+ ___123-[SBCoverSheetPresentationManager _notifyDelegateWillPerformTransitionWithFinalValue:forUserGesture:withVelocity:animated:]_block_invoke
+ ___132-[SBCoverSheetPresentationManager coverSheetSlidingViewController:willChangePresentationState:forUserGesture:withVelocity:animated:]_block_invoke
+ ___132-[SBCoverSheetPresentationManager coverSheetSlidingViewController:willChangePresentationState:forUserGesture:withVelocity:animated:]_block_invoke_2
+ ___132-[SBCoverSheetPresentationManager coverSheetSlidingViewController:willChangePresentationState:forUserGesture:withVelocity:animated:]_block_invoke_3
+ ___27-[SBLockScreenManager init]_block_invoke.220
+ ___33-[SBIdleTimerDescriptor isEqual:]_block_invoke_6
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1209
+ ___47-[SBLockScreenManager handleTransitionRequest:]_block_invoke.251
+ ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.86
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.754
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.785
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.816
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.922
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.809
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.926
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.392
+ ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.391
+ ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.785
+ ___56-[SBAppSwitcherReusableSnapshotView _updateTranslucency]_block_invoke_2
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1780
+ ___60-[SBIdleTimerGlobalCoordinator settings:changedValueForKey:]_block_invoke
+ ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.938
+ ___63-[SBLockScreenManager lockUIFromSource:withOptions:completion:]_block_invoke.242
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.683
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.684
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.685
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.686
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_2.692
+ ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_3.704
+ ___71-[SBCaptureButtonDeviceStationaryBehavior cameraLaunchIntentInContext:]_block_invoke
+ ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.398
+ ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1108
+ ___74-[SBIdleTimerGlobalCoordinator _registerClientDisableAssertionsTestRecipe]_block_invoke.110
+ ___74-[SBIdleTimerGlobalCoordinator _registerClientDisableAssertionsTestRecipe]_block_invoke_2.111
+ ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.420
+ ___81-[SBIdleTimerGlobalStateMonitor _boolMonitorForProperty:inDefaults:fetchingWith:]_block_invoke.77
+ ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.450
+ ___83-[SBDeviceApplicationSceneHandle reevaluateSafeAreaSettingsUsingAnimationSettings:]_block_invoke
+ ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.82
+ ___88-[SBScreenSleepCoordinator transitionToVisualState:fromVisualState:animated:completion:]_block_invoke_2.17
+ ___89-[SBIdleTimerGlobalStateMonitor _timeIntervalMonitorForProperty:inDefaults:fetchingWith:]_block_invoke.78
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1632
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1634
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1636
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1640
+ ___92-[SBHomeScreenController(AppearanceControlling) setHomeScreenAlpha:behaviorMode:completion:]_block_invoke_2
+ ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke.401
+ ___97-[SBSwitcherController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:]_block_invoke_3
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1763
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s_e33_v16?0?<?<v?BB>?"NSString">8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_40_e8_32r_e54_v32?0"NSNumber"8"SBSwitcherSnapshotImageView"16^B24lr32l8
+ ___block_descriptor_57_e8_32s_e34_v28?0"SBIcon"8"SBIconView"16B24ls32l8
+ ___block_descriptor_58_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_64_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_literal_global.1055
+ ___block_literal_global.1064
+ ___block_literal_global.1100
+ ___block_literal_global.1122
+ ___block_literal_global.1152
+ ___block_literal_global.1155
+ ___block_literal_global.1160
+ ___block_literal_global.1166
+ ___block_literal_global.1459
+ ___block_literal_global.1606
+ ___block_literal_global.1610
+ ___block_literal_global.1642
+ ___block_literal_global.1651
+ ___block_literal_global.1653
+ ___block_literal_global.1657
+ ___block_literal_global.1673
+ ___block_literal_global.1789
+ ___block_literal_global.1812
+ ___block_literal_global.1821
+ ___block_literal_global.1837
+ ___block_literal_global.254
+ ___block_literal_global.258
+ ___block_literal_global.272
+ ___block_literal_global.275
+ ___block_literal_global.279
+ ___block_literal_global.302
+ ___block_literal_global.306
+ ___block_literal_global.384
+ ___block_literal_global.499
+ ___block_literal_global.511
+ ___block_literal_global.555
+ ___block_literal_global.559
+ ___block_literal_global.588
+ ___block_literal_global.594
+ ___block_literal_global.611
+ ___block_literal_global.624
+ ___block_literal_global.636
+ ___block_literal_global.639
+ ___block_literal_global.642
+ ___block_literal_global.664
+ ___block_literal_global.678
+ ___block_literal_global.688
+ ___block_literal_global.691
+ ___block_literal_global.694
+ ___block_literal_global.697
+ ___block_literal_global.732
+ ___block_literal_global.758
+ ___block_literal_global.785
+ ___block_literal_global.820
+ ___block_literal_global.822
+ ___block_literal_global.846
+ ___block_literal_global.856
+ ___block_literal_global.859
+ ___block_literal_global.892
+ ___block_literal_global.896
+ ___block_literal_global.898
+ ___block_literal_global.902
+ ___block_literal_global.904
+ ___block_literal_global.908
+ ___block_literal_global.910
+ ___block_literal_global.914
+ ___block_literal_global.916
+ ___block_literal_global.920
+ ___block_literal_global.922
+ ___block_literal_global.926
+ ___block_literal_global.928
+ ___block_literal_global.932
+ _objc_msgSend$_calculateSBSDisplayLayoutElementRoleForDisplayItem:inAppLayout:zOrderIndex:layoutAttributesMap:
+ _objc_msgSend$_contentModeForApplication:
+ _objc_msgSend$_isGoingToSecureAppForSlidingViewController:
+ _objc_msgSend$_isInAlwaysOn
+ _objc_msgSend$_itemToZOrderIndexDictionaryForAppLayout:layoutAttributesMap:
+ _objc_msgSend$_notifyDelegateWillPerformTransitionWithFinalValue:forUserGesture:withVelocity:animated:
+ _objc_msgSend$_reevaluateSafeAreaSettingsForSceneSettings:
+ _objc_msgSend$_transitionToPresentationState:forUserGesture:withVelocity:animated:
+ _objc_msgSend$_updateFullScreenDisplayLayoutElementsForActiveAppLayouts:inAppLayout:layoutAttributesMap:
+ _objc_msgSend$_velocityForSpreadMultiplier:spreadMultiplierVelocity:point:
+ _objc_msgSend$animatesFlyOut
+ _objc_msgSend$animatesFlyOutToAOD
+ _objc_msgSend$animatesFlyOutToAODFromIdleDim
+ _objc_msgSend$applicationSceneViewController:didUpdateStatusBarHidden:withAnimation:
+ _objc_msgSend$contentMode
+ _objc_msgSend$coverSheetSlidingViewController:willChangePresentationState:forUserGesture:withVelocity:animated:
+ _objc_msgSend$durationInterval
+ _objc_msgSend$iconsFlyInResponse
+ _objc_msgSend$iconsFlyOutResponse
+ _objc_msgSend$isDimmed
+ _objc_msgSend$isProcessingUnlockAttempt
+ _objc_msgSend$isRequestingLayoutUpdateForHostedClient
+ _objc_msgSend$liveContentOverlay:didUpdateStatusBarHiddenSceneSettings:withAnimation:
+ _objc_msgSend$lockScreenViewControllerWillPerformTransitionToFinalValue:forUserGesture:withVelocity:animated:
+ _objc_msgSend$medusaDecoratedApplicationSceneViewController:didUpdateStatusBarHidden:withAnimation:
+ _objc_msgSend$overrideIdleTimer
+ _objc_msgSend$reevaluateSafeAreaSettingsUsingAnimationSettings:
+ _objc_msgSend$samplingStartBeforeFirstTimeout
+ _objc_msgSend$setAllowCameraButtonDeferringWhileFocusLocked:
+ _objc_msgSend$setCoverSheetTranslationToPresented:forcingTransition:ignoringPreflightRequirements:suppressingIconFly:animated:
+ _objc_msgSend$setDurationInterval:
+ _objc_msgSend$setIconContentView:
+ _objc_msgSend$setOverrideIdleTimer:
+ _objc_msgSend$setSamplingStartBeforeFirstTimeout:
+ _objc_msgSend$supportsGlassEffects
+ _objc_msgSend$updateBackgroundGlassEffectForDraggingProgress:usingGlassEffects:
+ _objc_msgSend$updateIdleTimerSettingsForPrototypeSettingsDisable:
+ _objc_msgSend$updateIdleTimerSettingsForPrototypeSettingsOverride:
+ _objc_msgSend$updateWindowControlsLayout:
- -[SBAppViewController applicationSceneViewController:didUpdateStatusBarHidden:]
- -[SBCoverSheetPresentationManager _notifyDelegateWillPerformTransitionWithFinalValue:velocity:forUserGesture:]
- -[SBCoverSheetPresentationManager coverSheetSlidingViewController:willChangePresentationState:withVelocity:forUserGesture:]
- -[SBCoverSheetPrimarySlidingViewController _transitionToPresentationState:forUserGesture:withVelocity:]
- -[SBCoverSheetSlidingViewController _transitionToPresentationState:forUserGesture:withVelocity:]
- -[SBCoverSheetSlidingViewController _transitionToPresentationState:forUserGesture:withVelocity:].cold.1
- -[SBCoverSheetSlidingViewController _transitionToPresentationState:forUserGesture:withVelocity:].cold.2
- -[SBFluidSwitcherViewController _folderExpansionAnimationWillBegin:]
- -[SBFluidSwitcherViewController liveContentOverlay:didUpdateStatusBarHiddenSceneSettings:]
- -[SBFullScreenSwitcherLiveContentOverlayCoordinator _calculateSBSDisplayLayoutElementRoleForDisplayItem:inAppLayout:zOrderIndex:]
- -[SBFullScreenSwitcherLiveContentOverlayCoordinator _itemToZOrderIndexDictionaryForAppLayout:]
- -[SBFullScreenSwitcherLiveContentOverlayCoordinator _updateFullScreenDisplayLayoutElementsForActiveAppLayouts:inAppLayout:]
- -[SBFullScreenSwitcherSceneLiveContentOverlay applicationSceneViewController:didUpdateStatusBarHidden:]
- -[SBFullScreenSwitcherSceneLiveContentOverlay medusaDecoratedApplicationSceneViewController:didUpdateStatusBarHidden:]
- -[SBHomeScreenMenuBar .cxx_destruct]
- -[SBHomeScreenMenuBar _activateAppLayout:fromSwitcher:withWindowScene:]
- -[SBHomeScreenMenuBar _createRecentAppsMenu]
- -[SBHomeScreenMenuBar _handleEditHomeScreenShortcut]
- -[SBHomeScreenMenuBar _handleShutDown]
- -[SBHomeScreenMenuBar buildMenuWithBuilder:]
- -[SBHomeScreenMenuBar delegate]
- -[SBHomeScreenMenuBar getEditMenu]
- -[SBHomeScreenMenuBar handleActionWithURL:]
- -[SBHomeScreenMenuBar handleAppStoreAction]
- -[SBHomeScreenMenuBar homeScreenMenuBarProvidingScene]
- -[SBHomeScreenMenuBar initWithWindowSceneManager:]
- -[SBHomeScreenMenuBar setDelegate:]
- -[SBHomeScreenMenuBar setHomeScreenMenuBarProvidingScene:]
- -[SBHomeScreenMenuBar setWindowSceneManager:]
- -[SBHomeScreenMenuBar showConfirmationAlertWithTitle:message:confirmTitle:handler:]
- -[SBHomeScreenMenuBar toggleMenuBarVisibility]
- -[SBHomeScreenMenuBar windowSceneManager]
- -[SBHomeScreenMenuBar windowScene]
- -[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForPrototypeSettings:]
- -[SBLockScreenManager lockScreenViewControllerWillPerformTransitionToFinalValue:velocity:forUserGesture:]
- -[SBMedusaDecoratedDeviceApplicationSceneViewController applicationSceneViewController:didUpdateStatusBarHidden:]
- -[SBMenuBarManager systemMenusToIgnoreForViewController:]
- -[SBMenuBarViewController isSpringBoardMenuBarForScene:]
- -[SBSystemApertureSceneElement settings]
- -[SBSystemShellEmbeddedDisplayController scene]
- -[SpringBoard _handleReboot]
- -[SpringBoard _handleRestartShortcutWithConfirmation]
- -[SpringBoard _handleScreenshotFullScreenShortcut:]
- -[SpringBoard _handleScreenshotPIPShortcut:]
- -[SpringBoard homeScreenMenuBarProvidingScene]
- -[SpringBoard homeScreenMenuBar]
- -[SpringBoard systemMenuIdentifiersIgnoredInMenuBar]
- -[_SBHomeScreenFloorSwitcherModifier wantsMenuBar]
- GCC_except_table159
- GCC_except_table217
- GCC_except_table289
- GCC_except_table304
- GCC_except_table381
- GCC_except_table450
- GCC_except_table487
- GCC_except_table491
- GCC_except_table531
- _OBJC_CLASS_$_SBHomeScreenMenuBar
- _OBJC_CLASS_$_UIMainMenuSystem
- _OBJC_CLASS_$__SBFKeyWindowStack
- _OBJC_IVAR_$_SBHomeScreenMenuBar._delegate
- _OBJC_IVAR_$_SBHomeScreenMenuBar._homeScreenMenuBarProvidingScene
- _OBJC_IVAR_$_SBHomeScreenMenuBar._windowSceneManager
- _OBJC_IVAR_$_SBSystemApertureSceneElement._settings
- _OBJC_IVAR_$_SpringBoard._homeScreenMenuBar
- _OBJC_IVAR_$_SpringBoard._systemMenuIdentifiersIgnoredInMenuBar
- _OBJC_METACLASS_$_SBHomeScreenMenuBar
- _SBFIsHomeScreenMenuBarAvailable
- _UIMenuApplication
- _UIMenuEdit
- _UIMenuFile
- _UIMenuFormat
- _UIMenuView
- __OBJC_$_INSTANCE_METHODS_SBHomeScreenMenuBar
- __OBJC_$_INSTANCE_VARIABLES_SBHomeScreenMenuBar
- __OBJC_$_PROP_LIST_SBHomeScreenMenuBar
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBHomeScreenMenuBarDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBHomeScreenMenuBarDelegate
- __OBJC_$_PROTOCOL_REFS_SBHomeScreenMenuBarDelegate
- __OBJC_CLASS_RO_$_SBHomeScreenMenuBar
- __OBJC_LABEL_PROTOCOL_$_SBHomeScreenMenuBarDelegate
- __OBJC_METACLASS_RO_$_SBHomeScreenMenuBar
- __OBJC_PROTOCOL_$_SBHomeScreenMenuBarDelegate
- ___106-[SBSystemApertureSceneElement contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:]_block_invoke.246
- ___110-[SBCoverSheetPresentationManager _notifyDelegateWillPerformTransitionWithFinalValue:velocity:forUserGesture:]_block_invoke
- ___113-[SBFluidSwitcherViewController initWithPersonality:liveContentOverlayCoordinator:dataSource:delegate:debugName:]_block_invoke.204
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.654
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.656
- ___123-[SBCoverSheetPresentationManager coverSheetSlidingViewController:willChangePresentationState:withVelocity:forUserGesture:]_block_invoke
- ___123-[SBCoverSheetPresentationManager coverSheetSlidingViewController:willChangePresentationState:withVelocity:forUserGesture:]_block_invoke_2
- ___123-[SBCoverSheetPresentationManager coverSheetSlidingViewController:willChangePresentationState:withVelocity:forUserGesture:]_block_invoke_3
- ___27-[SBLockScreenManager init]_block_invoke.217
- ___43-[SBHomeScreenMenuBar handleActionWithURL:]_block_invoke
- ___43-[SBHomeScreenMenuBar handleAppStoreAction]_block_invoke
- ___44-[SBHomeScreenMenuBar _createRecentAppsMenu]_block_invoke
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_10
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_11
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_12
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_13
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_14
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_2
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_3
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_4
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_5
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_6
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_7
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_8
- ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_9
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1221
- ___47-[SBLockScreenManager handleTransitionRequest:]_block_invoke.248
- ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.91
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.766
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.797
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.828
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.934
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.821
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.938
- ___53-[SpringBoard _handleRestartShortcutWithConfirmation]_block_invoke
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke.386
- ___54-[SBLockScreenManager unlockUIFromSource:withOptions:]_block_invoke_2.388
- ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.780
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1793
- ___59-[SBMenuBarViewController _loadAllMainMenusWithCompletion:]_block_invoke_4
- ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.933
- ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_12
- ___63-[SBLockScreenManager lockUIFromSource:withOptions:completion:]_block_invoke.239
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.676
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.678
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.679
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke.680
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_2.687
- ___67-[SBFluidSwitcherViewController _layoutAppLayout:roles:completion:]_block_invoke_3.699
- ___71-[SBHomeScreenMenuBar _activateAppLayout:fromSwitcher:withWindowScene:]_block_invoke
- ___71-[SBHomeScreenMenuBar _activateAppLayout:fromSwitcher:withWindowScene:]_block_invoke.252
- ___71-[SBHomeScreenMenuBar _activateAppLayout:fromSwitcher:withWindowScene:]_block_invoke_2
- ___72-[SBLockScreenManager _finishUIUnlockFromSource:withOptions:completion:]_block_invoke.395
- ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1103
- ___74-[SBIdleTimerGlobalCoordinator _registerClientDisableAssertionsTestRecipe]_block_invoke.106
- ___74-[SBIdleTimerGlobalCoordinator _registerClientDisableAssertionsTestRecipe]_block_invoke_2.107
- ___75-[SBLockScreenManager _unlockWithRequest:cancelPendingRequests:completion:]_block_invoke.417
- ___81-[SBIdleTimerGlobalStateMonitor _boolMonitorForProperty:inDefaults:fetchingWith:]_block_invoke.70
- ___81-[SBLockScreenManager _attemptUnlockWithPasscode:mesa:finishUIUnlock:completion:]_block_invoke.447
- ___83-[SBHomeScreenMenuBar showConfirmationAlertWithTitle:message:confirmTitle:handler:]_block_invoke
- ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.87
- ___88-[SBScreenSleepCoordinator transitionToVisualState:fromVisualState:animated:completion:]_block_invoke_2.16
- ___89-[SBIdleTimerGlobalStateMonitor _timeIntervalMonitorForProperty:inDefaults:fetchingWith:]_block_invoke.71
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1645
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1647
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1649
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1653
- ___97-[SBLockScreenManager _setPasscodeVisible:animated:ignoringPreflightRequirementsForPresentation:]_block_invoke.398
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1776
- ___block_descriptor_104_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_152_e8_32s40s48s56s64s72s80s_e33_v16?0?<?<v?BB>?"NSString">8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_32_e37_v24?0"BSProcessHandle"8"NSError"16l
- ___block_descriptor_40_e8_32bs_e23_v16?0"UIAlertAction"8ls32l8
- ___block_descriptor_40_e8_32w_e26_"NSArray"16?0"NSArray"8lw32l8
- ___block_descriptor_49_e8_32s_e34_v28?0"SBIcon"8"SBIconView"16B24ls32l8
- ___block_descriptor_56_e8_32bs40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48w_e26_"NSArray"16?0"NSArray"8ls32l8w48l8s40l8
- ___block_descriptor_56_e8_32s40s48w_e26_"NSArray"16?0"NSArray"8lw48l8s32l8s40l8
- ___block_literal_global.1067
- ___block_literal_global.1076
- ___block_literal_global.1112
- ___block_literal_global.1117
- ___block_literal_global.1164
- ___block_literal_global.1167
- ___block_literal_global.1172
- ___block_literal_global.1178
- ___block_literal_global.1472
- ___block_literal_global.1619
- ___block_literal_global.1623
- ___block_literal_global.1664
- ___block_literal_global.1666
- ___block_literal_global.1668
- ___block_literal_global.1670
- ___block_literal_global.1686
- ___block_literal_global.1802
- ___block_literal_global.1825
- ___block_literal_global.1834
- ___block_literal_global.1850
- ___block_literal_global.242
- ___block_literal_global.255
- ___block_literal_global.278
- ___block_literal_global.282
- ___block_literal_global.293
- ___block_literal_global.299
- ___block_literal_global.381
- ___block_literal_global.493
- ___block_literal_global.505
- ___block_literal_global.540
- ___block_literal_global.552
- ___block_literal_global.557
- ___block_literal_global.561
- ___block_literal_global.581
- ___block_literal_global.597
- ___block_literal_global.600
- ___block_literal_global.622
- ___block_literal_global.631
- ___block_literal_global.634
- ___block_literal_global.650
- ___block_literal_global.659
- ___block_literal_global.673
- ___block_literal_global.683
- ___block_literal_global.686
- ___block_literal_global.689
- ___block_literal_global.692
- ___block_literal_global.727
- ___block_literal_global.753
- ___block_literal_global.815
- ___block_literal_global.817
- ___block_literal_global.824
- ___block_literal_global.841
- ___block_literal_global.851
- ___block_literal_global.854
- ___block_literal_global.882
- ___block_literal_global.891
- ___block_literal_global.893
- ___block_literal_global.897
- ___block_literal_global.899
- ___block_literal_global.903
- ___block_literal_global.905
- ___block_literal_global.909
- ___block_literal_global.911
- ___block_literal_global.915
- ___block_literal_global.917
- ___block_literal_global.921
- ___block_literal_global.923
- ___block_literal_global.927
- ___block_literal_global.935
- _objc_msgSend$_activateAppLayout:fromSwitcher:withWindowScene:
- _objc_msgSend$_calculateSBSDisplayLayoutElementRoleForDisplayItem:inAppLayout:zOrderIndex:
- _objc_msgSend$_createRecentAppsMenu
- _objc_msgSend$_handleEditHomeScreenShortcut
- _objc_msgSend$_handleLockShortcut:
- _objc_msgSend$_handleReboot
- _objc_msgSend$_handleShutDown
- _objc_msgSend$_itemToZOrderIndexDictionaryForAppLayout:
- _objc_msgSend$_layoutHostMayNotPerformLayoutUpdateWithReasonsToExclude:
- _objc_msgSend$_notifyDelegateWillPerformTransitionWithFinalValue:velocity:forUserGesture:
- _objc_msgSend$_transitionToPresentationState:forUserGesture:withVelocity:
- _objc_msgSend$_updateFullScreenDisplayLayoutElementsForActiveAppLayouts:inAppLayout:
- _objc_msgSend$applicationSceneViewController:didUpdateStatusBarHidden:
- _objc_msgSend$buildMenuWithBuilder:
- _objc_msgSend$commandWithTitle:image:action:propertyList:alternates:
- _objc_msgSend$coverSheetSlidingViewController:willChangePresentationState:withVelocity:forUserGesture:
- _objc_msgSend$editMenu
- _objc_msgSend$expectedKeyWindow
- _objc_msgSend$getEditMenu
- _objc_msgSend$handleActionWithURL:
- _objc_msgSend$handleAppStoreAction
- _objc_msgSend$hasOpaqueContents
- _objc_msgSend$homeScreenMenuBar
- _objc_msgSend$homeScreenMenuBarProvidingScene
- _objc_msgSend$isSpringBoardMenuBarForScene:
- _objc_msgSend$liveContentOverlay:didUpdateStatusBarHiddenSceneSettings:
- _objc_msgSend$lockScreenViewControllerWillPerformTransitionToFinalValue:velocity:forUserGesture:
- _objc_msgSend$medusaDecoratedApplicationSceneViewController:didUpdateStatusBarHidden:
- _objc_msgSend$openSensitiveURL:withOptions:
- _objc_msgSend$removeMenuForIdentifier:
- _objc_msgSend$replaceChildrenOfMenuForIdentifier:fromChildrenBlock:
- _objc_msgSend$sharedSystem
- _objc_msgSend$showConfirmationAlertWithTitle:message:confirmTitle:handler:
- _objc_msgSend$systemMenuIdentifiersIgnoredInMenuBar
- _objc_msgSend$systemMenusToIgnoreForViewController:
- _objc_msgSend$toggleMenuBarVisibility
- _objc_msgSend$updateBackgroundGlassEffectForDraggingProgress:
- _objc_msgSend$updateIdleTimerSettingsForPrototypeSettings:
CStrings:
+ "@\"SBGlitchHUDSceneController\""
+ "Idle Timer Duration Override"
+ "IdleTimerPrototypeSettingsChanged"
+ "Override"
+ "Override Idle Timer"
+ "SBGlitchHUDSceneController"
+ "SBIconZoomContractionAnimationWillBeginNotification"
+ "SBIdleTimerSettings override is YES"
+ "SBLockScreenUIWillPerformTransitionAnimatedKey"
+ "SBSwitcherSnapshotImageView.m"
+ "Sampling Start Before First Timeout"
+ "T@\"SBGlitchHUDSceneController\",&,N,V_glitchHUDUISceneController"
+ "T@\"UIView\",&,N,V_iconContentView"
+ "TB,N,V_iconsIgnoreNextFlyRequest"
+ "TB,N,V_overrideIdleTimer"
+ "TB,N,V_providesIdleTimerDuration"
+ "Td,N,V_durationInterval"
+ "Td,N,V_samplingStartBeforeFirstTimeout"
+ "Tq,N,V_contentMode"
+ "Warn Duration Override"
+ "_calculateSBSDisplayLayoutElementRoleForDisplayItem:inAppLayout:zOrderIndex:layoutAttributesMap:"
+ "_contentMode"
+ "_contentModeForApplication:"
+ "_controlCenterDidPresent:"
+ "_durationInterval"
+ "_folderExpansionOrContractionAnimationWillBegin:"
+ "_glitchHUDUISceneController"
+ "_iconsIgnoreNextFlyRequest"
+ "_isGoingToSecureAppForSlidingViewController:"
+ "_isHandlingUnlockAttempt"
+ "_isInAlwaysOn"
+ "_itemToZOrderIndexDictionaryForAppLayout:layoutAttributesMap:"
+ "_notifyDelegateWillPerformTransitionWithFinalValue:forUserGesture:withVelocity:animated:"
+ "_overrideIdleTimer"
+ "_providesIdleTimerDuration"
+ "_reevaluateSafeAreaSettingsForSceneSettings:"
+ "_samplingStartBeforeFirstTimeout"
+ "_transitionToPresentationState:forUserGesture:withVelocity:animated:"
+ "_updateFullScreenDisplayLayoutElementsForActiveAppLayouts:inAppLayout:layoutAttributesMap:"
+ "_velocityForSpreadMultiplier:spreadMultiplierVelocity:point:"
+ "animatesFlyOut"
+ "animatesFlyOutToAOD"
+ "animatesFlyOutToAODFromIdleDim"
+ "applicationSceneViewController:didUpdateStatusBarHidden:withAnimation:"
+ "com.apple.GlitchHUD"
+ "com.apple.SpringBoard.SceneWorkspace.GlitchHUD"
+ "contentMode"
+ "contentMode == UIViewContentModeScaleToFill || contentMode == UIViewContentModeScaleAspectFit"
+ "coverSheetSlidingViewController:willChangePresentationState:forUserGesture:withVelocity:animated:"
+ "durationInterval"
+ "glitchHUDUISceneController"
+ "iconsFlyInResponse"
+ "iconsFlyOutResponse"
+ "iconsIgnoreNextFlyRequest"
+ "isDimmed"
+ "isProcessingUnlockAttempt"
+ "liveContentOverlay:didUpdateStatusBarHiddenSceneSettings:withAnimation:"
+ "lockScreenViewControllerWillPerformTransitionToFinalValue:forUserGesture:withVelocity:animated:"
+ "medusaDecoratedApplicationSceneViewController:didUpdateStatusBarHidden:withAnimation:"
+ "overrideIdleTimer"
+ "providesIdleTimerDuration"
+ "q48@0:8@16@24q32@40"
+ "reevaluateSafeAreaSettingsUsingAnimationSettings:"
+ "samplingStartBeforeFirstTimeout"
+ "setAllowCameraButtonDeferringWhileFocusLocked:"
+ "setCoverSheetTranslationToPresented:forcingTransition:ignoringPreflightRequirements:suppressingIconFly:animated:"
+ "setDurationInterval:"
+ "setGlitchHUDUISceneController:"
+ "setIconContentView:"
+ "setIconsIgnoreNextFlyRequest:"
+ "setOverrideIdleTimer:"
+ "setProvidesIdleTimerDuration:"
+ "setSamplingStartBeforeFirstTimeout:"
+ "supportsGlassEffects"
+ "updateBackgroundGlassEffectForDraggingProgress:usingGlassEffects:"
+ "updateIdleTimerSettingsForPrototypeSettingsDisable:"
+ "updateIdleTimerSettingsForPrototypeSettingsOverride:"
+ "updateWindowControlsLayout:"
+ "v36@0:8@\"<SBSwitcherLiveContentOverlay>\"16B24q28"
+ "v36@0:8@\"SBDeviceApplicationSceneViewController\"16B24q28"
+ "v36@0:8@\"SBMedusaDecoratedDeviceApplicationSceneViewController\"16B24q28"
+ "v36@0:8B16B20B24B28B32"
+ "v40@0:8d16B24d28B36"
+ "v40@0:8q16B24d28B36"
+ "v48@0:8@\"SBCoverSheetSlidingViewController\"16q24B32d36B44"
+ "v48@0:8@16q24B32d36B44"
+ "{CGPoint=dd}48@0:8d16d24{CGPoint=dd}32"
- "@\"<SBHomeScreenMenuBarDelegate>\""
- "@\"NSArray\"24@0:8@\"SBMenuBarViewController\"16"
- "@\"SBHomeScreenMenuBar\""
- "About This iPad"
- "App Store"
- "Are you sure you want your iPad to restart?"
- "Control Center"
- "Edit Home Screen"
- "Full Screen Apps"
- "Go"
- "Next Page"
- "Notification Center"
- "Previous Page"
- "Quick Note"
- "Recent Apps"
- "Restart"
- "Restart iPad"
- "SBHomeScreenMenuBar"
- "SBHomeScreenMenuBarDelegate"
- "Screenshot & Edit"
- "Show Dock"
- "Show/Hide Menu Bar"
- "Stage Manager"
- "T@\"<SBHomeScreenMenuBarDelegate>\",W,N,V_delegate"
- "T@\"FBScene\",W,N,V_homeScreenMenuBarProvidingScene"
- "T@\"NSArray\",R,N,V_systemMenuIdentifiersIgnoredInMenuBar"
- "T@\"SBHomeScreenMenuBar\",R,N,V_homeScreenMenuBar"
- "T@\"SBSystemApertureSettings\",R,N,V_settings"
- "Windowed Apps"
- "_activateAppLayout:fromSwitcher:withWindowScene:"
- "_calculateSBSDisplayLayoutElementRoleForDisplayItem:inAppLayout:zOrderIndex:"
- "_createRecentAppsMenu"
- "_folderExpansionAnimationWillBegin:"
- "_handleEditHomeScreenShortcut"
- "_handleReboot"
- "_handleRestartShortcutWithConfirmation"
- "_handleScreenshotFullScreenShortcut:"
- "_handleScreenshotPIPShortcut:"
- "_handleShutDown"
- "_handleToggleStash:"
- "_homeScreenMenuBar"
- "_homeScreenMenuBarProvidingScene"
- "_itemToZOrderIndexDictionaryForAppLayout:"
- "_notifyDelegateWillPerformTransitionWithFinalValue:velocity:forUserGesture:"
- "_systemMenuIdentifiersIgnoredInMenuBar"
- "_transitionToPresentationState:forUserGesture:withVelocity:"
- "_updateFullScreenDisplayLayoutElementsForActiveAppLayouts:inAppLayout:"
- "app.badge.clock"
- "app.grid.2x2.topbackward.filled"
- "applicationSceneViewController:didUpdateStatusBarHidden:"
- "apps.ipad.landscape"
- "appstore"
- "arrow.left"
- "arrow.right"
- "arrowtriangle.backward"
- "bell.badge.fill"
- "camera.viewfinder"
- "commandWithTitle:image:action:propertyList:alternates:"
- "coverSheetSlidingViewController:willChangePresentationState:withVelocity:forUserGesture:"
- "dock.rectangle"
- "editMenu"
- "expectedKeyWindow"
- "gear"
- "getEditMenu"
- "handleActionWithURL:"
- "handleAppStoreAction"
- "homeScreenMenuBar"
- "homeScreenMenuBarProvidingScene"
- "iPad"
- "iPad User Guide"
- "inset.filled.rectangle.and.camera"
- "isSpringBoardMenuBarForScene:"
- "lightbulb"
- "liveContentOverlay:didUpdateStatusBarHiddenSceneSettings:"
- "lockScreenViewControllerWillPerformTransitionToFinalValue:velocity:forUserGesture:"
- "macwindow.on.rectangle"
- "medusaDecoratedApplicationSceneViewController:didUpdateStatusBarHidden:"
- "menubar.rectangle"
- "openSensitiveURL:withOptions:"
- "rectangle"
- "rectangle.3.group"
- "removeMenuForIdentifier:"
- "replaceChildrenOfMenuForIdentifier:fromChildrenBlock:"
- "restart from menu bar"
- "setHomeScreenMenuBarProvidingScene:"
- "settings-navigation://com.apple.Settings.General"
- "settings-navigation://com.apple.Settings.General/About"
- "sharedSystem"
- "showConfirmationAlertWithTitle:message:confirmTitle:handler:"
- "siri"
- "square.and.pencil"
- "squares.leading.rectangle"
- "switch.2"
- "systemMenuIdentifiersIgnoredInMenuBar"
- "systemMenusToIgnoreForViewController:"
- "toggleMenuBarVisibility"
- "updateBackgroundGlassEffectForDraggingProgress:"
- "updateIdleTimerSettingsForPrototypeSettings:"
- "v24@0:8@\"UIKeyCommand\"16"
- "v28@0:8@\"<SBSwitcherLiveContentOverlay>\"16B24"
- "v28@0:8@\"SBDeviceApplicationSceneViewController\"16B24"
- "v28@0:8@\"SBMedusaDecoratedDeviceApplicationSceneViewController\"16B24"
- "v44@0:8@\"SBCoverSheetSlidingViewController\"16q24d32B40"
- "v44@0:8@16q24d32B40"

```
