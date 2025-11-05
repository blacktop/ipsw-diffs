## SiriVOX

> `/System/Library/PrivateFrameworks/SiriVOX.framework/Versions/A/SiriVOX`

```diff

-3402.8.1.0.0
-  __TEXT.__text: 0x89f34
+3404.25.1.0.0
+  __TEXT.__text: 0x89c3c
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x6750
+  __TEXT.__objc_methlist: 0x7fd0
   __TEXT.__const: 0x9c
-  __TEXT.__gcc_except_tab: 0x83c
-  __TEXT.__cstring: 0x1075a
+  __TEXT.__gcc_except_tab: 0x7b0
+  __TEXT.__cstring: 0x106c4
   __TEXT.__oslogstring: 0x7348
   __TEXT.__dlopen_cstrs: 0xda
   __TEXT.__ustring: 0x6c
-  __TEXT.__unwind_info: 0x2288
-  __TEXT.__objc_classname: 0x211d
-  __TEXT.__objc_methname: 0x10a77
-  __TEXT.__objc_methtype: 0x51f8
-  __TEXT.__objc_stubs: 0xb820
-  __DATA_CONST.__got: 0x698
-  __DATA_CONST.__const: 0xed8
-  __DATA_CONST.__objc_classlist: 0x5f8
+  __TEXT.__unwind_info: 0x2230
+  __TEXT.__objc_classname: 0x2134
+  __TEXT.__objc_methname: 0x10cf6
+  __TEXT.__objc_methtype: 0x528b
+  __TEXT.__objc_stubs: 0xba00
+  __DATA_CONST.__got: 0x6a0
+  __DATA_CONST.__const: 0xf10
+  __DATA_CONST.__objc_classlist: 0x600
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3530
+  __DATA_CONST.__objc_selrefs: 0x3728
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x450
   __DATA_CONST.__objc_arraydata: 0xa10
   __AUTH_CONST.__auth_got: 0x3f0
-  __AUTH_CONST.__const: 0x2ab0
+  __AUTH_CONST.__const: 0x29f0
   __AUTH_CONST.__cfstring: 0x5dc0
-  __AUTH_CONST.__objc_const: 0x14a80
+  __AUTH_CONST.__objc_const: 0x12078
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0xde0
   __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH.__objc_data: 0x3bb0
+  __AUTH.__objc_data: 0x3c00
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0xba8
+  __DATA.__objc_ivar: 0xbb0
   __DATA.__data: 0x1f28
   __DATA.__bss: 0x238
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /System/Library/PrivateFrameworks/UserActivity.framework/Versions/A/UserActivity
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2ED667A8-FC9B-3271-9D1F-D24BFFF8F263
-  Functions: 2957
-  Symbols:   7802
-  CStrings:  6134
+  UUID: 9BCC7921-27C3-303F-AC71-D738DCE8B4D9
+  Functions: 2945
+  Symbols:   7821
+  CStrings:  6156
 
Symbols:
+ -[SVXAFSiriTetherFactory createWithInstanceContext:]
+ -[SVXClientActivationService _buttonHoldToPreheatThreshold]
+ -[SVXClientActivationService _buttonHoldToTalkThreshold]
+ -[SVXClientActivationService _timeIntervalBetweenButtonUpTime:lastActivationButtonTime:]
+ -[SVXClientActivationService _validateButtonEventForActivation:]
+ -[SVXClientActivationService _validateSystemEventForActivation:]
+ -[SVXSessionManager _beginMonitoringAvailability]
+ -[SVXSessionManager _deviceSetupIsActive:endDate:recencyDuration:]
+ -[SVXSessionManager _deviceSupportsSiriMUX]
+ -[SVXSessionManager _stopMonitoringAvailability]
+ -[SVXSessionManager initWithModule:enableMyriad:]
+ -[SVXSessionUtils isSpeechRecordingAllowedWithActivationContext:]
+ -[SVXSessionUtils isVoiceTriggerWithActivationContext:]
+ GCC_except_table1072
+ GCC_except_table1133
+ GCC_except_table1397
+ GCC_except_table1550
+ GCC_except_table1558
+ GCC_except_table1559
+ GCC_except_table1796
+ GCC_except_table2129
+ GCC_except_table2143
+ GCC_except_table2160
+ GCC_except_table2161
+ GCC_except_table2282
+ GCC_except_table2285
+ GCC_except_table2596
+ GCC_except_table2752
+ GCC_except_table2827
+ GCC_except_table2864
+ GCC_except_table2867
+ GCC_except_table2873
+ GCC_except_table2876
+ GCC_except_table482
+ GCC_except_table499
+ GCC_except_table511
+ GCC_except_table714
+ OBJC_IVAR_$_SVXSession._sessionUtils
+ OBJC_IVAR_$_SVXSessionManager._tetherFactory
+ OBJC_IVAR_$_SVXTapToRadarManager._performer
+ TapToRadarKitLibraryCore.frameworkLibrary.7985
+ _OBJC_CLASS_$_AFNotifyObserver
+ _OBJC_CLASS_$_SVXAFSiriTetherFactory
+ _OBJC_METACLASS_$_SVXAFSiriTetherFactory
+ __156-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke.180
+ __156-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke.188
+ __156-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke_2.181
+ __156-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke_3.182
+ __156-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke_4.183
+ __181-[SVXSession activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:completion:]_block_invoke.80
+ __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.150
+ __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.155
+ __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.160
+ __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.163
+ __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.173
+ __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke_2.164
+ __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke_2.174
+ __37-[SVXSession _resignActiveForReason:]_block_invoke.230
+ __37-[SVXSession _resignActiveForReason:]_block_invoke.234
+ __37-[SVXSession _resignActiveForReason:]_block_invoke.240
+ __37-[SVXSession _resignActiveForReason:]_block_invoke.244
+ __38-[SVXSpeechSynthesizer _startContext:]_block_invoke.60
+ __38-[SVXSpeechSynthesizer _startContext:]_block_invoke.65
+ __43-[SVXSession _checkIsActiveWithCompletion:]_block_invoke.222
+ __43-[SVXSession _checkIsActiveWithCompletion:]_block_invoke.224
+ __43-[SVXSessionManager _processNextOperations]_block_invoke.68
+ __43-[SVXSessionManager _processNextOperations]_block_invoke.72
+ __43-[SVXSessionManager _processNextOperations]_block_invoke.78
+ __43-[SVXSessionManager _processNextOperations]_block_invoke.79
+ __45-[SVXSessionManager queue:didEnqueueObjects:]_block_invoke.66
+ __47-[SVXSession deactivateWithContext:completion:]_block_invoke.86
+ __47-[SVXSpeechSynthesizer _processPendingContexts]_block_invoke.57
+ __51-[SVXSession _presentError:taskTracker:completion:]_block_invoke.342
+ __51-[SVXSession _presentError:taskTracker:completion:]_block_invoke.345
+ __51-[SVXSession _presentError:taskTracker:completion:]_block_invoke.349
+ __52-[SVXSessionManager activateWithContext:completion:]_block_invoke.64
+ __54-[SVXSession acquireAudioSessionForReason:completion:]_block_invoke.117
+ __54-[SVXSession acquireAudioSessionForReason:completion:]_block_invoke.119
+ __56-[SVXSpeechSynthesizer _cancelPendingContextsAtIndexes:]_block_invoke.101
+ __56-[SVXSpeechSynthesizer _cancelPendingContextsAtIndexes:]_block_invoke.99
+ __57-[SVXSessionManager _fetchStereoPairStateWithCompletion:]_block_invoke.98
+ __57-[SVXSessionManager _fetchStereoPartnerLastMyriadWinDate]_block_invoke.96
+ __59-[SVXSession _getAlarmAndTimerFiringContextWithCompletion:]_block_invoke.214
+ __60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.80
+ __60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.84
+ __60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.88
+ __60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.89
+ __60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.93
+ __62-[SVXSession _forceAudioSessionInactiveWithReason:completion:]_block_invoke.204
+ __68-[SVXSession _forceAudioSessionActiveWithOptions:reason:completion:]_block_invoke.200
+ __69-[SVXTapToRadarManager createProblem:extraContent:completionHandler:]_block_invoke.122
+ __73-[SVXSpeechSynthesizer _startPresynthesizedAudioRequestForContext:error:]_block_invoke.76
+ __74-[SVXSessionManager startWithModuleInstanceProvider:platformDependencies:]_block_invoke.38
+ __74-[SVXSessionManager startWithModuleInstanceProvider:platformDependencies:]_block_invoke.42
+ __74-[SVXSessionManager startWithModuleInstanceProvider:platformDependencies:]_block_invoke_2.43
+ __76-[SVXSession _startActiveAudioSessionRequestForType:taskTracker:completion:]_block_invoke.194
+ __Block_byref_object_copy_.12998
+ __Block_byref_object_copy_.13803
+ __Block_byref_object_copy_.9031
+ __Block_byref_object_dispose_.12999
+ __Block_byref_object_dispose_.13804
+ __Block_byref_object_dispose_.9032
+ __OBJC_$_INSTANCE_METHODS_SVXAFSiriTetherFactory
+ __OBJC_CLASS_RO_$_SVXAFSiriTetherFactory
+ __OBJC_METACLASS_RO_$_SVXAFSiriTetherFactory
+ __TapToRadarKitLibraryCore_block_invoke.7986
+ ___46-[SVXSessionManager _invalidateCurrentSession]_block_invoke
+ ___49-[SVXSessionManager initWithModule:enableMyriad:]_block_invoke
+ ___56-[SVXClientActivationService _buttonHoldToTalkThreshold]_block_invoke
+ __block_literal_global.10949
+ __block_literal_global.11573
+ __block_literal_global.11642
+ __block_literal_global.11739
+ __block_literal_global.12328
+ __block_literal_global.12544
+ __block_literal_global.12717
+ __block_literal_global.12749
+ __block_literal_global.13273
+ __block_literal_global.1941
+ __block_literal_global.209
+ __block_literal_global.212
+ __block_literal_global.2253
+ __block_literal_global.2471
+ __block_literal_global.26.5003
+ __block_literal_global.264
+ __block_literal_global.2831
+ __block_literal_global.3002
+ __block_literal_global.3093
+ __block_literal_global.31.6200
+ __block_literal_global.34
+ __block_literal_global.382
+ __block_literal_global.3953
+ __block_literal_global.4415
+ __block_literal_global.4948
+ __block_literal_global.5019
+ __block_literal_global.5094
+ __block_literal_global.5378
+ __block_literal_global.5491
+ __block_literal_global.5746
+ __block_literal_global.59
+ __block_literal_global.6208
+ __block_literal_global.6412
+ __block_literal_global.6644
+ __block_literal_global.6948
+ __block_literal_global.8183
+ __block_literal_global.826
+ __block_literal_global.830
+ __block_literal_global.8469
+ __block_literal_global.8559
+ __block_literal_global.9217
+ __block_literal_global.9304
+ __block_literal_global.9519
+ __block_literal_global.9683
+ __block_literal_global.9875
+ _buttonHoldToTalkThreshold.onceToken
+ _buttonHoldToTalkThreshold.threshold
+ _objc_msgSend$_beginMonitoringAvailability
+ _objc_msgSend$_buttonHoldToPreheatThreshold
+ _objc_msgSend$_buttonHoldToTalkThreshold
+ _objc_msgSend$_deviceSetupIsActive:endDate:recencyDuration:
+ _objc_msgSend$_deviceSupportsSiriMUX
+ _objc_msgSend$_stopMonitoringAvailability
+ _objc_msgSend$_timeIntervalBetweenButtonUpTime:lastActivationButtonTime:
+ _objc_msgSend$_validateButtonEventForActivation:
+ _objc_msgSend$_validateSystemEventForActivation:
+ _objc_msgSend$createWithInstanceContext:
+ _objc_msgSend$initWithModule:enableMyriad:
+ _objc_msgSend$initWithName:options:queue:delegate:
+ _objc_msgSend$initWithUTF8String:
+ _objc_msgSend$isSpeechRecordingAllowedWithActivationContext:
+ _objc_msgSend$isVoiceTriggerWithActivationContext:
+ audit_stringTapToRadarKit.8001
- GCC_except_table1076
- GCC_except_table1130
- GCC_except_table1137
- GCC_except_table1402
- GCC_except_table1552
- GCC_except_table1560
- GCC_except_table1561
- GCC_except_table1795
- GCC_except_table2127
- GCC_except_table2141
- GCC_except_table2158
- GCC_except_table2159
- GCC_except_table2278
- GCC_except_table2283
- GCC_except_table2594
- GCC_except_table2750
- GCC_except_table2825
- GCC_except_table2862
- GCC_except_table2865
- GCC_except_table2871
- GCC_except_table2874
- GCC_except_table485
- GCC_except_table502
- GCC_except_table514
- GCC_except_table519
- GCC_except_table718
- OBJC_IVAR_$_SVXTapToRadarManager._ttrQueue
- TapToRadarKitLibraryCore.frameworkLibrary.7972
- _SVXClientActivationServiceGetButtonHoldToTalkThreshold.onceToken
- _SVXClientActivationServiceGetButtonHoldToTalkThreshold.threshold
- _SVXSessionIsSpeechRecordingAllowed
- __156-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke.179
- __156-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke.187
- __156-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke_2.180
- __156-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke_3.181
- __156-[SVXSession _startSpeechSynthesisRequest:languageCode:voiceName:gender:introductionSoundID:conclusionSoundID:taskTracker:postActivationHandler:completion:]_block_invoke_4.182
- __181-[SVXSession activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:completion:]_block_invoke.79
- __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.149
- __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.153
- __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.158
- __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.162
- __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke.172
- __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke_2.163
- __194-[SVXSession _activateWithContext:options:deviceSetupContext:deviceProblemsState:localDeviceContext:speechSynthesisRecord:speechSynthesisState:speechRecordingAlertPolicy:taskTracker:completion:]_block_invoke_2.173
- __37-[SVXSession _resignActiveForReason:]_block_invoke.229
- __37-[SVXSession _resignActiveForReason:]_block_invoke.232
- __37-[SVXSession _resignActiveForReason:]_block_invoke.237
- __37-[SVXSession _resignActiveForReason:]_block_invoke.243
- __38-[SVXSpeechSynthesizer _startContext:]_block_invoke.61
- __38-[SVXSpeechSynthesizer _startContext:]_block_invoke.66
- __40-[SVXSpeechSynthesizer _enqueueContext:]_block_invoke.56
- __43-[SVXSession _checkIsActiveWithCompletion:]_block_invoke.221
- __43-[SVXSession _checkIsActiveWithCompletion:]_block_invoke.223
- __43-[SVXSessionManager _processNextOperations]_block_invoke.65
- __43-[SVXSessionManager _processNextOperations]_block_invoke.69
- __43-[SVXSessionManager _processNextOperations]_block_invoke.75
- __43-[SVXSessionManager _processNextOperations]_block_invoke.76
- __45-[SVXSessionManager queue:didEnqueueObjects:]_block_invoke.63
- __47-[SVXSession deactivateWithContext:completion:]_block_invoke.85
- __47-[SVXSpeechSynthesizer _processPendingContexts]_block_invoke.58
- __51-[SVXSession _presentError:taskTracker:completion:]_block_invoke.341
- __51-[SVXSession _presentError:taskTracker:completion:]_block_invoke.344
- __51-[SVXSession _presentError:taskTracker:completion:]_block_invoke.348
- __52-[SVXSessionManager activateWithContext:completion:]_block_invoke.58
- __54-[SVXSession acquireAudioSessionForReason:completion:]_block_invoke.115
- __54-[SVXSession acquireAudioSessionForReason:completion:]_block_invoke.118
- __56-[SVXSpeechSynthesizer _cancelPendingContextsAtIndexes:]_block_invoke.102
- __56-[SVXSpeechSynthesizer _cancelPendingContextsAtIndexes:]_block_invoke.104
- __56-[SVXSpeechSynthesizer _cancelPendingContextsAtIndexes:]_block_invoke.105
- __57-[SVXSessionManager _fetchStereoPairStateWithCompletion:]_block_invoke.95
- __57-[SVXSessionManager _fetchStereoPartnerLastMyriadWinDate]_block_invoke.93
- __59-[SVXSession _getAlarmAndTimerFiringContextWithCompletion:]_block_invoke.213
- __60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.83
- __60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.87
- __60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.91
- __60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.95
- __60-[SVXSpeechSynthesizer _startSpeechRequestForContext:error:]_block_invoke.96
- __62-[SVXSession _forceAudioSessionInactiveWithReason:completion:]_block_invoke.202
- __62-[SVXSoundUtils createAudioPlaybackRequestFromID:preferences:]_block_invoke.40
- __68-[SVXSession _forceAudioSessionActiveWithOptions:reason:completion:]_block_invoke.199
- __69-[SVXTapToRadarManager createProblem:extraContent:completionHandler:]_block_invoke.119
- __73-[SVXSpeechSynthesizer _startPresynthesizedAudioRequestForContext:error:]_block_invoke.78
- __74-[SVXSessionManager startWithModuleInstanceProvider:platformDependencies:]_block_invoke.35
- __74-[SVXSessionManager startWithModuleInstanceProvider:platformDependencies:]_block_invoke.39
- __74-[SVXSessionManager startWithModuleInstanceProvider:platformDependencies:]_block_invoke_2.40
- __76-[SVXSession _startActiveAudioSessionRequestForType:taskTracker:completion:]_block_invoke.193
- __Block_byref_object_copy_.12972
- __Block_byref_object_copy_.13777
- __Block_byref_object_copy_.6207
- __Block_byref_object_copy_.9021
- __Block_byref_object_dispose_.12973
- __Block_byref_object_dispose_.13778
- __Block_byref_object_dispose_.6208
- __Block_byref_object_dispose_.9022
- __SVXClientActivationServiceValidateSystemEventForActivation
- __TapToRadarKitLibraryCore_block_invoke.7973
- ___36-[SVXSessionManager initWithModule:]_block_invoke
- ___57-[AFClockAlarmSnapshot(SiriVOX) svx_notifiedFiringAlarms]_block_invoke
- ___57-[AFClockTimerSnapshot(SiriVOX) svx_notifiedFiringTimers]_block_invoke
- ___65-[SVXClientActivationService _processLastButtonActivationContext]_block_invoke
- ____SVXClientActivationServiceGetButtonHoldToTalkThreshold_block_invoke
- ___block_descriptor_48_e8_32r_e42_v32?0"SVXSpeechSynthesisContext"8Q16^B24l
- ___block_descriptor_48_e8_32s40s_e22_v32?0"NSURL"8Q16^B24l
- ___block_descriptor_48_e8_32s40s_e23_v32?0"NSUUID"8Q16^B24l
- ___block_descriptor_56_e8_32r40r_e31_v32?0"SVXButtonEvent"8Q16^B24l
- ___copy_helper_block_e8_32r40r
- ___destroy_helper_block_e8_32r40r
- __block_literal_global.10947
- __block_literal_global.11566
- __block_literal_global.11635
- __block_literal_global.11716
- __block_literal_global.12302
- __block_literal_global.12517
- __block_literal_global.12690
- __block_literal_global.12722
- __block_literal_global.13249
- __block_literal_global.153
- __block_literal_global.1944
- __block_literal_global.208
- __block_literal_global.211
- __block_literal_global.2250
- __block_literal_global.2468
- __block_literal_global.26.4999
- __block_literal_global.263
- __block_literal_global.2828
- __block_literal_global.2999
- __block_literal_global.3090
- __block_literal_global.31.6178
- __block_literal_global.381
- __block_literal_global.3950
- __block_literal_global.4412
- __block_literal_global.4944
- __block_literal_global.5015
- __block_literal_global.5090
- __block_literal_global.5374
- __block_literal_global.5487
- __block_literal_global.5742
- __block_literal_global.60
- __block_literal_global.6186
- __block_literal_global.6392
- __block_literal_global.6624
- __block_literal_global.6927
- __block_literal_global.816
- __block_literal_global.8171
- __block_literal_global.820
- __block_literal_global.8457
- __block_literal_global.8547
- __block_literal_global.9214
- __block_literal_global.9301
- __block_literal_global.9516
- __block_literal_global.9680
- __block_literal_global.9872
- audit_stringTapToRadarKit.7988
CStrings:
+ "-[SVXClientActivationService _validateButtonEventForActivation:]"
+ "-[SVXClientActivationService _validateSystemEventForActivation:]"
+ "@\"SVXAFSiriTetherFactory\""
+ "B40@0:8@16@24d32"
+ "SVXAFSiriTetherFactory"
+ "_beginMonitoringAvailability"
+ "_buttonHoldToPreheatThreshold"
+ "_buttonHoldToTalkThreshold"
+ "_deviceSetupIsActive:endDate:recencyDuration:"
+ "_deviceSupportsSiriMUX"
+ "_stopMonitoringAvailability"
+ "_tetherFactory"
+ "_timeIntervalBetweenButtonUpTime:lastActivationButtonTime:"
+ "_validateButtonEventForActivation:"
+ "_validateSystemEventForActivation:"
+ "assistantConnection:replayAll:with:"
+ "assistantConnection:replayAt:with:"
+ "assistantConnection:setReplayEnabled:"
+ "assistantConnection:setReplayOverridePath:"
+ "com.apple.SiriVOX.device-problems"
+ "com.apple.sharing.problems"
+ "d32@0:8Q16Q24"
+ "initWithModule:enableMyriad:"
+ "initWithName:options:queue:delegate:"
+ "initWithUTF8String:"
+ "isSpeechRecordingAllowedWithActivationContext:"
+ "isVoiceTriggerWithActivationContext:"
+ "v32@0:8@\"AFConnection\"16@\"NSURL\"24"
+ "v40@0:8@\"AFConnection\"16Q24@\"NSURL\"32"
+ "v40@0:8@16Q24@32"
- "-[SVXClientActivationService _processLastButtonActivationContext]_block_invoke"
- "-[SVXSpeechSynthesizer _enqueueContext:]_block_invoke"
- "DISMISSALREASON_UNKNOWN_DISMISSAL_REASON"
- "_SVXClientActivationServiceValidateButtonEventForActivation"
- "_SVXClientActivationServiceValidateSystemEventForActivation"
- "_ttrQueue"
- "v32@?0@\"NSURL\"8Q16^B24"
- "v32@?0@\"NSUUID\"8Q16^B24"

```
