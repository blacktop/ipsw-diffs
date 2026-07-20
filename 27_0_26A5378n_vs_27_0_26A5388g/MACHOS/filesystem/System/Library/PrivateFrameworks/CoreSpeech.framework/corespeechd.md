## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-3600.70.20.4.1
-  __TEXT.__text: 0x17a144
-  __TEXT.__auth_stubs: 0x13d0
+3600.70.32.0.0
+  __TEXT.__text: 0x17b1bc
+  __TEXT.__auth_stubs: 0x13f0
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_stubs: 0x20720
-  __TEXT.__objc_methlist: 0x1ac28
+  __TEXT.__objc_stubs: 0x20840
+  __TEXT.__objc_methlist: 0x1ad10
   __TEXT.__const: 0x368
   __TEXT.__dlopen_cstrs: 0x126
   __TEXT.__gcc_except_tab: 0x2cc0
-  __TEXT.__cstring: 0x2dd9e
-  __TEXT.__objc_methname: 0x44887
-  __TEXT.__oslogstring: 0x25a15
-  __TEXT.__objc_classname: 0x3709
-  __TEXT.__objc_methtype: 0x8be5
-  __TEXT.__unwind_info: 0x59a8
-  __DATA_CONST.__const: 0x62a8
-  __DATA_CONST.__cfstring: 0x87c0
+  __TEXT.__cstring: 0x2de77
+  __TEXT.__objc_methname: 0x44b4d
+  __TEXT.__oslogstring: 0x25d27
+  __TEXT.__objc_classname: 0x3729
+  __TEXT.__objc_methtype: 0x8c63
+  __TEXT.__unwind_info: 0x59d0
+  __DATA_CONST.__const: 0x6278
+  __DATA_CONST.__cfstring: 0x87a0
   __DATA_CONST.__objc_classlist: 0x968
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x588
+  __DATA_CONST.__objc_protolist: 0x590
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x7b0
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_floatobj: 0x590
-  __DATA_CONST.__objc_intobj: 0xcd8
+  __DATA_CONST.__objc_intobj: 0xcf0
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_doubleobj: 0x60
-  __DATA_CONST.__auth_got: 0xa00
-  __DATA_CONST.__got: 0x1368
+  __DATA_CONST.__auth_got: 0xa10
+  __DATA_CONST.__got: 0x1378
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x29e88
-  __DATA.__objc_selrefs: 0xc5f0
-  __DATA.__objc_ivar: 0x20bc
+  __DATA.__objc_const: 0x29f78
+  __DATA.__objc_selrefs: 0xc660
+  __DATA.__objc_ivar: 0x20cc
   __DATA.__objc_data: 0x5e10
   __DATA.__lazy_load_got: 0x8
-  __DATA.__data: 0x4264
+  __DATA.__data: 0x42c4
   __DATA.__bss: 0x628
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 10160
-  Symbols:   934
-  CStrings:  16363
+  Functions: 10179
+  Symbols:   938
+  CStrings:  16398
 
