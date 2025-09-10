## CameraUI

> `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`

```diff

 4097.6.9.0.3
-  __TEXT.__text: 0x3afd4c
-  __TEXT.__auth_stubs: 0x6490
-  __TEXT.__objc_methlist: 0x2ec18
-  __TEXT.__const: 0x1d614
-  __TEXT.__gcc_except_tab: 0x32c8
-  __TEXT.__cstring: 0x1e087
-  __TEXT.__oslogstring: 0x158b4
+  __TEXT.__text: 0x3ca690
+  __TEXT.__auth_stubs: 0x6560
+  __TEXT.__objc_methlist: 0x2ff60
+  __TEXT.__const: 0x1e2d4
+  __TEXT.__gcc_except_tab: 0x33c0
+  __TEXT.__cstring: 0x1efb7
+  __TEXT.__oslogstring: 0x162a4
   __TEXT.__dlopen_cstrs: 0x407
   __TEXT.__ustring: 0x8
-  __TEXT.__constg_swiftt: 0x5530
-  __TEXT.__swift5_typeref: 0x225d6
-  __TEXT.__swift5_reflstr: 0x51ea
-  __TEXT.__swift5_fieldmd: 0x4938
+  __TEXT.__constg_swiftt: 0x572c
+  __TEXT.__swift5_typeref: 0x227b6
+  __TEXT.__swift5_reflstr: 0x56da
+  __TEXT.__swift5_fieldmd: 0x4b24
   __TEXT.__swift5_builtin: 0x3d4
   __TEXT.__swift5_assocty: 0x1540
-  __TEXT.__swift5_proto: 0x9e0
-  __TEXT.__swift5_types: 0x50c
-  __TEXT.__swift5_capture: 0x252c
+  __TEXT.__swift5_proto: 0xa04
+  __TEXT.__swift5_types: 0x518
+  __TEXT.__swift5_capture: 0x261c
   __TEXT.__swift_as_entry: 0xd0
   __TEXT.__swift_as_ret: 0xc4
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xe368
+  __TEXT.__unwind_info: 0xe8d8
   __TEXT.__eh_frame: 0x2ac0
-  __TEXT.__objc_classname: 0x55a9
-  __TEXT.__objc_methname: 0x991b6
-  __TEXT.__objc_methtype: 0x1017e
-  __TEXT.__objc_stubs: 0x58820
-  __DATA_CONST.__got: 0x4180
-  __DATA_CONST.__const: 0x7a28
-  __DATA_CONST.__objc_classlist: 0x11e8
+  __TEXT.__objc_classname: 0x5708
+  __TEXT.__objc_methname: 0x9fa0e
+  __TEXT.__objc_methtype: 0x1095d
+  __TEXT.__objc_stubs: 0x5b660
+  __DATA_CONST.__got: 0x4360
+  __DATA_CONST.__const: 0x7d40
+  __DATA_CONST.__objc_classlist: 0x1238
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x7a8
+  __DATA_CONST.__objc_protolist: 0x7b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x195a8
+  __DATA_CONST.__objc_selrefs: 0x1a1d8
   __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__objc_superrefs: 0xd68
-  __DATA_CONST.__objc_arraydata: 0x1008
-  __AUTH_CONST.__auth_got: 0x3258
-  __AUTH_CONST.__const: 0xd598
-  __AUTH_CONST.__cfstring: 0x15b40
-  __AUTH_CONST.__objc_const: 0x4e978
-  __AUTH_CONST.__objc_intobj: 0x17e8
-  __AUTH_CONST.__objc_doubleobj: 0x540
+  __DATA_CONST.__objc_superrefs: 0xdb8
+  __DATA_CONST.__objc_arraydata: 0x1040
+  __AUTH_CONST.__auth_got: 0x32c0
+  __AUTH_CONST.__const: 0xd840
+  __AUTH_CONST.__cfstring: 0x163a0
+  __AUTH_CONST.__objc_const: 0x50b10
+  __AUTH_CONST.__objc_intobj: 0x1878
+  __AUTH_CONST.__objc_doubleobj: 0x550
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH_CONST.__objc_arrayobj: 0xca8
+  __AUTH_CONST.__objc_arrayobj: 0xcf0
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH.__objc_data: 0x57a8
+  __AUTH.__objc_data: 0x5a88
   __AUTH.__data: 0xc08
-  __DATA.__objc_ivar: 0x3adc
-  __DATA.__data: 0xa0e8
-  __DATA.__bss: 0x102f0
-  __DATA.__common: 0x188
-  __DATA_DIRTY.__objc_data: 0x7580
-  __DATA_DIRTY.__data: 0x3c48
+  __DATA.__objc_ivar: 0x3cc8
+  __DATA.__data: 0xa278
+  __DATA.__bss: 0x10900
+  __DATA.__common: 0x190
+  __DATA_DIRTY.__objc_data: 0x77b0
+  __DATA_DIRTY.__data: 0x3cf8
   __DATA_DIRTY.__bss: 0x3e40
-  __DATA_DIRTY.__common: 0xa8
+  __DATA_DIRTY.__common: 0xb0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 45EDCB6B-22D9-3D13-998A-EC19D4675B23
-  Functions: 24921
-  Symbols:   58942
-  CStrings:  30663
+  UUID: D6CA0815-3230-3714-BA02-F41427179A68
+  Functions: 25618
+  Symbols:   60455
+  CStrings:  31550
 
Symbols:
+ +[CAMCaptureConfiguration _fallbackVideoConfigurationForUnsupportedConfiguration:frontRearSimultaneousVideoEnabled:]
+ +[CAMCaptureConfiguration sanitizeVideoConfigurationForDesiredConfiguration:mode:device:trueVideoEnabled:frontRearSimultaneousVideoEnabled:]
+ +[CAMCaptureConversions AVCaptureDynamicAspectRatioForCAMDynamicAspectRatio:]
+ +[CAMCaptureConversions AVCaptureSmartFramingFieldOfViewForCAMCaptureSmartFramingFieldOfView:]
+ +[CAMCaptureConversions CAMCaptureSmartFramingFieldOfViewForAVCaptureSmartFraming:]
+ +[CAMCaptureConversions CAMCaptureSmartFramingFieldOfViewForAVCaptureSmartFramingFieldOfView:]
+ +[CAMCaptureConversions CMVideoDimensionsForCAMPhotoResolution:wantsSquareDimensions:]
+ +[CAMConflictingControlConfiguration resolveDesiredMacroMode:forMode:device:videoConfiguration:videoStabilizationStrength:photoFormat:optionalDepthEffectEnabled:frontRearSimultaneousVideoEnabled:]
+ +[CAMPIPVideoPreviewView cornerRadiusForContainerWidth:]
+ +[CAMPIPVideoPreviewView defaultAnchor]
+ +[CAMPIPVideoPreviewView futureThrowTime]
+ +[CAMPIPVideoPreviewView pipInsetForViewportSize:]
+ +[CAMPIPVideoPreviewView pipOutsetForViewportSize:]
+ +[CAMPIPVideoPreviewView sizeForViewportSize:]
+ +[CAMUserPreferences bottomOverCaptureGradientEnabled]
+ +[CAMUserPreferences setBottomOverCaptureGradientEnabled:]
+ +[CAMUserPreferences setTopOverCaptureGradientEnabled:]
+ +[CAMUserPreferences topOverCaptureGradientEnabled]
+ +[CAMZoomControlUtilities exifFocalLengthsByZoomFactorForMode:device:videoConfiguration:videoStabilizationStrength:customLensGroup:isTrueVideo:frontRearSimultaneousVideoEnabled:]
+ +[CAMZoomControlUtilities shouldApplyContinuousZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:zoomFactors:displayZoomFactors:]
+ +[CAMZoomControlUtilities shouldEmulateTripleCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:]
+ +[CAMZoomControlUtilities shouldEmulateWideDualCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:]
+ +[CAMZoomControlUtilities zoomControlDisplayValueForZoomFactor:mode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:]
+ +[CAMZoomControlUtilities zoomControlDisplayValueForZoomFactor:mode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:].cold.1
+ -[AVCaptureDevice(CAMCaptureEngine) cam_frontFacingFormatForVideoConfiguration:videoEncodingBehavior:colorSpace:dynamicAspectRatio:useSquareFormat:requireVideoBinned:]
+ -[AVCaptureDeviceFormat(CAMCaptureEngine) cam_supportsFrontFacingFormatForVideoConfiguration:colorSpace:enableProResVideo:dynamicAspectRatio:useSquareFormat:requireVideoBinned:]
+ -[AVCaptureSession(CAMCaptureEngine) cam_addConnectionWithMediaType:fromDeviceInput:toOutput:]
+ -[AVCaptureSession(CAMCaptureEngine) cam_connectionWithMediaType:fromDeviceInput:toOutput:]
+ -[AVCaptureSession(CAMCaptureEngine) cam_ensureConnections:]
+ -[AVCaptureSession(CAMCaptureEngine) cam_ensureVideoPreviewLayers:withConnections:whileRemoving:]
+ -[CAMAnalyticsCaptureEvent populateZoomFieldOfView:graphConfiguration:smartFramingSource:]
+ -[CAMAutoFPSVideoCommand _configureSecondaryDevice]
+ -[CAMAutoFPSVideoCommand initWithAutoFPSVideoEnabled:configureSecondaryDevice:]
+ -[CAMAutoSmartFramingEnabledFieldOfViewsCommand .cxx_destruct]
+ -[CAMAutoSmartFramingEnabledFieldOfViewsCommand _enabledSmartFramingsFromSupportedFieldOfViews:]
+ -[CAMAutoSmartFramingEnabledFieldOfViewsCommand _isSmartFramingFieldOfView:equalToAVCaptureSmartFraming:]
+ -[CAMAutoSmartFramingEnabledFieldOfViewsCommand _smartFramingEnabledFieldsOfView]
+ -[CAMAutoSmartFramingEnabledFieldOfViewsCommand _smartFramingForSmartFramingFieldOfView:supportedFieldOfViews:]
+ -[CAMAutoSmartFramingEnabledFieldOfViewsCommand copyWithZone:]
+ -[CAMAutoSmartFramingEnabledFieldOfViewsCommand encodeWithCoder:]
+ -[CAMAutoSmartFramingEnabledFieldOfViewsCommand executeWithContext:]
+ -[CAMAutoSmartFramingEnabledFieldOfViewsCommand initWithCoder:]
+ -[CAMAutoSmartFramingEnabledFieldOfViewsCommand initWithSmartFramingEnabledFieldOfViews:]
+ -[CAMAutoSmartFramingMonitorCommand _enabled]
+ -[CAMAutoSmartFramingMonitorCommand copyWithZone:]
+ -[CAMAutoSmartFramingMonitorCommand encodeWithCoder:]
+ -[CAMAutoSmartFramingMonitorCommand executeWithContext:]
+ -[CAMAutoSmartFramingMonitorCommand executeWithContext:].cold.1
+ -[CAMAutoSmartFramingMonitorCommand initWithCoder:]
+ -[CAMAutoSmartFramingMonitorCommand initWithSmartFramingMonitorEnabled:]
+ -[CAMCaptureCapabilities _HDR10BitVideoSupports240FPS]
+ -[CAMCaptureCapabilities _dynamicAspectRatioInCinematicModeSupported]
+ -[CAMCaptureCapabilities _dynamicAspectRatioInVideoModeSupported]
+ -[CAMCaptureCapabilities _shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities backQuadraTeleFocalLengthDisplayValue]
+ -[CAMCaptureCapabilities defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:isTrueVideo:frontRearSimultaneousVideoEnabled:prefersHDR10BitVideo:smartFramingFieldOfView:overrodeWithForcedZoomValue:]
+ -[CAMCaptureCapabilities dynamicAspectRatioSupported]
+ -[CAMCaptureCapabilities fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:macroMode:]
+ -[CAMCaptureCapabilities isActionModeControlSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities isAutoSmartFramingSupported]
+ -[CAMCaptureCapabilities isBackQuadraTeleSupported]
+ -[CAMCaptureCapabilities isDynamicAspectRatioSupportedForMode:devicePosition:]
+ -[CAMCaptureCapabilities isDynamicAspectRatioSupportedForMode:videoConfiguration:devicePosition:]
+ -[CAMCaptureCapabilities isEnhancedStabilizationSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities isFrontRearSimultaneousVideo60FPSSupported]
+ -[CAMCaptureCapabilities isFrontRearSimultaneousVideoDeferredFrontCameraEnabled]
+ -[CAMCaptureCapabilities isFrontRearSimultaneousVideoFrontCameraHDR10Supported]
+ -[CAMCaptureCapabilities isFrontRearSimultaneousVideoFrontVideoStabilizationSupported]
+ -[CAMCaptureCapabilities isFrontRearSimultaneousVideoSupportedForMode:]
+ -[CAMCaptureCapabilities isFrontRearSimultaneousVideoSupportedForMode:devicePosition:]
+ -[CAMCaptureCapabilities isFrontRearSimultaneousVideoSupportedForVideoConfiguration:]
+ -[CAMCaptureCapabilities isFrontRearSimultaneousVideoSupported]
+ -[CAMCaptureCapabilities isLensPositionControlSupportedForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities isQuadraTeleBinningReconfigurationSupportedForMode:devicePosition:videoConfiguration:]
+ -[CAMCaptureCapabilities isQuadraTeleZoomButtonSupportedForMode:devicePosition:videoConfiguration:]
+ -[CAMCaptureCapabilities isSmartFramingSupportedForMode:devicePosition:]
+ -[CAMCaptureCapabilities isSmartFramingSupported]
+ -[CAMCaptureCapabilities isSmartFramingUsingDynamicAspectRatioSupported]
+ -[CAMCaptureCapabilities isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities isSupportedVideoConfiguration:forMode:device:trueVideoEnabled:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities isTripleCameraSupportedForMode:devicePosition:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities isVideoStabilizationStrength:supportedForMode:devicePosition:trueVideoEnabled:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities isZoomPIPSupportedForMode:devicePosition:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities quadraTeleDisplayZoomFactor]
+ -[CAMCaptureCapabilities quadraTeleRelativeZoomFactor]
+ -[CAMCaptureCapabilities resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:]
+ -[CAMCaptureCapabilities smartFramingFieldOfViewLandscapeZoomFactor]
+ -[CAMCaptureCapabilities smartFramingFieldOfViewPortraitZoomFactor]
+ -[CAMCaptureCapabilities smartFramingFieldOfViewZoomedOutLandscapeZoomFactor]
+ -[CAMCaptureCapabilities smartFramingFieldOfViewZoomedOutPortraitZoomFactor]
+ -[CAMCaptureCapabilities useMultiCamSession]
+ -[CAMCaptureCapabilities useSquareFormatForDynamicAspectRatioForMode:videoConfiguration:]
+ -[CAMCaptureCapabilities zoomFactorForSmartFramingFieldOfView:]
+ -[CAMCaptureCommandContext _captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:resolvedDevice:]
+ -[CAMCaptureCommandContext currentSecondaryVideoDeviceFormat]
+ -[CAMCaptureCommandContext currentSecondaryVideoDeviceInput]
+ -[CAMCaptureCommandContext currentSecondaryVideoDevice]
+ -[CAMCaptureCommandContext currentSecondaryVideoPreviewLayer]
+ -[CAMCaptureCommandContext primaryVideoPreviewLayerForGraphConfiguration:]
+ -[CAMCaptureCommandContext secondaryVideoPreviewLayerForGraphConfiguration:]
+ -[CAMCaptureCommandContext setCurrentSecondaryVideoDevice:]
+ -[CAMCaptureCommandContext setCurrentSecondaryVideoDeviceFormat:]
+ -[CAMCaptureCommandContext setCurrentSecondaryVideoDeviceInput:]
+ -[CAMCaptureCommandContext setCurrentSecondaryVideoPreviewLayer:]
+ -[CAMCaptureCommandContext videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:resolvedDevice:]
+ -[CAMCaptureEngine _multiCamPIPCompositingQueue]
+ -[CAMCaptureEngine _multiCamPIPCompositingQueue_multiCamPIPCompositor]
+ -[CAMCaptureEngine _secondaryVideoDeviceInputFromSession:]
+ -[CAMCaptureEngine _secondaryVideoPreviewLayer]
+ -[CAMCaptureEngine captureOutput:readyForClientCompositingForOutputFileAtURL:compositingData:]
+ -[CAMCaptureEngine captureOutput:readyForClientCompositingForResolvedSettings:compositingData:]
+ -[CAMCaptureEngine secondaryVideoPreviewLayer]
+ -[CAMCaptureEngine setMultiCamPictureInPictureMetrics:]
+ -[CAMCaptureEngine setMultiCamPictureInPictureMotionBlurDisabled:]
+ -[CAMCaptureEngine set_multiCamPIPCompositingQueue_multiCamPIPCompositor:]
+ -[CAMCaptureEngineDevice _cachedDynamicAspectRatioFormat]
+ -[CAMCaptureEngineDevice _deviceFormatForDynamicAspectRatioWithGraphConfiguration:deviceIsSecondary:]
+ -[CAMCaptureEngineDevice videoDeviceFormatForGraphConfiguration:captureSession:deviceIsSecondary:]
+ -[CAMCaptureGraphConfiguration frontRearSimultaneousVideoEnabled]
+ -[CAMCaptureGraphConfiguration initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:mixAudioWithOthers:windNoiseRemovalEnabled:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:smartStyles:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:videoBinned:enableDepthSuggestion:enableZoomPIP:customLensGroup:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:videoDynamicAspectRatio:smartFramingFieldOfView:]
+ -[CAMCaptureGraphConfiguration isSecondaryDeviceVideoBinned]
+ -[CAMCaptureGraphConfiguration secondaryDevice:]
+ -[CAMCaptureGraphConfiguration secondaryDeviceColorSpace]
+ -[CAMCaptureGraphConfiguration secondaryDeviceUsesPrimaryVideoConfigurationForFrameRate]
+ -[CAMCaptureGraphConfiguration secondaryDeviceVideoConfiguration]
+ -[CAMCaptureGraphConfiguration secondaryDeviceVideoDynamicAspectRatio]
+ -[CAMCaptureGraphConfiguration secondaryDeviceVideoStabilizationStrength]
+ -[CAMCaptureGraphConfiguration smartFramingFieldOfView]
+ -[CAMCaptureGraphConfiguration videoDynamicAspectRatio]
+ -[CAMCaptureMovieFileOutput captureOutput:readyForClientCompositingForOutputFileAtURL:compositingData:]
+ -[CAMControlStatusBar autoFramingIndicator]
+ -[CAMDynamicAspectRatioCommand _configureForSecondaryDevice]
+ -[CAMDynamicAspectRatioCommand _devicePosition]
+ -[CAMDynamicAspectRatioCommand _dynamicAspectRatio]
+ -[CAMDynamicAspectRatioCommand _executeForCurrentDeviceWithContext:]
+ -[CAMDynamicAspectRatioCommand _executeForSecondaryDeviceWithContext:]
+ -[CAMDynamicAspectRatioCommand _mode]
+ -[CAMDynamicAspectRatioCommand _smartFramingFieldOfView]
+ -[CAMDynamicAspectRatioCommand _videoConfiguration]
+ -[CAMDynamicAspectRatioCommand _videoDynamicAspectRatio]
+ -[CAMDynamicAspectRatioCommand copyWithZone:]
+ -[CAMDynamicAspectRatioCommand encodeWithCoder:]
+ -[CAMDynamicAspectRatioCommand executeWithContext:]
+ -[CAMDynamicAspectRatioCommand initForSecondaryDevice]
+ -[CAMDynamicAspectRatioCommand initWithCoder:]
+ -[CAMDynamicAspectRatioCommand initWithSmartFramingFieldOfView:videoDynamicAspectRatio:mode:videoConfiguration:devicePosition:]
+ -[CAMDynamicAspectRatioCommand initWithSmartFramingFieldOfView:videoDynamicAspectRatio:mode:videoConfiguration:devicePosition:configureForSecondaryDevice:]
+ -[CAMExposureCommand _configureSecondaryDevice]
+ -[CAMExposureCommand initWithExposureMode:atPointOfInterest:configureSecondaryDevice:]
+ -[CAMExposureTargetBiasCommand _configureSecondaryDevice]
+ -[CAMExposureTargetBiasCommand initWithExposureTargetBias:configureSecondaryDevice:]
+ -[CAMFlipAspectRatioButton accessibilityIdentifier]
+ -[CAMFlipAspectRatioButton active]
+ -[CAMFlipAspectRatioButton imageNameForCurrentState]
+ -[CAMFlipAspectRatioButton initWithFrame:]
+ -[CAMFlipAspectRatioButton setActive:]
+ -[CAMFlipAspectRatioButton setActive:animated:]
+ -[CAMFlipAspectRatioButton setOrientation:]
+ -[CAMFlipAspectRatioButton setOrientation:animated:]
+ -[CAMFlipAspectRatioButton shouldShowSlashForCurrentState]
+ -[CAMFlipAspectRatioButton shouldUseActiveTintForCurrentState]
+ -[CAMFlipAspectRatioButton useThinMaterialBackground]
+ -[CAMFocusCommand _configureSecondaryDevice]
+ -[CAMFocusCommand initWithFocusMode:atPointOfInterest:rectSize:smooth:configureSecondaryDevice:]
+ -[CAMFrontPIPButton accessibilityIdentifier]
+ -[CAMFrontPIPButton active]
+ -[CAMFrontPIPButton imageNameForCurrentState]
+ -[CAMFrontPIPButton initWithFrame:]
+ -[CAMFrontPIPButton setActive:]
+ -[CAMFrontPIPButton shouldShowSlashForCurrentState]
+ -[CAMFrontPIPButton shouldUseActiveTintForCurrentState]
+ -[CAMFrontRearSimultaneousCaptureCommand _isEnabled]
+ -[CAMFrontRearSimultaneousCaptureCommand copyWithZone:]
+ -[CAMFrontRearSimultaneousCaptureCommand executeWithContext:]
+ -[CAMFrontRearSimultaneousCaptureCommand initWithFrontRearSimultaneousCaptureEnabled:]
+ -[CAMFrontRearSimultaneousCaptureCommand initWithSubcommands:]
+ -[CAMFrontRearSimultaneousVideoRecordingCommand _isEnabled]
+ -[CAMFrontRearSimultaneousVideoRecordingCommand copyWithZone:]
+ -[CAMFrontRearSimultaneousVideoRecordingCommand executeWithContext:]
+ -[CAMFrontRearSimultaneousVideoRecordingCommand initWithSubcommands:]
+ -[CAMFrontRearSimultaneousVideoRecordingCommand initWithVideoRecordingEnabled:]
+ -[CAMFullscreenViewfinder _frontPIPButtonFrame]
+ -[CAMFullscreenViewfinder _layoutViewportWithFrame:previewFrame:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:]
+ -[CAMFullscreenViewfinder _setFlipAspectRatioButton:]
+ -[CAMFullscreenViewfinder _setFrontPIPButton:]
+ -[CAMFullscreenViewfinder _updatePreviewLayerForPreviewFrame:viewportFrame:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:]
+ -[CAMFullscreenViewfinder _useSmartFramingTransition]
+ -[CAMFullscreenViewfinder flipAspectRatioButton]
+ -[CAMFullscreenViewfinder frontPIPButtonVisible]
+ -[CAMFullscreenViewfinder frontPIPButton]
+ -[CAMFullscreenViewfinder isFlipAspectRatioButtonVisible]
+ -[CAMFullscreenViewfinder offsetZoomButtonForFlipAspectRatioButton]
+ -[CAMFullscreenViewfinder setFlipAspectRatioButtonVisible:]
+ -[CAMFullscreenViewfinder setFlipAspectRatioButtonVisible:animated:]
+ -[CAMFullscreenViewfinder setFrontPIPButtonVisible:]
+ -[CAMFullscreenViewfinder setFrontPIPButtonVisible:animated:]
+ -[CAMFullscreenViewfinder setOffsetZoomButtonForFlipAspectRatioButton:]
+ -[CAMFullscreenViewfinder setOffsetZoomButtonForFlipAspectRatioButton:animated:]
+ -[CAMFullscreenViewfinder setSmartFramingFieldOfView:]
+ -[CAMFullscreenViewfinder setSmartFramingFieldOfView:useTransition:animated:]
+ -[CAMFullscreenViewfinder set_useSmartFramingTransition:]
+ -[CAMFullscreenViewfinder smartFramingFieldOfView]
+ -[CAMModeAndDeviceCommand _desiredSecondaryInputsWithCaptureEngineSecondaryDevice:]
+ -[CAMModeAndDeviceCommand _existingVideoPreviewLayersWithContext:without:]
+ -[CAMModeAndDeviceCommand _secondaryEngineDeviceWithContext:graphConfiguration:resolvedDevice:]
+ -[CAMModeAndDeviceCommand _secondaryInputsBecomingPrimaryWithContext:desiredPrimaryInputs:]
+ -[CAMModeAndDeviceCommand _specificFramerateCommandForGraphConfiguration:withContext:configureSecondaryDevice:]
+ -[CAMModeAndDeviceCommand executeWithContext:].cold.5
+ -[CAMMultiCamPIPCompositor .cxx_destruct]
+ -[CAMMultiCamPIPCompositor _applyMaskAndBorderToImage:cornerRadius:borderWidth:borderColor:]
+ -[CAMMultiCamPIPCompositor _calculateMotionBlurAngle:motionBlurRadius:forPictureInPictureFrame:fromPictureInPictureFrame:]
+ -[CAMMultiCamPIPCompositor _calculateMotionBlurAngle:motionBlurRadius:forPictureInPictureFrame:fromPictureInPictureFrame:].cold.1
+ -[CAMMultiCamPIPCompositor _ciContext]
+ -[CAMMultiCamPIPCompositor _commandQueue]
+ -[CAMMultiCamPIPCompositor _compositePrimaryGainMapImage:pipGainMapImage:primarySDRImage:pipSDRImage:compositeSDRImage:pipFrame:pipCornerRadius:pipBorderWidth:pipBorderColor:mirrorPIP:captureOrientation:]
+ -[CAMMultiCamPIPCompositor _compositePrimaryImage:pipImage:pipFrame:pipCornerRadius:pipBorderWidth:pipBorderColor:mirrorPIP:captureOrientation:motionBlurAngle:motionBlurRadius:debugColorDuplicatedPrimaryImage:debugColorDuplicatedPIPImage:]
+ -[CAMMultiCamPIPCompositor _cropPIP:toSizeAspectRatioIfNecessary:]
+ -[CAMMultiCamPIPCompositor _debugColorDuplicatedMovieFileBuffers]
+ -[CAMMultiCamPIPCompositor _debugDisableMotionBlur]
+ -[CAMMultiCamPIPCompositor _debugImageWithDuplicatedColorTint:]
+ -[CAMMultiCamPIPCompositor _debugLastCompositedMovieFilePrimaryBufferPTS]
+ -[CAMMultiCamPIPCompositor _debugLastCompositedMovieFileSecondaryBufferPTS]
+ -[CAMMultiCamPIPCompositor _excessiveBlurRadiusReported]
+ -[CAMMultiCamPIPCompositor _gainMapCIContext]
+ -[CAMMultiCamPIPCompositor _isCompositingSessionActive]
+ -[CAMMultiCamPIPCompositor _lastCompositedPictureInPictureFrameForMotionBlur]
+ -[CAMMultiCamPIPCompositor _metalDevice]
+ -[CAMMultiCamPIPCompositor _mostRecentlyAddedPIPMetricsTimestamp]
+ -[CAMMultiCamPIPCompositor _motionBlurDisabledForCurrentCompositingSession]
+ -[CAMMultiCamPIPCompositor _pipFrameEqualsMostRecentlyAdded:]
+ -[CAMMultiCamPIPCompositor _pipMaxBlurRadius]
+ -[CAMMultiCamPIPCompositor _pipMetricsByTimestamp]
+ -[CAMMultiCamPIPCompositor _pipMetricsForCompositingClosestToTimestamp:]
+ -[CAMMultiCamPIPCompositor _pipMetricsForCompositingClosestToTimestamp:].cold.1
+ -[CAMMultiCamPIPCompositor _pipMetricsMaxCapacity]
+ -[CAMMultiCamPIPCompositor _pipRotationAngle]
+ -[CAMMultiCamPIPCompositor _pipTimestampTooOldReported]
+ -[CAMMultiCamPIPCompositor _scaledPIPMetrics:toPrimaryImageSize:]
+ -[CAMMultiCamPIPCompositor _sortedPIPTimestamps]
+ -[CAMMultiCamPIPCompositor _surfaceMemoryPool]
+ -[CAMMultiCamPIPCompositor _textureCache]
+ -[CAMMultiCamPIPCompositor _useCoreImageCVTextureCache]
+ -[CAMMultiCamPIPCompositor _useCoreImageSurfacePool]
+ -[CAMMultiCamPIPCompositor compositeWithCompositingData:strategy:captureOrientation:mirrorPIP:]
+ -[CAMMultiCamPIPCompositor initWithPictureInPictureRotationAngle:]
+ -[CAMMultiCamPIPCompositor isMotionBlurDisabled]
+ -[CAMMultiCamPIPCompositor prepareForCompositing]
+ -[CAMMultiCamPIPCompositor resetCompositingState:]
+ -[CAMMultiCamPIPCompositor setMotionBlurDisabled:]
+ -[CAMMultiCamPIPCompositor setPictureInPictureMetrics:]
+ -[CAMMultiCamPIPCompositor set_ciContext:]
+ -[CAMMultiCamPIPCompositor set_commandQueue:]
+ -[CAMMultiCamPIPCompositor set_compositingSessionActive:]
+ -[CAMMultiCamPIPCompositor set_debugLastCompositedMovieFilePrimaryBufferPTS:]
+ -[CAMMultiCamPIPCompositor set_debugLastCompositedMovieFileSecondaryBufferPTS:]
+ -[CAMMultiCamPIPCompositor set_excessiveBlurRadiusReported:]
+ -[CAMMultiCamPIPCompositor set_gainMapCIContext:]
+ -[CAMMultiCamPIPCompositor set_lastCompositedPictureInPictureFrameForMotionBlur:]
+ -[CAMMultiCamPIPCompositor set_metalDevice:]
+ -[CAMMultiCamPIPCompositor set_mostRecentlyAddedPIPMetricsTimestamp:]
+ -[CAMMultiCamPIPCompositor set_motionBlurDisabledForCurrentCompositingSession:]
+ -[CAMMultiCamPIPCompositor set_pipRotationAngle:]
+ -[CAMMultiCamPIPCompositor set_pipTimestampTooOldReported:]
+ -[CAMMultiCamPIPCompositor set_surfaceMemoryPool:]
+ -[CAMMultiCamPIPCompositor set_textureCache:]
+ -[CAMMultiCamPIPMetrics borderColor]
+ -[CAMMultiCamPIPMetrics borderWidth]
+ -[CAMMultiCamPIPMetrics cornerRadius]
+ -[CAMMultiCamPIPMetrics frameInCoreImageLandscapeCoordinateSpace]
+ -[CAMMultiCamPIPMetrics frame]
+ -[CAMMultiCamPIPMetrics initWithTimestamp:frame:cornerRadius:borderWidth:borderColor:videoResolution:]
+ -[CAMMultiCamPIPMetrics timeStampInSeconds]
+ -[CAMMultiCamPIPMetrics timestamp]
+ -[CAMMultiCamPIPMetrics videoResolution]
+ -[CAMMutableStillImageCaptureRequest setFrontRearSimultaneousCaptureEnabled:]
+ -[CAMMutableStillImageCaptureRequest setFrontRearSimultaneousCaptureMirrored:]
+ -[CAMMutableVideoCaptureRequest setFrontRearSimultaneousVideoEnabled:]
+ -[CAMMutableVideoCaptureRequest setFrontRearSimultaneousVideoMirrored:]
+ -[CAMPreviewView _compareCGPointsToAccuracy:point1:point2:]
+ -[CAMPreviewView _isFrontPIPAtAnAnchor]
+ -[CAMPreviewView _pipAnchorPointForPIPSize:]
+ -[CAMPreviewView frontPIPAnchor]
+ -[CAMPreviewView frontPIPVideoPreviewLayer]
+ -[CAMPreviewView frontPIPVideoPreviewView]
+ -[CAMPreviewView setFrontPIPAnchor:]
+ -[CAMPreviewView setFrontPIPVideoPreviewLayer:]
+ -[CAMPreviewView viewportAnchorsForFrontPIPOriginWithSize:]
+ -[CAMPreviewView viewportAnchorsForFrontPIP]
+ -[CAMPreviewViewController _animateFrontPIPToCenter:animationUpdateMode:resetFocusAndExposure:]
+ -[CAMPreviewViewController _createFrontPIPVideoPreviewViewPanGestureRecognizerIfNecessary]
+ -[CAMPreviewViewController _frontPIPVideoPreviewAnimationSpringSettings]
+ -[CAMPreviewViewController _frontPIPVideoPreviewCenterAnimatableProperty]
+ -[CAMPreviewViewController _frontPIPVideoPreviewCenterAnimationResetsFocusAndExposure]
+ -[CAMPreviewViewController _frontPIPVideoPreviewPanGestureRecognizer]
+ -[CAMPreviewViewController _frontPIPVideoPreviewRenderedCornerRadius]
+ -[CAMPreviewViewController _handleFrontPIPVideoPreviewViewPan:]
+ -[CAMPreviewViewController _handleFrontPIPVideoPreviewViewPanDidEndAtPosition:withVelocity:inView:timestamp:]
+ -[CAMPreviewViewController _handleFrontPIPVideoPreviewViewPanDidMoveWithTranslation:withGesture:inView:timestamp:]
+ -[CAMPreviewViewController _hideFrontPIPVideoPreviewView]
+ -[CAMPreviewViewController _previewDidStartRunning:]
+ -[CAMPreviewViewController _resetFocusAndExposureIfFrontPIPObscuresIndicator]
+ -[CAMPreviewViewController _updateCaptureControllerWithFrontPIPFrameRelativeToViewport:cornerRadius:timestamp:]
+ -[CAMPreviewViewController set_frontPIPVideoPreviewCenterAnimatableProperty:]
+ -[CAMPreviewViewController set_frontPIPVideoPreviewCenterAnimationResetsFocusAndExposure:]
+ -[CAMPreviewViewController set_frontPIPVideoPreviewRenderedCornerRadius:]
+ -[CAMPreviewViewController viewDidLayoutSubviews]
+ -[CAMResetVideoMinFrameDurationOverrideCommand _resetSecondaryDevice]
+ -[CAMResetVideoMinFrameDurationOverrideCommand initForSecondaryDevice]
+ -[CAMStillImageCaptureRequest isFrontRearSimultaneousCaptureEnabled]
+ -[CAMStillImageCaptureRequest isFrontRearSimultaneousCaptureMirrored]
+ -[CAMSubjectAreaChangeMonitoringCommand _configureSecondaryDevice]
+ -[CAMSubjectAreaChangeMonitoringCommand initWithSubjectAreaChangeMonitoringEnabled:configureSecondaryDevice:]
+ -[CAMSystemPressureState shouldDisablePIPMotionBlur]
+ -[CAMTextBadge updateForSmartFramingAutoFramingDidZoom:didRotate:]
+ -[CAMTextBadge updateForSmartFramingAutoRotation:]
+ -[CAMTextBadge updateForSmartFramingAutoZoom:]
+ -[CAMTextBadge updateForSmartFramingDisabled]
+ -[CAMUserPreferences _preserveFrontRearSimultaneousVideoEnabled]
+ -[CAMUserPreferences alwaysShowFrontPIPIndicator]
+ -[CAMUserPreferences didRecentlyUseFrontPIP]
+ -[CAMUserPreferences setDidRecentlyUseFrontPIP:]
+ -[CAMUserPreferences setDidRecentlyUseFrontPIP]
+ -[CAMUserPreferences setShouldEnableFrontRearSimultaneousVideo:]
+ -[CAMUserPreferences setWantsSmartFramingAutoRotationDefault:]
+ -[CAMUserPreferences setWantsSmartFramingAutoZoomDefault:]
+ -[CAMUserPreferences shouldEnableFrontRearSimultaneousVideo]
+ -[CAMUserPreferences wantsSmartFramingAutoRotationDefault]
+ -[CAMUserPreferences wantsSmartFramingAutoZoomDefault]
+ -[CAMVideoCaptureRequest isFrontRearSimultaneousVideoEnabled]
+ -[CAMVideoCaptureRequest isFrontRearSimultaneousVideoMirrored]
+ -[CAMVideoFramerateCommand _configureSecondaryDevice]
+ -[CAMVideoFramerateCommand initWithVideoConfiguration:configureSecondaryDevice:]
+ -[CAMVideoStabilizationCommand _configureSecondaryDevice]
+ -[CAMVideoStabilizationCommand _frontRearSimultaneousVideoEnabled]
+ -[CAMVideoStabilizationCommand initWithAutomaticVideoStabilizationEnabled:strength:frontRearSimultaneousVideoEnabled:configureSecondaryDevice:]
+ -[CAMViewfinderViewController _autoSmartFramingSupportedSmartFramingFieldOfViewsForGraphConfiguration:]
+ -[CAMViewfinderViewController _calculateVerticalOffsetFromZoomPlatterToFrame:fromView:]
+ -[CAMViewfinderViewController _defaultSmartFramingFieldOfViewForOrientation:]
+ -[CAMViewfinderViewController _delaySmartFramingDynamicAspectRatioUpdate]
+ -[CAMViewfinderViewController _desiredFieldOfView]
+ -[CAMViewfinderViewController _disableAutoSmartFramingIfSupported]
+ -[CAMViewfinderViewController _handleFlipAspectRatioButtonTapped:]
+ -[CAMViewfinderViewController _handleFrontPIPButtonTapped:]
+ -[CAMViewfinderViewController _isFrontRearSimultaneousVideoActiveForMode:devicePosition:]
+ -[CAMViewfinderViewController _isFrontRearSimultaneousVideoEnabled]
+ -[CAMViewfinderViewController _isFrontRearSimultaneousVideoSupportedForMode:devicePosition:]
+ -[CAMViewfinderViewController _overrideSmartFramingAutoRotateInLandscapeEnabled]
+ -[CAMViewfinderViewController _overrideSmartFramingAutoZoomInLandscapeEnabled]
+ -[CAMViewfinderViewController _performGraphConfigurationChangeForFrontRearSimultaneousVideoEnabledChange]
+ -[CAMViewfinderViewController _resetDynamicAspectRatio]
+ -[CAMViewfinderViewController _resetSmartFramingFieldOfViewAnimated:]
+ -[CAMViewfinderViewController _resolvedFlipAspectRatioForMode:videoConfiguration:devicePosition:trueVideoEnabled:]
+ -[CAMViewfinderViewController _resolvedSmartFramingAutoRotationEnabled]
+ -[CAMViewfinderViewController _resolvedSmartFramingAutoZoomEnabled]
+ -[CAMViewfinderViewController _resolvedSmartFramingFieldOfViewForMode:devicePosition:]
+ -[CAMViewfinderViewController _resolvedSmartFramingFieldOfViewForMode:devicePosition:].cold.1
+ -[CAMViewfinderViewController _setFrontRearSimultaneousVideoEnabled:]
+ -[CAMViewfinderViewController _setOverrideSmartFramingAutoRotateInLandscapeEnabled:]
+ -[CAMViewfinderViewController _setOverrideSmartFramingAutoZoomInLandscapeEnabled:]
+ -[CAMViewfinderViewController _setSmartFramingAutoRotationEnabled:]
+ -[CAMViewfinderViewController _setSmartFramingAutoZoomEnabled:]
+ -[CAMViewfinderViewController _setWantsSmartFramingAutoRotationDefault:]
+ -[CAMViewfinderViewController _setWantsSmartFramingAutoZoomDefault:]
+ -[CAMViewfinderViewController _shouldShowFlipAspectRatioButtonForGraphConfiguration:]
+ -[CAMViewfinderViewController _shouldShowFrontPIPButtonForGraphConfiguration:]
+ -[CAMViewfinderViewController _shouldShowSmartFramingAutoRotationForGraphConfiguration:]
+ -[CAMViewfinderViewController _shouldShowSmartFramingAutoZoomForGraphConfiguration:]
+ -[CAMViewfinderViewController _showSmartFramingAutoBadgeForSmartFramingFieldOfView:previousSmartFramingFieldOfView:]
+ -[CAMViewfinderViewController _smartFramingAutoRotationEnabled]
+ -[CAMViewfinderViewController _smartFramingAutoRotationMonitoringEnabled]
+ -[CAMViewfinderViewController _smartFramingAutoZoomEnabled]
+ -[CAMViewfinderViewController _smartFramingFieldOfViewSource]
+ -[CAMViewfinderViewController _smartFramingSupportsAspectRatioCrop:]
+ -[CAMViewfinderViewController _toggleZoomForSmartFramingFieldOfView:]
+ -[CAMViewfinderViewController _updateFlipAspectRatioButtonForGraphConfiguration:animated:]
+ -[CAMViewfinderViewController _updateFrontPIPButtonActiveState]
+ -[CAMViewfinderViewController _updateFrontRearSimultaneousVideoEnabled:]
+ -[CAMViewfinderViewController _updateFrontRearSimultaneousVideoEnabledForGraphConfiguration:]
+ -[CAMViewfinderViewController _updateSmartFramingDynamicAspectRatioAndZoomWithRampDuration:zoomRampTuning:]
+ -[CAMViewfinderViewController _updateSmartFramingFieldOfViewForGraphConfiguration:animated:]
+ -[CAMViewfinderViewController _updateSmartFramingFieldOfViewForGraphConfiguration:rampDuration:zoomRampTuning:animated:]
+ -[CAMViewfinderViewController _updateSmartFramingForCaptureOrientation:rampDuration:zoomRampTuning:animated:]
+ -[CAMViewfinderViewController _updateSmartFramingMonitorForGraphConfiguration:]
+ -[CAMViewfinderViewController _updateSmartFramingOverCaptureGradientHeightForGraphConfiguration:animated:]
+ -[CAMViewfinderViewController _wantsFlipAspectRatio]
+ -[CAMViewfinderViewController _wantsSmartFramingAutoRotationDefault]
+ -[CAMViewfinderViewController _wantsSmartFramingAutoZoomDefault]
+ -[CAMViewfinderViewController _zoomButtonPlatterOffsetAnimator]
+ -[CAMViewfinderViewController captureController:didOutputRecommendedSmartFramingFieldOfView:]
+ -[CAMViewfinderViewController frontPIPFrameDidChange:]
+ -[CAMViewfinderViewController frontPIPWillAnimateToPosition:withFrame:]
+ -[CAMViewfinderViewController fullScreenViewfinderDidCreateFlipAspectRatioButton:]
+ -[CAMViewfinderViewController fullScreenViewfinderDidCreateFrontPIPButton:]
+ -[CAMViewfinderViewController handleUserChangedFlippedAspectRatioEnabled:]
+ -[CAMViewfinderViewController handleUserChangedFrontPIPEnabled:]
+ -[CAMViewfinderViewController handleUserChangedSmartFramingAutoRotationEnabled:]
+ -[CAMViewfinderViewController handleUserChangedSmartFramingAutoZoomEnabled:]
+ -[CAMViewfinderViewController set_delaySmartFramingDynamicAspectRatioUpdate:]
+ -[CAMViewfinderViewController set_desiredFieldOfView:]
+ -[CAMViewfinderViewController set_smartFramingFieldOfViewSource:]
+ -[CAMViewfinderViewController set_wantsFlipAspectRatio:]
+ -[CAMViewfinderViewController set_zoomButtonPlatterOffsetAnimator:]
+ -[CAMWhiteBalanceCommand _configureSecondaryDevice]
+ -[CAMWhiteBalanceCommand initWithWhiteBalanceMode:configureSecondaryDevice:]
+ -[CAMZoomButtonPlatter contentType]
+ -[CAMZoomButtonPlatter setContentType:]
+ -[CAMZoomButtonPlatter setContentType:animated:]
+ -[CAMZoomButtonPlatter setZoomSymbols:]
+ -[CAMZoomButtonPlatter setZoomSymbols:animated:]
+ -[CAMZoomButtonPlatter zoomSymbols]
+ -[CUCaptureController _commandForResetFocus:resetExposure:resetExposureTargetBias:resetSecondaryDevice:]
+ -[CUCaptureController _recommendedSmartFramingChangedForKeyPath:ofObject:change:]
+ -[CUCaptureController _setupRecommendedSmartFramingMonitoring]
+ -[CUCaptureController _teardownRecommendedSmartFramingMonitoring]
+ -[CUCaptureController changeToSmartFramingFieldOfView:mode:videoConfiguration:devicePosition:]
+ -[CUCaptureController recommendedSmartFramingDelegate]
+ -[CUCaptureController secondaryVideoPreviewLayer]
+ -[CUCaptureController setAutoSmartFramingEnabledFieldOfViews:]
+ -[CUCaptureController setMultiCamPictureInPictureMetrics:]
+ -[CUCaptureController setRecommendedSmartFramingDelegate:]
+ -[CUCaptureController setSmartFramingMonitorEnabled:]
+ GCC_except_table100
+ GCC_except_table1215
+ GCC_except_table1224
+ GCC_except_table1230
+ GCC_except_table124
+ GCC_except_table1264
+ GCC_except_table1341
+ GCC_except_table1347
+ GCC_except_table1353
+ GCC_except_table138
+ GCC_except_table1472
+ GCC_except_table151
+ GCC_except_table180
+ GCC_except_table183
+ GCC_except_table184
+ GCC_except_table217
+ GCC_except_table244
+ GCC_except_table256
+ GCC_except_table263
+ GCC_except_table267
+ GCC_except_table272
+ GCC_except_table289
+ GCC_except_table302
+ GCC_except_table308
+ GCC_except_table320
+ GCC_except_table322
+ GCC_except_table324
+ GCC_except_table326
+ GCC_except_table330
+ GCC_except_table615
+ GCC_except_table617
+ GCC_except_table680
+ GCC_except_table845
+ GCC_except_table85
+ GCC_except_table865
+ GCC_except_table91
+ GCC_except_table918
+ GCC_except_table920
+ GCC_except_table922
+ OBJC_IVAR_$_CAMStillImageCaptureRequest._frontRearSimultaneousCaptureEnabled
+ OBJC_IVAR_$_CAMStillImageCaptureRequest._frontRearSimultaneousCaptureMirrored
+ OBJC_IVAR_$_CAMVideoCaptureRequest._frontRearSimultaneousVideoEnabled
+ OBJC_IVAR_$_CAMVideoCaptureRequest._frontRearSimultaneousVideoMirrored
+ _AVCaptureAspectRatio3x4
+ _AVCaptureAspectRatio4x3
+ _AVCaptureDynamicAspectRatio16x9
+ _AVCaptureDynamicAspectRatio9x16
+ _AVCaptureMultiCamClientCompositingMetadataCompositionPictureInPictureRectKey
+ _AVCaptureMultiCamClientCompositingMetadataCoreImageGainMapPropertiesKey
+ _AVCaptureSmartFramingFieldOfViewLandscape
+ _AVCaptureSmartFramingFieldOfViewNone
+ _AVCaptureSmartFramingFieldOfViewPortrait
+ _AVCaptureSmartFramingFieldOfViewZoomedOutLandscape
+ _AVCaptureSmartFramingFieldOfViewZoomedOutPortrait
+ _AVCaptureSystemPressureLevelCritical
+ _AVCaptureSystemPressureLevelSerious
+ _AVGQ4UHSO4KRGIJFZHZ3EAGDMAK6CA
+ _AVGQ5RTE3RTRZZFRGK7IDFEQC7NFBE
+ _AVGQ6HD7ZNZD33DG7SG4DOHIPW4SUQ
+ _AVGQAJT7KNQJHRRDW5Q5QTGETOLK2E
+ _AVGQHDDMQ6RTH76PQ2HVCQ4MSWG63Q
+ _AVGQHSSMVIQNR3MAPIGELAQM7DWP4U
+ _AVGQQIBUFDUYMZTKVBF36FTLQON3DY
+ _AVGQT42HZJM7T4BHFEGWILGWIJSNEQ
+ _AVGQYPHR3FTUAZCCTEYFPSINLTE7DI
+ _AVSmartStyleCastTypeBrightPop
+ _BSFloatApproximatelyEqualToFloat
+ _BSFloatEqualToFloat
+ _BSPointEqualToPoint
+ _BSRectRoundForScale
+ _BSSizeEqualToSize
+ _CAMRecommendedSmartFramingContext
+ _CAMUserPreferenceAlwaysShowFrontPIPIndicator
+ _CAMUserPreferenceAlwaysShowFrontPIPIndicatorDefaultValue
+ _CAMUserPreferenceBottomOverCaptureGradientEnabled
+ _CAMUserPreferenceEnableFrontRearSimultaneousVideo
+ _CAMUserPreferencePreserveFrontRearSimultaneousVideoEnabled
+ _CAMUserPreferenceTopOverCaptureGradientEnabled
+ _CAMUserPreferencesWantsSmartFramingAutoRotationDefault
+ _CAMUserPreferencesWantsSmartFramingAutoZoomDefault
+ _CAMVideoFramerateCommandConfigureSecondaryDevice
+ _CAMVideoStabilizationCommandConfigureSecondaryDevice
+ _CAMVideoStabilizationCommandFrontRearSimultaneousVideoEnabled
+ _CEKDeviceRegionPrefersSmartStyleUT6
+ _CMSampleBufferGetPresentationTimeStamp
+ _CVMetalTextureCacheCreate
+ _CVMetalTextureCacheFlush
+ _MGGetProductType
+ _OBJC_CLASS_$_AVCaptureMultiCamSession
+ _OBJC_CLASS_$_AVCaptureSmartFraming
+ _OBJC_CLASS_$_CAMAutoSmartFramingEnabledFieldOfViewsCommand
+ _OBJC_CLASS_$_CAMAutoSmartFramingMonitorCommand
+ _OBJC_CLASS_$_CAMDynamicAspectRatioCommand
+ _OBJC_CLASS_$_CAMFlipAspectRatioButton
+ _OBJC_CLASS_$_CAMFrontPIPButton
+ _OBJC_CLASS_$_CAMFrontRearSimultaneousCaptureCommand
+ _OBJC_CLASS_$_CAMFrontRearSimultaneousVideoRecordingCommand
+ _OBJC_CLASS_$_CAMMultiCamPIPCompositor
+ _OBJC_CLASS_$_CAMMultiCamPIPMetrics
+ _OBJC_CLASS_$_CAMPIPVideoPreviewView
+ _OBJC_CLASS_$_CIBlendKernel
+ _OBJC_CLASS_$_CIColor
+ _OBJC_CLASS_$_CIRenderDestination
+ _OBJC_CLASS_$_IOSurfaceMemoryPool
+ _OBJC_IVAR_$_CAMAutoFPSVideoCommand.__configureSecondaryDevice
+ _OBJC_IVAR_$_CAMAutoSmartFramingEnabledFieldOfViewsCommand.__smartFramingEnabledFieldsOfView
+ _OBJC_IVAR_$_CAMAutoSmartFramingMonitorCommand.__enabled
+ _OBJC_IVAR_$_CAMCaptureCapabilities.__HDR10BitVideoSupports240FPS
+ _OBJC_IVAR_$_CAMCaptureCapabilities.__dynamicAspectRatioInCinematicModeSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities.__dynamicAspectRatioInVideoModeSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._autoSmartFramingSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._backQuadraTeleFocalLengthDisplayValue
+ _OBJC_IVAR_$_CAMCaptureCapabilities._backQuadraTeleSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._dynamicAspectRatioSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._frontRearSimultaneousVideo60FPSSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._frontRearSimultaneousVideoDeferredFrontCameraEnabled
+ _OBJC_IVAR_$_CAMCaptureCapabilities._frontRearSimultaneousVideoFrontCameraHDR10Supported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._frontRearSimultaneousVideoFrontVideoStabilizationSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._frontRearSimultaneousVideoSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._quadraTeleDisplayZoomFactor
+ _OBJC_IVAR_$_CAMCaptureCapabilities._quadraTeleRelativeZoomFactor
+ _OBJC_IVAR_$_CAMCaptureCapabilities._smartFramingFieldOfViewLandscapeZoomFactor
+ _OBJC_IVAR_$_CAMCaptureCapabilities._smartFramingFieldOfViewPortraitZoomFactor
+ _OBJC_IVAR_$_CAMCaptureCapabilities._smartFramingFieldOfViewZoomedOutLandscapeZoomFactor
+ _OBJC_IVAR_$_CAMCaptureCapabilities._smartFramingFieldOfViewZoomedOutPortraitZoomFactor
+ _OBJC_IVAR_$_CAMCaptureCapabilities._smartFramingSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._smartFramingUsingDynamicAspectRatioSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._useMultiCamSession
+ _OBJC_IVAR_$_CAMCaptureCommandContext._currentSecondaryVideoDevice
+ _OBJC_IVAR_$_CAMCaptureCommandContext._currentSecondaryVideoDeviceFormat
+ _OBJC_IVAR_$_CAMCaptureCommandContext._currentSecondaryVideoDeviceInput
+ _OBJC_IVAR_$_CAMCaptureCommandContext._currentSecondaryVideoPreviewLayer
+ _OBJC_IVAR_$_CAMCaptureEngine.__multiCamPIPCompositingQueue
+ _OBJC_IVAR_$_CAMCaptureEngine.__multiCamPIPCompositingQueue_multiCamPIPCompositor
+ _OBJC_IVAR_$_CAMCaptureEngine.__secondaryVideoPreviewLayer
+ _OBJC_IVAR_$_CAMCaptureEngineDevice.__cachedDynamicAspectRatioFormat
+ _OBJC_IVAR_$_CAMCaptureGraphConfiguration._frontRearSimultaneousVideoEnabled
+ _OBJC_IVAR_$_CAMCaptureGraphConfiguration._smartFramingFieldOfView
+ _OBJC_IVAR_$_CAMCaptureGraphConfiguration._videoDynamicAspectRatio
+ _OBJC_IVAR_$_CAMControlStatusBar._autoFramingIndicator
+ _OBJC_IVAR_$_CAMDynamicAspectRatioCommand.__configureForSecondaryDevice
+ _OBJC_IVAR_$_CAMDynamicAspectRatioCommand.__devicePosition
+ _OBJC_IVAR_$_CAMDynamicAspectRatioCommand.__mode
+ _OBJC_IVAR_$_CAMDynamicAspectRatioCommand.__smartFramingFieldOfView
+ _OBJC_IVAR_$_CAMDynamicAspectRatioCommand.__videoConfiguration
+ _OBJC_IVAR_$_CAMDynamicAspectRatioCommand.__videoDynamicAspectRatio
+ _OBJC_IVAR_$_CAMExposureCommand.__configureSecondaryDevice
+ _OBJC_IVAR_$_CAMExposureTargetBiasCommand.__configureSecondaryDevice
+ _OBJC_IVAR_$_CAMFlipAspectRatioButton._active
+ _OBJC_IVAR_$_CAMFocusCommand.__configureSecondaryDevice
+ _OBJC_IVAR_$_CAMFrontPIPButton._active
+ _OBJC_IVAR_$_CAMFrontRearSimultaneousCaptureCommand.__enabled
+ _OBJC_IVAR_$_CAMFrontRearSimultaneousVideoRecordingCommand.__enabled
+ _OBJC_IVAR_$_CAMFullscreenViewfinder.__useSmartFramingTransition
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._flipAspectRatioButton
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._flipAspectRatioButtonVisible
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._frontPIPButton
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._frontPIPButtonVisible
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._offsetZoomButtonForFlipAspectRatioButton
+ _OBJC_IVAR_$_CAMFullscreenViewfinder._smartFramingFieldOfView
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__ciContext
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__commandQueue
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__compositingSessionActive
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__debugColorDuplicatedMovieFileBuffers
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__debugDisableMotionBlur
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__debugLastCompositedMovieFilePrimaryBufferPTS
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__debugLastCompositedMovieFileSecondaryBufferPTS
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__excessiveBlurRadiusReported
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__gainMapCIContext
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__lastCompositedPictureInPictureFrameForMotionBlur
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__metalDevice
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__mostRecentlyAddedPIPMetricsTimestamp
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__motionBlurDisabledForCurrentCompositingSession
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__pipMaxBlurRadius
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__pipMetricsByTimestamp
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__pipMetricsMaxCapacity
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__pipRotationAngle
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__pipTimestampTooOldReported
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__surfaceMemoryPool
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__textureCache
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__useCoreImageCVTextureCache
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor.__useCoreImageSurfacePool
+ _OBJC_IVAR_$_CAMMultiCamPIPCompositor._motionBlurDisabled
+ _OBJC_IVAR_$_CAMMultiCamPIPMetrics._borderColor
+ _OBJC_IVAR_$_CAMMultiCamPIPMetrics._borderWidth
+ _OBJC_IVAR_$_CAMMultiCamPIPMetrics._cornerRadius
+ _OBJC_IVAR_$_CAMMultiCamPIPMetrics._frame
+ _OBJC_IVAR_$_CAMMultiCamPIPMetrics._timestamp
+ _OBJC_IVAR_$_CAMMultiCamPIPMetrics._videoResolution
+ _OBJC_IVAR_$_CAMPreviewView._frontPIPAnchor
+ _OBJC_IVAR_$_CAMPreviewView._frontPIPVideoPreviewView
+ _OBJC_IVAR_$_CAMPreviewViewController.__frontPIPVideoPreviewAnimationSpringSettings
+ _OBJC_IVAR_$_CAMPreviewViewController.__frontPIPVideoPreviewCenterAnimatableProperty
+ _OBJC_IVAR_$_CAMPreviewViewController.__frontPIPVideoPreviewCenterAnimationResetsFocusAndExposure
+ _OBJC_IVAR_$_CAMPreviewViewController.__frontPIPVideoPreviewPanGestureRecognizer
+ _OBJC_IVAR_$_CAMPreviewViewController.__frontPIPVideoPreviewRenderedCornerRadius
+ _OBJC_IVAR_$_CAMResetVideoMinFrameDurationOverrideCommand.__resetSecondaryDevice
+ _OBJC_IVAR_$_CAMSubjectAreaChangeMonitoringCommand.__configureSecondaryDevice
+ _OBJC_IVAR_$_CAMUserPreferences.__preserveFrontRearSimultaneousVideoEnabled
+ _OBJC_IVAR_$_CAMUserPreferences._alwaysShowFrontPIPIndicator
+ _OBJC_IVAR_$_CAMUserPreferences._didRecentlyUseFrontPIP
+ _OBJC_IVAR_$_CAMUserPreferences._shouldEnableFrontRearSimultaneousVideo
+ _OBJC_IVAR_$_CAMUserPreferences._wantsSmartFramingAutoRotationDefault
+ _OBJC_IVAR_$_CAMUserPreferences._wantsSmartFramingAutoZoomDefault
+ _OBJC_IVAR_$_CAMVideoFramerateCommand.__configureSecondaryDevice
+ _OBJC_IVAR_$_CAMVideoStabilizationCommand.__configureSecondaryDevice
+ _OBJC_IVAR_$_CAMVideoStabilizationCommand.__frontRearSimultaneousVideoEnabled
+ _OBJC_IVAR_$_CAMViewfinderViewController.__delaySmartFramingDynamicAspectRatioUpdate
+ _OBJC_IVAR_$_CAMViewfinderViewController.__desiredFieldOfView
+ _OBJC_IVAR_$_CAMViewfinderViewController.__frontRearSimultaneousVideoEnabled
+ _OBJC_IVAR_$_CAMViewfinderViewController.__overrideSmartFramingAutoRotateInLandscapeEnabled
+ _OBJC_IVAR_$_CAMViewfinderViewController.__overrideSmartFramingAutoZoomInLandscapeEnabled
+ _OBJC_IVAR_$_CAMViewfinderViewController.__smartFramingAutoRotationEnabled
+ _OBJC_IVAR_$_CAMViewfinderViewController.__smartFramingAutoZoomEnabled
+ _OBJC_IVAR_$_CAMViewfinderViewController.__smartFramingFieldOfViewSource
+ _OBJC_IVAR_$_CAMViewfinderViewController.__wantsFlipAspectRatio
+ _OBJC_IVAR_$_CAMViewfinderViewController.__wantsSmartFramingAutoRotationDefault
+ _OBJC_IVAR_$_CAMViewfinderViewController.__wantsSmartFramingAutoZoomDefault
+ _OBJC_IVAR_$_CAMViewfinderViewController.__zoomButtonPlatterOffsetAnimator
+ _OBJC_IVAR_$_CAMWhiteBalanceCommand.__configureSecondaryDevice
+ _OBJC_IVAR_$_CAMZoomButtonPlatter._contentType
+ _OBJC_IVAR_$_CAMZoomButtonPlatter._zoomSymbols
+ _OBJC_IVAR_$_CUCaptureController._recommendedSmartFramingDelegate
+ _OBJC_METACLASS_$_CAMAutoSmartFramingEnabledFieldOfViewsCommand
+ _OBJC_METACLASS_$_CAMAutoSmartFramingMonitorCommand
+ _OBJC_METACLASS_$_CAMDynamicAspectRatioCommand
+ _OBJC_METACLASS_$_CAMFlipAspectRatioButton
+ _OBJC_METACLASS_$_CAMFrontPIPButton
+ _OBJC_METACLASS_$_CAMFrontRearSimultaneousCaptureCommand
+ _OBJC_METACLASS_$_CAMFrontRearSimultaneousVideoRecordingCommand
+ _OBJC_METACLASS_$_CAMMultiCamPIPCompositor
+ _OBJC_METACLASS_$_CAMMultiCamPIPMetrics
+ _OBJC_METACLASS_$_CAMPIPVideoPreviewView
+ _PISemanticStyleCastBrightPop
+ __OBJC_$_CLASS_METHODS_CAMPIPVideoPreviewView
+ __OBJC_$_INSTANCE_METHODS_CAMAutoSmartFramingEnabledFieldOfViewsCommand
+ __OBJC_$_INSTANCE_METHODS_CAMAutoSmartFramingMonitorCommand
+ __OBJC_$_INSTANCE_METHODS_CAMDynamicAspectRatioCommand
+ __OBJC_$_INSTANCE_METHODS_CAMFlipAspectRatioButton
+ __OBJC_$_INSTANCE_METHODS_CAMFrontPIPButton
+ __OBJC_$_INSTANCE_METHODS_CAMFrontRearSimultaneousCaptureCommand
+ __OBJC_$_INSTANCE_METHODS_CAMFrontRearSimultaneousVideoRecordingCommand
+ __OBJC_$_INSTANCE_METHODS_CAMMultiCamPIPCompositor
+ __OBJC_$_INSTANCE_METHODS_CAMMultiCamPIPMetrics
+ __OBJC_$_INSTANCE_VARIABLES_CAMAutoSmartFramingEnabledFieldOfViewsCommand
+ __OBJC_$_INSTANCE_VARIABLES_CAMAutoSmartFramingMonitorCommand
+ __OBJC_$_INSTANCE_VARIABLES_CAMDynamicAspectRatioCommand
+ __OBJC_$_INSTANCE_VARIABLES_CAMFlipAspectRatioButton
+ __OBJC_$_INSTANCE_VARIABLES_CAMFrontPIPButton
+ __OBJC_$_INSTANCE_VARIABLES_CAMFrontRearSimultaneousCaptureCommand
+ __OBJC_$_INSTANCE_VARIABLES_CAMFrontRearSimultaneousVideoRecordingCommand
+ __OBJC_$_INSTANCE_VARIABLES_CAMMultiCamPIPCompositor
+ __OBJC_$_INSTANCE_VARIABLES_CAMMultiCamPIPMetrics
+ __OBJC_$_INSTANCE_VARIABLES_CAMResetVideoMinFrameDurationOverrideCommand
+ __OBJC_$_PROP_LIST_CAMAutoSmartFramingEnabledFieldOfViewsCommand
+ __OBJC_$_PROP_LIST_CAMAutoSmartFramingMonitorCommand
+ __OBJC_$_PROP_LIST_CAMDynamicAspectRatioCommand
+ __OBJC_$_PROP_LIST_CAMFlipAspectRatioButton
+ __OBJC_$_PROP_LIST_CAMFrontPIPButton
+ __OBJC_$_PROP_LIST_CAMFrontRearSimultaneousCaptureCommand
+ __OBJC_$_PROP_LIST_CAMFrontRearSimultaneousVideoRecordingCommand
+ __OBJC_$_PROP_LIST_CAMMultiCamPIPCompositor
+ __OBJC_$_PROP_LIST_CAMMultiCamPIPMetrics
+ __OBJC_$_PROP_LIST_CAMResetVideoMinFrameDurationOverrideCommand
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAMRecommendedSmartFramingDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAMRecommendedSmartFramingDelegate
+ __OBJC_$_PROTOCOL_REFS_CAMRecommendedSmartFramingDelegate
+ __OBJC_CLASS_RO_$_CAMAutoSmartFramingEnabledFieldOfViewsCommand
+ __OBJC_CLASS_RO_$_CAMAutoSmartFramingMonitorCommand
+ __OBJC_CLASS_RO_$_CAMDynamicAspectRatioCommand
+ __OBJC_CLASS_RO_$_CAMFlipAspectRatioButton
+ __OBJC_CLASS_RO_$_CAMFrontPIPButton
+ __OBJC_CLASS_RO_$_CAMFrontRearSimultaneousCaptureCommand
+ __OBJC_CLASS_RO_$_CAMFrontRearSimultaneousVideoRecordingCommand
+ __OBJC_CLASS_RO_$_CAMMultiCamPIPCompositor
+ __OBJC_CLASS_RO_$_CAMMultiCamPIPMetrics
+ __OBJC_CLASS_RO_$_CAMPIPVideoPreviewView
+ __OBJC_LABEL_PROTOCOL_$_CAMRecommendedSmartFramingDelegate
+ __OBJC_METACLASS_RO_$_CAMAutoSmartFramingEnabledFieldOfViewsCommand
+ __OBJC_METACLASS_RO_$_CAMAutoSmartFramingMonitorCommand
+ __OBJC_METACLASS_RO_$_CAMDynamicAspectRatioCommand
+ __OBJC_METACLASS_RO_$_CAMFlipAspectRatioButton
+ __OBJC_METACLASS_RO_$_CAMFrontPIPButton
+ __OBJC_METACLASS_RO_$_CAMFrontRearSimultaneousCaptureCommand
+ __OBJC_METACLASS_RO_$_CAMFrontRearSimultaneousVideoRecordingCommand
+ __OBJC_METACLASS_RO_$_CAMMultiCamPIPCompositor
+ __OBJC_METACLASS_RO_$_CAMMultiCamPIPMetrics
+ __OBJC_METACLASS_RO_$_CAMPIPVideoPreviewView
+ __OBJC_PROTOCOL_$_CAMRecommendedSmartFramingDelegate
+ ___101-[CAMCaptureEngineDevice _deviceFormatForDynamicAspectRatioWithGraphConfiguration:deviceIsSecondary:]_block_invoke
+ ___103-[CAMViewfinderViewController _requestPasscodeUnlockForCameraRollController:forAction:completionBlock:]_block_invoke.1393
+ ___111-[CAMAutoSmartFramingEnabledFieldOfViewsCommand _smartFramingForSmartFramingFieldOfView:supportedFieldOfViews:]_block_invoke
+ ___132-[CAMCaptureEngine _captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:forVideoCaptureRequest:videoZoomFactor:error:]_block_invoke.331
+ ___132-[CAMCaptureEngine _captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:forVideoCaptureRequest:videoZoomFactor:error:]_block_invoke_2.332
+ ___138-[CAMFullscreenViewfinder _layoutViewportWithFrame:previewFrame:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:]_block_invoke
+ ___140-[CAMUserPreferences readPreferencesWithOverrides:emulationMode:callActive:shouldResetCaptureConfiguration:bypassXPCWhenReadingSystemStyle:]_block_invoke.631
+ ___167-[AVCaptureDevice(CAMCaptureEngine) cam_frontFacingFormatForVideoConfiguration:videoEncodingBehavior:colorSpace:dynamicAspectRatio:useSquareFormat:requireVideoBinned:]_block_invoke
+ ___178+[CAMZoomControlUtilities exifFocalLengthsByZoomFactorForMode:device:videoConfiguration:videoStabilizationStrength:customLensGroup:isTrueVideo:frontRearSimultaneousVideoEnabled:]_block_invoke
+ ___33-[CAMCaptureEngine stopRecording]_block_invoke.319
+ ___35-[CAMCaptureEngine enqueueCommand:]_block_invoke.224
+ ___39-[CAMCaptureEngine stopWithCompletion:]_block_invoke.112
+ ___47-[CAMCaptureEngine _handleSessionInterruption:]_block_invoke.148
+ ___47-[CAMCaptureEngine _handleSessionInterruption:]_block_invoke.149
+ ___52-[CAMPreviewViewController _previewDidStartRunning:]_block_invoke
+ ___55-[CAMCaptureEngine setMultiCamPictureInPictureMetrics:]_block_invoke
+ ___57-[CAMPreviewViewController _hideFrontPIPVideoPreviewView]_block_invoke
+ ___58-[CAMCaptureEngine _secondaryVideoDeviceInputFromSession:]_block_invoke
+ ___60-[AVCaptureSession(CAMCaptureEngine) cam_ensureConnections:]_block_invoke
+ ___60-[AVCaptureSession(CAMCaptureEngine) cam_ensureConnections:]_block_invoke_2
+ ___60-[AVCaptureSession(CAMCaptureEngine) cam_ensureConnections:]_block_invoke_2.cold.1
+ ___63-[CAMCaptureEngine _captureEngineDeviceForDeviceType:position:]_block_invoke.451
+ ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke.160
+ ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke_2.161
+ ___66-[CAMCaptureEngine setMultiCamPictureInPictureMotionBlurDisabled:]_block_invoke
+ ___70-[CAMCaptureEngine captureOutput:willBeginCaptureForResolvedSettings:]_block_invoke.258
+ ___71-[CAMViewfinderViewController frontPIPWillAnimateToPosition:withFrame:]_block_invoke
+ ___71-[CAMViewfinderViewController frontPIPWillAnimateToPosition:withFrame:]_block_invoke_2
+ ___71-[CAMViewfinderViewController frontPIPWillAnimateToPosition:withFrame:]_block_invoke_3
+ ___72-[CAMCaptureEngine _commitSessionConfigurationIfNecessaryWithLogReason:]_block_invoke.221
+ ___72-[CAMViewfinderViewController _createPhysicalCaptureInteractionIfNeeded]_block_invoke.1129
+ ___75-[CUCaptureController stillImageRequest:didCompleteVideoCaptureWithResult:]_block_invoke.278
+ ___81-[CUCaptureController _recommendedSmartFramingChangedForKeyPath:ofObject:change:]_block_invoke
+ ___85-[CAMCaptureEngine captureOutput:didPauseRecordingToOutputFileAtURL:fromConnections:]_block_invoke
+ ___85-[CAMCaptureEngine captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:]_block_invoke.323
+ ___85-[CAMCaptureEngine captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:]_block_invoke_3
+ ___92-[CAMCaptureEngine captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:]_block_invoke.421
+ ___92-[CAMViewfinderViewController _requestPasscodeUnlockForDocumentScanningWithCompletionBlock:]_block_invoke.1397
+ ___94-[CAMCaptureEngine captureOutput:readyForClientCompositingForOutputFileAtURL:compositingData:]_block_invoke
+ ___95-[CAMCaptureEngine captureOutput:readyForClientCompositingForResolvedSettings:compositingData:]_block_invoke
+ ___95-[CAMCaptureEngine captureOutput:readyForClientCompositingForResolvedSettings:compositingData:]_block_invoke_2
+ ___95-[CAMPreviewViewController _animateFrontPIPToCenter:animationUpdateMode:resetFocusAndExposure:]_block_invoke
+ ___95-[CAMPreviewViewController _animateFrontPIPToCenter:animationUpdateMode:resetFocusAndExposure:]_block_invoke_2
+ ___95-[CAMPreviewViewController _animateFrontPIPToCenter:animationUpdateMode:resetFocusAndExposure:]_block_invoke_3
+ ___97-[AVCaptureSession(CAMCaptureEngine) cam_ensureVideoPreviewLayers:withConnections:whileRemoving:]_block_invoke
+ ___97-[AVCaptureSession(CAMCaptureEngine) cam_ensureVideoPreviewLayers:withConnections:whileRemoving:]_block_invoke_2
+ ___97-[AVCaptureSession(CAMCaptureEngine) cam_ensureVideoPreviewLayers:withConnections:whileRemoving:]_block_invoke_3
+ ___block_descriptor_32_e43_v32?0"AVCaptureVideoPreviewLayer"8Q16^B24l
+ ___block_descriptor_41_e8_32s_e43_v32?0"AVCaptureVideoPreviewLayer"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32r40r_e31_v32?0"AVCaptureInput"8Q16^B24lr32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e36_v32?0"AVCaptureConnection"8Q16^B24lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e36_v32?0"AVCaptureConnection"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e43_v32?0"AVCaptureVideoPreviewLayer"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e9_v16?0^d8l
+ ___block_descriptor_56_e8_32s40r_e38_v32?0"AVCaptureSmartFraming"8Q16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48w_e40_B16?0"UIViewVectorAnimatableProperty"8lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e39_B16?0"UIViewFloatAnimatableProperty"8ls32l8s40l8s48l8
+ ___block_descriptor_67_e8_32r_e38_v32?0"AVCaptureDeviceFormat"8Q16^B24lr32l8
+ ___block_descriptor_74_e8_32s40s_e41_"AVCaptureDeviceFormat"16?0"NSString"8ls32l8s40l8
+ ___block_literal_global.101
+ ___block_literal_global.106
+ ___block_literal_global.115
+ ___block_literal_global.118
+ ___block_literal_global.119
+ ___block_literal_global.1224
+ ___block_literal_global.1381
+ ___block_literal_global.1392
+ ___block_literal_global.1396
+ ___block_literal_global.154
+ ___block_literal_global.319
+ ___block_literal_global.326
+ ___block_literal_global.334
+ ___block_literal_global.44
+ ___block_literal_global.454
+ ___block_literal_global.48
+ ___block_literal_global.497
+ ___block_literal_global.52
+ ___block_literal_global.57
+ ___block_literal_global.64
+ ___block_literal_global.675
+ ___block_literal_global.677
+ ___block_literal_global.682
+ ___block_literal_global.684
+ _associated conformance 8CameraUI13ChromeElementO18FrontPIPCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLOs9CodingKeyAAs23CustomStringConvertible
+ _associated conformance 8CameraUI13ChromeElementO18FrontPIPCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLOs9CodingKeyAAs28CustomDebugStringConvertible
+ _associated conformance 8CameraUI13ChromeElementO30SmartFramingAutoZoomCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 8CameraUI13ChromeElementO30SmartFramingAutoZoomCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLOs0I3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 8CameraUI13ChromeElementO34SmartFramingAutoRotationCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLOs0I3KeyAAs23CustomStringConvertible
+ _associated conformance 8CameraUI13ChromeElementO34SmartFramingAutoRotationCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLOs0I3KeyAAs28CustomDebugStringConvertible
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyACyACyAA6VStackVyAA9TupleViewVyACyAA6HStackVyAGyAA4TextV_AA6SpacerVtGGAA14_PaddingLayoutVGSg_ACyACyAA4GridVyAA7ForEachVySaySi6offset_06CameraB013ChromeElementO7elementtGSiAWySaySiAX_AY0R4MenuVA0_tGSiACyAY06TopBarU0V0vwU3Row33_922393C89093045A7FB9387957ECEEF9LLVAA21_TraitWritingModifierVyAA18TransitionTraitKeyVGGGSgGGAA010_FlexFrameL0VGAQGACyAA0G0PAAE8trackingyQr12CoreGraphics7CGFloatVFQOyACyACyAkQGAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGG_Qo_AA24_ForegroundStyleModifierVyAA5ColorVGGSgtGGAQGAQGA21_GAY06RotateN26ControlOrientationModifierVGAAA24_HPA50_AAA24_HPA49_AAA24_HPA48_AAA24_HPA47_AAA24_HPyHC_AqA0G8ModifierHPyHCHC_AqAA54_HPyHCHC_A21_AAA54_HPyHCHC_A52_AAA54_HPyHCHC.43
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyACyACyAA6ZStackVyAA9TupleViewVyACyAEyAGyAA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQOyAA012_ConditionalD0VyACyACyACy06CameraB009ChromePadG0VAA30_SafeAreaRegionsIgnoringLayoutVGAA010_FlexFrameW0VGAA16_OverlayModifierVyACyACyACyACyAA06_ShapeG0VyAA9RectangleVAA5ColorVGAA01_yW0VGAT17DebugMenuModifierVGAXGAA23_GeometryActionModifierVySo6CGRectVA20_SQ12CoreGraphicsyHCg_GGSgGGACyAT0qG7DefaultVAA19_BackgroundModifierVyACyACyACyA12_AA01_D13ShapeModifierVyA6_GGA14_GAXGSgGGG_AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQOyAT0p10UISettingsG0V_AT0qG5ModelCQo_Qo__ACyACyACyACyACyACyACyACyA9_A2_yASyACyACyACyACyA8_A2_yA4_yAA13_StrokedShapeVyA6_6_InsetVGA8_GGGAA25_AllowsHitTestingModifierVGA11_GAA09_PositionW0VGAA05EmptyG0VGGGA69_GA69_GA69_GA69_GA69_GA69_GA69_GSgtGGAXG_AT03TopsT12HeightReaderVtGGAA30_EnvironmentKeyWritingModifierVyAA9NamespaceV2IDVSgGGA87_yAT0Q15ScenePhaseModelCSgGGA87_ySo6CGSizeVGGA87_yA21_7CGFloatVGGAaHHPA103_AaHHPA99_AaHHPA94_AaHHPA85_AaHHPyHC_A93_AA0G8ModifierHPyHCHC_A98_AAA108_HPyHCHC_A102_AAA108_HPyHCHC_A106_AAA108_HPyHCHC.85
+ _get_witness_table 7SwiftUI4ViewPAAE19simultaneousGesture_9includingQrqd___AA0E4MaskVtAA0E0Rd__lFQOyAA01_C16Modifier_ContentVy06CameraB009DebugMenuH0VG_AA06_EndedE0VyAA03TapE0VGQo_SgAaBHpqd0__AaBHD3_ATHO_HC.87
+ _get_witness_table 7SwiftUI7GridRowVyAA9TupleViewVyAA0F0PAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQOyAgAE11buttonStyleyQrqd__AA015PrimitiveButtonN0Rd__lFQOyAA15ModifiedContentVyAA0P0VyAA6HStackVyAEyAOy06CameraB006ChromeH4IconOAA30_EnvironmentKeyWritingModifierVyAA5ImageV5ScaleOGGSg_AOyAgAE8trackingyQr12CoreGraphics7CGFloatVFQOyAOyAgAE17hyphenationFactoryQrA7_FQOyAA4TextV_Qo_AXySiSgGG_Qo_AA16_FixedSizeLayoutVGAA6SpacerVtGGGAA12_FrameLayoutVG_AA05PlainpN0VQo__Qo__AA7ForEachVySaySi6offset_AT0U10MenuOptionV7elementtGSiAOyAOyAOyAgAE0g10ShowsLargeR6VieweryQrqd__yXEAaFRd__lFQOyAgAEALyQrqd__AaMRd__lFQOyAQyAOyAOyASyAEyAOyAOyAOyAOyAZA25_GAA14_PaddingLayoutVGAT0t10ForegroundnZ0VGAA14_OpacityEffectVG_AOyAOyAOyAOyAOyAOyA10_A13_GAXyAA0R10TransitionVGGAA010_AnimationZ0VySSGGA44_GAA0j10AttachmentZ0VGA17_GAOyAOyAOyA10_A56_GA44_GA60_GSgA20_tGGA25_GAA16_FlexFrameLayoutVGG_A28_Qo__A10_Qo_AA01_c8CellSizeZ0VGAA01_c9AlignmentZ0VGA60_GGtGGAaFHPyHC.69
+ _get_witness_table 7SwiftUI9TupleViewVyAA4TextV_AA7SectionVy06CameraB018SettingsTitleLabelVSgACyAA6PickerVyAeH0G10UISettingsC21ModeWheelPeekBehaviorOAA7ForEachVySayAQGAqEGG_AA6ToggleVyAEGAA6VStackVyACyAA6HStackVyACyAE_AA6SpacerVAEtGG_AA6SliderVyAeA05EmptyD0VGtGGA12_tGAKGSgAGyAkMyAeH15ChromeImageWellV5ShapeOASySayA19_GA19_AEGGAKGSgAGyAkCyAA15DisclosureGroupVyAeCyAMyAeH20MaterialStylingStateV13MaterialStyleOASySayA30_GA30_AEGG_A6YtGG_AMyAEA28_8GroupingOASySayA37_GA37_AEGGA26_yAeCyAY_A16YA33_tGSgGAYA26_yAeCyAY_AYA12_tGGtGAKGSgAGyAkCyA12__A12_tGAKGSgA51_AGyAKA12_AKGSgAGyAkA14NavigationLinkVyAeA15ModifiedContentVyA57_yAH05BuddyD0VAA16_FlexFrameLayoutVGAA23_SafeAreaIgnoringLayoutVGGAKGSgAGyAkCyAY_AYtGAKGSgSgAGyAkyKGSgAA0D0PAAE15fullScreenCover11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAAA75_Rd__lFQOyAGyAkA6ButtonVyA1_yACyAA0Z0V_AEtGGGAKGSg_AH12MeasureNotchVQo_SgAGyAKA86_yAEGAKGSgtGAAA75_HPyHC.578
+ _hypotf
+ _kCIContextCVMetalTextureCache
+ _kCIContextCacheIntermediates
+ _kCIContextIOSurfaceMemoryPoolID
+ _kCIContextOutputColorSpace
+ _kCIContextPriorityRequestHigh
+ _kCIContextWorkingColorSpace
+ _kCVMetalTextureCacheMaximumTextureAgeKey
+ _kIOSurfaceAllocSize
+ _kIOSurfaceMemoryPoolSize
+ _kIOSurfaceMemoryPoolZeroFillEnabled
+ _keypath_get.447Tm
+ _keypath_get.482Tm
+ _keypath_get.608Tm
+ _keypath_get.632Tm
+ _keypath_get.830Tm
+ _keypath_set.110Tm
+ _keypath_set.12Tm
+ _keypath_set.29Tm
+ _keypath_set.394Tm
+ _keypath_set.553Tm
+ _objc_msgSend$AVCaptureDynamicAspectRatioForCAMDynamicAspectRatio:
+ _objc_msgSend$AVCaptureSmartFramingFieldOfViewForCAMCaptureSmartFramingFieldOfView:
+ _objc_msgSend$CAMCaptureSmartFramingFieldOfViewForAVCaptureSmartFraming:
+ _objc_msgSend$CMVideoDimensionsForCAMPhotoResolution:wantsSquareDimensions:
+ _objc_msgSend$_HDR10BitVideoSupports240FPS
+ _objc_msgSend$_animateFrontPIPToCenter:animationUpdateMode:resetFocusAndExposure:
+ _objc_msgSend$_applyMaskAndBorderToImage:cornerRadius:borderWidth:borderColor:
+ _objc_msgSend$_autoSmartFramingSupportedSmartFramingFieldOfViewsForGraphConfiguration:
+ _objc_msgSend$_cachedDynamicAspectRatioFormat
+ _objc_msgSend$_calculateMotionBlurAngle:motionBlurRadius:forPictureInPictureFrame:fromPictureInPictureFrame:
+ _objc_msgSend$_calculateVerticalOffsetFromZoomPlatterToFrame:fromView:
+ _objc_msgSend$_captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:resolvedDevice:
+ _objc_msgSend$_ciContext
+ _objc_msgSend$_commandForResetFocus:resetExposure:resetExposureTargetBias:resetSecondaryDevice:
+ _objc_msgSend$_compareCGPointsToAccuracy:point1:point2:
+ _objc_msgSend$_compositePrimaryGainMapImage:pipGainMapImage:primarySDRImage:pipSDRImage:compositeSDRImage:pipFrame:pipCornerRadius:pipBorderWidth:pipBorderColor:mirrorPIP:captureOrientation:
+ _objc_msgSend$_compositePrimaryImage:pipImage:pipFrame:pipCornerRadius:pipBorderWidth:pipBorderColor:mirrorPIP:captureOrientation:motionBlurAngle:motionBlurRadius:debugColorDuplicatedPrimaryImage:debugColorDuplicatedPIPImage:
+ _objc_msgSend$_configureForSecondaryDevice
+ _objc_msgSend$_configureSecondaryDevice
+ _objc_msgSend$_createFrontPIPVideoPreviewViewPanGestureRecognizerIfNecessary
+ _objc_msgSend$_cropPIP:toSizeAspectRatioIfNecessary:
+ _objc_msgSend$_debugColorDuplicatedMovieFileBuffers
+ _objc_msgSend$_debugDisableMotionBlur
+ _objc_msgSend$_debugImageWithDuplicatedColorTint:
+ _objc_msgSend$_debugLastCompositedMovieFilePrimaryBufferPTS
+ _objc_msgSend$_debugLastCompositedMovieFileSecondaryBufferPTS
+ _objc_msgSend$_defaultSmartFramingFieldOfViewForOrientation:
+ _objc_msgSend$_delaySmartFramingDynamicAspectRatioUpdate
+ _objc_msgSend$_desiredConnectionWithCaptureEngineSecondaryDevice:secondaryVideoPreviewLayer:
+ _objc_msgSend$_desiredFieldOfView
+ _objc_msgSend$_desiredSecondaryInputsWithCaptureEngineSecondaryDevice:
+ _objc_msgSend$_deviceFormatForDynamicAspectRatioWithGraphConfiguration:deviceIsSecondary:
+ _objc_msgSend$_disableAutoSmartFramingIfSupported
+ _objc_msgSend$_dynamicAspectRatio
+ _objc_msgSend$_dynamicAspectRatioInCinematicModeSupported
+ _objc_msgSend$_dynamicAspectRatioInVideoModeSupported
+ _objc_msgSend$_enabledSmartFramingsFromSupportedFieldOfViews:
+ _objc_msgSend$_excessiveBlurRadiusReported
+ _objc_msgSend$_executeForCurrentDeviceWithContext:
+ _objc_msgSend$_executeForSecondaryDeviceWithContext:
+ _objc_msgSend$_existingVideoPreviewLayersWithContext:without:
+ _objc_msgSend$_fallbackVideoConfigurationForUnsupportedConfiguration:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$_frontPIPButtonFrame
+ _objc_msgSend$_frontPIPVideoPreviewAnimationSpringSettings
+ _objc_msgSend$_frontPIPVideoPreviewCenterAnimatableProperty
+ _objc_msgSend$_frontPIPVideoPreviewCenterAnimationResetsFocusAndExposure
+ _objc_msgSend$_frontPIPVideoPreviewRenderedCornerRadius
+ _objc_msgSend$_frontRearSimultaneousVideoEnabled
+ _objc_msgSend$_gainMapCIContext
+ _objc_msgSend$_handleFrontPIPVideoPreviewViewPanDidEndAtPosition:withVelocity:inView:timestamp:
+ _objc_msgSend$_handleFrontPIPVideoPreviewViewPanDidMoveWithTranslation:withGesture:inView:timestamp:
+ _objc_msgSend$_hideFrontPIPVideoPreviewView
+ _objc_msgSend$_isCompositingSessionActive
+ _objc_msgSend$_isFrontPIPAtAnAnchor
+ _objc_msgSend$_isFrontRearSimultaneousVideoActiveForMode:devicePosition:
+ _objc_msgSend$_isFrontRearSimultaneousVideoEnabled
+ _objc_msgSend$_isFrontRearSimultaneousVideoSupportedForMode:devicePosition:
+ _objc_msgSend$_isSmartFramingFieldOfView:equalToAVCaptureSmartFraming:
+ _objc_msgSend$_lastCompositedPictureInPictureFrameForMotionBlur
+ _objc_msgSend$_layoutViewportWithFrame:previewFrame:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:
+ _objc_msgSend$_mostRecentlyAddedPIPMetricsTimestamp
+ _objc_msgSend$_motionBlurDisabledForCurrentCompositingSession
+ _objc_msgSend$_multiCamPIPCompositingQueue
+ _objc_msgSend$_multiCamPIPCompositingQueue_multiCamPIPCompositor
+ _objc_msgSend$_overrideSmartFramingAutoRotateInLandscapeEnabled
+ _objc_msgSend$_overrideSmartFramingAutoZoomInLandscapeEnabled
+ _objc_msgSend$_performGraphConfigurationChangeForFrontRearSimultaneousVideoEnabledChange
+ _objc_msgSend$_pipAnchorPointForPIPSize:
+ _objc_msgSend$_pipFrameEqualsMostRecentlyAdded:
+ _objc_msgSend$_pipMaxBlurRadius
+ _objc_msgSend$_pipMetricsByTimestamp
+ _objc_msgSend$_pipMetricsForCompositingClosestToTimestamp:
+ _objc_msgSend$_pipMetricsMaxCapacity
+ _objc_msgSend$_pipRotationAngle
+ _objc_msgSend$_pipTimestampTooOldReported
+ _objc_msgSend$_recommendedSmartFramingChangedForKeyPath:ofObject:change:
+ _objc_msgSend$_resetDynamicAspectRatio
+ _objc_msgSend$_resetFocusAndExposureIfFrontPIPObscuresIndicator
+ _objc_msgSend$_resetSecondaryDevice
+ _objc_msgSend$_resetSmartFramingFieldOfViewAnimated:
+ _objc_msgSend$_resolvedFlipAspectRatioForMode:videoConfiguration:devicePosition:trueVideoEnabled:
+ _objc_msgSend$_resolvedSmartFramingAutoRotationEnabled
+ _objc_msgSend$_resolvedSmartFramingAutoZoomEnabled
+ _objc_msgSend$_resolvedSmartFramingFieldOfViewForMode:devicePosition:
+ _objc_msgSend$_scaledPIPMetrics:toPrimaryImageSize:
+ _objc_msgSend$_secondaryEngineDeviceWithContext:graphConfiguration:resolvedDevice:
+ _objc_msgSend$_secondaryInputsBecomingPrimaryWithContext:desiredPrimaryInputs:
+ _objc_msgSend$_secondaryVideoDeviceInputFromSession:
+ _objc_msgSend$_setFlipAspectRatioButton:
+ _objc_msgSend$_setFrontPIPButton:
+ _objc_msgSend$_setFrontRearSimultaneousVideoEnabled:
+ _objc_msgSend$_setOverrideSmartFramingAutoRotateInLandscapeEnabled:
+ _objc_msgSend$_setOverrideSmartFramingAutoZoomInLandscapeEnabled:
+ _objc_msgSend$_setSmartFramingAutoRotationEnabled:
+ _objc_msgSend$_setSmartFramingAutoZoomEnabled:
+ _objc_msgSend$_setWantsSmartFramingAutoRotationDefault:
+ _objc_msgSend$_setWantsSmartFramingAutoZoomDefault:
+ _objc_msgSend$_setupRecommendedSmartFramingMonitoring
+ _objc_msgSend$_shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$_shouldShowFlipAspectRatioButtonForGraphConfiguration:
+ _objc_msgSend$_shouldShowFrontPIPButtonForGraphConfiguration:
+ _objc_msgSend$_shouldShowSmartFramingAutoRotationForGraphConfiguration:
+ _objc_msgSend$_shouldShowSmartFramingAutoZoomForGraphConfiguration:
+ _objc_msgSend$_showSmartFramingAutoBadgeForSmartFramingFieldOfView:previousSmartFramingFieldOfView:
+ _objc_msgSend$_smartFramingAutoRotationEnabled
+ _objc_msgSend$_smartFramingAutoRotationMonitoringEnabled
+ _objc_msgSend$_smartFramingAutoZoomEnabled
+ _objc_msgSend$_smartFramingEnabledFieldsOfView
+ _objc_msgSend$_smartFramingFieldOfView
+ _objc_msgSend$_smartFramingFieldOfViewSource
+ _objc_msgSend$_smartFramingForSmartFramingFieldOfView:supportedFieldOfViews:
+ _objc_msgSend$_smartFramingSupportsAspectRatioCrop:
+ _objc_msgSend$_sortedPIPTimestamps
+ _objc_msgSend$_specificFramerateCommandForGraphConfiguration:withContext:configureSecondaryDevice:
+ _objc_msgSend$_surfaceMemoryPool
+ _objc_msgSend$_teardownRecommendedSmartFramingMonitoring
+ _objc_msgSend$_textureCache
+ _objc_msgSend$_toggleZoomForSmartFramingFieldOfView:
+ _objc_msgSend$_updateCaptureControllerWithFrontPIPFrameRelativeToViewport:cornerRadius:timestamp:
+ _objc_msgSend$_updateFlipAspectRatioButtonForGraphConfiguration:animated:
+ _objc_msgSend$_updateFrontPIPButtonActiveState
+ _objc_msgSend$_updateFrontRearSimultaneousVideoEnabled:
+ _objc_msgSend$_updateFrontRearSimultaneousVideoEnabledForGraphConfiguration:
+ _objc_msgSend$_updatePreviewLayerForPreviewFrame:viewportFrame:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:
+ _objc_msgSend$_updateSmartFramingDynamicAspectRatioAndZoomWithRampDuration:zoomRampTuning:
+ _objc_msgSend$_updateSmartFramingFieldOfViewForGraphConfiguration:animated:
+ _objc_msgSend$_updateSmartFramingFieldOfViewForGraphConfiguration:rampDuration:zoomRampTuning:animated:
+ _objc_msgSend$_updateSmartFramingForCaptureOrientation:rampDuration:zoomRampTuning:animated:
+ _objc_msgSend$_updateSmartFramingMonitorForGraphConfiguration:
+ _objc_msgSend$_updateSmartFramingOverCaptureGradientHeightForGraphConfiguration:animated:
+ _objc_msgSend$_useCoreImageCVTextureCache
+ _objc_msgSend$_useCoreImageSurfacePool
+ _objc_msgSend$_useSmartFramingTransition
+ _objc_msgSend$_videoDynamicAspectRatio
+ _objc_msgSend$_wantsFlipAspectRatio
+ _objc_msgSend$_wantsSmartFramingAutoRotationDefault
+ _objc_msgSend$_wantsSmartFramingAutoZoomDefault
+ _objc_msgSend$_zoomButtonPlatterOffsetAnimator
+ _objc_msgSend$alwaysShowFrontPIPIndicator
+ _objc_msgSend$applyWithForeground:background:
+ _objc_msgSend$backQuadraTeleFocalLengthDisplayValue
+ _objc_msgSend$borderColor
+ _objc_msgSend$borderWidth
+ _objc_msgSend$bottomOverCaptureGradientEnabled
+ _objc_msgSend$bundleURL
+ _objc_msgSend$cam_addConnectionWithMediaType:fromDeviceInput:toOutput:
+ _objc_msgSend$cam_connectionWithMediaType:fromDeviceInput:toOutput:
+ _objc_msgSend$cam_ensureConnections:
+ _objc_msgSend$cam_ensureVideoPreviewLayers:withConnections:whileRemoving:
+ _objc_msgSend$cam_frontFacingFormatForVideoConfiguration:videoEncodingBehavior:colorSpace:dynamicAspectRatio:useSquareFormat:requireVideoBinned:
+ _objc_msgSend$cam_supportsFrontFacingFormatForVideoConfiguration:colorSpace:enableProResVideo:dynamicAspectRatio:useSquareFormat:requireVideoBinned:
+ _objc_msgSend$captureController:didOutputRecommendedSmartFramingFieldOfView:
+ _objc_msgSend$captureOutput:readyForClientCompositingForOutputFileAtURL:compositingData:
+ _objc_msgSend$changeToSmartFramingFieldOfView:mode:videoConfiguration:devicePosition:
+ _objc_msgSend$colorMonochromeFilter
+ _objc_msgSend$colorWithRed:green:blue:colorSpace:
+ _objc_msgSend$compositeWithCompositingData:strategy:captureOrientation:mirrorPIP:
+ _objc_msgSend$contextWithMTLDevice:options:
+ _objc_msgSend$cornerRadiusForContainerWidth:
+ _objc_msgSend$currentSecondaryVideoDevice
+ _objc_msgSend$currentSecondaryVideoDeviceFormat
+ _objc_msgSend$currentSecondaryVideoDeviceInput
+ _objc_msgSend$currentSecondaryVideoPreviewLayer
+ _objc_msgSend$currentTraitCollection
+ _objc_msgSend$defaultAnchor
+ _objc_msgSend$defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:isTrueVideo:frontRearSimultaneousVideoEnabled:prefersHDR10BitVideo:smartFramingFieldOfView:overrodeWithForcedZoomValue:
+ _objc_msgSend$deviceFormatForSessionPreset:device:
+ _objc_msgSend$didRecentlyUseFrontPIP
+ _objc_msgSend$dynamicAspectRatioSupported
+ _objc_msgSend$ensureMemory:
+ _objc_msgSend$exifFocalLengthsByZoomFactorForMode:device:videoConfiguration:videoStabilizationStrength:customLensGroup:isTrueVideo:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:macroMode:
+ _objc_msgSend$flipAspectRatioButton
+ _objc_msgSend$floatAnimatablePropertyWithInitialValue:cancelableFrameCallback:
+ _objc_msgSend$flush:
+ _objc_msgSend$frameInCoreImageLandscapeCoordinateSpace
+ _objc_msgSend$frontPIPAnchor
+ _objc_msgSend$frontPIPButton
+ _objc_msgSend$frontPIPButtonVisible
+ _objc_msgSend$frontPIPFrameDidChange:
+ _objc_msgSend$frontPIPVideoPreviewLayer
+ _objc_msgSend$frontPIPVideoPreviewView
+ _objc_msgSend$frontPIPWillAnimateToPosition:withFrame:
+ _objc_msgSend$frontRearSimultaneousVideoEnabled
+ _objc_msgSend$fullScreenViewfinderDidCreateFlipAspectRatioButton:
+ _objc_msgSend$fullScreenViewfinderDidCreateFrontPIPButton:
+ _objc_msgSend$futureThrowTime
+ _objc_msgSend$gainMapImageForSDR:HDR:colorSpace:rgbGainmap:
+ _objc_msgSend$handleUserChangedFlippedAspectRatioEnabled:
+ _objc_msgSend$imageByApplyingCGOrientation:
+ _objc_msgSend$imageByApplyingGainMap:
+ _objc_msgSend$imageByApplyingTransform:highQualityDownsample:
+ _objc_msgSend$imageByCompositingOverImage:
+ _objc_msgSend$imageByCroppingToRect:
+ _objc_msgSend$initForSecondaryDevice
+ _objc_msgSend$initWithAutoFPSVideoEnabled:configureSecondaryDevice:
+ _objc_msgSend$initWithAutomaticVideoStabilizationEnabled:strength:frontRearSimultaneousVideoEnabled:configureSecondaryDevice:
+ _objc_msgSend$initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:mixAudioWithOthers:windNoiseRemovalEnabled:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:smartStyles:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:videoBinned:enableDepthSuggestion:enableZoomPIP:customLensGroup:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:videoDynamicAspectRatio:smartFramingFieldOfView:
+ _objc_msgSend$initWithExposureMode:atPointOfInterest:configureSecondaryDevice:
+ _objc_msgSend$initWithExposureTargetBias:configureSecondaryDevice:
+ _objc_msgSend$initWithFocusMode:atPointOfInterest:rectSize:smooth:configureSecondaryDevice:
+ _objc_msgSend$initWithFrontRearSimultaneousCaptureEnabled:
+ _objc_msgSend$initWithPictureInPictureRotationAngle:
+ _objc_msgSend$initWithPixelBuffer:
+ _objc_msgSend$initWithProperties:
+ _objc_msgSend$initWithSmartFramingEnabledFieldOfViews:
+ _objc_msgSend$initWithSmartFramingFieldOfView:videoDynamicAspectRatio:mode:videoConfiguration:devicePosition:
+ _objc_msgSend$initWithSmartFramingFieldOfView:videoDynamicAspectRatio:mode:videoConfiguration:devicePosition:configureForSecondaryDevice:
+ _objc_msgSend$initWithSmartFramingMonitorEnabled:
+ _objc_msgSend$initWithSubjectAreaChangeMonitoringEnabled:configureSecondaryDevice:
+ _objc_msgSend$initWithTimestamp:frame:cornerRadius:borderWidth:borderColor:videoResolution:
+ _objc_msgSend$initWithVideoConfiguration:configureSecondaryDevice:
+ _objc_msgSend$initWithWhiteBalanceMode:configureSecondaryDevice:
+ _objc_msgSend$input
+ _objc_msgSend$isActionModeControlSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$isAutoSmartFramingSupported
+ _objc_msgSend$isBackQuadraTeleSupported
+ _objc_msgSend$isDynamicAspectRatioSupportedForMode:devicePosition:
+ _objc_msgSend$isDynamicAspectRatioSupportedForMode:videoConfiguration:devicePosition:
+ _objc_msgSend$isEnhancedStabilizationSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$isFlipAspectRatioButtonVisible
+ _objc_msgSend$isFrontRearSimultaneousCaptureEnabled
+ _objc_msgSend$isFrontRearSimultaneousCaptureMirrored
+ _objc_msgSend$isFrontRearSimultaneousVideo60FPSSupported
+ _objc_msgSend$isFrontRearSimultaneousVideoDeferredFrontCameraEnabled
+ _objc_msgSend$isFrontRearSimultaneousVideoEnabled
+ _objc_msgSend$isFrontRearSimultaneousVideoFrontCameraHDR10Supported
+ _objc_msgSend$isFrontRearSimultaneousVideoFrontVideoStabilizationSupported
+ _objc_msgSend$isFrontRearSimultaneousVideoMirrored
+ _objc_msgSend$isFrontRearSimultaneousVideoSupported
+ _objc_msgSend$isFrontRearSimultaneousVideoSupportedForMode:
+ _objc_msgSend$isFrontRearSimultaneousVideoSupportedForMode:devicePosition:
+ _objc_msgSend$isFrontRearSimultaneousVideoSupportedForVideoConfiguration:
+ _objc_msgSend$isLensPositionControlSupportedForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$isMonitoring
+ _objc_msgSend$isMotionBlurDisabled
+ _objc_msgSend$isMultiCamClientCompositingSupported
+ _objc_msgSend$isQuadraTeleBinningReconfigurationSupportedForMode:devicePosition:videoConfiguration:
+ _objc_msgSend$isQuadraTeleZoomButtonSupportedForMode:devicePosition:videoConfiguration:
+ _objc_msgSend$isSecondaryDeviceVideoBinned
+ _objc_msgSend$isSmartFramingSupported
+ _objc_msgSend$isSmartFramingSupportedForMode:devicePosition:
+ _objc_msgSend$isSmartFramingUsingDynamicAspectRatioSupported
+ _objc_msgSend$isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$isSupportedVideoConfiguration:forMode:device:trueVideoEnabled:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$isTripleCameraSupportedForMode:devicePosition:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$isVideoStabilizationStrength:supportedForMode:devicePosition:trueVideoEnabled:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$isZoomPIPSupportedForMode:devicePosition:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$loadArchiveWithName:fromURL:
+ _objc_msgSend$motionBlurFilter
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$offsetZoomButtonForFlipAspectRatioButton
+ _objc_msgSend$outputGainMapSampleBuffer
+ _objc_msgSend$outputSampleBuffer
+ _objc_msgSend$pipInsetForViewportSize:
+ _objc_msgSend$pipOutsetForViewportSize:
+ _objc_msgSend$poolId
+ _objc_msgSend$populateZoomFieldOfView:graphConfiguration:smartFramingSource:
+ _objc_msgSend$preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$prepareForCompositing
+ _objc_msgSend$presentationValue
+ _objc_msgSend$primaryGainMapImage
+ _objc_msgSend$primaryImage
+ _objc_msgSend$primarySampleBuffer
+ _objc_msgSend$primaryVideoPreviewLayerForGraphConfiguration:
+ _objc_msgSend$properties
+ _objc_msgSend$quadraTeleDisplayZoomFactor
+ _objc_msgSend$quadraTeleRelativeZoomFactor
+ _objc_msgSend$recommendedSmartFramingDelegate
+ _objc_msgSend$resetCompositingState:
+ _objc_msgSend$resolveDesiredMacroMode:forMode:device:videoConfiguration:videoStabilizationStrength:photoFormat:optionalDepthEffectEnabled:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$roundedRectangleGeneratorFilter
+ _objc_msgSend$roundedRectangleStrokeGeneratorFilter
+ _objc_msgSend$sanitizeVideoConfigurationForDesiredConfiguration:mode:device:trueVideoEnabled:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$secondaryDevice:
+ _objc_msgSend$secondaryDeviceColorSpace
+ _objc_msgSend$secondaryDeviceUsesPrimaryVideoConfigurationForFrameRate
+ _objc_msgSend$secondaryDeviceVideoConfiguration
+ _objc_msgSend$secondaryDeviceVideoDynamicAspectRatio
+ _objc_msgSend$secondaryDeviceVideoStabilizationStrength
+ _objc_msgSend$secondaryGainMapImage
+ _objc_msgSend$secondaryImage
+ _objc_msgSend$secondarySampleBuffer
+ _objc_msgSend$secondaryVideoPreviewLayer
+ _objc_msgSend$secondaryVideoPreviewLayerForGraphConfiguration:
+ _objc_msgSend$setAngle:
+ _objc_msgSend$setAutoSmartFramingEnabledFieldOfViews:
+ _objc_msgSend$setButtonPlatterVerticalOffset:
+ _objc_msgSend$setCompositingMetadata:
+ _objc_msgSend$setCurrentSecondaryVideoDevice:
+ _objc_msgSend$setCurrentSecondaryVideoDeviceFormat:
+ _objc_msgSend$setCurrentSecondaryVideoDeviceInput:
+ _objc_msgSend$setCurrentSecondaryVideoPreviewLayer:
+ _objc_msgSend$setDefaultValues
+ _objc_msgSend$setDidRecentlyUseFrontPIP
+ _objc_msgSend$setDidRecentlyUseFrontPIP:
+ _objc_msgSend$setDynamicAspectRatio:completionHandler:
+ _objc_msgSend$setEnabledSmartFramings:
+ _objc_msgSend$setExtent:
+ _objc_msgSend$setFlipAspectRatioButtonVisible:animated:
+ _objc_msgSend$setFrontPIPAnchor:
+ _objc_msgSend$setFrontPIPButtonVisible:animated:
+ _objc_msgSend$setFrontPIPFrame:
+ _objc_msgSend$setFrontPIPVideoPreviewLayer:
+ _objc_msgSend$setFrontRearSimultaneousCaptureEnabled:
+ _objc_msgSend$setFrontRearSimultaneousCaptureMirrored:
+ _objc_msgSend$setFrontRearSimultaneousVideoEnabled:
+ _objc_msgSend$setFrontRearSimultaneousVideoMirrored:
+ _objc_msgSend$setGradientAscending:
+ _objc_msgSend$setGradientHeight:
+ _objc_msgSend$setInputImage:
+ _objc_msgSend$setIntensity:
+ _objc_msgSend$setIsFrontPIPSupported:
+ _objc_msgSend$setIsSmartFramingAutoRotationSupported:
+ _objc_msgSend$setIsSmartFramingAutoZoomSupported:
+ _objc_msgSend$setMotionBlurDisabled:
+ _objc_msgSend$setMultiCamClientCompositingEnabled:
+ _objc_msgSend$setMultiCamClientCompositingPrimaryConnection:secondaryConnection:
+ _objc_msgSend$setMultiCamPictureInPictureMetrics:
+ _objc_msgSend$setMultiCamPictureInPictureMotionBlurDisabled:
+ _objc_msgSend$setOffsetZoomButtonForFlipAspectRatioButton:animated:
+ _objc_msgSend$setOverrideSmartFramingAutoRotateInLandscapeEnabled:
+ _objc_msgSend$setOverrideSmartFramingAutoZoomInLandscapeEnabled:
+ _objc_msgSend$setPictureInPictureMetrics:
+ _objc_msgSend$setPrimaryCaptureRectAspectRatio:centerPoint:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:
+ _objc_msgSend$setRadius:
+ _objc_msgSend$setRecommendedSmartFramingDelegate:
+ _objc_msgSend$setSession:
+ _objc_msgSend$setSessionWithNoConnection:
+ _objc_msgSend$setShouldEnableFrontRearSimultaneousVideo:
+ _objc_msgSend$setShowFrontPIPIndicator:
+ _objc_msgSend$setSmartFramingAutoRotationEnabled:
+ _objc_msgSend$setSmartFramingAutoZoomEnabled:
+ _objc_msgSend$setSmartFramingFieldOfView:useTransition:animated:
+ _objc_msgSend$setSmartFramingMonitorEnabled:
+ _objc_msgSend$setSmoothness:
+ _objc_msgSend$setTranslation:inView:
+ _objc_msgSend$setWantsSmartFramingAutoRotationDefault:
+ _objc_msgSend$setWantsSmartFramingAutoZoomDefault:
+ _objc_msgSend$setWidth:
+ _objc_msgSend$setZoomSymbols:animated:
+ _objc_msgSend$set_bottomOverCaptureGradientView:
+ _objc_msgSend$set_compositingSessionActive:
+ _objc_msgSend$set_debugLastCompositedMovieFilePrimaryBufferPTS:
+ _objc_msgSend$set_debugLastCompositedMovieFileSecondaryBufferPTS:
+ _objc_msgSend$set_delaySmartFramingDynamicAspectRatioUpdate:
+ _objc_msgSend$set_desiredFieldOfView:
+ _objc_msgSend$set_excessiveBlurRadiusReported:
+ _objc_msgSend$set_frontPIPVideoPreviewCenterAnimatableProperty:
+ _objc_msgSend$set_frontPIPVideoPreviewCenterAnimationResetsFocusAndExposure:
+ _objc_msgSend$set_frontPIPVideoPreviewRenderedCornerRadius:
+ _objc_msgSend$set_lastCompositedPictureInPictureFrameForMotionBlur:
+ _objc_msgSend$set_mostRecentlyAddedPIPMetricsTimestamp:
+ _objc_msgSend$set_motionBlurDisabledForCurrentCompositingSession:
+ _objc_msgSend$set_pipTimestampTooOldReported:
+ _objc_msgSend$set_smartFramingFieldOfViewSource:
+ _objc_msgSend$set_topOverCaptureGradientView:
+ _objc_msgSend$set_useSmartFramingTransition:
+ _objc_msgSend$set_wantsFlipAspectRatio:
+ _objc_msgSend$set_zoomButtonPlatterOffsetAnimator:
+ _objc_msgSend$shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$shouldApplyContinuousZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:zoomFactors:displayZoomFactors:
+ _objc_msgSend$shouldDisablePIPMotionBlur
+ _objc_msgSend$shouldEmulateTripleCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$shouldEmulateWideDualCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$shouldEnableFrontRearSimultaneousVideo
+ _objc_msgSend$sizeForViewportSize:
+ _objc_msgSend$smartFramingFieldOfView
+ _objc_msgSend$smartFramingFieldOfViewLandscapeZoomFactor
+ _objc_msgSend$smartFramingFieldOfViewPortraitZoomFactor
+ _objc_msgSend$smartFramingFieldOfViewZoomedOutLandscapeZoomFactor
+ _objc_msgSend$smartFramingFieldOfViewZoomedOutPortraitZoomFactor
+ _objc_msgSend$smartFramingMonitor
+ _objc_msgSend$smoothness
+ _objc_msgSend$sourceIn
+ _objc_msgSend$startMonitoring:
+ _objc_msgSend$startTaskToRender:toDestination:error:
+ _objc_msgSend$stopMonitoring
+ _objc_msgSend$supportedDynamicAspectRatios
+ _objc_msgSend$supportedSmartFramings
+ _objc_msgSend$timeStampInSeconds
+ _objc_msgSend$topBarItemCornerRadiusForContentSize:
+ _objc_msgSend$topOverCaptureGradientEnabled
+ _objc_msgSend$updateForSmartFramingAutoFramingDidZoom:didRotate:
+ _objc_msgSend$updateForSmartFramingAutoRotation:
+ _objc_msgSend$updateForSmartFramingAutoZoom:
+ _objc_msgSend$updateForSmartFramingDisabled
+ _objc_msgSend$useMultiCamSession
+ _objc_msgSend$useSquareFormatForDynamicAspectRatioForMode:videoConfiguration:
+ _objc_msgSend$vector2DAnimatablePropertyWithInitialValue:cancelableFrameCallback:
+ _objc_msgSend$velocityInView:
+ _objc_msgSend$videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:resolvedDevice:
+ _objc_msgSend$videoDeviceFormatForGraphConfiguration:captureSession:deviceIsSecondary:
+ _objc_msgSend$videoDynamicAspectRatio
+ _objc_msgSend$videoResolution
+ _objc_msgSend$viewportAnchorsForFrontPIP
+ _objc_msgSend$viewportAnchorsForFrontPIPOriginWithSize:
+ _objc_msgSend$wantsSmartFramingAutoRotationDefault
+ _objc_msgSend$wantsSmartFramingAutoZoomDefault
+ _objc_msgSend$zoomControlDisplayValueForZoomFactor:mode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:
+ _objc_msgSend$zoomFactorForSmartFramingFieldOfView:
+ _objc_msgSend$zoomSymbols
+ _objectdestroy.277Tm
+ _objectdestroy.36Tm
+ _objectdestroy.45Tm
+ _symbolic SbIegy_
+ _symbolic _____ 8CameraUI13ChromeElementO18FrontPIPCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLO
+ _symbolic _____ 8CameraUI13ChromeElementO30SmartFramingAutoZoomCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLO
+ _symbolic _____ 8CameraUI13ChromeElementO34SmartFramingAutoRotationCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLO
+ _symbolic ___________y_____Sg_____y_____yAA__________ySayAGGAgAGG______yAAG_____yAEy_____yAEyAA______AAtGG______yAA_____GtGGAWtGADGSgAByAdFyAA_____AHySayA_GA_AAGGADGSgAByAdEy_____yAaEyAFyAA_____AHySayA6_GA6_AAGG_A6MtGG_AFyAA_____AHySayA12_GA12_AAGGA5_yAaEyAM_A16MA9_tGSgGAMA5_yAaEyAM_AmWtGGtGADGSgAByAdEyAW_AWtGADGSgA26_AByAdwDGSgAByAD_____yAA_____yA30_y__________G_____GGADGSgAByAdEyAM_AMtGADGSgSgAByAdmDGSg_____yAByAD_____yAOyAEy______AAtGGGADGSg______Qo_SgAByADA45_yAAGADGSgt 7SwiftUI4TextV AA7SectionV 06CameraB018SettingsTitleLabelV AA9TupleViewV AA6PickerV AF0E10UISettingsC21ModeWheelPeekBehaviorO AA7ForEachV AA6ToggleV AA6VStackV AA6HStackV AA6SpacerV AA6SliderV AA05EmptyJ0V AF15ChromeImageWellV5ShapeO AA15DisclosureGroupV AF20MaterialStylingStateV13MaterialStyleO A10_8GroupingO AA14NavigationLinkV AA15ModifiedContentV AF05BuddyJ0V AA16_FlexFrameLayoutV AA23_SafeAreaIgnoringLayoutV AA0J0PAAE15fullScreenCover11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAAA25_Rd__lFQO AA6ButtonV AA0Z0V AF12MeasureNotchV
+ _symbolic _____yAAyAAyAAyAAyAAyAAyAAy_____y__________G_____y_____yAAyAAyAAyAAyAdFyABy_____y_____GADGGG_____G_____G_____G_____GGGAVGAVGAVGAVGAVGAVGAVGSg 7SwiftUI15ModifiedContentV AA10_ShapeViewV AA9RectangleV AA5ColorV AA16_OverlayModifierV AA012_ConditionalD0V AA08_StrokedE0V AG6_InsetV AA017_AllowsHitTestingJ0V AA12_FrameLayoutV AA09_PositionR0V AA05EmptyF0V
+ _symbolic _____yAAyAAyAAy_____y_____yAAyAByACy_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______tGG_____y_____SgGGA44_y_____SgGGA44_y_____GGA44_y_____GG 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V AT03TopsT12HeightReaderV AA30_EnvironmentKeyWritingModifierV AA9NamespaceV2IDV AT0Q15ScenePhaseModelC So6CGSizeV 12CoreGraphics7CGFloatV
+ _symbolic _____yAAyAAy_____y_____yAAyAByACy_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______tGG_____y_____SgGGA44_y_____SgGGA44_y_____GG 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V AT03TopsT12HeightReaderV AA30_EnvironmentKeyWritingModifierV AA9NamespaceV2IDV AT0Q15ScenePhaseModelC So6CGSizeV
+ _symbolic _____yAAy_____y_____yAAyAByACy_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______tGG_____y_____SgGGA44_y_____SgGG 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V AT03TopsT12HeightReaderV AA30_EnvironmentKeyWritingModifierV AA9NamespaceV2IDV AT0Q15ScenePhaseModelC
+ _symbolic _____y_____G s22KeyedDecodingContainerV 8CameraUI13ChromeElementO18FrontPIPCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 8CameraUI13ChromeElementO30SmartFramingAutoZoomCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 8CameraUI13ChromeElementO34SmartFramingAutoRotationCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 8CameraUI13ChromeElementO18FrontPIPCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 8CameraUI13ChromeElementO30SmartFramingAutoZoomCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 8CameraUI13ChromeElementO34SmartFramingAutoRotationCodingKeys33_103051DF3CEC21DDBD50C278EE765586LLO
+ _symbolic _____y_____G_ACt 7SwiftUI6ToggleV AA4TextV
+ _symbolic _____y_____Sg_____y_____y_____G_AGtGACG 7SwiftUI7SectionV 06CameraB018SettingsTitleLabelV AA9TupleViewV AA6ToggleV AA4TextV
+ _symbolic _____y_____Sg_____y_____y_____G_AGtGACGSg 7SwiftUI7SectionV 06CameraB018SettingsTitleLabelV AA9TupleViewV AA6ToggleV AA4TextV
+ _symbolic _____y_____Sg_____y_____y_____G_AGtGACGSgSg 7SwiftUI7SectionV 06CameraB018SettingsTitleLabelV AA9TupleViewV AA6ToggleV AA4TextV
+ _symbolic _____y___________y_____SgAAy_____yAB__________ySayAGGAgBGG______yABG_____yAAy_____yAAyAB______ABtGG______yAB_____GtGGAWtGAEGSgACyAeFyAB_____AHySayA_GA_ABGGAEGSgACyAeAy_____yAbAyAFyAB_____AHySayA6_GA6_ABGG_A6MtGG_AFyAB_____AHySayA12_GA12_ABGGA5_yAbAyAM_A16MA9_tGSgGAMA5_yAbAyAM_AmWtGGtGAEGSgACyAeAyAW_AWtGAEGSgA26_ACyAewEGSgACyAE_____yAB_____yA30_y__________G_____GGAEGSgACyAeAyAM_AMtGAEGSgSgACyAemEGSg_____yACyAE_____yAOyAAy______ABtGGGAEGSg______Qo_SgACyAEA45_yABGAEGSgtG 7SwiftUI9TupleViewV AA4TextV AA7SectionV 06CameraB018SettingsTitleLabelV AA6PickerV AH0G10UISettingsC21ModeWheelPeekBehaviorO AA7ForEachV AA6ToggleV AA6VStackV AA6HStackV AA6SpacerV AA6SliderV AA05EmptyD0V AH15ChromeImageWellV5ShapeO AA15DisclosureGroupV AH20MaterialStylingStateV13MaterialStyleO A10_8GroupingO AA14NavigationLinkV AA15ModifiedContentV AH05BuddyD0V AA16_FlexFrameLayoutV AA23_SafeAreaIgnoringLayoutV AA0D0PAAE15fullScreenCover11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAAA25_Rd__lFQO AA6ButtonV AA0Z0V AH12MeasureNotchV
+ _symbolic _____y___________y_____y_____yACy_____y_____yADyADyADy__________G_____G_____yADyADyADyADy_____y__________G_____G_____GAHG_____y_____AWSQ12CoreGraphicsyHCg_GGSgGGADy__________yADyADyADyAR_____yANGGASGAHGSgGGG______y___________Qo_Qo__ADyADyADyADyADyADyADyADyApLyAFyADyADyADyADyAoLyAMy_____y_____GAOGGG_____GAQG_____G_____GGGA30_GA30_GA30_GA30_GA30_GA30_GA30_GSgtGGAHG______tGG 7SwiftUI13_VariadicViewO4TreeV AA13_ZStackLayoutV AA05TupleD0V AA15ModifiedContentV AA0F0V AA0D0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaNRd__lFQO AA012_ConditionalJ0V 06CameraB009ChromePadD0V AA024_SafeAreaRegionsIgnoringG0V AA010_FlexFrameG0V AA16_OverlayModifierV AA06_ShapeD0V AA9RectangleV AA5ColorV AA06_FrameG0V AZ17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AZ0tD7DefaultV AA19_BackgroundModifierV AA01_J13ShapeModifierV AoAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AZ0s10UISettingsD0V AZ0tD5ModelC AA13_StrokedShapeV A10_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionG0V AA05EmptyD0V AZ03TopvW12HeightReaderV
+ _symbolic _____y___________y_____y_____y_____yAEyAEy__________G_____G_____yAEyAEyAEyAEy_____y__________G_____G_____GAGG_____y_____AVSQ12CoreGraphicsyHCg_GGSgGGAEy__________yAEyAEyAEyAQ_____yAMGGARGAGGSgGGG______y___________Qo_Qo__AEyAEyAEyAEyAEyAEyAEyAEyAoKyADyAEyAEyAEyAEyAnKyALy_____y_____GANGGG_____GAPG_____G_____GGGA29_GA29_GA29_GA29_GA29_GA29_GA29_GSgtGG 7SwiftUI13_VariadicViewO4TreeV AA13_ZStackLayoutV AA05TupleD0V AA0D0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaJRd__lFQO AA19_ConditionalContentV AA08ModifiedQ0V 06CameraB009ChromePadD0V AA024_SafeAreaRegionsIgnoringG0V AA010_FlexFrameG0V AA16_OverlayModifierV AA06_ShapeD0V AA9RectangleV AA5ColorV AA06_FrameG0V AX17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AX0tD7DefaultV AA19_BackgroundModifierV AA01_Q13ShapeModifierV AkAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AX0s10UISettingsD0V AX0tD5ModelC AA13_StrokedShapeV A8_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionG0V AA05EmptyD0V
+ _symbolic _____y__________y___________y_____SgACy_____yAD__________ySayAIGAiDGG______yADG_____yACy_____yACyAD______ADtGG______yAD_____GtGGAYtGAGGSgAEyAgHyAD_____AJySayA1_GA1_ADGGAGGSgAEyAgCy_____yAdCyAHyAD_____AJySayA8_GA8_ADGG_A6OtGG_AHyAD_____AJySayA14_GA14_ADGGA7_yAdCyAO_A16OA11_tGSgGAOA7_yAdCyAO_AoYtGGtGAGGSgAEyAgCyAY_AYtGAGGSgA28_AEyAgyGGSgAEyAG_____yAD_____yA32_y__________G_____GGAGGSgAEyAgCyAO_AOtGAGGSgSgAEyAgoGGSg_____yAEyAG_____yAQyACy______ADtGGGAGGSg______Qo_SgAEyAGA47_yADGAGGSgtGG 7SwiftUI4ListV s5NeverO AA9TupleViewV AA4TextV AA7SectionV 06CameraB018SettingsTitleLabelV AA6PickerV AL0I10UISettingsC21ModeWheelPeekBehaviorO AA7ForEachV AA6ToggleV AA6VStackV AA6HStackV AA6SpacerV AA6SliderV AA05EmptyF0V AL15ChromeImageWellV5ShapeO AA15DisclosureGroupV AL20MaterialStylingStateV13MaterialStyleO A14_8GroupingO AA14NavigationLinkV AA15ModifiedContentV AL05BuddyF0V AA16_FlexFrameLayoutV AA23_SafeAreaIgnoringLayoutV AA0F0PAAE15fullScreenCover11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAAA29_Rd__lFQO AA6ButtonV AA5ImageV AL12MeasureNotchV
+ _symbolic _____y_____y_____G_ADtG 7SwiftUI9TupleViewV AA6ToggleV AA4TextV
+ _symbolic _____y_____y__________y___________y_____SgADy_____yAE__________ySayAJGAjEGG______yAEG_____yADy_____yADyAE______AEtGG______yAE_____GtGGAZtGAHGSgAFyAhIyAE_____AKySayA2_GA2_AEGGAHGSgAFyAhDy_____yAeDyAIyAE_____AKySayA9_GA9_AEGG_A6PtGG_AIyAE_____AKySayA15_GA15_AEGGA8_yAeDyAP_A16PA12_tGSgGAPA8_yAeDyAP_ApZtGGtGAHGSgAFyAhDyAZ_AZtGAHGSgA29_AFyAhzHGSgAFyAH_____yAE_____yA33_y__________G_____GGAHGSgAFyAhDyAP_APtGAHGSgSgAFyAhpHGSg_____yAFyAH_____yARyADy______AEtGGGAHGSg______Qo_SgAFyAHA48_yAEGAHGSgtGGG 7SwiftUI14NavigationViewV AA4ListV s5NeverO AA05TupleD0V AA4TextV AA7SectionV 06CameraB018SettingsTitleLabelV AA6PickerV AN0J10UISettingsC21ModeWheelPeekBehaviorO AA7ForEachV AA6ToggleV AA6VStackV AA6HStackV AA6SpacerV AA6SliderV AA05EmptyD0V AN15ChromeImageWellV5ShapeO AA15DisclosureGroupV AN20MaterialStylingStateV13MaterialStyleO A16_8GroupingO AA0C4LinkV AA15ModifiedContentV AN05BuddyD0V AA16_FlexFrameLayoutV AA23_SafeAreaIgnoringLayoutV AA0D0PAAE15fullScreenCover11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAAA31_Rd__lFQO AA6ButtonV AA5ImageV AN12MeasureNotchV
+ _symbolic _____y_____y_____yAAyAByACy_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______tGG_____y_____SgGG 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V AT03TopsT12HeightReaderV AA30_EnvironmentKeyWritingModifierV AA9NamespaceV2IDV
+ _symbolic _____y_____y_____yAAyABy_____y_____yACyACyACy__________G_____G_____yACyACyACyACy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGACy__________yACyACyACyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__ACyACyACyACyACyACyACyACyAnJyADyACyACyACyACyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______tGG 7SwiftUI6ZStackV AA9TupleViewV AA15ModifiedContentV AA0E0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalG0V 06CameraB009ChromePadE0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeE0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qE7DefaultV AA19_BackgroundModifierV AA01_G13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsE0V AT0qE5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyE0V AT03TopsT12HeightReaderV
+ _symbolic _____y_____y_____yAByABy__________G_____G_____yAByAByAByABy_____y__________G_____G_____GADG_____y_____ASSQ12CoreGraphicsyHCg_GGSgGGABy__________yAByAByAByAN_____yAJGGAOGADGSgGGG______y___________Qo_Qo__AByAByAByAByAByAByAByAByAlHyAAyAByAByAByAByAkHyAIy_____y_____GAKGGG_____GAMG_____G_____GGGA26_GA26_GA26_GA26_GA26_GA26_GA26_GSgt 7SwiftUI4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AA19_ConditionalContentV AA08ModifiedL0V 06CameraB009ChromePadC0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameU0V AA16_OverlayModifierV AA06_ShapeC0V AA9RectangleV AA5ColorV AA01_wU0V AP09DebugMenuY0V AA015_GeometryActionY0V So6CGRectV AP0oC7DefaultV AA011_BackgroundY0V AA01_lzY0V AcAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AP0n10UISettingsC0V AP0oC5ModelC AA08_StrokedZ0V A0_6_InsetV AA017_AllowsHitTestingY0V AA09_PositionU0V AA05EmptyC0V
+ _symbolic _____y_____y_____y_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V
+ _symbolic _____y_____y_____y_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______t 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V AT03TopsT12HeightReaderV
- +[CAMCaptureConfiguration _fallbackVideoConfigurationForUnsupportedConfiguration:]
- +[CAMCaptureConfiguration sanitizeVideoConfigurationForDesiredConfiguration:mode:device:trueVideoEnabled:]
- +[CAMCaptureConversions CMVideoDimensionsForCAMPhotoResolution:]
- +[CAMConflictingControlConfiguration resolveDesiredMacroMode:forMode:device:videoConfiguration:videoStabilizationStrength:photoFormat:optionalDepthEffectEnabled:]
- +[CAMZoomControlUtilities exifFocalLengthsByZoomFactorForMode:device:videoConfiguration:videoStabilizationStrength:customLensGroup:isTrueVideo:]
- +[CAMZoomControlUtilities shouldApplyContinuousZoomForMode:device:videoConfiguration:videoStabilizationStrength:zoomFactors:displayZoomFactors:]
- +[CAMZoomControlUtilities shouldEmulateTripleCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:]
- +[CAMZoomControlUtilities shouldEmulateWideDualCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:]
- +[CAMZoomControlUtilities zoomControlDisplayValueForZoomFactor:mode:device:videoConfiguration:videoStabilizationStrength:]
- +[CAMZoomControlUtilities zoomControlDisplayValueForZoomFactor:mode:device:videoConfiguration:videoStabilizationStrength:].cold.1
- -[CAMCaptureCapabilities _shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:]
- -[CAMCaptureCapabilities defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:isTrueVideo:prefersHDR10BitVideo:overrodeWithForcedZoomValue:]
- -[CAMCaptureCapabilities fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:macroMode:]
- -[CAMCaptureCapabilities isActionModeControlSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:]
- -[CAMCaptureCapabilities isEnhancedStabilizationSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:]
- -[CAMCaptureCapabilities isLensPositionControlSupportedForMode:device:videoConfiguration:videoStabilizationStrength:]
- -[CAMCaptureCapabilities isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:]
- -[CAMCaptureCapabilities isSupportedVideoConfiguration:forMode:device:trueVideoEnabled:]
- -[CAMCaptureCapabilities isTripleCameraSupportedForMode:devicePosition:videoConfiguration:videoStabilizationStrength:]
- -[CAMCaptureCapabilities isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:trueVideoEnabled:prefersHDR10BitVideo:]
- -[CAMCaptureCapabilities isVideoStabilizationStrength:supportedForMode:devicePosition:trueVideoEnabled:]
- -[CAMCaptureCapabilities isZoomPIPSupportedForMode:devicePosition:]
- -[CAMCaptureCapabilities preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:]
- -[CAMCaptureCapabilities resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:]
- -[CAMCaptureCapabilities shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:]
- -[CAMCaptureCommandContext _captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:]
- -[CAMCaptureCommandContext videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:]
- -[CAMCaptureEngineDevice videoDeviceFormatForGraphConfiguration:captureSession:]
- -[CAMCaptureGraphConfiguration initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:mixAudioWithOthers:windNoiseRemovalEnabled:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:smartStyles:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:videoBinned:enableDepthSuggestion:enableZoomPIP:customLensGroup:trueVideoEnabled:prefersHDR10BitVideo:]
- -[CAMFullscreenViewfinder _layoutViewportWithFrame:previewFrame:trueVideoTransitionPercentComplete:]
- -[CAMFullscreenViewfinder _updatePreviewLayerForPreviewFrame:viewportFrame:trueVideoTransitionPercentComplete:]
- -[CAMModeAndDeviceCommand _specificFramerateCommandForGraphConfiguration:withContext:]
- -[CAMVideoFramerateCommand initWithVideoConfiguration:]
- -[CAMVideoStabilizationCommand initWithAutomaticVideoStabilizationEnabled:strength:]
- -[CUCaptureController _commandForResetFocus:resetExposure:resetExposureTargetBias:]
- GCC_except_table1191
- GCC_except_table1200
- GCC_except_table1206
- GCC_except_table122
- GCC_except_table1240
- GCC_except_table1317
- GCC_except_table1323
- GCC_except_table1329
- GCC_except_table135
- GCC_except_table1421
- GCC_except_table174
- GCC_except_table175
- GCC_except_table178
- GCC_except_table206
- GCC_except_table229
- GCC_except_table233
- GCC_except_table241
- GCC_except_table252
- GCC_except_table257
- GCC_except_table274
- GCC_except_table293
- GCC_except_table299
- GCC_except_table305
- GCC_except_table307
- GCC_except_table309
- GCC_except_table311
- GCC_except_table315
- GCC_except_table318
- GCC_except_table612
- GCC_except_table614
- GCC_except_table677
- GCC_except_table842
- GCC_except_table862
- GCC_except_table89
- GCC_except_table915
- GCC_except_table917
- GCC_except_table919
- GCC_except_table98
- ___100-[CAMFullscreenViewfinder _layoutViewportWithFrame:previewFrame:trueVideoTransitionPercentComplete:]_block_invoke
- ___103-[CAMViewfinderViewController _requestPasscodeUnlockForCameraRollController:forAction:completionBlock:]_block_invoke.1386
- ___132-[CAMCaptureEngine _captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:forVideoCaptureRequest:videoZoomFactor:error:]_block_invoke.328
- ___140-[CAMUserPreferences readPreferencesWithOverrides:emulationMode:callActive:shouldResetCaptureConfiguration:bypassXPCWhenReadingSystemStyle:]_block_invoke.610
- ___144+[CAMZoomControlUtilities exifFocalLengthsByZoomFactorForMode:device:videoConfiguration:videoStabilizationStrength:customLensGroup:isTrueVideo:]_block_invoke
- ___33-[CAMCaptureEngine stopRecording]_block_invoke.316
- ___35-[CAMCaptureEngine enqueueCommand:]_block_invoke.221
- ___39-[CAMCaptureEngine stopWithCompletion:]_block_invoke.109
- ___47-[CAMCaptureEngine _handleSessionInterruption:]_block_invoke.145
- ___47-[CAMCaptureEngine _handleSessionInterruption:]_block_invoke.146
- ___63-[CAMCaptureEngine _captureEngineDeviceForDeviceType:position:]_block_invoke.447
- ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke.157
- ___66-[CAMCaptureEngine _handleFailedSessionRecoveryAttemptAfterDelay:]_block_invoke_2.158
- ___70-[CAMCaptureEngine captureOutput:willBeginCaptureForResolvedSettings:]_block_invoke.255
- ___72-[CAMCaptureEngine _commitSessionConfigurationIfNecessaryWithLogReason:]_block_invoke.218
- ___72-[CAMViewfinderViewController _createPhysicalCaptureInteractionIfNeeded]_block_invoke.1125
- ___75-[CUCaptureController stillImageRequest:didCompleteVideoCaptureWithResult:]_block_invoke.275
- ___85-[CAMCaptureEngine captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:]_block_invoke.320
- ___92-[CAMCaptureEngine captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:]_block_invoke.417
- ___92-[CAMViewfinderViewController _requestPasscodeUnlockForDocumentScanningWithCompletionBlock:]_block_invoke.1390
- ___block_literal_global.103
- ___block_literal_global.109
- ___block_literal_global.116
- ___block_literal_global.1217
- ___block_literal_global.1374
- ___block_literal_global.1385
- ___block_literal_global.1389
- ___block_literal_global.151
- ___block_literal_global.313
- ___block_literal_global.323
- ___block_literal_global.331
- ___block_literal_global.450
- ___block_literal_global.46
- ___block_literal_global.493
- ___block_literal_global.55
- ___block_literal_global.58
- ___block_literal_global.654
- ___block_literal_global.656
- ___block_literal_global.661
- ___block_literal_global.663
- ___block_literal_global.92
- ___block_literal_global.97
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACyACyAA6VStackVyAA9TupleViewVyACyAA6HStackVyAGyAA4TextV_AA6SpacerVtGGAA14_PaddingLayoutVGSg_ACyACyAA4GridVyAA7ForEachVySaySi6offset_06CameraB013ChromeElementO7elementtGSiAWySaySiAX_AY0R4MenuVA0_tGSiACyAY06TopBarU0V0vwU3Row33_922393C89093045A7FB9387957ECEEF9LLVAA21_TraitWritingModifierVyAA18TransitionTraitKeyVGGGSgGGAA010_FlexFrameL0VGAQGACyAA0G0PAAE8trackingyQr12CoreGraphics7CGFloatVFQOyACyACyAkQGAA30_EnvironmentKeyWritingModifierVyAA4FontVSgGG_Qo_AA24_ForegroundStyleModifierVyAA5ColorVGGSgtGGAQGAQGA21_GAY06RotateN26ControlOrientationModifierVGAAA24_HPA50_AAA24_HPA49_AAA24_HPA48_AAA24_HPA47_AAA24_HPyHC_AqA0G8ModifierHPyHCHC_AqAA54_HPyHCHC_A21_AAA54_HPyHCHC_A52_AAA54_HPyHCHC.41
- _get_witness_table 7SwiftUI15ModifiedContentVyACyACyACyAA6ZStackVyAA9TupleViewVyACyAEyAGyAA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQOyAA012_ConditionalD0VyACyACyACy06CameraB009ChromePadG0VAA30_SafeAreaRegionsIgnoringLayoutVGAA010_FlexFrameW0VGAA16_OverlayModifierVyACyACyACyACyAA06_ShapeG0VyAA9RectangleVAA5ColorVGAA01_yW0VGAT17DebugMenuModifierVGAXGAA23_GeometryActionModifierVySo6CGRectVA20_SQ12CoreGraphicsyHCg_GGSgGGACyAT0qG7DefaultVAA19_BackgroundModifierVyACyACyACyA12_AA01_D13ShapeModifierVyA6_GGA14_GAXGSgGGG_AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQOyAT0p10UISettingsG0V_AT0qG5ModelCQo_Qo__ACyACyACyACyACyACyACyA9_A2_yASyACyACyACyACyA8_A2_yA4_yAA13_StrokedShapeVyA6_6_InsetVGA8_GGGAA25_AllowsHitTestingModifierVGA11_GAA09_PositionW0VGAA05EmptyG0VGGGA69_GA69_GA69_GA69_GA69_GA69_GSgtGGAXG_AT03TopsT12HeightReaderVtGGAA30_EnvironmentKeyWritingModifierVyAA9NamespaceV2IDVSgGGA86_yAT0Q15ScenePhaseModelCSgGGA86_ySo6CGSizeVGGA86_yA21_7CGFloatVGGAaHHPA102_AaHHPA98_AaHHPA93_AaHHPA84_AaHHPyHC_A92_AA0G8ModifierHPyHCHC_A97_AAA107_HPyHCHC_A101_AAA107_HPyHCHC_A105_AAA107_HPyHCHC.81
- _get_witness_table 7SwiftUI4ViewPAAE19simultaneousGesture_9includingQrqd___AA0E4MaskVtAA0E0Rd__lFQOyAA01_C16Modifier_ContentVy06CameraB009DebugMenuH0VG_AA06_EndedE0VyAA03TapE0VGQo_SgAaBHpqd0__AaBHD3_ATHO_HC.83
- _get_witness_table 7SwiftUI7GridRowVyAA9TupleViewVyAA0F0PAAE20accessibilityElement8childrenQrAA26AccessibilityChildBehaviorV_tFQOyAgAE11buttonStyleyQrqd__AA015PrimitiveButtonN0Rd__lFQOyAA15ModifiedContentVyAA0P0VyAA6HStackVyAEyAOy06CameraB006ChromeH4IconOAA30_EnvironmentKeyWritingModifierVyAA5ImageV5ScaleOGGSg_AOyAgAE8trackingyQr12CoreGraphics7CGFloatVFQOyAOyAgAE17hyphenationFactoryQrA7_FQOyAA4TextV_Qo_AXySiSgGG_Qo_AA16_FixedSizeLayoutVGAA6SpacerVtGGGAA12_FrameLayoutVG_AA05PlainpN0VQo__Qo__AA7ForEachVySaySi6offset_AT0U10MenuOptionV7elementtGSiAOyAOyAOyAgAE0g10ShowsLargeR6VieweryQrqd__yXEAaFRd__lFQOyAgAEALyQrqd__AaMRd__lFQOyAQyAOyAOyASyAEyAOyAOyAOyAOyAZA25_GAA14_PaddingLayoutVGAT0t10ForegroundnZ0VGAA14_OpacityEffectVG_AOyAOyAOyAOyAOyAOyA10_A13_GAXyAA0R10TransitionVGGAA010_AnimationZ0VySSGGA44_GAA0j10AttachmentZ0VGA17_GAOyAOyAOyA10_A56_GA44_GA60_GSgA20_tGGA25_GAA16_FlexFrameLayoutVGG_A28_Qo__A10_Qo_AA01_c8CellSizeZ0VGAA01_c9AlignmentZ0VGA60_GGtGGAaFHPyHC.67
- _get_witness_table 7SwiftUI9TupleViewVyAA4TextV_AA7SectionVy06CameraB018SettingsTitleLabelVSgACyAA6PickerVyAeH0G10UISettingsC21ModeWheelPeekBehaviorOAA7ForEachVySayAQGAqEGG_AA6ToggleVyAEGAA6VStackVyACyAA6HStackVyACyAE_AA6SpacerVAEtGG_AA6SliderVyAeA05EmptyD0VGtGGA12_tGAKGSgAGyAkMyAeH15ChromeImageWellV5ShapeOASySayA19_GA19_AEGGAKGSgAGyAkCyAA15DisclosureGroupVyAeCyAMyAeH20MaterialStylingStateV13MaterialStyleOASySayA30_GA30_AEGG_A6YtGG_AMyAEA28_8GroupingOASySayA37_GA37_AEGGA26_yAeCyAY_A16YA33_tGSgGAYA26_yAeCyAY_AYA12_tGGtGAKGSgAGyAkCyA12__A12_tGAKGSgA51_AGyAKA12_AKGSgAGyAkA14NavigationLinkVyAeA15ModifiedContentVyA57_yAH05BuddyD0VAA16_FlexFrameLayoutVGAA23_SafeAreaIgnoringLayoutVGGAKGSgAGyAkyKGSgAA0D0PAAE15fullScreenCover11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAAA71_Rd__lFQOyAGyAkA6ButtonVyA1_yACyAA0Z0V_AEtGGGAKGSg_AH12MeasureNotchVQo_SgAGyAKA82_yAEGAKGSgtGAAA71_HPyHC.549
- _keypath_get.411Tm
- _keypath_get.470Tm
- _keypath_get.518Tm
- _keypath_get.554Tm
- _keypath_get.722Tm
- _keypath_set.102Tm
- _keypath_set.11Tm
- _keypath_set.20Tm
- _keypath_set.349Tm
- _keypath_set.463Tm
- _keypath_set.60Tm
- _objc_msgSend$CMVideoDimensionsForCAMPhotoResolution:
- _objc_msgSend$_captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:
- _objc_msgSend$_commandForResetFocus:resetExposure:resetExposureTargetBias:
- _objc_msgSend$_fallbackVideoConfigurationForUnsupportedConfiguration:
- _objc_msgSend$_layoutViewportWithFrame:previewFrame:trueVideoTransitionPercentComplete:
- _objc_msgSend$_shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$_specificFramerateCommandForGraphConfiguration:withContext:
- _objc_msgSend$_updatePreviewLayerForPreviewFrame:viewportFrame:trueVideoTransitionPercentComplete:
- _objc_msgSend$defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:isTrueVideo:prefersHDR10BitVideo:overrodeWithForcedZoomValue:
- _objc_msgSend$exifFocalLengthsByZoomFactorForMode:device:videoConfiguration:videoStabilizationStrength:customLensGroup:isTrueVideo:
- _objc_msgSend$fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:macroMode:
- _objc_msgSend$initWithAutomaticVideoStabilizationEnabled:strength:
- _objc_msgSend$initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:mixAudioWithOthers:windNoiseRemovalEnabled:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:smartStyles:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:videoBinned:enableDepthSuggestion:enableZoomPIP:customLensGroup:trueVideoEnabled:prefersHDR10BitVideo:
- _objc_msgSend$initWithVideoConfiguration:
- _objc_msgSend$isActionModeControlSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:
- _objc_msgSend$isEnhancedStabilizationSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:
- _objc_msgSend$isLensPositionControlSupportedForMode:device:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$isSupportedVideoConfiguration:forMode:device:trueVideoEnabled:
- _objc_msgSend$isTripleCameraSupportedForMode:devicePosition:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:trueVideoEnabled:prefersHDR10BitVideo:
- _objc_msgSend$isVideoStabilizationStrength:supportedForMode:devicePosition:trueVideoEnabled:
- _objc_msgSend$isZoomPIPSupportedForMode:devicePosition:
- _objc_msgSend$preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$resolveDesiredMacroMode:forMode:device:videoConfiguration:videoStabilizationStrength:photoFormat:optionalDepthEffectEnabled:
- _objc_msgSend$resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$sanitizeVideoConfigurationForDesiredConfiguration:mode:device:trueVideoEnabled:
- _objc_msgSend$shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$shouldApplyContinuousZoomForMode:device:videoConfiguration:videoStabilizationStrength:zoomFactors:displayZoomFactors:
- _objc_msgSend$shouldEmulateTripleCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$shouldEmulateWideDualCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:
- _objc_msgSend$videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:
- _objc_msgSend$videoDeviceFormatForGraphConfiguration:captureSession:
- _objc_msgSend$zoomControlDisplayValueForZoomFactor:mode:device:videoConfiguration:videoStabilizationStrength:
- _objectdestroy.48Tm
- _symbolic ___________y_____Sg_____y_____yAA__________ySayAGGAgAGG______yAAG_____yAEy_____yAEyAA______AAtGG______yAA_____GtGGAWtGADGSgAByAdFyAA_____AHySayA_GA_AAGGADGSgAByAdEy_____yAaEyAFyAA_____AHySayA6_GA6_AAGG_A6MtGG_AFyAA_____AHySayA12_GA12_AAGGA5_yAaEyAM_A16MA9_tGSgGAMA5_yAaEyAM_AmWtGGtGADGSgAByAdEyAW_AWtGADGSgA26_AByAdwDGSgAByAD_____yAA_____yA30_y__________G_____GGADGSgAByAdmDGSg_____yAByAD_____yAOyAEy______AAtGGGADGSg______Qo_SgAByADA41_yAAGADGSgt 7SwiftUI4TextV AA7SectionV 06CameraB018SettingsTitleLabelV AA9TupleViewV AA6PickerV AF0E10UISettingsC21ModeWheelPeekBehaviorO AA7ForEachV AA6ToggleV AA6VStackV AA6HStackV AA6SpacerV AA6SliderV AA05EmptyJ0V AF15ChromeImageWellV5ShapeO AA15DisclosureGroupV AF20MaterialStylingStateV13MaterialStyleO A10_8GroupingO AA14NavigationLinkV AA15ModifiedContentV AF05BuddyJ0V AA16_FlexFrameLayoutV AA23_SafeAreaIgnoringLayoutV AA0J0PAAE15fullScreenCover11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAAA25_Rd__lFQO AA6ButtonV AA0Z0V AF12MeasureNotchV
- _symbolic _____yAAyAAyAAyAAyAAyAAy_____y__________G_____y_____yAAyAAyAAyAAyAdFyABy_____y_____GADGGG_____G_____G_____G_____GGGAVGAVGAVGAVGAVGAVGSg 7SwiftUI15ModifiedContentV AA10_ShapeViewV AA9RectangleV AA5ColorV AA16_OverlayModifierV AA012_ConditionalD0V AA08_StrokedE0V AG6_InsetV AA017_AllowsHitTestingJ0V AA12_FrameLayoutV AA09_PositionR0V AA05EmptyF0V
- _symbolic _____yAAyAAyAAy_____y_____yAAyAByACy_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______tGG_____y_____SgGGA43_y_____SgGGA43_y_____GGA43_y_____GG 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V AT03TopsT12HeightReaderV AA30_EnvironmentKeyWritingModifierV AA9NamespaceV2IDV AT0Q15ScenePhaseModelC So6CGSizeV 12CoreGraphics7CGFloatV
- _symbolic _____yAAyAAy_____y_____yAAyAByACy_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______tGG_____y_____SgGGA43_y_____SgGGA43_y_____GG 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V AT03TopsT12HeightReaderV AA30_EnvironmentKeyWritingModifierV AA9NamespaceV2IDV AT0Q15ScenePhaseModelC So6CGSizeV
- _symbolic _____yAAy_____y_____yAAyAByACy_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______tGG_____y_____SgGGA43_y_____SgGG 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V AT03TopsT12HeightReaderV AA30_EnvironmentKeyWritingModifierV AA9NamespaceV2IDV AT0Q15ScenePhaseModelC
- _symbolic _____y___________y_____SgAAy_____yAB__________ySayAGGAgBGG______yABG_____yAAy_____yAAyAB______ABtGG______yAB_____GtGGAWtGAEGSgACyAeFyAB_____AHySayA_GA_ABGGAEGSgACyAeAy_____yAbAyAFyAB_____AHySayA6_GA6_ABGG_A6MtGG_AFyAB_____AHySayA12_GA12_ABGGA5_yAbAyAM_A16MA9_tGSgGAMA5_yAbAyAM_AmWtGGtGAEGSgACyAeAyAW_AWtGAEGSgA26_ACyAewEGSgACyAE_____yAB_____yA30_y__________G_____GGAEGSgACyAemEGSg_____yACyAE_____yAOyAAy______ABtGGGAEGSg______Qo_SgACyAEA41_yABGAEGSgtG 7SwiftUI9TupleViewV AA4TextV AA7SectionV 06CameraB018SettingsTitleLabelV AA6PickerV AH0G10UISettingsC21ModeWheelPeekBehaviorO AA7ForEachV AA6ToggleV AA6VStackV AA6HStackV AA6SpacerV AA6SliderV AA05EmptyD0V AH15ChromeImageWellV5ShapeO AA15DisclosureGroupV AH20MaterialStylingStateV13MaterialStyleO A10_8GroupingO AA14NavigationLinkV AA15ModifiedContentV AH05BuddyD0V AA16_FlexFrameLayoutV AA23_SafeAreaIgnoringLayoutV AA0D0PAAE15fullScreenCover11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAAA25_Rd__lFQO AA6ButtonV AA0Z0V AH12MeasureNotchV
- _symbolic _____y___________y_____y_____yACy_____y_____yADyADyADy__________G_____G_____yADyADyADyADy_____y__________G_____G_____GAHG_____y_____AWSQ12CoreGraphicsyHCg_GGSgGGADy__________yADyADyADyAR_____yANGGASGAHGSgGGG______y___________Qo_Qo__ADyADyADyADyADyADyADyApLyAFyADyADyADyADyAoLyAMy_____y_____GAOGGG_____GAQG_____G_____GGGA30_GA30_GA30_GA30_GA30_GA30_GSgtGGAHG______tGG 7SwiftUI13_VariadicViewO4TreeV AA13_ZStackLayoutV AA05TupleD0V AA15ModifiedContentV AA0F0V AA0D0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaNRd__lFQO AA012_ConditionalJ0V 06CameraB009ChromePadD0V AA024_SafeAreaRegionsIgnoringG0V AA010_FlexFrameG0V AA16_OverlayModifierV AA06_ShapeD0V AA9RectangleV AA5ColorV AA06_FrameG0V AZ17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AZ0tD7DefaultV AA19_BackgroundModifierV AA01_J13ShapeModifierV AoAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AZ0s10UISettingsD0V AZ0tD5ModelC AA13_StrokedShapeV A10_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionG0V AA05EmptyD0V AZ03TopvW12HeightReaderV
- _symbolic _____y___________y_____y_____y_____yAEyAEy__________G_____G_____yAEyAEyAEyAEy_____y__________G_____G_____GAGG_____y_____AVSQ12CoreGraphicsyHCg_GGSgGGAEy__________yAEyAEyAEyAQ_____yAMGGARGAGGSgGGG______y___________Qo_Qo__AEyAEyAEyAEyAEyAEyAEyAoKyADyAEyAEyAEyAEyAnKyALy_____y_____GANGGG_____GAPG_____G_____GGGA29_GA29_GA29_GA29_GA29_GA29_GSgtGG 7SwiftUI13_VariadicViewO4TreeV AA13_ZStackLayoutV AA05TupleD0V AA0D0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaJRd__lFQO AA19_ConditionalContentV AA08ModifiedQ0V 06CameraB009ChromePadD0V AA024_SafeAreaRegionsIgnoringG0V AA010_FlexFrameG0V AA16_OverlayModifierV AA06_ShapeD0V AA9RectangleV AA5ColorV AA06_FrameG0V AX17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AX0tD7DefaultV AA19_BackgroundModifierV AA01_Q13ShapeModifierV AkAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AX0s10UISettingsD0V AX0tD5ModelC AA13_StrokedShapeV A8_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionG0V AA05EmptyD0V
- _symbolic _____y__________y___________y_____SgACy_____yAD__________ySayAIGAiDGG______yADG_____yACy_____yACyAD______ADtGG______yAD_____GtGGAYtGAGGSgAEyAgHyAD_____AJySayA1_GA1_ADGGAGGSgAEyAgCy_____yAdCyAHyAD_____AJySayA8_GA8_ADGG_A6OtGG_AHyAD_____AJySayA14_GA14_ADGGA7_yAdCyAO_A16OA11_tGSgGAOA7_yAdCyAO_AoYtGGtGAGGSgAEyAgCyAY_AYtGAGGSgA28_AEyAgyGGSgAEyAG_____yAD_____yA32_y__________G_____GGAGGSgAEyAgoGGSg_____yAEyAG_____yAQyACy______ADtGGGAGGSg______Qo_SgAEyAGA43_yADGAGGSgtGG 7SwiftUI4ListV s5NeverO AA9TupleViewV AA4TextV AA7SectionV 06CameraB018SettingsTitleLabelV AA6PickerV AL0I10UISettingsC21ModeWheelPeekBehaviorO AA7ForEachV AA6ToggleV AA6VStackV AA6HStackV AA6SpacerV AA6SliderV AA05EmptyF0V AL15ChromeImageWellV5ShapeO AA15DisclosureGroupV AL20MaterialStylingStateV13MaterialStyleO A14_8GroupingO AA14NavigationLinkV AA15ModifiedContentV AL05BuddyF0V AA16_FlexFrameLayoutV AA23_SafeAreaIgnoringLayoutV AA0F0PAAE15fullScreenCover11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAAA29_Rd__lFQO AA6ButtonV AA5ImageV AL12MeasureNotchV
- _symbolic _____y_____y__________y___________y_____SgADy_____yAE__________ySayAJGAjEGG______yAEG_____yADy_____yADyAE______AEtGG______yAE_____GtGGAZtGAHGSgAFyAhIyAE_____AKySayA2_GA2_AEGGAHGSgAFyAhDy_____yAeDyAIyAE_____AKySayA9_GA9_AEGG_A6PtGG_AIyAE_____AKySayA15_GA15_AEGGA8_yAeDyAP_A16PA12_tGSgGAPA8_yAeDyAP_ApZtGGtGAHGSgAFyAhDyAZ_AZtGAHGSgA29_AFyAhzHGSgAFyAH_____yAE_____yA33_y__________G_____GGAHGSgAFyAhpHGSg_____yAFyAH_____yARyADy______AEtGGGAHGSg______Qo_SgAFyAHA44_yAEGAHGSgtGGG 7SwiftUI14NavigationViewV AA4ListV s5NeverO AA05TupleD0V AA4TextV AA7SectionV 06CameraB018SettingsTitleLabelV AA6PickerV AN0J10UISettingsC21ModeWheelPeekBehaviorO AA7ForEachV AA6ToggleV AA6VStackV AA6HStackV AA6SpacerV AA6SliderV AA05EmptyD0V AN15ChromeImageWellV5ShapeO AA15DisclosureGroupV AN20MaterialStylingStateV13MaterialStyleO A16_8GroupingO AA0C4LinkV AA15ModifiedContentV AN05BuddyD0V AA16_FlexFrameLayoutV AA23_SafeAreaIgnoringLayoutV AA0D0PAAE15fullScreenCover11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAAA31_Rd__lFQO AA6ButtonV AA5ImageV AN12MeasureNotchV
- _symbolic _____y_____y_____yAAyAByACy_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______tGG_____y_____SgGG 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V AT03TopsT12HeightReaderV AA30_EnvironmentKeyWritingModifierV AA9NamespaceV2IDV
- _symbolic _____y_____y_____yAAyABy_____y_____yACyACyACy__________G_____G_____yACyACyACyACy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGACy__________yACyACyACyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__ACyACyACyACyACyACyACyAnJyADyACyACyACyACyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______tGG 7SwiftUI6ZStackV AA9TupleViewV AA15ModifiedContentV AA0E0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalG0V 06CameraB009ChromePadE0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeE0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qE7DefaultV AA19_BackgroundModifierV AA01_G13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsE0V AT0qE5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyE0V AT03TopsT12HeightReaderV
- _symbolic _____y_____y_____yAByABy__________G_____G_____yAByAByAByABy_____y__________G_____G_____GADG_____y_____ASSQ12CoreGraphicsyHCg_GGSgGGABy__________yAByAByAByAN_____yAJGGAOGADGSgGGG______y___________Qo_Qo__AByAByAByAByAByAByAByAlHyAAyAByAByAByAByAkHyAIy_____y_____GAKGGG_____GAMG_____G_____GGGA26_GA26_GA26_GA26_GA26_GA26_GSgt 7SwiftUI4ViewPAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaBRd__lFQO AA19_ConditionalContentV AA08ModifiedL0V 06CameraB009ChromePadC0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameU0V AA16_OverlayModifierV AA06_ShapeC0V AA9RectangleV AA5ColorV AA01_wU0V AP09DebugMenuY0V AA015_GeometryActionY0V So6CGRectV AP0oC7DefaultV AA011_BackgroundY0V AA01_lzY0V AcAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AP0n10UISettingsC0V AP0oC5ModelC AA08_StrokedZ0V A0_6_InsetV AA017_AllowsHitTestingY0V AA09_PositionU0V AA05EmptyC0V
- _symbolic _____y_____y_____y_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V
- _symbolic _____y_____y_____y_____y_____yAAyAAyAAy__________G_____G_____yAAyAAyAAyAAy_____y__________G_____G_____GAFG_____y_____AUSQ12CoreGraphicsyHCg_GGSgGGAAy__________yAAyAAyAAyAP_____yALGGAQGAFGSgGGG______y___________Qo_Qo__AAyAAyAAyAAyAAyAAyAAyAnJyADyAAyAAyAAyAAyAmJyAKy_____y_____GAMGGG_____GAOG_____G_____GGGA28_GA28_GA28_GA28_GA28_GA28_GSgtGGAFG______t 7SwiftUI15ModifiedContentV AA6ZStackV AA9TupleViewV AA0G0PAAE5sheet11isPresented9onDismiss7contentQrAA7BindingVySbG_yycSgqd__yctAaHRd__lFQO AA012_ConditionalD0V 06CameraB009ChromePadG0V AA30_SafeAreaRegionsIgnoringLayoutV AA010_FlexFrameW0V AA16_OverlayModifierV AA06_ShapeG0V AA9RectangleV AA5ColorV AA01_yW0V AT17DebugMenuModifierV AA23_GeometryActionModifierV So6CGRectV AT0qG7DefaultV AA19_BackgroundModifierV AA01_D13ShapeModifierV AiAE11environmentyQrqd__SgRld__C11Observation10ObservableRd__lFQO AT0p10UISettingsG0V AT0qG5ModelC AA13_StrokedShapeV A4_6_InsetV AA25_AllowsHitTestingModifierV AA09_PositionW0V AA05EmptyG0V AT03TopsT12HeightReaderV
CStrings:
+ "\"b"
+ "+%@"
+ "+%@(%@"
+ "9:16"
+ "@\"<CAMRecommendedSmartFramingDelegate>\""
+ "@\"CAMAutoFramingStatusIndicator\""
+ "@\"CAMFlipAspectRatioButton\""
+ "@\"CAMFrontPIPButton\""
+ "@\"CAMMultiCamPIPCompositor\""
+ "@\"CAMPIPVideoPreviewView\""
+ "@\"IOSurfaceMemoryPool\""
+ "@\"UIViewFloatAnimatableProperty\""
+ "@104@0:8{?=qiIq}16{CGRect={CGPoint=dd}{CGSize=dd}}40d72d80^{CGColor=}88q96"
+ "@116@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32d64d72^{CGColor=}80B88q92f100f104B108B112"
+ "@124@0:8@16@24@32@40@48{CGRect={CGPoint=dd}{CGSize=dd}}56d88d96^{CGColor=}104B112q116"
+ "@24@0:8f16B20"
+ "@252@0:8q16q24q32q40Q48B56B60Q64q72@80@88q96q104B112B116q120q128B136B140Q144@152@160B168B172B176q180q188q196B204B208B212@216B224B228B232q236q244"
+ "@32@0:8B16B20B24B28"
+ "@36@0:8B16q20B28B32"
+ "@40@0:8@16{CGSize=dd}24"
+ "@40@0:8{?=qiIq}16"
+ "@44@0:8q16{CGPoint=dd}24B40"
+ "@48@0:8@16d24d32^{CGColor=}40"
+ "@56@0:8q16q24q32q40B48B52"
+ "@56@0:8q16q24q32q40q48"
+ "@56@0:8q16{CGPoint=dd}24q40B48B52"
+ "@60@0:8q16q24q32q40B48^q52"
+ "@60@0:8q16q24q32q40q48B56"
+ "@64@0:8q16q24q32q40@48B56B60"
+ "AVCaptureDynamicAspectRatioForCAMDynamicAspectRatio:"
+ "AVCaptureSmartFramingFieldOfViewForCAMCaptureSmartFramingFieldOfView:"
+ "Attempting to configure the secondary device without a device format! Results may be unexpected."
+ "Auto Smart Framing Rotation ["
+ "Auto Smart Framing Zoom ["
+ "AutoSmartFraming"
+ "B16@?0@\"UIViewFloatAnimatableProperty\"8"
+ "B52@0:8q16q24B32q36B44B48"
+ "B56@0:8d16{CGPoint=dd}24{CGPoint=dd}40"
+ "B60@0:8q16q24q32q40B48B52B56"
+ "B68@0:8q16q24q32q40B48^@52^@60"
+ "B72@0:8q16q24q32q40q48B56B60B64B68"
+ "BRIGHT_POP_GRADIENT"
+ "Bottom Over-Capture Gradient Enabled"
+ "BuddyDeviceModel-alt"
+ "CAMAutoSmartFramingEnabledFieldOfViewsCommand"
+ "CAMAutoSmartFramingMonitorCommand"
+ "CAMCaptureSmartFramingFieldOfViewForAVCaptureSmartFraming:"
+ "CAMCaptureSmartFramingFieldOfViewForAVCaptureSmartFramingFieldOfView:"
+ "CAMDebugFrontRearSimultaneousVideoColorDuplicatedMovieFileBuffers"
+ "CAMDebugFrontRearSimultaneousVideoDisableMotionBlur"
+ "CAMDynamicAspectRatioCommand"
+ "CAMERA_SMART_FRAMING_AUTO_ROTATION_OFF"
+ "CAMERA_SMART_FRAMING_AUTO_ROTATION_ON"
+ "CAMERA_SMART_FRAMING_AUTO_ZOOM_OFF"
+ "CAMERA_SMART_FRAMING_AUTO_ZOOM_ON"
+ "CAMERA_SMART_FRAMING_CENTER_STAGE_OFF"
+ "CAMERA_SMART_FRAMING_ROTATE"
+ "CAMERA_SMART_FRAMING_ZOOM"
+ "CAMERA_SMART_FRAMING_ZOOM_AND_ROTATE"
+ "CAMFeatureDevelopmentAllowAutoSmartFraming"
+ "CAMFeatureDevelopmentAllowSmartFraming"
+ "CAMFeatureDevelopmentAllowSmartFramingUsingDynamicAspectRatio"
+ "CAMFeatureDevelopmentFrontRearSimultaneousVideo"
+ "CAMFeatureDevelopmentFrontRearSimultaneousVideo60FPSSupported"
+ "CAMFeatureDevelopmentFrontRearSimultaneousVideoFrontCameraHDR10SupportedOverride"
+ "CAMFeatureDevelopmentFrontRearSimultaneousVideoFrontVideoStabilizationSupported"
+ "CAMFeatureDevelopmentFrontRearSimultaneousVideoPIPMaxBlurRadius"
+ "CAMFeatureDevelopmentFrontRearSimultaneousVideoPIPMetricsMaxCapacity"
+ "CAMFeatureDevelopmentUseCoreImageCVTextureCache"
+ "CAMFeatureDevelopmentUseCoreImageSurfacePool"
+ "CAMFeatureDevelopmentUserSelectableAspectRatio"
+ "CAMFlipAspectRatioButton"
+ "CAMFrontPIPButton"
+ "CAMFrontRearSimultaneousCaptureCommand"
+ "CAMFrontRearSimultaneousVideoRecordingCommand"
+ "CAMMultiCamPIPCompositor"
+ "CAMMultiCamPIPMetrics"
+ "CAMPIPVideoPreviewView"
+ "CAMRecommendedSmartFramingDelegate"
+ "CAMUserPreferenceAlwaysShowFrontPIPIndicator"
+ "CAMUserPreferenceBottomOverCaptureGradientEnabled"
+ "CAMUserPreferenceEnableFrontRearSimultaneousVideo"
+ "CAMUserPreferencePreserveFrontRearSimultaneousVideoEnabled"
+ "CAMUserPreferenceTopOverCaptureGradientEnabled"
+ "CAMUserPreferencesWantsSmartFramingAutoRotationDefault"
+ "CAMUserPreferencesWantsSmartFramingAutoZoomDefault"
+ "CAMVideoFramerateCommandConfigureSecondaryDevice"
+ "CAMVideoStabilizationCommandConfigureSecondaryDevice"
+ "CAMVideoStabilizationCommandFrontRearSimultaneousVideoEnabled"
+ "CAMViewfinderAnimatorSmartFramingTransitionPercentCompleteKey"
+ "CMVideoDimensionsForCAMPhotoResolution:wantsSquareDimensions:"
+ "CameraUI-BrightPop"
+ "CameraUI-FRSV"
+ "CameraUI-SmartFraming"
+ "Chrome.ControlState.Off"
+ "Chrome.ControlState.On"
+ "Chrome.ControlState.On.axLabel"
+ "Chrome.FrontPIP.hide.axLabel"
+ "Chrome.FrontPIP.show.axLabel"
+ "Chrome.SmartFraming.Footer"
+ "CoreImage failed to render the gainmap image to destination: %@."
+ "CoreImage failed to render to destination: %@."
+ "Deferring enabling PIP motion blur for the next compositing session"
+ "Desired smartFramingFieldOfView should not be none if smart framing is supported, defaulting to portrait"
+ "Disabling PIP motion blur for the current compositing session"
+ "Disabling PIP motion blur for the next compositing session"
+ "Enabled smart framings: %@"
+ "Enabling PIP motion blur for the next compositing session"
+ "FRSV"
+ "FRSVCoreImageArchive"
+ "Failed to add connection %{public}@ to session %{public}@"
+ "Failed to find supported smart framing for field of view: %ld"
+ "FlipAspectRatioButton"
+ "FrontPIPButton"
+ "Ignoring auto smart framing recommendation: already equal to desired FOV"
+ "Ignoring auto smart framing recommendation: isSupported: %d, isNoneRecommended: %d, hasCurrentStillImageCaptureMomentSettings %d, isTrueVideoActive %d, isRecording: %d, suggested FOV: %ld"
+ "Ignoring auto smart framing recommendation: reticle is animating"
+ "Ignoring request to flip aspect ratio - reconfiguring: %d reticleAnimating: %d zooming: %d"
+ "Ignoring request to flip aspect ratio - smart framing is in transition"
+ "Ignoring smart framing zoom toggle, reticle animating"
+ "Ignoring tap inside the front PIP preview view area"
+ "Landscape"
+ "Missing PIP location information"
+ "Motion blur radius of %f exceeded max value of %f."
+ "OverrodeAuto"
+ "PIP timestamp %.2f is older than any known timestamps! Oldest timestamp is %.2f. Using oldest timestamp."
+ "QuadraTele"
+ "Received new smart framing recommendation: %ld"
+ "Received new smartFramingMonitor recommendation: %@"
+ "Rotated"
+ "RotatedNarrow"
+ "RotatedWide"
+ "SMART_STYLES_SETTINGS_DESCRIPTION_BRIGHT_POP"
+ "Secondary device %{public}@'s active device format %{public}@ does not match expected device format %{public}@"
+ "Setting dynamic aspect ratio for secondary device: %{public}@"
+ "Setting dynamic aspect ratio: %{public}@"
+ "Setting smartFramingFieldOfView to: %{public}ld using transition: %{public}@"
+ "Smart framing monitor failed to start with error: %{public}@"
+ "Smart framing supported but has no enabled auto framings - isAutoFramingSupported: %d, smartFramingAutoZoomEnabled: %d, smartFramingAutoRotationEnabled: %d"
+ "Smart framing: starting smart framing monitor"
+ "Smart framing: stopping smart framing monitor"
+ "SmartFramingAutoRotation"
+ "SmartFramingAutoZoom"
+ "StylesOnboarding_CN_1.HEIC"
+ "StylesOnboarding_CN_2.HEIC"
+ "StylesOnboarding_CN_3.HEIC"
+ "T@\"<CAMRecommendedSmartFramingDelegate>\",W,N,V_recommendedSmartFramingDelegate"
+ "T@\"<MTLCommandQueue>\",&,N,V__commandQueue"
+ "T@\"<MTLDevice>\",&,N,V__metalDevice"
+ "T@\"AVCaptureDevice\",&,N,V_currentSecondaryVideoDevice"
+ "T@\"AVCaptureDeviceFormat\",&,N,V_currentSecondaryVideoDeviceFormat"
+ "T@\"AVCaptureDeviceInput\",&,N,V_currentSecondaryVideoDeviceInput"
+ "T@\"AVCaptureVideoPreviewLayer\",&,N,V_currentSecondaryVideoPreviewLayer"
+ "T@\"AVCaptureVideoPreviewLayer\",R,N,V__secondaryVideoPreviewLayer"
+ "T@\"CAMAutoFramingStatusIndicator\",R,N,V_autoFramingIndicator"
+ "T@\"CAMFlipAspectRatioButton\",&,N,S_setFlipAspectRatioButton:,V_flipAspectRatioButton"
+ "T@\"CAMFrontPIPButton\",&,N,S_setFrontPIPButton:,V_frontPIPButton"
+ "T@\"CAMMemoizationCache\",R,N,V__cachedDynamicAspectRatioFormat"
+ "T@\"CAMMultiCamPIPCompositor\",&,N,V__multiCamPIPCompositingQueue_multiCamPIPCompositor"
+ "T@\"CAMPIPVideoPreviewView\",R,N,V_frontPIPVideoPreviewView"
+ "T@\"CEKFluidBehaviorSettings\",R,N,V__frontPIPVideoPreviewAnimationSpringSettings"
+ "T@\"CIContext\",&,N,V__ciContext"
+ "T@\"CIContext\",&,N,V__gainMapCIContext"
+ "T@\"IOSurfaceMemoryPool\",&,N,V__surfaceMemoryPool"
+ "T@\"NSArray\",N,V_zoomSymbols"
+ "T@\"NSArray\",R,N,V__smartFramingEnabledFieldsOfView"
+ "T@\"NSMutableDictionary\",R,N,V__pipMetricsByTimestamp"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V__multiCamPIPCompositingQueue"
+ "T@\"UIPanGestureRecognizer\",R,N,V__frontPIPVideoPreviewPanGestureRecognizer"
+ "T@\"UIViewFloatAnimatableProperty\",&,N,V__zoomButtonPlatterOffsetAnimator"
+ "T@\"UIViewVectorAnimatableProperty\",&,N,V__frontPIPVideoPreviewCenterAnimatableProperty"
+ "TB,D,N,GisFrontRearSimultaneousCaptureEnabled"
+ "TB,D,N,GisFrontRearSimultaneousCaptureMirrored"
+ "TB,D,N,GisFrontRearSimultaneousVideoEnabled"
+ "TB,D,N,GisFrontRearSimultaneousVideoMirrored"
+ "TB,N,G_isCompositingSessionActive,V__compositingSessionActive"
+ "TB,N,G_isFrontRearSimultaneousVideoEnabled,S_setFrontRearSimultaneousVideoEnabled:,V__frontRearSimultaneousVideoEnabled"
+ "TB,N,GisFlipAspectRatioButtonVisible,V_flipAspectRatioButtonVisible"
+ "TB,N,GisMotionBlurDisabled,V_motionBlurDisabled"
+ "TB,N,GoffsetZoomButtonForFlipAspectRatioButton,V_offsetZoomButtonForFlipAspectRatioButton"
+ "TB,N,S_setOverrideSmartFramingAutoRotateInLandscapeEnabled:,V__overrideSmartFramingAutoRotateInLandscapeEnabled"
+ "TB,N,S_setOverrideSmartFramingAutoZoomInLandscapeEnabled:,V__overrideSmartFramingAutoZoomInLandscapeEnabled"
+ "TB,N,S_setSmartFramingAutoRotationEnabled:,V__smartFramingAutoRotationEnabled"
+ "TB,N,S_setSmartFramingAutoZoomEnabled:,V__smartFramingAutoZoomEnabled"
+ "TB,N,S_setWantsSmartFramingAutoRotationDefault:,V__wantsSmartFramingAutoRotationDefault"
+ "TB,N,S_setWantsSmartFramingAutoZoomDefault:,V__wantsSmartFramingAutoZoomDefault"
+ "TB,N,V__delaySmartFramingDynamicAspectRatioUpdate"
+ "TB,N,V__excessiveBlurRadiusReported"
+ "TB,N,V__frontPIPVideoPreviewCenterAnimationResetsFocusAndExposure"
+ "TB,N,V__motionBlurDisabledForCurrentCompositingSession"
+ "TB,N,V__pipTimestampTooOldReported"
+ "TB,N,V__useSmartFramingTransition"
+ "TB,N,V__wantsFlipAspectRatio"
+ "TB,N,V_didRecentlyUseFrontPIP"
+ "TB,N,V_frontPIPButtonVisible"
+ "TB,N,V_shouldEnableFrontRearSimultaneousVideo"
+ "TB,N,V_wantsSmartFramingAutoRotationDefault"
+ "TB,N,V_wantsSmartFramingAutoZoomDefault"
+ "TB,R,N,GisAutoSmartFramingSupported,V_autoSmartFramingSupported"
+ "TB,R,N,GisBackQuadraTeleSupported,V_backQuadraTeleSupported"
+ "TB,R,N,GisFrontRearSimultaneousCaptureEnabled,V_frontRearSimultaneousCaptureEnabled"
+ "TB,R,N,GisFrontRearSimultaneousCaptureMirrored,V_frontRearSimultaneousCaptureMirrored"
+ "TB,R,N,GisFrontRearSimultaneousVideo60FPSSupported,V_frontRearSimultaneousVideo60FPSSupported"
+ "TB,R,N,GisFrontRearSimultaneousVideoDeferredFrontCameraEnabled,V_frontRearSimultaneousVideoDeferredFrontCameraEnabled"
+ "TB,R,N,GisFrontRearSimultaneousVideoEnabled,V_frontRearSimultaneousVideoEnabled"
+ "TB,R,N,GisFrontRearSimultaneousVideoFrontCameraHDR10Supported,V_frontRearSimultaneousVideoFrontCameraHDR10Supported"
+ "TB,R,N,GisFrontRearSimultaneousVideoFrontVideoStabilizationSupported,V_frontRearSimultaneousVideoFrontVideoStabilizationSupported"
+ "TB,R,N,GisFrontRearSimultaneousVideoMirrored,V_frontRearSimultaneousVideoMirrored"
+ "TB,R,N,GisFrontRearSimultaneousVideoSupported,V_frontRearSimultaneousVideoSupported"
+ "TB,R,N,GisSecondaryDeviceVideoBinned"
+ "TB,R,N,GisSmartFramingSupported,V_smartFramingSupported"
+ "TB,R,N,GisSmartFramingUsingDynamicAspectRatioSupported,V_smartFramingUsingDynamicAspectRatioSupported"
+ "TB,R,N,V__HDR10BitVideoSupports240FPS"
+ "TB,R,N,V__configureForSecondaryDevice"
+ "TB,R,N,V__configureSecondaryDevice"
+ "TB,R,N,V__debugColorDuplicatedMovieFileBuffers"
+ "TB,R,N,V__debugDisableMotionBlur"
+ "TB,R,N,V__dynamicAspectRatioInCinematicModeSupported"
+ "TB,R,N,V__dynamicAspectRatioInVideoModeSupported"
+ "TB,R,N,V__frontRearSimultaneousVideoEnabled"
+ "TB,R,N,V__preserveFrontRearSimultaneousVideoEnabled"
+ "TB,R,N,V__resetSecondaryDevice"
+ "TB,R,N,V__useCoreImageCVTextureCache"
+ "TB,R,N,V__useCoreImageSurfacePool"
+ "TB,R,N,V_alwaysShowFrontPIPIndicator"
+ "TB,R,N,V_dynamicAspectRatioSupported"
+ "TB,R,N,V_frontRearSimultaneousVideoEnabled"
+ "TB,R,N,V_useMultiCamSession"
+ "T^{CGColor=},R,N,V_borderColor"
+ "T^{__CVMetalTextureCache=},N,V__textureCache"
+ "Td,N,V__frontPIPVideoPreviewRenderedCornerRadius"
+ "Td,R,N,V__pipMaxBlurRadius"
+ "Td,R,N,V_borderWidth"
+ "Td,R,N,V_cornerRadius"
+ "Td,R,N,V_quadraTeleDisplayZoomFactor"
+ "Td,R,N,V_quadraTeleRelativeZoomFactor"
+ "Td,R,N,V_smartFramingFieldOfViewLandscapeZoomFactor"
+ "Td,R,N,V_smartFramingFieldOfViewPortraitZoomFactor"
+ "Td,R,N,V_smartFramingFieldOfViewZoomedOutLandscapeZoomFactor"
+ "Td,R,N,V_smartFramingFieldOfViewZoomedOutPortraitZoomFactor"
+ "Ti,N,V__pipRotationAngle"
+ "Top Over-Capture Gradient Enabled"
+ "Tq,N,V__desiredFieldOfView"
+ "Tq,N,V__smartFramingFieldOfViewSource"
+ "Tq,N,V_frontPIPAnchor"
+ "Tq,N,V_smartFramingFieldOfView"
+ "Tq,R,N,V__pipMetricsMaxCapacity"
+ "Tq,R,N,V__smartFramingFieldOfView"
+ "Tq,R,N,V__videoDynamicAspectRatio"
+ "Tq,R,N,V_backQuadraTeleFocalLengthDisplayValue"
+ "Tq,R,N,V_smartFramingFieldOfView"
+ "Tq,R,N,V_videoDynamicAspectRatio"
+ "Tq,R,N,V_videoResolution"
+ "T{?=qiIq},N,V__debugLastCompositedMovieFilePrimaryBufferPTS"
+ "T{?=qiIq},N,V__debugLastCompositedMovieFileSecondaryBufferPTS"
+ "T{?=qiIq},N,V__mostRecentlyAddedPIPMetricsTimestamp"
+ "T{?=qiIq},R,N,V_timestamp"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V__lastCompositedPictureInPictureFrameForMotionBlur"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_frame"
+ "Unsupported dynamic aspect ratio for secondary device: %{public}@"
+ "Unsupported dynamic aspect ratio: %{public}@"
+ "Updating overrideSmartFramingAutoRotateInLandscapeEnabled to: %d"
+ "Updating overrideSmartFramingAutoZoomInLandscapeEnabled to: %d"
+ "Updating smartFramingAutoRotationEnabled to: %d"
+ "Updating smartFramingAutoZoomEnabled to: %d"
+ "Updating wantsSmartFramingAutoRotationDefault to: %d"
+ "Updating wantsSmartFramingAutoZoomDefault to: %d"
+ "Using auto smart framing recommendation, updating to: %ld"
+ "^{__CVMetalTextureCache=}"
+ "^{__CVMetalTextureCache=}16@0:8"
+ "_%dfpsOverride"
+ "_HDR10BitVideoSupports240FPS"
+ "__HDR10BitVideoSupports240FPS"
+ "__cachedDynamicAspectRatioFormat"
+ "__ciContext"
+ "__compositingSessionActive"
+ "__configureForSecondaryDevice"
+ "__configureSecondaryDevice"
+ "__debugColorDuplicatedMovieFileBuffers"
+ "__debugDisableMotionBlur"
+ "__debugLastCompositedMovieFilePrimaryBufferPTS"
+ "__debugLastCompositedMovieFileSecondaryBufferPTS"
+ "__delaySmartFramingDynamicAspectRatioUpdate"
+ "__desiredFieldOfView"
+ "__dynamicAspectRatioInCinematicModeSupported"
+ "__dynamicAspectRatioInVideoModeSupported"
+ "__excessiveBlurRadiusReported"
+ "__frontPIPVideoPreviewAnimationSpringSettings"
+ "__frontPIPVideoPreviewCenterAnimatableProperty"
+ "__frontPIPVideoPreviewCenterAnimationResetsFocusAndExposure"
+ "__frontPIPVideoPreviewPanGestureRecognizer"
+ "__frontPIPVideoPreviewRenderedCornerRadius"
+ "__frontRearSimultaneousVideoEnabled"
+ "__gainMapCIContext"
+ "__lastCompositedPictureInPictureFrameForMotionBlur"
+ "__metalDevice"
+ "__mostRecentlyAddedPIPMetricsTimestamp"
+ "__motionBlurDisabledForCurrentCompositingSession"
+ "__multiCamPIPCompositingQueue"
+ "__multiCamPIPCompositingQueue_multiCamPIPCompositor"
+ "__overrideSmartFramingAutoRotateInLandscapeEnabled"
+ "__overrideSmartFramingAutoZoomInLandscapeEnabled"
+ "__pipMaxBlurRadius"
+ "__pipMetricsByTimestamp"
+ "__pipMetricsMaxCapacity"
+ "__pipRotationAngle"
+ "__pipTimestampTooOldReported"
+ "__preserveFrontRearSimultaneousVideoEnabled"
+ "__resetSecondaryDevice"
+ "__secondaryVideoPreviewLayer"
+ "__smartFramingAutoRotationEnabled"
+ "__smartFramingAutoZoomEnabled"
+ "__smartFramingEnabledFieldsOfView"
+ "__smartFramingFieldOfView"
+ "__smartFramingFieldOfViewSource"
+ "__surfaceMemoryPool"
+ "__textureCache"
+ "__useCoreImageCVTextureCache"
+ "__useCoreImageSurfacePool"
+ "__useSmartFramingTransition"
+ "__videoDynamicAspectRatio"
+ "__wantsFlipAspectRatio"
+ "__wantsSmartFramingAutoRotationDefault"
+ "__wantsSmartFramingAutoZoomDefault"
+ "__zoomButtonPlatterOffsetAnimator"
+ "_alwaysShowFrontPIPIndicator"
+ "_animateFrontPIPToCenter:animationUpdateMode:resetFocusAndExposure:"
+ "_applyMaskAndBorderToImage:cornerRadius:borderWidth:borderColor:"
+ "_autoFramingIndicator"
+ "_autoSmartFramingEnabled"
+ "_autoSmartFramingSupported"
+ "_autoSmartFramingSupportedSmartFramingFieldOfViewsForGraphConfiguration:"
+ "_backQuadraTeleFocalLengthDisplayValue"
+ "_backQuadraTeleSupported"
+ "_borderColor"
+ "_borderWidth"
+ "_cachedDynamicAspectRatioFormat"
+ "_calculateMotionBlurAngle:motionBlurRadius:forPictureInPictureFrame:fromPictureInPictureFrame:"
+ "_calculateVerticalOffsetFromZoomPlatterToFrame:fromView:"
+ "_captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:resolvedDevice:"
+ "_ciContext"
+ "_commandForResetFocus:resetExposure:resetExposureTargetBias:resetSecondaryDevice:"
+ "_compareCGPointsToAccuracy:point1:point2:"
+ "_compositePrimaryGainMapImage:pipGainMapImage:primarySDRImage:pipSDRImage:compositeSDRImage:pipFrame:pipCornerRadius:pipBorderWidth:pipBorderColor:mirrorPIP:captureOrientation:"
+ "_compositePrimaryImage:pipImage:pipFrame:pipCornerRadius:pipBorderWidth:pipBorderColor:mirrorPIP:captureOrientation:motionBlurAngle:motionBlurRadius:debugColorDuplicatedPrimaryImage:debugColorDuplicatedPIPImage:"
+ "_compositingSessionActive"
+ "_configureForSecondaryDevice"
+ "_configureSecondaryDevice"
+ "_cornerRadius"
+ "_createFrontPIPVideoPreviewViewPanGestureRecognizerIfNecessary"
+ "_cropPIP:toSizeAspectRatioIfNecessary:"
+ "_currentSecondaryVideoDevice"
+ "_currentSecondaryVideoDeviceFormat"
+ "_currentSecondaryVideoDeviceInput"
+ "_currentSecondaryVideoPreviewLayer"
+ "_debugColorDuplicatedMovieFileBuffers"
+ "_debugDisableMotionBlur"
+ "_debugImageWithDuplicatedColorTint:"
+ "_debugLastCompositedMovieFilePrimaryBufferPTS"
+ "_debugLastCompositedMovieFileSecondaryBufferPTS"
+ "_defaultSmartFramingFieldOfViewForOrientation:"
+ "_delaySmartFramingDynamicAspectRatioUpdate"
+ "_desiredFieldOfView"
+ "_desiredSecondaryInputsWithCaptureEngineSecondaryDevice:"
+ "_deviceFormatForDynamicAspectRatioWithGraphConfiguration:deviceIsSecondary:"
+ "_didRecentlyUseFrontPIP"
+ "_disableAutoSmartFramingIfSupported"
+ "_dynamicAspectRatio"
+ "_dynamicAspectRatioInCinematicModeSupported"
+ "_dynamicAspectRatioInVideoModeSupported"
+ "_dynamicAspectRatioSupported"
+ "_enabledSmartFramingsFromSupportedFieldOfViews:"
+ "_excessiveBlurRadiusReported"
+ "_executeForCurrentDeviceWithContext:"
+ "_executeForSecondaryDeviceWithContext:"
+ "_existingVideoPreviewLayersWithContext:without:"
+ "_fallbackVideoConfigurationForUnsupportedConfiguration:frontRearSimultaneousVideoEnabled:"
+ "_flipAspectRatioButton"
+ "_flipAspectRatioButtonVisible"
+ "_frame"
+ "_frontPIPAnchor"
+ "_frontPIPButton"
+ "_frontPIPButtonFrame"
+ "_frontPIPButtonVisible"
+ "_frontPIPFrame"
+ "_frontPIPVideoPreviewAnimationSpringSettings"
+ "_frontPIPVideoPreviewCenterAnimatableProperty"
+ "_frontPIPVideoPreviewCenterAnimationResetsFocusAndExposure"
+ "_frontPIPVideoPreviewPanGestureRecognizer"
+ "_frontPIPVideoPreviewRenderedCornerRadius"
+ "_frontPIPVideoPreviewView"
+ "_frontRearSimultaneousCaptureEnabled"
+ "_frontRearSimultaneousCaptureMirrored"
+ "_frontRearSimultaneousVideo60FPSSupported"
+ "_frontRearSimultaneousVideoDeferredFrontCameraEnabled"
+ "_frontRearSimultaneousVideoEnabled"
+ "_frontRearSimultaneousVideoFrontCameraHDR10Supported"
+ "_frontRearSimultaneousVideoFrontVideoStabilizationSupported"
+ "_frontRearSimultaneousVideoMirrored"
+ "_frontRearSimultaneousVideoSupported"
+ "_gainMapCIContext"
+ "_handleFlipAspectRatioButtonTapped:"
+ "_handleFrontPIPButtonTapped:"
+ "_handleFrontPIPVideoPreviewViewPan:"
+ "_handleFrontPIPVideoPreviewViewPanDidEndAtPosition:withVelocity:inView:timestamp:"
+ "_handleFrontPIPVideoPreviewViewPanDidMoveWithTranslation:withGesture:inView:timestamp:"
+ "_hideFrontPIPVideoPreviewView"
+ "_isCompositingSessionActive"
+ "_isFrontPIPAtAnAnchor"
+ "_isFrontPIPEnabled"
+ "_isFrontPIPSupported"
+ "_isFrontRearSimultaneousVideoActiveForMode:devicePosition:"
+ "_isFrontRearSimultaneousVideoEnabled"
+ "_isFrontRearSimultaneousVideoSupportedForMode:devicePosition:"
+ "_isSmartFramingAutoRotationSupported"
+ "_isSmartFramingAutoZoomSupported"
+ "_isSmartFramingFieldOfView:equalToAVCaptureSmartFraming:"
+ "_lastCompositedPictureInPictureFrameForMotionBlur"
+ "_layoutViewportWithFrame:previewFrame:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:"
+ "_metalDevice"
+ "_mostRecentlyAddedPIPMetricsTimestamp"
+ "_motionBlurDisabled"
+ "_motionBlurDisabledForCurrentCompositingSession"
+ "_multiCamPIPCompositingQueue"
+ "_multiCamPIPCompositingQueue_multiCamPIPCompositor"
+ "_offsetZoomButtonForFlipAspectRatioButton"
+ "_overrideSmartFramingAutoRotateInLandscapeEnabled"
+ "_overrideSmartFramingAutoZoomInLandscapeEnabled"
+ "_performGraphConfigurationChangeForFrontRearSimultaneousVideoEnabledChange"
+ "_pipAnchorPointForPIPSize:"
+ "_pipFrameEqualsMostRecentlyAdded:"
+ "_pipMaxBlurRadius"
+ "_pipMetricsByTimestamp"
+ "_pipMetricsForCompositingClosestToTimestamp:"
+ "_pipMetricsMaxCapacity"
+ "_pipRotationAngle"
+ "_pipTimestampTooOldReported"
+ "_preserveFrontRearSimultaneousVideoEnabled"
+ "_quadraTeleDisplayZoomFactor"
+ "_quadraTeleRelativeZoomFactor"
+ "_recommendedSmartFramingChangedForKeyPath:ofObject:change:"
+ "_recommendedSmartFramingDelegate"
+ "_resetDynamicAspectRatio"
+ "_resetFocusAndExposureIfFrontPIPObscuresIndicator"
+ "_resetSecondaryDevice"
+ "_resetSmartFramingFieldOfViewAnimated:"
+ "_resolvedFlipAspectRatioForMode:videoConfiguration:devicePosition:trueVideoEnabled:"
+ "_resolvedSmartFramingAutoRotationEnabled"
+ "_resolvedSmartFramingAutoZoomEnabled"
+ "_resolvedSmartFramingFieldOfViewForMode:devicePosition:"
+ "_scaledPIPMetrics:toPrimaryImageSize:"
+ "_secondaryEngineDeviceWithContext:graphConfiguration:resolvedDevice:"
+ "_secondaryInputsBecomingPrimaryWithContext:desiredPrimaryInputs:"
+ "_secondaryVideoDeviceInputFromSession:"
+ "_secondaryVideoPreviewLayer"
+ "_setFlipAspectRatioButton:"
+ "_setFrontPIPButton:"
+ "_setFrontRearSimultaneousVideoEnabled:"
+ "_setOverrideSmartFramingAutoRotateInLandscapeEnabled:"
+ "_setOverrideSmartFramingAutoZoomInLandscapeEnabled:"
+ "_setSmartFramingAutoRotationEnabled:"
+ "_setSmartFramingAutoZoomEnabled:"
+ "_setWantsSmartFramingAutoRotationDefault:"
+ "_setWantsSmartFramingAutoZoomDefault:"
+ "_setupRecommendedSmartFramingMonitoring"
+ "_shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:"
+ "_shouldEnableFrontRearSimultaneousVideo"
+ "_shouldShowFlipAspectRatioButtonForGraphConfiguration:"
+ "_shouldShowFrontPIPButtonForGraphConfiguration:"
+ "_shouldShowSmartFramingAutoRotationForGraphConfiguration:"
+ "_shouldShowSmartFramingAutoZoomForGraphConfiguration:"
+ "_showFrontPIPIndicator"
+ "_showSmartFramingAutoBadgeForSmartFramingFieldOfView:previousSmartFramingFieldOfView:"
+ "_smartFramingAutoRotationEnabled"
+ "_smartFramingAutoRotationMonitoringEnabled"
+ "_smartFramingAutoZoomEnabled"
+ "_smartFramingEnabledFieldsOfView"
+ "_smartFramingFieldOfView"
+ "_smartFramingFieldOfViewLandscapeZoomFactor"
+ "_smartFramingFieldOfViewPortraitZoomFactor"
+ "_smartFramingFieldOfViewSource"
+ "_smartFramingFieldOfViewZoomedOutLandscapeZoomFactor"
+ "_smartFramingFieldOfViewZoomedOutPortraitZoomFactor"
+ "_smartFramingForSmartFramingFieldOfView:supportedFieldOfViews:"
+ "_smartFramingSupported"
+ "_smartFramingSupportsAspectRatioCrop:"
+ "_smartFramingUsingDynamicAspectRatioSupported"
+ "_sortedPIPTimestamps"
+ "_specificFramerateCommandForGraphConfiguration:withContext:configureSecondaryDevice:"
+ "_surfaceMemoryPool"
+ "_teardownRecommendedSmartFramingMonitoring"
+ "_textureCache"
+ "_timestamp"
+ "_toggleZoomForSmartFramingFieldOfView:"
+ "_updateCaptureControllerWithFrontPIPFrameRelativeToViewport:cornerRadius:timestamp:"
+ "_updateFlipAspectRatioButtonForGraphConfiguration:animated:"
+ "_updateFrontPIPButtonActiveState"
+ "_updateFrontRearSimultaneousVideoEnabled:"
+ "_updateFrontRearSimultaneousVideoEnabledForGraphConfiguration:"
+ "_updatePreviewLayerForPreviewFrame:viewportFrame:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:"
+ "_updateSmartFramingDynamicAspectRatioAndZoomWithRampDuration:zoomRampTuning:"
+ "_updateSmartFramingFieldOfViewForGraphConfiguration:animated:"
+ "_updateSmartFramingFieldOfViewForGraphConfiguration:rampDuration:zoomRampTuning:animated:"
+ "_updateSmartFramingForCaptureOrientation:rampDuration:zoomRampTuning:animated:"
+ "_updateSmartFramingMonitorForGraphConfiguration:"
+ "_updateSmartFramingOverCaptureGradientHeightForGraphConfiguration:animated:"
+ "_useCoreImageCVTextureCache"
+ "_useCoreImageSurfacePool"
+ "_useMultiCamSession"
+ "_useSmartFramingTransition"
+ "_videoDynamicAspectRatio"
+ "_wantsFlipAspectRatio"
+ "_wantsSmartFramingAutoRotationDefault"
+ "_wantsSmartFramingAutoZoomDefault"
+ "_zoomButtonPlatterOffsetAnimator"
+ "_zoomSymbols"
+ "alwaysShowFrontPIPIndicator"
+ "applyWithForeground:background:"
+ "autoFramingIndicator"
+ "autoSmartFramingSupported"
+ "backQuadraTeleFocalLengthDisplayValue"
+ "backQuadraTeleSupported"
+ "borderColor"
+ "bottomOverCaptureGradientEnabled"
+ "bundleURL"
+ "cam_addConnectionWithMediaType:fromDeviceInput:toOutput:"
+ "cam_connectionWithMediaType:fromDeviceInput:toOutput:"
+ "cam_ensureConnections:"
+ "cam_ensureVideoPreviewLayers:withConnections:whileRemoving:"
+ "cam_frontFacingFormatForVideoConfiguration:videoEncodingBehavior:colorSpace:dynamicAspectRatio:useSquareFormat:requireVideoBinned:"
+ "cam_supportsFrontFacingFormatForVideoConfiguration:colorSpace:enableProResVideo:dynamicAspectRatio:useSquareFormat:requireVideoBinned:"
+ "captureController:didOutputRecommendedSmartFramingFieldOfView:"
+ "captureOutput:readyForClientCompositingForOutputFileAtURL:compositingData:"
+ "captureOutput:readyForClientCompositingForOutputFileAtURL:primaryPixelBuffer:primaryPTS:secondaryPixelBuffer:secondaryPTS:outputPixelBuffer:compositeMetadata:"
+ "captureOutput:readyForClientCompositingForResolvedSettings:compositingData:"
+ "changeToSmartFramingFieldOfView:mode:videoConfiguration:devicePosition:"
+ "colorMonochromeFilter"
+ "colorWithRed:green:blue:colorSpace:"
+ "com.apple.camera.capture-engine.multicam-pip-compositing-queue"
+ "compositeWithCompositingData:strategy:captureOrientation:mirrorPIP:"
+ "contextWithMTLDevice:options:"
+ "convertPoint:toCoordinateSpace:"
+ "cornerRadiusForContainerWidth:"
+ "currentCameraDevice.smartFramingMonitor.recommendedSmartFraming"
+ "currentSecondaryVideoDevice"
+ "currentSecondaryVideoDeviceFormat"
+ "currentSecondaryVideoDeviceInput"
+ "currentSecondaryVideoPreviewLayer"
+ "d104@0:8q16q24q32q40q48q56q64B72B76B80B84q88^B96"
+ "d56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48"
+ "d60@0:8d16q24q32q40q48B56"
+ "defaultAnchor"
+ "defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:isTrueVideo:frontRearSimultaneousVideoEnabled:prefersHDR10BitVideo:smartFramingFieldOfView:overrodeWithForcedZoomValue:"
+ "deviceFormatForSessionPreset:device:"
+ "didRecentlyUseFrontPIP"
+ "dynamicAspectRatioSupported"
+ "ensureMemory:"
+ "exifFocalLengthsByZoomFactorForMode:device:videoConfiguration:videoStabilizationStrength:customLensGroup:isTrueVideo:frontRearSimultaneousVideoEnabled:"
+ "fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:macroMode:"
+ "flipAspectRatioButton"
+ "flipAspectRatioButtonVisible"
+ "floatAnimatablePropertyWithInitialValue:cancelableFrameCallback:"
+ "flush:"
+ "frameInCoreImageLandscapeCoordinateSpace"
+ "frontPIPAnchor"
+ "frontPIPButton"
+ "frontPIPButtonVisible"
+ "frontPIPFrameDidChange:"
+ "frontPIPVideoPreviewLayer"
+ "frontPIPVideoPreviewView"
+ "frontPIPWillAnimateToPosition:withFrame:"
+ "frontRearSimultaneousCaptureEnabled"
+ "frontRearSimultaneousCaptureMirrored"
+ "frontRearSimultaneousVideo60FPSSupported"
+ "frontRearSimultaneousVideoDeferredFrontCameraEnabled"
+ "frontRearSimultaneousVideoEnabled"
+ "frontRearSimultaneousVideoFrontCameraHDR10Supported"
+ "frontRearSimultaneousVideoFrontVideoStabilizationSupported"
+ "frontRearSimultaneousVideoMirrored"
+ "frontRearSimultaneousVideoSupported"
+ "frontRearVideoEnabled"
+ "frsv.disableDeferFrontCamera"
+ "fullScreenViewfinderDidCreateFlipAspectRatioButton:"
+ "fullScreenViewfinderDidCreateFrontPIPButton:"
+ "futureThrowTime"
+ "gainMapImageForSDR:HDR:colorSpace:rgbGainmap:"
+ "handleUserChangedFlippedAspectRatioEnabled:"
+ "handleUserChangedFrontPIPEnabled:"
+ "handleUserChangedSmartFramingAutoRotationEnabled:"
+ "handleUserChangedSmartFramingAutoZoomEnabled:"
+ "iPhone18,1"
+ "iPhone18,2"
+ "iPhone18,3"
+ "iPhone18,4"
+ "imageByApplyingCGOrientation:"
+ "imageByApplyingGainMap:"
+ "imageByApplyingTransform:highQualityDownsample:"
+ "imageByCompositingOverImage:"
+ "imageByCroppingToRect:"
+ "initForSecondaryDevice"
+ "initWithAutoFPSVideoEnabled:configureSecondaryDevice:"
+ "initWithAutomaticVideoStabilizationEnabled:strength:frontRearSimultaneousVideoEnabled:configureSecondaryDevice:"
+ "initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:mixAudioWithOthers:windNoiseRemovalEnabled:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:smartStyles:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:videoBinned:enableDepthSuggestion:enableZoomPIP:customLensGroup:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:videoDynamicAspectRatio:smartFramingFieldOfView:"
+ "initWithExposureMode:atPointOfInterest:configureSecondaryDevice:"
+ "initWithExposureTargetBias:configureSecondaryDevice:"
+ "initWithFocusMode:atPointOfInterest:rectSize:smooth:configureSecondaryDevice:"
+ "initWithFrontRearSimultaneousCaptureEnabled:"
+ "initWithPictureInPictureRotationAngle:"
+ "initWithPixelBuffer:"
+ "initWithProperties:"
+ "initWithSmartFramingEnabledFieldOfViews:"
+ "initWithSmartFramingFieldOfView:videoDynamicAspectRatio:mode:videoConfiguration:devicePosition:"
+ "initWithSmartFramingFieldOfView:videoDynamicAspectRatio:mode:videoConfiguration:devicePosition:configureForSecondaryDevice:"
+ "initWithSmartFramingMonitorEnabled:"
+ "initWithSubjectAreaChangeMonitoringEnabled:configureSecondaryDevice:"
+ "initWithTimestamp:frame:cornerRadius:borderWidth:borderColor:videoResolution:"
+ "initWithVideoConfiguration:configureSecondaryDevice:"
+ "initWithWhiteBalanceMode:configureSecondaryDevice:"
+ "input"
+ "iphone.landscape"
+ "isActionModeControlSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:"
+ "isAutoSmartFramingSupported"
+ "isBackQuadraTeleSupported"
+ "isDynamicAspectRatioSupportedForMode:devicePosition:"
+ "isDynamicAspectRatioSupportedForMode:videoConfiguration:devicePosition:"
+ "isEnhancedStabilizationSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:"
+ "isFlipAspectRatioButtonVisible"
+ "isFrontRearSimultaneousCaptureEnabled"
+ "isFrontRearSimultaneousCaptureMirrored"
+ "isFrontRearSimultaneousVideo60FPSSupported"
+ "isFrontRearSimultaneousVideoDeferredFrontCameraEnabled"
+ "isFrontRearSimultaneousVideoEnabled"
+ "isFrontRearSimultaneousVideoFrontCameraHDR10Supported"
+ "isFrontRearSimultaneousVideoFrontVideoStabilizationSupported"
+ "isFrontRearSimultaneousVideoMirrored"
+ "isFrontRearSimultaneousVideoSupported"
+ "isFrontRearSimultaneousVideoSupportedForMode:"
+ "isFrontRearSimultaneousVideoSupportedForMode:devicePosition:"
+ "isFrontRearSimultaneousVideoSupportedForVideoConfiguration:"
+ "isLensPositionControlSupportedForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:"
+ "isMonitoring"
+ "isMotionBlurDisabled"
+ "isMultiCamClientCompositingSupported"
+ "isQuadraTeleBinningReconfigurationSupportedForMode:devicePosition:videoConfiguration:"
+ "isQuadraTeleZoomButtonSupportedForMode:devicePosition:videoConfiguration:"
+ "isSecondaryDeviceVideoBinned"
+ "isSmartFramingSupported"
+ "isSmartFramingSupportedForMode:devicePosition:"
+ "isSmartFramingUsingDynamicAspectRatioSupported"
+ "isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:"
+ "isSupportedVideoConfiguration:forMode:device:trueVideoEnabled:frontRearSimultaneousVideoEnabled:"
+ "isTripleCameraSupportedForMode:devicePosition:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:"
+ "isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:trueVideoEnabled:prefersHDR10BitVideo:frontRearSimultaneousVideoEnabled:"
+ "isVideoStabilizationStrength:supportedForMode:devicePosition:trueVideoEnabled:frontRearSimultaneousVideoEnabled:"
+ "isZoomPIPSupportedForMode:devicePosition:frontRearSimultaneousVideoEnabled:"
+ "loadArchiveWithName:fromURL:"
+ "motionBlurDisabled"
+ "motionBlurFilter"
+ "numberWithUnsignedLongLong:"
+ "offsetZoomButtonForFlipAspectRatioButton"
+ "outputGainMapSampleBuffer"
+ "outputSampleBuffer"
+ "person.crop.rectangle.landscape.rotate"
+ "person.crop.rectangle.portrait.rotate"
+ "person.fill.viewfinder"
+ "pip"
+ "pipInsetForViewportSize:"
+ "pipOutsetForViewportSize:"
+ "poolId"
+ "populateZoomFieldOfView:graphConfiguration:smartFramingSource:"
+ "preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:"
+ "prepareForCompositing"
+ "presentationValue"
+ "primaryGainMapImage"
+ "primaryImage"
+ "primarySampleBuffer"
+ "primaryVideoPreviewLayerForGraphConfiguration:"
+ "properties"
+ "q24@0:8^B16"
+ "q48@0:8q16q24q32B40B44"
+ "q52@0:8q16q24q32q40B48"
+ "q60@0:8q16q24q32q40B48q52"
+ "q80@0:8q16q24q32q40q48{?=qq}56B72B76"
+ "quadraTeleDisplayZoomFactor"
+ "quadraTeleRelativeZoomFactor"
+ "recommendedSmartFramingDelegate"
+ "resetCompositingState:"
+ "resolveDesiredMacroMode:forMode:device:videoConfiguration:videoStabilizationStrength:photoFormat:optionalDepthEffectEnabled:frontRearSimultaneousVideoEnabled:"
+ "resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:"
+ "roundedRectangleGeneratorFilter"
+ "roundedRectangleStrokeGeneratorFilter"
+ "sanitizeVideoConfigurationForDesiredConfiguration:mode:device:trueVideoEnabled:frontRearSimultaneousVideoEnabled:"
+ "secondaryDevice:"
+ "secondaryDeviceColorSpace"
+ "secondaryDeviceUsesPrimaryVideoConfigurationForFrameRate"
+ "secondaryDeviceVideoBinned"
+ "secondaryDeviceVideoConfiguration"
+ "secondaryDeviceVideoDynamicAspectRatio"
+ "secondaryDeviceVideoStabilizationStrength"
+ "secondaryGainMapImage"
+ "secondaryImage"
+ "secondarySampleBuffer"
+ "secondaryVideoPreviewLayer"
+ "secondaryVideoPreviewLayerForGraphConfiguration:"
+ "setAutoSmartFramingEnabled:"
+ "setAutoSmartFramingEnabledFieldOfViews:"
+ "setBottomOverCaptureGradientEnabled:"
+ "setCompositingMetadata:"
+ "setCurrentSecondaryVideoDevice:"
+ "setCurrentSecondaryVideoDeviceFormat:"
+ "setCurrentSecondaryVideoDeviceInput:"
+ "setCurrentSecondaryVideoPreviewLayer:"
+ "setDefaultValues"
+ "setDidRecentlyUseFrontPIP"
+ "setDidRecentlyUseFrontPIP:"
+ "setDynamicAspectRatio:completionHandler:"
+ "setEnabledSmartFramings:"
+ "setExtent:"
+ "setFlipAspectRatioButtonVisible:"
+ "setFlipAspectRatioButtonVisible:animated:"
+ "setFrontPIPAnchor:"
+ "setFrontPIPButtonVisible:"
+ "setFrontPIPButtonVisible:animated:"
+ "setFrontPIPFrame:"
+ "setFrontPIPVideoPreviewLayer:"
+ "setFrontRearSimultaneousCaptureEnabled:"
+ "setFrontRearSimultaneousCaptureMirrored:"
+ "setFrontRearSimultaneousVideoEnabled:"
+ "setFrontRearSimultaneousVideoMirrored:"
+ "setInputImage:"
+ "setIntensity:"
+ "setIsFrontPIPSupported:"
+ "setIsSmartFramingAutoRotationSupported:"
+ "setIsSmartFramingAutoZoomSupported:"
+ "setMotionBlurDisabled:"
+ "setMultiCamClientCompositingEnabled:"
+ "setMultiCamClientCompositingPrimaryConnection:secondaryConnection:"
+ "setMultiCamPictureInPictureMetrics:"
+ "setMultiCamPictureInPictureMotionBlurDisabled:"
+ "setOffsetZoomButtonForFlipAspectRatioButton:"
+ "setOffsetZoomButtonForFlipAspectRatioButton:animated:"
+ "setOverrideSmartFramingAutoRotateInLandscapeEnabled:"
+ "setOverrideSmartFramingAutoZoomInLandscapeEnabled:"
+ "setPictureInPictureMetrics:"
+ "setPrimaryCaptureRectAspectRatio:centerPoint:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:"
+ "setRadius:"
+ "setRecommendedSmartFramingDelegate:"
+ "setSessionWithNoConnection:"
+ "setShouldEnableFrontRearSimultaneousVideo:"
+ "setShowFrontPIPIndicator:"
+ "setSmartFramingAutoRotationEnabled:"
+ "setSmartFramingAutoZoomEnabled:"
+ "setSmartFramingFieldOfView:"
+ "setSmartFramingFieldOfView:useTransition:animated:"
+ "setSmartFramingMonitorEnabled:"
+ "setSmoothness:"
+ "setTopOverCaptureGradientEnabled:"
+ "setTranslation:inView:"
+ "setWantsSmartFramingAutoRotationDefault:"
+ "setWantsSmartFramingAutoZoomDefault:"
+ "setZoomSymbols:"
+ "setZoomSymbols:animated:"
+ "set_ciContext:"
+ "set_commandQueue:"
+ "set_compositingSessionActive:"
+ "set_debugLastCompositedMovieFilePrimaryBufferPTS:"
+ "set_debugLastCompositedMovieFileSecondaryBufferPTS:"
+ "set_delaySmartFramingDynamicAspectRatioUpdate:"
+ "set_desiredFieldOfView:"
+ "set_excessiveBlurRadiusReported:"
+ "set_frontPIPVideoPreviewCenterAnimatableProperty:"
+ "set_frontPIPVideoPreviewCenterAnimationResetsFocusAndExposure:"
+ "set_frontPIPVideoPreviewRenderedCornerRadius:"
+ "set_gainMapCIContext:"
+ "set_lastCompositedPictureInPictureFrameForMotionBlur:"
+ "set_metalDevice:"
+ "set_mostRecentlyAddedPIPMetricsTimestamp:"
+ "set_motionBlurDisabledForCurrentCompositingSession:"
+ "set_multiCamPIPCompositingQueue_multiCamPIPCompositor:"
+ "set_pipRotationAngle:"
+ "set_pipTimestampTooOldReported:"
+ "set_smartFramingFieldOfViewSource:"
+ "set_surfaceMemoryPool:"
+ "set_textureCache:"
+ "set_useSmartFramingTransition:"
+ "set_wantsFlipAspectRatio:"
+ "set_zoomButtonPlatterOffsetAnimator:"
+ "shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:"
+ "shouldApplyContinuousZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:zoomFactors:displayZoomFactors:"
+ "shouldDisablePIPMotionBlur"
+ "shouldEmulateTripleCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:"
+ "shouldEmulateWideDualCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:"
+ "shouldEnableFrontRearSimultaneousVideo"
+ "sizeForViewportSize:"
+ "smartFramingAutoRotation"
+ "smartFramingAutoZoom"
+ "smartFramingFieldOfView"
+ "smartFramingFieldOfViewLandscapeZoomFactor"
+ "smartFramingFieldOfViewPortraitZoomFactor"
+ "smartFramingFieldOfViewZoomedOutLandscapeZoomFactor"
+ "smartFramingFieldOfViewZoomedOutPortraitZoomFactor"
+ "smartFramingMonitor"
+ "smartFramingSource"
+ "smartFramingSupported"
+ "smartFramingUsingDynamicAspectRatioSupported"
+ "smoothness"
+ "sourceIn"
+ "startMonitoring:"
+ "startTaskToRender:toDestination:error:"
+ "stopMonitoring"
+ "supportedDynamicAspectRatios"
+ "supportedSmartFramings"
+ "timeStampInSeconds"
+ "topOverCaptureGradientEnabled"
+ "updateForSmartFramingAutoFramingDidZoom:didRotate:"
+ "updateForSmartFramingAutoRotation:"
+ "updateForSmartFramingAutoZoom:"
+ "updateForSmartFramingDisabled"
+ "useMultiCamSession"
+ "useSquareFormatForDynamicAspectRatioForMode:videoConfiguration:"
+ "v112@0:8@\"AVCaptureFileOutput\"16@\"NSURL\"24^{__CVBuffer=}32{?=qiIq}40^{__CVBuffer=}64{?=qiIq}72^{__CVBuffer=}96^@104"
+ "v112@0:8@16@24^{__CVBuffer=}32{?=qiIq}40^{__CVBuffer=}64{?=qiIq}72^{__CVBuffer=}96^@104"
+ "v24@0:8^{__CVMetalTextureCache=}16"
+ "v32@?0@\"AVCaptureSmartFraming\"8Q16^B24"
+ "v32@?0@\"AVCaptureVideoPreviewLayer\"8Q16^B24"
+ "v40@0:8@\"AVCaptureFileOutput\"16@\"NSURL\"24@\"AVCaptureMultiCamClientCompositingData\"32"
+ "v40@0:8q16@24q32"
+ "v40@0:8{?=qiIq}16"
+ "v44@0:8@16d24q32B40"
+ "v44@0:8@16q24q32B40"
+ "v44@0:8q16d24q32B40"
+ "v56@0:8q16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "v72@0:8{CGPoint=dd}16@32@40{?=qiIq}48"
+ "v80@0:8{CGPoint=dd}16{CGPoint=dd}32@48{?=qiIq}56"
+ "v80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16d48{?=qiIq}56"
+ "v96@0:8^f16^f24{CGRect={CGPoint=dd}{CGSize=dd}}32{CGRect={CGPoint=dd}{CGSize=dd}}64"
+ "v96@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48d80d88"
+ "vector2DAnimatablePropertyWithInitialValue:cancelableFrameCallback:"
+ "velocityInView:"
+ "videoConfiguration=%lu, encoding=%lu, colorSpace=%lu, videoDynamicAspectRatio=%lu useSquareFormat=%d requireVideoBinned=%d"
+ "videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:resolvedDevice:"
+ "videoDeviceFormatForGraphConfiguration:captureSession:deviceIsSecondary:"
+ "videoDynamicAspectRatio"
+ "videoResolution"
+ "viewportAnchorsForFrontPIP"
+ "viewportAnchorsForFrontPIPOriginWithSize:"
+ "wantsSmartFramingAutoRotationDefault"
+ "wantsSmartFramingAutoZoomDefault"
+ "zoomControlDisplayValueForZoomFactor:mode:device:videoConfiguration:videoStabilizationStrength:frontRearSimultaneousVideoEnabled:"
+ "zoomFactorForSmartFramingFieldOfView:"
+ "zoomSymbols"
+ "{?=ii}28@0:8q16B24"
+ "{?={CGPoint=dd}{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}}16@0:8"
+ "{?={CGPoint=dd}{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}}32@0:8{CGSize=dd}16"
+ "{CGPoint=dd}32@0:8{CGSize=dd}16"
+ "{UIEdgeInsets=dddd}32@0:8{CGSize=dd}16"
+ "\xf0\x91"
+ "\xf0\xc1"
+ "\xf0\xf0\x91"
- "\"B"
- "@232@0:8q16q24q32q40Q48B56B60Q64q72@80@88q96q104B112B116q120q128B136B140Q144@152@160B168B172B176q180q188q196B204B208B212@216B224B228"
- "@56@0:8q16q24q32q40^q48"
- "@60@0:8q16q24q32q40@48B56"
- "B56@0:8q16q24q32q40B48B52"
- "B64@0:8q16q24q32q40^@48^@56"
- "B68@0:8q16q24q32q40q48B56B60B64"
- "CMVideoDimensionsForCAMPhotoResolution:"
- "_captureEngineDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:"
- "_commandForResetFocus:resetExposure:resetExposureTargetBias:"
- "_fallbackVideoConfigurationForUnsupportedConfiguration:"
- "_layoutViewportWithFrame:previewFrame:trueVideoTransitionPercentComplete:"
- "_shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:"
- "_specificFramerateCommandForGraphConfiguration:withContext:"
- "_updatePreviewLayerForPreviewFrame:viewportFrame:trueVideoTransitionPercentComplete:"
- "d56@0:8d16q24q32q40q48"
- "d92@0:8q16q24q32q40q48q56q64B72B76B80^B84"
- "defaultZoomFactorForMode:device:videoConfiguration:captureOrientation:videoStabilizationStrength:videoEncodingBehavior:customLens:outputToExternalStorage:isTrueVideo:prefersHDR10BitVideo:overrodeWithForcedZoomValue:"
- "exifFocalLengthsByZoomFactorForMode:device:videoConfiguration:videoStabilizationStrength:customLensGroup:isTrueVideo:"
- "fallbackPrimaryConstituentDeviceSelectionForMode:device:videoConfiguration:videoStabilizationStrength:macroMode:"
- "initWithAutomaticVideoStabilizationEnabled:strength:"
- "initWithCaptureMode:captureDevice:macroMode:videoConfiguration:audioConfiguration:mixAudioWithOthers:windNoiseRemovalEnabled:previewConfiguration:previewSampleBufferVideoFormat:previewFilters:videoThumbnailOutputConfiguration:photoEncodingBehavior:videoEncodingBehavior:enableAutoFPSVideo:videoHDRSuspended:aspectRatioCrop:photoQualityPrioritization:captureMirrored:enableRAWCaptureIfSupported:semanticStyleSupport:previewSemanticStyle:smartStyles:enableContentAwareDistortionCorrection:enableResponsiveShutter:suspendLivePhotoCapture:videoStabilizationStrength:maximumPhotoResolution:colorSpace:videoBinned:enableDepthSuggestion:enableZoomPIP:customLensGroup:trueVideoEnabled:prefersHDR10BitVideo:"
- "initWithVideoConfiguration:"
- "isActionModeControlSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:"
- "isEnhancedStabilizationSupportedForMode:device:videoConfiguration:videoEncodingBehavior:trueVideoEnabled:prefersHDR10BitVideo:"
- "isLensPositionControlSupportedForMode:device:videoConfiguration:videoStabilizationStrength:"
- "isSuperWideAutoMacroSupportedForMode:device:videoConfiguration:videoStabilizationStrength:"
- "isSupportedVideoConfiguration:forMode:device:trueVideoEnabled:"
- "isTripleCameraSupportedForMode:devicePosition:videoConfiguration:videoStabilizationStrength:"
- "isVideoStabilizationStrength:supportedForMode:device:videoConfiguration:videoEncodingBehavior:outputToExternalStorage:trueVideoEnabled:prefersHDR10BitVideo:"
- "isVideoStabilizationStrength:supportedForMode:devicePosition:trueVideoEnabled:"
- "isZoomPIPSupportedForMode:devicePosition:"
- "preferredDeviceForPosition:mode:videoConfiguration:videoStabilizationStrength:"
- "q76@0:8q16q24q32q40q48{?=qq}56B72"
- "resolveDesiredMacroMode:forMode:device:videoConfiguration:videoStabilizationStrength:photoFormat:optionalDepthEffectEnabled:"
- "resolvedDeviceForDesiredDevice:mode:videoConfiguration:videoStabilizationStrength:"
- "sanitizeVideoConfigurationForDesiredConfiguration:mode:device:trueVideoEnabled:"
- "shouldAllowCameraToggleForMode:devicePosition:videoConfiguration:videoStabilizationStrength:"
- "shouldApplyContinuousZoomForMode:device:videoConfiguration:videoStabilizationStrength:zoomFactors:displayZoomFactors:"
- "shouldEmulateTripleCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:"
- "shouldEmulateWideDualCameraZoomForMode:device:videoConfiguration:videoStabilizationStrength:"
- "videoDeviceForMode:desiredDevice:videoConfiguration:videoStabilizationStrength:resolvedDevice:"
- "videoDeviceFormatForGraphConfiguration:captureSession:"
- "zoomControlDisplayValueForZoomFactor:mode:device:videoConfiguration:videoStabilizationStrength:"
- "{?=ii}24@0:8q16"
- "\xf0Q"
- "\xf0\xb1"
- "\xf0\xf0\x81"

```
