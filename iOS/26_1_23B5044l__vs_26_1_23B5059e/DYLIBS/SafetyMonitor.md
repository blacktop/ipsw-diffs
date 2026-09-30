## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-1067.0.2.0.0
-  __TEXT.__text: 0x73cac
+1069.0.1.0.0
+  __TEXT.__text: 0x7401c
   __TEXT.__auth_stubs: 0x1270
-  __TEXT.__objc_methlist: 0x4d64
-  __TEXT.__const: 0x1380
+  __TEXT.__objc_methlist: 0x4df4
+  __TEXT.__const: 0x1388
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__cstring: 0xbf90
+  __TEXT.__cstring: 0xc115
   __TEXT.__swift5_typeref: 0x4a2
-  __TEXT.__oslogstring: 0x448f
+  __TEXT.__oslogstring: 0x44cd
   __TEXT.__constg_swiftt: 0x450
   __TEXT.__swift5_reflstr: 0x2be
   __TEXT.__swift5_fieldmd: 0x3ec

   __TEXT.__swift5_protos: 0x4
   __TEXT.__ustring: 0xd34
   __TEXT.__gcc_except_tab: 0xf70
-  __TEXT.__unwind_info: 0x17f8
+  __TEXT.__unwind_info: 0x1820
   __TEXT.__eh_frame: 0x9dc
-  __TEXT.__objc_classname: 0x9e4
-  __TEXT.__objc_methname: 0xc621
-  __TEXT.__objc_methtype: 0x2166
-  __TEXT.__objc_stubs: 0x58e0
-  __DATA_CONST.__got: 0x4c8
-  __DATA_CONST.__const: 0x1478
-  __DATA_CONST.__objc_classlist: 0x268
+  __TEXT.__objc_classname: 0x9f3
+  __TEXT.__objc_methname: 0xc7dc
+  __TEXT.__objc_methtype: 0x2198
+  __TEXT.__objc_stubs: 0x59c0
+  __DATA_CONST.__got: 0x4d0
+  __DATA_CONST.__const: 0x14e0
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2290
+  __DATA_CONST.__objc_selrefs: 0x22e8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x1a8
+  __DATA_CONST.__objc_superrefs: 0x1b0
   __AUTH_CONST.__auth_got: 0x948
   __AUTH_CONST.__const: 0xa10
-  __AUTH_CONST.__cfstring: 0x4f40
-  __AUTH_CONST.__objc_const: 0x8290
+  __AUTH_CONST.__cfstring: 0x5100
+  __AUTH_CONST.__objc_const: 0x83c0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x11c0
+  __AUTH.__objc_data: 0x1210
   __AUTH.__data: 0x2d8
-  __DATA.__objc_ivar: 0x38c
+  __DATA.__objc_ivar: 0x398
   __DATA.__data: 0x1308
   __DATA.__bss: 0x1600
   __DATA.__common: 0x88

   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CEBFF489-0082-34A7-AC1F-09670B8E11D8
-  Functions: 2185
-  Symbols:   5694
-  CStrings:  4009
+  UUID: 62D8CC4D-1C52-3369-BBAE-C67BF46AEEE9
+  Functions: 2196
+  Symbols:   5748
+  CStrings:  4059
 
