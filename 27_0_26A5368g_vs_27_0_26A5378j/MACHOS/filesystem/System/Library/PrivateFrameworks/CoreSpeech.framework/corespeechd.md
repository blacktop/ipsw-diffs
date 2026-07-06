## corespeechd

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/corespeechd`

```diff

-  __TEXT.__text: 0x179cdc
-  __TEXT.__auth_stubs: 0x13c0
+  __TEXT.__text: 0x17a144
+  __TEXT.__auth_stubs: 0x13d0
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_stubs: 0x206a0
+  __TEXT.__objc_stubs: 0x20720
   __TEXT.__objc_methlist: 0x1ac28
   __TEXT.__const: 0x368
   __TEXT.__dlopen_cstrs: 0x126
   __TEXT.__gcc_except_tab: 0x2cc0
-  __TEXT.__cstring: 0x2dce7
-  __TEXT.__objc_methname: 0x4473d
-  __TEXT.__oslogstring: 0x2584a
-  __TEXT.__objc_classname: 0x374e
-  __TEXT.__objc_methtype: 0x8baa
-  __TEXT.__unwind_info: 0x59a0
-  __DATA_CONST.__const: 0x62c8
-  __DATA_CONST.__cfstring: 0x87e0
-  __DATA_CONST.__objc_classlist: 0x970
+  __TEXT.__cstring: 0x2dd9e
+  __TEXT.__objc_methname: 0x44887
+  __TEXT.__oslogstring: 0x25a15
+  __TEXT.__objc_classname: 0x3709
+  __TEXT.__objc_methtype: 0x8be5
+  __TEXT.__unwind_info: 0x59a8
+  __DATA_CONST.__const: 0x62a8
+  __DATA_CONST.__cfstring: 0x87c0
+  __DATA_CONST.__objc_classlist: 0x968
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x590
+  __DATA_CONST.__objc_protolist: 0x588
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA_CONST.__objc_superrefs: 0x7b8
+  __DATA_CONST.__objc_superrefs: 0x7b0
   __DATA_CONST.__objc_arraydata: 0x240
   __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_floatobj: 0x590
   __DATA_CONST.__objc_intobj: 0xcd8
   __DATA_CONST.__objc_arrayobj: 0x150
   __DATA_CONST.__objc_doubleobj: 0x60
-  __DATA_CONST.__auth_got: 0x9f8
-  __DATA_CONST.__got: 0x1280
+  __DATA_CONST.__auth_got: 0xa00
+  __DATA_CONST.__got: 0x1368
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x29f70
-  __DATA.__objc_selrefs: 0xc5b8
+  __DATA.__objc_const: 0x29e88
+  __DATA.__objc_selrefs: 0xc5f0
   __DATA.__objc_ivar: 0x20bc
-  __DATA.__objc_data: 0x5e60
+  __DATA.__objc_data: 0x5e10
   __DATA.__lazy_load_got: 0x8
-  __DATA.__data: 0x42c4
-  __DATA.__bss: 0x638
+  __DATA.__data: 0x4264
+  __DATA.__bss: 0x628
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 10159
-  Symbols:   932
-  CStrings:  17680
+  Functions: 10160
+  Symbols:   934
+  CStrings:  17694
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
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
- "configureForRecordRoute:"
- "emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:"
- "kVTPreferencesPhraseSpotterEnabledDidChangeDarwinNotification"
- "requestSampledForCollisionDetection:"
- "v48@0:8@16q24@32@40"

```
