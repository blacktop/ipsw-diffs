## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

-4503.5.9.0.0
-  __TEXT.__text: 0x14e960
-  __TEXT.__auth_stubs: 0x1390
+4552.106.0.0.0
+  __TEXT.__text: 0x15d998
+  __TEXT.__auth_stubs: 0x13a0
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x14f04
-  __TEXT.__const: 0x2970
-  __TEXT.__cstring: 0x94b5
-  __TEXT.__oslogstring: 0x8651
-  __TEXT.__gcc_except_tab: 0xbb4
-  __TEXT.__ustring: 0x94
+  __TEXT.__objc_methlist: 0x15bdc
+  __TEXT.__const: 0x2980
+  __TEXT.__cstring: 0x9d78
+  __TEXT.__oslogstring: 0x8883
+  __TEXT.__gcc_except_tab: 0xd10
+  __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x3bf8
-  __TEXT.__objc_classname: 0x32c2
-  __TEXT.__objc_methname: 0x3c9fa
-  __TEXT.__objc_methtype: 0x9258
-  __TEXT.__objc_stubs: 0x23c60
-  __DATA_CONST.__got: 0x1460
-  __DATA_CONST.__const: 0x2870
-  __DATA_CONST.__objc_classlist: 0x758
+  __TEXT.__unwind_info: 0x3e18
+  __TEXT.__objc_classname: 0x3414
+  __TEXT.__objc_methname: 0x3f169
+  __TEXT.__objc_methtype: 0x9a44
+  __TEXT.__objc_stubs: 0x24e00
+  __DATA_CONST.__got: 0x14f8
+  __DATA_CONST.__const: 0x2980
+  __DATA_CONST.__objc_classlist: 0x788
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x650
+  __DATA_CONST.__objc_protolist: 0x680
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb988
+  __DATA_CONST.__objc_selrefs: 0xc0f8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x5a0
-  __DATA_CONST.__objc_arraydata: 0x1030
-  __AUTH_CONST.__auth_got: 0x9d8
-  __AUTH_CONST.__const: 0x780
-  __AUTH_CONST.__cfstring: 0xb5a0
-  __AUTH_CONST.__objc_const: 0x3a0b8
-  __AUTH_CONST.__objc_doubleobj: 0x5e0
-  __AUTH_CONST.__objc_arrayobj: 0x1230
-  __AUTH_CONST.__objc_intobj: 0x420
-  __AUTH.__objc_data: 0x1270
-  __DATA.__objc_ivar: 0x1a08
-  __DATA.__data: 0x4bc8
-  __DATA.__bss: 0xc0
-  __DATA_DIRTY.__objc_data: 0x3700
+  __DATA_CONST.__objc_superrefs: 0x5d0
+  __DATA_CONST.__objc_arraydata: 0x10c0
+  __AUTH_CONST.__auth_got: 0x9e0
+  __AUTH_CONST.__const: 0x7c0
+  __AUTH_CONST.__cfstring: 0xbc20
+  __AUTH_CONST.__objc_const: 0x3bdb8
+  __AUTH_CONST.__objc_doubleobj: 0x630
+  __AUTH_CONST.__objc_arrayobj: 0x1290
+  __AUTH_CONST.__objc_intobj: 0x438
+  __AUTH.__objc_data: 0x13b0
+  __DATA.__objc_ivar: 0x1adc
+  __DATA.__data: 0x4e08
+  __DATA.__bss: 0xd0
+  __DATA_DIRTY.__objc_data: 0x37a0
   __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MaterialKit.framework/MaterialKit
   - /System/Library/PrivateFrameworks/MediaControls.framework/MediaControls
+  - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/PaperBoardUI.framework/PaperBoardUI

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F87AF776-4D71-3B2B-B780-6B8098C408A6
-  Functions: 6743
-  Symbols:   24759
-  CStrings:  13521
+  UUID: 0BC8AFB6-EAB8-3885-ABEA-48B081859480
+  Functions: 6971
+  Symbols:   25523
+  CStrings:  14028
 
