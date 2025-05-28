## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3300.119.1.1.7
-  __TEXT.__text: 0x1b790c
+3301.20.3.0.0
+  __TEXT.__text: 0x1b8a80
   __TEXT.__auth_stubs: 0x1ac0
-  __TEXT.__objc_stubs: 0x227c0
-  __TEXT.__objc_methlist: 0x1ada0
+  __TEXT.__objc_stubs: 0x22900
+  __TEXT.__objc_methlist: 0x1ae38
   __TEXT.__const: 0x250
-  __TEXT.__gcc_except_tab: 0x2f50
-  __TEXT.__cstring: 0x31974
-  __TEXT.__objc_methname: 0x447fe
-  __TEXT.__oslogstring: 0x27229
+  __TEXT.__gcc_except_tab: 0x2f78
+  __TEXT.__cstring: 0x31aaf
+  __TEXT.__objc_methname: 0x44b90
+  __TEXT.__oslogstring: 0x2749f
   __TEXT.__objc_classname: 0x3f0a
-  __TEXT.__objc_methtype: 0x8e44
+  __TEXT.__objc_methtype: 0x8eb0
   __TEXT.__dlopen_cstrs: 0x3c9
-  __TEXT.__unwind_info: 0x67d4
+  __TEXT.__unwind_info: 0x680c
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0xd78
-  __DATA_CONST.__got: 0x738
+  __DATA_CONST.__got: 0x750
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x6a70
-  __DATA_CONST.__cfstring: 0xac40
+  __DATA_CONST.__const: 0x6a98
+  __DATA_CONST.__cfstring: 0xac60
   __DATA_CONST.__objc_classlist: 0xbf0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x548
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0xf60
-  __DATA_CONST.__objc_doubleobj: 0x60
+  __DATA_CONST.__objc_doubleobj: 0x70
   __DATA_CONST.__objc_arraydata: 0x2c0
   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_dictobj: 0x398
   __DATA_CONST.__objc_floatobj: 0x4f0
-  __DATA.__objc_const: 0x58d48
-  __DATA.__objc_selrefs: 0xc938
+  __DATA.__objc_const: 0x58e88
+  __DATA.__objc_selrefs: 0xc9b8
   __DATA.__objc_protorefs: 0xf8
   __DATA.__objc_classrefs: 0x1380
   __DATA.__objc_superrefs: 0x9c8
-  __DATA.__objc_ivar: 0x2334
+  __DATA.__objc_ivar: 0x2344
   __DATA.__objc_data: 0x7760
   __DATA.__data: 0x3f60
   __DATA.__bss: 0xa18

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11292
-  Symbols:   948
-  CStrings:  17944
+  Functions: 11311
+  Symbols:   951
+  CStrings:  17986
 
