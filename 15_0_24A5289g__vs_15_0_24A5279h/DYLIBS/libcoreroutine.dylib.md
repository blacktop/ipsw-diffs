## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-956.0.0.0.0
-  __TEXT.__text: 0x4c78d8
-  __TEXT.__auth_stubs: 0x14f0
-  __TEXT.__objc_methlist: 0x2336c
-  __TEXT.__const: 0x16e8
-  __TEXT.__gcc_except_tab: 0x1a548
-  __TEXT.__oslogstring: 0x508ff
-  __TEXT.__cstring: 0x35237
+953.0.0.0.0
+  __TEXT.__text: 0x4bc990
+  __TEXT.__auth_stubs: 0x14d0
+  __TEXT.__objc_methlist: 0x22e8c
+  __TEXT.__const: 0x16d8
+  __TEXT.__gcc_except_tab: 0x1a238
+  __TEXT.__oslogstring: 0x4f9fd
+  __TEXT.__cstring: 0x341b1
   __TEXT.__dlopen_cstrs: 0xb2
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xa800
+  __TEXT.__unwind_info: 0xa6d8
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x471e
-  __TEXT.__objc_methname: 0x6ca47
-  __TEXT.__objc_methtype: 0xa638
-  __TEXT.__objc_stubs: 0x3efa0
-  __DATA_CONST.__got: 0x2450
-  __DATA_CONST.__const: 0x2648
+  __TEXT.__objc_classname: 0x46f7
+  __TEXT.__objc_methname: 0x6b5fd
+  __TEXT.__objc_methtype: 0xa5b4
+  __TEXT.__objc_stubs: 0x3e560
+  __DATA_CONST.__got: 0x2438
+  __DATA_CONST.__const: 0x25a0
   __DATA_CONST.__objc_classlist: 0x1108
   __DATA_CONST.__objc_catlist: 0x2c8
-  __DATA_CONST.__objc_protolist: 0x2d0
+  __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x126b8
+  __DATA_CONST.__objc_selrefs: 0x123a0
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0xe38
-  __DATA_CONST.__objc_arraydata: 0x1e78
-  __AUTH_CONST.__auth_got: 0xa88
-  __AUTH_CONST.__const: 0xbbf0
-  __AUTH_CONST.__cfstring: 0x1dfa0
-  __AUTH_CONST.__objc_const: 0x44318
-  __AUTH_CONST.__objc_intobj: 0x2d90
+  __DATA_CONST.__objc_arraydata: 0x1e70
+  __AUTH_CONST.__auth_got: 0xa78
+  __AUTH_CONST.__const: 0xba50
+  __AUTH_CONST.__cfstring: 0x1d8e0
+  __AUTH_CONST.__objc_const: 0x43d00
+  __AUTH_CONST.__objc_intobj: 0x2d30
   __AUTH_CONST.__objc_doubleobj: 0x950
   __AUTH_CONST.__objc_arrayobj: 0xb28
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x6c20
-  __DATA.__objc_ivar: 0x2a9c
-  __DATA.__data: 0x2750
+  __DATA.__objc_ivar: 0x2a34
+  __DATA.__data: 0x26e8
   __DATA.__bss: 0x118
   __DATA_DIRTY.__objc_data: 0x3e30
   __DATA_DIRTY.__data: 0x240

   - /System/Library/Frameworks/CoreTelephony.framework/Versions/A/CoreTelephony
   - /System/Library/Frameworks/EventKit.framework/Versions/A/EventKit
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
-  - /System/Library/Frameworks/HealthKit.framework/Versions/A/HealthKit
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Intents.framework/Versions/A/Intents
   - /System/Library/Frameworks/MapKit.framework/Versions/A/MapKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15500
-  Symbols:   34029
-  CStrings:  5377
+  Functions: 15358
+  Symbols:   33750
+  CStrings:  5290
 
