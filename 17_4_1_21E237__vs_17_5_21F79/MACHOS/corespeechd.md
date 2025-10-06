## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-3304.82.8.1.2
-  __TEXT.__text: 0x187c30
-  __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_stubs: 0x1f680
-  __TEXT.__objc_methlist: 0x18720
-  __TEXT.__const: 0x258
-  __TEXT.__gcc_except_tab: 0x29c8
-  __TEXT.__cstring: 0x2db4e
-  __TEXT.__objc_methname: 0x3fd32
-  __TEXT.__oslogstring: 0x22490
-  __TEXT.__objc_classname: 0x39f1
-  __TEXT.__objc_methtype: 0x8657
+3305.27.1.0.0
+  __TEXT.__text: 0x18ba6c
+  __TEXT.__auth_stubs: 0x1850
+  __TEXT.__objc_stubs: 0x1fcc0
+  __TEXT.__objc_methlist: 0x18b50
+  __TEXT.__const: 0x268
+  __TEXT.__gcc_except_tab: 0x2a5c
+  __TEXT.__cstring: 0x2e17d
+  __TEXT.__objc_methname: 0x40bfe
+  __TEXT.__oslogstring: 0x22a62
+  __TEXT.__objc_classname: 0x3a95
+  __TEXT.__objc_methtype: 0x8718
   __TEXT.__dlopen_cstrs: 0x325
-  __TEXT.__unwind_info: 0x5d24
+  __TEXT.__unwind_info: 0x5ddc
   __TEXT.__eh_frame: 0x38
-  __DATA_CONST.__auth_got: 0xc38
-  __DATA_CONST.__got: 0x610
+  __DATA_CONST.__auth_got: 0xc40
+  __DATA_CONST.__got: 0x628
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x6798
-  __DATA_CONST.__cfstring: 0xa0a0
-  __DATA_CONST.__objc_classlist: 0xac8
+  __DATA_CONST.__const: 0x68b0
+  __DATA_CONST.__cfstring: 0xa380
+  __DATA_CONST.__objc_classlist: 0xae0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x500
+  __DATA_CONST.__objc_protolist: 0x508
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_classrefs: 0x12c8
-  __DATA_CONST.__objc_superrefs: 0x8f0
+  __DATA_CONST.__objc_classrefs: 0x12e0
+  __DATA_CONST.__objc_superrefs: 0x908
   __DATA_CONST.__objc_intobj: 0xf30
   __DATA_CONST.__objc_doubleobj: 0x70
   __DATA_CONST.__objc_arraydata: 0x2e8
   __DATA_CONST.__objc_dictobj: 0x320
   __DATA_CONST.__objc_arrayobj: 0x210
   __DATA_CONST.__objc_floatobj: 0x4f0
-  __DATA.__objc_const: 0x53788
-  __DATA.__objc_selrefs: 0xba30
-  __DATA.__objc_ivar: 0x2094
-  __DATA.__objc_data: 0x6bd0
-  __DATA.__data: 0x3c00
-  __DATA.__bss: 0x8d0
+  __DATA.__objc_const: 0x53ed0
+  __DATA.__objc_selrefs: 0xbcc8
+  __DATA.__objc_ivar: 0x2104
+  __DATA.__objc_data: 0x6cc0
+  __DATA.__data: 0x3c60
+  __DATA.__bss: 0x8e0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9AE89B49-D495-3ACC-8B06-922100784985
-  Functions: 10252
-  Symbols:   886
-  CStrings:  17736
+  UUID: C6FC93C9-ED69-3350-BF12-E88F1BD78301
+  Functions: 10350
+  Symbols:   891
+  CStrings:  17967
 
