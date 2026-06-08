## LiveTranscription

> `/System/Library/PrivateFrameworks/LiveTranscription.framework/LiveTranscription`

```diff

-545.18.0.0.0
-  __TEXT.__text: 0x308f8
-  __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_methlist: 0x15cc
-  __TEXT.__const: 0x910
-  __TEXT.__cstring: 0x8fa
-  __TEXT.__gcc_except_tab: 0x8c
-  __TEXT.__oslogstring: 0x2784
+576.1.0.0.0
+  __TEXT.__text: 0x307c8
+  __TEXT.__objc_methlist: 0x16d4
+  __TEXT.__const: 0x978
   __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__swift5_typeref: 0x3f6
+  __TEXT.__swift5_typeref: 0x418
+  __TEXT.__cstring: 0x97a
   __TEXT.__swift5_reflstr: 0x21a
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__constg_swiftt: 0x4fc
-  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__constg_swiftt: 0x528
+  __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_fieldmd: 0x244
+  __TEXT.__oslogstring: 0x2a0e
   __TEXT.__swift5_proto: 0x30
-  __TEXT.__swift5_types: 0x28
-  __TEXT.__swift5_capture: 0x308
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift5_capture: 0x378
   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x78
-  __TEXT.__unwind_info: 0xb90
-  __TEXT.__eh_frame: 0xb78
-  __TEXT.__objc_classname: 0x34e
-  __TEXT.__objc_methname: 0x3bf9
-  __TEXT.__objc_methtype: 0xd8c
-  __TEXT.__objc_stubs: 0x2940
-  __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0x590
-  __DATA_CONST.__objc_classlist: 0xa8
+  __TEXT.__swift_as_cont: 0x78
+  __TEXT.__gcc_except_tab: 0x88
+  __TEXT.__unwind_info: 0xa48
+  __TEXT.__eh_frame: 0xb80
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x610
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe40
+  __DATA_CONST.__objc_selrefs: 0xed8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH_CONST.__const: 0x998
-  __AUTH_CONST.__cfstring: 0x740
-  __AUTH_CONST.__objc_const: 0x2958
+  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__got: 0x3d0
+  __AUTH_CONST.__const: 0xb50
+  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__objc_const: 0x2ae0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0xa38
+  __AUTH_CONST.__auth_got: 0x8f0
+  __AUTH.__objc_data: 0xa88
   __AUTH.__data: 0x140
-  __DATA.__objc_ivar: 0x180
-  __DATA.__data: 0x6a8
-  __DATA.__bss: 0x688
-  __DATA.__common: 0x80
+  __DATA.__objc_ivar: 0x18c
+  __DATA.__data: 0x718
+  __DATA.__bss: 0x6c8
+  __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x248
   __DATA_DIRTY.__data: 0x38
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__bss: 0x18
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
-  - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D191F1E8-4936-3798-B937-4E832E261D8A
-  Functions: 1042
-  Symbols:   2019
-  CStrings:  1145
+  UUID: 946860B2-9AAD-31DC-8EC8-B4AE00EC050B
+  Functions: 999
+  Symbols:   2038
+  CStrings:  349
 
Symbols:
+ +[AXLCAudioSessionsManager _isCurrentProcessAXUIServer]
+ +[AXLCAudioSessionsManager isExcludedAppID:]
+ +[AXLCAudioSessionsManager sharedInstance]
+ -[AXLCAudioSessionsManager .cxx_destruct]
+ -[AXLCAudioSessionsManager _appInfoFromPid:]
+ -[AXLCAudioSessionsManager _handleSessionsUpdate:]
+ -[AXLCAudioSessionsManager _notifyListenerAboutActiveSessions:]
+ -[AXLCAudioSessionsManager _notifyListenersWithBlock:]
+ -[AXLCAudioSessionsManager _registerForAudioSessionsUpdates:]
+ -[AXLCAudioSessionsManager _serverConnectionDiedNotification:]
+ -[AXLCAudioSessionsManager _someSessionIsPlayingDidChangeNotification:]
+ -[AXLCAudioSessionsManager _unregisterFromAudioSessionsUpdates:]
+ -[AXLCAudioSessionsManager activePIDs]
+ -[AXLCAudioSessionsManager audioSessionsQueue]
+ -[AXLCAudioSessionsManager init]
+ -[AXLCAudioSessionsManager isSubscribed]
+ -[AXLCAudioSessionsManager listeners]
+ -[AXLCAudioSessionsManager registerForAudioSessionsUpdates:]
+ -[AXLCAudioSessionsManager setActivePIDs:]
+ -[AXLCAudioSessionsManager setAudioSessionsQueue:]
+ -[AXLCAudioSessionsManager setIsSubscribed:]
+ -[AXLCAudioSessionsManager setListeners:]
+ -[AXLCAudioSessionsManager subscribeOnAudioSessionsEvents]
+ -[AXLCAudioSessionsManager unregisterFromAudioSessionsUpdates:]
+ -[AXLCAudioSessionsManager unsubscribeFromAudioSessionsEvents]
+ -[AXLTAudioOutManager _cleanupAllPIDs]
+ -[AXLTAudioOutManager audioSessionStartedForPID:appID:appName:]
+ -[AXLTAudioOutManager audioSessionStoppedForPID:]
+ -[AXLTAudioOutManager audioSessionsManagerDidReset]
+ -[AXLTAudioOutManager audioSessionsManager]
+ -[AXLTAudioOutManager setAudioSessionsManager:]
+ -[AXLTAudioOutTranscriber isPaused]
+ -[AXLTAudioOutTranscriber setIsPaused:]
+ GCC_except_table294
+ GCC_except_table309
+ GCC_except_table341
+ GCC_except_table71
+ _AXPerformBlockOnMainThread
+ _OBJC_CLASS_$_AXLCAudioSessionsManager
+ _OBJC_CLASS_$_NSPointerArray
+ _OBJC_IVAR_$_AXLCAudioSessionsManager._activePIDs
+ _OBJC_IVAR_$_AXLCAudioSessionsManager._audioSessionsQueue
+ _OBJC_IVAR_$_AXLCAudioSessionsManager._isSubscribed
+ _OBJC_IVAR_$_AXLCAudioSessionsManager._listeners
+ _OBJC_IVAR_$_AXLTAudioOutManager._audioSessionsManager
+ _OBJC_IVAR_$_AXLTAudioOutTranscriber._isPaused
+ _OBJC_METACLASS_$_AXLCAudioSessionsManager
+ __OBJC_$_CLASS_METHODS_AXLCAudioSessionsManager
+ __OBJC_$_CLASS_PROP_LIST_AXLCAudioSessionsManager
+ __OBJC_$_INSTANCE_METHODS_AXLCAudioSessionsManager
+ __OBJC_$_INSTANCE_VARIABLES_AXLCAudioSessionsManager
+ __OBJC_$_PROP_LIST_AXLCAudioSessionsManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AXLCAudioSessionsManagerListener
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXLCAudioSessionsManagerListener
+ __OBJC_$_PROTOCOL_REFS_AXLCAudioSessionsManagerListener
+ __OBJC_CLASS_RO_$_AXLCAudioSessionsManager
+ __OBJC_LABEL_PROTOCOL_$_AXLCAudioSessionsManagerListener
+ __OBJC_METACLASS_RO_$_AXLCAudioSessionsManager
+ __OBJC_PROTOCOL_$_AXLCAudioSessionsManagerListener
+ ___38-[AXLTAudioOutManager _cleanupAllPIDs]_block_invoke
+ ___42+[AXLCAudioSessionsManager sharedInstance]_block_invoke
+ ___44+[AXLCAudioSessionsManager isExcludedAppID:]_block_invoke
+ ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.376
+ ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.379
+ ___50-[AXLCAudioSessionsManager _handleSessionsUpdate:]_block_invoke
+ ___50-[AXLCAudioSessionsManager _handleSessionsUpdate:]_block_invoke.386
+ ___50-[AXLCAudioSessionsManager _handleSessionsUpdate:]_block_invoke.389
+ ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.358
+ ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.362
+ ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke.367
+ ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke_2.368
+ ___55+[AXLCAudioSessionsManager _isCurrentProcessAXUIServer]_block_invoke
+ ___58-[AXLCAudioSessionsManager subscribeOnAudioSessionsEvents]_block_invoke
+ ___58-[AXLCAudioSessionsManager subscribeOnAudioSessionsEvents]_block_invoke.371
+ ___60-[AXLCAudioSessionsManager registerForAudioSessionsUpdates:]_block_invoke
+ ___62-[AXLCAudioSessionsManager _serverConnectionDiedNotification:]_block_invoke
+ ___62-[AXLCAudioSessionsManager _serverConnectionDiedNotification:]_block_invoke_2
+ ___62-[AXLCAudioSessionsManager unsubscribeFromAudioSessionsEvents]_block_invoke
+ ___62-[AXLCAudioSessionsManager unsubscribeFromAudioSessionsEvents]_block_invoke_2
+ ___63-[AXLCAudioSessionsManager unregisterFromAudioSessionsUpdates:]_block_invoke
+ ___71-[AXLCAudioSessionsManager _someSessionIsPlayingDidChangeNotification:]_block_invoke
+ ___79-[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]_block_invoke.356
+ ___80-[AXLTTranscriber startTranscriptionForPID:appName:callback:completionCallback:]_block_invoke.358
+ ___block_descriptor_32_e44_v16?0"<AXLCAudioSessionsManagerListener>"8l
+ ___block_descriptor_33_e44_v16?0"<AXLCAudioSessionsManagerListener>"8l
+ ___block_descriptor_36_e44_v16?0"<AXLCAudioSessionsManagerListener>"8l
+ ___block_descriptor_52_e8_32s40s_e44_v16?0"<AXLCAudioSessionsManagerListener>"8ls32l8s40l8
+ ___block_literal_global.1007
+ ___block_literal_global.185
+ ___block_literal_global.379
+ ___block_literal_global.383
+ ___block_literal_global.385
+ ___block_literal_global.399
+ ___block_literal_global.421
+ ___block_literal_global.578
+ ___block_literal_global.652
+ ___block_literal_global.684
+ ___block_literal_global.82
+ ___block_literal_global.842
+ ___swift__destructor
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.10
+ ___swift_closure_destructor.103
+ ___swift_closure_destructor.108
+ ___swift_closure_destructor.10Tm
+ ___swift_closure_destructor.113
+ ___swift_closure_destructor.118
+ ___swift_closure_destructor.121
+ ___swift_closure_destructor.126
+ ___swift_closure_destructor.130
+ ___swift_closure_destructor.130Tm
+ ___swift_closure_destructor.134
+ ___swift_closure_destructor.138
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.142
+ ___swift_closure_destructor.151
+ ___swift_closure_destructor.155
+ ___swift_closure_destructor.160
+ ___swift_closure_destructor.166
+ ___swift_closure_destructor.17
+ ___swift_closure_destructor.170
+ ___swift_closure_destructor.175
+ ___swift_closure_destructor.185
+ ___swift_closure_destructor.19
+ ___swift_closure_destructor.190
+ ___swift_closure_destructor.19Tm
+ ___swift_closure_destructor.20
+ ___swift_closure_destructor.23
+ ___swift_closure_destructor.24
+ ___swift_closure_destructor.28
+ ___swift_closure_destructor.28Tm
+ ___swift_closure_destructor.32
+ ___swift_closure_destructor.37
+ ___swift_closure_destructor.41
+ ___swift_closure_destructor.46
+ ___swift_closure_destructor.52
+ ___swift_closure_destructor.56
+ ___swift_closure_destructor.6
+ ___swift_closure_destructor.61
+ ___swift_closure_destructor.68
+ ___swift_closure_destructor.75
+ ___swift_closure_destructor.79
+ ___swift_closure_destructor.83
+ ___swift_closure_destructor.88
+ ___swift_closure_destructor.91
+ ___swift_closure_destructorTm
+ __isCurrentProcessAXUIServer._result
+ __isCurrentProcessAXUIServer.token
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_appInfoFromPid:
+ _objc_msgSend$_cleanupAllPIDs
+ _objc_msgSend$_handleSessionsUpdate:
+ _objc_msgSend$_isCurrentProcessAXUIServer
+ _objc_msgSend$_notifyListenerAboutActiveSessions:
+ _objc_msgSend$_notifyListenersWithBlock:
+ _objc_msgSend$_registerForAudioSessionsUpdates:
+ _objc_msgSend$_unregisterFromAudioSessionsUpdates:
+ _objc_msgSend$activePIDs
+ _objc_msgSend$addPointer:
+ _objc_msgSend$allKeys
+ _objc_msgSend$allObjects
+ _objc_msgSend$audioSessionStartedForPID:appID:appName:
+ _objc_msgSend$audioSessionStoppedForPID:
+ _objc_msgSend$audioSessionsManagerDidReset
+ _objc_msgSend$audioSessionsQueue
+ _objc_msgSend$audioSessionsUpdated:
+ _objc_msgSend$compact
+ _objc_msgSend$connect:to:format:error:
+ _objc_msgSend$installTapOnBus:bufferSize:format:error:block:
+ _objc_msgSend$isSubscribed
+ _objc_msgSend$listeners
+ _objc_msgSend$pointerAtIndex:
+ _objc_msgSend$registerForAudioSessionsUpdates:
+ _objc_msgSend$removePointerAtIndex:
+ _objc_msgSend$setActivePIDs:
+ _objc_msgSend$setIsSubscribed:
+ _objc_msgSend$subscribeOnAudioSessionsEvents
+ _objc_msgSend$unregisterFromAudioSessionsUpdates:
+ _objc_msgSend$unsubscribeFromAudioSessionsEvents
+ _objc_msgSend$weakObjectsPointerArray
+ _objc_retain_x1
+ _objc_retain_x4
+ _sharedInstance._shared.1008
+ _sharedInstance._shared.653
+ _sharedInstance._shared.843
+ _sharedInstance.onceToken.1006
+ _sharedInstance.onceToken.184
+ _sharedInstance.onceToken.577
+ _sharedInstance.onceToken.651
+ _sharedInstance.onceToken.841
+ _swift_getForeignTypeMetadata
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release_x1
+ _swift_release_x12
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x1
+ _swift_retain_x13
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x23
+ _swift_retain_x25
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _symbolic SS_SSt
+ _symbolic _____ So27AVAudioConverterInputStatusV
+ _symbolic _____Spy_____GSo13AVAudioBufferCSgIgyyo_ s6UInt32V So27AVAudioConverterInputStatusV
- +[AXLTAudioOutManager isCurrentProcessAXUIServer]
- +[AXLTAudioOutManager isCurrentProcessAXUIServer].cold.1
- +[AXLTAudioOutManager isExcludedAppID:]
- +[AXLTAudioOutManager sharedInstance].cold.1
- +[AXLTAudioTextDumper sharedInstance].cold.1
- +[AXLTLanguageAssetManager sharedInstance].cold.1
- +[AXLTLiveTranscription sharedInstance].cold.1
- +[AXLTPhoneCallListener sharedInstance].cold.1
- -[AXLTAudioOutManager _avSessionMediaServicesResetNotification:]
- -[AXLTAudioOutManager _cleanupAllPids]
- -[AXLTAudioOutManager _reportErrorWithCode:debugErrorString:cleanupForPID:].cold.1
- -[AXLTAudioOutManager _setupAVSystemNotificationSystem]
- -[AXLTAudioOutManager _setupAVSystemNotificationSystem].cold.1
- -[AXLTAudioOutManager _someSessionIsPlayingDidChangeNotification:]
- -[AXLTAudioOutManager appInfoFromPid:]
- -[AXLTAudioOutManager appInfoFromPid:].cold.1
- -[AXLTAudioOutManager appInfoFromPid:].cold.2
- -[AXLTAudioOutManager appInfoFromPid:].cold.3
- -[AXLTAudioOutManager avSystemController]
- -[AXLTAudioOutManager registerForAVSystemControllerNotifications]
- -[AXLTAudioOutManager registerForAVSystemControllerNotifications].cold.1
- -[AXLTAudioOutManager setAvSystemController:]
- -[AXLTAudioOutManager setSubscribed:]
- -[AXLTAudioOutManager subscribed]
- -[AXLTAudioOutManager unregisterForAVSystemControllerNotifications]
- -[AXLTAudioOutManager unregisterForAVSystemControllerNotifications].cold.1
- -[AXLTAudioOutManager updateAudioSessionsInfoFromSessionsArray:]
- -[AXLTAudioOutManager updateAudioSessionsInfoFromSessionsArray:].cold.1
- -[AXLTAudioOutManager updateAudioSessionsInfoFromSessionsArray:].cold.2
- -[AXLTAudioOutManager updateAudioSessionsInfoFromSessionsArray:].cold.3
- -[AXLTAudioOutTranscriber _findSilencePacketOffset:packetCount:silentSamplesMin:zeroOffsetOnly:]
- -[AXLTAudioOutTranscriber _isSilenceOnlyInBuffer:packetCount:].cold.1
- -[AXLTAudioOutTranscriber cleanup].cold.1
- -[AXLTAudioOutTranscriber cleanup].cold.2
- -[AXLTAudioOutTranscriber cleanup].cold.3
- -[AXLTAudioOutTranscriber createAudioBuffersWithBufferByteSize:error:].cold.1
- -[AXLTAudioOutTranscriber createAudioBuffersWithBufferByteSize:error:].cold.2
- -[AXLTAudioOutTranscriber handleAudioBuffer:audioQueue:timestamp:packetCount:packetDesc:].cold.1
- -[AXLTAudioOutTranscriber setSilentSamplesTailCount:]
- -[AXLTAudioOutTranscriber silentSamplesTailCount]
- -[AXLTAudioTextDumper init].cold.1
- -[AXLTAudioTextDumper init].cold.2
- -[AXLTLanguageAssetManager languageAssetAvaliableForTaskHint:completion:].cold.1
- -[AXLTLiveTranscription audioInfoData:].cold.1
- -[AXLTLiveTranscription resetTranscribing:].cold.1
- -[AXLTLiveTranscription transcriberOutputData:].cold.1
- -[AXLTSpeechTranscriber cleanUp].cold.1
- -[AXLTSpeechTranscriber mediaServicesWereReset:].cold.1
- -[AXLTSpeechTranscriber resetTranscription].cold.1
- -[AXLTSpeechTranscriber resetTranscription].cold.2
- -[AXLTSpeechTranscriber setupAudioEngineTap].cold.1
- -[AXLTSpeechTranscriber setupAudioSession].cold.1
- -[AXLTSpeechTranscriber setupAudioSession].cold.2
- -[AXLTSpeechTranscriber setupAudioSession].cold.3
- -[AXLTSpeechTranscriber startTranscriptionWithLocale:error:].cold.1
- -[AXLTSpeechTranscriber startTranscriptionWithLocale:error:].cold.2
- -[AXLTSpeechTranscriber stopTranscription:].cold.1
- -[AXLTTranscriber _coalsecingTime].cold.1
- -[AXLTTranscriber _downloadAndInstallSpeechRecognizer].cold.1
- -[AXLTTranscriber appendAudioPCMBuffer:forPID:].cold.1
- -[AXLTTranscriber dealloc].cold.1
- -[AXLTTranscriber isAssetPending].cold.1
- -[AXLTTranscriber isAssetPending].cold.2
- -[AXLTTranscriber resumeTranscriptionForPID:].cold.1
- -[AXLTTranscriber resumeTranscriptionForPID:].cold.2
- -[AXLTTranscriber resumeTranscriptionForPID:].cold.3
- -[AXLTTranscriber speechRecognitionDidDetectSpeech:].cold.1
- -[AXLTTranscriber speechRecognitionTask:didFinishRecognition:].cold.1
- -[AXLTTranscriber speechRecognitionTask:didFinishSuccessfully:].cold.1
- -[AXLTTranscriber speechRecognitionTask:didHypothesizeTranscription:].cold.1
- -[AXLTTranscriber speechRecognitionTaskFinishedReadingAudio:].cold.1
- -[AXLTTranscriber speechRecognitionTaskWasCancelled:].cold.1
- -[AXLTTranscriber startTranscriptionForPID:appName:callback:completionCallback:].cold.1
- -[AXLTTranscriber startTranscriptionForPID:appName:callback:completionCallback:].cold.2
- -[AXLTTranscriber stopTranscriptionForPID:].cold.1
- -[AXLTTranscriber stopTranscriptionForPID:].cold.2
- -[AXLTTranscription _shouldUseNonUpdatingSegments].cold.1
- GCC_except_table0
- GCC_except_table1
- GCC_except_table15
- GCC_except_table5
- _OBJC_IVAR_$_AXLTAudioOutManager._avSystemController
- _OBJC_IVAR_$_AXLTAudioOutManager._subscribed
- _OBJC_IVAR_$_AXLTAudioOutTranscriber._silentSamplesTailCount
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- _OUTLINED_FUNCTION_4
- _OUTLINED_FUNCTION_5
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- ___38-[AXLTAudioOutManager _cleanupAllPids]_block_invoke
- ___39+[AXLTAudioOutManager isExcludedAppID:]_block_invoke
- ___44-[AXLTSpeechTranscriber setupAudioEngineTap]_block_invoke.cold.1
- ___49+[AXLTAudioOutManager isCurrentProcessAXUIServer]_block_invoke
- ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.355
- ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.358
- ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke.cold.1
- ___49-[AXLTSpeechTranscriber setupTranscriberIfNeeded]_block_invoke_2.cold.1
- ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.337
- ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.341
- ___51-[AXLTAudioOutTranscriber setupTranscriberIfNeeded]_block_invoke.cold.1
- ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke.346
- ___54-[AXLTTranscriber _downloadAndInstallSpeechRecognizer]_block_invoke_2.347
- ___57-[AXLTLanguageAssetManager deleteSpeechAssetForTaskHint:]_block_invoke.cold.1
- ___64-[AXLTAudioTextDumper saveAudioBuffer:appName:sessionStartTime:]_block_invoke.cold.1
- ___64-[AXLTAudioTextDumper saveAudioBuffer:appName:sessionStartTime:]_block_invoke.cold.2
- ___66-[AXLTAudioOutManager _someSessionIsPlayingDidChangeNotification:]_block_invoke
- ___68-[AXLTAudioTextDumper saveTranscribedText:appName:sessionStartTime:]_block_invoke.cold.1
- ___79-[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]_block_invoke.335
- ___79-[AXLTLanguageAssetManager downloadSpeechAssetForTaskHint:progress:completion:]_block_invoke.cold.1
- ___80-[AXLTTranscriber startTranscriptionForPID:appName:callback:completionCallback:]_block_invoke.337
- ___block_literal_global.361
- ___getAXSettingsClass_block_invoke.cold.1
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_LiveTranscription
- _handleInputBuffer.cold.1
- _isCurrentProcessAXUIServer._AXIsProcess
- _isCurrentProcessAXUIServer.token
- _isInternalInstall.cold.1
- _objc_msgSend$_calcHistogramForBuffer:packetCount:isSilence:
- _objc_msgSend$_cleanupAllPids
- _objc_msgSend$_setupAVSystemNotificationSystem
- _objc_msgSend$appInfoFromPid:
- _objc_msgSend$avSystemController
- _objc_msgSend$connect:to:format:
- _objc_msgSend$copy
- _objc_msgSend$installTapOnBus:bufferSize:format:block:
- _objc_msgSend$isCurrentProcessAXUIServer
- _objc_msgSend$registerForAVSystemControllerNotifications
- _objc_msgSend$setAvSystemController:
- _objc_msgSend$setSubscribed:
- _objc_msgSend$sharedAVSystemController
- _objc_msgSend$subscribed
- _objc_msgSend$unregisterForAVSystemControllerNotifications
- _objc_msgSend$updateAudioSessionsInfoFromSessionsArray:
- _objectdestroy.100Tm
- _objectdestroy.10Tm
- _objectdestroy.14Tm
- _objectdestroy.28Tm
- _objectdestroy.6Tm
- _objectdestroyTm
- _symbolic _____3key_Sd5valuetSg 10Foundation6LocaleV
CStrings:
+ "AudioManager: Audio session started for pid: %d, appName %@"
+ "AudioManager: Audio session stopped for pid: %d"
+ "AudioManager: Cleaning all PIDs info"
+ "AudioManager: Failed to start transcription for app: %{public}@, pid: %d, error: %@"
+ "AudioSessionsManager: All audio sessions: %@"
+ "AudioSessionsManager: Audio Sessions were updated"
+ "AudioSessionsManager: Audio server connection reset"
+ "AudioSessionsManager: Audio sessions: %@"
+ "AudioSessionsManager: Couldn't get appID for pid: %d"
+ "AudioSessionsManager: Couldn't get process handle for pid: %d, error: %@"
+ "AudioSessionsManager: Couldn't read appName from record, error: %@"
+ "AudioSessionsManager: Creating appID from name: %@"
+ "AudioSessionsManager: Creating appID from name: %{sensitive}@"
+ "AudioSessionsManager: Failed to register for Audio sessions events"
+ "AudioSessionsManager: Fetching process info, appID: %@, host: %@, Process handle name: %@, bundle: %@"
+ "AudioSessionsManager: Ignoring excluded app: %{public}@, pid: %d"
+ "AudioSessionsManager: Not subscribed to audio session updates, skip"
+ "AudioSessionsManager: Processing %lu audio sessions"
+ "AudioSessionsManager: Registered for Audio sessions events, systemController: %@"
+ "AudioSessionsManager: Skipping invalid pid"
+ "AudioSessionsManager: Starting session for app: %{public}@, pid: %d"
+ "AudioSessionsManager: Stopping session for pid: %d"
+ "AudioSessionsManager: Subscribing to Audio Server events"
+ "AudioSessionsManager: Unsubscribing from Audio Server events"
+ "AudioSessionsManager: Updating listener %@ isAnyAudioSessionActive: %d"
+ "AudioSessionsManager: Will notify a new listener %@ about %lu active sessions"
+ "AudioSessionsManager: audio is from app: %d, %@"
+ "AudioSessionsManager: registerForAudioUpdates, count: %@ added listener: %@"
+ "AudioSessionsManager: registerForAudioUpdates, no listeners, unregister from audio updates"
+ "AudioSessionsManager: unregisterFromAudioUpdates, count: %@, removed listener: %@"
+ "AudioSessionsManager: unregisterFromAudioUpdates, listeners count: %@"
+ "AudioTranscriber: Created for %@ %@"
+ "AudioTranscriber: Pause recognition for silence %@, pid %d, app: %@"
+ "AudioTranscriber: Resume recognition for pid %d, app: %@"
+ "com.apple.accessibility.LiveTranscription.audioSessionsQueue"
+ "v16@?0@\"<AXLCAudioSessionsManagerListener>\"8"
- "#16@0:8"
- "$defaultActor"
- ".cxx_destruct"
- "?"
- "@\"<AXLTLiveTranscriptionDelegate>\""
- "@\"<AXLTLockScreenObserverDelegate>\""
- "@\"<AXLTPhoneCallListenerDelegate>\""
- "@\"<AXLTTranscriberDelegateProtocol>\""
- "@\"<AXLTTranscriberDelegateProtocol>\"16@0:8"
- "@\"AVAudioBuffer\"20@?0I8^q12"
- "@\"AVAudioEngine\""
- "@\"AVAudioFile\""
- "@\"AVAudioFormat\""
- "@\"AVAudioSession\""
- "@\"AVSystemController\""
- "@\"AXLTLanguageAssetManager\""
- "@\"AXLTSpeechTranscriber\""
- "@\"AXLTTranscriber\""
- "@\"AXLTTranscription\""
- "@\"CXCallObserver\""
- "@\"NSArray\""
- "@\"NSDate\""
- "@\"NSLocale\""
- "@\"NSMapTable\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@\"SFSpeechAudioBufferRecognitionRequest\""
- "@\"SFSpeechRecognitionTask\""
- "@\"SFSpeechRecognizer\""
- "@\"SFTranscription\""
- "@\"TUCallCenter\""
- "@\"_TtC17LiveTranscription15AXLCTranscriber\""
- "@\"_TtC17LiveTranscription23AXLiveCaptionSourceInfo\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@28@0:8q16i24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8^f16q24"
- "@32@0:8^s16q24"
- "@32@0:8q16@24"
- "@36@0:8@16q24i32"
- "@36@0:8i16@20@28"
- "@36@0:8q16@24i32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@44@0:8q16i24@?28@?36"
- "@48@0:8^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16q24q32Q40"
- "@52@0:8q16i24@28@36@44"
- "@60@0:8i16@20@28@36@44q52"
- "@72@0:8@16q24@32i40@44@52q60B68"
- "@80@0:8@16q24@32i40@44@52q60B68q72"
- "@80@0:8q16@24@32@40@48@56@64q72"
- "@84@0:8@16q24@32i40@44@52q60B68q72B80"
- "@?"
- "@?16@0:8"
- "AXLTAudioInfo"
- "AXLTAudioOutManager"
- "AXLTAudioOutTranscriber"
- "AXLTAudioTextDumper"
- "AXLTHistogramCalculator"
- "AXLTLanguageAssetManager"
- "AXLTLiveTranscription"
- "AXLTLockScreenObserver"
- "AXLTPhoneCallListener"
- "AXLTSegmentUtilities"
- "AXLTSpeechTranscriber"
- "AXLTTimeUtilities"
- "AXLTTranscribedData"
- "AXLTTranscribedDataReceiver"
- "AXLTTranscriber"
- "AXLTTranscriberDelegateProtocol"
- "AXLTTranscriberProtocol"
- "AXLTTranscription"
- "AXLiveCaptions"
- "AudioManager Sessions: %@"
- "AudioManager Sessions: Failed to start transcription for app: %@, pid: %@"
- "AudioManager Sessions: Failed to stop transcription for pid: %d\n"
- "AudioManager Sessions: Ignore starting transcription for excluded app: %@, pid: %@"
- "AudioManager Sessions: Skip starting transcription pid: %d"
- "AudioManager Sessions: Skipping not valid pid"
- "AudioManager Sessions: Starting transcription for app: %@, pid: %@"
- "AudioManager Sessions: Stopping transcription for pid: %@"
- "AudioManager Sessions: Successfully started transcription for app: %@, pid: %@"
- "AudioManager Sessions: audio is from app: %d, %@"
- "AudioManager: Audio Sessions were updated"
- "AudioManager: Audio server connection reset"
- "AudioManager: Couldn't get appID for pid: %d"
- "AudioManager: Couldn't get process handle for pid: %d, error: %@"
- "AudioManager: Couldn't read appName from record, error = %@"
- "AudioManager: Creating appID from name: %@"
- "AudioManager: Creating appID from name: %{sensitive}@"
- "AudioManager: Failed to register for Audio server events"
- "AudioManager: Fetching process info, appID: %@, host: %@, Process handle name: %@, bundle %@"
- "AudioManager: Not subscribed to audio session updates, skip"
- "AudioManager: Processing Audio Sessions, active sessions number %@"
- "AudioManager: Registered for Audio server events"
- "AudioManager: Subscribing on Audio Server events"
- "AudioManager: Unsubscribing on Audio Server events"
- "B"
- "B16@0:8"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^@16"
- "B28@0:8I16^@20"
- "B28@0:8^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16I24"
- "B28@0:8i16^@20"
- "B32@0:8@\"NSLocale\"16^@24"
- "B32@0:8@16^@24"
- "B32@0:8q16^@24"
- "B36@0:8q16i24^@28"
- "B40@0:8q16@?24^@32"
- "B44@0:8i16@20^@28@?36"
- "B44@0:8q16i24@?28^@36"
- "B48@0:8q16@24@?32^@40"
- "B52@0:8i16@20@28@36^@44"
- "B52@0:8q16i24@?28@?36^@44"
- "B60@0:8i16@20@28@36@44^@52"
- "B60@0:8q16@24B32@36^@44@?52"
- "B60@0:8q16i24@28@?36@?44^@52"
- "CXCallObserverDelegate"
- "LiveTranscription"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Pause recognition for silence %@, pid %d, app: %@"
- "Q16@0:8"
- "SFSpeechRecognitionTaskDelegate"
- "SFSpeechRecognizerDelegate"
- "T#,R"
- "T@\"<AXLTLiveTranscriptionDelegate>\",W,N,V_delegate"
- "T@\"<AXLTLockScreenObserverDelegate>\",W,N,V_delegate"
- "T@\"<AXLTPhoneCallListenerDelegate>\",W,N,V_delegate"
- "T@\"<AXLTTranscriberDelegateProtocol>\",W,N"
- "T@\"<AXLTTranscriberDelegateProtocol>\",W,N,V_delegate"
- "T@\"<AXLTTranscriberDelegateProtocol>\",W,N,Vdelegate"
- "T@\"AVAudioEngine\",&,N,V_audioEngine"
- "T@\"AVAudioFile\",&,N,V_audioFile"
- "T@\"AVAudioFormat\",&,N,V_audioFormat"
- "T@\"AVAudioFormat\",&,N,V_tapFormat"
- "T@\"AVAudioSession\",&,N,V_audioSession"
- "T@\"AVSystemController\",&,N,V_avSystemController"
- "T@\"AXLTAudioOutManager\",R"
- "T@\"AXLTAudioTextDumper\",R"
- "T@\"AXLTLanguageAssetManager\",&,V_languageAssetManager"
- "T@\"AXLTLiveTranscription\",R"
- "T@\"AXLTSpeechTranscriber\",&,N,V_speechTranscriber"
- "T@\"AXLTTranscriber\",&,N,V_transcriber"
- "T@\"AXLTTranscriber\",&,V_transcriber"
- "T@\"AXLTTranscription\",&,N,V_currentTranscription"
- "T@\"AXLTTranscription\",&,N,V_transcription"
- "T@\"AXLiveCaptions\",N,R"
- "T@\"CXCallObserver\",&,N,V_callObserver"
- "T@\"NSArray\",&,N,V_audioHistogram"
- "T@\"NSArray\",&,N,V_nonUpdatingSegments"
- "T@\"NSArray\",N,C"
- "T@\"NSArray\",R,C,N"
- "T@\"NSAttributedString\",N,R"
- "T@\"NSDate\",&,N,V_bufferLogTime"
- "T@\"NSDate\",&,N,V_sessionStartTime"
- "T@\"NSDate\",&,N,V_textLogTime"
- "T@\"NSDate\",&,N,V_timestamp"
- "T@\"NSDate\",N,R"
- "T@\"NSLocale\",&,N,V_locale"
- "T@\"NSLocale\",N,C"
- "T@\"NSLocale\",R,N"
- "T@\"NSMapTable\",R,V_processToTranscriberMap"
- "T@\"NSMutableDictionary\",&,N,V_dataReceivers"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_bufferQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_saveQueue"
- "T@\"NSString\",&,N,V_appID"
- "T@\"NSString\",&,N,V_appName"
- "T@\"NSString\",&,N,V_filePath"
- "T@\"NSString\",&,N,V_textFileName"
- "T@\"NSString\",&,N,V_transcribedText"
- "T@\"NSString\",&,V_appName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",N,C"
- "T@\"NSString\",N,R"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSTimer\",&,V_audioBufferTimeoutTimer"
- "T@\"SFSpeechAudioBufferRecognitionRequest\",&,N,V_recognitionRequest"
- "T@\"SFSpeechRecognitionTask\",&,N,V_recognitionTask"
- "T@\"SFSpeechRecognitionTask\",&,N,V_task"
- "T@\"SFSpeechRecognizer\",&,N,V_recognizer"
- "T@\"SFTranscription\",&,N,V_transcription"
- "T@\"TUCallCenter\",&,N,V_callCenter"
- "T@\"_TtC17LiveTranscription15AXLCTranscriber\",&,N,V_transcriberV2"
- "T@\"_TtC17LiveTranscription15AXLCTranscriber\",N,R"
- "T@\"_TtC17LiveTranscription23AXLiveCaptionSourceInfo\",&,N,V_source"
- "T@\"_TtC17LiveTranscription23AXLiveCaptionSourceInfo\",N,R,Vsource"
- "T@?,C,V_completionCallback"
- "T@?,C,V_transcriptionCallback"
- "T@?,R,V_audioInfoBlock"
- "T@?,R,V_callbackBlock"
- "TB,N,GisSilence,V_silence"
- "TB,N,V_isV2"
- "TB,N,V_noPunctuation"
- "TB,N,V_suppressUsingIndependentInputRoute"
- "TB,N,Vprivileged"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_isTranscribing"
- "TB,V_isPending"
- "TB,V_isTranscribing"
- "TB,V_subscribed"
- "TQ,R"
- "T^{OpaqueAudioQueue=},N,V_audioQueue"
- "Ti,N,R,Vpid"
- "Ti,N,V_pid"
- "Ti,R,N,V_targetPID"
- "Ti,V_pid"
- "Tq,N"
- "Tq,N,R"
- "Tq,N,R,VassetState"
- "Tq,N,R,Vid"
- "Tq,N,R,VresultType"
- "Tq,N,R,VsourceType"
- "Tq,N,V_assetState"
- "Tq,N,V_downloadState"
- "Tq,N,V_requestType"
- "Tq,N,V_resultTypeV2"
- "Tq,N,V_silentBuffersCount"
- "Tq,N,V_silentSamplesTailCount"
- "Tq,N,V_taskHint"
- "Tq,N,V_transcriberVersion"
- "Tq,N,V_utilityType"
- "Tq,N,VactionType"
- "Tq,N,VprivilegedLength"
- "Tq,N,VresultType"
- "Tq,R,N,V_downloadProgress"
- "Tq,R,N,V_requestType"
- "Tq,V_downloadState"
- "UUID"
- "Vv16@0:8"
- "[1^{AudioQueueBuffer}]"
- "^{OpaqueAudioQueue=}"
- "^{OpaqueAudioQueue=}16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC17LiveTranscription11AXLTCaption"
- "_TtC17LiveTranscription13AXLiveCaption"
- "_TtC17LiveTranscription15AXLCTranscriber"
- "_TtC17LiveTranscription20AXLCTranscriberActor"
- "_TtC17LiveTranscription23AXLiveCaptionSourceInfo"
- "_appID"
- "_appName"
- "_appendBuffer:offsetInPackets:packetCount:"
- "_assetState"
- "_audioBufferTimeoutTimer"
- "_audioEngine"
- "_audioFile"
- "_audioFormat"
- "_audioHistogram"
- "_audioInfoBlock"
- "_audioQueue"
- "_audioSession"
- "_avSessionMediaServicesResetNotification:"
- "_avSystemController"
- "_avSystemController: %@"
- "_bufferLogTime"
- "_bufferQueue"
- "_calcHistogramForBuffer:packetCount:isSilence:"
- "_callCenter"
- "_callObserver"
- "_callbackBlock"
- "_cleanupAllPids"
- "_cleanupForPID:"
- "_coalsecingTime"
- "_completionCallback"
- "_currentTranscription"
- "_dataReceivers"
- "_delegate"
- "_deviceLanguage"
- "_downloadAndInstallSpeechRecognizer"
- "_downloadProgress"
- "_downloadState"
- "_dumpTestData"
- "_filePath"
- "_findSilencePacketOffset:packetCount:silentSamplesMin:zeroOffsetOnly:"
- "_handleAssetDownloadError:"
- "_initWithTranscribedText:requestType:timestamp:pid:appID:appName:assetState:silence:resultType:isV2:"
- "_isPending"
- "_isScreenLocked"
- "_isSilenceOnlyInBuffer:packetCount:"
- "_isTranscribing"
- "_isV2"
- "_languageAssetManager"
- "_locale"
- "_mBuffers"
- "_noPunctuation"
- "_nonUpdatingSegments"
- "_notifyLockStateToken"
- "_pauseSpeechRecognition"
- "_pid"
- "_processToTranscriberMap"
- "_receiverKeyForRequestType:targetPID:"
- "_recognitionRequest"
- "_recognitionTask"
- "_recognizer"
- "_registerScreenNotification"
- "_reportErrorWithCode:debugErrorString:cleanupForPID:"
- "_requestType"
- "_restartTranscription"
- "_resultTypeV2"
- "_saveQueue"
- "_sessionStartTime"
- "_setMaximumRecognitionDuration:"
- "_setupAVSystemNotificationSystem"
- "_shouldUseNonUpdatingSegments"
- "_silence"
- "_silentBuffersCount"
- "_silentSamplesTailCount"
- "_someSessionIsPlayingDidChangeNotification:"
- "_source"
- "_speechTranscriber"
- "_startObserving"
- "_startTranscriptionForPID:appID:appName:excludingPIDs:locale:error:"
- "_startTranscriptionForPID:appID:appName:locale:error:"
- "_stopTranscriptionForPID:error:"
- "_subscribed"
- "_suppressUsingIndependentInputRoute"
- "_tapDescriptionForPID:tapFormat:excludePIDs:"
- "_tapFormat"
- "_targetPID"
- "_task"
- "_taskHint"
- "_textFileName"
- "_textLogTime"
- "_timestamp"
- "_transcribedText"
- "_transcriber"
- "_transcriberV2"
- "_transcriberVersion"
- "_transcription"
- "_transcriptionCallback"
- "_updateScreenLock:"
- "_utilityType"
- "actionType"
- "addAudioPCMBuffer:for:"
- "addObject:"
- "addObserver:selector:name:object:"
- "addsPunctuation"
- "appID"
- "appInfoFromPid:"
- "appName"
- "appendAudioPCMBuffer:"
- "appendAudioPCMBuffer:forPID:"
- "arrayWithObjects:count:"
- "assetState"
- "attachNode:"
- "attributeForKey:"
- "attributedText"
- "audioBufferList"
- "audioBufferTimeoutTimer"
- "audioEngine"
- "audioEngineConfigurationDidChange:"
- "audioFile"
- "audioFormat"
- "audioHistogram"
- "audioInfoBlock"
- "audioInfoData:"
- "audioQueue"
- "audioSession"
- "audioTranscriber"
- "autorelease"
- "avSystemController"
- "bestAudioFormat"
- "bestTranscription"
- "boolForKey:"
- "bufferLogTime"
- "bufferQueue"
- "bundle"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "calcHistogramForBuffer:"
- "callCenter"
- "callObserver"
- "callObserver:callChanged:"
- "callStatusChanged:"
- "callUUID"
- "callbackBlock"
- "calls"
- "cancel"
- "caption"
- "channelCount"
- "class"
- "cleanUp"
- "cleanup"
- "clientCallback"
- "clients"
- "closeFile"
- "code"
- "commonFormat"
- "completionCallback"
- "conformsToProtocol:"
- "connect:to:format:"
- "containsObject:"
- "convertToBuffer:error:withInputFromBlock:"
- "converter"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAudioBuffersWithBufferByteSize:error:"
- "createFileAtPath:contents:attributes:"
- "currentCalls"
- "currentLocale"
- "currentThread"
- "currentTranscription"
- "currentVideoCalls"
- "d32@0:8@16@24"
- "dataReceivers"
- "dataUsingEncoding:"
- "date"
- "dateFromString:"
- "dateToString:"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "defaultCenter"
- "defaultLocaleWithCompletion:"
- "defaultLocaleWithCompletionHandler:"
- "defaultManager"
- "defaultTaskHint"
- "delegate"
- "deleteSpeechAssetForTaskHint:"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "downloadCompleted"
- "downloadError"
- "downloadProgress"
- "downloadSpeechAssetForTaskHint:progress:completion:"
- "downloadState"
- "encodeBool:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endAudio"
- "errorWithDomain:code:userInfo:"
- "f16@0:8"
- "fetchAssetWithConfig:clientIdentifier:progress:completion:"
- "fileHandleForUpdatingAtPath:"
- "filePath"
- "fileURLWithPath:"
- "finish"
- "floatForKey:"
- "floatValue"
- "format"
- "formattedLocaleIDsFrom:"
- "formattedString"
- "fractionCompleted"
- "frameCapacity"
- "frameLength"
- "handleAudioBuffer:audioQueue:timestamp:packetCount:packetDesc:"
- "handleForIdentifier:error:"
- "handleInputBufferWithContext:audioQueue:audioBuffer:timestamp:packetCount:packetDesc:"
- "hasConnected"
- "hasEnded"
- "hash"
- "histogramForAudioPCMBuffer:"
- "histogramForAudioQueueBuffer:packetCount:channelsCount:format:"
- "histogramForFloat32MonoBuffer:samplesCount:"
- "histogramForInt16MonoBuffer:samplesCount:"
- "hostProcess"
- "i"
- "i16@0:8"
- "id"
- "identifier"
- "identifierWithPid:"
- "init"
- "initForWriting:settings:commonFormat:interleaved:error:"
- "initFromFormat:toFormat:"
- "initProcessTapWithFormat:PID:"
- "initSessionForIndependentInputRoute"
- "initSystemTapWithFormat:excludePIDs:"
- "initWithAudioInfo:requestType:pid:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "initWithCaption:"
- "initWithCoder:"
- "initWithCommonFormat:sampleRate:channels:interleaved:"
- "initWithDelegate:"
- "initWithId:appID:appName:time:text:segments:placeholder:actionType:"
- "initWithId:liveCaption:"
- "initWithLanguage:taskHint:"
- "initWithLocale:"
- "initWithPCMFormat:frameCapacity:"
- "initWithPID:appID:appName:locale:delegate:transcriberVersion:"
- "initWithRecognitionTask:transcription:previousTranscription:"
- "initWithRequestType:targetPID:handler:audioInfoBlock:"
- "initWithSourceType:pid:appID:appName:locale:"
- "initWithStreamDescription:"
- "initWithSuiteName:"
- "initWithTapDescription:"
- "initWithTranscribedText:requestType:timestamp:pid:appID:appName:assetState:silence:"
- "initWithTranscribedText:requestType:timestamp:pid:appID:appName:assetState:silence:resultType:"
- "initWithTranscription:requestType:timestamp:pid:appID:appName:assetState:silence:"
- "initWithUUIDString:"
- "inputFormat"
- "inputNode"
- "inputStream"
- "inputStreamBuilder"
- "installTapOnBus:bufferSize:format:block:"
- "installedLanguagesForTaskHint:completion:"
- "installedLocalesWithCompletion:"
- "installedLocalesWithCompletionHandler:"
- "intValue"
- "isAssetPending"
- "isCallActive"
- "isCoreMediaNotificationsSupportedForPid:"
- "isCurrentProcessAXUIServer"
- "isEqual:"
- "isEqualToString:"
- "isExcludedAppID:"
- "isInterleaved"
- "isKindOfClass:"
- "isMainThread"
- "isMemberOfClass:"
- "isPending"
- "isProxy"
- "isPuncuation:"
- "isSilence"
- "isTranscribing"
- "isTranscribingForPID:"
- "isV2"
- "keyEnumerator"
- "languageAssetAvaliableForTaskHint:completion:"
- "languageAssetManager"
- "length"
- "liveCaptionsResult:"
- "liveCaptionsSelectedLocaleIdentifier"
- "liveTranscriptionAudioInfoDataArrived:"
- "locale"
- "localeIdentifier"
- "localeWithLocaleIdentifier:"
- "localesDownloadState"
- "localizedDescription"
- "localizedName"
- "localizedStringForDate:relativeToDate:"
- "localizedStringForKey:value:table:"
- "mainBundle"
- "mapUserTaskHint"
- "mediaServicesWereReset:"
- "mergeOldSegments:withNewSegments:"
- "micTranscriber"
- "mutableAudioBufferList"
- "mutableCopy"
- "name"
- "nextObject"
- "noPunctuation"
- "nonUpdatingSegments"
- "now"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "object"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "outputFormat"
- "outputFormatForBus:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "phoneCallListenerCallConnected:callID:"
- "phoneCallListenerCallDialing:"
- "phoneCallListenerCallEnded:callID:"
- "pid"
- "placeholder"
- "playing"
- "postNotificationName:object:"
- "prepare"
- "privileged"
- "privilegedLength"
- "processToTranscriberMap"
- "progressObserver"
- "punctuationCharacterSet"
- "q16@0:8"
- "q40@0:8^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16I24q28B36"
- "recognitionRequest"
- "recognitionTask"
- "recognitionTaskHint"
- "recognitionTaskWithRequest:delegate:"
- "recognizer"
- "registerForAVSystemControllerNotifications"
- "release"
- "removeAllObjects"
- "removeObjectForKey:"
- "removeObserver:name:object:"
- "removeTapOnBus:"
- "requestIdentifier"
- "requestType"
- "resetErrorStates"
- "resetTranscribing:"
- "resetTranscription"
- "respondsToSelector:"
- "resultType"
- "resultTypeV2"
- "resumeTranscriptionForPID:"
- "retain"
- "retainCount"
- "sampleRate"
- "saveAudioBuffer:appName:sessionStartTime:"
- "saveQueue"
- "saveTranscribedText:appName:sessionStartTime:"
- "screenLockStateChanged:"
- "seekToEndOfFile"
- "segments"
- "self"
- "sessionStartTime"
- "setActionType:"
- "setActive:withOptions:error:"
- "setAddsPunctuation:"
- "setAppID:"
- "setAppName:"
- "setAssetState:"
- "setAttribute:forKey:error:"
- "setAudioBufferTimeoutTimer:"
- "setAudioEngine:"
- "setAudioFile:"
- "setAudioFormat:"
- "setAudioHistogram:"
- "setAudioQueue:"
- "setAudioSession:"
- "setAvSystemController:"
- "setBufferLogTime:"
- "setBufferQueue:"
- "setCallCenter:"
- "setCallObserver:"
- "setCategory:withOptions:error:"
- "setCompletionCallback:"
- "setCurrentTranscription:"
- "setDataReceivers:"
- "setDateFormat:"
- "setDelegate:"
- "setDelegate:queue:"
- "setDetectMultipleUtterances:"
- "setDownloadState:"
- "setFilePath:"
- "setFrameLength:"
- "setIsPending:"
- "setIsTranscribing:"
- "setIsV2:"
- "setLanguageAssetManager:"
- "setLocale:"
- "setMXSessionProperty:value:error:"
- "setNoPunctuation:"
- "setNonUpdatingSegments:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPid:"
- "setPlaceholder:"
- "setPrivileged:"
- "setPrivilegedLength:"
- "setRecognitionRequest:"
- "setRecognitionTask:"
- "setRecognizer:"
- "setRequestType:"
- "setRequiresOnDeviceRecognition:"
- "setResultType:"
- "setResultTypeV2:"
- "setSaveQueue:"
- "setSegments:"
- "setSessionStartTime:"
- "setShouldReportPartialResults:"
- "setSilence:"
- "setSilentBuffersCount:"
- "setSilentSamplesTailCount:"
- "setSource:"
- "setSpeechTranscriber:"
- "setSubscribed:"
- "setSuppressUsingIndependentInputRoute:"
- "setTapFormat:"
- "setTask:"
- "setTaskHint:"
- "setTaskIdentifier:"
- "setText:"
- "setTextFileName:"
- "setTextLogTime:"
- "setTime:"
- "setTimestamp:"
- "setTranscribedText:"
- "setTranscriber:"
- "setTranscriberV2:"
- "setTranscriberVersion:"
- "setTranscription:"
- "setTranscriptionCallback:"
- "setUtilityType:"
- "settings"
- "setupAudioEngineTap"
- "setupAudioSession"
- "setupTranscriberIfNeeded"
- "shared"
- "sharedAVSystemController"
- "sharedInstance"
- "silence"
- "silentBuffersCount"
- "silentSamplesTailCount"
- "source"
- "sourceType"
- "speechAnalyzer"
- "speechRecognitionDidDetectSpeech:"
- "speechRecognitionTask:didFinishRecognition:"
- "speechRecognitionTask:didFinishSuccessfully:"
- "speechRecognitionTask:didHypothesizeTranscription:"
- "speechRecognitionTask:didProcessAudioDuration:"
- "speechRecognitionTaskFinishedReadingAudio:"
- "speechRecognitionTaskWasCancelled:"
- "speechRecognizer:availabilityDidChange:"
- "speechTranscriber"
- "standardUserDefaults"
- "startAndReturnError:"
- "startForPid:locale:error:transcriptionResult:"
- "startTranscribing:callbackBlock:error:"
- "startTranscribing:excludingPIDs:callbackBlock:error:"
- "startTranscribing:targetPID:callbackBlock:audioInfoBlock:error:"
- "startTranscribing:targetPID:callbackBlock:error:"
- "startTranscribing:targetPID:excludingPIDs:callbackBlock:audioInfoBlock:error:"
- "startTranscription:"
- "startTranscriptionFor:audioFormat:transcriberResult:"
- "startTranscriptionForPID:appID:appName:excludingPIDs:locale:error:"
- "startTranscriptionForPID:appName:callback:completionCallback:"
- "startTranscriptionWithLocale:error:"
- "startWithSource:locale:sharedRoute:excludePIDs:error:transcriptionResult:"
- "status"
- "stop"
- "stop:error:"
- "stopForPid:error:"
- "stopTranscribing:error:"
- "stopTranscribing:targetPID:error:"
- "stopTranscription:"
- "stopTranscriptionFor:"
- "stopTranscriptionForPID:"
- "stopTranscriptionForPID:error:"
- "streamDescription"
- "stringByAppendingPathComponent:"
- "stringByTrimmingCharactersInSet:"
- "stringFromDate:"
- "stringToDate:"
- "stringWithFormat:"
- "strongToStrongObjectsMapTable"
- "subscribed"
- "substring"
- "superclass"
- "supportedLocalesWithCompletion:"
- "supportedLocalesWithCompletionHandler:"
- "supportsOnDeviceRecognition"
- "supportsSecureCoding"
- "suppressUsingIndependentInputRoute"
- "tapFormat"
- "targetPID"
- "task"
- "taskHint"
- "taskIdentifier"
- "text"
- "textFileName"
- "textLogTime"
- "textWithConfidence"
- "time"
- "timeAgoSinceDate:currentDate:"
- "timeAgoSinceDateString:"
- "timeDifferenceDateStringOld:dateStringNew:"
- "timeIntervalSinceDate:"
- "timeStamp"
- "timestamp"
- "transcribedText"
- "transcriber"
- "transcriberOutputData:"
- "transcriberV2"
- "transcriberVersion"
- "transcription"
- "transcriptionCallback"
- "unregisterForAVSystemControllerNotifications"
- "unsubscribeFromAssetWithConfig:clientIdentifier:error:"
- "updateAudioSessionsInfoFromSessionsArray:"
- "userInfo"
- "utilityType"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"<AXLTTranscriberDelegateProtocol>\"16"
- "v24@0:8@\"AXLTAudioInfo\"16"
- "v24@0:8@\"AXLTTranscribedData\"16"
- "v24@0:8@\"AXLiveCaption\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"SFSpeechRecognitionTask\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSLocale\">16"
- "v24@0:8^{OpaqueAudioQueue=}16"
- "v24@0:8q16"
- "v28@0:8@\"SFSpeechRecognitionTask\"16B24"
- "v28@0:8@\"SFSpeechRecognizer\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v32@0:8@\"CXCallObserver\"16@\"CXCall\"24"
- "v32@0:8@\"SFSpeechRecognitionTask\"16@\"SFSpeechRecognitionResult\"24"
- "v32@0:8@\"SFSpeechRecognitionTask\"16@\"SFTranscription\"24"
- "v32@0:8@\"SFSpeechRecognitionTask\"16d24"
- "v32@0:8@16@24"
- "v32@0:8@16d24"
- "v32@0:8^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16I24B28"
- "v32@0:8^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16I24I28"
- "v32@0:8q16@?24"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8q16@?24@?32"
- "v44@0:8i16@20@?28@?36"
- "v52@0:8^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16^{OpaqueAudioQueue=}24r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}32I40r^{AudioStreamPacketDescription=qII}44"
- "v60@0:8^v16^{OpaqueAudioQueue=}24^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}32r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}40I48r^{AudioStreamPacketDescription=qII}52"
- "writeData:"
- "writeFromBuffer:error:"
- "zone"

```
