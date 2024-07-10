## SafetyMonitor

> `/System/Library/PrivateFrameworks/SafetyMonitor.framework/Versions/A/SafetyMonitor`

```diff

-953.0.0.0.0
-  __TEXT.__text: 0x788d8
-  __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0x3f88
-  __TEXT.__const: 0xe28
-  __TEXT.__cstring: 0xb1b7
+956.0.0.0.0
+  __TEXT.__text: 0x79c40
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_methlist: 0x4038
+  __TEXT.__const: 0xe30
+  __TEXT.__cstring: 0xb407
   __TEXT.__swift5_typeref: 0x3de
   __TEXT.__constg_swiftt: 0x348
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x27e
+  __TEXT.__swift5_reflstr: 0x28e
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x90
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__oslogstring: 0x404f
-  __TEXT.__swift5_fieldmd: 0x378
+  __TEXT.__oslogstring: 0x4095
+  __TEXT.__swift5_fieldmd: 0x390
   __TEXT.__swift5_capture: 0x1b8
   __TEXT.__swift5_protos: 0x4
   __TEXT.__ustring: 0xa8a
-  __TEXT.__gcc_except_tab: 0xedc
-  __TEXT.__unwind_info: 0x1680
+  __TEXT.__gcc_except_tab: 0xf00
+  __TEXT.__dlopen_cstrs: 0x60
+  __TEXT.__unwind_info: 0x16c0
   __TEXT.__eh_frame: 0x750
-  __TEXT.__objc_classname: 0x988
-  __TEXT.__objc_methname: 0xb60f
-  __TEXT.__objc_methtype: 0x20bd
-  __TEXT.__objc_stubs: 0x51e0
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__const: 0x810
-  __DATA_CONST.__objc_classlist: 0x250
+  __TEXT.__objc_classname: 0x99d
+  __TEXT.__objc_methname: 0xb9da
+  __TEXT.__objc_methtype: 0x20dc
+  __TEXT.__objc_stubs: 0x5320
+  __DATA_CONST.__got: 0x480
+  __DATA_CONST.__const: 0x868
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1de8
+  __DATA_CONST.__objc_selrefs: 0x1e60
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1a0
-  __AUTH_CONST.__auth_got: 0x760
+  __AUTH_CONST.__auth_got: 0x780
   __AUTH_CONST.__auth_ptr: 0x210
-  __AUTH_CONST.__const: 0x1768
-  __AUTH_CONST.__cfstring: 0x4980
-  __AUTH_CONST.__objc_const: 0x8d60
+  __AUTH_CONST.__const: 0x17b0
+  __AUTH_CONST.__cfstring: 0x4a40
+  __AUTH_CONST.__objc_const: 0x8f00
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x19f8
+  __AUTH.__objc_data: 0x1a48
   __AUTH.__data: 0x2e0
-  __DATA.__objc_ivar: 0x540
-  __DATA.__data: 0x1068
-  __DATA.__bss: 0x1210
-  __DATA.__common: 0x298
+  __DATA.__objc_ivar: 0x554
+  __DATA.__data: 0x1088
+  __DATA.__bss: 0x1220
+  __DATA.__common: 0x2a8
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2106
-  Symbols:   3808
-  CStrings:  957
+  Functions: 2131
+  Symbols:   3861
+  CStrings:  969
 
Symbols:
+ +[SMHandleFormatting canonicalIDSAddressForAddress:]
+ -[SMDeviceConfigurationChecker isEffectivePairedDeviceNearby]
+ -[SMHandle canonicalizedHandle]
+ -[SMInitiatorContact earliestActiveDeviceIdentifier]
+ -[SMInitiatorContact initWithIdentifier:conversation:shouldBeCleanedUpDate:cloudkitShareZoneCleanedUpSuccessfully:syncDate:keyReleaseMessageSendDate:scheduledSendExpiryDate:phoneCache:watchCache:sessionID:safetyCacheKey:allowReadToken:scheduleSendMessageGUID:unlockLocation:lockLocation:startingLocation:offWristLocation:parkedCarLocation:destinationMapItem:timeCacheUploadCompletion:maxCacheSize:maxLocationsInTrace:maxTimeBetweenCacheUpdates:numCacheUpdates:timeTilCacheRelease:numberOfSuccessfulCacheUpdates:numberOfMessageCancelling:numberOfSuccessfulMessageCancelling:numberOfMessageScheduling:numberOfSuccessfulMessageScheduling:wasCacheReleased:wasScheduledSendTriggered:locationOfTrigger:triggerDate:lockState:cacheUpdateBackstopExpiryDate:workoutEvents:numberOfHandoffBecomingActive:numberOfHandoffBecomingNonActive:earliestActiveDeviceIdentifier:latestActiveDeviceIdentifier:]
+ -[SMInitiatorContact latestActiveDeviceIdentifier]
+ -[SMInitiatorContact numberOfHandoffBecomingActive]
+ -[SMInitiatorContact numberOfHandoffBecomingNonActive]
+ -[SMInitiatorContact setEarliestActiveDeviceIdentifier:]
+ -[SMInitiatorContact setLatestActiveDeviceIdentifier:]
+ -[SMInitiatorContact setNumberOfHandoffBecomingActive:]
+ -[SMInitiatorContact setNumberOfHandoffBecomingNonActive:]
+ -[SMLocation hash]
+ -[SMLocation isEquivalent:]
+ -[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]
+ -[SMSessionConfiguration initDestinationBoundSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:]
+ -[SMSessionConfiguration initRoundTripSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:]
+ -[SMSessionConfiguration initTimeBoundSessionConfigurationWithConversation:sessionID:time:sessionStartDate:sessionSupportsHandoff:sosReceivers:]
+ -[SMSessionConfiguration initTimeBoundSessionConfigurationWithConversation:sessionID:time:sessionSupportsHandoff:sosReceivers:]
+ -[SMSessionConfiguration initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:]
+ -[SMSessionConfiguration initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:]
+ -[SMSessionConfiguration sosReceivers]
+ GCC_except_table121
+ GCC_except_table125
+ GCC_except_table129
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table142
+ GCC_except_table202
+ GCC_except_table206
+ GCC_except_table299
+ GCC_except_table303
+ GCC_except_table308
+ GCC_except_table312
+ GCC_except_table316
+ GCC_except_table320
+ GCC_except_table350
+ IMSharedUtilitiesLibraryCore.frameworkLibrary
+ OBJC_IVAR_$_SMSessionConfiguration._sosReceivers
+ _IMSharedUtilitiesLibraryCore
+ _OBJC_CLASS_$_SMHandleFormatting
+ _OBJC_METACLASS_$_SMHandleFormatting
+ _SMExitAndArrivalMetricsDestinationWasReachedKey
+ _SMExitAndArrivalMetricsTimeToExitOriginLOIKey
+ _SMExitAndArrivalMetricsTimeToMove250MetersKey
+ _SMExitAndArrivalMetricsTrueDurationRelativeToETAKey
+ _SMExitAndArrivalMetricsWasActiveAtEndKey
+ _SMExitAndArrivalMetricsWasActiveAtStartKey
+ _SMSessionManagerHandoffActiveSessionDetailsFetchTimeout
+ _SMSuggestionsWorkoutAlwaysPromptCategory
+ _SMWorkoutAlwaysPromptDismissActionIdentifier
+ __43-[SMSafetyMonitorManager _createConnection]_block_invoke.319
+ __43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.318
+ __45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.424
+ __54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.429
+ __55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.428
+ __56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.456
+ __57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.425
+ __58-[SMSafetyMonitorManager cancelInitializationWithHandler:]_block_invoke.346
+ __58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke.373
+ __60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.426
+ __60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.420
+ __61-[SMSafetyMonitorManager handoffSessionForSessionID:handler:]_block_invoke.354
+ __61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.427
+ __61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.423
+ __62-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]_block_invoke.385
+ __62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.358
+ __64-[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]_block_invoke.350
+ __64-[SMSafetyMonitorManager startSessionWithConfiguration:handler:]_block_invoke.359
+ __64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.384
+ __65-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithHandler:]_block_invoke.369
+ __65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.357
+ __65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.380
+ __67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.349
+ __67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.388
+ __68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.402
+ __68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.414
+ __68-[SMSafetyMonitorManager initializeSessionWithConversation:handler:]_block_invoke.343
+ __69-[SMSafetyMonitorManager fetchSessionReceiptForSessionID:completion:]_block_invoke.430
+ __69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.395
+ __70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.437
+ __70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.392
+ __72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.406
+ __72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.451
+ __73-[SMSafetyMonitorManager startMonitoringInitiatorSafetyCacheWithHandler:]_block_invoke.433
+ __74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.463
+ __74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.447
+ __74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.363
+ __74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.439
+ __74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.455
+ __75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.464
+ __75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.377
+ __76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.438
+ __76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.443
+ __76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.446
+ __77-[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]_block_invoke.360
+ __78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.418
+ __78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.361
+ __82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.362
+ __83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.465
+ __86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.417
+ __91-[SMSafetyMonitorManager prepareUserInfoForNotificationContent:initiatorHandle:messageUrl:]_block_invoke.472
+ __OBJC_$_CLASS_METHODS_SMHandleFormatting
+ __OBJC_CLASS_RO_$_SMHandleFormatting
+ __OBJC_METACLASS_RO_$_SMHandleFormatting
+ ___58-[SMSafetyMonitorManager fetchSOSReceiversWithCompletion:]_block_invoke
+ ___IMSharedUtilitiesLibraryCore_block_invoke
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ ___copy_helper_block_e8_32r
+ ___destroy_helper_block_e8_32r
+ ___getIMChatCanonicalIDSIDsForAddressSymbolLoc_block_invoke
+ __block_literal_global.367
+ __block_literal_global.564
+ __sl_dlopen
+ _abort_report_np
+ _audit_stringIMSharedUtilities
+ _dlerror
+ _dlsym
+ _getIMChatCanonicalIDSIDsForAddressSymbolLoc
+ _objc_msgSend$_stripFZIDPrefix
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$canonicalIDSAddressForAddress:
+ _objc_msgSend$earliestActiveDeviceIdentifier
+ _objc_msgSend$fetchSOSReceiversWithCompletion:
+ _objc_msgSend$initDestinationBoundSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:
+ _objc_msgSend$initRoundTripSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:
+ _objc_msgSend$initTimeBoundSessionConfigurationWithConversation:sessionID:time:sessionStartDate:sessionSupportsHandoff:sosReceivers:
+ _objc_msgSend$initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:
+ _objc_msgSend$initWithIdentifier:conversation:shouldBeCleanedUpDate:cloudkitShareZoneCleanedUpSuccessfully:syncDate:keyReleaseMessageSendDate:scheduledSendExpiryDate:phoneCache:watchCache:sessionID:safetyCacheKey:allowReadToken:scheduleSendMessageGUID:unlockLocation:lockLocation:startingLocation:offWristLocation:parkedCarLocation:destinationMapItem:timeCacheUploadCompletion:maxCacheSize:maxLocationsInTrace:maxTimeBetweenCacheUpdates:numCacheUpdates:timeTilCacheRelease:numberOfSuccessfulCacheUpdates:numberOfMessageCancelling:numberOfSuccessfulMessageCancelling:numberOfMessageScheduling:numberOfSuccessfulMessageScheduling:wasCacheReleased:wasScheduledSendTriggered:locationOfTrigger:triggerDate:lockState:cacheUpdateBackstopExpiryDate:workoutEvents:numberOfHandoffBecomingActive:numberOfHandoffBecomingNonActive:earliestActiveDeviceIdentifier:latestActiveDeviceIdentifier:
+ _objc_msgSend$initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:
+ _objc_msgSend$isEquivalent:
+ _objc_msgSend$latestActiveDeviceIdentifier
+ _objc_msgSend$numberOfHandoffBecomingActive
+ _objc_msgSend$numberOfHandoffBecomingNonActive
+ _objc_msgSend$sosReceivers
+ getIMChatCanonicalIDSIDsForAddressSymbolLoc.ptr
- -[SMDeviceConfigurationChecker _isEffectivePairedDeviceNearby]
- -[SMInitiatorContact initWithIdentifier:conversation:shouldBeCleanedUpDate:cloudkitShareZoneCleanedUpSuccessfully:syncDate:keyReleaseMessageSendDate:scheduledSendExpiryDate:phoneCache:watchCache:sessionID:safetyCacheKey:allowReadToken:scheduleSendMessageGUID:unlockLocation:lockLocation:startingLocation:offWristLocation:parkedCarLocation:destinationMapItem:timeCacheUploadCompletion:maxCacheSize:maxLocationsInTrace:maxTimeBetweenCacheUpdates:numCacheUpdates:timeTilCacheRelease:numberOfSuccessfulCacheUpdates:numberOfMessageCancelling:numberOfSuccessfulMessageCancelling:numberOfMessageScheduling:numberOfSuccessfulMessageScheduling:wasCacheReleased:wasScheduledSendTriggered:locationOfTrigger:triggerDate:lockState:cacheUpdateBackstopExpiryDate:workoutEvents:]
- -[SMSessionConfiguration initDestinationBoundSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:]
- -[SMSessionConfiguration initRoundTripSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:]
- -[SMSessionConfiguration initTimeBoundSessionConfigurationWithConversation:sessionID:time:sessionStartDate:sessionSupportsHandoff:]
- -[SMSessionConfiguration initTimeBoundSessionConfigurationWithConversation:sessionID:time:sessionSupportsHandoff:]
- -[SMSessionConfiguration initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sessionWorkoutType:]
- -[SMSessionConfiguration initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sessionWorkoutType:]
- GCC_except_table118
- GCC_except_table122
- GCC_except_table126
- GCC_except_table131
- GCC_except_table135
- GCC_except_table139
- GCC_except_table199
- GCC_except_table203
- GCC_except_table296
- GCC_except_table300
- GCC_except_table305
- GCC_except_table309
- GCC_except_table313
- GCC_except_table317
- GCC_except_table347
- _SMSessionDestinationWasReached
- _SMSessionTimeToExitOriginLoi
- _SMSessionTimeToMove250Meters
- _SMSessionTrueDurationRelativeToETA
- __43-[SMSafetyMonitorManager _createConnection]_block_invoke.315
- __43-[SMSafetyMonitorManager _createConnection]_block_invoke_2.316
- __45-[SMSafetyMonitorManager iMessageDeletedFor:]_block_invoke.421
- __54-[SMSafetyMonitorManager kickedFromIMessageGroupWith:]_block_invoke.426
- __55-[SMSafetyMonitorManager iMessageGroupPhotoChangedFor:]_block_invoke.425
- __56-[SMSafetyMonitorManager detailsViewOpenedForSessionID:]_block_invoke.453
- __57-[SMSafetyMonitorManager iMessageConversationDeletedFor:]_block_invoke.422
- __58-[SMSafetyMonitorManager cancelInitializationWithHandler:]_block_invoke.344
- __60-[SMSafetyMonitorManager iMessageGroupMembershipChangedFor:]_block_invoke.423
- __60-[SMSafetyMonitorManager iMessageScheduledSendTriggeredFor:]_block_invoke.417
- __61-[SMSafetyMonitorManager handoffSessionForSessionID:handler:]_block_invoke.352
- __61-[SMSafetyMonitorManager iMessageGroupDisplayNameChangedFor:]_block_invoke.424
- __61-[SMSafetyMonitorManager iMessageReceived:fromHandle:fromMe:]_block_invoke.420
- __62-[SMSafetyMonitorManager fetchCurrentSessionStateWithHandler:]_block_invoke.380
- __62-[SMSafetyMonitorManager sendSafetyCacheForSessionID:handler:]_block_invoke.356
- __64-[SMSafetyMonitorManager endSessionForSessionID:reason:handler:]_block_invoke.348
- __64-[SMSafetyMonitorManager startSessionWithConfiguration:handler:]_block_invoke.357
- __64-[SMSafetyMonitorManager stopMonitoringSessionStateWithHandler:]_block_invoke.379
- __65-[SMSafetyMonitorManager fetchCurrentWorkoutSnapshotWithHandler:]_block_invoke.367
- __65-[SMSafetyMonitorManager modifySessionWithConfiguration:handler:]_block_invoke.355
- __65-[SMSafetyMonitorManager startMonitoringSessionStateWithHandler:]_block_invoke.375
- __67-[SMSafetyMonitorManager cancelInitializationForSessionID:handler:]_block_invoke.347
- __67-[SMSafetyMonitorManager fetchCurrentLocalSessionStateWithHandler:]_block_invoke.383
- __68-[SMSafetyMonitorManager fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.399
- __68-[SMSafetyMonitorManager iMessageSendFor:guid:successful:withError:]_block_invoke.411
- __68-[SMSafetyMonitorManager initializeSessionWithConversation:handler:]_block_invoke.341
- __69-[SMSafetyMonitorManager fetchSessionReceiptForSessionID:completion:]_block_invoke.427
- __69-[SMSafetyMonitorManager stopMonitoringLocalSessionStateWithHandler:]_block_invoke.390
- __70-[SMSafetyMonitorManager fetchAllReceiverSessionStatusWithCompletion:]_block_invoke.434
- __70-[SMSafetyMonitorManager startMonitoringLocalSessionStateWithHandler:]_block_invoke.387
- __72-[SMSafetyMonitorManager fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.403
- __72-[SMSafetyMonitorManager startMonitoringReceiverSafetyCacheWithHandler:]_block_invoke.448
- __73-[SMSafetyMonitorManager startMonitoringInitiatorSafetyCacheWithHandler:]_block_invoke.430
- __74-[SMSafetyMonitorManager checkEligibilityOfDestination:completionHandler:]_block_invoke.460
- __74-[SMSafetyMonitorManager fetchReceiverSafetyCacheForSessionID:completion:]_block_invoke.444
- __74-[SMSafetyMonitorManager promptTimerEndedVerificationWithContext:handler:]_block_invoke.361
- __74-[SMSafetyMonitorManager startMonitoringReceiverSessionStatusWithHandler:]_block_invoke.436
- __74-[SMSafetyMonitorManager stopMonitoringReceiverSafetyCacheWithCompletion:]_block_invoke.452
- __75-[SMSafetyMonitorManager calculateDistanceToDestination:completionHandler:]_block_invoke.461
- __75-[SMSafetyMonitorManager fetchInitiatorSafetyCacheForSessionID:completion:]_block_invoke.372
- __76-[SMSafetyMonitorManager fetchReceiverSessionStatusForSessionID:completion:]_block_invoke.435
- __76-[SMSafetyMonitorManager stopMonitoringReceiverSessionStatusWithCompletion:]_block_invoke.440
- __76-[SMSafetyMonitorManager userRequestedCacheDownloadForSessionID:completion:]_block_invoke.443
- __77-[SMSafetyMonitorManager initializeAndStartSessionWithConfiguration:handler:]_block_invoke.358
- __78-[SMSafetyMonitorManager iMessageScheduledSendCancelFor:successful:withError:]_block_invoke.415
- __78-[SMSafetyMonitorManager respondToTriggerPromptForSessionID:response:handler:]_block_invoke.359
- __82-[SMSafetyMonitorManager promptDestinationAnomalyVerificationWithContext:handler:]_block_invoke.360
- __83-[SMSafetyMonitorManager estimateEtaToDestination:transportType:completionHandler:]_block_invoke.462
- __86-[SMSafetyMonitorManager iMessageScheduledSendScheduledFor:guid:successful:withError:]_block_invoke.414
- __91-[SMSafetyMonitorManager prepareUserInfoForNotificationContent:initiatorHandle:messageUrl:]_block_invoke.469
- __block_literal_global.365
- __block_literal_global.561
- _objc_msgSend$initDestinationBoundSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:
- _objc_msgSend$initRoundTripSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:
- _objc_msgSend$initTimeBoundSessionConfigurationWithConversation:sessionID:time:sessionStartDate:sessionSupportsHandoff:
- _objc_msgSend$initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sessionWorkoutType:
- _objc_msgSend$initWithIdentifier:conversation:shouldBeCleanedUpDate:cloudkitShareZoneCleanedUpSuccessfully:syncDate:keyReleaseMessageSendDate:scheduledSendExpiryDate:phoneCache:watchCache:sessionID:safetyCacheKey:allowReadToken:scheduleSendMessageGUID:unlockLocation:lockLocation:startingLocation:offWristLocation:parkedCarLocation:destinationMapItem:timeCacheUploadCompletion:maxCacheSize:maxLocationsInTrace:maxTimeBetweenCacheUpdates:numCacheUpdates:timeTilCacheRelease:numberOfSuccessfulCacheUpdates:numberOfMessageCancelling:numberOfSuccessfulMessageCancelling:numberOfMessageScheduling:numberOfSuccessfulMessageScheduling:wasCacheReleased:wasScheduledSendTriggered:locationOfTrigger:triggerDate:lockState:cacheUpdateBackstopExpiryDate:workoutEvents:
- _objc_msgSend$initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sessionWorkoutType:
CStrings:
+ "%!s(MISSING)"
+ "(null)"
+ "/System/Library/PrivateFrameworks/IMSharedUtilities.framework/Contents/MacOS/IMSharedUtilities"
+ "Check\u00a0In is not available to send to this group."
+ "IMChatCanonicalIDSIDsForAddress"
+ "SESSION_START_WORKOUT_STRING_LIVE_ACTIVITY"
+ "SMWorkoutAlwaysPromptDismissActionIdentifier"
+ "When Workout Ends"
+ "__kSMSessionConfigurationSOSReceiversKey"
+ "com.apple.SafetyMonitor.Suggestions.WorkoutAlwaysPrompt"
+ "groupReceiverIneligible"
+ "sessionID,%!@(MISSING),identifier,%!@(MISSING),receiverHandles,%!@(MISSING),syncDate,%!@(MISSING),keyReleaseMessageDate,%!@(MISSING),shouldBeCleanedUpDate,%!@(MISSING),allowReadToken,%!@(MISSING),safetyCacheKey,%!@(MISSING),cloudKitCleanedUp,%!d(MISSING),scheduledSendDate,%!@(MISSING),scheduledSendGUID,%!@(MISSING),startLocation,%!@(MISSING),unlockLocation,%!@(MISSING),lockLocation,%!@(MISSING),parkedCarLocation,%!@(MISSING),offWristLocation,%!@(MISSING),workoutEventsCount,%!l(MISSING)u,numberOfHandoffBecomingActive,%!l(MISSING)d,numberOfHandoffBecomingNonActive,%!l(MISSING)d,earliestActiveDeviceIdentifier,%!@(MISSING),latestActiveDeviceIdentifier,%!@(MISSING)"
+ "wasActiveAtEnd"
+ "wasActiveAtStart"
+ "{ReceiverHandles:%!@(MISSING), GroupID:%!@(MISSING), SessionID:%!@(MISSING), SessionStartDate:%!@(MISSING), SessionType:%!@(MISSING), Time:%!@(MISSING), Destination:%!@(MISSING) , userResponseSafeDate:%!@(MISSING), SessionSupportsHandoff:%!d(MISSING),SOSReceivers:%!@(MISSING), SessionWorkoutType:%!l(MISSING)u}"
- "SESSION_START_WORKOUT_STRING_SENDER"
- "sessionID,%!@(MISSING),identifier,%!@(MISSING),receiverHandles,%!@(MISSING),syncDate,%!@(MISSING),keyReleaseMessageDate,%!@(MISSING),shouldBeCleanedUpDate,%!@(MISSING),allowReadToken,%!@(MISSING),safetyCacheKey,%!@(MISSING),cloudKitCleanedUp,%!d(MISSING),scheduledSendDate,%!@(MISSING),scheduledSendGUID,%!@(MISSING),startLocation,%!@(MISSING),unlockLocation,%!@(MISSING),lockLocation,%!@(MISSING),parkedCarLocation,%!@(MISSING),offWristLocation,%!@(MISSING),workoutEventsCount,%!l(MISSING)u"
- "{ReceiverHandles:%!@(MISSING), GroupID:%!@(MISSING), SessionID:%!@(MISSING), SessionStartDate:%!@(MISSING), SessionType:%!@(MISSING), Time:%!@(MISSING), Destination:%!@(MISSING) , userResponseSafeDate:%!@(MISSING), SessionSupportsHandoff:%!d(MISSING), SessionWorkoutType:%!l(MISSING)u}"

```
