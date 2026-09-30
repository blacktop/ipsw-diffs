## SiriVOX

> `/System/Library/PrivateFrameworks/SiriVOX.framework/Versions/A/SiriVOX`

```diff

-3600.52.7.0.0
-  __TEXT.__text: 0x88828
-  __TEXT.__objc_methlist: 0x8a98
+3605.15.1.0.0
+  __TEXT.__text: 0x89ce4
+  __TEXT.__objc_methlist: 0x8b90
   __TEXT.__const: 0x12c
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x97
   __TEXT.__swift5_fieldmd: 0x38
   __TEXT.__swift5_types: 0x8
-  __TEXT.__cstring: 0x113fe
+  __TEXT.__cstring: 0x1157e
   __TEXT.__swift5_capture: 0x78
   __TEXT.__swift5_reflstr: 0x16
-  __TEXT.__gcc_except_tab: 0x580
-  __TEXT.__oslogstring: 0x86e7
+  __TEXT.__gcc_except_tab: 0x5cc
+  __TEXT.__oslogstring: 0x8850
   __TEXT.__dlopen_cstrs: 0xda
-  __TEXT.__unwind_info: 0x2c00
+  __TEXT.__unwind_info: 0x2c98
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
+  __DATA_CONST.__objc_selrefs: 0x3d38
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x498
+  __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0x980
   __DATA_CONST.__got: 0x768
-  __AUTH_CONST.__const: 0x2c28
-  __AUTH_CONST.__cfstring: 0x5f20
-  __AUTH_CONST.__objc_const: 0x13560
+  __AUTH_CONST.__const: 0x2c38
+  __AUTH_CONST.__cfstring: 0x5f40
+  __AUTH_CONST.__objc_const: 0x13818
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xe58
   __AUTH_CONST.__objc_dictobj: 0x348
-  __AUTH_CONST.__auth_got: 0x568
-  __AUTH.__objc_data: 0x40b0
+  __AUTH_CONST.__auth_got: 0x570
+  __AUTH.__objc_data: 0x4150
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0xc8c
+  __DATA.__objc_ivar: 0xcb4
   __DATA.__data: 0x2260
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3171
-  Symbols:   8291
-  CStrings:  2224
+  Functions: 3202
+  Symbols:   8370
+  CStrings:  2237
 
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
+ -[SVXSession _isRootRequestHoldToTalk]
+ -[SVXSession releaseAudioSessionIfIdleForReason:]
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
+ GCC_except_table2100
+ GCC_except_table2123
+ GCC_except_table2260
+ GCC_except_table2382
+ GCC_except_table2384
+ GCC_except_table2386
+ GCC_except_table2404
+ GCC_except_table2405
+ GCC_except_table2529
+ GCC_except_table2533
+ GCC_except_table2535
+ GCC_except_table2538
+ GCC_except_table2843
+ GCC_except_table2999
+ GCC_except_table3074
+ GCC_except_table798
+ OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._attendingStateQueue
+ OBJC_IVAR_$_SVXHomePodUIBridgeClientDelegate._lasAttendingTimeoutSeconds
+ OBJC_IVAR_$_SVXMissingAssetActivationDecision._promptLocalizationKey
+ OBJC_IVAR_$_SVXMissingAssetActivationDecision._shouldDeclineActivation
+ OBJC_IVAR_$_SVXMissingAssetActivationGuard._availabilityReporter
+ OBJC_IVAR_$_SVXMissingAssetActivationGuard._instrumentationUtils
+ OBJC_IVAR_$_SVXMissingAssetActivationGuard._siriAvailability
+ OBJC_IVAR_$_SVXMissingAssetActivationGuard._siriAvailabilityProvider
+ OBJC_IVAR_$_SVXSession._launchSignpostIsButton
+ OBJC_IVAR_$_SVXSession._rootRequestWasHoldToTalk
+ OBJC_IVAR_$_SVXSessionManager._missingAssetGuard
+ OBJC_IVAR_$_SVXSessionManager._sessionUtils
+ _CFNotificationCenterRemoveObserver
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
+ ___27-[SVXSession allTimersIdle]_block_invoke_2
+ ___38-[SVXMissingAssetActivationGuard init]_block_invoke
+ ___46-[SVXHomePodUIBridgeClientDelegate invalidate]_block_invoke
+ ___48-[SVXSession speechSynthesizerDidFinishPlayback]_block_invoke
+ ___49-[SVXSession releaseAudioSessionIfIdleForReason:]_block_invoke
+ ___53-[SVXHomePodUIBridgeClientDelegate didFinishPlayback]_block_invoke
+ ___60-[SVXSession uiBridgeClientShouldActivateForLASWithContext:]_block_invoke
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
+ ___block_descriptor_48_e8_32w_e5_v8?0l
+ _objc_msgSend$_isRootRequestHoldToTalk
+ _objc_msgSend$cancelPendingFollowUpActivation
+ _objc_msgSend$decisionForActivationIdentifier:
+ _objc_msgSend$didFinishPlayback
+ _objc_msgSend$didPromptListeningAfterSpeaking
+ _objc_msgSend$initWithAvailabilityReporter:siriAvailabilityProvider:instrumentationUtils:
+ _objc_msgSend$initWithShouldDeclineActivation:promptLocalizationKey:
+ _objc_msgSend$initWithSiriActivationListener:mainQueuePerformer:siriActivationSupportPredicate:virtualDeviceManager:instrumentationUtils:activationUtils:
+ _objc_msgSend$isContinuousConversationEnabled
+ _objc_msgSend$isUserInitiatedDeviceActivationWithContext:
+ _objc_msgSend$lasAttendingTimeoutSeconds
+ _objc_msgSend$promptLocalizationKey
+ _objc_msgSend$releaseAudioSessionIfIdleForReason:
+ _objc_msgSend$setBlockAttending:
+ _objc_msgSend$setInteractionLinkId:
+ _objc_msgSend$setLogLinkId:
+ _objc_msgSend$setStreamId:
+ _objc_msgSend$shouldDeclineActivation
+ _objc_msgSend$speechSynthesizerDidFinishPlayback
- -[SVXHomePodUIBridgeClientDelegate willPromptListeningAfterSpeaking]
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
- _objc_msgSend$initWithSiriActivationListener:mainQueuePerformer:siriActivationSupportPredicate:virtualDeviceManager:instrumentationUtils:activationUtils:siriAvailability:availabilityReporter:
- _objc_msgSend$setSiriAceViewId:
- _objc_msgSend$setSiriInputStreamId:
- _objc_msgSend$setSiriRequestId:
- _objc_msgSend$siriInputStreamId
- _objc_msgSend$willPromptListeningAfterSpeaking
CStrings:
+ "\""
+ "#Choreography New activation — cancelling stale LAS timer"
+ "#Choreography didFinishPlayback — starting follow-up window"
+ "#Choreography didPromptListeningAfterSpeaking: rootRequestId=%{public}@"
+ "%s #missingAssets - Declined activation timeout elapsed"
+ "%s #missingAssets - Declining activation for source %@ (promptKey = %@)"
+ "%s #missingAssets - Finishing declined activation"
+ "%s Hold-to-talk stop: set blockAttending=YES."
+ "%s No connection; cannot release audio session. (reason = %@)"
+ "%s Rejecting %@ continuous-conversation activation — session originated from hold-to-talk."
+ "%s Released audio session if idle. (reason = %@)"
+ "%s Releasing audio session if idle (reason = %@, activityState = %lu)"
+ "-[SVXMissingAssetActivationGuard _siriAvailabilityChanged]"
+ "-[SVXMissingAssetActivationGuard decisionForActivationIdentifier:]"
+ "-[SVXSession allTimersIdle]_block_invoke_2"
+ "-[SVXSession releaseAudioSessionIfIdleForReason:]_block_invoke"
+ "-[SVXSession speechSynthesizerDidFinishPlayback]"
+ "-[SVXSession uiBridgeClientDidStopAttendingWithoutActivation]_block_invoke"
+ "-[SVXSession uiBridgeClientShouldActivateForLASWithContext:]_block_invoke"
+ "-[SVXSessionManager _activateWithContext:activityState:completion:]_block_invoke"
+ "-[SVXSessionManager _activateWithContext:activityState:completion:]_block_invoke_2"
+ "@\"<SVXSiriAvailability>\"8@?0"
+ "Missing Assets Prompt Finished"
+ "buttonLaunch"
+ "com.apple.siri.SVXHomePodUIBridgeClientDelegate.attending"
+ "\xf0\xe1\xf0\xe1"
- "#Choreography willPromptListeningAfterSpeaking: rootRequestId=%{public}@"
- "%s #Availability - Queued unavailability prompt"
- "%s #Availability - Received Virtual Device for unavailability prompt"
- "%s #missingAssets - Queued Speech Request"
- "%s #missingAssets - Received Virtual Device"
- "%s Stopping stream because final chunk has been appended to stream."
- "-[SVXAceViewHandler streamingConsumerRequestsExecution:command:shouldWaitForAnimationCompletion:completion:]_block_invoke"
- "-[SVXSession uiBridgeClientDidStopAttendingWithoutActivation]"
- "-[SVXSession uiBridgeClientShouldActivateForLASWithContext:]"
- "-[SVXSiriActivationListenerDelegate _siriAvailabilityChanged]"
- "5"
- "continuous_conversation"
- "\xf0\xd1\xf0\xe1"
```