Symbols:
+ +[CSComponent notificationDimmingLayer]
+ +[CSCoverSheetSDFBackdropView layerClass]
+ +[CSNotificationDimView layerClass]
+ -[CSActivityContentView .cxx_destruct]
+ -[CSActivityContentView _buttonGroupName]
+ -[CSActivityContentView adjustedCrossfadeProgressForCrossfadeProgress:]
+ -[CSActivityContentView cleanUpAfterCrossfadeCompletion]
+ -[CSActivityContentView delegate]
+ -[CSActivityContentView hasSameOriginatingIconAsForIconZoomingView:]
+ -[CSActivityContentView iconContentScale]
+ -[CSActivityContentView iconImageAlignment]
+ -[CSActivityContentView iconImageFrame]
+ -[CSActivityContentView iconImageSizeMatchesBoundsSize]
+ -[CSActivityContentView iconImageSize]
+ -[CSActivityContentView intrinsicContentSize]
+ -[CSActivityContentView matchingIconZoomingViewOverlay]
+ -[CSActivityContentView prepareToCrossfadeImageWithView:]
+ -[CSActivityContentView scaleForFadeValue:originalSize:containerSize:]
+ -[CSActivityContentView setCrossfadeCornerRadius:]
+ -[CSActivityContentView setDelegate:]
+ -[CSActivityContentView setIconContentHidden:]
+ -[CSActivityContentView setMorphFraction:]
+ -[CSActivityContentView shouldClipToBoundsWhenSizeChanges]
+ -[CSActivityContentView sizeThatFits:]
+ -[CSActivityFullScreenViewController initWithDescriptor:]
+ -[CSActivityFullScreenViewController isContentVisibleAndAppeared]
+ -[CSActivityFullScreenViewController viewWillAppear:]
+ -[CSActivityFullScreenViewController viewWillDisappear:]
+ -[CSActivityListItemViewController .cxx_destruct]
+ -[CSActivityListItemViewController _invalidateRestrictsTouchesAssertion]
+ -[CSActivityListItemViewController initWithDescriptor:]
+ -[CSActivityListItemViewController isContentVisibleAndAppeared]
+ -[CSActivityListItemViewController isListAppeared]
+ -[CSActivityListItemViewController isScreenOn]
+ -[CSActivityListItemViewController notificationListSupplementaryViewPresentableContentWillBecomeVisible:]
+ -[CSActivityListItemViewController setListAppeared:]
+ -[CSActivityListItemViewController setRestrictsTouchesOnHostedScene:]
+ -[CSActivityListItemViewController setScreenOn:]
+ -[CSActivityManager activityViewController:didReceiveAction:]
+ -[CSActivityManager activityViewController:requestsLaunchWithAction:]
+ -[CSActivityManager activityViewControllerAudioCategoriesDisablingVolumeHUDDidChange:]
+ -[CSActivityManager activityViewControllerBackgroundTintColorDidChange:]
+ -[CSActivityManager activityViewControllerBackgroundTintColorDidChange:].cold.1
+ -[CSActivityManager activityViewControllerHostShouldCancelTouches:]
+ -[CSActivityManager activityViewControllerSignificantUserInteractionBegan:]
+ -[CSActivityManager activityViewControllerSignificantUserInteractionEnded:]
+ -[CSActivityManager activityViewControllerTextColorDidChange:]
+ -[CSActivityManager activityViewControllerTextColorDidChange:].cold.1
+ -[CSActivityManager activityViewControllersByActivityIdentifier]
+ -[CSActivityManager didAddNewSceneHostEnvironment:]
+ -[CSActivityManager iconZoomingViewForActivityIdentifier:]
+ -[CSActivityManager init].cold.1
+ -[CSActivityManager setActivityViewControllersByActivityIdentifier:]
+ -[CSActivityViewController .cxx_destruct]
+ -[CSActivityViewController _actionButtonPressed:]
+ -[CSActivityViewController _backlightLuminanceDidChange]
+ -[CSActivityViewController _isScreenOn]
+ -[CSActivityViewController _preferredContentSizeDidChangeForChildViewController:]
+ -[CSActivityViewController _presentationModeForActivityPresentationMode:]
+ -[CSActivityViewController _presentationModeForHostedEntityContentMode:]
+ -[CSActivityViewController _setPresentationMode:]
+ -[CSActivityViewController _setScreenOn:]
+ -[CSActivityViewController _updateAudioCategoriesDisablingVolumeHUDWithReason:]
+ -[CSActivityViewController _visiblityForCSActivityVisibilty:]
+ -[CSActivityViewController activityDescriptorForContentView:]
+ -[CSActivityViewController activityHostTouchRestrictedRects]
+ -[CSActivityViewController activityHostViewController:didReceiveAction:]
+ -[CSActivityViewController activityHostViewController:requestsLaunchWithAction:]
+ -[CSActivityViewController activityHostViewControllerAudioCategoriesDisablingVolumeHUDDidChange:]
+ -[CSActivityViewController activityHostViewControllerBackgroundTintColorDidChange:]
+ -[CSActivityViewController activityHostViewControllerHostShouldCancelTouches:]
+ -[CSActivityViewController activityHostViewControllerSignificantUserInteractionBegan:]
+ -[CSActivityViewController activityHostViewControllerSignificantUserInteractionEnded:]
+ -[CSActivityViewController activityHostViewControllerTextColorDidChange:]
+ -[CSActivityViewController audioCategoriesDisablingVolumeHUD]
+ -[CSActivityViewController conformsToCSHostableEntityPresenting]
+ -[CSActivityViewController contentSizeForContentView:]
+ -[CSActivityViewController dealloc]
+ -[CSActivityViewController delegate]
+ -[CSActivityViewController ensureContent:queue:completion:]
+ -[CSActivityViewController entityPresenterDelegate]
+ -[CSActivityViewController handleEvent:]
+ -[CSActivityViewController hostDelegate]
+ -[CSActivityViewController hostViewController]
+ -[CSActivityViewController iconZoomingView]
+ -[CSActivityViewController initWithDescriptor:sceneType:]
+ -[CSActivityViewController initWithHostViewController:]
+ -[CSActivityViewController invalidate]
+ -[CSActivityViewController isContentVisibleAndAppeared]
+ -[CSActivityViewController loadView]
+ -[CSActivityViewController reevaluateAudioCategoriesDisablingVolumeHUDForReason:]
+ -[CSActivityViewController reevaluatePresentationModeForReason:]
+ -[CSActivityViewController sceneHostEnvironmentEntriesForBacklightSession]
+ -[CSActivityViewController sceneHostEnvironmentObserver]
+ -[CSActivityViewController setContentVisibleAndAppeared:]
+ -[CSActivityViewController setDelegate:]
+ -[CSActivityViewController setEntityPresenterDelegate:]
+ -[CSActivityViewController setHostDelegate:]
+ -[CSActivityViewController setHostableEntityContentMode:]
+ -[CSActivityViewController setPresentationMode:]
+ -[CSActivityViewController setSceneHostEnvironmentObserver:]
+ -[CSActivityViewController setVisibility:]
+ -[CSActivityViewController viewDidLoad]
+ -[CSActivityViewController viewWillLayoutSubviews]
+ -[CSActivityViewController wouldHandleButtonEvent:]
+ -[CSBackgroundContentViewController _reevaluateContentObscured]
+ -[CSBackgroundContentViewController _setContentObscured:]
+ -[CSBackgroundContentViewController aggregateAppearance:]
+ -[CSBackgroundContentViewController handleEvent:]
+ -[CSBackgroundContentViewController hasContentAboveCoverSheet]
+ -[CSBackgroundContentViewController isContentObscured]
+ -[CSBackgroundContentViewController scene:didUpdateClientSettings:]
+ -[CSBackgroundContentViewController setHasContentAboveCoverSheet:]
+ -[CSBackgroundContentViewController viewDidMoveToWindow:shouldAppearOrDisappear:]
+ -[CSCameraExtensionViewController coverSheetViewController]
+ -[CSCameraExtensionViewController iconZoomingView]
+ -[CSCameraExtensionViewController setCoverSheetViewController:]
+ -[CSCameraSystemQuickAction initWithQuickActionControlIdentity:instance:delegate:prewarmer:]
+ -[CSCombinedListViewController _edgeInsetsForUnsupportedQuickActionsForOrientation:]
+ -[CSCombinedListViewController activityViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:]
+ -[CSCombinedListViewController effectiveListMaxY]
+ -[CSCombinedListViewController invalidateContentInsets]
+ -[CSCombinedListViewController notificationStructuredListViewController:glassContentInterfaceStyleOverridenToUserInterfaceStyle:]
+ -[CSCombinedListViewController notificationStructuredListViewController:requestsUpdateNotificationDimViewFadeRadiusY:]
+ -[CSCoverSheetAppearanceResolver _resolveNotificationDimmingLayerComponent]
+ -[CSCoverSheetSDFBackdropView .cxx_destruct]
+ -[CSCoverSheetSDFBackdropView _shouldAnimatePropertyWithKey:]
+ -[CSCoverSheetSDFBackdropView backdropLayer]
+ -[CSCoverSheetSDFBackdropView setBackdropLayer:]
+ -[CSCoverSheetSDFView .cxx_destruct]
+ -[CSCoverSheetSDFView _layoutLayer:inBounds:]
+ -[CSCoverSheetSDFView _setupAberrationLayer]
+ -[CSCoverSheetSDFView _setupDisplacementLayer]
+ -[CSCoverSheetSDFView _updateGlassLayerFilterValues]
+ -[CSCoverSheetSDFView aberrationElementLayer]
+ -[CSCoverSheetSDFView aberrationLayer]
+ -[CSCoverSheetSDFView backdropLayer]
+ -[CSCoverSheetSDFView backdropView]
+ -[CSCoverSheetSDFView cornerRadius]
+ -[CSCoverSheetSDFView displacementElementLayer]
+ -[CSCoverSheetSDFView displacementLayer]
+ -[CSCoverSheetSDFView effectMultiplier]
+ -[CSCoverSheetSDFView initWithFrame:]
+ -[CSCoverSheetSDFView layoutSubviews]
+ -[CSCoverSheetSDFView screenScale]
+ -[CSCoverSheetSDFView setCornerRadius:]
+ -[CSCoverSheetSDFView setEffectMultiplier:]
+ -[CSCoverSheetTransitionSettings crossBlurEnd]
+ -[CSCoverSheetTransitionSettings crossBlurStart]
+ -[CSCoverSheetTransitionSettings crossBlursForTransition]
+ -[CSCoverSheetTransitionSettings setCrossBlurEnd:]
+ -[CSCoverSheetTransitionSettings setCrossBlurStart:]
+ -[CSCoverSheetTransitionSettings setCrossBlursForTransition:]
+ -[CSCoverSheetTransitionsSettings setDefaultValuesForCrossFadeOnTouchUp]
+ -[CSCoverSheetView _addContentsContainerView]
+ -[CSCoverSheetView _addNotificationDimView]
+ -[CSCoverSheetView _addWallpaperLegibilityContainerView]
+ -[CSCoverSheetView _effectiveContentsContainerView]
+ -[CSCoverSheetView _layoutComplicationContainerView]
+ -[CSCoverSheetView _layoutContentContainerView]
+ -[CSCoverSheetView _layoutGlassEffectView]
+ -[CSCoverSheetView _layoutNotificationDimView]
+ -[CSCoverSheetView _layoutWallpaperLegibilityContainerView]
+ -[CSCoverSheetView backgroundGlassView]
+ -[CSCoverSheetView complicationContainerView]
+ -[CSCoverSheetView effectiveContainerBounds]
+ -[CSCoverSheetView effectiveContentsContainerView]
+ -[CSCoverSheetView modalPresentationViewOffset]
+ -[CSCoverSheetView notificationDimView]
+ -[CSCoverSheetView setBackgroundGlassView:]
+ -[CSCoverSheetView setComplicationContainerView:]
+ -[CSCoverSheetView setModalPresentationViewOffset:]
+ -[CSCoverSheetView setNotificationDimView:]
+ -[CSCoverSheetView wallpaperLegibilityContainerView]
+ -[CSCoverSheetViewController __currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:backgroundContentAppearance:]
+ -[CSCoverSheetViewController __currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:backgroundContentAppearance:].cold.1
+ -[CSCoverSheetViewController __currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:backgroundContentAppearance:].cold.2
+ -[CSCoverSheetViewController __currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:backgroundContentAppearance:].cold.3
+ -[CSCoverSheetViewController _adaptiveTimeMaxYFromConfigurationAndPosterPreferences]
+ -[CSCoverSheetViewController _effectivePreferredSalientContentRectangle]
+ -[CSCoverSheetViewController _posterPersistedTimeMaxY]
+ -[CSCoverSheetViewController _shouldAllowBottomGridPosition]
+ -[CSCoverSheetViewController _shouldAllowGlassCoverSheet]
+ -[CSCoverSheetViewController _updateBackgroundGlassView]
+ -[CSCoverSheetViewController _updateChargingSubtitleWithString:timeout:]
+ -[CSCoverSheetViewController _updateComplicationContainerPosition]
+ -[CSCoverSheetViewController _updateForSensitiveUI]
+ -[CSCoverSheetViewController _updateModalPresentationControllerVisibility:]
+ -[CSCoverSheetViewController _updateNotificationDimmingLayer]
+ -[CSCoverSheetViewController _wallpaperOccludedAssertions]
+ -[CSCoverSheetViewController adaptiveTimeHonorsPreferredSalientContentRectangle]
+ -[CSCoverSheetViewController attemptPhoneUnlockWithRemoteDevice]
+ -[CSCoverSheetViewController backgroundContentDidOccludeWallpaperAssertion]
+ -[CSCoverSheetViewController bottomInsetForBottomComplications]
+ -[CSCoverSheetViewController cleanupInterstitialWhileOffScreen]
+ -[CSCoverSheetViewController complicationContainerUsesBottomPosition]
+ -[CSCoverSheetViewController complicationsUsingBottomPosition]
+ -[CSCoverSheetViewController disableRecentUserPresenceDetectionForReason:]
+ -[CSCoverSheetViewController dismissInterstitialPresentationAnimated:]
+ -[CSCoverSheetViewController dismissInterstitialPresentationAnimated:].cold.1
+ -[CSCoverSheetViewController dismissOverlays:animated:]
+ -[CSCoverSheetViewController enableRecentUserPresenceDetectionForReason:]
+ -[CSCoverSheetViewController endCoverSheetTransition]
+ -[CSCoverSheetViewController isDepthEffectDisabled]
+ -[CSCoverSheetViewController isUserPresenceDetectionAllowed]
+ -[CSCoverSheetViewController notificationListDidOccludeWallpaperAssertion]
+ -[CSCoverSheetViewController performInterstitialPresentationAnimated:]
+ -[CSCoverSheetViewController performInterstitialPresentationAnimated:].cold.1
+ -[CSCoverSheetViewController phoneUnlockEnabledAndRequirementsMet]
+ -[CSCoverSheetViewController phoneUnlockWithVisionController:attemptFailedWithError:]
+ -[CSCoverSheetViewController phoneUnlockWithVisionControllerAttemptSucceeded:]
+ -[CSCoverSheetViewController posterPreferredSalientContentRectangle]
+ -[CSCoverSheetViewController setAdaptiveTimeHonorsPreferredSalientContentRectangle:]
+ -[CSCoverSheetViewController setBackgroundContentDidOccludeWallpaperAssertion:]
+ -[CSCoverSheetViewController setComplicationContainerUsesBottomPosition:]
+ -[CSCoverSheetViewController setNotificationListDidOccludeWallpaperAssertion:]
+ -[CSCoverSheetViewController setPasscodeLockVisible:animated:showBackground:completion:]
+ -[CSCoverSheetViewController setPasscodeLockVisible:animated:showBackground:forceBiometricPresentation:completion:]
+ -[CSCoverSheetViewController setPosterPreferredSalientContentRectangle:]
+ -[CSCoverSheetViewController setYContentOffset:]
+ -[CSCoverSheetViewController set_wallpaperOccludedAssertions:]
+ -[CSCoverSheetViewController updateCoverSheetDraggingProgress:]
+ -[CSCoverSheetViewController updateCoverSheetTransitionProgress:]
+ -[CSCoverSheetViewController updateFont:preferredTimeMaxYPortrait:preferredTimeMaxYLandscape:vibrancyConfiguration:numberingSystem:contentStyle:]
+ -[CSCoverSheetViewController userPresenceDetectedRecentlyDidChange:]
+ -[CSCoverSheetViewController userPresenceDetectedSinceWakeDidChange:]
+ -[CSDateViewComponent _setValueForInternalPageIndex:hidesTime:constrainsTime:usesCompactTime:]
+ -[CSDateViewComponent _valueCheckForMask:]
+ -[CSDateViewComponent constrainsTimeHeight:]
+ -[CSDateViewComponent constrainsTimeHeight]
+ -[CSDateViewComponent setConstrainsTimeHeight:]
+ -[CSDateViewComponent setConstrainsTimeHeight:].cold.1
+ -[CSDateViewComponent setHidesTime:].cold.1
+ -[CSDateViewComponent setShowCompactTime:]
+ -[CSDateViewComponent setShowCompactTime:].cold.1
+ -[CSDateViewComponent showCompactTime:]
+ -[CSDateViewComponent showCompactTime]
+ -[CSDeviceBlockViewController findMyAccount]
+ -[CSDeviceBlockViewController setFindMyAccount:]
+ -[CSDeviceUnblockViewController viewDidLoad].cold.1
+ -[CSDeviceUnblockViewModel account]
+ -[CSDeviceUnblockViewModel lastBackupTime]
+ -[CSDeviceUnblockViewModel lastBackupTime].cold.1
+ -[CSDeviceUnblockViewModel lastBackupTime].cold.2
+ -[CSDeviceUnblockViewModel lastBackupTime].cold.3
+ -[CSDeviceUnblockViewModel setAccount:]
+ -[CSFlashlightQuickAction _deviceBlockStateDidChangeNotification:]
+ -[CSFlashlightQuickAction _featureLockStateDidChangeNotification:]
+ -[CSFlashlightQuickAction _setupIfNecessary]
+ -[CSFlashlightQuickAction buttonVisibilityChangedTo:]
+ -[CSFlashlightQuickAction initWithLockoutController:]
+ -[CSFlashlightQuickAction lockoutController]
+ -[CSFlashlightQuickAction setLockoutController:]
+ -[CSHostedEntityViewController hostedEntityViewController]
+ -[CSHostedEntityViewController iconZoomingView]
+ -[CSLockScreenSettings setWallpaperOcclusionPercentage:]
+ -[CSLockScreenSettings wallpaperOcclusionPercentage]
+ -[CSMainPageContentViewController bottomComplicationsInsetForCombinedListViewController:]
+ -[CSMainPageContentViewController complicationGridLayoutMetricsProvider]
+ -[CSMainPageContentViewController complicationsUsingBottomPositionForCombinedListViewController:]
+ -[CSMainPageContentViewController setComplicationGridLayoutMetricsProvider:]
+ -[CSMainPageContentViewController userPresenceDetectedRecentlyDidChange:]
+ -[CSNotificationDimView .cxx_destruct]
+ -[CSNotificationDimView _configureFilter]
+ -[CSNotificationDimView _configureShadowMask]
+ -[CSNotificationDimView _layoutShadowMask]
+ -[CSNotificationDimView _performAlphaAnimationToAlpha:]
+ -[CSNotificationDimView effectiveFadeInThreshold]
+ -[CSNotificationDimView effectiveFadeRadiusY]
+ -[CSNotificationDimView fadeAlpha]
+ -[CSNotificationDimView fadeAnchorY]
+ -[CSNotificationDimView fadeRadiusY]
+ -[CSNotificationDimView fadeWidth]
+ -[CSNotificationDimView initWithCoder:]
+ -[CSNotificationDimView initWithFrame:]
+ -[CSNotificationDimView isPerformingAlphaAnimation]
+ -[CSNotificationDimView layoutSubviews]
+ -[CSNotificationDimView setFadeAlpha:]
+ -[CSNotificationDimView setFadeAnchorY:]
+ -[CSNotificationDimView setFadeRadiusY:]
+ -[CSNotificationDimView setFadeWidth:]
+ -[CSNotificationDimView setFrame:]
+ -[CSNotificationDimView setIsPerformingAlphaAnimation:]
+ -[CSNotificationDimView setShadowMaskLayer:]
+ -[CSNotificationDimView shadowMaskLayer]
+ -[CSNotificationDimmingLayerComponent init]
+ -[CSPosterSwitcherViewController _updateAdaptiveTimeTextHeightForSceneSettings:]
+ -[CSPosterSwitcherViewController lastAdaptiveTimeTextHeight]
+ -[CSPosterSwitcherViewController sceneHandle:didUpdateClientSettings:]
+ -[CSPosterSwitcherViewController sceneHandle:didUpdateClientSettings:].cold.1
+ -[CSPosterSwitcherViewController setLastAdaptiveTimeTextHeight:]
+ -[CSQuickAction buttonVisibilityChangedTo:]
+ -[CSQuickActionControlGlyphView _updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:]
+ -[CSQuickActionsView setUsesSensitiveUIAppearance:]
+ -[CSQuickActionsView usesSensitiveUIAppearance]
+ -[CSQuickActionsViewController _updateForSensitiveUI]
+ -[CSUserPresenceMonitor _setUserPresenceDetectedRecently:]
+ -[CSUserPresenceMonitor _updateFaceDetectionStateForMonitorType:]
+ -[CSUserPresenceMonitor disableDetectionForReason:monitorType:]
+ -[CSUserPresenceMonitor enableDetectionForReason:monitorType:]
+ -[CSUserPresenceMonitor userPresenceDetectedRecently]
+ -[CSWidgetGridViewController isEmpty]
+ -[CSWidgetGridViewController needsNestedVibrancyEffectView]
+ -[CSWidgetGridViewController setNeedsNestedVibrancyEffectView:]
+ GCC_except_table116
+ GCC_except_table168
+ GCC_except_table19
+ GCC_except_table208
+ GCC_except_table211
+ GCC_except_table306
+ GCC_except_table39
+ GCC_except_table441
+ GCC_except_table45
+ GCC_except_table498
+ GCC_except_table51
+ GCC_except_table518
+ GCC_except_table528
+ GCC_except_table606
+ GCC_except_table65
+ GCC_except_table663
+ GCC_except_table673
+ GCC_except_table675
+ GCC_except_table684
+ GCC_except_table695
+ GCC_except_table705
+ GCC_except_table84
+ GCC_except_table87
+ _CSFlashlightControlKind
+ _NSStringFromPRUISSwitcherLayoutMode
+ _OBJC_CLASS_$_CASDFElementLayer
+ _OBJC_CLASS_$_CASDFGlassDisplacementEffect
+ _OBJC_CLASS_$_CASDFLayer
+ _OBJC_CLASS_$_CSActivityContentView
+ _OBJC_CLASS_$_CSActivityFullScreenViewController
+ _OBJC_CLASS_$_CSActivityListItemViewController
+ _OBJC_CLASS_$_CSActivityViewController
+ _OBJC_CLASS_$_CSCoverSheetSDFBackdropView
+ _OBJC_CLASS_$_CSCoverSheetSDFView
+ _OBJC_CLASS_$_CSNotificationDimView
+ _OBJC_CLASS_$_CSNotificationDimmingLayerComponent
+ _OBJC_CLASS_$_MBManager
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_SBFAnimationUtilities
+ _OBJC_CLASS_$_SBUIPhoneUnlockWithRemoteDeviceCoordinator
+ _OBJC_CLASS_$_SBUIPhoneUnlockWithVisionController
+ _OBJC_IVAR_$_CSActivityContentView._delegate
+ _OBJC_IVAR_$_CSActivityContentView._iconZoomCrossfadeCounterpartFrame
+ _OBJC_IVAR_$_CSActivityListItemViewController._isContentVisible
+ _OBJC_IVAR_$_CSActivityListItemViewController._listAppeared
+ _OBJC_IVAR_$_CSActivityListItemViewController._restrictsTouchesAssertion
+ _OBJC_IVAR_$_CSActivityListItemViewController._screenOn
+ _OBJC_IVAR_$_CSActivityManager._activityViewControllersByActivityIdentifier
+ _OBJC_IVAR_$_CSActivityViewController._audioCategoriesDisablingVolumeHUD
+ _OBJC_IVAR_$_CSActivityViewController._contentVisibleAndAppeared
+ _OBJC_IVAR_$_CSActivityViewController._delegate
+ _OBJC_IVAR_$_CSActivityViewController._entityPresenterDelegate
+ _OBJC_IVAR_$_CSActivityViewController._hostDelegate
+ _OBJC_IVAR_$_CSActivityViewController._hostViewController
+ _OBJC_IVAR_$_CSActivityViewController._sceneHostEnvironmentObserver
+ _OBJC_IVAR_$_CSActivityViewController._sceneType
+ _OBJC_IVAR_$_CSActivityViewController._screenOn
+ _OBJC_IVAR_$_CSBackgroundContentViewController._contentObscured
+ _OBJC_IVAR_$_CSBackgroundContentViewController._hasContentAboveCoverSheet
+ _OBJC_IVAR_$_CSBackgroundContentViewController._isModalPresented
+ _OBJC_IVAR_$_CSBackgroundContentViewController._showCompactTime
+ _OBJC_IVAR_$_CSCameraExtensionViewController._coverSheetViewController
+ _OBJC_IVAR_$_CSCombinedListViewController._notificationDimmingLayerComponent
+ _OBJC_IVAR_$_CSCoverSheetSDFBackdropView._backdropLayer
+ _OBJC_IVAR_$_CSCoverSheetSDFView._aberrationElementLayer
+ _OBJC_IVAR_$_CSCoverSheetSDFView._aberrationLayer
+ _OBJC_IVAR_$_CSCoverSheetSDFView._backdropLayer
+ _OBJC_IVAR_$_CSCoverSheetSDFView._backdropView
+ _OBJC_IVAR_$_CSCoverSheetSDFView._cornerRadius
+ _OBJC_IVAR_$_CSCoverSheetSDFView._displacementElementLayer
+ _OBJC_IVAR_$_CSCoverSheetSDFView._displacementLayer
+ _OBJC_IVAR_$_CSCoverSheetSDFView._effectMultiplier
+ _OBJC_IVAR_$_CSCoverSheetSDFView._screenScale
+ _OBJC_IVAR_$_CSCoverSheetTransitionSettings._crossBlurEnd
+ _OBJC_IVAR_$_CSCoverSheetTransitionSettings._crossBlurStart
+ _OBJC_IVAR_$_CSCoverSheetTransitionSettings._crossBlursForTransition
+ _OBJC_IVAR_$_CSCoverSheetView._backgroundGlassView
+ _OBJC_IVAR_$_CSCoverSheetView._complicationContainerView
+ _OBJC_IVAR_$_CSCoverSheetView._contentsContainerView
+ _OBJC_IVAR_$_CSCoverSheetView._modalPresentationViewOffset
+ _OBJC_IVAR_$_CSCoverSheetView._notificationDimView
+ _OBJC_IVAR_$_CSCoverSheetView._wallpaperLegibilityContainerView
+ _OBJC_IVAR_$_CSCoverSheetViewController.__wallpaperOccludedAssertions
+ _OBJC_IVAR_$_CSCoverSheetViewController._adaptiveTimeHonorsPreferredSalientContentRectangle
+ _OBJC_IVAR_$_CSCoverSheetViewController._backgroundContentDidOccludeWallpaperAssertion
+ _OBJC_IVAR_$_CSCoverSheetViewController._complicationContainerUsesBottomPosition
+ _OBJC_IVAR_$_CSCoverSheetViewController._miscellaneousDefaults
+ _OBJC_IVAR_$_CSCoverSheetViewController._notificationListDidOccludeWallpaperAssertion
+ _OBJC_IVAR_$_CSCoverSheetViewController._phoneUnlockWithRemoteDeviceCoordinator
+ _OBJC_IVAR_$_CSCoverSheetViewController._phoneUnlockWithVisionController
+ _OBJC_IVAR_$_CSCoverSheetViewController._posterPreferredSalientContentRectangle
+ _OBJC_IVAR_$_CSCoverSheetViewController._posterPreferredTimeMaxYLandscape
+ _OBJC_IVAR_$_CSCoverSheetViewController._posterPreferredTimeMaxYPortrait
+ _OBJC_IVAR_$_CSDeviceUnblockViewModel._account
+ _OBJC_IVAR_$_CSFlashlightQuickAction._lockoutController
+ _OBJC_IVAR_$_CSLockScreenSettings._wallpaperOcclusionPercentage
+ _OBJC_IVAR_$_CSMainPageContentViewController._complicationGridLayoutMetricsProvider
+ _OBJC_IVAR_$_CSNotificationDimView._effectiveFadeRadiusY
+ _OBJC_IVAR_$_CSNotificationDimView._fadeAlpha
+ _OBJC_IVAR_$_CSNotificationDimView._fadeAnchorY
+ _OBJC_IVAR_$_CSNotificationDimView._fadeRadiusY
+ _OBJC_IVAR_$_CSNotificationDimView._fadeWidth
+ _OBJC_IVAR_$_CSNotificationDimView._isPerformingAlphaAnimation
+ _OBJC_IVAR_$_CSNotificationDimView._shadowMaskLayer
+ _OBJC_IVAR_$_CSPosterSwitcherViewController._lastAdaptiveTimeTextHeight
+ _OBJC_IVAR_$_CSQuickActionsButton._iconZoomBackgroundView
+ _OBJC_IVAR_$_CSQuickActionsView._usesSensitiveUIAppearance
+ _OBJC_IVAR_$_CSUserPresenceMonitor._userPresenceDetectedRecently
+ _OBJC_METACLASS_$_CSActivityContentView
+ _OBJC_METACLASS_$_CSActivityFullScreenViewController
+ _OBJC_METACLASS_$_CSActivityListItemViewController
+ _OBJC_METACLASS_$_CSActivityViewController
+ _OBJC_METACLASS_$_CSCoverSheetSDFBackdropView
+ _OBJC_METACLASS_$_CSCoverSheetSDFView
+ _OBJC_METACLASS_$_CSNotificationDimView
+ _OBJC_METACLASS_$_CSNotificationDimmingLayerComponent
+ _OUTLINED_FUNCTION_23
+ _PRUISSwitcherLayoutTransitionAnimationSettings
+ _SBActionButtonPressedNotification
+ _SBSDetailedBatteryUIDismissDuration
+ __OBJC_$_CLASS_METHODS_CSCoverSheetSDFBackdropView
+ __OBJC_$_CLASS_METHODS_CSNotificationDimView
+ __OBJC_$_INSTANCE_METHODS_CSActivityContentView
+ __OBJC_$_INSTANCE_METHODS_CSActivityFullScreenViewController
+ __OBJC_$_INSTANCE_METHODS_CSActivityListItemViewController
+ __OBJC_$_INSTANCE_METHODS_CSActivityViewController
+ __OBJC_$_INSTANCE_METHODS_CSCoverSheetSDFBackdropView
+ __OBJC_$_INSTANCE_METHODS_CSCoverSheetSDFView
+ __OBJC_$_INSTANCE_METHODS_CSNotificationDimView
+ __OBJC_$_INSTANCE_METHODS_CSNotificationDimmingLayerComponent
+ __OBJC_$_INSTANCE_VARIABLES_CSActivityContentView
+ __OBJC_$_INSTANCE_VARIABLES_CSActivityListItemViewController
+ __OBJC_$_INSTANCE_VARIABLES_CSActivityViewController
+ __OBJC_$_INSTANCE_VARIABLES_CSCoverSheetSDFBackdropView
+ __OBJC_$_INSTANCE_VARIABLES_CSCoverSheetSDFView
+ __OBJC_$_INSTANCE_VARIABLES_CSNotificationDimView
+ __OBJC_$_PROP_LIST_CSActivityContentView
+ __OBJC_$_PROP_LIST_CSActivityListItemViewController
+ __OBJC_$_PROP_LIST_CSActivityViewController
+ __OBJC_$_PROP_LIST_CSCoverSheetSDFBackdropView
+ __OBJC_$_PROP_LIST_CSCoverSheetSDFView
+ __OBJC_$_PROP_LIST_CSHostableEntityContentContaining
+ __OBJC_$_PROP_LIST_CSNotificationDimView
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivityContentViewDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivityViewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSHostableEntityContentContaining
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSMainPageComplicationsMetricsProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSceneHostEnvironmentObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSActivityViewControllerHostDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSceneObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MBManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBUIPhoneUnlockWithVisionControllerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivityContentViewDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivityViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivityViewControllerHostDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSHostableEntityContentContaining
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSMainPageComplicationsMetricsProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSceneHostEnvironmentObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSceneObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MBManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBUIPhoneUnlockWithVisionControllerObserver
+ __OBJC_$_PROTOCOL_REFS_CSActivityContentViewDelegate
+ __OBJC_$_PROTOCOL_REFS_CSActivityViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_CSActivityViewControllerHostDelegate
+ __OBJC_$_PROTOCOL_REFS_CSHostableEntityContentContaining
+ __OBJC_$_PROTOCOL_REFS_CSMainPageComplicationsMetricsProvider
+ __OBJC_$_PROTOCOL_REFS_CSSceneHostEnvironmentObserving
+ __OBJC_$_PROTOCOL_REFS_FBSceneObserver
+ __OBJC_$_PROTOCOL_REFS_SBUIPhoneUnlockWithVisionControllerObserver
+ __OBJC_CLASS_PROTOCOLS_$_CSActivityContentView
+ __OBJC_CLASS_PROTOCOLS_$_CSActivityListItemViewController
+ __OBJC_CLASS_PROTOCOLS_$_CSActivityViewController
+ __OBJC_CLASS_PROTOCOLS_$_CSDeviceUnblockViewModel
+ __OBJC_CLASS_RO_$_CSActivityContentView
+ __OBJC_CLASS_RO_$_CSActivityFullScreenViewController
+ __OBJC_CLASS_RO_$_CSActivityListItemViewController
+ __OBJC_CLASS_RO_$_CSActivityViewController
+ __OBJC_CLASS_RO_$_CSCoverSheetSDFBackdropView
+ __OBJC_CLASS_RO_$_CSCoverSheetSDFView
+ __OBJC_CLASS_RO_$_CSNotificationDimView
+ __OBJC_CLASS_RO_$_CSNotificationDimmingLayerComponent
+ __OBJC_LABEL_PROTOCOL_$_CSActivityContentViewDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSActivityViewControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSActivityViewControllerHostDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSHostableEntityContentContaining
+ __OBJC_LABEL_PROTOCOL_$_CSMainPageComplicationsMetricsProvider
+ __OBJC_LABEL_PROTOCOL_$_CSSceneHostEnvironmentObserving
+ __OBJC_LABEL_PROTOCOL_$_FBSceneObserver
+ __OBJC_LABEL_PROTOCOL_$_MBManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBUIPhoneUnlockWithVisionControllerObserver
+ __OBJC_METACLASS_RO_$_CSActivityContentView
+ __OBJC_METACLASS_RO_$_CSActivityFullScreenViewController
+ __OBJC_METACLASS_RO_$_CSActivityListItemViewController
+ __OBJC_METACLASS_RO_$_CSActivityViewController
+ __OBJC_METACLASS_RO_$_CSCoverSheetSDFBackdropView
+ __OBJC_METACLASS_RO_$_CSCoverSheetSDFView
+ __OBJC_METACLASS_RO_$_CSNotificationDimView
+ __OBJC_METACLASS_RO_$_CSNotificationDimmingLayerComponent
+ __OBJC_PROTOCOL_$_CSActivityContentViewDelegate
+ __OBJC_PROTOCOL_$_CSActivityViewControllerDelegate
+ __OBJC_PROTOCOL_$_CSActivityViewControllerHostDelegate
+ __OBJC_PROTOCOL_$_CSHostableEntityContentContaining
+ __OBJC_PROTOCOL_$_CSMainPageComplicationsMetricsProvider
+ __OBJC_PROTOCOL_$_CSSceneHostEnvironmentObserving
+ __OBJC_PROTOCOL_$_FBSceneObserver
+ __OBJC_PROTOCOL_$_MBManagerDelegate
+ __OBJC_PROTOCOL_$_SBUIPhoneUnlockWithVisionControllerObserver
+ __UISolariumEnabled
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.782
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.783
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.784
+ ___115-[CSCoverSheetViewController setPasscodeLockVisible:animated:showBackground:forceBiometricPresentation:completion:]_block_invoke
+ ___115-[CSQuickActionControlGlyphView _updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:]_block_invoke
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.189
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.193
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.202
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.196
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.205
+ ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.748
+ ___49-[CSActivityViewController _setPresentationMode:]_block_invoke
+ ___51-[CSCoverSheetView setModalPresentationViewOffset:]_block_invoke
+ ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.654
+ ___52-[CSCombinedListViewController scrollViewDidScroll:]_block_invoke
+ ___53-[CSCoverSheetViewController willUIUnlockFromSource:]_block_invoke
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.448
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.449
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.457
+ ___55-[CSNotificationDimView _performAlphaAnimationToAlpha:]_block_invoke
+ ___55-[CSNotificationDimView _performAlphaAnimationToAlpha:]_block_invoke_2
+ ___55-[CSNotificationDimView _performAlphaAnimationToAlpha:]_block_invoke_3
+ ___55-[CSNotificationDimView _performAlphaAnimationToAlpha:]_block_invoke_4
+ ___57-[CSBackgroundContentViewController _setContentObscured:]_block_invoke
+ ___58-[CSActivityManager _addActivityListItemForContentUpdate:]_block_invoke.54
+ ___61-[CSActivityManager activityViewController:didReceiveAction:]_block_invoke
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.717
+ ___64-[CSPosterSwitcherViewController setLastAdaptiveTimeTextHeight:]_block_invoke
+ ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.484
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.759
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.760
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.767
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.765
+ ___66-[CSCoverSheetViewController _updateComplicationContainerPosition]_block_invoke
+ ___66-[CSCoverSheetViewController _updateComplicationContainerPosition]_block_invoke_2
+ ___67-[CSBackgroundContentViewController scene:didUpdateClientSettings:]_block_invoke
+ ___69-[CSActivityManager activityViewController:requestsLaunchWithAction:]_block_invoke
+ ___70-[CSPosterSwitcherViewController sceneHandle:didUpdateClientSettings:]_block_invoke
+ ___72-[CSCoverSheetViewController _updateChargingSubtitleWithString:timeout:]_block_invoke
+ ___72-[CSCoverSheetViewController _updateChargingSubtitleWithString:timeout:]_block_invoke_2
+ ___74-[CSQuickActionControlGlyphView initWithControlInstance:symbolScaleValue:]_block_invoke
+ ___74-[CSWidgetGridViewController _updateComplicationPresentationState:reason:]_block_invoke.48
+ ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.580
+ ___79-[CSQuickActionsViewController initWithLockScreenDefaults:applicationInformer:]_block_invoke
+ ___81-[CSBackgroundContentViewController viewDidMoveToWindow:shouldAppearOrDisappear:]_block_invoke
+ ___81-[CSNotificationAdjunctListViewController _insertItem:atPreferredIndex:animated:]_block_invoke.35
+ ___81-[CSPresentationViewController _updateContentViewControllersAnimated:completion:]_block_invoke.83
+ ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.581
+ ___96-[CSCoverSheetViewController initWithPageViewControllers:mainPageContentViewController:context:]_block_invoke_2
+ ___96-[CSCoverSheetViewController initWithPageViewControllers:mainPageContentViewController:context:]_block_invoke_3
+ ___98-[CSCoverSheetViewController activateCameraWithHostableEntity:animated:sendingActions:completion:]_block_invoke.147
+ _____loadActivityProgressKitIfNecessary_block_invoke
+ ___block_descriptor_32_e61_v24?0"CSQuickActionControlGlyphView"8"UITraitCollection"16l
+ ___block_descriptor_33_e33_v16?0"FBSMutableSceneSettings"8l
+ ___block_descriptor_40_e8_32s_e50_v16?0"CHUISMutableControlInstanceConfiguration"8ls32l8
+ ___block_descriptor_40_e8_32w_e64_v24?0"CSActivityListItemViewController"8"UITraitCollection"16lw32l8
+ ___block_descriptor_48_e8_32s40s_e43_v16?0"UIMutableApplicationSceneSettings"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e30_v20?0"<CSLockProviding>"8B16lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e36_v16?0"<BSCompoundAssertionState>"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s_e18_v16?0"NSString"8ls32l8s40l8
+ ___block_descriptor_64_e43_v16?0"UIMutableApplicationSceneSettings"8l
+ ___block_descriptor_72_e8_32s40s48w56w64w_e18_v16?0"UIAction"8lw48l8w56l8w64l8s32l8s40l8
+ ___block_descriptor_88_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_97_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___block_literal_global.106
+ ___block_literal_global.114
+ ___block_literal_global.195
+ ___block_literal_global.224
+ ___block_literal_global.2256
+ ___block_literal_global.305
+ ___block_literal_global.308
+ ___block_literal_global.313
+ ___block_literal_global.318
+ ___block_literal_global.332
+ ___block_literal_global.36
+ ___block_literal_global.400
+ ___block_literal_global.405
+ ___block_literal_global.410
+ ___block_literal_global.415
+ ___block_literal_global.418
+ ___block_literal_global.420
+ ___block_literal_global.425
+ ___block_literal_global.777
+ ___block_literal_global.779
+ ___block_literal_global.82
+ ___loadActivityProgressKitIfNecessary.activityProgressKit
+ ___loadActivityProgressKitIfNecessary.onceToken
+ _dlopen
+ _kAccountDataclassBackup
+ _kCAFilterChromaticAberrationMap
+ _kCAFilterDisplacementMap
+ _kCAFilterInputAlphaValues
+ _kCAFilterInputBlueValues
+ _kCAFilterInputGreenValues
+ _kCAFilterInputRedValues
+ _objc_msgSend$__currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:backgroundContentAppearance:
+ _objc_msgSend$_adaptiveTimeMaxYFromConfigurationAndPosterPreferences
+ _objc_msgSend$_addContentsContainerView
+ _objc_msgSend$_addNotificationDimView
+ _objc_msgSend$_addWallpaperLegibilityContainerView
+ _objc_msgSend$_animateByRetargetingAnimations:completion:
+ _objc_msgSend$_animateUsingSpringInteractive:animations:completion:
+ _objc_msgSend$_configureFilter
+ _objc_msgSend$_configureShadowMask
+ _objc_msgSend$_edgeInsetsForUnsupportedQuickActionsForOrientation:
+ _objc_msgSend$_effectiveContentsContainerView
+ _objc_msgSend$_effectivePreferredSalientContentRectangle
+ _objc_msgSend$_layoutComplicationContainerView
+ _objc_msgSend$_layoutContentContainerView
+ _objc_msgSend$_layoutGlassEffectView
+ _objc_msgSend$_layoutLayer:inBounds:
+ _objc_msgSend$_layoutNotificationDimView
+ _objc_msgSend$_layoutShadowMask
+ _objc_msgSend$_layoutWallpaperLegibilityContainerView
+ _objc_msgSend$_performAlphaAnimationToAlpha:
+ _objc_msgSend$_posterPersistedTimeMaxY
+ _objc_msgSend$_presentationModeForActivityPresentationMode:
+ _objc_msgSend$_presentationModeForHostedEntityContentMode:
+ _objc_msgSend$_reevaluateContentObscured
+ _objc_msgSend$_setContentObscured:
+ _objc_msgSend$_setPresentationMode:
+ _objc_msgSend$_setUserPresenceDetectedRecently:
+ _objc_msgSend$_setupAberrationLayer
+ _objc_msgSend$_setupDisplacementLayer
+ _objc_msgSend$_setupIfNecessary
+ _objc_msgSend$_shouldAllowBottomGridPosition
+ _objc_msgSend$_shouldAllowGlassCoverSheet
+ _objc_msgSend$_synchronizeDrawingWithFence:
+ _objc_msgSend$_updateAdaptiveTimeTextHeightForSceneSettings:
+ _objc_msgSend$_updateBackgroundGlassView
+ _objc_msgSend$_updateChargingSubtitleWithString:timeout:
+ _objc_msgSend$_updateComplicationContainerPosition
+ _objc_msgSend$_updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:
+ _objc_msgSend$_updateFaceDetectionStateForMonitorType:
+ _objc_msgSend$_updateForSensitiveUI
+ _objc_msgSend$_updateGlassLayerFilterValues
+ _objc_msgSend$_updateModalPresentationControllerVisibility:
+ _objc_msgSend$_updateNotificationDimmingLayer
+ _objc_msgSend$_visiblityForCSActivityVisibilty:
+ _objc_msgSend$activitySceneType
+ _objc_msgSend$activityViewController:didReceiveAction:
+ _objc_msgSend$activityViewController:requestsLaunchWithAction:
+ _objc_msgSend$activityViewControllerAudioCategoriesDisablingVolumeHUDDidChange:
+ _objc_msgSend$activityViewControllerBackgroundTintColorDidChange:
+ _objc_msgSend$activityViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:
+ _objc_msgSend$activityViewControllerHostShouldCancelTouches:
+ _objc_msgSend$activityViewControllerSignificantUserInteractionBegan:
+ _objc_msgSend$activityViewControllerSignificantUserInteractionEnded:
+ _objc_msgSend$activityViewControllerTextColorDidChange:
+ _objc_msgSend$adaptiveTextHeight
+ _objc_msgSend$adaptiveTimeHonorsPreferredSalientContentRectangle
+ _objc_msgSend$addRemoteUnlockHandler:
+ _objc_msgSend$animationFence
+ _objc_msgSend$attemptPhoneUnlockWithRemoteDevice
+ _objc_msgSend$attemptUnlock
+ _objc_msgSend$backdropLayer
+ _objc_msgSend$backgroundGlassView
+ _objc_msgSend$bottomComplicationsInsetForCombinedListViewController:
+ _objc_msgSend$bottomInsetForBottomComplications
+ _objc_msgSend$buttonVisibilityChangedTo:
+ _objc_msgSend$buttons
+ _objc_msgSend$complicationsUsingBottomPosition
+ _objc_msgSend$complicationsUsingBottomPositionForCombinedListViewController:
+ _objc_msgSend$constrainsTimeHeight
+ _objc_msgSend$constrainsTimeHeight:
+ _objc_msgSend$containsProperty:
+ _objc_msgSend$copyBackgroundView
+ _objc_msgSend$coverSheetViewControllerDidCancelInlinePasscode:
+ _objc_msgSend$coverSheetViewControllerDidChangeUserPresence:
+ _objc_msgSend$coverSheetViewControllerDidOccludeWallpaper:occluded:
+ _objc_msgSend$coverSheetViewControllerRequestsTranslationToPresentedForExternalLockProvider:animated:
+ _objc_msgSend$dateOfLastBackupWithError:
+ _objc_msgSend$didAddNewSceneHostEnvironment:
+ _objc_msgSend$disableDetectionForReason:monitorType:
+ _objc_msgSend$dismissInterstitialPresentationAnimated:
+ _objc_msgSend$dismissOverlays:animated:
+ _objc_msgSend$dismissableOverlaysOutOf:
+ _objc_msgSend$displayConfiguration
+ _objc_msgSend$effectiveContainerBounds
+ _objc_msgSend$effectiveContentsContainerView
+ _objc_msgSend$effectiveFadeInThreshold
+ _objc_msgSend$effectiveListMaxY
+ _objc_msgSend$enableDetectionForReason:monitorType:
+ _objc_msgSend$event
+ _objc_msgSend$faceState
+ _objc_msgSend$fadeAlpha
+ _objc_msgSend$fadeAnchorY
+ _objc_msgSend$fadeRadiusY
+ _objc_msgSend$fadeWidth
+ _objc_msgSend$fetchFormattedChargeTimeEstimateWithCompletion:
+ _objc_msgSend$findMyAccount
+ _objc_msgSend$frameForElements:
+ _objc_msgSend$handleButtonTap:
+ _objc_msgSend$handleHardwareButtonPressForType:
+ _objc_msgSend$handlePhoneUnlockWithVisionError:
+ _objc_msgSend$handleSignificantUserInteractionOccurred
+ _objc_msgSend$handleWakeSourceIsUserActive
+ _objc_msgSend$hostDelegate
+ _objc_msgSend$iconZoomingView
+ _objc_msgSend$initWithAccount:delegate:eventQueue:error:
+ _objc_msgSend$initWithDescriptor:
+ _objc_msgSend$initWithHostViewController:
+ _objc_msgSend$initWithLockoutController:
+ _objc_msgSend$invalidateContentInsets
+ _objc_msgSend$isContentVisibleAndAppeared
+ _objc_msgSend$isDepthEffectDisabled
+ _objc_msgSend$isEmpty
+ _objc_msgSend$isEnabledForDataclass:
+ _objc_msgSend$isMainDisplay
+ _objc_msgSend$isOnAC
+ _objc_msgSend$isPerformingAlphaAnimation
+ _objc_msgSend$isPhoneUnlockWithVisionSupportedAndEnabled
+ _objc_msgSend$lastAdaptiveTimeTextHeight
+ _objc_msgSend$lastBackupTime
+ _objc_msgSend$mask
+ _objc_msgSend$matchMoveAnimationForPinningToView:
+ _objc_msgSend$maximumAdaptiveTimeTextHeight
+ _objc_msgSend$minimumAdaptiveTimeTextHeight
+ _objc_msgSend$minimumFrameHeight
+ _objc_msgSend$modalFullScreenMetrics
+ _objc_msgSend$notificationDimView
+ _objc_msgSend$notificationDimmingLayer
+ _objc_msgSend$notificationStructuredListViewControllerRequestsEdgeInsetsForOverlayFooterView:forOrientation:
+ _objc_msgSend$observeDefault:onQueue:withBlock:
+ _objc_msgSend$phoneUnlockEnabledAndRequirementsMet
+ _objc_msgSend$preferredSalientContentRectangle
+ _objc_msgSend$presentsAlert
+ _objc_msgSend$prominentDisplayViewController
+ _objc_msgSend$proportionalAdaptiveTime
+ _objc_msgSend$pruis_primaryPosterOffset
+ _objc_msgSend$pruis_primaryPosterScale
+ _objc_msgSend$pruis_setLeadingTopButtonFrame:
+ _objc_msgSend$pruis_setLockPosterComplicationRowHidden:
+ _objc_msgSend$pruis_setLockPosterFloatingLayerInlined:
+ _objc_msgSend$pruis_setLockPosterLiveContentLayerContextID:
+ _objc_msgSend$pruis_setLockPosterLiveContentLayerRenderID:
+ _objc_msgSend$pruis_setLockPosterLiveFloatingLayerContextID:
+ _objc_msgSend$pruis_setLockPosterLiveFloatingLayerRenderID:
+ _objc_msgSend$pruis_setLockPosterOverlayLayerContextID:
+ _objc_msgSend$pruis_setLockPosterOverlayLayerRenderID:
+ _objc_msgSend$pruis_setLockVibrancyConfiguration:
+ _objc_msgSend$pruis_setPreferredSwitcherLayoutMode:
+ _objc_msgSend$pruis_setTitleAdaptiveTextHeight:
+ _objc_msgSend$pruis_setTrailingTopButtonFrame:
+ _objc_msgSend$pruis_switcherContextID
+ _objc_msgSend$pruis_switcherLayoutMode
+ _objc_msgSend$reasons
+ _objc_msgSend$reevaluateAudioCategoriesDisablingVolumeHUDForReason:
+ _objc_msgSend$reevaluatePresentationModeForReason:
+ _objc_msgSend$sensitiveUIEnabled
+ _objc_msgSend$setAlertDismissalHandler:
+ _objc_msgSend$setAllowsHitTesting:
+ _objc_msgSend$setAngle:
+ _objc_msgSend$setAnimationsEnabled:
+ _objc_msgSend$setAppliesX:
+ _objc_msgSend$setAppliesY:
+ _objc_msgSend$setBackgroundGlassView:
+ _objc_msgSend$setComplicationContainerView:
+ _objc_msgSend$setComplicationGridLayoutMetricsProvider:
+ _objc_msgSend$setConstrainsTimeHeight:
+ _objc_msgSend$setContentObscured:
+ _objc_msgSend$setCrossBlurEnd:
+ _objc_msgSend$setCrossBlurStart:
+ _objc_msgSend$setCrossBlursForTransition:
+ _objc_msgSend$setCurvature:
+ _objc_msgSend$setDateStyle:
+ _objc_msgSend$setDefaultValuesForCrossFadeOnTouchUp
+ _objc_msgSend$setDisableActions:
+ _objc_msgSend$setDoesRelativeDateFormatting:
+ _objc_msgSend$setFadeAlpha:
+ _objc_msgSend$setFadeAnchorY:
+ _objc_msgSend$setFadeRadiusY:
+ _objc_msgSend$setFadeWidth:
+ _objc_msgSend$setForceOnlyFadeAnimations:
+ _objc_msgSend$setHasContentAboveCoverSheet:
+ _objc_msgSend$setHasSidebarContents:
+ _objc_msgSend$setHeight:
+ _objc_msgSend$setIsPerformingAlphaAnimation:
+ _objc_msgSend$setLastAdaptiveTimeTextHeight:
+ _objc_msgSend$setMaximumAdaptiveTimeTextHeight:
+ _objc_msgSend$setModalPresentationViewOffset:
+ _objc_msgSend$setNeedsNestedVibrancyEffectView:
+ _objc_msgSend$setPasscodeLockVisible:animated:showBackground:completion:
+ _objc_msgSend$setPasscodeLockVisible:animated:showBackground:forceBiometricPresentation:completion:
+ _objc_msgSend$setPosterHasComplications:
+ _objc_msgSend$setPreferredColorScheme:
+ _objc_msgSend$setRestrictsTouchesOnHostedScene:
+ _objc_msgSend$setShadowColor:
+ _objc_msgSend$setShadowOpacity:
+ _objc_msgSend$setShadowPathIsBounds:
+ _objc_msgSend$setShadowRadius:
+ _objc_msgSend$setShowCompactTime:
+ _objc_msgSend$setShowCompactTime:animated:
+ _objc_msgSend$setTimeStyle:
+ _objc_msgSend$setTimeSupportsStretch:
+ _objc_msgSend$setUseComplicationRenderStyle:
+ _objc_msgSend$setUsesSensitiveUIAppearance:
+ _objc_msgSend$settingsDiff
+ _objc_msgSend$showCompactTime
+ _objc_msgSend$showCompactTime:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$tearDown
+ _objc_msgSend$updateSalientContentRectangle:
+ _objc_msgSend$updateSettings:
+ _objc_msgSend$userPresenceDetectedRecently
+ _objc_msgSend$userPresenceDetectedRecentlyDidChange:
+ _objc_msgSend$wallpaperLegibilityContainerView
+ _objc_msgSend$wallpaperOcclusionPercentage
- -[CSActivityItemContentView .cxx_destruct]
- -[CSActivityItemContentView setSizeProvider:]
- -[CSActivityItemContentView sizeProvider]
- -[CSActivityItemContentView sizeThatFits:]
- -[CSActivityItemViewController .cxx_destruct]
- -[CSActivityItemViewController _backlightLuminanceDidChange]
- -[CSActivityItemViewController _canShowWhileLocked]
- -[CSActivityItemViewController _invalidateRestrictsTouchesAssertion]
- -[CSActivityItemViewController _isContentVisibleAndAppeared]
- -[CSActivityItemViewController _preferredContentSizeDidChangeForChildViewController:]
- -[CSActivityItemViewController _updateAudioCategoriesDisablingVolumeHUDWithReason:]
- -[CSActivityItemViewController _updatePresentationModeWithReason:]
- -[CSActivityItemViewController activityHostTouchRestrictedRects]
- -[CSActivityItemViewController activityHostViewController]
- -[CSActivityItemViewController audioCategoriesDisablingVolumeHUD]
- -[CSActivityItemViewController contentSizeForContentView:]
- -[CSActivityItemViewController dealloc]
- -[CSActivityItemViewController delegate]
- -[CSActivityItemViewController initWithActivityHostViewController:]
- -[CSActivityItemViewController isContentVisible]
- -[CSActivityItemViewController isListAppeared]
- -[CSActivityItemViewController isScreenOn]
- -[CSActivityItemViewController loadView]
- -[CSActivityItemViewController notificationListSupplementaryViewPresentableContentWillBecomeVisible:]
- -[CSActivityItemViewController reevaluateAudioCategoriesDisablingVolumeHUD]
- -[CSActivityItemViewController restrictsTouchesAssertion]
- -[CSActivityItemViewController restrictsTouchesOnHostedScene:]
- -[CSActivityItemViewController sceneHostEnvironmentEntriesForBacklightSession]
- -[CSActivityItemViewController sceneHostEnvironmentObserver]
- -[CSActivityItemViewController setActivityHostViewController:]
- -[CSActivityItemViewController setContentVisible:]
- -[CSActivityItemViewController setDelegate:]
- -[CSActivityItemViewController setListAppeared:]
- -[CSActivityItemViewController setPresentationMode:]
- -[CSActivityItemViewController setRestrictsTouchesAssertion:]
- -[CSActivityItemViewController setSceneHostEnvironmentObserver:]
- -[CSActivityItemViewController setScreenOn:]
- -[CSActivityItemViewController viewDidLoad]
- -[CSActivityItemViewController viewWillLayoutSubviews]
- -[CSActivityManager activityHostViewController:requestsLaunchWithAction:]
- -[CSActivityManager activityHostViewControllerAudioCategoriesDisablingVolumeHUDDidChange:]
- -[CSActivityManager activityHostViewControllerBackgroundTintColorDidChange:]
- -[CSActivityManager activityHostViewControllerBackgroundTintColorDidChange:].cold.1
- -[CSActivityManager activityHostViewControllerHostShouldCancelTouches:]
- -[CSActivityManager activityHostViewControllerSignificantUserInteractionBegan:]
- -[CSActivityManager activityHostViewControllerSignificantUserInteractionEnded:]
- -[CSActivityManager activityHostViewControllerTextColorDidChange:]
- -[CSActivityManager activityHostViewControllerTextColorDidChange:].cold.1
- -[CSActivityManager activityHostViewControllersByActivityIdentifier]
- -[CSActivityManager didAddNewSceneHostEnvironment]
- -[CSActivityManager setActivityHostViewControllersByActivityIdentifier:]
- -[CSCombinedListViewController _allowsNotificationListTopInset]
- -[CSCombinedListViewController _allowsSeparateAdjunctList]
- -[CSCombinedListViewController _integratesAdjunctListIntoFullList]
- -[CSCombinedListViewController _snapScrollView:toAcceptableOffsetAnimated:]
- -[CSCombinedListViewController _snapToAcceptableOffsetForScrollView:]
- -[CSCombinedListViewController activityItemViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:]
- -[CSCombinedListViewController interpretsViewAsAdjunctContent:]
- -[CSCombinedListViewController scrollViewDidEndDecelerating:]
- -[CSCombinedListViewController scrollViewDidEndDragging:willDecelerate:]
- -[CSCombinedListViewController scrollViewDidEndScrollingAnimation:]
- -[CSCombinedListViewController settleContentOffset]
- -[CSCoverSheetViewController __currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:]
- -[CSCoverSheetViewController __currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:].cold.1
- -[CSCoverSheetViewController __currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:].cold.2
- -[CSCoverSheetViewController __currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:].cold.3
- -[CSCoverSheetViewController _updateModalPresentationControllerVisibility]
- -[CSCoverSheetViewController attemptPhoneUnlockWithWatch]
- -[CSCoverSheetViewController didDetectFaceRequirementsForPAU]
- -[CSCoverSheetViewController dismissOverlaysAnimated:]
- -[CSCoverSheetViewController isDepthEffectEnabled]
- -[CSCoverSheetViewController phoneUnlockWithWatchEnabled]
- -[CSCoverSheetViewController setPasscodeLockVisible:animated:forceBiometricPresentation:completion:]
- -[CSCoverSheetViewController updateFont:vibrancyConfiguration:numberingSystem:contentStyle:]
- -[CSDashBoardRemoteContentSettings hostsInlineContentNativelyInNotificationList]
- -[CSDashBoardRemoteContentSettings includesDateTimeStandinInAdjunctList]
- -[CSDashBoardRemoteContentSettings setHostsInlineContentNativelyInNotificationList:]
- -[CSDashBoardRemoteContentSettings setIncludesDateTimeStandinInAdjunctList:]
- -[CSDashBoardRemoteContentSettings shouldHostContentInNotificationList]
- -[CSDateViewComponent _setValueForInternalPageIndex:hidesTime:]
- -[CSNotificationAdjunctListViewController _hostsInlineContentInAdjunctList]
- -[CSNotificationAdjunctListViewController _hostsTimeInAdjunctList]
- -[CSPosterSwitcherViewController sceneHandle:didUpdateClientSettingsWithDiff:transitionContext:]
- -[CSPosterSwitcherViewController sceneHandle:didUpdateClientSettingsWithDiff:transitionContext:].cold.1
- -[CSQuickActionsViewController _deviceBlockStateDidChangeNotification:]
- -[CSQuickActionsViewController _featureLockStateDidChangeNotification:]
- -[CSQuickActionsViewController _isFlashlightOn]
- -[CSQuickActionsViewController _setupFlashlightControllerIfNecessary]
- -[CSQuickActionsViewController _setupFlashlightController]
- -[CSQuickActionsViewController _tearDownFlashlightIfOff]
- -[CSQuickActionsViewController _tearDownFlashlight]
- -[CSQuickActionsViewController _updateFlashlightAction:]
- -[CSUserPresenceMonitor _updateFaceDetectionState]
- -[CSUserPresenceMonitor disableDetectionForReason:]
- -[CSUserPresenceMonitor enableDetectionForReason:]
- GCC_except_table112
- GCC_except_table192
- GCC_except_table215
- GCC_except_table23
- GCC_except_table290
- GCC_except_table36
- GCC_except_table422
- GCC_except_table46
- GCC_except_table479
- GCC_except_table48
- GCC_except_table499
- GCC_except_table505
- GCC_except_table582
- GCC_except_table62
- GCC_except_table632
- GCC_except_table642
- GCC_except_table644
- GCC_except_table653
- GCC_except_table662
- GCC_except_table672
- GCC_except_table75
- GCC_except_table78
- _CGAffineTransformTranslate
- _NSStringFromPRUISwitcherLayoutMode
- _OBJC_CLASS_$_CSActivityItemContentView
- _OBJC_CLASS_$_CSActivityItemViewController
- _OBJC_CLASS_$_PRPosterContentVibrantMonochromeStyle
- _OBJC_IVAR_$_CSActivityItemContentView._sizeProvider
- _OBJC_IVAR_$_CSActivityItemViewController._activityHostViewController
- _OBJC_IVAR_$_CSActivityItemViewController._audioCategoriesDisablingVolumeHUD
- _OBJC_IVAR_$_CSActivityItemViewController._contentVisible
- _OBJC_IVAR_$_CSActivityItemViewController._delegate
- _OBJC_IVAR_$_CSActivityItemViewController._listAppeared
- _OBJC_IVAR_$_CSActivityItemViewController._restrictsTouchesAssertion
- _OBJC_IVAR_$_CSActivityItemViewController._sceneHostEnvironmentObserver
- _OBJC_IVAR_$_CSActivityItemViewController._screenOn
- _OBJC_IVAR_$_CSActivityManager._activityHostViewControllersByActivityIdentifier
- _OBJC_IVAR_$_CSDashBoardRemoteContentSettings._hostsInlineContentNativelyInNotificationList
- _OBJC_IVAR_$_CSDashBoardRemoteContentSettings._includesDateTimeStandinInAdjunctList
- _OBJC_IVAR_$_CSQuickActionsButton._iconZoomBackgroundEffectView
- _OBJC_IVAR_$_CSQuickActionsViewController._flashlight
- _OBJC_METACLASS_$_CSActivityItemContentView
- _OBJC_METACLASS_$_CSActivityItemViewController
- _PRUISwitcherLayoutTransitionAnimationSettings
- _SBRingerButtonDownNotification
- __OBJC_$_INSTANCE_METHODS_CSActivityItemContentView
- __OBJC_$_INSTANCE_METHODS_CSActivityItemViewController
- __OBJC_$_INSTANCE_VARIABLES_CSActivityItemContentView
- __OBJC_$_INSTANCE_VARIABLES_CSActivityItemViewController
- __OBJC_$_PROP_LIST_CSActivityItemContentView
- __OBJC_$_PROP_LIST_CSActivityItemViewController
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivityItemContentViewSizeProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivityItemViewControllerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSListItemSceneHostEnvironmentObserving
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivityItemContentViewSizeProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivityItemViewControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSListItemSceneHostEnvironmentObserving
- __OBJC_$_PROTOCOL_REFS_CSActivityItemContentViewSizeProviding
- __OBJC_$_PROTOCOL_REFS_CSActivityItemViewControllerDelegate
- __OBJC_$_PROTOCOL_REFS_CSListItemSceneHostEnvironmentObserving
- __OBJC_CLASS_PROTOCOLS_$_CSActivityItemViewController
- __OBJC_CLASS_RO_$_CSActivityItemContentView
- __OBJC_CLASS_RO_$_CSActivityItemViewController
- __OBJC_LABEL_PROTOCOL_$_CSActivityItemContentViewSizeProviding
- __OBJC_LABEL_PROTOCOL_$_CSActivityItemViewControllerDelegate
- __OBJC_LABEL_PROTOCOL_$_CSListItemSceneHostEnvironmentObserving
- __OBJC_METACLASS_RO_$_CSActivityItemContentView
- __OBJC_METACLASS_RO_$_CSActivityItemViewController
- __OBJC_PROTOCOL_$_CSActivityItemContentViewSizeProviding
- __OBJC_PROTOCOL_$_CSActivityItemViewControllerDelegate
- __OBJC_PROTOCOL_$_CSListItemSceneHostEnvironmentObserving
- ___100-[CSCoverSheetViewController setPasscodeLockVisible:animated:forceBiometricPresentation:completion:]_block_invoke
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.736
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.737
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.738
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.162
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.166
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.175
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.169
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.178
- ___43-[CSCombinedListViewController viewDidLoad]_block_invoke_4
- ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.702
- ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.609
- ___52-[CSActivityItemViewController setPresentationMode:]_block_invoke
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.409
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.410
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.418
- ___58-[CSActivityManager _addActivityListItemForContentUpdate:]_block_invoke.50
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.672
- ___63-[CSCoverSheetViewController _showChargingSubtitleWithTimeout:]_block_invoke_2
- ___64-[CSNotificationAdjunctListViewController _removeItem:animated:]_block_invoke_3
- ___64-[CSNotificationAdjunctListViewController _removeItem:animated:]_block_invoke_4
- ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.445
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.713
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.714
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.721
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.719
- ___73-[CSActivityManager activityHostViewController:requestsLaunchWithAction:]_block_invoke
- ___74-[CSWidgetGridViewController _updateComplicationPresentationState:reason:]_block_invoke.49
- ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.538
- ___81-[CSNotificationAdjunctListViewController _insertItem:atPreferredIndex:animated:]_block_invoke.36
- ___81-[CSNotificationAdjunctListViewController _insertItem:atPreferredIndex:animated:]_block_invoke_2
- ___81-[CSPresentationViewController _updateContentViewControllersAnimated:completion:]_block_invoke.82
- ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.539
- ___96-[CSPosterSwitcherViewController sceneHandle:didUpdateClientSettingsWithDiff:transitionContext:]_block_invoke
- ___98-[CSCoverSheetViewController activateCameraWithHostableEntity:animated:sendingActions:completion:]_block_invoke.121
- ___block_descriptor_40_e8_32w_e63_v24?0"ACUISActivityHostViewController"8"UITraitCollection"16lw32l8
- ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_72_e8_32s_e43_v16?0"UIMutableApplicationSceneSettings"8ls32l8
- ___block_descriptor_73_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_73_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_literal_global.104
- ___block_literal_global.112
- ___block_literal_global.168
- ___block_literal_global.197
- ___block_literal_global.2129
- ___block_literal_global.236
- ___block_literal_global.241
- ___block_literal_global.246
- ___block_literal_global.293
- ___block_literal_global.345
- ___block_literal_global.347
- ___block_literal_global.35
- ___block_literal_global.361
- ___block_literal_global.366
- ___block_literal_global.371
- ___block_literal_global.376
- ___block_literal_global.381
- ___block_literal_global.386
- ___block_literal_global.731
- ___block_literal_global.733
- ___block_literal_global.79
- _objc_msgSend$__currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:
- _objc_msgSend$_adjunctListViewSize
- _objc_msgSend$_allowsNotificationListTopInset
- _objc_msgSend$_allowsSeparateAdjunctList
- _objc_msgSend$_hostsInlineContentInAdjunctList
- _objc_msgSend$_hostsTimeInAdjunctList
- _objc_msgSend$_integratesAdjunctListIntoFullList
- _objc_msgSend$_isContentVisibleAndAppeared
- _objc_msgSend$_setupFlashlightController
- _objc_msgSend$_setupFlashlightControllerIfNecessary
- _objc_msgSend$_snapScrollView:toAcceptableOffsetAnimated:
- _objc_msgSend$_snapToAcceptableOffsetForScrollView:
- _objc_msgSend$_tearDownFlashlight
- _objc_msgSend$_tearDownFlashlightIfOff
- _objc_msgSend$_updateFaceDetectionState
- _objc_msgSend$_updateFlashlightAction:
- _objc_msgSend$_updateModalPresentationControllerVisibility
- _objc_msgSend$_updatePresentationModeWithReason:
- _objc_msgSend$activityHostViewControllerBackgroundTintColorDidChange:
- _objc_msgSend$activityItemViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:
- _objc_msgSend$attemptPhoneUnlockWithWatch
- _objc_msgSend$backgroundEffectView
- _objc_msgSend$clearAllStyling
- _objc_msgSend$contentLayoutGuide
- _objc_msgSend$copyBackgroundVisualEffectView
- _objc_msgSend$defaultRestingOffsetExcludingAdjunct
- _objc_msgSend$didDetectFaceRequirementsForPAU
- _objc_msgSend$disableDetectionForReason:
- _objc_msgSend$dismissOverlaysAnimated:
- _objc_msgSend$dismissableOverlays
- _objc_msgSend$enableDetectionForReason:
- _objc_msgSend$frameLayoutGuide
- _objc_msgSend$hostsInlineContentNativelyInNotificationList
- _objc_msgSend$includesDateTimeStandinInAdjunctList
- _objc_msgSend$initWithActivityHostViewController:
- _objc_msgSend$insertArrangedSubview:atIndex:
- _objc_msgSend$interpretsViewAsAdjunctContent:
- _objc_msgSend$isContentVisible
- _objc_msgSend$isDepthEffectEnabled
- _objc_msgSend$isListAppeared
- _objc_msgSend$phoneUnlockWithWatchEnabled
- _objc_msgSend$prui_primaryPosterOffset
- _objc_msgSend$prui_primaryPosterScale
- _objc_msgSend$prui_setLeadingTopButtonFrame:
- _objc_msgSend$prui_setLockPosterComplicationRowHidden:
- _objc_msgSend$prui_setLockPosterFloatingLayerInlined:
- _objc_msgSend$prui_setLockPosterLiveContentLayerContextID:
- _objc_msgSend$prui_setLockPosterLiveContentLayerRenderID:
- _objc_msgSend$prui_setLockPosterLiveFloatingLayerContextID:
- _objc_msgSend$prui_setLockPosterLiveFloatingLayerRenderID:
- _objc_msgSend$prui_setLockPosterOverlayLayerContextID:
- _objc_msgSend$prui_setLockPosterOverlayLayerRenderID:
- _objc_msgSend$prui_setLockVibrancyConfiguration:
- _objc_msgSend$prui_setPreferredSwitcherLayoutMode:
- _objc_msgSend$prui_setTrailingTopButtonFrame:
- _objc_msgSend$prui_switcherContextID
- _objc_msgSend$prui_switcherLayoutMode
- _objc_msgSend$reevaluateAudioCategoriesDisablingVolumeHUD
- _objc_msgSend$restrictsTouchesOnHostedScene:
- _objc_msgSend$setContentOffset:animated:
- _objc_msgSend$setContentVisible:
- _objc_msgSend$setFlashlightController:
- _objc_msgSend$setHostsInlineContentNativelyInNotificationList:
- _objc_msgSend$setIncludesDateTimeStandinInAdjunctList:
- _objc_msgSend$setLiftToWakeGestureDetectedSinceScreenOn:
- _objc_msgSend$setPasscodeLockVisible:animated:forceBiometricPresentation:completion:
- _objc_msgSend$setSignificantUserInteractionOccuredSinceScreenOn:
- _objc_msgSend$setSizeProvider:
- _objc_msgSend$setWakeSourceIsUserAction:
- _objc_msgSend$settleContentOffset
- _objc_msgSend$shouldHostContentInNotificationList
- _objc_msgSend$sizeProvider
CStrings:
+ "!#"
+ "%"
+ "%@: %@"
+ "%{public}@ - Wallpaper is %@, assertions taken: %@"
+ "%{public}@ notification glassContentInterfaceStyle set to %ld"
+ "/System/Library/PrivateFrameworks/ActivityProgressKit.framework/ActivityProgressKit"
+ "2B"
+ "6"
+ "@\"<CSActivityContentViewDelegate>\""
+ "@\"<CSActivityViewControllerDelegate>\""
+ "@\"<CSActivityViewControllerHostDelegate>\""
+ "@\"<CSMainPageComplicationsMetricsProvider>\""
+ "@\"<CSSceneHostEnvironmentObserving>\""
+ "@\"ACActivityDescriptor\"24@0:8@\"CSActivityContentView\"16"
+ "@\"CASDFElementLayer\""
+ "@\"CASDFLayer\""
+ "@\"CSCoverSheetSDFBackdropView\""
+ "@\"CSCoverSheetSDFView\""
+ "@\"CSHostedEntityViewController\"16@0:8"
+ "@\"CSNotificationDimView\""
+ "@\"NSSet\"32@0:8@\"FBScene\"16@\"NSSet\"24"
+ "@\"SBUIPhoneUnlockWithRemoteDeviceCoordinator\""
+ "@\"SBUIPhoneUnlockWithVisionController\""
+ "@80@0:8^Q16^Q24^@32^@40^@48^@56^@64^@72"
+ "AC*** - progress: %f"
+ "APKActivityProgressEventAction"
+ "Account is nil, can't fetch backup date!"
+ "B24@0:8@\"<SBFHomeAffordanceInteraction>\"16"
+ "B24@0:8@\"CSCombinedListViewController\"16"
+ "B32@0:8@\"ACUISActivityHostViewController\"16@\"BSAction\"24"
+ "B32@0:8@\"CSActivityViewController\"16@\"BSAction\"24"
+ "Background content did get obscured: %{BOOL}u"
+ "BackgroundContentAdded"
+ "Backup is not enabled on this account!"
+ "BatteryAnalysis"
+ "CSActivityContentView"
+ "CSActivityContentViewDelegate"
+ "CSActivityFullScreenViewController"
+ "CSActivityListItemViewController"
+ "CSActivityViewController"
+ "CSActivityViewControllerDelegate"
+ "CSActivityViewControllerHostDelegate"
+ "CSCoverSheetSDFBackdropView"
+ "CSCoverSheetSDFView"
+ "CSCoverSheetViewBackgroundContentViewMatchMoveAnimation"
+ "CSHostableEntityContentContaining"
+ "CSMainPageComplicationsMetricsProvider"
+ "CSNotificationDimView"
+ "CSNotificationDimmingLayerComponent"
+ "CSSceneHostEnvironmentObserving"
+ "Cross Blur"
+ "Cross Blur End"
+ "Cross Blur Start"
+ "Cross Blurs Wallpaper"
+ "Error initializing MBManager: %@, for user: %@"
+ "FBSceneObserver"
+ "InspectorGadget"
+ "LOCKSCREEN_LAST_BACKUP_TITLE"
+ "Last backup string: %@"
+ "Last successful backup: %@"
+ "MBManagerDelegate"
+ "No backup found!"
+ "NotificationDimmingLayer"
+ "NotificationList"
+ "Obtaining the last backup date"
+ "PosterAdaptiveTimeModeUpdate"
+ "PosterSalientContentRectangleUpdate"
+ "Prism"
+ "Q24@0:8Q16"
+ "SBDashBoardLandscapeDateComponentIdentifier"
+ "SBUIPhoneUnlockWithVisionControllerObserver"
+ "SUTU"
+ "Salvador"
+ "ScreenOnChanged"
+ "T@\"<BSInvalidatable>\",&,N,V_backgroundContentDidOccludeWallpaperAssertion"
+ "T@\"<BSInvalidatable>\",&,N,V_notificationListDidOccludeWallpaperAssertion"
+ "T@\"<CSActivityContentViewDelegate>\",W,N,V_delegate"
+ "T@\"<CSActivityViewControllerDelegate>\",W,N,V_delegate"
+ "T@\"<CSActivityViewControllerHostDelegate>\",W,N,V_hostDelegate"
+ "T@\"<CSMainPageComplicationsMetricsProvider>\",W,N,V_complicationGridLayoutMetricsProvider"
+ "T@\"<CSSceneHostEnvironmentObserving>\",W,N,V_sceneHostEnvironmentObserver"
+ "T@\"<SBFLockOutStatusProvider>\",&,N,V_lockoutController"
+ "T@\"ACAccount\",&,N,V_account"
+ "T@\"ACAccount\",&,N,V_findMyAccount"
+ "T@\"ACUISActivityHostViewController\",R,N,V_hostViewController"
+ "T@\"BSCompoundAssertion\",&,N,V__wallpaperOccludedAssertions"
+ "T@\"CABackdropLayer\",&,N,V_backdropLayer"
+ "T@\"CABackdropLayer\",R,N,V_backdropLayer"
+ "T@\"CALayer\",&,N,V_shadowMaskLayer"
+ "T@\"CASDFElementLayer\",R,N,V_aberrationElementLayer"
+ "T@\"CASDFElementLayer\",R,N,V_displacementElementLayer"
+ "T@\"CASDFLayer\",R,N,V_aberrationLayer"
+ "T@\"CASDFLayer\",R,N,V_displacementLayer"
+ "T@\"CSCoverSheetSDFBackdropView\",R,N,V_backdropView"
+ "T@\"CSCoverSheetSDFView\",&,N,V_backgroundGlassView"
+ "T@\"CSHostedEntityViewController\",R,N"
+ "T@\"CSNotificationDimView\",&,N,V_notificationDimView"
+ "T@\"NSMutableDictionary\",&,N,V_activityViewControllersByActivityIdentifier"
+ "T@\"UIView\",&,N,V_complicationContainerView"
+ "T@\"UIView\",R,N,V_wallpaperLegibilityContainerView"
+ "T@\"UIView<SBSwitcherIconZooming>\",?,R,N"
+ "TB,N,GisContentObscured,S_setContentObscured:,V_contentObscured"
+ "TB,N,GisContentVisibleAndAppeared,V_contentVisibleAndAppeared"
+ "TB,N,GisDepthEffectDisabled,V_depthEffectDisabled"
+ "TB,N,V_adaptiveTimeHonorsPreferredSalientContentRectangle"
+ "TB,N,V_complicationContainerUsesBottomPosition"
+ "TB,N,V_crossBlursForTransition"
+ "TB,N,V_isPerformingAlphaAnimation"
+ "TB,N,V_needsNestedVibrancyEffectView"
+ "TB,N,V_usesSensitiveUIAppearance"
+ "TB,R,N,V_userPresenceDetectedRecently"
+ "Td,N,V_crossBlurEnd"
+ "Td,N,V_crossBlurStart"
+ "Td,N,V_fadeAlpha"
+ "Td,N,V_fadeAnchorY"
+ "Td,N,V_fadeRadiusY"
+ "Td,N,V_fadeWidth"
+ "Td,N,V_lastAdaptiveTimeTextHeight"
+ "Td,N,V_modalPresentationViewOffset"
+ "Td,R,N,V_effectiveFadeRadiusY"
+ "Td,R,N,V_screenScale"
+ "Td,V_wallpaperOcclusionPercentage"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_posterPreferredSalientContentRectangle"
+ "ViewDidDisappear"
+ "ViewWillAppear"
+ "Wallpaper Occlusion Percentage"
+ "WallpaperOccludedByContent"
+ "Will set background content obscured... isModalPresented: %{BOOL}u, hasContentAboveCoverSheet: %{BOOL}u"
+ "[CSViewController] Cancel button pressed for interstitial"
+ "[User Presence Monitor] No user attention or face out of view"
+ "__currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:backgroundContentAppearance:"
+ "__wallpaperOccludedAssertions"
+ "_aberrationElementLayer"
+ "_aberrationLayer"
+ "_account"
+ "_account is: %@, apple id: %@"
+ "_actionButtonPressed:"
+ "_activityViewControllersByActivityIdentifier"
+ "_adaptiveTimeHonorsPreferredSalientContentRectangle"
+ "_adaptiveTimeMaxYFromConfigurationAndPosterPreferences"
+ "_addContentsContainerView"
+ "_addNotificationDimView"
+ "_addWallpaperLegibilityContainerView"
+ "_animateByRetargetingAnimations:completion:"
+ "_animateUsingSpringInteractive:animations:completion:"
+ "_backdropLayer"
+ "_backgroundContentDidOccludeWallpaperAssertion"
+ "_backgroundGlassView"
+ "_complicationContainerUsesBottomPosition"
+ "_complicationContainerView"
+ "_complicationGridLayoutMetricsProvider"
+ "_configureFilter"
+ "_configureShadowMask"
+ "_contentObscured"
+ "_contentVisibleAndAppeared"
+ "_contentsContainerView"
+ "_crossBlurEnd"
+ "_crossBlurStart"
+ "_crossBlursForTransition"
+ "_displacementElementLayer"
+ "_displacementLayer"
+ "_edgeInsetsForUnsupportedQuickActionsForOrientation:"
+ "_effectiveContentsContainerView"
+ "_effectiveFadeRadiusY"
+ "_effectivePreferredSalientContentRectangle"
+ "_fadeAlpha"
+ "_fadeAnchorY"
+ "_fadeRadiusY"
+ "_fadeWidth"
+ "_iconZoomBackgroundView"
+ "_isContentVisible"
+ "_isModalPresented"
+ "_isPerformingAlphaAnimation"
+ "_lastAdaptiveTimeTextHeight"
+ "_layoutComplicationContainerView"
+ "_layoutContentContainerView"
+ "_layoutGlassEffectView"
+ "_layoutLayer:inBounds:"
+ "_layoutNotificationDimView"
+ "_layoutShadowMask"
+ "_layoutWallpaperLegibilityContainerView"
+ "_lockoutController"
+ "_modalPresentationViewOffset"
+ "_notificationDimView"
+ "_notificationDimmingLayerComponent"
+ "_notificationListDidOccludeWallpaperAssertion"
+ "_performAlphaAnimationToAlpha:"
+ "_phoneUnlockWithRemoteDeviceCoordinator"
+ "_phoneUnlockWithVisionController"
+ "_posterPersistedTimeMaxY"
+ "_posterPreferredSalientContentRectangle"
+ "_posterPreferredTimeMaxYLandscape"
+ "_posterPreferredTimeMaxYPortrait"
+ "_presentationModeForActivityPresentationMode:"
+ "_presentationModeForHostedEntityContentMode:"
+ "_reevaluateContentObscured"
+ "_sceneType"
+ "_screenScale"
+ "_setContentObscured:"
+ "_setPresentationMode:"
+ "_setUserPresenceDetectedRecently:"
+ "_setupAberrationLayer"
+ "_setupDisplacementLayer"
+ "_setupIfNecessary"
+ "_shadowMaskLayer"
+ "_shouldAllowBottomGridPosition"
+ "_shouldAllowGlassCoverSheet"
+ "_showCompactTime"
+ "_synchronizeDrawingWithFence:"
+ "_updateAdaptiveTimeTextHeightForSceneSettings:"
+ "_updateBackgroundGlassView"
+ "_updateChargingSubtitleWithString:timeout:"
+ "_updateComplicationContainerPosition"
+ "_updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:"
+ "_updateFaceDetectionStateForMonitorType:"
+ "_updateForSensitiveUI"
+ "_updateGlassLayerFilterValues"
+ "_updateModalPresentationControllerVisibility:"
+ "_updateNotificationDimmingLayer"
+ "_userPresenceDetectedRecently"
+ "_usesSensitiveUIAppearance"
+ "_visiblityForCSActivityVisibilty:"
+ "_wallpaperLegibilityContainerView"
+ "_wallpaperOccludedAssertions"
+ "_wallpaperOcclusionPercentage"
+ "aberration"
+ "aberrationElementLayer"
+ "aberrationLayer"
+ "account"
+ "activityDescriptorForContentView:"
+ "activityHostViewController:didReceiveAction:"
+ "activitySceneType"
+ "activityViewController:didReceiveAction:"
+ "activityViewController:requestsLaunchWithAction:"
+ "activityViewControllerAudioCategoriesDisablingVolumeHUDDidChange:"
+ "activityViewControllerBackgroundTintColorDidChange:"
+ "activityViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:"
+ "activityViewControllerHostShouldCancelTouches:"
+ "activityViewControllerSignificantUserInteractionBegan:"
+ "activityViewControllerSignificantUserInteractionEnded:"
+ "activityViewControllerTextColorDidChange:"
+ "activityViewControllersByActivityIdentifier"
+ "adaptiveTextHeight"
+ "adaptiveTimeHonorsPreferredSalientContentRectangle"
+ "addRemoteUnlockHandler:"
+ "animationFence"
+ "attemptPhoneUnlockWithRemoteDevice"
+ "attemptUnlock"
+ "backdropLayer"
+ "backgroundContentDidOccludeWallpaperAssertion"
+ "backgroundGlassView"
+ "bottomComplicationsInsetForCombinedListViewController:"
+ "bottomInsetForBottomComplications"
+ "buttonVisibilityChangedTo:"
+ "cleanupInterstitialWhileOffScreen"
+ "complicationContainerUsesBottomPosition"
+ "complicationContainerView"
+ "complicationGridLayoutMetricsProvider"
+ "complicationsUsingBottomPosition"
+ "complicationsUsingBottomPositionForCombinedListViewController:"
+ "constrainsTimeHeight"
+ "constrainsTimeHeight:"
+ "containsProperty:"
+ "contentObscured"
+ "contentVisibleAndAppeared"
+ "copyBackgroundView"
+ "coverSheetViewControllerDidCancelInlinePasscode:"
+ "coverSheetViewControllerDidChangeUserPresence:"
+ "coverSheetViewControllerDidOccludeWallpaper:occluded:"
+ "coverSheetViewControllerRequestsTranslationToPresentedForExternalLockProvider:animated:"
+ "crossBlurEnd"
+ "crossBlurStart"
+ "crossBlursForTransition"
+ "crossBlursForTransition == YES"
+ "d24@0:8@\"CSCombinedListViewController\"16"
+ "dateOfLastBackupWithError:"
+ "didAddNewSceneHostEnvironment:"
+ "differentWallpaperInitialTransitionSettings.crossBlurEnd"
+ "differentWallpaperInitialTransitionSettings.crossBlursForTransition"
+ "differentWallpaperInitialTransitionSettings.darkensContent"
+ "differentWallpaperInitialTransitionSettings.fadesCoverSheetContent"
+ "differentWallpaperInitialTransitionSettings.floatingLayerAsWallpaperOverlay"
+ "differentWallpaperInitialTransitionSettings.scaleWallpaper"
+ "differentWallpaperSubsequentTransitionSettings.crossBlurEnd"
+ "differentWallpaperSubsequentTransitionSettings.crossBlursForTransition"
+ "disableDetectionForReason:monitorType:"
+ "disableRecentUserPresenceDetectionForReason:"
+ "dismissInterstitialPresentationAnimated:"
+ "dismissInterstitialPresentationAnimated: called with SUTU disabled, ignoring..."
+ "dismissOverlays:animated:"
+ "dismissableOverlaysOutOf:"
+ "displacement"
+ "displacementElementLayer"
+ "displacementLayer"
+ "displayConfiguration"
+ "effectiveContainerBounds"
+ "effectiveContentsContainerView"
+ "effectiveFadeInThreshold"
+ "effectiveFadeRadiusY"
+ "effectiveListMaxY"
+ "enableDetectionForReason:monitorType:"
+ "enableRecentUserPresenceDetectionForReason:"
+ "endCoverSheetTransition"
+ "event"
+ "faceState"
+ "fadeAlpha"
+ "fadeAnchorY"
+ "fadeRadiusY"
+ "fadeWidth"
+ "fetchFormattedChargeTimeEstimateWithCompletion:"
+ "filters.aberration.inputAmount"
+ "filters.displacement.inputAmount"
+ "findMyAccount"
+ "frameForElements:"
+ "handleButtonTap:"
+ "handleHardwareButtonPressForType:"
+ "handlePhoneUnlockWithVisionError:"
+ "handleSignificantUserInteractionOccurred"
+ "handleWakeSourceIsUserActive"
+ "homeAffordanceInteraction:didRecognizeTouchThatShouldUnhideViewImmediately:"
+ "homeAffordanceInteractionAllowsUserInteraction:"
+ "homeAffordanceInteractionDidRecognizeSingleClick:"
+ "hostedEntityViewController"
+ "iconZoomingView"
+ "iconZoomingViewForActivityIdentifier:"
+ "init(coder:) has not been implemented"
+ "initWithAccount:delegate:eventQueue:error:"
+ "initWithCoder:"
+ "initWithDescriptor:"
+ "initWithDescriptor:sceneType:"
+ "initWithHostViewController:"
+ "initWithLockoutController:"
+ "initWithQuickActionControlIdentity:instance:delegate:prewarmer:"
+ "inputSourceSublayerName"
+ "invalidateContentInsets"
+ "isContentObscured"
+ "isContentVisibleAndAppeared"
+ "isDepthEffectDisabled"
+ "isEmpty"
+ "isEnabledForDataclass:"
+ "isMainDisplay"
+ "isOnAC"
+ "isPerformingAlphaAnimation"
+ "isPhoneUnlockWithVisionSupportedAndEnabled"
+ "isUserPresenceDetectionAllowed"
+ "lastAdaptiveTimeTextHeight"
+ "lastBackupTime"
+ "lockoutController"
+ "manager:didFailBackupWithError:"
+ "manager:didFailRestoreForPath:withError:"
+ "manager:didFailRestoreWithError:"
+ "manager:didFailScanWithError:"
+ "manager:didFailVerificationWithError:"
+ "manager:didFinishDeviceTransferKeychainTransfer:"
+ "manager:didFinishDeviceTransferWithError:"
+ "manager:didFinishRestoreForPath:"
+ "manager:didScanBundleWithID:bytesUsed:"
+ "manager:didScanDomainWithName:forBundleID:bytesUsed:"
+ "manager:didScanFiles:forDomainWithName:bundleID:"
+ "manager:didSetBackupEnabled:"
+ "manager:didUpdateDeviceTransferConnectionInfo:"
+ "manager:didUpdateDeviceTransferProgress:"
+ "manager:didUpdateProgress:estimatedTimeRemaining:"
+ "manager:didUpdateProgress:estimatedTimeRemaining:bytesRemaining:state:"
+ "managerDidCancelRestore:"
+ "managerDidFinishBackup:"
+ "managerDidFinishRestore:"
+ "managerDidFinishScan:"
+ "managerDidFinishScan:bytesUsed:"
+ "managerDidFinishVerification:"
+ "managerDidLoseConnectionToService:"
+ "managerDidUpdateBackgroundRestoreProgress:"
+ "mask"
+ "matchMoveAnimationForPinningToView:"
+ "maximumAdaptiveTimeTextHeight"
+ "minimumAdaptiveTimeTextHeight"
+ "minimumFrameHeight"
+ "modalFullScreenMetrics"
+ "modalPresentationViewOffset"
+ "needsNestedVibrancyEffectView"
+ "notificationDimView"
+ "notificationDimViewAlpha"
+ "notificationDimmingLayer"
+ "notificationListDidOccludeWallpaperAssertion"
+ "notificationStructuredListViewController:glassContentInterfaceStyleOverridenToUserInterfaceStyle:"
+ "notificationStructuredListViewController:requestsUpdateNotificationDimViewFadeRadiusY:"
+ "observeDefault:onQueue:withBlock:"
+ "occluded"
+ "overAppTransitionSettings.crossBlurEnd"
+ "overAppTransitionSettings.crossBlursForTransition"
+ "performInterstitialPresentationAnimated:"
+ "performInterstitialPresentationAnimated: called with SUTU disabled, ignoring..."
+ "phoneUnlockEnabledAndRequirementsMet"
+ "phoneUnlockWithVisionController:attemptFailedWithError:"
+ "phoneUnlockWithVisionControllerAttemptSucceeded:"
+ "posterPreferredSalientContentRectangle"
+ "preferredSalientContentRectangle"
+ "presentsAlert"
+ "prominentDisplayViewController"
+ "proportionalAdaptiveTime"
+ "pruis_primaryPosterOffset"
+ "pruis_primaryPosterScale"
+ "pruis_setLeadingTopButtonFrame:"
+ "pruis_setLockPosterComplicationRowHidden:"
+ "pruis_setLockPosterFloatingLayerInlined:"
+ "pruis_setLockPosterLiveContentLayerContextID:"
+ "pruis_setLockPosterLiveContentLayerRenderID:"
+ "pruis_setLockPosterLiveFloatingLayerContextID:"
+ "pruis_setLockPosterLiveFloatingLayerRenderID:"
+ "pruis_setLockPosterOverlayLayerContextID:"
+ "pruis_setLockPosterOverlayLayerRenderID:"
+ "pruis_setLockVibrancyConfiguration:"
+ "pruis_setPreferredSwitcherLayoutMode:"
+ "pruis_setTitleAdaptiveTextHeight:"
+ "pruis_setTrailingTopButtonFrame:"
+ "pruis_switcherContextID"
+ "pruis_switcherLayoutMode"
+ "reasons"
+ "reevaluateAudioCategoriesDisablingVolumeHUDForReason:"
+ "reevaluatePresentationModeForReason:"
+ "sameWallpaperInitialTransitionSettings.blursPanel"
+ "sameWallpaperInitialTransitionSettings.crossBlurEnd"
+ "sameWallpaperInitialTransitionSettings.crossBlursForTransition"
+ "sameWallpaperInitialTransitionSettings.darkensContent"
+ "sameWallpaperInitialTransitionSettings.fadePanelWallpaper"
+ "sameWallpaperInitialTransitionSettings.fadesContent"
+ "sameWallpaperInitialTransitionSettings.fadesCoverSheetContent"
+ "sameWallpaperInitialTransitionSettings.orientPanelWallpaper"
+ "sameWallpaperInitialTransitionSettings.panelWallpaper"
+ "sameWallpaperInitialTransitionSettings.scaleWallpaper"
+ "sameWallpaperInitialTransitionSettings.trackingWallpaper"
+ "sameWallpaperSubsequentTransitionSettings.crossBlurEnd"
+ "sameWallpaperSubsequentTransitionSettings.crossBlursForTransition"
+ "sameWallpaperSubsequentTransitionSettings.floatingLayerAsWallpaperOverlay"
+ "scene:clientDidConnect:"
+ "scene:didApplyUpdateWithContext:"
+ "scene:didCompleteUpdateWithContext:error:"
+ "scene:didPrepareUpdateWithContext:"
+ "scene:didUpdateClientSettings:"
+ "scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:"
+ "scene:didUpdateSettings:"
+ "scene:handleActions:"
+ "sceneContentStateDidChange:"
+ "sceneDidActivate:"
+ "sceneDidInvalidate:"
+ "sceneDidInvalidate:withContext:"
+ "sceneHandle:didUpdateClientSettings:"
+ "sceneHandleDidRecognizeDoubleTapInDraggableArea:"
+ "sceneHandleDidUpdateLayoutPreferences:"
+ "sceneWillActivate:"
+ "sceneWillDeactivate:withContext:"
+ "sceneWillDeactivate:withError:"
+ "screenScale"
+ "sensitiveUIEnabled"
+ "setActivityViewControllersByActivityIdentifier:"
+ "setAdaptiveTimeHonorsPreferredSalientContentRectangle:"
+ "setAlertDismissalHandler:"
+ "setAllowsHitTesting:"
+ "setAngle:"
+ "setAnimationsEnabled:"
+ "setAppliesX:"
+ "setAppliesY:"
+ "setBackdropLayer:"
+ "setBackgroundContentDidOccludeWallpaperAssertion:"
+ "setBackgroundGlassView:"
+ "setComplicationContainerUsesBottomPosition:"
+ "setComplicationContainerView:"
+ "setComplicationGridLayoutMetricsProvider:"
+ "setConstrainsTimeHeight:"
+ "setContentObscured:"
+ "setContentVisibleAndAppeared:"
+ "setCrossBlurEnd:"
+ "setCrossBlurStart:"
+ "setCrossBlursForTransition:"
+ "setCurvature:"
+ "setDateStyle:"
+ "setDefaultValuesForCrossFadeOnTouchUp"
+ "setDisableActions:"
+ "setDoesRelativeDateFormatting:"
+ "setFadeAlpha:"
+ "setFadeAnchorY:"
+ "setFadeRadiusY:"
+ "setFadeWidth:"
+ "setFindMyAccount:"
+ "setForceOnlyFadeAnimations:"
+ "setHasSidebarContents:"
+ "setHeight:"
+ "setIsPerformingAlphaAnimation:"
+ "setLastAdaptiveTimeTextHeight:"
+ "setLockoutController:"
+ "setMaximumAdaptiveTimeTextHeight:"
+ "setModalPresentationViewOffset:"
+ "setNeedsNestedVibrancyEffectView:"
+ "setNotificationDimView:"
+ "setNotificationListDidOccludeWallpaperAssertion:"
+ "setPasscodeLockVisible:animated:showBackground:completion:"
+ "setPasscodeLockVisible:animated:showBackground:forceBiometricPresentation:completion:"
+ "setPosterHasComplications:"
+ "setPosterPreferredSalientContentRectangle:"
+ "setPreferredColorScheme:"
+ "setRestrictsTouchesOnHostedScene:"
+ "setShadowColor:"
+ "setShadowMaskLayer:"
+ "setShadowOpacity:"
+ "setShadowPathIsBounds:"
+ "setShadowRadius:"
+ "setShowCompactTime:"
+ "setShowCompactTime:animated:"
+ "setTimeStyle:"
+ "setTimeSupportsStretch:"
+ "setUseComplicationRenderStyle:"
+ "setUsesSensitiveUIAppearance:"
+ "setWallpaperOcclusionPercentage:"
+ "setYContentOffset:"
+ "set_wallpaperOccludedAssertions:"
+ "settingsDiff"
+ "shadowMaskLayer"
+ "showCompactTime"
+ "showCompactTime:"
+ "stringFromDate:"
+ "updateCoverSheetDraggingProgress:"
+ "updateCoverSheetTransitionProgress:"
+ "updateFont:preferredTimeMaxYPortrait:preferredTimeMaxYLandscape:vibrancyConfiguration:numberingSystem:contentStyle:"
+ "updateSalientContentRectangle:"
+ "updateSettings:"
+ "userPresenceDetectedRecently"
+ "userPresenceDetectedRecentlyDidChange:"
+ "usesSensitiveUIAppearance"
+ "v20@?0@\"<CSLockProviding>\"8B16"
+ "v24@0:8@\"CSActivityViewController\"16"
+ "v24@0:8@\"FBScene\"16"
+ "v24@0:8@\"MBManager\"16"
+ "v24@0:8@\"SBDeviceApplicationSceneHandle\"16"
+ "v24@0:8@\"SBUIPhoneUnlockWithVisionController\"16"
+ "v24@?0@\"CSActivityListItemViewController\"8@\"UITraitCollection\"16"
+ "v24@?0@\"CSQuickActionControlGlyphView\"8@\"UITraitCollection\"16"
+ "v28@0:8@\"<SBFHomeAffordanceInteraction>\"16B24"
+ "v28@0:8@\"MBManager\"16B24"
+ "v32@0:8@\"CSActivityViewController\"16@\"BSAction\"24"
+ "v32@0:8@\"FBScene\"16@\"FBSSceneTransitionContext\"24"
+ "v32@0:8@\"FBScene\"16@\"FBSSceneUpdate\"24"
+ "v32@0:8@\"FBScene\"16@\"FBSceneClientHandle\"24"
+ "v32@0:8@\"FBScene\"16@\"FBSceneUpdateContext\"24"
+ "v32@0:8@\"FBScene\"16@\"NSError\"24"
+ "v32@0:8@\"MBManager\"16@\"MBDeviceTransferConnectionInfo\"24"
+ "v32@0:8@\"MBManager\"16@\"MBDeviceTransferProgress\"24"
+ "v32@0:8@\"MBManager\"16@\"NSError\"24"
+ "v32@0:8@\"MBManager\"16@\"NSString\"24"
+ "v32@0:8@\"MBManager\"16@24"
+ "v32@0:8@\"MBManager\"16Q24"
+ "v32@0:8@\"NCNotificationStructuredListViewController\"16d24"
+ "v32@0:8@\"NCNotificationStructuredListViewController\"16q24"
+ "v32@0:8@\"SBSceneHandle\"16@\"FBSSceneUpdate\"24"
+ "v32@0:8@\"SBUIPhoneUnlockWithVisionController\"16@\"NSError\"24"
+ "v36@0:8@\"MBManager\"16f24Q28"
+ "v36@0:8@16f24Q28"
+ "v40@0:8@\"FBScene\"16@\"FBSceneUpdateContext\"24@\"NSError\"32"
+ "v40@0:8@\"MBManager\"16@\"NSString\"24@\"NSError\"32"
+ "v40@0:8@\"MBManager\"16@\"NSString\"24Q32"
+ "v40@0:8@16@24Q32"
+ "v40@0:8B16B20B24B28@?32"
+ "v40@0:8d16@24@?32"
+ "v48@0:8@\"FBScene\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneClientSettings\"32@\"FBSSceneTransitionContext\"40"
+ "v48@0:8@\"MBManager\"16@\"NSSet\"24@\"NSString\"32@\"NSString\"40"
+ "v48@0:8@\"MBManager\"16@\"NSString\"24@\"NSString\"32Q40"
+ "v48@0:8@16@24@32Q40"
+ "v52@0:8@\"MBManager\"16f24Q28q36@\"NSString\"44"
+ "v52@0:8@16f24Q28q36@44"
+ "v64@0:8@16d24d32@40@48@56"
+ "wallpaperLegibilityContainerView"
+ "wallpaperOcclusionPercentage"
+ "{CGSize=dd}24@0:8@\"CSActivityContentView\"16"
+ "{UIEdgeInsets=dddd}24@0:8q16"
+ "\xf0\xc2\xf0\xf0\xf0\x91"
- "22"
- "@\"<CSActivityItemContentViewSizeProviding>\""
- "@\"<CSActivityItemViewControllerDelegate>\""
- "@\"<CSListItemSceneHostEnvironmentObserving>\""
- "@72@0:8^Q16^Q24^@32^@40^@48^@56^@64"
- "Active state changed to: %@"
- "Adding greeting view background: %{public}@"
- "CSActivityItemContentView"
- "CSActivityItemContentViewSizeProviding"
- "CSActivityItemViewController"
- "CSActivityItemViewControllerDelegate"
- "CSListItemSceneHostEnvironmentObserving"
- "Date Time Standin"
- "Dismissing greeting view: %{public}@"
- "Hosts in Notification List"
- "Initialization"
- "Lock Out Status Changed"
- "NotificationsUI"
- "Post notification request dismissed greeting view."
- "Presenting greeting view: %{public}@"
- "ReactiveList"
- "T@\"<BSInvalidatable>\",&,N,V_restrictsTouchesAssertion"
- "T@\"<CSActivityItemContentViewSizeProviding>\",W,N,V_sizeProvider"
- "T@\"<CSActivityItemViewControllerDelegate>\",W,N,V_delegate"
- "T@\"<CSListItemSceneHostEnvironmentObserving>\",W,N,V_sceneHostEnvironmentObserver"
- "T@\"ACUISActivityHostViewController\",&,N,V_activityHostViewController"
- "T@\"NSMutableDictionary\",&,N,V_activityHostViewControllersByActivityIdentifier"
- "TB,N,GisContentVisible,V_contentVisible"
- "TB,N,GisDepthEffectEnabled,V_depthEffectDisabled"
- "TB,N,V_hostsInlineContentNativelyInNotificationList"
- "TB,N,V_includesDateTimeStandinInAdjunctList"
- "[Quick Action] leading action being defaulted to flashlight"
- "__currentDesiredAppearanceWithStartIndex:targetIndex:targetAppearance:targetPresentation:modalAppearance:proudLockAppearance:poseidonAppearance:"
- "_activityHostViewController"
- "_activityHostViewControllersByActivityIdentifier"
- "_allowsNotificationListTopInset"
- "_allowsSeparateAdjunctList"
- "_contentVisible"
- "_flashlight"
- "_hostsInlineContentInAdjunctList"
- "_hostsInlineContentNativelyInNotificationList"
- "_hostsTimeInAdjunctList"
- "_iconZoomBackgroundEffectView"
- "_includesDateTimeStandinInAdjunctList"
- "_integratesAdjunctListIntoFullList"
- "_isContentVisibleAndAppeared"
- "_setupFlashlightController"
- "_setupFlashlightControllerIfNecessary"
- "_sizeProvider"
- "_snapScrollView:toAcceptableOffsetAnimated:"
- "_snapToAcceptableOffsetForScrollView:"
- "_tearDownFlashlight"
- "_tearDownFlashlightIfOff"
- "_updateFaceDetectionState"
- "_updateFlashlightAction:"
- "_updateModalPresentationControllerVisibility"
- "_updatePresentationModeWithReason:"
- "activityHostViewController"
- "activityHostViewControllersByActivityIdentifier"
- "activityItemViewControllerDidUpdateAudioCategoriesDisablingVolumeHUD:"
- "attemptPhoneUnlockWithWatch"
- "backgroundEffectView"
- "clearAllStyling"
- "contentLayoutGuide"
- "contentVisible"
- "copyBackgroundVisualEffectView"
- "didDetectFaceRequirementsForPAU"
- "disableDetectionForReason:"
- "dismissOverlaysAnimated:"
- "dismissableOverlays"
- "enableDetectionForReason:"
- "frameLayoutGuide"
- "hostsInlineContentNativelyInNotificationList"
- "includesDateTimeStandinInAdjunctList"
- "initWithActivityHostViewController:"
- "insertArrangedSubview:atIndex:"
- "interpretsViewAsAdjunctContent:"
- "isContentVisible"
- "isDepthEffectEnabled"
- "phoneUnlockWithWatchEnabled"
- "prui_primaryPosterOffset"
- "prui_primaryPosterScale"
- "prui_setLeadingTopButtonFrame:"
- "prui_setLockPosterComplicationRowHidden:"
- "prui_setLockPosterFloatingLayerInlined:"
- "prui_setLockPosterLiveContentLayerContextID:"
- "prui_setLockPosterLiveContentLayerRenderID:"
- "prui_setLockPosterLiveFloatingLayerContextID:"
- "prui_setLockPosterLiveFloatingLayerRenderID:"
- "prui_setLockPosterOverlayLayerContextID:"
- "prui_setLockPosterOverlayLayerRenderID:"
- "prui_setLockVibrancyConfiguration:"
- "prui_setPreferredSwitcherLayoutMode:"
- "prui_setTrailingTopButtonFrame:"
- "prui_switcherContextID"
- "prui_switcherLayoutMode"
- "reevaluateAudioCategoriesDisablingVolumeHUD"
- "restrictsTouchesAssertion"
- "restrictsTouchesOnHostedScene:"
- "sceneHandle:didUpdateClientSettingsWithDiff:transitionContext:"
- "sceneHandle:didUpdatePairingStatusForExternalSceneIdentifiers:"
- "setActivityHostViewController:"
- "setActivityHostViewControllersByActivityIdentifier:"
- "setContentVisible:"
- "setHostsInlineContentNativelyInNotificationList:"
- "setIncludesDateTimeStandinInAdjunctList:"
- "setLiftToWakeGestureDetectedSinceScreenOn:"
- "setPasscodeLockVisible:animated:forceBiometricPresentation:completion:"
- "setRestrictsTouchesAssertion:"
- "setSignificantUserInteractionOccuredSinceScreenOn:"
- "setSizeProvider:"
- "setWakeSourceIsUserAction:"
- "settleContentOffset"
- "shouldHostContentInNotificationList"
- "sizeProvider"
- "updateFont:vibrancyConfiguration:numberingSystem:contentStyle:"
- "v24@0:8@\"CSActivityItemViewController\"16"
- "v24@?0@\"ACUISActivityHostViewController\"8@\"UITraitCollection\"16"
- "v32@0:8@\"SBSceneHandle\"16@\"NSSet\"24"
- "v40@0:8@\"SBSceneHandle\"16@\"FBSSceneClientSettingsDiff\"24@\"FBSSceneTransitionContext\"32"
- "{CGSize=dd}24@0:8@\"CSActivityItemContentView\"16"
- "\xf0\xb2\xf0\xf0\xf0A"

```
