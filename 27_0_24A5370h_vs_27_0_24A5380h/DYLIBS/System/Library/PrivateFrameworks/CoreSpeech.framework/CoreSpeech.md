## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-  __TEXT.__text: 0x149b80
+  __TEXT.__text: 0x149944
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x14bec
+  __TEXT.__objc_methlist: 0x14c1c
   __TEXT.__const: 0x42c
   __TEXT.__dlopen_cstrs: 0x1e0
   __TEXT.__gcc_except_tab: 0x3140
-  __TEXT.__cstring: 0x28a0d
-  __TEXT.__oslogstring: 0x1fd55
-  __TEXT.__unwind_info: 0x4f28
+  __TEXT.__cstring: 0x289e7
+  __TEXT.__oslogstring: 0x1fd23
+  __TEXT.__unwind_info: 0x4f18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4268
-  __DATA_CONST.__objc_classlist: 0x848
+  __DATA_CONST.__const: 0x4260
+  __DATA_CONST.__objc_classlist: 0x840
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x4e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xad00
+  __DATA_CONST.__objc_selrefs: 0xad48
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x680
+  __DATA_CONST.__objc_superrefs: 0x678
   __DATA_CONST.__objc_arraydata: 0x3e8
   __DATA_CONST.__got: 0x1b18
-  __AUTH_CONST.__const: 0x1e60
-  __AUTH_CONST.__cfstring: 0x9680
-  __AUTH_CONST.__objc_const: 0x20cd8
+  __AUTH_CONST.__const: 0x1e40
+  __AUTH_CONST.__cfstring: 0x9660
+  __AUTH_CONST.__objc_const: 0x20c20
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x9a8

   __AUTH_CONST.__objc_floatobj: 0x4f0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0xda0
-  __AUTH.__objc_data: 0x3f20
-  __DATA.__objc_ivar: 0x1940
+  __AUTH.__objc_data: 0x3b10
+  __DATA.__objc_ivar: 0x193c
   __DATA.__data: 0x3a14
