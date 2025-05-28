## AIMLInstrumentationStreams

> `/System/Library/PrivateFrameworks/AIMLInstrumentationStreams.framework/AIMLInstrumentationStreams`

```diff

-3302.8.1.0.0
-  __TEXT.__text: 0x4f804
-  __TEXT.__auth_stubs: 0x14e0
+3303.9.1.0.0
+  __TEXT.__text: 0x58668
+  __TEXT.__auth_stubs: 0x1500
   __TEXT.__objc_methlist: 0x53c
-  __TEXT.__const: 0x22ec
-  __TEXT.__cstring: 0x393e
-  __TEXT.__constg_swiftt: 0x1480
-  __TEXT.__swift5_typeref: 0xece
-  __TEXT.__swift5_reflstr: 0x620
-  __TEXT.__swift5_fieldmd: 0x748
+  __TEXT.__const: 0x237c
+  __TEXT.__cstring: 0x441e
+  __TEXT.__constg_swiftt: 0x14c0
+  __TEXT.__swift5_typeref: 0xf3a
+  __TEXT.__swift5_reflstr: 0x650
+  __TEXT.__swift5_fieldmd: 0x77c
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_proto: 0x1a8
-  __TEXT.__swift5_types: 0xf0
+  __TEXT.__swift5_proto: 0x1ac
+  __TEXT.__swift5_types: 0xf4
   __TEXT.__swift5_assocty: 0xb8
   __TEXT.__swift5_capture: 0x194
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x1108
-  __TEXT.__eh_frame: 0x1f98
+  __TEXT.__unwind_info: 0x1830
+  __TEXT.__eh_frame: 0x2558
   __TEXT.__objc_classname: 0x64
-  __TEXT.__objc_methname: 0xc6b
+  __TEXT.__objc_methname: 0xcd4
   __TEXT.__objc_methtype: 0x3cc
-  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x19c8
-  __DATA_CONST.__objc_selrefs: 0x390
+  __DATA_CONST.__objc_const: 0x19c0
+  __DATA_CONST.__objc_selrefs: 0x3e0
   __AUTH_CONST.__objc_const: 0x228
-  __AUTH_CONST.__const: 0x1cf8
-  __AUTH_CONST.__auth_ptr: 0xd8
-  __AUTH_CONST.__auth_got: 0xa70
-  __AUTH.__data: 0xbf0
-  __AUTH.__objc_data: 0xfb8
+  __AUTH_CONST.__const: 0x1dd0
+  __AUTH_CONST.__auth_ptr: 0x108
+  __AUTH_CONST.__auth_got: 0xa80
+  __AUTH.__data: 0xc10
+  __AUTH.__objc_data: 0x1008
   __DATA.__objc_protorefs: 0x30
-  __DATA.__objc_classrefs: 0xd8
-  __DATA.__data: 0x10f8
-  __DATA.__bss: 0x1400
-  __DATA.__common: 0x78
+  __DATA.__objc_classrefs: 0x178
+  __DATA.__data: 0x12f0
+  __DATA.__bss: 0x1480
+  __DATA.__common: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1556
-  Symbols:   691
-  CStrings:  632
+  Functions: 1682
+  Symbols:   717
+  CStrings:  666
 
Symbols:
+ _OBJC_CLASS_$_ASRSchemaASRAssetLoadContext
+ _OBJC_CLASS_$_ASRSchemaASRFinalAudioPacketContainingSpeechReceived
+ _OBJC_CLASS_$_ASRSchemaASRInitializationContext
+ _OBJC_CLASS_$_ASRSchemaASRPackageGenerated
+ _OBJC_CLASS_$_FLOWSchemaFLOWClientEvent
+ _OBJC_CLASS_$_FLOWSchemaFLOWStep
+ _OBJC_CLASS_$_MHSchemaMHClientEvent
+ _OBJC_CLASS_$_MHSchemaMHSpeechStopDetected
+ _OBJC_CLASS_$_MHSchemaMHUserSpeakingContext
+ _OBJC_CLASS_$_ORCHSchemaORCHExecutionBridgeContext
+ _OBJC_CLASS_$_ORCHSchemaORCHResultCandidateReceived
+ _OBJC_CLASS_$_ORCHSchemaORCHServerFallbackContext
+ _OBJC_CLASS_$_ORCHSchemaORCHTRPCandidateReceived
+ _OBJC_CLASS_$_ORCHSchemaORCHTRPFinalized
+ _OBJC_CLASS_$_SISchemaAudioFirstBufferRecorded
+ _OBJC_CLASS_$_SISchemaAudioStopRecordingStarted
+ _OBJC_CLASS_$_SISchemaTextToSpeechBegin
+ _OBJC_CLASS_$_SISchemaUEILaunchContext
+ _OBJC_CLASS_$_SISchemaUEIUUFRReady
+ _OBJC_CLASS_$_SISchemaUUFRShown
+ _symbolic SS6errstr_t
+ _symbolic _____ 26AIMLInstrumentationStreams9RawStreamC0cD11AccessErrorO
+ _symbolic _____Sg 13SiriAnalytics16SandboxExtensionC
+ _symbolic _____Sg 19SiriInstrumentation12OrderedEventC
+ _symbolic _____ySo21MHSchemaMHClientEventCG 26AIMLInstrumentationStreams14ComponentGroupC
+ _symbolic _____ySo25FLOWSchemaFLOWClientEventCG 26AIMLInstrumentationStreams14ComponentGroupC
CStrings:
+ "ASR Asset Initialize Time is the time between ASRInitializationContext.startedOrChanged and ASRInitializationContext.ended."
+ "ASR Asset Load Time is the time between ASRAssetLoadContext.startedOrChanged and ASRAssetLoadContext.ended."
+ "Audio Stop Time is the time between AudioStopRecordingStarted until RC is selected."
+ "Eager Speech Ready time is the time between the eventually-selected Result Candidate is received until AudioStopRecording."
+ "For Medoc platforms, ASR Audio Lag is the time between MHSchemaMHUserSpeakingContext.ended and ASRFinalAudioPacketContainingSpeechReceived."
+ "For Medoc platforms, ASR Time is the time between MHSchemaMHUserSpeakingContext.ended and ORCHTRPCandidateReceived."
+ "For Medoc platforms, Endpoint Delay is the time between MHSchemaMHUserSpeakingContext.ended and MHSpeechStopDetected. The MHSchemaMHUserSpeakingContext matches the TRPID of the ORCHTRPFinalizedEvent."
+ "For Medoc platforms, Execution Time is the time between max(MHSpeechStopDetected,ORCHExecutionBridgeContext) and UEIUUFRReady."
+ "For Medoc platforms, NLX Time is the time between CDMRequestContextEvent.startedOrChanged and CDMRequestContextEvent.ended."
+ "For Medoc platforms, Server Fallback Time is the time between ORCHServerFallbackInitiated and either ORCHServerFallbackResponseReceived or ORCHServerFallbackFailed."
+ "For Medoc platforms, Siri Response Time is the time between MHSchemaMHUserSpeakingContext.ended and UUFR Ready. The MHSchemaMHUserSpeakingContext matches the TRPID of the ORCHTRPFinalizedEvent."
+ "For Medoc platforms, Useful User Facing Result is the time between MHSpeechStopDetected and UUFR Ready. In cases where the UUFRReady message is not available, the FLOWStep event with flowStateType 'UUFRREADY_DOMAIN' is used to calculate UUFR."
+ "For Medoc platforms, User Speech is the time between AudioFirstBufferRecorded and MHSchemaMHUserSpeakingContext.ended. For non-medoc platforms, User Speech is the time between AudioFirstBufferRecorded and UserStopSpeaking."
+ "Launch is the time between launch start and complete."
+ "Missing Start and End"
+ "Result Selection Time is the time between the eventually-selected Result Candidate is received and the selected result."
+ "Successful Calculation"
+ "TTS Wait is the time between UUFR Ready and TTS Begin. In cases where the UUFRReady message is not available, the FLOWStep event with flowStateType 'UUFRREADY_DOMAIN' is used to calculate TTS Wait."
+ "UI Rendering is the time between UI Rendering start and end."
+ "Unable to establish stream with Raw SiriAnalytics"
+ "Unable to establish stream with SiriAnalytics"
+ "ended"
+ "failed"
+ "failureExplanation"
+ "flowState"
+ "flowStateType"
+ "flowStep"
+ "isFinal"
+ "requestId"
+ "sandboxToken"
+ "serverFallbackTime"
+ "startedOrChanged"
+ "trpId"

```
