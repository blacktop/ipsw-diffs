## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.0.10.114.0
-  __TEXT.__text: 0xa88254
-  __TEXT.__auth_stubs: 0x5570
+4557.1.8.105.0
+  __TEXT.__text: 0xa77c18
+  __TEXT.__auth_stubs: 0x5560
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb7b70
-  __TEXT.__const: 0x12fa0
-  __TEXT.__oslogstring: 0x5e54c
-  __TEXT.__cstring: 0x7ce29
-  __TEXT.__gcc_except_tab: 0x17898
-  __TEXT.__ustring: 0xcf4
+  __TEXT.__objc_methlist: 0xb7150
+  __TEXT.__const: 0x12e50
+  __TEXT.__oslogstring: 0x5e4d4
+  __TEXT.__cstring: 0x7cce2
+  __TEXT.__gcc_except_tab: 0x17ff0
+  __TEXT.__ustring: 0xd0a
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2c118
+  __TEXT.__unwind_info: 0x2c090
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x2211b
-  __TEXT.__objc_methname: 0x1cf260
-  __TEXT.__objc_methtype: 0x4c859
-  __TEXT.__objc_stubs: 0xf3ca0
-  __DATA_CONST.__got: 0xa140
-  __DATA_CONST.__const: 0x1cce0
-  __DATA_CONST.__objc_classlist: 0x5248
-  __DATA_CONST.__objc_catlist: 0x360
+  __TEXT.__objc_classname: 0x21f96
+  __TEXT.__objc_methname: 0x1ce4ec
+  __TEXT.__objc_methtype: 0x4c7cf
+  __TEXT.__objc_stubs: 0xf3720
+  __DATA_CONST.__got: 0xa100
+  __DATA_CONST.__const: 0x1c928
+  __DATA_CONST.__objc_classlist: 0x51f0
+  __DATA_CONST.__objc_catlist: 0x350
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2928
+  __DATA_CONST.__objc_protolist: 0x2930
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4aa20
+  __DATA_CONST.__objc_selrefs: 0x4a8a8
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3f78
-  __DATA_CONST.__objc_arraydata: 0x1850
-  __AUTH_CONST.__auth_got: 0x2ad0
-  __AUTH_CONST.__const: 0x10998
-  __AUTH_CONST.__cfstring: 0x6efc0
-  __AUTH_CONST.__objc_const: 0x269638
-  __AUTH_CONST.__objc_arrayobj: 0x1770
-  __AUTH_CONST.__objc_doubleobj: 0x680
-  __AUTH_CONST.__objc_intobj: 0x2bc8
+  __DATA_CONST.__objc_superrefs: 0x3f30
+  __DATA_CONST.__objc_arraydata: 0x1878
+  __AUTH_CONST.__auth_got: 0x2ac8
+  __AUTH_CONST.__const: 0x109e8
+  __AUTH_CONST.__cfstring: 0x6ee60
+  __AUTH_CONST.__objc_const: 0x267ba0
+  __AUTH_CONST.__objc_arrayobj: 0x1788
+  __AUTH_CONST.__objc_doubleobj: 0x670
+  __AUTH_CONST.__objc_intobj: 0x2c28
   __AUTH_CONST.__objc_dictobj: 0x320
-  __AUTH.__objc_data: 0x104a0
-  __DATA.__objc_ivar: 0xf338
-  __DATA.__data: 0x1f8b8
+  __AUTH.__objc_data: 0x10540
+  __DATA.__objc_ivar: 0xf20c
+  __DATA.__data: 0x1f918
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xab0
+  __DATA.__bss: 0xac0
   __DATA.__common: 0xa40
-  __DATA_DIRTY.__objc_data: 0x23230
+  __DATA_DIRTY.__objc_data: 0x22e20
   __DATA_DIRTY.__data: 0x180
   __DATA_DIRTY.__bss: 0x1a78
   __DATA_DIRTY.__common: 0x50

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 8676BE2A-9484-3492-888E-7DE10333250F
-  Functions: 70051
-  Symbols:   236885
-  CStrings:  104141
+  UUID: 841F60C0-8A48-3E49-B5CB-F511B233B2C9
+  Functions: 69819
+  Symbols:   236230
+  CStrings:  104019
 
