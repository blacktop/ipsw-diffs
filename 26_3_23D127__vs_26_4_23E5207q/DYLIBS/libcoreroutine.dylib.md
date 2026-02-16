## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1071.0.1.0.0
-  __TEXT.__text: 0x6169e8
-  __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x315e8
-  __TEXT.__const: 0x49b0
+1072.0.5.0.1
+  __TEXT.__text: 0x671f60
+  __TEXT.__auth_stubs: 0x2160
+  __TEXT.__objc_methlist: 0x31910
+  __TEXT.__const: 0x4950
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x78544
-  __TEXT.__cstring: 0x45fec
+  __TEXT.__oslogstring: 0x7947b
+  __TEXT.__cstring: 0x46272
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c

   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x28e9c
+  __TEXT.__gcc_except_tab: 0x29528
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xdde0
-  __TEXT.__eh_frame: 0x390
-  __TEXT.__objc_classname: 0x58d0
-  __TEXT.__objc_methname: 0x933e9
-  __TEXT.__objc_methtype: 0xd1af
-  __TEXT.__objc_stubs: 0x56920
-  __DATA_CONST.__got: 0x3150
-  __DATA_CONST.__const: 0xf6c0
-  __DATA_CONST.__objc_classlist: 0x1548
+  __TEXT.__unwind_info: 0x10318
+  __TEXT.__eh_frame: 0x348
+  __TEXT.__objc_classname: 0x59c2
+  __TEXT.__objc_methname: 0x94455
+  __TEXT.__objc_methtype: 0xd36e
+  __TEXT.__objc_stubs: 0x577e0
+  __DATA_CONST.__got: 0x3178
+  __DATA_CONST.__const: 0xf770
+  __DATA_CONST.__objc_classlist: 0x1560
   __DATA_CONST.__objc_catlist: 0x3a8
-  __DATA_CONST.__objc_protolist: 0x358
+  __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19838
+  __DATA_CONST.__objc_selrefs: 0x19c00
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x1190
+  __DATA_CONST.__objc_superrefs: 0x11a0
   __DATA_CONST.__objc_arraydata: 0x2b88
-  __AUTH_CONST.__auth_got: 0x10d8
+  __AUTH_CONST.__auth_got: 0x10c0
   __AUTH_CONST.__const: 0x32e0
-  __AUTH_CONST.__cfstring: 0x29100
-  __AUTH_CONST.__objc_const: 0x510b0
+  __AUTH_CONST.__cfstring: 0x29260
+  __AUTH_CONST.__objc_const: 0x517c0
   __AUTH_CONST.__objc_intobj: 0x48c0
   __AUTH_CONST.__objc_arrayobj: 0xf00
   __AUTH_CONST.__objc_doubleobj: 0xb10
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x2118
-  __DATA.__objc_ivar: 0x25e0
-  __DATA.__data: 0x2cd8
+  __AUTH.__objc_data: 0x1fd8
+  __DATA.__objc_ivar: 0x25ec
+  __DATA.__data: 0x2d28
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_ivar: 0x117c
-  __DATA_DIRTY.__objc_data: 0xb470
-  __DATA_DIRTY.__data: 0x5b8
+  __DATA_DIRTY.__objc_ivar: 0x1194
+  __DATA_DIRTY.__objc_data: 0xb6a0
+  __DATA_DIRTY.__data: 0x5c8
   __DATA_DIRTY.__bss: 0x200
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
+  - /System/Library/PrivateFrameworks/MallocStackLogging.framework/MallocStackLogging
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MapsSync.framework/MapsSync
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9DADC641-51C5-3D3C-AF61-ED4341F7EE74
-  Functions: 20330
-  Symbols:   65640
-  CStrings:  40623
+  UUID: 58FF0CEF-6CA8-37E5-A492-4AB01A327962
+  Functions: 20405
+  Symbols:   65934
+  CStrings:  40848
 
