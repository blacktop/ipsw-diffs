## CMContinuityCaptureCore

> `/System/Library/PrivateFrameworks/CMContinuityCaptureCore.framework/Versions/A/CMContinuityCaptureCore`

```diff

-587.81.10.0.0
-  __TEXT.__text: 0x92000
-  __TEXT.__auth_stubs: 0xd70
-  __TEXT.__objc_methlist: 0x3cbc
-  __TEXT.__const: 0x370
-  __TEXT.__cstring: 0x7554
-  __TEXT.__gcc_except_tab: 0x413c
-  __TEXT.__oslogstring: 0xa1b8
-  __TEXT.__unwind_info: 0x1f20
+587.101.4.0.0
+  __TEXT.__text: 0x9161c
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x4adc
+  __TEXT.__const: 0x318
+  __TEXT.__cstring: 0x75a8
+  __TEXT.__gcc_except_tab: 0x418c
+  __TEXT.__oslogstring: 0xa28e
+  __TEXT.__unwind_info: 0x1fe8
   __TEXT.__objc_classname: 0xc00
-  __TEXT.__objc_methname: 0xb6fd
+  __TEXT.__objc_methname: 0xb7f2
   __TEXT.__objc_methtype: 0x262b
-  __TEXT.__objc_stubs: 0x8880
-  __DATA_CONST.__got: 0x610
-  __DATA_CONST.__const: 0x8a8
+  __TEXT.__objc_stubs: 0x8900
+  __DATA_CONST.__got: 0x620
+  __DATA_CONST.__const: 0x8b8
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2580
+  __DATA_CONST.__objc_selrefs: 0x2780
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0x20a0
-  __AUTH_CONST.__cfstring: 0x45e0
-  __AUTH_CONST.__objc_const: 0xa188
+  __AUTH_CONST.__cfstring: 0x4640
+  __AUTH_CONST.__objc_const: 0x8808
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH.__objc_data: 0xfa0
-  __DATA.__objc_ivar: 0x7ac
+  __DATA.__objc_ivar: 0x7b4
   __DATA.__data: 0xd60
   __DATA.__common: 0x60
   __DATA.__bss: 0x160

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F89217FD-6C82-35D4-AF81-36DD0107F0D2
-  Functions: 2139
-  Symbols:   5449
-  CStrings:  4397
+  UUID: B32C0A6C-547A-3365-AD70-2E15283029B8
+  Functions: 2214
+  Symbols:   5536
+  CStrings:  4417
 
Symbols:
+ +[CMContinuityCaptureAudioInputProvider sharedInstance].cold.1
+ +[CMContinuityCaptureAudioXPCHelper helper].cold.1
+ +[CMContinuityCaptureDeviceBase keepRemoteClientAliveForEvent:].cold.1
+ +[CMContinuityCaptureDiscoverySession sharedInstance].cold.1
+ +[CMContinuityCaptureFrameLatencyMetrics _metricsQueue].cold.1
+ +[CMContinuityCaptureSessionStateManager sharedInstance].cold.1
+ +[CMContinuityCaptureSystemStatus sharedInstance].cold.1
+ +[CMContinuityCaptureUserNotificationCenter sharedInstance].cold.1
+ +[CMContinuityCaptureUserOnboarding sharedInstance].cold.1
+ +[CMContinuityCaptureXPCClientCCA sharedInstance].cold.1
+ +[CMContinuityCaptureXPCServerCCA sharedInstance].cold.1
+ -[CMContinuityCaptureAudioDevice initWithCapabilities:publishDevice:compositeDelegate:].cold.1
+ -[CMContinuityCaptureAudioDevice initWithCapabilities:publishDevice:compositeDelegate:].cold.2
+ -[CMContinuityCaptureConfiguration reactionEffectSuppressedGesturesEnabled]
+ -[CMContinuityCaptureConfiguration setReactionEffectSuppressedGesturesEnabled:]
+ -[CMContinuityCaptureDeskcamVideoDevice _handleForcefulCenterStageEnablementIfNeeded].cold.1
+ -[CMContinuityCaptureDeskcamVideoDevice initWithCapabilities:compositeDelegate:].cold.1
+ -[CMContinuityCaptureMetricsReporter sessionUUID]
+ -[CMContinuityCaptureMetricsReporter setSessionUUID:]
+ -[CMContinuityCaptureProvider createCompositeDeviceWithTransportDevice:].cold.1
+ -[CMContinuityCaptureSystemStatus setupExternalDisplayListener].cold.1
+ -[CMContinuityCaptureUserOnboarding _reportClientState:forClient:].cold.1
+ -[CMContinuityCaptureUserOnboarding _reportClientState:forClient:].cold.2
+ -[CMContinuityCaptureUserOnboarding _reportClientState:forClient:].cold.3
+ -[CMContinuityCaptureUserOnboarding updateState].cold.1
+ -[CMContinuityCaptureUserOnboarding updateState].cold.2
+ -[CMContinuityCaptureVideoDevice _handleForcefulCenterStageEnablementIfNeeded].cold.1
+ -[CMContinuityCaptureVideoDevice populateDefaultManualFramingAndCenterStageValuesWithDeviceID:transportDevice:].cold.1
+ -[CVPixelBufferCoder initWithCoder:].cold.1
+ CMContinityCaptureDebugLogEnabled.cold.1
+ CMContinuityCaptureDevicePosition.cold.1
+ CMContinuityCaptureGetActivateGenerationID.cold.1
+ CMContinuityCaptureGetHostTimeInNanoSec.cold.1
+ CMContinuityCaptureGetMessageGenerationID.cold.1
+ CMContinuityCaptureGetStreamSessionGenerationID.cold.1
+ CMContinuityCaptureLagunaEnabled.cold.1
+ CMContinuityCaptureLog.cold.1
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table169
+ GCC_except_table170
+ GCC_except_table171
+ OBJC_IVAR_$_CMContinuityCaptureConfiguration._reactionEffectSuppressedGesturesEnabled
+ OBJC_IVAR_$_CMContinuityCaptureMetricsReporter._sessionUUID
+ _CMContinuityCaptureControlNameSuppressedGesture
+ _CMContinuityCaptureControlNameSuppressedGesturesEnabled
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ ___53-[CMContinuityCaptureMetricsReporter setSessionUUID:]_block_invoke
+ __block_literal_global.274
+ _bzero
+ _kAVCMediaStreamOptionClientSessionID
+ _kRTCReportingSessionInfoSamplingUUIID
+ _objc_msgSend$UUID
+ _objc_msgSend$reactionEffectSuppressedGesturesEnabled
+ _objc_msgSend$sessionUUID
+ _objc_msgSend$setReactionEffectSuppressedGesturesEnabled:
+ ccmr_generateUniqueID.cold.1
- +[CMContinuityCaptureUserOnboarding validContinuityCameraDeviceToOnboard:].cold.1
- -[CMContinuityCaptureAudioDevice createAVCAudioStream].cold.1
- -[CMContinuityCaptureAudioDevice startAVConferenceStack:].cold.1
- -[CMContinuityCaptureAudioDevice startAVConferenceStack:].cold.2
- -[CMContinuityCaptureCMIOVideoDevice initWithCaptureDevice:].cold.1
- -[CMContinuityCaptureCMIOVideoDevice initWithCaptureDevice:].cold.2
- -[CMContinuityCaptureCMIOVideoDevice setupStreamsWithDeviceID:].cold.1
- -[CMContinuityCaptureCMIOVideoDevice setupStreamsWithDeviceID:].cold.2
- -[CMContinuityCaptureCompositeDevice handleRemoteSystemNotificationControl:].cold.1
- -[CMContinuityCaptureSidecarClient initWithDevice:queue:taskDelegate:].cold.1
- -[CMContinuityCaptureStreamFormat initWithName:width:height:pixelFormat:minFrameRate:maxFrameRate:entity:minimumSupportedVersion:].cold.1
- -[CMContinuityCaptureSystemStatus setupPowerStateListener].cold.1
- -[CMContinuityCaptureVideoDevice createAVCVideoStream].cold.1
- -[CMContinuityCaptureVideoDevice createBlurredSampleBuffer].cold.1
- -[CMContinuityCaptureVideoDevice createBlurredSampleBuffer].cold.2
- -[CMContinuityCaptureVideoDevice createBlurredSampleBuffer].cold.3
- -[CMContinuityCaptureVideoDevice createBlurredSampleBuffer].cold.4
- -[CMContinuityCaptureVideoDevice createBlurredSampleBuffer].cold.5
- -[CMContinuityCaptureVideoDevice createBlurredSampleBuffer].cold.6
- -[CMContinuityCaptureVideoDevice createBlurredSampleBuffer].cold.7
- -[CMContinuityCaptureVideoDevice initWithCapabilities:compositeDelegate:].cold.1
- -[CMContinuityCaptureVideoDevice newVideoStreamCurrentConfiguration].cold.1
- -[CMContinuityCaptureVideoDevice newVideoStreamCurrentConfiguration].cold.2
- -[CMContinuityCaptureVideoDevice startAVConferenceStack:].cold.1
- -[CMContinuityCaptureVideoDevice startAVConferenceStack:].cold.2
- -[CMContinuityCaptureVideoStream _streamPropertiesForProperties:error:].cold.1
- -[CMContinuityCaptureVideoStream initWithDevice:streamFormats:deviceID:queue:].cold.1
- -[CMContinuityCaptureVideoStream initWithDevice:streamFormats:deviceID:queue:].cold.2
- __block_literal_global.267
CStrings:
+ "%{public}@ ReactionEffectSuppressedGesturesEnabled %d"
+ "%{public}@ SuppressedGesture %@"
+ "Filtered out unsupported control %@"
+ "Filtered out unsupported manual framing format %@"
+ "Filtered out unsupported stream format %@"
+ "SuppressedGesture"
+ "SuppressedGesturesEnabled"
+ "T@\"NSUUID\",&,N,V_sessionUUID"
+ "TB,V_reactionEffectSuppressedGesturesEnabled"
+ "UUID"
+ "_reactionEffectSuppressedGesturesEnabled"
+ "_sessionUUID"
+ "reactionEffectSuppressedGesturesEnabled"
+ "sessionUUID"
+ "setReactionEffectSuppressedGesturesEnabled:"
+ "setSessionUUID:"

```
