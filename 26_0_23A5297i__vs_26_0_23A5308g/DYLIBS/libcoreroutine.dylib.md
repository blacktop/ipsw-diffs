## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1057.0.0.0.0
-  __TEXT.__text: 0x5e57d0
+1061.0.0.0.0
+  __TEXT.__text: 0x5ec628
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x30b60
+  __TEXT.__objc_methlist: 0x31020
   __TEXT.__const: 0x4640
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x754a8
-  __TEXT.__cstring: 0x44b17
+  __TEXT.__oslogstring: 0x762a0
+  __TEXT.__cstring: 0x45352
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c

   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x282d8
+  __TEXT.__gcc_except_tab: 0x28a28
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xdb58
+  __TEXT.__unwind_info: 0xdc58
   __TEXT.__eh_frame: 0x390
-  __TEXT.__objc_classname: 0x580a
-  __TEXT.__objc_methname: 0x90a43
-  __TEXT.__objc_methtype: 0xcedb
-  __TEXT.__objc_stubs: 0x554a0
-  __DATA_CONST.__got: 0x30b0
-  __DATA_CONST.__const: 0xf608
-  __DATA_CONST.__objc_classlist: 0x1528
+  __TEXT.__objc_classname: 0x58c9
+  __TEXT.__objc_methname: 0x91589
+  __TEXT.__objc_methtype: 0xcf8a
+  __TEXT.__objc_stubs: 0x55a60
+  __DATA_CONST.__got: 0x30f0
+  __DATA_CONST.__const: 0xf4f8
+  __DATA_CONST.__objc_classlist: 0x1548
   __DATA_CONST.__objc_catlist: 0x3a8
-  __DATA_CONST.__objc_protolist: 0x340
+  __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19228
-  __DATA_CONST.__objc_protorefs: 0x120
-  __DATA_CONST.__objc_superrefs: 0x1180
-  __DATA_CONST.__objc_arraydata: 0x2a20
+  __DATA_CONST.__objc_selrefs: 0x19418
+  __DATA_CONST.__objc_protorefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x1198
+  __DATA_CONST.__objc_arraydata: 0x2a08
   __AUTH_CONST.__auth_got: 0x10d8
-  __AUTH_CONST.__const: 0x3220
-  __AUTH_CONST.__cfstring: 0x28600
-  __AUTH_CONST.__objc_const: 0x502b0
-  __AUTH_CONST.__objc_intobj: 0x45d8
+  __AUTH_CONST.__const: 0x3260
+  __AUTH_CONST.__cfstring: 0x287e0
+  __AUTH_CONST.__objc_const: 0x50a70
+  __AUTH_CONST.__objc_intobj: 0x4608
   __AUTH_CONST.__objc_arrayobj: 0xe70
-  __AUTH_CONST.__objc_doubleobj: 0xaf0
+  __AUTH_CONST.__objc_doubleobj: 0xb00
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x2bb8
-  __DATA.__objc_ivar: 0x2544
-  __DATA.__data: 0x2b98
+  __AUTH.__objc_data: 0x2208
+  __DATA.__objc_ivar: 0x2584
+  __DATA.__data: 0x2cc0
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_ivar: 0x1144
-  __DATA_DIRTY.__objc_data: 0xa890
+  __DATA_DIRTY.__objc_ivar: 0x1158
+  __DATA_DIRTY.__objc_data: 0xb380
   __DATA_DIRTY.__data: 0x5c8
   __DATA_DIRTY.__bss: 0x200
   __DATA_DIRTY.__common: 0x8

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed
+  - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics
   - /usr/lib/libAWDSupportFramework.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BE12BFF0-0DD8-3B24-9D5A-D07B2A308DEB
-  Functions: 20070
-  Symbols:   64820
-  CStrings:  39934
+  UUID: 488B7418-652E-3101-ACD3-DDFEFCF74E59
+  Functions: 20178
+  Symbols:   65148
+  CStrings:  40135
 
