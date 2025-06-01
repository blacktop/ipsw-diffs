## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-475.31.1.0.0
-  __TEXT.__text: 0xdce6c
-  __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_methlist: 0xb7e0
-  __TEXT.__const: 0x848
-  __TEXT.__gcc_except_tab: 0x1d24
-  __TEXT.__cstring: 0x17713
-  __TEXT.__oslogstring: 0x4706
+477.8.0.0.0
+  __TEXT.__text: 0xded6c
+  __TEXT.__auth_stubs: 0x1860
+  __TEXT.__objc_methlist: 0xbab8
+  __TEXT.__const: 0x860
+  __TEXT.__gcc_except_tab: 0x1d8c
+  __TEXT.__cstring: 0x17bf2
+  __TEXT.__oslogstring: 0x4838
   __TEXT.__dlopen_cstrs: 0x178
-  __TEXT.__unwind_info: 0x38c8
-  __TEXT.__objc_classname: 0x155c
-  __TEXT.__objc_methname: 0x20a82
-  __TEXT.__objc_methtype: 0x3514
-  __TEXT.__objc_stubs: 0x133c0
-  __DATA_CONST.__got: 0x1e70
-  __DATA_CONST.__const: 0x6328
-  __DATA_CONST.__objc_classlist: 0x4d8
+  __TEXT.__unwind_info: 0x37bc
+  __TEXT.__objc_classname: 0x157c
+  __TEXT.__objc_methname: 0x211a8
+  __TEXT.__objc_methtype: 0x3571
+  __TEXT.__objc_stubs: 0x13820
+  __DATA_CONST.__got: 0x1ec8
+  __DATA_CONST.__const: 0x6630
+  __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf608
-  __DATA_CONST.__objc_selrefs: 0x5f48
+  __DATA_CONST.__objc_const: 0xf9a0
+  __DATA_CONST.__objc_selrefs: 0x6070
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_classrefs: 0x790
-  __DATA_CONST.__objc_superrefs: 0x418
-  __DATA_CONST.__objc_arraydata: 0x348
-  __AUTH_CONST.__objc_const: 0x3f40
-  __AUTH_CONST.__cfstring: 0xf420
-  __AUTH_CONST.__objc_intobj: 0x7c8
+  __DATA_CONST.__objc_classrefs: 0x798
+  __DATA_CONST.__objc_superrefs: 0x420
+  __DATA_CONST.__objc_arraydata: 0x388
+  __AUTH_CONST.__objc_const: 0x3fd0
+  __AUTH_CONST.__cfstring: 0xf840
+  __AUTH_CONST.__objc_intobj: 0x7e0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__const: 0x760
   __AUTH_CONST.__objc_arrayobj: 0x258
-  __AUTH_CONST.__auth_got: 0xc30
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x13ac
-  __DATA.__data: 0xcc8
+  __AUTH_CONST.__auth_got: 0xc40
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x1404
+  __DATA.__data: 0xcf8
   __DATA.__common: 0x60
-  __DATA.__bss: 0x300
-  __DATA_DIRTY.__objc_data: 0x2ee0
+  __DATA.__bss: 0x2d0
+  __DATA_DIRTY.__objc_data: 0x2f80
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__common: 0x140
-  __DATA_DIRTY.__bss: 0x390
+  __DATA_DIRTY.__bss: 0x398
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7A9D2EB5-0A39-38D2-9FF1-1C8035FA7EBA
-  Functions: 4667
-  Symbols:   16970
-  CStrings:  9521
+  UUID: 7A5920AF-E765-36AA-B885-DA076E5EE0D7
+  Functions: 4727
+  Symbols:   17175
+  CStrings:  9656
 
