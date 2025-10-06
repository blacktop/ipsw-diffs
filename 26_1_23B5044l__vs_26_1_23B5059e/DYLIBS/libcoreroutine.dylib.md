## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1067.0.2.0.0
-  __TEXT.__text: 0x60b3bc
+1069.0.1.0.0
+  __TEXT.__text: 0x614ff0
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x310e0
-  __TEXT.__const: 0x4658
+  __TEXT.__objc_methlist: 0x31510
+  __TEXT.__const: 0x4928
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x768b4
-  __TEXT.__cstring: 0x45669
+  __TEXT.__oslogstring: 0x78185
+  __TEXT.__cstring: 0x45fcb
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c

   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x28cb8
+  __TEXT.__gcc_except_tab: 0x28d74
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xdcb0
+  __TEXT.__unwind_info: 0xddc8
   __TEXT.__eh_frame: 0x390
-  __TEXT.__objc_classname: 0x58ca
-  __TEXT.__objc_methname: 0x9184b
-  __TEXT.__objc_methtype: 0xcfd0
-  __TEXT.__objc_stubs: 0x55ba0
-  __DATA_CONST.__got: 0x30f8
-  __DATA_CONST.__const: 0xf550
+  __TEXT.__objc_classname: 0x58cf
+  __TEXT.__objc_methname: 0x92fc9
+  __TEXT.__objc_methtype: 0xd0eb
+  __TEXT.__objc_stubs: 0x566c0
+  __DATA_CONST.__got: 0x3150
+  __DATA_CONST.__const: 0xf6c0
   __DATA_CONST.__objc_classlist: 0x1548
   __DATA_CONST.__objc_catlist: 0x3a8
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19480
+  __DATA_CONST.__objc_selrefs: 0x19788
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x1198
-  __DATA_CONST.__objc_arraydata: 0x2a10
+  __DATA_CONST.__objc_superrefs: 0x1190
+  __DATA_CONST.__objc_arraydata: 0x2b88
   __AUTH_CONST.__auth_got: 0x10d8
-  __AUTH_CONST.__const: 0x3240
-  __AUTH_CONST.__cfstring: 0x28a40
-  __AUTH_CONST.__objc_const: 0x50a60
-  __AUTH_CONST.__objc_intobj: 0x4608
-  __AUTH_CONST.__objc_arrayobj: 0xe88
+  __AUTH_CONST.__const: 0x32e0
+  __AUTH_CONST.__cfstring: 0x290a0
+  __AUTH_CONST.__objc_const: 0x50fb8
+  __AUTH_CONST.__objc_intobj: 0x48c0
+  __AUTH_CONST.__objc_arrayobj: 0xf00
   __AUTH_CONST.__objc_doubleobj: 0xb00
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x2258
-  __DATA.__objc_ivar: 0x2584
-  __DATA.__data: 0x2cc0
+  __AUTH.__objc_data: 0x2118
+  __DATA.__objc_ivar: 0x25e0
+  __DATA.__data: 0x2cc8
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_ivar: 0x1158
-  __DATA_DIRTY.__objc_data: 0xb330
+  __DATA_DIRTY.__objc_ivar: 0x116c
+  __DATA_DIRTY.__objc_data: 0xb470
   __DATA_DIRTY.__data: 0x5c8
   __DATA_DIRTY.__bss: 0x200
   __DATA_DIRTY.__common: 0x8

   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/WirelessDiagnostics.framework/WirelessDiagnostics
   - /usr/lib/libAWDSupportFramework.dylib
   - /usr/lib/libMobileGestalt.dylib

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
-  UUID: 1C850A04-E36F-35AA-A68F-55547CE308D0
-  Functions: 20204
-  Symbols:   65214
-  CStrings:  40218
+  UUID: 366DC65F-9B67-31E9-8E46-3F649D28FFE8
+  Functions: 20319
+  Symbols:   65598
+  CStrings:  40571
 
