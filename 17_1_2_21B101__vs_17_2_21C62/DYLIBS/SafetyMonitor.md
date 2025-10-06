## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-893.0.5.0.2
-  __TEXT.__text: 0x58350
+895.0.11.0.2
+  __TEXT.__text: 0x58630
   __TEXT.__auth_stubs: 0x11e0
-  __TEXT.__objc_methlist: 0x3550
+  __TEXT.__objc_methlist: 0x3588
   __TEXT.__const: 0xe70
-  __TEXT.__cstring: 0x6edc
+  __TEXT.__cstring: 0x6f15
   __TEXT.__swift5_typeref: 0x441
   __TEXT.__swift5_capture: 0xf4
   __TEXT.__constg_swiftt: 0x358

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0xb0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__oslogstring: 0x3230
+  __TEXT.__oslogstring: 0x3267
   __TEXT.__ustring: 0x8c4
-  __TEXT.__gcc_except_tab: 0x7d4
+  __TEXT.__gcc_except_tab: 0x7c8
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x1cec
+  __TEXT.__unwind_info: 0x1ce4
   __TEXT.__eh_frame: 0x9c8
   __TEXT.__objc_classname: 0x7d7
-  __TEXT.__objc_methname: 0x978c
-  __TEXT.__objc_methtype: 0x170b
-  __TEXT.__objc_stubs: 0x4900
+  __TEXT.__objc_methname: 0x98da
+  __TEXT.__objc_methtype: 0x1726
+  __TEXT.__objc_stubs: 0x4920
   __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x10a0
+  __DATA_CONST.__const: 0x1140
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x59a0
-  __DATA_CONST.__objc_selrefs: 0x1a30
+  __DATA_CONST.__objc_const: 0x5a20
+  __DATA_CONST.__objc_selrefs: 0x1a58
   __AUTH_CONST.__const: 0x7c8
   __AUTH_CONST.__objc_const: 0x1c58
   __AUTH_CONST.__cfstring: 0x41c0

   __DATA.__data: 0xdc0
   __DATA.__common: 0xf8
   __DATA.__bss: 0x1200
-  __DATA_DIRTY.__objc_ivar: 0x17c
+  __DATA_DIRTY.__objc_ivar: 0x184
   __DATA_DIRTY.__objc_data: 0x6f0
   __DATA_DIRTY.__data: 0xd8
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E91DB5BC-4EF2-38E1-998E-C82025ADD218
-  Functions: 1748
-  Symbols:   4600
-  CStrings:  3103
+  UUID: EF1781CD-10CA-3706-B65B-43CA4C94F524
+  Functions: 1754
+  Symbols:   4619
+  CStrings:  3115
 
