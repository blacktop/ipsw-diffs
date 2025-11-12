## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4557.2.2.101.0
-  __TEXT.__text: 0xa92018
-  __TEXT.__auth_stubs: 0x5590
+4557.2.5.0.0
+  __TEXT.__text: 0xa93878
+  __TEXT.__auth_stubs: 0x5580
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xb80a0
-  __TEXT.__const: 0x12f40
-  __TEXT.__oslogstring: 0x5e4c8
-  __TEXT.__cstring: 0x7d254
-  __TEXT.__gcc_except_tab: 0x1969c
+  __TEXT.__objc_methlist: 0xb8290
+  __TEXT.__const: 0x12f50
+  __TEXT.__oslogstring: 0x5e5d8
+  __TEXT.__cstring: 0x7d451
+  __TEXT.__gcc_except_tab: 0x19690
   __TEXT.__ustring: 0xcce
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__unwind_info: 0x2c5c0
+  __TEXT.__unwind_info: 0x2c660
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x2220f
-  __TEXT.__objc_methname: 0x1d1695
-  __TEXT.__objc_methtype: 0x4d132
-  __TEXT.__objc_stubs: 0xf4e00
-  __DATA_CONST.__got: 0xa2f0
-  __DATA_CONST.__const: 0x1cb98
+  __TEXT.__objc_classname: 0x22216
+  __TEXT.__objc_methname: 0x1d1799
+  __TEXT.__objc_methtype: 0x4d143
+  __TEXT.__objc_stubs: 0xf4fe0
+  __DATA_CONST.__got: 0xa2e0
+  __DATA_CONST.__const: 0x1cbe8
   __DATA_CONST.__objc_classlist: 0x5278
   __DATA_CONST.__objc_catlist: 0x368
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2928
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4af88
+  __DATA_CONST.__objc_selrefs: 0x4afd8
   __DATA_CONST.__objc_protorefs: 0xb0
-  __DATA_CONST.__objc_superrefs: 0x3fa0
+  __DATA_CONST.__objc_superrefs: 0x3fa8
   __DATA_CONST.__objc_arraydata: 0x1868
-  __AUTH_CONST.__auth_got: 0x2ae0
-  __AUTH_CONST.__const: 0x10c78
-  __AUTH_CONST.__cfstring: 0x6f1a0
-  __AUTH_CONST.__objc_const: 0x26b6f8
+  __AUTH_CONST.__auth_got: 0x2ad8
+  __AUTH_CONST.__const: 0x10cb8
+  __AUTH_CONST.__cfstring: 0x6f460
+  __AUTH_CONST.__objc_const: 0x26b7f0
   __AUTH_CONST.__objc_arrayobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0x770
   __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH.__objc_data: 0x10770
-  __DATA.__objc_ivar: 0xf484
+  __DATA.__objc_ivar: 0xf480
   __DATA.__data: 0x1f8b8
-  __DATA.__bss: 0xab0
+  __DATA.__bss: 0xac0
   __DATA.__common: 0xa40
   __DATA_DIRTY.__objc_data: 0x23140
   __DATA_DIRTY.__data: 0x180

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  UUID: 6E2A351D-2519-33A7-B1AF-5F9704146E1D
-  Functions: 70264
-  Symbols:   237698
-  CStrings:  104514
+  UUID: 628E7FC4-424F-39F3-B3B7-FC408BDD7022
+  Functions: 70313
+  Symbols:   237814
+  CStrings:  104574
 
