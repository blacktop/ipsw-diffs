## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3401.1.1.1.1
-  __TEXT.__text: 0x170e04
-  __TEXT.__auth_stubs: 0x1740
-  __TEXT.__objc_stubs: 0x1e200
-  __TEXT.__objc_methlist: 0x16da8
+3401.9.2.0.0
+  __TEXT.__text: 0x171940
+  __TEXT.__auth_stubs: 0x1750
+  __TEXT.__objc_stubs: 0x1e2e0
+  __TEXT.__objc_methlist: 0x16e80
   __TEXT.__const: 0x338
   __TEXT.__gcc_except_tab: 0x38c0
-  __TEXT.__cstring: 0x2a419
-  __TEXT.__objc_methname: 0x3de5f
-  __TEXT.__oslogstring: 0x2153c
+  __TEXT.__cstring: 0x2a4d9
+  __TEXT.__objc_methname: 0x3e029
+  __TEXT.__oslogstring: 0x21769
   __TEXT.__objc_classname: 0x35c7
-  __TEXT.__objc_methtype: 0x86c0
+  __TEXT.__objc_methtype: 0x86db
   __TEXT.__dlopen_cstrs: 0x2c5
   __TEXT.__info_plist: 0x41f
-  __TEXT.__unwind_info: 0x5600
-  __DATA_CONST.__auth_got: 0xbb8
-  __DATA_CONST.__got: 0x1388
+  __TEXT.__unwind_info: 0x5620
+  __DATA_CONST.__auth_got: 0xbc0
+  __DATA_CONST.__got: 0x1398
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x5c70
-  __DATA_CONST.__cfstring: 0x8380
+  __DATA_CONST.__const: 0x5c98
+  __DATA_CONST.__cfstring: 0x83a0
   __DATA_CONST.__objc_classlist: 0x990
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x4f8

   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_floatobj: 0x4b0
-  __DATA.__objc_const: 0x2c318
-  __DATA.__objc_selrefs: 0xb560
-  __DATA.__objc_ivar: 0x1efc
+  __DATA.__objc_const: 0x2c418
+  __DATA.__objc_selrefs: 0xb5b0
+  __DATA.__objc_ivar: 0x1f10
   __DATA.__objc_data: 0x5fa0
   __DATA.__data: 0x3ba0
   __DATA.__bss: 0x808

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9602
-  Symbols:   1014
-  CStrings:  15644
+  Functions: 9625
+  Symbols:   1017
+  CStrings:  15666
 
