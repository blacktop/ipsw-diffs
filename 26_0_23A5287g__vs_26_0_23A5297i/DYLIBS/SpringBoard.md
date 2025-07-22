## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.0.3.103.0
-  __TEXT.__text: 0xa77db4
+4557.0.6.103.0
+  __TEXT.__text: 0xa7b764
   __TEXT.__auth_stubs: 0x5550
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb6c28
-  __TEXT.__const: 0x12ba0
-  __TEXT.__oslogstring: 0x5d375
-  __TEXT.__cstring: 0x7c54f
-  __TEXT.__gcc_except_tab: 0x16da0
+  __TEXT.__objc_methlist: 0xb6ec0
+  __TEXT.__const: 0x12be0
+  __TEXT.__oslogstring: 0x5d2b6
+  __TEXT.__cstring: 0x7c56f
+  __TEXT.__gcc_except_tab: 0x16e04
   __TEXT.__ustring: 0xcac
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2bcb8
+  __TEXT.__unwind_info: 0x2bd50
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x21ed7
-  __TEXT.__objc_methname: 0x1cb865
-  __TEXT.__objc_methtype: 0x4c18f
-  __TEXT.__objc_stubs: 0xf1e00
-  __DATA_CONST.__got: 0xa0f0
-  __DATA_CONST.__const: 0x1c938
-  __DATA_CONST.__objc_classlist: 0x5208
+  __TEXT.__objc_classname: 0x21f7a
+  __TEXT.__objc_methname: 0x1cc04a
+  __TEXT.__objc_methtype: 0x4c1ec
+  __TEXT.__objc_stubs: 0xf21c0
+  __DATA_CONST.__got: 0xa140
+  __DATA_CONST.__const: 0x1c9b8
+  __DATA_CONST.__objc_classlist: 0x5220
   __DATA_CONST.__objc_catlist: 0x348
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x28f8
+  __DATA_CONST.__objc_protolist: 0x2908
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a130
+  __DATA_CONST.__objc_selrefs: 0x4a248
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3f50
-  __DATA_CONST.__objc_arraydata: 0x1858
+  __DATA_CONST.__objc_superrefs: 0x3f70
+  __DATA_CONST.__objc_arraydata: 0x1828
   __AUTH_CONST.__auth_got: 0x2ac0
-  __AUTH_CONST.__const: 0x10828
+  __AUTH_CONST.__const: 0x10848
   __AUTH_CONST.__cfstring: 0x6e5a0
-  __AUTH_CONST.__objc_const: 0x266518
-  __AUTH_CONST.__objc_arrayobj: 0x1770
+  __AUTH_CONST.__objc_const: 0x2673f0
+  __AUTH_CONST.__objc_arrayobj: 0x1728
   __AUTH_CONST.__objc_doubleobj: 0x680
   __AUTH_CONST.__objc_intobj: 0x2b98
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x107c0
-  __DATA.__objc_ivar: 0xf1a0
-  __DATA.__data: 0x1f680
+  __AUTH.__objc_data: 0x108b0
+  __DATA.__objc_ivar: 0xf1f4
+  __DATA.__data: 0x1f740
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xac8
   __DATA.__common: 0xa40
   __DATA_DIRTY.__objc_data: 0x22c90
   __DATA_DIRTY.__data: 0x180
-  __DATA_DIRTY.__bss: 0x1a50
+  __DATA_DIRTY.__bss: 0x1a40
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 7D7351AA-49A5-3547-B6DD-EDD0FAA51107
-  Functions: 69678
-  Symbols:   235573
-  CStrings:  103450
+  UUID: 4D8E3042-FE86-3980-B46B-11002D71139C
+  Functions: 69743
+  Symbols:   235826
+  CStrings:  103521
 