Symbols:
+ +[RTMapItemManager createMapItemFromMapItem:]
+ +[RTPOIHarvestUtilities harvestCuration:mapItem:visitLocations:poiHarvester:error:]
+ +[RTPredictedContextManager modelBinPath]
+ +[RTTripClusterWaypoint divideArray:intoChunks:]
+ +[RTTripClusterWaypoint getWaypointDataFromWaypoints:maxWaypointsPerChunk:]
+ +[RTUserCurationMetrics collectMetricsForAppliedLabel:curatedVisit:learnedLocationStore:distanceCalculator:applicationResult:error:]
+ -[CLPPoiHarvest(RTExtensions) initWithMapItem:accessPoints:locations:motionActivities:triggerType:]
+ -[CLPPoiTriggerEvent(RTExtensions) initWithMapItem:triggerType:date:]
+ -[NSError(RTExtensions) isBluePOITileNotAvailableError]
+ -[RTDataSerializer purgeWithError:]
+ -[RTLearnedLocationEngine _isUpdateLearnedPlaceWithGeomapItemIdentifierRequired:]
+ -[RTLearnedLocationEngine _shouldFilterError:]
+ -[RTLearnedLocationEngine _submitMetricsForApplicationOfCuratedLabel:visit:result:]
+ -[RTLearnedLocationEngine _updateLearnedPlaceWithGeomapItemIdentifier:]
+ -[RTLearnedLocationStore processExternalMapItem:handler:]
+ -[RTPOIHarvester _augmentedLocationsForAccessPoints:metrics:error:]
+ -[RTPOIHarvester _fingerprintAccessPointsForSettledState:withinInterval:metrics:error:]
+ -[RTPOIHarvester _fingerprintAccessPointsWithinInterval:harvestType:metrics:error:]
+ -[RTPOIHarvester _harvestPOI:mapItemSource:accessPointArrays:referenceLocations:harvestType:metrics:error:]
+ -[RTPOIHarvester _motionActivitiesWithinInterval:error:]
+ -[RTPOIHarvester _poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:]
+ -[RTPOIHarvester harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:]
+ -[RTPOIHarvesterMetrics fingerprintErrorCount]
+ -[RTPOIHarvesterMetrics harvestCreationCount]
+ -[RTPOIHarvesterMetrics harvestSubmissionCount]
+ -[RTPOIHarvesterMetrics harvestSubmissionErrorCount]
+ -[RTPOIHarvesterMetrics harvestType]
+ -[RTPOIHarvesterMetrics mapItemCopyErrorCount]
+ -[RTPOIHarvesterMetrics referenceLocationsCount]
+ -[RTPOIHarvesterMetrics setFingerprintErrorCount:]
+ -[RTPOIHarvesterMetrics setHarvestCreationCount:]
+ -[RTPOIHarvesterMetrics setHarvestSubmissionCount:]
+ -[RTPOIHarvesterMetrics setHarvestSubmissionErrorCount:]
+ -[RTPOIHarvesterMetrics setHarvestType:]
+ -[RTPOIHarvesterMetrics setMapItemCopyErrorCount:]
+ -[RTPOIHarvesterMetrics setReferenceLocationsCount:]
+ -[RTPOIHarvesterMetrics setSettledFingerprintCountWithTimeWindowFallback:]
+ -[RTPOIHarvesterMetrics setSettledFingerprintCountWithoutTimeWindowFallback:]
+ -[RTPOIHarvesterMetrics setTotalAccessPointCount:]
+ -[RTPOIHarvesterMetrics setTotalAccessPointErrorCount:]
+ -[RTPOIHarvesterMetrics setTotalEstimatedFingerprintLocationsCount:]
+ -[RTPOIHarvesterMetrics setTotalEstimatedFingerprintLocationsErrorCount:]
+ -[RTPOIHarvesterMetrics setTotalFetchedFingerprintLocationsCount:]
+ -[RTPOIHarvesterMetrics setTotalFetchedFingerprintLocationsErrorCount:]
+ -[RTPOIHarvesterMetrics setTotalMotionActivitiesCount:]
+ -[RTPOIHarvesterMetrics setTotalMotionActivitiesErrorCount:]
+ -[RTPOIHarvesterMetrics setUnsettledFingerprintCountWithTimeWindowFallback:]
+ -[RTPOIHarvesterMetrics setUnsettledFingerprintCountWithoutTimeWindowFallback:]
+ -[RTPOIHarvesterMetrics settledFingerprintCountWithTimeWindowFallback]
+ -[RTPOIHarvesterMetrics settledFingerprintCountWithoutTimeWindowFallback]
+ -[RTPOIHarvesterMetrics submit]
+ -[RTPOIHarvesterMetrics totalAccessPointCount]
+ -[RTPOIHarvesterMetrics totalAccessPointErrorCount]
+ -[RTPOIHarvesterMetrics totalEstimatedFingerprintLocationsCount]
+ -[RTPOIHarvesterMetrics totalEstimatedFingerprintLocationsErrorCount]
+ -[RTPOIHarvesterMetrics totalFetchedFingerprintLocationsCount]
+ -[RTPOIHarvesterMetrics totalFetchedFingerprintLocationsErrorCount]
+ -[RTPOIHarvesterMetrics totalMotionActivitiesCount]
+ -[RTPOIHarvesterMetrics totalMotionActivitiesErrorCount]
+ -[RTPOIHarvesterMetrics unsettledFingerprintCountWithTimeWindowFallback]
+ -[RTPOIHarvesterMetrics unsettledFingerprintCountWithoutTimeWindowFallback]
+ -[RTPredictedContextManager _handleTrainingDurationCapTimerWithStartTime:]
+ -[RTPredictedContextManager _invalidateTrainingDurationCapTimer]
+ -[RTPredictedContextManager _startTrainingDurationCapTimerWithStartTime:]
+ -[RTPredictedContextManager _trainingDurationCapInterval]
+ -[RTPredictedContextManager pendingInterruptSource]
+ -[RTPredictedContextManager setPendingInterruptSource:]
+ -[RTPredictedContextManager setTrainingDurationCapTimer:]
+ -[RTPredictedContextManager trainingDurationCapTimer]
+ -[RTSynthesizedLocationStore _storeLocationsByBatches:handler:]
+ -[RTSynthesizedLocationStore _storeLocationsForBatch:batchNo:batchSize:handler:]
+ -[RTTripClusterManager _fetchLearnedRoutesWithOptionsDefault:handler:]
+ -[RTTripClusterManager deferClusterProcessing:]
+ -[RTTripClusterManager generateMissingRoutesForClusters]
+ -[RTTripClusterManager setShouldDeferClusterProcessing:]
+ -[RTTripClusterManager shouldDeferClusterProcessing]
+ -[RTTripClusterProcessor deferClusterProcessing:]
+ -[RTTripClusterProcessor deleteWaypointsForClustersWithDuplicateWaypoints:tripClusterWaypointStore:tripClusterRouteStore:tripClusterRouteTransitionsStore:minimumTraversalCountForLearnedRoutes:]
+ -[RTTripClusterProcessor fillInRouteLocationsForClustersInStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRoadTransitionsStore:minimumTraversalCountForLearnedRoutes:]
+ -[RTTripClusterProcessor setShouldDeferClusterProcessing:]
+ -[RTTripClusterProcessor shouldDeferClusterProcessing]
+ -[RTTripClusterProcessor updateClusterRouteUsingWaypointsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:]
+ -[RTTripClusterProcessorOptions cleanUpClusterWithDuplicateWaypoints]
+ -[RTTripClusterProcessorOptions enableWalkBikeClustering]
+ -[RTTripClusterProcessorOptions maxCleanUpOperationsCountPerRun]
+ -[RTTripClusterProcessorOptions maxDeletionAttemptsForClusterData]
+ -[RTTripClusterProcessorOptions maxRouteRehydrationsCountPerRun]
+ -[RTTripClusterProcessorOptions rehydrateRouteLocationsFromWaypoints]
+ -[RTTripClusterProcessorOptions setCleanUpClusterWithDuplicateWaypoints:]
+ -[RTTripClusterProcessorOptions setEnableWalkBikeClustering:]
+ -[RTTripClusterProcessorOptions setMaxCleanUpOperationsCountPerRun:]
+ -[RTTripClusterProcessorOptions setMaxDeletionAttemptsForClusterData:]
+ -[RTTripClusterProcessorOptions setMaxRouteRehydrationsCountPerRun:]
+ -[RTTripClusterProcessorOptions setRehydrateRouteLocationsFromWaypoints:]
+ -[RTTripClusterRoadTransitionsDataStore _fetchCountForClusterID:handler:]
+ -[RTTripClusterRoadTransitionsDataStore deleteTripClusterRoadTransitionsWithClusterID:maxDeleteAttempts:]
+ -[RTTripClusterRoadTransitionsDataStore getTripClusterRoadTransitionsDataCountForClusterID:]
+ -[RTTripClusterRouteStore _fetchTripClusterRouteCountWithOptions:handler:]
+ -[RTTripClusterRouteStore deleteTripClusterRouteWithClusterID:maxDeleteAttempts:]
+ -[RTTripClusterRouteStore fetchTripClusterRouteCountWithClusterID:handler:]
+ -[RTTripClusterRouteStore getTripClusterRouteCountWithClusterID:]
+ -[RTTripClusterWaypointDataStore deleteTripClusterWaypointWithClusterID:maxDeleteAttempts:]
+ -[RTTripClusterWaypointDataStore initWithPersistenceManager:defaultsManager:]
+ -[RTTripClusterWaypointDataStore maxWaypointsPerChunk]
+ -[RTTripClusterWaypointDataStore rejectDuplicateWaypoints]
+ -[RTTripClusterWaypointDataStore setMaxWaypointsPerChunk:]
+ -[RTTripClusterWaypointDataStore setRejectDuplicateWaypoints:]
+ -[RTVehicleLocationProvider _updateLastVehicleEventAndNotify:]
+ -[SMSuggestionsManager initWithAuthorizationManager:contactsManager:defaultsManager:deviceLocationPredictor:distanceCalculator:healthKitManager:learnedLocationStore:learnedLocationManager:locationManager:mapServiceManager:messagingService:motionActivityManager:navigationManager:platform:visitManager:visitConsolidator:sessionStore:suggestionsStore:suggestionsHelper:appDeletionManager:trialManager:]
+ -[SMSuggestionsManager trialManager]
+ -[SMSuggestionsMetricsManager sendSuggestionsConversionEventForSuggestion:selected:sessionStarted:]
+ GCC_except_table113
+ GCC_except_table122
+ GCC_except_table136
+ GCC_except_table169
+ GCC_except_table170
+ GCC_except_table187
+ GCC_except_table211
+ GCC_except_table215
+ GCC_except_table226
+ GCC_except_table239
+ GCC_except_table251
+ GCC_except_table256
+ GCC_except_table260
+ GCC_except_table279
+ GCC_except_table288
+ GCC_except_table290
+ GCC_except_table294
+ GCC_except_table301
+ GCC_except_table303
+ GCC_except_table59
+ GCC_except_table90
+ _OBJC_CLASS_$_RTPOIHarvesterMetrics
+ _OBJC_CLASS_$_SMTrialManager
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._fingerprintErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestCreationCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestSubmissionCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestSubmissionErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._harvestType
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._mapItemCopyErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._referenceLocationsCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._settledFingerprintCountWithTimeWindowFallback
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._settledFingerprintCountWithoutTimeWindowFallback
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalAccessPointCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalAccessPointErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalEstimatedFingerprintLocationsCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalEstimatedFingerprintLocationsErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalFetchedFingerprintLocationsCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalFetchedFingerprintLocationsErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalMotionActivitiesCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._totalMotionActivitiesErrorCount
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._unsettledFingerprintCountWithTimeWindowFallback
+ _OBJC_IVAR_$_RTPOIHarvesterMetrics._unsettledFingerprintCountWithoutTimeWindowFallback
+ _OBJC_IVAR_$_RTTripClusterManager._shouldDeferClusterProcessing
+ _OBJC_IVAR_$_RTTripClusterProcessor._shouldDeferClusterProcessing
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._cleanUpClusterWithDuplicateWaypoints
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._enableWalkBikeClustering
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._maxCleanUpOperationsCountPerRun
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._maxDeletionAttemptsForClusterData
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._maxRouteRehydrationsCountPerRun
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._rehydrateRouteLocationsFromWaypoints
+ _OBJC_METACLASS_$_RTPOIHarvesterMetrics
+ _RTAnalyticsEventBluePOIHarvest
+ _SMInitiatorEligibilityStatusKey
+ _SMReceiverEligibilityStatusKey
+ _SMSuggestionConversionAnalyticsEvent
+ _SMSuggestionConversionPresentedKey
+ _SMSuggestionConversionSelectedKey
+ _SMSuggestionConversionStartedKey
+ _SMSuggestionConversionSupppressionReasonKey
+ _SMSuggestionConversionTriggerKey
+ _SMSuggestionConversionUserTypeKey
+ _SMTrialFactorSuggestionFirstTimeUserSuppressionEndTime
+ _SMTrialFactorSuggestionFirstTimeUserSuppressionStartTime
+ __OBJC_$_CLASS_METHODS_RTMapItemManager
+ __OBJC_$_INSTANCE_METHODS_RTPOIHarvesterMetrics
+ __OBJC_$_INSTANCE_VARIABLES_RTPOIHarvesterMetrics
+ __OBJC_$_INSTANCE_VARIABLES_RTTripClusterWaypointDataStore
+ __OBJC_$_PROP_LIST_RTPOIHarvesterMetrics
+ __OBJC_CLASS_RO_$_RTPOIHarvesterMetrics
+ __OBJC_METACLASS_RO_$_RTPOIHarvesterMetrics
+ ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke.91
+ ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.412
+ ___105-[RTPOIHarvester harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:]_block_invoke
+ ___119-[RTTripClusterManager purgeClustersDatabaseWithTripClusterStore:tripClusterRouteStore:tripClusterRoadTransitionStore:]_block_invoke.458
+ ___119-[RTTripClusterManager purgeClustersDatabaseWithTripClusterStore:tripClusterRouteStore:tripClusterRoadTransitionStore:]_block_invoke.459
+ ___121+[RTPOIHarvestUtilities fingerprintsBetweenStartDate:endDate:isTimeWindowFallback:settledState:fingerprintManager:error:]_block_invoke.6
+ ___124-[RTPersistenceMigrator __executeImportStepWithSourceStore:sourceCoordinator:destinationStore:destinationCoordinator:model:]_block_invoke
+ ___124-[RTPersistenceMigrator __executeImportStepWithSourceStore:sourceCoordinator:destinationStore:destinationCoordinator:model:]_block_invoke_2
+ ___128-[RTPlaceInferenceManager _savePlaceInferenceQueriesFromInferredMapItems:inferenceErrorCode:referenceLocation:options:outError:]_block_invoke.234
+ ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke.93
+ ___132+[RTUserCurationMetrics collectMetricsForAppliedLabel:curatedVisit:learnedLocationStore:distanceCalculator:applicationResult:error:]_block_invoke
+ ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.55
+ ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.75
+ ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.77
+ ___136-[RTTripClusterProcessor updateClusterRouteUsingWaypointsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:]_block_invoke
+ ___136-[RTTripClusterProcessor updateClusterRouteUsingWaypointsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:]_block_invoke.268
+ ___136-[RTTripClusterProcessor updateClusterRouteUsingWaypointsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:]_block_invoke.270
+ ___148-[RTPlaceInferenceManager sendPlaceInferenceMetrics:inferredMapItems:fusedMapItems:fallbackInferredMapItems:finalPlaceInferences:referenceLocation:]_block_invoke.261
+ ___229-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:]_block_invoke.293
+ ___229-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:]_block_invoke.294
+ ___27-[RTLifeCycleManager _exit]_block_invoke.724
+ ___27-[RTLifeCycleManager _exit]_block_invoke.730
+ ___27-[RTLifeCycleManager _exit]_block_invoke.732
+ ___27-[RTLifeCycleManager _exit]_block_invoke.733
+ ___27-[RTLifeCycleManager _exit]_block_invoke_2.731
+ ___28-[RTLifeCycleManager _start]_block_invoke.709
+ ___28-[RTLifeCycleManager _start]_block_invoke.715
+ ___28-[RTLifeCycleManager _start]_block_invoke.718
+ ___28-[RTLifeCycleManager _start]_block_invoke.721
+ ___31-[RTPOIHarvesterMetrics submit]_block_invoke
+ ___31-[RTPOIHarvesterMetrics submit]_block_invoke.184
+ ___35-[RTDataSerializer purgeWithError:]_block_invoke
+ ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.195
+ ___41-[RTVisitManager _simulateVisit:handler:]_block_invoke.175
+ ___43-[RTPredictedContextManager _storeRequest:]_block_invoke.505
+ ___44-[RTPersistenceMigrator _executePrepareStep]_block_invoke
+ ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.198
+ ___47-[SMClientListener _setupConnection:forClient:]_block_invoke.286
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.159
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.161
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.163
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.165
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.167
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.160
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.162
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.164
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.166
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.179
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.188
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.191
+ ___51-[RTLearnedLocationEngine _getDailyTrainingMetrics]_block_invoke.809
+ ___51-[RTLearnedLocationEngine _teardownTrainingMetrics]_block_invoke.865
+ ___51-[SMInitiatorCacheManager _setupFetchOnZoneUpdates]_block_invoke.257
+ ___51-[SMInitiatorCacheManager _uploadCache:completion:]_block_invoke.381
+ ___52-[RTLearnedLocationEngine _createLOIForPlace:error:]_block_invoke.891
+ ___52-[RTPlaceInferenceManager _onSyncedPlaceInferences:]_block_invoke_2
+ ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.498
+ ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.501
+ ___53-[RTVisitMonitor fetchVisitsFromDate:toDate:handler:]_block_invoke.135
+ ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.455
+ ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.456
+ ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.457
+ ___54-[SMDaemonClient connection:handleInvocation:isReply:]_block_invoke.37
+ ___54-[SMInitiatorService _onHealthKitManagerNotification:]_block_invoke.215
+ ___54-[SMInitiatorService _onHealthKitManagerNotification:]_block_invoke.217
+ ___55-[RTLearnedLocationEngine _retrainVisitsWithoutPlaces:]_block_invoke.867
+ ___55-[RTLearnedLocationEngine trainForReason:mode:handler:]_block_invoke.649
+ ___55-[RTVisitManager fetchStoredVisitsWithOptions:handler:]_block_invoke_2.128
+ ___55-[SMInitiatorCacheManager _schedulePeriodicCacheUpdate]_block_invoke.347
+ ___55-[SMInitiatorCacheManager _schedulePeriodicCacheUpdate]_block_invoke.348
+ ___56-[RTPOIHarvester _motionActivitiesWithinInterval:error:]_block_invoke
+ ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.765
+ ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.766
+ ___57-[RTLearnedLocationStore processExternalMapItem:handler:]_block_invoke
+ ___57-[RTLearnedLocationStore processExternalMapItem:handler:]_block_invoke.618
+ ___57-[RTLearnedLocationStore processExternalMapItem:handler:]_block_invoke_2
+ ___57-[RTVisitManager _registerXpcActivityFindPointOfInterest]_block_invoke.139
+ ___57-[RTVisitManager _registerXpcActivityFindPointOfInterest]_block_invoke_2.140
+ ___57-[SMInitiatorCacheManager _setupShareZoneWithCompletion:]_block_invoke.262
+ ___57-[SMInitiatorCacheManager _storeInitiatorContactInStore:]_block_invoke.418
+ ___57-[SMInitiatorCacheManager updateCacheUpdateBackstopTimer]_block_invoke.416
+ ___57-[SMInitiatorCacheManager updateCacheUpdateBackstopTimer]_block_invoke.417
+ ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.136
+ ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.138
+ ___58-[RTPredictedContextManager _evaluateTrainErrorForResult:]_block_invoke.173
+ ___58-[SMInitiatorCacheManager _updateCacheDataWithCompletion:]_block_invoke.357
+ ___58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.317
+ ___58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.318
+ ___58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.321
+ ___58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.323
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.492
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.499
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.503
+ ___59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.187
+ ___59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.197
+ ___59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.212
+ ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.584
+ ___60-[RTPlaceInferenceManager _placeInferencesForOptions:error:]_block_invoke.231
+ ___60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.368
+ ___60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.369
+ ___60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.372
+ ___60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.373
+ ___61-[RTVehicleLocationProvider _onExternalVehicleEventReceived:]_block_invoke
+ ___61-[RTVehicleLocationProvider _onExternalVehicleEventReceived:]_block_invoke_2
+ ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke.159
+ ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke_2.160
+ ___61-[SMInitiatorCacheManager _cleanUpInitiatorContactLocalStore]_block_invoke.419
+ ___61-[SMInitiatorCacheManager _cleanUpInitiatorContactLocalStore]_block_invoke.420
+ ___61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.401
+ ___61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.402
+ ___61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.403
+ ___61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.404
+ ___62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.350
+ ___62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.351
+ ___62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.352
+ ___62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.354
+ ___62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.355
+ ___63-[RTTripClusterManager _fetchLearnedRoutesWithOptions:handler:]_block_invoke.430
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.308
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.310
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.313
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.316
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.319
+ ___65-[RTTripClusterRouteStore getTripClusterRouteCountWithClusterID:]_block_invoke
+ ___65-[SMDaemonClient startMonitoringInitiatorSafetyCacheWithHandler:]_block_invoke.46
+ ___65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.298
+ ___65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.299
+ ___65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.301
+ ___65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.228
+ ___66-[SMSafetyCacheZone createRecordsWithParticipants:qos:completion:]_block_invoke.54
+ ___67-[RTPOIHarvester _augmentedLocationsForAccessPoints:metrics:error:]_block_invoke
+ ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.117
+ ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.121
+ ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.127
+ ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke_2.122
+ ___67-[SMInitiatorCacheManager _requestSmoothedLocationsWithCompletion:]_block_invoke.363
+ ___68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.604
+ ___68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.607
+ ___68-[SMSafetyCacheZone updateSafetyCacheRecordWithData:qos:completion:]_block_invoke.63
+ ___69-[RTPredictedContextManager _rescheduleActivityTrainWithTrainPolicy:]_block_invoke.174
+ ___69-[RTTripClusterRouteStore _fetchTripClusterRouteWithContext:handler:]_block_invoke.48
+ ___69-[SMInitiatorCacheManager _cancelScheduledKeyReleaseForConversation:]_block_invoke.405
+ ___70-[RTLearnedLocationEngine _saveIdentifiersOfKnownPlaceTypesWithError:]_block_invoke.786
+ ___70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke.596
+ ___70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke_2.597
+ ___70-[RTTripClusterManager _fetchLearnedRoutesWithOptionsDefault:handler:]_block_invoke
+ ___70-[SMSafetyCacheZone setupZoneAndShareWithConversation:qos:completion:]_block_invoke.36
+ ___70-[SMSafetyCacheZone setupZoneAndShareWithConversation:qos:completion:]_block_invoke.40
+ ___71-[RTLearnedLocationEngine _updateLearnedPlaceWithGeomapItemIdentifier:]_block_invoke
+ ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke.852
+ ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke_2.853
+ ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.515
+ ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.557
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.466
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.470
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.481
+ ___73-[RTPredictedContextManager _startTrainingDurationCapTimerWithStartTime:]_block_invoke
+ ___73-[RTTripClusterRoadTransitionsDataStore _fetchCountForClusterID:handler:]_block_invoke
+ ___73-[RTTripClusterRoadTransitionsDataStore _fetchCountForClusterID:handler:]_block_invoke_2
+ ___74-[RTLearnedLocationEngine _relabelWithRelabeler:relabelerPersister:error:]_block_invoke.747
+ ___74-[RTPredictedContextManager _handleTrainingDurationCapTimerWithStartTime:]_block_invoke
+ ___74-[RTTripClusterRouteStore _fetchTripClusterRouteCountWithOptions:handler:]_block_invoke
+ ___74-[RTTripClusterRouteStore _fetchTripClusterRouteCountWithOptions:handler:]_block_invoke.49
+ ___74-[RTTripClusterRouteStore _fetchTripClusterRouteCountWithOptions:handler:]_block_invoke.50
+ ___74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.327
+ ___74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.328
+ ___74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.330
+ ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.800
+ ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.801
+ ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.804
+ ___75-[RTLearnedLocationEngine requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.681
+ ___75-[RTTripClusterRouteStore fetchTripClusterRouteCountWithClusterID:handler:]_block_invoke
+ ___76-[RTLearnedLocationEngine _appendVisitsToLocationsOfInterestModelWithError:]_block_invoke.869
+ ___76-[RTLearnedLocationEngine _requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.682
+ ___77+[RTLearnedLocationReconcilerPerDevice sortReconciledVisitsByMapItemQuality:]_block_invoke_3.81
+ ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.611
+ ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke.220
+ ___78-[RTTripClusterWaypointDataStore getTripClusterWaypointDataCountForClusterID:]_block_invoke_2
+ ___79-[RTTripClusterWaypointDataStore _fetchTripClusterWaypointWithContext:handler:]_block_invoke.65
+ ___79-[RTTripClusterWaypointDataStore _fetchTripClusterWaypointWithContext:handler:]_block_invoke.70
+ ___79-[RTTripClusterWaypointDataStore _fetchTripClusterWaypointWithContext:handler:]_block_invoke.71
+ ___79-[SMSafetyCacheZone updateAccessDataRecordWithCacheReleaseTime:qos:completion:]_block_invoke.65
+ ___80-[RTSynthesizedLocationStore _storeLocationsForBatch:batchNo:batchSize:handler:]_block_invoke
+ ___80-[RTSynthesizedLocationStore _storeLocationsForBatch:batchNo:batchSize:handler:]_block_invoke_2
+ ___81-[RTLearnedLocationEngine _isUpdateLearnedPlaceWithGeomapItemIdentifierRequired:]_block_invoke
+ ___81-[RTMapItemManager mapItemsFromLocalBluePOIResult:withConfidenceThreshold:error:]_block_invoke.18
+ ___81-[RTMapItemManager mapItemsFromLocalBluePOIResult:withConfidenceThreshold:error:]_block_invoke.19
+ ___82-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]_block_invoke.901
+ ___82-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]_block_invoke.902
+ ___83-[RTLearnedLocationEngine _recoverKnownPlaceTypesWithPlaceTypeClassifier:outError:]_block_invoke.808
+ ___84-[SMSuggestionsMetricsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.153
+ ___85-[RTTripClusterManager _findRouteFromCurrentLocation:options:queryStartTime:handler:]_block_invoke.355
+ ___85-[SMSuggestionsMetricsManager _getSuggestionsCountSelectedForPastDate:endDate:error:]_block_invoke.136
+ ___90+[RTPOIHarvestUtilities locationsForAccessPoints:harvestParameters:locationManager:error:]_block_invoke
+ ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.118
+ ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.127
+ ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.131
+ ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.138
+ ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.143
+ ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.147
+ ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke_2.128
+ ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke_2.132
+ ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke_2.139
+ ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke_2.144
+ ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke_2.148
+ ___92-[RTPOIHarvester _poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:]_block_invoke
+ ___92-[RTTripClusterRoadTransitionsDataStore getTripClusterRoadTransitionsDataCountForClusterID:]_block_invoke
+ ___93-[RTTripClusterRoadTransitionsDataStore _fetchTripClusterRoadTransitionsWithContext:handler:]_block_invoke.86
+ ___98-[RTLearnedLocationEngine _fetchCloudCurrentDeviceVisitsBetweenStartDate:endDate:ascending:error:]_block_invoke.571
+ ___98-[RTLearnedLocationEngine _fetchCloudCurrentDeviceVisitsBetweenStartDate:endDate:ascending:error:]_block_invoke.573
+ ___block_descriptor_104_e8_32s40s48s56s64bs72r80r88r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8r80l8r88l8s64l8
+ ___block_descriptor_32_e35_q24?0"RTLocation"8"RTLocation"16l
+ ___block_descriptor_32_e49_q24?0"RTWiFiAccessPoint"8"RTWiFiAccessPoint"16l
+ ___block_descriptor_32_e57_q24?0"RTTripClusterWaypoint"8"RTTripClusterWaypoint"16l
+ ___block_descriptor_56_e8_32s40r_e24_v32?0"NSError"8Q16^B24lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e33_v16?0"CLTripSegmentOutputData"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40w_e19_"NSDictionary"8?0lw40l8s32l8
+ ___block_descriptor_64_e8_32bs40r48r_e5_v8?0lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e20_v20?0B8"NSError"12ls32l8r48l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e31_v24?0"RTMapItem"8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_72_e8_32s40bs48r56r_e20_v20?0B8"NSError"12ls32l8r48l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r_e31_v24?0"RTMapItem"8"NSError"16lr48l8r56l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e33_v32?0"NSArray"8^B16"NSError"24ls32l8s40l8s56l8r64l8s48l8
+ ___block_descriptor_73_e8_32s40s48bs56r64r_e20_v20?0B8"NSError"12ls32l8r56l8r64l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e31_v24?0"RTMapItem"8"NSError"16lr64l8r72l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r_e31_v24?0"RTMapItem"8"NSError"16lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r_e5_v8?0ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_97_e8_32s40s48s56bs64r72r80r_e5_v8?0ls32l8s40l8r64l8r72l8r80l8s48l8s56l8
+ ___block_literal_global.1375
+ ___block_literal_global.140
+ ___block_literal_global.181
+ ___block_literal_global.183
+ ___block_literal_global.193
+ ___block_literal_global.212
+ ___block_literal_global.239
+ ___block_literal_global.241
+ ___block_literal_global.243
+ ___block_literal_global.273
+ ___block_literal_global.295
+ ___block_literal_global.325
+ ___block_literal_global.378
+ ___block_literal_global.381
+ ___block_literal_global.392
+ ___block_literal_global.412
+ ___block_literal_global.42
+ ___block_literal_global.430
+ ___block_literal_global.441
+ ___block_literal_global.569
+ ___block_literal_global.59
+ ___block_literal_global.603
+ ___block_literal_global.616
+ ___block_literal_global.712
+ ___block_literal_global.717
+ ___block_literal_global.720
+ ___block_literal_global.723
+ ___block_literal_global.735
+ ___block_literal_global.905
+ ___block_literal_global.932
+ ___block_literal_global.968
+ ___block_literal_global.979
+ ___handleShareAllLocationsChanged_block_invoke.983
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_libcoreroutine
+ _kRTBluePOIQueryEventAppIdentifier
+ _kRTBluePOIQueryEventAppIdentifierInternal
+ _kRTBluePOIQueryEventAppIdentifierUnknown
+ _objc_msgSend$_augmentedLocationsForAccessPoints:metrics:error:
+ _objc_msgSend$_fetchLearnedRoutesWithOptionsDefault:handler:
+ _objc_msgSend$_fetchTripClusterRouteCountWithOptions:handler:
+ _objc_msgSend$_fingerprintAccessPointsForSettledState:withinInterval:metrics:error:
+ _objc_msgSend$_fingerprintAccessPointsWithinInterval:harvestType:metrics:error:
+ _objc_msgSend$_handleTrainingDurationCapTimerWithStartTime:
+ _objc_msgSend$_harvestPOI:mapItemSource:accessPointArrays:referenceLocations:harvestType:metrics:error:
+ _objc_msgSend$_invalidateTrainingDurationCapTimer
+ _objc_msgSend$_isUpdateLearnedPlaceWithGeomapItemIdentifierRequired:
+ _objc_msgSend$_motionActivitiesWithinInterval:error:
+ _objc_msgSend$_poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:
+ _objc_msgSend$_shouldFilterError:
+ _objc_msgSend$_startTrainingDurationCapTimerWithStartTime:
+ _objc_msgSend$_storeLocationsByBatches:handler:
+ _objc_msgSend$_storeLocationsForBatch:batchNo:batchSize:handler:
+ _objc_msgSend$_submitMetricsForApplicationOfCuratedLabel:visit:result:
+ _objc_msgSend$_trainingDurationCapInterval
+ _objc_msgSend$_updateLastVehicleEventAndNotify:
+ _objc_msgSend$_updateLearnedPlaceWithGeomapItemIdentifier:
+ _objc_msgSend$accessPointsCount
+ _objc_msgSend$collectMetricsForAppliedLabel:curatedVisit:learnedLocationStore:distanceCalculator:applicationResult:error:
+ _objc_msgSend$constructRouteFromWaypoints:forRouteID:withOptions:outputHandler:completionHandler:
+ _objc_msgSend$deferClusterProcessing:
+ _objc_msgSend$deleteTripClusterRoadTransitionsWithClusterID:maxDeleteAttempts:
+ _objc_msgSend$deleteTripClusterRouteWithClusterID:maxDeleteAttempts:
+ _objc_msgSend$deleteTripClusterWaypointWithClusterID:maxDeleteAttempts:
+ _objc_msgSend$deleteWaypointsForClustersWithDuplicateWaypoints:tripClusterWaypointStore:tripClusterRouteStore:tripClusterRouteTransitionsStore:minimumTraversalCountForLearnedRoutes:
+ _objc_msgSend$divideArray:intoChunks:
+ _objc_msgSend$doubleValueForFactor:
+ _objc_msgSend$enableWalkBikeClustering
+ _objc_msgSend$fetchTripClusterRouteCountWithClusterID:handler:
+ _objc_msgSend$fillInRouteLocationsForClustersInStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRoadTransitionsStore:minimumTraversalCountForLearnedRoutes:
+ _objc_msgSend$fingerprintErrorCount
+ _objc_msgSend$firstResultOnly
+ _objc_msgSend$generateMissingRoutesForClusters
+ _objc_msgSend$geoMapItemIdentifier
+ _objc_msgSend$getTripClusterRoadTransitionsDataCountForClusterID:
+ _objc_msgSend$getTripClusterRouteCountWithClusterID:
+ _objc_msgSend$getWaypointDataFromWaypoints:maxWaypointsPerChunk:
+ _objc_msgSend$harvestCreationCount
+ _objc_msgSend$harvestCuration:mapItem:visitLocations:poiHarvester:error:
+ _objc_msgSend$harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:
+ _objc_msgSend$harvestSubmissionCount
+ _objc_msgSend$harvestSubmissionErrorCount
+ _objc_msgSend$harvestType
+ _objc_msgSend$initWithAscending:sortIndex:submissionDateInterval:visitDateInterval:limit:
+ _objc_msgSend$initWithAuthorizationManager:contactsManager:defaultsManager:deviceLocationPredictor:distanceCalculator:healthKitManager:learnedLocationStore:learnedLocationManager:locationManager:mapServiceManager:messagingService:motionActivityManager:navigationManager:platform:visitManager:visitConsolidator:sessionStore:suggestionsStore:suggestionsHelper:appDeletionManager:trialManager:
+ _objc_msgSend$initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:
+ _objc_msgSend$initWithMapItem:accessPoints:locations:motionActivities:triggerType:
+ _objc_msgSend$initWithMapItem:triggerType:date:
+ _objc_msgSend$isBluePOITileNotAvailableError
+ _objc_msgSend$locationsCount
+ _objc_msgSend$mapItemCopyErrorCount
+ _objc_msgSend$maxCleanUpOperationsCountPerRun
+ _objc_msgSend$maxDeletionAttemptsForClusterData
+ _objc_msgSend$maxRouteRehydrationsCountPerRun
+ _objc_msgSend$modelBinPath
+ _objc_msgSend$pendingInterruptSource
+ _objc_msgSend$processExternalMapItem:handler:
+ _objc_msgSend$purgeWithError:
+ _objc_msgSend$referenceLocationsCount
+ _objc_msgSend$refresh
+ _objc_msgSend$refreshAllObjects
+ _objc_msgSend$rehydrateRouteLocationsFromWaypoints
+ _objc_msgSend$sendSuggestionsConversionEventForSuggestion:selected:sessionStarted:
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setFingerprintErrorCount:
+ _objc_msgSend$setGeoMapItemIdentifier:
+ _objc_msgSend$setHarvestCreationCount:
+ _objc_msgSend$setHarvestSubmissionCount:
+ _objc_msgSend$setHarvestSubmissionErrorCount:
+ _objc_msgSend$setHarvestType:
+ _objc_msgSend$setMapItemCopyErrorCount:
+ _objc_msgSend$setPendingInterruptSource:
+ _objc_msgSend$setReferenceLocationsCount:
+ _objc_msgSend$setSettledFingerprintCountWithTimeWindowFallback:
+ _objc_msgSend$setSettledFingerprintCountWithoutTimeWindowFallback:
+ _objc_msgSend$setShouldDeferClusterProcessing:
+ _objc_msgSend$setTotalAccessPointCount:
+ _objc_msgSend$setTotalAccessPointErrorCount:
+ _objc_msgSend$setTotalEstimatedFingerprintLocationsCount:
+ _objc_msgSend$setTotalEstimatedFingerprintLocationsErrorCount:
+ _objc_msgSend$setTotalFetchedFingerprintLocationsCount:
+ _objc_msgSend$setTotalFetchedFingerprintLocationsErrorCount:
+ _objc_msgSend$setTotalMotionActivitiesCount:
+ _objc_msgSend$setTotalMotionActivitiesErrorCount:
+ _objc_msgSend$setTrainingDurationCapTimer:
+ _objc_msgSend$setUnsettledFingerprintCountWithTimeWindowFallback:
+ _objc_msgSend$setUnsettledFingerprintCountWithoutTimeWindowFallback:
+ _objc_msgSend$settledFingerprintCountWithTimeWindowFallback
+ _objc_msgSend$settledFingerprintCountWithoutTimeWindowFallback
+ _objc_msgSend$shouldDeferClusterProcessing
+ _objc_msgSend$suggestionsMetricsManager
+ _objc_msgSend$totalAccessPointCount
+ _objc_msgSend$totalAccessPointErrorCount
+ _objc_msgSend$totalEstimatedFingerprintLocationsCount
+ _objc_msgSend$totalEstimatedFingerprintLocationsErrorCount
+ _objc_msgSend$totalFetchedFingerprintLocationsCount
+ _objc_msgSend$totalFetchedFingerprintLocationsErrorCount
+ _objc_msgSend$totalMotionActivitiesCount
+ _objc_msgSend$totalMotionActivitiesErrorCount
+ _objc_msgSend$trainingDurationCapTimer
+ _objc_msgSend$trialManager
+ _objc_msgSend$unsettledFingerprintCountWithTimeWindowFallback
+ _objc_msgSend$unsettledFingerprintCountWithoutTimeWindowFallback
+ _objc_msgSend$updateClusterRouteUsingWaypointsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:
- +[RTPOIHarvestUtilities harvestCuration:mapItem:referenceLocations:poiHarvester:error:]
- +[RTTripClusterWaypoint getWaypointDataFromWaypoints:]
- +[RTUserCurationMetrics collectMetricsForAppliedUserCuration:curatedVisit:learnedLocationStore:distanceCalculator:error:]
- -[CLPPoiHarvest(RTExtensions) initWithMapItem:accessPoints:locations:motionActivities:]
- -[CLPPoiTriggerEvent(RTExtensions) initWithMapItem:date:]
- -[RTLearnedLocationEngine _harvestFeedbackData]
- -[RTMapItemManager createMapItemFromMapItem:]
- -[RTMapsSupportManager _fetchReviewedPlacesWithOptions:handler:]
- -[RTMapsSupportManager _fetchReviewedPlacesWrapperWithOptions:handler:]
- -[RTMapsSupportManager fetchReviewedPlacesWithOptions:handler:]
- -[RTPOIHarvester _motionActivitiesFrom:to:error:]
- -[RTPOIHarvester _poiHarvestForFingerprint:mapItem:referenceLocations:endDate:error:]
- -[RTPOIHarvester harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:]
- -[RTReviewedPlace .cxx_destruct]
- -[RTReviewedPlace description]
- -[RTReviewedPlace hasUserReviewed]
- -[RTReviewedPlace initWithMuid:lastSuggestedReviewDate:hasUserReviewed:modifiedDate:]
- -[RTReviewedPlace init]
- -[RTReviewedPlace lastSuggestedReviewDate]
- -[RTReviewedPlace modifiedDate]
- -[RTReviewedPlace muid]
- -[RTTripClusterWaypointDataStore initWithPersistenceManager:]
- -[SMSuggestionsManager initWithAuthorizationManager:contactsManager:defaultsManager:deviceLocationPredictor:distanceCalculator:healthKitManager:learnedLocationStore:learnedLocationManager:locationManager:mapServiceManager:messagingService:motionActivityManager:navigationManager:platform:visitManager:visitConsolidator:sessionStore:suggestionsStore:suggestionsHelper:appDeletionManager:]
- GCC_except_table109
- GCC_except_table139
- GCC_except_table149
- GCC_except_table168
- GCC_except_table209
- GCC_except_table212
- GCC_except_table224
- GCC_except_table235
- GCC_except_table249
- GCC_except_table252
- GCC_except_table258
- GCC_except_table280
- GCC_except_table285
- GCC_except_table287
- GCC_except_table291
- GCC_except_table295
- GCC_except_table300
- _OBJC_CLASS_$_MSReviewedPlaceRequest
- _OBJC_CLASS_$_RTReviewedPlace
- _OBJC_IVAR_$_RTReviewedPlace._hasUserReviewed
- _OBJC_IVAR_$_RTReviewedPlace._lastSuggestedReviewDate
- _OBJC_IVAR_$_RTReviewedPlace._modifiedDate
- _OBJC_IVAR_$_RTReviewedPlace._muid
- _OBJC_METACLASS_$_RTReviewedPlace
- __OBJC_$_INSTANCE_METHODS_RTReviewedPlace
- __OBJC_$_INSTANCE_VARIABLES_RTReviewedPlace
- __OBJC_$_PROP_LIST_RTReviewedPlace
- __OBJC_CLASS_RO_$_RTReviewedPlace
- __OBJC_METACLASS_RO_$_RTReviewedPlace
- ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke.88
- ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.409
- ___119-[RTTripClusterManager purgeClustersDatabaseWithTripClusterStore:tripClusterRouteStore:tripClusterRoadTransitionStore:]_block_invoke.455
- ___119-[RTTripClusterManager purgeClustersDatabaseWithTripClusterStore:tripClusterRouteStore:tripClusterRoadTransitionStore:]_block_invoke.456
- ___121+[RTPOIHarvestUtilities fingerprintsBetweenStartDate:endDate:isTimeWindowFallback:settledState:fingerprintManager:error:]_block_invoke.5
- ___121+[RTUserCurationMetrics collectMetricsForAppliedUserCuration:curatedVisit:learnedLocationStore:distanceCalculator:error:]_block_invoke
- ___128-[RTPlaceInferenceManager _savePlaceInferenceQueriesFromInferredMapItems:inferenceErrorCode:referenceLocation:options:outError:]_block_invoke.241
- ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke.90
- ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.52
- ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.72
- ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.74
- ___148-[RTPlaceInferenceManager sendPlaceInferenceMetrics:inferredMapItems:fusedMapItems:fallbackInferredMapItems:finalPlaceInferences:referenceLocation:]_block_invoke.268
- ___229-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:]_block_invoke.287
- ___229-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:]_block_invoke.288
- ___27-[RTLifeCycleManager _exit]_block_invoke.720
- ___27-[RTLifeCycleManager _exit]_block_invoke.726
- ___27-[RTLifeCycleManager _exit]_block_invoke.728
- ___27-[RTLifeCycleManager _exit]_block_invoke.729
- ___27-[RTLifeCycleManager _exit]_block_invoke_2.727
- ___28-[RTLifeCycleManager _start]_block_invoke.705
- ___28-[RTLifeCycleManager _start]_block_invoke.711
- ___28-[RTLifeCycleManager _start]_block_invoke.714
- ___28-[RTLifeCycleManager _start]_block_invoke.717
- ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.192
- ___41-[RTVisitManager _simulateVisit:handler:]_block_invoke.176
- ___43-[RTPredictedContextManager _storeRequest:]_block_invoke.493
- ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.195
- ___47-[RTLearnedLocationEngine _harvestFeedbackData]_block_invoke
- ___47-[RTLearnedLocationEngine _harvestFeedbackData]_block_invoke.575
- ___47-[SMClientListener _setupConnection:forClient:]_block_invoke.283
- ___49-[RTPOIHarvester _motionActivitiesFrom:to:error:]_block_invoke
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.156
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.158
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.160
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.162
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.164
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.157
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.159
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.161
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.163
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.176
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.185
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.188
- ___51-[RTLearnedLocationEngine _getDailyTrainingMetrics]_block_invoke.814
- ___51-[RTLearnedLocationEngine _teardownTrainingMetrics]_block_invoke.870
- ___51-[SMInitiatorCacheManager _setupFetchOnZoneUpdates]_block_invoke.236
- ___51-[SMInitiatorCacheManager _uploadCache:completion:]_block_invoke.361
- ___52-[RTLearnedLocationEngine _createLOIForPlace:error:]_block_invoke.896
- ___52-[RTPlaceInferenceManager _onSyncedPlaceInferences:]_block_invoke.217
- ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.486
- ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.489
- ___53-[RTVisitMonitor fetchVisitsFromDate:toDate:handler:]_block_invoke.132
- ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.445
- ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.446
- ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.447
- ___54-[SMDaemonClient connection:handleInvocation:isReply:]_block_invoke.34
- ___54-[SMInitiatorService _onHealthKitManagerNotification:]_block_invoke.211
- ___54-[SMInitiatorService _onHealthKitManagerNotification:]_block_invoke.212
- ___55-[RTLearnedLocationEngine _retrainVisitsWithoutPlaces:]_block_invoke.872
- ___55-[RTLearnedLocationEngine trainForReason:mode:handler:]_block_invoke.654
- ___55-[RTVisitManager fetchStoredVisitsWithOptions:handler:]_block_invoke_2.129
- ___55-[SMInitiatorCacheManager _schedulePeriodicCacheUpdate]_block_invoke.327
- ___55-[SMInitiatorCacheManager _schedulePeriodicCacheUpdate]_block_invoke.328
- ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.770
- ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.771
- ___57-[RTVisitManager _registerXpcActivityFindPointOfInterest]_block_invoke.140
- ___57-[RTVisitManager _registerXpcActivityFindPointOfInterest]_block_invoke_2.141
- ___57-[SMInitiatorCacheManager _setupShareZoneWithCompletion:]_block_invoke.241
- ___57-[SMInitiatorCacheManager _storeInitiatorContactInStore:]_block_invoke.398
- ___57-[SMInitiatorCacheManager updateCacheUpdateBackstopTimer]_block_invoke.396
- ___57-[SMInitiatorCacheManager updateCacheUpdateBackstopTimer]_block_invoke.397
- ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.133
- ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.135
- ___58-[RTPredictedContextManager _evaluateTrainErrorForResult:]_block_invoke.164
- ___58-[SMInitiatorCacheManager _updateCacheDataWithCompletion:]_block_invoke.337
- ___58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.296
- ___58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.297
- ___58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.300
- ___58-[SMInitiatorCacheManager processSessionStartInfoRequest:]_block_invoke.302
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.489
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.496
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.500
- ___59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.178
- ___59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.188
- ___59-[SMInitiatorCacheManager initializeSessionWithCompletion:]_block_invoke.203
- ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.581
- ___60-[RTPlaceInferenceManager _placeInferencesForOptions:error:]_block_invoke.238
- ___60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.348
- ___60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.349
- ___60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.352
- ___60-[SMInitiatorCacheManager _fetchDeviceStatusWithCompletion:]_block_invoke.353
- ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke.156
- ___61-[RTVisitMonitor _setupGeoFencesForVisit:pipelineType:error:]_block_invoke_2.157
- ___61-[SMInitiatorCacheManager _cleanUpInitiatorContactLocalStore]_block_invoke.399
- ___61-[SMInitiatorCacheManager _cleanUpInitiatorContactLocalStore]_block_invoke.400
- ___61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.381
- ___61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.382
- ___61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.383
- ___61-[SMInitiatorCacheManager _scheduleKeyReleaseWithCompletion:]_block_invoke.384
- ___62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.330
- ___62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.331
- ___62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.332
- ___62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.334
- ___62-[SMInitiatorCacheManager _periodicCacheUpdateWithCompletion:]_block_invoke.335
- ___63-[RTMapsSupportManager fetchReviewedPlacesWithOptions:handler:]_block_invoke
- ___63-[RTTripClusterManager _fetchLearnedRoutesWithOptions:handler:]_block_invoke.427
- ___64-[RTMapsSupportManager _fetchReviewedPlacesWithOptions:handler:]_block_invoke
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.292
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.295
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.296
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.298
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.301
- ___65-[SMDaemonClient startMonitoringInitiatorSafetyCacheWithHandler:]_block_invoke.43
- ___65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.277
- ___65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.278
- ___65-[SMInitiatorCacheManager onSessionStateChanged:forActiveDevice:]_block_invoke.280
- ___65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.225
- ___66-[SMSafetyCacheZone createRecordsWithParticipants:qos:completion:]_block_invoke.47
- ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.108
- ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.112
- ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.118
- ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke_2.113
- ___67-[SMInitiatorCacheManager _requestSmoothedLocationsWithCompletion:]_block_invoke.343
- ___68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.609
- ___68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.612
- ___68-[SMSafetyCacheZone updateSafetyCacheRecordWithData:qos:completion:]_block_invoke.56
- ___69-[RTPredictedContextManager _rescheduleActivityTrainWithTrainPolicy:]_block_invoke.165
- ___69-[RTTripClusterRouteStore _fetchTripClusterRouteWithContext:handler:]_block_invoke.46
- ___69-[SMInitiatorCacheManager _cancelScheduledKeyReleaseForConversation:]_block_invoke.385
- ___70-[RTLearnedLocationEngine _saveIdentifiersOfKnownPlaceTypesWithError:]_block_invoke.791
- ___70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke.601
- ___70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke_2.602
- ___70-[SMSafetyCacheZone setupZoneAndShareWithConversation:qos:completion:]_block_invoke.32
- ___70-[SMSafetyCacheZone setupZoneAndShareWithConversation:qos:completion:]_block_invoke.33
- ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke.857
- ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke_2.858
- ___71-[RTMapsSupportManager _fetchReviewedPlacesWrapperWithOptions:handler:]_block_invoke
- ___71-[RTMapsSupportManager _fetchReviewedPlacesWrapperWithOptions:handler:]_block_invoke_2
- ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.512
- ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.554
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.463
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.467
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.478
- ___74-[RTLearnedLocationEngine _relabelWithRelabeler:relabelerPersister:error:]_block_invoke.752
- ___74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.306
- ___74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.307
- ___74-[SMInitiatorCacheManager _sendKeyReleaseMessageForIsSecondarySOSTrigger:]_block_invoke.309
- ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.805
- ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.806
- ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.809
- ___75-[RTLearnedLocationEngine requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.686
- ___76-[RTLearnedLocationEngine _appendVisitsToLocationsOfInterestModelWithError:]_block_invoke.874
- ___76-[RTLearnedLocationEngine _requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.687
- ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.608
- ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke.214
- ___79-[RTTripClusterWaypointDataStore _fetchTripClusterWaypointWithContext:handler:]_block_invoke.59
- ___79-[RTTripClusterWaypointDataStore _fetchTripClusterWaypointWithContext:handler:]_block_invoke.60
- ___79-[SMSafetyCacheZone updateAccessDataRecordWithCacheReleaseTime:qos:completion:]_block_invoke.58
- ___81-[RTMapItemManager mapItemsFromLocalBluePOIResult:withConfidenceThreshold:error:]_block_invoke.16
- ___81-[RTMapItemManager mapItemsFromLocalBluePOIResult:withConfidenceThreshold:error:]_block_invoke.17
- ___82-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]_block_invoke.906
- ___82-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]_block_invoke.907
- ___83-[RTLearnedLocationEngine _recoverKnownPlaceTypesWithPlaceTypeClassifier:outError:]_block_invoke.813
- ___84-[SMSuggestionsManager _shouldShowKeyboardSuggestionsForInitiator:receiver:handler:]_block_invoke
- ___84-[SMSuggestionsMetricsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.150
- ___85-[RTTripClusterManager _findRouteFromCurrentLocation:options:queryStartTime:handler:]_block_invoke.352
- ___85-[SMSuggestionsMetricsManager _getSuggestionsCountSelectedForPastDate:endDate:error:]_block_invoke.133
- ___89-[SMSuggestionsManager _generatePersonalizedSuggestionForFirstTimeUserFromContext:error:]_block_invoke
- ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.116
- ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.125
- ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.129
- ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.136
- ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.139
- ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke.145
- ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke_2.126
- ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke_2.130
- ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke_2.137
- ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke_2.140
- ___91-[SMSuggestionsHelper _fetchMostLikelySessionDestinationsWithRefreshedLocationWithHandler:]_block_invoke_2.146
- ___93-[RTTripClusterRoadTransitionsDataStore _fetchTripClusterRoadTransitionsWithContext:handler:]_block_invoke.83
- ___98-[RTLearnedLocationEngine _fetchCloudCurrentDeviceVisitsBetweenStartDate:endDate:ascending:error:]_block_invoke.576
- ___98-[RTLearnedLocationEngine _fetchCloudCurrentDeviceVisitsBetweenStartDate:endDate:ascending:error:]_block_invoke.578
- ___98-[RTPOIHarvester harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:]_block_invoke
- ___block_descriptor_40_e8_32r_e24_v32?0"NSError"8Q16^B24lr32l8
- ___block_descriptor_48_e8_32bs40r_e20_v20?0B8"NSError"12lr40l8s32l8
- ___block_descriptor_57_e8_32s40bs48r_e20_v20?0B8"NSError"12lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40bs48r_e20_v20?0B8"NSError"12lr48l8s32l8s40l8
- ___block_descriptor_72_e8_32s40r48r56r_e31_v24?0"RTMapItem"8"NSError"16lr40l8r48l8r56l8s32l8
- ___block_descriptor_72_e8_32s40s48s56bs64r_e33_v32?0"NSArray"8^B16"NSError"24ls56l8s32l8s40l8r64l8s48l8
- ___block_descriptor_73_e8_32s40s48bs56r_e5_v8?0ls32l8s48l8s40l8r56l8
- ___block_descriptor_80_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8s56l8s48l8r64l8
- ___block_descriptor_80_e8_32s40s48s56r64r_e31_v24?0"RTMapItem"8"NSError"16lr56l8r64l8s32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s48s56s64s72r_e31_v24?0"RTMapItem"8"NSError"16lr72l8s32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.1376
- ___block_literal_global.145
- ___block_literal_global.164
- ___block_literal_global.178
- ___block_literal_global.180
- ___block_literal_global.182
- ___block_literal_global.209
- ___block_literal_global.236
- ___block_literal_global.238
- ___block_literal_global.240
- ___block_literal_global.322
- ___block_literal_global.365
- ___block_literal_global.409
- ___block_literal_global.427
- ___block_literal_global.439
- ___block_literal_global.49
- ___block_literal_global.551
- ___block_literal_global.607
- ___block_literal_global.608
- ___block_literal_global.708
- ___block_literal_global.713
- ___block_literal_global.716
- ___block_literal_global.719
- ___block_literal_global.728
- ___block_literal_global.731
- ___block_literal_global.89
- ___block_literal_global.910
- ___block_literal_global.923
- ___block_literal_global.950
- ___block_literal_global.971
- ___handleShareAllLocationsChanged_block_invoke.965
- _objc_msgSend$_fetchReviewedPlacesWithOptions:handler:
- _objc_msgSend$_fetchReviewedPlacesWrapperWithOptions:handler:
- _objc_msgSend$_motionActivitiesFrom:to:error:
- _objc_msgSend$_poiHarvestForFingerprint:mapItem:referenceLocations:endDate:error:
- _objc_msgSend$collectMetricsForAppliedUserCuration:curatedVisit:learnedLocationStore:distanceCalculator:error:
- _objc_msgSend$fetchReviewedPlacesWithOptions:handler:
- _objc_msgSend$getWaypointDataFromWaypoints:
- _objc_msgSend$harvestCuration:mapItem:referenceLocations:poiHarvester:error:
- _objc_msgSend$harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:
- _objc_msgSend$hasUserReviewed
- _objc_msgSend$initWithAuthorizationManager:contactsManager:defaultsManager:deviceLocationPredictor:distanceCalculator:healthKitManager:learnedLocationStore:learnedLocationManager:locationManager:mapServiceManager:messagingService:motionActivityManager:navigationManager:platform:visitManager:visitConsolidator:sessionStore:suggestionsStore:suggestionsHelper:appDeletionManager:
- _objc_msgSend$initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:
- _objc_msgSend$initWithMapItem:accessPoints:locations:motionActivities:
- _objc_msgSend$initWithMapItem:date:
- _objc_msgSend$initWithMuid:lastSuggestedReviewDate:hasUserReviewed:modifiedDate:
- _objc_msgSend$lastSuggestedReviewDate
- _objc_msgSend$modificationTime
CStrings:
+ "%@, %@, attempting to interrupt training due to duration cap"
+ "%@, %@, collecting application metrics for curated label, %@"
+ "%@, %@, collecting submission metrics for user curation, %@"
+ "%@, %@, collecting user curation count metrics"
+ "%@, %@, duration cap interrupt completed successfully - training was stopped, latency: %.2f"
+ "%@, %@, duration cap interrupt failed with unexpected error, latency: %.2f, error: %@"
+ "%@, %@, duration cap interrupt was ignored due to model age (training allowed to continue), latency: %.2f, error: %@"
+ "%@, %@, failed to calculate curation distance, error: %@"
+ "%@, %@, failed to calculate distance to visit, error: %@"
+ "%@, %@, failed to collect applied curation metrics for curated label with ID %@, visit ID %@, error: %@"
+ "%@, %@, failed to fetch visits to LOIs within %@ meters, error: %@"
+ "%@, %@, invalid parameters for collecting applied user curation metrics"
+ "%@, %@, received invalid interruption source value"
+ "%@, %@, training duration cap timer already exists, not starting new one"
+ "%@, %@, training duration cap timer fired after %.1f seconds (%.1f minutes)"
+ "%@, %@, training duration cap timer invalidated"
+ "%@, %@, training duration cap timer started, will fire at %@ (in %.1f seconds), error: %@"
+ "%@, No waypoints found for clusterID,%@"
+ "%@, Pruned directory, error, %@"
+ "%@, Purged directory, error, %@"
+ "%@, Purged model file, %@, error, %@"
+ "%@, error fetching stored mapItems, %@"
+ "%@, error processing external mapItem, %@"
+ "%@, error storing local copy of mapItem, %@"
+ "%@, failed to create local copy of mapItem, %{sensitive}@"
+ "%@, found existing mapItem, %{sensitive}@"
+ "%@, geoMapItemIdentifier refresh for place, %{sensitive}@, last visit, %{sensitive}@, required, %@"
+ "%@, successfully processed external mapItem, %{sensitive}@"
+ "%@,%@ storeLocations in batches,locationCount,%lu,batchSize,%lu"
+ "%@,%@,%lu waypoints passed in for clusterID %@, maxWaypoints per chunk, %d"
+ "%@,%@,Cluster learning is already in progress. Skipping new request"
+ "%@,%@,Defer cluster learning before generating commuteGroups."
+ "%@,%@,Defer cluster learning before generating origin-destination Groups."
+ "%@,%@,Defer cluster learning before processing a commute."
+ "%@,%@,Defer cluster learning."
+ "%@,%@,Duplicate waypoint cleanup process disabled by default"
+ "%@,%@,Duplicate waypoint cleanup process finished successfully"
+ "%@,%@,Route generation process disabled by default"
+ "%@,%@,Route generation process finished successfully"
+ "%@,%@,Starting clean up process for clusters with duplicate waypoints"
+ "%@,%@,Starting rehydration process for clusters with waypoints but no route locations"
+ "%@,%@,Trip cluster processing is disabled"
+ "%@,%@,clean up operations done for %lu clusters,limit,%lu,breaking"
+ "%@,%@,converted %lu waypoints for clusterID,%@"
+ "%@,%@,defer,ClusterProcessing,%d"
+ "%@,%@,maxDeleteAttempts out of range. Clamping to between %lu and %lu"
+ "%@,%@,resetting deferral flag to false for force learning trigger"
+ "%@,%@,stored location batch,%d,totalBatchs,%d,batchSize,%d"
+ "%@,%@,walk and bike clusters disabled"
+ "%@,Called updateClusterRouteUsingWaypointsWithClusterID (%lu/%lu) for clusterID,%@"
+ "%@,Completed fillInRouteLocationsForClustersInStore - called updateClusterRouteUsingWaypointsWithClusterID %lu times,limit,%lu"
+ "%@,Count fetch results,count,%lu,error,%@"
+ "%@,Delete road transitions attempt,%d/%d,failed for clusterID,%@"
+ "%@,Delete routes attempt,%d/%d,failed for clusterID,%@"
+ "%@,Delete waypoints attempt,%d/%d,failed for clusterID,%@"
+ "%@,Deleted %lu waypoints for clusterID,%@"
+ "%@,Dispatching count fetch block for clusterID,%@"
+ "%@,Duplicate sequence number 1 detected,clusterID,%@"
+ "%@,Error fetching road transitions count for cluster ID,%@,error,%@"
+ "%@,Error fetching route count for cluster with cluster ID,%@,error,%@"
+ "%@,Error performing count fetch block,%@"
+ "%@,Failed to delete route location after %lu attempts for clusterID,%@,not updating route"
+ "%@,Failed to delete waypoints after %lu attempts for clusterID,%@,not updating waypoints or route locations"
+ "%@,Failed to delete waypoints for clusterID,%@"
+ "%@,Fetched waypoints,clusterID,%@,count,%lu"
+ "%@,Fetching route count with clusterID,%@"
+ "%@,Limit,%lu,reached in rehydration loop for clusterID,%@"
+ "%@,New clusterID,%@,commuteID,%@,using tripSegmentID,%@"
+ "%@,No clusters found for waypoint deletion"
+ "%@,Processed %lu clusters, deleted waypoints for %lu clusters,limit,%lu"
+ "%@,Processing deferred in deleteWaypointsForClustersWithDuplicateWaypoints loop for clusterID,%@"
+ "%@,Processing deferred in fillInRouteLocationsForClustersInStore loop for clusterID,%@"
+ "%@,Road transitions delete failed after %lu attempts"
+ "%@,Semaphore Error fetching road transitions count for cluster ID,%@,error,%@"
+ "%@,Semaphore Error fetching route count for cluster with cluster ID,%@,error,%@"
+ "%@,Semaphore error when calling constructRouteWithID using waypoints,%@,error,%@"
+ "%@,Stored new TripCluster Route from waypoints,%d,clusterID,%@"
+ "%@,Updated road transitions for clusterID,%@,commuteID,%@,updated cluster commuteID,%@,using tripSegmentID,%@"
+ "%@,constructRouteUsingWaypoints for %@,received reconstructed route"
+ "%@,constructRouteUsingWaypoints,failed,clusterID,%@"
+ "%@,constructRouteUsingWaypoints,success,clusterID,%@"
+ "%@,deleted old, and stored new TripCluster Route,%d,clusterID,%@"
+ "%@,deleted old, and stored new TripCluster Waypoints,%d,clusterID,%@"
+ "%@,trip segments processed,%d/%d,exitByDefer,%d"
+ "%K <= %f"
+ "%K > %@ && %K < %@"
+ "%{public}@, %{public}@, %lu %s fingerprints with access points found between %{private}@, fallback time window, %{public}d, error, %{public}@"
+ "%{public}@, %{public}@, Canceling harvest after error fetching fingerprints, %{public}@, between start date, %{private}@, end date, %{private}@, harvest type, %{public}@"
+ "%{public}@, %{public}@, Canceling harvest because visit start date, %{private}@, comes after end date, %{private}@, for harvest type, %{public}@, error, %{public}@"
+ "%{public}@, %{public}@, Failed to copy map item, %{sensitive}@, exiting early"
+ "%{public}@, %{public}@, Fetched %lu locations for access points, %{sensitive}@, harvest params, %{public}@, error, %{public}@"
+ "%{public}@, %{public}@, Fetched %lu motion states between %{private}@, error, %{public}@"
+ "%{public}@, %{public}@, Fetched access points for fingerprint, %{sensitive}@, end date, %{private}@, error, %{public}@"
+ "%{public}@, %{public}@, No fingerprints with access points found between %{private}@, POI data will not be harvested"
+ "%{public}@, %{public}@, No settled fingerprints with access points found, retrying with unsettled"
+ "%{public}@, %{public}@, No valid map item provided, exiting early"
+ "%{public}@, %{public}@, date check failed, current date, %@, suggestion skipped because time of day is between %{public}f to %{public}f"
+ "%{public}@, %{public}@, submitting metrics, %@"
+ "%{public}@, %{public}@, time of the day logged from user context, %f, suppressing suggestion between %{public}f to %{public}f"
+ "+[RTPOIHarvestUtilities harvestCuration:mapItem:visitLocations:poiHarvester:error:]"
+ "-[RTTripClusterManager _fetchLearnedRoutesWithOptionsDefault:handler:]"
+ "-[RTTripClusterProcessor deleteWaypointsForClustersWithDuplicateWaypoints:tripClusterWaypointStore:tripClusterRouteStore:tripClusterRouteTransitionsStore:minimumTraversalCountForLearnedRoutes:]"
+ "-[RTTripClusterRouteStore _fetchTripClusterRouteCountWithOptions:handler:]"
+ "00:11:39"
+ "<%@: %p, downsampleFactor,%ld,windowSize,%ld,maxLocationPerTrip,%ld,maxProcessedTripSegments,%ld,useMaxProcessedTripSegments,%@,purgeClustersDataBase,%@,distBetweenTrips_km,%.2f,distanceThreshold_m,%.2f,unreachableDistance_m,%.2f,clusterLifeTimeThreshold_d,%ld,lengthDeviationThreshold_m,%.2f,locationThresholdRadius_m,%.2f,distAccuracyThreshold_m,%.2f,writeTripSegmentsToFile,%@,enableClusterProcessing,%@,saveToHTML,%@,clusterProcessorMode,%ld,learnedRoutesCurrentLocationSPIEnabled,%@,maxCleanUpOperationsCountPerRun,%ld,maxRouteRehydrationsCountPerRun,%ld,maxDeletionAttemptsForClusterData,%ld,rehydrateRouteLocationsFromWaypoints,%@,cleanUpClusterWithDuplicateWaypoints,%@>"
+ "@\"SMTrialManager\""
+ "@184@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176"
+ "@36@0:8@16i24@28"
+ "@48@0:8@16^Q24@32^@40"
+ "@48@0:8Q16@24@32^@40"
+ "@52@0:8@16@24@32@40i48"
+ "@56@0:8@16@24@32Q40@48"
+ "B64@0:8@16@24@32@40Q48^@56"
+ "B72@0:8@16Q24@32@40Q48@56^@64"
+ "CoreRoutine.BluePOIHarvest"
+ "Duplicate sequence numbers detected in waypoint data"
+ "Failed to create local copy of mapItem"
+ "Failed to update creation date for backup file %@: %@"
+ "HarvestType_VisitUnsettled"
+ "Harvested user curation of map item, %{sensitive}@, locations, %{sensitive}@, start, %@, end, %@, error, %{public}@"
+ "Harvested visit to map item, %{sensitive}@, source, %lu, location, %{sensitive}@, start, %@, end, %@, harvest type, %{public}lu, error, %{public}@"
+ "Interrupted: Duration Cap"
+ "Interrupted: System Deferral"
+ "Invalid parameter not satisfying: dateInterval != nil"
+ "Invalid parameter not satisfying: harvestParameters"
+ "Invalid parameter not satisfying: harvestType != RTHarvestTypeUnknown"
+ "Invalid parameter not satisfying: harvestTypeInOut != nil"
+ "Invalid parameter not satisfying: metrics != nil"
+ "Invalid parameter not satisfying: settledState == RTScenarioTriggerSettledStateSettled || settledState == RTScenarioTriggerSettledStateUnsettled"
+ "Invalid parameter not satisfying: trialManager"
+ "Invalid parameter not satisfying: tripClusterWaypointStore (in %s:%d)"
+ "RTDefaultsPredictedContextManagerTrainingDurationCapInterval"
+ "RTDefaultsTripClusterCleanUpClustersWithDuplicateWaypoints"
+ "RTDefaultsTripClusterEnableWalkBikeClustering"
+ "RTDefaultsTripClusterMaxCleanUpOperationsCountPerRun"
+ "RTDefaultsTripClusterMaxDeletionAttemptsForClusterData"
+ "RTDefaultsTripClusterMaxRouteRehydrationsCountPerRun"
+ "RTDefaultsTripClusterRehydrateRouteLocationsFromWaypoints"
+ "RTDefaultsTripSegmentClusterRejectDuplicateWaypointsKey"
+ "RTDefaultsTripSegmentClusterWaypointMaxPerChunk"
+ "RTPOIHarvesterMetrics"
+ "RTTripClusterManager:defer,ClusterProcessing,%d"
+ "Received %lu locations for %lu access points; filled in gaps and now have %lu locations"
+ "SMDefaultsSafetyCacheInitCKZoneCreateRecordsLatencyKey"
+ "SMDefaultsSafetyCacheInitCKZoneSaveLatencyKey"
+ "SMDefaultsSafetyCacheInitCKZoneSubscribeChangesLatencyKey"
+ "Sep 29 2025"
+ "Submitted POI harvest success, %{public}s, access point count, %lu, location count, %lu, triggerType, %{public}d, harvestType, %{public}@, error, %{public}@"
+ "T@\"RTXPCTimerAlarm\",&,N,V_trainingDurationCapTimer"
+ "T@\"SMTrialManager\",R,C,N,V_trialManager"
+ "TB,N,V_cleanUpClusterWithDuplicateWaypoints"
+ "TB,N,V_enableWalkBikeClustering"
+ "TB,N,V_rehydrateRouteLocationsFromWaypoints"
+ "TB,N,V_rejectDuplicateWaypoints"
+ "TB,V_shouldDeferClusterProcessing"
+ "TQ,N,V_fingerprintErrorCount"
+ "TQ,N,V_harvestCreationCount"
+ "TQ,N,V_harvestSubmissionCount"
+ "TQ,N,V_harvestSubmissionErrorCount"
+ "TQ,N,V_harvestType"
+ "TQ,N,V_mapItemCopyErrorCount"
+ "TQ,N,V_maxCleanUpOperationsCountPerRun"
+ "TQ,N,V_maxDeletionAttemptsForClusterData"
+ "TQ,N,V_maxRouteRehydrationsCountPerRun"
+ "TQ,N,V_pendingInterruptSource"
+ "TQ,N,V_referenceLocationsCount"
+ "TQ,N,V_settledFingerprintCountWithTimeWindowFallback"
+ "TQ,N,V_settledFingerprintCountWithoutTimeWindowFallback"
+ "TQ,N,V_totalAccessPointCount"
+ "TQ,N,V_totalAccessPointErrorCount"
+ "TQ,N,V_totalEstimatedFingerprintLocationsCount"
+ "TQ,N,V_totalEstimatedFingerprintLocationsErrorCount"
+ "TQ,N,V_totalFetchedFingerprintLocationsCount"
+ "TQ,N,V_totalFetchedFingerprintLocationsErrorCount"
+ "TQ,N,V_totalMotionActivitiesCount"
+ "TQ,N,V_totalMotionActivitiesErrorCount"
+ "TQ,N,V_unsettledFingerprintCountWithTimeWindowFallback"
+ "TQ,N,V_unsettledFingerprintCountWithoutTimeWindowFallback"
+ "Ti,N,V_maxWaypointsPerChunk"
+ "Timeout waiting for estimated locations for %lu access points; giving up after %lu locations"
+ "_augmentedLocationsForAccessPoints:metrics:error:"
+ "_cleanUpClusterWithDuplicateWaypoints"
+ "_enableWalkBikeClustering"
+ "_fetchLearnedRoutesWithOptionsDefault:handler:"
+ "_fetchTripClusterRouteCountWithOptions:handler:"
+ "_fingerprintAccessPointsForSettledState:withinInterval:metrics:error:"
+ "_fingerprintAccessPointsWithinInterval:harvestType:metrics:error:"
+ "_fingerprintErrorCount"
+ "_handleTrainingDurationCapTimerWithStartTime:"
+ "_harvestCreationCount"
+ "_harvestPOI:mapItemSource:accessPointArrays:referenceLocations:harvestType:metrics:error:"
+ "_harvestSubmissionCount"
+ "_harvestSubmissionErrorCount"
+ "_harvestType"
+ "_invalidateTrainingDurationCapTimer"
+ "_isUpdateLearnedPlaceWithGeomapItemIdentifierRequired:"
+ "_mapItemCopyErrorCount"
+ "_maxCleanUpOperationsCountPerRun"
+ "_maxDeletionAttemptsForClusterData"
+ "_maxRouteRehydrationsCountPerRun"
+ "_maxWaypointsPerChunk"
+ "_motionActivitiesWithinInterval:error:"
+ "_pendingInterruptSource"
+ "_poiHarvestForAccessPoints:mapItem:referenceLocations:harvestType:metrics:"
+ "_referenceLocationsCount"
+ "_rehydrateRouteLocationsFromWaypoints"
+ "_rejectDuplicateWaypoints"
+ "_settledFingerprintCountWithTimeWindowFallback"
+ "_settledFingerprintCountWithoutTimeWindowFallback"
+ "_shouldDeferClusterProcessing"
+ "_shouldFilterError:"
+ "_startTrainingDurationCapTimerWithStartTime:"
+ "_storeLocationsByBatches:handler:"
+ "_storeLocationsForBatch:batchNo:batchSize:handler:"
+ "_submitMetricsForApplicationOfCuratedLabel:visit:result:"
+ "_totalAccessPointCount"
+ "_totalAccessPointErrorCount"
+ "_totalEstimatedFingerprintLocationsCount"
+ "_totalEstimatedFingerprintLocationsErrorCount"
+ "_totalFetchedFingerprintLocationsCount"
+ "_totalFetchedFingerprintLocationsErrorCount"
+ "_totalMotionActivitiesCount"
+ "_totalMotionActivitiesErrorCount"
+ "_trainingDurationCapInterval"
+ "_trainingDurationCapTimer"
+ "_trialManager"
+ "_unsettledFingerprintCountWithTimeWindowFallback"
+ "_unsettledFingerprintCountWithoutTimeWindowFallback"
+ "_updateLastVehicleEventAndNotify:"
+ "_updateLearnedPlaceWithGeomapItemIdentifier:"
+ "accessPointsCount"
+ "appIdentifier"
+ "cleanUpClusterWithDuplicateWaypoints"
+ "collectMetricsForAppliedLabel:curatedVisit:learnedLocationStore:distanceCalculator:applicationResult:error:"
+ "com.apple"
+ "com.apple.CoreRoutine.BluePOIMonitor"
+ "com.apple.CoreRoutine.LocationContextManager"
+ "com.apple.CoreRoutine.VisitMonitor"
+ "com.apple.CoreRoutine.internal"
+ "com.apple.routined.predictedContext.trainingDurationCapTimer"
+ "constructRouteFromWaypoints:forRouteID:withOptions:outputHandler:completionHandler:"
+ "dateInterval != nil"
+ "deferClusterProcessing:"
+ "deleteTripClusterRoadTransitionsWithClusterID:maxDeleteAttempts:"
+ "deleteTripClusterRouteWithClusterID:maxDeleteAttempts:"
+ "deleteTripClusterWaypointWithClusterID:maxDeleteAttempts:"
+ "deleteWaypointsForClustersWithDuplicateWaypoints:tripClusterWaypointStore:tripClusterRouteStore:tripClusterRouteTransitionsStore:minimumTraversalCountForLearnedRoutes:"
+ "divideArray:intoChunks:"
+ "doubleValueForFactor:"
+ "enableWalkBikeClustering"
+ "error fetching geoMapItemHandle, %@"
+ "fetchTripClusterRouteCountWithClusterID:handler:"
+ "fillInRouteLocationsForClustersInStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRoadTransitionsStore:minimumTraversalCountForLearnedRoutes:"
+ "fingerprintErrorCount"
+ "firstResultOnly"
+ "generateMissingRoutesForClusters"
+ "getTripClusterRoadTransitionsDataCountForClusterID:"
+ "getTripClusterRouteCountWithClusterID:"
+ "getWaypointDataFromWaypoints:maxWaypointsPerChunk:"
+ "harvestCreationCount"
+ "harvestCuration:mapItem:visitLocations:poiHarvester:error:"
+ "harvestPOI:mapItemSource:visitLocations:visitEntryDate:visitExitDate:harvestType:error:"
+ "harvestSubmissionCount"
+ "harvestSubmissionErrorCount"
+ "harvestType"
+ "harvestTypeInOut != nil"
+ "harvested %lu visits, mapItem, %{sensitive}@, success, %{public}@, error, %{public}@"
+ "identifier, %@, name, %@, category, %@, categoryMUID, %@, latitude, %@, longitude, %@, uncertainty, %@, referenceFrame, %@, mapItemSource, %@, mapItemPlaceType, %@, muid, %@, resultProviderID, %@, geoMapItemHandle, %@, geoMapItemIdentifier, %@, creationDate, %@, expirationDate, %@, displayLanguage, %@, disputed, %@, address, %@, extendedAttributesIdentifier, %@"
+ "initWithAscending:sortIndex:submissionDateInterval:visitDateInterval:limit:"
+ "initWithAuthorizationManager:contactsManager:defaultsManager:deviceLocationPredictor:distanceCalculator:healthKitManager:learnedLocationStore:learnedLocationManager:locationManager:mapServiceManager:messagingService:motionActivityManager:navigationManager:platform:visitManager:visitConsolidator:sessionStore:suggestionsStore:suggestionsHelper:appDeletionManager:trialManager:"
+ "initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
+ "initWithMapItem:accessPoints:locations:motionActivities:triggerType:"
+ "initWithMapItem:triggerType:date:"
+ "isBluePOITileNotAvailableError"
+ "mapItem cannot be nil"
+ "mapItemCopyErrorCount"
+ "maxCleanUpOperationsCountPerRun"
+ "maxDeletionAttemptsForClusterData"
+ "maxRouteRehydrationsCountPerRun"
+ "maxWaypointsPerChunk"
+ "metrics != nil"
+ "modelBinPath"
+ "pendingInterruptSource"
+ "processExternalMapItem:handler:"
+ "purgeWithError:"
+ "q24@?0@\"RTLocation\"8@\"RTLocation\"16"
+ "q24@?0@\"RTTripClusterWaypoint\"8@\"RTTripClusterWaypoint\"16"
+ "q24@?0@\"RTWiFiAccessPoint\"8@\"RTWiFiAccessPoint\"16"
+ "referenceLocationsCount"
+ "refresh"
+ "refreshAllObjects"
+ "rehydrateRouteLocationsFromWaypoints"
+ "rejectDuplicateWaypoints"
+ "sendSuggestionsConversionEventForSuggestion:selected:sessionStarted:"
+ "setAttributes:ofItemAtPath:error:"
+ "setCleanUpClusterWithDuplicateWaypoints:"
+ "setEnableWalkBikeClustering:"
+ "setFingerprintErrorCount:"
+ "setGeoMapItemIdentifier:"
+ "setHarvestCreationCount:"
+ "setHarvestSubmissionCount:"
+ "setHarvestSubmissionErrorCount:"
+ "setHarvestType:"
+ "setMapItemCopyErrorCount:"
+ "setMaxCleanUpOperationsCountPerRun:"
+ "setMaxDeletionAttemptsForClusterData:"
+ "setMaxRouteRehydrationsCountPerRun:"
+ "setMaxWaypointsPerChunk:"
+ "setPendingInterruptSource:"
+ "setReferenceLocationsCount:"
+ "setRehydrateRouteLocationsFromWaypoints:"
+ "setRejectDuplicateWaypoints:"
+ "setSettledFingerprintCountWithTimeWindowFallback:"
+ "setSettledFingerprintCountWithoutTimeWindowFallback:"
+ "setShouldDeferClusterProcessing:"
+ "setTotalAccessPointCount:"
+ "setTotalAccessPointErrorCount:"
+ "setTotalEstimatedFingerprintLocationsCount:"
+ "setTotalEstimatedFingerprintLocationsErrorCount:"
+ "setTotalFetchedFingerprintLocationsCount:"
+ "setTotalFetchedFingerprintLocationsErrorCount:"
+ "setTotalMotionActivitiesCount:"
+ "setTotalMotionActivitiesErrorCount:"
+ "setTrainingDurationCapTimer:"
+ "setUnsettledFingerprintCountWithTimeWindowFallback:"
+ "setUnsettledFingerprintCountWithoutTimeWindowFallback:"
+ "settled"
+ "settledFingerprintCountWithTimeWindowFallback"
+ "settledFingerprintCountWithoutTimeWindowFallback"
+ "shouldDeferClusterProcessing"
+ "totalAccessPointCount"
+ "totalAccessPointErrorCount"
+ "totalErrorCount"
+ "totalEstimatedFingerprintLocationsCount"
+ "totalEstimatedFingerprintLocationsErrorCount"
+ "totalFetchedFingerprintLocationsCount"
+ "totalFetchedFingerprintLocationsErrorCount"
+ "totalFingerprintCount"
+ "totalLocationCount"
+ "totalMotionActivitiesCount"
+ "totalMotionActivitiesErrorCount"
+ "totalSettledFingerprintCount"
+ "totalUnsettledFingerprintCount"
+ "trainingDurationCapTimer"
+ "trialManager"
+ "unsettledFingerprintCountWithTimeWindowFallback"
+ "unsettledFingerprintCountWithoutTimeWindowFallback"
+ "update GeoMapItemHandle for place, %{sensitive}@"
+ "updateClusterRouteUsingWaypointsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:"
+ "v40@0:8@16@24Q32"
+ "v52@0:8@16@24@32@40i48"
+ "zoneCreateRecordsLatency"
+ "zoneSaveLatency"
+ "zoneSubscribeChangesLatency"
- " fetched, %lu, reviewedPlaces, error, %@"
- "\""
- "%@, %@, Failed to copy map item, %@, exiting early"
- "%@, %@, No fingerprints found between start date, %@, and end date, %@, POI data will not be harvested"
- "%@, %@, No valid map item provided, exiting early"
- "%@, %@, date check failed, current date, %@, suggestion skipped because time of day is between %f to %f"
- "%@, %@, failed to collect applied curation metrics for visit %@, error: %@"
- "%@, %@, likely receivers don't exist"
- "%@, %@, no eligible buddy for first time user, handles, %@"
- "%@, %lu places from query, error, %@"
- "%@, Purge files failed with error, %@"
- "%@, hasMapItemFromCurrentDevice: %@, error, %@"
- "%@,%@,converted %lu waypoints"
- "%@,Fetched waypoint,clusterID,%@,clRoadID,%{sensitive}llu,LL,%{sensitive}.7lf,%{sensitive}.7lf,course,%.3f,sequence,%u"
- "%@,New clusterID,%@,commuteID,%@"
- "%@,Processed,%d,trip segments"
- "%@,Updated road transitions for clusterID,%@,commuteID,%@,updated cluster commuteID,%@"
- "%@,deleted old, and stored new TripCluster Route,%d"
- "%@,deleted old, and stored new TripCluster Waypoints,%d"
- "+[RTPOIHarvestUtilities harvestCuration:mapItem:referenceLocations:poiHarvester:error:]"
- "-[RTMapsSupportManager _fetchReviewedPlacesWithOptions:handler:]"
- "-[RTMapsSupportManager _fetchReviewedPlacesWrapperWithOptions:handler:]"
- "20:52:23"
- "<%@: %p, downsampleFactor,%ld,windowSize,%ld,maxLocationPerTrip,%ld,maxProcessedTripSegments,%ld,useMaxProcessedTripSegments,%@,purgeClustersDataBase,%@,distBetweenTrips_km,%.2f,distanceThreshold_m,%.2f,unreachableDistance_m,%.2f,clusterLifeTimeThreshold_d,%ld,lengthDeviationThreshold_m,%.2f,locationThresholdRadius_m,%.2f,distAccuracyThreshold_m,%.2f,writeTripSegmentsToFile,%@,enableClusterProcessing,%@,saveToHTML,%@,clusterProcessorMode,%ld,learnedRoutesCurrentLocationSPIEnabled,%@>"
- "@44@0:8Q16@24B32@36"
- "Error was issued during fetching locationsOfInterest from store, error, %@"
- "HarvestType_Review"
- "Interrupted"
- "RTReviewedPlace"
- "ReviewedPlaceLastFetchedDate"
- "Sep 15 2025"
- "T@\"NSDate\",R,N,V_lastSuggestedReviewDate"
- "T@\"NSDate\",R,N,V_modifiedDate"
- "TB,R,N,V_hasUserReviewed"
- "TQ,R,N,V_muid"
- "Time of the day logged from user context: %f"
- "_fetchReviewedPlacesWithOptions:handler:"
- "_fetchReviewedPlacesWrapperWithOptions:handler:"
- "_harvestFeedbackData"
- "_hasUserReviewed"
- "_lastSuggestedReviewDate"
- "_modifiedDate"
- "_motionActivitiesFrom:to:error:"
- "_poiHarvestForFingerprint:mapItem:referenceLocations:endDate:error:"
- "collectMetricsForAppliedUserCuration:curatedVisit:learnedLocationStore:distanceCalculator:error:"
- "collecting application metrics for user curation, %@"
- "collecting submission metrics for user curation, %@"
- "collecting user curation count metrics"
- "failed to calculate curation distance, error: %@"
- "failed to calculate distance to visit, error: %@"
- "failed to fetch visits to LOIs within %@ meters, error: %@"
- "fetchReviewedPlacesWithOptions:handler:"
- "fetched, %lu, reviewedPlaces, error, %@"
- "getWaypointDataFromWaypoints:"
- "harvestCuration:mapItem:referenceLocations:poiHarvester:error:"
- "harvestPOI:mapItemSource:referenceLocations:startDate:endDate:harvestType:error:"
- "harvested %lu visits as feedback data, mapItem, %{sensitive}@, success, %@, error %@"
- "harvested %lu visits, mapItem, %{sensitive}@, success, %@, error %@"
- "harvested fingerprint, %@, poiHarvest, %@, triggerType, %d, harvestType, %@, error, %@"
- "hasUserReviewed"
- "identifier, %@, name, %@, category, %@, categoryMUID, %@, latitude, %@, longitude, %@, uncertainty, %@, referenceFrame, %@, mapItemSource, %@, mapItemPlaceType, %@, muid, %@, resultProviderID, %@, geoMapItemHandle, %@, creationDate, %@, expirationDate, %@, displayLanguage, %@, disputed, %@, address, %@, extendedAttributesIdentifier, %@"
- "initWithAuthorizationManager:contactsManager:defaultsManager:deviceLocationPredictor:distanceCalculator:healthKitManager:learnedLocationStore:learnedLocationManager:locationManager:mapServiceManager:messagingService:motionActivityManager:navigationManager:platform:visitManager:visitConsolidator:sessionStore:suggestionsStore:suggestionsHelper:appDeletionManager:"
- "initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:"
- "initWithMapItem:accessPoints:locations:motionActivities:"
- "initWithMapItem:date:"
- "initWithMuid:lastSuggestedReviewDate:hasUserReviewed:modifiedDate:"
- "invalid parameters for collecting applied user curation metrics"
- "lastSuggestedReviewDate"
- "lookbackWindow"
- "metricsKey"
- "modificationTime"
- "modificationTime >= &@"
- "modifiedDate"
- "muid, %lu, lastSuggestedReviewDate, %@, hasUserReviewed, %@, stringFromDate, %@"
- "reviewed place fetched, %@"

```
