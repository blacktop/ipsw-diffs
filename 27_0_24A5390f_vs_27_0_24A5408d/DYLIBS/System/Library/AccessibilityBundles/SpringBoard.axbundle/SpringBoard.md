## SpringBoard

> `/System/Library/AccessibilityBundles/SpringBoard.axbundle/SpringBoard`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`

```diff

-3045.0.0.0.0
-  __TEXT.__text: 0x399c4
-  __TEXT.__objc_methlist: 0x4d94
+3048.0.0.0.0
+  __TEXT.__text: 0x38610
+  __TEXT.__objc_methlist: 0x4c34
   __TEXT.__dlopen_cstrs: 0x98
-  __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0xa6c
-  __TEXT.__cstring: 0xa83c
+  __TEXT.__const: 0xd0
+  __TEXT.__gcc_except_tab: 0xa60
+  __TEXT.__cstring: 0xa401
   __TEXT.__oslogstring: 0x72a
-  __TEXT.__unwind_info: 0x1328
+  __TEXT.__unwind_info: 0x12f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xdf0
-  __DATA_CONST.__objc_classlist: 0x9a0
+  __DATA_CONST.__objc_classlist: 0x960
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25d0
+  __DATA_CONST.__objc_selrefs: 0x2568
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x3e8
+  __DATA_CONST.__objc_superrefs: 0x3d0
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x5d8
-  __AUTH_CONST.__const: 0x7d0
-  __AUTH_CONST.__cfstring: 0xbde0
-  __AUTH_CONST.__objc_const: 0xb6f0
+  __DATA_CONST.__got: 0x5c0
+  __AUTH_CONST.__const: 0x770
+  __AUTH_CONST.__cfstring: 0xb940
+  __AUTH_CONST.__objc_const: 0xb270
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xc30
+  __AUTH.__objc_data: 0xcd0
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x248
   __DATA.__common: 0x11
-  __DATA.__bss: 0xe0
-  __DATA_DIRTY.__objc_data: 0x5410
+  __DATA.__bss: 0xd0
+  __DATA_DIRTY.__objc_data: 0x50f0
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1615
-  Symbols:   4763
-  CStrings:  1674
+  Functions: 1589
+  Symbols:   4684
+  CStrings:  1632
 
