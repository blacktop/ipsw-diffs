## H16ISPServices

> `/System/Library/PrivateFrameworks/H16ISPServices.framework/H16ISPServices`

```diff

-3.504.14.0.0
-  __TEXT.__text: 0xe98c
-  __TEXT.__auth_stubs: 0x450
+3.509.0.0.0
+  __TEXT.__text: 0x10b48
+  __TEXT.__auth_stubs: 0x510
   __TEXT.__gcc_except_tab: 0x5b8
-  __TEXT.__cstring: 0x60dc
-  __TEXT.__const: 0x50
-  __TEXT.__unwind_info: 0x218
-  __DATA_CONST.__got: 0x160
-  __AUTH_CONST.__auth_got: 0x230
+  __TEXT.__cstring: 0x6269
+  __TEXT.__const: 0x98
+  __TEXT.__oslogstring: 0x5bd
+  __TEXT.__unwind_info: 0x268
+  __DATA_CONST.__got: 0x1d0
+  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__cfstring: 0x120
+  __DATA.__data: 0x8
+  __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
-  - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore
+  - /System/Library/PrivateFrameworks/CMCaptureDevice.framework/CMCaptureDevice
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libIOAccessoryManager.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 85
-  Symbols:   199
-  CStrings:  1417
+  Functions: 129
+  Symbols:   270
+  CStrings:  1459
 
Symbols:
+ _CFDataGetLength
+ _CFDictionaryContainsKey
+ _CGPointMakeWithDictionaryRepresentation
+ _CGPointZero
+ _CGRectZero
+ _CMTimeGetSeconds
+ _CMTimeMake
+ _FigCFDictionaryGetCGRectIfPresent
+ _FigCFEqual
+ _FigGetUpTime
+ _FigHostTimeToNanoseconds
+ __Z20FigMotionGetGravityZPK14__CFDictionaryPf
+ __Z30FigMotionComputePrincipalPointPK14__CFDictionaryffdiiiihP7CGPoint
+ __Z37FigMotionAdjustPointForSphereMovementPK14__CFDictionaryffdP7CGPoint
+ __Z37FigMotionComputeAverageSpherePositionPK14__CFDictionarydP11FigPosition
+ __Z38FigMotionCalculateAdjustedLensPositionPK14__CFDictionaryfP26CameraCharacterizationDatafPf
+ __Z39FigMotionCalculateAdjustedFocusPositionffPi
+ __Z41FigMotionComputeLensPositionScalingFactorPK14__CFDictionaryiiiiPf
+ ___chkstk_darwin
+ __os_log_default
+ __os_log_error_impl
+ _kFigCapturePortType_FrontFacingSuperWideCamera
+ _kFigCaptureStreamMetadata_CurrentFocusPosition
+ _kFigCaptureStreamMetadata_FrameRollingShutterSkew
+ _kFigCaptureStreamMetadata_ISPHallData
+ _kFigCaptureStreamMetadata_ISPMotionData
+ _kFigCaptureStreamMetadata_OpticalCenter
+ _kFigCaptureStreamMetadata_PortType
+ _kFigCaptureStreamMetadata_RawCropRect
+ _kFigCaptureStreamMetadata_SensorRawValidBufferRect
+ _kFigCaptureStreamMetadata_TotalSensorCropRect
+ _kFigCaptureStreamMetadata_ValidBufferRect
+ _os_log_create
+ _os_log_type_enabled
CStrings:
+ "%s - Could not find Hall samples in given time range [%f, %f]. Use the closest Hall sample in actual time range [%f, %f].\n"
+ "%s - Could not find any CropRect in the metadata dictionary!\n"
+ "%s - Empty ISP motion data\n"
+ "%s - ExposureTime missing from metadata\n"
+ "%s - Extracting only the first %d ISP Hall samples\n"
+ "%s - FrameRollingShutterSkew missing from metadata\n"
+ "%s - ISP Hall data size did not match expected number of bytes.\n"
+ "%s - ISP Hall data version is not supported.\n"
+ "%s - ISP motion data not available\n"
+ "%s - ISP motion data size did not match expected number of bytes.\n"
+ "%s - ISP motion data version is not supported.\n"
+ "%s - Invalid ISP Hall data\n"
+ "%s - Invalid ISP motion data\n"
+ "%s - Invalid lens coefficients!\n"
+ "%s - Invalid parameter!\n"
+ "%s - LensPositionScalingFactor disagrees by %.2f%% in horizontal (%f) and vertical (%f)\n"
+ "%s - NULL metadata dictionary\n"
+ "%s - No CurrentFocusPosition!\n"
+ "%s - No metadata dictionary!\n"
+ "%s - RawCropRect found in metadata dictionary but malformed!\n"
+ "%s - Sensor crop rect height is not strictly positive!\n"
+ "%s - Sensor crop rect width is not strictly positive!\n"
+ "%s - SensorRawValidBufferRect found in metadata dictionary but malformed!\n"
+ "%s - TotalSensorCropRect found in metadata dictionary but malformed!\n"
+ "%s - Unsupported Hall data version %d\n"
+ "%s - binningFactorHorizontal is not strictly positive!\n"
+ "%s - binningFactorVertical is not strictly positive!\n"
+ "%s - metadataDict is null!\n"
+ "%s - metadataDict or adjustedPrincipalPointOut is null!\n"
+ "FigMotionAdjustPointForSphereMovement"
+ "FigMotionCalculateAdjustedLensPosition"
+ "FigMotionComputeAverageSpherePosition"
+ "FigMotionComputeAverageSpherePositionForTimes"
+ "FigMotionComputeLensPositionScalingFactor"
+ "FigMotionComputePrincipalPoint"
+ "FigMotionGetGravityZ"
+ "FigMotionGetISPHallData"
+ "FigMotionGetSensorValidCropRect"
+ "FigMotionISPHallDataFromCFData"
+ "FigMotionISPMotionDataFromCFData"
+ "com.apple.isp"
+ "general"

```
