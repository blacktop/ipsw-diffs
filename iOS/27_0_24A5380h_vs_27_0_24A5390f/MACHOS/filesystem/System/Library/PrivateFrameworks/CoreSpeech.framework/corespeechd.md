## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-3600.70.20.1.1
-  __TEXT.__text: 0x18652c
-  __TEXT.__auth_stubs: 0x1760
+3600.70.32.0.0
+  __TEXT.__text: 0x185700
+  __TEXT.__auth_stubs: 0x1700
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_stubs: 0x22940
-  __TEXT.__objc_methlist: 0x1bbfc
+  __TEXT.__objc_stubs: 0x22840
+  __TEXT.__objc_methlist: 0x1bce4
   __TEXT.__dlopen_cstrs: 0x31a
   __TEXT.__const: 0x3b0
-  __TEXT.__gcc_except_tab: 0x3274
-  __TEXT.__objc_methname: 0x47e93
-  __TEXT.__cstring: 0x3109c
-  __TEXT.__oslogstring: 0x27685
-  __TEXT.__objc_classname: 0x3928
-  __TEXT.__objc_methtype: 0x9713
-  __TEXT.__unwind_info: 0x6020
-  __DATA_CONST.__const: 0x6638
-  __DATA_CONST.__cfstring: 0x9700
+  __TEXT.__gcc_except_tab: 0x30e8
+  __TEXT.__objc_methname: 0x4806b
+  __TEXT.__cstring: 0x30fcb
+  __TEXT.__oslogstring: 0x27722
+  __TEXT.__objc_classname: 0x3948
+  __TEXT.__objc_methtype: 0x9791
+  __TEXT.__unwind_info: 0x6010
+  __DATA_CONST.__const: 0x64d8
+  __DATA_CONST.__cfstring: 0x9640
   __DATA_CONST.__objc_classlist: 0xa00
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x5b0
+  __DATA_CONST.__objc_protolist: 0x5b8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x830
-  __DATA_CONST.__objc_intobj: 0xd38
   __DATA_CONST.__objc_doubleobj: 0x80
+  __DATA_CONST.__objc_intobj: 0xd38
   __DATA_CONST.__objc_arraydata: 0x288
   __DATA_CONST.__objc_arrayobj: 0x168
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x5b0
-  __DATA_CONST.__auth_got: 0xbc8
+  __DATA_CONST.__auth_got: 0xb98
   __DATA_CONST.__got: 0x15c8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x2b9c8
-  __DATA.__objc_selrefs: 0xd128
-  __DATA.__objc_ivar: 0x21d0
+  __DATA.__objc_const: 0x2bab8
+  __DATA.__objc_selrefs: 0xd130
+  __DATA.__objc_ivar: 0x21e0
   __DATA.__objc_data: 0x6400
   __DATA.__lazy_load_got: 0x8
-  __DATA.__data: 0x4444
+  __DATA.__data: 0x44a4
   __DATA.__bss: 0x710
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 10557
-  Symbols:   1060
+  Functions: 10563
+  Symbols:   1054
   CStrings:  17377
 
Symbols:
+ _AVAudioSessionPortBuiltInMic
+ _CSIsWatchWithPHS
+ _NSStringFromLBRuntimeType
+ _OBJC_CLASS_$_CSRemoteAudioController
- _OBJC_CLASS_$_BMDictationUserEdit
- _XPC_ACTIVITY_INTERVAL_1_DAY
- _loadBookmark
- _objc_begin_catch
- _objc_end_catch
- _objc_exception_rethrow
- _objc_terminate
- _saveBookmark
- _xpc_activity_add_eligibility_changed_handler
- _xpc_activity_remove_eligibility_changed_handler
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
+ "-[CSIntuitiveConvRequestHandler _resolveAttendingDecisionWithRequestReset:]_block_invoke_2"
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
- "%s User Edit: BMDictatinoUserEdit reading completed successfully, saving bookmark"
- "%s User Edit: BMDictatinoUserEdit reading completed, saving bookmark"
- "%s User Edit: Deferred:%d"
- "%s User Edit: Error with confusion pair generation: %@"
- "%s User Edit: Started building"
- "%s User Edit: alignmentInfo: %@"
- "%s User Edit: eligibilityHandler deferred: %d"
- "%s User Edit: enumerating %luu event from Biome"
- "%s User Edit: failed to read from Biome, %@"
- "%s User Edit: generating confusion pairs with nbest result, n=%lu"
- "%s User Edit: process Biome event is successful, saving bookmark and logging edit events"
- "%s User Edit: xpc_transaction_exit_clean"
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
- "-[CSIntuitiveConvRequestHandler _handleClientDidStopWithOption:]_block_invoke_2"
- "-[CSIntuitiveConvRequestHandler handleTurnFinalizedForRequest:trpId:runtimeType:selectedRuntime:]_block_invoke"
- "-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke_2"
- "6\"12B"
- "B16@?0@\"BMStoreEvent\"8"
- "CSClassifyUserEdit"
- "CSClassifyUserEdit_block_invoke"
- "CSClassifyUserEdit_block_invoke_2"
- "T@\"<CSAudioStreamProviding>\",W,N,V_streamProvider"
- "TB,V_receivedUserTurnEnded"
- "TB,V_receivedUserTurnFinalized"
- "Td,N,V_firstAudioSampleSensorTimestamp"
- "UserEdit"
- "_holdAudioStream"
- "_receivedUserTurnEnded"
- "_receivedUserTurnFinalized"
- "_streamProvider"
- "alternativeSelections"
- "asrID"
- "com.apple.siri.speech-user-edit-classification"
- "com.apple.siri.xpc_activity.speech-user-edit"
- "drivableSinkWithBookmark:completion:shouldContinue:"
- "editMethod"
- "errorType"
- "isDictationUserEditClassificationEnabled"
- "originalText"
- "populateAlignmentInfo"
- "populateAlignmentInfo_block_invoke"
- "preItnNbest"
- "publisher"
- "receivedUserTurnEnded"
- "receivedUserTurnEnded:"
- "receivedUserTurnFinalized"
- "receivedUserTurnFinalized:"
- "recognizedText"
- "releaseAudioStreamHold"
- "replacementText"
- "sampling_rate"
- "setCSAudioStreamProviding:"
- "setReceivedUserTurnEnded:"
- "setReceivedUserTurnEnded:runtimeType:"
- "setReceivedUserTurnFinalized:"
- "setReceivedUserTurnFinalized:runtimeType:"
- "setStreamProvider:"
- "v24@?0@\"BPSCompletion\"8@\"<BMBookmark>\"16"
```
