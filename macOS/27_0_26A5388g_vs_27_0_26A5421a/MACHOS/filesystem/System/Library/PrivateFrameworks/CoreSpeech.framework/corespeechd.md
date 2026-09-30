## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3600.70.32.0.0
-  __TEXT.__text: 0x17b1bc
-  __TEXT.__auth_stubs: 0x13f0
+3600.70.47.0.0
+  __TEXT.__text: 0x17c338
+  __TEXT.__auth_stubs: 0x1400
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_stubs: 0x20840
-  __TEXT.__objc_methlist: 0x1ad10
-  __TEXT.__const: 0x368
+  __TEXT.__objc_stubs: 0x20a00
+  __TEXT.__objc_methlist: 0x1ae30
+  __TEXT.__const: 0x378
   __TEXT.__dlopen_cstrs: 0x126
-  __TEXT.__gcc_except_tab: 0x2cc0
-  __TEXT.__cstring: 0x2de77
-  __TEXT.__objc_methname: 0x44b4d
-  __TEXT.__oslogstring: 0x25d27
+  __TEXT.__gcc_except_tab: 0x2cf0
+  __TEXT.__cstring: 0x2e09e
+  __TEXT.__objc_methname: 0x45105
+  __TEXT.__oslogstring: 0x26048
   __TEXT.__objc_classname: 0x3729
-  __TEXT.__objc_methtype: 0x8c63
-  __TEXT.__unwind_info: 0x59d0
-  __DATA_CONST.__const: 0x6278
-  __DATA_CONST.__cfstring: 0x87a0
+  __TEXT.__objc_methtype: 0x8ccc
+  __TEXT.__unwind_info: 0x5a08
+  __DATA_CONST.__const: 0x62f0
+  __DATA_CONST.__cfstring: 0x87c0
   __DATA_CONST.__objc_classlist: 0x968
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x590

   __DATA_CONST.__objc_intobj: 0xcf0
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_doubleobj: 0x60
-  __DATA_CONST.__auth_got: 0xa10
+  __DATA_CONST.__auth_got: 0xa18
   __DATA_CONST.__got: 0x1378
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x29f78
-  __DATA.__objc_selrefs: 0xc660
-  __DATA.__objc_ivar: 0x20cc
+  __DATA.__objc_const: 0x2a0d0
+  __DATA.__objc_selrefs: 0xc720
+  __DATA.__objc_ivar: 0x20e8
   __DATA.__objc_data: 0x5e10
   __DATA.__lazy_load_got: 0x8
   __DATA.__data: 0x42c4

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 10179
-  Symbols:   938
-  CStrings:  16398
+  Functions: 10205
+  Symbols:   939
+  CStrings:  16456
 
