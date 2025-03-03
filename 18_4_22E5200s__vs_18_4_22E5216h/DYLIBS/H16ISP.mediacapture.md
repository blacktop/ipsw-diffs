## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-3.504.14.0.0
-  __TEXT.__text: 0x1afa48
+3.509.0.0.0
+  __TEXT.__text: 0x1b24fc
   __TEXT.__auth_stubs: 0x3180
   __TEXT.__init_offsets: 0x18
   __TEXT.__objc_methlist: 0x268
-  __TEXT.__const: 0x235df
-  __TEXT.__oslogstring: 0x1be0a
-  __TEXT.__cstring: 0x18325
-  __TEXT.__gcc_except_tab: 0x6510
-  __TEXT.__unwind_info: 0x3c58
+  __TEXT.__const: 0x236af
+  __TEXT.__oslogstring: 0x1c4ce
+  __TEXT.__cstring: 0x185e5
+  __TEXT.__gcc_except_tab: 0x64f8
+  __TEXT.__unwind_info: 0x3ca0
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_classname: 0x89
   __TEXT.__objc_methname: 0x1cbd
   __TEXT.__objc_methtype: 0x105f
   __TEXT.__objc_stubs: 0x1f80
-  __DATA_CONST.__got: 0x3228
-  __DATA_CONST.__const: 0x87c0
+  __DATA_CONST.__got: 0x3238
+  __DATA_CONST.__const: 0xa270
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x18d0
-  __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x2740
-  __AUTH_CONST.__cfstring: 0x9bc0
+  __AUTH_CONST.__auth_ptr: 0x98
+  __AUTH_CONST.__const: 0x2718
+  __AUTH_CONST.__cfstring: 0x9c00
   __AUTH_CONST.__objc_const: 0x880
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x34
-  __DATA.__data: 0x334640
-  __DATA.__bss: 0xe9
+  __DATA.__data: 0x334648
+  __DATA.__bss: 0x1f1
   __DATA.__common: 0x54
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x110
+  __DATA_DIRTY.__data: 0x118
   __DATA_DIRTY.__bss: 0x94c
   __DATA_DIRTY.__common: 0x5558
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/AppleCVHWA.framework/AppleCVHWA
   - /System/Library/PrivateFrameworks/AppleDepth.framework/AppleDepth
   - /System/Library/PrivateFrameworks/AppleDepthCore.framework/AppleDepthCore
-  - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture
+  - /System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore
+  - /System/Library/PrivateFrameworks/CMCaptureDevice.framework/CMCaptureDevice
   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5410
-  Symbols:   8850
-  CStrings:  6405
+  Functions: 5459
+  Symbols:   8905
+  CStrings:  6465
 
