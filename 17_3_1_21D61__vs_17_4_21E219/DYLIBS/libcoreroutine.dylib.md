## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-896.0.1.0.1
-  __TEXT.__text: 0x4530e8
-  __TEXT.__auth_stubs: 0x1850
-  __TEXT.__objc_methlist: 0x22558
-  __TEXT.__const: 0x1ab8
-  __TEXT.__gcc_except_tab: 0x16b84
-  __TEXT.__oslogstring: 0x50f3c
-  __TEXT.__cstring: 0x33656
+900.0.12.0.0
+  __TEXT.__text: 0x4691b0
+  __TEXT.__auth_stubs: 0x1880
+  __TEXT.__objc_methlist: 0x22e38
+  __TEXT.__const: 0x1ac8
+  __TEXT.__gcc_except_tab: 0x17520
+  __TEXT.__oslogstring: 0x52158
+  __TEXT.__cstring: 0x3451f
   __TEXT.__ustring: 0x16
   __TEXT.__dlopen_cstrs: 0x254
-  __TEXT.__unwind_info: 0xa6f8
-  __TEXT.__objc_classname: 0x4463
-  __TEXT.__objc_methname: 0x6a66f
-  __TEXT.__objc_methtype: 0xa3e3
-  __TEXT.__objc_stubs: 0x3fe20
-  __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__const: 0xb6e0
-  __DATA_CONST.__objc_classlist: 0x1080
-  __DATA_CONST.__objc_catlist: 0x2c0
+  __TEXT.__unwind_info: 0xa964
+  __TEXT.__objc_classname: 0x4511
+  __TEXT.__objc_methname: 0x6bcff
+  __TEXT.__objc_methtype: 0xa6f9
+  __TEXT.__objc_stubs: 0x40b00
+  __DATA_CONST.__got: 0xa70
+  __DATA_CONST.__const: 0xb9c0
+  __DATA_CONST.__objc_classlist: 0x10b0
+  __DATA_CONST.__objc_catlist: 0x2c8
   __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x334a0
-  __DATA_CONST.__objc_selrefs: 0x12648
-  __DATA_CONST.__objc_arraydata: 0x19c8
-  __AUTH_CONST.__const: 0x2620
-  __AUTH_CONST.__cfstring: 0x1f0c0
-  __AUTH_CONST.__objc_const: 0xda50
-  __AUTH_CONST.__objc_intobj: 0x2bb0
+  __DATA_CONST.__objc_const: 0x34360
+  __DATA_CONST.__objc_selrefs: 0x129d8
+  __DATA_CONST.__objc_protorefs: 0x108
+  __DATA_CONST.__objc_classrefs: 0x1cb8
+  __DATA_CONST.__objc_superrefs: 0xe50
+  __DATA_CONST.__objc_arraydata: 0x1f58
+  __AUTH_CONST.__const: 0x2680
+  __AUTH_CONST.__cfstring: 0x1fc60
+  __AUTH_CONST.__objc_const: 0xdd18
+  __AUTH_CONST.__objc_intobj: 0x30a8
   __AUTH_CONST.__objc_doubleobj: 0x900
-  __AUTH_CONST.__objc_arrayobj: 0xbb8
-  __AUTH_CONST.__objc_dictobj: 0xa0
+  __AUTH_CONST.__objc_arrayobj: 0xbd0
+  __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__auth_got: 0xc38
-  __AUTH.__objc_data: 0x20d0
-  __DATA.__objc_protorefs: 0x108
-  __DATA.__objc_classrefs: 0x1c60
-  __DATA.__objc_superrefs: 0xe30
-  __DATA.__objc_ivar: 0x1c38
-  __DATA.__data: 0x2468
+  __AUTH_CONST.__auth_got: 0xc50
+  __AUTH.__objc_data: 0x1cc0
+  __DATA.__objc_ivar: 0x1c90
+  __DATA.__data: 0x2488
   __DATA.__bss: 0x60
-  __DATA_DIRTY.__objc_ivar: 0xc10
-  __DATA_DIRTY.__objc_data: 0x8430
-  __DATA_DIRTY.__data: 0x498
+  __DATA_DIRTY.__objc_ivar: 0xca4
+  __DATA_DIRTY.__objc_data: 0x8a20
+  __DATA_DIRTY.__data: 0x4b0
   __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
   - /System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester
   - /System/Library/PrivateFrameworks/PersistentConnection.framework/PersistentConnection

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0B04E158-6B46-378B-9FAF-1CE62751EA39
-  Functions: 14974
-  Symbols:   49034
-  CStrings:  30170
+  UUID: 1EC1E131-1CDC-3640-B78D-07947ED0B613
+  Functions: 15231
+  Symbols:   49776
+  CStrings:  30656
 
