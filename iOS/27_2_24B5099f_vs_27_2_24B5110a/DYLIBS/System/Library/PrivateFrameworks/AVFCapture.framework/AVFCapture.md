## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-764.40.7.0.0
-  __TEXT.__text: 0x141114
-  __TEXT.__objc_methlist: 0x114fc
-  __TEXT.__const: 0xf22
+764.42.8.0.0
+  __TEXT.__text: 0x1428d8
+  __TEXT.__objc_methlist: 0x116bc
+  __TEXT.__const: 0xf42
   __TEXT.__gcc_except_tab: 0x3170
-  __TEXT.__cstring: 0x2f649
-  __TEXT.__oslogstring: 0xb215
+  __TEXT.__cstring: 0x2f969
+  __TEXT.__oslogstring: 0xb3be
   __TEXT.__dlopen_cstrs: 0x274
   __TEXT.__ustring: 0x54
   __TEXT.__swift5_typeref: 0xef

   __TEXT.__swift5_reflstr: 0x24
   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x6888
+  __TEXT.__unwind_info: 0x6900
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9470
-  __DATA_CONST.__objc_classlist: 0x6c8
+  __DATA_CONST.__const: 0x9480
+  __DATA_CONST.__objc_classlist: 0x6d8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9288
+  __DATA_CONST.__objc_selrefs: 0x9358
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x5f0
-  __DATA_CONST.__objc_arraydata: 0x4f8
-  __DATA_CONST.__got: 0x2f90
-  __AUTH_CONST.__const: 0xe50
-  __AUTH_CONST.__cfstring: 0x16c80
-  __AUTH_CONST.__objc_const: 0x1cb48
-  __AUTH_CONST.__objc_intobj: 0xb70
+  __DATA_CONST.__objc_superrefs: 0x600
+  __DATA_CONST.__objc_arraydata: 0x520
+  __DATA_CONST.__got: 0x2fe8
+  __AUTH_CONST.__const: 0xe70
+  __AUTH_CONST.__cfstring: 0x16e20
+  __AUTH_CONST.__objc_const: 0x1ce88
+  __AUTH_CONST.__objc_intobj: 0xba0
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x3f0
+  __AUTH_CONST.__objc_arrayobj: 0x408
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1178
-  __AUTH.__objc_data: 0xd18
-  __DATA.__objc_ivar: 0x1ed0
+  __AUTH_CONST.__auth_got: 0x1188
+  __AUTH.__objc_data: 0xdb8
+  __DATA.__objc_ivar: 0x1efc
   __DATA.__data: 0xe50
   __DATA.__common: 0x1e0
   __DATA_DIRTY.__objc_data: 0x36d8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7857
-  Symbols:   14479
-  CStrings:  4230
+  Functions: 7891
+  Symbols:   14554
+  CStrings:  4251
 