Symbols:
+ _kCSDiagnosticReporterEndpointDelayNegative
+ _kCSDiagnosticReporterEndpointDelayTooHigh
+ _kCSDiagnosticReporterEndpointerProxyMissingFirstAudioSampleHostTime
CStrings:
+ "%@-%@%@%@"
+ "%s #Boron check FAIL. StartSampleCount: %llu. PrependSamples: %llu. LatestBoronSampleCount: %lld. LastAudioSampleCount: %lld. Diff: %lld Thresh: %lld"
+ "%s #Boron check SUCCESS. StartSampleCount: %llu. PrependSamples: %llu. LatestBoronSampleCount: %lld. LastAudioSampleCount: %lld. Diff: %lld Thresh: %lld"
+ "%s CSBenchmarkXPCListener does not have entitlement"
+ "%s CSJarvisTriggerMode : %@"
+ "%s Calling start audio stream : %@ %@, context: %@"
+ "%s Failed to delete leading utterance log file at: %@ with error:%@"
+ "%s Not reporting EPD due to unexpected zero or negative values: _stopRecordingHostTime: %{public}llu, _userSpeakingEndedHostTime: %{public}llu, _userSpeakingEndedTimeInMs: %{public}f, _endpointTimeInMs: %{public}f"
+ "%s Setting firstAudioSampleSensorHostTime: %llu"
+ "%s Stop received for invalid requestId:%@, currentRequestId:%@"
+ "%s allowZeroInjection : %@"
+ "%s requestId:%@"
+ "%s session in progress:%u"
+ "%s voiceTriggerEnabled : %d, enable AOP mode : %d"
+ "&\x13"
+ "-[CSAttSiriSSRNode handleSiriSessionEnd]_block_invoke"
+ "-[CSAttSiriSSRNode setUpSpeakerProfileForFlexibleFollowup]_block_invoke"
+ "-[CSAudioInjectionProvider startAudioStreamWithOption:recordDeviceIndicator:error:]_block_invoke"
+ "-[CSBuiltInVoiceTrigger _transitAOPModeIfNeeded:]"
+ "-[CSEndpointerProxy _setFirstAudioSampleSensorHostTimeIfNeeded:]"
+ "-[CSIntuitiveConvRequestHandler _handleStopProcessingForRequestId:]"
+ "-[CSModelBenchmarker _onDeviceCompilationWithConfigFile:locale:]"
+ "T@\"NSString\",&,N,V_lastLoggedMhUUID"
+ "TC,N,V_jarvisTriggerModeLogHeartbeat"
+ "TQ,N,V_hearstNumberOfBytesPerChunk"
+ "TQ,N,V_hearstNumberOfSamplesPerChunk"
+ "_emitEndpointDelayMessage:epdModel:speakingStart:speakingEnd:"
+ "_handleStopProcessingForRequestId:"
+ "_hearstNumberOfBytesPerChunk"
+ "_hearstNumberOfSamplesPerChunk"
+ "_jarvisTriggerModeLogHeartbeat"
+ "_lastLoggedMhUUID"
+ "_onDeviceCompilationWithConfigFile:locale:"
+ "_transitAOPModeIfNeeded:"
+ "_transitAOPModeIfNeededAsync:"
+ "_transitAOPModeIfNeededSync:"
+ "agnosticLocale"
+ "generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedNbest:recognizedText:correctedText:selectedAlternatives:completion:"
+ "handleSiriSessionEnd"
+ "isFlexibleFollowupsSupported"
+ "jarvisTriggerModeLogHeartbeat"
+ "lastLoggedMhUUID"
+ "runNCModelWithConfig:completion:"
+ "setHearstNumberOfBytesPerChunk:"
+ "setHearstNumberOfSamplesPerChunk:"
+ "setIsAirpodsConnected:"
+ "setJarvisTriggerModeLogHeartbeat:"
+ "setLastLoggedMhUUID:"
+ "setPrevStageOutput:"
+ "setTimeSinceLastQuery:"
+ "setUpSpeakerProfileForFlexibleFollowup"
+ "silencePosteriorGeneratorProcessorIsFinished:"
+ "v24@0:8@\"EARCaesuraSilencePosteriorGenerator\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v48@0:8d16d24d32d40"
+ "v68@0:8@\"CSAttSiriOSDProvider\"16d24d32d40d48B56q60"
+ "v68@0:8@\"CSAttSiriSignalProvider\"16d24d32d40d48B56q60"
+ "v68@0:8@16d24d32d40d48B56q60"
- "%@%@%@%@"
- "%s #Boron check FAIL. StartSampleCount: %llu. PrependSamples: %llu. LatestBoronSampleCount: %llu. Diff: %lld Thresh: %lld"
- "%s #Boron check SUCCESS. StartSampleCount: %llu. PrependSamples: %llu. LatestBoronSampleCount: %llu. Diff: %lld Thresh: %lld"
- "%s CSBenchmarkXPCListener here"
- "%s Calling start audio stream : %@ %@"
- "&\x12"
- "-[CSBuiltInVoiceTrigger _transitAOPMode:]"
- "-[CSIntuitiveConvRequestHandler _handleStopProcessing]"
- "-[CSModelBenchmarker _onDeviceCompilationWithConfigFile:modelType:locale:]"
- "_onDeviceCompilationWithConfigFile:modelType:locale:"
- "_transitAOPMode:"
- "_transitAOPModeAsync:"
- "_transitAOPModeSync:"
- "v68@0:8@\"CSAttSiriOSDProvider\"16d24d32d40d48B56Q60"
- "v68@0:8@\"CSAttSiriSignalProvider\"16d24d32d40d48B56Q60"
- "v68@0:8@16d24d32d40d48B56Q60"

```