Symbols:
+ _FigCFEqual
+ _FigGetUpTime
+ __Z20FigMotionGetGravityZPK14__CFDictionaryPf
+ __Z30FigMotionComputePrincipalPointPK14__CFDictionaryffdiiiihP7CGPoint
+ __Z37FigMotionAdjustPointForSphereMovementPK14__CFDictionaryffdP7CGPoint
+ __Z37FigMotionComputeAverageSpherePositionPK14__CFDictionarydP11FigPosition
+ __Z38FigMotionCalculateAdjustedLensPositionPK14__CFDictionaryfP26CameraCharacterizationDatafPf
+ __Z39FigMotionCalculateAdjustedFocusPositionffPi
+ __Z41FigMotionComputeLensPositionScalingFactorPK14__CFDictionaryiiiiPf
+ __ZN20GMCProcessorInternal21updatePCECalibWithISFEddddP22H16ISPAnalyticsGMCInfoRK26sCIspCmdChPearlCalibrationRS2_
+ __ZN6H16ISP23DepthRearConfigurations8supportsEj
+ __ZN6H16ISP24DepthFrontConfigurations8supportsEj15ePearlHWVersion
+ __ZN6H16ISP31DepthFrontRotatedConfigurations8supportsEj15ePearlHWVersion
+ __ZN6H16ISP40H16ISPGraphExclaveAttentionDetectionNode17AddFaceIDMetadataEPNS_24H16ISPFilterGraphMessageEP28ISPExclaveCoreChRunKitADRsltb
+ __ZNK11IsfInternal20getHistoryStatisticsERN3Isf20IsfHistoryStatisticsE
+ __ZNK11IsfInternal24getHistoryAxisStatisticsEiRN3Isf24IsfHistoryAxisStatisticsE
+ __ZNK18H16ISPFirmwareWork17IsInternalVariantEv
+ __ZNK3Isf20getHistoryStatisticsERNS_20IsfHistoryStatisticsE
+ _kFigCaptureStreamMetadata_PortType
+ _kFigCaptureStreamSecureFaceIDReadinessKey_UserEngagementStatus
+ _os_variant_allows_internal_security_policies
+ _os_variant_has_internal_content
- _FigMotionCalculateAdjustedLensPosition
- _FigMotionComputeLensPositionScalingFactor
- _FigMotionComputePrincipalPoint
- _FigMotionGetGravityZ
- __ZN12GMCProcessor20postProcessStereoGMCE12_GMC_Results26sCIspCmdChPearlCalibration18GMCInnerStatisticsyb
- __ZN20GMCProcessorInternal21updatePCECalibWithISFEddddRK26sCIspCmdChPearlCalibrationRS0_
- __ZN6H16ISP23DepthRearConfigurations8supportsEjPK24H16ISPPlatformInfoStruct
CStrings:
+ "%s - Could not find Hall samples in given time range [%f, %f]. Use the closest Hall sample in actual time range [%f, %f].\n"
+ "%s - Could not find any CropRect in the metadata dictionary!\n"
+ "%s - Empty ISP motion data\n"
+ "%s - ExposureTime missing from metadata\n"
+ "%s - Extracting only the first %d ISP Hall samples\n"
+ "%s - Face ID PreCheck uxFeedback=0x%08X, hasAttention=%{bool}d, isUserEngaged=%{bool}d\n"
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
+ "%s - Unexpected GMC type %d\n"
+ "%s - Unsupported Hall data version %d\n"
+ "%s - binningFactorHorizontal is not strictly positive!\n"
+ "%s - binningFactorVertical is not strictly positive!\n"
+ "%s - illegal RPC access\n"
+ "%s - metadataDict is null!\n"
+ "%s - metadataDict or adjustedPrincipalPointOut is null!\n"
+ "%s-Ch%d.DAT"
+ "/private/var/mobile/tmp/com.apple.cameracaptured/"
+ "/usr/local/share/firmware/isp/CmPM-CALm"
+ "/usr/local/share/firmware/isp/CmPM-DPCd"
+ "/usr/local/share/firmware/isp/CmPM-DPCm"
+ "/usr/local/share/firmware/isp/CmPM-brcl"
+ "/usr/local/share/firmware/isp/CmPM-brgd"
+ "/usr/local/share/firmware/isp/CmPM-dcnu"
+ "Correspondences"
+ "EXCLAVE_EMPTY_QUEUE_ENABLE ch 0x%x tailspinCode 0x%x"
+ "EXCLAVE_SOURCE_AE_REQ_LATE ch 0x%x tailspinCode 0x%x"
+ "FaceHeight"
+ "FaceWidth"
+ "FaceX"
+ "FaceY"
+ "Failed, too many events - Stop logging!.\n"
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
+ "IsfDifferenceXMaxMin"
+ "IsfDifferenceXQ31"
+ "IsfDifferenceYMaxMin"
+ "IsfDifferenceYQ31"
+ "IsfDifferenceZMaxMin"
+ "IsfDifferenceZQ31"
+ "Pearl Calibration (MI): Current session isn't suitable for algorithm (square color buffers)\n"
+ "TailspinNotification"
+ "TailspinNotification unknown messageType 0x%08x\n"
+ "TemperatureDiffSincePrevConvergence"
+ "TimeSincePrevConvergence"
+ "TriggeringReason"
+ "[Exclaves]: Face crop score is %f (i.e., no face in FOV). Return empty dictionary\n"
+ "daemon"
+ "dumpTailspinInBackground dirAndPrefix %s reason %s requested but tailspins not supported\n"
+ "kH16ISPTailspinAEReqLate ch %u tailspinCode 0x%08x\n"
+ "kH16ISPTailspinExclaveEmptyQueue ch %u tailspinCode 0x%08x\n"
+ "tailspinDir"
- "%s - Could not set strobe state, res = 0x%x\n\n"
- "%s - IR-RGB\n"
- "%s - Stereo GMC reporting analytics\n"
- "%s - Stereo-GMC post processing done\n"
- "%s - [Exclaves]: Face ID PreCheck uxFeedback=0x%08X readiness=%s\n"
- "/usr/local/share/firmware/isp/CmPM-CALm.DAT"
- "/usr/local/share/firmware/isp/CmPM-DPCd.DAT"
- "/usr/local/share/firmware/isp/CmPM-DPCm.DAT"
- "/usr/local/share/firmware/isp/CmPM-brcl.DAT"
- "/usr/local/share/firmware/isp/CmPM-brgd.DAT"
- "/usr/local/share/firmware/isp/CmPM-dcnu.DAT"
- "SetTorchLevel"
- "SetTorchManualParameters"
- "SetTorchSegmentParameters"
- "[Exclaves]: Face confidence is less than 0.0 (i.e., no face in FOV). Return empty dictionary\n"
- "failed, event-logging array is not set up correctly.\n"
- "postProcessStereoGMC_block_invoke"

```
