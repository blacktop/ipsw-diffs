## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1048.0.0.0.0
-  __TEXT.__text: 0x5c9064
-  __TEXT.__auth_stubs: 0x2140
-  __TEXT.__objc_methlist: 0x30418
-  __TEXT.__const: 0x4558
+1053.0.1.0.0
+  __TEXT.__text: 0x5de538
+  __TEXT.__auth_stubs: 0x2180
+  __TEXT.__objc_methlist: 0x30a30
+  __TEXT.__const: 0x4608
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x7104a
-  __TEXT.__cstring: 0x43547
-  __TEXT.__swift5_capture: 0x8c
+  __TEXT.__oslogstring: 0x7440e
+  __TEXT.__cstring: 0x448f8
+  __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__constg_swiftt: 0x88
   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x27460
-  __TEXT.__ustring: 0x16
-  __TEXT.__unwind_info: 0xd7e8
-  __TEXT.__eh_frame: 0x368
-  __TEXT.__objc_classname: 0x5796
-  __TEXT.__objc_methname: 0x8ebf1
-  __TEXT.__objc_methtype: 0xce1f
-  __TEXT.__objc_stubs: 0x54100
-  __DATA_CONST.__got: 0x3030
-  __DATA_CONST.__const: 0xf138
-  __DATA_CONST.__objc_classlist: 0x14f8
+  __TEXT.__gcc_except_tab: 0x27b98
+  __TEXT.__ustring: 0x1e
+  __TEXT.__unwind_info: 0xdab0
+  __TEXT.__eh_frame: 0x390
+  __TEXT.__objc_classname: 0x57fa
+  __TEXT.__objc_methname: 0x90440
+  __TEXT.__objc_methtype: 0xcec1
+  __TEXT.__objc_stubs: 0x55100
+  __DATA_CONST.__got: 0x3088
+  __DATA_CONST.__const: 0xf558
+  __DATA_CONST.__objc_classlist: 0x1520
   __DATA_CONST.__objc_catlist: 0x3a8
   __DATA_CONST.__objc_protolist: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18d38
+  __DATA_CONST.__objc_selrefs: 0x19118
   __DATA_CONST.__objc_protorefs: 0x120
-  __DATA_CONST.__objc_superrefs: 0x1168
-  __DATA_CONST.__objc_arraydata: 0x2870
-  __AUTH_CONST.__auth_got: 0x10b0
-  __AUTH_CONST.__const: 0x31b8
-  __AUTH_CONST.__cfstring: 0x27300
-  __AUTH_CONST.__objc_const: 0x4f810
-  __AUTH_CONST.__objc_intobj: 0x4248
-  __AUTH_CONST.__objc_arrayobj: 0xd50
-  __AUTH_CONST.__objc_doubleobj: 0x9e0
-  __AUTH_CONST.__objc_dictobj: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x1180
+  __DATA_CONST.__objc_arraydata: 0x2990
+  __AUTH_CONST.__auth_got: 0x10d0
+  __AUTH_CONST.__const: 0x3260
+  __AUTH_CONST.__cfstring: 0x283c0
+  __AUTH_CONST.__objc_const: 0x50128
+  __AUTH_CONST.__objc_intobj: 0x4518
+  __AUTH_CONST.__objc_arrayobj: 0xd98
+  __AUTH_CONST.__objc_doubleobj: 0xab0
+  __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x29d8
-  __DATA.__objc_ivar: 0x24dc
-  __DATA.__data: 0x2b58
+  __AUTH.__objc_data: 0x2b68
+  __DATA.__objc_ivar: 0x2534
+  __DATA.__data: 0x2b90
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_ivar: 0x1124
+  __DATA_DIRTY.__objc_ivar: 0x1144
   __DATA_DIRTY.__objc_data: 0xa890
   __DATA_DIRTY.__data: 0x5c8
   __DATA_DIRTY.__bss: 0x200

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BFF53444-5439-3AC4-875E-F789A1EEF885
-  Functions: 19860
-  Symbols:   64051
-  CStrings:  39189
+  UUID: 9AE2205F-F490-3AF7-8569-7C57FD99BA3A
+  Functions: 20037
+  Symbols:   64703
+  CStrings:  39811
 
