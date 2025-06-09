## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0xfc83c
-  __TEXT.__auth_stubs: 0x19a0
-  __TEXT.__objc_methlist: 0xda0c
-  __TEXT.__const: 0x900
-  __TEXT.__gcc_except_tab: 0x2558
-  __TEXT.__cstring: 0x1b38c
-  __TEXT.__oslogstring: 0x56b1
+650.0.0.122.4
+  __TEXT.__text: 0x14fc54
+  __TEXT.__auth_stubs: 0x1b30
+  __TEXT.__objc_methlist: 0xde8c
+  __TEXT.__const: 0x930
+  __TEXT.__gcc_except_tab: 0x28c8
+  __TEXT.__cstring: 0x279bb
+  __TEXT.__oslogstring: 0x1f0b0
   __TEXT.__dlopen_cstrs: 0x178
   __TEXT.__ustring: 0x54
-  __TEXT.__unwind_info: 0x4140
-  __TEXT.__objc_classname: 0x17da
-  __TEXT.__objc_methname: 0x25de4
-  __TEXT.__objc_methtype: 0x3abb
-  __TEXT.__objc_stubs: 0x16120
-  __DATA_CONST.__got: 0x2728
-  __DATA_CONST.__const: 0x7b88
-  __DATA_CONST.__objc_classlist: 0x588
+  __TEXT.__unwind_info: 0x45f8
+  __TEXT.__objc_classname: 0x17e1
+  __TEXT.__objc_methname: 0x26ddd
+  __TEXT.__objc_methtype: 0x3c0f
+  __TEXT.__objc_stubs: 0x16ac0
+  __DATA_CONST.__got: 0x27b0
+  __DATA_CONST.__const: 0x6f30
+  __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ec0
+  __DATA_CONST.__objc_selrefs: 0x71c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x4c0
-  __DATA_CONST.__objc_arraydata: 0x440
-  __AUTH_CONST.__auth_got: 0xce0
-  __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0x12400
-  __AUTH_CONST.__objc_const: 0x16450
-  __AUTH_CONST.__objc_intobj: 0x8e8
+  __DATA_CONST.__objc_arraydata: 0x428
+  __AUTH_CONST.__auth_got: 0xda8
+  __AUTH_CONST.__const: 0xa40
+  __AUTH_CONST.__cfstring: 0x13940
+  __AUTH_CONST.__objc_const: 0x16908
+  __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x2d0
+  __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x175c
-  __DATA.__data: 0xc58
-  __DATA.__bss: 0x6b0
-  __DATA.__common: 0x60
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x17dc
+  __DATA.__data: 0xc70
+  __DATA.__common: 0x280
+  __DATA.__bss: 0x6f0
   __DATA_DIRTY.__objc_data: 0x2fd0
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__common: 0x1a0
-  __DATA_DIRTY.__bss: 0x378
+  __DATA_DIRTY.__common: 0x2b0
+  __DATA_DIRTY.__bss: 0x3d0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
+  - /System/Library/Frameworks/CoreMIDI.framework/CoreMIDI
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9340FEC8-203C-39F2-BFFA-62C3AA381E38
-  Functions: 5654
-  Symbols:   20155
-  CStrings:  11167
+  UUID: 1F3DBC2B-AA9F-3344-891D-6898C4329F49
+  Functions: 5907
+  Symbols:   20967
+  CStrings:  13379
 