Symbols:
+ +[SBHomeGrabberView defaultBehavior]
+ -[SBActivityManager _activityHasDifferentAlertSceneTarget:]
+ -[SBActivitySystemApertureElementObserver _removePendingAlertForItem:]
+ -[SBActivityViewController handleActivityWillDismissFromBottomSwipeGesture]
+ -[SBCaptureButtonBehaviorsResponse descriptionBuilderWithMultilinePrefix:]
+ -[SBCaptureButtonBehaviorsResponse descriptionWithMultilinePrefix:]
+ -[SBCaptureButtonBehaviorsResponse description]
+ -[SBCaptureButtonBehaviorsResponse hasNonUnknownIntents]
+ -[SBCaptureButtonBehaviorsResponse succinctDescriptionBuilder]
+ -[SBCaptureButtonBehaviorsResponse succinctDescription]
+ -[SBCaptureButtonBehaviorsResponseLog descriptionBuilderWithMultilinePrefix:]
+ -[SBCaptureButtonBehaviorsResponseLog descriptionWithMultilinePrefix:]
+ -[SBCaptureButtonBehaviorsResponseLog description]
+ -[SBCaptureButtonBehaviorsResponseLog succinctDescriptionBuilder]
+ -[SBCaptureButtonBehaviorsResponseLog succinctDescription]
+ -[SBCaptureButtonContext descriptionBuilderWithMultilinePrefix:]
+ -[SBCaptureButtonContext descriptionWithMultilinePrefix:]
+ -[SBCaptureButtonContext succinctDescriptionBuilder]
+ -[SBCaptureButtonContext succinctDescription]
+ -[SBCaptureButtonInteraction descriptionBuilderWithMultilinePrefix:]
+ -[SBCaptureButtonInteraction descriptionWithMultilinePrefix:]
+ -[SBCaptureButtonInteraction description]
+ -[SBCaptureButtonInteraction succinctDescriptionBuilder]
+ -[SBCaptureButtonInteraction succinctDescription]
+ -[SBCaptureButtonPolicy descriptionBuilderWithMultilinePrefix:]
+ -[SBCaptureButtonPolicy descriptionWithMultilinePrefix:]
+ -[SBCaptureButtonPolicy succinctDescriptionBuilder]
+ -[SBCaptureButtonPolicy succinctDescription]
+ -[SBDruidUISceneController didDisableSecureRendering:]
+ -[SBDruidUISceneController willEnableSecureRendering:]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier _performSlideOverConfigurationUpdateWithConfiguration:appLayout:layoutAttributes:]
+ -[SBFlexibleWindowingWindowDragSwitcherModifier _slideOverCenterExitRemainingTimeWithSettledDuration:]
+ -[SBFluidScrunchGestureRecognizer timeWithinRadius:]
+ -[SBFluidSwitcherPanGestureRecognizer timeWithinRadius:]
+ -[SBFluidSwitcherViewController _homeGrabberViewBehaviorForAppLayout:]
+ -[SBFluidSwitcherViewController displayItemIsAlwaysMaximized:]
+ -[SBGestureSwitcherModifierEvent timeWithinRadius:]
+ -[SBHomeGesturePanGestureRecognizer timeWithinRadius:]
+ -[SBHomeGrabberView behavior]
+ -[SBHomeGrabberView setBehavior:]
+ -[SBHomeScreenController addIconOcclusionReason:removeIconOcclusionReason:updateVisibleIcons:]
+ -[SBHomeScreenController isAppGestureActive]
+ -[SBHomeScreenController setAppGestureActive:]
+ -[SBIndirectPanGestureRecognizer timeWithinRadius:]
+ -[SBRingerPillView _updateGlyphWithTintColor]
+ -[SBSwitcherWindowManagementContext(Biome) _multitaskingMode]
+ -[SBSwitcherWindowManagementContext(Biome) biomeStageManagerMode]
+ -[SBSwitcherWindowingSettings windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:]
+ -[SBSwitcherWindowingSettings windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:]
+ -[SBSwitcherWindowingSettings windowingConfigurationForWindowScene:interfaceOrientation:floatingDockHeight:]
+ -[SBTouchHistory timeWithinRadius:]
+ -[_SBDisplayItemFreeFormGrid maxSize]
+ GCC_except_table1005
+ GCC_except_table155
+ GCC_except_table307
+ GCC_except_table384
+ GCC_except_table385
+ GCC_except_table588
+ GCC_except_table634
+ GCC_except_table669
+ GCC_except_table742
+ GCC_except_table766
+ GCC_except_table769
+ GCC_except_table810
+ GCC_except_table852
+ GCC_except_table891
+ GCC_except_table901
+ GCC_except_table947
+ GCC_except_table986
+ _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._rubberbandingRangeX
+ _OBJC_IVAR_$_SBFlexibleWindowingItemResizeGestureSwitcherModifier._rubberbandingRangeY
+ _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._centerExitingEntryPoint
+ _OBJC_IVAR_$_SBHomeGrabberView._behavior
+ _OBJC_IVAR_$_SBHomeScreenController._appGestureActive
+ _SBCaptureButtonGestureDescription
+ _SBLogCameraCaptureAppActivator
+ _SBLogCameraCaptureAppActivator.__logObj
+ _SBLogCameraCaptureAppActivator.cold.1
+ _SBLogCameraCaptureAppActivator.onceToken
+ _UIViewGlassGetLegibilitySetting
+ __OBJC_$_INSTANCE_METHODS_SBDruidUISceneController
+ __OBJC_$_INSTANCE_METHODS_SBSwitcherWindowManagementContext(Telemetry|Biome)
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.668
+ ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.670
+ ___38-[SBIconController _registerAnalytics]_block_invoke.219
+ ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1219
+ ___45-[SBExposeWindowingModifier appLayoutTapped:]_block_invoke
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.763
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.794
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.825
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.931
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.818
+ ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.935
+ ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1790
+ ___57-[SBActivitySystemApertureElementObserver _presentAlert:]_block_invoke.52
+ ___59-[SBIconController _updateUninstallingSystemAppsRestricted]_block_invoke.218
+ ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.947
+ ___63-[SBCaptureButtonPolicy descriptionBuilderWithMultilinePrefix:]_block_invoke
+ ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.245
+ ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.245.cold.1
+ ___68-[SBCaptureButtonInteraction descriptionBuilderWithMultilinePrefix:]_block_invoke
+ ___68-[SBCaptureButtonInteraction descriptionBuilderWithMultilinePrefix:]_block_invoke_2
+ ___68-[SBCaptureButtonInteraction descriptionBuilderWithMultilinePrefix:]_block_invoke_3
+ ___70-[SBActivitySystemApertureElementObserver _removePendingAlertForItem:]_block_invoke
+ ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.370
+ ___83-[SBIconController _obtainSmartStackForWidgetDiscoverabilityWithCompletionHandler:]_block_invoke.250
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1642
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1644
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1646
+ ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1650
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.652
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.674
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.689
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.693
+ ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.701
+ ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1773
+ ___SBLogCameraCaptureAppActivator_block_invoke
+ ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls32l8s48l8s40l8s56l8
+ ___block_literal_global.1074
+ ___block_literal_global.1110
+ ___block_literal_global.1162
+ ___block_literal_global.1165
+ ___block_literal_global.1170
+ ___block_literal_global.1176
+ ___block_literal_global.1207
+ ___block_literal_global.1255
+ ___block_literal_global.1469
+ ___block_literal_global.1616
+ ___block_literal_global.1620
+ ___block_literal_global.1661
+ ___block_literal_global.1663
+ ___block_literal_global.1665
+ ___block_literal_global.1667
+ ___block_literal_global.1683
+ ___block_literal_global.1799
+ ___block_literal_global.1831
+ ___block_literal_global.1847
+ ___block_literal_global.213
+ ___block_literal_global.243
+ ___block_literal_global.270
+ ___block_literal_global.433
+ ___block_literal_global.554
+ ___block_literal_global.563
+ ___block_literal_global.589
+ ___block_literal_global.595
+ ___block_literal_global.600
+ ___block_literal_global.602
+ ___block_literal_global.604
+ ___block_literal_global.606
+ ___block_literal_global.608
+ ___block_literal_global.610
+ ___block_literal_global.625
+ ___block_literal_global.645
+ ___block_literal_global.646
+ ___block_literal_global.648
+ ___block_literal_global.651
+ ___block_literal_global.673
+ ___block_literal_global.706
+ ___block_literal_global.794
+ ___block_literal_global.817
+ ___block_literal_global.819
+ ___block_literal_global.824
+ ___block_literal_global.826
+ ___block_literal_global.829
+ ___block_literal_global.831
+ ___block_literal_global.855
+ ___block_literal_global.865
+ ___block_literal_global.868
+ ___block_literal_global.901
+ ___block_literal_global.905
+ ___block_literal_global.907
+ ___block_literal_global.911
+ ___block_literal_global.913
+ ___block_literal_global.917
+ ___block_literal_global.919
+ ___block_literal_global.923
+ ___block_literal_global.925
+ ___block_literal_global.929
+ ___block_literal_global.931
+ ___block_literal_global.935
+ ___block_literal_global.937
+ ___block_literal_global.941
+ ___block_literal_global.949
+ _kSlideOverExitViaCenterCheckDuration
+ _kSlideOverExitViaCenterMinimumMovementThreshold
+ _kSlideOverSettledMaxRadius
+ _objc_msgSend$_homeGrabberViewBehaviorForAppLayout:
+ _objc_msgSend$_multitaskingMode
+ _objc_msgSend$_performSlideOverConfigurationUpdateWithConfiguration:appLayout:layoutAttributes:
+ _objc_msgSend$_removePendingAlertForItem:
+ _objc_msgSend$_slideOverCenterExitRemainingTimeWithSettledDuration:
+ _objc_msgSend$_updateGlyphWithTintColor
+ _objc_msgSend$addIconOcclusionReason:removeIconOcclusionReason:updateVisibleIcons:
+ _objc_msgSend$autoHides
+ _objc_msgSend$biomeStageManagerMode
+ _objc_msgSend$builderWithClass:
+ _objc_msgSend$displayItemIsAlwaysMaximized:
+ _objc_msgSend$handleActivityWillDismissFromBottomSwipeGesture
+ _objc_msgSend$handleEntityWillDismissFromBottomSwipeGesture
+ _objc_msgSend$hasNonUnknownIntents
+ _objc_msgSend$imageNamed:inBundle:withConfiguration:
+ _objc_msgSend$initWithStarting:multitaskingMode:
+ _objc_msgSend$initWithVariant:size:
+ _objc_msgSend$responseLogs
+ _objc_msgSend$setAppGestureActive:
+ _objc_msgSend$systemTraitsAffectingColorAppearance
+ _objc_msgSend$timeWithinRadius:
+ _objc_msgSend$windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:
+ _objc_msgSend$windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:
+ _objc_msgSend$windowingConfigurationForWindowScene:interfaceOrientation:floatingDockHeight:
- -[SBDisplayItemLayoutAttributesCalculator _appLayoutContainsOnlyResizableApps:]
- -[SBFlexibleWindowingWindowDragSwitcherModifier _slideOverCenterExitingTimerWaitingWhileStillCloseWithCenter:]
- -[SBRingerPillView materialView]
- -[SBRingerPillView setMaterialView:]
- -[SBRingerPillView setShadowView:]
- -[SBRingerPillView setStylingProvider:]
- -[SBRingerPillView shadowView]
- -[SBRingerPillView stylingProvider]
- -[SBRingerPillView traitCollectionDidChange:]
- -[SBSwitcherWindowingConfiguration requiresFullScreen]
- -[SBSwitcherWindowingConfiguration setRequiresFullScreen:]
- -[SBSwitcherWindowingSettings windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:]
- -[SBSwitcherWindowingSettings windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:]
- -[SBSwitcherWindowingSettings windowingConfigurationForWindowScene:interfaceOrientation:requiresFullScreen:floatingDockHeight:]
- GCC_except_table153
- GCC_except_table278
- GCC_except_table382
- GCC_except_table587
- GCC_except_table633
- GCC_except_table668
- GCC_except_table740
- GCC_except_table764
- GCC_except_table767
- GCC_except_table808
- GCC_except_table848
- GCC_except_table889
- GCC_except_table899
- GCC_except_table945
- GCC_except_table984
- GCC_except_table991
- _CFBundleGetBundleWithIdentifier
- _CFBundleGetFunctionPointerForName
- _MCFeatureMaximumAppsRating
- _OBJC_CLASS_$_MTShadowView
- _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._slideOverCenterSettledPosition
- _OBJC_IVAR_$_SBRingerPillView._materialView
- _OBJC_IVAR_$_SBRingerPillView._shadowView
- _OBJC_IVAR_$_SBRingerPillView._stylingProvider
- _OBJC_IVAR_$_SBSwitcherWindowingConfiguration._requiresFullScreen
- _OBJC_IVAR_$_SBSwitcherWindowingSettings._cachedWindowingConfiguration_requiresFullScreen
- __OBJC_$_INSTANCE_METHODS_SBSwitcherWindowManagementContext(Telemetry)
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke.659
- ___121-[SBSystemApertureViewController _handleContainerAndElementUpdatesFromPreferences:orderedElementViewControllers:context:]_block_invoke_2.661
- ___38-[SBIconController _registerAnalytics]_block_invoke.221
- ___44-[SpringBoard __handleHIDEvent:withUIEvent:]_block_invoke.1210
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.754
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.785
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.816
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke.922
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.809
- ___53-[SpringBoard _completeStartupAfterMainSceneConnect:]_block_invoke_2.926
- ___56-[SpringBoard _keyboardOrCaseLatchWantsToAttemptUnlock:]_block_invoke.1781
- ___57-[SBActivitySystemApertureElementObserver _presentAlert:]_block_invoke.51
- ___59-[SBIconController _updateUninstallingSystemAppsRestricted]_block_invoke.220
- ___60-[SBSystemApertureViewController _addZoomAnimationAssertion]_block_invoke.938
- ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.247
- ___64-[SBIconController _addSmartStackToTodayList:completionHandler:]_block_invoke.247.cold.1
- ___81-[SBSystemActionCoachingHUDViewController transitionToState:animated:completion:]_block_invoke.361
- ___83-[SBIconController _obtainSmartStackForWidgetDiscoverabilityWithCompletionHandler:]_block_invoke.254
- ___84-[SBActivitySystemApertureElementObserver _removeSystemApertureSceneHandleWithItem:]_block_invoke
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1633
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1635
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke.1637
- ___90-[SpringBoard remoteTransientOverlaySessionManager:performPresentationRequest:forSession:]_block_invoke_2.1641
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.649
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.671
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.686
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke.690
- ___94-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:]_block_invoke_2.698
- ___97-[SpringBoard handleDeferredUILockForInCallPresentationAnimateIfNeeded:inCallPresentationActive:]_block_invoke.1764
- ___block_literal_global.1056
- ___block_literal_global.1101
- ___block_literal_global.1153
- ___block_literal_global.1156
- ___block_literal_global.1161
- ___block_literal_global.1167
- ___block_literal_global.1204
- ___block_literal_global.1252
- ___block_literal_global.1460
- ___block_literal_global.1607
- ___block_literal_global.1611
- ___block_literal_global.1643
- ___block_literal_global.1654
- ___block_literal_global.1656
- ___block_literal_global.1658
- ___block_literal_global.1674
- ___block_literal_global.1790
- ___block_literal_global.180
- ___block_literal_global.1813
- ___block_literal_global.1838
- ___block_literal_global.272
- ___block_literal_global.294
- ___block_literal_global.371
- ___block_literal_global.555
- ___block_literal_global.586
- ___block_literal_global.588
- ___block_literal_global.594
- ___block_literal_global.599
- ___block_literal_global.601
- ___block_literal_global.603
- ___block_literal_global.605
- ___block_literal_global.607
- ___block_literal_global.609
- ___block_literal_global.611
- ___block_literal_global.624
- ___block_literal_global.636
- ___block_literal_global.637
- ___block_literal_global.639
- ___block_literal_global.642
- ___block_literal_global.664
- ___block_literal_global.691
- ___block_literal_global.697
- ___block_literal_global.785
- ___block_literal_global.809
- ___block_literal_global.814
- ___block_literal_global.816
- ___block_literal_global.820
- ___block_literal_global.822
- ___block_literal_global.823
- ___block_literal_global.846
- ___block_literal_global.856
- ___block_literal_global.859
- ___block_literal_global.887
- ___block_literal_global.892
- ___block_literal_global.898
- ___block_literal_global.902
- ___block_literal_global.904
- ___block_literal_global.908
- ___block_literal_global.910
- ___block_literal_global.914
- ___block_literal_global.916
- ___block_literal_global.920
- ___block_literal_global.922
- ___block_literal_global.926
- ___block_literal_global.928
- ___block_literal_global.932
- ___block_literal_global.940
- _objc_msgSend$_slideOverCenterExitingTimerWaitingWhileStillCloseWithCenter:
- _objc_msgSend$appsRatingExemptedBundleIDs
- _objc_msgSend$frameWithContentWithFrame:
- _objc_msgSend$initWithShadowAttributes:maskCornerRadius:
- _objc_msgSend$requiresFullScreen
- _objc_msgSend$setRequiresFullScreen:
- _objc_msgSend$windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:
- _objc_msgSend$windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:
- _objc_msgSend$windowingConfigurationForWindowScene:interfaceOrientation:requiresFullScreen:floatingDockHeight:
CStrings:
+ "@152@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80d88d96d104d112d120d128B136B140B144B148"
+ "@40@0:8@16q24d32"
+ "@72@0:8{SBDisplayItemSlideOverConfiguration=qd{CGSize=dd}BBB}16@56@64"
+ "@80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48d56B64B68B72B76"
+ "AX Click"
+ "CameraCaptureAppActivator"
+ "Context: %{public}@"
+ "Double Click"
+ "Druid did disable secure rendering"
+ "Druid will enable secure rendering"
+ "Evaluate scene visibility for %{public}@ invalidateClientProcess[%{BOOL}u] isInSecureDisplayMode[%{BOOL}u] canShowWhileLocked[%{BOOL}u]"
+ "Final response"
+ "Hide_App"
+ "Hide_Others"
+ "No preference"
+ "Response log"
+ "Response log: %{public}@"
+ "Response: %{public}@"
+ "Single Click"
+ "TB,N,GisAppGestureActive,V_appGestureActive"
+ "Tq,N,V_behavior"
+ "_appGestureActive"
+ "_centerExitingEntryPoint"
+ "_homeGrabberViewBehaviorForAppLayout:"
+ "_multitaskingMode"
+ "_performSlideOverConfigurationUpdateWithConfiguration:appLayout:layoutAttributes:"
+ "_removePendingAlertForItem:"
+ "_rubberbandingRangeX"
+ "_rubberbandingRangeY"
+ "_slideOverCenterExitRemainingTimeWithSettledDuration:"
+ "_updateGlyphWithTintColor"
+ "addIconOcclusionReason:removeIconOcclusionReason:updateVisibleIcons:"
+ "appGestureActive"
+ "biomeStageManagerMode"
+ "builderWithClass:"
+ "coach intent"
+ "displayItemIsAlwaysMaximized:"
+ "glassLegibilitySetting"
+ "handleActivityWillDismissFromBottomSwipeGesture"
+ "handleEntityWillDismissFromBottomSwipeGesture"
+ "hasNonUnknownIntents"
+ "imageNamed:inBundle:withConfiguration:"
+ "initWithStarting:multitaskingMode:"
+ "initWithVariant:size:"
+ "isAppGestureActive"
+ "launch intent"
+ "prewarm intent"
+ "setAppGestureActive:"
+ "systemTraitsAffectingColorAppearance"
+ "this device doesn't currently support activating apps in roles other than primary and center"
+ "timeWithinRadius:"
+ "wake intent"
+ "windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:"
+ "windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:"
+ "windowingConfigurationForWindowScene:interfaceOrientation:floatingDockHeight:"
- "@\"MTShadowView\""
- "@\"MTVisualStylingProvider\""
- "@156@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48q80d88d96d104d112d120d128B136B140B144B148B152"
- "@44@0:8@16q24B32d36"
- "@84@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16q48d56B64B68B72B76B80"
- "T@\"MTMaterialView\",&,N,V_materialView"
- "T@\"MTShadowView\",&,N,V_shadowView"
- "T@\"MTVisualStylingProvider\",&,N,V_stylingProvider"
- "TB,N,V_requiresFullScreen"
- "UIViewGlassGetLegibilitySetting"
- "_cachedWindowingConfiguration_requiresFullScreen"
- "_requiresFullScreen"
- "_slideOverCenterExitingTimerWaitingWhileStillCloseWithCenter:"
- "_slideOverCenterSettledPosition"
- "_stylingProvider"
- "appsRatingExemptedBundleIDs"
- "com.apple.UIKit"
- "frameWithContentWithFrame:"
- "initWithShadowAttributes:maskCornerRadius:"
- "requiresFullScreen"
- "setMaterialView:"
- "setRequiresFullScreen:"
- "setShadowView:"
- "setStylingProvider:"
- "stylingProvider"
- "windowingConfigurationForContainerBounds:interfaceOrientation:floatingDockHeight:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:"
- "windowingConfigurationForContainerBounds:nativeContainerReferencePixelBounds:interfaceOrientation:floatingDockHeight:statusBarHeight:prototypingMinimumWindowWidth:prototypingMinimumWindowHeight:prototypingSlideOverEnterCenterRegionThreshold:prototypingSlideOverExitCenterRegionThreshold:requiresFullScreen:prefersStripHidden:prefersDockHidden:isEmbeddedDisplay:isFlexibleWindowingEnabled:"
- "windowingConfigurationForWindowScene:interfaceOrientation:requiresFullScreen:floatingDockHeight:"

```
