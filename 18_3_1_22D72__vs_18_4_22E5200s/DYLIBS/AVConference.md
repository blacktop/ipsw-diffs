## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2100.5.1.1.1
-  __TEXT.__text: 0x6c2878
-  __TEXT.__auth_stubs: 0x5060
-  __TEXT.__objc_methlist: 0x2de40
-  __TEXT.__const: 0x7e10
-  __TEXT.__cstring: 0x8081d
-  __TEXT.__oslogstring: 0xededf
-  __TEXT.__gcc_except_tab: 0x2550
+2105.5.1.0.0
+  __TEXT.__text: 0x6c9960
+  __TEXT.__auth_stubs: 0x5050
+  __TEXT.__objc_methlist: 0x31208
+  __TEXT.__const: 0x7a60
+  __TEXT.__cstring: 0x809fe
+  __TEXT.__oslogstring: 0xee28a
+  __TEXT.__gcc_except_tab: 0x26d8
   __TEXT.__ustring: 0x144
-  __TEXT.__unwind_info: 0xd2d8
+  __TEXT.__unwind_info: 0xeeb8
   __TEXT.__objc_classname: 0x47d1
-  __TEXT.__objc_methname: 0x7292c
-  __TEXT.__objc_methtype: 0x248b4
-  __TEXT.__objc_stubs: 0x48380
-  __DATA_CONST.__got: 0x18d8
-  __DATA_CONST.__const: 0x61e0
+  __TEXT.__objc_methname: 0x72b29
+  __TEXT.__objc_methtype: 0x248f1
+  __TEXT.__objc_stubs: 0x48460
+  __DATA_CONST.__got: 0x18e0
+  __DATA_CONST.__const: 0x61c0
   __DATA_CONST.__objc_classlist: 0x1180
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x440
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14ad0
+  __DATA_CONST.__objc_selrefs: 0x14ce8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0xfa8
   __DATA_CONST.__objc_arraydata: 0x25a0
-  __AUTH_CONST.__auth_got: 0x2848
-  __AUTH_CONST.__auth_ptr: 0xc8
-  __AUTH_CONST.__const: 0x3390
-  __AUTH_CONST.__cfstring: 0x22c20
-  __AUTH_CONST.__objc_const: 0x61b78
+  __AUTH_CONST.__auth_got: 0x2840
+  __AUTH_CONST.__auth_ptr: 0xd8
+  __AUTH_CONST.__const: 0x3368
+  __AUTH_CONST.__cfstring: 0x22c80
+  __AUTH_CONST.__objc_const: 0x5bea8
   __AUTH_CONST.__objc_intobj: 0x45f0
   __AUTH_CONST.__objc_arrayobj: 0x1a58
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x641c
-  __DATA.__data: 0x7490
-  __DATA.__bss: 0xb68
+  __DATA.__objc_ivar: 0x6440
+  __DATA.__data: 0x74b0
+  __DATA.__bss: 0xa68
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0xaeb0
   __DATA_DIRTY.__data: 0x180
-  __DATA_DIRTY.__bss: 0x390
+  __DATA_DIRTY.__bss: 0x490
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 27942
-  Symbols:   32680
-  CStrings:  47496
+  Functions: 28529
+  Symbols:   34762
+  CStrings:  47529
 
