## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1053.0.1.0.0
-  __TEXT.__text: 0x5de538
-  __TEXT.__auth_stubs: 0x2180
-  __TEXT.__objc_methlist: 0x30a30
-  __TEXT.__const: 0x4608
+1057.0.0.0.0
+  __TEXT.__text: 0x5e57d0
+  __TEXT.__auth_stubs: 0x2190
+  __TEXT.__objc_methlist: 0x30b60
+  __TEXT.__const: 0x4640
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x7440e
-  __TEXT.__cstring: 0x448f8
+  __TEXT.__oslogstring: 0x754a8
+  __TEXT.__cstring: 0x44b17
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c

   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x27b98
+  __TEXT.__gcc_except_tab: 0x282d8
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xdab0
+  __TEXT.__unwind_info: 0xdb58
   __TEXT.__eh_frame: 0x390
-  __TEXT.__objc_classname: 0x57fa
-  __TEXT.__objc_methname: 0x90440
-  __TEXT.__objc_methtype: 0xcec1
-  __TEXT.__objc_stubs: 0x55100
-  __DATA_CONST.__got: 0x3088
-  __DATA_CONST.__const: 0xf558
-  __DATA_CONST.__objc_classlist: 0x1520
+  __TEXT.__objc_classname: 0x580a
+  __TEXT.__objc_methname: 0x90a43
+  __TEXT.__objc_methtype: 0xcedb
+  __TEXT.__objc_stubs: 0x554a0
+  __DATA_CONST.__got: 0x30b0
+  __DATA_CONST.__const: 0xf608
+  __DATA_CONST.__objc_classlist: 0x1528
   __DATA_CONST.__objc_catlist: 0x3a8
   __DATA_CONST.__objc_protolist: 0x340
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19118
+  __DATA_CONST.__objc_selrefs: 0x19228
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x1180
-  __DATA_CONST.__objc_arraydata: 0x2990
-  __AUTH_CONST.__auth_got: 0x10d0
-  __AUTH_CONST.__const: 0x3260
-  __AUTH_CONST.__cfstring: 0x283c0
-  __AUTH_CONST.__objc_const: 0x50128
-  __AUTH_CONST.__objc_intobj: 0x4518
-  __AUTH_CONST.__objc_arrayobj: 0xd98
-  __AUTH_CONST.__objc_doubleobj: 0xab0
+  __DATA_CONST.__objc_arraydata: 0x2a20
+  __AUTH_CONST.__auth_got: 0x10d8
+  __AUTH_CONST.__const: 0x3220
+  __AUTH_CONST.__cfstring: 0x28600
+  __AUTH_CONST.__objc_const: 0x502b0
+  __AUTH_CONST.__objc_intobj: 0x45d8
+  __AUTH_CONST.__objc_arrayobj: 0xe70
+  __AUTH_CONST.__objc_doubleobj: 0xaf0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x2b68
-  __DATA.__objc_ivar: 0x2534
-  __DATA.__data: 0x2b90
+  __AUTH.__objc_data: 0x2bb8
+  __DATA.__objc_ivar: 0x2544
+  __DATA.__data: 0x2b98
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_ivar: 0x1144
   __DATA_DIRTY.__objc_data: 0xa890

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9AE2205F-F490-3AF7-8569-7C57FD99BA3A
-  Functions: 20037
-  Symbols:   64703
-  CStrings:  39811
+  UUID: BE12BFF0-0DD8-3B24-9D5A-D07B2A308DEB
+  Functions: 20070
+  Symbols:   64820
+  CStrings:  39934
 