Symbols:
+ +[SBHIconGridSizeClassSizeMap(SBUnitTests) sb_test_padGridSizeClassMap]
+ +[SBHIconGridSizeClassSizeMap(SBUnitTests) sb_test_phoneGridSizeClassMap]
+ -[NSObject(SBDisplayItemLayoutAttributes) sb_isDisplayItemLayoutAttributes]
+ -[SBActivityBannerObserver _postBannerWithAlert:]
+ -[SBActivityBannerObserver presentFallbackAlert:]
+ -[SBActivityManager alertPresentationFailed:]
+ -[SBActivitySystemApertureElementObserver presentFallbackAlert:]
+ -[SBAppSwitcherContinuousExposeSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[SBApplication _appRestrictionReason]
+ -[SBApplication isLaunchDisallowedForRatingRank]
+ -[SBCommandTabController selectedDisplayItem]
+ -[SBContinuousExposeRootSwitcherModifier handleDidEdgeProtectResizeGrabberEvent:]
+ -[SBContinuousExposeWindowDragContainerSwitcherModifier homeScreenDimmingAlpha]
+ -[SBDashBoardLockScreenEnvironment willUIUnlockFromSource:isLockScreenDisabledForAssertion:]
+ -[SBDeckFloatingSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[SBDeckSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[SBDestroyDisplayItemSwitcherEventResponse destroyAllScenesMatchingBundleIdentifier]
+ -[SBDestroyDisplayItemSwitcherEventResponse initWithDisplayItem:destroyAllScenesMatchingBundleIdentifier:]
+ -[SBDestroyDisplayItemSwitcherEventResponse initWithDisplayItem:destroyAllScenesMatchingBundleIdentifier:].cold.1
+ -[SBDidEdgeProtectResizeGrabberModifierEvent .cxx_destruct]
+ -[SBDidEdgeProtectResizeGrabberModifierEvent corners]
+ -[SBDidEdgeProtectResizeGrabberModifierEvent displayItem]
+ -[SBDidEdgeProtectResizeGrabberModifierEvent hasEmptyCorners]
+ -[SBDidEdgeProtectResizeGrabberModifierEvent initWithDisplayItem:corners:]
+ -[SBDidEdgeProtectResizeGrabberModifierEvent type]
+ -[SBDisplayItemLayoutAttributes sb_isDisplayItemLayoutAttributes]
+ -[SBDisplayItemLayoutAttributesProvider performBlockWithoutUpdating:]
+ -[SBDisplayItemLayoutAttributesProvider performBlockWithoutUpdating:].cold.1
+ -[SBDragAndDropWorkspaceTransaction _defaultReferenceSizeForSceneView]
+ -[SBDynamicLightingController disableEffectsForReason:]
+ -[SBDynamicLightingController initWithBacklightController:thermalController:]
+ -[SBFluidSwitcherViewController homeScreenIsOnFirstPage]
+ -[SBFluidSwitcherViewController isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[SBFluidSwitcherViewController noteDidEdgeProtectResizeGrabberForDisplayItem:inCorner:]
+ -[SBFluidSwitcherViewController sceneHandleDisablesKillingInSwitcher:]
+ -[SBHeartbeatMetricPersistence cleanUpPersistedDataIfNeeded]
+ -[SBHeartbeatMetricPersistence initWithPersistenceURL:]
+ -[SBHomeScreenController _lockScreenUIWillDismiss:]
+ -[SBHomeScreenController iconManager:preferredMenuElementOrderForIconView:]
+ -[SBHomeScreenMenuBar .cxx_destruct]
+ -[SBHomeScreenMenuBar _activateAppLayout:fromSwitcher:withWindowScene:]
+ -[SBHomeScreenMenuBar _createRecentAppsMenu]
+ -[SBHomeScreenMenuBar _handleEditHomeScreenShortcut]
+ -[SBHomeScreenMenuBar _handleShutDown]
+ -[SBHomeScreenMenuBar buildMenuWithBuilder:]
+ -[SBHomeScreenMenuBar delegate]
+ -[SBHomeScreenMenuBar getEditMenu]
+ -[SBHomeScreenMenuBar handleActionWithURL:]
+ -[SBHomeScreenMenuBar handleAppStoreAction]
+ -[SBHomeScreenMenuBar homeScreenMenuBarProvidingScene]
+ -[SBHomeScreenMenuBar initWithWindowSceneManager:]
+ -[SBHomeScreenMenuBar setDelegate:]
+ -[SBHomeScreenMenuBar setHomeScreenMenuBarProvidingScene:]
+ -[SBHomeScreenMenuBar setWindowSceneManager:]
+ -[SBHomeScreenMenuBar showConfirmationAlertWithTitle:message:confirmTitle:handler:]
+ -[SBHomeScreenMenuBar toggleMenuBarVisibility]
+ -[SBHomeScreenMenuBar windowSceneManager]
+ -[SBHomeScreenMenuBar windowScene]
+ -[SBIconModel insertOSMigrationHomeScreenLayoutItem:intoListAtIndex:inFolder:rootFolder:referenceGridSize:subsequentListSlide:]
+ -[SBLockScreenBiometricAuthenticationCoordinator _shouldShowAlertForSeed]
+ -[SBLockScreenViewControllerBase willUIUnlockFromSource:isLockScreenDisabledForAssertion:]
+ -[SBLoginAppContainerViewController willUIUnlockFromSource:isLockScreenDisabledForAssertion:]
+ -[SBMainSwitcherControllerCoordinator switcherContentController:removeDisplayItemsFromDesktop:]
+ -[SBMedusaDecoratedDeviceApplicationSceneViewController topAffordanceViewController:requestsPerformShortcutActionWithType:]
+ -[SBMenuBarHelpMenuProvider searchTextFieldUsedOnce]
+ -[SBMenuBarHelpMenuProvider setSearchTextFieldUsedOnce:]
+ -[SBMenuBarInvocationMetric handleEvent:withContext:]
+ -[SBMenuBarItemSelectionMetric handleEvent:withContext:]
+ -[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]
+ -[SBMenuBarManager displayNameForWebAppWithSceneIdentifier:]
+ -[SBMenuBarManager isPointInsideMenuBarContent:fromCoordinateSpace:]
+ -[SBMenuBarManager systemHideMenuWithOptions:]
+ -[SBMenuBarManager systemMenusToIgnoreForViewController:]
+ -[SBMenuBarManager systemQuitMenuWithOptions:]
+ -[SBMenuBarSearchMetric handleEvent:withContext:]
+ -[SBMenuBarViewController isSpringBoardMenuBarForScene:]
+ -[SBMenuBarViewController noteSearchUsedInMenuBarHelpMenuProvider:]
+ -[SBMenuBarViewController overrideClientNameForMainMenu:]
+ -[SBRecordingIndicatorSystemApertureElement _cancelDwellTimer]
+ -[SBRecordingIndicatorSystemApertureElement _ensureMotRequirements]
+ -[SBRecordingIndicatorSystemApertureElement _startDwellTimer]
+ -[SBRecordingIndicatorSystemApertureElement dealloc]
+ -[SBRecordingIndicatorSystemApertureElement indicatorNeedsDisplayWellKnownLocation]
+ -[SBRecordingIndicatorSystemApertureElement initWithInterSensorRegionIndicatorVisualRepresentation:microRegionIndicatorVisualRepresentation:recordingIndicatorManager:minimumOnTimeCoordinator:]
+ -[SBRecordingIndicatorSystemApertureElement initWithInterSensorRegionIndicatorVisualRepresentation:microRegionIndicatorVisualRepresentation:recordingIndicatorManager:minimumOnTimeCoordinator:].cold.1
+ -[SBRecordingIndicatorSystemApertureElement interSensorDwellTimerSatisfied]
+ -[SBRecordingIndicatorSystemApertureElement interSensorDwellTimer]
+ -[SBRecordingIndicatorSystemApertureElement layoutHost]
+ -[SBRecordingIndicatorSystemApertureElement minimumOnTimeAssertion]
+ -[SBRecordingIndicatorSystemApertureElement minimumOnTimeCoordinator]
+ -[SBRecordingIndicatorSystemApertureElement minimumOnTimeSatisfied]
+ -[SBRecordingIndicatorSystemApertureElement preferredIndicatorEdgeOutsets]
+ -[SBRecordingIndicatorSystemApertureElement resetInternalState]
+ -[SBRecordingIndicatorSystemApertureElement setInterSensorDwellTimer:]
+ -[SBRecordingIndicatorSystemApertureElement setInterSensorDwellTimerSatisfied:]
+ -[SBRecordingIndicatorSystemApertureElement setLayoutHost:]
+ -[SBRecordingIndicatorSystemApertureElement setMinimumOnTimeAssertion:]
+ -[SBRecordingIndicatorSystemApertureElement setMinimumOnTimeCoordinator:]
+ -[SBRecordingIndicatorSystemApertureElement setMinimumOnTimeSatisfied:]
+ -[SBRecordingIndicatorSystemApertureElement sizeThatFitsSize:forProvidedView:]
+ -[SBRecordingIndicatorWindow wantsDisableUpdateClonedDuringSharePlay]
+ -[SBRemoteTransientOverlayHostViewController _pendOrExecuteDelegateCallout:]
+ -[SBRemoveFromDesktopSwitcherEventResponse displayItems]
+ -[SBRemoveFromDesktopSwitcherEventResponse initWithDisplayItems:]
+ -[SBRemoveFromDesktopSwitcherEventResponse initWithDisplayItems:].cold.1
+ -[SBResizeGrabberHintingSwitcherModifier .cxx_destruct]
+ -[SBResizeGrabberHintingSwitcherModifier _isHandlingEvent:]
+ -[SBResizeGrabberHintingSwitcherModifier corners]
+ -[SBResizeGrabberHintingSwitcherModifier description]
+ -[SBResizeGrabberHintingSwitcherModifier displayItem]
+ -[SBResizeGrabberHintingSwitcherModifier handleDidEdgeProtectResizeGrabberEvent:]
+ -[SBResizeGrabberHintingSwitcherModifier handleTimerEvent:]
+ -[SBResizeGrabberHintingSwitcherModifier identifier]
+ -[SBResizeGrabberHintingSwitcherModifier initWithDisplayItem:corners:]
+ -[SBResizeGrabberHintingSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[SBResizeGrabberHintingSwitcherModifier visibleCornersForTouchResizeForLayoutRole:inAppLayout:]
+ -[SBRoutingSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[SBSAIndicatorAppearanceStateContext .cxx_destruct]
+ -[SBSAIndicatorAppearanceStateContext _setActiveIndicatorElementContext:]
+ -[SBSAIndicatorAppearanceStateContext activeIndicatorElementContext]
+ -[SBSAIndicatorAppearanceStateContext isSettled]
+ -[SBSAIndicatorAppearanceStateContextMutator activeIndicatorElementContext]
+ -[SBSAIndicatorAppearanceStateContextMutator setActiveIndicatorElementContext:]
+ -[SBSAIndicatorElementContext _setIndicatorNeedsDisplayWellKnownLocation:]
+ -[SBSAIndicatorElementContext _setIndicatorSize:]
+ -[SBSAIndicatorElementContext _setPreferredEdgeOutsets:]
+ -[SBSAIndicatorElementContext indicatorNeedsDisplayWellKnownLocation]
+ -[SBSAIndicatorElementContext indicatorSize]
+ -[SBSAIndicatorElementContext preferredEdgeOutsets]
+ -[SBSAIndicatorElementContextMutator indicatorNeedsDisplayWellKnownLocation]
+ -[SBSAIndicatorElementContextMutator indicatorSize]
+ -[SBSAIndicatorElementContextMutator preferredEdgeOutsets]
+ -[SBSAIndicatorElementContextMutator setIndicatorNeedsDisplayWellKnownLocation:]
+ -[SBSAIndicatorElementContextMutator setIndicatorSize:]
+ -[SBSAIndicatorElementContextMutator setPreferredEdgeOutsets:]
+ -[SBSAMaintainedPreferences jsonDescription]
+ -[SBSceneManager isSceneHandleNotUserDestroyable:]
+ -[SBSecureIndicatorBacklightCoordinator allowsBacklightChanges]
+ -[SBShelfCarouselSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[SBSwitcherController _buildHideMenuWithAdditionalOptions:]
+ -[SBSwitcherController _buildQuitMenuWithAdditionalOptions:]
+ -[SBSwitcherController _centerWindowSizeForPreviousFullscreenWindow]
+ -[SBSwitcherController _handleCloseAllWindowsShortcut:]
+ -[SBSwitcherController _handleCloseWindowShortcut:]
+ -[SBSwitcherController _handleRemoveAllWindowFromSetAndQuitShortcut:]
+ -[SBSwitcherController _handleRemoveAllWindowFromSetForNonSelectedAppShortcut:]
+ -[SBSwitcherController _handleRemoveAllWindowFromSetShortcut:]
+ -[SBSwitcherController _homeScreenIsOnFirstPage]
+ -[SBSwitcherController _removeDisplayItemsFromDesktop:]
+ -[SBSwitcherController hideMenuWithOptions:]
+ -[SBSwitcherController quitMenuWithOptions:]
+ -[SBSwitcherModifier handleDidEdgeProtectResizeGrabberEvent:]
+ -[SBSwitcherTransitionRequest bundleIdentifierOfAppToKillGracefully]
+ -[SBSwitcherTransitionRequest setBundleIdentifierOfAppToKillGracefully:]
+ -[SBSystemAperturePlatformElementHost performAction:withCompletionUponIndicatorSettling:]
+ -[SBSystemApertureProvidedContentElement minimumCustomElementHeightUnderSensor]
+ -[SBSystemApertureProvidedContentElement minimumCustomElementHeightUnderSensor].cold.1
+ -[SBSystemApertureSceneElement _layoutHostMayNotPerformLayoutUpdateWithReasonsToExclude:]
+ -[SBSystemApertureSettings indicatorContainerMinimumOutset]
+ -[SBSystemApertureSettings indicatorContentMinimumScale]
+ -[SBSystemApertureSettings indicatorMinimumScreenPadding]
+ -[SBSystemApertureSettings setIndicatorContainerMinimumOutset:]
+ -[SBSystemApertureSettings setIndicatorContentMinimumScale:]
+ -[SBSystemApertureSettings setIndicatorMinimumScreenPadding:]
+ -[SBSystemApertureViewController _flushIndicatorDidSettleHandlersIfNecessary]
+ -[SBSystemApertureViewController _flushIndicatorDidSettleHandlersIfNecessary].cold.1
+ -[SBSystemApertureViewController indicatorNeedsDisplayWellKnownLocationDidInvalidateForLayoutSpecifier:]
+ -[SBSystemApertureViewController performAction:withCompletionUponIndicatorSettling:]
+ -[SBSystemApertureViewController preferredIndicatorEdgeOutsetsDidInvalidateForLayoutSpecifier:]
+ -[SBSystemShellEmbeddedDisplayController scene]
+ -[SBTopAffordanceViewController _requestPerformShortcutActionWithType:]
+ -[SBWorkspaceApplicationSceneTransitionContext isContingencyPlan]
+ -[SBWorkspaceApplicationSceneTransitionContext setContingencyPlan:]
+ -[SpringBoard _handleCloseAllWindowsShortcut:]
+ -[SpringBoard _handleCloseWindowShortcut:]
+ -[SpringBoard _handleReboot]
+ -[SpringBoard _handleRemoveAllWindowFromSetAndQuitShortcut:]
+ -[SpringBoard _handleRemoveAllWindowFromSetForNonSelectedAppShortcut:]
+ -[SpringBoard _handleRemoveAllWindowFromSetShortcut:]
+ -[SpringBoard _handleRestartShortcutWithConfirmation]
+ -[SpringBoard _handleScreenshotFullScreenShortcut:]
+ -[SpringBoard _handleScreenshotPIPShortcut:]
+ -[SpringBoard dynamicLightingController]
+ -[SpringBoard homeScreenMenuBarProvidingScene]
+ -[SpringBoard homeScreenMenuBar]
+ -[SpringBoard systemMenuIdentifiersIgnoredInMenuBar]
+ -[_SBActiveAppFloorFloatingSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[_SBFullScreenAppFloorSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[_SBGridFloorSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[_SBHomeScreenFloorSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]
+ -[_SBHomeScreenFloorSwitcherModifier wantsMenuBar]
+ GCC_except_table176
+ GCC_except_table188
+ GCC_except_table194
+ GCC_except_table197
+ GCC_except_table221
+ GCC_except_table255
+ GCC_except_table268
+ GCC_except_table271
+ GCC_except_table274
+ GCC_except_table279
+ GCC_except_table281
+ GCC_except_table283
+ GCC_except_table305
+ GCC_except_table314
+ GCC_except_table317
+ GCC_except_table348
+ GCC_except_table369
+ GCC_except_table382
+ GCC_except_table383
+ GCC_except_table395
+ GCC_except_table407
+ GCC_except_table409
+ GCC_except_table442
+ GCC_except_table461
+ GCC_except_table485
+ GCC_except_table487
+ GCC_except_table489
+ GCC_except_table502
+ GCC_except_table510
+ GCC_except_table515
+ GCC_except_table517
+ GCC_except_table519
+ GCC_except_table530
+ GCC_except_table534
+ GCC_except_table538
+ GCC_except_table544
+ GCC_except_table548
+ GCC_except_table572
+ GCC_except_table618
+ GCC_except_table653
+ GCC_except_table723
+ GCC_except_table750
+ GCC_except_table791
+ GCC_except_table831
+ GCC_except_table870
+ GCC_except_table879
+ GCC_except_table925
+ GCC_except_table964
+ GCC_except_table971
+ GCC_except_table973
+ GCC_except_table975
+ GCC_except_table977
+ GCC_except_table979
+ GCC_except_table981
+ GCC_except_table983
+ _OBJC_CLASS_$_SBDidEdgeProtectResizeGrabberModifierEvent
+ _OBJC_CLASS_$_SBFMachNextMinuteDateProvider
+ _OBJC_CLASS_$_SBHIconGridSizeClassSizeMap
+ _OBJC_CLASS_$_SBHMutableIconGridSizeClassSizeMap
+ _OBJC_CLASS_$_SBHomeScreenMenuBar
+ _OBJC_CLASS_$_SBMenuBarInvocationMetric
+ _OBJC_CLASS_$_SBMenuBarItemSelectionMetric
+ _OBJC_CLASS_$_SBMenuBarSearchMetric
+ _OBJC_CLASS_$_SBResizeGrabberHintingSwitcherModifier
+ _OBJC_CLASS_$_UIMainMenuSystem
+ _OBJC_CLASS_$__SBFKeyWindowStack
+ _OBJC_IVAR_$_SBContinuityDisplayDelayedUIWindowSceneDelegate._disableDynamicLightingAssertion
+ _OBJC_IVAR_$_SBContinuousExposeWindowDragContainerSwitcherModifier._initialHomeScreenDimmingAlpha
+ _OBJC_IVAR_$_SBDestroyDisplayItemSwitcherEventResponse._destroyAllScenesMatchingBundleIdentifier
+ _OBJC_IVAR_$_SBDidEdgeProtectResizeGrabberModifierEvent._corners
+ _OBJC_IVAR_$_SBDidEdgeProtectResizeGrabberModifierEvent._displayItem
+ _OBJC_IVAR_$_SBDisplayItemLayoutAttributesProvider._isPerformingWithoutUpdating
+ _OBJC_IVAR_$_SBDragAndDropWorkspaceTransaction._cachedDefaultReferenceSizeForSceneView
+ _OBJC_IVAR_$_SBFileStackOpenIndicatorView._packageView
+ _OBJC_IVAR_$_SBHomeScreenMenuBar._delegate
+ _OBJC_IVAR_$_SBHomeScreenMenuBar._homeScreenMenuBarProvidingScene
+ _OBJC_IVAR_$_SBHomeScreenMenuBar._windowSceneManager
+ _OBJC_IVAR_$_SBMenuBarHelpMenuProvider._searchTextFieldUsedOnce
+ _OBJC_IVAR_$_SBMenuBarViewController._dismissed
+ _OBJC_IVAR_$_SBRecordingIndicatorSystemApertureElement._interSensorDwellTimer
+ _OBJC_IVAR_$_SBRecordingIndicatorSystemApertureElement._interSensorDwellTimerSatisfied
+ _OBJC_IVAR_$_SBRecordingIndicatorSystemApertureElement._layoutHost
+ _OBJC_IVAR_$_SBRecordingIndicatorSystemApertureElement._minimumOnTimeAssertion
+ _OBJC_IVAR_$_SBRecordingIndicatorSystemApertureElement._minimumOnTimeCoordinator
+ _OBJC_IVAR_$_SBRecordingIndicatorSystemApertureElement._minimumOnTimeSatisfied
+ _OBJC_IVAR_$_SBRemoteTransientOverlayHostViewController._pendedDelegateCalloutBlocks
+ _OBJC_IVAR_$_SBRemoveFromDesktopSwitcherEventResponse._displayItems
+ _OBJC_IVAR_$_SBResizeGrabberHintingSwitcherModifier._corners
+ _OBJC_IVAR_$_SBResizeGrabberHintingSwitcherModifier._displayItem
+ _OBJC_IVAR_$_SBSAIndicatorAppearanceStateContext._activeIndicatorElementContext
+ _OBJC_IVAR_$_SBSAIndicatorElementContext._indicatorNeedsDisplayWellKnownLocation
+ _OBJC_IVAR_$_SBSAIndicatorElementContext._indicatorSize
+ _OBJC_IVAR_$_SBSAIndicatorElementContext._preferredEdgeOutsets
+ _OBJC_IVAR_$_SBSwitcherTransitionRequest._bundleIdentifierOfAppToKillGracefully
+ _OBJC_IVAR_$_SBSystemApertureSettings._indicatorContainerMinimumOutset
+ _OBJC_IVAR_$_SBSystemApertureSettings._indicatorContentMinimumScale
+ _OBJC_IVAR_$_SBSystemApertureSettings._indicatorMinimumScreenPadding
+ _OBJC_IVAR_$_SBSystemApertureViewController._systemApertureIndicatorDidSettleCompletionBlocks
+ _OBJC_IVAR_$_SBWorkspaceApplicationSceneTransitionContext._contingencyPlan
+ _OBJC_IVAR_$_SpringBoard._homeScreenMenuBar
+ _OBJC_IVAR_$_SpringBoard._systemMenuIdentifiersIgnoredInMenuBar
+ _OBJC_METACLASS_$_SBDidEdgeProtectResizeGrabberModifierEvent
+ _OBJC_METACLASS_$_SBHomeScreenMenuBar
+ _OBJC_METACLASS_$_SBMenuBarInvocationMetric
+ _OBJC_METACLASS_$_SBMenuBarItemSelectionMetric
+ _OBJC_METACLASS_$_SBMenuBarSearchMetric
+ _OBJC_METACLASS_$_SBResizeGrabberHintingSwitcherModifier
+ _SBFIsHomeScreenMenuBarAvailable
+ _SBHIconGridRangeOffset
+ _SBMenuBarInvocationMetricEventName
+ _SBMenuBarItemSelectionMetricEventName
+ _SBMenuBarSearchUsedMetricEventName
+ _SBPasswordsBundleIdentifier
+ _SBStringFromUIRectCorner
+ _UIMenuApplication
+ _UIMenuEdit
+ _UIMenuFile
+ _UIMenuFormat
+ _UIMenuHide
+ _UIMenuQuit
+ _UIMenuView
+ _UIRectCornersAtEdges
+ __OBJC_$_CATEGORY_CLASS_METHODS_SBHIconGridSizeClassSizeMap_$_SBUnitTests
+ __OBJC_$_CATEGORY_SBHIconGridSizeClassSizeMap_$_SBUnitTests
+ __OBJC_$_INSTANCE_METHODS_NSObject(SBSceneLayoutStatusBarAssertionProvidingAdditions|SBSAGeometricTypeAnimationDecomposing|SBDisplayItemLayoutAttributes|SBApplicationSceneStatusBarDescribingAdditions|SBMainDisplaySceneLayoutElementViewControllingAdditions|SBSwitcherModifierDebugTimelineDescription|SBMedusaDecoratedDeviceApplicationSceneViewControllingAdditions)
+ __OBJC_$_INSTANCE_METHODS_SBDidEdgeProtectResizeGrabberModifierEvent
+ __OBJC_$_INSTANCE_METHODS_SBHomeScreenMenuBar
+ __OBJC_$_INSTANCE_METHODS_SBMenuBarInvocationMetric
+ __OBJC_$_INSTANCE_METHODS_SBMenuBarItemSelectionMetric
+ __OBJC_$_INSTANCE_METHODS_SBMenuBarSearchMetric
+ __OBJC_$_INSTANCE_METHODS_SBResizeGrabberHintingSwitcherModifier
+ __OBJC_$_INSTANCE_VARIABLES_SBDidEdgeProtectResizeGrabberModifierEvent
+ __OBJC_$_INSTANCE_VARIABLES_SBHomeScreenMenuBar
+ __OBJC_$_INSTANCE_VARIABLES_SBResizeGrabberHintingSwitcherModifier
+ __OBJC_$_PROP_LIST_SAUIIndicatorLayoutSpecifying
+ __OBJC_$_PROP_LIST_SBDidEdgeProtectResizeGrabberModifierEvent
+ __OBJC_$_PROP_LIST_SBHomeScreenMenuBar
+ __OBJC_$_PROP_LIST_SBMenuBarInvocationMetric
+ __OBJC_$_PROP_LIST_SBMenuBarItemSelectionMetric
+ __OBJC_$_PROP_LIST_SBMenuBarSearchMetric
+ __OBJC_$_PROP_LIST_SBResizeGrabberHintingSwitcherModifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SAUIIndicatorLayoutHosting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SAUIIndicatorLayoutSpecifying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBHomeScreenMenuBarDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SAUIIndicatorLayoutHosting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SAUIIndicatorLayoutSpecifying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBHomeScreenMenuBarDelegate
+ __OBJC_$_PROTOCOL_REFS_SAUIIndicatorLayoutHosting
+ __OBJC_$_PROTOCOL_REFS_SAUIIndicatorLayoutSpecifying
+ __OBJC_$_PROTOCOL_REFS_SBHomeScreenMenuBarDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SBMenuBarInvocationMetric
+ __OBJC_CLASS_PROTOCOLS_$_SBMenuBarItemSelectionMetric
+ __OBJC_CLASS_PROTOCOLS_$_SBMenuBarSearchMetric
+ __OBJC_CLASS_RO_$_SBDidEdgeProtectResizeGrabberModifierEvent
+ __OBJC_CLASS_RO_$_SBHomeScreenMenuBar
+ __OBJC_CLASS_RO_$_SBMenuBarInvocationMetric
+ __OBJC_CLASS_RO_$_SBMenuBarItemSelectionMetric
+ __OBJC_CLASS_RO_$_SBMenuBarSearchMetric
+ __OBJC_CLASS_RO_$_SBResizeGrabberHintingSwitcherModifier
+ __OBJC_LABEL_PROTOCOL_$_SAUIIndicatorLayoutHosting
+ __OBJC_LABEL_PROTOCOL_$_SAUIIndicatorLayoutSpecifying
+ __OBJC_LABEL_PROTOCOL_$_SBHomeScreenMenuBarDelegate
+ __OBJC_METACLASS_RO_$_SBDidEdgeProtectResizeGrabberModifierEvent
+ __OBJC_METACLASS_RO_$_SBHomeScreenMenuBar
+ __OBJC_METACLASS_RO_$_SBMenuBarInvocationMetric
+ __OBJC_METACLASS_RO_$_SBMenuBarItemSelectionMetric
+ __OBJC_METACLASS_RO_$_SBMenuBarSearchMetric
+ __OBJC_METACLASS_RO_$_SBResizeGrabberHintingSwitcherModifier
+ __OBJC_PROTOCOL_$_SAUIIndicatorLayoutHosting
+ __OBJC_PROTOCOL_$_SAUIIndicatorLayoutSpecifying
+ __OBJC_PROTOCOL_$_SBHomeScreenMenuBarDelegate
+ __SBWindowControlsAnalyticsLogAction
+ ___102-[SBMedusaDecoratedDeviceApplicationSceneViewController updateTopAffordanceOverrideUserInterfaceStyle]_block_invoke
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.318
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.319
+ ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.320
+ ___111-[SBMainSwitcherControllerCoordinator switcherContentController:performTransitionWithRequest:gestureInitiated:]_block_invoke_3
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.654
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.656
+ ___128-[SBSceneSnapshotRequestor _fbsSceneSnapshotRequestsFromSBSceneSnapshotRequests:forSceneHandle:settings:snapshotRequestContext:]_block_invoke
+ ___39-[SBSAIndicatorElementContext isEqual:]_block_invoke_6
+ ___39-[SBSAIndicatorElementContext isEqual:]_block_invoke_7
+ ___43-[SBHomeScreenMenuBar handleActionWithURL:]_block_invoke
+ ___43-[SBHomeScreenMenuBar handleAppStoreAction]_block_invoke
+ ___44-[SBHomeScreenMenuBar _createRecentAppsMenu]_block_invoke
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_10
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_11
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_12
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_13
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_14
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_2
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_3
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_4
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_5
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_6
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_7
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_8
+ ___44-[SBHomeScreenMenuBar buildMenuWithBuilder:]_block_invoke_9
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1221
+ ___47-[SBSAIndicatorAppearanceStateContext isEqual:]_block_invoke_4
+ ___49-[SBActivityBannerObserver _postBannerWithAlert:]_block_invoke
+ ___49-[SBMenuBarSearchMetric handleEvent:withContext:]_block_invoke
+ ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.90
+ ___53-[SBMenuBarInvocationMetric handleEvent:withContext:]_block_invoke
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.766
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.797
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.828
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.934
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.821
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.938
+ ___53-[SpringBoard _handleRestartShortcutWithConfirmation]_block_invoke
+ ___56-[SBMenuBarItemSelectionMetric handleEvent:withContext:]_block_invoke
+ ___56-[SBRemoteTransientOverlayHostViewController deactivate]_block_invoke
+ ___56-[SBRemoteTransientOverlayHostViewController invalidate]_block_invoke
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1786
+ ___58-[SBSystemApertureViewController _indicatorElementContext]_block_invoke.cold.2
+ ___59-[SBMenuBarViewController _loadAllMainMenusWithCompletion:]_block_invoke_4
+ ___60-[SBRemoteTransientOverlayHostViewController setAllowsSiri:]_block_invoke
+ ___60-[SBSwitcherController _buildHideMenuWithAdditionalOptions:]_block_invoke
+ ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.933
+ ___61-[SBRecordingIndicatorSystemApertureElement _startDwellTimer]_block_invoke
+ ___62-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]_block_invoke
+ ___62-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]_block_invoke_2
+ ___62-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]_block_invoke_3
+ ___62-[SBMenuBarManager _setMenuBarVisible:animated:userInitiated:]_block_invoke_4
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_10
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_11
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_12
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_2
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_3
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_4
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_5
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_6
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_7
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_8
+ ___63-[SBGlassBannerTransitionAnimator performActionsForTransition:]_block_invoke_9
+ ___63-[SBRemoteTransientOverlayHostViewController setAllowsBanners:]_block_invoke
+ ___64-[SBActivityManager _activityStartedOrUpdatedWithContentUpdate:]_block_invoke.45
+ ___66-[SBRemoteTransientOverlayHostViewController setAllowsAlertItems:]_block_invoke
+ ___67-[SBRecordingIndicatorSystemApertureElement _ensureMotRequirements]_block_invoke
+ ___68-[SBFluidSwitcherViewController _performDestroyDisplayItemResponse:]_block_invoke_2
+ ___68-[SBFluidSwitcherViewController _performDestroyDisplayItemResponse:]_block_invoke_2.cold.1
+ ___69-[SBDashBoardEmergencyDialerViewController _updateEmergencyCallMode:]_block_invoke.27
+ ___69-[SBRemoteTransientOverlayHostViewController setAllowsControlCenter:]_block_invoke
+ ___69-[SBRemoteTransientOverlayHostViewController setSwipeDismissalStyle:]_block_invoke
+ ___70-[SBRemoteTransientOverlayHostViewController setReachabilityDisabled:]_block_invoke
+ ___71-[SBHomeScreenMenuBar _activateAppLayout:fromSwitcher:withWindowScene:]_block_invoke
+ ___71-[SBHomeScreenMenuBar _activateAppLayout:fromSwitcher:withWindowScene:]_block_invoke.252
+ ___71-[SBHomeScreenMenuBar _activateAppLayout:fromSwitcher:withWindowScene:]_block_invoke_2
+ ___71-[SBRemoteTransientOverlayHostViewController setWallpaperTunnelActive:]_block_invoke
+ ___73-[SBRemoteTransientOverlayHostViewController setDesiredAutoLockDuration:]_block_invoke
+ ___73-[SBRemoteTransientOverlayHostViewController setDismissalAnimationStyle:]_block_invoke
+ ___73-[SBRemoteTransientOverlayHostViewController setSceneDeactivationReason:]_block_invoke
+ ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1093
+ ___74-[SBRemoteTransientOverlayHostViewController setDesiredIdleTimerSettings:]_block_invoke
+ ___75-[SBRemoteTransientOverlayHostViewController setAllowsMenuButtonDismissal:]_block_invoke
+ ___75-[SBRemoteTransientOverlayHostViewController setWhitePointAdaptivityStyle:]_block_invoke
+ ___75-[_SBFullScreenAppFloorSwitcherModifier handleSwitcherShortcutActionEvent:]_block_invoke_5
+ ___75-[_SBFullScreenAppFloorSwitcherModifier handleSwitcherShortcutActionEvent:]_block_invoke_6
+ ___75-[_SBFullScreenAppFloorSwitcherModifier handleSwitcherShortcutActionEvent:]_block_invoke_7
+ ___77-[SBDynamicLightingController initWithBacklightController:thermalController:]_block_invoke
+ ___77-[SBDynamicLightingController initWithBacklightController:thermalController:]_block_invoke_2
+ ___77-[SBRemoteTransientOverlayHostViewController setIdleTimerDisabled:forReason:]_block_invoke
+ ___77-[SBRemoteTransientOverlayHostViewController setWallpaperStyle:withDuration:]_block_invoke
+ ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke.23
+ ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke.23.cold.1
+ ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke.24
+ ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke.24.cold.1
+ ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke_2
+ ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke_2.cold.1
+ ___78-[SBDashBoardEmergencyDialerViewController _activateEmergencyDialerController]_block_invoke.23
+ ___78-[SBRecordingIndicatorSystemApertureElement didUpdateFixedIndicatorViewAlpha:]_block_invoke
+ ___78-[SBRecordingIndicatorSystemApertureElement didUpdateFixedIndicatorViewAlpha:]_block_invoke_2
+ ___78-[SBRemoteTransientOverlayHostViewController _setDesiredHardwareButtonEvents:]_block_invoke
+ ___78-[SBRemoteTransientOverlayHostViewController configureWithContext:completion:]_block_invoke_4
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke.123
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_2.125
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_33
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_34
+ ___79-[SBRemoteTransientOverlayHostViewController setLaunchingInterfaceOrientation:]_block_invoke
+ ___79-[SBRemoteTransientOverlayHostViewController viewServiceDidTerminateWithError:]_block_invoke
+ ___79-[SBSystemApertureProvidedContentElement minimumCustomElementHeightUnderSensor]_block_invoke
+ ___81-[SBRemoteTransientOverlayHostViewController setOrientationChangedEventsEnabled:]_block_invoke
+ ___82-[SBCoverSheetPresentationManager _prepareIconAnimatorForPresenting:withVelocity:]_block_invoke
+ ___83-[SBHomeScreenMenuBar showConfirmationAlertWithTitle:message:confirmTitle:handler:]_block_invoke
+ ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.222
+ ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke.45
+ ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke_2.46
+ ___85-[SBRoutingSwitcherModifier isHintingResizeGrabberForDisplayItem:corner:inAppLayout:]_block_invoke
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.376
+ ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.377
+ ___86-[SBRemoteTransientOverlayHostViewController setInteractiveScreenshotGestureDisabled:]_block_invoke
+ ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.86
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1638
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1640
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1642
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1646
+ ___96-[SBRemoteTransientOverlayHostViewController setBackgroundActivitiesToCancel:animationSettings:]_block_invoke
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1769
+ ____SBWindowControlsAnalyticsLogAction_block_invoke
+ ___blockIMPFromContextSignature102_block_invoke
+ ___blockIMPFromEventSignature102_block_invoke
+ ___blockIMPFromQuerySignature102_block_invoke
+ ___block_descriptor_106_e8_32s40s_e8_v16?08ls32l8s40l8
+ ___block_descriptor_129_e8_32s40s48s56s64s72s80s88s_e38_B16?0"SBFluidSwitcherItemContainer"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_152_e8_32s40s48s56s64s72s80s_e33_v16?0?<?<v?BB>?"NSString">8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_160_e8_32s40s48s56s64s72s80s88s96s104s112r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r112l8s96l8s104l8
+ ___block_descriptor_32_e37_v24?0"BSProcessHandle"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_descriptor_40_e8_32w_e26_"NSArray"16?0"NSArray"8lw32l8
+ ___block_descriptor_48_e38_B40?0"SBChainableModifier"816Q2432l
+ ___block_descriptor_48_e8_32s40bs_e12_v24?0q8^B16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e26_"NSArray"16?0"NSArray"8ls32l8w48l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e26_"NSArray"16?0"NSArray"8lw48l8s32l8s40l8
+ ___block_descriptor_65_e8_32s40s48r_e8_v16?08ls32l8r48l8s40l8
+ ___block_literal_global.1067
+ ___block_literal_global.1076
+ ___block_literal_global.1107
+ ___block_literal_global.1112
+ ___block_literal_global.1167
+ ___block_literal_global.117
+ ___block_literal_global.1172
+ ___block_literal_global.1178
+ ___block_literal_global.1472
+ ___block_literal_global.1612
+ ___block_literal_global.1616
+ ___block_literal_global.1648
+ ___block_literal_global.1657
+ ___block_literal_global.1659
+ ___block_literal_global.1661
+ ___block_literal_global.1663
+ ___block_literal_global.1679
+ ___block_literal_global.1795
+ ___block_literal_global.1818
+ ___block_literal_global.1827
+ ___block_literal_global.1843
+ ___block_literal_global.335
+ ___block_literal_global.341
+ ___block_literal_global.345
+ ___block_literal_global.351
+ ___block_literal_global.353
+ ___block_literal_global.362
+ ___block_literal_global.372
+ ___block_literal_global.537
+ ___block_literal_global.542
+ ___block_literal_global.546
+ ___block_literal_global.580
+ ___block_literal_global.591
+ ___block_literal_global.593
+ ___block_literal_global.595
+ ___block_literal_global.599
+ ___block_literal_global.601
+ ___block_literal_global.603
+ ___block_literal_global.616
+ ___block_literal_global.631
+ ___block_literal_global.634
+ ___block_literal_global.659
+ ___block_literal_global.692
+ ___block_literal_global.815
+ ___block_literal_global.817
+ ___block_literal_global.824
+ ___block_literal_global.841
+ ___block_literal_global.851
+ ___block_literal_global.854
+ ___block_literal_global.882
+ ___block_literal_global.923
+ ___block_literal_global.927
+ ___block_literal_global.935
+ ___block_literal_global.940
+ _blockIMPFromContextSignature102
+ _blockIMPFromEventSignature102
+ _blockIMPFromQuerySignature102
+ _kResizeHintingDuration
+ _kSBSAnalyticsMenuBarItemSelectedMenuTitleKey
+ _minimumCustomElementHeightUnderSensor.__minimumCustomElementHeightUnderSensor
+ _minimumCustomElementHeightUnderSensor.onceToken
+ _objc_msgSend$_activateAppLayout:fromSwitcher:withWindowScene:
+ _objc_msgSend$_appRestrictionReason
+ _objc_msgSend$_buildHideMenuWithAdditionalOptions:
+ _objc_msgSend$_buildQuitMenuWithAdditionalOptions:
+ _objc_msgSend$_cancelDwellTimer
+ _objc_msgSend$_centerWindowSizeForPreviousFullscreenWindow
+ _objc_msgSend$_createRecentAppsMenu
+ _objc_msgSend$_defaultReferenceSizeForSceneView
+ _objc_msgSend$_ensureMotRequirements
+ _objc_msgSend$_flushIndicatorDidSettleHandlersIfNecessary
+ _objc_msgSend$_handleEditHomeScreenShortcut
+ _objc_msgSend$_handleLockShortcut:
+ _objc_msgSend$_handleReboot
+ _objc_msgSend$_handleShutDown
+ _objc_msgSend$_homeScreenIsOnFirstPage
+ _objc_msgSend$_isHandlingEvent:
+ _objc_msgSend$_layoutHostMayNotPerformLayoutUpdateWithReasonsToExclude:
+ _objc_msgSend$_pendOrExecuteDelegateCallout:
+ _objc_msgSend$_postBannerWithAlert:
+ _objc_msgSend$_removeDisplayItemsFromDesktop:
+ _objc_msgSend$_requestPerformShortcutActionWithType:
+ _objc_msgSend$_setActiveIndicatorElementContext:
+ _objc_msgSend$_setIndicatorNeedsDisplayWellKnownLocation:
+ _objc_msgSend$_setIndicatorSize:
+ _objc_msgSend$_setMenuBarVisible:animated:userInitiated:
+ _objc_msgSend$_shouldShowAlertForSeed
+ _objc_msgSend$_startDwellTimer
+ _objc_msgSend$activeIndicatorElementContext
+ _objc_msgSend$addIcon:toList:options:
+ _objc_msgSend$alertPresentationFailed:
+ _objc_msgSend$allowsBacklightChanges
+ _objc_msgSend$applicationState
+ _objc_msgSend$buildMenuWithBuilder:
+ _objc_msgSend$bundleIdentifierOfAppToKillGracefully
+ _objc_msgSend$cleanUpPersistedDataIfNeeded
+ _objc_msgSend$commandWithTitle:image:action:propertyList:alternates:
+ _objc_msgSend$destroyAllScenesMatchingBundleIdentifier
+ _objc_msgSend$disableEffectsForReason:
+ _objc_msgSend$displayNameForWebAppWithSceneIdentifier:
+ _objc_msgSend$dynamicLightingController
+ _objc_msgSend$editMenu
+ _objc_msgSend$expectedKeyWindow
+ _objc_msgSend$getEditMenu
+ _objc_msgSend$handleActionWithURL:
+ _objc_msgSend$handleAppStoreAction
+ _objc_msgSend$handleDidEdgeProtectResizeGrabberEvent:
+ _objc_msgSend$hideMenuWithOptions:
+ _objc_msgSend$homeScreenIsOnFirstPage
+ _objc_msgSend$homeScreenMenuBar
+ _objc_msgSend$homeScreenMenuBarProvidingScene
+ _objc_msgSend$indexOfFirstUsedGridCellInGridRange:
+ _objc_msgSend$indicatorContainerMinimumOutset
+ _objc_msgSend$indicatorContentMinimumScale
+ _objc_msgSend$indicatorMinimumScreenPadding
+ _objc_msgSend$indicatorNeedsDisplayWellKnownLocation
+ _objc_msgSend$indicatorNeedsDisplayWellKnownLocationDidInvalidateForLayoutSpecifier:
+ _objc_msgSend$indicatorSize
+ _objc_msgSend$initWithBacklightController:thermalController:
+ _objc_msgSend$initWithDisplayItem:corners:
+ _objc_msgSend$initWithDisplayItem:destroyAllScenesMatchingBundleIdentifier:
+ _objc_msgSend$initWithInterSensorRegionIndicatorVisualRepresentation:microRegionIndicatorVisualRepresentation:recordingIndicatorManager:minimumOnTimeCoordinator:
+ _objc_msgSend$initWithPersistenceURL:
+ _objc_msgSend$initWithReferenceView:
+ _objc_msgSend$insertOSMigrationHomeScreenLayoutItem:intoListAtIndex:inFolder:rootFolder:referenceGridSize:subsequentListSlide:
+ _objc_msgSend$isContingencyPlan
+ _objc_msgSend$isHintingResizeGrabberForDisplayItem:corner:inAppLayout:
+ _objc_msgSend$isLaunchDisallowedForRatingRank
+ _objc_msgSend$isPhoneUnlockEnabledAndRequirementsMet
+ _objc_msgSend$isPointInsideMenuBarContent:fromCoordinateSpace:
+ _objc_msgSend$isSceneHandleNotUserDestroyable:
+ _objc_msgSend$isSettled
+ _objc_msgSend$isSpringBoardMenuBarForScene:
+ _objc_msgSend$markIcon:asNeedingAnimation:
+ _objc_msgSend$minimumCustomElementHeightUnderSensor
+ _objc_msgSend$noteDidEdgeProtectResizeGrabberForDisplayItem:inCorner:
+ _objc_msgSend$noteSearchUsedInMenuBarHelpMenuProvider:
+ _objc_msgSend$openSensitiveURL:withOptions:
+ _objc_msgSend$performAction:withCompletionUponIndicatorSettling:
+ _objc_msgSend$performBlockWithoutUpdating:
+ _objc_msgSend$persistenceURL
+ _objc_msgSend$preferredIndicatorEdgeOutsets
+ _objc_msgSend$presentFallbackAlert:
+ _objc_msgSend$quitMenuWithOptions:
+ _objc_msgSend$removeMenuForIdentifier:
+ _objc_msgSend$replaceChildrenOfMenuForIdentifier:fromChildrenBlock:
+ _objc_msgSend$resetInternalState
+ _objc_msgSend$restrictionReason
+ _objc_msgSend$sb_isDisplayItemLayoutAttributes
+ _objc_msgSend$sceneHandleDisablesKillingInSwitcher:
+ _objc_msgSend$setActiveIndicatorElementContext:
+ _objc_msgSend$setAsynchronousOpaque:
+ _objc_msgSend$setBundleIdentifierOfAppToKillGracefully:
+ _objc_msgSend$setContingencyPlan:
+ _objc_msgSend$setCornerOffset:
+ _objc_msgSend$setGridSize:forGridSizeClass:
+ _objc_msgSend$setIndicatorContainerMinimumOutset:
+ _objc_msgSend$setIndicatorContentMinimumScale:
+ _objc_msgSend$setIndicatorMinimumScreenPadding:
+ _objc_msgSend$setIndicatorNeedsDisplayWellKnownLocation:
+ _objc_msgSend$setIndicatorSize:
+ _objc_msgSend$setInterSensorDwellTimerSatisfied:
+ _objc_msgSend$setMinimumOnTimeSatisfied:
+ _objc_msgSend$sharedSystem
+ _objc_msgSend$showConfirmationAlertWithTitle:message:confirmTitle:handler:
+ _objc_msgSend$sizeThatFitsSize:forProvidedView:
+ _objc_msgSend$switcherContentController:removeDisplayItemsFromDesktop:
+ _objc_msgSend$systemHideMenuWithOptions:
+ _objc_msgSend$systemMenuIdentifiersIgnoredInMenuBar
+ _objc_msgSend$systemMenusToIgnoreForViewController:
+ _objc_msgSend$systemQuitMenuWithOptions:
+ _objc_msgSend$toggleMenuBarVisibility
+ _objc_msgSend$topAffordanceViewController:requestsPerformShortcutActionWithType:
+ _objc_msgSend$wantsDisableUpdateClonedDuringSharePlay
+ _objc_msgSend$willUIUnlockFromSource:isLockScreenDisabledForAssertion:
- +[SBDeviceEmulationController applicationInitializationContext]
- +[SBDeviceEmulationController deviceContext]
- +[SBDeviceEmulationController displayContext]
- -[SBAppLayout cachedLastAutoLayoutSpace]
- -[SBAppLayout setCachedLastAutoLayoutSpace:]
- -[SBCenterWindowSessionMetric .cxx_destruct]
- -[SBCenterWindowSessionMetric _bundleIdentifierForElementWithLayoutRole:fromContext:]
- -[SBCenterWindowSessionMetric _sendCoreAnalyticsEventWithStartReason:endReason:duration:centerBundleIdentifier:doNotDisturbActive:hardwareKeyboardAttached:]
- -[SBCenterWindowSessionMetric centerBundleIdentifier]
- -[SBCenterWindowSessionMetric initWithHeartbeatMetricPersistence:]
- -[SBCenterWindowSessionMetric sendCoreAnalyticsEventWithName:payload:]
- -[SBCenterWindowSessionMetric setCenterBundleIdentifier:]
- -[SBCenterWindowSessionMetric setStartReason:]
- -[SBCenterWindowSessionMetric setStartTimestamp:]
- -[SBCenterWindowSessionMetric startReason]
- -[SBCenterWindowSessionMetric startTimestamp]
- -[SBContinuousExposeAutoLayoutController _compactSpacingBetweenItemsInSpace:configuration:]
- -[SBContinuousExposeAutoLayoutController _fullyOccludedItemsForSpace:configuration:]
- -[SBContinuousExposeAutoLayoutController _itemsSortedByXInSpace:configuration:]
- -[SBContinuousExposeAutoLayoutController _performAutoLayoutWithSpace:configuration:stageInset:]
- -[SBContinuousExposeAutoLayoutController _performAutoLayoutWithSpace:configuration:stageInset:].cold.1
- -[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]
- -[SBContinuousExposeAutoLayoutController _spaceWithoutPerformingAutoLayoutWithSpace:previousSpace:configuration:options:]
- -[SBContinuousExposeAutoLayoutController _updateCompactedFramesForSpace:configuration:]
- -[SBContinuousExposeAutoLayoutController _updateCompactedFramesForSpace:configuration:].cold.1
- -[SBContinuousExposeAutoLayoutController _updateItemsCoveredByFullyOccludedPeekingItemsInSpace:configuration:]
- -[SBContinuousExposeAutoLayoutController _updateOcclusionStatusForItemsInSpace:configuration:]
- -[SBContinuousExposeAutoLayoutController boundingBoxForSpace:configuration:]
- -[SBContinuousExposeAutoLayoutController dodgeFullyOccludedWindowsToNearestVisibleEdgeForSpace:configuration:]
- -[SBContinuousExposeAutoLayoutController snapPositionToNearestEdgesIfNecessaryForSpace:stageArea:configuration:]
- -[SBContinuousExposeAutoLayoutController spaceByPerformingAutoLayoutWithSpace:previousSpace:configuration:options:]
- -[SBContinuousExposeAutoLayoutController stageAreaForSpace:configuration:]
- -[SBContinuousExposeAutoLayoutController updateOverlappingScaleAnchorPositionsForSpace:configuration:]
- -[SBContinuousExposeAutoLayoutController validBottomStageAreaInsetsWithConfiguration:]
- -[SBContinuousExposeAutoLayoutController validLeadingStageAreaInsetsWithConfiguration:]
- -[SBContinuousExposeAutoLayoutController validTopStageAreaInsetsWithConfiguration:]
- -[SBContinuousExposeAutoLayoutController validTrailingStageAreaInsetsWithConfiguration:]
- -[SBContinuousExposeAutoLayoutItem .cxx_destruct]
- -[SBContinuousExposeAutoLayoutItem _copyWithClass:]
- -[SBContinuousExposeAutoLayoutItem anchorPosition]
- -[SBContinuousExposeAutoLayoutItem compactedPosition]
- -[SBContinuousExposeAutoLayoutItem copyWithZone:]
- -[SBContinuousExposeAutoLayoutItem descriptionBuilderWithMultilinePrefix:]
- -[SBContinuousExposeAutoLayoutItem descriptionWithMultilinePrefix:]
- -[SBContinuousExposeAutoLayoutItem description]
- -[SBContinuousExposeAutoLayoutItem displayItem]
- -[SBContinuousExposeAutoLayoutItem hash]
- -[SBContinuousExposeAutoLayoutItem initWithDisplayItem:]
- -[SBContinuousExposeAutoLayoutItem initWithDisplayItem:].cold.1
- -[SBContinuousExposeAutoLayoutItem isEqual:]
- -[SBContinuousExposeAutoLayoutItem isFullyOccluded]
- -[SBContinuousExposeAutoLayoutItem isInDefaultPosition]
- -[SBContinuousExposeAutoLayoutItem isOverlapped]
- -[SBContinuousExposeAutoLayoutItem isPartiallyCoveredByPeekingItem]
- -[SBContinuousExposeAutoLayoutItem mutableCopyWithZone:]
- -[SBContinuousExposeAutoLayoutItem position]
- -[SBContinuousExposeAutoLayoutItem setAnchorPosition:]
- -[SBContinuousExposeAutoLayoutItem setCompactedPosition:]
- -[SBContinuousExposeAutoLayoutItem setFullyOccluded:]
- -[SBContinuousExposeAutoLayoutItem setInDefaultPosition:]
- -[SBContinuousExposeAutoLayoutItem setOverlapped:]
- -[SBContinuousExposeAutoLayoutItem setPartiallyCoveredByPeekingItem:]
- -[SBContinuousExposeAutoLayoutItem setPosition:]
- -[SBContinuousExposeAutoLayoutItem setSize:]
- -[SBContinuousExposeAutoLayoutItem setUnoccludedPeekingPosition:]
- -[SBContinuousExposeAutoLayoutItem size]
- -[SBContinuousExposeAutoLayoutItem succinctDescriptionBuilder]
- -[SBContinuousExposeAutoLayoutItem succinctDescription]
- -[SBContinuousExposeAutoLayoutItem unoccludedPeekingPosition]
- -[SBContinuousExposeAutoLayoutSpace .cxx_destruct]
- -[SBContinuousExposeAutoLayoutSpace _copyWithClass:]
- -[SBContinuousExposeAutoLayoutSpace autoLayoutItemForDisplayItem:]
- -[SBContinuousExposeAutoLayoutSpace autoLayoutItemForDisplayItem:].cold.1
- -[SBContinuousExposeAutoLayoutSpace autoLayoutItemForDisplayItemIfExists:]
- -[SBContinuousExposeAutoLayoutSpace boundingBox]
- -[SBContinuousExposeAutoLayoutSpace compactedBoundingBox]
- -[SBContinuousExposeAutoLayoutSpace configuration]
- -[SBContinuousExposeAutoLayoutSpace containsDisplayItem:]
- -[SBContinuousExposeAutoLayoutSpace copyWithZone:]
- -[SBContinuousExposeAutoLayoutSpace descriptionBuilderWithMultilinePrefix:]
- -[SBContinuousExposeAutoLayoutSpace descriptionWithMultilinePrefix:]
- -[SBContinuousExposeAutoLayoutSpace description]
- -[SBContinuousExposeAutoLayoutSpace hash]
- -[SBContinuousExposeAutoLayoutSpace initWithItems:]
- -[SBContinuousExposeAutoLayoutSpace initWithItems:].cold.1
- -[SBContinuousExposeAutoLayoutSpace isEqual:]
- -[SBContinuousExposeAutoLayoutSpace isStripVisible]
- -[SBContinuousExposeAutoLayoutSpace items]
- -[SBContinuousExposeAutoLayoutSpace mutableCopyWithZone:]
- -[SBContinuousExposeAutoLayoutSpace setBoundingBox:]
- -[SBContinuousExposeAutoLayoutSpace setCompactedBoundingBox:]
- -[SBContinuousExposeAutoLayoutSpace setConfiguration:]
- -[SBContinuousExposeAutoLayoutSpace setItems:]
- -[SBContinuousExposeAutoLayoutSpace setStageArea:]
- -[SBContinuousExposeAutoLayoutSpace setStripVisible:]
- -[SBContinuousExposeAutoLayoutSpace stageArea]
- -[SBContinuousExposeAutoLayoutSpace succinctDescriptionBuilder]
- -[SBContinuousExposeAutoLayoutSpace succinctDescription]
- -[SBContinuousExposeWindowDragContainerSwitcherModifier windowDragModifier]
- -[SBContinuousExposeWindowDragSwitcherModifier .cxx_destruct]
- -[SBContinuousExposeWindowDragSwitcherModifier _anyProposedAppLayoutContainsSelectedDisplayItem]
- -[SBContinuousExposeWindowDragSwitcherModifier _appLayoutContainingDisplayItem:]
- -[SBContinuousExposeWindowDragSwitcherModifier _baseLayoutSettings]
- -[SBContinuousExposeWindowDragSwitcherModifier _beginAnimatingAnchorPointRampingPropertyWithMode:settings:]
- -[SBContinuousExposeWindowDragSwitcherModifier _beginStageRubberbandingRampingPropertyWithMode:settings:]
- -[SBContinuousExposeWindowDragSwitcherModifier _isStripStashed]
- -[SBContinuousExposeWindowDragSwitcherModifier anchorPointForIndex:]
- -[SBContinuousExposeWindowDragSwitcherModifier animationAttributesForLayoutElement:]
- -[SBContinuousExposeWindowDragSwitcherModifier appLayoutByAddingAppLayout:toAppLayout:]
- -[SBContinuousExposeWindowDragSwitcherModifier appLayoutContainingAppLayout:]
- -[SBContinuousExposeWindowDragSwitcherModifier appLayoutOnStage]
- -[SBContinuousExposeWindowDragSwitcherModifier appLayout]
- -[SBContinuousExposeWindowDragSwitcherModifier asyncRenderingAttributesForAppLayout:]
- -[SBContinuousExposeWindowDragSwitcherModifier continuousExposeStripProgress]
- -[SBContinuousExposeWindowDragSwitcherModifier cornerRadiiForIndex:]
- -[SBContinuousExposeWindowDragSwitcherModifier descriptionBuilderWithMultilinePrefix:]
- -[SBContinuousExposeWindowDragSwitcherModifier didMoveToParentModifier:]
- -[SBContinuousExposeWindowDragSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:]
- -[SBContinuousExposeWindowDragSwitcherModifier frameForIndex:]
- -[SBContinuousExposeWindowDragSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:]
- -[SBContinuousExposeWindowDragSwitcherModifier handleEvent:]
- -[SBContinuousExposeWindowDragSwitcherModifier handleGestureEvent:]
- -[SBContinuousExposeWindowDragSwitcherModifier handleTransitionEvent:]
- -[SBContinuousExposeWindowDragSwitcherModifier hoveringOverAppLayout]
- -[SBContinuousExposeWindowDragSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:]
- -[SBContinuousExposeWindowDragSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:].cold.1
- -[SBContinuousExposeWindowDragSwitcherModifier initWithGestureID:initialAppLayout:selectedDisplayItem:].cold.2
- -[SBContinuousExposeWindowDragSwitcherModifier initialAppLayout]
- -[SBContinuousExposeWindowDragSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:]
- -[SBContinuousExposeWindowDragSwitcherModifier isSwitcherWindowUserInteractionEnabled]
- -[SBContinuousExposeWindowDragSwitcherModifier isSwitcherWindowVisible]
- -[SBContinuousExposeWindowDragSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:]
- -[SBContinuousExposeWindowDragSwitcherModifier perspectiveAngleForIndex:]
- -[SBContinuousExposeWindowDragSwitcherModifier preferredCenterForSelectedItemInDestinationModifier:clippingToInitialStageArea:]
- -[SBContinuousExposeWindowDragSwitcherModifier proposedAppLayout]
- -[SBContinuousExposeWindowDragSwitcherModifier scaleForIndex:]
- -[SBContinuousExposeWindowDragSwitcherModifier selectedDisplayItem]
- -[SBContinuousExposeWindowDragSwitcherModifier shadowStyleForLayoutRole:inAppLayout:]
- -[SBContinuousExposeWindowDragSwitcherModifier shouldPinLayoutRolesToSpace:]
- -[SBContinuousExposeWindowDragSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:]
- -[SBContinuousExposeWindowDragSwitcherModifier titleAndIconOpacityForIndex:]
- -[SBContinuousExposeWindowDragSwitcherModifier topMostLayoutElements]
- -[SBContinuousExposeWindowDragSwitcherModifier updateProposedAppLayoutWithAppLayout:andInitialAppLayout:]
- -[SBContinuousExposeWindowDragSwitcherModifier visibleAppLayouts]
- -[SBContinuousExposeWindowDragSwitcherModifier wallpaperGradientAttributesForLayoutRole:inAppLayout:]
- -[SBContinuousExposeWindowDragSwitcherModifier wantsSceneResizesHostedContextForAppLayout:]
- -[SBControlCenterController medusaHostedKeyboardWindowLevelAssertion]
- -[SBControlCenterController setMedusaHostedKeyboardWindowLevelAssertion:]
- -[SBDashBoardLockScreenEnvironment willUIUnlockFromSource:]
- -[SBDestroyDisplayItemSwitcherEventResponse initWithDisplayItem:]
- -[SBDestroyDisplayItemSwitcherEventResponse initWithDisplayItem:].cold.1
- -[SBDisplayItemLayoutAttributesCalculator _autoLayoutController]
- -[SBDisplayItemLayoutAttributesCalculator autoLayoutSpaceForAppLayout:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:]
- -[SBDragAndDropWorkspaceTransaction _sizeForFloatingApplication]
- -[SBDynamicLightingController initWithBacklightController:]
- -[SBFlexibleWindowingAutoLayoutItem continuousExposeAutoLayoutItemRepresentation]
- -[SBFlexibleWindowingAutoLayoutSpace continuousExposeAutoLayoutSpaceRepresentation]
- -[SBFlexibleWindowingWindowDragSwitcherModifier homeScreenDimmingAlpha]
- -[SBFluidSwitcherGestureManager _currentAutoLayoutSpace]
- -[SBFullScreenContinuousExposeSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:]
- -[SBFullScreenContinuousExposeSwitcherModifier highlightedByHoverAppLayouts]
- -[SBFullScreenContinuousExposeSwitcherModifier highlightedByTouchAppLayouts]
- -[SBFullScreenContinuousExposeSwitcherModifier scaleForLayoutRole:inAppLayout:]
- -[SBFullScreenContinuousExposeSwitcherModifier setHighlightedByHoverAppLayouts:]
- -[SBFullScreenContinuousExposeSwitcherModifier setHighlightedByTouchAppLayouts:]
- -[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]
- -[SBHeartbeatMetric .cxx_destruct]
- -[SBHeartbeatMetric _makePayloadFromMetricsByDatestamp:]
- -[SBHeartbeatMetric calendar]
- -[SBHeartbeatMetric dateFormatter]
- -[SBHeartbeatMetric handleEvent:withContext:]
- -[SBHeartbeatMetric heartbeatMetricPersistence]
- -[SBHeartbeatMetric initWithPersistence:]
- -[SBHeartbeatMetric sendCoreAnalyticsEventWithName:payload:]
- -[SBHeartbeatMetricPersistence _queue_initializeIfNeeded]
- -[SBHeartbeatMetricPersistence _queue_scheduleWriteIfNeeded]
- -[SBHeartbeatMetricPersistence _queue_writeToPersistenceURL]
- -[SBHeartbeatMetricPersistence initWithPersistenceURL:persistenceDelay:persistenceLeeway:]
- -[SBHeartbeatMetricPersistence metricsByDatestamp]
- -[SBHeartbeatMetricPersistence migrateDataFromDefaultsIfNeeded:]
- -[SBHeartbeatMetricPersistence persistenceDelay]
- -[SBHeartbeatMetricPersistence persistenceLeeway]
- -[SBHeartbeatMetricPersistence trackInteractionWithFeatureNamed:]
- -[SBHeartbeatMetricPersistence trackInteractionWithFeatureNamed:duration:]
- -[SBIconModel insertOSMigrationHomeScreenLayoutItem:intoListAtIndex:inFolder:rootFolder:referenceGridSize:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier .cxx_destruct]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _canShowReopenClosedWindowsButton]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _inlineAppExposeAppLayouts]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _inlineAppExposeSwitcherFrame]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _maximumNumberOfInlineAppExposeAppLayouts]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _maximumNumberOfInlineAppExposeColumns]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _maximumNumberOfInlineAppExposeRows]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _numberOfInlineAppExposeAppLayouts]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _numberOfInlineAppExposeColumns]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _numberOfInlineAppExposeRows]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _responseToUpdateReopenClosedWindowsButtonPresenceIfNeeded]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _scaleForActiveAppLayoutLeafAppLayouts]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier _scaleForInlineAppExposeAppLayouts]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier activeAppLayout]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier activeCornersForTouchResizeForLayoutRole:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier adjustedAppLayoutsForAppLayouts:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier adjustedSpaceAccessoryViewFrame:forAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier appExposeAccessoryButtonsBundleIdentifier]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier appExposeAccessoryButtonsOverrideUserInterfaceStyle]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier appExposeBundleIdentifier]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier backgroundOpacityForIndex:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier cornerRadiiForIndex:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier dockProgress]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier frameForIndex:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier fullScreenAppLayoutModifier]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier handleHighlightEvent:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier handleInsertionEvent:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier handleTapAppLayoutEvent:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier handleTapAppLayoutHeaderEvent:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier handleTapOutsideToDismissEvent:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier handleTimerEvent:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier handleTransitionEvent:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier headerStyleForIndex:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier hiddenContentStatusBarPartsForLayoutRole:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier highlightedByHoverAppLayouts]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier highlightedByTouchAppLayouts]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier homeScreenAlpha]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier homeScreenBackdropBlurProgress]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier homeScreenBackdropBlurType]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier homeScreenDimmingAlpha]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier initWithActiveAppLayout:appExposeBundleIdentifier:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isContainerStatusBarVisible]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isFocusEnabledForAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isHomeAffordanceSupportedForAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isHomeScreenContentRequired]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isItemContainerPointerInteractionEnabled]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isItemResizingAllowedForLayoutRole:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isLayoutRoleDraggable:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isLayoutRoleEligibleForContentDragSpringLoading:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isLayoutRoleSelectable:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isResizeGrabberVisibleForAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isScrollEnabled]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isShowingReopenClosedWindowsButton]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier isWallpaperRequiredForSwitcher]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier maskedCornersForIndex:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier numberOfHiddenAppLayouts]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier occlusionStateForLayoutRole:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier plusButtonAlpha]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier plusButtonStyle]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier reopenClosedWindowsButtonAlpha]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier reopenClosedWindowsButtonScale]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier scaleForIndex:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier scaleForLayoutRole:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier setFullScreenAppLayoutModifier:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier setHighlightedByHoverAppLayouts:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier setHighlightedByTouchAppLayouts:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier setNumberOfHiddenAppLayouts:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier setShowingReopenClosedWindowsButton:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier shadowOpacityForLayoutRole:atIndex:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier shadowStyleForLayoutRole:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier shouldAccessoryDrawShadowForAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier shouldAllowContentViewTouchesForLayoutRole:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier shouldAnimateInsertionOrRemovalOfAppLayout:atIndex:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier shouldConfigureInAppDockHiddenAssertion]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier shouldPinLayoutRolesToSpace:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier shouldScrollViewBlockTouches]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier spaceAccessoryViewIconHitTestOutsetForAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier switcherHitTestsAsOpaque]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier titleAndIconOpacityForIndex:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier titleOpacityForIndex:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier touchBehaviorForLayoutRole:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier visibleAppLayouts]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier visibleCornersForTouchResizeForLayoutRole:inAppLayout:]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier wallpaperStyle]
- -[SBInlineAppExposeContinuousExposeSwitcherModifier wantsSpaceAccessoryViewPointerInteractionsForAppLayout:]
- -[SBItemResizeGestureSwitcherModifier .cxx_destruct]
- -[SBItemResizeGestureSwitcherModifier _animationSettingsForLayout]
- -[SBItemResizeGestureSwitcherModifier _convertToScreenRectFromSpaceRect:]
- -[SBItemResizeGestureSwitcherModifier _convertToSpaceRectFromScreenRect:]
- -[SBItemResizeGestureSwitcherModifier _initialScaledFrameInScreenCoordinatesForSelectedDisplayItemInAppLayout:]
- -[SBItemResizeGestureSwitcherModifier _isStripVisibleForCurrentAppLayout]
- -[SBItemResizeGestureSwitcherModifier _responseForGestureUpdateAtGestureEnd:]
- -[SBItemResizeGestureSwitcherModifier _responseForSceneSizeUpdateToSize:center:sceneUpdatesOnly:]
- -[SBItemResizeGestureSwitcherModifier _shouldUseSprings]
- -[SBItemResizeGestureSwitcherModifier activeCornersForTouchResizeForLayoutRole:inAppLayout:]
- -[SBItemResizeGestureSwitcherModifier animationAttributesForLayoutElement:]
- -[SBItemResizeGestureSwitcherModifier cornerRadiiForIndex:]
- -[SBItemResizeGestureSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:]
- -[SBItemResizeGestureSwitcherModifier handleGestureEvent:]
- -[SBItemResizeGestureSwitcherModifier handleGestureEvent:].cold.1
- -[SBItemResizeGestureSwitcherModifier handleSceneReadyEvent:]
- -[SBItemResizeGestureSwitcherModifier handleTransitionEvent:]
- -[SBItemResizeGestureSwitcherModifier initWithGestureID:]
- -[SBItemResizeGestureSwitcherModifier isContentStatusBarVisibleForIndex:]
- -[SBItemResizeGestureSwitcherModifier isItemResizingAllowedForLayoutRole:inAppLayout:]
- -[SBItemResizeGestureSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:]
- -[SBItemResizeGestureSwitcherModifier layoutRestrictionInfoForItem:]
- -[SBItemResizeGestureSwitcherModifier maskedCornersForIndex:]
- -[SBItemResizeGestureSwitcherModifier selectedAppLayout]
- -[SBItemResizeGestureSwitcherModifier topMostLayoutRolesForAppLayout:]
- -[SBItemResizeGestureSwitcherModifier wantsSceneResizesHostedContextForAppLayout:]
- -[SBLockScreenViewControllerBase willUIUnlockFromSource:]
- -[SBLoginAppContainerViewController willUIUnlockFromSource:]
- -[SBMainDisplayConfigurationTransformer transformDisplayConfiguration:].cold.2
- -[SBMainSwitcherControllerCoordinator switcherContentController:removeDisplayItemFromDesktop:]
- -[SBMainWorkspaceLayoutStateContingencyPlan transitionContextToUndoTransitionContext:]
- -[SBMedusaDecoratedDeviceApplicationSceneViewController topAffordanceViewController:handleActionType:]
- -[SBMedusaSwitcherDragMetric handleEvent:withContext:]
- -[SBMedusaWindowDragMetric handleEvent:withContext:]
- -[SBMenuBarManager _setMenuBarVisible:animated:]
- -[SBMenuBarManager isPointInsideMenuBarContent:]
- -[SBMutableContinuousExposeAutoLayoutSpace autoLayoutItemForDisplayItem:]
- -[SBMutableContinuousExposeAutoLayoutSpace autoLayoutItemForDisplayItemIfExists:]
- -[SBRecordingIndicatorSystemApertureElement initWithInterSensorRegionIndicatorVisualRepresentation:microRegionIndicatorVisualRepresentation:recordingIndicatorManager:]
- -[SBRemoveFromDesktopSwitcherEventResponse displayItem]
- -[SBRemoveFromDesktopSwitcherEventResponse initWithDisplayItem:]
- -[SBRemoveFromDesktopSwitcherEventResponse initWithDisplayItem:].cold.1
- -[SBRootSceneWindow .cxx_destruct]
- -[SBRootSceneWindow _configureRootLayer:sceneTransformLayer:transformLayer:]
- -[SBRootSceneWindow _updateRootLayerBackgroundColor]
- -[SBRootSceneWindow backgroundColor]
- -[SBRootSceneWindow bezelLayer]
- -[SBRootSceneWindow initWithDisplayConfiguration:]
- -[SBRootSceneWindow layerForBackgroundColor]
- -[SBRootSceneWindow maskLayer]
- -[SBRootSceneWindow traitCollectionDidChange:]
- -[SBSAIndicatorAppearanceStateTransitionProvider preferencesFromContext:].cold.6
- -[SBSAIndicatorAppearanceStateTransitionProvider preferencesFromContext:].cold.7
- -[SBSAIndicatorElementContext _setInterSensorRegionMinimumDwellTimeSatisfied:]
- -[SBSAIndicatorElementContext interSensorRegionMinimumDwellTimeSatisfied]
- -[SBSAIndicatorElementContextMutator interSensorRegionMinimumDwellTimeSatisfied]
- -[SBSAIndicatorElementContextMutator setInterSensorRegionMinimumDwellTimeSatisfied:]
- -[SBScreenLongevitySettings attentionScoreThreshold]
- -[SBScreenLongevitySettings setAttentionScoreThreshold:]
- -[SBSecureIndicatorBacklightCoordinator _allowsBacklightChanges]
- -[SBSlideOverSessionMetric .cxx_destruct]
- -[SBSlideOverSessionMetric _bundleIdentifierForElementWithLayoutRole:fromContext:]
- -[SBSlideOverSessionMetric _sendCoreAnalyticsEventWithStartReason:endReason:duration:floatingBundleIdentifier:doNotDisturbActive:hardwareKeyboardAttached:]
- -[SBSlideOverSessionMetric floatingBundleIdentifier]
- -[SBSlideOverSessionMetric initWithHeartbeatMetricPersistence:]
- -[SBSlideOverSessionMetric sendCoreAnalyticsEventWithName:payload:]
- -[SBSlideOverSessionMetric setFloatingBundleIdentifier:]
- -[SBSlideOverSessionMetric setStartReason:]
- -[SBSlideOverSessionMetric setStartTimestamp:]
- -[SBSlideOverSessionMetric startReason]
- -[SBSlideOverSessionMetric startTimestamp]
- -[SBSplitViewSessionMetric .cxx_destruct]
- -[SBSplitViewSessionMetric _bundleIdentifierForElementWithLayoutRole:fromContext:]
- -[SBSplitViewSessionMetric _sendAggregateSessionCoreAnalyticsEventWithIdentifier:startReason:endReason:duration:doNotDisturbActive:hardwareKeyboardAttached:]
- -[SBSplitViewSessionMetric _sendIndividualSessionCoreAnalyticsEventWithAggregateIdentifier:startReason:endReason:duration:primaryBundleIdentifier:sideBundleIdentifier:doNotDisturbActive:hardwareKeyboardAttached:]
- -[SBSplitViewSessionMetric aggregateSessionIdentifier]
- -[SBSplitViewSessionMetric aggregateSessionStartReason]
- -[SBSplitViewSessionMetric aggregateSessionStartTimestamp]
- -[SBSplitViewSessionMetric individualSessionPrimaryBundleIdentifier]
- -[SBSplitViewSessionMetric individualSessionSideBundleIdentifier]
- -[SBSplitViewSessionMetric individualSessionStartReason]
- -[SBSplitViewSessionMetric individualSessionStartTimestamp]
- -[SBSplitViewSessionMetric initWithHeartbeatMetricPersistence:]
- -[SBSplitViewSessionMetric sendCoreAnalyticsEventWithName:payload:]
- -[SBSplitViewSessionMetric setAggregateSessionIdentifier:]
- -[SBSplitViewSessionMetric setAggregateSessionStartReason:]
- -[SBSplitViewSessionMetric setAggregateSessionStartTimestamp:]
- -[SBSplitViewSessionMetric setIndividualSessionPrimaryBundleIdentifier:]
- -[SBSplitViewSessionMetric setIndividualSessionSideBundleIdentifier:]
- -[SBSplitViewSessionMetric setIndividualSessionStartReason:]
- -[SBSplitViewSessionMetric setIndividualSessionStartTimestamp:]
- -[SBStripContinuousExposeSwitcherModifier .cxx_destruct]
- -[SBStripContinuousExposeSwitcherModifier _appStripOriginX]
- -[SBStripContinuousExposeSwitcherModifier _cachedOrFallbackFrameForIndex:cacheValidityToken:]
- -[SBStripContinuousExposeSwitcherModifier _cachedOrFallbackScaleForIndex:cacheValidityToken:]
- -[SBStripContinuousExposeSwitcherModifier _currentLayoutCalculationsValidityToken]
- -[SBStripContinuousExposeSwitcherModifier _highlightScaleForAppLayout:]
- -[SBStripContinuousExposeSwitcherModifier _indexInContinuousExposeIdentifierPileForAppLayout:]
- -[SBStripContinuousExposeSwitcherModifier _invalidateAppStripOriginX]
- -[SBStripContinuousExposeSwitcherModifier _isAppLayoutEffectivelyOnStage:]
- -[SBStripContinuousExposeSwitcherModifier _isGroupForAppLayoutHighlightedFromHover:]
- -[SBStripContinuousExposeSwitcherModifier _isGroupForAppLayoutHighlightedFromTouch:]
- -[SBStripContinuousExposeSwitcherModifier _orderedVisibleAppLayoutsIgnoringProgress:]
- -[SBStripContinuousExposeSwitcherModifier _positionForPositionIn3DContainerSpace:layerPosition:layerSize:layerAnchorPoint:layerTransform:containerPerspective:]
- -[SBStripContinuousExposeSwitcherModifier _stripScreenEdgePadding]
- -[SBStripContinuousExposeSwitcherModifier _wallpaperDimmingForIndex:]
- -[SBStripContinuousExposeSwitcherModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:]
- -[SBStripContinuousExposeSwitcherModifier adjustedSpaceAccessoryViewScale:forAppLayout:]
- -[SBStripContinuousExposeSwitcherModifier anchorPointForIndex:]
- -[SBStripContinuousExposeSwitcherModifier animationAttributesForLayoutElement:]
- -[SBStripContinuousExposeSwitcherModifier appLayoutsForContinuousExposeIdentifier:]
- -[SBStripContinuousExposeSwitcherModifier backgroundOpacityForIndex:]
- -[SBStripContinuousExposeSwitcherModifier buildLayoutCalculationsForCache:]
- -[SBStripContinuousExposeSwitcherModifier contentPageViewScaleForAppLayout:withScale:]
- -[SBStripContinuousExposeSwitcherModifier cornerRadiiForIndex:]
- -[SBStripContinuousExposeSwitcherModifier destinationAppLayoutForDismissingCurrentMode]
- -[SBStripContinuousExposeSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:]
- -[SBStripContinuousExposeSwitcherModifier frameForIndex:]
- -[SBStripContinuousExposeSwitcherModifier handleEvent:]
- -[SBStripContinuousExposeSwitcherModifier handleHighlightEvent:]
- -[SBStripContinuousExposeSwitcherModifier headerStyleForIndex:]
- -[SBStripContinuousExposeSwitcherModifier highlightedByHoverAppLayouts]
- -[SBStripContinuousExposeSwitcherModifier highlightedByTouchAppLayouts]
- -[SBStripContinuousExposeSwitcherModifier inactiveAppLayoutsReachableByKeyboardShortcut]
- -[SBStripContinuousExposeSwitcherModifier init]
- -[SBStripContinuousExposeSwitcherModifier isContinuousExposeConfigurationChangeTransition]
- -[SBStripContinuousExposeSwitcherModifier isHomeAffordanceSupportedForAppLayout:]
- -[SBStripContinuousExposeSwitcherModifier maskedCornersForIndex:]
- -[SBStripContinuousExposeSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:]
- -[SBStripContinuousExposeSwitcherModifier perspectiveAngleForIndex:]
- -[SBStripContinuousExposeSwitcherModifier scaleForIndex:]
- -[SBStripContinuousExposeSwitcherModifier setContinuousExposeConfigurationChangeTransition:]
- -[SBStripContinuousExposeSwitcherModifier setHighlightedByHoverAppLayouts:]
- -[SBStripContinuousExposeSwitcherModifier setHighlightedByTouchAppLayouts:]
- -[SBStripContinuousExposeSwitcherModifier shadowOpacityForLayoutRole:atIndex:]
- -[SBStripContinuousExposeSwitcherModifier shadowStyleForLayoutRole:inAppLayout:]
- -[SBStripContinuousExposeSwitcherModifier titleAndIconOpacityForIndex:]
- -[SBStripContinuousExposeSwitcherModifier titleOpacityForIndex:]
- -[SBStripContinuousExposeSwitcherModifier topMostLayoutElements]
- -[SBStripContinuousExposeSwitcherModifier visibleAppLayouts]
- -[SBStripContinuousExposeSwitcherModifier wallpaperGradientAttributesForLayoutRole:inAppLayout:]
- -[SBSwitcherController _removeDisplayItemFromDesktop:]
- -[SBSwitcherModifier(SharedModifierUtilities) autoLayoutSpaceForAppLayout:]
- -[SBSystemApertureSceneElement _layoutHostMayNotPerformLayoutUpdate]
- -[SBSystemApertureSettings indicatorContainerMinimumScale]
- -[SBSystemApertureSettings indicatorContainerSize]
- -[SBSystemApertureSettings setIndicatorContainerMinimumScale:]
- -[SBSystemApertureSettings setIndicatorContainerSize:]
- -[SBSystemApertureViewController _handleIndicatorAppearanceStateContextChanges:]
- -[SBSystemApertureViewController _interSensorRegionMinimumDwellTimeTimerFired]
- -[SBTopAffordanceMenuInteractionMetric handleEvent:withContext:]
- -[SBTopAffordanceViewController _emitAnalyticsEventForMenuInteraction:]
- -[SpringBoard _handleCommandQ:]
- -[UISMutableApplicationInitializationContext(DeviceEmulation) sb_configureForDeviceEmulation]
- -[UISMutableDeviceContext(DeviceEmulation) sb_configureForDeviceEmulation]
- -[UISMutableDisplayContext(DeviceEmulation) sb_configureForDeviceEmulation]
- GCC_except_table114
- GCC_except_table163
- GCC_except_table189
- GCC_except_table192
- GCC_except_table195
- GCC_except_table198
- GCC_except_table201
- GCC_except_table223
- GCC_except_table233
- GCC_except_table263
- GCC_except_table267
- GCC_except_table269
- GCC_except_table272
- GCC_except_table275
- GCC_except_table276
- GCC_except_table278
- GCC_except_table303
- GCC_except_table306
- GCC_except_table315
- GCC_except_table316
- GCC_except_table318
- GCC_except_table329
- GCC_except_table349
- GCC_except_table362
- GCC_except_table364
- GCC_except_table379
- GCC_except_table384
- GCC_except_table385
- GCC_except_table390
- GCC_except_table393
- GCC_except_table394
- GCC_except_table396
- GCC_except_table403
- GCC_except_table423
- GCC_except_table444
- GCC_except_table467
- GCC_except_table475
- GCC_except_table479
- GCC_except_table499
- GCC_except_table507
- GCC_except_table509
- GCC_except_table514
- GCC_except_table516
- GCC_except_table528
- GCC_except_table531
- GCC_except_table535
- GCC_except_table541
- GCC_except_table545
- GCC_except_table569
- GCC_except_table615
- GCC_except_table650
- GCC_except_table720
- GCC_except_table744
- GCC_except_table788
- GCC_except_table828
- GCC_except_table867
- GCC_except_table876
- GCC_except_table920
- GCC_except_table959
- GCC_except_table966
- GCC_except_table968
- GCC_except_table970
- GCC_except_table972
- GCC_except_table974
- GCC_except_table976
- GCC_except_table978
- _CARenderServerFlushIRDC
- _CGRegionGetBoundingBox
- _FBSDisplayRotationFromRadians
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_NSISO8601DateFormatter
- _OBJC_CLASS_$_SBCenterWindowSessionMetric
- _OBJC_CLASS_$_SBContinuousExposeAutoLayoutController
- _OBJC_CLASS_$_SBContinuousExposeAutoLayoutItem
- _OBJC_CLASS_$_SBContinuousExposeAutoLayoutSpace
- _OBJC_CLASS_$_SBContinuousExposeWindowDragSwitcherModifier
- _OBJC_CLASS_$_SBDeviceEmulationController
- _OBJC_CLASS_$_SBHeartbeatMetric
- _OBJC_CLASS_$_SBInlineAppExposeContinuousExposeSwitcherModifier
- _OBJC_CLASS_$_SBItemResizeGestureSwitcherModifier
- _OBJC_CLASS_$_SBMedusaSwitcherDragMetric
- _OBJC_CLASS_$_SBMedusaWindowDragMetric
- _OBJC_CLASS_$_SBMutableContinuousExposeAutoLayoutItem
- _OBJC_CLASS_$_SBMutableContinuousExposeAutoLayoutSpace
- _OBJC_CLASS_$_SBSlideOverSessionMetric
- _OBJC_CLASS_$_SBSplitViewSessionMetric
- _OBJC_CLASS_$_SBStripContinuousExposeSwitcherModifier
- _OBJC_CLASS_$_SBTopAffordanceMenuInteractionMetric
- _OBJC_IVAR_$_SBAppLayout._cachedLastAutoLayoutSpace
- _OBJC_IVAR_$_SBCenterWindowSessionMetric._centerBundleIdentifier
- _OBJC_IVAR_$_SBCenterWindowSessionMetric._startReason
- _OBJC_IVAR_$_SBCenterWindowSessionMetric._startTimestamp
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutController._reentrancyGuard
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutItem._anchorPosition
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutItem._compactedPosition
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutItem._displayItem
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutItem._fullyOccluded
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutItem._inDefaultPosition
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutItem._overlapped
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutItem._partiallyCoveredByPeekingItem
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutItem._position
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutItem._size
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutItem._unoccludedPeekingPosition
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutSpace._boundingBox
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutSpace._compactedBoundingBox
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutSpace._configuration
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutSpace._items
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutSpace._stageArea
- _OBJC_IVAR_$_SBContinuousExposeAutoLayoutSpace._stripVisible
- _OBJC_IVAR_$_SBContinuousExposeWindowDragContainerSwitcherModifier._windowDragModifier
- _OBJC_IVAR_$_SBContinuousExposeWindowDragDestinationSwitcherModifier._initialAutoLayoutSpace
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._anchorPoint
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._anchorPointRampingProperty
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._autoLayoutController
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._destinationModifier
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._dragBeganInAnyStrip
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._dragBeganInOtherSwitcher
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._dragBeganInOurSwitcher
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._dragBeganOnAnyStage
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._gestureWasCanceled
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._initialAnchorPoint
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._initialAppLayout
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._initialAutoLayoutSpace
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._location
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._previousAutoLayoutSpace
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._selectedDisplayItem
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._sizeOfSelectedDisplayItem
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._stageRubberbandingRampingProperty
- _OBJC_IVAR_$_SBContinuousExposeWindowDragSwitcherModifier._stageRubberbandingSettings
- _OBJC_IVAR_$_SBControlCenterController._medusaHostedKeyboardWindowLevelAssertion
- _OBJC_IVAR_$_SBDisplayItemLayoutAttributesCalculator._cached_autoLayoutController
- _OBJC_IVAR_$_SBDragAndDropWorkspaceTransaction._cachedSizeForFloatingApplication
- _OBJC_IVAR_$_SBFileStackOpenIndicatorView._backgroundView
- _OBJC_IVAR_$_SBFileStackOpenIndicatorView._foregroundImage
- _OBJC_IVAR_$_SBFileStackOpenIndicatorView._xColorBurnView
- _OBJC_IVAR_$_SBFileStackOpenIndicatorView._xPlusDView
- _OBJC_IVAR_$_SBFullScreenContinuousExposeSwitcherModifier._continuousExposeStripModifierIfExists
- _OBJC_IVAR_$_SBHeartbeatMetric._calendar
- _OBJC_IVAR_$_SBHeartbeatMetric._dateFormatter
- _OBJC_IVAR_$_SBHeartbeatMetric._heartbeatMetricPersistence
- _OBJC_IVAR_$_SBHeartbeatMetricPersistence._persistenceDelay
- _OBJC_IVAR_$_SBHeartbeatMetricPersistence._persistenceLeeway
- _OBJC_IVAR_$_SBHeartbeatMetricPersistence._queue
- _OBJC_IVAR_$_SBHeartbeatMetricPersistence._queue_calendar
- _OBJC_IVAR_$_SBHeartbeatMetricPersistence._queue_dateFormatter
- _OBJC_IVAR_$_SBHeartbeatMetricPersistence._queue_metricsByDatestamp
- _OBJC_IVAR_$_SBHeartbeatMetricPersistence._queue_persistenceTimer
- _OBJC_IVAR_$_SBHomeScreenContinuousExposeSwitcherModifier._continuousExposeStripModifierIfExists
- _OBJC_IVAR_$_SBInlineAppExposeContinuousExposeSwitcherModifier._activeAppLayout
- _OBJC_IVAR_$_SBInlineAppExposeContinuousExposeSwitcherModifier._appExposeBundleIdentifier
- _OBJC_IVAR_$_SBInlineAppExposeContinuousExposeSwitcherModifier._fullScreenAppLayoutModifier
- _OBJC_IVAR_$_SBInlineAppExposeContinuousExposeSwitcherModifier._highlightedByHoverAppLayouts
- _OBJC_IVAR_$_SBInlineAppExposeContinuousExposeSwitcherModifier._highlightedByTouchAppLayouts
- _OBJC_IVAR_$_SBInlineAppExposeContinuousExposeSwitcherModifier._numberOfHiddenAppLayouts
- _OBJC_IVAR_$_SBInlineAppExposeContinuousExposeSwitcherModifier._showingReopenClosedWindowsButton
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._autoLayoutController
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._currentActiveResizeCorner
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._currentAppLayout
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._currentFrameForDrawingInScreenCoordinates
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._currentSceneSize
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._initialFrameInScreenCoordinates
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._layoutGrid
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._location
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._locationEdgeAdjustment
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._resizeAnchor
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._selectedEdge
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._selectedItemWasInitiallyInDefaultPosition
- _OBJC_IVAR_$_SBItemResizeGestureSwitcherModifier._selectedLayoutRole
- _OBJC_IVAR_$_SBRemoveFromDesktopSwitcherEventResponse._displayItem
- _OBJC_IVAR_$_SBRootSceneWindow._backgroundColor
- _OBJC_IVAR_$_SBRootSceneWindow._bezelLayer
- _OBJC_IVAR_$_SBRootSceneWindow._layerForBackgroundColor
- _OBJC_IVAR_$_SBRootSceneWindow._maskLayer
- _OBJC_IVAR_$_SBSAIndicatorElementContext._interSensorRegionMinimumDwellTimeSatisfied
- _OBJC_IVAR_$_SBSAIndicatorLayoutProvider._isMicroSupported
- _OBJC_IVAR_$_SBScreenLongevitySettings._attentionScoreThreshold
- _OBJC_IVAR_$_SBSlideOverSessionMetric._floatingBundleIdentifier
- _OBJC_IVAR_$_SBSlideOverSessionMetric._startReason
- _OBJC_IVAR_$_SBSlideOverSessionMetric._startTimestamp
- _OBJC_IVAR_$_SBSplitViewSessionMetric._aggregateSessionIdentifier
- _OBJC_IVAR_$_SBSplitViewSessionMetric._aggregateSessionStartReason
- _OBJC_IVAR_$_SBSplitViewSessionMetric._aggregateSessionStartTimestamp
- _OBJC_IVAR_$_SBSplitViewSessionMetric._individualSessionPrimaryBundleIdentifier
- _OBJC_IVAR_$_SBSplitViewSessionMetric._individualSessionSideBundleIdentifier
- _OBJC_IVAR_$_SBSplitViewSessionMetric._individualSessionStartReason
- _OBJC_IVAR_$_SBSplitViewSessionMetric._individualSessionStartTimestamp
- _OBJC_IVAR_$_SBStripContinuousExposeSwitcherModifier._cached_appStripOriginX
- _OBJC_IVAR_$_SBStripContinuousExposeSwitcherModifier._cached_appStripUnocclusionProgress
- _OBJC_IVAR_$_SBStripContinuousExposeSwitcherModifier._continuousExposeConfigurationChangeTransition
- _OBJC_IVAR_$_SBStripContinuousExposeSwitcherModifier._highlightedByHoverAppLayouts
- _OBJC_IVAR_$_SBStripContinuousExposeSwitcherModifier._highlightedByTouchAppLayouts
- _OBJC_IVAR_$_SBStripContinuousExposeSwitcherModifier._modifierEventGenCount
- _OBJC_IVAR_$_SBStripContinuousExposeSwitcherModifier._requireStripContentsInViewHierarchy
- _OBJC_IVAR_$_SBStripContinuousExposeSwitcherModifier._stripLayoutCache
- _OBJC_IVAR_$_SBSystemApertureSettings._indicatorContainerMinimumScale
- _OBJC_IVAR_$_SBSystemApertureSettings._indicatorContainerSize
- _OBJC_IVAR_$_SBSystemApertureViewController._interSensorRegionMinimumDwellTimeSatisfied
- _OBJC_IVAR_$_SBSystemApertureViewController._temporaryInterSensorRegionMinimumDwellTimeTimer
- _OBJC_METACLASS_$_SBCenterWindowSessionMetric
- _OBJC_METACLASS_$_SBContinuousExposeAutoLayoutController
- _OBJC_METACLASS_$_SBContinuousExposeAutoLayoutItem
- _OBJC_METACLASS_$_SBContinuousExposeAutoLayoutSpace
- _OBJC_METACLASS_$_SBContinuousExposeWindowDragSwitcherModifier
- _OBJC_METACLASS_$_SBDeviceEmulationController
- _OBJC_METACLASS_$_SBHeartbeatMetric
- _OBJC_METACLASS_$_SBInlineAppExposeContinuousExposeSwitcherModifier
- _OBJC_METACLASS_$_SBItemResizeGestureSwitcherModifier
- _OBJC_METACLASS_$_SBMedusaSwitcherDragMetric
- _OBJC_METACLASS_$_SBMedusaWindowDragMetric
- _OBJC_METACLASS_$_SBMutableContinuousExposeAutoLayoutItem
- _OBJC_METACLASS_$_SBMutableContinuousExposeAutoLayoutSpace
- _OBJC_METACLASS_$_SBSlideOverSessionMetric
- _OBJC_METACLASS_$_SBSplitViewSessionMetric
- _OBJC_METACLASS_$_SBStripContinuousExposeSwitcherModifier
- _OBJC_METACLASS_$_SBTopAffordanceMenuInteractionMetric
- _SBFIsIRDCResetAvailable
- _SBHeartbeatMetricPersistenceFeatureNameCenterWindowSession
- _SBHeartbeatMetricPersistenceFeatureNameSlideOverSession
- _SBHeartbeatMetricPersistenceFeatureNameSplitViewSession
- _SBHeartbeatMetricPersistenceKeyCounts
- _SBHeartbeatMetricPersistenceKeyDurations
- _UIImageSymbolSizeLarge
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableApplicationInitializationContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDeviceContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_INSTANCE_METHODS_UISMutableDisplayContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_UISMutableApplicationInitializationContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_UISMutableDeviceContext_$_DeviceEmulation
- __OBJC_$_CATEGORY_UISMutableDisplayContext_$_DeviceEmulation
- __OBJC_$_CLASS_METHODS_SBDeviceEmulationController
- __OBJC_$_CLASS_PROP_LIST_SBDeviceEmulationController
- __OBJC_$_INSTANCE_METHODS_NSObject(SBSceneLayoutStatusBarAssertionProvidingAdditions|SBSAGeometricTypeAnimationDecomposing|SBApplicationSceneStatusBarDescribingAdditions|SBMainDisplaySceneLayoutElementViewControllingAdditions|SBSwitcherModifierDebugTimelineDescription|SBMedusaDecoratedDeviceApplicationSceneViewControllingAdditions)
- __OBJC_$_INSTANCE_METHODS_SBCenterWindowSessionMetric
- __OBJC_$_INSTANCE_METHODS_SBContinuousExposeAutoLayoutController
- __OBJC_$_INSTANCE_METHODS_SBContinuousExposeAutoLayoutItem
- __OBJC_$_INSTANCE_METHODS_SBContinuousExposeAutoLayoutSpace
- __OBJC_$_INSTANCE_METHODS_SBContinuousExposeWindowDragSwitcherModifier
- __OBJC_$_INSTANCE_METHODS_SBHeartbeatMetric
- __OBJC_$_INSTANCE_METHODS_SBInlineAppExposeContinuousExposeSwitcherModifier
- __OBJC_$_INSTANCE_METHODS_SBItemResizeGestureSwitcherModifier
- __OBJC_$_INSTANCE_METHODS_SBMedusaSwitcherDragMetric
- __OBJC_$_INSTANCE_METHODS_SBMedusaWindowDragMetric
- __OBJC_$_INSTANCE_METHODS_SBMutableContinuousExposeAutoLayoutSpace
- __OBJC_$_INSTANCE_METHODS_SBRootSceneWindow
- __OBJC_$_INSTANCE_METHODS_SBSlideOverSessionMetric
- __OBJC_$_INSTANCE_METHODS_SBSplitViewSessionMetric
- __OBJC_$_INSTANCE_METHODS_SBStripContinuousExposeSwitcherModifier
- __OBJC_$_INSTANCE_METHODS_SBTopAffordanceMenuInteractionMetric
- __OBJC_$_INSTANCE_VARIABLES_SBCenterWindowSessionMetric
- __OBJC_$_INSTANCE_VARIABLES_SBContinuousExposeAutoLayoutController
- __OBJC_$_INSTANCE_VARIABLES_SBContinuousExposeAutoLayoutItem
- __OBJC_$_INSTANCE_VARIABLES_SBContinuousExposeAutoLayoutSpace
- __OBJC_$_INSTANCE_VARIABLES_SBContinuousExposeWindowDragSwitcherModifier
- __OBJC_$_INSTANCE_VARIABLES_SBHeartbeatMetric
- __OBJC_$_INSTANCE_VARIABLES_SBInlineAppExposeContinuousExposeSwitcherModifier
- __OBJC_$_INSTANCE_VARIABLES_SBItemResizeGestureSwitcherModifier
- __OBJC_$_INSTANCE_VARIABLES_SBRootSceneWindow
- __OBJC_$_INSTANCE_VARIABLES_SBSAIndicatorLayoutProvider
- __OBJC_$_INSTANCE_VARIABLES_SBSlideOverSessionMetric
- __OBJC_$_INSTANCE_VARIABLES_SBSplitViewSessionMetric
- __OBJC_$_INSTANCE_VARIABLES_SBStripContinuousExposeSwitcherModifier
- __OBJC_$_PROP_LIST_SBCenterWindowSessionMetric
- __OBJC_$_PROP_LIST_SBContinuousExposeAutoLayoutItem
- __OBJC_$_PROP_LIST_SBContinuousExposeAutoLayoutSpace
- __OBJC_$_PROP_LIST_SBContinuousExposeWindowDragSwitcherModifier
- __OBJC_$_PROP_LIST_SBHeartbeatMetric
- __OBJC_$_PROP_LIST_SBInlineAppExposeContinuousExposeSwitcherModifier
- __OBJC_$_PROP_LIST_SBItemResizeGestureSwitcherModifier
- __OBJC_$_PROP_LIST_SBMedusaSwitcherDragMetric
- __OBJC_$_PROP_LIST_SBMedusaWindowDragMetric
- __OBJC_$_PROP_LIST_SBMutableContinuousExposeAutoLayoutItem
- __OBJC_$_PROP_LIST_SBMutableContinuousExposeAutoLayoutSpace
- __OBJC_$_PROP_LIST_SBRootSceneWindow
- __OBJC_$_PROP_LIST_SBSlideOverSessionMetric
- __OBJC_$_PROP_LIST_SBSplitViewSessionMetric
- __OBJC_$_PROP_LIST_SBStripContinuousExposeSwitcherModifier
- __OBJC_$_PROP_LIST_SBTopAffordanceMenuInteractionMetric
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBIconViewShortcutsDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBWindowDragSwitcherModifying
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBIconViewShortcutsDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SBWindowDragSwitcherModifying
- __OBJC_$_PROTOCOL_REFS_SBIconViewShortcutsDelegate
- __OBJC_CLASS_PROTOCOLS_$_SBContinuousExposeAutoLayoutItem
- __OBJC_CLASS_PROTOCOLS_$_SBContinuousExposeAutoLayoutSpace
- __OBJC_CLASS_PROTOCOLS_$_SBContinuousExposeWindowDragSwitcherModifier
- __OBJC_CLASS_PROTOCOLS_$_SBHeartbeatMetric
- __OBJC_CLASS_PROTOCOLS_$_SBMedusaSwitcherDragMetric
- __OBJC_CLASS_PROTOCOLS_$_SBMedusaWindowDragMetric
- __OBJC_CLASS_PROTOCOLS_$_SBStripContinuousExposeSwitcherModifier
- __OBJC_CLASS_PROTOCOLS_$_SBTopAffordanceMenuInteractionMetric
- __OBJC_CLASS_RO_$_SBCenterWindowSessionMetric
- __OBJC_CLASS_RO_$_SBContinuousExposeAutoLayoutController
- __OBJC_CLASS_RO_$_SBContinuousExposeAutoLayoutItem
- __OBJC_CLASS_RO_$_SBContinuousExposeAutoLayoutSpace
- __OBJC_CLASS_RO_$_SBContinuousExposeWindowDragSwitcherModifier
- __OBJC_CLASS_RO_$_SBDeviceEmulationController
- __OBJC_CLASS_RO_$_SBHeartbeatMetric
- __OBJC_CLASS_RO_$_SBInlineAppExposeContinuousExposeSwitcherModifier
- __OBJC_CLASS_RO_$_SBItemResizeGestureSwitcherModifier
- __OBJC_CLASS_RO_$_SBMedusaSwitcherDragMetric
- __OBJC_CLASS_RO_$_SBMedusaWindowDragMetric
- __OBJC_CLASS_RO_$_SBMutableContinuousExposeAutoLayoutItem
- __OBJC_CLASS_RO_$_SBMutableContinuousExposeAutoLayoutSpace
- __OBJC_CLASS_RO_$_SBSlideOverSessionMetric
- __OBJC_CLASS_RO_$_SBSplitViewSessionMetric
- __OBJC_CLASS_RO_$_SBStripContinuousExposeSwitcherModifier
- __OBJC_CLASS_RO_$_SBTopAffordanceMenuInteractionMetric
- __OBJC_LABEL_PROTOCOL_$_SBIconViewShortcutsDelegate
- __OBJC_LABEL_PROTOCOL_$_SBWindowDragSwitcherModifying
- __OBJC_METACLASS_RO_$_SBCenterWindowSessionMetric
- __OBJC_METACLASS_RO_$_SBContinuousExposeAutoLayoutController
- __OBJC_METACLASS_RO_$_SBContinuousExposeAutoLayoutItem
- __OBJC_METACLASS_RO_$_SBContinuousExposeAutoLayoutSpace
- __OBJC_METACLASS_RO_$_SBContinuousExposeWindowDragSwitcherModifier
- __OBJC_METACLASS_RO_$_SBDeviceEmulationController
- __OBJC_METACLASS_RO_$_SBHeartbeatMetric
- __OBJC_METACLASS_RO_$_SBInlineAppExposeContinuousExposeSwitcherModifier
- __OBJC_METACLASS_RO_$_SBItemResizeGestureSwitcherModifier
- __OBJC_METACLASS_RO_$_SBMedusaSwitcherDragMetric
- __OBJC_METACLASS_RO_$_SBMedusaWindowDragMetric
- __OBJC_METACLASS_RO_$_SBMutableContinuousExposeAutoLayoutItem
- __OBJC_METACLASS_RO_$_SBMutableContinuousExposeAutoLayoutSpace
- __OBJC_METACLASS_RO_$_SBSlideOverSessionMetric
- __OBJC_METACLASS_RO_$_SBSplitViewSessionMetric
- __OBJC_METACLASS_RO_$_SBStripContinuousExposeSwitcherModifier
- __OBJC_METACLASS_RO_$_SBTopAffordanceMenuInteractionMetric
- __OBJC_PROTOCOL_$_SBIconViewShortcutsDelegate
- __OBJC_PROTOCOL_$_SBWindowDragSwitcherModifying
- ___105-[SBContinuousExposeWindowDragSwitcherModifier _beginStageRubberbandingRampingPropertyWithMode:settings:]_block_invoke
- ___105-[SBContinuousExposeWindowDragSwitcherModifier _beginStageRubberbandingRampingPropertyWithMode:settings:]_block_invoke_2
- ___107-[SBContinuousExposeWindowDragSwitcherModifier _beginAnimatingAnchorPointRampingPropertyWithMode:settings:]_block_invoke
- ___107-[SBContinuousExposeWindowDragSwitcherModifier _beginAnimatingAnchorPointRampingPropertyWithMode:settings:]_block_invoke_2
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke.315
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_2.316
- ___108-[SBMainSwitcherControllerCoordinator switcherContentController:reopenHiddenAppLayoutsWithBundleIdentifier:]_block_invoke_3.317
- ___111-[SBInlineAppExposeContinuousExposeSwitcherModifier _responseToUpdateReopenClosedWindowsButtonPresenceIfNeeded]_block_invoke
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.645
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.647
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke_10
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke_11
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke_12
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke_2
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke_3
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke_4
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke_5
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke_6
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke_7
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke_8
- ___166-[SBContinuousExposeAutoLayoutController _snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:]_block_invoke_9
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1213
- ___48-[SBMenuBarManager _setMenuBarVisible:animated:]_block_invoke
- ___48-[SBMenuBarManager _setMenuBarVisible:animated:]_block_invoke_2
- ___48-[SBMenuBarManager _setMenuBarVisible:animated:]_block_invoke_3
- ___48-[SBMenuBarManager _setMenuBarVisible:animated:]_block_invoke_4
- ___50-[SBHeartbeatMetricPersistence metricsByDatestamp]_block_invoke
- ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.85
- ___52-[SBMedusaWindowDragMetric handleEvent:withContext:]_block_invoke
- ___52-[SBMedusaWindowDragMetric handleEvent:withContext:]_block_invoke_2
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.754
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.785
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.816
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.922
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.809
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.926
- ___54-[SBMedusaSwitcherDragMetric handleEvent:withContext:]_block_invoke
- ___54-[SBMedusaSwitcherDragMetric handleEvent:withContext:]_block_invoke_2
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1758
- ___57-[SBActivityBannerObserver _handleActivityAlert:present:]_block_invoke
- ___57-[SBSAKeyLinePreferencesProvider preferencesFromContext:]_block_invoke_6
- ___57-[SBSAKeyLinePreferencesProvider preferencesFromContext:]_block_invoke_6.cold.1
- ___57-[SBSAKeyLinePreferencesProvider preferencesFromContext:]_block_invoke_7
- ___57-[SBSAKeyLinePreferencesProvider preferencesFromContext:]_block_invoke_7.cold.1
- ___59-[SBDynamicLightingController initWithBacklightController:]_block_invoke
- ___59-[SBDynamicLightingController initWithBacklightController:]_block_invoke_2
- ___60-[SBHeartbeatMetric sendCoreAnalyticsEventWithName:payload:]_block_invoke
- ___60-[SBHeartbeatMetricPersistence _queue_scheduleWriteIfNeeded]_block_invoke
- ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.927
- ___63-[SBSlideOverSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke
- ___63-[SBSlideOverSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_2
- ___63-[SBSlideOverSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_3
- ___63-[SBSlideOverSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_4
- ___63-[SBSlideOverSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_5
- ___63-[SBSplitViewSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke
- ___63-[SBSplitViewSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_2
- ___63-[SBSplitViewSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_3
- ___63-[SBSplitViewSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_4
- ___63-[SBSplitViewSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_5
- ___64-[SBActivityManager _activityStartedOrUpdatedWithContentUpdate:]_block_invoke.43
- ___64-[SBHeartbeatMetricPersistence migrateDataFromDefaultsIfNeeded:]_block_invoke
- ___64-[SBTopAffordanceMenuInteractionMetric handleEvent:withContext:]_block_invoke
- ___64-[SBTopAffordanceMenuInteractionMetric handleEvent:withContext:]_block_invoke_2
- ___66-[SBCenterWindowSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke
- ___66-[SBCenterWindowSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_2
- ___66-[SBCenterWindowSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_3
- ___66-[SBCenterWindowSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_4
- ___66-[SBCenterWindowSessionMetric initWithHeartbeatMetricPersistence:]_block_invoke_5
- ___67-[SBContinuousExposeWindowDragSwitcherModifier handleGestureEvent:]_block_invoke
- ___67-[SBContinuousExposeWindowDragSwitcherModifier handleGestureEvent:]_block_invoke_2
- ___67-[SBContinuousExposeWindowDragSwitcherModifier handleGestureEvent:]_block_invoke_3
- ___67-[SBSlideOverSessionMetric sendCoreAnalyticsEventWithName:payload:]_block_invoke
- ___67-[SBSplitViewSessionMetric sendCoreAnalyticsEventWithName:payload:]_block_invoke
- ___68-[SBFluidSwitcherViewController _performDestroyDisplayItemResponse:]_block_invoke.cold.1
- ___69-[SBDashBoardEmergencyDialerViewController _updateEmergencyCallMode:]_block_invoke.43
- ___70-[SBCenterWindowSessionMetric sendCoreAnalyticsEventWithName:payload:]_block_invoke
- ___74-[SBFluidSwitcherViewController _performBlurthroughItemContainerResponse:]_block_invoke.1092
- ___74-[SBHeartbeatMetricPersistence trackInteractionWithFeatureNamed:duration:]_block_invoke
- ___74-[SBHeartbeatMetricPersistence trackInteractionWithFeatureNamed:duration:]_block_invoke_2
- ___74-[SBStripContinuousExposeSwitcherModifier _isAppLayoutEffectivelyOnStage:]_block_invoke
- ___75-[SBStripContinuousExposeSwitcherModifier buildLayoutCalculationsForCache:]_block_invoke
- ___77-[SBItemResizeGestureSwitcherModifier _responseForGestureUpdateAtGestureEnd:]_block_invoke
- ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke.19
- ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke.19.cold.1
- ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke.20
- ___77-[SBSADefaultIndicatorAppearanceStateContextProvider preferencesFromContext:]_block_invoke.20.cold.1
- ___78-[SBDashBoardEmergencyDialerViewController _activateEmergencyDialerController]_block_invoke.38
- ___79-[SBContinuousExposeAutoLayoutController _itemsSortedByXInSpace:configuration:]_block_invoke
- ___79-[SBContinuousExposeAutoLayoutController _itemsSortedByXInSpace:configuration:]_block_invoke_2
- ___79-[SBContinuousExposeAutoLayoutController _itemsSortedByXInSpace:configuration:]_block_invoke_3
- ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke.122
- ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_2.124
- ___80-[SBContinuousExposeWindowDragSwitcherModifier _appLayoutContainingDisplayItem:]_block_invoke
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_10
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_11
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_12
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_2
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_3
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_4
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_5
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_6
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_7
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_8
- ___80-[SBGlassBannerTransitionAnimator runAnimationsWithActions:animated:completion:]_block_invoke_9
- ___80-[SBSystemApertureViewController _handleIndicatorAppearanceStateContextChanges:]_block_invoke
- ___82-[SBSlideOverSessionMetric _bundleIdentifierForElementWithLayoutRole:fromContext:]_block_invoke
- ___82-[SBSplitViewSessionMetric _bundleIdentifierForElementWithLayoutRole:fromContext:]_block_invoke
- ___83-[SBFlexibleWindowingAutoLayoutSpace continuousExposeAutoLayoutSpaceRepresentation]_block_invoke
- ___83-[SBStripContinuousExposeSwitcherModifier appLayoutsForContinuousExposeIdentifier:]_block_invoke
- ___84-[SBLockScreenBiometricAuthenticationCoordinator _updateMatchingForState:forReason:]_block_invoke.223
- ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke.47
- ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke_2.48
- ___85-[SBCenterWindowSessionMetric _bundleIdentifierForElementWithLayoutRole:fromContext:]_block_invoke
- ___85-[SBInlineAppExposeContinuousExposeSwitcherModifier adjustedAppLayoutsForAppLayouts:]_block_invoke
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke.373
- ___86-[SBMainSwitcherControllerCoordinator _performSceneDestructionForModelRemovalResults:]_block_invoke_2.374
- ___86-[SBMainWorkspaceLayoutStateContingencyPlan transitionContextToUndoTransitionContext:]_block_invoke
- ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.81
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1610
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1612
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1614
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1618
- ___93-[SBStripContinuousExposeSwitcherModifier _cachedOrFallbackFrameForIndex:cacheValidityToken:]_block_invoke
- ___93-[SBStripContinuousExposeSwitcherModifier _cachedOrFallbackScaleForIndex:cacheValidityToken:]_block_invoke
- ___96-[SBContinuousExposeWindowDragSwitcherModifier _anyProposedAppLayoutContainsSelectedDisplayItem]_block_invoke
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1741
- ___98-[SBInlineAppExposeContinuousExposeSwitcherModifier adjustedSpaceAccessoryViewFrame:forAppLayout:]_block_invoke
- ___SBNSStringFromUIRectCorner_block_invoke
- ___block_descriptor_105_e8_32s40s48s56s64s72s80s_e27_v16?0"SBSAnalyticsState"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_113_e8_32s40s48s56s64s72s_e38_B16?0"SBFluidSwitcherItemContainer"8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_148_e8_32s40s_e29_{CGPoint=dd}24?0{CGSize=dd}8ls32l8s40l8
- ___block_descriptor_160_e8_32s40s48s56s64s72s80s88bs_e33_v16?0?<?<v?BB>?"NSString">8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_32_e93_q24?0"SBMutableContinuousExposeAutoLayoutItem"8"SBMutableContinuousExposeAutoLayoutItem"16l
- ___block_descriptor_48_e8_32s40s_e25_B32?0"NSString"8Q16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e55_Q24?0Q8"<SBFAnalyticsBackendEventContextProviding>"16ls32l8s40l8
- ___block_descriptor_48_e8_32s_e36_{CGRect={CGPoint=dd}{CGSize=dd}}8?0ls32l8
- ___block_descriptor_49_e8_32s40s_e27_v16?0"SBSAnalyticsState"8ls32l8s40l8
- ___block_descriptor_49_e8_32s_e27_v16?0"SBSAnalyticsState"8ls32l8
- ___block_descriptor_50_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
- ___block_descriptor_50_e8_32s_e19_"NSDictionary"8?0ls32l8
- ___block_descriptor_56_e16_{CGPoint=dd}8?0l
- ___block_descriptor_65_e8_32s40s48s_e27_v16?0"SBSAnalyticsState"8ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s_e27_v16?0"SBSAnalyticsState"8ls32l8s40l8
- ___block_descriptor_66_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
- ___block_descriptor_72_e16_{CGPoint=dd}8?0l
- ___block_descriptor_73_e8_32s40s48s56r_e8_v16?08ls32l8r56l8s40l8s48l8
- ___block_descriptor_73_e8_32s40s48s56r_e8_v16?08ls32l8s40l8s48l8r56l8
- ___block_descriptor_80_e16_{CGPoint=dd}8?0l
- ___block_descriptor_80_e40_B24?0^{CGPoint=dd}8?<{CGPoint=dd}?>16l
- ___block_descriptor_88_e8_32s40s48r_e30_v32?0q8"SBDisplayItem"16^B24ls32l8s40l8r48l8
- ___block_descriptor_88_e8_d16?0Q8l
- ___block_descriptor_89_e8_32s40s48s56s64s72s_e27_v16?0"SBSAnalyticsState"8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_98_e8_32s_e8_v16?08ls32l8
- ___block_literal_global.1059
- ___block_literal_global.1068
- ___block_literal_global.1104
- ___block_literal_global.1105
- ___block_literal_global.1156
- ___block_literal_global.1159
- ___block_literal_global.1170
- ___block_literal_global.1463
- ___block_literal_global.1584
- ___block_literal_global.1588
- ___block_literal_global.1620
- ___block_literal_global.1629
- ___block_literal_global.1631
- ___block_literal_global.1633
- ___block_literal_global.1635
- ___block_literal_global.1651
- ___block_literal_global.1767
- ___block_literal_global.1790
- ___block_literal_global.1799
- ___block_literal_global.1815
- ___block_literal_global.263
- ___block_literal_global.332
- ___block_literal_global.338
- ___block_literal_global.348
- ___block_literal_global.350
- ___block_literal_global.359
- ___block_literal_global.366
- ___block_literal_global.488
- ___block_literal_global.493
- ___block_literal_global.497
- ___block_literal_global.575
- ___block_literal_global.588
- ___block_literal_global.590
- ___block_literal_global.592
- ___block_literal_global.594
- ___block_literal_global.596
- ___block_literal_global.611
- ___block_literal_global.622
- ___block_literal_global.625
- ___block_literal_global.628
- ___block_literal_global.680
- ___block_literal_global.774
- ___block_literal_global.809
- ___block_literal_global.811
- ___block_literal_global.845
- ___block_literal_global.848
- ___block_literal_global.876
- ___block_literal_global.881
- ___block_literal_global.885
- ___block_literal_global.928
- ___block_literal_global.929
- _colorForSpecifierString
- _kCAFilterColorBurnBlendMode
- _kSBSAnalyticsSwitcherCardDropActionKey
- _kSBSAnalyticsSwitcherCardDropDraggingLeafAppLayoutBundleIdentifierKey
- _kSBSAnalyticsSwitcherCardDropIntersectingLeafAppLayoutBundleIdentifierKey
- _kSBSAnalyticsSwitcherCardDropRegionKey
- _kSBSAnalyticsWindowDropBundleIdentifierKey
- _kSBSAnalyticsWindowDropDestinationKey
- _kSBSAnalyticsWindowDropPeekConfigurationKey
- _objc_msgSend$_allowsBacklightChanges
- _objc_msgSend$_appStripOriginX
- _objc_msgSend$_autoLayoutController
- _objc_msgSend$_beginStageRubberbandingRampingPropertyWithMode:settings:
- _objc_msgSend$_cachedOrFallbackFrameForIndex:cacheValidityToken:
- _objc_msgSend$_cachedOrFallbackScaleForIndex:cacheValidityToken:
- _objc_msgSend$_compactSpacingBetweenItemsInSpace:configuration:
- _objc_msgSend$_currentAutoLayoutSpace
- _objc_msgSend$_emitAnalyticsEventForMenuInteraction:
- _objc_msgSend$_fullyOccludedItemsForSpace:configuration:
- _objc_msgSend$_handleIndicatorAppearanceStateContextChanges:
- _objc_msgSend$_highlightScaleForAppLayout:
- _objc_msgSend$_indexInContinuousExposeIdentifierPileForAppLayout:
- _objc_msgSend$_inlineAppExposeSwitcherFrame
- _objc_msgSend$_interSensorRegionMinimumDwellTimeTimerFired
- _objc_msgSend$_invalidateAppStripOriginX
- _objc_msgSend$_itemsSortedByXInSpace:configuration:
- _objc_msgSend$_layoutHostMayNotPerformLayoutUpdate
- _objc_msgSend$_makePayloadFromMetricsByDatestamp:
- _objc_msgSend$_maximumNumberOfInlineAppExposeAppLayouts
- _objc_msgSend$_maximumNumberOfInlineAppExposeColumns
- _objc_msgSend$_maximumNumberOfInlineAppExposeRows
- _objc_msgSend$_numberOfInlineAppExposeAppLayouts
- _objc_msgSend$_numberOfInlineAppExposeColumns
- _objc_msgSend$_numberOfInlineAppExposeRows
- _objc_msgSend$_orderedVisibleAppLayoutsIgnoringProgress:
- _objc_msgSend$_performAutoLayoutWithSpace:configuration:stageInset:
- _objc_msgSend$_queue_initializeIfNeeded
- _objc_msgSend$_queue_scheduleWriteIfNeeded
- _objc_msgSend$_queue_writeToPersistenceURL
- _objc_msgSend$_removeDisplayItemFromDesktop:
- _objc_msgSend$_responseForSceneSizeUpdateToSize:center:sceneUpdatesOnly:
- _objc_msgSend$_responseToUpdateReopenClosedWindowsButtonPresenceIfNeeded
- _objc_msgSend$_scaleForActiveAppLayoutLeafAppLayouts
- _objc_msgSend$_scaleForInlineAppExposeAppLayouts
- _objc_msgSend$_sendAggregateSessionCoreAnalyticsEventWithIdentifier:startReason:endReason:duration:doNotDisturbActive:hardwareKeyboardAttached:
- _objc_msgSend$_sendCoreAnalyticsEventWithStartReason:endReason:duration:centerBundleIdentifier:doNotDisturbActive:hardwareKeyboardAttached:
- _objc_msgSend$_sendCoreAnalyticsEventWithStartReason:endReason:duration:floatingBundleIdentifier:doNotDisturbActive:hardwareKeyboardAttached:
- _objc_msgSend$_sendIndividualSessionCoreAnalyticsEventWithAggregateIdentifier:startReason:endReason:duration:primaryBundleIdentifier:sideBundleIdentifier:doNotDisturbActive:hardwareKeyboardAttached:
- _objc_msgSend$_setInterSensorRegionMinimumDwellTimeSatisfied:
- _objc_msgSend$_setMenuBarVisible:animated:
- _objc_msgSend$_sizeForFloatingApplication
- _objc_msgSend$_snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:
- _objc_msgSend$_spaceWithoutPerformingAutoLayoutWithSpace:previousSpace:configuration:options:
- _objc_msgSend$_stripScreenEdgePadding
- _objc_msgSend$_supportedSizingPoliciesForContentOrientation:containerOrientation:
- _objc_msgSend$_updateItemsCoveredByFullyOccludedPeekingItemsInSpace:configuration:
- _objc_msgSend$_updateOcclusionStatusForItemsInSpace:configuration:
- _objc_msgSend$_updateRootLayerBackgroundColor
- _objc_msgSend$_updateTransformLayer
- _objc_msgSend$_wallpaperDimmingForIndex:
- _objc_msgSend$addIcon:toListAtIndex:options:
- _objc_msgSend$aggregateSessionIdentifier
- _objc_msgSend$aggregateSessionStartReason
- _objc_msgSend$aggregateSessionStartTimestamp
- _objc_msgSend$analyticsDefaults
- _objc_msgSend$anchorPosition
- _objc_msgSend$attentionScore
- _objc_msgSend$attentionScoreThreshold
- _objc_msgSend$autoLayoutItemForDisplayItem:
- _objc_msgSend$autoLayoutItemForDisplayItemIfExists:
- _objc_msgSend$autoLayoutSpaceForAppLayout:
- _objc_msgSend$autoLayoutSpaceForAppLayout:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:
- _objc_msgSend$boundingBoxForSpace:configuration:
- _objc_msgSend$cachedLastAutoLayoutSpace
- _objc_msgSend$calendar
- _objc_msgSend$centerBundleIdentifier
- _objc_msgSend$configurationWithTextStyle:scale:
- _objc_msgSend$configurationWithWeight:
- _objc_msgSend$continuousExposeAutoLayoutItemRepresentation
- _objc_msgSend$continuousExposeAutoLayoutSpaceRepresentation
- _objc_msgSend$currentTraitCollection
- _objc_msgSend$customContext
- _objc_msgSend$customScaleFactorX
- _objc_msgSend$customScaleFactorY
- _objc_msgSend$customTranslationOffsetX
- _objc_msgSend$customTranslationOffsetY
- _objc_msgSend$dateFormatter
- _objc_msgSend$deviceContext
- _objc_msgSend$displayContext
- _objc_msgSend$dodgeFullyOccludedWindowsToNearestVisibleEdgeForSpace:configuration:
- _objc_msgSend$emulatedDeviceBezelImageName
- _objc_msgSend$emulatedDeviceBounds
- _objc_msgSend$emulatedDeviceClass
- _objc_msgSend$emulatedDeviceImageContainingBundle
- _objc_msgSend$emulatedDeviceMaskImageName
- _objc_msgSend$emulatedDisplayCornerRadius
- _objc_msgSend$emulatedHomeButtonType
- _objc_msgSend$engagementPlistRepresentation
- _objc_msgSend$hasDifferentColorAppearanceComparedToTraitCollection:
- _objc_msgSend$hasEmulatedDeviceBounds
- _objc_msgSend$highlightedByHoverAppLayouts
- _objc_msgSend$highlightedByTouchAppLayouts
- _objc_msgSend$indicatorContainerMinimumScale
- _objc_msgSend$indicatorContainerSize
- _objc_msgSend$individualSessionPrimaryBundleIdentifier
- _objc_msgSend$individualSessionSideBundleIdentifier
- _objc_msgSend$individualSessionStartReason
- _objc_msgSend$individualSessionStartTimestamp
- _objc_msgSend$initWithBacklightController:
- _objc_msgSend$initWithHeartbeatMetricPersistence:
- _objc_msgSend$initWithInterSensorRegionIndicatorVisualRepresentation:microRegionIndicatorVisualRepresentation:recordingIndicatorManager:
- _objc_msgSend$initWithPersistence:
- _objc_msgSend$initWithPersistenceURL:persistenceDelay:persistenceLeeway:
- _objc_msgSend$insertOSMigrationHomeScreenLayoutItem:intoListAtIndex:inFolder:rootFolder:referenceGridSize:
- _objc_msgSend$insertSublayer:below:
- _objc_msgSend$interSensorRegionMinimumDwellTimeSatisfied
- _objc_msgSend$intersectingLeafAppLayout
- _objc_msgSend$isEmulatedDevice
- _objc_msgSend$isInDefaultPosition
- _objc_msgSend$isPartiallyCoveredByPeekingItem
- _objc_msgSend$isPhoneUnlockWithVisionSupportedAndEnabled
- _objc_msgSend$isPointInsideMenuBarContent:
- _objc_msgSend$isShowingReopenClosedWindowsButton
- _objc_msgSend$materialViewWithRecipeNamesByTraitCollection:inBundle:options:initialWeighting:scaleAdjustment:compatibleWithTraitCollection:
- _objc_msgSend$metricsByDatestamp
- _objc_msgSend$migrateDataFromDefaultsIfNeeded:
- _objc_msgSend$renderingCenter
- _objc_msgSend$requestForTapAppLayoutHeaderEvent:
- _objc_msgSend$requireStripContentsInViewHierarchy
- _objc_msgSend$rootLayerBackgroundColorString
- _objc_msgSend$sb_configureForDeviceEmulation
- _objc_msgSend$scalingStyle
- _objc_msgSend$setAggregateSessionIdentifier:
- _objc_msgSend$setAggregateSessionStartReason:
- _objc_msgSend$setAggregateSessionStartTimestamp:
- _objc_msgSend$setAnchorPosition:
- _objc_msgSend$setCachedLastAutoLayoutSpace:
- _objc_msgSend$setCenterBundleIdentifier:
- _objc_msgSend$setDeviceContext:
- _objc_msgSend$setDisplayContext:
- _objc_msgSend$setEngagementPlistRepresentation:
- _objc_msgSend$setHighlightedByHoverAppLayouts:
- _objc_msgSend$setHighlightedByTouchAppLayouts:
- _objc_msgSend$setInDefaultPosition:
- _objc_msgSend$setIndicatorContainerMinimumScale:
- _objc_msgSend$setIndicatorContainerSize:
- _objc_msgSend$setIndividualSessionPrimaryBundleIdentifier:
- _objc_msgSend$setIndividualSessionSideBundleIdentifier:
- _objc_msgSend$setIndividualSessionStartReason:
- _objc_msgSend$setIndividualSessionStartTimestamp:
- _objc_msgSend$setInterSensorRegionMinimumDwellTimeSatisfied:
- _objc_msgSend$setPartiallyCoveredByPeekingItem:
- _objc_msgSend$setUnoccludedPeekingPosition:
- _objc_msgSend$snapPositionToNearestEdgesIfNecessaryForSpace:stageArea:configuration:
- _objc_msgSend$spaceByPerformingAutoLayoutWithSpace:previousSpace:configuration:options:
- _objc_msgSend$stageAreaForSpace:configuration:
- _objc_msgSend$startOfDayForDate:
- _objc_msgSend$switcherContentController:removeDisplayItemFromDesktop:
- _objc_msgSend$topAffordanceViewController:handleActionType:
- _objc_msgSend$trackInteractionWithFeatureNamed:duration:
- _objc_msgSend$unoccludedPeekingPosition
- _objc_msgSend$updateOverlappingScaleAnchorPositionsForSpace:configuration:
- _objc_msgSend$validBottomStageAreaInsetsWithConfiguration:
- _objc_msgSend$validLeadingStageAreaInsetsWithConfiguration:
- _objc_msgSend$validTopStageAreaInsetsWithConfiguration:
- _objc_msgSend$validTrailingStageAreaInsetsWithConfiguration:
- _objc_msgSend$willUIUnlockFromSource:
- _sscanf
CStrings:
+ "#\xf0\xb1"
+ "-[SBDisplayItemLayoutAttributesProvider performBlockWithoutUpdating:]"
+ "<%@: %p; clientIdentifier: %@; elementIdentifier: %@; supportsMicroIndicatorPosition: %@; indicatorNeedsDisplayWellKnownLocation: %@; indicatorSize: %@; preferredEdgeOutsets: %@; interfaceOrientation: %@>"
+ "<%@: %p; indicatorElementContext: %@; interSensorIndicatorPhase: %@; microIndicatorEjectionPhase: %@; microIndicatorPhase: %@>"
+ "<%@: %p> (%@, %@)"
+ "@\"<SAUIIndicatorLayoutHosting>\""
+ "@\"<SAUIIndicatorLayoutHosting>\"16@0:8"
+ "@\"<SBHomeScreenMenuBarDelegate>\""
+ "@\"NSArray\"24@0:8@\"SBMenuBarViewController\"16"
+ "@\"SBFlexibleWindowingWindowDragSwitcherModifier\""
+ "@\"SBHomeScreenMenuBar\""
+ "@\"SBStripLayoutWindowingModifier\""
+ "@\"UIViewController\"24@0:8@\"SBIconView\"16"
+ "About This iPad"
+ "App Store"
+ "Are you sure you want your iPad to restart?"
+ "B40@0:8@\"SBDisplayItem\"16Q24@\"SBAppLayout\"32"
+ "B40@0:8@16Q24@32"
+ "B40@?0@\"SBChainableModifier\"8@16Q24@32"
+ "B60@0:8@16Q24@32@40{SBHIconGridSize=SS}48^Q52"
+ "Base State"
+ "CLOSE_ALL_WINDOW_DISCOVERABILITY"
+ "CLOSE_WINDOW_DISCOVERABILITY"
+ "CommandQKeyboardShortcut"
+ "Control Center"
+ "DidEdgeProtectResizeGrabber"
+ "Edit Home Screen"
+ "File-stack-chevron-open-indicator"
+ "Full Screen Apps"
+ "Go"
+ "HIDE_APP_DISCOVERABILITY"
+ "HIDE_DISCOVERABILITY"
+ "HIDE_OTHERS_DISCOVERABILITY"
+ "Minimum Container Outset"
+ "Minimum Content Scale"
+ "Minimum Screen Padding"
+ "Next Page"
+ "Notification Center"
+ "Preventing the switcher live resize gesture because of edge protect."
+ "Previous Page"
+ "QUIT_APP_DISCOVERABILITY"
+ "QUIT_DISCOVERABILITY"
+ "Quick Note"
+ "Recent Apps"
+ "Restart"
+ "Restart iPad"
+ "SAUIIndicatorLayoutHosting"
+ "SAUIIndicatorLayoutSpecifying"
+ "SBDidEdgeProtectResizeGrabberModifierEvent"
+ "SBHomeScreenMenuBar"
+ "SBHomeScreenMenuBarDelegate"
+ "SBMenuBarInvocationMetric"
+ "SBMenuBarItemSelectionMetric"
+ "SBMenuBarSearchMetric"
+ "SBRecordingIndicatorSystemApertureElement.m"
+ "SBResizeGrabberHintingSwitcherModifier"
+ "SBResizeGrabberHintingSwitcherModifier(%@, %@)"
+ "Screenshot & Edit"
+ "Show Dock"
+ "Show/Hide Menu Bar"
+ "Stage Manager"
+ "T@\"<SAUIIndicatorLayoutHosting>\",?,W,N"
+ "T@\"<SAUIIndicatorLayoutHosting>\",?,W,N,V_layoutHost"
+ "T@\"<SBHomeScreenMenuBarDelegate>\",W,N,V_delegate"
+ "T@\"<SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistration>\",&,N,V_minimumOnTimeAssertion"
+ "T@\"BSContinuousMachTimer\",&,N,V_interSensorDwellTimer"
+ "T@\"FBScene\",W,N,V_homeScreenMenuBarProvidingScene"
+ "T@\"NSArray\",R,N,V_systemMenuIdentifiersIgnoredInMenuBar"
+ "T@\"NSString\",C,N,V_bundleIdentifierOfAppToKillGracefully"
+ "T@\"SBDynamicLightingController\",R,N,V_dynamicLightingController"
+ "T@\"SBFlexibleWindowingWindowDragSwitcherModifier\",R,N,V_gestureModifier"
+ "T@\"SBHomeScreenMenuBar\",R,N,V_homeScreenMenuBar"
+ "T@\"SBSAIndicatorElementContext\",&,N,S_setActiveIndicatorElementContext:,V_activeIndicatorElementContext"
+ "T@\"SBSAIndicatorElementContext\",N"
+ "T@\"SBSecureIndicatorMinimumOnTimeCoordinator\",&,N,V_minimumOnTimeCoordinator"
+ "TB,N,GisContingencyPlan,V_contingencyPlan"
+ "TB,N,S_setIndicatorNeedsDisplayWellKnownLocation:,V_indicatorNeedsDisplayWellKnownLocation"
+ "TB,N,V_interSensorDwellTimerSatisfied"
+ "TB,N,V_minimumOnTimeSatisfied"
+ "TB,N,V_searchTextFieldUsedOnce"
+ "TB,R,N,V_destroyAllScenesMatchingBundleIdentifier"
+ "TQ,R,N,V_corners"
+ "Td,N,V_indicatorContainerMinimumOutset"
+ "Td,N,V_indicatorContentMinimumScale"
+ "Td,N,V_indicatorMinimumScreenPadding"
+ "T{CGSize=dd},N,S_setIndicatorSize:,V_indicatorSize"
+ "Windowed Apps"
+ "[%{public}lu] Container property identifier %@ is no longer being tracked for milestone: %f; assume that indicates the milestone is completed and we can push forward our state machine. IndicatorAppearStateContext is currently: %@"
+ "[%{public}lu] Ejection is viable. %@"
+ "[ActivityID: %{public}@] alert presentation failed for original destination. Looking for fallback destination."
+ "[ActivityID: %{public}@] posting banner as fallback alert"
+ "[ActivityID: %{public}@] posting fallback alert"
+ "[Recording Indicator] element MOT changed: %{BOOL}u; oldValue: %{BOOL}u"
+ "[Recording Indicator] element MOT evaluating: %{BOOL}u; oldValue: %{BOOL}u; %@"
+ "[Recording Indicator] element dwell time satisfied changed: %{BOOL}u; oldValue: %{BOOL}u"
+ "[Recording Indicator] element registering for MOT satisfied changes: %{BOOL}u; %@"
+ "[displayItems count] > 0"
+ "_activateAppLayout:fromSwitcher:withWindowScene:"
+ "_activeIndicatorElementContext"
+ "_appRestrictionReason"
+ "_buildHideMenuWithAdditionalOptions:"
+ "_buildQuitMenuWithAdditionalOptions:"
+ "_bundleIdentifierOfAppToKillGracefully"
+ "_cachedDefaultReferenceSizeForSceneView"
+ "_cancelDwellTimer"
+ "_centerWindowSizeForPreviousFullscreenWindow"
+ "_contingencyPlan"
+ "_createRecentAppsMenu"
+ "_defaultReferenceSizeForSceneView"
+ "_destroyAllScenesMatchingBundleIdentifier"
+ "_disableDynamicLightingAssertion"
+ "_ensureMotRequirements"
+ "_flushIndicatorDidSettleHandlersIfNecessary"
+ "_handleCloseAllWindowsShortcut:"
+ "_handleCloseWindowShortcut:"
+ "_handleEditHomeScreenShortcut"
+ "_handleReboot"
+ "_handleRemoveAllWindowFromSetAndQuitShortcut:"
+ "_handleRemoveAllWindowFromSetForNonSelectedAppShortcut:"
+ "_handleRemoveAllWindowFromSetShortcut:"
+ "_handleRestartShortcutWithConfirmation"
+ "_handleScreenshotFullScreenShortcut:"
+ "_handleScreenshotPIPShortcut:"
+ "_handleShutDown"
+ "_homeScreenIsOnFirstPage"
+ "_homeScreenMenuBar"
+ "_homeScreenMenuBarProvidingScene"
+ "_indicatorContainerMinimumOutset"
+ "_indicatorContentMinimumScale"
+ "_indicatorMinimumScreenPadding"
+ "_indicatorNeedsDisplayWellKnownLocation"
+ "_indicatorSize"
+ "_initialHomeScreenDimmingAlpha"
+ "_interSensorDwellTimer"
+ "_interSensorDwellTimerSatisfied"
+ "_isHandlingEvent:"
+ "_isPerformingWithoutUpdating"
+ "_layoutHostMayNotPerformLayoutUpdateWithReasonsToExclude:"
+ "_lockScreenUIWillDismiss:"
+ "_minimumOnTimeAssertion"
+ "_minimumOnTimeSatisfied"
+ "_pendOrExecuteDelegateCallout:"
+ "_pendedDelegateCalloutBlocks"
+ "_postBannerWithAlert:"
+ "_removeDisplayItemsFromDesktop:"
+ "_requestPerformShortcutActionWithType:"
+ "_searchTextFieldUsedOnce"
+ "_setActiveIndicatorElementContext:"
+ "_setIndicatorNeedsDisplayWellKnownLocation:"
+ "_setIndicatorSize:"
+ "_setMenuBarVisible:animated:userInitiated:"
+ "_shouldShowAlertForSeed"
+ "_startDwellTimer"
+ "_systemApertureIndicatorDidSettleCompletionBlocks"
+ "_systemMenuIdentifiersIgnoredInMenuBar"
+ "activeIndicatorElementContext"
+ "addIcon:toList:options:"
+ "alertPresentationFailed:"
+ "allowsBacklightChanges"
+ "app.badge.clock"
+ "app.grid.2x2.topbackward.filled"
+ "applicationState"
+ "apps.ipad.landscape"
+ "appstore"
+ "arrow.left"
+ "arrow.right"
+ "arrowtriangle.backward"
+ "bell.badge.fill"
+ "bundleIdentifierOfAppToKillGracefully"
+ "camera.viewfinder"
+ "cleanUpPersistedDataIfNeeded"
+ "com.apple.Passwords"
+ "com.apple.ipad_menubar_invoked"
+ "com.apple.ipad_menubar_search"
+ "com.apple.ipad_menubar_selected"
+ "com.apple.ipad_multitasking_window_controls"
+ "com.apple.springboard.SBRecordingIndicatorSystemApertureElement.interSensorDwellTimer"
+ "commandWithTitle:image:action:propertyList:alternates:"
+ "contingencyPlan"
+ "destroyAllScenesMatchingBundleIdentifier"
+ "disableEffectsForReason:"
+ "displayNameForWebAppWithSceneIdentifier:"
+ "dock.rectangle"
+ "dynamicLightingController"
+ "editMenu"
+ "expectedKeyWindow"
+ "gear"
+ "getEditMenu"
+ "handleActionWithURL:"
+ "handleAppStoreAction"
+ "handleDidEdgeProtectResizeGrabberEvent:"
+ "hasEmptyCorners"
+ "hideMenuWithOptions:"
+ "homeScreenIsOnFirstPage"
+ "homeScreenMenuBar"
+ "homeScreenMenuBarProvidingScene"
+ "iPad"
+ "iPad User Guide"
+ "iconManager:preferredMenuElementOrderForIconView:"
+ "indexOfFirstUsedGridCellInGridRange:"
+ "indicatorContainerMinimumOutset"
+ "indicatorContentMinimumScale"
+ "indicatorLayoutSpecifying"
+ "indicatorMinimumScreenPadding"
+ "indicatorNeedsDisplayWellKnownLocation"
+ "indicatorNeedsDisplayWellKnownLocationDidInvalidateForLayoutSpecifier:"
+ "indicatorSize"
+ "initWithBacklightController:thermalController:"
+ "initWithDisplayItem:corners:"
+ "initWithDisplayItem:destroyAllScenesMatchingBundleIdentifier:"
+ "initWithInterSensorRegionIndicatorVisualRepresentation:microRegionIndicatorVisualRepresentation:recordingIndicatorManager:minimumOnTimeCoordinator:"
+ "initWithPersistenceURL:"
+ "initWithReferenceView:"
+ "insertOSMigrationHomeScreenLayoutItem:intoListAtIndex:inFolder:rootFolder:referenceGridSize:subsequentListSlide:"
+ "inset.filled.rectangle.and.camera"
+ "interSensorDwellTimer"
+ "interSensorDwellTimerSatisfied"
+ "isContingencyPlan"
+ "isHintingResizeGrabberForDisplayItem:corner:inAppLayout:"
+ "isLaunchDisallowedForRatingRank"
+ "isPhoneUnlockEnabledAndRequirementsMet"
+ "isPointInsideMenuBarContent:fromCoordinateSpace:"
+ "isSceneHandleNotUserDestroyable:"
+ "isSettled"
+ "isSpringBoardMenuBarForScene:"
+ "jsonDescription"
+ "kill application for keyboard shortcut"
+ "lightbulb"
+ "macwindow.on.rectangle"
+ "markIcon:asNeedingAnimation:"
+ "menubar.rectangle"
+ "minimumCustomElementHeightUnderSensor"
+ "minimumOnTimeAssertion"
+ "minimumOnTimeSatisfied"
+ "noteDidEdgeProtectResizeGrabberForDisplayItem:inCorner:"
+ "noteSearchUsedInMenuBarHelpMenuProvider:"
+ "openSensitiveURL:withOptions:"
+ "parentViewControllerForCustomIconImageViewControllerForIconView:"
+ "performAction:withCompletionUponIndicatorSettling:"
+ "performBlockWithoutUpdating:"
+ "preferredIndicatorEdgeOutsets"
+ "preferredIndicatorEdgeOutsetsDidInvalidateForLayoutSpecifier:"
+ "presentFallbackAlert:"
+ "quitMenuWithOptions:"
+ "rectangle"
+ "rectangle.3.group"
+ "removeMenuForIdentifier:"
+ "replaceChildrenOfMenuForIdentifier:fromChildrenBlock:"
+ "resetInternalState"
+ "restart from menu bar"
+ "restrictionReason"
+ "sb_isDisplayItemLayoutAttributes"
+ "sb_test_padGridSizeClassMap"
+ "sb_test_phoneGridSizeClassMap"
+ "sceneHandleDisablesKillingInSwitcher:"
+ "searchTextFieldUsedOnce"
+ "setActiveIndicatorElementContext:"
+ "setAsynchronousOpaque:"
+ "setBundleIdentifierOfAppToKillGracefully:"
+ "setContingencyPlan:"
+ "setCornerOffset:"
+ "setGridSize:forGridSizeClass:"
+ "setHomeScreenMenuBarProvidingScene:"
+ "setIndicatorContainerMinimumOutset:"
+ "setIndicatorContentMinimumScale:"
+ "setIndicatorMinimumScreenPadding:"
+ "setIndicatorNeedsDisplayWellKnownLocation:"
+ "setIndicatorSize:"
+ "setInterSensorDwellTimer:"
+ "setInterSensorDwellTimerSatisfied:"
+ "setMinimumOnTimeAssertion:"
+ "setMinimumOnTimeCoordinator:"
+ "setMinimumOnTimeSatisfied:"
+ "setSearchTextFieldUsedOnce:"
+ "settings-navigation://com.apple.Settings.General"
+ "settings-navigation://com.apple.Settings.General/About"
+ "sharedSystem"
+ "showConfirmationAlertWithTitle:message:confirmTitle:handler:"
+ "siri"
+ "sizeThatFitsSize:forProvidedView:"
+ "square.and.pencil"
+ "squares.leading.rectangle"
+ "switch.2"
+ "switcherContentController:removeDisplayItemsFromDesktop:"
+ "systemHideMenuWithOptions:"
+ "systemMenuIdentifiersIgnoredInMenuBar"
+ "systemMenusToIgnoreForViewController:"
+ "systemQuitMenuWithOptions:"
+ "toggleMenuBarVisibility"
+ "topAffordanceViewController:requestsPerformShortcutActionWithType:"
+ "trafficLightPartIdentifier"
+ "v24@0:8@\"<SAUIIndicatorLayoutHosting>\"16"
+ "v24@0:8@\"<SAUIIndicatorLayoutSpecifying>\"16"
+ "v24@0:8@\"SBMenuBarHelpMenuProvider\"16"
+ "v24@0:8@\"UIKeyCommand\"16"
+ "v32@0:8@\"<SBSwitcherContentViewControlling>\"16@\"NSSet\"24"
+ "w"
+ "wantsDisableUpdateClonedDuringSharePlay"
+ "willUIUnlockFromSource:isLockScreenDisabledForAssertion:"
+ "windowControlsViewController:didRequestSlideOverAction:"
+ "workspaceEntity must be present in layout state"
+ "{?=\"switcherContentControllerBringAppLayoutToFront\"b1\"switcherContentControllerActivatedBestAppSuggestion\"b1\"updateUserInteractionEnabledForSwitcherContentController\"b1\"updateWindowVisibilityForSwitcherContentController\"b1\"switcherContentControllerSetHomeScreenScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenAlphaWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenDimmingAlphaWithSettingsAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurProgressWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurType\"b1\"switcherContentControllerSetHomeScreenBackdropBlurMaterialRecipeNameWithAnimationModeCompletion\"b1\"switcherContentControllerControlsWallpaper\"b1\"switcherContentControllerSetWallpaperScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetWallpaperStyle\"b1\"switcherContentControllerSetInterfaceOrientation\"b1\"switcherContentControllerSetInterfaceOrientationFromUserResizingForDisplayItem\"b1\"switcherContentControllerRequestNewWindowForBundleIdentifier\"b1\"switcherContentControllerSetContainerStatusBarHiddenPartsHiddenAnimationDuration\"b1\"switcherContentControllerWantsToDismissMenuBar\"b1\"switcherContentControllerWantsToPeekMenuBar\"b1\"switcherContentControllerWantsToUpdateMenuBarVisibility\"b1\"switcherContentControllerDemoLayoutAttributesForDisplayItem\"b1\"switcherContentControllerSetPointerInteractionsEnabled\"b1\"switcherContentControllerShouldResignActiveForStartOfTransition\"b1\"switcherContentControllerControlsHomeScreenContents\"b1\"switcherContentControllerSetCacheAsynchronousRenderingSurfaces\"b1\"cancelActiveGestureForSwitcherContentController\"b1\"switcherContentControllerReopenHiddenAppLayoutsWithBundleIdentifier\"b1\"switcherContentControllerLayoutStateTransitionDidEndWithTransitionContext\"b1\"switcherContentControllerTransformForCardUnderSheetForBoundsSize\"b1\"switcherContentControllerMoveDisplayItemFromOtherDisplay\"b1\"presentContinuousExposeStripRevealGrabberTongueImmediatelyForSwitcherContentController\"b1\"tickleContinuousExposeStripRevealGrabberTongueIfVisibleForSwitcherContentController\"b1\"switcherContentControllerDidUpdateVisibleHomeAffordances\"b1\"switcherContentControllerRemoveDisplayItemsFromDesktop\"b1\"switcherContentControllerRequestDismissalForHomeScreenBackgroundTaps\"b1}"
+ "{CGSize=dd}40@0:8{CGSize=dd}16@\"UIView\"32"
+ "{SBDisplayItemAttributedSize={CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}q}16@0:8"
+ "\x81!\xa1"
- "#\xf0\xc1"
- "%@Color"
- "%@CountTrailing1Day"
- "%@CountTrailing30Days"
- "%@CountTrailing7Days"
- "%@DurationTrailing1Day"
- "%@DurationTrailing30Days"
- "%@DurationTrailing7Days"
- "%x"
- "([\\dA-F]{6})"
- "<%@: %p; clientIdentifier: %@; elementIdentifier: %@; supportsMicroIndicatorPosition: %@; interSensorRegionMinimumDwellTimeSatisfied: %@; interfaceOrientation: %@>"
- "<%@: %p; interSensorIndicatorPhase: %@; microIndicatorEjectionPhase: %@; microIndicatorPhase: %@>"
- "@\"<SBIconViewShortcutsDelegate>\"24@0:8@\"SBIconView\"16"
- "@\"<SBWindowDragSwitcherModifying>\""
- "@\"NSArray\"32@0:8@\"SBIconView\"16@\"NSArray\"24"
- "@\"NSISO8601DateFormatter\""
- "@\"SBAppLayout\"32@0:8@\"SBAppLayout\"16@\"SBAppLayout\"24"
- "@\"SBContinuousExposeAutoLayoutController\""
- "@\"SBContinuousExposeAutoLayoutSpace\""
- "@\"SBContinuousExposeWindowDragSwitcherModifier\""
- "@\"SBHRecentsDocumentExtensionProvider\"24@0:8@\"SBIconView\"16"
- "@\"SBHeartbeatMetricPersistence\""
- "@\"SBStripContinuousExposeSwitcherModifier\""
- "@52@0:8{CGSize=dd}16{CGPoint=dd}32B48"
- "AddToSet"
- "AggregateID"
- "AppLayoutPrimary"
- "AppLayoutSide"
- "ArrangeBottomAndTop"
- "ArrangeFill"
- "ArrangeGridEvenFour"
- "ArrangeLeftAndQuarters"
- "ArrangeLeftAndRight"
- "ArrangeRightAndLeft"
- "ArrangeThirds"
- "ArrangeTopAndBottom"
- "Attention Score Threshold"
- "B24@?0^{CGPoint=dd}8@?<{CGPoint=dd}@?>16"
- "B40@0:8@\"SBIconView\"16@\"SBSApplicationShortcutItem\"24Q32"
- "B52@0:8@16Q24@32@40{SBHIconGridSize=SS}48"
- "B56@0:8@16@24@32d40B48B52"
- "B72@0:8@16@24@32d40@48@56B64B68"
- "BetweenSpaces"
- "Called into the non-flexible autolayout controller when in flexible windowing."
- "Cancelled interSensorRegionMinimumDwellTimer; timer: %@"
- "CenterBundleID"
- "CenterWindowSession"
- "CloseWindow"
- "Container Size"
- "Counts"
- "DeviceEmulation"
- "DragOrigin"
- "DraggingBundleID"
- "DropAction"
- "DropRegion"
- "Expected to get an auto layout item for displayItem: '%@' in auto layout space: '%@'"
- "FloatingOntoExistingMainCard"
- "FloatingToMainNewIndex"
- "FullToFull"
- "FullToSplit"
- "IntersectingBundleID"
- "InvalidAppLayout"
- "Kicking off interSensorRegionMinimumDwellTimer; timer: %@"
- "MainToFloating"
- "Minimum Container Scale"
- "MoveToExternalDisplay"
- "MoveToMainDisplay"
- "PeekPrimary"
- "PeekSide"
- "RemoveFromSet"
- "Result"
- "SBCenterWindowSessionMetric"
- "SBContinuousExposeAutoLayoutController"
- "SBContinuousExposeAutoLayoutController.m"
- "SBContinuousExposeAutoLayoutItem"
- "SBContinuousExposeAutoLayoutItem.m"
- "SBContinuousExposeAutoLayoutSpace"
- "SBContinuousExposeAutoLayoutSpace.m"
- "SBContinuousExposeWindowDragSwitcherModifier"
- "SBContinuousExposeWindowDragSwitcherModifier.m"
- "SBDeviceEmulationController"
- "SBHeartbeatMetric"
- "SBIconViewShortcutsDelegate"
- "SBInlineAppExposeContinuousExposeSwitcherModifier"
- "SBInlineAppExposeContinuousExposeSwitcherModifierTimerEventReason"
- "SBItemResizeGestureSwitcherModifier"
- "SBItemResizeGestureSwitcherModifier.m"
- "SBMedusaSwitcherDragMetric"
- "SBMedusaWindowDragMetric"
- "SBMutableContinuousExposeAutoLayoutItem"
- "SBMutableContinuousExposeAutoLayoutSpace"
- "SBSlideOverSessionMetric"
- "SBSplitViewSessionMetric"
- "SBStripContinuousExposeSwitcherModifier"
- "SBTopAffordanceMenuInteractionMetric"
- "SBWindowDragSwitcherModifying"
- "SecureIndicatorDisplayOff"
- "Should have a valid `unoccludedPeekingPosition` by this point"
- "SlideOverPrimary"
- "SlideOverSession"
- "SlideOverSide"
- "SplitToFull"
- "SplitToSplit"
- "SplitViewPrimary"
- "SplitViewSession"
- "SplitViewSide"
- "Swap"
- "T@\"<SBWindowDragSwitcherModifying>\",R,N,V_gestureModifier"
- "T@\"CALayer\",R,N,V_bezelLayer"
- "T@\"CALayer\",R,N,V_layerForBackgroundColor"
- "T@\"CALayer\",R,N,V_maskLayer"
- "T@\"NSArray\",&,N,V_items"
- "T@\"NSMutableSet\",&,N"
- "T@\"NSMutableSet\",&,N,V_highlightedByHoverAppLayouts"
- "T@\"NSMutableSet\",&,N,V_highlightedByTouchAppLayouts"
- "T@\"NSString\",C,N,V_aggregateSessionStartReason"
- "T@\"NSString\",C,N,V_centerBundleIdentifier"
- "T@\"NSString\",C,N,V_individualSessionPrimaryBundleIdentifier"
- "T@\"NSString\",C,N,V_individualSessionSideBundleIdentifier"
- "T@\"NSString\",C,N,V_individualSessionStartReason"
- "T@\"NSUUID\",C,N,V_aggregateSessionIdentifier"
- "T@\"SBAppLayout\",R,N,V_activeAppLayout"
- "T@\"SBContinuousExposeAutoLayoutSpace\",&,N,V_cachedLastAutoLayoutSpace"
- "T@\"SBContinuousExposeWindowDragSwitcherModifier\",R,N,V_windowDragModifier"
- "T@\"SBFullScreenAppLayoutSwitcherModifier\",&,N,V_fullScreenAppLayoutModifier"
- "T@\"SBHeartbeatMetricPersistence\",R,N,V_heartbeatMetricPersistence"
- "T@\"UIColor\",R,N,V_backgroundColor"
- "T@\"UISApplicationInitializationContext\",R,C,N"
- "T@\"UISDeviceContext\",R,C,N"
- "T@\"UISDisplayContext\",R,C,N"
- "TB,D,N,GisInDefaultPosition"
- "TB,D,N,GisPartiallyCoveredByPeekingItem"
- "TB,N,GisInDefaultPosition,V_inDefaultPosition"
- "TB,N,GisPartiallyCoveredByPeekingItem,V_partiallyCoveredByPeekingItem"
- "TB,N,GisShowingReopenClosedWindowsButton,V_showingReopenClosedWindowsButton"
- "TB,N,S_setInterSensorRegionMinimumDwellTimeSatisfied:,V_interSensorRegionMinimumDwellTimeSatisfied"
- "TQ,N,V_numberOfHiddenAppLayouts"
- "Td,N,V_aggregateSessionStartTimestamp"
- "Td,N,V_attentionScoreThreshold"
- "Td,N,V_indicatorContainerMinimumScale"
- "Td,N,V_indicatorContainerSize"
- "Td,N,V_individualSessionStartTimestamp"
- "Td,R,N,V_persistenceDelay"
- "Td,R,N,V_persistenceLeeway"
- "TileBottom"
- "TileBottomLeft"
- "TileBottomRight"
- "TileLeft"
- "TileRight"
- "TileTop"
- "TileTopLeft"
- "TileTopRight"
- "ToggleMaximizationUnzoom"
- "ToggleMaximizationZoom"
- "T{CGPoint=dd},N,V_anchorPosition"
- "T{CGPoint=dd},N,V_unoccludedPeekingPosition"
- "UTC"
- "Unable to create redacted display configuration: %@ from configuration:%@"
- "Unsplit"
- "[%{public}lu] Container property identitifier %@ is no longer being tracked for milestone: %f; assume that indicates the milestone is completed and we can push forward our state machine. IndicatorAppearStateContext is currently: %@"
- "[%{public}lu] Ejection is viable, and the micro indicator is already appearing. %@"
- "[%{public}lu] Ejection is viable, but still maintain the InterSensor indicator is the only appeared indicator because the InterSensor region timer has not elapsed: %@"
- "[%{public}lu] Ejection is viable, the micro indicator is not yet appearing, but the inter sensor indicator has satisfied its time limit in place, so eject. %@"
- "_aggregateSessionIdentifier"
- "_aggregateSessionStartReason"
- "_aggregateSessionStartTimestamp"
- "_allowsBacklightChanges"
- "_anchorPosition"
- "_appStripOriginX"
- "_attentionScoreThreshold"
- "_beginStageRubberbandingRampingPropertyWithMode:settings:"
- "_bezelLayer"
- "_cachedLastAutoLayoutSpace"
- "_cachedOrFallbackFrameForIndex:cacheValidityToken:"
- "_cachedOrFallbackScaleForIndex:cacheValidityToken:"
- "_cachedSizeForFloatingApplication"
- "_cached_appStripOriginX"
- "_cached_appStripUnocclusionProgress"
- "_cached_autoLayoutController"
- "_calendar"
- "_centerBundleIdentifier"
- "_compactSpacingBetweenItemsInSpace:configuration:"
- "_configureRootLayer:sceneTransformLayer:transformLayer:"
- "_continuousExposeStripModifierIfExists"
- "_convertToScreenRectFromSpaceRect:"
- "_currentAutoLayoutSpace"
- "_dateFormatter"
- "_emitAnalyticsEventForMenuInteraction:"
- "_foregroundImage"
- "_fullyOccludedItemsForSpace:configuration:"
- "_handleCommandQ:"
- "_handleIndicatorAppearanceStateContextChanges:"
- "_heartbeatMetricPersistence"
- "_highlightScaleForAppLayout:"
- "_inDefaultPosition"
- "_indexInContinuousExposeIdentifierPileForAppLayout:"
- "_indicatorContainerMinimumScale"
- "_indicatorContainerSize"
- "_individualSessionPrimaryBundleIdentifier"
- "_individualSessionSideBundleIdentifier"
- "_individualSessionStartReason"
- "_individualSessionStartTimestamp"
- "_inlineAppExposeSwitcherFrame"
- "_interSensorRegionMinimumDwellTimeSatisfied"
- "_interSensorRegionMinimumDwellTimeTimerFired"
- "_invalidateAppStripOriginX"
- "_isMicroSupported"
- "_itemsSortedByXInSpace:configuration:"
- "_layerForBackgroundColor"
- "_layoutHostMayNotPerformLayoutUpdate"
- "_makePayloadFromMetricsByDatestamp:"
- "_maskLayer"
- "_maximumNumberOfInlineAppExposeAppLayouts"
- "_maximumNumberOfInlineAppExposeColumns"
- "_maximumNumberOfInlineAppExposeRows"
- "_numberOfInlineAppExposeAppLayouts"
- "_numberOfInlineAppExposeColumns"
- "_numberOfInlineAppExposeRows"
- "_orderedVisibleAppLayoutsIgnoringProgress:"
- "_partiallyCoveredByPeekingItem"
- "_performAutoLayoutWithSpace:configuration:stageInset:"
- "_persistenceLeeway"
- "_queue_calendar"
- "_queue_dateFormatter"
- "_queue_initializeIfNeeded"
- "_queue_metricsByDatestamp"
- "_queue_persistenceTimer"
- "_queue_scheduleWriteIfNeeded"
- "_queue_writeToPersistenceURL"
- "_reentrancyGuard"
- "_removeDisplayItemFromDesktop:"
- "_requireStripContentsInViewHierarchy"
- "_responseForSceneSizeUpdateToSize:center:sceneUpdatesOnly:"
- "_responseToUpdateReopenClosedWindowsButtonPresenceIfNeeded"
- "_scaleForActiveAppLayoutLeafAppLayouts"
- "_scaleForInlineAppExposeAppLayouts"
- "_sendAggregateSessionCoreAnalyticsEventWithIdentifier:startReason:endReason:duration:doNotDisturbActive:hardwareKeyboardAttached:"
- "_sendCoreAnalyticsEventWithStartReason:endReason:duration:centerBundleIdentifier:doNotDisturbActive:hardwareKeyboardAttached:"
- "_sendCoreAnalyticsEventWithStartReason:endReason:duration:floatingBundleIdentifier:doNotDisturbActive:hardwareKeyboardAttached:"
- "_sendIndividualSessionCoreAnalyticsEventWithAggregateIdentifier:startReason:endReason:duration:primaryBundleIdentifier:sideBundleIdentifier:doNotDisturbActive:hardwareKeyboardAttached:"
- "_setInterSensorRegionMinimumDwellTimeSatisfied:"
- "_setMenuBarVisible:animated:"
- "_showingReopenClosedWindowsButton"
- "_sizeForFloatingApplication"
- "_snapPositionForAppToEdgesAndCenterOfRectForItem:rect:centerSnapPadding:edgeSnapPadding:requireBothAxesToSnap:configuration:"
- "_spaceWithoutPerformingAutoLayoutWithSpace:previousSpace:configuration:options:"
- "_stageRubberbandingRampingProperty"
- "_stageRubberbandingSettings"
- "_stripLayoutCache"
- "_temporaryInterSensorRegionMinimumDwellTimeTimer"
- "_unoccludedPeekingPosition"
- "_updateItemsCoveredByFullyOccludedPeekingItemsInSpace:configuration:"
- "_updateOcclusionStatusForItemsInSpace:configuration:"
- "_updateRootLayerBackgroundColor"
- "_updateTransformLayer"
- "_wallpaperDimmingForIndex:"
- "_windowDragModifier"
- "_xColorBurnView"
- "addIcon:toListAtIndex:options:"
- "aggregateSessionIdentifier"
- "aggregateSessionStartReason"
- "aggregateSessionStartTimestamp"
- "analyticsDefaults"
- "anchorPosition"
- "applicationBundleURLForShortcutsWithIconView:"
- "applicationInitializationContext"
- "attentionScore"
- "attentionScoreThreshold"
- "autoLayoutItemForDisplayItem:"
- "autoLayoutItemForDisplayItemIfExists:"
- "autoLayoutSpaceForAppLayout:"
- "autoLayoutSpaceForAppLayout:containerOrientation:windowingConfiguration:floatingDockHeight:screenScale:bounds:prefersStripHidden:prefersDockHidden:leftStatusBarPartIntersectionRegion:rightStatusBarPartIntersectionRegion:"
- "bezelLayer"
- "boundingBoxForSpace:configuration:"
- "cachedLastAutoLayoutSpace"
- "calendar"
- "centerBundleIdentifier"
- "chevron.down"
- "com.apple.SpringBoard.Analytics.CenterWindowSession"
- "com.apple.SpringBoard.Analytics.Heartbeat"
- "com.apple.SpringBoard.Analytics.SBHeartbeatMetricPersistence"
- "com.apple.SpringBoard.Analytics.SlideOverSession"
- "com.apple.SpringBoard.Analytics.SplitViewSession.Aggregate"
- "com.apple.SpringBoard.Analytics.SplitViewSession.Individual"
- "com.apple.SpringBoard.Analytics.SwitcherDrag"
- "com.apple.SpringBoard.Analytics.TopAffordanceMenuInteraction"
- "com.apple.SpringBoard.Analytics.WindowDrag"
- "configurationWithTextStyle:scale:"
- "configurationWithWeight:"
- "continuousExposeAutoLayoutItemRepresentation"
- "continuousExposeAutoLayoutSpaceRepresentation"
- "currentTraitCollection"
- "customScaleFactorX"
- "customScaleFactorY"
- "customTranslationOffsetX"
- "customTranslationOffsetY"
- "d16@?0Q8"
- "d32@0:8Q16@24"
- "dateFormatter"
- "deviceContext"
- "displayContext"
- "dodgeFullyOccludedWindowsToNearestVisibleEdgeForSpace:configuration:"
- "emulatedDeviceBezelImageName"
- "emulatedDeviceBounds"
- "emulatedDeviceClass"
- "emulatedDeviceImageContainingBundle"
- "emulatedDeviceMaskImageName"
- "emulatedDisplayCornerRadius"
- "emulatedHomeButtonType"
- "engagementPlistRepresentation"
- "folderDark"
- "folderLight"
- "fullScreenAppLayoutModifier"
- "hasDifferentColorAppearanceComparedToTraitCollection:"
- "hasEmulatedDeviceBounds"
- "heartbeatMetricPersistence"
- "highlightedByHoverAppLayouts"
- "highlightedByTouchAppLayouts"
- "iconView:applicationShortcutItemsWithProposedItems:"
- "iconView:shouldActivateApplicationShortcutItem:atIndex:"
- "iconViewShortcutsPresentationDidCancel:"
- "iconViewShortcutsPresentationDidFinish:"
- "iconViewShortcutsPresentationWillBegin:"
- "iconViewShortcutsPresentationWillFinish:"
- "iconViewShouldBeginShortcutsPresentation:"
- "iconViewShouldIncludeUninstallShortcutItem:"
- "inDefaultPosition"
- "indicatorContainerMinimumScale"
- "indicatorContainerSize"
- "individualSessionPrimaryBundleIdentifier"
- "individualSessionSideBundleIdentifier"
- "individualSessionStartReason"
- "individualSessionStartTimestamp"
- "initWithActiveAppLayout:appExposeBundleIdentifier:"
- "initWithBacklightController:"
- "initWithHeartbeatMetricPersistence:"
- "initWithInterSensorRegionIndicatorVisualRepresentation:microRegionIndicatorVisualRepresentation:recordingIndicatorManager:"
- "initWithPersistence:"
- "initWithPersistenceURL:persistenceDelay:persistenceLeeway:"
- "insertOSMigrationHomeScreenLayoutItem:intoListAtIndex:inFolder:rootFolder:referenceGridSize:"
- "insertSublayer:below:"
- "interSensorRegion time no longer satisified because InterSensor region indicator changed appearance state: %@; timer: %@"
- "interSensorRegionIndicatorDwellTime"
- "interSensorRegionMinimumDwellTimeSatisfied"
- "interSensorRegionMinimumDwellTimer fired; %@"
- "isEmulatedDevice"
- "isInDefaultPosition"
- "isPartiallyCoveredByPeekingItem"
- "isPhoneUnlockWithVisionSupportedAndEnabled"
- "isPointInsideMenuBarContent:"
- "isShowingReopenClosedWindowsButton"
- "layerForBackgroundColor"
- "maskLayer"
- "materialViewWithRecipeNamesByTraitCollection:inBundle:options:initialWeighting:scaleAdjustment:compatibleWithTraitCollection:"
- "metricsByDatestamp"
- "migrateDataFromDefaultsIfNeeded:"
- "numberOfHiddenAppLayouts"
- "partiallyCoveredByPeekingItem"
- "persistenceLeeway"
- "q!\xa1"
- "q24@?0@\"SBMutableContinuousExposeAutoLayoutItem\"8@\"SBMutableContinuousExposeAutoLayoutItem\"16"
- "recentDocumentExtensionProviderForIconView:"
- "renderingCenter"
- "rootLayerBackgroundColorString"
- "runAnimationsWithActions:animated:completion:"
- "sb_configureForDeviceEmulation"
- "scalingStyle"
- "setAggregateSessionIdentifier:"
- "setAggregateSessionStartReason:"
- "setAggregateSessionStartTimestamp:"
- "setAnchorPosition:"
- "setAttentionScoreThreshold:"
- "setCachedLastAutoLayoutSpace:"
- "setCenterBundleIdentifier:"
- "setDeviceContext:"
- "setDisplayContext:"
- "setEngagementPlistRepresentation:"
- "setFullScreenAppLayoutModifier:"
- "setHighlightedByHoverAppLayouts:"
- "setHighlightedByTouchAppLayouts:"
- "setInDefaultPosition:"
- "setIndicatorContainerMinimumScale:"
- "setIndicatorContainerSize:"
- "setIndividualSessionPrimaryBundleIdentifier:"
- "setIndividualSessionSideBundleIdentifier:"
- "setIndividualSessionStartReason:"
- "setIndividualSessionStartTimestamp:"
- "setInterSensorRegionMinimumDwellTimeSatisfied:"
- "setItems:"
- "setNumberOfHiddenAppLayouts:"
- "setPartiallyCoveredByPeekingItem:"
- "setShowingReopenClosedWindowsButton:"
- "setUnoccludedPeekingPosition:"
- "shortcutsDelegateForIconView:"
- "showingReopenClosedWindowsButton"
- "snapPositionToNearestEdgesIfNecessaryForSpace:stageArea:configuration:"
- "space"
- "spaceByPerformingAutoLayoutWithSpace:previousSpace:configuration:options:"
- "stageAreaForSpace:configuration:"
- "startOfDayForDate:"
- "switcherContentController:removeDisplayItemFromDesktop:"
- "topAffordanceViewController:handleActionType:"
- "trackInteractionWithFeatureNamed:"
- "trackInteractionWithFeatureNamed:duration:"
- "transitionContextToUndoTransitionContext:"
- "unoccludedPeekingPosition"
- "updateOverlappingScaleAnchorPositionsForSpace:configuration:"
- "v36@0:8@?16B24@?28"
- "v84@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24d56d64B72@76"
- "validBottomStageAreaInsetsWithConfiguration:"
- "validLeadingStageAreaInsetsWithConfiguration:"
- "validTopStageAreaInsetsWithConfiguration:"
- "validTrailingStageAreaInsetsWithConfiguration:"
- "willUIUnlockFromSource:"
- "windowDragModifier"
- "{?=\"switcherContentControllerBringAppLayoutToFront\"b1\"switcherContentControllerActivatedBestAppSuggestion\"b1\"updateUserInteractionEnabledForSwitcherContentController\"b1\"updateWindowVisibilityForSwitcherContentController\"b1\"switcherContentControllerSetHomeScreenScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenAlphaWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenDimmingAlphaWithSettingsAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurProgressWithAnimationModeCompletion\"b1\"switcherContentControllerSetHomeScreenBackdropBlurType\"b1\"switcherContentControllerSetHomeScreenBackdropBlurMaterialRecipeNameWithAnimationModeCompletion\"b1\"switcherContentControllerControlsWallpaper\"b1\"switcherContentControllerSetWallpaperScaleWithAnimationModeCompletion\"b1\"switcherContentControllerSetWallpaperStyle\"b1\"switcherContentControllerSetInterfaceOrientation\"b1\"switcherContentControllerSetInterfaceOrientationFromUserResizingForDisplayItem\"b1\"switcherContentControllerRequestNewWindowForBundleIdentifier\"b1\"switcherContentControllerSetContainerStatusBarHiddenPartsHiddenAnimationDuration\"b1\"switcherContentControllerWantsToDismissMenuBar\"b1\"switcherContentControllerWantsToPeekMenuBar\"b1\"switcherContentControllerWantsToUpdateMenuBarVisibility\"b1\"switcherContentControllerDemoLayoutAttributesForDisplayItem\"b1\"switcherContentControllerSetPointerInteractionsEnabled\"b1\"switcherContentControllerShouldResignActiveForStartOfTransition\"b1\"switcherContentControllerControlsHomeScreenContents\"b1\"switcherContentControllerSetCacheAsynchronousRenderingSurfaces\"b1\"cancelActiveGestureForSwitcherContentController\"b1\"switcherContentControllerReopenHiddenAppLayoutsWithBundleIdentifier\"b1\"switcherContentControllerLayoutStateTransitionDidEndWithTransitionContext\"b1\"switcherContentControllerTransformForCardUnderSheetForBoundsSize\"b1\"switcherContentControllerMoveDisplayItemFromOtherDisplay\"b1\"presentContinuousExposeStripRevealGrabberTongueImmediatelyForSwitcherContentController\"b1\"tickleContinuousExposeStripRevealGrabberTongueIfVisibleForSwitcherContentController\"b1\"switcherContentControllerDidUpdateVisibleHomeAffordances\"b1\"switcherContentControllerRemoveDisplayItemFromDesktop\"b1\"switcherContentControllerRequestDismissalForHomeScreenBackgroundTaps\"b1}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8Q16@24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}64@0:8@16@24{UIEdgeInsets=dddd}32"
- "\xa9"

```
