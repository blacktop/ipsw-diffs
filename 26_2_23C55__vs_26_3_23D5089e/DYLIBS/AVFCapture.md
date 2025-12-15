## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-664.62.12.0.0
-  __TEXT.__text: 0x11f2a8
-  __TEXT.__auth_stubs: 0x1ff0
-  __TEXT.__objc_methlist: 0xf0ac
-  __TEXT.__const: 0xb72
-  __TEXT.__gcc_except_tab: 0x2760
-  __TEXT.__cstring: 0x201e9
-  __TEXT.__oslogstring: 0x8226
+665.80.6.0.0
+  __TEXT.__text: 0x1729cc
+  __TEXT.__auth_stubs: 0x2040
+  __TEXT.__objc_methlist: 0xf0bc
+  __TEXT.__const: 0xba2
+  __TEXT.__gcc_except_tab: 0x2bac
+  __TEXT.__cstring: 0x2b7c9
+  __TEXT.__oslogstring: 0x22b98
   __TEXT.__dlopen_cstrs: 0x21e
   __TEXT.__ustring: 0x54
   __TEXT.__swift5_typeref: 0xf7

   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x4c60
-  __TEXT.__objc_classname: 0x1996
-  __TEXT.__objc_methname: 0x2aa0b
+  __TEXT.__unwind_info: 0x4e40
+  __TEXT.__objc_classname: 0x1998
+  __TEXT.__objc_methname: 0x2aafb
   __TEXT.__objc_methtype: 0x4080
-  __TEXT.__objc_stubs: 0x18bc0
-  __DATA_CONST.__got: 0x2a90
-  __DATA_CONST.__const: 0x7ce0
+  __TEXT.__objc_stubs: 0x18e20
+  __DATA_CONST.__got: 0x2aa0
+  __DATA_CONST.__const: 0x7df0
   __DATA_CONST.__objc_classlist: 0x5e0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7b68
+  __DATA_CONST.__objc_selrefs: 0x7bd0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x510
   __DATA_CONST.__objc_arraydata: 0x470
-  __AUTH_CONST.__auth_got: 0x1008
-  __AUTH_CONST.__const: 0xcb0
-  __AUTH_CONST.__cfstring: 0x145a0
+  __AUTH_CONST.__auth_got: 0x1030
+  __AUTH_CONST.__const: 0xcd0
+  __AUTH_CONST.__cfstring: 0x14f60
   __AUTH_CONST.__objc_const: 0x18988
   __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_doubleobj: 0x10

   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x1a60
   __DATA.__data: 0xd70
+  __DATA.__common: 0x300
   __DATA.__bss: 0x910
-  __DATA.__common: 0x100
   __DATA_DIRTY.__objc_data: 0x2fd0
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__common: 0x1c0
+  __DATA_DIRTY.__common: 0x2b0
   __DATA_DIRTY.__bss: 0x3d0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVRouting.framework/AVRouting

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 758D6CE7-543C-309E-B569-3E79A971AA9B
-  Functions: 6465
-  Symbols:   22739
-  CStrings:  12672
+  UUID: 5EBD320E-76BE-3E52-85D3-C26F28B5D2BD
+  Functions: 6541
+  Symbols:   23005
+  CStrings:  14605
 
