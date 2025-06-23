## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4552.106.0.0.0
-  __TEXT.__text: 0xa628b0
-  __TEXT.__auth_stubs: 0x5510
+4556.102.0.0.0
+  __TEXT.__text: 0xa66238
+  __TEXT.__auth_stubs: 0x5520
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb5970
-  __TEXT.__const: 0x12b90
-  __TEXT.__oslogstring: 0x5cd55
-  __TEXT.__cstring: 0x7b7de
-  __TEXT.__gcc_except_tab: 0x16818
+  __TEXT.__objc_methlist: 0xb5c40
+  __TEXT.__const: 0x12b80
+  __TEXT.__oslogstring: 0x5d059
+  __TEXT.__cstring: 0x7bb14
+  __TEXT.__gcc_except_tab: 0x168b8
   __TEXT.__ustring: 0xcac
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2aba8
+  __TEXT.__unwind_info: 0x2ac78
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x21de5
-  __TEXT.__objc_methname: 0x1c8c47
-  __TEXT.__objc_methtype: 0x4bd8b
-  __TEXT.__objc_stubs: 0xf0be0
-  __DATA_CONST.__got: 0xa098
-  __DATA_CONST.__const: 0x1c538
-  __DATA_CONST.__objc_classlist: 0x51d0
+  __TEXT.__objc_classname: 0x21dcc
+  __TEXT.__objc_methname: 0x1c9729
+  __TEXT.__objc_methtype: 0x4c00a
+  __TEXT.__objc_stubs: 0xf11a0
+  __DATA_CONST.__got: 0xa0a0
+  __DATA_CONST.__const: 0x1c5d0
+  __DATA_CONST.__objc_classlist: 0x51c8
   __DATA_CONST.__objc_catlist: 0x348
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x49b10
+  __DATA_CONST.__objc_selrefs: 0x49ce0
   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x3f00
-  __DATA_CONST.__objc_arraydata: 0x17c8
-  __AUTH_CONST.__auth_got: 0x2aa0
-  __AUTH_CONST.__const: 0x10678
-  __AUTH_CONST.__cfstring: 0x6de40
-  __AUTH_CONST.__objc_const: 0x263a20
-  __AUTH_CONST.__objc_arrayobj: 0x1710
-  __AUTH_CONST.__objc_doubleobj: 0x5f0
+  __DATA_CONST.__objc_arraydata: 0x17e0
+  __AUTH_CONST.__auth_got: 0x2aa8
+  __AUTH_CONST.__const: 0x10718
+  __AUTH_CONST.__cfstring: 0x6e0a0
+  __AUTH_CONST.__objc_const: 0x263b00
+  __AUTH_CONST.__objc_arrayobj: 0x1728
+  __AUTH_CONST.__objc_doubleobj: 0x600
   __AUTH_CONST.__objc_intobj: 0x2b68
   __AUTH_CONST.__objc_dictobj: 0x2f8
-  __AUTH.__objc_data: 0x10540
-  __DATA.__objc_ivar: 0xf020
+  __AUTH.__objc_data: 0x104f0
+  __DATA.__objc_ivar: 0xf040
   __DATA.__data: 0x1f680
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xac8

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: B3AFC0DD-F4CD-3CCB-B8F4-480E1EDF6318
-  Functions: 69197
-  Symbols:   234180
-  CStrings:  102978
+  UUID: D614885C-607B-39E1-B91F-A3C41176BC1B
+  Functions: 69268
+  Symbols:   234385
+  CStrings:  103107
 
