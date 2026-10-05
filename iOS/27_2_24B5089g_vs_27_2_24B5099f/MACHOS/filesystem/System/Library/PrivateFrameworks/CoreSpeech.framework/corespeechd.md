## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-3605.25.1.0.0
-  __TEXT.__text: 0x17cf18
+3605.31.3.0.0
+  __TEXT.__text: 0x17e5f8
   __TEXT.__auth_stubs: 0x1610
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_stubs: 0x22340
-  __TEXT.__objc_methlist: 0x1c178
+  __TEXT.__objc_stubs: 0x22660
+  __TEXT.__objc_methlist: 0x1c3a0
   __TEXT.__dlopen_cstrs: 0x31a
   __TEXT.__const: 0x3d0
-  __TEXT.__gcc_except_tab: 0x30f8
-  __TEXT.__objc_methname: 0x48a91
-  __TEXT.__cstring: 0x30f03
-  __TEXT.__oslogstring: 0x27ae9
-  __TEXT.__objc_classname: 0x3a44
-  __TEXT.__objc_methtype: 0x973d
-  __TEXT.__unwind_info: 0x75e8
-  __DATA_CONST.__const: 0x5e50
-  __DATA_CONST.__cfstring: 0x9100
-  __DATA_CONST.__objc_classlist: 0xa10
+  __TEXT.__gcc_except_tab: 0x3138
+  __TEXT.__objc_methname: 0x49237
+  __TEXT.__cstring: 0x3116b
+  __TEXT.__oslogstring: 0x280c5
+  __TEXT.__objc_classname: 0x3a7f
+  __TEXT.__objc_methtype: 0x97e8
+  __TEXT.__unwind_info: 0x7658
+  __DATA_CONST.__const: 0x5e80
+  __DATA_CONST.__cfstring: 0x9180
+  __DATA_CONST.__objc_classlist: 0xa20
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x5d0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf8
-  __DATA_CONST.__objc_superrefs: 0x838
+  __DATA_CONST.__objc_superrefs: 0x848
   __DATA_CONST.__objc_doubleobj: 0x80
-  __DATA_CONST.__objc_intobj: 0xd38
+  __DATA_CONST.__objc_intobj: 0xd50
   __DATA_CONST.__objc_arraydata: 0x290
   __DATA_CONST.__objc_arrayobj: 0x180
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x5b0
   __DATA_CONST.__auth_got: 0xb20
-  __DATA_CONST.__got: 0x1540
+  __DATA_CONST.__got: 0x1550
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x2c4b0
-  __DATA.__objc_selrefs: 0xd0f8
-  __DATA.__objc_ivar: 0x226c
-  __DATA.__objc_data: 0x64a0
+  __DATA.__objc_const: 0x2c900
+  __DATA.__objc_selrefs: 0xd210
+  __DATA.__objc_ivar: 0x22a8
+  __DATA.__objc_data: 0x6540
   __DATA.__lazy_load_got: 0x8
   __DATA.__data: 0x45c4
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10579
-  Symbols:   1035
-  CStrings:  17362
+  Functions: 10623
+  Symbols:   1037
+  CStrings:  17449
 
