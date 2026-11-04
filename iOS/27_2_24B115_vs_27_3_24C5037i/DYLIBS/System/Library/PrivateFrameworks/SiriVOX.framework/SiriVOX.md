## SiriVOX

> `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX`

```diff

-3605.19.1.0.0
-  __TEXT.__text: 0x847f8
-  __TEXT.__objc_methlist: 0x8cb0
-  __TEXT.__const: 0x124
+3610.11.1.0.0
+  __TEXT.__text: 0x86d9c
+  __TEXT.__objc_methlist: 0x8e98
+  __TEXT.__const: 0x130
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x11b5e
+  __TEXT.__cstring: 0x11ecd
   __TEXT.__swift5_capture: 0x78
   __TEXT.__swift5_reflstr: 0x16
-  __TEXT.__gcc_except_tab: 0x5e8
-  __TEXT.__oslogstring: 0x8ec0
+  __TEXT.__gcc_except_tab: 0x680
+  __TEXT.__oslogstring: 0x94a4
   __TEXT.__dlopen_cstrs: 0xda
-  __TEXT.__unwind_info: 0x2c58
+  __TEXT.__unwind_info: 0x2d60
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2ca8
-  __DATA_CONST.__objc_classlist: 0x678
+  __DATA_CONST.__const: 0x2da0
+  __DATA_CONST.__objc_classlist: 0x680
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x2d8
+  __DATA_CONST.__objc_protolist: 0x2e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e58
+  __DATA_CONST.__objc_selrefs: 0x3f58
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x4a8
-  __DATA_CONST.__objc_arraydata: 0x980
-  __DATA_CONST.__got: 0x798
-  __AUTH_CONST.__const: 0xc08
-  __AUTH_CONST.__cfstring: 0x6020
-  __AUTH_CONST.__objc_const: 0x13a28
+  __DATA_CONST.__objc_superrefs: 0x4b0
+  __DATA_CONST.__objc_arraydata: 0x990
+  __DATA_CONST.__got: 0x7b8
+  __AUTH_CONST.__const: 0xca8
+  __AUTH_CONST.__cfstring: 0x60c0
+  __AUTH_CONST.__objc_const: 0x13d60
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH_CONST.__objc_intobj: 0xe58
+  __AUTH_CONST.__objc_intobj: 0xe70
   __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH_CONST.__auth_got: 0x6e8
-  __AUTH.__objc_data: 0x4150
+  __AUTH_CONST.__auth_got: 0x708
+  __AUTH.__objc_data: 0x41a0
   __AUTH.__data: 0x38
-  __DATA.__objc_ivar: 0xce8
-  __DATA.__data: 0x2260
+  __DATA.__objc_ivar: 0xd34
+  __DATA.__data: 0x22c0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3187
-  Symbols:   6765
-  CStrings:  2286
+  Functions: 3250
+  Symbols:   6876
+  CStrings:  2332
 
Symbols:
+ -[SVXHomePodUIBridgeClientDelegate _handleDirectedSpeechDetected]
+ -[SVXHomePodUIBridgeClientDelegate _handleDirectedSpeechSelected]
+ -[SVXHomePodUIBridgeClientDelegate _handleSpeechMitigated]
+ -[SVXHomePodUIBridgeClientDelegate _openFollowUpWindow]
+ -[SVXHomePodUIBridgeClientDelegate _resetLASWindowState]
+ -[SVXHomePodUIBridgeClientDelegate _sendPrompt]
+ -[SVXHomePodUIBridgeClientDelegate _tearDownLASWindow]
+ -[SVXHomePodUIBridgeClientDelegate _unduckTTSIfNeeded]
+ -[SVXHomePodUIBridgeClientDelegate attendingStatusChanged:]
+ -[SVXHomePodUIBridgeClientDelegate didDetectSameUserSpeech]
+ -[SVXHomePodUIBridgeClientDelegate didDetectUserSpeech]
+ -[SVXHomePodUIBridgeClientDelegate didDuckTTS]
+ -[SVXHomePodUIBridgeClientDelegate duckTTSToVolume:rampTime:completion:]
+ -[SVXHomePodUIBridgeClientDelegate orchestrationDidPresentResponseFullyInApp]
+ -[SVXHomePodUIBridgeClientDelegate pauseTTS]
+ -[SVXHomePodUIBridgeClientDelegate playbackFinished]
+ -[SVXHomePodUIBridgeClientDelegate promptPending]
+ -[SVXHomePodUIBridgeClientDelegate resumeTTS]
+ -[SVXHomePodUIBridgeClientDelegate sessionDismissed]
+ -[SVXHomePodUIBridgeClientDelegate sessionStateHandler:didTransitionFromState:toState:forEvent:machAbsoluteTime:]
+ -[SVXHomePodUIBridgeClientDelegate sessionStateHandler]
+ -[SVXHomePodUIBridgeClientDelegate setDidDuckTTS:]
+ -[SVXHomePodUIBridgeClientDelegate setPlaybackFinished:]
+ -[SVXHomePodUIBridgeClientDelegate setPromptPending:]
+ -[SVXHomePodUIBridgeClientDelegate setSessionDismissed:]
+ -[SVXHomePodUIBridgeClientDelegate setSessionStateHandler:]
+ -[SVXHomePodUIBridgeClientDelegate setSpeculativeLASActivationContext:]
+ -[SVXHomePodUIBridgeClientDelegate setSruifClient:]
+ -[SVXHomePodUIBridgeClientDelegate showAssetsDownloadNotificationPrompt]
+ -[SVXHomePodUIBridgeClientDelegate siriDismissed]
+ -[SVXHomePodUIBridgeClientDelegate speculativeLASActivationContext]
+ -[SVXHomePodUIBridgeClientDelegate sruifClient]
+ -[SVXHomePodUIBridgeClientDelegate willStartPlayback]
+ -[SVXMissingAssetActivationDecision declineError]
+ -[SVXMissingAssetActivationDecision initWithDeclineError:promptLocalizationKey:]
+ -[SVXMissingAssetActivationGuard setSiriAvailability:]
+ -[SVXMissingAssetActivationGuard siriAvailability]
+ -[SVXSession _isContinuousConversationActive]
+ -[SVXSession _showListeningIfFollowUpWindowOpen]
+ -[SVXSession endContinuousConversation]
+ -[SVXSession speechSynthesizerDidFinishPlaybackWithTaskTracker:queueIsEmpty:]
+ -[SVXSession uiBridgeClientDidOpenFollowUpWindow]
+ -[SVXSession uiBridgeClientDidRestoreFollowUpWindow]
+ -[SVXSessionManager _currentOrchestrationMode]
+ -[SVXSessionManager _handleSiriCapabilitiesChanged]
+ -[SVXSessionManager _invalidateStaleSessionForOrchestrationModeChange]
+ -[SVXSessionManager _isDeviceSelectionShadowMode]
+ -[SVXSessionManager _refreshOrchestrationMode]
+ -[SVXSessionManager _siriCapabilitiesDidChange]
+ -[SVXSessionManager dealloc]
+ -[SVXShadowRecencyDonor .cxx_destruct]
+ -[SVXShadowRecencyDonor activationBegan]
+ -[SVXShadowRecencyDonor initWithNow:continuousUptime:donate:]
+ -[SVXShadowRecencyDonor init]
+ -[SVXShadowRecencyDonor myriadWon]
+ -[SVXSpeechSynthesisUtils isPhaticPrompt:]
+ -[SVXSpeechSynthesizer _handleContextFailedBeforeStreamStart:error:]
+ -[SVXSpeechSynthesizer _handleSpeakingContextFinishedWithoutAudio:]
+ -[SVXSpeechSynthesizer _holdAudioSessionAssertion:forStreamId:]
+ -[SVXSpeechSynthesizer _releaseAllStreamAudioSessionAssertions]
+ -[SVXSpeechSynthesizer _releaseAudioSessionAssertionForStreamId:]
+ GCC_except_table1153
+ GCC_except_table1168
+ GCC_except_table1224
+ GCC_except_table1495
+ GCC_except_table1637
+ GCC_except_table1638
+ GCC_except_table1675
+ GCC_except_table1681
+ GCC_except_table1682
+ GCC_except_table1714
+ GCC_except_table1820
+ GCC_except_table1822
+ GCC_except_table1823
+ GCC_except_table1934
+ GCC_except_table2105
+ GCC_except_table2116
+ GCC_except_table2118
+ GCC_except_table2123
+ GCC_except_table2136
+ GCC_except_table2138
+ GCC_except_table2296
+ GCC_except_table2420
+ GCC_except_table2422
+ GCC_except_table2425
+ GCC_except_table2427
+ GCC_except_table2429
+ GCC_except_table2431
+ GCC_except_table2447
+ GCC_except_table2448
+ GCC_except_table2576
+ GCC_except_table2580
+ GCC_except_table2582
+ GCC_except_table2585
+ GCC_except_table2891
+ GCC_except_table3046
+ GCC_except_table3121
+ GCC_except_table525
+ GCC_except_table537
+ GCC_except_table547
+ GCC_except_table778
+ _AFDeviceSelectionParticipating
+ _NSDebugDescriptionErrorKey
+ _NSStringFromAFSiriOrchestrationMode
+ _NSStringFromAFSiriUnavailabilityReasons
+ _OBJC_CLASS_$_AFDialogPhase
+ _OBJC_CLASS_$_DeviceSelectionSignalDonation
+ _OBJC_CLASS_$_SRUIFSiriSessionStateHandler
+ _OBJC_CLASS_$_SRUIFUIBridgeClient
+ _OBJC_CLASS_$_SVXShadowRecencyDonor
+ _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._didDuckTTS
+ _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._playbackFinished
+ _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._promptPending
+ _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._sessionDismissed
+ _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._sessionStateHandler
+ _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._speculativeLASActivationContext
+ _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._sruifClient
+ _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._sruifDelegateQueue
+ _OBJC_IVAR_$_SVXMissingAssetActivationDecision._declineError
+ _OBJC_IVAR_$_SVXSession._hasEndedContinuousConversation
+ _OBJC_IVAR_$_SVXSession._isAwaitingFollowUpActivation
+ _OBJC_IVAR_$_SVXSession._isLASFollowUpWindowOpen
+ _OBJC_IVAR_$_SVXSessionManager._contextOrchestrationMode
+ _OBJC_IVAR_$_SVXSessionManager._currentSessionNeedsRebuild
+ _OBJC_IVAR_$_SVXSessionManager._currentSessionOrchestrationMode
+ _OBJC_IVAR_$_SVXSessionManager._hasLoggedDeferredTeardown
+ _OBJC_IVAR_$_SVXSessionManager._orchestrationMode
+ _OBJC_IVAR_$_SVXSessionManager._shadowRecencyDonor
+ _OBJC_IVAR_$_SVXShadowRecencyDonor._continuousUptime
+ _OBJC_IVAR_$_SVXShadowRecencyDonor._donate
+ _OBJC_IVAR_$_SVXShadowRecencyDonor._now
+ _OBJC_IVAR_$_SVXShadowRecencyDonor._pendingActivationDate
+ _OBJC_IVAR_$_SVXShadowRecencyDonor._pendingActivationUptime
+ _OBJC_IVAR_$_SVXSpeechSynthesizer._streamAudioSessionAssertions
+ _OBJC_METACLASS_$_SVXShadowRecencyDonor
+ _SVXDeclineErrorForSiriStatus
+ __OBJC_$_INSTANCE_METHODS_SVXShadowRecencyDonor
+ __OBJC_$_INSTANCE_VARIABLES_SVXShadowRecencyDonor
+ __OBJC_$_PROP_LIST_SVXMissingAssetActivationGuard
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SRUIFUIBridgeClientDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SRUIFSiriSessionStateHandlerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SRUIFUIBridgeClientDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SRUIFSiriSessionStateHandlerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SRUIFUIBridgeClientDelegate
+ __OBJC_$_PROTOCOL_REFS_SRUIFSiriSessionStateHandlerDelegate
+ __OBJC_$_PROTOCOL_REFS_SRUIFUIBridgeClientDelegate
+ __OBJC_CLASS_RO_$_SVXShadowRecencyDonor
+ __OBJC_LABEL_PROTOCOL_$_SRUIFSiriSessionStateHandlerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SRUIFUIBridgeClientDelegate
+ __OBJC_METACLASS_RO_$_SVXShadowRecencyDonor
+ __OBJC_PROTOCOL_$_SRUIFSiriSessionStateHandlerDelegate
+ __OBJC_PROTOCOL_$_SRUIFUIBridgeClientDelegate
+ ___29-[SVXShadowRecencyDonor init]_block_invoke
+ ___29-[SVXShadowRecencyDonor init]_block_invoke_2
+ ___29-[SVXShadowRecencyDonor init]_block_invoke_3
+ ___29-[SVXShadowRecencyDonor init]_block_invoke_4
+ ___39-[SVXSession endContinuousConversation]_block_invoke
+ ___39-[SVXSessionManager initiateEmergency:]_block_invoke
+ ___47-[SVXSessionManager _siriCapabilitiesDidChange]_block_invoke
+ ___49-[SVXHomePodUIBridgeClientDelegate siriDismissed]_block_invoke
+ ___49-[SVXSession uiBridgeClientDidOpenFollowUpWindow]_block_invoke
+ ___52-[SVXSession uiBridgeClientDidRestoreFollowUpWindow]_block_invoke
+ ___53-[SVXHomePodUIBridgeClientDelegate willStartPlayback]_block_invoke
+ ___54-[SVXHomePodUIBridgeClientDelegate _unduckTTSIfNeeded]_block_invoke
+ ___58-[SVXHomePodUIBridgeClientDelegate _handleSpeechMitigated]_block_invoke
+ ___59-[SVXHomePodUIBridgeClientDelegate attendingStatusChanged:]_block_invoke
+ ___65-[SVXHomePodUIBridgeClientDelegate _handleDirectedSpeechDetected]_block_invoke
+ ___65-[SVXHomePodUIBridgeClientDelegate _handleDirectedSpeechSelected]_block_invoke
+ ___67-[SVXHomePodUIBridgeClientDelegate didPromptListeningAfterSpeaking]_block_invoke
+ ___70-[SVXSessionManager _invalidateStaleSessionForOrchestrationModeChange]_block_invoke
+ ___77-[SVXSession speechSynthesizerDidFinishPlaybackWithTaskTracker:queueIsEmpty:]_block_invoke
+ ___88-[SVXSessionManager _handleSession:didResignActiveWithDeactivationContext:activityUUID:]_block_invoke_2
+ ___block_descriptor_32_e13_"NSDate"8?0l
+ ___block_descriptor_32_e16_v16?0"NSDate"8l
+ ___block_descriptor_32_e5_d8?0l
+ ___block_descriptor_41_e8_32s_e43_v24?0"DeviceSelectionDevice"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e8_v16?0q8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0ls32l8r56l8s48l8s40l8
+ ___block_descriptor_72_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ __siriCapabilitiesDidChange
+ _objc_setProperty_atomic
- -[SVXHomePodUIBridgeClientDelegate currentUserTurnID]
- -[SVXHomePodUIBridgeClientDelegate didPauseTTSForCurrentUserTurn]
- -[SVXHomePodUIBridgeClientDelegate isAttending]
- -[SVXHomePodUIBridgeClientDelegate setCurrentUserTurnID:]
- -[SVXHomePodUIBridgeClientDelegate setDidPauseTTSForCurrentUserTurn:]
- -[SVXHomePodUIBridgeClientDelegate setIsAttending:]
- -[SVXHomePodUIBridgeClientDelegate setUiBridgeClient:]
- -[SVXHomePodUIBridgeClientDelegate uiBridgeClient]
- -[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDetectedSpeechStart:]
- -[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidDetectUserSpeechWithContext:]
- -[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidFinalizeUserTurnWithContext:]
- -[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidStartAttending]
- -[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidStopAttendingUnexpectedlyWithReason:]
- -[SVXHomePodUIBridgeClientDelegate uiBridgeServiceReceivedSpeechMitigationResult:]
- -[SVXHomePodUIBridgeClientDelegate uiBridgeServiceWillStartAttending]
- -[SVXMissingAssetActivationDecision initWithShouldDeclineActivation:promptLocalizationKey:]
- -[SVXMissingAssetActivationDecision shouldDeclineActivation]
- -[SVXSession speechSynthesizerDidFinishPlayback]
- GCC_except_table1147
- GCC_except_table1162
- GCC_except_table1218
- GCC_except_table1489
- GCC_except_table1631
- GCC_except_table1632
- GCC_except_table1662
- GCC_except_table1668
- GCC_except_table1669
- GCC_except_table1700
- GCC_except_table1804
- GCC_except_table1806
- GCC_except_table1807
- GCC_except_table1914
- GCC_except_table2079
- GCC_except_table2104
- GCC_except_table2241
- GCC_except_table2364
- GCC_except_table2366
- GCC_except_table2368
- GCC_except_table2384
- GCC_except_table2385
- GCC_except_table2513
- GCC_except_table2517
- GCC_except_table2519
- GCC_except_table2522
- GCC_except_table2828
- GCC_except_table2983
- GCC_except_table3058
- GCC_except_table524
- GCC_except_table536
- GCC_except_table546
- GCC_except_table772
- _OBJC_CLASS_$_SUIBUIBridgeClient
- _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._currentUserTurnID
- _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._didPauseTTSForCurrentUserTurn
- _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._isAttending
- _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._uiBridgeClient
- _OBJC_IVAR_$_SVXMissingAssetActivationDecision._shouldDeclineActivation
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SUIBUIBridgeServiceDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SUIBUIBridgeServiceDelegate
- __OBJC_$_PROTOCOL_REFS_SUIBUIBridgeServiceDelegate
- __OBJC_LABEL_PROTOCOL_$_SUIBUIBridgeServiceDelegate
- __OBJC_PROTOCOL_$_SUIBUIBridgeServiceDelegate
- ___48-[SVXSession speechSynthesizerDidFinishPlayback]_block_invoke
- ___69-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceWillStartAttending]_block_invoke
- ___71-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDetectedSpeechStart:]_block_invoke
- ___82-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidDetectUserSpeechWithContext:]_block_invoke
- ___82-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidFinalizeUserTurnWithContext:]_block_invoke
- ___82-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceReceivedSpeechMitigationResult:]_block_invoke
- ___90-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidStopAttendingUnexpectedlyWithReason:]_block_invoke
- ___block_descriptor_40_e8_32s_e43_v24?0"DeviceSelectionDevice"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
CStrings:
+ "#Choreography Attending stopped, discarding pending LAS activation"
+ "#Choreography Created SRUIFUIBridgeClient"
+ "#Choreography Directed speech detected during LAS attending, activating follow-up"
+ "#Choreography Ignoring follow-up barrier after dismissal"
+ "#Choreography More audio starting — pausing follow-up window"
+ "#Choreography Playback already finished — starting follow-up window"
+ "#Choreography Sending SiriPrompted: rootRequestId=%{public}@"
+ "#Choreography Speech mitigated, restoring follow-up window"
+ "#Choreography attendingStatusChanged: %d"
+ "#Choreography didDetectUserSpeech (not the invoking user), ignoring for LAS"
+ "#Choreography duckTTSToVolume: %f"
+ "#Choreography failed to unduck TTS: %{public}@"
+ "#Choreography orchestrationDidPresentResponseFullyInApp: no HomePod UI, ignoring"
+ "#Choreography showAssetsDownloadNotificationPrompt: no HomePod UI, ignoring"
+ "#Choreography siriDismissed: rootRequestId=%{public}@"
+ "#Choreography unducking TTS"
+ "#Choreography verdict: directed speech selected"
+ "#Choreography verdict: speech mitigated"
+ "%@ (reasons: %@)"
+ "%s #deviceSelection #shadow Myriad won; donating recency."
+ "%s #deviceSelection #shadow Recency donation failed: %{public}@"
+ "%s #deviceSelection #shadow recorded %{public}s; Myriad decides."
+ "%s #missingAssets - Declining activation for source %@ (promptKey = %@, error = %{public}@)"
+ "%s #tts Empty first piece for streamId %@; starting the stream without text."
+ "%s Blocking listeningAfterSpeaking activation because the last Siri request resulted in an error dialog (isErrorDialogPhase = %d)"
+ "%s Ending continuous conversation after the current request"
+ "%s Ending continuous conversation — deactivating session"
+ "%s Ignoring playback end from an earlier request. (_currentRequestUUID = %@, playbackRequestUUID = %@)"
+ "%s LAS follow-up window open and request ended, showing listening"
+ "%s LAS follow-up window open, waiting for the request to end before showing listening"
+ "%s LAS follow-up window restored after mitigation"
+ "%s Not acquiring audio ducking coordination assertion: another device ducks this speaker."
+ "%s Not arming listen-after-speaking for the two-shot phatic prompt"
+ "%s Orchestration mode changed %@ -> %@ (rebuild = %d), invalidating session"
+ "%s Orchestration mode changed %@ -> %@ since the last context clear, clearing context"
+ "%s Orchestration mode changed mid-request, deferring session invalidation"
+ "%s Playback ended but more synthesis is queued; the response is not over."
+ "%s Releasing the audio session held for a stream. (streamId = %@, assertion = %@)"
+ "%s Speaking context finished without audio; reporting the audio end. (context = %@)"
+ "%s Stream never started; reporting its end here. (streamId = %@, error = %@)"
+ "%s taskTracker = %@, queueIsEmpty = %d"
+ "-[SVXSession _showListeningIfFollowUpWindowOpen]"
+ "-[SVXSession endContinuousConversation]_block_invoke"
+ "-[SVXSession speechSynthesizerDidFinishPlaybackWithTaskTracker:queueIsEmpty:]"
+ "-[SVXSession speechSynthesizerDidFinishPlaybackWithTaskTracker:queueIsEmpty:]_block_invoke"
+ "-[SVXSession uiBridgeClientDidRestoreFollowUpWindow]_block_invoke"
+ "-[SVXSessionManager _invalidateStaleSessionForOrchestrationModeChange]_block_invoke"
+ "-[SVXShadowRecencyDonor init]_block_invoke_4"
+ "-[SVXShadowRecencyDonor myriadWon]"
+ "-[SVXSpeechSynthesizer _handleContextFailedBeforeStreamStart:error:]"
+ "-[SVXSpeechSynthesizer _handleSpeakingContextFinishedWithoutAudio:]"
+ "-[SVXSpeechSynthesizer _releaseAudioSessionAssertionForStreamId:]"
+ "2"
+ "@\"NSDate\"8@?0"
+ "Siri is on but unavailable"
+ "Siri is restricted by a policy"
+ "Siri is turned off in Settings"
+ "assistantDisabled"
+ "com.apple.siri.SVXHomePodUIBridgeClientDelegate.sruif"
+ "d8@?0"
+ "lost"
+ "v16@?0@\"NSDate\"8"
+ "won"
- "\""
- "#Choreography - TTS was never paused for this turn, skipping resume"
- "#Choreography - TTS was never paused, skipping legacy resume"
- "#Choreography - UUID mismatch, skipping resume"
- "#Choreography Attending stopped unexpectedly — discarding pending LAS activation and deactivating session"
- "#Choreography Created SUIBUIBridgeClient"
- "#Choreography Directed speech detected during LAS attending — activating follow-up"
- "#Choreography SUIBUIBridgeServiceDelegate: uiBridgeServiceDidStartAttending"
- "#Choreography SUIBUIBridgeServiceDelegate: uiBridgeServiceDidStopAttendingUnexpectedly reason=%ld, hasPendingLAS=%d"
- "#Choreography SUIBUIBridgeServiceDelegate: uiBridgeServiceWillStartAttending"
- "#Choreography uiBridgeServiceDetectedSpeechStart: shouldDuckTTS=%d"
- "#Choreography uiBridgeServiceDidDetectUserSpeechWithContext: isInvocationUser=%d, hasPendingLAS=%d"
- "#Choreography uiBridgeServiceDidFinalizeUserTurnWithContext: decision=%ld"
- "#Choreography uiBridgeServiceReceivedSpeechMitigationResult: mitigationResult=%ld"
- "%s #missingAssets - Declining activation for source %@ (promptKey = %@)"
- "%s Blocking listeningAfterSpeaking activation because the last Siri request resulted in an error dialog"
- "-[SVXSession speechSynthesizerDidFinishPlayback]"
```
