## CMCaptureCore

> `/System/Library/PrivateFrameworks/CMCaptureCore.framework/Versions/A/CMCaptureCore`

```diff

-587.81.10.0.0
-  __TEXT.__text: 0x1d7c
+587.101.4.0.0
+  __TEXT.__text: 0x1d88
   __TEXT.__auth_stubs: 0xc0
-  __TEXT.__cstring: 0xbd40
+  __TEXT.__cstring: 0xbe28
   __TEXT.__const: 0x1f
   __TEXT.__oslogstring: 0xa6
   __TEXT.__unwind_info: 0x78
   __TEXT.__objc_methname: 0x3c
   __TEXT.__objc_stubs: 0x40
   __DATA_CONST.__got: 0x2f0
-  __DATA_CONST.__const: 0x4a68
+  __DATA_CONST.__const: 0x4aa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x10
   __AUTH_CONST.__auth_got: 0x68
-  __AUTH_CONST.__cfstring: 0x113a0
+  __AUTH_CONST.__cfstring: 0x11480
   __DATA.__data: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/ImageIO.framework/Versions/A/ImageIO
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 583EC52E-5E91-36A6-A211-279E04C9831A
+  UUID: 00858A60-534D-3B7B-8C73-FEDD96472381
   Functions: 8
-  Symbols:   2501
-  CStrings:  4418
+  Symbols:   2508
+  CStrings:  4432
 
Symbols:
+ _kFigCaptureMetadata_CorrespondingMetadataIdentifiers
+ _kFigCaptureSampleBufferAttachmentKey_FaceIDReadiness
+ _kFigCaptureSampleBufferAttachmentKey_MotionToWake
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceIDReadinessConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceIDReadinessEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceTrackingConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureFaceTrackingEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureMotionToWakeConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureMotionToWakeEnabled
+ _kFigCaptureStreamMetadataOutputKey_SecureFaceIDReadiness
+ _kFigCaptureStreamMetadataOutputKey_SecureMotionToWake
+ _kFigCaptureStreamMetadataOutputKey_SecureTrackedFaces
+ _kFigCaptureStreamNotification_SuppressedGesture
+ _kFigCaptureStreamProperty_SensorVendorInfo
+ _kFigCaptureStreamSecureFaceDetectionConfigurationKey_OcclusionDetectionEnabled
+ _kFigCaptureStreamSecureFaceIDReadinessConfigurationKey_AttentionRequired
+ _kFigCaptureStreamSecureFaceIDReadinessConfigurationKey_PeriocularEnabled
+ _kFigCaptureStreamSecureFaceIDReadinessKey_CoachingStatus
+ _kFigCaptureStreamSecureFaceIDReadinessKey_Ready
+ _kFigCaptureStreamSecureFaceIDReadinessKey_UserEngagementStatus
+ _kFigCaptureStreamSecureFaceTrackingConfigurationKey_NetworkFailureThresholdMultiplier
+ _kFigCaptureStreamSecureFaceTrackingConfigurationKey_NumTrackedFaces
+ _kFigCaptureStreamSecureFaceTrackingConfigurationKey_TrackingFailureFieldOfViewModifier
+ _kFigCaptureStreamSecureMotionToWakeConfigurationKey_TargetFrameRate
+ _kFigCaptureStreamSecureMotionToWakeKey_Density
+ _kFigCaptureStreamSecureMotionToWakeKey_DetectedMotion
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_FaceOcclusionDetectionEnabled
+ _kFigMetadataIdentifier_QuickTimeMetadataFaceIDReadiness
+ _kFigMetadataIdentifier_QuickTimeMetadataMotionToWake
- _kFigCaptureStreamDetectedMotion
- _kFigCaptureStreamFaceTrackingConfigurationKey_NetworkFailureThresholdMultiplier
- _kFigCaptureStreamFaceTrackingConfigurationKey_NumTrackedFaces
- _kFigCaptureStreamFaceTrackingConfigurationKey_TrackingFailureFieldOfViewModifier
- _kFigCaptureStreamLMAConfigurationKey_EdgeDetectionEnabled
- _kFigCaptureStreamLMAConfigurationKey_FaceRequired
- _kFigCaptureStreamMetadataOutputConfigurationKey_LMAConfiguration
- _kFigCaptureStreamMetadataOutputConfigurationKey_LMAEnabled
- _kFigCaptureStreamMetadataOutputConfigurationKey_MotionEstimationConfiguration
- _kFigCaptureStreamMetadataOutputConfigurationKey_MotionEstimationEnabled
- _kFigCaptureStreamMetadataOutputConfigurationKey_StreamingFaceTrackingConfiguration
- _kFigCaptureStreamMetadataOutputConfigurationKey_StreamingFaceTrackingEnabled
- _kFigCaptureStreamMetadataOutputConfigurationKey_TargetFrameRate
- _kFigCaptureStreamMetadataOutputKey_FaceFound
- _kFigCaptureStreamMetadataOutputKey_MotionEstimation
- _kFigCaptureStreamMetadataOutputKey_StreamingTrackedFaces
- _kFigCaptureStreamMotionEstimate
- _kFigCaptureStreamStreamingFaceDetectionConfigurationKey_OcclusionDetectionEnabled
- _kFigCaptureStreamStreamingFaceKey_FaceIndex
- _kFigCaptureStreamStreamingFaceKey_FaceRotation
- _kFigCaptureStreamStreamingFaceKey_Found
- _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_FaceOcclusionDetectionEnabled
Functions:
~ _FigStartCaptureServers : 492 -> 488
~ _FigCaptureComputeImageGainFromMetadata -> _FigCaptureCopySerializableKeys : 284 -> 6496
~ _FigCaptureCopySerializableKeys -> _FigCaptureStreamFocusingMethodIsContrastBased : 6480 -> 36
~ _FigCaptureStreamFocusingMethodIsPhaseDetectionBased -> FigStartCaptureServers.cold.1 : 36 -> 76
~ FigStartCaptureServers.cold.3 -> _FigCaptureComputeImageGainFromMetadata : 76 -> 284
CStrings:
+ "AttentionRequired"
+ "CorrespondingMetadataIdentifiers"
+ "FaceIDReadiness"
+ "Metadata_SecureFaceTrackingConfiguration"
+ "Metadata_SecureFaceTrackingEnabled"
+ "MotionToWake"
+ "PeriocularEnabled"
+ "SecureFaceIDReadiness"
+ "SecureFaceIDReadinessConfiguration"
+ "SecureFaceIDReadinessEnabled"
+ "SecureMotionToWake"
+ "SecureMotionToWakeConfiguration"
+ "SecureMotionToWakeEnabled"
+ "SecureTrackedFaces"
+ "SensorVendorInfo"
+ "StreamSuppressedGesture"
+ "description=CameraCapture_CMCore-587.101.4"
+ "mdta/com.apple.quicktime.faceid-readiness"
+ "mdta/com.apple.quicktime.motion-to-wake"
- "EdgeDetectionEnabled"
- "FaceFound"
- "FaceRequired"
- "LMAConfiguration"
- "LMAEnabled"
- "Metadata_StreamingFaceTrackingConfiguration"
- "Metadata_StreamingFaceTrackingEnabled"
- "MotionEstimation"
- "MotionEstimationConfiguration"
- "MotionEstimationEnabled"
- "StreamingTrackedFaces"
- "description=CameraCapture_CMCore-587.81.10"

```
