## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/SafetyMonitor`

```diff

-990.0.10.0.0
-  __TEXT.__text: 0x73308
-  __TEXT.__auth_stubs: 0x12a0
-  __TEXT.__objc_methlist: 0x4c7c
-  __TEXT.__const: 0x1278
+1044.0.2.0.0
+  __TEXT.__text: 0x71d10
+  __TEXT.__auth_stubs: 0x1240
+  __TEXT.__objc_methlist: 0x4cc4
+  __TEXT.__const: 0x1378
   __TEXT.__dlopen_cstrs: 0x60
-  __TEXT.__cstring: 0xb87b
+  __TEXT.__cstring: 0xbcf5
   __TEXT.__swift5_typeref: 0x4a2
-  __TEXT.__oslogstring: 0x4361
+  __TEXT.__oslogstring: 0x4345
   __TEXT.__constg_swiftt: 0x450
   __TEXT.__swift5_reflstr: 0x2be
   __TEXT.__swift5_fieldmd: 0x3ec

   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift5_protos: 0x4
   __TEXT.__ustring: 0xd34
-  __TEXT.__gcc_except_tab: 0xf64
-  __TEXT.__unwind_info: 0x17c0
-  __TEXT.__eh_frame: 0x95c
+  __TEXT.__gcc_except_tab: 0xf58
+  __TEXT.__unwind_info: 0x17a8
+  __TEXT.__eh_frame: 0x98c
   __TEXT.__objc_classname: 0x9c9
-  __TEXT.__objc_methname: 0xc364
+  __TEXT.__objc_methname: 0xc41f
   __TEXT.__objc_methtype: 0x2155
   __TEXT.__objc_stubs: 0x57c0
   __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0x1468
+  __DATA_CONST.__const: 0x1478
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2220
+  __DATA_CONST.__objc_selrefs: 0x2250
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1a8
-  __AUTH_CONST.__auth_got: 0x960
-  __AUTH_CONST.__const: 0x938
-  __AUTH_CONST.__cfstring: 0x4e40
-  __AUTH_CONST.__objc_const: 0x81a0
+  __AUTH_CONST.__auth_got: 0x930
+  __AUTH_CONST.__const: 0x960
+  __AUTH_CONST.__cfstring: 0x4ea0
+  __AUTH_CONST.__objc_const: 0x81d8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x11c0
   __AUTH.__data: 0x2d8
   __DATA.__objc_ivar: 0x380
-  __DATA.__data: 0x1398
-  __DATA.__bss: 0x1610
+  __DATA.__data: 0x12a8
+  __DATA.__bss: 0x1600
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_ivar: 0x1d4
   __DATA_DIRTY.__objc_data: 0x9c8
-  __DATA_DIRTY.__data: 0x108
-  __DATA_DIRTY.__bss: 0x420
+  __DATA_DIRTY.__data: 0x100
+  __DATA_DIRTY.__bss: 0x430
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/CloudKitCode.framework/CloudKitCode
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 6A3421F6-9589-3F0E-BE5A-5104424CAFED
-  Functions: 2155
+  UUID: 523A5CD4-27A1-353F-BD7E-7366E596A53B
+  Functions: 2163
   Symbols:   5655
-  CStrings:  3946
+  CStrings:  3973
 
Symbols:
+ +[SMMobileSMSPreferencesUtilities alwaysOnPromptCount]
+ +[SMMobileSMSPreferencesUtilities checkInRemindersPreviouslyEnabled]
+ +[SMMobileSMSPreferencesUtilities setAlwaysOnPromptCount:]
+ +[SMMobileSMSPreferencesUtilities setCheckInRemindersPreviouslyEnabled:]
+ +[SMMobileSMSPreferencesUtilities showCheckInRemindersTip]
+ -[SMSafetyMonitorManager cancelInitializationWithCompletion:]
+ -[SMSafetyMonitorManager endSessionForSessionID:reason:completion:]
+ -[SMSafetyMonitorManager fetchCurrentSessionStateWithCompletion:]
+ -[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]
+ -[SMSafetyMonitorManager fetchQuickReplySuggestionURLWithCompletion:]
+ -[SMSafetyMonitorManager initializeSessionWithConversation:completion:]
+ -[SMSafetyMonitorManager startSessionWithConfiguration:completion:]
+ GCC_except_table102
+ GCC_except_table112
+ GCC_except_table121
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table134
+ GCC_except_table194
+ GCC_except_table198
+ GCC_except_table211
+ GCC_except_table82
+ _SMAlwaysOnPromptMaxCount
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.326
+ ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.325
+ ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.384
+ ___54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.389
+ ___55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.388
+ ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.402
+ ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.385
+ ___58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke.364
+ ___60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.386
+ ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.382
+ ___61-[SMSafetyMonitorManager cancelInitializationWithCompletion:]_block_invoke
+ ___61-[SMSafetyMonitorManager cancelInitializationWithCompletion:]_block_invoke.351
+ ___61-[SMSafetyMonitorManager cancelInitializationWithCompletion:]_block_invoke_2
+ ___61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.387
+ ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.383
+ ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.355
+ ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.368
+ ___65-[SMSafetyMonitorManager fetchCurrentSessionStateWithCompletion:]_block_invoke
+ ___65-[SMSafetyMonitorManager fetchCurrentSessionStateWithCompletion:]_block_invoke.369
+ ___65-[SMSafetyMonitorManager fetchCurrentSessionStateWithCompletion:]_block_invoke_2
+ ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.354
+ ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.366
+ ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.352
+ ___67-[SMSafetyMonitorManager endSessionForSessionID:reason:completion:]_block_invoke
+ ___67-[SMSafetyMonitorManager endSessionForSessionID:reason:completion:]_block_invoke.353
+ ___67-[SMSafetyMonitorManager endSessionForSessionID:reason:completion:]_block_invoke_2
+ ___67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.370
+ ___67-[SMSafetyMonitorManager startSessionWithConfiguration:completion:]_block_invoke
+ ___67-[SMSafetyMonitorManager startSessionWithConfiguration:completion:]_block_invoke.356
+ ___67-[SMSafetyMonitorManager startSessionWithConfiguration:completion:]_block_invoke_2
+ ___68-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]_block_invoke
+ ___68-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]_block_invoke.362
+ ___68-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]_block_invoke_2
+ ___68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.374
+ ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.379
+ ___69-[SMSafetyMonitorManager fetchQuickReplySuggestionURLWithCompletion:]_block_invoke
+ ___69-[SMSafetyMonitorManager fetchQuickReplySuggestionURLWithCompletion:]_block_invoke_2
+ ___69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.373
+ ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.391
+ ___70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.372
+ ___71-[SMSafetyMonitorManager initializeSessionWithConversation:completion:]_block_invoke
+ ___71-[SMSafetyMonitorManager initializeSessionWithConversation:completion:]_block_invoke.348
+ ___71-[SMSafetyMonitorManager initializeSessionWithConversation:completion:]_block_invoke_2
+ ___72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.377
+ ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.399
+ ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.405
+ ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.397
+ ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.359
+ ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.393
+ ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.401
+ ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.406
+ ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.365
+ ___76-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithOptions:handler:]_block_invoke.376
+ ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.392
+ ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.395
+ ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.396
+ ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.381
+ ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.357
+ ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.358
+ ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.407
+ ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.380
+ ___block_literal_global.327
+ ___block_literal_global.331
+ ___block_literal_global.361
+ ___block_literal_global.500
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_SafetyMonitor
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_SafetyMonitor
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_SafetyMonitor
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_SafetyMonitor
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_SafetyMonitor
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_SafetyMonitor
+ _objc_msgSend$cancelInitializationWithCompletion:
+ _objc_msgSend$endSessionForSessionID:reason:completion:
+ _objc_msgSend$fetchCurrentSessionStateWithCompletion:
+ _objc_msgSend$fetchCurrentWorkoutSnapshotWithCompletion:
+ _objc_msgSend$fetchQuickReplySuggestionURLWithCompletion:
+ _objc_msgSend$initializeSessionWithConversation:completion:
+ _objc_msgSend$startSessionWithConfiguration:completion:
+ _symbolic _____y___________pG s6ResultOsRi_zRi0_zrlE 13SafetyMonitor05FetchB13CacheResponseV s5ErrorP
- -[SMSafetyMonitorManager cancelInitializationWithHandler:]
- -[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]
- -[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithHandler:]
- -[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]
- -[SMSafetyMonitorManager initializeSessionWithConversation:handler:]
- -[SMSafetyMonitorManager startSessionWithConfiguration:handler:]
- GCC_except_table106
- GCC_except_table120
- GCC_except_table124
- GCC_except_table129
- GCC_except_table133
- GCC_except_table137
- GCC_except_table197
- GCC_except_table201
- GCC_except_table214
- GCC_except_table78
- GCC_except_table86
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke.322
- ___43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.323
- ___45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.383
- ___54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.388
- ___55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.387
- ___56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.401
- ___57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.384
- ___58-[SMSafetyMonitorManager cancelInitializationWithHandler:]_block_invoke
- ___58-[SMSafetyMonitorManager cancelInitializationWithHandler:]_block_invoke.349
- ___58-[SMSafetyMonitorManager cancelInitializationWithHandler:]_block_invoke_2
- ___58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke.363
- ___60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.385
- ___60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.381
- ___61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.386
- ___61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.382
- ___62-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]_block_invoke
- ___62-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]_block_invoke.368
- ___62-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]_block_invoke_2
- ___62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.353
- ___64-[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]_block_invoke
- ___64-[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]_block_invoke.351
- ___64-[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]_block_invoke_2
- ___64-[SMSafetyMonitorManager startSessionWithConfiguration:handler:]_block_invoke
- ___64-[SMSafetyMonitorManager startSessionWithConfiguration:handler:]_block_invoke.354
- ___64-[SMSafetyMonitorManager startSessionWithConfiguration:handler:]_block_invoke_2
- ___64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.367
- ___65-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithHandler:]_block_invoke
- ___65-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithHandler:]_block_invoke.361
- ___65-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithHandler:]_block_invoke_2
- ___65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.352
- ___65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.365
- ___67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.350
- ___67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.369
- ___68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.373
- ___68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.378
- ___68-[SMSafetyMonitorManager initializeSessionWithConversation:handler:]_block_invoke
- ___68-[SMSafetyMonitorManager initializeSessionWithConversation:handler:]_block_invoke.346
- ___68-[SMSafetyMonitorManager initializeSessionWithConversation:handler:]_block_invoke_2
- ___69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.372
- ___70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.390
- ___70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.371
- ___72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.376
- ___72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.398
- ___74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.404
- ___74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.396
- ___74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.358
- ___74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.392
- ___74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.400
- ___75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.405
- ___75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.364
- ___76-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithOptions:handler:]_block_invoke.375
- ___76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.391
- ___76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.394
- ___76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.395
- ___77-[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]_block_invoke
- ___77-[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]_block_invoke.355
- ___77-[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]_block_invoke_2
- ___78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.380
- ___78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.356
- ___82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.357
- ___83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.406
- ___86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.379
- ___block_literal_global.30
- ___block_literal_global.34
- ___block_literal_global.360
- ___block_literal_global.499
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_SafetyMonitor
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_SafetyMonitor
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_SafetyMonitor
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_SafetyMonitor
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_SafetyMonitor
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_SafetyMonitor
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_SafetyMonitor
- _malloc
- _objc_msgSend$cancelInitializationWithHandler:
- _objc_msgSend$endSessionForSessionID:reason:handler:
- _objc_msgSend$fetchCurrentSessionStateWithHandler:
- _objc_msgSend$fetchCurrentWorkoutSnapshotWithHandler:
- _objc_msgSend$initializeAndStartSessionWithConfiguration:handler:
- _objc_msgSend$initializeSessionWithConversation:handler:
- _objc_msgSend$startSessionWithConfiguration:handler:
- _objc_retain_x9
- _swift_bridgeObjectRelease_n
- _swift_bridgeObjectRetain_n
- _swift_release_n
- _swift_retain_n
- _symbolic _____y___________pG s6ResultOsRi_zrlE 13SafetyMonitor05FetchB13CacheResponseV s5ErrorP
CStrings:
+ "-[SMSafetyMonitorManager fetchCurrentSessionStateWithCompletion:]"
+ "-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]"
+ "-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithCompletion:]_block_invoke"
+ "LIVE_ACTIVITY_DESTINATION_SUBTITLE_STANDARD_FALLBACK_GROUP_NO_NAME"
+ "LIVE_ACTIVITY_DESTINATION_SUBTITLE_STANDARD_FALLBACK_INDIVIDUAL"
+ "LIVE_ACTIVITY_DESTINATION_SUBTITLE_STANDARD_GROUP_FALLBACK_NO_NAME"
+ "LIVE_ACTIVITY_DESTINATION_SUBTITLE_STANDARD_INDIVIDUAL_FALLBACK"
+ "LIVE_ACTIVITY_ETA_SUBTITLE_STANDARD_GROUP_NO_NAME"
+ "LIVE_ACTIVITY_ETA_SUBTITLE_STANDARD_INDIVIDUAL"
+ "LIVE_ACTIVITY_PRERELEASE_PROMPT_SUBTITLE_GROUP_NO_NAME"
+ "LIVE_ACTIVITY_PRERELEASE_PROMPT_SUBTITLE_INDIVIDUAL"
+ "LIVE_ACTIVITY_PRERELEASE_PROMPT_SUBTITLE_WATCH_GROUP_NO_NAME"
+ "LIVE_ACTIVITY_PRERELEASE_PROMPT_SUBTITLE_WATCH_INDIVIDUAL"
+ "LIVE_ACTIVITY_PROMPT_SUBTITLE_STANDARD_GROUP_NO_NAME"
+ "LIVE_ACTIVITY_PROMPT_SUBTITLE_STANDARD_INDIVIDUAL"
+ "LIVE_ACTIVITY_PROMPT_SUBTITLE_WATCH_GROUP_NO_NAME"
+ "LIVE_ACTIVITY_PROMPT_SUBTITLE_WATCH_INDIVIDUAL"
+ "LIVE_ACTIVITY_WORKOUT_SUBTITLE_STANDARD_GROUP_NO_NAME"
+ "LIVE_ACTIVITY_WORKOUT_SUBTITLE_STANDARD_INDIVIDUAL"
+ "SMTriggerCategoryWorkoutAutoPauseTimeout"
+ "SafetyMonitorAlwaysOnPreviouslyEnabled"
+ "SafetyMonitorAlwaysOnPromptCount"
+ "alwaysOnPromptCount"
+ "cancelInitializationWithCompletion:"
+ "checkInRemindersPreviouslyEnabled"
+ "endSessionForSessionID:reason:completion:"
+ "fetchCurrentSessionStateWithCompletion:"
+ "fetchCurrentWorkoutSnapshotWithCompletion:"
+ "fetchQuickReplySuggestionURLWithCompletion:"
+ "initializeSessionWithConversation:completion:"
+ "setAlwaysOnPromptCount:"
+ "setCheckInRemindersPreviouslyEnabled:"
+ "showCheckInRemindersTip"
+ "startSessionWithConfiguration:completion:"
- "-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]"
- "-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithHandler:]"
- "-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithHandler:]_block_invoke"
- "SMInitializeAndStartSession"
- "cancelInitializationWithHandler:"
- "endSessionForSessionID:reason:handler:"
- "fetchCurrentWorkoutSnapshotWithHandler:"
- "initializeAndStartSessionWithConfiguration:handler:"
- "initializeSessionWithConversation:handler:"
- "startSessionWithConfiguration:handler:"

```
