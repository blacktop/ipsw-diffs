## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/CoreSpeech`

```diff

-  __TEXT.__text: 0x13bc74
+  __TEXT.__text: 0x13ba54
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x13ba8
+  __TEXT.__objc_methlist: 0x13bd8
   __TEXT.__const: 0x40c
   __TEXT.__dlopen_cstrs: 0x4e
   __TEXT.__gcc_except_tab: 0x30a4
-  __TEXT.__cstring: 0x25097
-  __TEXT.__oslogstring: 0x1dbb6
-  __TEXT.__unwind_info: 0x4a30
+  __TEXT.__cstring: 0x25071
+  __TEXT.__oslogstring: 0x1db84
+  __TEXT.__unwind_info: 0x4a20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd28
-  __DATA_CONST.__objc_classlist: 0x818
+  __DATA_CONST.__const: 0xd20
+  __DATA_CONST.__objc_classlist: 0x810
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x4a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xa370
+  __DATA_CONST.__objc_selrefs: 0xa3b8
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x638
+  __DATA_CONST.__objc_superrefs: 0x630
   __DATA_CONST.__objc_arraydata: 0x3f0
   __DATA_CONST.__got: 0x1868
-  __AUTH_CONST.__const: 0x5850
-  __AUTH_CONST.__cfstring: 0x9140
-  __AUTH_CONST.__objc_const: 0x1f3e0
+  __AUTH_CONST.__const: 0x5830
+  __AUTH_CONST.__cfstring: 0x9120
+  __AUTH_CONST.__objc_const: 0x1f328
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x900

   __AUTH_CONST.__objc_floatobj: 0x4d0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__auth_got: 0xc10
-  __AUTH.__objc_data: 0x3d40
-  __DATA.__objc_ivar: 0x17d0
+  __AUTH.__objc_data: 0x39d0
+  __DATA.__objc_ivar: 0x17cc
   __DATA.__data: 0x3774
-  __DATA.__bss: 0x5e0
+  __DATA.__bss: 0x5d0
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x13b0
+  __DATA_DIRTY.__objc_data: 0x16d0
   __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7687
-  Symbols:   17503
-  CStrings:  6298
+  Functions: 7682
+  Symbols:   17483
+  CStrings:  6294
 
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
+ GCC_except_table6770
+ GCC_except_table6806
+ GCC_except_table6857
+ GCC_except_table6912
+ GCC_except_table6935
+ GCC_except_table6976
+ GCC_except_table6986
+ GCC_except_table6996
+ GCC_except_table7037
+ GCC_except_table7065
+ GCC_except_table7114
+ GCC_except_table7205
+ GCC_except_table7206
+ GCC_except_table7207
+ GCC_except_table7208
+ GCC_except_table7209
+ GCC_except_table7278
+ GCC_except_table7326
+ GCC_except_table7332
+ GCC_except_table7335
+ GCC_except_table7343
+ GCC_except_table7349
+ GCC_except_table7374
+ GCC_except_table7380
+ GCC_except_table7386
+ GCC_except_table7518
+ OBJC_IVAR_$_CSEndpointDetectedSelfLogger._collisionExtraDelayMs
+ __79-[CSSiriSpeechRecorder _setupAudioFileWritingForSpeechController:info:context:]_block_invoke
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
- GCC_except_table6778
- GCC_except_table6814
- GCC_except_table6865
- GCC_except_table6920
- GCC_except_table6943
- GCC_except_table6984
- GCC_except_table6994
- GCC_except_table7004
- GCC_except_table7051
- GCC_except_table7071
- GCC_except_table7119
- GCC_except_table7210
- GCC_except_table7211
- GCC_except_table7212
- GCC_except_table7213
- GCC_except_table7219
- GCC_except_table7283
- GCC_except_table7331
- GCC_except_table7337
- GCC_except_table7340
- GCC_except_table7348
- GCC_except_table7354
- GCC_except_table7379
- GCC_except_table7385
- GCC_except_table7391
- GCC_except_table7523
- OBJC_IVAR_$_CSPhraseSpotterEnabledMonitor._isPhraseSpotterEnabled
- OBJC_IVAR_$_CSPhraseSpotterEnabledMonitor._notifyToken
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
