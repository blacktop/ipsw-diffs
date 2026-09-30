## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-758.0.0.0.1
-  __TEXT.__text: 0x559314
-  __TEXT.__objc_methlist: 0x28994
-  __TEXT.__const: 0x143020
-  __TEXT.__cstring: 0x98852
-  __TEXT.__oslogstring: 0xc8807
-  __TEXT.__gcc_except_tab: 0x20b0
+761.0.0.0.3
+  __TEXT.__text: 0x55daf0
+  __TEXT.__objc_methlist: 0x28acc
+  __TEXT.__const: 0x143018
+  __TEXT.__cstring: 0x98ea8
+  __TEXT.__oslogstring: 0xc91b8
+  __TEXT.__gcc_except_tab: 0x20dc
   __TEXT.__dlopen_cstrs: 0x290
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0xa4e8
+  __TEXT.__unwind_info: 0xa528
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5f68
+  __DATA_CONST.__const: 0x5f88
   __DATA_CONST.__objc_classlist: 0x1338
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11cf0
+  __DATA_CONST.__objc_selrefs: 0x11d98
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x11e0
   __DATA_CONST.__objc_arraydata: 0x1620
-  __DATA_CONST.__got: 0x61e8
-  __AUTH_CONST.__const: 0x5678
-  __AUTH_CONST.__cfstring: 0x41ee0
-  __AUTH_CONST.__objc_const: 0x72560
+  __DATA_CONST.__got: 0x6208
+  __AUTH_CONST.__const: 0x56b8
+  __AUTH_CONST.__cfstring: 0x42120
+  __AUTH_CONST.__objc_const: 0x72810
   __AUTH_CONST.__objc_intobj: 0x3c48
   __AUTH_CONST.__objc_arrayobj: 0x11e8
   __AUTH_CONST.__objc_floatobj: 0x170
   __AUTH_CONST.__objc_doubleobj: 0x200
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x2178
+  __AUTH_CONST.__auth_got: 0x2180
   __AUTH.__objc_data: 0x2620
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0x8918
+  __DATA.__objc_ivar: 0x8960
   __DATA.__data: 0x282c
-  __DATA.__common: 0x1990
+  __DATA.__common: 0x19a0
   __DATA.__bss: 0x1258
   __DATA_DIRTY.__objc_data: 0x9a10
   __DATA_DIRTY.__data: 0xfb8

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 26387
-  Symbols:   47498
-  CStrings:  23659
+  Functions: 26433
+  Symbols:   47554
+  CStrings:  23709
 