Symbols:
+ +[RTAccountManager accountStatusToString:]
+ +[RTFeatureExtractor countKeyForFeature:]
+ +[RTFeatureExtractor latencyKeyForFeature:]
+ +[RTFeatureExtractor logFeatureExtractionForFeature:stimulationDate:featureArray:success:toDict:]
+ +[RTFeatureExtractor metricCodeForFeatureExtractorOperationType:]
+ +[RTFeatureExtractor successKeyForFeature:]
+ +[RTLearnedLocationReconcilerPerDevice sortReconciledVisitsByMapItemQuality:]
+ +[RTPredictedContextManager stringFromTrainResult:]
+ +[RTPredictedContextMetricsManager calculatePredictability:priorVisits:timeWindowHalfWidth:]
+ +[RTPredictedContextMetricsManager getAllContextsInOneArray:]
+ +[RTPredictedContextMetricsManager getFrequentLoiFromCount:]
+ +[RTPredictedContextMetricsManager getHighProbabilityPredictedContexts:]
+ +[RTPredictedContextMetricsManager getPredictedContextLocationFromDictionary:]
+ +[RTPredictedContextMetricsManager getRequestCountByInferenceTriggerReasonForRequests:]
+ +[RTPredictedContextMetricsManager getTotalInferenceLatencyForRequests:]
+ +[RTPredictedContextMetricsManager getTotalMemoryFootprintForRequests:]
+ +[RTPredictedContextMetricsManager isCorrectPrediction:forTruthVisits:matchingVisit:]
+ +[RTPredictedContextMetricsManager isCorrectTruth:forPredictions:]
+ +[RTPredictedContextMetricsManager isWithinMidnightBoundary:targetDay:interval:]
+ +[RTUserCurationMetrics collectMetricsForSubmittedUserCuration:submissionResult:]
+ +[RTUserCurationMetrics collectUserCurationCountMetricsWithUserCurationStore:error:]
+ +[RTVisit(RTExtensions) visits:withLoiIdentifier:]
+ +[RTVisit(RTExtensions) visitsWithExit:beforeDate:]
+ +[RTVisit(RTExtensions) visitsWithExit:dateInterval:]
+ +[RTVisitRedactionUtilities obfuscatedVisitDateIntervalForEntryDate:previousObfuscatedVisitEntryDate:]
+ +[RTVisitRedactionUtilities redactVisits:authorizedLocations:bluePOICategoryDenylist:]
+ +[RTVisitRedactionUtilities shouldRedactAllVisitsForCurrentRegion]
+ +[RTVisitRedactionUtilities visitStartDateRangeFromObfuscatedStartDate:]
+ -[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]
+ -[RTBluePOIMonitorEnabler setStationaryStartDate:]
+ -[RTBluePOIMonitorEnabler stationaryStartDate]
+ -[RTBlueSkyDailyMetrics .cxx_destruct]
+ -[RTBlueSkyDailyMetrics create]
+ -[RTBlueSkyDailyMetrics defaultsManager]
+ -[RTBlueSkyDailyMetrics description]
+ -[RTBlueSkyDailyMetrics increaseCountForKey:]
+ -[RTBlueSkyDailyMetrics initWithDefaultsManager:]
+ -[RTBlueSkyDailyMetrics init]
+ -[RTBlueSkyDailyMetrics metrics]
+ -[RTBlueSkyDailyMetrics reset]
+ -[RTBlueSkyDailyMetrics shouldSubmit]
+ -[RTBlueSkyDailyMetrics submit]
+ -[RTCompanionLinkManager _onDailyMetricsNotification:]
+ -[RTCompanionLinkManager _setup]
+ -[RTCompanionLinkManager _updatePendingSyncMetrics:]
+ -[RTCompanionLinkManager _updateSyncCachedMetrics:]
+ -[RTCompanionLinkManager _updateSyncMetrics:]
+ -[RTCompanionLinkManager _updateSyncSuccessMetrics:waitRequired:]
+ -[RTCompanionLinkManager dailyBlueSkyMetrics]
+ -[RTCompanionLinkManager defaultsManager]
+ -[RTCompanionLinkManager initWithCompanionLinkClient:dailyBlueSkyMetrics:defaultsManager:]
+ -[RTCompanionLinkManager initWithDefaultsManager:]
+ -[RTCompanionLinkManager lastPlaceInferenceSyncAttemptDate]
+ -[RTCompanionLinkManager lastVisitSyncAttemptDate]
+ -[RTCompanionLinkManager onDailyMetricsNotification:]
+ -[RTCompanionLinkManager setDailyBlueSkyMetrics:]
+ -[RTCompanionLinkManager setLastPlaceInferenceSyncAttemptDate:]
+ -[RTCompanionLinkManager setLastVisitSyncAttemptDate:]
+ -[RTFeatureExtractor _extractFeatures:operationType:lookbackDurations:outError:]
+ -[RTFeatureExtractor _submitMetrics:]
+ -[RTFeatureExtractor initWithLearnedLocationManager:visitManager:locationManager:eventManager:navigationManager:mapsSupportManager:motionActivityManager:vehicleLocationProvider:visitConsolidator:healthKitManager:homeKitManager:tripLocationPropagator:metricsManager:]
+ -[RTFeatureExtractor metricsManager]
+ -[RTFeatureExtractor setMetricsManager:]
+ -[RTLearnedLocationEngine _createLOIForPlace:error:]
+ -[RTLearnedLocationEngine _findOrCreateLOIForMapItem:error:]
+ -[RTLearnedLocationEngine _findVisitsAssociatedWithCurrentPlaceCuration:error:]
+ -[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]
+ -[RTLearnedLocationEngine _submitDailyUserCurationMetrics]
+ -[RTLearnedLocationStore _fetchCurrentDeviceWithHandler:]
+ -[RTLearnedLocationStore _fetchVisitsOverlappingDate:handler:]
+ -[RTLearnedLocationStore fetchCurrentDeviceWithHandler:]
+ -[RTLearnedLocationStore fetchVisitsOverlappingDate:handler:]
+ -[RTLearnedPlaceTypeInferencePlaceStats visitIntervalsForVisits:place:]
+ -[RTLearnedPlaceTypeInferencePlaceStats visitsPredatingCurrentDeviceFromVisits:]
+ -[RTLearnedRouteCloudKitSyncStatisticsMetrics initForDefaultMetric]
+ -[RTLearnedRouteClusterStatisticsMetrics initForDefaultMetric]
+ -[RTLearnedRouteCompoundRouteMetrics initForDefaultMetric]
+ -[RTLearnedRouteMultiModalStatisticsMetrics initForDefaultMetric]
+ -[RTLearnedRouteSPIStatisticsMetrics initForDefaultMetric]
+ -[RTMotionActivityManager_CoreMotion _setup]
+ -[RTPersistenceDriver _setupPersistenceAfterConfigurationChange:cloudSyncAuthorization:accountStatus:account:]
+ -[RTPersistenceDriver _shouldAttemptSetupAccordingToAccountStatus:account:]
+ -[RTPersistenceDriver _shouldAttemptSetupAccordingToCloudSyncAuthorization:]
+ -[RTPersistenceDriver currentAccountStatus]
+ -[RTPersistenceDriver setCurrentAccountStatus:]
+ -[RTPersistenceMirroringManager(Metrics) mirroringManager:exceededHistoryType:count:limit:hasExceeded:]
+ -[RTPredictedContextManager _evaluateTrainErrorForResult:]
+ -[RTPredictedContextManager _onVisit:]
+ -[RTPredictedContextManager _processTrainingResult:]
+ -[RTPredictedContextManager currentVisitType]
+ -[RTPredictedContextManager setCurrentVisitType:]
+ -[RTPredictedContextMetricsManager _onDailyMetricsNotification:]
+ -[RTPredictedContextMetricsManager _setup]
+ -[RTPredictedContextMetricsManager getPredictionsForInterval:completion:]
+ -[RTPredictedContextMetricsManager getRequestsForInterval:completion:]
+ -[RTPredictedContextMetricsManager getVisitsForInterval:completion:]
+ -[RTPredictedContextMetricsManager initWithManagedConfiguration:predictedContextStore:defaultsManager:visitConsolidator:]
+ -[RTPredictedContextMetricsManager onDailyMetricsNotification:]
+ -[RTPredictedContextMetricsManager prepareAndSubmitDailyInferenceEventMetrics:]
+ -[RTPredictedContextMetricsManager prepareAndSubmitPredictionEventMetrics:yesterdayVisits:]
+ -[RTPredictedContextMetricsManager prepareAndSubmitTrainingEventMetrics:]
+ -[RTPredictedContextMetricsManager prepareAndSubmitTruthEventMetrics:yesterdayVisits:yesterdayPredictions:]
+ -[RTPredictedContextMetricsManager prepareDailyInferenceEventMetrics:]
+ -[RTPredictedContextMetricsManager preparePredictionEventMetric:correctPrediction:matchingVisit:]
+ -[RTPredictedContextMetricsManager prepareTrainingEventMetric:]
+ -[RTPredictedContextMetricsManager prepareTruthEventMetric:predictability:truePositiveCount:highestProbability:frequentLoi:leadTime:]
+ -[RTPredictedContextMetricsManager queue]
+ -[RTPredictedContextMetricsManager setQueue:]
+ -[RTPredictedContextMetricsManager setVisitConsolidator:]
+ -[RTPredictedContextMetricsManager setup]
+ -[RTPredictedContextMetricsManager submitFeatureExtractorMetrics:]
+ -[RTPredictedContextMetricsManager visitConsolidator]
+ -[RTPredictedContextStore _fetchPredictedContextAndRequestDateWithOptions:handler:]
+ -[RTPredictedContextStore fetchPredictedContextAndRequestDateWithOptions:handler:]
+ -[RTTripClusterManager maximumInterTripSegmentDistanceAllowedForCompoundRoute]
+ -[RTTripClusterProcessorOptions setStartEndRoadCountBufferZonePercentage:]
+ -[RTTripClusterProcessorOptions startEndRoadCountBufferZonePercentage]
+ -[RTTripSegmentProvider _isValidTransitionToProcess:]
+ -[RTTripSegmentProvider _logDeferTripSegmentAndClusterProcessingDate:]
+ -[RTTripSegmentProvider _processSingleOrCompoundedVisitTransition:]
+ -[RTTripSegmentProvider buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:]
+ -[RTTripSegmentProvider buildTripSegmentsFromTripSegmentFeaturesList:startVisitLocation:stopVisitLocation:transitionStartStopLocations:]
+ -[RTTripSegmentProvider chunkLocationsCloseEnoughToCompound:stitchDateEndInterval:]
+ -[RTTripSegmentProvider getStoredLocationWithOptions:]
+ -[RTTripSegmentProvider idOfCurrentlyProcessingChunk]
+ -[RTTripSegmentProvider setIdOfCurrentlyProcessingChunk:]
+ -[RTTripSegmentTransitionPreprocessor _addCompoundedVisitInterval:]
+ -[RTTripSegmentTransitionPreprocessor _areTwoVisitsSame:firstVisitLocation:secondLearnedLOI:secondVisitLocation:]
+ -[RTTripSegmentTransitionPreprocessor _isVisitCompoundingLeadingToLoopbackTransition:currentVisitStatus:]
+ -[RTTripSegmentTransitionPreprocessor _visitCompoundingLoopbackCheckDurationSec]
+ -[RTTripSegmentTransitionPreprocessor _visitCompoundingShortVisitDurationSec]
+ -[RTTripSegmentTransitionPreprocessor compoundedVisitIntervals]
+ -[RTTripSegmentTransitionPreprocessor fetchLearnedLocationOfInterestForVisitIdentifier:outLearnedVisitLocation:]
+ -[RTTripSegmentTransitionPreprocessor isVisitCompoundingEnabled]
+ -[RTTripSegmentTransitionPreprocessor maxAdjacentVisitsToCompound]
+ -[RTTripSegmentTransitionPreprocessor tryCompoundingVisits]
+ -[RTUserCurationManager createAndStoreCurationWithEntryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:handler:]
+ -[RTUserCurationStore _fetchStoredUserCurationWithIdentifier:handler:]
+ -[RTUserCurationStore fetchStoredUserCurationWithIdentifier:handler:]
+ -[RTVisitConsolidator _fetchRedactedStoredVisitsWithOptions:redactedVisitsHandler:]
+ -[RTVisitConsolidator _onDailyMetricsNotification:]
+ -[RTVisitConsolidator onDailyMetricsNotification:]
+ -[RTVisitConsolidatorResult .cxx_destruct]
+ -[RTVisitConsolidatorResult initWithVisits:redactionDetails:]
+ -[RTVisitConsolidatorResult redactionDetails]
+ -[RTVisitConsolidatorResult visits]
+ -[RTVisitRedactionDetails .cxx_destruct]
+ -[RTVisitRedactionDetails description]
+ -[RTVisitRedactionDetails init]
+ -[RTVisitRedactionDetails redactedVisitCount]
+ -[RTVisitRedactionDetails setVisitsRedactedForAge:]
+ -[RTVisitRedactionDetails setVisitsRedactedForAuthorizedLocation:]
+ -[RTVisitRedactionDetails setVisitsRedactedForCategory:]
+ -[RTVisitRedactionDetails setVisitsRedactedForConfidence:]
+ -[RTVisitRedactionDetails setVisitsRedactedForPlaceType:]
+ -[RTVisitRedactionDetails setVisitsRedactedForRegion:]
+ -[RTVisitRedactionDetails visitsRedactedForAge]
+ -[RTVisitRedactionDetails visitsRedactedForAuthorizedLocation]
+ -[RTVisitRedactionDetails visitsRedactedForCategory]
+ -[RTVisitRedactionDetails visitsRedactedForConfidence]
+ -[RTVisitRedactionDetails visitsRedactedForPlaceType]
+ -[RTVisitRedactionDetails visitsRedactedForRegion]
+ -[RTVisitRedactionMetric .cxx_destruct]
+ -[RTVisitRedactionMetric init]
+ -[RTVisitRedactionMetric metricDictionary]
+ -[RTVisitRedactionMetric redactedForAuthorizedLocation]
+ -[RTVisitRedactionMetric redactedForCategory]
+ -[RTVisitRedactionMetric redactedForConfidence]
+ -[RTVisitRedactionMetric redactedForPlaceType]
+ -[RTVisitRedactionMetric redactedForRegion]
+ -[RTVisitRedactionMetric redactionProportion]
+ -[RTVisitRedactionMetric setRedactedForAuthorizedLocation:]
+ -[RTVisitRedactionMetric setRedactedForCategory:]
+ -[RTVisitRedactionMetric setRedactedForConfidence:]
+ -[RTVisitRedactionMetric setRedactedForPlaceType:]
+ -[RTVisitRedactionMetric setRedactedForRegion:]
+ -[RTVisitRedactionMetric setRedactionProportion:]
+ -[RTVisitRedactionMetric setVisitsConsideredCount:]
+ -[RTVisitRedactionMetric visitsConsideredCount]
+ -[SMDaemonClient checkIMessageAccountEnabledWithHandler:]
+ GCC_except_table205
+ GCC_except_table223
+ GCC_except_table234
+ GCC_except_table236
+ GCC_except_table248
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table257
+ GCC_except_table263
+ GCC_except_table274
+ GCC_except_table277
+ GCC_except_table284
+ GCC_except_table289
+ GCC_except_table291
+ GCC_except_table293
+ GCC_except_table295
+ GCC_except_table301
+ GCC_except_table306
+ GCC_except_table338
+ GCC_except_table416
+ GCC_except_table424
+ GCC_except_table86
+ _CFRetain
+ _CFStringCreateCopy
+ _GEOPOICategoryBeach
+ _GEOPOICategoryFoodMarket
+ _GEOPOICategoryLandmark
+ _GEOPOICategoryStadium
+ _OBJC_CLASS_$_RTBlueSkyDailyMetrics
+ _OBJC_CLASS_$_RTUserCurationMetrics
+ _OBJC_CLASS_$_RTVisitConsolidatorResult
+ _OBJC_CLASS_$_RTVisitRedactionDetails
+ _OBJC_CLASS_$_RTVisitRedactionMetric
+ _OBJC_CLASS_$_RTVisitRedactionUtilities
+ _OBJC_IVAR_$_RTBlueSkyDailyMetrics._defaultsManager
+ _OBJC_IVAR_$_RTBlueSkyDailyMetrics._metrics
+ _OBJC_IVAR_$_RTPersistenceDriver._currentAccountStatus
+ _OBJC_IVAR_$_RTPredictedContextMetricsManager._queue
+ _OBJC_IVAR_$_RTPredictedContextMetricsManager._visitConsolidator
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._startEndRoadCountBufferZonePercentage
+ _OBJC_IVAR_$_RTTripRegionChecker._shouldDisableProcessingInChina
+ _OBJC_IVAR_$_RTTripSegmentProvider._idOfCurrentlyProcessingChunk
+ _OBJC_IVAR_$_RTTripSegmentTransitionPreprocessor._compoundedVisitIntervals
+ _OBJC_IVAR_$_RTVisitConsolidatorResult._redactionDetails
+ _OBJC_IVAR_$_RTVisitConsolidatorResult._visits
+ _OBJC_IVAR_$_RTVisitRedactionDetails._visitsRedactedForAge
+ _OBJC_IVAR_$_RTVisitRedactionDetails._visitsRedactedForAuthorizedLocation
+ _OBJC_IVAR_$_RTVisitRedactionDetails._visitsRedactedForCategory
+ _OBJC_IVAR_$_RTVisitRedactionDetails._visitsRedactedForConfidence
+ _OBJC_IVAR_$_RTVisitRedactionDetails._visitsRedactedForPlaceType
+ _OBJC_IVAR_$_RTVisitRedactionDetails._visitsRedactedForRegion
+ _OBJC_IVAR_$_RTVisitRedactionMetric._countBins
+ _OBJC_IVAR_$_RTVisitRedactionMetric._proportionBins
+ _OBJC_IVAR_$_RTVisitRedactionMetric._redactedForAuthorizedLocation
+ _OBJC_IVAR_$_RTVisitRedactionMetric._redactedForCategory
+ _OBJC_IVAR_$_RTVisitRedactionMetric._redactedForConfidence
+ _OBJC_IVAR_$_RTVisitRedactionMetric._redactedForPlaceType
+ _OBJC_IVAR_$_RTVisitRedactionMetric._redactedForRegion
+ _OBJC_IVAR_$_RTVisitRedactionMetric._redactionProportion
+ _OBJC_IVAR_$_RTVisitRedactionMetric._visitsConsideredCount
+ _OBJC_METACLASS_$_RTBlueSkyDailyMetrics
+ _OBJC_METACLASS_$_RTUserCurationMetrics
+ _OBJC_METACLASS_$_RTVisitConsolidatorResult
+ _OBJC_METACLASS_$_RTVisitRedactionDetails
+ _OBJC_METACLASS_$_RTVisitRedactionMetric
+ _OBJC_METACLASS_$_RTVisitRedactionUtilities
+ _RTAnalyticsEventBlueSkySendDaily
+ _RTAnalyticsEventPredictedContextFeatureExtractorEvent
+ _RTAnalyticsEventPredictedContextInferenceDaily
+ _RTAnalyticsEventPredictedContextTruthEvent
+ _RTAnalyticsEventUserCurationCount
+ _RTAnalyticsEventUserCurationSubmission
+ _RTAnalyticsEventVisitRedactionDaily
+ __OBJC_$_CLASS_METHODS_RTLearnedLocationReconcilerPerDevice
+ __OBJC_$_CLASS_METHODS_RTUserCurationMetrics
+ __OBJC_$_CLASS_METHODS_RTVisitRedactionUtilities
+ __OBJC_$_INSTANCE_METHODS_RTBlueSkyDailyMetrics
+ __OBJC_$_INSTANCE_METHODS_RTVisitConsolidatorResult
+ __OBJC_$_INSTANCE_METHODS_RTVisitRedactionDetails
+ __OBJC_$_INSTANCE_METHODS_RTVisitRedactionMetric
+ __OBJC_$_INSTANCE_VARIABLES_RTBlueSkyDailyMetrics
+ __OBJC_$_INSTANCE_VARIABLES_RTVisitConsolidatorResult
+ __OBJC_$_INSTANCE_VARIABLES_RTVisitRedactionDetails
+ __OBJC_$_INSTANCE_VARIABLES_RTVisitRedactionMetric
+ __OBJC_$_PROP_LIST_RTBlueSkyDailyMetrics
+ __OBJC_$_PROP_LIST_RTUserCurationMetrics
+ __OBJC_$_PROP_LIST_RTVisitConsolidatorResult
+ __OBJC_$_PROP_LIST_RTVisitRedactionDetails
+ __OBJC_$_PROP_LIST_RTVisitRedactionMetric
+ __OBJC_CLASS_PROTOCOLS_$_RTUserCurationMetrics
+ __OBJC_CLASS_RO_$_RTBlueSkyDailyMetrics
+ __OBJC_CLASS_RO_$_RTUserCurationMetrics
+ __OBJC_CLASS_RO_$_RTVisitConsolidatorResult
+ __OBJC_CLASS_RO_$_RTVisitRedactionDetails
+ __OBJC_CLASS_RO_$_RTVisitRedactionMetric
+ __OBJC_CLASS_RO_$_RTVisitRedactionUtilities
+ __OBJC_METACLASS_RO_$_RTBlueSkyDailyMetrics
+ __OBJC_METACLASS_RO_$_RTUserCurationMetrics
+ __OBJC_METACLASS_RO_$_RTVisitConsolidatorResult
+ __OBJC_METACLASS_RO_$_RTVisitRedactionDetails
+ __OBJC_METACLASS_RO_$_RTVisitRedactionMetric
+ __OBJC_METACLASS_RO_$_RTVisitRedactionUtilities
+ ___101-[RTBluePOIMonitor _updateLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:error:]_block_invoke_3
+ ___101-[RTLearnedLocationStore _fetchCountOfVisitsToLocationOfInterestWithIdentifier:dateInterval:handler:]_block_invoke.285
+ ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke.88
+ ___107-[RTPredictedContextMetricsManager prepareAndSubmitTruthEventMetrics:yesterdayVisits:yesterdayPredictions:]_block_invoke
+ ___110-[RTPersistenceDriver _setupPersistenceAfterConfigurationChange:cloudSyncAuthorization:accountStatus:account:]_block_invoke
+ ___110-[RTTripSegmentProvider buildTinySegmentArrayForTransitionWithIndex:withinDateInterval:fromActivity:uuidType:]_block_invoke.359
+ ___112-[RTTripSegmentTransitionPreprocessor fetchLearnedLocationOfInterestForVisitIdentifier:outLearnedVisitLocation:]_block_invoke
+ ___112-[RTTripSegmentTransitionPreprocessor fetchLearnedLocationOfInterestForVisitIdentifier:outLearnedVisitLocation:]_block_invoke.188
+ ___121-[RTUserCurationManager createAndStoreCurationWithEntryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:handler:]_block_invoke
+ ___121-[RTUserCurationManager createAndStoreCurationWithEntryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:handler:]_block_invoke.18
+ ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke
+ ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke_3
+ ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.72
+ ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.74
+ ___144-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:includePlaceholders:includeVisits:includeTransitions:handler:]_block_invoke.343
+ ___159-[RTTripSegmentProvider buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:]_block_invoke
+ ___159-[RTTripSegmentProvider buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:]_block_invoke.398
+ ___159-[RTTripSegmentProvider buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:]_block_invoke.401
+ ___159-[RTTripSegmentProvider buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:]_block_invoke.402
+ ___214-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:]_block_invoke.289
+ ___214-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:]_block_invoke_2
+ ___28-[RTHealthKitManager _setup]_block_invoke.624
+ ___36-[RTBlueSkyDailyMetrics description]_block_invoke
+ ___41-[RTPredictedContextMetricsManager setup]_block_invoke
+ ___43-[RTPredictedContextManager _storeRequest:]_block_invoke.472
+ ___47-[RTLearnedLocationStore _removePlace:handler:]_block_invoke.430
+ ___47-[SMClientListener _setupConnection:forClient:]_block_invoke.279
+ ___48-[RTFeatureExtractor _getHomeKitHomesWithError:]_block_invoke.434
+ ___50+[RTVisit(RTExtensions) visits:withLoiIdentifier:]_block_invoke
+ ___50-[RTVisitConsolidator onDailyMetricsNotification:]_block_invoke
+ ___51+[RTVisit(RTExtensions) visitsWithExit:beforeDate:]_block_invoke
+ ___51-[RTLearnedLocationEngine _getDailyTrainingMetrics]_block_invoke.814
+ ___51-[RTLearnedLocationEngine _teardownTrainingMetrics]_block_invoke.870
+ ___51-[RTVisitConsolidator _onDailyMetricsNotification:]_block_invoke
+ ___52-[RTLearnedLocationEngine _createLOIForPlace:error:]_block_invoke
+ ___52-[RTLearnedLocationEngine _createLOIForPlace:error:]_block_invoke.896
+ ___53+[RTVisit(RTExtensions) visitsWithExit:dateInterval:]_block_invoke
+ ___53-[RTCompanionLinkManager onDailyMetricsNotification:]_block_invoke
+ ___53-[RTLearnedLocationStore _fetchLastVisitWithHandler:]_block_invoke.273
+ ___53-[RTLearnedLocationStore _fetchPlaceOfVisit:handler:]_block_invoke.189
+ ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.465
+ ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.468
+ ___53-[RTTripSegmentProvider _isValidTransitionToProcess:]_block_invoke
+ ___54-[RTClusterLearnedRouteMetrics submitToCoreAnalytics:]_block_invoke.902
+ ___54-[RTClusterLearnedRouteMetrics submitToCoreAnalytics:]_block_invoke_2.903
+ ___54-[RTLearnedLocationStore _fetchVisitsToPlace:handler:]_block_invoke.261
+ ___54-[RTTripSegmentProvider getStoredLocationWithOptions:]_block_invoke
+ ___55-[RTFeatureExtractor _getLocationsOfInterestWithError:]_block_invoke.418
+ ___55-[RTLearnedLocationEngine _retrainVisitsWithoutPlaces:]_block_invoke.872
+ ___55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.557
+ ___55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.418
+ ___55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.419
+ ___56-[RTLearnedLocationStore fetchCurrentDeviceWithHandler:]_block_invoke
+ ___56-[RTPredictedContextManager setMonitorPredictedContext:]_block_invoke
+ ___56-[RTPredictedContextManager setMonitorPredictedContext:]_block_invoke_2
+ ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.374
+ ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.375
+ ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.383
+ ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.388
+ ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.390
+ ___57-[RTLearnedLocationStore _fetchCurrentDeviceWithHandler:]_block_invoke
+ ___57-[RTLearnedLocationStore _fetchCurrentDeviceWithHandler:]_block_invoke_2
+ ___57-[SMDaemonClient checkIMessageAccountEnabledWithHandler:]_block_invoke
+ ___57-[SMDaemonClient checkIMessageAccountEnabledWithHandler:]_block_invoke_2
+ ___58-[RTAuthorizedLocationManager onVisitMonitorNotification:]_block_invoke.159
+ ___58-[RTFeatureExtractor _getVisitsWithDateInterval:outError:]_block_invoke.414
+ ___58-[RTPredictedContextManager _evaluateTrainErrorForResult:]_block_invoke
+ ___58-[RTPredictedContextManager _evaluateTrainErrorForResult:]_block_invoke.158
+ ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.832
+ ___59-[RTLearnedLocationStore _fetchVisitIdentifiersIn:handler:]_block_invoke.293
+ ___59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.587
+ ___59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.583
+ ___60-[RTLearnedLocationEngine _findOrCreateLOIForMapItem:error:]_block_invoke
+ ___60-[RTLearnedLocationStore _fetchPlacesWithPredicate:handler:]_block_invoke.184
+ ___60-[RTLearnedLocationStore _fetchVisitWithIdentifier:handler:]_block_invoke.242
+ ___60-[RTVisitConsolidator fetchStoredVisitsWithOptions:handler:]_block_invoke_2
+ ___61-[RTLearnedLocationStore fetchVisitsOverlappingDate:handler:]_block_invoke
+ ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.39
+ ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.40
+ ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.41
+ ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.46
+ ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.47
+ ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.52
+ ___62-[RTLearnedLocationStore _fetchPlacesWithIdentifiers:handler:]_block_invoke.244
+ ___62-[RTLearnedLocationStore _fetchPlacesWithIdentifiers:handler:]_block_invoke.247
+ ___63-[RTFeatureExtractor _getTransitionsWithDateInterval:outError:]_block_invoke.416
+ ___63-[RTPredictedContextMetricsManager onDailyMetricsNotification:]_block_invoke
+ ___64-[RTAuthorizedLocationManager collectMetricDataForTest:handler:]_block_invoke.162
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.283
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.286
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.287
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.289
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.292
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.295
+ ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.298
+ ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke
+ ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.454
+ ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.455
+ ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.456
+ ___65-[RTLearnedLocationStore _fetchPlacesWithType:predicate:handler:]_block_invoke.188
+ ___66+[RTPredictedContextMetricsManager isCorrectTruth:forPredictions:]_block_invoke
+ ___66-[RTFeatureExtractor _getCalendarEventsWithDateInterval:outError:]_block_invoke.423
+ ___66-[RTLearnedLocationStore _fetchMapItemWithMuid:predicate:handler:]_block_invoke.409
+ ___66-[RTLearnedLocationStore _removeRecordsExpiredBeforeDate:handler:]_block_invoke.522
+ ___67-[RTLearnedLocationEngine _applyUserCurationsSubmittedSince:error:]_block_invoke.917
+ ___67-[RTLearnedLocationStore _fetchPlaceWithMapItemIdentifier:handler:]_block_invoke.238
+ ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.112
+ ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke_2.110
+ ___68-[RTFeatureExtractor _getMapsViewedPlacesWithDateInterval:outError:]_block_invoke.428
+ ___68-[RTFeatureExtractor _getMotionActivitiesWithDateInterval:outError:]_block_invoke.430
+ ___68-[RTLearnedLocationStore _fetchLocationOfInterestWithPlace:handler:]_block_invoke.376
+ ___68-[RTLearnedLocationStore _fetchPlacesWithMapItem:predicate:handler:]_block_invoke.220
+ ___68-[RTMotionActivityManager_CoreMotion initWithPlatform:vehicleStore:]_block_invoke_3
+ ___68-[RTPredictedContextMetricsManager getVisitsForInterval:completion:]_block_invoke
+ ___68-[RTPredictedContextMetricsManager getVisitsForInterval:completion:]_block_invoke_2
+ ___68-[RTUserCurationStore _fetchStoredUserCurationsWithOptions:handler:]_block_invoke.36
+ ___69-[RTFeatureExtractor _getLocationHistoriesWithDateInterval:outError:]_block_invoke.421
+ ___69-[RTLearnedLocationEngine _getUUIDSetOfLocationsOfInterestWithError:]_block_invoke.895
+ ___69-[RTPredictedContextManager _rescheduleActivityTrainWithTrainPolicy:]_block_invoke.159
+ ___69-[RTTripSegmentTransitionPreprocessor appendTransitionToCurrentVisit]_block_invoke.196
+ ___69-[RTTripSegmentTransitionPreprocessor appendTransitionToCurrentVisit]_block_invoke.197
+ ___69-[RTUserCurationStore fetchStoredUserCurationWithIdentifier:handler:]_block_invoke
+ ___70-[RTAuthorizedLocationManager _runEraseInstallDatabaseInitialization:]_block_invoke.154
+ ___70-[RTLearnedLocationStore _fetchLocationOfInterestWithMapItem:handler:]_block_invoke.372
+ ___70-[RTLearnedLocationStore _fetchVisitsOverlappingDateInterval:handler:]_block_invoke.272
+ ___70-[RTPredictedContextMetricsManager getRequestsForInterval:completion:]_block_invoke
+ ___70-[RTPredictedContextMetricsManager getRequestsForInterval:completion:]_block_invoke_2
+ ___70-[RTUserCurationStore _fetchStoredUserCurationWithIdentifier:handler:]_block_invoke
+ ___70-[RTUserCurationStore _fetchStoredUserCurationWithIdentifier:handler:]_block_invoke.13
+ ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke.857
+ ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke_2.858
+ ___71-[RTLearnedLocationStore _fetchDevicesNotFromCurrentDeviceWithHandler:]_block_invoke.175
+ ___71-[RTLearnedLocationStore _fetchLastVisitToPlaceWithIdentifier:handler:]_block_invoke.277
+ ___71-[RTPredictedContextStore performPurgeOfType:referenceDate:completion:]_block_invoke.31
+ ___72+[RTPredictedContextMetricsManager getHighProbabilityPredictedContexts:]_block_invoke
+ ___72-[RTTripSegmentProvider addToTransitionLocationsBuffer:forDateInterval:]_block_invoke.362
+ ___73-[RTLearnedLocationStore _fetchLocationOfInterestVisitedLastWithHandler:]_block_invoke.367
+ ___73-[RTLearnedLocationStore _fetchLocationOfInterestWithIdentifier:handler:]_block_invoke.368
+ ___73-[RTLearnedLocationStore _fetchLocationsOfInterestWithPlaceType:handler:]_block_invoke.327
+ ___73-[RTPredictedContextMetricsManager getPredictionsForInterval:completion:]_block_invoke
+ ___73-[RTPredictedContextMetricsManager getPredictionsForInterval:completion:]_block_invoke_2
+ ___74-[RTLearnedLocationStore _fetchInferredMapItemForVisitIdentifier:handler:]_block_invoke.365
+ ___74-[RTLearnedLocationStore _fetchLocationOfInterestVisitedFirstWithHandler:]_block_invoke.366
+ ___75-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:handler:]_block_invoke.278
+ ___76-[RTLearnedLocationEngine _appendVisitsToLocationsOfInterestModelWithError:]_block_invoke.874
+ ___76-[RTLearnedLocationStore _fetchStoredMapItemsWithMapItem:predicate:handler:]_block_invoke.215
+ ___76-[RTLearnedLocationStore _fetchTransitionsBetweenStartDate:endDate:handler:]_block_invoke.307
+ ___76-[RTLearnedLocationStore _fetchVisitsWithPredicate:ascending:limit:handler:]_block_invoke.254
+ ___77+[RTLearnedLocationReconcilerPerDevice sortReconciledVisitsByMapItemQuality:]_block_invoke
+ ___77+[RTLearnedLocationReconcilerPerDevice sortReconciledVisitsByMapItemQuality:]_block_invoke.75
+ ___77+[RTLearnedLocationReconcilerPerDevice sortReconciledVisitsByMapItemQuality:]_block_invoke_2
+ ___77+[RTLearnedLocationReconcilerPerDevice sortReconciledVisitsByMapItemQuality:]_block_invoke_2.78
+ ___77+[RTLearnedLocationReconcilerPerDevice sortReconciledVisitsByMapItemQuality:]_block_invoke_3
+ ___77+[RTLearnedLocationReconcilerPerDevice sortReconciledVisitsByMapItemQuality:]_block_invoke_4
+ ___77-[RTFeatureExtractor _getMapsHistoricalNavigationsWithDateInterval:outError:]_block_invoke.426
+ ___77-[RTPredictedContextStore _fetchPredictedContextRequestsWithOptions:handler:]_block_invoke.23
+ ___77-[SMTriggerDestination _updateInitiatorStatusDestinationBoundWithCompletion:]_block_invoke.216
+ ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke_3
+ ___79-[RTLearnedLocationEngine _findVisitsAssociatedWithCurrentPlaceCuration:error:]_block_invoke
+ ___80-[RTLearnedLocationStore _fetchPlacesWithinDistance:location:predicate:handler:]_block_invoke.231
+ ___80-[RTLearnedPlaceTypeInferencePlaceStats visitsPredatingCurrentDeviceFromVisits:]_block_invoke
+ ___81-[RTAuthorizedLocationManager _fetchAuthorizedLocationExtendedStatusWithMetrics:]_block_invoke.148
+ ___82-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]_block_invoke
+ ___82-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]_block_invoke.906
+ ___82-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]_block_invoke.907
+ ___82-[RTPredictedContextStore fetchPredictedContextAndRequestDateWithOptions:handler:]_block_invoke
+ ___83-[RTLearnedLocationEngine _recoverKnownPlaceTypesWithPlaceTypeClassifier:outError:]_block_invoke.813
+ ___83-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:endDate:handler:]_block_invoke.289
+ ___83-[RTLearnedLocationStore _fetchLocationsOfInterestWithinDistance:location:handler:]_block_invoke.323
+ ___83-[RTPredictedContextStore _fetchPredictedContextAndRequestDateWithOptions:handler:]_block_invoke
+ ___83-[RTPredictedContextStore _fetchPredictedContextAndRequestDateWithOptions:handler:]_block_invoke.25
+ ___83-[RTVisitConsolidator _fetchRedactedStoredVisitsWithOptions:redactedVisitsHandler:]_block_invoke
+ ___83-[RTVisitConsolidator _fetchRedactedStoredVisitsWithOptions:redactedVisitsHandler:]_block_invoke.31
+ ___83-[RTVisitConsolidator _fetchRedactedStoredVisitsWithOptions:redactedVisitsHandler:]_block_invoke.33
+ ___84+[RTUserCurationMetrics collectUserCurationCountMetricsWithUserCurationStore:error:]_block_invoke
+ ___85-[RTTripSegmentTransitionPreprocessor fetchEndpointCLLocationForTransition:atOrigin:]_block_invoke.211
+ ___86-[RTLearnedLocationStore _fetchVisitsWithIncompletePlacesForCurrentDeviceWithHandler:]_block_invoke.402
+ ___87+[RTUserCurationMO managedObjectWithUserCuration:managedObject:inManagedObjectContext:]_block_invoke
+ ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke.911
+ ___90-[RTCompanionLinkManager initWithCompanionLinkClient:dailyBlueSkyMetrics:defaultsManager:]_block_invoke
+ ___90-[RTCompanionLinkManager initWithCompanionLinkClient:dailyBlueSkyMetrics:defaultsManager:]_block_invoke.30
+ ___90-[RTCompanionLinkManager initWithCompanionLinkClient:dailyBlueSkyMetrics:defaultsManager:]_block_invoke.31
+ ___90-[RTCompanionLinkManager initWithCompanionLinkClient:dailyBlueSkyMetrics:defaultsManager:]_block_invoke.39
+ ___90-[RTMotionActivityManager_CoreMotion _fetchMotionActivitiesFromStartDate:endDate:handler:]_block_invoke.129
+ ___90-[RTMotionActivityManager_CoreMotion _fetchMotionActivitiesFromStartDate:endDate:handler:]_block_invoke.132
+ ___91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.558
+ ___91-[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke.179
+ ___91-[RTPredictedContextMetricsManager prepareAndSubmitPredictionEventMetrics:yesterdayVisits:]_block_invoke
+ ___94-[RTLearnedLocationStore _fetchLocationOfInterestTransitionsBetweenStartDate:endDate:handler:]_block_invoke.389
+ ___97-[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngineWithPlaceStats:dateInterval:]_block_invoke.414
+ ___97-[RTPredictedContextMetricsManager preparePredictionEventMetric:correctPrediction:matchingVisit:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48r56r64r72r80r88r_e5_v8?0lr48l8r56l8r64l8r72l8r80l8r88l8s32l8s40l8
+ ___block_descriptor_120_e8_32s40s48bs56r64r72r80r88r96r_e5_v8?0lr56l8r64l8r72l8r80l8r88l8r96l8s48l8s32l8s40l8
+ ___block_descriptor_122_e8_32s40s48bs56r64r72r80r88r96r_e5_v8?0lr56l8r64l8s32l8r72l8s40l8r80l8r88l8r96l8s48l8
+ ___block_descriptor_32_e47_v24?0"RTVisitConsolidatorResult"8"NSError"16l
+ ___block_descriptor_40_e8_32bs_e47_v24?0"RTVisitConsolidatorResult"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e24_v32?0"NSError"8Q16^B24lr32l8
+ ___block_descriptor_40_e8_32s_e11_B16?0i8i12ls32l8
+ ___block_descriptor_40_e8_32s_e32_v32?0"NSDate"8"NSArray"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40w_e39_v24?0"NSDictionary"8"NSDictionary"16lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e24_v32?0"NSError"8Q16^B24ls32l8
+ ___block_descriptor_56_e8_32s40bs_e20_v24?0Q8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e32_v32?0"NSDate"8"NSArray"16^B24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r_e20_v24?0Q8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s_e24_v32?0"RTVisit"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e38_v32?0"RTTripSegmentFeatures"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48r56r_e34_v24?0"NSDictionary"8"NSError"16ls32l8r48l8r56l8s40l8
+ ___block_descriptor_72_e8_32s40s48r56r_e49_v24?0"RTLearnedLocationOfInterest"8"NSError"16ls32l8r48l8s40l8r56l8
+ ___block_descriptor_72_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e39_v24?0"RTInferredMapItem"8"NSError"16lr56l8s32l8s40l8r64l8s48l8
+ ___block_descriptor_80_e8_32s40r48r56r_e32_v32?0"NSDate"8"NSArray"16^B24ls32l8r40l8r48l8r56l8
+ ___block_descriptor_80_e8_32s40s48s56r64r_e36_v24?0"RTLearnedVisit"8"NSError"16ls32l8s40l8r56l8s48l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_86_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8r72l8
+ ___block_descriptor_88_e8_32s40bs48r56r64r72r_e5_v8?0lr48l8r56l8s40l8r64l8r72l8s32l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8r64l8s48l8s56l8r72l8
+ ___block_descriptor_88_e8_32s40s48s56s64r72r_e36_v24?0"RTUserCuration"8"NSError"16lr64l8s32l8s40l8s48l8s56l8r72l8
+ ___block_literal_global.1382
+ ___block_literal_global.141
+ ___block_literal_global.149
+ ___block_literal_global.185
+ ___block_literal_global.214
+ ___block_literal_global.330
+ ___block_literal_global.356
+ ___block_literal_global.395
+ ___block_literal_global.422
+ ___block_literal_global.424
+ ___block_literal_global.449
+ ___block_literal_global.450
+ ___block_literal_global.578
+ ___block_literal_global.646
+ ___block_literal_global.66
+ ___block_literal_global.698
+ ___block_literal_global.904
+ ___block_literal_global.91
+ ___block_literal_global.915
+ _block_copy_helper.34
+ _block_descriptor.36
+ _block_destroy_helper.35
+ _kRTBlueSkyMetricKeyNumberOfQualifiedPlaceInferences
+ _kRTBlueSkyMetricKeyNumberOfQualifiedPlaceInferencesSent
+ _kRTBlueSkyMetricKeyNumberOfQualifiedVisits
+ _kRTBlueSkyMetricKeyNumberOfQualifiedVisitsOverLimit
+ _kRTBlueSkyMetricKeyNumberOfQualifiedVisitsSent
+ _kRTBlueSkyMetricKeyNumberOfSyncs10SecWait
+ _kRTBlueSkyMetricKeyNumberOfSyncs1MinWait
+ _kRTBlueSkyMetricKeyNumberOfSyncs20SecWait
+ _kRTBlueSkyMetricKeyNumberOfSyncs2MinWait
+ _kRTBlueSkyMetricKeyNumberOfSyncs30SecWait
+ _kRTBlueSkyMetricKeyNumberOfSyncs5MinPlusWait
+ _kRTBlueSkyMetricKeyNumberOfSyncs5MinWait
+ _kRTBlueSkyMetricKeyNumberOfSyncsNoWait
+ _kRTCompanionLinkManagerEventUpdate
+ _kRTCompanionLinkManagerKeyPayload
+ _kRTCompanionLinkManagerKeyPayloadType
+ _kRTFingerprintStoreDefaultAccessPointsFetchLimit
+ _kRTPredictedContextMetricsKeyCalendarEventsCount
+ _kRTPredictedContextMetricsKeyCalendarEventsLatency
+ _kRTPredictedContextMetricsKeyCalendarEventsSuccess
+ _kRTPredictedContextMetricsKeyCorrectPrediction
+ _kRTPredictedContextMetricsKeyCorrectPredictionCount
+ _kRTPredictedContextMetricsKeyCorrectTruth
+ _kRTPredictedContextMetricsKeyDailyInferenceCount
+ _kRTPredictedContextMetricsKeyDailyInferenceLatency
+ _kRTPredictedContextMetricsKeyDailyInferenceMemoryUsage
+ _kRTPredictedContextMetricsKeyDailyInferenceReasonClientRegistrationCount
+ _kRTPredictedContextMetricsKeyDailyInferenceReasonDominantMotionCount
+ _kRTPredictedContextMetricsKeyDailyInferenceReasonNavigationNotificationCount
+ _kRTPredictedContextMetricsKeyDailyInferenceReasonPeriodicTriggerCount
+ _kRTPredictedContextMetricsKeyDailyInferenceReasonSingleShotCount
+ _kRTPredictedContextMetricsKeyDailyInferenceReasonUnknownReasonCount
+ _kRTPredictedContextMetricsKeyDailyInferenceReasonVisitNotificationCount
+ _kRTPredictedContextMetricsKeyFeatureExtractorReason
+ _kRTPredictedContextMetricsKeyFrequentLoi
+ _kRTPredictedContextMetricsKeyHighestConfidence
+ _kRTPredictedContextMetricsKeyHomeKitHomesCount
+ _kRTPredictedContextMetricsKeyHomeKitHomesLatency
+ _kRTPredictedContextMetricsKeyHomeKitHomesSuccess
+ _kRTPredictedContextMetricsKeyLeadTime
+ _kRTPredictedContextMetricsKeyLocationLatency
+ _kRTPredictedContextMetricsKeyLocationOfInterestCount
+ _kRTPredictedContextMetricsKeyLocationOfInterestLatency
+ _kRTPredictedContextMetricsKeyLocationsCount
+ _kRTPredictedContextMetricsKeyLocationsOfInterestSuccess
+ _kRTPredictedContextMetricsKeyLocationsSuccess
+ _kRTPredictedContextMetricsKeyMapsActiveNavigationCount
+ _kRTPredictedContextMetricsKeyMapsActiveNavigationLatency
+ _kRTPredictedContextMetricsKeyMapsActiveNavigationSuccess
+ _kRTPredictedContextMetricsKeyMapsHistoricalNavigationCount
+ _kRTPredictedContextMetricsKeyMapsHistoricalNavigationLatency
+ _kRTPredictedContextMetricsKeyMapsHistoricalNavigationSuccess
+ _kRTPredictedContextMetricsKeyMapsViewedPlacesCount
+ _kRTPredictedContextMetricsKeyMapsViewedPlacesLatency
+ _kRTPredictedContextMetricsKeyMapsViewedPlacesSuccess
+ _kRTPredictedContextMetricsKeyMotionActivitiesCount
+ _kRTPredictedContextMetricsKeyMotionActivitiesLatency
+ _kRTPredictedContextMetricsKeyMotionActivitiesSuccess
+ _kRTPredictedContextMetricsKeyParkedCarCount
+ _kRTPredictedContextMetricsKeyParkedCarLatency
+ _kRTPredictedContextMetricsKeyParkedCarSuccess
+ _kRTPredictedContextMetricsKeyPredictability
+ _kRTPredictedContextMetricsKeyPredictionCount
+ _kRTPredictedContextMetricsKeyPropagatedLocationsCount
+ _kRTPredictedContextMetricsKeyPropagatedLocationsLatency
+ _kRTPredictedContextMetricsKeyPropagatedLocationsSuccess
+ _kRTPredictedContextMetricsKeyTotalLatency
+ _kRTPredictedContextMetricsKeyTrainingResultMask
+ _kRTPredictedContextMetricsKeyTransitionsCount
+ _kRTPredictedContextMetricsKeyTransitionsLatency
+ _kRTPredictedContextMetricsKeyTransitionsSuccess
+ _kRTPredictedContextMetricsKeyVisitCount
+ _kRTPredictedContextMetricsKeyVisitLatency
+ _kRTPredictedContextMetricsKeyVisitPlaceType
+ _kRTPredictedContextMetricsKeyVisitSuccess
+ _kRTPredictedContextMetricsKeyWorkoutsCount
+ _kRTPredictedContextMetricsKeyWorkoutsLatency
+ _kRTPredictedContextMetricsKeyWorkoutsSuccess
+ _objc_msgSend$_addCompoundedVisitInterval:
+ _objc_msgSend$_areTwoVisitsSame:firstVisitLocation:secondLearnedLOI:secondVisitLocation:
+ _objc_msgSend$_createLOIForPlace:error:
+ _objc_msgSend$_evaluateTrainErrorForResult:
+ _objc_msgSend$_extractFeatures:operationType:lookbackDurations:outError:
+ _objc_msgSend$_fetchCurrentDeviceWithHandler:
+ _objc_msgSend$_fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:
+ _objc_msgSend$_fetchPredictedContextAndRequestDateWithOptions:handler:
+ _objc_msgSend$_fetchRedactedStoredVisitsWithOptions:redactedVisitsHandler:
+ _objc_msgSend$_fetchStoredUserCurationWithIdentifier:handler:
+ _objc_msgSend$_fetchVisitsOverlappingDate:handler:
+ _objc_msgSend$_findOrCreateLOIForMapItem:error:
+ _objc_msgSend$_findVisitsAssociatedWithCurrentPlaceCuration:error:
+ _objc_msgSend$_findVisitsAssociatedWithHistoricalVisitCuration:error:
+ _objc_msgSend$_isValidTransitionToProcess:
+ _objc_msgSend$_isVisitCompoundingLeadingToLoopbackTransition:currentVisitStatus:
+ _objc_msgSend$_logDeferTripSegmentAndClusterProcessingDate:
+ _objc_msgSend$_onVisit:
+ _objc_msgSend$_processSingleOrCompoundedVisitTransition:
+ _objc_msgSend$_processTrainingResult:
+ _objc_msgSend$_setupPersistenceAfterConfigurationChange:cloudSyncAuthorization:accountStatus:account:
+ _objc_msgSend$_shouldAttemptSetupAccordingToAccountStatus:account:
+ _objc_msgSend$_shouldAttemptSetupAccordingToCloudSyncAuthorization:
+ _objc_msgSend$_submitDailyUserCurationMetrics
+ _objc_msgSend$_updatePendingSyncMetrics:
+ _objc_msgSend$_updateSyncCachedMetrics:
+ _objc_msgSend$_updateSyncMetrics:
+ _objc_msgSend$_updateSyncSuccessMetrics:waitRequired:
+ _objc_msgSend$_visitCompoundingLoopbackCheckDurationSec
+ _objc_msgSend$_visitCompoundingShortVisitDurationSec
+ _objc_msgSend$abbreviation
+ _objc_msgSend$accountStatusToString:
+ _objc_msgSend$addUserCuration:handler:
+ _objc_msgSend$buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:
+ _objc_msgSend$buildTripSegmentsFromTripSegmentFeaturesList:startVisitLocation:stopVisitLocation:transitionStartStopLocations:
+ _objc_msgSend$calculatePredictability:priorVisits:timeWindowHalfWidth:
+ _objc_msgSend$chunkLocationsCloseEnoughToCompound:stitchDateEndInterval:
+ _objc_msgSend$collectMetricsForSubmittedUserCuration:submissionResult:
+ _objc_msgSend$collectUserCurationCountMetricsWithUserCurationStore:error:
+ _objc_msgSend$compoundedVisitIntervals
+ _objc_msgSend$countKeyForFeature:
+ _objc_msgSend$createAndStoreCurationWithEntryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:handler:
+ _objc_msgSend$currentAccountStatus
+ _objc_msgSend$currentTimeCFAbsolute
+ _objc_msgSend$currentTimeZoneAbbreviation
+ _objc_msgSend$dailyBlueSkyMetrics
+ _objc_msgSend$fetchCurrentDeviceWithHandler:
+ _objc_msgSend$fetchLearnedLocationOfInterestForVisitIdentifier:outLearnedVisitLocation:
+ _objc_msgSend$fetchPredictedContextAndRequestDateWithOptions:handler:
+ _objc_msgSend$fetchStoredUserCurationWithIdentifier:handler:
+ _objc_msgSend$fetchVisitsOverlappingDate:handler:
+ _objc_msgSend$getAllContextsInOneArray:
+ _objc_msgSend$getEarliestDate:
+ _objc_msgSend$getFrequentLoiFromCount:
+ _objc_msgSend$getHighProbabilityPredictedContexts:
+ _objc_msgSend$getPredictedContextLocationFromDictionary:
+ _objc_msgSend$getPredictionsForInterval:completion:
+ _objc_msgSend$getRequestCountByInferenceTriggerReasonForRequests:
+ _objc_msgSend$getRequestsForInterval:completion:
+ _objc_msgSend$getStoredLocationWithOptions:
+ _objc_msgSend$getTotalInferenceLatencyForRequests:
+ _objc_msgSend$getTotalMemoryFootprintForRequests:
+ _objc_msgSend$getVisitsForInterval:completion:
+ _objc_msgSend$idOfCurrentlyProcessingChunk
+ _objc_msgSend$indexSet
+ _objc_msgSend$initForDefaultMetric
+ _objc_msgSend$initWithAscending:confidence:dateInterval:labelVisit:limit:sources:redact:
+ _objc_msgSend$initWithCompanionLinkClient:dailyBlueSkyMetrics:defaultsManager:
+ _objc_msgSend$initWithIdentifier:submissionDate:expirationDate:entryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:
+ _objc_msgSend$initWithLearnedLocationManager:visitManager:locationManager:eventManager:navigationManager:mapsSupportManager:motionActivityManager:vehicleLocationProvider:visitConsolidator:healthKitManager:homeKitManager:tripLocationPropagator:metricsManager:
+ _objc_msgSend$initWithManagedConfiguration:predictedContextStore:defaultsManager:visitConsolidator:
+ _objc_msgSend$initWithVisits:redactionDetails:
+ _objc_msgSend$isCorrectPrediction:forTruthVisits:matchingVisit:
+ _objc_msgSend$isCorrectTruth:forPredictions:
+ _objc_msgSend$isVisitCompoundingEnabled
+ _objc_msgSend$isWithinMidnightBoundary:targetDay:interval:
+ _objc_msgSend$killProcessingWithID:
+ _objc_msgSend$lastPlaceInferenceSyncAttemptDate
+ _objc_msgSend$lastVisitSyncAttemptDate
+ _objc_msgSend$latencyKeyForFeature:
+ _objc_msgSend$logFeatureExtractionForFeature:stimulationDate:featureArray:success:toDict:
+ _objc_msgSend$maxAdjacentVisitsToCompound
+ _objc_msgSend$maximumInterTripSegmentDistanceAllowedForCompoundRoute
+ _objc_msgSend$metricCodeForFeatureExtractorOperationType:
+ _objc_msgSend$metricDictionary
+ _objc_msgSend$mirroringManager:exceededHistoryType:count:limit:hasExceeded:
+ _objc_msgSend$obfuscatedVisitDateIntervalForEntryDate:previousObfuscatedVisitEntryDate:
+ _objc_msgSend$originalLabel
+ _objc_msgSend$predictedContextRequest
+ _objc_msgSend$prepareAndSubmitDailyInferenceEventMetrics:
+ _objc_msgSend$prepareAndSubmitPredictionEventMetrics:yesterdayVisits:
+ _objc_msgSend$prepareAndSubmitTrainingEventMetrics:
+ _objc_msgSend$prepareAndSubmitTruthEventMetrics:yesterdayVisits:yesterdayPredictions:
+ _objc_msgSend$prepareDailyInferenceEventMetrics:
+ _objc_msgSend$preparePredictionEventMetric:correctPrediction:matchingVisit:
+ _objc_msgSend$prepareTrainingEventMetric:
+ _objc_msgSend$prepareTruthEventMetric:predictability:truePositiveCount:highestProbability:frequentLoi:leadTime:
+ _objc_msgSend$redactedForAuthorizedLocation
+ _objc_msgSend$redactedForCategory
+ _objc_msgSend$redactedForConfidence
+ _objc_msgSend$redactedForPlaceType
+ _objc_msgSend$redactedForRegion
+ _objc_msgSend$redactedVisitCount
+ _objc_msgSend$redactionDetails
+ _objc_msgSend$removeAllIndexes
+ _objc_msgSend$replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:
+ _objc_msgSend$setCurrentAccountStatus:
+ _objc_msgSend$setCurrentTimeZoneAbbreviation:
+ _objc_msgSend$setIdOfCurrentlyProcessingChunk:
+ _objc_msgSend$setLastPlaceInferenceSyncAttemptDate:
+ _objc_msgSend$setLastVisitSyncAttemptDate:
+ _objc_msgSend$setOriginalLabel:
+ _objc_msgSend$setRedactedForAuthorizedLocation:
+ _objc_msgSend$setRedactedForCategory:
+ _objc_msgSend$setRedactedForConfidence:
+ _objc_msgSend$setRedactedForPlaceType:
+ _objc_msgSend$setRedactedForRegion:
+ _objc_msgSend$setRedactionProportion:
+ _objc_msgSend$setSelector:
+ _objc_msgSend$setShouldDeferTripSegmentAndClusterProcessing:
+ _objc_msgSend$setVisitsConsideredCount:
+ _objc_msgSend$setVisitsRedactedForAge:
+ _objc_msgSend$setVisitsRedactedForAuthorizedLocation:
+ _objc_msgSend$setVisitsRedactedForCategory:
+ _objc_msgSend$setVisitsRedactedForConfidence:
+ _objc_msgSend$setVisitsRedactedForPlaceType:
+ _objc_msgSend$setVisitsRedactedForRegion:
+ _objc_msgSend$shouldDeferTripSegmentAndClusterProcessing
+ _objc_msgSend$sortReconciledVisitsByMapItemQuality:
+ _objc_msgSend$startEndRoadCountBufferZonePercentage
+ _objc_msgSend$submitFeatureExtractorMetrics:
+ _objc_msgSend$successKeyForFeature:
+ _objc_msgSend$tryCompoundingVisits
+ _objc_msgSend$visitIntervalsForVisits:place:
+ _objc_msgSend$visitStartDateRangeFromObfuscatedStartDate:
+ _objc_msgSend$visits:withLoiIdentifier:
+ _objc_msgSend$visitsConsideredCount
+ _objc_msgSend$visitsPredatingCurrentDeviceFromVisits:
+ _objc_msgSend$visitsRedactedForAge
+ _objc_msgSend$visitsRedactedForAuthorizedLocation
+ _objc_msgSend$visitsRedactedForCategory
+ _objc_msgSend$visitsRedactedForConfidence
+ _objc_msgSend$visitsRedactedForPlaceType
+ _objc_msgSend$visitsRedactedForRegion
+ _objc_msgSend$visitsWithExit:beforeDate:
+ _objc_msgSend$visitsWithExit:dateInterval:
+ _objc_msgSend$wifiAccessPoints
+ _objectdestroy.29Tm
+ _os_eligibility_get_domain_answer
- +[RTFeatureExtractor featureExtractorSummary:featureDescription:firstFeatureItemDescription:lastFeatureItemDescription:stimulationDate:]
- +[RTVisitConsolidator redactVisits:authorizedLocations:bluePOICategoryDenylist:]
- -[RTCompanionLinkManager initWithCompanionLinkClient:]
- -[RTFeatureExtractor _extractFeatures:lookbackDurations:outError:]
- -[RTFeatureExtractor initWithLearnedLocationManager:visitManager:locationManager:eventManager:navigationManager:mapsSupportManager:motionActivityManager:vehicleLocationProvider:visitConsolidator:healthKitManager:homeKitManager:tripLocationPropagator:]
- -[RTLearnedLocationEngine _createAndStoreLOIForPlace:handler:]
- -[RTPersistenceDriver _setupPersistenceAfterConfigurationChange:cloudSyncAuthorization:account:]
- -[RTPersistenceMirroringManager(Metrics) mirroringManager:exceededHistoryType:count:limit:]
- -[RTPredictedContextDailyMetricsManager .cxx_destruct]
- -[RTPredictedContextDailyMetricsManager defaultsManager]
- -[RTPredictedContextDailyMetricsManager initWithDefaultsManager:]
- -[RTPredictedContextDailyMetricsManager init]
- -[RTPredictedContextDailyMetricsManager setDefaultsManager:]
- -[RTPredictedContextDailyMetricsManager submitMetricsForDailyPredictions:data:error:]
- -[RTPredictedContextManager _processTrainingEvent]
- -[RTPredictedContextMetricsManager initWithManagedConfiguration:predictedContextStore:defaultsManager:]
- -[RTPredictedContextMetricsManager prepareAndSubmitPredictionEventMetrics:]
- -[RTPredictedContextMetricsManager prepareAndSubmitTrainingEventMetrics]
- -[RTPredictedContextMetricsManager preparePredictionEventMetric:inferenceStartDate:inferenceTriggerReason:]
- -[RTPredictedContextMetricsManager prepareTrainingEventMetric]
- -[RTTripClusterManager _maximumInterTripSegmentDistanceAllowedForCompoundRoute]
- -[RTTripSegmentProvider _deferTripSegmentAndClusterProcessing:]
- -[RTTripSegmentProvider buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:]
- -[RTTripSegmentTransitionPreprocessor fetchLearnedLocationOfInterestForVisitIdentifier:]
- -[RTVisitConsolidator shouldRedactAllVisitsForCurrentRegion]
- -[SMActiveSessionZone setObservers:]
- -[SMDaemonClient setAuthorizationManager:]
- -[SMDaemonClient setDefaultsManager:]
- -[SMDaemonClient setDistanceCalculator:]
- -[SMDaemonClient setPlatform:]
- -[SMDaemonClient setQueue:]
- -[SMInitiatorService setLocationManager:]
- -[SMInitiatorService setMotionActivityManager:]
- -[SMLocationEvent setDistance:]
- -[SMLocationEvent setLocation:]
- -[SMReplayManager replayEvents]
- -[SMReplayManager setDefaults:]
- -[SMReplayManager setLocationToEtaDictionary:]
- -[SMReplayManager setMockLocations:]
- -[SMReplayManager setMockMotionActivities:]
- -[SMReplayManager setQueue:]
- -[SMReplayManager setReplayEvents:]
- -[SMReplayManager setResults:]
- -[SMReplayManager setTimerStack:]
- -[SMSessionMetricManager setCurrentDeviceIdentifier:]
- -[SMSessionMetricManager setDefaultsManager:]
- -[SMSessionMetricManager setDistanceCalculator:]
- -[SMSessionMetricManager setLearnedLocationManager:]
- -[SMSessionMetricManager setLocationManager:]
- -[SMSessionMetricManager setQueue:]
- -[SMSessionMetricManager setSessionStore:]
- -[SMSessionWorkoutMonitor pedometerSubscriptionUUID]
- -[SMSessionWorkoutMonitor setPedometerSubscriptionUUID:]
- -[SMWatchdogRecord setState:]
- -[SMWatchdogRecord setTimeout:]
- GCC_except_table125
- GCC_except_table207
- GCC_except_table228
- GCC_except_table233
- GCC_except_table235
- GCC_except_table247
- GCC_except_table250
- GCC_except_table252
- GCC_except_table256
- GCC_except_table273
- GCC_except_table283
- GCC_except_table299
- GCC_except_table300
- GCC_except_table305
- GCC_except_table331
- GCC_except_table409
- GCC_except_table417
- GCC_except_table74
- _OBJC_CLASS_$_RTPredictedContextDailyMetricsManager
- _OBJC_IVAR_$_RTPredictedContextDailyMetricsManager._defaultsManager
- _OBJC_IVAR_$_RTPredictedContextManager._monitorPredictedContext
- _OBJC_IVAR_$_SMReplayManager._replayEvents
- _OBJC_IVAR_$_SMSessionWorkoutMonitor._pedometerSubscriptionUUID
- _OBJC_METACLASS_$_RTPredictedContextDailyMetricsManager
- __OBJC_$_INSTANCE_METHODS_RTPredictedContextDailyMetricsManager
- __OBJC_$_INSTANCE_VARIABLES_RTPredictedContextDailyMetricsManager
- __OBJC_$_PROP_LIST_RTPredictedContextDailyMetricsManager
- __OBJC_CLASS_RO_$_RTPredictedContextDailyMetricsManager
- __OBJC_METACLASS_RO_$_RTPredictedContextDailyMetricsManager
- ___101-[RTBluePOIMonitor _updateLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:error:]_block_invoke
- ___101-[RTBluePOIMonitor _updateLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:error:]_block_invoke_2
- ___101-[RTLearnedLocationStore _fetchCountOfVisitsToLocationOfInterestWithIdentifier:dateInterval:handler:]_block_invoke.278
- ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke.75
- ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke.89
- ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke_2.78
- ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke_2.90
- ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke_3
- ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke_3.81
- ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke_4
- ___107-[RTPredictedContextMetricsManager preparePredictionEventMetric:inferenceStartDate:inferenceTriggerReason:]_block_invoke
- ___110-[RTTripSegmentProvider buildTinySegmentArrayForTransitionWithIndex:withinDateInterval:fromActivity:uuidType:]_block_invoke.355
- ___130-[RTBluePOIMonitor fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke.84
- ___130-[RTBluePOIMonitor fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke_2
- ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.69
- ___133-[RTBluePOIMonitor localBluePOIResultForReferenceLocation:locations:accessPoints:signalEnv:tileRequestPriority:collectMetrics:error:]_block_invoke.71
- ___144-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:includePlaceholders:includeVisits:includeTransitions:handler:]_block_invoke.337
- ___28-[RTHealthKitManager _setup]_block_invoke.616
- ___43-[RTPredictedContextManager _storeRequest:]_block_invoke.427
- ___47-[RTFingerprintManager onWiFiScanNotification:]_block_invoke.66
- ___47-[RTLearnedLocationStore _removePlace:handler:]_block_invoke.424
- ___47-[SMClientListener _setupConnection:forClient:]_block_invoke.278
- ___48-[RTFeatureExtractor _getHomeKitHomesWithError:]_block_invoke.432
- ___51-[RTLearnedLocationEngine _getDailyTrainingMetrics]_block_invoke.813
- ___51-[RTLearnedLocationEngine _teardownTrainingMetrics]_block_invoke.869
- ___53-[RTLearnedLocationStore _fetchLastVisitWithHandler:]_block_invoke.266
- ___53-[RTLearnedLocationStore _fetchPlaceOfVisit:handler:]_block_invoke.183
- ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.420
- ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.423
- ___54-[RTClusterLearnedRouteMetrics submitToCoreAnalytics:]_block_invoke.901
- ___54-[RTClusterLearnedRouteMetrics submitToCoreAnalytics:]_block_invoke_2.902
- ___54-[RTCompanionLinkManager initWithCompanionLinkClient:]_block_invoke
- ___54-[RTCompanionLinkManager initWithCompanionLinkClient:]_block_invoke.27
- ___54-[RTCompanionLinkManager initWithCompanionLinkClient:]_block_invoke.28
- ___54-[RTCompanionLinkManager initWithCompanionLinkClient:]_block_invoke.36
- ___54-[RTLearnedLocationStore _fetchVisitsToPlace:handler:]_block_invoke.255
- ___55-[RTFeatureExtractor _getLocationsOfInterestWithError:]_block_invoke.416
- ___55-[RTLearnedLocationEngine _retrainVisitsWithoutPlaces:]_block_invoke.871
- ___55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.551
- ___55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.412
- ___55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.413
- ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.371
- ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.372
- ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.378
- ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.380
- ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.385
- ___58-[RTAuthorizedLocationManager onVisitMonitorNotification:]_block_invoke.158
- ___58-[RTFeatureExtractor _getVisitsWithDateInterval:outError:]_block_invoke.411
- ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.823
- ___59-[RTLearnedLocationStore _fetchVisitIdentifiersIn:handler:]_block_invoke.286
- ___59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.581
- ___59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.577
- ___60-[RTLearnedLocationStore _fetchPlacesWithPredicate:handler:]_block_invoke.178
- ___60-[RTLearnedLocationStore _fetchVisitWithIdentifier:handler:]_block_invoke.236
- ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.34
- ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.35
- ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.37
- ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.38
- ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.43
- ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.44
- ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.49
- ___62-[RTLearnedLocationEngine _createAndStoreLOIForPlace:handler:]_block_invoke
- ___62-[RTLearnedLocationEngine _createAndStoreLOIForPlace:handler:]_block_invoke_2
- ___62-[RTLearnedLocationStore _fetchPlacesWithIdentifiers:handler:]_block_invoke.238
- ___62-[RTLearnedLocationStore _fetchPlacesWithIdentifiers:handler:]_block_invoke.241
- ___62-[RTTripSegmentProvider _processOneVisitTransition:trainMode:]_block_invoke
- ___63-[RTFeatureExtractor _getTransitionsWithDateInterval:outError:]_block_invoke.414
- ___64-[RTAuthorizedLocationManager collectMetricDataForTest:handler:]_block_invoke.161
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.244
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.247
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.248
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.250
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.253
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.256
- ___64-[RTPredictedContextManager _convertLocationOfInterest:sources:]_block_invoke.259
- ___65-[RTLearnedLocationStore _fetchPlacesWithType:predicate:handler:]_block_invoke.182
- ___66-[RTFeatureExtractor _getCalendarEventsWithDateInterval:outError:]_block_invoke.421
- ___66-[RTLearnedLocationStore _fetchMapItemWithMuid:predicate:handler:]_block_invoke.403
- ___66-[RTLearnedLocationStore _removeRecordsExpiredBeforeDate:handler:]_block_invoke.516
- ___67-[RTLearnedLocationEngine _applyUserCurationsSubmittedSince:error:]_block_invoke.918
- ___67-[RTLearnedLocationStore _fetchPlaceWithMapItemIdentifier:handler:]_block_invoke.232
- ___67-[RTPredictedContextManager _registerActivityTrainWithTrainPolicy:]_block_invoke.111
- ___68-[RTFeatureExtractor _getMapsViewedPlacesWithDateInterval:outError:]_block_invoke.426
- ___68-[RTFeatureExtractor _getMotionActivitiesWithDateInterval:outError:]_block_invoke.428
- ___68-[RTLearnedLocationStore _fetchLocationOfInterestWithPlace:handler:]_block_invoke.370
- ___68-[RTLearnedLocationStore _fetchPlacesWithMapItem:predicate:handler:]_block_invoke.214
- ___68-[RTMotionActivityManager_CoreMotion initWithPlatform:vehicleStore:]_block_invoke.95
- ___68-[RTUserCurationStore _fetchStoredUserCurationsWithOptions:handler:]_block_invoke.25
- ___69-[RTFeatureExtractor _getLocationHistoriesWithDateInterval:outError:]_block_invoke.419
- ___69-[RTLearnedLocationEngine _getUUIDSetOfLocationsOfInterestWithError:]_block_invoke.894
- ___69-[RTPredictedContextManager _rescheduleActivityTrainWithTrainPolicy:]_block_invoke.157
- ___69-[RTTripSegmentTransitionPreprocessor appendTransitionToCurrentVisit]_block_invoke.182
- ___69-[RTTripSegmentTransitionPreprocessor appendTransitionToCurrentVisit]_block_invoke.183
- ___70-[RTAuthorizedLocationManager _runEraseInstallDatabaseInitialization:]_block_invoke.152
- ___70-[RTLearnedLocationStore _fetchLocationOfInterestWithMapItem:handler:]_block_invoke.366
- ___70-[RTLearnedLocationStore _fetchVisitsOverlappingDateInterval:handler:]_block_invoke.265
- ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke.856
- ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke_2.857
- ___71-[RTLearnedLocationStore _fetchDevicesNotFromCurrentDeviceWithHandler:]_block_invoke.169
- ___71-[RTLearnedLocationStore _fetchLastVisitToPlaceWithIdentifier:handler:]_block_invoke.270
- ___71-[RTPredictedContextStore performPurgeOfType:referenceDate:completion:]_block_invoke.35
- ___72-[RTLearnedLocationStore _verifyExpirationDatesOfVisitGraphWithHandler:]_block_invoke_3
- ___72-[RTTripSegmentProvider addToTransitionLocationsBuffer:forDateInterval:]_block_invoke.358
- ___73-[RTLearnedLocationStore _fetchLocationOfInterestVisitedLastWithHandler:]_block_invoke.361
- ___73-[RTLearnedLocationStore _fetchLocationOfInterestWithIdentifier:handler:]_block_invoke.362
- ___73-[RTLearnedLocationStore _fetchLocationsOfInterestWithPlaceType:handler:]_block_invoke.320
- ___74-[RTLearnedLocationStore _fetchInferredMapItemForVisitIdentifier:handler:]_block_invoke.359
- ___74-[RTLearnedLocationStore _fetchLocationOfInterestVisitedFirstWithHandler:]_block_invoke.360
- ___75-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:handler:]_block_invoke.271
- ___75-[RTPredictedContextMetricsManager prepareAndSubmitPredictionEventMetrics:]_block_invoke
- ___76-[RTLearnedLocationEngine _appendVisitsToLocationsOfInterestModelWithError:]_block_invoke.873
- ___76-[RTLearnedLocationStore _fetchStoredMapItemsWithMapItem:predicate:handler:]_block_invoke.209
- ___76-[RTLearnedLocationStore _fetchTransitionsBetweenStartDate:endDate:handler:]_block_invoke.300
- ___76-[RTLearnedLocationStore _fetchVisitsWithPredicate:ascending:limit:handler:]_block_invoke.248
- ___77-[RTFeatureExtractor _getMapsHistoricalNavigationsWithDateInterval:outError:]_block_invoke.424
- ___77-[RTPredictedContextStore _fetchPredictedContextRequestsWithOptions:handler:]_block_invoke.29
- ___77-[SMTriggerDestination _updateInitiatorStatusDestinationBoundWithCompletion:]_block_invoke.220
- ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke.211
- ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke_2
- ___80-[RTLearnedLocationStore _fetchPlacesWithinDistance:location:predicate:handler:]_block_invoke.225
- ___81-[RTAuthorizedLocationManager _fetchAuthorizedLocationExtendedStatusWithMetrics:]_block_invoke.147
- ___83-[RTLearnedLocationEngine _recoverKnownPlaceTypesWithPlaceTypeClassifier:outError:]_block_invoke.812
- ___83-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:endDate:handler:]_block_invoke.282
- ___83-[RTLearnedLocationStore _fetchLocationsOfInterestWithinDistance:location:handler:]_block_invoke.316
- ___85-[RTTripSegmentTransitionPreprocessor fetchEndpointCLLocationForTransition:atOrigin:]_block_invoke.198
- ___86-[RTLearnedLocationStore _fetchVisitsWithIncompletePlacesForCurrentDeviceWithHandler:]_block_invoke.396
- ___88-[RTTripSegmentTransitionPreprocessor fetchLearnedLocationOfInterestForVisitIdentifier:]_block_invoke
- ___88-[RTTripSegmentTransitionPreprocessor fetchLearnedLocationOfInterestForVisitIdentifier:]_block_invoke.174
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke.900
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke.905
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke.906
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke.907
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke.908
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke.913
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke.914
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke_2
- ___89-[RTLearnedLocationEngine _applyUserCuration:relabelerPersister:harvestCuration:handler:]_block_invoke_2.901
- ___90-[RTMotionActivityManager_CoreMotion _fetchMotionActivitiesFromStartDate:endDate:handler:]_block_invoke.130
- ___90-[RTMotionActivityManager_CoreMotion _fetchMotionActivitiesFromStartDate:endDate:handler:]_block_invoke.133
- ___91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.552
- ___91-[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke.173
- ___94-[RTLearnedLocationStore _fetchLocationOfInterestTransitionsBetweenStartDate:endDate:handler:]_block_invoke.383
- ___96-[RTPersistenceDriver _setupPersistenceAfterConfigurationChange:cloudSyncAuthorization:account:]_block_invoke
- ___97-[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngineWithPlaceStats:dateInterval:]_block_invoke.408
- ___99-[RTTripSegmentProvider buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:]_block_invoke
- ___99-[RTTripSegmentProvider buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:]_block_invoke.395
- ___99-[RTTripSegmentProvider buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:]_block_invoke.398
- ___99-[RTTripSegmentProvider buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:]_block_invoke.399
- ___block_descriptor_105_e8_32s40s48s56s64s72s80s88bs_e5_v8?0ls32l8s88l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_128_e8_32s40s48bs56r64r72r80r88r96r104r_e5_v8?0lr56l8r64l8r72l8r80l8r88l8r96l8s48l8s32l8s40l8r104l8
- ___block_descriptor_130_e8_32s40s48bs56r64r72r80r88r96r104r_e5_v8?0lr56l8r64l8s32l8r72l8s40l8r80l8r88l8r96l8s48l8r104l8
- ___block_descriptor_40_e8_32w_e39_v24?0"NSDictionary"8"NSDictionary"16lw32l8
- ___block_descriptor_48_e8_32s40r_e30_v24?0"NSNumber"8"NSError"16lr40l8s32l8
- ___block_descriptor_48_e8_32s40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs_e36_v24?0"RTUserCuration"8"NSError"16ls40l8s32l8
- ___block_descriptor_56_e8_32s40s_e35_v32?0"RTPredictedContext"8Q16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s_e38_v32?0"RTTripSegmentFeatures"8Q16^B24ls32l8s40l8
- ___block_descriptor_64_e8_32s40bs48r_e20_v20?0B8"NSError"12ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56r_e38_"RTInferredMapItem"16?0"RTMapItem"8ls32l8s40l8s48l8r56l8
- ___block_descriptor_81_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16ls32l8s64l8s40l8s48l8s56l8
- ___block_descriptor_89_e8_32s40s48s56s64s72bs_e17_v16?0"NSError"8ls32l8s72l8s40l8s48l8s56l8s64l8
- ___block_descriptor_89_e8_32s40s48s56s64s72bs_e49_v24?0"RTLearnedLocationOfInterest"8"NSError"16ls32l8s72l8s40l8s48l8s56l8s64l8
- ___block_descriptor_97_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s80l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.1373
- ___block_literal_global.1379
- ___block_literal_global.142
- ___block_literal_global.150
- ___block_literal_global.189
- ___block_literal_global.212
- ___block_literal_global.230
- ___block_literal_global.262
- ___block_literal_global.314
- ___block_literal_global.323
- ___block_literal_global.370
- ___block_literal_global.389
- ___block_literal_global.418
- ___block_literal_global.443
- ___block_literal_global.546
- ___block_literal_global.580
- ___block_literal_global.638
- ___block_literal_global.684
- ___block_literal_global.894
- ___block_literal_global.911
- ___block_literal_global.916
- _block_copy_helper.29
- _block_descriptor.31
- _block_destroy_helper.30
- _kRTPredictedContextMetricsKeyInferencePredictionCount
- _kRTPredictedContextMetricsKeyTrainingSuccess
- _objc_msgSend$_createAndStoreLOIForPlace:handler:
- _objc_msgSend$_deferTripSegmentAndClusterProcessing:
- _objc_msgSend$_extractFeatures:lookbackDurations:outError:
- _objc_msgSend$_isHealthKitInaccessibleErrorIncludedInTheErrorArray:
- _objc_msgSend$_maximumInterTripSegmentDistanceAllowedForCompoundRoute
- _objc_msgSend$_processTrainingEvent
- _objc_msgSend$_setupPersistenceAfterConfigurationChange:cloudSyncAuthorization:account:
- _objc_msgSend$buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:
- _objc_msgSend$featureExtractorSummary:featureDescription:firstFeatureItemDescription:lastFeatureItemDescription:stimulationDate:
- _objc_msgSend$fetchLearnedLocationOfInterestForVisitIdentifier:
- _objc_msgSend$initWithCompanionLinkClient:
- _objc_msgSend$initWithInterval:gracePeriod:priority:requireNetworkConnectivity:requireInexpensiveNetworkConnectivity:networkTransferDirection:allowBattery:powerNap:requiresClassA:
- _objc_msgSend$initWithLearnedLocationManager:visitManager:locationManager:eventManager:navigationManager:mapsSupportManager:motionActivityManager:vehicleLocationProvider:visitConsolidator:healthKitManager:homeKitManager:tripLocationPropagator:
- _objc_msgSend$initWithManagedConfiguration:predictedContextStore:defaultsManager:
- _objc_msgSend$mirroringManager:exceededHistoryType:count:limit:
- _objc_msgSend$prepareAndSubmitPredictionEventMetrics:
- _objc_msgSend$prepareAndSubmitTrainingEventMetrics
- _objc_msgSend$preparePredictionEventMetric:inferenceStartDate:inferenceTriggerReason:
- _objc_msgSend$prepareTrainingEventMetric
- _objectdestroy.24Tm
CStrings:
+ "\x05'"
+ "%@ %@, found an existing map item for original label, %@, map item, %@"
+ "%@ %@, no existing map item found, creating one for original label, %@"
+ "%@, %@, Feture event metrics submission error, %@"
+ "%@, %@, Finished training, result, %@, was deferred, %@, error, %@"
+ "%@, %@, Overriding trainPolicy from, %@, to %@, because areMaxTrainAttemptsWithinLastDayReached, %@"
+ "%@, %@, Running verification of expiration dates of visit graph"
+ "%@, %@, applying user curation as a current place curation"
+ "%@, %@, applying user curation as a historical visit curation"
+ "%@, %@, comparing prediction loiIdentifier, %@, dateInterval start, %@, end, %@, with visit loiIdentifier, %@, entry, %@, exit, %@, same loiIdentifier, %@, overlapping intervals, %@"
+ "%@, %@, comparing visit loiIdentifier, %@, entry, %@, exit, %@, with prediction loiIdentifier, %@, dateInterval start, %@, end, %@, same loiIdentifier, %@, overlapping intervals, %@"
+ "%@, %@, could not fetch current visit type"
+ "%@, %@, could not find any LOIs associated with curation with UUID %@, error, %@"
+ "%@, %@, could not find any visits to associate with curation with UUID %@, error, %@"
+ "%@, %@, dailyInferenceEventMetrics, %{sensitive}@"
+ "%@, %@, distance from place to visit location exceeded threshold. Skipping visit interval."
+ "%@, %@, earliest start date for visits ending before yesterday, %@, earliest start date for visits ending yesterday, %@, latest end date for visits ending yesterday, %@, last 24 hour inference request count, %lu, predictions ending yesterday count, %lu, inferences with predictions ending yesterday count, %lu, total fetched visit count, %lu, visits ending yesterday count, %lu, visits before that, %lu"
+ "%@, %@, error detected: truth visit from yesterday, %@, is unknown"
+ "%@, %@, error fetching predicted context requests, %@"
+ "%@, %@, error fetching predictions, %@"
+ "%@, %@, error fetching visits, %@"
+ "%@, %@, error occurred while attempting to store new LOI, %@"
+ "%@, %@, error occurred while creating and storing new LOI, %@"
+ "%@, %@, error occurred while fetching LOI, %@"
+ "%@, %@, error occurred while fetching place for map item, %@"
+ "%@, %@, error occurred while initializing visit date interval with start date %@ and end date %@, error, %@. Skipping visit interval."
+ "%@, %@, error occurred while invoking fetchVisitWithIdentifier with identifier, %@, error, %@"
+ "%@, %@, error occurred while invoking fetchVisitsOverlappingDate for date, %@, error, %@"
+ "%@, %@, error occurred while invoking fetchVisitsOverlappingDateInterval with date interval, %@, error, %@"
+ "%@, %@, error was issued while fetching current device from store, error: %@"
+ "%@, %@, error was issued while fetching local device visits from store, error: %@"
+ "%@, %@, fetch of newly stored LOI with ID, %@, unexpectedly failed"
+ "%@, %@, fetched %lu visits overlapping user curation with entry date, %@"
+ "%@, %@, fetched %lu visits within curation date interval, %@, error, %@"
+ "%@, %@, fetched current visit while currentVisitType was nil"
+ "%@, %@, fetched newly submitted curation with identifier, %@"
+ "%@, %@, fetched requests count, %lu"
+ "%@, %@, filtering for remote device visits predating device creation date on %@"
+ "%@, %@, found %lu visits to associate with curation with UUID %@"
+ "%@, %@, high probability prediction count, %lu"
+ "%@, %@, idx, %lu, error, %@"
+ "%@, %@, idx, %lu, truthEventMetrics, %{sensitive}@"
+ "%@, %@, new LOI created and stored successfully for curation label, %@"
+ "%@, %@, no curated label associated with curation, exiting early"
+ "%@, %@, no input visits provided, returning early"
+ "%@, %@, no pre-existing location of interest found for map item, creating one"
+ "%@, %@, no predicted context requests fetched"
+ "%@, %@, no predicted contexts fetched"
+ "%@, %@, no valid creation date for current device, returning early"
+ "%@, %@, no visit found matching the user curation's visit identifier, searching for matching visits within the unobfuscated time range, %@"
+ "%@, %@, no visits fetched"
+ "%@, %@, obfuscated visit start date was pushed out to the next time bucket - this should not happen; original start date, %@, obfuscated start date, %@"
+ "%@, %@, overall visits count, %lu, local device visits count, %lu, earlier remote device visits count, %lu, place, %{sensitive}@"
+ "%@, %@, place location, %{sensitive}@, visit location, %{sensitive}@, distance from place to visit location, %.3f, visit interval start date, %@, visit interval end date, %@, earliestStartDate, %@, latestEndDate, %@, error, %@"
+ "%@, %@, pre-existing location of interest was found, %@"
+ "%@, %@, prediction count, %lu, truePositive count, %lu, highestProbability, %.2f, leadTime, %.2f"
+ "%@, %@, predictionEventMetrics, %{sensitive}@"
+ "%@, %@, received visit , %{sensitive}@"
+ "%@, %@, reduced all visits within curation date interval to %lu visits matching curation's map item, error, %@"
+ "%@, %@, result, %@, error, %@"
+ "%@, %@, retrieving curation with identifier, %@"
+ "%@, %@, semaphore error while fetching current device from store, error: %@"
+ "%@, %@, skipping metrics submission due to errors"
+ "%@, %@, skipping metrics submission due to no visits ending before yesterday"
+ "%@, %@, skipping metrics submission due to no visits ending yesterday"
+ "%@, %@, storing %@: %@"
+ "%@, %@, successfully fetched a visit matching the user curation's visit identifier"
+ "%@, %@, successfully fetched newly stored LOI with ID, %@, now returning"
+ "%@, %@, successfully stored new LOI with ID, %@"
+ "%@, %@, training result, %@, after evaluating error(s), %@"
+ "%@, %@, truth event metrics submission error, %@"
+ "%@, %@, user curation has no associated visit identifier, but does not appear to be a current place curation, this may have been submitted by a deprecated SPI, %@"
+ "%@, %@, visit interval end date exceeded earliest start date. Skipping visit interval."
+ "%@, %@, while attempting to fetch a newly submitted user curation with identifier, %@, a different curation was found - this should not happen"
+ "%@, %@, while attempting to fetch a newly submitted user curation with identifier, %@, no curation was found - this should not happen"
+ "%@, %@, yesterday's visit to %{sensitive}@, entry, %@, predictability, %.2f"
+ "%@, %@, ✅ overlapping truth visit, %@, prediction, %@"
+ "%@, %@, ✅ true positive prediction, %{sensitive}@, visit, %{sensitive}@"
+ "%@, %@, ❌ no overlapping truth visit for prediction, %@"
+ "%@, Error: Invalid targetVisit"
+ "%@, Error: No priorVisits"
+ "%@, No relevant prior visits found for LOI: %@ and day of week: %ld"
+ "%@, Time Difference: %f"
+ "%@, averageOccupancy: %f"
+ "%@, correlation: %f"
+ "%@, current account, (%@), current status, %@, new account, (%@), new status, %@"
+ "%@, currentCloudSyncAuthorization, %@, newCloudSyncAuthorization, %@"
+ "%@, currentDataAvailability, %@, newDataAvailability, %@"
+ "%@, currentTimeCFAbsolute, %.2f, currentTimeZoneAbbreviation, %@"
+ "%@, encryptedDataAvailability, %{public}@, cloudSyncAuthorization, %{public}@, accountStatus, %{public}@, account, %{private}@"
+ "%@, exceeds per-fingerprint limit, before, %lu, after, %lu"
+ "%@, failedWithError, %ld"
+ "%@, iMessageAccountEnabled, %@, error, %@"
+ "%@, including visit within midnight boundary"
+ "%@, invalid inputs for dateInterval, startDate, %@, endDate, %@, error, %@"
+ "%@, numberOfVisitsByDayOfWeek: %ld"
+ "%@, predictability (before clamping): %f"
+ "%@, predictability, %f, for target visit, %{sensitive}@, loiIdentifier, %@, entry, %@"
+ "%@, predictedContextMO, %{sensitive}@, requestDate, %@"
+ "%@, priorVisitOccupancies: %@"
+ "%@, relevantPriorVisits count: %lu"
+ "%@, scaleFactor: %f"
+ "%@, shouldSetupAccordingTo, deviceConfiguration, %@, cloudSyncAuthorization, %@, accountState, %@, overall, %@"
+ "%@, sync allowed, current count %lu < max%lu"
+ "%@, target visit, %{sensitive}@, loiIdentifier, %@, entry, %@, prior visit count, %lu, timeWindowHalfWidthSeconds: %f"
+ "%@, timeVariance: %f"
+ "%@, variancePenalty: %f"
+ "%@:%@,numberOfSetupLocs,%{public}d,zdrSetupEntryWithOldestEntryTime,%{sensitive}@,zdrSetupEntryWithOldestValidLocation,%{sensitive}@"
+ "%@:%@: curation date interval error,%{public}@"
+ "%@:%@: curation date interval start,%{public}@,end,%{public}@"
+ "%@:%@: isStartOlderThanEndDate,%{public}d,Either Start,%{public}@ or end,%{public}@ date is not valid"
+ "%@:No tripClusters with valid routes found for RTLearnedRouteFetchType_Any"
+ "%@_processNextVisitTransition,learnClusters,starting,count,%{public}lu,fetchedNewTransitions,%{public}d,successfulTransitionsSinceLastClustering,%{public}d,learnClusters,starting."
+ "+[RTVisitRedactionUtilities redactVisits:authorizedLocations:bluePOICategoryDenylist:]"
+ "-[RTLearnedLocationEngine _findVisitsAssociatedWithCurrentPlaceCuration:error:]"
+ "-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]"
+ "-[RTTripSegmentProvider _isValidTransitionToProcess:]"
+ "-[RTTripSegmentProvider buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:]"
+ "-[RTTripSegmentProvider buildTripSegmentsFromTripSegmentFeaturesList:startVisitLocation:stopVisitLocation:transitionStartStopLocations:]"
+ "-[RTTripSegmentTransitionPreprocessor _addCompoundedVisitInterval:]"
+ "-[RTTripSegmentTransitionPreprocessor _isVisitCompoundingLeadingToLoopbackTransition:currentVisitStatus:]"
+ "-[RTUserCurationManager createAndStoreCurationWithEntryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:handler:]"
+ "-[RTUserCurationStore _fetchStoredUserCurationWithIdentifier:handler:]"
+ "-[RTVisitConsolidator _fetchRedactedStoredVisitsWithOptions:redactedVisitsHandler:]"
+ ".B"
+ "22:36:42"
+ "<invalid>"
+ "@\"RTBlueSkyDailyMetrics\""
+ "@\"RTVisitRedactionDetails\""
+ "@48@0:8Q16Q24@32^@40"
+ "@52@0:8@16f24q28f36q40f48"
+ "@64@0:8Q16@24Q32^@40^@48^@56"
+ "B16@?0i8i12"
+ "B40@0:8@16q24d32"
+ "Becoming stationary, setting stationary start date"
+ "BlueSkyDailyNumAOILabels"
+ "BlueSkyDailyNumCategoriesOfInterest"
+ "BlueSkyDailyNumPOILabels"
+ "BlueSkyDailyNumPlaceInferencesReceived"
+ "BlueSkyDailyNumSyncsRequiring10SecWait"
+ "BlueSkyDailyNumSyncsRequiring1MinWait"
+ "BlueSkyDailyNumSyncsRequiring20SecWait"
+ "BlueSkyDailyNumSyncsRequiring2MinWait"
+ "BlueSkyDailyNumSyncsRequiring30SecWait"
+ "BlueSkyDailyNumSyncsRequiring5MinPlusWait"
+ "BlueSkyDailyNumSyncsRequiring5MinWait"
+ "BlueSkyDailyNumSyncsRequiringNoWait"
+ "BlueSkyDailyNumVisitsReceived"
+ "BlueSkyDailyQualifiedPlaceInferences"
+ "BlueSkyDailyQualifiedPlaceInferencesSent"
+ "BlueSkyDailyQualifiedVisits"
+ "BlueSkyDailyQualifiedVisitsOverLimit"
+ "BlueSkyDailyQualifiedVisitsSent"
+ "BlueSkyLastDailyMetricsSubmissonAttemptDate"
+ "CoreRoutine.BlueSkySendDaily"
+ "CoreRoutine.PredictedContext.DailyInferenceEvents"
+ "CoreRoutine.PredictedContext.FeatureExtractor"
+ "CoreRoutine.PredictedContext.TruthEvent"
+ "CoreRoutine.StoredVisitRedaction"
+ "CoreRoutine.UserCuration.CurationCount"
+ "CoreRoutine.UserCuration.CurationSubmission"
+ "Defer: Feature Extractor Error"
+ "Defer: Integrity Error"
+ "Error constructing date interval for metrics, startDate, %@, endDate, %@"
+ "Fail: Algo State Version Mismatch Error"
+ "Fail: Insufficient Input Error"
+ "Fail: Invalid Parameter Error"
+ "Fail: Invalid State Error"
+ "Failed to create an RTDevice from RTDeviceMO"
+ "Fetch block failed, error, %@"
+ "FetchStoredVisits-Done"
+ "FetchStoredVisits-Start"
+ "Interrupted"
+ "Invalid parameter not satisfying: chunks (in %s:%d)"
+ "Invalid parameter not satisfying: compoundedVisitInterval (in %s:%d)"
+ "Invalid parameter not satisfying: currentVisitStatus (in %s:%d)"
+ "Invalid parameter not satisfying: dailyBlueSkyMetrics"
+ "Invalid parameter not satisfying: originalLabel"
+ "Invalid parameter not satisfying: startVisitLocationOut (in %s:%d)"
+ "Invalid parameter not satisfying: stopVisitLocationOut (in %s:%d)"
+ "Invalid parameter not satisfying: transitionStartStopLocationsOut (in %s:%d)"
+ "Invalid parameter not satisfying: transitions (in %s:%d)"
+ "Jul  1 2025"
+ "L'"
+ "ManagedObjectContext failed to return current device"
+ "Mismatched curation retrieved"
+ "NULL device object"
+ "Newly stored LOI unexpectedly not found"
+ "NoAccount"
+ "Not stationary, clearing stationary start date"
+ "RTBlueSkyDailyMetrics"
+ "RTBlueSkyDailyMetrics, %lu, "
+ "RTCloudManagedObject, %@, object of class %@ with identifier %@  has an expiration date (%@) which is more than 2 weeks away, skipping expiration date verification"
+ "RTDefaultsBluePOIMonitorEnablerStationaryDurationForPausing"
+ "RTDefaultsLearnedRoutesFetchSPITopListClusterMaxNum"
+ "RTDefaultsTripClusterStartEndRoadCountBufferZonePercentage"
+ "RTDefaultsTripSegmentCompoundingLoopbackCheckDuration"
+ "RTDefaultsTripSegmentEnableVisitBasedCompounding"
+ "RTDefaultsTripSegmentMaxAdjacentVisitsToCompound"
+ "RTDefaultsTripSegmentShouldDisableProcessingInChina"
+ "RTDefaultsTripSegmentVisitCompoundingShortVisitDuration"
+ "RTTripSegmentProvider,_isValidTransitionToProcess,TripSegment already exists in store for date interval %@, and configuration set to reprocess trip segment data."
+ "RTTripSegmentProvider,_isValidTransitionToProcess,TripSegment already exists in store for date interval %@, and configuration set to skip reprocessing trip segment data."
+ "RTTripSegmentProvider,_isValidTransitionToProcess,transition processing disallowed based on region check,%@,startCoordinate,%{sensitive}.7lf,%{sensitive}.7lf,stopCoordinate,%{sensitive}.7lf,%{sensitive}.7lf"
+ "RTTripSegmentProvider,_isValidTransitionToProcess,unable to verify region,coordinate not available,transition processing disallowed,%@"
+ "RTTripSegmentProvider,buildTripSegmentsFeaturesWithIndex,failed in motion activity fetching,fetchError,%@,semaError,%@"
+ "RTTripSegmentProvider,buildTripSegmentsFeaturesWithIndex,fetchedMotionActivity,transitionIndex,%tu,rawActivityCount,%tu,rawActivityIndex,%tu,thisRawActivity,%@"
+ "RTTripSegmentProvider,buildTripSegmentsFeaturesWithIndex,fetchedMotionActivitySummary,transitionIndex,%tu,countOfFetchedActivities,%tu"
+ "RTTripSegmentProvider,buildTripSegmentsFeaturesWithIndex,filteredMotionActivity,transitionIndex,%tu,activityCount,%tu,activityIndex,%tu,thisFilteredActivity,%@"
+ "RTTripSegmentProvider,buildTripSegmentsFeaturesWithIndex,filteredMotionActivitySummary,transitionIndex,%tu,activityCount,%tu"
+ "RTTripSegmentProvider,buildTripSegmentsFeaturesWithIndex,for tripId,%@,start date,%@,stop date,%@"
+ "RTTripSegmentProvider,buildTripSegmentsFeaturesWithIndex,generatedChunks,tId,%@,transitionIndex,%tu,activityCount,%tu,chunkIndex,%tu,chunkCount,%tu,thisChunk,%@"
+ "RTTripSegmentProvider,buildTripSegmentsFeaturesWithIndex,generatedChunksSummary,transitionIndex,%tu,chunkCount,%tu"
+ "RTTripSegmentProvider,buildTripSegmentsFeaturesWithIndex,skipThisTransition,%tu,lack of real mode of transportation,predominantType,%tu"
+ "RTTripSegmentProvider,buildTripSegmentsFeaturesWithIndex,trainMode,%{public}lu,transition cnt,%{public}lu,curr index,%{public}lu"
+ "RTTripSegmentProvider,buildTripSegmentsFromTripSegmentFeaturesList,transitionId,%@,status,%{public}d"
+ "RTTripSegmentProvider,transitionId,%@,buildTripSegmentsFeaturesWithIndex,chunk generation failed"
+ "RTTripSegmentProvider: buildTripSegmentsFeaturesWithIndex, trainMode, %lu"
+ "RTTripSegmentProvider: no clLocations fetched for,dateInterval,%@,fetchError,%@,semaError,%@"
+ "RTTripSegmentProvider:defer,TripSegmentAndClusterProcessing,%d"
+ "RTTripSegmentProvider:processChunkWithIndex,deferring,chunk,%{public}d/%{public}d,tripStart,%{private}@,tripEnd,%{private}@"
+ "RTTripSegmentTransitionPreprocessor,pre tryCompounding,found long duration visit,transitions index,%{public}ld"
+ "RTTripSegmentTransitionPreprocessor,pre tryCompounding,large num of terminal short duration visits,%{public}lu"
+ "RTTripSegmentTransitionPreprocessor,pre tryCompounding,last transition > 3 days old, processing all transitions"
+ "RTTripSegmentTransitionPreprocessor,pre tryCompounding,number of terminal transitions removed,%{public}lu,transitions to process,%{public}lu"
+ "RTTripSegmentTransitionPreprocessor,pre tryCompounding,visit timestamps null,transition index,%{public}ld"
+ "RTTripSegmentTransitionPreprocessor,tryCompoundingVisits,not enabled"
+ "RTTripSegmentTransitionPreprocessor,tryCompoundingVisits,not enough transitions to compound,%{public}lu"
+ "RTTripSegmentTransitionPreprocessor,tryCompoundingVisits,unexpected size for _tripSegmentVisitStatus,%{public}lu,and _tripSegmentTransitions,%{public}lu"
+ "RTTripSegmentTransitionPreprocessor: applyRule_VehicleConnectionCannotSpanVisits_ForVisitAtIndex, tripSegmentVisitStatus[%ld], Reject"
+ "RTTripSegmentTransitionPreprocessor: fetchLearnedLocationOfInterestForVisitIdentifier: %@ fetched learnedLocation: %{sensitive}@"
+ "RTTripSegmentTransitionPreprocessor: fetchLearnedLocationOfInterestForVisitIdentifier: %@ fetched learnedLocationOfInterest: %{sensitive}@"
+ "RTUserCurationMetrics"
+ "RTVisitConsolidatorResult"
+ "RTVisitRedactionDetails"
+ "RTVisitRedactionMetric"
+ "RTVisitRedactionUtilities"
+ "Success: HealthKit InaccessibleError"
+ "Success: Interruption Ignored"
+ "Success: No Errors"
+ "T@\"NSDate\",&,N,V_stationaryStartDate"
+ "T@\"NSDate\",C,N,V_currentDate"
+ "T@\"NSDate\",C,N,V_date"
+ "T@\"NSDate\",C,N,V_lastPlaceInferenceSyncAttemptDate"
+ "T@\"NSDate\",C,N,V_lastVisitSyncAttemptDate"
+ "T@\"NSDate\",C,N,V_sessionEndDate"
+ "T@\"NSDate\",C,N,V_sessionStartDate"
+ "T@\"NSHashTable\",R,N,V_observers"
+ "T@\"NSMutableArray\",&,N,V_visitsRedactedForAge"
+ "T@\"NSMutableArray\",&,N,V_visitsRedactedForAuthorizedLocation"
+ "T@\"NSMutableArray\",&,N,V_visitsRedactedForCategory"
+ "T@\"NSMutableArray\",&,N,V_visitsRedactedForConfidence"
+ "T@\"NSMutableArray\",&,N,V_visitsRedactedForPlaceType"
+ "T@\"NSMutableArray\",&,N,V_visitsRedactedForRegion"
+ "T@\"NSMutableArray\",R,N,V_compoundedVisitIntervals"
+ "T@\"NSMutableArray\",R,N,V_mockLocations"
+ "T@\"NSMutableArray\",R,N,V_mockMotionActivities"
+ "T@\"NSMutableArray\",R,N,V_timerStack"
+ "T@\"NSMutableDictionary\",R,N,V_defaults"
+ "T@\"NSMutableDictionary\",R,N,V_locationToEtaDictionary"
+ "T@\"NSMutableDictionary\",R,N,V_results"
+ "T@\"NSNumber\",&,V_currentVisitType"
+ "T@\"NSString\",C,N,V_resultsPath"
+ "T@\"NSUUID\",&,V_idOfCurrentlyProcessingChunk"
+ "T@\"NSUUID\",R,N,V_currentDeviceIdentifier"
+ "T@\"RTBlueSkyDailyMetrics\",&,N,V_dailyBlueSkyMetrics"
+ "T@\"RTVisitRedactionDetails\",R,N,V_redactionDetails"
+ "T@\"SMSessionManagerState\",R,N,V_state"
+ "TB,V_shouldDeferTripSegmentAndClusterProcessing"
+ "TQ,N,V_redactedForAuthorizedLocation"
+ "TQ,N,V_redactedForCategory"
+ "TQ,N,V_redactedForConfidence"
+ "TQ,N,V_redactedForPlaceType"
+ "TQ,N,V_redactedForRegion"
+ "TQ,N,V_visitsConsideredCount"
+ "Td,N,V_redactionProportion"
+ "Td,N,V_startEndRoadCountBufferZonePercentage"
+ "Tq,V_currentAccountStatus"
+ "Unsupported Platform"
+ "ValidAccount"
+ "_addCompoundedVisitInterval:"
+ "_areTwoVisitsSame:firstVisitLocation:secondLearnedLOI:secondVisitLocation:"
+ "_compoundedVisitIntervals"
+ "_countBins"
+ "_createLOIForPlace:error:"
+ "_currentAccountStatus"
+ "_currentVisitType"
+ "_dailyBlueSkyMetrics"
+ "_evaluateTrainErrorForResult:"
+ "_extractFeatures:operationType:lookbackDurations:outError:"
+ "_fetchCurrentDeviceWithHandler:"
+ "_fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:"
+ "_fetchPredictedContextAndRequestDateWithOptions:handler:"
+ "_fetchRedactedStoredVisitsWithOptions"
+ "_fetchRedactedStoredVisitsWithOptions:redactedVisitsHandler:"
+ "_fetchStoredUserCurationWithIdentifier:handler:"
+ "_fetchVisitsOverlappingDate:handler:"
+ "_findOrCreateLOIForMapItem:error:"
+ "_findVisitsAssociatedWithCurrentPlaceCuration:error:"
+ "_findVisitsAssociatedWithHistoricalVisitCuration:error:"
+ "_idOfCurrentlyProcessingChunk"
+ "_isValidTransitionToProcess,Unexpected - transition pointer is nil"
+ "_isValidTransitionToProcess:"
+ "_isVisitCompoundingLeadingToLoopbackTransition,%{public}ld,out of range [0, %{public}lu]"
+ "_isVisitCompoundingLeadingToLoopbackTransition,loopback visit"
+ "_isVisitCompoundingLeadingToLoopbackTransition,loopbackReferenceTime,nil,transition,%@"
+ "_isVisitCompoundingLeadingToLoopbackTransition,nil learnedLOI,nil visitlocation,visit,%@"
+ "_isVisitCompoundingLeadingToLoopbackTransition,nil nextLearnedLOI,nil learnedLocationNextVisit"
+ "_isVisitCompoundingLeadingToLoopbackTransition,nil previousLearnedLOI,nil learnedLocationPrevVisit"
+ "_isVisitCompoundingLeadingToLoopbackTransition,no loopback visit,deltaTime from past visit,%{public}0.2f,prevVisitStopDate,%@,maxVisitLoopDurationSec,%{public}d,visitStatus,%{public}lu,tId,%{public}ld"
+ "_isVisitCompoundingLeadingToLoopbackTransition,no loopback,maxVisitLoopDurationSec,%{public}d,tId,%{public}ld"
+ "_isVisitCompoundingLeadingToLoopbackTransition,past history loopback"
+ "_isVisitCompoundingLeadingToLoopbackTransition,prevVisitId,%@,currVisit,%@,nextVisit,%@"
+ "_isVisitCompoundingLeadingToLoopbackTransition,transitionStopTime,nil,transition,%@"
+ "_isVisitCompoundingLeadingToLoopbackTransition:currentVisitStatus:"
+ "_lastPlaceInferenceSyncAttemptDate"
+ "_lastVisitSyncAttemptDate"
+ "_logDeferTripSegmentAndClusterProcessingDate:"
+ "_onVisit:"
+ "_processNextVisitTransition,learnClusters,Skipped,count,%{public}lu,fetchedNewTransitions,%{public}d,successfulTransitionsSinceLastClustering,%{public}d"
+ "_processOneVisitTransition,Unexpected - transition pointer is nil"
+ "_processSingleOrCompoundedVisitTransition,chunk generation failed,no compounding"
+ "_processSingleOrCompoundedVisitTransition,chunkLocationsNearEnoughToCompound failed,no compounding"
+ "_processSingleOrCompoundedVisitTransition,compounding check end,transitions to compound,%{public}d"
+ "_processSingleOrCompoundedVisitTransition,compounding success status,%{public}d,startLoc,%{sensitive}@,endLoc,%{sensitive}@,numChunks,%{public}lu"
+ "_processSingleOrCompoundedVisitTransition,no compounding,_isValidTransitionToProcess failed"
+ "_processSingleOrCompoundedVisitTransition,no compounding,prevTransitionStopData,%@,currentTransitionStartDate,%@,error,%@"
+ "_processSingleOrCompoundedVisitTransition,stitchWalkChunk,%@,prevMode,%d,currentMode,%d"
+ "_processSingleOrCompoundedVisitTransition,transition count,%{public}lu,transitions to compound,%{public}d"
+ "_processSingleOrCompoundedVisitTransition,transition count,%{public}lu,transitions to compound,%{public}d,start index,%{public}ld"
+ "_processSingleOrCompoundedVisitTransition,tripId,%@,num chunks generated to compound,%{public}lu"
+ "_processSingleOrCompoundedVisitTransition:"
+ "_processTrainingResult:"
+ "_proportionBins"
+ "_redactedForAuthorizedLocation"
+ "_redactedForCategory"
+ "_redactedForConfidence"
+ "_redactedForPlaceType"
+ "_redactedForRegion"
+ "_redactionDetails"
+ "_redactionProportion"
+ "_setupPersistenceAfterConfigurationChange:cloudSyncAuthorization:accountStatus:account:"
+ "_shouldAttemptSetupAccordingToAccountStatus:account:"
+ "_shouldAttemptSetupAccordingToCloudSyncAuthorization:"
+ "_shouldDisableProcessingInChina"
+ "_startEndRoadCountBufferZonePercentage"
+ "_stationaryStartDate"
+ "_submitDailyUserCurationMetrics"
+ "_updatePendingSyncMetrics:"
+ "_updateSyncCachedMetrics:"
+ "_updateSyncMetrics:"
+ "_updateSyncSuccessMetrics:waitRequired:"
+ "_visitCompoundingLoopbackCheckDurationSec"
+ "_visitCompoundingShortVisitDurationSec"
+ "_visitsConsideredCount"
+ "_visitsRedactedForAge"
+ "_visitsRedactedForAuthorizedLocation"
+ "_visitsRedactedForCategory"
+ "_visitsRedactedForConfidence"
+ "_visitsRedactedForPlaceType"
+ "_visitsRedactedForRegion"
+ "a backup already exists at the path %@ and is recent (%@, %@), skipping"
+ "abbreviation"
+ "accountStatusToString:"
+ "buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:"
+ "buildTripSegmentsFromTripSegmentFeaturesList:startVisitLocation:stopVisitLocation:transitionStartStopLocations:"
+ "calculatePredictability:priorVisits:timeWindowHalfWidth:"
+ "calendarEventsCount"
+ "calendarEventsLatency"
+ "calendarEventsSuccess"
+ "checkIMessageAccountEnabledWithHandler:"
+ "chunkLocationsCloseEnoughToCompound,distance check fail,%{public}0.2f,frmLoc,%{sensitive}0.7f,%{sensitive}0.7f,toLoc,%{sensitive}0.7f,%{sensitive}0.7f"
+ "chunkLocationsCloseEnoughToCompound,distance check ok,%{public}0.2f,frmLoc,%{sensitive}0.7f,%{sensitive}0.7f,toLoc,%{sensitive}0.7f,%{sensitive}0.7f"
+ "chunkLocationsCloseEnoughToCompound,no loc for dateInterval,%@"
+ "chunkLocationsCloseEnoughToCompound:stitchDateEndInterval:"
+ "collectMetricsForSubmittedUserCuration:submissionResult:"
+ "collectUserCurationCountMetricsWithUserCurationStore:error:"
+ "collecting submission metrics for user curation, %@"
+ "collecting user curation count metrics"
+ "compoundedVisitIntervals"
+ "correctPrediction"
+ "correctPredictionCount"
+ "correctTruth"
+ "countKeyForFeature:"
+ "createAndStoreCurationWithEntryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:handler:"
+ "curationDuration"
+ "curationWhereOriginal"
+ "currentAccountStatus"
+ "currentTimeCFAbsolute"
+ "currentTimeZoneAbbreviation"
+ "currentVisitType"
+ "dailyBlueSkyMetrics"
+ "dailyCount"
+ "dailyInferenceCount"
+ "dailyInferenceLatency"
+ "dailyInferenceMemoryUsage"
+ "dailyInferenceTriggerReasonClientRegistration"
+ "dailyInferenceTriggerReasonDominantMotionCount"
+ "dailyInferenceTriggerReasonNavigationNotificationCount"
+ "dailyInferenceTriggerReasonPeriodicTriggerCount"
+ "dailyInferenceTriggerReasonSingleShotCount"
+ "dailyInferenceTriggerReasonUnknownCount"
+ "dailyInferenceTriggerReasonVisitNotificationCount"
+ "elapsedTimeBeforeCuration"
+ "f40@0:8@16@24d32"
+ "failureReason"
+ "featureExtractorReason"
+ "fetchCurrentDeviceWithHandler:"
+ "fetchLearnedLocationOfInterestForVisitIdentifier:outLearnedVisitLocation:"
+ "fetchPredictedContextAndRequestDateWithOptions:handler:"
+ "fetchStoredUserCurationWithIdentifier:handler:"
+ "fetchVisitsOverlappingDate:handler:"
+ "fetched authorized location, error, %@, zdrCount, %lu, fullCount, %lu"
+ "frequentLoi"
+ "getAllContextsInOneArray:"
+ "getEarliestDate:"
+ "getFrequentLoiFromCount:"
+ "getHighProbabilityPredictedContexts:"
+ "getPredictedContextLocationFromDictionary:"
+ "getPredictionsForInterval:completion:"
+ "getRequestCountByInferenceTriggerReasonForRequests:"
+ "getRequestsForInterval:completion:"
+ "getStoredLocationWithOptions:"
+ "getTotalInferenceLatencyForRequests:"
+ "getTotalMemoryFootprintForRequests:"
+ "getVisitsForInterval:completion:"
+ "hasExceeded"
+ "highestConfidence"
+ "highestProbability"
+ "historyCount"
+ "homeKitHomesLatency"
+ "homeKitHomesSuccess"
+ "idOfCurrentlyProcessingChunk"
+ "indexSet"
+ "initForDefaultMetric"
+ "initWithAscending:confidence:dateInterval:labelVisit:limit:sources:redact:"
+ "initWithCompanionLinkClient:dailyBlueSkyMetrics:defaultsManager:"
+ "initWithIdentifier:submissionDate:expirationDate:entryDate:exitDate:visitIdentifier:originalLabel:curatedLabel:"
+ "initWithLearnedLocationManager:visitManager:locationManager:eventManager:navigationManager:mapsSupportManager:motionActivityManager:vehicleLocationProvider:visitConsolidator:healthKitManager:homeKitManager:tripLocationPropagator:metricsManager:"
+ "initWithManagedConfiguration:predictedContextStore:defaultsManager:visitConsolidator:"
+ "initWithVisits:redactionDetails:"
+ "isCorrectPrediction:forTruthVisits:matchingVisit:"
+ "isCorrectTruth:forPredictions:"
+ "isVisitCompoundingEnabled"
+ "isWithinMidnightBoundary:targetDay:interval:"
+ "kRTBluePOIQueryEventHasResultWiFiChannel%ld"
+ "killProcessingWithID:"
+ "lastPlaceInferenceSyncAttemptDate"
+ "lastVisitSyncAttemptDate"
+ "latencyKeyForFeature:"
+ "leadTime"
+ "locationLatency"
+ "locationOfInterestLatency"
+ "locationsCount"
+ "locationsOfInterestSuccess"
+ "locationsSuccess"
+ "logFeatureExtractionForFeature:stimulationDate:featureArray:success:toDict:"
+ "lookbackWindow"
+ "mapsActiveNavigationCount"
+ "mapsActiveNavigationLatency"
+ "mapsActiveNavigationSuccess"
+ "mapsHistoricalNavigationCount"
+ "mapsHistoricalNavigationLatency"
+ "mapsHistoricalNavigationSuccess"
+ "mapsViewedPlacesLatency"
+ "mapsViewedPlacesSuccess"
+ "maxAdjacentVisitsToCompound"
+ "maximumInterTripSegmentDistanceAllowedForCompoundRoute"
+ "metricCodeForFeatureExtractorOperationType:"
+ "metricDictionary"
+ "metricsKey"
+ "mirroringManager:exceededHistoryType:count:limit:hasExceeded:"
+ "monthlyCount"
+ "motionActivitiesCount"
+ "motionActivitiesLatency"
+ "motionActivitiesSuccess"
+ "muteAutoPauseForWorkoutType:mute:"
+ "numQualifiedPlaceInferences"
+ "numQualifiedPlaceInferencesSent"
+ "numQualifiedVisits"
+ "numQualifiedVisitsOverLimit"
+ "numQualifiedVisitsSent"
+ "numSyncsRequiring10SecWait"
+ "numSyncsRequiring1MinWait"
+ "numSyncsRequiring20SecWait"
+ "numSyncsRequiring2MinWait"
+ "numSyncsRequiring30SecWait"
+ "numSyncsRequiring5MinPlusWait"
+ "numSyncsRequiring5MinWait"
+ "numSyncsRequiringNoWait"
+ "obfuscatedVisitDateIntervalForEntryDate:previousObfuscatedVisitEntryDate:"
+ "originalLabel"
+ "parkedCarCount"
+ "parkedCarLatency"
+ "parkedCarSuccess"
+ "predictability"
+ "prepareAndSubmitDailyInferenceEventMetrics:"
+ "prepareAndSubmitPredictionEventMetrics:yesterdayVisits:"
+ "prepareAndSubmitTrainingEventMetrics:"
+ "prepareAndSubmitTruthEventMetrics:yesterdayVisits:yesterdayPredictions:"
+ "prepareDailyInferenceEventMetrics:"
+ "preparePredictionEventMetric:correctPrediction:matchingVisit:"
+ "prepareTrainingEventMetric:"
+ "prepareTruthEventMetric:predictability:truePositiveCount:highestProbability:frequentLoi:leadTime:"
+ "propagatedLocationsCount"
+ "propagatedLocationsLatency"
+ "propagatedLocationsSuccess"
+ "q32@0:8@\"RTPersistenceStore\"16@\"NSSet\"24"
+ "q32@0:8q16@24"
+ "redact must be set (in %s:%d)"
+ "redactedForAuthorizedLocation"
+ "redactedForCategory"
+ "redactedForConfidence"
+ "redactedForPlaceType"
+ "redactedForRegion"
+ "redactedVisitCount"
+ "redactedVisitCount, %ld, badAge, %ld, badCategory, %ld, badConfidence, %ld, badPlaceType, %ld, badRegion, %ld"
+ "redactionDetails"
+ "redactionProportion"
+ "removeAllIndexes"
+ "replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:"
+ "setCurrentAccountStatus:"
+ "setCurrentTimeZoneAbbreviation:"
+ "setCurrentVisitType:"
+ "setDailyBlueSkyMetrics:"
+ "setIdOfCurrentlyProcessingChunk:"
+ "setLastPlaceInferenceSyncAttemptDate:"
+ "setLastVisitSyncAttemptDate:"
+ "setOriginalLabel:"
+ "setRedactedForAuthorizedLocation:"
+ "setRedactedForCategory:"
+ "setRedactedForConfidence:"
+ "setRedactedForPlaceType:"
+ "setRedactedForRegion:"
+ "setRedactionProportion:"
+ "setStartEndRoadCountBufferZonePercentage:"
+ "setStationaryStartDate:"
+ "setVisitsConsideredCount:"
+ "setVisitsRedactedForAge:"
+ "setVisitsRedactedForAuthorizedLocation:"
+ "setVisitsRedactedForCategory:"
+ "setVisitsRedactedForConfidence:"
+ "setVisitsRedactedForPlaceType:"
+ "setVisitsRedactedForRegion:"
+ "sortReconciledVisitsByMapItemQuality:"
+ "startEndRoadCountBufferZonePercentage"
+ "stationaryStartDate"
+ "submitFeatureExtractorMetrics:"
+ "successKeyForFeature:"
+ "totalLatency"
+ "trainingResultMask"
+ "transitionsCount"
+ "transitionsLatency"
+ "transitionsSuccess"
+ "truePositiveCount"
+ "tryCompoundingVisits"
+ "tryCompoundingVisits,_areTwoVisitsSame,firstLOI,%@,secondLOI,%@,firstVisitLoc,%{sensitive}@,secondVisitLoc,%{sensitive}@,isSameLOI,%{public}d,isSameLocation,%{public}d"
+ "tryCompoundingVisits,applied,visit compounded,%@,visit duration,%{public}lu,tId,%{public}ld"
+ "tryCompoundingVisits,malformed transition,_tripSegmentTransitions[%{public}ld],start/stop dates,%@,%@"
+ "tryCompoundingVisits,motion,tId,%{public}ld,motion modes,%{public}lu,%{public}lu,stop,%@,next start,%@"
+ "tryCompoundingVisits,not applicable,loopback check not cleared,tId,%{public}ld,loopback,%{public}d"
+ "tryCompoundingVisits,not applicable,maxAdjacentVisitsToCompound limit reached,,tId,%{public}ld,max,%{public}ld,current,%{public}lu"
+ "tryCompoundingVisits,not applicable,visit duration,%{public}lu > compounding threshold,%{public}lu"
+ "tryCompoundingVisits,tId,%{public}ld,count,%{public}lu"
+ "user curation daily metrics submission, start"
+ "user curation daily metrics submission, success, %@, error, %@"
+ "v24@?0@\"RTVisitConsolidatorResult\"8@\"NSError\"16"
+ "v32@?0@\"NSDate\"8@\"NSArray\"16^B24"
+ "v52@0:8@\"RTPersistenceMirroringManager\"16Q24Q32Q40B48"
+ "v52@0:8@16Q24Q32Q40B48"
+ "validating current AppleIDs (%{sensitive}@) against appleIDs (%{sensitive}@)"
+ "visitIntervalsForVisits:place:"
+ "visitLatency"
+ "visitStartDateRangeFromObfuscatedStartDate:"
+ "visitSuccess"
+ "visits:withLoiIdentifier:"
+ "visitsConsideredCount"
+ "visitsPredatingCurrentDeviceFromVisits:"
+ "visitsRedactedForAge"
+ "visitsRedactedForAuthorizedLocation"
+ "visitsRedactedForCategory"
+ "visitsRedactedForConfidence"
+ "visitsRedactedForPlaceType"
+ "visitsRedactedForRegion"
+ "visitsWithExit:beforeDate:"
+ "visitsWithExit:dateInterval:"
+ "weeklyCount"
+ "workoutsCount"
+ "workoutsLatency"
+ "workoutsSuccess"
- "%@, %@, Finished training, success, %@, was deferred, %@, error, %@"
- "%@, %@, Overring trainPolicy from, %@, to %@, because areMaxTrainAttemptsWithinLastDayReached, %@"
- "%@, %@, error occurred while creating and storing LOI, %@"
- "%@, %@, error occurred while fetching place for curation label, %@"
- "%@, %@, fetchVisitsOverlappingDateInterval returned no visits, exiting early"
- "%@, %@, fetched %lu visits overlapping user curation"
- "%@, %@, idx, %lu, predictionEventMetrics, %@"
- "%@, %@, new LOI created and stored successfully for curation label"
- "%@, %@, no label associated with curation, exiting early"
- "%@, %@, no pre-existing location of interest found for curation label, creating one"
- "%@, %@, pre-existing location of interest was found and will be used to curate visits, %@"
- "%@, %@, user curation submitted but not applied to LOI graph, %@"
- "%@,_processNextVisitTransition,count,%{public}lu,fetchedNewTransitions,%{public}d,successfulTransitionsSinceLastClustering,%{public}d,learnClusters,starting."
- "%@,learnClusters,starting."
- "%@:%@,numberOfSetupLocs,%{public}d,zdrSetupEntryWithOldestEntryTime,%{public}@,zdrSetupEntryWithOldestValidLocation,%{public}@"
- "+[RTVisitConsolidator redactVisits:authorizedLocations:bluePOICategoryDenylist:]"
- ".C"
- "09:59:42"
- "B32@0:8@\"RTPersistenceStore\"16@\"NSSet\"24"
- "B40@0:8Q16@24Q32"
- "Defer TripSegmentAndClusterProcessing,%d"
- "Distance from place to visit location exceeded threshold. Skipping visit interval."
- "Error was issued during fetching visits from store. Error: %@"
- "Jun 14 2025"
- "RTDefaultsLearnedRoutesFetchSPITopListClusterMaxNumKey"
- "RTPredictedContextDailyMetricsManager"
- "RTTripSegmentProvider: buildTripSegmentsForOneLearnedTransitionWithIndex, trainMode, %lu"
- "RTTripSegmentProvider: failed in motion activity fetching,fetchError,%@,semaError,%@"
- "RTTripSegmentProvider: fetch endpoints for transition identifier, %@, _transitionStartLocation, %{sensitive}@, _transitionStopLocation, %{sensitive}@"
- "RTTripSegmentProvider: fetchedMotionActivity,transitionIndex,%tu,rawActivityCount,%tu,rawActivityIndex,%tu,thisRawActivity,%@"
- "RTTripSegmentProvider: fetchedMotionActivitySummary,transitionIndex,%tu,countOfFetchedActivities,%tu"
- "RTTripSegmentProvider: filteredMotionActivity,transitionIndex,%tu,activityCount,%tu,activityIndex,%tu,thisFilteredActivity,%@"
- "RTTripSegmentProvider: filteredMotionActivitySummary,transitionIndex,%tu,activityCount,%tu"
- "RTTripSegmentProvider: skipThisTransition,%tu,lack of real mode of transportation,predominantType,%tu"
- "RTTripSegmentProvider: unable to fetch endpoints for transition identifier, %@"
- "RTTripSegmentProvider:%@"
- "RTTripSegmentProvider:TripSegment already exists in store for date interval %@, and configuration set to reprocess trip segment data."
- "RTTripSegmentProvider:TripSegment already exists in store for date interval %@, and configuration set to skip reprocessing trip segment data."
- "RTTripSegmentProvider:_processOneVisitTransition completed processing one Transition,isOccupied,%d,allowReprocessTransition,%d"
- "RTTripSegmentProvider:generatedChunks,transitionIndex,%tu,activityCount,%tu,chunkIndex,%tu,chunkCount,%tu,thisChunk,%@"
- "RTTripSegmentProvider:generatedChunksSummary,transitionIndex,%tu,chunkCount,%tu"
- "RTTripSegmentProvider:transition processing disallowed based on region check,%@,startCoordinate,%{sensitive}.7lf,%{sensitive}.7lf,stopCoordinate,%{sensitive}.7lf,%{sensitive}.7lf"
- "RTTripSegmentProvider:unable to verify region,coordinate not available,transition processing disallowed,%@"
- "RTTripSegmentTransitionPreprocessor: fetchLearnedLocationOfInterestForVisitIdentifier fetched learnedLocation: %{sensitive}@"
- "T@\"CLLocation\",&,N,V_location"
- "T@\"NSDate\",&,N,V_currentDate"
- "T@\"NSDate\",&,N,V_date"
- "T@\"NSDate\",&,N,V_sessionEndDate"
- "T@\"NSDate\",&,N,V_sessionStartDate"
- "T@\"NSMutableArray\",&,N,V_mockLocations"
- "T@\"NSMutableArray\",&,N,V_mockMotionActivities"
- "T@\"NSMutableArray\",&,N,V_replayEvents"
- "T@\"NSMutableArray\",&,N,V_timerStack"
- "T@\"NSMutableDictionary\",&,N,V_defaults"
- "T@\"NSMutableDictionary\",&,N,V_locationToEtaDictionary"
- "T@\"NSMutableDictionary\",&,N,V_results"
- "T@\"NSString\",&,N,V_resultsPath"
- "T@\"NSUUID\",&,N,V_currentDeviceIdentifier"
- "T@\"NSUUID\",&,N,V_pedometerSubscriptionUUID"
- "T@\"SMSessionManagerState\",&,N,V_state"
- "TB,N,V_shouldDeferTripSegmentAndClusterProcessing"
- "Unexpected - transition pointer is nil"
- "Visit interval end date exceeded earliest start date. Skipping visit interval."
- "_createAndStoreLOIForPlace:handler:"
- "_deferTripSegmentAndClusterProcessing:"
- "_extractFeatures:lookbackDurations:outError:"
- "_maximumInterTripSegmentDistanceAllowedForCompoundRoute"
- "_pedometerSubscriptionUUID"
- "_processTrainingEvent"
- "_replayEvents"
- "_setupPersistenceAfterConfigurationChange:cloudSyncAuthorization:account:"
- "a backup already exists at the path %@ or is recent (%@, %@), skipping"
- "buildTripSegmentsForOneLearnedTransitionWithIndex:inTransitions:trainMode:"
- "cloud sync state disabled"
- "cloud sync state enabled"
- "cloud sync state unknown"
- "error fetching authorized locations, %@"
- "failed to save wifi access points with error, %@"
- "featureExtractorSummary:featureDescription:firstFeatureItemDescription:lastFeatureItemDescription:stimulationDate:"
- "fetchLearnedLocationOfInterestForVisitIdentifier:"
- "fetched authorized location, error, %@,%lu,%lu"
- "initWithCompanionLinkClient:"
- "initWithLearnedLocationManager:visitManager:locationManager:eventManager:navigationManager:mapsSupportManager:motionActivityManager:vehicleLocationProvider:visitConsolidator:healthKitManager:homeKitManager:tripLocationPropagator:"
- "initWithManagedConfiguration:predictedContextStore:defaultsManager:"
- "mirroringManager:exceededHistoryType:count:limit:"
- "pedometerSubscriptionUUID"
- "place location, %{sensitive}@, visit location, %{sensitive}@, distance from place to visit location, %.3f, visit interval start date, %@, visit interval end date, %@, earliestStartDate, %@, latestEndDate, %@, error, %@"
- "prepareAndSubmitPredictionEventMetrics:"
- "prepareAndSubmitTrainingEventMetrics"
- "preparePredictionEventMetric:inferenceStartDate:inferenceTriggerReason:"
- "prepareTrainingEventMetric"
- "replayEvents"
- "setDefaults:"
- "setLocationToEtaDictionary:"
- "setMockLocations:"
- "setMockMotionActivities:"
- "setPedometerSubscriptionUUID:"
- "setReplayEvents:"
- "setResults:"
- "setTimerStack:"
- "submitMetricsForDailyPredictions:data:error:"
- "trainingSuccess"
- "v48@0:8@\"RTPersistenceMirroringManager\"16Q24Q32Q40"
- "v56@0:8Q16@24@32@40@48"
- "visits count, %lu, local device visits count, %lu, place, %{sensitive}@"
- "\xc1"

```