Symbols:
+ +[AVCaptureDevice _checkEligibilityForEffect:]
+ +[AVCapturePhotoOutput temporarilySuppressShutterSoundForAirpodStemClick]
+ +[AVCaptureSession _isDeviceInputInSpatialAudioMode:]
+ +[AVCaptureSpatialAudioMetadataSampleGenerator initialize]
+ +[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:].cold.1
+ +[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:].cold.2
+ +[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:].cold.3
+ +[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:].cold.4
+ +[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:].cold.5
+ -[AVCaptureAudioDataOutput setSpatialAudioChannelLayoutTag:]
+ -[AVCaptureAudioDataOutput spatialAudioChannelLayoutTag]
+ -[AVCaptureConnection _indexOfAudioLevelChannel:]
+ -[AVCaptureConnection connectionID]
+ -[AVCaptureControlsOverlay _sendControlsIsolated].cold.1
+ -[AVCaptureControlsOverlay _sendControlsIsolated].cold.2
+ -[AVCaptureControlsOverlay cameraOverlayConnection:didChangeActiveControlIdentifier:].cold.1
+ -[AVCaptureControlsOverlay cameraOverlayConnection:didChangeFocusLocked:].cold.1
+ -[AVCaptureControlsOverlay cameraOverlayConnection:didChangeInterfaceReduced:].cold.1
+ -[AVCaptureControlsOverlay cameraOverlayConnection:didChangeOverlayVisible:activeControlIdentifier:].cold.1
+ -[AVCaptureControlsOverlay cameraOverlayConnection:didChangeStatus:].cold.1
+ -[AVCaptureDeferredPhotoProcessor prewarmWithSettings:].cold.1
+ -[AVCaptureDeferredPhotoProcessor prewarmWithSettings:].cold.2
+ -[AVCaptureDeferredPhotoProcessor prewarmWithSettings:].cold.3
+ -[AVCaptureDeferredPhotoProxy initWithDeferredPhotoIdentifier:applicationIdentifier:photoLibraryThumbnailDimensions:]
+ -[AVCaptureDeferredPhotoProxy photoLibraryThumbnailDimensions]
+ -[AVCaptureDeferredPhotoSettings initWithCoder:].cold.1
+ -[AVCaptureDeferredPhotoSettings initWithCoder:].cold.2
+ -[AVCaptureDevice aspectRatioForNonDestructiveCrop]
+ -[AVCaptureDevice defaultRectForExposurePointOfInterest:]
+ -[AVCaptureDevice defaultRectForFocusPointOfInterest:]
+ -[AVCaptureDevice exposureRectOfInterest]
+ -[AVCaptureDevice focusRectOfInterest]
+ -[AVCaptureDevice isDICOMSupported]
+ -[AVCaptureDevice isExposureRectOfInterestSupported]
+ -[AVCaptureDevice isFocusRectOfInterestSupported]
+ -[AVCaptureDevice minExposureRectOfInterestSize]
+ -[AVCaptureDevice minFocusRectOfInterestSize]
+ -[AVCaptureDevice nominalFocalLengthIn35mmFilm]
+ -[AVCaptureDevice preferredIOBufferDuration]
+ -[AVCaptureDevice setAspectRatioForNonDestructiveCrop:]
+ -[AVCaptureDevice setCinematicVideoFixedFocusAtPoint:focusMode:]
+ -[AVCaptureDevice setCinematicVideoTrackingFocusAtPoint:focusMode:]
+ -[AVCaptureDevice setCinematicVideoTrackingFocusWithDetectedObjectID:focusMode:]
+ -[AVCaptureDevice setExposureRectOfInterest:]
+ -[AVCaptureDevice setFocusRectOfInterest:]
+ -[AVCaptureDevice setPreferredIOBufferDuration:]
+ -[AVCaptureDevice(CameraLensSmudgeDetection) cameraLensSmudgeDetectionInterval]
+ -[AVCaptureDevice(CameraLensSmudgeDetection) cameraLensSmudgeDetectionStatus]
+ -[AVCaptureDevice(CameraLensSmudgeDetection) isCameraLensSmudgeDetectionEnabled]
+ -[AVCaptureDevice(CameraLensSmudgeDetection) setCameraLensSmudgeDetectionEnabled:detectionInterval:]
+ -[AVCaptureDeviceDiscoverySession init].cold.1
+ -[AVCaptureDeviceFormat _defaultPhotoDimensionsWithHighResolutionCaptureEnabled:]
+ -[AVCaptureDeviceFormat isCameraLensSmudgeDetectionSupported]
+ -[AVCaptureDeviceFormat isCinematicVideoCaptureSupported]
+ -[AVCaptureDeviceFormat videoFrameRateRangeForCinematicVideo]
+ -[AVCaptureDeviceFormat videoMaxZoomFactorForCinematicVideo]
+ -[AVCaptureDeviceFormat videoMinZoomFactorForCinematicVideo]
+ -[AVCaptureDeviceInput _resetCinematicVideoCaptureSupported]
+ -[AVCaptureDeviceInput isCinematicVideoCaptureEnabled]
+ -[AVCaptureDeviceInput isCinematicVideoCaptureSupported]
+ -[AVCaptureDeviceInput notReadyError].cold.1
+ -[AVCaptureDeviceInput remoteIOOutputFormat]
+ -[AVCaptureDeviceInput sensitiveContentAnalyzerEnabled]
+ -[AVCaptureDeviceInput sensitiveContentAnalyzerXPCObject]
+ -[AVCaptureDeviceInput setCinematicVideoCaptureEnabled:]
+ -[AVCaptureDeviceInput setRemoteIOOutputFormat:]
+ -[AVCaptureDeviceInput setSensitiveContentAnalyzerEnabled:]
+ -[AVCaptureDeviceInput setSensitiveContentAnalyzerXPCObject:]
+ -[AVCaptureDeviceRotationCoordinator _updateVideoRotationAngleForHorizonLevelPreview].cold.3
+ -[AVCaptureFigAudioDevice init].cold.1
+ -[AVCaptureFigAudioDevice preferredIOBufferDuration]
+ -[AVCaptureFigAudioDevice setPreferredIOBufferDuration:]
+ -[AVCaptureFigVideoDevice _defaultRectForExposurePointOfInterest:]
+ -[AVCaptureFigVideoDevice _defaultRectForFocusPointOfInterest:focusMode:]
+ -[AVCaptureFigVideoDevice _minExposureRectOfInterestSizeForFormat:]
+ -[AVCaptureFigVideoDevice _minFocusRectOfInterestSizeForFormat:]
+ -[AVCaptureFigVideoDevice _setSimulatedAperture:]
+ -[AVCaptureFigVideoDevice _updateCinematicVideoCaptureSceneMonitoringStatus:]
+ -[AVCaptureFigVideoDevice _updateCinematicVideoCaptureSceneMonitoringStatus:].cold.1
+ -[AVCaptureFigVideoDevice aspectRatioForNonDestructiveCrop]
+ -[AVCaptureFigVideoDevice cameraLensSmudgeDetectionInterval]
+ -[AVCaptureFigVideoDevice cameraLensSmudgeDetectionStatus]
+ -[AVCaptureFigVideoDevice cinematicVideoCaptureSceneMonitoringStatuses]
+ -[AVCaptureFigVideoDevice defaultRectForExposurePointOfInterest:]
+ -[AVCaptureFigVideoDevice defaultRectForFocusPointOfInterest:]
+ -[AVCaptureFigVideoDevice exposureRectOfInterest]
+ -[AVCaptureFigVideoDevice figCaptureSourceAttributes]
+ -[AVCaptureFigVideoDevice focusRectOfInterest]
+ -[AVCaptureFigVideoDevice init].cold.1
+ -[AVCaptureFigVideoDevice isCameraLensSmudgeDetectionEnabled]
+ -[AVCaptureFigVideoDevice isDICOMSupported]
+ -[AVCaptureFigVideoDevice isExposureRectOfInterestSupported]
+ -[AVCaptureFigVideoDevice isFocusRectOfInterestSupported]
+ -[AVCaptureFigVideoDevice minExposureRectOfInterestSize]
+ -[AVCaptureFigVideoDevice minFocusRectOfInterestSize]
+ -[AVCaptureFigVideoDevice nominalFocalLengthIn35mmFilm]
+ -[AVCaptureFigVideoDevice setAspectRatioForNonDestructiveCrop:]
+ -[AVCaptureFigVideoDevice setCameraLensSmudgeDetectionEnabled:detectionInterval:]
+ -[AVCaptureFigVideoDevice setCinematicVideoFixedFocusAtPoint:focusMode:]
+ -[AVCaptureFigVideoDevice setCinematicVideoTrackingFocusAtPoint:focusMode:]
+ -[AVCaptureFigVideoDevice setCinematicVideoTrackingFocusWithDetectedObjectID:focusMode:]
+ -[AVCaptureFigVideoDevice setExposureRectOfInterest:]
+ -[AVCaptureFigVideoDevice setFocusRectOfInterest:]
+ -[AVCaptureMetadataOutput _removeMetadataObjectTypeFromMetadataObjectTypes:]
+ -[AVCaptureMetadataOutput _removeMetadataObjectTypesFromMetadataObjectTypes:]
+ -[AVCaptureMetadataOutput isFaceTrackingSuspended]
+ -[AVCaptureMetadataOutput requiredMetadataObjectTypesForCinematicVideoCapture]
+ -[AVCaptureMetadataOutput setFaceTrackingSuspended:]
+ -[AVCaptureMovieFileOutput _delegateWrapperForSettingsID:]
+ -[AVCaptureMovieFileOutput _totalNANDBandwidthAllowed:videoCodecType:].cold.1
+ -[AVCaptureMovieFileOutput pauseRecording].cold.1
+ -[AVCaptureMovieFileOutput resumeRecording].cold.1
+ -[AVCaptureMovieFileOutput startRecordingMovieWithSettings:delegate:].cold.3
+ -[AVCaptureMovieFileOutput startRecordingToOutputFileURL:recordingDelegate:].cold.2
+ -[AVCaptureMultiCamSession _canAddInput:failureReason:].cold.1
+ -[AVCaptureMultiCamSession _requireMultiCamSupportedFormatsForVideoDevices]
+ -[AVCaptureMultiCamSession _updateSystemPressureCost].cold.1
+ -[AVCaptureOutput _recommendedAudioOutputSettingsForConnection:sourceSettings:fileType:spatialAudioChannelLayoutTag:]
+ -[AVCaptureOutput _recommendedAudioOutputSettingsForConnection:sourceSettings:fileType:spatialAudioChannelLayoutTag:].cold.1
+ -[AVCaptureOutput isDeferredStartEnabled]
+ -[AVCaptureOutput isDeferredStartSupported]
+ -[AVCaptureOutput recommendedOutputSettingsForConnection:sourceSettings:videoCodecType:fileType:isIris:outputFileURL:spatialAudioChannelLayoutTag:]
+ -[AVCaptureOutput recommendedOutputSettingsForConnection:sourceSettings:videoCodecType:fileType:isIris:outputFileURL:spatialAudioChannelLayoutTag:].cold.1
+ -[AVCaptureOutput setDeferredStartEnabled:]
+ -[AVCapturePhoto _fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:replacementPortraitEffectsMatte:replacementHairSegmentationMatte:replacementSkinSegmentationMatte:replacementTeethSegmentationMatte:replacementGlassesSegmentationMatte:replacementRawCompressionSettings:exceptionReason:].cold.1
+ -[AVCapturePhoto initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:photoLibraryThumbnails:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:]
+ -[AVCapturePhoto photoLibraryThumbnails]
+ -[AVCapturePhotoOutput _addObserversForConnectionDevice:]
+ -[AVCapturePhotoOutput _removeObserversForConnectionDevice:]
+ -[AVCaptureSession _didRunDeferredStart]
+ -[AVCaptureSession _initWithMediaEnvironment:].cold.1
+ -[AVCaptureSession _validateAudioConfiguration:]
+ -[AVCaptureSession _validateCinematicVideoConfiguration:]
+ -[AVCaptureSession _willRunDeferredStart]
+ -[AVCaptureSession automaticallyRunsDeferredStart]
+ -[AVCaptureSession configuresApplicationAudioSessionForBluetoothHighQualityRecording]
+ -[AVCaptureSession deferredStartDelegateCallbackQueue]
+ -[AVCaptureSession deferredStartDelegate]
+ -[AVCaptureSession deviceFormatForSessionPreset:device:]
+ -[AVCaptureSession handleControlsOverlay:didChangeActiveControl:].cold.1
+ -[AVCaptureSession handleControlsOverlay:didChangeFocusLocked:].cold.1
+ -[AVCaptureSession isManualDeferredStartSupported]
+ -[AVCaptureSession isManualDeferredStartSupported].cold.1
+ -[AVCaptureSession runDeferredStartWhenNeeded]
+ -[AVCaptureSession setAutomaticallyRunsDeferredStart:]
+ -[AVCaptureSession setConfiguresApplicationAudioSessionForBluetoothHighQualityRecording:]
+ -[AVCaptureSession setDeferredStartDelegate:deferredStartDelegateCallbackQueue:]
+ -[AVCaptureSessionConfiguration _videoPreviewLayersContains:]
+ -[AVCaptureSpatialAudioMetadataSampleGenerator analyzeAudioSample:]
+ -[AVCaptureSpatialAudioMetadataSampleGenerator dealloc]
+ -[AVCaptureSpatialAudioMetadataSampleGenerator init]
+ -[AVCaptureSpatialAudioMetadataSampleGenerator newTimedMetadataSampleBufferAndResetAnalyzer]
+ -[AVCaptureSpatialAudioMetadataSampleGenerator resetAnalyzer]
+ -[AVCaptureSpatialAudioMetadataSampleGenerator timedMetadataSampleBufferFormatDescription]
+ -[AVCaptureSystemPressureState initWithFigLevel:factors:recommendedFrameRateRangeForPortrait:recommendedFrameRateRangeForPhotoMode:]
+ -[AVCaptureSystemPressureState init].cold.1
+ -[AVCaptureSystemPressureState recommendedFrameRateRangeForPhotoMode]
+ -[AVCaptureSystemPressureStateInternal initWithFigLevel:factors:recommendedFrameRateRangeForPortrait:recommendedFrameRateRangeForPhotoMode:]
+ -[AVCaptureSystemPressureStateInternal recommendedFrameRateRangeForPhotoMode]
+ -[AVCaptureVideoDataOutput preparesCellularRadioForNetworkConnection]
+ -[AVCaptureVideoDataOutput preservesDynamicHDRMetadata]
+ -[AVCaptureVideoDataOutput recommendedMediaTimeScaleForAssetWriter]
+ -[AVCaptureVideoDataOutput setPreparesCellularRadioForNetworkConnection:]
+ -[AVCaptureVideoDataOutput setPreservesDynamicHDRMetadata:]
+ -[AVCaptureVideoDataOutput setVideoSettings:].cold.1
+ -[AVCaptureVideoPreviewLayer isDeferredStartEnabled]
+ -[AVCaptureVideoPreviewLayer isDeferredStartSupported]
+ -[AVCaptureVideoPreviewLayer setDeferredStartEnabled:]
+ -[AVDepthData depthDataByApplyingExifOrientation:].cold.1
+ -[AVDepthData dictionaryRepresentationForAuxiliaryDataType:].cold.1
+ -[AVDepthData dictionaryRepresentationForAuxiliaryDataType:].cold.2
+ -[AVExternalStorageDevice _uniqueIdentifier].cold.1
+ -[AVExternalStorageDevice _uniqueIdentifier].cold.2
+ -[AVExternalStorageDevice baseURL].cold.1
+ -[AVExternalStorageDevice baseURL].cold.2
+ -[AVExternalStorageDevice displayName].cold.1
+ -[AVExternalStorageDevice displayName].cold.2
+ -[AVExternalStorageDevice freeSize].cold.1
+ -[AVExternalStorageDevice freeSize].cold.2
+ -[AVExternalStorageDevice isConnected].cold.1
+ -[AVExternalStorageDevice isConnected].cold.2
+ -[AVExternalStorageDevice isNotRecommendedForCaptureUse].cold.1
+ -[AVExternalStorageDevice isNotRecommendedForCaptureUse].cold.2
+ -[AVExternalStorageDevice isNotRecommendedForCaptureUse].cold.3
+ -[AVExternalStorageDevice isNotRecommendedForCaptureUse].cold.4
+ -[AVExternalStorageDevice nextAvailableURLsWithPathExtensions:error:].cold.3
+ -[AVExternalStorageDevice totalSize].cold.1
+ -[AVExternalStorageDevice totalSize].cold.2
+ -[AVExternalStorageDeviceDiscoverySession _checkAuthorizationStatus].cold.1
+ -[AVExternalStorageDeviceDiscoverySession _requestAuthorization:].cold.1
+ -[AVExternalStorageDeviceDiscoverySession _setupExternalStorageDeviceDiscoverySession].cold.1
+ -[AVExternalStorageDeviceDiscoverySession _setupExternalStorageDeviceDiscoverySession].cold.2
+ -[AVMetadataCatHeadObject initWithObjectID:time:duration:bounds:]
+ -[AVMetadataCatHeadObject initWithObjectID:time:duration:bounds:optionalInfoDict:originalMetadataObject:sourceCaptureInput:]
+ -[AVMetadataCatHeadObject objectID]
+ -[AVMetadataDogHeadObject initWithObjectID:time:duration:bounds:]
+ -[AVMetadataDogHeadObject initWithObjectID:time:duration:bounds:optionalInfoDict:originalMetadataObject:sourceCaptureInput:]
+ -[AVMetadataDogHeadObject objectID]
+ -[AVMetadataObject cinematicVideoFocusMode]
+ -[AVMetadataObject isFixedFocus]
+ -[AVMetadataObjectInternal cinematicVideoFocusMode]
+ -[AVMetadataObjectInternal isFixedFocus]
+ -[AVMetadataObjectInternal setCinematicVideoFocusMode:]
+ -[AVMetadataObjectInternal setFixedFocus:]
+ -[AVPortraitEffectsMatte dictionaryRepresentationForAuxiliaryDataType:].cold.1
+ -[AVPortraitEffectsMatte dictionaryRepresentationForAuxiliaryDataType:].cold.2
+ -[AVPortraitEffectsMatte portraitEffectsMatteByApplyingExifOrientation:].cold.1
+ -[AVSemanticSegmentationMatte dictionaryRepresentationForAuxiliaryDataType:].cold.1
+ -[AVSemanticSegmentationMatte dictionaryRepresentationForAuxiliaryDataType:].cold.2
+ -[AVSemanticSegmentationMatte semanticSegmentationMatteByApplyingExifOrientation:].cold.1
+ -[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:]
+ -[AVSpatialOverCaptureVideoPreviewLayer _updatePrimaryCaptureRectWithCamerasMountedInLandscapeOrientation:center:aspectRatio:]
+ -[AVSpatialOverCaptureVideoPreviewLayer getPrimaryCaptureRectWithCamerasMountedInLandscapeOrientation:center:aspectRatio:uniqueID:]
+ -[AVVirtualCaptureCard capacity].cold.1
+ -[AVVirtualCaptureCard freeSpace].cold.1
+ -[AVVirtualCaptureCard showSystemUserInterface].cold.1
+ GCC_except_table10
+ GCC_except_table102
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table108
+ GCC_except_table110
+ GCC_except_table114
+ GCC_except_table12
+ GCC_except_table120
+ GCC_except_table128
+ GCC_except_table140
+ GCC_except_table149
+ GCC_except_table157
+ GCC_except_table162
+ GCC_except_table170
+ GCC_except_table179
+ GCC_except_table185
+ GCC_except_table193
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table200
+ GCC_except_table202
+ GCC_except_table205
+ GCC_except_table207
+ GCC_except_table21
+ GCC_except_table214
+ GCC_except_table215
+ GCC_except_table217
+ GCC_except_table218
+ GCC_except_table219
+ GCC_except_table223
+ GCC_except_table233
+ GCC_except_table238
+ GCC_except_table250
+ GCC_except_table268
+ GCC_except_table278
+ GCC_except_table281
+ GCC_except_table284
+ GCC_except_table285
+ GCC_except_table286
+ GCC_except_table294
+ GCC_except_table297
+ GCC_except_table312
+ GCC_except_table333
+ GCC_except_table344
+ GCC_except_table346
+ GCC_except_table348
+ GCC_except_table354
+ GCC_except_table36
+ GCC_except_table368
+ GCC_except_table391
+ GCC_except_table401
+ GCC_except_table413
+ GCC_except_table428
+ GCC_except_table431
+ GCC_except_table462
+ GCC_except_table473
+ GCC_except_table481
+ GCC_except_table488
+ GCC_except_table491
+ GCC_except_table494
+ GCC_except_table499
+ GCC_except_table50
+ GCC_except_table506
+ GCC_except_table514
+ GCC_except_table524
+ GCC_except_table538
+ GCC_except_table55
+ GCC_except_table561
+ GCC_except_table572
+ GCC_except_table582
+ GCC_except_table596
+ GCC_except_table612
+ GCC_except_table631
+ GCC_except_table65
+ GCC_except_table652
+ GCC_except_table655
+ GCC_except_table683
+ GCC_except_table685
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table711
+ GCC_except_table723
+ GCC_except_table725
+ GCC_except_table727
+ GCC_except_table733
+ GCC_except_table735
+ GCC_except_table75
+ GCC_except_table76
+ GCC_except_table77
+ GCC_except_table778
+ GCC_except_table782
+ GCC_except_table79
+ GCC_except_table835
+ GCC_except_table837
+ GCC_except_table839
+ GCC_except_table841
+ GCC_except_table883
+ GCC_except_table885
+ GCC_except_table887
+ GCC_except_table92
+ GCC_except_table96
+ _AVCaptureAspectRatioForDimensions
+ _AVCaptureClientHasEntitlement.audioFormatOverride
+ _AVCaptureClientHasEntitlement.checkAudioFormatOverrideOnceToken
+ _AVCaptureClientHasEntitlement.checkVDOPreparesCellularRadioForMRCOnceToken
+ _AVCaptureClientHasEntitlement.vdoPreparesCellularRadioForMRC
+ _AVCaptureDeviceLensSmudgeDetectionStatusChangedKeyStatus
+ _AVCaptureDeviceLensSmudgeDetectionStatusChangedNotification
+ _AVCaptureEntitlementAudioFormatOverride
+ _AVCaptureEntitlementVDOPreparesCellularRadioForMRC
+ _AVCaptureInitializeShutterSoundSuppressedByAirpodStemClickStorageOnce
+ _AVCaptureInitializeShutterSoundSuppressedByAirpodStemClickStorageOnce.cold.1
+ _AVCapturePhotoOutputIsForcedShutterSoundRegion
+ _AVCaptureSceneMonitoringStatusNotEnoughLight
+ _AVCaptureSessionInputSensitiveContentAnalyzerEnabledChangedContext
+ _AVCaptureSessionInputSensitiveContentAnalyzerXPCObjectChangedContext
+ _AVCaptureSessionIsDeferredStartSupported
+ _AVCaptureSessionIsDeferredStartSupported.cold.1
+ _AVCaptureSessionIsDeferredStartSupported.deferredStartSupported
+ _AVCaptureSessionIsDeferredStartSupported.onceToken
+ _AVCaptureSessionVideoInputDeviceLensSmudgeDetectionEnabledChangedContext
+ _AVCaptureStillImageOutputPlayShutterSound.cold.1
+ _AVCaptureTemporarilySuppressShutterSoundForAirpodStemClick
+ _AVCaptureVideoDimensionsAreValid
+ _AVControlCenterMicrophoneModuleMicrophoneModesShouldBeShownForBundleID
+ _AVControlCenterMicrophoneModuleShouldBeShownForBundleID
+ _AVControlCenterVideoEffectsModuleShouldBeShownForBundleID
+ _AVEncoderASPFrequencyKey
+ _AVEncoderContentSourceKey
+ _AVEncoderDynamicRangeControlConfigurationKey
+ _AVFileTypeDICOM
+ _AVGQ4UHSO4KRGIJFZHZ3EAGDMAK6CA
+ _AVGQ5RTE3RTRZZFRGK7IDFEQC7NFBE
+ _AVGQ6HD7ZNZD33DG7SG4DOHIPW4SUQ
+ _AVGQAJT7KNQJHRRDW5Q5QTGETOLK2E
+ _AVGQBGWR3YSZWCQ7BKUUAOT5CCLHHE
+ _AVGQCB54MH3XAXNGTVD2SAMOV5WWOQ
+ _AVGQCaptureDeferredStartSupported
+ _AVGQCaptureMultipleAudioDataOutputsSupported
+ _AVGQCaptureSessionMultiCamCaptureAlwaysRequiresSupportedFormats
+ _AVGQFrontFacingCameraSupportsCinematicVideo
+ _AVGQFrontFacingCameraSupportsCinematicVideo4K
+ _AVGQFrontFacingCameraSupportsPortraitAutoSuggest
+ _AVGQHDDMQ6RTH76PQ2HVCQ4MSWG63Q
+ _AVGQHSSMVIQNR3MAPIGELAQM7DWP4U
+ _AVGQIDWZFGNLZOQVZINTCD5JZM57DE
+ _AVGQKYDMKTE2UUKHJCGGZGQNYH5GDE
+ _AVGQODGWLXGASKA4RNU2OP6Z44TGZ4
+ _AVGQOKRXQZPHFZ4X2XCPOHTANZXNGM
+ _AVGQQIBUFDUYMZTKVBF36FTLQON3DY
+ _AVGQRearFacingCameraSupportsCinematicVideo
+ _AVGQRearFacingCameraSupportsCinematicVideo4K
+ _AVGQRearFacingCameraSupportsPortraitAutoSuggest
+ _AVGQRearWideCameraDisplayCustomZoomStops
+ _AVGQT42HZJM7T4BHFEGWILGWIJSNEQ
+ _AVGQVYXTSFZ3R7TURIB5WPPITDPJLY
+ _AVGQYPHR3FTUAZCCTEYFPSINLTE7DI
+ _AVMetadataItemGetDataTypesForIdentifiersOfFieldsOfDogBodyObject
+ _AVMetadataItemGetDataTypesForIdentifiersOfFieldsOfSalientObject
+ _AVMetadataItemMakeCatHeadObjectFromBoxedMetadata
+ _AVMetadataItemMakeCatHeadObjectFromBoxedMetadata.cold.1
+ _AVMetadataItemMakeCatHeadObjectFromBoxedMetadata.cold.2
+ _AVMetadataItemMakeDogHeadObjectFromBoxedMetadata
+ _AVMetadataItemMakeDogHeadObjectFromBoxedMetadata.cold.1
+ _AVMetadataItemMakeDogHeadObjectFromBoxedMetadata.cold.2
+ _CGRectGetMidX
+ _CGRectGetMidY
+ _CGRectIntersection
+ _CMTimeMinimum
+ _CVPixelBufferGetIOSurface
+ _D16_D17
+ _D27_D28
+ _D37_D38
+ _D421_D431
+ _D47_D48
+ _D52g_D53g
+ _D63_D64
+ _D73_D74
+ _D93_D94
+ _FigCaptureFrameRateAsData
+ _FigCaptureFrameRateAsFloat
+ _FigCaptureFrameRateFromCMTime
+ _FigCaptureFrameRateFromFloat
+ _FigCaptureFrontCameraRotationAngle
+ _FigCaptureGetFrameworkRadarComponent
+ _FigCaptureGetFrameworkRadarComponentName
+ _FigCapturePixelFormatIsPackedBayerRaw
+ _FigCapturePixelFormatIsUsedForProRes
+ _FigCapturePleaseFileRadar
+ _FigCaptureRotateCalibrationData
+ _FigCaptureSimplifiedLeastCommonMultiple
+ _FigCaptureSourceDefaultAudioSampleRateForClientSDKVersionToken
+ _FigDispatchQueueCreateWithPriority
+ _FigKTraceInit
+ _FigSignalErrorAt3
+ _IOSurfaceCopyValue
+ _IOSurfaceGetID
+ _J317_J317x_J318_J318x_J320_J320x_J321_J321x
+ _J517_J517x_J518_J518x_J522_J522x_J523_J523x
+ _NSDebugDescriptionErrorKey
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_AVCaptureSpatialAudioMetadataSampleGenerator
+ _OBJC_CLASS_$_CMCaptureSpatialAudioMetadataSampleGenerator
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSPointerArray
+ _OBJC_IVAR_$_AVCaptureAudioDataOutputInternal.spatialAudioChannelLayoutTag
+ _OBJC_IVAR_$_AVCaptureConnectionInternal.spatialAudioChannelLayoutTagForChannelLevels
+ _OBJC_IVAR_$_AVCaptureDeferredPhotoProxy._photoLibraryThumbnailDimensions
+ _OBJC_IVAR_$_AVCaptureDeviceFormatInternal.cinematicVideoSupported
+ _OBJC_IVAR_$_AVCaptureDeviceInputInternal.cinematicVideoCaptureEnabled
+ _OBJC_IVAR_$_AVCaptureDeviceInputInternal.cinematicVideoCaptureSupported
+ _OBJC_IVAR_$_AVCaptureDeviceInputInternal.remoteIOOutputFormat
+ _OBJC_IVAR_$_AVCaptureDeviceInputInternal.sensitiveContentAnalyzerEnabled
+ _OBJC_IVAR_$_AVCaptureDeviceInputInternal.sensitiveContentAnalyzerXPCObject
+ _OBJC_IVAR_$_AVCaptureFigAudioDevice._preferredIOBufferDuration
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._cameraLensSmudgeDetectionEnabled
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._cameraLensSmudgeDetectionInterval
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._cameraLensSmudgeDetectionStatus
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._cinematicVideoEnabled
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._cinematicVideoSceneMonitoringStatuses
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._exposureRectOfInterest
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._focusRectOfInterest
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._geometricDistortionCorrectionEnabledByClient
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._geometricDistortionCorrectionSupported
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._isDefaultExposureRectOfInterest
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._isDefaultFocusRectOfInterest
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._minExposureRectOfInterestSize
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._minFocusRectOfInterestSize
+ _OBJC_IVAR_$_AVCaptureMetadataOutputInternal.faceTrackingSuspended
+ _OBJC_IVAR_$_AVCaptureOutputInternal.deferredStartEnabled
+ _OBJC_IVAR_$_AVCapturePhotoInternal.photoLibraryThumbnails
+ _OBJC_IVAR_$_AVCaptureSessionInternal.automaticallyRunsDeferredStart
+ _OBJC_IVAR_$_AVCaptureSessionInternal.configuresApplicationAudioSessionForBluetoothHighQualityRecording
+ _OBJC_IVAR_$_AVCaptureSessionInternal.deferredStartDelegateStorage
+ _OBJC_IVAR_$_AVCaptureSpatialAudioMetadataSampleGenerator._spatialAudioMetadataSampleGenerator
+ _OBJC_IVAR_$_AVCaptureSystemPressureStateInternal._recommendedFrameRateRangeForPhotoMode
+ _OBJC_IVAR_$_AVCaptureVideoDataOutputInternal.preparesCellularRadioForNetworkConnection
+ _OBJC_IVAR_$_AVCaptureVideoDataOutputInternal.preparesCellularRadioForNetworkConnectionSetByClient
+ _OBJC_IVAR_$_AVCaptureVideoDataOutputInternal.preservesDynamicHDRMetadata
+ _OBJC_IVAR_$_AVCaptureVideoPreviewLayerInternal.deferredStartEnabled
+ _OBJC_IVAR_$_AVMetadataCatHeadObject._objectID
+ _OBJC_IVAR_$_AVMetadataDogHeadObject._objectID
+ _OBJC_IVAR_$_AVMetadataObjectInternal._cinematicVideoFocusMode
+ _OBJC_IVAR_$_AVMetadataObjectInternal._fixedFocus
+ _OBJC_IVAR_$_AVSpatialOverCaptureVideoPreviewLayer._lastCamerasMountedInLandscapeOrientation
+ _OBJC_IVAR_$_AVSpatialOverCaptureVideoPreviewLayer._primaryCaptureRectTrueVideoTransitionPercentComplete
+ _OBJC_METACLASS_$_AVCaptureSpatialAudioMetadataSampleGenerator
+ __OBJC_$_CLASS_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification|CameraLensSmudgeDetection)
+ __OBJC_$_CLASS_METHODS_AVCaptureSpatialAudioMetadataSampleGenerator
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification|CameraLensSmudgeDetection)
+ __OBJC_$_INSTANCE_METHODS_AVCaptureSpatialAudioMetadataSampleGenerator
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureSpatialAudioMetadataSampleGenerator
+ __OBJC_$_INSTANCE_VARIABLES_AVMetadataCatHeadObject
+ __OBJC_$_INSTANCE_VARIABLES_AVMetadataDogHeadObject
+ __OBJC_$_PROP_LIST_AVCaptureSpatialAudioMetadataSampleGenerator
+ __OBJC_CLASS_RO_$_AVCaptureSpatialAudioMetadataSampleGenerator
+ __OBJC_METACLASS_RO_$_AVCaptureSpatialAudioMetadataSampleGenerator
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke.216
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_16
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_17
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_18
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_19
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_20
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_21
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_22
+ ___104-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForWrapper:withPayload:demoof:addMetadata:]_block_invoke.178
+ ___110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke.192
+ ___110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke.193
+ ___113-[AVCaptureStillImageOutput prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:]_block_invoke.170
+ ___122-[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:]_block_invoke
+ ___132-[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:]_block_invoke.46
+ ___29+[AVCaptureSession dotString]_block_invoke
+ ___29+[AVCaptureSession dotString]_block_invoke_10
+ ___29+[AVCaptureSession dotString]_block_invoke_2
+ ___29+[AVCaptureSession dotString]_block_invoke_3
+ ___29+[AVCaptureSession dotString]_block_invoke_4
+ ___29+[AVCaptureSession dotString]_block_invoke_6
+ ___29+[AVCaptureSession dotString]_block_invoke_7
+ ___29+[AVCaptureSession dotString]_block_invoke_8
+ ___29+[AVCaptureSession dotString]_block_invoke_9
+ ___384-[AVCapturePhoto _fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:replacementPortraitEffectsMatte:replacementHairSegmentationMatte:replacementSkinSegmentationMatte:replacementTeethSegmentationMatte:replacementGlassesSegmentationMatte:replacementRawCompressionSettings:exceptionReason:]_block_invoke.cold.2
+ ___40-[AVCaptureFigVideoDevice setFocusMode:]_block_invoke_2
+ ___40-[AVCaptureSession _didRunDeferredStart]_block_invoke
+ ___41-[AVCaptureSession _willRunDeferredStart]_block_invoke
+ ___43-[AVCaptureFigVideoDevice setExposureMode:]_block_invoke.428
+ ___46-[AVCaptureFigVideoDevice focusRectOfInterest]_block_invoke
+ ___47-[AVCaptureFigVideoDevice focusPointOfInterest]_block_invoke
+ ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke.442
+ ___49-[AVCaptureFigVideoDevice exposureRectOfInterest]_block_invoke
+ ___50-[AVCaptureFigVideoDevice exposurePointOfInterest]_block_invoke
+ ___50-[AVCaptureFigVideoDevice setFocusRectOfInterest:]_block_invoke
+ ___50-[AVCaptureFigVideoDevice setFocusRectOfInterest:]_block_invoke_2
+ ___51-[AVCaptureFigVideoDevice setFocusPointOfInterest:]_block_invoke
+ ___51-[AVCaptureFigVideoDevice setFocusPointOfInterest:]_block_invoke_2
+ ___53-[AVCaptureFigVideoDevice minFocusRectOfInterestSize]_block_invoke
+ ___53-[AVCaptureFigVideoDevice setExposureRectOfInterest:]_block_invoke
+ ___53-[AVCaptureFigVideoDevice setExposureRectOfInterest:]_block_invoke_2
+ ___53-[AVCaptureFigVideoDevice setExposureRectOfInterest:]_block_invoke_3
+ ___54+[AVCaptureDevice continuityCaptureCameraCapabilities]_block_invoke.554
+ ___54-[AVCaptureFigVideoDevice setExposurePointOfInterest:]_block_invoke
+ ___54-[AVCaptureFigVideoDevice setExposurePointOfInterest:]_block_invoke_2
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.685
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.696
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.696.cold.1
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.698
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.703
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.706
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.714
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.723
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.727
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.728
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.733
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.735
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.740
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.742
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.747
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.756
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.686
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.702
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.704
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.707
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.715
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.732
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.734
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.739
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.741
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.746
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.751
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.687
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.705
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.716
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.752
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.691
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.692
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_6.693
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_7.694
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_8.695
+ ___56-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]_block_invoke.626
+ ___56-[AVCaptureFigVideoDevice minExposureRectOfInterestSize]_block_invoke
+ ___58-[AVCaptureFigVideoDevice cameraLensSmudgeDetectionStatus]_block_invoke
+ ___58-[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:]_block_invoke.337
+ ___59-[AVCaptureFigVideoDevice aspectRatioForNonDestructiveCrop]_block_invoke
+ ___59-[AVCaptureVideoDataOutput setPreservesDynamicHDRMetadata:]_block_invoke
+ ___60-[AVCaptureFigVideoDevice cameraLensSmudgeDetectionInterval]_block_invoke
+ ___61-[AVCaptureFigVideoDevice isCameraLensSmudgeDetectionEnabled]_block_invoke
+ ___63+[AVCaptureDevice requestAccessForMediaType:completionHandler:]_block_invoke.208
+ ___63-[AVCaptureFigVideoDevice setAspectRatioForNonDestructiveCrop:]_block_invoke
+ ___63-[AVCaptureSession handleControlsOverlay:didChangeFocusLocked:]_block_invoke.cold.1
+ ___65-[AVCaptureSession handleControlsOverlay:didChangeActiveControl:]_block_invoke.cold.1
+ ___66-[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:]_block_invoke.29
+ ___67-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:]_block_invoke.341
+ ___67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.329
+ ___67-[AVCaptureFigVideoDevice isGeometricDistortionCorrectionSupported]_block_invoke
+ ___67-[AVCaptureFigVideoDevice setExposureTargetBias:completionHandler:]_block_invoke.448
+ ___68-[AVCaptureSession handleControlsOverlay:didChangeInterfaceReduced:]_block_invoke.cold.1
+ ___71-[AVCaptureFigVideoDevice cinematicVideoCaptureSceneMonitoringStatuses]_block_invoke
+ ___72-[AVCaptureFigVideoDevice chromaticityValuesForDeviceWhiteBalanceGains:]_block_invoke.501
+ ___72-[AVCaptureFigVideoDevice setCinematicVideoFixedFocusAtPoint:focusMode:]_block_invoke
+ ___72-[AVCapturePhotoOutput setPreparedPhotoSettingsArray:completionHandler:]_block_invoke.201
+ ___74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.679
+ ___75-[AVCaptureFigVideoDevice setCinematicVideoTrackingFocusAtPoint:focusMode:]_block_invoke
+ ___76-[AVCaptureSession handleControlsOverlay:didChangeVisibility:activeControl:]_block_invoke.cold.1
+ ___77-[AVCaptureFigVideoDevice _updateCinematicVideoCaptureSceneMonitoringStatus:]_block_invoke
+ ___80-[AVCaptureFigVideoDevice setFocusModeLockedWithLensPosition:completionHandler:]_block_invoke.415
+ ___81-[AVCaptureFigVideoDevice setCameraLensSmudgeDetectionEnabled:detectionInterval:]_block_invoke
+ ___81-[AVCaptureFigVideoDevice setCameraLensSmudgeDetectionEnabled:detectionInterval:]_block_invoke_2
+ ___83-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke.443
+ ___85-[AVCapturePhotoOutput _handleStillImageCompleteNotification:withPayload:forRequest:]_block_invoke.796
+ ___85-[AVCapturePhotoOutput _handleStillImageCompleteNotification:withPayload:forRequest:]_block_invoke.797
+ ___86-[AVCaptureMovieFileOutput handleDidStartRecordingNotificationForWrapper:withPayload:]_block_invoke.169
+ ___88-[AVCaptureFigVideoDevice setCinematicVideoTrackingFocusWithDetectedObjectID:focusMode:]_block_invoke
+ ___94-[AVCapturePhotoOutput commitMomentCaptureWithUniqueID:toMovieRecordingWithSettings:delegate:]_block_invoke.393
+ ___98-[AVCaptureFigVideoDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:]_block_invoke.499
+ ___AVCaptureInitializeShutterSoundSuppressedByAirpodStemClickStorageOnce_block_invoke
+ ___AVCaptureSessionIsDeferredStartSupported_block_invoke
+ ___AVCaptureStillImageOutputPlayShutterSound_block_invoke
+ ___AVCaptureTemporarilySuppressShutterSoundForAirpodStemClick_block_invoke
+ ___AVCaptureTemporarilySuppressShutterSoundForAirpodStemClick_block_invoke_2
+ ___AVControlCenterModulesPrewarm_block_invoke.441
+ ___block_descriptor_104_e8_32o40r48r56r64r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8
+ ___block_descriptor_104_e8_32o40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_112_e8_32o40r48r56r64r72r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8r72l8
+ ___block_descriptor_136_e8_32o40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_228_e8_32o40o48o56o64o72o80o88o96o104o112r_e51_v16?0"<AVCaptureDeferredPhotoProcessorDelegate>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8r112l8s104l8
+ ___block_descriptor_32_e28_"NSString"16?0"NSString"8l
+ ___block_descriptor_32_e48_"NSMutableString"16?0"AVCaptureDeviceFormat"8l
+ ___block_descriptor_40_e8_32b_e41_"NSMutableString"16?0"AVCaptureInput"8ls32l8
+ ___block_descriptor_40_e8_32b_e45_"NSMutableString"16?0"AVCaptureInputPort"8ls32l8
+ ___block_descriptor_40_e8_32o_e49_v16?0"<AVCaptureSessionDeferredStartDelegate>"8ls32l8
+ ___block_descriptor_40_e8_32r_e18_"NSString"16?08lr32l8
+ ___block_descriptor_441_e8_32o40o48o56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r296r304r312r320r328r336r344r352r360r368r376r384r392r400r408r416r424r432r_e5_v8?0ls32l8s40l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8s48l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8r280l8r288l8r296l8r304l8r312l8r320l8r328l8r336l8r344l8r352l8r360l8r368l8r376l8r384l8r392l8r400l8r408l8r416l8r424l8r432l8
+ ___block_descriptor_48_e8_32o40b_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_48_e8_32o40b_e8_v12?0C8ls32l8s40l8
+ ___block_descriptor_64_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_65_e8_32o40o48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_65_e8_32o_e5_v8?0ls32l8
+ ___block_descriptor_72_e8_32o40r48r56r_e5_v8?0lr40l8s32l8r48l8r56l8
+ ___block_descriptor_73_e8_32o40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_74_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_80_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32o40r48r56r_e5_v8?0lr40l8s32l8r48l8r56l8
+ ___block_descriptor_88_e8_32o40o48o56o64r72r80r_e5_v8?0lr64l8s32l8r72l8s40l8s48l8s56l8r80l8
+ ___block_literal_global.109
+ ___block_literal_global.1108
+ ___block_literal_global.1110
+ ___block_literal_global.1115
+ ___block_literal_global.123
+ ___block_literal_global.1378
+ ___block_literal_global.1385
+ ___block_literal_global.139
+ ___block_literal_global.141
+ ___block_literal_global.150
+ ___block_literal_global.163
+ ___block_literal_global.1669
+ ___block_literal_global.187
+ ___block_literal_global.192
+ ___block_literal_global.209
+ ___block_literal_global.220
+ ___block_literal_global.222
+ ___block_literal_global.254
+ ___block_literal_global.264
+ ___block_literal_global.287
+ ___block_literal_global.380
+ ___block_literal_global.402
+ ___block_literal_global.413
+ ___block_literal_global.421
+ ___block_literal_global.426
+ ___block_literal_global.434
+ ___block_literal_global.444
+ ___block_literal_global.464
+ ___block_literal_global.468
+ ___block_literal_global.490
+ ___block_literal_global.547
+ ___block_literal_global.552
+ ___block_literal_global.556
+ ___block_literal_global.69
+ ___getCameraCaptureLegacyLog_block_invoke
+ __os_log_default
+ _abort_with_reason
+ _audit_token_to_pid
+ _avccm_commonDisallowListForVideoEffectsAndMicModes
+ _avcmcs_computeSystemPressureCost.allSlopes
+ _avcmcs_computeSystemPressureCost.sSlopeIndicesOnce
+ _avco_cancelShutterSoundSuppressionTimer
+ _avcp_copyCGImageForUncompressedBuffer.cold.1
+ _avcp_copyDNGFileDataRepresentationForSushiRawBuffer.cold.1
+ _avcp_copyTIFFFileDataRepresentationForImage.cold.1
+ _avcp_copyTIFFFileDataRepresentationForImage.cold.2
+ _avcp_copyTIFFFileDataRepresentationForImage.cold.3
+ _dyld_get_program_sdk_version_token
+ _fvd_cgRectDictionaryForRectOfInterest
+ _fvd_validatedRectOfInterestForMinRectOfInterestSize
+ _gAVCaptureAudioDataOutputTrace
+ _gAVCaptureCameraCalibrationDataOutputTrace
+ _gAVCaptureControlsOverlayTrace
+ _gAVCaptureCoreAnalyticsReporterTrace
+ _gAVCaptureDataOutputDelegateCallbackHelperTrace
+ _gAVCaptureDataOutputSynchronizerTrace
+ _gAVCaptureDeferredPhotoSettingsTrace
+ _gAVCaptureDepthDataOutputTrace
+ _gAVCaptureDeviceFormatTrace
+ _gAVCaptureDeviceInputTrace
+ _gAVCaptureFileOutputTrace
+ _gAVCaptureIndexPickerTrace
+ _gAVCaptureInputPortTrace
+ _gAVCaptureInputTrace
+ _gAVCaptureOutputTrace
+ _gAVCapturePointCloudDataOutputTrace
+ _gAVCaptureSliderTrace
+ _gAVCaptureStillImageOutputTrace
+ _gAVCaptureSystemExposureBiasSliderTrace
+ _gAVCaptureSystemLensSelectorTrace
+ _gAVCaptureSystemStyleParameterSliderTrace
+ _gAVCaptureSystemStylePickerTrace
+ _gAVCaptureSystemZoomSliderTrace
+ _gAVCaptureToggleTrace
+ _gAVCaptureVideoDataOutputTrace
+ _gAVCaptureVideoThumbnailOutputTrace
+ _gAVCaptureVisionDataOutputTrace
+ _gAVDepthDataTrace
+ _gAVGestaltTrace
+ _gAVMetadataMachineReadableCodeObjectTrace
+ _gAVOfflineVideoStabilizerTrace
+ _gAVPointCloudDataTrace
+ _gAVPortraitEffectsMatteTrace
+ _gAVSemanticSegmentationMatteTrace
+ _gAVSmartStyleSettingsTrace
+ _gAVVirtualCaptureCardTrace
+ _gGMFigKTraceEnabled
+ _gSpatialAudioMetadataSampleGeneratorTrace
+ _getCameraCaptureLegacyLog.cameraCaptureLegacyLog
+ _getCameraCaptureLegacyLog.cameraCaptureLegacyLogOnceToken
+ _kCMMetadataIdentifier_QuickTimeMetadataDetectedCatHead
+ _kCMMetadataIdentifier_QuickTimeMetadataDetectedDogHead
+ _kCVPixelBufferVersatileBayerKey_BayerPattern
+ _kFigCaptureDeferredPhotoProcessorNotificationPayloadKey_PhotoLibraryThumbnails
+ _kFigCaptureSessionNotification_DidRunDeferredStart
+ _kFigCaptureSessionNotification_WillRunDeferredStart
+ _kFigCaptureSessionProperty_RunDeferredStartWhenNeeded
+ _kFigCaptureSessionVideoConnectionProperty_VideoRotationDegrees
+ _kFigCaptureSessionVideoDataSinkProperty_PreservesDynamicHDRMetadata
+ _kFigCaptureSourceAttributeKey_AVCaptureSessionPresetCompressionSettings
+ _kFigCaptureSourceAttributeKey_AVH264Settings
+ _kFigCaptureSourceAttributeKey_AVHEVCSettings
+ _kFigCaptureSourceAttributeKey_DICOM
+ _kFigCaptureSourceAttributeKey_FrameRatesForSystemPressureLevel
+ _kFigCaptureSourceAttributeKey_SupportedOptionalFaceDetectionFeatures
+ _kFigCaptureSourceAttributeKey_ThrottleFrameRatesWithDepthDisabled
+ _kFigCaptureSourceAttributeKey_WhiteBalanceCalibrations
+ _kFigCaptureSourceExposureOperationKey_IsDefaultRect
+ _kFigCaptureSourceLensSmudgeDetectionStatusChangedPayloadKey_Status
+ _kFigCaptureSourceNotification_LensSmudgeDetectionStatusChanged
+ _kFigCaptureSourceProperty_SimulatedAperture
+ _kIOSurfaceVersatileSenselArrayPattern
+ _kdebug_trace
+ _objc_msgSend$_addObserversForConnectionDevice:
+ _objc_msgSend$_checkEligibilityForEffect:
+ _objc_msgSend$_defaultPhotoDimensionsWithHighResolutionCaptureEnabled:
+ _objc_msgSend$_defaultRectForExposurePointOfInterest:
+ _objc_msgSend$_defaultRectForFocusPointOfInterest:focusMode:
+ _objc_msgSend$_delegateWrapperForSettingsID:
+ _objc_msgSend$_didRunDeferredStart
+ _objc_msgSend$_indexOfAudioLevelChannel:
+ _objc_msgSend$_isDeviceInputInSpatialAudioMode:
+ _objc_msgSend$_metadataConstantValueToName:
+ _objc_msgSend$_minExposureRectOfInterestSizeForFormat:
+ _objc_msgSend$_minFocusRectOfInterestSizeForFormat:
+ _objc_msgSend$_recommendedAudioOutputSettingsForConnection:sourceSettings:fileType:spatialAudioChannelLayoutTag:
+ _objc_msgSend$_removeMetadataObjectTypeFromMetadataObjectTypes:
+ _objc_msgSend$_removeMetadataObjectTypesFromMetadataObjectTypes:
+ _objc_msgSend$_removeObserversForConnectionDevice:
+ _objc_msgSend$_requireMultiCamSupportedFormatsForVideoDevices
+ _objc_msgSend$_resetCinematicVideoCaptureSupported
+ _objc_msgSend$_setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:
+ _objc_msgSend$_setSimulatedAperture:
+ _objc_msgSend$_updateCinematicVideoCaptureSceneMonitoringStatus:
+ _objc_msgSend$_updatePrimaryCaptureRectWithCamerasMountedInLandscapeOrientation:center:aspectRatio:
+ _objc_msgSend$_validateAudioConfiguration:
+ _objc_msgSend$_validateCinematicVideoConfiguration:
+ _objc_msgSend$_videoPreviewLayersContains:
+ _objc_msgSend$_willRunDeferredStart
+ _objc_msgSend$addPointer:
+ _objc_msgSend$analyzeAudioSample:
+ _objc_msgSend$cameraLensSmudgeDetectionInterval
+ _objc_msgSend$channelCount
+ _objc_msgSend$channelLayout
+ _objc_msgSend$cinematicAudioSettings
+ _objc_msgSend$cinematicVideoFocusMode
+ _objc_msgSend$compact
+ _objc_msgSend$deviceFormatForSessionPreset:device:
+ _objc_msgSend$dotString
+ _objc_msgSend$figMetadataPropertyFromMetadataItems:
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$filterWithName:
+ _objc_msgSend$focalLengthIn35mmFilmWithGeometricDistortionCorrection:
+ _objc_msgSend$getPrimaryCaptureRectWithCamerasMountedInLandscapeOrientation:center:aspectRatio:uniqueID:
+ _objc_msgSend$initWithFigLevel:factors:recommendedFrameRateRangeForPortrait:recommendedFrameRateRangeForPhotoMode:
+ _objc_msgSend$initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:photoLibraryThumbnails:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:
+ _objc_msgSend$isCameraLensSmudgeDetectionEnabled
+ _objc_msgSend$isCameraLensSmudgeDetectionSupported
+ _objc_msgSend$isCinematicVideoCaptureEnabled
+ _objc_msgSend$isCinematicVideoCaptureSupported
+ _objc_msgSend$isCinematicVideoSupported
+ _objc_msgSend$isDICOMSupported
+ _objc_msgSend$isDeferredStartEnabled
+ _objc_msgSend$isDeferredStartSupported
+ _objc_msgSend$isExposureRectOfInterestSupported
+ _objc_msgSend$isFaceTrackingSuspended
+ _objc_msgSend$isFixedFocus
+ _objc_msgSend$isFocusRectOfInterestSupported
+ _objc_msgSend$isLensSmudgeDetectionSupported
+ _objc_msgSend$isManualDeferredStartSupported
+ _objc_msgSend$isStreamingDepthOnlyPrivatelySupported
+ _objc_msgSend$metadataObjectsDelegate
+ _objc_msgSend$newTimedMetadataSampleBufferAndResetAnalyzer
+ _objc_msgSend$nonretainedObjectValue
+ _objc_msgSend$now
+ _objc_msgSend$opaqueSessionID
+ _objc_msgSend$outputRotationDegrees
+ _objc_msgSend$photoLibraryThumbnailDimensions
+ _objc_msgSend$pointerAtIndex:
+ _objc_msgSend$preferredIOBufferDuration
+ _objc_msgSend$preparesCellularRadioForNetworkConnection
+ _objc_msgSend$preservesDynamicHDRMetadata
+ _objc_msgSend$previewHeight
+ _objc_msgSend$previewWidth
+ _objc_msgSend$rawThumbnailHeight
+ _objc_msgSend$rawThumbnailWidth
+ _objc_msgSend$recommendedFrameRateRangeForPhotoMode
+ _objc_msgSend$recommendedOutputSettingsForConnection:sourceSettings:videoCodecType:fileType:isIris:outputFileURL:spatialAudioChannelLayoutTag:
+ _objc_msgSend$remoteIOOutputFormat
+ _objc_msgSend$removePointerAtIndex:
+ _objc_msgSend$requiredMetadataObjectTypesForCinematicVideoCapture
+ _objc_msgSend$resetAnalyzer
+ _objc_msgSend$sampleBufferDelegate
+ _objc_msgSend$sensitiveContentAnalyzerEnabled
+ _objc_msgSend$sensitiveContentAnalyzerXPCObject
+ _objc_msgSend$sessionDidRunDeferredStart:
+ _objc_msgSend$sessionWillRunDeferredStart:
+ _objc_msgSend$setAspectRatioForNonDestructiveCrop:
+ _objc_msgSend$setAutomaticallyRunsDeferredStart:
+ _objc_msgSend$setCinematicVideoCaptureEnabled:
+ _objc_msgSend$setCinematicVideoFocusMode:
+ _objc_msgSend$setConfiguresAppAudioSessionForBluetoothHighQualityRecording:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDeferredStartEnabled:
+ _objc_msgSend$setFaceTrackingSuspended:
+ _objc_msgSend$setFixedFocus:
+ _objc_msgSend$setLensSmudgeDetectionEnabled:
+ _objc_msgSend$setLensSmudgeDetectionInterval:
+ _objc_msgSend$setOutputRotationDegrees:
+ _objc_msgSend$setPreferredIOBufferDuration:
+ _objc_msgSend$setPreparesCellularRadioForNetworkConnection:
+ _objc_msgSend$setPreservesDynamicHDRMetadata:
+ _objc_msgSend$setPreviewRotationDegrees:
+ _objc_msgSend$setRemoteIOOutputFormat:
+ _objc_msgSend$setRotationDegrees:
+ _objc_msgSend$setSensitiveContentAnalyzerEnabled:
+ _objc_msgSend$setSensitiveContentAnalyzerXPCObject:
+ _objc_msgSend$setSpatialAudioChannelLayoutTag:
+ _objc_msgSend$setVideoRotationDegrees:
+ _objc_msgSend$spatialAudioChannelLayoutTag
+ _objc_msgSend$spiDebugDescription
+ _objc_msgSend$streamDescription
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$thumbnailContentsDelegate
+ _objc_msgSend$thumbnailHeight
+ _objc_msgSend$thumbnailWidth
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$timedMetadataSampleBufferFormatDescription
+ _objc_msgSend$videoFrameRateRangeForCinematicVideo
+ _objc_msgSend$videoRotationAngle
+ _objc_msgSend$weakObjectsPointerArray
+ _objc_msgSend$writeToFile:atomically:encoding:error:
+ _os_log_create
+ _sShutterSoundSuppressedByAirPodStemClickTimer
+ _sShutterSoundSuppressedByAirpodStemClick
+ _vpl_pointToString
+ _vpl_rectValueToString
+ _vpl_sizeToString
- +[AVCaptureDevice _checkEligiblityForEffect:]
- +[AVCaptureDevice authorizationStatusForMediaType:].cold.1
- +[AVMetadataVisualIntelligenceObject visualIntelligenceObjectWithVisualIntelligenceDictionary:input:time:]
- -[AVCaptureDevice nonDestructiveCropAspectRatio]
- -[AVCaptureDevice performReactionEffect:]
- -[AVCaptureDevice reactionEffectsActive]
- -[AVCaptureDevice reactionEffectsAvailable]
- -[AVCaptureDevice setNonDestructiveCropAspectRatio:]
- -[AVCaptureFigVideoDevice _supportedOptionalFaceDetectionFeaturesDictionary]
- -[AVCaptureFigVideoDevice nonDestructiveCropAspectRatio]
- -[AVCaptureFigVideoDevice setNonDestructiveCropAspectRatio:]
- -[AVCaptureMetadataOutput _appClipCodesCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput _barcodeCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput _detectedObjectsCollectionForSampleBuffer:input:facesArrayOut:need180DegreeMetadataTransform:]
- -[AVCaptureMetadataOutput _emitCollections:].cold.1
- -[AVCaptureMetadataOutput _eyeReliefResultCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput _faceIDReadinessCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput _legacyFaceCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput _lumaHistogramDataCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput _motionToWakeCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput _offlineVISMotionCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput _sceneClassificationCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput _textRegionsCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput _trackedFacesCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput _visualIntelligenceCollectionForSampleBuffer:input:]
- -[AVCaptureMetadataOutput isVisualIntelligenceMetadataObjectTypeAvailable]
- -[AVCaptureMetadataOutput isVisualIntelligenceMetadataSupported]
- -[AVCaptureMetadataOutput setVisualIntelligenceMetadataObjectTypeAvailable:]
- -[AVCaptureOutput _recommendedAudioOutputSettingsForConnection:sourceSettings:fileType:]
- -[AVCaptureOutput recommendedOutputSettingsForConnection:sourceSettings:videoCodecType:fileType:isIris:outputFileURL:]
- -[AVCaptureOutput recommendedOutputSettingsForConnection:sourceSettings:videoCodecType:fileType:isIris:outputFileURL:].cold.1
- -[AVCapturePhoto initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:]
- -[AVCapturePhoto portraitEffectsMatte].cold.1
- -[AVCaptureSession _createFigCaptureSession].cold.2
- -[AVCaptureSession areControlsSupported]
- -[AVCaptureSlider setValueFormat:]
- -[AVCaptureSlider valueFormat]
- -[AVCaptureStillImageOutput highResolutionStillImageOutputEnabledChangeCausesCaptureSessionRestart]
- -[AVCaptureStillImageOutput setSquareCropEnabled:]
- -[AVCaptureStillImageOutput squareCropEnabled]
- -[AVCaptureSystemPressureState initWithFigLevel:factors:recommendedFrameRateRangeForPortrait:]
- -[AVCaptureSystemPressureStateInternal initWithFigLevel:factors:recommendedFrameRateRangeForPortrait:]
- -[AVMetadataVisualIntelligenceObject copyWithZone:]
- -[AVMetadataVisualIntelligenceObject dealloc]
- -[AVMetadataVisualIntelligenceObject description]
- -[AVMetadataVisualIntelligenceObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:]
- -[AVMetadataVisualIntelligenceObject initVisualIntelligenceObjectWithVisualIntelligenceDictionary:time:sourceCaptureInput:]
- -[AVMetadataVisualIntelligenceObject objectDetectionCachedResult]
- -[AVMetadataVisualIntelligenceObject objectDetectionUprightExifOrientation]
- -[AVMetadataVisualIntelligenceObject visualIntelligence]
- -[AVOfflineVideoStabilizer _copyStabilizedSampleBuffer:].cold.1
- -[AVOfflineVideoStabilizer _setupVISProcessor].cold.4
- -[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:transitionPercentComplete:]
- GCC_except_table112
- GCC_except_table119
- GCC_except_table121
- GCC_except_table133
- GCC_except_table135
- GCC_except_table137
- GCC_except_table138
- GCC_except_table143
- GCC_except_table144
- GCC_except_table146
- GCC_except_table150
- GCC_except_table152
- GCC_except_table153
- GCC_except_table154
- GCC_except_table156
- GCC_except_table158
- GCC_except_table16
- GCC_except_table164
- GCC_except_table165
- GCC_except_table166
- GCC_except_table175
- GCC_except_table178
- GCC_except_table186
- GCC_except_table188
- GCC_except_table225
- GCC_except_table228
- GCC_except_table247
- GCC_except_table256
- GCC_except_table259
- GCC_except_table261
- GCC_except_table264
- GCC_except_table269
- GCC_except_table273
- GCC_except_table292
- GCC_except_table299
- GCC_except_table305
- GCC_except_table313
- GCC_except_table32
- GCC_except_table327
- GCC_except_table350
- GCC_except_table360
- GCC_except_table37
- GCC_except_table372
- GCC_except_table387
- GCC_except_table390
- GCC_except_table417
- GCC_except_table421
- GCC_except_table43
- GCC_except_table432
- GCC_except_table440
- GCC_except_table447
- GCC_except_table45
- GCC_except_table453
- GCC_except_table465
- GCC_except_table472
- GCC_except_table477
- GCC_except_table482
- GCC_except_table496
- GCC_except_table519
- GCC_except_table530
- GCC_except_table540
- GCC_except_table554
- GCC_except_table570
- GCC_except_table589
- GCC_except_table606
- GCC_except_table609
- GCC_except_table638
- GCC_except_table640
- GCC_except_table642
- GCC_except_table665
- GCC_except_table677
- GCC_except_table679
- GCC_except_table681
- GCC_except_table689
- GCC_except_table732
- GCC_except_table736
- GCC_except_table78
- GCC_except_table788
- GCC_except_table80
- GCC_except_table81
- GCC_except_table82
- GCC_except_table83
- GCC_except_table831
- GCC_except_table86
- GCC_except_table87
- GCC_except_table88
- GCC_except_table97
- _AVCaptureGetFrameworkRadarComponentName
- _AVCaptureReactionTypeVictory
- _AVCaptureVideoPreviewLayerDeviceInputSimulatedApertureChangedContext
- _AVMetadataObjectTypeVisualIntelligence
- _D16
- _D17
- _D27
- _D28
- _D321
- _D331_D331p
- _D37
- _D38
- _D421
- _D431
- _D47
- _D48
- _D52g
- _D53g
- _D63
- _D64
- _D73
- _D74
- _D93
- _D94
- _FigDepthRotateCalibrationData
- _FigSignalErrorAt
- _J171_J172
- _J317_J318_J320_J321_J317x_J318x_J320x_J321x
- _J517_J518_J522_J523_J517x_J518x_J522x_J523x
- _N84_N841
- _OBJC_CLASS_$_AVCaptureReactionEffectStatus
- _OBJC_CLASS_$_AVMetadataVisualIntelligenceObject
- _OBJC_CLASS_$_NSHashTable
- _OBJC_IVAR_$_AVCaptureConnectionInternal.clientUsesVideoRotationAngleAPI
- _OBJC_IVAR_$_AVCaptureFigVideoDevice._h264EncoderLimitations
- _OBJC_IVAR_$_AVCaptureFigVideoDevice._hevcEncoderSettings
- _OBJC_IVAR_$_AVCaptureFigVideoDevice._sessionPresetCompressionSettings
- _OBJC_IVAR_$_AVCaptureFigVideoDevice._supportedOptionalFaceDetectionFeatures
- _OBJC_IVAR_$_AVCaptureMetadataOutputInternal.visualIntelligenceObjectTypeAvailable
- _OBJC_IVAR_$_AVCaptureStillImageOutputInternal.squareCropEnabled
- _OBJC_IVAR_$_AVMetadataVisualIntelligenceObject._visualIntelligence
- _OBJC_IVAR_$_AVSpatialOverCaptureVideoPreviewLayer._primaryCaptureRectTransitionPercentComplete
- _OBJC_METACLASS_$_AVCaptureReactionEffectStatus
- _OBJC_METACLASS_$_AVMetadataVisualIntelligenceObject
- _OUTLINED_FUNCTION_12
- __OBJC_$_CLASS_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification)
- __OBJC_$_CLASS_METHODS_AVMetadataVisualIntelligenceObject
- __OBJC_$_INSTANCE_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification)
- __OBJC_$_INSTANCE_METHODS_AVMetadataVisualIntelligenceObject
- __OBJC_$_INSTANCE_VARIABLES_AVMetadataVisualIntelligenceObject
- __OBJC_$_PROP_LIST_AVMetadataVisualIntelligenceObject
- __OBJC_CLASS_PROTOCOLS_$_AVMetadataVisualIntelligenceObject
- __OBJC_CLASS_RO_$_AVCaptureReactionEffectStatus
- __OBJC_CLASS_RO_$_AVMetadataVisualIntelligenceObject
- __OBJC_METACLASS_RO_$_AVCaptureReactionEffectStatus
- __OBJC_METACLASS_RO_$_AVMetadataVisualIntelligenceObject
- ___104-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForWrapper:withPayload:demoof:addMetadata:]_block_invoke_2
- ___110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke_2
- ___110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke_3
- ___113-[AVCaptureStillImageOutput prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:]_block_invoke_3
- ___113-[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:transitionPercentComplete:]_block_invoke
- ___132-[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:]_block_invoke_2
- ___43-[AVCaptureFigVideoDevice setExposureMode:]_block_invoke_2
- ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke.421
- ___54+[AVCaptureDevice continuityCaptureCameraCapabilities]_block_invoke_3
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_10
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_11
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_12
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_13
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_14
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_15
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_16
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_17
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_17.cold.1
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_18
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_19
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_20
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_21
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_22
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_23
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_24
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_25
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_26
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_27
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_28
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_29
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_30
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_31
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_32
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_33
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_34
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_35
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_36
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_37
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_38
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_39
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_40
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_41
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_42
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_9
- ___56-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]_block_invoke_2
- ___56-[AVCaptureFigVideoDevice nonDestructiveCropAspectRatio]_block_invoke
- ___58-[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:]_block_invoke_2
- ___60-[AVCaptureFigVideoDevice setNonDestructiveCropAspectRatio:]_block_invoke
- ___63+[AVCaptureDevice requestAccessForMediaType:completionHandler:]_block_invoke_2
- ___66-[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:]_block_invoke_2
- ___67-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:]_block_invoke.307
- ___67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.294
- ___67-[AVCaptureFigVideoDevice setExposureTargetBias:completionHandler:]_block_invoke_2
- ___72-[AVCaptureFigVideoDevice chromaticityValuesForDeviceWhiteBalanceGains:]_block_invoke_3
- ___72-[AVCapturePhotoOutput setPreparedPhotoSettingsArray:completionHandler:]_block_invoke_3
- ___74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.598
- ___74-[AVCaptureProprietaryDefaultsSingleton imageForKey:fillWidth:fillHeight:]_block_invoke.cold.5
- ___77-[AVCaptureVideoPreviewLayer observeValueForKeyPath:ofObject:change:context:]_block_invoke_2
- ___80-[AVCaptureFigVideoDevice setFocusModeLockedWithLensPosition:completionHandler:]_block_invoke_3
- ___83-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke_3
- ___85-[AVCapturePhotoOutput _handleStillImageCompleteNotification:withPayload:forRequest:]_block_invoke_2
- ___85-[AVCapturePhotoOutput _handleStillImageCompleteNotification:withPayload:forRequest:]_block_invoke_3
- ___86-[AVCaptureMovieFileOutput handleDidStartRecordingNotificationForWrapper:withPayload:]_block_invoke_2
- ___94-[AVCapturePhotoOutput commitMomentCaptureWithUniqueID:toMovieRecordingWithSettings:delegate:]_block_invoke_3
- ___98-[AVCaptureFigVideoDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:]_block_invoke_3
- ___AVControlCenterModulesPrewarm_block_invoke.439
- ___block_descriptor_220_e8_32o40o48o56o64o72o80o88o96o104r_e51_v16?0"<AVCaptureDeferredPhotoProcessorDelegate>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r104l8s96l8
- ___block_descriptor_305_e8_32o40o48r56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r296r_e5_v8?0ls32l8s40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8r280l8r288l8r296l8
- ___block_descriptor_40_e8_32b_e8_v12?0B8ls32l8
- ___block_descriptor_40_e8_32b_e8_v12?0C8ls32l8
- ___block_descriptor_65_e8_32o40o48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_74_e8_32o40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_80_e8_32o40o48o56r64r72r_e5_v8?0lr56l8s32l8r64l8s40l8s48l8r72l8
- ___block_literal_global.119
- ___block_literal_global.122
- ___block_literal_global.1320
- ___block_literal_global.1327
- ___block_literal_global.137
- ___block_literal_global.140
- ___block_literal_global.155
- ___block_literal_global.178
- ___block_literal_global.183
- ___block_literal_global.212
- ___block_literal_global.257
- ___block_literal_global.396
- ___block_literal_global.407
- ___block_literal_global.415
- ___block_literal_global.420
- ___block_literal_global.432
- ___block_literal_global.442
- ___block_literal_global.443
- ___block_literal_global.469
- ___block_literal_global.481
- ___block_literal_global.523
- ___block_literal_global.528
- ___block_literal_global.531
- ___block_literal_global.831
- ___block_literal_global.836
- ___block_literal_global.90
- ___stack_chk_fail
- ___stack_chk_guard
- _avcc_prefixedSignalPreferenceKeyForBundleID
- _fig_log_get_emitter
- _fvd_cgRectDictionaryForCenterAndSize
- _kFigCaptureSampleBufferAttachmentKey_VisualIntelligence
- _kFigCaptureSampleBufferAttachmentKey_VisualIntelligenceObjectDetectionCachedResult
- _kFigCaptureSampleBufferAttachmentKey_VisualIntelligenceObjectDetectionUprightExifOrientation
- _kFigCaptureSessionPreviewSinkProperty_SimulatedAperture
- _kFigCaptureSessionVideoConnectionProperty_VideoOrientation
- _kFigCaptureSourceProperty_AVCaptureSessionPresetCompressionSettings
- _kFigCaptureSourceProperty_AVH264Settings
- _kFigCaptureSourceProperty_AVHEVCSettings
- _kFigCaptureSourceProperty_SupportedOptionalFaceDetectionFeatures
- _kFigCaptureSourceProperty_WhiteBalanceCalibrations
- _kFigMetadataIdentifier_QuickTimeMetadataDetectedCatHead
- _kFigMetadataIdentifier_QuickTimeMetadataDetectedDogHead
- _kFigMetadataIdentifier_QuickTimeMetadataVisualIntelligence
- _metadataIdentifiersForMetadataObjectTypes:.sVisualIntelligenceMetadataConstantToMetadataIdentifierDictionary
- _metadataObjectTypesForMetadataIdentifiers:.sVisualIntelligenceMetadataIdentifierToMetadataConstantDictionary
- _objc_msgSend$_appClipCodesCollectionForSampleBuffer:input:
- _objc_msgSend$_barcodeCollectionForSampleBuffer:input:
- _objc_msgSend$_checkEligiblityForEffect:
- _objc_msgSend$_detectedObjectsCollectionForSampleBuffer:input:facesArrayOut:need180DegreeMetadataTransform:
- _objc_msgSend$_eyeReliefResultCollectionForSampleBuffer:input:
- _objc_msgSend$_faceIDReadinessCollectionForSampleBuffer:input:
- _objc_msgSend$_figMetadataPropertyFromMetadataItems:
- _objc_msgSend$_legacyFaceCollectionForSampleBuffer:input:
- _objc_msgSend$_lumaHistogramDataCollectionForSampleBuffer:input:
- _objc_msgSend$_motionToWakeCollectionForSampleBuffer:input:
- _objc_msgSend$_offlineVISMotionCollectionForSampleBuffer:input:
- _objc_msgSend$_recommendedAudioOutputSettingsForConnection:sourceSettings:fileType:
- _objc_msgSend$_sceneClassificationCollectionForSampleBuffer:input:
- _objc_msgSend$_setPrimaryCaptureRectAspectRatio:centerPoint:transitionPercentComplete:
- _objc_msgSend$_supportedOptionalFaceDetectionFeaturesDictionary
- _objc_msgSend$_textRegionsCollectionForSampleBuffer:input:
- _objc_msgSend$_trackedFacesCollectionForSampleBuffer:input:
- _objc_msgSend$_visualIntelligenceCollectionForSampleBuffer:input:
- _objc_msgSend$availableReactionTypes
- _objc_msgSend$canAddConnection:
- _objc_msgSend$highResolutionStillImageOutputEnabledChangeCausesCaptureSessionRestart
- _objc_msgSend$initVisualIntelligenceObjectWithVisualIntelligenceDictionary:time:sourceCaptureInput:
- _objc_msgSend$initWithFigLevel:factors:recommendedFrameRateRangeForPortrait:
- _objc_msgSend$initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:
- _objc_msgSend$isQuadraHighResStillImageSupported
- _objc_msgSend$isVisualIntelligenceMetadataSupported
- _objc_msgSend$localizedValueFormat
- _objc_msgSend$minusHashTable:
- _objc_msgSend$objectDetectionCachedResult
- _objc_msgSend$outputOrientation
- _objc_msgSend$performEffectForReaction:
- _objc_msgSend$recommendedOutputSettingsForConnection:sourceSettings:videoCodecType:fileType:isIris:outputFileURL:
- _objc_msgSend$setLocalizedValueFormat:
- _objc_msgSend$setMetadataObjectTypes:
- _objc_msgSend$setNonDestructiveCropAspectRatio:
- _objc_msgSend$setOutputOrientation:
- _objc_msgSend$setPreviewOrientation:
- _objc_msgSend$setQuadraHighResCaptureEnabled:
- _objc_msgSend$supportsQuadraHighResolutionStillImageOutput
- _objc_msgSend$visualIntelligence
- _objc_msgSend$visualIntelligenceObjectWithVisualIntelligenceDictionary:input:time:
- _objc_msgSend$weakObjectsHashTable
CStrings:
+ "\t%@ -> %@ [label=\"%@\\nenabled: %s\\nactive: %s\\norientation: %d\\nmirrored: %d\",color=%s];\n"
+ "\t%@ -> %@ [label=\"delegate\",style=dotted];\n"
+ "\t%@ -> %@ [label=\"delegateOverride\",style=dotted];\n"
+ "\t%@ [shape=box,label=\"%@\",color=black];\n"
+ "\t%@ [shape=box,label=\"%@\\n%p\",color=%@];\n"
+ "\t%@ [shape=circle,label=\"%@\\n%p\",color=black];\n"
+ "\tlabel=\"%@\\n%@\\n%@\\n%@\";\n"
+ "\tranksep=1.5;nodesep=1;\n"
+ " (modes:"
+ " standard"
+ "%@ Recommended Frame Rate for Portrait:%.0f-%.0f, Recommended Frame Rate for Photo Mode:%.0f-%.0f"
+ "%@AVCaptureSession"
+ "%@\\n%p"
+ "%c"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "'%@' %dx%d, %dfps"
+ "( chanIdx >= 0 ) && ( ( chanIdx * 2 ) < _internal->audioChannelLevels.count )"
+ "( sceneMonitoringStatus != ((void *)0) ) || backToNormal"
+ "(%g,%g)"
+ "(original) "
+ "(spatialAudioChannelLayoutTag == kAudioChannelLayoutTag_Unknown) || spatialAudioChannelLayoutTagSpecifiesSpatial || spatialAudioChannelLayoutTagSpecifiesStereo"
+ "***Original*** "
+ "***OverCapture*** "
+ "+[AVCaptureCoreAnalyticsReporter clientApplicationIDType:]"
+ "+[AVCaptureCoreAnalyticsReporter initialize]"
+ "+[AVCaptureDevice _backgroundBlurApertureChanged:]"
+ "+[AVCaptureDevice _backgroundReplacementEnabledChanged:]"
+ "+[AVCaptureDevice _backgroundReplacementURLBookmarkChanged:]"
+ "+[AVCaptureDevice _reactionTriggered:]"
+ "+[AVCaptureDevice _reactionsInProgressChangedByControlCenter:]"
+ "+[AVCaptureDevice _studioLightingIntensityChanged:]"
+ "+[AVCaptureDevice activeMicrophoneMode]"
+ "+[AVCaptureDevice authorizationStatusForMediaType:]"
+ "+[AVCaptureDevice backgroundBlurAperture]"
+ "+[AVCaptureDevice backgroundBlurControlMode]"
+ "+[AVCaptureDevice backgroundReplacementPixelBuffer]"
+ "+[AVCaptureDevice backgroundReplacementURL]"
+ "+[AVCaptureDevice centerStageControlMode]"
+ "+[AVCaptureDevice continuityCaptureCameraCapabilities]_block_invoke"
+ "+[AVCaptureDevice continuityCaptureCameraCapabilities]_block_invoke_2"
+ "+[AVCaptureDevice isBackgroundBlurEnabled]"
+ "+[AVCaptureDevice isBackgroundReplacementEnabled]"
+ "+[AVCaptureDevice isCenterStageEnabled]"
+ "+[AVCaptureDevice isPortraitEffectEnabled]"
+ "+[AVCaptureDevice isStudioLightEnabled]"
+ "+[AVCaptureDevice portraitEffectStudioLightQuality]"
+ "+[AVCaptureDevice preferredMicrophoneMode]"
+ "+[AVCaptureDevice reactionEffectGesturesEnabled]"
+ "+[AVCaptureDevice reactionEffectsEnabled]"
+ "+[AVCaptureDevice requestAccessForMediaType:completionHandler:]"
+ "+[AVCaptureDevice requestAccessForMediaType:completionHandler:]_block_invoke"
+ "+[AVCaptureDevice setBackgroundBlurAperture:]"
+ "+[AVCaptureDevice setBackgroundBlurControlMode:]"
+ "+[AVCaptureDevice setBackgroundReplacementEnabled:]"
+ "+[AVCaptureDevice setBackgroundReplacementPixelBuffer:]"
+ "+[AVCaptureDevice setBackgroundReplacementURL:]"
+ "+[AVCaptureDevice setCenterStageControlMode:]"
+ "+[AVCaptureDevice setControlCenterVideoEffectUnavailableReasonsForVideoEffect:reasons:]"
+ "+[AVCaptureDevice setPortraitEffectStudioLightQuality:]"
+ "+[AVCaptureDevice setStudioLightingControlMode:]"
+ "+[AVCaptureDevice setStudioLightingIntensity:]"
+ "+[AVCaptureDevice studioLightingControlMode]"
+ "+[AVCaptureDevice studioLightingIntensity]"
+ "+[AVCaptureFigVideoDevice _newFigCaptureSources]"
+ "+[AVCaptureFigVideoDevice _prioritizedDeviceList:]"
+ "+[AVCapturePhotoOutput DNGPhotoDataRepresentationForRawSampleBuffer:previewPhotoSampleBuffer:]"
+ "+[AVCapturePhotoOutput JPEGPhotoDataRepresentationForJPEGSampleBuffer:previewPhotoSampleBuffer:]"
+ "+[AVCaptureSession _writeDotStringToFile]"
+ "+[AVCaptureStillImageOutput jpegStillImageNSDataRepresentation:]"
+ "+[AVCaptureStillImageOutput jpegStillImageNSDataRepresentationForSurface:size:metadata:]"
+ "+[AVCaptureStillImageOutput maxStillImageJPEGDataSize]_block_invoke"
+ "+[AVDepthData depthDataFromDictionaryRepresentation:error:]"
+ "+[AVExternalStorageDevice(AVExternalStorageDeviceAuthorization) authorizationStatus]"
+ "+[AVExternalStorageDevice(AVExternalStorageDeviceAuthorization) requestAccessWithCompletionHandler:]"
+ "+[AVExternalStorageDeviceDiscoverySession sharedSession]_block_invoke"
+ "+[AVFlashlight hasFlashlight]"
+ "+[AVPortraitEffectsMatte portraitEffectsMatteFromDictionaryRepresentation:error:]"
+ "+[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:]"
+ "+[AVVirtualCaptureCard sharedVirtualCaptureCard]_block_invoke"
+ ", cinematic"
+ ", enhanced"
+ ", extended"
+ ", preview"
+ ", supports Cinematic Video"
+ ", supports Smudge Detection"
+ "-%.0f.dot"
+ "-%@"
+ "-[AVCDOSDataOutputStorage hasAllExpectedSynchronizedDataForLeaderTimestamp:]"
+ "-[AVCDOSDataOutputStorage updateDelegateOverrideCallbackQueueQOSClass:]"
+ "-[AVCaptureAudioDataOutput _handleConfigurationLiveEventForID:updatedFormatDescription:]"
+ "-[AVCaptureAudioDataOutput _handleLocalQueueMessage:]"
+ "-[AVCaptureAudioDataOutput _handleNotification:payload:]"
+ "-[AVCaptureAudioDataOutput _handleRemoteQueueOperation:]"
+ "-[AVCaptureAudioDataOutput _handleSampleBufferEventForSampleBuffer:]"
+ "-[AVCaptureAudioDataOutput _updateRemoteQueue:]_block_invoke"
+ "-[AVCaptureAudioDataOutput setDelegateOverride:delegateOverrideCallbackQueue:]"
+ "-[AVCaptureAudioDataOutput setSampleBufferDelegate:queue:]"
+ "-[AVCaptureCameraCalibrationDataOutput _handleLocalQueueMessage:]"
+ "-[AVCaptureCameraCalibrationDataOutput _handleNotification:payload:]"
+ "-[AVCaptureCameraCalibrationDataOutput _handleRemoteQueueOperation:]"
+ "-[AVCaptureCameraCalibrationDataOutput _processSampleBuffer:]"
+ "-[AVCaptureCameraCalibrationDataOutput _updateRemoteQueue:]_block_invoke"
+ "-[AVCaptureCameraCalibrationDataOutput setDelegate:callbackQueue:]"
+ "-[AVCaptureCameraCalibrationDataOutput setDelegateOverride:delegateOverrideCallbackQueue:]"
+ "-[AVCaptureConnection _setVideoMinFrameDuration:]"
+ "-[AVCaptureConnection _setVideoRotationAngle:]"
+ "-[AVCaptureConnection _updateActiveVideoStabilizationMode:bumpChangeSeed:]"
+ "-[AVCaptureConnection _updatePropertiesForFormat:]"
+ "-[AVCaptureConnection dealloc]"
+ "-[AVCaptureConnection figCaptureConnectionConfigurationForSessionPreset:allConnections:]"
+ "-[AVCaptureConnection setAutomaticallyAdjustsVideoMirroring:]"
+ "-[AVCaptureConnection setEnabled:]"
+ "-[AVCaptureConnection setEnablesVideoStabilizationWhenAvailable:]"
+ "-[AVCaptureConnection setPreferredVideoStabilizationMode:]"
+ "-[AVCaptureConnection setVideoMaxFrameDuration:]"
+ "-[AVCaptureConnection setVideoMinFrameDuration:]"
+ "-[AVCaptureConnection setVideoMirrored:]"
+ "-[AVCaptureConnection setVideoOrientation:]"
+ "-[AVCaptureConnection updateAudioChannelsArray]"
+ "-[AVCaptureControlsOverlay _sendControlsIsolated]"
+ "-[AVCaptureControlsOverlay _sendControlsIsolated]_block_invoke"
+ "-[AVCaptureControlsOverlay _updateControlIsolated:]"
+ "-[AVCaptureControlsOverlay _updateControlIsolated:]_block_invoke"
+ "-[AVCaptureControlsOverlay cameraOverlayConnection:didChangeActiveControlIdentifier:]"
+ "-[AVCaptureControlsOverlay cameraOverlayConnection:didChangeFocusLocked:]"
+ "-[AVCaptureControlsOverlay cameraOverlayConnection:didChangeInterfaceReduced:]"
+ "-[AVCaptureControlsOverlay cameraOverlayConnection:didChangeOverlayVisible:activeControlIdentifier:]"
+ "-[AVCaptureControlsOverlay cameraOverlayConnection:didChangeStatus:]"
+ "-[AVCaptureDataOutputDelegateCallbackHelper updateLocalQueue:handler:]"
+ "-[AVCaptureDataOutputDelegateCallbackHelper updateRemoteQueueReceiver:handler:]"
+ "-[AVCaptureDataOutputSynchronizer _adjustSynchronizedDataTimestamps]"
+ "-[AVCaptureDataOutputSynchronizer _appendSynchronizedData:forCaptureOutput:]"
+ "-[AVCaptureDataOutputSynchronizer _dispatchRipenedSynchronizedData]"
+ "-[AVCaptureDataOutputSynchronizer _dispatchSynchronizedDataWithTimestamp:]"
+ "-[AVCaptureDataOutputSynchronizer _dispatchSynchronizedDataWithTimestamp:]_block_invoke"
+ "-[AVCaptureDataOutputSynchronizer _overrideDataOutputDelegatesForDelegateCallbackQueue:]"
+ "-[AVCaptureDataOutputSynchronizer cameraCalibrationDataOutput:didDropCameraCalibrationDataAtTimestamp:connection:reason:]"
+ "-[AVCaptureDataOutputSynchronizer cameraCalibrationDataOutput:didOutputCameraCalibrationData:timestamp:connection:]"
+ "-[AVCaptureDataOutputSynchronizer captureOutput:didDropSampleBuffer:fromConnection:]"
+ "-[AVCaptureDataOutputSynchronizer captureOutput:didOutputMetadataObjectCollections:fromConnection:]"
+ "-[AVCaptureDataOutputSynchronizer captureOutput:didOutputSampleBuffer:fromConnection:]"
+ "-[AVCaptureDataOutputSynchronizer depthDataOutput:didDropDepthData:timestamp:connection:reason:]"
+ "-[AVCaptureDataOutputSynchronizer depthDataOutput:didOutputDepthData:timestamp:connection:]"
+ "-[AVCaptureDataOutputSynchronizer initWithDataOutputs:]"
+ "-[AVCaptureDataOutputSynchronizer pointCloudDataOutput:didDropPointCloudData:timestamp:connection:reason:]"
+ "-[AVCaptureDataOutputSynchronizer pointCloudDataOutput:didOutputPointCloudData:timestamp:connection:]"
+ "-[AVCaptureDataOutputSynchronizer setDelegate:queue:]"
+ "-[AVCaptureDataOutputSynchronizer visionDataOutput:didDropVisionDataPixelBufferForTimestamp:connection:reason:]"
+ "-[AVCaptureDataOutputSynchronizer visionDataOutput:didOutputVisionDataPixelBuffer:timestamp:connection:]"
+ "-[AVCaptureDeferredPhotoProcessor _establishServerConnection]"
+ "-[AVCaptureDeferredPhotoProcessor _executeBlockOnProcessorQueueSync:]_block_invoke"
+ "-[AVCaptureDeferredPhotoProcessor _handleDidFinishProcessingPhotoProxyNotificationWithPayload:forRequest:]"
+ "-[AVCaptureDeferredPhotoProcessor _handleNotification:payload:]"
+ "-[AVCaptureDeferredPhotoProcessor _handleServerConnectionDiedAndRequestsWillBeReenqueued]"
+ "-[AVCaptureDeferredPhotoProcessor _handleServerConnectionDiedSendingClientNotification:]"
+ "-[AVCaptureDeferredPhotoProcessor _handleWillAbortProcessingDueToPriorityInversion]"
+ "-[AVCaptureDeferredPhotoSettings initWithCoder:]"
+ "-[AVCaptureDepthDataOutput _handleLocalQueueMessage:]"
+ "-[AVCaptureDepthDataOutput _handleNotification:payload:]"
+ "-[AVCaptureDepthDataOutput _handleRemoteQueueOperation:]"
+ "-[AVCaptureDepthDataOutput _processSampleBuffer:]"
+ "-[AVCaptureDepthDataOutput _updateRemoteQueue:]_block_invoke"
+ "-[AVCaptureDepthDataOutput observeValueForKeyPath:ofObject:change:context:]"
+ "-[AVCaptureDepthDataOutput setDelegate:callbackQueue:]"
+ "-[AVCaptureDepthDataOutput setDelegateOverride:delegateOverrideCallbackQueue:]"
+ "-[AVCaptureDevice initProxyDeviceWithUniqueID:targetClientAuditToken:]"
+ "-[AVCaptureDevice performEffectForReaction:]"
+ "-[AVCaptureDevice updateReactionsInProgress:]"
+ "-[AVCaptureDeviceInput _authorizedToUseDeviceAndRequestIfNecessary:]"
+ "-[AVCaptureDeviceInput _handleNotification:payload:]"
+ "-[AVCaptureDeviceInput setMultichannelAudioMode:]"
+ "-[AVCaptureDeviceRotationCoordinator _handleActiveInterfaceOrientationUpdate:]"
+ "-[AVCaptureDeviceRotationCoordinator _handleSystemReferenceAngleDidChangeNotification:]"
+ "-[AVCaptureDeviceRotationCoordinator _updateVideoRotationAngleForHorizonLevelPreview]"
+ "-[AVCaptureDeviceRotationCoordinator dealloc]"
+ "-[AVCaptureDeviceRotationCoordinator handleVideoPreviewLayerDidBecomeVisibleNotification:]"
+ "-[AVCaptureDeviceRotationCoordinator initWithDevice:previewLayer:]"
+ "-[AVCaptureDeviceRotationCoordinator layer:didBecomeVisible:]"
+ "-[AVCaptureFigAudioDevice _copyFigCaptureSourceProperty:]_block_invoke"
+ "-[AVCaptureFigAudioDevice _handleNotification:payload:]"
+ "-[AVCaptureFigAudioDevice _initWithFigCaptureSource:]"
+ "-[AVCaptureFigAudioDevice audioInputDeviceLocalizedNameDidChangeHandler:]_block_invoke"
+ "-[AVCaptureFigAudioDevice audioInputDeviceLocalizedNameDidChangeHandler:]_block_invoke_2"
+ "-[AVCaptureFigAudioDevice deviceClock]"
+ "-[AVCaptureFigVideoDevice _checkTCCAccess]_block_invoke"
+ "-[AVCaptureFigVideoDevice _copyFigCaptureSourceProperty:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _defaultRectForExposurePointOfInterest:]"
+ "-[AVCaptureFigVideoDevice _defaultRectForFocusPointOfInterest:focusMode:]"
+ "-[AVCaptureFigVideoDevice _drainManualControlRequestQueue:]"
+ "-[AVCaptureFigVideoDevice _handleManualControlCompletionForRequestQueue:withPayload:]"
+ "-[AVCaptureFigVideoDevice _handleNotification:payload:]"
+ "-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2"
+ "-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3"
+ "-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_8"
+ "-[AVCaptureFigVideoDevice _incrementObserverCountForHighFrequencyProperty:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _incrementObserverCountForHighFrequencyProperty:]_block_invoke_2"
+ "-[AVCaptureFigVideoDevice _initWithFigCaptureSource:isProxy:]"
+ "-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_22"
+ "-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDuration:]"
+ "-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDuration:]"
+ "-[AVCaptureFigVideoDevice _setAdjustingExposure:]"
+ "-[AVCaptureFigVideoDevice _setAdjustingExposure:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]"
+ "-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _setExposureWithMode:duration:ISO:requestID:newMaxFrameDuration:]"
+ "-[AVCaptureFigVideoDevice _setFigCaptureSourcePixelBufferProperty:withValue:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _setFigCaptureSourceProperty:withValue:cacheOnly:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _setFocusWithMode:lensPosition:requestID:]"
+ "-[AVCaptureFigVideoDevice _setWhiteBalanceWithMode:gains:requestID:]"
+ "-[AVCaptureFigVideoDevice _updateBackgroundBlurAperture:]"
+ "-[AVCaptureFigVideoDevice _updateBackgroundReplacementPixelBuffer:]"
+ "-[AVCaptureFigVideoDevice _updateGesturesEnabled:]"
+ "-[AVCaptureFigVideoDevice _updatePortraitEffectStudioLightQuality:]"
+ "-[AVCaptureFigVideoDevice _updateStudioLightingIntensity:]"
+ "-[AVCaptureFigVideoDevice _updateSuppressedGesturesEnabled:]"
+ "-[AVCaptureFigVideoDevice addCMIOExtensionPropertyValueChangeHandler:]_block_invoke"
+ "-[AVCaptureFigVideoDevice availableBoxedMetadataFormatDescriptions]"
+ "-[AVCaptureFigVideoDevice cancelVideoZoomRamp]"
+ "-[AVCaptureFigVideoDevice chromaticityValuesForDeviceWhiteBalanceGains:]"
+ "-[AVCaptureFigVideoDevice deviceType]"
+ "-[AVCaptureFigVideoDevice deviceWhiteBalanceGains]"
+ "-[AVCaptureFigVideoDevice documentSceneConfidence]"
+ "-[AVCaptureFigVideoDevice faceRectangle]_block_invoke"
+ "-[AVCaptureFigVideoDevice grayWorldDeviceWhiteBalanceGains]"
+ "-[AVCaptureFigVideoDevice initProxyDeviceWithUniqueID:targetClientAuditToken:]"
+ "-[AVCaptureFigVideoDevice isSceneClassificationActive]"
+ "-[AVCaptureFigVideoDevice panWithTranslation:]"
+ "-[AVCaptureFigVideoDevice performOneShotFraming]"
+ "-[AVCaptureFigVideoDevice profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:]"
+ "-[AVCaptureFigVideoDevice rampExponentiallyToVideoZoomFactor:withDuration:]"
+ "-[AVCaptureFigVideoDevice rampToVideoZoomFactor:withRate:]"
+ "-[AVCaptureFigVideoDevice rampToVideoZoomFactor:withTuning:]"
+ "-[AVCaptureFigVideoDevice removeCMIOExtensionPropertyValueChangeHandler:]_block_invoke"
+ "-[AVCaptureFigVideoDevice resetFraming]"
+ "-[AVCaptureFigVideoDevice setActiveColorSpace:]"
+ "-[AVCaptureFigVideoDevice setActiveDepthDataFormat:]"
+ "-[AVCaptureFigVideoDevice setActiveDepthDataMinFrameDuration:]"
+ "-[AVCaptureFigVideoDevice setActiveFormat:]"
+ "-[AVCaptureFigVideoDevice setActiveMaxExposureDuration:]"
+ "-[AVCaptureFigVideoDevice setActiveVideoMaxFrameDuration:]"
+ "-[AVCaptureFigVideoDevice setActiveVideoMaxFrameDuration:]_block_invoke"
+ "-[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:]"
+ "-[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:]_block_invoke"
+ "-[AVCaptureFigVideoDevice setAspectRatioForNonDestructiveCrop:]"
+ "-[AVCaptureFigVideoDevice setAutoFocusRangeRestriction:]"
+ "-[AVCaptureFigVideoDevice setAutomaticallyAdjustsImageControlMode:]"
+ "-[AVCaptureFigVideoDevice setAutomaticallyAdjustsVideoHDREnabled:]"
+ "-[AVCaptureFigVideoDevice setCameraLensSmudgeDetectionEnabled:detectionInterval:]"
+ "-[AVCaptureFigVideoDevice setCenterStageFieldOfViewRestrictedToWide:]"
+ "-[AVCaptureFigVideoDevice setCenterStageMetadataDeliveryEnabled:]"
+ "-[AVCaptureFigVideoDevice setCinematicVideoFixedFocusAtPoint:focusMode:]_block_invoke"
+ "-[AVCaptureFigVideoDevice setCinematicVideoFocusAtPoint:objectID:isHardFocus:isFixedPlaneFocus:]_block_invoke"
+ "-[AVCaptureFigVideoDevice setCinematicVideoTrackingFocusAtPoint:focusMode:]_block_invoke"
+ "-[AVCaptureFigVideoDevice setCinematicVideoTrackingFocusWithDetectedObjectID:focusMode:]_block_invoke"
+ "-[AVCaptureFigVideoDevice setDeskViewCameraMode:]"
+ "-[AVCaptureFigVideoDevice setDigitalFlashMode:]"
+ "-[AVCaptureFigVideoDevice setExposureMode:]"
+ "-[AVCaptureFigVideoDevice setExposureMode:]_block_invoke"
+ "-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]"
+ "-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke_2"
+ "-[AVCaptureFigVideoDevice setExposurePointOfInterest:]"
+ "-[AVCaptureFigVideoDevice setExposureRectOfInterest:]"
+ "-[AVCaptureFigVideoDevice setExposureTargetBias:completionHandler:]"
+ "-[AVCaptureFigVideoDevice setExposureTargetBias:completionHandler:]_block_invoke"
+ "-[AVCaptureFigVideoDevice setEyeClosedDetectionEnabled:]"
+ "-[AVCaptureFigVideoDevice setEyeDetectionEnabled:]"
+ "-[AVCaptureFigVideoDevice setFaceDetectionDrivenImageProcessingEnabled:]"
+ "-[AVCaptureFigVideoDevice setFlashMode:]"
+ "-[AVCaptureFigVideoDevice setFocusMode:]"
+ "-[AVCaptureFigVideoDevice setFocusModeLockedWithLensPosition:completionHandler:]"
+ "-[AVCaptureFigVideoDevice setFocusModeLockedWithLensPosition:completionHandler:]_block_invoke_2"
+ "-[AVCaptureFigVideoDevice setFocusPointOfInterest:]"
+ "-[AVCaptureFigVideoDevice setFocusRectOfInterest:]"
+ "-[AVCaptureFigVideoDevice setGeometricDistortionCorrectionEnabled:]"
+ "-[AVCaptureFigVideoDevice setImageControlMode:]"
+ "-[AVCaptureFigVideoDevice setLowLightVideoCaptureEnabled:]"
+ "-[AVCaptureFigVideoDevice setNonDestructiveCropEnabled:]"
+ "-[AVCaptureFigVideoDevice setProvidesStortorgetMetadata:]"
+ "-[AVCaptureFigVideoDevice setSmileDetectionEnabled:]"
+ "-[AVCaptureFigVideoDevice setSmoothAutoFocusEnabled:]"
+ "-[AVCaptureFigVideoDevice setSpatialOverCaptureEnabled:]"
+ "-[AVCaptureFigVideoDevice setSubjectAreaChangeMonitoringEnabled:]"
+ "-[AVCaptureFigVideoDevice setTimeOfFlightProjectorMode:]"
+ "-[AVCaptureFigVideoDevice setTorchMode:]"
+ "-[AVCaptureFigVideoDevice setTorchModeOnWithLevel:error:]"
+ "-[AVCaptureFigVideoDevice setVariableFrameRateVideoCaptureEnabled:]"
+ "-[AVCaptureFigVideoDevice setVideoHDREnabled:]"
+ "-[AVCaptureFigVideoDevice setVideoHDRSuspended:]"
+ "-[AVCaptureFigVideoDevice setVideoStabilizationStrength:]"
+ "-[AVCaptureFigVideoDevice setVideoZoomFactor:]"
+ "-[AVCaptureFigVideoDevice setVideoZoomRampAcceleration:]"
+ "-[AVCaptureFigVideoDevice setWhiteBalanceMode:]"
+ "-[AVCaptureFigVideoDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:]"
+ "-[AVCaptureFigVideoDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:]_block_invoke_2"
+ "-[AVCaptureFigVideoDevice startPanningAtPoint:]"
+ "-[AVCaptureFigVideoDevice supportedMetadataObjectIdentifiersForZeroFrameDelaySynchronization]"
+ "-[AVCaptureFigVideoDevice supportedMetadataObjectIdentifiers]"
+ "-[AVCaptureFigVideoDevice supportsAVCaptureSessionPreset:]"
+ "-[AVCaptureInput attachToFigCaptureSession:]"
+ "-[AVCaptureInput detachFromFigCaptureSession:]"
+ "-[AVCaptureInputPort figCaptureSourceConfigurationForSessionPreset:]"
+ "-[AVCaptureMetadataOutput _emitCollections:]"
+ "-[AVCaptureMetadataOutput _handleLocalQueueMessage:]"
+ "-[AVCaptureMetadataOutput _handleNotification:payload:]"
+ "-[AVCaptureMetadataOutput _handleRemoteQueueOperation:]"
+ "-[AVCaptureMetadataOutput _newEmitTimerForSynchronizedMetadataCollections:]_block_invoke"
+ "-[AVCaptureMetadataOutput _processSynchronizationWithCollections:withCorrespondingMetadataObjectTypes:]"
+ "-[AVCaptureMetadataOutput _updateRemoteQueue:]_block_invoke"
+ "-[AVCaptureMetadataOutput setDelegateOverride:delegateOverrideCallbackQueue:]"
+ "-[AVCaptureMetadataOutput setMetadataObjectTypes:]"
+ "-[AVCaptureMetadataOutput setMetadataObjectsDelegate:queue:]"
+ "-[AVCaptureMovieFileOutput _cleanupDelegateWrappers:]_block_invoke"
+ "-[AVCaptureMovieFileOutput _startRecording:]"
+ "-[AVCaptureMovieFileOutput _totalNANDBandwidthAllowed:videoCodecType:]"
+ "-[AVCaptureMovieFileOutput handleDidPauseRecordingNotificationForWrapper:withPayload:]"
+ "-[AVCaptureMovieFileOutput handleDidResumeRecordingNotificationForWrapper:withPayload:]"
+ "-[AVCaptureMovieFileOutput handleDidStartRecordingNotificationForWrapper:withPayload:]"
+ "-[AVCaptureMovieFileOutput handleDidStartRecordingNotificationForWrapper:withPayload:]_block_invoke"
+ "-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForMomentCaptureWrapper:withPayload:demoof:addMetadata:]"
+ "-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForMomentCaptureWrapper:withPayload:demoof:addMetadata:]_block_invoke"
+ "-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForWrapper:withPayload:demoof:addMetadata:]"
+ "-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForWrapper:withPayload:demoof:addMetadata:]_block_invoke"
+ "-[AVCaptureMovieFileOutput startRecordingMovieWithSettings:delegate:]"
+ "-[AVCaptureMovieFileOutput startRecordingToOutputFileURL:recordingDelegate:]"
+ "-[AVCaptureMultiCamSession _canAddConnection:failureReason:]"
+ "-[AVCaptureMultiCamSession _canAddInput:failureReason:]"
+ "-[AVCaptureMultiCamSession _canAddOutput:failureReason:]"
+ "-[AVCaptureMultiCamSession _computeISPHardwareCost]"
+ "-[AVCaptureMultiCamSession _updateSystemPressureCost]"
+ "-[AVCaptureOutput _recommendedAudioOutputSettingsForConnection:sourceSettings:fileType:spatialAudioChannelLayoutTag:]"
+ "-[AVCaptureOutput _recommendedVideoOutputSettingsForConnection:sourceSettings:videoCodec:isIris:outputFileURL:]"
+ "-[AVCaptureOutput attachToFigCaptureSession:]"
+ "-[AVCaptureOutput detachFromFigCaptureSession:]"
+ "-[AVCaptureOutput handleServerConnectionDeathForFigCaptureSession:]"
+ "-[AVCaptureOutput recommendedCinematicAudioOutputSettingsForConnection:fileType:isProResCapture:]"
+ "-[AVCaptureOutput updateMetadataTransformForSourceFormat:]"
+ "-[AVCapturePhoto CGImageRepresentation]"
+ "-[AVCapturePhoto _fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:replacementPortraitEffectsMatte:replacementHairSegmentationMatte:replacementSkinSegmentationMatte:replacementTeethSegmentationMatte:replacementGlassesSegmentationMatte:replacementRawCompressionSettings:exceptionReason:]"
+ "-[AVCapturePhoto _fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:replacementPortraitEffectsMatte:replacementHairSegmentationMatte:replacementSkinSegmentationMatte:replacementTeethSegmentationMatte:replacementGlassesSegmentationMatte:replacementRawCompressionSettings:exceptionReason:]_block_invoke"
+ "-[AVCapturePhoto _maximumAppleProRAWBitDepth]"
+ "-[AVCapturePhoto initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:photoLibraryThumbnails:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:]"
+ "-[AVCapturePhoto pixelBuffer]"
+ "-[AVCapturePhoto previewCGImageRepresentation]"
+ "-[AVCapturePhoto sourceDeviceType]"
+ "-[AVCapturePhotoOutput _dispatchFailureCallbacks:forMovieRequest:withError:cleanupRequest:]"
+ "-[AVCapturePhotoOutput _dispatchFailureCallbacks:forMovieRequest:withError:cleanupRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _dispatchFailureCallbacks:forPhotoRequest:withError:cleanupRequest:]"
+ "-[AVCapturePhotoOutput _dispatchFailureCallbacks:forPhotoRequest:withError:cleanupRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _dispatchFailureCallbacks:forPhotoRequest:withError:cleanupRequest:]_block_invoke_3"
+ "-[AVCapturePhotoOutput _figCaptureIrisStillImageSettingsForAVCapturePhotoSettings:captureRequestIdentifier:delegate:connections:]"
+ "-[AVCapturePhotoOutput _handleDidBeginRecordingMomentCaptureMovieNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleDidCaptureStillImageNotificationWithPayload:forRequest:]"
+ "-[AVCapturePhotoOutput _handleDidCaptureStillImageNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleDidFinishCaptureNotificationWithPayload:forRequest:]"
+ "-[AVCapturePhotoOutput _handleDidFinishCaptureNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleDidFinishMovieCaptureMovieNotificationWithPayload:forRequest:]"
+ "-[AVCapturePhotoOutput _handleDidFinishMovieCaptureMovieNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleDidFinishRecordingIrisMovieNotificationWithPayload:forRequest:]"
+ "-[AVCapturePhotoOutput _handleDidFinishRecordingIrisMovieNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleDidFinishRecordingMomentCaptureMovieNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleDidFinishRecordingMomentCaptureMovieNotificationWithPayload:forRequest:]_block_invoke_3"
+ "-[AVCapturePhotoOutput _handleDidFinishRecordingVideoNotificationWithPayload:forRequest:]"
+ "-[AVCapturePhotoOutput _handleDidFinishRecordingVideoNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleDidFinishWritingMomentCaptureMovieNotificationWithPayload:forRequest:]"
+ "-[AVCapturePhotoOutput _handleDidFinishWritingMomentCaptureMovieNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleDidRecordIrisMovieNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleDidRecordIrisMovieNotificationWithPayload:forRequest:]_block_invoke_3"
+ "-[AVCapturePhotoOutput _handleNotification:payload:]"
+ "-[AVCapturePhotoOutput _handlePreparationCompleteNotificationWithPayload:settingsID:]"
+ "-[AVCapturePhotoOutput _handleReadyForResponsiveRequestWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleStillImageCompleteNotification:withPayload:forRequest:]"
+ "-[AVCapturePhotoOutput _handleStillImageCompleteNotification:withPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleWillBeginCaptureBeforeResolvingSettingsNotificationWithPayload:forRequest:]"
+ "-[AVCapturePhotoOutput _handleWillBeginCaptureBeforeResolvingSettingsNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleWillBeginCaptureNotificationWithPayload:forRequest:]"
+ "-[AVCapturePhotoOutput _handleWillBeginCaptureNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _handleWillCaptureStillImageNotificationWithPayload:forRequest:]_block_invoke"
+ "-[AVCapturePhotoOutput _updateCaptureReadinessStateForCompletedRequest:]"
+ "-[AVCapturePhotoOutput _updateCaptureReadiness]"
+ "-[AVCapturePhotoOutput _updateOfflineVISSupportedForSourceDevice:]"
+ "-[AVCapturePhotoOutput beginMomentCaptureWithSettings:delegate:]_block_invoke"
+ "-[AVCapturePhotoOutput cancelMomentCaptureWithUniqueID:]"
+ "-[AVCapturePhotoOutput capturePhotoWithSettings:delegate:]"
+ "-[AVCapturePhotoOutput capturePhotoWithSettings:delegate:]_block_invoke"
+ "-[AVCapturePhotoOutput commitMomentCaptureWithUniqueID:toMovieRecordingWithSettings:delegate:]"
+ "-[AVCapturePhotoOutput commitMomentCaptureWithUniqueID:toMovieRecordingWithSettings:delegate:]_block_invoke"
+ "-[AVCapturePhotoOutput commitMomentCaptureWithUniqueID:toPhotoCaptureWithSettings:delegate:]"
+ "-[AVCapturePhotoOutput commitMomentCaptureWithUniqueID:toPhotoCaptureWithSettings:delegate:]_block_invoke"
+ "-[AVCapturePhotoOutput dealloc]"
+ "-[AVCapturePhotoOutput endMomentCaptureWithUniqueID:]"
+ "-[AVCapturePhotoOutput initiateCaptureWithSettings:]_block_invoke"
+ "-[AVCapturePhotoOutput observeValueForKeyPath:ofObject:change:context:]"
+ "-[AVCapturePhotoOutput safelyHandleServerConnectionDeathForFigCaptureSession:]"
+ "-[AVCapturePhotoOutput setAutoDeferredPhotoDeliveryEnabled:]"
+ "-[AVCapturePhotoOutput setConstantColorClippingRecoveryEnabled:]"
+ "-[AVCapturePhotoOutput setConstantColorEnabled:]"
+ "-[AVCapturePhotoOutput setConstantColorSaturationBoostEnabled:]"
+ "-[AVCapturePhotoOutput setContentAwareDistortionCorrectionEnabled:]"
+ "-[AVCapturePhotoOutput setDepthDataDeliveryEnabled:]"
+ "-[AVCapturePhotoOutput setDualCameraDualPhotoDeliveryEnabled:]"
+ "-[AVCapturePhotoOutput setEnabledSemanticSegmentationMatteTypes:]"
+ "-[AVCapturePhotoOutput setFastCapturePrioritizationEnabled:]"
+ "-[AVCapturePhotoOutput setFigCaptureSessionSectionProperty:withHostTime:]_block_invoke"
+ "-[AVCapturePhotoOutput setFigCaptureSessionSectionProperty:withValue:]_block_invoke"
+ "-[AVCapturePhotoOutput setFocusPixelBlurScoreEnabled:]"
+ "-[AVCapturePhotoOutput setLivePhotoCaptureEnabled:]"
+ "-[AVCapturePhotoOutput setLivePhotoMovieProcessingSuspended:]"
+ "-[AVCapturePhotoOutput setLivePhotoMovieProcessingSuspended:]_block_invoke"
+ "-[AVCapturePhotoOutput setMovieRecordingEnabled:]"
+ "-[AVCapturePhotoOutput setOptimizesImagesForOfflineVideoStabilization:]"
+ "-[AVCapturePhotoOutput setPortraitEffectsMatteDeliveryEnabled:]"
+ "-[AVCapturePhotoOutput setPreparedPhotoSettingsArray:completionHandler:]"
+ "-[AVCapturePhotoOutput setPreparedPhotoSettingsArray:completionHandler:]_block_invoke_2"
+ "-[AVCapturePhotoOutput setPreservesLivePhotoCaptureSuspendedOnSessionStop:]"
+ "-[AVCapturePhotoOutput setPreviewQualityAdjustedPhotoFilterRenderingEnabled:]"
+ "-[AVCapturePhotoOutput setResponsiveCaptureEnabled:]"
+ "-[AVCapturePhotoOutput setSemanticStyleRenderingEnabled:]"
+ "-[AVCapturePhotoOutput setSpatialOverCaptureEnabled:]"
+ "-[AVCapturePhotoOutput setSpatialPhotoCaptureEnabled:]"
+ "-[AVCapturePhotoOutput setUltraHighResolutionZeroShutterLagEnabled:]"
+ "-[AVCapturePhotoOutput setUltraHighResolutionZeroShutterLagSupportEnabled:]"
+ "-[AVCapturePhotoOutput setVirtualDeviceConstituentPhotoDeliveryEnabled:]"
+ "-[AVCapturePhotoOutput setZeroShutterLagEnabled:]"
+ "-[AVCapturePhotoOutput userInitiatedCaptureRequestAtTime:]_block_invoke"
+ "-[AVCapturePhotoOutputReadinessCoordinator _invokeDelegateCallbackWithBlock:]"
+ "-[AVCapturePhotoOutputReadinessCoordinator _photoOutputDidUpdateCaptureReadinessState:]_block_invoke"
+ "-[AVCapturePhotoOutputReadinessCoordinator _setDelegate:queue:]_block_invoke"
+ "-[AVCapturePhotoOutputReadinessCoordinator _updateCaptureReadinessWithDelegate:]"
+ "-[AVCapturePhotoOutputReadinessCoordinator stopTrackingCaptureRequestUsingPhotoSettingsUniqueID:]_block_invoke"
+ "-[AVCapturePointCloudDataOutput _handleLocalQueueMessage:]"
+ "-[AVCapturePointCloudDataOutput _handleNotification:payload:]"
+ "-[AVCapturePointCloudDataOutput _handleRemoteQueueOperation:]"
+ "-[AVCapturePointCloudDataOutput _processSampleBuffer:]"
+ "-[AVCapturePointCloudDataOutput _updateRemoteQueue:]_block_invoke"
+ "-[AVCapturePointCloudDataOutput setDelegate:callbackQueue:]"
+ "-[AVCapturePointCloudDataOutput setDelegateOverride:delegateOverrideCallbackQueue:]"
+ "-[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:]"
+ "-[AVCaptureProprietaryDefaultsSingleton _updateProprietaryDefaultsSource:]_block_invoke"
+ "-[AVCaptureProprietaryDefaultsSingleton addObserver:forKey:callHandlerForInitialValue:defaultChangedHandler:]_block_invoke"
+ "-[AVCaptureProprietaryDefaultsSingleton cameraHistoryDownplayOverrideList]_block_invoke"
+ "-[AVCaptureProprietaryDefaultsSingleton imageForKey:fillWidth:fillHeight:]_block_invoke"
+ "-[AVCaptureProprietaryDefaultsSingleton objectForKey:]_block_invoke"
+ "-[AVCaptureProprietaryDefaultsSingleton objectsForWildcardKey:]_block_invoke"
+ "-[AVCaptureProprietaryDefaultsSingleton proprietaryDefaultsDomainForAuditToken:]_block_invoke"
+ "-[AVCaptureProprietaryDefaultsSingleton removeObserver:forKey:]_block_invoke"
+ "-[AVCaptureProprietaryDefaultsSingleton retryPriorFailedKeyObservationRegistrations]_block_invoke"
+ "-[AVCaptureProprietaryDefaultsSingleton setObject:forKey:]_block_invoke"
+ "-[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:]_block_invoke"
+ "-[AVCaptureProprietaryDefaultsSingleton unobserveChangesForKey:]"
+ "-[AVCaptureProprietaryDefaultsSingleton updateCameraHistory:withCameraInfo:maxLength:updateCameraHistoryDownplayOverrideList:cameraCanBeInOverrideList:]_block_invoke"
+ "-[AVCaptureSession _canAddConnection:failureReason:]"
+ "-[AVCaptureSession _canAddVideoPreviewLayer:failureReason:]"
+ "-[AVCaptureSession _computeMemoryUsageForOutputs]"
+ "-[AVCaptureSession _createFigCaptureSession]"
+ "-[AVCaptureSession _didRunDeferredStart]"
+ "-[AVCaptureSession _encoderCost]"
+ "-[AVCaptureSession _getSmartStyleRenderingSupported]"
+ "-[AVCaptureSession _handleCaptureServerConnectionDiedNotification]"
+ "-[AVCaptureSession _handleConfigurationCommittedNotificationWithPayload:]"
+ "-[AVCaptureSession _handleConfigurationDidBecomeLiveNotificationWithPayload:]"
+ "-[AVCaptureSession _handleDidStopRunningNotificationWithPayload:]"
+ "-[AVCaptureSession _handleVideoEffectFrameRateThrottling:]"
+ "-[AVCaptureSession _makeConfigurationLive:]"
+ "-[AVCaptureSession _memoryCost]"
+ "-[AVCaptureSession _nandCost]"
+ "-[AVCaptureSession _reconnectAfterServerConnectionDied]"
+ "-[AVCaptureSession _removeVideoPreviewLayer:]"
+ "-[AVCaptureSession _startFigCaptureSession]"
+ "-[AVCaptureSession _stopAndTearDownGraph]"
+ "-[AVCaptureSession _stopFigCaptureSession]"
+ "-[AVCaptureSession _updateDeviceActiveFormatsAndActiveConnections]"
+ "-[AVCaptureSession _updateHardwareCost]"
+ "-[AVCaptureSession _validateAudioConfiguration:]"
+ "-[AVCaptureSession _validateCinematicVideoConfiguration:]"
+ "-[AVCaptureSession _videoAndMovieOutputCost]"
+ "-[AVCaptureSession _willRunDeferredStart]"
+ "-[AVCaptureSession canAddConnection:]"
+ "-[AVCaptureSession canAddControl:]"
+ "-[AVCaptureSession canAddInput:]"
+ "-[AVCaptureSession canAddOutput:]"
+ "-[AVCaptureSession controlsDelegateCanReceiveAutoFocusLockedCallback]"
+ "-[AVCaptureSession displaySmartStylesOptOutAlert]"
+ "-[AVCaptureSession handleControlsOverlay:didChangeActiveControl:]"
+ "-[AVCaptureSession handleControlsOverlay:didChangeActiveControl:]_block_invoke"
+ "-[AVCaptureSession handleControlsOverlay:didChangeFocusLocked:]"
+ "-[AVCaptureSession handleControlsOverlay:didChangeFocusLocked:]_block_invoke"
+ "-[AVCaptureSession handleControlsOverlay:didChangeInterfaceReduced:]"
+ "-[AVCaptureSession handleControlsOverlay:didChangeInterfaceReduced:]_block_invoke"
+ "-[AVCaptureSession handleControlsOverlay:didChangeVisibility:activeControl:]"
+ "-[AVCaptureSession handleControlsOverlay:didChangeVisibility:activeControl:]_block_invoke"
+ "-[AVCaptureSession handleVideoInputDevice:activeDepthDataFormatChanged:]"
+ "-[AVCaptureSession handleVideoInputDevice:activeFormatChanged:]"
+ "-[AVCaptureSession isApplicationOptedOutByDefaultToSmartStyles]"
+ "-[AVCaptureSession isBeingConfiguredOnCurrentThread]"
+ "-[AVCaptureSession observeValueForKeyPath:ofObject:change:context:]"
+ "-[AVCaptureSession runDeferredStartWhenNeeded]"
+ "-[AVCaptureSession setDeferredStartDelegate:deferredStartDelegateCallbackQueue:]"
+ "-[AVCaptureSpatialAudioMetadataSampleGenerator init]"
+ "-[AVCaptureStillImageOutput _setStillImageStabilizationAutomaticallyEnabled:]"
+ "-[AVCaptureStillImageOutput handleNotification:payload:]"
+ "-[AVCaptureStillImageOutput handleNotificationForPrepareRequest:withPayload:]"
+ "-[AVCaptureStillImageOutput handleNotificationForRequest:withPayload:imageIsEV0:]"
+ "-[AVCaptureStillImageOutput prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:]"
+ "-[AVCaptureStillImageOutput setAutomaticallyEnablesStillImageStabilizationWhenAvailable:]"
+ "-[AVCaptureSystemExposureBiasSlider enqueueActionWithUpdate:]"
+ "-[AVCaptureSystemLensSelector enqueueActionWithUpdate:]"
+ "-[AVCaptureSystemStylePicker enqueueActionWithUpdate:]"
+ "-[AVCaptureSystemZoomSlider enqueueActionWithUpdate:]"
+ "-[AVCaptureVideoDataOutput _handleLocalQueueMessage:]"
+ "-[AVCaptureVideoDataOutput _handleNotification:payload:]"
+ "-[AVCaptureVideoDataOutput _handleRemoteQueueOperation:]"
+ "-[AVCaptureVideoDataOutput _processSampleBuffer:]"
+ "-[AVCaptureVideoDataOutput _updateRemoteQueue:]_block_invoke"
+ "-[AVCaptureVideoDataOutput handleChangedActiveFormat:forDevice:]"
+ "-[AVCaptureVideoDataOutput observeValueForKeyPath:ofObject:change:context:]"
+ "-[AVCaptureVideoDataOutput setDelegateOverride:delegateOverrideCallbackQueue:]"
+ "-[AVCaptureVideoDataOutput setMinFrameDuration:]"
+ "-[AVCaptureVideoDataOutput setSampleBufferDelegate:queue:]"
+ "-[AVCaptureVideoPreviewLayer _initWithSession:makeConnection:]"
+ "-[AVCaptureVideoPreviewLayer _setPortraitLightingEffectStrengthFromDeviceInput]"
+ "-[AVCaptureVideoPreviewLayer _setSensorAndEstimatedPreviewSizes]"
+ "-[AVCaptureVideoPreviewLayer _updateZoomPIPOverlayRect:]"
+ "-[AVCaptureVideoPreviewLayer _updateZoomPictureInPictureOverlaySupported]"
+ "-[AVCaptureVideoPreviewLayer attachToFigCaptureSession:]"
+ "-[AVCaptureVideoPreviewLayer captureDevicePointOfInterestForPoint:]"
+ "-[AVCaptureVideoPreviewLayer captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:]"
+ "-[AVCaptureVideoPreviewLayer centerSublayer:]"
+ "-[AVCaptureVideoPreviewLayer dealloc]"
+ "-[AVCaptureVideoPreviewLayer detachFromFigCaptureSession:]"
+ "-[AVCaptureVideoPreviewLayer initWithLayer:]"
+ "-[AVCaptureVideoPreviewLayer layerDidBecomeVisible:]"
+ "-[AVCaptureVideoPreviewLayer layoutSublayers]"
+ "-[AVCaptureVideoPreviewLayer observeValueForKeyPath:ofObject:change:context:]"
+ "-[AVCaptureVideoPreviewLayer pointForCaptureDevicePointOfInterest:]"
+ "-[AVCaptureVideoPreviewLayer setDepthDataDeliveryEnabled:]"
+ "-[AVCaptureVideoPreviewLayer setFilterRenderingEnabled:]"
+ "-[AVCaptureVideoPreviewLayer setPaused:]"
+ "-[AVCaptureVideoPreviewLayer setPortraitAutoSuggestEnabled:]"
+ "-[AVCaptureVideoPreviewLayer setSemanticStyle:animated:]"
+ "-[AVCaptureVideoPreviewLayer setSemanticStyleRenderingEnabled:]"
+ "-[AVCaptureVideoPreviewLayer setSession:]"
+ "-[AVCaptureVideoPreviewLayer setVideoGravity:]"
+ "-[AVCaptureVideoPreviewLayer setVideoPreviewFilters:]"
+ "-[AVCaptureVideoPreviewLayer setZoomPictureInPictureOverlayEnabled:]"
+ "-[AVCaptureVideoThumbnailOutput _handleNotification:payload:]"
+ "-[AVCaptureVisionDataOutput _handleLocalQueueMessage:]"
+ "-[AVCaptureVisionDataOutput _handleNotification:payload:]"
+ "-[AVCaptureVisionDataOutput _handleRemoteQueueOperation:]"
+ "-[AVCaptureVisionDataOutput _processSampleBuffer:]"
+ "-[AVCaptureVisionDataOutput _updateRemoteQueue:]_block_invoke"
+ "-[AVCaptureVisionDataOutput handleChangedActiveFormat:forDevice:]"
+ "-[AVCaptureVisionDataOutput setDelegate:callbackQueue:]"
+ "-[AVCaptureVisionDataOutput setDelegateOverride:delegateOverrideCallbackQueue:]"
+ "-[AVControlCenterModuleState _defaultOriginalVideoZoomFactor]"
+ "-[AVControlCenterModuleState _updateEligibleEffects:]"
+ "-[AVControlCenterModuleState initForBundleID:]"
+ "-[AVControlCenterModuleState setAutoMicrophoneModeEnabled:]"
+ "-[AVControlCenterModuleState setBackgroundReplacementURL:]"
+ "-[AVControlCenterModuleState setMicrophoneMode:]"
+ "-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke"
+ "-[AVDepthData _copyPixelBufferRepresentationWithPixelFormatType:]"
+ "-[AVDepthData depthDataByApplyingExifOrientation:]"
+ "-[AVDepthData dictionaryRepresentationForAuxiliaryDataType:]"
+ "-[AVExternalStorageDevice updateExternalStorageDeviceManager:andFigExternalStorageDeviceUUID:]"
+ "-[AVExternalStorageDeviceDiscoverySession _checkAuthorizationStatus]"
+ "-[AVExternalStorageDeviceDiscoverySession _requestAuthorization:]"
+ "-[AVExternalStorageDeviceDiscoverySession _setupExternalStorageDeviceDiscoverySession]"
+ "-[AVFlashlight _handleNotification:payload:]"
+ "-[AVFlashlight _setupFlashlight]"
+ "-[AVFlashlight _teardownFlashlight]"
+ "-[AVFlashlight beamWidthControlSupported]"
+ "-[AVFlashlight beamWidth]"
+ "-[AVFlashlight dealloc]"
+ "-[AVFlashlight flashlightLevel]"
+ "-[AVFlashlight init]"
+ "-[AVFlashlight isAvailable]"
+ "-[AVFlashlight isOverheated]"
+ "-[AVFlashlight maxBeamWidth]"
+ "-[AVFlashlight minBeamWidth]"
+ "-[AVMetadataMachineReadableCodeObject initWithFigEmbeddedCaptureDeviceMachineReadableCodeDictionary:input:]"
+ "-[AVOfflineVideoStabilizer _copyStabilizedSampleBuffer:]"
+ "-[AVOfflineVideoStabilizer _createSampleBufferWithPixelBuffer:sampleTime:futureMetadata:status:]"
+ "-[AVOfflineVideoStabilizer _setupVISProcessor]"
+ "-[AVOfflineVideoStabilizer _validateSourcePixelBuffer:withSampleTime:metadata:isEndOfData:]"
+ "-[AVOfflineVideoStabilizer _validateStabilizationMetadata:withSampleTime:isEndOfData:]"
+ "-[AVOfflineVideoStabilizer didCompleteProcessingOfBuffer:withStatus:]"
+ "-[AVPortraitEffectsMatte dictionaryRepresentationForAuxiliaryDataType:]"
+ "-[AVPortraitEffectsMatte portraitEffectsMatteByApplyingExifOrientation:]"
+ "-[AVSemanticSegmentationMatte dictionaryRepresentationForAuxiliaryDataType:]"
+ "-[AVSemanticSegmentationMatte semanticSegmentationMatteByApplyingExifOrientation:]"
+ "-[AVSmartStyleSettingsState _proprietaryDefaultChanged:keyPath:]"
+ "-[AVSmartStyleSettingsState setSystemStyleEnabled:]"
+ "-[AVSmartStyleSettingsState setSystemStyleEnabled:]_block_invoke"
+ "-[AVSpatialOverCaptureVideoPreviewLayer _handleSpatialNotification:payload:]"
+ "-[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:]"
+ "-[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:]_block_invoke"
+ "-[AVSpatialOverCaptureVideoPreviewLayer attachSafelyToFigCaptureSession:]"
+ "-[AVSpatialOverCaptureVideoPreviewLayer captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:]"
+ "-[AVSpatialOverCaptureVideoPreviewLayer detachSafelyFromFigCaptureSession:]"
+ "-[AVSpatialOverCaptureVideoPreviewLayer initWithLayer:]"
+ "-[AVSpatialOverCaptureVideoPreviewLayer setSemanticStyle:animated:]"
+ "-[AVSpatialOverCaptureVideoPreviewLayer setSemanticStyleRenderingEnabled:]"
+ "-[AVSpatialOverCaptureVideoPreviewLayer setSemanticStyles:semanticStylesRegions:]"
+ "-[AVSpatialOverCaptureVideoPreviewLayer setSemanticStyles:semanticStylesRegions:]_block_invoke"
+ "-[AVVirtualCaptureCard capacity]"
+ "-[AVVirtualCaptureCard freeSpace]"
+ "-[AVVirtualCaptureCard init]"
+ "-[AVVirtualCaptureCard showSystemUserInterface]"
+ "-[AVVirtualCaptureCard(AVVirtualCaptureCardConfiguration) setCapacity:error:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVCaptureConnection.m"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVCaptureVideoPreviewLayer.m"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVSpatialOverCaptureVideoPreviewLayer.m"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_AVF/AVFCapture/Common/Sources/AVCaptureCommon.m %s: could not determine proprietary defaults domain for %{private}@, so using unknown"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_AVF/AVFCapture/Common/Sources/AVCaptureCommon.m %s: not caching \"unknown\" proprietary defaults domain for %{private}@"
+ "0f4ec8652c6ac8093cc67a178a48c7d5260463ef"
+ "16c20df05460c3f1051d8276a8d50b236cb7c3ec"
+ "2OOO"
+ "580bcf2268cc115fc76e8d7941782a46a93070c2"
+ ": %@"
+ "<<<< AVAUVoiceIOChatFlavor >>>> %s: %@ translated to %@"
+ "<<<< AVAUVoiceIOChatFlavor >>>> %s: adding observer for %@"
+ "<<<< AVAUVoiceIOChatFlavor >>>> %s: posting NSNotificationCenter notification %@ with userInfo %@"
+ "<<<< AVAuxiliaryMetadata >>>> %s: Absent metadata: %@"
+ "<<<< AVAuxiliaryMetadata >>>> %s: Auxiliary metadata: '%@' : %@"
+ "<<<< AVAuxiliaryMetadata >>>> %s: Unpacked metadata: %@ value: %@"
+ "<<<< AVCaptureAudioDataOutput >>>> %s: (%p) %@ : %@"
+ "<<<< AVCaptureAudioDataOutput >>>> %s: (%p) Client is running inside of mediaserverd, and should be passing nil for the callback queue!  This check will be removed in the future and an exception will be thrown!"
+ "<<<< AVCaptureAudioDataOutput >>>> %s: (%p) Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCaptureAudioDataOutput >>>> %s: (%p) Got unexpected dequeue error: %d"
+ "<<<< AVCaptureAudioDataOutput >>>> %s: (%p) Got unknown opType %d"
+ "<<<< AVCaptureAudioDataOutput >>>> %s: (%p) calling %@ didOutputSampleBuffer:%p"
+ "<<<< AVCaptureAudioDataOutput >>>> %s: (%p) configurationID %lld became live with updated format description %@"
+ "<<<< AVCaptureAudioDataOutput >>>> %s: (%p) setting delegateOverride to %@ (%p)"
+ "<<<< AVCaptureAudioDataOutput >>>> %s: (%p) setting delegateOverride to nil"
+ "<<<< AVCaptureAudioDataOutput >>>> %s: (%p) setting sampleBufferDelegate to %@ (%p)"
+ "<<<< AVCaptureCameraCalibrationDataOutput >>>> %s: (%p) %@ : %@"
+ "<<<< AVCaptureCameraCalibrationDataOutput >>>> %s: (%p) Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCaptureCameraCalibrationDataOutput >>>> %s: (%p) Got unexpected dequeue error: %d"
+ "<<<< AVCaptureCameraCalibrationDataOutput >>>> %s: (%p) Got unknown opType %d"
+ "<<<< AVCaptureCameraCalibrationDataOutput >>>> %s: (%p) calling %@ didDropCameraCalibrationDataAtTimestamp reason:%d"
+ "<<<< AVCaptureCameraCalibrationDataOutput >>>> %s: (%p) calling %@ didOutputCameraCalibrationData:%p"
+ "<<<< AVCaptureCameraCalibrationDataOutput >>>> %s: (%p) configurationID %lld became live with updated format description %@"
+ "<<<< AVCaptureCameraCalibrationDataOutput >>>> %s: (%p) setting delegate to %@ (%p)"
+ "<<<< AVCaptureCameraCalibrationDataOutput >>>> %s: (%p) setting delegate to nil"
+ "<<<< AVCaptureCameraCalibrationDataOutput >>>> %s: (%p) setting delegateOverride to %@ (%p)"
+ "<<<< AVCaptureCameraCalibrationDataOutput >>>> %s: (%p) setting delegateOverride to nil"
+ "<<<< AVCaptureConnection >>>> %s: %@ %.2f"
+ "<<<< AVCaptureConnection >>>> %s: %@ %d"
+ "<<<< AVCaptureConnection >>>> %s: %@ cannot be set as the active video stabilization mode."
+ "<<<< AVCaptureConnection >>>> %s: %lld / %d"
+ "<<<< AVCaptureConnection >>>> %s: %p activeVideoStabilizationMode for connection to %@ is: %@ -> %@"
+ "<<<< AVCaptureConnection >>>> %s: %p activeVideoStabilizationMode for connection to %@ is: %@ -> %@ (preferred: %@)"
+ "<<<< AVCaptureConnection >>>> %s: %p preferredVideoStabilizationMode for connection to %@ is: %@"
+ "<<<< AVCaptureConnection >>>> %s: AVCaptureVideoStabilizationModeAuto does not map to a FigCaptureVideoStabilizationMethod.  Turning off."
+ "<<<< AVCaptureConnection >>>> %s: Input class is not AVCaptureMetadataInput or AVCaptureCoreMotionMetadataInput?"
+ "<<<< AVCaptureConnection >>>> %s: Output class is not AVCaptureMetadataOutput?"
+ "<<<< AVCaptureConnection >>>> %s: Specified max frame rate (%f) is too high, changing it to %f"
+ "<<<< AVCaptureConnection >>>> %s: Specified max frame rate (%f) is too low, changing it to %f"
+ "<<<< AVCaptureConnection >>>> %s: Specified min frame rate (%f) is too high, changing it to %f"
+ "<<<< AVCaptureConnection >>>> %s: Specified min frame rate (%f) is too low, changing it to %f"
+ "<<<< AVCaptureConnection >>>> %s: Unexpected spatial audio channel layout tag 0x%08x"
+ "<<<< AVCaptureConnection >>>> %s: We should not remove the observers in dealloc. see [17229521]"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Cannot send controls from an invalid connection!"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Cannot send controlsDelegate methods because the session reference is nil"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Cannot update a control from an invalid connection!"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Failed to send %lu controls to the overlay (%@)"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Failed to send control update to the overlay (%@)"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Ignoring status update from a stale connection!"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Not sending controls to the angel because the connection isn't active yet"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Successfully sent %lu controls to the overlay"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Successfully sent control value update to the overlay"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Unknown active control with identifier %@"
+ "<<<< AVCaptureCoreAnalyticsReporter >>>> %s: AVCaptureCoreAnalyticsReporter initialize"
+ "<<<< AVCaptureCoreAnalyticsReporter >>>> %s: Unknown internal client ID %@"
+ "<<<< AVCaptureDataOutputDelegateCallbackHelper >>>> %s: NULL handler"
+ "<<<< AVCaptureDataOutputDelegateCallbackHelper >>>> %s: NULL local queue"
+ "<<<< AVCaptureDataOutputDelegateCallbackHelper >>>> %s: NULL receiver"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p)"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) %*s%d]%@ %lld"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) **NOT** calling [%@ setDelegateOverride:nil queue:nil] since the data output's delegate override doesn't match (client probably initialized a new DOS)"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) ADJUSTED EARLIER: prevLeader:%lld (~%lld) -> follower:%lld -> (~%lld) nextLeader:%lld. Picked %lld"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) ADJUSTED LATER: prevLeader:%lld (~%lld) -> follower:%lld -> (~%lld) nextLeader:%lld. Picked %lld"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) Aging out leader data with time %lld / %d"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) Calling [%@ setDelegateOverride:%@ queue:%@]"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) Calling [%@ setDelegateOverride:nil queue:nil]"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) EXACT MATCH: leader:%lld follower:%lld adjusting to:%lld"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) Emitting %@"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) NOT ENOUGH LEADER: leader:%lld follower:%lld"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) NOT merging syncedMetadata %lld into %lld since they're different"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) Received data callback from an unknown capture output %@, dropping data on the floor"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) count=%d"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) dataOutput[%d](%p) No synchronized datas. Skipping."
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) dataOutput[%d](%p) ts %lld / %d != %lld / %d. Off by %lld / %d. Not dispatching"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) dataOutput[%d](%p) ts %lld / %d matches. Dispatching."
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) dataOutputs:%@"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) merging syncedMetadata %lld into %lld w/ adjusted time %lld"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) setting delegate to %@ (%p)"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) setting delegate to nil"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: (%p) updating QOS to %d"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: NO - for leader time %lld, cur time %lld is greater"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: NO - for leader time %lld, mdo is still expecting %d md types"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: NO - for leader time %lld, syncedDataQueue count is 0"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: NO - for leader time %lld, syncedDataQueue head hasn't been adjusted"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: for leader time %lld, dispatching leader data since all followers contain equal or greater timestamp at head"
+ "<<<< AVCaptureDataOutputSynchronizer >>>> %s: for leader time %lld, dispatching synced data for earliest follower time %lld"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s:  called for \"%@\" and request %@ with payload %@"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: (%p) %@"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: ***%@: Couldn't find a paired request for captureRequestIdentifier %@; returning without handling notification"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: ***%@: No captureRequestIdentifier; returning without handling notification"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Handling didFinishProcessingPhotoProxyNotification for identifier %@"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Missing capture settings for prewarming"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Missing serialized processing settings for prewarming"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Not calling, delegate %@ doesn't respond to willBeginProcessingPhotoProxy:%@"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Not propagating \"%@\" for request %@ as we plan to re-enqueue all requests; payload: %@"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Server connection died (sending client notification? %s)"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Server connection died and requests will be re-enqueued"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Server died without a client notification; re-establishing server connection"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Server will abort processing with %lu outstanding requests to re-enqueue"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Unable to cancel photo processor prewarming (%d)"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Unable to establish server connection (%d)"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Unable to prewarm photo processor (%d)"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: calling %@ willBeginProcessingPhotoProxy:%@"
+ "<<<< AVCaptureDeferredPhotoSettings >>>> %s: Failed to deserialize capture settings"
+ "<<<< AVCaptureDeferredPhotoSettings >>>> %s: Failed to deserialize serialized processing settings"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) %@ : %@"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) Client is running inside of mediaserverd, and should be passing nil for the callback queue!  This check will be removed in the future and an exception will be thrown!"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) Got unexpected dequeue error: %d"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) Got unknown opType %d"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) Observed change in active on connection from %d to %d"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) Observed change in mirroring on connection from %@ to %@"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) Observed change in orientation on connection from %@ to %@"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) calling %@ didDropDepthData:%p reason:%d"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) calling %@ didOutputDepthData:%p"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) configurationID %lld became live with updated format description %@"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) setting delegate to %@ (%p)"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) setting delegate to nil"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) setting delegateOverride to %@ (%p)"
+ "<<<< AVCaptureDepthDataOutput >>>> %s: (%p) setting delegateOverride to nil"
+ "<<<< AVCaptureDevice >>>> %s: %@: resetting backgroundReplacementURL to %@"
+ "<<<< AVCaptureDevice >>>> %s: (pthread:%p) ServerConnectionDied"
+ "<<<< AVCaptureDevice >>>> %s: BUG: Dropping extra reaction activity 1/3: %@"
+ "<<<< AVCaptureDevice >>>> %s: BUG: Dropping extra reaction activity 2/3: Previous:%@"
+ "<<<< AVCaptureDevice >>>> %s: BUG: Dropping extra reaction activity 3/3: Incoming:%@"
+ "<<<< AVCaptureDevice >>>> %s: Called with media type '%@'"
+ "<<<< AVCaptureDevice >>>> %s: Called with media type '%@', handler %p"
+ "<<<< AVCaptureDevice >>>> %s: Called with unsupported device class %@"
+ "<<<< AVCaptureDevice >>>> %s: Camera access is restricted: %s"
+ "<<<< AVCaptureDevice >>>> %s: Continuity capture enabled user preference changed: %@"
+ "<<<< AVCaptureDevice >>>> %s: Continuity capture in use volatile user preference changed: %@"
+ "<<<< AVCaptureDevice >>>> %s: Device missing unique ID: %@"
+ "<<<< AVCaptureDevice >>>> %s: Error unpacking bookmark %@: %@"
+ "<<<< AVCaptureDevice >>>> %s: Failed to create AVCaptureReactionEffectState from %@"
+ "<<<< AVCaptureDevice >>>> %s: FigCaptureTCCAccessPreflight result was kTCCAccessPreflightDenied for media type '%@'"
+ "<<<< AVCaptureDevice >>>> %s: FigCaptureTCCAccessPreflight result was kTCCAccessPreflightGranted for media type '%@'"
+ "<<<< AVCaptureDevice >>>> %s: FigCaptureTCCAccessPreflight result was kTCCAccessPreflightUnknown for media type '%@'"
+ "<<<< AVCaptureDevice >>>> %s: Got bad trigger: %@"
+ "<<<< AVCaptureDevice >>>> %s: Got bad update: %@"
+ "<<<< AVCaptureDevice >>>> %s: Missing tccServiceName for media type '%@'"
+ "<<<< AVCaptureDevice >>>> %s: Posting AVCaptureDeviceWasConnectedNotification for audio device %@"
+ "<<<< AVCaptureDevice >>>> %s: Posting AVCaptureDeviceWasConnectedNotification for video device %@"
+ "<<<< AVCaptureDevice >>>> %s: Posting AVCaptureDeviceWasDisconnectedNotification for audio device %@"
+ "<<<< AVCaptureDevice >>>> %s: Posting AVCaptureDeviceWasDisconnectedNotification for video device %@"
+ "<<<< AVCaptureDevice >>>> %s: Probably a bug 1/3: previous %@ vs early incoming %@"
+ "<<<< AVCaptureDevice >>>> %s: Probably a bug 1/3: previous %@ vs late incoming %@"
+ "<<<< AVCaptureDevice >>>> %s: Probably a bug 2/3: Incoming:%@"
+ "<<<< AVCaptureDevice >>>> %s: Probably a bug 2/3: Previous:%@"
+ "<<<< AVCaptureDevice >>>> %s: Probably a bug 3/3: Incoming:%@"
+ "<<<< AVCaptureDevice >>>> %s: Read activeMicrophoneMode %d"
+ "<<<< AVCaptureDevice >>>> %s: Read backgroundBlurAperture %f"
+ "<<<< AVCaptureDevice >>>> %s: Read backgroundBlurControlMode %d"
+ "<<<< AVCaptureDevice >>>> %s: Read backgroundReplacementPixelBuffer %p (cached %d)"
+ "<<<< AVCaptureDevice >>>> %s: Read backgroundReplacementURL %@"
+ "<<<< AVCaptureDevice >>>> %s: Read centerStageControlMode %d"
+ "<<<< AVCaptureDevice >>>> %s: Read isBackgroundBlurEnabled %@ via self.isPortraitEffectEnabled"
+ "<<<< AVCaptureDevice >>>> %s: Read isBackgroundReplacementEnabled %@"
+ "<<<< AVCaptureDevice >>>> %s: Read isCenterStageEnabled %@"
+ "<<<< AVCaptureDevice >>>> %s: Read isPortraitEffectEnabled %@"
+ "<<<< AVCaptureDevice >>>> %s: Read isStudioLightEnabled %@"
+ "<<<< AVCaptureDevice >>>> %s: Read portraitEffectStudioLightQuality %ld"
+ "<<<< AVCaptureDevice >>>> %s: Read preferredMicrophoneMode %d"
+ "<<<< AVCaptureDevice >>>> %s: Read reactionEffectGesturesEnabled %@"
+ "<<<< AVCaptureDevice >>>> %s: Read reactionsEnabled %@"
+ "<<<< AVCaptureDevice >>>> %s: Read studioLightingControlMode %d"
+ "<<<< AVCaptureDevice >>>> %s: Read studioLightingIntensity %f"
+ "<<<< AVCaptureDevice >>>> %s: Running in xctest; access granted to media type '%@'"
+ "<<<< AVCaptureDevice >>>> %s: Set backgroundBlurAperture %f"
+ "<<<< AVCaptureDevice >>>> %s: Set backgroundBlurControlMode %d"
+ "<<<< AVCaptureDevice >>>> %s: Set backgroundReplacementEnabled %@"
+ "<<<< AVCaptureDevice >>>> %s: Set backgroundReplacementPixelBuffer %p (%s)"
+ "<<<< AVCaptureDevice >>>> %s: Set backgroundReplacementURL %@"
+ "<<<< AVCaptureDevice >>>> %s: Set centerStageControlMode %d"
+ "<<<< AVCaptureDevice >>>> %s: Set portraitEffectStudioLightQuality %ld"
+ "<<<< AVCaptureDevice >>>> %s: Set sBackgroundBlurAperture %f"
+ "<<<< AVCaptureDevice >>>> %s: Set sBackgroundReplacementEnabled %@"
+ "<<<< AVCaptureDevice >>>> %s: Set sBackgroundReplacementURL %@"
+ "<<<< AVCaptureDevice >>>> %s: Set sStudioLightingIntensity %f"
+ "<<<< AVCaptureDevice >>>> %s: Set studioLightingControlMode %d"
+ "<<<< AVCaptureDevice >>>> %s: Set studioLightingIntensity %f"
+ "<<<< AVCaptureDevice >>>> %s: Setting %@ unavailable reasons from %lu to %lu"
+ "<<<< AVCaptureDevice >>>> %s: Trying to set unavailable reasons for unsupported video effect: %@"
+ "<<<< AVCaptureDevice >>>> %s: Unavailable reasons for gestures doesn't exist, forwards to unavailable reasons for reactions."
+ "<<<< AVCaptureDevice >>>> %s: Unsupported unique ID: %@"
+ "<<<< AVCaptureDevice >>>> %s: Updating eligible effects for %@: %@"
+ "<<<< AVCaptureDevice >>>> %s: bookmarkDataWithOptions error: %@"
+ "<<<< AVCaptureDevice >>>> %s: ignoring attempt to assign NULL background replacement pixel buffer"
+ "<<<< AVCaptureDevice >>>> %s: notify_register_check for %s failed (%d)"
+ "<<<< AVCaptureDevice >>>> %s: sCenterStageFramingMode changing from %ld to %ld"
+ "<<<< AVCaptureDevice >>>> %s: updateReactionsInProgress %@ -> %@"
+ "<<<< AVCaptureDeviceInput >>>> %s: %@ : %@"
+ "<<<< AVCaptureDeviceInput >>>> %s: (%p) called with %lu"
+ "<<<< AVCaptureDeviceInput >>>> %s: AVAuthorizationStatus result was AVAuthorizationStatusNotDetermined for media type '%@'; firing off async query to UI"
+ "<<<< AVCaptureDeviceInput >>>> %s: Authorized to use AVCaptureDevice %p: %s"
+ "<<<< AVCaptureDeviceInput >>>> %s: Disregarding notification %@ since sourceIDs don't match"
+ "<<<< AVCaptureDeviceInput >>>> %s: Expecting either audio or video for device %@"
+ "<<<< AVCaptureDeviceInput >>>> %s: called (%p)"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: %@"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Device orientation: %d"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Device: %@, Preview Layer: %@"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Helper Layer Visible: %@, Context ID: %u"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Helper layer is visible, updating video rotation angle for horizon-level preview"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Not changing _videoRotationAngleForHorizonLevelCapture (already %.1f)"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Not changing _videoRotationAngleForHorizonLevelPreview (already %.1f)"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Notification: %@"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Orientation update: %@"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Preview Layer Context ID: %u"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Preview Layer System Reference Angle Mode: %lu"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Preview layer is nil. Bailing."
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: System Reference Angle: %.1f"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Video Preview Layer is visible. Context ID: %u"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Video preview layer is visible, updating video rotation angle for horizon-level preview"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Will not update _videoRotationAngleForHorizonLevelPreview -- Mode is Unknown and layer context ID is 0."
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Will update _videoRotationAngleForHorizonLevelPreview using system reference angle (%.1f)"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Will update _videoRotationAngleForHorizonLevelPreview using system reference angle (%.1f) from active interface orientation (%d)"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: Will update _videoRotationAngleForHorizonLevelPreview using system reference angle (%.1f) from device orientation (%d)"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: %{public}@ Changing audioInputRouteIsBuiltInMic from %d to %d"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: %{public}@ Changing localized name from %{public}@ to %{public}@"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: (%p)"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: (%p) %@"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: (%p) Copy(%@) failed (%d)"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: (%p)(pthread:%p) Ignoring ServerConnectionDied notification"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: Error creating a clock for the shared AVAudioSession.  Session: %p, sessionID: %d, err: %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: Could not create a proxy source with %@ for %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: FigCaptureSourceRemoteCopyCaptureSources error retry %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] \tFiring completion handler %p for EXACT MATCH request with time %f (cur=%d/completed=%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] \tFiring completion handler %p for earlier (coalesced?) request with time %f (cur=%d/completed=%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] \tFiring completion handler %p for fake bias request with time %f (cur=%d/completed=%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] \tFiring completion handler %p with kCMTimeInvalid due to error %d (cur=%d/completed=%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] \tNot dequeueing request -- it's in the future (cur=%d/completed=%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] %lld / %d (%f ms)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] (pthread:%p) Ignoring ServerConnectionDied notification"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Accepting zoom ramp: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Active primary constituent device changed from %@ to %@."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] AutoExpose adjustment finished. Transitioning to locked"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Battery level not supported"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Battery state not supported"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] CMMetadataFormatDescriptionCreateWithMetadataSpecifications returned error %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Caching FigCaptureSource %@ to %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Called with queue %p"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Changing kCMTimeInvalid to %.2f max fps"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Changing kCMTimeInvalid to %f min fps"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Cinematic video focus at: %.2fx%.2f, objectID: %ld, isHardFocus %d, isFixedPlaneFocus %d - operation: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Copy(%@) failed (%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Current activeMaxFrameDuration (%lld/%d) is out of range for the new activeFormat, whose maxSupportedDuration is (%lld/%d). Clamping!"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Current activeMinFrameDuration (%lld/%d) is out of range for the new activeFormat, whose minSupportedDuration is (%lld/%d). Clamping!"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Current videoZoomFactor (%f) exceeds the new activeFormat's max zoom factor (%f). Clamping!"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Current videoZoomFactor (%f) is less than the new activeFormat's min zoom factor (%f). Clamping!"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Custom exposure duration changed to %lld/%d (%f) (as rate + .05 = %f), cur min frame rate %f is lower, so NOT changing."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Custom exposure duration changed to %lld/%d (%f) (as rate + .05 = %f), setting min frame rate %f -> %f"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Data change handler already active"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Data change handler not active"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Encountered unknown device."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Enqueued custom exposure request %d with error %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Enqueued fake bias request %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Enqueued manual focus request %d with error %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Enqueued manual wb request %d with error %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Enqueueing bias request %d with error %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Error setting centerStageFramingMode to %ld (%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Exiting for queue %p"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Hidden changed from %d to %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Invalid notification payload!"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Iterations used: %d (HIT ITER LIMIT) for gains (%a %a %a) start %a"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Leaving custom exposure, so restoring min:%.2lld/%.2d max:%.2lld/%.2d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Macro focus changed from %d to %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] MaxFrameDuration to set %lld / %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] MinFrameDuration to set %lld / %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] No FigCaptureSource"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Overriding max frame rate %f to the cap of %f"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Overriding min frame rate %f to the cap of %f"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Preferred primary constituent device changed from %@ to %@."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] ReadyToUnhide changed from %d to %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received %@ with %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received DeviceWhiteBalanceGains notification with a bad payload. Expected size = %d, actual = %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received GrayWorldDeviceWhiteBalanceGains notification with a bad payload. Expected size = %d, actual = %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received kFigCaptureSourceProperty_Hidden notification payload with value YES. Skip updating device property."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received kFigCaptureSourceProperty_ReadyToUnhide notification payload with value NO. Skip updating device property."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received unexpected Connected notification"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Resetting framing"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Sending notification: %@ with payload: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Set(%@) failed (%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Setting FigCaptureSource %@ to %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Setting exposureMode = Locked after one-shot Auto-Expose or transition from Custom -> Locked Exposure"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Setting max frame rate failed"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Setting min frame rate failed"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] State inconsistency: ramp %d notified completion but invalid ramping target %g"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Supported frame duration range for %@ (%lld / %d - %lld / %d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Supported frame duration range for Background Blur (%lld / %d - %lld / %d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Supported frame duration range for Background Replacement (%lld / %d - %lld / %d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Supported frame duration range for Cinematic Video (%lld / %d - %lld / %d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Supported frame duration range for Studio Lighting (%lld / %d - %lld / %d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] System pressure change: %@ -> %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] System pressure change: %@ -> %@ for SDOF effects enabled change"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] System pressure change: %@ -> %@ for depth data delivery enabled change"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] System pressure change: %@ -> %@ for format change"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Unable to copy property %@ into cache"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Underlying master source (deviceType %d) is not one of the constituent devices of this AVCaptureDevice"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Unexpected gray world white balance gains size! Expected %d, actual %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Unexpected white balance gains size! Expected %d, actual %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Unexpected white balance gains size! Expected %lu, actual %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Unhandled property: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Value for activeMaxFrameRate set to value: %lld timescale:%d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Value for activeMinFrameRate set to value: %lld timescale:%d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] _captureSourceSupportedMetadata: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] _captureSourceSupportedZeroFrameDelaySynchronizationMetadata: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] activeVideoMaxFrameDuration is changing in custom exposure mode, so sending custom exposure request (if ss is out of range, it will change to the min frame rate)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] activeVideoMinFrameDuration changing in custom exposure mode, so sending a new custom exposure request to update frame rate"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] adjustingExposure %d -> %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with %f"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with %lld / %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with detectedObjectID %lu focusMode %lu"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with duration: %lld / %d ISO: %f"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with factor: %f duration: %f"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with factor: %f rate: %f"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with factor: %f tuning: %ld"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with point x %f y %f focusMode %lu"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with starting point [%f,%f]"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with translation [%f,%f]"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with { %f, %f }"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with { r: %f, g: %f, b: %f }"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with { { %f, %f } { %f, %f } }"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] changing to connected=%d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] depthDataDeliveryEnabledChanging: NO"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] depthDataDeliveryEnabledChanging: YES"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] draining request %d from queue %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] exposure operation: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] faceRectangle <x:%f, y:%f>, [w:%f, h:%f]"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] failed (%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] focus operation: mode %d, lensPosition %f, %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] forcing default exposure ROI size { %.4lf, %.4lf } to { %.4lf, %.4lf } ... point of interest is { %.4lf, %.4lf } which came from %@ : %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] forcing default focus ROI size { %.4lf, %.4lf } to { %.4lf, %.4lf } ... point of interest is { %.4lf, %.4lf } which came from %@ : %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] format:%{public}@ preset:%{public}@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] from KVO %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] from query %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] initialized with fcs: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] kCMTimeInvalid (clearing override)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] performing one-shot framing"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] scene classification activity changed from %d to %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] scene classification activity check: %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] ss is too low for new min frame rate %f, increasing ss."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] video zoom factor changed from %f to %f"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] white-balance operation: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: exposure rect (isDefault: %c) { (%.2f : %.2f) : [%.2f : %.2f] : (%.2f : %.2f) }"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: focus rect (isDefault: %c) { (%.2f : %.2f) : [%.2f : %.2f] : (%.2f : %.2f) }"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: leftover devices! %@\nAppending to prioritized list: %@"
+ "<<<< AVCaptureInput >>>> %s: %@ %@"
+ "<<<< AVCaptureInputPort >>>> %s: sourceConfig.requiredFormat is still nil"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) %@ : %@"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) Client is running inside of mediaserverd, and should be passing nil for the callback queue!  This check will be removed in the future and an exception will be thrown!"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) Emit timer fires. Aging out queued metadata collection %@ with time %lld / %d"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) Emitting synchronized queued metadata collection %@ with time %lld / %d"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) Got unexpected dequeue error: %d"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) Got unknown opType %d"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) Received new collection %@ and merging to synchronized queued metadata collection %@ with time %lld / %d"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) Received new collection %@. Emitting readyToEmit synchronized metadata collection %@ with time %lld / %d"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) Received new collection %@. Enqueuing new synchronized metadata collection %@ with time %lld / %d"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) Synchonized queue exceeds max size. Aging out first queued metadata collection %@ with time %lld / %d"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) calling %@ didOutputMetadataObjectCollections:%@"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) calling %@ didOutputMetadataObjects:%@"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) calling %@ didOutputMetadataObjects:%@ forMetadataObjectTypes:%@"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) configurationID %lld became live with updated format description %@"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) metadata object types: %@"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) setting delegate to %@ (%p)"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) setting delegate to nil"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) setting delegateOverride to %@ (%p)"
+ "<<<< AVCaptureMetadataOutput >>>> %s: (%p) setting delegateOverride to nil"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) Cleaning up unfinished movie recordings since mediaserverd died"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) Disregarding notification %@ since its settingsID doesn't match any I know about"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) NOT posting AVCaptureMovieFileOutputRecordingCompletedNotification because no thumbnail"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) Received _DidPauseRecording message without first receiving a _DidStartRecording. That can't be good."
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) Received _DidResumeRecording message without first receiving a _DidPauseRecording.  That can't be good."
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) Received _DidResumeRecording message without first receiving a _DidStartRecording.  That can't be good."
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) Received duplicate _DidStartRecording message from FigCaptureSession! BAD!!!"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) calling [%@ captureOutput:%@ didBeginMovieCaptureForResolvedSettings:%@]"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) calling [%@ captureOutput:%@ didStartRecordingToOutputFileAtURL:%@ fromConnections:%@]"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) calling [%@ captureOutput:%@ didStartRecordingToOutputFileAtURL:%@ startPTS:%.4lf fromConnections:%@]"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) consolidateMovieFragmentsInFile:%@ (spatial:%d) failed (%@)"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) consolidateMovieFragmentsInFile:%@ failed (%@)"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) posting AVCaptureMovieFileOutputRecordingCompletedNotification"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) updateMovieMetadataInFile:%@ failed (%@)"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: A file at the requested path already exists."
+ "<<<< AVCaptureMovieFileOutput >>>> %s: Preview pixel buffer creation from IOSurface failed (%d)"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: The total NAND bandwidth is not allowed."
+ "<<<< AVCaptureMovieFileOutput >>>> %s: Unhandled notification %@ with payload: %@"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: Using cinematicAudioSettings: %@"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: calling from main thread [%@ captureOutput:%@ didFinishRecordingToOutputFileAtURL:%@ debugMetadataSidecarFileURL:%@ fromConnections:blah error:%@] (recording = %d, paused = %d)"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: calling from main thread [%@ captureOutput:%@ didFinishRecordingToOutputFileAtURL:%@ fromConnections:blah error:%@] (recording = %d, paused = %d)"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: calling from main thread [%@ captureOutput:%@ didFinishWritingMovie:%@ error:%@] (recording = %d, overcapture = %d)"
+ "<<<< AVCaptureMultiCamSession >>>> %s: (%p)failureReason = %@"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW base CPU power"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for %@ CPU"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for %@ ISP"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for %@ OIS"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for %@ sensor"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for Background Blur (%dmW for %d devices)"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for Center Stage (%dmW for %d devices)"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for Cinematic Video (%dmW for %d inputs)"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for Gestures (%dmW for %d devices)"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for Studio Lighting (%dmW for %d devices)"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for VIS on MFO"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for VIS on VDO"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for encoding %d%d@%d, %g bytesPerPixel"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %dmW for mic"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Adding %fmW for Pearl depth"
+ "<<<< AVCaptureMultiCamSession >>>> %s: ISP hardware cost: %f"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Invalid encoder power model for platformID %d"
+ "<<<< AVCaptureMultiCamSession >>>> %s: More than two active cameras of which two or more are 4k is not supported, forcing cost > 1.0: %f"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Multiple non-LiDAR depth outputs are not supported, forcing cost > 1.0: %f"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Power adjustments: SOC: %dmW, camera: %dmW, temp adj. soc: %dmW, temp adj. camera: %dmW, camera PMU: %dmW, main PMU: %dmW, total SOC: %dmW. "
+ "<<<< AVCaptureMultiCamSession >>>> %s: System pressure cost: %f (socPower=%dmW, cameraPower=%dmW, total=%dmW)"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Unable to find a constituent device format for %@ (on device %@)"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Unable to find a thermal model for %@"
+ "<<<< AVCaptureMultiCamSession >>>> %s: Unable to find an encoder power model for platformID %d"
+ "<<<< AVCaptureOutput >>>> %s: %@ %@"
+ "<<<< AVCaptureOutput >>>> %s: (%p) Bumping bit rate by 10 percent for 10 bit HDR video mode."
+ "<<<< AVCaptureOutput >>>> %s: (%p) NOT using AVCaptureSession.plist video settings, since max frame rate is changed"
+ "<<<< AVCaptureOutput >>>> %s: (%p) enable double encoding for ProRes"
+ "<<<< AVCaptureOutput >>>> %s: (%p) sensor:{%fx%f} scaled:{%fx%f} vt:%@ front:%d applyRot:%d rotDegs:%f orient:%d applyMirr:%d isMirr:%d"
+ "<<<< AVCaptureOutput >>>> %s: (%p) setting average bit rate of %lld."
+ "<<<< AVCaptureOutput >>>> %s: (%p) stereo capture enabled, scaling bitrate by %.2lf from %d to %d"
+ "<<<< AVCaptureOutput >>>> %s: Cancelling shutter sound suppression for AirPod Stem Click"
+ "<<<< AVCaptureOutput >>>> %s: Shutter sound suppressed by API"
+ "<<<< AVCaptureOutput >>>> %s: Shutter sound suppressed by AirPod Stem Click"
+ "<<<< AVCaptureOutput >>>> %s: Shutter sound suppressed due to active movie recording"
+ "<<<< AVCaptureOutput >>>> %s: Using asbd from fdesc. destSampleRate: %f, destNumChannels: %u, pcmBitDepth: %u"
+ "<<<< AVCaptureOutput >>>> %s: recommendedCinematicAudioOutputSettingsForConnection returning: %@"
+ "<<<< AVCapturePhoto >>>>"
+ "<<<< AVCapturePhoto >>>> %s: (%p) CMPhotoDetermineMIAFCompliantThumbnailMaxPixelSize() returned error %d for photo dimensions %dx%d. We are using max pixel size %lu for thumbnail."
+ "<<<< AVCapturePhoto >>>> %s: (%p) photo dimensions %dx%d MIAF compliant thumbnail max pixel size %lu"
+ "<<<< AVCapturePhoto >>>> %s: CGImageDestinationCreateWithData failed"
+ "<<<< AVCapturePhoto >>>> %s: CGImageDestinationFinalize failed"
+ "<<<< AVCapturePhoto >>>> %s: CGImageSourceCreateImageAtIndex failed"
+ "<<<< AVCapturePhoto >>>> %s: CGImageSourceCreateWithData failed"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoCompressionCreateDataContainerFromImage failed to convert preview sbuf to jpeg (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoCompressionSessionAddMetadataFromImageProperties failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoCompressionSessionAddThumbnail failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoCompressionSessionCloseContainerAndCopyBacking failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoCompressionSessionCreate failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoCompressionSessionOpenExistingContainerForModification failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDNGCompressorCreateFromSourceDNGWithModificationHandler failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDNGCompressorFinalizeAndCreateData failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDNGCompressorReplaceMainImageOptions failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDNGCompressorReplaceMainImageProperties failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDNGCompressorSetCompressedPreviewImage failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDNGCompressorSetPreviewImage failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDNGCompressorSetPreviewImageFromRAW failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDNGCreateDNGFromRAWPixelBufferAndAuxiliaryImage failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDecompressionContainerCopyAuxiliaryImageMetadataForIndex failed (%d) - carrying on anyway"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDecompressionContainerCreateAuxiliaryImageForIndex failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDecompressionContainerGetAuxiliaryImageCountForIndex failed (%d) or has no aux images"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDecompressionContainerGetImageCount failed (%d) or has no images"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDecompressionSessionCreate failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: CMPhotoDecompressionSessionCreateContainer failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Can't make a preview CGImage because no preview photo was requested"
+ "<<<< AVCapturePhoto >>>> %s: Can't make fileDataRepresentation of rawPhoto - no pixel buffer"
+ "<<<< AVCapturePhoto >>>> %s: Constant color confidence map creation from IOSurface failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Could not create array"
+ "<<<< AVCapturePhoto >>>> %s: Depth pixel buffer creation from IOSurface failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Embedded thumbnail source pixel buffer creation from IOSurface failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Failed to read image properties from DNG (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Found auxiliary image of type %d at index 0/%d"
+ "<<<< AVCapturePhoto >>>> %s: Glasses segmentation matte pixel buffer creation from IOSurface failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Hair segmentation matte pixel buffer creation from IOSurface failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Nil pixelBuffer"
+ "<<<< AVCapturePhoto >>>> %s: Photo pixel buffer creation from IOSurface failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Portrait effects matte pixel buffer creation from IOSurface failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Preview pixel buffer creation from IOSurface failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Skin segmentation matte pixel buffer creation from IOSurface failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Teeth segmentation matte pixel buffer creation from IOSurface failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: Unexpectedly had multiple different bit depths in a ProRAW photo (initial:%d, other:%d)"
+ "<<<< AVCapturePhoto >>>> %s: VTCreateCGImageFromCVPixelBuffer failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: _addAuxiliaryImage (disparity) failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: _addAuxiliaryImage (glasses segmentation matte) failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: _addAuxiliaryImage (hair segmentation matte) failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: _addAuxiliaryImage (portrait effects matte) failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: _addAuxiliaryImage (skin segmentation matte) failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: _addAuxiliaryImage (teeth segmentation matte) failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: _createCompressionSessionWithModifications failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: _createDNGCompressorWithModifications failed (%d)"
+ "<<<< AVCapturePhoto >>>> %s: avcp_copyCGImageForCompressedData failed"
+ "<<<< AVCapturePhoto >>>> %s: focal length didn't match the lens aperture of any of the virtual camera's constituent devices! (%f)"
+ "<<<< AVCapturePhoto >>>> %s: nil data passed"
+ "<<<< AVCapturePhoto >>>> %s: pixelBuffer must be non-NULL!"
+ "<<<< AVCapturePhoto >>>> %s: ts:%f main:%p prev:%p thumb:%p meta:%p depth:%p pem:%p hair:%p skin:%p teeth:%p glasses:%p seq:%d count:%d flags:%08x devType:%@%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) %@:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) %@Not calling %@ didFinishWritingMovieFileAtURL:%@ debugMetadataSidecarFileURL:%@ previewPixelBuffer:%p duration:%fs resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) %@calling %@ didFinishWritingMovie:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) %@calling %@ didFinishWritingMovieFileAtURL:%@ debugMetadataSidecarFileURL:%@ previewPixelBuffer:%p duration:%fs resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) %s%scalling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ debugMetadataSidecarFileURL:%@ duration:%fs photoDisplayTime:%fs resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) %s%scalling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ duration:%fs photoDisplayTime:%fs metadataIdentifiers:%@ resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) %s%scalling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ duration:%fs photoDisplayTime:%fs resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) ***didFinishProcessingVideoFileAtURL error: (%@, %d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Allowing synchronous readinessUpdateBlock for the main thread/queue"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Already received %d notifications for still image capture with settings ID %lld; ignoring."
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Aspect ratio mismatch between Original and Optimized Image output dimensions"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) CMBlockBufferCreateContiguous failed (%d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) CMBlockBufferGetDataPointer failed (%d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) CMPhotoDNGCreateDNGFromRAWPixelBuffer failed (%d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Calling CommitMomentCaptureToStillImageCapture with %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Calling FigCaptureSessionIrisStillImageSinkPrepareToCapture with %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Calling StillImageSinkCaptureImage with %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Cannot begin moment capture since there is no FigCaptureSession instance"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Cannot set %@ since there is no FigCaptureSession instance"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Discarding old requests: %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Finished waiting for capture for uid:%lld (by uid:%lld)"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Finished waiting for processing for uid:%lld (by uid:%lld)"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Handling cancelled request: %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Handling matchingRequest request: %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) New IrisPreparedSettings is equal to old. Overriding request ID from %lld -> %lld to match old settings."
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Non-overlapping capture complete for uid:%lld (by uid:%lld)"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling %@ didFinishMovieCaptureForResolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to captureOutput:readyForResponsiveRequestAfterResolvedSettings:"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to didBeginCaptureForResolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to didBeginMovieCaptureForResolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to didCapturePhotoForResolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to didFinishCaptureForSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to didFinishMovieCaptureForResolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to didFinishRecordingLivePhotoMovieForEventualFileAtURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to didFinishRecordingMovie: or didFinishRecordingMovieFileAtEventualURL:%@ resolvedSettings:%@ previewPixelBuffer:NULL error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to didFinishWritingMovie:error: or didFinishWritingMovieFileAtURL:%@ debugMetadataSidecarFileURL:nil previewPixelBuffer:NULL duration:kCMTimeInvalid resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to readyForResponsiveRequestAfterResolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to willBeginCaptureBeforeResolvingSettingsForUniqueID:%lld"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to willBeginCaptureForResolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not calling, delegate %@ doesn't respond to willCapturePhotoForResolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not setting %@ since there is no FigCaptureSession instance"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Not setting livePhotoMovieProcessingSuspended since there is no FigCaptureSession instance"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Optimized dimensions: %d x %d"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Overscan percentage for offline vis: %f (Front: %@)"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) PreparationComplete error: (%d, %d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Received PreparationComplete notification for settingsID %lld"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Received a PreparationCompleteNotification from the past (mine=%lld, theirs=%lld)!!!"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Received will begin capture before resolving settings notification after capture has already started. Ignoring."
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Set %@ failed %d"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Set livePhotoMovieProcessingSuspended failed %d"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Set(%@) failed %d"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Unable to cancel moment capture (%lld) as FigCaptureSession has been deallocated!"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Unable to end moment capture (%lld) as FigCaptureSession has been deallocated!"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Using waiting for capture readiness for uid:%lld (by uid:%lld)"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Using waiting for processing readiness uid:%lld (by uid:%lld)"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [%d]calling %@ didFinishProcessingPhotoSampleBuffer:(null) previewPhotoSampleBuffer:(null) resolvedSettings:%@ bracketSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [%d]calling %@ didFinishProcessingRawPhotoSampleBuffer:(null) previewPhotoSampleBuffer:(null) resolvedSettings:%@ bracketSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***Original***] Not calling, delegate %@ doesn't respond to didFinishRecordingLivePhotoMovieForEventualFileAtURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***Original***] calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ debugMetadataSidecarFileURL:%@ duration:nans photoDisplayTime:nans resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***Original***] calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ duration:nans photoDisplayTime:nans metadataIdentifiers:@{} resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***Original***] calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ duration:nans photoDisplayTime:nans resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***Original***] calling %@ didFinishRecordingLivePhotoMovieForEventualFileAtURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***Original-OverCapture***] Not calling, delegate %@ doesn't respond to didFinishRecordingLivePhotoMovieForEventualFileAtURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***Original-OverCapture***] calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ debugMetadataSidecarFileURL:%@ duration:nans photoDisplayTime:nans resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***Original-OverCapture***] calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ duration:nans photoDisplayTime:nans metadataIdentifiers:@{} resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***Original-OverCapture***] calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ duration:nans photoDisplayTime:nans resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***Original-OverCapture***] calling %@ didFinishRecordingLivePhotoMovieForEventualFileAtURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***OverCapture***] Not calling %@ didFinishWritingMovieFileAtURL:%@ debugMetadataSidecarFileURL:nil previewPixelBuffer:NULL duration:kCMTimeInvalid resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***OverCapture***] Not calling, delegate %@ doesn't respond to didFinishRecordingLivePhotoMovieForEventualFileAtURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***OverCapture***] Not calling, delegate %@ doesn't respond to didFinishRecordingMovie: or didFinishRecordingMovieFileAtEventualURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***OverCapture***] calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ debugMetadataSidecarFileURL:%@ duration:nans photoDisplayTime:nans resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***OverCapture***] calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ duration:nans photoDisplayTime:nans metadataIdentifiers:@{} resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***OverCapture***] calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ duration:nans photoDisplayTime:nans resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***OverCapture***] calling %@ didFinishRecordingLivePhotoMovieForEventualFileAtURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***OverCapture***] calling %@ didFinishRecordingMovie:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***OverCapture***] calling %@ didFinishRecordingMovieFileAtEventualURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) [***OverCapture***] calling %@ didFinishWritingMovieFileAtURL:%@ debugMetadataSidecarFileURL:nil previewPixelBuffer:NULL duration:kCMTimeInvalid resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) _trackedPhotoSettingsArray after pruning %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) _trackedPhotoSettingsArray before pruning to > unique ID %lld: %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) _trackedPhotoSettingsArray before pruning unique ID %lld: %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) called"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) called with %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) called with %d"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) called with flags:%x request:%@, error: %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) called with preparedPhotoSettingsArray:%@ completionHandler:%p"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ captureOutput:readyForResponsiveRequestAfterResolvedSettings:"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didBeginMovieCaptureForResolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didCapturePhotoForResolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishCaptureForResolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishCapturingDeferredPhotoProxy:%@ error:%@ for photo with processing flags \"%@\""
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishMovieCaptureForResolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ debugMetadataSidecarFileURL:%@ duration:nans photoDisplayTime:nans resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ duration:nans photoDisplayTime:nans metadataIdentifiers:@{} resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishProcessingLivePhotoToMovieFileAtURL:%@ duration:nans photoDisplayTime:nans resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishProcessingPhoto:%@ error:%@ for photo with processing flags \"%@\""
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishProcessingPhotoFileAtURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishProcessingPhotoSampleBuffer:%p previewPhotoSampleBuffer:%p resolvedSettings:%@ bracketSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishProcessingRawPhotoSampleBuffer:%p previewPhotoSampleBuffer:%p resolvedSettings:%@ bracketSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishProcessingVideoFileAtURL:%@ resolvedSettings:%@ previewPixelBuffer:%p recordedDuration:%fs error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishProcessingVideoFileAtURL:%@ resolvedSettings:%@ previewPixelBuffer:NULL recordedDuration:kCMTimeInvalid error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishRecordingLivePhotoMovieForEventualFileAtURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishRecordingMovie:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishRecordingMovieFileAtEventualURL:%@ resolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishWritingMovie:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ didFinishWritingMovieFileAtURL:%@ debugMetadataSidecarFileURL:nil previewPixelBuffer:NULL duration:kCMTimeInvalid resolvedSettings:%@ error:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ readyForResponsiveRequestAfterResolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ willBeginCaptureBeforeResolvingSettingsForUniqueID:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ willBeginCaptureForResolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@ willCapturePhotoForResolvedSettings:%@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@%@ didFinishCapturingDeferredPhotoProxy:%@error:%@ for photo with processing flags \"%@\""
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling %@%@ didFinishProcessingPhoto:%@error:%@ for photo with processing flags \"%@\""
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling readinessCoordinator:captureReadinessDidChange: with initial readiness %d"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) calling readinessCoordinator:captureReadinessDidChange: with readiness %d"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) consolidateMovieFragmentsInFile:%@ failed (%d) for request captureID:%lld"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) no outputFileURL for captureID:%lld"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) sessionIsRunning changed %d -> %d"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) starting non-overlapping capture for uid:%lld"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) timed out waiting for Live Photos begin/end movie capture hosttime group to empty"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) timed out waiting for begin video recording sound to finish playing"
+ "<<<< AVCapturePhotoOutput >>>> %s: *** (%p) %@: Couldn't find a paired request for uniqueID %lld"
+ "<<<< AVCapturePhotoOutput >>>> %s: *** (%p) DidFinishCapture error: (%d, %d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: *** (%p) DidFinishMovieCapture error: (%d, %d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: *** (%p) DidFinishRecordingIrisMovie error: (%@, %d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: *** (%p) DidFinishWritingMomentCaptureMovie error: (%@, %d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: *** (%p) StillImageComplete error: (%d, %d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: *** (%p) no photo sample buffer returned, errorStatus = %d ***"
+ "<<<< AVCapturePhotoOutput >>>> %s: *** (%p) no photo surface returned, must have run out of memory! ***"
+ "<<<< AVCapturePhotoOutput >>>> %s: CMPhotoCompressionCreateDataContainerFromImage failed to convert preview sbuf to jpeg (%d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: Resolved dimensions: photo:%dx%d, preview:%dx%d (enabled:%d), thumbnail:%dx%d (enabled:%d), rawThumbnail:%dx%d (enabled:%d)"
+ "<<<< AVCapturePhotoOutput >>>> %s: captureReadiness changed %d -> %d, numberOfPhotoCapturesInflight %d, inflightNonOverlappingCaptureUniqueID %lld, inflightIndeterminateReadinessCaptureUniqueID %lld"
+ "<<<< AVCapturePhotoOutput >>>> %s: captureReadiness did not change: %d, numberOfPhotoCapturesInflight %d, inflightNonOverlappingCaptureUniqueID %lld"
+ "<<<< AVCapturePhotoOutput >>>> %s: starting non-overlapping capture for uid:%lld"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) %@ : %@"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) Client is running inside of mediaserverd, and should be passing nil for the callback queue!  This check will be removed in the future and an exception will be thrown!"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) Got unexpected dequeue error: %d"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) Got unknown opType %d"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) calling %@ didDropPointCloudData:%@ ts:%f reason:%d"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) calling %@ didOutputPointCloudData:%@ ts:%f"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) configurationID %lld became live with updated format description %@"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) setting delegate to %@ (%p)"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) setting delegate to nil"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) setting delegateOverride to %@ (%p)"
+ "<<<< AVCapturePointCloudDataOutput >>>> %s: (%p) setting delegateOverride to nil"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: %@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: %@ presists observer %@ for key %@, but couldn't find a valid changeHandler"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: *finally* listening to server change notifications for %@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Could not create pixel buffer: %d"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to copy value for %@, error:%d, source:%p"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to get camera history override list, error:%d, source:%p"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to get proprietary defaults for audit token, error:%d, source:%p"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to re-register ProprietaryDefaultChanges notifications for %@, error:%d, source:%p"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to register ProprietaryDefaultChanges notifications for %@, error:%d"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to register ProprietaryDefaultChanges notifications for %@, error:%d, source:%p"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to remove ProprietaryDefaultChanges notifications for %@, error:%d, source:%p"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to set camera history %@ override %@, error:%d, source:%p"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to set value %@ for %@, error:%d, source:%p"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to set value %@ for wildcard key %@, error:%d, source:%p"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to update camera history %@ for %@, error:%d, source:%p"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Got %d proprietaryDefaultsSource but expecting one"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Updating _proprietaryDefaultsSource from %p to %p"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: already observing %@ for %@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: could not find observers for key %@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: currently not observing %@ for %@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: error resolving bookmark %@: %@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: first observer for %@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: loading imageForKey %@: %s"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: no longer listening to change notifications for %@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: no longer observing %@ for %@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: now listening to server change notifications for %@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: now observing %@ for %@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: removed last observer for %@"
+ "<<<< AVCaptureSession >>>> %s: %@"
+ "<<<< AVCaptureSession >>>> %s: %p called"
+ "<<<< AVCaptureSession >>>> %s: (%p) %@"
+ "<<<< AVCaptureSession >>>> %s: (%p) %@: %@"
+ "<<<< AVCaptureSession >>>> %s: (%p) (thread %p) Triggering buildAndRunGraph for audioInputRouteIsBuiltInMic change %{public}@ current audioCaptureMode %ld on input %{public}@"
+ "<<<< AVCaptureSession >>>> %s: (%p) Cancel requested to happen %.1f seconds from now"
+ "<<<< AVCaptureSession >>>> %s: (%p) Creating new FigCaptureSession (local!)"
+ "<<<< AVCaptureSession >>>> %s: (%p) Creating new FigCaptureSessionRemote"
+ "<<<< AVCaptureSession >>>> %s: (%p) Failed to build and run capture session (%@) (%d)!"
+ "<<<< AVCaptureSession >>>> %s: (%p) NOT posting AVCaptureSessionDidStartRunningNotification due to _buildAndRunGraph failure"
+ "<<<< AVCaptureSession >>>> %s: (%p) NOT posting AVCaptureSessionDidStartRunningNotification, we are interrupted."
+ "<<<< AVCaptureSession >>>> %s: (%p) Smart style rendering is disabled because active format doesn't support it %@"
+ "<<<< AVCaptureSession >>>> %s: (%p) Smart style rendering is disabled for multi-cam session"
+ "<<<< AVCaptureSession >>>> %s: (%p) Smart style rendering is disabled for panorama capture"
+ "<<<< AVCaptureSession >>>> %s: (%p) Smart style rendering is disabled for spatial photo capture"
+ "<<<< AVCaptureSession >>>> %s: (%p) Smart style rendering is disabled for spatial video capture"
+ "<<<< AVCaptureSession >>>> %s: (%p) Smart style rendering is disabled for time-lapse capture"
+ "<<<< AVCaptureSession >>>> %s: (%p) Smart style rendering is disabled for video mode and active format is not photo format %@"
+ "<<<< AVCaptureSession >>>> %s: (%p) Timed out waiting for configuration to become live"
+ "<<<< AVCaptureSession >>>> %s: (%p) Timed out waiting for session to start"
+ "<<<< AVCaptureSession >>>> %s: (%p) Timed out waiting for session to stop"
+ "<<<< AVCaptureSession >>>> %s: (%p) Timed out with unknown reason"
+ "<<<< AVCaptureSession >>>> %s: (%p) _stopFigCaptureSession failed with error %d"
+ "<<<< AVCaptureSession >>>> %s: (%p) called: %{public}@, %{public}@"
+ "<<<< AVCaptureSession >>>> %s: (%p) currentThread %@ isMainThread:%d, threadWhichBeganConfiguration %@ isMainThread:%d, isBeingConfiguredOnCurrentThread %d"
+ "<<<< AVCaptureSession >>>> %s: (%p) failed (%d)"
+ "<<<< AVCaptureSession >>>> %s: (%p) posting AVCaptureDeviceDidStartRunningNotification for %@"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) BACK FROM WAITING FOR START timedOut = %d, stillWaiting = %d (should be 0)<-------------------------------------------------"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) BACK FROM WAITING FOR STOP timedOut = %d, stillWaiting = %d (should be 0)<-------------------------------------------------"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) ServerConnectionDied"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) WAITING FOR START--------------------------------------->"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) WAITING FOR STOP--------------------------------------->"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) kFigCaptureSessionError_AudioServerConnectionDied"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) kFigCaptureSessionError_SessionNotRunning"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) kFigCaptureSessionError_UnrecoverableError"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) locking"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) locking for ConfigurationCommitted (configID = %lld)"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) locking for ConfigurationDidBecomeLive (configID = %lld)"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) locking for DidStartRunning"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) locking for DidStopRunning"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) locking to call FigCaptureSessionStop"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) not calling waitInMode:, since FigCaptureSession won't be sending any notifications"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) signalling for ConfigurationCommitted (configID = %lld)"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) signalling for ConfigurationDidBecomeLive (configID = %lld)"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) signalling for DidStartRunning"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) signalling for DidStopRunning"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) signalling for ServerConnectionDied"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) unlocking"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) unlocking for ConfigurationCommitted (configID = %lld)"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) unlocking for ConfigurationDidBecomeLive (configID = %lld)"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) unlocking for DidStartRunning"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) unlocking for DidStopRunning"
+ "<<<< AVCaptureSession >>>> %s: (%p)(pthread:%p) unlocking for ServerConnectionDied"
+ "<<<< AVCaptureSession >>>> %s: (%p)*** Device just became %s."
+ "<<<< AVCaptureSession >>>> %s: (%p)Stopping and uninitializing graph"
+ "<<<< AVCaptureSession >>>> %s: (%p)failureReason = %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Ignoring active color space change (a session is configuring it automatically) %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Ignoring active color space change (device.activeFormat just changed to a non wide-color format) %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Ignoring active depth data format change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Ignoring active depth data format change (it didn't really change) %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Ignoring active format change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Ignoring active format change while preset = InputPriority (I didn't do it, but nothing's changed) %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Setting preset to input priority *WITHOUT triggering buildAndRunGraph* (because nothing really changed) for change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Setting preset to input priority and triggering buildAndRunGraph for change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for activeColorSpace change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for backgroundBlurActive change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for backgroundReplacementActive change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for centerStageActive change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for client-initiated activeDepthDataFormat change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for client-initiated videoHDREnabled change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for gazeSelectionEnabled change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for geometricDistortionCorrectionEnabled change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for lensSmudgeDetectionEnabled change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for lowLightVideoCaptureEnabled change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for manualFramingEnabled change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for manualFramingPanningAngleX change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for manualFramingPanningAngleY change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for reactionEffectsActive change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for studioLightingActive change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for variableFrameRateVideoCaptureEnabled change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for videoStabilizationStrength change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for videoZoomFactor change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph while preset = InputPriority for change %@"
+ "<<<< AVCaptureSession >>>> %s: AVCaptureSession.dot file written to %@ string:\n%@"
+ "<<<< AVCaptureSession >>>> %s: Aggregate connection max frame rate (%f) is too high, changing it to %f"
+ "<<<< AVCaptureSession >>>> %s: Aggregate connection max frame rate (%f) is too low, changing it to %f"
+ "<<<< AVCaptureSession >>>> %s: Aggregate connection min frame rate (%f) is too high, changing it to %f"
+ "<<<< AVCaptureSession >>>> %s: Aggregate connection min frame rate (%f) is too low, changing it to %f"
+ "<<<< AVCaptureSession >>>> %s: Already shown opt-out message for bundleID: %@"
+ "<<<< AVCaptureSession >>>> %s: Altering default video frame rate range to %lld-%d to maximize depth frame rate (%d)"
+ "<<<< AVCaptureSession >>>> %s: Cancel prewarming %{private}@ with options: %@"
+ "<<<< AVCaptureSession >>>> %s: Computed NAND cost for %@ is %f"
+ "<<<< AVCaptureSession >>>> %s: Could not display Smart Styles Alert due to missing bundle name"
+ "<<<< AVCaptureSession >>>> %s: Could not find LSApplicationRecord for bundleID: %@"
+ "<<<< AVCaptureSession >>>> %s: Couldn't find an AVCaptureSessionConfiguration for committed config with id %lld"
+ "<<<< AVCaptureSession >>>> %s: Encoder bandwidth for %@ output (%dx%d): %dMP/s"
+ "<<<< AVCaptureSession >>>> %s: Encoder cost: %f (%d / %d)"
+ "<<<< AVCaptureSession >>>> %s: FigCaptureSessionRemoteCreate error %d retry %d"
+ "<<<< AVCaptureSession >>>> %s: Got interrupted: %d"
+ "<<<< AVCaptureSession >>>> %s: Hardware cost: %f"
+ "<<<< AVCaptureSession >>>> %s: Ignored active control update because the session was deallocated"
+ "<<<< AVCaptureSession >>>> %s: Ignored active control update for unknown control"
+ "<<<< AVCaptureSession >>>> %s: Ignored active control update from unknown controls overlay"
+ "<<<< AVCaptureSession >>>> %s: Ignored focus locked update because the session was deallocated"
+ "<<<< AVCaptureSession >>>> %s: Ignored interface-reduced update because the session was deallocated"
+ "<<<< AVCaptureSession >>>> %s: Ignored interface-reduced update from unknown controls overlay"
+ "<<<< AVCaptureSession >>>> %s: Ignored visibility update because the session was deallocated"
+ "<<<< AVCaptureSession >>>> %s: Ignored visibility update from unknown controls overlay"
+ "<<<< AVCaptureSession >>>> %s: Interrupted with unexpected fig interruption reason (%d)"
+ "<<<< AVCaptureSession >>>> %s: MSR bandwidth for %@ output: %d MP/s"
+ "<<<< AVCaptureSession >>>> %s: Memory cost: %f (%d / %d)"
+ "<<<< AVCaptureSession >>>> %s: Memory for RAW buffers: %dMB"
+ "<<<< AVCaptureSession >>>> %s: Memory for photo output: %dMB"
+ "<<<< AVCaptureSession >>>> %s: Memory for video encoder: %dMB"
+ "<<<< AVCaptureSession >>>> %s: Memory for video preview layer: %dMB"
+ "<<<< AVCaptureSession >>>> %s: Memory for video/movie output: %dMB"
+ "<<<< AVCaptureSession >>>> %s: New fcs config: %@"
+ "<<<< AVCaptureSession >>>> %s: Not calling -session:didChangeActiveControl: on delegate on an unsupported client"
+ "<<<< AVCaptureSession >>>> %s: Not calling -session:didChangeFocusLocked: on delegate on an unsupported client"
+ "<<<< AVCaptureSession >>>> %s: Not removing AVCaptureSessionConfiguration with configID %lld, since the commit operation failed with err %d, and the app may restart with the same config."
+ "<<<< AVCaptureSession >>>> %s: Old fcs config: %@"
+ "<<<< AVCaptureSession >>>> %s: Picked a different activeFormat for wide color: %@"
+ "<<<< AVCaptureSession >>>> %s: Prewarm %{private}@ with options: %@"
+ "<<<< AVCaptureSession >>>> %s: Removing orphaned AVCaptureSessionConfiguration with configID %lld"
+ "<<<< AVCaptureSession >>>> %s: Session %@ non-spatial audio configuration %@ is valid"
+ "<<<< AVCaptureSession >>>> %s: Session %@ spatial audio configuration %@ is valid"
+ "<<<< AVCaptureSession >>>> %s: SmartStyles - CFUserNotificationCreate gave error %d"
+ "<<<< AVCaptureSession >>>> %s: Started running while interrupted, so ending interruption: (%d, %d)"
+ "<<<< AVCaptureSession >>>> %s: Starting fig capture session"
+ "<<<< AVCaptureSession >>>> %s: The fig capture session is already running. Will not start session."
+ "<<<< AVCaptureSession >>>> %s: Total NAND cost: %f"
+ "<<<< AVCaptureSession >>>> %s: VEFrameRate Throttling (%p) : needToThrottle (%d) minFDSetByClient: (%d) maxFDSetByClient: (%d). newMaxFD: ( %lld / %d ) newMinFD: ( %lld / %d )."
+ "<<<< AVCaptureSession >>>> %s: Video/Movie output cost: %f (bandwidth: %d / %d, outputs: %d, VIS: %d / %d)"
+ "<<<< AVCaptureSession >>>> %s: called while session is not running."
+ "<<<< AVCaptureSession >>>> %s: resetting the active min/max frame rate to the default values"
+ "<<<< AVCaptureSession >>>> %s: updating %@ to %@"
+ "<<<< AVCaptureSpatialAudioMetadataSampleGenerator >>>> %s: AVCaptureSpatialAudioMetadataSampleGenerator: node init FAILED"
+ "<<<< AVCaptureSpatialAudioMetadataSampleGenerator >>>> %s: AVCaptureSpatialAudioMetadataSampleGenerator: node init."
+ "<<<< AVCaptureSpatialAudioMetadataSampleGenerator >>>> %s: failed to allocate CMCaptureSpatialAudioMetadataSampleGenerator"
+ "<<<< AVCaptureSpatialAudioMetadataSampleGenerator >>>> Fig"
+ "<<<< AVCaptureStillImageOutput >>>> %s: #### maxDataSize reported as 0 ####"
+ "<<<< AVCaptureStillImageOutput >>>> %s: %d"
+ "<<<< AVCaptureStillImageOutput >>>> %s: *** no image data sbuf found -- we were expecting one, assuming out of memory ***"
+ "<<<< AVCaptureStillImageOutput >>>> %s: *** no jpeg surface returned, must have run out of memory! ***"
+ "<<<< AVCaptureStillImageOutput >>>> %s: :%s"
+ "<<<< AVCaptureStillImageOutput >>>> %s: Bracket preparation error invalid settingsID %lld"
+ "<<<< AVCaptureStillImageOutput >>>> %s: CMBlockBufferCreateContiguous failed (%d)"
+ "<<<< AVCaptureStillImageOutput >>>> %s: CMBlockBufferGetDataPointer failed (%d)"
+ "<<<< AVCaptureStillImageOutput >>>> %s: Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCaptureStillImageOutput >>>> %s: Image CustomRendered tag is %d"
+ "<<<< AVCaptureStillImageOutput >>>> %s: Still image capture error invalid settingsID %lld"
+ "<<<< AVCaptureStillImageOutput >>>> %s: Still image capture error: (%d, %d)"
+ "<<<< AVCaptureStillImageOutput >>>> %s: Still image prepare bracket error: (%d, %d)"
+ "<<<< AVCaptureStillImageOutput >>>> %s: called"
+ "<<<< AVCaptureStillImageOutput >>>> %s: called with %@"
+ "<<<< AVCaptureStillImageOutput >>>> %s: calling bracketedCaptureCompletionBlock with %@, error: %@"
+ "<<<< AVCaptureStillImageOutput >>>> %s: calling iosurfaceCompletionBlock with %@, %d, %@, %d, %@, error: %@"
+ "<<<< AVCaptureStillImageOutput >>>> %s: calling sbufCompletionBlock with %@, error: %@"
+ "<<<< AVCaptureStillImageOutput >>>> %s: isPrepared = %d"
+ "<<<< AVCaptureSystemExposureBiasSlider >>>> %s: %@ Ignoring out-of-bounds exposure target bias %.2f"
+ "<<<< AVCaptureSystemLensSelector >>>> %s: %@ Ignoring out-of-bounds zoom factor %.2f"
+ "<<<< AVCaptureSystemStylePicker >>>> %s: %@ Ignoring out-of-bounds smart style request at index %d"
+ "<<<< AVCaptureSystemZoomSlider >>>> %s: %@ Ignoring out-of-bounds zoom factor %.2f"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: %lld / %d (%f fps)"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) %@ : %@"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) Client is running inside of mediaserverd, and should be passing nil for the callback queue!  This check will be removed in the future and an exception will be thrown!"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) Got unexpected dequeue error: %d"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) Got unknown opType %d"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) Observed change in mirroring on connection from %@ to %@"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) Observed change in orientation on connection from %@ to %@"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) Observed change in sessionPreset from %@ to %@"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) activeFormat changed to %@"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) calling %@ didDropSampleBuffer:%p"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) calling %@ didOutputSampleBuffer:%p"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) configurationID %lld became live with updated format description %@"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) setting delegateOverride to %@ (%p)"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) setting delegateOverride to nil"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) setting sampleBufferDelegate to %@ (%p)"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: (%p) setting sampleBufferDelegate to nil"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@ %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@ Output size: %d, %d. Estimated preview size: %d, %d;"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@ have pending primary capture rect change"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@ received notification %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@ setting pending primary capture rect on FigCaptureSession %p"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %{public}@: Posting AVCaptureVideoPreviewLayerDidBecomeVisibleNotification"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %{public}@: imageQueueSlot = %u. %{public}@ Forcing a crash."
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %{public}@: imageQueueSlot: %u, imageQueue: %{public}@, rotationDegrees: %.0f, size: %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %{public}@: posting AVCaptureVideoPreviewLayerDidStartRunningNotification"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %{public}@: preview started - contents = %{public}@, imageQueueSlot = %u"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) %@ : %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) %@->%@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) %d"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) (pthread %p)"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) (pthread %p)PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) NOT centering sublayer because it's already centered"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) called"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) called enable %d"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) called with %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) called with %@ animated:%d"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) called with %d"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) called with styles:%@ regions:%@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) new preview format: %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) previewMirrored changed %d -> %d"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) update sensor:%@ preview:%@ vt:%@ front:%d orientation:%d bounds:%@ gravity:%@ mirrored:%d"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: Changing zoomPictureInPictureOverlaySupported to %d"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: Created semantic style set: %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: Failed to set PortraitLightingEffectStrength to %.2f (err:%d)"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: Invalid source dimensions"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: Return CATransform3DIdentity because previewSize is CGSizeZero"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: Set PrimaryCaptureRect is taking more than %.0f seconds."
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: Set PrimaryCaptureRect took %.3f seconds, started at %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: Updating Zoom PIP overlay rect to %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: originalRotationDegrees:%i previewRotationDegrees:%i finalRotationDegrees:%i isMirrored:%i"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: overCaptureStatus %d -> %d, rampingVideoZoom %d"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: previewAspectRatio %f, primaryCaptureRectCenterPoint %@, centerOffset %@, centerOffsetTranslationScale %@, previewAspectRelativeToSensor %f, centerOffsetTranslation %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: previewAspectRatio %f, sensorAspectRatio %f, primaryCaptureRectAspectRatio %f, primaryCaptureRectAspectRatioScale %f"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: previewSize = %@, containerSize = %@, scaleX = %f, scaleY = %f"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: returnTransform [ %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f ]"
+ "<<<< AVCaptureVideoThumbnailOutput >>>> %s: %@"
+ "<<<< AVCaptureVideoThumbnailOutput >>>> %s: %@ received notification %@"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) %@ : %@"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) Client is running inside of mediaserverd, and should be passing nil for the callback queue!  This check will be removed in the future and an exception will be thrown!"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) Disregarding notification %@ since sinkIDs don't match"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) Got unexpected dequeue error: %d"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) Got unknown opType %d"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) activeFormat changed to %@"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) calling %@ didDropVisionDataPixelBufferForTimestamp:%p reason:%d"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) calling %@ didOutputVisionDataPixelBuffer:%p"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) configurationID %lld became live with updated format description %@"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) setting delegate to %@ (%p)"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) setting delegate to nil"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) setting delegateOverride to %@ (%p)"
+ "<<<< AVCaptureVisionDataOutput >>>> %s: (%p) setting delegateOverride to nil"
+ "<<<< AVControlCenterModules >>>> %s: %@ is opted in for BB:%d SL:%d RE:%d BR:%d"
+ "<<<< AVControlCenterModules >>>> %s: %@ isManualFramingEnabled:%@"
+ "<<<< AVControlCenterModules >>>> %s: %@: send notification for one-shot framing completion"
+ "<<<< AVControlCenterModules >>>> %s: %@: send notification for reset framing completion"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( controlMode != _backgroundBlurControlMode ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectControlModeDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( controlMode != _centerStageControlMode ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectControlModeDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( controlMode != _studioLightingControlMode ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectControlModeDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( intensityValue != _backgroundBlurAperture ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectIntensityDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( intensityValue != _studioLightingIntensity ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectIntensityDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _backgroundBlurEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _backgroundReplacementEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _centerStageEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _gesturesEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _reactionsEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _studioLightingEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( url != _backgroundReplacementURL ) is %@, NOT sending AVControlCenterVideoEffectsBackgroundReplacementURLDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, _hiddenMicrophoneModes = %@, ! [hiddenMicModes isEqual:_hiddenMicrophoneModes] is %@, NOT sending AVControlCenterMicrophoneModesModuleHiddenMicrophoneModesDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, autoMicModeSupported = %@, ( autoEnabled != _autoMicModeEnabled ) is %@, NOT sending AVControlCenterMicrophoneModesModuleAutoEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, micModesSupported = %@, ! [supportedMicModes isEqual:_supportedMicrophoneModes] is %@, NOT sending AVControlCenterMicrophoneModesModuleSupportedMicrophoneModesDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, micModesSupported = %@, ( activeMicMode != _activeMicrophoneMode ) is %@, NOT sending AVControlCenterMicrophoneModesModuleActiveMicrophoneModeDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, micModesSupported = %@, ( bypassVoiceProcessing != _auVoiceIOBypassVoiceProcessing ) is %@, NOT sending AVControlCenterMicrophoneModesModuleVoiceProcessingBypassedDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, micModesSupported = %@, ( micMode != _microphoneMode ) is %@, NOT sending AVControlCenterMicrophoneModesModuleMicrophoneModeDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _activeMicrophoneMode from %d to %d"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _auVoiceIOBypassVoiceProcessing from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _autoMicModeEnabled from %d to %d"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _backgroundBlurAperture from %f to %f"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _backgroundBlurControlMode from %d to %d"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _backgroundBlurEnabled from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _backgroundReplacementEnabled from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _backgroundReplacementURL from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _centerStageControlMode from %d to %d"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _centerStageEnabled from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _gesturesEnabled from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _hiddenMicrophoneModes from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _microphoneMode from %d to %d"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _reactionsEnabled from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _studioLightingControlMode from %d to %d"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _studioLightingEnabled from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _studioLightingIntensity from %f to %f"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _supportedMicrophoneModes from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %s blackenFrames from deviceID %@ for bundleID %@"
+ "<<<< AVControlCenterModules >>>> %s: %{public}@ videoEffectsShouldBeShown:%d micModesShouldBeShown:%d"
+ "<<<< AVControlCenterModules >>>> %s: Auto mic mode is not supported on this platform, ignoring setAutoMicrophoneModeEnabled:%d"
+ "<<<< AVControlCenterModules >>>> %s: BundleID %@, current selected manual framing device type %d, manualFramingDefaultZoomFactor %.3f"
+ "<<<< AVControlCenterModules >>>> %s: Mic modes are not supported on this platform, ignoring setMicrophoneMode:%@"
+ "<<<< AVControlCenterModules >>>> %s: Missing the value for dockedTrackingActiveChanged notification"
+ "<<<< AVControlCenterModules >>>> %s: Pan with translation at [%.3f, %.3f] on %@"
+ "<<<< AVControlCenterModules >>>> %s: Received the wrong type for eligible effects array for %@"
+ "<<<< AVControlCenterModules >>>> %s: Received wrong value type for gestures-disabled notification request: %@"
+ "<<<< AVControlCenterModules >>>> %s: Start panning at [%.3f, %.3f] on %@"
+ "<<<< AVControlCenterModules >>>> %s: Unknown PTEffectReactionType %d for effect %@"
+ "<<<< AVControlCenterModules >>>> %s: bookmarkDataWithOptions error: %@"
+ "<<<< AVControlCenterModules >>>> %s: error resolving bookmark %@: %@"
+ "<<<< AVControlCenterModules >>>> %s: for %@, preferenceDomain:%@"
+ "<<<< AVControlCenterModules >>>> %s: panningAngles [x:%f,y:%f], defaultPanningAngles [x:%f,y:%f], currentPanningAnglesAtDefault:%@, newOriginalZoomFactor: %f, default original zoom factor: %f, newZoomFactorAtDefault:%@"
+ "<<<< AVControlCenterModules >>>> %s: panningAngles [x:%f,y:%f], defaultPanningAngles [x:%f,y:%f], newPanningAnglesAtDefault:%@, currentOriginalZoomFactor: %f, default original zoom factor: %f, zoomFactorAtDefault:%@"
+ "<<<< AVDepthData >>>> %s: CVPixelBufferCreate failed (%d)"
+ "<<<< AVDepthData >>>> %s: CVPixelBufferLockBaseAddress failed (%d)"
+ "<<<< AVDepthData >>>> %s: Failed to create rotated pixel buffer"
+ "<<<< AVDepthData >>>> %s: FigDepthConvertBuffer failed (%d)"
+ "<<<< AVDepthData >>>> %s: FigDepthRotateBuffer reported failure (%d)"
+ "<<<< AVDepthData >>>> %s: Pixel buffer copy failed (%d)"
+ "<<<< AVExternalStorageDevice >>>>"
+ "<<<< AVExternalStorageDevice >>>> %s: %@:%@"
+ "<<<< AVExternalStorageDevice >>>> %s: AVExternalStorageDeviceDiscoverySession callback"
+ "<<<< AVExternalStorageDevice >>>> %s: Adding AVExternalStorageDevice %p with UUID %@ (base URL %@) to list %@"
+ "<<<< AVExternalStorageDevice >>>> %s: After values: ExternalStorageDeviceManager %p, UUID %@"
+ "<<<< AVExternalStorageDevice >>>> %s: Before values: ExternalStorageDeviceManager %p, UUID %@"
+ "<<<< AVExternalStorageDevice >>>> %s: Callback %lu %lu"
+ "<<<< AVExternalStorageDevice >>>> %s: Called"
+ "<<<< AVExternalStorageDevice >>>> %s: Checking if %@ disconnected with stored array %@ callback array %@"
+ "<<<< AVExternalStorageDevice >>>> %s: Creating AVExternalStorageDevice for %@"
+ "<<<< AVExternalStorageDevice >>>> %s: Failed to get NSURLVolumeTypeNameKey on baseURL"
+ "<<<< AVExternalStorageDevice >>>> %s: Failed to get resourceValuesForKeys on baseURL"
+ "<<<< AVExternalStorageDevice >>>> %s: FigExternalStorageDeviceManagerCheckAuthorizationStatus err = %d."
+ "<<<< AVExternalStorageDevice >>>> %s: FigExternalStorageDeviceManagerCheckAuthorizationStatus result was kFigExternalStorageDeviceAuthorizationStatusAuthorized"
+ "<<<< AVExternalStorageDevice >>>> %s: FigExternalStorageDeviceManagerCheckAuthorizationStatus result was kFigExternalStorageDeviceAuthorizationStatusDenied"
+ "<<<< AVExternalStorageDevice >>>> %s: FigExternalStorageDeviceManagerCheckAuthorizationStatus result was kFigExternalStorageDeviceAuthorizationStatusNotDetermined"
+ "<<<< AVExternalStorageDevice >>>> %s: FigExternalStorageDeviceManagerMonitorBeginMonitoring err = %d."
+ "<<<< AVExternalStorageDevice >>>> %s: FigExternalStorageDeviceManagerMonitorRemoteCreate err = %d."
+ "<<<< AVExternalStorageDevice >>>> %s: FigExternalStorageDeviceManagerRef is NULL"
+ "<<<< AVExternalStorageDevice >>>> %s: FigExternalStorageDeviceManagerRemoteCreate error: %d sleep time (ms) before retrying: %d"
+ "<<<< AVExternalStorageDevice >>>> %s: Recovering from mediaserverd crash: %lu devices to restore"
+ "<<<< AVExternalStorageDevice >>>> %s: Recovering from mediaserverd crash: AVExternalStorageDevice %p was not found. Removing from the list."
+ "<<<< AVExternalStorageDevice >>>> %s: Recovering from mediaserverd crash: baseURL %@ deviceURL %@"
+ "<<<< AVExternalStorageDevice >>>> %s: Recovering from mediaserverd crash: looping through AVExternalStorageDevice %p"
+ "<<<< AVExternalStorageDevice >>>> %s: Recovering from mediaserverd crash: looping through UUID %@"
+ "<<<< AVExternalStorageDevice >>>> %s: Recovering from mediaserverd crash: updating underlying parameters."
+ "<<<< AVExternalStorageDevice >>>> %s: Removing AVExternalStorageDevice %p with UUID %@ from externalStorageDevice list %@"
+ "<<<< AVExternalStorageDevice >>>> %s: Removing UUID %@ from detected list %@"
+ "<<<< AVExternalStorageDevice >>>> %s: Returning _checkAuthorizationStatus"
+ "<<<< AVExternalStorageDevice >>>> %s: Returning _requestAuthorization"
+ "<<<< AVExternalStorageDevice >>>> %s: The drive is of type apfs"
+ "<<<< AVExternalStorageDevice >>>> %s: The drive is of type msdos"
+ "<<<< AVExternalStorageDevice >>>> %s: URL array allocation failed."
+ "<<<< AVExternalStorageDevice >>>> %s: Unable to allocate/init AVExternalStorageDeviceDiscoverySession"
+ "<<<< AVExternalStorageDevice >>>> %s: Unable to copy property 'base URL'"
+ "<<<< AVExternalStorageDevice >>>> %s: Unable to copy property 'connected'"
+ "<<<< AVExternalStorageDevice >>>> %s: Unable to copy property 'display name'"
+ "<<<< AVExternalStorageDevice >>>> %s: Unable to copy property 'freeSize'"
+ "<<<< AVExternalStorageDevice >>>> %s: Unable to copy property 'is encrypted'"
+ "<<<< AVExternalStorageDevice >>>> %s: Unable to copy property 'totalSize'"
+ "<<<< AVExternalStorageDevice >>>> %s: Unable to copy property 'uniqueIdentifier'"
+ "<<<< AVExternalStorageDevice >>>> %s: Unable to get next available URL"
+ "<<<< AVExternalStorageDevice >>>> %s: Unable to get security scoped URL wrapper"
+ "<<<< AVExternalStorageDevice >>>> %s: [%@] nextAvailableURLsWithPathExtensions error %d"
+ "<<<< AVFlashlight >>>> %s: %@:%@"
+ "<<<< AVFlashlight >>>> %s: %p setting available from %d to %d"
+ "<<<< AVFlashlight >>>> %s: %p setting beam width from %f to %f"
+ "<<<< AVFlashlight >>>> %s: %p setting beam width from %g to %g"
+ "<<<< AVFlashlight >>>> %s: %p setting level from %g to %g"
+ "<<<< AVFlashlight >>>> %s: %p setting overheated from %d to %d"
+ "<<<< AVFlashlight >>>> %s: Called (%p)"
+ "<<<< AVFlashlight >>>> %s: Called (%p), returning %d"
+ "<<<< AVFlashlight >>>> %s: Called (%p), returning %f"
+ "<<<< AVFlashlight >>>> %s: FigFlashlightRemoteCreate error %d retry %d"
+ "<<<< AVFlashlight >>>> %s: beamWidth %f, beamWidthNormalized %f"
+ "<<<< AVFlashlight >>>> %s: called (%p), returning %d"
+ "<<<< AVFlashlight >>>> %s: called (%p), returning %f"
+ "<<<< AVFlashlight >>>> %s: called (%p), returning %g"
+ "<<<< AVFlashlight >>>> %s: failed to set beam width (%f) with err (%d)"
+ "<<<< AVFlashlight >>>> %s: failed to set level (%d)"
+ "<<<< AVFlashlight >>>> %s: failed to turn power off (%d)"
+ "<<<< AVFlashlight >>>> %s: failed to turn power on (%d)"
+ "<<<< AVFlashlight >>>> %s: minBeamWidth %f is greater than maxBeamWidth %f. Something is wrong, disabling beam width control"
+ "<<<< AVFlashlight >>>> %s: minBeamWidth %f, maxBeamWidth %f"
+ "<<<< AVGestalt >>>> %s: DeviceFeatures versions Spreadsheet = %@, Header = %@, Source = %@"
+ "<<<< AVMetadataMachineReadableCodeObject >>>> %s: Unexpected Quagga QR error correction level: %ld"
+ "<<<< AVOfflineVideoStabilizer >>>>"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: CMSampleBufferCreateForImageBuffer failed (%d)"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: CMVideoFormatDescriptionCreateForImageBuffer failed (%d)"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: Client only provided %d frames of priming metadata instead of the desired %d"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: Client provided a bad pixel buffer (%d)"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: Client provided bad metadata (%d)"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: Rejecting metadata dictionary since it contains keys we don't understand: %@"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: Rejecting metadata dictionary since it is missing the following required keys: %@"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: Source pixel buffer sample time doesn't match the metadata sample time for the same frame number"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: The head of the output sbuf queue contained an error: %d"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: Unable to prepare to process vis processor"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: Unable to stabilize a frame"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: VIS processor failed to finish pending processing (%d)"
+ "<<<< AVOfflineVideoStabilizer >>>> %s: err == 0, but no sample buffer was returned"
+ "<<<< AVPortraitEffectsMatte >>>> %s: CVPixelBufferCreate failed (%d)"
+ "<<<< AVPortraitEffectsMatte >>>> %s: CVPixelBufferLockBaseAddress failed (%d)"
+ "<<<< AVPortraitEffectsMatte >>>> %s: Failed to create rotated pixel buffer"
+ "<<<< AVPortraitEffectsMatte >>>> %s: VTPixelRotationSessionCreate failed (%d)"
+ "<<<< AVPortraitEffectsMatte >>>> %s: VTPixelRotationSessionRotateImage failed (%d)"
+ "<<<< AVPortraitEffectsMatte >>>> %s: VTPixelTransferSessionCreate failed (%d)"
+ "<<<< AVPortraitEffectsMatte >>>> %s: VTPixelTransferSessionTransferImage failed (%d)"
+ "<<<< AVSemanticSegmentationMatte >>>> %s: CVPixelBufferCreate failed (%d)"
+ "<<<< AVSemanticSegmentationMatte >>>> %s: CVPixelBufferLockBaseAddress failed (%d)"
+ "<<<< AVSemanticSegmentationMatte >>>> %s: Failed to create rotated pixel buffer"
+ "<<<< AVSemanticSegmentationMatte >>>> %s: VTPixelRotationSessionCreate failed (%d)"
+ "<<<< AVSemanticSegmentationMatte >>>> %s: VTPixelRotationSessionRotateImage failed (%d)"
+ "<<<< AVSemanticSegmentationMatte >>>> %s: VTPixelTransferSessionCreate failed (%d)"
+ "<<<< AVSemanticSegmentationMatte >>>> %s: VTPixelTransferSessionTransferImage failed (%d)"
+ "<<<< AVSmartStyleSettings >>>> %s: Posting Notification ( %@ ). userInfo: %@"
+ "<<<< AVSmartStyleSettings >>>> %s: Skip writing SystemStyleEnabled (%d) for bundleID (%@)."
+ "<<<< AVSmartStyleSettings >>>> %s: SystemStyleEnabled Dictionary is empty!"
+ "<<<< AVSmartStyleSettings >>>> %s: SystemStyleEnabled dict or entry for bundleID ( %@ ) is not found!"
+ "<<<< AVSmartStyleSettings >>>> %s: Updating System Style %@ : %@"
+ "<<<< AVSmartStyleSettings >>>> %s: Updating System Style Enabled %@ : %d"
+ "<<<< AVVirtualCaptureCard >>>> %s: FigVirtualCaptureCardRemoteCreate err = %d"
+ "<<<< AVVirtualCaptureCard >>>> %s: Returning capacity %lld"
+ "<<<< AVVirtualCaptureCard >>>> %s: Returning freeSpace %lld"
+ "<<<< AVVirtualCaptureCard >>>> %s: Setting newCapacity to %@"
+ "<<<< AVVirtualCaptureCard >>>> %s: Unable to allocate/init AVVirtualCaptureCard"
+ "<<<< AVVirtualCaptureCard >>>> %s: Unable to copy property 'capacity'"
+ "<<<< AVVirtualCaptureCard >>>> %s: Unable to copy property 'freeSpace'"
+ "<<<< AVVirtualCaptureCard >>>> %s: Unable to set capacity to %@"
+ "<<<< AVVirtualCaptureCard >>>> %s: Unable to show system user interface"
+ "@\"AVAudioFormat\""
+ "@\"CMCaptureSpatialAudioMetadataSampleGenerator\""
+ "@\"NSMutableString\"16@?0@\"AVCaptureDeviceFormat\"8"
+ "@\"NSMutableString\"16@?0@\"AVCaptureInput\"8"
+ "@\"NSMutableString\"16@?0@\"AVCaptureInputPort\"8"
+ "@\"NSNumber\""
+ "@\"NSObject<OS_xpc_object>\""
+ "@\"NSPointerArray\""
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "@\"NSString\"16@?0@8"
+ "@252@0:8{?=qiIq}16^{__IOSurface=}40Q48@56^{__IOSurface=}64^{__IOSurface=}72@80@88^{__IOSurface=}96@104^{__IOSurface=}112@120^{__IOSurface=}128@136^{__IOSurface=}144@152^{__IOSurface=}160@168^{__IOSurface=}176@184^{__IOSurface=}192@200@208@216Q224Q232I240@244"
+ "@44@0:8i16Q20@28@36"
+ "@64@0:8@16@24@32@40B48@52I60"
+ "A local queue cannot be used in conjunction with a remote queue receiver"
+ "AVAuxiliaryMetadataAddValue"
+ "AVAuxiliaryMetadataArrayTagWithPrefixedKey"
+ "AVAuxiliaryMetadataStringTagWithPrefixedKey"
+ "AVCaptureCancelPrewarm"
+ "AVCaptureClientPreferencesDomain"
+ "AVCaptureDepthDataOutput cannot be used in conjunction with Cinematic Video capture."
+ "AVCaptureDepthDataOutput is not supported when its input's cinematicVideoCaptureEnabled is set to true."
+ "AVCaptureDeviceLensSmudgeDetectionStatusChangedKeyStatus"
+ "AVCaptureDeviceLensSmudgeDetectionStatusChangedNotification"
+ "AVCapturePrewarmWithOptions"
+ "AVCaptureSceneMonitoringStatusNotEnoughLight"
+ "AVCaptureSpatialAudioMetadataSampleGenerator"
+ "AVCaptureSpatialAudioMetadataSampleGenerator.m"
+ "AVCaptureStillImageOutputPlayShutterSound"
+ "AVCaptureSystemLensSelector_trace"
+ "AVCaptureTemporarilySuppressShutterSoundForAirpodStemClick_block_invoke_2"
+ "AVControlCenterBlackenFramesFromDeviceForBundleID"
+ "AVControlCenterIsManualFramingEnabledForDevice"
+ "AVControlCenterMicrophoneModuleShouldBeShownForBundleID"
+ "AVControlCenterPanWithTranslation"
+ "AVControlCenterStartPanningAtPoint"
+ "AVControlCenterVideoEffectsModuleShouldBeShownForBundleID"
+ "AVErrorInvalidSourceMedia"
+ "AVGQ4UHSO4KRGIJFZHZ3EAGDMAK6CA"
+ "AVGQ5RTE3RTRZZFRGK7IDFEQC7NFBE"
+ "AVGQ6HD7ZNZD33DG7SG4DOHIPW4SUQ"
+ "AVGQAJT7KNQJHRRDW5Q5QTGETOLK2E"
+ "AVGQBGWR3YSZWCQ7BKUUAOT5CCLHHE"
+ "AVGQCB54MH3XAXNGTVD2SAMOV5WWOQ"
+ "AVGQCaptureDeferredStartSupported"
+ "AVGQCaptureMultipleAudioDataOutputsSupported"
+ "AVGQCaptureSessionMultiCamCaptureAlwaysRequiresSupportedFormats"
+ "AVGQFrontFacingCameraSupportsCinematicVideo"
+ "AVGQFrontFacingCameraSupportsCinematicVideo4K"
+ "AVGQFrontFacingCameraSupportsPortraitAutoSuggest"
+ "AVGQHDDMQ6RTH76PQ2HVCQ4MSWG63Q"
+ "AVGQHSSMVIQNR3MAPIGELAQM7DWP4U"
+ "AVGQIDWZFGNLZOQVZINTCD5JZM57DE"
+ "AVGQKYDMKTE2UUKHJCGGZGQNYH5GDE"
+ "AVGQODGWLXGASKA4RNU2OP6Z44TGZ4"
+ "AVGQOKRXQZPHFZ4X2XCPOHTANZXNGM"
+ "AVGQQIBUFDUYMZTKVBF36FTLQON3DY"
+ "AVGQRearFacingCameraSupportsCinematicVideo"
+ "AVGQRearFacingCameraSupportsCinematicVideo4K"
+ "AVGQRearFacingCameraSupportsPortraitAutoSuggest"
+ "AVGQRearWideCameraDisplayCustomZoomStops"
+ "AVGQT42HZJM7T4BHFEGWILGWIJSNEQ"
+ "AVGQVYXTSFZ3R7TURIB5WPPITDPJLY"
+ "AVGQYPHR3FTUAZCCTEYFPSINLTE7DI"
+ "AWB needs to be locked for this configuration. Please set AVCaptureWhiteBalanceModeLocked on AVCaptureDevice."
+ "Alternates other than tmap are not supported"
+ "Audio format must be kAudioFormatLinearPCM"
+ "Aux data with invalid values not supported for DNG"
+ "CFBundleDisplayName"
+ "CameraLensSmudgeDetection"
+ "CameraScannerView"
+ "Can't call runDeferredStartWhenNeeded if automaticallyRunsDeferredStart is YES"
+ "Can't enable deferred start if deferredStartSupported is NO"
+ "Capturing HD120 with ProRes codec on this device is supported only on external storage device."
+ "Capturing HD60 with ProRes codec on this device is supported only on external storage device."
+ "Channel count and audio channel layout must agree"
+ "Cinematic Video focus can only be set when AVCaptureDeviceInput's isCinematicVideoCaptureEnabled is YES"
+ "Cisco-Systems.Spark"
+ "D16-D17"
+ "D27-D28"
+ "D37-D38"
+ "D421-D431"
+ "D47-D48"
+ "D52g-D53g"
+ "D63-D64"
+ "D73-D74"
+ "D93-D94"
+ "DICM"
+ "Image collections not supported"
+ "In order to capture HEIF/DICOM containerized photos, your delegate must respond to the selector captureOutput:didFinishProcessingPhoto:error:"
+ "Invalid argument - available values are kAudioChannelLayoutTag_Stereo or ( kAudioChannelLayoutTag_HOA_ACN_SN3D | 4 )"
+ "Invalid spatialAudioChannelLayoutTag property value %@, it must be kAudioChannelLayoutTag_Unknown with the input device's configured audio mode, session: %@"
+ "J317-J317x-J318-J318x-J320-J320x-J321-J321x"
+ "J517-J517x-J518-J518x-J522-J522x-J523-J523x"
+ "LastShownBuild:AVCaptureConnection.m:800"
+ "LastShownBuild:AVCaptureVideoPreviewLayer.m:1908"
+ "LastShownBuild:AVSpatialOverCaptureVideoPreviewLayer.m:294"
+ "LastShownDate:AVCaptureConnection.m:800"
+ "LastShownDate:AVCaptureVideoPreviewLayer.m:1908"
+ "LastShownDate:AVSpatialOverCaptureVideoPreviewLayer.m:294"
+ "Max"
+ "Metadata sample time is invalid"
+ "Min"
+ "No head bounds found"
+ "Not allowed to set automaticallyRunsDeferredStart to NO if not supported"
+ "Not supported - use -activeFormat.isCameraLensSmudgeDetectionSupported"
+ "Not supported - use -isExposurePointOfInterestSupported:"
+ "Not supported - use -isExposureRectOfInterestSupported"
+ "Not supported - use -isFocusRectOfInterestSupported"
+ "Not supported - use -isFocusRectOfInterestSupported:"
+ "Not supported - use activeFormat.isCinematicVideoCaptureSupported"
+ "Not supported - use isCinematicVideoCaptureSupported"
+ "Not supported by this device - use -[AVCaptureDeviceFormat isCameraLensSmudgeDetectionSupported]"
+ "One or more AVCaptureAudioDataOutputs contain duplicate values for the spatialAudioChannelLayoutTag property. One or the other must be either kAudioChannelLayoutTag_Stereo or ( kAudioChannelLayoutTag_HOA_ACN_SN3D | 4 ) but not both. Session: %@, outputs: %@"
+ "Processor version is not available"
+ "Rectangle must lay within the bounds of ( 0, 0, 1, 1 )"
+ "Rectangle size must be at least the size returned by minExposureRectOfInterestSize ( %lf, %lf )"
+ "Rectangle size must be at least the size returned by minFocusRectOfInterestSize ( %lf, %lf )"
+ "SensitiveContentMitigationActivated"
+ "Set PrimaryCaptureRect is taking more than %.0f seconds."
+ "T@\"<AVCaptureSessionDeferredStartDelegate>\",R,N"
+ "T@\"NSArray\",R,V_photoLibraryThumbnailDimensions"
+ "T@\"NSPointerArray\",R,V_videoPreviewLayers"
+ "TB,GisFixedFocus,V_fixedFocus"
+ "TB,N,GisCinematicVideoCaptureEnabled"
+ "TB,N,GisDeferredStartEnabled"
+ "TB,R,N,GisCameraLensSmudgeDetectionEnabled"
+ "TB,R,N,GisCinematicVideoCaptureSupported"
+ "TB,R,N,GisDeferredStartSupported"
+ "TB,R,N,GisManualDeferredStartSupported"
+ "TI,N"
+ "This device doesn't support external storage device."
+ "Too many audio outputs %@ configured for AVCaptureMultichannelAudioModeFirstOrderAmbisonics audio mode, session %@, the maximum is 2"
+ "Too many audio outputs %@ configured for session %@, the maximum is 1 when not in spatial audio mode"
+ "Tq,V_cinematicVideoFocusMode"
+ "Trying to enable cinematicVideo, however it is not supported by the format"
+ "Unable to create a vis configuration"
+ "Unable to create a vis processor"
+ "Unexpected image queue is nil, error (%d)."
+ "Unexpected spatial audio channel layout tag 0x%08x"
+ "Unsupported - use -isFaceOcclusionDetectionSupported"
+ "When Cinematic Video is enabled, AVCaptureMetadataOutput's metadataObjectTypes must match requiredMetadataObjectTypesForCinematicVideoCapture."
+ "When the device input's multichannelAudioMode is set to AVCaptureMultichannelAudioModeFirstOrderAmbisonics, the AVCaptureAudioDataOutput spatialAudioChannelLayoutTag property must be either kAudioChannelLayoutTag_Stereo or ( kAudioChannelLayoutTag_HOA_ACN_SN3D | 4 ) for session %@. Invalid AVAudioChannelLayoutTags: %@"
+ "["
+ "[***OverCapture***] "
+ "\\n"
+ "\\n%@"
+ "\\n(%@)"
+ "\\nDepth Format [%d]: %@"
+ "\\nVideo Format [%d]"
+ "_addAuxiliaryImage"
+ "_addObserversForConnectionDevice:"
+ "_cameraLensSmudgeDetectionEnabled"
+ "_cameraLensSmudgeDetectionInterval"
+ "_cameraLensSmudgeDetectionStatus"
+ "_checkEligibilityForEffect:"
+ "_cinematicVideoEnabled"
+ "_cinematicVideoFocusMode"
+ "_cinematicVideoSceneMonitoringStatuses"
+ "_createCompressionSessionWithModifications"
+ "_createDNGCompressorWithModifications"
+ "_defaultPhotoDimensionsWithHighResolutionCaptureEnabled:"
+ "_defaultRectForExposurePointOfInterest:"
+ "_defaultRectForFocusPointOfInterest:focusMode:"
+ "_delegateWrapperForSettingsID:"
+ "_didRunDeferredStart"
+ "_exposureRectOfInterest"
+ "_fixedFocus"
+ "_focusRectOfInterest"
+ "_geometricDistortionCorrectionEnabledByClient"
+ "_geometricDistortionCorrectionSupported"
+ "_getUniqueIDsForDevices"
+ "_indexOfAudioLevelChannel:"
+ "_isDefaultExposureRectOfInterest"
+ "_isDefaultFocusRectOfInterest"
+ "_isDeviceInputInSpatialAudioMode:"
+ "_lastCamerasMountedInLandscapeOrientation"
+ "_minExposureRectOfInterestSize"
+ "_minExposureRectOfInterestSizeForFormat:"
+ "_minFocusRectOfInterestSize"
+ "_minFocusRectOfInterestSizeForFormat:"
+ "_photoLibraryThumbnailDimensions"
+ "_preferredIOBufferDuration"
+ "_primaryCaptureRectTrueVideoTransitionPercentComplete"
+ "_recommendedAudioOutputSettingsForConnection:sourceSettings:fileType:spatialAudioChannelLayoutTag:"
+ "_recommendedFrameRateRangeForPhotoMode"
+ "_refreshRegisteredDevices"
+ "_registerServerConnectionDiedNotification_block_invoke"
+ "_removeMetadataObjectTypeFromMetadataObjectTypes:"
+ "_removeMetadataObjectTypesFromMetadataObjectTypes:"
+ "_removeObserversForConnectionDevice:"
+ "_requireMultiCamSupportedFormatsForVideoDevices"
+ "_resetCinematicVideoCaptureSupported"
+ "_setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:"
+ "_setSimulatedAperture:"
+ "_spatialAudioMetadataSampleGenerator"
+ "_updateCinematicVideoCaptureSceneMonitoringStatus:"
+ "_updatePrimaryCaptureRectWithCamerasMountedInLandscapeOrientation:center:aspectRatio:"
+ "_validateAudioConfiguration:"
+ "_validateCinematicVideoConfiguration:"
+ "_videoPreviewLayersContains:"
+ "_willRunDeferredStart"
+ "addPointer:"
+ "analyzeAudioSample:"
+ "aspectRatioForNonDestructiveCrop"
+ "audio"
+ "automaticallyRunsDeferredStart"
+ "avExternalStorageDeviceNotification"
+ "avcaptureFigCaptureSessionNotification"
+ "avcaptureVideoStabilizationModeToFigCaptureVideoStabilizationMethod"
+ "avcaptureaudiodataoutput_trace"
+ "avcapturecameracalibrationdataoutput_trace"
+ "avcapturecontrolsoverlay_trace"
+ "avcapturecoreanalyticsreporter_trace"
+ "avcapturedataoutputdelegatecallbackhelper_trace"
+ "avcapturedataoutputsynchronizer_trace"
+ "avcapturedepthdataoutput_trace"
+ "avcapturedeviceformat_trace"
+ "avcapturedeviceinput_trace"
+ "avcapturefileoutput_trace"
+ "avcaptureindexpicker_trace"
+ "avcaptureinput_trace"
+ "avcaptureoutput_trace"
+ "avcapturephoto_trace"
+ "avcapturepointclouddataoutput_trace"
+ "avcaptureslider_trace"
+ "avcapturespatialaudiometadatasamplegenerator"
+ "avcapturestillimageoutput_trace"
+ "avcapturesystemstylepicker_trace"
+ "avcapturesystemstyleslider_trace"
+ "avcapturesystemzoomslider_trace"
+ "avcapturetoggle_trace"
+ "avcapturevideodataoutput_trace"
+ "avcapturevideothumbnailoutput_trace"
+ "avcapturevisiondataoutput_trace"
+ "avcdpp_dispatchNotification_block_invoke"
+ "avcmcs_adjustPowerNumbersForTemperatureAndPMU"
+ "avcmcs_computeSystemPressureCost"
+ "avcmcs_constituentDeviceFormatFromVirtualDeviceFormat"
+ "avcp_copyCGImageForCompressedData"
+ "avcp_copyCGImageForUncompressedBuffer"
+ "avcp_copyDNGFileDataRepresentationForSushiRawBuffer"
+ "avcp_copyFirstAuxiliaryImageOfType"
+ "avcp_copyJPEGThumbnailForPixelBuffer"
+ "avcp_copyTIFFFileDataRepresentationForImage"
+ "avdepthdata_trace"
+ "avflashlightNotification"
+ "avgestalt_buildDataBase_block_invoke"
+ "avgestalt_trace"
+ "avofflinevideostabilizer_trace"
+ "avpds_proprietaryDefaultsSourceNotificationHandler_block_invoke"
+ "avpointclouddata_trace"
+ "avportraiteffectsmatte_trace"
+ "avsemanticsegmentationmatte_trace"
+ "avvirtualcapturecard_trace"
+ "black"
+ "cameraLensSmudgeDetectionEnabled"
+ "cameraLensSmudgeDetectionInterval"
+ "cameraLensSmudgeDetectionStatus"
+ "channelCount"
+ "channelLayout"
+ "cinematicAudioSettings"
+ "cinematicVideoCaptureEnabled"
+ "cinematicVideoCaptureSceneMonitoringStatuses"
+ "cinematicVideoCaptureSupported"
+ "cinematicVideoEnabled"
+ "cinematicVideoFocusMode"
+ "cinematicVideoSupported"
+ "com.apple.Magnifier"
+ "com.apple.SpeechRecognitionCore.speechrecognitiond"
+ "com.apple.avfoundation.capture.photooutput.sound-suppression-timer"
+ "com.apple.coremedia"
+ "com.apple.developer.avfoundation.video-data-output-prepares-cellular-radio-for-machine-readable-code-scanning"
+ "com.apple.private.avfoundation.audio-format-override"
+ "compact"
+ "configuresApplicationAudioSessionForBluetoothHighQualityRecording"
+ "defaultRectForExposurePointOfInterest:"
+ "defaultRectForFocusPointOfInterest:"
+ "deferredStartDelegate"
+ "deferredStartDelegateCallbackQueue"
+ "deferredStartDelegateStorage"
+ "deferredStartEnabled"
+ "deferredStartSupported"
+ "depth data"
+ "description=CameraCapture_AVF-650.0.0.122.4"
+ "deviceFormatForSessionPreset:device:"
+ "digraph %@ {\n"
+ "disconnected"
+ "exposureRectOfInterest"
+ "faceTrackingSuspended"
+ "fad_figCaptureSourceNotificationHandler_block_invoke"
+ "fiel/com.apple.quicktime.detected-cat-head.bounds"
+ "fiel/com.apple.quicktime.detected-cat-head.object-id"
+ "fiel/com.apple.quicktime.detected-dog-head.bounds"
+ "fiel/com.apple.quicktime.detected-dog-head.object-id"
+ "figCaptureSourceAttributes"
+ "figMetadataPropertyFromMetadataItems:"
+ "fileSystemRepresentation"
+ "filterRenderingEnabled must be set to YES before setting videoPreviewFilters with a non-empty array"
+ "filterWithName:"
+ "fixedFocus"
+ "focusMode cannot be locked when capturing Cinematic Video."
+ "focusRectOfInterest"
+ "getPrimaryCaptureRectWithCamerasMountedInLandscapeOrientation:center:aspectRatio:uniqueID:"
+ "green"
+ "i24@0:8^{opaqueCMSampleBuffer=}16"
+ "initWithDeferredPhotoIdentifier:applicationIdentifier:photoLibraryThumbnailDimensions:"
+ "initWithFigLevel:factors:recommendedFrameRateRangeForPortrait:recommendedFrameRateRangeForPhotoMode:"
+ "initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:photoLibraryThumbnails:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:"
+ "isCameraLensSmudgeDetectionEnabled"
+ "isCameraLensSmudgeDetectionSupported"
+ "isCinematicVideoCaptureEnabled"
+ "isCinematicVideoCaptureSupported"
+ "isCinematicVideoSupported"
+ "isDICOMSupported"
+ "isDeferredStartEnabled"
+ "isDeferredStartSupported"
+ "isExposureRectOfInterestSupported"
+ "isFaceTrackingSuspended"
+ "isFixedFocus"
+ "isFocusRectOfInterestSupported"
+ "isLensSmudgeDetectionSupported"
+ "isManualDeferredStartSupported"
+ "isStreamingDepthOnlyPrivatelySupported"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "kCMPhotoError_InternalFailure"
+ "kCMPhotoError_UnsupportedOperation"
+ "kFigExternalStorageDeviceManagerError_DeviceNotSupported"
+ "legacyLog"
+ "manualDeferredStartSupported"
+ "metadata items"
+ "metadata objects"
+ "minExposureRectOfInterestSize"
+ "minFocusRectOfInterestSize"
+ "multichannelAudioMode must be set to None to override the AURemoteIO output format, session: %@"
+ "newTimedMetadataSampleBufferAndResetAnalyzer"
+ "nil bundleID"
+ "nil device"
+ "no; self-healing the connection"
+ "nominalFocalLengthIn35mmFilm"
+ "nonretainedObjectValue"
+ "now"
+ "opaqueSessionID"
+ "outputRotationDegrees"
+ "photoLibraryThumbnailDimensions"
+ "photoLibraryThumbnails"
+ "po_createPreviewJPEGRepresentationForSampleBuffer"
+ "pointerAtIndex:"
+ "preferredIOBufferDuration"
+ "preparesCellularRadioForNetworkConnection"
+ "preparesCellularRadioForNetworkConnectionSetByClient"
+ "preservesDynamicHDRMetadata"
+ "previewHeight"
+ "previewWidth"
+ "rawThumbnailHeight"
+ "rawThumbnailWidth"
+ "recommendedFrameRateRangeForPhotoMode"
+ "recommendedMediaTimeScaleForAssetWriter"
+ "recommendedOutputSettingsForConnection:sourceSettings:videoCodecType:fileType:isIris:outputFileURL:spatialAudioChannelLayoutTag:"
+ "red"
+ "remoteIOOutputFormat"
+ "removePointerAtIndex:"
+ "requiredMetadataObjectTypesForCinematicVideoCapture"
+ "resetAnalyzer"
+ "runDeferredStartWhenNeeded"
+ "sShutterSoundSuppressedByAirpodStemClickQueue != nil"
+ "sensitiveContentAnalyzerEnabled"
+ "sensitiveContentAnalyzerXPCObject"
+ "sessionDidRunDeferredStart:"
+ "sessionWillRunDeferredStart:"
+ "setAspectRatioForNonDestructiveCrop:"
+ "setAutomaticallyRunsDeferredStart:"
+ "setCameraLensSmudgeDetectionEnabled:detectionInterval:"
+ "setCinematicVideoCaptureEnabled:"
+ "setCinematicVideoFixedFocusAtPoint:focusMode:"
+ "setCinematicVideoFocusMode:"
+ "setCinematicVideoTrackingFocusAtPoint:focusMode:"
+ "setCinematicVideoTrackingFocusWithDetectedObjectID:focusMode:"
+ "setConfiguresAppAudioSessionForBluetoothHighQualityRecording:"
+ "setConfiguresApplicationAudioSessionForBluetoothHighQualityRecording:"
+ "setDateFormat:"
+ "setDeferredStartDelegate:deferredStartDelegateCallbackQueue:"
+ "setDeferredStartEnabled:"
+ "setExposureRectOfInterest:"
+ "setFaceTrackingSuspended:"
+ "setFixedFocus:"
+ "setFocusRectOfInterest:"
+ "setLensSmudgeDetectionEnabled:"
+ "setLensSmudgeDetectionInterval:"
+ "setOutputRotationDegrees:"
+ "setPreferredIOBufferDuration:"
+ "setPreparesCellularRadioForNetworkConnection:"
+ "setPreservesDynamicHDRMetadata:"
+ "setPreviewRotationDegrees:"
+ "setRemoteIOOutputFormat:"
+ "setRotationDegrees:"
+ "setSensitiveContentAnalyzerEnabled:"
+ "setSensitiveContentAnalyzerXPCObject:"
+ "setSpatialAudioChannelLayoutTag:"
+ "setVideoRotationDegrees:"
+ "simulatedAperture can only be set before a Cinematic Video capture starts"
+ "socvpl_figCaptureSessionNotification"
+ "source settings must be nil when getting recommended settings for spatial audio"
+ "spatialAudioChannelLayoutTag"
+ "spatialAudioChannelLayoutTagForChannelLevels"
+ "streamDescription"
+ "stringFromDate:"
+ "temporarilySuppressShutterSoundForAirpodStemClick"
+ "thumbnailHeight"
+ "thumbnailWidth"
+ "timeIntervalSinceDate:"
+ "timedMetadataSampleBufferFormatDescription"
+ "v16@?0@\"<AVCaptureSessionDeferredStartDelegate>\"8"
+ "v32@0:8q16q24"
+ "v36@0:8B16^{CGPoint=dd}20^d28"
+ "v40@0:8{CGPoint=dd}16q32"
+ "v44@0:8B16^{CGPoint=dd}20^d28^q36"
+ "v44@0:8B16{?=qiIq}20"
+ "video"
+ "video data"
+ "videoFrameRateRangeForCinematicVideo"
+ "videoMaxZoomFactorForCinematicVideo"
+ "videoMinZoomFactorForCinematicVideo"
+ "vision data"
+ "vpio_translatedBundleIDForBundleID"
+ "vpl_figCaptureSessionNotification"
+ "vpl_transformForPlacement"
+ "vto_notificationHandler"
+ "weakObjectsPointerArray"
+ "writeToFile:atomically:encoding:error:"
+ "yyyy-MM-dd    HH:mm:ss.SSS"
+ "yyyy-MM-dd hh:mm:ss.SSS"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8{CGPoint=dd}16"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}40@0:8{CGPoint=dd}16q32"
+ "}\n"
- "%@ Recommended:%.0f-%.0f"
- "-[AVCapturePhotoOutput _handleWillCaptureStillImageNotificationWithPayload:forRequest:]"
- "1OO"
- "<%@: %p, time=%lld, cachedResult=%@"
- "<<<< AVCaptureFigVideoDevice >>>> %s: %@"
- "<<<< AVCaptureFigVideoDevice >>>> %s: (%@) video zoom factor changed from %f to %f"
- "<<<< AVCaptureFigVideoDevice >>>> %s: Error setting centerStageFramingMode to %ld (%d)"
- "<<<< AVCaptureFigVideoDevice >>>> %s: MaxFrameDuration to set %lld / %d"
- "<<<< AVCaptureFigVideoDevice >>>> %s: MinFrameDuration to set %lld / %d"
- "<<<< AVCaptureFigVideoDevice >>>> %s: Supported frame duration range for %@ (%lld / %d - %lld / %d)"
- "<<<< AVCaptureFigVideoDevice >>>> %s: Supported frame duration range for Background Blur (%lld / %d - %lld / %d)"
- "<<<< AVCaptureFigVideoDevice >>>> %s: Supported frame duration range for Background Replacement (%lld / %d - %lld / %d)"
- "<<<< AVCaptureFigVideoDevice >>>> %s: Supported frame duration range for Studio Lighting (%lld / %d - %lld / %d)"
- "<<<< AVCaptureFigVideoDevice >>>> %s: Value for activeMaxFrameRate set to %lf"
- "<<<< AVCaptureFigVideoDevice >>>> %s: Value for activeMinFrameRate set to %lf"
- "<<<< AVCaptureFigVideoDevice >>>> %s: format:%{public}@ preset:%{public}@"
- "<<<< AVCapturePhotoOutput >>>> %s: (%p) suppressing shutter sound"
- "<<<< AVCaptureSession >>>> %s: Cancel requested to happen %.1f seconds from now"
- "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@: imageQueueSlot: %u, imageQueue: %@, rotationDegrees: %.0f, size: %@"
- "<<<< AVCaptureVideoPreviewLayer >>>> %s: preview started - contents = %@, imageQueueSlot = %d"
- "@\"NSHashTable\""
- "@244@0:8{?=qiIq}16^{__IOSurface=}40Q48@56^{__IOSurface=}64^{__IOSurface=}72@80^{__IOSurface=}88@96^{__IOSurface=}104@112^{__IOSurface=}120@128^{__IOSurface=}136@144^{__IOSurface=}152@160^{__IOSurface=}168@176^{__IOSurface=}184@192@200@208Q216Q224I232@236"
- "@36@0:8i16Q20@28"
- "@44@0:8^{opaqueCMSampleBuffer=}16@24^@32B40"
- "@60@0:8@16@24@32@40B48@52"
- "A local queue cannot be used in conjunction with a remote queue reciever"
- "AVCaptureReactionEffectStatus"
- "AVMetadataVisualIntelligenceObject"
- "Capturing 1080p120 with ProRes codec on this device is supported only on external storage device."
- "Capturing 1080p60 with ProRes codec on this device is supported only on external storage device."
- "D321"
- "D331"
- "D331-D331p"
- "D331p"
- "In order to capture HEIF containerized photos, your delegate must respond to the selector captureOutput:didFinishProcessingPhoto:error:"
- "J171-J172"
- "J317-J318-J320-J321-J317x-J318x-J320x-J321x"
- "J517-J518-J522-J523-J517x-J518x-J522x-J523x"
- "N84-N841"
- "N841"
- "ReactionVictory"
- "Setting max frame rate failed"
- "Setting min frame rate failed"
- "T@\"NSDictionary\",R,V_visualIntelligence"
- "T@\"NSHashTable\",R,V_videoPreviewLayers"
- "Unsupported - use -isVisualIntelligenceMetadataSupported"
- "_appClipCodesCollectionForSampleBuffer:input:"
- "_barcodeCollectionForSampleBuffer:input:"
- "_checkEligiblityForEffect:"
- "_detectedObjectsCollectionForSampleBuffer:input:facesArrayOut:need180DegreeMetadataTransform:"
- "_eyeReliefResultCollectionForSampleBuffer:input:"
- "_faceIDReadinessCollectionForSampleBuffer:input:"
- "_figMetadataPropertyFromMetadataItems:"
- "_h264EncoderLimitations"
- "_hevcEncoderSettings"
- "_legacyFaceCollectionForSampleBuffer:input:"
- "_lumaHistogramDataCollectionForSampleBuffer:input:"
- "_motionToWakeCollectionForSampleBuffer:input:"
- "_offlineVISMotionCollectionForSampleBuffer:input:"
- "_primaryCaptureRectTransitionPercentComplete"
- "_recommendedAudioOutputSettingsForConnection:sourceSettings:fileType:"
- "_sceneClassificationCollectionForSampleBuffer:input:"
- "_sessionPresetCompressionSettings"
- "_setPrimaryCaptureRectAspectRatio:centerPoint:transitionPercentComplete:"
- "_supportedOptionalFaceDetectionFeatures"
- "_supportedOptionalFaceDetectionFeaturesDictionary"
- "_textRegionsCollectionForSampleBuffer:input:"
- "_trackedFacesCollectionForSampleBuffer:input:"
- "_visualIntelligence"
- "_visualIntelligenceCollectionForSampleBuffer:input:"
- "areControlsSupported"
- "chanIdx >= 0 && chanIdx < _internal->audioChannels.count"
- "clientUsesVideoRotationAngleAPI"
- "description=CameraCapture_AVF-587.122.6.0.2"
- "highResolutionStillImageOutputEnabledChangeCausesCaptureSessionRestart"
- "iOS 12.0"
- "iOS 13.1"
- "initVisualIntelligenceObjectWithVisualIntelligenceDictionary:time:sourceCaptureInput:"
- "initWithFigLevel:factors:recommendedFrameRateRangeForPortrait:"
- "initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:"
- "isQuadraHighResStillImageSupported"
- "isVisualIntelligenceMetadataObjectTypeAvailable"
- "isVisualIntelligenceMetadataSupported"
- "mdta/com.apple.quicktime.visual-intelligence"
- "minusHashTable:"
- "nonDestructiveCropAspectRatio"
- "objectDetectionCachedResult"
- "objectDetectionUprightExifOrientation"
- "outputOrientation"
- "performReactionEffect:"
- "reactionEffectsActive"
- "reactionEffectsAvailable"
- "recommendedOutputSettingsForConnection:sourceSettings:videoCodecType:fileType:isIris:outputFileURL:"
- "setNonDestructiveCropAspectRatio:"
- "setOutputOrientation:"
- "setPreviewOrientation:"
- "setQuadraHighResCaptureEnabled:"
- "setVisualIntelligenceMetadataObjectTypeAvailable:"
- "valueFormat"
- "visualIntelligence"
- "visualIntelligenceObjectTypeAvailable"
- "visualIntelligenceObjectWithVisualIntelligenceDictionary:input:time:"
- "weakObjectsHashTable"

```