Symbols:
+ _OBJC_CLASS_$_CSFModelConfigDecoder
+ _OBJC_CLASS_$_LBLocalSpeechRecognizerTurnEndContext
CStrings:
+ "#Bab"
+ "%s Cancel received for retired requestId:%{public}@, currentRequestId:%{public}@. Bail out!"
+ "%s Coordinator discarding speech recognition task %lu for stale requestId: %@ (active: %@)"
+ "%s Coordinator received ASR first pass features - wordCount: %lu, trailingSilence: %ldms, processedAudio: %ldms"
+ "%s Coordinator speech recognition task set to %lu (isSiriDictation=%d)"
+ "%s Dropping pending attending decision for disabled rootRequestId: %@"
+ "%s Dropping pending attending start for disabled rootRequestId: %@"
+ "%s Evicting ctx for requestId:%{public}@ ageMs:%llu"
+ "%s Failed to delete uncommitted leading utterance: %{public}@"
+ "%s Inference profile: appDomain=%{public}@ profileID=%{public}@ locale=%{public}@"
+ "%s Multiple requests in progress - %@"
+ "%s Newer request (%@) is active, skipping completion tail for drained request %@"
+ "%s Resolved turn-end metrics: speechEndHostTime=%llu trailingSilence=%.1fms"
+ "%s Skipping cc session-end cleanup: leading-utterance recording in flight"
+ "%s Trailing silence threshold met via NoTRPArrival (%.1fms): trailingSilence=%.1fms (processedAudio=%ldms - trpSilStart=%.1fms)"
+ "%s Trailing silence threshold met: trailingSilence=%.1fms (processedAudio=%ldms - trpSilStart=%.1fms)"
+ "%s Triggering TRP timeout since %.1f ms have elapsed since last TCU/Speech and ASR decoded %.1f ms with no wordCount change (threshold: %.1f), wordCount: %lu, asrProcessedAudioAtLastWordCountChangeMs: %.1ld, totalProcessAudioDurationMs: %.1ld and startAnchorPoint: %.1f"
+ "%s Triggering TRP timeout since %.1f ms have elapsed since last TCU/Speech and no wordCount change, totalProcessAudioDurationMs: %.1ld and startAnchorPoint: %.1f"
+ "%s not stopping audio stream; requestId:%{public}@ retired, currentRequestId:%{public}@"
+ "%s open turn-based audio gate for requestId: %@"
+ "%s received requestId:%{public}@ doesn't match currentRequest's %{public}@ requestId:%{public}@. Bail out!"
+ "%s requestId: %@, trpId: %@, turnEndReason: %{public}@, processedAudioDurationMs: %f, trailingSilenceDurationMs: %f, runtimeType: %{public}@, shouldStartAttendingAtUserTurnEnded: %{public}@"
+ "%s requestId: %{public}@ turn Ended at sample count: %.3llu, trailingSilenceDurationMs: %f (not subtracted)"
+ "%s trpId:%@ lastTransitionTimeMs: %f, trailingSilenceDurationMs:%f, turnEndReason:%{public}@, runtimeType:%{public}@"
+ "%s tryReplayingFromBufferStart: gate already open, skipping replay"
+ "-[CSAttSiriSSRNode _beginLeadingUtteranceCapture]"
+ "-[CSAttSiriSpeechPresenceCoordinator turnEndMetricsForTRPId:turnEndReason:processedAudioDurationMs:]"
+ "-[CSAttSiriSpeechPresenceCoordinator updateSpeechRecognitionTask:forRequestId:]_block_invoke"
+ "-[CSAttSiriSpeechRecognitionNode _releaseDrainingSpeechRecognition]"
+ "-[CSAttSiriUresNode _removeExpiredRequestsExcluding:now:]"
+ "-[CSIntuitiveConvRequestHandler disableAttendingRequestedForRootRequestId:]_block_invoke"
+ "-[CSIntuitiveConvRequestHandler openTurnBasedAudioGateForRequestId:]_block_invoke"
+ "<%@: speechEndHostTime=%llu trailingSilenceMs=%.1f>"
+ "@\"CSAttSiriDrainingSpeechRecognition\""
+ "@32@0:8Q16d24"
+ "@40@0:8@16Q24d32"
+ "B40@0:8@16^@24^@32"
+ "B56@0:8Q16Q24@\"NSString\"32^@40^@48"
+ "B56@0:8Q16Q24@32^@40^@48"
+ "CSAttSiriDrainingSpeechRecognition"
+ "CSAttSiriTurnEndMetrics"
+ "MHId %@ recordType %@ ageMs %llu"
+ "T@\"<CoreEmbeddedSpeechRecognizerProvider>\",R,N,V_recognizer"
+ "T@\"CSAttSiriDrainingSpeechRecognition\",&,N,V_drainingSpeechRecognition"
+ "T@\"NSString\",R,N,V_recognizerLanguage"
+ "T@,&,N,V_analytics"
+ "T@,&,N,V_selfLoggingStream"
+ "TB,N,V_committedLeadingUtterance"
+ "TB,V_requestExclaveAudio"
+ "TQ,N,V_speechRecognitionTask"
+ "TQ,R,N,V_creationHostTime"
+ "TQ,R,N,V_speechEndHostTime"
+ "Td,R,N,V_trailingSilenceMs"
+ "Tq,N,V_asrProcessedAudioAtLastWordCountChangeMs"
+ "Tq,R,N,V_endpointMode"
+ "_analytics"
+ "_asrProcessedAudioAtLastWordCountChangeMs"
+ "_audioBufferForWriting"
+ "_beginLeadingUtteranceCapture"
+ "_committedLeadingUtterance"
+ "_creationHostTime"
+ "_drainingSpeechRecognition"
+ "_isSiriDictationTask"
+ "_newestRequestCtx"
+ "_recognizer"
+ "_releaseDrainingSpeechRecognition"
+ "_removeExpiredRequestsExcluding:"
+ "_removeExpiredRequestsExcluding:now:"
+ "_requestExclaveAudio"
+ "_selfLoggingStream"
+ "_sendMessageAndReplySync:reply:error:"
+ "_sendReplyMessageWithResult:audioDeviceInfo:error:event:client:"
+ "_speechEndHostTime"
+ "_speechRecognitionTask"
+ "_trailingSilenceMs"
+ "activateAudioSessionWithReason:dynamicAttribute:bundleID:audioDeviceInfo:error:"
+ "analytics"
+ "asrNoWordCountChangeTimeoutMs"
+ "asrProcessedAudioAtLastWordCountChangeMs"
+ "canCreateContinuousConversationProfile"
+ "committedLeadingUtterance"
+ "creationHostTime"
+ "decodeJsonFromFile:"
+ "defaultOptionWithTimeout:requestExclaveAudio:"
+ "drainingLocalSpeechRecognizer"
+ "drainingSpeechRecognition"
+ "initWithLanguage:requestIdentifier:dictationUIInteractionIdentifier:task:loggingContext:applicationName:profile:overrides:modelOverrideURL:originalAudioFileURL:codec:narrowband:detectUtterances:censorSpeech:farField:secureOfflineOnly:shouldStoreAudioOnDevice:continuousListening:shouldHandleCapitalization:isSpeechAPIRequest:maximumRecognitionDuration:endpointStart:inputOrigin:location:jitGrammar:deliverEagerPackage:disableDeliveringAsrFeatures:enableEmojiRecognition:enableAutoPunctuation:enableVoiceCommands:disableEagerLimit:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:recognitionStart:shouldGenerateVoiceCommandCandidates:asrId:activeUserInfo:messagesContext:sessionIdentifier:applicationProcessIdentifier:isAudioSourceRemote:"
+ "initWithRecognizer:requestId:endpointMode:recognizerLanguage:"
+ "initWithSpeechEndHostTime:trailingSilenceMs:"
+ "initWithTimeout:clientIdentity:requireRecordModeLock:requireListeningMicIndicatorLock:requestExclaveAudio:"
+ "isAudioSourceRemote"
+ "openTurnBasedAudioGateForRequestId:"
+ "purgeCachedConfigs"
+ "recognizer"
+ "requestAudioDeviceInfo"
+ "requestExclaveAudio"
+ "selfLoggingStream"
+ "setAnalytics:"
+ "setAsrProcessedAudioAtLastWordCountChangeMs:"
+ "setCommittedLeadingUtterance:"
+ "setDrainingSpeechRecognition:"
+ "setSelfLoggingStream:"
+ "setSpeechRecognitionTask:"
+ "trailingSilenceDurationThresholdMsExtendedSiriDictation"
+ "trailingSilenceDurationThresholdMsMaximumSiriDictation"
+ "trailingSilenceMs"
+ "turnEndMetricsForTRPId:turnEndReason:processedAudioDurationMs:"
+ "turnEndReasonString:"
+ "updateSpeechRecognitionTask:forRequestId:"
+ "v52@0:8B16@20@28@36@44"
+ "\xa5"
- "#2aR"
- "%s Coordinator received ASR first pass features - wordCount: %lu, trailingSilence: %ldms"
- "%s ERR: metaData is nil, defaulting to NO for %@"
- "%s ERR: read metafile %@ failed with %{public}@ - defaulting to NO"
- "%s Triggering TRP timeout since %.1f ms have elapsed since last TCU/Speech, totalProcessAudioDurationMs: %.1ld and startAnchorPoint: %.1f"
- "%s not stopping audio stream; received requestId:%@ doesn't match the current requestId:%@"
- "%s requestId: %@, trpId: %@, turnEndReason: %i, processedAudioDurationMs: %f, runtimeType: %{public}@, shouldStartAttendingAtUserTurnEnded: %{public}@"
- "%s trailingSilence(%f) >= baseNoTRPThreshold(%f)?"
- "%s trailingSilence=%.1f"
- "%s trpId:%@ lastTransitionTimeMs: %f, trailingSilenceDurationMs:%f, turnEndReason:%lu, runtimeType:%{public}@"
- "%s turn Ended at sample count: %.3llu, turnEndSampleCountMinusTrailingSilence: %.3llu"
- "-[CSAttSiriSSRNode _setupLeadingUtteranceLogger]"
- "-[CSAttSiriUresNode _decodeJsonFromFile:]"
- "-[CSEndpointAnalyzerBase getHybridEndpointerConfigForAsset:]"
- "MHId %@ recordType %@"
- "_decodeJsonFromFile:"
- "_setupLeadingUtteranceLogger"
- "companionSettingsWithRequestId:inputOrigin:"
- "configureForRecordRoute:preferUseSelfTap:"
- "deactivate"
- "initWithLanguage:requestIdentifier:dictationUIInteractionIdentifier:task:loggingContext:applicationName:profile:overrides:modelOverrideURL:originalAudioFileURL:codec:narrowband:detectUtterances:censorSpeech:farField:secureOfflineOnly:shouldStoreAudioOnDevice:continuousListening:shouldHandleCapitalization:isSpeechAPIRequest:maximumRecognitionDuration:endpointStart:inputOrigin:location:jitGrammar:deliverEagerPackage:disableDeliveringAsrFeatures:enableEmojiRecognition:enableAutoPunctuation:enableVoiceCommands:disableEagerLimit:sharedUserInfos:prefixText:postfixText:selectedText:powerContext:recognitionStart:shouldGenerateVoiceCommandCandidates:asrId:activeUserInfo:messagesContext:sessionIdentifier:applicationProcessIdentifier:"
- "isTriggerlessAnnounce"
- "processAudioChunkForTV:"
- "\xa3"
```
