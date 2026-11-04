## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`

```diff

-3605.32.1.0.0
-  __TEXT.__text: 0x17f150
-  __TEXT.__auth_stubs: 0x1620
-  __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_stubs: 0x226a0
-  __TEXT.__objc_methlist: 0x1c430
-  __TEXT.__dlopen_cstrs: 0x31a
-  __TEXT.__const: 0x400
-  __TEXT.__gcc_except_tab: 0x3138
-  __TEXT.__objc_methname: 0x49432
-  __TEXT.__cstring: 0x312c0
-  __TEXT.__oslogstring: 0x283f6
-  __TEXT.__objc_classname: 0x3aa5
-  __TEXT.__objc_methtype: 0x97ff
-  __TEXT.__unwind_info: 0x7680
-  __DATA_CONST.__const: 0x5f50
-  __DATA_CONST.__cfstring: 0x91e0
-  __DATA_CONST.__objc_classlist: 0xa28
+3610.11.1.0.0
+  __TEXT.__text: 0x181534
+  __TEXT.__auth_stubs: 0x1640
+  __TEXT.__lazy_helpers: 0xa8
+  __TEXT.__objc_stubs: 0x22b60
+  __TEXT.__objc_methlist: 0x1c670
+  __TEXT.__dlopen_cstrs: 0x2d1
+  __TEXT.__const: 0x3f8
+  __TEXT.__gcc_except_tab: 0x312c
+  __TEXT.__objc_methname: 0x49d88
+  __TEXT.__cstring: 0x31655
+  __TEXT.__oslogstring: 0x28e0d
+  __TEXT.__objc_classname: 0x3b25
+  __TEXT.__objc_methtype: 0x994f
+  __TEXT.__unwind_info: 0x76f8
+  __DATA_CONST.__const: 0x5f20
+  __DATA_CONST.__cfstring: 0x92c0
+  __DATA_CONST.__objc_classlist: 0xa30
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x5d0
+  __DATA_CONST.__objc_protolist: 0x5e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xf8
-  __DATA_CONST.__objc_superrefs: 0x850
+  __DATA_CONST.__objc_superrefs: 0x858
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__objc_intobj: 0xd68
   __DATA_CONST.__objc_arraydata: 0x290
   __DATA_CONST.__objc_arrayobj: 0x180
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x5b0
-  __DATA_CONST.__auth_got: 0xb28
-  __DATA_CONST.__got: 0x1560
+  __DATA_CONST.__auth_got: 0xb38
+  __DATA_CONST.__got: 0x1578
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x2ca28
-  __DATA.__objc_selrefs: 0xd258
-  __DATA.__objc_ivar: 0x22b4
-  __DATA.__objc_data: 0x6590
-  __DATA.__lazy_load_got: 0x8
-  __DATA.__data: 0x45c4
+  __DATA.__objc_const: 0x2cd58
+  __DATA.__objc_selrefs: 0xd3d0
+  __DATA.__objc_ivar: 0x22e0
+  __DATA.__objc_data: 0x65e0
+  __DATA.__lazy_load_got: 0x10
+  __DATA.__data: 0x46e4
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10639
-  Symbols:   1039
-  CStrings:  17480
+  Functions: 10679
+  Symbols:   1045
+  CStrings:  17597
 
Symbols:
+ _LBRequestMutexServiceDelegateGetXPCInterface
+ _LBRequestMutexServiceGetXPCInterface
+ _LBRequestMutexServiceName
+ _OBJC_CLASS_$_CSCompanionRuntimeThresholdKeys
+ _OBJC_CLASS_$_CSLinwoodEnabledAndAvailableMonitor
+ _OBJC_CLASS_$_CSRequestMutexController
+ _OBJC_CLASS_$_DeviceSelectionTriggerAudio
+ _OBJC_CLASS_$_SSRSpeakerProfileEmbeddingServiceListener
+ _kSFSpeechProfileDefaultUserId
- _OBJC_CLASS_$_AVAudioFormat
- _OBJC_CLASS_$_AVAudioPCMBuffer
- _kVTEIInputLatency
CStrings:
+ "\n"
+ "%@/%@%-@ch%d-mct%llu.pcm.wav"
+ "%s #deviceSelection AToA Failed to get trigger audio buffer"
+ "%s #deviceSelection AToA exclave trigger; no slice is donated on this build"
+ "%s #deviceSelection AToA trigger audio chunk is empty; no slice to donate"
+ "%s #deviceSelection AToA trigger audio has no buffer timestamp; it cannot be ordered"
+ "%s #deviceSelection AToA trigger audio slice has no samples; nothing donated"
+ "%s #deviceSelection Error - no audio chunk for trigger audio slice, channel: %@"
+ "%s #deviceSelection Trigger audio buffer too short for %lu samples; slice will start at 0"
+ "%s #deviceSelection Trigger audio slice: %lu samples, format: %@, channel: %@"
+ "%s #mutex Request mutex service xpc connection started listening"
+ "%s #mutex owner changed to %lu, notifying clients"
+ "%s #mutex received release, isCompanionRequest: %d, requestId: %@, pid: %d"
+ "%s #mutex received tryAcquire, isCompanionRequest: %d, requestId: %@, holdTimeInMillis: %ld, pid: %d"
+ "%s #mutex release without a current connection"
+ "%s #mutex tryAcquire with feature flag disabled"
+ "%s #mutex tryAcquire without a current connection"
+ "%s #requestLock cannot disable consuming for requestId %@: a companion request holds Audio"
+ "%s #requestLock cannot enable consuming for requestId %@: a local request holds Audio"
+ "%s #requestLock cannot handle PrepareRequest : companion request mutex is held, streamClientType:%lu"
+ "%s #requestLock cannot handle startAudioStream : companion request mutex is held, streamClientType:%lu"
+ "%s #requestlock ignoring companion ASR start for requestId %@, local request mutex is held"
+ "%s #requestlock ignoring local ASR start for requestId %@, companion request mutex is held"
+ "%s #stream #requestLock could not acquire CSRequestMutex"
+ "%s #stream Audio streaming stopping and clearing buffer"
+ "%s #stream resetting audio chunk queue on stream stop as force clear was requested"
+ "%s ASR didComplete for requestId %@, releasing request mutex"
+ "%s Acquired local request mutex for startAudioStream, streamClientType:%lu"
+ "%s CSVoiceTriggerSecondPass[%{public}@]:First pass selected channel %{public}tu, using channel %{public}tu for second pass"
+ "%s CSVoiceTriggerSecondPass[%{public}@]:No first pass score for allowed channels 0x%{public}llx, using first pass channel %{public}tu"
+ "%s Device Selection Feature or AToA (Audio Time of Arrival) disabled, returning"
+ "%s Donated trigger audio slice (%@, at: %llu) successfully"
+ "%s Failed to donate trigger audio slice: %@"
+ "%s Failed to save trigger audio slice to file %{public}@"
+ "%s Ignoring ASR start for retired requestId %@"
+ "%s Linwood enabled and available changed to %{public}@, first pass channels 0x%{public}llx -> 0x%{public}llx. Apply the current voice trigger asset again."
+ "%s Linwood enabled and available changed to %{public}@, first pass channels 0x%{public}llx do not change"
+ "%s No final scorecard after %llu ms, releasing session %{public}@"
+ "%s Remote audio source stopped with endpoint mode unset; treating as manual stop"
+ "%s Selected multi-user TRP candidate trpCandidateId: %{public}@"
+ "%s TSSD: target scored %.3f vs threshold %.3f (selfPlatform:%lu originatingDeviceType:%lu recordRoute:%{public}@)"
+ "%s Trigger Audio length %lu, format: %@"
+ "%s Using %{public}@=%{public}@ from section %{public}@"
+ "%s Wrote trigger audio slice as a PCM WAV file: %@"
+ "%s stopping audio stream and clearing buffer since companion user turn ended"
+ "+[CSMyriadPHash getTriggerAudioForVoiceTriggerInfo:withHostTime:writeFile:]"
+ "-[CSAsset(SpeakerRecognition) _firstNumberForKey:inSectionKeys:]"
+ "-[CSAttSiriConnectionManager setupRequestMutexServiceListener]"
+ "-[CSAttSiriSSRNode _holdSessionForFinalScoreCard:]_block_invoke"
+ "-[CSAttSiriSSRNode _notifyLocalSRBridgeWithScoreCard:]"
+ "-[CSAttSiriSpeechPresenceMessageBuilder didGenerateMultiUserTRPCandidatePackage:selectedTRPCandidateId:]"
+ "-[CSAudioStreamProviderServiceHandler _stopStreamingAndClearBuffer]"
+ "-[CSBuiltInVoiceTrigger linwoodEnabledAndAvailableMonitor:didReceiveEnabledAndAvailable:]_block_invoke"
+ "-[CSDeviceSelectionNotifier _notifyTriggerAudioSliceVoiceTriggerInfo:]"
+ "-[CSDeviceSelectionNotifier _notifyTriggerAudioSliceVoiceTriggerInfo:]_block_invoke"
+ "-[CSIntuitiveConvRequestHandler didCompleteRecognitionTaskWithStatistics:requestId:endpointMode:error:]"
+ "-[CSRequestMutexServiceHandler releaseCSRequestMutex:requestId:resourceType:]"
+ "-[CSRequestMutexServiceHandler requestMutexOwnerDidChange:]"
+ "-[CSRequestMutexServiceHandler tryAcquireCSRequestMutex:requestId:resourceType:holdTimeInMillis:completion:]"
+ "-[CSVoiceTriggerSecondPass _secondPassChannelForFirstPassChannel:channelSelectionScores:isLinwoodEnabledAndAvailable:]"
+ "2"
+ "3"
+ "@\"CSRequestMutexServiceHandler\""
+ "@36@0:8@16^Q24B32"
+ "AB"
+ "B24@0:8@\"NSString\"16"
+ "CSLinwoodEnabledAndAvailableMonitorDelegate"
+ "CSRequestMutexControllerObserver"
+ "CSRequestMutexServiceHandler"
+ "Companion request mutex is held; local ASR start rejected"
+ "LBRequestMutexService"
+ "Local request mutex is held; companion ASR start rejected"
+ "Q36@0:8Q16@24B32"
+ "RequestMutexServiceListener"
+ "StopAndClearBuffer"
+ "T@\"<CSSpeakerRecognitionSession>\",&,N,V_finishingSession"
+ "T@\"CSConnectionListener\",&,N,V_requestMutexServiceListener"
+ "T@\"CSRequestMutexServiceHandler\",&,N,V_requestMutexServiceHandler"
+ "TB,N,V_isListeningWithActiveCallContext"
+ "TriggerAudioSlice-"
+ "Vv36@0:8B16@\"NSString\"20Q28"
+ "Vv36@0:8B16@20Q28"
+ "Vv52@0:8B16@\"NSString\"20Q28q36@?<v@?B@\"NSError\">44"
+ "Vv52@0:8B16@20Q28q36@?44"
+ "_audioMutexLock"
+ "_audioMutexRequestId"
+ "_finishingSession"
+ "_firstNumberForKey:inSectionKeys:"
+ "_holdSessionForFinalScoreCard:"
+ "_holdsAudioMutex"
+ "_isLinwoodEnabledAndAvailable"
+ "_isListeningWithActiveCallContext"
+ "_isLocalDeviceSiriRequest"
+ "_notifyLocalSRBridgeWithScoreCard:"
+ "_notifyTriggerAudioSliceVoiceTriggerInfo:"
+ "_numberForKey:inSection:"
+ "_recordAudioRequestMutexHeldForRequestId:"
+ "_releaseAudioRequestMutexForRequestId:"
+ "_releaseAudioRequestMutexIfHeld"
+ "_requestMutexServiceHandler"
+ "_requestMutexServiceListener"
+ "_retiredRequestIds"
+ "_retiredRequestIdsLock"
+ "_secondPassChannelForFirstPassChannel:channelSelectionScores:isLinwoodEnabledAndAvailable:"
+ "_shouldDonateTriggerAudioSlice"
+ "_shouldHoldSessionForFinalScoreCard"
+ "_shouldPublishFinalScoreCardToLocalSRBridge"
+ "_shouldRequestExclaveAudioWithProvider:"
+ "_stopStreamingAndClearBuffer"
+ "_trpCandidateFromGuestUser:"
+ "allowedChannelsBitset"
+ "allowedChannelsBitsetLinwood"
+ "areAllResourcesAvailableToAcquireByOwner:resourceType:"
+ "decodeConfigFrom:shouldExcludeBSSChannels:isLinwoodEnabledAndAvailable:"
+ "deviceSelectionTriggerAudioSliceMs"
+ "didGenerateMultiUserTRPCandidatePackage:selectedTRPCandidateId:"
+ "donateTriggerAudioSlice:withCompletion:"
+ "f28@0:8Q16B24"
+ "f40@0:8Q16Q24@\"NSString\"32"
+ "f40@0:8Q16Q24@32"
+ "finishingSession"
+ "float32"
+ "getTriggerAudioForVoiceTriggerInfo:withHostTime:writeFile:"
+ "inRequestSegmentSpkrIdScoreThresholdForSelfPlatform:servingPlatform:recordRoute:"
+ "initWithBuffer:sampleRate:isFloat32:timestamp:triggerStartMachTime:triggerEndMachTime:dspLatency:"
+ "insertObject:atIndex:"
+ "int16"
+ "isDeviceSelectionParticipating"
+ "isDeviceSelectionShadowModeEnabled"
+ "isEnabledAndAvailable"
+ "isListeningWithActiveCallContext"
+ "isRequestIdRetired:"
+ "isRequestLockEnforcingSingleTenancyEnabled"
+ "linwoodEnabledAndAvailableMonitor:didReceiveEnabledAndAvailable:"
+ "prepareToStartRequestWithStartStreamOption:"
+ "releaseAllForRemoteClient:"
+ "releaseCSRequestMutex:requestId:resourceType:"
+ "releaseForOwner:requestId:resourceType:"
+ "releaseForRemoteClient:requestId:isCompanionRequest:resourceType:"
+ "releaseIfHeldForRequestId:resourceType:"
+ "requestMutexOwnerDidChange:"
+ "requestMutexOwnershipChanged:"
+ "requestMutexServiceHandler"
+ "requestMutexServiceListener"
+ "sectionKeysForSelfPlatform:servingPlatform:recordRoute:"
+ "setFinishingSession:"
+ "setIsListeningWithActiveCallContext:"
+ "setRequestMutexServiceHandler:"
+ "setRequestMutexServiceListener:"
+ "setupRequestMutexServiceListener"
+ "sha256HashStringFromInputString:"
+ "shouldExcludeBSSChannelsFromVoiceTrigger"
+ "stopStreamingAndClearBuffer"
+ "supportMindPalaceAmbient"
+ "supportsVoiceTriggerAssetChannelSelection"
+ "trailingSilenceDurationThresholdMsForDeviceType:runningInCompanionRuntime:"
+ "trailingSilenceDurationThresholdMsPebbleCompanion"
+ "trailingSilenceDurationThresholdMsPebbleStandalone"
+ "tryAcquireCSRequestMutex:requestId:resourceType:holdTimeInMillis:completion:"
+ "tryAcquireForCompanionWithRequestId:resourceType:"
+ "tryAcquireForLocalWithRequestId:resourceType:"
+ "tryAcquireForRemoteClient:requestId:isCompanionRequest:resourceType:holdTimeInMillis:"
+ "userId"
+ "v28@0:8@\"CSLinwoodEnabledAndAvailableMonitor\"16B24"
+ "v32@0:8@\"SMTMultiUserTRPCandidate\"16@\"NSString\"24"
- "%@/%@%@.pcm.wav"
- "%s #deviceSelection Error - no audio chunk for channel: %@"
- "%s #deviceSelection Error appending buffer to generator: %@"
- "%s #deviceSelection configured to grab maximum of %f seconds of audio"
- "%s #deviceSelection signature duration == 0.0, skipping"
- "%s Donated fingerprint (%@, at: %llu) successfully"
- "%s Failed to donate fingerprint: %@"
- "%s Failed to save shazam signature chunk to file %{public}@"
- "%s Fingerprint duration = %f Signature len = %d channel = %@"
- "%s Signature length %lu"
- "%s Skipping NC inference for requestId %@: mitigation bypassed for this context"
- "%s TSSD: target scored %.3f vs threshold %.3f"
- "%s Wrote the fingerprint audio buffer as a PCM WAV file: %@"
- "%s stopping audio stream since companion user turn ended"
- "+[CSMyriadPHash _generateFingerPrintFromVoiceTriggerInfo:audioHostTime:usingGenerator:]"
- "+[CSMyriadPHash generateFingerprintForVoiceTriggerInfo:forTime:]"
- "-[CSAttSiriSSRNode speakerRecognitionSession:hasSpeakerInfo:]_block_invoke_2"
- "-[CSAttSiriSpeechPresenceMessageBuilder didGenerateMultiUserTRPCandidatePackage:]"
- "-[CSBuiltInVoiceTrigger _stopListening]"
- "-[CSBuiltInVoiceTrigger _stopListening]_block_invoke"
- "-[CSDeviceSelectionNotifier _notifyFingerprintForVoiceTriggerInfo:]"
- "-[CSDeviceSelectionNotifier _notifyFingerprintForVoiceTriggerInfo:]_block_invoke"
- "@32@0:8@16^Q24"
- "@40@0:8@16^Q24@32"
- "C!E"
- "SHSignatureGenerator"
- "ShazamPCM-"
- "T"
- "T@\"NSString\",C,N,V_previousRequestId"
- "_generateFingerPrintFromVoiceTriggerInfo:audioHostTime:usingGenerator:"
- "_notifyFingerprintForVoiceTriggerInfo:"
- "_previousRequestId"
- "appendBuffer:atTime:error:"
- "dataRepresentation"
- "deviceSelectionShazamDuration"
- "donateFingerprint:forTimestamp:triggerStartMachTime:triggerEndMachTime:withCompletion:"
- "duration"
- "floatChannelData"
- "frameCapacity"
- "generateFingerprintForVoiceTriggerInfo:forTime:"
- "initWithCommonFormat:sampleRate:channels:interleaved:"
- "initWithPCMFormat:frameCapacity:"
- "int16ChannelData"
- "isDeviceSelectionEnabled"
- "setFrameLength:"
- "softlink:r:path:/System/Library/Frameworks/ShazamKit.framework/ShazamKit"
- "trailingSilenceDurationThresholdMsForDeviceType:"
- "trailingSilenceDurationThresholdMsPebble"
```