Symbols:
+ _AVAudioSessionPortBuiltInMic
+ _CSIsWatchWithPHS
+ _NSStringFromLBRuntimeType
+ _OBJC_CLASS_$_CSRemoteAudioController
CStrings:
+ "%s #stream Audio streaming stopping"
+ "%s #stream Client stopped streaming"
+ "%s Ignore SpkrId Score updates for HS/JS on communal device"
+ "%s Re-anchored audio start to exclave sampleCount %llu via hostTime %llu"
+ "%s RuntimeFinalizedContext: %@"
+ "%s _handleClientDidStopWithOption; shouldStartAttending: %{public}@, shouldStartAttendingAtUserTurnEnded: %{public}@, receivedSelectedRuntimeFinalized: %{public}@"
+ "%s client stop after runtime finalized; resolving attending decision"
+ "%s handleRuntimeFinalizedForRequest; called for inactive runtime (%@). Bail out!"
+ "%s received a runtimeFinalized for both the standalone and companion, but neither runtime was selected!"
+ "%s received requestId:%@ for runtime %{public}@ doesn't match current requestId:%@. Bail out!"
+ "%s received requestId:%@ for runtime %{public}@ doesn't match the current request:%@. Bail out!"
+ "%s requestId %@, trpId: %@, runtimeType: %{public}@, selectedRuntime: %{public}@, attendingDecisionReceived: %{public}@, _startAttendingSampleCount: %lld"
+ "%s requestId: %@, trpId: %@, attendingModePreference: %i, runtimeType: %{public}@"
+ "%s requestId: %@, trpId: %@, turnEndReason: %i, runtimeType: %{public}@, shouldStartAttendingAtUserTurnEnded: %{public}@"
+ "%s rootRequestId : %@, shouldStartAttending : %{public}@"
+ "%s rootRequestId: %@, shouldStartAttending: %{public}@, _startAttendingSampleCount: %lld"
+ "%s runtime finalized before client stop; deferring attending decision to client stop"
+ "%s scdaContext = %@"
+ "%s shouldStartAttending: %d"
+ "%s trpId:%@ lastTransitionTimeMs: %f, trailingSilenceDurationMs:%f, turnEndReason:%lu, runtimeType:%{public}@"
+ "%s turnMessageHandler update requestId: %@ for runtimeType: %{public}@"
+ "%s voiceTriggerInfo[\"%@\"] was not set, scdaContext will not have a value for this property."
+ "-[CSAttSiriBridgeMessageHandler runtimeFinalizedwithContext:]"
+ "-[CSAttSiriTurnMessageHandler runtimeFinalizedwithContext:]_block_invoke"
+ "-[CSAudioStreamProviderServiceHandler _stopStreamingWithCompletion:]"
+ "-[CSIntuitiveConvRequest setShouldStartAttending:]"
+ "-[CSIntuitiveConvRequestHandler _resolveAttendingDecisionWithRequestReset:]"
+ "-[CSIntuitiveConvRequestHandler handleRuntimeFinalizedForRequest:trpId:runtimeType:selectedRuntime:]_block_invoke"
+ "@\"CSRemoteAudioController\""
+ "CSRemoteAudioControllerDelegate"
+ "T@\"CSRemoteAudioController\",&,N,V_remoteAudioController"
+ "T@\"NSString\",&,N,V_recordRoute"
+ "TB,N,V_recordingFromExclave"
+ "TB,V_receivedRuntimeFinalized"
+ "TB,V_shouldIgnoreLocalVoiceTriggerActivation"
+ "Vv24@0:8@\"LBLocalSpeechRecognizerRuntimeFinalizedContext\"16"
+ "_attendingDecisionReceived"
+ "_deliverRuntimeFinalizedEvent:trpId:runtimeType:selectedRuntime:"
+ "_handleClientStoppedStreaming"
+ "_receivedRuntimeFinalized"
+ "_receivedSelectedRuntimeFinalized"
+ "_recordingFromExclave"
+ "_remoteAudioController"
+ "_resolveAttendingDecisionWithRequestReset:"
+ "_shouldIgnoreLocalVoiceTriggerActivation"
+ "_shouldStartAttending"
+ "_startRemoteAudioControllerIfNeeded"
+ "_stopStreamingWithCompletion:"
+ "attendingDecisionReceived"
+ "audioStartHostTime"
+ "handleRuntimeFinalizedForRequest:trpId:runtimeType:selectedRuntime:"
+ "initWithProviderSelector:"
+ "receivedRuntimeFinalized"
+ "receivedRuntimeFinalized:"
+ "receivedSelectedRuntimeFinalized"
+ "recordingFromExclave"
+ "remoteAudioController"
+ "remoteAudioController:didChangeReadiness:"
+ "runtimeFinalizedwithContext:"
+ "setReceivedRuntimeFinalized:"
+ "setReceivedRuntimeFinalized:runtimeType:"
+ "setReceivedSelectedRuntimeFinalized:"
+ "setRecordingFromExclave:"
+ "setRemoteAudioController:"
+ "setShouldIgnoreLocalVoiceTriggerActivation:"
+ "setShouldStartAttending:"
+ "shouldIgnoreLocalVoiceTriggerActivation"
+ "shouldStartAttending"
+ "stopStreamingWithCompletion:"
+ "v28@0:8@\"CSRemoteAudioController\"16B24"
- "%s _handleClientDidStopWithOption; shouldStartAttending: %i"
- "%s handleTurnFinalizedForRequest; called for inactive runtime (%i). Bail out!"
- "%s received a userTurnFinalized for both the standalone and companion, but neither runtime was selected!"
- "%s received requestId:%@ for runtime %i doesn't match current requestId:%@. Bail out!"
- "%s received requestId:%@ for runtime %i doesn't match the current request:%@. Bail out!"
- "%s requestId %@, trpId: %@, runtimeType: %i, selectedRuntime: %i, shouldStartAttending: %i, _startAttendingSampleCount: %lld"
- "%s requestId: %@, trpId: %@, attendingModePreference: %i, runtimeType: %i"
- "%s requestId: %@, trpId: %@, turnEndReason: %i, runtimeType: %i, shouldStartAttendingAtUserTurnEnded: %i"
- "%s rootRequestId : %@, shouldStartAttending : %@"
- "%s streamProvider is not set!"
- "%s trpId:%@ lastTransitionTimeMs: %f, trailingSilenceDurationMs:%f, turnEndReason:%lu, runtimeType:%lu"
- "%s turnMessageHandler update requestId: %@ for runtimeType: %i"
- "-[CSIntuitiveConvRequest _holdAudioStream]"
- "-[CSIntuitiveConvRequest releaseAudioStreamHold]"
- "-[CSIntuitiveConvRequestHandler handleTurnFinalizedForRequest:trpId:runtimeType:selectedRuntime:]_block_invoke"
- "6\"12B"
- "T@\"<CSAudioStreamProviding>\",W,N,V_streamProvider"
- "TB,V_receivedUserTurnEnded"
- "TB,V_receivedUserTurnFinalized"
- "Td,N,V_firstAudioSampleSensorTimestamp"
- "_holdAudioStream"
- "_receivedUserTurnEnded"
- "_receivedUserTurnFinalized"
- "_streamProvider"
- "receivedUserTurnEnded"
- "receivedUserTurnEnded:"
- "receivedUserTurnFinalized"
- "receivedUserTurnFinalized:"
- "releaseAudioStreamHold"
- "setCSAudioStreamProviding:"
- "setReceivedUserTurnEnded:"
- "setReceivedUserTurnEnded:runtimeType:"
- "setReceivedUserTurnFinalized:"
- "setReceivedUserTurnFinalized:runtimeType:"
- "setStreamProvider:"
```