Symbols:
+ +[AVCaptureDevice moduleSealedStateForDeviceType:position:]
+ +[AVCapturePersonalPhotographerSessionFinishCoordinator inactivityTimeoutForSystemPressureState:]
+ +[AVMetadataDeviceProximityDetectionObject deviceProximityDetectionWithDeviceDictionary:input:time:]
+ +[AVMetadataLightSourceEstimationObject lightSourceEstimationWithDictionary:input:time:]
+ -[AVCaptureDevice supportedMetadataIdentifiersForPerceptionThumbnailChannel]
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
+ -[AVCapturePersonalPhotographerSessionFinishCoordinator initWithInactivityTimeout:completionHandler:]
+ -[AVMetadataDeviceProximityDetectionObject confidence]
+ -[AVMetadataDeviceProximityDetectionObject copyWithZone:]
+ -[AVMetadataDeviceProximityDetectionObject description]
+ -[AVMetadataDeviceProximityDetectionObject deviceID]
+ -[AVMetadataDeviceProximityDetectionObject deviceType]
+ -[AVMetadataDeviceProximityDetectionObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:]
+ -[AVMetadataDeviceProximityDetectionObject initWithDeviceDictionary:sourceCaptureInput:time:]
+ -[AVMetadataDeviceProximityDetectionObject pose]
+ -[AVMetadataLightSourceEstimationObject copyWithZone:]
+ -[AVMetadataLightSourceEstimationObject dealloc]
+ -[AVMetadataLightSourceEstimationObject description]
+ -[AVMetadataLightSourceEstimationObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:]
+ -[AVMetadataLightSourceEstimationObject initWithLightSourceEstimationDictionary:sourceCaptureInput:time:]
+ -[AVMetadataLightSourceEstimationObject payload]
+ -[AVMetadataObject sentToPerceptionThumbnailChannel]
+ -[AVMetadataObjectInternal sentToPerceptionThumbnailChannel]
+ -[AVMetadataObjectInternal setSentToPerceptionThumbnailChannel:]
+ GCC_except_table1026
+ GCC_except_table1032
+ GCC_except_table1040
+ GCC_except_table1050
+ GCC_except_table171
+ GCC_except_table173
+ GCC_except_table175
+ GCC_except_table375
+ GCC_except_table803
+ GCC_except_table805
+ GCC_except_table807
+ GCC_except_table809
+ GCC_except_table836
+ GCC_except_table848
+ GCC_except_table850
+ GCC_except_table852
+ GCC_except_table858
+ GCC_except_table860
+ GCC_except_table903
+ GCC_except_table907
+ GCC_except_table974
+ GCC_except_table976
+ GCC_except_table978
+ GCC_except_table980
+ _AVMetadataObjectTypeDeviceProximityDetection
+ _AVMetadataObjectTypeLightSourceEstimation
+ _CFPreferencesCopyAppValue
+ _FigCaptureSourceRemoteGetPersonalizationStateForPosition
+ _OBJC_CLASS_$_AVMetadataDeviceProximityDetectionObject
+ _OBJC_CLASS_$_AVMetadataLightSourceEstimationObject
+ _OBJC_IVAR_$_AVCaptureMetadataOutputInternal.deviceProximityDetectionDeviceTypes
+ _OBJC_IVAR_$_AVCaptureMetadataOutputInternal.lightSourceEstimationAmbientLuminance
+ _OBJC_IVAR_$_AVCaptureMetadataOutputInternal.metadataObjectTypesForPerceptionThumbnailChannel
+ _OBJC_IVAR_$_AVCaptureMetadataOutputInternal.perceptionTestModeEnabled
+ _OBJC_IVAR_$_AVControlCenterModuleState._isOptedInForRingLight
+ _OBJC_IVAR_$_AVMetadataDeviceProximityDetectionObject._confidence
+ _OBJC_IVAR_$_AVMetadataDeviceProximityDetectionObject._deviceID
+ _OBJC_IVAR_$_AVMetadataDeviceProximityDetectionObject._deviceType
+ _OBJC_IVAR_$_AVMetadataDeviceProximityDetectionObject._pose
+ _OBJC_IVAR_$_AVMetadataLightSourceEstimationObject._payload
+ _OBJC_IVAR_$_AVMetadataObjectInternal._sentToPerceptionThumbnailChannel
+ _OBJC_METACLASS_$_AVMetadataDeviceProximityDetectionObject
+ _OBJC_METACLASS_$_AVMetadataLightSourceEstimationObject
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
+ ___101-[AVCapturePersonalPhotographerSessionFinishCoordinator initWithInactivityTimeout:completionHandler:]_block_invoke
+ ____personalizationStateForPosition_block_invoke
+ __personalizationStateForPosition.sPersonalizationStatesByPosition
+ __personalizationStateForPosition.sPersonalizationStatesByPositionOnceToken
+ _kFigCaptureSampleBufferAttachmentKey_DeviceProximityDetection
+ _kFigCaptureSampleBufferAttachmentKey_LightSourceEstimation
+ _kFigCaptureStreamDetectedObjectKey_SentToPerceptionThumbnailChannel
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_ConfidenceLevel
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_DeviceID
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_DeviceType
+ _kFigCaptureStreamSecureDetectedProximityDeviceKey_PoseMatrix
+ _kFigCaptureStreamSecureDetectedProximityDevicesKey_DevicesArray
- -[AVCapturePersonalPhotographerSessionFinishCoordinator initWithCompletionHandler:]
- GCC_except_table1025
- GCC_except_table1031
- GCC_except_table1039
- GCC_except_table1049
- GCC_except_table147
- GCC_except_table148
- GCC_except_table150
- GCC_except_table161
- GCC_except_table163
- GCC_except_table165
- GCC_except_table356
- GCC_except_table558
- GCC_except_table802
- GCC_except_table804
- GCC_except_table806
- GCC_except_table808
- GCC_except_table835
- GCC_except_table847
- GCC_except_table849
- GCC_except_table851
- GCC_except_table857
- GCC_except_table859
- GCC_except_table902
- GCC_except_table906
- GCC_except_table973
- GCC_except_table975
- GCC_except_table977
- GCC_except_table979
- ___83-[AVCapturePersonalPhotographerSessionFinishCoordinator initWithCompletionHandler:]_block_invoke
CStrings:
+ "%@: %p deviceID: %d, confidence: %f, deviceType: %d"
+ ", sentToPerceptionThumbnailChannel=%d"
+ "-[AVCapturePhotoOutput _handleNotification:payload:]"
+ "-[AVCapturePhotoOutput _handleStillImageCompleteNotification:withPayload:forRequest:]"
+ "<<<< AVCaptureDevice >>>> %s: Module personalization state: back=%ld front=%ld"
+ "<<<< AVCaptureMetadataOutput >>>> %s: Face ID Result <rawFrameId: %lu, metadataFrameId: %lu, refFrameId: %lu, frameType: %d, projectorMode: %d>"
+ "<<<< AVCapturePhotoOutput >>>> %s: *** (%p) %{public}@: Couldn't find a paired request for uniqueID %lld"
+ "<<<< AVCapturePhotoOutput >>>> %s: *** (%p) StillImageComplete error: (%d, %d) for uniqueID %lld"
+ "DeviceProximityDetection"
+ "HomeAccessory"
+ "J490"
+ "J491"
+ "LastShownBuild:AVCaptureDevice.m:4904"
+ "LastShownBuild:AVCaptureDevice.m:4908"
+ "LastShownBuild:AVCapturePhotoOutput.m:3226"
+ "LastShownBuild:AVCapturePhotoOutput.m:9732"
+ "LastShownBuild:AVControlCenterModules.m:4569"
+ "LastShownBuild:AVControlCenterModules.m:4573"
+ "LastShownDate:AVCaptureDevice.m:4904"
+ "LastShownDate:AVCaptureDevice.m:4908"
+ "LastShownDate:AVCapturePhotoOutput.m:3226"
+ "LastShownDate:AVCapturePhotoOutput.m:9732"
+ "LastShownDate:AVControlCenterModules.m:4569"
+ "LastShownDate:AVControlCenterModules.m:4573"
+ "LightSourceEstimation"
+ "Unsupported - check for AVMetadataDeviceProximityDetectionObject in -availableMetadataObjectTypes"
+ "Unsupported - check for AVMetadataLightSourceEstimationObject in -availableMetadataObjectTypes"
+ "Unsupported type found (%@) - use -supportedMetadataObjectTypesForPerceptionThumbnailChannel"
+ "_personalizationStateForPosition_block_invoke"
+ "avcapturedevice_moduleSealedStateOverrides"
+ "avcmdo_faceIDCollectionForSampleBuffer"
+ "com.apple.TVMirror"
+ "description=CameraCapture_AVF-764.42.8"
+ "mdta/com.apple.quicktime.device-proximity-detection"
+ "mdta/com.apple.quicktime.light-source-estimation"
- "DeviceSupportsTouchSensitiveCameraControl"
- "LastShownBuild:AVCaptureDevice.m:4820"
- "LastShownBuild:AVCaptureDevice.m:4824"
- "LastShownBuild:AVCapturePhotoOutput.m:3225"
- "LastShownBuild:AVCapturePhotoOutput.m:9720"
- "LastShownBuild:AVControlCenterModules.m:4551"
- "LastShownBuild:AVControlCenterModules.m:4555"
- "LastShownDate:AVCaptureDevice.m:4820"
- "LastShownDate:AVCaptureDevice.m:4824"
- "LastShownDate:AVCapturePhotoOutput.m:3225"
- "LastShownDate:AVCapturePhotoOutput.m:9720"
- "LastShownDate:AVControlCenterModules.m:4551"
- "LastShownDate:AVControlCenterModules.m:4555"
- "description=CameraCapture_AVF-764.40.7"
```