Symbols:
+ +[RTBluePOIHelper confidenceWeightForMapItem:startDate:endDate:]
+ +[RTBluePOIHelper insideRTBusinessHours:date:timeZone:]
+ +[RTBluePOIHelper weightBasedOnRTBusinessHours:startDate:endDate:timeZone:metrics:]
+ +[RTBluePOITileManager downloadKeyForLocation:]
+ +[RTBusinessHoursArrayTransformer allowsReverseTransformation]
+ +[RTBusinessHoursArrayTransformer transformedValueClass]
+ +[RTPersistenceMigrator _metadataStateToString:]
+ -[NSManagedObjectContext(SafePerformBlock) rt_performBlock:]
+ -[NSManagedObjectContext(SafePerformBlock) rt_performBlockAndWait:]
+ -[RTAuthorizedLocationZDRLocationManager _getFirstZDRCreationTime]
+ -[RTBusinessHoursArrayTransformer reverseTransformedValue:]
+ -[RTBusinessHoursArrayTransformer transformedValue:]
+ -[RTClientListenerInternal initWithAccountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:]
+ -[RTClientListenerInternal setTripSegmentManager:]
+ -[RTClientListenerInternal tripSegmentManager]
+ -[RTDaemonClient generatedTripSegmentsRegistrar:didReceiveGeneratedTripSegment:withError:]
+ -[RTDaemonClient generatedTripSegmentsRegistrar]
+ -[RTDaemonClient setGeneratedTripSegmentsRegistrar:]
+ -[RTDaemonClient startMonitoringForGeneratedTripSegmentsWithReply:]
+ -[RTDaemonClient stopMonitoringForGeneratedTripSegmentsWithReply:]
+ -[RTDaemonClientInternal fetchVisitWithIdentifier:reply:]
+ -[RTDaemonClientInternal initWithQueue:accountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:]
+ -[RTDaemonClientInternal setMallocStackLoggingEnabled:mode:handler:]
+ -[RTDaemonClientInternal setTripSegmentManager:]
+ -[RTDaemonClientInternal simulateGeneratedTripSegment:withCallback:]
+ -[RTDaemonClientInternal tripSegmentManager]
+ -[RTDaemonClientRegistrarGeneratedTripSegments .cxx_destruct]
+ -[RTDaemonClientRegistrarGeneratedTripSegments _onGeneratedTripSegmentNotification:]
+ -[RTDaemonClientRegistrarGeneratedTripSegments _startMonitoringForGeneratedTripSegments]
+ -[RTDaemonClientRegistrarGeneratedTripSegments _stopMonitoringForGeneratedTripSegments]
+ -[RTDaemonClientRegistrarGeneratedTripSegments countOfPendingInvocations]
+ -[RTDaemonClientRegistrarGeneratedTripSegments delegate]
+ -[RTDaemonClientRegistrarGeneratedTripSegments dispatcher]
+ -[RTDaemonClientRegistrarGeneratedTripSegments enqueueGeneratedTripSegmentBlock:onFailureBlock:description:]
+ -[RTDaemonClientRegistrarGeneratedTripSegments initWithTripSegmentManager:onQueue:]
+ -[RTDaemonClientRegistrarGeneratedTripSegments invocationsPending]
+ -[RTDaemonClientRegistrarGeneratedTripSegments isMonitoring]
+ -[RTDaemonClientRegistrarGeneratedTripSegments onGeneratedTripSegmentNotification:]
+ -[RTDaemonClientRegistrarGeneratedTripSegments queue]
+ -[RTDaemonClientRegistrarGeneratedTripSegments registered]
+ -[RTDaemonClientRegistrarGeneratedTripSegments setDelegate:]
+ -[RTDaemonClientRegistrarGeneratedTripSegments setDispatcher:]
+ -[RTDaemonClientRegistrarGeneratedTripSegments setIsMonitoring:]
+ -[RTDaemonClientRegistrarGeneratedTripSegments setTripSegmentManager:]
+ -[RTDaemonClientRegistrarGeneratedTripSegments startMonitoringForGeneratedTripSegments]
+ -[RTDaemonClientRegistrarGeneratedTripSegments stopMonitoringForGeneratedTripSegments]
+ -[RTDaemonClientRegistrarGeneratedTripSegments tripSegmentManager]
+ -[RTGeneratedTripSegmentNotification .cxx_destruct]
+ -[RTGeneratedTripSegmentNotification generatedTripSegment]
+ -[RTGeneratedTripSegmentNotification initWithGeneratedTripSegment:]
+ -[RTInferredMapItemFuser boostHighUserIntentionConfidences:candidates:referenceLocation:error:]
+ -[RTInferredMapItemFuser highIntentionSource:]
+ -[RTLearnedLocationEngine _isUpdateLearnedPlaceWithBusinessHoursRequired:]
+ -[RTLearnedLocationEngine _updateLearnedPlaceWithBusinessHours:]
+ -[RTLearnedLocationManager _createLookbackDateIntervalFromOptions:error:]
+ -[RTLearnedLocationManager defaultsManager]
+ -[RTLearnedLocationManager initWithQueue:contactsManager:defaultsManager:distanceCalculator:learnedLocationStore:learnedPlaceTypeInferenceStore:mapServiceManager:]
+ -[RTMapServiceManager fetchGeoMapItemWithMUID:options:handler:]
+ -[RTPersistenceDriver _backgroundProcessingAssertionsDidRelease]
+ -[RTPersistenceMigrator _detectMetadataStateForStore:coordinator:error:]
+ -[RTPersistenceMigrator _updateStoreMetadataWithAppleIDs:coordinator:error:]
+ -[RTPersistenceStore peekMetadataWithCoordinator:error:]
+ -[RTTripSegmentManager _isOKToAddTripSegmentdata:]
+ -[RTTripSegmentManager _postNotificationForGeneratedTripSegment:]
+ -[RTTripSegmentManager postNotificationForGeneratedTripSegment:]
+ -[RTTripSegmentManager(Internal) simulateGeneratedTripSegment:withCallback:]
+ -[RTVisitLabeler startWiFiScanForLabelling:clientIdentifier:policy:delay:maxRetries:handler:]
+ GCC_except_table166
+ GCC_except_table173
+ GCC_except_table177
+ GCC_except_table192
+ GCC_except_table195
+ GCC_except_table228
+ GCC_except_table231
+ GCC_except_table249
+ GCC_except_table259
+ GCC_except_table261
+ GCC_except_table262
+ GCC_except_table264
+ GCC_except_table265
+ GCC_except_table282
+ GCC_except_table291
+ GCC_except_table293
+ GCC_except_table295
+ GCC_except_table297
+ GCC_except_table300
+ GCC_except_table306
+ GCC_except_table308
+ _OBJC_CLASS_$_RTBusinessHours
+ _OBJC_CLASS_$_RTBusinessHoursArrayTransformer
+ _OBJC_CLASS_$_RTDaemonClientRegistrarGeneratedTripSegments
+ _OBJC_CLASS_$_RTDailyHours
+ _OBJC_CLASS_$_RTGeneratedTripSegmentNotification
+ _OBJC_CLASS_$_RTLocalTimeInterval
+ _OBJC_IVAR_$_RTDaemonClient._generatedTripSegmentsRegistrar
+ _OBJC_IVAR_$_RTDaemonClientInternal._tripSegmentManager
+ _OBJC_IVAR_$_RTDaemonClientRegistrarGeneratedTripSegments._isMonitoring
+ _OBJC_IVAR_$_RTGeneratedTripSegmentNotification._generatedTripSegment
+ _OBJC_METACLASS_$_RTBusinessHoursArrayTransformer
+ _OBJC_METACLASS_$_RTDaemonClientRegistrarGeneratedTripSegments
+ _OBJC_METACLASS_$_RTGeneratedTripSegmentNotification
+ _RTApplicationManagerExecutableRoutineAppRoutineToolWidgetExtension
+ _RTRestorationKeyGeneratedTripSegmentsRegistrar
+ _RTRestorationKeyPeopleDiscoveryRegistrar
+ _RTRestorationKeyPredictedContextRegistrar
+ _RTRestorationKeyRemoteStatusRegistrar
+ _RTRestorationKeyScenarioTriggerRegistrar
+ _RTRestorationKeyVehicleEventRegistrar
+ __OBJC_$_CLASS_METHODS_RTBusinessHoursArrayTransformer
+ __OBJC_$_CLASS_METHODS_RTPersistenceMigrator
+ __OBJC_$_INSTANCE_METHODS_NSManagedObjectContext(RTExtensions|Cloud|SafePerformBlock)
+ __OBJC_$_INSTANCE_METHODS_RTBusinessHoursArrayTransformer
+ __OBJC_$_INSTANCE_METHODS_RTDaemonClientRegistrarGeneratedTripSegments
+ __OBJC_$_INSTANCE_METHODS_RTGeneratedTripSegmentNotification
+ __OBJC_$_INSTANCE_METHODS_RTTripSegmentManager(Internal)
+ __OBJC_$_INSTANCE_VARIABLES_RTDaemonClientRegistrarGeneratedTripSegments
+ __OBJC_$_INSTANCE_VARIABLES_RTGeneratedTripSegmentNotification
+ __OBJC_$_PROP_LIST_RTDaemonClientRegistrarGeneratedTripSegments
+ __OBJC_$_PROP_LIST_RTGeneratedTripSegmentNotification
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RTDaemonClientRegistrarGeneratedTripSegmentProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RTDaemonClientRegistrarGeneratedTripSegmentProtocol
+ __OBJC_$_PROTOCOL_REFS_RTDaemonClientRegistrarGeneratedTripSegmentProtocol
+ __OBJC_CLASS_PROTOCOLS_$_RTDaemonClientRegistrarGeneratedTripSegments
+ __OBJC_CLASS_RO_$_RTBusinessHoursArrayTransformer
+ __OBJC_CLASS_RO_$_RTDaemonClientRegistrarGeneratedTripSegments
+ __OBJC_CLASS_RO_$_RTGeneratedTripSegmentNotification
+ __OBJC_LABEL_PROTOCOL_$_RTDaemonClientRegistrarGeneratedTripSegmentProtocol
+ __OBJC_METACLASS_RO_$_RTBusinessHoursArrayTransformer
+ __OBJC_METACLASS_RO_$_RTDaemonClientRegistrarGeneratedTripSegments
+ __OBJC_METACLASS_RO_$_RTGeneratedTripSegmentNotification
+ __OBJC_PROTOCOL_$_RTDaemonClientRegistrarGeneratedTripSegmentProtocol
+ ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke.94
+ ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.460
+ ___122-[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:error:]_block_invoke.135
+ ___122-[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:error:]_block_invoke.136
+ ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke.94
+ ___25-[RTDaemonClient restore]_block_invoke.801
+ ___25-[RTDaemonClient restore]_block_invoke.804
+ ___25-[RTDaemonClient restore]_block_invoke.807
+ ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.274
+ ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.275
+ ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.276
+ ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.277
+ ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.281
+ ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.282
+ ___27-[RTLifeCycleManager _exit]_block_invoke.772
+ ___27-[RTLifeCycleManager _exit]_block_invoke.778
+ ___27-[RTLifeCycleManager _exit]_block_invoke.780
+ ___27-[RTLifeCycleManager _exit]_block_invoke.781
+ ___27-[RTLifeCycleManager _exit]_block_invoke_2.779
+ ___28-[RTHealthKitManager _setup]_block_invoke.673
+ ___28-[RTLifeCycleManager _start]_block_invoke.757
+ ___28-[RTLifeCycleManager _start]_block_invoke.763
+ ___28-[RTLifeCycleManager _start]_block_invoke.766
+ ___28-[RTLifeCycleManager _start]_block_invoke.769
+ ___41-[RTAssetManager _downloadAsset:handler:]_block_invoke.410
+ ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.910
+ ___47-[RTClientListener _setupConnection:forClient:]_block_invoke.316
+ ___48-[RTFeatureExtractor _getHomeKitHomesWithError:]_block_invoke.497
+ ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.831
+ ___50-[RTTripSegmentManager _isOKToAddTripSegmentdata:]_block_invoke
+ ___50-[RTTripSegmentManager _isOKToAddTripSegmentdata:]_block_invoke.261
+ ___51-[RTLearnedLocationEngine _getDailyTrainingMetrics]_block_invoke.814
+ ___51-[RTLearnedLocationEngine _teardownTrainingMetrics]_block_invoke.870
+ ___52-[RTLearnedLocationEngine _createLOIForPlace:error:]_block_invoke.896
+ ___52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.737
+ ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.726
+ ___55-[RTLearnedLocationEngine _retrainVisitsWithoutPlaces:]_block_invoke.872
+ ___55-[RTLearnedLocationEngine trainForReason:mode:handler:]_block_invoke.651
+ ___57-[RTDaemonClientInternal fetchVisitWithIdentifier:reply:]_block_invoke
+ ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.770
+ ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.771
+ ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.772
+ ___57-[SMSessionMetricManager _gatherSessionDestinationStats:]_block_invoke.729
+ ___58-[RTFeatureExtractor _getVisitsWithDateInterval:outError:]_block_invoke.465
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.540
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.547
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.551
+ ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.886
+ ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.283
+ ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.284
+ ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.285
+ ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.632
+ ___60-[NSManagedObjectContext(SafePerformBlock) rt_performBlock:]_block_invoke
+ ___62-[RTDaemonClientInternal connection:handleInvocation:isReply:]_block_invoke.671
+ ___63-[RTFeatureExtractor _getTransitionsWithDateInterval:outError:]_block_invoke.467
+ ___63-[RTMapServiceManager fetchGeoMapItemWithMUID:options:handler:]_block_invoke
+ ___63-[RTMapServiceManager fetchGeoMapItemWithMUID:options:handler:]_block_invoke_2
+ ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.745
+ ___64-[RTLearnedLocationEngine _updateLearnedPlaceWithBusinessHours:]_block_invoke
+ ___64-[RTTripSegmentManager postNotificationForGeneratedTripSegment:]_block_invoke
+ ___65-[RTTripSegmentManager _purgeTripSegmentsOnDateInterval:handler:]_block_invoke.293
+ ___65-[RTTripSegmentManager _purgeTripSegmentsOnDateInterval:handler:]_block_invoke.294
+ ___66-[RTAuthorizedLocationZDRLocationManager _getFirstZDRCreationTime]_block_invoke
+ ___66-[RTFeatureExtractor _getCalendarEventsWithDateInterval:outError:]_block_invoke.486
+ ___67-[NSManagedObjectContext(SafePerformBlock) rt_performBlockAndWait:]_block_invoke
+ ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.793
+ ___68-[RTDaemonClientInternal simulateGeneratedTripSegment:withCallback:]_block_invoke
+ ___68-[RTDaemonClientInternal simulateGeneratedTripSegment:withCallback:]_block_invoke_2
+ ___68-[RTFeatureExtractor _getMapsViewedPlacesWithDateInterval:outError:]_block_invoke.491
+ ___68-[RTFeatureExtractor _getMotionActivitiesWithDateInterval:outError:]_block_invoke.493
+ ___68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.606
+ ___68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.609
+ ___69-[RTDaemonClient remoteStatusRegistrar:didReceiveRemoteStatus:error:]_block_invoke.832
+ ___69-[RTFeatureExtractor _getLocationHistoriesWithDateInterval:outError:]_block_invoke.484
+ ___69-[RTTripSegmentManager _fetchTripSegmentMetadataWithOptions:handler:]_block_invoke.244
+ ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.823
+ ___70-[RTLearnedLocationEngine _saveIdentifiersOfKnownPlaceTypesWithError:]_block_invoke.792
+ ___70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke.598
+ ___70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke_2.599
+ ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.301
+ ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.302
+ ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.303
+ ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.305
+ ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.306
+ ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.307
+ ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.308
+ ___71-[RTFeatureExtractor _getLocationsOfInterestWithDateInterval:outError:]_block_invoke.482
+ ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke.857
+ ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke_2.858
+ ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.563
+ ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.936
+ ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.605
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.514
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.518
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.529
+ ___74-[RTLearnedLocationEngine _isUpdateLearnedPlaceWithBusinessHoursRequired:]_block_invoke
+ ___74-[RTLearnedLocationEngine _relabelWithRelabeler:relabelerPersister:error:]_block_invoke.752
+ ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.806
+ ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.807
+ ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.810
+ ___75-[RTLearnedLocationEngine requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.686
+ ___76-[RTAssetManager initWithDefaultsManager:assetProcessor:xpcActivityManager:]_block_invoke.349
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.788
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.789
+ ___76-[RTLearnedLocationEngine _appendVisitsToLocationsOfInterestModelWithError:]_block_invoke.874
+ ___76-[RTLearnedLocationEngine _requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.687
+ ___77+[RTLearnedLocationReconcilerPerDevice sortReconciledVisitsByMapItemQuality:]_block_invoke_4.84
+ ___77-[RTFeatureExtractor _getMapsHistoricalNavigationsWithDateInterval:outError:]_block_invoke.489
+ ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.659
+ ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke.219
+ ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.827
+ ___79-[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]_block_invoke.865
+ ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.777
+ ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.796
+ ___82-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]_block_invoke.906
+ ___82-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]_block_invoke.907
+ ___83-[RTDaemonClient predictedContextRegistrar:didReceivePredictedContextResult:error:]_block_invoke.876
+ ___83-[RTDaemonClientRegistrarGeneratedTripSegments onGeneratedTripSegmentNotification:]_block_invoke
+ ___83-[RTLearnedLocationEngine _recoverKnownPlaceTypesWithPlaceTypeClassifier:outError:]_block_invoke.813
+ ___86-[RTDaemonClientRegistrarGeneratedTripSegments stopMonitoringForGeneratedTripSegments]_block_invoke
+ ___87-[RTDaemonClientRegistrarGeneratedTripSegments startMonitoringForGeneratedTripSegments]_block_invoke
+ ___90-[RTDaemonClient generatedTripSegmentsRegistrar:didReceiveGeneratedTripSegment:withError:]_block_invoke
+ ___90-[RTDaemonClient generatedTripSegmentsRegistrar:didReceiveGeneratedTripSegment:withError:]_block_invoke.850
+ ___90-[RTDaemonClient generatedTripSegmentsRegistrar:didReceiveGeneratedTripSegment:withError:]_block_invoke.851
+ ___92-[RTVisitLabeler _collectWiFiScansAndLabelVisit:clientIdentifier:policy:maxRetries:handler:]_block_invoke.30
+ ___93-[RTVisitLabeler startWiFiScanForLabelling:clientIdentifier:policy:delay:maxRetries:handler:]_block_invoke
+ ___93-[RTVisitLabeler startWiFiScanForLabelling:clientIdentifier:policy:delay:maxRetries:handler:]_block_invoke.29
+ ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.732
+ ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.469
+ ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.473
+ ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.475
+ ___block_descriptor_40_e8_32bs_e36_v24?0"RTLearnedVisit"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e35_v24?0"RTTripSegment"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e38_"RTInferredMapItem"16?0"RTMapItem"8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e38_"RTInferredMapItem"16?0"RTMapItem"8ls32l8s40l8
+ ___block_descriptor_50_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_56_e8_32s40r_e36_v24?0"NSMutableArray"8"NSError"16lr40l8s32l8
+ ___block_descriptor_96_e8_32s40s48s56bs64r_e5_v8?0ls32l8s40l8s48l8r64l8s56l8
+ ___block_literal_global.1027
+ ___block_literal_global.1382
+ ___block_literal_global.142
+ ___block_literal_global.1437
+ ___block_literal_global.217
+ ___block_literal_global.236
+ ___block_literal_global.238
+ ___block_literal_global.240
+ ___block_literal_global.242
+ ___block_literal_global.409
+ ___block_literal_global.429
+ ___block_literal_global.433
+ ___block_literal_global.605
+ ___block_literal_global.626
+ ___block_literal_global.658
+ ___block_literal_global.661
+ ___block_literal_global.664
+ ___block_literal_global.695
+ ___block_literal_global.760
+ ___block_literal_global.765
+ ___block_literal_global.768
+ ___block_literal_global.771
+ ___block_literal_global.783
+ ___block_literal_global.795
+ ___block_literal_global.798
+ ___block_literal_global.803
+ ___block_literal_global.806
+ ___block_literal_global.809
+ ___block_literal_global.86
+ ___block_literal_global.910
+ _msl_turn_off_stack_logging
+ _msl_turn_on_stack_logging
+ _objc_msgSend$Discoverability
+ _objc_msgSend$Signals
+ _objc_msgSend$_backgroundProcessingAssertionsDidRelease
+ _objc_msgSend$_createLookbackDateIntervalFromOptions:error:
+ _objc_msgSend$_detectMetadataStateForStore:coordinator:error:
+ _objc_msgSend$_getFirstZDRCreationTime
+ _objc_msgSend$_isOKToAddTripSegmentdata:
+ _objc_msgSend$_isUpdateLearnedPlaceWithBusinessHoursRequired:
+ _objc_msgSend$_metadataStateToString:
+ _objc_msgSend$_onGeneratedTripSegmentNotification:
+ _objc_msgSend$_postNotificationForGeneratedTripSegment:
+ _objc_msgSend$_startMonitoringForGeneratedTripSegments
+ _objc_msgSend$_stopMonitoringForGeneratedTripSegments
+ _objc_msgSend$_updateLearnedPlaceWithBusinessHours:
+ _objc_msgSend$_updateStoreMetadataWithAppleIDs:coordinator:error:
+ _objc_msgSend$addressAdministrativeArea
+ _objc_msgSend$addressAdministrativeAreaCode
+ _objc_msgSend$addressAreasOfInterest
+ _objc_msgSend$addressCountry
+ _objc_msgSend$addressCountryCode
+ _objc_msgSend$addressCreationDate
+ _objc_msgSend$addressExpirationDate
+ _objc_msgSend$addressGeoAddressData
+ _objc_msgSend$addressISO3166CountryCode
+ _objc_msgSend$addressISO3166SubdivisionCode
+ _objc_msgSend$addressInlandWater
+ _objc_msgSend$addressIsland
+ _objc_msgSend$addressLocality
+ _objc_msgSend$addressOcean
+ _objc_msgSend$addressPostalCode
+ _objc_msgSend$addressSubAdministrativeArea
+ _objc_msgSend$addressSubLocality
+ _objc_msgSend$addressSubPremises
+ _objc_msgSend$addressSubThoroughfare
+ _objc_msgSend$addressThoroughfare
+ _objc_msgSend$boostHighUserIntentionConfidences:candidates:referenceLocation:error:
+ _objc_msgSend$businessHours
+ _objc_msgSend$confidenceWeightForMapItem:startDate:endDate:
+ _objc_msgSend$dailyHours
+ _objc_msgSend$deletedLearnedPlaceTypeInferencesPredating:handler:
+ _objc_msgSend$enqueueGeneratedTripSegmentBlock:onFailureBlock:description:
+ _objc_msgSend$fetchGeoMapItemWithMUID:options:handler:
+ _objc_msgSend$generatedTripSegment
+ _objc_msgSend$generatedTripSegmentsRegistrar
+ _objc_msgSend$generatedTripSegmentsRegistrar:didReceiveGeneratedTripSegment:withError:
+ _objc_msgSend$highIntentionSource:
+ _objc_msgSend$initWithAccountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:
+ _objc_msgSend$initWithContentIdentifier:context:osBuild:userInfo:
+ _objc_msgSend$initWithDate:messageID:sessionID:invitationTokenDict:sessionType:estimatedEndTime:coarseEstimatedEndTime:destinationType:destinationMapItem:lowPowerModeWarningState:
+ _objc_msgSend$initWithGeneratedTripSegment:
+ _objc_msgSend$initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:
+ _objc_msgSend$initWithQueue:accountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:
+ _objc_msgSend$initWithQueue:contactsManager:defaultsManager:distanceCalculator:learnedLocationStore:learnedPlaceTypeInferenceStore:mapServiceManager:
+ _objc_msgSend$initWithTripSegmentManager:onQueue:
+ _objc_msgSend$insideRTBusinessHours:date:timeZone:
+ _objc_msgSend$locationContextManager
+ _objc_msgSend$mapItemBusinessHours
+ _objc_msgSend$mapItemCategory
+ _objc_msgSend$mapItemCategoryMUID
+ _objc_msgSend$mapItemCreationDate
+ _objc_msgSend$mapItemDisplayLanguage
+ _objc_msgSend$mapItemDisputed
+ _objc_msgSend$mapItemExpirationDate
+ _objc_msgSend$mapItemExtendedAttributesAddressIdentifier
+ _objc_msgSend$mapItemExtendedAttributesIdentifier
+ _objc_msgSend$mapItemExtendedAttributesIsMe
+ _objc_msgSend$mapItemExtendedAttributesWifiConfidence
+ _objc_msgSend$mapItemExtendedAttributesWifiFingerprintLabelType
+ _objc_msgSend$mapItemGeoMapItemIdentifier
+ _objc_msgSend$mapItemLatitude
+ _objc_msgSend$mapItemLongitude
+ _objc_msgSend$mapItemMUID
+ _objc_msgSend$mapItemName
+ _objc_msgSend$mapItemReferenceFrame
+ _objc_msgSend$mapItemResultProviderID
+ _objc_msgSend$mapItemUncertainty
+ _objc_msgSend$onGeneratedTripSegment:withError:
+ _objc_msgSend$peekMetadataWithCoordinator:error:
+ _objc_msgSend$postNotificationForGeneratedTripSegment:
+ _objc_msgSend$rt_performBlockAndWait:
+ _objc_msgSend$setAddressAdministrativeArea:
+ _objc_msgSend$setAddressAdministrativeAreaCode:
+ _objc_msgSend$setAddressAreasOfInterest:
+ _objc_msgSend$setAddressCountry:
+ _objc_msgSend$setAddressCountryCode:
+ _objc_msgSend$setAddressCreationDate:
+ _objc_msgSend$setAddressExpirationDate:
+ _objc_msgSend$setAddressGeoAddressData:
+ _objc_msgSend$setAddressISO3166CountryCode:
+ _objc_msgSend$setAddressISO3166SubdivisionCode:
+ _objc_msgSend$setAddressInlandWater:
+ _objc_msgSend$setAddressIsland:
+ _objc_msgSend$setAddressLocality:
+ _objc_msgSend$setAddressOcean:
+ _objc_msgSend$setAddressPostalCode:
+ _objc_msgSend$setAddressSubAdministrativeArea:
+ _objc_msgSend$setAddressSubLocality:
+ _objc_msgSend$setAddressSubPremises:
+ _objc_msgSend$setAddressSubThoroughfare:
+ _objc_msgSend$setAddressThoroughfare:
+ _objc_msgSend$setBusinessHours:
+ _objc_msgSend$setMapItemBusinessHours:
+ _objc_msgSend$setMapItemCategory:
+ _objc_msgSend$setMapItemCategoryMUID:
+ _objc_msgSend$setMapItemCreationDate:
+ _objc_msgSend$setMapItemDisplayLanguage:
+ _objc_msgSend$setMapItemDisputed:
+ _objc_msgSend$setMapItemExpirationDate:
+ _objc_msgSend$setMapItemExtendedAttributesAddressIdentifier:
+ _objc_msgSend$setMapItemExtendedAttributesIdentifier:
+ _objc_msgSend$setMapItemExtendedAttributesIsMe:
+ _objc_msgSend$setMapItemExtendedAttributesWifiConfidence:
+ _objc_msgSend$setMapItemExtendedAttributesWifiFingerprintLabelType:
+ _objc_msgSend$setMapItemGeoMapItemIdentifier:
+ _objc_msgSend$setMapItemLatitude:
+ _objc_msgSend$setMapItemLongitude:
+ _objc_msgSend$setMapItemName:
+ _objc_msgSend$setMapItemReferenceFrame:
+ _objc_msgSend$setMapItemResultProviderID:
+ _objc_msgSend$setMapItemUncertainty:
+ _objc_msgSend$simulateGeneratedTripSegment:withCallback:
+ _objc_msgSend$startMonitoringForGeneratedTripSegments
+ _objc_msgSend$startMonitoringForGeneratedTripSegmentsWithReply:
+ _objc_msgSend$startWiFiScanForLabelling:clientIdentifier:policy:delay:maxRetries:handler:
+ _objc_msgSend$stopMonitoringForGeneratedTripSegments
+ _objc_msgSend$timeIntervals
+ _objc_msgSend$weightBasedOnRTBusinessHours:startDate:endDate:timeZone:metrics:
+ _objc_release_x11
- +[RTBluePOIHelper shouldFilterByBusinessHours:]
- -[RTBluePOITileManager downloadKeyForLocation:]
- -[RTClientListenerInternal initWithAccountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:]
- -[RTDaemonClientInternal initWithQueue:accountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:]
- -[RTLearnedLocationManager initWithQueue:contactsManager:distanceCalculator:learnedLocationStore:learnedPlaceTypeInferenceStore:mapServiceManager:]
- -[RTLearnedLocationOfInterestMO .cxx_destruct]
- -[RTLearnedLocationOfInterestMO cachedMapItem]
- -[RTLearnedLocationOfInterestMO setCachedMapItem:]
- -[RTMapServiceManager fetchConfidenceWeightForMapItem:startDate:endDate:options:handler:]
- -[RTTripSegmentManager isOKToAddTripSegmentdata:]
- -[RTVisitLabeler startWiFiScanForLabelling:clientIdentifier:policy:handler:]
- GCC_except_table151
- GCC_except_table169
- GCC_except_table185
- GCC_except_table187
- GCC_except_table208
- GCC_except_table221
- GCC_except_table226
- GCC_except_table237
- GCC_except_table239
- GCC_except_table251
- GCC_except_table254
- GCC_except_table255
- GCC_except_table257
- GCC_except_table260
- GCC_except_table277
- GCC_except_table279
- GCC_except_table283
- GCC_except_table290
- GCC_except_table294
- GCC_except_table296
- GCC_except_table298
- GCC_except_table301
- GCC_except_table56
- _OBJC_IVAR_$_RTLearnedLocationOfInterestMO.cachedMapItem
- _RTApplicationManagerExecutableRoutineAssistant
- __OBJC_$_INSTANCE_METHODS_NSManagedObjectContext(RTExtensions|Cloud)
- __OBJC_$_INSTANCE_METHODS_RTTripSegmentManager
- __OBJC_$_INSTANCE_VARIABLES_RTLearnedLocationOfInterestMO
- ___101-[RTBluePOIMonitor _updateLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:error:]_block_invoke_2
- ___101-[RTBluePOIMonitor _updateLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:error:]_block_invoke_3
- ___102-[RTLearnedLocationReconcilerPerDevice collapseReconciledVisitsToLocationsOfInterest:context:handler:]_block_invoke.91
- ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.412
- ___122-[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:error:]_block_invoke.132
- ___122-[RTInferredMapItemFuser fusedInferredMapItemsUsingCandidates:referenceLocation:snapToBestKnownPlace:snapToBestAoi:error:]_block_invoke.133
- ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke.95
- ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke_2
- ___131-[RTBluePOIMonitor _fetchLocalMapItemsFromReferenceLocation:locations:accessPoints:signalEnv:skipAggregation:collectMetrics:error:]_block_invoke_3
- ___25-[RTDaemonClient restore]_block_invoke.745
- ___25-[RTDaemonClient restore]_block_invoke.748
- ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.264
- ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.265
- ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.266
- ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.267
- ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.271
- ___264-[RTTripSegmentManager _addTripSegmentDataWithIdentifier:dateInterval:tripDistance:tripDistanceUncertainty:modeOfTransportation:locations:roads:isEndOfSegment:originLocation:destinationLocation:tripSegSequenceNumber:tripSegSequenceNumberMax:tripCommuteID:handler:]_block_invoke.272
- ___27-[RTLifeCycleManager _exit]_block_invoke.724
- ___27-[RTLifeCycleManager _exit]_block_invoke.730
- ___27-[RTLifeCycleManager _exit]_block_invoke.732
- ___27-[RTLifeCycleManager _exit]_block_invoke.733
- ___27-[RTLifeCycleManager _exit]_block_invoke_2.731
- ___28-[RTHealthKitManager _setup]_block_invoke.625
- ___28-[RTLifeCycleManager _start]_block_invoke.709
- ___28-[RTLifeCycleManager _start]_block_invoke.715
- ___28-[RTLifeCycleManager _start]_block_invoke.718
- ___28-[RTLifeCycleManager _start]_block_invoke.721
- ___41-[RTAssetManager _downloadAsset:handler:]_block_invoke.362
- ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.726
- ___47-[RTClientListener _setupConnection:forClient:]_block_invoke.312
- ___48-[RTFeatureExtractor _getHomeKitHomesWithError:]_block_invoke.449
- ___49-[RTTripSegmentManager isOKToAddTripSegmentdata:]_block_invoke
- ___49-[RTTripSegmentManager isOKToAddTripSegmentdata:]_block_invoke.251
- ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.772
- ___51-[RTLearnedLocationEngine _getDailyTrainingMetrics]_block_invoke.809
- ___51-[RTLearnedLocationEngine _teardownTrainingMetrics]_block_invoke.865
- ___52-[RTLearnedLocationEngine _createLOIForPlace:error:]_block_invoke.891
- ___52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.689
- ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.670
- ___55-[RTLearnedLocationEngine _retrainVisitsWithoutPlaces:]_block_invoke.867
- ___55-[RTLearnedLocationEngine trainForReason:mode:handler:]_block_invoke.649
- ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.765
- ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.766
- ___57-[SMSessionMetricManager _gatherSessionDestinationStats:]_block_invoke.681
- ___58-[RTFeatureExtractor _getVisitsWithDateInterval:outError:]_block_invoke.417
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.492
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.499
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.503
- ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.838
- ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.273
- ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.274
- ___59-[RTTripSegmentManager _deleteTripSegmentWithUUID:handler:]_block_invoke.275
- ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.584
- ___62-[RTDaemonClientInternal connection:handleInvocation:isReply:]_block_invoke.494
- ___63-[RTFeatureExtractor _getTransitionsWithDateInterval:outError:]_block_invoke.419
- ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.689
- ___65-[RTTripSegmentManager _purgeTripSegmentsOnDateInterval:handler:]_block_invoke.283
- ___65-[RTTripSegmentManager _purgeTripSegmentsOnDateInterval:handler:]_block_invoke.284
- ___66-[RTFeatureExtractor _getCalendarEventsWithDateInterval:outError:]_block_invoke.438
- ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.737
- ___68-[RTFeatureExtractor _getMapsViewedPlacesWithDateInterval:outError:]_block_invoke.443
- ___68-[RTFeatureExtractor _getMotionActivitiesWithDateInterval:outError:]_block_invoke.445
- ___68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.604
- ___68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.607
- ___69-[RTDaemonClient remoteStatusRegistrar:didReceiveRemoteStatus:error:]_block_invoke.773
- ___69-[RTFeatureExtractor _getLocationHistoriesWithDateInterval:outError:]_block_invoke.436
- ___69-[RTTripSegmentManager _fetchTripSegmentMetadataWithOptions:handler:]_block_invoke.234
- ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.764
- ___70-[RTLearnedLocationEngine _saveIdentifiersOfKnownPlaceTypesWithError:]_block_invoke.786
- ___70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke.596
- ___70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke_2.597
- ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.291
- ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.292
- ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.293
- ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.295
- ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.296
- ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.297
- ___70-[RTTripSegmentManager _sanitizeTripSegmentDatabaseSinceDate:handler:]_block_invoke.298
- ___71-[RTFeatureExtractor _getLocationsOfInterestWithDateInterval:outError:]_block_invoke.434
- ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke.852
- ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke_2.853
- ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.515
- ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.749
- ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.557
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.466
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.470
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.481
- ___74-[RTLearnedLocationEngine _relabelWithRelabeler:relabelerPersister:error:]_block_invoke.747
- ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.800
- ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.801
- ___75-[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]_block_invoke.804
- ___75-[RTLearnedLocationEngine requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.681
- ___76-[RTAssetManager initWithDefaultsManager:assetProcessor:xpcActivityManager:]_block_invoke.301
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.732
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.733
- ___76-[RTLearnedLocationEngine _appendVisitsToLocationsOfInterestModelWithError:]_block_invoke.869
- ___76-[RTLearnedLocationEngine _requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.682
- ___76-[RTVisitLabeler startWiFiScanForLabelling:clientIdentifier:policy:handler:]_block_invoke
- ___76-[RTVisitLabeler startWiFiScanForLabelling:clientIdentifier:policy:handler:]_block_invoke.26
- ___77-[RTFeatureExtractor _getMapsHistoricalNavigationsWithDateInterval:outError:]_block_invoke.441
- ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.611
- ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke.220
- ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke_2
- ___78-[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]_block_invoke_3
- ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.768
- ___79-[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]_block_invoke.801
- ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.721
- ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.740
- ___82-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]_block_invoke.901
- ___82-[RTLearnedLocationEngine _findVisitsAssociatedWithHistoricalVisitCuration:error:]_block_invoke.902
- ___83-[RTDaemonClient predictedContextRegistrar:didReceivePredictedContextResult:error:]_block_invoke.812
- ___83-[RTLearnedLocationEngine _recoverKnownPlaceTypesWithPlaceTypeClassifier:outError:]_block_invoke.808
- ___89-[RTMapServiceManager fetchConfidenceWeightForMapItem:startDate:endDate:options:handler:]_block_invoke
- ___89-[RTMapServiceManager fetchConfidenceWeightForMapItem:startDate:endDate:options:handler:]_block_invoke_2
- ___92-[RTVisitLabeler _collectWiFiScansAndLabelVisit:clientIdentifier:policy:maxRetries:handler:]_block_invoke.27
- ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.676
- ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.421
- ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.425
- ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.427
- ___block_descriptor_48_e8_32s40r_e30_v24?0"NSNumber"8"NSError"16lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e38_"RTInferredMapItem"16?0"RTMapItem"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56r_e38_"RTInferredMapItem"16?0"RTMapItem"8ls32l8s40l8s48l8r56l8
- ___block_descriptor_66_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
- ___block_literal_global.136
- ___block_literal_global.1375
- ___block_literal_global.1389
- ___block_literal_global.239
- ___block_literal_global.243
- ___block_literal_global.361
- ___block_literal_global.430
- ___block_literal_global.434
- ___block_literal_global.603
- ___block_literal_global.610
- ___block_literal_global.613
- ___block_literal_global.616
- ___block_literal_global.619
- ___block_literal_global.647
- ___block_literal_global.65
- ___block_literal_global.691
- ___block_literal_global.712
- ___block_literal_global.717
- ___block_literal_global.720
- ___block_literal_global.723
- ___block_literal_global.735
- ___block_literal_global.742
- ___block_literal_global.750
- ___block_literal_global.81
- ___block_literal_global.905
- ___block_literal_global.93
- ___block_literal_global.979
- _kRTVisitLabelerWiFiScanDelay
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_timeZoneFromLocation:
- _objc_msgSend$fetchConfidenceWeightForMapItem:startDate:endDate:options:handler:
- _objc_msgSend$initWithAccountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:
- _objc_msgSend$initWithQueue:accountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:
- _objc_msgSend$initWithQueue:contactsManager:distanceCalculator:learnedLocationStore:learnedPlaceTypeInferenceStore:mapServiceManager:
- _objc_msgSend$isOKToAddTripSegmentdata:
- _objc_msgSend$placeMapItemIdentifiersFromLearnedLocationsOfInterestMO:
- _objc_msgSend$shouldFilterByBusinessHours:
- _objc_msgSend$startWiFiScanForLabelling:clientIdentifier:policy:handler:
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _rand
CStrings:
+ "%@, boost high intention confidence error, %@"
+ "%@, business hours refresh for place, %{sensitive}@, last visit, %{sensitive}@, required, %@"
+ "%@, capping lookback window start, requested, %@, capped to, %@"
+ "%@, confidenceWeight, %.2f, businessHours, %.2f, duration, %.2f, muid, %lu, hasBusinessHours, %@"
+ "%@, dailyHours weekday, %lu, compareDate weekday, %lu"
+ "%@, failed to create lookback date interval, error, %@"
+ "%@, failed to remove LearnedPlaceTypeInferences, error, %@"
+ "%@, invalid MUID, skip business hours update"
+ "%@, invalid learned visit date interval, entryDate, %@, exitDate, %@, error, %@"
+ "%@, mostRecentVisit, %{sensitive}@, finalVisit, %{sensitive}@"
+ "%@, periodic purge in learned locations concluded, error, %@"
+ "%@, query window startDate (%@) is before 8-week retention boundary (%@), capping to retention boundary"
+ "%@, ready to execute request, %@"
+ "%@, start power assertion, timeout, %.1f"
+ "%@, write metadata dict %@, was succeeded, %@, updateError, %@"
+ "%@,store, %@, migration step, open, metadataState %@"
+ "%@-%@: Dropping callback to generated trip segment trigger handler because generatedTripSegment is nil"
+ "%@-%@: failed to create notification for generated trip segment"
+ "%@-%@: no delegate (%d) or does not respond to selector, returning."
+ "%@-%@: received nil generated trip segment, returning."
+ "%@-%@: sent notification for generated trip segment with identifier, %@"
+ "%@: %@"
+ "%@: Dropping callback to generated trip segments monitor handler because routine is either not enabled %d or supported %d."
+ "%@: client, %@, not connected. enqueuing generated trip segment %@"
+ "%@: nil reference to self, returning from generated trip segment block."
+ "%@: nil reference to self, returning from generated trip segment failure block."
+ "%@: sending generated trip segment, %{sensitive}@, to client, %@"
+ "%@:%@,ZDR setup locations,%{private}@"
+ "%@:%@,failed to read setup location,%{public}@"
+ "%@:%@,invalid setup locations"
+ "%@:%@,no ZDR locations"
+ "%@:%@,timeSinceZDRSetup,%{public}.3f"
+ "%@:%@,zdrAge,%{public}.3lf,zdrLocationPassTrustAgeCriteria,%{public}d,isSetupLocationTrusted,%{public}d,isValidLoc,%{public}d,isZdrSetupLocationAgeWithinExemptLimit,%{public}d,isSetupLoc,%{public}d,isZdrLocTrusted,%{public}d,isDeviceSetupRecently,%{public}d,isLearnedLocation,%{public}d,isExemptedFromWaitTime,%{public}d"
+ "%s, bypassing LOI check"
+ "%s, bypassing WiFi check"
+ "%s, enqueueing handler, created dispatcher? %@, scheduled wifi scan? %@"
+ "%{public}@, %{public}@, boosting confidence for high intention item from %f to %f, map item, %{sensitive}@"
+ "%{public}@, %{public}@, conflicting high intention signals, returning original fused items"
+ "%{public}@, %{public}@, found known place type candidate, skipping boost"
+ "%{public}@, %{public}@, high intention items have different map items (not AOI/POI pair), skipping boost"
+ "%{public}@, %{public}@, high intention items have different map items but are AOI/POI pair, continuing with boost"
+ "%{public}@, %{public}@, no high intention items found, returning original fused items"
+ "%{public}@, %{public}@, normalizing non-high-intention POI confidence from %f to %f, map item, %{sensitive}@"
+ "%{public}@, %{public}@, reducing AOI confidence from %f to %f to be below high intention AOIs, map item, %{sensitive}@"
+ "-[RTBusinessHoursArrayTransformer reverseTransformedValue:]"
+ "-[RTBusinessHoursArrayTransformer transformedValue:]"
+ "-[RTDaemonClientInternal simulateGeneratedTripSegment:withCallback:]"
+ "-[RTDaemonClientRegistrarGeneratedTripSegments enqueueGeneratedTripSegmentBlock:onFailureBlock:description:]"
+ "-[RTDaemonClientRegistrarGeneratedTripSegments onGeneratedTripSegmentNotification:]_block_invoke"
+ "-[RTTripSegmentManager _postNotificationForGeneratedTripSegment:]"
+ "-[RTTripSegmentManager(Internal) simulateGeneratedTripSegment:withCallback:]"
+ "19:25:57"
+ "4AF61239-332F-481C-B7DE-7E80973B07BF"
+ "@\"<RTDaemonClientRegistrarGeneratedTripSegmentProtocol>\""
+ "@\"RTDaemonClientRegistrarGeneratedTripSegments\""
+ "@288@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264@272@280"
+ "AccountIDEmpty"
+ "AccountIDNonExistent"
+ "AccountIDPopulated"
+ "Address identifier is nil for mapItemMO: %{sensitive}@. This indicates data corruption."
+ "BluePOIMonitorSkipBusinessHourFilter"
+ "Coordinator did not have any persistent stores with URL %@, returning nil without adding"
+ "Enqueuing generated trip segment failed."
+ "Event %lu, %{sensitive}@, %{sensitive}@, %@, %@, %@"
+ "Failed to enable malloc stack logging with mode %ld"
+ "Failed to update metadata for new database: %@"
+ "Feb  7 2026"
+ "Invalid parameter not satisfying: callback (in %s:%d)"
+ "Invalid parameter not satisfying: generatedTripSegment (in %s:%d)"
+ "Invalid parameter not satisfying: loiMO.mapItem"
+ "LearnedLocationEngineTrainLocationsOfInterestLastAttemptDate"
+ "RTBusinessHoursArrayTransformer"
+ "RTDaemonClientRegistrarGeneratedTripSegmentProtocol"
+ "RTDaemonClientRegistrarGeneratedTripSegments"
+ "RTDefaultsFamiliarityIndexAllowExtendedLookback"
+ "RTGeneratedTripSegmentNotification"
+ "RoutineToolWidgetExtension"
+ "SafePerformBlock"
+ "Setting malloc stack logging enabled: %@, mode: %ld"
+ "Successfully disabled malloc stack logging"
+ "Successfully enabled malloc stack logging with mode %ld"
+ "T@\"<RTDaemonClientRegistrarGeneratedTripSegmentProtocol>\",W,N,V_delegate"
+ "T@\"NSArray\",C,D,N"
+ "T@\"RTDaemonClientRegistrarGeneratedTripSegments\",&,N,V_generatedTripSegmentsRegistrar"
+ "T@\"RTTripSegment\",R,N,V_generatedTripSegment"
+ "TB,N,V_isMonitoring"
+ "TB,R,N,G_isCoordinateDerived"
+ "Unknown(%ld)"
+ "_backgroundProcessingAssertionsDidRelease"
+ "_createLookbackDateIntervalFromOptions:error:"
+ "_detectMetadataStateForStore:coordinator:error:"
+ "_generatedTripSegment"
+ "_generatedTripSegmentsRegistrar"
+ "_getFirstZDRCreationTime"
+ "_isCoordinateDerived"
+ "_isOKToAddTripSegmentdata:"
+ "_isUpdateLearnedPlaceWithBusinessHoursRequired:"
+ "_metadataStateToString:"
+ "_onGeneratedTripSegmentNotification:"
+ "_postNotificationForGeneratedTripSegment:"
+ "_startMonitoringForGeneratedTripSegments"
+ "_stopMonitoringForGeneratedTripSegments"
+ "_updateLearnedPlaceWithBusinessHours:"
+ "_updateStoreMetadataWithAppleIDs:coordinator:error:"
+ "addressAdministrativeArea"
+ "addressAdministrativeAreaCode"
+ "addressAreasOfInterest"
+ "addressCountry"
+ "addressCountryCode"
+ "addressCreationDate"
+ "addressExpirationDate"
+ "addressGeoAddressData"
+ "addressISO3166CountryCode"
+ "addressISO3166SubdivisionCode"
+ "addressInlandWater"
+ "addressIsland"
+ "addressLocality"
+ "addressOcean"
+ "addressPostalCode"
+ "addressSubAdministrativeArea"
+ "addressSubLocality"
+ "addressSubPremises"
+ "addressSubThoroughfare"
+ "addressThoroughfare"
+ "boostHighUserIntentionConfidences:candidates:referenceLocation:error:"
+ "confidenceWeightForMapItem:startDate:endDate:"
+ "dailyHours"
+ "enqueueGeneratedTripSegmentBlock:onFailureBlock:description:"
+ "error fetching businessHours, %@"
+ "error restoring generated trip segment registrar, %@"
+ "failed business hours array deserialization, value, %@, error, %@"
+ "failed business hours array serialization, value, %@, error, %@"
+ "failed to unarchive geoMapItemIdentifier for place, %{sensitive}@"
+ "fetchGeoMapItemWithMUID:options:handler:"
+ "fetchVisitWithIdentifier:reply:"
+ "fusedInferredMapItems"
+ "generatedTripSegment"
+ "generatedTripSegmentsRegistrar"
+ "generatedTripSegmentsRegistrar:didReceiveGeneratedTripSegment:withError:"
+ "highIntentionSource:"
+ "initWithAccountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:"
+ "initWithGeneratedTripSegment:"
+ "initWithIdentifier:name:category:categoryMUID:address:location:source:mapItemPlaceType:muid:resultProviderID:geoMapItemHandle:geoMapItemIdentifier:creationDate:expirationDate:extendedAttributes:displayLanguage:disputed:businessHours:"
+ "initWithQueue:accountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:tripSegmentManager:workoutRouteManager:workoutScheduler:"
+ "initWithQueue:contactsManager:defaultsManager:distanceCalculator:learnedLocationStore:learnedPlaceTypeInferenceStore:mapServiceManager:"
+ "initWithTripSegmentManager:onQueue:"
+ "insideRTBusinessHours:date:timeZone:"
+ "isCoordinateDerived"
+ "mapItemBusinessHours"
+ "mapItemCategory"
+ "mapItemCategoryMUID"
+ "mapItemCreationDate"
+ "mapItemDisplayLanguage"
+ "mapItemDisputed"
+ "mapItemExpirationDate"
+ "mapItemExtendedAttributesAddressIdentifier"
+ "mapItemExtendedAttributesIdentifier"
+ "mapItemExtendedAttributesIsMe"
+ "mapItemExtendedAttributesWifiConfidence"
+ "mapItemExtendedAttributesWifiFingerprintLabelType"
+ "mapItemGeoMapItemIdentifier"
+ "mapItemLatitude"
+ "mapItemLongitude"
+ "mapItemMUID"
+ "mapItemName"
+ "mapItemReferenceFrame"
+ "mapItemResultProviderID"
+ "mapItemUncertainty"
+ "no businessHours available for place, %{sensitive}@"
+ "onGeneratedTripSegment:withError:"
+ "onGeneratedTripSegmentNotification:"
+ "peekMetadataWithCoordinator:error:"
+ "peeking at metadata of store %@"
+ "postNotificationForGeneratedTripSegment:"
+ "requires a non negative delay value."
+ "rt_performBlock:"
+ "rt_performBlockAndWait:"
+ "setAddressAdministrativeArea:"
+ "setAddressAdministrativeAreaCode:"
+ "setAddressAreasOfInterest:"
+ "setAddressCountry:"
+ "setAddressCountryCode:"
+ "setAddressCreationDate:"
+ "setAddressExpirationDate:"
+ "setAddressGeoAddressData:"
+ "setAddressISO3166CountryCode:"
+ "setAddressISO3166SubdivisionCode:"
+ "setAddressInlandWater:"
+ "setAddressIsland:"
+ "setAddressLocality:"
+ "setAddressOcean:"
+ "setAddressPostalCode:"
+ "setAddressSubAdministrativeArea:"
+ "setAddressSubLocality:"
+ "setAddressSubPremises:"
+ "setAddressSubThoroughfare:"
+ "setAddressThoroughfare:"
+ "setBusinessHours:"
+ "setGeneratedTripSegmentsRegistrar:"
+ "setMallocStackLoggingEnabled:mode:handler:"
+ "setMapItemBusinessHours:"
+ "setMapItemCategory:"
+ "setMapItemCategoryMUID:"
+ "setMapItemCreationDate:"
+ "setMapItemDisplayLanguage:"
+ "setMapItemDisputed:"
+ "setMapItemExpirationDate:"
+ "setMapItemExtendedAttributesAddressIdentifier:"
+ "setMapItemExtendedAttributesIdentifier:"
+ "setMapItemExtendedAttributesIsMe:"
+ "setMapItemExtendedAttributesWifiConfidence:"
+ "setMapItemExtendedAttributesWifiFingerprintLabelType:"
+ "setMapItemGeoMapItemIdentifier:"
+ "setMapItemLatitude:"
+ "setMapItemLongitude:"
+ "setMapItemName:"
+ "setMapItemReferenceFrame:"
+ "setMapItemResultProviderID:"
+ "setMapItemUncertainty:"
+ "simulateGeneratedTripSegment:withCallback:"
+ "startMonitoringForGeneratedTripSegments"
+ "startMonitoringForGeneratedTripSegmentsWithReply:"
+ "startWiFiScanForLabelling:clientIdentifier:policy:delay:maxRetries:handler:"
+ "stopMonitoringForGeneratedTripSegments"
+ "stopMonitoringForGeneratedTripSegmentsWithReply:"
+ "store, %@, migration step, open, attempt to write metadata, reason, databaseFileDidExist %@, metadataState, %@"
+ "taking process assertion for client, %@"
+ "timeIntervals"
+ "update businessHours for place, %{sensitive}@"
+ "v24@?0@\"RTTripSegment\"8@\"NSError\"16"
+ "v32@0:8@\"NSUUID\"16@?<v@?@\"RTVisit\"@\"NSError\">24"
+ "v32@0:8@\"RTTripSegment\"16@\"NSError\"24"
+ "v32@0:8@\"RTTripSegment\"16@?<v@?@\"RTTripSegment\"@\"NSError\">24"
+ "v36@0:8B16q20@?28"
+ "v36@0:8B16q20@?<v@?@\"NSError\">28"
+ "v40@0:8@\"RTDaemonClientRegistrarGeneratedTripSegments\"16@\"RTTripSegment\"24@\"NSError\"32"
+ "v40@0:8Q16@\"RTMapServiceOptions\"24@?<v@?@\"<GEOMapItem>\"@\"NSError\">32"
+ "v64@0:8@16@24Q32d40Q48@?56"
+ "weightBasedOnRTBusinessHours:startDate:endDate:timeZone:metrics:"
- "%@, internalInstall, %@, sampled, %@"
- "%@, mostRecentVisit, %@, finalVisit, %@"
- "%@:%@,zdrAge,%{public}.3lf,zdrLocationPassTrustAgeCriteria,%{public}d,isSetupLocationTrusted,%{public}d,isValidLoc,%{public}d,isZdrAgeWithinExemptLimit,%{public}d,isSetupLoc,%{public}d,isZdrLocTrusted,%{public}d"
- "%s, enqueueing handler, created dispatcher? %@"
- "22:02:57"
- "4AF61239-2126-4FD6-8E7A-CDA2D7A0BFE9"
- "@272@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248@256@264"
- "Event %lu, %@, %@, %@, %@, %@"
- "Invalid parameter not satisfying: loiMO.placeMapItemIdentifier"
- "Jan 16 2026"
- "RoutineAssistant"
- "fetchConfidenceWeightForMapItem:startDate:endDate:options:handler:"
- "initWithAccountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:"
- "initWithQueue:accountManager:assetManager:authorizationManager:bluePOITileManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:predictedContextManager:purgeManager:safetyCacheStore:scenarioTriggerManager:userCurationManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:"
- "initWithQueue:contactsManager:distanceCalculator:learnedLocationStore:learnedPlaceTypeInferenceStore:mapServiceManager:"
- "isOKToAddTripSegmentdata:"
- "options.lookbackWindow can not be set after the dateInterval.startDate"
- "shouldFilterByBusinessHours:"
- "startWiFiScanForLabelling:clientIdentifier:policy:handler:"
- "taking process asssertion for client, %@"
- "v56@0:8@\"RTMapItem\"16@\"NSDate\"24@\"NSDate\"32@\"RTMapServiceOptions\"40@?<v@?@\"NSNumber\"@\"NSError\">48"

```