Symbols:
+ +[RTBiomeManager biomeStreamTypeToBiomeStream:]
+ +[RTBiomeManager streamTypeToString:]
+ +[RTPlaceDataMetrics DataSourceToString:]
+ +[RTPlaceDataMetrics calculateMLFeaturesUsingBiomeManager:intervalDictionary:startDate:endDate:createBucketedFeatures:]
+ +[RTPlaceInferenceManager periodicPurgePolicy]
+ +[RTPlaceInferenceQuery(RTCoreDataTransformable) createWithManagedObject:]
+ +[RTPlaceInferenceQuery(RTCoreDataTransformable) createWithPlaceInferenceQueryMO:]
+ +[RTPlaceInferenceQueryMO managedObjectWithPlaceInferenceQuery:inManagedObjectContext:]
+ +[RTPlaceInferenceQueryMO(CoreDataProperties) fetchRequest]
+ +[RTWiFiManager_MobileWiFi activeScanRequest]
+ +[SMTriggerDestination convertSMDirectionTransportTypeToMKDirectionTransportType:]
+ +[SMTriggerDestination convertSMDirectionTransportTypeToString:]
+ -[RTAddressMO debugDescription]
+ -[RTAuthorizedLocation ageDaysFirstRegisteredVisit]
+ -[RTAuthorizedLocation ageDaysFirstVisit]
+ -[RTAuthorizedLocation initWithLoi:dwellTime:numberOfDaysVisited:ageDaysFirstVisit:ageDaysFirstRegisteredVisit:]
+ -[RTAuthorizedLocationCurationMetrics ageDaysFirstAnyLoiVisit]
+ -[RTAuthorizedLocationCurationMetrics ageDaysFirstTopLoiGeoVisit]
+ -[RTAuthorizedLocationCurationMetrics ageDaysFirstTopLoiRegisteredVisit]
+ -[RTAuthorizedLocationCurationMetrics ageDaysFirstTopLoiVisit]
+ -[RTAuthorizedLocationCurationMetrics ageDaysRegistry]
+ -[RTAuthorizedLocationCurationMetrics init]
+ -[RTAuthorizedLocationCurationMetrics maxCumulativeDwellTimeForNotFamiliarLoiHours]
+ -[RTAuthorizedLocationCurationMetrics maxUniqueVisitDaysForNotFamiliarLois]
+ -[RTAuthorizedLocationCurationMetrics registrationUsesBestTimeFraction]
+ -[RTAuthorizedLocationCurationMetrics setAgeDaysFirstAnyLoiVisit:]
+ -[RTAuthorizedLocationCurationMetrics setAgeDaysFirstTopLoiGeoVisit:]
+ -[RTAuthorizedLocationCurationMetrics setAgeDaysFirstTopLoiRegisteredVisit:]
+ -[RTAuthorizedLocationCurationMetrics setAgeDaysFirstTopLoiVisit:]
+ -[RTAuthorizedLocationCurationMetrics setAgeDaysRegistry:]
+ -[RTAuthorizedLocationCurationMetrics setMaxCumulativeDwellTimeForNotFamiliarLoiHours:]
+ -[RTAuthorizedLocationCurationMetrics setMaxUniqueVisitDaysForNotFamiliarLois:]
+ -[RTAuthorizedLocationCurationMetrics setRegistrationUsesBestTimeFraction:]
+ -[RTAuthorizedLocationCurationMetrics setVisitRegistrationFraction:]
+ -[RTAuthorizedLocationCurationMetrics visitRegistrationFraction]
+ -[RTAuthorizedLocationManager _assertRecentLocationTechnologyQualityForAuthorizedLocation:visit:]
+ -[RTAuthorizedLocationManager _assertRecentMotionActivityAndLocationHistoryAreConsistentForAuthorizedLocation:visit:]
+ -[RTAuthorizedLocationManager _decodeTimeSourceWithValue:isRetroRegistration:isTrusted:]
+ -[RTAuthorizedLocationManager _encodeTimeSourceWithValue:isTrusted:isRetroRegistration:]
+ -[RTAuthorizedLocationManager _fetchCurrentLocationWithHandler:]
+ -[RTAuthorizedLocationManager _updateReferenceTimeBoundsFromVisitLog]
+ -[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]
+ -[RTAuthorizedLocationManager curationMetrics]
+ -[RTAuthorizedLocationManager lastMetricSubmissionDate]
+ -[RTAuthorizedLocationManager setCurationMetrics:]
+ -[RTAuthorizedLocationManager setLastMetricSubmissionDate:]
+ -[RTAuthorizedLocationQueryMetrics curationMetrics]
+ -[RTAuthorizedLocationQueryMetrics historicalRejectionReasonCode]
+ -[RTAuthorizedLocationQueryMetrics historicalRejectionSpeedMps]
+ -[RTAuthorizedLocationQueryMetrics locationAgeMinutes]
+ -[RTAuthorizedLocationQueryMetrics setCurationMetrics:]
+ -[RTAuthorizedLocationQueryMetrics setHistoricalRejectionReasonCode:]
+ -[RTAuthorizedLocationQueryMetrics setHistoricalRejectionSpeedMps:]
+ -[RTAuthorizedLocationQueryMetrics setLocationAgeMinutes:]
+ -[RTAuthorizedLocationQueryMetrics setMotionSpeedLimitRejectionCodeFromLookbackHours:]
+ -[RTBiomeManager .cxx_destruct]
+ -[RTBiomeManager _compareEvent1:event2:streamType:]
+ -[RTBiomeManager _extractDateIntervalFromBiomeEvent1:event2:streamType:]
+ -[RTBiomeManager _isValidEvent:streamType:]
+ -[RTBiomeManager _setup]
+ -[RTBiomeManager defaultsManager]
+ -[RTBiomeManager enumerateEventsWithinDateInterval:streamType:handler:]
+ -[RTBiomeManager initWithDefaultsManager:platform:]
+ -[RTBiomeManager platform]
+ -[RTClientListenerInternal initWithAccountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:]
+ -[RTClientListenerInternal mapServiceManager]
+ -[RTClientListenerInternal placeInferenceQueryStore]
+ -[RTClientListenerInternal pointOfInterestSampler]
+ -[RTClientListenerInternal setMapServiceManager:]
+ -[RTClientListenerInternal setPlaceInferenceQueryStore:]
+ -[RTClientListenerInternal setPointOfInterestSampler:]
+ -[RTDaemonClientInternal fetchPlaceInferenceQueriesWithDateInterval:ascending:reply:]
+ -[RTDaemonClientInternal fetchPointOfInterestAttributesWithIdentifier:reply:]
+ -[RTDaemonClientInternal fetchPointOfInterestsAroundCoordinate:radius:reply:]
+ -[RTDaemonClientInternal initWithQueue:accountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:]
+ -[RTDaemonClientInternal mapServiceManager]
+ -[RTDaemonClientInternal placeInferenceQueryStore]
+ -[RTDaemonClientInternal pointOfInterestSampler]
+ -[RTDaemonClientInternal setMapServiceManager:]
+ -[RTDaemonClientInternal setPlaceInferenceQueryStore:]
+ -[RTDaemonClientInternal setPointOfInterestSampler:]
+ -[RTDaemonClientInternal startSamplingPointOfInterestWithInterval:handler:]
+ -[RTDaemonClientInternal stopSamplingPointOfInterest:]
+ -[RTDeviceLocationPredictor initWithQueue:authorizationManager:defaultsManager:distanceCalculator:learnedLocationManager:locationManager:mapServiceManager:metricManager:platform:providers:]
+ -[RTLearnedLocationEngine _maximumExpirationDateForLearnedPlace:]
+ -[RTLearnedLocationEngine biomeManager]
+ -[RTLearnedLocationEngine initWithAccountManager:biomeManager:contactsManager:dailyTrainingSessionCounter:defaultsManager:diagnostics:distanceCalculator:elevationManager:eventManager:fingerprintManager:learnedLocationStore:learnedPlaceTypeInferenceStore:locationManager:locationStore:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:platform:pointOfInterestMetricsManager:portraitManager:reconcilerPerVisit:reconcilerPerDevice:settledStateTransitionStore:transitMetricManager:tripSegmentProvider:visitManager:xpcActivityManager:]
+ -[RTLearnedLocationEngine pointOfInterestMetricsManager]
+ -[RTLearnedPlaceTypeInferenceGenerator biomeManager]
+ -[RTLearnedPlaceTypeInferenceGenerator initWithBiomeManager:defaultsManager:distanceCalculator:learnedLocationStore:placeTypeClassifierMetricsCalculator:platform:]
+ -[RTLearnedPlaceTypeInferenceGenerator setBiomeManager:]
+ -[RTLocationManager trustedTimeCache]
+ -[RTMapItemMO debugDescription]
+ -[RTMapServiceManager fetchPointOfInterestAttributesWithIdentifier:options:handler:]
+ -[RTMapServiceManager fetchPointOfInterestsAroundCoordinate:radius:options:handler:]
+ -[RTNavigationManager navigationListener:didChangeNavigationState:transportType:]
+ -[RTPlaceDataMetrics setMLMetricsFromFeaturesDict:sourceName:]
+ -[RTPlaceInferenceManager _performPurgeOfType:referenceDate:completion:]
+ -[RTPlaceInferenceManager _savePlaceInferenceQueriesFromInferredMapItems:referenceLocation:options:outError:]
+ -[RTPlaceInferenceManager initWithQueue:defaultsManager:distanceCalculator:eventManager:fingerprintManager:inferredMapItemFuser:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:placeInferenceQueryStore:platform:portraitManager:visitStore:]
+ -[RTPlaceInferenceManager performPurgeOfType:referenceDate:completion:]
+ -[RTPlaceInferenceManager placeInferenceQueryStore]
+ -[RTPlaceInferenceQuery(RTCoreDataTransformable) managedObjectWithContext:]
+ -[RTPlaceInferenceQueryMO .cxx_destruct]
+ -[RTPlaceInferenceQueryMO cachedMapItem]
+ -[RTPlaceInferenceQueryMO setCachedMapItem:]
+ -[RTPlaceInferenceQueryMO(CoreDataProperties) mapItem]
+ -[RTPlaceInferenceQueryMO(CoreDataProperties) setMapItem:]
+ -[RTPlaceInferenceQueryStore _fetchPlaceInferenceQueriesWithDateInterval:ascending:handler:]
+ -[RTPlaceInferenceQueryStore _purgePlaceInferenceQueriesPredating:handler:]
+ -[RTPlaceInferenceQueryStore _storePlaceInferenceQuery:handler:]
+ -[RTPlaceInferenceQueryStore fetchPlaceInferenceQueriesWithDateInterval:ascending:handler:]
+ -[RTPlaceInferenceQueryStore purgePlaceInferenceQueriesPredating:handler:]
+ -[RTPlaceInferenceQueryStore storePlaceInferenceQuery:handler:]
+ -[RTPlaceTypeClassifier biomeManager]
+ -[RTPlaceTypeClassifier initWithBiomeManager:contactsManager:defaultsManager:distanceCalculator:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:placeTypeClassifierMetricsCalculator:platform:queue:visitManager:]
+ -[RTPlaceTypeClassifier setBiomeManager:]
+ -[RTPlaceTypeClassifierExpertInferred biomeManager]
+ -[RTPlaceTypeClassifierExpertInferred initWithBiomeManager:defaultsManager:distanceCalculator:learnedLocationStore:placeTypeClassifierMetricsCalculator:platform:]
+ -[RTPlaceTypeClassifierExpertInferred setBiomeManager:]
+ -[RTPointOfInterestMetricsManager .cxx_destruct]
+ -[RTPointOfInterestMetricsManager _onLearnedLocationStoreNotification:]
+ -[RTPointOfInterestMetricsManager _onLeechedLocationNotification:]
+ -[RTPointOfInterestMetricsManager _onNavigationNotification:]
+ -[RTPointOfInterestMetricsManager _onVisitManagerVisitIncidentNotification:]
+ -[RTPointOfInterestMetricsManager _registerForNotifications]
+ -[RTPointOfInterestMetricsManager _setup]
+ -[RTPointOfInterestMetricsManager _shouldCollectQueriesForMapItem:]
+ -[RTPointOfInterestMetricsManager _shutdown]
+ -[RTPointOfInterestMetricsManager _unRegisterForNotifications]
+ -[RTPointOfInterestMetricsManager _updateLocationDenyList]
+ -[RTPointOfInterestMetricsManager batteryManager]
+ -[RTPointOfInterestMetricsManager collectMetricsWithError:]
+ -[RTPointOfInterestMetricsManager currentSignalEnvironmentType]
+ -[RTPointOfInterestMetricsManager defaultsManager]
+ -[RTPointOfInterestMetricsManager distanceCalculator]
+ -[RTPointOfInterestMetricsManager getTruthPointOfInterestIdentifier]
+ -[RTPointOfInterestMetricsManager initWithBatteryManager:defaultsManager:distanceCalculator:learnedLocationStore:locationManager:mapServiceManager:navigationManager:placeInferenceQueryStore:pointOfInterestSampler:scenarioTriggerManager:timerManager:visitManager:]
+ -[RTPointOfInterestMetricsManager init]
+ -[RTPointOfInterestMetricsManager learnedLocationStore]
+ -[RTPointOfInterestMetricsManager locationDenyList]
+ -[RTPointOfInterestMetricsManager locationManager]
+ -[RTPointOfInterestMetricsManager mapServiceManager]
+ -[RTPointOfInterestMetricsManager navigationManager]
+ -[RTPointOfInterestMetricsManager onLearnedLocationStoreNotification:]
+ -[RTPointOfInterestMetricsManager onLeechedLocationNotification:]
+ -[RTPointOfInterestMetricsManager onNavigationNotification:]
+ -[RTPointOfInterestMetricsManager onSettledNotification:]
+ -[RTPointOfInterestMetricsManager onUnsettledNotification:]
+ -[RTPointOfInterestMetricsManager onVisitManagerVisitIncidentNotification:]
+ -[RTPointOfInterestMetricsManager placeInferenceQueryStore]
+ -[RTPointOfInterestMetricsManager pointOfInterestSampler]
+ -[RTPointOfInterestMetricsManager processQueries:visitEntryDate:poiIdentifier:]
+ -[RTPointOfInterestMetricsManager samplingPointOfInterest]
+ -[RTPointOfInterestMetricsManager samplingTimer]
+ -[RTPointOfInterestMetricsManager scenarioTriggerManager]
+ -[RTPointOfInterestMetricsManager setCurrentSignalEnvironmentType:]
+ -[RTPointOfInterestMetricsManager setSamplingPointOfInterest:]
+ -[RTPointOfInterestMetricsManager setSamplingTimer:]
+ -[RTPointOfInterestMetricsManager setSettledState:]
+ -[RTPointOfInterestMetricsManager settledState]
+ -[RTPointOfInterestMetricsManager shutdownWithHandler:]
+ -[RTPointOfInterestMetricsManager submitMetricsWithError:]
+ -[RTPointOfInterestMetricsManager timerManager]
+ -[RTPointOfInterestMetricsManager visitManager]
+ -[RTPointOfInterestSampler .cxx_destruct]
+ -[RTPointOfInterestSampler _addRequester:samplingInterval:]
+ -[RTPointOfInterestSampler _removeRequester:]
+ -[RTPointOfInterestSampler _shutdownWithHandler:]
+ -[RTPointOfInterestSampler _startSampling]
+ -[RTPointOfInterestSampler _updateSamplingInterval]
+ -[RTPointOfInterestSampler accessPoints]
+ -[RTPointOfInterestSampler defaultsManager]
+ -[RTPointOfInterestSampler initWithDefaultsManager:locationManager:placeInferenceManager:timerManager:wifiManager:]
+ -[RTPointOfInterestSampler init]
+ -[RTPointOfInterestSampler locationManager]
+ -[RTPointOfInterestSampler onWiFiScanNotification:]
+ -[RTPointOfInterestSampler placeInferenceManager]
+ -[RTPointOfInterestSampler registeredForWifiScan]
+ -[RTPointOfInterestSampler requesters]
+ -[RTPointOfInterestSampler running]
+ -[RTPointOfInterestSampler samplingInterval]
+ -[RTPointOfInterestSampler samplingTimer]
+ -[RTPointOfInterestSampler setAccessPoints:]
+ -[RTPointOfInterestSampler setRegisteredForWifiScan:]
+ -[RTPointOfInterestSampler setRequesters:]
+ -[RTPointOfInterestSampler setRunning:]
+ -[RTPointOfInterestSampler setSamplingInterval:]
+ -[RTPointOfInterestSampler setSamplingTimer:]
+ -[RTPointOfInterestSampler setShouldRun:]
+ -[RTPointOfInterestSampler setWifiScanTimer:]
+ -[RTPointOfInterestSampler shouldRun]
+ -[RTPointOfInterestSampler startSamplingPointOfInterestFromRequester:samplingInterval:]
+ -[RTPointOfInterestSampler stopSamplingPointOfInterestFromRequester:]
+ -[RTPointOfInterestSampler timerManager]
+ -[RTPointOfInterestSampler wifiManager]
+ -[RTPointOfInterestSampler wifiScanTimer]
+ -[RTStore purgeDateInterval:predicateMappings:purgeLimit:handler:]
+ -[RTVisitMO debugDescription]
+ -[RTWiFiManager _scheduleActiveScan]
+ -[RTWiFiManager scheduleActiveScan]
+ -[RTWiFiManager_MobileWiFi _scheduleActiveScan]
+ -[SMDaemonClient initializeAndStartSessionWithConfiguration:handler:]
+ -[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]
+ -[SMInitiatorService initializeAndStartSessionWithConfiguration:handler:]
+ GCC_except_table111
+ GCC_except_table112
+ GCC_except_table127
+ GCC_except_table169
+ GCC_except_table172
+ GCC_except_table187
+ GCC_except_table198
+ GCC_except_table200
+ GCC_except_table215
+ GCC_except_table217
+ GCC_except_table221
+ _AnalyticsIsEventUsed
+ _BiomeLibrary
+ _OBJC_CLASS_$_BMPublisherOptions
+ _OBJC_CLASS_$_OSASystemConfiguration
+ _OBJC_CLASS_$_RTAuthorizedLocationCurationMetrics
+ _OBJC_CLASS_$_RTBiomeManager
+ _OBJC_CLASS_$_RTCoordinate
+ _OBJC_CLASS_$_RTPlaceInferenceQuery
+ _OBJC_CLASS_$_RTPlaceInferenceQueryMO
+ _OBJC_CLASS_$_RTPlaceInferenceQueryStore
+ _OBJC_CLASS_$_RTPointOfInterestAttributes
+ _OBJC_CLASS_$_RTPointOfInterestMetricsManager
+ _OBJC_CLASS_$_RTPointOfInterestSampler
+ _OBJC_IVAR_$_RTAuthorizedLocation._ageDaysFirstRegisteredVisit
+ _OBJC_IVAR_$_RTAuthorizedLocation._ageDaysFirstVisit
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._ageDaysFirstAnyLoiVisit
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._ageDaysFirstTopLoiGeoVisit
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._ageDaysFirstTopLoiRegisteredVisit
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._ageDaysFirstTopLoiVisit
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._ageDaysRegistry
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._maxCumulativeDwellTimeForNotFamiliarLoiHours
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._maxUniqueVisitDaysForNotFamiliarLois
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._registrationUsesBestTimeFraction
+ _OBJC_IVAR_$_RTAuthorizedLocationCurationMetrics._visitRegistrationFraction
+ _OBJC_IVAR_$_RTAuthorizedLocationQueryMetrics._curationMetrics
+ _OBJC_IVAR_$_RTAuthorizedLocationQueryMetrics._historicalRejectionReasonCode
+ _OBJC_IVAR_$_RTAuthorizedLocationQueryMetrics._historicalRejectionSpeedMps
+ _OBJC_IVAR_$_RTAuthorizedLocationQueryMetrics._locationAgeMinutes
+ _OBJC_IVAR_$_RTDaemonClientInternal._mapServiceManager
+ _OBJC_IVAR_$_RTDaemonClientInternal._placeInferenceQueryStore
+ _OBJC_IVAR_$_RTDaemonClientInternal._pointOfInterestSampler
+ _OBJC_IVAR_$_RTLearnedLocationEngine._biomeManager
+ _OBJC_IVAR_$_RTLearnedLocationEngine._pointOfInterestMetricsManager
+ _OBJC_IVAR_$_RTLearnedPlaceTypeInferenceGenerator._biomeManager
+ _OBJC_IVAR_$_RTPlaceInferenceQueryMO.cachedMapItem
+ _OBJC_IVAR_$_RTPlaceTypeClassifier._biomeManager
+ _OBJC_IVAR_$_RTPlaceTypeClassifierExpertInferred._biomeManager
+ _OBJC_METACLASS_$_RTAuthorizedLocationCurationMetrics
+ _OBJC_METACLASS_$_RTBiomeManager
+ _OBJC_METACLASS_$_RTPlaceInferenceQueryMO
+ _OBJC_METACLASS_$_RTPlaceInferenceQueryStore
+ _OBJC_METACLASS_$_RTPointOfInterestMetricsManager
+ _OBJC_METACLASS_$_RTPointOfInterestSampler
+ _RTAnalyticsEventBluePoiMetrics
+ _RTBiomeStreamErrorDomain
+ _RTLogFacilityBiome
+ _RTLogFacilityTrustedTime
+ __OBJC_$_CATEGORY_RTPlaceInferenceQuery_$_RTCoreDataTransformable
+ __OBJC_$_CLASS_METHODS_RTBiomeManager
+ __OBJC_$_CLASS_METHODS_RTPlaceInferenceQuery(RTCoreDataTransformable)
+ __OBJC_$_CLASS_METHODS_RTPlaceInferenceQueryMO(CoreDataProperties)
+ __OBJC_$_INSTANCE_METHODS_RTAddressMO(CoreDataProperties)
+ __OBJC_$_INSTANCE_METHODS_RTAuthorizedLocationCurationMetrics
+ __OBJC_$_INSTANCE_METHODS_RTBiomeManager
+ __OBJC_$_INSTANCE_METHODS_RTPlaceInferenceQuery(RTCoreDataTransformable)
+ __OBJC_$_INSTANCE_METHODS_RTPlaceInferenceQueryMO(CoreDataProperties)
+ __OBJC_$_INSTANCE_METHODS_RTPlaceInferenceQueryStore
+ __OBJC_$_INSTANCE_METHODS_RTPointOfInterestMetricsManager
+ __OBJC_$_INSTANCE_METHODS_RTPointOfInterestSampler
+ __OBJC_$_INSTANCE_VARIABLES_RTAuthorizedLocationCurationMetrics
+ __OBJC_$_INSTANCE_VARIABLES_RTBiomeManager
+ __OBJC_$_INSTANCE_VARIABLES_RTPlaceInferenceQueryMO
+ __OBJC_$_INSTANCE_VARIABLES_RTPointOfInterestMetricsManager
+ __OBJC_$_INSTANCE_VARIABLES_RTPointOfInterestSampler
+ __OBJC_$_PROP_LIST_RTAuthorizedLocationCurationMetrics
+ __OBJC_$_PROP_LIST_RTBiomeManager
+ __OBJC_$_PROP_LIST_RTPointOfInterestMetricsManager
+ __OBJC_$_PROP_LIST_RTPointOfInterestSampler
+ __OBJC_CLASS_PROTOCOLS_$_RTPlaceInferenceManager
+ __OBJC_CLASS_PROTOCOLS_$_RTPlaceInferenceQuery(RTCoreDataTransformable)
+ __OBJC_CLASS_RO_$_RTAuthorizedLocationCurationMetrics
+ __OBJC_CLASS_RO_$_RTBiomeManager
+ __OBJC_CLASS_RO_$_RTPlaceInferenceQueryMO
+ __OBJC_CLASS_RO_$_RTPlaceInferenceQueryStore
+ __OBJC_CLASS_RO_$_RTPointOfInterestMetricsManager
+ __OBJC_CLASS_RO_$_RTPointOfInterestSampler
+ __OBJC_METACLASS_RO_$_RTAuthorizedLocationCurationMetrics
+ __OBJC_METACLASS_RO_$_RTBiomeManager
+ __OBJC_METACLASS_RO_$_RTPlaceInferenceQueryMO
+ __OBJC_METACLASS_RO_$_RTPlaceInferenceQueryStore
+ __OBJC_METACLASS_RO_$_RTPointOfInterestMetricsManager
+ __OBJC_METACLASS_RO_$_RTPointOfInterestSampler
+ ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke.407
+ ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke.409
+ ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke.418
+ ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke_2.408
+ ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke_2.412
+ ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke_3.413
+ ___109-[RTPlaceInferenceManager _savePlaceInferenceQueriesFromInferredMapItems:referenceLocation:options:outError:]_block_invoke
+ ___109-[RTPlaceInferenceManager _savePlaceInferenceQueriesFromInferredMapItems:referenceLocation:options:outError:]_block_invoke.214
+ ___117-[RTAuthorizedLocationManager _assertRecentMotionActivityAndLocationHistoryAreConsistentForAuthorizedLocation:visit:]_block_invoke
+ ___117-[RTAuthorizedLocationManager _assertRecentMotionActivityAndLocationHistoryAreConsistentForAuthorizedLocation:visit:]_block_invoke.308
+ ___119+[RTPlaceDataMetrics calculateMLFeaturesUsingBiomeManager:intervalDictionary:startDate:endDate:createBucketedFeatures:]_block_invoke
+ ___119+[RTPlaceDataMetrics calculateMLFeaturesUsingBiomeManager:intervalDictionary:startDate:endDate:createBucketedFeatures:]_block_invoke.1706
+ ___148-[RTPlaceInferenceManager sendPlaceInferenceMetrics:inferredMapItems:fusedMapItems:fallbackInferredMapItems:finalPlaceInferences:referenceLocation:]_block_invoke.241
+ ___25-[RTDaemonClient restore]_block_invoke.516
+ ___27-[RTLifeCycleManager _exit]_block_invoke.465
+ ___27-[RTLifeCycleManager _exit]_block_invoke.471
+ ___27-[RTLifeCycleManager _exit]_block_invoke.473
+ ___27-[RTLifeCycleManager _exit]_block_invoke.474
+ ___27-[RTLifeCycleManager _exit]_block_invoke_2.472
+ ___28-[RTHealthKitManager _setup]_block_invoke.409
+ ___28-[RTLifeCycleManager _start]_block_invoke.456
+ ___28-[RTLifeCycleManager _start]_block_invoke.462
+ ___35-[RTWiFiManager scheduleActiveScan]_block_invoke
+ ___41-[RTAssetManager _downloadAsset:handler:]_block_invoke.311
+ ___42-[RTPointOfInterestSampler _startSampling]_block_invoke
+ ___42-[RTPointOfInterestSampler _startSampling]_block_invoke.12
+ ___42-[RTPointOfInterestSampler _startSampling]_block_invoke.13
+ ___42-[RTPointOfInterestSampler _startSampling]_block_invoke.16
+ ___42-[RTPointOfInterestSampler _startSampling]_block_invoke.18
+ ___42-[RTPointOfInterestSampler _startSampling]_block_invoke.20
+ ___42-[RTPointOfInterestSampler _startSampling]_block_invoke_2
+ ___42-[RTPointOfInterestSampler _startSampling]_block_invoke_2.17
+ ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.628
+ ___43-[RTEventAgentManager setPluginConnection:]_block_invoke.54
+ ___44-[RTMetricManager registerForXPCActivities:]_block_invoke.87
+ ___45-[RTLocationManager _storeLocations:handler:]_block_invoke.153
+ ___47-[RTClientListener _setupConnection:forClient:]_block_invoke.256
+ ___47-[RTWiFiManager_MobileWiFi _scheduleActiveScan]_block_invoke
+ ___47-[SMClientListener _setupConnection:forClient:]_block_invoke.231
+ ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.537
+ ___51-[RTLearnedLocationEngine _getDailyTrainingMetrics]_block_invoke.621
+ ___51-[RTLearnedLocationEngine _teardownTrainingMetrics]_block_invoke.676
+ ___51-[RTPointOfInterestSampler onWiFiScanNotification:]_block_invoke
+ ___53-[RTAuthorizedLocationManager _setupVisitLogActivity]_block_invoke.279
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.459
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.461
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.463
+ ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke_2.462
+ ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.421
+ ___55-[RTLearnedLocationEngine _retrainVisitsWithoutPlaces:]_block_invoke.678
+ ___55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.526
+ ___55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke_5
+ ___55-[RTLocationManager _removeLocationsPredating:handler:]_block_invoke.208
+ ___55-[RTPointOfInterestMetricsManager shutdownWithHandler:]_block_invoke
+ ___56-[RTMetricManager _registerQueriableMetric:withHandler:]_block_invoke.93
+ ___56-[RTMetricManager _registerQueriableMetric:withHandler:]_block_invoke_2.94
+ ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.589
+ ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.590
+ ___57-[RTPointOfInterestMetricsManager onSettledNotification:]_block_invoke
+ ___58-[RTPointOfInterestMetricsManager _updateLocationDenyList]_block_invoke
+ ___58-[RTPointOfInterestMetricsManager _updateLocationDenyList]_block_invoke.324
+ ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.597
+ ___59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.556
+ ___59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.552
+ ___59-[RTPointOfInterestMetricsManager collectMetricsWithError:]_block_invoke
+ ___59-[RTPointOfInterestMetricsManager collectMetricsWithError:]_block_invoke.354
+ ___59-[RTPointOfInterestMetricsManager collectMetricsWithError:]_block_invoke.360
+ ___59-[RTPointOfInterestMetricsManager onUnsettledNotification:]_block_invoke
+ ___60-[RTPersistenceStoreImporter importEntityRowsAndAttributes:]_block_invoke.60
+ ___60-[RTPersistenceStoreImporter importEntityRowsAndAttributes:]_block_invoke.63
+ ___60-[RTPointOfInterestMetricsManager onNavigationNotification:]_block_invoke
+ ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.172
+ ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.176
+ ___61-[RTLocationManager fetchCurrentLocationWithOptions:handler:]_block_invoke.166
+ ___61-[RTPointOfInterestMetricsManager _onNavigationNotification:]_block_invoke
+ ___61-[RTPointOfInterestMetricsManager _onNavigationNotification:]_block_invoke_2
+ ___62-[RTDaemonClientInternal connection:handleInvocation:isReply:]_block_invoke.440
+ ___62-[RTLocationManager _fetchStoredLocationsWithContext:handler:]_block_invoke.183
+ ___62-[RTPointOfInterestMetricsManager setSamplingPointOfInterest:]_block_invoke
+ ___62-[SMTriggerDestination _updateInitiatorStatusDestinationBound]_block_invoke.198
+ ___63-[RTPlaceInferenceQueryStore storePlaceInferenceQuery:handler:]_block_invoke
+ ___64-[RTAuthorizedLocationManager _fetchCurrentLocationWithHandler:]_block_invoke
+ ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.440
+ ___65-[RTLocationManager locationManager:didDetermineState:forRegion:]_block_invoke.231
+ ___65-[RTPointOfInterestMetricsManager onLeechedLocationNotification:]_block_invoke
+ ___66-[RTStore purgeDateInterval:predicateMappings:purgeLimit:handler:]_block_invoke
+ ___66-[SMInitiatorService _fetchSessionReceiptForSessionID:completion:]_block_invoke.221
+ ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.508
+ ___67-[RTLocationManager _fetchEstimatedLocationAtDate:options:handler:]_block_invoke.194
+ ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke.156
+ ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke.161
+ ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke_2.160
+ ___67-[RTPointOfInterestMetricsManager _shouldCollectQueriesForMapItem:]_block_invoke
+ ___69-[RTAuthorizedLocationManager _curateAuthorizedLocationsWithHandler:]_block_invoke.296
+ ___69-[RTAuthorizedLocationManager _curateAuthorizedLocationsWithHandler:]_block_invoke.305
+ ___69-[RTAuthorizedLocationManager _updateReferenceTimeBoundsFromVisitLog]_block_invoke
+ ___69-[RTPointOfInterestSampler stopSamplingPointOfInterestFromRequester:]_block_invoke
+ ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.529
+ ___70-[RTLearnedLocationEngine _saveIdentifiersOfKnownPlaceTypesWithError:]_block_invoke.608
+ ___70-[RTPointOfInterestMetricsManager onLearnedLocationStoreNotification:]_block_invoke
+ ___71-[RTBiomeManager enumerateEventsWithinDateInterval:streamType:handler:]_block_invoke
+ ___71-[RTBiomeManager enumerateEventsWithinDateInterval:streamType:handler:]_block_invoke.14
+ ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke.663
+ ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke_2.664
+ ___71-[RTPlaceInferenceManager performPurgeOfType:referenceDate:completion:]_block_invoke
+ ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.651
+ ___72-[RTPlaceInferenceManager _performPurgeOfType:referenceDate:completion:]_block_invoke
+ ___73-[SMInitiatorService initializeAndStartSessionWithConfiguration:handler:]_block_invoke
+ ___74-[RTLearnedLocationEngine _relabelWithRelabeler:relabelerPersister:error:]_block_invoke.571
+ ___74-[RTPlaceInferenceQueryStore purgePlaceInferenceQueriesPredating:handler:]_block_invoke
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.201
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.205
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.206
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.209
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.211
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke_2
+ ___74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke_3
+ ___75-[RTLearnedLocationEngine requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.505
+ ___75-[RTPointOfInterestMetricsManager onVisitManagerVisitIncidentNotification:]_block_invoke
+ ___76-[RTAssetManager initWithDefaultsManager:assetProcessor:xpcActivityManager:]_block_invoke.250
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.503
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.504
+ ___76-[RTLearnedLocationEngine _appendVisitsToLocationsOfInterestModelWithError:]_block_invoke.680
+ ___76-[RTLearnedLocationEngine _requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.506
+ ___77-[RTDaemonClientInternal fetchPointOfInterestAttributesWithIdentifier:reply:]_block_invoke
+ ___77-[RTDaemonClientInternal fetchPointOfInterestAttributesWithIdentifier:reply:]_block_invoke_2
+ ___77-[RTDaemonClientInternal fetchPointOfInterestsAroundCoordinate:radius:reply:]_block_invoke
+ ___77-[RTDaemonClientInternal fetchPointOfInterestsAroundCoordinate:radius:reply:]_block_invoke_2
+ ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.533
+ ___79-[RTPointOfInterestMetricsManager processQueries:visitEntryDate:poiIdentifier:]_block_invoke
+ ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.492
+ ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.511
+ ___83+[RTPlaceDataMetrics calculateMLFeatures:startDate:endDate:createBucketedFeatures:]_block_invoke.1689
+ ___83-[RTLearnedLocationEngine _recoverKnownPlaceTypesWithPlaceTypeClassifier:outError:]_block_invoke.619
+ ___84-[RTMapServiceManager fetchPointOfInterestAttributesWithIdentifier:options:handler:]_block_invoke
+ ___84-[RTMapServiceManager fetchPointOfInterestAttributesWithIdentifier:options:handler:]_block_invoke_2
+ ___84-[RTMapServiceManager fetchPointOfInterestsAroundCoordinate:radius:options:handler:]_block_invoke
+ ___84-[RTMapServiceManager fetchPointOfInterestsAroundCoordinate:radius:options:handler:]_block_invoke_2
+ ___85-[RTDaemonClientInternal fetchPlaceInferenceQueriesWithDateInterval:ascending:reply:]_block_invoke
+ ___85-[RTDaemonClientInternal fetchPlaceInferenceQueriesWithDateInterval:ascending:reply:]_block_invoke_2
+ ___87+[RTPlaceInferenceQueryMO managedObjectWithPlaceInferenceQuery:inManagedObjectContext:]_block_invoke
+ ___87+[RTPlaceInferenceQueryMO managedObjectWithPlaceInferenceQuery:inManagedObjectContext:]_block_invoke_2
+ ___87-[RTPointOfInterestSampler startSamplingPointOfInterestFromRequester:samplingInterval:]_block_invoke
+ ___91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.527
+ ___91-[RTPersistenceStoreImporter enumerateRelationshipsInEntityDescription:sourceObject:error:]_block_invoke.73
+ ___91-[RTPersistenceStoreImporter enumerateRelationshipsInEntityDescription:sourceObject:error:]_block_invoke.77
+ ___91-[RTPlaceInferenceQueryStore fetchPlaceInferenceQueriesWithDateInterval:ascending:handler:]_block_invoke
+ ___92-[RTPlaceInferenceQueryStore _fetchPlaceInferenceQueriesWithDateInterval:ascending:handler:]_block_invoke
+ ___92-[RTPlaceInferenceQueryStore _fetchPlaceInferenceQueriesWithDateInterval:ascending:handler:]_block_invoke.10
+ ___94-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]_block_invoke
+ ___94-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]_block_invoke.291
+ ___94-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]_block_invoke.293
+ ___94-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]_block_invoke.294
+ ___97-[RTAuthorizedLocationManager _assertRecentLocationTechnologyQualityForAuthorizedLocation:visit:]_block_invoke
+ ___97-[RTAuthorizedLocationManager _assertRecentLocationTechnologyQualityForAuthorizedLocation:visit:]_block_invoke.309
+ ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.427
+ ___block_descriptor_40_e24_v32?0"NSArray"8Q16^B24l
+ ___block_descriptor_40_e33_v32?0"RTPlaceInference"8Q16^B24l
+ ___block_descriptor_40_e8_32bs_e33_v28?0"NSString"8B16"NSError"20ls32l8
+ ___block_descriptor_40_e8_32r_e29_v24?0"NSArray"8"NSError"16lr32l8
+ ___block_descriptor_48_e8_32s40r_e8_v12?0i8lr40l8s32l8
+ ___block_descriptor_48_e8_32s_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40bs_e49_v24?0"RTPointOfInterestAttributes"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48r_e49_v24?0"RTPointOfInterestAttributes"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e64_v40?0"CKDeviceToDeviceShareInvitationToken"8q16q24"NSError"32ls48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40bs_e32_v16?0"NSManagedObjectContext"8ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e46_v28?0"SMSessionManagerState"8B16"NSError"20ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e17_v16?0"NSError"8ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40bs48r56r64r72r_e32_v16?0"NSManagedObjectContext"8lr48l8r56l8r64l8r72l8s32l8s40l8
+ ___block_descriptor_88_e8_32s40r48r56r64r_e22_v16?0"BMStoreEvent"8ls32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_96_e8_32s40bs48bs56r64r72r80r_e5_v8?0lr56l8r64l8r72l8r80l8s40l8s32l8s48l8
+ ___block_descriptor_96_e8_32s40s48r56r64r72r_e23_v16?0"BPSCompletion"8ls32l8r48l8r56l8r64l8r72l8s40l8
+ ___block_literal_global.1064
+ ___block_literal_global.130
+ ___block_literal_global.143
+ ___block_literal_global.159
+ ___block_literal_global.166
+ ___block_literal_global.214
+ ___block_literal_global.266
+ ___block_literal_global.310
+ ___block_literal_global.320
+ ___block_literal_global.356
+ ___block_literal_global.360
+ ___block_literal_global.368
+ ___block_literal_global.373
+ ___block_literal_global.386
+ ___block_literal_global.442
+ ___block_literal_global.459
+ ___block_literal_global.464
+ ___block_literal_global.467
+ ___block_literal_global.476
+ ___block_literal_global.510
+ ___block_literal_global.513
+ ___block_literal_global.518
+ ___block_literal_global.539
+ ___block_literal_global.540
+ ___block_literal_global.552
+ ___block_literal_global.56
+ ___block_literal_global.614
+ ___block_literal_global.692
+ ___block_literal_global.771
+ ___block_literal_global.851
+ ___block_literal_global.88
+ ___block_literal_global.927
+ __unnamed_array_storage.342
+ __unnamed_array_storage.345
+ __unnamed_array_storage.503
+ __unnamed_array_storage.606
+ _kRTPlaceDataMetrics_DataSource
+ _kRTPointOfInterestMetricKeyAggregatedResult1Match
+ _kRTPointOfInterestMetricKeyAggregatedResult1PoiSize
+ _kRTPointOfInterestMetricKeyAggregatedResult2Match
+ _kRTPointOfInterestMetricKeyAggregatedResult2PoiSize
+ _kRTPointOfInterestMetricKeyApplePaySupport
+ _kRTPointOfInterestMetricKeyComponentResult
+ _kRTPointOfInterestMetricKeyNearbyPoiCountBucketed
+ _kRTPointOfInterestMetricKeyPoiCategory
+ _kRTPointOfInterestMetricKeyPrefixAggregatedResult
+ _kRTPointOfInterestMetricKeyPrefixVisitDwellQuery
+ _kRTPointOfInterestMetricKeyPrefixVisitEntryQuery
+ _kRTPointOfInterestMetricKeyQueryCount
+ _kRTPointOfInterestMetricKeySignalEnvironment
+ _kRTPointOfInterestMetricKeySuffixConfidence
+ _kRTPointOfInterestMetricKeySuffixMatch
+ _kRTPointOfInterestMetricKeySuffixPoiSize
+ _kRTPointOfInterestMetricKeySuffixTimeOffset
+ _kRTPointOfInterestMetricKeyVisitDuration
+ _kSMSuggestionVisitExitTriggerMinDuration
+ _objc_msgSend$Activity
+ _objc_msgSend$DataSourceToString:
+ _objc_msgSend$Device
+ _objc_msgSend$Motion
+ _objc_msgSend$PluggedIn
+ _objc_msgSend$Power
+ _objc_msgSend$ScreenLocked
+ _objc_msgSend$WiFiAvailabilityStatus
+ _objc_msgSend$Wireless
+ _objc_msgSend$_addRequester:samplingInterval:
+ _objc_msgSend$_assertRecentLocationTechnologyQualityForAuthorizedLocation:visit:
+ _objc_msgSend$_assertRecentMotionActivityAndLocationHistoryAreConsistentForAuthorizedLocation:visit:
+ _objc_msgSend$_compareEvent1:event2:streamType:
+ _objc_msgSend$_decodeTimeSourceWithValue:isRetroRegistration:isTrusted:
+ _objc_msgSend$_encodeTimeSourceWithValue:isTrusted:isRetroRegistration:
+ _objc_msgSend$_extractDateIntervalFromBiomeEvent1:event2:streamType:
+ _objc_msgSend$_fetchPlaceInferenceQueriesWithDateInterval:ascending:handler:
+ _objc_msgSend$_initializeAndStartSessionWithConfiguration:handler:
+ _objc_msgSend$_isValidEvent:streamType:
+ _objc_msgSend$_maximumExpirationDateForLearnedPlace:
+ _objc_msgSend$_onLeechedLocationNotification:
+ _objc_msgSend$_purgePlaceInferenceQueriesPredating:handler:
+ _objc_msgSend$_removeRequester:
+ _objc_msgSend$_savePlaceInferenceQueriesFromInferredMapItems:referenceLocation:options:outError:
+ _objc_msgSend$_scheduleActiveScan
+ _objc_msgSend$_shouldCollectQueriesForMapItem:
+ _objc_msgSend$_startSampling
+ _objc_msgSend$_storePlaceInferenceQuery:handler:
+ _objc_msgSend$_updateLocationDenyList
+ _objc_msgSend$_updateReferenceTimeBoundsFromVisitLog
+ _objc_msgSend$_updateSamplingInterval
+ _objc_msgSend$_updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:
+ _objc_msgSend$activeScanRequest
+ _objc_msgSend$ageDaysFirstAnyLoiVisit
+ _objc_msgSend$ageDaysFirstRegisteredVisit
+ _objc_msgSend$ageDaysFirstTopLoiGeoVisit
+ _objc_msgSend$ageDaysFirstTopLoiRegisteredVisit
+ _objc_msgSend$ageDaysFirstTopLoiVisit
+ _objc_msgSend$ageDaysFirstVisit
+ _objc_msgSend$ageDaysRegistry
+ _objc_msgSend$applePaySupport
+ _objc_msgSend$biomeManager
+ _objc_msgSend$biomeStreamTypeToBiomeStream:
+ _objc_msgSend$calculateMLFeaturesUsingBiomeManager:intervalDictionary:startDate:endDate:createBucketedFeatures:
+ _objc_msgSend$convertSMDirectionTransportTypeToMKDirectionTransportType:
+ _objc_msgSend$convertSMDirectionTransportTypeToString:
+ _objc_msgSend$copyConfigurationWithNewSessionID:
+ _objc_msgSend$createWithPlaceInferenceQueryMO:
+ _objc_msgSend$currentSignalEnvironmentType
+ _objc_msgSend$debugDescription
+ _objc_msgSend$enumerateEventsWithinDateInterval:streamType:handler:
+ _objc_msgSend$fetchPlaceInferenceQueriesWithDateInterval:ascending:handler:
+ _objc_msgSend$fetchPointOfInterestAttributesWithIdentifier:options:handler:
+ _objc_msgSend$fetchPointOfInterestsAroundCoordinate:radius:options:handler:
+ _objc_msgSend$fidelityPolicyMask
+ _objc_msgSend$getTruthPointOfInterestIdentifier
+ _objc_msgSend$hasStarting
+ _objc_msgSend$hasStationary
+ _objc_msgSend$initWithAccountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:
+ _objc_msgSend$initWithAccountManager:biomeManager:contactsManager:dailyTrainingSessionCounter:defaultsManager:diagnostics:distanceCalculator:elevationManager:eventManager:fingerprintManager:learnedLocationStore:learnedPlaceTypeInferenceStore:locationManager:locationStore:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:platform:pointOfInterestMetricsManager:portraitManager:reconcilerPerVisit:reconcilerPerDevice:settledStateTransitionStore:transitMetricManager:tripSegmentProvider:visitManager:xpcActivityManager:
+ _objc_msgSend$initWithBatteryManager:defaultsManager:distanceCalculator:learnedLocationStore:locationManager:mapServiceManager:navigationManager:placeInferenceQueryStore:pointOfInterestSampler:scenarioTriggerManager:timerManager:visitManager:
+ _objc_msgSend$initWithBiomeManager:contactsManager:defaultsManager:distanceCalculator:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:placeTypeClassifierMetricsCalculator:platform:queue:visitManager:
+ _objc_msgSend$initWithBiomeManager:defaultsManager:distanceCalculator:learnedLocationStore:placeTypeClassifierMetricsCalculator:platform:
+ _objc_msgSend$initWithDate:messageID:sessionID:invitationTokenDict:sessionType:estimatedEndTime:coarseEstimatedEndTime:destinationType:destinationMapItem:
+ _objc_msgSend$initWithDefaultsManager:locationManager:placeInferenceManager:timerManager:wifiManager:
+ _objc_msgSend$initWithIdentifier:date:fidelityPolicyMask:placeInference:
+ _objc_msgSend$initWithLoi:dwellTime:numberOfDaysVisited:ageDaysFirstVisit:ageDaysFirstRegisteredVisit:
+ _objc_msgSend$initWithQueue:accountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:
+ _objc_msgSend$initWithQueue:authorizationManager:defaultsManager:distanceCalculator:learnedLocationManager:locationManager:mapServiceManager:metricManager:platform:providers:
+ _objc_msgSend$initWithQueue:defaultsManager:distanceCalculator:eventManager:fingerprintManager:inferredMapItemFuser:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:placeInferenceQueryStore:platform:portraitManager:visitStore:
+ _objc_msgSend$initWithStartDate:endDate:maxEvents:lastN:reversed:
+ _objc_msgSend$initializeAndStartSessionWithConfiguration:handler:
+ _objc_msgSend$locationDenyList
+ _objc_msgSend$managedObjectWithPlaceInferenceQuery:inManagedObjectContext:
+ _objc_msgSend$maxCumulativeDwellTimeForNotFamiliarLoiHours
+ _objc_msgSend$maxUniqueVisitDaysForNotFamiliarLois
+ _objc_msgSend$nearbyPoiCount
+ _objc_msgSend$optInApple
+ _objc_msgSend$placeInferenceQueryStore
+ _objc_msgSend$pointOfInterestMetricsManager
+ _objc_msgSend$pointOfInterestSampler
+ _objc_msgSend$processQueries:visitEntryDate:poiIdentifier:
+ _objc_msgSend$publisherWithOptions:
+ _objc_msgSend$purgeDateInterval:predicateMappings:purgeLimit:handler:
+ _objc_msgSend$purgePlaceInferenceQueriesPredating:handler:
+ _objc_msgSend$registrationUsesBestTimeFraction
+ _objc_msgSend$requesters
+ _objc_msgSend$samplingInterval
+ _objc_msgSend$samplingPointOfInterest
+ _objc_msgSend$samplingTimer
+ _objc_msgSend$scheduleActiveScan
+ _objc_msgSend$setAgeDaysFirstAnyLoiVisit:
+ _objc_msgSend$setAgeDaysFirstTopLoiGeoVisit:
+ _objc_msgSend$setAgeDaysFirstTopLoiRegisteredVisit:
+ _objc_msgSend$setAgeDaysFirstTopLoiVisit:
+ _objc_msgSend$setAgeDaysRegistry:
+ _objc_msgSend$setCurationMetrics:
+ _objc_msgSend$setCurrentSignalEnvironmentType:
+ _objc_msgSend$setFidelityPolicyMask:
+ _objc_msgSend$setHistoricalRejectionReasonCode:
+ _objc_msgSend$setHistoricalRejectionSpeedMps:
+ _objc_msgSend$setLocationAgeMinutes:
+ _objc_msgSend$setMLMetricsFromFeaturesDict:sourceName:
+ _objc_msgSend$setMotionSpeedLimitRejectionCodeFromLookbackHours:
+ _objc_msgSend$setRegistrationUsesBestTimeFraction:
+ _objc_msgSend$setRunning:
+ _objc_msgSend$setSamplingInterval:
+ _objc_msgSend$setSamplingPointOfInterest:
+ _objc_msgSend$setSamplingTimer:
+ _objc_msgSend$setShouldRun:
+ _objc_msgSend$setUserType:
+ _objc_msgSend$setUserTypeSource:
+ _objc_msgSend$setVisitRegistrationFraction:
+ _objc_msgSend$shouldRun
+ _objc_msgSend$startSamplingPointOfInterestFromRequester:samplingInterval:
+ _objc_msgSend$starting
+ _objc_msgSend$stopSamplingPointOfInterestFromRequester:
+ _objc_msgSend$storePlaceInferenceQuery:handler:
+ _objc_msgSend$visitRegistrationFraction
+ _objc_msgSend$zelkovaOnWatchEnabled
+ _objc_release_x2
- +[SMTriggerDestination convertMKDirectionTransportTypeToString:]
- -[RTAuthorizedLocation initWithLoi:dwellTime:numberOfDaysVisited:]
- -[RTAuthorizedLocationManager _assertCurrentLocationTechnologyIntegrityForLocation:authorizedLocation:visit:]
- -[RTAuthorizedLocationManager _assertInVisitMotionIsConsistentForCurrentVisit:]
- -[RTAuthorizedLocationManager _assertRecentMotionActivityAndLocationHistoryAreConsistentForLocation:authorizedLocation:visit:]
- -[RTAuthorizedLocationManager _fetchCurrentLocationSinceDate:handler:]
- -[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]
- -[RTAuthorizedLocationQueryMetrics description]
- -[RTAuthorizedLocationQueryMetrics maxCumulativeDwellTimeForNotFamiliarLoiHours]
- -[RTAuthorizedLocationQueryMetrics maxUniqueVisitDaysForNotFamiliarLois]
- -[RTAuthorizedLocationQueryMetrics setMaxCumulativeDwellTimeForNotFamiliarLoiHours:]
- -[RTAuthorizedLocationQueryMetrics setMaxUniqueVisitDaysForNotFamiliarLois:]
- -[RTClientListenerInternal initWithAccountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:motionActivityManager:peopleDiscoveryProvider:persistenceManager:platform:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:]
- -[RTDaemonClientInternal initWithQueue:accountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:motionActivityManager:peopleDiscoveryProvider:persistenceManager:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:]
- -[RTDeviceLocationPredictor initWithQueue:authorizationManager:defaultsManager:distanceCalculator:learnedLocationManager:locationManager:mapServiceManager:metricManager:platfrom:providers:]
- -[RTLearnedLocationEngine initWithAccountManager:contactsManager:dailyTrainingSessionCounter:defaultsManager:diagnostics:distanceCalculator:elevationManager:eventManager:fingerprintManager:learnedLocationStore:learnedPlaceTypeInferenceStore:locationManager:locationStore:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:platform:portraitManager:reconcilerPerVisit:reconcilerPerDevice:settledStateTransitionStore:transitMetricManager:tripSegmentProvider:visitManager:xpcActivityManager:]
- -[RTLearnedPlaceTypeInferenceGenerator initWithDefaultsManager:distanceCalculator:learnedLocationStore:placeTypeClassifierMetricsCalculator:platform:]
- -[RTLocationManager setUserTimeAtLastTrustedTimeUpdate:]
- -[RTLocationManager setUserTimeToTrustedTimeOffset_s:]
- -[RTLocationManager userTimeAtLastTrustedTimeUpdate]
- -[RTLocationManager userTimeToTrustedTimeOffset_s]
- -[RTPlaceDataMetrics setMLMetricsFromFeaturesDict:]
- -[RTPlaceInferenceManager initWithQueue:defaultsManager:distanceCalculator:eventManager:fingerprintManager:inferredMapItemFuser:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:platform:portraitManager:visitStore:]
- -[RTPlaceTypeClassifier initWithContactsManager:defaultsManager:distanceCalculator:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:placeTypeClassifierMetricsCalculator:platform:queue:visitManager:]
- -[RTPlaceTypeClassifierExpertInferred initWithDefaultsManager:distanceCalculator:learnedLocationStore:placeTypeClassifierMetricsCalculator:platform:]
- GCC_except_table137
- GCC_except_table171
- GCC_except_table186
- GCC_except_table197
- GCC_except_table199
- GCC_except_table211
- GCC_except_table214
- GCC_except_table220
- GCC_except_table71
- GCC_except_table84
- _OBJC_IVAR_$_RTAuthorizedLocationQueryMetrics._maxCumulativeDwellTimeForNotFamiliarLoiHours
- _OBJC_IVAR_$_RTAuthorizedLocationQueryMetrics._maxUniqueVisitDaysForNotFamiliarLois
- ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke.406
- ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke.408
- ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke.417
- ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke_2.407
- ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke_2.411
- ___104-[RTEventModelProvider(RTMetricManager) _submitMetricScoreBoardFromStartDate:endDate:submissionHandler:]_block_invoke_3.412
- ___109-[RTAuthorizedLocationManager _assertCurrentLocationTechnologyIntegrityForLocation:authorizedLocation:visit:]_block_invoke
- ___126-[RTAuthorizedLocationManager _assertRecentMotionActivityAndLocationHistoryAreConsistentForLocation:authorizedLocation:visit:]_block_invoke
- ___126-[RTAuthorizedLocationManager _assertRecentMotionActivityAndLocationHistoryAreConsistentForLocation:authorizedLocation:visit:]_block_invoke.209
- ___148-[RTPlaceInferenceManager sendPlaceInferenceMetrics:inferredMapItems:fusedMapItems:fallbackInferredMapItems:finalPlaceInferences:referenceLocation:]_block_invoke.237
- ___25-[RTDaemonClient restore]_block_invoke.492
- ___27-[RTLifeCycleManager _exit]_block_invoke.437
- ___27-[RTLifeCycleManager _exit]_block_invoke.443
- ___27-[RTLifeCycleManager _exit]_block_invoke.445
- ___27-[RTLifeCycleManager _exit]_block_invoke.446
- ___27-[RTLifeCycleManager _exit]_block_invoke_2.444
- ___28-[RTHealthKitManager _setup]_block_invoke.385
- ___28-[RTLifeCycleManager _start]_block_invoke.428
- ___28-[RTLifeCycleManager _start]_block_invoke.434
- ___41-[RTAssetManager _downloadAsset:handler:]_block_invoke.287
- ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.583
- ___43-[RTEventAgentManager setPluginConnection:]_block_invoke.53
- ___44-[RTMetricManager registerForXPCActivities:]_block_invoke.86
- ___45-[RTLocationManager _storeLocations:handler:]_block_invoke.152
- ___47-[RTClientListener _setupConnection:forClient:]_block_invoke.255
- ___47-[SMClientListener _setupConnection:forClient:]_block_invoke.229
- ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.513
- ___51-[RTLearnedLocationEngine _getDailyTrainingMetrics]_block_invoke.618
- ___51-[RTLearnedLocationEngine _teardownTrainingMetrics]_block_invoke.673
- ___53-[RTAuthorizedLocationManager _setupVisitLogActivity]_block_invoke.180
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.435
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.437
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke.439
- ___53-[RTDaemonClient fetchStoredVisitsWithOptions:reply:]_block_invoke_2.438
- ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.397
- ___55-[RTLearnedLocationEngine _retrainVisitsWithoutPlaces:]_block_invoke.675
- ___55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.525
- ___55-[RTLocationManager _removeLocationsPredating:handler:]_block_invoke.207
- ___56-[RTMetricManager _registerQueriableMetric:withHandler:]_block_invoke.92
- ___56-[RTMetricManager _registerQueriableMetric:withHandler:]_block_invoke_2.93
- ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.581
- ___57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.582
- ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.573
- ___59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.555
- ___59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.551
- ___60-[RTPersistenceStoreImporter importEntityRowsAndAttributes:]_block_invoke.59
- ___60-[RTPersistenceStoreImporter importEntityRowsAndAttributes:]_block_invoke.62
- ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.171
- ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.175
- ___61-[RTLocationManager fetchCurrentLocationWithOptions:handler:]_block_invoke.165
- ___62-[RTAuthorizedLocationManager _fetchAuthorizedLocationStatus:]_block_invoke.218
- ___62-[RTDaemonClientInternal connection:handleInvocation:isReply:]_block_invoke.416
- ___62-[RTLocationManager _fetchStoredLocationsWithContext:handler:]_block_invoke.182
- ___62-[SMTriggerDestination _updateInitiatorStatusDestinationBound]_block_invoke.197
- ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.416
- ___65-[RTLocationManager locationManager:didDetermineState:forRegion:]_block_invoke.230
- ___66-[SMInitiatorService _fetchSessionReceiptForSessionID:completion:]_block_invoke.201
- ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.484
- ___67-[RTLocationManager _fetchEstimatedLocationAtDate:options:handler:]_block_invoke.193
- ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke.155
- ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke.160
- ___67-[RTLocationManager locationManager:didUpdateLocations:completion:]_block_invoke_2.159
- ___69-[RTAuthorizedLocationManager _curateAuthorizedLocationsWithHandler:]_block_invoke.198
- ___70-[RTAuthorizedLocationManager _fetchCurrentLocationSinceDate:handler:]_block_invoke
- ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke
- ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke.192
- ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke.193
- ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke.195
- ___70-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]_block_invoke.196
- ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.505
- ___70-[RTLearnedLocationEngine _saveIdentifiersOfKnownPlaceTypesWithError:]_block_invoke.605
- ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke.660
- ___71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke_2.661
- ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.606
- ___74-[RTLearnedLocationEngine _relabelWithRelabeler:relabelerPersister:error:]_block_invoke.563
- ___75-[RTLearnedLocationEngine requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.497
- ___76-[RTAssetManager initWithDefaultsManager:assetProcessor:xpcActivityManager:]_block_invoke.226
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.479
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.480
- ___76-[RTLearnedLocationEngine _appendVisitsToLocationsOfInterestModelWithError:]_block_invoke.677
- ___76-[RTLearnedLocationEngine _requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.498
- ___79-[RTAuthorizedLocationManager _assertInVisitMotionIsConsistentForCurrentVisit:]_block_invoke
- ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.509
- ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.468
- ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.487
- ___83+[RTPlaceDataMetrics calculateMLFeatures:startDate:endDate:createBucketedFeatures:]_block_invoke.1686
- ___83-[RTLearnedLocationEngine _recoverKnownPlaceTypesWithPlaceTypeClassifier:outError:]_block_invoke.616
- ___91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.526
- ___91-[RTPersistenceStoreImporter enumerateRelationshipsInEntityDescription:sourceObject:error:]_block_invoke.72
- ___91-[RTPersistenceStoreImporter enumerateRelationshipsInEntityDescription:sourceObject:error:]_block_invoke.76
- ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.403
- ___block_descriptor_80_e8_32s40bs48bs56r64r_e5_v8?0lr56l8r64l8s40l8s32l8s48l8
- ___block_descriptor_80_e8_32s40bs48r56r64r_e32_v16?0"NSManagedObjectContext"8lr48l8r56l8r64l8s32l8s40l8
- ___block_literal_global.1049
- ___block_literal_global.134
- ___block_literal_global.158
- ___block_literal_global.160
- ___block_literal_global.286
- ___block_literal_global.319
- ___block_literal_global.355
- ___block_literal_global.359
- ___block_literal_global.372
- ___block_literal_global.387
- ___block_literal_global.407
- ___block_literal_global.436
- ___block_literal_global.448
- ___block_literal_global.466
- ___block_literal_global.486
- ___block_literal_global.489
- ___block_literal_global.494
- ___block_literal_global.534
- ___block_literal_global.536
- ___block_literal_global.551
- ___block_literal_global.619
- ___block_literal_global.691
- ___block_literal_global.769
- ___block_literal_global.849
- ___block_literal_global.87
- ___block_literal_global.902
- __unnamed_array_storage.603
- _kCLLocationIntegrityLow
- _objc_msgSend$_assertCurrentLocationTechnologyIntegrityForLocation:authorizedLocation:visit:
- _objc_msgSend$_assertInVisitMotionIsConsistentForCurrentVisit:
- _objc_msgSend$_assertRecentMotionActivityAndLocationHistoryAreConsistentForLocation:authorizedLocation:visit:
- _objc_msgSend$_fetchCurrentLocationSinceDate:handler:
- _objc_msgSend$_updateVisitLogWithTrustedTime:handler:
- _objc_msgSend$convertMKDirectionTransportTypeToString:
- _objc_msgSend$initWithAccountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:motionActivityManager:peopleDiscoveryProvider:persistenceManager:platform:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:
- _objc_msgSend$initWithAccountManager:contactsManager:dailyTrainingSessionCounter:defaultsManager:diagnostics:distanceCalculator:elevationManager:eventManager:fingerprintManager:learnedLocationStore:learnedPlaceTypeInferenceStore:locationManager:locationStore:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:platform:portraitManager:reconcilerPerVisit:reconcilerPerDevice:settledStateTransitionStore:transitMetricManager:tripSegmentProvider:visitManager:xpcActivityManager:
- _objc_msgSend$initWithContactsManager:defaultsManager:distanceCalculator:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:placeTypeClassifierMetricsCalculator:platform:queue:visitManager:
- _objc_msgSend$initWithDefaultsManager:distanceCalculator:learnedLocationStore:placeTypeClassifierMetricsCalculator:platform:
- _objc_msgSend$initWithLoi:dwellTime:numberOfDaysVisited:
- _objc_msgSend$initWithQueue:accountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:motionActivityManager:peopleDiscoveryProvider:persistenceManager:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:
- _objc_msgSend$initWithQueue:authorizationManager:defaultsManager:distanceCalculator:learnedLocationManager:locationManager:mapServiceManager:metricManager:platfrom:providers:
- _objc_msgSend$initWithQueue:defaultsManager:distanceCalculator:eventManager:fingerprintManager:inferredMapItemFuser:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:platform:portraitManager:visitStore:
- _objc_msgSend$purgeDateInterval:predicateMappings:handler:
- _objc_msgSend$setMLMetricsFromFeaturesDict:
- _objc_msgSend$trustedTimestamp
CStrings:
+ "\n\x11\x12\x11"
+ "\x0f\x0f\x01"
+ "\x15\x14"
+ "\x1d\x11"
+ "\x1f\x01"
+ "\x1f\x04"
+ "\x1f\x0f\x03"
+ "%@%lu%@"
+ "%@%lu%@%lu%@"
+ "%@, %@, %lu output date interval, %@"
+ "%@, %@, completion, %@"
+ "%@, %@, error was issued during fetching visits from store, error, %@"
+ "%@, %@, error was issued during metrics submission for RTPlaceDataMetrics, data source, %@, error, %@"
+ "%@, %@, final output date interval, %@"
+ "%@, %@, home map item, %@, work map item, %@"
+ "%@, %@, learned location manager available, %@, isPedometerNotificationsSetupAfterRoutineStarted, %@"
+ "%@, %@, output date interval, %@"
+ "%@, %@, proactive engine not triggered"
+ "%@, %@, received event, %@"
+ "%@, %@, setting mlFeatures for placeStat, %@, mlFeatures, %@, biomeMLFeatures, %@"
+ "%@, %@, start date, %@, end date, %@"
+ "%@, %@, streamType, %@, date interval, %@"
+ "%@, %@, streamType, %@, date interval, %@, outputDateIntervals count, %lu"
+ "%@, %@, submission skipped due to invalid home or work map items"
+ "%@, %@, submitting metrics, data source, %@, distance threshold, %.3f"
+ "%@, %@, visit duration, %f, kSMSuggestionVisitExitTriggerMinDuration, %f"
+ "%@, AOI label, %@, count, %lu, max count, %lu"
+ "%@, Key: %@, Value: %@"
+ "%@, POI label, %@, count, %lu, max count, %lu"
+ "%@, add requester, %@, sampling interval, %.1f"
+ "%@, aggregated AOI label, %lu, count, %lu"
+ "%@, aggregated POI label, %lu, count, %lu"
+ "%@, battery percent, %lu, error, %@"
+ "%@, collecting point of interest metrics"
+ "%@, current location, %@, error, %@"
+ "%@, downgrading leeched location integrity because trusted-time is unavailable, %@, integrity, %{public}d."
+ "%@, downgrading leeched location integrity because user-time to trusted-time offset is too large: %@, %@, integrity, %{public}d."
+ "%@, fetched POI attributes, %@, error, %@"
+ "%@, fetched learned visit, %@, nav session end date, %@, error, %@"
+ "%@, fetched place inference queries, %lu, error, %@"
+ "%@, group idx, %lu, query count, %lu"
+ "%@, group idx, %lu, result idx, %lu, query, %@"
+ "%@, idx, %lu, placeInference, %@"
+ "%@, invalid truth POI identifier, skip metrics collection"
+ "%@, learned store available, %@"
+ "%@, locationDenyList size, %lu"
+ "%@, managedObject, %@, is not supported by RTPlaceInferenceQuery+CoreDataReadable (in %s:%d)"
+ "%@, metric count, %lu, error, %@"
+ "%@, muid, %lu, poi category, %@, applePay support, %@, bucketed nearby point count, %@, signal enviroment, %@"
+ "%@, navigation destination, %@"
+ "%@, optInApple, %@, sampled, %@"
+ "%@, placeInference count, %lu, error, %@"
+ "%@, query count, %lu, visit entry date, %@, poi muid, %lu"
+ "%@, query group count, %lu"
+ "%@, received navigation notification, %@, state, %lu"
+ "%@, received route summary, no op"
+ "%@, received scan result count, %lu, total count, before, %lu, after, %lu"
+ "%@, received visit exit, %@"
+ "%@, registeredForWifiScan, %@"
+ "%@, remove requester, %@"
+ "%@, requester not found, %@"
+ "%@, requester, %@, interval, %@, interval min, %.1f"
+ "%@, run placeInference with options, %@"
+ "%@, sampling timer expiry, timer, %@"
+ "%@, sampling timer start, timer, %@, interval, %.1f"
+ "%@, samplingPointOfInterest transitioned from, %@, to, %@"
+ "%@, samplingTimer expiry"
+ "%@, samplingTimer start"
+ "%@, save placeInferenceQuery, %@, error, %@"
+ "%@, saving BluePOI queries hits error, %@"
+ "%@, settled state transitioned from, %@, to, %@, samplingPointOfInterest, %@"
+ "%@, should collect queries, YES, mapItem, %@"
+ "%@, skip collect queries due to invalid MUID"
+ "%@, skip collect queries due to low battery"
+ "%@, skip collect queries, current location, %@, denied location, %@, distance, %.2f"
+ "%@, skip collect queries, last query collection date, %@, current date, %@"
+ "%@, submit metrics error, %@"
+ "%@, update current signal environment type, %lu"
+ "%@, updated interval, %.1f"
+ "%@, wifi scan timer expiry, timer, %@"
+ "%@, wifi scan timer start, timer, %@, interval, %.1f"
+ "%@,%@, %@, processed location, no integrity downgrade, %@, integrity, %{public}d."
+ "%@,%@, %@, processing location, %@, integrity %{private}d"
+ "%@.samplingTimer"
+ "%@:%@ %{public}d/%{public}d visits registered"
+ "%@:%@ distance, %{public}.3f, matched, %{public}d, threshold %{public}.3f"
+ "%@:%@ failed to fetch current location (%@)."
+ "%@:%@ fetched location: %@, integrity, %{public}d"
+ "%@:%@ rejection 10."
+ "%@:%@ rejection 5."
+ "%@:%@ rejection 6."
+ "%@:%@ rejection 7."
+ "%@:%@ rejection 8."
+ "%@:%@, distance from location, %@, to ALOI location, %@, of %{public}.2f is greater than threshold, %{public}.2f m. Setting state to OUTSIDE."
+ "%@:%@, distance from location, %@, to ALOI, %@, of %{public}.2f is less than threshold, %{public}.2f m. Setting state to INSIDE."
+ "%@:%@, earliest visit to vicinity of LOI: %@."
+ "%@:%@, failed to fetch locations: %@."
+ "%@:%@, found %{public}zu UUIDs in visit log store for interval %@ with %{public}d/%{public}d (%{public}d) sources"
+ "%@:%@, processing %{public}zu locations using INSIDE distance threshold %{public}f m."
+ "%@:%@, processing visit, isRegistered, %{public}d, dwell, %{private}.1f: %@"
+ "%@:%@, rejected by 5,7-12."
+ "%@:%@, threshold for INSIDE authorized location: %{public}f m"
+ "%s, Configuration modified for wrong session, current config sessionID, %@, modified config sessionID, %@"
+ "%s, cancel initialization after start failure with error, %@"
+ "%s, expected monitoring state but got unexpected state, %@, activeDevice, %ld"
+ "%s, expected ready state but got unexpected state, %@, activeDevice, %ld"
+ "%s, fetch error, %@"
+ "%s, missing invitation token with no error"
+ "%s, ready state fetch error, %@"
+ "%s, sent start message with GUID, %@, success, %ld, error, %@"
+ "%s, start error, %@"
+ "+[RTPlaceInferenceQuery(RTCoreDataTransformable) createWithManagedObject:]"
+ "-[RTAuthorizedLocationManager _fetchCurrentLocationWithHandler:]"
+ "-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:]"
+ "-[RTBiomeManager _compareEvent1:event2:streamType:]"
+ "-[RTDeviceLocationPredictor initWithQueue:authorizationManager:defaultsManager:distanceCalculator:learnedLocationManager:locationManager:mapServiceManager:metricManager:platform:providers:]"
+ "-[RTPointOfInterestMetricsManager _onLearnedLocationStoreNotification:]"
+ "-[RTPointOfInterestMetricsManager _onLeechedLocationNotification:]"
+ "-[RTPointOfInterestMetricsManager _onNavigationNotification:]"
+ "-[RTPointOfInterestMetricsManager _onVisitManagerVisitIncidentNotification:]"
+ "-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke"
+ "-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke_3"
+ "/\x0f\x01"
+ "00:53:49"
+ "@\"RTAuthorizedLocationCurationMetrics\""
+ "@\"RTBiomeManager\""
+ "@\"RTPlaceInferenceQueryStore\""
+ "@\"RTPointOfInterestMetricsManager\""
+ "@\"RTPointOfInterestSampler\""
+ "@240@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232"
+ "@248@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240"
+ "@256@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224@232@240@248"
+ "@32@0:8@16B24B28"
+ "@52@0:8@16@24@32@40B48"
+ "@56@0:8@16d24q32q40q48"
+ "Activity"
+ "AgeDaysFirstAnyLoiVisit"
+ "AgeDaysFirstTopLoiGeoVisit"
+ "AgeDaysFirstTopLoiRegisteredVisit"
+ "AgeDaysFirstTopLoiVisit"
+ "AgeDaysRegistry"
+ "B40@0:8@16^B24^B32"
+ "BIOME"
+ "BiomeStream"
+ "CoreDuet"
+ "CoreRoutine.BluePoiMetrics"
+ "Corrupted RTAddressMO, %@"
+ "Corrupted RTMapItemMO, %@"
+ "Corrupted RTVisitMO, %@, was converted to RTVisit, %@"
+ "DataSourceToString:"
+ "Feb 23 2024"
+ "GEOPOICategoryATM"
+ "GEOPOICategoryAirport"
+ "GEOPOICategoryAirportGate"
+ "GEOPOICategoryAirportTerminal"
+ "GEOPOICategoryAmusementPark"
+ "GEOPOICategoryAquarium"
+ "GEOPOICategoryBakery"
+ "GEOPOICategoryBank"
+ "GEOPOICategoryBeach"
+ "GEOPOICategoryBrewery"
+ "GEOPOICategoryCafe"
+ "GEOPOICategoryCampground"
+ "GEOPOICategoryCarRental"
+ "GEOPOICategoryEVCharger"
+ "GEOPOICategoryFireStation"
+ "GEOPOICategoryFitnessCenter"
+ "GEOPOICategoryFoodMarket"
+ "GEOPOICategoryGasStation"
+ "GEOPOICategoryHospital"
+ "GEOPOICategoryHotel"
+ "GEOPOICategoryLaundry"
+ "GEOPOICategoryLibrary"
+ "GEOPOICategoryMarina"
+ "GEOPOICategoryMovieTheater"
+ "GEOPOICategoryMuseum"
+ "GEOPOICategoryNationalPark"
+ "GEOPOICategoryNightlife"
+ "GEOPOICategoryPark"
+ "GEOPOICategoryParking"
+ "GEOPOICategoryPharmacy"
+ "GEOPOICategoryPlayground"
+ "GEOPOICategoryPolice"
+ "GEOPOICategoryPostOffice"
+ "GEOPOICategoryPublicTransport"
+ "GEOPOICategoryReligiousSite"
+ "GEOPOICategoryRestaurant"
+ "GEOPOICategoryRestroom"
+ "GEOPOICategorySchool"
+ "GEOPOICategoryStadium"
+ "GEOPOICategoryStore"
+ "GEOPOICategoryTheater"
+ "GEOPOICategoryUniversity"
+ "GEOPOICategoryWinery"
+ "GEOPOICategoryZoo"
+ "HistoricalRejectionReasonCode"
+ "HistoricalRejectionSpeedMps"
+ "Invalid biome stream type, %lu"
+ "Invalid biome stream type."
+ "Invalid parameter not satisfying: RT_BIOME_STREAM_STREAM_TYPE_VALID(streamType)"
+ "Invalid parameter not satisfying: biomeManager"
+ "Invalid parameter not satisfying: event1"
+ "Invalid parameter not satisfying: event2"
+ "Invalid parameter not satisfying: placeInferenceQuery"
+ "Invalid parameter not satisfying: placeInferenceQueryStore"
+ "Invalid parameter not satisfying: pointOfInterestMetricsManager"
+ "Invalid parameter not satisfying: pointOfInterestSampler"
+ "Invalid parameter not satisfying: samplingInterval > 0"
+ "Invalid parameter not satisfying: timerManger"
+ "LocationAgeMinutes"
+ "Match"
+ "Metric, %@"
+ "Missing invitation token with no error"
+ "Motion"
+ "PluggedIn"
+ "PoiSize"
+ "PointOfInterestMetricsManagerNavSessionEndDate"
+ "PointOfInterestMetricsManagerQueryCollectionDate"
+ "PointOfInterestMetricsManagerSignalEnvironment"
+ "PointOfInterestMetricsManagerTruthLabelIdentifier"
+ "Power"
+ "RTAuthorizedLocation, loi, %@, dwellTime_s, %f, numberOfDaysVisited, %ld, age first visit, %d/%d."
+ "RTAuthorizedLocationCurationMetrics"
+ "RTBiomeManager"
+ "RTBiomeStreamErrorDomain"
+ "RTPlaceInferenceQueryMO"
+ "RTPlaceInferenceQueryStore"
+ "RTPointOfInterestMetricsManager"
+ "RTPointOfInterestSampler"
+ "RegistrationUsesBestTimeFraction"
+ "Result"
+ "SMDirectionsTransportTypeAny"
+ "SMDirectionsTransportTypeAutomobile"
+ "SMDirectionsTransportTypeBicycle"
+ "SMDirectionsTransportTypeTransit"
+ "SMDirectionsTransportTypeWalking"
+ "ScreenLocked"
+ "T@\"<SMTriggerManagerProtocol>\",?,W,N"
+ "T@\"<SMTriggerManagerProtocol>\",?,W,N,VsessionMonitorDelegate"
+ "T@\"NSDate\",&,N,V_lastMetricSubmissionDate"
+ "T@\"NSMutableArray\",R,N,V_locationDenyList"
+ "T@\"NSMutableDictionary\",&,N,V_requesters"
+ "T@\"NSString\",?,R,C"
+ "T@\"RTAuthorizedLocationCurationMetrics\",&,N,V_curationMetrics"
+ "T@\"RTAuthorizedLocationCurationMetrics\",&,V_curationMetrics"
+ "T@\"RTBiomeManager\",&,N,V_biomeManager"
+ "T@\"RTBiomeManager\",R,N,V_biomeManager"
+ "T@\"RTNavigationManager\",R,N,V_navigationManager"
+ "T@\"RTPlaceInferenceQueryStore\",&,N,V_placeInferenceQueryStore"
+ "T@\"RTPlaceInferenceQueryStore\",R,N,V_placeInferenceQueryStore"
+ "T@\"RTPointOfInterestMetricsManager\",R,N,V_pointOfInterestMetricsManager"
+ "T@\"RTPointOfInterestSampler\",&,N,V_pointOfInterestSampler"
+ "T@\"RTPointOfInterestSampler\",R,N,V_pointOfInterestSampler"
+ "T@\"RTTimer\",&,N,V_samplingTimer"
+ "TB,?,N"
+ "TB,N,V_running"
+ "TB,N,V_samplingPointOfInterest"
+ "TB,N,V_shouldRun"
+ "TRUSTED TIME"
+ "Td,N,V_samplingInterval"
+ "Tf,V_historicalRejectionSpeedMps"
+ "Tf,V_registrationUsesBestTimeFraction"
+ "Tf,V_visitRegistrationFraction"
+ "Ti,N,V_currentSignalEnvironmentType"
+ "Ti,V_ageDaysFirstAnyLoiVisit"
+ "Ti,V_ageDaysFirstTopLoiGeoVisit"
+ "Ti,V_ageDaysFirstTopLoiRegisteredVisit"
+ "Ti,V_ageDaysFirstTopLoiVisit"
+ "Ti,V_ageDaysRegistry"
+ "Ti,V_historicalRejectionReasonCode"
+ "Ti,V_locationAgeMinutes"
+ "TimeOffset"
+ "Tq,R,V_ageDaysFirstRegisteredVisit"
+ "Tq,R,V_ageDaysFirstVisit"
+ "Unable to send message"
+ "Unexpected state during initialization"
+ "VisitRegistrationFraction"
+ "WiFiAvailabilityStatus"
+ "Wireless"
+ "_addRequester:samplingInterval:"
+ "_ageDaysFirstAnyLoiVisit"
+ "_ageDaysFirstRegisteredVisit"
+ "_ageDaysFirstTopLoiGeoVisit"
+ "_ageDaysFirstTopLoiRegisteredVisit"
+ "_ageDaysFirstTopLoiVisit"
+ "_ageDaysFirstVisit"
+ "_ageDaysRegistry"
+ "_assertRecentLocationTechnologyQualityForAuthorizedLocation:visit:"
+ "_assertRecentMotionActivityAndLocationHistoryAreConsistentForAuthorizedLocation:visit:"
+ "_biomeManager"
+ "_compareEvent1:event2:streamType:"
+ "_curationMetrics"
+ "_currentSignalEnvironmentType"
+ "_decodeTimeSourceWithValue:isRetroRegistration:isTrusted:"
+ "_encodeTimeSourceWithValue:isTrusted:isRetroRegistration:"
+ "_extractDateIntervalFromBiomeEvent1:event2:streamType:"
+ "_fetchPlaceInferenceQueriesWithDateInterval:ascending:handler:"
+ "_historicalRejectionReasonCode"
+ "_historicalRejectionSpeedMps"
+ "_initializeAndStartSessionWithConfiguration:handler:"
+ "_isValidEvent:streamType:"
+ "_lastMetricSubmissionDate"
+ "_locationAgeMinutes"
+ "_locationDenyList"
+ "_maximumExpirationDateForLearnedPlace:"
+ "_onLeechedLocationNotification:"
+ "_placeInferenceQueryStore"
+ "_pointOfInterestMetricsManager"
+ "_pointOfInterestSampler"
+ "_purgePlaceInferenceQueriesPredating:handler:"
+ "_registrationUsesBestTimeFraction"
+ "_removeRequester:"
+ "_requesters"
+ "_running"
+ "_samplingInterval"
+ "_samplingPointOfInterest"
+ "_samplingTimer"
+ "_savePlaceInferenceQueriesFromInferredMapItems:referenceLocation:options:outError:"
+ "_scheduleActiveScan"
+ "_shouldCollectQueriesForMapItem:"
+ "_shouldRun"
+ "_startSampling"
+ "_storePlaceInferenceQuery:handler:"
+ "_updateLocationDenyList"
+ "_updateReferenceTimeBoundsFromVisitLog"
+ "_updateSamplingInterval"
+ "_updateVisitLogWithTrustedTime:isRetroRegistrationTime:handler:"
+ "_visitRegistrationFraction"
+ "activeScanRequest"
+ "ageDaysFirstAnyLoiVisit"
+ "ageDaysFirstRegisteredVisit"
+ "ageDaysFirstTopLoiGeoVisit"
+ "ageDaysFirstTopLoiRegisteredVisit"
+ "ageDaysFirstTopLoiVisit"
+ "ageDaysFirstVisit"
+ "ageDaysRegistry"
+ "aggregatedResult"
+ "aggregatedResult1Match"
+ "aggregatedResult1PoiSize"
+ "aggregatedResult2Match"
+ "aggregatedResult2PoiSize"
+ "applePaySupport"
+ "biomeManager"
+ "biomeStreamTypeToBiomeStream:"
+ "c"
+ "calculateMLFeaturesUsingBiomeManager:intervalDictionary:startDate:endDate:createBucketedFeatures:"
+ "com.apple.CoreRoutine.PoiMetrics"
+ "com.apple.CoreRoutine.poisampler"
+ "com.apple.routined.poisampler.sampling.timer"
+ "com.apple.routined.poisampler.wifiscan.timer"
+ "confidence, %@, dataPointCount, %@, detectionDate, %@, entryDate, %@, exitDate, %@, locationLatitude, %@, locationLongitude, %@, locationUncertainty, %@, locationReferenceFrame, %@, locationDate, %@, placeInferenceConfidence, %@, placeInferenceMapItemIdentifier, %@, placeInferencePlaceType, %@, placeInferenceUserType, %@, placeInferenceUserTypeSource, %@, source, %@, type, %@"
+ "convertSMDirectionTransportTypeToMKDirectionTransportType:"
+ "convertSMDirectionTransportTypeToString:"
+ "copyConfigurationWithNewSessionID:"
+ "createWithPlaceInferenceQueryMO:"
+ "curationMetrics"
+ "currentSignalEnvironmentType"
+ "data_source"
+ "enumerateEventsWithinDateInterval:streamType:handler:"
+ "fetchPlaceInferenceQueriesWithDateInterval:ascending:handler:"
+ "fetchPlaceInferenceQueriesWithDateInterval:ascending:reply:"
+ "fetchPointOfInterestAttributesWithIdentifier:options:handler:"
+ "fetchPointOfInterestAttributesWithIdentifier:reply:"
+ "fetchPointOfInterestsAroundCoordinate:radius:options:handler:"
+ "fetchPointOfInterestsAroundCoordinate:radius:reply:"
+ "fetched visit, %@, has a placeInference, %@ but not a map item this should not happen"
+ "fidelityPolicyMask"
+ "getTruthPointOfInterestIdentifier"
+ "hasStarting"
+ "hasStationary"
+ "historicalRejectionReasonCode"
+ "historicalRejectionSpeedMps"
+ "identifier, %@, geoAddressData.length, %lu, subPremises, %@, subThoroughfare, %@, thoroughfare, %@, subLocality, %@, locality, %@, subAdministrativeArea, %@, administrativeArea, %@, administrativeAreaCode, %@, postalCode, %@, country, %@, countryCode, %@, inlandWater, %@, ocean, %@, areasOfInterest.count, %lu, island, %@, creationDate, %@, expirationDate, %@, iso3166CountryCode, %@, iso3166SubdivisionCode, %@"
+ "identifier, %@, name, %@, category, %@, latitude, %@, longitude, %@, uncertainty, %@, referenceFrame, %@, mapItemSource, %@, mapItemPlaceType, %@, muid, %@, resultProviderID, %@, geoMapItemHandle, %@, creationDate, %@, expirationDate, %@, displayLanguage, %@, disputed, %b, address, %@, extendedAttributesIdentifier, %@"
+ "initWithAccountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:platform:pointOfInterestSampler:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:"
+ "initWithAccountManager:biomeManager:contactsManager:dailyTrainingSessionCounter:defaultsManager:diagnostics:distanceCalculator:elevationManager:eventManager:fingerprintManager:learnedLocationStore:learnedPlaceTypeInferenceStore:locationManager:locationStore:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:platform:pointOfInterestMetricsManager:portraitManager:reconcilerPerVisit:reconcilerPerDevice:settledStateTransitionStore:transitMetricManager:tripSegmentProvider:visitManager:xpcActivityManager:"
+ "initWithBatteryManager:defaultsManager:distanceCalculator:learnedLocationStore:locationManager:mapServiceManager:navigationManager:placeInferenceQueryStore:pointOfInterestSampler:scenarioTriggerManager:timerManager:visitManager:"
+ "initWithBiomeManager:contactsManager:defaultsManager:distanceCalculator:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:placeTypeClassifierMetricsCalculator:platform:queue:visitManager:"
+ "initWithBiomeManager:defaultsManager:distanceCalculator:learnedLocationStore:placeTypeClassifierMetricsCalculator:platform:"
+ "initWithDate:messageID:sessionID:invitationTokenDict:sessionType:estimatedEndTime:coarseEstimatedEndTime:destinationType:destinationMapItem:"
+ "initWithDefaultsManager:locationManager:placeInferenceManager:timerManager:wifiManager:"
+ "initWithIdentifier:date:fidelityPolicyMask:placeInference:"
+ "initWithLoi:dwellTime:numberOfDaysVisited:ageDaysFirstVisit:ageDaysFirstRegisteredVisit:"
+ "initWithQueue:accountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:mapServiceManager:motionActivityManager:peopleDiscoveryProvider:persistenceManager:placeInferenceQueryStore:pointOfInterestSampler:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:"
+ "initWithQueue:authorizationManager:defaultsManager:distanceCalculator:learnedLocationManager:locationManager:mapServiceManager:metricManager:platform:providers:"
+ "initWithQueue:defaultsManager:distanceCalculator:eventManager:fingerprintManager:inferredMapItemFuser:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:placeInferenceQueryStore:platform:portraitManager:visitStore:"
+ "initWithStartDate:endDate:maxEvents:lastN:reversed:"
+ "initializeAndStartSessionWithConfiguration:handler:"
+ "lastMetricSubmissionDate"
+ "locationAgeMinutes"
+ "locationDenyList"
+ "managedObjectWithPlaceInferenceQuery:inManagedObjectContext:"
+ "nearbyPoiCount"
+ "nearbyPoiCountBucketed"
+ "nil handle"
+ "nil message"
+ "optInApple"
+ "placeInferenceQueryStartDate cannot be after placeInferenceQueryEndDate"
+ "placeInferenceQueryStore"
+ "pointOfInterestMetricsManager"
+ "pointOfInterestSampler"
+ "processQueries:visitEntryDate:poiIdentifier:"
+ "publisherWithOptions:"
+ "purgeDateInterval:predicateMappings:purgeLimit:handler:"
+ "purgePlaceInferenceQueriesPredating:handler:"
+ "q40@0:8@16@24q32"
+ "registrationUsesBestTimeFraction"
+ "requesters"
+ "samplingInterval"
+ "samplingPointOfInterest"
+ "samplingTimer"
+ "scheduleActiveScan"
+ "setAgeDaysFirstAnyLoiVisit:"
+ "setAgeDaysFirstTopLoiGeoVisit:"
+ "setAgeDaysFirstTopLoiRegisteredVisit:"
+ "setAgeDaysFirstTopLoiVisit:"
+ "setAgeDaysRegistry:"
+ "setBiomeManager:"
+ "setCurationMetrics:"
+ "setCurrentSignalEnvironmentType:"
+ "setFidelityPolicyMask:"
+ "setHistoricalRejectionReasonCode:"
+ "setHistoricalRejectionSpeedMps:"
+ "setLastMetricSubmissionDate:"
+ "setLocationAgeMinutes:"
+ "setMLMetricsFromFeaturesDict:sourceName:"
+ "setMotionSpeedLimitRejectionCodeFromLookbackHours:"
+ "setPlaceInferenceQueryStore:"
+ "setPointOfInterestSampler:"
+ "setRegistrationUsesBestTimeFraction:"
+ "setRequesters:"
+ "setRunning:"
+ "setSamplingInterval:"
+ "setSamplingPointOfInterest:"
+ "setSamplingTimer:"
+ "setShouldRun:"
+ "setUserType:"
+ "setUserTypeSource:"
+ "setVisitRegistrationFraction:"
+ "shouldRun"
+ "startSamplingPointOfInterestFromRequester:samplingInterval:"
+ "startSamplingPointOfInterestWithInterval:handler:"
+ "starting"
+ "stopSamplingPointOfInterest:"
+ "stopSamplingPointOfInterestFromRequester:"
+ "storePlaceInferenceQuery:handler:"
+ "v24@?0@\"RTPointOfInterestAttributes\"8@\"NSError\"16"
+ "v32@0:8Q16@?<v@?@\"RTPointOfInterestAttributes\"@\"NSError\">24"
+ "v32@0:8d16@?24"
+ "v32@0:8d16@?<v@?@\"NSError\">24"
+ "v32@?0@\"RTPlaceInference\"8Q16^B24"
+ "v36@0:8@\"NSDateInterval\"16B24@?<v@?@\"NSArray\"@\"NSError\">28"
+ "v40@0:8@\"RTCoordinate\"16d24@?<v@?@\"NSArray\"@\"NSError\">32"
+ "v40@0:8Q16@\"RTMapServiceOptions\"24@?<v@?@\"RTPointOfInterestAttributes\"@\"NSError\">32"
+ "v40@?0@\"CKDeviceToDeviceShareInvitationToken\"8q16q24@\"NSError\"32"
+ "v48@0:8@\"RTCoordinate\"16d24@\"RTMapServiceOptions\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@16d24@32@?40"
+ "visitDwellQuery"
+ "visitEntryQuery"
+ "visitRegistrationFraction"
+ "zelkovaOnWatchEnabled"
- "\n\x11\x12"
- "\x0f\r"
- "\x14\x1f"
- "\x1f\x0f"
- "%@, %@, learned location manager available, %@, isPedometerNotificationsSetupAfterRoutineStartedm, %@"
- "%@, %@, setting mlFeatures for placeStat, %@"
- "%@, %@, skipped, distance, %@, min threshold, %.3f, max threshold, %.3f"
- "%@, downgrading leeched location integrity because trusted-time is unavailable."
- "%@, downgrading leeched location integrity because user-time to trusted-time offset is too large: %@, %@."
- "%@:%@ distance, %{public}.3f, matched, %{public}d, threshold %{public}.3f, type, %{public}d, unc, %{public}.1f, age, %{public}.1f"
- "%@:%@ fetched location: %@"
- "%@:%@ rejection 5 (%@)."
- "%@:%@, detected vehicular motion of %{private}f seconds (threshold %{private}f seconds) in visit."
- "%@:%@, found %zu UUIDs in visit log store for interval %@"
- "%@:%@, no anomalous vehicular motion detected in visit."
- "%@:%@, no motion activity, assuming consistency."
- "%@:%@, processing visit %@."
- "%@:%@, processing visit, UUID was found in visit log: %@"
- "%@:%@, rejected by 7-12."
- "%@:%@, rejection 10."
- "%@:%@, rejection 13."
- "%@:%@, rejection 7."
- "%@:%@, rejection 8 (%{private}ld)."
- "%@:%@, skipping visit, UUID was not found in visit log: %@"
- "%s, Configuartion modified for wrong session, current config sessionID, %@, modified config sessionID, %@"
- "-[RTAuthorizedLocationManager _fetchCurrentLocationSinceDate:handler:]"
- "-[RTAuthorizedLocationManager _updateVisitLogWithTrustedTime:handler:]"
- "-[RTDeviceLocationPredictor initWithQueue:authorizationManager:defaultsManager:distanceCalculator:learnedLocationManager:locationManager:mapServiceManager:metricManager:platfrom:providers:]"
- "/\x0e"
- "20:13:30"
- "@224@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216"
- "@232@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208@216@224"
- "Error was issued during metrics submission for RTPlaceDataMetrics. Error: %@"
- "Invalid parameter not satisfying: RTMapItemSourceValid(source)"
- "Jan  5 2024"
- "MKDirectionsTransportTypeAny"
- "MKDirectionsTransportTypeAutomobile"
- "MKDirectionsTransportTypeBicycle"
- "MKDirectionsTransportTypeTransit"
- "MKDirectionsTransportTypeWalking"
- "MOAngelEnabled"
- "Moments"
- "RTAuthorizedLocation, loi, %@, dwellTime_s, %f, numberOfDaysVisited, %ld."
- "RTAuthorizedLocationManager,%@:%@, %@"
- "T@\"<SMTriggerManagerProtocol>\",W,N"
- "T@\"<SMTriggerManagerProtocol>\",W,N,VsessionMonitorDelegate"
- "T@\"NSDate\",&,N,V_userTimeAtLastTrustedTimeUpdate"
- "TB,N"
- "Td,V_userTimeToTrustedTimeOffset_s"
- "_assertCurrentLocationTechnologyIntegrityForLocation:authorizedLocation:visit:"
- "_assertInVisitMotionIsConsistentForCurrentVisit:"
- "_assertRecentMotionActivityAndLocationHistoryAreConsistentForLocation:authorizedLocation:visit:"
- "_fetchCurrentLocationSinceDate:handler:"
- "_updateVisitLogWithTrustedTime:handler:"
- "_userTimeAtLastTrustedTimeUpdate"
- "_userTimeToTrustedTimeOffset_s"
- "b"
- "convertMKDirectionTransportTypeToString:"
- "daemonResponseLatencyMs, %f, loiFamiliarityRank, %d, maxCumulativeDwellTimeForNotFamiliarLoiHours, %f, maxUniqueVisitDaysForNotFamiliarLois, %d, normalizedDistanceToCentroid, %f, numFamiliarLois, %d, rejectionReasonCode, %d, responseValue, %d, technologyAvailability, %d, roundedUserTimeOffsetHours, %f, visitDwellMinutes, %f."
- "initWithAccountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventAgentManager:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:motionActivityManager:peopleDiscoveryProvider:persistenceManager:platform:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:"
- "initWithAccountManager:contactsManager:dailyTrainingSessionCounter:defaultsManager:diagnostics:distanceCalculator:elevationManager:eventManager:fingerprintManager:learnedLocationStore:learnedPlaceTypeInferenceStore:locationManager:locationStore:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:platform:portraitManager:reconcilerPerVisit:reconcilerPerDevice:settledStateTransitionStore:transitMetricManager:tripSegmentProvider:visitManager:xpcActivityManager:"
- "initWithContactsManager:defaultsManager:distanceCalculator:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:placeTypeClassifierMetricsCalculator:platform:queue:visitManager:"
- "initWithDefaultsManager:distanceCalculator:learnedLocationStore:placeTypeClassifierMetricsCalculator:platform:"
- "initWithLoi:dwellTime:numberOfDaysVisited:"
- "initWithQueue:accountManager:assetManager:authorizationManager:buildingPolygonManager:deviceLocationPredictor:diagnostics:eventModelProvider:authorizedLocationManager:fingerprintManager:hintManager:intermittentGNSSManager:learnedLocationManager:learnedLocationStore:locationManager:locationStore:motionActivityManager:peopleDiscoveryProvider:persistenceManager:purgeManager:safetyCacheStore:scenarioTriggerManager:vehicleLocationProvider:visitManager:workoutRouteManager:workoutScheduler:"
- "initWithQueue:authorizationManager:defaultsManager:distanceCalculator:learnedLocationManager:locationManager:mapServiceManager:metricManager:platfrom:providers:"
- "initWithQueue:defaultsManager:distanceCalculator:eventManager:fingerprintManager:inferredMapItemFuser:learnedLocationStore:locationManager:mapServiceManager:mapsSupportManager:metricManager:motionActivityManager:platform:portraitManager:visitStore:"
- "setMLMetricsFromFeaturesDict:"
- "setUserTimeAtLastTrustedTimeUpdate:"
- "setUserTimeToTrustedTimeOffset_s:"
- "trustedTimestamp"
- "userTimeAtLastTrustedTimeUpdate"
- "userTimeToTrustedTimeOffset_s"

```
