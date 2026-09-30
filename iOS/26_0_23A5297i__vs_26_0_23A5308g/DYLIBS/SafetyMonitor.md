## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-1057.0.0.0.0
-  __TEXT.__text: 0x72538
+1061.0.0.0.0
+  __TEXT.__text: 0x72bac
   __TEXT.__auth_stubs: 0x1250
-  __TEXT.__objc_methlist: 0x4ce4
+  __TEXT.__objc_methlist: 0x4d54
   __TEXT.__const: 0x1380
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__cstring: 0xbd41
+  __TEXT.__cstring: 0xbf20
   __TEXT.__swift5_typeref: 0x4a2
   __TEXT.__oslogstring: 0x4345
   __TEXT.__constg_swiftt: 0x450

   __TEXT.__swift5_protos: 0x4
   __TEXT.__ustring: 0xd34
   __TEXT.__gcc_except_tab: 0xf70
-  __TEXT.__unwind_info: 0x17d8
+  __TEXT.__unwind_info: 0x17f0
   __TEXT.__eh_frame: 0x9dc
-  __TEXT.__objc_classname: 0x9c9
-  __TEXT.__objc_methname: 0xc447
-  __TEXT.__objc_methtype: 0x2155
-  __TEXT.__objc_stubs: 0x57e0
+  __TEXT.__objc_classname: 0x9e4
+  __TEXT.__objc_methname: 0xc60c
+  __TEXT.__objc_methtype: 0x2166
+  __TEXT.__objc_stubs: 0x5860
   __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x1440
+  __DATA_CONST.__const: 0x1480
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x118
+  __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2258
+  __DATA_CONST.__objc_selrefs: 0x2288
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1a8
   __AUTH_CONST.__auth_got: 0x938
-  __AUTH_CONST.__const: 0x9b0
-  __AUTH_CONST.__cfstring: 0x4ea0
-  __AUTH_CONST.__objc_const: 0x81e0
+  __AUTH_CONST.__const: 0xa10
+  __AUTH_CONST.__cfstring: 0x4f00
+  __AUTH_CONST.__objc_const: 0x8290
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x11c0
   __AUTH.__data: 0x2d8
-  __DATA.__objc_ivar: 0x380
-  __DATA.__data: 0x12a8
+  __DATA.__objc_ivar: 0x38c
+  __DATA.__data: 0x1308
   __DATA.__bss: 0x1600
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_ivar: 0x1d4

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3AD67FDB-A741-35A7-A707-A9D84F4AF584
-  Functions: 2173
-  Symbols:   5650
-  CStrings:  3975
+  UUID: E83DBBE8-F760-3812-92BE-CA60296A9614
+  Functions: 2184
+  Symbols:   5688
+  CStrings:  3997
 