Symbols:
+ +[SBChargingControllerAccessibility _accessibilityPerformValidations:]
+ +[SBChargingControllerAccessibility(SafeCategory) safeCategoryBaseClass]
+ +[SBChargingControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
+ -[SBAppLayoutAccessibility initWithItems:centerItem:centerConfiguration:environment:hidden:preferredDisplayOrdinal:]
+ -[SBChargingControllerAccessibility updateBatteryState:]
+ -[SBFloatingDockWindowAccessibility _axIsPresentingLibraryOrFolder]
+ -[SBFluidSwitcherViewControllerAccessibility _axPostScreenChangeToFocusAppLayout:attempt:]
+ -[SBMainScreenActiveInterfaceOrientationWindowAccessibility _axIsPresentingLibraryOrFolder]
+ -[SBMenuBarManagerAccessibility _setMenuBarVisible:animated:userInitiated:clearStatusBarAssertionsForDismissal:]
+ -[SBMenuBarViewControllerAccessibility addWindowControlsAlongsideAnimations:completion:]
+ -[SBRecordingIndicatorViewControllerAccessibility initForLocation:windowScene:indicatorDisplayPowerManaging:minimumOnTimeCoordinator:]
+ -[SBSwitcherShelfViewControllerAccessibility initWithShelf:dataSource:delegate:applicationController:]
+ -[SBWallpaperControllerAccessibility initWithWindowScene:variant:wallpaperConfigurationManager:cachingIdentifier:]
+ -[SpringBoardAccessibility takeScreenshotWithPresentationMode:]
+ GCC_except_table103
+ GCC_except_table1114
+ GCC_except_table1134
+ GCC_except_table1141
+ GCC_except_table1145
+ GCC_except_table1148
+ GCC_except_table119
+ GCC_except_table1300
+ GCC_except_table1326
+ GCC_except_table1335
+ GCC_except_table1338
+ GCC_except_table1363
+ GCC_except_table1365
+ GCC_except_table1373
+ GCC_except_table1379
+ GCC_except_table1390
+ GCC_except_table1515
+ GCC_except_table1569
+ GCC_except_table208
+ GCC_except_table229
+ GCC_except_table257
+ GCC_except_table261
+ GCC_except_table287
+ GCC_except_table313
+ GCC_except_table318
+ GCC_except_table321
+ GCC_except_table382
+ GCC_except_table394
+ GCC_except_table437
+ GCC_except_table543
+ GCC_except_table578
+ GCC_except_table605
+ GCC_except_table611
+ GCC_except_table614
+ GCC_except_table71
+ GCC_except_table714
+ GCC_except_table720
+ GCC_except_table721
+ GCC_except_table738
+ GCC_except_table745
+ GCC_except_table746
+ GCC_except_table750
+ GCC_except_table773
+ GCC_except_table791
+ GCC_except_table809
+ GCC_except_table85
+ GCC_except_table91
+ _AXSBActiveDisplayWindowScene
+ _AXSBChargingController
+ _OBJC_CLASS_$_SBChargingControllerAccessibility
+ _OBJC_CLASS_$___SBChargingControllerAccessibility_super
+ _OBJC_METACLASS_$_SBChargingControllerAccessibility
+ _OBJC_METACLASS_$___SBChargingControllerAccessibility_super
+ __OBJC_$_CLASS_METHODS_SBChargingControllerAccessibility(SafeCategory)
+ __OBJC_$_INSTANCE_METHODS_SBChargingControllerAccessibility
+ __OBJC_CLASS_RO_$_SBChargingControllerAccessibility
+ __OBJC_CLASS_RO_$___SBChargingControllerAccessibility_super
+ __OBJC_METACLASS_RO_$_SBChargingControllerAccessibility
+ __OBJC_METACLASS_RO_$___SBChargingControllerAccessibility_super
+ ___112-[SBMenuBarManagerAccessibility _setMenuBarVisible:animated:userInitiated:clearStatusBarAssertionsForDismissal:]_block_invoke
+ ___112-[SBMenuBarManagerAccessibility _setMenuBarVisible:animated:userInitiated:clearStatusBarAssertionsForDismissal:]_block_invoke_2
+ ___62-[SpringBoardAccessibility _accessibilityNotificationSummary:]_block_invoke
+ ___63-[SpringBoardAccessibility takeScreenshotWithPresentationMode:]_block_invoke
+ ___63-[SpringBoardAccessibility takeScreenshotWithPresentationMode:]_block_invoke_2
+ ___90-[SBFluidSwitcherViewControllerAccessibility _axPostScreenChangeToFocusAppLayout:attempt:]_block_invoke
+ ___block_descriptor_56_e8_32s40w_e5_v8?0lw40l8s32l8
+ _objc_msgSend$_axIsPresentingLibraryOrFolder
+ _objc_msgSend$_axPostScreenChangeToFocusAppLayout:attempt:
+ _objc_msgSend$allWindowsIncludingInternalWindows:onlyVisibleWindows:
+ _objc_msgSend$alpha
- +[SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility _accessibilityPerformValidations:]
- +[SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility(SafeCategory) safeCategoryBaseClass]
- +[SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[SBMoveGestureFloatingSwitcherModifierAccessibility _accessibilityPerformValidations:]
- +[SBMoveGestureFloatingSwitcherModifierAccessibility(SafeCategory) safeCategoryBaseClass]
- +[SBMoveGestureFloatingSwitcherModifierAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[SBRootSceneWindowAccessibility _accessibilityPerformValidations:]
- +[SBRootSceneWindowAccessibility(SafeCategory) safeCategoryBaseClass]
- +[SBRootSceneWindowAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[SBScreenshotManagerAccessibility(SafeCategory) safeCategoryBaseClass]
- +[SBScreenshotManagerAccessibility(SafeCategory) safeCategoryTargetClassName]
- +[SBUIControllerAccessibility _accessibilityPerformValidations:]
- +[SBUIControllerAccessibility(SafeCategory) safeCategoryBaseClass]
- +[SBUIControllerAccessibility(SafeCategory) safeCategoryTargetClassName]
- -[SBAppLayoutAccessibility initWithItems:centerItem:floatingItem:configuration:centerConfiguration:environment:hidden:preferredDisplayOrdinal:]
- -[SBMainSwitcherWindowAccessibility _axSideAppDivider]
- -[SBMenuBarManagerAccessibility _setMenuBarVisible:animated:userInitiated:]
- -[SBMenuBarViewControllerAccessibility _createWindowControlsPlaceholderViewForViewController:]
- -[SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility _axDestinationAppName]
- -[SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility handleTransitionRequestForGestureComplete:fromGestureManager:]
- -[SBMoveGestureFloatingSwitcherModifierAccessibility _axFloatingConfigurationForGestureEvent:withZeroVelocity:]
- -[SBMoveGestureFloatingSwitcherModifierAccessibility _axGetCurrentFloatingConfiguration]
- -[SBMoveGestureFloatingSwitcherModifierAccessibility _axGetFinishedFloatingConfiguration]
- -[SBMoveGestureFloatingSwitcherModifierAccessibility _axInitialFloatingConfiguration]
- -[SBMoveGestureFloatingSwitcherModifierAccessibility _axSetCurrentFloatingConfiguration:]
- -[SBMoveGestureFloatingSwitcherModifierAccessibility _axSetFinishedFloatingConfiguration:]
- -[SBMoveGestureFloatingSwitcherModifierAccessibility _updateForGestureDidBeginWithEvent:]
- -[SBMoveGestureFloatingSwitcherModifierAccessibility _updateForGestureDidChangeWithEvent:]
- -[SBMoveGestureFloatingSwitcherModifierAccessibility _updateForGestureDidEndWithEvent:]
- -[SBRecordingIndicatorViewControllerAccessibility initForLocation:windowScene:minimumOnTimeCoordinator:]
- -[SBRootSceneWindowAccessibility _accessibilityLoadAccessibilityInformation]
- -[SBSwitcherShelfViewControllerAccessibility initWithShelf:dataSource:delegate:]
- -[SBUIControllerAccessibility _accessibilityIsAppSwitcherVisible]
- -[SBUIControllerAccessibility updateBatteryState:]
- -[SBWallpaperControllerAccessibility initWithWindowScene:orientation:variant:wallpaperConfigurationManager:cachingIdentifier:]
- -[SpringBoardAccessibility _accessibilitySideAppDividerElement]
- -[SpringBoardAccessibility _takeScreenshotWithPresentationMode:]
- GCC_except_table105
- GCC_except_table1139
- GCC_except_table1159
- GCC_except_table1166
- GCC_except_table1170
- GCC_except_table1173
- GCC_except_table121
- GCC_except_table1362
- GCC_except_table1367
- GCC_except_table1386
- GCC_except_table1394
- GCC_except_table1402
- GCC_except_table1408
- GCC_except_table1420
- GCC_except_table1422
- GCC_except_table1545
- GCC_except_table1599
- GCC_except_table211
- GCC_except_table232
- GCC_except_table259
- GCC_except_table263
- GCC_except_table289
- GCC_except_table314
- GCC_except_table319
- GCC_except_table322
- GCC_except_table383
- GCC_except_table395
- GCC_except_table438
- GCC_except_table544
- GCC_except_table579
- GCC_except_table606
- GCC_except_table613
- GCC_except_table617
- GCC_except_table716
- GCC_except_table722
- GCC_except_table727
- GCC_except_table73
- GCC_except_table740
- GCC_except_table747
- GCC_except_table748
- GCC_except_table754
- GCC_except_table777
- GCC_except_table793
- GCC_except_table87
- GCC_except_table93
- _AXImageExplorerGenerativeModelsAvailable
- _AXSBUIControllerSharedInstance
- _AXSBUIControllerSharedInstance.SharedInstance
- _AXSpringBoardGlueSBUIControllerClass
- _AXSpringBoardGlueSBUIControllerClass.class
- _OBJC_CLASS_$_AXVoiceOverServer
- _OBJC_CLASS_$_SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility
- _OBJC_CLASS_$_SBMoveGestureFloatingSwitcherModifierAccessibility
- _OBJC_CLASS_$_SBRootSceneWindowAccessibility
- _OBJC_CLASS_$_SBScreenshotManagerAccessibility
- _OBJC_CLASS_$_SBUIControllerAccessibility
- _OBJC_CLASS_$___SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility_super
- _OBJC_CLASS_$___SBMoveGestureFloatingSwitcherModifierAccessibility_super
- _OBJC_CLASS_$___SBRootSceneWindowAccessibility_super
- _OBJC_CLASS_$___SBScreenshotManagerAccessibility_super
- _OBJC_CLASS_$___SBUIControllerAccessibility_super
- _OBJC_METACLASS_$_SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility
- _OBJC_METACLASS_$_SBMoveGestureFloatingSwitcherModifierAccessibility
- _OBJC_METACLASS_$_SBRootSceneWindowAccessibility
- _OBJC_METACLASS_$_SBScreenshotManagerAccessibility
- _OBJC_METACLASS_$_SBUIControllerAccessibility
- _OBJC_METACLASS_$___SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility_super
- _OBJC_METACLASS_$___SBMoveGestureFloatingSwitcherModifierAccessibility_super
- _OBJC_METACLASS_$___SBRootSceneWindowAccessibility_super
- _OBJC_METACLASS_$___SBScreenshotManagerAccessibility_super
- _OBJC_METACLASS_$___SBUIControllerAccessibility_super
- __OBJC_$_CLASS_METHODS_SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_SBMoveGestureFloatingSwitcherModifierAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_SBRootSceneWindowAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_SBScreenshotManagerAccessibility(SafeCategory)
- __OBJC_$_CLASS_METHODS_SBUIControllerAccessibility(SafeCategory)
- __OBJC_$_INSTANCE_METHODS_SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility
- __OBJC_$_INSTANCE_METHODS_SBMoveGestureFloatingSwitcherModifierAccessibility
- __OBJC_$_INSTANCE_METHODS_SBRootSceneWindowAccessibility
- __OBJC_$_INSTANCE_METHODS_SBUIControllerAccessibility
- __OBJC_CLASS_RO_$_SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility
- __OBJC_CLASS_RO_$_SBMoveGestureFloatingSwitcherModifierAccessibility
- __OBJC_CLASS_RO_$_SBRootSceneWindowAccessibility
- __OBJC_CLASS_RO_$_SBScreenshotManagerAccessibility
- __OBJC_CLASS_RO_$_SBUIControllerAccessibility
- __OBJC_CLASS_RO_$___SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility_super
- __OBJC_CLASS_RO_$___SBMoveGestureFloatingSwitcherModifierAccessibility_super
- __OBJC_CLASS_RO_$___SBRootSceneWindowAccessibility_super
- __OBJC_CLASS_RO_$___SBScreenshotManagerAccessibility_super
- __OBJC_CLASS_RO_$___SBUIControllerAccessibility_super
- __OBJC_METACLASS_RO_$_SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility
- __OBJC_METACLASS_RO_$_SBMoveGestureFloatingSwitcherModifierAccessibility
- __OBJC_METACLASS_RO_$_SBRootSceneWindowAccessibility
- __OBJC_METACLASS_RO_$_SBScreenshotManagerAccessibility
- __OBJC_METACLASS_RO_$_SBUIControllerAccessibility
- __OBJC_METACLASS_RO_$___SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility_super
- __OBJC_METACLASS_RO_$___SBMoveGestureFloatingSwitcherModifierAccessibility_super
- __OBJC_METACLASS_RO_$___SBRootSceneWindowAccessibility_super
- __OBJC_METACLASS_RO_$___SBScreenshotManagerAccessibility_super
- __OBJC_METACLASS_RO_$___SBUIControllerAccessibility_super
- ___64-[SpringBoardAccessibility _takeScreenshotWithPresentationMode:]_block_invoke
- ___64-[SpringBoardAccessibility _takeScreenshotWithPresentationMode:]_block_invoke_2
- ___73-[SBSystemApertureViewControllerAccessibility accessibilityCustomActions]_block_invoke_3
- ___73-[SBSystemApertureViewControllerAccessibility accessibilityCustomActions]_block_invoke_4
- ___75-[SBMenuBarManagerAccessibility _setMenuBarVisible:animated:userInitiated:]_block_invoke
- ___75-[SBMenuBarManagerAccessibility _setMenuBarVisible:animated:userInitiated:]_block_invoke_2
- ___76-[SBRootSceneWindowAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke
- ___82-[SBMenuBarViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2
- ___SBMoveGestureFloatingSwitcherModifierAccessibility___axGetCurrentFloatingConfiguration
- ___SBMoveGestureFloatingSwitcherModifierAccessibility___axGetFinishedFloatingConfiguration
- ___assert_rtn
- ___block_descriptor_40_e8_32w_e14_"NSArray"8?0lw32l8
- _kVOTEventCommandActivateScreenExplorer
- _kVOTEventCommandAskAboutScreen
- _objc_msgSend$_accessibilitySideAppDividerElement
- _objc_msgSend$_axDestinationAppName
- _objc_msgSend$_axFloatingConfigurationForGestureEvent:withZeroVelocity:
- _objc_msgSend$_axGetCurrentFloatingConfiguration
- _objc_msgSend$_axInitialFloatingConfiguration
- _objc_msgSend$_axSetCurrentFloatingConfiguration:
- _objc_msgSend$_axSetFinishedFloatingConfiguration:
- _objc_msgSend$_axSideAppDivider
- _objc_msgSend$imageExplorerAskAboutScreenDynamicIslandActionEnabled
- _objc_msgSend$imageExplorerScreenExplorerDynamicIslandActionEnabled
- _objc_msgSend$setAccessibilityElementsBlock:
- _objc_msgSend$triggerEventCommand:
CStrings:
+ "SBAssistantSceneController"
+ "SBChargingController"
+ "SBChargingControllerAccessibility"
+ "SBSRemoteAlertDefinition"
+ "SBVOT: skipping screen curtain apply for enabled=%d because system is sleeping; will not be resynced on wake"
+ "SBVOT: tearing down VoiceOverTouch connection, force-disabling screen curtain (was %d)"
+ "SBVOT: tearing down connection during registration (votPort=%d, appReadyToBeProbed=%d)"
+ "UIViewController<CCUIMainViewControllerProtocol><CCUIMainViewControllerPPTSupporting>"
+ "_activityViewController"
+ "_adjustFocusContentOffset:toShowFocusItem:"
+ "_focusedScene"
+ "_sceneHandle"
+ "_setMenuBarVisible:animated:userInitiated:clearStatusBarAssertionsForDismissal:"
+ "_transientOverlay"
+ "addWindowControlsAlongsideAnimations:completion:"
+ "allWindowsIncludingInternalWindows:onlyVisibleWindows:"
+ "alr_activePreflightScene"
+ "alr_preflightTargetScene"
+ "alr_requiresPreflight"
+ "assistantRootViewController"
+ "bluetoothController"
+ "chargingController"
+ "configurationIdentifier"
+ "definition"
+ "initForLocation:windowScene:indicatorDisplayPowerManaging:minimumOnTimeCoordinator:"
+ "initWithItems:centerItem:centerConfiguration:environment:hidden:preferredDisplayOrdinal:"
+ "initWithShelf:dataSource:delegate:applicationController:"
+ "initWithWindowScene:variant:wallpaperConfigurationManager:cachingIdentifier:"
+ "remoteSearchViewController"
+ "takeScreenshotWithPresentationMode:"
+ "transitionToCompactOverlayModeWithCompletion:"
- "AXSBFloatingConfigurationForMovingFloatingApplication"
- "SBAppContainerViewController"
- "SBFluidSwitcherGestureWorkspaceTransaction"
- "SBLiveTranscriptionUISceneController"
- "SBMainDisplayInterfaceOrientationAggregator"
- "SBMedusaSettings"
- "SBMoveFloatingApplicationGestureWorkspaceTransaction"
- "SBMoveFloatingApplicationGestureWorkspaceTransactionAccessibility"
- "SBMoveGestureFloatingSwitcherModifier"
- "SBMoveGestureFloatingSwitcherModifierAccessibility"
- "SBMoveGestureFloatingSwitcherModifierAccessibility.m"
- "SBRootSceneWindow"
- "SBRootSceneWindowAccessibility"
- "SBSceneManager"
- "SBScreenshotManager"
- "SBScreenshotManagerAccessibility"
- "SBSwitcherContextProviding"
- "SBSwitcherTransitionRequest"
- "SBUIController"
- "SBUIControllerAccessibility"
- "SBWorkspaceTransaction"
- "SBWorkspaceTransitionRequest"
- "UIViewController<CCUIMainViewController><CCUIMainViewControllerPPTSupporting>"
- "_adjustFocusContentOffset:toShowFocusItemWithInfo:"
- "_createWindowControlsPlaceholderViewForViewController:"
- "_inputUIScene"
- "_orientationAggregator"
- "_resizeGrabber"
- "_setMenuBarVisible:animated:userInitiated:"
- "_takeScreenshotWithPresentationMode:"
- "_updateForGestureDidBeginWithEvent:"
- "_updateForGestureDidChangeWithEvent:"
- "_updateForGestureDidEndWithEvent:"
- "_windowControlsPlaceholderView"
- "accessibilityIsAppSwitcherVisible"
- "app.pip.nib.action.moved.app.left"
- "app.pip.nib.action.moved.app.right"
- "app.pip.nib.action.moved.app.stashed.left"
- "app.pip.nib.action.moved.app.stashed.right"
- "applicationContext"
- "applicationSceneEntities"
- "ask.about.screen"
- "containerViewBounds"
- "delegate.windowControlsViewController"
- "dotsView"
- "effectiveMinCenterX < effectiveMaxCenterX"
- "explore.screen"
- "floatingConfiguration"
- "handleTransitionRequestForGestureComplete:fromGestureManager:"
- "hasOpenFolder"
- "initForLocation:windowScene:minimumOnTimeCoordinator:"
- "initWithItems:centerItem:floatingItem:configuration:centerConfiguration:environment:hidden:preferredDisplayOrdinal:"
- "initWithShelf:dataSource:delegate:"
- "initWithWindowScene:orientation:variant:wallpaperConfigurationManager:cachingIdentifier:"
- "initialFloatingConfiguration"
- "interfaceOrientationSources"
- "isMedusaCapable"
- "lift.move.app.left"
- "lift.move.app.right"
- "liveTranscriptionUISceneController"
- "medusaSettings"
- "movePanGestureNegativeVelocityThreshold"
- "movePanGesturePositiveVelocityThreshold"
- "movePanGestureThresholdPercentage"
- "negativeVelocity < 0.0f"
- "positiveVelocity > 0.0f"
- "sharedRemoteSearchViewController"
- "subviews"
- "switcherViewBounds"
- "transitionRequest"
- "translationInContainerView"
- "velocityInContainerView"
- "viewControllerClass"
```
