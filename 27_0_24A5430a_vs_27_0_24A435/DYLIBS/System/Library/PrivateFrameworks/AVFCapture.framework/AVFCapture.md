## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

 764.22.13.0.0
-  __TEXT.__text: 0x12e15c
-  __TEXT.__objc_methlist: 0x1002c
-  __TEXT.__const: 0xec2
-  __TEXT.__gcc_except_tab: 0x2b6c
-  __TEXT.__cstring: 0x2bd79
-  __TEXT.__oslogstring: 0x9806
+  __TEXT.__text: 0x1454a8
+  __TEXT.__objc_methlist: 0x113cc
+  __TEXT.__const: 0xf02
+  __TEXT.__gcc_except_tab: 0x314c
+  __TEXT.__cstring: 0x2f009
+  __TEXT.__oslogstring: 0xa75e
   __TEXT.__dlopen_cstrs: 0x274
   __TEXT.__ustring: 0x54
   __TEXT.__swift5_typeref: 0xef

   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x5208
+  __TEXT.__unwind_info: 0x5768
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8938
-  __DATA_CONST.__objc_classlist: 0x638
+  __DATA_CONST.__const: 0x9458
+  __DATA_CONST.__objc_classlist: 0x6c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8828
+  __DATA_CONST.__objc_selrefs: 0x91d8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x568
-  __DATA_CONST.__objc_arraydata: 0x458
-  __DATA_CONST.__got: 0x2b50
-  __AUTH_CONST.__const: 0xdf0
-  __AUTH_CONST.__cfstring: 0x15540
-  __AUTH_CONST.__objc_const: 0x1a690
-  __AUTH_CONST.__objc_intobj: 0xa80
+  __DATA_CONST.__objc_superrefs: 0x5f0
+  __DATA_CONST.__objc_arraydata: 0x4a8
+  __DATA_CONST.__got: 0x2fa0
+  __AUTH_CONST.__const: 0xe10
+  __AUTH_CONST.__cfstring: 0x16be0
+  __AUTH_CONST.__objc_const: 0x1cac8
+  __AUTH_CONST.__objc_intobj: 0xb70
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x330
-  __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1108
-  __AUTH.__objc_data: 0x2370
+  __AUTH_CONST.__objc_arrayobj: 0x3a8
+  __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__auth_got: 0x1170
+  __AUTH.__objc_data: 0x2910
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x1c78
-  __DATA.__data: 0xdc0
+  __DATA.__objc_ivar: 0x1ec8
+  __DATA.__data: 0xe48
   __DATA.__common: 0x1c0
   __DATA_DIRTY.__objc_data: 0x1ae0
   __DATA_DIRTY.__data: 0x178

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7331
-  Symbols:   16990
-  CStrings:  3869
+  Functions: 7817
+  Symbols:   18208
+  CStrings:  4187
 