Symbols:
+ _CSDeviceSupportsAlwaysListeningHeySiri
+ _dispatch_assert_queue_not$V2
- _CSIsXR
CStrings:
+ "#1QB"
+ "%s #stream CSAttSuruTCUGenerator DROP - invalid silenceStartTime=%f"
+ "%s #stream notifyClientUSE called with nil requestId — caller did not supply one. silenceStartTime=%f"
+ "%s #stream notifying client USE requestId: %@ silenceStartTime: %f s secondsFromEnd: %f s lastPacketIndex: %llu"
+ "%s Coordinator received audio anchor host time: %llu"
+ "%s Ignore SpkrId Score updates for HS/JS on communal/companion device without always-listening Hey Siri support"
+ "%s Invalid secure RTS replay request: type=%lld, dataPath=%{public}@"
+ "%s No speechEndHostTime for trpId: %@ (requestId: %@) — Processing Chime may not play"
+ "%s Routing Secure RTS Replay message to CSRaiseToSpeakAnalyzerExclave"
+ "%s Secure RTS Replay STOP request - cleanup will happen via second pass completion or timeout"
+ "%s Secure RTS Replay request: type=%lld, dataPath=%{public}@, useStitchedAudio=%d"
+ "%s Secure RTS Replay start is only supported on watchOS"
+ "%s Skipping NC inference for requestId %@: mitigation bypassed for this context"
+ "%s Stored silStart=%.3fs for trpId: %@"
+ "%s User selected multiphrase but current Siri language does not support the compact trigger; treating as HS only"
+ "%s requestId:%@, mhId:%@ recordCtx:%@ voiceTriggerInfo:%@ recordRoute:%@ isLinwoodEnabled:%d originatingDeviceType:%lu originatingDeviceSupportsAlwaysListeningHeySiri:%d"
+ "-[CSAttSiriSpeechPresenceCoordinator analyzer:didReceiveAudioAnchorHostTime:]"
+ "-[CSAttSiriTCUGenerator _forwardUserSpeakingEndToEndpointReceiverWithSilenceStartTime:]"
+ "-[CSAttSiriTurnMessageHandler _deliverTurnEndEvent:trpId:processedAudioDuration:trailingSilenceDurationMs:turnEndReason:runtimeType:]"
+ "-[CSAttSiriTurnMessageHandler registerSpeechPresenceCoordinator:]_block_invoke"
+ "-[CSAttSiriUresNode startUresRequestWithAudioRecordContext:forRequestId:mhId:voiceTriggerInfo:recordRoute:isLinwoodEnabled:originatingDeviceType:originatingDeviceSupportsAlwaysListeningHeySiri:]_block_invoke"
+ "-[CSAudioStreamConsumerServiceHandler notifyClientUserSpeakingEndForRequestId:silenceStartTime:]_block_invoke"
+ "-[CSAudioStreamProviderServiceHandler _prepareToStartNewStreamWithOption:audioRecordContext:voiceTriggerInfo:handoffInvocationType:]"
+ "-[CSClientXPCConnection _handleSecureRTSReplayMessage:messageBody:client:]"
+ "-[CSVoiceTriggerUserSelectedPhrase _isMultiPhrase:]"
+ "B36@0:8@16B24^@28"
+ "Q16@?0d8"
+ "Q32@0:8@16Q24"
+ "T@\"CSAttSiriSpeechPresenceCoordinator\",W,N,V_speechPresenceCoordinator"
+ "T@\"NSMutableArray\",&,N,V_packetEndSampleCounts"
+ "T@\"NSMutableDictionary\",&,N,V_perTRPSilStartMs"
+ "TB,N,V_originatingDeviceSupportsAlwaysListeningHeySiri"
+ "TQ,N,V_audioAnchorHostTime"
+ "Tq,N,V_handoffInvocationType"
+ "Tq,N,V_speechNoMatchSpeechEndAudioMs"
+ "_audioAnchorHostTime"
+ "_forwardUserSpeakingEndToEndpointReceiverWithSilenceStartTime:"
+ "_handleSecureRTSReplayMessage:messageBody:client:"
+ "_handoffInvocationType"
+ "_localeSupportsMultiPhrase"
+ "_originatingDeviceSupportsAlwaysListeningHeySiri"
+ "_packetEndSampleCounts"
+ "_packetIndexForSilenceStartTime:"
+ "_perTRPSilStartMs"
+ "_prepareToStartNewStreamWithOption:audioRecordContext:voiceTriggerInfo:handoffInvocationType:"
+ "_speechNoMatchSpeechEndAudioMs"
+ "analyzer:didReceiveAudioAnchorHostTime:"
+ "audioAnchorHostTime"
+ "dataPath"
+ "didPrepareRecognitionWithAudioContext:requestId:mhId:voiceTriggerInfo:recordRoute:isLinwoodEnabled:originatingDeviceType:originatingDeviceSupportsAlwaysListeningHeySiri:"
+ "handoffInvocationType"
+ "handoffInvocationTypeFromTriggerPhrase"
+ "initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:originatingDeviceType:originatingDeviceSupportsAlwaysListeningHeySiri:originatingDeviceInvocationType:"
+ "initWithCapacity:"
+ "notifyClientUserSpeakingEndForRequestId:silenceStartTime:"
+ "originatingDeviceInvocationType"
+ "originatingDeviceSupportsAlwaysListeningHeySiri"
+ "packetEndSampleCounts"
+ "perTRPSilStartMs"
+ "prepareToStartNewStreamWithOption:audioRecordContext:voiceTriggerInfo:handoffInvocationType:"
+ "registerSpeechPresenceCoordinator:"
+ "remoteDeviceInvocationType"
+ "setAudioAnchorHostTime:"
+ "setHandoffInvocationType:"
+ "setOriginatingDeviceSupportsAlwaysListeningHeySiri:"
+ "setPacketEndSampleCounts:"
+ "setPerTRPSilStartMs:"
+ "setRemoteDeviceInvocationType:"
+ "setSpeechNoMatchSpeechEndAudioMs:"
+ "speechEndHostTime"
+ "speechEndHostTimeForTRPId:turnEndReason:"
+ "speechNoMatchSpeechEndAudioMs"
+ "startSecureRTSReplay:useStitchedAudio:error:"
+ "startUresRequestWithAudioRecordContext:forRequestId:mhId:voiceTriggerInfo:recordRoute:isLinwoodEnabled:originatingDeviceType:originatingDeviceSupportsAlwaysListeningHeySiri:"
+ "tcuGenerator:didDetectUserSpeakingEndWithSilenceStartTime:"
+ "useStitchedAudio"
+ "v32@0:8@\"CSAttSiriSpeechPresenceAnalyzer\"16Q24"
+ "v48@0:8@16@24@32q40"
+ "v72@0:8@\"CSAudioRecordContext\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40@\"NSString\"48B56Q60B68"
+ "v72@0:8@16@24@32@40@48B56Q60B68"
- "#1r"
- "%s #stream CSAttSuruTCUGenerator DROP - invalid secondsFromEnd=%f"
- "%s #stream notifyClientUSE called with nil requestId — caller did not supply one. secondsFromEnd=%f"
- "%s #stream notifying client USE requestId: %@ secondsFromEnd: %f s lastPacketIndex: %llu"
- "%s Ignore SpkrId Score updates for HS/JS on communal device"
- "%s Skipping NC inference for requestId %@: UI button press on Vision Pro"
- "%s requestId:%@, mhId:%@ recordCtx:%@ voiceTriggerInfo:%@ recordRoute:%@ isLinwoodEnabled:%d originatingDeviceType:%lu"
- "(!"
- "-[CSAttSiriTCUGenerator _forwardUserSpeakingEndToEndpointReceiverWithSecondsFromEnd:]"
- "-[CSAttSiriUresNode startUresRequestWithAudioRecordContext:forRequestId:mhId:voiceTriggerInfo:recordRoute:isLinwoodEnabled:originatingDeviceType:]_block_invoke"
- "-[CSAudioStreamConsumerServiceHandler notifyClientUserSpeakingEndForRequestId:secondsFromEnd:]_block_invoke"
- "-[CSAudioStreamProviderServiceHandler _prepareToStartNewStreamWithOption:audioRecordContext:voiceTriggerInfo:]"
- "_forwardUserSpeakingEndToEndpointReceiverWithSecondsFromEnd:"
- "_prepareToStartNewStreamWithOption:audioRecordContext:voiceTriggerInfo:"
- "didPrepareRecognitionWithAudioContext:requestId:mhId:voiceTriggerInfo:recordRoute:isLinwoodEnabled:originatingDeviceType:"
- "initWithAudioRecordType:audioRecordDeviceId:recordRoute:audioFormat:streamIdentifier:originatingDeviceType:"
- "notifyClientUserSpeakingEndForRequestId:secondsFromEnd:"
- "prepareToStartNewStreamWithOption:audioRecordContext:voiceTriggerInfo:"
- "startUresRequestWithAudioRecordContext:forRequestId:mhId:voiceTriggerInfo:recordRoute:isLinwoodEnabled:originatingDeviceType:"
- "tcuGenerator:didDetectUserSpeakingEndWithSecondsFromEnd:"
- "v68@0:8@\"CSAudioRecordContext\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40@\"NSString\"48B56Q60"
- "v68@0:8@16@24@32@40@48B56Q60"
```
