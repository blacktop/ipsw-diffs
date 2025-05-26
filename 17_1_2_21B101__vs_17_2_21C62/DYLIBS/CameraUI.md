## CameraUI

> `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`

```diff

-4005.6.0.0.0
-  __TEXT.__text: 0x1da320
+4007.14.0.0.0
+  __TEXT.__text: 0x1dec1c
   __TEXT.__auth_stubs: 0x20a0
-  __TEXT.__objc_methlist: 0x14f98
+  __TEXT.__objc_methlist: 0x152a0
   __TEXT.__const: 0x2d70
-  __TEXT.__gcc_except_tab: 0x23b8
-  __TEXT.__cstring: 0x1248f
-  __TEXT.__oslogstring: 0x11cbf
+  __TEXT.__gcc_except_tab: 0x2404
+  __TEXT.__cstring: 0x12763
+  __TEXT.__oslogstring: 0x11f21
   __TEXT.__dlopen_cstrs: 0x310
   __TEXT.__ustring: 0x8
-  __TEXT.__objc_const_ax: 0xe6f8
-  __TEXT.__unwind_info: 0x83c0
-  __TEXT.__objc_classname: 0x4994
-  __TEXT.__objc_methname: 0x7ea29
-  __TEXT.__objc_methtype: 0xd697
-  __TEXT.__objc_stubs: 0x49340
-  __DATA_CONST.__got: 0x1160
-  __DATA_CONST.__const: 0x6128
-  __DATA_CONST.__objc_classlist: 0xea8
+  __TEXT.__objc_const_ax: 0xe9b0
+  __TEXT.__unwind_info: 0x84f0
+  __TEXT.__objc_classname: 0x4a4d
+  __TEXT.__objc_methname: 0x80281
+  __TEXT.__objc_methtype: 0xd84d
+  __TEXT.__objc_stubs: 0x49e40
+  __DATA_CONST.__got: 0x1170
+  __DATA_CONST.__const: 0x6290
+  __DATA_CONST.__objc_classlist: 0xed0
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x5d8
+  __DATA_CONST.__objc_protolist: 0x5e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3b048
-  __DATA_CONST.__objc_selrefs: 0x14388
+  __DATA_CONST.__objc_const: 0x3b978
+  __DATA_CONST.__objc_selrefs: 0x146a0
   __DATA_CONST.__objc_arraydata: 0xcf0
-  __AUTH_CONST.__cfstring: 0x127a0
-  __AUTH_CONST.__objc_const: 0x9e60
+  __AUTH_CONST.__cfstring: 0x12a80
+  __AUTH_CONST.__objc_const: 0x9fc8
   __AUTH_CONST.__objc_intobj: 0x15a8
   __AUTH_CONST.__objc_doubleobj: 0x500
   __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH_CONST.__objc_arrayobj: 0xaf8
+  __AUTH_CONST.__objc_arrayobj: 0xb28
   __AUTH_CONST.__const: 0xa80
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x1060
-  __AUTH.__objc_data: 0x29b8
+  __AUTH.__objc_data: 0x2b48
   __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0x1670
-  __DATA.__objc_superrefs: 0xc50
-  __DATA.__objc_ivar: 0x3120
+  __DATA.__objc_classrefs: 0x16a0
+  __DATA.__objc_superrefs: 0xc68
+  __DATA.__objc_ivar: 0x31b4
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x46b8
+  __DATA.__data: 0x4720
   __DATA.__bss: 0x208
   __DATA_DIRTY.__objc_data: 0x68d8
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x290
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/ACTFramework.framework/ACTFramework
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 13676
-  Symbols:   46656
-  CStrings:  22268
+  Functions: 13806
+  Symbols:   47094
+  CStrings:  22477
 
Symbols:
+ +[CAMAccountController _isRealityDevice:]
+ +[CAMAccountController _shouldCheckPrimaryAccountForRegisteredRealityDevices]
+ +[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]
+ +[CAMAnalyticsSessionEvent _launchMethodToString:]
+ +[CAMCaptureConfiguration _fallbackVideoConfigurationForUnsupportedConfiguration:spatialVideoEnabled:]
+ +[CAMCaptureConfiguration sanitizeVideoConfigurationForDesiredConfiguration:mode:device:spatialVideoEnabled:]
+ +[CAMCaptureConversions CAMStereoVideoCaptureStatusForAVStereoVideoCaptureStatus:]
+ -[CAMAnalyticsCaptureEvent _spatialVideoEnabled]
+ -[CAMAnalyticsSessionEvent _capabilities]
+ -[CAMAnalyticsSessionEvent _firstConfiguredDevice]
+ -[CAMAnalyticsSessionEvent _firstConfiguredMode]
+ -[CAMAnalyticsSessionEvent _launchEventWithinReasonableTimeInterval]
+ -[CAMAnalyticsSessionEvent _launchMethod]
+ -[CAMAnalyticsSessionEvent _totalPortraitLightingChanges]
+ -[CAMAnalyticsSessionEvent didChangePortraitLighting]
+ -[CAMAnalyticsSessionEvent didLaunchShortCutItemWithMode:device:]
+ -[CAMAnalyticsSessionEvent didLaunchWithURLConfigurationRequest:]
+ -[CAMAnalyticsSessionEvent initWithCapabilities:availableCaptureModes:currentCaptureMode:currentCaptureDevice:callStatusMonitor:]
+ -[CAMAnalyticsSessionEvent set_firstConfiguredDevice:]
+ -[CAMAnalyticsSessionEvent set_firstConfiguredMode:]
+ -[CAMAnalyticsSessionEvent set_launchMethod:]
+ -[CAMAnalyticsSessionEvent set_totalPortraitLightingChanges:]
+ -[CAMCaptureCapabilities _defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:spatialVideoEnabled:overrodeWithForcedZoomValue:]
+ -[CAMCaptureCapabilities fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:macroMode:spatialVideoEnabled:]
+ -[CAMCaptureCapabilities isAutoFPSVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:spatialVideoEnabled:]
+ -[CAMCaptureCapabilities isSpatialVideoCaptureSupported]
+ -[CAMCaptureCapabilities isSpatialVideoSupportedForMode:devicePosition:]
+ -[CAMCaptureCapabilities isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:]
+ -[CAMCaptureCapabilities isSupportedVideoConfiguration:forMode:device:spatialVideoEnabled:]
+ -[CAMCaptureCapabilities isVariableFramerateVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:spatialVideoEnabled:]
+ -[CAMCaptureCapabilities isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:spatialVideoEnabled:]
+ -[CAMCaptureCapabilities isVideoStabilizationStrength:supportedForMode:devicePosition:spatialVideoEnabled:]
+ -[CAMCaptureCapabilities preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:]
+ -[CAMCaptureCapabilities resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:]
+ -[CAMCaptureCapabilities resolvedVideoConfigurationForMode:device:videoEncodingBehavior:videoConfiguration:outputToExternalStorage:spatialVideoEnabled:]
+ -[CAMCaptureCommandContext _captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:resolvedDevice:]
+ -[CAMCaptureCommandContext videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:resolvedDevice:]
+ -[CAMCaptureConfiguration initWithCaptureMode:captureDevice:videoConfiguration:audioConfiguration:flashMode:torchMode:HDRMode:irisMode:timerDuration:photoModeAspectRatioCrop:photoModeEffectFilterType:squareModeEffectFilterType:portraitModeEffectFilterType:portraitModeLightingEffectType:portraitModeApertureValue:portraitModeIntensityValue:mirrorFrontCameraCaptures:exposureBiasesByMode:macroMode:rawMode:proResVideoMode:semanticStyles:selectedSemanticStyleIndex:videoStabilizationMode:zoomPIPEnabled:spatialVideoEnabled:sharedLibraryMode:]
+ -[CAMCaptureConfiguration spatialVideoEnabled]
+ -[CAMCaptureGraphConfiguration enableStereoVideoCapture]
+ -[CAMCaptureGraphConfiguration initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:enableDepthSuggestion:enableZoomPIP:enableStereoVideoCapture:]
+ -[CAMFullscreenViewfinder _frameForSpatialRecordingIndicatorWithElapsedTimeViewGeometry:orientation:]
+ -[CAMFullscreenViewfinder _orientationInstructionView]
+ -[CAMFullscreenViewfinder _setOrientationInstructionView:]
+ -[CAMFullscreenViewfinder _setSpatialCaptureButton:]
+ -[CAMFullscreenViewfinder _setSpatialCaptureInstructionLabel:]
+ -[CAMFullscreenViewfinder _setSpatialCaptureRecordingIndicator:]
+ -[CAMFullscreenViewfinder deviceOrientation]
+ -[CAMFullscreenViewfinder isOrientationInstructionBackgroundBlurred]
+ -[CAMFullscreenViewfinder isOrientationInstructionVisible]
+ -[CAMFullscreenViewfinder isSpatialCaptureRecordingIndicatorVisible]
+ -[CAMFullscreenViewfinder setDeviceOrientation:]
+ -[CAMFullscreenViewfinder setDeviceOrientation:animated:]
+ -[CAMFullscreenViewfinder setOrientationInstructionBackgroundBlurred:]
+ -[CAMFullscreenViewfinder setOrientationInstructionBackgroundBlurred:animated:]
+ -[CAMFullscreenViewfinder setOrientationInstructionVisible:]
+ -[CAMFullscreenViewfinder setOrientationInstructionVisible:animated:]
+ -[CAMFullscreenViewfinder setSpatialCaptureRecordingIndicatorVisible:]
+ -[CAMFullscreenViewfinder setSpatialCaptureRecordingIndicatorVisible:animated:]
+ -[CAMFullscreenViewfinder setStereoVideoCaptureStatus:]
+ -[CAMFullscreenViewfinder setStereoVideoCaptureStatus:animated:]
+ -[CAMFullscreenViewfinder spatialCaptureButton]
+ -[CAMFullscreenViewfinder spatialCaptureInstructionLabel]
+ -[CAMFullscreenViewfinder spatialCaptureRecordingIndicator]
+ -[CAMFullscreenViewfinder stereoVideoCaptureStatus]
+ -[CAMLevelViewModel _deviceAngleForGravity:captureOrientation:relativeRoll:relativePitch:]
+ -[CAMLevelViewModel applyDeviceMotion:captureOrientation:]
+ -[CAMMotionController _orientationIfForcedToLandscape]
+ -[CAMMotionController _setOrientationWhenForcedToLandscape:]
+ -[CAMMotionController forceLandscapeOrientation]
+ -[CAMMotionController setDeviceOrientation:]
+ -[CAMMotionController setForceLandscapeOrientation:]
+ -[CAMOrientationInstructionView .cxx_destruct]
+ -[CAMOrientationInstructionView _effectView]
+ -[CAMOrientationInstructionView _formatLabel]
+ -[CAMOrientationInstructionView _interfaceOrientation]
+ -[CAMOrientationInstructionView _label]
+ -[CAMOrientationInstructionView hasBlurredBackground]
+ -[CAMOrientationInstructionView initWithFrame:]
+ -[CAMOrientationInstructionView layoutSubviews]
+ -[CAMOrientationInstructionView orientation]
+ -[CAMOrientationInstructionView setHasBlurredBackground:]
+ -[CAMOrientationInstructionView setHasBlurredBackground:animated:]
+ -[CAMOrientationInstructionView setOrientation:]
+ -[CAMOrientationInstructionView setOrientation:animated:]
+ -[CAMOrientationInstructionView set_effectView:]
+ -[CAMOrientationInstructionView set_interfaceOrientation:]
+ -[CAMPhysicalCaptureNotifier includesVolumeButtons]
+ -[CAMPhysicalCaptureNotifier initWithView:includeVolumeButtons:]
+ -[CAMPostConfigurationSetupCommand _configureStereoVideoCaptureEnabled:]
+ -[CAMRemoteShutterController cameraConnectionIsSpatialCapture:]
+ -[CAMRemoteShutterController setSpatialEnabled:]
+ -[CAMRemoteShutterController spatialEnabled]
+ -[CAMSpatialCaptureButton active]
+ -[CAMSpatialCaptureButton imageNameForCurrentState]
+ -[CAMSpatialCaptureButton initWithFrame:]
+ -[CAMSpatialCaptureButton setActive:]
+ -[CAMSpatialCaptureButton setActive:animated:]
+ -[CAMSpatialCaptureButton shouldShowSlashForCurrentState]
+ -[CAMSpatialCaptureButton shouldUseActiveTintForCurrentState]
+ -[CAMSpatialCaptureInstructionLabel _stringForStereoVideoCaptureStatus:]
+ -[CAMSpatialCaptureInstructionLabel setStereoVideoCaptureStatus:]
+ -[CAMSpatialCaptureInstructionLabel stereoVideoCaptureStatus]
+ -[CAMSpatialCaptureRecordingIndicator .cxx_destruct]
+ -[CAMSpatialCaptureRecordingIndicator _imageView]
+ -[CAMSpatialCaptureRecordingIndicator initWithFrame:]
+ -[CAMSpatialCaptureRecordingIndicator layoutSubviews]
+ -[CAMSpatialCaptureRecordingIndicator orientation]
+ -[CAMSpatialCaptureRecordingIndicator setOrientation:]
+ -[CAMSpatialCaptureRecordingIndicator setOrientation:animated:]
+ -[CAMStillImageCaptureResult predictedFinalAssetPhotoDimensions]
+ -[CAMUserPreferences colorSpaceForMode:videoConfiguration:videoEncodingBehavior:spatialVideoEnabled:]
+ -[CAMUserPreferences defaultDeviceForModeChange:devicePosition:spatialVideoEnabled:]
+ -[CAMUserPreferences isAutoFPSVideoEnabledForMode:device:videoConfiguration:encodingBehavior:outputToExternalStorage:spatialVideoEnabled:]
+ -[CAMUserPreferences preserveSpatialVideoEnabled]
+ -[CAMUserPreferences spatialVideoControlEnabled]
+ -[CAMUserPreferences spatialVideoEnabled]
+ -[CAMUserPreferences videoEncodingBehaviorForConfiguration:mode:desiredProResVideoMode:outputToExternalStorage:spatialVideoEnabled:]
+ -[CAMUserPreferences videoStabilizationStrengthForVideoStabilizationMode:captureMode:spatialVideoEnabled:]
+ -[CAMViewfinderViewController _cameraCaseShutterNotifier]
+ -[CAMViewfinderViewController _createAnalyticsSessionEventIfNeeded]
+ -[CAMViewfinderViewController _createCameraCaseShutterNotifierIfNeeded]
+ -[CAMViewfinderViewController _createPhysicalCaptureInteractionIfNeeded]
+ -[CAMViewfinderViewController _createPhysicalCaptureRecognizerIfNecessary]
+ -[CAMViewfinderViewController _deviceOrientationChanged:]
+ -[CAMViewfinderViewController _handlePhotoFormatPickerTapped].cold.1
+ -[CAMViewfinderViewController _handlePhysicalCaptureInteractionDidChangePhase:forButton:]
+ -[CAMViewfinderViewController _handleSpatialCaptureButtonTapped:]
+ -[CAMViewfinderViewController _isSpatialVideoActiveForMode:devicePosition:]
+ -[CAMViewfinderViewController _isSpatialVideoEnabled]
+ -[CAMViewfinderViewController _physicalButtonInteraction]
+ -[CAMViewfinderViewController _resolvedTorchModeForGraphConfiguration:]
+ -[CAMViewfinderViewController _setSpatialVideoEnabled:]
+ -[CAMViewfinderViewController _setStereoVideoCaptureStatus:]
+ -[CAMViewfinderViewController _shouldShowSpatialCaptureControlForGraphConfiguration:]
+ -[CAMViewfinderViewController _shouldShowSpatialCaptureInstructionsForGraphConfiguration:]
+ -[CAMViewfinderViewController _shouldShowVideoConfigurationIndicatorForGraphConfiguration:]
+ -[CAMViewfinderViewController _stereoVideoCaptureStatus]
+ -[CAMViewfinderViewController _updateSpatialCaptureUIStateForGraphConfiguration:animated:]
+ -[CAMViewfinderViewController _updateTorchModeForGraphConfiguration:animated:]
+ -[CAMViewfinderViewController captureController:didOutputStereoVideoCaptureStatus:]
+ -[CAMViewfinderViewController fullscreenViewfinderDidCreateSpatialCaptureButton:]
+ -[CAMViewfinderViewController generateAnalyticsForLaunchWithShortCutItem:]
+ -[CAMViewfinderViewController generateAnalyticsForLaunchWithURLConfigurationRequest:]
+ -[CAMViewfinderViewController set_cameraCaseShutterNotifier:]
+ -[CAMViewfinderViewController set_physicalButtonInteraction:]
+ -[CUCaptureController _setupStereoVideoCaptureStatusMonitoring]
+ -[CUCaptureController _stereoVideoCaptureStatusChangedForKeyPath:ofObject:change:]
+ -[CUCaptureController _teardownStereoVideoCaptureStatusMonitoring]
+ -[CUCaptureController setStereoVideoCaptureStatusDelegate:]
+ -[CUCaptureController stereoVideoCaptureStatusDelegate]
+ GCC_except_table1040
+ GCC_except_table1046
+ GCC_except_table1155
+ GCC_except_table1160
+ GCC_except_table1165
+ GCC_except_table170
+ GCC_except_table176
+ GCC_except_table182
+ GCC_except_table183
+ GCC_except_table194
+ GCC_except_table209
+ GCC_except_table537
+ GCC_except_table539
+ GCC_except_table593
+ GCC_except_table752
+ GCC_except_table770
+ GCC_except_table823
+ GCC_except_table826
+ _AVGQBWQSOG5QWWG276TG2HH4RGJZDA
+ _CAMMotionControllerCaptureDeviceOrientationChangedNotification
+ _CAMStereoVideoCaptureStatusContext
+ _CAMUserDeviceListLastCheckDate
+ _CAMUserPreferenceEnableSpatialVideoCaptureControl
+ _CAMUserPreferencePreserveSpatialVideoEnabled
+ _CAMUserPreferenceSpatialVideoEnabled
+ _OBJC_CLASS_$_AADeviceListRequest
+ _OBJC_CLASS_$_AADeviceListResponse
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_AVCaptureEventInteraction
+ _OBJC_CLASS_$_CAMAccountController
+ _OBJC_CLASS_$_CAMOrientationInstructionView
+ _OBJC_CLASS_$_CAMSpatialCaptureButton
+ _OBJC_CLASS_$_CAMSpatialCaptureInstructionLabel
+ _OBJC_CLASS_$_CAMSpatialCaptureRecordingIndicator
+ _OBJC_IVAR_$_CAMAnalyticsCaptureEvent.__spatialVideoEnabled
+ _OBJC_IVAR_$_CAMAnalyticsSessionEvent.__capabilities
+ _OBJC_IVAR_$_CAMAnalyticsSessionEvent.__firstConfiguredDevice
+ _OBJC_IVAR_$_CAMAnalyticsSessionEvent.__firstConfiguredMode
+ _OBJC_IVAR_$_CAMAnalyticsSessionEvent.__launchMethod
+ _OBJC_IVAR_$_CAMAnalyticsSessionEvent.__totalPortraitLightingChanges
+ _OBJC_IVAR_$_CAMCaptureCapabilities._spatialVideoCaptureSupported
+ _OBJC_IVAR_$_CAMCaptureConfiguration._spatialVideoEnabled
+ _OBJC_IVAR_$_CAMCaptureGraphConfiguration._enableStereoVideoCapture
+ _OBJC_IVAR_$_CAMFullscreenViewfinder.__orientationInstructionView
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._deviceOrientation
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._orientationInstructionBackgroundBlurred
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._orientationInstructionVisible
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._spatialCaptureButton
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._spatialCaptureInstructionLabel
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._spatialCaptureRecordingIndicator
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._spatialCaptureRecordingIndicatorVisible
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._stereoVideoCaptureStatus
+ _OBJC_IVAR_$_CAMMotionController.__orientationIfForcedToLandscape
+ _OBJC_IVAR_$_CAMMotionController._forceLandscapeOrientation
+ _OBJC_IVAR_$_CAMOrientationInstructionView.__effectView
+ _OBJC_IVAR_$_CAMOrientationInstructionView.__interfaceOrientation
+ _OBJC_IVAR_$_CAMOrientationInstructionView.__label
+ _OBJC_IVAR_$_CAMOrientationInstructionView._hasBlurredBackground
+ _OBJC_IVAR_$_CAMOrientationInstructionView._orientation
+ _OBJC_IVAR_$_CAMPhysicalCaptureNotifier._includesVolumeButtons
+ _OBJC_IVAR_$_CAMRemoteShutterController._spatialEnabled
+ _OBJC_IVAR_$_CAMSpatialCaptureButton._active
+ _OBJC_IVAR_$_CAMSpatialCaptureInstructionLabel._stereoVideoCaptureStatus
+ _OBJC_IVAR_$_CAMSpatialCaptureRecordingIndicator.__imageView
+ _OBJC_IVAR_$_CAMSpatialCaptureRecordingIndicator._orientation
+ _OBJC_IVAR_$_CAMUserPreferences._preserveSpatialVideoEnabled
+ _OBJC_IVAR_$_CAMUserPreferences._spatialVideoControlEnabled
+ _OBJC_IVAR_$_CAMUserPreferences._spatialVideoEnabled
+ _OBJC_IVAR_$_CAMViewfinderViewController.__cameraCaseShutterNotifier
+ _OBJC_IVAR_$_CAMViewfinderViewController.__physicalButtonInteraction
+ _OBJC_IVAR_$_CAMViewfinderViewController.__spatialVideoEnabled
+ _OBJC_IVAR_$_CAMViewfinderViewController.__stereoVideoCaptureStatus
+ _OBJC_IVAR_$_CUCaptureController._stereoVideoCaptureStatusDelegate
+ _OBJC_METACLASS_$_CAMAccountController
+ _OBJC_METACLASS_$_CAMOrientationInstructionView
+ _OBJC_METACLASS_$_CAMSpatialCaptureButton
+ _OBJC_METACLASS_$_CAMSpatialCaptureInstructionLabel
+ _OBJC_METACLASS_$_CAMSpatialCaptureRecordingIndicator
+ _UIFontWeightThin
+ __OBJC_$_CLASS_METHODS_CAMAccountController
+ __OBJC_$_INSTANCE_METHODS_CAMOrientationInstructionView
+ __OBJC_$_INSTANCE_METHODS_CAMSpatialCaptureButton
+ __OBJC_$_INSTANCE_METHODS_CAMSpatialCaptureInstructionLabel
+ __OBJC_$_INSTANCE_METHODS_CAMSpatialCaptureRecordingIndicator
+ __OBJC_$_INSTANCE_VARIABLES_CAMOrientationInstructionView
+ __OBJC_$_INSTANCE_VARIABLES_CAMSpatialCaptureButton
+ __OBJC_$_INSTANCE_VARIABLES_CAMSpatialCaptureInstructionLabel
+ __OBJC_$_INSTANCE_VARIABLES_CAMSpatialCaptureRecordingIndicator
+ __OBJC_$_PROP_LIST_CAMOrientationInstructionView
+ __OBJC_$_PROP_LIST_CAMSpatialCaptureButton
+ __OBJC_$_PROP_LIST_CAMSpatialCaptureInstructionLabel
+ __OBJC_$_PROP_LIST_CAMSpatialCaptureRecordingIndicator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAMStereoVideoCaptureStatusDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAMStereoVideoCaptureStatusDelegate
+ __OBJC_$_PROTOCOL_REFS_CAMStereoVideoCaptureStatusDelegate
+ __OBJC_CLASS_RO_$_CAMAccountController
+ __OBJC_CLASS_RO_$_CAMOrientationInstructionView
+ __OBJC_CLASS_RO_$_CAMSpatialCaptureButton
+ __OBJC_CLASS_RO_$_CAMSpatialCaptureInstructionLabel
+ __OBJC_CLASS_RO_$_CAMSpatialCaptureRecordingIndicator
+ __OBJC_LABEL_PROTOCOL_$_CAMStereoVideoCaptureStatusDelegate
+ __OBJC_METACLASS_RO_$_CAMAccountController
+ __OBJC_METACLASS_RO_$_CAMOrientationInstructionView
+ __OBJC_METACLASS_RO_$_CAMSpatialCaptureButton
+ __OBJC_METACLASS_RO_$_CAMSpatialCaptureInstructionLabel
+ __OBJC_METACLASS_RO_$_CAMSpatialCaptureRecordingIndicator
+ __OBJC_PROTOCOL_$_CAMStereoVideoCaptureStatusDelegate
+ ___66-[CAMOrientationInstructionView setHasBlurredBackground:animated:]_block_invoke
+ ___68-[CAMViewfinderViewController _setWantsVisualTextAnalysis:animated:]_block_invoke.418
+ ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke
+ ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke.21
+ ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke_2
+ ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke_2.cold.1
+ ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke_2.cold.2
+ ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke_2.cold.3
+ ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke_2.cold.4
+ ___72-[CAMViewfinderViewController _createPhysicalCaptureInteractionIfNeeded]_block_invoke
+ ___72-[CAMViewfinderViewController _createPhysicalCaptureInteractionIfNeeded]_block_invoke.929
+ ___82-[CUCaptureController _stereoVideoCaptureStatusChangedForKeyPath:ofObject:change:]_block_invoke
+ ___block_descriptor_40_e46_v32?0"AARequest"8"AAResponse"16"NSError"24l
+ ___block_descriptor_40_e8_32w_e24_v16?0"AVCaptureEvent"8lw32l8
+ ___block_descriptor_48_e8_32r_e25_v32?0"AADevice"8Q16^B24lr32l8
+ ___block_descriptor_57_e8_32s40s_e8_B16?0q8ls32l8s40l8
+ ___block_literal_global.1006
+ ___block_literal_global.1147
+ ___block_literal_global.24
+ ___block_literal_global.440
+ ___block_literal_global.462
+ __unnamed_array_storage.1001
+ __unnamed_array_storage.1004
+ __unnamed_array_storage.1007
+ __unnamed_array_storage.1060
+ __unnamed_array_storage.326
+ __unnamed_array_storage.332
+ __unnamed_array_storage.337
+ __unnamed_array_storage.356
+ __unnamed_array_storage.3899
+ __unnamed_array_storage.3902
+ __unnamed_array_storage.3905
+ __unnamed_array_storage.391
+ __unnamed_array_storage.396
+ __unnamed_array_storage.410
+ __unnamed_array_storage.440
+ __unnamed_array_storage.443
+ __unnamed_array_storage.446
+ __unnamed_array_storage.626
+ __unnamed_array_storage.647
+ __unnamed_array_storage.758
+ __unnamed_array_storage.761
+ __unnamed_array_storage.764
+ __unnamed_array_storage.767
+ __unnamed_array_storage.770
+ __unnamed_array_storage.773
+ __unnamed_array_storage.776
+ __unnamed_array_storage.779
+ __unnamed_array_storage.782
+ __unnamed_array_storage.785
+ __unnamed_array_storage.788
+ __unnamed_array_storage.791
+ __unnamed_array_storage.794
+ __unnamed_array_storage.797
+ __unnamed_array_storage.800
+ __unnamed_array_storage.803
+ __unnamed_array_storage.806
+ __unnamed_array_storage.809
+ __unnamed_array_storage.812
+ __unnamed_array_storage.815
+ __unnamed_array_storage.818
+ __unnamed_array_storage.821
+ __unnamed_array_storage.824
+ __unnamed_array_storage.827
+ __unnamed_array_storage.830
+ __unnamed_array_storage.833
+ __unnamed_array_storage.836
+ __unnamed_array_storage.839
+ __unnamed_array_storage.842
+ _objc_msgSend$CAMStereoVideoCaptureStatusForAVStereoVideoCaptureStatus:
+ _objc_msgSend$_cameraCaseShutterNotifier
+ _objc_msgSend$_captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:resolvedDevice:
+ _objc_msgSend$_configureStereoVideoCaptureEnabled:
+ _objc_msgSend$_createAnalyticsSessionEventIfNeeded
+ _objc_msgSend$_createCameraCaseShutterNotifierIfNeeded
+ _objc_msgSend$_createPhysicalCaptureInteractionIfNeeded
+ _objc_msgSend$_createPhysicalCaptureRecognizerIfNecessary
+ _objc_msgSend$_defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:spatialVideoEnabled:overrodeWithForcedZoomValue:
+ _objc_msgSend$_deviceAngleForGravity:captureOrientation:relativeRoll:relativePitch:
+ _objc_msgSend$_effectView
+ _objc_msgSend$_fallbackVideoConfigurationForUnsupportedConfiguration:spatialVideoEnabled:
+ _objc_msgSend$_firstConfiguredDevice
+ _objc_msgSend$_firstConfiguredMode
+ _objc_msgSend$_formatLabel
+ _objc_msgSend$_frameForSpatialRecordingIndicatorWithElapsedTimeViewGeometry:orientation:
+ _objc_msgSend$_handlePhysicalCaptureInteractionDidChangePhase:forButton:
+ _objc_msgSend$_isRealityDevice:
+ _objc_msgSend$_isSpatialVideoActiveForMode:devicePosition:
+ _objc_msgSend$_isSpatialVideoEnabled
+ _objc_msgSend$_launchEventWithinReasonableTimeInterval
+ _objc_msgSend$_launchMethod
+ _objc_msgSend$_launchMethodToString:
+ _objc_msgSend$_orientationIfForcedToLandscape
+ _objc_msgSend$_orientationInstructionView
+ _objc_msgSend$_physicalButtonInteraction
+ _objc_msgSend$_resolvedTorchModeForGraphConfiguration:
+ _objc_msgSend$_setOrientationInstructionView:
+ _objc_msgSend$_setOrientationWhenForcedToLandscape:
+ _objc_msgSend$_setSpatialCaptureButton:
+ _objc_msgSend$_setSpatialCaptureInstructionLabel:
+ _objc_msgSend$_setSpatialCaptureRecordingIndicator:
+ _objc_msgSend$_setSpatialVideoEnabled:
+ _objc_msgSend$_setStereoVideoCaptureStatus:
+ _objc_msgSend$_setupStereoVideoCaptureStatusMonitoring
+ _objc_msgSend$_shouldCheckPrimaryAccountForRegisteredRealityDevices
+ _objc_msgSend$_shouldShowSpatialCaptureControlForGraphConfiguration:
+ _objc_msgSend$_shouldShowSpatialCaptureInstructionsForGraphConfiguration:
+ _objc_msgSend$_shouldShowVideoConfigurationIndicatorForGraphConfiguration:
+ _objc_msgSend$_spatialVideoEnabled
+ _objc_msgSend$_stereoVideoCaptureStatus
+ _objc_msgSend$_stereoVideoCaptureStatusChangedForKeyPath:ofObject:change:
+ _objc_msgSend$_stringForStereoVideoCaptureStatus:
+ _objc_msgSend$_teardownStereoVideoCaptureStatusMonitoring
+ _objc_msgSend$_totalPortraitLightingChanges
+ _objc_msgSend$_updateSpatialCaptureUIStateForGraphConfiguration:animated:
+ _objc_msgSend$_updateTorchModeForGraphConfiguration:animated:
+ _objc_msgSend$aa_primaryAppleAccount
+ _objc_msgSend$applyDeviceMotion:captureOrientation:
+ _objc_msgSend$captureController:didOutputStereoVideoCaptureStatus:
+ _objc_msgSend$checkPrimaryAccountForRegisteredRealityDevices
+ _objc_msgSend$colorSpaceForMode:videoConfiguration:videoEncodingBehavior:spatialVideoEnabled:
+ _objc_msgSend$defaultDeviceForModeChange:devicePosition:spatialVideoEnabled:
+ _objc_msgSend$defaultStore
+ _objc_msgSend$didChangePortraitLighting
+ _objc_msgSend$didLaunchShortCutItemWithMode:device:
+ _objc_msgSend$didLaunchWithURLConfigurationRequest:
+ _objc_msgSend$enableStereoVideoCapture
+ _objc_msgSend$fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:macroMode:spatialVideoEnabled:
+ _objc_msgSend$forceLandscapeOrientation
+ _objc_msgSend$fullscreenViewfinderDidCreateSpatialCaptureButton:
+ _objc_msgSend$generateAnalyticsForLaunchWithShortCutItem:
+ _objc_msgSend$generateAnalyticsForLaunchWithURLConfigurationRequest:
+ _objc_msgSend$includesVolumeButtons
+ _objc_msgSend$initWithAccount:
+ _objc_msgSend$initWithAttributedString:
+ _objc_msgSend$initWithCapabilities:availableCaptureModes:currentCaptureMode:currentCaptureDevice:callStatusMonitor:
+ _objc_msgSend$initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:enableDepthSuggestion:enableZoomPIP:enableStereoVideoCapture:
+ _objc_msgSend$initWithCaptureMode:captureDevice:videoConfiguration:audioConfiguration:flashMode:torchMode:HDRMode:irisMode:timerDuration:photoModeAspectRatioCrop:photoModeEffectFilterType:squareModeEffectFilterType:portraitModeEffectFilterType:portraitModeLightingEffectType:portraitModeApertureValue:portraitModeIntensityValue:mirrorFrontCameraCaptures:exposureBiasesByMode:macroMode:rawMode:proResVideoMode:semanticStyles:selectedSemanticStyleIndex:videoStabilizationMode:zoomPIPEnabled:spatialVideoEnabled:sharedLibraryMode:
+ _objc_msgSend$initWithPrimaryEventHandler:secondaryEventHandler:
+ _objc_msgSend$initWithView:includeVolumeButtons:
+ _objc_msgSend$isAutoFPSVideoEnabledForMode:device:videoConfiguration:encodingBehavior:outputToExternalStorage:spatialVideoEnabled:
+ _objc_msgSend$isAutoFPSVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:spatialVideoEnabled:
+ _objc_msgSend$isOrientationInstructionBackgroundBlurred
+ _objc_msgSend$isOrientationInstructionVisible
+ _objc_msgSend$isSpatialCaptureRecordingIndicatorVisible
+ _objc_msgSend$isSpatialVideoCaptureSupported
+ _objc_msgSend$isSpatialVideoSupportedForMode:devicePosition:
+ _objc_msgSend$isStereoVideoCaptureSupported
+ _objc_msgSend$isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:
+ _objc_msgSend$isSupportedVideoConfiguration:forMode:device:spatialVideoEnabled:
+ _objc_msgSend$isVariableFramerateVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:spatialVideoEnabled:
+ _objc_msgSend$isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:spatialVideoEnabled:
+ _objc_msgSend$isVideoStabilizationStrength:supportedForMode:devicePosition:spatialVideoEnabled:
+ _objc_msgSend$performRequestWithHandler:
+ _objc_msgSend$phase
+ _objc_msgSend$predictedFinalAssetPhotoDimensions
+ _objc_msgSend$preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:
+ _objc_msgSend$preserveSpatialVideoEnabled
+ _objc_msgSend$resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:
+ _objc_msgSend$resolvedVideoConfigurationForMode:device:videoEncodingBehavior:videoConfiguration:outputToExternalStorage:spatialVideoEnabled:
+ _objc_msgSend$sanitizeVideoConfigurationForDesiredConfiguration:mode:device:spatialVideoEnabled:
+ _objc_msgSend$setDeviceOrientation:
+ _objc_msgSend$setDeviceOrientation:animated:
+ _objc_msgSend$setForceLandscapeOrientation:
+ _objc_msgSend$setHasBlurredBackground:animated:
+ _objc_msgSend$setOrientationInstructionBackgroundBlurred:animated:
+ _objc_msgSend$setOrientationInstructionVisible:animated:
+ _objc_msgSend$setSpatialCaptureRecordingIndicatorVisible:animated:
+ _objc_msgSend$setSpatialEnabled:
+ _objc_msgSend$setStereoVideoCaptureEnabled:
+ _objc_msgSend$setStereoVideoCaptureStatus:
+ _objc_msgSend$setStereoVideoCaptureStatus:animated:
+ _objc_msgSend$setStereoVideoCaptureStatusDelegate:
+ _objc_msgSend$set_cameraCaseShutterNotifier:
+ _objc_msgSend$set_firstConfiguredDevice:
+ _objc_msgSend$set_firstConfiguredMode:
+ _objc_msgSend$set_interfaceOrientation:
+ _objc_msgSend$set_launchMethod:
+ _objc_msgSend$set_physicalButtonInteraction:
+ _objc_msgSend$set_totalPortraitLightingChanges:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$spatialCaptureButton
+ _objc_msgSend$spatialCaptureInstructionLabel
+ _objc_msgSend$spatialCaptureRecordingIndicator
+ _objc_msgSend$spatialModeDidChange
+ _objc_msgSend$spatialVideoControlEnabled
+ _objc_msgSend$spatialVideoEnabled
+ _objc_msgSend$statusCode
+ _objc_msgSend$stereoVideoCaptureStatus
+ _objc_msgSend$stereoVideoCaptureStatusDelegate
+ _objc_msgSend$videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:resolvedDevice:
+ _objc_msgSend$videoEncodingBehaviorForConfiguration:mode:desiredProResVideoMode:outputToExternalStorage:spatialVideoEnabled:
+ _objc_msgSend$videoStabilizationStrengthForVideoStabilizationMode:captureMode:spatialVideoEnabled:
- +[CAMCaptureConfiguration _fallbackVideoConfigurationForUnsupportedConfiguration:]
- +[CAMCaptureConfiguration sanitizeVideoConfigurationForDesiredConfiguration:mode:device:]
- -[CAMAnalyticsSessionEvent initWithCapabilities:availableCaptureModes:callStatusMonitor:]
- -[CAMAnalyticsSessionEvent set_hostProcess:]
- -[CAMAnalyticsSessionEvent set_startTime:]
- -[CAMCaptureCapabilities _defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:overrodeWithForcedZoomValue:]
- -[CAMCaptureCapabilities allowActionButtonSimulation]
- -[CAMCaptureCapabilities fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:macroMode:]
- -[CAMCaptureCapabilities isAutoFPSVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:]
- -[CAMCaptureCapabilities isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:]
- -[CAMCaptureCapabilities isVariableFramerateVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:]
- -[CAMCaptureCapabilities isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:]
- -[CAMCaptureCapabilities isVideoStabilizationStrength:supportedForMode:devicePosition:]
- -[CAMCaptureCapabilities preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:]
- -[CAMCaptureCapabilities resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:]
- -[CAMCaptureCapabilities resolvedVideoConfigurationForMode:device:videoEncodingBehavior:videoConfiguration:outputToExternalStorage:]
- -[CAMCaptureCommandContext _captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:]
- -[CAMCaptureCommandContext videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:]
- -[CAMCaptureConfiguration initWithCaptureMode:captureDevice:videoConfiguration:audioConfiguration:flashMode:torchMode:HDRMode:irisMode:timerDuration:photoModeAspectRatioCrop:photoModeEffectFilterType:squareModeEffectFilterType:portraitModeEffectFilterType:portraitModeLightingEffectType:portraitModeApertureValue:portraitModeIntensityValue:mirrorFrontCameraCaptures:exposureBiasesByMode:macroMode:rawMode:proResVideoMode:semanticStyles:selectedSemanticStyleIndex:videoStabilizationMode:zoomPIPEnabled:sharedLibraryMode:]
- -[CAMCaptureGraphConfiguration initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:enableDepthSuggestion:enableZoomPIP:]
- -[CAMLevelViewModel _deviceAngleForGravity:deviceOrientation:relativeRoll:relativePitch:]
- -[CAMLevelViewModel applyDeviceMotion:deviceOrientation:]
- -[CAMPhysicalCaptureNotifier initWithView:]
- -[CAMUserPreferences colorSpaceForMode:videoConfiguration:videoEncodingBehavior:]
- -[CAMUserPreferences defaultDeviceForModeChange:devicePosition:]
- -[CAMUserPreferences isAutoFPSVideoEnabledForMode:device:videoConfiguration:encodingBehavior:outputToExternalStorage:]
- -[CAMUserPreferences videoEncodingBehaviorForConfiguration:mode:desiredProResVideoMode:outputToExternalStorage:]
- -[CAMUserPreferences videoStabilizationStrengthForVideoStabilizationMode:captureMode:]
- -[CAMViewfinderViewController _createPhysicalCaptureRecognizerOrNotifierIfNecessary]
- -[CAMViewfinderViewController _physicalCaptureNotifier]
- -[CAMViewfinderViewController _resolvedTorchModeForDesiredTorchMode]
- -[CAMViewfinderViewController _updateTorchModeAnimated:]
- -[CAMViewfinderViewController set_physicalCaptureNotifier:]
- GCC_except_table1023
- GCC_except_table1029
- GCC_except_table1138
- GCC_except_table1143
- GCC_except_table1148
- GCC_except_table159
- GCC_except_table179
- GCC_except_table180
- GCC_except_table206
- GCC_except_table532
- GCC_except_table534
- GCC_except_table588
- GCC_except_table760
- GCC_except_table812
- GCC_except_table815
- _OBJC_CLASS_$__UIPhysicalButtonConfiguration
- _OBJC_CLASS_$__UIPhysicalButtonInteraction
- _OBJC_IVAR_$_CAMCaptureCapabilities._allowActionButtonSimulation
- _OBJC_IVAR_$_CAMViewfinderViewController.__physicalCaptureNotifier
- ___68-[CAMViewfinderViewController _setWantsVisualTextAnalysis:animated:]_block_invoke.416
- ___block_descriptor_56_e8_32s40s_e8_B16?0q8ls32l8s40l8
- ___block_literal_global.1009
- ___block_literal_global.1150
- ___block_literal_global.438
- ___block_literal_global.460
- __unnamed_array_storage.1035
- __unnamed_array_storage.329
- __unnamed_array_storage.335
- __unnamed_array_storage.355
- __unnamed_array_storage.359
- __unnamed_array_storage.3861
- __unnamed_array_storage.3864
- __unnamed_array_storage.3867
- __unnamed_array_storage.393
- __unnamed_array_storage.401
- __unnamed_array_storage.425
- __unnamed_array_storage.621
- __unnamed_array_storage.642
- __unnamed_array_storage.753
- __unnamed_array_storage.756
- __unnamed_array_storage.759
- __unnamed_array_storage.762
- __unnamed_array_storage.765
- __unnamed_array_storage.768
- __unnamed_array_storage.771
- __unnamed_array_storage.774
- __unnamed_array_storage.777
- __unnamed_array_storage.780
- __unnamed_array_storage.783
- __unnamed_array_storage.786
- __unnamed_array_storage.789
- __unnamed_array_storage.792
- __unnamed_array_storage.795
- __unnamed_array_storage.798
- __unnamed_array_storage.801
- __unnamed_array_storage.804
- __unnamed_array_storage.807
- __unnamed_array_storage.810
- __unnamed_array_storage.813
- __unnamed_array_storage.816
- __unnamed_array_storage.819
- __unnamed_array_storage.822
- __unnamed_array_storage.825
- __unnamed_array_storage.828
- __unnamed_array_storage.831
- __unnamed_array_storage.834
- __unnamed_array_storage.837
- __unnamed_array_storage.931
- __unnamed_array_storage.976
- __unnamed_array_storage.979
- __unnamed_array_storage.982
- _objc_msgSend$_actionButtonInteraction
- _objc_msgSend$_captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:
- _objc_msgSend$_configurationWithPhysicalButton:behavior:behaviorOptions:
- _objc_msgSend$_createPhysicalCaptureRecognizerOrNotifierIfNecessary
- _objc_msgSend$_defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:overrodeWithForcedZoomValue:
- _objc_msgSend$_deviceAngleForGravity:deviceOrientation:relativeRoll:relativePitch:
- _objc_msgSend$_fallbackVideoConfigurationForUnsupportedConfiguration:
- _objc_msgSend$_physicalCaptureNotifier
- _objc_msgSend$_resolvedTorchModeForDesiredTorchMode
- _objc_msgSend$_updateTorchModeAnimated:
- _objc_msgSend$applyDeviceMotion:deviceOrientation:
- _objc_msgSend$colorSpaceForMode:videoConfiguration:videoEncodingBehavior:
- _objc_msgSend$defaultDeviceForModeChange:devicePosition:
- _objc_msgSend$fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:macroMode:
- _objc_msgSend$initWithCapabilities:availableCaptureModes:callStatusMonitor:
- _objc_msgSend$initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:enableDepthSuggestion:enableZoomPIP:
- _objc_msgSend$initWithCaptureMode:captureDevice:videoConfiguration:audioConfiguration:flashMode:torchMode:HDRMode:irisMode:timerDuration:photoModeAspectRatioCrop:photoModeEffectFilterType:squareModeEffectFilterType:portraitModeEffectFilterType:portraitModeLightingEffectType:portraitModeApertureValue:portraitModeIntensityValue:mirrorFrontCameraCaptures:exposureBiasesByMode:macroMode:rawMode:proResVideoMode:semanticStyles:selectedSemanticStyleIndex:videoStabilizationMode:zoomPIPEnabled:sharedLibraryMode:
- _objc_msgSend$initWithConfigurations:delegate:
- _objc_msgSend$initWithView:
- _objc_msgSend$isActionButtonSupported
- _objc_msgSend$isAutoFPSVideoEnabledForMode:device:videoConfiguration:encodingBehavior:outputToExternalStorage:
- _objc_msgSend$isAutoFPSVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:
- _objc_msgSend$isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$isVariableFramerateVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:
- _objc_msgSend$isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:
- _objc_msgSend$isVideoStabilizationStrength:supportedForMode:devicePosition:
- _objc_msgSend$preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$resolvedVideoConfigurationForMode:device:videoEncodingBehavior:videoConfiguration:outputToExternalStorage:
- _objc_msgSend$sanitizeVideoConfigurationForDesiredConfiguration:mode:device:
- _objc_msgSend$setActiveButtons:
- _objc_msgSend$setDesiredButtons:
- _objc_msgSend$set_actionButtonInteraction:
- _objc_msgSend$videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:
- _objc_msgSend$videoEncodingBehaviorForConfiguration:mode:desiredProResVideoMode:outputToExternalStorage:
- _objc_msgSend$videoStabilizationStrengthForVideoStabilizationMode:captureMode:
CStrings:
+ "\x01\xf0\x91,\x13\x18"
+ "\x12\x12R\x82"
+ "!\x11"
+ "@\"<CAMStereoVideoCaptureStatusDelegate>\""
+ "@\"AVCaptureEventInteraction\""
+ "@\"CAMOrientationInstructionView\""
+ "@\"CAMSpatialCaptureButton\""
+ "@\"CAMSpatialCaptureInstructionLabel\""
+ "@\"CAMSpatialCaptureRecordingIndicator\""
+ "@200@0:8q16q24q32q40q48Q56q64@72@80q88q96B104B108q112q120B128B132Q136@144B152B156B160q164q172q180B188B192B196"
+ "@220@0:8q16q24q32q40q48q56q64q72q80q88q96q104q112q120d128d136B144@148q156q164q172@180Q188q196B204B208q212"
+ "@56@0:8@16@24q32q40@48"
+ "@60@0:8q16q24q32q40B48^q52"
+ "B\x15\x1c\x12"
+ "B48@0:8q16q24q32B40B44"
+ "B56@0:8q16q24q32q40B48B52"
+ "B64@0:8q16q24q32q40q48B56B60"
+ "Began"
+ "Beginning force landscape orientation, changing orientation from %{public}@ to %{public}@"
+ "CAMAccountController"
+ "CAMFeatureDevelopmentAllowSpatialVideoCapture"
+ "CAMFeatureDevelopmentForceSpatialVideoControlEnabled"
+ "CAMMotionControllerCaptureDeviceOrientationChangedNotification"
+ "CAMOrientationInstructionView"
+ "CAMSpatialCaptureButton"
+ "CAMSpatialCaptureInstructionLabel"
+ "CAMSpatialCaptureRecordingIndicator"
+ "CAMStereoVideoCaptureStatusDelegate"
+ "CAMStereoVideoCaptureStatusForAVStereoVideoCaptureStatus:"
+ "CAMUserDeviceListLastCheckDate"
+ "CAMUserPreferenceEnableSpatialVideoCaptureControl"
+ "CAMUserPreferencePreserveSpatialVideoEnabled"
+ "CAMUserPreferenceSpatialVideoEnabled"
+ "CameraUI-SpatialVideo"
+ "Cancelled"
+ "Device list request failed with missing response and error: %{public}@"
+ "Device list request failed with response error: %{public}@ and request error: %{public}@"
+ "Device list request succeeded with no reality device found"
+ "Device list request succeeded, reality device found"
+ "Ended"
+ "Ending force landscape orientation, changing orientation from %{public}@ to %{public}@"
+ "LockWhiteBalance"
+ "Photo format picker tapped from unsupported configuration: %{public}@"
+ "PreserveSpatialVideo"
+ "Primary button press stage: %{public}@"
+ "RealityDevice"
+ "SPATIAL_VIDEO_LANDSCAPE_ORIENTATION_INSTRUCTION_LABEL"
+ "SPATIAL_VIDEO_LOW_LIGHT_INSTRUCTION_LABEL"
+ "SPATIAL_VIDEO_SUBJECT_TOO_CLOSE_INSTRUCTION_LABEL"
+ "Secondary (volume-up) button press stage: %{public}@"
+ "Shortcuts"
+ "SpatialCaptureButton"
+ "SpatialVideoControl"
+ "T@\"<CAMStereoVideoCaptureStatusDelegate>\",W,N,V_stereoVideoCaptureStatusDelegate"
+ "T@\"AVCaptureEventInteraction\",&,N,V__physicalButtonInteraction"
+ "T@\"CAMOrientationInstructionView\",&,N,S_setOrientationInstructionView:,V__orientationInstructionView"
+ "T@\"CAMPhysicalCaptureNotifier\",&,N,V__cameraCaseShutterNotifier"
+ "T@\"CAMSpatialCaptureButton\",&,N,S_setSpatialCaptureButton:,V_spatialCaptureButton"
+ "T@\"CAMSpatialCaptureInstructionLabel\",&,N,S_setSpatialCaptureInstructionLabel:,V_spatialCaptureInstructionLabel"
+ "T@\"CAMSpatialCaptureRecordingIndicator\",&,N,S_setSpatialCaptureRecordingIndicator:,V_spatialCaptureRecordingIndicator"
+ "T@\"NSString\",R,N,V__hostProcess"
+ "T@\"UIVisualEffectView\",&,N,V__effectView"
+ "TB,N,G_isSpatialVideoEnabled,S_setSpatialVideoEnabled:,V__spatialVideoEnabled"
+ "TB,N,GisOrientationInstructionBackgroundBlurred,V_orientationInstructionBackgroundBlurred"
+ "TB,N,GisOrientationInstructionVisible,V_orientationInstructionVisible"
+ "TB,N,GisSpatialCaptureRecordingIndicatorVisible,V_spatialCaptureRecordingIndicatorVisible"
+ "TB,N,V_forceLandscapeOrientation"
+ "TB,N,V_hasBlurredBackground"
+ "TB,N,V_spatialEnabled"
+ "TB,R,N,GisSpatialVideoCaptureSupported,V_spatialVideoCaptureSupported"
+ "TB,R,N,V__spatialVideoEnabled"
+ "TB,R,N,V_enableStereoVideoCapture"
+ "TB,R,N,V_includesVolumeButtons"
+ "TB,R,N,V_preserveSpatialVideoEnabled"
+ "TB,R,N,V_spatialVideoControlEnabled"
+ "TB,R,N,V_spatialVideoEnabled"
+ "TQ,N,V__totalPortraitLightingChanges"
+ "Tq,N,S_setOrientationWhenForcedToLandscape:,V__orientationIfForcedToLandscape"
+ "Tq,N,S_setStereoVideoCaptureStatus:,V__stereoVideoCaptureStatus"
+ "Tq,N,V__firstConfiguredDevice"
+ "Tq,N,V__firstConfiguredMode"
+ "Tq,N,V__interfaceOrientation"
+ "Tq,N,V__launchMethod"
+ "Tq,N,V_deviceOrientation"
+ "Tq,N,V_stereoVideoCaptureStatus"
+ "T{?=ii},R,N"
+ "__cameraCaseShutterNotifier"
+ "__effectView"
+ "__firstConfiguredDevice"
+ "__firstConfiguredMode"
+ "__interfaceOrientation"
+ "__launchMethod"
+ "__orientationIfForcedToLandscape"
+ "__orientationInstructionView"
+ "__physicalButtonInteraction"
+ "__spatialVideoEnabled"
+ "__stereoVideoCaptureStatus"
+ "__totalPortraitLightingChanges"
+ "_cameraCaseShutterNotifier"
+ "_captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:resolvedDevice:"
+ "_configureStereoVideoCaptureEnabled:"
+ "_createAnalyticsSessionEventIfNeeded"
+ "_createCameraCaseShutterNotifierIfNeeded"
+ "_createPhysicalCaptureInteractionIfNeeded"
+ "_createPhysicalCaptureRecognizerIfNecessary"
+ "_defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:spatialVideoEnabled:overrodeWithForcedZoomValue:"
+ "_deviceAngleForGravity:captureOrientation:relativeRoll:relativePitch:"
+ "_deviceOrientationChanged:"
+ "_effectView"
+ "_enableStereoVideoCapture"
+ "_fallbackVideoConfigurationForUnsupportedConfiguration:spatialVideoEnabled:"
+ "_firstConfiguredDevice"
+ "_firstConfiguredMode"
+ "_forceLandscapeOrientation"
+ "_formatLabel"
+ "_frameForSpatialRecordingIndicatorWithElapsedTimeViewGeometry:orientation:"
+ "_handlePhysicalCaptureInteractionDidChangePhase:forButton:"
+ "_handleSpatialCaptureButtonTapped:"
+ "_hasBlurredBackground"
+ "_includesVolumeButtons"
+ "_isRealityDevice:"
+ "_isSpatialVideoActiveForMode:devicePosition:"
+ "_isSpatialVideoEnabled"
+ "_launchEventWithinReasonableTimeInterval"
+ "_launchMethod"
+ "_launchMethodToString:"
+ "_orientationIfForcedToLandscape"
+ "_orientationInstructionBackgroundBlurred"
+ "_orientationInstructionView"
+ "_orientationInstructionVisible"
+ "_physicalButtonInteraction"
+ "_preserveSpatialVideoEnabled"
+ "_resolvedTorchModeForGraphConfiguration:"
+ "_setOrientationInstructionView:"
+ "_setOrientationWhenForcedToLandscape:"
+ "_setSpatialCaptureButton:"
+ "_setSpatialCaptureInstructionLabel:"
+ "_setSpatialCaptureRecordingIndicator:"
+ "_setSpatialVideoEnabled:"
+ "_setStereoVideoCaptureStatus:"
+ "_setupStereoVideoCaptureStatusMonitoring"
+ "_shouldCheckPrimaryAccountForRegisteredRealityDevices"
+ "_shouldShowSpatialCaptureControlForGraphConfiguration:"
+ "_shouldShowSpatialCaptureInstructionsForGraphConfiguration:"
+ "_shouldShowVideoConfigurationIndicatorForGraphConfiguration:"
+ "_spatialCaptureButton"
+ "_spatialCaptureInstructionLabel"
+ "_spatialCaptureRecordingIndicator"
+ "_spatialCaptureRecordingIndicatorVisible"
+ "_spatialEnabled"
+ "_spatialVideoCaptureSupported"
+ "_spatialVideoControlEnabled"
+ "_spatialVideoEnabled"
+ "_stereoVideoCaptureStatus"
+ "_stereoVideoCaptureStatusChangedForKeyPath:ofObject:change:"
+ "_stereoVideoCaptureStatusDelegate"
+ "_stringForStereoVideoCaptureStatus:"
+ "_teardownStereoVideoCaptureStatusMonitoring"
+ "_totalPortraitLightingChanges"
+ "_updateSpatialCaptureUIStateForGraphConfiguration:animated:"
+ "_updateTorchModeForGraphConfiguration:animated:"
+ "aa_primaryAppleAccount"
+ "applyDeviceMotion:captureOrientation:"
+ "cameraConnectionIsSpatialCapture:"
+ "captureController:didOutputStereoVideoCaptureStatus:"
+ "checkPrimaryAccountForRegisteredRealityDevices"
+ "colorSpaceForMode:videoConfiguration:videoEncodingBehavior:spatialVideoEnabled:"
+ "currentCameraDevice.stereoVideoCaptureStatus"
+ "d88@0:8q16q24q32q40q48q56q64B72B76^B80"
+ "defaultDeviceForModeChange:devicePosition:spatialVideoEnabled:"
+ "defaultStore"
+ "didChangePortraitLighting"
+ "didLaunchShortCutItemWithMode:device:"
+ "didLaunchWithURLConfigurationRequest:"
+ "enableStereoVideoCapture"
+ "fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:macroMode:spatialVideoEnabled:"
+ "firstConfiguredDevice"
+ "firstConfiguredMode"
+ "forceLandscapeOrientation"
+ "fullscreenViewfinderDidCreateSpatialCaptureButton:"
+ "generateAnalyticsForLaunchWithShortCutItem:"
+ "generateAnalyticsForLaunchWithURLConfigurationRequest:"
+ "hasBlurredBackground"
+ "includesVolumeButtons"
+ "initWithAccount:"
+ "initWithAttributedString:"
+ "initWithCapabilities:availableCaptureModes:currentCaptureMode:currentCaptureDevice:callStatusMonitor:"
+ "initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:enableDepthSuggestion:enableZoomPIP:enableStereoVideoCapture:"
+ "initWithCaptureMode:captureDevice:videoConfiguration:audioConfiguration:flashMode:torchMode:HDRMode:irisMode:timerDuration:photoModeAspectRatioCrop:photoModeEffectFilterType:squareModeEffectFilterType:portraitModeEffectFilterType:portraitModeLightingEffectType:portraitModeApertureValue:portraitModeIntensityValue:mirrorFrontCameraCaptures:exposureBiasesByMode:macroMode:rawMode:proResVideoMode:semanticStyles:selectedSemanticStyleIndex:videoStabilizationMode:zoomPIPEnabled:spatialVideoEnabled:sharedLibraryMode:"
+ "initWithPrimaryEventHandler:secondaryEventHandler:"
+ "initWithView:includeVolumeButtons:"
+ "isAutoFPSVideoEnabledForMode:device:videoConfiguration:encodingBehavior:outputToExternalStorage:spatialVideoEnabled:"
+ "isAutoFPSVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:spatialVideoEnabled:"
+ "isOrientationInstructionBackgroundBlurred"
+ "isOrientationInstructionVisible"
+ "isSpatialCaptureRecordingIndicatorVisible"
+ "isSpatialVideoCaptureSupported"
+ "isSpatialVideoSupportedForMode:devicePosition:"
+ "isStereoVideoCaptureSupported"
+ "isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:"
+ "isSupportedVideoConfiguration:forMode:device:spatialVideoEnabled:"
+ "isVariableFramerateVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:spatialVideoEnabled:"
+ "isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:spatialVideoEnabled:"
+ "isVideoStabilizationStrength:supportedForMode:devicePosition:spatialVideoEnabled:"
+ "launchMethod"
+ "orientationInstructionBackgroundBlurred"
+ "orientationInstructionVisible"
+ "performRequestWithHandler:"
+ "phase"
+ "predictedFinalAssetPhotoDimensions"
+ "preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:"
+ "preserveSpatialVideoEnabled"
+ "q56@0:8q16q24q32q40B48B52"
+ "q60@0:8q16q24q32q40q48B56"
+ "rectangle.portrait.rotate"
+ "resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:"
+ "resolvedVideoConfigurationForMode:device:videoEncodingBehavior:videoConfiguration:outputToExternalStorage:spatialVideoEnabled:"
+ "sanitizeVideoConfigurationForDesiredConfiguration:mode:device:spatialVideoEnabled:"
+ "setDeviceOrientation:"
+ "setDeviceOrientation:animated:"
+ "setForceLandscapeOrientation:"
+ "setHasBlurredBackground:"
+ "setHasBlurredBackground:animated:"
+ "setOrientationInstructionBackgroundBlurred:"
+ "setOrientationInstructionBackgroundBlurred:animated:"
+ "setOrientationInstructionVisible:"
+ "setOrientationInstructionVisible:animated:"
+ "setSpatialCaptureRecordingIndicatorVisible:"
+ "setSpatialCaptureRecordingIndicatorVisible:animated:"
+ "setSpatialEnabled:"
+ "setStereoVideoCaptureEnabled:"
+ "setStereoVideoCaptureStatus:"
+ "setStereoVideoCaptureStatus:animated:"
+ "setStereoVideoCaptureStatusDelegate:"
+ "set_cameraCaseShutterNotifier:"
+ "set_effectView:"
+ "set_firstConfiguredDevice:"
+ "set_firstConfiguredMode:"
+ "set_interfaceOrientation:"
+ "set_launchMethod:"
+ "set_physicalButtonInteraction:"
+ "set_totalPortraitLightingChanges:"
+ "sortedArrayUsingSelector:"
+ "spatialCaptureButton"
+ "spatialCaptureInstructionLabel"
+ "spatialCaptureRecordingIndicator"
+ "spatialCaptureRecordingIndicatorVisible"
+ "spatialEnabled"
+ "spatialModeDidChange"
+ "spatialVideoCaptureSupported"
+ "spatialVideoControlEnabled"
+ "spatialVideoEnabled"
+ "statusCode"
+ "stereoVideoCaptureStatus"
+ "stereoVideoCaptureStatusDelegate"
+ "v16@?0@\"AVCaptureEvent\"8"
+ "v32@0:8Q16q24"
+ "v32@?0@\"AADevice\"8Q16^B24"
+ "v32@?0@\"AARequest\"8@\"AAResponse\"16@\"NSError\"24"
+ "videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:spatialVideoEnabled:resolvedDevice:"
+ "videoEncodingBehaviorForConfiguration:mode:desiredProResVideoMode:outputToExternalStorage:spatialVideoEnabled:"
+ "videoStabilizationStrengthForVideoStabilizationMode:captureMode:spatialVideoEnabled:"
+ "visionpro"
+ "yO\x05\x12\x12\x14\x13\x1f\x02"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}120@0:8{?={CGRect={CGPoint=dd}{CGSize=dd}}{CGPoint=dd}{CGAffineTransform=dddddd}}16q112"
+ "\x92\xf0\xf0\xf0\xf0\xf0\xf0\xf0Q\xf0\xf0\xf0\xb3\x11"
+ "\xbf\x031\xf0\xe1!\x11?\x05/\r-2\x12\x14!B\x12\x1f\x011a"
- "\x01\xf0\x91\x1c\x13\x18"
- "\x11\x12Rr"
- "@196@0:8q16q24q32q40q48Q56q64@72@80q88q96B104B108q112q120B128B132Q136@144B152B156B160q164q172q180B188B192"
- "@216@0:8q16q24q32q40q48q56q64q72q80q88q96q104q112q120d128d136B144@148q156q164q172@180Q188q196B204q208"
- "@56@0:8q16q24q32q40^q48"
- "B\x15\x1c\x11"
- "B60@0:8q16q24q32q40q48B56"
- "CAMFeatureDevelopmentAllowStaccatoSimulation"
- "CameraUI-ExternalStorage"
- "CameraUI-PhotoModeDepth"
- "CameraUI-R850"
- "Must have a view when installing the physical capture recognizer."
- "T@\"CAMPhysicalCaptureNotifier\",&,N,V__physicalCaptureNotifier"
- "T@\"NSString\",&,N,V__hostProcess"
- "TB,R,N,V_allowActionButtonSimulation"
- "Td,N,V__startTime"
- "Tq,R,N,V_deviceOrientation"
- "__physicalCaptureNotifier"
- "_allowActionButtonSimulation"
- "_captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:"
- "_configurationWithPhysicalButton:behavior:behaviorOptions:"
- "_createPhysicalCaptureRecognizerOrNotifierIfNecessary"
- "_defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:overrodeWithForcedZoomValue:"
- "_deviceAngleForGravity:deviceOrientation:relativeRoll:relativePitch:"
- "_fallbackVideoConfigurationForUnsupportedConfiguration:"
- "_physicalCaptureNotifier"
- "_resolvedTorchModeForDesiredTorchMode"
- "_updateTorchModeAnimated:"
- "allowActionButtonSimulation"
- "applyDeviceMotion:deviceOrientation:"
- "colorSpaceForMode:videoConfiguration:videoEncodingBehavior:"
- "d84@0:8q16q24q32q40q48q56q64B72^B76"
- "defaultDeviceForModeChange:devicePosition:"
- "fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:macroMode:"
- "i?\x05\x12\x12\x14\x1f\x01"
- "initWithCapabilities:availableCaptureModes:callStatusMonitor:"
- "initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:enableDepthSuggestion:enableZoomPIP:"
- "initWithCaptureMode:captureDevice:videoConfiguration:audioConfiguration:flashMode:torchMode:HDRMode:irisMode:timerDuration:photoModeAspectRatioCrop:photoModeEffectFilterType:squareModeEffectFilterType:portraitModeEffectFilterType:portraitModeLightingEffectType:portraitModeApertureValue:portraitModeIntensityValue:mirrorFrontCameraCaptures:exposureBiasesByMode:macroMode:rawMode:proResVideoMode:semanticStyles:selectedSemanticStyleIndex:videoStabilizationMode:zoomPIPEnabled:sharedLibraryMode:"
- "initWithConfigurations:delegate:"
- "initWithView:"
- "isAutoFPSVideoEnabledForMode:device:videoConfiguration:encodingBehavior:outputToExternalStorage:"
- "isAutoFPSVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:"
- "isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:"
- "isVariableFramerateVideoSupportedForMode:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:"
- "isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:"
- "isVideoStabilizationStrength:supportedForMode:devicePosition:"
- "preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:"
- "q48@0:8q16q24q32q40"
- "q56@0:8q16q24q32q40q48"
- "resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:"
- "resolvedVideoConfigurationForMode:device:videoEncodingBehavior:videoConfiguration:outputToExternalStorage:"
- "sanitizeVideoConfigurationForDesiredConfiguration:mode:device:"
- "set_hostProcess:"
- "set_physicalCaptureNotifier:"
- "set_startTime:"
- "videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:"
- "videoEncodingBehaviorForConfiguration:mode:desiredProResVideoMode:outputToExternalStorage:"
- "videoStabilizationStrengthForVideoStabilizationMode:captureMode:"
- "\x92\xf0\xf0\xf0\xf0\xf0\xf0\xf0A\xf0\xf0\xf0\xa3\x11"
- "\xbf\x031\xf0\xd1!\x11?\x05/\r,2\x12\x14!B\x12\x1f\x011a"

```
