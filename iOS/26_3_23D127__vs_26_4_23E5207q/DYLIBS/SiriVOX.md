## SiriVOX

> `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX`

```diff

-3500.16.1.0.0
-  __TEXT.__text: 0x81d74
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_methlist: 0x80b0
-  __TEXT.__const: 0x94
-  __TEXT.__gcc_except_tab: 0x7b0
-  __TEXT.__cstring: 0x10a59
-  __TEXT.__oslogstring: 0x766b
+3520.28.1.0.0
+  __TEXT.__text: 0x84f14
+  __TEXT.__auth_stubs: 0x9a0
+  __TEXT.__objc_methlist: 0x8250
+  __TEXT.__const: 0xac
+  __TEXT.__constg_swiftt: 0x28
+  __TEXT.__swift5_typeref: 0x6
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__gcc_except_tab: 0x798
+  __TEXT.__cstring: 0x10e74
+  __TEXT.__oslogstring: 0x791e
   __TEXT.__dlopen_cstrs: 0xda
-  __TEXT.__unwind_info: 0x2210
-  __TEXT.__objc_classname: 0x2135
-  __TEXT.__objc_methname: 0x10fbf
-  __TEXT.__objc_methtype: 0x5348
-  __TEXT.__objc_stubs: 0xbca0
-  __DATA_CONST.__got: 0x6c0
-  __DATA_CONST.__const: 0x2ab8
-  __DATA_CONST.__objc_classlist: 0x600
+  __TEXT.__unwind_info: 0x2260
+  __TEXT.__objc_classname: 0x21be
+  __TEXT.__objc_methname: 0x115f8
+  __TEXT.__objc_methtype: 0x53d4
+  __TEXT.__objc_stubs: 0xbf80
+  __DATA_CONST.__got: 0x6d8
+  __DATA_CONST.__const: 0x2a78
+  __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x298
+  __DATA_CONST.__objc_protolist: 0x2a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37d8
+  __DATA_CONST.__objc_selrefs: 0x38c0
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x450
-  __DATA_CONST.__objc_arraydata: 0x940
-  __AUTH_CONST.__auth_got: 0x510
-  __AUTH_CONST.__const: 0x9e0
-  __AUTH_CONST.__cfstring: 0x5d80
-  __AUTH_CONST.__objc_const: 0x12188
+  __DATA_CONST.__objc_superrefs: 0x468
+  __DATA_CONST.__objc_arraydata: 0x960
+  __AUTH_CONST.__auth_got: 0x4e0
+  __AUTH_CONST.__const: 0xa20
+  __AUTH_CONST.__cfstring: 0x5e20
+  __AUTH_CONST.__objc_const: 0x126e0
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0xdf8
+  __AUTH_CONST.__objc_intobj: 0xe28
   __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH.__objc_data: 0x3c00
+  __AUTH.__objc_data: 0x3d40
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0xbc8
-  __DATA.__data: 0x1f28
+  __DATA.__objc_ivar: 0xc10
+  __DATA.__data: 0x1fe8
   __DATA.__bss: 0x238
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
   - /System/Library/PrivateFrameworks/SiriCore.framework/SiriCore
   - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration
+  - /System/Library/PrivateFrameworks/SiriDeviceSelection.framework/SiriDeviceSelection
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SiriModes.framework/SiriModes
   - /System/Library/PrivateFrameworks/SiriStates.framework/SiriStates

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 76CFB4CA-D0C0-3486-BBAF-BA47EF878CB8
-  Functions: 2910
-  Symbols:   10675
-  CStrings:  6210
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 95798335-065B-3EF1-BB05-38C962EB6C92
+  Functions: 2940
+  Symbols:   10823
+  CStrings:  6297
 
Symbols:
+ -[SVXAFConnectionManager .cxx_destruct]
+ -[SVXAFConnectionManager _createClientConfiguration:storeDemo:preferences:]
+ -[SVXAFConnectionManager connectionDelegate]
+ -[SVXAFConnectionManager getConnection:]
+ -[SVXAFConnectionManager initWithPerformer:instanceContext:preferences:]
+ -[SVXAFConnectionManager invalidateConnection]
+ -[SVXAFConnectionManager setConnectionDelegate:]
+ -[SVXAFConnectionManager updateClientConfigurationWithContext:storeDemo:createIfAbsent:]
+ -[SVXAceViewHandler firstTimestamp]
+ -[SVXAceViewHandler setFirstTimestamp:]
+ -[SVXAceViewHandler setTaskTrackers:]
+ -[SVXAceViewHandler taskTrackers]
+ -[SVXMyriadDeviceManager managingHostDevice]
+ -[SVXRequestPrewarmer .cxx_destruct]
+ -[SVXRequestPrewarmer _preheatWithStyle:]
+ -[SVXRequestPrewarmer initWithConnectionManager:speechSynthesizer:idleTimer:performer:]
+ -[SVXRequestPrewarmer preheatWithStyle:]
+ -[SVXRequestPrewarmer prewarmWithContext:completion:]
+ -[SVXServiceCommandResult convertToResponseForCommand:]
+ -[SVXSession allTimersIdle]
+ -[SVXSession connectionManager]
+ -[SVXSession handleDidChangeAudioSessionID:]
+ -[SVXSession handleShouldSpeak:]
+ -[SVXSession initWithPerformer:serviceCommandHandler:powerLevelManager:speechSynthesizer:connectionManager:requestPrewarmer:instanceContext:preferences:analytics:delegate:]
+ -[SVXSession requestPrewarmer]
+ -[SVXSessionFactory createWithPerformer:serviceCommandHandler:powerLevelManager:speechSynthesizer:connectionManager:requestPrewarmer:instanceContext:preferences:analytics:delegate:]
+ -[SVXSessionIdleAssertion initWithTimestamp:sessionTimer:]
+ -[SVXSessionIdleAssertion sessionTimer]
+ -[SVXSessionIdleTimer .cxx_destruct]
+ -[SVXSessionIdleTimer _handleSessionIdleTimerFireEventWithAssertion:timerInterval:]
+ -[SVXSessionIdleTimer _sessionIdleFiredWithAssertion:]
+ -[SVXSessionIdleTimer delegate]
+ -[SVXSessionIdleTimer init]
+ -[SVXSessionIdleTimer setDelegate:]
+ -[SVXSessionIdleTimer startSessionIdleTimerWithTimeInterval:]
+ -[SVXSessionIdleTimer stopSessionIdleTimer]
+ -[SVXSessionManager _sendActivationTriggerToDeviceSelection:]
+ -[SVXSpeechSynthesizer _handleDidFinishStreamingWithSpeechRequest:success:error:]
+ -[SVXSpeechSynthesizer _handleDidGenerateAudioChunkData:forSynthesisRequest:]
+ -[SVXSpeechSynthesizer _handleDidReceiveSpeechWordTimingInfoArray:forSynthesisRequest:]
+ -[SVXSpeechSynthesizer _withSpeechRequest:didGenerateAudioChunk:]
+ -[SVXSpeechSynthesizer _withSpeechRequest:didReceiveTimingInfo:]
+ -[SVXSpeechSynthesizer _withSynthesisRequest:didGenerateAudioChunk:]
+ -[SVXSpeechSynthesizer _withSynthesisRequest:didReceiveTimingInfo:]
+ -[SVXSpeechSynthesizer didFinishStreamingRequest:successfully:withError:]
+ GCC_except_table1068
+ GCC_except_table1083
+ GCC_except_table110
+ GCC_except_table1139
+ GCC_except_table1410
+ GCC_except_table1567
+ GCC_except_table1573
+ GCC_except_table1574
+ GCC_except_table1703
+ GCC_except_table1705
+ GCC_except_table1706
+ GCC_except_table1811
+ GCC_except_table2151
+ GCC_except_table2166
+ GCC_except_table2167
+ GCC_except_table2284
+ GCC_except_table2286
+ GCC_except_table2289
+ GCC_except_table2591
+ GCC_except_table2746
+ GCC_except_table2821
+ GCC_except_table2858
+ GCC_except_table2861
+ GCC_except_table2866
+ GCC_except_table2869
+ GCC_except_table322
+ GCC_except_table464
+ GCC_except_table475
+ GCC_except_table485
+ GCC_except_table693
+ _AFDeviceSupportsDeviceSelection
+ _OBJC_CLASS_$_DeviceSelectionSignalDonation
+ _OBJC_CLASS_$_DeviceSelectionTriggerContext
+ _OBJC_CLASS_$_DeviceSelectionTriggerSource
+ _OBJC_CLASS_$_OS_os_log
+ _OBJC_CLASS_$_SVXAFConnectionManager
+ _OBJC_CLASS_$_SVXRequestPrewarmer
+ _OBJC_CLASS_$_SVXSessionFactory
+ _OBJC_CLASS_$_SVXSessionIdleTimer
+ _OBJC_IVAR_$_SVXAFConnectionManager._connection
+ _OBJC_IVAR_$_SVXAFConnectionManager._connectionDelegate
+ _OBJC_IVAR_$_SVXAFConnectionManager._connectionFactory
+ _OBJC_IVAR_$_SVXAFConnectionManager._deviceSetupContext
+ _OBJC_IVAR_$_SVXAFConnectionManager._instanceContext
+ _OBJC_IVAR_$_SVXAFConnectionManager._performer
+ _OBJC_IVAR_$_SVXAFConnectionManager._preferences
+ _OBJC_IVAR_$_SVXAFConnectionManager._soundUtils
+ _OBJC_IVAR_$_SVXAceViewHandler._firstTimestamp
+ _OBJC_IVAR_$_SVXAceViewHandler._taskTrackers
+ _OBJC_IVAR_$_SVXRequestPrewarmer._connectionManager
+ _OBJC_IVAR_$_SVXRequestPrewarmer._idleTimer
+ _OBJC_IVAR_$_SVXRequestPrewarmer._performer
+ _OBJC_IVAR_$_SVXRequestPrewarmer._speechSynthesizer
+ _OBJC_IVAR_$_SVXSession._connectionManager
+ _OBJC_IVAR_$_SVXSession._idleTimer
+ _OBJC_IVAR_$_SVXSession._requestPrewarmer
+ _OBJC_IVAR_$_SVXSessionIdleAssertion._sessionTimer
+ _OBJC_IVAR_$_SVXSessionIdleTimer._delegate
+ _OBJC_IVAR_$_SVXSessionIdleTimer._performer
+ _OBJC_IVAR_$_SVXSessionIdleTimer._sessionIdleAssertions
+ _OBJC_IVAR_$_SVXSessionManager._sessionFactory
+ _OBJC_METACLASS_$_SVXAFConnectionManager
+ _OBJC_METACLASS_$_SVXRequestPrewarmer
+ _OBJC_METACLASS_$_SVXSessionFactory
+ _OBJC_METACLASS_$_SVXSessionIdleTimer
+ _TapToRadarKitLibraryCore.frameworkLibrary.8147
+ __OBJC_$_INSTANCE_METHODS_SVXAFConnectionManager
+ __OBJC_$_INSTANCE_METHODS_SVXRequestPrewarmer
+ __OBJC_$_INSTANCE_METHODS_SVXSessionFactory
+ __OBJC_$_INSTANCE_METHODS_SVXSessionIdleTimer
+ __OBJC_$_INSTANCE_VARIABLES_SVXAFConnectionManager
+ __OBJC_$_INSTANCE_VARIABLES_SVXRequestPrewarmer
+ __OBJC_$_INSTANCE_VARIABLES_SVXSessionIdleTimer
+ __OBJC_$_PROP_LIST_SVXAFConnectionManager
+ __OBJC_$_PROP_LIST_SVXAceViewHandler
+ __OBJC_$_PROP_LIST_SVXSessionIdleTimer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SVXAFConnectionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SVXSessionIdleTimerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SVXAFConnectionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SVXSessionIdleTimerDelegate
+ __OBJC_$_PROTOCOL_REFS_SVXAFConnectionDelegate
+ __OBJC_CLASS_RO_$_SVXAFConnectionManager
+ __OBJC_CLASS_RO_$_SVXRequestPrewarmer
+ __OBJC_CLASS_RO_$_SVXSessionFactory
+ __OBJC_CLASS_RO_$_SVXSessionIdleTimer
+ __OBJC_LABEL_PROTOCOL_$_SVXAFConnectionDelegate
+ __OBJC_LABEL_PROTOCOL_$_SVXSessionIdleTimerDelegate
+ __OBJC_METACLASS_RO_$_SVXAFConnectionManager
+ __OBJC_METACLASS_RO_$_SVXRequestPrewarmer
+ __OBJC_METACLASS_RO_$_SVXSessionFactory
+ __OBJC_METACLASS_RO_$_SVXSessionIdleTimer
+ __OBJC_PROTOCOL_$_SVXAFConnectionDelegate
+ __OBJC_PROTOCOL_$_SVXSessionIdleTimerDelegate
+ ___171-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:audioSessionID:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke.139
+ ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.109
+ ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.111
+ ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.119
+ ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.123
+ ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.124
+ ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke_2.125
+ ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke_2.131
+ ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke_3.132
+ ___27-[SVXSession allTimersIdle]_block_invoke
+ ___37-[SVXSession _resignActiveForReason:]_block_invoke.169
+ ___37-[SVXSession _resignActiveForReason:]_block_invoke.170
+ ___37-[SVXSession _resignActiveForReason:]_block_invoke.171
+ ___37-[SVXSession _resignActiveForReason:]_block_invoke.173
+ ___37-[SVXSession _resignActiveForReason:]_block_invoke.174
+ ___37-[SVXSession _resignActiveForReason:]_block_invoke.175
+ ___37-[SVXSession _resignActiveForReason:]_block_invoke_2.176
+ ___38-[SVXSpeechSynthesizer _startContext:]_block_invoke.71
+ ___38-[SVXSpeechSynthesizer _startContext:]_block_invoke.76
+ ___40-[SVXRequestPrewarmer preheatWithStyle:]_block_invoke
+ ___43-[SVXSession _checkIsActiveWithCompletion:]_block_invoke.165
+ ___43-[SVXSession _checkIsActiveWithCompletion:]_block_invoke.167
+ ___43-[SVXSessionIdleTimer stopSessionIdleTimer]_block_invoke
+ ___43-[SVXSessionManager _processNextOperations]_block_invoke.43
+ ___43-[SVXSessionManager _processNextOperations]_block_invoke.46
+ ___43-[SVXSessionManager _processNextOperations]_block_invoke.47
+ ___45-[SVXSessionManager queue:didEnqueueObjects:]_block_invoke.39
+ ___47-[SVXSpeechSynthesizer _processPendingContexts]_block_invoke.68
+ ___51-[SVXSession _presentError:taskTracker:completion:]_block_invoke.263
+ ___52-[SVXSessionManager activateWithContext:completion:]_block_invoke.37
+ ___53-[SVXRequestPrewarmer prewarmWithContext:completion:]_block_invoke
+ ___54-[SVXSession acquireAudioSessionForReason:completion:]_block_invoke.69
+ ___54-[SVXSession acquireAudioSessionForReason:completion:]_block_invoke.70
+ ___54-[SVXSession acquireAudioSessionForReason:completion:]_block_invoke.72
+ ___55-[SVXSessionManager _handleMyriadForActivationContext:]_block_invoke
+ ___56-[SVXSpeechSynthesizer _cancelPendingContextsAtIndexes:]_block_invoke.92
+ ___57-[SVXSessionManager _fetchStereoPairStateWithCompletion:]_block_invoke.62
+ ___57-[SVXSessionManager _fetchStereoPartnerLastMyriadWinDate]_block_invoke.60
+ ___59-[SVXSession _getAlarmAndTimerFiringContextWithCompletion:]_block_invoke.161
+ ___60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.86
+ ___60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.87
+ ___60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.90
+ ___60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke_2.88
+ ___60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke_3.89
+ ___61-[SVXSessionIdleTimer startSessionIdleTimerWithTimeInterval:]_block_invoke
+ ___61-[SVXSessionManager _sendActivationTriggerToDeviceSelection:]_block_invoke
+ ___62-[SVXSession _forceAudioSessionInactiveWithReason:completion:]_block_invoke.149
+ ___62-[SVXSession _forceAudioSessionInactiveWithReason:completion:]_block_invoke.150
+ ___64-[SVXSpeechSynthesizer _withSpeechRequest:didReceiveTimingInfo:]_block_invoke
+ ___65-[SVXSpeechSynthesizer _withSpeechRequest:didGenerateAudioChunk:]_block_invoke
+ ___66-[SVXSessionManager continuousVoiceTriggerDetectedWithCompletion:]_block_invoke.33
+ ___67-[SVXSpeechSynthesizer _withSynthesisRequest:didReceiveTimingInfo:]_block_invoke
+ ___68-[SVXSession _forceAudioSessionActiveWithOptions:reason:completion:]_block_invoke.148
+ ___68-[SVXSpeechSynthesizer _withSynthesisRequest:didGenerateAudioChunk:]_block_invoke
+ ___71-[SVXAceViewHandler handleAceView:isExpository:taskTracker:completion:]_block_invoke.14
+ ___71-[SVXAceViewHandler handleAceView:isExpository:taskTracker:completion:]_block_invoke.16
+ ___73-[SVXSpeechSynthesizer didFinishStreamingRequest:successfully:withError:]_block_invoke
+ ___75-[SVXAFConnectionManager _createClientConfiguration:storeDemo:preferences:]_block_invoke
+ ___76-[SVXSession _startActiveAudioSessionRequestForType:taskTracker:completion:]_block_invoke.144
+ ___88-[SVXAFConnectionManager updateClientConfigurationWithContext:storeDemo:createIfAbsent:]_block_invoke
+ ___Block_byref_object_copy_.13198
+ ___Block_byref_object_copy_.14003
+ ___Block_byref_object_copy_.9184
+ ___Block_byref_object_dispose_.13199
+ ___Block_byref_object_dispose_.14004
+ ___Block_byref_object_dispose_.9185
+ ___TapToRadarKitLibraryCore_block_invoke.8148
+ ___block_literal_global.10040
+ ___block_literal_global.11124
+ ___block_literal_global.1119
+ ___block_literal_global.11758
+ ___block_literal_global.11827
+ ___block_literal_global.11884
+ ___block_literal_global.12529
+ ___block_literal_global.12746
+ ___block_literal_global.12916
+ ___block_literal_global.12948
+ ___block_literal_global.13471
+ ___block_literal_global.156
+ ___block_literal_global.159
+ ___block_literal_global.18.6313
+ ___block_literal_global.1856
+ ___block_literal_global.193
+ ___block_literal_global.1955
+ ___block_literal_global.21.6305
+ ___block_literal_global.2252
+ ___block_literal_global.2475
+ ___block_literal_global.2830
+ ___block_literal_global.298
+ ___block_literal_global.2999
+ ___block_literal_global.3091
+ ___block_literal_global.3977
+ ___block_literal_global.4438
+ ___block_literal_global.4970
+ ___block_literal_global.5036
+ ___block_literal_global.5109
+ ___block_literal_global.5445
+ ___block_literal_global.5557
+ ___block_literal_global.5812
+ ___block_literal_global.629
+ ___block_literal_global.6321
+ ___block_literal_global.6554
+ ___block_literal_global.6786
+ ___block_literal_global.70
+ ___block_literal_global.7089
+ ___block_literal_global.746
+ ___block_literal_global.750
+ ___block_literal_global.8304
+ ___block_literal_global.8584
+ ___block_literal_global.8675
+ ___block_literal_global.9153
+ ___block_literal_global.9381
+ ___block_literal_global.9468
+ ___block_literal_global.9684
+ ___block_literal_global.9848
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SiriVOX
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SiriVOX
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SiriVOX
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SiriVOX
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_SiriVOX
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_SiriVOX
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_SiriVOX
+ _audit_stringTapToRadarKit.8163
+ _objc_msgSend$_handleDidFinishStreamingWithSpeechRequest:success:error:
+ _objc_msgSend$_handleDidGenerateAudioChunkData:forSynthesisRequest:
+ _objc_msgSend$_handleDidReceiveSpeechWordTimingInfoArray:forSynthesisRequest:
+ _objc_msgSend$_sendActivationTriggerToDeviceSelection:
+ _objc_msgSend$_withSpeechRequest:didReceiveTimingInfo:
+ _objc_msgSend$_withSynthesisRequest:didGenerateAudioChunk:
+ _objc_msgSend$_withSynthesisRequest:didReceiveTimingInfo:
+ _objc_msgSend$allTimersIdle
+ _objc_msgSend$connectionManager
+ _objc_msgSend$convertToResponseForCommand:
+ _objc_msgSend$createWithPerformer:serviceCommandHandler:powerLevelManager:speechSynthesizer:connectionManager:requestPrewarmer:instanceContext:preferences:analytics:delegate:
+ _objc_msgSend$donateTriggerSource:withCompletion:
+ _objc_msgSend$getConnection:
+ _objc_msgSend$handleDidChangeAudioSessionID:
+ _objc_msgSend$handleShouldSpeak:
+ _objc_msgSend$initWithConnectionManager:speechSynthesizer:idleTimer:performer:
+ _objc_msgSend$initWithIsConnectedToCarPlay:isSiriDisplayed:isSiriSpeaking:
+ _objc_msgSend$initWithPerformer:instanceContext:preferences:
+ _objc_msgSend$initWithPerformer:serviceCommandHandler:powerLevelManager:speechSynthesizer:connectionManager:requestPrewarmer:instanceContext:preferences:analytics:delegate:
+ _objc_msgSend$initWithTimestamp:sessionTimer:
+ _objc_msgSend$initWithTriggerType:context:
+ _objc_msgSend$invalidateConnection
+ _objc_msgSend$isConnectedToCarPlay
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$isSiriDisplayed
+ _objc_msgSend$isSiriSpeaking
+ _objc_msgSend$managingHostDevice
+ _objc_msgSend$requestPrewarmer
+ _objc_msgSend$setConnectionDelegate:
+ _objc_msgSend$startListenerSelectionWithDate:requestSessionId:resultCallback:
+ _objc_msgSend$startSessionIdleTimerWithTimeInterval:
+ _objc_msgSend$stopSessionIdleTimer
+ _objc_msgSend$updateClientConfigurationWithContext:storeDemo:createIfAbsent:
+ _objc_opt_self
+ _swift_getObjCClassMetadata
+ _swift_once
+ _swift_slowAlloc
+ _symbolic _____ 7SiriVOX6LoggerO
- -[SVXSession _connection:]
- -[SVXSession _createClientConfiguration:storeDemo:preferences:]
- -[SVXSession _handleDidChangeAudioSessionID:]
- -[SVXSession _handleSessionIdleTimerFireEventWithAssertion:timerInterval:]
- -[SVXSession _handleShouldSpeak:]
- -[SVXSession _invalidateConnection]
- -[SVXSession _preheatWithStyle:]
- -[SVXSession _sessionIdleFiredWithAssertion:]
- -[SVXSession _startSessionIdleTimerWithTimeInterval:]
- -[SVXSession _stopSessionIdleTimer]
- -[SVXSession initWithPerformer:serviceCommandHandler:powerLevelManager:speechSynthesizer:instanceContext:preferences:analytics:delegate:]
- -[SVXSession preheatWithStyle:]
- -[SVXSession prewarmWithContext:completion:]
- -[SVXSessionIdleAssertion initWithTimestamp:session:]
- -[SVXSessionIdleAssertion session]
- -[SVXSpeechSynthesizer withRequest:didGenerateAudioChunk:]
- -[SVXSpeechSynthesizer withRequest:didReceiveTimingInfo:]
- GCC_except_table1047
- GCC_except_table109
- GCC_except_table1108
- GCC_except_table1372
- GCC_except_table1526
- GCC_except_table1532
- GCC_except_table1533
- GCC_except_table1661
- GCC_except_table1663
- GCC_except_table1664
- GCC_except_table1769
- GCC_except_table2101
- GCC_except_table2115
- GCC_except_table2130
- GCC_except_table2131
- GCC_except_table2248
- GCC_except_table2250
- GCC_except_table2253
- GCC_except_table2562
- GCC_except_table2717
- GCC_except_table2792
- GCC_except_table2829
- GCC_except_table2832
- GCC_except_table2837
- GCC_except_table2840
- GCC_except_table326
- GCC_except_table468
- GCC_except_table479
- GCC_except_table489
- GCC_except_table688
- _OBJC_IVAR_$_SVXSession._connection
- _OBJC_IVAR_$_SVXSession._connectionFactory
- _OBJC_IVAR_$_SVXSession._sessionIdleAssertions
- _OBJC_IVAR_$_SVXSessionIdleAssertion._session
- _SVXLocalizationTableDeviceSetup
- _SVXLocalizationTableInterstitials
- _TapToRadarKitLibraryCore.frameworkLibrary.8017
- ___171-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:audioSessionID:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke.153
- ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.132
- ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.133
- ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.137
- ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.138
- ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.144
- ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke_2.139
- ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke_2.145
- ___194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke_3.146
- ___31-[SVXSession preheatWithStyle:]_block_invoke
- ___37-[SVXSession _resignActiveForReason:]_block_invoke.184
- ___37-[SVXSession _resignActiveForReason:]_block_invoke.185
- ___37-[SVXSession _resignActiveForReason:]_block_invoke.186
- ___37-[SVXSession _resignActiveForReason:]_block_invoke.188
- ___37-[SVXSession _resignActiveForReason:]_block_invoke.189
- ___37-[SVXSession _resignActiveForReason:]_block_invoke.190
- ___37-[SVXSession _resignActiveForReason:]_block_invoke_2.191
- ___38-[SVXSpeechSynthesizer _startContext:]_block_invoke.52
- ___38-[SVXSpeechSynthesizer _startContext:]_block_invoke.57
- ___39-[SVXSession updateDeviceSetupContext:]_block_invoke
- ___43-[SVXSession _checkIsActiveWithCompletion:]_block_invoke.180
- ___43-[SVXSession _checkIsActiveWithCompletion:]_block_invoke.182
- ___43-[SVXSessionManager _processNextOperations]_block_invoke.37
- ___43-[SVXSessionManager _processNextOperations]_block_invoke.40
- ___43-[SVXSessionManager _processNextOperations]_block_invoke.41
- ___44-[SVXSession prewarmWithContext:completion:]_block_invoke
- ___45-[SVXSession _sessionIdleFiredWithAssertion:]_block_invoke
- ___45-[SVXSessionManager queue:didEnqueueObjects:]_block_invoke.35
- ___47-[SVXSession taskTrackingCenterWillBecomeBusy:]_block_invoke
- ___47-[SVXSpeechSynthesizer _processPendingContexts]_block_invoke.49
- ___51-[SVXSession _presentError:taskTracker:completion:]_block_invoke.278
- ___52-[SVXSessionManager activateWithContext:completion:]_block_invoke.33
- ___53-[SVXSession _startSessionIdleTimerWithTimeInterval:]_block_invoke
- ___54-[SVXSession acquireAudioSessionForReason:completion:]_block_invoke.90
- ___54-[SVXSession acquireAudioSessionForReason:completion:]_block_invoke.91
- ___54-[SVXSession acquireAudioSessionForReason:completion:]_block_invoke.93
- ___56-[SVXSpeechSynthesizer _cancelPendingContextsAtIndexes:]_block_invoke.73
- ___57-[SVXSessionManager _fetchStereoPairStateWithCompletion:]_block_invoke.56
- ___57-[SVXSessionManager _fetchStereoPartnerLastMyriadWinDate]_block_invoke.54
- ___57-[SVXSpeechSynthesizer withRequest:didReceiveTimingInfo:]_block_invoke
- ___58-[SVXSpeechSynthesizer withRequest:didGenerateAudioChunk:]_block_invoke
- ___59-[SVXSession _getAlarmAndTimerFiringContextWithCompletion:]_block_invoke.176
- ___60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.67
- ___60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.68
- ___60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.71
- ___60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke_2.69
- ___60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke_3.70
- ___62-[SVXSession _forceAudioSessionInactiveWithReason:completion:]_block_invoke.164
- ___62-[SVXSession _forceAudioSessionInactiveWithReason:completion:]_block_invoke.165
- ___63-[SVXServiceCommandHandler handleResult:forCommand:completion:]_block_invoke
- ___63-[SVXServiceCommandHandler handleResult:forCommand:completion:]_block_invoke_2
- ___63-[SVXServiceCommandHandler handleResult:forCommand:completion:]_block_invoke_3
- ___63-[SVXServiceCommandHandler handleResult:forCommand:completion:]_block_invoke_4
- ___63-[SVXServiceCommandHandler handleResult:forCommand:completion:]_block_invoke_5
- ___63-[SVXSession _createClientConfiguration:storeDemo:preferences:]_block_invoke
- ___68-[SVXSession _forceAudioSessionActiveWithOptions:reason:completion:]_block_invoke.163
- ___71-[SVXAceViewHandler handleAceView:isExpository:taskTracker:completion:]_block_invoke.13
- ___71-[SVXAceViewHandler handleAceView:isExpository:taskTracker:completion:]_block_invoke.15
- ___76-[SVXSession _startActiveAudioSessionRequestForType:taskTracker:completion:]_block_invoke.159
- ___Block_byref_object_copy_.12981
- ___Block_byref_object_copy_.13784
- ___Block_byref_object_copy_.9035
- ___Block_byref_object_dispose_.12982
- ___Block_byref_object_dispose_.13785
- ___Block_byref_object_dispose_.9036
- ___TapToRadarKitLibraryCore_block_invoke.8018
- ___block_descriptor_40_e8_32bs_e33_v16?0"AceObject<SAAceCommand>"8ls32l8
- ___block_descriptor_48_e8_32s40bs_e21_v24?0q8"NSString"16ls40l8s32l8
- ___block_descriptor_72_e8_32s40bs48bs56bs64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.10953
- ___block_literal_global.1116
- ___block_literal_global.11576
- ___block_literal_global.11645
- ___block_literal_global.11727
- ___block_literal_global.12314
- ___block_literal_global.12528
- ___block_literal_global.12698
- ___block_literal_global.12730
- ___block_literal_global.13252
- ___block_literal_global.171
- ___block_literal_global.174
- ___block_literal_global.18.6226
- ___block_literal_global.1858
- ___block_literal_global.1957
- ___block_literal_global.208
- ___block_literal_global.21.6218
- ___block_literal_global.2299
- ___block_literal_global.2519
- ___block_literal_global.2874
- ___block_literal_global.3044
- ___block_literal_global.3136
- ___block_literal_global.314
- ___block_literal_global.3992
- ___block_literal_global.4459
- ___block_literal_global.4986
- ___block_literal_global.5052
- ___block_literal_global.51.13208
- ___block_literal_global.5126
- ___block_literal_global.5410
- ___block_literal_global.5522
- ___block_literal_global.5776
- ___block_literal_global.621
- ___block_literal_global.6234
- ___block_literal_global.6433
- ___block_literal_global.6665
- ___block_literal_global.6968
- ___block_literal_global.767
- ___block_literal_global.771
- ___block_literal_global.8177
- ___block_literal_global.8457
- ___block_literal_global.8548
- ___block_literal_global.9229
- ___block_literal_global.9316
- ___block_literal_global.9531
- ___block_literal_global.9695
- ___block_literal_global.9887
- _audit_stringTapToRadarKit.8033
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_connection:
- _objc_msgSend$_handleDidChangeAudioSessionID:
- _objc_msgSend$_handleShouldSpeak:
- _objc_msgSend$_invalidateConnection
- _objc_msgSend$_startSessionIdleTimerWithTimeInterval:
- _objc_msgSend$_stopSessionIdleTimer
- _objc_msgSend$initWithPerformer:serviceCommandHandler:powerLevelManager:speechSynthesizer:instanceContext:preferences:analytics:delegate:
- _objc_msgSend$initWithTimestamp:session:
- _objc_msgSend$withRequest:didGenerateAudioChunk:
- _objc_msgSend$withRequest:didReceiveTimingInfo:
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
CStrings:
+ "%@ {timestamp = %llu, sessionTimer = %@}"
+ "%s #deviceSelection Device lost election. Abort UI session."
+ "%s #deviceSelection Device won election. Continue UI session."
+ "%s #deviceSelection Donating activation with type(%@), isConnectedToCarPlay %d, isSiriDisplayed %d, isSiriSpeaking %d"
+ "%s #deviceSelection Failed to donate Siri activation trigger source: %@"
+ "%s #deviceSelection Starting device selection."
+ "%s #deviceSelection Successfully donated Siri activation trigger source."
+ "%s Streaming speechRequest = %@, success = %d, error = %@"
+ "%s TTS session = %@, request = %@, finishedStreaming = %d, error = %@"
+ "%s siri_signpost_begin `%s`"
+ "%s synthesisRequest = %@, audioChunkData = %@"
+ "%s synthesisRequest = %@, speechWordTimingInfoArray = %@"
+ "-[SVXAFConnectionManager getConnection:]"
+ "-[SVXAFConnectionManager invalidateConnection]"
+ "-[SVXRequestPrewarmer _preheatWithStyle:]"
+ "-[SVXSession allTimersIdle]_block_invoke"
+ "-[SVXSession handleDidChangeAudioSessionID:]"
+ "-[SVXSession handleShouldSpeak:]"
+ "-[SVXSession initWithPerformer:serviceCommandHandler:powerLevelManager:speechSynthesizer:connectionManager:requestPrewarmer:instanceContext:preferences:analytics:delegate:]"
+ "-[SVXSessionIdleTimer _handleSessionIdleTimerFireEventWithAssertion:timerInterval:]"
+ "-[SVXSessionIdleTimer _sessionIdleFiredWithAssertion:]"
+ "-[SVXSessionIdleTimer startSessionIdleTimerWithTimeInterval:]"
+ "-[SVXSessionIdleTimer stopSessionIdleTimer]_block_invoke"
+ "-[SVXSessionManager _handleMyriadForActivationContext:]_block_invoke"
+ "-[SVXSessionManager _sendActivationTriggerToDeviceSelection:]"
+ "-[SVXSessionManager _sendActivationTriggerToDeviceSelection:]_block_invoke"
+ "-[SVXSessionManager continuousVoiceTriggerDetectedWithCompletion:]_block_invoke"
+ "-[SVXSpeechSynthesizer _handleDidFinishStreamingWithSpeechRequest:success:error:]"
+ "-[SVXSpeechSynthesizer _handleDidGenerateAudioChunkData:forSynthesisRequest:]"
+ "-[SVXSpeechSynthesizer _handleDidReceiveSpeechWordTimingInfoArray:forSynthesisRequest:]"
+ "-[SVXSpeechSynthesizer _withSpeechRequest:didGenerateAudioChunk:]"
+ "-[SVXSpeechSynthesizer _withSpeechRequest:didReceiveTimingInfo:]"
+ "-[SVXSpeechSynthesizer _withSpeechRequest:didReceiveTimingInfo:]_block_invoke"
+ "-[SVXSpeechSynthesizer _withSynthesisRequest:didGenerateAudioChunk:]"
+ "-[SVXSpeechSynthesizer _withSynthesisRequest:didReceiveTimingInfo:]"
+ "-[SVXSpeechSynthesizer _withSynthesisRequest:didReceiveTimingInfo:]_block_invoke"
+ "-[SVXSpeechSynthesizer didFinishStreamingRequest:successfully:withError:]"
+ "@\"<SVXAFConnectionDelegate>\""
+ "@\"<SVXSessionIdleTimerDelegate>\""
+ "@\"SVXAFConnectionManager\""
+ "@\"SVXRequestPrewarmer\""
+ "@\"SVXSessionFactory\""
+ "@\"SVXSessionIdleTimer\""
+ "Button Press"
+ "SVXAFConnectionDelegate"
+ "SVXAFConnectionManager"
+ "SVXRequestPrewarmer"
+ "SVXSessionFactory"
+ "SVXSessionIdleTimer"
+ "SVXSessionIdleTimerDelegate"
+ "T@\"<SVXAFConnectionDelegate>\",W,N,V_connectionDelegate"
+ "T@\"<SVXSessionIdleTimerDelegate>\",W,N,V_delegate"
+ "T@\"NSMutableDictionary\",&,N,V_taskTrackers"
+ "T@\"SVXAFConnectionManager\",R,N,V_connectionManager"
+ "T@\"SVXRequestPrewarmer\",R,N,V_requestPrewarmer"
+ "T@\"SVXSessionIdleTimer\",R,N,V_sessionTimer"
+ "TQ,N,V_firstTimestamp"
+ "Voice"
+ "_connectionDelegate"
+ "_connectionManager"
+ "_firstTimestamp"
+ "_handleDidFinishStreamingWithSpeechRequest:success:error:"
+ "_handleDidGenerateAudioChunkData:forSynthesisRequest:"
+ "_handleDidReceiveSpeechWordTimingInfoArray:forSynthesisRequest:"
+ "_idleTimer"
+ "_requestPrewarmer"
+ "_sendActivationTriggerToDeviceSelection:"
+ "_sessionFactory"
+ "_sessionTimer"
+ "_taskTrackers"
+ "_withSpeechRequest:didGenerateAudioChunk:"
+ "_withSpeechRequest:didReceiveTimingInfo:"
+ "_withSynthesisRequest:didGenerateAudioChunk:"
+ "_withSynthesisRequest:didReceiveTimingInfo:"
+ "allTimersIdle"
+ "com.apple.siri.SVXSessionIdleTimer"
+ "connectionDelegate"
+ "connectionManager"
+ "connectionManager != nil"
+ "convertToResponseForCommand:"
+ "createWithPerformer:serviceCommandHandler:powerLevelManager:speechSynthesizer:connectionManager:requestPrewarmer:instanceContext:preferences:analytics:delegate:"
+ "didFinishStreamingRequest:successfully:withError:"
+ "donateTriggerSource:withCompletion:"
+ "firstTimestamp"
+ "getConnection:"
+ "handleDidChangeAudioSessionID:"
+ "handleShouldSpeak:"
+ "initWithConnectionManager:speechSynthesizer:idleTimer:performer:"
+ "initWithIsConnectedToCarPlay:isSiriDisplayed:isSiriSpeaking:"
+ "initWithPerformer:instanceContext:preferences:"
+ "initWithPerformer:serviceCommandHandler:powerLevelManager:speechSynthesizer:connectionManager:requestPrewarmer:instanceContext:preferences:analytics:delegate:"
+ "initWithTimestamp:sessionTimer:"
+ "initWithTriggerType:context:"
+ "invalidateConnection"
+ "isConnectedToCarPlay"
+ "isSiriDisplayed"
+ "isSiriSpeaking"
+ "managingHostDevice"
+ "requestPrewarmer"
+ "requestPrewarmer != nil"
+ "sessionTimer"
+ "setConnectionDelegate:"
+ "setFirstTimestamp:"
+ "setTaskTrackers:"
+ "startListenerSelectionWithDate:requestSessionId:resultCallback:"
+ "startSessionIdleTimerWithTimeInterval:"
+ "stopSessionIdleTimer"
+ "streamChunkRejected"
+ "streamNotFound"
+ "taskTrackers"
+ "updateClientConfigurationWithContext:storeDemo:createIfAbsent:"
+ "v36@0:8@16@24B32"
+ "\xf0\xc1"
- "%@ {timestamp = %llu, session = %@}"
- "-[SVXSession _connection:]"
- "-[SVXSession _handleDidChangeAudioSessionID:]"
- "-[SVXSession _handleSessionIdleTimerFireEventWithAssertion:timerInterval:]"
- "-[SVXSession _handleShouldSpeak:]"
- "-[SVXSession _invalidateConnection]"
- "-[SVXSession _preheatWithStyle:]"
- "-[SVXSession _sessionIdleFiredWithAssertion:]"
- "-[SVXSession _sessionIdleFiredWithAssertion:]_block_invoke"
- "-[SVXSession _startSessionIdleTimerWithTimeInterval:]"
- "-[SVXSession _stopSessionIdleTimer]"
- "-[SVXSession initWithPerformer:serviceCommandHandler:powerLevelManager:speechSynthesizer:instanceContext:preferences:analytics:delegate:]"
- "-[SVXSpeechSynthesizer withRequest:didGenerateAudioChunk:]"
- "-[SVXSpeechSynthesizer withRequest:didReceiveTimingInfo:]"
- "-[SVXSpeechSynthesizer withRequest:didReceiveTimingInfo:]_block_invoke"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "DeviceSetup"
- "Interstitials"
- "T@\"SVXSession\",R,N,V_session"
- "_connection:"
- "_handleDidChangeAudioSessionID:"
- "_handleShouldSpeak:"
- "_invalidateConnection"
- "_session"
- "_startSessionIdleTimerWithTimeInterval:"
- "_stopSessionIdleTimer"
- "initWithPerformer:serviceCommandHandler:powerLevelManager:speechSynthesizer:instanceContext:preferences:analytics:delegate:"
- "initWithTimestamp:session:"
- "session"
- "v24@?0q8@\"NSString\"16"
- "withRequest:didGenerateAudioChunk:"
- "withRequest:didReceiveTimingInfo:"
- "\xf0\xd1"

```
