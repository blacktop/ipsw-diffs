## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-1048.0.0.0.0
-  __TEXT.__text: 0x71d10
-  __TEXT.__auth_stubs: 0x1240
-  __TEXT.__objc_methlist: 0x4cc4
-  __TEXT.__const: 0x1378
+1053.0.1.0.0
+  __TEXT.__text: 0x72538
+  __TEXT.__auth_stubs: 0x1250
+  __TEXT.__objc_methlist: 0x4ce4
+  __TEXT.__const: 0x1380
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__cstring: 0xbcf5
+  __TEXT.__cstring: 0xbd41
   __TEXT.__swift5_typeref: 0x4a2
   __TEXT.__oslogstring: 0x4345
   __TEXT.__constg_swiftt: 0x450

   __TEXT.__swift5_fieldmd: 0x3ec
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_capture: 0x120
+  __TEXT.__swift5_capture: 0x140
   __TEXT.__swift5_proto: 0xd0
   __TEXT.__swift5_types: 0x54
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift5_protos: 0x4
   __TEXT.__ustring: 0xd34
-  __TEXT.__gcc_except_tab: 0xf58
-  __TEXT.__unwind_info: 0x17a8
-  __TEXT.__eh_frame: 0x98c
+  __TEXT.__gcc_except_tab: 0xf70
+  __TEXT.__unwind_info: 0x17d8
+  __TEXT.__eh_frame: 0x9dc
   __TEXT.__objc_classname: 0x9c9
-  __TEXT.__objc_methname: 0xc41f
+  __TEXT.__objc_methname: 0xc447
   __TEXT.__objc_methtype: 0x2155
-  __TEXT.__objc_stubs: 0x57c0
+  __TEXT.__objc_stubs: 0x57e0
   __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__const: 0x1458
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2250
+  __DATA_CONST.__objc_selrefs: 0x2258
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1a8
-  __AUTH_CONST.__auth_got: 0x930
-  __AUTH_CONST.__const: 0x960
+  __AUTH_CONST.__auth_got: 0x938
+  __AUTH_CONST.__const: 0x9b0
   __AUTH_CONST.__cfstring: 0x4ea0
-  __AUTH_CONST.__objc_const: 0x81d8
+  __AUTH_CONST.__objc_const: 0x81e0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x11c0
   __AUTH.__data: 0x2d8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8AA57328-DB3E-3016-8954-E4B31E391F94
-  Functions: 2163
-  Symbols:   5647
-  CStrings:  3973
+  UUID: 1CFD94B0-AF0A-3B35-B22C-C3B3AB026072
+  Functions: 2173
+  Symbols:   5656
+  CStrings:  3975
 
Symbols:
+ -[SMSafetyMonitorManager checkIMessageAccountEnabledWithHandler:]
+ GCC_except_table355
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.328
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.327
+ ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.386
+ ___54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.391
+ ___55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.390
+ ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.404
+ ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.387
+ ___58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke.366
+ ___60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.388
+ ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.384
+ ___61-[SMSafetyMonitorManager cancelInitializationWithCompletion:]_block_invoke.353
+ ___61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.389
+ ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.385
+ ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.357
+ ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.370
+ ___65-[SMSafetyMonitorManager checkIMessageAccountEnabledWithHandler:]_block_invoke
+ ___65-[SMSafetyMonitorManager checkIMessageAccountEnabledWithHandler:]_block_invoke_2
+ ___65-[SMSafetyMonitorManager checkIMessageAccountEnabledWithHandler:]_block_invoke_3
+ ___65-[SMSafetyMonitorManager fetchCurrentSessionStateWithCompletion:]_block_invoke.371
+ ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.356
+ ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.368
+ ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.354
+ ___67-[SMSafetyMonitorManager endSessionForSessionID:reason:completion:]_block_invoke.355
+ ___67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.372
+ ___67-[SMSafetyMonitorManager startSessionWithConfiguration:completion:]_block_invoke.358
+ ___68-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]_block_invoke.364
+ ___68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.376
+ ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.381
+ ___69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.375
+ ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.393
+ ___70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.374
+ ___71-[SMSafetyMonitorManager initializeSessionWithConversation:completion:]_block_invoke.350
+ ___72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.379
+ ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.401
+ ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.407
+ ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.399
+ ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.361
+ ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.395
+ ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.403
+ ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.408
+ ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.367
+ ___76-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithOptions:handler:]_block_invoke.378
+ ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.394
+ ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.397
+ ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.398
+ ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.383
+ ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.359
+ ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.360
+ ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.409
+ ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.382
+ ___block_literal_global.363
+ ___block_literal_global.502
+ _objc_msgSend$checkIMessageAccountEnabledWithHandler:
- GCC_except_table351
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.324
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.325
- ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.384
- ___54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.389
- ___55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.388
- ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.402
- ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.385
- ___58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke.364
- ___60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.386
- ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.382
- ___61-[SMSafetyMonitorManager cancelInitializationWithCompletion:]_block_invoke.351
- ___61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.387
- ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.383
- ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.355
- ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.368
- ___65-[SMSafetyMonitorManager fetchCurrentSessionStateWithCompletion:]_block_invoke.369
- ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.354
- ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.366
- ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.352
- ___67-[SMSafetyMonitorManager endSessionForSessionID:reason:completion:]_block_invoke.353
- ___67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.370
- ___67-[SMSafetyMonitorManager startSessionWithConfiguration:completion:]_block_invoke.356
- ___68-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]_block_invoke.362
- ___68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.374
- ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.379
- ___69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.373
- ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.391
- ___70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.372
- ___71-[SMSafetyMonitorManager initializeSessionWithConversation:completion:]_block_invoke.348
- ___72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.377
- ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.399
- ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.405
- ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.397
- ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.359
- ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.393
- ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.401
- ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.406
- ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.365
- ___76-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithOptions:handler:]_block_invoke.376
- ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.392
- ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.395
- ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.396
- ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.381
- ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.357
- ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.358
- ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.407
- ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.380
- ___block_literal_global.361
- ___block_literal_global.500
CStrings:
+ "-[SMSafetyMonitorManager checkIMessageAccountEnabledWithHandler:]"
+ "T@\"NSDate\",C,N,V_keyReleaseMessageSendDate"
+ "checkIMessageAccountEnabledWithHandler:"
+ "messages://open?groupid="
+ "messages://open?recipient="
- "T@\"NSDate\",&,N,V_keyReleaseMessageSendDate"
- "sms://open?groupid="
- "sms://open?recipient="

```
