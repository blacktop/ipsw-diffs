## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/Versions/A/AVFCapture`

```diff

-587.81.10.0.0
-  __TEXT.__text: 0x170568
-  __TEXT.__auth_stubs: 0x2310
-  __TEXT.__objc_methlist: 0x13760
-  __TEXT.__cstring: 0x25844
+587.101.4.0.0
+  __TEXT.__text: 0x1793fc
+  __TEXT.__auth_stubs: 0x2340
+  __TEXT.__objc_methlist: 0x13ef4
+  __TEXT.__cstring: 0x25d08
   __TEXT.__const: 0x10e0
-  __TEXT.__gcc_except_tab: 0x2df0
+  __TEXT.__gcc_except_tab: 0x2ec4
   __TEXT.__dlopen_cstrs: 0x1d1
-  __TEXT.__oslogstring: 0xa387
+  __TEXT.__oslogstring: 0xa5c2
   __TEXT.__ustring: 0x112
-  __TEXT.__unwind_info: 0x59d8
-  __TEXT.__objc_classname: 0x25e3
-  __TEXT.__objc_methname: 0x2b8b5
-  __TEXT.__objc_methtype: 0x4ac7
-  __TEXT.__objc_stubs: 0x18280
-  __DATA_CONST.__got: 0x2658
-  __DATA_CONST.__const: 0x1298
-  __DATA_CONST.__objc_classlist: 0x878
+  __TEXT.__unwind_info: 0x5ce0
+  __TEXT.__objc_classname: 0x2649
+  __TEXT.__objc_methname: 0x2c383
+  __TEXT.__objc_methtype: 0x4b52
+  __TEXT.__objc_stubs: 0x18c60
+  __DATA_CONST.__got: 0x2710
+  __DATA_CONST.__const: 0x1340
+  __DATA_CONST.__objc_classlist: 0x890
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a58
+  __DATA_CONST.__objc_selrefs: 0x7cd0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x6d8
+  __DATA_CONST.__objc_superrefs: 0x6f0
   __DATA_CONST.__objc_arraydata: 0x280
-  __AUTH_CONST.__auth_got: 0x1198
-  __AUTH_CONST.__const: 0x2680
-  __AUTH_CONST.__cfstring: 0x12b80
-  __AUTH_CONST.__objc_const: 0x1fe20
+  __AUTH_CONST.__auth_got: 0x11b0
+  __AUTH_CONST.__const: 0x2700
+  __AUTH_CONST.__cfstring: 0x12ea0
+  __AUTH_CONST.__objc_const: 0x1fd48
   __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0xdc0
-  __DATA.__objc_ivar: 0x1fc0
-  __DATA.__data: 0xe50
-  __DATA.__bss: 0xc38
-  __DATA.__common: 0x2c0
+  __AUTH.__objc_data: 0xeb0
+  __DATA.__objc_ivar: 0x2020
+  __DATA.__data: 0xe60
+  __DATA.__bss: 0xc68
+  __DATA.__common: 0x2e0
   __DATA_DIRTY.__objc_data: 0x46f0
   __DATA_DIRTY.__bss: 0x68
   __DATA_DIRTY.__common: 0x20

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2CDC82B1-6577-317A-877C-F67E2EBC0C00
-  Functions: 7736
-  Symbols:   18263
-  CStrings:  13022
+  UUID: 72B53643-A5B2-3833-93DF-A9C3FBF6F117
+  Functions: 8778
+  Symbols:   19595
+  CStrings:  13180
 
Symbols:
+ +[AVCaptureAudioFileOutput availableOutputFileTypes].cold.1
+ +[AVCaptureAudioFileOutput_Tundra availableOutputFileTypes].cold.1
+ +[AVCaptureCoreAnalyticsReporter clientApplicationIDType:].cold.1
+ +[AVCaptureDALDevice _cameraHistoryDispatchQueue].cold.1
+ +[AVCaptureDALDevice _ensureDeviceList].cold.1
+ +[AVCaptureDALDevice _refreshDevices].cold.1
+ +[AVCaptureDALDevice _userPreferredCameraOverrideHistoryKey].cold.1
+ +[AVCaptureDeferredPhotoProcessor sharedPhotoProcessor].cold.1
+ +[AVCaptureDevice _devicesWithDeviceTypes:mediaType:position:].cold.1
+ +[AVCaptureDevice _devicesWithDeviceTypes:mediaType:position:].cold.2
+ +[AVCaptureDevice _listEligibleEffects].cold.1
+ +[AVCaptureDevice _reactionTriggered:].cold.1
+ +[AVCaptureDevice _reactionTriggered:].cold.2
+ +[AVCaptureDevice _reactionTriggered:].cold.3
+ +[AVCaptureDevice _reactionsInProgressChangedByControlCenter:].cold.1
+ +[AVCaptureDevice _reactionsInProgressChangedByControlCenter:].cold.2
+ +[AVCaptureDevice _reactionsInProgressChangedByControlCenter:].cold.3
+ +[AVCaptureDevice backgroundReplacementURLDefault].cold.1
+ +[AVCaptureDevice reactionEffectGesturesEnabledDefault].cold.1
+ +[AVCaptureDevice reactionEffectSuppressedGesture]
+ +[AVCaptureDevice reactionEffectSuppressedGesturesEnabled]
+ +[AVCaptureDevice setReactionEffectSuppressedGesture:]
+ +[AVCaptureDevice setReactionEffectSuppressedGesturesEnabled:]
+ +[AVCaptureDevice setUserPreferredCamera:].cold.1
+ +[AVCaptureDevice setUserPreferredCamera:forClientPreferenceDomain:].cold.1
+ +[AVCaptureDevice setupKVOLoggingOnce].cold.1
+ +[AVCaptureDevice_Tundra _devicesWithDeviceTypes:mediaType:position:allowIOSMacEnvironment:].cold.1
+ +[AVCaptureDevice_Tundra _reactionTriggered:].cold.1
+ +[AVCaptureDevice_Tundra _reactionTriggered:].cold.2
+ +[AVCaptureDevice_Tundra _reactionTriggered:].cold.3
+ +[AVCaptureDevice_Tundra _reactionsInProgressChangedByControlCenter:].cold.1
+ +[AVCaptureDevice_Tundra _reactionsInProgressChangedByControlCenter:].cold.2
+ +[AVCaptureDevice_Tundra _reactionsInProgressChangedByControlCenter:].cold.3
+ +[AVCaptureDevice_Tundra _registeredDeviceClassNames].cold.1
+ +[AVCaptureDevice_Tundra backgroundReplacementURLDefault].cold.1
+ +[AVCaptureDevice_Tundra reactionEffectGesturesEnabledDefault].cold.1
+ +[AVCaptureDevice_Tundra reactionEffectSuppressedGesture]
+ +[AVCaptureDevice_Tundra reactionEffectSuppressedGesturesEnabled]
+ +[AVCaptureDevice_Tundra setReactionEffectSuppressedGesture:]
+ +[AVCaptureDevice_Tundra setReactionEffectSuppressedGesturesEnabled:]
+ +[AVCaptureDevice_Tundra setUserPreferredCamera:].cold.1
+ +[AVCaptureDevice_Tundra setupKVOProtectionOnce].cold.1
+ +[AVCaptureFigVideoDevice _cameraHistoryDispatchQueue].cold.1
+ +[AVCaptureFigVideoDevice _userPreferredCameraOverrideHistoryKey].cold.1
+ +[AVCaptureHALDevice _deviceFormatWithASBD:deviceChannelCount:].cold.1
+ +[AVCaptureHALDevice _ensureDeviceList].cold.1
+ +[AVCaptureHALDevice _refreshDevices].cold.1
+ +[AVCaptureHALDevice _refreshDevices].cold.2
+ +[AVCaptureHALDevice defaultDeviceWithDeviceType:mediaType:position:].cold.1
+ +[AVCaptureHALDevice defaultDeviceWithDeviceType:mediaType:position:].cold.2
+ +[AVCaptureMetadataOutput _metadataConstantValueToName:].cold.1
+ +[AVCapturePhotoOutput DNGPhotoDataRepresentationForRawSampleBuffer:previewPhotoSampleBuffer:].cold.1
+ +[AVCapturePhotoOutput_Tundra JPEGPhotoDataRepresentationForJPEGSampleBuffer:previewPhotoSampleBuffer:].cold.1
+ +[AVCapturePhotoOutput_Tundra _blockBufferDataForSampleBuffer:].cold.1
+ +[AVCapturePhotoOutput_Tundra compressedPhotoDataRepresentationForSampleBuffer:].cold.1
+ +[AVCaptureProprietaryDefaultsSingleton proprietaryDefaultsSingleton].cold.1
+ +[AVCaptureSession initialize].cold.1
+ +[AVCaptureStillImageOutput maxStillImageJPEGDataSize].cold.1
+ +[AVCaptureStillImageOutput_Tundra jpegStillImageNSDataRepresentation:].cold.1
+ +[AVCaptureStillImageOutput_Tundra jpegStillImageNSDataRepresentation:].cold.2
+ +[AVDepthData depthDataFromDictionaryRepresentation:error:].cold.1
+ +[AVDepthData depthDataFromDictionaryRepresentation:error:].cold.2
+ +[AVDepthData depthDataFromDictionaryRepresentation:error:].cold.3
+ +[AVExternalStorageDeviceDiscoverySession sharedSession].cold.1
+ +[AVFlashlight hasFlashlight].cold.1
+ +[AVMetadataFaceIDReadinessObject faceIDReadinessObjectWithReady:coachingStatus:userEngagementStatus:input:time:]
+ +[AVMetadataMotionToWakeObject motionToWakeObjectWithDetectedMotion:input:time:]
+ +[AVPortraitEffectsMatte portraitEffectsMatteFromDictionaryRepresentation:error:].cold.1
+ +[AVPortraitEffectsMatte portraitEffectsMatteFromDictionaryRepresentation:error:].cold.2
+ +[AVPortraitEffectsMatte portraitEffectsMatteFromDictionaryRepresentation:error:].cold.3
+ +[AVSmartStyleSettingsState _smartStyleSettingsQueue].cold.1
+ +[WombatDeviceFilter _isFilteringWombatDevices].cold.1
+ +[WombatDeviceFilter _isShowingWombatDevices].cold.1
+ +[WombatDeviceFilter singleton].cold.1
+ -[AVCameraCalibrationData _distortionLookupTableFromCoefficients:distortionCenter:pixelSize:referenceDimensions:lookupTableLength:].cold.1
+ -[AVCameraCalibrationData _distortionLookupTableFromCoefficients:distortionCenter:pixelSize:referenceDimensions:lookupTableLength:].cold.2
+ -[AVCameraCalibrationData _distortionLookupTableFromCoefficients:distortionCenter:pixelSize:referenceDimensions:lookupTableLength:].cold.3
+ -[AVCameraCalibrationData _distortionLookupTableFromCoefficients:distortionCenter:pixelSize:referenceDimensions:lookupTableLength:].cold.4
+ -[AVCameraCalibrationData copyAuxiliaryMetadata].cold.1
+ -[AVCameraCalibrationData copyAuxiliaryMetadata].cold.10
+ -[AVCameraCalibrationData copyAuxiliaryMetadata].cold.11
+ -[AVCameraCalibrationData copyAuxiliaryMetadata].cold.2
+ -[AVCameraCalibrationData copyAuxiliaryMetadata].cold.3
+ -[AVCameraCalibrationData copyAuxiliaryMetadata].cold.4
+ -[AVCameraCalibrationData copyAuxiliaryMetadata].cold.5
+ -[AVCameraCalibrationData copyAuxiliaryMetadata].cold.6
+ -[AVCameraCalibrationData copyAuxiliaryMetadata].cold.7
+ -[AVCameraCalibrationData copyAuxiliaryMetadata].cold.8
+ -[AVCameraCalibrationData copyAuxiliaryMetadata].cold.9
+ -[AVCaptureAudioDataOutput_Tundra _updateCompressorNodesForConnection:].cold.1
+ -[AVCaptureAudioDataOutput_Tundra _updateCompressorNodesForConnection:].cold.2
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.1
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.10
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.11
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.12
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.13
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.14
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.2
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.3
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.4
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.5
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.6
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.7
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.8
+ -[AVCaptureAudioDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.9
+ -[AVCaptureAudioDataOutput_Tundra connectionMediaTypes].cold.1
+ -[AVCaptureAudioDataOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.1
+ -[AVCaptureAudioDataOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.2
+ -[AVCaptureAudioDataOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.3
+ -[AVCaptureAudioDataOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.4
+ -[AVCaptureAudioFileOutput_Tundra _controlFileWritingForConnection:busNumber:fileControlToken:].cold.1
+ -[AVCaptureAudioFileOutput_Tundra _controlFileWritingForConnection:busNumber:fileControlToken:].cold.2
+ -[AVCaptureAudioFileOutput_Tundra _controlFileWritingForConnection:busNumber:fileControlToken:].cold.3
+ -[AVCaptureAudioFileOutput_Tundra _controlFileWritingForConnection:busNumber:fileControlToken:].cold.4
+ -[AVCaptureAudioFileOutput_Tundra _forciblyStopFileWritingForRunningRecordingOperation].cold.1
+ -[AVCaptureAudioFileOutput_Tundra _forciblyStopFileWritingForRunningRecordingOperation].cold.2
+ -[AVCaptureAudioFileOutput_Tundra _updateCompressorNodesForConnection:].cold.1
+ -[AVCaptureAudioFileOutput_Tundra _updateCompressorNodesForConnection:].cold.2
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.1
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.10
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.11
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.12
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.13
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.14
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.15
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.16
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.17
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.18
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.19
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.2
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.3
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.4
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.5
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.6
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.7
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.8
+ -[AVCaptureAudioFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.9
+ -[AVCaptureAudioFileOutput_Tundra connectionMediaTypes].cold.1
+ -[AVCaptureAudioPreviewOutput_Tundra _updateCompressorNodesForConnection:].cold.1
+ -[AVCaptureAudioPreviewOutput_Tundra _updateCompressorNodesForConnection:].cold.2
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.1
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.10
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.11
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.12
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.13
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.14
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.15
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.16
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.17
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.18
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.2
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.3
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.4
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.5
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.6
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.7
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.8
+ -[AVCaptureAudioPreviewOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.9
+ -[AVCaptureAudioPreviewOutput_Tundra connectionMediaTypes].cold.1
+ -[AVCaptureAudioPreviewOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.1
+ -[AVCaptureAudioPreviewOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.2
+ -[AVCaptureAudioPreviewOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.3
+ -[AVCaptureAudioPreviewOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.4
+ -[AVCaptureAudioPreviewOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.5
+ -[AVCaptureAudioPreviewOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.6
+ -[AVCaptureAudioPreviewOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.7
+ -[AVCaptureAudioPreviewOutput_Tundra setOutputDeviceUniqueID:].cold.1
+ -[AVCaptureAudioPreviewOutput_Tundra setOutputDeviceUniqueID:].cold.2
+ -[AVCaptureAudioPreviewOutput_Tundra setOutputDeviceUniqueID:].cold.3
+ -[AVCaptureAudioPreviewOutput_Tundra setVolume:].cold.1
+ -[AVCaptureAudioPreviewOutput_Tundra setVolume:].cold.2
+ -[AVCaptureConnection figCaptureConnectionConfigurationForSessionPreset:allConnections:].cold.1
+ -[AVCaptureConnection figCaptureConnectionConfigurationForSessionPreset:allConnections:].cold.2
+ -[AVCaptureConnection_Tundra _applySplitterChannelMapFromAudioChannelsEnabled].cold.1
+ -[AVCaptureConnection_Tundra _applySplitterChannelMapFromAudioChannelsEnabled].cold.2
+ -[AVCaptureConnection_Tundra _applyVolumeFromAudioChannel:].cold.1
+ -[AVCaptureConnection_Tundra _applyVolumeFromAudioChannel:].cold.2
+ -[AVCaptureConnection_Tundra _applyVolumeFromAudioChannel:].cold.3
+ -[AVCaptureConnection_Tundra _audioLevelsForPropertyID:].cold.1
+ -[AVCaptureConnection_Tundra _audioLevelsForPropertyID:].cold.2
+ -[AVCaptureConnection_Tundra _audioLevelsForPropertyID:].cold.3
+ -[AVCaptureDALDevice _performReaction:].cold.1
+ -[AVCaptureDALDevice _performReaction:].cold.2
+ -[AVCaptureDALDevice _performReaction:].cold.3
+ -[AVCaptureDALDevice _performReaction:].cold.4
+ -[AVCaptureDALDevice _refreshActiveFormatAndKVONotify:].cold.1
+ -[AVCaptureDALDevice _refreshActiveFormatAndKVONotify:].cold.2
+ -[AVCaptureDALDevice _refreshActiveFormatAndKVONotify:].cold.3
+ -[AVCaptureDALDevice _refreshActiveFormatAndKVONotify:].cold.4
+ -[AVCaptureDALDevice _refreshCenterStageActiveAndKVONotify:].cold.1
+ -[AVCaptureDALDevice _refreshCenterStageActiveAndKVONotify:].cold.2
+ -[AVCaptureDALDevice _refreshCenterStageActiveAndKVONotify:].cold.3
+ -[AVCaptureDALDevice _refreshCenterStageActiveAndKVONotify:].cold.4
+ -[AVCaptureDALDevice _refreshCenterStageFramingMode].cold.1
+ -[AVCaptureDALDevice _refreshCenterStageFramingMode].cold.2
+ -[AVCaptureDALDevice _refreshCenterStageFramingMode].cold.3
+ -[AVCaptureDALDevice _refreshCenterStageFramingMode].cold.4
+ -[AVCaptureDALDevice _refreshCenterStageRectOfInterestAndKVONotify:].cold.1
+ -[AVCaptureDALDevice _refreshCenterStageRectOfInterestAndKVONotify:].cold.2
+ -[AVCaptureDALDevice _refreshCenterStageRectOfInterestAndKVONotify:].cold.3
+ -[AVCaptureDALDevice _refreshCenterStageRectOfInterestAndKVONotify:].cold.4
+ -[AVCaptureDALDevice _refreshFormatsAndKVONotify:].cold.1
+ -[AVCaptureDALDevice _refreshFormatsAndKVONotify:].cold.2
+ -[AVCaptureDALDevice _refreshFormatsAndKVONotify:].cold.3
+ -[AVCaptureDALDevice _refreshFormatsAndKVONotify:].cold.4
+ -[AVCaptureDALDevice _refreshLinkedDevicesAndKVONotify:].cold.1
+ -[AVCaptureDALDevice _refreshMetadataEnablement].cold.1
+ -[AVCaptureDALDevice _refreshMetadataEnablement].cold.2
+ -[AVCaptureDALDevice _refreshMetadataEnablement].cold.3
+ -[AVCaptureDALDevice _refreshMetadataEnablement].cold.4
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.1
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.10
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.11
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.12
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.13
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.14
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.15
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.16
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.17
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.18
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.19
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.2
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.20
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.21
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.22
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.23
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.24
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.3
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.4
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.5
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.6
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.7
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.8
+ -[AVCaptureDALDevice _refreshStreamsAndKVONotify:].cold.9
+ -[AVCaptureDALDevice _refreshSuspendedAttributeAndKVONotify:].cold.1
+ -[AVCaptureDALDevice _refreshVideoZoomFactorAndKVONotify:].cold.1
+ -[AVCaptureDALDevice _refreshVideoZoomFactorAndKVONotify:].cold.2
+ -[AVCaptureDALDevice _refreshVideoZoomFactorAndKVONotify:].cold.3
+ -[AVCaptureDALDevice _refreshVideoZoomFactorAndKVONotify:].cold.4
+ -[AVCaptureDALDevice _removePropertyListeners].cold.1
+ -[AVCaptureDALDevice _removePropertyListeners].cold.2
+ -[AVCaptureDALDevice _removePropertyListeners].cold.3
+ -[AVCaptureDALDevice _removePropertyListeners].cold.4
+ -[AVCaptureDALDevice _sendAVCDeviceOpcode:playbackMode:].cold.1
+ -[AVCaptureDALDevice _setActiveVideoMaxFrameDurationInternal:].cold.1
+ -[AVCaptureDALDevice _setActiveVideoMaxFrameDurationInternal:].cold.2
+ -[AVCaptureDALDevice _setActiveVideoMaxFrameDurationInternal:].cold.3
+ -[AVCaptureDALDevice _setActiveVideoMaxFrameDurationInternal:].cold.4
+ -[AVCaptureDALDevice _setActiveVideoMinFrameDurationInternal:].cold.1
+ -[AVCaptureDALDevice _setActiveVideoMinFrameDurationInternal:].cold.2
+ -[AVCaptureDALDevice _setActiveVideoMinFrameDurationInternal:].cold.3
+ -[AVCaptureDALDevice _setActiveVideoMinFrameDurationInternal:].cold.4
+ -[AVCaptureDALDevice _setBackgroundBlurAperture:].cold.1
+ -[AVCaptureDALDevice _setBackgroundBlurAperture:].cold.2
+ -[AVCaptureDALDevice _setBackgroundBlurAperture:].cold.3
+ -[AVCaptureDALDevice _setBackgroundBlurAperture:].cold.4
+ -[AVCaptureDALDevice _setBackgroundBlurEnabled:].cold.1
+ -[AVCaptureDALDevice _setBackgroundBlurEnabled:].cold.2
+ -[AVCaptureDALDevice _setBackgroundBlurEnabled:].cold.3
+ -[AVCaptureDALDevice _setBackgroundBlurEnabled:].cold.4
+ -[AVCaptureDALDevice _setBackgroundReplacementEnabled:].cold.1
+ -[AVCaptureDALDevice _setBackgroundReplacementEnabled:].cold.2
+ -[AVCaptureDALDevice _setBackgroundReplacementEnabled:].cold.3
+ -[AVCaptureDALDevice _setBackgroundReplacementEnabled:].cold.4
+ -[AVCaptureDALDevice _setBackgroundReplacementPixelBuffer:].cold.1
+ -[AVCaptureDALDevice _setBackgroundReplacementPixelBuffer:].cold.2
+ -[AVCaptureDALDevice _setBackgroundReplacementPixelBuffer:].cold.3
+ -[AVCaptureDALDevice _setBackgroundReplacementPixelBuffer:].cold.4
+ -[AVCaptureDALDevice _setCMIOAsyncStillCaptureConfigurations:].cold.1
+ -[AVCaptureDALDevice _setCMIOAsyncStillCaptureConfigurations:].cold.2
+ -[AVCaptureDALDevice _setCMIOAsyncStillCaptureConfigurations:].cold.3
+ -[AVCaptureDALDevice _setCMIOAsyncStillCaptureConfigurations:].cold.4
+ -[AVCaptureDALDevice _setCMIOAsyncStillCaptureEnabled:].cold.1
+ -[AVCaptureDALDevice _setCMIOAsyncStillCaptureEnabled:].cold.2
+ -[AVCaptureDALDevice _setCMIOAsyncStillCaptureEnabled:].cold.3
+ -[AVCaptureDALDevice _setCMIOAsyncStillCaptureEnabled:].cold.4
+ -[AVCaptureDALDevice _setCenterStageEnabled:].cold.1
+ -[AVCaptureDALDevice _setCenterStageEnabled:].cold.2
+ -[AVCaptureDALDevice _setCenterStageEnabled:].cold.3
+ -[AVCaptureDALDevice _setCenterStageEnabled:].cold.4
+ -[AVCaptureDALDevice _setCenterStageFramingMode:].cold.1
+ -[AVCaptureDALDevice _setCenterStageFramingMode:].cold.2
+ -[AVCaptureDALDevice _setCenterStageFramingMode:].cold.3
+ -[AVCaptureDALDevice _setCenterStageFramingMode:].cold.4
+ -[AVCaptureDALDevice _setCenterStageFramingMode:].cold.5
+ -[AVCaptureDALDevice _setCenterStageRectOfInterest:].cold.1
+ -[AVCaptureDALDevice _setCenterStageRectOfInterest:].cold.2
+ -[AVCaptureDALDevice _setCenterStageRectOfInterest:].cold.3
+ -[AVCaptureDALDevice _setCenterStageRectOfInterest:].cold.4
+ -[AVCaptureDALDevice _setGesturesEnabled:].cold.1
+ -[AVCaptureDALDevice _setGesturesEnabled:].cold.2
+ -[AVCaptureDALDevice _setGesturesEnabled:].cold.3
+ -[AVCaptureDALDevice _setGesturesEnabled:].cold.4
+ -[AVCaptureDALDevice _setReactionEffectsEnabled:].cold.1
+ -[AVCaptureDALDevice _setReactionEffectsEnabled:].cold.2
+ -[AVCaptureDALDevice _setReactionEffectsEnabled:].cold.3
+ -[AVCaptureDALDevice _setReactionEffectsEnabled:].cold.4
+ -[AVCaptureDALDevice _setStudioLightingEnabled:].cold.1
+ -[AVCaptureDALDevice _setStudioLightingEnabled:].cold.2
+ -[AVCaptureDALDevice _setStudioLightingEnabled:].cold.3
+ -[AVCaptureDALDevice _setStudioLightingEnabled:].cold.4
+ -[AVCaptureDALDevice _setStudioLightingIntensity:].cold.1
+ -[AVCaptureDALDevice _setStudioLightingIntensity:].cold.2
+ -[AVCaptureDALDevice _setStudioLightingIntensity:].cold.3
+ -[AVCaptureDALDevice _setStudioLightingIntensity:].cold.4
+ -[AVCaptureDALDevice _setSuppressedGesturesEnabled:]
+ -[AVCaptureDALDevice _setSuppressedGesturesEnabled:].cold.1
+ -[AVCaptureDALDevice _setSuppressedGesturesEnabled:].cold.2
+ -[AVCaptureDALDevice _setSuppressedGesturesEnabled:].cold.3
+ -[AVCaptureDALDevice _setSuppressedGesturesEnabled:].cold.4
+ -[AVCaptureDALDevice _sharedSuppressedGestureForStream:]
+ -[AVCaptureDALDevice _sharedSuppressedGesturesEnabledChangedForStream:]
+ -[AVCaptureDALDevice asyncStillCaptureSupported].cold.1
+ -[AVCaptureDALDevice asyncStillCaptureSupported].cold.2
+ -[AVCaptureDALDevice asyncStillCaptureSupported].cold.3
+ -[AVCaptureDALDevice asyncStillCaptureSupported].cold.4
+ -[AVCaptureDALDevice availableStillImageFormats].cold.1
+ -[AVCaptureDALDevice availableStillImageFormats].cold.2
+ -[AVCaptureDALDevice availableStillImageFormats].cold.3
+ -[AVCaptureDALDevice captureStillImage:photoSettings:completionHandler:].cold.1
+ -[AVCaptureDALDevice captureStillImage:photoSettings:completionHandler:].cold.2
+ -[AVCaptureDALDevice captureStillImage:photoSettings:completionHandler:].cold.3
+ -[AVCaptureDALDevice captureStillImage:photoSettings:completionHandler:].cold.4
+ -[AVCaptureDALDevice copyStillImageSampleBufferWithFormat:error:].cold.1
+ -[AVCaptureDALDevice copyStillImageSampleBufferWithFormat:error:].cold.2
+ -[AVCaptureDALDevice copyStillImageSampleBufferWithFormat:error:].cold.3
+ -[AVCaptureDALDevice deviceType].cold.1
+ -[AVCaptureDALDevice hasUltraWideCamera].cold.1
+ -[AVCaptureDALDevice hasUltraWideCamera].cold.2
+ -[AVCaptureDALDevice hasUltraWideCamera].cold.3
+ -[AVCaptureDALDevice hasUltraWideCamera].cold.4
+ -[AVCaptureDALDevice hasWideCamera].cold.1
+ -[AVCaptureDALDevice hasWideCamera].cold.2
+ -[AVCaptureDALDevice hasWideCamera].cold.3
+ -[AVCaptureDALDevice hasWideCamera].cold.4
+ -[AVCaptureDALDevice isCenterStageRectOfInterestSupported].cold.1
+ -[AVCaptureDALDevice isCenterStageRectOfInterestSupported].cold.2
+ -[AVCaptureDALDevice isCenterStageRectOfInterestSupported].cold.3
+ -[AVCaptureDALDevice isCenterStageRectOfInterestSupported].cold.4
+ -[AVCaptureDALDevice isDeskViewCameraModeSupported:].cold.1
+ -[AVCaptureDALDevice isDeskViewCameraModeSupported:].cold.2
+ -[AVCaptureDALDevice isDeskViewCameraModeSupported:].cold.3
+ -[AVCaptureDALDevice isDeskViewCameraModeSupported:].cold.4
+ -[AVCaptureDALDevice manualFramingDeviceType].cold.1
+ -[AVCaptureDALDevice manualFramingDeviceType].cold.2
+ -[AVCaptureDALDevice manualFramingDeviceType].cold.3
+ -[AVCaptureDALDevice manualFramingDeviceType].cold.4
+ -[AVCaptureDALDevice relinquishDeviceMaster].cold.1
+ -[AVCaptureDALDevice setActiveFormat:].cold.1
+ -[AVCaptureDALDevice setActiveFormat:].cold.2
+ -[AVCaptureDALDevice setActiveFormat:].cold.3
+ -[AVCaptureDALDevice setActiveFormat:].cold.4
+ -[AVCaptureDALDevice setActiveFormat:].cold.5
+ -[AVCaptureDALDevice setActiveInputSource:].cold.1
+ -[AVCaptureDALDevice setActiveInputSource:].cold.2
+ -[AVCaptureDALDevice setActiveVideoMaxFrameDuration:].cold.1
+ -[AVCaptureDALDevice setActiveVideoMinFrameDuration:].cold.1
+ -[AVCaptureDALDevice setAutomaticallyAdjustsFeatureControls:].cold.1
+ -[AVCaptureDALDevice setAutomaticallyAdjustsFeatureControls:].cold.2
+ -[AVCaptureDALDevice setAutomaticallyAdjustsFeatureControls:].cold.3
+ -[AVCaptureDALDevice setAutomaticallyAdjustsFeatureControls:].cold.4
+ -[AVCaptureDALDevice setAutomaticallyAdjustsFeatureControls:].cold.5
+ -[AVCaptureDALDevice setAutomaticallyAdjustsFeatureControls:].cold.6
+ -[AVCaptureDALDevice setAutomaticallyAdjustsFeatureControls:].cold.7
+ -[AVCaptureDALDevice setAutomaticallyAdjustsFeatureControls:].cold.8
+ -[AVCaptureDALDevice setAutomaticallyAdjustsFeatureControls:].cold.9
+ -[AVCaptureDALDevice setCenterStageRectOfInterest:].cold.1
+ -[AVCaptureDALDevice setDeskViewCameraMode:].cold.1
+ -[AVCaptureDALDevice setDeskViewCameraMode:].cold.2
+ -[AVCaptureDALDevice setDeskViewCameraMode:].cold.3
+ -[AVCaptureDALDevice setDeskViewCameraMode:].cold.4
+ -[AVCaptureDALDevice setDeskViewCameraMode:].cold.5
+ -[AVCaptureDALDevice setVideoZoomFactor:].cold.1
+ -[AVCaptureDALDevice setVideoZoomFactor:].cold.2
+ -[AVCaptureDALDevice setVideoZoomFactor:].cold.3
+ -[AVCaptureDALDevice setVideoZoomFactor:].cold.4
+ -[AVCaptureDALDevice setVideoZoomFactor:].cold.5
+ -[AVCaptureDALDevice startUsingDevice:].cold.1
+ -[AVCaptureDALDevice stopUsingDevice].cold.1
+ -[AVCaptureDALDevice stopUsingDevice].cold.2
+ -[AVCaptureDALDevice zoomFactorConstantsByManualFramingDeviceType].cold.1
+ -[AVCaptureDALDevice zoomFactorConstantsByManualFramingDeviceType].cold.2
+ -[AVCaptureDALDevice zoomFactorConstantsByManualFramingDeviceType].cold.3
+ -[AVCaptureDALDevice zoomFactorConstantsByManualFramingDeviceType].cold.4
+ -[AVCaptureDALDevice(AVCaptureDeviceExposure) setExposureMode:].cold.1
+ -[AVCaptureDALDevice(AVCaptureDeviceExposure) setExposureMode:].cold.2
+ -[AVCaptureDALDevice(AVCaptureDeviceFocus) setFocusMode:].cold.1
+ -[AVCaptureDALDevice(AVCaptureDeviceTransportControls) setTransportControlsPlaybackMode:speed:].cold.1
+ -[AVCaptureDALDevice(AVCaptureDeviceWhiteBalance) setWhiteBalanceMode:].cold.1
+ -[AVCaptureDALDevice(AVCaptureDeviceWhiteBalance) setWhiteBalanceMode:].cold.2
+ -[AVCaptureDepthDataOutput companionSettingsVideoDataOutput]
+ -[AVCaptureDepthDataOutput setCompanionSettingsVideoDataOutput:]
+ -[AVCaptureDepthDataOutput_Tundra companionSettingsVideoDataOutput]
+ -[AVCaptureDepthDataOutput_Tundra connectionMediaTypes].cold.1
+ -[AVCaptureDepthDataOutput_Tundra setCompanionSettingsVideoDataOutput:]
+ -[AVCaptureDevice _startUsingDevice:].cold.1
+ -[AVCaptureDevice isFaceOcclusionDetectionSupported]
+ -[AVCaptureDevice supportedMetadataObjectIdentifiersForZeroFrameDelaySynchronization]
+ -[AVCaptureDeviceInput_Tundra _refreshDALDeviceSuppressedGesturesEnabled]
+ -[AVCaptureDeviceInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.1
+ -[AVCaptureDeviceInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.2
+ -[AVCaptureDeviceInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.3
+ -[AVCaptureDeviceInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.4
+ -[AVCaptureDeviceInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.5
+ -[AVCaptureDeviceInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.6
+ -[AVCaptureDeviceInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.7
+ -[AVCaptureDeviceInput_Tundra removeInputUnitsForInputPort:fromGraph:ofCaptureSession:].cold.1
+ -[AVCaptureDeviceInput_Tundra removeInputUnitsForInputPort:fromGraph:ofCaptureSession:].cold.2
+ -[AVCaptureDevice_Tundra _startUsingDevice:].cold.1
+ -[AVCaptureFigVideoDevice _cameraAccessIsEnabled]
+ -[AVCaptureFigVideoDevice _initDegradedCaptureQualityFactors].cold.1
+ -[AVCaptureFigVideoDevice _setExposureWithMode:duration:ISO:requestID:newMaxFrameDuration:].cold.1
+ -[AVCaptureFigVideoDevice _setFigCaptureSource:allowSendingWorkToMainThread:].cold.1
+ -[AVCaptureFigVideoDevice _setFocusWithMode:lensPosition:requestID:].cold.1
+ -[AVCaptureFigVideoDevice _setTorchMode:withLevel:].cold.1
+ -[AVCaptureFigVideoDevice _setTorchMode:withLevel:].cold.2
+ -[AVCaptureFigVideoDevice _updateActiveDepthDataFormatForContinuousZoomWithDepth].cold.1
+ -[AVCaptureFigVideoDevice _updateContinuousZoomWithDepthActiveWithEnabled:disallowed:isActiveDepthDataFormatChangingOut:].cold.1
+ -[AVCaptureFigVideoDevice _updateFigCaptureSourceObserverCounts].cold.1
+ -[AVCaptureFigVideoDevice _updateSuppressedGesturesEnabled:]
+ -[AVCaptureFigVideoDevice availableMetadataKeyGroupsSupportingZeroFrameDelaySynchronization]
+ -[AVCaptureFigVideoDevice deviceType].cold.1
+ -[AVCaptureFigVideoDevice deviceType].cold.2
+ -[AVCaptureFigVideoDevice isFaceOcclusionDetectionSupported]
+ -[AVCaptureFigVideoDevice supportedMetadataObjectIdentifiersForZeroFrameDelaySynchronization]
+ -[AVCaptureHALDevice _getDeviceChannelCount].cold.1
+ -[AVCaptureHALDevice _getDeviceChannelCount].cold.2
+ -[AVCaptureHALDevice _getDeviceChannelCount].cold.3
+ -[AVCaptureHALDevice _getDeviceChannelCount].cold.4
+ -[AVCaptureHALDevice _getDeviceChannelCount].cold.5
+ -[AVCaptureHALDevice _refreshFormatsAndKVONotify:].cold.1
+ -[AVCaptureHALDevice _refreshFormatsAndKVONotify:].cold.2
+ -[AVCaptureHALDevice _refreshFormatsAndKVONotify:].cold.3
+ -[AVCaptureHALDevice _refreshFormatsAndKVONotify:].cold.4
+ -[AVCaptureHALDevice _refreshFormatsAndKVONotify:].cold.5
+ -[AVCaptureHALDevice _refreshFormatsAndKVONotify:].cold.6
+ -[AVCaptureHALDevice _refreshInputSourcesAndKVONotify:].cold.1
+ -[AVCaptureHALDevice _refreshInputSourcesAndKVONotify:].cold.2
+ -[AVCaptureHALDevice _refreshInputSourcesAndKVONotify:].cold.3
+ -[AVCaptureHALDevice _refreshInputSourcesAndKVONotify:].cold.4
+ -[AVCaptureHALDevice isAlive].cold.1
+ -[AVCaptureHALDevice setActiveFormat:].cold.1
+ -[AVCaptureHALDevice setActiveInputSource:].cold.1
+ -[AVCaptureHALDevice startUsingDevice:].cold.1
+ -[AVCaptureInputPort_Tundra setGraph:node:element:scope:].cold.1
+ -[AVCaptureInputPort_Tundra setGraph:node:element:scope:].cold.2
+ -[AVCaptureMetadataOutput _emitCollections:]
+ -[AVCaptureMetadataOutput _emitCollections:].cold.1
+ -[AVCaptureMetadataOutput _emitSyncedCollections:]
+ -[AVCaptureMetadataOutput _faceIDReadinessCollectionForSampleBuffer:input:]
+ -[AVCaptureMetadataOutput _flushSynchronizedMetadataCollectionsQueue]
+ -[AVCaptureMetadataOutput _motionToWakeCollectionForSampleBuffer:input:]
+ -[AVCaptureMetadataOutput _newEmitTimerForSynchronizedMetadataCollections:]
+ -[AVCaptureMetadataOutput _processSynchronizationWithCollections:withCorrespondingMetadataObjectTypes:]
+ -[AVCaptureMetadataOutput _updateSynchronizationEnabledStatus]
+ -[AVCaptureMetadataOutput isAttentionForFaceIDReadinessRequired]
+ -[AVCaptureMetadataOutput isFaceOcclusionDetectionEnabled]
+ -[AVCaptureMetadataOutput isFaceOcclusionDetectionSupported]
+ -[AVCaptureMetadataOutput isPeriocularForFaceIDReadinessEnabled]
+ -[AVCaptureMetadataOutput isSynchronizationEnabled]
+ -[AVCaptureMetadataOutput maxSynchronizationFrameDelay]
+ -[AVCaptureMetadataOutput metadataIdentifiersForMetadataObjectTypes:].cold.1
+ -[AVCaptureMetadataOutput metadataObjectTypesForMetadataIdentifiers:].cold.1
+ -[AVCaptureMetadataOutput metadataObjectTypesSupportingZeroFrameDelaySynchronization]
+ -[AVCaptureMetadataOutput motionToWakeTargetFrameRate]
+ -[AVCaptureMetadataOutput setAttentionForFaceIDReadinessRequired:]
+ -[AVCaptureMetadataOutput setFaceOcclusionDetectionEnabled:]
+ -[AVCaptureMetadataOutput setMaxSynchronizationFrameDelay:]
+ -[AVCaptureMetadataOutput setPeriocularForFaceIDReadinessEnabled:]
+ -[AVCaptureMetadataOutput setSynchronizationEnabled:]
+ -[AVCaptureMetadataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.1
+ -[AVCaptureMetadataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.2
+ -[AVCaptureMetadataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.3
+ -[AVCaptureMetadataOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.1
+ -[AVCaptureMovieFileOutput _cleanupDelegateWrappers:]
+ -[AVCaptureMovieFileOutput _cleanupDelegateWrappersPendingDidStopRecordingUnregistration]
+ -[AVCaptureMovieFileOutput startRecordingMovieWithSettings:delegate:].cold.1
+ -[AVCaptureMovieFileOutput startRecordingMovieWithSettings:delegate:].cold.2
+ -[AVCaptureMovieFileOutput startRecordingToOutputFileURL:recordingDelegate:].cold.1
+ -[AVCaptureMovieFileOutput_Tundra _controlFileWritingForConnection:busNumber:fileControlToken:].cold.1
+ -[AVCaptureMovieFileOutput_Tundra _controlFileWritingForConnection:busNumber:fileControlToken:].cold.2
+ -[AVCaptureMovieFileOutput_Tundra _controlFileWritingForConnection:busNumber:fileControlToken:].cold.3
+ -[AVCaptureMovieFileOutput_Tundra _controlFileWritingForConnection:busNumber:fileControlToken:].cold.4
+ -[AVCaptureMovieFileOutput_Tundra _forciblyStopFileWritingForRunningRecordingOperation].cold.1
+ -[AVCaptureMovieFileOutput_Tundra _forciblyStopFileWritingForRunningRecordingOperation].cold.2
+ -[AVCaptureMovieFileOutput_Tundra _startFileWritingForConnection:fileControlToken:runningRecordingOperationDescriptor:].cold.1
+ -[AVCaptureMovieFileOutput_Tundra _updateCompressorNodesForConnection:].cold.1
+ -[AVCaptureMovieFileOutput_Tundra _updateCompressorNodesForConnection:].cold.2
+ -[AVCaptureMovieFileOutput_Tundra _updateCompressorNodesForConnection:].cold.3
+ -[AVCaptureMovieFileOutput_Tundra _updateCompressorNodesForConnection:].cold.4
+ -[AVCaptureMovieFileOutput_Tundra _updateCompressorNodesForConnection:].cold.5
+ -[AVCaptureMovieFileOutput_Tundra _updateCompressorNodesForConnection:].cold.6
+ -[AVCaptureMovieFileOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.1
+ -[AVCaptureMovieFileOutput_Tundra _updateVideoFrameRateGovernorNodeForConnection:].cold.1
+ -[AVCaptureMovieFileOutput_Tundra _updateVideoFrameRateGovernorNodeForConnection:].cold.2
+ -[AVCaptureMovieFileOutput_Tundra _updateVideoFrameRateGovernorNodeForConnection:].cold.3
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.1
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.10
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.11
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.12
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.13
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.14
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.15
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.16
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.17
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.18
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.19
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.2
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.20
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.21
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.22
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.23
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.24
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.25
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.26
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.3
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.4
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.5
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.6
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.7
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.8
+ -[AVCaptureMovieFileOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.9
+ -[AVCaptureMovieFileOutput_Tundra connectionMediaTypes].cold.1
+ -[AVCaptureOutput _recommendedVideoOutputSettingsForConnection:sourceSettings:videoCodec:isIris:outputFileURL:].cold.1
+ -[AVCaptureOutput _recommendedVideoOutputSettingsForConnection:sourceSettings:videoCodec:isIris:outputFileURL:].cold.2
+ -[AVCaptureOutput recommendedOutputSettingsForConnection:sourceSettings:videoCodecType:fileType:isIris:outputFileURL:].cold.1
+ -[AVCaptureOutput_Tundra _preferredInputPixelBufferAttributesForConnection:].cold.1
+ -[AVCaptureOutput_Tundra _preferredInputPixelBufferAttributesForConnection:].cold.2
+ -[AVCaptureOutput_Tundra _preferredInputPixelBufferAttributesForConnection:].cold.3
+ -[AVCaptureOutput_Tundra configureAudioSplitter:mixer:converter:forGraph:connection:withSettings:audioFileType:forceConverterToPassThru:setClientSequenceID:].cold.1
+ -[AVCaptureOutput_Tundra configureAudioSplitter:mixer:converter:forGraph:connection:withSettings:audioFileType:forceConverterToPassThru:setClientSequenceID:].cold.2
+ -[AVCaptureOutput_Tundra configureAudioSplitter:mixer:converter:forGraph:connection:withSettings:audioFileType:forceConverterToPassThru:setClientSequenceID:].cold.3
+ -[AVCaptureOutput_Tundra configureAudioSplitter:mixer:converter:forGraph:connection:withSettings:audioFileType:forceConverterToPassThru:setClientSequenceID:].cold.4
+ -[AVCaptureOutput_Tundra configureAudioSplitter:mixer:converter:forGraph:connection:withSettings:audioFileType:forceConverterToPassThru:setClientSequenceID:].cold.5
+ -[AVCaptureOutput_Tundra configureAudioSplitter:mixer:converter:forGraph:connection:withSettings:audioFileType:forceConverterToPassThru:setClientSequenceID:].cold.6
+ -[AVCaptureOutput_Tundra configureAudioSplitter:mixer:converter:forGraph:connection:withSettings:audioFileType:forceConverterToPassThru:setClientSequenceID:].cold.7
+ -[AVCaptureOutput_Tundra configureAudioSplitter:mixer:converter:forGraph:connection:withSettings:audioFileType:forceConverterToPassThru:setClientSequenceID:].cold.8
+ -[AVCaptureOutput_Tundra setEnabled:forConnection:].cold.1
+ -[AVCapturePhoto portraitEffectsMatte].cold.1
+ -[AVCapturePhotoOutput _figCaptureIrisStillImageSettingsForAVCapturePhotoSettings:captureRequestIdentifier:delegate:connections:].cold.1
+ -[AVCapturePhotoOutput _figCaptureMovieFileRecordingSettingsForAVMomentCaptureMovieRecordingSettings:momentCaptureSettings:delegate:connections:].cold.1
+ -[AVCapturePhotoOutput commitMomentCaptureToPhotoWithUniqueID:].cold.1
+ -[AVCapturePhotoOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.1
+ -[AVCapturePhotoOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.2
+ -[AVCapturePhotoOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.3
+ -[AVCapturePhotoOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.4
+ -[AVCapturePhotoOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.5
+ -[AVCapturePhotoOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.1
+ -[AVCapturePhotoOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.2
+ -[AVCapturePhotoOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.3
+ -[AVCapturePhotoOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.4
+ -[AVCapturePhotoOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.5
+ -[AVCapturePhotoOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.6
+ -[AVCapturePhotoOutput_Tundra capturePhotoWithSettings:delegate:].cold.1
+ -[AVCapturePhotoOutput_Tundra connectionMediaTypes].cold.1
+ -[AVCapturePhotoOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.1
+ -[AVCapturePhotoOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.2
+ -[AVCapturePhotoOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.3
+ -[AVCapturePhotoOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.4
+ -[AVCapturePhoto_Tundra fileDataRepresentation].cold.1
+ -[AVCaptureProprietaryDefaultsSingleton setObserveFrameSenderServerEndpoints:endpointsChangedHandler:].cold.1
+ -[AVCaptureScreenInput_Tundra _flippedCropRectForCropRect:].cold.1
+ -[AVCaptureScreenInput_Tundra _getInputUnitProperty:bytes:length:].cold.1
+ -[AVCaptureScreenInput_Tundra _getInputUnitProperty:bytes:length:].cold.2
+ -[AVCaptureScreenInput_Tundra _setInputUnitProperty:bytes:length:].cold.1
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.1
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.10
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.11
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.12
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.13
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.14
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.2
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.3
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.4
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.5
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.6
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.7
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.8
+ -[AVCaptureScreenInput_Tundra _syncScreenInputWithSessionSettings].cold.9
+ -[AVCaptureScreenInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.1
+ -[AVCaptureScreenInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.2
+ -[AVCaptureScreenInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.3
+ -[AVCaptureScreenInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.4
+ -[AVCaptureScreenInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.5
+ -[AVCaptureScreenInput_Tundra addInputUnitsForInputPort:toGraph:ofCaptureSession:error:].cold.6
+ -[AVCaptureSession _canAddInput:failureReason:].cold.1
+ -[AVCaptureSession _createFigCaptureSession].cold.1
+ -[AVCaptureSession _createFigCaptureSession].cold.2
+ -[AVCaptureSession _setInterrupted:withReason:interruptor:]
+ -[AVCaptureSessionInternalState init].cold.1
+ -[AVCaptureSessionInternalState invalidate].cold.1
+ -[AVCaptureSession_Tundra _buildAndRunGraph].cold.1
+ -[AVCaptureSession_Tundra _buildAndRunGraph].cold.2
+ -[AVCaptureSession_Tundra _buildGraphUnitsForConnection:error:].cold.1
+ -[AVCaptureSession_Tundra _buildGraphUnitsForInputPort:error:].cold.1
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.1
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.10
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.11
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.12
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.13
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.14
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.15
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.16
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.17
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.18
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.19
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.2
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.3
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.4
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.5
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.6
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.7
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.8
+ -[AVCaptureSession_Tundra _buildSupportUnitsForAudioInputPort:error:].cold.9
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.1
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.10
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.11
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.12
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.2
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.3
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.4
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.5
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.6
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.7
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.8
+ -[AVCaptureSession_Tundra _buildSupportUnitsForClosedCaptionInputPort:error:].cold.9
+ -[AVCaptureSession_Tundra _buildSupportUnitsForGenericInputPort:error:].cold.1
+ -[AVCaptureSession_Tundra _buildSupportUnitsForGenericInputPort:error:].cold.2
+ -[AVCaptureSession_Tundra _buildSupportUnitsForGenericInputPort:error:].cold.3
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.1
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.10
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.11
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.12
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.2
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.3
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.4
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.5
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.6
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.7
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.8
+ -[AVCaptureSession_Tundra _buildSupportUnitsForMetadataObjectInputPort:error:].cold.9
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.1
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.10
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.11
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.12
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.13
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.14
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.15
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.16
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.17
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.18
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.19
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.2
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.20
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.21
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.22
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.23
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.24
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.25
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.26
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.3
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.4
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.5
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.6
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.7
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.8
+ -[AVCaptureSession_Tundra _buildSupportUnitsForVideoInputPort:error:].cold.9
+ -[AVCaptureSession_Tundra _configureAudioDecoderConverters].cold.1
+ -[AVCaptureSession_Tundra _configureAudioDecoderConverters].cold.2
+ -[AVCaptureSession_Tundra _configureAudioDecoderConverters].cold.3
+ -[AVCaptureSession_Tundra _connectGraphUnitsForAudioConnection:error:].cold.1
+ -[AVCaptureSession_Tundra _connectGraphUnitsForClosedCaptionConnection:error:].cold.1
+ -[AVCaptureSession_Tundra _connectGraphUnitsForGenericConnection:error:].cold.1
+ -[AVCaptureSession_Tundra _connectGraphUnitsForMetadataConnection:error:].cold.1
+ -[AVCaptureSession_Tundra _connectGraphUnitsForVideoConnection:error:].cold.1
+ -[AVCaptureSession_Tundra _graphIsInitialized].cold.1
+ -[AVCaptureSession_Tundra _graphIsRunning].cold.1
+ -[AVCaptureSession_Tundra _informActiveInputsAndOutputsThatGraphWillStopWithError:].cold.1
+ -[AVCaptureSession_Tundra _setRunning:].cold.1
+ -[AVCaptureSession_Tundra _setRunning:].cold.2
+ -[AVCaptureSession_Tundra _setRunning:].cold.3
+ -[AVCaptureSession_Tundra _setRunning:].cold.4
+ -[AVCaptureSession_Tundra _setUpSynchronizationClock].cold.1
+ -[AVCaptureSession_Tundra _setUpSynchronizationClock].cold.2
+ -[AVCaptureSession_Tundra _setupMasterSynchronizers].cold.1
+ -[AVCaptureSession_Tundra _setupMasterSynchronizers].cold.2
+ -[AVCaptureSession_Tundra _setupMasterSynchronizers].cold.3
+ -[AVCaptureSession_Tundra _setupMasterSynchronizers].cold.4
+ -[AVCaptureSession_Tundra _setupMasterSynchronizers].cold.5
+ -[AVCaptureSession_Tundra _setupMasterSynchronizers].cold.6
+ -[AVCaptureSession_Tundra _setupMasterSynchronizers].cold.7
+ -[AVCaptureSession_Tundra _setupMasterSynchronizers].cold.8
+ -[AVCaptureSession_Tundra _stopAndTearDownGraph].cold.1
+ -[AVCaptureSession_Tundra _stopAndTearDownGraph].cold.2
+ -[AVCaptureSession_Tundra decompressionSettingsDidChangeForConnection:].cold.1
+ -[AVCaptureSession_Tundra decompressionSettingsDidChangeForConnection:].cold.2
+ -[AVCaptureSession_Tundra decompressionSettingsDidChangeForConnection:].cold.3
+ -[AVCaptureSession_Tundra decompressionSettingsDidChangeForConnection:].cold.4
+ -[AVCaptureSession_Tundra decompressionSettingsDidChangeForConnection:].cold.5
+ -[AVCaptureSession_Tundra decompressionSettingsDidChangeForConnection:].cold.6
+ -[AVCaptureStillImageOutputUtils _encodeTransform:].cold.1
+ -[AVCaptureStillImageOutputUtils _encodeTransform:].cold.2
+ -[AVCaptureStillImageOutputUtils _encodeTransform:].cold.3
+ -[AVCaptureStillImageOutputUtils _encodeTransform:].cold.4
+ -[AVCaptureStillImageOutputUtils _encodeTransform:].cold.5
+ -[AVCaptureStillImageOutputUtils _rotationTransform:].cold.1
+ -[AVCaptureStillImageOutputUtils _rotationTransform:].cold.2
+ -[AVCaptureStillImageOutputUtils _rotationTransform:].cold.3
+ -[AVCaptureStillImageOutputUtils _rotationTransform:].cold.4
+ -[AVCaptureStillImageOutputUtils _rotationTransform:].cold.5
+ -[AVCaptureStillImageOutputUtils _rotationTransform:].cold.6
+ -[AVCaptureStillImageOutputUtils _rotationTransform:].cold.7
+ -[AVCaptureStillImageOutputUtils _rotationTransform:].cold.8
+ -[AVCaptureStillImageOutputUtils _rotationTransform:].cold.9
+ -[AVCaptureStillImageOutputUtils _transferTransform:].cold.1
+ -[AVCaptureStillImageOutputUtils _transferTransform:].cold.2
+ -[AVCaptureStillImageOutputUtils _transferTransform:].cold.3
+ -[AVCaptureStillImageOutputUtils _transferTransform:].cold.4
+ -[AVCaptureStillImageOutputUtils _transferTransform:].cold.5
+ -[AVCaptureStillImageOutputUtils _transferTransform:].cold.6
+ -[AVCaptureStillImageOutputUtils _transferTransform:].cold.7
+ -[AVCaptureStillImageOutputUtils _transferTransform:].cold.8
+ -[AVCaptureStillImageOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.1
+ -[AVCaptureStillImageOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.2
+ -[AVCaptureStillImageOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.3
+ -[AVCaptureStillImageOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.4
+ -[AVCaptureStillImageOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.5
+ -[AVCaptureStillImageOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.1
+ -[AVCaptureStillImageOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.2
+ -[AVCaptureStillImageOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.3
+ -[AVCaptureStillImageOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.4
+ -[AVCaptureStillImageOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.5
+ -[AVCaptureStillImageOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.6
+ -[AVCaptureStillImageOutput_Tundra connectionMediaTypes].cold.1
+ -[AVCaptureStillImageOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.1
+ -[AVCaptureStillImageOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.2
+ -[AVCaptureStillImageOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.3
+ -[AVCaptureStillImageOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.4
+ -[AVCaptureSynchronizedMetadataCollections addCollections:]
+ -[AVCaptureSynchronizedMetadataCollections dealloc]
+ -[AVCaptureSynchronizedMetadataCollections emitTimer]
+ -[AVCaptureSynchronizedMetadataCollections initWithMetadataCollections:expectedMetadataObjectTypes:]
+ -[AVCaptureSynchronizedMetadataCollections metadataCollections]
+ -[AVCaptureSynchronizedMetadataCollections metadataObjectTypes]
+ -[AVCaptureSynchronizedMetadataCollections metadataObjects]
+ -[AVCaptureSynchronizedMetadataCollections readyToEmit]
+ -[AVCaptureSynchronizedMetadataCollections setEmitTimer:]
+ -[AVCaptureSynchronizedMetadataCollections skipMetadataObjectTypes:]
+ -[AVCaptureSynchronizedMetadataCollections time]
+ -[AVCaptureVideoDataOutput isVideoSettingsAspectRatioOverrideOptimized]
+ -[AVCaptureVideoDataOutput_Tundra _updateCompressorNodesForConnection:].cold.1
+ -[AVCaptureVideoDataOutput_Tundra _updateCompressorNodesForConnection:].cold.2
+ -[AVCaptureVideoDataOutput_Tundra _updateCompressorNodesForConnection:].cold.3
+ -[AVCaptureVideoDataOutput_Tundra _updateCompressorNodesForConnection:].cold.4
+ -[AVCaptureVideoDataOutput_Tundra _updateCompressorNodesForConnection:].cold.5
+ -[AVCaptureVideoDataOutput_Tundra _updateCompressorNodesForConnection:].cold.6
+ -[AVCaptureVideoDataOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.1
+ -[AVCaptureVideoDataOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.2
+ -[AVCaptureVideoDataOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.3
+ -[AVCaptureVideoDataOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.4
+ -[AVCaptureVideoDataOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.5
+ -[AVCaptureVideoDataOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.6
+ -[AVCaptureVideoDataOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.7
+ -[AVCaptureVideoDataOutput_Tundra _updateVideoDecompressorNodeForConnection:].cold.8
+ -[AVCaptureVideoDataOutput_Tundra _updateVideoFrameRateGovernorNodeForConnection:].cold.1
+ -[AVCaptureVideoDataOutput_Tundra _updateVideoFrameRateGovernorNodeForConnection:].cold.2
+ -[AVCaptureVideoDataOutput_Tundra _updateVideoFrameRateGovernorNodeForConnection:].cold.3
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.1
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.10
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.11
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.12
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.13
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.2
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.3
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.4
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.5
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.6
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.7
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.8
+ -[AVCaptureVideoDataOutput_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.9
+ -[AVCaptureVideoDataOutput_Tundra connectionMediaTypes].cold.1
+ -[AVCaptureVideoDataOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.1
+ -[AVCaptureVideoDataOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.2
+ -[AVCaptureVideoDataOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.3
+ -[AVCaptureVideoDataOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.4
+ -[AVCaptureVideoDataOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.5
+ -[AVCaptureVideoDataOutput_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.6
+ -[AVCaptureVideoPreviewLayer(_AVCaptureVideoPreviewLayerMetadataObjectDrawing) _setUpMetadataObjectLayerAttributes].cold.1
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.1
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.10
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.11
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.12
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.2
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.3
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.4
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.5
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.6
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.7
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.8
+ -[AVCaptureVideoPreviewLayer_Tundra addOutputUnitsForConnection:toGraph:ofCaptureSession:error:].cold.9
+ -[AVCaptureVideoPreviewLayer_Tundra connectionMediaTypes].cold.1
+ -[AVCaptureVideoPreviewLayer_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.1
+ -[AVCaptureVideoPreviewLayer_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.2
+ -[AVCaptureVideoPreviewLayer_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.3
+ -[AVCaptureVideoPreviewLayer_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.4
+ -[AVCaptureVideoPreviewLayer_Tundra removeOutputUnitsForConnection:fromGraph:ofCaptureSession:].cold.5
+ -[AVCaptureVideoPreviewLayer_Tundra setPaused:forConnection:].cold.1
+ -[AVCaptureVideoPreviewLayer_Tundra setPixelBufferAttributes:].cold.1
+ -[AVCaptureVideoPreviewLayer_Tundra setPixelBufferAttributes:].cold.2
+ -[AVContinuityCaptureOnBoardingManager showContinuityCaptureOnBoardingUIIfNeeded:deviceSupportsAllVideoEffectsFeatures:forceOpenDialog:].cold.1
+ -[AVContinuityCaptureOnBoardingManager showContinuityCaptureOnBoardingUIIfNeeded:deviceSupportsAllVideoEffectsFeatures:forceOpenDialog:].cold.2
+ -[AVContinuityCaptureOnBoardingManager showContinuityCaptureOnBoardingUIIfNeeded:deviceSupportsAllVideoEffectsFeatures:forceOpenDialog:].cold.3
+ -[AVControlCenterModuleState setupDeviceBasedModuleStatesIfNeeded].cold.1
+ -[AVDepthData _copyPixelBufferRepresentationWithPixelFormatType:].cold.1
+ -[AVDepthData _copyPixelBufferRepresentationWithPixelFormatType:].cold.2
+ -[AVDepthData copyAuxiliaryMetadata].cold.1
+ -[AVDepthData copyAuxiliaryMetadata].cold.10
+ -[AVDepthData copyAuxiliaryMetadata].cold.11
+ -[AVDepthData copyAuxiliaryMetadata].cold.12
+ -[AVDepthData copyAuxiliaryMetadata].cold.13
+ -[AVDepthData copyAuxiliaryMetadata].cold.2
+ -[AVDepthData copyAuxiliaryMetadata].cold.3
+ -[AVDepthData copyAuxiliaryMetadata].cold.4
+ -[AVDepthData copyAuxiliaryMetadata].cold.5
+ -[AVDepthData copyAuxiliaryMetadata].cold.6
+ -[AVDepthData copyAuxiliaryMetadata].cold.7
+ -[AVDepthData copyAuxiliaryMetadata].cold.8
+ -[AVDepthData copyAuxiliaryMetadata].cold.9
+ -[AVDepthData depthDataByReplacingDepthDataMapWithPixelBuffer:error:].cold.1
+ -[AVMetadataFaceIDReadinessObject coachingStatus]
+ -[AVMetadataFaceIDReadinessObject copyWithZone:]
+ -[AVMetadataFaceIDReadinessObject description]
+ -[AVMetadataFaceIDReadinessObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:]
+ -[AVMetadataFaceIDReadinessObject initWithReady:coachingStatus:userEngagementStatus:time:sourceCaptureInput:]
+ -[AVMetadataFaceIDReadinessObject isReady]
+ -[AVMetadataFaceIDReadinessObject userEngagementStatus]
+ -[AVMetadataFaceObject hasOccludedFeatures]
+ -[AVMetadataFaceObject occludedFeatures]
+ -[AVMetadataFaceObjectInternal hasOccludedFeatures]
+ -[AVMetadataFaceObjectInternal occludedFeatures]
+ -[AVMetadataFaceObjectInternal setHasOccludedFeatures:]
+ -[AVMetadataFaceObjectInternal setOccludedFeatures:]
+ -[AVMetadataMachineReadableCodeObject initWithFigEmbeddedCaptureDeviceMachineReadableCodeDictionary:input:].cold.1
+ -[AVMetadataMotionToWakeObject copyWithZone:]
+ -[AVMetadataMotionToWakeObject description]
+ -[AVMetadataMotionToWakeObject detectedMotion]
+ -[AVMetadataMotionToWakeObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:]
+ -[AVMetadataMotionToWakeObject initWithDetectedMotion:time:sourceCaptureInput:]
+ -[AVMetadataOfflineVideoStabilizationMotionObject initWithTime:motionDictionary:input:].cold.1
+ -[AVMetadataTrackedFacesObject initWithTime:faceTrackingDictionary:input:].cold.1
+ -[AVOfflineVideoStabilizer _copyStabilizedSampleBuffer:].cold.1
+ -[AVOfflineVideoStabilizer _setupVISProcessor].cold.1
+ -[AVOfflineVideoStabilizer _setupVISProcessor].cold.2
+ -[AVOfflineVideoStabilizer _setupVISProcessor].cold.3
+ -[AVOfflineVideoStabilizer _setupVISProcessor].cold.4
+ -[AVPortraitEffectsMatte copyAuxiliaryMetadata].cold.1
+ -[AVPortraitEffectsMatte copyAuxiliaryMetadata].cold.2
+ -[AVPortraitEffectsMatte copyAuxiliaryMetadata].cold.3
+ -[AVPortraitEffectsMatte portraitEffectsMatteByReplacingPortraitEffectsMatteWithPixelBuffer:error:].cold.1
+ -[AVPortraitEffectsMatte portraitEffectsMatteByReplacingPortraitEffectsMatteWithPixelBuffer:error:].cold.2
+ -[AVSemanticSegmentationMatte copyAuxiliaryMetadata].cold.1
+ -[AVSemanticSegmentationMatte copyAuxiliaryMetadata].cold.2
+ -[AVSemanticSegmentationMatte copyAuxiliaryMetadata].cold.3
+ -[AVSemanticSegmentationMatte semanticSegmentationMatteByReplacingSemanticSegmentationMatteWithPixelBuffer:error:].cold.1
+ -[AVSemanticSegmentationMatte semanticSegmentationMatteByReplacingSemanticSegmentationMatteWithPixelBuffer:error:].cold.2
+ -[CMIOProprietaryDefaultsSource imageForKey:fillWidth:fillHeight:].cold.1
+ -[CMIOProprietaryDefaultsSource imageForKey:fillWidth:fillHeight:].cold.2
+ -[CMIOProprietaryDefaultsSource imageForKey:fillWidth:fillHeight:].cold.3
+ -[CMIOProprietaryDefaultsSource imageForKey:fillWidth:fillHeight:].cold.4
+ -[CMIOProprietaryDefaultsSource imageForKey:fillWidth:fillHeight:].cold.5
+ -[CMIOProprietaryDefaultsSource imageForKey:fillWidth:fillHeight:].cold.6
+ -[CMIOProprietaryDefaultsSource imageForKey:fillWidth:fillHeight:].cold.7
+ -[CMIOProprietaryDefaultsSource updateCameraHistory:withCameraInfo:maxLength:updateCameraHistoryDownplayOverrideList:cameraCanBeInOverrideList:outNewCameraHistory:].cold.1
+ -[CMIOProprietaryDefaultsSource updateCameraHistory:withCameraInfo:maxLength:updateCameraHistoryDownplayOverrideList:cameraCanBeInOverrideList:outNewCameraHistory:].cold.2
+ -[CMIOProprietaryDefaultsSource updateCameraHistory:withCameraInfo:maxLength:updateCameraHistoryDownplayOverrideList:cameraCanBeInOverrideList:outNewCameraHistory:].cold.3
+ -[MediaIOGraphNodeDescription nodeFunctionalDesignation].cold.1
+ -[MediaIOGraphNodeDescription nodeIndex].cold.1
+ -[MediaIOGraphNodeDescription unit].cold.1
+ AVAUVoiceIOGetPreferredChatFlavorForBundleID.cold.1
+ AVAUVoiceIOGetSupportedChatFlavorsForBundleID.cold.1
+ AVAUVoiceIOInitializeListenersForBundleID.cold.1
+ AVAUVoiceIOIsAutoChatFlavorEnabledForBundleID.cold.1
+ AVAUVoiceIORemoveActiveChatFlavorForBundleID.cold.1
+ AVAUVoiceIOSetActiveChatFlavorForBundleID.cold.1
+ AVAUVoiceIOSetHiddenChatFlavorsForBundleID.cold.1
+ AVAUVoiceIOSetSupportedChatFlavorsForBundleID.cold.1
+ AVAUVoiceIOSetVoiceProcessingBypassedForBundleID.cold.1
+ AVAuxiliaryMetadataAddValue.cold.1
+ AVAuxiliaryMetadataAddValue.cold.2
+ AVCaptureBackgroundBlurUnavailableReasonsForFormat.cold.1
+ AVCaptureBackgroundReplacementUnavailableReasonsForFormat.cold.1
+ AVCaptureClientExpectsCameraMountedInLandscapeOrientation.cold.1
+ AVCaptureClientHasEntitlement.cameraStolenInterruptorAllowed
+ AVCaptureClientHasEntitlement.checkCameraStolenInterruptorOnceToken
+ AVCaptureClientIsCameraOrDerivative.cold.1
+ AVCaptureClientIsContinuityCapture.cold.1
+ AVCaptureClientIsFigCam.cold.1
+ AVCaptureClientIsFigCam.sAnswer
+ AVCaptureClientIsFigCam.sOnceToken
+ AVCaptureClientIsInternalTestTool.cold.1
+ AVCaptureConfigureClassForTundraPersonality.cold.1
+ AVCaptureCopyClientCodeSigningIdentifier.cold.1
+ AVCaptureCurrentClientIsFaceTimeVariant.cold.1
+ AVCaptureGetCurrentProcessAuditToken.cold.1
+ AVCaptureIsRunningInIOSAppOnMacEnvironment.cold.1
+ AVCaptureIsRunningInMacCatalystEnvironment.cold.1
+ AVCaptureIsRunningInMediaserverd.cold.1
+ AVCaptureIsRunningInXCTest.cold.1
+ AVCaptureMainScreenPixelSize.cold.1
+ AVCaptureMetadataObjectsOnly.cold.1
+ AVCapturePlatformMountsCamerasInLandscapeOrientation.cold.1
+ AVCaptureReactionEffectsUnavailableReasonsForFormat.cold.1
+ AVCaptureReactionSystemImageNameForType.cold.1
+ AVCaptureScreenInputGetCaptureWidthAndHeightForScaleFactor.cold.1
+ AVCaptureScreenInputGetCaptureWidthAndHeightForScaleFactor.cold.2
+ AVCaptureScreenInputGetCaptureWidthAndHeightForScaleFactor.cold.3
+ AVCaptureSessionIsLaunchPrewarmingEnabled.cold.1
+ AVCaptureSetUpMethodPosingForTundraClass.cold.1
+ AVCaptureShouldThrowForAPIViolations.cold.1
+ AVCaptureStudioLightingUnavailableReasonsForFormat.cold.1
+ AVCaptureTundraPersonalityEnabled.cold.1
+ AVCaptureTundraPersonalityEnabled.cold.2
+ AVControlCenterAudioAreMicrophoneModesSupported.cold.1
+ AVControlCenterAudioDefaultIsAutoMicrophoneEnabledForBundleIDAndMicMode.cold.1
+ AVControlCenterAudioDefaultSupportedMicrophoneModesForBundleID.cold.1
+ AVControlCenterAudioMicrophoneMGAutoMode.cold.1
+ AVControlCenterModulesPrewarm.cold.1
+ AVControlCenterPreferencesDomainForPreferencesDomain.cold.1
+ AVControlCenterVideoEffectsObserveGesturesDefaultDisabled.cold.1
+ AVGestaltGetBoolAnswer.cold.1
+ AVGestaltGetBoolAnswerWithDefault.cold.1
+ AVGestaltGetBoolAnswerWithError.cold.1
+ AVGestaltGetFloatAnswer.cold.1
+ AVGestaltGetFloatAnswerWithDefault.cold.1
+ AVGestaltGetFloatAnswerWithError.cold.1
+ AVGestaltGetIntegerAnswer.cold.1
+ AVGestaltGetIntegerAnswerWithDefault.cold.1
+ AVGestaltGetIntegerAnswerWithError.cold.1
+ AVGestaltGetQuestions.cold.1
+ AVGestaltGetStringAnswer.cold.1
+ AVGestaltGetStringAnswerWithDefault.cold.1
+ AVGestaltGetStringAnswerWithError.cold.1
+ AVGestaltIsQuestionValid.cold.1
+ AVMediaTypeForMetadataObjects.cold.1
+ AVMediaTypeMetadataObjectAndAVMediaTypeMetadataAreDefined.cold.1
+ AVMetadataItemIdentifierForItemIndex.cold.1
+ AVMetadataItemIdentifierForItemIndex.cold.2
+ AVMetadataMakeMetadataObjectFromBoxedMetadata.cold.1
+ AVMetadataMakeMetadataObjectFromBoxedMetadata.cold.10
+ AVMetadataMakeMetadataObjectFromBoxedMetadata.cold.2
+ AVMetadataMakeMetadataObjectFromBoxedMetadata.cold.3
+ AVMetadataMakeMetadataObjectFromBoxedMetadata.cold.4
+ AVMetadataMakeMetadataObjectFromBoxedMetadata.cold.5
+ AVMetadataMakeMetadataObjectFromBoxedMetadata.cold.6
+ AVMetadataMakeMetadataObjectFromBoxedMetadata.cold.7
+ AVMetadataMakeMetadataObjectFromBoxedMetadata.cold.8
+ AVMetadataMakeMetadataObjectFromBoxedMetadata.cold.9
+ AVMetadataObjectCreateBoxedMetadataFromFaceObjectAndFormatDescription.cold.1
+ AVMetadataObjectCreateBoxedMetadataFromFaceObjectAndFormatDescription.cold.10
+ AVMetadataObjectCreateBoxedMetadataFromFaceObjectAndFormatDescription.cold.2
+ AVMetadataObjectCreateBoxedMetadataFromFaceObjectAndFormatDescription.cold.3
+ AVMetadataObjectCreateBoxedMetadataFromFaceObjectAndFormatDescription.cold.4
+ AVMetadataObjectCreateBoxedMetadataFromFaceObjectAndFormatDescription.cold.5
+ AVMetadataObjectCreateBoxedMetadataFromFaceObjectAndFormatDescription.cold.6
+ AVMetadataObjectCreateBoxedMetadataFromFaceObjectAndFormatDescription.cold.7
+ AVMetadataObjectCreateBoxedMetadataFromFaceObjectAndFormatDescription.cold.8
+ AVMetadataObjectCreateBoxedMetadataFromFaceObjectAndFormatDescription.cold.9
+ AVSmartStyleSettingsGetSystemStyleEnabledStateForCameraApps.cold.1
+ ConnectionFormatDescriptionListener.cold.1
+ CreateCVImageBufferFromCMSampleBuffer.cold.1
+ CreateCVImageBufferFromCMSampleBuffer.cold.2
+ DeviceIsAliveListener.cold.1
+ GCC_except_table100
+ GCC_except_table105
+ GCC_except_table112
+ GCC_except_table378
+ GCC_except_table384
+ GCC_except_table575
+ GCC_except_table591
+ GCC_except_table610
+ GCC_except_table627
+ GCC_except_table630
+ GCC_except_table659
+ GCC_except_table663
+ GCC_except_table665
+ GCC_except_table68
+ GCC_except_table692
+ GCC_except_table704
+ GCC_except_table706
+ GCC_except_table708
+ GCC_except_table714
+ GCC_except_table718
+ GCC_except_table761
+ GCC_except_table770
+ MediaIOGraphConnectNodeToFanOutNode.cold.1
+ MediaIOGraphConnectNodeToFanOutNode.cold.2
+ MediaIOGraphConnectNodeToFanOutNode.cold.3
+ MediaIOGraphConnectNodeToFanOutNode.cold.4
+ MediaIOGraphConnectNodeToFanOutNode.cold.5
+ MediaIOGraphRemoveAllNodes.cold.1
+ MediaIOGraphRemoveAllNodes.cold.2
+ MediaIOGraphRemoveAllNodes.cold.3
+ OBJC_IVAR_$_AVCaptureConnectionInternal.cameraCalibrationDataInputPort
+ OBJC_IVAR_$_AVCaptureConnectionInternal.pointCloudDataInputPort
+ OBJC_IVAR_$_AVCaptureConnectionInternal.visionDataInputPort
+ OBJC_IVAR_$_AVCaptureDALDevice._lostCMIODeviceOnError
+ OBJC_IVAR_$_AVCaptureDALDevice._sharedSuppressedGesture
+ OBJC_IVAR_$_AVCaptureDALDevice._sharedSuppressedGesturesEnabled
+ OBJC_IVAR_$_AVCaptureDepthDataOutputInternal.companionSettingsVideoDataOutput
+ OBJC_IVAR_$_AVCaptureFigVideoDevice._captureSourceSupportedZeroFrameDelaySynchronizationMetadata
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.attentionForFaceIDReadinessRequired
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.faceOcclusionDetectionEnabled
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.maxSynchronizationFrameDelay
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.periocularForFaceIDReadinessEnabled
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.synchronizationEnabled
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.synchronizationEnabledByClient
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.synchronizationQueueFlushTimer
+ OBJC_IVAR_$_AVCaptureMetadataOutputInternal.synchronizedMetadataCollectionsQueue
+ OBJC_IVAR_$_AVCaptureSynchronizedMetadataCollections._collections
+ OBJC_IVAR_$_AVCaptureSynchronizedMetadataCollections._emitTimer
+ OBJC_IVAR_$_AVCaptureSynchronizedMetadataCollections._expectedMetadataObjectTypes
+ OBJC_IVAR_$_AVCaptureSynchronizedMetadataCollections._handledMetadataObjectTypes
+ OBJC_IVAR_$_AVCaptureSynchronizedMetadataCollections._time
+ OBJC_IVAR_$_AVMetadataFaceIDReadinessObject._coachingStatus
+ OBJC_IVAR_$_AVMetadataFaceIDReadinessObject._ready
+ OBJC_IVAR_$_AVMetadataFaceIDReadinessObject._userEngagementStatus
+ OBJC_IVAR_$_AVMetadataFaceObjectInternal._hasOccludedFeatures
+ OBJC_IVAR_$_AVMetadataFaceObjectInternal._occludedFeatures
+ OBJC_IVAR_$_AVMetadataMotionToWakeObject._detectedMotion
+ _AVCaptureClientApplicationIdentifierAnimoji
+ _AVCaptureClientApplicationIdentifierCamera
+ _AVCaptureClientApplicationIdentifierCameraMessagesApp
+ _AVCaptureClientApplicationIdentifierContinuityCaptureD
+ _AVCaptureClientApplicationIdentifierDeskView
+ _AVCaptureClientApplicationIdentifierFaceTime
+ _AVCaptureClientApplicationIdentifierInCallService
+ _AVCaptureClientApplicationIdentifierMeasure
+ _AVCaptureClientApplicationIdentifierMusic
+ _AVCaptureClientApplicationIdentifierNetworkEndpointUI
+ _AVCaptureClientApplicationIdentifierPhotoBooth
+ _AVCaptureClientApplicationIdentifierQuickTime
+ _AVCaptureClientApplicationIdentifierRelatived
+ _AVCaptureClientApplicationIdentifierReplayD
+ _AVCaptureClientApplicationIdentifierReplayD_obsolete
+ _AVCaptureClientApplicationIdentifierSidecarExtensionCapture
+ _AVCaptureClientIdentifierFigCam
+ _AVCaptureClientIsFigCam
+ _AVCaptureEntitlementCameraStolenInterruptor
+ _AVCaptureFigVideoDeviceSuppressedGesturesEnabledChangedContext
+ _AVCaptureOutputDimensionsHaveSameAspectRatio
+ _AVCaptureOutputFitAspectInsideDimensions
+ _AVCaptureSessionCameraStolenInterruptorKey
+ _AVControlCenterModuleStateForBundleID.cold.1
+ _AVMetadataObjectTypeFaceIDReadiness
+ _AVMetadataObjectTypeMotionToWake
+ _AVSmartStyleSettingsStateForBundleID.cold.1
+ _CMTimeAbsoluteValue
+ _OBJC_CLASS_$_AVCaptureSynchronizedMetadataCollections
+ _OBJC_CLASS_$_AVMetadataFaceIDReadinessObject
+ _OBJC_CLASS_$_AVMetadataMotionToWakeObject
+ _OBJC_CLASS_$_FigCameraCalibrationDataCaptureConnectionConfiguration
+ _OBJC_CLASS_$_FigCaptureCameraCalibrationDataSinkConfiguration
+ _OBJC_CLASS_$_FigCapturePointCloudDataSinkConfiguration
+ _OBJC_CLASS_$_FigCaptureVideoThumbnailSinkConfiguration
+ _OBJC_CLASS_$_FigCaptureVisionDataSinkConfiguration
+ _OBJC_CLASS_$_FigPointCloudDataCaptureConnectionConfiguration
+ _OBJC_CLASS_$_FigVisionDataCaptureConnectionConfiguration
+ _OBJC_METACLASS_$_AVCaptureSynchronizedMetadataCollections
+ _OBJC_METACLASS_$_AVMetadataFaceIDReadinessObject
+ _OBJC_METACLASS_$_AVMetadataMotionToWakeObject
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _StreamSharedSuppressedGestureListener
+ _StreamSharedSuppressedGesturesEnabledListener
+ __102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke.224
+ __102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke.279
+ __102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_2.283
+ __110-[AVCaptureFigVideoDevice setPrimaryConstituentDeviceSwitchingBehavior:restrictedSwitchingBehaviorConditions:]_block_invoke.638
+ __110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke.204
+ __110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke.207
+ __122-[CMIOProprietaryDefaultsSource initWithDefaultChangedHandler:frameSenderEndpointsChangedHandler:connectionBrokenHandler:]_block_invoke.cold.1
+ __122-[CMIOProprietaryDefaultsSource initWithDefaultChangedHandler:frameSenderEndpointsChangedHandler:connectionBrokenHandler:]_block_invoke.cold.2
+ __384-[AVCapturePhoto _fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:replacementPortraitEffectsMatte:replacementHairSegmentationMatte:replacementSkinSegmentationMatte:replacementTeethSegmentationMatte:replacementGlassesSegmentationMatte:replacementRawCompressionSettings:exceptionReason:]_block_invoke.cold.1
+ __39+[AVCaptureDALDevice _ensureDeviceList]_block_invoke.cold.1
+ __39+[AVCaptureHALDevice _ensureDeviceList]_block_invoke.cold.1
+ __41-[AVCaptureFigVideoDevice _setConnected:]_block_invoke.364
+ __42-[AVCaptureFigVideoDevice _setTorchLevel:]_block_invoke.492
+ __43-[AVCaptureFigVideoDevice setExposureMode:]_block_invoke.409
+ __52+[AVCaptureAudioFileOutput availableOutputFileTypes]_block_invoke.cold.1
+ __52+[AVCaptureAudioFileOutput availableOutputFileTypes]_block_invoke.cold.2
+ __52+[AVCaptureAudioFileOutput availableOutputFileTypes]_block_invoke.cold.3
+ __52+[AVCaptureAudioFileOutput availableOutputFileTypes]_block_invoke.cold.4
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.690
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.693
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.705
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.718
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.718.cold.1
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.727
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.736
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.739
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.765
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.779
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.697
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.706
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.720
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.729
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.740
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.766
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.780
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.698
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.707
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.724
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.747
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.767
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.781
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.711
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.725
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.751
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.768
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.785
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.712
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.726
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.752
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.772
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_6.713
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_6.756
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_6.773
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_7.714
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_7.757
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_8.715
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_8.758
+ __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_9.759
+ __56-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]_block_invoke.608
+ __57-[AVControlCenterModuleState cmioPropertyListener:count:]_block_invoke.188
+ __59+[AVCaptureAudioFileOutput_Tundra availableOutputFileTypes]_block_invoke.cold.1
+ __59+[AVCaptureAudioFileOutput_Tundra availableOutputFileTypes]_block_invoke.cold.2
+ __59+[AVCaptureAudioFileOutput_Tundra availableOutputFileTypes]_block_invoke.cold.3
+ __59+[AVCaptureAudioFileOutput_Tundra availableOutputFileTypes]_block_invoke.cold.4
+ __64-[AVControlCenterModuleState installProprietaryDefaultsHandlers]_block_invoke.199
+ __65+[AVCaptureDALDevice setOnAllCMIOPlugInsTheUInt32Property:value:]_block_invoke.cold.1
+ __65+[AVCaptureDALDevice setOnAllCMIOPlugInsTheUInt32Property:value:]_block_invoke.cold.2
+ __65+[AVCaptureDALDevice setOnAllCMIOPlugInsTheUInt32Property:value:]_block_invoke.cold.3
+ __65-[AVCaptureFigVideoDevice _ensureWhiteBalanceCalibrationUnpacked]_block_invoke.cold.1
+ __65-[AVCaptureFigVideoDevice _ensureWhiteBalanceCalibrationUnpacked]_block_invoke.cold.2
+ __65-[AVCaptureFigVideoDevice _ensureWhiteBalanceCalibrationUnpacked]_block_invoke.cold.3
+ __65-[AVCaptureFigVideoDevice _ensureWhiteBalanceCalibrationUnpacked]_block_invoke.cold.4
+ __65-[AVCaptureFigVideoDevice _ensureWhiteBalanceCalibrationUnpacked]_block_invoke.cold.5
+ __65-[AVCaptureFigVideoDevice _ensureWhiteBalanceCalibrationUnpacked]_block_invoke.cold.6
+ __65-[AVCaptureFigVideoDevice _ensureWhiteBalanceCalibrationUnpacked]_block_invoke.cold.7
+ __66-[AVControlCenterModuleState setupDeviceBasedModuleStatesIfNeeded]_block_invoke.242
+ __66-[AVControlCenterModuleState setupDeviceBasedModuleStatesIfNeeded]_block_invoke.249
+ __67-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:]_block_invoke.328
+ __67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.313
+ __67-[AVCaptureFigVideoDevice setExposureTargetBias:completionHandler:]_block_invoke.429
+ __72-[AVCaptureFigVideoDevice chromaticityValuesForDeviceWhiteBalanceGains:]_block_invoke.478
+ __74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.670
+ __74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.683
+ __74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke_2.684
+ __80-[AVCaptureFigVideoDevice setFocusModeLockedWithLensPosition:completionHandler:]_block_invoke.394
+ __83-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke.424
+ __88-[AVCaptureFigVideoDevice _rampToVideoZoomFactor:withRate:duration:rampType:rampTuning:]_block_invoke.545
+ __88-[AVCaptureFigVideoDevice _updateCenterStageActiveForEnabled:updateDependentProperties:]_block_invoke.557
+ __98-[AVCaptureFigVideoDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:]_block_invoke.474
+ __AVCaptureBackgroundBlurUnavailableReasonsForFormat_block_invoke.cold.1
+ __AVCaptureBackgroundReplacementUnavailableReasonsForFormat_block_invoke.cold.1
+ __AVCaptureClientExpectsCameraMountedInLandscapeOrientation_block_invoke.cold.1
+ __AVCaptureReactionEffectsUnavailableReasonsForFormat_block_invoke.cold.1
+ __AVCaptureShouldThrowForAPIViolations_block_invoke.cold.1
+ __AVCaptureStudioLightingUnavailableReasonsForFormat_block_invoke.cold.1
+ __AVControlCenterModulesPrewarm_block_invoke.478
+ __AVMediaTypeForMetadataObjects_block_invoke.cold.1
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_AVMetadataFaceIDReadinessObject
+ __OBJC_$_CLASS_METHODS_AVMetadataMotionToWakeObject
+ __OBJC_$_INSTANCE_METHODS_AVCaptureSynchronizedMetadataCollections
+ __OBJC_$_INSTANCE_METHODS_AVMetadataFaceIDReadinessObject
+ __OBJC_$_INSTANCE_METHODS_AVMetadataMotionToWakeObject
+ __OBJC_$_INSTANCE_VARIABLES_AVCaptureSynchronizedMetadataCollections
+ __OBJC_$_INSTANCE_VARIABLES_AVMetadataFaceIDReadinessObject
+ __OBJC_$_INSTANCE_VARIABLES_AVMetadataMotionToWakeObject
+ __OBJC_$_PROP_LIST_AVCaptureSynchronizedMetadataCollections
+ __OBJC_$_PROP_LIST_AVMetadataFaceIDReadinessObject
+ __OBJC_$_PROP_LIST_AVMetadataMotionToWakeObject
+ __OBJC_CLASS_PROTOCOLS_$_AVMetadataFaceIDReadinessObject
+ __OBJC_CLASS_PROTOCOLS_$_AVMetadataMotionToWakeObject
+ __OBJC_CLASS_RO_$_AVCaptureSynchronizedMetadataCollections
+ __OBJC_CLASS_RO_$_AVMetadataFaceIDReadinessObject
+ __OBJC_CLASS_RO_$_AVMetadataMotionToWakeObject
+ __OBJC_METACLASS_RO_$_AVCaptureSynchronizedMetadataCollections
+ __OBJC_METACLASS_RO_$_AVMetadataFaceIDReadinessObject
+ __OBJC_METACLASS_RO_$_AVMetadataMotionToWakeObject
+ ___53-[AVCaptureMovieFileOutput _cleanupDelegateWrappers:]_block_invoke
+ ___60-[AVCaptureFigVideoDevice _updateSuppressedGesturesEnabled:]_block_invoke
+ ___75-[AVCaptureMetadataOutput _newEmitTimerForSynchronizedMetadataCollections:]_block_invoke
+ ___AVCaptureClientIsFigCam_block_invoke
+ ___block_descriptor_48_e8_32o40w_e95_v28?0{FigLocalQueueMessage=i(?={?=^{opaqueCMSampleBuffer}}{?=q^{opaqueCMFormatDescription}})}8l
+ ___block_descriptor_48_e8_32w40w_e5_v8?0l
+ ___copy_helper_block_e8_32o40w
+ ___copy_helper_block_e8_32w40w
+ ___destroy_helper_block_e8_32o40w
+ ___destroy_helper_block_e8_32w40w
+ __block_literal_global.119
+ __block_literal_global.129
+ __block_literal_global.158
+ __block_literal_global.187
+ __block_literal_global.195
+ __block_literal_global.206
+ __block_literal_global.227
+ __block_literal_global.248
+ __block_literal_global.289
+ __block_literal_global.308
+ __block_literal_global.310
+ __block_literal_global.311
+ __block_literal_global.346
+ __block_literal_global.366
+ __block_literal_global.370
+ __block_literal_global.391
+ __block_literal_global.393
+ __block_literal_global.409
+ __block_literal_global.414
+ __block_literal_global.416
+ __block_literal_global.418
+ __block_literal_global.455
+ __block_literal_global.471
+ __block_literal_global.478
+ __block_literal_global.481
+ __block_literal_global.487
+ __block_literal_global.489
+ __block_literal_global.526
+ __block_literal_global.62
+ __block_literal_global.692
+ __block_literal_global.75
+ __block_literal_global.776
+ __block_literal_global.909
+ _addAuxiliaryImage.cold.1
+ _addAuxiliaryImage.cold.2
+ _addAuxiliaryImage.cold.3
+ _addAuxiliaryImage.cold.4
+ _avcaptureVideoStabilizationModeToFigCaptureVideoStabilizationMethod
+ _cpdXPCMessageSetCFString.cold.1
+ _cpdXPCMessageSetCFString.cold.2
+ _cpdXPCMessageSetCFString.cold.3
+ _dispatch_activate
+ _gAVCaptureMetadataOutputTrace
+ _getIsAliveForDevice
+ _getSuppressedGesturesEnabledForStream
+ _kFigCaptureMetadata_CorrespondingMetadataIdentifiers
+ _kFigCaptureSampleBufferAttachmentKey_FaceIDReadiness
+ _kFigCaptureSampleBufferAttachmentKey_MotionToWake
+ _kFigCaptureSessionNotificationPayloadKey_CameraStolenInterruptor
+ _kFigCaptureSourceAttributeKey_AvailableMetadataKeyGroups
+ _kFigCaptureSourceAttributeKey_AvailableMetadataKeyGroupsSupportingZeroFrameDelaySynchronization
+ _kFigCaptureSourceAttributeKey_FaceOcclusionDetectionSupported
+ _kFigCaptureSourceMetadataKeyGroup_ObjectDetection
+ _kFigCaptureSourceNotification_SuppressedGestureNotification
+ _kFigCaptureSourceProperty_SuppressedGesturesEnabled
+ _kFigCaptureStreamMetadata_FaceOccluded
+ _kFigCaptureStreamSecureFaceIDReadinessKey_CoachingStatus
+ _kFigCaptureStreamSecureFaceIDReadinessKey_Ready
+ _kFigCaptureStreamSecureFaceIDReadinessKey_UserEngagementStatus
+ _kFigCaptureStreamSecureMotionToWakeKey_DetectedMotion
+ _objc_loadWeak
+ _objc_msgSend$_cleanupDelegateWrappers:
+ _objc_msgSend$_cleanupDelegateWrappersPendingDidStopRecordingUnregistration
+ _objc_msgSend$_emitCollections:
+ _objc_msgSend$_emitSyncedCollections:
+ _objc_msgSend$_faceIDReadinessCollectionForSampleBuffer:input:
+ _objc_msgSend$_flushSynchronizedMetadataCollectionsQueue
+ _objc_msgSend$_motionToWakeCollectionForSampleBuffer:input:
+ _objc_msgSend$_newEmitTimerForSynchronizedMetadataCollections:
+ _objc_msgSend$_processSynchronizationWithCollections:withCorrespondingMetadataObjectTypes:
+ _objc_msgSend$_refreshDALDeviceSuppressedGesturesEnabled
+ _objc_msgSend$_setInterrupted:withReason:interruptor:
+ _objc_msgSend$_setSuppressedGesturesEnabled:
+ _objc_msgSend$_sharedSuppressedGestureForStream:
+ _objc_msgSend$_sharedSuppressedGesturesEnabledChangedForStream:
+ _objc_msgSend$_updateSuppressedGesturesEnabled:
+ _objc_msgSend$_updateSynchronizationEnabledStatus
+ _objc_msgSend$addCollections:
+ _objc_msgSend$alwaysDiscardsLateCameraCalibrationData
+ _objc_msgSend$alwaysDiscardsLatePointCloudData
+ _objc_msgSend$availableMetadataKeyGroupsSupportingZeroFrameDelaySynchronization
+ _objc_msgSend$coachingStatus
+ _objc_msgSend$companionSettingsVideoDataOutput
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$contents
+ _objc_msgSend$detectedMotion
+ _objc_msgSend$faceIDReadinessObjectWithReady:coachingStatus:userEngagementStatus:input:time:
+ _objc_msgSend$featureMatchingDescriptorSize
+ _objc_msgSend$filters
+ _objc_msgSend$gaussianPyramidBaseOctaveDownscalingFactor
+ _objc_msgSend$gaussianPyramidOctavesCount
+ _objc_msgSend$hammingDistanceThreshold
+ _objc_msgSend$hasOccludedFeatures
+ _objc_msgSend$initWithDetectedMotion:time:sourceCaptureInput:
+ _objc_msgSend$initWithMetadataCollections:expectedMetadataObjectTypes:
+ _objc_msgSend$initWithReady:coachingStatus:userEngagementStatus:time:sourceCaptureInput:
+ _objc_msgSend$isAttentionForFaceIDReadinessRequired
+ _objc_msgSend$isDynamicThresholdingEnabled
+ _objc_msgSend$isFaceOcclusionDetectionEnabled
+ _objc_msgSend$isFaceOcclusionDetectionSupported
+ _objc_msgSend$isFeatureBinningEnabled
+ _objc_msgSend$isFeatureMatchingEnabled
+ _objc_msgSend$isFeatureOrientationAssignmentEnabled
+ _objc_msgSend$isPeriocularForFaceIDReadinessEnabled
+ _objc_msgSend$isReady
+ _objc_msgSend$keypointDetectionFlowType
+ _objc_msgSend$keypointDetectionThreshold
+ _objc_msgSend$laccConfigAndMetadata
+ _objc_msgSend$maxBurstDuration
+ _objc_msgSend$maxKeypointsCount
+ _objc_msgSend$metadataCollections
+ _objc_msgSend$metadataObjectTypesSupportingZeroFrameDelaySynchronization
+ _objc_msgSend$minBurstFrameDuration
+ _objc_msgSend$motionToWakeObjectWithDetectedMotion:input:time:
+ _objc_msgSend$motionToWakeTargetFrameRate
+ _objc_msgSend$occludedFeatures
+ _objc_msgSend$orientationDistanceThreshold
+ _objc_msgSend$reactionEffectSuppressedGesturesEnabled
+ _objc_msgSend$readyToEmit
+ _objc_msgSend$setAttentionForFaceIDReadinessRequired:
+ _objc_msgSend$setDiscardsLateCameraCalibrationData:
+ _objc_msgSend$setDiscardsLatePointCloudData:
+ _objc_msgSend$setEmitTimer:
+ _objc_msgSend$setFaceOcclusionDetectionEnabled:
+ _objc_msgSend$setFilters:
+ _objc_msgSend$setHasOccludedFeatures:
+ _objc_msgSend$setLaccConfigAndMetadata:
+ _objc_msgSend$setMaxBurstFrameRate:
+ _objc_msgSend$setMaxFrameRate:
+ _objc_msgSend$setMotionToWakeTargetFrameRate:
+ _objc_msgSend$setOccludedFeatures:
+ _objc_msgSend$setPeriocularForFaceIDReadinessEnabled:
+ _objc_msgSend$setProjectorMode:
+ _objc_msgSend$setReactionEffectSuppressedGesture:
+ _objc_msgSend$setReactionEffectSuppressedGesturesEnabled:
+ _objc_msgSend$setSmartStyles:
+ _objc_msgSend$setThumbnailSize:
+ _objc_msgSend$sigmaDistanceThreshold
+ _objc_msgSend$skipMetadataObjectTypes:
+ _objc_msgSend$smartStyles
+ _objc_msgSend$squareDistanceDisparityFraction
+ _objc_msgSend$subPixelThreshold
+ _objc_msgSend$supportedMetadataObjectIdentifiersForZeroFrameDelaySynchronization
+ _objc_msgSend$thumbnailSize
+ _objc_msgSend$userEngagementStatus
+ _sHaveShownAppGesturesDefaultDisabledNotificationKey
+ _sHaveShownGlobalGesturesDefaultDisabledNotificationKey
+ _sSuppressedGesture
+ _sSuppressedGesturesEnabled
+ _sourceInfoArrayChangedNotification.cold.1
+ _sourceInfoArrayChangedNotification.cold.2
+ _sourceInfoArrayChangedNotification.cold.3
+ audioPreviewDeviceIDPropertyListener.cold.1
+ audioPreviewDeviceIDPropertyListener.cold.2
+ audioPreviewVolumePropertyListener.cold.1
+ deviceSupportsCenterStage.cold.1
+ deviceSupportsCenterStage.cold.2
+ deviceSupportsCenterStage.cold.3
+ deviceSupportsCenterStage.cold.4
+ graphicsSubsystemErrorStatusPropertyListener.cold.1
- +[AVCaptureFigVideoDevice _cameraAccessIsEnabled]
- -[AVCaptureSession _setInterrupted:withReason:]
- -[AVMetadataFaceObjectInternal hasPayingAttentionConfidence]
- -[AVMetadataFaceObjectInternal payingAttentionConfidence]
- -[AVMetadataFaceObjectInternal setHasPayingAttentionConfidence:]
- -[AVMetadataFaceObjectInternal setPayingAttentionConfidence:]
- GCC_except_table125
- GCC_except_table133
- GCC_except_table257
- GCC_except_table374
- GCC_except_table380
- GCC_except_table573
- GCC_except_table589
- GCC_except_table608
- GCC_except_table625
- GCC_except_table628
- GCC_except_table654
- GCC_except_table658
- GCC_except_table660
- GCC_except_table687
- GCC_except_table699
- GCC_except_table701
- GCC_except_table703
- GCC_except_table709
- GCC_except_table713
- GCC_except_table756
- GCC_except_table765
- OBJC_IVAR_$_AVCaptureFigVideoDevice._availableMetadataKeyGroups
- OBJC_IVAR_$_AVMetadataFaceObjectInternal._hasPayingAttentionConfidence
- OBJC_IVAR_$_AVMetadataFaceObjectInternal._payingAttentionConfidence
- __102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke.221
- __110-[AVCaptureFigVideoDevice setPrimaryConstituentDeviceSwitchingBehavior:restrictedSwitchingBehaviorConditions:]_block_invoke.630
- __110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke.203
- __110-[AVControlCenterModuleState updateActiveReactions:currentRenderPTS:requestedTriggers:forCaptureDeviceWithID:]_block_invoke.206
- __41-[AVCaptureFigVideoDevice _setConnected:]_block_invoke.356
- __42-[AVCaptureFigVideoDevice _setTorchLevel:]_block_invoke.484
- __43-[AVCaptureFigVideoDevice setExposureMode:]_block_invoke.401
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.682
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.685
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.697
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.710
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.719
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.720
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.731
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.757
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke.771
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.689
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.698
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.712
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.721
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.732
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.758
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_2.772
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.690
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.699
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.716
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.739
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.759
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_3.773
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.703
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.717
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.743
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.760
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_4.777
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.704
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.718
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.744
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_5.764
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_6.705
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_6.748
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_6.765
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_7.706
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_7.749
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_8.707
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_8.750
- __55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_9.751
- __56-[AVCaptureFigVideoDevice _setDepthDataDeliveryEnabled:]_block_invoke.600
- __57-[AVControlCenterModuleState cmioPropertyListener:count:]_block_invoke.187
- __64-[AVControlCenterModuleState installProprietaryDefaultsHandlers]_block_invoke.198
- __66-[AVControlCenterModuleState setupDeviceBasedModuleStatesIfNeeded]_block_invoke.241
- __66-[AVControlCenterModuleState setupDeviceBasedModuleStatesIfNeeded]_block_invoke.248
- __67-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:]_block_invoke.320
- __67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.305
- __67-[AVCaptureFigVideoDevice setExposureTargetBias:completionHandler:]_block_invoke.421
- __72-[AVCaptureFigVideoDevice chromaticityValuesForDeviceWhiteBalanceGains:]_block_invoke.470
- __74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.662
- __74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.675
- __74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke_2.676
- __80-[AVCaptureFigVideoDevice setFocusModeLockedWithLensPosition:completionHandler:]_block_invoke.386
- __83-[AVCaptureFigVideoDevice setExposureModeCustomWithDuration:ISO:completionHandler:]_block_invoke.416
- __88-[AVCaptureFigVideoDevice _rampToVideoZoomFactor:withRate:duration:rampType:rampTuning:]_block_invoke.537
- __88-[AVCaptureFigVideoDevice _updateCenterStageActiveForEnabled:updateDependentProperties:]_block_invoke.549
- __98-[AVCaptureFigVideoDevice setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:]_block_invoke.466
- __AVControlCenterModulesPrewarm_block_invoke.477
- ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_13
- ___102-[AVCaptureFigVideoDevice _setActiveFormat:resetVideoZoomFactorAndMinMaxFrameDurations:sessionPreset:]_block_invoke_14
- ___82-[AVCaptureMovieFileOutput safelyHandleServerConnectionDeathForFigCaptureSession:]_block_invoke
- __block_literal_global.114
- __block_literal_global.124
- __block_literal_global.145
- __block_literal_global.157
- __block_literal_global.184
- __block_literal_global.192
- __block_literal_global.226
- __block_literal_global.284
- __block_literal_global.303
- __block_literal_global.306
- __block_literal_global.307
- __block_literal_global.340
- __block_literal_global.358
- __block_literal_global.361
- __block_literal_global.383
- __block_literal_global.385
- __block_literal_global.398
- __block_literal_global.401
- __block_literal_global.408
- __block_literal_global.410
- __block_literal_global.449
- __block_literal_global.469
- __block_literal_global.470
- __block_literal_global.477
- __block_literal_global.480
- __block_literal_global.488
- __block_literal_global.522
- __block_literal_global.525
- __block_literal_global.684
- __block_literal_global.71
- __block_literal_global.773
- __block_literal_global.900
- _kFigCaptureSourceProperty_AvailableMetadataKeyGroups
- _kFigCaptureStreamMetadata_AttentionConfidenceLevel
- _objc_msgSend$_setInterrupted:withReason:
- _objc_msgSend$hasPayingAttentionConfidence
- _objc_msgSend$payingAttentionConfidence
- _objc_msgSend$setHasPayingAttentionConfidence:
- _objc_msgSend$setPayingAttentionConfidence:
- _sHaveShownGesturesDefaultDisabledNotificationKey
- _vpl_CTFontCreateUIFontForLanguage
- _vpl_kCTFontAttributeName
- _vpl_kCTForegroundColorAttributeName
- _vpl_kCTStrokeColorAttributeName
- _vpl_kCTStrokeWidthAttributeName
CStrings:
+ "%@: %p motion: %d"
+ "%@: %p ready: %d, coachingStatus: %d, userEngagementStatus: %d"
+ "( session != ((void*)0) ) ^ ( dngCompressor != ((void*)0) )"
+ ", confidence=%.2f"
+ ", translation:(%@)"
+ "-[AVCaptureDALDevice _sharedSuppressedGestureForStream:]"
+ "-[AVCaptureDALDevice _sharedSuppressedGesturesEnabledChangedForStream:]"
+ "-[AVCaptureSession _setInterrupted:withReason:interruptor:]"
+ "-[AVCaptureVideoPreviewLayer _handleNotification:payload:]"
+ "/System/AppleInternal/Library/Frameworks/TelephonyUtilities.framework/TelephonyUtilities"
+ "<<<< AVCaptureDALDevice >>>> %s: Device is not running anywhere else. Setting reactionEffectsEnabled on device to:%c (gestures to %d, suppressed gestures to %d) for %{public}@"
+ "<<<< AVCaptureDALDevice >>>> %s: Device is running somewhere else. Resetting to shared reactionEffectsEnabled:%c gesturesEnabled:%d suppressedGesturesEnabled:%d for %{public}@"
+ "<<<< AVCaptureDALDevice >>>> %s: _sharedSuppressedGesture is changing from %d to %d for %@"
+ "<<<< AVCaptureDALDevice >>>> %s: _sharedSuppressedGesturesEnabled is changing from %d to %d for %@"
+ "<<<< AVCaptureDALDevice >>>> %s: updating suppressed gesture:%d for %@"
+ "<<<< AVCaptureDALDevice >>>> %s: updating suppressed gestures enabled:%d for %@"
+ "<<<< AVCaptureDevice >>>> %s: Suppressed gestures %d : enabled %d have shown %d"
+ "<<<< AVCaptureVideoPreviewLayer >>>> %s: preview started - contents = %@, imageQueueSlot = %d"
+ "@\"AVCaptureVideoDataOutput\""
+ "@56@0:8Q16@24{?=qiIq}32"
+ "@56@0:8Q16{?=qiIq}24@48"
+ "@68@0:8B16q20q28@36{?=qiIq}44"
+ "@68@0:8B16q20q28{?=qiIq}36@60"
+ "AVCaptureSessionCameraStolenInterruptorKey"
+ "AVCaptureSynchronizedMetadataCollections"
+ "AVMetadataFaceIDReadinessObject"
+ "AVMetadataMotionToWakeObject"
+ "Adding stream suppressed gesture property listener"
+ "Adding stream suppressed gestures enabled property listener"
+ "FaceIDReadiness"
+ "MotionToWake"
+ "Not available - use -hasOccludedFeatures"
+ "Removing stream suppressed gesture property listener"
+ "T@\"NSArray\",R,C"
+ "T@\"NSMutableSet\",R,C"
+ "T@\"NSObject<OS_dispatch_source>\",&"
+ "TB,N,V_hasOccludedFeatures"
+ "TB,N,V_occludedFeatures"
+ "TB,R,GisReady"
+ "TQ,R,V_detectedMotion"
+ "Unsupported - check for AVMetadataObjectTypeFaceIDReadiness in -availableMetadataObjectTypes"
+ "_captureSourceSupportedZeroFrameDelaySynchronizationMetadata"
+ "_cleanupDelegateWrappers:"
+ "_cleanupDelegateWrappersPendingDidStopRecordingUnregistration"
+ "_coachingStatus"
+ "_collections"
+ "_detectedMotion"
+ "_emitCollections:"
+ "_emitSyncedCollections:"
+ "_emitTimer"
+ "_expectedMetadataObjectTypes"
+ "_faceIDReadinessCollectionForSampleBuffer:input:"
+ "_flushSynchronizedMetadataCollectionsQueue"
+ "_hasOccludedFeatures"
+ "_lostCMIODeviceOnError"
+ "_motionToWakeCollectionForSampleBuffer:input:"
+ "_newEmitTimerForSynchronizedMetadataCollections:"
+ "_occludedFeatures"
+ "_processSynchronizationWithCollections:withCorrespondingMetadataObjectTypes:"
+ "_ready"
+ "_refreshDALDeviceSuppressedGesturesEnabled"
+ "_setInterrupted:withReason:interruptor:"
+ "_setSuppressedGesturesEnabled:"
+ "_sharedSuppressedGesture"
+ "_sharedSuppressedGestureForStream:"
+ "_sharedSuppressedGesturesEnabled"
+ "_sharedSuppressedGesturesEnabledChangedForStream:"
+ "_updateSuppressedGesturesEnabled:"
+ "_updateSynchronizationEnabledStatus"
+ "_userEngagementStatus"
+ "addCollections:"
+ "attentionForFaceIDReadinessRequired"
+ "audioLevelValues != ((void*)0)"
+ "availableMetadataKeyGroupsSupportingZeroFrameDelaySynchronization"
+ "avcapturemetadataoutput_trace"
+ "cameraCalibrationDataInputPort"
+ "cfObject != ((void*)0)"
+ "channelVolumes != ((void*)0)"
+ "coachingStatus"
+ "com.apple.Jellyfish.Animoji"
+ "com.apple.avfoundation.figcam"
+ "com.apple.private.avfoundation.capture.camera-stolen-interruptor.allow"
+ "com.apple.relatived"
+ "companionSettingsVideoDataOutput"
+ "componentsJoinedByString:"
+ "contents"
+ "description=CameraCapture_AVF-587.101.4"
+ "detectedMotion"
+ "displayMode != ((void*)0)"
+ "emitTimer"
+ "faceIDReadinessObjectWithReady:coachingStatus:userEngagementStatus:input:time:"
+ "faceOcclusionDetectionEnabled"
+ "global"
+ "hasOccludedFeatures"
+ "inNotificationPayload == ((void*)0)"
+ "inNotifyingObject != ((void*)0)"
+ "initWithDetectedMotion:time:sourceCaptureInput:"
+ "initWithMetadataCollections:expectedMetadataObjectTypes:"
+ "initWithReady:coachingStatus:userEngagementStatus:time:sourceCaptureInput:"
+ "inputSources != ((void*)0)"
+ "isAttentionForFaceIDReadinessRequired"
+ "isFaceOcclusionDetectionEnabled"
+ "isFaceOcclusionDetectionSupported"
+ "isPeriocularForFaceIDReadinessEnabled"
+ "isReady"
+ "isSynchronizationEnabled"
+ "isVideoSettingsAspectRatioOverrideOptimized"
+ "itemIdentifier != ((void*)0)"
+ "kAVCaptureDeviceInputSuppressedGesturesEnabledChangedContext"
+ "lite_shareddata"
+ "maxSynchronizationFrameDelay"
+ "mdta/com.apple.quicktime.faceid-readiness"
+ "mdta/com.apple.quicktime.motion-to-wake"
+ "message != ((void*)0)"
+ "metadataCollections"
+ "metadataObjectTypesSupportingZeroFrameDelaySynchronization"
+ "motionToWakeObjectWithDetectedMotion:input:time:"
+ "motionToWakeTargetFrameRate"
+ "occludedFeatures"
+ "periocularForFaceIDReadinessEnabled"
+ "pointCloudDataInputPort"
+ "pose"
+ "raw_data"
+ "reactionEffectSuppressedGesture"
+ "reactionEffectSuppressedGesturesEnabled"
+ "readyToEmit"
+ "setAttentionForFaceIDReadinessRequired:"
+ "setCompanionSettingsVideoDataOutput:"
+ "setDiscardsLateCameraCalibrationData:"
+ "setDiscardsLatePointCloudData:"
+ "setEmitTimer:"
+ "setFaceOcclusionDetectionEnabled:"
+ "setHasOccludedFeatures:"
+ "setMaxBurstFrameRate:"
+ "setMaxFrameRate:"
+ "setMaxSynchronizationFrameDelay:"
+ "setMotionToWakeTargetFrameRate:"
+ "setOccludedFeatures:"
+ "setPeriocularForFaceIDReadinessEnabled:"
+ "setProjectorMode:"
+ "setReactionEffectSuppressedGesture:"
+ "setReactionEffectSuppressedGesturesEnabled:"
+ "setSynchronizationEnabled:"
+ "skipMetadataObjectTypes:"
+ "streams != ((void*)0)"
+ "supportedMetadataObjectIdentifiersForZeroFrameDelaySynchronization"
+ "synchronizationEnabled"
+ "synchronizationEnabledByClient"
+ "synchronizationQueueFlushTimer"
+ "synchronizedMetadataCollectionsQueue"
+ "translation"
+ "userEngagementStatus"
+ "v32@0:8B16i20@24"
+ "visionDataInputPort"
+ "xpcObject != ((void*)0)"
- "( session != ((void *)0) ) ^ ( dngCompressor != ((void *)0) )"
- "-[AVCaptureSession _setInterrupted:withReason:]"
- "<<<< AVCaptureDALDevice >>>> %s: Device is not running anywhere else. Setting reactionEffectsEnabled on device to:%c (gestures to %d) for %{public}@"
- "<<<< AVCaptureDALDevice >>>> %s: Device is running somewhere else. Resetting to shared reactionEffectsEnabled:%c gesturesEnabled:%d for %{public}@"
- "MetadataGroup-ObjectDetection"
- "TB,N,V_hasPayingAttentionConfidence"
- "Td,N,V_payingAttentionConfidence"
- "_availableMetadataKeyGroups"
- "_hasPayingAttentionConfidence"
- "_payingAttentionConfidence"
- "_setInterrupted:withReason:"
- "audioLevelValues != ((void *)0)"
- "cfObject != ((void *)0)"
- "channelVolumes != ((void *)0)"
- "description=CameraCapture_AVF-587.81.10"
- "displayMode != ((void *)0)"
- "inNotificationPayload == ((void *)0)"
- "inNotifyingObject != ((void *)0)"
- "inputSources != ((void *)0)"
- "itemIdentifier != ((void *)0)"
- "message != ((void *)0)"
- "setHasPayingAttentionConfidence:"
- "setPayingAttentionConfidence:"
- "streams != ((void *)0)"
- "v24@0:8B16i20"
- "xpcObject != ((void *)0)"

```
