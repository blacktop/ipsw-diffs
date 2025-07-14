## SiriUIFoundation

> `/System/Library/PrivateFrameworks/SiriUIFoundation.framework/SiriUIFoundation`

```diff

-3302.13.3.1.1
-  __TEXT.__text: 0x247f8
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x283c
+3304.61.1.0.0
+  __TEXT.__text: 0x2b774
+  __TEXT.__auth_stubs: 0x6d0
+  __TEXT.__objc_methlist: 0x2b6c
   __TEXT.__const: 0x8c
-  __TEXT.__cstring: 0x36c7
-  __TEXT.__oslogstring: 0x1e4b
-  __TEXT.__gcc_except_tab: 0x494
+  __TEXT.__cstring: 0x3f51
+  __TEXT.__oslogstring: 0x29de
+  __TEXT.__gcc_except_tab: 0x61c
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0xb64
-  __TEXT.__objc_classname: 0x654
-  __TEXT.__objc_methname: 0x8c88
-  __TEXT.__objc_methtype: 0x114b
-  __TEXT.__objc_stubs: 0x5e40
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0xfd8
-  __DATA_CONST.__objc_classlist: 0x180
+  __TEXT.__unwind_info: 0xce0
+  __TEXT.__objc_classname: 0x6d7
+  __TEXT.__objc_methname: 0x9cbc
+  __TEXT.__objc_methtype: 0x145a
+  __TEXT.__objc_stubs: 0x69e0
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x12f0
+  __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x138
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3b58
-  __DATA_CONST.__objc_selrefs: 0x1f68
+  __DATA_CONST.__objc_const: 0x4330
+  __DATA_CONST.__objc_selrefs: 0x2260
+  __DATA_CONST.__objc_classrefs: 0x4a0
+  __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__objc_const: 0x19c8
-  __AUTH_CONST.__cfstring: 0x1a40
-  __AUTH_CONST.__const: 0x1c0
+  __AUTH_CONST.__objc_const: 0x1a58
+  __AUTH_CONST.__cfstring: 0x1b20
+  __AUTH_CONST.__const: 0x220
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x338
-  __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_classrefs: 0x448
-  __DATA.__objc_superrefs: 0x138
-  __DATA.__objc_ivar: 0x2e8
-  __DATA.__data: 0x5a0
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH.__objc_data: 0x820
+  __DATA.__objc_ivar: 0x354
+  __DATA.__data: 0x6c0
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x730
+  __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
-  - /System/Library/PrivateFrameworks/VoiceServices.framework/VoiceServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7E678438-1F3E-3EB7-B7FC-DA5B9FCB699D
-  Functions: 998
-  Symbols:   3871
-  CStrings:  2336
+  UUID: 8289A103-90E6-3F35-9F08-2E1B3981B36F
+  Functions: 1128
+  Symbols:   4328
+  CStrings:  2607
 
Symbols:
+ -[SRUIFSpeechSynthesisRequest .cxx_destruct]
+ -[SRUIFSpeechSynthesisRequest analyticsContext]
+ -[SRUIFSpeechSynthesisRequest audioData]
+ -[SRUIFSpeechSynthesisRequest canUseServerTTS]
+ -[SRUIFSpeechSynthesisRequest completion]
+ -[SRUIFSpeechSynthesisRequest delayed]
+ -[SRUIFSpeechSynthesisRequest eligibleAfterDuration]
+ -[SRUIFSpeechSynthesisRequest gender]
+ -[SRUIFSpeechSynthesisRequest identifier]
+ -[SRUIFSpeechSynthesisRequest initWithAudioData:identifier:sessionId:provisionally:eligibleAfterDuration:canUseServerTTS:completion:]
+ -[SRUIFSpeechSynthesisRequest initWithText:audioData:identifier:sessionId:language:gender:voiceName:provisional:eligibleAfterDuration:delayed:preparationIdentifier:completion:analyticsContext:speakableContextInfo:canUseServerTTS:]
+ -[SRUIFSpeechSynthesisRequest initWithText:identifier:sessionId:language:gender:voiceName:canUseServerTTS:completion:]
+ -[SRUIFSpeechSynthesisRequest isPhonetic]
+ -[SRUIFSpeechSynthesisRequest language]
+ -[SRUIFSpeechSynthesisRequest preparationIdentifier]
+ -[SRUIFSpeechSynthesisRequest provisional]
+ -[SRUIFSpeechSynthesisRequest sessionId]
+ -[SRUIFSpeechSynthesisRequest speakableContextInfo]
+ -[SRUIFSpeechSynthesisRequest text]
+ -[SRUIFSpeechSynthesisRequest voiceName]
+ -[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]
+ -[SRUIFSpeechSynthesisTask preferredVoice]
+ -[SRUIFSpeechSynthesizer .cxx_destruct]
+ -[SRUIFSpeechSynthesizer _activeTaskWithTTSRequest:]
+ -[SRUIFSpeechSynthesizer _activeTasks]
+ -[SRUIFSpeechSynthesizer _cancelByCancellingActiveTasksOnly:]
+ -[SRUIFSpeechSynthesizer _delayedTasks]
+ -[SRUIFSpeechSynthesizer _duckTTSVolumeTo:rampTime:completion:]
+ -[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]
+ -[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:].cold.1
+ -[SRUIFSpeechSynthesizer _filterVoices:gender:]
+ -[SRUIFSpeechSynthesizer _findVoiceForLanguage:gender:completion:]
+ -[SRUIFSpeechSynthesizer _findVoiceForLanguage:gender:completion:].cold.1
+ -[SRUIFSpeechSynthesizer _genderForString:]
+ -[SRUIFSpeechSynthesizer _handleAudioData:completion:]
+ -[SRUIFSpeechSynthesizer _handleText:completion:]
+ -[SRUIFSpeechSynthesizer _handleText:completion:].cold.1
+ -[SRUIFSpeechSynthesizer _isSynthesisQueueEmpty]
+ -[SRUIFSpeechSynthesizer _processProvisionalTasks]
+ -[SRUIFSpeechSynthesizer _processTaskQueue]
+ -[SRUIFSpeechSynthesizer _speechFootPrintForVoice:]
+ -[SRUIFSpeechSynthesizer _taskQueue]
+ -[SRUIFSpeechSynthesizer audioSessionID]
+ -[SRUIFSpeechSynthesizer cancel]
+ -[SRUIFSpeechSynthesizer clientStateManagerDelegate]
+ -[SRUIFSpeechSynthesizer dealloc]
+ -[SRUIFSpeechSynthesizer delegate]
+ -[SRUIFSpeechSynthesizer didFinishAudioTask:withError:]
+ -[SRUIFSpeechSynthesizer didFinishSpeakTask:withError:]
+ -[SRUIFSpeechSynthesizer didStartAudioTask:]
+ -[SRUIFSpeechSynthesizer didStartSpeakTask:]
+ -[SRUIFSpeechSynthesizer duckTTSVolumeTo:rampTime:completion:]
+ -[SRUIFSpeechSynthesizer enqueueAudioData:identifier:sessionId:provisionally:eligibleAfterDuration:completion:]
+ -[SRUIFSpeechSynthesizer enqueuePhaticWithCompletion:]
+ -[SRUIFSpeechSynthesizer enqueueSpeechSynthesisRequest:]
+ -[SRUIFSpeechSynthesizer enqueueText:identifier:sessionId:completion:]
+ -[SRUIFSpeechSynthesizer enqueueText:identifier:sessionId:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:completion:analyticsContext:speakableContextInfo:]
+ -[SRUIFSpeechSynthesizer enqueueText:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:completion:analyticsContext:speakableContextInfo:]
+ -[SRUIFSpeechSynthesizer init]
+ -[SRUIFSpeechSynthesizer invalidateOnMainThread]
+ -[SRUIFSpeechSynthesizer invalidate]
+ -[SRUIFSpeechSynthesizer isSpeaking]
+ -[SRUIFSpeechSynthesizer isSynthesisQueueEmpty:]
+ -[SRUIFSpeechSynthesizer prewarmIfNeeded]
+ -[SRUIFSpeechSynthesizer processDelayedItem:]
+ -[SRUIFSpeechSynthesizer processDelayedItem:].cold.1
+ -[SRUIFSpeechSynthesizer queue:didEnqueueObjects:]
+ -[SRUIFSpeechSynthesizer setAudioSessionID:]
+ -[SRUIFSpeechSynthesizer setClientStateManagerDelegate:]
+ -[SRUIFSpeechSynthesizer setDelegate:]
+ -[SRUIFSpeechSynthesizer setOutputVoice:]
+ -[SRUIFSpeechSynthesizer setTtsSession:]
+ -[SRUIFSpeechSynthesizer skipCurrentSynthesis]
+ -[SRUIFSpeechSynthesizer speakTask:didGenerateMetrics:]
+ -[SRUIFSpeechSynthesizer speakTask:didGenerateMetrics:].cold.1
+ -[SRUIFSpeechSynthesizer taskEligibilityDidChange:]
+ -[SRUIFSpeechSynthesizer ttsSession]
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table71
+ GCC_except_table76
+ _AFAnalyticsContextsMerge
+ _OBJC_CLASS_$_AFSpeechSynthesisRecord
+ _OBJC_CLASS_$_AFVoiceInfo
+ _OBJC_CLASS_$_SRUIFSpeechSynthesisRequest
+ _OBJC_CLASS_$_SRUIFSpeechSynthesizer
+ _OBJC_CLASS_$_SiriTTSAudioData
+ _OBJC_CLASS_$_SiriTTSAudioRequest
+ _OBJC_CLASS_$_SiriTTSDaemonSession
+ _OBJC_CLASS_$_SiriTTSSpeechRequest
+ _OBJC_CLASS_$_SiriTTSSynthesisRequest
+ _OBJC_CLASS_$_SiriTTSSynthesisVoice
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._analyticsContext
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._audioData
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._canUseServerTTS
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._completion
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._delayed
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._eligibleAfterDuration
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._gender
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._identifier
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._isPhonetic
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._language
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._preparationIdentifier
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._provisional
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._sessionId
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._speakableContextInfo
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._text
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisRequest._voiceName
+ _OBJC_IVAR_$_SRUIFSpeechSynthesisTask._preferredVoice
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._activeTasks
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._audioSessionID
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._availableVoicesForLanguage
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._clientStateManagerDelegate
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._delayedTasks
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._delegate
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._outputVoice
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._pendingTasksGroup
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._pendingTasksQueue
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._processingTasksQueue
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._taskQueue
+ _OBJC_IVAR_$_SRUIFSpeechSynthesizer._ttsSession
+ _OBJC_METACLASS_$_SRUIFSpeechSynthesisRequest
+ _OBJC_METACLASS_$_SRUIFSpeechSynthesizer
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __OBJC_$_INSTANCE_METHODS_SRUIFSpeechSynthesisRequest
+ __OBJC_$_INSTANCE_METHODS_SRUIFSpeechSynthesizer
+ __OBJC_$_INSTANCE_VARIABLES_SRUIFSpeechSynthesisRequest
+ __OBJC_$_INSTANCE_VARIABLES_SRUIFSpeechSynthesizer
+ __OBJC_$_PROP_LIST_SRUIFSpeechSynthesisRequest
+ __OBJC_$_PROP_LIST_SRUIFSpeechSynthesizer
+ __OBJC_$_PROP_LIST_SRUIFSpeechSynthesizing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AFQueueDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SRUIFSpeechSynthesisTaskDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SRUIFSpeechSynthesizing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AFQueueDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SRUIFSpeechSynthesisTaskDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SRUIFSpeechSynthesizing
+ __OBJC_$_PROTOCOL_REFS_AFQueueDelegate
+ __OBJC_$_PROTOCOL_REFS_SRUIFSpeechSynthesizing
+ __OBJC_CLASS_PROTOCOLS_$_SRUIFSpeechSynthesizer
+ __OBJC_CLASS_RO_$_SRUIFSpeechSynthesisRequest
+ __OBJC_CLASS_RO_$_SRUIFSpeechSynthesizer
+ __OBJC_LABEL_PROTOCOL_$_AFQueueDelegate
+ __OBJC_LABEL_PROTOCOL_$_SRUIFSpeechSynthesisTaskDelegate
+ __OBJC_LABEL_PROTOCOL_$_SRUIFSpeechSynthesizing
+ __OBJC_METACLASS_RO_$_SRUIFSpeechSynthesisRequest
+ __OBJC_METACLASS_RO_$_SRUIFSpeechSynthesizer
+ __OBJC_PROTOCOL_$_AFQueueDelegate
+ __OBJC_PROTOCOL_$_SRUIFSpeechSynthesisTaskDelegate
+ __OBJC_PROTOCOL_$_SRUIFSpeechSynthesizing
+ ___246-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke
+ ___246-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke.2
+ ___246-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke_2
+ ___255-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke
+ ___255-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke.45
+ ___255-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke.49
+ ___36-[SRUIFSpeechSynthesizer isSpeaking]_block_invoke
+ ___41-[SRUIFSpeechSynthesizer prewarmIfNeeded]_block_invoke
+ ___43-[SRUIFSpeechSynthesizer _processTaskQueue]_block_invoke
+ ___43-[SRUIFSpeechSynthesizer _processTaskQueue]_block_invoke.77
+ ___43-[SRUIFSpeechSynthesizer _processTaskQueue]_block_invoke.79
+ ___44-[SRUIFSpeechSynthesizer didStartAudioTask:]_block_invoke
+ ___44-[SRUIFSpeechSynthesizer didStartSpeakTask:]_block_invoke
+ ___47-[SRUIFSpeechSynthesizer _filterVoices:gender:]_block_invoke
+ ___48-[SRUIFSpeechSynthesizer isSynthesisQueueEmpty:]_block_invoke
+ ___48-[SRUIFSpeechSynthesizer isSynthesisQueueEmpty:]_block_invoke_2
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke.62
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke.66
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke.69
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke.72
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke.73
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke.73.cold.1
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke.75
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke.cold.1
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke_2
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke_2.76
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke_2.76.cold.1
+ ___49-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke_3
+ ___52-[SRUIFSpeechSynthesizer _activeTaskWithTTSRequest:]_block_invoke
+ ___54-[SRUIFSpeechSynthesizer _handleAudioData:completion:]_block_invoke
+ ___54-[SRUIFSpeechSynthesizer _handleAudioData:completion:]_block_invoke_2
+ ___55-[SRUIFSpeechSynthesizer didFinishAudioTask:withError:]_block_invoke
+ ___55-[SRUIFSpeechSynthesizer didFinishAudioTask:withError:]_block_invoke.30
+ ___55-[SRUIFSpeechSynthesizer didFinishAudioTask:withError:]_block_invoke.cold.1
+ ___55-[SRUIFSpeechSynthesizer didFinishAudioTask:withError:]_block_invoke.cold.2
+ ___55-[SRUIFSpeechSynthesizer didFinishAudioTask:withError:]_block_invoke_2
+ ___55-[SRUIFSpeechSynthesizer didFinishSpeakTask:withError:]_block_invoke
+ ___55-[SRUIFSpeechSynthesizer didFinishSpeakTask:withError:]_block_invoke.32
+ ___55-[SRUIFSpeechSynthesizer didFinishSpeakTask:withError:]_block_invoke.32.cold.1
+ ___55-[SRUIFSpeechSynthesizer didFinishSpeakTask:withError:]_block_invoke.33
+ ___55-[SRUIFSpeechSynthesizer didFinishSpeakTask:withError:]_block_invoke.cold.1
+ ___55-[SRUIFSpeechSynthesizer didFinishSpeakTask:withError:]_block_invoke.cold.2
+ ___55-[SRUIFSpeechSynthesizer didFinishSpeakTask:withError:]_block_invoke.cold.3
+ ___61-[SRUIFSpeechSynthesizer _cancelByCancellingActiveTasksOnly:]_block_invoke
+ ___61-[SRUIFSpeechSynthesizer _cancelByCancellingActiveTasksOnly:]_block_invoke_2
+ ___61-[SRUIFSpeechSynthesizer _cancelByCancellingActiveTasksOnly:]_block_invoke_3
+ ___62-[SRUIFSpeechSynthesizer duckTTSVolumeTo:rampTime:completion:]_block_invoke
+ ___62-[SRUIFSpeechSynthesizer duckTTSVolumeTo:rampTime:completion:]_block_invoke_2
+ ___63-[SRUIFSpeechSynthesizer _duckTTSVolumeTo:rampTime:completion:]_block_invoke
+ ___66-[SRUIFSpeechSynthesizer _findVoiceForLanguage:gender:completion:]_block_invoke
+ ___NSDictionary0__struct
+ ___block_descriptor_32_e41_v32?0"SRUIFSpeechSynthesisTask"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e21_v20?0"NSString"8B16ls32l8
+ ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_41_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e41_v32?0"SRUIFSpeechSynthesisTask"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e28_v32?0"AFVoiceInfo"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e39_v16?0"SiriTTSInstrumentationMetrics"8lw40l8s32l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32r40r_e28_v32?0"AFVoiceInfo"8Q16^B24lr32l8r40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_57_e8_32s40s48w_e26_v16?0?<v?"NSString"B>8lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56bs64bs72w_e21_v16?0"AFVoiceInfo"8lw72l8s32l8s40l8s56l8s48l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56bs64bs72w_e21_v16?0"AFVoiceInfo"8lw72l8s32l8s56l8s40l8s48l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s40l8s72l8s48l8s56l8s64l8s80l8
+ ___block_literal_global.23
+ ___block_literal_global.25
+ __os_feature_enabled_impl
+ _dispatch_group_wait
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kAFAssistantErrorDomain
+ _objc_msgSend$_activeTasks
+ _objc_msgSend$_cancelByCancellingActiveTasksOnly:
+ _objc_msgSend$_delayedTasks
+ _objc_msgSend$_duckTTSVolumeTo:rampTime:completion:
+ _objc_msgSend$_enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:
+ _objc_msgSend$_filterVoices:gender:
+ _objc_msgSend$_findVoiceForLanguage:gender:completion:
+ _objc_msgSend$_genderForString:
+ _objc_msgSend$_handleAudioData:completion:
+ _objc_msgSend$_handleText:completion:
+ _objc_msgSend$_isSynthesisQueueEmpty
+ _objc_msgSend$_processProvisionalTasks
+ _objc_msgSend$_processTaskQueue
+ _objc_msgSend$_speechFootPrintForVoice:
+ _objc_msgSend$_taskQueue
+ _objc_msgSend$adjustVolume:rampTime:didFinish:
+ _objc_msgSend$allVoicesForSiriSessionLanguage:
+ _objc_msgSend$analyticsContext
+ _objc_msgSend$cancelWithRequest:
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$clientStateManagerDelegate
+ _objc_msgSend$completion
+ _objc_msgSend$decoderStreamDescription
+ _objc_msgSend$delayed
+ _objc_msgSend$dequeueAllObjects
+ _objc_msgSend$didFinishAudioTask:withError:
+ _objc_msgSend$didFinishSpeakTask:withError:
+ _objc_msgSend$didStartAudioTask:
+ _objc_msgSend$didStartSpeakTask:
+ _objc_msgSend$eligibleAfterDuration
+ _objc_msgSend$enqueueObject:
+ _objc_msgSend$errorWithCode:
+ _objc_msgSend$executeCompletion
+ _objc_msgSend$footprint
+ _objc_msgSend$genderString
+ _objc_msgSend$initWithAudio:
+ _objc_msgSend$initWithLanguage:name:
+ _objc_msgSend$initWithLanguageCode:gender:isCustom:name:footprint:contentVersion:masteredVersion:
+ _objc_msgSend$initWithText:audioData:identifier:sessionId:language:gender:voiceName:provisional:eligibleAfterDuration:delayed:preparationIdentifier:completion:analyticsContext:speakableContextInfo:canUseServerTTS:
+ _objc_msgSend$initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:
+ _objc_msgSend$initWithText:voice:
+ _objc_msgSend$initWithUtterance:beginTimestamp:endTimestamp:
+ _objc_msgSend$isCustom
+ _objc_msgSend$isPhonetic
+ _objc_msgSend$isSpeaking:
+ _objc_msgSend$isSpeechSynthesisErrorUserCancelled:
+ _objc_msgSend$languageString
+ _objc_msgSend$makeObjectsPerformSelector:
+ _objc_msgSend$name
+ _objc_msgSend$notifyClientStateManagerSpeakingBegan:
+ _objc_msgSend$notifyClientStateManagerSpeakingEnded:
+ _objc_msgSend$notifyClientStateManagerTransactionBegan:
+ _objc_msgSend$notifyClientStateManagerTransactionEnded:
+ _objc_msgSend$outputVoice
+ _objc_msgSend$performSelectorOnMainThread:withObject:waitUntilDone:
+ _objc_msgSend$preferredVoice
+ _objc_msgSend$preparationIdentifier
+ _objc_msgSend$prewarmWithRequest:didFinish:
+ _objc_msgSend$provisional
+ _objc_msgSend$queryPhaticCapabilityWithVoice:reply:
+ _objc_msgSend$requestCreatedTime
+ _objc_msgSend$setAsbd:
+ _objc_msgSend$setAudioData:
+ _objc_msgSend$setAudioSessionId:
+ _objc_msgSend$setContextInfo:
+ _objc_msgSend$setDelayed:
+ _objc_msgSend$setDidReportInstrument:
+ _objc_msgSend$setDidStartSpeaking:
+ _objc_msgSend$setFootprint:
+ _objc_msgSend$setIsPhonetic:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setPrivacySensitive:
+ _objc_msgSend$setRate:
+ _objc_msgSend$setShouldCache:
+ _objc_msgSend$setSiriRequestId:
+ _objc_msgSend$setSynthesisError:
+ _objc_msgSend$setSynthesisResult:
+ _objc_msgSend$setTtsSessionRequest:
+ _objc_msgSend$siriSpeechRate
+ _objc_msgSend$speakTask:didGenerateMetrics:
+ _objc_msgSend$speakWithAudioRequest:didFinish:
+ _objc_msgSend$speakWithSpeechRequest:didFinish:
+ _objc_msgSend$speakableContextInfo
+ _objc_msgSend$speechBeginTime
+ _objc_msgSend$speechEndTime
+ _objc_msgSend$speechSynthesisDidFinish:
+ _objc_msgSend$speechSynthesisDidStartSpeakingWithIdentifier:
+ _objc_msgSend$speechSynthesisDidStopSpeakingWithIdentifier:queueIsEmpty:
+ _objc_msgSend$speechSynthesisGetPreparedTextForIdentifier:completion:
+ _objc_msgSend$startObserversWithOptions:
+ _objc_msgSend$synchronizeVoiceServicesLanguageCode
+ _objc_msgSend$synthesisResult
+ _objc_msgSend$ttsSession
+ _objc_msgSend$ttsSessionRequest
+ _objc_retain_x9
+ _objc_unsafeClaimAutoreleasedReturnValue
- -[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]
- -[SRUIFSpeechSynthesisTask presynthesizedAudioRequest]
- -[SRUIFSpeechSynthesisTask setPresynthesizedAudioRequest:]
- -[SRUIFSpeechSynthesisTask setSpeechRequest:]
- -[SRUIFSpeechSynthesisTask speechRequest]
- _OBJC_IVAR_$_SRUIFSpeechSynthesisTask._presynthesizedAudioRequest
- _OBJC_IVAR_$_SRUIFSpeechSynthesisTask._speechRequest
- ___231-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke
- ___231-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke.2
- ___231-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke_2
- _objc_msgSend$startObservers
CStrings:
+ "\x01'\x11\x13"
+ "\x054"
+ "\x1b"
+ "\x1b/+%@\x1b/+"
+ "\x1b\\mrk=play=phat\\"
+ "%s #phatic [Post] Fail! Phatic Not Supported"
+ "%s #phatic [Pre]"
+ "%s #phatic [Pre] Success"
+ "%s #tts"
+ "%s #tts %@"
+ "%s #tts %@ has %@ available Voices"
+ "%s #tts 24 [Pre] Calling speakWithSpeechRequest:%@"
+ "%s #tts Canceling speech synthesis"
+ "%s #tts Expected an active task that corresponds to an active speech request, but got nothing!"
+ "%s #tts Finished speaking presynthesized audio \"%@\""
+ "%s #tts Invalidating %@"
+ "%s #tts No voice found for language: %@ gender: %@"
+ "%s #tts Not speaking nil text"
+ "%s #tts Started:%@"
+ "%s #tts Unable to finish speaking presynthesized request\"%@\": %{public}@"
+ "%s #tts Unable to prewarm session, error=%@"
+ "%s #tts Updating synthesizer voice to %@"
+ "%s #tts [Post] Active Task count: %tu"
+ "%s #tts [Post] Calling completion for Task: %@"
+ "%s #tts [Post] Event metrics was missing for the request\"%@\""
+ "%s #tts [Post] Expected an active task that corresponds to an active speech request, but got nothing!"
+ "%s #tts [Post] Failed onNoOutputVoice"
+ "%s #tts [Post] Finished %@"
+ "%s #tts [Post] Finished Metrics generated %@"
+ "%s #tts [Post] Marking result %@"
+ "%s #tts [Post] No text, marking finished"
+ "%s #tts [Post] Pending Tasks Group Complete"
+ "%s #tts [Post] Removing Task: %@"
+ "%s #tts [Post] Synthesis failed for with %@ for %@ "
+ "%s #tts [Post] Synthesis was cancelled, marking speech request finished \"%@\": %{public}@"
+ "%s #tts [Post] Synthesis was cancelled, marking speech request finished \"%{sensitive}@\": %{public}@"
+ "%s #tts [Post] Unable to finish speaking \"%@\": %{public}@"
+ "%s #tts [Post] Unable to finish speaking \"%{sensitive}@\": %{public}@"
+ "%s #tts [Post] text=\"%@\" error=%@ request=%@ finishedSpeaking=%i"
+ "%s #tts [Post] text=\"%{sensitive}@\" error=%@ request=%@ finishedSpeaking=%i"
+ "%s #tts [Post] text=%@ request=%@"
+ "%s #tts [Post] text=%{sensitive}@ request=%@"
+ "%s #tts [Pre] Audio Data:%@"
+ "%s #tts [Pre] Could not find voice for %@ %@"
+ "%s #tts [Pre] Discarding %@; it is provisional and there are other tasks enqueued"
+ "%s #tts [Pre] Enqueueing task: %@"
+ "%s #tts [Pre] Found voice for %@ %@: %@"
+ "%s #tts [Pre] Invalid speak request. No text and no audio data"
+ "%s #tts [Pre] No match for output voice"
+ "%s #tts [Pre] No voice for %@ %@. Using %@"
+ "%s #tts [Pre] Output voice [%@, %@] %@ specified language %@, gender %@"
+ "%s #tts [Pre] Pending Tasks Group Wait"
+ "%s #tts [Pre] Preparation %@"
+ "%s #tts [Pre] Processing task text=\"%@\" identifier=%@"
+ "%s #tts [Pre] Processing task text=\"%{sensitive}@\" identifier=%@"
+ "%s #tts [Pre] Started synthesis, %@, %@"
+ "%s #tts [Pre] Success ValidOutputVoice:%@"
+ "%s #tts [Pre] Task is delayed but no identifier provided. This will likely result in out-of-order TTS: %@"
+ "%s #tts [Pre] Using preferredVoice"
+ "%s #tts [Pre] nil is an invalid delayed item identifier"
+ "%s #tts [Pre] outputVoiceMatches"
+ "%s #tts [Pre] task not eligible: %@"
+ "%s #tts [Pre] text:%@"
+ "%s #tts [Pre] text:%{sensitive}@"
+ "%s #tts activeTasks=%tu taskQueue=%tu"
+ "%s #tts outputVoice:%@"
+ "%s #tts request=%@ error=%@"
+ "%s #tts started presynthesized audio for %@"
+ "%s #tts strongSelf==nil"
+ "%s #tts task=%@"
+ "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]"
+ "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke"
+ "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke_2"
+ "-[SRUIFSpeechSynthesizer _cancelByCancellingActiveTasksOnly:]_block_invoke"
+ "-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]"
+ "-[SRUIFSpeechSynthesizer _enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:]_block_invoke"
+ "-[SRUIFSpeechSynthesizer _findVoiceForLanguage:gender:completion:]"
+ "-[SRUIFSpeechSynthesizer _handleAudioData:completion:]"
+ "-[SRUIFSpeechSynthesizer _handleText:completion:]"
+ "-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke"
+ "-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke_2"
+ "-[SRUIFSpeechSynthesizer _handleText:completion:]_block_invoke_4"
+ "-[SRUIFSpeechSynthesizer _processProvisionalTasks]"
+ "-[SRUIFSpeechSynthesizer _processTaskQueue]_block_invoke"
+ "-[SRUIFSpeechSynthesizer _processTaskQueue]_block_invoke_2"
+ "-[SRUIFSpeechSynthesizer cancel]"
+ "-[SRUIFSpeechSynthesizer dealloc]"
+ "-[SRUIFSpeechSynthesizer didFinishAudioTask:withError:]_block_invoke"
+ "-[SRUIFSpeechSynthesizer didFinishSpeakTask:withError:]"
+ "-[SRUIFSpeechSynthesizer didFinishSpeakTask:withError:]_block_invoke"
+ "-[SRUIFSpeechSynthesizer didStartSpeakTask:]"
+ "-[SRUIFSpeechSynthesizer enqueuePhaticWithCompletion:]"
+ "-[SRUIFSpeechSynthesizer init]"
+ "-[SRUIFSpeechSynthesizer invalidate]"
+ "-[SRUIFSpeechSynthesizer prewarmIfNeeded]"
+ "-[SRUIFSpeechSynthesizer prewarmIfNeeded]_block_invoke"
+ "-[SRUIFSpeechSynthesizer processDelayedItem:]"
+ "-[SRUIFSpeechSynthesizer setOutputVoice:]"
+ "-[SRUIFSpeechSynthesizer speakTask:didGenerateMetrics:]"
+ "-[SRUIFSpeechSynthesizer taskEligibilityDidChange:]"
+ "@\"<SRUIFSpeechSynthesizerClientStateManagerDelegate>\""
+ "@\"<SRUIFSpeechSynthesizerDelegate>\""
+ "@\"<SRUIFSpeechSynthesizerDelegate>\"16@0:8"
+ "@\"AFQueue\""
+ "@\"AFVoiceInfo\""
+ "@\"SAVoice\""
+ "@\"SiriTTSDaemonSession\""
+ "@124@0:8@16@24@32@40@48@56@64B72d76B84@88@?96@104@112B120"
+ "@132@0:8@16@24@32@40@48@56@64B72d76B84@?88@?96@104@112B120@124"
+ "@64@0:8@16@24@32B40d44B52@?56"
+ "@76@0:8@16@24@32@40@48@56B64@?68"
+ "AFQueueDelegate"
+ "Accessibility"
+ "HighSpeedSiriTTS"
+ "I"
+ "I16@0:8"
+ "SRUIFSpeechSynthesisRequest"
+ "SRUIFSpeechSynthesisTaskDelegate"
+ "SRUIFSpeechSynthesizer"
+ "SRUIFSpeechSynthesizing"
+ "SpeechSynthesisPendingTasksQueue"
+ "SpeechSynthesisProcessingTasksQueue"
+ "T@\"<SRUIFSpeechSynthesizerClientStateManagerDelegate>\",W,N,V_clientStateManagerDelegate"
+ "T@\"<SRUIFSpeechSynthesizerDelegate>\",W,N"
+ "T@\"<SRUIFSpeechSynthesizerDelegate>\",W,N,V_delegate"
+ "T@\"AFQueue\",R,N,G_taskQueue,V_taskQueue"
+ "T@\"NSDictionary\",R,&,N,V_speakableContextInfo"
+ "T@\"NSMutableArray\",R,N,G_activeTasks,V_activeTasks"
+ "T@\"NSMutableDictionary\",R,N,G_delayedTasks,V_delayedTasks"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N,V_preparationIdentifier"
+ "T@\"NSString\",R,N,V_text"
+ "T@\"NSString\",R,N,V_voiceName"
+ "T@\"SAVoice\",R,N,V_preferredVoice"
+ "T@\"SiriTTSDaemonSession\",&,N,V_ttsSession"
+ "T@?,R,N,V_completion"
+ "TB,R,N,V_canUseServerTTS"
+ "TB,R,N,V_delayed"
+ "TB,R,N,V_eligibleAfterDuration"
+ "TB,R,N,V_isPhonetic"
+ "TB,R,N,V_provisional"
+ "TI,N,V_audioSessionID"
+ "_activeTaskWithTTSRequest:"
+ "_activeTasks"
+ "_audioSessionID"
+ "_availableVoicesForLanguage"
+ "_cancelByCancellingActiveTasksOnly:"
+ "_clientStateManagerDelegate"
+ "_delayedTasks"
+ "_duckTTSVolumeTo:rampTime:completion:"
+ "_eligibleAfterDuration"
+ "_enqueueText:audioData:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:shouldCache:completion:analyticsContext:speakableContextInfo:"
+ "_filterVoices:gender:"
+ "_findVoiceForLanguage:gender:completion:"
+ "_genderForString:"
+ "_handleAudioData:completion:"
+ "_handleText:completion:"
+ "_isSynthesisQueueEmpty"
+ "_outputVoice"
+ "_pendingTasksGroup"
+ "_pendingTasksQueue"
+ "_preferredVoice"
+ "_preparationIdentifier"
+ "_processProvisionalTasks"
+ "_processTaskQueue"
+ "_processingTasksQueue"
+ "_speechFootPrintForVoice:"
+ "_taskQueue"
+ "_ttsSession"
+ "_voiceName"
+ "activeTasks"
+ "adjustVolume:rampTime:didFinish:"
+ "allVoicesForSiriSessionLanguage:"
+ "b"
+ "cancelWithRequest:"
+ "caseInsensitiveCompare:"
+ "clientStateManagerDelegate"
+ "decoderStreamDescription"
+ "delayedTasks"
+ "dequeueAllObjects"
+ "didFinishAudioTask:withError:"
+ "didFinishSpeakTask:withError:"
+ "didStartAudioTask:"
+ "didStartSpeakTask:"
+ "duckTTSVolumeTo:rampTime:completion:"
+ "eligibleAfterDuration"
+ "enqueueAudioData:identifier:sessionId:provisionally:eligibleAfterDuration:completion:"
+ "enqueueObject:"
+ "enqueuePhaticWithCompletion:"
+ "enqueueSpeechSynthesisRequest:"
+ "enqueueText:identifier:sessionId:completion:"
+ "enqueueText:identifier:sessionId:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:completion:analyticsContext:speakableContextInfo:"
+ "enqueueText:identifier:sessionId:preferredVoice:language:gender:isPhonetic:provisionally:eligibleAfterDuration:delayed:canUseServerTTS:preparationIdentifier:completion:analyticsContext:speakableContextInfo:"
+ "female"
+ "footprint"
+ "genderString"
+ "id"
+ "initWithAudio:"
+ "initWithAudioData:identifier:sessionId:provisionally:eligibleAfterDuration:canUseServerTTS:completion:"
+ "initWithLanguage:name:"
+ "initWithLanguageCode:gender:isCustom:name:footprint:contentVersion:masteredVersion:"
+ "initWithText:audioData:identifier:sessionId:language:gender:voiceName:provisional:eligibleAfterDuration:delayed:preparationIdentifier:completion:analyticsContext:speakableContextInfo:canUseServerTTS:"
+ "initWithText:audioData:identifier:sessionId:preferredVoice:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:"
+ "initWithText:identifier:sessionId:language:gender:voiceName:canUseServerTTS:completion:"
+ "initWithText:voice:"
+ "initWithUtterance:beginTimestamp:endTimestamp:"
+ "invalidateOnMainThread"
+ "isCustom"
+ "isSpeaking"
+ "isSpeaking:"
+ "isSynthesisQueueEmpty:"
+ "languageString"
+ "makeObjectsPerformSelector:"
+ "male"
+ "matches"
+ "mismatches"
+ "neutral"
+ "notifyClientStateManagerSpeakingBegan:"
+ "notifyClientStateManagerSpeakingEnded:"
+ "notifyClientStateManagerTransactionBegan:"
+ "notifyClientStateManagerTransactionEnded:"
+ "outputVoice"
+ "performSelectorOnMainThread:withObject:waitUntilDone:"
+ "preferredVoice"
+ "preparationIdentifier"
+ "prewarmIfNeeded"
+ "prewarmWithRequest:didFinish:"
+ "processDelayedItem:"
+ "queryPhaticCapabilityWithVoice:reply:"
+ "queue:didEnqueueObjects:"
+ "requestCreatedTime"
+ "setAsbd:"
+ "setAudioData:"
+ "setAudioSessionID:"
+ "setAudioSessionId:"
+ "setClientStateManagerDelegate:"
+ "setContextInfo:"
+ "setDidReportInstrument:"
+ "setDidStartSpeaking:"
+ "setFootprint:"
+ "setObject:forKeyedSubscript:"
+ "setOutputVoice:"
+ "setPrivacySensitive:"
+ "setRate:"
+ "setSiriRequestId:"
+ "setTtsSession:"
+ "siriSpeechRate"
+ "skipCurrentSynthesis"
+ "speakTask:didGenerateMetrics:"
+ "speakWithAudioRequest:didFinish:"
+ "speakWithSpeechRequest:didFinish:"
+ "speechBeginTime"
+ "speechEndTime"
+ "speechSynthesisDidFinish:"
+ "speechSynthesisDidStartSpeakingWithIdentifier:"
+ "speechSynthesisDidStopSpeakingWithIdentifier:queueIsEmpty:"
+ "speechSynthesisGetPreparedTextForIdentifier:completion:"
+ "startObserversWithOptions:"
+ "synchronizeVoiceServicesLanguageCode"
+ "taskQueue"
+ "ttsSession"
+ "v112@0:8@16@24@32@40@48B56B60d64B72B76@80@?88@96@104"
+ "v120@0:8@16@24@32@40@48@56B64B68d72B80B84@88@?96@104@112"
+ "v132@0:8@16@24@32@40@48@56@64B72B76d80B88B92@96B104@?108@116@124"
+ "v16@?0@\"AFVoiceInfo\"8"
+ "v16@?0@\"SiriTTSInstrumentationMetrics\"8"
+ "v16@?0@?<v@?@\"NSString\"B>8"
+ "v20@0:8I16"
+ "v24@0:8@\"<SRUIFSpeechSynthesizerDelegate>\"16"
+ "v24@0:8@\"NSString\"16"
+ "v24@0:8@\"SRUIFSpeechSynthesisRequest\"16"
+ "v24@0:8@\"SRUIFSpeechSynthesisTask\"16"
+ "v24@0:8@?<v@?B>16"
+ "v24@0:8@?<v@?q@\"NSError\">16"
+ "v32@0:8@\"AFQueue\"16@\"NSArray\"24"
+ "v32@?0@\"AFVoiceInfo\"8Q16^B24"
+ "v32@?0@\"SRUIFSpeechSynthesisTask\"8Q16^B24"
+ "v36@0:8f16d20@?28"
+ "v36@0:8f16d20@?<v@?@\"NSError\">28"
+ "v48@0:8@16@24@32@?40"
+ "v60@0:8@16@24@32B40d44@?52"
+ "voiceName"
+ "\xc1"
- "\x01(\x11\x13"
- "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]"
- "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke"
- "-[SRUIFSpeechSynthesisTask initWithText:audioData:identifier:sessionId:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:]_block_invoke_2"
- "@\"VSPresynthesizedAudioRequest\""
- "@\"VSSpeechRequest\""
- "@124@0:8@16@24@32@40@48@56B64d68B76@?80@?88@96@104B112@116"
- "ServerTTSErrorDomain"
- "T@\"VSPresynthesizedAudioRequest\",&,N,V_presynthesizedAudioRequest"
- "T@\"VSSpeechRequest\",&,N,V_speechRequest"
- "VoiceServicesErrorDomain"
- "_presynthesizedAudioRequest"
- "_speechRequest"
- "initWithText:audioData:identifier:sessionId:language:gender:provisional:eligibleAfterDuration:delayed:preparation:completion:analyticsContext:speakableContextInfo:canUseServerTTS:eligibilityChangedQueue:"
- "presynthesizedAudioRequest"
- "setPresynthesizedAudioRequest:"
- "setSpeechRequest:"
- "speechRequest"
- "startObservers"
- "\xd1"

```