Symbols:
+ _AVAudioSessionCategoryPlayback
+ _AVAudioSessionModeDefault
+ _AudioQueueNewOutput
+ _OBJC_CLASS_$_SSRSpeakerProfileEmbeddingExtractor
+ _kCFRunLoopCommonModes
CStrings:
+ "\x0f\x04"
+ "\x11\""
+ "%s AudioQueue call back is asking for audio, injected file has been found"
+ "%s AudioQueue call back is asking for audio, injected file is not available, injecting digital 1s"
+ "%s CSHybridEndpointer can NOT ProcessCurrentRequest, fallback to NNVAD"
+ "%s CSVoiceTriggerSecondPass[%{public}@]:Not valid firstPass source for Exclave : %{public}lu"
+ "%s Client request to speak audio into exclave with URL: %@ at time: %llu"
+ "%s Directly enable AOP without configuring model"
+ "%s Disable FF since this is Exclave hardware without Siri DSP"
+ "%s Failed to activate audioSession with error: %@"
+ "%s Failed to create Exclave Audio Injection AudioQueue with OSStatus error: %d"
+ "%s Failed to deactivate audioSession with error: %@"
+ "%s Failed to feed audio into exclave, AQ or AQBuffer is invalid"
+ "%s Failed to feed audio into exclave, unable to alloc AudioQueue AudioBuffer with OSStatus: %d"
+ "%s Failed to feed audio into exclave, unable to enqueue AQ buffer with OSStatus: %d"
+ "%s Failed to feed audio into exclave, unable to locate available audio queue"
+ "%s Failed to feed audio into exclave, unable to start AQ buffer with OSStatus: %d"
+ "%s Failed to set audioSession properties with error: %@"
+ "%s File doesn't exist: %{public}@"
+ "%s Ignore %{public}@ since Siri client is current listening"
+ "%s Ignore %{public}@ since Siri client is currently in a connected call"
+ "%s Ignore %{public}@ since Siri client is currently in a ringtone and does not support A2DP"
+ "%s Ignore %{public}@ since Siri client is currently in an outgoing call"
+ "%s Ignore %{public}@ since VoiceTrigger was turned off"
+ "%s New asset is the same as current asset - no update needed."
+ "%s Not a ReadThis or voiceOver audioSession - bail out!"
+ "%s PSR Profile Embedding extract : %d * %d with error %@"
+ "%s PSR Profile embedding is nil, not sending embedding to Exclave"
+ "%s Request timeout with features %{public}@"
+ "%s SAT Profile Embedding extract : %d * %d  with error %@"
+ "%s SAT Profile embedding is nil, not sending embedding to Exclave"
+ "%s SecureSpeakerRecognitionConfig string %s"
+ "%s Successfully activate audioSession"
+ "%s Successfully deactivate audioSession"
+ "%s Successfully start the audio queue"
+ "%s Unable to alloc AudioQueue AudioBuffer with OSStatus: %d"
+ "%s Updating current asset."
+ "%s attendingStateStart:(%u) readThisOrVoiceOverSessionActive:(%u) aggressiveECParamsApplied:(%u) inAttendingWindow:(%u)"
+ "%s audio session info is nil - bail out!"
+ "%s goodness = %d, confidence = %d absTime = %llu, frac = %d"
+ "%s injection is ended at time: %llu"
+ "%s isReadThisAudioSession:(%u), isVoiceOver:(%u)"
+ "%s locale=%@"
+ "%s readThisOrVoiceOverSessionActive:(%u) aggressiveEchoCancellationApplied:(%u) inAttendingWindow:(%u)"
+ "%s starting the injection provider for exclave"
+ "%s trigger-length : %{public}llu"
+ "-[CSAudioInjectionProviderExclave _createAudioQueueIfNeeded]"
+ "-[CSAudioInjectionProviderExclave _defaultBufferRef]"
+ "-[CSAudioInjectionProviderExclave _prepareAndStartAudioQueue]"
+ "-[CSAudioInjectionProviderExclave _readAudioBufferAndFeedIntoAudioQueue]_block_invoke"
+ "-[CSAudioInjectionProviderExclave _setAudioSessionActive:]"
+ "-[CSAudioInjectionProviderExclave speakAudioInExclave:withCompletion:]_block_invoke"
+ "-[CSAudioInjectionXPC init]"
+ "-[CSBuiltInVoiceTrigger activationEventNotificationHandler:event:completion:]_block_invoke"
+ "-[CSBuiltInVoiceTrigger updateExclaveKitSiriLocale:]_block_invoke"
+ "-[CSHybridEndpointer _updateCurrentAsset:]"
+ "-[CSVoiceTriggerSecondPass _calculateRecordingTimeForAOPTriggerFromFirstPassInfo:completion:]"
+ "-[CSVoiceTriggerSecondPass _syncVoiceProfileEmbeddingsToExclave]_block_invoke"
+ "-[SecureVoiceTriggerSpeakerRecognitionDecoder decodeSecureVoiceTriggerSpeakerRecognitionConfigForAsset:]"
+ "9\x14"
+ "@\"CSAudioInjectionProviderExclave\""
+ "@\"SSRVTUITrainingMessageHandler\""
+ "@28@0:8@16f24"
+ "@88@0:8@16I24f28f32f36f40f44f48f52f56I60B64I68I72I76I80B84"
+ "ApplicationProcessorExclave"
+ "ApplicationProcessorExclaveWithConnectedCall"
+ "ApplicationProcessorExclaveWithRingtone"
+ "B36@0:8@16@24B32"
+ "BuiltInAlwaysOnProcessorExclave"
+ "CSAudioInjectionProviderExclave"
+ "I40@0:8@16@24Q32"
+ "Q\x1b\xc1\x81\x12\x19A"
+ "SSRVTUITrainingAudioSessionDelegate"
+ "SecureSpeakerRecognitionConfigBridge"
+ "SecureSpeakerRecognitionPhraseConfigBridge"
+ "SecureVoiceTriggerSpeakerRecognitionDecoder"
+ "T@\"CSAudioTimeConverter\",&,N,V_exclaveAudioTimeConverter"
+ "T@\"CSPhoneCallStateMonitor\",&,N,V_phoneCallStateMonitor"
+ "T@\"CSVoiceTriggerEnabledMonitor\",&,N,V_voiceTriggerEnabledMonitor"
+ "T@\"NSArray\",C,N,V_phraseConfigs"
+ "T@\"NSString\",C,N,V_name"
+ "T@\"SSRVTUITrainingMessageHandler\",&,N,V_trainingMessageHandler"
+ "T@?,C,N,V_injectionCompletion"
+ "TB,N,V_didForceEndpoint"
+ "TB,N,V_implicitTrainingEnabled"
+ "TB,N,V_isAudioQueueStarted"
+ "TB,N,V_readThisOrVoiceOverSessionActive"
+ "TB,N,V_useTDTIEnrollment"
+ "TI,N,V_maxEnrollmentUtterances"
+ "TI,N,V_multiUserConfidentScoreThreshold"
+ "TI,N,V_multiUserDeltaScoreThreshold"
+ "TI,N,V_multiUserHighScoreThreshold"
+ "TI,N,V_multiUserLowScoreThreshold"
+ "TI,N,V_numPruningRetentionUtt"
+ "TQ,N,V_injectionEndTime"
+ "TQ,N,V_injectionStartTime"
+ "T^{OpaqueAudioQueue=},N,V_exclaveAudioQueue"
+ "Tf,N,V_combinationWeight"
+ "Tf,N,V_implicitProfileDeltaThreshold"
+ "Tf,N,V_implicitProfileThreshold"
+ "Tf,N,V_implicitVTThreshold"
+ "Tf,N,V_pruningExplicitPSRThreshold"
+ "Tf,N,V_pruningExplicitSATThreshold"
+ "Tf,N,V_pruningPSRThreshold"
+ "Tf,N,V_pruningSATThreshold"
+ "Tf,N,V_satThreshold"
+ "Tq,N,V_echoCancellationReason"
+ "^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16@0:8"
+ "_calculateRecordingTimeForAOPTriggerFromFirstPassInfo:completion:"
+ "_combinationWeight"
+ "_combinationWeight: %f\n"
+ "_createAudioQueueIfNeeded"
+ "_decodePhraseConfig:"
+ "_defaultBufferRef"
+ "_didForceEndpoint"
+ "_echoCancellationReason"
+ "_exclaveAudioQueue"
+ "_exclaveAudioTimeConverter"
+ "_getBooleanValue:forKey:withDefaultValue:"
+ "_getExclaveAudioTimeConverter"
+ "_getFloatValue:forKey:withDefaultValue:"
+ "_getIntValue:forKey:withDefaultValue:"
+ "_implicitProfileDeltaThreshold"
+ "_implicitProfileThreshold"
+ "_implicitProfileThreshold: %f\n"
+ "_implicitTrainingEnabled"
+ "_implicitVTThreshold"
+ "_implicitVTThreshold: %f\n"
+ "_implicit_training_enabled: %d\n"
+ "_injectionCompletion"
+ "_injectionEndTime"
+ "_injectionProviderExclave"
+ "_injectionStartTime"
+ "_isAudioQueueStarted"
+ "_maxEnrollmentUtterances"
+ "_maxEnrollmentUtterances: %u\n"
+ "_multiUserConfidentScoreThreshold"
+ "_multiUserConfidentScoreThreshold: %u\n"
+ "_multiUserDeltaScoreThreshold"
+ "_multiUserDeltaScoreThreshold: %u\n"
+ "_multiUserHighScoreThreshold"
+ "_multiUserHighScoreThreshold: %u\n"
+ "_multiUserLowScoreThreshold"
+ "_multiUserLowScoreThreshold: %u\n"
+ "_numPruningRetentionUtt"
+ "_numPruningRetentionUtt: %u\n"
+ "_phoneCallStateMonitor"
+ "_phraseConfigs"
+ "_prepareAndStartAudioQueue"
+ "_pruningExplicitPSRThreshold"
+ "_pruningExplicitPSRThreshold: %f\n"
+ "_pruningExplicitSATThreshold"
+ "_pruningExplicitSATThreshold: %f\n"
+ "_pruningPSRThreshold"
+ "_pruningPSRThreshold: %f\n"
+ "_pruningSATThreshold"
+ "_pruningSATThreshold: %f\n"
+ "_readAudioBufferAndFeedIntoAudioQueue"
+ "_readThisOrVoiceOverSessionActive"
+ "_satThreshold"
+ "_setAudioSessionActive:"
+ "_trainingMessageHandler"
+ "_updateCurrentAsset:"
+ "_updateExclaveKitSiriLocale:"
+ "_useTDTIEnrollment"
+ "_useTDTIEnrollment: %d\n"
+ "cString"
+ "category"
+ "configAOPVoiceTrigger"
+ "contextForVoiceTriggerTraining"
+ "decodeSecureVoiceTriggerSpeakerRecognitionConfigForAsset:"
+ "defaultExclaveConverter"
+ "didForceEndpoint"
+ "echoCancellationReason"
+ "exclave-built-in"
+ "exclaveAudioInjectionEnabled"
+ "exclaveAudioQueue"
+ "exclaveAudioTimeConverter"
+ "exclaveSignalIntensity"
+ "extractPSRVoiceProfileWithContext:completion:"
+ "extractSATVoiceProfileWithContext:completion:"
+ "f36@0:8@16@24f32"
+ "fetchAOPVoiceTriggerResult:"
+ "generatePHashFromExclaveVoiceTriggerInfo:writeFile:"
+ "getBool:category:defaultValue:"
+ "getDictionaryArray:category:"
+ "getFloat:category:defaultValue:"
+ "getString:category:defaultValue:"
+ "getUnsignedLongLongValue:category:defaultValue:"
+ "implicitTrainingEnabled"
+ "initWithName:satThreshold:"
+ "initWithPhraseConfigs:numPruningRetentionUtt:pruningExplicitSATThreshold:pruningExplicitPSRThreshold:pruningSATThreshold:pruningPSRThreshold:combinationWeight:implicitProfileThreshold:implicitProfileDeltaThreshold:implicitVTThreshold:maxEnrollmentUtterances:implicit_training_enabled:multiUserHighScoreThreshold:multiUserLowScoreThreshold:multiUserConfidentScoreThreshold:multiUserDeltaScoreThreshold:useTDTIEnrollment:"
+ "initWithSpeechManager:voiceTriggerEnabledMonitor:siriClientBehaviorMonitor:phoneCallStateMonitor:otherAppRecordingStateMonitor:"
+ "injectionCompletion"
+ "injectionEndTime"
+ "injectionStartTime"
+ "isAudioQueueStarted"
+ "isFirstPassSourceTypeRingtoneWithVTEI:"
+ "isSiriDSPTurnedOn"
+ "isVoiceTriggerFromExclaveWithVTEI:"
+ "iteratePhraseConfigs:"
+ "phraseConfigs-count: %ld\n"
+ "readThisOrVoiceOverSessionActive"
+ "requestAudioProviderForTrainingWithSyncBlock:"
+ "resetCache"
+ "setCategory:mode:options:error:"
+ "setCombinationWeight:"
+ "setDidForceEndpoint:"
+ "setEchoCancellationReason:"
+ "setExclaveAudioQueue:"
+ "setExclaveAudioTimeConverter:"
+ "setImplicitProfileDeltaThreshold:"
+ "setImplicitProfileThreshold:"
+ "setImplicitTrainingEnabled:"
+ "setImplicitVTThreshold:"
+ "setInjectionCompletion:"
+ "setInjectionEndTime:"
+ "setInjectionStartTime:"
+ "setIsAudioQueueStarted:"
+ "setMaxEnrollmentUtterances:"
+ "setMultiUserConfidentScoreThreshold:"
+ "setMultiUserDeltaScoreThreshold:"
+ "setMultiUserHighScoreThreshold:"
+ "setMultiUserLowScoreThreshold:"
+ "setNumPruningRetentionUtt:"
+ "setPhoneCallStateMonitor:"
+ "setPhraseConfigs:"
+ "setPruningExplicitPSRThreshold:"
+ "setPruningExplicitSATThreshold:"
+ "setPruningPSRThreshold:"
+ "setPruningSATThreshold:"
+ "setReadThisOrVoiceOverSessionActive:"
+ "setSatThreshold:"
+ "setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:"
+ "setTrainingMessageHandler:"
+ "setUseTDTIEnrollment:"
+ "setVoiceTriggerEnabledMonitor:"
+ "speakAudioInExclave:withCompletion:"
+ "startSecondPassVoiceTriggerWithFirstPassSource:phsEnabled:supportMultiPhrase:"
+ "trainingMessageHandler"
+ "updateExclaveKitSiriLocale:"
+ "v24@0:8@?<v@?@\"CSAudioProvider\">16"
+ "v24@?0Q8Q16"
+ "v32@?0@\"NSDictionary\"8Q16^B24"
+ "v32@?0@\"SecureSpeakerRecognitionPhraseConfigBridge\"8Q16^B24"
+ "v36@?0@\"NSData\"8I16I20I24@\"NSError\"28"
+ "v56@?0Q8d16f24f28I32f36Q40Q48"
+ "v60@?0I8Q12d20f28f32I36f40Q44Q52"
+ "\x81"
- "\x0f\x03"
- "%s CSHybridEndpointer can-NOT-ProcessCurrentRequest, fallback  to NNVAD"
- "%s File not exist: %{public}@"
- "%s IVoiceTrigger on hearst cannot be turned on since Siri client is currently in an outgoing call"
- "%s Ignore %{public}@ since voice trigger enabled policy returned NO"
- "%s VoiceTrigger on hearst cannot be turned on Siri client is current listening"
- "%s VoiceTrigger on hearst cannot be turned on since Siri client is currently in a connected call"
- "%s VoiceTrigger on hearst cannot be turned on since Siri client is currently in a ringtone and does not support A2DP"
- "%s VoiceTrigger on hearst cannot be turned on since Siri is restricted on lock screen"
- "%s VoiceTrigger on hearst cannot be turned on since VoiceTrigger is disabled"
- "%s VoiceTrigger on hearst cannot be turned on since phrases spotter is disabled"
- "%s VoiceTrigger on hearst cannot be turned on since there is an other non eligible app recording"
- "%s attendingStateStart:(%u) audioSessionStateActive:(%u) aggressiveECParamsApplied:(%u) inAttendingWindow:(%u)"
- "%s audioSessionRequiresECParams:(%u) aggressiveEchoCancellationApplied:(%u) inAttendingWindow:(%u)"
- "%s isReadThis:(%u), isVoiceOver:(%u)"
- "%s progCheckerReocgnizerConfigFiles: %@"
- "%s update assets to: %@"
- "+[CSOnDeviceCompilationUtils getModelConfigsWithAsset:modelType:]"
- "-[CSHybridEndpointer endpointerAssetManagerDidUpdateAsset:]_block_invoke"
- "-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke"
- ";"
- "@\"CSScreenLockMonitor\""
- "@\"CSSiriRestrictionOnLockScreenMonitor\""
- "@\"CSVoiceTriggerHearstEnabledPolicy\""
- "CSVoiceTriggerHearstEnabledPolicy"
- "Q\x1b\xc1\x81\x12\x18A"
- "T@\"CSOtherAppRecordingStateMonitor\",R,N,V_otherAppRecordingStateMonitor"
- "T@\"CSPhoneCallStateMonitor\",R,N,V_phonecallStateMonitor"
- "T@\"CSScreenLockMonitor\",R,N,V_screenLockMonitor"
- "T@\"CSSiriClientBehaviorMonitor\",R,N,V_siriClientBehaviorMonitor"
- "T@\"CSSiriRestrictionOnLockScreenMonitor\",R,N,V_siriRestrictionOnLockScreenMonitor"
- "T@\"CSVoiceTriggerEnabledMonitor\",R,N,V_voiceTriggerEnabledMonitor"
- "T@\"CSVoiceTriggerHearstEnabledPolicy\",&,N,V_voicetriggerHearstEnabledPolicy"
- "TB,N,V_audioSessionStateActive"
- "TB,N,V_echoCancellationDeferred"
- "_audioSessionStateActive"
- "_echoCancellationDeferred"
- "_phonecallStateMonitor"
- "_screenLockMonitor"
- "_siriRestrictionOnLockScreenMonitor"
- "_voicetriggerHearstEnabledPolicy"
- "audioSessionStateActive"
- "echoCancellationDeferred"
- "initWithSiriRestrictionOnLockScreenMonitor:screenLockMonitor:voiceTriggerEnabledMonitor:CSPhoneCallStateMonitor:otherAppRecordingStateMonitor:siriClientBehaviorMonitor:srfUserSettingsMonitor:"
- "initWithSpeechManager:voiceTriggerEnabledPolicyHearst:"
- "phonecallStateMonitor"
- "screenLockMonitor"
- "setAudioSessionStateActive:"
- "setEchoCancellationDeferred:"
- "setVoicetriggerHearstEnabledPolicy:"
- "siriRestrictionOnLockScreenMonitor"
- "startSecondPassVoiceTriggerWithPHSEnabled:supportMultiPhrase:"
- "v20@?0I8Q12"
- "voicetriggerHearstEnabledPolicy"

```
