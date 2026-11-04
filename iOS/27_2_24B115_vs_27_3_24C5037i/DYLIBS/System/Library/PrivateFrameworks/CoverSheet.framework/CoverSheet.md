## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

-159.2.4.0.0
-  __TEXT.__text: 0x192080
-  __TEXT.__objc_methlist: 0x169c4
-  __TEXT.__const: 0x415c
-  __TEXT.__cstring: 0xd0cc
-  __TEXT.__oslogstring: 0x9269
-  __TEXT.__gcc_except_tab: 0x139c
-  __TEXT.__ustring: 0xa4
+159.3.10.200.0
+  __TEXT.__text: 0x19d94c
+  __TEXT.__objc_methlist: 0x17644
+  __TEXT.__const: 0x4614
+  __TEXT.__cstring: 0xd155
+  __TEXT.__oslogstring: 0x8f66
+  __TEXT.__gcc_except_tab: 0x1140
+  __TEXT.__ustring: 0x98
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x5a28
+  __TEXT.__unwind_info: 0x5da0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x40f8
-  __DATA_CONST.__objc_classlist: 0x7c8
-  __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x670
+  __DATA_CONST.__const: 0x4158
+  __DATA_CONST.__objc_classlist: 0x7d0
+  __DATA_CONST.__objc_catlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x698
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc950
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x600
-  __DATA_CONST.__objc_arraydata: 0x1108
-  __DATA_CONST.__got: 0x15b8
-  __AUTH_CONST.__const: 0xcf0
-  __AUTH_CONST.__cfstring: 0xd180
-  __AUTH_CONST.__objc_const: 0x3d760
-  __AUTH_CONST.__objc_arrayobj: 0x12a8
-  __AUTH_CONST.__objc_intobj: 0x510
-  __AUTH_CONST.__objc_doubleobj: 0x660
-  __AUTH_CONST.__auth_got: 0xd28
-  __AUTH.__objc_data: 0xf50
-  __DATA.__objc_ivar: 0x1ca8
-  __DATA.__data: 0x56f8
+  __DATA_CONST.__objc_selrefs: 0xd190
+  __DATA_CONST.__objc_protorefs: 0x30
+  __DATA_CONST.__objc_superrefs: 0x618
+  __DATA_CONST.__objc_arraydata: 0x1098
+  __DATA_CONST.__got: 0x15c8
+  __AUTH_CONST.__const: 0xd50
+  __AUTH_CONST.__cfstring: 0xd000
+  __AUTH_CONST.__objc_const: 0x3e570
+  __AUTH_CONST.__objc_arrayobj: 0x1278
+  __AUTH_CONST.__objc_intobj: 0x450
+  __AUTH_CONST.__objc_doubleobj: 0x6a0
+  __AUTH_CONST.__auth_got: 0xd68
+  __AUTH.__objc_data: 0x10e0
+  __DATA.__objc_ivar: 0x1d4c
+  __DATA.__data: 0x58e0
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x3e80
+  __DATA_DIRTY.__objc_data: 0x3d40
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8048
-  Symbols:   14287
-  CStrings:  2743
+  Functions: 8311
+  Symbols:   14646
+  CStrings:  2725
 