Symbols:
+ _AFBTProductIDSupportsAnnounce
+ _OBJC_CLASS_$_CESRUtilities
+ _kCSDiagnosticReporterIntuitiveConvTandemStreamDidNotReceiveAudio
CStrings:
+ "%!s(MISSING) CSVoiceTriggerSecondPass[%!{(MISSING)public}@]:Skip increasing _numAnalyzedSamples since Exclave didn't process audio chunk"
+ "%!s(MISSING) Client didStop but audio coordinator didn't ever received audio started, issue attSiriAudioSrcNodeDidStop here to let all nodes hard stop"
+ "%!s(MISSING) Received audio chunk from %!@(MISSING) with hostTime: %!l(MISSING)lu, startSampleCount: %!l(MISSING)lu, numSamples: %!l(MISSING)u, wasBuffered: %!l(MISSING)u, atTime: %!l(MISSING)lu, audioDeliveryHostTimeDelta: %!l(MISSING)lu"
+ "%!s(MISSING) Request is ineligible for sampling. Disabling audio logging."
+ "%!s(MISSING) Request was not selected for sampling. Disabling audio logging."
+ "%!s(MISSING) _userSpeakingStartedTimeInMs %!{(MISSING)public}f, _userSpeakingEndedTimeInMs: %!{(MISSING)public}f, _userSpeakingStartedHostTime: %!{(MISSING)public}llu, _userSpeakingEndedHostTime: %!{(MISSING)public}llu, _stopRecordingHostTime: %!{(MISSING)public}llu, _endpointBufferHostTime: %!{(MISSING)public}llu, _endpointHostTime: %!{(MISSING)public}llu, _audioDeliveryHostTimeDelta: %!{(MISSING)public}llu"
+ "-[CSAttSiriAudioCoordinator _handleClientDidStopIfNeeded]"
+ "-[CSAttSiriAudioCoordinator attSiriAudioSrcNodeDidStartRecording:successfully:error:]_block_invoke"
+ "-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_4"
+ "-[CSMyriadPHash generatePHashFromExclaveVoiceTriggerInfo:writeFile:]"
+ "-[CSSpeechManager _setAssetForBuiltInVoiceTrigger:completion:]_block_invoke_4"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]_block_invoke"
+ "@152@0:8d16Q24@32q40@48@56d64@72@80@88B96@100d108d116Q124B132Q136Q144"
+ "C24@0:8d16"
+ "KeyLog - %!s(MISSING) EPD (ms): %!{(MISSING)public}f, EPD_Model (ms): %!{(MISSING)public}f, EPD_Latency (ms): %!{(MISSING)public}f, EPD_V2 (ms): %!{(MISSING)public}f, EPD_Latency_V2 (ms): %!{(MISSING)public}f"
+ "TB,N,V_hasAudioEverStarted"
+ "TQ,N,V_audioDeliveryHostTimeDelta"
+ "_audioDeliveryHostTimeDelta"
+ "_emitEndpointDelayMessage:epdModel:speakingStart:speakingEnd:epdV2:"
+ "_handleClientDidStopIfNeeded"
+ "_hasAudioEverStarted"
+ "attSiriNode:didUpdateAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:audioDeliveryHostTimeDelta:"
+ "audioDeliveryHostTimeDelta"
+ "ay12!Rc"
+ "com.apple.MobileAsset.SpeakerRecognitionASMacAssets"
+ "fetchHypotheticalBluetoothRouteProductIdFromAudioSessionId:"
+ "hasAudioEverStarted"
+ "initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:osdFeatures:asrFeatures:isRequestTimeOut:assetConfigVersion:blkHepAudioOrigin:vtExtraAudioAtStartInMs:firstAudioSampleSensorTimestamp:isAnchorTimeBuffered:endpointHostTime:audioDeliveryHostTimeDelta:"
+ "isSamplingSupportedForTask:"
+ "logAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:audioDeliveryHostTimeDelta:"
+ "setAudioDeliveryHostTimeDelta:"
+ "setEndpointDelayInNsV2:"
+ "setHasAudioEverStarted:"
+ "sigFrac:"
+ "sigNorm:"
+ "v44@0:8Q16Q24B32Q36"
+ "v52@0:8@\"<CSAttSiriNode>\"16Q24Q32B40Q44"
+ "v52@0:8@16Q24Q32B40Q44"
+ "v56@0:8d16d24d32d40d48"
+ "\xa3"
- "%!s(MISSING) Received audio chunk from %!@(MISSING) with hostTime: %!l(MISSING)lu, startSampleCount: %!l(MISSING)lu, numSamples: %!l(MISSING)u, wasBuffered: %!l(MISSING)u, atTime: %!l(MISSING)lu"
- "%!s(MISSING) _userSpeakingStartedTimeInMs %!{(MISSING)public}f, _userSpeakingEndedTimeInMs: %!{(MISSING)public}f, _userSpeakingStartedHostTime: %!{(MISSING)public}llu, _userSpeakingEndedHostTime: %!{(MISSING)public}llu, _stopRecordingHostTime: %!{(MISSING)public}llu, _endpointBufferHostTime: %!{(MISSING)public}llu"
- "-[CSAttSiriAsrNode _startLocalSpeechRecognizerIfNeeded]_block_invoke_2"
- "-[CSAttSiriSpeechRecognitionNode _startLocalSpeechRecognizerIfNeeded]_block_invoke_2"
- "-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_3"
- "-[CSSpeechManager _setAssetForBuiltInVoiceTrigger:completion:]_block_invoke_3"
- "@144@0:8d16Q24@32q40@48@56d64@72@80@88B96@100d108d116Q124B132Q136"
- "KeyLog - %!s(MISSING) EPD (ms): %!{(MISSING)public}f, EPD_Model (ms): %!{(MISSING)public}f, EPD_Latency (ms): %!{(MISSING)public}f"
- "_emitEndpointDelayMessage:epdModel:speakingStart:speakingEnd:"
- "attSiriNode:didUpdateAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:"
- "ay12!RS"
- "initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:osdFeatures:asrFeatures:isRequestTimeOut:assetConfigVersion:blkHepAudioOrigin:vtExtraAudioAtStartInMs:firstAudioSampleSensorTimestamp:isAnchorTimeBuffered:endpointHostTime:"
- "logAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:"
- "v36@0:8Q16Q24B32"
- "v44@0:8@\"<CSAttSiriNode>\"16Q24Q32B40"
- "v44@0:8@16Q24Q32B40"
- "v48@0:8d16d24d32d40"
- "\x83"

```
