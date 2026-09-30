## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3401.1.1.1.1
-  __TEXT.__text: 0x156ed0
-  __TEXT.__auth_stubs: 0x1c10
-  __TEXT.__objc_methlist: 0x130e8
+3401.9.2.0.0
+  __TEXT.__text: 0x1575a0
+  __TEXT.__auth_stubs: 0x1c20
+  __TEXT.__objc_methlist: 0x13170
   __TEXT.__const: 0x5c0
   __TEXT.__gcc_except_tab: 0x3754
-  __TEXT.__cstring: 0x27012
-  __TEXT.__oslogstring: 0x1f516
+  __TEXT.__cstring: 0x270d1
+  __TEXT.__oslogstring: 0x1f669
   __TEXT.__dlopen_cstrs: 0x197
-  __TEXT.__unwind_info: 0x4ec0
+  __TEXT.__unwind_info: 0x4ed0
   __TEXT.__objc_classname: 0x2f3f
-  __TEXT.__objc_methname: 0x37d37
-  __TEXT.__objc_methtype: 0x7c70
-  __TEXT.__objc_stubs: 0x1be00
+  __TEXT.__objc_methname: 0x37e6d
+  __TEXT.__objc_methtype: 0x7c85
+  __TEXT.__objc_stubs: 0x1bee0
   __DATA_CONST.__got: 0x1a80
-  __DATA_CONST.__const: 0x40e0
+  __DATA_CONST.__const: 0x4108
   __DATA_CONST.__objc_classlist: 0x858
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x4a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa620
+  __DATA_CONST.__objc_selrefs: 0xa658
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x438
-  __AUTH_CONST.__auth_got: 0xe20
+  __AUTH_CONST.__auth_got: 0xe28
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1e00
-  __AUTH_CONST.__cfstring: 0x8f40
-  __AUTH_CONST.__objc_const: 0x25628
+  __AUTH_CONST.__cfstring: 0x8f60
+  __AUTH_CONST.__objc_const: 0x256e8
   __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_floatobj: 0x4c0
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x3f70
-  __DATA.__objc_ivar: 0x1a64
+  __DATA.__objc_ivar: 0x1a74
   __DATA.__data: 0x3710
-  __DATA.__bss: 0x678
+  __DATA.__bss: 0x670
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x1400
+  __DATA_DIRTY.__objc_data: 0x5370
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x180
+  __DATA_DIRTY.__bss: 0x188
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8271
-  Symbols:   10056
-  CStrings:  14462
+  Functions: 8285
+  Symbols:   10072
+  CStrings:  14477
 
Symbols:
+ _AFBTProductIDSupportsAnnounce
+ __decimationFractional
CStrings:
+ "%!s(MISSING) CSVoiceTriggerSecondPass[%!{(MISSING)public}@]:Skip increasing _numAnalyzedSamples since Exclave didn't process audio chunk"
+ "%!s(MISSING) State feedback is enabled and this is Gibraltar VoiceTrigger, using CVT for two shot"
+ "%!s(MISSING) _userSpeakingStartedTimeInMs %!{(MISSING)public}f, _userSpeakingEndedTimeInMs: %!{(MISSING)public}f, _userSpeakingStartedHostTime: %!{(MISSING)public}llu, _userSpeakingEndedHostTime: %!{(MISSING)public}llu, _stopRecordingHostTime: %!{(MISSING)public}llu, _endpointBufferHostTime: %!{(MISSING)public}llu, _endpointHostTime: %!{(MISSING)public}llu, _audioDeliveryHostTimeDelta: %!{(MISSING)public}llu"
+ "-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_4"
+ "-[CSMyriadPHash generatePHashFromExclaveVoiceTriggerInfo:writeFile:]"
+ "-[CSSpeechManager _setAssetForBuiltInVoiceTrigger:completion:]_block_invoke_4"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]_block_invoke"
+ "@152@0:8d16Q24@32q40@48@56d64@72@80@88B96@100d108d116Q124B132Q136Q144"
+ "C24@0:8d16"
+ "KeyLog - %!s(MISSING) EPD (ms): %!{(MISSING)public}f, EPD_Model (ms): %!{(MISSING)public}f, EPD_Latency (ms): %!{(MISSING)public}f, EPD_V2 (ms): %!{(MISSING)public}f, EPD_Latency_V2 (ms): %!{(MISSING)public}f"
+ "TQ,N,V_audioDeliveryHostTimeDelta"
+ "_audioDeliveryHostTimeDelta"
+ "_doesRecordRouteSupportZLL:"
+ "_emitEndpointDelayMessage:epdModel:speakingStart:speakingEnd:epdV2:"
+ "audioDeliveryHostTimeDelta"
+ "ay12!Rc"
+ "com.apple.MobileAsset.SpeakerRecognitionASMacAssets"
+ "fetchHypotheticalBluetoothRouteProductIdFromAudioSessionId:"
+ "initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:osdFeatures:asrFeatures:isRequestTimeOut:assetConfigVersion:blkHepAudioOrigin:vtExtraAudioAtStartInMs:firstAudioSampleSensorTimestamp:isAnchorTimeBuffered:endpointHostTime:audioDeliveryHostTimeDelta:"
+ "logAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:audioDeliveryHostTimeDelta:"
+ "setAudioDeliveryHostTimeDelta:"
+ "setEndpointDelayInNsV2:"
+ "sigFrac:"
+ "sigNorm:"
+ "v44@0:8Q16Q24B32Q36"
+ "v56@0:8d16d24d32d40d48"
+ "\xa3"
- "%!s(MISSING) _userSpeakingStartedTimeInMs %!{(MISSING)public}f, _userSpeakingEndedTimeInMs: %!{(MISSING)public}f, _userSpeakingStartedHostTime: %!{(MISSING)public}llu, _userSpeakingEndedHostTime: %!{(MISSING)public}llu, _stopRecordingHostTime: %!{(MISSING)public}llu, _endpointBufferHostTime: %!{(MISSING)public}llu"
- "-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_3"
- "-[CSSpeechManager _setAssetForBuiltInVoiceTrigger:completion:]_block_invoke_3"
- "@144@0:8d16Q24@32q40@48@56d64@72@80@88B96@100d108d116Q124B132Q136"
- "KeyLog - %!s(MISSING) EPD (ms): %!{(MISSING)public}f, EPD_Model (ms): %!{(MISSING)public}f, EPD_Latency (ms): %!{(MISSING)public}f"
- "_emitEndpointDelayMessage:epdModel:speakingStart:speakingEnd:"
- "ay12!RS"
- "initWithTotalAudioRecorded:endpointBufferHostTime:featuresAtEndpoint:endpointerType:asrFeatureLatencyDistribution:additionalMetrics:trailingSilenceDurationAtEndpoint:requestId:osdFeatures:asrFeatures:isRequestTimeOut:assetConfigVersion:blkHepAudioOrigin:vtExtraAudioAtStartInMs:firstAudioSampleSensorTimestamp:isAnchorTimeBuffered:endpointHostTime:"
- "logAnchorMachAbsTime:numSamplesProcessedBeforeAnchorTime:isAnchorTimeBuffered:"
- "v36@0:8Q16Q24B32"
- "v48@0:8d16d24d32d40"
- "\x83"

```