Symbols:
+ +[AVCaptureDevice exposureSignalsBitmaskForSet:]
+ +[AVCaptureDevice exposureSignalsSetForBitmask:includingInternal:]
+ +[AVCaptureDevice publicExposureSignalsSet]
+ +[AVCaptureDevice(SecureSigning_Private) isSecureSigningCertificateAvailable]
+ +[AVCaptureDeviceStateDescriptor descriptorForDevice:]
+ +[AVCaptureDeviceStateDescriptor mediaTypesForDevice:]
+ +[AVCaptureMovieFileOutput _makeTimelapseMovieFromTimewarpTimelapseClassicIntermediateMovie:timelapseMovie:timelapseDestinationFrameRate:error:]
+ +[AVCaptureMovieFileOutput makeTimelapseMovieFromTimewarpTimelapseClassicIntermediateMovie:timelapseMovie:error:]
+ +[AVCapturePersonalPhotographerDuplicateInfo supportsSecureCoding]
+ +[AVCapturePersonalPhotographerMetadata supportsSecureCoding]
+ +[AVCapturePersonalPhotographerSessionFinishCoordinator initialize]
+ +[AVCapturePersonalPhotographerSessionResults initialize]
+ +[AVCapturePhotographicStyle styleWithSmartStyle:textureStyle:]
+ +[AVCaptureResolvedPhotoSettings resolvedSettingsWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:]
+ +[AVCaptureSecureVideoDataOutput initialize]
+ +[AVCaptureSecureVideoDataOutput new]
+ +[AVCaptureTextureStyle identityStyle]
+ +[AVCaptureTextureStyle styleWithPreset:intensity:]
+ +[AVCaptureTextureStyle styleWithPreset:intensity:grain:]
+ +[AVMetadataCinematicVideoMetadataObject cinematicVideoMetadataFormatDescription]
+ +[AVMetadataCinematicVideoMetadataObject cinematicVideoMetadataObjectWithPayload:input:time:]
+ +[AVMetadataFaceIDObject faceIDObjectWithFaceIDResultDictionary:metadataDictionary:input:time:]
+ +[AVMetadataFocusTrackedObject focusTrackedObjectWithObjectID:mask:bounds:input:time:]
+ -[AVCaptureAncillaryDataEncoder .cxx_destruct]
+ -[AVCaptureAncillaryDataEncoder canSetDataForTag:]
+ -[AVCaptureAncillaryDataEncoder canSetStringForTag:]
+ -[AVCaptureAncillaryDataEncoder currentUserDefinedAncillaryData]
+ -[AVCaptureAncillaryDataEncoder initWithCaptureOutput:]
+ -[AVCaptureAncillaryDataEncoder isEnabled]
+ -[AVCaptureAncillaryDataEncoder removeRDD18AncillaryDataForTag:]
+ -[AVCaptureAncillaryDataEncoder sendUserDataEntryToCCD:value:]
+ -[AVCaptureAncillaryDataEncoder setEnabled:]
+ -[AVCaptureAncillaryDataEncoder setRDD18AncillaryData:forTag:error:]
+ -[AVCaptureAncillaryDataEncoder setRDD18AncillaryDataString:forTag:error:]
+ -[AVCaptureAncillaryDataEncoder setUserInstanceUID:forUserUDAMVersion:]
+ -[AVCaptureAncillaryDataEncoder sizeForTag:]
+ -[AVCaptureAncillaryDataEncoder userDefinedAncillaryDataSizeRemaining]
+ -[AVCaptureBroadcastVideoOutput ancillaryDataEncoder]
+ -[AVCaptureBroadcastVideoOutput sendAncillaryUserDataToCCD:]
+ -[AVCaptureConnection _setLowLightVideoNoiseReductionEnabled:]
+ -[AVCaptureConnection _updateLowLightVideoNoiseReductionSupported]
+ -[AVCaptureConnection automaticallyEnablesLowLightVideoNoiseReduction]
+ -[AVCaptureConnection isLowLightVideoNoiseReductionEnabled]
+ -[AVCaptureConnection isLowLightVideoNoiseReductionSupported]
+ -[AVCaptureConnection setAutomaticallyEnablesLowLightVideoNoiseReduction:]
+ -[AVCaptureConnection setLowLightVideoNoiseReductionEnabled:]
+ -[AVCaptureDeferredPhotoProxy initWithTimestamp:proxySurface:proxySurfaceSize:proxyFileType:previewPhotoSurface:secureSignedRawSurface:secureSignedRawSurfaceSize:metadata:captureRequest:sequenceCount:photoCount:applicationIdentifier:captureRequestIdentifier:photoIdentifier:expectedPhotoProcessingFlags:underlyingSourceDeviceType:sourceDeviceType:]
+ -[AVCaptureDevice _exposesOmahaConstituentDevices]
+ -[AVCaptureDevice activeExposureSignals]
+ -[AVCaptureDevice autoExposureLensApertureRateLimit]
+ -[AVCaptureDevice automaticallyAdjustsExposureDuration]
+ -[AVCaptureDevice automaticallyAdjustsISO]
+ -[AVCaptureDevice automaticallyAdjustsLensAperture]
+ -[AVCaptureDevice automaticallyEnablesExposureSignals]
+ -[AVCaptureDevice continuousAutoFocusTrackingLensPositionBias]
+ -[AVCaptureDevice enabledExposureSignals]
+ -[AVCaptureDevice faceIDCoexistenceSupported]
+ -[AVCaptureDevice faceIDUnwrapResult]
+ -[AVCaptureDevice faceIDUnwrapSupported]
+ -[AVCaptureDevice isContinuousAutoFocusTrackingEnabled]
+ -[AVCaptureDevice isContinuousAutoFocusTrackingSubjectAcquired]
+ -[AVCaptureDevice isFaceIDCoexistenceEnabled]
+ -[AVCaptureDevice isLowCurrentTorchEnabled]
+ -[AVCaptureDevice isLowCurrentTorchSupported]
+ -[AVCaptureDevice isLowLightVideoNoiseReductionEnabled]
+ -[AVCaptureDevice isOmahaVariant]
+ -[AVCaptureDevice isPrimaryConstituentDeviceSwitchingBehaviorLockedWithDeviceSupported]
+ -[AVCaptureDevice releaseFaceIDFrameProxyWithIdentifier:]
+ -[AVCaptureDevice secureSigningPhotoCaptureEnabled]
+ -[AVCaptureDevice setAutoExposureLensApertureRateLimit:]
+ -[AVCaptureDevice setAutomaticallyEnablesExposureSignals:]
+ -[AVCaptureDevice setContinuousAutoFocusTrackingEnabled:]
+ -[AVCaptureDevice setEnabledExposureSignals:]
+ -[AVCaptureDevice setExposureModeCustomWithLensAperture:duration:ISO:completionHandler:]
+ -[AVCaptureDevice setFaceIDCoexistenceEnabled:]
+ -[AVCaptureDevice setLowCurrentTorchEnabled:]
+ -[AVCaptureDevice setLowLightVideoNoiseReductionEnabled:]
+ -[AVCaptureDevice setPrimaryConstituentDeviceSwitchingBehaviorLockedWithDevice:]
+ -[AVCaptureDevice setSecureSigningPhotoCaptureEnabled:]
+ -[AVCaptureDevice setcontinuousAutoFocusTrackingLensPositionBias:]
+ -[AVCaptureDevice startFaceIDUnwrap]
+ -[AVCaptureDevice supportedExposureSignals]
+ -[AVCaptureDevice(ActiveOmahaConstituentDeviceType) activeOmahaConstituentDeviceType]
+ -[AVCaptureDevice(DeviceAngle) deviceAngle]
+ -[AVCaptureDevice(PrimaryDisplayRegion) _queryPrimaryDisplayRegion]
+ -[AVCaptureDevice(PrimaryDisplayRegion) primaryDisplayRegion]
+ -[AVCaptureDeviceFormat _checkCustomExposureModeWithLensAperture:duration:ISO:entryPoint:]
+ -[AVCaptureDeviceFormat defaultLensAperture]
+ -[AVCaptureDeviceFormat isCinematicVideoMetadataCaptureSupported]
+ -[AVCaptureDeviceFormat isContinuousAutoFocusTrackingSupported]
+ -[AVCaptureDeviceFormat isFaceIDCoexistenceSupported]
+ -[AVCaptureDeviceFormat isLowLightVideoNoiseReductionSupported]
+ -[AVCaptureDeviceFormat isPersonalPhotographerSupported]
+ -[AVCaptureDeviceFormat isSecureSigningPhotoCaptureSupported]
+ -[AVCaptureDeviceFormat isTextureStyleSupported]
+ -[AVCaptureDeviceFormat maxLensAperture]
+ -[AVCaptureDeviceFormat minLensAperture]
+ -[AVCaptureDeviceFormat recommendedLensApertureStops]
+ -[AVCaptureDeviceFormat supportsExposureModeCustomWithLensAperture:duration:ISO:]
+ -[AVCaptureDeviceRotationCoordinator _handleDeviceAngleDidChangeNotification:]
+ -[AVCaptureDeviceRotationCoordinator _shouldInvertBackCameraRotationForDeviceAngle]
+ -[AVCaptureDeviceRotationCoordinator _systemReferenceAngleForDeviceOrientation:onDisplayRegion:]
+ -[AVCaptureDeviceStateCoordinatorUtilities dealloc]
+ -[AVCaptureDeviceStateCoordinatorUtilities initWithTypes:]
+ -[AVCaptureDeviceStateCoordinatorUtilities stateAForPosition:deviceAngle:]
+ -[AVCaptureDeviceStateCoordinatorUtilities stateBForPosition:deviceAngle:]
+ -[AVCaptureDeviceStateDescriptor _initWithDeviceType:mediaTypes:position:uniqueID:localizedName:]
+ -[AVCaptureDeviceStateDescriptor dealloc]
+ -[AVCaptureDeviceStateDescriptor debugDescription]
+ -[AVCaptureDeviceStateDescriptor description]
+ -[AVCaptureDeviceStateDescriptor deviceType]
+ -[AVCaptureDeviceStateDescriptor hash]
+ -[AVCaptureDeviceStateDescriptor isEqual:]
+ -[AVCaptureDeviceStateDescriptor localizedName]
+ -[AVCaptureDeviceStateDescriptor mediaTypes]
+ -[AVCaptureDeviceStateDescriptor position]
+ -[AVCaptureDeviceStateDescriptor uniqueID]
+ -[AVCaptureFaceIDBracketConfiguration colorBracketEncryptionConfiguration]
+ -[AVCaptureFaceIDBracketConfiguration copyWithZone:]
+ -[AVCaptureFaceIDBracketConfiguration dealloc]
+ -[AVCaptureFaceIDBracketConfiguration doubleOrder]
+ -[AVCaptureFaceIDBracketConfiguration faceIDBracketConfigurationDictionary]
+ -[AVCaptureFaceIDBracketConfiguration infraredBracketEncryptionConfiguration]
+ -[AVCaptureFaceIDBracketConfiguration init]
+ -[AVCaptureFaceIDBracketConfiguration isEqual:]
+ -[AVCaptureFaceIDBracketConfiguration numberOfDoubles]
+ -[AVCaptureFaceIDBracketConfiguration probePatternIndex]
+ -[AVCaptureFaceIDBracketConfiguration probePatternType]
+ -[AVCaptureFaceIDBracketConfiguration setColorBracketEncryptionConfiguration:]
+ -[AVCaptureFaceIDBracketConfiguration setDoubleOrder:]
+ -[AVCaptureFaceIDBracketConfiguration setInfraredBracketEncryptionConfiguration:]
+ -[AVCaptureFaceIDBracketConfiguration setNumberOfDoubles:]
+ -[AVCaptureFaceIDBracketConfiguration setProbePatternIndex:]
+ -[AVCaptureFaceIDBracketConfiguration setProbePatternType:]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration copyWithZone:]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration dealloc]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration faceIDBracketEncryptionConfigurationDictionary]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration hostMainKeyIndex]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration initializationVector]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration isEqual:]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration linearFeedbackShiftRegisterSeed]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration nonce]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration setHostMainKeyIndex:]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration setInitializationVector:]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration setLinearFeedbackShiftRegisterSeed:]
+ -[AVCaptureFaceIDBracketEncryptionConfiguration setNonce:]
+ -[AVCaptureFaceIDConfiguration copyWithZone:]
+ -[AVCaptureFaceIDConfiguration faceIDConfigurationDictionary]
+ -[AVCaptureFaceIDConfiguration isAttentionRequired]
+ -[AVCaptureFaceIDConfiguration isEqual:]
+ -[AVCaptureFaceIDConfiguration isFrameLogEnabled]
+ -[AVCaptureFaceIDConfiguration isFrameMetadataEnabled]
+ -[AVCaptureFaceIDConfiguration isPeriocularEnabled]
+ -[AVCaptureFaceIDConfiguration mode]
+ -[AVCaptureFaceIDConfiguration retryType]
+ -[AVCaptureFaceIDConfiguration setAttentionRequired:]
+ -[AVCaptureFaceIDConfiguration setFrameLogEnabled:]
+ -[AVCaptureFaceIDConfiguration setFrameMetadataEnabled:]
+ -[AVCaptureFaceIDConfiguration setMode:]
+ -[AVCaptureFaceIDConfiguration setPeriocularEnabled:]
+ -[AVCaptureFaceIDConfiguration setRetryType:]
+ -[AVCaptureFaceIDUnwrapResult cameraStreamError]
+ -[AVCaptureFaceIDUnwrapResult initWithUnwrapStatus:pearlSecureSessionError:streamError:]
+ -[AVCaptureFaceIDUnwrapResult isEqual:]
+ -[AVCaptureFaceIDUnwrapResult pearlSecureSessionUnwrapError]
+ -[AVCaptureFaceIDUnwrapResult unwrapStatus]
+ -[AVCaptureFigVideoDevice _customExposureIsFullyLocked]
+ -[AVCaptureFigVideoDevice _disableContinuousAutoFocusTracking]
+ -[AVCaptureFigVideoDevice _handleDeviceAngleChanged:]
+ -[AVCaptureFigVideoDevice _handleOccludedChange:]
+ -[AVCaptureFigVideoDevice _handlePrimaryDisplayRegionChanged:]
+ -[AVCaptureFigVideoDevice _queryPrimaryDisplayRegion]
+ -[AVCaptureFigVideoDevice _setExposureModeCustomWithLensAperture:duration:ISO:entryPoint:completionHandler:]
+ -[AVCaptureFigVideoDevice _setExposureWithMode:duration:ISO:lensAperture:requestID:newMaxFrameDuration:]
+ -[AVCaptureFigVideoDevice activeExposureSignals]
+ -[AVCaptureFigVideoDevice activeOmahaConstituentDeviceType]
+ -[AVCaptureFigVideoDevice autoExposureLensApertureRateLimit]
+ -[AVCaptureFigVideoDevice automaticallyAdjustsExposureDuration]
+ -[AVCaptureFigVideoDevice automaticallyAdjustsISO]
+ -[AVCaptureFigVideoDevice automaticallyAdjustsLensAperture]
+ -[AVCaptureFigVideoDevice automaticallyEnablesExposureSignals]
+ -[AVCaptureFigVideoDevice continuousAutoFocusTrackingLensPositionBias]
+ -[AVCaptureFigVideoDevice deviceAngle]
+ -[AVCaptureFigVideoDevice enabledExposureSignals]
+ -[AVCaptureFigVideoDevice faceIDCoexistenceSupported]
+ -[AVCaptureFigVideoDevice faceIDUnwrapResult]
+ -[AVCaptureFigVideoDevice faceIDUnwrapSupported]
+ -[AVCaptureFigVideoDevice isContinuousAutoFocusTrackingEnabled]
+ -[AVCaptureFigVideoDevice isContinuousAutoFocusTrackingSubjectAcquired]
+ -[AVCaptureFigVideoDevice isFaceIDCoexistenceEnabled]
+ -[AVCaptureFigVideoDevice isLowCurrentTorchEnabled]
+ -[AVCaptureFigVideoDevice isLowCurrentTorchSupported]
+ -[AVCaptureFigVideoDevice isLowLightVideoNoiseReductionEnabled]
+ -[AVCaptureFigVideoDevice isOmahaVariant]
+ -[AVCaptureFigVideoDevice isPrimaryConstituentDeviceSwitchingBehaviorLockedWithDeviceSupported]
+ -[AVCaptureFigVideoDevice personalPhotographerSubjectDetectionStatus]
+ -[AVCaptureFigVideoDevice primaryDisplayRegion]
+ -[AVCaptureFigVideoDevice releaseFaceIDFrameProxyWithIdentifier:]
+ -[AVCaptureFigVideoDevice secureSigningPhotoCaptureEnabled]
+ -[AVCaptureFigVideoDevice setAutoExposureLensApertureRateLimit:]
+ -[AVCaptureFigVideoDevice setAutomaticallyEnablesExposureSignals:]
+ -[AVCaptureFigVideoDevice setContinuousAutoFocusTrackingEnabled:]
+ -[AVCaptureFigVideoDevice setContinuousAutoFocusTrackingLensPositionBias:]
+ -[AVCaptureFigVideoDevice setEnabledExposureSignals:]
+ -[AVCaptureFigVideoDevice setExposureModeCustomWithLensAperture:duration:ISO:completionHandler:]
+ -[AVCaptureFigVideoDevice setFaceIDCoexistenceEnabled:]
+ -[AVCaptureFigVideoDevice setLowCurrentTorchEnabled:]
+ -[AVCaptureFigVideoDevice setLowLightVideoNoiseReductionEnabled:]
+ -[AVCaptureFigVideoDevice setPrimaryConstituentDeviceSwitchingBehaviorLockedWithDevice:]
+ -[AVCaptureFigVideoDevice setSecureSigningPhotoCaptureEnabled:]
+ -[AVCaptureFigVideoDevice startFaceIDUnwrap]
+ -[AVCaptureFigVideoDevice supportedExposureSignals]
+ -[AVCaptureFileOutputDelegateWrapper setTimewarpDestinationFrameRate:]
+ -[AVCaptureFileOutputDelegateWrapper timewarpDestinationFrameRate]
+ -[AVCaptureMetadataOutput captureFaceIDBracketWithConfiguration:]
+ -[AVCaptureMetadataOutput faceIDConfiguration]
+ -[AVCaptureMetadataOutput rawFrameDeliveryEnabled]
+ -[AVCaptureMetadataOutput rawFrameDeliverySupported]
+ -[AVCaptureMetadataOutput setFaceIDConfiguration:]
+ -[AVCaptureMetadataOutput setRawFrameDeliveryEnabled:]
+ -[AVCaptureMovieFileOutput _updateCinematicVideoMetadataCaptureSupportedForSourceDevice:]
+ -[AVCaptureMovieFileOutput automaticallyAdjustsCinematicVideoMetadataCaptureEnabled]
+ -[AVCaptureMovieFileOutput cinematicVideoMetadataCaptureEnabledByClient]
+ -[AVCaptureMovieFileOutput handleChangedDynamicAspectRatio:forFormat:]
+ -[AVCaptureMovieFileOutput handleVideoStabilizationStrengthChangedForDevice:]
+ -[AVCaptureMovieFileOutput isCinematicVideoMetadataCaptureEnabled]
+ -[AVCaptureMovieFileOutput isCinematicVideoMetadataCaptureSupported]
+ -[AVCaptureMovieFileOutput isTimewarpEnabled]
+ -[AVCaptureMovieFileOutput isTimewarpSupported]
+ -[AVCaptureMovieFileOutput setAutomaticallyAdjustsCinematicVideoMetadataCaptureEnabled:]
+ -[AVCaptureMovieFileOutput setCinematicVideoMetadataCaptureEnabled:]
+ -[AVCaptureMovieFileOutput setTimewarpDestinationFrameRate:]
+ -[AVCaptureMovieFileOutput setTimewarpEnabled:]
+ -[AVCaptureMovieFileOutput setTimewarpMode:]
+ -[AVCaptureMovieFileOutput timewarpDestinationFrameRate]
+ -[AVCaptureMovieFileOutput timewarpMode]
+ -[AVCaptureMovieFileOutputAssetWriterInputHelper dealloc]
+ -[AVCaptureMovieFileOutputAssetWriterInputHelper ensureWriterInputIsReadyForMoreMediaData]
+ -[AVCaptureMovieFileOutputAssetWriterInputHelper initWithAsssetWriterInput:]
+ -[AVCaptureMovieFileOutputAssetWriterInputHelper observeValueForKeyPath:ofObject:change:context:]
+ -[AVCaptureOutput handleVideoStabilizationStrengthChangedForDevice:]
+ -[AVCapturePersonalPhotographerDuplicateInfo description]
+ -[AVCapturePersonalPhotographerDuplicateInfo encodeWithCoder:]
+ -[AVCapturePersonalPhotographerDuplicateInfo initWithCoder:]
+ -[AVCapturePersonalPhotographerDuplicateInfo initWithDuplicateInfoDictionary:]
+ -[AVCapturePersonalPhotographerDuplicateInfo originalPresentationTimestamp]
+ -[AVCapturePersonalPhotographerDuplicateInfo replacedPhotoTimestamp]
+ -[AVCapturePersonalPhotographerDuplicateInfo settingsID]
+ -[AVCapturePersonalPhotographerMetadata dealloc]
+ -[AVCapturePersonalPhotographerMetadata description]
+ -[AVCapturePersonalPhotographerMetadata detectedContext]
+ -[AVCapturePersonalPhotographerMetadata duplicateInfo]
+ -[AVCapturePersonalPhotographerMetadata encodeWithCoder:]
+ -[AVCapturePersonalPhotographerMetadata frameID]
+ -[AVCapturePersonalPhotographerMetadata frameScore]
+ -[AVCapturePersonalPhotographerMetadata initWithCoder:]
+ -[AVCapturePersonalPhotographerMetadata initWithPersonalPhotographerMetadataDictionary:]
+ -[AVCapturePersonalPhotographerMetadata manualCapture]
+ -[AVCapturePersonalPhotographerMetadata sessionID]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator _addExpectedTimestamp:]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator _handleWatchdogTimeout]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator _invokeCompletionWithRequest:error:]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator _shouldInvokeCompletionCopyOutRequest:copyOutError:]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator dealloc]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator description]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator finishWithRequest:expectedTimestamps:error:]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator initWithCompletionHandler:]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator recordCaptureCompleteForSettingsID:]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator recordStillCompleteForSettingsID:timestamp:]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator reset]
+ -[AVCapturePersonalPhotographerSessionResults _isPhotoRegisteredWithTimestampNSValue:]
+ -[AVCapturePersonalPhotographerSessionResults dealloc]
+ -[AVCapturePersonalPhotographerSessionResults debugDescription]
+ -[AVCapturePersonalPhotographerSessionResults description]
+ -[AVCapturePersonalPhotographerSessionResults initWithPhotoSettingsUniqueID:]
+ -[AVCapturePersonalPhotographerSessionResults isPhotoRegisteredForDeletionWithTimestamp:]
+ -[AVCapturePersonalPhotographerSessionResults isPhotoRegisteredWithTimestamp:]
+ -[AVCapturePersonalPhotographerSessionResults photoSettingsUniqueID]
+ -[AVCapturePersonalPhotographerSessionResults registerPhotoCapturedWithTimestamp:]
+ -[AVCapturePersonalPhotographerSessionResults registerPhotoTimestampForDeletion:]
+ -[AVCapturePersonalPhotographerSessionResults systemRecommendedPhotosToDeleteByTimestamp]
+ -[AVCapturePersonalPhotographerSessionResults systemRecommendedPhotosToSaveByTimestamp]
+ -[AVCapturePhoto initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:photoLibraryThumbnails:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:secureSignedRawSurface:secureSignedRawSurfaceSize:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:underlyingSourceDeviceType:sourceDeviceType:]
+ -[AVCapturePhoto personalPhotographerMetadata]
+ -[AVCapturePhoto secureSignedPhotoData]
+ -[AVCapturePhotoOutput _copyPersonalPhotographerSessionPhotoRequestWithUniqueID:]
+ -[AVCapturePhotoOutput _dispatchPersonalPhotographerSessionDidFinishCallbackForRequest:error:cleanupRequest:]
+ -[AVCapturePhotoOutput _dispatchPersonalPhotographerSessionDidFinishWithFailureCallbackForPhotoSettings:figSettings:toDelegate:withError:]
+ -[AVCapturePhotoOutput _handleDidFinishPersonalPhotographerSessionNotificationWithPayload:forRequest:]
+ -[AVCapturePhotoOutput _personalPhotographerSessionPhotoRequestForUniqueID:]
+ -[AVCapturePhotoOutput _updatePersonalPhotographerSupportedForDevice:]
+ -[AVCapturePhotoOutput _updateSecureSigningPhotoCaptureSupportedForSourceDevice:]
+ -[AVCapturePhotoOutput initiateManualPersonalPhotographerCapture]
+ -[AVCapturePhotoOutput isPersonalPhotographerEnabled]
+ -[AVCapturePhotoOutput isPersonalPhotographerSessionActive]
+ -[AVCapturePhotoOutput isPersonalPhotographerSupported]
+ -[AVCapturePhotoOutput isSecureSigningPhotoCaptureEnabled]
+ -[AVCapturePhotoOutput isSecureSigningPhotoCaptureSupportEnabled]
+ -[AVCapturePhotoOutput isSecureSigningPhotoCaptureSupported]
+ -[AVCapturePhotoOutput setPersonalPhotographerEnabled:]
+ -[AVCapturePhotoOutput setSecureSigningPhotoCaptureEnabled:]
+ -[AVCapturePhotoOutput setSecureSigningPhotoCaptureSupportEnabled:]
+ -[AVCapturePhotoOutput startPersonalPhotographerSessionWithSettings:delegate:]
+ -[AVCapturePhotoOutput stopPersonalPhotographerSession]
+ -[AVCapturePhotoSettings isAutoSecureSigningPhotoCaptureEnabled]
+ -[AVCapturePhotoSettings personalPhotographerCaptureRate]
+ -[AVCapturePhotoSettings setAutoSecureSigningPhotoCaptureEnabled:]
+ -[AVCapturePhotoSettings setPersonalPhotographerCaptureRate:]
+ -[AVCapturePhotographicStyle _initWithSmartStyle:textureStyle:]
+ -[AVCapturePhotographicStyle textureStyle]
+ -[AVCaptureResolvedPhotoSettings _initWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:]
+ -[AVCaptureResolvedPhotoSettings isSecureSigningPhotoCaptureEnabled]
+ -[AVCaptureSecureVideoDataOutput _handleLocalQueueMessage:]
+ -[AVCaptureSecureVideoDataOutput _handleNotification:payload:]
+ -[AVCaptureSecureVideoDataOutput _handleRemoteQueueOperation:]
+ -[AVCaptureSecureVideoDataOutput _processSampleBuffer:]
+ -[AVCaptureSecureVideoDataOutput _updateLocalQueue:]
+ -[AVCaptureSecureVideoDataOutput _updateRemoteQueue:]
+ -[AVCaptureSecureVideoDataOutput addConnection:error:]
+ -[AVCaptureSecureVideoDataOutput alwaysDiscardsLateSecureVideoFrames:]
+ -[AVCaptureSecureVideoDataOutput alwaysDiscardsLateSecureVideoFrames]
+ -[AVCaptureSecureVideoDataOutput attachSafelyToFigCaptureSession:]
+ -[AVCaptureSecureVideoDataOutput canAddConnection:failureReason:]
+ -[AVCaptureSecureVideoDataOutput connectionMediaTypes]
+ -[AVCaptureSecureVideoDataOutput dealloc]
+ -[AVCaptureSecureVideoDataOutput delegateCallbackQueue]
+ -[AVCaptureSecureVideoDataOutput delegateOverrideCallbackQueue]
+ -[AVCaptureSecureVideoDataOutput delegateOverride]
+ -[AVCaptureSecureVideoDataOutput delegate]
+ -[AVCaptureSecureVideoDataOutput detachSafelyFromFigCaptureSession:]
+ -[AVCaptureSecureVideoDataOutput init]
+ -[AVCaptureSecureVideoDataOutput removeConnection:]
+ -[AVCaptureSecureVideoDataOutput sampleBufferCallbackQueue]
+ -[AVCaptureSecureVideoDataOutput sampleBufferDelegate]
+ -[AVCaptureSecureVideoDataOutput setAlwaysDiscardsLateSecureVideoFrames:]
+ -[AVCaptureSecureVideoDataOutput setDelegateOverride:delegateOverrideCallbackQueue:]
+ -[AVCaptureSecureVideoDataOutput setSampleBufferDelegate:queue:]
+ -[AVCaptureSession _configureCinematicVideoMetadataIfNeededForSessionConfiguration:]
+ -[AVCaptureSession _getTextureStyleSupported:]
+ -[AVCaptureSession _handleVideoStabilizationStrengthChangedForDevice:]
+ -[AVCaptureSession _lowLightVideoNoiseReductionANEAndGPUCost]
+ -[AVCaptureSession _setTextureStyleSetByClient:]
+ -[AVCaptureSession _textureStyleSetByClient]
+ -[AVCaptureSession _updateLowLightVideoNoiseReductionEnabledForAllConnections]
+ -[AVCaptureSession _updatePrimaryDisplayRegionIfNeeded]
+ -[AVCaptureSession _validateCinematicVideoMetadataConfiguration:]
+ -[AVCaptureSession _validateFaceIDConfiguration:]
+ -[AVCaptureSession textureStyleEnabled]
+ -[AVCaptureTextureStyle _initWithPreset:intensity:grain:]
+ -[AVCaptureTextureStyle dealloc]
+ -[AVCaptureTextureStyle debugDescription]
+ -[AVCaptureTextureStyle description]
+ -[AVCaptureTextureStyle grain]
+ -[AVCaptureTextureStyle intensity]
+ -[AVCaptureTextureStyle isEqual:]
+ -[AVCaptureTextureStyle preset]
+ -[AVCaptureTextureStyle version]
+ -[AVMetadataCinematicVideoMetadataObject copyWithZone:]
+ -[AVMetadataCinematicVideoMetadataObject dealloc]
+ -[AVMetadataCinematicVideoMetadataObject description]
+ -[AVMetadataCinematicVideoMetadataObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:]
+ -[AVMetadataCinematicVideoMetadataObject initWithPayload:input:time:]
+ -[AVMetadataCinematicVideoMetadataObject payload]
+ -[AVMetadataCinematicVideoMetadataObject timedMetadataGroup]
+ -[AVMetadataFaceIDFrameProxy dealloc]
+ -[AVMetadataFaceIDFrameProxy formatDescription]
+ -[AVMetadataFaceIDFrameProxy frameIdentifier]
+ -[AVMetadataFaceIDFrameProxy initWithFrameDictionary:sourceCaptureInput:]
+ -[AVMetadataFaceIDFrameProxy setFormatDescription:]
+ -[AVMetadataFaceIDFrameProxy setFrameIdentifier:]
+ -[AVMetadataFaceIDFrameProxy setSharedMemoryAreaOffset:]
+ -[AVMetadataFaceIDFrameProxy sharedMemoryAreaOffset]
+ -[AVMetadataFaceIDObject bracketProbePatternType]
+ -[AVMetadataFaceIDObject coachingStatus]
+ -[AVMetadataFaceIDObject contextIndex]
+ -[AVMetadataFaceIDObject copyWithZone:]
+ -[AVMetadataFaceIDObject dealloc]
+ -[AVMetadataFaceIDObject description]
+ -[AVMetadataFaceIDObject frameType]
+ -[AVMetadataFaceIDObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:]
+ -[AVMetadataFaceIDObject initWithFaceIDResultDictionary:metadataDictionary:time:sourceCaptureInput:]
+ -[AVMetadataFaceIDObject isReady]
+ -[AVMetadataFaceIDObject lightSourceProjectorMode]
+ -[AVMetadataFaceIDObject metadataFrameProxy]
+ -[AVMetadataFaceIDObject metadata]
+ -[AVMetadataFaceIDObject rawFrameProxy]
+ -[AVMetadataFaceIDObject referenceFrameProxy]
+ -[AVMetadataFaceIDObject userEngagementStatus]
+ -[AVMetadataFaceObject metadataFrameProxy]
+ -[AVMetadataFaceObject rawFrameProxy]
+ -[AVMetadataFaceObjectInternal metadataFrameProxy]
+ -[AVMetadataFaceObjectInternal rawFrameProxy]
+ -[AVMetadataFaceObjectInternal setMetadataFrameProxy:]
+ -[AVMetadataFaceObjectInternal setRawFrameProxy:]
+ -[AVMetadataFocusTrackedObject copyWithZone:]
+ -[AVMetadataFocusTrackedObject dealloc]
+ -[AVMetadataFocusTrackedObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:]
+ -[AVMetadataFocusTrackedObject initWithObjectID:mask:bounds:input:time:]
+ -[AVMetadataObject mask]
+ -[AVMetadataObjectInternal mask]
+ -[AVMetadataObjectInternal setMask:]
+ -[AVSpatialOverCaptureVideoPreviewLayer primaryDisplayRegion]
+ -[AVSpatialOverCaptureVideoPreviewLayer setPrimaryDisplayRegion:]
+ GCC_except_table100
+ GCC_except_table1023
+ GCC_except_table1029
+ GCC_except_table1037
+ GCC_except_table1047
+ GCC_except_table115
+ GCC_except_table131
+ GCC_except_table135
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table140
+ GCC_except_table141
+ GCC_except_table150
+ GCC_except_table156
+ GCC_except_table159
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table167
+ GCC_except_table169
+ GCC_except_table170
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table185
+ GCC_except_table187
+ GCC_except_table189
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table206
+ GCC_except_table211
+ GCC_except_table213
+ GCC_except_table215
+ GCC_except_table217
+ GCC_except_table224
+ GCC_except_table228
+ GCC_except_table229
+ GCC_except_table230
+ GCC_except_table233
+ GCC_except_table234
+ GCC_except_table237
+ GCC_except_table240
+ GCC_except_table241
+ GCC_except_table243
+ GCC_except_table250
+ GCC_except_table265
+ GCC_except_table266
+ GCC_except_table274
+ GCC_except_table280
+ GCC_except_table289
+ GCC_except_table301
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table315
+ GCC_except_table318
+ GCC_except_table338
+ GCC_except_table339
+ GCC_except_table342
+ GCC_except_table345
+ GCC_except_table350
+ GCC_except_table351
+ GCC_except_table355
+ GCC_except_table362
+ GCC_except_table369
+ GCC_except_table371
+ GCC_except_table375
+ GCC_except_table385
+ GCC_except_table388
+ GCC_except_table424
+ GCC_except_table435
+ GCC_except_table437
+ GCC_except_table439
+ GCC_except_table448
+ GCC_except_table45
+ GCC_except_table487
+ GCC_except_table497
+ GCC_except_table509
+ GCC_except_table529
+ GCC_except_table532
+ GCC_except_table558
+ GCC_except_table562
+ GCC_except_table57
+ GCC_except_table575
+ GCC_except_table583
+ GCC_except_table591
+ GCC_except_table597
+ GCC_except_table602
+ GCC_except_table609
+ GCC_except_table616
+ GCC_except_table626
+ GCC_except_table640
+ GCC_except_table663
+ GCC_except_table674
+ GCC_except_table684
+ GCC_except_table698
+ GCC_except_table720
+ GCC_except_table73
+ GCC_except_table739
+ GCC_except_table760
+ GCC_except_table763
+ GCC_except_table800
+ GCC_except_table802
+ GCC_except_table804
+ GCC_except_table806
+ GCC_except_table833
+ GCC_except_table845
+ GCC_except_table847
+ GCC_except_table849
+ GCC_except_table855
+ GCC_except_table857
+ GCC_except_table88
+ GCC_except_table900
+ GCC_except_table904
+ GCC_except_table95
+ GCC_except_table973
+ GCC_except_table975
+ GCC_except_table977
+ _AVAppleMakerNote_ProvenanceFlags
+ _AVAppleMakerNote_TextureStyleKey_Grain
+ _AVAppleMakerNote_TextureStyleKey_Intensity
+ _AVAppleMakerNote_TextureStyleKey_OriginalInsteadOfReversibility
+ _AVAppleMakerNote_TextureStyleKey_Preset
+ _AVAppleMakerNote_TextureStyleKey_RenderingVersion
+ _AVCaptureAncillaryDataUserKeyRDD18InstanceUID
+ _AVCaptureAncillaryDataUserKeyRDD18UDAMSetVersion
+ _AVCaptureAncillaryDataUserKeyRDD18UserItems
+ _AVCaptureAspectRatioSupportsCinematicVideoMetadata
+ _AVCaptureConnectionDeviceAutoVideoFrameRateEnabledChangedContext
+ _AVCaptureConnectionDeviceCinematicVideoCaptureEnabledChangedContext
+ _AVCaptureConnectionDeviceVideoStabilizationStrengthChangedContext
+ _AVCaptureConnectionTimewarpModeChangedContext
+ _AVCaptureDeviceAngleDidChangeNotification
+ _AVCaptureDeviceExposureSignalDocument
+ _AVCaptureDeviceExposureSignalFlicker
+ _AVCaptureDeviceExposureSignalGroupPhoto
+ _AVCaptureDeviceExposureSignalStarburst
+ _AVCaptureDeviceExposureSignalSubjectMotion
+ _AVCaptureDeviceTypeBuiltInBostonUltraWideCamera
+ _AVCaptureDeviceTypeBuiltInColorAssistedInfraredMetadataCamera
+ _AVCaptureDeviceTypeBuiltInRenoUltraWideCamera
+ _AVCaptureDeviceTypeBuiltInRenoUltraWideMetadataCamera
+ _AVCaptureExposureDurationAuto
+ _AVCaptureISOAuto
+ _AVCaptureIsTimewarpSupported
+ _AVCaptureLensApertureAuto
+ _AVCaptureLensApertureCurrent
+ _AVCapturePersonalPhotographerMetadataDictionary
+ _AVCapturePhotographicStyleSettingsTextureStyleGrainKey
+ _AVCapturePhotographicStyleSettingsTextureStyleIntensityKey
+ _AVCapturePhotographicStyleSettingsTextureStylePresetKey
+ _AVCaptureSessionPrimaryDisplayRegionChangedContext
+ _AVCaptureSessionStateSupportsCinematicVideoMetadata
+ _AVCaptureSessionVideoInputDeviceActiveOmahaConstituentDeviceTypeChangedContext
+ _AVCaptureSessionVideoInputDeviceFaceIDCoexistenceEnabledChangedContext
+ _AVCaptureSessionVideoInputDeviceSuspendedChangedContext
+ _AVCaptureTextureStylePresetFilmic
+ _AVCaptureTextureStylePresetGlowy
+ _AVCaptureTextureStylePresetPreview
+ _AVCaptureTextureStylePresetSoft
+ _AVCaptureTextureStylePresetStandard
+ _AVCaptureTextureStylePresetStudio
+ _AVCaptureTimewarpTimelapseClassicIntermediateFilePathPostfix
+ _AVGQCaptureLowLightVideoNoiseReductionAutomaticallyEnabled
+ _AVGQCaptureOmahaConstituentDevicesSupported
+ _AVMediaTypeSecureVideo
+ _AVMetadataObjectTypeCinematicVideoMetadata
+ _AVMetadataObjectTypeFaceID
+ _AVMetadataObjectTypeFocusTrackedObject
+ _AVTrackAssociationTypeMetadataReferent
+ _AVTrackAssociationTypeRenderMetadataSource
+ _AVVideoColorPrimariesKey
+ _AVVideoColorPropertiesKey
+ _AVVideoTransferFunctionKey
+ _AVVideoYCbCrMatrixKey
+ _C743
+ _CFArrayContainsValue
+ _CMFormatDescriptionGetExtension
+ _CMSampleBufferCreateCopyWithNewTiming
+ _CMSampleBufferCreateReady
+ _CMSampleBufferGetNumSamples
+ _CMSampleBufferGetSampleAttachmentsArray
+ _CMTimeRangeMake
+ _CMVideoFormatDescriptionGetH264ParameterSetAtIndex
+ _FigCaptureSourceRemoteIsSecureSigningCertificateAvailable
+ _FigCaptureTimewarpClassicTimelapseIntermediateFileBitRateMultiplier
+ _FigDebugIsInternalBuild
+ _FigSampleBufferGetEXSurfaceProxy
+ _FigVideoFormatDescriptionCreateFromSPSAndPPS
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_AVAssetReader
+ _OBJC_CLASS_$_AVAssetReaderOutputMetadataAdaptor
+ _OBJC_CLASS_$_AVAssetReaderTrackOutput
+ _OBJC_CLASS_$_AVAssetWriter
+ _OBJC_CLASS_$_AVAssetWriterInput
+ _OBJC_CLASS_$_AVAssetWriterInputMetadataAdaptor
+ _OBJC_CLASS_$_AVAssetWriterInputPixelBufferAdaptor
+ _OBJC_CLASS_$_AVCaptureAncillaryDataEncoder
+ _OBJC_CLASS_$_AVCaptureDeviceStateCoordinatorUtilities
+ _OBJC_CLASS_$_AVCaptureDeviceStateDescriptor
+ _OBJC_CLASS_$_AVCaptureFaceIDBracketConfiguration
+ _OBJC_CLASS_$_AVCaptureFaceIDBracketEncryptionConfiguration
+ _OBJC_CLASS_$_AVCaptureFaceIDConfiguration
+ _OBJC_CLASS_$_AVCaptureFaceIDUnwrapResult
+ _OBJC_CLASS_$_AVCaptureMovieFileOutputAssetWriterInputHelper
+ _OBJC_CLASS_$_AVCapturePersonalPhotographerDuplicateInfo
+ _OBJC_CLASS_$_AVCapturePersonalPhotographerMetadata
+ _OBJC_CLASS_$_AVCapturePersonalPhotographerSessionFinishCoordinator
+ _OBJC_CLASS_$_AVCapturePersonalPhotographerSessionResults
+ _OBJC_CLASS_$_AVCaptureSecureVideoDataOutput
+ _OBJC_CLASS_$_AVCaptureTextureStyle
+ _OBJC_CLASS_$_AVMetadataCinematicVideoMetadataObject
+ _OBJC_CLASS_$_AVMetadataFaceIDFrameProxy
+ _OBJC_CLASS_$_AVMetadataFaceIDObject
+ _OBJC_CLASS_$_AVMetadataFocusTrackedObject
+ _OBJC_CLASS_$_AVTimedMetadataGroup
+ _OBJC_CLASS_$_AVURLAsset
+ _OBJC_CLASS_$_CMCaptureCinematicVideoTimedMetadataSampleGenerator
+ _OBJC_CLASS_$_FigCaptureSecureVideoDataSinkConfiguration
+ _OBJC_CLASS_$_FigCaptureTextureStyle
+ _OBJC_IVAR_$_AVCaptureAncillaryDataEncoder._currentUserDefinedAncillaryData
+ _OBJC_IVAR_$_AVCaptureAncillaryDataEncoder._enabled
+ _OBJC_IVAR_$_AVCaptureAncillaryDataEncoder._output
+ _OBJC_IVAR_$_AVCaptureAncillaryDataEncoder._setUUID
+ _OBJC_IVAR_$_AVCaptureBroadcastVideoOutput._ancillaryDataEncoder
+ _OBJC_IVAR_$_AVCaptureConnectionInternal.automaticallyEnablesLowLightVideoNoiseReduction
+ _OBJC_IVAR_$_AVCaptureConnectionInternal.lowLightVideoNoiseReductionEnabled
+ _OBJC_IVAR_$_AVCaptureConnectionInternal.lowLightVideoNoiseReductionSupported
+ _OBJC_IVAR_$_AVCaptureConnectionInternal.secureVideoInputPort
+ _OBJC_IVAR_$_AVCaptureDeviceFormatInternal.cinematicVideoMetadataCaptureSupported
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinatorUtilities._bostonDescriptors
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinatorUtilities._omahaDescriptors
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinatorUtilities._otherDescriptors
+ _OBJC_IVAR_$_AVCaptureDeviceStateCoordinatorUtilities._renoDescriptors
+ _OBJC_IVAR_$_AVCaptureDeviceStateDescriptor._deviceType
+ _OBJC_IVAR_$_AVCaptureDeviceStateDescriptor._localizedName
+ _OBJC_IVAR_$_AVCaptureDeviceStateDescriptor._mediaTypes
+ _OBJC_IVAR_$_AVCaptureDeviceStateDescriptor._position
+ _OBJC_IVAR_$_AVCaptureDeviceStateDescriptor._uniqueID
+ _OBJC_IVAR_$_AVCaptureFaceIDBracketConfiguration._colorBracketEncryptionConfiguration
+ _OBJC_IVAR_$_AVCaptureFaceIDBracketConfiguration._doubleOrder
+ _OBJC_IVAR_$_AVCaptureFaceIDBracketConfiguration._infraredBracketEncryptionConfiguration
+ _OBJC_IVAR_$_AVCaptureFaceIDBracketConfiguration._numberOfDoubles
+ _OBJC_IVAR_$_AVCaptureFaceIDBracketConfiguration._probePatternIndex
+ _OBJC_IVAR_$_AVCaptureFaceIDBracketConfiguration._probePatternType
+ _OBJC_IVAR_$_AVCaptureFaceIDBracketEncryptionConfiguration._hostMainKeyIndex
+ _OBJC_IVAR_$_AVCaptureFaceIDBracketEncryptionConfiguration._initializationVector
+ _OBJC_IVAR_$_AVCaptureFaceIDBracketEncryptionConfiguration._linearFeedbackShiftRegisterSeed
+ _OBJC_IVAR_$_AVCaptureFaceIDBracketEncryptionConfiguration._nonce
+ _OBJC_IVAR_$_AVCaptureFaceIDConfiguration._attentionRequired
+ _OBJC_IVAR_$_AVCaptureFaceIDConfiguration._frameLogEnabled
+ _OBJC_IVAR_$_AVCaptureFaceIDConfiguration._frameMetadataEnabled
+ _OBJC_IVAR_$_AVCaptureFaceIDConfiguration._mode
+ _OBJC_IVAR_$_AVCaptureFaceIDConfiguration._periocularEnabled
+ _OBJC_IVAR_$_AVCaptureFaceIDConfiguration._retryType
+ _OBJC_IVAR_$_AVCaptureFaceIDUnwrapResult._cameraStreamError
+ _OBJC_IVAR_$_AVCaptureFaceIDUnwrapResult._pearlSecureSessionUnwrapError
+ _OBJC_IVAR_$_AVCaptureFaceIDUnwrapResult._unwrapStatus
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._activeExposureSignalsBitmask
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._activeOmahaConstituentDeviceType
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._autoExposureLensApertureRateLimit
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._automaticallyEnablesExposureSignals
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._continuousAutoFocusTrackingBiasUpdateOnly
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._continuousAutoFocusTrackingEnabled
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._continuousAutoFocusTrackingLensPositionBias
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._continuousAutoFocusTrackingSubjectAcquired
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._deviceAngle
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._faceIDCoexistenceEnabled
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._faceIDCoexistenceSupported
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._faceIDUnwrapResult
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._ignoredExposureSignalsBitmask
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._lastLensApertureCommand
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._lensApertureKVO
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._lowCurrentTorchEnabled
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._personalPhotographerSubjectDetectionStatus
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._primaryDisplayRegion
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._primaryDisplayRegionSupported
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._supportedExposureSignalsBitmask
+ _OBJC_IVAR_$_AVCaptureFileOutputDelegateWrapper._timewarpDestinationFrameRate
+ _OBJC_IVAR_$_AVCaptureMetadataOutputInternal.cinematicVideoMetadataCaptureSupported
+ _OBJC_IVAR_$_AVCaptureMetadataOutputInternal.continuousAutoFocusTrackingSupported
+ _OBJC_IVAR_$_AVCaptureMetadataOutputInternal.faceIDConfiguration
+ _OBJC_IVAR_$_AVCaptureMetadataOutputInternal.rawFrameDeliveryEnabled
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputAssetWriterInputHelper._assetWriterInput
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputAssetWriterInputHelper._readyForMoreSemaphore
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputAssetWriterInputHelper._signalRequestLock
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputAssetWriterInputHelper._signalRequested
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.automaticallyAdjustsCinematicVideoMetadataCaptureEnabled
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.cinematicVideoMetadataAspectRatioSupported
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.cinematicVideoMetadataCaptureEnabledByClient
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.cinematicVideoMetadataCaptureSupported
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.timewarpDecimationQueue
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.timewarpDestinationFrameRate
+ _OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.timewarpMode
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerDuplicateInfo._originalPresentationTimestamp
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerDuplicateInfo._replacedPhotoTimestamp
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerDuplicateInfo._settingsID
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerMetadata._detectedContext
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerMetadata._duplicateInfo
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerMetadata._frameID
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerMetadata._frameScore
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerMetadata._manualCapture
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerMetadata._sessionID
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._completed
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._completedSettingsIDs
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._completionHandler
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._expectedSetOfTimestampsCommitted
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._expectedSettingsIDs
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._lock
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._pendingError
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._pendingRequest
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._settingsIDByTimestamp
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._unmappedExpectedTimestamps
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._watchdog
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionResults._capturedPhotos
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionResults._photoSettingsUniqueID
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionResults._systemRecommendedPhotosToDeleteByTimestamp
+ _OBJC_IVAR_$_AVCapturePersonalPhotographerSessionResults._systemRecommendedPhotosToSaveByTimestamp
+ _OBJC_IVAR_$_AVCapturePhotoInternal.personalPhotographerMetadata
+ _OBJC_IVAR_$_AVCapturePhotoInternal.secureSignedRawSurface
+ _OBJC_IVAR_$_AVCapturePhotoInternal.secureSignedRawSurfaceSize
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.personalPhotographerEnabled
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.personalPhotographerSessionActive
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.personalPhotographerSessionFinishCoordinator
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.personalPhotographerSessionPhotoRequest
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.personalPhotographerSessionResults
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.personalPhotographerSupported
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.secureSigningPhotoCaptureEnabled
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.secureSigningPhotoCaptureSupportEnabled
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.secureSigningPhotoCaptureSupported
+ _OBJC_IVAR_$_AVCapturePhotoSettingsInternal.autoSecureSigningPhotoCaptureEnabled
+ _OBJC_IVAR_$_AVCapturePhotoSettingsInternal.personalPhotographerCaptureRate
+ _OBJC_IVAR_$_AVCapturePhotographicStyle._textureStyle
+ _OBJC_IVAR_$_AVCaptureResolvedPhotoSettingsInternal.secureSigningPhotoCaptureEnabled
+ _OBJC_IVAR_$_AVCaptureSecureVideoDataOutput._alwaysDiscardsLateSecureVideoFrames
+ _OBJC_IVAR_$_AVCaptureSecureVideoDataOutput._delegateCallbackHelper
+ _OBJC_IVAR_$_AVCaptureSecureVideoDataOutput._frameRateMonitor
+ _OBJC_IVAR_$_AVCaptureSecureVideoDataOutput._sampleBufferCallbackQueue
+ _OBJC_IVAR_$_AVCaptureSecureVideoDataOutput._sampleBufferDelegate
+ _OBJC_IVAR_$_AVCaptureSecureVideoDataOutput._weakReference
+ _OBJC_IVAR_$_AVCaptureSessionInternal.textureStyleEnabled
+ _OBJC_IVAR_$_AVCaptureSessionInternal.textureStyleSetByClient
+ _OBJC_IVAR_$_AVCaptureSessionInternal.textureStyleSupported
+ _OBJC_IVAR_$_AVCaptureTextureStyle._grain
+ _OBJC_IVAR_$_AVCaptureTextureStyle._hash
+ _OBJC_IVAR_$_AVCaptureTextureStyle._intensity
+ _OBJC_IVAR_$_AVCaptureTextureStyle._preset
+ _OBJC_IVAR_$_AVCaptureTextureStyle._version
+ _OBJC_IVAR_$_AVMetadataCinematicVideoMetadataObject._payload
+ _OBJC_IVAR_$_AVMetadataFaceIDFrameProxy._formatDescription
+ _OBJC_IVAR_$_AVMetadataFaceIDFrameProxy._frameIdentifier
+ _OBJC_IVAR_$_AVMetadataFaceIDFrameProxy._sharedMemoryAreaOffset
+ _OBJC_IVAR_$_AVMetadataFaceIDFrameProxy._sourceDevice
+ _OBJC_IVAR_$_AVMetadataFaceIDObject._bracketProbePatternType
+ _OBJC_IVAR_$_AVMetadataFaceIDObject._coachingStatus
+ _OBJC_IVAR_$_AVMetadataFaceIDObject._contextIndex
+ _OBJC_IVAR_$_AVMetadataFaceIDObject._frameType
+ _OBJC_IVAR_$_AVMetadataFaceIDObject._lightSourceProjectorMode
+ _OBJC_IVAR_$_AVMetadataFaceIDObject._metadata
+ _OBJC_IVAR_$_AVMetadataFaceIDObject._metadataFrameProxy
+ _OBJC_IVAR_$_AVMetadataFaceIDObject._rawFrameProxy
+ _OBJC_IVAR_$_AVMetadataFaceIDObject._ready
+ _OBJC_IVAR_$_AVMetadataFaceIDObject._referenceFrameProxy
+ _OBJC_IVAR_$_AVMetadataFaceIDObject._userEngagementStatus
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._metadataFrameProxy
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._rawFrameProxy
+ _OBJC_IVAR_$_AVMetadataObjectInternal._mask
+ _OBJC_IVAR_$_AVSpatialOverCaptureVideoPreviewLayer._primaryDisplayRegion
+ _OBJC_METACLASS_$_AVCaptureAncillaryDataEncoder
+ _OBJC_METACLASS_$_AVCaptureDeviceStateCoordinatorUtilities
+ _OBJC_METACLASS_$_AVCaptureDeviceStateDescriptor
+ _OBJC_METACLASS_$_AVCaptureFaceIDBracketConfiguration
+ _OBJC_METACLASS_$_AVCaptureFaceIDBracketEncryptionConfiguration
+ _OBJC_METACLASS_$_AVCaptureFaceIDConfiguration
+ _OBJC_METACLASS_$_AVCaptureFaceIDUnwrapResult
+ _OBJC_METACLASS_$_AVCaptureMovieFileOutputAssetWriterInputHelper
+ _OBJC_METACLASS_$_AVCapturePersonalPhotographerDuplicateInfo
+ _OBJC_METACLASS_$_AVCapturePersonalPhotographerMetadata
+ _OBJC_METACLASS_$_AVCapturePersonalPhotographerSessionFinishCoordinator
+ _OBJC_METACLASS_$_AVCapturePersonalPhotographerSessionResults
+ _OBJC_METACLASS_$_AVCaptureSecureVideoDataOutput
+ _OBJC_METACLASS_$_AVCaptureTextureStyle
+ _OBJC_METACLASS_$_AVMetadataCinematicVideoMetadataObject
+ _OBJC_METACLASS_$_AVMetadataFaceIDFrameProxy
+ _OBJC_METACLASS_$_AVMetadataFaceIDObject
+ _OBJC_METACLASS_$_AVMetadataFocusTrackedObject
+ _OUTLINED_FUNCTION_128
+ _V63
+ _V64_V64s
+ _V68
+ __OBJC_$_CLASS_METHODS_AVCaptureDevice(SecureSigning_Private|AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification|DynamicAspectRatio|OutputAspectRatio_SPI|CameraLensSmudgeDetection|SmartFramingMonitoringInternal|ActiveOmahaConstituentDeviceType|PrimaryDisplayRegion|DeviceAngle|EmbeddedDisplay)
+ __OBJC_$_CLASS_METHODS_AVCaptureDeviceStateDescriptor
+ __OBJC_$_CLASS_METHODS_AVCapturePersonalPhotographerDuplicateInfo
+ __OBJC_$_CLASS_METHODS_AVCapturePersonalPhotographerMetadata
+ __OBJC_$_CLASS_METHODS_AVCapturePersonalPhotographerSessionFinishCoordinator
+ __OBJC_$_CLASS_METHODS_AVCapturePersonalPhotographerSessionResults
+ __OBJC_$_CLASS_METHODS_AVCaptureSecureVideoDataOutput
+ __OBJC_$_CLASS_METHODS_AVCaptureTextureStyle
+ __OBJC_$_CLASS_METHODS_AVMetadataCinematicVideoMetadataObject
+ __OBJC_$_CLASS_METHODS_AVMetadataFaceIDObject
+ __OBJC_$_CLASS_METHODS_AVMetadataFocusTrackedObject
+ __OBJC_$_CLASS_PROP_LIST_AVCapturePersonalPhotographerDuplicateInfo
+ __OBJC_$_CLASS_PROP_LIST_AVCapturePersonalPhotographerMetadata
+ __OBJC_$_CLASS_PROP_LIST_AVMetadataCinematicVideoMetadataObject
+ __OBJC_$_INSTANCE_METHODS_AVCaptureAncillaryDataEncoder
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDevice(SecureSigning_Private|AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification|DynamicAspectRatio|OutputAspectRatio_SPI|CameraLensSmudgeDetection|SmartFramingMonitoringInternal|ActiveOmahaConstituentDeviceType|PrimaryDisplayRegion|DeviceAngle|EmbeddedDisplay)
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDeviceStateCoordinatorUtilities
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDeviceStateDescriptor
+ __OBJC_$_INSTANCE_METHODS_AVCaptureFaceIDBracketConfiguration
+ __OBJC_$_INSTANCE_METHODS_AVCaptureFaceIDBracketEncryptionConfiguration
+ __OBJC_$_INSTANCE_METHODS_AVCaptureFaceIDConfiguration
+ __OBJC_$_INSTANCE_METHODS_AVCaptureFaceIDUnwrapResult
+ __OBJC_$_INSTANCE_METHODS_AVCaptureMovieFileOutputAssetWriterInputHelper
+ __OBJC_$_INSTANCE_METHODS_AVCapturePersonalPhotographerDuplicateInfo
+ __OBJC_$_INSTANCE_METHODS_AVCapturePersonalPhotographerMetadata
+ __OBJC_$_INSTANCE_METHODS_AVCapturePersonalPhotographerSessionFinishCoordinator
+ __OBJC_$_INSTANCE_METHODS_AVCapturePersonalPhotographerSessionResults
+ __OBJC_$_INSTANCE_METHODS_AVCaptureSecureVideoDataOutput
+ __OBJC_$_INSTANCE_METHODS_AVCaptureTextureStyle
+ __OBJC_$_INSTANCE_METHODS_AVMetadataCinematicVideoMetadataObject
+ __OBJC_$_INSTANCE_METHODS_AVMetadataFaceIDFrameProxy
+ __OBJC_$_INSTANCE_METHODS_AVMetadataFaceIDObject
+ __OBJC_$_INSTANCE_METHODS_AVMetadataFocusTrackedObject
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureAncillaryDataEncoder
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureDeviceStateCoordinatorUtilities
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureDeviceStateDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureFaceIDBracketConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureFaceIDBracketEncryptionConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureFaceIDConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureFaceIDUnwrapResult
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureMovieFileOutputAssetWriterInputHelper
+ __OBJC_$_INSTANCE_VARIABLES_AVCapturePersonalPhotographerDuplicateInfo
+ __OBJC_$_INSTANCE_VARIABLES_AVCapturePersonalPhotographerMetadata
+ __OBJC_$_INSTANCE_VARIABLES_AVCapturePersonalPhotographerSessionFinishCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_AVCapturePersonalPhotographerSessionResults
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureSecureVideoDataOutput
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureTextureStyle
+ __OBJC_$_INSTANCE_VARIABLES_AVMetadataCinematicVideoMetadataObject
+ __OBJC_$_INSTANCE_VARIABLES_AVMetadataFaceIDFrameProxy
+ __OBJC_$_INSTANCE_VARIABLES_AVMetadataFaceIDObject
+ __OBJC_$_PROP_LIST_AVCaptureAncillaryDataEncoder
+ __OBJC_$_PROP_LIST_AVCaptureDeviceStateDescriptor
+ __OBJC_$_PROP_LIST_AVCaptureFaceIDBracketConfiguration
+ __OBJC_$_PROP_LIST_AVCaptureFaceIDBracketEncryptionConfiguration
+ __OBJC_$_PROP_LIST_AVCaptureFaceIDConfiguration
+ __OBJC_$_PROP_LIST_AVCaptureFaceIDUnwrapResult
+ __OBJC_$_PROP_LIST_AVCapturePersonalPhotographerDuplicateInfo
+ __OBJC_$_PROP_LIST_AVCapturePersonalPhotographerMetadata
+ __OBJC_$_PROP_LIST_AVCapturePersonalPhotographerSessionResults
+ __OBJC_$_PROP_LIST_AVCaptureSecureVideoDataOutput
+ __OBJC_$_PROP_LIST_AVCaptureTextureStyle
+ __OBJC_$_PROP_LIST_AVMetadataCinematicVideoMetadataObject
+ __OBJC_$_PROP_LIST_AVMetadataFaceIDFrameProxy
+ __OBJC_$_PROP_LIST_AVMetadataFaceIDObject
+ __OBJC_CLASS_PROTOCOLS_$_AVCaptureFaceIDBracketConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_AVCaptureFaceIDBracketEncryptionConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_AVCaptureFaceIDConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_AVCapturePersonalPhotographerDuplicateInfo
+ __OBJC_CLASS_PROTOCOLS_$_AVCapturePersonalPhotographerMetadata
+ __OBJC_CLASS_PROTOCOLS_$_AVCaptureSecureVideoDataOutput
+ __OBJC_CLASS_PROTOCOLS_$_AVMetadataCinematicVideoMetadataObject
+ __OBJC_CLASS_PROTOCOLS_$_AVMetadataFaceIDObject
+ __OBJC_CLASS_PROTOCOLS_$_AVMetadataFocusTrackedObject
+ __OBJC_CLASS_RO_$_AVCaptureAncillaryDataEncoder
+ __OBJC_CLASS_RO_$_AVCaptureDeviceStateCoordinatorUtilities
+ __OBJC_CLASS_RO_$_AVCaptureDeviceStateDescriptor
+ __OBJC_CLASS_RO_$_AVCaptureFaceIDBracketConfiguration
+ __OBJC_CLASS_RO_$_AVCaptureFaceIDBracketEncryptionConfiguration
+ __OBJC_CLASS_RO_$_AVCaptureFaceIDConfiguration
+ __OBJC_CLASS_RO_$_AVCaptureFaceIDUnwrapResult
+ __OBJC_CLASS_RO_$_AVCaptureMovieFileOutputAssetWriterInputHelper
+ __OBJC_CLASS_RO_$_AVCapturePersonalPhotographerDuplicateInfo
+ __OBJC_CLASS_RO_$_AVCapturePersonalPhotographerMetadata
+ __OBJC_CLASS_RO_$_AVCapturePersonalPhotographerSessionFinishCoordinator
+ __OBJC_CLASS_RO_$_AVCapturePersonalPhotographerSessionResults
+ __OBJC_CLASS_RO_$_AVCaptureSecureVideoDataOutput
+ __OBJC_CLASS_RO_$_AVCaptureTextureStyle
+ __OBJC_CLASS_RO_$_AVMetadataCinematicVideoMetadataObject
+ __OBJC_CLASS_RO_$_AVMetadataFaceIDFrameProxy
+ __OBJC_CLASS_RO_$_AVMetadataFaceIDObject
+ __OBJC_CLASS_RO_$_AVMetadataFocusTrackedObject
+ __OBJC_METACLASS_RO_$_AVCaptureAncillaryDataEncoder
+ __OBJC_METACLASS_RO_$_AVCaptureDeviceStateCoordinatorUtilities
+ __OBJC_METACLASS_RO_$_AVCaptureDeviceStateDescriptor
+ __OBJC_METACLASS_RO_$_AVCaptureFaceIDBracketConfiguration
+ __OBJC_METACLASS_RO_$_AVCaptureFaceIDBracketEncryptionConfiguration
+ __OBJC_METACLASS_RO_$_AVCaptureFaceIDConfiguration
+ __OBJC_METACLASS_RO_$_AVCaptureFaceIDUnwrapResult
+ __OBJC_METACLASS_RO_$_AVCaptureMovieFileOutputAssetWriterInputHelper
+ __OBJC_METACLASS_RO_$_AVCapturePersonalPhotographerDuplicateInfo
+ __OBJC_METACLASS_RO_$_AVCapturePersonalPhotographerMetadata
+ __OBJC_METACLASS_RO_$_AVCapturePersonalPhotographerSessionFinishCoordinator
+ __OBJC_METACLASS_RO_$_AVCapturePersonalPhotographerSessionResults
+ __OBJC_METACLASS_RO_$_AVCaptureSecureVideoDataOutput
+ __OBJC_METACLASS_RO_$_AVCaptureTextureStyle
+ __OBJC_METACLASS_RO_$_AVMetadataCinematicVideoMetadataObject
+ __OBJC_METACLASS_RO_$_AVMetadataFaceIDFrameProxy
+ __OBJC_METACLASS_RO_$_AVMetadataFaceIDObject
+ __OBJC_METACLASS_RO_$_AVMetadataFocusTrackedObject
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_27
+ ___104-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForWrapper:withPayload:demoof:addMetadata:]_block_invoke_2
+ ___108-[AVCaptureFigVideoDevice _setExposureModeCustomWithLensAperture:duration:ISO:entryPoint:completionHandler:]_block_invoke
+ ___108-[AVCaptureFigVideoDevice _setExposureModeCustomWithLensAperture:duration:ISO:entryPoint:completionHandler:]_block_invoke_2
+ ___108-[AVCaptureFigVideoDevice _setExposureModeCustomWithLensAperture:duration:ISO:entryPoint:completionHandler:]_block_invoke_3
+ ___109-[AVCapturePhotoOutput _dispatchPersonalPhotographerSessionDidFinishCallbackForRequest:error:cleanupRequest:]_block_invoke
+ ___144+[AVCaptureMovieFileOutput _makeTimelapseMovieFromTimewarpTimelapseClassicIntermediateMovie:timelapseMovie:timelapseDestinationFrameRate:error:]_block_invoke
+ ___144+[AVCaptureMovieFileOutput _makeTimelapseMovieFromTimewarpTimelapseClassicIntermediateMovie:timelapseMovie:timelapseDestinationFrameRate:error:]_block_invoke_2
+ ___38-[AVCaptureFigVideoDevice deviceAngle]_block_invoke
+ ___39-[AVCaptureFigVideoDevice lensAperture]_block_invoke
+ ___43+[AVCaptureDevice publicExposureSignalsSet]_block_invoke
+ ___44-[AVCaptureFigVideoDevice startFaceIDUnwrap]_block_invoke
+ ___45-[AVCaptureFigVideoDevice faceIDUnwrapResult]_block_invoke
+ ___47-[AVCaptureFigVideoDevice primaryDisplayRegion]_block_invoke
+ ___48-[AVCaptureFigVideoDevice activeExposureSignals]_block_invoke
+ ___49-[AVCaptureFigVideoDevice _handleOccludedChange:]_block_invoke
+ ___49-[AVCaptureFigVideoDevice enabledExposureSignals]_block_invoke
+ ___51-[AVCaptureFigVideoDevice isLowCurrentTorchEnabled]_block_invoke
+ ___51-[AVCaptureFigVideoDevice supportedExposureSignals]_block_invoke
+ ___52-[AVCaptureSecureVideoDataOutput _updateLocalQueue:]_block_invoke
+ ___53-[AVCaptureFigVideoDevice _handleDeviceAngleChanged:]_block_invoke
+ ___53-[AVCaptureFigVideoDevice isFaceIDCoexistenceEnabled]_block_invoke
+ ___53-[AVCaptureFigVideoDevice setEnabledExposureSignals:]_block_invoke
+ ___53-[AVCaptureFigVideoDevice setLowCurrentTorchEnabled:]_block_invoke
+ ___53-[AVCaptureSecureVideoDataOutput _updateRemoteQueue:]_block_invoke
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_44
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_45
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_46
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_47
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_48
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_49
+ ___55-[AVCaptureFigVideoDevice setFaceIDCoexistenceEnabled:]_block_invoke
+ ___55-[AVCapturePhotoOutput stopPersonalPhotographerSession]_block_invoke
+ ___59-[AVCaptureFigVideoDevice activeOmahaConstituentDeviceType]_block_invoke
+ ___60-[AVCaptureBroadcastVideoOutput sendAncillaryUserDataToCCD:]_block_invoke
+ ___62-[AVCaptureFigVideoDevice _disableContinuousAutoFocusTracking]_block_invoke
+ ___62-[AVCaptureFigVideoDevice _disableContinuousAutoFocusTracking]_block_invoke_2
+ ___62-[AVCaptureFigVideoDevice _handlePrimaryDisplayRegionChanged:]_block_invoke
+ ___62-[AVCaptureFigVideoDevice _handlePrimaryDisplayRegionChanged:]_block_invoke_2
+ ___62-[AVCaptureFigVideoDevice automaticallyEnablesExposureSignals]_block_invoke
+ ___63-[AVCaptureFigVideoDevice isContinuousAutoFocusTrackingEnabled]_block_invoke
+ ___65-[AVCaptureFigVideoDevice releaseFaceIDFrameProxyWithIdentifier:]_block_invoke
+ ___65-[AVCaptureFigVideoDevice setContinuousAutoFocusTrackingEnabled:]_block_invoke
+ ___65-[AVCaptureFigVideoDevice setContinuousAutoFocusTrackingEnabled:]_block_invoke_2
+ ___65-[AVCaptureMetadataOutput captureFaceIDBracketWithConfiguration:]_block_invoke
+ ___65-[AVCapturePhotoOutput initiateManualPersonalPhotographerCapture]_block_invoke
+ ___66-[AVCaptureFigVideoDevice setAutomaticallyEnablesExposureSignals:]_block_invoke
+ ___69-[AVCaptureFigVideoDevice personalPhotographerSubjectDetectionStatus]_block_invoke
+ ___70-[AVCaptureFigVideoDevice continuousAutoFocusTrackingLensPositionBias]_block_invoke
+ ___71-[AVCaptureFigVideoDevice isContinuousAutoFocusTrackingSubjectAcquired]_block_invoke
+ ___74-[AVCaptureFigVideoDevice setContinuousAutoFocusTrackingLensPositionBias:]_block_invoke
+ ___78-[AVCapturePhotoOutput startPersonalPhotographerSessionWithSettings:delegate:]_block_invoke
+ ___83-[AVCapturePersonalPhotographerSessionFinishCoordinator initWithCompletionHandler:]_block_invoke
+ ___96-[AVCaptureVideoDataOutput recommendedMovieMetadataForVideoCodecType:assetWriterOutputFileType:]_block_invoke_2
+ ____sharedCinematicVideoMetadataSampleGenerator_block_invoke
+ ___block_descriptor_252_e8_32o40o48o56o64o72o80o88o96o104o112o120r_e51_v16?0"<AVCaptureDeferredPhotoProcessorDelegate>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8r120l8s112l8
+ ___block_descriptor_40_e8_32o_e43_v24?0"AVCapturePhotoRequest"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32o40r_e29_v24?0"NSArray"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32o40r_e34_v16?0^{OpaqueFigCaptureSession=}8lr40l8s32l8
+ ___block_descriptor_521_e8_32o40o48o56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r296r304r312r320r328r336r344r352r360r368r376r384r392r400r408r416r424r432r440r448r456r464r472r480r488r496r504r512r_e5_v8?0ls32l8s40l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8s48l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8r280l8r288l8r296l8r304l8r312l8r320l8r328l8r336l8r344l8r352l8r360l8r368l8r376l8r384l8r392l8r400l8r408l8r416l8r424l8r432l8r440l8r448l8r456l8r464l8r472l8r480l8r488l8r496l8r504l8r512l8
+ ___block_descriptor_53_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_60_e8_32o40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_64_e8_32o40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_72_e8_32o40o48o56o_e8_v16?08ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32o40o48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_86_e8_32o40o48o56o64o_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32o40r48r56r64r72r80r_e5_v8?0lr40l8r48l8s32l8r56l8r64l8r72l8r80l8
+ ___block_descriptor_88_e8_32o40r48r56r64r72r_e5_v8?0lr40l8s32l8r48l8r56l8r64l8r72l8
+ ___block_descriptor_89_e8_32o40r48r56r64r72r80r_e5_v8?0lr40l8r48l8s32l8r56l8r64l8r72l8r80l8
+ ___block_descriptor_96_e8_32o40o48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_96_e8_32o40o48r_e5_v8?0lr48l8s32l8s40l8
+ __sharedCinematicVideoMetadataSampleGenerator.sGenerator
+ __sharedCinematicVideoMetadataSampleGenerator.sOnceToken
+ _abort
+ _kCMFormatDescriptionExtension_BytesPerRow
+ _kCMMetadataBaseDataType_UInt64
+ _kCMMetadataFormatDescriptionMetadataSpecificationKey_StructuralDependency
+ _kCMMetadataFormatDescription_StructuralDependencyKey_DependencyIsInvalidFlag
+ _kCMMetadataIdentifier_QuickTimeMetadataSceneIlluminance
+ _kCMSampleAttachmentKey_DependsOnOthers
+ _kCMSampleAttachmentKey_EarlierDisplayTimesAllowed
+ _kCMSampleAttachmentKey_HasRedundantCoding
+ _kCMSampleAttachmentKey_IsDependedOnByOthers
+ _kCMSampleAttachmentKey_NotSync
+ _kCMSampleAttachmentKey_PartialSync
+ _kCVImageBufferColorPrimariesKey
+ _kCVImageBufferYCbCrMatrixKey
+ _kFigCaptureDeferredPhotoProcessorNotificationPayloadKey_SecureSignedRawSurface
+ _kFigCaptureDeferredPhotoProcessorNotificationPayloadKey_SecureSignedRawSurfaceSize
+ _kFigCapturePersonalPhotographerDuplicateInfoKey_OriginalPresentationTimestamp
+ _kFigCapturePersonalPhotographerDuplicateInfoKey_ReplacedPhotoTimestamp
+ _kFigCapturePersonalPhotographerDuplicateInfoKey_SettingsID
+ _kFigCapturePersonalPhotographerKey_DetectedContext
+ _kFigCapturePersonalPhotographerKey_DuplicateInfo
+ _kFigCapturePersonalPhotographerKey_FrameID
+ _kFigCapturePersonalPhotographerKey_FrameScore
+ _kFigCapturePersonalPhotographerKey_ManualCapture
+ _kFigCapturePersonalPhotographerKey_SessionID
+ _kFigCapturePortType_RenoFrontFacingSuperWideCamera
+ _kFigCaptureSampleBufferAttachmentKey_FaceID
+ _kFigCaptureSampleBufferAttachmentKey_FocusTrackedObjectInfo
+ _kFigCaptureSegmentFocusTrackingFocusTrackedObjectMetadata_Mask
+ _kFigCaptureSessionBroadcastVideoSinkProperty_AncillaryData
+ _kFigCaptureSessionDidFinishPersonalPhotographerSessionPayloadKey_CapturesToKeep
+ _kFigCaptureSessionDidFinishPersonalPhotographerSessionPayloadKey_CapturesToRemove
+ _kFigCaptureSessionDidFinishRecordingIrisMovieNotificationPayloadKey_OutputFilePath
+ _kFigCaptureSessionDidRecordIrisMovieNotificationPayloadKey_OutputFilePath
+ _kFigCaptureSessionIrisStillImageSinkNotification_DidFinishPersonalPhotographerSession
+ _kFigCaptureSessionNotificationPayloadKey_SecureSignedRawSurface
+ _kFigCaptureSessionNotificationPayloadKey_SecureSignedRawSurfaceSize
+ _kFigCaptureSessionNotificationPayloadKey_TimewarpTimelapseClassicIntermediateFilePath
+ _kFigCaptureSessionProperty_TextureStyle
+ _kFigCaptureSessionVideoDataSinkProperty_CinematicVideoMetadataCaptureEnabled
+ _kFigCaptureSessionWillBeginCaptureNotificationPayloadKey_SecureSigningPhotoCaptureEnabled
+ _kFigCaptureSourceExposureOperationKey_LensAperture
+ _kFigCaptureSourceFaceIDUnwrapStatusChangedPayloadKey_PearlSecureSessionError
+ _kFigCaptureSourceFaceIDUnwrapStatusChangedPayloadKey_Status
+ _kFigCaptureSourceFaceIDUnwrapStatusChangedPayloadKey_StreamError
+ _kFigCaptureSourceFocusOperationKey_Tracking
+ _kFigCaptureSourceFocusOperationKey_TrackingLensPositionBias
+ _kFigCaptureSourceFocusOperationKey_TrackingSeedingPoint
+ _kFigCaptureSourceNotification_ContinuousAutoFocusTrackingSubjectAcquiredChanged
+ _kFigCaptureSourceNotification_FaceIDUnwrapStatusChanged
+ _kFigCaptureSourceNotification_PersonalPhotographerSubjectDetectionStatusChanged
+ _kFigCaptureSourcePersonalPhotographerSubjectDetectionStatusChangedPayloadKey_Status
+ _kFigCaptureSourcePropertyBravoCameraSelectionConfigurationKey_LockedDeviceType
+ _kFigCaptureSourceProperty_ActiveExposureSignals
+ _kFigCaptureSourceProperty_AutoExposureLensApertureRateLimit
+ _kFigCaptureSourceProperty_AutomaticallyIgnoresExposureSignals
+ _kFigCaptureSourceProperty_DeviceAngle
+ _kFigCaptureSourceProperty_IgnoredExposureSignals
+ _kFigCaptureSourceProperty_LensAperture
+ _kFigCaptureSourceProperty_LowCurrentTorchEnabled
+ _kFigCaptureSourceProperty_Occluded
+ _kFigCaptureSourceProperty_PrimaryDisplayRegion
+ _kFigCaptureSourceProperty_SecureSigningPhotoCaptureEnabled
+ _kFigCaptureSourceProperty_SupportedExposureSignals
+ _kFigCaptureStreamAEApertureIgnorableSignals
+ _kFigCaptureStreamCaptureSecureFaceIDBracketKey_ColorBracketEncryption
+ _kFigCaptureStreamCaptureSecureFaceIDBracketKey_DoubleOrder
+ _kFigCaptureStreamCaptureSecureFaceIDBracketKey_InfraredBracketEncryption
+ _kFigCaptureStreamCaptureSecureFaceIDBracketKey_NumberOfDoubles
+ _kFigCaptureStreamCaptureSecureFaceIDBracketKey_ProbePatternIndex
+ _kFigCaptureStreamCaptureSecureFaceIDBracketKey_ProbePatternType
+ _kFigCaptureStreamFaceIDBracketEncryptionKey_HostMainKeyIndex
+ _kFigCaptureStreamFaceIDBracketEncryptionKey_InitializationVector
+ _kFigCaptureStreamFaceIDBracketEncryptionKey_LinearFeedbackShiftRegisterSeed
+ _kFigCaptureStreamFaceIDBracketEncryptionKey_Nonce
+ _kFigCaptureStreamSecureFaceIDConfigurationKey_AttentionRequired
+ _kFigCaptureStreamSecureFaceIDConfigurationKey_FrameLogEnabled
+ _kFigCaptureStreamSecureFaceIDConfigurationKey_FrameMetadataEnabled
+ _kFigCaptureStreamSecureFaceIDConfigurationKey_Mode
+ _kFigCaptureStreamSecureFaceIDConfigurationKey_PeriocularEnabled
+ _kFigCaptureStreamSecureFaceIDConfigurationKey_RetryType
+ _kFigCaptureStreamSecureFaceIDFrameProxyKey_FrameHeight
+ _kFigCaptureStreamSecureFaceIDFrameProxyKey_FrameIdentifier
+ _kFigCaptureStreamSecureFaceIDFrameProxyKey_FrameWidth
+ _kFigCaptureStreamSecureFaceIDFrameProxyKey_PixelFormat
+ _kFigCaptureStreamSecureFaceIDFrameProxyKey_SharedMemoryAreaOffset
+ _kFigCaptureStreamSecureFaceIDFrameProxyKey_Stride
+ _kFigCaptureStreamSecureFaceIDKey_BracketProbePatternType
+ _kFigCaptureStreamSecureFaceIDKey_CoachingStatus
+ _kFigCaptureStreamSecureFaceIDKey_ContextIndex
+ _kFigCaptureStreamSecureFaceIDKey_FrameType
+ _kFigCaptureStreamSecureFaceIDKey_MetadataFrameProxy
+ _kFigCaptureStreamSecureFaceIDKey_ProjectornMode
+ _kFigCaptureStreamSecureFaceIDKey_RawFrameProxy
+ _kFigCaptureStreamSecureFaceIDKey_Ready
+ _kFigCaptureStreamSecureFaceIDKey_ReferenceFrameProxy
+ _kFigMetadataIdentifier_QuickTimeMetadataCinematicVideoMetadata
+ _kFigMetadataIdentifier_QuickTimeMetadataFaceID
+ _kFigMetadataIdentifier_QuickTimeMetadataFocusTrackedObject
+ _kFigPersonalPhotographerMetadata_Version
+ _kFigQuicktimeMetadataKey_TimewarpCaptureMode
+ _kFigQuicktimeMetadataKey_TimewarpTimelapseFastDecimationAllowed
+ _kFigQuicktimeMetadataKey_TimewarpTimelapseMaxDecimationLevel
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_addExpectedTimestamp:
+ _objc_msgSend$_checkCustomExposureModeWithLensAperture:duration:ISO:entryPoint:
+ _objc_msgSend$_configureCinematicVideoMetadataIfNeededForSessionConfiguration:
+ _objc_msgSend$_copyPersonalPhotographerSessionPhotoRequestWithUniqueID:
+ _objc_msgSend$_customExposureIsFullyLocked
+ _objc_msgSend$_disableContinuousAutoFocusTracking
+ _objc_msgSend$_dispatchPersonalPhotographerSessionDidFinishCallbackForRequest:error:cleanupRequest:
+ _objc_msgSend$_dispatchPersonalPhotographerSessionDidFinishWithFailureCallbackForPhotoSettings:figSettings:toDelegate:withError:
+ _objc_msgSend$_exposesOmahaConstituentDevices
+ _objc_msgSend$_getTextureStyleSupported:
+ _objc_msgSend$_handleDeviceAngleChanged:
+ _objc_msgSend$_handleDidFinishPersonalPhotographerSessionNotificationWithPayload:forRequest:
+ _objc_msgSend$_handleOccludedChange:
+ _objc_msgSend$_handlePrimaryDisplayRegionChanged:
+ _objc_msgSend$_handleVideoStabilizationStrengthChangedForDevice:
+ _objc_msgSend$_handleWatchdogTimeout
+ _objc_msgSend$_initWithDeviceType:mediaTypes:position:uniqueID:localizedName:
+ _objc_msgSend$_initWithPreset:intensity:grain:
+ _objc_msgSend$_initWithSmartStyle:textureStyle:
+ _objc_msgSend$_initWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:
+ _objc_msgSend$_invokeCompletionWithRequest:error:
+ _objc_msgSend$_isActionCameraEnabled
+ _objc_msgSend$_isPhotoRegisteredWithTimestampNSValue:
+ _objc_msgSend$_lowLightVideoNoiseReductionANEAndGPUCost
+ _objc_msgSend$_makeTimelapseMovieFromTimewarpTimelapseClassicIntermediateMovie:timelapseMovie:timelapseDestinationFrameRate:error:
+ _objc_msgSend$_personalPhotographerSessionPhotoRequestForUniqueID:
+ _objc_msgSend$_queryPrimaryDisplayRegion
+ _objc_msgSend$_setExposureModeCustomWithLensAperture:duration:ISO:entryPoint:completionHandler:
+ _objc_msgSend$_setExposureWithMode:duration:ISO:lensAperture:requestID:newMaxFrameDuration:
+ _objc_msgSend$_setLowLightVideoNoiseReductionEnabled:
+ _objc_msgSend$_setTextureStyleSetByClient:
+ _objc_msgSend$_shouldInvertBackCameraRotationForDeviceAngle
+ _objc_msgSend$_shouldInvokeCompletionCopyOutRequest:copyOutError:
+ _objc_msgSend$_systemReferenceAngleForDeviceOrientation:onDisplayRegion:
+ _objc_msgSend$_updateCinematicVideoMetadataCaptureSupportedForSourceDevice:
+ _objc_msgSend$_updateLowLightVideoNoiseReductionEnabledForAllConnections
+ _objc_msgSend$_updateLowLightVideoNoiseReductionSupported
+ _objc_msgSend$_updatePersonalPhotographerSupportedForDevice:
+ _objc_msgSend$_updatePrimaryDisplayRegionIfNeeded
+ _objc_msgSend$_updateSecureSigningPhotoCaptureSupportedForSourceDevice:
+ _objc_msgSend$_validateCinematicVideoMetadataConfiguration:
+ _objc_msgSend$_validateFaceIDConfiguration:
+ _objc_msgSend$activeOmahaConstituentDeviceType
+ _objc_msgSend$addInput:
+ _objc_msgSend$addOutput:
+ _objc_msgSend$addTrackAssociationWithTrackOfInput:type:
+ _objc_msgSend$alwaysDiscardsLateSecureVideoFrames
+ _objc_msgSend$appendPixelBuffer:withPresentationTime:
+ _objc_msgSend$appendSampleBuffer:
+ _objc_msgSend$appendTimedMetadataGroup:
+ _objc_msgSend$assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput:
+ _objc_msgSend$automaticallyAdjustsCinematicVideoMetadataCaptureEnabled
+ _objc_msgSend$automaticallyEnablesExposureSignals
+ _objc_msgSend$automaticallyEnablesLowLightVideoNoiseReduction
+ _objc_msgSend$bracketProbePatternType
+ _objc_msgSend$cameraStreamError
+ _objc_msgSend$canAddInput:
+ _objc_msgSend$canAddOutput:
+ _objc_msgSend$canAddTrackAssociationWithTrackOfInput:type:
+ _objc_msgSend$canSetDataForTag:
+ _objc_msgSend$canSetStringForTag:
+ _objc_msgSend$cancel
+ _objc_msgSend$cancelReading
+ _objc_msgSend$captureOutput:didFinishPersonalPhotographerSessionWithResults:error:
+ _objc_msgSend$captureOutput:willFinishRecordingTimelapseToOutputFileAtURL:previewSurface:previewSurfaceSize:fromConnections:error:
+ _objc_msgSend$cinematicVideoMetadataCaptureEnabledByClient
+ _objc_msgSend$cinematicVideoMetadataObjectWithPayload:input:time:
+ _objc_msgSend$colorBracketEncryptionConfiguration
+ _objc_msgSend$contextIndex
+ _objc_msgSend$continuousAutoFocusTrackingLensPositionBias
+ _objc_msgSend$copyForPersonalPhotographerWithSettingsID:rotationDegrees:mirrored:
+ _objc_msgSend$copyNextSampleBuffer
+ _objc_msgSend$dataUsingEncoding:
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$defaultLensAperture
+ _objc_msgSend$descriptorForDevice:
+ _objc_msgSend$deviceAngle
+ _objc_msgSend$dictionaryWithObject:forKey:
+ _objc_msgSend$dimLayerWithAnimationDuration:undimOnNextFirstPreviewFrame:
+ _objc_msgSend$doubleOrder
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$encodeInt64:forKey:
+ _objc_msgSend$endSessionAtSourceTime:
+ _objc_msgSend$ensureWriterInputIsReadyForMoreMediaData
+ _objc_msgSend$estimatedDataRate
+ _objc_msgSend$exposureSignalsBitmaskForSet:
+ _objc_msgSend$exposureSignalsSetForBitmask:includingInternal:
+ _objc_msgSend$faceIDBracketConfigurationDictionary
+ _objc_msgSend$faceIDBracketEncryptionConfigurationDictionary
+ _objc_msgSend$faceIDCoexistenceSupported
+ _objc_msgSend$faceIDConfiguration
+ _objc_msgSend$faceIDConfigurationDictionary
+ _objc_msgSend$faceIDObjectWithFaceIDResultDictionary:metadataDictionary:input:time:
+ _objc_msgSend$faceIDUnwrapSupported
+ _objc_msgSend$figSettings
+ _objc_msgSend$finishWithRequest:expectedTimestamps:error:
+ _objc_msgSend$finishWritingWithCompletionHandler:
+ _objc_msgSend$focusTrackedObjectWithObjectID:mask:bounds:input:time:
+ _objc_msgSend$formatDescriptions
+ _objc_msgSend$frameIdentifier
+ _objc_msgSend$frameType
+ _objc_msgSend$grain
+ _objc_msgSend$handleVideoStabilizationStrengthChangedForDevice:
+ _objc_msgSend$hasDirectoryPath
+ _objc_msgSend$hostMainKeyIndex
+ _objc_msgSend$incrementUniqueIDToValue:
+ _objc_msgSend$infraredBracketEncryptionConfiguration
+ _objc_msgSend$initWithAsset:error:
+ _objc_msgSend$initWithAssetReaderTrackOutput:
+ _objc_msgSend$initWithAssetWriterInput:
+ _objc_msgSend$initWithAssetWriterInput:sourcePixelBufferAttributes:
+ _objc_msgSend$initWithAsssetWriterInput:
+ _objc_msgSend$initWithCaptureOutput:
+ _objc_msgSend$initWithCompletionHandler:
+ _objc_msgSend$initWithDuplicateInfoDictionary:
+ _objc_msgSend$initWithFaceIDResultDictionary:metadataDictionary:time:sourceCaptureInput:
+ _objc_msgSend$initWithFrameDictionary:sourceCaptureInput:
+ _objc_msgSend$initWithItems:timeRange:
+ _objc_msgSend$initWithMediaType:outputSettings:
+ _objc_msgSend$initWithMediaType:outputSettings:sourceFormatHint:
+ _objc_msgSend$initWithObjectID:mask:bounds:input:time:
+ _objc_msgSend$initWithPayload:input:time:
+ _objc_msgSend$initWithPersonalPhotographerMetadataDictionary:
+ _objc_msgSend$initWithPhotoSettingsUniqueID:
+ _objc_msgSend$initWithSampleBuffer:
+ _objc_msgSend$initWithTimeout:handler:
+ _objc_msgSend$initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:photoLibraryThumbnails:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:secureSignedRawSurface:secureSignedRawSurfaceSize:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:underlyingSourceDeviceType:sourceDeviceType:
+ _objc_msgSend$initWithTimestamp:proxySurface:proxySurfaceSize:proxyFileType:previewPhotoSurface:secureSignedRawSurface:secureSignedRawSurfaceSize:metadata:captureRequest:sequenceCount:photoCount:applicationIdentifier:captureRequestIdentifier:photoIdentifier:expectedPhotoProcessingFlags:underlyingSourceDeviceType:sourceDeviceType:
+ _objc_msgSend$initWithTrack:outputSettings:
+ _objc_msgSend$initWithURL:fileType:error:
+ _objc_msgSend$initWithURL:options:
+ _objc_msgSend$initWithUnwrapStatus:pearlSecureSessionError:streamError:
+ _objc_msgSend$initializationVector
+ _objc_msgSend$isAttentionRequired
+ _objc_msgSend$isAutoSecureSigningPhotoCaptureEnabled
+ _objc_msgSend$isCinematicMetadataCaptureSupported
+ _objc_msgSend$isCinematicVideoMetadataCaptureEnabled
+ _objc_msgSend$isCinematicVideoMetadataCaptureSupported
+ _objc_msgSend$isContinuousAutoFocusTrackingEnabled
+ _objc_msgSend$isContinuousAutoFocusTrackingSupported
+ _objc_msgSend$isFaceIDCoexistenceEnabled
+ _objc_msgSend$isFaceIDCoexistenceSupported
+ _objc_msgSend$isFrameLogEnabled
+ _objc_msgSend$isFrameMetadataEnabled
+ _objc_msgSend$isLowCurrentTorchSupported
+ _objc_msgSend$isLowLightVideoNoiseReductionEnabled
+ _objc_msgSend$isLowLightVideoNoiseReductionSupported
+ _objc_msgSend$isOmahaVariant
+ _objc_msgSend$isPeriocularEnabled
+ _objc_msgSend$isPersonalPhotographerEnabled
+ _objc_msgSend$isPersonalPhotographerSessionActive
+ _objc_msgSend$isPersonalPhotographerSupported
+ _objc_msgSend$isPhotoRegisteredForDeletionWithTimestamp:
+ _objc_msgSend$isPhotoRegisteredWithTimestamp:
+ _objc_msgSend$isPrimaryConstituentDeviceSwitchingBehaviorLockedWithDeviceSupported
+ _objc_msgSend$isReadyForMoreMediaData
+ _objc_msgSend$isSecureSigningPhotoCaptureSupportEnabled
+ _objc_msgSend$isSecureSigningPhotoCaptureSupported
+ _objc_msgSend$isTextureStyleSupported
+ _objc_msgSend$isTimewarpSupported
+ _objc_msgSend$lightSourceProjectorMode
+ _objc_msgSend$linearFeedbackShiftRegisterSeed
+ _objc_msgSend$loadTracksWithMediaType:completionHandler:
+ _objc_msgSend$lowCurrentTorchSupported
+ _objc_msgSend$mainDisplay
+ _objc_msgSend$mask
+ _objc_msgSend$maxAvailableVideoZoomFactor
+ _objc_msgSend$maxLensAperture
+ _objc_msgSend$mediaTypes
+ _objc_msgSend$mediaTypesForDevice:
+ _objc_msgSend$metadataFrameProxy
+ _objc_msgSend$metadataItem
+ _objc_msgSend$minAvailableVideoZoomFactor
+ _objc_msgSend$minLensAperture
+ _objc_msgSend$mode
+ _objc_msgSend$newTimedMetadataSampleBufferFromPayload:presentationTimeStamp:
+ _objc_msgSend$nextTimedMetadataGroup
+ _objc_msgSend$nonce
+ _objc_msgSend$numberOfDoubles
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$overCaptureGradientPercentInset
+ _objc_msgSend$pearlSecureSessionUnwrapError
+ _objc_msgSend$personalPhotographerCapture
+ _objc_msgSend$personalPhotographerCaptureRate
+ _objc_msgSend$photographicStyle
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$preferredTransform
+ _objc_msgSend$preset
+ _objc_msgSend$primaryConstituentDeviceSwitchingBehaviorLockedWithDeviceSupported
+ _objc_msgSend$primaryDisplayRegion
+ _objc_msgSend$probePatternIndex
+ _objc_msgSend$probePatternType
+ _objc_msgSend$rawFrameDeliveryEnabled
+ _objc_msgSend$rawFrameDeliverySupported
+ _objc_msgSend$rawFrameProxy
+ _objc_msgSend$recommendedLensApertures
+ _objc_msgSend$recordCaptureCompleteForSettingsID:
+ _objc_msgSend$recordStillCompleteForSettingsID:timestamp:
+ _objc_msgSend$referenceFrameProxy
+ _objc_msgSend$registerPhotoCapturedWithTimestamp:
+ _objc_msgSend$registerPhotoTimestampForDeletion:
+ _objc_msgSend$releaseFaceIDFrameProxyWithIdentifier:
+ _objc_msgSend$removeItemAtURL:error:
+ _objc_msgSend$reset
+ _objc_msgSend$resolvedSettingsWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:
+ _objc_msgSend$retryType
+ _objc_msgSend$sendUserDataEntryToCCD:value:
+ _objc_msgSend$setActiveOmahaConstituentDeviceType:
+ _objc_msgSend$setAlwaysCopiesSampleData:
+ _objc_msgSend$setAttentionRequired:
+ _objc_msgSend$setAutoSecureSigningPhotoCaptureEnabled:
+ _objc_msgSend$setCinematicVideoMetadataCaptureEnabled:
+ _objc_msgSend$setCinematicVideoMetadataCaptureEnabledByClient:
+ _objc_msgSend$setColorBracketEncryptionConfiguration:
+ _objc_msgSend$setDoubleOrder:
+ _objc_msgSend$setExposureModeCustomWithLensAperture:duration:ISO:completionHandler:
+ _objc_msgSend$setFaceIDCoexistenceEnabled:
+ _objc_msgSend$setFaceIDConfiguration:
+ _objc_msgSend$setFrameLogEnabled:
+ _objc_msgSend$setFrameMetadataEnabled:
+ _objc_msgSend$setHostMainKeyIndex:
+ _objc_msgSend$setInfraredBracketEncryptionConfiguration:
+ _objc_msgSend$setInitializationVector:
+ _objc_msgSend$setLinearFeedbackShiftRegisterSeed:
+ _objc_msgSend$setLowLightVideoNoiseReductionEnabled:
+ _objc_msgSend$setMask:
+ _objc_msgSend$setMetadataFrameProxy:
+ _objc_msgSend$setMode:
+ _objc_msgSend$setNonce:
+ _objc_msgSend$setNumberOfDoubles:
+ _objc_msgSend$setOverCaptureGradientPercentInset:
+ _objc_msgSend$setPeriocularEnabled:
+ _objc_msgSend$setPersonalPhotographerCapture:
+ _objc_msgSend$setPersonalPhotographerCaptureRate:
+ _objc_msgSend$setPersonalPhotographerEnabled:
+ _objc_msgSend$setPrimaryDisplayRegion:
+ _objc_msgSend$setProbePatternIndex:
+ _objc_msgSend$setProbePatternType:
+ _objc_msgSend$setRawFrameDeliveryEnabled:
+ _objc_msgSend$setRawFrameProxy:
+ _objc_msgSend$setRetryType:
+ _objc_msgSend$setSecureSigningPhotoCaptureEnabled:
+ _objc_msgSend$setSecureSigningPhotoCaptureSupportEnabled:
+ _objc_msgSend$setTextureStyle:
+ _objc_msgSend$setTextureStyleEnabled:
+ _objc_msgSend$setTimewarpDestinationFrameRate:
+ _objc_msgSend$setTimewarpEnabled:
+ _objc_msgSend$setTimewarpMode:
+ _objc_msgSend$setWithObjects:count:
+ _objc_msgSend$sizeForTag:
+ _objc_msgSend$startReading
+ _objc_msgSend$startSessionAtSourceTime:
+ _objc_msgSend$startWriting
+ _objc_msgSend$styleWithPreset:intensity:grain:
+ _objc_msgSend$styleWithSmartStyle:textureStyle:
+ _objc_msgSend$subdataWithRange:
+ _objc_msgSend$supportsExposureModeCustomWithLensAperture:duration:ISO:
+ _objc_msgSend$textureStyle
+ _objc_msgSend$textureStyleEnabled
+ _objc_msgSend$timewarpDestinationFrameRate
+ _objc_msgSend$timewarpMode
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$unwrapStatus
+ _objc_msgSend$userDefinedAncillaryDataSizeRemaining
+ _objc_retain_x1
+ _publicExposureSignalsSet.onceToken
+ _publicExposureSignalsSet.signals
+ _socvpl_camerasMountedInLandscapeOrientation
+ _svdo_notificationHandler
- +[AVCaptureResolvedPhotoSettings resolvedSettingsWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:]
- -[AVCaptureDeferredPhotoProxy initWithTimestamp:proxySurface:proxySurfaceSize:proxyFileType:previewPhotoSurface:metadata:captureRequest:sequenceCount:photoCount:applicationIdentifier:captureRequestIdentifier:photoIdentifier:expectedPhotoProcessingFlags:underlyingSourceDeviceType:sourceDeviceType:]
- -[AVCaptureDeviceFormat _checkCustomExposureModeWithDuration:ISO:entryPoint:]
- -[AVCaptureDeviceRotationCoordinator _systemReferenceAngleForDeviceOrientation:]
- -[AVCaptureFigVideoDevice _isCustomExposure]
- -[AVCaptureFigVideoDevice _setExposureWithMode:duration:ISO:requestID:newMaxFrameDuration:]
- -[AVCapturePhoto initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:photoLibraryThumbnails:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:underlyingSourceDeviceType:sourceDeviceType:]
- -[AVCapturePhotographicStyle _initWithSmartStyle:]
- -[AVCaptureResolvedPhotoSettings _initWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:]
- GCC_except_table109
- GCC_except_table110
- GCC_except_table132
- GCC_except_table143
- GCC_except_table146
- GCC_except_table158
- GCC_except_table162
- GCC_except_table164
- GCC_except_table171
- GCC_except_table172
- GCC_except_table173
- GCC_except_table175
- GCC_except_table176
- GCC_except_table183
- GCC_except_table184
- GCC_except_table186
- GCC_except_table190
- GCC_except_table192
- GCC_except_table194
- GCC_except_table197
- GCC_except_table203
- GCC_except_table209
- GCC_except_table210
- GCC_except_table212
- GCC_except_table216
- GCC_except_table221
- GCC_except_table223
- GCC_except_table226
- GCC_except_table249
- GCC_except_table254
- GCC_except_table263
- GCC_except_table269
- GCC_except_table278
- GCC_except_table284
- GCC_except_table290
- GCC_except_table295
- GCC_except_table298
- GCC_except_table316
- GCC_except_table317
- GCC_except_table320
- GCC_except_table323
- GCC_except_table324
- GCC_except_table327
- GCC_except_table330
- GCC_except_table332
- GCC_except_table340
- GCC_except_table343
- GCC_except_table349
- GCC_except_table379
- GCC_except_table390
- GCC_except_table392
- GCC_except_table419
- GCC_except_table442
- GCC_except_table452
- GCC_except_table479
- GCC_except_table482
- GCC_except_table508
- GCC_except_table512
- GCC_except_table520
- GCC_except_table523
- GCC_except_table531
- GCC_except_table539
- GCC_except_table545
- GCC_except_table55
- GCC_except_table550
- GCC_except_table564
- GCC_except_table574
- GCC_except_table588
- GCC_except_table611
- GCC_except_table622
- GCC_except_table632
- GCC_except_table646
- GCC_except_table656
- GCC_except_table668
- GCC_except_table687
- GCC_except_table711
- GCC_except_table738
- GCC_except_table740
- GCC_except_table742
- GCC_except_table767
- GCC_except_table779
- GCC_except_table781
- GCC_except_table783
- GCC_except_table789
- GCC_except_table791
- GCC_except_table834
- GCC_except_table838
- GCC_except_table895
- GCC_except_table897
- GCC_except_table899
- GCC_except_table901
- GCC_except_table93
- GCC_except_table94
- GCC_except_table947
- GCC_except_table953
- GCC_except_table96
- GCC_except_table961
- GCC_except_table97
- __OBJC_$_CLASS_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification|DynamicAspectRatio|OutputAspectRatio_SPI|CameraLensSmudgeDetection|SmartFramingMonitoringInternal|EmbeddedDisplay)
- __OBJC_$_INSTANCE_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification|DynamicAspectRatio|OutputAspectRatio_SPI|CameraLensSmudgeDetection|SmartFramingMonitoringInternal|EmbeddedDisplay)
- ___83-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke
- ___83-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke_2
- ___83-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke_3
- ___block_descriptor_236_e8_32o40o48o56o64o72o80o88o96o104o112o120r_e51_v16?0"<AVCaptureDeferredPhotoProcessorDelegate>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8r120l8s112l8
- ___block_descriptor_505_e8_32o40o48o56r64r72r80r88r96r104r112r120r128r136r144r152r160r168r176r184r192r200r208r216r224r232r240r248r256r264r272r280r288r296r304r312r320r328r336r344r352r360r368r376r384r392r400r408r416r424r432r440r448r456r464r472r480r488r496r_e5_v8?0ls32l8s40l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8r160l8r168l8r176l8r184l8r192l8r200l8s48l8r208l8r216l8r224l8r232l8r240l8r248l8r256l8r264l8r272l8r280l8r288l8r296l8r304l8r312l8r320l8r328l8r336l8r344l8r352l8r360l8r368l8r376l8r384l8r392l8r400l8r408l8r416l8r424l8r432l8r440l8r448l8r456l8r464l8r472l8r480l8r488l8r496l8
- ___block_descriptor_72_e8_32o40r48r56r_e5_v8?0lr40l8s32l8r48l8r56l8
- ___block_descriptor_80_e8_32o40r48r56r64r72r_e5_v8?0lr40l8r48l8s32l8r56l8r64l8r72l8
- ___block_descriptor_81_e8_32o40r48r56r64r72r_e5_v8?0lr40l8r48l8s32l8r56l8r64l8r72l8
- ___block_descriptor_92_e8_32o40o48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
- ___block_descriptor_92_e8_32o40o48r_e5_v8?0lr48l8s32l8s40l8
- _objc_msgSend$_checkCustomExposureModeWithDuration:ISO:entryPoint:
- _objc_msgSend$_initWithSmartStyle:
- _objc_msgSend$_initWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:
- _objc_msgSend$_isCustomExposure
- _objc_msgSend$_setExposureWithMode:duration:ISO:requestID:newMaxFrameDuration:
- _objc_msgSend$_systemReferenceAngleForDeviceOrientation:
- _objc_msgSend$initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:photoLibraryThumbnails:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:underlyingSourceDeviceType:sourceDeviceType:
- _objc_msgSend$initWithTimestamp:proxySurface:proxySurfaceSize:proxyFileType:previewPhotoSurface:metadata:captureRequest:sequenceCount:photoCount:applicationIdentifier:captureRequestIdentifier:photoIdentifier:expectedPhotoProcessingFlags:underlyingSourceDeviceType:sourceDeviceType:
- _objc_msgSend$resolvedSettingsWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:
- _objc_msgSend$setExposureModeCustomWithDuration:ISO:completionHandler:
- _objc_msgSend$styleWithSmartStyle:
- _swift_release_x9
CStrings:
+ " duplicateInfo:"
+ "%@ %@"
+ "( duplicateInfoDictionary.count > 0 )"
+ "( personalPhotographerMetadataDictionary.count > 0 )"
+ "( version >= 1 )"
+ "+[AVCaptureMovieFileOutput _makeTimelapseMovieFromTimewarpTimelapseClassicIntermediateMovie:timelapseMovie:timelapseDestinationFrameRate:error:]"
+ ", %lu expected (%lu unmapped)"
+ ", mask=%p"
+ ", supports Cinematic Metadata"
+ ", supports Continuous AF Tracking"
+ ", supports Personal Photographer"
+ ", supports Texture Style"
+ "-[AVCaptureFigVideoDevice _queryPrimaryDisplayRegion]"
+ "-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForWrapper:withPayload:demoof:addMetadata:]"
+ "-[AVCaptureMovieFileOutputAssetWriterInputHelper ensureWriterInputIsReadyForMoreMediaData]"
+ "-[AVCapturePersonalPhotographerSessionFinishCoordinator _handleWatchdogTimeout]"
+ "-[AVCapturePhotoOutput _handleDidFinishPersonalPhotographerSessionNotificationWithPayload:forRequest:]"
+ "-[AVCapturePhotoOutput initiateManualPersonalPhotographerCapture]"
+ "-[AVCapturePhotoOutput startPersonalPhotographerSessionWithSettings:delegate:]_block_invoke"
+ ".lapse.mov"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVCapturePhotoOutput.m"
+ "10"
+ "12"
+ "2OOOI"
+ "8"
+ "9"
+ "99"
+ "<%@ %p> captures: %lu%@, state:%@>"
+ "<%@ %p> manualCapture:%@ frameScore:%.3f frameID:%d sessionID:%u context:%@%@%@"
+ "<%@ %p> origPTS:%.6f replacedPhotoTimestamp:%.6f settingsID:%lld"
+ "<%@: %p, payloadSize=%lu, time=%lld>"
+ "<%@: %p, rawFrameId: %lu, metadataFrameId: %lu, refFrameId: %lu, contextIndex: %d, frameType: %d, projectorMode: %d, ready: %d, coachingStatus: %d, probePattern: %d, time=%lld>"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Failed to query primaryDisplayRegion. Reusing cached value"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received notification for kFigCaptureSourceProperty_DeviceAngle change - %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received notification for kFigCaptureSourceProperty_Occluded change - %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received notification for kFigCaptureSourceProperty_PrimaryDisplayRegion change - %@"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: %.4lf: missing frame timestamp (%@) and/or decimation tag (%@)"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: %.4lf: retiming returned error %d"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: %@: %.4lf: decimation tag %d, max decimation level %d, toss frame %c with compression flags %@"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: %@: keeping %.4lf as %.4lf : %.4lf with compression flags %@"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: %@: signal was already requested!!!"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) max decimation level: %d, framerate %.4lf, fast decimation allowed %c, frame retiming allowed %c"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: (%p) trying to make final Timewarp Timelapse Classic movie even though the following error happened: %d"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: Average bitrate for final movie is %.0lf"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: appending TW timed metadata group for %.4lf failed"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: appending scene illuminance timed metadata group for %.4lf failed"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: appending video for %.4lf"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: could not create TW timed metadata group for %.4lf"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: could not create scene illuminance timed metadata group for %.4lf"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: could not get valid frame duration!"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: did not have pixel buffer for %.4lf"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: ending decimation, %d video samples with EOD %c, %d TW metadata with EOD %c, %d scene illuminance metadata with EOD %c"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: fast decimation is allowed due to sequence capture ID matching for %d samples"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: fast decimation not allowed due to mismatching sequence capture IDs or mismatching sample counts (%d video samples, %d metadata samples)"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: fast decimation not allowed due to sequence capture ID mismatch:  read %d vs expected %d"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: intermediate video PTS %.4lf does not match metadata time %.4lf"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: intermediate video PTS %.4lf does not match metadata time %.4lf, which indicates a frame drop, therefore fast decimation not allowed"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: movie metadata specifies %c for fast decimation"
+ "<<<< AVCaptureMovieFileOutput >>>> %s: movie metadata specifies %d for max decimation level"
+ "<<<< AVCaptureMovieFileOutput >>>> Fig"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Photo to keep with timestamp %fs has already been registered for deletion"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Received PEP capture registration decisions: %lu to keep, %lu to remove"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Unable to initiate a manual Personal Photographer session as FigCaptureSession has been deallocated!"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Unknown photo to keep with timestamp: %fs"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Unknown photo to remove with timestamp: %fs"
+ "<<<< AVCapturePhotoOutput >>>> %s: Personal Photographer configuration error"
+ "<<<< AVCapturePhotoOutput >>>> %s: Personal Photographer session completion timeout"
+ "<<<< AVCapturePhotoOutput >>>> %s: Personal Photographer session coordinator timed out waiting for in-flight captures; forcing didFinish callback (%{private}@)"
+ "AVCaptureAncillaryDataUserKeyRDD18InstanceUID"
+ "AVCaptureAncillaryDataUserKeyRDD18UDAMSetVersion"
+ "AVCaptureAncillaryDataUserKeyRDD18UserItems"
+ "AVCaptureDeviceAngleDidChangeNotification"
+ "AVCaptureDeviceExposureSignalDocument"
+ "AVCaptureDeviceExposureSignalFlicker"
+ "AVCaptureDeviceExposureSignalGroupPhoto"
+ "AVCaptureDeviceExposureSignalStarburst"
+ "AVCaptureDeviceExposureSignalSubjectMotion"
+ "AVCaptureDeviceTypeBuiltInBostonUltraWideCamera"
+ "AVCaptureDeviceTypeBuiltInColorAssistedInfraredMetadataCamera"
+ "AVCaptureDeviceTypeBuiltInRenoUltraWideCamera"
+ "AVCaptureDeviceTypeBuiltInRenoUltraWideMetadataCamera"
+ "AVCaptureMovieFileOutput.m"
+ "AVCapturePersonalPhotographerDuplicateInfo.m"
+ "AVCapturePersonalPhotographerMetadata.m"
+ "AVGQCaptureLowLightVideoNoiseReductionAutomaticallyEnabled"
+ "AVGQCaptureOmahaConstituentDevicesSupported"
+ "AVMetadataObjectTypeCinematicVideoMetadata"
+ "AVMetadataObjectTypeCinematicVideoMetadata is not supported in an AVCaptureMultiCamSession."
+ "AVMetadataObjectTypeCinematicVideoMetadata is not supported when an AVCaptureMovieFileOutput is present."
+ "AVMetadataObjectTypeCinematicVideoMetadata is not supported when video stabilization strength is set to Ultra."
+ "BUW"
+ "Bias must be greater than -1 and less than 1"
+ "BostonUltraWide"
+ "C743"
+ "CIRM"
+ "Cannot assign enabledExposureSignals while automaticallyEnablesExposureSignals is true, assign automaticallyEnablesExposureSignals = false first"
+ "Cannot be set when AVCaptureDeviceInput's isCinematicVideoCaptureEnabled is YES"
+ "Cannot be set when automaticallyEnablesLowLightVideoNoiseReduction is YES"
+ "Cannot be set when videoStabilizationStrength is High or Ultra (Action Camera mode)"
+ "Cannot set cinematicVideoMetadataCaptureEnabled when automaticallyAdjustsCinematicVideoMetadataCaptureEnabled is YES"
+ "Cannot set data for tag 0x%04X"
+ "Cannot set string for tag 0x%04X"
+ "Captures are not supported while Personal Photographer is enabled"
+ "Capturing ProRes on this device requires Pro Video Storage. Set usesProVideoStorage = YES or capture to external storage device."
+ "ColorAssistedInfraredMetadata"
+ "Complete"
+ "Continuous auto focus tracking cannot be set when AVCaptureDeviceInput's isCinematicVideoCaptureEnabled is YES"
+ "Continuous auto focus tracking cannot be set when action camera is enabled"
+ "Continuous auto focus tracking must be enabled"
+ "Existing Personal Photographer session photo request replaced with %@"
+ "FT_"
+ "Face ID coexistence is not supported on this receiver"
+ "Face ID mode(%lu) outside of expected range for AVCaptureFaceIDMode."
+ "Face ID retryType(%lu) outside of expected range for AVCaptureFaceIDRetryType."
+ "Face ID unwrap is not supported on this receiver"
+ "FaceID"
+ "Failed to create Personal Photographer session coordinator"
+ "Filmic"
+ "Glowy"
+ "LastShownBuild:AVCapturePhotoOutput.m:3224"
+ "LastShownBuild:AVCapturePhotoOutput.m:9675"
+ "LastShownDate:AVCapturePhotoOutput.m:3224"
+ "LastShownDate:AVCapturePhotoOutput.m:9675"
+ "LowCurrentTorch is not supported on this device"
+ "Moment captures are not supported while Personal Photographer is enabled"
+ "NONE"
+ "NOT (SELF IN %@)"
+ "No active personal photographer session"
+ "Not supported - setPrimaryConstituentDeviceSwitchingBehaviorLockedWithDevice: cannot be called on this receiver"
+ "Not supported - use -[AVCaptureDeviceFormat isLowLightVideoNoiseReductionSupported]"
+ "Not supported - use -isLowLightVideoNoiseReductionSupported"
+ "Not supported - use activeFormat.isContinuousAutoFocusTrackingSupported"
+ "Not supported - use faceIDUnwrapSupported"
+ "Not supported - use isCinematicVideoMetadataCaptureSupported"
+ "Not supported - use isFaceIDCoexistenceSupported"
+ "Not supported - use isTimewarpSupported"
+ "Pending"
+ "Personal Photographer configuration error"
+ "Personal Photographer is not enabled"
+ "Personal Photographer is not supported in the current configuration"
+ "Personal Photographer session already active"
+ "Personal Photographer session completion timeout"
+ "Personal Photographer session did finish timed out waiting for in-flight captures (%@)"
+ "ProbePatternIndex(%lu) outside the range of numberOfDoubles expected"
+ "ProbePatternType(%lu) outside the range of expected AVCaptureFaceIDProbePatternType"
+ "RUW"
+ "RUWM"
+ "Received invalid constant for variable aperture device"
+ "RenoUltraWide"
+ "RenoUltraWideMetadata"
+ "Secure signing capture is not supported in this configuration"
+ "Secure signing capture is not supported or support is not enabled by this device"
+ "Soft"
+ "Studio"
+ "TOO MANY SAMPLE ATTACHMENTS (%d)!"
+ "TextureStyleGrain"
+ "TextureStyleIntensity"
+ "TextureStylePreset"
+ "The active format of the source device does not support manual exposure bracketed capture. Use AVCaptureDeviceFormat supportsExposureModeCustomWithLensAperture:duration:ISO:] with AVCaptureLensApertureCurrent, AVCaptureExposureDurationCurrent and AVCaptureISOCurrent"
+ "The current device does not support locking primary constituent with a device."
+ "The passed lensAperture value %f %s - use activeFormat.minLensAperture and activeFormat.maxLensAperture"
+ "The selected device is not a valid constituent device"
+ "The specified tag does not support data type"
+ "The specified tag is invalid or reserved"
+ "The userDefinedAncillaryDataSizeRemaining would be exceeded"
+ "Time-lapse"
+ "Time-lapse-Classic"
+ "UNSPECIFIED"
+ "Unsupported - cannot trigger Face ID bracket without AVMetadataObjectTypeFaceID included in -metadataObjectTypes"
+ "Unsupported - check for AVMetadataObjectTypeFaceID in -availableMetadataObjectTypes"
+ "Unsupported - use -rawFrameDeliverySupported"
+ "Unsupported combination of auto/locked parameters (lensAperture %s, duration %s, ISO %s), use -[AVCaptureDeviceFormat supportsExposureModeCustomWithLensAperture:duration:ISO:] to check mode support"
+ "Unsupported metadataObjectTypes(%@) enabled when running Face ID."
+ "Unsupported personal photographer capture rate - %d"
+ "V63"
+ "V64"
+ "V64-V64s"
+ "V64s"
+ "V68"
+ "Value in doubleOrder array(%lu) outside the range of expected AVCaptureFaceIDDoubleOrder"
+ "Virtual devices do not support direct assignment to exposure mode Custom - use -[AVCaptureDevice setExposureModeCustomWithLensAperture:duration:ISO:] to a supported configuration."
+ "[%@][%@][%@]"
+ "_watchdog"
+ "activeExposureSignals"
+ "activeOmahaConstituentDeviceType"
+ "assetReader != ((void *)0)"
+ "assetReaderTimewarpMetadataOutput != ((void *)0)"
+ "assetReaderVideoOutput != ((void *)0)"
+ "autoExposureLensApertureRateLimit must be 0 or a value greater than or equal to 1"
+ "automaticallyAdjustsExposureDuration"
+ "automaticallyAdjustsISO"
+ "automaticallyAdjustsLensAperture"
+ "canAddMetadataOutput"
+ "canAddSceneIlluminanceMetadataInput"
+ "canAddSceneIlluminanceMetadataOutput"
+ "canAddTimewarpMetadataInput"
+ "canAddTimewarpMetadataOutput"
+ "canAddVideoInput"
+ "canAddVideoOutput"
+ "capturedPhotos: %lu, photosToSave: %lu, photosToDelete: %lu"
+ "cinematicVideoMetadata"
+ "cinematicVideoMetadataCaptureEnabled"
+ "cinematicVideoMetadataCaptureSupported"
+ "com.apple.avfoundation.AVCaptureAncillaryDataEncoder"
+ "com.apple.avfoundation.capture.moviefileoutput.tw_decimation_queue"
+ "com.apple.avfoundation.securevideooutput.queue"
+ "com.apple.photos.captureMode"
+ "completionHandler"
+ "continuousAutoFocusTrackingEnabled"
+ "continuousAutoFocusTrackingLensPositionBias"
+ "continuousAutoFocusTrackingSubjectAcquired"
+ "could not add TW metadata AVAssetReaderOutput"
+ "could not add TW metadata AVAssetWriterInput"
+ "could not add metadata AVAssetReaderOutput"
+ "could not add scene illuminance metadata AVAssetReaderOutput"
+ "could not add scene illuminance metadata AVAssetWriterInput"
+ "could not add video AVAssetReaderOutput for video track"
+ "could not add video AVAssetWriterInput"
+ "could not create AVAssetReader"
+ "could not create AVAssetReaderOutputMetadataAdaptor"
+ "could not create AVAssetReaderTrackOutput"
+ "could not create AVAssetReaderTrackOutput for video track"
+ "could not create AVAssetWriter"
+ "could not create AVAssetWriterInputPixelBufferAdaptor"
+ "could not create TW AVAssetReaderOutputMetadataAdaptor"
+ "could not create TW AVAssetReaderTrackOutput"
+ "could not create TW AVAssetWriterInputMetadataAdaptor"
+ "could not create TW metadata AVAssetWriterInput"
+ "could not create TW metadata AVCaptureMovieFileOutputAssetWriterInputHelper"
+ "could not create final metadata fdesc"
+ "could not create scene illuminance AVAssetReaderOutputMetadataAdaptor"
+ "could not create scene illuminance AVAssetReaderTrackOutput"
+ "could not create scene illuminance AVAssetWriterInputMetadataAdaptor"
+ "could not create scene illuminance metadata AVAssetWriterInput"
+ "could not create scene illuminance metadata AVCaptureMovieFileOutputAssetWriterInputHelper"
+ "could not create video AVAssetWriterInput"
+ "could not create video AVCaptureMovieFileOutputAssetWriterInputHelper"
+ "could not start asset reader"
+ "could not start asset writer"
+ "deviceAngle"
+ "enabledExposureSignals"
+ "exsp"
+ "faceIDCoexistenceEnabled"
+ "faceIDUnwrapResult"
+ "figSettings"
+ "finalAssetWriter != ((void *)0)"
+ "finalAssetWriterSceneIlluminanceMetadataInput != ((void *)0)"
+ "finalAssetWriterSceneIlluminanceMetadataInputAdaptor != ((void *)0)"
+ "finalAssetWriterSceneIlluminanceMetadataInputHelper != ((void *)0)"
+ "finalAssetWriterTimewarpMetadataInput != ((void *)0)"
+ "finalAssetWriterTimewarpMetadataInputAdaptor != ((void *)0)"
+ "finalAssetWriterTimewarpMetadataInputHelper != ((void *)0)"
+ "finalAssetWriterVideoInput != ((void *)0)"
+ "finalAssetWriterVideoInputAdaptor != ((void *)0)"
+ "finalAssetWriterVideoInputHelper != ((void *)0)"
+ "floating"
+ "focusTrackedObject"
+ "found metadata but no video track"
+ "found video track but no description"
+ "frameRate > 0"
+ "grain must be between 0.0 and 1.0"
+ "iOS 27.0"
+ "intermediateAsset"
+ "intermediateAssetReader != ((void *)0)"
+ "intermediateAssetReaderSceneIlluminanceMetadataOutput != ((void *)0)"
+ "intermediateAssetReaderTimewarpMetadataOutput != ((void *)0)"
+ "intermediateAssetReaderVideoOutput != ((void *)0)"
+ "intermediateSceneIlluminanceMetadataOutputAdaptor != ((void *)0)"
+ "intermediateTimewarpMetadataOutputAdaptor != ((void *)0)"
+ "intermediateTimewarpMetadataTrack != ((void *)0)"
+ "intermediateVideoFormatDesc != ((void*)0)"
+ "intermediateVideoTrack != ((void *)0)"
+ "invalid framerate specified"
+ "is not the fixed aperture value"
+ "is outside the supported range"
+ "lensAperture"
+ "level > 60"
+ "livePhotoMovieFileURL directory must be created by the caller for Personal Photographer captures"
+ "livePhotoMovieFileURL must have a directory path for Personal Photographer captures"
+ "locked"
+ "lowLightVideoNoiseReductionEnabled"
+ "lowLightVideoNoiseReductionSupported"
+ "mdta/%@"
+ "mdta/com.apple.quicktime.cinematic-video-metadata"
+ "mdta/com.apple.quicktime.cinematic-video.cinematography"
+ "mdta/com.apple.quicktime.faceid"
+ "mdta/com.apple.quicktime.focus-tracked-object"
+ "mdta/com.apple.quicktime.timewarp-decimation-level"
+ "mdta/com.apple.quicktime.timewarp-decimation-tag"
+ "mdta/com.apple.quicktime.timewarp-original-frame-timestamp-in-milliseconds-since-1970"
+ "mdta/com.apple.quicktime.timewarp-sequence-capture-id"
+ "mfo_getTimewarpTimelapseDecimationInformation"
+ "no TW metadata found"
+ "numberOfDoubles(%lu) not equal to number of elements in the doubleOrder array %lu"
+ "personalPhotographerEnabled"
+ "personalPhotographerSessionActive"
+ "personalPhotographerSubjectDetectionStatus"
+ "personalPhotographerSupported"
+ "photoRequest"
+ "preset:%@ intensity:%.3f grain:%.3f version:%ld"
+ "primaryDisplayRegion"
+ "profile == 100"
+ "readingStarted"
+ "readyForMoreMediaData"
+ "secureSigningPhotoCaptureEnabled"
+ "secureSigningPhotoCaptureSupportEnabled"
+ "secureSigningPhotoCaptureSupported"
+ "self != %@"
+ "settings.autoSecureSigningPhotoCaptureEnabled may not be set to YES unless self.secureSigningPhotoCaptureEnabled is YES"
+ "settings.personalPhotographerCaptureRate may not be set unless self.personalPhotographerEnabled is YES"
+ "spsDataSize >= 4"
+ "suspended"
+ "timewarpMetadataOutputAdaptor != ((void *)0)"
+ "timewarpMode"
+ "unable to create intermediate timelapse asset object"
+ "unresolvedSettings"
+ "v24@?0@\"AVCapturePhotoRequest\"8@\"NSError\"16"
+ "v24@?0@\"NSArray\"8@\"NSError\"16"
+ "writingStarted"
+ "{PersonalPhotographer}"
- "2OOOG"
- "Source device does not support manual exposure bracketed capture. Use AVCaptureDevice -isExposureModeSupported: with AVCaptureExposureModeCustom"
```