-  __DATA.__bss: 0x678
+  __DATA.__bss: 0x660
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x13b0
+  __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__bss: 0x158
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8087
-  Symbols:   26615
-  CStrings:  6781
+  Functions: 8082
+  Symbols:   26590
+  CStrings:  6777
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__lazy_load_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[CSEndpointDetectedSelfLogger emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:collisionExtraDelayMs:]
+ -[CSEndpointDetectedSelfLogger collisionExtraDelayMs]
+ -[CSEndpointDetectedSelfLogger requestSampledForCollisionDetection:extraDelayMs:]
+ -[CSEndpointDetectedSelfLogger setCollisionExtraDelayMs:]
+ -[CSSiriSpeechRecorder _stopRecordingWithReason:hostTime:blockAttending:]
+ -[CSSiriSpeechRecorder stopSpeechCaptureForEvent:suppressAlert:hostTime:blockAttending:]
+ GCC_except_table7112
+ GCC_except_table7148
+ GCC_except_table7221
+ GCC_except_table7275
+ GCC_except_table7298
+ GCC_except_table7339
+ GCC_except_table7350
+ GCC_except_table7493
+ GCC_except_table7501
+ GCC_except_table7617
+ GCC_except_table7618
+ GCC_except_table7619
+ GCC_except_table7620
+ GCC_except_table7621
+ GCC_except_table7689
+ GCC_except_table7735
+ GCC_except_table7743
+ GCC_except_table7749
+ GCC_except_table7774
+ GCC_except_table7780
+ GCC_except_table7786
+ GCC_except_table7924
+ _OBJC_IVAR_$_CSEndpointDetectedSelfLogger._collisionExtraDelayMs
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAttSiriSpeechPresenceCoordinatorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAttSiriSpeechPresenceCoordinatorDelegate
+ __OBJC_$_PROTOCOL_REFS_CSAttSiriSpeechPresenceCoordinatorDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSAttSiriSpeechPresenceCoordinatorDelegate
+ __OBJC_PROTOCOL_$_CSAttSiriSpeechPresenceCoordinatorDelegate
+ ___73-[CSSiriSpeechRecorder _stopRecordingWithReason:hostTime:blockAttending:]_block_invoke
+ ___81-[CSEndpointDetectedSelfLogger requestSampledForCollisionDetection:extraDelayMs:]_block_invoke
+ _objc_msgSend$_stopRecordingWithReason:hostTime:blockAttending:
+ _objc_msgSend$emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:collisionExtraDelayMs:
+ _objc_msgSend$initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:blockAttending:
+ _objc_msgSend$recordedAudioAvailableAt:requestId:filenamePostfix:completion:
+ _objc_msgSend$stopSpeechCaptureForEvent:suppressAlert:hostTime:blockAttending:
- +[CSEndpointDetectedSelfLogger emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:]
- +[CSPhraseSpotterEnabledMonitor sharedInstance]
- -[CSPhraseSpotterEnabledMonitor _checkPhraseSpotterEnabled]
- -[CSPhraseSpotterEnabledMonitor _didReceivePhraseSpotterSettingChangedInQueue:]
- -[CSPhraseSpotterEnabledMonitor _notifyObserver:withEnabled:]
- -[CSPhraseSpotterEnabledMonitor _phraseSpotterEnabledDidChange]
- -[CSPhraseSpotterEnabledMonitor _startMonitoringWithQueue:]
- -[CSPhraseSpotterEnabledMonitor _stopMonitoring]
- -[CSPhraseSpotterEnabledMonitor init]
- -[CSPhraseSpotterEnabledMonitor isEnabled]
- GCC_except_table7120
- GCC_except_table7156
- GCC_except_table7229
- GCC_except_table7283
- GCC_except_table7306
- GCC_except_table7347
- GCC_except_table7358
- GCC_except_table7498
- GCC_except_table7506
- GCC_except_table7622
- GCC_except_table7623
- GCC_except_table7624
- GCC_except_table7625
- GCC_except_table7631
- GCC_except_table7694
- GCC_except_table7740
- GCC_except_table7748
- GCC_except_table7754
- GCC_except_table7779
- GCC_except_table7785
- GCC_except_table7791
- GCC_except_table7929
- _OBJC_IVAR_$_CSPhraseSpotterEnabledMonitor._isPhraseSpotterEnabled
- _OBJC_IVAR_$_CSPhraseSpotterEnabledMonitor._notifyToken
- _OBJC_METACLASS_$_CSPhraseSpotterEnabledMonitor
- __OBJC_$_CLASS_METHODS_CSPhraseSpotterEnabledMonitor
- __OBJC_$_INSTANCE_METHODS_CSPhraseSpotterEnabledMonitor
- __OBJC_$_INSTANCE_VARIABLES_CSPhraseSpotterEnabledMonitor
- __OBJC_$_PROP_LIST_CSPhraseSpotterEnabledMonitor
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhraseSpotterEnabledMonitorProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhraseSpotterEnabledMonitorProviding
- __OBJC_$_PROTOCOL_REFS_CSPhraseSpotterEnabledMonitorProviding
- __OBJC_CLASS_PROTOCOLS_$_CSPhraseSpotterEnabledMonitor
- __OBJC_CLASS_RO_$_CSPhraseSpotterEnabledMonitor
- __OBJC_LABEL_PROTOCOL_$_CSPhraseSpotterEnabledMonitorProviding
- __OBJC_METACLASS_RO_$_CSPhraseSpotterEnabledMonitor
- __OBJC_PROTOCOL_$_CSPhraseSpotterEnabledMonitorProviding
- __PhraseSpotterEnabledDidChange
- ___47+[CSPhraseSpotterEnabledMonitor sharedInstance]_block_invoke
- ___58-[CSSiriSpeechRecorder _stopRecordingWithReason:hostTime:]_block_invoke
- ___79-[CSPhraseSpotterEnabledMonitor _didReceivePhraseSpotterSettingChangedInQueue:]_block_invoke
- _kCSPhraseSpotterEnabledDidChangeDarwinNotification
- _objc_msgSend$CSPhraseSpotterEnabledMonitor:didReceiveEnabled:
- _objc_msgSend$_checkPhraseSpotterEnabled
- _objc_msgSend$_didReceivePhraseSpotterSettingChangedInQueue:
- _objc_msgSend$_phraseSpotterEnabledDidChange
- _objc_msgSend$emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:
- _objc_msgSend$initWithStopRecordingReason:expectedStopHostTime:trailingSilenceDurationAtEndpoint:holdRequest:supportsMagus:
- _objc_msgSend$recordedAudioAvailableAt:requestId:filenamePostfix:
CStrings:
+ "%s (event = %ld, suppressAlert = %d, hostTime = %llu, blockAttending = %d)"
+ "%s isRequestSampled:%d extraDelayMs:%.1f"
+ "+[CSEndpointDetectedSelfLogger emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:collisionExtraDelayMs:]"
+ "-[CSEndpointDetectedSelfLogger requestSampledForCollisionDetection:extraDelayMs:]_block_invoke"
+ "-[CSSiriSpeechRecorder _stopRecordingWithReason:hostTime:blockAttending:]"
+ "-[CSSiriSpeechRecorder stopSpeechCaptureForEvent:suppressAlert:hostTime:blockAttending:]"
- "%s (event = %ld, suppressAlert = %d, hostTime = %llu)"
- "%s PhraseSpotter enabled = %{public}@"
- "%s PhraseSpotter is already %{public}@, received duplicated notification!"
- "+[CSEndpointDetectedSelfLogger emitEndpointDetectedEventWithEndpointerMetrics:eventType:trpId:mhId:]"
- "-[CSPhraseSpotterEnabledMonitor _checkPhraseSpotterEnabled]"
- "-[CSPhraseSpotterEnabledMonitor _phraseSpotterEnabledDidChange]"
- "-[CSSiriSpeechRecorder _stopRecordingWithReason:hostTime:]"
- "-[CSSiriSpeechRecorder stopSpeechCaptureForEvent:suppressAlert:hostTime:]"
- "kVTPreferencesPhraseSpotterEnabledDidChangeDarwinNotification"

```