Symbols:
+ -[SBDashBoardHostableEntityWorkspaceTransitionManager invalidate]
+ -[SBDashBoardHostableEntityWorkspaceTransitionManager transactionDidComplete:]
+ -[SBDashBoardSetupView setOrientation:]
+ -[SBDashBoardSetupView wallpaperUnlockProgressDidUpdate:]
+ -[SBDashBoardSetupViewController viewWillTransitionToSize:withTransitionCoordinator:]
+ -[SBDisplayItemLayoutAttributesCalculator _appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:layoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
+ -[SBDisplayItemLayoutAttributesCalculator frameForLayoutRole:inAppLayout:layoutAttributesMap:containerOrientation:windowScene:]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay _updatePreferredWindowControlsPlacementForSceneHandle:contentState:]
+ -[SBHomeScreenOverlayViewController buttonBackgroundView]
+ -[SBHomeScreenService hasConfiguredFilesStackWithURL:]
+ -[SBHomeScreenService hasConfiguredFilesStackWithURL:].cold.1
+ -[SBHomeScreenView setUsesGlassGroup:]
+ -[SBHomeScreenView updateGlassGroup]
+ -[SBHomeScreenView usesGlassGroup]
+ -[SBHomeScreenViewController setUsesGlassGroup:]
+ -[SBHomeScreenViewController usesGlassGroup]
+ -[SBIdleTimerService _addMediaPlaybackDisableReason:]
+ -[SBIdleTimerService _addMediaPlaybackDisableReason:].cold.1
+ -[SBIdleTimerService _clientRequestConfigurations]
+ -[SBIdleTimerService _mediaPlaybackDisableReasons]
+ -[SBIdleTimerService _removeMediaPlaybackDisableReason:]
+ -[SBIdleTimerService _removeMediaPlaybackDisableReason:].cold.1
+ -[SBInCallPresentationScreenSharingIcon makeIconImageWithInfo:traitCollection:context:options:]
+ -[SBInCallPresentationSession _layoutStateTransitionCoordinator]
+ -[SBKeyboardFocusCoordinator _handleFocusSceneChange:fromArbiter:request:waitForSecretSceneHost:]
+ -[SBKeyboardFocusCoordinator _handleFocusSceneChange:fromArbiter:request:waitForSecretSceneHost:].cold.1
+ -[SBKeyboardFocusCoordinator _handleFocusSceneChange:fromArbiter:request:waitForSecretSceneHost:].cold.2
+ -[SBKeyboardFocusCoordinator _handleSceneFocusChange_denyRequestForOverlayUI:]
+ -[SBKeyboardFocusCoordinator _handleSceneFocusChange_reasonToAvoidFocusingAppSceneIdentityToken:]
+ -[SBKeyboardFocusCoordinator _sceneControllerHostingSceneIdentityToken:ultimateHostTarget:isSecretScene:]
+ -[SBKeyboardFocusSceneController _topmostZOrderedSceneExcluding:]
+ -[SBKeyboardFocusSceneController supportsFlexibleWindowing]
+ -[SBKeyboardFocusSceneProvider deviceApplicationSceneHandleForSceneIdentity:]
+ -[SBLockScreenManager wallpaperLegibilityEnvironmentDidChange:]
+ -[SBMainDisplaySceneManager currentLayoutState]
+ -[SBMenuBarMainMenuView isPresentingMenuForKeyPress]
+ -[SBMenuBarMainMenuView isPresentingMenuForPointerHover]
+ -[SBMenuBarMainMenuView setPresentingMenuForKeyPress:]
+ -[SBMenuBarMainMenuView setPresentingMenuForPointerHover:]
+ -[SBMenuBarManager sceneDidInvalidate:withContext:]
+ -[SBMenuBarSystemService .cxx_destruct]
+ -[SBMenuBarSystemService _toggleMenuBarVisibilityForClient:]
+ -[SBMenuBarSystemService _toggleMenuBarVisibilityForClient:].cold.1
+ -[SBMenuBarSystemService init]
+ -[SBMenuBarSystemService systemServiceServer:toggleMenuBarVisibilityForClient:]
+ -[SBMenuBarViewController _presentMenuViewNonInteractively:forPointerHover:]
+ -[SBMicroPIPTetheringMirrorView layoutSubviews]
+ -[SBPIPSceneContentAdapter initWithPIPContentType:windowScene:]
+ -[SBPIPStashTabSuppressionPolicyProvider initWithObserver:bannerManager:windowScene:pipManager:]
+ -[SBPIPStashTabSuppressionPolicyProvider initWithObserver:bannerManager:windowScene:pipManager:].cold.1
+ -[SBPIPStashTabSuppressionPolicyProvider initWithObserver:bannerManager:windowScene:pipManager:].cold.2
+ -[SBPIPStashTabSuppressionPolicyProvider sbWindowScene]
+ -[SBRotateScenesWorkspaceTransaction _isOrientationChanging]
+ -[SBSceneLayoutWhitePointAdaptationController _whitePointAdaptivityStyleForSceneHandle:]
+ -[SBSwitcherController sceneHandleForWhitePointAdaptivityStyle]
+ -[SBSwitcherModifier(SharedModifierUtilities) autoLayoutItemIntersectsHomeAffordanceArea:]
+ -[SBSwitcherWindowManagementContext(Telemetry) telemetryMultitaskingMode]
+ -[SBSystemApertureController systemApertureViewController:isDisplayingAnyRequiredPriorityElements:]
+ -[SBSystemApertureStatusBarPillElementProvider sbWindowScene]
+ -[SBSystemApertureStatusBarPillElementProvider setSbWindowScene:]
+ -[SBSystemServiceServer _handleMenuBarServiceClientMessageTypeToggleVisibility:fromClient:]
+ -[SBSystemServiceServer menuBarDelegate]
+ -[SBSystemServiceServer setMenuBarDelegate:]
+ -[SBSystemShellExternalDisplaySceneManager currentLayoutState]
+ -[SBTapOutsideToDismissSwitcherModifierEvent initWithPointerTouch:]
+ -[SBTapOutsideToDismissSwitcherModifierEvent isPointerTouch]
+ -[SBWallpaperController addWallpaperUnlockProgressObserver:]
+ -[SBWallpaperController removeWallpaperUnlockProgressObserver:]
+ -[SBWallpaperController wallpaperWindow]
+ -[SBWindowingUsageMetric .cxx_destruct]
+ -[SBWindowingUsageMetric _flushStageWithItems:multitaskingMode:]
+ -[SBWindowingUsageMetric _multitaskingModeForContext:]
+ -[SBWindowingUsageMetric _stageItemsInContext:]
+ -[SBWindowingUsageMetric init]
+ -[SBWindowingUsageStageItem .cxx_destruct]
+ -[SBWindowingUsageStageItem initWithSceneIdentifier:maximized:]
+ -[SBWindowingUsageStageItem isMaximized]
+ -[SBWindowingUsageStageItem sceneIdentifier]
+ GCC_except_table149
+ GCC_except_table319
+ GCC_except_table371
+ _OBJC_CLASS_$_SBHTraitIconPresentationStyle
+ _OBJC_CLASS_$_SBMenuBarSystemService
+ _OBJC_CLASS_$_SBWindowingUsageMetric
+ _OBJC_CLASS_$_SBWindowingUsageStageItem
+ _OBJC_CLASS_$__UIViewGlassGroup
+ _OBJC_IVAR_$_SBDashBoardHostableEntityWorkspaceTransitionManager._currentLayoutStateTransitionContext
+ _OBJC_IVAR_$_SBDashBoardHostableEntityWorkspaceTransitionManager._currentTransitionCompletionHandler
+ _OBJC_IVAR_$_SBDisplayAppInteractionEventSource._appLayoutOnStage
+ _OBJC_IVAR_$_SBDockToStageZoomWindowingModifier._shouldDodgeDock
+ _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._effectiveInitialPositionY
+ _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._resizedDisplayItemIntersectsHomeAffordanceArea
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._draggedDisplayItemIntersectsHomeAffordanceArea
+ _OBJC_IVAR_$_SBHomeScreenOverlayViewController._buttonBackgroundView
+ _OBJC_IVAR_$_SBHomeScreenView._usesGlassGroup
+ _OBJC_IVAR_$_SBIdleTimerService._lock
+ _OBJC_IVAR_$_SBIdleTimerService._lock_clientRequestConfigurations
+ _OBJC_IVAR_$_SBIdleTimerService._lock_mediaPlaybackDisableReasons
+ _OBJC_IVAR_$_SBKeyboardFocusCoordinator._handleFocusChangeGenerationCount
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._presentingMenuForKeyPress
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._presentingMenuForPointerHover
+ _OBJC_IVAR_$_SBMenuBarSystemService._menuBarVisibilityRequestAuthenticator
+ _OBJC_IVAR_$_SBPIPSceneContentAdapter._sbWindowScene
+ _OBJC_IVAR_$_SBPIPStashTabSuppressionPolicyProvider._sbWindowScene
+ _OBJC_IVAR_$_SBStripModelWindowingModifier._peekingAppLayout
+ _OBJC_IVAR_$_SBStripModelWindowingModifier._previousPeekingAppLayout
+ _OBJC_IVAR_$_SBSystemApertureController._isDisplayingAnyRequiredPriorityElements
+ _OBJC_IVAR_$_SBSystemApertureStatusBarPillElementProvider._sbWindowScene
+ _OBJC_IVAR_$_SBSystemApertureViewController._elementHasRequiredPriority
+ _OBJC_IVAR_$_SBSystemServiceServer._menuBarDelegate
+ _OBJC_IVAR_$_SBSystemShellExternalDisplaySceneManager._currentLayoutState
+ _OBJC_IVAR_$_SBTapOutsideToDismissSwitcherModifierEvent._pointerTouch
+ _OBJC_IVAR_$_SBWallpaperController._wallpaperUnlockProgressObservers
+ _OBJC_IVAR_$_SBWindowingUsageMetric._initialMultitaskingMode
+ _OBJC_IVAR_$_SBWindowingUsageMetric._itemsOnStage
+ _OBJC_IVAR_$_SBWindowingUsageStageItem._maximized
+ _OBJC_IVAR_$_SBWindowingUsageStageItem._sceneIdentifier
+ _OBJC_IVAR_$_SpringBoard._menuBarSystemService
+ _OBJC_METACLASS_$_SBMenuBarSystemService
+ _OBJC_METACLASS_$_SBWindowingUsageMetric
+ _OBJC_METACLASS_$_SBWindowingUsageStageItem
+ _SBActivityWidgetContentTargetBundleIdentifier
+ _SBDisplayItemSizeIsUnspecified
+ _SBDisplayItemSizeIsUnspecified.cold.1
+ _SBSMenuBarServiceToggleVisibilityEntitlement
+ __OBJC_$_INSTANCE_METHODS_SBMenuBarSystemService
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherWindowManagementContext(Telemetry)
+ __OBJC_$_INSTANCE_METHODS_SBWindowingUsageMetric
+ __OBJC_$_INSTANCE_METHODS_SBWindowingUsageStageItem
+ __OBJC_$_INSTANCE_VARIABLES_SBMenuBarSystemService
+ __OBJC_$_INSTANCE_VARIABLES_SBTapOutsideToDismissSwitcherModifierEvent
+ __OBJC_$_INSTANCE_VARIABLES_SBWindowingUsageMetric
+ __OBJC_$_INSTANCE_VARIABLES_SBWindowingUsageStageItem
+ __OBJC_$_PROP_LIST_SBDashBoardHostableEntityWorkspaceTransitionManager
+ __OBJC_$_PROP_LIST_SBMenuBarSystemService
+ __OBJC_$_PROP_LIST_SBTapOutsideToDismissSwitcherModifierEvent
+ __OBJC_$_PROP_LIST_SBWindowingUsageStageItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSystemServiceServerMenuBarDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBWallpaperUnlockProgressObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSystemServiceServerMenuBarDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBWallpaperUnlockProgressObserver
+ __OBJC_$_PROTOCOL_REFS_SBSystemServiceServerMenuBarDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SBDashBoardHostableEntityWorkspaceTransitionManager
+ __OBJC_CLASS_PROTOCOLS_$_SBMenuBarSystemService
+ __OBJC_CLASS_RO_$_SBMenuBarSystemService
+ __OBJC_CLASS_RO_$_SBWindowingUsageMetric
+ __OBJC_CLASS_RO_$_SBWindowingUsageStageItem
+ __OBJC_LABEL_PROTOCOL_$_SBSystemServiceServerMenuBarDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBWallpaperUnlockProgressObserver
+ __OBJC_METACLASS_RO_$_SBMenuBarSystemService
+ __OBJC_METACLASS_RO_$_SBWindowingUsageMetric
+ __OBJC_METACLASS_RO_$_SBWindowingUsageStageItem
+ __OBJC_PROTOCOL_$_SBSystemServiceServerMenuBarDelegate
+ __OBJC_PROTOCOL_$_SBWallpaperUnlockProgressObserver
+ ___100-[SBActivityAmbientViewController _fullOverlayViewControllerForItem:configuringForAlert:completion:]_block_invoke.30
+ ___101-[SBActivityBannerObserver _postBannerWithActivityIdentifier:payloadIdentifier:prominent:completion:]_block_invoke.56
+ ___114-[SBFullScreenSwitcherSceneLiveContentOverlay _updatePreferredWindowControlsPlacementForSceneHandle:contentState:]_block_invoke
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.642
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.644
+ ___129-[SBSystemApertureStatusBarPillElementProvider _updateActiveElementIfNeededWithLayoutState:reason:notifyingObserversIfNecessary:]_block_invoke.107
+ ___134-[SBWidgetExtensionDebuggingController _reallyFindDescriptorForWidgetFromExtension:forRequestedKind:requestedWidgetFamily:completion:]_block_invoke.135
+ ___134-[SBWidgetExtensionDebuggingController _reallyFindDescriptorForWidgetFromExtension:forRequestedKind:requestedWidgetFamily:completion:]_block_invoke_4.119
+ ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke.31
+ ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke.32
+ ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke.37
+ ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke.42
+ ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke_2.38
+ ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke_2.38.cold.1
+ ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke_2.38.cold.2
+ ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke_2.38.cold.3
+ ___228-[SBActivityAmbientViewController _animateTransitionToBecomeNewPrimaryAcivityWithItem:transitionType:fullOverlayViewController:compactOverlayViewControllerForTransition:oldFullViewController:oldCompactViewController:completion:]_block_invoke.79
+ ___30-[SBWindowingUsageMetric init]_block_invoke
+ ___30-[SBWindowingUsageMetric init]_block_invoke_2
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1206
+ ___47-[SBWindowingUsageMetric _stageItemsInContext:]_block_invoke
+ ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.81
+ ___52-[SBControlCenterController _updateWindowVisibility]_block_invoke
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.747
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.778
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.809
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.915
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.802
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.919
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1748
+ ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.512
+ ___58-[SBDashBoardSetupViewController _checkIfActivationLocked]_block_invoke.161
+ ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.924
+ ___63-[SBSwitcherController sceneHandleForWhitePointAdaptivityStyle]_block_invoke
+ ___63-[SBTransientOverlayScenePresenter performPresentationRequest:]_block_invoke.94
+ ___64-[SBActivityManager _activityStartedOrUpdatedWithContentUpdate:]_block_invoke.43
+ ___64-[SBWindowingUsageMetric _flushStageWithItems:multitaskingMode:]_block_invoke
+ ___64-[SBWindowingUsageMetric _flushStageWithItems:multitaskingMode:]_block_invoke_2
+ ___64-[SBWindowingUsageMetric _flushStageWithItems:multitaskingMode:]_block_invoke_3
+ ___66-[SBDisplayAppInteractionEventSource _notifyTransition:beginning:]_block_invoke_4
+ ___66-[SBDisplayAppInteractionEventSource _notifyTransition:beginning:]_block_invoke_5
+ ___66-[SBDisplayAppInteractionEventSource _notifyTransition:beginning:]_block_invoke_6
+ ___66-[SBTransientOverlayViewController setDisplayLayoutElementActive:]_block_invoke
+ ___71-[SBFluidSwitcherDragAndDropManager _beginTrackingDropSessionIfNeeded:]_block_invoke.54
+ ___79-[SBMenuBarSystemService systemServiceServer:toggleMenuBarVisibilityForClient:]_block_invoke
+ ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.358
+ ___85-[SBDashBoardSetupViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke
+ ___88-[SBHomeScreenOverlayViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke.72
+ ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.77
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1600
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1602
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1604
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1608
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.645
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.667
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.682
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.686
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.694
+ ___97-[SBKeyboardFocusCoordinator _handleFocusSceneChange:fromArbiter:request:waitForSecretSceneHost:]_block_invoke
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1731
+ ___block_descriptor_104_e8_32s40s48s56s64s72r80r_e33_v16?0"ATXAppDirectoryResponse"8lr72l8s32l8r80l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88bs96w_e8_v12?0B8ls32l8s40l8s48l8s56l8w96l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_32_e40_"NSString"16?0"CHSControlDescriptor"8l
+ ___block_descriptor_40_e8_32bs_e19_"NSDictionary"8?0ls32l8
+ ___block_descriptor_40_e8_32s_e37_"NSDictionary"16?0"SBLayoutState"8ls32l8
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e57_B24?0"SBDisplayItem"8"SBDisplayItemLayoutAttributes"16ls32l8
+ ___block_descriptor_48_e8_32r40r_e39_v24?0"SBWindowingUsageStageItem"8^B16lr32l8r40l8
+ ___block_descriptor_48_e8_32s40w_e36_v16?0"_UIMainMenuSessionResponse"8lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e22_v16?0"NSDictionary"8ls32l8s40l8w56l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8r72l8
+ ___block_literal_global.1052
+ ___block_literal_global.1061
+ ___block_literal_global.108
+ ___block_literal_global.1097
+ ___block_literal_global.1149
+ ___block_literal_global.1152
+ ___block_literal_global.1157
+ ___block_literal_global.1163
+ ___block_literal_global.1199
+ ___block_literal_global.122
+ ___block_literal_global.1247
+ ___block_literal_global.1453
+ ___block_literal_global.1574
+ ___block_literal_global.1578
+ ___block_literal_global.1610
+ ___block_literal_global.1619
+ ___block_literal_global.1621
+ ___block_literal_global.1623
+ ___block_literal_global.1625
+ ___block_literal_global.1641
+ ___block_literal_global.1757
+ ___block_literal_global.1780
+ ___block_literal_global.1789
+ ___block_literal_global.1805
+ ___block_literal_global.222
+ ___block_literal_global.225
+ ___block_literal_global.263
+ ___block_literal_global.281
+ ___block_literal_global.537
+ ___block_literal_global.575
+ ___block_literal_global.578
+ ___block_literal_global.586
+ ___block_literal_global.611
+ ___block_literal_global.619
+ ___block_literal_global.630
+ ___block_literal_global.647
+ ___block_literal_global.677
+ ___block_literal_global.683
+ ___block_literal_global.771
+ ___block_literal_global.805
+ ___block_literal_global.806
+ ___block_literal_global.810
+ ___block_literal_global.812
+ ___block_literal_global.817
+ ___block_literal_global.819
+ ___block_literal_global.832
+ ___block_literal_global.842
+ ___block_literal_global.873
+ ___block_literal_global.878
+ ___block_literal_global.882
+ ___block_literal_global.884
+ ___block_literal_global.888
+ ___block_literal_global.890
+ ___block_literal_global.894
+ ___block_literal_global.896
+ ___block_literal_global.900
+ ___block_literal_global.902
+ ___block_literal_global.906
+ ___block_literal_global.908
+ ___block_literal_global.912
+ ___block_literal_global.914
+ ___block_literal_global.918
+ ___block_literal_global.926
+ _kSBSAnalyticsLayoutStateLayoutAttributesKey
+ _kSBSAnalyticsLayoutStateLayoutAttributesMaximizedKey
+ _kSBSAnalyticsLayoutStateWindowManagementContextKey
+ _kSBSAnalyticsLayoutStateWindowManagementContextTelemetryMultitaskingModeKey
+ _objc_msgSend$_addMediaPlaybackDisableReason:
+ _objc_msgSend$_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:layoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
+ _objc_msgSend$_clientRequestConfigurations
+ _objc_msgSend$_flushStageWithItems:multitaskingMode:
+ _objc_msgSend$_handleFocusSceneChange:fromArbiter:request:waitForSecretSceneHost:
+ _objc_msgSend$_handleMenuBarServiceClientMessageTypeToggleVisibility:fromClient:
+ _objc_msgSend$_handleSceneFocusChange_denyRequestForOverlayUI:
+ _objc_msgSend$_handleSceneFocusChange_reasonToAvoidFocusingAppSceneIdentityToken:
+ _objc_msgSend$_isOrientationChanging
+ _objc_msgSend$_mediaPlaybackDisableReasons
+ _objc_msgSend$_multitaskingModeForContext:
+ _objc_msgSend$_presentMenuViewNonInteractively:forPointerHover:
+ _objc_msgSend$_removeMediaPlaybackDisableReason:
+ _objc_msgSend$_sceneControllerHostingSceneIdentityToken:ultimateHostTarget:isSecretScene:
+ _objc_msgSend$_stageItemsInContext:
+ _objc_msgSend$_toggleMenuBarVisibilityForClient:
+ _objc_msgSend$_topmostZOrderedSceneExcluding:
+ _objc_msgSend$_updatePreferredWindowControlsPlacementForSceneHandle:contentState:
+ _objc_msgSend$_whitePointAdaptivityStyleForSceneHandle:
+ _objc_msgSend$activityHostViewControllerWithDescriptor:metricsRequest:payloadID:targetBundleIdentifier:
+ _objc_msgSend$appLayoutPreviouslyOnStage
+ _objc_msgSend$autoLayoutItemIntersectsHomeAffordanceArea:
+ _objc_msgSend$buttonBackgroundView
+ _objc_msgSend$deviceApplicationSceneHandleForSceneIdentity:
+ _objc_msgSend$frameForLayoutRole:inAppLayout:layoutAttributesMap:containerOrientation:windowScene:
+ _objc_msgSend$genericApplicationIcon
+ _objc_msgSend$hasConfiguredFilesStackWithURL:
+ _objc_msgSend$initWithObserver:bannerManager:windowScene:pipManager:
+ _objc_msgSend$initWithPIPContentType:windowScene:
+ _objc_msgSend$initWithPointerTouch:
+ _objc_msgSend$initWithSceneIdentifier:maximized:
+ _objc_msgSend$isPresentingMenuForPointerHover
+ _objc_msgSend$maximumPossibleMenuBarWidth
+ _objc_msgSend$sceneHandleForWhitePointAdaptivityStyle
+ _objc_msgSend$secureWindowVisibilityDidChange:
+ _objc_msgSend$setMenuBarDelegate:
+ _objc_msgSend$setPresentingMenuForKeyPress:
+ _objc_msgSend$setPresentingMenuForPointerHover:
+ _objc_msgSend$setUsesGlassGroup:
+ _objc_msgSend$supportsFlexibleWindowing
+ _objc_msgSend$systemApertureViewController:isDisplayingAnyRequiredPriorityElements:
+ _objc_msgSend$systemServiceServer:toggleMenuBarVisibilityForClient:
+ _objc_msgSend$telemetryMultitaskingMode
+ _objc_msgSend$updateGlassGroup
+ _objc_msgSend$usesGlassGroup
+ _objc_msgSend$wallpaperLegibilityEnvironmentDidChange:
+ _objc_msgSend$wallpaperUnlockProgressDidUpdate:
- +[SBProactiveLibraryCategoryMapProviderSource _defaultSuggestedApps]
- -[SBDisplayItemLayoutAttributesCalculator _appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
- -[SBInCallPresentationScreenSharingIcon makeIconImageWithInfo:traitCollection:options:]
- -[SBKeyboardFocusCoordinator _handleFocusSceneChange:fromArbiter:request:]
- -[SBKeyboardFocusCoordinator _sceneControllerHostingSceneIdentityToken:ultimateHostTarget:]
- -[SBLiveWindowResizeGestureWorkspaceTransaction _begin]
- -[SBMenuBarMainMenuView prepareToPresentMenuForIndirectInput]
- -[SBMenuBarMainMenuView presentingMenuForIndirectInput]
- -[SBMenuBarMainMenuView setPresentingMenuForIndirectInput:]
- -[SBMenuBarViewController _presentMenuViewNonInteractively:]
- -[SBPIPSceneContentAdapter initWithPIPContentType:sceneManager:]
- -[SBPIPStashTabSuppressionPolicyProvider initWithObserver:bannerManager:sceneManager:pipManager:]
- -[SBPIPStashTabSuppressionPolicyProvider initWithObserver:bannerManager:sceneManager:pipManager:].cold.1
- -[SBPIPStashTabSuppressionPolicyProvider initWithObserver:bannerManager:sceneManager:pipManager:].cold.2
- -[SBPIPStashTabSuppressionPolicyProvider sceneManager]
- -[SBProactiveLibraryCategoryMapProviderSource _filteredLastKnownGoodSuggestions]
- -[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:].cold.2
- -[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:].cold.3
- -[SBSceneManager currentLayoutState]
- -[SBSceneManager(ChamoisDevelopmentShimming) _layoutStateTransitionCoordinator]
- -[SBSceneManager(ChamoisDevelopmentShimming) _layoutStateTransitionCoordinator].cold.1
- -[SBSceneManager(ChamoisDevelopmentShimming) _sbWindowScene]
- -[SBSceneManager(ChamoisDevelopmentShimming) _sbWindowScene].cold.1
- -[SBSceneManager(ChamoisDevelopmentShimming) currentLayoutState]
- -[SBSceneManager(ChamoisDevelopmentShimming) currentLayoutState].cold.1
- -[SBSystemApertureController systemApertureViewController:isDisplayingAnyRequiredSecureElements:]
- -[SBTransientOverlayViewController setDisplayLayoutElementActive:].cold.1
- -[SBTransientOverlayViewController setDisplayLayoutElementActive:].cold.2
- -[SBTransientOverlayViewController updateDisplayLayoutElementWithBuilder:].cold.1
- -[SBTransientOverlayViewController updateDisplayLayoutElementWithBuilder:].cold.2
- GCC_except_table143
- _OBJC_IVAR_$_SBDashBoardHostableEntityWorkspaceTransitionManager._currentTransaction
- _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._selectedItemWasInitiallyFullscreen
- _OBJC_IVAR_$_SBIdleTimerService._clientRequestConfigurations
- _OBJC_IVAR_$_SBIdleTimerService._mediaPlaybackDisableReasons
- _OBJC_IVAR_$_SBMenuBarMainMenuView._presentingMenuForIndirectInput
- _OBJC_IVAR_$_SBPIPStashTabSuppressionPolicyProvider._sceneManager
- _OBJC_IVAR_$_SBProactiveLibraryCategoryMapProviderSource._lastKnownGoodRecentApps
- _OBJC_IVAR_$_SBProactiveLibraryCategoryMapProviderSource._lastKnownGoodSuggestions
- _OBJC_IVAR_$_SBSceneManager._currentLayoutState
- _OBJC_IVAR_$_SBSystemApertureController._isDisplayingAnyRequiredSecureContent
- _OBJC_IVAR_$_SBSystemApertureViewController._secureDisplayRequired
- __OBJC_$_CLASS_METHODS_SBProactiveLibraryCategoryMapProviderSource
- __OBJC_$_INSTANCE_METHODS_SBSwitcherWindowManagementContext
- ___100-[SBActivityAmbientViewController _fullOverlayViewControllerForItem:configuringForAlert:completion:]_block_invoke.33
- ___101-[SBActivityBannerObserver _postBannerWithActivityIdentifier:payloadIdentifier:prominent:completion:]_block_invoke.55
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.645
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.647
- ___129-[SBSystemApertureStatusBarPillElementProvider _updateActiveElementIfNeededWithLayoutState:reason:notifyingObserversIfNecessary:]_block_invoke.108
- ___134-[SBWidgetExtensionDebuggingController _reallyFindDescriptorForWidgetFromExtension:forRequestedKind:requestedWidgetFamily:completion:]_block_invoke.128
- ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke.41
- ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke.46
- ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke.47
- ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke.52
- ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke.56
- ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke_2.53
- ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke_2.53.cold.1
- ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke_2.53.cold.2
- ___170-[SBProactiveLibraryCategoryMapProviderSource requestLibraryCategoryMapWithOptions:existingLibraryCategoryMap:forbiddenApplicationIdentifiers:sessionId:queue:completion:]_block_invoke_2.53.cold.3
- ___228-[SBActivityAmbientViewController _animateTransitionToBecomeNewPrimaryAcivityWithItem:transitionType:fullOverlayViewController:compactOverlayViewControllerForTransition:oldFullViewController:oldCompactViewController:completion:]_block_invoke.82
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1207
- ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.83
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.750
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.781
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.812
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.917
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.805
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.921
- ___55-[SBLiveWindowResizeGestureWorkspaceTransaction _begin]_block_invoke
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1749
- ___58-[SBDashBoardSetupViewController _checkIfActivationLocked]_block_invoke.157
- ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.927
- ___64-[SBActivityManager _activityStartedOrUpdatedWithContentUpdate:]_block_invoke.40
- ___71-[SBFluidSwitcherDragAndDropManager _beginTrackingDropSessionIfNeeded:]_block_invoke.56
- ___75-[_SBFullScreenAppFloorSwitcherModifier handleSwitcherShortcutActionEvent:]_block_invoke_5
- ___81-[SBFullScreenSwitcherSceneLiveContentOverlay sceneHandle:didUpdateContentState:]_block_invoke
- ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.361
- ___88-[SBHomeScreenOverlayViewController viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke.70
- ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.79
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1601
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1603
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1605
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1609
- ___91-[SBDashBoardHostableEntityWorkspaceTransitionManager executeTransitionRequest:completion:]_block_invoke
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.644
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.666
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.681
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.685
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.693
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1732
- ___block_descriptor_112_e8_32s40s48s56s64s72s80r88r_e33_v16?0"ATXAppDirectoryResponse"8lr80l8s32l8r88l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_40_e8_32s_e36_v16?0"_UIMainMenuSessionResponse"8ls32l8
- ___block_descriptor_40_e8_32s_e48_v16?0"_UIMainMenuCommandPrimaryActionContext"8ls32l8
- ___block_descriptor_48_e8_32s40s_e33_v16?0"ATXAppDirectoryResponse"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80r_e5_v8?0ls32l8r80l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_97_e8_32s40s48s56s64s72s80bs88w_e8_v12?0B8ls32l8s40l8s48l8s56l8w88l8s64l8s72l8s80l8
- ___block_literal_global.1053
- ___block_literal_global.1062
- ___block_literal_global.1098
- ___block_literal_global.1150
- ___block_literal_global.1153
- ___block_literal_global.1158
- ___block_literal_global.1164
- ___block_literal_global.1198
- ___block_literal_global.1246
- ___block_literal_global.1454
- ___block_literal_global.1575
- ___block_literal_global.1579
- ___block_literal_global.1611
- ___block_literal_global.1620
- ___block_literal_global.1622
- ___block_literal_global.1624
- ___block_literal_global.1626
- ___block_literal_global.1642
- ___block_literal_global.1758
- ___block_literal_global.1781
- ___block_literal_global.1790
- ___block_literal_global.1806
- ___block_literal_global.494
- ___block_literal_global.540
- ___block_literal_global.577
- ___block_literal_global.583
- ___block_literal_global.600
- ___block_literal_global.613
- ___block_literal_global.628
- ___block_literal_global.633
- ___block_literal_global.650
- ___block_literal_global.680
- ___block_literal_global.686
- ___block_literal_global.774
- ___block_literal_global.804
- ___block_literal_global.809
- ___block_literal_global.811
- ___block_literal_global.816
- ___block_literal_global.818
- ___block_literal_global.848
- ___block_literal_global.876
- ___block_literal_global.881
- ___block_literal_global.885
- ___block_literal_global.887
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
- ___block_literal_global.923
- ___block_literal_global.929
- _objc_msgSend$_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
- _objc_msgSend$_defaultSuggestedApps
- _objc_msgSend$_filteredLastKnownGoodSuggestions
- _objc_msgSend$_handleFocusSceneChange:fromArbiter:request:
- _objc_msgSend$_presentMenuViewNonInteractively:
- _objc_msgSend$_sceneControllerHostingSceneIdentityToken:ultimateHostTarget:
- _objc_msgSend$_shouldRemoveRecentsPodWithLastKnownRecentApps:
- _objc_msgSend$_whitePointAdaptivityStyleForLayoutElement:
- _objc_msgSend$activityHostViewControllerWithDescriptor:metricsRequest:payloadID:
- _objc_msgSend$defaultContentCornerRadius
- _objc_msgSend$genericIconLayerViewWithInfo:traitCollection:options:
- _objc_msgSend$initWithMenuIdentifier:session:
- _objc_msgSend$initWithObserver:bannerManager:sceneManager:pipManager:
- _objc_msgSend$initWithPIPContentType:sceneManager:
- _objc_msgSend$prepareToPresentMenuForIndirectInput
- _objc_msgSend$setAnimationCompletion:
- _objc_msgSend$systemApertureViewController:isDisplayingAnyRequiredSecureElements:
CStrings:
+ "\"!q"
+ "$!1"
+ "(%ld) Removing Recents Pod as we have no recent apps!"
+ "-[SBHomeScreenService hasConfiguredFilesStackWithURL:]"
+ "@\"<PLKLegibilityEnvironmentContext>\"24@0:8q16"
+ "@\"<SBSystemServiceServerMenuBarDelegate>\""
+ "@\"NSDictionary\"16@?0@\"SBLayoutState\"8"
+ "@\"NSString\"16@?0@\"CHSControlDescriptor\"8"
+ "@\"SBDeviceApplicationSceneHandle\"24@0:8@\"FBSSceneIdentityToken\"16"
+ "@\"SBMenuBarSystemService\""
+ "@40@0:8@16o^@24o^B32"
+ "@72@0:8{SBIconImageInfo={CGSize=dd}dd}16@48@56Q64"
+ "ArrangeFill"
+ "B24@0:8@\"NSURL\"16"
+ "B24@?0@\"SBDisplayItem\"8@\"SBDisplayItemLayoutAttributes\"16"
+ "Forcing System Aperture visible in order to display required priority element"
+ "Game overlay key shortcut handled by game policy."
+ "Invalidated"
+ "SBMenuBarSystemService"
+ "SBSystemServiceServerMenuBarDelegate"
+ "SBWallpaperUnlockProgressObserver"
+ "SBWindowingUsageMetric"
+ "SBWindowingUsageStageItem"
+ "SCENE IDENTIFIER"
+ "T@\"<SBSystemServiceServerMenuBarDelegate>\",W,N,V_menuBarDelegate"
+ "T@\"NSDate\",&,V_lastAppearanceTimestamp"
+ "T@\"SBMainDisplayLayoutState\",R,N,V_currentLayoutState"
+ "T@\"UIView\",R,N,V_buttonBackgroundView"
+ "TB,N,GisPresentingMenuForKeyPress,V_presentingMenuForKeyPress"
+ "TB,N,GisPresentingMenuForPointerHover,V_presentingMenuForPointerHover"
+ "TB,N,V_usesGlassGroup"
+ "TB,R,N,GisMaximized,V_maximized"
+ "TB,R,N,GisPointerTouch,V_pointerTouch"
+ "Telemetry"
+ "[%{public}@] setting keyboard arbiter suggested scene to z-order topmost scene %{public}@ "
+ "[coordinator] S33KR3T gen:%d begin host retry"
+ "[coordinator] S33KR3T gen:%d host not found; retrying once"
+ "[coordinator] S33KR3T gen:%d host retry usurped (current gen:%d)"
+ "[coordinator] gen:%d handling new keyboard arbiter request pid: %d sceneIdentity: %{public}@"
+ "[coordinator] ignoring KeyboardArbiter focus request(%{public}@): %{public}@"
+ "[coordinator] not a known app scene %{public}@"
+ "_addMediaPlaybackDisableReason:"
+ "_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:layoutAttributes:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
+ "_appLayoutOnStage"
+ "_buttonBackgroundView"
+ "_currentLayoutStateTransitionContext"
+ "_currentTransitionCompletionHandler"
+ "_draggedDisplayItemIntersectsHomeAffordanceArea"
+ "_effectiveInitialPositionY"
+ "_elementHasRequiredPriority"
+ "_flushStageWithItems:multitaskingMode:"
+ "_handleFocusChangeGenerationCount"
+ "_handleFocusSceneChange:fromArbiter:request:waitForSecretSceneHost:"
+ "_handleMenuBarServiceClientMessageTypeToggleVisibility:fromClient:"
+ "_handleSceneFocusChange_denyRequestForOverlayUI:"
+ "_handleSceneFocusChange_reasonToAvoidFocusingAppSceneIdentityToken:"
+ "_initialMultitaskingMode"
+ "_isDisplayingAnyRequiredPriorityElements"
+ "_isOrientationChanging"
+ "_itemsOnStage"
+ "_lock_clientRequestConfigurations"
+ "_lock_mediaPlaybackDisableReasons"
+ "_menuBarDelegate"
+ "_menuBarSystemService"
+ "_menuBarVisibilityRequestAuthenticator"
+ "_multitaskingModeForContext:"
+ "_presentMenuViewNonInteractively:forPointerHover:"
+ "_presentingMenuForKeyPress"
+ "_presentingMenuForPointerHover"
+ "_previousPeekingAppLayout"
+ "_removeMediaPlaybackDisableReason:"
+ "_resizedDisplayItemIntersectsHomeAffordanceArea"
+ "_sceneControllerHostingSceneIdentityToken:ultimateHostTarget:isSecretScene:"
+ "_shouldDodgeDock"
+ "_stageItemsInContext:"
+ "_toggleMenuBarVisibilityForClient:"
+ "_topmostZOrderedSceneExcluding:"
+ "_updatePreferredWindowControlsPlacementForSceneHandle:contentState:"
+ "_usesGlassGroup"
+ "_wallpaperUnlockProgressObservers"
+ "_whitePointAdaptivityStyleForSceneHandle:"
+ "activeMultitaskingSetting"
+ "activityHostViewControllerWithDescriptor:metricsRequest:payloadID:targetBundleIdentifier:"
+ "addWallpaperUnlockProgressObserver:"
+ "autoLayoutItemIntersectsHomeAffordanceArea:"
+ "buttonBackgroundView"
+ "com.apple.SpringBoard.Windowing.Usage"
+ "deviceApplicationSceneHandleForSceneIdentity:"
+ "frameForLayoutRole:inAppLayout:layoutAttributesMap:containerOrientation:windowScene:"
+ "genericApplicationIcon"
+ "hasConfiguredFilesStackWithURL:"
+ "initWithObserver:bannerManager:windowScene:pipManager:"
+ "initWithPIPContentType:windowScene:"
+ "initWithPointerTouch:"
+ "initWithSceneIdentifier:maximized:"
+ "invalid windowScene"
+ "isPresentingMenuForKeyPress"
+ "isPresentingMenuForPointerHover"
+ "legibilityEnvironmentContextForVariant:"
+ "makeIconImageWithInfo:traitCollection:context:options:"
+ "maximumPossibleMenuBarWidth"
+ "menuBarDelegate"
+ "numberOfAppsOnStage"
+ "numberOfMaximizedApps"
+ "numberOfWindowedApps"
+ "presenterMinimumPreferredEdgeInsets:"
+ "presentingMenuForKeyPress"
+ "presentingMenuForPointerHover"
+ "removeWallpaperUnlockProgressObserver:"
+ "sceneHandleForWhitePointAdaptivityStyle"
+ "secureWindowVisibilityDidChange:"
+ "setMenuBarDelegate:"
+ "setPresentingMenuForKeyPress:"
+ "setPresentingMenuForPointerHover:"
+ "setUsesGlassGroup:"
+ "supportsFlexibleWindowing"
+ "system service setting menu bar to visible: %d for client %{public}@"
+ "systemApertureViewController:isDisplayingAnyRequiredPriorityElements:"
+ "systemServiceServer:toggleMenuBarVisibilityForClient:"
+ "telemetryMultitaskingMode"
+ "updateGlassGroup"
+ "usesGlassGroup"
+ "v24@?0@\"SBWindowingUsageStageItem\"8^B16"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "wallpaperUnlockProgressDidUpdate:"
+ "wallpaperWindow"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}56@0:8q16@24@32q40@48"
+ "{UIEdgeInsets=dddd}24@0:8@\"<BNPresenting>\"16"
+ "\xc5R"
+ "\xf0\x82"
- "\"!"
- "$!"
- "%@ has no layout state transition coordinator- does your corresponding window scene exist yet?"
- "%@ has no layout state- does your corresponding window scene exist yet?"
- "%@ has no windowScene- we should!"
- "(%ld) !!!!!!!!!!!!!!!! We failed to populate default suggestions, going with stale lame set of apps we know the user has."
- "(%ld) Attempting _lastKnownGoodRecentApps update"
- "(%ld) Attempting _lastKnownGoodSuggestions update"
- "(%ld) Fetched predicted apps has no apps; using last known good predicted apps"
- "(%ld) Fetched recents apps has no apps; using last known good recent apps"
- "(%ld) Removing Recents Pod as the last known recents app is now hidden)"
- "(%ld) Timed out trying to retrieve default suggestions / recent apps"
- "(%ld) Updated _lastKnownGoodRecentApps"
- "(%ld) Updated _lastKnownGoodSuggestions"
- "(%ld) _lastKnownGoodRecentApps is same; skipping update"
- "(%ld) _lastKnownGoodSuggestions is same; skipping update"
- "@\"SBMainDisplayLayoutState\"16@0:8"
- "@192@0:8@16@24Q32q40@48d56d64{CGRect={CGPoint=dd}{CGSize=dd}}72B104B108q112q120{CGRect={CGPoint=dd}{CGSize=dd}}128{CGRect={CGPoint=dd}{CGSize=dd}}160"
- "@64@0:8{SBIconImageInfo={CGSize=dd}dd}16@48Q56"
- "Forcing System Aperture visible in order to display securely rendered element"
- "Game overlay key shortcut handled by game policy"
- "PRIMARY LAYOUT ELEMENT"
- "SBHTraitIconPresentationStyle"
- "SBTransientOverlayViewController.m"
- "SIDE LAYOUT ELEMENT"
- "T@\"NSDate\",&,N,V_lastAppearanceTimestamp"
- "T@\"SBLayoutState\",R,N,V_currentLayoutState"
- "T@\"SBMainDisplayLayoutState\",R,D,N"
- "TB,N,V_presentingMenuForIndirectInput"
- "[coordinator] handling new keyboard arbiter request pid: %d sceneIdentity: %{public}@"
- "_appLayoutByPerformingAutoLayoutIfNeededInAppLayout:previousAppLayout:options:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:source:flexibleAutoLayoutSource:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
- "_defaultSuggestedApps"
- "_filteredLastKnownGoodSuggestions"
- "_handleFocusSceneChange:fromArbiter:request:"
- "_isDisplayingAnyRequiredSecureContent"
- "_lastKnownGoodRecentApps"
- "_lastKnownGoodSuggestions"
- "_presentMenuViewNonInteractively:"
- "_presentingMenuForIndirectInput"
- "_sceneControllerHostingSceneIdentityToken:ultimateHostTarget:"
- "_secureDisplayRequired"
- "_selectedItemWasInitiallyFullscreen"
- "activityHostViewControllerWithDescriptor:metricsRequest:payloadID:"
- "com.apple.controlcenter.outsidecontentinteraction.pan"
- "com.apple.controlcenter.outsidecontentinteraction.tap"
- "defaultContentCornerRadius"
- "genericIconLayerViewWithInfo:traitCollection:options:"
- "initWithMenuIdentifier:session:"
- "initWithObserver:bannerManager:sceneManager:pipManager:"
- "initWithPIPContentType:sceneManager:"
- "invalid scene manager"
- "makeIconImageWithInfo:traitCollection:options:"
- "notificationViewControllerDidUpdateGlassInterfaceStyleToUserInterfaceStyle:notificationVC:"
- "prepareToPresentMenuForIndirectInput"
- "presentingMenuForIndirectInput"
- "setPresentingMenuForIndirectInput:"
- "systemApertureViewController:isDisplayingAnyRequiredSecureElements:"
- "v32@0:8q16@\"NCNotificationViewController\"24"
- "\xc5B"
- "\xf0r"

```
