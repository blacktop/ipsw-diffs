## SpringBoard

> `/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard`

```diff

-3050.3.8.0.0
-  __TEXT.__text: 0x39534
-  __TEXT.__objc_methlist: 0x4d4c
+3050.3.12.0.0
+  __TEXT.__text: 0x3f988
+  __TEXT.__objc_methlist: 0x52c4
   __TEXT.__dlopen_cstrs: 0x98
-  __TEXT.__const: 0xe8
-  __TEXT.__gcc_except_tab: 0xb2c
-  __TEXT.__cstring: 0xa3f2
-  __TEXT.__oslogstring: 0xd4d
-  __TEXT.__unwind_info: 0x1728
+  __TEXT.__const: 0xf0
+  __TEXT.__gcc_except_tab: 0xca0
+  __TEXT.__cstring: 0xad00
+  __TEXT.__oslogstring: 0x11c5
+  __TEXT.__unwind_info: 0x1930
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe18
-  __DATA_CONST.__objc_classlist: 0x970
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__const: 0xfb8
+  __DATA_CONST.__objc_classlist: 0x9c0
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2650
+  __DATA_CONST.__objc_selrefs: 0x29e8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x5d0
-  __AUTH_CONST.__const: 0x770
-  __AUTH_CONST.__cfstring: 0xbb40
-  __AUTH_CONST.__objc_const: 0xb390
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __DATA_CONST.__got: 0x620
+  __AUTH_CONST.__const: 0x830
+  __AUTH_CONST.__cfstring: 0xc700
+  __AUTH_CONST.__objc_const: 0xbb90
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xb90
-  __DATA.__objc_ivar: 0x68
-  __DATA.__data: 0x248
+  __AUTH.__objc_data: 0xeb0
+  __DATA.__objc_ivar: 0x8c
+  __DATA.__data: 0x2a8
   __DATA.__common: 0x11
   __DATA_DIRTY.__objc_data: 0x52d0
   __DATA_DIRTY.__data: 0x4

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1624
-  Symbols:   3860
-  CStrings:  1674
+  Functions: 1762
+  Symbols:   4105
+  CStrings:  1786
 
Symbols:
+ +[AXSpringBoardGlue handleActiveDisplayChangeForHardwareIdentifier:]
+ +[AXSpringBoardGlue handleOrientationChangeToDeviceOrientation:]
+ +[SBHomeScreenControllerAccessibility _accessibilityPerformValidations:]
+ +[SBHomeScreenControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[SBHomeScreenControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[SBNSObjectDisplayContentAccessibility _accessibilityPerformValidations:]
+ +[SBNSObjectDisplayContentAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[SBNSObjectDisplayContentAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[SBPosterEditingTransientOverlayViewControllerAccessibility _accessibilityPerformValidations:]
+ +[SBPosterEditingTransientOverlayViewControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[SBPosterEditingTransientOverlayViewControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[SBSplitViewHandleNubViewAccessibility _accessibilityPerformValidations:]
+ +[SBSplitViewHandleNubViewAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[SBSplitViewHandleNubViewAccessibility(SafeCategory) safeCategoryTargetClassName]
+ +[SpeakScreenUnintendedInteractionObserver sharedObserver]
+ -[AXSBFolderFocusState .cxx_destruct]
+ -[AXSBFolderFocusState contributesHint]
+ -[AXSBFolderFocusState focusedItemBeforeOpening]
+ -[AXSBFolderFocusState forgetStateBeforeOpening]
+ -[AXSBFolderFocusState keyWindowBeforeOpening]
+ -[AXSBFolderFocusState mayHoldKeyboardFocus]
+ -[AXSBFolderFocusState openingFolder]
+ -[AXSBFolderFocusState openingToken]
+ -[AXSBFolderFocusState setContributesHint:]
+ -[AXSBFolderFocusState setFocusedItemBeforeOpening:]
+ -[AXSBFolderFocusState setKeyWindowBeforeOpening:]
+ -[AXSBFolderFocusState setOpeningFolder:]
+ -[AXSBFolderFocusState setOpeningToken:]
+ -[AXSBFolderFocusState setTookKeyboardFocus:]
+ -[AXSBFolderFocusState tookKeyboardFocus]
+ -[SBChargingAlertElementAccessibility _updateBatteryContent]
+ -[SBCoverSheetPresentationManagerAccessibility _axIsOnInactiveDisplay]
+ -[SBDashBoardLockScreenEnvironmentAccessibility _axIsDisplayContentModeTransitionWakeWhileAwake:]
+ -[SBFloatingDockWindowAccessibility _accessibilityIgnoresStatusBarFrame]
+ -[SBFloatingDockWindowAccessibility _axDockIsCoveredByFullScreenContent]
+ -[SBFloatingDockWindowAccessibility _axDockIsCoveredByHomeScreenFolder]
+ -[SBFloatingDockWindowAccessibility _axDockIsOccludedByOverlay]
+ -[SBFloatingDockWindowAccessibility _axIsNonPrimaryDisplayDockWindow]
+ -[SBFluidSwitcherItemContainerAccessibility _accessibilityArrangementActions]
+ -[SBFluidSwitcherViewControllerAccessibility _axPendingScrollAppLayout]
+ -[SBFluidSwitcherViewControllerAccessibility _setAXPendingScrollAppLayout:]
+ -[SBHomeScreenControllerAccessibility _accessibilityIsWindowBehindOpenFolder:]
+ -[SBHomeScreenControllerAccessibility _accessibilityOpenFolderHoldsKeyboardFocus]
+ -[SBHomeScreenControllerAccessibility _axFolderFocusState]
+ -[SBHomeScreenControllerAccessibility _axFolderWindow]
+ -[SBHomeScreenControllerAccessibility _axHomeScreenKeyWindow]
+ -[SBHomeScreenControllerAccessibility _axHomeScreenWindow]
+ -[SBHomeScreenControllerAccessibility _axOpenedFolderControllerInFolderWindow]
+ -[SBHomeScreenControllerAccessibility _axRestoreKeyboardFocusToView:]
+ -[SBHomeScreenControllerAccessibility _axUpdateFolderKeyboardFocusHint]
+ -[SBHomeScreenControllerAccessibility _updateHomeScreenVisibleKeyboardFocusDeferringRule]
+ -[SBHomeScreenControllerAccessibility iconManager:didCloseFolder:]
+ -[SBHomeScreenControllerAccessibility iconManager:didOpenFolder:]
+ -[SBHomeScreenControllerAccessibility iconManager:willCloseFolder:]
+ -[SBHomeScreenControllerAccessibility iconManager:willOpenFolder:]
+ -[SBHomeScreenWindowAccessibility _accessibilityIsMainAppSwitcherCoveringHomeScreen]
+ -[SBHomeScreenWindowAccessibility _axIsBehindOpenFolderHoldingKeyboardFocus]
+ -[SBKeyboardFocusCoordinatorAccessibility _accessibilityDeferringGraphFocusLockForScene:fromWindowScene:]
+ -[SBKeyboardFocusCoordinatorAccessibility _axDeferringGraphFocusLockForScene:fromWindowScene:]
+ -[SBNSObjectDisplayContentAccessibility _accessibilityIsDisplayContentActive]
+ -[SBPosterEditingTransientOverlayViewControllerAccessibility _axIsVisible]
+ -[SBPosterEditingTransientOverlayViewControllerAccessibility _axKeyboardFocusDeferral]
+ -[SBPosterEditingTransientOverlayViewControllerAccessibility _axLockKeyboardFocusToEditingSceneWithRemainingAttempts:]
+ -[SBPosterEditingTransientOverlayViewControllerAccessibility _axReleaseKeyboardFocusDeferral]
+ -[SBPosterEditingTransientOverlayViewControllerAccessibility _axSetIsVisible:]
+ -[SBPosterEditingTransientOverlayViewControllerAccessibility _axSetKeyboardFocusDeferral:]
+ -[SBPosterEditingTransientOverlayViewControllerAccessibility viewDidAppear:]
+ -[SBPosterEditingTransientOverlayViewControllerAccessibility viewDidDisappear:]
+ -[SBPosterEditingTransientOverlayViewControllerAccessibility viewWillDisappear:]
+ -[SBSplitViewHandleNubViewAccessibility _axActionForBundleID:appName:formatKey:fallbackKey:gesture:]
+ -[SBSplitViewHandleNubViewAccessibility _axAppNameFromLayout:]
+ -[SBSplitViewHandleNubViewAccessibility _axAppsRegionModel]
+ -[SBSplitViewHandleNubViewAccessibility _axBundleIdentifierFromLayout:]
+ -[SBSplitViewHandleNubViewAccessibility _axHasTwoAppSplit]
+ -[SBSplitViewHandleNubViewAccessibility _axIsStronglyPaired]
+ -[SBSplitViewHandleNubViewAccessibility accessibilityCustomActions]
+ -[SBSplitViewHandleNubViewAccessibility accessibilityFrame]
+ -[SBSplitViewHandleNubViewAccessibility accessibilityLabel]
+ -[SBSplitViewHandleNubViewAccessibility accessibilityValue]
+ -[SBSplitViewHandleNubViewAccessibility isAccessibilityElement]
+ -[SBStatusBarWindowAccessibility _accessibilityHitTest:withEvent:]
+ -[SBStatusBarWindowAccessibility _axShouldDeferToActiveDisplayStatusBar]
+ -[SBStatusBarWindowAccessibility _axStatusBarWrapper]
+ -[SBStatusBarWindowAccessibility _axStatusBar]
+ -[SBStatusBarWindowAccessibility _isStatusBarWindow]
+ -[SpeakScreenGestureRecognizer gestureRecognizerShouldBegin:]
+ -[SpeakScreenGestureRecognizer initWithTarget:action:]
+ -[SpeakScreenGestureRecognizer reset]
+ -[SpeakScreenGestureRecognizer touchesBegan:withEvent:]
+ -[SpeakScreenUnintendedInteractionObserver touchBeganAtTimestampOverlapsSuppression:]
+ -[SpeakScreenUnintendedInteractionObserver unintendedInteractionSuppressionCoordinatorDidEnableInteractions:]
+ -[SpeakScreenUnintendedInteractionObserver unintendedInteractionSuppressionCoordinatorWillDisableInteractions:]
+ -[SpringBoardAccessibility _axActivateActiveInterfaceOrientationObserver]
+ -[SpringBoardAccessibility _axHandleActiveInterfaceOrientationState:]
+ -[SpringBoardAccessibility _axIsContentTransferSwap]
+ -[SpringBoardAccessibility _axSBDisplayContentModeCoordinator]
+ -[SpringBoardAccessibility _axTeardownActiveInterfaceOrientationObserver]
+ -[SpringBoardAccessibility displayContentModeCoordinator:handleDisplayContentModeTransition:]
+ -[SpringBoardAccessibility displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:]
+ GCC_except_table1059
+ GCC_except_table1061
+ GCC_except_table107
+ GCC_except_table1153
+ GCC_except_table1224
+ GCC_except_table123
+ GCC_except_table1244
+ GCC_except_table1251
+ GCC_except_table1255
+ GCC_except_table1259
+ GCC_except_table1262
+ GCC_except_table1267
+ GCC_except_table1415
+ GCC_except_table1425
+ GCC_except_table1432
+ GCC_except_table1436
+ GCC_except_table1473
+ GCC_except_table1477
+ GCC_except_table1482
+ GCC_except_table1485
+ GCC_except_table1504
+ GCC_except_table1510
+ GCC_except_table1512
+ GCC_except_table1516
+ GCC_except_table1524
+ GCC_except_table1530
+ GCC_except_table1541
+ GCC_except_table1543
+ GCC_except_table1613
+ GCC_except_table1620
+ GCC_except_table1621
+ GCC_except_table168
+ GCC_except_table1688
+ GCC_except_table1742
+ GCC_except_table224
+ GCC_except_table245
+ GCC_except_table275
+ GCC_except_table279
+ GCC_except_table305
+ GCC_except_table331
+ GCC_except_table336
+ GCC_except_table339
+ GCC_except_table401
+ GCC_except_table413
+ GCC_except_table456
+ GCC_except_table50
+ GCC_except_table562
+ GCC_except_table599
+ GCC_except_table618
+ GCC_except_table645
+ GCC_except_table651
+ GCC_except_table652
+ GCC_except_table654
+ GCC_except_table75
+ GCC_except_table759
+ GCC_except_table765
+ GCC_except_table766
+ GCC_except_table768
+ GCC_except_table770
+ GCC_except_table784
+ GCC_except_table792
+ GCC_except_table795
+ GCC_except_table796
+ GCC_except_table801
+ GCC_except_table803
+ GCC_except_table824
+ GCC_except_table826
+ GCC_except_table844
+ GCC_except_table866
+ GCC_except_table873
+ GCC_except_table89
+ GCC_except_table939
+ GCC_except_table95
+ _AXActiveSBBacklightController
+ _AXDeviceIsViridian
+ _AXDeviceSupportsArrangementMultitasking
+ _AXSBAnnounceLockScreenCoaching
+ _AXStringForDisplayContentMode
+ _AXStringForSurfaceType
+ _AX_SBIconLocationFloatingDockUtilities_block_invoke.sLastText
+ _AX_SBIconLocationFloatingDockUtilities_block_invoke.sLastTime
+ _OBJC_CLASS_$_AXSBFolderFocusState
+ _OBJC_CLASS_$_FBSActiveInterfaceOrientationObserver
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_SBHomeScreenControllerAccessibility
+ _OBJC_CLASS_$_SBNSObjectDisplayContentAccessibility
+ _OBJC_CLASS_$_SBPosterEditingTransientOverlayViewControllerAccessibility
+ _OBJC_CLASS_$_SBSplitViewHandleNubViewAccessibility
+ _OBJC_CLASS_$_SpeakScreenUnintendedInteractionObserver
+ _OBJC_CLASS_$_UIFocusUpdateContext
+ _OBJC_CLASS_$_UIImage
+ _OBJC_CLASS_$___SBHomeScreenControllerAccessibility_super
+ _OBJC_CLASS_$___SBNSObjectDisplayContentAccessibility_super
+ _OBJC_CLASS_$___SBPosterEditingTransientOverlayViewControllerAccessibility_super
+ _OBJC_CLASS_$___SBSplitViewHandleNubViewAccessibility_super
+ _OBJC_IVAR_$_AXSBFolderFocusState._contributesHint
+ _OBJC_IVAR_$_AXSBFolderFocusState._focusedItemBeforeOpening
+ _OBJC_IVAR_$_AXSBFolderFocusState._keyWindowBeforeOpening
+ _OBJC_IVAR_$_AXSBFolderFocusState._openingFolder
+ _OBJC_IVAR_$_AXSBFolderFocusState._openingToken
+ _OBJC_IVAR_$_AXSBFolderFocusState._tookKeyboardFocus
+ _OBJC_IVAR_$_SpeakScreenGestureRecognizer._firstTouchTimestamp
+ _OBJC_IVAR_$_SpeakScreenUnintendedInteractionObserver._lastSuppressionEndTimestamp
+ _OBJC_IVAR_$_SpeakScreenUnintendedInteractionObserver._suppressingInteractions
+ _OBJC_METACLASS_$_AXSBFolderFocusState
+ _OBJC_METACLASS_$_SBHomeScreenControllerAccessibility
+ _OBJC_METACLASS_$_SBNSObjectDisplayContentAccessibility
+ _OBJC_METACLASS_$_SBPosterEditingTransientOverlayViewControllerAccessibility
+ _OBJC_METACLASS_$_SBSplitViewHandleNubViewAccessibility
+ _OBJC_METACLASS_$_SpeakScreenUnintendedInteractionObserver
+ _OBJC_METACLASS_$___SBHomeScreenControllerAccessibility_super
+ _OBJC_METACLASS_$___SBNSObjectDisplayContentAccessibility_super
+ _OBJC_METACLASS_$___SBPosterEditingTransientOverlayViewControllerAccessibility_super
+ _OBJC_METACLASS_$___SBSplitViewHandleNubViewAccessibility_super
+ _UIFocusDidUpdateNotification
+ _UIFocusUpdateContextKey
+ __AXSBActiveInterfaceOrientationObserver
+ __AXSBDisplayTransferGeneration
+ __OBJC_$_CLASS_METHODS_SBHomeScreenControllerAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_SBNSObjectDisplayContentAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_SBPosterEditingTransientOverlayViewControllerAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_SBSplitViewHandleNubViewAccessibility(SafeCategory)
+ __OBJC_$_CLASS_METHODS_SpeakScreenUnintendedInteractionObserver
+ __OBJC_$_INSTANCE_METHODS_AXSBFolderFocusState
+ __OBJC_$_INSTANCE_METHODS_SBHomeScreenControllerAccessibility
+ __OBJC_$_INSTANCE_METHODS_SBNSObjectDisplayContentAccessibility
+ __OBJC_$_INSTANCE_METHODS_SBPosterEditingTransientOverlayViewControllerAccessibility
+ __OBJC_$_INSTANCE_METHODS_SBSplitViewHandleNubViewAccessibility
+ __OBJC_$_INSTANCE_METHODS_SpeakScreenUnintendedInteractionObserver
+ __OBJC_$_INSTANCE_VARIABLES_AXSBFolderFocusState
+ __OBJC_$_INSTANCE_VARIABLES_SpeakScreenGestureRecognizer
+ __OBJC_$_INSTANCE_VARIABLES_SpeakScreenUnintendedInteractionObserver
+ __OBJC_$_PROP_LIST_AXSBFolderFocusState
+ __OBJC_$_PROP_LIST_SpeakScreenGestureRecognizer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UIGestureRecognizerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UIGestureRecognizerDelegate
+ __OBJC_$_PROTOCOL_REFS_UIGestureRecognizerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SpeakScreenGestureRecognizer
+ __OBJC_CLASS_RO_$_AXSBFolderFocusState
+ __OBJC_CLASS_RO_$_SBHomeScreenControllerAccessibility
+ __OBJC_CLASS_RO_$_SBNSObjectDisplayContentAccessibility
+ __OBJC_CLASS_RO_$_SBPosterEditingTransientOverlayViewControllerAccessibility
+ __OBJC_CLASS_RO_$_SBSplitViewHandleNubViewAccessibility
+ __OBJC_CLASS_RO_$_SpeakScreenUnintendedInteractionObserver
+ __OBJC_CLASS_RO_$___SBHomeScreenControllerAccessibility_super
+ __OBJC_CLASS_RO_$___SBNSObjectDisplayContentAccessibility_super
+ __OBJC_CLASS_RO_$___SBPosterEditingTransientOverlayViewControllerAccessibility_super
+ __OBJC_CLASS_RO_$___SBSplitViewHandleNubViewAccessibility_super
+ __OBJC_LABEL_PROTOCOL_$_UIGestureRecognizerDelegate
+ __OBJC_METACLASS_RO_$_AXSBFolderFocusState
+ __OBJC_METACLASS_RO_$_SBHomeScreenControllerAccessibility
+ __OBJC_METACLASS_RO_$_SBNSObjectDisplayContentAccessibility
+ __OBJC_METACLASS_RO_$_SBPosterEditingTransientOverlayViewControllerAccessibility
+ __OBJC_METACLASS_RO_$_SBSplitViewHandleNubViewAccessibility
+ __OBJC_METACLASS_RO_$_SpeakScreenUnintendedInteractionObserver
+ __OBJC_METACLASS_RO_$___SBHomeScreenControllerAccessibility_super
+ __OBJC_METACLASS_RO_$___SBNSObjectDisplayContentAccessibility_super
+ __OBJC_METACLASS_RO_$___SBPosterEditingTransientOverlayViewControllerAccessibility_super
+ __OBJC_METACLASS_RO_$___SBSplitViewHandleNubViewAccessibility_super
+ __OBJC_PROTOCOL_$_UIGestureRecognizerDelegate
+ ___100-[SBSplitViewHandleNubViewAccessibility _axActionForBundleID:appName:formatKey:fallbackKey:gesture:]_block_invoke
+ ___103-[SBDeviceApplicationSceneClassicAccessoryViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
+ ___118-[SBPosterEditingTransientOverlayViewControllerAccessibility _axLockKeyboardFocusToEditingSceneWithRemainingAttempts:]_block_invoke
+ ___151-[SpringBoardAccessibility displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:]_block_invoke
+ ___151-[SpringBoardAccessibility displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:]_block_invoke_2
+ ___48-[SpringBoardAccessibility accessibilityDisable]_block_invoke
+ ___58+[SpeakScreenUnintendedInteractionObserver sharedObserver]_block_invoke
+ ___58+[SpeakScreenUnintendedInteractionObserver sharedObserver]_block_invoke_2
+ ___61-[SpringBoardAccessibility _accessibilityPerformOneTimeSetup]_block_invoke_3
+ ___66-[SBHomeScreenControllerAccessibility iconManager:willOpenFolder:]_block_invoke
+ ___67-[SBSplitViewHandleNubViewAccessibility accessibilityCustomActions]_block_invoke
+ ___67-[SBSplitViewHandleNubViewAccessibility accessibilityCustomActions]_block_invoke_2
+ ___67-[SBSplitViewHandleNubViewAccessibility accessibilityCustomActions]_block_invoke_3
+ ___67-[SBSplitViewHandleNubViewAccessibility accessibilityCustomActions]_block_invoke_4
+ ___69-[SBHomeScreenControllerAccessibility _axRestoreKeyboardFocusToView:]_block_invoke
+ ___69-[SBHomeScreenControllerAccessibility _axRestoreKeyboardFocusToView:]_block_invoke_2
+ ___69-[SBHomeScreenControllerAccessibility _axRestoreKeyboardFocusToView:]_block_invoke_3
+ ___73-[SpringBoardAccessibility _axActivateActiveInterfaceOrientationObserver]_block_invoke
+ ___73-[SpringBoardAccessibility _axActivateActiveInterfaceOrientationObserver]_block_invoke_2
+ ___77-[SBFluidSwitcherItemContainerAccessibility _accessibilityArrangementActions]_block_invoke
+ ___77-[SBFluidSwitcherItemContainerAccessibility _accessibilityArrangementActions]_block_invoke_2
+ ___77-[SBNSObjectDisplayContentAccessibility _accessibilityIsDisplayContentActive]_block_invoke
+ ___93-[SpringBoardAccessibility displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke
+ ___93-[SpringBoardAccessibility displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_2
+ ___93-[SpringBoardAccessibility displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_3
+ ___93-[SpringBoardAccessibility displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_4
+ ___93-[SpringBoardAccessibility displayContentModeCoordinator:handleDisplayContentModeTransition:]_block_invoke_5
+ ___94-[SBKeyboardFocusCoordinatorAccessibility _axDeferringGraphFocusLockForScene:fromWindowScene:]_block_invoke
+ ___94-[SBKeyboardFocusCoordinatorAccessibility _axDeferringGraphFocusLockForScene:fromWindowScene:]_block_invoke_2
+ ___AXSBAnnounceLockScreenCoaching_block_invoke
+ ___SBFluidSwitcherViewControllerAccessibility___axPendingScrollAppLayout
+ ___SBPosterEditingTransientOverlayViewControllerAccessibility___axIsVisible
+ ___SBPosterEditingTransientOverlayViewControllerAccessibility___axKeyboardFocusDeferral
+ ____AXSBSetDisplayContentModeTransitionInProgress_block_invoke
+ ___block_descriptor_32_e11_v24?0816l
+ ___block_descriptor_40_e37_B16?0"UIAccessibilityCustomAction"8l
+ ___block_descriptor_40_e8_32w_e50_v16?0"FBSActiveInterfaceOrientationStateUpdate"8lw32l8
+ ___block_descriptor_48_e8_32s40s_e37_B16?0"UIAccessibilityCustomAction"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e37_B16?0"UIAccessibilityCustomAction"8ls32l8
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_49_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e24_v16?0"NSNotification"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e11_v16?0B8B12ls32l8s40l8s56l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ __handleAuthenticationFeedback:.sLastFailureFeedbackTime
+ _dispatch_after
+ _dispatch_time
+ _kAXPageScrollShouldSpeakElement
+ _objc_retain_x10
+ _objc_retain_x27
+ _sharedObserver.SharedObserver
+ _sharedObserver.onceToken
- GCC_except_table105
- GCC_except_table1123
- GCC_except_table1143
- GCC_except_table1150
- GCC_except_table1154
- GCC_except_table1158
- GCC_except_table1161
- GCC_except_table1165
- GCC_except_table121
- GCC_except_table1321
- GCC_except_table1328
- GCC_except_table1332
- GCC_except_table1359
- GCC_except_table1363
- GCC_except_table1368
- GCC_except_table1371
- GCC_except_table1390
- GCC_except_table1396
- GCC_except_table1398
- GCC_except_table1402
- GCC_except_table1407
- GCC_except_table1413
- GCC_except_table1424
- GCC_except_table1426
- GCC_except_table1550
- GCC_except_table1604
- GCC_except_table210
- GCC_except_table231
- GCC_except_table259
- GCC_except_table263
- GCC_except_table289
- GCC_except_table315
- GCC_except_table320
- GCC_except_table323
- GCC_except_table385
- GCC_except_table397
- GCC_except_table440
- GCC_except_table48
- GCC_except_table546
- GCC_except_table581
- GCC_except_table608
- GCC_except_table614
- GCC_except_table615
- GCC_except_table617
- GCC_except_table717
- GCC_except_table723
- GCC_except_table724
- GCC_except_table726
- GCC_except_table728
- GCC_except_table73
- GCC_except_table742
- GCC_except_table750
- GCC_except_table751
- GCC_except_table756
- GCC_except_table758
- GCC_except_table779
- GCC_except_table781
- GCC_except_table799
- GCC_except_table821
- GCC_except_table828
- GCC_except_table87
- GCC_except_table93
- GCC_except_table971
- GCC_except_table973
- ___78-[SBKeyboardFocusCoordinatorAccessibility _axDeferringGraphFocusLockForScene:]_block_invoke
- ___78-[SBKeyboardFocusCoordinatorAccessibility _axDeferringGraphFocusLockForScene:]_block_invoke_2
- ___block_descriptor_48_e8_32s40bs_e11_v16?0B8B12ls40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
CStrings:
+ ".auxiliaryContent"
+ ".cover"
+ ".default"
+ ".disabled"
+ ".inner"
+ ".invalid"
+ ".primaryContent"
+ ".surface3"
+ ".unknown"
+ "AXSBFolderFocusState"
+ "AXSBFolderKeyboardFocusHolderCount"
+ "AXSBFolderMayHoldKeyboardFocus"
+ "Could not route keyboard focus to the poster editing scene. scene: %@, windowScene: %@"
+ "Error"
+ "FKA: folder closed, returning keyboard focus to %{public}@"
+ "FKA: keeping keyboard focus in the open folder's window"
+ "FKA: moving keyboard focus into opened folder %{public}@ (folder window key: %{BOOL}d)"
+ "FKA: opened folder is not hosted in the folder window, leaving keyboard focus alone"
+ "FKA: restoring keyboard focus to the item focused before the folder opened"
+ "Holding device orientation across all panels (requested displayID %u)"
+ "Holding device orientation for displayID %u (window scene %{public}@)"
+ "Ignoring Speak Screen gesture: its touches began during or just after hinge motion"
+ "Not posting screen change for cover sheet presented=%{BOOL}d on inactive display"
+ "PRUISModalRemoteViewController"
+ "Posting silent screen on: display content mode transition woke a panel while awake"
+ "SBAppsRegionModel"
+ "SBDisplayContentModeCoordinator"
+ "SBHomeScreenControllerAccessibility"
+ "SBNSObjectDisplayContentAccessibility"
+ "SBPosterEditingTransientOverlayViewController"
+ "SBPosterEditingTransientOverlayViewControllerAccessibility"
+ "SBSplitViewHandleNubView"
+ "SBUIPoseidonIconViewAccessibility"
+ "SBUnintendedInteractionSuppressionCoordinator"
+ "SBWindowingSwitcherPersonality"
+ "Speak Screen gesture began"
+ "_axKeyboardFocusCoordinator"
+ "_classicAppPhoneOnPadPrefersLandscape"
+ "_isInButterflyStrongPairConfiguration"
+ "_isInSplitPIP"
+ "_remoteViewController"
+ "_rotationButton"
+ "_sbWindowScene"
+ "_sceneIdentifier"
+ "_updateBatteryContent"
+ "_updateHomeScreenVisibleKeyboardFocusDeferringRule"
+ "activated active interface orientation observer"
+ "addObserver:"
+ "appsRegionModel"
+ "arrangement.move.left"
+ "arrangement.move.right"
+ "batteryPercentage"
+ "broadcasting active interface orientation %ld (hardwareIdentifier=%{public}@)"
+ "charging"
+ "classic.rotate.to.landscape.button"
+ "classic.rotate.to.portrait.button"
+ "content transfer: %{public}@ -> %{public}@, announce=%{BOOL}d (voiceOver=%{BOOL}d contentTransfer=%{BOOL}d)"
+ "content transfer: announcing move to %{public}@"
+ "continuousExposeIdentifier"
+ "currentContext"
+ "currentLeftAppLayout"
+ "currentRightAppLayout"
+ "currentTransitionContext"
+ "display.transfer.to.cover"
+ "display.transfer.to.inner"
+ "displayConfiguration"
+ "displayContentModeCoordinator"
+ "displayContentModeForWindowScene"
+ "folderWindow"
+ "hardwareIdentifier"
+ "hasOpenFolder"
+ "homeScreenWindow"
+ "iconManager:didCloseFolder:"
+ "iconManager:didOpenFolder:"
+ "iconManager:willCloseFolder:"
+ "iconManager:willOpenFolder:"
+ "interactive"
+ "isDisplayedWithLimitedSize"
+ "isFullScreen"
+ "isHomeScreenVisible"
+ "isInScreenOffMode"
+ "isModeSwapTransition"
+ "mainDisplay"
+ "nubContainerView"
+ "openedFolderController"
+ "primaryWindowScene"
+ "rectangle.lefthalf.inset.fill"
+ "rectangle.righthalf.inset.fill"
+ "sbWindowScene"
+ "sbui_systemArbitratedInterfaceOrientation"
+ "scene"
+ "screen"
+ "screen.displayIdentity"
+ "splitview.handle.dismiss.format"
+ "splitview.handle.dismiss.left"
+ "splitview.handle.dismiss.right"
+ "splitview.handle.fullscreen.format"
+ "splitview.handle.fullscreen.left"
+ "splitview.handle.fullscreen.right"
+ "splitview.handle.label"
+ "splitview.handle.pin"
+ "splitview.handle.pinned.value"
+ "splitview.handle.swap"
+ "splitview.handle.switch.left"
+ "splitview.handle.switch.right"
+ "splitview.handle.unpin"
+ "splitview.handle.unpinned.value"
+ "surfaceType"
+ "trailingBatteryLabel"
+ "unintendedInteractionSuppressionCoordinator"
+ "v16@?0@\"FBSActiveInterfaceOrientationStateUpdate\"8"
+ "v24@?0@8@16"
```
