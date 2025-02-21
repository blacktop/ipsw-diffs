## com.apple.siri.analyzer

> `/System/Library/PrivateFrameworks/AssistantServices.framework/XPCServices/com.apple.siri.analyzer.xpc/com.apple.siri.analyzer`

```diff

-3403.5.1.11.1
-  __TEXT.__text: 0x5114
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x394
+3404.68.6.1.1
+  __TEXT.__text: 0x2c1c
+  __TEXT.__auth_stubs: 0x5c0
+  __TEXT.__objc_stubs: 0x520
+  __TEXT.__objc_methlist: 0x98
   __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x1a4
-  __TEXT.__objc_methname: 0xf59
-  __TEXT.__cstring: 0x8d7
-  __TEXT.__oslogstring: 0x5ba
-  __TEXT.__objc_classname: 0x65
-  __TEXT.__objc_methtype: 0x148
-  __TEXT.__unwind_info: 0x1a0
-  __DATA_CONST.__auth_got: 0x360
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x4b0
+  __TEXT.__gcc_except_tab: 0x158
+  __TEXT.__cstring: 0x461
+  __TEXT.__oslogstring: 0x293
+  __TEXT.__objc_classname: 0xb
+  __TEXT.__objc_methname: 0x363
+  __TEXT.__objc_methtype: 0x81
+  __TEXT.__unwind_info: 0x100
+  __DATA_CONST.__auth_got: 0x2f0
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__cfstring: 0x280
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x5e0
-  __DATA.__objc_selrefs: 0x3b8
-  __DATA.__objc_ivar: 0x4c
-  __DATA.__objc_data: 0xf0
-  __DATA.__bss: 0x18
+  __DATA.__objc_const: 0x90
+  __DATA.__objc_selrefs: 0x158
+  __DATA.__objc_data: 0x50
+  __DATA.__bss: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
-  - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics
-  - /usr/lib/libAWDSupportFramework.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 114
-  Symbols:   143
-  CStrings:  296
+  Functions: 33
+  Symbols:   117
+  CStrings:  124
 
Symbols:
+ _objc_release_x28
- _OBJC_CLASS_$_AWDServerConnection
- _OBJC_CLASS_$_AWDSiriNetworkAnalyzerRun
- _OBJC_CLASS_$_AWDSiriServerConnectionFailed
- _OBJC_CLASS_$_AWDSiriServerConnectionOpen
- _OBJC_CLASS_$_AWDSiriServerConnectionStart
- _OBJC_CLASS_$_AWDSiriSpeechRecognized
- _OBJC_CLASS_$_AWDSiriVoiceRecordingEnd
- _OBJC_CLASS_$_AWDSiriVoiceRecordingStart
- _OBJC_CLASS_$_AWDSiriVoiceSendEnd
- _OBJC_CLASS_$_AWDSiriVoiceSendStart
- _OBJC_CLASS_$_SASFinishSpeech
- _OBJC_CLASS_$_SASStartSpeech
- __os_log_error_impl
- _dispatch_once
- _dispatch_queue_attr_make_with_autorelease_frequency
- _dispatch_queue_attr_make_with_qos_class
- _objc_msgSendSuper2
- _objc_opt_new
- _objc_opt_respondsToSelector
- _objc_release_x1
- _objc_release_x26
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x5
- _objc_setProperty_nonatomic_copy
CStrings:
- "\a"
- "\x15\x13"
- "%s "
- "%s Hot-ship metric 0x%lx does not respond to -setTimestamp:. Will not set timestamp."
- "%s Received -logConnectionOpenWithConnectionType: with no corresponding -logConnectionStart. Unable to determine how long it took to open the connection."
- "%s Received -logSpeechRecognized with no corresponding -logVoiceRecordingEnd. Unable to determine duration since voice recording completed."
- "%s Received -logSpeechRecognized with no corresponding -logVoiceSendEnd. Unable to determine duration since voice send completed."
- "%s Received -logVoiceRecordingEnd with no corresponding -logVoiceRecordingStart. Unable to determine how long voice recording lasted."
- "%s Received -logVoiceSendEnd with no corresponding -logVoiceSendStart. Unable to determine how long voice transfer lasted."
- "%s Unable to submit AWD metric 0x%lx"
- "-[AFDiagnostics _submitMetricWithIdentifier:generation:]"
- "-[AFDiagnostics _submitMetricWithIdentifier:hotShipIdentifier:hotShipTimestamp:generation:]_block_invoke"
- "-[AFDiagnostics logConnectionFailedWithError:connectionType:]"
- "-[AFDiagnostics logConnectionOpenWithConnectionType:]"
- "-[AFDiagnostics logConnectionOpenWithConnectionType:]_block_invoke_2"
- "-[AFDiagnostics logConnectionStart]"
- "-[AFDiagnostics logNetworkAnalyzeRunWithResults:]"
- "-[AFDiagnostics logSpeechRecognized]"
- "-[AFDiagnostics logSpeechRecognized]_block_invoke"
- "-[AFDiagnostics logSpeechRecognized]_block_invoke_2"
- "-[AFDiagnostics logVoiceRecordingEnd]"
- "-[AFDiagnostics logVoiceRecordingEnd]_block_invoke_2"
- "-[AFDiagnostics logVoiceRecordingStart]"
- "-[AFDiagnostics logVoiceSendEnd]"
- "-[AFDiagnostics logVoiceSendEnd]_block_invoke_2"
- "-[AFDiagnostics logVoiceSendStart]"
- ".cxx_destruct"
- "@\"AWDServerConnection\""
- "@\"AWDSiriNetworkAnalyzerRun\"8@?0"
- "@\"AWDSiriServerConnectionFailed\"8@?0"
- "@\"AWDSiriServerConnectionOpen\"8@?0"
- "@\"AWDSiriServerConnectionStart\"8@?0"
- "@\"AWDSiriSpeechRecognized\"8@?0"
- "@\"AWDSiriVoiceRecordingEnd\"8@?0"
- "@\"AWDSiriVoiceRecordingStart\"8@?0"
- "@\"AWDSiriVoiceSendEnd\"8@?0"
- "@\"AWDSiriVoiceSendStart\"8@?0"
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@8@?0"
- "AFAdditions"
- "AFDiagnostics"
- "AFDiagnosticsAdditions"
- "AFDiagnosticsNetworkAnalyzerResults"
- "B"
- "B16@0:8"
- "Q16@0:8"
- "Q24@0:8@16"
- "Q32@0:8d16d24"
- "Siri diagnostics queue"
- "T@\"AWDServerConnection\",R,N,G_serverConnection,V_serverConnection"
- "T@\"NSNumber\",&,N,G_connectionStartTime,S_setConnectionStartTime:,V_connectionStartTime"
- "T@\"NSNumber\",&,N,G_voiceRecordingEndTime,S_setVoiceRecordingEndTime:,V_voiceRecordingEndTime"
- "T@\"NSNumber\",&,N,G_voiceRecordingStartTime,S_setVoiceRecordingStartTime:,V_voiceRecordingStartTime"
- "T@\"NSNumber\",&,N,G_voiceSendEndTime,S_setVoiceSendEndTime:,V_voiceSendEndTime"
- "T@\"NSNumber\",&,N,G_voiceSendStartTime,S_setVoiceSendStartTime:,V_voiceSendStartTime"
- "T@\"NSNumber\",C,N,V_connectionInterface"
- "T@\"NSNumber\",C,N,V_gatewayPingDuration"
- "T@\"NSNumber\",C,N,V_gatewayPingsDropped"
- "T@\"NSNumber\",C,N,V_gatewayPingsSent"
- "T@\"NSNumber\",C,N,V_knownURLLoadDuration"
- "T@\"NSNumber\",C,N,V_sendBufferBytesRemaining"
- "T@\"NSNumber\",C,N,V_siriSaltURLLoadDuration"
- "T@\"NSNumber\",C,N,V_siriURLLoadDuration"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,G_queue,V_queue"
- "TB,N,GisForUserRequest,V_forUserRequest"
- "TB,N,V_analyzedSuccessfulRetry"
- "TB,N,V_wwanPreferred"
- "Tq,N,V_gatewayStatus"
- "_AWDTimestampTruncatedToHourPrecision"
- "_analyzedSuccessfulRetry"
- "_connectionInterface"
- "_connectionStartTime"
- "_currentTime"
- "_durationInMillisecondsForDuration:"
- "_durationInMillisecondsFromTime:toTime:"
- "_forUserRequest"
- "_gatewayPingDuration"
- "_gatewayPingsDropped"
- "_gatewayPingsSent"
- "_gatewayStatus"
- "_knownURLLoadDuration"
- "_queue"
- "_sendBufferBytesRemaining"
- "_serverConnection"
- "_setConnectionStartTime:"
- "_setVoiceRecordingEndTime:"
- "_setVoiceRecordingStartTime:"
- "_setVoiceSendEndTime:"
- "_setVoiceSendStartTime:"
- "_siriSaltURLLoadDuration"
- "_siriURLLoadDuration"
- "_submitMetricWithIdentifier:generation:"
- "_submitMetricWithIdentifier:hotShipIdentifier:hotShipTimestamp:generation:"
- "_voiceRecordingEndTime"
- "_voiceRecordingStartTime"
- "_voiceSendEndTime"
- "_voiceSendStartTime"
- "_wwanPreferred"
- "af_logDiagnostics"
- "analyzedSuccessfulRetry"
- "code"
- "connectionInterface"
- "connectionStartTime"
- "d16@0:8"
- "domain"
- "doubleValue"
- "flush"
- "forUserRequest"
- "gatewayPingDuration"
- "gatewayPingsDropped"
- "gatewayPingsSent"
- "gatewayStatus"
- "getAWDTimestamp"
- "init"
- "initWithComponentId:andBlockOnConfiguration:"
- "isForUserRequest"
- "knownURLLoadDuration"
- "logConnectionFailedWithError:connectionType:"
- "logConnectionOpenWithConnectionType:"
- "logConnectionStart"
- "logNetworkAnalyzeRunWithResults:"
- "logSpeechRecognized"
- "logVoiceRecordingEnd"
- "logVoiceRecordingStart"
- "logVoiceSendEnd"
- "logVoiceSendStart"
- "metricValue"
- "newMetricContainerWithIdentifier:"
- "q"
- "q16@0:8"
- "queue"
- "sendBufferBytesRemaining"
- "serverConnection"
- "setAnalyzedSuccessfulRetry:"
- "setAnalyzingSuccessfulRetry:"
- "setConnectionInterface:"
- "setConnectionType:"
- "setDuration:"
- "setDurationFromVoiceRecordingEnd:"
- "setDurationFromVoiceSendEnd:"
- "setErrorCode:"
- "setErrorDomain:"
- "setForUserRequest:"
- "setGatewayPingDuration:"
- "setGatewayPingsDropped:"
- "setGatewayPingsSent:"
- "setGatewayStatus:"
- "setInterface:"
- "setIsUserRequest:"
- "setKnownURLLoadDuration:"
- "setMetric:"
- "setSendBufferBytesRemaining:"
- "setSiriSaltURLLoadDuration:"
- "setSiriURLLoadDuration:"
- "setTimestamp:"
- "setWwanPreferred:"
- "sharedDiagnostics"
- "siriSaltURLLoadDuration"
- "siriURLLoadDuration"
- "submitMetric:"
- "unsignedIntValue"
- "v20@0:8B16"
- "v24@0:8q16"
- "v28@0:8I16@?20"
- "v32@0:8@16q24"
- "v40@0:8I16I20Q24@?32"
- "voiceRecordingEndTime"
- "voiceRecordingStartTime"
- "voiceSendEndTime"
- "voiceSendStartTime"
- "wwanPreferred"

```