Symbols:
+ +[SBDisplayItem displayItemForWorkspaceEntity:]
+ +[SBRecordingIndicatorVisualRepresentation indicatorFrameForScreenType:screen:style:]
+ -[SBAppExposeWindowingModifier canPerformKeyboardShortcutAction:forBundleIdentifier:]
+ -[SBApplicationController isApplicationAlwaysAvailableForInfo:]
+ -[SBApplicationController isApplicationAlwaysAvailableForProxy:]
+ -[SBContinuousExposeWindowDragContainerGestureSwitcherModifier isHitTestBlockingViewVisible]
+ -[SBContinuousExposeWindowDragContainerGestureSwitcherModifier setState:]
+ -[SBCoverSheetIconFlyInAnimator _cleanupAnimation].cold.1
+ -[SBCoverSheetIconFlyInAnimator _cleanupAnimation].cold.2
+ -[SBCoverSheetIconFlyInAnimator _effectiveCenterPoint]
+ -[SBCoverSheetIconFlyInAnimator _iconViewAlphaForSpreadValue:]
+ -[SBCoverSheetIconFlyInAnimator _prepareToAnimateZPositions]
+ -[SBCoverSheetIconFlyInAnimator _referenceBounds]
+ -[SBCoverSheetSlidingViewController latestTransitionedPresentationState]
+ -[SBDynamicLightingController backlightController:willTransitionToBacklightState:source:]
+ -[SBDynamicLightingController backlightController:willTransitionToBacklightState:source:].cold.1
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier _dockProgressForResizingWindow]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier dockProgress]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier shouldConfigureInAppDockHiddenAssertion]
+ -[SBFlexibleWindowingItemResizeGestureSwitcherModifier wantsDockBehaviorAssertion]
+ -[SBFloatingDockBehaviorAssertion setAnimated:]
+ -[SBFloatingDockController floatingDockRootViewController:canHandleDataDropSession:inIconListView:]
+ -[SBFloatingDockController floatingDockRootViewController:dataDropSessionDidUpdate:inIconListView:]
+ -[SBFloatingDockRemoteContentManager _closeFileStackForIconView:animated:]
+ -[SBFloatingDockRemoteContentManager _closeFileStackForIconView:animated:].cold.1
+ -[SBFloatingDockRemoteContentManager _closeFileStackForIconView:animated:].cold.2
+ -[SBFloatingDockRemoteContentManager _shouldInsertDownloadsFolderAfterFirstDownload]
+ -[SBFloatingDockRemoteContentManager clientRequestTestHandleDownloadCompletedForFileStackIcon:iconUrl:isDownloadsFolder:]
+ -[SBFloatingDockRemoteContentManager clientRequestToAcknowledgeDidFinishAnimatingFor:withFileStackIcon:]
+ -[SBFloatingDockRemoteContentManager handleDownloadCompletedForFileStackIcon:iconUrl:isDownloadsFolder:]
+ -[SBFloatingDockRootViewController floatingDockViewController:canHandleDataDropSession:inIconListView:]
+ -[SBFloatingDockRootViewController floatingDockViewController:dataDropSessionDidUpdate:inIconListView:]
+ -[SBFluidSwitcherGestureManager _isLiveResizeGestureWithinTopEdgeResizeRegionForTouch]
+ -[SBFluidSwitcherGestureManager _shouldLiveResizeItemContainerGestureWithTouch:receiveTouch:allowedCorners:requiresVisibleCorner:allowedEdges:]
+ -[SBFluidSwitcherPanGestureRecognizer hasEdgeResizeSeenTouchOutsideHittestedView]
+ -[SBFluidSwitcherPanGestureRecognizer selectedEdge]
+ -[SBFluidSwitcherPanGestureRecognizer setHasEdgeResizeSeenTouchOutsideHittestedView:]
+ -[SBFluidSwitcherPanGestureRecognizer setSelectedEdge:]
+ -[SBFullScreenToPeekAnimationModifier initWithDirection:]
+ -[SBHomeScreenController iconManager:customInsertionGridPathForIcon:inRootFolder:]
+ -[SBLockScreenDeviceMotionEffectController performanceOptimizationUpdateQueue]
+ -[SBLockScreenDeviceMotionEffectController setPerformanceOptimizationUpdateQueue:]
+ -[SBMenuBarHeaderContainerView appendOverflowMenuView:fittingMaximumContentWidth:]
+ -[SBMenuBarHeaderContainerView appendOverflowMenuView:fittingMaximumContentWidth:].cold.1
+ -[SBMenuBarHeaderContainerView contentWidth]
+ -[SBMenuBarMainMenuView _contextMenuInteraction:overrideSuggestedActionsForConfiguration:]
+ -[SBMenuBarMainMenuView _handleTapOnClosedMenu:]
+ -[SBMenuBarMainMenuView alongsidePresentTapRecognizer]
+ -[SBMenuBarMainMenuView displayTitleWithAttributes:]
+ -[SBMenuBarMainMenuView initWithMainMenu:type:delegate:]
+ -[SBMenuBarMainMenuView isTransitioningMenuForPointerInteraction]
+ -[SBMenuBarMainMenuView overflowMenus]
+ -[SBMenuBarMainMenuView prepareToPresentMenuForPointerHover]
+ -[SBMenuBarMainMenuView presentingMenuForPointerHover]
+ -[SBMenuBarMainMenuView setAlongsidePresentTapRecognizer:]
+ -[SBMenuBarMainMenuView setOverflowMenus:]
+ -[SBMenuBarMainMenuView setPresentingMenuForPointerHover:]
+ -[SBMenuBarMainMenuView setTransitioningMenuForPointerClick:]
+ -[SBMenuBarMainMenuView transitioningMenuForPointerClick]
+ -[SBMenuBarMainMenuView type]
+ -[SBMenuBarManager _handleAdjustPresentedMenuHoverGesture:]
+ -[SBMenuBarManager adjustPresentedMenuHoverGestureRecognizer]
+ -[SBMenuBarManager maximumContentWidthForMenuBarViewController:]
+ -[SBMenuBarManager setAdjustPresentedMenuHoverGestureRecognizer:]
+ -[SBMenuBarViewController _addOverflowMenuToContainerIfNeededForcingViewLayout:]
+ -[SBMenuBarViewController _createHelpMenuProviderIfNeeded]
+ -[SBMenuBarViewController _createMainMenuViewForUIMainMenu:type:]
+ -[SBMenuBarViewController _movePresentedMenuViewToPreviouslyPresented]
+ -[SBMenuBarViewController adjustPresentedMenuForPointerOverViewInContainer:]
+ -[SBMenuBarViewController baseMainMenu]
+ -[SBMenuBarViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
+ -[SBMenuBarViewController initWithScene:delegate:loadCompletion:]
+ -[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]
+ -[SBMenuBarViewController menuSessionIsActiveForPointer]
+ -[SBMenuBarViewController setBaseMainMenu:]
+ -[SBMenuBarViewController setMenuSessionIsActiveForPointer:]
+ -[SBMenuBarViewController viewDidDisappear:]
+ -[SBMenuBarViewController willDismissContextMenuForMainMenuView:forPointerClick:]
+ -[SBMenuBarViewController willPresentContextMenuForMainMenuView:forPointerClick:]
+ -[SBPIPPegasusAdapter pictureInPictureController:displayConfigurationForApplication:]
+ -[SBRemoteTransientOverlayHostContentAdapter setShouldEmbedOverShieldedApps:]
+ -[SBRemoteTransientOverlayHostContentAdapter shouldEmbedOverShieldedApps]
+ -[SBRemoteTransientOverlayViewController shouldEmbedOverShieldedApps]
+ -[SBSASecureFlipBookElementPreferencesProvider _fallbackUpdateSecureStateStatusForInitialTransitionsWithRenderingContext:]
+ -[SBSASecureFlipBookView initWithSecureFlipBookNameAndFallbacks:].cold.1
+ -[SBSAViewDescription _setBackgroundColor:]
+ -[SBSAViewDescription backgroundColor]
+ -[SBSAViewDescriptionMutator backgroundColor]
+ -[SBSAViewDescriptionMutator setBackgroundColor:]
+ -[SBSwitcherController _handleActivateAppExposeKeyShortcut:]
+ -[SBSystemUISceneController _evaluateSceneVisibility]
+ -[SBTelephonyManager _otherSubscriptionSlot:]
+ -[SBTelephonyManager _secondaryCarrierBundleInfoIfEnabled]
+ -[SBTelephonyManager _secondarySubscriptionInfoIfEnabled]
+ -[SBTelephonyManager _secondarySubscriptionSlotIfEnabled]
+ -[SBTransientOverlayViewController shouldEmbedOverShieldedApps]
+ -[SpringBoard _handleGameOverlayShortcut:]
+ -[SpringBoard _takeScreenshotWithPresentationMode:]
+ GCC_except_table149
+ GCC_except_table190
+ GCC_except_table437
+ GCC_except_table485
+ GCC_except_table526
+ _DOCSBFolderNotificationIsDownloadsFolderKey
+ _OBJC_CLASS_$_GPUserExperienceProxy
+ _OBJC_CLASS_$_NSTextAttachment
+ _OBJC_IVAR_$_SBCoverSheetSlidingViewController._latestTransitionedPresentationState
+ _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._dockAwareIfCenterAnchored
+ _OBJC_IVAR_$_SBFluidSwitcherPanGestureRecognizer._hasEdgeResizeSeenTouchOutsideHittestedView
+ _OBJC_IVAR_$_SBFluidSwitcherPanGestureRecognizer._selectedEdge
+ _OBJC_IVAR_$_SBFullScreenToPeekAnimationModifier._direction
+ _OBJC_IVAR_$_SBInteractiveScreenshotGestureRootViewController._wallpaperEffectView
+ _OBJC_IVAR_$_SBLockScreenDeviceMotionEffectController._performanceOptimizationUpdateQueue
+ _OBJC_IVAR_$_SBMenuBarHeaderContainerView._leadingEdgeConstraint
+ _OBJC_IVAR_$_SBMenuBarHeaderContainerView._trailingConstraints
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._alongsidePresentTapRecognizer
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._overflowMenus
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._presentingMenuForPointerHover
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._transitioningMenuForPointerClick
+ _OBJC_IVAR_$_SBMenuBarMainMenuView._type
+ _OBJC_IVAR_$_SBMenuBarManager._adjustPresentedMenuHoverGestureRecognizer
+ _OBJC_IVAR_$_SBMenuBarViewController._baseMainMenu
+ _OBJC_IVAR_$_SBMenuBarViewController._menuSessionIsActiveForPointer
+ _OBJC_IVAR_$_SBRemoteTransientOverlayHostContentAdapter._shouldEmbedOverShieldedApps
+ _OBJC_IVAR_$_SBSAViewDescription._backgroundColor
+ _OBJC_IVAR_$_SBTransientOverlayViewController._shouldEmbedOverShieldedApps
+ _SFUCaptureCoordinatorOptionFallbackIndicatorFrame
+ _SFUCaptureCoordinatorOptionVerbose
+ __OBJC_$_CLASS_METHODS_SBRecordingIndicatorVisualRepresentation
+ __OBJC_$_INSTANCE_VARIABLES_SBFullScreenToPeekAnimationModifier
+ ___104-[SBFloatingDockRemoteContentManager handleDownloadCompletedForFileStackIcon:iconUrl:isDownloadsFolder:]_block_invoke
+ ___120-[SBSystemApertureSecureElementRenderingOverlayViewController _applyFlipBookComponentStatesForSecureElementPreferences:]_block_invoke.23
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.645
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.647
+ ___143-[SBFluidSwitcherGestureManager _shouldLiveResizeItemContainerGestureWithTouch:receiveTouch:allowedCorners:requiresVisibleCorner:allowedEdges:]_block_invoke
+ ___143-[SBFluidSwitcherGestureManager _shouldLiveResizeItemContainerGestureWithTouch:receiveTouch:allowedCorners:requiresVisibleCorner:allowedEdges:]_block_invoke_2
+ ___180-[SBSystemApertureSecureElementCoordinator _captureBoundsForElement:configuration:component:layoutDirection:orientation:layoutMode:containerDescription:coordinateSpace:completion:]_block_invoke.129
+ ___31-[SBApplicationController init]_block_invoke.43
+ ___31-[SBApplicationController init]_block_invoke_2.54
+ ___31-[SBApplicationController init]_block_invoke_3.55
+ ___42-[SpringBoard _handleGameOverlayShortcut:]_block_invoke
+ ___42-[SpringBoard _handleGameOverlayShortcut:]_block_invoke_2
+ ___44-[SBMenuBarHeaderContainerView contentWidth]_block_invoke
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1207
+ ___45-[SBFloatingDockController _setupStateDumper]_block_invoke.208
+ ___45-[SBFloatingDockController _setupStateDumper]_block_invoke_2.212
+ ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.85
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.750
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.781
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.812
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.917
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.805
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.921
+ ___55-[SBSALayoutTransitionProvider preferencesFromContext:]_block_invoke.17
+ ___55-[SBSALayoutTransitionProvider preferencesFromContext:]_block_invoke.17.cold.1
+ ___55-[SBSALayoutTransitionProvider preferencesFromContext:]_block_invoke_2
+ ___55-[SBSALayoutTransitionProvider preferencesFromContext:]_block_invoke_2.cold.1
+ ___55-[SBSASecureFlipBookView transitionToState:completion:]_block_invoke.15
+ ___56-[SBMenuBarMainMenuView initWithMainMenu:type:delegate:]_block_invoke
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1749
+ ___57-[SBApplicationRestrictionController initWithDataSource:]_block_invoke
+ ___58-[SBDashBoardSetupViewController _checkIfActivationLocked]_block_invoke.157
+ ___60-[SBCoverSheetIconFlyInAnimator _prepareToAnimateZPositions]_block_invoke
+ ___60-[SBCoverSheetIconFlyInAnimator _prepareToAnimateZPositions]_block_invoke_2
+ ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.927
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke_10
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke_2
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke_3
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke_4
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke_5
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke_6
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke_7
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke_8
+ ___64-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:]_block_invoke_9
+ ___65-[SBMenuBarViewController _createMainMenuViewForUIMainMenu:type:]_block_invoke
+ ___70-[SBMenuBarViewController _movePresentedMenuViewToPreviouslyPresented]_block_invoke
+ ___71-[SBCoverSheetIconFlyInAnimator _updateLabelAlphaForPresentationValue:]_block_invoke.47
+ ___72-[SBCoverSheetIconFlyInAnimator _updateSpreadMultiplierForPresentation:]_block_invoke.41
+ ___75-[SBFlexibleWindowingItemResizeGestureSwitcherModifier handleGestureEvent:]_block_invoke
+ ___76-[SBMenuBarViewController adjustPresentedMenuForPointerOverViewInContainer:]_block_invoke
+ ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.361
+ ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke.45
+ ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke_2.46
+ ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.81
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1601
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1603
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1605
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1609
+ ___91-[SBSystemApertureFakeDisplayOffTestRecipe _changeRecordingIndicatorPortalLayerVisibility:]_block_invoke.35
+ ___95-[SBFlexibleWindowingItemResizeGestureSwitcherModifier shouldConfigureInAppDockHiddenAssertion]_block_invoke
+ ___95-[SBSwitcherController _buildWindowArrangementMenuForKeyCommandRegistration:additionalOptions:]_block_invoke_7
+ ___96-[SBLockScreenDeviceMotionEffectController deviceMotionControllerDidUpdateDeviceMotionSettings:]_block_invoke
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1732
+ ___block_descriptor_108_e8_32s_e29_{CGPoint=dd}24?0{CGSize=dd}8ls32l8
+ ___block_descriptor_113_e8_32s40s48s56s64s72s_e38_B16?0"SBFluidSwitcherItemContainer"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_144_e8_32s40s48s56s64s72s80s88s96bs104r112r120r128r_e39_v40?0{CGRect={CGPoint=dd}{CGSize=dd}}8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r104l8r112l8r120l8r128l8s96l8
+ ___block_descriptor_32_e19_24?08"UIView"16l
+ ___block_descriptor_32_e21_16?0"_UIMainMenu"8l
+ ___block_descriptor_32_e31_B16?0"_UIMainMenuIdentifier"8l
+ ___block_descriptor_32_e8_v16?0Q8l
+ ___block_descriptor_40_e8_32s_e18_v16?0"UIButton"8ls32l8
+ ___block_descriptor_42_e8_32w_e28_B16?0"LSApplicationProxy"8lw32l8
+ ___block_descriptor_56_e8_32s40bs48w_e34_v16?0"_UIMainMenuStateResponse"8lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e36_v16?0"_UIMainMenuSessionResponse"8lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e22_v16?0"NSDictionary"8ls32l8s40l8s48l8
+ ___block_descriptor_63_e8_32s40bs_e11_v16?0B8B12ls32l8s40l8
+ ___block_descriptor_73_e8_32s40s48s56s64w_e8_v12?0B8lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s_e34_v28?0"SBIcon"8"SBIconView"16B24ls32l8
+ ___block_descriptor_82_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_82_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_88_e8_32s40s48r_e34_v28?0"SBIcon"8"SBIconView"16B24ls32l8s40l8r48l8
+ ___block_literal_global.1053
+ ___block_literal_global.1062
+ ___block_literal_global.1098
+ ___block_literal_global.1153
+ ___block_literal_global.1158
+ ___block_literal_global.1164
+ ___block_literal_global.1454
+ ___block_literal_global.1575
+ ___block_literal_global.1579
+ ___block_literal_global.1620
+ ___block_literal_global.1622
+ ___block_literal_global.1624
+ ___block_literal_global.1626
+ ___block_literal_global.1642
+ ___block_literal_global.1758
+ ___block_literal_global.1781
+ ___block_literal_global.1790
+ ___block_literal_global.1806
+ ___block_literal_global.215
+ ___block_literal_global.485
+ ___block_literal_global.490
+ ___block_literal_global.493
+ ___block_literal_global.540
+ ___block_literal_global.581
+ ___block_literal_global.628
+ ___block_literal_global.633
+ ___block_literal_global.650
+ ___block_literal_global.680
+ ___block_literal_global.686
+ ___block_literal_global.774
+ ___block_literal_global.809
+ ___block_literal_global.811
+ ___block_literal_global.833
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
+ ___block_literal_global.921
+ ___block_literal_global.923
+ ___block_literal_global.929
+ _class_getName
+ _objc_msgSend$_addOverflowMenuToContainerIfNeededForcingViewLayout:
+ _objc_msgSend$_closeFileStackForIconView:animated:
+ _objc_msgSend$_createHelpMenuProviderIfNeeded
+ _objc_msgSend$_createMainMenuViewForUIMainMenu:type:
+ _objc_msgSend$_dockProgressForResizingWindow
+ _objc_msgSend$_effectiveCenterPoint
+ _objc_msgSend$_evaluateSceneVisibility
+ _objc_msgSend$_fallbackUpdateSecureStateStatusForInitialTransitionsWithRenderingContext:
+ _objc_msgSend$_iconViewAlphaForSpreadValue:
+ _objc_msgSend$_isLiveResizeGestureWithinTopEdgeResizeRegionForTouch
+ _objc_msgSend$_movePresentedMenuViewToPreviouslyPresented
+ _objc_msgSend$_otherSubscriptionSlot:
+ _objc_msgSend$_prepareToAnimateZPositions
+ _objc_msgSend$_secondaryCarrierBundleInfoIfEnabled
+ _objc_msgSend$_secondarySubscriptionInfoIfEnabled
+ _objc_msgSend$_secondarySubscriptionSlotIfEnabled
+ _objc_msgSend$_setBackgroundColor:
+ _objc_msgSend$_shouldInsertDownloadsFolderAfterFirstDownload
+ _objc_msgSend$_shouldLiveResizeItemContainerGestureWithTouch:receiveTouch:allowedCorners:requiresVisibleCorner:allowedEdges:
+ _objc_msgSend$_takeScreenshotWithPresentationMode:
+ _objc_msgSend$adjustPresentedMenuForPointerOverViewInContainer:
+ _objc_msgSend$appState
+ _objc_msgSend$appTags
+ _objc_msgSend$appendOverflowMenuView:fittingMaximumContentWidth:
+ _objc_msgSend$applicationType
+ _objc_msgSend$attributedStringWithAttachment:attributes:
+ _objc_msgSend$contentCornerRadiusForViewSize:
+ _objc_msgSend$deviceInfoFloatValueForKey:
+ _objc_msgSend$displayItemForWorkspaceEntity:
+ _objc_msgSend$displayTitleWithAttributes:
+ _objc_msgSend$dragHitRegionForPoint:icon:
+ _objc_msgSend$floatingDockRootViewController:canHandleDataDropSession:inIconListView:
+ _objc_msgSend$floatingDockRootViewController:dataDropSessionDidUpdate:inIconListView:
+ _objc_msgSend$handleDownloadCompletedForFileStackIcon:iconUrl:isDownloadsFolder:
+ _objc_msgSend$hasEdgeResizeSeenTouchOutsideHittestedView
+ _objc_msgSend$hasEverUsedMultiAppConfiguration
+ _objc_msgSend$highlightTransitions
+ _objc_msgSend$iconLayerViewWithInfo:traitCollection:options:priority:
+ _objc_msgSend$indicatorFrameForScreenType:screen:style:
+ _objc_msgSend$initWithAttributedString:
+ _objc_msgSend$initWithDirection:
+ _objc_msgSend$initWithMainMenu:type:delegate:
+ _objc_msgSend$initWithMenuIdentifiers:session:
+ _objc_msgSend$initWithScene:delegate:loadCompletion:
+ _objc_msgSend$isApplicationAlwaysAvailableForProxy:
+ _objc_msgSend$isCursorActive
+ _objc_msgSend$isTransitioningMenuForPointerInteraction
+ _objc_msgSend$latestTransitionedPresentationState
+ _objc_msgSend$launchGameOverlayWithOptions:reply:
+ _objc_msgSend$loadMenuElementsForMainMenus:handler:
+ _objc_msgSend$maximumContentWidthForMenuBarViewController:
+ _objc_msgSend$menuStates
+ _objc_msgSend$overflowMenus
+ _objc_msgSend$prepareToPresentMenuForPointerHover
+ _objc_msgSend$proxy
+ _objc_msgSend$setAdjustPresentedMenuHoverGestureRecognizer:
+ _objc_msgSend$setBaseMainMenu:
+ _objc_msgSend$setEffect:
+ _objc_msgSend$setHasEdgeResizeSeenTouchOutsideHittestedView:
+ _objc_msgSend$setHasEverUsedMultiAppConfiguration:
+ _objc_msgSend$setIndicatorPortalViewsHidesSourceViewChanged
+ _objc_msgSend$setInitialMenuStateIdentifiers:
+ _objc_msgSend$setOverflowMenus:
+ _objc_msgSend$setPreferredEdgeInsets:
+ _objc_msgSend$setShouldEmbedOverShieldedApps:
+ _objc_msgSend$setSubvariant:
+ _objc_msgSend$shouldEmbedOverShieldedApps
+ _objc_msgSend$startObservingDownloadsFolder
+ _objc_msgSend$stopObservingDownloadsFolder
+ _objc_msgSend$textAttachmentWithImage:
+ _objc_msgSend$willDismissContextMenuForMainMenuView:forPointerClick:
+ _objc_msgSend$willPresentContextMenuForMainMenuView:forPointerClick:
- +[SBFloatingDockRemoteContentManager _defaultDownloadsLocation]
- -[SBAssistantController _siriCapabilitiesDidChange]
- -[SBAssistantController _updateSiriWithAppIntentsEnabled]
- -[SBAssistantController isSiriWithAppIntentsEnabled]
- -[SBAssistantController setSiriWithAppIntentsEnabled:]
- -[SBCoverSheetIconFlyInAnimator _iconScrollViewAlphaForSpreadValue:]
- -[SBCoverSheetIconFlyInAnimator floatingDockBehaviorPresentationAssertion]
- -[SBCoverSheetIconFlyInAnimator initWithFolderController:].cold.1
- -[SBCoverSheetIconFlyInAnimator setFloatingDockBehaviorPresentationAssertion:]
- -[SBDynamicLightingController backlightController:didTransitionToBacklightState:source:].cold.2
- -[SBFloatingDockRemoteContentManager _closeFileStackForIconView:].cold.1
- -[SBFloatingDockRemoteContentManager _closeFileStackForIconView:].cold.2
- -[SBFloatingDockRemoteContentManager _insertDefaultDownloadFileStackIconToFloatingDockIfNeeded]
- -[SBFloatingDockRemoteContentManager _insertDefaultDownloadFileStackIconToFloatingDockIfNeeded].cold.1
- -[SBFloatingDockRemoteContentManager _shouldInsertDefaultDownloadFileStackIcon]
- -[SBFloatingDockRemoteContentManager clientRequestTestHandleDownloadCompletedForFileStackIcon:iconUrl:]
- -[SBFloatingDockRemoteContentManager handleDownloadCompletedForFileStackIcon:iconUrl:]
- -[SBFloatingDockRemoteContentManager insertDefaultDownloadFolder]
- -[SBFluidSwitcherGestureManager _shouldLiveResizeItemContainerGestureWithTouch:receiveTouch:allowedCorners:requiresVisibleCorner:]
- -[SBInteractiveScreenshotGestureRootViewController _createMaterialViewWithFrame:groupName:isCaptureOnly:]
- -[SBMenuBarDeviceBezelCornerView .cxx_destruct]
- -[SBMenuBarDeviceBezelCornerView initWithDesiredCorner:cornerRadius:]
- -[SBMenuBarDeviceBezelCornerView layoutSubviews]
- -[SBMenuBarMainMenuView initWithMainMenu:delegate:]
- -[SBMenuBarMainMenuView prepareToPresentMenuForPointerInteraction]
- -[SBMenuBarManager leftCornerView]
- -[SBMenuBarManager needsDeviceCornerViews]
- -[SBMenuBarManager rightCornerView]
- -[SBMenuBarManager setLeftCornerView:]
- -[SBMenuBarManager setNeedsDeviceCornerViews:]
- -[SBMenuBarManager setRightCornerView:]
- -[SBMenuBarSettings forceTranslucentBackground]
- -[SBMenuBarSettings setForceTranslucentBackground:]
- -[SBMenuBarViewController initWithScene:style:delegate:loadCompletion:]
- -[SBMenuBarViewController loadMenuElementsForMainMenu:handler:]
- -[SBMenuBarViewController pointerInteraction:willEnterRegion:animator:]
- -[SBMenuBarViewController style]
- -[SBMenuBarViewController willDismissContextMenuForMainMenuView:]
- -[SBMenuBarViewController willPresentContextMenuForMainMenuView:]
- -[SBSystemUISceneController _updateShouldHideForSecureMode]
- -[SpringBoard _takeScreenshotAndEdit:]
- GCC_except_table197
- GCC_except_table221
- GCC_except_table307
- GCC_except_table419
- GCC_except_table434
- GCC_except_table471
- GCC_except_table525
- _DOCSBFolderPlaceholderLocationDownloads
- _OBJC_CLASS_$_SBMenuBarDeviceBezelCornerView
- _OBJC_IVAR_$_SBAssistantController._siriWithAppIntentsEnabled
- _OBJC_IVAR_$_SBCoverSheetIconFlyInAnimator._floatingDockBehaviorPresentationAssertion
- _OBJC_IVAR_$_SBMenuBarDeviceBezelCornerView._cornerMaskView
- _OBJC_IVAR_$_SBMenuBarDeviceBezelCornerView._desiredCorner
- _OBJC_IVAR_$_SBMenuBarHeaderContainerView._firstLeadingConstraint
- _OBJC_IVAR_$_SBMenuBarHeaderContainerView._firstTrailingConstraint
- _OBJC_IVAR_$_SBMenuBarManager._leftCornerView
- _OBJC_IVAR_$_SBMenuBarManager._needsDeviceCornerViews
- _OBJC_IVAR_$_SBMenuBarManager._rightCornerView
- _OBJC_IVAR_$_SBMenuBarSettings._forceTranslucentBackground
- _OBJC_IVAR_$_SBMenuBarViewController._style
- _OBJC_IVAR_$_SBSASecureFlipBookView._unloadedStateNameLabel
- _OBJC_METACLASS_$_SBMenuBarDeviceBezelCornerView
- __OBJC_$_CLASS_METHODS_SBFloatingDockRemoteContentManager
- __OBJC_$_INSTANCE_METHODS_SBMenuBarDeviceBezelCornerView
- __OBJC_$_INSTANCE_VARIABLES_SBMenuBarDeviceBezelCornerView
- __OBJC_CLASS_RO_$_SBMenuBarDeviceBezelCornerView
- __OBJC_METACLASS_RO_$_SBMenuBarDeviceBezelCornerView
- __SBAssistantControllerSiriCapabilitiesDidChange
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.642
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.644
- ___180-[SBSystemApertureSecureElementCoordinator _captureBoundsForElement:configuration:component:layoutDirection:orientation:layoutMode:containerDescription:coordinateSpace:completion:]_block_invoke.126
- ___31-[SBApplicationController init]_block_invoke.41
- ___31-[SBApplicationController init]_block_invoke_2.53
- ___31-[SBApplicationController init]_block_invoke_3.54
- ___35-[SBMenuBarManager _dismissMenuBar]_block_invoke_4
- ___38-[SBMenuBarManager setMenuBarVisible:]_block_invoke_5
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1204
- ___45-[SBFloatingDockController _setupStateDumper]_block_invoke.203
- ___45-[SBFloatingDockController _setupStateDumper]_block_invoke_2.207
- ___50-[SBMenuBarViewController _runCommandFromContext:]_block_invoke.75
- ___51-[SBMenuBarMainMenuView initWithMainMenu:delegate:]_block_invoke
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.747
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.778
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.809
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.914
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.802
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.918
- ___55-[SBSASecureFlipBookView transitionToState:completion:]_block_invoke.17
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1738
- ___58-[SBDashBoardSetupViewController _checkIfActivationLocked]_block_invoke.151
- ___59-[SBMenuBarViewController _loadAllMainMenusWithCompletion:]_block_invoke_4
- ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.924
- ___63-[SBMenuBarViewController loadMenuElementsForMainMenu:handler:]_block_invoke
- ___63-[SBMenuBarViewController loadMenuElementsForMainMenu:handler:]_block_invoke_2
- ___63-[SBMenuBarViewController loadMenuElementsForMainMenu:handler:]_block_invoke_3
- ___63-[SBMenuBarViewController loadMenuElementsForMainMenu:handler:]_block_invoke_4
- ___63-[SBMenuBarViewController loadMenuElementsForMainMenu:handler:]_block_invoke_5
- ___63-[SBMenuBarViewController loadMenuElementsForMainMenu:handler:]_block_invoke_6
- ___63-[SBMenuBarViewController loadMenuElementsForMainMenu:handler:]_block_invoke_7
- ___63-[SBMenuBarViewController loadMenuElementsForMainMenu:handler:]_block_invoke_8
- ___63-[SBMenuBarViewController loadMenuElementsForMainMenu:handler:]_block_invoke_9
- ___71-[SBCoverSheetIconFlyInAnimator _updateLabelAlphaForPresentationValue:]_block_invoke.48
- ___72-[SBCoverSheetIconFlyInAnimator _updateSpreadMultiplierForPresentation:]_block_invoke.42
- ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.358
- ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke.44
- ___84-[SBRecordingIndicatorViewController _updateIndicatorVisibilityWithSpringAnimation:]_block_invoke_2.45
- ___88-[SBCoverSheetIconFlyInAnimator animateZPositionsToFraction:completionGroup:completion:]_block_invoke_4
- ___88-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:]_block_invoke.71
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1590
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1592
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1594
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1598
- ___91-[SBSystemApertureFakeDisplayOffTestRecipe _changeRecordingIndicatorPortalLayerVisibility:]_block_invoke.32
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1721
- ___block_descriptor_120_e8_32s40s48r_e34_v28?0"SBIcon"8"SBIconView"16B24ls32l8s40l8r48l8
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88bs96r104r112r120r_e39_v40?0{CGRect={CGPoint=dd}{CGSize=dd}}8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r96l8r104l8r112l8r120l8s88l8
- ___block_descriptor_33_e28_B16?0"LSApplicationProxy"8l
- ___block_descriptor_48_e8_32bs40w_e34_v16?0"_UIMainMenuStateResponse"8lw40l8s32l8
- ___block_descriptor_48_e8_32bs40w_e36_v16?0"_UIMainMenuSessionResponse"8lw40l8s32l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_49_e8_32s_e18_v16?0"UIButton"8ls32l8
- ___block_descriptor_55_e8_32s40bs_e11_v16?0B8B12ls32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e23_v32?0"SBIcon"8Q16^B24lr40l8s32l8r48l8
- ___block_descriptor_56_e8_32s40s48bs_e26_v16?0"_UIMainMenuState"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e21_v16?0"_UIMainMenu"8ls32l8s40l8s48l8
- ___block_descriptor_66_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_66_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_81_e8_32s40s48s56s64w_e8_v12?0B8lw64l8s32l8s40l8s48l8s56l8
- ___block_literal_global.1050
- ___block_literal_global.1059
- ___block_literal_global.1095
- ___block_literal_global.1147
- ___block_literal_global.1155
- ___block_literal_global.1161
- ___block_literal_global.1446
- ___block_literal_global.1600
- ___block_literal_global.1609
- ___block_literal_global.1613
- ___block_literal_global.1615
- ___block_literal_global.1631
- ___block_literal_global.1747
- ___block_literal_global.1770
- ___block_literal_global.1779
- ___block_literal_global.1795
- ___block_literal_global.329
- ___block_literal_global.450
- ___block_literal_global.455
- ___block_literal_global.458
- ___block_literal_global.537
- ___block_literal_global.578
- ___block_literal_global.619
- ___block_literal_global.630
- ___block_literal_global.647
- ___block_literal_global.677
- ___block_literal_global.683
- ___block_literal_global.771
- ___block_literal_global.806
- ___block_literal_global.830
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
- ___block_literal_global.920
- ___block_literal_global.926
- _kAFSiriCapabilitiesDidChangeNotification
- _kSFUSecureFlipBookRecordingVerbose
- _objc_msgSend$_createMaterialViewWithFrame:groupName:isCaptureOnly:
- _objc_msgSend$_defaultDownloadsLocation
- _objc_msgSend$_iconScrollViewAlphaForSpreadValue:
- _objc_msgSend$_insertDefaultDownloadFileStackIconToFloatingDockIfNeeded
- _objc_msgSend$_secondaryCarrierBundleInfo
- _objc_msgSend$_shouldInsertDefaultDownloadFileStackIcon
- _objc_msgSend$_shouldLiveResizeItemContainerGestureWithTouch:receiveTouch:allowedCorners:requiresVisibleCorner:
- _objc_msgSend$_siriCapabilitiesDidChange
- _objc_msgSend$_takeScreenshotAndEdit:
- _objc_msgSend$_updateShouldHideForSecureMode
- _objc_msgSend$_updateSiriWithAppIntentsEnabled
- _objc_msgSend$forceTranslucentBackground
- _objc_msgSend$handleDownloadCompletedForFileStackIcon:iconUrl:
- _objc_msgSend$iconLayerViewWithInfo:traitCollection:options:
- _objc_msgSend$initWithDesiredCorner:cornerRadius:
- _objc_msgSend$initWithMainMenu:delegate:
- _objc_msgSend$initWithScene:style:delegate:loadCompletion:
- _objc_msgSend$isSiriWithAppIntentsEnabled
- _objc_msgSend$loadMenuElementsForMainMenu:handler:
- _objc_msgSend$materialViewWithRecipeNamed:
- _objc_msgSend$prepareToPresentMenuForPointerInteraction
- _objc_msgSend$setInvertsMask:
- _objc_msgSend$setSiriWithAppIntentsEnabled:
- _objc_msgSend$swaiEnabled
- _objc_msgSend$willDismissContextMenuForMainMenuView:
- _objc_msgSend$willPresentContextMenuForMainMenuView:
CStrings:
+ "-[SBApplicationRestrictionController initWithDataSource:]"
+ "@\"FBSDisplayConfiguration\"32@0:8@\"PGPictureInPictureController\"16@\"PGPictureInPictureApplication\"24"
+ "@\"SBHIconGridPath\"40@0:8@\"SBHIconManager\"16@\"SBIcon\"24@\"SBRootFolder\"32"
+ "@\"UIDropProposal\"40@0:8@\"SBFloatingDockRootViewController\"16@\"<UIDropSession>\"24@\"SBIconListView\"32"
+ "@\"UIDropProposal\"40@0:8@\"SBFloatingDockViewController\"16@\"<UIDropSession>\"24@\"SBIconListView\"32"
+ "@16@?0@\"_UIMainMenu\"8"
+ "@24@?0@8@\"UIView\"16"
+ "ADD_NEW_WINDOW_SHORTCUT_ITEM_TITLE"
+ "B16@?0@\"_UIMainMenuIdentifier\"8"
+ "B40@0:8@\"SBFloatingDockRootViewController\"16@\"<UIDropSession>\"24@\"SBIconListView\"32"
+ "B40@0:8@\"SBFloatingDockViewController\"16@\"<UIDropSession>\"24@\"SBIconListView\"32"
+ "B52@0:8@16@24Q32B40Q44"
+ "Backlight activating - Releasing assertion to disable dynamic lighting output"
+ "Client finishes closing animation."
+ "Client finishes opening animation."
+ "Device Motion Effect performance optimization settings have changed. areAllPerformanceOptimizationsDisabled: %{BOOL}u, Reduced Motion(OptimizationEnabled: %{BOOL}u, ReducedMotionSetting: %{BOOL}u), Low Power Mode(OptimizationEnabled: %{BOOL}u, LowPowerModeSetting: %{BOOL}u), Wallpaper Obscured(OptimizationEnabled: %{BOOL}u, isWallpaperObscured: %{BOOL}u), User Presence(OptimizationEnabled: %{BOOL}u, isUserPresenceDetected: %{BOOL}u), Significant Motion (OptimizationEnabled: %{BOOL}u, hasSignificantMotion: %{BOOL}u), Backlight Change Source(OptimizationEnabled: %{BOOL}u)"
+ "Failed to insert downloads folder into the floating dock after first download even though we should, url %@"
+ "GAME_OVERLAY_SHORTCUT_DISCOVERABILITY"
+ "Game overlay key shortcut handled by game policy"
+ "Game overlay key shortcut not handled by game policy."
+ "Icon URL already exists in floating dock, will not insert download folder again, url %@"
+ "Initializing with isSystemAssistantExperienceEnabled: %{BOOL}u; isSystemAssistantExperiencePersistentSiriEnabled: %{BOOL}u; isHomeAffordanceDoubleTapGestureEnabled: %{BOOL}u; isVisualSearchEnabled: %{BOOL}u"
+ "Not preparing icon animator due to reduced motion"
+ "Preventing <%{public}s: %{public}p> from receiving <%{public}s: %p> because the switcher does not own the home gesture."
+ "Reusing icon animator due to reversed in progress animation"
+ "SBMenuBarHeaderContainerView.m"
+ "SBSALayoutTransitionProvider.m"
+ "SHOW_ALL_WINDOWS_SHORTCUT_ITEM_TITLE"
+ "Secure transition already applied for component %@ (->%@). (_secureStateStatus->%@)"
+ "Successfully inserted downloads folder into the floating dock after first download, url %@"
+ "T@\"NSArray\",&,N,V_overflowMenus"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_performanceOptimizationUpdateQueue"
+ "T@\"UIColor\",&,N,S_setBackgroundColor:,V_backgroundColor"
+ "T@\"UIHoverGestureRecognizer\",&,N,V_adjustPresentedMenuHoverGestureRecognizer"
+ "T@\"UITapGestureRecognizer\",&,N,V_alongsidePresentTapRecognizer"
+ "T@\"_UIMainMenu\",&,N,V_baseMainMenu"
+ "TB,N,V_hasEdgeResizeSeenTouchOutsideHittestedView"
+ "TB,N,V_menuSessionIsActiveForPointer"
+ "TB,N,V_presentingMenuForPointerHover"
+ "TB,N,V_shouldEmbedOverShieldedApps"
+ "TB,N,V_transitioningMenuForPointerClick"
+ "TB,R,N,GisTransitioningMenuForPointerInteraction"
+ "TB,R,N,V_shouldEmbedOverShieldedApps"
+ "Tq,R,N,V_latestTransitionedPresentationState"
+ "UseLaunchServicesForAppRestrictions"
+ "User defaults shouldInsertDownloads is %d"
+ "We should only be dealing with app menu views when overflowing menu content"
+ "[%{public}lu] Change Micro indicator state to accepting"
+ "[%{public}lu] Container property identitifier %@ is no longer being tracked for milestone: %f; assume that indicates the milestone is completed and we can push forward our state machine. IndicatorAppearStateContext is currently: %@"
+ "[Overlay] FlipBooks failed to load. Allowing state machine forward progress."
+ "_addOverflowMenuToContainerIfNeededForcingViewLayout:"
+ "_adjustPresentedMenuHoverGestureRecognizer"
+ "_alongsidePresentTapRecognizer"
+ "_baseMainMenu"
+ "_closeFileStackForIconView:animated:"
+ "_contextMenuInteraction:overrideSuggestedActionsForConfiguration:"
+ "_createHelpMenuProviderIfNeeded"
+ "_createMainMenuViewForUIMainMenu:type:"
+ "_dockAwareIfCenterAnchored"
+ "_dockProgressForResizingWindow"
+ "_effectiveCenterPoint"
+ "_evaluateSceneVisibility"
+ "_fallbackUpdateSecureStateStatusForInitialTransitionsWithRenderingContext:"
+ "_handleAdjustPresentedMenuHoverGesture:"
+ "_handleGameOverlayShortcut:"
+ "_handleTapOnClosedMenu:"
+ "_hasEdgeResizeSeenTouchOutsideHittestedView"
+ "_iconViewAlphaForSpreadValue:"
+ "_isLiveResizeGestureWithinTopEdgeResizeRegionForTouch"
+ "_latestTransitionedPresentationState"
+ "_leadingEdgeConstraint"
+ "_menuSessionIsActiveForPointer"
+ "_movePresentedMenuViewToPreviouslyPresented"
+ "_otherSubscriptionSlot:"
+ "_overflowMenus"
+ "_performanceOptimizationUpdateQueue"
+ "_prepareToAnimateZPositions"
+ "_presentingMenuForPointerHover"
+ "_secondaryCarrierBundleInfoIfEnabled"
+ "_secondarySubscriptionInfoIfEnabled"
+ "_secondarySubscriptionSlotIfEnabled"
+ "_setBackgroundColor:"
+ "_shouldEmbedOverShieldedApps"
+ "_shouldInsertDownloadsFolderAfterFirstDownload"
+ "_shouldLiveResizeItemContainerGestureWithTouch:receiveTouch:allowedCorners:requiresVisibleCorner:allowedEdges:"
+ "_takeScreenshotWithPresentationMode:"
+ "_trailingConstraints"
+ "_transitioningMenuForPointerClick"
+ "a1q"
+ "adjustPresentedMenuForPointerOverViewInContainer:"
+ "adjustPresentedMenuHoverGestureRecognizer"
+ "alongsidePresentTapRecognizer"
+ "appState"
+ "appTags"
+ "appendOverflowMenuView:fittingMaximumContentWidth:"
+ "applicationType"
+ "arrow.down.forward.and.arrow.up.backward.rectangle"
+ "arrow.up.backward.and.arrow.down.forward.rectangle"
+ "attributedStringWithAttachment:attributes:"
+ "a\xb1"
+ "baseMainMenu"
+ "canRenderAboveBlankingContext"
+ "chevron.left.2"
+ "chevron.right.2"
+ "clientRequestTestHandleDownloadCompletedForFileStackIcon:iconUrl:isDownloadsFolder:"
+ "clientRequestToAcknowledgeDidFinishAnimatingFor:withFileStackIcon:"
+ "com.apple.SpringBoardFramework.SBLockScreenDeviceMotionEffectController.queue"
+ "contentCornerRadiusForViewSize:"
+ "deviceInfoFloatValueForKey:"
+ "displayItemForWorkspaceEntity:"
+ "displayTitleWithAttributes:"
+ "dragHitRegionForPoint:icon:"
+ "e"
+ "floatingDockRootViewController:canHandleDataDropSession:inIconListView:"
+ "floatingDockRootViewController:dataDropSessionDidUpdate:inIconListView:"
+ "floatingDockViewController:canHandleDataDropSession:inIconListView:"
+ "floatingDockViewController:dataDropSessionDidUpdate:inIconListView:"
+ "handleDownloadCompletedForFileStackIcon:iconUrl:isDownloadsFolder:"
+ "hasEdgeResizeSeenTouchOutsideHittestedView"
+ "hasEverUsedMultiAppConfiguration"
+ "icon animator %p - prepare"
+ "icon animator %p setting folder view alpha %f"
+ "icon animator %p setting icon scroll view alpha 1.0 (reversal)"
+ "icon animator: %p cleaning up animation"
+ "icon scroll view is still alpha == 0 after cleanup, iconCount: %lu"
+ "icon scroll view layer opacity is still == 0 after cleanup, iconCount: %lu"
+ "iconLayerViewWithInfo:traitCollection:options:priority:"
+ "iconManager:customInsertionGridPathForIcon:inRootFolder:"
+ "iconTypeIdentifierForImageForIcon:"
+ "indicatorFrameForScreenType:screen:style:"
+ "initWithAttributedString:"
+ "initWithDirection:"
+ "initWithMainMenu:type:delegate:"
+ "initWithMenuIdentifiers:session:"
+ "initWithScene:delegate:loadCompletion:"
+ "inset.filled.center.rectangle"
+ "inset.filled.trailinghalf.arrow.trailing.rectangle"
+ "isApplicationAlwaysAvailableForInfo:"
+ "isApplicationAlwaysAvailableForProxy:"
+ "isCursorActive"
+ "isTransitioningMenuForPointerInteraction"
+ "latestTransitionedPresentationState"
+ "launchGameOverlayWithOptions:reply:"
+ "lefttwothird"
+ "loadMenuElementsForMainMenus:handler:"
+ "maximumContentWidthForMenuBarViewController:"
+ "menuSessionIsActiveForPointer"
+ "menuStates"
+ "notificationViewControllerDidUpdateGlassInterfaceStyleToUserInterfaceStyle:notificationVC:"
+ "overflowMenus"
+ "performanceOptimizationUpdateQueue"
+ "pictureInPictureController:displayConfigurationForApplication:"
+ "plus.rectangle"
+ "prepareToPresentMenuForPointerHover"
+ "presentingMenuForPointerHover"
+ "proxy"
+ "rectangle.grid.2x2"
+ "righttwothird"
+ "setAdjustPresentedMenuHoverGestureRecognizer:"
+ "setAlongsidePresentTapRecognizer:"
+ "setBaseMainMenu:"
+ "setEffect:"
+ "setHasEdgeResizeSeenTouchOutsideHittestedView:"
+ "setHasEverUsedMultiAppConfiguration:"
+ "setInitialMenuStateIdentifiers:"
+ "setMenuSessionIsActiveForPointer:"
+ "setOverflowMenus:"
+ "setPerformanceOptimizationUpdateQueue:"
+ "setPreferredEdgeInsets:"
+ "setPresentingMenuForPointerHover:"
+ "setShouldEmbedOverShieldedApps:"
+ "setSubvariant:"
+ "setTransitioningMenuForPointerClick:"
+ "shouldEmbedOverShieldedApps"
+ "startObservingDownloadsFolder"
+ "stopObservingDownloadsFolder"
+ "textAttachmentWithImage:"
+ "tile-role-left-two-third"
+ "tile-role-right-two-third"
+ "transitioningMenuForPointerClick"
+ "transitioningMenuForPointerInteraction"
+ "unknown edge '%ld"
+ "v28@0:8@\"SBMenuBarMainMenuView\"16B24"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8q16@\"NCNotificationViewController\"24"
+ "v36@0:8@\"NSString\"16@\"NSURL\"24B32"
+ "volumeSlider"
+ "willDismissContextMenuForMainMenuView:forPointerClick:"
+ "willPresentContextMenuForMainMenuView:forPointerClick:"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}40@0:8Q16@24Q32"
+ "\xf0\xf0\xf0!"
- "!\""
- "@\"SBMenuBarDeviceBezelCornerView\""
- "@48@0:8@16q24@32@?40"
- "B44@0:8@16@24Q32B40"
- "Backlight activated - Releasing assertion to disable dynamic lighting output"
- "Bezel Effects Hint Droplet Window: Hidden"
- "Bezel Effects Hint Droplet Window: Visible"
- "Bezel Effects Window: Hidden"
- "Bezel Effects Window: Visible"
- "Bezel Effects: Cancel prelude animatedly"
- "Bezel Effects: issuing prelude token: %@"
- "Bezel Effects: issuing zoom up token: %@"
- "Device Motion Effect performance optimization settings have changed. areAllPerformanceOptimizationsDisabled: %{BOOL}u, Reduced Motion(OptimizationEnabled: %{BOOL}u, ReducedMotionSetting: %{BOOL}u), Low Power Mode(OptimizationEnabled: %{BOOL}u, LowPowerModeSetting: %{BOOL}u), Wallpaper Obscured(OptimizationEnabled: %{BOOL}u, isWallpaperObscured: %{BOOL}u), User Presence(OptimizationEnabled: %{BOOL}u, isUserPresenceDetected: %{BOOL}u), Significant Motion (OptimizationEnabled: %{BOOL}u), Backlight Change Source(OptimizationEnabled: %{BOOL}u)"
- "Force Translucent Background"
- "Initializing with isSystemAssistantExperienceEnabled: %{BOOL}u; isSiriWithAppIntentsEnabled: %{BOOL}u; isSystemAssistantExperiencePersistentSiriEnabled: %{BOOL}u; isHomeAffordanceDoubleTapGestureEnabled: %{BOOL}u; isVisualSearchEnabled: %{BOOL}u"
- "Peek is showing"
- "Preventing the switcher live resize touch gesture because current layout state doesn't contain leaf app layout. %@ %@"
- "Preventing the switcher live resize touch gesture because didn't hit test. %@ %@"
- "SBMenuBarDeviceBezelCornerView"
- "T@\"SBFloatingDockBehaviorAssertion\",&,N,V_floatingDockBehaviorPresentationAssertion"
- "T@\"SBMenuBarDeviceBezelCornerView\",&,N,V_leftCornerView"
- "T@\"SBMenuBarDeviceBezelCornerView\",&,N,V_rightCornerView"
- "TB,N,GisSiriWithAppIntentsEnabled,V_siriWithAppIntentsEnabled"
- "TB,N,V_forceTranslucentBackground"
- "TB,N,V_needsDeviceCornerViews"
- "Updating isSiriWithAppIntentsEnabled to %{BOOL}u"
- "[FileStackURLSourcePersist] Failed to add download folder to floating dock even though it should have been added."
- "_cornerMaskView"
- "_createMaterialViewWithFrame:groupName:isCaptureOnly:"
- "_defaultDownloadsLocation"
- "_desiredCorner"
- "_firstLeadingConstraint"
- "_firstTrailingConstraint"
- "_floatingDockBehaviorPresentationAssertion"
- "_forceTranslucentBackground"
- "_iconScrollViewAlphaForSpreadValue:"
- "_insertDefaultDownloadFileStackIconToFloatingDockIfNeeded"
- "_leftCornerView"
- "_needsDeviceCornerViews"
- "_rightCornerView"
- "_shouldInsertDefaultDownloadFileStackIcon"
- "_shouldLiveResizeItemContainerGestureWithTouch:receiveTouch:allowedCorners:requiresVisibleCorner:"
- "_siriCapabilitiesDidChange"
- "_siriWithAppIntentsEnabled"
- "_takeScreenshotAndEdit:"
- "_unloadedStateNameLabel"
- "_updateShouldHideForSecureMode"
- "_updateSiriWithAppIntentsEnabled"
- "aAa"
- "clientRequestTestHandleDownloadCompletedForFileStackIcon:iconUrl:"
- "floatingDockBehaviorPresentationAssertion"
- "forceTranslucentBackground"
- "handleDownloadCompletedForFileStackIcon:iconUrl:"
- "icon animator: %p cleanup animation"
- "iconLayerViewWithInfo:traitCollection:options:"
- "initWithDesiredCorner:cornerRadius:"
- "initWithMainMenu:delegate:"
- "initWithScene:style:delegate:loadCompletion:"
- "insertDefaultDownloadFolder"
- "isSiriWithAppIntentsEnabled"
- "leftCornerView"
- "loadMenuElementsForMainMenu:handler:"
- "materialViewWithRecipeNamed:"
- "needsDeviceCornerViews"
- "notificationViewControllerDidUpdateGlassInterfaceStyleToUserInterfaceStyle:"
- "prepareToPresentMenuForPointerInteraction"
- "reevaluateSystemGlowEffect: %{bool}u viewController: %@"
- "rightCornerView"
- "setFloatingDockBehaviorPresentationAssertion:"
- "setForceTranslucentBackground:"
- "setInvertsMask:"
- "setLeftCornerView:"
- "setNeedsDeviceCornerViews:"
- "setRightCornerView:"
- "setSiriWithAppIntentsEnabled:"
- "siriWithAppIntentsEnabled"
- "swaiEnabled"
- "v16@?0@\"_UIMainMenuState\"8"
- "v32@0:8@\"_UIMainMenu\"16@?<v@?@\"NSArray\">24"
- "willDismissContextMenuForMainMenuView:"
- "willPresentContextMenuForMainMenuView:"

```