Symbols:
+ -[SMCurrentWorkoutSnapshot initWithSessionIdentifier:activityType:sessionType:isWorkoutOngoing:isFirstPartyWorkout:]
+ -[SMCurrentWorkoutSnapshot sessionType]
+ -[SMSafetyMonitorManager respondedToCheckInRemindersTipWithResponse:]
+ -[SMSafetyMonitorManager startCheckInRemindersTipMetricsCollection]
+ -[SMSessionConfiguration initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:]
+ -[SMSessionConfiguration initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:]
+ -[SMSessionConfiguration sessionWorkoutIdentifier]
+ -[SMSessionConfiguration sessionWorkoutMirrorType]
+ -[SMSessionConfiguration setSessionWorkoutIdentifier:]
+ -[SMSessionConfiguration setSessionWorkoutMirrorType:]
+ _OBJC_IVAR_$_SMCurrentWorkoutSnapshot._sessionType
+ _OBJC_IVAR_$_SMSessionConfiguration._sessionWorkoutIdentifier
+ _OBJC_IVAR_$_SMSessionConfiguration._sessionWorkoutMirrorType
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SMInitiatorMetricsProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SMInitiatorMetricsProtocol
+ __OBJC_LABEL_PROTOCOL_$_SMInitiatorMetricsProtocol
+ __OBJC_PROTOCOL_$_SMInitiatorMetricsProtocol
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.330
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.332
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.331
+ ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.390
+ ___54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.395
+ ___55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.394
+ ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.408
+ ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.391
+ ___58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke.370
+ ___60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.392
+ ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.388
+ ___61-[SMSafetyMonitorManager cancelInitializationWithCompletion:]_block_invoke.357
+ ___61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.393
+ ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.389
+ ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.361
+ ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.374
+ ___65-[SMSafetyMonitorManager fetchCurrentSessionStateWithCompletion:]_block_invoke.375
+ ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.360
+ ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.372
+ ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.358
+ ___67-[SMSafetyMonitorManager endSessionForSessionID:reason:completion:]_block_invoke.359
+ ___67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.376
+ ___67-[SMSafetyMonitorManager startCheckInRemindersTipMetricsCollection]_block_invoke
+ ___67-[SMSafetyMonitorManager startCheckInRemindersTipMetricsCollection]_block_invoke.426
+ ___67-[SMSafetyMonitorManager startSessionWithConfiguration:completion:]_block_invoke.362
+ ___68-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]_block_invoke.368
+ ___68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.380
+ ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.385
+ ___69-[SMSafetyMonitorManager respondedToCheckInRemindersTipWithResponse:]_block_invoke
+ ___69-[SMSafetyMonitorManager respondedToCheckInRemindersTipWithResponse:]_block_invoke.422
+ ___69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.379
+ ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.397
+ ___70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.378
+ ___71-[SMSafetyMonitorManager initializeSessionWithConversation:completion:]_block_invoke.354
+ ___72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.383
+ ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.405
+ ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.411
+ ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.403
+ ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.365
+ ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.399
+ ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.407
+ ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.412
+ ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.371
+ ___76-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithOptions:handler:]_block_invoke.382
+ ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.398
+ ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.401
+ ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.402
+ ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.387
+ ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.363
+ ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.364
+ ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.413
+ ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.386
+ ___block_descriptor_32_e8_v16?08l
+ ___block_descriptor_40_e8_v16?08l
+ ___block_literal_global.330
+ ___block_literal_global.334
+ ___block_literal_global.367
+ ___block_literal_global.421
+ ___block_literal_global.425
+ ___block_literal_global.428
+ ___block_literal_global.515
+ _objc_msgSend$initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:
+ _objc_msgSend$initWithSessionIdentifier:activityType:sessionType:isWorkoutOngoing:isFirstPartyWorkout:
+ _objc_msgSend$initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:
+ _objc_msgSend$respondedToCheckInRemindersTipWithResponse:
+ _objc_msgSend$sessionWorkoutIdentifier
+ _objc_msgSend$sessionWorkoutMirrorType
+ _objc_msgSend$startCheckInRemindersTipMetricsCollection
- -[SMCurrentWorkoutSnapshot initWithSessionIdentifier:activityType:isWorkoutOngoing:isFirstPartyWorkout:]
- -[SMSessionConfiguration initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:]
- -[SMSessionConfiguration initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:]
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.326
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.328
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.327
- ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.386
- ___54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.391
- ___55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.390
- ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.404
- ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.387
- ___58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke.366
- ___60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.388
- ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.384
- ___61-[SMSafetyMonitorManager cancelInitializationWithCompletion:]_block_invoke.353
- ___61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.389
- ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.385
- ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.357
- ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.370
- ___65-[SMSafetyMonitorManager fetchCurrentSessionStateWithCompletion:]_block_invoke.371
- ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.356
- ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.368
- ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.354
- ___67-[SMSafetyMonitorManager endSessionForSessionID:reason:completion:]_block_invoke.355
- ___67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.372
- ___67-[SMSafetyMonitorManager startSessionWithConfiguration:completion:]_block_invoke.358
- ___68-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]_block_invoke.364
- ___68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.376
- ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.381
- ___69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.375
- ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.393
- ___70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.374
- ___71-[SMSafetyMonitorManager initializeSessionWithConversation:completion:]_block_invoke.350
- ___72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.379
- ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.401
- ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.407
- ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.399
- ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.361
- ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.395
- ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.403
- ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.408
- ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.367
- ___76-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithOptions:handler:]_block_invoke.378
- ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.394
- ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.397
- ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.398
- ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.383
- ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.359
- ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.360
- ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.409
- ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.382
- ___block_literal_global.327
- ___block_literal_global.331
- ___block_literal_global.363
- ___block_literal_global.502
- _objc_msgSend$initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:
- _objc_msgSend$initWithSessionIdentifier:activityType:isWorkoutOngoing:isFirstPartyWorkout:
- _objc_msgSend$initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:
CStrings:
+ "-[SMSafetyMonitorManager respondedToCheckInRemindersTipWithResponse:]"
+ "-[SMSafetyMonitorManager respondedToCheckInRemindersTipWithResponse:]_block_invoke"
+ "-[SMSafetyMonitorManager startCheckInRemindersTipMetricsCollection]"
+ "-[SMSafetyMonitorManager startCheckInRemindersTipMetricsCollection]_block_invoke"
+ "@108@0:8@16@24@32Q40@48@56@64B72@76@84Q92q100"
+ "@48@0:8@16Q24q32B40B44"
+ "@76@0:8@16@24@32B40@44@52Q60q68"
+ "SMInitiatorMetricsProtocol"
+ "T@\"NSUUID\",&,N,V_sessionWorkoutIdentifier"
+ "Tq,N,V_sessionWorkoutMirrorType"
+ "Tq,R,N,V_sessionType"
+ "__kSMSessionConfigurationSessionWorkoutIDKey"
+ "__kSMSessionConfigurationSessionWorkoutMirrorTypeKey"
+ "__kSMWorkoutSessionTypeKey"
+ "_sessionWorkoutIdentifier"
+ "_sessionWorkoutMirrorType"
+ "initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:"
+ "initWithSessionIdentifier:activityType:sessionType:isWorkoutOngoing:isFirstPartyWorkout:"
+ "initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:"
+ "respondedToCheckInRemindersTipWithResponse:"
+ "sessionWorkoutIdentifier"
+ "sessionWorkoutMirrorType"
+ "setSessionWorkoutIdentifier:"
+ "setSessionWorkoutMirrorType:"
+ "startCheckInRemindersTipMetricsCollection"
+ "{ReceiverHandles:%@, GroupID:%@, SessionID:%@, SessionStartDate:%@, SessionType:%@, Time:%@, Destination:%@ , userResponseSafeDate:%@, SessionSupportsHandoff:%d, SOSReceivers:%@, SessionWorkoutID:%@, SessionWorkoutType:%lu, SessionWorkoutMirrorType:%ld}"
- "@40@0:8@16Q24B32B36"
- "@60@0:8@16@24@32B40@44Q52"
- "@92@0:8@16@24@32Q40@48@56@64B72@76Q84"
- "initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:"
- "initWithSessionIdentifier:activityType:isWorkoutOngoing:isFirstPartyWorkout:"
- "initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:"
- "{ReceiverHandles:%@, GroupID:%@, SessionID:%@, SessionStartDate:%@, SessionType:%@, Time:%@, Destination:%@ , userResponseSafeDate:%@, SessionSupportsHandoff:%d,SOSReceivers:%@, SessionWorkoutType:%lu}"

```
