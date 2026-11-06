## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/Versions/A/AVFCapture`

```diff

-764.21.3.0.0
-  __TEXT.__text: 0x1b179c
-  __TEXT.__objc_methlist: 0x17fec
-  __TEXT.__cstring: 0x39099
+764.41.11.0.0
+  __TEXT.__text: 0x1b42b0
+  __TEXT.__objc_methlist: 0x182fc
+  __TEXT.__cstring: 0x39829
   __TEXT.__const: 0x1602
-  __TEXT.__gcc_except_tab: 0x371c
-  __TEXT.__oslogstring: 0xf476
+  __TEXT.__gcc_except_tab: 0x3748
+  __TEXT.__oslogstring: 0xfe20
   __TEXT.__dlopen_cstrs: 0x275
   __TEXT.__ustring: 0x112
   __TEXT.__swift5_typeref: 0xef

   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x6f30
+  __TEXT.__unwind_info: 0x6fc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1878
-  __DATA_CONST.__objc_classlist: 0x9d8
+  __DATA_CONST.__const: 0x1880
+  __DATA_CONST.__objc_classlist: 0x9e8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9f90
+  __DATA_CONST.__objc_selrefs: 0xa0b0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x828
+  __DATA_CONST.__objc_superrefs: 0x838
   __DATA_CONST.__objc_arraydata: 0x2c0
-  __DATA_CONST.__got: 0x2fd8
-  __AUTH_CONST.__const: 0x3380
-  __AUTH_CONST.__cfstring: 0x17420
-  __AUTH_CONST.__objc_const: 0x26818
+  __DATA_CONST.__got: 0x3020
+  __AUTH_CONST.__const: 0x3360
+  __AUTH_CONST.__cfstring: 0x175e0
+  __AUTH_CONST.__objc_const: 0x26b48
   __AUTH_CONST.__objc_intobj: 0xab0
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1560
+  __AUTH_CONST.__auth_got: 0x1570
   __AUTH_CONST.__auth_ptr: 0x40
-  __AUTH.__objc_data: 0x4260
-  __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x27a4
-  __DATA.__data: 0x1058
-  __DATA.__bss: 0xa00
-  __DATA.__common: 0x1e0
-  __DATA_DIRTY.__objc_data: 0x2030
-  __DATA_DIRTY.__data: 0x160
+  __AUTH.__objc_data: 0x2848
+  __DATA.__objc_ivar: 0x27c8
+  __DATA.__data: 0x1068
+  __DATA.__bss: 0xa20
+  __DATA.__common: 0x200
+  __DATA_DIRTY.__objc_data: 0x3ae8
+  __DATA_DIRTY.__data: 0x170
   __DATA_DIRTY.__bss: 0x77c
   __DATA_DIRTY.__common: 0x200
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11340
-  Symbols:   22367
-  CStrings:  5022
+  Functions: 11409
+  Symbols:   22506
+  CStrings:  5071
 
Symbols:
+ +[AVCaptureDevice continuityCaptureEnabled]
+ +[AVCaptureDevice setContinuityCaptureEnabled:]
+ +[AVCaptureDevice_Tundra continuityCaptureEnabled]
+ +[AVCaptureDevice_Tundra setContinuityCaptureEnabled:]
+ +[AVCaptureProprietaryDefaultsSingleton migrateDefaultsFromAppBundleID:newAppBundleID:]
+ +[AVCaptureResolvedPhotoSettings resolvedSettingsWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:personalPhotographerDuplicateInfo:]
+ +[AVMetadataDeviceProximityDetectionObject deviceProximityDetectionWithDeviceDictionary:input:time:]
+ +[AVMetadataLightSourceEstimationObject lightSourceEstimationWithDictionary:input:time:]
+ -[AVCaptureDevice _exposesOmahaConstituentDevices]
+ -[AVCaptureDevice moduleSealedState]
+ -[AVCaptureDevice supportedMetadataIdentifiersForPerceptionThumbnailChannel]
+ -[AVCaptureDevice(PrimaryDisplayRegion) _queryPrimaryDisplayRegion]
+ -[AVCaptureDeviceRotationCoordinator _initWithDevice:previewLayer:suppliesVideoRotationAngleForHorizonLevelPreviewWithoutPreviewLayer:]
+ -[AVCaptureFigVideoDevice _queryPrimaryDisplayRegion]
+ -[AVCaptureFigVideoDevice moduleSealedState]
+ -[AVCaptureFigVideoDevice supportedMetadataIdentifiersForPerceptionThumbnailChannel]
+ -[AVCaptureMetadataOutput _metadataIdentifiersForPerceptionThumbnailChannel]
+ -[AVCaptureMetadataOutput deviceProximityDetectionDeviceTypes]
+ -[AVCaptureMetadataOutput deviceProximityDetectionTargetFrameRate]
+ -[AVCaptureMetadataOutput lightSourceEstimationAmbientLuminance]
+ -[AVCaptureMetadataOutput lightSourceEstimationTargetFrameRate]
+ -[AVCaptureMetadataOutput metadataObjectTypesForPerceptionThumbnailChannel]
+ -[AVCaptureMetadataOutput perceptionTestModeEnabled]
+ -[AVCaptureMetadataOutput setDeviceProximityDetectionDeviceTypes:]
+ -[AVCaptureMetadataOutput setLightSourceEstimationAmbientLuminance:]
+ -[AVCaptureMetadataOutput setMetadataObjectTypesForPerceptionThumbnailChannel:]
+ -[AVCaptureMetadataOutput setPerceptionTestModeEnabled:]
+ -[AVCaptureMetadataOutput supportedMetadataObjectTypesForPerceptionThumbnailChannel]
+ -[AVCaptureMetadataOutput_Tundra _metadataIdentifiersForPerceptionThumbnailChannel]
+ -[AVCaptureMetadataOutput_Tundra deviceProximityDetectionDeviceTypes]
+ -[AVCaptureMetadataOutput_Tundra lightSourceEstimationAmbientLuminance]
+ -[AVCaptureMetadataOutput_Tundra metadataObjectTypesForPerceptionThumbnailChannel]
+ -[AVCaptureMetadataOutput_Tundra perceptionTestModeEnabled]
+ -[AVCaptureMetadataOutput_Tundra setDeviceProximityDetectionDeviceTypes:]
+ -[AVCaptureMetadataOutput_Tundra setLightSourceEstimationAmbientLuminance:]
+ -[AVCaptureMetadataOutput_Tundra setMetadataObjectTypesForPerceptionThumbnailChannel:]
+ -[AVCaptureMetadataOutput_Tundra setPerceptionTestModeEnabled:]
+ -[AVCaptureMetadataOutput_Tundra supportedMetadataObjectTypesForPerceptionThumbnailChannel]
+ -[AVCaptureMovieFileOutput _updateConstituentDeviceSwitchingBehaviorForSourceDevice:]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator finishWithRequest:expectedSettingsIDs:error:]
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator recordStillComplete]
+ -[AVCapturePersonalPhotographerSessionResults _isPhotoRegisteredWithSettingsIDNumber:]
+ -[AVCapturePersonalPhotographerSessionResults _timestampsForSettingsIDs:]
+ -[AVCapturePersonalPhotographerSessionResults isPhotoRegisteredForDeletionWithSettingsID:]
+ -[AVCapturePersonalPhotographerSessionResults isPhotoRegisteredWithSettingsID:]
+ -[AVCapturePersonalPhotographerSessionResults registerPhotoSettingsIDForDeletion:]
+ -[AVCapturePersonalPhotographerSessionResults registerPhotoTimestamp:forSettingsID:]
+ -[AVCapturePersonalPhotographerSessionResults registerPhotoWithSettingsID:]
+ -[AVCapturePersonalPhotographerSessionResults systemRecommendedPhotosToDeleteBySettingsID]
+ -[AVCapturePersonalPhotographerSessionResults systemRecommendedPhotosToSaveBySettingsID]
+ -[AVCaptureProprietaryDefaultsSingleton migrateDefaultsFromAppBundleID:newAppBundleID:]
+ -[AVCaptureResolvedPhotoSettings _initWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:personalPhotographerDuplicateInfo:]
+ -[AVCaptureResolvedPhotoSettings personalPhotographerDuplicateInfo]
+ -[AVCaptureSession _updatePrimaryDisplayRegionIfNeeded]
+ -[AVMetadataDeviceProximityDetectionObject confidence]
+ -[AVMetadataDeviceProximityDetectionObject copyWithZone:]
+ -[AVMetadataDeviceProximityDetectionObject description]
+ -[AVMetadataDeviceProximityDetectionObject deviceID]
+ -[AVMetadataDeviceProximityDetectionObject deviceType]
+ -[AVMetadataDeviceProximityDetectionObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:]
+ -[AVMetadataDeviceProximityDetectionObject initWithDeviceDictionary:sourceCaptureInput:time:]
+ -[AVMetadataDeviceProximityDetectionObject pose]
+ -[AVMetadataFaceObject hasLookingAtCameraConfidence]
+ -[AVMetadataFaceObject lookingAtCameraConfidence]
+ -[AVMetadataFaceObjectInternal hasLookingAtCameraConfidence]
+ -[AVMetadataFaceObjectInternal lookingAtCameraConfidence]
+ -[AVMetadataFaceObjectInternal setHasLookingAtCameraConfidence:]
+ -[AVMetadataFaceObjectInternal setLookingAtCameraConfidence:]
+ -[AVMetadataLightSourceEstimationObject copyWithZone:]
+ -[AVMetadataLightSourceEstimationObject dealloc]
+ -[AVMetadataLightSourceEstimationObject description]
+ -[AVMetadataLightSourceEstimationObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:]
+ -[AVMetadataLightSourceEstimationObject initWithLightSourceEstimationDictionary:sourceCaptureInput:time:]
+ -[AVMetadataLightSourceEstimationObject payload]
+ -[AVMetadataObject sentToPerceptionThumbnailChannel]
+ -[AVMetadataObjectInternal sentToPerceptionThumbnailChannel]
+ -[AVMetadataObjectInternal setSentToPerceptionThumbnailChannel:]
+ AVCaptureClientHasEntitlement.checkDisableContinuityCameraHostOnceToken
+ AVCaptureClientHasEntitlement.checkMigrateDefaultsOnceToken
+ AVCaptureClientHasEntitlement.disableContinuityCameraHostAllowed
+ AVCaptureClientHasEntitlement.migrateDefaults
+ GCC_except_table1030
+ GCC_except_table1038
+ GCC_except_table1048
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table134
+ GCC_except_table135
+ GCC_except_table156
+ GCC_except_table157
+ GCC_except_table161
+ GCC_except_table166
+ GCC_except_table177
+ GCC_except_table18
+ GCC_except_table181
+ GCC_except_table186
+ GCC_except_table188
+ GCC_except_table193
+ GCC_except_table197
+ GCC_except_table198
+ GCC_except_table203
+ GCC_except_table204
+ GCC_except_table208
+ GCC_except_table209
+ GCC_except_table216
+ GCC_except_table219
+ GCC_except_table226
+ GCC_except_table243
+ GCC_except_table248
+ GCC_except_table268
+ GCC_except_table277
+ GCC_except_table286
+ GCC_except_table295
+ GCC_except_table296
+ GCC_except_table305
+ GCC_except_table314
+ GCC_except_table326
+ GCC_except_table331
+ GCC_except_table334
+ GCC_except_table342
+ GCC_except_table345
+ GCC_except_table366
+ GCC_except_table372
+ GCC_except_table375
+ GCC_except_table378
+ GCC_except_table382
+ GCC_except_table385
+ GCC_except_table389
+ GCC_except_table400
+ GCC_except_table404
+ GCC_except_table41
+ GCC_except_table414
+ GCC_except_table419
+ GCC_except_table425
+ GCC_except_table426
+ GCC_except_table434
+ GCC_except_table455
+ GCC_except_table470
+ GCC_except_table479
+ GCC_except_table497
+ GCC_except_table520
+ GCC_except_table53
+ GCC_except_table530
+ GCC_except_table542
+ GCC_except_table562
+ GCC_except_table565
+ GCC_except_table591
+ GCC_except_table595
+ GCC_except_table608
+ GCC_except_table616
+ GCC_except_table624
+ GCC_except_table630
+ GCC_except_table635
+ GCC_except_table643
+ GCC_except_table650
+ GCC_except_table660
+ GCC_except_table674
+ GCC_except_table688
+ GCC_except_table699
+ GCC_except_table709
+ GCC_except_table723
+ GCC_except_table733
+ GCC_except_table745
+ GCC_except_table764
+ GCC_except_table77
+ GCC_except_table785
+ GCC_except_table788
+ GCC_except_table826
+ GCC_except_table828
+ GCC_except_table83
+ GCC_except_table830
+ GCC_except_table85
+ GCC_except_table861
+ GCC_except_table873
+ GCC_except_table875
+ GCC_except_table877
+ GCC_except_table883
+ GCC_except_table887
+ GCC_except_table89
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table930
+ GCC_except_table939
+ OBJC_IVAR_$_AVCaptureFigVideoDevice._primaryDisplayRegionSupported
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.deviceProximityDetectionDeviceTypes
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.lightSourceEstimationAmbientLuminance
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.metadataObjectTypesForPerceptionThumbnailChannel
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.perceptionTestModeEnabled
+ OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.deviceExposesOmahaConstituentDevices
+ OBJC_IVAR_$_AVCaptureMovieFileOutputInternal.deviceIsBravoVariant
+ OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._expectedSetOfSettingsIDsCommitted
+ OBJC_IVAR_$_AVCapturePersonalPhotographerSessionResults._capturedSettingsIDs
+ OBJC_IVAR_$_AVCapturePersonalPhotographerSessionResults._systemRecommendedPhotosToDeleteBySettingsID
+ OBJC_IVAR_$_AVCapturePersonalPhotographerSessionResults._systemRecommendedPhotosToSaveBySettingsID
+ OBJC_IVAR_$_AVCapturePersonalPhotographerSessionResults._timestampsBySettingsID
+ OBJC_IVAR_$_AVCaptureResolvedPhotoSettingsInternal.personalPhotographerDuplicateInfo
+ OBJC_IVAR_$_AVMetadataDeviceProximityDetectionObject._confidence
+ OBJC_IVAR_$_AVMetadataDeviceProximityDetectionObject._deviceID
+ OBJC_IVAR_$_AVMetadataDeviceProximityDetectionObject._deviceType
+ OBJC_IVAR_$_AVMetadataDeviceProximityDetectionObject._pose
+ OBJC_IVAR_$_AVMetadataFaceObjectInternal._hasLookingAtCameraConfidence
+ OBJC_IVAR_$_AVMetadataFaceObjectInternal._lookingAtCameraConfidence
+ OBJC_IVAR_$_AVMetadataLightSourceEstimationObject._payload
+ OBJC_IVAR_$_AVMetadataObjectInternal._sentToPerceptionThumbnailChannel
+ _AVCaptureDevicePrimaryDisplayRegionDidChangeNotification
+ _AVCaptureDeviceTypeBuiltInInnerUltraWideCamera
+ _AVCaptureDeviceTypeBuiltInOuterUltraWideCamera
+ _AVCaptureEntitlementProprietaryDefaultsMigration
+ _AVCaptureEntitlementToggleContinuityCaptureEnablement
+ _AVContinuityCaptureOnBoardingUIButtonClickedNotificationSetUpLater
+ _AVControlCenterVideoEffectsRingLightOnboardingTipSignalPreferenceKey
+ _AVMetadataObjectTypeDeviceProximityDetection
+ _AVMetadataObjectTypeLightSourceEstimation
+ _CMTimeCopyDescription
+ _FigCaptureProprietaryDefaultsContinuityCaptureEnabledOnMacKey
+ _FigCaptureProprietaryDefaultsRingLightOnboardingTipSignalKey
+ _FigCaptureSkipTTR
+ _OBJC_CLASS_$_AVMetadataDeviceProximityDetectionObject
+ _OBJC_CLASS_$_AVMetadataLightSourceEstimationObject
+ _OBJC_METACLASS_$_AVMetadataDeviceProximityDetectionObject
+ _OBJC_METACLASS_$_AVMetadataLightSourceEstimationObject
+ __73-[AVControlCenterModuleState _proprietaryDefaultChanged:keyPath:context:]_block_invoke
+ __OBJC_$_CLASS_METHODS_AVMetadataDeviceProximityDetectionObject
+ __OBJC_$_CLASS_METHODS_AVMetadataLightSourceEstimationObject
+ __OBJC_$_INSTANCE_METHODS_AVMetadataDeviceProximityDetectionObject
+ __OBJC_$_INSTANCE_METHODS_AVMetadataLightSourceEstimationObject
+ __OBJC_$_INSTANCE_VARIABLES_AVMetadataDeviceProximityDetectionObject
+ __OBJC_$_INSTANCE_VARIABLES_AVMetadataLightSourceEstimationObject
+ __OBJC_$_PROP_LIST_AVMetadataDeviceProximityDetectionObject
+ __OBJC_$_PROP_LIST_AVMetadataLightSourceEstimationObject
+ __OBJC_CLASS_PROTOCOLS_$_AVMetadataDeviceProximityDetectionObject
+ __OBJC_CLASS_PROTOCOLS_$_AVMetadataLightSourceEstimationObject
+ __OBJC_CLASS_RO_$_AVMetadataDeviceProximityDetectionObject
+ __OBJC_CLASS_RO_$_AVMetadataLightSourceEstimationObject
+ __OBJC_METACLASS_RO_$_AVMetadataDeviceProximityDetectionObject
+ __OBJC_METACLASS_RO_$_AVMetadataLightSourceEstimationObject
+ ___27-[AVCaptureSession dealloc]_block_invoke
+ ___46-[AVCaptureSession _initWithMediaEnvironment:]_block_invoke_2
+ ___87-[AVCaptureProprietaryDefaultsSingleton migrateDefaultsFromAppBundleID:newAppBundleID:]_block_invoke
+ ___block_descriptor_40_e8_32o_e11_v16?0B8B12l
+ _fvd_clampFrameDuration
+ _gAVCapturePersonalPhotographerSessionResultsTrace
+ _kFigCaptureSampleBufferAttachmentKey_DeviceProximityDetection
+ _kFigCaptureSampleBufferAttachmentKey_LightSourceEstimation
+ _kFigCaptureSessionDidFinishPersonalPhotographerSessionCaptureKey_PresentationTimestamp
+ _kFigCaptureSessionDidFinishPersonalPhotographerSessionCaptureKey_SettingsID
+ _kFigCaptureSessionWillBeginCaptureNotificationPayloadKey_PersonalPhotographerDuplicateInfo
+ _kFigCaptureStreamDetectedObjectKey_SentToPerceptionThumbnailChannel
+ _kFigCaptureStreamMetadata_LookingAtCameraConfidenceLevel
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_ConfidenceLevel
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_DeviceID
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_DeviceType
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_PoseMatrix
+ _kFigCaptureStreamSecureDetectedProximityDevicesKey_DevicesArray
+ _objc_msgSend$_exposesOmahaConstituentDevices
+ _objc_msgSend$_initWithDevice:previewLayer:suppliesVideoRotationAngleForHorizonLevelPreviewWithoutPreviewLayer:
+ _objc_msgSend$_initWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:personalPhotographerDuplicateInfo:
+ _objc_msgSend$_isPhotoRegisteredWithSettingsIDNumber:
+ _objc_msgSend$_metadataIdentifiersForPerceptionThumbnailChannel
+ _objc_msgSend$_queryPrimaryDisplayRegion
+ _objc_msgSend$_timestampsForSettingsIDs:
+ _objc_msgSend$_updateConstituentDeviceSwitchingBehaviorForSourceDevice:
+ _objc_msgSend$_updatePrimaryDisplayRegionIfNeeded
+ _objc_msgSend$data
+ _objc_msgSend$deviceProximityDetectionDeviceTypes
+ _objc_msgSend$deviceProximityDetectionTargetFrameRate
+ _objc_msgSend$deviceProximityDetectionWithDeviceDictionary:input:time:
+ _objc_msgSend$finishWithRequest:expectedSettingsIDs:error:
+ _objc_msgSend$hasLookingAtCameraConfidence
+ _objc_msgSend$initWithDeviceDictionary:sourceCaptureInput:time:
+ _objc_msgSend$initWithLightSourceEstimationDictionary:sourceCaptureInput:time:
+ _objc_msgSend$isLowLightVideoNoiseReductionEnabled
+ _objc_msgSend$isPhotoRegisteredForDeletionWithSettingsID:
+ _objc_msgSend$isPhotoRegisteredWithSettingsID:
+ _objc_msgSend$lightSourceEstimationAmbientLuminance
+ _objc_msgSend$lightSourceEstimationTargetFrameRate
+ _objc_msgSend$lightSourceEstimationWithDictionary:input:time:
+ _objc_msgSend$lookingAtCameraConfidence
+ _objc_msgSend$migrateDefaultsFromAppBundleID:newAppBundleID:
+ _objc_msgSend$moduleSealedState
+ _objc_msgSend$perceptionTestModeEnabled
+ _objc_msgSend$pose
+ _objc_msgSend$recordStillComplete
+ _objc_msgSend$registerPhotoSettingsIDForDeletion:
+ _objc_msgSend$registerPhotoTimestamp:forSettingsID:
+ _objc_msgSend$registerPhotoWithSettingsID:
+ _objc_msgSend$resolvedSettingsWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:personalPhotographerDuplicateInfo:
+ _objc_msgSend$sentToPerceptionThumbnailChannel
+ _objc_msgSend$setContinuityCaptureEnabled:
+ _objc_msgSend$setDeviceProximityDetectionDeviceTypes:
+ _objc_msgSend$setDeviceProximityDetectionTargetFrameRate:
+ _objc_msgSend$setHasLookingAtCameraConfidence:
+ _objc_msgSend$setLightSourceEstimationAmbientLuminance:
+ _objc_msgSend$setLightSourceEstimationTargetFrameRate:
+ _objc_msgSend$setLookingAtCameraConfidence:
+ _objc_msgSend$setMetadataIdentifiersForPerceptionThumbnailChannel:
+ _objc_msgSend$setPerceptionTestModeEnabled:
+ _objc_msgSend$setSentToPerceptionThumbnailChannel:
+ _objc_msgSend$supportedMetadataIdentifiersForPerceptionThumbnailChannel
+ _objc_msgSend$supportedMetadataObjectTypesForPerceptionThumbnailChannel
- +[AVCaptureResolvedPhotoSettings resolvedSettingsWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:]
- -[AVCaptureDeviceRotationCoordinator _bsDeviceOrientationToVideoRotationAngle:unsupportedDeviceOrientation:]
- -[AVCaptureMovieFileOutput _updateBravoCameraSelectionBehaviorForSourceDevice:]
- -[AVCapturePersonalPhotographerSessionFinishCoordinator _addExpectedTimestamp:]
- -[AVCapturePersonalPhotographerSessionFinishCoordinator finishWithRequest:expectedTimestamps:error:]
- -[AVCapturePersonalPhotographerSessionFinishCoordinator recordStillCompleteForSettingsID:timestamp:]
- -[AVCapturePersonalPhotographerSessionResults _isPhotoRegisteredWithTimestampNSValue:]
- -[AVCapturePersonalPhotographerSessionResults isPhotoRegisteredForDeletionWithTimestamp:]
- -[AVCapturePersonalPhotographerSessionResults isPhotoRegisteredWithTimestamp:]
- -[AVCapturePersonalPhotographerSessionResults registerPhotoCapturedWithTimestamp:]
- -[AVCapturePersonalPhotographerSessionResults registerPhotoTimestampForDeletion:]
- -[AVCaptureResolvedPhotoSettings _initWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:]
- -[AVControlCenterModuleState ringLightAutoColorEnabled]
- -[AVControlCenterModuleState ringLightRecommendedColor]
- -[AVControlCenterModuleState setRingLightAutoColorEnabled:]
- GCC_except_table1027
- GCC_except_table1035
- GCC_except_table1045
- GCC_except_table110
- GCC_except_table111
- GCC_except_table119
- GCC_except_table122
- GCC_except_table132
- GCC_except_table133
- GCC_except_table145
- GCC_except_table150
- GCC_except_table151
- GCC_except_table154
- GCC_except_table16
- GCC_except_table160
- GCC_except_table165
- GCC_except_table167
- GCC_except_table168
- GCC_except_table169
- GCC_except_table184
- GCC_except_table185
- GCC_except_table190
- GCC_except_table192
- GCC_except_table195
- GCC_except_table196
- GCC_except_table199
- GCC_except_table200
- GCC_except_table205
- GCC_except_table206
- GCC_except_table207
- GCC_except_table214
- GCC_except_table217
- GCC_except_table232
- GCC_except_table241
- GCC_except_table266
- GCC_except_table284
- GCC_except_table293
- GCC_except_table294
- GCC_except_table303
- GCC_except_table324
- GCC_except_table329
- GCC_except_table332
- GCC_except_table340
- GCC_except_table343
- GCC_except_table350
- GCC_except_table364
- GCC_except_table370
- GCC_except_table376
- GCC_except_table380
- GCC_except_table383
- GCC_except_table387
- GCC_except_table396
- GCC_except_table402
- GCC_except_table412
- GCC_except_table417
- GCC_except_table422
- GCC_except_table423
- GCC_except_table432
- GCC_except_table453
- GCC_except_table464
- GCC_except_table477
- GCC_except_table495
- GCC_except_table518
- GCC_except_table528
- GCC_except_table540
- GCC_except_table56
- GCC_except_table560
- GCC_except_table563
- GCC_except_table589
- GCC_except_table593
- GCC_except_table606
- GCC_except_table614
- GCC_except_table622
- GCC_except_table628
- GCC_except_table633
- GCC_except_table641
- GCC_except_table648
- GCC_except_table658
- GCC_except_table67
- GCC_except_table672
- GCC_except_table686
- GCC_except_table697
- GCC_except_table707
- GCC_except_table721
- GCC_except_table731
- GCC_except_table743
- GCC_except_table762
- GCC_except_table783
- GCC_except_table786
- GCC_except_table82
- GCC_except_table823
- GCC_except_table825
- GCC_except_table827
- GCC_except_table858
- GCC_except_table870
- GCC_except_table872
- GCC_except_table874
- GCC_except_table880
- GCC_except_table884
- GCC_except_table927
- GCC_except_table936
- OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._expectedSetOfTimestampsCommitted
- OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._settingsIDByTimestamp
- OBJC_IVAR_$_AVCapturePersonalPhotographerSessionFinishCoordinator._unmappedExpectedTimestamps
- OBJC_IVAR_$_AVCapturePersonalPhotographerSessionResults._capturedPhotos
- OBJC_IVAR_$_AVCapturePersonalPhotographerSessionResults._systemRecommendedPhotosToDeleteByTimestamp
- OBJC_IVAR_$_AVCapturePersonalPhotographerSessionResults._systemRecommendedPhotosToSaveByTimestamp
- OBJC_IVAR_$_AVControlCenterModuleState._ringLightAutoColorEnabled
- OBJC_IVAR_$_AVControlCenterModuleState._ringLightAutoColorEnabledKey
- OBJC_IVAR_$_AVControlCenterModuleState._ringLightBias
- OBJC_IVAR_$_AVControlCenterModuleState._ringLightBiasKey
- OBJC_IVAR_$_AVControlCenterModuleState._ringLightRecommendedColor
- OBJC_IVAR_$_AVControlCenterModuleState._ringLightRecommendedColorKey
- _AVContinuityCaptureOnBoardingUIButtonClickedNotificationRemindLater
- _AVControlCenterVideoEffectsModuleGetDisplayRingLightColorForBundleID
- _AVControlCenterVideoEffectsModuleGetDisplayRingLightRecommendedNitsFloorForBundleID
- _AVControlCenterVideoEffectsModuleGetRingLightColorRecommendationEnabledForBundleID
- _AVControlCenterVideoEffectsModuleSetDisplayRingLightColorForBundleID
- _AVControlCenterVideoEffectsModuleSetRingLightColorRecommendationEnabledForBundleID
- _AVControlCenterVideoEffectsRingLightAutoColorEnabledPreferenceKey
- _AVControlCenterVideoEffectsRingLightBiasPreferenceKey
- _AVControlCenterVideoEffectsRingLightRecommendedColorPreferenceKey
- _FigCaptureProprietaryDefaultsRingLightAutoColorEnabledKey
- _FigCaptureProprietaryDefaultsRingLightBiasKey
- _FigCaptureProprietaryDefaultsRingLightRecommendedColorKey
- _FigCaptureRingLightAutoColorEnabledDefault
- _FigCaptureRingLightBiasDefault
- _FigCaptureRingLightRecommendedColorDefault
- ___64-[AVControlCenterModuleState installProprietaryDefaultsHandlers]_block_invoke_37
- ___64-[AVControlCenterModuleState installProprietaryDefaultsHandlers]_block_invoke_38
- ___64-[AVControlCenterModuleState installProprietaryDefaultsHandlers]_block_invoke_39
- ___block_descriptor_32_e11_v16?0B8B12l
- ___block_descriptor_53_e8_32o40r_e5_v8?0l
- _objc_msgSend$_addExpectedTimestamp:
- _objc_msgSend$_initWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:
- _objc_msgSend$_isPhotoRegisteredWithTimestampNSValue:
- _objc_msgSend$_updateBravoCameraSelectionBehaviorForSourceDevice:
- _objc_msgSend$continuousAutoFocusTrackingLensPositionBias
- _objc_msgSend$finishWithRequest:expectedTimestamps:error:
- _objc_msgSend$isPhotoRegisteredForDeletionWithTimestamp:
- _objc_msgSend$isPhotoRegisteredWithTimestamp:
- _objc_msgSend$recordStillCompleteForSettingsID:timestamp:
- _objc_msgSend$registerPhotoCapturedWithTimestamp:
- _objc_msgSend$registerPhotoTimestampForDeletion:
- _objc_msgSend$resolvedSettingsWithUniqueID:photoDimensions:rawPhotoDimensions:previewDimensions:embeddedThumbnailDimensions:rawEmbeddedThumbnailDimensions:livePhotoMovieEnabled:livePhotoMovieDimensions:livePhotoAssetIdentifier:portraitEffectsMatteDimensions:hairSegmentationMatteDimensions:skinSegmentationMatteDimensions:teethSegmentationMatteDimensions:glassesSegmentationMatteDimensions:spatialOverCapturePhotoDimensions:turboModeEnabled:flashEnabled:redEyeReductionEnabled:HDREnabled:adjustedPhotoFiltersEnabled:EV0PhotoDeliveryEnabled:stillImageStabilizationEnabled:virtualDeviceFusionEnabled:squareCropEnabled:deferredPhotoProxyDimensions:photoProcessingTimeRange:contentAwareDistortionCorrectionEnabled:spatialPhotoCaptureEnabled:photoManifest:digitalFlashUserInterfaceHints:digitalFlashUserInterfaceRGBEstimate:captureBeforeResolvingSettingsEnabled:secureSigningPhotoCapturePhotoEnabled:
- _objc_msgSend$ringLightAutoColorEnabled
- _objc_msgSend$ringLightRecommendedColor
- _objc_msgSend$setRingLightAutoColorEnabled:
CStrings:
+ "%@: %p deviceID: %d, confidence: %f, deviceType: %d"
+ ", expected: %lu"
+ ", sentToPerceptionThumbnailChannel=%d"
+ "-[AVCaptureFigVideoDevice _drainManualControlRequestQueue:]"
+ "-[AVCaptureFigVideoDevice _handleManualControlCompletionForRequestQueue:withPayload:]"
+ "-[AVCaptureFigVideoDevice _queryPrimaryDisplayRegion]"
+ "-[AVCaptureFigVideoDevice _setExposureWithMode:duration:ISO:lensAperture:requestID:newMaxFrameDuration:]"
+ "-[AVCaptureFigVideoDevice _setFocusWithMode:lensPosition:requestID:]"
+ "-[AVCaptureFigVideoDevice _setWhiteBalanceWithMode:whiteBalanceGains:requestID:featuresEnabled:]"
+ "-[AVCaptureFigVideoDevice setExposureTargetBias:completionHandler:]_block_invoke"
+ "-[AVCapturePersonalPhotographerSessionFinishCoordinator finishWithRequest:expectedSettingsIDs:error:]"
+ "-[AVCapturePersonalPhotographerSessionResults registerPhotoSettingsIDForDeletion:]"
+ "-[AVCapturePersonalPhotographerSessionResults registerPhotoTimestamp:forSettingsID:]"
+ "-[AVCapturePersonalPhotographerSessionResults registerPhotoWithSettingsID:]"
+ "-[AVCaptureProprietaryDefaultsSingleton migrateDefaultsFromAppBundleID:newAppBundleID:]_block_invoke"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] \tFiring completion handler %p for EXACT MATCH request with time %f (cur=%d/completed=%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] \tFiring completion handler %p for earlier (coalesced?) request with time %f (cur=%d/completed=%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] \tFiring completion handler %p for fake bias request with time %f (cur=%d/completed=%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] \tFiring completion handler %p with kCMTimeInvalid due to error %d (cur=%d/completed=%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] \tNot dequeueing request -- it's in the future (cur=%d/completed=%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Enqueued fake bias request %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Failed to query primaryDisplayRegion. Reusing cached value"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] draining request %d from queue %{public}@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] exposure operation: %{public}@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] exposure-target-bias operation: %{public}@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] focus operation: mode %d, lensPosition %f, %{public}@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] white-balance operation: %{public}@"
+ "<<<< AVCaptureMetadataOutput >>>> %s: Face ID Result <rawFrameId: %lu, metadataFrameId: %lu, refFrameId: %lu, frameType: %d, projectorMode: %d>"
+ "<<<< AVCapturePersonalPhotographerSessionResults >>>> %s: Cannot register timestamp for unregistered photo with settingsID %lld"
+ "<<<< AVCapturePersonalPhotographerSessionResults >>>> %s: Could not find photo with settingsID %lld in array of captured photos: %@"
+ "<<<< AVCapturePersonalPhotographerSessionResults >>>> %s: Invalid timestamp for photo with settingsID %lld: %@"
+ "<<<< AVCapturePersonalPhotographerSessionResults >>>> %s: Photo with settingsID %lld already registered for deletion: %@"
+ "<<<< AVCapturePersonalPhotographerSessionResults >>>> %s: Photo with settingsID %lld already registered: %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: %{public}@ Will wait for remaining captures: %{public}@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Missing settings ID for capture to keep: %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Missing settings ID for capture to remove: %@"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Photo to keep with settingsID:%lld pts:%.6fs has already been registered for deletion"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Unknown photo to keep with settingsID:%lld pts:%.6fs"
+ "<<<< AVCapturePhotoOutput >>>> %s: (%p) Unknown photo to remove with settingsID:%lld pts:%.6fs"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: Failed to migrate defaults, error:%d, source:%p"
+ "<<<< AVCaptureSession >>>> %s: (%p) "
+ "<<<< AVCaptureSession >>>> %s: (%p) AVCaptureSession: CMCapture.framework is not loaded. Camera capture requires CMCapture, CMPhoto, and CMImaging frameworks."
+ "<<<< AVCaptureSession >>>> %s: (%p) Updating device orientation %d -> %d"
+ "<<<< AVCaptureSession >>>> %s: (%p) [Routing] (pthread:%p) Not triggering buildAndRunGraph for audioInputRouteIsBuiltInMic change due to in-progress movie recording"
+ "<<<< AVCaptureSession >>>> %s: (%p) [Routing] (pthread:%p) Triggering buildAndRunGraph for audioInputRouteIsBuiltInMic change %{public}@ current audioCaptureMode %ld on input %{public}@"
+ "<<<< AVContinuityCaptureOnBoardingManager >>>> %s: ContinuityCaptureOnBoardingUI SetUpLater clicked. Disabling Wombat on the Mac."
+ "AVCaptureDevicePrimaryDisplayRegionDidChangeNotification"
+ "AVCaptureDeviceTypeBuiltInInnerUltraWideCamera"
+ "AVCaptureDeviceTypeBuiltInOuterUltraWideCamera"
+ "DeviceProximityDetection"
+ "DeviceSupportsTouchSensitiveCameraControl"
+ "LastShownBuild:AVCaptureConnection.m:953"
+ "LastShownBuild:AVCaptureDevice.m:4385"
+ "LastShownBuild:AVCaptureDevice.m:4389"
+ "LastShownBuild:AVCaptureDevice.m:4534"
+ "LastShownBuild:AVCaptureDevice.m:4820"
+ "LastShownBuild:AVCaptureDevice.m:4824"
+ "LastShownBuild:AVCaptureDevice.m:4964"
+ "LastShownBuild:AVCapturePhotoOutput.m:3225"
+ "LastShownBuild:AVCapturePhotoOutput.m:9720"
+ "LastShownBuild:AVCaptureVideoPreviewLayer.m:2342"
+ "LastShownBuild:AVControlCenterModules.m:4551"
+ "LastShownBuild:AVControlCenterModules.m:4555"
+ "LastShownDate:AVCaptureConnection.m:953"
+ "LastShownDate:AVCaptureDevice.m:4385"
+ "LastShownDate:AVCaptureDevice.m:4389"
+ "LastShownDate:AVCaptureDevice.m:4534"
+ "LastShownDate:AVCaptureDevice.m:4820"
+ "LastShownDate:AVCaptureDevice.m:4824"
+ "LastShownDate:AVCaptureDevice.m:4964"
+ "LastShownDate:AVCapturePhotoOutput.m:3225"
+ "LastShownDate:AVCapturePhotoOutput.m:9720"
+ "LastShownDate:AVCaptureVideoPreviewLayer.m:2342"
+ "LastShownDate:AVControlCenterModules.m:4551"
+ "LastShownDate:AVControlCenterModules.m:4555"
+ "LightSourceEstimation"
+ "Not available - use -hasLookingAtCameraConfidence"
+ "Only AVCapturePrimaryConstituentDeviceSwitchingBehaviorAuto is supported as the primaryConstituentDeviceSwitchingBehaviorForRecording on this receiver"
+ "SetUpLater"
+ "Unsupported - check for AVMetadataDeviceProximityDetectionObject in -availableMetadataObjectTypes"
+ "Unsupported - check for AVMetadataLightSourceEstimationObject in -availableMetadataObjectTypes"
+ "Unsupported type found (%@) - use -supportedMetadataObjectTypesForPerceptionThumbnailChannel"
+ "avcmdo_faceIDCollectionForSampleBuffer"
+ "com.apple.private.avfoundation.capture.proprietary-defaults-migration"
+ "com.apple.private.avfoundation.capture.toggle-continuity-capture"
+ "description=CameraCapture_AVF-764.41.11"
+ "mdta/com.apple.quicktime.device-proximity-detection"
+ "mdta/com.apple.quicktime.light-source-estimation"
- ", %lu expected (%lu unmapped)"
- "<<<< AVCapturePhotoOutput >>>> %s: (%p) Photo to keep with timestamp %fs has already been registered for deletion"
- "<<<< AVCapturePhotoOutput >>>> %s: (%p) Unknown photo to keep with timestamp: %fs"
- "<<<< AVCapturePhotoOutput >>>> %s: (%p) Unknown photo to remove with timestamp: %fs"
- "<<<< AVCaptureSession >>>> %s: %p called"
- "<<<< AVCaptureSession >>>> %s: AVCaptureSession: CMCapture.framework is not loaded. Camera capture requires CMCapture, CMPhoto, and CMImaging frameworks."
- "<<<< AVCaptureSession >>>> %s: Updating device orientation %d -> %d"
- "<<<< AVCaptureSession >>>> %s: [Routing] (%p) (thread %p) Not triggering buildAndRunGraph for audioInputRouteIsBuiltInMic change due to in-progress movie recording"
- "<<<< AVCaptureSession >>>> %s: [Routing] (%p) (thread %p) Triggering buildAndRunGraph for audioInputRouteIsBuiltInMic change %{public}@ current audioCaptureMode %ld on input %{public}@"
- "<<<< AVContinuityCaptureOnBoardingManager >>>> %s: ContinuityCaptureOnBoardingUI RemindLater clicked. Delaying Wombats publishing."
- "AVCaptureDeviceTypeBuiltInBostonUltraWideCamera"
- "AVCaptureDeviceTypeBuiltInRenoUltraWideCamera"
- "LastShownBuild:AVCaptureConnection.m:866"
- "LastShownBuild:AVCaptureDevice.m:4362"
- "LastShownBuild:AVCaptureDevice.m:4366"
- "LastShownBuild:AVCaptureDevice.m:4511"
- "LastShownBuild:AVCaptureDevice.m:4807"
- "LastShownBuild:AVCaptureDevice.m:4811"
- "LastShownBuild:AVCaptureDevice.m:4951"
- "LastShownBuild:AVCapturePhotoOutput.m:3224"
- "LastShownBuild:AVCapturePhotoOutput.m:9675"
- "LastShownBuild:AVCaptureVideoPreviewLayer.m:2332"
- "LastShownBuild:AVControlCenterModules.m:4684"
- "LastShownBuild:AVControlCenterModules.m:4688"
- "LastShownDate:AVCaptureConnection.m:866"
- "LastShownDate:AVCaptureDevice.m:4362"
- "LastShownDate:AVCaptureDevice.m:4366"
- "LastShownDate:AVCaptureDevice.m:4511"
- "LastShownDate:AVCaptureDevice.m:4807"
- "LastShownDate:AVCaptureDevice.m:4811"
- "LastShownDate:AVCaptureDevice.m:4951"
- "LastShownDate:AVCapturePhotoOutput.m:3224"
- "LastShownDate:AVCapturePhotoOutput.m:9675"
- "LastShownDate:AVCaptureVideoPreviewLayer.m:2332"
- "LastShownDate:AVControlCenterModules.m:4684"
- "LastShownDate:AVControlCenterModules.m:4688"
- "Out of bounds input argument for ringLightIntensity"
- "RemindLater"
- "description=CameraCapture_AVF-764.21.3"
```
