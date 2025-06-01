## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-891.0.1.0.0
-  __TEXT.__text: 0x422468
-  __TEXT.__auth_stubs: 0x17d0
-  __TEXT.__objc_methlist: 0x21050
-  __TEXT.__const: 0x19f0
-  __TEXT.__gcc_except_tab: 0x14f94
-  __TEXT.__oslogstring: 0x4d01a
-  __TEXT.__cstring: 0x31928
+893.0.5.0.2
+  __TEXT.__text: 0x42c04c
+  __TEXT.__auth_stubs: 0x1820
+  __TEXT.__objc_methlist: 0x214a8
+  __TEXT.__const: 0x1a38
+  __TEXT.__gcc_except_tab: 0x15530
+  __TEXT.__oslogstring: 0x4dd96
+  __TEXT.__cstring: 0x31f15
   __TEXT.__ustring: 0x16
-  __TEXT.__dlopen_cstrs: 0x112
-  __TEXT.__unwind_info: 0xa094
-  __TEXT.__objc_classname: 0x41e4
-  __TEXT.__objc_methname: 0x65e03
-  __TEXT.__objc_methtype: 0x9f7a
-  __TEXT.__objc_stubs: 0x3dca0
-  __DATA_CONST.__got: 0xa10
-  __DATA_CONST.__const: 0xb200
-  __DATA_CONST.__objc_classlist: 0xff0
-  __DATA_CONST.__objc_catlist: 0x2b8
+  __TEXT.__dlopen_cstrs: 0x188
+  __TEXT.__unwind_info: 0xa1f0
+  __TEXT.__objc_classname: 0x427c
+  __TEXT.__objc_methname: 0x66d43
+  __TEXT.__objc_methtype: 0xa02e
+  __TEXT.__objc_stubs: 0x3e1e0
+  __DATA_CONST.__got: 0xa28
+  __DATA_CONST.__const: 0xb260
+  __DATA_CONST.__objc_classlist: 0x1010
+  __DATA_CONST.__objc_catlist: 0x2c0
   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x315f8
-  __DATA_CONST.__objc_selrefs: 0x11bf0
+  __DATA_CONST.__objc_const: 0x31c38
+  __DATA_CONST.__objc_selrefs: 0x11e08
   __DATA_CONST.__objc_arraydata: 0x1998
-  __AUTH_CONST.__const: 0x2480
-  __AUTH_CONST.__cfstring: 0x1e120
-  __AUTH_CONST.__objc_const: 0xd1e8
+  __AUTH_CONST.__const: 0x2500
+  __AUTH_CONST.__cfstring: 0x1e440
+  __AUTH_CONST.__objc_const: 0xd420
   __AUTH_CONST.__objc_intobj: 0x2b38
   __AUTH_CONST.__objc_doubleobj: 0x8e0
   __AUTH_CONST.__objc_arrayobj: 0xb70
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0xbf8
-  __AUTH.__objc_data: 0x1b30
+  __AUTH_CONST.__objc_floatobj: 0x20
+  __AUTH_CONST.__auth_got: 0xc20
+  __AUTH.__objc_data: 0x1c70
   __DATA.__objc_protorefs: 0x108
-  __DATA.__objc_classrefs: 0x1b90
-  __DATA.__objc_superrefs: 0xdb0
-  __DATA.__objc_ivar: 0x1aec
+  __DATA.__objc_classrefs: 0x1bb8
+  __DATA.__objc_superrefs: 0xdd0
+  __DATA.__objc_ivar: 0x1b58
   __DATA.__data: 0x23c8
-  __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_ivar: 0xb70
+  __DATA.__bss: 0x60
+  __DATA_DIRTY.__objc_ivar: 0xb78
   __DATA_DIRTY.__objc_data: 0x8430
   __DATA_DIRTY.__data: 0x498
-  __DATA_DIRTY.__bss: 0x118
+  __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
+  - /System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter
   - /System/Library/PrivateFrameworks/ContactsDonation.framework/ContactsDonation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: F0B1705E-E62D-331B-8765-9DCBC7F0C5CA
-  Functions: 14415
-  Symbols:   47252
-  CStrings:  29079
+  UUID: 7374E541-81AF-3C0E-96FF-B853CAD5BB13
+  Functions: 14524
+  Symbols:   47603
+  CStrings:  29307
 