Symbols:
+ -[SMLikelyReceiverOptions firstResultOnly]
+ -[SMLikelyReceiverOptions initWithRequireEligibility:requireContact:requireNonBlockedContact:requireOnlyFavoritedHandles:requireOnlyPastSessionRecipients:firstResultOnly:]
+ -[SMTrialManager .cxx_destruct]
+ -[SMTrialManager doubleValueForFactor:]
+ -[SMTrialManager init]
+ -[SMTrialManager levelForFactor:]
+ -[SMTrialManager namespaceName]
+ -[SMTrialManager refresh]
+ -[SMTrialManager setNamespaceName:]
+ -[SMTrialManager setTrialClient:]
+ -[SMTrialManager trialClient]
+ _OBJC_CLASS_$_SMTrialManager
+ _OBJC_CLASS_$_TRIClient
+ _OBJC_IVAR_$_SMLikelyReceiverOptions._firstResultOnly
+ _OBJC_IVAR_$_SMTrialManager._namespaceName
+ _OBJC_IVAR_$_SMTrialManager._trialClient
+ _OBJC_METACLASS_$_SMTrialManager
+ _SMInitiatorEligibilityStatusKey
+ _SMReceiverEligibilityStatusKey
+ _SMStagingPerformanceAnalyticsEvent
+ _SMSuggestionConversionAnalyticsEvent
+ _SMSuggestionConversionPresentedKey
+ _SMSuggestionConversionSelectedKey
+ _SMSuggestionConversionStartedKey
+ _SMSuggestionConversionSupppressionReasonKey
+ _SMSuggestionConversionTriggerKey
+ _SMSuggestionConversionUserTypeKey
+ _SMTrialFactorSuggestionFirstTimeUserSuppressionEndTime
+ _SMTrialFactorSuggestionFirstTimeUserSuppressionStartTime
+ __OBJC_$_INSTANCE_METHODS_SMTrialManager
+ __OBJC_$_INSTANCE_VARIABLES_SMTrialManager
+ __OBJC_$_PROP_LIST_SMTrialManager
+ __OBJC_CLASS_RO_$_SMTrialManager
+ __OBJC_METACLASS_RO_$_SMTrialManager
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.331
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.333
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.332
+ ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.391
+ ___54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.396
+ ___55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.395
+ ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.409
+ ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.392
+ ___58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke.371
+ ___60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.393
+ ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.389
+ ___61-[SMSafetyMonitorManager cancelInitializationWithCompletion:]_block_invoke.358
+ ___61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.394
+ ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.390
+ ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.362
+ ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.375
+ ___65-[SMSafetyMonitorManager fetchCurrentSessionStateWithCompletion:]_block_invoke.376
+ ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.361
+ ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.373
+ ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.359
+ ___67-[SMSafetyMonitorManager endSessionForSessionID:reason:completion:]_block_invoke.360
+ ___67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.377
+ ___67-[SMSafetyMonitorManager startCheckInRemindersTipMetricsCollection]_block_invoke.427
+ ___67-[SMSafetyMonitorManager startSessionWithConfiguration:completion:]_block_invoke.363
+ ___68-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]_block_invoke.369
+ ___68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.381
+ ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.386
+ ___69-[SMSafetyMonitorManager respondedToCheckInRemindersTipWithResponse:]_block_invoke.423
+ ___69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.380
+ ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.398
+ ___70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.379
+ ___71-[SMSafetyMonitorManager initializeSessionWithConversation:completion:]_block_invoke.355
+ ___72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.384
+ ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.406
+ ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.412
+ ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.404
+ ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.366
+ ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.400
+ ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.408
+ ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.413
+ ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.372
+ ___76-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithOptions:handler:]_block_invoke.383
+ ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.399
+ ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.402
+ ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.403
+ ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.388
+ ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.364
+ ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.365
+ ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.414
+ ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.387
+ ___block_literal_global.368
+ ___block_literal_global.422
+ ___block_literal_global.426
+ ___block_literal_global.429
+ ___block_literal_global.516
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_SafetyMonitor
+ _objc_msgSend$client
+ _objc_msgSend$firstResultOnly
+ _objc_msgSend$initWithRequireEligibility:requireContact:requireNonBlockedContact:requireOnlyFavoritedHandles:requireOnlyPastSessionRecipients:firstResultOnly:
+ _objc_msgSend$levelForFactor:
+ _objc_msgSend$levelForFactor:withNamespaceName:
+ _objc_msgSend$namespaceName
+ _objc_msgSend$refresh
+ _objc_msgSend$trialClient
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.330
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.332
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.331
- ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.390
- ___54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.395
- ___55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.394
- ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.408
- ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.391
- ___58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke.370
- ___60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.392
- ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.388
- ___61-[SMSafetyMonitorManager cancelInitializationWithCompletion:]_block_invoke.357
- ___61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.393
- ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.389
- ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.361
- ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.374
- ___65-[SMSafetyMonitorManager fetchCurrentSessionStateWithCompletion:]_block_invoke.375
- ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.360
- ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.372
- ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.358
- ___67-[SMSafetyMonitorManager endSessionForSessionID:reason:completion:]_block_invoke.359
- ___67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.376
- ___67-[SMSafetyMonitorManager startCheckInRemindersTipMetricsCollection]_block_invoke.426
- ___67-[SMSafetyMonitorManager startSessionWithConfiguration:completion:]_block_invoke.362
- ___68-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]_block_invoke.368
- ___68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.380
- ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.385
- ___69-[SMSafetyMonitorManager respondedToCheckInRemindersTipWithResponse:]_block_invoke.422
- ___69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.379
- ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.397
- ___70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.378
- ___71-[SMSafetyMonitorManager initializeSessionWithConversation:completion:]_block_invoke.354
- ___72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.383
- ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.405
- ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.411
- ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.403
- ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.365
- ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.399
- ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.407
- ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.412
- ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.371
- ___76-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithOptions:handler:]_block_invoke.382
- ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.398
- ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.401
- ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.402
- ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.387
- ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.363
- ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.364
- ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.413
- ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.386
- ___block_literal_global.367
- ___block_literal_global.421
- ___block_literal_global.425
- ___block_literal_global.428
- ___block_literal_global.515
- _objc_msgSend$initWithRequireEligibility:requireContact:requireNonBlockedContact:requireOnlyFavoritedHandles:requireOnlyPastSessionRecipients:
CStrings:
+ "%{public}@, %{public}@, factor, %{public}@, level, %{public}@"
+ "@\"TRIClient\""
+ "@40@0:8B16B20B24B28B32B36"
+ "LOMO_CHECK_IN"
+ "SMInitiatorEligibilityStatusKey"
+ "SMReceiverEligibilityStatusKey"
+ "SMTrialManager"
+ "T@\"NSString\",&,N,V_namespaceName"
+ "T@\"TRIClient\",&,N,V_trialClient"
+ "TB,R,N,V_firstResultOnly"
+ "_firstResultOnly"
+ "_namespaceName"
+ "_trialClient"
+ "com.apple.SafetyMonitor.initiator.StagingPerformance"
+ "com.apple.SafetyMonitor.proactiveNotifications.SuggestionConversion"
+ "d24@0:8@16"
+ "doubleValueForFactor:"
+ "firstResultOnly"
+ "initWithRequireEligibility:requireContact:requireNonBlockedContact:requireOnlyFavoritedHandles:requireOnlyPastSessionRecipients:firstResultOnly:"
+ "levelForFactor:"
+ "levelForFactor:withNamespaceName:"
+ "namespaceName"
+ "refresh"
+ "sessionStarted"
+ "setNamespaceName:"
+ "setTrialClient:"
+ "suggestionFirstTimeUserSuppressionEndTime"
+ "suggestionFirstTimeUserSuppressionStartTime"
+ "suggestionPresented"
+ "suggestionSelected"
+ "trialClient"
+ "trigger"
+ "userType"

```