Symbols:
+ +[FigCaptureCustomFocusConfiguration focusConfigurationWithLensPosition:clampToHyperfocal:requestID:]
+ +[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByDeviceType:position:requestID:featuresEnabled:]
+ +[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByPortType:requestID:featuresEnabled:]
+ -[BWFigCaptureDevice _invalidateSyncStreamGroupsAndControlledStreams:preserveTorchState:unsynchronizedStreamsStopSupported:]
+ -[BWFigCaptureDevice invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:unsynchronizedStreamsStopSupported:]
+ -[BWFigCaptureDeviceVendor _invalidate:keepFigCaptureDeviceAlive:preserveTorchState:unsynchronizedStreamsStopSupported:]
+ -[BWFigCaptureSession stillImageCoordinator:didSelectVitalityMode:forSettings:]
+ -[BWFigCaptureStream didStop]
+ -[BWFigCaptureStream willStop]
+ -[BWFigVideoCaptureDevice lastKnownSubjectGazingState]
+ -[BWFigVideoCaptureDevice portTypesWithSoftISPClientBracketEnabled]
+ -[BWFigVideoCaptureDevice restoreLastKnownSubjectGazingState:]
+ -[BWFigVideoCaptureDevice setPortTypesWithSoftISPClientBracketEnabled:]
+ -[BWFigVideoCaptureDevice setShutterSoundRelaxationTrueVideoTransitionActive:]
+ -[BWFigVideoCaptureDevice shutterSoundRelaxationTrueVideoTransitionActive]
+ -[BWIrisMovieGenerator disableVitalityForSettingsID:]
+ -[BWIrisMovieInfo setVitalityDisabled:]
+ -[BWIrisMovieInfo vitalityDisabled]
+ -[BWPhotoDecompressor preserveBorderRows]
+ -[BWPhotoDecompressor setPreserveBorderRows:]
+ -[BWPhotoEncoderController _adjustAspectRatio:settings:applyOutputAspectRatioOverride:]
+ -[BWPhotoEncoderController _cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:applyOutputAspectRatioOverride:]
+ -[BWQuickTimeMovieFileSinkNode disableVitalityForSettingsID:]
+ -[BWStillImageCoordinatorNode _didSelectVitalityMode:forSettings:]
+ -[BWStillImageCoordinatorNode node:didSelectVitalityMode:forSettings:]
+ -[BWTemporalFilterNode _prepareVTTemporalFilterSession]
+ -[BWTemporalFilterNode didReachEndOfDataForConfigurationID:input:]
+ -[BWTemporalFilterNode hasNonLiveConfigurationChanges]
+ -[BWUBCaptureParameters digitalFlashBacklitRecommendFlashNormalizedSNRHysteresisLag]
+ -[BWUBCaptureParameters digitalFlashBacklitRecommendFlashNormalizedSNRThreshold]
+ -[BWUBCaptureParameters digitalFlashRecommendFlashNormalizedSNRHysteresisLag]
+ -[BWUBCaptureParameters digitalFlashRecommendFlashNormalizedSNRThreshold]
+ -[FigCaptureAncillaryDataHIDTransmitter openDeviceWithUsagePage:vendor:product:error:]
+ -[FigCaptureAncillaryDataHIDTransmitter setTargetProduct:]
+ -[FigCaptureAncillaryDataHIDTransmitter setTargetVendor:]
+ -[FigCaptureAncillaryDataHIDTransmitter targetProduct]
+ -[FigCaptureAncillaryDataHIDTransmitter targetVendor]
+ -[FigCaptureCustomFocusConfiguration _initWithLensPosition:clampToHyperfocal:requestID:]
+ -[FigCaptureCustomWhiteBalanceConfiguration _initWithGainsByPortType:requestID:featuresEnabled:]
+ -[FigCaptureSessionConfiguration reasonForNotEqualingConfigurationIgnoringConfigurationID:]
+ -[FigCaptureSessionStateManager sessionClearNonSystemInterruption]
+ -[FigCaptureStillImageSettings outputAspectRatioOverride]
+ -[FigCaptureStillImageSettings setOutputAspectRatioOverride:]
+ -[TrackedSubject _updateGazeStatesUsingGazeProbabilitiesData:gazeScoreOut:]
+ -[TrackedSubject initWithGroupID:significanceDetectionThreshold:smartFramingSceneMonitorMode:isPet:]
+ GCC_except_table190
+ GCC_except_table299
+ GCC_except_table354
+ GCC_except_table702
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._consecutiveNotGazingFrameCount
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._digitalFlashBacklitRecommendFlashSceneByPortType
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._digitalFlashRecommendFlashSceneByPortType
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._portTypesWithSoftISPClientBracketEnabled
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._shutterSoundRelaxationTrueVideoTransitionActive
+ OBJC_IVAR_$_BWFigVideoCaptureStream._temporalNoiseReductionRawEnabled
+ OBJC_IVAR_$_BWIrisMovieInfo._vitalityDisabled
+ OBJC_IVAR_$_BWPhotoDecompressor._preserveBorderRows
+ OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._pendingVitalityDisabledSettingsIDs
+ OBJC_IVAR_$_BWSmartCropNode._rtscProcessorInitQueue
+ OBJC_IVAR_$_BWTemporalFilterNode._liveSessionHeight
+ OBJC_IVAR_$_BWTemporalFilterNode._liveSessionInputPixelFormat
+ OBJC_IVAR_$_BWTemporalFilterNode._liveSessionOutputPixelFormat
+ OBJC_IVAR_$_BWTemporalFilterNode._liveSessionWidth
+ OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashBacklitRecommendFlashNormalizedSNRHysteresisLag
+ OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashBacklitRecommendFlashNormalizedSNRThreshold
+ OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashRecommendFlashNormalizedSNRHysteresisLag
+ OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashRecommendFlashNormalizedSNRThreshold
+ OBJC_IVAR_$_FigCaptureAncillaryDataHIDTransmitter._targetProduct
+ OBJC_IVAR_$_FigCaptureAncillaryDataHIDTransmitter._targetVendor
+ OBJC_IVAR_$_FigCaptureCustomFocusConfiguration._clampToHyperfocalLogicalLensPositionEnabled
+ OBJC_IVAR_$_FigCaptureCustomWhiteBalanceConfiguration._featuresEnabled
+ OBJC_IVAR_$_FigCaptureStillImageSettings._outputAspectRatioOverride
+ _BWStillImageAppendCaptureFrameFlagsToSampleBuffer
+ _CGRectInfinite
+ _CMILSCOISAdaptation_convertV3LSCTableToV2LSCTableWithAperture
+ ___26-[BWSmartCropNode dealloc]_block_invoke
+ ___47-[BWSmartCropNode renderSampleBuffer:forInput:]_block_invoke
+ ___61-[BWSmartCropNode prepareForCurrentConfigurationToBecomeLive]_block_invoke
+ ___66-[BWTemporalFilterNode didReachEndOfDataForConfigurationID:input:]_block_invoke
+ ___66-[FigCaptureSessionStateManager sessionClearNonSystemInterruption]_block_invoke
+ ___70-[BWStillImageCoordinatorNode node:didSelectVitalityMode:forSettings:]_block_invoke
+ ___captureSession_teardownGraph_block_invoke
+ __captureSession_teardownGraph_block_invoke
+ _kCMPhotoCompressionOption_ExtractAndStoreBorderRowsSeparately
+ _kCMPhotoDecompressionOption_ApplyBorderRows
+ _kFigCaptureSourceWhiteBalanceOperationKey_FeaturesEnabled
+ _kFigQuickTimeMetadataKey_LivePhotoVitalityDisabled
+ _kFigVirtualCaptureCardProperty_InitialCapacityOverhead
+ _objc_msgSend$_adjustAspectRatio:settings:applyOutputAspectRatioOverride:
+ _objc_msgSend$_cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:applyOutputAspectRatioOverride:
+ _objc_msgSend$_initWithGainsByPortType:requestID:featuresEnabled:
+ _objc_msgSend$_initWithLensPosition:clampToHyperfocal:requestID:
+ _objc_msgSend$_updateGazeStatesUsingGazeProbabilitiesData:gazeScoreOut:
+ _objc_msgSend$beginIrisMovieCaptureTime
+ _objc_msgSend$didStop
+ _objc_msgSend$digitalFlashBacklitRecommendFlashNormalizedSNRHysteresisLag
+ _objc_msgSend$digitalFlashBacklitRecommendFlashNormalizedSNRThreshold
+ _objc_msgSend$digitalFlashRecommendFlashNormalizedSNRHysteresisLag
+ _objc_msgSend$digitalFlashRecommendFlashNormalizedSNRThreshold
+ _objc_msgSend$disableVitalityForSettingsID:
+ _objc_msgSend$hyperfocalLogicalFocusLensPosition
+ _objc_msgSend$initWithGroupID:significanceDetectionThreshold:smartFramingSceneMonitorMode:isPet:
+ _objc_msgSend$invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:unsynchronizedStreamsStopSupported:
+ _objc_msgSend$lastKnownSubjectGazingState
+ _objc_msgSend$openDeviceWithUsagePage:vendor:product:error:
+ _objc_msgSend$outputAspectRatioOverride
+ _objc_msgSend$reasonForNotEqualingConfigurationIgnoringConfigurationID:
+ _objc_msgSend$restoreLastKnownSubjectGazingState:
+ _objc_msgSend$sessionClearNonSystemInterruption
+ _objc_msgSend$setOutputAspectRatioOverride:
+ _objc_msgSend$setShutterSoundRelaxationTrueVideoTransitionActive:
+ _objc_msgSend$setTargetVendor:
+ _objc_msgSend$setVitalityDisabled:
+ _objc_msgSend$stillImageCoordinator:didSelectVitalityMode:forSettings:
+ _objc_msgSend$subjectRelightingEnabled
+ _objc_msgSend$vitalityDisabled
+ _objc_msgSend$willStop
- +[FigCaptureCustomFocusConfiguration focusConfigurationWithLensPosition:requestID:]
- +[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByDeviceType:position:requestID:]
- +[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByPortType:requestID:]
- -[BWFigCaptureDevice _invalidateSyncStreamGroupsAndControlledStreams:preserveTorchState:]
- -[BWFigCaptureDevice invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:]
- -[BWFigCaptureDeviceVendor _invalidate:keepFigCaptureDeviceAlive:preserveTorchState:]
- -[BWFigCaptureStream synchronizedStreamsGroupDidStop]
- -[BWFigCaptureStream synchronizedStreamsGroupWillStop]
- -[BWPhotoEncoderController _adjustAspectRatio:settings:]
- -[BWPhotoEncoderController _cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:]
- -[BWTemporalFilterNode didReachEndOfDataForInput:]
- -[FigCaptureAncillaryDataHIDTransmitter openDeviceWithUsagePage:usage:error:]
- -[FigCaptureAncillaryDataHIDTransmitter setTargetUsage:]
- -[FigCaptureAncillaryDataHIDTransmitter targetUsage]
- -[FigCaptureCustomFocusConfiguration _initWithLensPosition:requestID:]
- -[FigCaptureCustomWhiteBalanceConfiguration _initWithGainsByPortType:requestID:]
- -[FigCaptureSessionStateManager clearNonSystemInterruption]
- -[TrackedSubject _updateGazeStatesUsingGazeProbabilitiesData:gazeScoreOut:gazeScoreFilteredOut:]
- -[TrackedSubject initWithGroupID:significanceDetectionThreshold:gazeFilteringStrength:smartFramingSceneMonitorMode:isPet:]
- -[TrackedSubject isSignificantFiltered]
- GCC_except_table109
- GCC_except_table189
- GCC_except_table216
- GCC_except_table296
- GCC_except_table350
- GCC_except_table351
- GCC_except_table700
- OBJC_IVAR_$_FigCaptureAncillaryDataHIDTransmitter._targetUsage
- OBJC_IVAR_$_SubjectSelection._gazeFilteringStrength
- OBJC_IVAR_$_TrackedSubject._gazeFilteringStrength
- OBJC_IVAR_$_TrackedSubject._gazeScoreFiltered
- OBJC_IVAR_$_TrackedSubject._isSignificantFiltered
- _OUTLINED_FUNCTION_706
- _OUTLINED_FUNCTION_707
- _OUTLINED_FUNCTION_708
- _OUTLINED_FUNCTION_709
- _OUTLINED_FUNCTION_710
- _OUTLINED_FUNCTION_711
- _OUTLINED_FUNCTION_712
- _OUTLINED_FUNCTION_713
- _OUTLINED_FUNCTION_714
- _OUTLINED_FUNCTION_715
- _OUTLINED_FUNCTION_716
- _OUTLINED_FUNCTION_717
- _OUTLINED_FUNCTION_718
- _OUTLINED_FUNCTION_719
- _OUTLINED_FUNCTION_720
- ___50-[BWTemporalFilterNode didReachEndOfDataForInput:]_block_invoke
- ___59-[FigCaptureSessionStateManager clearNonSystemInterruption]_block_invoke
- _objc_msgSend$_adjustAspectRatio:settings:
- _objc_msgSend$_cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:
- _objc_msgSend$_initWithGainsByPortType:requestID:
- _objc_msgSend$_initWithLensPosition:requestID:
- _objc_msgSend$_updateGazeStatesUsingGazeProbabilitiesData:gazeScoreOut:gazeScoreFilteredOut:
- _objc_msgSend$clearNonSystemInterruption
- _objc_msgSend$initWithGroupID:significanceDetectionThreshold:gazeFilteringStrength:smartFramingSceneMonitorMode:isPet:
- _objc_msgSend$invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:
- _objc_msgSend$openDeviceWithUsagePage:usage:error:
- _objc_msgSend$setTargetUsage:
- _objc_msgSend$synchronizedStreamsGroupDidStop
- _objc_msgSend$synchronizedStreamsGroupWillStop
CStrings:
+ " AROverride:%.3f"
+ "%@ %p: captureID:%lld '%.4s'('%.4s')%@ %dx%d R:%d%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
+ "%@ %p: requestID:%d appliedFrameStatistics:%@ featuresEnabled:%@"
+ "(*modified by aspect-ratio override)"
+ "+[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByDeviceType:position:requestID:featuresEnabled:]"
+ "-[BWFigCaptureDevice _invalidateSyncStreamGroupsAndControlledStreams:preserveTorchState:unsynchronizedStreamsStopSupported:]"
+ "-[BWFigCaptureDevice invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:unsynchronizedStreamsStopSupported:]"
+ "-[BWFigCaptureDeviceVendor _invalidate:keepFigCaptureDeviceAlive:preserveTorchState:unsynchronizedStreamsStopSupported:]"
+ "-[BWFigCaptureSession stillImageCoordinator:didSelectVitalityMode:forSettings:]"
+ "-[BWFigCaptureStream didStop]"
+ "-[BWIrisMovieGenerator disableVitalityForSettingsID:]"
+ "-[BWPhotoEncoderController _cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:applyOutputAspectRatioOverride:]"
+ "-[BWQuickTimeMovieFileSinkNode dealloc]"
+ "-[BWQuickTimeMovieFileSinkNode disableVitalityForSettingsID:]"
+ "-[BWTemporalFilterNode _prepareVTTemporalFilterSession]"
+ "-[BWTemporalFilterNode didReachEndOfDataForConfigurationID:input:]"
+ "-[BWTemporalFilterNode didReachEndOfDataForConfigurationID:input:]_block_invoke"
+ "-[FigCaptureAncillaryDataHIDTransmitter openDeviceWithUsagePage:vendor:product:error:]"
+ "-[FigCaptureCustomExposureConfiguration applyFrameStatistics:forPortTypes:primaryPortType:limitsByPortType:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/CMCaptureLocal/CMCaptureLocalSessionController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/CameraViewfinder/FigCaptureSessionObserver.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureMetadataUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSessionPipelines.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSessionStateManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSourceBackingsProvider.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/CMCaptureUserNotification.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureCommon.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unknown flip %i"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unsupported rotation of %d degrees"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: rotationDegrees (%d) is invalid, must be 0/90/180/270. Returning kFigExifOrientation_0RowTop0ColLeft (%d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/FigCapturePixelFormatUtilities.m %s: Unexpected plist value for a pixel format type: %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Cannot look up key.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Not adding key.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Returning 0."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Key (%s) has already been registered. Not adding key.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: keyspace not found, has no name"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Common/FigRemoteQueue/FigRemoteQueue.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWDeviceMotionActivityDetector.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigCaptureDeviceVendor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureDevice.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureStream.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFrameStatistics.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWGraph.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWInvalidFramesChecker.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing noise reduction and sharpening parameters"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing portType"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing sensorIDDictionary"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing MBNR parameters for type '%d' and gain '%.1f'"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing noise reduction and sharpening parameters for type '%d' and gain '%.1f'"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWPixelBufferPool.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing PortType"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing cameraInfo"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDDictionary"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDString"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil input for %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil portType for %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@ took %lld ms"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@..."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Couldn't find Deep Fusion HDR EV0 count for EIT '%f': %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Missing portType"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then Long-Without-Sphere threshold: %@."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then SIFR-Main threshold: %@."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Motion and focus scores RFS is specified, but weights are missing: %@."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. SIFR-Main threshold should be smaller then Long-Without-Sphere threshold: %@."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWVideoFormat.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWAudioSourceNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWCameraInfoMetadataNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDeferredCaptureController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDepthConverterNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWFileCoordinatorNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWFrameRateGovernorNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWImageQueueSinkNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWIrisStagingNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWLearnSmartStyleRenderer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWMultiStreamCameraSourceNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWOverCaptureSmartStyleApplyNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPiecemealEncodingNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPreviewStitcherNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPreviewTimeMachineSinkNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSensitiveContentAnalyzerSinkNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSmartStyleReversibilityRenderer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSmartStyleTargetRenderer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageCoordinatorNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageScalerNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSynchronizerNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVISNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVideoPIPOverlayNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWAggdDataReporter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWCoreAnalyticsReporter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFencedAnimationQueue.m %s: Fenced animation queue wait timeout occurred - not queuing animation"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFigVideoCaptureSynchronizedStreamsGroup.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWPixelBufferTransferRenderer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWStillImageMetadataUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/Autofocus/FigSampleBufferProcessor_Autofocus.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: %d motion-related log messages filtered out (max of 1/s displayed from FigCoreMotionDelegate)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration fused vector is computed incorrectly"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration vector is computed incorrectly"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Allocation error when retrieving motion data"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Closest motion sample for timestamp %f has timestamp %f, difference %f\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not find motion sample to get Quaternion.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not lock the ringMutex\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Frame timestamp is %f, Sample timestamps in the ring buffer are from %f to %f\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Gravity is computed incorrectly"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Potential missing three motion samples: new timestamp %f, latest timestamp %f\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: no data semaphore was available to wait on"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: %d motion-related log messages filtered out (max of 1/s displayed from FigMotionProcessingUtilities)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall sample for the given timestamp on hallPositionIndex %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall samples in given time range [%f, %f]. Use the closest Hall sample in actual time range [%f, %f]."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find a motion sample within %fms of the current frame. Frame timestamp is %f, sample timestamps in the ring buffer are from %f to %f, latestTimeDifference %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find motion sample to get Quaternion."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find the closest motion sample index in the ring buffer for the frame timestamp (%f)."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP Hall samples"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP motion samples"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming default value of 1.0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming value of %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Frame timestamp is from %f to %f, Sample timestamps in the ring buffer are from %f to %f, get %d motion samples"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Motion Hardware Unavailable - prototype hardware detected"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: No valid baseZoomFactor found, will proceed with a value of 1.0f."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Quaternion pointer is null!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Time interval %f is not positive"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Too many motion samples for the array"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Unsupported Hall data version %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Using default focus characterization entry because an entry corresponding to the original requested values was not found."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after Hall sample timestamp difference is close to 0.0f!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after motion sample timestamp difference is close to 0.0f!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: interpolateQuaternionsByAngle: delta quaternion w %f is larger than 1"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: invalid micronsPerPixel value %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed computing scaling factor"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed extracting metadata"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed getting ISPFrameCorrectionShiftValues. Using value of 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Unsupported sag removal method"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: sagPosition memory allocation failed"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Could not parse motion data from ISP due to error: %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Failed to allocate and initialize VISRotationCorrectionEstimator"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Height is missing from visInputPixelBufferAttributes"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData from metadataDict"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PinholeCameraFocalLength in metadataDict"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PortType from metadataDict"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSize for portType: %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSizeInMicrons for port %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing portType in metadataDict"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: No motion samples for this frame. Skipping processing"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Overscan is 0 or less. l:%f r:%f t:%f b:%f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Timestamp %f is earlier than previous sample %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Width is missing from visInputPixelBufferAttributes"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: focalLength is null"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Y9bqR9/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: pole must be between 0 and 1"
+ "00:18:24"
+ "1905686"
+ "<%@: %p> lowLightEIT=%f, sifrMainEIT=%f, sifrGain=%f, lowLightHDRWithoutSIFR=%f, longWithoutSphere=%f, deepFusion=%f, rsmMainEIT=%f, rsmSIFRGain=%f, toneCurveBehavior=%d, preserveBlackLevel=%d, afWindows=%p, refMethod=%d, usePreviousSIFR=%d, motionAndFocusScoreWeights=%@, maxNumberOfFramesForAdaptiveBracketing=%d, dFlashAvailableEIT=%f, dFlashRecommendedEIT=%f, dFlashStationaryRecommendedEIT=%f, dFlashAvailableSNR=%f, dFlashAvailableSNRLag=%f, dFlashRecommendedSNR=%f, dFlashRecommendedSNRLag=%f, dFlashStationaryRecommendedSNR=%f, dFlashStationaryRecommendedSNRLag=%f, dFlashBacklitRecommendFlashSNR=%f, dFlashBacklitRecommendFlashSNRLag=%f, dFlashRecommendFlashSNR=%f, dFlashRecommendFlashSNRLag=%f, dFlashRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashAERelativeDiff=%f%@"
+ "<<< FigCaptureCustomExposureConfiguration >>> %s: deferring lock to unknown ISO limits for %@ (primary %@); available limits: %@"
+ "<<< FigCaptureCustomExposureConfiguration >>> %s: deferring lock to unknown current ISO"
+ "<<< FigCaptureCustomExposureConfiguration >>> %s: deferring lock to unknown current duration"
+ "<<< FigCaptureCustomFocusConfiguration >>> %s: [%@] Clamping focus position '%d' to '%d' using hyper focal focus postion '%d'"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Tagging asset bundle frame not used by this capture to be discarded (captureFlags:%{public}@): %{private}@"
+ "<<<< BWGraph >>>> %s: <%p> All %lu source nodes had deferred start enabled. Falling back to non-deferred start for <%p, %@, %{public}@> and continuing."
+ "<<<< BWGraph >>>> %s: Parent of shared pool output should have a prepared pool: attachedMediaKey=%{public}@ sharedPoolOutput=%{public}@ parentOutput=%{public}@ parentAttachedMediaKey=%{public}@"
+ "<<<< BWIrisMovieGenerator >>>> %s: %p: Disabled vitality for %@"
+ "<<<< BWIrisMovieGenerator >>>> %s: %p: Disabling vitality for captureID:%lld"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Applied pending vitality disable for %@"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Disabled vitality for firstIrisMovieInfo %@"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Disabled vitality for pendingIrisRefMovieRequests %@"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Disabling vitality for captureID:%lld"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: deallocating with %lu unhandled pending vitality disabled settingsIDs: %@"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: settingsID:%lld not found in sink node yet, adding to pending vitality disabled list"
+ "<<<< BWSmartFramingSceneMonitor >>>> %s: TrackedSubject scores: groupID (%@), gazeScore (%f), significanceScore (%f), isSignificant (%d)"
+ "<<<< BWStillImageMetadataUtilities >>>> %s: Missing noise parameters: ReadNoise_1x=%@, ReadNoise_8x=%@, ConversionGain=%@, AGC=%@"
+ "<<<< BWStillImageMetadataUtilities >>>> %s: SushiRAW LSC GainMap failed to convert V3 LSC gain grid to V2 (err:%{public}d, AD:%{public}.1f microns)"
+ "<<<< BWTemporalFilterNode >>>> %s: %@ %@ is EOD (configurationID: %@)"
+ "<<<< BWTemporalFilterNode >>>> %s: %{private}@ ConfigurationID %lld is now live for video input and output"
+ "<<<< BWTemporalFilterNode >>>> %s: MCTF session is nil after init attempt"
+ "<<<< FigCaptureMetadataUtilities >>>> %s: textOrientationExtraRotationDegrees: %d must be a multiple of 90"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ Disabling vitality in movie file sink nodes for captureID:%lld"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ New configuration (%lld) differs from live configuration (%lld) due to: %{public}@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Error(%d) starting session: %{public}@"
+ "BackgroundBlurNode - Still Image CrossOver"
+ "BackgroundBlurNode - Still Image FanOut"
+ "CameraCapture Stills Core"
+ "Digital Flash Backlit Recommend Regular Flash - Scene ( Normalized QSum SNR )"
+ "Digital Flash Recommend Regular Flash - Scene ( Normalized QSum SNR )"
+ "DigitalFlashBacklitRecommendRegularFlash"
+ "DigitalFlashRecommendRegularFlash"
+ "FeaturesEnabled"
+ "FigCaptureSessionStartDetachedSession"
+ "InitialCapacityOverhead"
+ "Jul 11 2026"
+ "LastShownBuild:BWDeferredCaptureController.m:488"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:1577"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3031"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3668"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3681"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10367"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10877"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11328"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11363"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11552"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11561"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11573"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11580"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11614"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11680"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11849"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:12788"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:15806"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18640"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:19028"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:1984"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:19873"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20295"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20297"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20299"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:22193"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:23584"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:23616"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:23772"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24530"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24776"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:25133"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:6009"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7689"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7698"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8777"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8778"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8797"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9086"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9900"
+ "LastShownBuild:BWFigVideoCaptureStream.m:3878"
+ "LastShownBuild:BWFigVideoCaptureStream.m:4298"
+ "LastShownBuild:BWGraph.m:2691"
+ "LastShownBuild:BWGraph.m:3617"
+ "LastShownBuild:BWGraph.m:3620"
+ "LastShownBuild:BWGraph.m:3623"
+ "LastShownBuild:BWIrisStagingNode.m:3884"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:13642"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:2725"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4419"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4426"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4433"
+ "LastShownBuild:BWOverCaptureSmartStyleApplyNode.m:442"
+ "LastShownBuild:BWPhotoEncoderController.m:1306"
+ "LastShownBuild:BWPhotoEncoderController.m:1309"
+ "LastShownBuild:BWPhotoEncoderController.m:1700"
+ "LastShownBuild:BWPhotoEncoderController.m:1705"
+ "LastShownBuild:BWPhotoEncoderController.m:1954"
+ "LastShownBuild:BWPhotoEncoderController.m:2093"
+ "LastShownBuild:BWPhotoEncoderController.m:2109"
+ "LastShownBuild:BWPhotoEncoderController.m:2119"
+ "LastShownBuild:BWPhotoEncoderController.m:3279"
+ "LastShownBuild:BWPhotoEncoderController.m:4664"
+ "LastShownBuild:BWPhotoEncoderController.m:6426"
+ "LastShownBuild:BWPhotoEncoderManager.m:623"
+ "LastShownBuild:BWPhotoEncoderNode.m:389"
+ "LastShownBuild:BWPixelBufferTransferRenderer.m:642"
+ "LastShownBuild:BWPreviewStitcherNode.m:3375"
+ "LastShownBuild:BWSmartStyleTargetRenderer.m:630"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1221"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1225"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1431"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1438"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1508"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1611"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1622"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:2248"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:3739"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1008"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:126"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2195"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2202"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2208"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2231"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2419"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:3031"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:3061"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:658"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:876"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:990"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:996"
+ "LastShownBuild:BWUBCaptureParameters.m:242"
+ "LastShownBuild:BWUBCaptureParameters.m:245"
+ "LastShownBuild:BWUBCaptureParameters.m:250"
+ "LastShownBuild:BWUBCaptureParameters.m:313"
+ "LastShownBuild:CMCaptureLocalSessionController.m:888"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:1539"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:6245"
+ "LastShownBuild:FigCaptureSession.m:10960"
+ "LastShownBuild:FigCaptureSession.m:11155"
+ "LastShownBuild:FigCaptureSession.m:12067"
+ "LastShownBuild:FigCaptureSession.m:18692"
+ "LastShownBuild:FigCaptureSession.m:20210"
+ "LastShownBuild:FigCaptureSession.m:20213"
+ "LastShownBuild:FigCaptureSession.m:5069"
+ "LastShownBuild:FigCaptureSession.m:9028"
+ "LastShownBuild:FigCaptureSession.m:9034"
+ "LastShownBuild:FigCaptureSession.m:9037"
+ "LastShownBuild:FigCaptureSession.m:9040"
+ "LastShownBuild:FigCaptureSession.m:9043"
+ "LastShownBuild:FigCaptureSession.m:9054"
+ "LastShownBuild:FigCaptureSession.m:9057"
+ "LastShownBuild:FigCaptureSession.m:9065"
+ "LastShownBuild:FigCaptureSession.m:9083"
+ "LastShownBuild:FigCaptureSession.m:9128"
+ "LastShownBuild:FigCaptureSession.m:9132"
+ "LastShownBuild:FigCaptureSession.m:9156"
+ "LastShownBuild:FigCaptureSession.m:9171"
+ "LastShownBuild:FigCaptureSession.m:9175"
+ "LastShownBuild:FigCaptureSession.m:9178"
+ "LastShownBuild:FigCaptureSession.m:9302"
+ "LastShownBuild:FigCaptureSession.m:9308"
+ "LastShownBuild:FigCaptureSession.m:9334"
+ "LastShownBuild:FigCaptureSession.m:9346"
+ "LastShownBuild:FigCaptureSession.m:995"
+ "LastShownBuild:FigCaptureSessionStateManager.m:515"
+ "LastShownBuild:FigCaptureSourceBackingsProvider.m:2732"
+ "LastShownBuild:FigSampleBufferProcessor_Autofocus.m:931"
+ "LastShownDate:BWDeferredCaptureController.m:488"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:1577"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3031"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3668"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3681"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10367"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10877"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11328"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11363"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11552"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11561"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11573"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11580"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11614"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11680"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11849"
+ "LastShownDate:BWFigVideoCaptureDevice.m:12788"
+ "LastShownDate:BWFigVideoCaptureDevice.m:15806"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18640"
+ "LastShownDate:BWFigVideoCaptureDevice.m:19028"
+ "LastShownDate:BWFigVideoCaptureDevice.m:1984"
+ "LastShownDate:BWFigVideoCaptureDevice.m:19873"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20295"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20297"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20299"
+ "LastShownDate:BWFigVideoCaptureDevice.m:22193"
+ "LastShownDate:BWFigVideoCaptureDevice.m:23584"
+ "LastShownDate:BWFigVideoCaptureDevice.m:23616"
+ "LastShownDate:BWFigVideoCaptureDevice.m:23772"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24530"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24776"
+ "LastShownDate:BWFigVideoCaptureDevice.m:25133"
+ "LastShownDate:BWFigVideoCaptureDevice.m:6009"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7689"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7698"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8777"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8778"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8797"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9086"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9900"
+ "LastShownDate:BWFigVideoCaptureStream.m:3878"
+ "LastShownDate:BWFigVideoCaptureStream.m:4298"
+ "LastShownDate:BWGraph.m:2691"
+ "LastShownDate:BWGraph.m:3617"
+ "LastShownDate:BWGraph.m:3620"
+ "LastShownDate:BWGraph.m:3623"
+ "LastShownDate:BWIrisStagingNode.m:3884"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:13642"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:2725"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4419"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4426"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4433"
+ "LastShownDate:BWOverCaptureSmartStyleApplyNode.m:442"
+ "LastShownDate:BWPhotoEncoderController.m:1306"
+ "LastShownDate:BWPhotoEncoderController.m:1309"
+ "LastShownDate:BWPhotoEncoderController.m:1700"
+ "LastShownDate:BWPhotoEncoderController.m:1705"
+ "LastShownDate:BWPhotoEncoderController.m:1954"
+ "LastShownDate:BWPhotoEncoderController.m:2093"
+ "LastShownDate:BWPhotoEncoderController.m:2109"
+ "LastShownDate:BWPhotoEncoderController.m:2119"
+ "LastShownDate:BWPhotoEncoderController.m:3279"
+ "LastShownDate:BWPhotoEncoderController.m:4664"
+ "LastShownDate:BWPhotoEncoderController.m:6426"
+ "LastShownDate:BWPhotoEncoderManager.m:623"
+ "LastShownDate:BWPhotoEncoderNode.m:389"
+ "LastShownDate:BWPixelBufferTransferRenderer.m:642"
+ "LastShownDate:BWPreviewStitcherNode.m:3375"
+ "LastShownDate:BWSmartStyleTargetRenderer.m:630"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1221"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1225"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1431"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1438"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1508"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1611"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1622"
+ "LastShownDate:BWStillImageCoordinatorNode.m:2248"
+ "LastShownDate:BWStillImageCoordinatorNode.m:3739"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1008"
+ "LastShownDate:BWStillImageMetadataUtilities.m:126"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2195"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2202"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2208"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2231"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2419"
+ "LastShownDate:BWStillImageMetadataUtilities.m:3031"
+ "LastShownDate:BWStillImageMetadataUtilities.m:3061"
+ "LastShownDate:BWStillImageMetadataUtilities.m:658"
+ "LastShownDate:BWStillImageMetadataUtilities.m:876"
+ "LastShownDate:BWStillImageMetadataUtilities.m:990"
+ "LastShownDate:BWStillImageMetadataUtilities.m:996"
+ "LastShownDate:BWUBCaptureParameters.m:242"
+ "LastShownDate:BWUBCaptureParameters.m:245"
+ "LastShownDate:BWUBCaptureParameters.m:250"
+ "LastShownDate:BWUBCaptureParameters.m:313"
+ "LastShownDate:CMCaptureLocalSessionController.m:888"
+ "LastShownDate:FigCaptureMetadataUtilities.m:1539"
+ "LastShownDate:FigCaptureMetadataUtilities.m:6245"
+ "LastShownDate:FigCaptureSession.m:10960"
+ "LastShownDate:FigCaptureSession.m:11155"
+ "LastShownDate:FigCaptureSession.m:12067"
+ "LastShownDate:FigCaptureSession.m:18692"
+ "LastShownDate:FigCaptureSession.m:20210"
+ "LastShownDate:FigCaptureSession.m:20213"
+ "LastShownDate:FigCaptureSession.m:5069"
+ "LastShownDate:FigCaptureSession.m:9028"
+ "LastShownDate:FigCaptureSession.m:9034"
+ "LastShownDate:FigCaptureSession.m:9037"
+ "LastShownDate:FigCaptureSession.m:9040"
+ "LastShownDate:FigCaptureSession.m:9043"
+ "LastShownDate:FigCaptureSession.m:9054"
+ "LastShownDate:FigCaptureSession.m:9057"
+ "LastShownDate:FigCaptureSession.m:9065"
+ "LastShownDate:FigCaptureSession.m:9083"
+ "LastShownDate:FigCaptureSession.m:9128"
+ "LastShownDate:FigCaptureSession.m:9132"
+ "LastShownDate:FigCaptureSession.m:9156"
+ "LastShownDate:FigCaptureSession.m:9171"
+ "LastShownDate:FigCaptureSession.m:9175"
+ "LastShownDate:FigCaptureSession.m:9178"
+ "LastShownDate:FigCaptureSession.m:9302"
+ "LastShownDate:FigCaptureSession.m:9308"
+ "LastShownDate:FigCaptureSession.m:9334"
+ "LastShownDate:FigCaptureSession.m:9346"
+ "LastShownDate:FigCaptureSession.m:995"
+ "LastShownDate:FigCaptureSessionStateManager.m:515"
+ "LastShownDate:FigCaptureSourceBackingsProvider.m:2732"
+ "LastShownDate:FigSampleBufferProcessor_Autofocus.m:931"
+ "Parent of shared pool output should have a prepared pool: attachedMediaKey=%{public}@ sharedPoolOutput=%{public}@ parentOutput=%{public}@ parentAttachedMediaKey=%{public}@"
+ "ProductID"
+ "SushiRAW LSC GainMap failed to convert V3 LSC gain grid to V2 (err:%{public}d, AD:%{public}.1f microns)"
+ "VendorID"
+ "[graph connectOutput:backgroundBlurNode.stillImageOutput toInput:backgroundBlurStillImageFanOut.input pipelineStage:((void *)0)]"
+ "[super addNode:backgroundBlurStillImageFanOut error:&error]"
+ "com.apple.coremedia.BWSmartCropNode.rtscInit"
+ "description=CameraCapture-761.0.0.0.3"
+ "outputAspectRatioOverride"
+ "simu_getNoiseProfileFromSensorParams"
+ "ub.scene.digitalFlashBacklitRecommendRegularFlashSNR"
+ "ub.scene.digitalFlashRecommendRegularFlashSNR"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x81\xf0\xf0q"
- "%@ %p: captureID:%lld '%.4s'('%.4s')%@ %dx%d R:%d%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
- "%@ %p: requestID:%d appliedFrameStatistics:%@"
- "(*modified by nonDestructiveCrop)"
- "+[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByDeviceType:position:requestID:]"
- "-[BWFigCaptureDevice _invalidateSyncStreamGroupsAndControlledStreams:preserveTorchState:]"
- "-[BWFigCaptureDevice invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:]"
- "-[BWFigCaptureDeviceVendor _invalidate:keepFigCaptureDeviceAlive:preserveTorchState:]"
- "-[BWFigCaptureStream synchronizedStreamsGroupDidStop]"
- "-[BWPhotoEncoderController _cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:]"
- "-[BWTemporalFilterNode didReachEndOfDataForInput:]"
- "-[BWTemporalFilterNode didReachEndOfDataForInput:]_block_invoke"
- "-[BWTemporalFilterNode prepareForCurrentConfigurationToBecomeLive]"
- "-[FigCaptureAncillaryDataHIDTransmitter openDeviceWithUsagePage:usage:error:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CMCaptureLocal/CMCaptureLocalSessionController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CameraViewfinder/FigCaptureSessionObserver.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureMetadataUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSessionPipelines.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSessionStateManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSourceBackingsProvider.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/CMCaptureUserNotification.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureCommon.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unknown flip %i"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unsupported rotation of %d degrees"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: rotationDegrees (%d) is invalid, must be 0/90/180/270. Returning kFigExifOrientation_0RowTop0ColLeft (%d)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigCapturePixelFormatUtilities.m %s: Unexpected plist value for a pixel format type: %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Cannot look up key.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Not adding key.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Returning 0."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Key (%s) has already been registered. Not adding key.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: keyspace not found, has no name"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigRemoteQueue/FigRemoteQueue.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWDeviceMotionActivityDetector.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigCaptureDeviceVendor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureDevice.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureStream.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFrameStatistics.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWGraph.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWInvalidFramesChecker.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing noise reduction and sharpening parameters"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing portType"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing sensorIDDictionary"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing MBNR parameters for type '%d' and gain '%.1f'"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing noise reduction and sharpening parameters for type '%d' and gain '%.1f'"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWPixelBufferPool.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing PortType"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing cameraInfo"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDDictionary"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDString"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil input for %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil portType for %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@ took %lld ms"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@..."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Couldn't find Deep Fusion HDR EV0 count for EIT '%f': %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Missing portType"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then Long-Without-Sphere threshold: %@."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then SIFR-Main threshold: %@."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Motion and focus scores RFS is specified, but weights are missing: %@."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. SIFR-Main threshold should be smaller then Long-Without-Sphere threshold: %@."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWVideoFormat.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWAudioSourceNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWCameraInfoMetadataNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDeferredCaptureController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDepthConverterNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWFileCoordinatorNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWFrameRateGovernorNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWImageQueueSinkNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWIrisStagingNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWLearnSmartStyleRenderer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWMultiStreamCameraSourceNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWOverCaptureSmartStyleApplyNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPiecemealEncodingNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPreviewStitcherNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPreviewTimeMachineSinkNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSensitiveContentAnalyzerSinkNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSmartStyleReversibilityRenderer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSmartStyleTargetRenderer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageCoordinatorNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageScalerNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSynchronizerNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVISNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVideoPIPOverlayNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWAggdDataReporter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWCoreAnalyticsReporter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFencedAnimationQueue.m %s: Fenced animation queue wait timeout occurred - not queuing animation"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFigVideoCaptureSynchronizedStreamsGroup.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWPixelBufferTransferRenderer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWStillImageMetadataUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/Autofocus/FigSampleBufferProcessor_Autofocus.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: %d motion-related log messages filtered out (max of 1/s displayed from FigCoreMotionDelegate)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration fused vector is computed incorrectly"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration vector is computed incorrectly"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Allocation error when retrieving motion data"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Closest motion sample for timestamp %f has timestamp %f, difference %f\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not find motion sample to get Quaternion.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not lock the ringMutex\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Frame timestamp is %f, Sample timestamps in the ring buffer are from %f to %f\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Gravity is computed incorrectly"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Potential missing three motion samples: new timestamp %f, latest timestamp %f\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: no data semaphore was available to wait on"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: %d motion-related log messages filtered out (max of 1/s displayed from FigMotionProcessingUtilities)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall sample for the given timestamp on hallPositionIndex %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall samples in given time range [%f, %f]. Use the closest Hall sample in actual time range [%f, %f]."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find a motion sample within %fms of the current frame. Frame timestamp is %f, sample timestamps in the ring buffer are from %f to %f, latestTimeDifference %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find motion sample to get Quaternion."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find the closest motion sample index in the ring buffer for the frame timestamp (%f)."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP Hall samples"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP motion samples"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming default value of 1.0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming value of %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Frame timestamp is from %f to %f, Sample timestamps in the ring buffer are from %f to %f, get %d motion samples"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Motion Hardware Unavailable - prototype hardware detected"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: No valid baseZoomFactor found, will proceed with a value of 1.0f."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Quaternion pointer is null!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Time interval %f is not positive"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Too many motion samples for the array"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Unsupported Hall data version %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Using default focus characterization entry because an entry corresponding to the original requested values was not found."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after Hall sample timestamp difference is close to 0.0f!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after motion sample timestamp difference is close to 0.0f!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: interpolateQuaternionsByAngle: delta quaternion w %f is larger than 1"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: invalid micronsPerPixel value %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed computing scaling factor"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed extracting metadata"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed getting ISPFrameCorrectionShiftValues. Using value of 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Unsupported sag removal method"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: sagPosition memory allocation failed"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Could not parse motion data from ISP due to error: %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Failed to allocate and initialize VISRotationCorrectionEstimator"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Height is missing from visInputPixelBufferAttributes"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData from metadataDict"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PinholeCameraFocalLength in metadataDict"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PortType from metadataDict"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSize for portType: %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSizeInMicrons for port %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing portType in metadataDict"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: No motion samples for this frame. Skipping processing"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Overscan is 0 or less. l:%f r:%f t:%f b:%f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Timestamp %f is earlier than previous sample %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Width is missing from visInputPixelBufferAttributes"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: focalLength is null"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: pole must be between 0 and 1"
- "08:29:03"
- "<%@: %p> lowLightEIT=%f, sifrMainEIT=%f, sifrGain=%f, lowLightHDRWithoutSIFR=%f, longWithoutSphere=%f, deepFusion=%f, rsmMainEIT=%f, rsmSIFRGain=%f, toneCurveBehavior=%d, preserveBlackLevel=%d, afWindows=%p, refMethod=%d, usePreviousSIFR=%d, motionAndFocusScoreWeights=%@, maxNumberOfFramesForAdaptiveBracketing=%d, dFlashAvailableEIT=%f, dFlashRecommendedEIT=%f, dFlashStationaryRecommendedEIT=%f, dFlashAvailableSNR=%f, dFlashAvailableSNRLag=%f, dFlashRecommendedSNR=%f, dFlashRecommendedSNRLag=%f, dFlashStationaryRecommendedSNR=%f, dFlashStationaryRecommendedSNRLag=%f, dFlashRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashAERelativeDiff=%f%@"
- "<<< FigCaptureCustomExposureConfiguration >>> %s: Unexpected use of invalid min ISO: %@ applied to %@"
- "<<<< BWSmartFramingSceneMonitor >>>> %s: TrackedSubject scores: groupID (%@), gazeScore (%f), significanceScore (%f), isSignificant (%d), gazeScoreF (%f), significanceScoreF (%f), isSignificantF (%d)"
- "<<<< BWTemporalFilterNode >>>> %s: %@ %@ is EOD"
- "<<<< BWTemporalFilterNode >>>> %s: Attempted to create a new MCTF session before the last one is invalidated"
- "<<<< BWTemporalFilterNode >>>> %s: ConfigurationID %lld is now live for input %@"
- "<<<< BWTemporalFilterNode >>>> %s: MCTF session is nil"
- "Jun 27 2026"
- "LastShownBuild:BWDeferredCaptureController.m:468"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:1564"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3018"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3654"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3667"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10323"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10833"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11284"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11319"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11508"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11517"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11529"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11536"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11570"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11636"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11805"
- "LastShownBuild:BWFigVideoCaptureDevice.m:12727"
- "LastShownBuild:BWFigVideoCaptureDevice.m:15744"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18576"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18964"
- "LastShownBuild:BWFigVideoCaptureDevice.m:1960"
- "LastShownBuild:BWFigVideoCaptureDevice.m:19771"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20193"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20195"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20197"
- "LastShownBuild:BWFigVideoCaptureDevice.m:22094"
- "LastShownBuild:BWFigVideoCaptureDevice.m:23484"
- "LastShownBuild:BWFigVideoCaptureDevice.m:23516"
- "LastShownBuild:BWFigVideoCaptureDevice.m:23672"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24430"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24676"
- "LastShownBuild:BWFigVideoCaptureDevice.m:25033"
- "LastShownBuild:BWFigVideoCaptureDevice.m:5970"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7647"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7656"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8733"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8734"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8753"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9042"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9856"
- "LastShownBuild:BWFigVideoCaptureStream.m:3854"
- "LastShownBuild:BWFigVideoCaptureStream.m:4274"
- "LastShownBuild:BWGraph.m:3582"
- "LastShownBuild:BWGraph.m:3585"
- "LastShownBuild:BWGraph.m:3598"
- "LastShownBuild:BWIrisStagingNode.m:3867"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:13588"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:2717"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4399"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4406"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4413"
- "LastShownBuild:BWOverCaptureSmartStyleApplyNode.m:420"
- "LastShownBuild:BWPhotoEncoderController.m:1308"
- "LastShownBuild:BWPhotoEncoderController.m:1311"
- "LastShownBuild:BWPhotoEncoderController.m:1697"
- "LastShownBuild:BWPhotoEncoderController.m:1702"
- "LastShownBuild:BWPhotoEncoderController.m:1955"
- "LastShownBuild:BWPhotoEncoderController.m:2094"
- "LastShownBuild:BWPhotoEncoderController.m:2110"
- "LastShownBuild:BWPhotoEncoderController.m:2120"
- "LastShownBuild:BWPhotoEncoderController.m:3278"
- "LastShownBuild:BWPhotoEncoderController.m:4666"
- "LastShownBuild:BWPhotoEncoderController.m:6395"
- "LastShownBuild:BWPhotoEncoderManager.m:656"
- "LastShownBuild:BWPhotoEncoderNode.m:393"
- "LastShownBuild:BWPixelBufferTransferRenderer.m:639"
- "LastShownBuild:BWPreviewStitcherNode.m:3318"
- "LastShownBuild:BWSmartStyleTargetRenderer.m:626"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1209"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1213"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1419"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1426"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1496"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1599"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1610"
- "LastShownBuild:BWStillImageCoordinatorNode.m:2229"
- "LastShownBuild:BWStillImageCoordinatorNode.m:3713"
- "LastShownBuild:BWStillImageMetadataUtilities.m:120"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1911"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1918"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1924"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1947"
- "LastShownBuild:BWStillImageMetadataUtilities.m:2714"
- "LastShownBuild:BWStillImageMetadataUtilities.m:2744"
- "LastShownBuild:BWStillImageMetadataUtilities.m:652"
- "LastShownBuild:BWStillImageMetadataUtilities.m:786"
- "LastShownBuild:BWStillImageMetadataUtilities.m:965"
- "LastShownBuild:BWStillImageMetadataUtilities.m:971"
- "LastShownBuild:BWStillImageMetadataUtilities.m:983"
- "LastShownBuild:BWUBCaptureParameters.m:222"
- "LastShownBuild:BWUBCaptureParameters.m:228"
- "LastShownBuild:BWUBCaptureParameters.m:231"
- "LastShownBuild:BWUBCaptureParameters.m:299"
- "LastShownBuild:CMCaptureLocalSessionController.m:878"
- "LastShownBuild:FigCaptureMetadataUtilities.m:1533"
- "LastShownBuild:FigCaptureMetadataUtilities.m:6235"
- "LastShownBuild:FigCaptureSession.m:10919"
- "LastShownBuild:FigCaptureSession.m:11114"
- "LastShownBuild:FigCaptureSession.m:12026"
- "LastShownBuild:FigCaptureSession.m:18514"
- "LastShownBuild:FigCaptureSession.m:20016"
- "LastShownBuild:FigCaptureSession.m:20019"
- "LastShownBuild:FigCaptureSession.m:5059"
- "LastShownBuild:FigCaptureSession.m:8996"
- "LastShownBuild:FigCaptureSession.m:9002"
- "LastShownBuild:FigCaptureSession.m:9005"
- "LastShownBuild:FigCaptureSession.m:9008"
- "LastShownBuild:FigCaptureSession.m:9011"
- "LastShownBuild:FigCaptureSession.m:9022"
- "LastShownBuild:FigCaptureSession.m:9025"
- "LastShownBuild:FigCaptureSession.m:9033"
- "LastShownBuild:FigCaptureSession.m:9051"
- "LastShownBuild:FigCaptureSession.m:9096"
- "LastShownBuild:FigCaptureSession.m:9100"
- "LastShownBuild:FigCaptureSession.m:9124"
- "LastShownBuild:FigCaptureSession.m:9139"
- "LastShownBuild:FigCaptureSession.m:9143"
- "LastShownBuild:FigCaptureSession.m:9146"
- "LastShownBuild:FigCaptureSession.m:9269"
- "LastShownBuild:FigCaptureSession.m:9275"
- "LastShownBuild:FigCaptureSession.m:9301"
- "LastShownBuild:FigCaptureSession.m:9313"
- "LastShownBuild:FigCaptureSession.m:992"
- "LastShownBuild:FigCaptureSessionStateManager.m:511"
- "LastShownBuild:FigCaptureSourceBackingsProvider.m:2728"
- "LastShownBuild:FigSampleBufferProcessor_Autofocus.m:928"
- "LastShownDate:BWDeferredCaptureController.m:468"
- "LastShownDate:BWFigCaptureDeviceVendor.m:1564"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3018"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3654"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3667"
- "LastShownDate:BWFigVideoCaptureDevice.m:10323"
- "LastShownDate:BWFigVideoCaptureDevice.m:10833"
- "LastShownDate:BWFigVideoCaptureDevice.m:11284"
- "LastShownDate:BWFigVideoCaptureDevice.m:11319"
- "LastShownDate:BWFigVideoCaptureDevice.m:11508"
- "LastShownDate:BWFigVideoCaptureDevice.m:11517"
- "LastShownDate:BWFigVideoCaptureDevice.m:11529"
- "LastShownDate:BWFigVideoCaptureDevice.m:11536"
- "LastShownDate:BWFigVideoCaptureDevice.m:11570"
- "LastShownDate:BWFigVideoCaptureDevice.m:11636"
- "LastShownDate:BWFigVideoCaptureDevice.m:11805"
- "LastShownDate:BWFigVideoCaptureDevice.m:12727"
- "LastShownDate:BWFigVideoCaptureDevice.m:15744"
- "LastShownDate:BWFigVideoCaptureDevice.m:18576"
- "LastShownDate:BWFigVideoCaptureDevice.m:18964"
- "LastShownDate:BWFigVideoCaptureDevice.m:1960"
- "LastShownDate:BWFigVideoCaptureDevice.m:19771"
- "LastShownDate:BWFigVideoCaptureDevice.m:20193"
- "LastShownDate:BWFigVideoCaptureDevice.m:20195"
- "LastShownDate:BWFigVideoCaptureDevice.m:20197"
- "LastShownDate:BWFigVideoCaptureDevice.m:22094"
- "LastShownDate:BWFigVideoCaptureDevice.m:23484"
- "LastShownDate:BWFigVideoCaptureDevice.m:23516"
- "LastShownDate:BWFigVideoCaptureDevice.m:23672"
- "LastShownDate:BWFigVideoCaptureDevice.m:24430"
- "LastShownDate:BWFigVideoCaptureDevice.m:24676"
- "LastShownDate:BWFigVideoCaptureDevice.m:25033"
- "LastShownDate:BWFigVideoCaptureDevice.m:5970"
- "LastShownDate:BWFigVideoCaptureDevice.m:7647"
- "LastShownDate:BWFigVideoCaptureDevice.m:7656"
- "LastShownDate:BWFigVideoCaptureDevice.m:8733"
- "LastShownDate:BWFigVideoCaptureDevice.m:8734"
- "LastShownDate:BWFigVideoCaptureDevice.m:8753"
- "LastShownDate:BWFigVideoCaptureDevice.m:9042"
- "LastShownDate:BWFigVideoCaptureDevice.m:9856"
- "LastShownDate:BWFigVideoCaptureStream.m:3854"
- "LastShownDate:BWFigVideoCaptureStream.m:4274"
- "LastShownDate:BWGraph.m:3582"
- "LastShownDate:BWGraph.m:3585"
- "LastShownDate:BWGraph.m:3598"
- "LastShownDate:BWIrisStagingNode.m:3867"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:13588"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:2717"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4399"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4406"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4413"
- "LastShownDate:BWOverCaptureSmartStyleApplyNode.m:420"
- "LastShownDate:BWPhotoEncoderController.m:1308"
- "LastShownDate:BWPhotoEncoderController.m:1311"
- "LastShownDate:BWPhotoEncoderController.m:1697"
- "LastShownDate:BWPhotoEncoderController.m:1702"
- "LastShownDate:BWPhotoEncoderController.m:1955"
- "LastShownDate:BWPhotoEncoderController.m:2094"
- "LastShownDate:BWPhotoEncoderController.m:2110"
- "LastShownDate:BWPhotoEncoderController.m:2120"
- "LastShownDate:BWPhotoEncoderController.m:3278"
- "LastShownDate:BWPhotoEncoderController.m:4666"
- "LastShownDate:BWPhotoEncoderController.m:6395"
- "LastShownDate:BWPhotoEncoderManager.m:656"
- "LastShownDate:BWPhotoEncoderNode.m:393"
- "LastShownDate:BWPixelBufferTransferRenderer.m:639"
- "LastShownDate:BWPreviewStitcherNode.m:3318"
- "LastShownDate:BWSmartStyleTargetRenderer.m:626"
- "LastShownDate:BWStillImageCoordinatorNode.m:1209"
- "LastShownDate:BWStillImageCoordinatorNode.m:1213"
- "LastShownDate:BWStillImageCoordinatorNode.m:1419"
- "LastShownDate:BWStillImageCoordinatorNode.m:1426"
- "LastShownDate:BWStillImageCoordinatorNode.m:1496"
- "LastShownDate:BWStillImageCoordinatorNode.m:1599"
- "LastShownDate:BWStillImageCoordinatorNode.m:1610"
- "LastShownDate:BWStillImageCoordinatorNode.m:2229"
- "LastShownDate:BWStillImageCoordinatorNode.m:3713"
- "LastShownDate:BWStillImageMetadataUtilities.m:120"
- "LastShownDate:BWStillImageMetadataUtilities.m:1911"
- "LastShownDate:BWStillImageMetadataUtilities.m:1918"
- "LastShownDate:BWStillImageMetadataUtilities.m:1924"
- "LastShownDate:BWStillImageMetadataUtilities.m:1947"
- "LastShownDate:BWStillImageMetadataUtilities.m:2714"
- "LastShownDate:BWStillImageMetadataUtilities.m:2744"
- "LastShownDate:BWStillImageMetadataUtilities.m:652"
- "LastShownDate:BWStillImageMetadataUtilities.m:786"
- "LastShownDate:BWStillImageMetadataUtilities.m:965"
- "LastShownDate:BWStillImageMetadataUtilities.m:971"
- "LastShownDate:BWStillImageMetadataUtilities.m:983"
- "LastShownDate:BWUBCaptureParameters.m:222"
- "LastShownDate:BWUBCaptureParameters.m:228"
- "LastShownDate:BWUBCaptureParameters.m:231"
- "LastShownDate:BWUBCaptureParameters.m:299"
- "LastShownDate:CMCaptureLocalSessionController.m:878"
- "LastShownDate:FigCaptureMetadataUtilities.m:1533"
- "LastShownDate:FigCaptureMetadataUtilities.m:6235"
- "LastShownDate:FigCaptureSession.m:10919"
- "LastShownDate:FigCaptureSession.m:11114"
- "LastShownDate:FigCaptureSession.m:12026"
- "LastShownDate:FigCaptureSession.m:18514"
- "LastShownDate:FigCaptureSession.m:20016"
- "LastShownDate:FigCaptureSession.m:20019"
- "LastShownDate:FigCaptureSession.m:5059"
- "LastShownDate:FigCaptureSession.m:8996"
- "LastShownDate:FigCaptureSession.m:9002"
- "LastShownDate:FigCaptureSession.m:9005"
- "LastShownDate:FigCaptureSession.m:9008"
- "LastShownDate:FigCaptureSession.m:9011"
- "LastShownDate:FigCaptureSession.m:9022"
- "LastShownDate:FigCaptureSession.m:9025"
- "LastShownDate:FigCaptureSession.m:9033"
- "LastShownDate:FigCaptureSession.m:9051"
- "LastShownDate:FigCaptureSession.m:9096"
- "LastShownDate:FigCaptureSession.m:9100"
- "LastShownDate:FigCaptureSession.m:9124"
- "LastShownDate:FigCaptureSession.m:9139"
- "LastShownDate:FigCaptureSession.m:9143"
- "LastShownDate:FigCaptureSession.m:9146"
- "LastShownDate:FigCaptureSession.m:9269"
- "LastShownDate:FigCaptureSession.m:9275"
- "LastShownDate:FigCaptureSession.m:9301"
- "LastShownDate:FigCaptureSession.m:9313"
- "LastShownDate:FigCaptureSession.m:992"
- "LastShownDate:FigCaptureSessionStateManager.m:511"
- "LastShownDate:FigCaptureSourceBackingsProvider.m:2728"
- "LastShownDate:FigSampleBufferProcessor_Autofocus.m:928"
- "description=CameraCapture-758.0.0.0.1"
- "sourceNodesCount > _deferredStartSourceNodes.count"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0a\xf0\xf0Q"
```
