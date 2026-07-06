## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-  __TEXT.__text: 0x18605c
-  __TEXT.__auth_stubs: 0x1750
+  __TEXT.__text: 0x18652c
+  __TEXT.__auth_stubs: 0x1760
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_stubs: 0x228a0
-  __TEXT.__objc_methlist: 0x1bc04
+  __TEXT.__objc_stubs: 0x22940
+  __TEXT.__objc_methlist: 0x1bbfc
   __TEXT.__dlopen_cstrs: 0x31a
   __TEXT.__const: 0x3b0
   __TEXT.__gcc_except_tab: 0x3274
-  __TEXT.__objc_methname: 0x47d34
-  __TEXT.__cstring: 0x31007
-  __TEXT.__oslogstring: 0x274ba
-  __TEXT.__objc_classname: 0x396d
-  __TEXT.__objc_methtype: 0x96d8
-  __TEXT.__unwind_info: 0x6018
-  __DATA_CONST.__const: 0x6678
-  __DATA_CONST.__cfstring: 0x9720
-  __DATA_CONST.__objc_classlist: 0xa08
+  __TEXT.__objc_methname: 0x47e93
+  __TEXT.__cstring: 0x3109c
+  __TEXT.__oslogstring: 0x27685
+  __TEXT.__objc_classname: 0x3928
+  __TEXT.__objc_methtype: 0x9713
+  __TEXT.__unwind_info: 0x6020
+  __DATA_CONST.__const: 0x6638
+  __DATA_CONST.__cfstring: 0x9700
+  __DATA_CONST.__objc_classlist: 0xa00
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x5b8
+  __DATA_CONST.__objc_protolist: 0x5b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x838
+  __DATA_CONST.__objc_superrefs: 0x830
   __DATA_CONST.__objc_intobj: 0xd38
   __DATA_CONST.__objc_doubleobj: 0x80
   __DATA_CONST.__objc_arraydata: 0x288
   __DATA_CONST.__objc_arrayobj: 0x168
   __DATA_CONST.__objc_dictobj: 0x348
   __DATA_CONST.__objc_floatobj: 0x5b0
-  __DATA_CONST.__auth_got: 0xbc0
-  __DATA_CONST.__got: 0x14c8
+  __DATA_CONST.__auth_got: 0xbc8
+  __DATA_CONST.__got: 0x15c8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x2bab0
-  __DATA.__objc_selrefs: 0xd0e8
+  __DATA.__objc_const: 0x2b9c8
+  __DATA.__objc_selrefs: 0xd128
   __DATA.__objc_ivar: 0x21d0
-  __DATA.__objc_data: 0x6450
+  __DATA.__objc_data: 0x6400
   __DATA.__lazy_load_got: 0x8