Symbols:
+ +[CSCombinedListViewController viewClass]
+ +[CSComplicationColumnComponent hardwareSupportsFeature]
+ +[CSComponent complicationColumn]
+ +[CSContentCutoutBoundsCalculator _boundsForPortrait:bounds:]
+ +[CSContentCutoutBoundsCalculator _boundsForWindowScene:]
+ +[CSContentCutoutBoundsCalculator _contentCutoutBounds:portrait:forModal:buttonLayout:deviceConfiguration:]
+ +[CSContentCutoutBoundsCalculator _contentCutoutBoundsForLandscapePhoneWithoutButtonsBoundingSize:]
+ +[CSContentCutoutBoundsCalculator _contentCutoutBoundsForPortrait:forModal:deviceConfiguration:]
+ +[CSContentCutoutBoundsCalculator _contentCutoutBoundsForPortrait:forModal:screen:]
+ +[CSContentCutoutBoundsCalculator _contentCutoutBoundsForPortrait:forModal:windowScene:]
+ +[CSContentCutoutBoundsCalculator _normalizedContentCutoutForBounds:contentBoundingRect:]
+ +[CSMagSafeAccessoryView centerForBounds:withOffset:view:]
+ +[CSMagSafeSilhouetteConfiguration isOrientation:oneCounterClockwiseShiftFrom:]
+ +[CSModalView _modalViewBottomBaselineOffsetPortraitDodgingQuickActions:]
+ +[CSModalView(Private) _bottomBaselineOffsetForPortrait:dodgingQuickActions:]
+ +[CSNotificationLegibilityDimView usesPadStyleLayoutForTraitCollection:deviceConfiguration:]
+ +[CSPageControl suggestedFrameForPageBounds:desiredSize:view:]
+ +[CSPageControl suggestedFrameForPageBounds:view:]
+ +[CSRemoteContentCoordinator sharedCoordinator]
+ -[CSActivityManager _addActivityItem:toRecords:forKey:]
+ -[CSActivityManager _bundleIdentifierForItem:]
+ -[CSActivityManager _clearAuthorizationOptionsIfNecessaryForBundleIdentifier:]
+ -[CSActivityManager _groupNameForDescriptor:groupingIdentifier:]
+ -[CSActivityManager _groupingIdentifierForDescriptor:]
+ -[CSActivityManager _invalidateActivityMetrics]
+ -[CSActivityManager _removeActivityItem:fromRecords:forKey:]
+ -[CSActivityManager activityItemsByGroupingIdentifier]
+ -[CSActivityManager isAvoidingFold]
+ -[CSActivityManager setActivityItemsByGroupingIdentifier:]
+ -[CSActivityManager setAvoidingFold:]
+ -[CSActivityManager updateAvoidingFold:]
+ -[CSActivityViewController invalidateMetrics]
+ -[CSBackgroundContentActionManager _adoptAction:]
+ -[CSBackgroundContentActionManager _invalidationHandlerForAction:]
+ -[CSBackgroundContentActionManager transferActiveActionsToManager:]
+ -[CSBatteryChargingRingView _activeInterfaceOrientation]
+ -[CSBatteryChargingRingView _showsSilhouette]
+ -[CSBatteryChargingRingView _silhouetteAlignedOrientation]
+ -[CSBatteryChargingRingView _updateLabelVisibility:]
+ -[CSBatteryChargingRingView didMoveToWindow]
+ -[CSBatteryChargingRingView ringCenterOffset]
+ -[CSBatteryChargingView _fontSizeForElement:]
+ -[CSBatteryChargingView didMoveToWindow]
+ -[CSBatteryChargingView effectiveRingCenterForBounds:]
+ -[CSBatteryChargingView ringCenterOffset]
+ -[CSBatteryChargingView setRingCenterOffset:]
+ -[CSCombinedListView .cxx_destruct]
+ -[CSCombinedListView containsPointInHitBoxAddenda:]
+ -[CSCombinedListView hitBoxAddendumView]
+ -[CSCombinedListView hitTest:withEvent:]
+ -[CSCombinedListView leftHitBoxAddendumRect]
+ -[CSCombinedListView obstructingContentHitTester]
+ -[CSCombinedListView rightHitBoxAddendumRect]
+ -[CSCombinedListView setHitBoxAddendumView:]
+ -[CSCombinedListView setLeftHitBoxAddendumRect:]
+ -[CSCombinedListView setObstructingContentHitTester:]
+ -[CSCombinedListView setRightHitBoxAddendumRect:]
+ -[CSCombinedListViewController _deviceSupportsStatusBarBackground]
+ -[CSCombinedListViewController _fullySupportsLandscapeFeatures]
+ -[CSCombinedListViewController _hitBoxAddendumSwipeRecognizerChanged:]
+ -[CSCombinedListViewController _isFlexibleLockScreenEnabled]
+ -[CSCombinedListViewController _supportsHitBoxAddenda]
+ -[CSCombinedListViewController _updateHitBoxAddenda]
+ -[CSCombinedListViewController _updateTimeScrolledOffscreenForScrollOffset:]
+ -[CSCombinedListViewController beginContainerResize]
+ -[CSCombinedListViewController endContainerResize]
+ -[CSCombinedListViewController gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:]
+ -[CSCombinedListViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
+ -[CSCombinedListViewController gestureRecognizer:shouldRequireFailureOfGestureRecognizer:]
+ -[CSCombinedListViewController gestureRecognizerShouldBegin:]
+ -[CSCombinedListViewController interpretsLocationAsHitBoxAddendum:inView:]
+ -[CSCombinedListViewController isTimeScrolledOffscreen]
+ -[CSCombinedListViewController obstructingContentHitTester]
+ -[CSCombinedListViewController permittedBounds]
+ -[CSCombinedListViewController setObstructingContentHitTester:]
+ -[CSCombinedListViewController setPermittedBounds:]
+ -[CSComplicationColumnComponent init]
+ -[CSComplicationManager onColumnWidgetUpdate]
+ -[CSComplicationManager setOnColumnWidgetUpdate:]
+ -[CSCoverSheetAppearanceResolver _resolveComplicationColumnComponent]
+ -[CSCoverSheetFlyInSettings dockFlyZResponseMultiplier]
+ -[CSCoverSheetFlyInSettings iconFlyZDistanceExponent]
+ -[CSCoverSheetFlyInSettings iconFlyZMaxDistanceForPad]
+ -[CSCoverSheetFlyInSettings iconFlyZMaxDistanceForPhone]
+ -[CSCoverSheetFlyInSettings iconFlyZMaxDistance]
+ -[CSCoverSheetFlyInSettings setDockFlyZResponseMultiplier:]
+ -[CSCoverSheetFlyInSettings setIconFlyZDistanceExponent:]
+ -[CSCoverSheetFlyInSettings setIconFlyZMaxDistance:]
+ -[CSCoverSheetFlyInSettings setIconFlyZMaxDistanceForPad:]
+ -[CSCoverSheetFlyInSettings setIconFlyZMaxDistanceForPhone:]
+ -[CSCoverSheetFlyInSettings setVerticalDockCenterPointOffsetX:]
+ -[CSCoverSheetFlyInSettings setVerticalDockCenterPointOffsetY:]
+ -[CSCoverSheetFlyInSettings setWidgetLoomMinEligibleSize:]
+ -[CSCoverSheetFlyInSettings setWidgetMaxLoomSize:]
+ -[CSCoverSheetFlyInSettings setWidgetSpreadFactor:]
+ -[CSCoverSheetFlyInSettings verticalDockCenterPointOffsetX]
+ -[CSCoverSheetFlyInSettings verticalDockCenterPointOffsetY]
+ -[CSCoverSheetFlyInSettings widgetLoomMinEligibleSize]
+ -[CSCoverSheetFlyInSettings widgetMaxLoomSize]
+ -[CSCoverSheetFlyInSettings widgetSpreadFactor]
+ -[CSCoverSheetSDFView _attachCornerRadiiPresentationModifier:]
+ -[CSCoverSheetSDFView _cornerRadiiDrivenLayers]
+ -[CSCoverSheetSDFView _detachCornerRadiiPresentationModifier]
+ -[CSCoverSheetSDFView _layoutLayer:inBounds:withCornerRadii:]
+ -[CSCoverSheetSDFView _layoutLayer:inBounds:withCornerRadii:horizontalOutset:]
+ -[CSCoverSheetSDFView _removeCornerRadiiPresentationModifierFromLayers:]
+ -[CSCoverSheetSDFView _updateCornerConfiguration]
+ -[CSCoverSheetSDFView cornerRadiiOverride]
+ -[CSCoverSheetSDFView didMoveToWindow]
+ -[CSCoverSheetSDFView endBackgroundCornerRadiiUpdates]
+ -[CSCoverSheetSDFView setBackgroundCornerRadii:forPresentationValue:]
+ -[CSCoverSheetView _addFocusQuickActionView]
+ -[CSCoverSheetView _complicationContainerFrameForElements:]
+ -[CSCoverSheetView _layoutComplicationColumnView]
+ -[CSCoverSheetView _permittedRegionOffsetX]
+ -[CSCoverSheetView _regionsAwareAvailableRect]
+ -[CSCoverSheetView _regionsAwareScaleAnchorPoint]
+ -[CSCoverSheetView _usesPadWallpaperBehavior]
+ -[CSCoverSheetView cachedPermittedBounds]
+ -[CSCoverSheetView columnComplicationContainerView]
+ -[CSCoverSheetView endBackgroundCornerRadiiUpdates]
+ -[CSCoverSheetView focusQuickActionView]
+ -[CSCoverSheetView freezesPermittedBounds]
+ -[CSCoverSheetView setBackgroundCornerRadii:forPresentationValue:]
+ -[CSCoverSheetView setColumnComplicationContainerView:]
+ -[CSCoverSheetView setFocusQuickActionView:]
+ -[CSCoverSheetView setFreezesPermittedBounds:]
+ -[CSCoverSheetView setNotificationLegibilityFadeRadiusY:]
+ -[CSCoverSheetView setShouldClipBackgroundElements:]
+ -[CSCoverSheetView shouldClipBackgroundElements]
+ -[CSCoverSheetViewController _backgroundIsDarkAffectingLegibility]
+ -[CSCoverSheetViewController _cancelRestToOpenCoachingIdleTimer]
+ -[CSCoverSheetViewController _configureNotificationDispatcher]
+ -[CSCoverSheetViewController _coverSheetUniqueIdentifier]
+ -[CSCoverSheetViewController _floatingLayerAlphaForTransitionProgress:]
+ -[CSCoverSheetViewController _fullySupportsAutorotation]
+ -[CSCoverSheetViewController _fullySupportsLandscapeFeatures]
+ -[CSCoverSheetViewController _hidesTallElementsInLandscape]
+ -[CSCoverSheetViewController _interpretsLocationAsVerticalStatusBarContent:inView:]
+ -[CSCoverSheetViewController _isConfigurationEligibleForWidgets]
+ -[CSCoverSheetViewController _isReachabilityOffsetZero]
+ -[CSCoverSheetViewController _publishRemoteContentAppearance]
+ -[CSCoverSheetViewController _reconcileAppearanceForDeviceState]
+ -[CSCoverSheetViewController _reinstateRemoteContentIfNecessary]
+ -[CSCoverSheetViewController _sendScreenStateEventToViewController:]
+ -[CSCoverSheetViewController _setFakeStatusBarMode:]
+ -[CSCoverSheetViewController _setFreezesPermittedBoundsForFoldAvoidance:]
+ -[CSCoverSheetViewController _setRealStatusBarMode:]
+ -[CSCoverSheetViewController _showRestToOpenCoachingViewWithState:]
+ -[CSCoverSheetViewController _startRestToOpenCoachingIdleTimer]
+ -[CSCoverSheetViewController _stopRestToOpenCoachingAnimated:]
+ -[CSCoverSheetViewController _subduedGlassAssertions]
+ -[CSCoverSheetViewController _tryBiometricSuppressionObserverSetup]
+ -[CSCoverSheetViewController _updateComplicationColumn]
+ -[CSCoverSheetViewController _updateLeadingAlignedContentEnablement]
+ -[CSCoverSheetViewController _updatePoseidonBiometricMentionSuppressionForModalities:]
+ -[CSCoverSheetViewController _updatePoseidonCoachingSuppression]
+ -[CSCoverSheetViewController _updateSubduedGlassTimeAppearance]
+ -[CSCoverSheetViewController _usesSubtitleRestToOpenCoaching]
+ -[CSCoverSheetViewController _validRemoteContentAssertionForIdentifier:]
+ -[CSCoverSheetViewController acquireSubduedGlassAssertionForReason:]
+ -[CSCoverSheetViewController areComplicationsUsingTopPosition]
+ -[CSCoverSheetViewController backgroundContentActionManagerShouldHandleActions:]
+ -[CSCoverSheetViewController biometricSuppressionProvider:didUpdateSuppressedBiometricModalities:]
+ -[CSCoverSheetViewController columnComplicationContainerViewController]
+ -[CSCoverSheetViewController combinedListViewController]
+ -[CSCoverSheetViewController coordinatorPowerStatusChangedToConnectedState:]
+ -[CSCoverSheetViewController embeddedContentActionManager]
+ -[CSCoverSheetViewController endBackgroundCornerRadiiUpdates]
+ -[CSCoverSheetViewController hasAuxillaryContentObscuringCoverSheet]
+ -[CSCoverSheetViewController interpretsLocationAsObstructingContent:inView:]
+ -[CSCoverSheetViewController isHorizontalScrollingPossible]
+ -[CSCoverSheetViewController isPermanentCompactTimeEnabled]
+ -[CSCoverSheetViewController passcodeViewController:didChangeBiometricInterstitialVisibility:]
+ -[CSCoverSheetViewController realStatusBarAssertedMode]
+ -[CSCoverSheetViewController realStatusBarModeAssertion]
+ -[CSCoverSheetViewController remoteContentListItemSpacing]
+ -[CSCoverSheetViewController setBackgroundCornerRadii:forPresentationValue:]
+ -[CSCoverSheetViewController setColumnComplicationContainerViewController:]
+ -[CSCoverSheetViewController setCombinedListViewController:]
+ -[CSCoverSheetViewController setEmbeddedContentActionManager:]
+ -[CSCoverSheetViewController setHasAuxillaryContentObscuringCoverSheet:]
+ -[CSCoverSheetViewController setLiftAndRestToOpenCoachingVisible:]
+ -[CSCoverSheetViewController setPermanentCompactTimeEnabled:]
+ -[CSCoverSheetViewController setRealStatusBarAssertedMode:]
+ -[CSCoverSheetViewController setRealStatusBarModeAssertion:]
+ -[CSCoverSheetViewController setWantsLeadingAlignedContent:]
+ -[CSCoverSheetViewController set_subduedGlassAssertions:]
+ -[CSCoverSheetViewController supportedInactiveBacklightInterfaceOrientations]
+ -[CSCoverSheetViewController wantsLeadingAlignedContent]
+ -[CSCoverSheetViewController(Layout) _hasUVBButtons]
+ -[CSCoverSheetViewController(Layout) prominentContentTopY]
+ -[CSDashBoardNotificationVersusPagingScrollSettings allowsAuxiliaryScrollingWhileViscous]
+ -[CSDashBoardNotificationVersusPagingScrollSettings setAllowsAuxiliaryScrollingWhileViscous:]
+ -[CSDashBoardQuickActionsButtonSettings alwaysOnFocusButtonAnimatesMove]
+ -[CSDashBoardQuickActionsButtonSettings alwaysOnFocusButtonShowsMaterial]
+ -[CSDashBoardQuickActionsButtonSettings alwaysOnFocusButtonSlides]
+ -[CSDashBoardQuickActionsButtonSettings alwaysOnFocusButtonWhitepoint]
+ -[CSDashBoardQuickActionsButtonSettings setAlwaysOnFocusButtonAnimatesMove:]
+ -[CSDashBoardQuickActionsButtonSettings setAlwaysOnFocusButtonShowsMaterial:]
+ -[CSDashBoardQuickActionsButtonSettings setAlwaysOnFocusButtonSlides:]
+ -[CSDashBoardQuickActionsButtonSettings setAlwaysOnFocusButtonWhitepoint:]
+ -[CSDashBoardQuickActionsButtonSettings setWantsConcentricityInAOD:]
+ -[CSDashBoardQuickActionsButtonSettings wantsConcentricityInAOD]
+ -[CSDashBoardScrollModifierSettings marginSwipeDirectionMinimumTravel]
+ -[CSDashBoardScrollModifierSettings setMarginSwipeDirectionMinimumTravel:]
+ -[CSDismissableModalViewController homeGestureParticipantUpdateZStackZOrderPreferences:forZStackParticipant:]
+ -[CSDismissableModalViewController touchInterfaceOrientationForGestureRecognizer:]
+ -[CSEmbeddedContentActionManager adoptActiveActionsFromManager:]
+ -[CSFixedFooterView permittedBounds]
+ -[CSFixedFooterView setPermittedBounds:]
+ -[CSFocusQuickAction .cxx_destruct]
+ -[CSFocusQuickAction _accessibilityIdentifierForFocusMode]
+ -[CSFocusQuickAction _isFocusActivity:equalTo:]
+ -[CSFocusQuickAction accessibilityIdentifier]
+ -[CSFocusQuickAction accessoryTitleKey]
+ -[CSFocusQuickAction actionDidDisappear]
+ -[CSFocusQuickAction actionIdentifier]
+ -[CSFocusQuickAction allowsInteraction]
+ -[CSFocusQuickAction appearance]
+ -[CSFocusQuickAction effectiveFocusMode]
+ -[CSFocusQuickAction fireAction]
+ -[CSFocusQuickAction focusMode]
+ -[CSFocusQuickAction initWithFocusMode:delegate:]
+ -[CSFocusQuickAction isSelected]
+ -[CSFocusQuickAction previousFocusMode]
+ -[CSFocusQuickAction selectedSymbolName]
+ -[CSFocusQuickAction setFocusMode:]
+ -[CSFocusQuickAction showsButton]
+ -[CSFocusQuickAction statisticsIdentifier]
+ -[CSFocusQuickAction supportsSelection]
+ -[CSFocusQuickAction symbolName]
+ -[CSFocusQuickAction symbolOnColor]
+ -[CSFocusQuickAction symbolScaleValue]
+ -[CSFocusQuickAction togglesSelectionOnPress]
+ -[CSFocusQuickAction touchBegan]
+ -[CSFocusQuickAction touchEnded]
+ -[CSFocusQuickAction unavailableSymbolName]
+ -[CSHitBoxAddendumSwipeRecognizer addendumSwipeMinimumTravel]
+ -[CSHitBoxAddendumSwipeRecognizer reset]
+ -[CSHitBoxAddendumSwipeRecognizer setAddendumSwipeMinimumTravel:]
+ -[CSHitBoxAddendumSwipeRecognizer startingLocationInView]
+ -[CSHitBoxAddendumSwipeRecognizer touchesBegan:withEvent:]
+ -[CSHitBoxAddendumSwipeRecognizer touchesCancelled:withEvent:]
+ -[CSHitBoxAddendumSwipeRecognizer touchesEnded:withEvent:]
+ -[CSHitBoxAddendumSwipeRecognizer touchesMoved:withEvent:]
+ -[CSLayoutStrategy suggestedFrameForListForPage:bounds:device:]
+ -[CSLayoutStrategy suggestedFrameForListForPage:bounds:permittedBounds:device:]
+ -[CSLockScreenMesaSettings isPoseidonPhone]
+ -[CSMagSafeAccessoryConfiguration offsetFromScreenCenter:]
+ -[CSMagSafeAccessoryConfiguration prominentContentTopY]
+ -[CSMagSafeAccessoryView didMoveToWindow]
+ -[CSMagSafeAccessoryView effectiveRingCenterForBounds:]
+ -[CSMagSafeAccessoryViewController viewWillAppear:]
+ -[CSMagSafeAccessoryWalletView _activeInterfaceOrientation]
+ -[CSMagSafeAccessoryWalletView _recreateSilhouette]
+ -[CSMagSafeAccessoryWalletView _silhouetteAlignedOrientation]
+ -[CSMagSafeAccessoryWalletView _updateRoundedCorners]
+ -[CSMagSafeAccessoryWalletView didMoveToWindow]
+ -[CSMagSafeRingConfiguration _initWithRingDiameter:lineWidth:splashRingDiamter:]
+ -[CSMagSafeSilhouetteConfiguration _cornersForRoundedCorners:]
+ -[CSMagSafeSilhouetteConfiguration _roundedCornersForOrientation:]
+ -[CSMagSafeSilhouetteConfiguration aligningOrientation]
+ -[CSMagSafeSilhouetteConfiguration initWithSize:bottomOffset:cornerRadius:aligningOrientation:]
+ -[CSMagSafeSilhouetteConfiguration initWithSize:bottomOffset:cornerRadius:aligningOrientation:roundedCorners:]
+ -[CSMagSafeSilhouetteConfiguration setAligningOrientation:]
+ -[CSMainPageContentViewController _fullySupportsLandscapeFeatures]
+ -[CSMainPageContentViewController _isAvoidingFold]
+ -[CSMainPageContentViewController _isPhoneThatSupportsFullLandscape]
+ -[CSMainPageContentViewController _isV68InnerDisplay]
+ -[CSMainPageContentViewController _isV68OuterDisplay]
+ -[CSMainPageContentViewController setPermittedBounds:]
+ -[CSMainPageView _updateWithPermittedBounds]
+ -[CSMainPageView permittedBounds]
+ -[CSMainPageView setPermittedBounds:]
+ -[CSModalView _updateCentralGroupInsets]
+ -[CSNotificationLegibilityDimController setUsesPadStyleLayout:]
+ -[CSNotificationLegibilityDimController usesPadStyleLayout]
+ -[CSNotificationLegibilityDimView _usesPadStyleLayout]
+ -[CSNotificationLegibilityDimView layoutInsetsForSize:fadeAnchorY:permittedBounds:]
+ -[CSNotificationLegibilityDimView layoutInsetsForSize:permittedBounds:]
+ -[CSPageControl suggestedFrameForPageBounds:]
+ -[CSPageControl suggestedFrameForPageBounds:desiredSize:]
+ -[CSPasscodeViewController _createPoseidonViewControllerIfNeeded]
+ -[CSPasscodeViewController _reallyUsesBiometricPresentation]
+ -[CSPasscodeViewController destinationScreen]
+ -[CSPasscodeViewController ownsPoseidonCoaching]
+ -[CSPasscodeViewController refreshBiometricPresentationMode]
+ -[CSPasscodeViewController setDestinationScreen:]
+ -[CSPasscodeViewController setUnlockIntent:]
+ -[CSPasscodeViewController unlockIntent]
+ -[CSPoseidonViewController _updateWindowPinningAnimation]
+ -[CSPoseidonViewController acquireCoachingSuppressionAssertionWithLevel:]
+ -[CSPoseidonViewController dealloc]
+ -[CSPoseidonViewController devicePoseProvider:didChangeDevicePose:]
+ -[CSPoseidonViewController devicePoseProvider]
+ -[CSPoseidonViewController isScreenOn]
+ -[CSPoseidonViewController setDevicePoseProvider:]
+ -[CSPoseidonViewController setScreenOn:]
+ -[CSPoseidonViewController viewDidMoveToWindow:shouldAppearOrDisappear:]
+ -[CSQuickAction setTogglesSelectionOnPress:]
+ -[CSQuickAction togglesSelectionOnPress]
+ -[CSQuickActionImageGlyphView _fallbackSystemImage]
+ -[CSQuickActionImageGlyphView overrideTintColor]
+ -[CSQuickActionImageGlyphView setOverrideTintColor:]
+ -[CSQuickActionsButton _shouldAnimatePropertyWithKey:]
+ -[CSQuickActionsButton _updateGlyphTintOverride]
+ -[CSQuickActionsButton animatedLayerProperties]
+ -[CSQuickActionsButton setAnimatedLayerProperties:]
+ -[CSQuickActionsButton setHidesBackground:]
+ -[CSQuickActionsComponent retainsFocusButtonInAOD:]
+ -[CSQuickActionsComponent retainsFocusButtonInAOD]
+ -[CSQuickActionsComponent setRetainsFocusButtonInAOD:]
+ -[CSQuickActionsView _applyFocusButtonMaterial]
+ -[CSQuickActionsView _applyFocusButtonSlot]
+ -[CSQuickActionsView _buttonsIncludingAddenda]
+ -[CSQuickActionsView _interpretsLocationAsContent:inView:visibleButtonsOnly:]
+ -[CSQuickActionsView _layoutFocusButton]
+ -[CSQuickActionsView _movesFocusButtonToCornerForAlwaysOn]
+ -[CSQuickActionsView _updateFocusButtonSlot]
+ -[CSQuickActionsView didMoveToWindow]
+ -[CSQuickActionsView focusAction]
+ -[CSQuickActionsView focusButtonHostView]
+ -[CSQuickActionsView focusButton]
+ -[CSQuickActionsView interpretsLocationAsVisibleContent:inView:]
+ -[CSQuickActionsView setFocusAction:]
+ -[CSQuickActionsView setFocusButton:]
+ -[CSQuickActionsView setFocusButtonHostView:]
+ -[CSQuickActionsView setRetainsFocusButtonInAOD:]
+ -[CSQuickActionsViewController _fetchFocusModeWithCompletion:]
+ -[CSQuickActionsViewController _setActionsVisible:]
+ -[CSQuickActionsViewController activeActivityDidChangeForManager:]
+ -[CSQuickActionsViewController activityPickerViewControllerPresentingView:]
+ -[CSQuickActionsViewController activityPickerViewControllerRepresentedActivityForDismissal:]
+ -[CSQuickActionsViewController activityPickerViewControllerRepresentedActivityForPresentation:]
+ -[CSQuickActionsViewController activityPickerViewController]
+ -[CSQuickActionsViewController availableActivitiesDidChangeForManager:]
+ -[CSQuickActionsViewController presentFocusLabelForAction:]
+ -[CSQuickActionsViewController presentFocusPicker]
+ -[CSQuickActionsViewController setRetainsFocusButtonInAOD:]
+ -[CSRemoteContentCoordinator .cxx_destruct]
+ -[CSRemoteContentCoordinator _activeForwardingTarget]
+ -[CSRemoteContentCoordinator _initShared]
+ -[CSRemoteContentCoordinator activeRemoteContentAssertionForIdentifier:]
+ -[CSRemoteContentCoordinator authenticationStatusProvider]
+ -[CSRemoteContentCoordinator registerCoverSheetViewController:]
+ -[CSRemoteContentCoordinator remoteContentComplicationHeightInset]
+ -[CSRemoteContentCoordinator remoteContentComplicationTopYInset]
+ -[CSRemoteContentCoordinator remoteContentDidUpdateStyle]
+ -[CSRemoteContentCoordinator remoteContentListItemSpacing]
+ -[CSRemoteContentCoordinator remoteContentSession:didInvalidateWithError:]
+ -[CSRemoteContentCoordinator remoteContentSession:dismissWithReason:completion:]
+ -[CSRemoteContentCoordinator remoteContentSession:presentViewController:]
+ -[CSRemoteContentCoordinator sessionManager]
+ -[CSRemoteContentCoordinator setAuthenticationStatusProvider:]
+ -[CSRemoteContentCoordinator shouldActivateRemoteContentSession:]
+ -[CSRemoteContentCoordinator unregisterCoverSheetViewController:]
+ -[CSRemoteContentHostViewController _contentBoundsFittingInlinePlatter:]
+ -[CSRemoteContentHostViewController _vendableContentBounds]
+ -[CSRemoteContentHostViewController inlinePlatterWidth]
+ -[CSRemoteContentHostViewController setInlinePlatterWidth:]
+ -[CSRemoteContentInlineView .cxx_destruct]
+ -[CSRemoteContentInlineView didMoveToWindowHandler]
+ -[CSRemoteContentInlineView didMoveToWindow]
+ -[CSRemoteContentInlineView setDidMoveToWindowHandler:]
+ -[CSRemoteContentInlineViewController _contributesGlobalSuppression]
+ -[CSRemoteContentInlineViewController _handleWindowChange]
+ -[CSRemoteContentInlineViewController hidesTime]
+ -[CSRemoteContentInlineViewController whitePointReduction]
+ -[CSRemoteContentSession remoteContentListItemSpacing]
+ -[CSRestToOpenCoachingView .cxx_destruct]
+ -[CSRestToOpenCoachingView _activeTextLabel]
+ -[CSRestToOpenCoachingView _animateContentToScale:duration:options:]
+ -[CSRestToOpenCoachingView _currentProgressFillLocations]
+ -[CSRestToOpenCoachingView _installProgressFillMask]
+ -[CSRestToOpenCoachingView _labelWithFont:textColor:]
+ -[CSRestToOpenCoachingView _prepareUnfilled]
+ -[CSRestToOpenCoachingView _progressFillMaskFrame]
+ -[CSRestToOpenCoachingView _removeProgressAnimations]
+ -[CSRestToOpenCoachingView _touchIDGlyphImageWithPointSize:]
+ -[CSRestToOpenCoachingView _updateLabelAlpha]
+ -[CSRestToOpenCoachingView animationDidStop:finished:]
+ -[CSRestToOpenCoachingView fillWithDuration:]
+ -[CSRestToOpenCoachingView initWithFont:textColor:state:freshTouchRequired:]
+ -[CSRestToOpenCoachingView layoutSubviews]
+ -[CSRestToOpenCoachingView resetFill]
+ -[CSRestToOpenCoachingView setState:animated:]
+ -[CSRestToOpenCoachingView sizeThatFits:]
+ -[CSRestToOpenCoachingView state]
+ -[CSWidgetGridViewController setWantsLeadingAlignedContent:]
+ -[CSWidgetGridViewController wantsLeadingAlignedContent]
+ -[NCNotificationRequest(CoverSheet) cs_isEmergencyAlert]
+ -[UIView(CSDeviceConfiguration) cs_deviceDeterminedConfiguration]
+ -[_CSScreenEdgePanGestureRecognizer .cxx_destruct]
+ -[_CSScreenEdgePanGestureRecognizer interfaceOrientationDelegate]
+ -[_CSScreenEdgePanGestureRecognizer setInterfaceOrientationDelegate:]
+ GCC_except_table11
+ GCC_except_table112
+ GCC_except_table16
+ GCC_except_table214
+ GCC_except_table23
+ GCC_except_table255
+ GCC_except_table256
+ GCC_except_table380
+ GCC_except_table429
+ GCC_except_table453
+ GCC_except_table46
+ GCC_except_table466
+ GCC_except_table470
+ GCC_except_table48
+ GCC_except_table54
+ GCC_except_table555
+ GCC_except_table620
+ GCC_except_table640
+ GCC_except_table651
+ GCC_except_table68
+ GCC_except_table738
+ GCC_except_table795
+ GCC_except_table805
+ GCC_except_table807
+ GCC_except_table816
+ GCC_except_table831
+ GCC_except_table842
+ GCC_except_table881
+ _CACornerRadiiEqualToRadii
+ _CACornerRadiiUnset
+ _CATransform3DGetAffineTransform
+ _CSMagSafeRingCenterOffsetX
+ _CSMagSafeRingCenterOffsetY
+ _CSQuickActionsLayoutUsesSideButtons
+ _OBJC_CLASS_$_CAGradientLayer
+ _OBJC_CLASS_$_CAPresentationModifier
+ _OBJC_CLASS_$_CSCombinedListView
+ _OBJC_CLASS_$_CSComplicationColumnComponent
+ _OBJC_CLASS_$_CSDeviceDetermination
+ _OBJC_CLASS_$_CSFocusQuickAction
+ _OBJC_CLASS_$_CSHitBoxAddendumSwipeRecognizer
+ _OBJC_CLASS_$_CSRemoteContentCoordinator
+ _OBJC_CLASS_$_CSRestToOpenCoachingView
+ _OBJC_CLASS_$_NCNotificationRequest
+ _OBJC_CLASS_$_NSThread
+ _OBJC_CLASS_$_SBUIDeviceDeterminationTrait
+ _OBJC_CLASS_$_SBUIDeviceDeterminedConfiguration
+ _OBJC_CLASS_$_UICornerConfiguration
+ _OBJC_CLASS_$_UICornerRadius
+ _OBJC_IVAR_$_CSActivityManager._activityItemsByGroupingIdentifier
+ _OBJC_IVAR_$_CSActivityManager._avoidingFold
+ _OBJC_IVAR_$_CSBatteryChargingView._ringCenterOffset
+ _OBJC_IVAR_$_CSCombinedListView._hitBoxAddendumView
+ _OBJC_IVAR_$_CSCombinedListView._leftHitBoxAddendumRect
+ _OBJC_IVAR_$_CSCombinedListView._obstructingContentHitTester
+ _OBJC_IVAR_$_CSCombinedListView._rightHitBoxAddendumRect
+ _OBJC_IVAR_$_CSCombinedListViewController._foldAvoidanceHomeAffordanceComponent
+ _OBJC_IVAR_$_CSCombinedListViewController._hitBoxAddendumSwipeRecognizer
+ _OBJC_IVAR_$_CSCombinedListViewController._obstructingContentHitTester
+ _OBJC_IVAR_$_CSCombinedListViewController._permittedBounds
+ _OBJC_IVAR_$_CSCombinedListViewController._timeScrolledOffscreen
+ _OBJC_IVAR_$_CSComplicationManager._columnComplicationDescriptors
+ _OBJC_IVAR_$_CSComplicationManager._columnIconLayout
+ _OBJC_IVAR_$_CSComplicationManager._onColumnWidgetUpdate
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._dockFlyZResponseMultiplier
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._iconFlyZDistanceExponent
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._iconFlyZMaxDistance
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._iconFlyZMaxDistanceForPad
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._iconFlyZMaxDistanceForPhone
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._verticalDockCenterPointOffsetX
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._verticalDockCenterPointOffsetY
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._widgetLoomMinEligibleSize
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._widgetMaxLoomSize
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._widgetSpreadFactor
+ _OBJC_IVAR_$_CSCoverSheetSDFView._cornerRadiiOverride
+ _OBJC_IVAR_$_CSCoverSheetSDFView._cornerRadiiPresentationModifier
+ _OBJC_IVAR_$_CSCoverSheetSDFView._cornerRadiiPresentationModifierLock
+ _OBJC_IVAR_$_CSCoverSheetView._cachedPermittedBounds
+ _OBJC_IVAR_$_CSCoverSheetView._columnComplicationContainerView
+ _OBJC_IVAR_$_CSCoverSheetView._focusQuickActionView
+ _OBJC_IVAR_$_CSCoverSheetView._freezesPermittedBounds
+ _OBJC_IVAR_$_CSCoverSheetView._shouldClipBackgroundElements
+ _OBJC_IVAR_$_CSCoverSheetViewController.__subduedGlassAssertions
+ _OBJC_IVAR_$_CSCoverSheetViewController._appearanceDeviceClass
+ _OBJC_IVAR_$_CSCoverSheetViewController._columnComplicationContainerViewController
+ _OBJC_IVAR_$_CSCoverSheetViewController._didRegisterBiometricSuppressionObserver
+ _OBJC_IVAR_$_CSCoverSheetViewController._floatingLayerTransitionProgress
+ _OBJC_IVAR_$_CSCoverSheetViewController._hasAuxillaryContentObscuringCoverSheet
+ _OBJC_IVAR_$_CSCoverSheetViewController._opaqueContentAboveSubduedGlassAssertion
+ _OBJC_IVAR_$_CSCoverSheetViewController._permanentCompactTimeEnabled
+ _OBJC_IVAR_$_CSCoverSheetViewController._poseidonBiometricInaccessibleAssertion
+ _OBJC_IVAR_$_CSCoverSheetViewController._poseidonPasscodeNotVisibleAssertion
+ _OBJC_IVAR_$_CSCoverSheetViewController._realStatusBarAssertedMode
+ _OBJC_IVAR_$_CSCoverSheetViewController._realStatusBarModeAssertion
+ _OBJC_IVAR_$_CSCoverSheetViewController._restToOpenCoachingIdleTimer
+ _OBJC_IVAR_$_CSCoverSheetViewController._restToOpenCoachingView
+ _OBJC_IVAR_$_CSCoverSheetViewController._usingSubduedGlassTimeAppearance
+ _OBJC_IVAR_$_CSCoverSheetViewController._wantsLeadingAlignedContent
+ _OBJC_IVAR_$_CSDashBoardNotificationVersusPagingScrollSettings._allowsAuxiliaryScrollingWhileViscous
+ _OBJC_IVAR_$_CSDashBoardQuickActionsButtonSettings._alwaysOnFocusButtonAnimatesMove
+ _OBJC_IVAR_$_CSDashBoardQuickActionsButtonSettings._alwaysOnFocusButtonShowsMaterial
+ _OBJC_IVAR_$_CSDashBoardQuickActionsButtonSettings._alwaysOnFocusButtonSlides
+ _OBJC_IVAR_$_CSDashBoardQuickActionsButtonSettings._alwaysOnFocusButtonWhitepoint
+ _OBJC_IVAR_$_CSDashBoardQuickActionsButtonSettings._wantsConcentricityInAOD
+ _OBJC_IVAR_$_CSDashBoardScrollModifierSettings._marginSwipeDirectionMinimumTravel
+ _OBJC_IVAR_$_CSFixedFooterView._permittedBounds
+ _OBJC_IVAR_$_CSFocusQuickAction._accessibilityIdentifier
+ _OBJC_IVAR_$_CSFocusQuickAction._delegate
+ _OBJC_IVAR_$_CSFocusQuickAction._didFireForTouch
+ _OBJC_IVAR_$_CSFocusQuickAction._focusMode
+ _OBJC_IVAR_$_CSFocusQuickAction._previousFocusMode
+ _OBJC_IVAR_$_CSHitBoxAddendumSwipeRecognizer._addendumSwipeMinimumTravel
+ _OBJC_IVAR_$_CSHitBoxAddendumSwipeRecognizer._startingLocationInView
+ _OBJC_IVAR_$_CSHitBoxAddendumSwipeRecognizer._tracking
+ _OBJC_IVAR_$_CSMagSafeAccessory._accessoryType
+ _OBJC_IVAR_$_CSMagSafeSilhouetteConfiguration._aligningOrientation
+ _OBJC_IVAR_$_CSMainPageView._permittedBounds
+ _OBJC_IVAR_$_CSModalView._centralGroupLeadingConstraint
+ _OBJC_IVAR_$_CSModalView._centralGroupTrailingConstraint
+ _OBJC_IVAR_$_CSModalView._hasAppliedInsets
+ _OBJC_IVAR_$_CSModalView._lastInsetsBoundsSize
+ _OBJC_IVAR_$_CSModalView._lastInsetsButtonLayout
+ _OBJC_IVAR_$_CSModalView._wasRTL
+ _OBJC_IVAR_$_CSNotificationLegibilityDimController._usesPadStyleLayout
+ _OBJC_IVAR_$_CSPasscodeViewController._destinationScreen
+ _OBJC_IVAR_$_CSPasscodeViewController._poseidonViewController
+ _OBJC_IVAR_$_CSPasscodeViewController._unlockIntent
+ _OBJC_IVAR_$_CSPoseidonViewController._devicePoseProvider
+ _OBJC_IVAR_$_CSPoseidonViewController._screenOn
+ _OBJC_IVAR_$_CSQuickAction._togglesSelectionOnPress
+ _OBJC_IVAR_$_CSQuickActionImageGlyphView._overrideTintColor
+ _OBJC_IVAR_$_CSQuickActionsButton.animatedLayerProperties
+ _OBJC_IVAR_$_CSQuickActionsView._focusAction
+ _OBJC_IVAR_$_CSQuickActionsView._focusButton
+ _OBJC_IVAR_$_CSQuickActionsView._focusButtonHostView
+ _OBJC_IVAR_$_CSQuickActionsView._retainsFocusButtonInAOD
+ _OBJC_IVAR_$_CSQuickActionsViewController._activityManager
+ _OBJC_IVAR_$_CSQuickActionsViewController._activityManagerQueue
+ _OBJC_IVAR_$_CSQuickActionsViewController._activityPickerViewController
+ _OBJC_IVAR_$_CSQuickActionsViewController._focusAction
+ _OBJC_IVAR_$_CSRemoteContentCoordinator._authenticationStatusProvider
+ _OBJC_IVAR_$_CSRemoteContentCoordinator._coverSheetViewControllers
+ _OBJC_IVAR_$_CSRemoteContentCoordinator._sessionManager
+ _OBJC_IVAR_$_CSRemoteContentHostViewController._inlinePlatterWidth
+ _OBJC_IVAR_$_CSRemoteContentHostViewController._vendedContentBounds
+ _OBJC_IVAR_$_CSRemoteContentInlineView._didMoveToWindowHandler
+ _OBJC_IVAR_$_CSRemoteContentInlineViewController._lastSeenScreen
+ _OBJC_IVAR_$_CSRemoteContentInlineViewController._waitingForFreshContentFrame
+ _OBJC_IVAR_$_CSRestToOpenCoachingView._contentLineFrame
+ _OBJC_IVAR_$_CSRestToOpenCoachingView._contentView
+ _OBJC_IVAR_$_CSRestToOpenCoachingView._fullProgressFillDuration
+ _OBJC_IVAR_$_CSRestToOpenCoachingView._glyphImageView
+ _OBJC_IVAR_$_CSRestToOpenCoachingView._isFilling
+ _OBJC_IVAR_$_CSRestToOpenCoachingView._isFreshTouchRequired
+ _OBJC_IVAR_$_CSRestToOpenCoachingView._liftFingerLabel
+ _OBJC_IVAR_$_CSRestToOpenCoachingView._progressFillGradientLayer
+ _OBJC_IVAR_$_CSRestToOpenCoachingView._restToOpenLabel
+ _OBJC_IVAR_$_CSRestToOpenCoachingView._startProgressFillTime
+ _OBJC_IVAR_$_CSRestToOpenCoachingView._state
+ _OBJC_IVAR_$_CSWidgetGridViewController._wantsLeadingAlignedContent
+ _OBJC_IVAR_$__CSScreenEdgePanGestureRecognizer._interfaceOrientationDelegate
+ _OBJC_METACLASS_$_CSCombinedListView
+ _OBJC_METACLASS_$_CSComplicationColumnComponent
+ _OBJC_METACLASS_$_CSFocusQuickAction
+ _OBJC_METACLASS_$_CSHitBoxAddendumSwipeRecognizer
+ _OBJC_METACLASS_$_CSRemoteContentCoordinator
+ _OBJC_METACLASS_$_CSRestToOpenCoachingView
+ _SBSCurrentCoverDisplaySize
+ _UIRectInset
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NCNotificationRequest_$_CoverSheet
+ __OBJC_$_CATEGORY_NCNotificationRequest_$_CoverSheet
+ __OBJC_$_CLASS_METHODS_CSCombinedListViewController
+ __OBJC_$_CLASS_METHODS_CSComplicationColumnComponent
+ __OBJC_$_CLASS_METHODS_CSMagSafeAccessoryView
+ __OBJC_$_CLASS_METHODS_CSMagSafeSilhouetteConfiguration
+ __OBJC_$_CLASS_METHODS_CSModalView(Private)
+ __OBJC_$_CLASS_METHODS_CSRemoteContentCoordinator
+ __OBJC_$_INSTANCE_METHODS_CSCombinedListView
+ __OBJC_$_INSTANCE_METHODS_CSComplicationColumnComponent
+ __OBJC_$_INSTANCE_METHODS_CSFocusQuickAction
+ __OBJC_$_INSTANCE_METHODS_CSHitBoxAddendumSwipeRecognizer
+ __OBJC_$_INSTANCE_METHODS_CSRemoteContentCoordinator
+ __OBJC_$_INSTANCE_METHODS_CSRestToOpenCoachingView
+ __OBJC_$_INSTANCE_METHODS_UIView(CSCoverSheetViewBase|CSDeviceConfiguration|CSRegion)
+ __OBJC_$_INSTANCE_VARIABLES_CSCombinedListView
+ __OBJC_$_INSTANCE_VARIABLES_CSFocusQuickAction
+ __OBJC_$_INSTANCE_VARIABLES_CSHitBoxAddendumSwipeRecognizer
+ __OBJC_$_INSTANCE_VARIABLES_CSRemoteContentCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_CSRemoteContentInlineView
+ __OBJC_$_INSTANCE_VARIABLES_CSRestToOpenCoachingView
+ __OBJC_$_INSTANCE_VARIABLES__CSScreenEdgePanGestureRecognizer
+ __OBJC_$_PROP_LIST_CSActivityMetricsContextProviding
+ __OBJC_$_PROP_LIST_CSCombinedListView
+ __OBJC_$_PROP_LIST_CSFocusQuickAction
+ __OBJC_$_PROP_LIST_CSHitBoxAddendumSwipeRecognizer
+ __OBJC_$_PROP_LIST_CSRemoteContentCoordinator
+ __OBJC_$_PROP_LIST_CSRemoteContentInlineView
+ __OBJC_$_PROP_LIST_CSRestToOpenCoachingView
+ __OBJC_$_PROP_LIST__CSScreenEdgePanGestureRecognizer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivityMetricsContextProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivityPickerPresenter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSDevicePoseProviderObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSFocusQuickActionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSObstructingContentHitTesting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSBiometricSuppressionObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBFStatusBarManagerObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__CSScreenEdgePanGestureRecognizerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivityMetricsContextProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivityPickerPresenter
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSBiometricSuppressionObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSDevicePoseProviderObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSFocusQuickActionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSObstructingContentHitTesting
+ __OBJC_$_PROTOCOL_METHOD_TYPES__CSScreenEdgePanGestureRecognizerDelegate
+ __OBJC_$_PROTOCOL_REFS_CSActivityMetricsContextProviding
+ __OBJC_$_PROTOCOL_REFS_CSActivityPickerPresenter
+ __OBJC_$_PROTOCOL_REFS_CSBiometricSuppressionObserver
+ __OBJC_$_PROTOCOL_REFS_CSDevicePoseProviderObserver
+ __OBJC_$_PROTOCOL_REFS_CSFocusQuickActionDelegate
+ __OBJC_$_PROTOCOL_REFS_CSObstructingContentHitTesting
+ __OBJC_CLASS_PROTOCOLS_$_CSRemoteContentCoordinator
+ __OBJC_CLASS_PROTOCOLS_$_CSRestToOpenCoachingView
+ __OBJC_CLASS_RO_$_CSCombinedListView
+ __OBJC_CLASS_RO_$_CSComplicationColumnComponent
+ __OBJC_CLASS_RO_$_CSFocusQuickAction
+ __OBJC_CLASS_RO_$_CSHitBoxAddendumSwipeRecognizer
+ __OBJC_CLASS_RO_$_CSRemoteContentCoordinator
+ __OBJC_CLASS_RO_$_CSRestToOpenCoachingView
+ __OBJC_LABEL_PROTOCOL_$_CSActivityMetricsContextProviding
+ __OBJC_LABEL_PROTOCOL_$_CSActivityPickerPresenter
+ __OBJC_LABEL_PROTOCOL_$_CSBiometricSuppressionObserver
+ __OBJC_LABEL_PROTOCOL_$_CSDevicePoseProviderObserver
+ __OBJC_LABEL_PROTOCOL_$_CSFocusQuickActionDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSObstructingContentHitTesting
+ __OBJC_LABEL_PROTOCOL_$__CSScreenEdgePanGestureRecognizerDelegate
+ __OBJC_METACLASS_RO_$_CSCombinedListView
+ __OBJC_METACLASS_RO_$_CSComplicationColumnComponent
+ __OBJC_METACLASS_RO_$_CSFocusQuickAction
+ __OBJC_METACLASS_RO_$_CSHitBoxAddendumSwipeRecognizer
+ __OBJC_METACLASS_RO_$_CSRemoteContentCoordinator
+ __OBJC_METACLASS_RO_$_CSRestToOpenCoachingView
+ __OBJC_PROTOCOL_$_CSActivityMetricsContextProviding
+ __OBJC_PROTOCOL_$_CSActivityPickerPresenter
+ __OBJC_PROTOCOL_$_CSBiometricSuppressionObserver
+ __OBJC_PROTOCOL_$_CSDevicePoseProviderObserver
+ __OBJC_PROTOCOL_$_CSFocusQuickActionDelegate
+ __OBJC_PROTOCOL_$_CSObstructingContentHitTesting
+ __OBJC_PROTOCOL_$__CSScreenEdgePanGestureRecognizerDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_CSActivityPickerPresenter
+ __OBJC_PROTOCOL_REFERENCE_$_CSStateCoordinating
+ ___40-[CSQuickActionsView _layoutFocusButton]_block_invoke
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_8
+ ___43-[CSBatteryChargingRingView layoutSubviews]_block_invoke
+ ___44-[CSQuickActionsView _updateFocusButtonSlot]_block_invoke
+ ___44-[CSQuickActionsView _updateFocusButtonSlot]_block_invoke_2
+ ___44-[CSQuickActionsView _updateFocusButtonSlot]_block_invoke_3
+ ___44-[CSQuickActionsView _updateFocusButtonSlot]_block_invoke_4
+ ___46-[CSMagSafeAccessoryWalletView layoutSubviews]_block_invoke
+ ___46-[CSRestToOpenCoachingView setState:animated:]_block_invoke
+ ___47+[CSRemoteContentCoordinator sharedCoordinator]_block_invoke
+ ___47-[CSRemoteContentInlineViewController loadView]_block_invoke
+ ___56-[CSCoverSheetViewController _updateStatusBarBackground]_block_invoke
+ ___57-[CSCoverSheetViewController shouldShowLockStatusBarTime]_block_invoke
+ ___61-[CSCoverSheetSDFView _detachCornerRadiiPresentationModifier]_block_invoke
+ ___62-[CSCoverSheetSDFView _attachCornerRadiiPresentationModifier:]_block_invoke
+ ___62-[CSQuickActionsViewController _fetchFocusModeWithCompletion:]_block_invoke
+ ___62-[CSQuickActionsViewController _fetchFocusModeWithCompletion:]_block_invoke_2
+ ___63-[CSCoverSheetViewController _startRestToOpenCoachingIdleTimer]_block_invoke
+ ___65-[CSPasscodeViewController _createPoseidonViewControllerIfNeeded]_block_invoke
+ ___66-[CSBackgroundContentActionManager _invalidationHandlerForAction:]_block_invoke
+ ___66-[CSBackgroundContentActionManager _invalidationHandlerForAction:]_block_invoke_2
+ ___66-[CSQuickActionsViewController activeActivityDidChangeForManager:]_block_invoke
+ ___68-[CSRestToOpenCoachingView _animateContentToScale:duration:options:]_block_invoke
+ ___71-[CSRemoteContentInlineViewController didChangeRemoteHostContentFrame:]_block_invoke
+ ___73-[CSComplicationManager _updateComplicationsForActivePosterConfiguration]_block_invoke_4
+ ___88-[CSCoverSheetViewController _complicationsInterpretGestureRecognizerLocationAsContent:]_block_invoke_4
+ ___block_descriptor_104_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32s_e22_B16?0"CSAppearance"8ls32l8
+ ___block_descriptor_40_e8_32s_e32_v16?0"<FCActivityDescribing>"8ls32l8
+ ___block_descriptor_48_e54_v52?0"CALayer"8{CGRect={CGPoint=dd}{CGSize=dd}}16B48l
+ ___block_descriptor_48_e8_32s40bs_e21_v20?0"NSString"8B16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_64_e8_32s40w_e8_v12?0B8lw40l8s32l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0ls32l8r48l8r56l8r64l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___der_key_expert_tbm_support
+ _der_key_expert_tbm_support
+ _hypot
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sharedCoordinator.onceToken
+ _sharedCoordinator.sShared
- +[CSContentCutoutBoundsCalculator _contentCutoutBoundsForPortrait:forModal:]
- +[CSContentCutoutBoundsCalculator _normalizedContentCutoutForScreenBounds:contentBoundingRect:]
- +[CSContentCutoutBoundsCalculator _screenBoundsForPortrait:]
- +[CSInadvertentTouchIDRecognizerSettings settingsControllerModule]
- +[CSModalView _bottomBaselineOffsetForPortrait:]
- +[CSModalView _modalViewBottomBaselineOffsetPortrait]
- +[CSQuickActionsViewController deviceSupportsButtons]
- -[CSActivityManager _addAppActivitiesRecordForBundleId:activityItem:]
- -[CSActivityManager _clearAuthorizationOptionsIfNecessaryForGroupingIdentifier:]
- -[CSActivityManager _removeAppActivitiesRecordForBundleId:activityItem:]
- -[CSCoverSheetSDFView _layoutLayer:inBounds:withCornerRadius:]
- -[CSCoverSheetSDFView _layoutLayer:inBounds:withCornerRadius:horizontalOutset:]
- -[CSCoverSheetSDFView cornerRadius]
- -[CSCoverSheetView _maglevActive]
- -[CSCoverSheetView setClipping:corners:radius:]
- -[CSCoverSheetViewController _containsCachedBatteryDeviceWithIdenfifier:]
- -[CSCoverSheetViewController _inadvertentTouchIDRecognizerDidUpdate:]
- -[CSCoverSheetViewController _setupInadvertentTouchIDRecognizer]
- -[CSCoverSheetViewController _transitionTimerViewToVisible:animated:]
- -[CSCoverSheetViewController _updateRemoteContentInlineHorizontalMargin]
- -[CSCoverSheetViewController accessoryAnimationStatusChanged:]
- -[CSCoverSheetViewController activityCenter]
- -[CSCoverSheetViewController connectedDevicesDidChange:]
- -[CSCoverSheetViewController setActivityCenter:]
- -[CSCoverSheetViewController setTimerViewController:]
- -[CSCoverSheetViewController timerControllerDidStartTimer:]
- -[CSCoverSheetViewController timerControllerDidStopTimer:]
- -[CSCoverSheetViewController timerControllerDidUpdateTimer:]
- -[CSCoverSheetViewController timerViewController]
- -[CSInadvertentTouchIDRecognizer .cxx_destruct]
- -[CSInadvertentTouchIDRecognizer _debugLayerWithRect:cornerCutouts:color:]
- -[CSInadvertentTouchIDRecognizer _evaluateProtectionState]
- -[CSInadvertentTouchIDRecognizer _isActiveProtectionMode:]
- -[CSInadvertentTouchIDRecognizer _loadFromSettings:]
- -[CSInadvertentTouchIDRecognizer _protectionModeDescription:]
- -[CSInadvertentTouchIDRecognizer _removeDebugLayers]
- -[CSInadvertentTouchIDRecognizer _updateBiometricBlockState:]
- -[CSInadvertentTouchIDRecognizer _updateDebugViews]
- -[CSInadvertentTouchIDRecognizer _updateStrictCoverageState:]
- -[CSInadvertentTouchIDRecognizer _updateToChangedForReason:]
- -[CSInadvertentTouchIDRecognizer biometricAuthShouldBeBlocked]
- -[CSInadvertentTouchIDRecognizer canBePreventedByGestureRecognizer:]
- -[CSInadvertentTouchIDRecognizer canPreventGestureRecognizer:]
- -[CSInadvertentTouchIDRecognizer dealloc]
- -[CSInadvertentTouchIDRecognizer initWithTarget:action:]
- -[CSInadvertentTouchIDRecognizer lockScreenActive]
- -[CSInadvertentTouchIDRecognizer reset]
- -[CSInadvertentTouchIDRecognizer setLockScreenActive:]
- -[CSInadvertentTouchIDRecognizer setShowsViewDebugArea:]
- -[CSInadvertentTouchIDRecognizer settings:changedValueForKey:]
- -[CSInadvertentTouchIDRecognizer showsViewDebugArea]
- -[CSInadvertentTouchIDRecognizer strictCoverageRequired]
- -[CSInadvertentTouchIDRecognizer touchesBegan:withEvent:]
- -[CSInadvertentTouchIDRecognizer touchesCancelled:withEvent:]
- -[CSInadvertentTouchIDRecognizer touchesEnded:withEvent:]
- -[CSInadvertentTouchIDRecognizer touchesMoved:withEvent:]
- -[CSInadvertentTouchIDRecognizerSettings cornerAllowBottomLeftX]
- -[CSInadvertentTouchIDRecognizerSettings cornerAllowBottomLeftY]
- -[CSInadvertentTouchIDRecognizerSettings cornerAllowBottomRightX]
- -[CSInadvertentTouchIDRecognizerSettings cornerAllowBottomRightY]
- -[CSInadvertentTouchIDRecognizerSettings cornerAllowTopLeftX]
- -[CSInadvertentTouchIDRecognizerSettings cornerAllowTopLeftY]
- -[CSInadvertentTouchIDRecognizerSettings cornerAllowTopRightX]
- -[CSInadvertentTouchIDRecognizerSettings cornerAllowTopRightY]
- -[CSInadvertentTouchIDRecognizerSettings edgeProtectionBottomInset]
- -[CSInadvertentTouchIDRecognizerSettings edgeProtectionBottomMode]
- -[CSInadvertentTouchIDRecognizerSettings edgeProtectionLeftInset]
- -[CSInadvertentTouchIDRecognizerSettings edgeProtectionLeftMode]
- -[CSInadvertentTouchIDRecognizerSettings edgeProtectionRightInset]
- -[CSInadvertentTouchIDRecognizerSettings edgeProtectionRightMode]
- -[CSInadvertentTouchIDRecognizerSettings edgeProtectionTopInset]
- -[CSInadvertentTouchIDRecognizerSettings edgeProtectionTopMode]
- -[CSInadvertentTouchIDRecognizerSettings impermissibleTouchCountMode]
- -[CSInadvertentTouchIDRecognizerSettings impermissibleTouchCount]
- -[CSInadvertentTouchIDRecognizerSettings isEnabled]
- -[CSInadvertentTouchIDRecognizerSettings lockScreenActiveMode]
- -[CSInadvertentTouchIDRecognizerSettings setCornerAllowBottomLeftX:]
- -[CSInadvertentTouchIDRecognizerSettings setCornerAllowBottomLeftY:]
- -[CSInadvertentTouchIDRecognizerSettings setCornerAllowBottomRightX:]
- -[CSInadvertentTouchIDRecognizerSettings setCornerAllowBottomRightY:]
- -[CSInadvertentTouchIDRecognizerSettings setCornerAllowTopLeftX:]
- -[CSInadvertentTouchIDRecognizerSettings setCornerAllowTopLeftY:]
- -[CSInadvertentTouchIDRecognizerSettings setCornerAllowTopRightX:]
- -[CSInadvertentTouchIDRecognizerSettings setCornerAllowTopRightY:]
- -[CSInadvertentTouchIDRecognizerSettings setDefaultValues]
- -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionBottomInset:]
- -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionBottomMode:]
- -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionLeftInset:]
- -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionLeftMode:]
- -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionRightInset:]
- -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionRightMode:]
- -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionTopInset:]
- -[CSInadvertentTouchIDRecognizerSettings setEdgeProtectionTopMode:]
- -[CSInadvertentTouchIDRecognizerSettings setEnabled:]
- -[CSInadvertentTouchIDRecognizerSettings setImpermissibleTouchCount:]
- -[CSInadvertentTouchIDRecognizerSettings setImpermissibleTouchCountMode:]
- -[CSInadvertentTouchIDRecognizerSettings setLockScreenActiveMode:]
- -[CSInadvertentTouchIDRecognizerSettings setShowsViewDebugArea:]
- -[CSInadvertentTouchIDRecognizerSettings setTreatsRestrictiveAsBlocking:]
- -[CSInadvertentTouchIDRecognizerSettings showsViewDebugArea]
- -[CSInadvertentTouchIDRecognizerSettings treatsRestrictiveAsBlocking]
- -[CSLockScreenSettings inadvertentTouchIDRecognizerSettings]
- -[CSLockScreenSettings setInadvertentTouchIDRecognizerSettings:]
- -[CSMagSafeAccessory _getEmblemResourceURLForNFCType:]
- -[CSMagSafeAccessory emblemResourceURL]
- -[CSMagSafeAccessoryWalletEmblemView .cxx_destruct]
- -[CSMagSafeAccessoryWalletEmblemView _dismissAnimation]
- -[CSMagSafeAccessoryWalletEmblemView _presentAnimation]
- -[CSMagSafeAccessoryWalletEmblemView emblemView]
- -[CSMagSafeAccessoryWalletEmblemView initWithFrame:emblemResourceURL:]
- -[CSMagSafeAccessoryWalletEmblemView layoutSubviews]
- -[CSMagSafeAccessoryWalletEmblemView setEmblemView:]
- -[CSMagSafeRingConfiguration initWithRingDiameter:lineWidth:splashRingDiamter:]
- -[CSMagSafeSilhouetteConfiguration initWithSize:bottomOffset:cornerRadius:]
- -[CSMagSafeSilhouetteConfiguration initWithSize:bottomOffset:cornerRadius:roundedCorners:]
- -[CSNotificationLegibilityDimView layoutInsetsForSize:fadeAnchorY:]
- -[CSRemoteContentInlineViewController horizontalInsetMargin]
- -[CSRemoteContentInlineViewController setHorizontalInsetMargin:]
- -[CSTimerView .cxx_destruct]
- -[CSTimerView _newTimerDialForSettings:withFont:]
- -[CSTimerView _timerFont]
- -[CSTimerView _updateLegibilityStrength]
- -[CSTimerView accessoryView]
- -[CSTimerView dealloc]
- -[CSTimerView init]
- -[CSTimerView interItemSpacing]
- -[CSTimerView setEndDate:]
- -[CSTimerView setFont:]
- -[CSTimerView setLegibilitySettings:]
- -[CSTimerView settings:changedValueForKey:]
- -[CSTimerView timerText]
- -[CSTimerView updateTimerLabel]
- -[CSTimerViewController .cxx_destruct]
- -[CSTimerViewController _nextTimerChanged:]
- -[CSTimerViewController _startTimer]
- -[CSTimerViewController _stopTimerNotifyingDelegate:]
- -[CSTimerViewController _stopTimer]
- -[CSTimerViewController _updateNextTimer]
- -[CSTimerViewController _updateTimerFired]
- -[CSTimerViewController _updateTimerLabelView]
- -[CSTimerViewController dealloc]
- -[CSTimerViewController delegate]
- -[CSTimerViewController initWithNibName:bundle:]
- -[CSTimerViewController isEnabled]
- -[CSTimerViewController isEndDateValid]
- -[CSTimerViewController isTimerActive]
- -[CSTimerViewController loadView]
- -[CSTimerViewController setDelegate:]
- -[CSTimerViewController setEnabled:]
- -[CSTimerViewController setEndDate:]
- -[CSTimerViewController timerText]
- -[CSTimerViewController timerView]
- GCC_except_table10
- GCC_except_table104
- GCC_except_table14
- GCC_except_table15
- GCC_except_table195
- GCC_except_table221
- GCC_except_table235
- GCC_except_table356
- GCC_except_table39
- GCC_except_table419
- GCC_except_table430
- GCC_except_table434
- GCC_except_table45
- GCC_except_table51
- GCC_except_table512
- GCC_except_table576
- GCC_except_table596
- GCC_except_table607
- GCC_except_table65
- GCC_except_table689
- GCC_except_table755
- GCC_except_table765
- GCC_except_table767
- GCC_except_table776
- GCC_except_table791
- GCC_except_table8
- GCC_except_table802
- GCC_except_table839
- _MTTimerManagerNextTimerChanged
- _OBJC_CLASS_$_BSDateFormatterCache
- _OBJC_CLASS_$_BSUICAPackageView
- _OBJC_CLASS_$_CSInadvertentTouchIDRecognizer
- _OBJC_CLASS_$_CSInadvertentTouchIDRecognizerSettings
- _OBJC_CLASS_$_CSMagSafeAccessoryWalletEmblemView
- _OBJC_CLASS_$_CSTimerView
- _OBJC_CLASS_$_CSTimerViewController
- _OBJC_CLASS_$_MTTimer
- _OBJC_CLASS_$_MTTimerManager
- _OBJC_CLASS_$_SBLockScreenTimerDialView
- _OBJC_IVAR_$_CSActivityViewController._metricsProvider
- _OBJC_IVAR_$_CSCoverSheetSDFView._cornerRadius
- _OBJC_IVAR_$_CSCoverSheetViewController._activityCenter
- _OBJC_IVAR_$_CSCoverSheetViewController._cachedBatteryDevices
- _OBJC_IVAR_$_CSCoverSheetViewController._inadvertentTouchIDRecognizer
- _OBJC_IVAR_$_CSCoverSheetViewController._isAccessoryAnimationAllowed
- _OBJC_IVAR_$_CSCoverSheetViewController._remoteContentSessionManager
- _OBJC_IVAR_$_CSCoverSheetViewController._timerViewController
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._biometricAuthShouldBeBlocked
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowBottomLeftX
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowBottomLeftY
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowBottomRightX
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowBottomRightY
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowTopLeftX
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowTopLeftY
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowTopRightX
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._cornerAllowTopRightY
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionBottomInset
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionBottomLayer
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionBottomMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionLeftInset
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionLeftLayer
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionLeftMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionRightInset
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionRightLayer
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionRightMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionTopInset
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionTopLayer
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._edgeProtectionTopMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._enabled
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._impermissibleTouchCount
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._impermissibleTouchCountMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._lockScreenActive
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._lockScreenActiveMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._needsDebugViewUpdate
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._showsViewDebugArea
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._strictCoverageRequired
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._trackedTouches
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizer._treatsRestrictiveAsBlocking
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowBottomLeftX
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowBottomLeftY
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowBottomRightX
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowBottomRightY
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowTopLeftX
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowTopLeftY
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowTopRightX
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._cornerAllowTopRightY
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionBottomInset
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionBottomMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionLeftInset
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionLeftMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionRightInset
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionRightMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionTopInset
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._edgeProtectionTopMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._enabled
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._impermissibleTouchCount
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._impermissibleTouchCountMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._lockScreenActiveMode
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._showsViewDebugArea
- _OBJC_IVAR_$_CSInadvertentTouchIDRecognizerSettings._treatsRestrictiveAsBlocking
- _OBJC_IVAR_$_CSLockScreenSettings._inadvertentTouchIDRecognizerSettings
- _OBJC_IVAR_$_CSMagSafeAccessory._emblemResourceURL
- _OBJC_IVAR_$_CSMagSafeAccessoryWalletEmblemView._emblemView
- _OBJC_IVAR_$_CSRemoteContentInlineViewController._horizontalInsetMargin
- _OBJC_IVAR_$_CSTimerView._endDate
- _OBJC_IVAR_$_CSTimerViewController._delegate
- _OBJC_IVAR_$_CSTimerViewController._enabled
- _OBJC_IVAR_$_CSTimerViewController._endDate
- _OBJC_IVAR_$_CSTimerViewController._timerManager
- _OBJC_IVAR_$_CSTimerViewController._updateTimer
- _OBJC_METACLASS_$_CSInadvertentTouchIDRecognizer
- _OBJC_METACLASS_$_CSInadvertentTouchIDRecognizerSettings
- _OBJC_METACLASS_$_CSMagSafeAccessoryWalletEmblemView
- _OBJC_METACLASS_$_CSTimerView
- _OBJC_METACLASS_$_CSTimerViewController
- _OBJC_METACLASS_$_SBFLockScreenDateSubtitleView
- __OBJC_$_CLASS_METHODS_CSInadvertentTouchIDRecognizerSettings
- __OBJC_$_CLASS_METHODS_CSModalView
- __OBJC_$_INSTANCE_METHODS_CSInadvertentTouchIDRecognizer
- __OBJC_$_INSTANCE_METHODS_CSInadvertentTouchIDRecognizerSettings
- __OBJC_$_INSTANCE_METHODS_CSMagSafeAccessoryWalletEmblemView
- __OBJC_$_INSTANCE_METHODS_CSTimerView
- __OBJC_$_INSTANCE_METHODS_CSTimerViewController
- __OBJC_$_INSTANCE_METHODS_UIView(CSCoverSheetViewBase|CSRegion)
- __OBJC_$_INSTANCE_VARIABLES_CSInadvertentTouchIDRecognizer
- __OBJC_$_INSTANCE_VARIABLES_CSInadvertentTouchIDRecognizerSettings
- __OBJC_$_INSTANCE_VARIABLES_CSMagSafeAccessoryWalletEmblemView
- __OBJC_$_INSTANCE_VARIABLES_CSTimerView
- __OBJC_$_INSTANCE_VARIABLES_CSTimerViewController
- __OBJC_$_PROP_LIST_CSInadvertentTouchIDRecognizer
- __OBJC_$_PROP_LIST_CSInadvertentTouchIDRecognizerSettings
- __OBJC_$_PROP_LIST_CSMagSafeAccessoryWalletEmblemView
- __OBJC_$_PROP_LIST_CSTimerView
- __OBJC_$_PROP_LIST_CSTimerViewController
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSMagSafeAccessoryStatusDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSTimerViewControllerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSMagSafeAccessoryStatusDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSTimerViewControllerDelegate
- __OBJC_$_PROTOCOL_REFS_CSMagSafeAccessoryStatusDelegate
- __OBJC_CLASS_PROTOCOLS_$_CSInadvertentTouchIDRecognizer
- __OBJC_CLASS_PROTOCOLS_$_CSTimerView
- __OBJC_CLASS_RO_$_CSInadvertentTouchIDRecognizer
- __OBJC_CLASS_RO_$_CSInadvertentTouchIDRecognizerSettings
- __OBJC_CLASS_RO_$_CSMagSafeAccessoryWalletEmblemView
- __OBJC_CLASS_RO_$_CSTimerView
- __OBJC_CLASS_RO_$_CSTimerViewController
- __OBJC_LABEL_PROTOCOL_$_CSMagSafeAccessoryStatusDelegate
- __OBJC_LABEL_PROTOCOL_$_CSTimerViewControllerDelegate
- __OBJC_METACLASS_RO_$_CSInadvertentTouchIDRecognizer
- __OBJC_METACLASS_RO_$_CSInadvertentTouchIDRecognizerSettings
- __OBJC_METACLASS_RO_$_CSMagSafeAccessoryWalletEmblemView
- __OBJC_METACLASS_RO_$_CSTimerView
- __OBJC_METACLASS_RO_$_CSTimerViewController
- __OBJC_PROTOCOL_$_CSMagSafeAccessoryStatusDelegate
- __OBJC_PROTOCOL_$_CSTimerViewControllerDelegate
- ___41-[CSTimerViewController _updateNextTimer]_block_invoke
- ___41-[CSTimerViewController _updateNextTimer]_block_invoke_2
- ___47-[CSBackgroundContentActionManager _addAction:]_block_invoke
- ___47-[CSBackgroundContentActionManager _addAction:]_block_invoke_2
- ___51-[CSInadvertentTouchIDRecognizer _updateDebugViews]_block_invoke
- ___51-[CSInadvertentTouchIDRecognizer _updateDebugViews]_block_invoke_2
- ___56-[CSNotificationLegibilityDimController _updateDimViews]_block_invoke_3
- ___56-[CSNotificationLegibilityDimController _updateDimViews]_block_invoke_4
- ___56-[CSNotificationLegibilityDimController _updateDimViews]_block_invoke_5
- ___58-[CSInadvertentTouchIDRecognizer _evaluateProtectionState]_block_invoke
- ___58-[CSInadvertentTouchIDRecognizer _evaluateProtectionState]_block_invoke_2
- ___58-[CSInadvertentTouchIDRecognizer _evaluateProtectionState]_block_invoke_3
- ___62-[CSCoverSheetViewController accessoryAnimationStatusChanged:]_block_invoke
- ___69-[CSCoverSheetViewController _transitionTimerViewToVisible:animated:]_block_invoke
- ___block_descriptor_40_e8_32r_e8_Q16?0Q8lr32l8
- ___block_descriptor_40_e8_32s_e21_v20?0"NSString"8B16ls32l8
- ___block_descriptor_40_e8_32s_e29_v24?0"MTTimer"8"NSError"16ls32l8
- ___block_descriptor_40_e8_d16?0d8l
- ___block_descriptor_41_e8_32s_e14_"NSArray"8?0ls32l8
- ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8r48l8r56l8s40l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- _kCAFillRuleEvenOdd
CStrings:
+ "!#"
+ "%@-%p"
+ "9"
+ "?\v"
+ "Always On Focus Button"
+ "Animates Move"
+ "Aq"
+ "B16@?0@\"CSAppearance\"8"
+ "CSCoverSheetHideVerticalStatusBar"
+ "CSFocusQuickAction"
+ "CSNotifLegibilityDim no-dim: usesPad=%{BOOL}d dimVisible=%{BOOL}d fadeAnchorY=%.1f effectiveFadeInThreshold=%.1f fadeRadiusY=%.1f"
+ "CSNotifLegibilityDim ramp: usesPad=%{BOOL}d fadeAnchorY=%.1f effectiveFadeInThreshold=%.1f fullDimHeight=%.1f rangeStart=%.1f rangeEnd=%.1f progress=%.3f"
+ "CSPoseidonViewWindowPinning"
+ "CSRestToOpenCoachingFillAnimationKey"
+ "CSRestToOpenCoachingUnfillAnimationKey"
+ "ComplicationColumn"
+ "Concentric In AOD"
+ "CoverSheet legibility fadeRadiusY=%.1f localizedDimFrame=%{public}@"
+ "CoverSheetQuickAction"
+ "Dock Fly Z Response Multiplier"
+ "FOCUS_HINT_TEXT"
+ "FlexibleLockScreen"
+ "Focus Quick Action"
+ "Icon Fly Z Distance"
+ "Icon Fly Z Distance Exponent"
+ "Icon Fly Z Max Distance"
+ "Icon Fly Z Max Distance (Pad)"
+ "Icon Fly Z Max Distance (Phone)"
+ "Ionic"
+ "LIFT_FINGER_FOR_REST_TO_OPEN_SUBTITLE"
+ "Lock Screen will update to _usingSubduedGlassTimeAppearance: %{bool}u, reasons: %@"
+ "LockScreenSubduedGlassAppearance"
+ "LunaLeaf"
+ "Margin Scrolls (Vertical)"
+ "Minimum Travel"
+ "Moves To Corner"
+ "OpaqueContentAboveCoverSheet"
+ "Poster Switcher gesture not beginning because location for the gesture is in a column complication"
+ "REST_TO_OPEN_SUBTITLE"
+ "Received column widget update: %@"
+ "SBSceneRegionSceneExtension"
+ "Scroll From Margins While Locked"
+ "Setting cover sheet appearance for landscape: %{BOOL}d (effectiveDeviceClass: %ld)"
+ "Shows Material"
+ "V68"
+ "Vertical Dock Center Point Offset X"
+ "Vertical Dock Center Point Offset Y"
+ "Whiteness"
+ "Widget Loom Min Eligible Size"
+ "Widget Max Loom Size"
+ "Widget Spread Factor"
+ "[CSActivityManager] avoidingFold %{BOOL}u -> %{BOOL}u; invalidating %lu hosted activities"
+ "[Notification Long Press Gesture] Should finish long look transition via %{public}@ for notification %{public}@: [ pulled-down: %{BOOL}d revealed-history: %{BOOL}d face-detecting: %{BOOL}d face-detected: %{BOOL}d default-action: %{BOOL}d content-preview-always: %{BOOL}d authenticated: %{BOOL}d proximity-uncovered-after-wake: %{BOOL}d device-class: %ld override: %{BOOL}d ]: %{BOOL}d"
+ "[RemoteContent] CSRemoteContentHostViewController vending content bounds %{public}@ for interfaceOrientation %ld (windowScene: %d)"
+ "allowsAuxiliaryScrollingWhileViscous"
+ "alwaysOnFocusButtonAnimatesMove"
+ "alwaysOnFocusButtonShowsMaterial"
+ "alwaysOnFocusButtonSlides"
+ "alwaysOnFocusButtonWhitepoint"
+ "cornerRadii"
+ "dockFlyZResponseMultiplier"
+ "exclamationmark.circle"
+ "exclamationmark.circle.fill"
+ "exclamationmark.octagon.fill"
+ "exclamationmark.triangle"
+ "focus"
+ "focus-orb-button"
+ "focus-orb-button-%@"
+ "iconFlyZDistanceExponent"
+ "iconFlyZMaxDistance"
+ "iconFlyZMaxDistanceForPad"
+ "iconFlyZMaxDistanceForPhone"
+ "locations"
+ "marginSwipeDirectionMinimumTravel"
+ "touchid"
+ "v16@?0@\"<FCActivityDescribing>\"8"
+ "v52@?0@\"CALayer\"8{CGRect={CGPoint=dd}{CGSize=dd}}16B48"
+ "verticalDockCenterPointOffsetX"
+ "verticalDockCenterPointOffsetY"
+ "wantsConcentricityInAOD"
+ "widgetLoomMinEligibleSize"
+ "widgetMaxLoomSize"
+ "widgetSpreadFactor"
+ "\x91a"
+ "\xc1"
+ "\xf0\xf0\xa2\xf0\xf0\xf0\xc1"
- "%@%@"
- "("
- "4"
- "5+"
- "?\f"
- "Accessory animation status changed, isAnimationsAllowed: %{BOOL}u"
- "BLOCKING"
- "Block"
- "BlockBioAuth"
- "Bottom Inset %"
- "Bottom-Left X %"
- "Bottom-Left Y %"
- "Bottom-Right X %"
- "Bottom-Right Y %"
- "CSInadvertentTouchIDRecognizer"
- "Charge Ring Build"
- "Corner Allow Zones"
- "DoNothing"
- "Edge Bottom"
- "Edge Inset Protection"
- "Edge Left"
- "Edge Right"
- "Edge Top"
- "Enabled"
- "Impermissible Touch Count"
- "Inadvertent Settings"
- "Inadvertent TouchID Settings"
- "InadvertentTouchIDRecognizer - after load (treatsRestrictiveAsBlocking: %{BOOL}d)"
- "InadvertentTouchIDRecognizer - biometric block state changed: %{public}@"
- "InadvertentTouchIDRecognizer - escalating Restrictive to BlockBioAuth (treatsRestrictiveAsBlocking enabled)"
- "InadvertentTouchIDRecognizer - failed to update to changed for reason: %@"
- "InadvertentTouchIDRecognizer - protection state: %{public}@\n  contributors: [%{public}@]"
- "InadvertentTouchIDRecognizer - protection state: NONE (no active checks)"
- "InadvertentTouchIDRecognizer - settings changed key: %{public}@ (treatsRestrictiveAsBlocking: %{BOOL}d, trackedTouches: %lu, blocked: %{BOOL}d, strict: %{BOOL}d)"
- "InadvertentTouchIDRecognizer - strict coverage state changed: %{public}@"
- "Left Inset %"
- "Lock Screen Active"
- "No Impact"
- "Out"
- "Protection Modes"
- "Q16@?0Q8"
- "RESTRICTIVE"
- "Received next timer changed notification: %{public}@"
- "Restrictive"
- "Right Inset %"
- "Setting next timer: %{public}@ with trigger: %{public}@"
- "Started update timer: %{public}@"
- "Starting update timer..."
- "Stopping update timer: %@"
- "Timer Controller did start timer."
- "Timer Controller did stop timer."
- "Timer end date is invalid or nil."
- "TimerView"
- "Top Inset %"
- "Top-Left X %"
- "Top-Left Y %"
- "Top-Right X %"
- "Top-Right Y %"
- "Touch Count"
- "Treat Restrictive as Blocking"
- "Unable to start update timer with end date: %{public}@"
- "Update timer fired with end date: %{public}@"
- "[CSCSVC][RemoteContent] Forcefully removing stale remote session %{public}@"
- "[Charge UI][Novel Packs] visible YES, showBattery YES – isAlreadyShowingChargingModal: %d"
- "[Charge UI][Novel Packs] – endedShowingChargingModal: %d"
- "[Charge UI][Removed Packs] visible YES, showBattery NO – isAlreadyShowingChargingModal: %d"
- "[Charge UI][Removed Packs] – endedShowingChargingModal: %d"
- "[Notification Long Press Gesture] Should finish long look transition via %{public}@ for notification %{public}@: [ pulled-down: %{BOOL}d revealed-history: %{BOOL}d face-detecting: %{BOOL}d face-detected: %{BOOL}d default-action: %{BOOL}d content-preview-always: %{BOO}d authenticated: %{BOOL}d proximity-uncovered-after-wake: %{BOOL}d override: %{BOOL}d ]: %{BOOL}d"
- "cornerAllowBottomLeftX"
- "cornerAllowBottomLeftY"
- "cornerAllowBottomRightX"
- "cornerAllowBottomRightY"
- "cornerAllowTopLeftX"
- "cornerAllowTopLeftY"
- "cornerAllowTopRightX"
- "cornerAllowTopRightY"
- "edgeProtectionBottom(%@): touch at (%.1f, %.1f) inside bottom inset"
- "edgeProtectionBottomInset"
- "edgeProtectionBottomMode"
- "edgeProtectionLeft(%@): touch at (%.1f, %.1f) inside left inset"
- "edgeProtectionLeftInset"
- "edgeProtectionLeftMode"
- "edgeProtectionRight(%@): touch at (%.1f, %.1f) inside right inset"
- "edgeProtectionRightInset"
- "edgeProtectionRightMode"
- "edgeProtectionTop(%@): touch at (%.1f, %.1f) inside top inset"
- "edgeProtectionTopInset"
- "edgeProtectionTopMode"
- "impermissibleTouchCount"
- "impermissibleTouchCount(%@): %lu touches >= threshold %lu"
- "impermissibleTouchCountMode"
- "inadvertentTouchIDRecognizer didUpdate biometricBlock: %{BOOL}d (delegate: %{public}@)"
- "inadvertentTouchIDRecognizerSettings"
- "lockScreenActive(%@)"
- "lockScreenActiveMode"
- "showsViewDebugArea"
- "treatsRestrictiveAsBlocking"
- "updateBiometricBlockState"
- "updateStrictCoverageState"
- "v24@?0@\"MTTimer\"8@\"NSError\"16"
- "wallet-inset-zeus"
- "\xb1"
- "\u200f%@%@"
- "\xf0\xf0b\xf0\xf0\xf0\xa1"
```