Symbols:
+ +[SMSessionConfigurationMO managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sessionWorkoutType:managedObject:managedObjectContext:]
+ -[RTTripSegmentProvider initWithLearnedLocationManager:locationManager:motionActivityManager:tripSegmentInertialDataManager:vehicleStore:tripSegmentManager:elevationAdjuster:distanceCalculator:defaultsManager:visitManager:]
+ -[SMCloudKitQosOptions initWithDefaultQos:masqeradeBundleID:xpcActivity:]
+ -[SMCloudKitQosOptions masqeradeBundleID]
+ -[SMSessionManager _updateSessionWithConversation:handler:]
+ -[SMSessionManager _updateStateMetaDataTo:]
+ -[SMSessionMetricManager _createMetricDictionary]
+ -[SMSessionMetricManager initWithDefaultsManager:learnedLocationManager:sessionStore:locationManager:]
+ -[SMSessionMetricManager onSessionEndedWithReason:]
+ GCC_except_table107
+ GCC_except_table107
+ GCC_except_table120
+ GCC_except_table174
+ GCC_except_table236
+ GCC_except_table242
+ GCC_except_table302
+ GCC_except_table308
+ OBJC_IVAR_$_SMCloudKitQosOptions._masqeradeBundleID
+ _SMSessionDestinationWasReached
+ _SMSessionTimeToExitOriginLoi
+ _SMSessionTimeToMove250Meters
+ _SMSessionTrueDurationRelativeToETA
+ __110-[RTTripSegmentProvider buildTinySegmentArrayForTransitionWithIndex:withinDateInterval:fromActivity:uuidType:]_block_invoke.136
+ __37-[SMInitiatorService _onWorkoutPause]_block_invoke.199
+ __40-[SMInitiatorService _onDeletedMessage:]_block_invoke.191
+ __41-[SMSessionManager _setupTimerForAnomaly]_block_invoke.371
+ __43-[SMSessionManager _setUpCacheReleaseTimer]_block_invoke.366
+ __44-[SMSessionManager processStateSyncMessage:]_block_invoke.136
+ __45-[SMInitiatorService _onDeletedConversation:]_block_invoke.194
+ __46-[SMSessionManager _getMostRecentSessionState]_block_invoke.161
+ __47-[SMClientListener _setupConnection:forClient:]_block_invoke.269
+ __48-[SMSessionManager setSessionStoreAvailability:]_block_invoke.204
+ __48-[SMSessionManager setSessionStoreAvailability:]_block_invoke.207
+ __48-[SMSessionManager setSessionStoreAvailability:]_block_invoke.209
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.153
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.155
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.157
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.154
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.156
+ __49-[SMInitiatorService _startInitializationProcess]_block_invoke.171
+ __49-[SMInitiatorService _startInitializationProcess]_block_invoke.180
+ __49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.183
+ __51-[SMInitiatorCacheManager _setupFetchOnZoneUpdates]_block_invoke.193
+ __51-[SMInitiatorCacheManager _uploadCache:completion:]_block_invoke.357
+ __51-[SMInitiatorCacheManager _uploadCache:completion:]_block_invoke.361
+ __51-[SMSessionManager promptDirectTriggerWithContext:]_block_invoke.475
+ __52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.295
+ __53-[SMSessionManager processStateSyncUpdateReqMessage:]_block_invoke.138
+ __54-[SMSessionManager iMessageGroupMembershipChangedFor:]_block_invoke.442
+ __54-[SMSessionManager iMessageGroupMembershipChangedFor:]_block_invoke.445
+ __54-[SMSessionMetricManager _onDailyMetricsNotification:]_block_invoke.292
+ __55-[SMInitiatorCacheManager _schedulePeriodicCacheUpdate]_block_invoke.302
+ __55-[SMInitiatorCacheManager _schedulePeriodicCacheUpdate]_block_invoke.303
+ __55-[SMSessionManager iMessageGroupDisplayNameChangedFor:]_block_invoke.452
+ __55-[SMSessionManager iMessageGroupDisplayNameChangedFor:]_block_invoke.453
+ __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.149
+ __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.150
+ __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.155
+ __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.159
+ __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.160
+ __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.164
+ __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.166
+ __57-[SMInitiatorCacheManager _setupShareZoneWithCompletion:]_block_invoke.199
+ __57-[SMInitiatorCacheManager _storeInitiatorContactInStore:]_block_invoke.415
+ __57-[SMInitiatorCacheManager updateCacheUpdateBackstopTimer]_block_invoke.411
+ __57-[SMInitiatorCacheManager updateCacheUpdateBackstopTimer]_block_invoke.412
+ __57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.120
+ __57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.122
+ __57-[SMSessionManager promptSafeArrivalWithContext:handler:]_block_invoke.460
+ __57-[SMSessionManager storeManagerStatusInStore:completion:]_block_invoke.218
+ __58-[SMInitiatorCacheManager _updateCacheDataWithCompletion:]_block_invoke.322
+ __58-[SMInitiatorCacheManager _updateCacheDataWithCompletion:]_block_invoke.326
+ __58-[SMInitiatorCacheManager _updateCacheDataWithCompletion:]_block_invoke.328
+ __58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.259
+ __58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.260
+ __58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.265
+ __58-[SMSessionManager processSessionEndRemoteControlMessage:]_block_invoke.134
+ __58-[SMSessionManager startSessionWithConfiguration:handler:]_block_invoke.426
+ __59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.142
+ __59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.152
+ __59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.167
+ __60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.343
+ __60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.344
+ __60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.347
+ __60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.348
+ __61-[SMInitiatorCacheManager _cleanUpInitiatorContactLocalStore]_block_invoke.424
+ __61-[SMInitiatorCacheManager _cleanUpInitiatorContactLocalStore]_block_invoke.429
+ __61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.383
+ __61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.384
+ __61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.385
+ __61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.386
+ __61-[SMInitiatorService _fetchAllZonesFromContainerWithHandler:]_block_invoke.208
+ __62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.311
+ __62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.314
+ __62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.315
+ __62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.319
+ __62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.320
+ __65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.238
+ __65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.239
+ __65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.241
+ __65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.241
+ __66-[SMInitiatorService _fetchSessionReceiptForSessionID:completion:]_block_invoke.290
+ __67-[RTTripSegmentProvider _startReconstructTripSegmentWithTrainMode:]_block_invoke.127
+ __67-[RTTripSegmentProvider _startReconstructTripSegmentWithTrainMode:]_block_invoke.129
+ __67-[SMInitiatorCacheManager _requestSmoothedLocationsWithCompletion:]_block_invoke.334
+ __67-[SMInitiatorService _endSessionEarlyIfNecessaryWithConfiguration:]_block_invoke.283
+ __67-[SMInitiatorService _startFrequentSingleShotFetchAllZonesActivity]_block_invoke.218
+ __67-[SMInitiatorService _startInfrequentPeriodicFetchAllZonesActivity]_block_invoke.229
+ __67-[SMSessionManager _handoffSessionForSessionID:retryCount:handler:]_block_invoke.284
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke.313
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke.319
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke.329
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_10.342
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_11.343
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_12.344
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_13.345
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_14.346
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_15.349
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_16.350
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_17.351
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_18.354
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_19.355
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_2.320
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_2.332
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_3.333
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_4.334
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_5.335
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_6.336
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_7.339
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_8.340
+ __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_9.341
+ __69-[SMInitiatorCacheManager _cancelScheduledKeyReleaseForConversation:]_block_invoke.395
+ __69-[SMInitiatorService _sendSessionStartMessageWithInvitationTokenMap:]_block_invoke.270
+ __69-[SMSessionManager _checkIfHandoffCriteriaSatisfiedForState:handler:]_block_invoke.292
+ __69-[SMSessionManager _checkIfHandoffCriteriaSatisfiedForState:handler:]_block_invoke_2.293
+ __69-[SMSessionManager _notifyObserversForStateChangeWithTransitionType:]_block_invoke.248
+ __70-[SMActiveSessionZone writeActiveSessionDetailsRecord:qos:completion:]_block_invoke.48
+ __70-[SMActiveSessionZone writeActiveSessionDetailsRecord:qos:completion:]_block_invoke.51
+ __71-[SMSessionManager _checkInitiatorEligibilityWithIsHandoff:completion:]_block_invoke.305
+ __71-[SMSessionManager processResponseToTriggerPromptRemoteControlMessage:]_block_invoke.132
+ __72-[RTTripSegmentProvider addToTransitionLocationsBuffer:forDateInterval:]_block_invoke.139
+ __72-[SMSessionManager initializeSessionWithSessionID:conversation:handler:]_block_invoke.398
+ __73-[SMSessionManager sendSessionEndMessageWithReason:associatedGUID:state:]_block_invoke.504
+ __74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.275
+ __74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.276
+ __74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.278
+ __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.254
+ __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.258
+ __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.259
+ __74-[SMSessionManager processModifySessionConfigurationRemoteControlMessage:]_block_invoke.135
+ __76-[SMSessionManager promptWorkoutSessionEndVerificationWithContext:handlers:]_block_invoke.459
+ __83-[SMActiveSessionZone checkActiveSessionDetailsZoneAvailibilityWithQos:completion:]_block_invoke.46
+ __84-[SMSuggestionsMetricsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.133
+ __85-[SMSuggestionsMetricsManager _getSuggestionsCountSelectedForPastDate:endDate:error:]_block_invoke.116
+ __99-[RTTripSegmentProvider buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:]_block_invoke.172
+ __99-[RTTripSegmentProvider buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:]_block_invoke.177
+ __99-[RTTripSegmentProvider buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:]_block_invoke.180
+ ___373+[SMSessionConfigurationMO managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sessionWorkoutType:managedObject:managedObjectContext:]_block_invoke
+ ___51-[SMSessionMetricManager onSessionEndedWithReason:]_block_invoke
+ ___69-[SMSessionManager _checkIfHandoffCriteriaSatisfiedForState:handler:]_block_invoke_2
+ ___block_descriptor_173_e8_32s40s48s56s64s72s80s88r_e5_v8?0l
+ ___block_descriptor_40_e33_v28?0"NSString"8B16"NSError"20l
+ ___block_descriptor_40_e8_32bs_e47_v28?0"SMActiveSessionDetails"8B16"NSError"20l
+ ___block_descriptor_64_e8_32s40s48bs56r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_64_e8_32s40s48bs56r_e47_v28?0"SMActiveSessionDetails"8B16"NSError"20l
+ ___block_descriptor_81_e8_32s40s48s56s64bs72r_e5_v8?0l
+ __block_literal_global.1096
+ __block_literal_global.158
+ __block_literal_global.173
+ __block_literal_global.175
+ __block_literal_global.177
+ __block_literal_global.179
+ __block_literal_global.182
+ __block_literal_global.185
+ __block_literal_global.196
+ __block_literal_global.214
+ __block_literal_global.250
+ __block_literal_global.261
+ __block_literal_global.315
+ __block_literal_global.322
+ __block_literal_global.324
+ __block_literal_global.326
+ __block_literal_global.327
+ __block_literal_global.328
+ __block_literal_global.331
+ __block_literal_global.337
+ __block_literal_global.353
+ __block_literal_global.357
+ __block_literal_global.368
+ __block_literal_global.402
+ __block_literal_global.447
+ __block_literal_global.451
+ __block_literal_global.479
+ __block_literal_global.481
+ __block_literal_global.485
+ __block_literal_global.487
+ __handleShareAllLocationsChanged_block_invoke.957
+ _objc_msgSend$_createMetricDictionary
+ _objc_msgSend$_updateSessionWithConversation:handler:
+ _objc_msgSend$_updateStateMetaDataTo:
+ _objc_msgSend$hasEqualPrimaryHandlesAsConversation:
+ _objc_msgSend$initDestinationBoundSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:
+ _objc_msgSend$initRoundTripSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:
+ _objc_msgSend$initTimeBoundSessionConfigurationWithConversation:sessionID:time:sessionStartDate:sessionSupportsHandoff:
+ _objc_msgSend$initTimeBoundSessionConfigurationWithConversation:sessionID:time:sessionSupportsHandoff:
+ _objc_msgSend$initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sessionWorkoutType:
+ _objc_msgSend$initWithDefaultQos:masqeradeBundleID:xpcActivity:
+ _objc_msgSend$initWithDefaultsManager:learnedLocationManager:sessionStore:locationManager:
+ _objc_msgSend$initWithIdentifier:conversation:shouldBeCleanedUpDate:cloudkitShareZoneCleanedUpSuccessfully:syncDate:keyReleaseMessageSendDate:scheduledSendExpiryDate:phoneCache:watchCache:sessionID:safetyCacheKey:allowReadToken:scheduleSendMessageGUID:unlockLocation:lockLocation:startingLocation:offWristLocation:parkedCarLocation:destinationMapItem:timeCacheUploadCompletion:maxCacheSize:maxLocationsInTrace:maxTimeBetweenCacheUpdates:numCacheUpdates:timeTilCacheRelease:numberOfSuccessfulCacheUpdates:numberOfMessageCancelling:numberOfSuccessfulMessageCancelling:numberOfMessageScheduling:numberOfSuccessfulMessageScheduling:wasCacheReleased:wasScheduledSendTriggered:locationOfTrigger:triggerDate:lockState:cacheUpdateBackstopExpiryDate:workoutEvents:
+ _objc_msgSend$initWithLearnedLocationManager:locationManager:motionActivityManager:tripSegmentInertialDataManager:vehicleStore:tripSegmentManager:elevationAdjuster:distanceCalculator:defaultsManager:visitManager:
+ _objc_msgSend$initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sessionWorkoutType:
+ _objc_msgSend$managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sessionWorkoutType:managedObject:managedObjectContext:
+ _objc_msgSend$masqeradeBundleID
+ _objc_msgSend$onSessionEndedWithReason:
- +[SMMessagingUtilities _canonicalHandleMapFromHandles:]
- +[SMMessagingUtilities _canonicalizeHandles:]
- +[SMMessagingUtilities canonicalIDSIDsForAddress:]
- +[SMMessagingUtilities conversationFromHandlesInConversation1:canonicallyIntersectedWithHandlesInConversation2:]
- +[SMMessagingUtilities conversationFromHandlesInConversation1:canonicallyMappedToHandlesInConversation2:]
- +[SMMessagingUtilities handlesInConversation1:canonicallyEqualsHandlesInConversation2:]
- +[SMSessionConfigurationMO managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:managedObject:managedObjectContext:]
- +[SMSessionManager SessionHandoffRebootReconciliationDecisionToString:]
- +[SMSessionManager SessionHandoffRebootReconciliationStateToString:]
- -[RTIntermittentGNSSManager completedInitialWifiScan]
- -[RTIntermittentGNSSManager remoteStatusTimeoutTimer]
- -[RTIntermittentGNSSManager setCompletedInitialWifiScan:]
- -[RTIntermittentGNSSManager setRemoteStatusTimeoutTimer:]
- -[RTTripSegmentProvider inertialOdometryManager]
- -[RTTripSegmentProvider initWithLearnedLocationManager:locationManager:motionActivityManager:tripSegmentInertialDataManager:inertialOdometryManager:vehicleStore:tripSegmentManager:elevationAdjuster:distanceCalculator:defaultsManager:visitManager:]
- -[RTTripSegmentProvider setInertialOdometryManager:]
- -[RTTripSegmentProvider setUsingLegacyInertialData:]
- -[RTTripSegmentProvider usingLegacyInertialData]
- -[SMActiveSessionZone _addObserver:]
- -[SMActiveSessionZone _notifyObserversForActiveSessionDetailsFetchAttemptedFromCKCompleted:success:error:]
- -[SMActiveSessionZone _onActiveSessionDetailsFetchAttemptFromCKCompleted:success:error:]
- -[SMActiveSessionZone _removeObserver:]
- -[SMActiveSessionZone _saveLatestActiveSessionDetailsStateToDefaults:]
- -[SMActiveSessionZone addObserver:]
- -[SMActiveSessionZone observers]
- -[SMActiveSessionZone removeObserver:]
- -[SMActiveSessionZone setObservers:]
- -[SMCloudKitQosOptions initWithDefaultQos:masqueradeBundleID:xpcActivity:]
- -[SMCloudKitQosOptions masqueradeBundleID]
- -[SMDaemonClient fetchSOSReceiversWithCompletion:]
- -[SMInitiatorService _fetchSOSReceiversWithCompletion:]
- -[SMInitiatorService fetchSOSReceiversWithCompletion:]
- -[SMInitiatorService receivedSessionTypeKeyRelease:fromHandle:fromMe:]
- -[SMSessionManager _clearActiveSessionDetailsTimeoutTimer]
- -[SMSessionManager _evaluateHandoffRebootReconciliationState:]
- -[SMSessionManager _handleTransitionToStateAfterBootstrap:isActiveDevice:]
- -[SMSessionManager _isActiveSessionDetailsFetchAttemptFailed]
- -[SMSessionManager _isActiveSessionDetailsFetchedFromCloudKitSinceBoot]
- -[SMSessionManager _isActiveSessionDetailsLocalRecordExpired]
- -[SMSessionManager _isActiveSessionDetailsOutOfSync]
- -[SMSessionManager _isEligibleToSendStateUpdateReqMessageAfterBootstrap:isActiveDevice:]
- -[SMSessionManager _isLocalStateInSyncWithActiveSessionDetails:deviceSessionManagerState:]
- -[SMSessionManager _isMultiDeviceSetupForLocalState:]
- -[SMSessionManager _onActiveSessionDetailsFetchAttemptFromCKCompleted:success:error:]
- -[SMSessionManager _onActiveSessionDetailsTimeoutTimerExpiry]
- -[SMSessionManager _reconciliationDecisionForState:isActiveDevice:]
- -[SMSessionManager _reconciliationForDecisionForCKFetchCompleted:]
- -[SMSessionManager _resetPendingSendSessionEndMessage]
- -[SMSessionManager _setPendingSendSessionEndMessageWithReason:associatedGUID:]
- -[SMSessionManager _startActiveSessionDetailsTimerWithLatency:]
- -[SMSessionManager _stateValidForSendSessionEndMessageRetry:]
- -[SMSessionManager _updateSessionWithConversation:sosReceivers:handler:]
- -[SMSessionManager activeSessionDetailsFetchTimeout]
- -[SMSessionManager activeSessionDetailsTimeoutTimer]
- -[SMSessionManager activeSessionDetails]
- -[SMSessionManager fetchSOSReceiversWithCompletion:]
- -[SMSessionManager handoffRebootReconciliationState]
- -[SMSessionManager onActiveSessionDetailsFetchAttemptFromCKCompleted:success:error:]
- -[SMSessionManager processSessionTypeKeyRelease:]
- -[SMSessionManager setActiveSessionDetails:]
- -[SMSessionManager setActiveSessionDetailsFetchTimeout:]
- -[SMSessionManager setActiveSessionDetailsTimeoutTimer:]
- -[SMSessionManager setHandoffRebootReconciliationState:]
- -[SMSessionMetricManager _createDestinationMetricDictionary]
- -[SMSessionMetricManager _isCellularActivated]
- -[SMSessionMetricManager _isStandalone]
- -[SMSessionMetricManager currentDeviceIdentifier]
- -[SMSessionMetricManager didHandoffOccur]
- -[SMSessionMetricManager didWorkoutEnd]
- -[SMSessionMetricManager didWorkoutPause]
- -[SMSessionMetricManager initWithDefaultsManager:learnedLocationManager:sessionStore:locationManager:currentDeviceIdentifier:]
- -[SMSessionMetricManager isWorkoutAlwaysOn]
- -[SMSessionMetricManager modeOfTransportation]
- -[SMSessionMetricManager numAnomalyPromptDuringHysteresis]
- -[SMSessionMetricManager numAnomalyPrompt]
- -[SMSessionMetricManager numHandoff]
- -[SMSessionMetricManager numLPMSeparation]
- -[SMSessionMetricManager numRecipients]
- -[SMSessionMetricManager numTakeover]
- -[SMSessionMetricManager numUnsupportedDeviceSeparation]
- -[SMSessionMetricManager numUserDisabledConnectivity]
- -[SMSessionMetricManager onBecomingActiveDevice:]
- -[SMSessionMetricManager onBecomingNonActiveDevice:]
- -[SMSessionMetricManager onLPMSeparation]
- -[SMSessionMetricManager onSessionEndedForActiveDevice:]
- -[SMSessionMetricManager onSessionTerminatedWithReason:]
- -[SMSessionMetricManager onUnsupportedDeviceSeparation]
- -[SMSessionMetricManager onUserDisabledConnectivity]
- -[SMSessionMetricManager onWorkoutEnded]
- -[SMSessionMetricManager onWorkoutPaused]
- -[SMSessionMetricManager setCurrentDeviceIdentifier:]
- -[SMSessionMetricManager setDidHandoffOccur:]
- -[SMSessionMetricManager setDidWorkoutEnd:]
- -[SMSessionMetricManager setDidWorkoutPause:]
- -[SMSessionMetricManager setIsWorkoutAlwaysOn:]
- -[SMSessionMetricManager setModeOfTransportation:]
- -[SMSessionMetricManager setNumAnomalyPrompt:]
- -[SMSessionMetricManager setNumAnomalyPromptDuringHysteresis:]
- -[SMSessionMetricManager setNumHandoff:]
- -[SMSessionMetricManager setNumLPMSeparation:]
- -[SMSessionMetricManager setNumRecipients:]
- -[SMSessionMetricManager setNumTakeover:]
- -[SMSessionMetricManager setNumUnsupportedDeviceSeparation:]
- -[SMSessionMetricManager setNumUserDisabledConnectivity:]
- -[SMSessionMetricManager setWasActiveAtEnd:]
- -[SMSessionMetricManager setWasActiveAtStart:]
- -[SMSessionMetricManager setWorkoutActivityTypeString:]
- -[SMSessionMetricManager wasActiveAtEnd]
- -[SMSessionMetricManager wasActiveAtStart]
- -[SMSessionMetricManager workoutActivityTypeString]
- -[SMSuggestionsMetricsManager _computeWorkoutAlwaysPromptMetricsWithError:]
- -[SMSuggestionsMetricsManager _submitWorkoutAlwaysPromptResponseMetricUponNotification:]
- -[SMSuggestionsMetricsManager submitWorkoutAlwaysPromptResponseMetricUponNotification:]
- GCC_except_table133
- GCC_except_table258
- GCC_except_table267
- GCC_except_table273
- GCC_except_table336
- GCC_except_table342
- OBJC_IVAR_$_RTIntermittentGNSSManager._completedInitialWifiScan
- OBJC_IVAR_$_RTTripSegmentProvider._inertialOdometryManager
- OBJC_IVAR_$_RTTripSegmentProvider._usingLegacyInertialData
- OBJC_IVAR_$_SMCloudKitQosOptions._masqueradeBundleID
- OBJC_IVAR_$_SMSessionManager._activeSessionDetails
- OBJC_IVAR_$_SMSessionManager._activeSessionDetailsFetchTimeout
- OBJC_IVAR_$_SMSessionManager._activeSessionDetailsTimeoutTimer
- OBJC_IVAR_$_SMSessionManager._handoffRebootReconciliationState
- OBJC_IVAR_$_SMSessionMetricManager._currentDeviceIdentifier
- OBJC_IVAR_$_SMSessionMetricManager._didHandoffOccur
- OBJC_IVAR_$_SMSessionMetricManager._didWorkoutEnd
- OBJC_IVAR_$_SMSessionMetricManager._didWorkoutPause
- OBJC_IVAR_$_SMSessionMetricManager._isWorkoutAlwaysOn
- OBJC_IVAR_$_SMSessionMetricManager._modeOfTransportation
- OBJC_IVAR_$_SMSessionMetricManager._numAnomalyPrompt
- OBJC_IVAR_$_SMSessionMetricManager._numAnomalyPromptDuringHysteresis
- OBJC_IVAR_$_SMSessionMetricManager._numHandoff
- OBJC_IVAR_$_SMSessionMetricManager._numLPMSeparation
- OBJC_IVAR_$_SMSessionMetricManager._numRecipients
- OBJC_IVAR_$_SMSessionMetricManager._numTakeover
- OBJC_IVAR_$_SMSessionMetricManager._numUnsupportedDeviceSeparation
- OBJC_IVAR_$_SMSessionMetricManager._numUserDisabledConnectivity
- OBJC_IVAR_$_SMSessionMetricManager._wasActiveAtEnd
- OBJC_IVAR_$_SMSessionMetricManager._wasActiveAtStart
- OBJC_IVAR_$_SMSessionMetricManager._workoutActivityTypeString
- _IMChatCanonicalIDSIDsForAddress
- _RTAnalyticsEventSMSuggestionsWorkoutAlwaysPromptConsidered
- _RTIntermittentGNSSFetchRemoteStatusTimeoutTimerIdentifier
- _SMExitAndArrivalMetricsDestinationWasReachedKey
- _SMExitAndArrivalMetricsTimeToExitOriginLOIKey
- _SMExitAndArrivalMetricsTimeToMove250MetersKey
- _SMExitAndArrivalMetricsTrueDurationRelativeToETAKey
- _SMExitAndArrivalMetricsWasActiveAtEndKey
- _SMExitAndArrivalMetricsWasActiveAtStartKey
- _SMSessionManagerHandoffActiveSessionDetailsFetchTimeout
- _SMSubmitSuggesionsWorkoutAlwaysPromptResponseNotification
- __110-[RTTripSegmentProvider buildTinySegmentArrayForTransitionWithIndex:withinDateInterval:fromActivity:uuidType:]_block_invoke.139
- __37-[SMInitiatorService _onWorkoutPause]_block_invoke.215
- __40-[SMInitiatorService _onDeletedMessage:]_block_invoke.207
- __41-[SMSessionManager _setupTimerForAnomaly]_block_invoke.430
- __43-[SMSessionManager _setUpCacheReleaseTimer]_block_invoke.426
- __44-[SMSessionManager processStateSyncMessage:]_block_invoke.143
- __45-[SMInitiatorService _onDeletedConversation:]_block_invoke.210
- __46-[SMSessionManager _getMostRecentSessionState]_block_invoke.179
- __47-[SMClientListener _setupConnection:forClient:]_block_invoke.270
- __48-[SMSessionManager setSessionStoreAvailability:]_block_invoke.228
- __48-[SMSessionManager setSessionStoreAvailability:]_block_invoke.230
- __48-[SMSessionManager setSessionStoreAvailability:]_block_invoke.232
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.168
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.170
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.172
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.169
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.171
- __49-[SMInitiatorService _startInitializationProcess]_block_invoke.187
- __49-[SMInitiatorService _startInitializationProcess]_block_invoke.196
- __49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.199
- __49-[SMSessionManager processSessionTypeKeyRelease:]_block_invoke.150
- __51-[SMInitiatorCacheManager _setupFetchOnZoneUpdates]_block_invoke.226
- __51-[SMInitiatorCacheManager _uploadCache:completion:]_block_invoke.393
- __51-[SMInitiatorCacheManager _uploadCache:completion:]_block_invoke.397
- __51-[SMSessionManager promptDirectTriggerWithContext:]_block_invoke.543
- __52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.408
- __53-[SMSessionManager processStateSyncUpdateReqMessage:]_block_invoke.145
- __54-[SMSessionManager iMessageGroupMembershipChangedFor:]_block_invoke.501
- __54-[SMSessionManager iMessageGroupMembershipChangedFor:]_block_invoke.504
- __54-[SMSessionMetricManager _onDailyMetricsNotification:]_block_invoke.405
- __55-[SMInitiatorCacheManager _schedulePeriodicCacheUpdate]_block_invoke.338
- __55-[SMInitiatorCacheManager _schedulePeriodicCacheUpdate]_block_invoke.339
- __55-[SMInitiatorService _fetchSOSReceiversWithCompletion:]_block_invoke.305
- __55-[SMSessionManager iMessageGroupDisplayNameChangedFor:]_block_invoke.511
- __55-[SMSessionManager iMessageGroupDisplayNameChangedFor:]_block_invoke.512
- __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.152
- __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.153
- __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.158
- __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.162
- __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.163
- __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.171
- __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.175
- __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.176
- __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.177
- __56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.180
- __57-[SMInitiatorCacheManager _setupShareZoneWithCompletion:]_block_invoke.232
- __57-[SMInitiatorCacheManager _storeInitiatorContactInStore:]_block_invoke.451
- __57-[SMInitiatorCacheManager updateCacheUpdateBackstopTimer]_block_invoke.447
- __57-[SMInitiatorCacheManager updateCacheUpdateBackstopTimer]_block_invoke.448
- __57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.135
- __57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.137
- __57-[SMSessionManager promptSafeArrivalWithContext:handler:]_block_invoke.520
- __57-[SMSessionManager storeManagerStatusInStore:completion:]_block_invoke.262
- __57-[SMSessionMetricManager _gatherSessionDestinationStats:]_block_invoke.395
- __58-[RTIntermittentGNSSManager fetchRemoteStatusWithHandler:]_block_invoke.110
- __58-[SMInitiatorCacheManager _updateCacheDataWithCompletion:]_block_invoke.358
- __58-[SMInitiatorCacheManager _updateCacheDataWithCompletion:]_block_invoke.362
- __58-[SMInitiatorCacheManager _updateCacheDataWithCompletion:]_block_invoke.364
- __58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.293
- __58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.294
- __58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.299
- __58-[SMSessionManager processSessionEndRemoteControlMessage:]_block_invoke.141
- __58-[SMSessionManager startSessionWithConfiguration:handler:]_block_invoke.485
- __59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.175
- __59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.185
- __59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.200
- __60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.379
- __60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.380
- __60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.383
- __60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.384
- __61-[SMInitiatorCacheManager _cleanUpInitiatorContactLocalStore]_block_invoke.460
- __61-[SMInitiatorCacheManager _cleanUpInitiatorContactLocalStore]_block_invoke.465
- __61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.419
- __61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.420
- __61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.421
- __61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.422
- __61-[SMInitiatorService _fetchAllZonesFromContainerWithHandler:]_block_invoke.224
- __62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.347
- __62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.350
- __62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.351
- __62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.355
- __62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.356
- __62-[SMSessionManager _evaluateHandoffRebootReconciliationState:]_block_invoke.358
- __65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.272
- __65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.273
- __65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.275
- __65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.257
- __66-[SMInitiatorService _fetchSessionReceiptForSessionID:completion:]_block_invoke.311
- __67-[RTTripSegmentProvider _startReconstructTripSegmentWithTrainMode:]_block_invoke.130
- __67-[RTTripSegmentProvider _startReconstructTripSegmentWithTrainMode:]_block_invoke.132
- __67-[SMInitiatorCacheManager _requestSmoothedLocationsWithCompletion:]_block_invoke.370
- __67-[SMInitiatorService _endSessionEarlyIfNecessaryWithConfiguration:]_block_invoke.299
- __67-[SMInitiatorService _startFrequentSingleShotFetchAllZonesActivity]_block_invoke.234
- __67-[SMInitiatorService _startInfrequentPeriodicFetchAllZonesActivity]_block_invoke.245
- __67-[SMSessionManager _handoffSessionForSessionID:retryCount:handler:]_block_invoke.328
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke.372
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke.378
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke.388
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_10.401
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_11.402
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_12.403
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_13.404
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_14.405
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_15.406
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_16.407
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_17.410
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_18.411
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_19.412
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_2.379
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_2.391
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_20.415
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_3.392
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_4.393
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_5.394
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_6.395
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_7.398
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_8.399
- __67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_9.400
- __68-[SMSessionManager onScheduledSendMessageCanceledForSessionID:guid:]_block_invoke.530
- __69-[SMInitiatorCacheManager _cancelScheduledKeyReleaseForConversation:]_block_invoke.431
- __69-[SMInitiatorService _sendSessionStartMessageWithInvitationTokenMap:]_block_invoke.286
- __69-[SMSessionManager _checkIfHandoffCriteriaSatisfiedForState:handler:]_block_invoke.337
- __69-[SMSessionManager _checkIfHandoffCriteriaSatisfiedForState:handler:]_block_invoke.340
- __69-[SMSessionManager _checkIfHandoffCriteriaSatisfiedForState:handler:]_block_invoke.341
- __69-[SMSessionManager _notifyObserversForStateChangeWithTransitionType:]_block_invoke.292
- __70-[SMActiveSessionZone writeActiveSessionDetailsRecord:qos:completion:]_block_invoke.55
- __70-[SMActiveSessionZone writeActiveSessionDetailsRecord:qos:completion:]_block_invoke.58
- __71-[SMSessionManager _checkInitiatorEligibilityWithIsHandoff:completion:]_block_invoke.351
- __71-[SMSessionManager processResponseToTriggerPromptRemoteControlMessage:]_block_invoke.139
- __72-[RTTripSegmentProvider addToTransitionLocationsBuffer:forDateInterval:]_block_invoke.142
- __72-[SMSessionManager initializeSessionWithSessionID:conversation:handler:]_block_invoke.457
- __73-[SMSessionManager sendSessionEndMessageWithReason:associatedGUID:state:]_block_invoke.572
- __74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.311
- __74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.312
- __74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.314
- __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.270
- __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.274
- __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.275
- __74-[SMSessionManager onScheduledSendMessageScheduledForSessionID:guid:date:]_block_invoke.525
- __74-[SMSessionManager processModifySessionConfigurationRemoteControlMessage:]_block_invoke.142
- __76-[SMSessionManager promptWorkoutSessionEndVerificationWithContext:handlers:]_block_invoke.518
- __83-[SMActiveSessionZone checkActiveSessionDetailsZoneAvailibilityWithQos:completion:]_block_invoke.53
- __84-[SMSuggestionsMetricsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.152
- __85-[SMSuggestionsMetricsManager _getSuggestionsCountSelectedForPastDate:endDate:error:]_block_invoke.135
- __89-[SMSessionManager onSessionStartMessageSendResultWithMessage:messageGUID:success:error:]_block_invoke.521
- __99-[RTTripSegmentProvider buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:]_block_invoke.182
- __99-[RTTripSegmentProvider buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:]_block_invoke.187
- __99-[RTTripSegmentProvider buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:]_block_invoke.190
- __HKWorkoutActivityNameForActivityType
- __OBJC_$_CLASS_METHODS_SMSessionManager
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SMActiveSessionZoneObserverProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SMActiveSessionZoneProtocol
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SMActiveSessionZoneObserverProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_SMActiveSessionZoneObserverProtocol
- __OBJC_$_PROTOCOL_REFS_SMActiveSessionZoneObserverProtocol
- __OBJC_LABEL_PROTOCOL_$_SMActiveSessionZoneObserverProtocol
- __OBJC_PROTOCOL_$_SMActiveSessionZoneObserverProtocol
- ___35-[SMActiveSessionZone addObserver:]_block_invoke
- ___38-[SMActiveSessionZone removeObserver:]_block_invoke
- ___386+[SMSessionConfigurationMO managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:managedObject:managedObjectContext:]_block_invoke
- ___40-[SMSessionMetricManager onWorkoutEnded]_block_invoke
- ___41-[SMSessionMetricManager onLPMSeparation]_block_invoke
- ___41-[SMSessionMetricManager onWorkoutPaused]_block_invoke
- ___46-[SMSessionMetricManager _isCellularActivated]_block_invoke
- ___49-[SMSessionManager processSessionTypeKeyRelease:]_block_invoke
- ___49-[SMSessionMetricManager onBecomingActiveDevice:]_block_invoke
- ___52-[SMSessionMetricManager onBecomingNonActiveDevice:]_block_invoke
- ___52-[SMSessionMetricManager onUserDisabledConnectivity]_block_invoke
- ___54-[SMInitiatorService fetchSOSReceiversWithCompletion:]_block_invoke
- ___55-[SMInitiatorService _fetchSOSReceiversWithCompletion:]_block_invoke
- ___55-[SMInitiatorService _fetchSOSReceiversWithCompletion:]_block_invoke_2
- ___55-[SMInitiatorService _fetchSOSReceiversWithCompletion:]_block_invoke_3
- ___55-[SMSessionMetricManager onUnsupportedDeviceSeparation]_block_invoke
- ___56-[SMSessionMetricManager onSessionEndedForActiveDevice:]_block_invoke
- ___56-[SMSessionMetricManager onSessionTerminatedWithReason:]_block_invoke
- ___62-[SMSessionManager _evaluateHandoffRebootReconciliationState:]_block_invoke
- ___63-[SMSessionManager _startActiveSessionDetailsTimerWithLatency:]_block_invoke
- ___67-[SMSessionManager _stateTransitionDecisionToState:transitionType:]_block_invoke_21
- ___74-[SMSessionManager _handleTransitionToStateAfterBootstrap:isActiveDevice:]_block_invoke
- ___84-[SMSessionManager onActiveSessionDetailsFetchAttemptFromCKCompleted:success:error:]_block_invoke
- ___87-[SMSuggestionsMetricsManager submitWorkoutAlwaysPromptResponseMetricUponNotification:]_block_invoke
- ___block_descriptor_181_e8_32s40s48s56s64s72s80s88s96r_e5_v8?0l
- ___block_descriptor_32_e47_v28?0"SMActiveSessionDetails"8B16"NSError"20l
- ___block_descriptor_33_e20_v20?0B8"NSError"12l
- ___block_descriptor_40_e8_32s_e61_B24?0"CLBackgroundInertialOdometrySample"8"NSDictionary"16l
- ___block_descriptor_48_e8_32s_e33_v28?0"NSString"8B16"NSError"20l
- ___block_descriptor_56_e8_32s40bs_e47_v28?0"SMActiveSessionDetails"8B16"NSError"20l
- ___block_descriptor_56_e8_32s40r48r_e47_v28?0"SMActiveSessionDetails"8B16"NSError"20l
- ___block_descriptor_56_e8_32s_e20_v20?0B8"NSError"12l
- ___block_descriptor_64_e8_32s40bs_e30_v24?0"CKRecord"8"NSError"16l
- ___block_descriptor_72_e8_32s40s48bs56r64r_e20_v20?0B8"NSError"12l
- ___block_descriptor_72_e8_32s40s48bs56r64r_e47_v28?0"SMActiveSessionDetails"8B16"NSError"20l
- ___block_descriptor_80_e8_32s40s48s56bs_e20_v20?0B8"NSError"12l
- ___block_descriptor_89_e8_32s40s48s56s64bs72r80r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96r
- __block_literal_global.1218
- __block_literal_global.148
- __block_literal_global.156
- __block_literal_global.189
- __block_literal_global.195
- __block_literal_global.198
- __block_literal_global.201
- __block_literal_global.238
- __block_literal_global.277
- __block_literal_global.290
- __block_literal_global.294
- __block_literal_global.360
- __block_literal_global.371
- __block_literal_global.374
- __block_literal_global.381
- __block_literal_global.383
- __block_literal_global.385
- __block_literal_global.387
- __block_literal_global.397
- __block_literal_global.400
- __block_literal_global.409
- __block_literal_global.414
- __block_literal_global.417
- __block_literal_global.428
- __block_literal_global.432
- __block_literal_global.506
- __block_literal_global.510
- __block_literal_global.514
- __block_literal_global.523
- __block_literal_global.527
- __block_literal_global.532
- __block_literal_global.547
- __block_literal_global.549
- __block_literal_global.551
- __block_literal_global.553
- __block_literal_global.555
- __handleShareAllLocationsChanged_block_invoke.1005
- _kSMSuggestionsMetricEventWorkoutAlwaysPromptConsideredCountKey
- _kSMSuggestionsMetricEventWorkoutAlwaysPromptConsideredSettingStateKey
- _kSMSuggestionsMetricEventWorkoutAlwaysPromptLastWorkoutTypeKey
- _kSMSuggestionsMetricEventWorkoutAlwaysPromptResponseKey
- _objc_msgSend$SessionHandoffRebootReconciliationDecisionToString:
- _objc_msgSend$SessionHandoffRebootReconciliationStateToString:
- _objc_msgSend$_canonicalHandleMapFromHandles:
- _objc_msgSend$_canonicalizeHandles:
- _objc_msgSend$_clearActiveSessionDetailsTimeoutTimer
- _objc_msgSend$_computeWorkoutAlwaysPromptMetricsWithError:
- _objc_msgSend$_createDestinationMetricDictionary
- _objc_msgSend$_evaluateHandoffRebootReconciliationState:
- _objc_msgSend$_fetchSOSReceiversWithCompletion:
- _objc_msgSend$_handleTransitionToStateAfterBootstrap:isActiveDevice:
- _objc_msgSend$_isActiveSessionDetailsFetchAttemptFailed
- _objc_msgSend$_isActiveSessionDetailsOutOfSync
- _objc_msgSend$_isCellularActivated
- _objc_msgSend$_isEligibleToSendStateUpdateReqMessageAfterBootstrap:isActiveDevice:
- _objc_msgSend$_isLocalStateInSyncWithActiveSessionDetails:deviceSessionManagerState:
- _objc_msgSend$_isMultiDeviceSetupForLocalState:
- _objc_msgSend$_isStandalone
- _objc_msgSend$_notifyObserversForActiveSessionDetailsFetchAttemptedFromCKCompleted:success:error:
- _objc_msgSend$_onActiveSessionDetailsFetchAttemptFromCKCompleted:success:error:
- _objc_msgSend$_onActiveSessionDetailsTimeoutTimerExpiry
- _objc_msgSend$_reconciliationDecisionForState:isActiveDevice:
- _objc_msgSend$_reconciliationForDecisionForCKFetchCompleted:
- _objc_msgSend$_resetPendingSendSessionEndMessage
- _objc_msgSend$_saveLatestActiveSessionDetailsStateToDefaults:
- _objc_msgSend$_setPendingSendSessionEndMessageWithReason:associatedGUID:
- _objc_msgSend$_startActiveSessionDetailsTimerWithLatency:
- _objc_msgSend$_stateValidForSendSessionEndMessageRetry:
- _objc_msgSend$_submitWorkoutAlwaysPromptResponseMetricUponNotification:
- _objc_msgSend$_updateSessionWithConversation:sosReceivers:handler:
- _objc_msgSend$activeSessionDetails
- _objc_msgSend$canonicalIDSIDsForAddress:
- _objc_msgSend$canonicalizedHandle
- _objc_msgSend$conversationFromHandlesInConversation1:canonicallyIntersectedWithHandlesInConversation2:
- _objc_msgSend$conversationFromHandlesInConversation1:canonicallyMappedToHandlesInConversation2:
- _objc_msgSend$didHandoffOccur
- _objc_msgSend$didWorkoutEnd
- _objc_msgSend$didWorkoutPause
- _objc_msgSend$earliestActiveDeviceIdentifier
- _objc_msgSend$fetchSOSReceiversWithCompletion:
- _objc_msgSend$handlesInConversation1:canonicallyEqualsHandlesInConversation2:
- _objc_msgSend$handoffRebootReconciliationState
- _objc_msgSend$initDestinationBoundSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:
- _objc_msgSend$initRoundTripSessionConfigurationWithConversation:sessionID:destination:sessionStartDate:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:
- _objc_msgSend$initTimeBoundSessionConfigurationWithConversation:sessionID:time:sessionStartDate:sessionSupportsHandoff:sosReceivers:
- _objc_msgSend$initTimeBoundSessionConfigurationWithConversation:sessionID:time:sessionSupportsHandoff:sosReceivers:
- _objc_msgSend$initWithBatchSize:fetchLimit:sortByCreationDate:ascending:dateInterval:sessionState:locationBoundingBox:boundingBoxRadius:sessionIdentifier:
- _objc_msgSend$initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:
- _objc_msgSend$initWithDefaultQos:masqueradeBundleID:xpcActivity:
- _objc_msgSend$initWithDefaultsManager:learnedLocationManager:sessionStore:locationManager:currentDeviceIdentifier:
- _objc_msgSend$initWithIdentifier:conversation:shouldBeCleanedUpDate:cloudkitShareZoneCleanedUpSuccessfully:syncDate:keyReleaseMessageSendDate:scheduledSendExpiryDate:phoneCache:watchCache:sessionID:safetyCacheKey:allowReadToken:scheduleSendMessageGUID:unlockLocation:lockLocation:startingLocation:offWristLocation:parkedCarLocation:destinationMapItem:timeCacheUploadCompletion:maxCacheSize:maxLocationsInTrace:maxTimeBetweenCacheUpdates:numCacheUpdates:timeTilCacheRelease:numberOfSuccessfulCacheUpdates:numberOfMessageCancelling:numberOfSuccessfulMessageCancelling:numberOfMessageScheduling:numberOfSuccessfulMessageScheduling:wasCacheReleased:wasScheduledSendTriggered:locationOfTrigger:triggerDate:lockState:cacheUpdateBackstopExpiryDate:workoutEvents:numberOfHandoffBecomingActive:numberOfHandoffBecomingNonActive:earliestActiveDeviceIdentifier:latestActiveDeviceIdentifier:
- _objc_msgSend$initWithLearnedLocationManager:locationManager:motionActivityManager:tripSegmentInertialDataManager:inertialOdometryManager:vehicleStore:tripSegmentManager:elevationAdjuster:distanceCalculator:defaultsManager:visitManager:
- _objc_msgSend$initWithTripSegmentID:isFinalPart:modeOfTransport:tripLocations:startTripLocation:stopTripLocation:inertialOdometryData:
- _objc_msgSend$initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:
- _objc_msgSend$isEffectivePairedDeviceNearby
- _objc_msgSend$latestActiveDeviceIdentifier
- _objc_msgSend$managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:managedObject:managedObjectContext:
- _objc_msgSend$masqueradeBundleID
- _objc_msgSend$numAnomalyPrompt
- _objc_msgSend$numAnomalyPromptDuringHysteresis
- _objc_msgSend$numHandoff
- _objc_msgSend$numLPMSeparation
- _objc_msgSend$numRecipients
- _objc_msgSend$numTakeover
- _objc_msgSend$numUnsupportedDeviceSeparation
- _objc_msgSend$numUserDisabledConnectivity
- _objc_msgSend$numberOfHandoffBecomingActive
- _objc_msgSend$numberOfHandoffBecomingNonActive
- _objc_msgSend$onActiveSessionDetailsFetchAttemptFromCKCompleted:success:error:
- _objc_msgSend$onSessionTerminatedWithReason:
- _objc_msgSend$onUnsupportedDeviceSeparation
- _objc_msgSend$processSessionTypeKeyRelease:
- _objc_msgSend$receivedSessionTypeKeyRelease:fromHandle:fromMe:
- _objc_msgSend$remoteStatusTimeoutTimer
- _objc_msgSend$setActiveSessionDetails:
- _objc_msgSend$setCompletedInitialWifiScan:
- _objc_msgSend$setDidHandoffOccur:
- _objc_msgSend$setDidWorkoutEnd:
- _objc_msgSend$setDidWorkoutPause:
- _objc_msgSend$setEarliestActiveDeviceIdentifier:
- _objc_msgSend$setHandoffRebootReconciliationState:
- _objc_msgSend$setLatestActiveDeviceIdentifier:
- _objc_msgSend$setNumAnomalyPrompt:
- _objc_msgSend$setNumAnomalyPromptDuringHysteresis:
- _objc_msgSend$setNumHandoff:
- _objc_msgSend$setNumLPMSeparation:
- _objc_msgSend$setNumRecipients:
- _objc_msgSend$setNumTakeover:
- _objc_msgSend$setNumUnsupportedDeviceSeparation:
- _objc_msgSend$setNumUserDisabledConnectivity:
- _objc_msgSend$setNumberOfHandoffBecomingActive:
- _objc_msgSend$setNumberOfHandoffBecomingNonActive:
- _objc_msgSend$setRemoteStatusTimeoutTimer:
- _objc_msgSend$setSosReceivers:
- _objc_msgSend$setWasActiveAtEnd:
- _objc_msgSend$setWasActiveAtStart:
- _objc_msgSend$setWorkoutActivityTypeString:
- _objc_msgSend$sosReceivers
- _objc_msgSend$wasActiveAtEnd
- _objc_msgSend$wasActiveAtStart
CStrings:
+ "-[SMSessionManager _checkIfHandoffCriteriaSatisfiedForState:handler:]_block_invoke_2"
+ "-[SMSessionManager _updateStateMetaDataTo:]"
+ "07:00:50"
+ "Jun 15 2024"
+ "RTDefaultsSafetyCacheActiveSessionDetailsDateKey"
- "+[SMMessagingUtilities _canonicalHandleMapFromHandles:]"
- "+[SMMessagingUtilities _canonicalizeHandles:]"
- "+[SMMessagingUtilities conversationFromHandlesInConversation1:canonicallyIntersectedWithHandlesInConversation2:]"
- "+[SMMessagingUtilities conversationFromHandlesInConversation1:canonicallyMappedToHandlesInConversation2:]"
- "+[SMMessagingUtilities handlesInConversation1:canonicallyEqualsHandlesInConversation2:]"
- "-[RTIntermittentGNSSManager _completeRemoteStatusChecklistItem:]"
- "-[RTIntermittentGNSSManager fetchRemoteStatusWithHandler:]_block_invoke"
- "-[RTIntermittentGNSSManager fetchRemoteStatusWithHandler:]_block_invoke_2"
- "-[SMActiveSessionZone _addObserver:]"
- "-[SMActiveSessionZone _notifyObserversForActiveSessionDetailsFetchAttemptedFromCKCompleted:success:error:]"
- "-[SMActiveSessionZone _onActiveSessionDetailsFetchAttemptFromCKCompleted:success:error:]"
- "-[SMActiveSessionZone _removeObserver:]"
- "-[SMSessionManager _checkIfHandoffCriteriaSatisfiedForState:handler:]_block_invoke"
- "-[SMSessionManager _evaluateHandoffRebootReconciliationState:]"
- "-[SMSessionManager _evaluateHandoffRebootReconciliationState:]_block_invoke"
- "-[SMSessionManager _handleTransitionToStateAfterBootstrap:isActiveDevice:]"
- "-[SMSessionManager _handleTransitionToStateAfterBootstrap:isActiveDevice:]_block_invoke"
- "-[SMSessionManager _isActiveSessionDetailsFetchAttemptFailed]"
- "-[SMSessionManager _isActiveSessionDetailsFetchedFromCloudKitSinceBoot]"
- "-[SMSessionManager _isActiveSessionDetailsLocalRecordExpired]"
- "-[SMSessionManager _isActiveSessionDetailsOutOfSync]"
- "-[SMSessionManager _isLocalStateInSyncWithActiveSessionDetails:deviceSessionManagerState:]"
- "-[SMSessionManager _onActiveSessionDetailsFetchAttemptFromCKCompleted:success:error:]"
- "-[SMSessionManager _onActiveSessionDetailsTimeoutTimerExpiry]"
- "-[SMSessionManager _reconciliationDecisionForState:isActiveDevice:]"
- "-[SMSessionManager _resetPendingSendSessionEndMessage]"
- "-[SMSessionManager _setPendingSendSessionEndMessageWithReason:associatedGUID:]"
- "-[SMSessionManager onActiveSessionDetailsFetchAttemptFromCKCompleted:success:error:]"
- "-[SMSessionManager processSessionTypeKeyRelease:]_block_invoke"
- "-[SMSessionMetricManager _gatherSessionDestinationStats:]"
- "-[SMSessionMetricManager _gatherSessionDestinationStats:]_block_invoke"
- "-[SMSessionMetricManager _isCellularActivated]"
- "00:27:04"
- "B24@?0@\"CLBackgroundInertialOdometrySample\"8@\"NSDictionary\"16"
- "FetchCompleted"
- "FetchFailed"
- "Jun 29 2024"
- "LocalState"
- "NotActiveWaitForStateSync"
- "NotValidForSessionResume"
- "RTDefaultsSafetyCacheActiveSessionDetailsFetchFailureDateKey"
- "RTDefaultsSafetyCacheActiveSessionDetailsFetchSuccessDateKey"
- "RTDefaultsSessionManagerHandoffActiveSessionDetailsFetchTimeout"
- "RTDefaultsSessionManagerPendingSendSessionEndMessageAssociatedGUIDKey"
- "RTDefaultsSessionManagerPendingSendSessionEndMessageReasonKey"
- "RTDefaultsSessionMetricManagerDidHandoffOccurKey"
- "RTDefaultsSessionMetricManagerDidWorkoutEndKey"
- "RTDefaultsSessionMetricManagerDidWorkoutPauseKey"
- "RTDefaultsSessionMetricManagerIsWorkoutAlwaysOnKey"
- "RTDefaultsSessionMetricManagerModeOfTransportationKey"
- "RTDefaultsSessionMetricManagerNumAnomalyPromptDuringHysteresisKey"
- "RTDefaultsSessionMetricManagerNumAnomalyPromptKey"
- "RTDefaultsSessionMetricManagerNumHandoffKey"
- "RTDefaultsSessionMetricManagerNumLPMSeparationKey"
- "RTDefaultsSessionMetricManagerNumRecipientsKey"
- "RTDefaultsSessionMetricManagerNumTakeoverKey"
- "RTDefaultsSessionMetricManagerNumUnsupportedDeviceSeparationKey"
- "RTDefaultsSessionMetricManagerNumUserDisabledConnectivityKey"
- "RTDefaultsSessionMetricManagerWasActiveAtEndKey"
- "RTDefaultsSessionMetricManagerWasActiveAtStartKey"
- "RTDefaultsSessionMetricManagerWorkoutActivityTypeStringKey"
- "RTDefaultsTripSegmentUseInertialOdometrySamples"
- "RTIntermittentGNSSFetchRemoteStatusTimeoutTimer"
- "SMHandoffActiveSessionDetailsTimeoutTimerIdentifier"
- "SMSubmitSuggesionsWorkoutAlwaysPromptResponseNotification"
- "SafetyMonitor.promptToAlwaysPromptConsidered"
- "SuggestionsMetricsEventWorkoutAlwaysPromptConsidered"
- "alwaysPromptSettingState"
- "didHandoffOccur"
- "didWorkoutEnd"
- "didWorkoutPause"
- "isActiveAtEnd"
- "isActiveAtStart"
- "isCellularActivated"
- "isStandalone"
- "isWorkoutAlwaysOn"
- "lastWorkoutActivityTypeString"
- "modeOfTransportation"
- "numAnomalyPrompt"
- "numAnomalyPromptDuringHysteresis"
- "numHandoff"
- "numLPMSeparation"
- "numRecipients"
- "numTakeover"
- "numTimesPromptConsidered"
- "numUnsupportedDeviceSeparation"
- "numUserDisabledConnectivity"
- "overriding active session details fech timeout"
- "userResponse"
- "wasActiveAtEnd"
- "wasActiveAtStart"
- "workoutActivityTypeString"

```
