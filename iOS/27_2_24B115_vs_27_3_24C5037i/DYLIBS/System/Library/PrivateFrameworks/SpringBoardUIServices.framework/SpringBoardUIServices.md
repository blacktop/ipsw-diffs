## SpringBoardUIServices

> `/System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices`

```diff

-4637.1.14.103.0
-  __TEXT.__text: 0x9e924
-  __TEXT.__objc_methlist: 0xe94c
-  __TEXT.__const: 0xb48
-  __TEXT.__gcc_except_tab: 0x988
-  __TEXT.__cstring: 0xac52
+4637.2.11.104.0
+  __TEXT.__text: 0xa7454
+  __TEXT.__objc_methlist: 0xf72c
+  __TEXT.__const: 0xbb0
+  __TEXT.__gcc_except_tab: 0xa1c
+  __TEXT.__cstring: 0xaec3
   __TEXT.__dlopen_cstrs: 0x42e
   __TEXT.__ustring: 0x4
-  __TEXT.__oslogstring: 0x4802
-  __TEXT.__unwind_info: 0x3fc8
+  __TEXT.__oslogstring: 0x4e6f
+  __TEXT.__unwind_info: 0x4338
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2be8
-  __DATA_CONST.__objc_classlist: 0x998
+  __DATA_CONST.__const: 0x2d38
+  __DATA_CONST.__objc_classlist: 0x9f0
   __DATA_CONST.__objc_catlist: 0xd8
-  __DATA_CONST.__objc_protolist: 0x4a8
+  __DATA_CONST.__objc_protolist: 0x4d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d00
-  __DATA_CONST.__objc_protorefs: 0x140
-  __DATA_CONST.__objc_superrefs: 0x5f8
+  __DATA_CONST.__objc_selrefs: 0x8478
+  __DATA_CONST.__objc_protorefs: 0x150
+  __DATA_CONST.__objc_superrefs: 0x610
   __DATA_CONST.__objc_arraydata: 0x110
-  __DATA_CONST.__got: 0x10c8
-  __AUTH_CONST.__const: 0x9e0
-  __AUTH_CONST.__cfstring: 0xa340
-  __AUTH_CONST.__objc_const: 0x2db60
+  __DATA_CONST.__got: 0x1140
+  __AUTH_CONST.__const: 0xa40
+  __AUTH_CONST.__cfstring: 0xa600
+  __AUTH_CONST.__objc_const: 0x2f9c8
   __AUTH_CONST.__objc_doubleobj: 0x160
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x5118
-  __DATA.__objc_ivar: 0xd40
-  __DATA.__data: 0x3810
+  __AUTH.__objc_data: 0x5488
+  __DATA.__objc_ivar: 0xe2c
+  __DATA.__data: 0x39f0
   __DATA_DIRTY.__objc_data: 0xed8
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x8

   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SPOwner.framework/SPOwner
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
+  - /System/Library/PrivateFrameworks/ShellSceneKit.framework/ShellSceneKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4821
-  Symbols:   9460
-  CStrings:  1830
+  Functions: 5091
+  Symbols:   9886
+  CStrings:  1881
 
Symbols:
+ +[SBLightPasscodeNumberPadButton _numberPadButtonOuterCircleDiameterForScreen:]
+ +[SBLightPasscodeNumberPadButton defaultSizeForScreen:]
+ +[SBLightPasscodeNumberPadButton outerCircleDiameter]
+ +[SBPasscodeNumberPadButton _isPortraitForScreen:]
+ +[SBPasscodeNumberPadButton _numberPadButtonOuterCircleDiameterForScreen:]
+ +[SBPasscodeNumberPadButton _sizingScreen]
+ +[SBPasscodeNumberPadButton _withSizingScreen:perform:]
+ +[SBPasscodeNumberPadButton defaultSizeForScreen:]
+ +[SBPasscodeNumberPadButton outerCircleDiameterForScreen:]
+ +[SBPasscodeNumberPadButton paddingOutsideRingForScreen:]
+ +[SBSUIDisplayYoinkingSceneExtension clientSettingsExtensions]
+ +[SBSUIDisplayYoinkingSceneExtension hostComponents]
+ +[SBSUIDisplayYoinkingSceneExtension settingsExtensions]
+ +[SBSUIRemoteAlertClientSettingsExtension configureSetting:]
+ +[SBSUISurfaceTypeSceneExtension clientComponents]
+ +[SBSUISurfaceTypeSceneExtension propagateToSceneWithDefinition:]
+ +[SBUIDeviceDeterminedConfiguration _configurationFromScreenSize:nativeBounds:scale:nativeScale:]
+ +[SBUIDeviceDeterminedConfiguration _configurationFromScreenSize:nativeBounds:surfaceType:scale:nativeScale:]
+ +[SBUIDeviceDeterminedConfiguration _configurationFromWindowScene:surfaceType:]
+ +[SBUIDeviceDeterminedConfiguration configurationFromDisplayConfigurationContext:]
+ +[SBUIDeviceDeterminedConfiguration configurationFromWindowScene:]
+ +[SBUIDisplayActivationTrackingSceneExtension hostComponents]
+ +[SBUIPasscodeLockNumberPad _buttonForCharacter:withLightStyle:screen:]
+ +[SBUIPasscodeLockNumberPad _desiredFrameForNumberPad:screen:]
+ +[SBUIPasscodeLockNumberPad _inputButtonCircleSizeForScreen:]
+ +[SBUIPasscodeLockNumberPad _inputButtonCircleSpacingForScreen:]
+ +[SBUIPasscodeLockViewFactory _passcodeLockViewForStyle:withLightStyle:dimmed:screen:]
+ +[SBUIPasscodeLockViewFactory installTonightPasscodeLockViewForUsersCurrentStyleDestinationScreen:]
+ +[SBUIPasscodeLockViewFactory lightPasscodeLockViewForStyle:destinationScreen:]
+ +[SBUIPasscodeLockViewFactory lightPasscodeLockViewForUsersCurrentStyleDestinationScreen:]
+ +[SBUIPasscodeLockViewFactory passcodeLockViewForStyle:destinationScreen:]
+ +[SBUIPasscodeLockViewFactory passcodeLockViewForUsersCurrentStyleDestinationScreen:]
+ +[SBUIPasscodeLockViewFactory undimmedLightPasscodeLockViewForStyle:destinationScreen:]
+ +[SBUIPasscodeLockViewFactory undimmedLightPasscodeLockViewForUsersCurrentStyleDestinationScreen:]
+ +[SBUIPasscodeLockViewFactory undimmedPasscodeLockViewForStyle:destinationScreen:]
+ +[SBUIPasscodeLockViewFactory undimmedPasscodeLockViewForUsersCurrentStyleDestinationScreen:]
+ +[_SBSUIDisplayYoinkingWindow _isSecure]
+ -[FBSScene(SBSUISurfaceTypeClient) sbsui_surfaceTypeClient]
+ -[SBSUIDisplayYoinkingSceneComponent .cxx_destruct]
+ -[SBSUIDisplayYoinkingSceneComponent _reportSlideStateOfViewController:]
+ -[SBSUIDisplayYoinkingSceneComponent _sceneWillInvalidate:]
+ -[SBSUIDisplayYoinkingSceneComponent _scene]
+ -[SBSUIDisplayYoinkingSceneComponent _setScene:]
+ -[SBSUIDisplayYoinkingSceneComponent displayYoinkingViewControllerDidBeginInteraction:]
+ -[SBSUIDisplayYoinkingSceneComponent displayYoinkingViewControllerDidBeginSlide:]
+ -[SBSUIDisplayYoinkingSceneComponent displayYoinkingViewControllerDidCancelSlide:]
+ -[SBSUIDisplayYoinkingSceneComponent displayYoinkingViewControllerDidChangePastSwapThreshold:]
+ -[SBSUIDisplayYoinkingSceneComponent displayYoinkingViewControllerDidChangePastTouchBlockingThreshold:]
+ -[SBSUIDisplayYoinkingSceneComponent displayYoinkingViewControllerDidCompleteSlide:]
+ -[SBSUIDisplayYoinkingSceneComponent displayYoinkingViewControllerDidEndInteraction:]
+ -[SBSUIDisplayYoinkingSceneComponent initWithScene:]
+ -[SBSUIDisplayYoinkingSceneComponent scene:didUpdateSettings:]
+ -[SBSUIDisplayYoinkingSceneHostComponent .cxx_destruct]
+ -[SBSUIDisplayYoinkingSceneHostComponent _handleSliderStateChangeToPhase:pastSwapThreshold:pastTouchBlockingThreshold:interacting:]
+ -[SBSUIDisplayYoinkingSceneHostComponent delegate]
+ -[SBSUIDisplayYoinkingSceneHostComponent scene:didUpdateClientSettings:]
+ -[SBSUIDisplayYoinkingSceneHostComponent sceneWillDeactivate:withContext:]
+ -[SBSUIDisplayYoinkingSceneHostComponent setDelegate:]
+ -[SBSUIDisplayYoinkingSceneHostComponent slidePhase]
+ -[SBSUIDisplayYoinkingSceneSpecification affectsAppLifecycleIfInternal]
+ -[SBSUIDisplayYoinkingSceneSpecification affectsScreenOrientation]
+ -[SBSUIDisplayYoinkingSceneSpecification baseSceneComponentClassDictionary]
+ -[SBSUIDisplayYoinkingSceneSpecification defaultExtensions]
+ -[SBSUIDisplayYoinkingSceneSpecification isInternal]
+ -[SBSUIDisplayYoinkingSceneSpecification uiSceneSessionRole]
+ -[SBSUIDisplayYoinkingViewController .cxx_destruct]
+ -[SBSUIDisplayYoinkingViewController _canShowWhileLocked]
+ -[SBSUIDisplayYoinkingViewController _cancelSlideIfPending]
+ -[SBSUIDisplayYoinkingViewController _createActionSlider]
+ -[SBSUIDisplayYoinkingViewController _createDimmingBackdropViewWithFrame:]
+ -[SBSUIDisplayYoinkingViewController _dimmingTintAlphaForProgress:]
+ -[SBSUIDisplayYoinkingViewController _pixelAlignedValue:]
+ -[SBSUIDisplayYoinkingViewController _rebuildActionSlider]
+ -[SBSUIDisplayYoinkingViewController _rebuildDimmingBackdropView]
+ -[SBSUIDisplayYoinkingViewController _setFeedbackGeneratorActive:]
+ -[SBSUIDisplayYoinkingViewController _setTouchesActive:]
+ -[SBSUIDisplayYoinkingViewController _sliderConfigurationWithTrackHeight:trackWidth:titleFont:titleLeadingInset:]
+ -[SBSUIDisplayYoinkingViewController _sliderDidCompleteSlide]
+ -[SBSUIDisplayYoinkingViewController _sliderDidUpdateProgress:]
+ -[SBSUIDisplayYoinkingViewController _sliderSystemImageName]
+ -[SBSUIDisplayYoinkingViewController _sliderTitleFont]
+ -[SBSUIDisplayYoinkingViewController _sliderTitle]
+ -[SBSUIDisplayYoinkingViewController _sliderTrackHeight]
+ -[SBSUIDisplayYoinkingViewController _updatePastSwapThresholdForProgress:]
+ -[SBSUIDisplayYoinkingViewController _updatePastTouchBlockingThresholdForProgress:]
+ -[SBSUIDisplayYoinkingViewController dealloc]
+ -[SBSUIDisplayYoinkingViewController delegate]
+ -[SBSUIDisplayYoinkingViewController initWithSettings:delegate:]
+ -[SBSUIDisplayYoinkingViewController isInteracting]
+ -[SBSUIDisplayYoinkingViewController isPastSwapThreshold]
+ -[SBSUIDisplayYoinkingViewController isPastTouchBlockingThreshold]
+ -[SBSUIDisplayYoinkingViewController setDelegate:]
+ -[SBSUIDisplayYoinkingViewController setSettings:]
+ -[SBSUIDisplayYoinkingViewController settings]
+ -[SBSUIDisplayYoinkingViewController slidePhase]
+ -[SBSUIDisplayYoinkingViewController supportedInterfaceOrientations]
+ -[SBSUIDisplayYoinkingViewController viewDidLayoutSubviews]
+ -[SBSUIDisplayYoinkingViewController viewDidLoad]
+ -[SBSUIDuoDisplaySceneRequestBuilder _specification]
+ -[SBSUIDuoDisplaySceneSpecification uiSceneSessionRole]
+ -[SBSUIRemoteAlertScene setMovesAutomaticallyToPrimaryDisplay:]
+ -[SBSUIRemoteAlertSceneHostComponent movesAutomaticallyToPrimaryDisplay]
+ -[SBSUIRemoteAlertSceneHostComponent preferredStatusBarAxis]
+ -[SBSUIRemoteAlertSceneHostComponent setDefaultStatusBarHeightsForStatusBarProvider:]
+ -[SBSUISurfaceTypeClientComponent .cxx_destruct]
+ -[SBSUISurfaceTypeClientComponent _notifyObservers:surfaceTypeChange:]
+ -[SBSUISurfaceTypeClientComponent addSurfaceTypeObserver:]
+ -[SBSUISurfaceTypeClientComponent removeSurfaceTypeObserver:]
+ -[SBSUISurfaceTypeClientComponent sbsui_surfaceType]
+ -[SBSUISurfaceTypeClientComponent scene:didUpdateSettings:]
+ -[SBSUISurfaceTypeClientComponent scene:surfaceTypeDidUpdate:]
+ -[SBSimplePasscodeEntryFieldButton paddingOutsideRing]
+ -[SBSimplePasscodeEntryFieldButton setPaddingOutsideRing:]
+ -[SBUIAlphanumericPasscodeEntryField initWithDefaultSizeAndLightStyle:screen:]
+ -[SBUIBiometricResource _effectiveLockoutStateWithBaseState:]
+ -[SBUIBiometricResource _notifyObserversOfMesaOcclusionChange]
+ -[SBUIBiometricResource _operation:failedToStartForAssertion:withError:]
+ -[SBUIBiometricResource _restartMatchOperationsForStrictTouchCoverageIfNeeded]
+ -[SBUIBiometricResource _restartMatchOperationsForStrictTouchCoverage]
+ -[SBUIBiometricResource _updateFingerPresenceIfNeededWithOperations:]
+ -[SBUIBiometricResource acquireMesaOcclusionAssertionForReason:]
+ -[SBUIBiometricResource biometricKitInterface:fingerPresenceDidChange:]
+ -[SBUIBiometricResource biometricLockoutStateForDeviceKind:]
+ -[SBUIBiometricResource hasAuthenticationCapabilityEnabledForDeviceKind:]
+ -[SBUIBiometricResource isMesaOccluded]
+ -[SBUIBiometricResource requiresFaceIDLatencyMitigation]
+ -[SBUILongNumericPasscodeEntryField initWithDefaultSizeAndLightStyle:screen:]
+ -[SBUINumericPasscodeEntryFieldBase initWithDefaultSizeAndLightStyle:screen:]
+ -[SBUIPasscodeBiometricAuthenticationView _isPoseidonPhoneAuthentication]
+ -[SBUIPasscodeBiometricAuthenticationView _updatePhoneScreenBasedConstraintConstants]
+ -[SBUIPasscodeBiometricAuthenticationView _updatePhoneScreenBasedConstraintsScreen:]
+ -[SBUIPasscodeBiometricAuthenticationView cancelButtonCenterXConstraint]
+ -[SBUIPasscodeBiometricAuthenticationView cancelButtonCenterYConstraint]
+ -[SBUIPasscodeBiometricAuthenticationView centeredContentHelperGuide]
+ -[SBUIPasscodeBiometricAuthenticationView emergencyButtonCenterXConstraint]
+ -[SBUIPasscodeBiometricAuthenticationView hasPoseidonSupport]
+ -[SBUIPasscodeBiometricAuthenticationView layoutDelegateDidUpdateValues:screen:]
+ -[SBUIPasscodeBiometricAuthenticationView setCancelButtonCenterXConstraint:]
+ -[SBUIPasscodeBiometricAuthenticationView setCancelButtonCenterYConstraint:]
+ -[SBUIPasscodeBiometricAuthenticationView setCenteredContentHelperGuide:]
+ -[SBUIPasscodeBiometricAuthenticationView setEmergencyButtonCenterXConstraint:]
+ -[SBUIPasscodeBiometricAuthenticationView setHasPoseidonSupport:]
+ -[SBUIPasscodeBiometricAuthenticationView setUsePasscodeButton:]
+ -[SBUIPasscodeBiometricAuthenticationView setUsePasscodeButtonVisible:]
+ -[SBUIPasscodeBiometricAuthenticationView updateConstraints]
+ -[SBUIPasscodeBiometricAuthenticationView usePasscodeButtonVisible]
+ -[SBUIPasscodeBiometricAuthenticationView usePasscodeButton]
+ -[SBUIPasscodeBiometricResource acquireMesaOcclusionAssertionForReason:]
+ -[SBUIPasscodeBiometricResource biometricLockoutStateForDeviceKind:]
+ -[SBUIPasscodeBiometricResource hasAuthenticationCapabilityEnabledForDeviceKind:]
+ -[SBUIPasscodeBiometricResource isMesaOccluded]
+ -[SBUIPasscodeEntryField initWithDefaultSizeAndLightStyle:screen:]
+ -[SBUIPasscodeLockNumberPad _distanceToTopOfFirstButtonForScreen:]
+ -[SBUIPasscodeLockNumberPad _effectiveDeviceClass]
+ -[SBUIPasscodeLockNumberPad _effectiveScreen]
+ -[SBUIPasscodeLockNumberPad _tightNumberPadHeight]
+ -[SBUIPasscodeLockNumberPad _updateAncillaryButtonOffsetForCurrentScreen]
+ -[SBUIPasscodeLockNumberPad _updateAncillaryButtonOffsetForScreen:isPortrait:]
+ -[SBUIPasscodeLockNumberPad _updateNumberPadLayout]
+ -[SBUIPasscodeLockNumberPad desiredFrame]
+ -[SBUIPasscodeLockNumberPad didMoveToWindow]
+ -[SBUIPasscodeLockNumberPad initWithDefaultSizeAndLightStyle:screen:]
+ -[SBUIPasscodeLockNumberPad layoutSubviews]
+ -[SBUIPasscodeLockNumberPad nonUniversalOffsetY]
+ -[SBUIPasscodeLockNumberPad setDesiredFrame:]
+ -[SBUIPasscodeLockNumberPad setNonUniversalOffsetY:]
+ -[SBUIPasscodeLockNumberPad updateConstraints]
+ -[SBUIPasscodeLockViewBase _effectiveDeviceClass]
+ -[SBUIPasscodeLockViewBase _isPoseidonPhone]
+ -[SBUIPasscodeLockViewBase _isV68DeviceClass]
+ -[SBUIPasscodeLockViewBase _permittedBoundsForRegions:]
+ -[SBUIPasscodeLockViewBase _updatePoseidonCoachingLabelVisibility]
+ -[SBUIPasscodeLockViewBase _updateValuesForLayoutDelegate]
+ -[SBUIPasscodeLockViewBase biometricResource:mesaOcclusionDidChange:]
+ -[SBUIPasscodeLockViewBase passcodeBiometricAuthenticationViewNumberPadAncillaryButtonOffset:fromTopOfScreen:]
+ -[SBUIPasscodeLockViewBase setUnlockIntent:]
+ -[SBUIPasscodeLockViewBase unlockIntent]
+ -[SBUIPasscodeLockViewInstallTonightLongNumericKeypad initWithLightStyle:providesDimming:screen:]
+ -[SBUIPasscodeLockViewLongNumericKeypad .cxx_destruct]
+ -[SBUIPasscodeLockViewLongNumericKeypad _newEntryFieldForScreen:]
+ -[SBUIPasscodeLockViewLongNumericKeypad initWithLightStyle:providesDimming:screen:]
+ -[SBUIPasscodeLockViewSimpleFixedDigitKeypad _newEntryFieldForScreen:]
+ -[SBUIPasscodeLockViewSimpleFixedDigitKeypad initWithLightStyle:providesDimming:numberOfDigits:screen:]
+ -[SBUIPasscodeLockViewWithKeyboard _effectiveScreen]
+ -[SBUIPasscodeLockViewWithKeyboard didMoveToWindow]
+ -[SBUIPasscodeLockViewWithKeyboard initWithLightStyle:pinKeyboardToBottom:screen:]
+ -[SBUIPasscodeLockViewWithKeyboard initWithLightStyle:screen:]
+ -[SBUIPasscodeLockViewWithKeypad _defaultEntryFieldPositionForBounds:]
+ -[SBUIPasscodeLockViewWithKeypad _effectiveScreen]
+ -[SBUIPasscodeLockViewWithKeypad _newEntryFieldForScreen:]
+ -[SBUIPasscodeLockViewWithKeypad _permittedBoundsOffsetYForNumberPad:]
+ -[SBUIPasscodeLockViewWithKeypad didMoveToWindow]
+ -[SBUIPasscodeLockViewWithKeypad initWithLightStyle:providesDimming:screen:]
+ -[SBUIPasscodeLockViewWithKeypad passcodeLockNumberPadDidUpdateLayout:]
+ -[SBUIPhoneUnlockWithWatchController _hardwareHasFaceRequirements]
+ -[SBUIPhoneUnlockWithWatchController acquireUnlockSuppressionAssertionForReason:]
+ -[SBUIPoseidonContainerViewController _addSuppressionAssertion:]
+ -[SBUIPoseidonContainerViewController _applyEffectiveCoachingSuppressionLevel]
+ -[SBUIPoseidonContainerViewController _effectiveCoachingSuppressionLevel]
+ -[SBUIPoseidonContainerViewController _isHingeOpenOnCoverSurface]
+ -[SBUIPoseidonContainerViewController _removeSuppressionAssertion:]
+ -[SBUIPoseidonContainerViewController _surfaceType]
+ -[SBUIPoseidonContainerViewController _updateIconViewState]
+ -[SBUIPoseidonContainerViewController acquireCoachingSuppressionAssertionWithLevel:]
+ -[SBUIPoseidonContainerViewController devicePose]
+ -[SBUIPoseidonContainerViewController isCoachingLabelVisible]
+ -[SBUIPoseidonContainerViewController overrideSurfaceType]
+ -[SBUIPoseidonContainerViewController setCoachingLabelVisible:]
+ -[SBUIPoseidonContainerViewController setCoachingSuppressed:]
+ -[SBUIPoseidonContainerViewController setDevicePose:]
+ -[SBUIPoseidonContainerViewController setOverrideSurfaceType:]
+ -[SBUIPoseidonContainerViewController viewDidMoveToWindow:shouldAppearOrDisappear:]
+ -[SBUIPoseidonIconView _coachingLabelTargetAlpha]
+ -[SBUIPoseidonIconView _currentOrientation]
+ -[SBUIPoseidonIconView _deviceClass]
+ -[SBUIPoseidonIconView _hasIntersectingUI]
+ -[SBUIPoseidonIconView _intersectionOffset]
+ -[SBUIPoseidonIconView columnFrame]
+ -[SBUIPoseidonIconView isCoachingLabelVisible]
+ -[SBUIPoseidonIconView setCoachingLabelVisible:]
+ -[SBUIPoseidonIconView setColumnFrame:]
+ -[SBUIProudLockContainerViewController _shouldShowCoachingForBiometricMatchFailure]
+ -[SBUISActivityMetrics _ambientWidgetScaleFactor]
+ -[SBUISActivityMetrics _innerSurfaceWidgetCardItemMetricsWithAvailableWidth:screen:]
+ -[SBUISActivityMetrics _isCoverSurface]
+ -[SBUISActivityMetrics _isInnerSurface]
+ -[SBUISActivityMetrics _orientationSensitiveItemMetrics:scaleFactor:screen:]
+ -[SBUISActivityMetrics _supportsInnerSurfaceGutter]
+ -[SBUISActivityMetrics ambientDefaultMetricsForContentType:]
+ -[SBUISActivityMetrics initWithWindowScene:allowsPortraitInAmbient:surfaceType:avoidingFold:activeLayoutDirection:]
+ -[SBUISActivityMetrics isAvoidingFold]
+ -[SBUISActivityMetrics surfaceType]
+ -[SBUISimpleFixedDigitPasscodeEntryField _characterIndicatorContainerFrameForScreen:numberOfDigits:]
+ -[SBUISimpleFixedDigitPasscodeEntryField _effectiveScreen]
+ -[SBUISimpleFixedDigitPasscodeEntryField didMoveToWindow]
+ -[SBUISimpleFixedDigitPasscodeEntryField initWithDefaultSizeAndLightStyle:numberOfDigits:screen:]
+ -[SBUISimpleFixedDigitPasscodeEntryField layoutSubviews]
+ -[SBUISystemApertureLayoutMetrics _deviceWidth]
+ -[SBUISystemApertureLayoutMetrics _realDeviceMainScreenScale]
+ -[SBUISystemApertureLayoutMetrics _realDeviceNativeBoundsInPixels]
+ -[SBUISystemApertureLayoutMetrics _realDeviceNativeScreenSizeInPoints]
+ -[SBUISystemApertureLayoutMetrics _sizeIsCoverDisplay:]
+ -[UIWindowScene(SBSUISurfaceTypeClient) sbsui_surfaceTypeClient]
+ -[_SBUIBiometricKitInterface _deviceForKind:]
+ -[_SBUIBiometricKitInterface _isAccessDeferredForDevice:]
+ -[_SBUIBiometricKitInterface _matchModeForDevice:withMatchMode:]
+ -[_SBUIBiometricKitInterface _queryRequiresFaceIDLatencyMitigation]
+ -[_SBUIBiometricKitInterface _refreshEnrolledIdentitiesCount]
+ -[_SBUIBiometricKitInterface _setFingerDetected:]
+ -[_SBUIBiometricKitInterface _shouldCreateMatchOperationForDevice:withMatchMode:]
+ -[_SBUIBiometricKitInterface hasEnrolledIdentitiesForDeviceKind:]
+ -[_SBUIBiometricKitInterface lockoutStateForDeviceKind:]
+ -[_SBUIBiometricKitInterface requiresFaceIDLatencyMitigation]
+ -[_SBUIBiometricKitInterface updateFingerPresenceWithOperations:]
+ -[_SBUIPoseidonCoachingSuppressionAssertion .cxx_destruct]
+ -[_SBUIPoseidonCoachingSuppressionAssertion dealloc]
+ -[_SBUIPoseidonCoachingSuppressionAssertion initWithLevel:invalidationBlock:]
+ -[_SBUIPoseidonCoachingSuppressionAssertion invalidate]
+ -[_SBUIPoseidonCoachingSuppressionAssertion level]
+ GCC_except_table145
+ GCC_except_table17
+ GCC_except_table31
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table64
+ _NSStringForSurfaceType
+ _NSStringFromSBUIBiometricDeviceKind
+ _OBJC_CLASS_$_SBSUIDisplayYoinkingSceneComponent
+ _OBJC_CLASS_$_SBSUIDisplayYoinkingSceneExtension
+ _OBJC_CLASS_$_SBSUIDisplayYoinkingSceneHostComponent
+ _OBJC_CLASS_$_SBSUIDisplayYoinkingSceneSpecification
+ _OBJC_CLASS_$_SBSUIDisplayYoinkingViewController
+ _OBJC_CLASS_$_SBSUIDuoDisplaySceneRequestBuilder
+ _OBJC_CLASS_$_SBSUIDuoDisplaySceneSpecification
+ _OBJC_CLASS_$_SBSUISurfaceTypeClientComponent
+ _OBJC_CLASS_$_SBSUISurfaceTypeSceneExtension
+ _OBJC_CLASS_$_SBUIDisplayActivationTrackingSceneExtension
+ _OBJC_CLASS_$_TPGlassActionSliderDisplayHandoffConfiguration
+ _OBJC_CLASS_$_UIViewReservedRegionKind
+ _OBJC_CLASS_$__SBSUIDisplayYoinkingWindow
+ _OBJC_CLASS_$__SBUIPoseidonCoachingSuppressionAssertion
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingSceneComponent._fbsScene
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingSceneComponent._viewController
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingSceneComponent._window
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingSceneComponent._windowScene
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingSceneHostComponent._delegate
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingSceneHostComponent._interacting
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingSceneHostComponent._pastSwapThreshold
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingSceneHostComponent._pastTouchBlockingThreshold
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingSceneHostComponent._phase
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._actionSlider
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._backdropView
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._cancelPending
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._delegate
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._dimmingTintView
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._displayYoinkFeedbackGenerator
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._feedbackGeneratorActive
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._pastSwapThreshold
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._pastTouchBlockingThreshold
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._settings
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._slidePhase
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._sliderHasStartedSliding
+ _OBJC_IVAR_$_SBSUIDisplayYoinkingViewController._touchesActive
+ _OBJC_IVAR_$_SBSUISurfaceTypeClientComponent._observers
+ _OBJC_IVAR_$_SBSUISurfaceTypeClientComponent._pendingObservers
+ _OBJC_IVAR_$_SBUIBiometricResource._bkMatchConvenienceOperationClass
+ _OBJC_IVAR_$_SBUIBiometricResource._mesaOcclusionAssertions
+ _OBJC_IVAR_$_SBUIBiometricResource._needsFingerPresenceUpdate
+ _OBJC_IVAR_$_SBUIBiometricResource._needsStrictTouchCoverageAppliedOnFingerOff
+ _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._cancelButtonCenterXConstraint
+ _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._cancelButtonCenterYConstraint
+ _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._centeredContentHelperGuide
+ _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._emergencyButtonCenterXConstraint
+ _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._hasPoseidonSupport
+ _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._lastConstraintUpdateSize
+ _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._usePasscodeButton
+ _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._usePasscodeButtonVisible
+ _OBJC_IVAR_$_SBUIPasscodeLockNumberPad._cancelButtonConstraintCenterY
+ _OBJC_IVAR_$_SBUIPasscodeLockNumberPad._desiredFrame
+ _OBJC_IVAR_$_SBUIPasscodeLockNumberPad._nonUniversalOffsetY
+ _OBJC_IVAR_$_SBUIPasscodeLockNumberPad._screen
+ _OBJC_IVAR_$_SBUIPasscodeLockNumberPad._sizeAtLastLayout
+ _OBJC_IVAR_$_SBUIPasscodeLockViewBase._unlockIntent
+ _OBJC_IVAR_$_SBUIPasscodeLockViewLongNumericKeypad._screen
+ _OBJC_IVAR_$_SBUIPasscodeLockViewWithKeyboard._screen
+ _OBJC_IVAR_$_SBUIPasscodeLockViewWithKeypad._permittedBounds
+ _OBJC_IVAR_$_SBUIPasscodeLockViewWithKeypad._screen
+ _OBJC_IVAR_$_SBUIPhoneUnlockWithWatchController._unlockSuppressionAssertions
+ _OBJC_IVAR_$_SBUIPoseidonContainerViewController._coachingSuppressionAssertions
+ _OBJC_IVAR_$_SBUIPoseidonContainerViewController._devicePose
+ _OBJC_IVAR_$_SBUIPoseidonContainerViewController._isHingeFullyClosed
+ _OBJC_IVAR_$_SBUIPoseidonContainerViewController._overrideSurfaceType
+ _OBJC_IVAR_$_SBUIPoseidonContainerViewController._wantsCoaching
+ _OBJC_IVAR_$_SBUIPoseidonIconView._coachingLabelVisible
+ _OBJC_IVAR_$_SBUIPoseidonIconView._columnFrame
+ _OBJC_IVAR_$_SBUISActivityMetrics._avoidingFold
+ _OBJC_IVAR_$_SBUISActivityMetrics._surfaceType
+ _OBJC_IVAR_$_SBUISimpleFixedDigitPasscodeEntryField._mostRecentLayoutDiameter
+ _OBJC_IVAR_$_SBUISimpleFixedDigitPasscodeEntryField._mostRecentLayoutScreen
+ _OBJC_IVAR_$_SBUISimpleFixedDigitPasscodeEntryField._screen
+ _OBJC_IVAR_$__SBUIBiometricKitInterface._currentTouchDidFailToMatch
+ _OBJC_IVAR_$__SBUIBiometricKitInterface._enrolledIdentitiesCountByDevice
+ _OBJC_IVAR_$__SBUIBiometricKitInterface._requiresFaceIDLatencyMitigation
+ _OBJC_IVAR_$__SBUIPoseidonCoachingSuppressionAssertion._invalidationBlock
+ _OBJC_IVAR_$__SBUIPoseidonCoachingSuppressionAssertion._level
+ _OBJC_METACLASS_$_SBSUIDisplayYoinkingSceneComponent
+ _OBJC_METACLASS_$_SBSUIDisplayYoinkingSceneExtension
+ _OBJC_METACLASS_$_SBSUIDisplayYoinkingSceneHostComponent
+ _OBJC_METACLASS_$_SBSUIDisplayYoinkingSceneSpecification
+ _OBJC_METACLASS_$_SBSUIDisplayYoinkingViewController
+ _OBJC_METACLASS_$_SBSUIDuoDisplaySceneRequestBuilder
+ _OBJC_METACLASS_$_SBSUIDuoDisplaySceneSpecification
+ _OBJC_METACLASS_$_SBSUISurfaceTypeClientComponent
+ _OBJC_METACLASS_$_SBSUISurfaceTypeSceneExtension
+ _OBJC_METACLASS_$_SBUIDisplayActivationTrackingSceneExtension
+ _OBJC_METACLASS_$__SBSUIDisplayYoinkingWindow
+ _OBJC_METACLASS_$__SBUIPoseidonCoachingSuppressionAssertion
+ _SBFPermittedBoundsAvoidingRegionRects
+ _SBLogDisplayContentMode
+ _SBRectCornerRadiiByReplacingIntersectedCorners
+ _SBRectCornerRadiiConvertCornerRadiiFromOrientationToOrientation
+ _SBRectCornerRadiiIsSymmetrical
+ _SBSCurrentCoverDisplaySize
+ _SBSUISurfaceTypeFromSSKSurfaceType
+ _SBSUISurfaceTypeIsValid
+ _SBSUIWindowSceneSessionRoleDisplayYoinking
+ _SBSUIWindowSceneSessionRoleDuoDisplay
+ _SBTransformedRectCornerRadiiWithScale
+ _SBUIBiometricLockoutStateFromBKLockoutState
+ _UIFontWeightBold
+ __OBJC_$_CLASS_METHODS_SBSUIDisplayYoinkingSceneExtension
+ __OBJC_$_CLASS_METHODS_SBSUISurfaceTypeSceneExtension
+ __OBJC_$_CLASS_METHODS_SBUIDisplayActivationTrackingSceneExtension
+ __OBJC_$_CLASS_METHODS__SBSUIDisplayYoinkingWindow
+ __OBJC_$_INSTANCE_METHODS_FBSScene(Resizability|SBSUISurfaceTypeClient|SBSUICameraOverlaySceneClientMonitor|SBSUIRemoteAlertSceneClientComponent|SBUIContinuitySessionParticipantClientComponent|SBContinuitySessionSceneParticipant)
+ __OBJC_$_INSTANCE_METHODS_SBSUIDisplayYoinkingSceneComponent
+ __OBJC_$_INSTANCE_METHODS_SBSUIDisplayYoinkingSceneHostComponent
+ __OBJC_$_INSTANCE_METHODS_SBSUIDisplayYoinkingSceneSpecification
+ __OBJC_$_INSTANCE_METHODS_SBSUIDisplayYoinkingViewController
+ __OBJC_$_INSTANCE_METHODS_SBSUIDuoDisplaySceneRequestBuilder
+ __OBJC_$_INSTANCE_METHODS_SBSUIDuoDisplaySceneSpecification
+ __OBJC_$_INSTANCE_METHODS_SBSUISurfaceTypeClientComponent
+ __OBJC_$_INSTANCE_METHODS_UIWindowScene(SBSUIScreenSharingOverlaySceneSpecification|RetailDemoSupport|Resizability|SBSUISurfaceTypeClient|SBSUIHearingTestModeAdditions|SBUISystemAperture)
+ __OBJC_$_INSTANCE_METHODS__SBUIPoseidonCoachingSuppressionAssertion
+ __OBJC_$_INSTANCE_VARIABLES_SBSUIDisplayYoinkingSceneComponent
+ __OBJC_$_INSTANCE_VARIABLES_SBSUIDisplayYoinkingSceneHostComponent
+ __OBJC_$_INSTANCE_VARIABLES_SBSUIDisplayYoinkingViewController
+ __OBJC_$_INSTANCE_VARIABLES_SBSUISurfaceTypeClientComponent
+ __OBJC_$_INSTANCE_VARIABLES_SBUIPasscodeLockViewLongNumericKeypad
+ __OBJC_$_INSTANCE_VARIABLES__SBUIPoseidonCoachingSuppressionAssertion
+ __OBJC_$_PROP_LIST_SBSUIDisplayYoinkingSceneClientSettings
+ __OBJC_$_PROP_LIST_SBSUIDisplayYoinkingSceneComponent
+ __OBJC_$_PROP_LIST_SBSUIDisplayYoinkingSceneHostComponent
+ __OBJC_$_PROP_LIST_SBSUIDisplayYoinkingSceneSettings
+ __OBJC_$_PROP_LIST_SBSUIDisplayYoinkingViewController
+ __OBJC_$_PROP_LIST_SBSUISurfaceTypeClient
+ __OBJC_$_PROP_LIST_SBSUISurfaceTypeClientComponent
+ __OBJC_$_PROP_LIST__SBUIPoseidonCoachingSuppressionAssertion
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSUIDisplayYoinkingSceneClientSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSUIDisplayYoinkingSceneSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSUIDisplayYoinkingViewControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBSUISurfaceTypeClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SSKDisplayTraitsObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSUIDisplayYoinkingSceneClientSettings
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSUIDisplayYoinkingSceneSettings
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSUIDisplayYoinkingViewControllerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBSUISurfaceTypeClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSKDisplayTraitsObserver
+ __OBJC_$_PROTOCOL_REFS_SBSUIDisplayYoinkingSceneClientSettings
+ __OBJC_$_PROTOCOL_REFS_SBSUIDisplayYoinkingSceneSettings
+ __OBJC_$_PROTOCOL_REFS_SBSUIDisplayYoinkingViewControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_SBSUISurfaceTypeClient
+ __OBJC_$_PROTOCOL_REFS_SSKDisplayTraitsObserver
+ __OBJC_CLASS_PROTOCOLS_$_SBSUIDisplayYoinkingSceneComponent
+ __OBJC_CLASS_PROTOCOLS_$_SBSUISurfaceTypeClientComponent
+ __OBJC_CLASS_PROTOCOLS_$__SBUIPoseidonCoachingSuppressionAssertion
+ __OBJC_CLASS_RO_$_SBSUIDisplayYoinkingSceneComponent
+ __OBJC_CLASS_RO_$_SBSUIDisplayYoinkingSceneExtension
+ __OBJC_CLASS_RO_$_SBSUIDisplayYoinkingSceneHostComponent
+ __OBJC_CLASS_RO_$_SBSUIDisplayYoinkingSceneSpecification
+ __OBJC_CLASS_RO_$_SBSUIDisplayYoinkingViewController
+ __OBJC_CLASS_RO_$_SBSUIDuoDisplaySceneRequestBuilder
+ __OBJC_CLASS_RO_$_SBSUIDuoDisplaySceneSpecification
+ __OBJC_CLASS_RO_$_SBSUISurfaceTypeClientComponent
+ __OBJC_CLASS_RO_$_SBSUISurfaceTypeSceneExtension
+ __OBJC_CLASS_RO_$_SBUIDisplayActivationTrackingSceneExtension
+ __OBJC_CLASS_RO_$__SBSUIDisplayYoinkingWindow
+ __OBJC_CLASS_RO_$__SBUIPoseidonCoachingSuppressionAssertion
+ __OBJC_LABEL_PROTOCOL_$_SBSUIDisplayYoinkingSceneClientSettings
+ __OBJC_LABEL_PROTOCOL_$_SBSUIDisplayYoinkingSceneSettings
+ __OBJC_LABEL_PROTOCOL_$_SBSUIDisplayYoinkingViewControllerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SBSUISurfaceTypeClient
+ __OBJC_LABEL_PROTOCOL_$_SSKDisplayTraitsObserver
+ __OBJC_METACLASS_RO_$_SBSUIDisplayYoinkingSceneComponent
+ __OBJC_METACLASS_RO_$_SBSUIDisplayYoinkingSceneExtension
+ __OBJC_METACLASS_RO_$_SBSUIDisplayYoinkingSceneHostComponent
+ __OBJC_METACLASS_RO_$_SBSUIDisplayYoinkingSceneSpecification
+ __OBJC_METACLASS_RO_$_SBSUIDisplayYoinkingViewController
+ __OBJC_METACLASS_RO_$_SBSUIDuoDisplaySceneRequestBuilder
+ __OBJC_METACLASS_RO_$_SBSUIDuoDisplaySceneSpecification
+ __OBJC_METACLASS_RO_$_SBSUISurfaceTypeClientComponent
+ __OBJC_METACLASS_RO_$_SBSUISurfaceTypeSceneExtension
+ __OBJC_METACLASS_RO_$_SBUIDisplayActivationTrackingSceneExtension
+ __OBJC_METACLASS_RO_$__SBSUIDisplayYoinkingWindow
+ __OBJC_METACLASS_RO_$__SBUIPoseidonCoachingSuppressionAssertion
+ __OBJC_PROTOCOL_$_SBSUIDisplayYoinkingSceneClientSettings
+ __OBJC_PROTOCOL_$_SBSUIDisplayYoinkingSceneSettings
+ __OBJC_PROTOCOL_$_SBSUIDisplayYoinkingViewControllerDelegate
+ __OBJC_PROTOCOL_$_SBSUISurfaceTypeClient
+ __OBJC_PROTOCOL_$_SSKDisplayTraitsObserver
+ __OBJC_PROTOCOL_REFERENCE_$_SBSUIDisplayYoinkingSceneClientSettings
+ __OBJC_PROTOCOL_REFERENCE_$_SBSUIDisplayYoinkingSceneSettings
+ ___44-[SBUIPasscodeLockNumberPad didMoveToWindow]_block_invoke
+ ___48-[SBUIPoseidonIconView setCoachingLabelVisible:]_block_invoke
+ ___49-[SBUIPasscodeLockViewWithKeypad didMoveToWindow]_block_invoke
+ ___55-[SBSUIDuoDisplaySceneSpecification uiSceneSessionRole]_block_invoke
+ ___55-[SBUIPasscodeLockViewBase _permittedBoundsForRegions:]_block_invoke
+ ___56-[SBUISimpleFixedDigitPasscodeEntryField layoutSubviews]_block_invoke
+ ___57-[SBSUIDisplayYoinkingViewController _createActionSlider]_block_invoke
+ ___57-[SBSUIDisplayYoinkingViewController _createActionSlider]_block_invoke_2
+ ___57-[SBSUIDisplayYoinkingViewController _createActionSlider]_block_invoke_3
+ ___62-[SBSUIDisplayYoinkingSceneComponent scene:didUpdateSettings:]_block_invoke
+ ___63-[SBSUIRemoteAlertScene setMovesAutomaticallyToPrimaryDisplay:]_block_invoke
+ ___64-[SBUIBiometricResource acquireMesaOcclusionAssertionForReason:]_block_invoke
+ ___65-[_SBUIBiometricKitInterface updateFingerPresenceWithOperations:]_block_invoke
+ ___65-[_SBUIBiometricKitInterface updateFingerPresenceWithOperations:]_block_invoke_2
+ ___71+[SBUIPasscodeLockNumberPad _buttonForCharacter:withLightStyle:screen:]_block_invoke
+ ___71-[SBUIPasscodeBiometricAuthenticationView setUsePasscodeButtonVisible:]_block_invoke
+ ___72-[SBSUIDisplayYoinkingSceneComponent _reportSlideStateOfViewController:]_block_invoke
+ ___84-[SBUIPoseidonContainerViewController acquireCoachingSuppressionAssertionWithLevel:]_block_invoke
+ ___85-[SBSUIRemoteAlertSceneHostComponent setDefaultStatusBarHeightsForStatusBarProvider:]_block_invoke
+ ___85-[SBSUIRemoteAlertSceneHostComponent setDefaultStatusBarHeightsForStatusBarProvider:]_block_invoke_2
+ ___block_descriptor_32_e21_B16?0"BKOperation"8l
+ ___block_descriptor_32_e39_"NSValue"16?0"UIViewReservedRegion"8l
+ ___block_descriptor_40_e8_32w_e51_v16?0"_SBUIPoseidonCoachingSuppressionAssertion"8lw32l8
+ ___block_descriptor_43_e69_v24?0"FBSMutableSceneClientSettings"8"FBSSceneTransitionContext"16l
+ ___block_descriptor_50_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_56_e8_32r_e5_v8?0lr32l8u40l8
+ ___block_descriptor_56_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40r48r_e49_v32?0"SBSimplePasscodeEntryFieldButton"8Q16^B24ls32l8r40l8r48l8
+ __sbPasscodeButtonSizingScreen
+ _kCTFontUIFontDesignCompactRounded
+ _memcpy
+ _scene:didUpdateSettings:.onceToken
+ _scene:didUpdateSettings:.sliderSettingsSelectorNames
- +[SBLightPasscodeNumberPadButton _numberPadButtonOuterCircleDiameter]
- +[SBPasscodeNumberPadButton _isPortrait]
- +[SBPasscodeNumberPadButton _numberPadButtonOuterCircleDiameter]
- +[SBSUIRemoteAlertClientSettingsExtension valueForUndefinedSetting:]
- +[SBUIPasscodeLockNumberPad _buttonForCharacter:withLightStyle:]
- +[SBUIPasscodeLockNumberPad _inputButtonCircleSize]
- +[SBUIPasscodeLockNumberPad _inputButtonCircleSpacing]
- +[SBUIPasscodeLockViewFactory _passcodeLockViewForStyle:withLightStyle:dimmed:]
- +[SBUIPhoneRLSceneSpecification isSupported]
- -[SBSUIRemoteAlertSceneHostComponent setDefaultStatusBarHeightsForWindowScene:]
- -[SBUIAlphanumericPasscodeEntryField initWithDefaultSizeAndLightStyle:]
- -[SBUILongNumericPasscodeEntryField initWithDefaultSizeAndLightStyle:]
- -[SBUINumericPasscodeEntryFieldBase initWithDefaultSizeAndLightStyle:]
- -[SBUIPasscodeBiometricAuthenticationView faceIDLabelAndReasonHelperGuide]
- -[SBUIPasscodeBiometricAuthenticationView faceIDUsePasscodeButtonVisible]
- -[SBUIPasscodeBiometricAuthenticationView faceIDUsePasscodeButton]
- -[SBUIPasscodeBiometricAuthenticationView setFaceIDLabelAndReasonHelperGuide:]
- -[SBUIPasscodeBiometricAuthenticationView setFaceIDUsePasscodeButton:]
- -[SBUIPasscodeBiometricAuthenticationView setFaceIDUsePasscodeButtonVisible:]
- -[SBUIPasscodeLockNumberPad _distanceToTopOfFirstButton]
- -[SBUIPasscodeLockViewBase passcodeBiometricAuthenticationViewNumberPadAncillaryButtonOffsetFromTopOfScreen:]
- -[SBUIPasscodeLockViewLongNumericKeypad _newEntryField]
- -[SBUIPasscodeLockViewSimpleFixedDigitKeypad _newEntryField]
- -[SBUIPasscodeLockViewWithKeypad _defaultEntryFieldPosition]
- -[SBUIPasscodeLockViewWithKeypad _newEntryField]
- -[SBUIPhoneRLSceneSpecification allowsHostedSoftwareKeyboard]
- -[SBUIPhoneRLSceneSpecification defaultExtensions]
- -[SBUIPhoneRLSceneSpecification uiSceneMinimumClass]
- -[SBUIPhoneRLSceneSpecification uiSceneSessionRole]
- -[SBUIPoseidonContainerViewController viewDidLoad]
- -[SBUISActivityMetrics ambientDefaultMetrics]
- -[SBUISActivityMetrics initWithWindowScene:allowsPortraitInAmbient:activeLayoutDirection:]
- -[SBUISystemApertureLayoutMetrics sensorVariant]
- -[SBUISystemApertureLayoutMetrics setSensorVariant:]
- GCC_except_table138
- GCC_except_table16
- GCC_except_table21
- _OBJC_CLASS_$_SBUIPhoneRLSceneSpecification
- _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._faceIDLabelAndReasonHelperGuide
- _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._faceIDUsePasscodeButton
- _OBJC_IVAR_$_SBUIPasscodeBiometricAuthenticationView._faceIDUsePasscodeButtonVisible
- _OBJC_IVAR_$_SBUISystemApertureLayoutMetrics._sensorVariant
- _OBJC_IVAR_$__SBUIBiometricKitInterface._enrolledIdentitiesCount
- _OBJC_METACLASS_$_SBUIPhoneRLSceneSpecification
- _SBUISceneLevelPhoneRL
- _SBUIWindowSceneSessionRolePhoneRL
- __OBJC_$_CLASS_METHODS_SBUIPhoneRLSceneSpecification
- __OBJC_$_INSTANCE_METHODS_FBSScene(Resizability|SBSUICameraOverlaySceneClientMonitor|SBSUIRemoteAlertSceneClientComponent|SBUIContinuitySessionParticipantClientComponent|SBContinuitySessionSceneParticipant)
- __OBJC_$_INSTANCE_METHODS_SBUIPhoneRLSceneSpecification
- __OBJC_$_INSTANCE_METHODS_UIWindowScene(SBSUIScreenSharingOverlaySceneSpecification|RetailDemoSupport|Resizability|SBSUIHearingTestModeAdditions|SBUISystemAperture)
- __OBJC_CLASS_RO_$_SBUIPhoneRLSceneSpecification
- __OBJC_METACLASS_RO_$_SBUIPhoneRLSceneSpecification
- ___44+[SBUIPhoneRLSceneSpecification isSupported]_block_invoke
- ___77-[SBUIPasscodeBiometricAuthenticationView setFaceIDUsePasscodeButtonVisible:]_block_invoke
- ___79-[SBSUIRemoteAlertSceneHostComponent setDefaultStatusBarHeightsForWindowScene:]_block_invoke
- ___79-[SBSUIRemoteAlertSceneHostComponent setDefaultStatusBarHeightsForWindowScene:]_block_invoke_2
- ___block_descriptor_49_e8_32s_e8_v12?0B8ls32l8
- _isSupported.__onceToken
- _isSupported.__supported
- _notify_get_state
CStrings:
+ ".cover"
+ ".default"
+ ".inner"
+ ".unknown"
+ "@\"NSValue\"16@?0@\"UIViewReservedRegion\"8"
+ "@`"
+ "Applying strict touch coverage update after finger off"
+ "B16@?0@\"BKOperation\"8"
+ "BKMatchConvenienceOperation"
+ "Deferring identities query for device %@ until first unlock"
+ "Deferring strict matching update until finger off"
+ "Error updating finger presence: %{public}@"
+ "Error(%li)"
+ "Failed to query Face ID latency-mitigation device property: %{public}@"
+ "Failed to read lockout state for %{public}@ device %@: %{public}@"
+ "Failed to start operation %{public}@ for match assertion %{public}@: %{public}@"
+ "FlexibleLockScreen"
+ "Ignoring duplicate match failure for a touch that has already failed"
+ "Ignoring start failure for operation %{public}@ (doesn't belong to a matching assertion): %{public}@"
+ "Lockout state %ld for device %@"
+ "Mesa"
+ "Mesa occluded %{public}@ - all assertions: %@"
+ "MesaOcclusion"
+ "MesaOcclusionAssertions"
+ "No %{public}@ device to report a lockout state for"
+ "Not attempting phone unlock with watch because unlock is suppressed"
+ "Not refreshing finger presence, no Touch ID operation"
+ "PHONE_UNLOCK_REQUIRED_FACE_PROMPT"
+ "PHONE_UNLOCK_REQUIRED_TOUCH_PROMPT"
+ "Pearl"
+ "PhoneUnlockWithWatchSuppression"
+ "PosterKit"
+ "SBDisplayActivationTrackingHostComponent"
+ "SBSUIDisplayYoinkingSceneComponent"
+ "SBSUIWindowSceneSessionRoleDisplayYoinking"
+ "SBSUIWindowSceneSessionRoleDuoDisplay"
+ "SBSceneRegionSceneExtension"
+ "SBUIPoseidonContainerViewController.m"
+ "SWIPE_UP_TO_RETRY_FACE_PROMPT"
+ "Skipping creation of match operation for device %@, deferring device access until first unlock"
+ "Skipping creation of match operation for device %@, no enrolled identities"
+ "Skipping creation of presence detect operation for device %@, deferring device access until first unlock"
+ "Unknown enrolled identities count for device %@, creating match operation anyway"
+ "Updated finger presence: %d"
+ "[Display Yoinking] ignoring a slide completion that never began in the slider scene"
+ "[Display Yoinking] slide began in the slider scene"
+ "[Display Yoinking] slide completed in the slider scene"
+ "[Display Yoinking] slide returned to rest in the slider scene; finger lifted"
+ "[Display Yoinking] slider %{public}@"
+ "[Display Yoinking] slider scene component attached to a non-window scene"
+ "[Display Yoinking] slider scene connected %{public}@"
+ "[Display Yoinking] slider scene invalidating %{public}@"
+ "b"
+ "invalidationBlock != nil"
+ "ipad.landscape"
+ "needsStrictTouchCoverageAppliedOnFingerOff"
+ "shown"
+ "strictTouchCoverageRequired"
+ "v16@?0@\"_SBUIPoseidonCoachingSuppressionAssertion\"8"
+ "\xd1"
- "%@"
- "A"
- "Failed to activate match assertion %{public}@ with error %{public}@"
- "PHONE_UNLOCK_REQUIRED_PROMPT"
- "SBPhoneRLWindowScene"
- "SBUIWindowSceneSessionRolePhoneRL"
- "SWIPE_UP_TO_RETRY_PROMPT"
- "adi"
- "debug"
```
