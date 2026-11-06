## SiriVOX

> `/System/Library/PrivateFrameworks/SiriVOX.framework/Versions/A/SiriVOX`

```diff

-3600.52.7.0.0
-  __TEXT.__text: 0x8a8e8
-  __TEXT.__objc_methlist: 0x8a98
+3605.19.1.0.0
+  __TEXT.__text: 0x8cd20
+  __TEXT.__objc_methlist: 0x8bf8
   __TEXT.__const: 0x12c
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x113fe
+  __TEXT.__cstring: 0x1175f
   __TEXT.__swift5_capture: 0x78
   __TEXT.__swift5_reflstr: 0x16
-  __TEXT.__gcc_except_tab: 0x580
-  __TEXT.__oslogstring: 0x86e7
+  __TEXT.__gcc_except_tab: 0x5e8
+  __TEXT.__oslogstring: 0x8be9
   __TEXT.__dlopen_cstrs: 0xda
-  __TEXT.__unwind_info: 0x23e8
+  __TEXT.__unwind_info: 0x2478
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xfd8
-  __DATA_CONST.__objc_classlist: 0x668
+  __DATA_CONST.__const: 0xff8
+  __DATA_CONST.__objc_classlist: 0x678
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cd0
+  __DATA_CONST.__objc_selrefs: 0x3db8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x498
+  __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x980
-  __DATA_CONST.__got: 0x768
-  __AUTH_CONST.__const: 0x2c28
-  __AUTH_CONST.__cfstring: 0x5f20
-  __AUTH_CONST.__objc_const: 0x13560
+  __DATA_CONST.__got: 0x778
+  __AUTH_CONST.__const: 0x2cc8
+  __AUTH_CONST.__cfstring: 0x5f60
+  __AUTH_CONST.__objc_const: 0x13900
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH_CONST.__auth_got: 0x568
+  __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x40b0
+  __AUTH.__objc_data: 0x4150
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0xc8c
+  __DATA.__objc_ivar: 0xccc
   __DATA.__data: 0x2260
   __DATA.__bss: 0x248
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3171
-  Symbols:   8291
-  CStrings:  2224
+  Functions: 3215
+  Symbols:   8408
+  CStrings:  2259
 
Symbols:
+ -[SVXHomePodUIBridgeClientDelegate cancelPendingFollowUpActivation]
+ -[SVXHomePodUIBridgeClientDelegate didFinishPlayback]
+ -[SVXHomePodUIBridgeClientDelegate didPauseTTSForCurrentUserTurn]
+ -[SVXHomePodUIBridgeClientDelegate lasAttendingTimeoutSeconds]
+ -[SVXHomePodUIBridgeClientDelegate setDidPauseTTSForCurrentUserTurn:]
+ -[SVXHomePodUIBridgeClientDelegate setLasAttendingTimeoutSeconds:]
+ -[SVXMissingAssetActivationDecision .cxx_destruct]
+ -[SVXMissingAssetActivationDecision initWithShouldDeclineActivation:promptLocalizationKey:]
+ -[SVXMissingAssetActivationDecision promptLocalizationKey]
+ -[SVXMissingAssetActivationDecision shouldDeclineActivation]
+ -[SVXMissingAssetActivationGuard .cxx_destruct]
+ -[SVXMissingAssetActivationGuard _siriAvailabilityChanged]
+ -[SVXMissingAssetActivationGuard dealloc]
+ -[SVXMissingAssetActivationGuard decisionForActivationIdentifier:]
+ -[SVXMissingAssetActivationGuard initWithAvailabilityReporter:siriAvailabilityProvider:instrumentationUtils:]
+ -[SVXMissingAssetActivationGuard init]
+ -[SVXMyriadDeviceManager startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:electionIdentity:completion:]
+ -[SVXMyriadHostDevice startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:electionIdentity:completion:]
+ -[SVXSession _electionLedger]
+ -[SVXSession _isRootRequestHoldToTalk]
+ -[SVXSession _useElectionLedger:]
+ -[SVXSession _waitForLedgerDecisionForElection:usingHandler:]
+ -[SVXSession beginElectionWithIdentity:]
+ -[SVXSession currentActivationContext]
+ -[SVXSession releaseAudioSessionIfIdleForReason:]
+ -[SVXSession speechSynthesizerDidFailStreamWithError:taskTracker:]
+ -[SVXSession speechSynthesizerDidFinishPlayback]
+ -[SVXSessionUtils isUserInitiatedDeviceActivationWithContext:]
+ -[SVXSiriActivationListenerDelegate initWithSiriActivationListener:mainQueuePerformer:siriActivationSupportPredicate:virtualDeviceManager:instrumentationUtils:activationUtils:]
+ GCC_except_table1172
+ GCC_except_table1187
+ GCC_except_table1243
+ GCC_except_table1514
+ GCC_except_table1656
+ GCC_except_table1657
+ GCC_except_table1687
+ GCC_except_table1695
+ GCC_except_table1696
+ GCC_except_table1727
+ GCC_except_table1831
+ GCC_except_table1833
+ GCC_except_table1834
+ GCC_except_table1937
+ GCC_except_table2102
+ GCC_except_table2127
+ GCC_except_table2264
+ GCC_except_table2387
+ GCC_except_table2389
+ GCC_except_table2391
+ GCC_except_table2409
+ GCC_except_table2410
+ GCC_except_table2540
+ GCC_except_table2544
+ GCC_except_table2546
+ GCC_except_table2549
+ GCC_except_table2856
+ GCC_except_table3012
+ GCC_except_table3087
+ GCC_except_table798
+ OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._attendingStateQueue
+ OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._didPauseTTSForCurrentUserTurn
+ OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._lasAttendingTimeoutSeconds
+ OBJC_IVAR_$_SVXMissingAssetActivationDecision._promptLocalizationKey
+ OBJC_IVAR_$_SVXMissingAssetActivationDecision._shouldDeclineActivation
+ OBJC_IVAR_$_SVXMissingAssetActivationGuard._availabilityReporter
+ OBJC_IVAR_$_SVXMissingAssetActivationGuard._instrumentationUtils
+ OBJC_IVAR_$_SVXMissingAssetActivationGuard._siriAvailability
+ OBJC_IVAR_$_SVXMissingAssetActivationGuard._siriAvailabilityProvider
+ OBJC_IVAR_$_SVXSession._electionIdentity
+ OBJC_IVAR_$_SVXSession._electionLedgerOverride
+ OBJC_IVAR_$_SVXSession._launchSignpostIsButton
+ OBJC_IVAR_$_SVXSession._ledgerDeliveryQueue
+ OBJC_IVAR_$_SVXSession._rootRequestWasHoldToTalk
+ OBJC_IVAR_$_SVXSessionManager._missingAssetGuard
+ OBJC_IVAR_$_SVXSessionManager._sessionUtils
+ OBJC_IVAR_$_SVXSpeechSynthesizer._streamTaskTrackers
+ OBJC_IVAR_$_SVXSpeechSynthesizer._streamsWithFinishedPlayback
+ _CFNotificationCenterRemoveObserver
+ _OBJC_CLASS_$_SCDAElectionLedger
+ _OBJC_CLASS_$_SISchemaUEIUUFRReady
+ _OBJC_CLASS_$_SVXMissingAssetActivationDecision
+ _OBJC_CLASS_$_SVXMissingAssetActivationGuard
+ _OBJC_METACLASS_$_SVXMissingAssetActivationDecision
+ _OBJC_METACLASS_$_SVXMissingAssetActivationGuard
+ __49-[SVXSession releaseAudioSessionIfIdleForReason:]_block_invoke
+ __67-[SVXSessionManager _activateWithContext:activityState:completion:]_block_invoke
+ __OBJC_$_INSTANCE_METHODS_SVXMissingAssetActivationDecision
+ __OBJC_$_INSTANCE_METHODS_SVXMissingAssetActivationGuard
+ __OBJC_$_INSTANCE_VARIABLES_SVXMissingAssetActivationDecision
+ __OBJC_$_INSTANCE_VARIABLES_SVXMissingAssetActivationGuard
+ __OBJC_$_PROP_LIST_SVXMissingAssetActivationDecision
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SVXSpeechSynthesisListening
+ __OBJC_CLASS_RO_$_SVXMissingAssetActivationDecision
+ __OBJC_CLASS_RO_$_SVXMissingAssetActivationGuard
+ __OBJC_METACLASS_RO_$_SVXMissingAssetActivationDecision
+ __OBJC_METACLASS_RO_$_SVXMissingAssetActivationGuard
+ ___118-[SVXMyriadHostDevice startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:electionIdentity:completion:]_block_invoke
+ ___27-[SVXSession allTimersIdle]_block_invoke_2
+ ___38-[SVXMissingAssetActivationGuard init]_block_invoke
+ ___46-[SVXHomePodUIBridgeClientDelegate invalidate]_block_invoke
+ ___48-[SVXSession speechSynthesizerDidFinishPlayback]_block_invoke
+ ___49-[SVXSession releaseAudioSessionIfIdleForReason:]_block_invoke
+ ___53-[SVXHomePodUIBridgeClientDelegate didFinishPlayback]_block_invoke
+ ___60-[SVXSession uiBridgeClientShouldActivateForLASWithContext:]_block_invoke
+ ___61-[SVXSession _waitForLedgerDecisionForElection:usingHandler:]_block_invoke
+ ___61-[SVXSession _waitForLedgerDecisionForElection:usingHandler:]_block_invoke_2
+ ___61-[SVXSession uiBridgeClientDidStopAttendingWithoutActivation]_block_invoke
+ ___66-[SVXMissingAssetActivationGuard decisionForActivationIdentifier:]_block_invoke
+ ___66-[SVXSession speechSynthesizerDidFailStreamWithError:taskTracker:]_block_invoke
+ ___67-[SVXHomePodUIBridgeClientDelegate cancelPendingFollowUpActivation]_block_invoke
+ ___67-[SVXSessionManager _activateWithContext:activityState:completion:]_block_invoke
+ ___67-[SVXSessionManager _activateWithContext:activityState:completion:]_block_invoke_2
+ ___69-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceWillStartAttending]_block_invoke
+ ___71-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDetectedSpeechStart:]_block_invoke
+ ___73-[SVXHomePodUIBridgeClientDelegate beginAttendingForFollowUpWithContext:]_block_invoke
+ ___82-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidDetectUserSpeechWithContext:]_block_invoke
+ ___82-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidFinalizeUserTurnWithContext:]_block_invoke
+ ___82-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceReceivedSpeechMitigationResult:]_block_invoke
+ ___90-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidStopAttendingUnexpectedlyWithReason:]_block_invoke
+ ___block_descriptor_32_e28_"<SVXSiriAvailability>"8?0l
+ ___block_descriptor_48_e8_32w_e5_v8?0l
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48bs_e32_v20?0B8"SCDAElectionOutcome"12l
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0l
+ _objc_msgSend$_electionLedger
+ _objc_msgSend$_isRootRequestHoldToTalk
+ _objc_msgSend$_waitForLedgerDecisionForElection:usingHandler:
+ _objc_msgSend$beginElectionWithIdentity:
+ _objc_msgSend$cancelPendingFollowUpActivation
+ _objc_msgSend$decisionForActivationIdentifier:
+ _objc_msgSend$decisionForElection:reason:detail:deliverOn:completion:
+ _objc_msgSend$didFinishPlayback
+ _objc_msgSend$didPauseTTSForCurrentUserTurn
+ _objc_msgSend$didPromptListeningAfterSpeaking
+ _objc_msgSend$initWithAvailabilityReporter:siriAvailabilityProvider:instrumentationUtils:
+ _objc_msgSend$initWithShouldDeclineActivation:promptLocalizationKey:
+ _objc_msgSend$initWithSiriActivationListener:mainQueuePerformer:siriActivationSupportPredicate:virtualDeviceManager:instrumentationUtils:activationUtils:
+ _objc_msgSend$isContinuousConversationEnabled
+ _objc_msgSend$isUserInitiatedDeviceActivationWithContext:
+ _objc_msgSend$lasAttendingTimeoutSeconds
+ _objc_msgSend$myriadElectionIdentity
+ _objc_msgSend$promptLocalizationKey
+ _objc_msgSend$releaseAudioSessionIfIdleForReason:
+ _objc_msgSend$setAceCommandClass:
+ _objc_msgSend$setBlockAttending:
+ _objc_msgSend$setDidPauseTTSForCurrentUserTurn:
+ _objc_msgSend$setInteractionLinkId:
+ _objc_msgSend$setLogLinkId:
+ _objc_msgSend$setStreamId:
+ _objc_msgSend$sharedLedger
+ _objc_msgSend$shouldDeclineActivation
+ _objc_msgSend$speechSynthesizerDidFailStreamWithError:taskTracker:
+ _objc_msgSend$speechSynthesizerDidFinishPlayback
+ _objc_msgSend$startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:electionIdentity:completion:
+ _objc_msgSend$startAdvertisingFromAlertFiringVoiceTriggerWithContext:electionIdentity:
+ _objc_msgSend$startAdvertisingFromDirectTriggerWithContext:electionIdentity:
+ _objc_msgSend$startAdvertisingFromInTaskVoiceTriggerWithContext:electionIdentity:
+ _objc_msgSend$startAdvertisingFromVoiceTriggerWithGoodnessScoreContext:withContext:electionIdentity:
- -[SVXHomePodUIBridgeClientDelegate willPromptListeningAfterSpeaking]
- -[SVXMyriadDeviceManager startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:completion:]
- -[SVXMyriadHostDevice startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:completion:]
- -[SVXSiriActivationListenerDelegate _siriAvailabilityChanged]
- -[SVXSiriActivationListenerDelegate initWithSiriActivationListener:mainQueuePerformer:siriActivationSupportPredicate:virtualDeviceManager:instrumentationUtils:activationUtils:siriAvailability:availabilityReporter:]
- GCC_except_table1183
- GCC_except_table1198
- GCC_except_table1254
- GCC_except_table1525
- GCC_except_table1667
- GCC_except_table1668
- GCC_except_table1698
- GCC_except_table1706
- GCC_except_table1707
- GCC_except_table1838
- GCC_except_table1840
- GCC_except_table1841
- GCC_except_table1944
- GCC_except_table2105
- GCC_except_table2238
- GCC_except_table2361
- GCC_except_table2378
- GCC_except_table2379
- GCC_except_table2500
- GCC_except_table2504
- GCC_except_table2506
- GCC_except_table2509
- GCC_except_table2812
- GCC_except_table2968
- GCC_except_table3043
- GCC_except_table809
- OBJC_IVAR_$_SVXSiriActivationListenerDelegate._availabilityReporter
- OBJC_IVAR_$_SVXSiriActivationListenerDelegate._siriAvailability
- ___101-[SVXMyriadHostDevice startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:completion:]_block_invoke
- _objc_msgSend$initWithSiriActivationListener:mainQueuePerformer:siriActivationSupportPredicate:virtualDeviceManager:instrumentationUtils:activationUtils:siriAvailability:availabilityReporter:
- _objc_msgSend$setSiriAceViewId:
- _objc_msgSend$setSiriInputStreamId:
- _objc_msgSend$setSiriRequestId:
- _objc_msgSend$siriInputStreamId
- _objc_msgSend$startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:completion:
- _objc_msgSend$willPromptListeningAfterSpeaking
CStrings:
+ "\""
+ "#Choreography - TTS was never paused for this turn, skipping resume"
+ "#Choreography - TTS was never paused, skipping legacy resume"
+ "#Choreography New activation — cancelling stale LAS timer"
+ "#Choreography didFinishPlayback — starting follow-up window"
+ "#Choreography didPromptListeningAfterSpeaking: rootRequestId=%{public}@"
+ "%s #SVXInstrumentation - Emit UUFR ready event (aceCommandClass: %@)"
+ "%s #missingAssets - Declined activation timeout elapsed"
+ "%s #missingAssets - Declining activation for source %@ (promptKey = %@)"
+ "%s #missingAssets - Finishing declined activation"
+ "%s #myriad queueAdvertisementType:%lu, context=%@, goodnessScoreContext=%@, electionIdentity=%@"
+ "%s Election ledger answered identity %@ with didWin=%d."
+ "%s Hold-to-talk stop: set blockAttending=YES."
+ "%s Ignored because the stream does not belong to the current request. (_currentRequestUUID = %@, streamRequestUUID = %@)"
+ "%s Ignored failure of an unregistered stream. (streamId = %@, error = %@)"
+ "%s No connection; cannot release audio session. (reason = %@)"
+ "%s Rejecting %@ continuous-conversation activation — session originated from hold-to-talk."
+ "%s Released audio session if idle. (reason = %@)"
+ "%s Releasing audio session if idle (reason = %@, activityState = %lu)"
+ "%s Request election identity %@."
+ "%s Response stream failed; ending the abandoned request. (_currentRequestUUID = %@, error = %@)"
+ "%s Stopping TTS for the active request with no current speaking context... (ttsSession = %@, activeTTSRequest = %@)"
+ "%s Stream errored after its audio finished; reporting success. (streamId = %@, error = %@)"
+ "%s Waiting on the election ledger for identity %@."
+ "%s _electionIdentity (%@ -> %@)"
+ "%s error = %@, taskTracker = %@"
+ "-[SVXMissingAssetActivationGuard _siriAvailabilityChanged]"
+ "-[SVXMissingAssetActivationGuard decisionForActivationIdentifier:]"
+ "-[SVXMyriadDeviceManager startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:electionIdentity:completion:]"
+ "-[SVXMyriadHostDevice startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:electionIdentity:completion:]_block_invoke"
+ "-[SVXSession _waitForLedgerDecisionForElection:usingHandler:]"
+ "-[SVXSession _waitForLedgerDecisionForElection:usingHandler:]_block_invoke_2"
+ "-[SVXSession allTimersIdle]_block_invoke_2"
+ "-[SVXSession beginElectionWithIdentity:]"
+ "-[SVXSession releaseAudioSessionIfIdleForReason:]_block_invoke"
+ "-[SVXSession speechSynthesizerDidFailStreamWithError:taskTracker:]"
+ "-[SVXSession speechSynthesizerDidFailStreamWithError:taskTracker:]_block_invoke"
+ "-[SVXSession speechSynthesizerDidFinishPlayback]"
+ "-[SVXSession uiBridgeClientDidStopAttendingWithoutActivation]_block_invoke"
+ "-[SVXSession uiBridgeClientShouldActivateForLASWithContext:]_block_invoke"
+ "-[SVXSessionManager _activateWithContext:activityState:completion:]_block_invoke"
+ "-[SVXSessionManager _activateWithContext:activityState:completion:]_block_invoke_2"
+ "@\"<SVXSiriAvailability>\"8@?0"
+ "Missing Assets Prompt Finished"
+ "SVXInstrumentationEmitUUFRReady"
+ "activity %@"
+ "buttonLaunch"
+ "com.apple.siri.SVXHomePodUIBridgeClientDelegate.attending"
+ "com.apple.siri.vox.session.electionledger"
+ "v20@?0B8@\"SCDAElectionOutcome\"12"
+ "\xf0\xe1\xf0\xf0!"
- "#Choreography willPromptListeningAfterSpeaking: rootRequestId=%{public}@"
- "%s #Availability - Queued unavailability prompt"
- "%s #Availability - Received Virtual Device for unavailability prompt"
- "%s #missingAssets - Queued Speech Request"
- "%s #missingAssets - Received Virtual Device"
- "%s #myriad queueAdvertisementType:%lu, context=%@, goodnessScoreContext=%@"
- "%s Stopping stream because final chunk has been appended to stream."
- "-[SVXAceViewHandler streamingConsumerRequestsExecution:command:shouldWaitForAnimationCompletion:completion:]_block_invoke"
- "-[SVXMyriadDeviceManager startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:completion:]"
- "-[SVXMyriadHostDevice startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:completion:]_block_invoke"
- "-[SVXSession uiBridgeClientDidStopAttendingWithoutActivation]"
- "-[SVXSession uiBridgeClientShouldActivateForLASWithContext:]"
- "-[SVXSiriActivationListenerDelegate _siriAvailabilityChanged]"
- "5"
- "continuous_conversation"
- "\xf0\xd1\xf0\xe1"
```