Symbols:
+ +[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:].cold.1
+ +[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:].cold.2
+ +[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:].cold.3
+ +[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:].cold.4
+ +[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:].cold.5
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
+ -[AVCaptureDeferredPhotoSettings initWithCoder:].cold.1
+ -[AVCaptureDeferredPhotoSettings initWithCoder:].cold.2
+ -[AVCaptureDeviceRotationCoordinator _updateVideoRotationAngleForHorizonLevelPreview].cold.3
+ -[AVCaptureMovieFileOutput _totalNANDBandwidthAllowed:videoCodecType:].cold.1
+ -[AVCaptureMovieFileOutput startRecordingMovieWithSettings:delegate:].cold.3
+ -[AVCaptureMovieFileOutput startRecordingToOutputFileURL:recordingDelegate:].cold.2
+ -[AVCaptureMultiCamSession _updateSystemPressureCost].cold.1
+ -[AVCaptureOutputInternal .cxx_destruct]
+ -[AVCapturePhoto _fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:replacementPortraitEffectsMatte:replacementHairSegmentationMatte:replacementSkinSegmentationMatte:replacementTeethSegmentationMatte:replacementGlassesSegmentationMatte:replacementRawCompressionSettings:exceptionReason:].cold.1
+ -[AVCaptureSession handleControlsOverlay:didChangeActiveControl:].cold.1
+ -[AVCaptureSession handleControlsOverlay:didChangeFocusLocked:].cold.1
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
+ -[AVPortraitEffectsMatte dictionaryRepresentationForAuxiliaryDataType:].cold.1
+ -[AVPortraitEffectsMatte dictionaryRepresentationForAuxiliaryDataType:].cold.2
+ -[AVPortraitEffectsMatte portraitEffectsMatteByApplyingExifOrientation:].cold.1
+ -[AVSemanticSegmentationMatte dictionaryRepresentationForAuxiliaryDataType:].cold.1
+ -[AVSemanticSegmentationMatte dictionaryRepresentationForAuxiliaryDataType:].cold.2
+ -[AVSemanticSegmentationMatte semanticSegmentationMatteByApplyingExifOrientation:].cold.1
+ -[AVVirtualCaptureCard capacity].cold.1
+ -[AVVirtualCaptureCard freeSpace].cold.1
+ -[AVVirtualCaptureCard showSystemUserInterface].cold.1
+ GCC_except_table109
+ GCC_except_table112
+ GCC_except_table115
+ GCC_except_table116
+ GCC_except_table12
+ GCC_except_table138
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table166
+ GCC_except_table176
+ GCC_except_table180
+ GCC_except_table183
+ GCC_except_table193
+ GCC_except_table197
+ GCC_except_table203
+ GCC_except_table205
+ GCC_except_table210
+ GCC_except_table212
+ GCC_except_table218
+ GCC_except_table219
+ GCC_except_table220
+ GCC_except_table222
+ GCC_except_table224
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table69
+ GCC_except_table75
+ GCC_except_table77
+ GCC_except_table915
+ GCC_except_table93
+ _FigKTraceInit
+ _FigSignalErrorAt3
+ _IOSurfaceGetID
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_NSDateFormatter
+ ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke.216
+ ___104-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForWrapper:withPayload:demoof:addMetadata:]_block_invoke.181
+ ___110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke.215
+ ___110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke.216
+ ___113-[AVCaptureStillImageOutput prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:]_block_invoke.176
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
+ ___43-[AVCaptureFigVideoDevice setExposureMode:]_block_invoke.467
+ ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke.507
+ ___54+[AVCaptureDevice continuityCaptureCameraCapabilities]_block_invoke.645
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.724
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.735
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.735.cold.1
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.737
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.742
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.745
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.753
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.762
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.766
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.767
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.772
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.774
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.779
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.781
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.786
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.792
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.797
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.725
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.741
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.743
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.746
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.754
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.771
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.773
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.778
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.780
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.785
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.790
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.796
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.726
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.744
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.755
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.791
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.730
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.731
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_6.732
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_7.733
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_8.734
+ ___56-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]_block_invoke.665
+ ___58-[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:]_block_invoke.358
+ ___63+[AVCaptureDevice requestAccessForMediaType:completionHandler:]_block_invoke.237
+ ___63-[AVCaptureSession handleControlsOverlay:didChangeFocusLocked:]_block_invoke.cold.1
+ ___65-[AVCaptureSession handleControlsOverlay:didChangeActiveControl:]_block_invoke.cold.1
+ ___66-[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:]_block_invoke.29
+ ___67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.347
+ ___67-[AVCaptureFigVideoDevice setDynamicAspectRatio:completionHandler:]_block_invoke.818
+ ___67-[AVCaptureFigVideoDevice setExposureTargetBias:completionHandler:]_block_invoke.487
+ ___68-[AVCaptureSession handleControlsOverlay:didChangeInterfaceReduced:]_block_invoke.cold.1
+ ___72-[AVCaptureFigVideoDevice chromaticityValuesForDeviceWhiteBalanceGains:]_block_invoke.540
+ ___72-[AVCapturePhotoOutput setPreparedPhotoSettingsArray:completionHandler:]_block_invoke.207
+ ___74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.718
+ ___75-[AVCaptureFigVideoDevice _handleLiveReconfigurationCompletionWithPayload:]_block_invoke.819
+ ___76-[AVCaptureSession handleControlsOverlay:didChangeVisibility:activeControl:]_block_invoke.cold.1
+ ___80-[AVCaptureFigVideoDevice setFocusModeLockedWithLensPosition:completionHandler:]_block_invoke.454
+ ___83-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke.482
+ ___85-[AVCapturePhotoOutput _handleStillImageCompleteNotification:withPayload:forRequest:]_block_invoke.839
+ ___85-[AVCapturePhotoOutput _handleStillImageCompleteNotification:withPayload:forRequest:]_block_invoke.840
+ ___86-[AVCaptureMovieFileOutput handleDidStartRecordingNotificationForWrapper:withPayload:]_block_invoke.172
+ ___94-[AVCapturePhotoOutput commitMomentCaptureWithUniqueID:toMovieRecordingWithSettings:delegate:]_block_invoke.426
+ ___95-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:isSettingExposureModeCustom:]_block_invoke.362
+ ___98-[AVCaptureFigVideoDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:]_block_invoke.538
+ ___AVControlCenterModulesPrewarm_block_invoke.527
+ ____registerVideoDevicesOnce_block_invoke.1532
+ ___block_descriptor_32_e28_"NSString"16?0"NSString"8l
+ ___block_descriptor_32_e48_"NSMutableString"16?0"AVCaptureDeviceFormat"8l
+ ___block_descriptor_40_e8_32b_e41_"NSMutableString"16?0"AVCaptureInput"8ls32l8
+ ___block_descriptor_40_e8_32b_e45_"NSMutableString"16?0"AVCaptureInputPort"8ls32l8
+ ___block_descriptor_40_e8_32o_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32r_e18_"NSString"16?08lr32l8
+ ___block_descriptor_48_e8_32o40b_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_48_e8_32o40b_e8_v12?0C8ls32l8s40l8
+ ___block_descriptor_64_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_65_e8_32o40o48r_e5_v8?0ls32l8s40l8r48l8
+ ___block_descriptor_74_e8_32o40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_80_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32o40o48o56o64r72r80r_e5_v8?0lr64l8s32l8r72l8s40l8s48l8s56l8r80l8
+ ___block_literal_global.1127
+ ___block_literal_global.1129
+ ___block_literal_global.1134
+ ___block_literal_global.123
+ ___block_literal_global.139
+ ___block_literal_global.144
+ ___block_literal_global.1524
+ ___block_literal_global.1531
+ ___block_literal_global.1534
+ ___block_literal_global.160
+ ___block_literal_global.163
+ ___block_literal_global.1716
+ ___block_literal_global.201
+ ___block_literal_global.228
+ ___block_literal_global.283
+ ___block_literal_global.337
+ ___block_literal_global.376
+ ___block_literal_global.520
+ ___block_literal_global.529
+ ___block_literal_global.530
+ ___block_literal_global.554
+ ___block_literal_global.581
+ ___block_literal_global.638
+ ___block_literal_global.647
+ _audit_token_to_pid
+ _avcmcs_computeSystemPressureCost.allSlopes
+ _avcmcs_computeSystemPressureCost.sSlopeIndicesOnce
+ _avcp_copyCGImageForUncompressedBuffer.cold.1
+ _avcp_copyDNGFileDataRepresentationForSushiRawBuffer.cold.1
+ _avcp_copyTIFFFileDataRepresentationForImage.cold.1
+ _avcp_copyTIFFFileDataRepresentationForImage.cold.2
+ _avcp_copyTIFFFileDataRepresentationForImage.cold.3
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
+ _kdebug_trace
+ _objc_msgSend$_metadataConstantValueToName:
+ _objc_msgSend$cinematicAudioSettings
+ _objc_msgSend$dotString
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$metadataObjectsDelegate
+ _objc_msgSend$nonretainedObjectValue
+ _objc_msgSend$now
+ _objc_msgSend$previewHeight
+ _objc_msgSend$previewWidth
+ _objc_msgSend$rawThumbnailHeight
+ _objc_msgSend$rawThumbnailWidth
+ _objc_msgSend$sampleBufferDelegate
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$spiDebugDescription
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$thumbnailContentsDelegate
+ _objc_msgSend$thumbnailHeight
+ _objc_msgSend$thumbnailWidth
+ _objc_msgSend$writeToFile:atomically:encoding:error:
+ _objc_storeWeak
+ _vpl_pointToString
+ _vpl_rectValueToString
+ _vpl_sizeToString
- -[AVCaptureMetadataOutput _emitCollections:].cold.1
- -[AVCapturePhoto portraitEffectsMatte].cold.1
- -[AVCaptureSession _createFigCaptureSession].cold.2
- -[AVCaptureSpatialAudioMetadataSampleGenerator init].cold.1
- -[AVOfflineVideoStabilizer _copyStabilizedSampleBuffer:].cold.1
- -[AVOfflineVideoStabilizer _setupVISProcessor].cold.4
- GCC_except_table104
- GCC_except_table127
- GCC_except_table140
- GCC_except_table154
- GCC_except_table155
- GCC_except_table16
- GCC_except_table163
- GCC_except_table169
- GCC_except_table171
- GCC_except_table172
- GCC_except_table173
- GCC_except_table175
- GCC_except_table179
- GCC_except_table185
- GCC_except_table192
- GCC_except_table199
- GCC_except_table201
- GCC_except_table208
- GCC_except_table211
- GCC_except_table213
- GCC_except_table29
- GCC_except_table37
- GCC_except_table39
- GCC_except_table87
- GCC_except_table92
- GCC_except_table98
- GCC_except_table99
- _FigSignalErrorAtGM
- _OUTLINED_FUNCTION_12
- ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_25
- ___104-[AVCaptureMovieFileOutput handleDidStopRecordingNotificationForWrapper:withPayload:demoof:addMetadata:]_block_invoke_2
- ___110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke_2
- ___110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke_3
- ___113-[AVCaptureStillImageOutput prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:]_block_invoke_3
- ___132-[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:]_block_invoke_2
- ___43-[AVCaptureFigVideoDevice setExposureMode:]_block_invoke_2
- ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke.504
- ___54+[AVCaptureDevice continuityCaptureCameraCapabilities]_block_invoke_3
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.751
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
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_43
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_44
- ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_9
- ___56-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]_block_invoke.656
- ___58-[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:]_block_invoke_2
- ___63+[AVCaptureDevice requestAccessForMediaType:completionHandler:]_block_invoke_2
- ___66-[AVCaptureProprietaryDefaultsSingleton setObject:forWildcardKey:]_block_invoke_2
- ___67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.345
- ___67-[AVCaptureFigVideoDevice setDynamicAspectRatio:completionHandler:]_block_invoke_5
- ___67-[AVCaptureFigVideoDevice setExposureTargetBias:completionHandler:]_block_invoke_2
- ___72-[AVCaptureFigVideoDevice chromaticityValuesForDeviceWhiteBalanceGains:]_block_invoke_3
- ___72-[AVCapturePhotoOutput setPreparedPhotoSettingsArray:completionHandler:]_block_invoke_3
- ___74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.709
- ___74-[AVCaptureProprietaryDefaultsSingleton imageForKey:fillWidth:fillHeight:]_block_invoke.cold.5
- ___75-[AVCaptureFigVideoDevice _handleLiveReconfigurationCompletionWithPayload:]_block_invoke_2
- ___80-[AVCaptureFigVideoDevice setFocusModeLockedWithLensPosition:completionHandler:]_block_invoke_3
- ___83-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke_3
- ___85-[AVCapturePhotoOutput _handleStillImageCompleteNotification:withPayload:forRequest:]_block_invoke_2
- ___85-[AVCapturePhotoOutput _handleStillImageCompleteNotification:withPayload:forRequest:]_block_invoke_3
- ___86-[AVCaptureMovieFileOutput handleDidStartRecordingNotificationForWrapper:withPayload:]_block_invoke_2
- ___94-[AVCapturePhotoOutput commitMomentCaptureWithUniqueID:toMovieRecordingWithSettings:delegate:]_block_invoke_3
- ___95-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:isSettingExposureModeCustom:]_block_invoke.359
- ___98-[AVCaptureFigVideoDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:]_block_invoke_3
- ___AVControlCenterModulesPrewarm_block_invoke.523
- ____registerVideoDevicesOnce_block_invoke.1528
- ___block_descriptor_32_e17_v16?0"NSError"8l
- ___block_descriptor_40_e8_32b_e8_v12?0B8ls32l8
- ___block_descriptor_40_e8_32b_e8_v12?0C8ls32l8
- ___block_descriptor_65_e8_32o40o48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_74_e8_32o40r_e5_v8?0lr40l8s32l8
- ___block_descriptor_80_e8_32o40o48o56r64r72r_e5_v8?0lr56l8s32l8r64l8s40l8s48l8r72l8
- ___block_literal_global.122
- ___block_literal_global.137
- ___block_literal_global.143
- ___block_literal_global.152
- ___block_literal_global.1520
- ___block_literal_global.1527
- ___block_literal_global.1530
- ___block_literal_global.155
- ___block_literal_global.1668
- ___block_literal_global.191
- ___block_literal_global.224
- ___block_literal_global.327
- ___block_literal_global.516
- ___block_literal_global.526
- ___block_literal_global.550
- ___block_literal_global.575
- ___block_literal_global.635
- ___block_literal_global.640
- ___block_literal_global.927
- ___block_literal_global.930
- ___block_literal_global.935
- _fig_log_get_emitter
CStrings:
+ "\t%@ -> %@ [label=\"%@\\nenabled: %s\\nactive: %s\\norientation: %d\\nmirrored: %d\",color=%s];\n"
+ "\t%@ -> %@ [label=\"delegate\",style=dotted];\n"
+ "\t%@ -> %@ [label=\"delegateOverride\",style=dotted];\n"
+ "\t%@ [shape=box,label=\"%@\",color=black];\n"
+ "\t%@ [shape=box,label=\"%@\\n%p\",color=%@];\n"
+ "\t%@ [shape=circle,label=\"%@\\n%p\",color=black];\n"
+ "\tlabel=\"%@\\n%@\\n%@\\n%@\";\n"
+ "\tranksep=1.5;nodesep=1;\n"
+ "%@AVCaptureSession"
+ "%@\\n%p"
+ "%c"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "'%@' %dx%d, %dfps"
+ "(%g,%g)"
+ "(original) "
+ "***Original*** "
+ "***OverCapture*** "
+ "+[AVCaptureCoreAnalyticsReporter clientApplicationIDType:]"
+ "+[AVCaptureCoreAnalyticsReporter initialize]"
+ "+[AVCaptureDevice _backgroundBlurApertureChanged:]"
+ "+[AVCaptureDevice _backgroundReplacementEnabledChanged:]"
+ "+[AVCaptureDevice _backgroundReplacementURLBookmarkChanged:]"
+ "+[AVCaptureDevice _reactionTriggered:]"
+ "+[AVCaptureDevice _reactionsInProgressChangedByControlCenter:]"
+ "+[AVCaptureDevice _setControlCenterVideoEffectUnavailableReasonsForVideoEffect:reasons:]"
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
+ "+[AVCaptureDevice isEdgeLightActive]"
+ "+[AVCaptureDevice isEdgeLightEnabled]"
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
+ "+[AVCaptureDevice setPortraitEffectStudioLightQuality:]"
+ "+[AVCaptureDevice setStudioLightingControlMode:]"
+ "+[AVCaptureDevice setStudioLightingIntensity:]"
+ "+[AVCaptureDevice studioLightingControlMode]"
+ "+[AVCaptureDevice studioLightingIntensity]"
+ "+[AVCaptureFigVideoDevice _newFigCaptureSources]"
+ "+[AVCaptureFigVideoDevice _prioritizedDeviceList:]"
+ "+[AVCaptureOutput availableVideoCodecTypesForSourceDevice:sourceFormat:outputDimensions:fileType:videoCodecTypesAllowList:]"
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
+ "+[AVExternalSyncDeviceDiscoverySession sharedSession]"
+ "+[AVExternalSyncDeviceDiscoverySession sharedSession]_block_invoke"
+ "+[AVFlashlight hasFlashlight]"
+ "+[AVPortraitEffectsMatte portraitEffectsMatteFromDictionaryRepresentation:error:]"
+ "+[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:]"
+ "+[AVVirtualCaptureCard sharedVirtualCaptureCard]_block_invoke"
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
+ "-[AVCaptureConnection clientRetainedBufferCount]"
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
+ "-[AVCaptureDeviceRotationCoordinator externalDisplayLayerObserver:visibiltyChanged:]"
+ "-[AVCaptureDeviceRotationCoordinator handleVideoPreviewLayerDidBecomeVisibleNotification:]"
+ "-[AVCaptureDeviceRotationCoordinator initWithDevice:previewLayer:]"
+ "-[AVCaptureFigAudioDevice _copyFigCaptureSourceProperty:]_block_invoke"
+ "-[AVCaptureFigAudioDevice _handleNotification:payload:]"
+ "-[AVCaptureFigAudioDevice _initWithFigCaptureSource:]"
+ "-[AVCaptureFigAudioDevice deviceClock]"
+ "-[AVCaptureFigVideoDevice _checkTCCAccess]_block_invoke"
+ "-[AVCaptureFigVideoDevice _copyFigCaptureSourceProperty:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _defaultRectForExposurePointOfInterest:]"
+ "-[AVCaptureFigVideoDevice _defaultRectForFocusPointOfInterest:focusMode:]"
+ "-[AVCaptureFigVideoDevice _drainDynamicAspectRatioRequestQueue]"
+ "-[AVCaptureFigVideoDevice _drainManualControlRequestQueue:]"
+ "-[AVCaptureFigVideoDevice _handleLiveReconfigurationCompletionWithPayload:]"
+ "-[AVCaptureFigVideoDevice _handleManualControlCompletionForRequestQueue:withPayload:]"
+ "-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2"
+ "-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3"
+ "-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_8"
+ "-[AVCaptureFigVideoDevice _incrementObserverCountForHighFrequencyProperty:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _incrementObserverCountForHighFrequencyProperty:]_block_invoke_2"
+ "-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke"
+ "-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_24"
+ "-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDuration:]"
+ "-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDuration:]"
+ "-[AVCaptureFigVideoDevice _setAdjustingExposure:]"
+ "-[AVCaptureFigVideoDevice _setAdjustingExposure:]_block_invoke"
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
+ "-[AVCaptureFigVideoDevice _updateRectOfInterestSizeForSensorOrientationAndDynamicAspectRatio:]"
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
+ "-[AVCaptureFigVideoDevice isFollowingExternalSyncDevice]"
+ "-[AVCaptureFigVideoDevice isSceneClassificationActive]"
+ "-[AVCaptureFigVideoDevice isVideoFrameDurationLocked]"
+ "-[AVCaptureFigVideoDevice panWithTranslation:]"
+ "-[AVCaptureFigVideoDevice performOneShotFraming]"
+ "-[AVCaptureFigVideoDevice rampExponentiallyToVideoZoomFactor:withDuration:]"
+ "-[AVCaptureFigVideoDevice rampToVideoZoomFactor:withRate:]"
+ "-[AVCaptureFigVideoDevice rampToVideoZoomFactor:withTuning:]"
+ "-[AVCaptureFigVideoDevice removeCMIOExtensionPropertyValueChangeHandler:]_block_invoke"
+ "-[AVCaptureFigVideoDevice resetFraming]"
+ "-[AVCaptureFigVideoDevice setActiveColorSpace:]"
+ "-[AVCaptureFigVideoDevice setActiveDepthDataFormat:]"
+ "-[AVCaptureFigVideoDevice setActiveDepthDataMinFrameDuration:]"
+ "-[AVCaptureFigVideoDevice setActiveExternalSyncSignalCompensationDelay:withExternalSyncDevice:]"
+ "-[AVCaptureFigVideoDevice setActiveExternalSyncSignalCompensationDelay:withExternalSyncDevice:]_block_invoke"
+ "-[AVCaptureFigVideoDevice setActiveFormat:]"
+ "-[AVCaptureFigVideoDevice setActiveMaxExposureDuration:]"
+ "-[AVCaptureFigVideoDevice setActiveVideoMaxFrameDuration:]"
+ "-[AVCaptureFigVideoDevice setActiveVideoMaxFrameDuration:]_block_invoke"
+ "-[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:]"
+ "-[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:]_block_invoke"
+ "-[AVCaptureFigVideoDevice setActiveVideoMinFrameDuration:activeVideoMaxFrameDuration:]"
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
+ "-[AVCaptureFigVideoDevice setDynamicAspectRatio:completionHandler:]"
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
+ "-[AVCaptureFraming _initWithAspectRatio:zoomFactor:]"
+ "-[AVCaptureFraming dealloc]"
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
+ "-[AVCaptureOutput _recommendedVideoOutputSettingsForConnection:sourceSettings:videoCodec:isIris:outputFileURL:]"
+ "-[AVCaptureOutput attachToFigCaptureSession:]"
+ "-[AVCaptureOutput detachFromFigCaptureSession:]"
+ "-[AVCaptureOutput handleServerConnectionDeathForFigCaptureSession:]"
+ "-[AVCaptureOutput recommendedCinematicAudioOutputSettingsForConnection:fileType:isProResCapture:]"
+ "-[AVCaptureOutput updateMetadataTransformForSourceFormat:aspectRatio:]"
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
+ "-[AVCapturePhotoOutput setCameraSensorOrientationCompensationEnabled:]"
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
+ "-[AVCaptureSession _canAddControl:failureReason:]"
+ "-[AVCaptureSession _canAddInput:failureReason:]"
+ "-[AVCaptureSession _canAddOutput:failureReason:]"
+ "-[AVCaptureSession _canAddVideoPreviewLayer:failureReason:]"
+ "-[AVCaptureSession _computeMemoryUsageForOutputs]"
+ "-[AVCaptureSession _createFigCaptureSession]"
+ "-[AVCaptureSession _encoderCost]"
+ "-[AVCaptureSession _getSmartStyleRenderingSupported]"
+ "-[AVCaptureSession _handleCaptureServerConnectionDiedNotification]"
+ "-[AVCaptureSession _handleConfigurationDidBecomeLiveNotificationWithPayload:]"
+ "-[AVCaptureSession _handleDidStopRunningNotificationWithPayload:]"
+ "-[AVCaptureSession _handleVideoEffectFrameRateThrottling:]"
+ "-[AVCaptureSession _memoryCost]"
+ "-[AVCaptureSession _nandCost]"
+ "-[AVCaptureSession _reconnectAfterServerConnectionDied]"
+ "-[AVCaptureSession _removeVideoPreviewLayer:]"
+ "-[AVCaptureSession _startFigCaptureSession]"
+ "-[AVCaptureSession _stopAndTearDownGraph]"
+ "-[AVCaptureSession _updateDeviceActiveFormatsAndActiveConnections]"
+ "-[AVCaptureSession _updateHardwareCost]"
+ "-[AVCaptureSession _validateAudioConfiguration:]"
+ "-[AVCaptureSession _validateCinematicVideoConfiguration:]"
+ "-[AVCaptureSession _validateProResRawVideoConfiguration:]"
+ "-[AVCaptureSession _videoAndMovieOutputCost]"
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
+ "-[AVCaptureSession isBeingConfiguredOnCurrentThread]"
+ "-[AVCaptureSmartFraming _initWithAspectRatio:zoomFactor:]"
+ "-[AVCaptureSmartFraming dealloc]"
+ "-[AVCaptureSmartFramingMonitor dealloc]"
+ "-[AVCaptureSmartFramingMonitor initWithDevice:smartFramingZoomFactorsByFieldOfView:]"
+ "-[AVCaptureSpatialAudioMetadataSampleGenerator init]"
+ "-[AVCaptureStillImageOutput _setStillImageStabilizationAutomaticallyEnabled:]"
+ "-[AVCaptureStillImageOutput handleNotification:payload:]"
+ "-[AVCaptureStillImageOutput handleNotificationForPrepareRequest:withPayload:]"
+ "-[AVCaptureStillImageOutput handleNotificationForRequest:withPayload:imageIsEV0:]"
+ "-[AVCaptureStillImageOutput prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:]"
+ "-[AVCaptureStillImageOutput setAutomaticallyEnablesStillImageStabilizationWhenAvailable:]"
+ "-[AVCaptureStillImageOutput setCameraSensorOrientationCompensationEnabled:]"
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
+ "-[AVCaptureVideoDataOutput updateClientVideoSettingsForAspectRatio:]"
+ "-[AVCaptureVideoDataOutput vettedVideoSettingsForSettingsDictionary:connection:]"
+ "-[AVCaptureVideoPreviewLayer _initWithSession:makeConnection:]"
+ "-[AVCaptureVideoPreviewLayer _setPortraitLightingEffectStrengthFromDeviceInput]"
+ "-[AVCaptureVideoPreviewLayer _setSensorAndEstimatedPreviewSizes]"
+ "-[AVCaptureVideoPreviewLayer _updateZoomPIPOverlayRect:]"
+ "-[AVCaptureVideoPreviewLayer _updateZoomPictureInPictureOverlaySupported]"
+ "-[AVCaptureVideoPreviewLayer attachToFigCaptureSession:]"
+ "-[AVCaptureVideoPreviewLayer captureDevicePointOfInterestForPoint:]"
+ "-[AVCaptureVideoPreviewLayer captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:applyDynamicAspectRatio:]"
+ "-[AVCaptureVideoPreviewLayer centerSublayer:]"
+ "-[AVCaptureVideoPreviewLayer dealloc]"
+ "-[AVCaptureVideoPreviewLayer detachFromFigCaptureSession:]"
+ "-[AVCaptureVideoPreviewLayer initWithLayer:]"
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
+ "-[AVControlCenterModuleState setRingLightMode:]"
+ "-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke"
+ "-[AVDepthData _copyPixelBufferRepresentationWithPixelFormatType:]"
+ "-[AVDepthData depthDataByApplyingExifOrientation:]"
+ "-[AVDepthData dictionaryRepresentationForAuxiliaryDataType:]"
+ "-[AVExternalStorageDevice updateExternalStorageDeviceManager:andFigExternalStorageDeviceUUID:]"
+ "-[AVExternalStorageDeviceDiscoverySession _checkAuthorizationStatus]"
+ "-[AVExternalStorageDeviceDiscoverySession _requestAuthorization:]"
+ "-[AVExternalStorageDeviceDiscoverySession _setupExternalStorageDeviceDiscoverySession]"
+ "-[AVExternalSyncDevice _handleUnfollow]"
+ "-[AVExternalSyncDevice _setupStateMachine]"
+ "-[AVExternalSyncDevice handleTransitionToActiveSyncFromConfiguring]"
+ "-[AVExternalSyncDevice handleTransitionToActiveSync]"
+ "-[AVExternalSyncDevice handleTransitionToConfiguring]"
+ "-[AVExternalSyncDevice handleTransitionToConfiguring]_block_invoke"
+ "-[AVExternalSyncDevice handleTransitionToIdle]"
+ "-[AVExternalSyncDevice handleTransitionToJamSync]"
+ "-[AVExternalSyncDevice handleTransitionToUnavailable]"
+ "-[AVExternalSyncDeviceDiscoverySession _updateDevicesEvent:]"
+ "-[AVExternalSyncDeviceDiscoverySession setupNotifications]"
+ "-[AVExternalSyncDeviceDiscoverySession teardownNotifications]"
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
+ "-[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:]"
+ "-[AVSpatialOverCaptureVideoPreviewLayer _setPrimaryCaptureRectAspectRatio:centerPoint:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:]_block_invoke"
+ "-[AVSpatialOverCaptureVideoPreviewLayer attachSafelyToFigCaptureSession:]"
+ "-[AVSpatialOverCaptureVideoPreviewLayer captureDeviceTransformForSensorSize:previewSize:sensorToPreviewVTScalingMode:applyDynamicAspectRatio:]"
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
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_AVF/AVFCapture/BW/Sources/AVSpatialOverCaptureVideoPreviewLayer.m"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_AVF/AVFCapture/Common/Sources/AVCaptureCommon.m %s: could not determine proprietary defaults domain for %{private}@, so using unknown"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_AVF/AVFCapture/Common/Sources/AVCaptureCommon.m %s: not caching \"unknown\" proprietary defaults domain for %{private}@"
+ "4b6e3d8790e69de2ca8879c2ffd37a979da2e695"
+ "5c66fcbba677180c2f4ee8a0978673ff2cabf19b"
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
+ "<<<< AVCaptureConnection >>>> %s: %p clientRetainedBufferCount for connection to %@ is %d"
+ "<<<< AVCaptureConnection >>>> %s: %p preferredVideoStabilizationMode for connection to %@ is: %@"
+ "<<<< AVCaptureConnection >>>> %s: AVCaptureVideoStabilizationModeAuto does not map to a FigCaptureVideoStabilizationMethod.  Turning off."
+ "<<<< AVCaptureConnection >>>> %s: Input class is not AVCaptureMetadataInput or AVCaptureCoreMotionMetadataInput?"
+ "<<<< AVCaptureConnection >>>> %s: Output class is not AVCaptureMetadataOutput?"
+ "<<<< AVCaptureConnection >>>> %s: Specified max frame rate (%f) is too high, changing it to %f"
+ "<<<< AVCaptureConnection >>>> %s: Specified max frame rate (%f) is too low, changing it to %f"
+ "<<<< AVCaptureConnection >>>> %s: Specified min frame rate (%f) is too high, changing it to %f"
+ "<<<< AVCaptureConnection >>>> %s: Specified min frame rate (%f) is too low, changing it to %f"
+ "<<<< AVCaptureConnection >>>> %s: We should not remove the observers in dealloc. see [17229521]"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Cannot send controls from an invalid connection!"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Cannot send controlsDelegate methods because the session reference is nil"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Cannot update a control from an invalid connection!"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Failed to send %lu controls to the overlay (%@)"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Failed to send control update (%@) to the overlay (%@) for %@"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Ignoring status update from a stale connection!"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Not sending controls to the angel because the connection isn't active yet"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Overlay changed active control identifier: %@"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Overlay changed visible: %d, active control identifier: %@"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Successfully sent %lu controls to the overlay"
+ "<<<< AVCaptureControlsOverlay >>>> %s: Successfully sent control value update (%@) to the overlay for %@"
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
+ "<<<< AVCaptureDevice >>>> %s: Read isRingLightActive %@"
+ "<<<< AVCaptureDevice >>>> %s: Read isRingLightEnabled %@"
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
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Draining Dynamic Aspect Ratio Handler for Request: %d. Current RequestID: %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Draining request %d from Dynamic Aspect Ratio Requests handler queue."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Encountered unknown device."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Enqueued custom exposure request %d with error %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Enqueued fake bias request %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Enqueued manual focus request %d with error %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Enqueued manual wb request %d with error %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Enqueueing bias request %d with error %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Exiting for queue %p"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Failed to set values in activeExternalSyncSignalCompensationDelay (%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Failed to set values in setFrameMinDuration:maxDuration: (%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] FigVideoDevice.input.activeExternalSyncVideoFrameDuration is not in sync with FigVideoDevice.activeExternalSyncVideoFrameDuration"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] FigVideoDevice.input.activeLockedVideoFrameDuration is not in sync with FigVideoDevice.activeLockedVideoFrameDuration"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Firing Dynamic Aspect Ratio handler for request: %d. Error: %{public}@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Hidden changed from %d to %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Invalid notification payload!"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Iterations used: %d (HIT ITER LIMIT) for gains (%a %a %a) start %a"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Leaving custom exposure, so restoring min:%.2lld/%.2d max:%.2lld/%.2d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Macro focus changed from %d to %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] No FigCaptureSource"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Old Aspect Ratio: %@ is the same as the New Aspect Ratio: %@. Fire Completion Handler immediately."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Overriding max frame rate %f to the cap of %f"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Overriding min frame rate %f to the cap of %f"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Preferred primary constituent device changed from %@ to %@."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] ReadyToUnhide changed from %d to %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received %@ with %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received DeviceWhiteBalanceGains notification with a bad payload. Expected size = %d, actual = %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received GrayWorldDeviceWhiteBalanceGains notification with a bad payload. Expected size = %d, actual = %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received kFigCaptureSourceProperty_Hidden notification payload with value YES. Skip updating device property."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received kFigCaptureSourceProperty_ReadyToUnhide notification payload with value NO. Skip updating device property."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received live reconfiguration complete notification with payload: %{public}@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Received unexpected Connected notification"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Resetting framing"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Sending notification: %@ with payload: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Set(%@) failed (%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Setting FigCaptureSource %@ to %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Setting exposureMode = Locked after one-shot Auto-Expose or transition from Custom -> Locked Exposure"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Setting max frame rate failed"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] Setting min frame rate failed"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] State inconsistency: ramp %d notified completion but invalid ramping target %g"
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
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with minDuration {%lld / %d}, maxDuration: {%lld/ %d}"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with point x %f y %f focusMode %lu"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with starting point [%f,%f]"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with translation [%f,%f]"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with { %f, %f }"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with { r: %f, g: %f, b: %f }"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with { { %f, %f } { %f, %f } }"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] called with {%lld / %d}"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] depthDataDeliveryEnabledChanging: NO"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] draining request %d from queue %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] dynamicAspectRatio %@, dynamicDimensions %d,%d, size %f,%f"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] exposure operation: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] faceRectangle <x:%f, y:%f>, [w:%f, h:%f]"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] failed (%d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] focus operation: mode %d, lensPosition %f, %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] forcing default exposure ROI size { %.4lf, %.4lf } to { %.4lf, %.4lf } ... point of interest is { %.4lf, %.4lf } which came from %@ : %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] forcing default focus ROI size { %.4lf, %.4lf } to { %.4lf, %.4lf } ... point of interest is { %.4lf, %.4lf } which came from %@ : %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] from KVO %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] from query %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] initialized with fcs: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] kCMTimeInvalid (clearing override)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] payload:%{public}@ _activeExternalSyncDevice:%{public}@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] performing one-shot framing"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] scene classification activity changed from %d to %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] scene classification activity check: %d"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] ss is too low for new min frame rate %f, increasing ss."
+ "<<<< AVCaptureFigVideoDevice >>>> %s: [%{public}@] white-balance operation: %@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: exposure rect (isDefault: %c) { (%.2f : %.2f) : [%.2f : %.2f] : (%.2f : %.2f) }"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: focus rect (isDefault: %c) { (%.2f : %.2f) : [%.2f : %.2f] : (%.2f : %.2f) }"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: leftover devices! %@\nAppending to prioritized list: %@"
+ "<<<< AVCaptureFraming >>>> %s: %@"
+ "<<<< AVCaptureFraming >>>> %s: Framing: %@, %.2f"
+ "<<<< AVCaptureFraming >>>> %s: Smart Framing: %@, %.2f"
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
+ "<<<< AVCaptureMetadataOutput >>>> %s: Unsupported rotation of %d degrees"
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
+ "<<<< AVCaptureOutput >>>> %s: %@ sensor:{%fx%f} scaled:{%fx%f} vt:%@ front:%d applyRot:%d rotDegs:%f orient:%d applyMirr:%d isMirr:%d"
+ "<<<< AVCaptureOutput >>>> %s: %@ sensorAspectRatio %f, outputAspectRatio %f, outputAspectRatioScale %f"
+ "<<<< AVCaptureOutput >>>> %s: (%p) Bumping bit rate by 10 percent for 10 bit HDR video mode."
+ "<<<< AVCaptureOutput >>>> %s: (%p) FRSV enabled, scaling bitrate by %.2lf from %d to %d"
+ "<<<< AVCaptureOutput >>>> %s: (%p) NOT using AVCaptureSession.plist video settings, since max frame rate is changed"
+ "<<<< AVCaptureOutput >>>> %s: (%p) Removing ProResRaw HQ codec for 120fps"
+ "<<<< AVCaptureOutput >>>> %s: (%p) enable double encoding for ProRes"
+ "<<<< AVCaptureOutput >>>> %s: (%p) setting average bit rate of %lld."
+ "<<<< AVCaptureOutput >>>> %s: (%p) stereo capture enabled, scaling bitrate by %.2lf from %d to %d"
+ "<<<< AVCaptureOutput >>>> %s: Using asbd from fdesc. destSampleRate: %f, destNumChannels: %u, pcmBitDepth: %u"
+ "<<<< AVCaptureOutput >>>> %s: recommendedCinematicAudioOutputSettingsForConnection returning: %@"
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
+ "<<<< AVCaptureSession >>>> %s: (%p) %@"
+ "<<<< AVCaptureSession >>>> %s: (%p) %@: %@"
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
+ "<<<< AVCaptureSession >>>> %s: (%p) Smart style rendering is disabled, active format is not photo format %@"
+ "<<<< AVCaptureSession >>>> %s: (%p) _stopFigCaptureSession failed with error %d"
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
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Session is not running, fire dynamicAspectRatio completion handler."
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Setting preset to input priority *WITHOUT triggering buildAndRunGraph* (because nothing really changed) for change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Setting preset to input priority and triggering buildAndRunGraph for change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for activeColorSpace change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for backgroundBlurActive change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for backgroundReplacementActive change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for centerStageActive change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for client-initiated activeDepthDataFormat change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for client-initiated videoHDREnabled change %@"
+ "<<<< AVCaptureSession >>>> %s: (Session %p, thread %p) Triggering buildAndRunGraph for dynamicAspectRatio change %@"
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
+ "<<<< AVCaptureSession >>>> %s: Not calling -session:didChangeFocusLocked: on delegate when Cinematic Video is enabled"
+ "<<<< AVCaptureSession >>>> %s: Not calling -session:didChangeFocusLocked: on delegate when delegate does not respond to session:controlsDidChangeAutoFocusLocked"
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
+ "<<<< AVCaptureSession >>>> %s: Updating MFO (%p) output settings dimension to %dx%d for %@"
+ "<<<< AVCaptureSession >>>> %s: VEFrameRate Throttling (%p) : needToThrottle (%d) minFDSetByClient: (%d) maxFDSetByClient: (%d). newMaxFD: ( %lld / %d ) newMinFD: ( %lld / %d )."
+ "<<<< AVCaptureSession >>>> %s: Video/Movie output cost: %f (bandwidth: %d / %d, outputs: %d, VIS: %d / %d)"
+ "<<<< AVCaptureSession >>>> %s: called while session is not running."
+ "<<<< AVCaptureSession >>>> %s: resetting the active min/max frame rate to the default values"
+ "<<<< AVCaptureSession >>>> %s: updating %@ to %@"
+ "<<<< AVCaptureSmartFramingMonitor >>>> %s: %@"
+ "<<<< AVCaptureSmartFramingMonitor >>>> %s: Device: %@"
+ "<<<< AVCaptureSpatialAudioMetadataSampleGenerator >>>> %s: AVCaptureSpatialAudioMetadataSampleGenerator: node init FAILED"
+ "<<<< AVCaptureSpatialAudioMetadataSampleGenerator >>>> %s: AVCaptureSpatialAudioMetadataSampleGenerator: node init."
+ "<<<< AVCaptureSpatialAudioMetadataSampleGenerator >>>> %s: failed to allocate CMCaptureSpatialAudioMetadataSampleGenerator"
+ "<<<< AVCaptureStillImageOutput >>>> %s: #### maxDataSize reported as 0 ####"
+ "<<<< AVCaptureStillImageOutput >>>> %s: %d"
+ "<<<< AVCaptureStillImageOutput >>>> %s: (%p) called with %d"
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
+ "<<<< AVCaptureVideoDataOutput >>>> %s: Client provided video settings are not valid! (%fx%f). Using device.dynamicDimensions instead ( %fx%f )"
+ "<<<< AVCaptureVideoDataOutput >>>> %s: Updating video settings to %@ for %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@ %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@ Output size: %d, %d. Estimated preview size: %d, %d;"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@ have pending primary capture rect change"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@ received notification %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: %@ setting pending primary capture rect on FigCaptureSession %p"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) %@ : %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) %@->%@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) %d"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) (pthread %p)"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) (pthread %p)PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: (%p) Disregarding notification %@ since sinkIDs don't match (%@ vs %@)"
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
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: deviceAspectRatio %f, primaryCaptureRectAspectRatioScale %f"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: originalRotationDegrees:%i previewRotationDegrees:%i finalRotationDegrees:%i isMirrored:%i"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: overCaptureStatus %d -> %d, rampingVideoZoom %d"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: previewAspectRatio %f, primaryCaptureRectCenterPoint %@, centerOffset %@, centerOffsetTranslationScale %@, previewAspectRelativeToSensor %f, centerOffsetTranslation %@"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: previewAspectRatio %f, sensorAspectRatio %f, primaryCaptureRectAspectRatio %f, primaryCaptureRectAspectRatioScale %f"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: previewSize = %@, containerSize = %@, scaleX = %f, scaleY = %f"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: returnTransform [ %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f ]"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: sensorAspectRatio %f, previewAspectRatio %f, primaryCaptureRectAspectRatioScale %f"
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
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( biasValue != _ringLightBias ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectIntensityDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( controlMode != _backgroundBlurControlMode ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectControlModeDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( controlMode != _centerStageControlMode ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectControlModeDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( controlMode != _studioLightingControlMode ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectControlModeDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( intensityValue != _backgroundBlurAperture ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectIntensityDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( intensityValue != _studioLightingIntensity ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectIntensityDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isAutoSupported != _ringLightAutoSupported ) is %@, NOT sending AVControlCenterVideoEffectsModuleAutoRingLightSupportedDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _backgroundBlurEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _backgroundReplacementEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _centerStageEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _gesturesEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _reactionsEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _ringLightEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isEnabled != _studioLightingEnabled ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectEnabledDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( isSupported != _ringLightSupported ) is %@, NOT sending AVControlCenterVideoEffectsModuleEffectSupportedDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( ringLightMode != _ringLightMode ) is %@, NOT sending AVControlCenterVideoEffectsModuleRingLightModeDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( ringLightRecommendedColor != _ringLightRecommendedColor ) is %@, NOT sending AVControlCenterVideoEffectsModuleRingLightRecommendedColorDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( ringLightWidth != _ringLightWidth ) is %@, NOT sending AVControlCenterVideoEffectsModuleRingLightWidthDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( screenNitsFloor != _ringLightScreenNitsFloor ) is %@, NOT sending AVControlCenterVideoEffectsModuleRingLightRecommendedNitsFloorDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, ( url != _backgroundReplacementURL ) is %@, NOT sending AVControlCenterVideoEffectsBackgroundReplacementURLDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, _hiddenMicrophoneModes = %@, ! [hiddenMicModes isEqual:_hiddenMicrophoneModes] is %@, NOT sending AVControlCenterMicrophoneModesModuleHiddenMicrophoneModesDidChangeNotification"
+ "<<<< AVControlCenterModules >>>> %s: %@: sendNotification = %@, _ringLightScreenNitsFloor is %f, screenNitsFloor is %f and showRingLightOnboardingTip is %@, NOT sending AVControlCenterVideoEffectsModuleRingLightInitiateOnboardingNotification"
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
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightActive from %s to %s"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightAutoColorEnabled from %s to %s"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightAutoSupported from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightBias from %f to %f"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightColor from %f to %f"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightEnabled from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightMode from %d to %d"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightOnboardingPreviousTipTimestamp from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightOnboardingState from %lu to %lu"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightOnboardingStrikeCount from %i to %i"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightRecommendedColor from %f to %f"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightScreenNitsFloor from %f to %f"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightSupported from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _ringLightWidth from %f to %f"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _studioLightingControlMode from %d to %d"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _studioLightingEnabled from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _studioLightingIntensity from %f to %f"
+ "<<<< AVControlCenterModules >>>> %s: %@: setting _supportedMicrophoneModes from %@ to %@"
+ "<<<< AVControlCenterModules >>>> %s: %s blackenFrames from deviceID %@ for bundleID %@"
+ "<<<< AVControlCenterModules >>>> %s: Auto mic mode is not supported on this platform, ignoring setAutoMicrophoneModeEnabled:%d"
+ "<<<< AVControlCenterModules >>>> %s: BundleID %@, current selected manual framing device type %d, manualFramingDefaultZoomFactor %.3f"
+ "<<<< AVControlCenterModules >>>> %s: Mic modes are not supported on this platform, ignoring setMicrophoneMode:%@"
+ "<<<< AVControlCenterModules >>>> %s: Missing the value for dockedTrackingActiveChanged notification"
+ "<<<< AVControlCenterModules >>>> %s: Pan with translation at [%.3f, %.3f] on %@"
+ "<<<< AVControlCenterModules >>>> %s: Received the wrong type for eligible effects array for %@"
+ "<<<< AVControlCenterModules >>>> %s: Received wrong value type for gestures-disabled notification request: %@"
+ "<<<< AVControlCenterModules >>>> %s: Start panning at [%.3f, %.3f] on %@"
+ "<<<< AVControlCenterModules >>>> %s: Tried setting ringLightMode to AVControlCenterVideoEffectRingLightModeAuto but automatic Ring Light is not supported."
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
+ "<<<< AVExternalSyncDevice >>>> %s: %{public}@ AVExternalSyncDeviceDiscoverySession requested"
+ "<<<< AVExternalSyncDevice >>>> %s: %{public}@ adding devices:%{public}@"
+ "<<<< AVExternalSyncDevice >>>> %s: Setting up notification listener"
+ "<<<< AVExternalSyncDevice >>>> %s: Tearing down listener"
+ "<<<< AVExternalSyncDevice >>>> %s: Unable to allocate/init AVExternalSyncDeviceDiscoverySession"
+ "<<<< AVExternalSyncDevice >>>> %s: _setupStateMachine after init"
+ "<<<< AVExternalSyncDevice >>>> %s: _setupStateMachine init"
+ "<<<< AVExternalSyncDevice >>>> %s: configuration timed out"
+ "<<<< AVExternalSyncDevice >>>> %s: configurationTimeoutBlock early exit since self was released"
+ "<<<< AVExternalSyncDevice >>>> %s: deviceDatas %@"
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
+ "@\"NSMutableString\"16@?0@\"AVCaptureDeviceFormat\"8"
+ "@\"NSMutableString\"16@?0@\"AVCaptureInput\"8"
+ "@\"NSMutableString\"16@?0@\"AVCaptureInputPort\"8"
+ "@\"NSString\"16@?0@\"NSString\"8"
+ "@\"NSString\"16@?0@8"
+ "AVAuxiliaryMetadataAddValue"
+ "AVAuxiliaryMetadataArrayTagWithPrefixedKey"
+ "AVAuxiliaryMetadataStringTagWithPrefixedKey"
+ "AVCaptureCancelPrewarm"
+ "AVCaptureClientPreferencesDomain"
+ "AVCapturePrewarmWithOptions"
+ "AVCaptureSystemLensSelector_trace"
+ "AVControlCenterBlackenFramesFromDeviceForBundleID"
+ "AVControlCenterIsManualFramingEnabledForDevice"
+ "AVControlCenterPanWithTranslation"
+ "AVControlCenterStartPanningAtPoint"
+ "AVErrorInvalidSourceMedia"
+ "Alternates other than tmap are not supported"
+ "Aux data with invalid values not supported for DNG"
+ "CFBundleDisplayName"
+ "Image collections not supported"
+ "LastShownBuild:AVSpatialOverCaptureVideoPreviewLayer.m:294"
+ "LastShownDate:AVSpatialOverCaptureVideoPreviewLayer.m:294"
+ "Metadata sample time is invalid"
+ "Processor version is not available"
+ "Set PrimaryCaptureRect is taking more than %.0f seconds."
+ "This device doesn't support external storage device."
+ "Unable to create a vis configuration"
+ "Unable to create a vis processor"
+ "["
+ "[***OverCapture***] "
+ "\\n"
+ "\\n%@"
+ "\\n(%@)"
+ "\\nDepth Format [%d]: %@"
+ "\\nVideo Format [%d]"
+ "_addAuxiliaryImage"
+ "_createCompressionSessionWithModifications"
+ "_createDNGCompressorWithModifications"
+ "_getUniqueIDsForDevices"
+ "_refreshRegisteredDevices"
+ "_registerServerConnectionDiedNotification_block_invoke"
+ "audio"
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
+ "avcmdo_detectedObjectsCollectionForSampleBuffer"
+ "avcp_copyCGImageForCompressedData"
+ "avcp_copyCGImageForUncompressedBuffer"
+ "avcp_copyDNGFileDataRepresentationForSushiRawBuffer"
+ "avcp_copyFirstAuxiliaryImageOfType"
+ "avcp_copyJPEGThumbnailForPixelBuffer"
+ "avcp_copyTIFFFileDataRepresentationForImage"
+ "avcs_updateAVCaptureConnectionForAspectRatio"
+ "avdepthdata_trace"
+ "avexternalsyncdevicediscoverysession_trace"
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
+ "c7adc2e80986a12a567fb63ed7a059d24c65ed70"
+ "cinematicAudioSettings"
+ "com.apple.coremedia"
+ "depth data"
+ "description=CameraCapture_AVF-665.80.6"
+ "digraph %@ {\n"
+ "disconnected"
+ "fad_figCaptureSourceNotificationHandler_block_invoke"
+ "fileSystemRepresentation"
+ "green"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "kCMPhotoError_InternalFailure"
+ "kCMPhotoError_UnsupportedOperation"
+ "kFigExternalStorageDeviceManagerError_DeviceNotSupported"
+ "metadata items"
+ "metadata objects"
+ "no; self-healing the connection"
+ "nonretainedObjectValue"
+ "now"
+ "po_createPreviewJPEGRepresentationForSampleBuffer"
+ "previewHeight"
+ "previewWidth"
+ "rawThumbnailHeight"
+ "rawThumbnailWidth"
+ "red"
+ "setDateFormat:"
+ "socvpl_figCaptureSessionNotification"
+ "stringFromDate:"
+ "thumbnailHeight"
+ "thumbnailWidth"
+ "video"
+ "video data"
+ "vision data"
+ "vpio_translatedBundleIDForBundleID"
+ "vpl_figCaptureSessionNotification"
+ "vpl_transformForPlacement"
+ "vto_notificationHandler"
+ "writeToFile:atomically:encoding:error:"
+ "yyyy-MM-dd    HH:mm:ss.SSS"
+ "yyyy-MM-dd hh:mm:ss.SSS"
+ "}\n"
- "%s signalled err=%d at <>:%d"
- "description=CameraCapture_AVF-664.62.12"

```
