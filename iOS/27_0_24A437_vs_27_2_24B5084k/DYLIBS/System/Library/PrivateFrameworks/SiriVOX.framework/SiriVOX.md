## SiriVOX

> `/System/Library/PrivateFrameworks/SiriVOX.framework/SiriVOX`

```diff

-3600.52.7.0.0
-  __TEXT.__text: 0x824cc
-  __TEXT.__objc_methlist: 0x8b58
+3605.16.1.0.0
+  __TEXT.__text: 0x83fac
+  __TEXT.__objc_methlist: 0x8c78
   __TEXT.__const: 0x124
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x11850
+  __TEXT.__cstring: 0x11acb
   __TEXT.__swift5_capture: 0x78
   __TEXT.__swift5_reflstr: 0x16
-  __TEXT.__gcc_except_tab: 0x57c
-  __TEXT.__oslogstring: 0x89be
+  __TEXT.__gcc_except_tab: 0x5cc
+  __TEXT.__oslogstring: 0x8c2d
   __TEXT.__dlopen_cstrs: 0xda
-  __TEXT.__unwind_info: 0x2ba0
+  __TEXT.__unwind_info: 0x2c40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2be8
-  __DATA_CONST.__objc_classlist: 0x668
+  __DATA_CONST.__const: 0x2ca8
+  __DATA_CONST.__objc_classlist: 0x678
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d70
+  __DATA_CONST.__objc_selrefs: 0x3e38
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x498
+  __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x980
-  __DATA_CONST.__got: 0x788
-  __AUTH_CONST.__const: 0xc28
-  __AUTH_CONST.__cfstring: 0x5fe0
-  __AUTH_CONST.__objc_const: 0x13688
+  __DATA_CONST.__got: 0x798
+  __AUTH_CONST.__const: 0xc08
+  __AUTH_CONST.__cfstring: 0x6020
+  __AUTH_CONST.__objc_const: 0x139a0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH_CONST.__auth_got: 0x6d8
-  __AUTH.__objc_data: 0x40b0
+  __AUTH_CONST.__auth_got: 0x6e8
+  __AUTH.__objc_data: 0x4150
   __AUTH.__data: 0x38
-  __DATA.__objc_ivar: 0xca8
+  __DATA.__objc_ivar: 0xcdc
   __DATA.__data: 0x2260
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3142
-  Symbols:   8313
-  CStrings:  2252
+  Functions: 3179
+  Symbols:   8416
+  CStrings:  2276
 
Symbols:
+ -[SVXHomePodUIBridgeClientDelegate cancelPendingFollowUpActivation]
+ -[SVXHomePodUIBridgeClientDelegate didFinishPlayback]
+ -[SVXHomePodUIBridgeClientDelegate lasAttendingTimeoutSeconds]
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
+ -[SVXSession releaseAudioSessionIfIdleForReason:]
+ -[SVXSession speechSynthesizerDidFinishPlayback]
+ -[SVXSessionUtils isUserInitiatedDeviceActivationWithContext:]
+ -[SVXSiriActivationListenerDelegate initWithSiriActivationListener:mainQueuePerformer:siriActivationSupportPredicate:virtualDeviceManager:instrumentationUtils:activationUtils:]
+ GCC_except_table1147
+ GCC_except_table1162
+ GCC_except_table1218
+ GCC_except_table1489
+ GCC_except_table1631
+ GCC_except_table1632
+ GCC_except_table1662
+ GCC_except_table1668
+ GCC_except_table1669
+ GCC_except_table1700
+ GCC_except_table1804
+ GCC_except_table1806
+ GCC_except_table1807
+ GCC_except_table1914
+ GCC_except_table2076
+ GCC_except_table2099
+ GCC_except_table2236
+ GCC_except_table2358
+ GCC_except_table2360
+ GCC_except_table2362
+ GCC_except_table2378
+ GCC_except_table2379
+ GCC_except_table2507
+ GCC_except_table2511
+ GCC_except_table2513
+ GCC_except_table2516
+ GCC_except_table2820
+ GCC_except_table2975
+ GCC_except_table3050
+ GCC_except_table772
+ _CFNotificationCenterRemoveObserver
+ _OBJC_CLASS_$_SCDAElectionLedger
+ _OBJC_CLASS_$_SISchemaUEIUUFRReady
+ _OBJC_CLASS_$_SVXMissingAssetActivationDecision
+ _OBJC_CLASS_$_SVXMissingAssetActivationGuard
+ _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._attendingStateQueue
+ _OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._lasAttendingTimeoutSeconds
+ _OBJC_IVAR_$_SVXMissingAssetActivationDecision._promptLocalizationKey
+ _OBJC_IVAR_$_SVXMissingAssetActivationDecision._shouldDeclineActivation
+ _OBJC_IVAR_$_SVXMissingAssetActivationGuard._availabilityReporter
+ _OBJC_IVAR_$_SVXMissingAssetActivationGuard._instrumentationUtils
+ _OBJC_IVAR_$_SVXMissingAssetActivationGuard._siriAvailability
+ _OBJC_IVAR_$_SVXMissingAssetActivationGuard._siriAvailabilityProvider
+ _OBJC_IVAR_$_SVXSession._electionIdentity
+ _OBJC_IVAR_$_SVXSession._electionLedgerOverride
+ _OBJC_IVAR_$_SVXSession._launchSignpostIsButton
+ _OBJC_IVAR_$_SVXSession._ledgerDeliveryQueue
+ _OBJC_IVAR_$_SVXSession._rootRequestWasHoldToTalk
+ _OBJC_IVAR_$_SVXSessionManager._missingAssetGuard
+ _OBJC_IVAR_$_SVXSessionManager._sessionUtils
+ _OBJC_METACLASS_$_SVXMissingAssetActivationDecision
+ _OBJC_METACLASS_$_SVXMissingAssetActivationGuard
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
+ ___67-[SVXHomePodUIBridgeClientDelegate cancelPendingFollowUpActivation]_block_invoke
+ ___67-[SVXSessionManager _activateWithContext:activityState:completion:]_block_invoke
+ ___67-[SVXSessionManager _activateWithContext:activityState:completion:]_block_invoke_2
+ ___69-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceWillStartAttending]_block_invoke
+ ___73-[SVXHomePodUIBridgeClientDelegate beginAttendingForFollowUpWithContext:]_block_invoke
+ ___82-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidDetectUserSpeechWithContext:]_block_invoke
+ ___82-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidFinalizeUserTurnWithContext:]_block_invoke
+ ___90-[SVXHomePodUIBridgeClientDelegate uiBridgeServiceDidStopAttendingUnexpectedlyWithReason:]_block_invoke
+ ___block_descriptor_32_e28_"<SVXSiriAvailability>"8?0l
+ ___block_descriptor_48_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e32_v20?0B8"SCDAElectionOutcome"12ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$_electionLedger
+ _objc_msgSend$_isRootRequestHoldToTalk
+ _objc_msgSend$_waitForLedgerDecisionForElection:usingHandler:
+ _objc_msgSend$beginElectionWithIdentity:
+ _objc_msgSend$cancelPendingFollowUpActivation
+ _objc_msgSend$decisionForActivationIdentifier:
+ _objc_msgSend$decisionForElection:reason:detail:deliverOn:completion:
+ _objc_msgSend$didFinishPlayback
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
+ _objc_msgSend$setInteractionLinkId:
+ _objc_msgSend$setLogLinkId:
+ _objc_msgSend$setStreamId:
+ _objc_msgSend$sharedLedger
+ _objc_msgSend$shouldDeclineActivation
+ _objc_msgSend$speechSynthesizerDidFinishPlayback
+ _objc_msgSend$startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:electionIdentity:completion:
+ _objc_msgSend$startAdvertisingFromAlertFiringVoiceTriggerWithContext:electionIdentity:
+ _objc_msgSend$startAdvertisingFromDirectTriggerWithContext:electionIdentity:
+ _objc_msgSend$startAdvertisingFromInTaskVoiceTriggerWithContext:electionIdentity:
+ _objc_msgSend$startAdvertisingFromVoiceTriggerWithGoodnessScoreContext:withContext:electionIdentity:
+ _objc_release_x3
- -[SVXHomePodUIBridgeClientDelegate willPromptListeningAfterSpeaking]
- -[SVXMyriadDeviceManager startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:completion:]
- -[SVXMyriadHostDevice startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:completion:]
- -[SVXSiriActivationListenerDelegate _siriAvailabilityChanged]
- -[SVXSiriActivationListenerDelegate initWithSiriActivationListener:mainQueuePerformer:siriActivationSupportPredicate:virtualDeviceManager:instrumentationUtils:activationUtils:siriAvailability:availabilityReporter:]
- GCC_except_table1158
- GCC_except_table1173
- GCC_except_table1229
- GCC_except_table1500
- GCC_except_table1642
- GCC_except_table1643
- GCC_except_table1673
- GCC_except_table1679
- GCC_except_table1680
- GCC_except_table1811
- GCC_except_table1813
- GCC_except_table1814
- GCC_except_table1921
- GCC_except_table2081
- GCC_except_table2214
- GCC_except_table2337
- GCC_except_table2352
- GCC_except_table2353
- GCC_except_table2472
- GCC_except_table2476
- GCC_except_table2478
- GCC_except_table2481
- GCC_except_table2783
- GCC_except_table2938
- GCC_except_table3013
- GCC_except_table783
- _OBJC_IVAR_$_SVXSiriActivationListenerDelegate._availabilityReporter
- _OBJC_IVAR_$_SVXSiriActivationListenerDelegate._siriAvailability
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
+ "%s No connection; cannot release audio session. (reason = %@)"
+ "%s Rejecting %@ continuous-conversation activation — session originated from hold-to-talk."
+ "%s Released audio session if idle. (reason = %@)"
+ "%s Releasing audio session if idle (reason = %@, activityState = %lu)"
+ "%s Request election identity %@."
+ "%s Waiting on the election ledger for identity %@."
+ "%s _electionIdentity (%@ -> %@)"
+ "-[SVXMissingAssetActivationGuard _siriAvailabilityChanged]"
+ "-[SVXMissingAssetActivationGuard decisionForActivationIdentifier:]"
+ "-[SVXMyriadDeviceManager startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:electionIdentity:completion:]"
+ "-[SVXMyriadHostDevice startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:electionIdentity:completion:]_block_invoke"
+ "-[SVXSession _waitForLedgerDecisionForElection:usingHandler:]"
+ "-[SVXSession _waitForLedgerDecisionForElection:usingHandler:]_block_invoke_2"
+ "-[SVXSession allTimersIdle]_block_invoke_2"
+ "-[SVXSession beginElectionWithIdentity:]"
+ "-[SVXSession releaseAudioSessionIfIdleForReason:]_block_invoke"
+ "-[SVXSession speechSynthesizerDidFinishPlayback]"
+ "-[SVXSession uiBridgeClientDidStopAttendingWithoutActivation]_block_invoke"
+ "-[SVXSession uiBridgeClientShouldActivateForLASWithContext:]_block_invoke"
+ "-[SVXSessionManager _activateWithContext:activityState:completion:]_block_invoke_2"
+ "@\"<SVXSiriAvailability>\"8@?0"
+ "Missing Assets Prompt Finished"
+ "SVXInstrumentationEmitUUFRReady"
+ "activity %@"
+ "buttonLaunch"
+ "com.apple.siri.SVXHomePodUIBridgeClientDelegate.attending"
+ "com.apple.siri.vox.session.electionledger"
+ "v20@?0B8@\"SCDAElectionOutcome\"12"
+ "\xf0\xf1\xf0\xf01"
- "#Choreography willPromptListeningAfterSpeaking: rootRequestId=%{public}@"
- "%s #Availability - Queued unavailability prompt"
- "%s #Availability - Received Virtual Device for unavailability prompt"
- "%s #missingAssets - Queued Speech Request"
- "%s #missingAssets - Received Virtual Device"
- "%s #myriad queueAdvertisementType:%lu, context=%@, goodnessScoreContext=%@"
- "%s Stopping stream because final chunk has been appended to stream."
- "-[SVXAceViewHandler streamingConsumerRequestsExecution:command:shouldWaitForAnimationCompletion:completion:]_block_invoke_3"
- "-[SVXMyriadDeviceManager startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:completion:]"
- "-[SVXMyriadHostDevice startAdvertising:withSCDAGoodnessScoreContext:withSCDAAudioContext:completion:]_block_invoke"
- "-[SVXSession uiBridgeClientDidStopAttendingWithoutActivation]"
- "-[SVXSession uiBridgeClientShouldActivateForLASWithContext:]"
- "-[SVXSiriActivationListenerDelegate _siriAvailabilityChanged]"
- "5"
- "continuous_conversation"
- "\xf0\xe1\xf0\xf1"
```