Symbols:
+ +[RTException coreDataExceptionLogging:]
+ +[RTException unknownExceptionHandlingPolicyDeadInside]
+ +[RTStore evaluatePolicyForCoreDataContextPerformBlockException:]
+ +[SMCheckInRemindersTipResponseMetricManager event]
+ +[SMCheckInRemindersTipResponseMetricManager supportedMetricKeys]
+ +[SMSessionConfigurationMO managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:managedObject:managedObjectContext:]
+ -[RTCurrentWorkoutSnapshot initWithSessionIdentifier:activityType:locationType:swimmingLocationType:sessionType:isFirstPartyWorkout:sessionState:workoutStartDate:snapshotDate:sessionError:]
+ -[RTCurrentWorkoutSnapshot sessionError]
+ -[RTCurrentWorkoutSnapshot sessionType]
+ -[RTHealthKitManager fetchMostRecentWorkoutInfoWithHandler:]
+ -[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:error:]
+ -[RTLearnedLocationEngine _curateVisit:newLabel:relabelerPersister:error:]
+ -[RTLearnedLocationEngine _curateVisits:newLabel:relabelerPersister:error:]
+ -[RTLearnedLocationEngine _updateExpirationDateOfStoredUserCuration:associatedVisits:error:]
+ -[RTLearnedLocationStore _fetchLocationsOfInterestUUIDsVisitedWithHandler:]
+ -[RTLearnedLocationStore fetchLocationsOfInterestUUIDsVisitedWithHandler:]
+ -[RTLearnedPlaceTypeInferenceGenerator _storeMetricsForNonFallbackPlacesWithHome:homeSource:work:workSource:]
+ -[RTLearnedPlaceTypeInferenceGenerator inferWorkFromHistoryAndPlaceStats:]
+ -[RTPlaceTypeClassifierMetricsCalculator fetchWorkInferenceStatsForLookbackDays:handler:]
+ -[RTPredictedContextManager available]
+ -[RTPredictedContextManager dataProtectionManager]
+ -[RTPredictedContextManager initWithFeatureExtractor:learnedLocationManager:platform:activityManager:dataProtectionManager:defaultsManager:visitManager:eventManager:mapServiceManager:mapsSupportManager:navigationManager:motionActivityManager:vehicleLocationProvider:distanceCalculator:predictedContextStore:metricsManager:]
+ -[RTPredictedContextManager onDataProtectionNotification:]
+ -[RTPredictedContextManager setAvailable:]
+ -[RTPredictedContextManager setDataProtectionManager:]
+ -[RTTripSegmentManager _checkForValidAltitudeSpeedAccuracyDefault]
+ -[RTTripSegmentManager checkForValidAltitudeSpeedAccuracy]
+ -[RTTripSegmentManager isValidSynthesizedLocation:]
+ -[RTTripSegmentManager setCheckForValidAltitudeSpeedAccuracy:]
+ -[RTWorkInferenceHistoryStats .cxx_destruct]
+ -[RTWorkInferenceHistoryStats description]
+ -[RTWorkInferenceHistoryStats initWithLearnedPlaceIdentifier:totalInferences:workInferences:lastDateInferred:]
+ -[RTWorkInferenceHistoryStats lastDateInferred]
+ -[RTWorkInferenceHistoryStats learnedPlaceIdentifier]
+ -[RTWorkInferenceHistoryStats totalInferences]
+ -[RTWorkInferenceHistoryStats workInferences]
+ -[SMCMOdometer .cxx_destruct]
+ -[SMCMOdometer init]
+ -[SMCMOdometer odometer:didUpdateGpsAvailability:]
+ -[SMCMOdometer odometer]
+ -[SMCMOdometer startOdometerUpdatesForActivity:withHandler:]
+ -[SMCMOdometer stopOdometerUpdates]
+ -[SMCheckInRemindersTipResponseMetricManager .cxx_destruct]
+ -[SMCheckInRemindersTipResponseMetricManager defaultsManager]
+ -[SMCheckInRemindersTipResponseMetricManager init]
+ -[SMCheckInRemindersTipResponseMetricManager mostRecentResponse]
+ -[SMCheckInRemindersTipResponseMetricManager resetMetrics]
+ -[SMCheckInRemindersTipResponseMetricManager setDefaultsManager:]
+ -[SMCheckInRemindersTipResponseMetricManager startMetricsCollection]
+ -[SMCheckInRemindersTipResponseMetricManager submitMetricsWithError:]
+ -[SMCheckInRemindersTipResponseMetricManager updateTipResponse:]
+ -[SMDaemonClient respondedToCheckInRemindersTipWithResponse:]
+ -[SMDaemonClient startCheckInRemindersTipMetricsCollection]
+ -[SMEmergencyCallManager .cxx_destruct]
+ -[SMEmergencyCallManager _addObserver:]
+ -[SMEmergencyCallManager _isEmergencyCallOngoing]
+ -[SMEmergencyCallManager _notifyObserversForEmergencyCallEnded]
+ -[SMEmergencyCallManager _notifyObserversForEmergencyCallStarted]
+ -[SMEmergencyCallManager _onTUCallCenterCallStatusChangedNotification:]
+ -[SMEmergencyCallManager _removeObserver:]
+ -[SMEmergencyCallManager _setup]
+ -[SMEmergencyCallManager addObserver:]
+ -[SMEmergencyCallManager callCenter]
+ -[SMEmergencyCallManager fetchIsEmergencyCallOngoingWithHandler:]
+ -[SMEmergencyCallManager init]
+ -[SMEmergencyCallManager observers]
+ -[SMEmergencyCallManager onTUCallCenterCallStatusChangedNotification:]
+ -[SMEmergencyCallManager queue]
+ -[SMEmergencyCallManager removeObserver:]
+ -[SMEmergencyCallManager setCallCenter:]
+ -[SMEmergencyCallManager setObservers:]
+ -[SMEmergencyCallManager setup]
+ -[SMInitiatorService _onEmergencyCallEnded]
+ -[SMInitiatorService _onEmergencyCallStarted]
+ -[SMInitiatorService _tearDownWorkoutEndedBufferTimer]
+ -[SMInitiatorService emergencyCallManager]
+ -[SMInitiatorService initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:emergencyCallManager:]
+ -[SMInitiatorService initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:sessionManager:sessionMonitor:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:emergencyCallManager:]
+ -[SMInitiatorService isEmergencyCallOngoing]
+ -[SMInitiatorService onEmergencyCallEnded]
+ -[SMInitiatorService onEmergencyCallStarted]
+ -[SMInitiatorService setEmergencyCallManager:]
+ -[SMInitiatorService setIsEmergencyCallOngoing:]
+ -[SMInitiatorService setTipResponseMetricManager:]
+ -[SMInitiatorService tipResponseMetricManager]
+ -[SMSessionManager _onEmergencyCallEnded]
+ -[SMSessionManager _onEmergencyCallStarted]
+ -[SMSessionManager _setUpWorkoutTimeouts]
+ -[SMSessionManager _setupWorkoutTimeoutWithFireDate:]
+ -[SMSessionManager _tearDownWorkoutTimeouts]
+ -[SMSessionManager _updateSessionWithWorkoutSnapshot:handler:]
+ -[SMSessionManager emergencyCallManager]
+ -[SMSessionManager initWithAuthorizationManager:biomeManager:contactsManager:defaultsManager:locationManager:platform:sessionMetricManager:sessionStore:messagingService:carPlayAlertManager:observers:activeSessionDetailsDelegate:wristStateManager:appDeletionManager:healthKitManager:emergencyCallManager:]
+ -[SMSessionManager isEmergencyCallOngoing]
+ -[SMSessionManager onEmergencyCallEnded]
+ -[SMSessionManager onEmergencyCallStarted]
+ -[SMSessionManager setEmergencyCallManager:]
+ -[SMSessionManager setIsEmergencyCallOngoing:]
+ -[SMSessionManager setWorkoutTimeoutXPCTimerAlarm:]
+ -[SMSessionManager workoutTimeoutXPCTimerAlarm]
+ -[SMSessionWorkoutMonitor checkIfCurrentWorkoutIsOutdoorPedestrianWithHandler:]
+ -[SMSessionWorkoutMonitor cmOdometer]
+ -[SMSessionWorkoutMonitor initializeTimersOnStartMonitoring:]
+ -[SMSessionWorkoutMonitor outdoorPedAutoPauseDistanceThreshold]
+ -[SMSessionWorkoutMonitor outdoorPedAutoPauseDistance]
+ -[SMSessionWorkoutMonitor setCmOdometer:]
+ -[SMSessionWorkoutMonitor setOutdoorPedAutoPauseDistance:]
+ -[SMSessionWorkoutMonitor setOutdoorPedAutoPauseDistanceThreshold:]
+ -[SMSessionWorkoutMonitor takeOdometerDistanceSampleWithHandler:]
+ GCC_except_table125
+ GCC_except_table166
+ GCC_except_table180
+ GCC_except_table190
+ GCC_except_table198
+ GCC_except_table216
+ GCC_except_table266
+ GCC_except_table277
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table287
+ GCC_except_table291
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table300
+ GCC_except_table311
+ GCC_except_table343
+ GCC_except_table406
+ GCC_except_table421
+ GCC_except_table429
+ _OBJC_CLASS_$_CMOdometer
+ _OBJC_CLASS_$_RTWorkInferenceHistoryStats
+ _OBJC_CLASS_$_SMCMOdometer
+ _OBJC_CLASS_$_SMCheckInRemindersTipResponseMetricManager
+ _OBJC_CLASS_$_SMEmergencyCallManager
+ _OBJC_CLASS_$_TUCall
+ _OBJC_CLASS_$_TUCallCenter
+ _OBJC_IVAR_$_RTCurrentWorkoutSnapshot._sessionError
+ _OBJC_IVAR_$_RTCurrentWorkoutSnapshot._sessionType
+ _OBJC_IVAR_$_RTPredictedContextManager._available
+ _OBJC_IVAR_$_RTWorkInferenceHistoryStats._lastDateInferred
+ _OBJC_IVAR_$_RTWorkInferenceHistoryStats._learnedPlaceIdentifier
+ _OBJC_IVAR_$_RTWorkInferenceHistoryStats._totalInferences
+ _OBJC_IVAR_$_RTWorkInferenceHistoryStats._workInferences
+ _OBJC_IVAR_$_SMCMOdometer._odometer
+ _OBJC_IVAR_$_SMCheckInRemindersTipResponseMetricManager._defaultsManager
+ _OBJC_IVAR_$_SMEmergencyCallManager._callCenter
+ _OBJC_IVAR_$_SMEmergencyCallManager._observers
+ _OBJC_IVAR_$_SMEmergencyCallManager._queue
+ _OBJC_IVAR_$_SMSessionManager._emergencyCallManager
+ _OBJC_IVAR_$_SMSessionManager._isEmergencyCallOngoing
+ _OBJC_IVAR_$_SMSessionManager._workoutTimeoutXPCTimerAlarm
+ _OBJC_IVAR_$_SMSessionWorkoutMonitor._cmOdometer
+ _OBJC_IVAR_$_SMSessionWorkoutMonitor._outdoorPedAutoPauseDistance
+ _OBJC_IVAR_$_SMSessionWorkoutMonitor._outdoorPedAutoPauseDistanceThreshold
+ _OBJC_METACLASS_$_RTWorkInferenceHistoryStats
+ _OBJC_METACLASS_$_SMCMOdometer
+ _OBJC_METACLASS_$_SMCheckInRemindersTipResponseMetricManager
+ _OBJC_METACLASS_$_SMEmergencyCallManager
+ _RTAnalyticsEventSafetyMonitorInitiatorFitnessTipResponse
+ _RTPersistenceOperationsErrorDomain
+ _TUCallCenterCallStatusChangedNotification
+ __OBJC_$_CLASS_METHODS_SMCheckInRemindersTipResponseMetricManager
+ __OBJC_$_INSTANCE_METHODS_RTWorkInferenceHistoryStats
+ __OBJC_$_INSTANCE_METHODS_SMCMOdometer
+ __OBJC_$_INSTANCE_METHODS_SMCheckInRemindersTipResponseMetricManager
+ __OBJC_$_INSTANCE_METHODS_SMEmergencyCallManager
+ __OBJC_$_INSTANCE_VARIABLES_RTWorkInferenceHistoryStats
+ __OBJC_$_INSTANCE_VARIABLES_SMCMOdometer
+ __OBJC_$_INSTANCE_VARIABLES_SMCheckInRemindersTipResponseMetricManager
+ __OBJC_$_INSTANCE_VARIABLES_SMEmergencyCallManager
+ __OBJC_$_PROP_LIST_RTWorkInferenceHistoryStats
+ __OBJC_$_PROP_LIST_SMCMOdometer
+ __OBJC_$_PROP_LIST_SMCheckInRemindersTipResponseMetricManager
+ __OBJC_$_PROP_LIST_SMEmergencyCallManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CMOdometerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SMEmergencyCallObserverProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SMInitiatorMetricsProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CMOdometerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SMEmergencyCallObserverProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SMInitiatorMetricsProtocol
+ __OBJC_$_PROTOCOL_REFS_CMOdometerDelegate
+ __OBJC_$_PROTOCOL_REFS_SMEmergencyCallObserverProtocol
+ __OBJC_CLASS_PROTOCOLS_$_SMCMOdometer
+ __OBJC_CLASS_PROTOCOLS_$_SMCheckInRemindersTipResponseMetricManager
+ __OBJC_CLASS_RO_$_RTWorkInferenceHistoryStats
+ __OBJC_CLASS_RO_$_SMCMOdometer
+ __OBJC_CLASS_RO_$_SMCheckInRemindersTipResponseMetricManager
+ __OBJC_CLASS_RO_$_SMEmergencyCallManager
+ __OBJC_LABEL_PROTOCOL_$_CMOdometerDelegate
+ __OBJC_LABEL_PROTOCOL_$_SMEmergencyCallObserverProtocol
+ __OBJC_LABEL_PROTOCOL_$_SMInitiatorMetricsProtocol
+ __OBJC_METACLASS_RO_$_RTWorkInferenceHistoryStats
+ __OBJC_METACLASS_RO_$_SMCMOdometer
+ __OBJC_METACLASS_RO_$_SMCheckInRemindersTipResponseMetricManager
+ __OBJC_METACLASS_RO_$_SMEmergencyCallManager
+ __OBJC_PROTOCOL_$_CMOdometerDelegate
+ __OBJC_PROTOCOL_$_SMEmergencyCallObserverProtocol
+ __OBJC_PROTOCOL_$_SMInitiatorMetricsProtocol
+ __OBJC_PROTOCOL_REFERENCE_$_SMInitiatorMetricsProtocol
+ ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.409
+ ___25-[RTDaemonClient restore]_block_invoke.748
+ ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.265
+ ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.266
+ ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.267
+ ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.271
+ ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.272
+ ___27-[RTLifeCycleManager _exit]_block_invoke.720
+ ___27-[RTLifeCycleManager _exit]_block_invoke.726
+ ___27-[RTLifeCycleManager _exit]_block_invoke.728
+ ___27-[RTLifeCycleManager _exit]_block_invoke.729
+ ___27-[RTLifeCycleManager _exit]_block_invoke_2.727
+ ___28-[RTHealthKitManager _setup]_block_invoke.625
+ ___28-[RTLifeCycleManager _start]_block_invoke.705
+ ___28-[RTLifeCycleManager _start]_block_invoke.711
+ ___28-[RTLifeCycleManager _start]_block_invoke.714
+ ___28-[RTLifeCycleManager _start]_block_invoke.717
+ ___31-[SMEmergencyCallManager setup]_block_invoke
+ ___32-[SMEmergencyCallManager _setup]_block_invoke
+ ___38-[SMEmergencyCallManager addObserver:]_block_invoke
+ ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.189
+ ___40-[SMSessionManager onEmergencyCallEnded]_block_invoke
+ ___41-[RTAssetManager _downloadAsset:handler:]_block_invoke.362
+ ___41-[SMEmergencyCallManager removeObserver:]_block_invoke
+ ___41-[SMSessionManager _handleMagnetConnect:]_block_invoke.548
+ ___42-[SMInitiatorService onEmergencyCallEnded]_block_invoke
+ ___42-[SMSessionManager onEmergencyCallStarted]_block_invoke
+ ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.726
+ ___43-[RTPredictedContextManager _storeRequest:]_block_invoke.487
+ ___436+[SMSessionConfigurationMO managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:managedObject:managedObjectContext:]_block_invoke
+ ___44-[SMInitiatorService onEmergencyCallStarted]_block_invoke
+ ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.192
+ ___47-[RTLearnedLocationStore _removePlace:handler:]_block_invoke.431
+ ___47-[SMClientListener _setupConnection:forClient:]_block_invoke.283
+ ___48-[RTFeatureExtractor _getHomeKitHomesWithError:]_block_invoke.437
+ ___49-[RTTripSegmentManager isOKToAddTripSegmentdata:]_block_invoke.251
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.153
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.155
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.157
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.159
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.161
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.154
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.156
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.158
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.160
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.173
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.182
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.185
+ ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.772
+ ___52-[SMSessionManager _onHealthKitManagerNotification:]_block_invoke
+ ___52-[SMSessionManager _onHealthKitManagerNotification:]_block_invoke.568
+ ___52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.689
+ ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.480
+ ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.483
+ ___53-[SMSessionManager _setupWorkoutTimeoutWithFireDate:]_block_invoke
+ ___53-[SMSessionManager _setupWorkoutTimeoutWithFireDate:]_block_invoke_2
+ ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.670
+ ___55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.558
+ ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.130
+ ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.132
+ ___57-[SMSessionMetricManager _gatherSessionDestinationStats:]_block_invoke.681
+ ___58-[RTFeatureExtractor _getVisitsWithDateInterval:outError:]_block_invoke.417
+ ___58-[RTPredictedContextManager _evaluateTrainErrorForResult:]_block_invoke.164
+ ___58-[RTPredictedContextManager onDataProtectionNotification:]_block_invoke
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.489
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.496
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.500
+ ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.838
+ ___59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.588
+ ___59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.584
+ ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.273
+ ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.274
+ ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.275
+ ___59-[SMDaemonClient startCheckInRemindersTipMetricsCollection]_block_invoke
+ ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.581
+ ___60-[RTHealthKitManager fetchMostRecentWorkoutInfoWithHandler:]_block_invoke
+ ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.179
+ ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.183
+ ___60-[SMSessionWorkoutMonitor _onTimerExpiryForTimerIdentifier:]_block_invoke
+ ___60-[SMSessionWorkoutMonitor _onTimerExpiryForTimerIdentifier:]_block_invoke_2
+ ___61-[SMDaemonClient respondedToCheckInRemindersTipWithResponse:]_block_invoke
+ ___61-[SMSessionWorkoutMonitor initializeTimersOnStartMonitoring:]_block_invoke
+ ___62-[RTDaemonClientInternal connection:handleInvocation:isReply:]_block_invoke.494
+ ___63-[RTFeatureExtractor _getTransitionsWithDateInterval:outError:]_block_invoke.419
+ ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.689
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.296
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.301
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.304
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.307
+ ___65-[RTTripSegmentManager _purgeTripSegmentsOnDateInterval:handler:]_block_invoke.283
+ ___65-[RTTripSegmentManager _purgeTripSegmentsOnDateInterval:handler:]_block_invoke.284
+ ___65-[SMEmergencyCallManager fetchIsEmergencyCallOngoingWithHandler:]_block_invoke
+ ___65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.207
+ ___65-[SMSessionWorkoutMonitor takeOdometerDistanceSampleWithHandler:]_block_invoke
+ ___66-[RTFeatureExtractor _getCalendarEventsWithDateInterval:outError:]_block_invoke.426
+ ___66-[RTLearnedLocationStore _fetchMapItemWithMuid:predicate:handler:]_block_invoke.410
+ ___66-[RTLearnedLocationStore _removeRecordsExpiredBeforeDate:handler:]_block_invoke.523
+ ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.737
+ ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.108
+ ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.118
+ ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke_2.113
+ ___68-[RTFeatureExtractor _getMapsViewedPlacesWithDateInterval:outError:]_block_invoke.431
+ ___68-[RTFeatureExtractor _getMotionActivitiesWithDateInterval:outError:]_block_invoke.433
+ ___68-[RTLearnedLocationStore _fetchLocationOfInterestWithPlace:handler:]_block_invoke.377
+ ___69-[RTDaemonClient remoteStatusRegistrar:didReceiveRemoteStatus:error:]_block_invoke.773
+ ___69-[RTFeatureExtractor _getLocationHistoriesWithDateInterval:outError:]_block_invoke.424
+ ___69-[RTPredictedContextManager _rescheduleActivityTrainWithTrainPolicy:]_block_invoke.165
+ ___69-[RTTripSegmentManager _fetchTripSegmentMetadataWithOptions:handler:]_block_invoke.234
+ ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.764
+ ___70-[RTLearnedLocationStore _fetchLocationOfInterestWithMapItem:handler:]_block_invoke.373
+ ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.291
+ ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.296
+ ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.297
+ ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.298
+ ___70-[SMEmergencyCallManager onTUCallCenterCallStatusChangedNotification:]_block_invoke
+ ___71-[RTFeatureExtractor _getLocationsOfInterestWithDateInterval:outError:]_block_invoke.421
+ ___71-[SMEmergencyCallManager _onTUCallCenterCallStatusChangedNotification:]_block_invoke
+ ___71-[SMEmergencyCallManager _onTUCallCenterCallStatusChangedNotification:]_block_invoke.10
+ ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.512
+ ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.749
+ ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.554
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.463
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.467
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.478
+ ___73-[RTLearnedLocationStore _fetchLocationOfInterestVisitedLastWithHandler:]_block_invoke.368
+ ___73-[RTLearnedLocationStore _fetchLocationOfInterestWithIdentifier:handler:]_block_invoke.369
+ ___74-[RTLearnedLocationEngine _curateVisit:newLabel:relabelerPersister:error:]_block_invoke
+ ___74-[RTLearnedLocationStore _fetchInferredMapItemForVisitIdentifier:handler:]_block_invoke.366
+ ___74-[RTLearnedLocationStore _fetchLocationOfInterestVisitedFirstWithHandler:]_block_invoke.367
+ ___74-[RTLearnedLocationStore fetchLocationsOfInterestUUIDsVisitedWithHandler:]_block_invoke
+ ___74-[RTLearnedPlaceTypeInferenceGenerator inferWorkFromHistoryAndPlaceStats:]_block_invoke
+ ___75-[RTLearnedLocationStore _fetchLocationsOfInterestUUIDsVisitedWithHandler:]_block_invoke
+ ___75-[RTLearnedLocationStore _fetchLocationsOfInterestUUIDsVisitedWithHandler:]_block_invoke.345
+ ___76-[RTAssetManager initWithDefaultsManager:assetProcessor:xpcActivityManager:]_block_invoke.301
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.732
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.733
+ ___77-[RTFeatureExtractor _getMapsHistoricalNavigationsWithDateInterval:outError:]_block_invoke.429
+ ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.608
+ ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.768
+ ___79-[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]_block_invoke.801
+ ___79-[SMSessionWorkoutMonitor checkIfCurrentWorkoutIsOutdoorPedestrianWithHandler:]_block_invoke
+ ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.721
+ ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.740
+ ___83-[RTDaemonClient predictedContextRegistrar:didReceivePredictedContextResult:error:]_block_invoke.812
+ ___86-[RTLearnedLocationStore _fetchVisitsWithIncompletePlacesForCurrentDeviceWithHandler:]_block_invoke.403
+ ___87-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:error:]_block_invoke
+ ___89-[RTPlaceTypeClassifierMetricsCalculator fetchWorkInferenceStatsForLookbackDays:handler:]_block_invoke
+ ___91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.559
+ ___92-[RTLearnedLocationEngine _updateExpirationDateOfStoredUserCuration:associatedVisits:error:]_block_invoke
+ ___94-[RTLearnedLocationStore _fetchLocationOfInterestTransitionsBetweenStartDate:endDate:handler:]_block_invoke.390
+ ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.676
+ ___block_descriptor_197_e8_32s40s48s56s64s72s80s88s96s104r_e5_v8?0lr104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_40_e8_32s_e18_v16?0"NSNumber"8ls32l8
+ ___block_descriptor_41_e8_32s_e46_v24?0"RTCurrentWorkoutSnapshot"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32bs40w_e36_v24?0"CMOdometerData"8"NSError"16lw40l8s32l8
+ ___block_descriptor_64_e8_32s40s48w_e39_v24?0"CMWorkoutSnapshot"8"NSError"16lw48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e22_v32?0"NSUUID"8Q16q24ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_80_e8_32s40r48r56r64r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48r56r64r_e46_v24?0"RTCurrentWorkoutSnapshot"8"NSError"16lr48l8r56l8r64l8s32l8s40l8
+ ___block_literal_global.1251
+ ___block_literal_global.1376
+ ___block_literal_global.1389
+ ___block_literal_global.175
+ ___block_literal_global.177
+ ___block_literal_global.179
+ ___block_literal_global.181
+ ___block_literal_global.184
+ ___block_literal_global.187
+ ___block_literal_global.191
+ ___block_literal_global.326
+ ___block_literal_global.361
+ ___block_literal_global.396
+ ___block_literal_global.432
+ ___block_literal_global.456
+ ___block_literal_global.561
+ ___block_literal_global.573
+ ___block_literal_global.613
+ ___block_literal_global.647
+ ___block_literal_global.682
+ ___block_literal_global.691
+ ___block_literal_global.708
+ ___block_literal_global.713
+ ___block_literal_global.716
+ ___block_literal_global.719
+ ___block_literal_global.731
+ ___block_literal_global.742
+ ___block_literal_global.750
+ ___block_literal_global.907
+ ___block_literal_global.910
+ ___block_literal_global.971
+ _objc_msgSend$_applyUserCuration:relabelerPersister:harvestCuration:error:
+ _objc_msgSend$_checkForValidAltitudeSpeedAccuracyDefault
+ _objc_msgSend$_curateVisit:newLabel:relabelerPersister:error:
+ _objc_msgSend$_curateVisits:newLabel:relabelerPersister:error:
+ _objc_msgSend$_fetchLocationsOfInterestUUIDsVisitedWithHandler:
+ _objc_msgSend$_isEmergencyCallOngoing
+ _objc_msgSend$_notifyObserversForEmergencyCallEnded
+ _objc_msgSend$_notifyObserversForEmergencyCallStarted
+ _objc_msgSend$_onEmergencyCallEnded
+ _objc_msgSend$_onEmergencyCallStarted
+ _objc_msgSend$_onTUCallCenterCallStatusChangedNotification:
+ _objc_msgSend$_setUpWorkoutTimeouts
+ _objc_msgSend$_setupWorkoutTimeoutWithFireDate:
+ _objc_msgSend$_storeMetricsForNonFallbackPlacesWithHome:homeSource:work:workSource:
+ _objc_msgSend$_tearDownWorkoutEndedBufferTimer
+ _objc_msgSend$_tearDownWorkoutTimeouts
+ _objc_msgSend$_updateExpirationDateOfStoredUserCuration:associatedVisits:error:
+ _objc_msgSend$_updateSessionWithWorkoutSnapshot:handler:
+ _objc_msgSend$callCenterWithQueue:
+ _objc_msgSend$checkIfCurrentWorkoutIsOutdoorPedestrianWithHandler:
+ _objc_msgSend$cmOdometer
+ _objc_msgSend$coreDataExceptionLogging:
+ _objc_msgSend$currentCalls
+ _objc_msgSend$evaluatePolicyForCoreDataContextPerformBlockException:
+ _objc_msgSend$fetchLocationsOfInterestUUIDsVisitedWithHandler:
+ _objc_msgSend$fetchMostRecentWorkoutInfoWithHandler:
+ _objc_msgSend$fetchWorkInferenceStatsForLookbackDays:handler:
+ _objc_msgSend$hasMapItemStorage
+ _objc_msgSend$inferWorkFromHistoryAndPlaceStats:
+ _objc_msgSend$initWithAuthorizationManager:biomeManager:contactsManager:defaultsManager:locationManager:platform:sessionMetricManager:sessionStore:messagingService:carPlayAlertManager:observers:activeSessionDetailsDelegate:wristStateManager:appDeletionManager:healthKitManager:emergencyCallManager:
+ _objc_msgSend$initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:
+ _objc_msgSend$initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:emergencyCallManager:
+ _objc_msgSend$initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:sessionManager:sessionMonitor:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:emergencyCallManager:
+ _objc_msgSend$initWithFeatureExtractor:learnedLocationManager:platform:activityManager:dataProtectionManager:defaultsManager:visitManager:eventManager:mapServiceManager:mapsSupportManager:navigationManager:motionActivityManager:vehicleLocationProvider:distanceCalculator:predictedContextStore:metricsManager:
+ _objc_msgSend$initWithHealthStore:reportInactiveSessions:
+ _objc_msgSend$initWithLearnedPlaceIdentifier:totalInferences:workInferences:lastDateInferred:
+ _objc_msgSend$initWithSessionIdentifier:activityType:locationType:swimmingLocationType:sessionType:isFirstPartyWorkout:sessionState:workoutStartDate:snapshotDate:sessionError:
+ _objc_msgSend$initWithSessionIdentifier:activityType:sessionType:isWorkoutOngoing:isFirstPartyWorkout:
+ _objc_msgSend$initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:
+ _objc_msgSend$initializeTimersOnStartMonitoring:
+ _objc_msgSend$isEmergency
+ _objc_msgSend$isEmergencyCallOngoing
+ _objc_msgSend$lastDateInferred
+ _objc_msgSend$managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:managedObject:managedObjectContext:
+ _objc_msgSend$mostRecentResponse
+ _objc_msgSend$muteAutoPauseForWorkoutType:mute:
+ _objc_msgSend$odometer
+ _objc_msgSend$onEmergencyCallEnded
+ _objc_msgSend$onEmergencyCallStarted
+ _objc_msgSend$registerWithCompletionHandler:
+ _objc_msgSend$requestRouteSummary
+ _objc_msgSend$sessionError
+ _objc_msgSend$sessionWorkoutIdentifier
+ _objc_msgSend$sessionWorkoutMirrorType
+ _objc_msgSend$setIsEmergencyCallOngoing:
+ _objc_msgSend$setSessionWorkoutIdentifier:
+ _objc_msgSend$setSessionWorkoutMirrorType:
+ _objc_msgSend$setWorkoutSessionEndBufferTimerAlarm:
+ _objc_msgSend$setWorkoutTimeoutXPCTimerAlarm:
+ _objc_msgSend$startOdometerUpdatesForActivity:withHandler:
+ _objc_msgSend$stopOdometerUpdates
+ _objc_msgSend$takeOdometerDistanceSampleWithHandler:
+ _objc_msgSend$tipResponseMetricManager
+ _objc_msgSend$totalInferences
+ _objc_msgSend$unknownExceptionHandlingPolicyDeadInside
+ _objc_msgSend$updateTipResponse:
+ _objc_msgSend$workInferences
+ _objc_msgSend$workoutSessionEndBufferTimerAlarm
+ _objc_msgSend$workoutTimeoutXPCTimerAlarm
- +[RTTripSegmentManager isValidSynthesizedLocation:]
- +[SMSessionConfigurationMO managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:managedObject:managedObjectContext:]
- -[RTCurrentWorkoutSnapshot initWithSessionIdentifier:activityType:locationType:swimmingLocationType:isFirstPartyWorkout:sessionState:workoutStartDate:snapshotDate:]
- -[RTHealthKitManager fetchMostRecentWorkoutActivityTypeWithHandler:]
- -[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]
- -[RTLearnedLocationEngine _curateVisit:newLabel:relabelerPersister:handler:]
- -[RTLearnedLocationEngine _curateVisits:newLabel:relabelerPersister:handler:]
- -[RTLearnedLocationEngine _updateExpirationDateOfStoredUserCuration:associatedVisits:handler:]
- -[RTPersistenceMigrator __executeVacuumStepWithStore:coordinator:delegate:vacuumDate:]
- -[RTPersistenceMigrator didVacuumStore]
- -[RTPersistenceStore performVacuumWithCoordinator:error:]
- -[RTPredictedContextManager initWithFeatureExtractor:learnedLocationManager:platform:activityManager:defaultsManager:visitManager:eventManager:mapServiceManager:mapsSupportManager:navigationManager:motionActivityManager:vehicleLocationProvider:distanceCalculator:predictedContextStore:metricsManager:]
- -[SMInitiatorService initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:]
- -[SMInitiatorService initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:sessionManager:sessionMonitor:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:]
- -[SMSessionManager _setUpWorkoutStartTimeoutTimer]
- -[SMSessionManager initWithAuthorizationManager:biomeManager:contactsManager:defaultsManager:locationManager:platform:sessionMetricManager:sessionStore:messagingService:carPlayAlertManager:observers:activeSessionDetailsDelegate:wristStateManager:appDeletionManager:healthKitManager:]
- -[SMSessionManager setWorkoutStartTimeoutXPCTimerAlarm:]
- -[SMSessionManager workoutStartTimeoutXPCTimerAlarm]
- -[SMSessionWorkoutMonitor handleCurrentCMWorkoutSnapshotAtSetup]
- GCC_except_table123
- GCC_except_table127
- GCC_except_table136
- GCC_except_table163
- GCC_except_table194
- GCC_except_table263
- GCC_except_table278
- GCC_except_table290
- GCC_except_table296
- GCC_except_table302
- GCC_except_table306
- GCC_except_table307
- GCC_except_table309
- GCC_except_table338
- GCC_except_table416
- GCC_except_table424
- GCC_except_table59
- _OBJC_IVAR_$_RTPersistenceMigrator._didVacuumStore
- _OBJC_IVAR_$_SMSessionManager._workoutStartTimeoutXPCTimerAlarm
- _RTPersistentStoreMetadataLastVacuumDateKey
- ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.406
- ___25-[RTDaemonClient restore]_block_invoke.742
- ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.261
- ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.262
- ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.263
- ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.268
- ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.269
- ___27-[RTLifeCycleManager _exit]_block_invoke.716
- ___27-[RTLifeCycleManager _exit]_block_invoke.722
- ___27-[RTLifeCycleManager _exit]_block_invoke.724
- ___27-[RTLifeCycleManager _exit]_block_invoke.725
- ___27-[RTLifeCycleManager _exit]_block_invoke_2.723
- ___28-[RTHealthKitManager _setup]_block_invoke.621
- ___28-[RTLifeCycleManager _start]_block_invoke.701
- ___28-[RTLifeCycleManager _start]_block_invoke.707
- ___28-[RTLifeCycleManager _start]_block_invoke.710
- ___28-[RTLifeCycleManager _start]_block_invoke.713
- ___386+[SMSessionConfigurationMO managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:managedObject:managedObjectContext:]_block_invoke
- ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.188
- ___41-[RTAssetManager _downloadAsset:handler:]_block_invoke.359
- ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.723
- ___43-[RTPredictedContextManager _storeRequest:]_block_invoke.478
- ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.191
- ___47-[RTLearnedLocationStore _removePlace:handler:]_block_invoke.430
- ___47-[SMClientListener _setupConnection:forClient:]_block_invoke.279
- ___48-[RTFeatureExtractor _getHomeKitHomesWithError:]_block_invoke.434
- ___49-[RTTripSegmentManager isOKToAddTripSegmentdata:]_block_invoke.248
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.152
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.154
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.156
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.158
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.160
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.153
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.155
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.157
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.159
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.172
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.181
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.184
- ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.769
- ___50-[SMSessionManager _setUpWorkoutStartTimeoutTimer]_block_invoke
- ___50-[SMSessionManager _setUpWorkoutStartTimeoutTimer]_block_invoke_2
- ___52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.686
- ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.471
- ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.474
- ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.667
- ___55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.557
- ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.129
- ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.131
- ___57-[SMSessionMetricManager _gatherSessionDestinationStats:]_block_invoke.678
- ___58-[RTFeatureExtractor _getVisitsWithDateInterval:outError:]_block_invoke.414
- ___58-[RTPredictedContextManager _evaluateTrainErrorForResult:]_block_invoke.158
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.486
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.493
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.497
- ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.829
- ___59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.587
- ___59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.583
- ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.270
- ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.271
- ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.272
- ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.578
- ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.178
- ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.182
- ___62-[RTDaemonClientInternal connection:handleInvocation:isReply:]_block_invoke.491
- ___63-[RTFeatureExtractor _getTransitionsWithDateInterval:outError:]_block_invoke.416
- ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.686
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.283
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.286
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.287
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.289
- ___64-[SMSessionWorkoutMonitor handleCurrentCMWorkoutSnapshotAtSetup]_block_invoke
- ___65-[RTTripSegmentManager _purgeTripSegmentsOnDateInterval:handler:]_block_invoke.280
- ___65-[RTTripSegmentManager _purgeTripSegmentsOnDateInterval:handler:]_block_invoke.281
- ___65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.203
- ___66-[RTFeatureExtractor _getCalendarEventsWithDateInterval:outError:]_block_invoke.423
- ___66-[RTLearnedLocationStore _fetchMapItemWithMuid:predicate:handler:]_block_invoke.409
- ___66-[RTLearnedLocationStore _removeRecordsExpiredBeforeDate:handler:]_block_invoke.522
- ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.734
- ___67-[RTLearnedLocationEngine _applyUserCurationsSubmittedSince:error:]_block_invoke.917
- ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.105
- ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.109
- ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke_2.110
- ___68-[RTFeatureExtractor _getMapsViewedPlacesWithDateInterval:outError:]_block_invoke.428
- ___68-[RTFeatureExtractor _getMotionActivitiesWithDateInterval:outError:]_block_invoke.430
- ___68-[RTHealthKitManager fetchMostRecentWorkoutActivityTypeWithHandler:]_block_invoke
- ___68-[RTLearnedLocationStore _fetchLocationOfInterestWithPlace:handler:]_block_invoke.376
- ___69-[RTDaemonClient remoteStatusRegistrar:didReceiveRemoteStatus:error:]_block_invoke.770
- ___69-[RTFeatureExtractor _getLocationHistoriesWithDateInterval:outError:]_block_invoke.421
- ___69-[RTLearnedLocationEngine _getUUIDSetOfLocationsOfInterestWithError:]_block_invoke.895
- ___69-[RTLearnedLocationEngine applyUserCuration:harvestCuration:handler:]_block_invoke
- ___69-[RTPredictedContextManager _rescheduleActivityTrainWithTrainPolicy:]_block_invoke.159
- ___69-[RTTripSegmentManager _fetchTripSegmentMetadataWithOptions:handler:]_block_invoke.231
- ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.761
- ___70-[RTLearnedLocationStore _fetchLocationOfInterestWithMapItem:handler:]_block_invoke.372
- ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.288
- ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.289
- ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.290
- ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.294
- ___71-[RTFeatureExtractor _getLocationsOfInterestWithDateInterval:outError:]_block_invoke.418
- ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.509
- ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.746
- ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.551
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.460
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.464
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.475
- ___73-[RTLearnedLocationStore _fetchLocationOfInterestVisitedLastWithHandler:]_block_invoke.367
- ___73-[RTLearnedLocationStore _fetchLocationOfInterestWithIdentifier:handler:]_block_invoke.368
- ___74-[RTLearnedLocationStore _fetchInferredMapItemForVisitIdentifier:handler:]_block_invoke.365
- ___74-[RTLearnedLocationStore _fetchLocationOfInterestVisitedFirstWithHandler:]_block_invoke.366
- ___76-[RTAssetManager initWithDefaultsManager:assetProcessor:xpcActivityManager:]_block_invoke.298
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.729
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.730
- ___76-[RTLearnedLocationEngine _curateVisit:newLabel:relabelerPersister:handler:]_block_invoke
- ___76-[RTLearnedLocationEngine _curateVisit:newLabel:relabelerPersister:handler:]_block_invoke_2
- ___76-[RTLearnedLocationEngine _curateVisit:newLabel:relabelerPersister:handler:]_block_invoke_3
- ___77-[RTFeatureExtractor _getMapsHistoricalNavigationsWithDateInterval:outError:]_block_invoke.426
- ___77-[RTLearnedLocationEngine _curateVisits:newLabel:relabelerPersister:handler:]_block_invoke
- ___77-[RTLearnedLocationEngine _curateVisits:newLabel:relabelerPersister:handler:]_block_invoke_2
- ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.605
- ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.765
- ___79-[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]_block_invoke.798
- ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.718
- ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.737
- ___83-[RTDaemonClient predictedContextRegistrar:didReceivePredictedContextResult:error:]_block_invoke.809
- ___86-[RTLearnedLocationStore _fetchVisitsWithIncompletePlacesForCurrentDeviceWithHandler:]_block_invoke.402
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke.911
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke.912
- ___91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.558
- ___94-[RTLearnedLocationEngine _updateExpirationDateOfStoredUserCuration:associatedVisits:handler:]_block_invoke
- ___94-[RTLearnedLocationStore _fetchLocationOfInterestTransitionsBetweenStartDate:endDate:handler:]_block_invoke.389
- ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.673
- ___block_descriptor_181_e8_32s40s48s56s64s72s80s88s96r_e5_v8?0lr96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_40_e8_32r_e44_v32?0"RTLearnedLocationOfInterest"8Q16^B24lr32l8
- ___block_descriptor_48_e8_32bs40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_48_e8_32s_e39_v24?0"CMWorkoutSnapshot"8"NSError"16ls32l8
- ___block_descriptor_56_e8_32s40r48r_e17_v16?0"NSError"8lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40r_e31_v32?0"RTLearnedPlace"8Q16^B24ls32l8r40l8
- ___block_descriptor_72_e8_32s40s48r56r_e49_v24?0"RTLearnedLocationOfInterest"8"NSError"16ls32l8r48l8s40l8r56l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e8_v16?0Q8ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_72_e8_32s40s48s56bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e39_v24?0"RTInferredMapItem"8"NSError"16lr56l8s32l8s40l8r64l8s48l8
- ___block_descriptor_80_e8_32s40s48r56r64r_e29_v24?0"NSArray"8"NSError"16lr48l8s32l8r56l8s40l8r64l8
- ___block_descriptor_80_e8_32s40s48s56r64r_e36_v24?0"RTLearnedVisit"8"NSError"16ls32l8s40l8r56l8s48l8r64l8
- ___block_descriptor_80_e8_32s40s48s56s64bs_e36_v24?0"RTLearnedPlace"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_81_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64r72r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8r64l8s48l8s56l8r72l8
- ___block_literal_global.1222
- ___block_literal_global.133
- ___block_literal_global.1379
- ___block_literal_global.1383
- ___block_literal_global.174
- ___block_literal_global.176
- ___block_literal_global.178
- ___block_literal_global.180
- ___block_literal_global.183
- ___block_literal_global.186
- ___block_literal_global.190
- ___block_literal_global.193
- ___block_literal_global.291
- ___block_literal_global.395
- ___block_literal_global.452
- ___block_literal_global.554
- ___block_literal_global.563
- ___block_literal_global.604
- ___block_literal_global.642
- ___block_literal_global.643
- ___block_literal_global.688
- ___block_literal_global.704
- ___block_literal_global.709
- ___block_literal_global.712
- ___block_literal_global.715
- ___block_literal_global.727
- ___block_literal_global.736
- ___block_literal_global.744
- ___block_literal_global.904
- ___block_literal_global.915
- ___block_literal_global.968
- _kRTPersistentStoreVacuumTimeInterval
- _objc_msgSend$__executeVacuumStepWithStore:coordinator:delegate:vacuumDate:
- _objc_msgSend$_applyUserCuration:relabelerPersister:harvestCuration:handler:
- _objc_msgSend$_curateVisit:newLabel:relabelerPersister:handler:
- _objc_msgSend$_curateVisits:newLabel:relabelerPersister:handler:
- _objc_msgSend$_setUpWorkoutStartTimeoutTimer
- _objc_msgSend$_updateExpirationDateOfStoredUserCuration:associatedVisits:handler:
- _objc_msgSend$didVacuumStore
- _objc_msgSend$fetchMostRecentWorkoutActivityTypeWithHandler:
- _objc_msgSend$handleCurrentCMWorkoutSnapshotAtSetup
- _objc_msgSend$initWithAuthorizationManager:biomeManager:contactsManager:defaultsManager:locationManager:platform:sessionMetricManager:sessionStore:messagingService:carPlayAlertManager:observers:activeSessionDetailsDelegate:wristStateManager:appDeletionManager:healthKitManager:
- _objc_msgSend$initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:
- _objc_msgSend$initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:
- _objc_msgSend$initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:sessionManager:sessionMonitor:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:
- _objc_msgSend$initWithFeatureExtractor:learnedLocationManager:platform:activityManager:defaultsManager:visitManager:eventManager:mapServiceManager:mapsSupportManager:navigationManager:motionActivityManager:vehicleLocationProvider:distanceCalculator:predictedContextStore:metricsManager:
- _objc_msgSend$initWithSessionIdentifier:activityType:isWorkoutOngoing:isFirstPartyWorkout:
- _objc_msgSend$initWithSessionIdentifier:activityType:locationType:swimmingLocationType:isFirstPartyWorkout:sessionState:workoutStartDate:snapshotDate:
- _objc_msgSend$initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:
- _objc_msgSend$managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:managedObject:managedObjectContext:
- _objc_msgSend$performSelector:
- _objc_msgSend$performVacuumWithCoordinator:error:
- _objc_msgSend$setSelector:
- _objc_msgSend$setWorkoutStartTimeoutXPCTimerAlarm:
- _objc_msgSend$workoutStartTimeoutXPCTimerAlarm
CStrings:
+ "#SessionManager,Initiator,sessionID:%@,%@,%@, do not handoff"
+ "#SessionManager,Initiator,sessionID:%@,%@,%@, handoff finished with error, %@ "
+ "#SessionManager,Initiator,sessionID:%@,%@,%@, sessionType, %ld, workoutOngoing, %d, isFirstPartyWorkout, %d, local workoutID, %@, config workoutID, %@, local workoutSessionType, %ld, config workoutSessionType, %ld"
+ "#SessionManager,Initiator,sessionID:%@,%@,%@,failed to fetch workout snapshot with error,%@"
+ "%@, %@, A fallback candidate was identified from history (%@), but it was not found in the current set of place candidates. Aborting fallback."
+ "%@, %@, Failed to fetch historical work inferences: %@"
+ "%@, %@, Failed to fetch historical work stats: %@"
+ "%@, %@, Fetched work inference history stats for %lu places over %lu days, number of PlaceTypeInferences fetched, %lu"
+ "%@, %@, Found multiple place stats for the same best identifier %@. Aborting fallback."
+ "%@, %@, Historical stats for place %@: %@"
+ "%@, %@, No fallback candidate met the required ratio threshold of %.2f."
+ "%@, %@, Processing history stats for identifier: %@, num inferences with yield: %lu, num total yield: %lu, ratio: %.3f, last inferred: %@"
+ "%@, %@, RTDataProtectionManagerNotificationUnlockedSinceBoot received, available, YES"
+ "%@, %@, Selected fallback work %@ with ratio %.2f and date %@"
+ "%@, %@, Tie detected in fallback ratio (%.2f). Selecting candidate %@ with more recent inference date %@ over existing candidate %@ with date %@"
+ "%@, %@, _createLOIForPlace failed to return a valid RTLearnedLocationOfInterest, error, %@"
+ "%@, %@, _placeForMapItem failed to return a valid RTLearnedPlace, error, %@"
+ "%@, %@, attempted to apply user curation, %@, success, %@, error, %@"
+ "%@, %@, attempted to curate visit, %@, new label, %@, success, %@, error, %@"
+ "%@, %@, attempting to submit metric with response, %ld"
+ "%@, %@, available, %@"
+ "%@, %@, endWorkoutReminderSettingEnabled, %@, endWorkoutReminderDate, %@, latestWorkoutManualPauseDate, %@, latestWorkoutAutoPauseDate, %@, outdoorPedAutoPauseDistance, %@, outdoorPedAutoPauseDistanceThreshold, %f"
+ "%@, %@, fetchInferredMapItemForVisitIdentifier failed to return a valid map item with visit identifier, %@, error, %@"
+ "%@, %@, fetched historical stats for %lu places for fallback analysis"
+ "%@, %@, invoked with start date, %@"
+ "%@, %@, placeStats count, %lu, inferred home from fallback, %{sensitive}@, inferred works from fallback, %{sensitive}@"
+ "%@, %@, reduced all visits within curation date interval to %lu visits matching curation's map item"
+ "%@, %@, request, %{sensitive}@, error, %@"
+ "%@, %@, retrieved %lu user curations"
+ "%@, %@, route summary, %{sensitive}@"
+ "%@, %@, skipping metric submission due to no collection started"
+ "%@, %@, skipping response update"
+ "%@, %@, treating user curation as a current place curation"
+ "%@, %@, treating user curation as a historical visit curation"
+ "%@, %@, triggerReason, %@, client.clientIdentity, %@, can skip inference since the original registration is old"
+ "%@, %@, updating response, %ld"
+ "%@, %@, user curation POI data harvested successfully!"
+ "%@, dateInterval, startDate, %@, endDate, %@, fetched lois uuids count, %lu, latency %.2f, error(s), %@"
+ "%@, failed to convert RTUserCurationMO to RTUserCuration, %@"
+ "%@, ignoring deferral due to defaults key: %@"
+ "%@, loisUUIDs, %@"
+ "%@, response, %lu"
+ "%s delta distance %f, should trigger, %@"
+ "%s error %@"
+ "%s intial distance %@, final distance, %@"
+ "%s odometer distance %@"
+ "%s, Current workout, start date: %@, session type: %ld"
+ "%{public}@, %{public}@, incoming workout snapshot, activityType, %d, locationType, %d, sessionState, %d, sessionError, %{public}@"
+ "%{public}@, %{public}@, new workout started with uuid, %@"
+ "%{public}@, %{public}@, setting current workout session to nil"
+ "%{public}s workoutTimeoutXPCTimerAlarm fireWithDate failed with error, %{public}@"
+ "%{public}s, adding observer, %@"
+ "%{public}s, device not eligible to time out the session, isActiveDevice, %@, sessionType is workout, %@, workoutOngoing, %@"
+ "%{public}s, emergency call ended"
+ "%{public}s, emergency call has ended"
+ "%{public}s, emergency call is active"
+ "%{public}s, emergency call is being placed, tear down the workout end buffer timer"
+ "%{public}s, emergency call started, tearing down workout timeouts"
+ "%{public}s, emergency call with status, %d"
+ "%{public}s, failed to end session due to error, %{public}@"
+ "%{public}s, received RTHealthKitManager notification, %{public}@"
+ "%{public}s, received TUCallCenterCallStatusChangedNotification"
+ "%{public}s, removing observer, %@"
+ "%{public}s, skipping session update due to identical workout snapshot"
+ "%{public}s, state update with new workout snapshot failed due to, %{public}@"
+ "%{public}s, tearing down workout ended buffer timer"
+ "%{public}s, timer set with end date, %@"
+ "%{public}s, workout end awaiting emergency contact notification timeout resumed"
+ "%{public}s, workout end buffer resumed"
+ "%{public}s, workout snapshot fetch failed due to, %{public}@"
+ "%{public}s, workout start timeout started"
+ "-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:error:]"
+ "-[RTLearnedLocationEngine _curateVisit:newLabel:relabelerPersister:error:]"
+ "-[RTLearnedLocationEngine _curateVisits:newLabel:relabelerPersister:error:]"
+ "-[RTLearnedLocationEngine _updateExpirationDateOfStoredUserCuration:associatedVisits:error:]"
+ "-[RTPlaceTypeClassifierMetricsCalculator fetchWorkInferenceStatsForLookbackDays:handler:]"
+ "-[SMCMOdometer odometer:didUpdateGpsAvailability:]"
+ "-[SMEmergencyCallManager _addObserver:]"
+ "-[SMEmergencyCallManager _onTUCallCenterCallStatusChangedNotification:]"
+ "-[SMEmergencyCallManager _removeObserver:]"
+ "-[SMEmergencyCallManager onTUCallCenterCallStatusChangedNotification:]"
+ "-[SMInitiatorService _onEmergencyCallEnded]"
+ "-[SMInitiatorService _onEmergencyCallStarted]"
+ "-[SMInitiatorService _tearDownWorkoutEndedBufferTimer]"
+ "-[SMSessionManager _onEmergencyCallEnded]"
+ "-[SMSessionManager _onEmergencyCallStarted]"
+ "-[SMSessionManager _onHealthKitManagerNotification:]_block_invoke"
+ "-[SMSessionManager _setUpWorkoutTimeouts]"
+ "-[SMSessionManager _setupWorkoutTimeoutWithFireDate:]"
+ "-[SMSessionManager _setupWorkoutTimeoutWithFireDate:]_block_invoke_2"
+ "-[SMSessionManager _updateSessionWithWorkoutSnapshot:handler:]"
+ "-[SMSessionManager initWithAuthorizationManager:biomeManager:contactsManager:defaultsManager:locationManager:platform:sessionMetricManager:sessionStore:messagingService:carPlayAlertManager:observers:activeSessionDetailsDelegate:wristStateManager:appDeletionManager:healthKitManager:emergencyCallManager:]"
+ "-[SMSessionWorkoutMonitor _onTimerExpiryForTimerIdentifier:]_block_invoke"
+ "-[SMSessionWorkoutMonitor _onTimerExpiryForTimerIdentifier:]_block_invoke_2"
+ "-[SMSessionWorkoutMonitor checkIfCurrentWorkoutIsOutdoorPedestrianWithHandler:]_block_invoke"
+ "-[SMSessionWorkoutMonitor initializeTimersOnStartMonitoring:]"
+ "-[SMSessionWorkoutMonitor takeOdometerDistanceSampleWithHandler:]_block_invoke"
+ "05:39:03"
+ "3"
+ "@\"CMOdometer\""
+ "@\"SMCMOdometer\""
+ "@\"SMCheckInRemindersTipResponseMetricManager\""
+ "@\"SMEmergencyCallManager\""
+ "@\"TUCallCenter\""
+ "@176@0:8@16Q24@32d40d48i56d60Q68d76d84Q92@100@108@116B124@128@136Q144q152@160@168"
+ "@216@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208"
+ "@232@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224"
+ "@48@0:8@16Q24Q32@40"
+ "@92@0:8@16Q24q32q40q48B56Q60@68@76@84"
+ "CMOdometerDelegate"
+ "InferredExcludingFallback"
+ "Invalid parameter not satisfying: emergencyCallManager"
+ "Jul 26 2025"
+ "Metric collection not started"
+ "RTDefaultsCheckInRemindersFitnessTipResponse"
+ "RTDefaultsInitiatorServiceWorkoutEndBufferTimerFireDate"
+ "RTDefaultsMostRecentWorkoutMirrorType"
+ "RTDefaultsMostRecentWorkoutSessionID"
+ "RTDefaultsPredictedContextManagerTrainIgnoreDeferral"
+ "RTDefaultsSessionManagerWorkoutEmergencyContactNotificationTimerFireDate"
+ "RTDefaultsTripSegmentCheckSynthesizedLocationsForAltitudeSpeedAccuracy"
+ "RTPersistenceOpearationsErrorDomain"
+ "RTStore RTStoreExceptionHandlingPolicy did not have a policy handling.\n%@"
+ "RTWorkInferenceHistoryStats"
+ "Received exception in persistence stack, %@"
+ "Resource temporarily unavailable; data access not available until first unlock after boot."
+ "SMCMOdometer"
+ "SMCheckInRemindersTipResponseMetricManager"
+ "SMDefaultsSessionWorkoutMonitorLatestWorkoutAutoPauseDate"
+ "SMDefaultsSessionWorkoutMonitorLatestWorkoutManualPauseDate"
+ "SMDefaultsSessionWorkoutMonitorOutdoorPedAutoPauseDistance"
+ "SMDefaultsSessionWorkoutMonitorOutdoorPedAutoPauseDistanceThreshold"
+ "SMEmergencyCallManager"
+ "SMEmergencyCallObserverProtocol"
+ "SMInitiatorMetricsProtocol"
+ "SafetyMonitor.initiator.CheckInRemindersFitnessTipResponse"
+ "T@\"CMOdometer\",R,N,V_odometer"
+ "T@\"NSDate\",R,N,V_lastDateInferred"
+ "T@\"NSError\",R,N,V_sessionError"
+ "T@\"NSNumber\",&,N,V_outdoorPedAutoPauseDistance"
+ "T@\"RTXPCTimerAlarm\",&,N,V_workoutSessionEndBufferTimerAlarm"
+ "T@\"RTXPCTimerAlarm\",&,N,V_workoutTimeoutXPCTimerAlarm"
+ "T@\"SMCMOdometer\",&,N,V_cmOdometer"
+ "T@\"SMCheckInRemindersTipResponseMetricManager\",&,N,V_tipResponseMetricManager"
+ "T@\"SMEmergencyCallManager\",&,N,V_emergencyCallManager"
+ "T@\"TUCallCenter\",&,N,V_callCenter"
+ "TB,N,V_checkForValidAltitudeSpeedAccuracy"
+ "TB,N,V_isEmergencyCallOngoing"
+ "TQ,R,N,V_totalInferences"
+ "TQ,R,N,V_workInferences"
+ "Td,N,V_outdoorPedAutoPauseDistanceThreshold"
+ "Timed out fetching historical work stats."
+ "Tq,R"
+ "Tq,R,N,V_sessionType"
+ "WorkStats[%@: %lu/%lu], date:%@"
+ "_applyUserCuration:relabelerPersister:harvestCuration:error:"
+ "_callCenter"
+ "_checkForValidAltitudeSpeedAccuracy"
+ "_checkForValidAltitudeSpeedAccuracyDefault"
+ "_cmOdometer"
+ "_curateVisit:newLabel:relabelerPersister:error:"
+ "_curateVisits:newLabel:relabelerPersister:error:"
+ "_emergencyCallManager"
+ "_fetchLocationsOfInterestUUIDsVisitedWithHandler:"
+ "_isEmergencyCallOngoing"
+ "_lastDateInferred"
+ "_notifyObserversForEmergencyCallEnded"
+ "_notifyObserversForEmergencyCallStarted"
+ "_odometer"
+ "_onEmergencyCallEnded"
+ "_onEmergencyCallStarted"
+ "_onTUCallCenterCallStatusChangedNotification:"
+ "_outdoorPedAutoPauseDistance"
+ "_outdoorPedAutoPauseDistanceThreshold"
+ "_sessionError"
+ "_setUpWorkoutTimeouts"
+ "_setupWorkoutTimeoutWithFireDate:"
+ "_storeMetricsForNonFallbackPlacesWithHome:homeSource:work:workSource:"
+ "_tearDownWorkoutEndedBufferTimer"
+ "_tearDownWorkoutTimeouts"
+ "_tipResponseMetricManager"
+ "_totalInferences"
+ "_updateExpirationDateOfStoredUserCuration:associatedVisits:error:"
+ "_updateSessionWithWorkoutSnapshot:handler:"
+ "_workInferences"
+ "_workoutTimeoutXPCTimerAlarm"
+ "callCenter"
+ "callCenterWithQueue:"
+ "checkForValidAltitudeSpeedAccuracy"
+ "checkIfCurrentWorkoutIsOutdoorPedestrianWithHandler:"
+ "cmOdometer"
+ "com.apple.routined.SMSessionWorkoutMonitorWorkoutAutoPauseFireTriggerTimerIdentifier"
+ "com.apple.routined.safetyMonitor.sessionManager.workoutTimeout"
+ "coreDataExceptionLogging:"
+ "currentCalls"
+ "durationOfPendingSyncNoWait"
+ "durationOfPendingSyncOver5Min"
+ "durationOfPendingSyncUnder10Sec"
+ "durationOfPendingSyncUnder1Min"
+ "durationOfPendingSyncUnder20Sec"
+ "durationOfPendingSyncUnder2Min"
+ "durationOfPendingSyncUnder30Sec"
+ "durationOfPendingSyncUnder5Min"
+ "emergencyCallManager"
+ "evaluatePolicyForCoreDataContextPerformBlockException:"
+ "fetchIsEmergencyCallOngoingWithHandler:"
+ "fetchLocationsOfInterestUUIDsVisitedWithHandler:"
+ "fetchMostRecentWorkoutInfoWithHandler:"
+ "fetchWorkInferenceStatsForLookbackDays:handler:"
+ "hasMapItemStorage"
+ "inferWorkFromHistoryAndPlaceStats:"
+ "initWithAuthorizationManager:biomeManager:contactsManager:defaultsManager:locationManager:platform:sessionMetricManager:sessionStore:messagingService:carPlayAlertManager:observers:activeSessionDetailsDelegate:wristStateManager:appDeletionManager:healthKitManager:emergencyCallManager:"
+ "initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:"
+ "initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:emergencyCallManager:"
+ "initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:sessionManager:sessionMonitor:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:emergencyCallManager:"
+ "initWithFeatureExtractor:learnedLocationManager:platform:activityManager:dataProtectionManager:defaultsManager:visitManager:eventManager:mapServiceManager:mapsSupportManager:navigationManager:motionActivityManager:vehicleLocationProvider:distanceCalculator:predictedContextStore:metricsManager:"
+ "initWithHealthStore:reportInactiveSessions:"
+ "initWithLearnedPlaceIdentifier:totalInferences:workInferences:lastDateInferred:"
+ "initWithSessionIdentifier:activityType:locationType:swimmingLocationType:sessionType:isFirstPartyWorkout:sessionState:workoutStartDate:snapshotDate:sessionError:"
+ "initWithSessionIdentifier:activityType:sessionType:isWorkoutOngoing:isFirstPartyWorkout:"
+ "initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:"
+ "initializeTimersOnStartMonitoring:"
+ "isEmergency"
+ "isEmergencyCallOngoing"
+ "lastDateInferred"
+ "managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sosReceivers:sessionWorkoutIdentifier:sessionWorkoutType:sessionWorkoutMirrorType:managedObject:managedObjectContext:"
+ "mostRecentResponse"
+ "odometer"
+ "odometer:didUpdateGpsAvailability:"
+ "onEmergencyCallEnded"
+ "onEmergencyCallStarted"
+ "onTUCallCenterCallStatusChangedNotification:"
+ "origin, hasMapItem, %@, location, <%f, %f>, destination, hasMapItem, %@, name, %@, location, <%f, %f>"
+ "origin, location, <%f, %f>, destination, name, %@, location, <%f, %f>"
+ "outdoorPedAutoPauseDistance"
+ "outdoorPedAutoPauseDistanceThreshold"
+ "overriding outdoor ped auto-pause distance threshold"
+ "registerWithCompletionHandler:"
+ "requestRouteSummary"
+ "respondedToCheckInRemindersTipWithResponse:"
+ "sessionError"
+ "sessionIdentifier, %@, activityType, %lu, locationType, %lu, swimmingLocationType, %lu, sessionType, %lu, isFirstPartyWorkout, %@, sessionState, %@, workoutStartDate, %@, sessionErrorDomain, %@, sessionErrorCode, %ld"
+ "sessionWorkoutIdentifier"
+ "sessionWorkoutMirrorType"
+ "setCallCenter:"
+ "setCheckForValidAltitudeSpeedAccuracy:"
+ "setCmOdometer:"
+ "setEmergencyCallManager:"
+ "setIsEmergencyCallOngoing:"
+ "setOutdoorPedAutoPauseDistance:"
+ "setOutdoorPedAutoPauseDistanceThreshold:"
+ "setSessionWorkoutIdentifier:"
+ "setSessionWorkoutMirrorType:"
+ "setTipResponseMetricManager:"
+ "setWorkoutTimeoutXPCTimerAlarm:"
+ "startCheckInRemindersTipMetricsCollection"
+ "startOdometerUpdatesForActivity:withHandler:"
+ "stopOdometerUpdates"
+ "takeOdometerDistanceSampleWithHandler:"
+ "tipResponse"
+ "tipResponseMetricManager"
+ "totalInferences"
+ "unknownExceptionHandlingPolicyDeadInside"
+ "updateTipResponse:"
+ "v16@?0@\"NSNumber\"8"
+ "v24@?0@\"CMOdometerData\"8@\"NSError\"16"
+ "v28@0:8@\"CMOdometer\"16B24"
+ "v32@?0@\"NSUUID\"8Q16q24"
+ "v48@0:8@16Q24@32Q40"
+ "workInferences"
+ "workoutTimeoutXPCTimerAlarm"
- "#SessionManager,Initiator,sessionID:%@,%@,%@, phone device handle magnetConnect finished with error %@ "
- "#SessionManager,Initiator,sessionID:%@,%@,%@,phone noop,sessionType,%ld"
- "%@, %@, _placeForMapItem returned a nil place, exiting early"
- "%@, %@, applying user curation as a current place curation"
- "%@, %@, applying user curation as a historical visit curation"
- "%@, %@, error occurred while creating and storing new LOI, %@"
- "%@, %@, error occurred while fetching place for map item, %@"
- "%@, %@, incoming workout snapshot, activityType, %d, locationType, %d, sessionState, %d"
- "%@, %@, new workout started with uuid, %@"
- "%@, %@, placeStats count, %lu, inferred home from fallback, %{sensitive}@,"
- "%@, %@, reduced all visits within curation date interval to %lu visits matching curation's map item, error, %@"
- "%@, %@, retrieved %lu curations"
- "%@, %@, setting current workout session to nil"
- "%@, dateInterval, startDate, %@, endDate, %@, fetched lois count, %lu, latency %.2f, error(s), %@"
- "%s workoutStartTimeoutXPCTimerAlarm fireWithDate failed with error, %@"
- "%s, Configuartion modified for wrong session, current config sessionID, %@, modified config sessionID, %@"
- "%s, endWorkoutReminderSettingEnabled, %@, endWorkoutReminderDate, %@, latestWorkoutManualPauseDate, %@, latestWorkoutAutoPauseDate. %@"
- "%s, failed to end session due to error, %@"
- "%s, received RTHealthKitManager notification, %@"
- "-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]"
- "-[RTLearnedLocationEngine _curateVisit:newLabel:relabelerPersister:handler:]"
- "-[RTLearnedLocationEngine _curateVisits:newLabel:relabelerPersister:handler:]"
- "-[RTLearnedLocationEngine _updateExpirationDateOfStoredUserCuration:associatedVisits:handler:]"
- "-[RTPersistenceMigrator __executeVacuumStepWithStore:coordinator:delegate:vacuumDate:]"
- "-[RTPersistenceStore performVacuumWithCoordinator:error:]"
- "-[SMSessionManager _setUpWorkoutStartTimeoutTimer]"
- "-[SMSessionManager _setUpWorkoutStartTimeoutTimer]_block_invoke_2"
- "-[SMSessionManager initWithAuthorizationManager:biomeManager:contactsManager:defaultsManager:locationManager:platform:sessionMetricManager:sessionStore:messagingService:carPlayAlertManager:observers:activeSessionDetailsDelegate:wristStateManager:appDeletionManager:healthKitManager:]"
- "-[SMSessionWorkoutMonitor handleCurrentCMWorkoutSnapshotAtSetup]"
- ".B"
- "20:19:11"
- "@\"NSTimer\""
- "@160@0:8@16Q24@32d40d48i56d60Q68d76d84Q92@100@108@116B124@128Q136@144@152"
- "@208@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200"
- "@224@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216"
- "@76@0:8@16Q24q32q40B48Q52@60@68"
- "Fetched a nil place"
- "Invalid parameter not satisfying: originMapItem"
- "Invalid parameter not satisfying: vacuumDate"
- "Jul 12 2025"
- "Q48@0:8@16@24@32@40"
- "RTPersistentStoreMetadataLastVacuumDateKey"
- "SMDefaultsSessionWorkoutMonitorLatestWorkoutAutoPauseDateKey"
- "SMDefaultsSessionWorkoutMonitorLatestWorkoutManualPauseDateKey"
- "T@\"NSTimer\",&,N,V_workoutSessionEndBufferTimerAlarm"
- "T@\"RTXPCTimerAlarm\",&,N,V_workoutStartTimeoutXPCTimerAlarm"
- "TB,R,V_didVacuumStore"
- "__executeVacuumStepWithStore:coordinator:delegate:vacuumDate:"
- "_applyUserCuration:relabelerPersister:harvestCuration:handler:"
- "_curateVisit:newLabel:relabelerPersister:handler:"
- "_curateVisits:newLabel:relabelerPersister:handler:"
- "_didVacuumStore"
- "_setUpWorkoutStartTimeoutTimer"
- "_updateExpirationDateOfStoredUserCuration:associatedVisits:handler:"
- "_workoutStartTimeoutXPCTimerAlarm"
- "com.apple.routined.safetyMonitor.sessionManager.workoutStartTimeout"
- "didVacuumStore"
- "fetchMostRecentWorkoutActivityTypeWithHandler:"
- "handleCurrentCMWorkoutSnapshotAtSetup"
- "initWithAuthorizationManager:biomeManager:contactsManager:defaultsManager:locationManager:platform:sessionMetricManager:sessionStore:messagingService:carPlayAlertManager:observers:activeSessionDetailsDelegate:wristStateManager:appDeletionManager:healthKitManager:"
- "initWithConversation:sessionID:sessionStartDate:sessionType:time:destination:userResponseSafeDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:"
- "initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:"
- "initWithDefaultsManager:contactsManager:locationManager:motionActivityManager:platform:sessionManager:sessionMonitor:messagingService:safetyCacheStore:sessionStore:dataProtectionManager:batteryManager:xpcActivityManager:networkOfInterestManager:authorizationManager:wristStateManager:vehicleLocationProvider:starkManager:suggestionsManager:suggestionsHelper:learnedLocationManager:healthKitManager:deviceConfigurationChecker:noMovementMonitor:biomeManager:appDeletionManager:"
- "initWithFeatureExtractor:learnedLocationManager:platform:activityManager:defaultsManager:visitManager:eventManager:mapServiceManager:mapsSupportManager:navigationManager:motionActivityManager:vehicleLocationProvider:distanceCalculator:predictedContextStore:metricsManager:"
- "initWithSessionIdentifier:activityType:isWorkoutOngoing:isFirstPartyWorkout:"
- "initWithSessionIdentifier:activityType:locationType:swimmingLocationType:isFirstPartyWorkout:sessionState:workoutStartDate:snapshotDate:"
- "initWorkoutBoundSessionConfigurationWithConversation:sessionID:sessionStartDate:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:"
- "managedObjectWithSessionIdentifier:sessionType:sessionStartDate:destinationLatitude:destinationLongitude:destinationReferenceFrame:destinationRadius:destinationType:expectedTravelTime:additionalTravelTime:transportType:sessionTimeBound:conversation:destinationMapItem:sessionSupportsHandoff:sosReceivers:sessionWorkoutType:managedObject:managedObjectContext:"
- "numSyncsRequiring10SecWait"
- "numSyncsRequiring1MinWait"
- "numSyncsRequiring20SecWait"
- "numSyncsRequiring2MinWait"
- "numSyncsRequiring30SecWait"
- "numSyncsRequiring5MinPlusWait"
- "numSyncsRequiring5MinWait"
- "numSyncsRequiringNoWait"
- "origin location, <%f, %f>, destination name, %@, destination location, <%f, %f>"
- "performVacuumWithCoordinator:error:"
- "sessionIdentifier, %@, activityType, %lu, locationType, %lu, swimmingLocationType, %lu, isFirstPartyWorkout, %@, sessionState, %@, workoutStartDate, %@"
- "setWorkoutStartTimeoutXPCTimerAlarm:"
- "vacuum duration, %lf"
- "vacuuming store %@"
- "workoutStartTimeoutXPCTimerAlarm"

```