Symbols:
+ -[SMReceiverContact firstDetailViewSessionState]
+ -[SMReceiverContact initWithIdentifier:syncDate:phoneCache:watchCache:sessionStatus:allowReadToken:safetyCacheKey:shareURL:participantID:sharingInvitationData:numCacheDownloads:numSuccessfulCacheDownloads:maxPhoneCacheSize:maxWatchCacheSize:maxLocationsInPhoneCacheTrace:maxLocationsInWatchCacheTrace:timeTillCacheRelease:timeTillFirstSuccessfulCacheDownload:sessionID:firstDetailViewSessionState:lastDetailViewSessionState:]
+ -[SMReceiverContact lastDetailViewSessionState]
+ -[SMReceiverContact setFirstDetailViewSessionState:]
+ -[SMReceiverContact setLastDetailViewSessionState:]
+ -[SMSafetyMonitorManager detailsViewOpenedForSessionID:]
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.274
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.273
+ ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.322
+ ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke
+ ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.337
+ ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.323
+ ___58-[SMSafetyMonitorManager cancelInitializationWithHandler:]_block_invoke.301
+ ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.320
+ ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.321
+ ___62-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]_block_invoke.316
+ ___62-[SMSafetyMonitorManager initializeSessionWithHandle:handler:]_block_invoke.298
+ ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.305
+ ___64-[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]_block_invoke.303
+ ___64-[SMSafetyMonitorManager startSessionWithConfiguration:handler:]_block_invoke.306
+ ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.315
+ ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.304
+ ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.313
+ ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.302
+ ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.317
+ ___69-[SMSafetyMonitorManager fetchSessionReceiptForSessionID:completion:]_block_invoke.324
+ ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.326
+ ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.334
+ ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.339
+ ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.332
+ ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.309
+ ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.328
+ ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.336
+ ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.340
+ ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.312
+ ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.327
+ ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.330
+ ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.331
+ ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.319
+ ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.307
+ ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.308
+ ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.341
+ ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.318
+ ___91-[SMSafetyMonitorManager prepareUserInfoForNotificationContent:initiatorHandle:messageUrl:]_block_invoke.346
+ ___block_descriptor_48_e8_32s40bs_e74_v56?0"NSUUID"8"SMCache"16"SMCache"24"NSDate"32"NSDate"40"NSError"48ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v16?08ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e17_v16?0"NSError"8lr48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e46_v28?0"SMSessionManagerState"8B16"NSError"20lr48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e52_v40?0"NSUUID"8"SMCache"16"SMCache"24"NSError"32lr48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e56_v32?0"NSUUID"8"SMReceiverSessionStatus"16"NSError"24lr48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48r_e8_v16?08lr48l8s40l8s32l8
+ ___block_literal_global.311
+ ___block_literal_global.430
+ _objc_msgSend$detailsViewOpenedForSessionID:
- -[SMReceiverContact initWithIdentifier:syncDate:phoneCache:watchCache:sessionStatus:allowReadToken:safetyCacheKey:shareURL:participantID:sharingInvitationData:numCacheDownloads:numSuccessfulCacheDownloads:maxPhoneCacheSize:maxWatchCacheSize:maxLocationsInPhoneCacheTrace:maxLocationsInWatchCacheTrace:timeTillCacheRelease:timeTillFirstSuccessfulCacheDownload:sessionID:]
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.270
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.271
- ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.320
- ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.321
- ___58-[SMSafetyMonitorManager cancelInitializationWithHandler:]_block_invoke.299
- ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.318
- ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.319
- ___62-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]_block_invoke.314
- ___62-[SMSafetyMonitorManager initializeSessionWithHandle:handler:]_block_invoke.296
- ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.303
- ___64-[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]_block_invoke.301
- ___64-[SMSafetyMonitorManager startSessionWithConfiguration:handler:]_block_invoke.304
- ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.313
- ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.302
- ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.311
- ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.300
- ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.315
- ___69-[SMSafetyMonitorManager fetchSessionReceiptForSessionID:completion:]_block_invoke.322
- ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.324
- ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.332
- ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.336
- ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.330
- ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.307
- ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.326
- ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.334
- ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.337
- ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.310
- ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.325
- ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.328
- ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.329
- ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.317
- ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.305
- ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.306
- ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.338
- ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.316
- ___91-[SMSafetyMonitorManager prepareUserInfoForNotificationContent:initiatorHandle:messageUrl:]_block_invoke.343
- ___block_descriptor_40_e8_32bs_e74_v56?0"NSUUID"8"SMCache"16"SMCache"24"NSDate"32"NSDate"40"NSError"48ls32l8
- ___block_descriptor_48_e8_32bs40r_e52_v40?0"NSUUID"8"SMCache"16"SMCache"24"NSError"32lr40l8s32l8
- ___block_descriptor_48_e8_32bs40r_e56_v32?0"NSUUID"8"SMReceiverSessionStatus"16"NSError"24lr40l8s32l8
- ___block_literal_global.309
- ___block_literal_global.427
CStrings:
+ "-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]"
+ "@184@0:8@16@24@32@40@48@56@64@72@80@88q96q104q112q120q128q136d144d152@160q168q176"
+ "Invalid parameter not satisfying: sessionID (in %s:%d)"
+ "Tq,N,V_firstDetailViewSessionState"
+ "Tq,N,V_lastDetailViewSessionState"
+ "_firstDetailViewSessionState"
+ "_lastDetailViewSessionState"
+ "detailsViewOpenedForSessionID:"
+ "firstDetailViewSessionState"
+ "initWithIdentifier:syncDate:phoneCache:watchCache:sessionStatus:allowReadToken:safetyCacheKey:shareURL:participantID:sharingInvitationData:numCacheDownloads:numSuccessfulCacheDownloads:maxPhoneCacheSize:maxWatchCacheSize:maxLocationsInPhoneCacheTrace:maxLocationsInWatchCacheTrace:timeTillCacheRelease:timeTillFirstSuccessfulCacheDownload:sessionID:firstDetailViewSessionState:lastDetailViewSessionState:"
+ "lastDetailViewSessionState"
+ "setFirstDetailViewSessionState:"
+ "setLastDetailViewSessionState:"
+ "v24@0:8@\"NSUUID\"16"
- "@168@0:8@16@24@32@40@48@56@64@72@80@88q96q104q112q120q128q136d144d152@160"
- "initWithIdentifier:syncDate:phoneCache:watchCache:sessionStatus:allowReadToken:safetyCacheKey:shareURL:participantID:sharingInvitationData:numCacheDownloads:numSuccessfulCacheDownloads:maxPhoneCacheSize:maxWatchCacheSize:maxLocationsInPhoneCacheTrace:maxLocationsInWatchCacheTrace:timeTillCacheRelease:timeTillFirstSuccessfulCacheDownload:sessionID:"

```
