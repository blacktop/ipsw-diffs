## CoreSpeechDataAnalytics

> `/System/Library/PrivateFrameworks/CoreSpeechDataAnalytics.framework/CoreSpeechDataAnalytics`

```diff

-3610.11.1.0.0
-  __TEXT.__text: 0x71660
+3610.19.5.0.0
+  __TEXT.__text: 0x73c3c
   __TEXT.__objc_methlist: 0x120
-  __TEXT.__const: 0x2a50
-  __TEXT.__constg_swiftt: 0x26f4
-  __TEXT.__swift5_typeref: 0xf8f
-  __TEXT.__swift5_reflstr: 0x1cb2
-  __TEXT.__swift5_fieldmd: 0x1494
-  __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_assocty: 0x120
-  __TEXT.__oslogstring: 0x3adf
+  __TEXT.__const: 0x2c18
+  __TEXT.__constg_swiftt: 0x27e8
+  __TEXT.__swift5_typeref: 0xfcf
+  __TEXT.__swift5_reflstr: 0x1d8c
+  __TEXT.__swift5_fieldmd: 0x1528
+  __TEXT.__swift5_builtin: 0x17c
+  __TEXT.__swift5_assocty: 0x150
+  __TEXT.__oslogstring: 0x3d3f
   __TEXT.__swift5_capture: 0x1a0
-  __TEXT.__swift5_proto: 0xf4
-  __TEXT.__swift5_types: 0x12c
-  __TEXT.__cstring: 0x4a38
+  __TEXT.__swift5_proto: 0x10c
+  __TEXT.__swift5_types: 0x138
+  __TEXT.__cstring: 0x4eed
   __TEXT.__swift_as_entry: 0xc4
   __TEXT.__swift_as_ret: 0xc4
   __TEXT.__swift_as_cont: 0x180
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x1340
+  __TEXT.__unwind_info: 0x1388
   __TEXT.__eh_frame: 0x2350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x3788
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x658
+  __DATA_CONST.__objc_selrefs: 0x660
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1680
-  __AUTH_CONST.__cfstring: 0x4e00
-  __AUTH_CONST.__objc_const: 0x2e40
-  __AUTH_CONST.__auth_got: 0xc48
+  __AUTH_CONST.__const: 0x1798
+  __AUTH_CONST.__cfstring: 0x5040
+  __AUTH_CONST.__objc_const: 0x2f20
+  __AUTH_CONST.__auth_got: 0xc40
   __AUTH.__objc_data: 0x308
-  __AUTH.__data: 0x1580
+  __AUTH.__data: 0x1648
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x548
-  __DATA.__common: 0xa8
+  __DATA.__data: 0x580
+  __DATA.__common: 0xd8
   __DATA_DIRTY.__objc_data: 0x380
-  __DATA_DIRTY.__data: 0x2db0
+  __DATA_DIRTY.__data: 0x2f30
   __DATA_DIRTY.__common: 0x240
   __DATA_DIRTY.__bss: 0x500
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1198
-  Symbols:   769
-  CStrings:  943
+  Functions: 1223
+  Symbols:   778
+  CStrings:  974
 
Symbols:
+ ___swift_memcpy56_8
+ _associated conformance 23CoreSpeechDataAnalytics18SessionRequestInfoV7VersionOSHAASQ
+ _associated conformance So46ORCHSchemaORCHIFProxyRequestCancellationReasonVSHSCSQ
+ _objc_retain_x9
+ _symbolic _____ 23CoreSpeechDataAnalytics18SessionRequestInfoV7VersionO
+ _symbolic _____ So24ASRSchemaASRCancelReasonV
+ _symbolic _____ So46ORCHSchemaORCHIFProxyRequestCancellationReasonV
+ _symbolic _____Sg So24ASRSchemaASRCancelReasonV
+ _symbolic _____Sg So46ORCHSchemaORCHIFProxyRequestCancellationReasonV
+ _symbolic _____y_____G s11_SetStorageC So46ORCHSchemaORCHIFProxyRequestCancellationReasonV
- ___swift_memcpy40_8
CStrings:
+ "#SiriSessionGenerator: Session %s has no valid voice trigger or manual invocation (button press, gesture) request from a recognized speaker, excluding session"
+ "#SiriSessionGenerator: Session %s is valid with %ld of %ld requests"
+ "#SiriSessionGenerator: asrCancelledReason is not nil: %s"
+ "#SiriSessionGenerator: ifproxy cancelled with %d"
+ "#SiriSessionGenerator: postItn1Best is nil or empty on non-communal device"
+ "#SiriSessionGenerator: request is mitigated"
+ "#SiriSessionGenerator: voice trigger is not SAT triggered on non-communal device"
+ "#SpkrIdSamplingOneSessionPolicy: cannot read selected siri session, keep collection start date: %@"
+ "#SpkrIdSamplingOneSessionPolicy: sampling window ended without a stored session, cleared collection start date"
+ "#SpkrIdSamplingOneSessionPolicy: voice trigger is not enabled, should not sample device"
+ "ASRCANCELREASON_RECOGNITION_CANCELLED"
+ "ASRCANCELREASON_RECOGNITION_REJECTED"
+ "ASRCANCELREASON_UNKNOWN"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_ACOUSTIC_FTM_MITIGATED"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_ADBLOCKER_MITIGATED"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_DEACTIVATION_REQUESTED"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_MYRIAD_LOSS"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_NEW_REQUEST_STARTED"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_REQUEST_CANCELED_FROM_UI"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_REQUEST_CANCELLED"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_REQUEST_DELAGATE_REPLACED_FOR_UNKNOWN_REASON"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_REQUEST_FAILED"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_REQUEST_ROLLBACK"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_REQUEST_TIMEDOUT"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_SESSION_ENDED"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_SPEECH_CANCELED"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_UNKNOWN"
+ "ORCHIFPROXYREQUESTCANCELLATIONREASON_USER_INTERACTION"
+ "asr_cancelled_reason"
+ "btCpVtRequestsCount"
+ "ifproxy_cancelled_reason"
+ "manualInvocationRequestsCount"
+ "otherRequestsCount"
+ "requestInfoVersion"
+ "satVtRequestsCount"
- "#SiriSessionGenerator: Session %s contains invalid requests, excluding entire session"
- "#SiriSessionGenerator: Session %s is valid with %ld requests"
- "#SiriSessionGenerator: invalid invocation source: %s"
- "#SiriSessionGenerator: requestRecord is not SAT trigger on non-communal device"
```
