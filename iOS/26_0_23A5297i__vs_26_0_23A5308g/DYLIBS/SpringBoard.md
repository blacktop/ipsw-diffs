## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.0.6.103.0
-  __TEXT.__text: 0xa7b764
-  __TEXT.__auth_stubs: 0x5550
+4557.0.9.100.0
+  __TEXT.__text: 0xa7df44
+  __TEXT.__auth_stubs: 0x5500
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb6ec0
-  __TEXT.__const: 0x12be0
-  __TEXT.__oslogstring: 0x5d2b6
-  __TEXT.__cstring: 0x7c56f
-  __TEXT.__gcc_except_tab: 0x16e04
+  __TEXT.__objc_methlist: 0xb74c0
+  __TEXT.__const: 0x12c20
+  __TEXT.__oslogstring: 0x5d829
+  __TEXT.__cstring: 0x7ca15
+  __TEXT.__gcc_except_tab: 0x16d98
   __TEXT.__ustring: 0xcac
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2bd50
-  __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x21f7a
-  __TEXT.__objc_methname: 0x1cc04a
-  __TEXT.__objc_methtype: 0x4c1ec
-  __TEXT.__objc_stubs: 0xf21c0
-  __DATA_CONST.__got: 0xa140
-  __DATA_CONST.__const: 0x1c9b8
-  __DATA_CONST.__objc_classlist: 0x5220
+  __TEXT.__unwind_info: 0x2be40
+  __TEXT.__eh_frame: 0xb8
+  __TEXT.__objc_classname: 0x220e5
+  __TEXT.__objc_methname: 0x1cd603
+  __TEXT.__objc_methtype: 0x4c52c
+  __TEXT.__objc_stubs: 0xf2e60
+  __DATA_CONST.__got: 0xa0f8
+  __DATA_CONST.__const: 0x1ca58
+  __DATA_CONST.__objc_classlist: 0x5240
   __DATA_CONST.__objc_catlist: 0x348
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2908
+  __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a248
+  __DATA_CONST.__objc_selrefs: 0x4a5d8
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3f70
-  __DATA_CONST.__objc_arraydata: 0x1828
-  __AUTH_CONST.__auth_got: 0x2ac0
-  __AUTH_CONST.__const: 0x10848
-  __AUTH_CONST.__cfstring: 0x6e5a0
-  __AUTH_CONST.__objc_const: 0x2673f0
-  __AUTH_CONST.__objc_arrayobj: 0x1728
+  __DATA_CONST.__objc_superrefs: 0x3f80
+  __DATA_CONST.__objc_arraydata: 0x1830
+  __AUTH_CONST.__auth_got: 0x2a98
+  __AUTH_CONST.__const: 0x108e8
+  __AUTH_CONST.__cfstring: 0x6eb00
+  __AUTH_CONST.__objc_const: 0x2684f8
+  __AUTH_CONST.__objc_arrayobj: 0x1740
   __AUTH_CONST.__objc_doubleobj: 0x680
-  __AUTH_CONST.__objc_intobj: 0x2b98
+  __AUTH_CONST.__objc_intobj: 0x2bb0
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x108b0
-  __DATA.__objc_ivar: 0xf1f4
-  __DATA.__data: 0x1f740
+  __AUTH.__objc_data: 0x10450
+  __DATA.__objc_ivar: 0xf290
+  __DATA.__data: 0x1f8b8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xac8
+  __DATA.__bss: 0xa98
   __DATA.__common: 0xa40
-  __DATA_DIRTY.__objc_data: 0x22c90
+  __DATA_DIRTY.__objc_data: 0x23230
   __DATA_DIRTY.__data: 0x180
-  __DATA_DIRTY.__bss: 0x1a40
+  __DATA_DIRTY.__bss: 0x1a80
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices
   - /System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost
   - /System/Library/PrivateFrameworks/BannerKit.framework/BannerKit

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 4D8E3042-FE86-3980-B46B-11002D71139C
-  Functions: 69743
-  Symbols:   235826
-  CStrings:  103521
+  UUID: E710F3EB-903D-3F2E-A529-283E621C7850
+  Functions: 69871
+  Symbols:   236265
+  CStrings:  103821
 