Symbols:
+ +[RTBluePOIHelper insideBusinessHours:date:timeZone:]
+ +[RTBluePOIHelper shouldFilterByBusinessHours:]
+ +[RTBluePOIHelper weightBasedOnBusinessHours:startDate:endDate:timeZone:metrics:]
+ +[RTBluePOIHelper weightBasedOnDurationWithStartDate:endDate:timeZone:poiCategory:]
+ +[RTPredictedContextManager _dataCollectionDefaultLookbackDurations]
+ +[RTPredictedContextManager _defaultLookbackDurations]
+ +[RTPredictedContextManager _inferenceDefaultLookbackDurations]
+ +[RTTripClusterScheduleStore _predicateForClusterAndTimeID:timeID:]
+ +[RTUserCurationMetrics collectMetricsForAppliedUserCuration:curatedVisit:learnedLocationStore:distanceCalculator:error:]
+ +[RTVisitConsolidator consolidateHindsightVisits:constantMonitorVisits:sortDescriptor:filterPairedVisitEntries:]
+ +[RTVisitConsolidator filterConstantMonitorVisits:]
+ -[PCPMapsActiveNavigation(RTFeatureExtractorExtension) initWithRouteSummary:loiIdentifier:]
+ -[RTBluePOIMonitorEnabler _onVisitManagerNotification:]
+ -[RTBluePOIMonitorEnabler onVisitManagerNotification:]
+ -[RTFeatureExtractor _extractFeatures:operationType:lookbackIntervals:outError:]
+ -[RTFeatureExtractor _fetchLocationOfInterestForMapItem:error:]
+ -[RTFeatureExtractor _getLocationsOfInterestWithDateInterval:outError:]
+ -[RTFeatureExtractor extractFeaturesWithLookbackIntervals:operationType:outError:]
+ -[RTLearnedLocationEngine _mapItemsWithUserCurationCorrection:error:]
+ -[RTMapItemProviderBluePOI _timeZoneFromLocation:]
+ -[RTPredictedContextManager _lookbackIntervalsWithDefaults:]
+ -[RTTripClusterManager _deleteAllTripClusterDataForClusterID:]
+ -[RTTripClusterManager _updateSPIMetricReasonCodeAndSubmit:]
+ -[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:]
+ -[RTTripClusterProcessorOptions familiarityDecayFactor]
+ -[RTTripClusterProcessorOptions maxClusterTraversalCount]
+ -[RTTripClusterProcessorOptions maxTripSegmentDistanceForClustering]
+ -[RTTripClusterProcessorOptions maxTripSegmentTimeForClustering]
+ -[RTTripClusterProcessorOptions setFamiliarityDecayFactor:]
+ -[RTTripClusterProcessorOptions setMaxClusterTraversalCount:]
+ -[RTTripClusterProcessorOptions setMaxTripSegmentDistanceForClustering:]
+ -[RTTripClusterProcessorOptions setMaxTripSegmentTimeForClustering:]
+ -[RTTripSegmentProvider _isMatchingODPair:tripCluster2:]
+ -[RTTripSegmentTransitionPreprocessor applyRule_largeDistanceTransitionsAreInvalid_ForTransitionAtIndex:]
+ GCC_except_table149
+ GCC_except_table151
+ GCC_except_table156
+ GCC_except_table163
+ GCC_except_table206
+ GCC_except_table209
+ GCC_except_table224
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table249
+ GCC_except_table252
+ GCC_except_table254
+ GCC_except_table258
+ GCC_except_table278
+ GCC_except_table285
+ GCC_except_table290
+ GCC_except_table296
+ GCC_except_table302
+ GCC_except_table307
+ GCC_except_table309
+ GCC_except_table74
+ _GEOPOICategoryGasStation
+ _GEOPOICategoryHotel
+ _GEOPOICategoryRestaurant
+ _OBJC_CLASS_$_CLGeocoder
+ _OBJC_CLASS_$_RTBluePOIHelper
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._familiarityDecayFactor
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._maxClusterTraversalCount
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._maxTripSegmentDistanceForClustering
+ _OBJC_IVAR_$_RTTripClusterProcessorOptions._maxTripSegmentTimeForClustering
+ _OBJC_METACLASS_$_RTBluePOIHelper
+ _RTAnalyticsEventUserCurationApplication
+ _RTBluePOIErrorDomain
+ __OBJC_$_CLASS_METHODS_RTBluePOIHelper
+ __OBJC_CLASS_RO_$_RTBluePOIHelper
+ __OBJC_METACLASS_RO_$_RTBluePOIHelper
+ ___101-[RTBluePOIMonitor _updateLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:error:]_block_invoke
+ ___101-[RTBluePOIMonitor _updateLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:error:]_block_invoke_2
+ ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.406
+ ___105-[RTTripSegmentTransitionPreprocessor applyRule_largeDistanceTransitionsAreInvalid_ForTransitionAtIndex:]_block_invoke
+ ___105-[RTTripSegmentTransitionPreprocessor applyRule_largeDistanceTransitionsAreInvalid_ForTransitionAtIndex:]_block_invoke_2
+ ___110-[RTTripSegmentProvider buildTinySegmentArrayForTransitionWithIndex:withinDateInterval:fromActivity:uuidType:]_block_invoke.360
+ ___112-[RTTripSegmentTransitionPreprocessor fetchLearnedLocationOfInterestForVisitIdentifier:outLearnedVisitLocation:]_block_invoke.190
+ ___121+[RTUserCurationMetrics collectMetricsForAppliedUserCuration:curatedVisit:learnedLocationStore:distanceCalculator:error:]_block_invoke
+ ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke.90
+ ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke_2
+ ___159-[RTTripSegmentProvider buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:]_block_invoke.399
+ ___159-[RTTripSegmentProvider buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:]_block_invoke.403
+ ___229-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:]_block_invoke
+ ___229-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:]_block_invoke.288
+ ___229-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:]_block_invoke.289
+ ___229-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:]_block_invoke_2
+ ___25-[RTDaemonClient restore]_block_invoke.742
+ ___27-[RTLifeCycleManager _exit]_block_invoke.716
+ ___27-[RTLifeCycleManager _exit]_block_invoke.722
+ ___27-[RTLifeCycleManager _exit]_block_invoke.724
+ ___27-[RTLifeCycleManager _exit]_block_invoke_2.723
+ ___28-[RTHealthKitManager _setup]_block_invoke.621
+ ___28-[RTLifeCycleManager _start]_block_invoke.701
+ ___28-[RTLifeCycleManager _start]_block_invoke.707
+ ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.188
+ ___41-[RTAssetManager _downloadAsset:handler:]_block_invoke.359
+ ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.723
+ ___43-[RTPredictedContextManager _storeRequest:]_block_invoke.478
+ ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.191
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.152
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.154
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.156
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.158
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.160
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.153
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.155
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.157
+ ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.159
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.172
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.181
+ ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.184
+ ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.769
+ ___52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.686
+ ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.471
+ ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.474
+ ___54-[RTBluePOIMonitorEnabler onVisitManagerNotification:]_block_invoke
+ ___54-[RTClusterLearnedRouteMetrics submitToCoreAnalytics:]_block_invoke.905
+ ___54-[RTClusterLearnedRouteMetrics submitToCoreAnalytics:]_block_invoke_2.906
+ ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.667
+ ___55-[RTBluePOIMonitorEnabler _onVisitManagerNotification:]_block_invoke
+ ___55-[RTBluePOIMonitorEnabler _onVisitManagerNotification:]_block_invoke_2
+ ___55-[RTLearnedLocationEngine trainForReason:mode:handler:]_block_invoke_2
+ ___55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.421
+ ___55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.422
+ ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.376
+ ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.382
+ ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.385
+ ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.389
+ ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.391
+ ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.129
+ ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.131
+ ___57-[SMSessionMetricManager _gatherSessionDestinationStats:]_block_invoke.678
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.486
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.493
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.497
+ ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.829
+ ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.578
+ ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.48
+ ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.53
+ ___62-[RTDaemonClientInternal connection:handleInvocation:isReply:]_block_invoke.491
+ ___63-[RTFeatureExtractor _fetchLocationOfInterestForMapItem:error:]_block_invoke
+ ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.686
+ ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.457
+ ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.458
+ ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.459
+ ___65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.203
+ ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.734
+ ___69-[RTDaemonClient remoteStatusRegistrar:didReceiveRemoteStatus:error:]_block_invoke.770
+ ___69-[RTLearnedLocationEngine _mapItemsWithUserCurationCorrection:error:]_block_invoke
+ ___69-[RTTripSegmentTransitionPreprocessor appendTransitionToCurrentVisit]_block_invoke.198
+ ___69-[RTTripSegmentTransitionPreprocessor appendTransitionToCurrentVisit]_block_invoke.199
+ ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.761
+ ___71-[RTFeatureExtractor _getLocationsOfInterestWithDateInterval:outError:]_block_invoke
+ ___71-[RTFeatureExtractor _getLocationsOfInterestWithDateInterval:outError:]_block_invoke.418
+ ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.509
+ ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.746
+ ___72-[RTTripSegmentProvider addToTransitionLocationsBuffer:forDateInterval:]_block_invoke.363
+ ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.551
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.460
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.464
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.475
+ ___76-[RTAssetManager initWithDefaultsManager:assetProcessor:xpcActivityManager:]_block_invoke.298
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.729
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.730
+ ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.605
+ ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke.214
+ ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke.217
+ ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke_2
+ ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.765
+ ___79-[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]_block_invoke.798
+ ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.718
+ ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.737
+ ___82-[RTFeatureExtractor extractFeaturesWithLookbackIntervals:operationType:outError:]_block_invoke
+ ___83-[RTDaemonClient predictedContextRegistrar:didReceivePredictedContextResult:error:]_block_invoke.809
+ ___85-[RTTripSegmentTransitionPreprocessor fetchEndpointCLLocationForTransition:atOrigin:]_block_invoke.213
+ ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.673
+ ___97-[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngineWithPlaceStats:dateInterval:]_block_invoke.417
+ ___block_descriptor_105_e8_32s40s48s56s64bs72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
+ ___block_descriptor_48_e8_32s40r_e30_v24?0"NSNumber"8"NSError"16lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e38_"RTInferredMapItem"16?0"RTMapItem"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e38_"RTInferredMapItem"16?0"RTMapItem"8ls32l8s40l8s48l8r56l8
+ ___block_descriptor_68_e8_32s40s48s56s_e33_v16?0"CLTripSegmentOutputData"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48r56r_e49_v24?0"RTLearnedLocationOfInterest"8"NSError"16lr48l8r56l8s32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56r_e29_v24?0"NSArray"8"NSError"16ls32l8r56l8s40l8s48l8
+ ___block_descriptor_96_e8_32s40s48s56s64r72r_e29_v24?0"NSArray"8"NSError"16lr64l8r72l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.133
+ ___block_literal_global.1379
+ ___block_literal_global.1383
+ ___block_literal_global.174
+ ___block_literal_global.176
+ ___block_literal_global.178
+ ___block_literal_global.186
+ ___block_literal_global.193
+ ___block_literal_global.209
+ ___block_literal_global.238
+ ___block_literal_global.240
+ ___block_literal_global.374
+ ___block_literal_global.427
+ ___block_literal_global.452
+ ___block_literal_global.453
+ ___block_literal_global.554
+ ___block_literal_global.566
+ ___block_literal_global.604
+ ___block_literal_global.643
+ ___block_literal_global.688
+ ___block_literal_global.700
+ ___block_literal_global.704
+ ___block_literal_global.709
+ ___block_literal_global.727
+ ___block_literal_global.732
+ ___block_literal_global.736
+ ___block_literal_global.744
+ ___block_literal_global.89
+ ___block_literal_global.92
+ ___block_literal_global.968
+ _kRTBluePOIConfidenceAdjustmentEventHasBusinessHours
+ _kRTBluePOIConfidenceAdjustmentEventInsideBusinessHours
+ _kRTPredictedContextMetricsKeyLocationOfInterestType
+ _objc_msgSend$_dataCollectionDefaultLookbackDurations
+ _objc_msgSend$_deleteAllTripClusterDataForClusterID:
+ _objc_msgSend$_extractFeatures:operationType:lookbackIntervals:outError:
+ _objc_msgSend$_fetchLocationOfInterestForMapItem:error:
+ _objc_msgSend$_getLocationsOfInterestWithDateInterval:outError:
+ _objc_msgSend$_inferenceDefaultLookbackDurations
+ _objc_msgSend$_isMatchingODPair:tripCluster2:
+ _objc_msgSend$_lookbackIntervalsWithDefaults:
+ _objc_msgSend$_mapItemsWithUserCurationCorrection:error:
+ _objc_msgSend$_predicateForClusterAndTimeID:timeID:
+ _objc_msgSend$_timeZoneAtLocation:
+ _objc_msgSend$_timeZoneFromLocation:
+ _objc_msgSend$_updateSPIMetricReasonCodeAndSubmit:
+ _objc_msgSend$collectMetricsForAppliedUserCuration:curatedVisit:learnedLocationStore:distanceCalculator:error:
+ _objc_msgSend$consolidateHindsightVisits:constantMonitorVisits:sortDescriptor:filterPairedVisitEntries:
+ _objc_msgSend$contactIncludingImage:
+ _objc_msgSend$dateOfMostRecentTrip
+ _objc_msgSend$extractFeaturesWithLookbackIntervals:operationType:outError:
+ _objc_msgSend$familiarityDecayFactor
+ _objc_msgSend$filterConstantMonitorVisits:
+ _objc_msgSend$hoursType
+ _objc_msgSend$initWithDateInterval:predictionSources:probability:sourceBundleIdentifier:workoutActivityType:workoutLocationType:
+ _objc_msgSend$initWithRouteSummary:loiIdentifier:
+ _objc_msgSend$insideBusinessHours:date:timeZone:
+ _objc_msgSend$localTimeIntervals
+ _objc_msgSend$locationOfInterestType
+ _objc_msgSend$maxClusterTraversalCount
+ _objc_msgSend$maxTripSegmentDistanceForClustering
+ _objc_msgSend$maxTripSegmentTimeForClustering
+ _objc_msgSend$placeDailyNormalizedHours
+ _objc_msgSend$setDidSPIReturned3Routes:
+ _objc_msgSend$setLocationOfInterestType:
+ _objc_msgSend$setWorkoutLocationType:
+ _objc_msgSend$shouldFilterByBusinessHours:
+ _objc_msgSend$spiStatMetrics
+ _objc_msgSend$updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:
+ _objc_msgSend$weightBasedOnDurationWithStartDate:endDate:timeZone:poiCategory:
+ _objc_msgSend$workoutLocationType
+ _rand
- +[RTVisitConsolidator consolidateHindsightVisits:constantMonitorVisits:sortDescriptor:]
- +[RTVisitConsolidator removeConstantMonitorVisitEntriesWithExits:]
- -[PCPMapsActiveNavigation(RTFeatureExtractorExtension) initWithRouteSummary:]
- -[RTFeatureExtractor _extractFeatures:operationType:lookbackDurations:outError:]
- -[RTFeatureExtractor _getLocationsOfInterestWithError:]
- -[RTFeatureExtractor extractFeaturesWithLookbackDurations:operationType:outError:]
- -[RTPredictedContextManager _defaultLookbackDurations]
- -[RTPredictedContextManager _lookbackDurationsForDataCollection]
- -[RTPredictedContextManager _lookbackDurationsWithDefaults:]
- -[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:]
- GCC_except_table145
- GCC_except_table159
- GCC_except_table166
- GCC_except_table187
- GCC_except_table205
- GCC_except_table223
- GCC_except_table234
- GCC_except_table248
- GCC_except_table251
- GCC_except_table253
- GCC_except_table274
- GCC_except_table277
- GCC_except_table284
- GCC_except_table289
- GCC_except_table291
- GCC_except_table293
- GCC_except_table295
- GCC_except_table301
- GCC_except_table86
- ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.409
- ___110-[RTTripSegmentProvider buildTinySegmentArrayForTransitionWithIndex:withinDateInterval:fromActivity:uuidType:]_block_invoke.359
- ___112-[RTTripSegmentTransitionPreprocessor fetchLearnedLocationOfInterestForVisitIdentifier:outLearnedVisitLocation:]_block_invoke.188
- ___159-[RTTripSegmentProvider buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:]_block_invoke.398
- ___159-[RTTripSegmentProvider buildTripSegmentsFeaturesWithIndex:inTransitions:trainMode:startVisitLocationOut:stopVisitLocationOut:transitionStartStopLocationsOut:]_block_invoke.401
- ___214-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:]_block_invoke
- ___214-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:]_block_invoke.288
- ___214-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:]_block_invoke.289
- ___214-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:]_block_invoke_2
- ___25-[RTDaemonClient restore]_block_invoke.748
- ___27-[RTLifeCycleManager _exit]_block_invoke.719
- ___27-[RTLifeCycleManager _exit]_block_invoke.727
- ___27-[RTLifeCycleManager _exit]_block_invoke.728
- ___27-[RTLifeCycleManager _exit]_block_invoke_2.726
- ___28-[RTHealthKitManager _setup]_block_invoke.624
- ___28-[RTLifeCycleManager _start]_block_invoke.704
- ___28-[RTLifeCycleManager _start]_block_invoke.716
- ___40-[SMInitiatorService _onDeletedMessage:]_block_invoke.185
- ___41-[RTAssetManager _downloadAsset:handler:]_block_invoke.362
- ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.726
- ___43-[RTPredictedContextManager _storeRequest:]_block_invoke.472
- ___45-[SMInitiatorService _onDeletedConversation:]_block_invoke.188
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.149
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.151
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.153
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.155
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke.157
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.150
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.152
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.154
- ___49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.156
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.169
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke.178
- ___49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.181
- ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.772
- ___52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.689
- ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.465
- ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.468
- ___54-[RTClusterLearnedRouteMetrics submitToCoreAnalytics:]_block_invoke.902
- ___54-[RTClusterLearnedRouteMetrics submitToCoreAnalytics:]_block_invoke_2.903
- ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.670
- ___55-[RTFeatureExtractor _getLocationsOfInterestWithError:]_block_invoke
- ___55-[RTFeatureExtractor _getLocationsOfInterestWithError:]_block_invoke.418
- ___55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.418
- ___55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.419
- ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.374
- ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.381
- ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.383
- ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.387
- ___56-[RTTripSegmentProvider processChunkWithIndex:inChunks:]_block_invoke.390
- ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.126
- ___57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.128
- ___57-[SMSessionMetricManager _gatherSessionDestinationStats:]_block_invoke.681
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.489
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.496
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.500
- ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.832
- ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.581
- ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.47
- ___61-[RTVisitConsolidator _fetchStoredVisitsWithOptions:handler:]_block_invoke.52
- ___62-[RTDaemonClientInternal connection:handleInvocation:isReply:]_block_invoke.494
- ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.689
- ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.454
- ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.455
- ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.456
- ___65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.200
- ___66+[RTVisitConsolidator removeConstantMonitorVisitEntriesWithExits:]_block_invoke
- ___66+[RTVisitConsolidator removeConstantMonitorVisitEntriesWithExits:]_block_invoke_2
- ___66+[RTVisitConsolidator removeConstantMonitorVisitEntriesWithExits:]_block_invoke_3
- ___66+[RTVisitConsolidator removeConstantMonitorVisitEntriesWithExits:]_block_invoke_4
- ___66+[RTVisitConsolidator removeConstantMonitorVisitEntriesWithExits:]_block_invoke_5
- ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.737
- ___69-[RTDaemonClient remoteStatusRegistrar:didReceiveRemoteStatus:error:]_block_invoke.773
- ___69-[RTTripSegmentTransitionPreprocessor appendTransitionToCurrentVisit]_block_invoke.196
- ___69-[RTTripSegmentTransitionPreprocessor appendTransitionToCurrentVisit]_block_invoke.197
- ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.764
- ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.512
- ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.749
- ___72-[RTTripSegmentProvider addToTransitionLocationsBuffer:forDateInterval:]_block_invoke.362
- ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.554
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.463
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.467
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.478
- ___76-[RTAssetManager initWithDefaultsManager:assetProcessor:xpcActivityManager:]_block_invoke.301
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.732
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.733
- ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.608
- ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke.209
- ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.768
- ___79-[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]_block_invoke.801
- ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.721
- ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.740
- ___82-[RTFeatureExtractor extractFeaturesWithLookbackDurations:operationType:outError:]_block_invoke
- ___83-[RTDaemonClient predictedContextRegistrar:didReceivePredictedContextResult:error:]_block_invoke.812
- ___85-[RTTripSegmentTransitionPreprocessor fetchEndpointCLLocationForTransition:atOrigin:]_block_invoke.211
- ___87+[RTVisitConsolidator consolidateHindsightVisits:constantMonitorVisits:sortDescriptor:]_block_invoke
- ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.676
- ___97-[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngineWithPlaceStats:dateInterval:]_block_invoke.414
- ___block_descriptor_32_e29_q24?0"RTVisit"8"RTVisit"16l
- ___block_descriptor_40_e8_32s_e39_v32?0"NSDate"8"NSMutableArray"16^B24ls32l8
- ___block_descriptor_64_e8_32s40s48s56s_e33_v16?0"CLTripSegmentOutputData"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56r64r_e29_v24?0"NSArray"8"NSError"16lr56l8r64l8s32l8s40l8s48l8
- ___block_literal_global.1382
- ___block_literal_global.171
- ___block_literal_global.173
- ___block_literal_global.175
- ___block_literal_global.177
- ___block_literal_global.187
- ___block_literal_global.214
- ___block_literal_global.232
- ___block_literal_global.234
- ___block_literal_global.361
- ___block_literal_global.422
- ___block_literal_global.424
- ___block_literal_global.449
- ___block_literal_global.450
- ___block_literal_global.613
- ___block_literal_global.646
- ___block_literal_global.66
- ___block_literal_global.691
- ___block_literal_global.698
- ___block_literal_global.707
- ___block_literal_global.718
- ___block_literal_global.725
- ___block_literal_global.730
- ___block_literal_global.742
- ___block_literal_global.750
- ___block_literal_global.91
- ___block_literal_global.971
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_libcoreroutine
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_libcoreroutine
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_libcoreroutine
- _objc_msgSend$_extractFeatures:operationType:lookbackDurations:outError:
- _objc_msgSend$_getLocationsOfInterestWithError:
- _objc_msgSend$_lookbackDurationsForDataCollection
- _objc_msgSend$_lookbackDurationsWithDefaults:
- _objc_msgSend$consolidateHindsightVisits:constantMonitorVisits:sortDescriptor:
- _objc_msgSend$extractFeaturesWithLookbackDurations:operationType:outError:
- _objc_msgSend$initWithDateInterval:predictionSources:probability:sourceBundleIdentifier:workoutActivityType:
- _objc_msgSend$removeConstantMonitorVisitEntriesWithExits:
- _objc_msgSend$updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:
CStrings:
+ "%@, %@, %@ stats for place with identifier, %@, number of days considered, %lu, number of days with data, %@, percentage of days with data, %@, cumulative event value, %@, daily total stats, median, %@, mean, %@, std, %@, daily longest duration stats, median, %@, mean, %@, std, %@"
+ "%@, %@, Biome event spanning the interval %@ -> %@ labeled with place identifier %@, due to visit + event overlapping with a duration of %.2f"
+ "%@, %@, adding user curated map item replacement, %{sensitive}@, originalMapItem, %{sensitive}@"
+ "%@, %@, failed to collect applied curation metrics for visit %@, error: %@"
+ "%@, %@, in time period between %@ -> %@, fetched %d Biome events of type %@ with a cumulative duration of %.2f"
+ "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, total dwell time, %@,  mlFeatures, %@, \n\npredicted probability for %@, %@, predicted probability for %@, %@, probability threshold for %@, %@, error, %@"
+ "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, total dwell time, %@, mlFeatures, %@, \n\nSkipping place inference in Ranker model because all the longest Biome stream bucketed values are <= 1. It means the stream doesn't exist or the values are less than 10 mins each."
+ "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, total dwell time, %@, mlFeatures, %@, \n\nSkipping place inference in multi class model because all the longest biome stream bucketed values are <= 1. It means the stream doesn't exist or the values are less than 10 mins each."
+ "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, total dwell time, %@, mlFeatures, %@, \n\noutput target score, %lf, error, %@"
+ "%@, %@, invoked for map items, %{sensitive}@"
+ "%@, %@, invoked with %lu places, for features within start date, %@, end date, %@"
+ "%@, %@, no matching user curations for map item, %{sensitive}@"
+ "%@, %@, no user curations fetched for options, %{sensitive}@, returning original map items early"
+ "%@, %@, not applying user curation correction to AOI, %{sensitive}@"
+ "%@, %@, overall visits count, %lu, local device visits count, %lu, earlier remote device visits count, %lu, total considered dwell time, %@, place, %{sensitive}@"
+ "%@, %@, place details, identifier, %@, name, %{sensitive}@, location, %{sensitive}@, visit location, %{sensitive}@, distance from place to visit location, %.3f, visit interval start date, %@, visit interval end date, %@, visit interval duration, %.2f, earliestStartDate, %@, latestEndDate, %@, error, %@"
+ "%@, %@, replacement map item candidate, %{sensitive}@, for original map item, %{sensitive}@, has an invalid map item and thus will not be applied"
+ "%@, %@, retrieved %lu Biome events of type %@ between dates %@ -> %@"
+ "%@, %@, retrieving Biome events of type %@"
+ "%@, adjusted entry date for the last constant monitor entry - before, %@, after, %@"
+ "%@, appending constant monitor exit visit - starts before the end of the last hindsight visit exit, but ends after"
+ "%@, business is permanently/temporarily closed"
+ "%@, constant monitor visit count, %lu, filtered output count, %lu"
+ "%@, dateInterval, startDate, %@, fetched lois count, %lu, error(s), %@"
+ "%@, fetched LOI, %@ for mapItem, %@, error, %@"
+ "%@, fetched visit, %@, error, %@"
+ "%@, internalInstall, %@, sampled, %@"
+ "%@, mostRecentVisit, %@, finalVisit, %@"
+ "%@, normalizedHours weekday, %lu, compareDate weekday, %lu"
+ "%@, result, %@, business hours start, %.1f, end, %.1f, compareTime, %.1f"
+ "%@, result, %@, hasHoursOnAnyDayThisWeek, %@"
+ "%@, skip duration filter, startDate, %@, endDate, %@, poi category, %@, timezone, %@"
+ "%@, weight, %.1f, businessHoursAvailable, %@, start, %@, end, %@, timeZone, %@"
+ "%@, weight, %.1f, startDate, %@, endDate, %@, duration, %.1f, poi category, %@, timezone, %@"
+ "%@,%@,Distance between origins,%{public}.3lf,destinations,%{public}.3lf"
+ "%@,%@,Skipping commute, duration too long,%f,threshold,%lu"
+ "%@,%@,Skipping commute, duration too long,%lf,threshold,%lu"
+ "%@,Updating trip cluster schedule,ID,%@,timeID,%d"
+ "%@,_predicate for cluster,ID,%@,timeID,%d"
+ "%@,failed to get clusterRouteRoads or convertedTripClusterRoute for clusterID,%@"
+ "%@:%@,Cluster data for metrics,numberOfMatchedCluster,%{public}d,numberOfUnMatchedCluster,%{public}d,numberOfTripsToFormLR,%{public}d,numberOfClusterStat,%{public}d,dtwForMatchedTripAvg,%{public}.3lf,dtwForUnmatchedTripAvg,%{public}.3lf,routeLengthAvg,%{public}.3lf,tripsToFormLearnedRouteAvg,%{public}.3lf,waypointCountAvg,%{public}.3lf,clusterProcessingRunTimeAvg,%{public}.3lf"
+ "20:19:11"
+ "@sum.duration"
+ "B92@0:8@16@24@32@40@48d56d64d72d80i88"
+ "CoreRoutine.UserCuration.CurationApplication"
+ "DTWDistance check failed for aStar reconstructed route. Using existing trip segment representative route"
+ "GEOErrorDomain"
+ "Jul 12 2025"
+ "RTBluePOIErrorDomain"
+ "RTBluePOIHelper"
+ "RTDefaultsFeatureExtractorLookbackDurationLocationsOfInterest"
+ "RTDefaultsSuggestionAlwaysOnPromptCount"
+ "RTDefaultsTripClusterManagerMaxClusterCountOnDevice"
+ "RTDefaultsTripClusterMaxClusterTraversalCount"
+ "RTDefaultsTripClusterMaxTripSegmentDistance"
+ "RTDefaultsTripClusterMaxTripSegmentTime"
+ "RTDefaultsTripClusterRoadFamiliarityDecayFactor"
+ "RTTripSegmentProvider, trip segment with nil commuteID found for interval %@"
+ "RTTripSegmentProvider:Chunk index,%d/%d has nil tripId, skipping index"
+ "RTTripSegmentTransitionPreprocessor: applyRule_largeDistanceTransitionsAreInvalid_ForTransitionAtIndex, tripSegmentTransitionStatus[%ld], distance %f m above threshold %f m. Reject."
+ "RTTripSegmentTransitionPreprocessor: applyRule_largeDistanceTransitionsAreInvalid_ForTransitionAtIndex, tripSegmentTransitionStatus[%ld]. Passthrough."
+ "RTTripSegmentTransitionPreprocessor: applyRule_longTransitionsAreInvalid_ForTransitionAtIndex, automotive transition, tripSegmentTransitionStatus[%ld], Reject"
+ "RTTripSegmentTransitionPreprocessor:applyRule_largeDistanceTransitionsAreInvalid_ForTransitionAtIndex: failed to compute distance from %{sensitive}@ to %{sensitive}@. Passthrough."
+ "RTTripSegmentTransitionPreprocessor:applyRule_largeDistanceTransitionsAreInvalid_ForTransitionAtIndex: failed to fetch visit location for identifiers %@ and %@. Passthrough."
+ "SpiQueryType"
+ "SpiResponseTime"
+ "TB,R,N,G_hasSprLandmarkIcon"
+ "TQ,N,V_maxClusterTraversalCount"
+ "TQ,N,V_maxTripSegmentDistanceForClustering"
+ "TQ,N,V_maxTripSegmentTimeForClustering"
+ "Td,N,V_familiarityDecayFactor"
+ "Tf,V_clusterProcessingRunTimeAvg"
+ "Tf,V_clusterProcessingRunTimeMax"
+ "Tf,V_compoundRoutesDistanceBetweenAdjacentCompoundTripSegmentsAvg"
+ "Tf,V_compoundRoutesNumDriveSegmentsCompoundedAvg"
+ "Tf,V_dtwForMatchedTripAvg"
+ "Tf,V_dtwForMatchedTripMax"
+ "Tf,V_dtwForUnmatchedTripAvg"
+ "Tf,V_dtwForUnmatchedTripMax"
+ "Tf,V_dtwForUnmatchedTripMin"
+ "Tf,V_multiModalBikeDistanceAfterDriveAvg"
+ "Tf,V_multiModalBikeDistanceAfterDriveMax"
+ "Tf,V_multiModalBikeDistanceBeforeDriveAvg"
+ "Tf,V_multiModalBikeDistanceBeforeDriveMax"
+ "Tf,V_multiModalBikeTimeAfterDriveAvg"
+ "Tf,V_multiModalBikeTimeAfterDriveMax"
+ "Tf,V_multiModalBikeTimeBeforeDriveAvg"
+ "Tf,V_multiModalBikeTimeBeforeDriveMax"
+ "Tf,V_multiModalDriveDistanceMax"
+ "Tf,V_multiModalDriveTimeMax"
+ "Tf,V_multiModalNumBikeSegmentsAvg"
+ "Tf,V_multiModalNumBikeSegmentsMax"
+ "Tf,V_multiModalNumWalkSegmentsAvg"
+ "Tf,V_multiModalNumWalkSegmentsMax"
+ "Tf,V_multiModalWalkDistanceAfterDriveAvg"
+ "Tf,V_multiModalWalkDistanceAfterDriveMax"
+ "Tf,V_multiModalWalkDistanceBeforeDriveAvg"
+ "Tf,V_multiModalWalkDistanceBeforeDriveMax"
+ "Tf,V_multiModalWalkTimeAfterDriveAvg"
+ "Tf,V_multiModalWalkTimeAfterDriveMax"
+ "Tf,V_multiModalWalkTimeBeforeDriveAvg"
+ "Tf,V_multiModalWalkTimeBeforeDriveMax"
+ "Tf,V_routeLengthAvg"
+ "Tf,V_routeLengthMax"
+ "Tf,V_spiResponseTime"
+ "Tf,V_spiReturnRouteLengthAvg"
+ "Tf,V_timeBetweenSPIQueries"
+ "Tf,V_tripsToFormLearnedRouteAvg"
+ "Tf,V_tspRunTimeAvg"
+ "Tf,V_tspRunTimeMax"
+ "Tf,V_waypointCountAvg"
+ "Tf,V_waypointCountMax"
+ "TimeBetweenSPIQueriesAvg"
+ "_dataCollectionDefaultLookbackDurations"
+ "_deleteAllTripClusterDataForClusterID:"
+ "_extractFeatures:operationType:lookbackIntervals:outError:"
+ "_familiarityDecayFactor"
+ "_fetchLocationOfInterestForMapItem:error:"
+ "_getLocationsOfInterestWithDateInterval:outError:"
+ "_hasSprLandmarkIcon"
+ "_inferenceDefaultLookbackDurations"
+ "_isMatchingODPair:tripCluster2:"
+ "_lookbackIntervalsWithDefaults:"
+ "_mapItemsWithUserCurationCorrection:error:"
+ "_maxClusterTraversalCount"
+ "_maxTripSegmentDistanceForClustering"
+ "_maxTripSegmentTimeForClustering"
+ "_predicateForClusterAndTimeID:timeID:"
+ "_timeZoneAtLocation:"
+ "_timeZoneFromLocation:"
+ "_updateSPIMetricReasonCodeAndSubmit:"
+ "applyRule_largeDistanceTransitionsAreInvalid_ForTransitionAtIndex:"
+ "collectMetricsForAppliedUserCuration:curatedVisit:learnedLocationStore:distanceCalculator:error:"
+ "collecting application metrics for user curation, %@"
+ "consolidateHindsightVisits:constantMonitorVisits:sortDescriptor:filterPairedVisitEntries:"
+ "contactIncludingImage:"
+ "correctPredictionsCount"
+ "curationDistance"
+ "curationVisitDensity1000m"
+ "curationVisitDensity100m"
+ "curationVisitDensity500m"
+ "d56@0:8@16@24@32@40@48"
+ "dateOfMostRecentTrip"
+ "extractFeaturesWithLookbackIntervals:operationType:outError:"
+ "failed to calculate curation distance, error: %@"
+ "failed to calculate distance to visit, error: %@"
+ "failed to fetch visits to LOIs within %@ meters, error: %@"
+ "familiarityDecayFactor"
+ "filterConstantMonitorVisits:"
+ "hasSprLandmarkIcon"
+ "hoursType"
+ "initWithDateInterval:predictionSources:probability:sourceBundleIdentifier:workoutActivityType:workoutLocationType:"
+ "initWithRouteSummary:loiIdentifier:"
+ "insideBusinessHours"
+ "insideBusinessHours:date:timeZone:"
+ "invalid parameters for collecting applied user curation metrics"
+ "localTimeIntervals"
+ "locationOfInterestType"
+ "maxClusterTraversalCount"
+ "maxTripSegmentDistanceForClustering"
+ "maxTripSegmentTimeForClustering"
+ "placeDailyNormalizedHours"
+ "requires a non nil map item."
+ "setFamiliarityDecayFactor:"
+ "setLocationOfInterestType:"
+ "setMaxClusterTraversalCount:"
+ "setMaxTripSegmentDistanceForClustering:"
+ "setMaxTripSegmentTimeForClustering:"
+ "setWorkoutLocationType:"
+ "shouldFilterByBusinessHours:"
+ "updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:"
+ "weightBasedOnBusinessHours:startDate:endDate:timeZone:metrics:"
+ "weightBasedOnDurationWithStartDate:endDate:timeZone:poiCategory:"
+ "workoutLocationType"
- "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, mlFeatures, %@, \n\nSkipping place inference in Ranker model because all the longest Biome stream bucketed values are <= 1. It means the stream doesn't exist or the values are less than 10 mins each."
- "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, mlFeatures, %@, \n\nSkipping place inference in multi class model because all the longest biome stream bucketed values are <= 1. It means the stream doesn't exist or the values are less than 10 mins each."
- "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, mlFeatures, %@, \n\noutput target score, %lf, error, %@"
- "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, mlFeatures, %@, \n\npredicted probability for %@, %@, predicted probability for %@, %@, probability threshold for %@, %@, error, %@"
- "%@, %@, overall visits count, %lu, local device visits count, %lu, earlier remote device visits count, %lu, place, %{sensitive}@"
- "%@, %@, place location, %{sensitive}@, visit location, %{sensitive}@, distance from place to visit location, %.3f, visit interval start date, %@, visit interval end date, %@, earliestStartDate, %@, latestEndDate, %@, error, %@"
- "%@, %lu hindsight visits, %lu constant monitor visits, %lu consolidated visits"
- "%@, appending most recent visit sourced from constantMonitor, %@"
- "%@, constant monitor visit count, %lu, output count, %lu"
- "%@, dateInterval, startDate, %@, endDate, %@, fetched lois count, %lu, error(s), %@"
- "%@,Updating trip cluster schedule,ID,%@"
- "22:36:42"
- "B88@0:8@16@24@32@40@48d56d64d72d80"
- "Jul  1 2025"
- "SPIQueryType"
- "SPIResponseTime"
- "Ti,V_clusterProcessingRunTimeAvg"
- "Ti,V_clusterProcessingRunTimeMax"
- "Ti,V_compoundRoutesDistanceBetweenAdjacentCompoundTripSegmentsAvg"
- "Ti,V_compoundRoutesNumDriveSegmentsCompoundedAvg"
- "Ti,V_dtwForMatchedTripAvg"
- "Ti,V_dtwForMatchedTripMax"
- "Ti,V_dtwForUnmatchedTripAvg"
- "Ti,V_dtwForUnmatchedTripMax"
- "Ti,V_dtwForUnmatchedTripMin"
- "Ti,V_multiModalBikeDistanceAfterDriveAvg"
- "Ti,V_multiModalBikeDistanceAfterDriveMax"
- "Ti,V_multiModalBikeDistanceBeforeDriveAvg"
- "Ti,V_multiModalBikeDistanceBeforeDriveMax"
- "Ti,V_multiModalBikeTimeAfterDriveAvg"
- "Ti,V_multiModalBikeTimeAfterDriveMax"
- "Ti,V_multiModalBikeTimeBeforeDriveAvg"
- "Ti,V_multiModalBikeTimeBeforeDriveMax"
- "Ti,V_multiModalDriveDistanceMax"
- "Ti,V_multiModalDriveTimeMax"
- "Ti,V_multiModalNumBikeSegmentsAvg"
- "Ti,V_multiModalNumBikeSegmentsMax"
- "Ti,V_multiModalNumWalkSegmentsAvg"
- "Ti,V_multiModalNumWalkSegmentsMax"
- "Ti,V_multiModalWalkDistanceAfterDriveAvg"
- "Ti,V_multiModalWalkDistanceAfterDriveMax"
- "Ti,V_multiModalWalkDistanceBeforeDriveAvg"
- "Ti,V_multiModalWalkDistanceBeforeDriveMax"
- "Ti,V_multiModalWalkTimeAfterDriveAvg"
- "Ti,V_multiModalWalkTimeAfterDriveMax"
- "Ti,V_multiModalWalkTimeBeforeDriveAvg"
- "Ti,V_multiModalWalkTimeBeforeDriveMax"
- "Ti,V_routeLengthAvg"
- "Ti,V_routeLengthMax"
- "Ti,V_spiResponseTime"
- "Ti,V_spiReturnRouteLengthAvg"
- "Ti,V_timeBetweenSPIQueries"
- "Ti,V_tripsToFormLearnedRouteAvg"
- "Ti,V_tspRunTimeAvg"
- "Ti,V_tspRunTimeMax"
- "Ti,V_waypointCountAvg"
- "Ti,V_waypointCountMax"
- "TimeBetweenSPIQueries"
- "_extractFeatures:operationType:lookbackDurations:outError:"
- "_getLocationsOfInterestWithError:"
- "_lookbackDurationsForDataCollection"
- "_lookbackDurationsWithDefaults:"
- "consolidateHindsightVisits:constantMonitorVisits:sortDescriptor:"
- "correctPredictionCount"
- "extractFeaturesWithLookbackDurations:operationType:outError:"
- "filtered out visit, %{sensitive}@"
- "initWithDateInterval:predictionSources:probability:sourceBundleIdentifier:workoutActivityType:"
- "q24@?0@\"RTVisit\"8@\"RTVisit\"16"
- "removeConstantMonitorVisitEntriesWithExits:"
- "updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:"
- "v32@?0@\"NSDate\"8@\"NSMutableArray\"16^B24"

```