-  __DATA.__data: 0x44a4
-  __DATA.__bss: 0x720
+  __DATA.__data: 0x4444
+  __DATA.__bss: 0x710
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 10556
-  Symbols:   1058
-  CStrings:  18829
+  Functions: 10557
+  Symbols:   1060
+  CStrings:  18844
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_ivar : content changed
Symbols:
+ _LBSpeechRecognitionModeDescription
+ _OBJC_CLASS_$_CSPhraseSpotterEnabledMonitor
CStrings:
+ "%s Audio stream consuming during deferred teardown for requestId: %@ - ignore callback"
+ "%s Companion mode — disabling standalone processing for requestId: %@"
+ "%s DEBUG: _siriClientStream:%@, startStreamOption:%@, rootRequestId:%@, stopReason=%lu, supportsMagus=%d, _dismissedRequestId:%@, isDismissed=%d, _attendingDisabledRootRequestId:%@, isDisabled=%d, blockAttending=%d"
+ "%s defer to didProcessTRPCandidatePackage for sending trpCandidate when external signal is active"
+ "%s handle speechRecognition start with requestId: %@, mode: %{public}@"
+ "%s isRequestSampled:%d extraDelayMs:%.1f"
+ "%s requestId: %@, currentRequestId: %@"
+ "%s speechRecognitionMode = %{public}@; Force disabling local speech recognition"
+ "%s startCompanionRequestId: %@ — ignored: standaloneDisabled is NO"
+ "%s startCompanionRequestId: %@, standaloneDisabled: %d"
+ "%s startLogging for %@ called with previous file %@ in flight; forcing teardown"
+ "+[CSEndpointDetectedSelfLogger emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:collisionExtraDelayMs:]"
+ "-[CSAttSiriBridgeMessageHandler startCompanionRequestId:withStandaloneDisabled:inputOrigin:]"
+ "-[CSAttSiriSpeechPresenceMessageBuilder requestSampledForCollisionDetection:extraDelayMs:]"
+ "-[CSEndpointDetectedSelfLogger requestSampledForCollisionDetection:extraDelayMs:]_block_invoke"
+ "-[CSIntuitiveConvRequest releaseAudioStreamHold]"
+ "-[CSIntuitiveConvRequestHandler _handleStopProcessingForRequestId:requestEnded:]"
+ "-[CSIntuitiveConvRequestHandler handleExternallyTriggeredLinwoodRequestCancelled:]"
+ "Td,N,V_collisionExtraDelayMs"
+ "Vv36@0:8@\"NSString\"16B24@\"NSString\"28"
+ "Vv36@0:8@16B24@28"
+ "_collisionExtraDelayMs"
+ "_evaluateAsrEndTurnSignals"
+ "_evaluateNoTRPArrivalThreshold"
+ "_evaluateTrailingSilenceThresholds"
+ "_handleStopProcessingForRequestId:requestEnded:"
+ "_runDailyEuclidProfileMaintenance"
+ "_runDailyEuclidProfileMaintenance_block_invoke"
+ "_stopProcessingNodesIncludingAudioSrcNode:"
+ "blockAttending"
+ "collisionExtraDelayMs"
+ "companionSettingsWithRequestId:inputOrigin:"
+ "configureForRecordRoute:preferUseSelfTap:"
+ "emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:collisionExtraDelayMs:"
+ "handleExternallyTriggeredLinwoodRequestCancelled:"
+ "releaseAudioStreamHold"
+ "requestSampledForCollisionDetection:extraDelayMs:"
+ "setCollisionExtraDelayMs:"
+ "setExpectedDuration:"
+ "startCompanionRequestId:withStandaloneDisabled:inputOrigin:"
+ "v56@0:8@16q24@32@40d48"
- "%s DEBUG: _siriClientStream:%@, startStreamOption:%@, rootRequestId:%@, stopReason=%lu, supportsMagus=%d, _dismissedRequestId:%@, isDismissed=%d, _attendingDisabledRootRequestId:%@, isDisabled=%d, isRequestCancelled=%d"
- "%s Ignore TRP candidate package since external signal is active"
- "%s PhraseSpotter enabled = %{public}@"
- "%s PhraseSpotter is already %{public}@, received duplicated notification!"
- "%s handle speechRecognition start with requestId: %@"
- "+[CSEndpointDetectedSelfLogger emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:]"
- "-[CSAttSiriSpeechPresenceMessageBuilder requestSampledForCollisionDetection:]"
- "-[CSIntuitiveConvRequestHandler _handleStopProcessingForRequestId:]"
- "-[CSPhraseSpotterEnabledMonitor _checkPhraseSpotterEnabled]"
- "-[CSPhraseSpotterEnabledMonitor _phraseSpotterEnabledDidChange]"
- "CSPhraseSpotterEnabledMonitor"
- "CSPhraseSpotterEnabledMonitor:didReceiveEnabled:"
- "CSPhraseSpotterEnabledMonitorProviding"
- "_checkPhraseSpotterEnabled"
- "_didReceivePhraseSpotterSettingChangedInQueue:"
- "_evaluateThresholds"
- "_isPhraseSpotterEnabled"
- "_phraseSpotterEnabledDidChange"
- "_runDailyEuclidProfileMaintenanceWithPermitMonitor"
- "_runDailyEuclidProfileMaintenanceWithPermitMonitor_block_invoke"
- "configureForRecordRoute:"
- "emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:"
- "kVTPreferencesPhraseSpotterEnabledDidChangeDarwinNotification"
- "requestSampledForCollisionDetection:"
- "v48@0:8@16q24@32@40"

```