Symbols:
+ _VCAbTestThermalLightMitigationsEnabled
+ _objc_release_x9
+ _objc_retain_x26
+ _sRTCReportingSafeViewScreenSharingClientName
+ _sRTCReportingSafeViewSystemAudioSharingClientName
- _fmodf
- _objc_release_x2
- _objc_retain_x28
CStrings:
+ " [%s] %s:%d %@(%p) Choosing to stop capture, streamGroupMode=%u audioIOState=%u"
+ " [%s] %s:%d %@(%p) Skipping configuration because device role and operating mode have NOT changed"
+ " [%s] %s:%d %@(%p) isAnyCameraMediaTypeEnabled=%{BOOL}d operatingMode=%s [%u] oneToOneModeEnabled=%{BOOL}d"
+ " [%s] %s:%d Choosing to stop capture, streamGroupMode=%u audioIOState=%u"
+ " [%s] %s:%d Skipping configuration because device role and operating mode have NOT changed"
+ " [%s] %s:%d SwitchManager: A/B testing turned off - using master local switch: %08X"
+ " [%s] %s:%d isAnyCameraMediaTypeEnabled=%{BOOL}d operatingMode=%s [%u] oneToOneModeEnabled=%{BOOL}d"
+ "-[AVConferencePreview applyTransform:forLayer:]"
+ "-[VCAudioStreamSendGroup stopCaptureForEndToEndStreamIfNeeded]"
+ "-[VCRateControlOWRDEstimator shouldResumeOWRDEstimationWhenOutOfOrderWithTimestamp:isSend:]"
+ "-[VCRateControlOWRDEstimator shouldResumeOWRDEstimationWhenSpuriousLagDetected]"
+ "-[VCVideoCaptureServer setThermalLightMitigationsEnabled:]_block_invoke"
+ "2105.5.1"
+ "AVConferenceOperatingModeAirPlayMirroring"
+ "AVConferenceOperatingModeAppleCalling"
+ "AVConferenceOperatingModeFaceTime"
+ "AVConferenceOperatingModeHomeKit"
+ "AVConferenceOperatingModeMultiway"
+ "AVConferenceOperatingModeRemoteCamera"
+ "AVConferenceOperatingModeRemoteMic"
+ "AVConferenceOperatingModeScreenSharing"
+ "AVConferenceOperatingModeSecondDisplay"
+ "AVConferenceOperatingModeSystemAudioSharing"
+ "AVConferenceOperatingModeTinCan"
+ "AVConferenceOperatingModeWifiCalling"
+ "AVConferencePreview [%s] %s:%d Invalid layer: layer=%p"
+ "B24@0:8I16B20"
+ "EnableThermalLightMitigations"
+ "ProtocolStringEnableThermalLightMitigations"
+ "Ti,R,N,V_operatingMode"
+ "VCRC [%s] %s:%d Lag=%f with receiveDiff=%f and sendDiff=%f looks spurious (shortLag=%f, longLag=%f, threshold=%f), discarding"
+ "VCRC [%s] %s:%d No consecutive out of order with %sTimestamp=%u, previous%sTimestamp=%u, increment oooContinuousRecoveredCount=%d"
+ "VCRC [%s] %s:%d Reset oooContinuousRecoveredCount, since consecutively out of order with %sTimestamp=%u, previous%sTimestamp=%u"
+ "VCRC [%s] %s:%d Spurious lag detected with _sendTimestampSpikeDetected=%d, _sendTimestampSpikeDetected=%d"
+ "VCRC [%s] %s:%d Spurious lag detected without _sendTimestampSpikeDetected=%d, _sendTimestampSpikeDetected=%d, increment _spuriousLagWithoutSpikeCount=%d"
+ "_VCSystemAudioCaptureSession_ResetAudioBufferPool"
+ "_mediaConnectionTimeStartToStartComplete"
+ "_previousOOOReceiveTimestamp"
+ "_previousOOOSendTimestamp"
+ "_receiveTimestampOOORecoveredCount"
+ "_sendTimestampOOORecoveredCount"
+ "_shouldResetAudioBufferPool"
+ "_spuriousLagWithoutSpikeCount"
+ "_thermalLightMitigationsEnabled"
+ "applyTransform:forLayer:"
+ "cStringFromOperatingMode:"
+ "receive"
+ "reportOperatingMode:"
+ "setThermalLightMitigationsEnabled:"
+ "shouldCreateReceiveSideTransmitter"
+ "shouldResumeOWRDEstimationWhenOutOfOrderWithTimestamp:isSend:"
+ "shouldResumeOWRDEstimationWhenSpuriousLagDetected"
+ "v152@0:8{CATransform3D=dddddddddddddddd}16@144"
+ "vc-ab-test-thermal-light-mitigations-enabled"
- " [%s] %s:%d Got unsupported SIMD fetch type %d for packetOffset=%d"
- " [%s] %s:%d SwitchManager: Non-seed build - using master local switch: %08X"
- " [%s] %s:%d Unexpected event in silence state for direction=%d"
- " [%s] %s:%d Unexpected event in speech state in direction=%d"
- "-[VCSystemAudioCaptureSession resetAudioBufferPool]"
- "2100.5.1.1.1"
- "AS"
- "LF"
- "VCAudioReceiver_SendEndCallReport"
- "VCRC [%s] %s:%d Lag=%f with receiveDiff=%f and sendDiff=%f looks spurios (shortLag=%f, longLag=%f, threshold=%f), discarding"
- "_RSU_GatherDecodedDataOneSymbol"
- "_RSU_GatherDecodedDataTwoSymbols"
- "_RSU_ScatterRecoveryDataToSimdFourSymbols"
- "_RSU_ScatterRecoveryDataToSimdOneSymbol"
- "_RSU_ScatterRecoveryDataToSimdTwoSymbols"
- "_RSU_ScatterToCodewordLaneFourSymbols"
- "_RSU_ScatterToCodewordLaneOneSymbol"
- "_RSU_ScatterToCodewordLaneTwoSymbols"
- "_VCAudioIssueDetectorUtil_HandleSilenceStateEvents"
- "_VCAudioIssueDetectorUtil_HandleSpeechStateEvents"
- "resetAudioBufferPool"

```