Symbols:
+ +[SBEdgeResizeSystemPointerInteractionHelper latchingAxesForHoveredEdge:]
+ +[SBInteractiveScreenshotGestureRoundedCropsView _roundedCropsCornerRadius]
+ +[SBMenuBarBackgroundVariableBlurView layerClass]
+ +[SBSceneHostingExternalSettingsModifierServiceSingleton startService]
+ +[SBSceneHostingExternalSettingsModifierServiceSingleton startService].cold.1
+ -[SBActivityBannerObserver _postBannerWithAlert:]
+ -[SBActivityBannerObserver presentFallbackAlert:]
+ -[SBActivityManager alertPresentationFailed:]
+ -[SBActivitySystemApertureElementObserver presentFallbackAlert:]
+ -[SBAlertProvidedContentElement .cxx_destruct]
+ -[SBAlertProvidedContentElement alertHost]
+ -[SBAlertProvidedContentElement setAlertHost:]
+ -[SBAppSwitcherWallpaperGradientView setCornerRadii:]
+ -[SBAppViewController applicationSceneViewController:didRequestWindowControlsAdaptiveStyle:adaptive:]
+ -[SBApplication(ChamoisCapabilities) onlySupportsOneOrientation]
+ -[SBContinuousExposeAppToAppModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:]
+ -[SBContinuousExposeHomeGestureSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:]
+ -[SBContinuousExposeWindowDragContainerGestureSwitcherModifier .cxx_destruct]
+ -[SBContinuousExposeWindowDragContainerGestureSwitcherModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:]
+ -[SBContinuousExposeWindowDropSwitcherModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:]
+ -[SBCoverSheetPresentationManager _setCoverSheetPresented:forcePresented:animated:dismissModalPresentation:options:withCompletion:]
+ -[SBCoverSheetPresentationManager setCoverSheetPresented:animated:dismissModalPresentation:withCompletion:]
+ -[SBCoverSheetSlidingViewController _contentViewFrame]
+ -[SBCoverSheetSlidingViewController setTrailingIndicatorAnimationViewVelocityY:]
+ -[SBCoverSheetSlidingViewController setTrailingIndicatorTransitionViewVelocityY:]
+ -[SBCoverSheetSlidingViewController trailingIndicatorAnimationViewVelocityY]
+ -[SBCoverSheetSlidingViewController trailingIndicatorTransitionViewVelocityY]
+ -[SBDashBoardSetupView _hasNonCursiveSuppressingUI]
+ -[SBDashBoardSetupView _hasSuppressingUI]
+ -[SBDashBoardSetupView _updateHelloVisibility]
+ -[SBDashBoardSetupViewController _canShowSolariumCursiveAnimation]
+ -[SBDeviceApplicationSceneViewController _updateWindowControlsAdaptiveStyle]
+ -[SBFlexibleWindowingAutoLayoutItem intersectedDisplayRectCorners]
+ -[SBFlexibleWindowingAutoLayoutItem setIntersectedDisplayRectCorners:]
+ -[SBFlexibleWindowingHomeGestureSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:]
+ -[SBFloatingDockRemoteContentManager applicationRestrictionController:didUpdateVisibleTags:hiddenTags:]
+ -[SBFloatingDockRemoteContentManager handleInstalledAppsDidChange:]
+ -[SBFloatingDockRemoteContentManager hiddenRestorableFileStackIcons]
+ -[SBFloatingDockRemoteContentManager setHiddenRestorableFileStackIcons:]
+ -[SBFluidSwitcherViewController _performUpdateMenuBarVisibilityResponse:]
+ -[SBFullScreenSwitcherSceneLiveContentOverlay applicationSceneViewController:didRequestWindowControlsAdaptiveStyle:adaptive:]
+ -[SBFullScreenToHomePIPSwitcherModifier transitionWillUpdate]
+ -[SBHomeScreenController suggestionsWidgetViewController:iconForApplicationWithBundleIdentifier:]
+ -[SBItemResizeTransitionSwitcherModifier initWithTransitionID:selectedAppLayout:selectedLayoutRole:]
+ -[SBItemResizeTransitionSwitcherModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:]
+ -[SBLockScreenManager coverSheetViewControllerDidPresentPasscodeLockView:]
+ -[SBLowPowerAlertItem _setLowPowerMode:]
+ -[SBLowPowerAlertItem _toggleLowPowerMode]
+ -[SBMainSwitcherControllerCoordinator switcherContentControllerWantsToUpdateMenuBarVisibility:]
+ -[SBMedusaDecoratedDeviceApplicationSceneViewController applicationSceneViewController:didRequestWindowControlsAdaptiveStyle:adaptive:]
+ -[SBMenuBarBackgroundVariableBlurView .cxx_destruct]
+ -[SBMenuBarBackgroundVariableBlurView delegate]
+ -[SBMenuBarBackgroundVariableBlurView initWithDelegate:]
+ -[SBMenuBarBackgroundVariableBlurView layoutSubviews]
+ -[SBMenuBarManager _dismissMenuBarAnimated:]
+ -[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]
+ -[SBMenuBarManager _hitTestInMenuBarContentWithPoint:gestureWindow:]
+ -[SBMenuBarManager _setMenuBarVisible:animated:]
+ -[SBMenuBarManager _updateMenuBarVisibilityWithRequestedVisibility:]
+ -[SBMenuBarManager isMenuBarSupported]
+ -[SBMenuBarManager requestMenuBarVisibility:]
+ -[SBMenuBarManager shouldDisableMenusForAppRestrictionForViewController:]
+ -[SBMenuBarManager updateMenuBarVisibility]
+ -[SBMenuBarSettings alwaysVisibleOnExternalDisplay]
+ -[SBMenuBarSettings backgroundBlurContentOverhang]
+ -[SBMenuBarSettings entryAnimationDamping]
+ -[SBMenuBarSettings entryAnimationDuration]
+ -[SBMenuBarSettings entryAnimationMass]
+ -[SBMenuBarSettings entryAnimationStiffness]
+ -[SBMenuBarSettings exitAnimationDamping]
+ -[SBMenuBarSettings exitAnimationDuration]
+ -[SBMenuBarSettings exitAnimationMass]
+ -[SBMenuBarSettings exitAnimationStiffness]
+ -[SBMenuBarSettings setAlwaysVisibleOnExternalDisplay:]
+ -[SBMenuBarSettings setBackgroundBlurContentOverhang:]
+ -[SBMenuBarSettings setEntryAnimationDamping:]
+ -[SBMenuBarSettings setEntryAnimationDuration:]
+ -[SBMenuBarSettings setEntryAnimationMass:]
+ -[SBMenuBarSettings setEntryAnimationStiffness:]
+ -[SBMenuBarSettings setExitAnimationDamping:]
+ -[SBMenuBarSettings setExitAnimationDuration:]
+ -[SBMenuBarSettings setExitAnimationMass:]
+ -[SBMenuBarSettings setExitAnimationStiffness:]
+ -[SBMenuBarSystemService _queryMenuBarSupportedForClient:withCompletion:]
+ -[SBMenuBarSystemService _queryMenuBarSupportedForClient:withCompletion:].cold.1
+ -[SBMenuBarSystemService systemServiceServer:queryMenuBarSupportedForClient:withCompletion:]
+ -[SBMenuBarViewController backgroundEffectContainerView]
+ -[SBMenuBarViewController desiredBlurWidth]
+ -[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:]
+ -[SBMenuBarViewController initWithScene:delegate:animateInitialPresentation:loadCompletion:]
+ -[SBMenuBarViewController setBackgroundEffectContainerView:]
+ -[SBMenuBarViewController setVariableBlurNeeded:]
+ -[SBMenuBarViewController setVariableBlurView:]
+ -[SBMenuBarViewController variableBlurNeeded]
+ -[SBMenuBarViewController variableBlurView]
+ -[SBPosterBoardUpdateManager _backgroundTaskIdentifierForUpdate:]
+ -[SBPosterBoardUpdateManager _backgroundTaskIdentifierForUpdate:].cold.1
+ -[SBPosterBoardUpdateManager _backgroundTaskIdentifierForUpdate:].cold.2
+ -[SBPosterBoardUpdateManager _isBGSystemTaskUpdate:]
+ -[SBPosterBoardUpdateManager _submitTaskRequestForUpdate:]
+ -[SBPosterBoardUpdateManager _submitTaskRequestForUpdate:].cold.1
+ -[SBPowerAlertElement _extendDismissalTimer]
+ -[SBPowerAlertElement _secondaryTextColorForStyle]
+ -[SBPowerAlertElement _secondaryTextForStyle]
+ -[SBPowerAlertElement _updateLowPowerMode]
+ -[SBPowerAlertElement action]
+ -[SBPowerAlertElement dealloc]
+ -[SBPowerAlertElement dismissalTimer]
+ -[SBPowerAlertElement handleElementViewEvent:]
+ -[SBPowerAlertElement secondaryContent]
+ -[SBPowerAlertElement setAction:]
+ -[SBPowerAlertElement setDismissalTimer:]
+ -[SBPowerAlertElement setSecondaryContent:]
+ -[SBPowerAlertElement setTrailingLowBatteryStyleIconPackageView:]
+ -[SBPowerAlertElement trailingLowBatteryStyleIconPackageView]
+ -[SBSceneHostingExternalSettingsModifierServiceDelegate .cxx_destruct]
+ -[SBSceneHostingExternalSettingsModifierServiceDelegate init]
+ -[SBSceneHostingExternalSettingsModifierServiceDelegate settingsModifiersForClientProcessIdentity:hostedBy:]
+ -[SBStatusBarStateAggregator _batteryDomainData]
+ -[SBSwitcherController isMenuBarSupported]
+ -[SBSwitcherWindowingConfiguration setStripOffscreenPadding:]
+ -[SBSwitcherWindowingConfiguration stripOffscreenPadding]
+ -[SBSwitcherWindowingSettings setStageCornerRadiusSettings:]
+ -[SBSwitcherWindowingSettings stageCornerRadiusSettings]
+ -[SBSystemServiceServer _handleMenuBarServiceClientMessageTypeQuerySupported:fromClient:]
+ -[SBSystemStatusBatteryDataProvider lastPublishedData]
+ -[SBTopAffordanceViewController updateWindowControlsAdaptiveStyle:adaptive:]
+ -[SBUpdateMenuBarVisibilitySwitcherEventResponse type]
+ -[SBWorkspaceApplicationSceneTransitionContext itemsCrossingToOtherDisplay]
+ -[SBWorkspaceApplicationSceneTransitionContext setItemsCrossingToOtherDisplay:]
+ -[_SBDisplayItemFixedAspectGrid initWithBounds:fixedSize:screenScale:supportsOrthogonalSizes:windowingConfiguration:allowsLetterboxing:]
+ GCC_except_table118
+ GCC_except_table178
+ GCC_except_table182
+ GCC_except_table231
+ GCC_except_table274
+ GCC_except_table297
+ GCC_except_table323
+ GCC_except_table401
+ GCC_except_table528
+ GCC_except_table808
+ GCC_except_table848
+ GCC_except_table857
+ GCC_except_table900
+ GCC_except_table939
+ GCC_except_table98
+ OBJC_IVAR_$_SBSceneHostingExternalSettingsModifierServiceDelegate._externalSettingsModifierService
+ _CACornerRadiiEqualToRadii
+ _OBJC_CLASS_$_BGNonRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGRepeatingSystemTaskRequest
+ _OBJC_CLASS_$_BGSystemTaskScheduler
+ _OBJC_CLASS_$_SASCaptureSessionTextureDataSource
+ _OBJC_CLASS_$_SBMenuBarBackgroundVariableBlurView
+ _OBJC_CLASS_$_SBSceneHostingExternalSettingsModifierServiceDelegate
+ _OBJC_CLASS_$_SBSceneHostingExternalSettingsModifierServiceSingleton
+ _OBJC_CLASS_$_SBUpdateMenuBarVisibilitySwitcherEventResponse
+ _OBJC_CLASS_$_SSChromeHelper
+ _OBJC_CLASS_$_UISSceneHostingExternalSettingsModifierService
+ _OBJC_CLASS_$__UISceneClassicModeExternalSettingsModifier
+ _OBJC_IVAR_$_SBAlertProvidedContentElement._alertHost
+ _OBJC_IVAR_$_SBAppSwitcherWallpaperGradientView._cornerRadii
+ _OBJC_IVAR_$_SBContinuousExposeAppToAppModifier._displayItemsChangingPosition
+ _OBJC_IVAR_$_SBContinuousExposeAppToAppModifier._isFromPeek
+ _OBJC_IVAR_$_SBContinuousExposeWindowDragContainerGestureSwitcherModifier._selectedDisplayItem
+ _OBJC_IVAR_$_SBCoverSheetSlidingViewController._trailingIndicatorAnimationViewVelocityY
+ _OBJC_IVAR_$_SBCoverSheetSlidingViewController._trailingIndicatorTransitionViewVelocityY
+ _OBJC_IVAR_$_SBDashBoardSetupView._glassTextureDataSource
+ _OBJC_IVAR_$_SBDynamicLightingController._disableSpecularsForHomeScreenDefaultAssertion
+ _OBJC_IVAR_$_SBFlexibleWindowingAutoLayoutItem._intersectedDisplayRectCorners
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._layoutGrid
+ _OBJC_IVAR_$_SBFloatingDockRemoteContentManager._hiddenRestorableFileStackIcons
+ _OBJC_IVAR_$_SBItemResizeTransitionSwitcherModifier._selectedDisplayItem
+ _OBJC_IVAR_$_SBMenuBarBackgroundVariableBlurView._delegate
+ _OBJC_IVAR_$_SBMenuBarBackgroundVariableBlurView._gradientMaskLayer
+ _OBJC_IVAR_$_SBMenuBarManager._gestureDefaults
+ _OBJC_IVAR_$_SBMenuBarSettings._alwaysVisibleOnExternalDisplay
+ _OBJC_IVAR_$_SBMenuBarSettings._backgroundBlurContentOverhang
+ _OBJC_IVAR_$_SBMenuBarSettings._entryAnimationDamping
+ _OBJC_IVAR_$_SBMenuBarSettings._entryAnimationDuration
+ _OBJC_IVAR_$_SBMenuBarSettings._entryAnimationMass
+ _OBJC_IVAR_$_SBMenuBarSettings._entryAnimationStiffness
+ _OBJC_IVAR_$_SBMenuBarSettings._exitAnimationDamping
+ _OBJC_IVAR_$_SBMenuBarSettings._exitAnimationDuration
+ _OBJC_IVAR_$_SBMenuBarSettings._exitAnimationMass
+ _OBJC_IVAR_$_SBMenuBarSettings._exitAnimationStiffness
+ _OBJC_IVAR_$_SBMenuBarViewController._animateInitialPresentation
+ _OBJC_IVAR_$_SBMenuBarViewController._backgroundEffectContainerView
+ _OBJC_IVAR_$_SBMenuBarViewController._variableBlurNeeded
+ _OBJC_IVAR_$_SBMenuBarViewController._variableBlurView
+ _OBJC_IVAR_$_SBPowerAlertElement._action
+ _OBJC_IVAR_$_SBPowerAlertElement._dismissalTimer
+ _OBJC_IVAR_$_SBPowerAlertElement._secondaryContent
+ _OBJC_IVAR_$_SBPowerAlertElement._trailingLowBatteryStyleIconPackageView
+ _OBJC_IVAR_$_SBRecordingIndicatorViewController._defaultGainMapDefeatingLayer
+ _OBJC_IVAR_$_SBStatusBarStateAggregator._hasReceivedBatteryDataFromSystemStatus
+ _OBJC_IVAR_$_SBSwitcherWindowingConfiguration._stripOffscreenPadding
+ _OBJC_IVAR_$_SBSwitcherWindowingSettings._stageCornerRadiusSettings
+ _OBJC_IVAR_$_SBSystemStatusBatteryDataProvider._lastPublishedData
+ _OBJC_IVAR_$_SBWorkspaceApplicationSceneTransitionContext._itemsCrossingToOtherDisplay
+ _OBJC_IVAR_$__SBDisplayItemFixedAspectGrid._allowsLetterboxing
+ _OBJC_METACLASS_$_SBMenuBarBackgroundVariableBlurView
+ _OBJC_METACLASS_$_SBSceneHostingExternalSettingsModifierServiceDelegate
+ _OBJC_METACLASS_$_SBSceneHostingExternalSettingsModifierServiceSingleton
+ _OBJC_METACLASS_$_SBUpdateMenuBarVisibilitySwitcherEventResponse
+ _SBCALayerCornerCurveForRadius
+ _SBFIsFullScreenLetterboxingAvailable
+ _SBSystemStatusBatteryDataProviderDidChangeNotification
+ _SBWorkspaceTerminateProcesses
+ __OBJC_$_CLASS_METHODS_SBInteractiveScreenshotGestureRoundedCropsView
+ __OBJC_$_CLASS_METHODS_SBMenuBarBackgroundVariableBlurView
+ __OBJC_$_CLASS_METHODS_SBSceneHostingExternalSettingsModifierServiceSingleton
+ __OBJC_$_INSTANCE_METHODS_SBMenuBarBackgroundVariableBlurView
+ __OBJC_$_INSTANCE_METHODS_SBSceneHostingExternalSettingsModifierServiceDelegate
+ __OBJC_$_INSTANCE_METHODS_SBUpdateMenuBarVisibilitySwitcherEventResponse
+ __OBJC_$_INSTANCE_VARIABLES_SBAlertProvidedContentElement
+ __OBJC_$_INSTANCE_VARIABLES_SBContinuousExposeWindowDragContainerGestureSwitcherModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBMenuBarBackgroundVariableBlurView
+ __OBJC_$_INSTANCE_VARIABLES_SBSceneHostingExternalSettingsModifierServiceDelegate
+ __OBJC_$_PROP_LIST_SBMenuBarBackgroundVariableBlurView
+ __OBJC_$_PROP_LIST_SBSceneHostingExternalSettingsModifierServiceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_APUISuggestionsWidgetViewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UISSceneHostingExternalSettingsModifierServiceDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBMenuBarBackgroundVariableBlurViewDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBWindowControlsControlling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_APUISuggestionsWidgetViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBMenuBarBackgroundVariableBlurViewDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBWindowControlsControlling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UISSceneHostingExternalSettingsModifierServiceDelegate
+ __OBJC_$_PROTOCOL_REFS_SBMenuBarBackgroundVariableBlurViewDelegate
+ __OBJC_$_PROTOCOL_REFS_SBWindowControlsControlling
+ __OBJC_$_PROTOCOL_REFS_UISSceneHostingExternalSettingsModifierServiceDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SBSceneHostingExternalSettingsModifierServiceDelegate
+ __OBJC_CLASS_RO_$_SBMenuBarBackgroundVariableBlurView
+ __OBJC_CLASS_RO_$_SBSceneHostingExternalSettingsModifierServiceDelegate
+ __OBJC_CLASS_RO_$_SBSceneHostingExternalSettingsModifierServiceSingleton
+ __OBJC_CLASS_RO_$_SBUpdateMenuBarVisibilitySwitcherEventResponse
+ __OBJC_LABEL_PROTOCOL_$_APUISuggestionsWidgetViewControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBMenuBarBackgroundVariableBlurViewDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBWindowControlsControlling
+ __OBJC_LABEL_PROTOCOL_$_UISSceneHostingExternalSettingsModifierServiceDelegate
+ __OBJC_METACLASS_RO_$_SBMenuBarBackgroundVariableBlurView
+ __OBJC_METACLASS_RO_$_SBSceneHostingExternalSettingsModifierServiceDelegate
+ __OBJC_METACLASS_RO_$_SBSceneHostingExternalSettingsModifierServiceSingleton
+ __OBJC_METACLASS_RO_$_SBUpdateMenuBarVisibilitySwitcherEventResponse
+ __OBJC_PROTOCOL_$_APUISuggestionsWidgetViewControllerDelegate
+ __OBJC_PROTOCOL_$_SBMenuBarBackgroundVariableBlurViewDelegate
+ __OBJC_PROTOCOL_$_SBWindowControlsControlling
+ __OBJC_PROTOCOL_$_UISSceneHostingExternalSettingsModifierServiceDelegate
+ ___102-[SBContinuousExposeHomeGestureSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:]_block_invoke
+ ___103-[SBFlexibleWindowingHomeGestureSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:]_block_invoke
+ ___106-[SBSystemApertureSceneElement contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:]_block_invoke.246
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.302
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.303
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.304
+ ___113-[SBFluidSwitcherViewController initWithPersonality:liveContentOverlayCoordinator:dataSource:delegate:debugName:]_block_invoke.204
+ ___116-[SBAssistantSession presentSiriPresentationViewController:withAnimationFactory:siriPresentationOptions:completion:]_block_invoke.86
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.645
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.647
+ ___131-[SBCoverSheetPresentationManager _setCoverSheetPresented:forcePresented:animated:dismissModalPresentation:options:withCompletion:]_block_invoke
+ ___138-[SBCoverSheetSlidingViewController _finishTransitionToPresented:forcingTransition:ignoringPreflightRequirements:animated:withCompletion:]_block_invoke.101
+ ___138-[SBCoverSheetSlidingViewController _finishTransitionToPresented:forcingTransition:ignoringPreflightRequirements:animated:withCompletion:]_block_invoke.101.cold.1
+ ___138-[SBCoverSheetSlidingViewController _finishTransitionToPresented:forcingTransition:ignoringPreflightRequirements:animated:withCompletion:]_block_invoke.115
+ ___138-[SBDashBoardHostableEntityPresentationManager presentEntity:fromRequest:animated:withEphemeralSwitcher:dismissGestureEnabled:completion:]_block_invoke_4
+ ___40-[SBLowPowerAlertItem _setLowPowerMode:]_block_invoke
+ ___42-[SBPowerAlertElement _updateLowPowerMode]_block_invoke
+ ___44-[SBPosterBoardUpdateManager executeUpdate:]_block_invoke.6
+ ___44-[SBPowerAlertElement _extendDismissalTimer]_block_invoke
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1210
+ ___48-[SBMenuBarManager _setMenuBarVisible:animated:]_block_invoke
+ ___48-[SBMenuBarManager _setMenuBarVisible:animated:]_block_invoke_2
+ ___48-[SBMenuBarManager _setMenuBarVisible:animated:]_block_invoke_3
+ ___48-[SBMenuBarManager _setMenuBarVisible:animated:]_block_invoke_4
+ ___49-[SBActivityBannerObserver _postBannerWithAlert:]_block_invoke
+ ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.82
+ ___51-[SBStatusBarStateAggregator _updateTetheringState]_block_invoke.231
+ ___53-[SBLockScreenManager activateLostModeForRemoteLock:]_block_invoke
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.751
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.782
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.813
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.919
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.806
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.923
+ ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.759
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke.96
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_10.112
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_11.113
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_12.115
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_13.116
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_14.117
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_15.119
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_16.120
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_17.121
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_18.124
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_19.126
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_2.99
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_3.101
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_4.102
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_5.105
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_6.107
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_7.108
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_8.109
+ ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_9.111
+ ___56-[SBAssistantController _updateControlWidgetEligibility]_block_invoke.268
+ ___56-[SBCaptureHardwareButtonAppActivator _launchCaptureApp]_block_invoke.197
+ ___56-[SBCaptureHardwareButtonAppActivator _launchCaptureApp]_block_invoke.199
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1755
+ ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.500
+ ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.507
+ ___59-[SBFloatingDockRemoteContentManager iconView:performDrop:]_block_invoke.73
+ ___59-[SBFloatingDockRemoteContentManager iconView:performDrop:]_block_invoke.75
+ ___59-[SBMainSwitcherControllerCoordinator _buildAppLayoutCache]_block_invoke_12
+ ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke
+ ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke_2
+ ___59-[SBMenuBarManager _dismissMenuBarAnimated:withCompletion:]_block_invoke_3
+ ___60-[SBMainWorkspace _preflightTransitionRequest:forExecution:]_block_invoke.376
+ ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.927
+ ___64-[SBActivityManager _activityStartedOrUpdatedWithContentUpdate:]_block_invoke.45
+ ___64-[SBAssistantController alwaysOnLiveRenderingAssertionRequested]_block_invoke.212
+ ___66-[SBAssistantSession presentSiriEffectsViewController:completion:]_block_invoke.104
+ ___68-[SBCoverSheetSlidingViewController _updateForLocation:interactive:]_block_invoke.131
+ ___68-[SBCoverSheetSlidingViewController _updateForLocation:interactive:]_block_invoke.131.cold.1
+ ___69-[SBDashBoardEmergencyDialerViewController _updateEmergencyCallMode:]_block_invoke.43
+ ___70+[SBSceneHostingExternalSettingsModifierServiceSingleton startService]_block_invoke
+ ___70-[SBDashBoardEmergencyDialerController launchEmergencyDialerAnimated:]_block_invoke_2
+ ___71-[SBAssistantController siriPresentation:requestsPunchout:withHandler:]_block_invoke.231
+ ___71-[SBAssistantController siriPresentation:requestsPunchout:withHandler:]_block_invoke.236
+ ___72-[SBCoverSheetSlidingViewController _animationTickForPresentationValue:]_block_invoke
+ ___72-[SBCoverSheetSlidingViewController _animationTickForPresentationValue:]_block_invoke.cold.1
+ ___72-[SBSwitcherController _ancillaryTransitionRequestForTransitionRequest:]_block_invoke_8
+ ___73-[SBCoverSheetSlidingViewController _transitionTickForPresentationValue:]_block_invoke
+ ___73-[SBCoverSheetSlidingViewController _transitionTickForPresentationValue:]_block_invoke.cold.1
+ ___74-[SBControlCenterController initWithWindowScene:controlCenterCoordinator:]_block_invoke_4
+ ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1076
+ ___74-[SBMenuBarViewController dismissAnimated:alongsideAnimations:completion:]_block_invoke
+ ___78-[SBDashBoardEmergencyDialerViewController _activateEmergencyDialerController]_block_invoke.38
+ ___78-[SBDashBoardSetupView prepareSolariumCursiveTextViewWithDelegate:completion:]_block_invoke.16
+ ___78-[SBDashBoardSetupView prepareSolariumCursiveTextViewWithDelegate:completion:]_block_invoke_2.18
+ ___78-[SBDashBoardSetupView prepareSolariumCursiveTextViewWithDelegate:completion:]_block_invoke_2.18.cold.1
+ ___78-[SBDashBoardSetupViewController _retrieveChildIconIfNecessaryWithCompletion:]_block_invoke.cold.2
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke.122
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_2.124
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_32
+ ___79-[SBMainWorkspace _removeApplicationEntities:withDestructionIntent:completion:]_block_invoke.468
+ ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.361
+ ___83-[SBAssistantController siriPresentation:requestsDismissalWithOptions:withHandler:]_block_invoke.225
+ ___83-[SBCoverSheetSlidingViewController _performAppFlyInToPresented:animated:velocity:]_block_invoke.116
+ ___83-[SBCoverSheetSlidingViewController _performAppFlyInToPresented:animated:velocity:]_block_invoke.116.cold.1
+ ___83-[SBMainDisplaySceneManager _noteDidChangeToVisibility:previouslyExisted:forScene:]_block_invoke
+ ___83-[SBMainDisplaySceneManager _noteDidChangeToVisibility:previouslyExisted:forScene:]_block_invoke_2
+ ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke.47
+ ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke_2.48
+ ___86-[SBAssistantController siriPresentation:requestsPresentationWithOptions:withHandler:]_block_invoke.224
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.360
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.361
+ ___88-[SBFluidSwitcherViewController _setupPIPMorphingIfNeededForTransitionContext:response:]_block_invoke
+ ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.78
+ ___89-[SBSystemServiceServer _handleMenuBarServiceClientMessageTypeQuerySupported:fromClient:]_block_invoke
+ ___89-[SBSystemServiceServer _handleMenuBarServiceClientMessageTypeQuerySupported:fromClient:]_block_invoke_2
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1607
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1609
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1611
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1615
+ ___91-[SBStatusBarStateAggregator _updateCallingBackgroundActivityAssertionsForCallDescriptors:]_block_invoke.240
+ ___91-[SBStatusBarStateAggregator _updateCallingBackgroundActivityAssertionsForCallDescriptors:]_block_invoke.240.cold.1
+ ___92-[SBMenuBarSystemService systemServiceServer:queryMenuBarSupportedForClient:withCompletion:]_block_invoke
+ ___94-[SBAssistantController siriPresentation:requestsDismissalOfEffectsViewControllerWithHandler:]_block_invoke.223
+ ___94-[SBFlexibleWindowingItemResizeGestureSwitcherModifier _responseForGestureUpdateAtGestureEnd:]_block_invoke_2
+ ___94-[SBFlexibleWindowingItemResizeGestureSwitcherModifier _responseForGestureUpdateAtGestureEnd:]_block_invoke_3
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.640
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.662
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.677
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.681
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.689
+ ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke.212
+ ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke.216
+ ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke_2.217
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1738
+ ___98-[SBAssistantController siriPresentation:requestsPresentationOfEffectsViewController:withHandler:]_block_invoke.218
+ ___SetDisplayShowsProgress_block_invoke.100
+ ___SetDisplayShowsProgress_block_invoke.101
+ ___SetDisplayShowsProgress_block_invoke.99
+ ____SBXXAcquireFocusPreventingFullScreenPresentationAssertion_block_invoke.186
+ ____SBXXAddWallpaperAnimationSuspensionAssertion_block_invoke.175
+ ____SBXXSetAllApplicationsShowSyncIndicator_block_invoke.109
+ ____SBXXSetShowsOverridesForRecording_block_invoke.113
+ ____SBXXSetWallpaperImageSurfaceForLocations_block_invoke.169
+ ___block_descriptor_32_e30_B16?0"FBApplicationProcess"8l
+ ___block_descriptor_40_e8_32bs_e31_v24?0"ACAccount"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32w_e36_v16?0"_UIMainMenuSessionResponse"8lw32l8
+ ___block_descriptor_40_e8_32w_e44_v16?0"SASCaptureSessionTextureDataSource"8lw32l8
+ ___block_descriptor_48_e29_{CGPoint=dd}24?0{CGSize=dd}8l
+ ___block_descriptor_48_e8_32s40r_e34_v24?0"SBSwitcherController"8^B16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e33_v24?0"BSTransaction"8?<v?B>16lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e22_v16?0"BGSystemTask"8ls32l8
+ ___block_descriptor_64_e8_32r40r48r56r_e5_v8?0lr32l8r40l8r48l8r56l8
+ ___block_descriptor_74_e8_32s40s48s56s64w_e8_v12?0B8lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.104
+ ___block_literal_global.1056
+ ___block_literal_global.1065
+ ___block_literal_global.1089
+ ___block_literal_global.1101
+ ___block_literal_global.113
+ ___block_literal_global.1153
+ ___block_literal_global.1156
+ ___block_literal_global.1161
+ ___block_literal_global.1167
+ ___block_literal_global.1193
+ ___block_literal_global.123
+ ___block_literal_global.1241
+ ___block_literal_global.128
+ ___block_literal_global.1460
+ ___block_literal_global.1581
+ ___block_literal_global.1585
+ ___block_literal_global.1617
+ ___block_literal_global.162
+ ___block_literal_global.1626
+ ___block_literal_global.1628
+ ___block_literal_global.1630
+ ___block_literal_global.1632
+ ___block_literal_global.1648
+ ___block_literal_global.1764
+ ___block_literal_global.177
+ ___block_literal_global.1787
+ ___block_literal_global.1796
+ ___block_literal_global.1812
+ ___block_literal_global.194
+ ___block_literal_global.215
+ ___block_literal_global.230
+ ___block_literal_global.243
+ ___block_literal_global.266
+ ___block_literal_global.270
+ ___block_literal_global.272
+ ___block_literal_global.275
+ ___block_literal_global.279
+ ___block_literal_global.309
+ ___block_literal_global.335
+ ___block_literal_global.348
+ ___block_literal_global.351
+ ___block_literal_global.353
+ ___block_literal_global.356
+ ___block_literal_global.467
+ ___block_literal_global.487
+ ___block_literal_global.488
+ ___block_literal_global.490
+ ___block_literal_global.493
+ ___block_literal_global.497
+ ___block_literal_global.500
+ ___block_literal_global.503
+ ___block_literal_global.536
+ ___block_literal_global.540
+ ___block_literal_global.595
+ ___block_literal_global.628
+ ___block_literal_global.634
+ ___block_literal_global.650
+ ___block_literal_global.662
+ ___block_literal_global.664
+ ___block_literal_global.669
+ ___block_literal_global.680
+ ___block_literal_global.686
+ ___block_literal_global.706
+ ___block_literal_global.732
+ ___block_literal_global.774
+ ___block_literal_global.800
+ ___block_literal_global.807
+ ___block_literal_global.809
+ ___block_literal_global.811
+ ___block_literal_global.814
+ ___block_literal_global.848
+ ___block_literal_global.876
+ ___block_literal_global.881
+ ___block_literal_global.885
+ ___block_literal_global.887
+ ___block_literal_global.891
+ ___block_literal_global.893
+ ___block_literal_global.897
+ ___block_literal_global.899
+ ___block_literal_global.903
+ ___block_literal_global.905
+ ___block_literal_global.909
+ ___block_literal_global.911
+ ___block_literal_global.915
+ ___block_literal_global.917
+ ___block_literal_global.925
+ ___block_literal_global.929
+ ___setApplicationBadge_block_invoke.201
+ _kCAFilterInputSourceSublayerName
+ _kCAFilterVariableBlur
+ _kSBSMenuBarServiceMessageKeyMenuBarSupported
+ _objc_msgSend$_backgroundTaskIdentifierForUpdate:
+ _objc_msgSend$_batteryDomainData
+ _objc_msgSend$_canShowSolariumCursiveAnimation
+ _objc_msgSend$_dismissMenuBarAnimated:
+ _objc_msgSend$_dismissMenuBarAnimated:withCompletion:
+ _objc_msgSend$_handleMenuBarServiceClientMessageTypeQuerySupported:fromClient:
+ _objc_msgSend$_hasNonCursiveSuppressingUI
+ _objc_msgSend$_hasSuppressingUI
+ _objc_msgSend$_hitTestInMenuBarContentWithPoint:gestureWindow:
+ _objc_msgSend$_isBGSystemTaskUpdate:
+ _objc_msgSend$_performUpdateMenuBarVisibilityResponse:
+ _objc_msgSend$_postBannerWithAlert:
+ _objc_msgSend$_queryMenuBarSupportedForClient:withCompletion:
+ _objc_msgSend$_roundedCropsCornerRadius
+ _objc_msgSend$_secondaryTextColorForStyle
+ _objc_msgSend$_secondaryTextForStyle
+ _objc_msgSend$_setCoverSheetPresented:forcePresented:animated:dismissModalPresentation:options:withCompletion:
+ _objc_msgSend$_setLowPowerMode:
+ _objc_msgSend$_setMenuBarVisible:animated:
+ _objc_msgSend$_submitTaskRequestForUpdate:
+ _objc_msgSend$_toggleLowPowerMode
+ _objc_msgSend$_updateHelloVisibility
+ _objc_msgSend$_updateMenuBarVisibilityWithRequestedVisibility:
+ _objc_msgSend$_updateWindowControlsAdaptiveStyle
+ _objc_msgSend$addWallpaperUnlockProgressObserver:
+ _objc_msgSend$alertPresentationFailed:
+ _objc_msgSend$alwaysVisibleOnExternalDisplay
+ _objc_msgSend$applicationSceneViewController:didRequestWindowControlsAdaptiveStyle:adaptive:
+ _objc_msgSend$backgroundBlurContentOverhang
+ _objc_msgSend$captureView:
+ _objc_msgSend$deregisterTaskWithIdentifier:
+ _objc_msgSend$desiredBlurWidth
+ _objc_msgSend$dismissAnimated:alongsideAnimations:completion:
+ _objc_msgSend$dismissModalPresentationAnimated:completion:
+ _objc_msgSend$entryAnimationDamping
+ _objc_msgSend$entryAnimationDuration
+ _objc_msgSend$entryAnimationMass
+ _objc_msgSend$entryAnimationStiffness
+ _objc_msgSend$exitAnimationDamping
+ _objc_msgSend$exitAnimationDuration
+ _objc_msgSend$exitAnimationMass
+ _objc_msgSend$exitAnimationStiffness
+ _objc_msgSend$frameForContentViewForContainerBounds:
+ _objc_msgSend$hasOpaqueContents
+ _objc_msgSend$hiddenRestorableFileStackIcons
+ _objc_msgSend$initWithBounds:fixedSize:screenScale:supportsOrthogonalSizes:windowingConfiguration:allowsLetterboxing:
+ _objc_msgSend$initWithMainDisplayConfiguration:maximumPortraitSize:cornerRadiusConfiguration:
+ _objc_msgSend$initWithScene:delegate:animateInitialPresentation:loadCompletion:
+ _objc_msgSend$initWithTransitionID:selectedAppLayout:selectedLayoutRole:
+ _objc_msgSend$intersectedDisplayRectCorners
+ _objc_msgSend$isMenuBarSupported
+ _objc_msgSend$isShowingModalView
+ _objc_msgSend$isWaiting
+ _objc_msgSend$itemsCrossingToOtherDisplay
+ _objc_msgSend$lastPublishedData
+ _objc_msgSend$latchingAxesForHoveredEdge:
+ _objc_msgSend$menu
+ _objc_msgSend$menuBarStatusBar
+ _objc_msgSend$onlySupportsOneOrientation
+ _objc_msgSend$performWithSender:target:
+ _objc_msgSend$preferredComponentViewSizeDidInvalidateForLayoutSpecifier:
+ _objc_msgSend$prepareBackgroundUpdateTask:
+ _objc_msgSend$presentFallbackAlert:
+ _objc_msgSend$registerForTaskWithIdentifier:usingQueue:launchHandler:
+ _objc_msgSend$requestMenuBarVisibility:
+ _objc_msgSend$roundedCropsCornerRadius
+ _objc_msgSend$secondaryContent
+ _objc_msgSend$selectedDisplayItem
+ _objc_msgSend$setBackgroundTextureDataSource:
+ _objc_msgSend$setContentsCenter:
+ _objc_msgSend$setCoverSheetPresented:animated:dismissModalPresentation:withCompletion:
+ _objc_msgSend$setForcesEdgeAntialiasing:
+ _objc_msgSend$setIntersectedDisplayRectCorners:
+ _objc_msgSend$setInterval:
+ _objc_msgSend$setInvolvedProcesses:
+ _objc_msgSend$setItemsCrossingToOtherDisplay:
+ _objc_msgSend$setLatchingAxes:
+ _objc_msgSend$setMinDurationBetweenInstances:
+ _objc_msgSend$setOnReadyBlock:
+ _objc_msgSend$setRequiresBuddyComplete:
+ _objc_msgSend$setRequiresExternalPower:
+ _objc_msgSend$setRequiresNetworkConnectivity:
+ _objc_msgSend$setResourceIntensive:
+ _objc_msgSend$setResources:
+ _objc_msgSend$setScheduleAfter:
+ _objc_msgSend$setStageCornerRadiusSettings:
+ _objc_msgSend$setStripOffscreenPadding:
+ _objc_msgSend$setTrySchedulingBefore:
+ _objc_msgSend$setUnlockProgress:
+ _objc_msgSend$setVariableBlurNeeded:
+ _objc_msgSend$sharedScheduler
+ _objc_msgSend$shouldDisableDockSpecular
+ _objc_msgSend$shouldDisableFolderSpecular
+ _objc_msgSend$shouldDisableGlassDock
+ _objc_msgSend$shouldDisableMenusForAppRestrictionForViewController:
+ _objc_msgSend$shouldDisableParallax
+ _objc_msgSend$shouldDisableSpecularEverywhere
+ _objc_msgSend$shouldDisableSpecularEverywhereUsingLSSAssertion
+ _objc_msgSend$shouldDisableWidgetSpecular
+ _objc_msgSend$shouldExcludeAllClearGlassShadows
+ _objc_msgSend$shouldExcludeDockShadow
+ _objc_msgSend$shouldExcludeSearchShadow
+ _objc_msgSend$shouldRenderBackgroundTexture:
+ _objc_msgSend$shouldUseFlatIconsEverywhere
+ _objc_msgSend$stageCornerRadiusSettings
+ _objc_msgSend$stringForPresentationState:
+ _objc_msgSend$stripOffscreenPadding
+ _objc_msgSend$submitTaskRequest:error:
+ _objc_msgSend$swipeToRevealMenuBarGesturesEnabled
+ _objc_msgSend$switcherContentControllerWantsToUpdateMenuBarVisibility:
+ _objc_msgSend$systemServiceServer:queryMenuBarSupportedForClient:withCompletion:
+ _objc_msgSend$trailingLowBatteryStyleIconPackageView
+ _objc_msgSend$undimmedPasscodeLockViewForUsersCurrentStyle
+ _objc_msgSend$updateAdaptiveStyle:adaptive:
+ _objc_msgSend$updateBackgroundGlassEffectForDraggingProgress:
+ _objc_msgSend$updateCoverSheetDraggingProgress:forPresentationValue:
+ _objc_msgSend$updateMenuBarVisibility
+ _objc_msgSend$updateWindowControlsAdaptiveStyle:adaptive:
+ _objc_msgSend$variableBlurNeeded
+ _objc_msgSend$wallpaperWindow
- +[SBKeyboardFocusLockReason keyShortcutHUD]
- -[SBAbstractWindowSceneDelegate _handleKeyShortcutHUDVisibilityDidDismiss]
- -[SBAbstractWindowSceneDelegate _handleKeyShortcutHUDVisibilityDidPresent]
- -[SBAbstractWindowSceneDelegate zStackParticipant:updatePreferences:]
- -[SBAbstractWindowSceneDelegate zStackParticipantDidChange:]
- -[SBCoverSheetPresentationManager _setCoverSheetPresented:forcePresented:animated:options:withCompletion:]
- -[SBCoverSheetPrimarySlidingViewController _frameForContentViewForContainerBounds:]
- -[SBCoverSheetSlidingViewController _beginTransitionFromAppeared:].cold.1
- -[SBCoverSheetSlidingViewController _endTransitionToAppeared:].cold.1
- -[SBCoverSheetSlidingViewController _frameForContentViewForContainerBounds:]
- -[SBCoverSheetSlidingViewController setCompletionBlock:].cold.1
- -[SBCoverSheetSlidingViewController setCompletionBlock:].cold.2
- -[SBFlexibleWindowingHomeGestureSwitcherModifier cornerRadiiForIndex:]
- -[SBItemResizeTransitionSwitcherModifier initWithTransitionID:selectedAppLayout:]
- -[SBMainWorkspace _handleKeyShortcutHUDVisibilityDidDismiss]
- -[SBMainWorkspace _handleKeyShortcutHUDVisibilityDidPresent:]
- -[SBMenuBarManager _dismissMenuBarWithCompletion:]
- -[SBMenuBarManager _dismissMenuBar]
- -[SBMenuBarViewController dismissAlongsideAnimations:completion:]
- -[SBMenuBarViewController gradientContainerView]
- -[SBMenuBarViewController initWithScene:delegate:loadCompletion:]
- -[SBMenuBarViewController setGradientContainerView:]
- -[SBPosterBoardUpdateManager _criteriaForUpdate:]
- -[SBPosterBoardUpdateManager _criteriaForUpdate:].cold.1
- -[SBPosterBoardUpdateManager _isXPCActivity:]
- -[SBPosterBoardUpdateManager _xpcActivityNameForUpdate:]
- -[SBPosterBoardUpdateManager _xpcActivityNameForUpdate:].cold.1
- -[SBPosterBoardUpdateManager _xpcActivityNameForUpdate:].cold.2
- -[SBPowerAlertElement _leadingTextForStyle:]
- -[SBSwitcherController windowControlsViewControllerDidRequestMoveToDisplay:]
- -[SBTopAffordanceViewController windowControlsViewControllerDidRequestMoveToDisplay:]
- -[_SBDisplayItemFixedAspectGrid initWithBounds:fixedSize:screenScale:supportsOrthogonalSizes:windowingConfiguration:]
- GCC_except_table159
- GCC_except_table171
- GCC_except_table181
- GCC_except_table190
- GCC_except_table319
- GCC_except_table371
- GCC_except_table399
- GCC_except_table527
- GCC_except_table807
- GCC_except_table847
- GCC_except_table856
- GCC_except_table898
- GCC_except_table937
- _OBJC_CLASS_$_UIKeyShortcutHUDService
- _OBJC_IVAR_$_SBAbstractWindowSceneDelegate._keyShortcutHUDZStackParticipant
- _OBJC_IVAR_$_SBMainWorkspace._lockKeyboardFocusAssertion
- _OBJC_IVAR_$_SBMenuBarViewController._gradientContainerView
- _UIKeyShortcutHUDDidDismissNotification
- _UIKeyShortcutHUDDidPresentNotification
- _XPC_ACTIVITY_ALLOW_BATTERY
- _XPC_ACTIVITY_CHECK_IN
- _XPC_ACTIVITY_DELAY
- _XPC_ACTIVITY_DISK_INTENSIVE
- _XPC_ACTIVITY_DUET_RELATED_APPLICATIONS
- _XPC_ACTIVITY_EXPECTED_DURATION
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_GROUP_CONCURRENCY_LIMIT
- _XPC_ACTIVITY_GROUP_NAME
- _XPC_ACTIVITY_INTERVAL_1_DAY
- _XPC_ACTIVITY_INTERVAL_5_MIN
- _XPC_ACTIVITY_INVOLVED_PROCESSES
- _XPC_ACTIVITY_MEMORY_INTENSIVE
- _XPC_ACTIVITY_POST_INSTALL
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_UTILITY
- _XPC_ACTIVITY_REPEATING
- _XPC_ACTIVITY_REQUIRES_CLASS_C
- _XPC_ACTIVITY_REQUIRE_SCREEN_SLEEP
- _XPC_ACTIVITY_RUN_WHEN_APP_FOREGROUNDED
- ___106-[SBCoverSheetPresentationManager _setCoverSheetPresented:forcePresented:animated:options:withCompletion:]_block_invoke
- ___106-[SBSystemApertureSceneElement contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:]_block_invoke.244
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.303
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.304
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.305
- ___113-[SBFluidSwitcherViewController initWithPersonality:liveContentOverlayCoordinator:dataSource:delegate:debugName:]_block_invoke.198
- ___116-[SBAssistantSession presentSiriPresentationViewController:withAnimationFactory:siriPresentationOptions:completion:]_block_invoke.80
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.642
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.644
- ___138-[SBCoverSheetSlidingViewController _finishTransitionToPresented:forcingTransition:ignoringPreflightRequirements:animated:withCompletion:]_block_invoke.107
- ___138-[SBCoverSheetSlidingViewController _finishTransitionToPresented:forcingTransition:ignoringPreflightRequirements:animated:withCompletion:]_block_invoke.99
- ___138-[SBCoverSheetSlidingViewController _finishTransitionToPresented:forcingTransition:ignoringPreflightRequirements:animated:withCompletion:]_block_invoke.99.cold.1
- ___138-[SBCoverSheetSlidingViewController _finishTransitionToPresented:forcingTransition:ignoringPreflightRequirements:animated:withCompletion:]_block_invoke.cold.1
- ___38-[SBMenuBarManager setMenuBarVisible:]_block_invoke
- ___38-[SBMenuBarManager setMenuBarVisible:]_block_invoke_2
- ___38-[SBMenuBarManager setMenuBarVisible:]_block_invoke_3
- ___38-[SBMenuBarManager setMenuBarVisible:]_block_invoke_4
- ___42-[SBLowPowerAlertItem _enableLowPowerMode]_block_invoke
- ___44-[SBPosterBoardUpdateManager executeUpdate:]_block_invoke.5
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1206
- ___50-[SBMenuBarManager _dismissMenuBarWithCompletion:]_block_invoke
- ___50-[SBMenuBarManager _dismissMenuBarWithCompletion:]_block_invoke_2
- ___50-[SBMenuBarManager _dismissMenuBarWithCompletion:]_block_invoke_3
- ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.81
- ___51-[SBStatusBarStateAggregator _updateTetheringState]_block_invoke.229
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.747
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.778
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.809
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.915
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.802
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.919
- ___55-[SBFluidSwitcherViewController _ensureSubviewOrdering]_block_invoke.750
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke.94
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_10.110
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_11.111
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_12.113
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_13.114
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_14.115
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_15.117
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_16.118
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_17.119
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_18.122
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_19.124
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_2.97
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_3.99
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_4.100
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_5.103
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_6.105
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_7.106
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_8.107
- ___55-[SBStatusBarStateAggregator _registerForNotifications]_block_invoke_9.109
- ___56-[SBAssistantController _updateControlWidgetEligibility]_block_invoke.262
- ___56-[SBCaptureHardwareButtonAppActivator _launchCaptureApp]_block_invoke.191
- ___56-[SBCaptureHardwareButtonAppActivator _launchCaptureApp]_block_invoke.193
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1748
- ___57-[SBActivityBannerObserver _handleActivityAlert:present:]_block_invoke
- ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.505
- ___57-[SBMainWorkspace applicationProcessDidExit:withContext:]_block_invoke.512
- ___59-[SBFloatingDockRemoteContentManager iconView:performDrop:]_block_invoke.68
- ___59-[SBFloatingDockRemoteContentManager iconView:performDrop:]_block_invoke.70
- ___60-[SBMainWorkspace _preflightTransitionRequest:forExecution:]_block_invoke.380
- ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.924
- ___61-[SBFloatingDockRemoteContentManager setOpenedFileStackIcon:]_block_invoke
- ___62-[SBContinuousExposeAppToAppModifier didMoveToParentModifier:]_block_invoke
- ___64-[SBActivityManager _activityStartedOrUpdatedWithContentUpdate:]_block_invoke.43
- ___64-[SBAssistantController alwaysOnLiveRenderingAssertionRequested]_block_invoke.206
- ___65-[SBMenuBarViewController dismissAlongsideAnimations:completion:]_block_invoke
- ___66-[SBAssistantSession presentSiriEffectsViewController:completion:]_block_invoke.98
- ___68-[SBContinuousExposeAppToAppModifier fadeInDelayForSplitViewHandles]_block_invoke
- ___68-[SBCoverSheetSlidingViewController _updateForLocation:interactive:]_block_invoke.123
- ___68-[SBCoverSheetSlidingViewController _updateForLocation:interactive:]_block_invoke.123.cold.1
- ___69-[SBDashBoardEmergencyDialerViewController _updateEmergencyCallMode:]_block_invoke.27
- ___70-[SBFlexibleWindowingHomeGestureSwitcherModifier cornerRadiiForIndex:]_block_invoke
- ___71-[SBAssistantController siriPresentation:requestsPunchout:withHandler:]_block_invoke.225
- ___71-[SBAssistantController siriPresentation:requestsPunchout:withHandler:]_block_invoke.230
- ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1068
- ___78-[SBDashBoardEmergencyDialerViewController _activateEmergencyDialerController]_block_invoke.23
- ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke.121
- ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_2.123
- ___79-[SBMainWorkspace _removeApplicationEntities:withDestructionIntent:completion:]_block_invoke.472
- ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.358
- ___83-[SBAssistantController siriPresentation:requestsDismissalWithOptions:withHandler:]_block_invoke.219
- ___83-[SBCoverSheetSlidingViewController _performAppFlyInToPresented:animated:velocity:]_block_invoke.108
- ___83-[SBCoverSheetSlidingViewController _performAppFlyInToPresented:animated:velocity:]_block_invoke.108.cold.1
- ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke.45
- ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke_2.46
- ___86-[SBAssistantController siriPresentation:requestsPresentationWithOptions:withHandler:]_block_invoke.218
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.361
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.362
- ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.77
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1600
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1602
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1604
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1608
- ___91-[SBStatusBarStateAggregator _updateCallingBackgroundActivityAssertionsForCallDescriptors:]_block_invoke.238
- ___91-[SBStatusBarStateAggregator _updateCallingBackgroundActivityAssertionsForCallDescriptors:]_block_invoke.238.cold.1
- ___94-[SBAssistantController siriPresentation:requestsDismissalOfEffectsViewControllerWithHandler:]_block_invoke.217
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.645
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.667
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.682
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.686
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.694
- ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke.210
- ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke.214
- ___95-[SBStatusBarStateAggregator _updateBackgroundActivityAssertionsForSystemStatusDomain:andData:]_block_invoke_2.215
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1731
- ___98-[SBAssistantController siriPresentation:requestsPresentationOfEffectsViewController:withHandler:]_block_invoke.212
- ___SetDisplayShowsProgress_block_invoke.93
- ___SetDisplayShowsProgress_block_invoke.94
- ___SetDisplayShowsProgress_block_invoke.95
- ____SBXXAcquireFocusPreventingFullScreenPresentationAssertion_block_invoke.180
- ____SBXXAddWallpaperAnimationSuspensionAssertion_block_invoke.169
- ____SBXXSetAllApplicationsShowSyncIndicator_block_invoke.103
- ____SBXXSetShowsOverridesForRecording_block_invoke.107
- ____SBXXSetWallpaperImageSurfaceForLocations_block_invoke.163
- ___block_descriptor_48_e8_32s40bs_e31_v24?0"ACAccount"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e36_v16?0"_UIMainMenuSessionResponse"8lw40l8s32l8
- ___block_descriptor_48_e8_32s_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8
- ___block_descriptor_72_e8_32r40r48r56r64r_e5_v8?0lr32l8r40l8r48l8r56l8r64l8
- ___block_descriptor_73_e8_32s40s48s56s64w_e8_v12?0B8lw64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_96_e8_32s40r_e61_v32?0"SBDisplayItem"8"SBDisplayItemLayoutAttributes"16^B24ls32l8r40l8
- ___block_literal_global.1052
- ___block_literal_global.1061
- ___block_literal_global.107
- ___block_literal_global.1081
- ___block_literal_global.1097
- ___block_literal_global.1149
- ___block_literal_global.1152
- ___block_literal_global.1157
- ___block_literal_global.1163
- ___block_literal_global.117
- ___block_literal_global.1199
- ___block_literal_global.1247
- ___block_literal_global.141
- ___block_literal_global.143
- ___block_literal_global.1453
- ___block_literal_global.150
- ___block_literal_global.1574
- ___block_literal_global.1578
- ___block_literal_global.1610
- ___block_literal_global.1619
- ___block_literal_global.1621
- ___block_literal_global.1623
- ___block_literal_global.1625
- ___block_literal_global.1641
- ___block_literal_global.1757
- ___block_literal_global.1780
- ___block_literal_global.1789
- ___block_literal_global.1805
- ___block_literal_global.182
- ___block_literal_global.209
- ___block_literal_global.213
- ___block_literal_global.264
- ___block_literal_global.311
- ___block_literal_global.320
- ___block_literal_global.326
- ___block_literal_global.336
- ___block_literal_global.338
- ___block_literal_global.347
- ___block_literal_global.354
- ___block_literal_global.357
- ___block_literal_global.380
- ___block_literal_global.475
- ___block_literal_global.482
- ___block_literal_global.486
- ___block_literal_global.491
- ___block_literal_global.492
- ___block_literal_global.495
- ___block_literal_global.537
- ___block_literal_global.578
- ___block_literal_global.587
- ___block_literal_global.619
- ___block_literal_global.630
- ___block_literal_global.647
- ___block_literal_global.654
- ___block_literal_global.656
- ___block_literal_global.661
- ___block_literal_global.677
- ___block_literal_global.683
- ___block_literal_global.697
- ___block_literal_global.723
- ___block_literal_global.771
- ___block_literal_global.806
- ___block_literal_global.808
- ___block_literal_global.810
- ___block_literal_global.817
- ___block_literal_global.819
- ___block_literal_global.832
- ___block_literal_global.842
- ___block_literal_global.873
- ___block_literal_global.878
- ___block_literal_global.882
- ___block_literal_global.884
- ___block_literal_global.888
- ___block_literal_global.890
- ___block_literal_global.894
- ___block_literal_global.896
- ___block_literal_global.900
- ___block_literal_global.902
- ___block_literal_global.906
- ___block_literal_global.908
- ___block_literal_global.912
- ___block_literal_global.914
- ___block_literal_global.918
- ___block_literal_global.926
- ___setApplicationBadge_block_invoke.195
- _objc_msgSend$_criteriaForUpdate:
- _objc_msgSend$_dismissMenuBar
- _objc_msgSend$_dismissMenuBarWithCompletion:
- _objc_msgSend$_frameForContentViewForContainerBounds:
- _objc_msgSend$_isXPCActivity:
- _objc_msgSend$_leadingTextForStyle:
- _objc_msgSend$_setCoverSheetPresented:forcePresented:animated:options:withCompletion:
- _objc_msgSend$_xpcActivityNameForUpdate:
- _objc_msgSend$dismissAlongsideAnimations:completion:
- _objc_msgSend$dismissOrCancelHUDPresentationIfNeeded
- _objc_msgSend$initWithBounds:fixedSize:screenScale:supportsOrthogonalSizes:windowingConfiguration:
- _objc_msgSend$initWithScene:delegate:loadCompletion:
- _objc_msgSend$initWithTransitionID:selectedAppLayout:
- _objc_msgSend$isCongruent
- _objc_msgSend$keyShortcutHUD
- _objc_msgSend$passcodeLockViewForUsersCurrentStyle
- _objc_msgSend$secureWindowVisibilityDidChange:
- _objc_msgSend$sharedHUDService
- _objc_msgSend$updateCoverSheetDraggingProgress:
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_set_criteria
- _xpc_activity_unregister
- _xpc_array_create
- _xpc_dictionary_set_double
- _xpc_string_create
CStrings:
+ "-[SBCoverSheetPresentationManager _cleanupPresentationTransition]"
+ "-[SBCoverSheetPresentationManager _prepareForPresentationTransition]"
+ "-[SBCoverSheetSlidingViewController _beginTransitionFromAppeared: %{BOOL}d]"
+ "-[SBCoverSheetSlidingViewController _endTransitionToAppeared: %{BOOL}d]"
+ "-[SBLockScreenManager lockScreenViewControllerDidDismiss]"
+ "-[SBLockScreenManager lockScreenViewControllerDidPresent]"
+ "-[SBLockScreenManager lockScreenViewControllerWillDismissWithVelocity:]"
+ "-[SBLockScreenManager lockScreenViewControllerWillPresent]"
+ "@\"<SBMenuBarBackgroundVariableBlurViewDelegate>\""
+ "@\"NSSet\"32@0:8@\"RBSProcessIdentity\"16@\"BSAuditToken\"24"
+ "@\"NSString\"24@0:8@\"<_UISceneMainMenuProviding>\"16"
+ "@\"SASCaptureSessionTextureDataSource\""
+ "@\"SBIcon\"32@0:8@\"APUISuggestionsWidgetViewController\"16@\"NSString\"24"
+ "@\"SBMenuBarBackgroundVariableBlurView\""
+ "@\"STBatteryStatusDomainData\""
+ "@\"UISSceneHostingExternalSettingsModifierService\""
+ "@\"UIWindowScene\"24@0:8@\"SBHIconManager\"16"
+ "@44@0:8@16@24B32@?36"
+ "@52@0:8@16Q24d32B40@?44"
+ "@88@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48d64B72@76B84"
+ "APUISuggestionsWidgetViewControllerDelegate"
+ "Always Visible on External Display"
+ "B16@?0@\"FBApplicationProcess\"8"
+ "B24@0:8@\"SBMenuBarViewController\"16"
+ "BATTERY_PERCENTAGE"
+ "Background Blur Content Overhang"
+ "Bailed on Bookend presentation"
+ "Created %@ completionBlock %p"
+ "Entry Animation Duration"
+ "Entry Animation Spring Damping"
+ "Entry Animation Spring Mass"
+ "Entry Animation Spring Stiffnes"
+ "Entry/Exit Animation Spring Constants"
+ "Exit Animation Duration"
+ "Exit Animation Spring Damping"
+ "Exit Animation Spring Mass"
+ "Exit Animation Spring Stiffnes"
+ "Failed to submit Posters prewarm task with error: %{public}@"
+ "Home Screen default set"
+ "Invalid bookend window"
+ "LOW_BATT_SUBTITLE_LOW_POWER_MODE_DISABLED"
+ "LOW_BATT_SUBTITLE_LOW_POWER_MODE_ENABLED"
+ "Low battery alert user interaction"
+ "SBCoverSheetSlidingViewController completionBlock %p cancelled"
+ "SBCoverSheetSlidingViewController completionBlock %p saved"
+ "SBCoverSheetSlidingViewController transitioning to presentation state %@"
+ "SBMenuBarBackgroundVariableBlurView"
+ "SBMenuBarBackgroundVariableBlurViewDelegate"
+ "SBSceneHostingExternalSettingsModifierServiceDelegate"
+ "SBSceneHostingExternalSettingsModifierServiceSingleton"
+ "SBSystemStatusBatteryDataProviderDidChangeNotification"
+ "SBUpdateMenuBarVisibilitySwitcherEventResponse"
+ "SBWindowControlsControlling"
+ "SBWorkspaceTerminateProcesses: %@; reason = \"%@\"; description = \"%@\""
+ "SINGLE_APP_MENU_TITLE"
+ "Set low power mode"
+ "Setting Texure based data source"
+ "Setting bookend window for projection"
+ "Stage Corner Radius Settings"
+ "Submitted Posters prewarm task with error: %{public}@"
+ "T@\"<SBMenuBarBackgroundVariableBlurViewDelegate>\",R,W,N,V_delegate"
+ "T@\"BSUICAPackageView\",&,N,V_trailingLowBatteryStyleIconPackageView"
+ "T@\"NSMutableArray\",&,N,V_hiddenRestorableFileStackIcons"
+ "T@\"NSSet\",C,N,V_itemsCrossingToOtherDisplay"
+ "T@\"SBFFluidBehaviorSettings\",&,V_stageCornerRadiusSettings"
+ "T@\"SBMenuBarBackgroundVariableBlurView\",&,N,V_variableBlurView"
+ "T@\"SBUISystemApertureTextContentProvider\",&,N,V_secondaryContent"
+ "T@\"STBatteryStatusDomainData\",R,N,V_lastPublishedData"
+ "T@\"UIView\",&,N,V_backgroundEffectContainerView"
+ "T@?,C,N,V_action"
+ "TB,N,V_alwaysVisibleOnExternalDisplay"
+ "TB,N,V_variableBlurNeeded"
+ "TB,R,N,GisMenuBarSupported"
+ "TQ,N,V_intersectedDisplayRectCorners"
+ "Td,N,V_backgroundBlurContentOverhang"
+ "Td,N,V_entryAnimationDamping"
+ "Td,N,V_entryAnimationDuration"
+ "Td,N,V_entryAnimationMass"
+ "Td,N,V_entryAnimationStiffness"
+ "Td,N,V_exitAnimationDamping"
+ "Td,N,V_exitAnimationDuration"
+ "Td,N,V_exitAnimationMass"
+ "Td,N,V_exitAnimationStiffness"
+ "Td,N,V_stripOffscreenPadding"
+ "Td,N,V_trailingIndicatorAnimationViewVelocityY"
+ "Td,N,V_trailingIndicatorTransitionViewVelocityY"
+ "Transitioning from capture extension [%{public}@] to application [%{public}@] failed."
+ "Transitioning from capture extension [%{public}@] to application [%{public}@] succeeded."
+ "UISSceneHostingExternalSettingsModifierServiceDelegate"
+ "UpdateMenuBarVisibility"
+ "Using fallback battery data until first update from SystemStatus"
+ "[ActivityID: %{public}@] alert presentation failed for original destination. Looking for fallback destination."
+ "[ActivityID: %{public}@] posting banner as fallback alert"
+ "[ActivityID: %{public}@] posting fallback alert"
+ "[Solarium Cursive Check] Activation locked"
+ "[Solarium Cursive Check] Feature not enabled"
+ "[Solarium Cursive Check] In Store Mode (Do Not Buy)"
+ "[self _isBGSystemTaskUpdate:update]"
+ "_allowsLetterboxing"
+ "_alwaysVisibleOnExternalDisplay"
+ "_animateInitialPresentation"
+ "_backgroundBlurContentOverhang"
+ "_backgroundEffectContainerView"
+ "_backgroundTaskIdentifierForUpdate:"
+ "_batteryDomainData"
+ "_canShowSolariumCursiveAnimation"
+ "_defaultGainMapDefeatingLayer"
+ "_disableSpecularsForHomeScreenDefaultAssertion"
+ "_dismissMenuBarAnimated:"
+ "_dismissMenuBarAnimated:withCompletion:"
+ "_displayItemsChangingPosition"
+ "_entryAnimationDamping"
+ "_entryAnimationDuration"
+ "_entryAnimationMass"
+ "_entryAnimationStiffness"
+ "_exitAnimationDamping"
+ "_exitAnimationDuration"
+ "_exitAnimationMass"
+ "_exitAnimationStiffness"
+ "_externalSettingsModifierService"
+ "_glassTextureDataSource"
+ "_gradientMaskLayer"
+ "_handleMenuBarServiceClientMessageTypeQuerySupported:fromClient:"
+ "_hasNonCursiveSuppressingUI"
+ "_hasReceivedBatteryDataFromSystemStatus"
+ "_hasSuppressingUI"
+ "_hiddenRestorableFileStackIcons"
+ "_hitTestInMenuBarContentWithPoint:gestureWindow:"
+ "_intersectedDisplayRectCorners"
+ "_isBGSystemTaskUpdate:"
+ "_isFromPeek"
+ "_itemsCrossingToOtherDisplay"
+ "_lastPublishedData"
+ "_performUpdateMenuBarVisibilityResponse:"
+ "_postBannerWithAlert:"
+ "_queryMenuBarSupportedForClient:withCompletion:"
+ "_roundedCropsCornerRadius"
+ "_secondaryContent"
+ "_secondaryTextColorForStyle"
+ "_secondaryTextForStyle"
+ "_setCoverSheetPresented:forcePresented:animated:dismissModalPresentation:options:withCompletion:"
+ "_setLowPowerMode:"
+ "_setMenuBarVisible:animated:"
+ "_stageCornerRadiusSettings"
+ "_stripOffscreenPadding"
+ "_submitTaskRequestForUpdate:"
+ "_toggleLowPowerMode"
+ "_trailingIndicatorAnimationViewVelocityY"
+ "_trailingIndicatorTransitionViewVelocityY"
+ "_trailingLowBatteryStyleIconPackageView"
+ "_updateHelloVisibility"
+ "_updateLowPowerMode"
+ "_updateMenuBarVisibilityWithRequestedVisibility:"
+ "_updateWindowControlsAdaptiveStyle"
+ "_variableBlurNeeded"
+ "alertPresentationFailed:"
+ "alwaysVisibleOnExternalDisplay"
+ "animation trailing velocity updated: %.2f"
+ "applicationSceneViewController:didRequestWindowControlsAdaptiveStyle:adaptive:"
+ "backgroundBlurContentOverhang"
+ "backgroundEffectContainerView"
+ "captureView:"
+ "coverSheetViewControllerDidPresentPasscodeLockView:"
+ "deregisterTaskWithIdentifier:"
+ "desiredBlurWidth"
+ "dismissAnimated:alongsideAnimations:completion:"
+ "dismissModalPresentationAnimated:completion:"
+ "entryAnimationDamping"
+ "entryAnimationDuration"
+ "entryAnimationMass"
+ "entryAnimationStiffness"
+ "exitAnimationDamping"
+ "exitAnimationDuration"
+ "exitAnimationMass"
+ "exitAnimationStiffness"
+ "failed to fetch apple account"
+ "frameForContentViewForContainerBounds:"
+ "gradientMask"
+ "handleInstalledAppsDidChange:"
+ "hiddenRestorableFileStackIcons"
+ "initWithBounds:fixedSize:screenScale:supportsOrthogonalSizes:windowingConfiguration:allowsLetterboxing:"
+ "initWithMainDisplayConfiguration:maximumPortraitSize:cornerRadiusConfiguration:"
+ "initWithScene:delegate:animateInitialPresentation:loadCompletion:"
+ "initWithTransitionID:selectedAppLayout:selectedLayoutRole:"
+ "intersectedDisplayRectCorners"
+ "is a child, loading account"
+ "isMenuBarSupported"
+ "isShowingModalView"
+ "isWaiting"
+ "itemsCrossingToOtherDisplay"
+ "lastPublishedData"
+ "latchingAxesForHoveredEdge:"
+ "layout update isn't a sufficient reason to switch the focused window scene to %{public}@"
+ "lowbattery"
+ "lpm"
+ "lpm-asset-v1"
+ "menuBarSupported"
+ "menuBarVariableBlurGradient"
+ "not a child, bailing"
+ "onlySupportsOneOrientation"
+ "overrideClientNameForMainMenu:"
+ "performWithSender:target:"
+ "preferredComponentViewSizeDidInvalidateForLayoutSpecifier:"
+ "prepareBackgroundUpdateTask:"
+ "presentFallbackAlert:"
+ "primaryWindowSceneForIconManager:"
+ "q!\xa1"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "requestMenuBarVisibility:"
+ "roundedCropsCornerRadius"
+ "secondaryContent"
+ "setAlwaysVisibleOnExternalDisplay:"
+ "setBackgroundBlurContentOverhang:"
+ "setBackgroundEffectContainerView:"
+ "setBackgroundTextureDataSource:"
+ "setContentsCenter:"
+ "setCoverSheetPresented:animated:dismissModalPresentation:withCompletion:"
+ "setEntryAnimationDamping:"
+ "setEntryAnimationDuration:"
+ "setEntryAnimationMass:"
+ "setEntryAnimationStiffness:"
+ "setExitAnimationDamping:"
+ "setExitAnimationDuration:"
+ "setExitAnimationMass:"
+ "setExitAnimationStiffness:"
+ "setForcesEdgeAntialiasing:"
+ "setHiddenRestorableFileStackIcons:"
+ "setIntersectedDisplayRectCorners:"
+ "setInterval:"
+ "setInvolvedProcesses:"
+ "setItemsCrossingToOtherDisplay:"
+ "setLatchingAxes:"
+ "setMinDurationBetweenInstances:"
+ "setOnReadyBlock:"
+ "setRequiresBuddyComplete:"
+ "setRequiresExternalPower:"
+ "setRequiresNetworkConnectivity:"
+ "setResourceIntensive:"
+ "setResources:"
+ "setScheduleAfter:"
+ "setSecondaryContent:"
+ "setStageCornerRadiusSettings:"
+ "setStripOffscreenPadding:"
+ "setTrailingIndicatorAnimationViewVelocityY:"
+ "setTrailingIndicatorTransitionViewVelocityY:"
+ "setTrailingLowBatteryStyleIconPackageView:"
+ "setTrySchedulingBefore:"
+ "setUnlockProgress:"
+ "setVariableBlurNeeded:"
+ "settingsModifiersForClientProcessIdentity:hostedBy:"
+ "sharedScheduler"
+ "shouldDisableDockSpecular"
+ "shouldDisableFolderSpecular"
+ "shouldDisableGlassDock"
+ "shouldDisableMenusForAppRestrictionForViewController:"
+ "shouldDisableParallax"
+ "shouldDisableSpecularEverywhere"
+ "shouldDisableSpecularEverywhereUsingLSSAssertion"
+ "shouldDisableWidgetSpecular"
+ "shouldExcludeAllClearGlassShadows"
+ "shouldExcludeDockShadow"
+ "shouldExcludeSearchShadow"
+ "shouldRenderBackgroundTexture:"
+ "shouldUseFlatIconsEverywhere"
+ "stageCornerRadiusSettings"
+ "stripOffscreenPadding"
+ "submitTaskRequest:error:"
+ "suggestionsWidgetViewController:iconForApplicationWithBundleIdentifier:"
+ "swipeToRevealMenuBarGesturesEnabled"
+ "switcherContentControllerWantsToUpdateMenuBarVisibility:"
+ "systemServiceServer:queryMenuBarSupportedForClient:withCompletion:"
+ "trailingIndicatorAnimationViewVelocityY"
+ "trailingIndicatorTransitionViewVelocityY"
+ "trailingLowBatteryStyleIconPackageView"
+ "transition trailing velocity updated: %.2f"
+ "undimmedPasscodeLockViewForUsersCurrentStyle"
+ "updateAdaptiveStyle:adaptive:"
+ "updateBackgroundGlassEffectForDraggingProgress:"
+ "updateCoverSheetDraggingProgress:forPresentationValue:"
+ "updateMenuBarVisibility"
+ "updateWindowControlsAdaptiveStyle:adaptive:"
+ "v16@?0@\"BGSystemTask\"8"
+ "v16@?0@\"SASCaptureSessionTextureDataSource\"8"
+ "v36@0:8@\"SBDeviceApplicationSceneViewController\"16q24B32"
+ "v48@0:8B16B20B24B28Q32@?40"
+ "v80@0:8{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}}16"
+ "variableBlurNeeded"
+ "{?=\"switcherContentControllerBringAppLayoutToFront\"b1\"switcherContentControllerActivatedBestAppSuggestion\"b1\"updateUserInteractionEnabledForSwitcherContentController\"b1\"updateWindowVisibilityForSwitcherContentController\"b1\"switcherContentControllerSetHomeScreenScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenAlphaWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenDimmingAlphaWithSettingsAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurProgressWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurType\"b1\"switcherContentControllerSetHomeScreenBackdropBlurMaterialRecipeNameWithAnimationModeCompletion\"b1\"switcherContentControllerControlsWallpaper\"b1\"switcherContentControllerSetWallpaperScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetWallpaperStyle\"b1\"switcherContentControllerSetInterfaceOrientation\"b1\"switcherContentControllerSetInterfaceOrientationFromUserResizingForDisplayItem\"b1\"switcherContentControllerRequestNewWindowForBundleIdentifier\"b1\"switcherContentControllerSetContainerStatusBarHiddenPartsHiddenAnimationDuration\"b1\"switcherContentControllerWantsToDismissMenuBar\"b1\"switcherContentControllerWantsToPeekMenuBar\"b1\"switcherContentControllerWantsToUpdateMenuBarVisibility\"b1\"switcherContentControllerDemoLayoutAttributesForDisplayItem\"b1\"switcherContentControllerSetPointerInteractionsEnabled\"b1\"switcherContentControllerShouldResignActiveForStartOfTransition\"b1\"switcherContentControllerControlsHomeScreenContents\"b1\"switcherContentControllerSetCacheAsynchronousRenderingSurfaces\"b1\"cancelActiveGestureForSwitcherContentController\"b1\"switcherContentControllerReopenHiddenAppLayoutsWithBundleIdentifier\"b1\"switcherContentControllerLayoutStateTransitionDidEndWithTransitionContext\"b1\"switcherContentControllerTransformForCardUnderSheetForBoundsSize\"b1\"switcherContentControllerMoveDisplayItemFromOtherDisplay\"b1\"presentContinuousExposeStripRevealGrabberTongueImmediatelyForSwitcherContentController\"b1\"tickleContinuousExposeStripRevealGrabberTongueIfVisibleForSwitcherContentController\"b1\"switcherContentControllerDidUpdateVisibleHomeAffordances\"b1\"switcherContentControllerRemoveDisplayItemFromDesktop\"b1\"switcherContentControllerRequestDismissalForHomeScreenBackgroundTaps\"b1}"
+ "{CACornerRadii=\"minXMaxY\"{CGSize=\"width\"d\"height\"d}\"maxXMaxY\"{CGSize=\"width\"d\"height\"d}\"maxXMinY\"{CGSize=\"width\"d\"height\"d}\"minXMinY\"{CGSize=\"width\"d\"height\"d}}"
+ "\xc5S"
+ "\xf0\xf02"
+ "\xf0\xf0Q"
+ "\xf0\xf0\xc1"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb1"
- "@52@0:8@16Q24d32B40@44"
- "@84@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGSize=dd}48d64B72@76"
- "Enabling low power mode"
- "LOW_BATT_TITLE_COMPACT"
- "PosterBoardUpdate"
- "SBPosterBoardUpdateAppInstallOrUninstall is not implemented.  Please update PosterBoard."
- "T@\"UIView\",&,N,V_gradientContainerView"
- "Transtioning from capture extension [%{public}@] to application [%{public}@] failed."
- "Transtioning from capture extension [%{public}@] to application [%{public}@] succeeded."
- "[self _isXPCActivity:update]"
- "_beginTransitionFromAppeared: %{BOOL}d"
- "_criteriaForUpdate:"
- "_dismissMenuBar"
- "_dismissMenuBarWithCompletion:"
- "_endTransitionToAppeared: %{BOOL}d"
- "_frameForContentViewForContainerBounds:"
- "_gradientContainerView"
- "_handleKeyShortcutHUDVisibilityDidDismiss"
- "_handleKeyShortcutHUDVisibilityDidPresent"
- "_handleKeyShortcutHUDVisibilityDidPresent:"
- "_isXPCActivity:"
- "_keyShortcutHUDZStackParticipant"
- "_leadingTextForStyle:"
- "_prepareForPresentationTransition"
- "_setCoverSheetPresented:forcePresented:animated:options:withCompletion:"
- "_xpcActivityNameForUpdate:"
- "a!\xa1"
- "completionBlock %p Cancelled"
- "completionBlock %p Creation"
- "completionBlock %p Saved"
- "dismissAlongsideAnimations:completion:"
- "dismissOrCancelHUDPresentationIfNeeded"
- "gradientContainerView"
- "initWithBounds:fixedSize:screenScale:supportsOrthogonalSizes:windowingConfiguration:"
- "initWithScene:delegate:loadCompletion:"
- "initWithTransitionID:selectedAppLayout:"
- "isCongruent"
- "keyShortcutHUD"
- "passcodeLockViewForUsersCurrentStyle"
- "secureWindowVisibilityDidChange:"
- "setGradientContainerView:"
- "sharedHUDService"
- "updateCoverSheetDraggingProgress:"
- "v44@0:8B16B20B24Q28@?36"
- "windowControlsViewControllerDidRequestMoveToDisplay:"
- "{?=\"switcherContentControllerBringAppLayoutToFront\"b1\"switcherContentControllerActivatedBestAppSuggestion\"b1\"updateUserInteractionEnabledForSwitcherContentController\"b1\"updateWindowVisibilityForSwitcherContentController\"b1\"switcherContentControllerSetHomeScreenScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenAlphaWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenDimmingAlphaWithSettingsAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurProgressWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurType\"b1\"switcherContentControllerSetHomeScreenBackdropBlurMaterialRecipeNameWithAnimationModeCompletion\"b1\"switcherContentControllerControlsWallpaper\"b1\"switcherContentControllerSetWallpaperScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetWallpaperStyle\"b1\"switcherContentControllerSetInterfaceOrientation\"b1\"switcherContentControllerSetInterfaceOrientationFromUserResizingForDisplayItem\"b1\"switcherContentControllerRequestNewWindowForBundleIdentifier\"b1\"switcherContentControllerSetContainerStatusBarHiddenPartsHiddenAnimationDuration\"b1\"switcherContentControllerWantsToDismissMenuBar\"b1\"switcherContentControllerWantsToPeekMenuBar\"b1\"switcherContentControllerDemoLayoutAttributesForDisplayItem\"b1\"switcherContentControllerSetPointerInteractionsEnabled\"b1\"switcherContentControllerShouldResignActiveForStartOfTransition\"b1\"switcherContentControllerControlsHomeScreenContents\"b1\"switcherContentControllerSetCacheAsynchronousRenderingSurfaces\"b1\"cancelActiveGestureForSwitcherContentController\"b1\"switcherContentControllerReopenHiddenAppLayoutsWithBundleIdentifier\"b1\"switcherContentControllerLayoutStateTransitionDidEndWithTransitionContext\"b1\"switcherContentControllerTransformForCardUnderSheetForBoundsSize\"b1\"switcherContentControllerMoveDisplayItemFromOtherDisplay\"b1\"presentContinuousExposeStripRevealGrabberTongueImmediatelyForSwitcherContentController\"b1\"tickleContinuousExposeStripRevealGrabberTongueIfVisibleForSwitcherContentController\"b1\"switcherContentControllerDidUpdateVisibleHomeAffordances\"b1\"switcherContentControllerRemoveDisplayItemFromDesktop\"b1\"switcherContentControllerRequestDismissalForHomeScreenBackgroundTaps\"b1}"
- "\xc5R"
- "\xf0\xf0\""
- "\xf0\xf0A"
- "\xf0\xf0\xb1"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa1"

```