Symbols:
+ +[AVMetadataEyeReliefStatusObject eyeReliefStatusObjectWithEyeReliefStatus:input:time:optionalInfoDict:]
+ -[AVCaptureConnection _setVideoRotationAngle:forceUpdate:]
+ -[AVCaptureDevice _setConstantColorEnabled:]
+ -[AVCaptureDevice isAttentionDetectionSupported]
+ -[AVCaptureDeviceFormat isConstantColorSupported]
+ -[AVCaptureFigVideoDevice _setConstantColorEnabled:]
+ -[AVCaptureFigVideoDevice isAttentionDetectionSupported]
+ -[AVCaptureMetadataOutput _detectedObjectsCollectionForSampleBuffer:input:facesArrayOut:need180DegreeMetadataTransform:]
+ -[AVCaptureMetadataOutput _eyeReliefResultCollectionForSampleBuffer:input:]
+ -[AVCaptureMetadataOutput isAttentionDetectionEnabled]
+ -[AVCaptureMetadataOutput isAttentionDetectionSupported]
+ -[AVCaptureMetadataOutput setAttentionDetectionEnabled:]
+ -[AVCapturePhoto constantColorCenterWeightedMeanConfidenceLevel]
+ -[AVCapturePhoto constantColorConfidenceMap]
+ -[AVCapturePhoto initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:]
+ -[AVCapturePhoto isConstantColorFallbackPhoto]
+ -[AVCapturePhotoOutput _updateConstantColorSupportedForSourceDevice:]
+ -[AVCapturePhotoOutput isConstantColorClippingRecoveryEnabled]
+ -[AVCapturePhotoOutput isConstantColorEnabled]
+ -[AVCapturePhotoOutput isConstantColorSaturationBoostEnabled]
+ -[AVCapturePhotoOutput isConstantColorSupported]
+ -[AVCapturePhotoOutput setConstantColorClippingRecoveryEnabled:]
+ -[AVCapturePhotoOutput setConstantColorEnabled:]
+ -[AVCapturePhotoOutput setConstantColorSaturationBoostEnabled:]
+ -[AVCapturePhotoSettings isConstantColorEnabled]
+ -[AVCapturePhotoSettings isConstantColorFallbackPhotoDeliveryEnabled]
+ -[AVCapturePhotoSettings setConstantColorEnabled:]
+ -[AVCapturePhotoSettings setConstantColorFallbackPhotoDeliveryEnabled:]
+ -[AVCaptureSession _updateConstantColorEnabledForAllConnectedSourceDevices]
+ -[AVCaptureSession _updateConstantColorEnabledForSourceDevice:]
+ -[AVMetadataEyeReliefStatusObject copyWithZone:]
+ -[AVMetadataEyeReliefStatusObject description]
+ -[AVMetadataEyeReliefStatusObject distance]
+ -[AVMetadataEyeReliefStatusObject eyeReliefStatus]
+ -[AVMetadataEyeReliefStatusObject hasDistance]
+ -[AVMetadataEyeReliefStatusObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:]
+ -[AVMetadataEyeReliefStatusObject initWithEyeReliefStatus:time:sourceCaptureInput:optionalInfoDict:]
+ -[AVMetadataFaceObject distance]
+ -[AVMetadataFaceObject hasDistance]
+ -[AVMetadataFaceObject hasOrientation]
+ -[AVMetadataFaceObject hasPayingAttentionConfidence]
+ -[AVMetadataFaceObject hasPayingAttention]
+ -[AVMetadataFaceObject orientation]
+ -[AVMetadataFaceObject payingAttentionConfidence]
+ -[AVMetadataFaceObject payingAttention]
+ -[AVMetadataFaceObjectInternal distance]
+ -[AVMetadataFaceObjectInternal hasDistance]
+ -[AVMetadataFaceObjectInternal hasOrientation]
+ -[AVMetadataFaceObjectInternal hasPayingAttentionConfidence]
+ -[AVMetadataFaceObjectInternal hasPayingAttention]
+ -[AVMetadataFaceObjectInternal orientation]
+ -[AVMetadataFaceObjectInternal payingAttentionConfidence]
+ -[AVMetadataFaceObjectInternal payingAttention]
+ -[AVMetadataFaceObjectInternal setDistance:]
+ -[AVMetadataFaceObjectInternal setHasDistance:]
+ -[AVMetadataFaceObjectInternal setHasOrientation:]
+ -[AVMetadataFaceObjectInternal setHasPayingAttention:]
+ -[AVMetadataFaceObjectInternal setHasPayingAttentionConfidence:]
+ -[AVMetadataFaceObjectInternal setOrientation:]
+ -[AVMetadataFaceObjectInternal setPayingAttention:]
+ -[AVMetadataFaceObjectInternal setPayingAttentionConfidence:]
+ GCC_except_table145
+ GCC_except_table20
+ GCC_except_table214
+ GCC_except_table250
+ GCC_except_table284
+ GCC_except_table288
+ GCC_except_table435
+ GCC_except_table598
+ GCC_except_table600
+ GCC_except_table602
+ GCC_except_table625
+ GCC_except_table637
+ GCC_except_table639
+ GCC_except_table641
+ GCC_except_table647
+ GCC_except_table649
+ GCC_except_table690
+ GCC_except_table694
+ GCC_except_table744
+ GCC_except_table787
+ _AVCaptureDeviceTypeBuiltInInfraredMetadataCamera
+ _AVGQCaptureAttentionDetectionSupported
+ _AVMetadataObjectTypeEyeReliefStatus
+ _FigCapturePlatformSupportsExclaves
+ _J507_J508_J537_J538
+ _J717_J718_J720_J721
+ _OBJC_CLASS_$_AVMetadataEyeReliefStatusObject
+ _OBJC_IVAR_$_AVCaptureDeviceFormatInternal.constantColorSupported
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._constantColorEnabled
+ _OBJC_IVAR_$_AVCaptureMetadataOutputInternal.attentionDetectionEnabled
+ _OBJC_IVAR_$_AVCapturePhotoInternal.constantColorCenterWeightedMeanConfidenceLevel
+ _OBJC_IVAR_$_AVCapturePhotoInternal.constantColorConfidenceMap
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.constantColorClippingRecoveryEnabled
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.constantColorEnabled
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.constantColorSaturationBoostEnabled
+ _OBJC_IVAR_$_AVCapturePhotoOutputInternal.constantColorSupported
+ _OBJC_IVAR_$_AVCapturePhotoSettingsInternal.constantColorEnabled
+ _OBJC_IVAR_$_AVCapturePhotoSettingsInternal.constantColorFallbackPhotoDeliveryEnabled
+ _OBJC_IVAR_$_AVMetadataEyeReliefStatusObject._distance
+ _OBJC_IVAR_$_AVMetadataEyeReliefStatusObject._eyeReliefStatus
+ _OBJC_IVAR_$_AVMetadataEyeReliefStatusObject._hasDistance
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._distance
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._hasDistance
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._hasOrientation
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._hasPayingAttention
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._hasPayingAttentionConfidence
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._orientation
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._payingAttention
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._payingAttentionConfidence
+ _OBJC_METACLASS_$_AVMetadataEyeReliefStatusObject
+ __OBJC_$_CLASS_METHODS_AVMetadataEyeReliefStatusObject
+ __OBJC_$_INSTANCE_METHODS_AVMetadataEyeReliefStatusObject
+ __OBJC_$_INSTANCE_VARIABLES_AVMetadataEyeReliefStatusObject
+ __OBJC_$_PROP_LIST_AVMetadataEyeReliefStatusObject
+ __OBJC_CLASS_PROTOCOLS_$_AVMetadataEyeReliefStatusObject
+ __OBJC_CLASS_RO_$_AVMetadataEyeReliefStatusObject
+ __OBJC_METACLASS_RO_$_AVMetadataEyeReliefStatusObject
+ ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke.401
+ ___52-[AVCaptureFigVideoDevice _setConstantColorEnabled:]_block_invoke
+ ___58-[AVCaptureConnection _setVideoRotationAngle:forceUpdate:]_block_invoke
+ ___block_literal_global.1231
+ ___block_literal_global.1238
+ ___block_literal_global.135
+ ___block_literal_global.161
+ ___block_literal_global.165
+ ___block_literal_global.170
+ ___block_literal_global.417
+ ___block_literal_global.481
+ ___block_literal_global.489
+ ___block_literal_global.671
+ __unnamed_array_storage.220
+ __unnamed_array_storage.271
+ __unnamed_array_storage.283
+ __unnamed_array_storage.292
+ __unnamed_array_storage.343
+ __unnamed_array_storage.358
+ __unnamed_array_storage.414
+ __unnamed_array_storage.470
+ __unnamed_array_storage.512
+ __unnamed_array_storage.515
+ __unnamed_array_storage.527
+ __unnamed_array_storage.530
+ __unnamed_array_storage.539
+ __unnamed_array_storage.542
+ _getFBSOrientationObserverClass
+ _kFigCaptureSampleBufferAttachmentKey_EyeReliefResult
+ _kFigCaptureSessionNotificationPayloadKey_ConstantColorConfidenceMapSurface
+ _kFigCaptureSessionNotificationPayloadKey_ConstantColorMetadata
+ _kFigCaptureSourceAttributeKey_AttentionDetectionSupported
+ _kFigCaptureStreamMetadata_Attention
+ _kFigCaptureStreamMetadata_AttentionConfidenceLevel
+ _kFigCaptureStreamMetadata_FaceDistance
+ _kFigCaptureStreamMetadata_FaceOrientation
+ _kFigCaptureStreamSecureEyeReliefResultKey_Distance
+ _kFigCaptureStreamSecureEyeReliefResultKey_Status
+ _kFigConstantColorMetadataAttachmentKey_CenterWeightedMeanConfidenceLevel
+ _objc_msgSend$_detectedObjectsCollectionForSampleBuffer:input:facesArrayOut:need180DegreeMetadataTransform:
+ _objc_msgSend$_eyeReliefResultCollectionForSampleBuffer:input:
+ _objc_msgSend$_setConstantColorEnabled:
+ _objc_msgSend$_setVideoRotationAngle:forceUpdate:
+ _objc_msgSend$_updateConstantColorEnabledForAllConnectedSourceDevices
+ _objc_msgSend$_updateConstantColorEnabledForSourceDevice:
+ _objc_msgSend$_updateConstantColorSupportedForSourceDevice:
+ _objc_msgSend$distance
+ _objc_msgSend$eyeReliefStatus
+ _objc_msgSend$eyeReliefStatusObjectWithEyeReliefStatus:input:time:optionalInfoDict:
+ _objc_msgSend$hasDistance
+ _objc_msgSend$hasOrientation
+ _objc_msgSend$hasPayingAttention
+ _objc_msgSend$hasPayingAttentionConfidence
+ _objc_msgSend$initWithEyeReliefStatus:time:sourceCaptureInput:optionalInfoDict:
+ _objc_msgSend$initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:
+ _objc_msgSend$isAttentionDetectionEnabled
+ _objc_msgSend$isAttentionDetectionSupported
+ _objc_msgSend$isConstantColorClippingRecoveryEnabled
+ _objc_msgSend$isConstantColorEnabled
+ _objc_msgSend$isConstantColorFallbackPhotoDeliveryEnabled
+ _objc_msgSend$isConstantColorSaturationBoostEnabled
+ _objc_msgSend$isConstantColorSupported
+ _objc_msgSend$orientation
+ _objc_msgSend$payingAttention
+ _objc_msgSend$payingAttentionConfidence
+ _objc_msgSend$setAttentionDetectionEnabled:
+ _objc_msgSend$setConstantColorClippingRecoveryEnabled:
+ _objc_msgSend$setConstantColorEnabled:
+ _objc_msgSend$setConstantColorFallbackPhotoDeliveryEnabled:
+ _objc_msgSend$setConstantColorSaturationBoostEnabled:
+ _objc_msgSend$setDistance:
+ _objc_msgSend$setHasDistance:
+ _objc_msgSend$setHasOrientation:
+ _objc_msgSend$setHasPayingAttention:
+ _objc_msgSend$setHasPayingAttentionConfidence:
+ _objc_msgSend$setPayingAttention:
+ _objc_msgSend$setPayingAttentionConfidence:
+ _objc_retain_x26
- -[AVCaptureConnection _setVideoRotationAngle:]
- -[AVCaptureMetadataOutput _detectedObjectsCollectionForSampleBuffer:input:facesArrayOut:]
- -[AVCapturePhoto initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:]
- GCC_except_table207
- GCC_except_table208
- GCC_except_table243
- GCC_except_table276
- GCC_except_table280
- GCC_except_table3
- GCC_except_table433
- GCC_except_table595
- GCC_except_table597
- GCC_except_table599
- GCC_except_table622
- GCC_except_table634
- GCC_except_table636
- GCC_except_table638
- GCC_except_table644
- GCC_except_table646
- GCC_except_table687
- GCC_except_table691
- GCC_except_table741
- GCC_except_table784
- ___46-[AVCaptureConnection _setVideoRotationAngle:]_block_invoke
- ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke.398
- ___block_literal_global.1220
- ___block_literal_global.1227
- ___block_literal_global.131
- ___block_literal_global.154
- ___block_literal_global.162
- ___block_literal_global.167
- ___block_literal_global.414
- ___block_literal_global.478
- ___block_literal_global.483
- ___block_literal_global.669
- __unnamed_array_storage.208
- __unnamed_array_storage.247
- __unnamed_array_storage.259
- __unnamed_array_storage.268
- __unnamed_array_storage.319
- __unnamed_array_storage.334
- __unnamed_array_storage.407
- __unnamed_array_storage.463
- __unnamed_array_storage.505
- __unnamed_array_storage.508
- __unnamed_array_storage.520
- __unnamed_array_storage.523
- __unnamed_array_storage.532
- __unnamed_array_storage.535
- _objc_msgSend$_detectedObjectsCollectionForSampleBuffer:input:facesArrayOut:
- _objc_msgSend$_setVideoRotationAngle:
- _objc_msgSend$initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:
CStrings:
+ " constant-color:1%@"
+ " constantColorConfidence:%p"
+ "%@: %p eyeReliefStatus: %d, distance: %f"
+ "(fallback:1)"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: %{public}@ Device is face-up or face-down. Falling back to active interface orientation %d for the initial videoRotationAngleForHorizonLevelCapture value"
+ "<<<< AVCaptureDeviceRotationCoordinator >>>> %s: %{public}@ Unexpected initial device orientation: %d!"
+ "@244@0:8{?=qiIq}16^{__IOSurface=}40Q48@56^{__IOSurface=}64^{__IOSurface=}72@80^{__IOSurface=}88@96^{__IOSurface=}104@112^{__IOSurface=}120@128^{__IOSurface=}136@144^{__IOSurface=}152@160^{__IOSurface=}168@176^{__IOSurface=}184@192@200@208Q216Q224I232@236"
+ "@44@0:8^{opaqueCMSampleBuffer=}16@24^@32B40"
+ "@64@0:8Q16@24{?=qiIq}32@56"
+ "@64@0:8Q16{?=qiIq}24@48@56"
+ "AVCaptureDeviceTypeBuiltInInfraredMetadataCamera"
+ "AVGQCaptureAttentionDetectionSupported"
+ "AVMetadataEyeReliefStatusObject"
+ "Constant color is not supported in the current configuration"
+ "EyeReliefStatus"
+ "IRM"
+ "InfraredMetadata"
+ "J507"
+ "J507-J508-J537-J538"
+ "J508"
+ "J537"
+ "J538"
+ "J717"
+ "J717-J718-J720-J721"
+ "J718"
+ "J720"
+ "J721"
+ "Not available - use -hasDistance"
+ "Not available - use -hasOrientation"
+ "Not available - use -hasPayingAttention"
+ "Not available - use -hasPayingAttentionConfidence"
+ "TB,N,V_hasDistance"
+ "TB,N,V_hasOrientation"
+ "TB,N,V_hasPayingAttention"
+ "TB,N,V_hasPayingAttentionConfidence"
+ "TB,N,V_payingAttention"
+ "TQ,N,V_orientation"
+ "Td,N,V_distance"
+ "Td,N,V_payingAttentionConfidence"
+ "Unsupported - use -isAttentionDetectionSupported"
+ "When capturing a raw photo, settings.constantColorEnabled must be set to NO"
+ "_constantColorEnabled"
+ "_detectedObjectsCollectionForSampleBuffer:input:facesArrayOut:need180DegreeMetadataTransform:"
+ "_distance"
+ "_eyeReliefResultCollectionForSampleBuffer:input:"
+ "_eyeReliefStatus"
+ "_hasDistance"
+ "_hasOrientation"
+ "_hasPayingAttention"
+ "_hasPayingAttentionConfidence"
+ "_payingAttention"
+ "_payingAttentionConfidence"
+ "_setConstantColorEnabled:"
+ "_setVideoRotationAngle:forceUpdate:"
+ "_updateConstantColorEnabledForAllConnectedSourceDevices"
+ "_updateConstantColorEnabledForSourceDevice:"
+ "_updateConstantColorSupportedForSourceDevice:"
+ "attentionDetectionEnabled"
+ "constantColorCenterWeightedMeanConfidenceLevel"
+ "constantColorClippingRecoveryEnabled"
+ "constantColorConfidenceMap"
+ "constantColorEnabled"
+ "constantColorFallbackPhotoDeliveryEnabled"
+ "constantColorSaturationBoostEnabled"
+ "constantColorSupported"
+ "description=CameraCapture_AVF-477.8"
+ "distance"
+ "eyeReliefStatus"
+ "eyeReliefStatusObjectWithEyeReliefStatus:input:time:optionalInfoDict:"
+ "hasDistance"
+ "hasOrientation"
+ "hasPayingAttention"
+ "hasPayingAttentionConfidence"
+ "iOS 17.4"
+ "initWithEyeReliefStatus:time:sourceCaptureInput:optionalInfoDict:"
+ "initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:constantColorConfidenceMapSurface:constantColorMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:"
+ "isAttentionDetectionEnabled"
+ "isAttentionDetectionSupported"
+ "isConstantColorClippingRecoveryEnabled"
+ "isConstantColorEnabled"
+ "isConstantColorFallbackPhoto"
+ "isConstantColorFallbackPhotoDeliveryEnabled"
+ "isConstantColorSaturationBoostEnabled"
+ "isConstantColorSupported"
+ "mdta/com.apple.quicktime.eye-relief-status"
+ "payingAttention"
+ "payingAttentionConfidence"
+ "setAttentionDetectionEnabled:"
+ "setConstantColorClippingRecoveryEnabled:"
+ "setConstantColorEnabled:"
+ "setConstantColorFallbackPhotoDeliveryEnabled:"
+ "setConstantColorSaturationBoostEnabled:"
+ "setDistance:"
+ "setHasDistance:"
+ "setHasOrientation:"
+ "setHasPayingAttention:"
+ "setHasPayingAttentionConfidence:"
+ "setPayingAttention:"
+ "setPayingAttentionConfidence:"
+ "settings.constantColorEnabled must be NO if settings.virtualDeviceConstituentPhotoDeliveryEnabledDevices is a non-empty array"
+ "settings.flashMode must be AVCaptureFlashModeOn or AVCaptureFlashModeAuto if settings.isConstantColorEnabled is YES"
+ "settings.isConstantColorEnabled must be NO if self.isConstantColorEnabled is NO"
+ "settings.isConstantColorEnabled must be YES if settings.isConstantColorFallbackPhotoDeliveryEnabled is YES"
+ "v28@0:8d16B24"
- "@228@0:8{?=qiIq}16^{__IOSurface=}40Q48@56^{__IOSurface=}64^{__IOSurface=}72@80^{__IOSurface=}88@96^{__IOSurface=}104@112^{__IOSurface=}120@128^{__IOSurface=}136@144^{__IOSurface=}152@160^{__IOSurface=}168@176@184@192Q200Q208I216@220"
- "@40@0:8^{opaqueCMSampleBuffer=}16@24^@32"
- "_detectedObjectsCollectionForSampleBuffer:input:facesArrayOut:"
- "_setVideoRotationAngle:"
- "description=CameraCapture_AVF-475.31.1"
- "initWithTimestamp:photoSurface:photoSurfaceSize:processedFileType:previewPhotoSurface:embeddedThumbnailSourceSurface:metadata:depthDataSurface:depthMetadataDictionary:portraitEffectsMatteSurface:portraitEffectsMatteMetadataDictionary:hairSegmentationMatteSurface:hairSegmentationMatteMetadataDictionary:skinSegmentationMatteSurface:skinSegmentationMatteMetadataDictionary:teethSegmentationMatteSurface:teethSegmentationMatteMetadataDictionary:glassesSegmentationMatteSurface:glassesSegmentationMatteMetadataDictionary:captureRequest:bracketSettings:sequenceCount:photoCount:expectedPhotoProcessingFlags:sourceDeviceType:"

```