Symbols:
+ +[NSPersonNameComponents(SMExtensions) sharedNameComponents]
+ +[RTPeopleDensityTTR tryShowingHighDensityDetectedUIWithValue:threshold:defaultsManager:densityStore:singleRecords:]
+ +[RTVisitPipelineMotionAccumulator isActivityTypeMotionTrimmable:]
+ +[RTVisitPipelineMotionAccumulatorParams loadParameterFromDefaults:parameterName:defaultValue:]
+ -[RTDefaultsManager copyKeyListContainingString:]
+ -[RTHealthKitManager _getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:]
+ -[RTHealthKitManager _getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:error:]
+ -[RTHealthKitManager _getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:]
+ -[RTHealthKitManager getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:]
+ -[RTHealthKitManager getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:error:]
+ -[RTHealthKitManager getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:]
+ -[RTLearnedLocationStore _fetchCountOfVisitsToLocationOfInterestWithIdentifier:endDate:handler:]
+ -[RTLearnedLocationStore fetchCountOfVisitsToLocationOfInterestWithIdentifier:endDate:handler:]
+ -[RTLearnedPlaceTypeInferenceGenerator _getCandidatePlaceStatsFromPlaceStats:]
+ -[RTLearnedPlaceTypeInferenceGenerator _getFullLocationHistoryDateInterval]
+ -[RTLearnedPlaceTypeInferenceGenerator _prepareMLFeaturesWithPlaceStats:]
+ -[RTLearnedPlaceTypeInferenceGenerator filteredPlaceStatsByWeeklyVisitThreshold:placeStats:]
+ -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromDailyPatternsWithPlaceStats:dateInterval:]
+ -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromFallbackWithPlaceStats:dateInterval:]
+ -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromModelWithCandidateSelection:homeModelType:workModelType:placeStats:dateInterval:]
+ -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromModelWithPlaceStats:dateInterval:]
+ -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngineWithPlaceStats:dateInterval:]
+ -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromTopMedianDwellTimeWithPlaceStats:dateInterval:]
+ -[RTLearnedPlaceTypeInferenceGenerator placeCandidateStatsForType:placeStats:dateInterval:excludingPlaces:parameters:distanceThreshold:]
+ -[RTLearnedPlaceTypeInferenceGenerator placeCandidatesFromDailyPatternsForType:placeStats:parameters:]
+ -[RTLearnedPlaceTypeInferenceGenerator placeCandidatesFromTopMedianDwellTimeForType:placeStats:parameters:]
+ -[RTPeopleDensityRecord cleanUpOngoingPeopleDensityBundle]
+ -[RTPeopleDensityRecord defaultsManager]
+ -[RTPeopleDensityRecord highDensityThreshold]
+ -[RTPeopleDensityRecord setDefaultsManager:]
+ -[RTPeopleDensityRecord setHighDensityThreshold:]
+ -[RTPeopleDensityTTR .cxx_destruct]
+ -[RTPeopleDensityTTR _highPeopleDensityUIResponseFlags:]
+ -[RTPeopleDensityTTR _showHighDensityDetectedUI]
+ -[RTPeopleDensityTTR defaultsManager]
+ -[RTPeopleDensityTTR densityStore]
+ -[RTPeopleDensityTTR highPeopleDensityUIResponseFlags:]
+ -[RTPeopleDensityTTR initWithQueue:value:threshold:defaultsManager:densityStore:singleRecords:]
+ -[RTPeopleDensityTTR queue]
+ -[RTPeopleDensityTTR setDefaultsManager:]
+ -[RTPeopleDensityTTR setDensityStore:]
+ -[RTPeopleDensityTTR setQueue:]
+ -[RTPeopleDensityTTR setSingleRecordsDescription:]
+ -[RTPeopleDensityTTR setThreshold:]
+ -[RTPeopleDensityTTR setValue:]
+ -[RTPeopleDensityTTR showHighDensityDetectedUI]
+ -[RTPeopleDensityTTR singleRecordsDescription]
+ -[RTPeopleDensityTTR threshold]
+ -[RTPeopleDensityTTR value]
+ -[RTPeopleDiscoveryContactRecord cleanUpOngoingContactRecordsAndScores]
+ -[RTPeopleDiscoveryProvider _clearPeopleDensityBundles:]
+ -[RTPeopleDiscoveryProvider _clearProximityEvents:]
+ -[RTPersistenceDriver _cleanUpFileDescriptoersForPersistenceStore]
+ -[RTPurgeManager _cacheDateDependencyMomentsWithDateInterval:]
+ -[RTPurgeManager platform]
+ -[RTRelabelerPersister filteredVisitMOs:referenceMapItem:referencePlaceType:error:]
+ -[RTService isShuttingDown]
+ -[RTService setIsShuttingDown:]
+ -[RTStore _purgeDateInterval:predicateMappings:limit:handler:]
+ -[RTStore purgePredating:predicateMappings:purgeLimit:handler:]
+ -[RTVisitManager initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:motionActivityManager:platform:pointOfInterestMonitor:visitLabeler:visitStore:]
+ -[RTVisitManager motionActivityManager]
+ -[RTVisitManager setMotionActivityManager:]
+ -[RTVisitMonitor initWithDefaultsManager:deviceLocationPredictor:distanceCalculator:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:motionActivityManager:platform:queue:state:timerManager:visitLabeler:]
+ -[RTVisitMonitor initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:motionActivityManager:platform:queue:state:visitLabeler:]
+ -[RTVisitMonitor motionActivityManager]
+ -[RTVisitMonitor setMotionActivityManager:]
+ -[RTVisitPipelineModuleMotionStateTrimmer .cxx_destruct]
+ -[RTVisitPipelineModuleMotionStateTrimmer _fetchActivitiesWithinDateInterval:error:]
+ -[RTVisitPipelineModuleMotionStateTrimmer _trimVisitClusterForMotionActivity:]
+ -[RTVisitPipelineModuleMotionStateTrimmer initWithMotionActivityManager:defaultsManager:]
+ -[RTVisitPipelineModuleMotionStateTrimmer init]
+ -[RTVisitPipelineModuleMotionStateTrimmer motionAccumulatorParams]
+ -[RTVisitPipelineModuleMotionStateTrimmer motionActivityManager]
+ -[RTVisitPipelineModuleMotionStateTrimmer process:]
+ -[RTVisitPipelineMotionAccumulator .cxx_destruct]
+ -[RTVisitPipelineMotionAccumulator finishMotionObservations:]
+ -[RTVisitPipelineMotionAccumulator getTrimDate]
+ -[RTVisitPipelineMotionAccumulator initWithParams:processInReverse:]
+ -[RTVisitPipelineMotionAccumulator params]
+ -[RTVisitPipelineMotionAccumulator processActivitiesReverse]
+ -[RTVisitPipelineMotionAccumulator processMotionActivity:]
+ -[RTVisitPipelineMotionAccumulatorParams initWithDefaultsManager:]
+ -[RTVisitPipelineMotionAccumulatorParams init]
+ -[RTVisitPipelineMotionAccumulatorParams maxAllowedGapBetweenActiveMotionStates]
+ -[RTVisitPipelineMotionAccumulatorParams maxTimeToTrim]
+ -[RTVisitPipelineMotionAccumulatorParams minMotionDurationAtHighConfidence]
+ -[RTVisitPipelineMotionAccumulatorParams minMotionDurationAtMediumConfidence]
+ -[RTVisitPipelineMotionAccumulatorParams motionLookWindowOutsideVisit]
+ -[RTVisitPipelineMotionAccumulatorParams setMaxAllowedGapBetweenActiveMotionStates:]
+ -[RTVisitPipelineMotionAccumulatorParams setMaxTimeToTrim:]
+ -[RTVisitPipelineMotionAccumulatorParams setMinMotionDurationAtHighConfidence:]
+ -[RTVisitPipelineMotionAccumulatorParams setMinMotionDurationAtMediumConfidence:]
+ -[RTVisitPipelineMotionAccumulatorParams setMotionLookWindowOutsideVisit:]
+ -[RTXPCActivityManager deleteDefaultsForIdentifier:]
+ -[SMInitiatorService _shutdownWithHandler:]
+ -[SMInitiatorService checkAndDeleteKey:forIdentifier:]
+ -[SMInitiatorService deleteAllStoredDefaults]
+ -[SMInitiatorSessionInitializationRequest .cxx_destruct]
+ -[SMInitiatorSessionInitializationRequest description]
+ -[SMInitiatorSessionInitializationRequest handle]
+ -[SMInitiatorSessionInitializationRequest handler]
+ -[SMInitiatorSessionInitializationRequest hash]
+ -[SMInitiatorSessionInitializationRequest initWithSessionID:handle:handler:]
+ -[SMInitiatorSessionInitializationRequest isEqual:]
+ -[SMInitiatorSessionInitializationRequest sessionID]
+ -[SMInitiatorSessionInitializationRequest startDate]
+ -[SMMadridMessenger processSessionStartMessageSendResultWithMessageUrl:guid:successful:withError:]
+ -[SMReplayManager crowFliesWalkingSpeed]
+ -[SMReplayManager minDistanceETAUpdateThreshold]
+ -[SMReplayManager muteMapsExpectedETA]
+ -[SMReplayManager muteRouteDeviationTriggerWithinThreshold]
+ -[SMReplayManager objectForKey:value:]
+ -[SMReplayManager setCrowFliesWalkingSpeed:]
+ -[SMReplayManager setMinDistanceETAUpdateThreshold:]
+ -[SMReplayManager setMuteMapsExpectedETA:]
+ -[SMReplayManager setMuteRouteDeviationTriggerWithinThreshold:]
+ -[SMSafetyCacheStore _shutdownWithHandler:]
+ -[SMSuggestionsManager _deleteProactiveNotificationUponNavigationDestination:error:]
+ -[SMSuggestionsManager _deleteProactiveNotificationWithDestinationLocation:error:]
+ -[SMSuggestionsManager _deleteProactiveNotificationWithError:]
+ -[SMSuggestionsManager _isContactBlocked:error:]
+ GCC_except_table132
+ GCC_except_table141
+ GCC_except_table143
+ GCC_except_table147
+ GCC_except_table206
+ GCC_except_table231
+ GCC_except_table267
+ GCC_except_table294
+ GCC_except_table372
+ GCC_except_table380
+ _CFPhoneNumberCreate
+ _CKPartialErrorsByItemIDKey
+ _CMFBlockListIsItemBlocked
+ _CMFItemCreateWithEmailAddress
+ _CMFItemCreateWithPhoneNumber
+ _CPPhoneNumberCopyHomeCountryCode
+ _OBJC_CLASS_$_RTPeopleDensityTTR
+ _OBJC_CLASS_$_RTVisitPipelineModuleMotionStateTrimmer
+ _OBJC_CLASS_$_RTVisitPipelineMotionAccumulator
+ _OBJC_CLASS_$_RTVisitPipelineMotionAccumulatorParams
+ _OBJC_CLASS_$_SMInitiatorSessionInitializationRequest
+ _OBJC_CLASS_$_UIImage
+ _OBJC_IVAR_$_RTPeopleDensityRecord._defaultsManager
+ _OBJC_IVAR_$_RTPeopleDensityRecord._highDensityThreshold
+ _OBJC_IVAR_$_RTPeopleDensityTTR._defaultsManager
+ _OBJC_IVAR_$_RTPeopleDensityTTR._densityStore
+ _OBJC_IVAR_$_RTPeopleDensityTTR._queue
+ _OBJC_IVAR_$_RTPeopleDensityTTR._singleRecordsDescription
+ _OBJC_IVAR_$_RTPeopleDensityTTR._threshold
+ _OBJC_IVAR_$_RTPeopleDensityTTR._value
+ _OBJC_IVAR_$_RTService._isShuttingDown
+ _OBJC_IVAR_$_RTVisitMonitor._motionActivityManager
+ _OBJC_IVAR_$_RTVisitPipelineModuleMotionStateTrimmer._motionAccumulatorParams
+ _OBJC_IVAR_$_RTVisitPipelineModuleMotionStateTrimmer._motionActivityManager
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulator._foundIntervalToTrim
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulator._intervalStartDate
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulator._lastObservedMotionActivity
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulator._params
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulator._processActivitiesReverse
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulator._runningScoreHighConfidence
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulator._runningScoreMediumConfidence
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulatorParams._maxAllowedGapBetweenActiveMotionStates
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulatorParams._maxTimeToTrim
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulatorParams._minMotionDurationAtHighConfidence
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulatorParams._minMotionDurationAtMediumConfidence
+ _OBJC_IVAR_$_RTVisitPipelineMotionAccumulatorParams._motionLookWindowOutsideVisit
+ _OBJC_IVAR_$_SMInitiatorSessionInitializationRequest._handle
+ _OBJC_IVAR_$_SMInitiatorSessionInitializationRequest._handler
+ _OBJC_IVAR_$_SMInitiatorSessionInitializationRequest._sessionID
+ _OBJC_IVAR_$_SMInitiatorSessionInitializationRequest._startDate
+ _OBJC_IVAR_$_SMReplayManager._crowFliesWalkingSpeed
+ _OBJC_IVAR_$_SMReplayManager._minDistanceETAUpdateThreshold
+ _OBJC_IVAR_$_SMReplayManager._muteMapsExpectedETA
+ _OBJC_IVAR_$_SMReplayManager._muteRouteDeviationTriggerWithinThreshold
+ _OBJC_METACLASS_$_RTPeopleDensityTTR
+ _OBJC_METACLASS_$_RTVisitPipelineModuleMotionStateTrimmer
+ _OBJC_METACLASS_$_RTVisitPipelineMotionAccumulator
+ _OBJC_METACLASS_$_RTVisitPipelineMotionAccumulatorParams
+ _OBJC_METACLASS_$_SMInitiatorSessionInitializationRequest
+ _SMPeriodicCacheMaintenanceSchedulerXPCActivityIdentifier
+ _SMRoutinedBundleID
+ _SMScheduleSendCancelRetryXPCActivityIdentifier
+ __HKPrivateMetadataKeyWorkoutExtendedMode
+ __OBJC_$_CATEGORY_NSPersonNameComponents_$_SMExtensions
+ __OBJC_$_CLASS_METHODS_NSPersonNameComponents(SMExtensions)
+ __OBJC_$_CLASS_METHODS_RTPeopleDensityTTR
+ __OBJC_$_CLASS_METHODS_RTVisitPipelineMotionAccumulator
+ __OBJC_$_CLASS_METHODS_RTVisitPipelineMotionAccumulatorParams
+ __OBJC_$_INSTANCE_METHODS_RTPeopleDensityTTR
+ __OBJC_$_INSTANCE_METHODS_RTVisitPipelineModuleMotionStateTrimmer
+ __OBJC_$_INSTANCE_METHODS_RTVisitPipelineMotionAccumulator
+ __OBJC_$_INSTANCE_METHODS_RTVisitPipelineMotionAccumulatorParams
+ __OBJC_$_INSTANCE_METHODS_SMInitiatorSessionInitializationRequest
+ __OBJC_$_INSTANCE_VARIABLES_RTPeopleDensityTTR
+ __OBJC_$_INSTANCE_VARIABLES_RTService
+ __OBJC_$_INSTANCE_VARIABLES_RTVisitPipelineModuleMotionStateTrimmer
+ __OBJC_$_INSTANCE_VARIABLES_RTVisitPipelineMotionAccumulator
+ __OBJC_$_INSTANCE_VARIABLES_RTVisitPipelineMotionAccumulatorParams
+ __OBJC_$_INSTANCE_VARIABLES_SMInitiatorSessionInitializationRequest
+ __OBJC_$_PROP_LIST_RTPeopleDensityTTR
+ __OBJC_$_PROP_LIST_RTVisitPipelineModuleMotionStateTrimmer
+ __OBJC_$_PROP_LIST_RTVisitPipelineMotionAccumulator
+ __OBJC_$_PROP_LIST_RTVisitPipelineMotionAccumulatorParams
+ __OBJC_$_PROP_LIST_SMInitiatorSessionInitializationRequest
+ __OBJC_CLASS_PROTOCOLS_$_RTVisitPipelineModuleMotionStateTrimmer
+ __OBJC_CLASS_RO_$_RTPeopleDensityTTR
+ __OBJC_CLASS_RO_$_RTVisitPipelineModuleMotionStateTrimmer
+ __OBJC_CLASS_RO_$_RTVisitPipelineMotionAccumulator
+ __OBJC_CLASS_RO_$_RTVisitPipelineMotionAccumulatorParams
+ __OBJC_CLASS_RO_$_SMInitiatorSessionInitializationRequest
+ __OBJC_METACLASS_RO_$_RTPeopleDensityTTR
+ __OBJC_METACLASS_RO_$_RTVisitPipelineModuleMotionStateTrimmer
+ __OBJC_METACLASS_RO_$_RTVisitPipelineMotionAccumulator
+ __OBJC_METACLASS_RO_$_RTVisitPipelineMotionAccumulatorParams
+ __OBJC_METACLASS_RO_$_SMInitiatorSessionInitializationRequest
+ ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.142
+ ___111-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:includePlaceholders:handler:]_block_invoke.313
+ ___115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke.204
+ ___115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke.206
+ ___115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke_2.205
+ ___115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke_2.207
+ ___136-[RTLearnedPlaceTypeInferenceGenerator placeCandidateStatsForType:placeStats:dateInterval:excludingPlaces:parameters:distanceThreshold:]_block_invoke
+ ___140-[RTHealthKitManager getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:error:]_block_invoke
+ ___153-[RTHealthKitManager getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:]_block_invoke
+ ___170-[RTHealthKitManager getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:]_block_invoke
+ ___171-[RTHealthKitManager _getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:]_block_invoke
+ ___25-[RTDaemonClient restore]_block_invoke.496
+ ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.149
+ ___44-[RTLearnedLocationManager _logLearnedState]_block_invoke.76
+ ___44-[RTLearnedLocationManager _logLearnedState]_block_invoke.78
+ ___44-[RTLearnedLocationManager _logLearnedState]_block_invoke.82
+ ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.152
+ ___47-[RTLearnedLocationStore _removePlace:handler:]_block_invoke.396
+ ___47-[RTPeopleDensityTTR showHighDensityDetectedUI]_block_invoke
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.117
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.118
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.133
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.142
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.145
+ ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.517
+ ___51-[RTPeopleDiscoveryProvider _clearProximityEvents:]_block_invoke
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.433
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.435
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.437
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke_2.436
+ ___53-[RTVisitMonitor fetchVisitsFromDate:toDate:handler:]_block_invoke.135
+ ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.395
+ ___55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.516
+ ___55-[RTPeopleDensityTTR highPeopleDensityUIResponseFlags:]_block_invoke
+ ___56-[RTPeopleDensityTTR _highPeopleDensityUIResponseFlags:]_block_invoke
+ ___56-[RTPeopleDensityTTR _highPeopleDensityUIResponseFlags:]_block_invoke.66
+ ___56-[RTPeopleDiscoveryProvider _clearPeopleDensityBundles:]_block_invoke
+ ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.94
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.188
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.195
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.199
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.200
+ ___59-[RTLearnedLocationStore _fetchVisitIdentifiersIn:handler:]_block_invoke.262
+ ___59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.546
+ ___59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.542
+ ___59-[RTMapItemProviderLearnedPlace mapItemsWithOptions:error:]_block_invoke.25
+ ___59-[RTMapItemProviderLearnedPlace mapItemsWithOptions:error:]_block_invoke_2.26
+ ___59-[SMInitiatorService _initializeSessionWithHandle:handler:]_block_invoke.193
+ ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.296
+ ___60+[NSPersonNameComponents(SMExtensions) sharedNameComponents]_block_invoke
+ ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke.159
+ ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke_2.160
+ ___62-[RTStore _purgeDateInterval:predicateMappings:limit:handler:]_block_invoke
+ ___62-[SMTriggerDestination _updateInitiatorStatusDestinationBound]_block_invoke.197
+ ___63-[RTLearnedLocationManager _reconstructTransitionsWithHandler:]_block_invoke.235
+ ___63-[RTLearnedLocationManager _reconstructTransitionsWithHandler:]_block_invoke.237
+ ___63-[RTStore purgePredating:predicateMappings:purgeLimit:handler:]_block_invoke
+ ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.414
+ ___65-[SMReplayManager _fetchEstimatedLocationAtDate:options:handler:]_block_invoke.129
+ ___65-[SMSessionStore _fetchSessionConfigurationsWithOptions:handler:]_block_invoke_3
+ ___66-[RTLearnedLocationStore _removeRecordsExpiredBeforeDate:handler:]_block_invoke.488
+ ___66-[RTPersistenceDriver _cleanUpFileDescriptoersForPersistenceStore]_block_invoke
+ ___66-[SMInitiatorService _fetchSessionReceiptForSessionID:completion:]_block_invoke.201
+ ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.488
+ ___67-[SMInitiatorService _startFrequentSingleShotFetchAllZonesActivity]_block_invoke.172
+ ___67-[SMInitiatorService _startInfrequentPeriodicFetchAllZonesActivity]_block_invoke.180
+ ___67-[SMSuggestionsManager _fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.215
+ ___68-[RTLearnedLocationStore _fetchLocationOfInterestWithPlace:handler:]_block_invoke.349
+ ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.509
+ ___70-[RTLearnedLocationStore _fetchLocationOfInterestWithMapItem:handler:]_block_invoke.345
+ ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.227
+ ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.234
+ ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.236
+ ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.212
+ ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.269
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.182
+ ___73-[RTLearnedLocationStore _fetchLocationOfInterestVisitedLastWithHandler:]_block_invoke.337
+ ___73-[RTLearnedLocationStore _fetchLocationOfInterestWithIdentifier:handler:]_block_invoke.341
+ ___73-[RTLearnedLocationStore _fetchLocationsOfInterestWithPlaceType:handler:]_block_invoke.302
+ ___74-[RTLearnedLocationStore _fetchInferredMapItemForVisitIdentifier:handler:]_block_invoke.335
+ ___74-[RTLearnedLocationStore _fetchLocationOfInterestVisitedFirstWithHandler:]_block_invoke.336
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.483
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.484
+ ___76-[RTLearnedLocationStore _fetchTransitionsBetweenStartDate:endDate:handler:]_block_invoke.276
+ ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.362
+ ___78-[RTLearnedPlaceTypeInferenceGenerator _getCandidatePlaceStatsFromPlaceStats:]_block_invoke
+ ___78-[RTSensitiveDateClassifier fetchLookbackWindowStartDateWithLocation:handler:]_block_invoke.14
+ ___78-[RTSensitiveDateClassifier fetchLookbackWindowStartDateWithLocation:handler:]_block_invoke.16
+ ___78-[RTSensitiveDateClassifier fetchLookbackWindowStartDateWithLocation:handler:]_block_invoke_2.17
+ ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.513
+ ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.472
+ ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.491
+ ___82-[SMSuggestionsManager _deleteProactiveNotificationWithDestinationLocation:error:]_block_invoke
+ ___83-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:endDate:handler:]_block_invoke.258
+ ___83-[RTLearnedLocationStore _fetchLocationsOfInterestWithinDistance:location:handler:]_block_invoke.298
+ ___84-[RTVisitPipelineModuleMotionStateTrimmer _fetchActivitiesWithinDateInterval:error:]_block_invoke
+ ___84-[SMSuggestionsManager _deleteProactiveNotificationUponNavigationDestination:error:]_block_invoke
+ ___85-[RTLearnedLocationManager _getAreasGeohashesFamiliarPlacesWithGranularity:outError:]_block_invoke.268
+ ___85-[RTLearnedLocationManager _getAreasGeohashesFamiliarPlacesWithGranularity:outError:]_block_invoke.270
+ ___86-[RTLearnedLocationStore _fetchVisitsWithIncompletePlacesForCurrentDeviceWithHandler:]_block_invoke.375
+ ___88-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:customLabel:handler:]_block_invoke.208
+ ___91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.517
+ ___92-[RTLearnedPlaceTypeInferenceGenerator filteredPlaceStatsByWeeklyVisitThreshold:placeStats:]_block_invoke
+ ___93-[RTLearnedLocationManager _fetchDedupedLocationOfInterestIdentifiersWithIdentifier:handler:]_block_invoke.225
+ ___94-[RTLearnedLocationStore _fetchLocationOfInterestTransitionsBetweenStartDate:endDate:handler:]_block_invoke.362
+ ___95-[RTLearnedLocationStore fetchCountOfVisitsToLocationOfInterestWithIdentifier:endDate:handler:]_block_invoke
+ ___96-[RTLearnedLocationStore _fetchCountOfVisitsToLocationOfInterestWithIdentifier:endDate:handler:]_block_invoke
+ ___96-[RTLearnedLocationStore _fetchCountOfVisitsToLocationOfInterestWithIdentifier:endDate:handler:]_block_invoke.257
+ ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.401
+ ___97-[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngineWithPlaceStats:dateInterval:]_block_invoke
+ ___97-[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngineWithPlaceStats:dateInterval:]_block_invoke.400
+ ___MomentsOnboardingAndSettingsLibraryCore_block_invoke
+ ____RTSemaphoreWait_block_invoke
+ ___block_descriptor_106_e8_32s40s48s56s64s72r80r_e5_v8?0lr72l8s32l8s40l8s48l8s56l8s64l8r80l8
+ ___block_descriptor_32_e35_v32?0"NSString"8"NSNumber"16^B24l
+ ___block_descriptor_32_e64_B24?0"RTLearnedPlaceTypeInferencePlaceStats"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32s_e59_q24?0"SMSessionConfiguration"8"SMSessionConfiguration"16ls32l8
+ ___block_descriptor_48_e8_32s40r_e31_v32?0"RTLearnedPlace"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e31_v32?0"RTLearnedPlace"8Q16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e44_v32?0"RTLearnedLocationOfInterest"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e32_v16?0"NSManagedObjectContext"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_90_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8r72l8
+ ___block_literal_global.122
+ ___block_literal_global.135
+ ___block_literal_global.140
+ ___block_literal_global.147
+ ___block_literal_global.151
+ ___block_literal_global.319
+ ___block_literal_global.334
+ ___block_literal_global.361
+ ___block_literal_global.367
+ ___block_literal_global.368
+ ___block_literal_global.409
+ ___block_literal_global.416
+ ___block_literal_global.440
+ ___block_literal_global.490
+ ___block_literal_global.493
+ ___block_literal_global.498
+ ___block_literal_global.520
+ ___block_literal_global.531
+ ___block_literal_global.536
+ ___block_literal_global.691
+ ___block_literal_global.839
+ ___block_literal_global.85
+ ___block_literal_global.98
+ ___getMOOnboardingManagerClass_block_invoke
+ __unnamed_array_storage.159
+ __unnamed_array_storage.197
+ __unnamed_array_storage.225
+ _audit_stringMomentsOnboardingAndSettings
+ _kSMSuggestionProactiveNotificationTearDownDistanceCloseBy
+ _kSMSuggestionProactiveNotificationTearDownDistanceFromNavigationDestination
+ _objc_msgSend$_cacheDateDependencyMomentsWithDateInterval:
+ _objc_msgSend$_cleanUpFileDescriptoersForPersistenceStore
+ _objc_msgSend$_clearPeopleDensityBundles:
+ _objc_msgSend$_clearProximityEvents:
+ _objc_msgSend$_deleteProactiveNotificationUponNavigationDestination:error:
+ _objc_msgSend$_deleteProactiveNotificationWithDestinationLocation:error:
+ _objc_msgSend$_deleteProactiveNotificationWithError:
+ _objc_msgSend$_fetchActivitiesWithinDateInterval:error:
+ _objc_msgSend$_fetchCountOfVisitsToLocationOfInterestWithIdentifier:endDate:handler:
+ _objc_msgSend$_getCandidatePlaceStatsFromPlaceStats:
+ _objc_msgSend$_getFullLocationHistoryDateInterval
+ _objc_msgSend$_getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:
+ _objc_msgSend$_getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:error:
+ _objc_msgSend$_getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:
+ _objc_msgSend$_highPeopleDensityUIResponseFlags:
+ _objc_msgSend$_isContactBlocked:error:
+ _objc_msgSend$_prepareMLFeaturesWithPlaceStats:
+ _objc_msgSend$_purgeDateInterval:predicateMappings:limit:handler:
+ _objc_msgSend$_showHighDensityDetectedUI
+ _objc_msgSend$_trimVisitClusterForMotionActivity:
+ _objc_msgSend$bundleWithPath:
+ _objc_msgSend$checkAndDeleteKey:forIdentifier:
+ _objc_msgSend$cleanUpOngoingContactRecordsAndScores
+ _objc_msgSend$cleanUpOngoingPeopleDensityBundle
+ _objc_msgSend$copyKeyListContainingString:
+ _objc_msgSend$deleteAllStoredDefaults
+ _objc_msgSend$deleteDefaultsForIdentifier:
+ _objc_msgSend$fetchCountOfVisitsToLocationOfInterestWithIdentifier:endDate:handler:
+ _objc_msgSend$filteredPlaceStatsByWeeklyVisitThreshold:placeStats:
+ _objc_msgSend$filteredVisitMOs:referenceMapItem:referencePlaceType:error:
+ _objc_msgSend$finishMotionObservations:
+ _objc_msgSend$getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:
+ _objc_msgSend$getTrimDate
+ _objc_msgSend$getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:error:
+ _objc_msgSend$getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:
+ _objc_msgSend$highPeopleDensityUIResponseFlags:
+ _objc_msgSend$imageNamed:inBundle:withConfiguration:
+ _objc_msgSend$inferPlaceTypesFromDailyPatternsWithPlaceStats:dateInterval:
+ _objc_msgSend$inferPlaceTypesFromFallbackWithPlaceStats:dateInterval:
+ _objc_msgSend$inferPlaceTypesFromModelWithCandidateSelection:homeModelType:workModelType:placeStats:dateInterval:
+ _objc_msgSend$inferPlaceTypesFromModelWithPlaceStats:dateInterval:
+ _objc_msgSend$inferPlaceTypesFromRuleEngineWithPlaceStats:dateInterval:
+ _objc_msgSend$inferPlaceTypesFromTopMedianDwellTimeWithPlaceStats:dateInterval:
+ _objc_msgSend$initWithDefaultsManager:deviceLocationPredictor:distanceCalculator:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:motionActivityManager:platform:queue:state:timerManager:visitLabeler:
+ _objc_msgSend$initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:motionActivityManager:platform:pointOfInterestMonitor:visitLabeler:visitStore:
+ _objc_msgSend$initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:motionActivityManager:platform:queue:state:visitLabeler:
+ _objc_msgSend$initWithMotionActivityManager:defaultsManager:
+ _objc_msgSend$initWithParams:processInReverse:
+ _objc_msgSend$initWithQueue:value:threshold:defaultsManager:densityStore:singleRecords:
+ _objc_msgSend$isActivityTypeMotionTrimmable:
+ _objc_msgSend$isSameSession:
+ _objc_msgSend$isShuttingDown
+ _objc_msgSend$loadParameterFromDefaults:parameterName:defaultValue:
+ _objc_msgSend$maxAllowedGapBetweenActiveMotionStates
+ _objc_msgSend$maxTimeToTrim
+ _objc_msgSend$minMotionDurationAtHighConfidence
+ _objc_msgSend$minMotionDurationAtMediumConfidence
+ _objc_msgSend$motionLookWindowOutsideVisit
+ _objc_msgSend$onboardingFlowCompletionStatus
+ _objc_msgSend$placeCandidateStatsForType:placeStats:dateInterval:excludingPlaces:parameters:distanceThreshold:
+ _objc_msgSend$placeCandidatesFromDailyPatternsForType:placeStats:parameters:
+ _objc_msgSend$placeCandidatesFromTopMedianDwellTimeForType:placeStats:parameters:
+ _objc_msgSend$processMotionActivity:
+ _objc_msgSend$processSessionStartMessageSendResultWithMessageUrl:guid:successful:withError:
+ _objc_msgSend$purgePredating:predicateMappings:purgeLimit:handler:
+ _objc_msgSend$setIsShuttingDown:
+ _objc_msgSend$sharedNameComponents
+ _objc_msgSend$showHighDensityDetectedUI
+ _objc_msgSend$tryShowingHighDensityDetectedUIWithValue:threshold:defaultsManager:densityStore:singleRecords:
+ _staticHighPeopleDensityUIResponseHandler
- -[RTHealthKitManager _getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:]
- -[RTHealthKitManager _getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:error:]
- -[RTHealthKitManager _getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:]
- -[RTHealthKitManager getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:]
- -[RTHealthKitManager getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:error:]
- -[RTHealthKitManager getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:]
- -[RTLearnedPlaceTypeInferenceGenerator _prepareMLFeatures]
- -[RTLearnedPlaceTypeInferenceGenerator filteredPlaceStatsByWeeklyVisitThreshold:]
- -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromDailyPatterns]
- -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromFallback]
- -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromModelWithCandidateSelection:homeModelType:workModelType:]
- -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromModel]
- -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngine]
- -[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromTopMedianDwellTime]
- -[RTLearnedPlaceTypeInferenceGenerator placeCandidateStatsForType:excludingPlaces:parameters:distanceThreshold:]
- -[RTLearnedPlaceTypeInferenceGenerator placeCandidatesFromDailyPatternsForType:parameters:]
- -[RTLearnedPlaceTypeInferenceGenerator placeCandidatesFromTopMedianDwellTimeForType:parameters:]
- -[RTRelabelerPersister filteredVisitMOs:referenceLocation:error:]
- -[RTSensitiveDateClassifier currentLocationTimer]
- -[RTSensitiveDateClassifier setCurrentLocationTimer:]
- -[RTStore _purgeDateInterval:predicateMappings:handler:]
- -[RTVisitManager initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:platform:pointOfInterestMonitor:visitLabeler:visitStore:]
- -[RTVisitMonitor initWithDefaultsManager:deviceLocationPredictor:distanceCalculator:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:platform:queue:state:timerManager:visitLabeler:]
- -[RTVisitMonitor initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:platform:queue:state:visitLabeler:]
- -[SMInitiatorService dealloc]
- -[SMInitiatorSessionInitilizationRequest .cxx_destruct]
- -[SMInitiatorSessionInitilizationRequest description]
- -[SMInitiatorSessionInitilizationRequest handle]
- -[SMInitiatorSessionInitilizationRequest handler]
- -[SMInitiatorSessionInitilizationRequest hash]
- -[SMInitiatorSessionInitilizationRequest initWithSessionID:handle:handler:]
- -[SMInitiatorSessionInitilizationRequest isEqual:]
- -[SMInitiatorSessionInitilizationRequest sessionID]
- -[SMInitiatorSessionInitilizationRequest startDate]
- -[SMMadridMessenger processSesssionStartMessageSendResultWithMessageUrl:guid:successful:withError:]
- -[SMReplayManager objectForKey:]
- GCC_except_table125
- GCC_except_table127
- GCC_except_table201
- GCC_except_table226
- GCC_except_table262
- GCC_except_table289
- GCC_except_table367
- GCC_except_table375
- GCC_except_table82
- _OBJC_CLASS_$_SMInitiatorSessionInitilizationRequest
- _OBJC_IVAR_$_RTSensitiveDateClassifier._currentLocationTimer
- _OBJC_IVAR_$_SMInitiatorSessionInitilizationRequest._handle
- _OBJC_IVAR_$_SMInitiatorSessionInitilizationRequest._handler
- _OBJC_IVAR_$_SMInitiatorSessionInitilizationRequest._sessionID
- _OBJC_IVAR_$_SMInitiatorSessionInitilizationRequest._startDate
- _OBJC_METACLASS_$_SMInitiatorSessionInitilizationRequest
- _RTFamiliarityIndexLearnedLOITotalVisitsKey
- __OBJC_$_INSTANCE_METHODS_SMInitiatorSessionInitilizationRequest
- __OBJC_$_INSTANCE_VARIABLES_SMInitiatorSessionInitilizationRequest
- __OBJC_$_PROP_LIST_SMInitiatorSessionInitilizationRequest
- __OBJC_CLASS_RO_$_SMInitiatorSessionInitilizationRequest
- __OBJC_METACLASS_RO_$_SMInitiatorSessionInitilizationRequest
- ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.132
- ___111-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:includePlaceholders:handler:]_block_invoke.309
- ___112-[RTLearnedPlaceTypeInferenceGenerator placeCandidateStatsForType:excludingPlaces:parameters:distanceThreshold:]_block_invoke
- ___115-[RTHealthKitManager getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:error:]_block_invoke
- ___115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke.207
- ___115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke.209
- ___115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke_2.208
- ___115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke_2.210
- ___128-[RTHealthKitManager getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:]_block_invoke
- ___145-[RTHealthKitManager getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:]_block_invoke
- ___146-[RTHealthKitManager _getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:]_block_invoke
- ___25-[RTDaemonClient restore]_block_invoke.486
- ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.151
- ___44-[RTLearnedLocationManager _logLearnedState]_block_invoke.79
- ___44-[RTLearnedLocationManager _logLearnedState]_block_invoke.81
- ___44-[RTLearnedLocationManager _logLearnedState]_block_invoke.85
- ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.154
- ___47-[RTLearnedLocationStore _removePlace:handler:]_block_invoke.392
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.123
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.122
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.135
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.144
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.147
- ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.507
- ___50-[RTPeopleDiscoveryProvider clearProximityEvents:]_block_invoke_2
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.423
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.425
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.427
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke_2.426
- ___53-[RTVisitMonitor fetchVisitsFromDate:toDate:handler:]_block_invoke.131
- ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.385
- ___55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.512
- ___55-[RTPeopleDiscoveryProvider clearPeopleDensityBundles:]_block_invoke_2
- ___56-[RTStore _purgeDateInterval:predicateMappings:handler:]_block_invoke
- ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.98
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.187
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.191
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.192
- ___59-[RTLearnedLocationStore _fetchVisitIdentifiersIn:handler:]_block_invoke.258
- ___59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.542
- ___59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.538
- ___59-[RTMapItemProviderLearnedPlace mapItemsWithOptions:error:]_block_invoke_4
- ___59-[SMInitiatorService _initializeSessionWithHandle:handler:]_block_invoke.195
- ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.283
- ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke.155
- ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke_2.156
- ___62-[RTSensitiveDateClassifier _fetchCurrentLocationWithHandler:]_block_invoke_2
- ___62-[RTSensitiveDateClassifier _fetchCurrentLocationWithHandler:]_block_invoke_3
- ___62-[SMTriggerDestination _updateInitiatorStatusDestinationBound]_block_invoke.187
- ___63-[RTLearnedLocationManager _reconstructTransitionsWithHandler:]_block_invoke.240
- ___63-[RTLearnedLocationManager _reconstructTransitionsWithHandler:]_block_invoke.241
- ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.404
- ___65-[SMReplayManager _fetchEstimatedLocationAtDate:options:handler:]_block_invoke.114
- ___66-[RTLearnedLocationStore _removeRecordsExpiredBeforeDate:handler:]_block_invoke.484
- ___66-[SMInitiatorService _fetchSessionReceiptForSessionID:completion:]_block_invoke.203
- ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.478
- ___67-[SMInitiatorService _startFrequentSingleShotFetchAllZonesActivity]_block_invoke.174
- ___67-[SMInitiatorService _startInfrequentPeriodicFetchAllZonesActivity]_block_invoke.182
- ___67-[SMSuggestionsManager _fetchMostLikelyReceiverHandlesWithHandler:]_block_invoke.207
- ___68-[RTLearnedLocationStore _fetchLocationOfInterestWithPlace:handler:]_block_invoke.345
- ___69-[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngine]_block_invoke
- ___69-[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngine]_block_invoke.400
- ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.499
- ___70-[RTLearnedLocationStore _fetchLocationOfInterestWithMapItem:handler:]_block_invoke.341
- ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.211
- ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.226
- ___71-[SMSuggestionsManager _fetchMostLikelySessionDestinationsWithHandler:]_block_invoke.228
- ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.204
- ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.256
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.174
- ___73-[RTLearnedLocationStore _fetchLocationOfInterestVisitedLastWithHandler:]_block_invoke.333
- ___73-[RTLearnedLocationStore _fetchLocationOfInterestWithIdentifier:handler:]_block_invoke.337
- ___73-[RTLearnedLocationStore _fetchLocationsOfInterestWithPlaceType:handler:]_block_invoke.298
- ___74-[RTLearnedLocationStore _fetchInferredMapItemForVisitIdentifier:handler:]_block_invoke.331
- ___74-[RTLearnedLocationStore _fetchLocationOfInterestVisitedFirstWithHandler:]_block_invoke.332
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.473
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.474
- ___76-[RTLearnedLocationStore _fetchTransitionsBetweenStartDate:endDate:handler:]_block_invoke.272
- ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.352
- ___78-[RTSensitiveDateClassifier fetchLookbackWindowStartDateWithLocation:handler:]_block_invoke.17
- ___78-[RTSensitiveDateClassifier fetchLookbackWindowStartDateWithLocation:handler:]_block_invoke.19
- ___78-[RTSensitiveDateClassifier fetchLookbackWindowStartDateWithLocation:handler:]_block_invoke_2.20
- ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.503
- ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.462
- ___81-[RTLearnedPlaceTypeInferenceGenerator filteredPlaceStatsByWeeklyVisitThreshold:]_block_invoke
- ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.481
- ___83-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:endDate:handler:]_block_invoke.254
- ___83-[RTLearnedLocationStore _fetchLocationsOfInterestWithinDistance:location:handler:]_block_invoke.294
- ___85-[RTLearnedLocationManager _getAreasGeohashesFamiliarPlacesWithGranularity:outError:]_block_invoke.271
- ___85-[RTLearnedLocationManager _getAreasGeohashesFamiliarPlacesWithGranularity:outError:]_block_invoke.273
- ___86-[RTLearnedLocationStore _fetchVisitsWithIncompletePlacesForCurrentDeviceWithHandler:]_block_invoke.371
- ___88-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:customLabel:handler:]_block_invoke.211
- ___91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.513
- ___93-[RTLearnedLocationManager _fetchDedupedLocationOfInterestIdentifiersWithIdentifier:handler:]_block_invoke.228
- ___94-[RTLearnedLocationStore _fetchLocationOfInterestTransitionsBetweenStartDate:endDate:handler:]_block_invoke.358
- ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.391
- ___RTSemaphoreWait_block_invoke
- ___block_descriptor_105_e8_32s40s48s56s64s72r80r_e5_v8?0lr72l8s32l8s40l8s48l8s56l8s64l8r80l8
- ___block_descriptor_32_e32_"NSUUID"16?0"RTLearnedPlace"8l
- ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48r56r_e44_v32?0"RTLearnedLocationOfInterest"8Q16^B24lr48l8s32l8s40l8r56l8
- ___block_descriptor_80_e8_32s40s48s56r64r72r_e29_v24?0"NSArray"8"NSError"16lr56l8s32l8s40l8r64l8r72l8s48l8
- ___block_descriptor_81_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
- ___block_descriptor_89_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8r72l8
- ___block_literal_global.100
- ___block_literal_global.131
- ___block_literal_global.133
- ___block_literal_global.143
- ___block_literal_global.149
- ___block_literal_global.153
- ___block_literal_global.156
- ___block_literal_global.179
- ___block_literal_global.216
- ___block_literal_global.218
- ___block_literal_global.224
- ___block_literal_global.313
- ___block_literal_global.329
- ___block_literal_global.331
- ___block_literal_global.351
- ___block_literal_global.354
- ___block_literal_global.357
- ___block_literal_global.430
- ___block_literal_global.480
- ___block_literal_global.483
- ___block_literal_global.488
- ___block_literal_global.516
- ___block_literal_global.527
- ___block_literal_global.534
- ___block_literal_global.677
- ___block_literal_global.833
- ___block_literal_global.84
- ___block_literal_global.88
- __unnamed_array_storage.151
- __unnamed_array_storage.217
- __unnamed_array_storage.222
- __unnamed_array_storage.80
- _lookbackWindowCurrentLocationTimerIdentifier
- _objc_msgSend$_getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:
- _objc_msgSend$_getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:error:
- _objc_msgSend$_getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:
- _objc_msgSend$_prepareMLFeatures
- _objc_msgSend$_purgeDateInterval:predicateMappings:handler:
- _objc_msgSend$currentLocationTimer
- _objc_msgSend$fetchCountOfVisitsToPlaceWithIdentifier:endDate:handler:
- _objc_msgSend$filteredPlaceStatsByWeeklyVisitThreshold:
- _objc_msgSend$filteredVisitMOs:referenceLocation:error:
- _objc_msgSend$getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:
- _objc_msgSend$getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:error:
- _objc_msgSend$getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:
- _objc_msgSend$inferPlaceTypesFromDailyPatterns
- _objc_msgSend$inferPlaceTypesFromFallback
- _objc_msgSend$inferPlaceTypesFromModel
- _objc_msgSend$inferPlaceTypesFromModelWithCandidateSelection:homeModelType:workModelType:
- _objc_msgSend$inferPlaceTypesFromRuleEngine
- _objc_msgSend$inferPlaceTypesFromTopMedianDwellTime
- _objc_msgSend$initWithDefaultsManager:deviceLocationPredictor:distanceCalculator:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:platform:queue:state:timerManager:visitLabeler:
- _objc_msgSend$initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:platform:pointOfInterestMonitor:visitLabeler:visitStore:
- _objc_msgSend$initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:platform:queue:state:visitLabeler:
- _objc_msgSend$isSimilar:
- _objc_msgSend$placeCandidateStatsForType:excludingPlaces:parameters:distanceThreshold:
- _objc_msgSend$placeCandidatesFromDailyPatternsForType:parameters:
- _objc_msgSend$placeCandidatesFromTopMedianDwellTimeForType:parameters:
- _objc_msgSend$processSesssionStartMessageSendResultWithMessageUrl:guid:successful:withError:
- _objc_msgSend$setCurrentLocationTimer:
CStrings:
+ "\x01\x12\x14"
+ "\x02.2"
+ "\x11!\x11"
+ "\x12(R"
+ "\x1e"
+ "\x1f\x02"
+ "#RTPeopleDensityProvider tryShowingHighDensityDetectedUI because %.1f > %.1f"
+ "#RTPeopleDensityRecord receives zero total scan duration when computing scores"
+ "#RTPeopleDensityRecord update bundle start time to, %@"
+ "#RTPeopleDiscoveryProvider receive advertisements, incomingAdvs count %lu, countSinceLastFetch %lu, scanDuration %f, earliestAdvertisementDate, %@"
+ "#SafetyCache,%@,%@,Partial failure - Failed to delete record with record ID %@ with error %@"
+ "#SafetyCache,%@,%@,Partial failure - Failed to save record %@ with error %@"
+ "#SafetyCache,%@,%@,failed to save records in zone with zoneID %@  after retries with recoverable error %@"
+ "#SafetyCache,%@,%@,failed to save records in zone with zoneID %@ with non recoverable error %@"
+ "#SafetyCache,%@,%@,failed to save records in zone with zoneID %@ with recoverable error %@, pendingRetryCount %d, retrying..."
+ "#SafetyCache,Initiator,%@,%@,deleted default for %@"
+ "#SafetyCache,Initiator,%@,%@,nil stored defaults for %@, early return"
+ "#SafetyCache,Initiator,%@,%@,received state sync req message for unmatched device identifier,%@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,failed to fetch record to write active session details with error %@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,safety cache update timed out"
+ "#SessionManager,Initiator,sessionID:%@,%@,%@,proccesing notification already processing magnetBreak %d"
+ "%@ %@: Failed to fetch motion activities at end, error, %@, for cluster %@"
+ "%@ %@: Failed to fetch motion activities at start, error, %@, for cluster %@"
+ "%@ %@: Trimming input cluster for motion, between %@ and %@"
+ "%@ %@: Visit culled, no locations between %@ and %@"
+ "%@ %@: Visit culled, only motion between %@ and %@"
+ "%@ %@: Visit end, number of detected moving activities: %lu."
+ "%@ %@: Visit start, number of detected moving activities: %lu."
+ "%@ %@: Visit trimming, entry date %@ -> %@, exit date %@ -> %@ Locations count %lu -> %lu"
+ "%@ %@: skipping cluster with null visit entry, %@ "
+ "%@ %@: working on cluster, %@"
+ "%@, %@, delete proactive notification status, %@, error, %@,"
+ "%@, %@, distance, %.3f, kSMSuggestionMinimimDistanceBetweenSourceAndDestination, %.3f, suggestion location, %@, destinationLocation, %@"
+ "%@, %@, distanceBetweenCurrentLocationAndNavigationDestination, %.3f, kSMSuggestionProactiveNotificationTearDownDistanceCloseBy, %.3f, latestLocationOfTheDevice, %@, navigationDestination, %@"
+ "%@, %@, distanceBetweenDestinations, %.3f, kSMSuggestionProactiveNotificationTearDownDistanceFromNavigationDestination, %.3f, suggestion location, %@, navigationDestination, %@"
+ "%@, %@, email, %@, isBlocked, %@"
+ "%@, %@, invalid start and end date, core motion pedometer data,\u00a0%@, error, %@,"
+ "%@, %@, learned place type, %@, placeInference is null, learned LOI, %@"
+ "%@, %@, phoneNumber, %@, countryCode, %@, isBlocked, %@"
+ "%@, %@, placeStats count, %lu, candidate placeStats count, %lu, dateInterval, %@"
+ "%@, %@, proactive notification deletion status, %@"
+ "%@, %@, reset states for pedometer data"
+ "%@, %@, suggestions count, %lu"
+ "%@, %@: Parameter updated: \"%@\", original value, %f, overridden value, %@"
+ "%@, onboarding flow completion status, %lu, earliest date required by moments, %@"
+ "%@, shutdown service, %@, error, %@, latency, %.2f"
+ "%K.%K >= %@"
+ "%s crowFliesWalkingSpeed, %.2f"
+ "%s invalid crowFliesWalkingSpeed, %.2f"
+ "%s minDistanceETAUptdateThreshold, %@"
+ "%s muteMapsExpectedETA, %@"
+ "%s muteRouteDeviationTriggerWithinThreshold, %@"
+ "%s, %s, original value, %.2f, overridden value, %.2f, by defaultsKey, %@"
+ "%s, NO, distance, %.2f, location_i, %@, location_j, %@, no progress distance threshold, %.2f"
+ "%s, YES, no significant change detected for cachedLocations count, %lu, no progress distance threshold, %.2f"
+ "%s, effectivePairedDevice, %@, effectivePairedDevice.nearby, %@, sessionID, %@, lastSessionIDDuringMagnetBreak, %@, magnetBreakTimer, %@, is state active state, %@, state, %@"
+ "&Attachments=%@"
+ "&ComponentID=1566449&ComponentName=Proximity&ComponentVersion=Gathering"
+ "+"
+ "-[RTHealthKitManager _getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:]"
+ "-[RTHealthKitManager getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:]"
+ "-[RTLearnedPlaceTypeInferenceGenerator placeCandidateStatsForType:placeStats:dateInterval:excludingPlaces:parameters:distanceThreshold:]"
+ "-[RTStore _purgeDateInterval:predicateMappings:limit:handler:]"
+ "-[RTVisitPipelineMotionAccumulator initWithParams:processInReverse:]"
+ "-[RTVisitPipelineMotionAccumulator processMotionActivity:]"
+ "-[SMReplayManager objectForKey:value:]"
+ "-[SMReplayManager setCrowFliesWalkingSpeed:]"
+ "-[SMReplayManager setMinDistanceETAUpdateThreshold:]"
+ "-[SMReplayManager setMuteMapsExpectedETA:]"
+ "-[SMReplayManager setMuteRouteDeviationTriggerWithinThreshold:]"
+ "/System/Library/Messages/iMessageApps/SafetyMonitorMessages.bundle"
+ "03:04:19"
+ "?Title=Detected%20High%20People%20Density"
+ "@\"RTVisitPipelineMotionAccumulatorParams\""
+ "@\"SMInitiatorSessionInitializationRequest\""
+ "@128@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120"
+ "@52@0:8B16Q20Q28@36@44"
+ "@56@0:8@16f24f28@32@40@48"
+ "@64@0:8@16@24d32B40B44@48^@56"
+ "@64@0:8Q16@24@32@40@48d56"
+ "@80@0:8@16q24@32@40d48B56B60@64^@72"
+ "CheckInMessagesAppIcon_32"
+ "Completed high people density value TTR, error %@"
+ "Dismiss forever"
+ "Error RTSemaphoreWait for TTR: sema %@ fetch %@"
+ "Error when creating density bundles JSON description for TTR: %@"
+ "Error when creating file %@ for TTR."
+ "Ignoring %lu locations for storage, shutdown in progress"
+ "Interval start not set (in %s:%d)"
+ "Invalid parameter not satisfying: contactInformation"
+ "Invalid parameter not satisfying: destinationLocation"
+ "Invalid parameter not satisfying: keySubstring"
+ "Invalid parameter not satisfying: manager"
+ "Invalid parameter not satisfying: motionAccumulatorParams (in %s:%d)"
+ "Invalid parameter not satisfying: navigationDestination"
+ "Invalid parameter not satisfying: referenceMapItem"
+ "MOOnboardingManager"
+ "Not enough identities available on device"
+ "Observed motion activity is out of expected order. Running in reverse: %u. Previous time %@, current time %@ (in %s:%d)"
+ "Oct 10 2023"
+ "PD detected a density value of %.1f, above %.1f.\n\nRecords:\n%@\n"
+ "Please file a radar if you think this should not be the case"
+ "Processing LOI, %@, near entry location, %@, consistent, %@"
+ "RTDefaultsPeopleDiscoveryProviderHighDensityDetection"
+ "RTDefaultsPeopleDiscoveryProviderHighDensityDetectionPopupThreshold"
+ "RTDefaultsPeopleDiscoveryProviderHighDensityThreshold"
+ "RTDefaultsSMTriggerDestinationMuteRouteDeviationTriggerWithinThresholdKey"
+ "RTDefaultsVisitPipelineMotionStateTrimmerDisabled"
+ "RTDefaultsVisitPipelineMotionStateTrimmerDurationAtHighConfidence"
+ "RTDefaultsVisitPipelineMotionStateTrimmerDurationAtMediumConfidence"
+ "RTDefaultsVisitPipelineMotionStateTrimmerLookOutsideVisit"
+ "RTDefaultsVisitPipelineMotionStateTrimmerMaxAllowedMotionGap"
+ "RTDefaultsVisitPipelineMotionStateTrimmerTimeToTrim"
+ "RTPeopleDensityTTR"
+ "RTVisitPipelineModuleMotionStateTrimmer"
+ "RTVisitPipelineMotionAccumulator"
+ "RTVisitPipelineMotionAccumulatorParams"
+ "SMExtensions"
+ "SMInitiatorSessionInitializationRequest"
+ "Shutdown Initiator Service"
+ "T@\"NSPersonNameComponents\",R,N"
+ "T@\"NSString\",&,N,V_singleRecordsDescription"
+ "T@\"RTPeopleDensityStore\",&,N,V_densityStore"
+ "T@\"RTVisitPipelineMotionAccumulatorParams\",R,N,V_motionAccumulatorParams"
+ "T@\"RTVisitPipelineMotionAccumulatorParams\",R,N,V_params"
+ "T@\"SMInitiatorSessionInitializationRequest\",&,N,V_pendingInitializationRequest"
+ "TB,N,V_isShuttingDown"
+ "TB,R,N,V_processActivitiesReverse"
+ "TTR not showing pop-up because popupDisabledCond %d noThresholdCond %d probabilisticCond %d, roll %.3f"
+ "TTR not showing pop-up because there is one already"
+ "Td,N,V_crowFliesWalkingSpeed"
+ "Td,N,V_maxAllowedGapBetweenActiveMotionStates"
+ "Td,N,V_maxTimeToTrim"
+ "Td,N,V_minDistanceETAUpdateThreshold"
+ "Td,N,V_minMotionDurationAtHighConfidence"
+ "Td,N,V_minMotionDurationAtMediumConfidence"
+ "Td,N,V_motionLookWindowOutsideVisit"
+ "Td,N,V_muteMapsExpectedETA"
+ "Td,N,V_muteRouteDeviationTriggerWithinThreshold"
+ "Tf,N,V_highDensityThreshold"
+ "Tf,N,V_threshold"
+ "Tf,N,V_value"
+ "[Internal Only] High People Density detected (%.1f above %.1f threshold).\n"
+ "_cacheDateDependencyMomentsWithDateInterval:"
+ "_cleanUpFileDescriptoersForPersistenceStore"
+ "_clearPeopleDensityBundles:"
+ "_clearProximityEvents:"
+ "_crowFliesWalkingSpeed"
+ "_deleteProactiveNotificationUponNavigationDestination:error:"
+ "_deleteProactiveNotificationWithDestinationLocation:error:"
+ "_deleteProactiveNotificationWithError:"
+ "_densityStore"
+ "_fetchActivitiesWithinDateInterval:error:"
+ "_fetchCountOfVisitsToLocationOfInterestWithIdentifier:endDate:handler:"
+ "_foundIntervalToTrim"
+ "_getCandidatePlaceStatsFromPlaceStats:"
+ "_getFullLocationHistoryDateInterval"
+ "_getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:"
+ "_getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:error:"
+ "_getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:"
+ "_highDensityThreshold"
+ "_highPeopleDensityUIResponseFlags:"
+ "_intervalStartDate"
+ "_isContactBlocked:error:"
+ "_isShuttingDown"
+ "_lastObservedMotionActivity"
+ "_maxAllowedGapBetweenActiveMotionStates"
+ "_maxTimeToTrim"
+ "_minDistanceETAUpdateThreshold"
+ "_minMotionDurationAtHighConfidence"
+ "_minMotionDurationAtMediumConfidence"
+ "_motionAccumulatorParams"
+ "_motionLookWindowOutsideVisit"
+ "_muteMapsExpectedETA"
+ "_muteRouteDeviationTriggerWithinThreshold"
+ "_params"
+ "_prepareMLFeaturesWithPlaceStats:"
+ "_processActivitiesReverse"
+ "_purgeDateInterval:predicateMappings:limit:handler:"
+ "_runningScoreHighConfidence"
+ "_runningScoreMediumConfidence"
+ "_showHighDensityDetectedUI"
+ "_singleRecordsDescription"
+ "_threshold"
+ "_trimVisitClusterForMotionActivity:"
+ "_value"
+ "bundleWithPath:"
+ "checkAndDeleteKey:forIdentifier:"
+ "cleanUpOngoingContactRecordsAndScores"
+ "cleanUpOngoingPeopleDensityBundle"
+ "com.apple.coreroutine.peopleDiscovery.highDensity.ttr"
+ "contactInformation"
+ "copyKeyListContainingString:"
+ "crowFliesWalkingSpeed"
+ "deleteAllStoredDefaults"
+ "deleteDefaultsForIdentifier:"
+ "density-bundles.json"
+ "densityBundles"
+ "densityStore"
+ "f"
+ "fetchCountOfVisitsToLocationOfInterestWithIdentifier:endDate:handler:"
+ "filteredPlaceStatsByWeeklyVisitThreshold:placeStats:"
+ "filteredVisitMOs:referenceMapItem:referencePlaceType:error:"
+ "finishMotionObservations:"
+ "getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:"
+ "getTrimDate"
+ "getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:error:"
+ "getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:includePastureModeRoutes:workoutTypes:error:"
+ "highDensityThreshold"
+ "highPeopleDensityUIResponseFlags:"
+ "imageNamed:inBundle:withConfiguration:"
+ "inferPlaceTypesFromDailyPatternsWithPlaceStats:dateInterval:"
+ "inferPlaceTypesFromFallbackWithPlaceStats:dateInterval:"
+ "inferPlaceTypesFromModelWithCandidateSelection:homeModelType:workModelType:placeStats:dateInterval:"
+ "inferPlaceTypesFromModelWithPlaceStats:dateInterval:"
+ "inferPlaceTypesFromRuleEngineWithPlaceStats:dateInterval:"
+ "inferPlaceTypesFromTopMedianDwellTimeWithPlaceStats:dateInterval:"
+ "initWithDefaultsManager:deviceLocationPredictor:distanceCalculator:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:motionActivityManager:platform:queue:state:timerManager:visitLabeler:"
+ "initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:motionActivityManager:platform:pointOfInterestMonitor:visitLabeler:visitStore:"
+ "initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:motionActivityManager:platform:queue:state:visitLabeler:"
+ "initWithMotionActivityManager:defaultsManager:"
+ "initWithParams:processInReverse:"
+ "initWithQueue:value:threshold:defaultsManager:densityStore:singleRecords:"
+ "isActivityTypeMotionTrimmable:"
+ "isSameSession:"
+ "isShuttingDown"
+ "loadParameterFromDefaults:parameterName:defaultValue:"
+ "maxAllowedGapBetweenActiveMotionStates"
+ "maxTimeToTrim"
+ "minDistanceETAUpdateThreshold"
+ "minMotionDurationAtHighConfidence"
+ "minMotionDurationAtMediumConfidence"
+ "motionAccumulatorParams"
+ "motionLookWindowOutsideVisit"
+ "muteMapsExpectedETA"
+ "muteRouteDeviationTriggerWithinThreshold"
+ "onboardingFlowCompletionStatus"
+ "params"
+ "placeCandidateStatsForType:placeStats:dateInterval:excludingPlaces:parameters:distanceThreshold:"
+ "placeCandidatesFromDailyPatternsForType:placeStats:parameters:"
+ "placeCandidatesFromTopMedianDwellTimeForType:placeStats:parameters:"
+ "processActivitiesReverse"
+ "processMotionActivity:"
+ "processSessionStartMessageSendResultWithMessageUrl:guid:successful:withError:"
+ "purgePredating:predicateMappings:purgeLimit:handler:"
+ "q56@0:8@16@24d32B40B44^@48"
+ "referenceMapItem"
+ "setCrowFliesWalkingSpeed:"
+ "setDensityStore:"
+ "setHighDensityThreshold:"
+ "setIsShuttingDown:"
+ "setMaxAllowedGapBetweenActiveMotionStates:"
+ "setMaxTimeToTrim:"
+ "setMinDistanceETAUpdateThreshold:"
+ "setMinMotionDurationAtHighConfidence:"
+ "setMinMotionDurationAtMediumConfidence:"
+ "setMotionLookWindowOutsideVisit:"
+ "setMuteMapsExpectedETA:"
+ "setMuteRouteDeviationTriggerWithinThreshold:"
+ "setSingleRecordsDescription:"
+ "setThreshold:"
+ "sharedNameComponents"
+ "showHighDensityDetectedUI"
+ "singleRecordsDescription"
+ "softlink:r:path:/System/Library/PrivateFrameworks/MomentsOnboardingAndSettings.framework/MomentsOnboardingAndSettings"
+ "tapToRadarURL %@"
+ "threshold"
+ "tryShowingHighDensityDetectedUIWithValue:threshold:defaultsManager:densityStore:singleRecords:"
+ "v20@0:8f16"
+ "v48@0:8f16f20@24@32@40"
- "\x01\x12\x13"
- "\x02-2"
- "\x12(\x12"
- "\x1d"
- "#RTPeopleDensityRecord fail to update record due to invalid reference date, %@"
- "#RTPeopleDensityRecord receives zero total scan duraton when computing scores"
- "#RTPeopleDiscoveryProvider receive advertisements, incomingAdvs count %lu, countSinceLastFetch %lu, scanDuration %f"
- "#SafetyCache,Initiator,%@,%@,received state sync req message for unmatched device identifer,%@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,failed to fetch record to write active session detais with error %@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,safety cache update timedout"
- "#SessionManager,Initiator,sessionID:%@,%@,%@,proccesing notification already proccesing magnetBreak %d"
- "%@, %@, learned place type, %@, placeInference is null, learnde LOI, %@"
- "%@, %@, resetted states for pedometer data"
- "%@, shutdown listener, %@, latency, %.2f"
- "%s, %s, original value, %.2f, overriden value, %.2f, by defaultsKey, %@"
- "%s, Current location after gps request, %@, error, %@"
- "%s, distance, %.2f, location_i, %@, location_j, %@, no progress distance threshold, %.2f"
- "%s, effectivePariedDevice, %@, effectivePairedDevice.nearby, %@, sessionID, %@, lastSessionIDDuringMagnetBreak, %@, magnetBreakTimer, %@, is state active state, %@, state, %@"
- "%s, no significant change detected for cachedLocations count, %lu, no progress distance threshold, %.2f"
- "-[RTHealthKitManager _getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:]"
- "-[RTHealthKitManager getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:]"
- "-[RTLearnedPlaceTypeInferenceGenerator placeCandidateStatsForType:excludingPlaces:parameters:distanceThreshold:]"
- "-[RTSensitiveDateClassifier _fetchCurrentLocationWithHandler:]_block_invoke_3"
- "-[RTStore _purgeDateInterval:predicateMappings:handler:]"
- "-[SMReplayManager objectForKey:]"
- "18:05:34"
- "@\"NSUUID\"16@?0@\"RTLearnedPlace\"8"
- "@\"SMInitiatorSessionInitilizationRequest\""
- "@36@0:8B16Q20Q28"
- "@48@0:8Q16@24@32d40"
- "@60@0:8@16@24d32B40@44^@52"
- "@76@0:8@16q24@32@40d48B56@60^@68"
- "Failed to fetch learned places with error %@"
- "Processing LOI, %@, near entry location, %@, consistent?, %@"
- "RTSensitiveDateClassifierCurrentLocationTimer"
- "SMInitiatorSessionInitilizationRequest"
- "Sep 30 2023"
- "T@\"RTTimer\",&,N,V_currentLocationTimer"
- "T@\"SMInitiatorSessionInitilizationRequest\",&,N,V_pendingInitializationRequest"
- "_currentLocationTimer"
- "_getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:"
- "_getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:error:"
- "_getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:"
- "_prepareMLFeatures"
- "_purgeDateInterval:predicateMappings:handler:"
- "currentLocationTimer"
- "filteredPlaceStatsByWeeklyVisitThreshold:"
- "filteredVisitMOs:referenceLocation:error:"
- "getLatestWorkoutWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:"
- "getWorkoutsCountWithStartDate:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:error:"
- "getWorkoutsWithStartDate:limit:sortDescriptors:nearLocation:distanceThreshold:onlySourcedFromFitnessApp:workoutTypes:error:"
- "inferPlaceTypesFromDailyPatterns"
- "inferPlaceTypesFromFallback"
- "inferPlaceTypesFromModel"
- "inferPlaceTypesFromModelWithCandidateSelection:homeModelType:workModelType:"
- "inferPlaceTypesFromRuleEngine"
- "inferPlaceTypesFromTopMedianDwellTime"
- "initWithDefaultsManager:deviceLocationPredictor:distanceCalculator:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:platform:queue:state:timerManager:visitLabeler:"
- "initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:platform:pointOfInterestMonitor:visitLabeler:visitStore:"
- "initWithDefaultsManager:deviceLocationPredictor:hintManager:learnedLocationManager:locationAwarenessManager:locationManager:metricManager:platform:queue:state:visitLabeler:"
- "isSimilar:"
- "placeCandidateStatsForType:excludingPlaces:parameters:distanceThreshold:"
- "placeCandidatesFromDailyPatternsForType:parameters:"
- "placeCandidatesFromTopMedianDwellTimeForType:parameters:"
- "processSesssionStartMessageSendResultWithMessageUrl:guid:successful:withError:"
- "q52@0:8@16@24d32B40^@44"
- "setCurrentLocationTimer:"
- "totalVisitsLOI"
- "your destination"

```
