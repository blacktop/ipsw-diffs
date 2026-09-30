## SpeechTranslation

> `/System/Library/PrivateFrameworks/SpeechTranslation.framework/SpeechTranslation`

```diff

-341.0.0.0.0
-  __TEXT.__text: 0x22874
-  __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x1104
-  __TEXT.__const: 0x53c
-  __TEXT.__cstring: 0x11ba
-  __TEXT.__oslogstring: 0x24d5
+343.3.0.0.0
+  __TEXT.__text: 0x235a8
+  __TEXT.__auth_stubs: 0x1170
+  __TEXT.__objc_methlist: 0x122c
+  __TEXT.__const: 0x54c
+  __TEXT.__cstring: 0x11fa
+  __TEXT.__oslogstring: 0x2605
   __TEXT.__gcc_except_tab: 0x36c
   __TEXT.__constg_swiftt: 0x340
   __TEXT.__swift5_typeref: 0x43f

   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0x38
-  __TEXT.__unwind_info: 0x9d8
+  __TEXT.__unwind_info: 0xa18
   __TEXT.__eh_frame: 0x9f0
-  __TEXT.__objc_classname: 0x29b
-  __TEXT.__objc_methname: 0x2393
-  __TEXT.__objc_methtype: 0x9d4
-  __TEXT.__objc_stubs: 0x1880
-  __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x530
-  __DATA_CONST.__objc_classlist: 0xa8
+  __TEXT.__objc_classname: 0x2ce
+  __TEXT.__objc_methname: 0x26bb
+  __TEXT.__objc_methtype: 0xa16
+  __TEXT.__objc_stubs: 0x1b40
+  __DATA_CONST.__got: 0x360
+  __DATA_CONST.__const: 0x558
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x960
+  __DATA_CONST.__objc_selrefs: 0x9f0
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x8c0
-  __AUTH_CONST.__const: 0x598
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x8c8
+  __AUTH_CONST.__const: 0x5b8
   __AUTH_CONST.__cfstring: 0x3e0
-  __AUTH_CONST.__objc_const: 0x1fe0
-  __AUTH.__objc_data: 0x5a0
+  __AUTH_CONST.__objc_const: 0x22a8
+  __AUTH.__objc_data: 0x640
   __AUTH.__data: 0x5b8
-  __DATA.__objc_ivar: 0xac
+  __DATA.__objc_ivar: 0xcc
   __DATA.__data: 0x920
-  __DATA.__bss: 0x320
+  __DATA.__bss: 0x330
   __DATA.__common: 0x80
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3FDB2067-E28F-3A87-9344-F90B04D631FD
-  Functions: 729
-  Symbols:   1527
-  CStrings:  821
+  UUID: 5B85CC28-7B78-3CCF-97DD-3E7F224733A6
+  Functions: 761
+  Symbols:   1644
+  CStrings:  862
 
Symbols:
+ -[_STSELFLoggingClient .cxx_destruct]
+ -[_STSELFLoggingClient _endSessionWithError:]
+ -[_STSELFLoggingClient audioGenerationDidFinish]
+ -[_STSELFLoggingClient clientShouldDisconnect]
+ -[_STSELFLoggingClient didGenerateTranslatedAudio:]
+ -[_STSELFLoggingClient init]
+ -[_STSELFLoggingClient producedTranscription:]
+ -[_STSELFLoggingClient producedTranslation:]
+ -[_STSELFLoggingClient registerClientList:configuration:]
+ -[_STSELFLoggingClient translationDidPauseWithReason:]
+ -[_STSELFLoggingClient translationDidResume]
+ -[_STSELFLoggingClient translationDidStart]
+ -[_STSELFLoggingClient translationDidStopWithError:]
+ -[_STSELFLoggingClient willStartTranslatedAudioWithMetadata:]
+ -[_STSELFLoggingSession .cxx_destruct]
+ -[_STSELFLoggingSession initWithLocalePair:]
+ -[_STSELFLoggingSession localePair]
+ -[_STSELFLoggingSession logSessionEnd:]
+ -[_STSELFLoggingSession logSessionStart]
+ -[_STSELFLoggingSession logSessionStart].cold.1
+ -[_STSELFLoggingSession setTtsPlaybackEnabled:]
+ -[_STSELFLoggingSession ttsPlaybackEnabled]
+ -[_STSpeechTranslatorClientList delegate]
+ -[_STSpeechTranslatorClientList setDelegate:]
+ _OBJC_CLASS_$__LTSELFLoggingEventData
+ _OBJC_CLASS_$__LTSELFLoggingInvocationOptions
+ _OBJC_CLASS_$__LTSELFLoggingTranslateAppContext
+ _OBJC_CLASS_$__LTTranslator
+ _OBJC_CLASS_$__STSELFLoggingClient
+ _OBJC_CLASS_$__STSELFLoggingSession
+ _OBJC_IVAR_$__STSELFLoggingClient._loggingQueue
+ _OBJC_IVAR_$__STSELFLoggingClient._ongoingSession
+ _OBJC_IVAR_$__STSELFLoggingSession._isActive
+ _OBJC_IVAR_$__STSELFLoggingSession._localePair
+ _OBJC_IVAR_$__STSELFLoggingSession._sessionID
+ _OBJC_IVAR_$__STSELFLoggingSession._ttsPlaybackEnabled
+ _OBJC_IVAR_$__STSpeechTranslatorClientList._delegate
+ _OBJC_IVAR_$__STSpeechTranslatorManager._selfClient
+ _OBJC_METACLASS_$__STSELFLoggingClient
+ _OBJC_METACLASS_$__STSELFLoggingSession
+ __LTOSLogSTInstrumentation
+ __LTOSLogSTInstrumentation.cold.1
+ __LTOSLogSTInstrumentation.log
+ __LTOSLogSTInstrumentation.onceToken
+ __OBJC_$_INSTANCE_METHODS__STSELFLoggingClient
+ __OBJC_$_INSTANCE_METHODS__STSELFLoggingSession
+ __OBJC_$_INSTANCE_VARIABLES__STSELFLoggingClient
+ __OBJC_$_INSTANCE_VARIABLES__STSELFLoggingSession
+ __OBJC_$_PROP_LIST__STSELFLoggingClient
+ __OBJC_$_PROP_LIST__STSELFLoggingSession
+ __OBJC_CLASS_PROTOCOLS_$__STSELFLoggingClient
+ __OBJC_CLASS_RO_$__STSELFLoggingClient
+ __OBJC_CLASS_RO_$__STSELFLoggingSession
+ __OBJC_METACLASS_RO_$__STSELFLoggingClient
+ __OBJC_METACLASS_RO_$__STSELFLoggingSession
+ __PROTOCOLS_STTranscriptionResult.15
+ __PROTOCOLS_STTranslationResult.19
+ ___43-[_STSELFLoggingClient translationDidStart]_block_invoke
+ ___45-[_STSELFLoggingClient _endSessionWithError:]_block_invoke
+ ___57-[_STSELFLoggingClient registerClientList:configuration:]_block_invoke
+ ___57-[_STSELFLoggingClient registerClientList:configuration:]_block_invoke.cold.1
+ ___57-[_STSELFLoggingClient registerClientList:configuration:]_block_invoke.cold.2
+ ____LTOSLogSTInstrumentation_block_invoke
+ ___block_descriptor_56_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_literal_global.4
+ _objc_msgSend$UUIDString
+ _objc_msgSend$_endSessionWithError:
+ _objc_msgSend$_ltLocaleIdentifier
+ _objc_msgSend$delegate
+ _objc_msgSend$initWithDisplayMode:localePair:isGenderAlternativeEnabled:tabName:tabSessionId:conversationTabView:isPlayTranslationsEnabled:autoTranslateSessionId:audioChannel:languageIdentificationEnabled:
+ _objc_msgSend$initWithLocalePair:
+ _objc_msgSend$initWithSourceLocale:targetLocale:
+ _objc_msgSend$initWithTask:inputMode:invocationType:translateAppContext:
+ _objc_msgSend$initWithType:invocationId:
+ _objc_msgSend$isBidirectionalEqual:
+ _objc_msgSend$localePair
+ _objc_msgSend$logSessionEnd:
+ _objc_msgSend$logSessionStart
+ _objc_msgSend$omitTranslatedAudio
+ _objc_msgSend$registerClientList:configuration:
+ _objc_msgSend$selfLoggingEventWithData:
+ _objc_msgSend$setInvocationEndedError:
+ _objc_msgSend$setStartInvocationOptions:
+ _objc_msgSend$setTranslationLocalePair:
+ _objc_msgSend$setTtsPlaybackEnabled:
+ _objc_msgSend$targetLocale
+ _objc_msgSend$ttsPlaybackEnabled
+ _objectdestroy.44Tm
- __PROTOCOLS_STTranscriptionResult.19
- __PROTOCOLS_STTranslationResult.23
- _objectdestroy.48Tm
CStrings:
+ "@\"_LTLocalePair\""
+ "@\"_STSELFLoggingClient\""
+ "@\"_STSELFLoggingSession\""
+ "Additional client list doesn't match language of ongoing logging session"
+ "Additional client list for ongoing session ignored."
+ "Creating new logging session with languages: %{public}@ - %{public}@"
+ "Register new client list for instrumentation observation"
+ "STInstrumentation"
+ "Send new invocation event for session ID: %{public}@"
+ "T@\"<_STSpeechTranslatorClientConforming>\",W,N,V_delegate"
+ "T@\"_LTLocalePair\",R,N,V_localePair"
+ "TB,N,V_ttsPlaybackEnabled"
+ "UUIDString"
+ "_STSELFLoggingClient"
+ "_STSELFLoggingSession"
+ "_endSessionWithError:"
+ "_isActive"
+ "_localePair"
+ "_loggingQueue"
+ "_ltLocaleIdentifier"
+ "_ongoingSession"
+ "_selfClient"
+ "_sessionID"
+ "_ttsPlaybackEnabled"
+ "com.apple.SpeechTranslation.Instrumentation"
+ "initWithDisplayMode:localePair:isGenderAlternativeEnabled:tabName:tabSessionId:conversationTabView:isPlayTranslationsEnabled:autoTranslateSessionId:audioChannel:languageIdentificationEnabled:"
+ "initWithLocalePair:"
+ "initWithTask:inputMode:invocationType:translateAppContext:"
+ "initWithType:invocationId:"
+ "isBidirectionalEqual:"
+ "localePair"
+ "logSessionEnd:"
+ "logSessionStart"
+ "registerClientList:configuration:"
+ "selfLoggingEventWithData:"
+ "setInvocationEndedError:"
+ "setStartInvocationOptions:"
+ "setTranslationLocalePair:"
+ "setTtsPlaybackEnabled:"
+ "ttsPlaybackEnabled"
+ "\xa1"

```
