## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-986.0.1.0.0
-  __TEXT.__text: 0x4d46b0
-  __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_methlist: 0x238c4
-  __TEXT.__const: 0x17c0
-  __TEXT.__cstring: 0x35c88
-  __TEXT.__oslogstring: 0x53206
-  __TEXT.__swift5_typeref: 0xd
-  __TEXT.__gcc_except_tab: 0x1a7f8
+990.0.10.0.0
+  __TEXT.__text: 0x4cfa1c
+  __TEXT.__auth_stubs: 0x1660
+  __TEXT.__objc_methlist: 0x2628c
+  __TEXT.__const: 0x17e0
   __TEXT.__dlopen_cstrs: 0xb2
+  __TEXT.__cstring: 0x3577b
+  __TEXT.__oslogstring: 0x54076
+  __TEXT.__swift5_typeref: 0xd
+  __TEXT.__gcc_except_tab: 0x1a42c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xaa10
+  __TEXT.__unwind_info: 0xa8d8
   __TEXT.__eh_frame: 0x60
-  __TEXT.__objc_classname: 0x478b
-  __TEXT.__objc_methname: 0x6d9df
-  __TEXT.__objc_methtype: 0xa74e
-  __TEXT.__objc_stubs: 0x3f860
-  __DATA_CONST.__got: 0x2508
-  __DATA_CONST.__const: 0x2738
-  __DATA_CONST.__objc_classlist: 0x1128
+  __TEXT.__objc_classname: 0x47a3
+  __TEXT.__objc_methname: 0x6d7c6
+  __TEXT.__objc_methtype: 0xa6f1
+  __TEXT.__objc_stubs: 0x3f780
+  __DATA_CONST.__got: 0x2510
+  __DATA_CONST.__const: 0x28a8
+  __DATA_CONST.__objc_classlist: 0x1120
   __DATA_CONST.__objc_catlist: 0x2c8
   __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12980
-  __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0xe50
-  __DATA_CONST.__objc_arraydata: 0x2610
-  __AUTH_CONST.__auth_got: 0xb78
-  __AUTH_CONST.__const: 0xc090
-  __AUTH_CONST.__cfstring: 0x1e180
-  __AUTH_CONST.__objc_const: 0x44a48
-  __AUTH_CONST.__objc_intobj: 0x31e0
-  __AUTH_CONST.__objc_arrayobj: 0xbd0
-  __AUTH_CONST.__objc_doubleobj: 0x990
+  __DATA_CONST.__objc_selrefs: 0x132b0
+  __DATA_CONST.__objc_protorefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0xe48
+  __DATA_CONST.__objc_arraydata: 0x2620
+  __AUTH_CONST.__auth_got: 0xb40
+  __AUTH_CONST.__const: 0xbf50
+  __AUTH_CONST.__cfstring: 0x1e1a0
+  __AUTH_CONST.__objc_const: 0x3fcd8
+  __AUTH_CONST.__objc_intobj: 0x31b0
+  __AUTH_CONST.__objc_arrayobj: 0xbb8
+  __AUTH_CONST.__objc_doubleobj: 0x950
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x6d60
-  __DATA.__objc_ivar: 0x2ad8
-  __DATA.__data: 0x27f0
-  __DATA.__bss: 0x158
+  __AUTH.__objc_data: 0x6d10
+  __DATA.__objc_ivar: 0x2ad4
+  __DATA.__data: 0x27d0
+  __DATA.__bss: 0x138
   __DATA_DIRTY.__objc_data: 0x3e30
   __DATA_DIRTY.__data: 0x240
   __DATA_DIRTY.__bss: 0x38

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: EB128E7D-595E-38E5-9631-9F1ABD5DDF53
-  Functions: 15691
-  Symbols:   34467
-  CStrings:  30347
+  UUID: D07329F5-C100-3C3D-8C94-8B337E0978A4
+  Functions: 15627
+  Symbols:   34435
+  CStrings:  30325
 
Symbols:
+ +[NSFileManager(RTExtensions) routineBluePOIQueryPath]
+ +[RTBluePOIQuery supportsSecureCoding]
+ +[RTPlaceTypeClassifierMetricsCalculator allPlaceTypes]
+ +[RTPlaceTypeClassifierMetricsCalculator inferredPlaceTypes]
+ +[RTPlaceTypeClassifierMetricsCalculator nonInferredPlaceTypes]
+ +[RTPlaceTypeClassifierMetricsCalculator schoolGymEligibleSources]
+ +[RTVisit(RTExtensions) stringFromVisitSource:]
+ -[RTBluePOIQuery .cxx_destruct]
+ -[RTBluePOIQuery accessPoints]
+ -[RTBluePOIQuery copyWithZone:]
+ -[RTBluePOIQuery date]
+ -[RTBluePOIQuery description]
+ -[RTBluePOIQuery encodeWithCoder:]
+ -[RTBluePOIQuery getCLLocations]
+ -[RTBluePOIQuery hash]
+ -[RTBluePOIQuery identifier]
+ -[RTBluePOIQuery initWithCoder:]
+ -[RTBluePOIQuery initWithDictionary:]
+ -[RTBluePOIQuery initWithFirstJSONDictionary:]
+ -[RTBluePOIQuery initWithIdentifier:accessPoints:locations:referenceLocation:settledState:selectedToLabel:date:]
+ -[RTBluePOIQuery init]
+ -[RTBluePOIQuery isEqual:]
+ -[RTBluePOIQuery locations]
+ -[RTBluePOIQuery outputToDictionary]
+ -[RTBluePOIQuery outputToFirstJSONDictionary]
+ -[RTBluePOIQuery referenceLocation]
+ -[RTBluePOIQuery selectedToLabel]
+ -[RTBluePOIQuery settledState]
+ -[RTDaemonClient fetchFinerGranularityInferredMapItemWithVisitIdentifier:reply:]
+ -[RTDaemonClientInternal injectVisit:finerGranularityInferredMapItem:locationOfInterest:reply:]
+ -[RTLearnedLocationEngine _extractBluePOIQueriesJSONDObjectBetweenStartDate:endDate:error:]
+ -[RTLearnedLocationEngine _extractBluePOIQueriesJSONDObjectForVisit:bluePOIMapItemProvider:]
+ -[RTLearnedLocationEngine _fetchCloudCurrentDeviceVisitsBetweenStartDate:endDate:ascending:error:]
+ -[RTLearnedLocationEngine _generateDiagnosticFilesAtURL:error:]
+ -[RTLearnedLocationEngine _refreshMapItemsForLocationsOfInterestWithError:]
+ -[RTLearnedLocationEngine dataWithBluePOIQueriesBetweenStartDate:endDate:error:]
+ -[RTLearnedLocationEngine sendDiagnosticsToURL:options:handler:]
+ -[RTLearnedLocationManager _addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:]
+ -[RTLearnedLocationManager _fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]
+ -[RTLearnedLocationManager addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:]
+ -[RTLearnedLocationManager fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]
+ -[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]
+ -[RTLearnedLocationStore _fetchMapItemWithMuid:predicate:handler:]
+ -[RTLearnedLocationStore fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]
+ -[RTLearnedLocationStore fetchMapItemWithMuid:predicate:handler:]
+ -[RTMapItemProviderBluePOI _bluePOIQueryFromFingerprint:fingerprintIdx:referenceLocationArray:selected:endDate:totalAPsCount:error:]
+ -[RTMapItemProviderBluePOI _fetchAllFingerprintsBetweenStartDate:endDate:error:]
+ -[RTMapItemProviderBluePOI _mapItemsFromBluePOIQuery:startDate:endDate:error:]
+ -[RTMapItemProviderBluePOI _selectFingerprintsStartDate:endDate:maxQueryAttemps:isTimeWindowFallback:fingerprintsTotalOut:fingerprintsNonZeroAPsTotalOut:error:]
+ -[RTMapItemProviderBluePOI getAllBluePOIQuerriesForStartDate:endDate:location:error:]
+ -[RTMapsSupportManager classForMapsSyncClassName:]
+ -[RTMapsSupportManager classNameForMapsSyncClass:]
+ -[RTMapsSupportManager classNamesForMapsSyncClasses:]
+ -[RTMapsSupportManager queryTypeForMapsSyncClass:]
+ -[RTMapsSupportManager queryTypeForMapsSyncClassName:]
+ -[RTMapsSupportManager setStoreSubscriptionTypes:]
+ -[RTMapsSupportManager storeChangeNotificationClasses]
+ -[RTMapsSupportManager storeDidChangeWithTypes:]
+ -[RTMapsSupportManager storeSubscriptionTypes]
+ -[RTMapsSupportManager stringForQueryType:]
+ -[RTPinnedPlace copyWithZone:]
+ -[RTPinnedPlace hash]
+ -[RTPinnedPlace isEqual:]
+ -[RTPlaceTypeClassifier _convertToIdToLearnedPlace:]
+ -[RTPlaceTypeClassifier _getClosestLearnedPlacesAtDestination:source:threshold:error:]
+ -[RTPlaceTypeClassifier _logExpertClassifications:sourceNames:]
+ -[RTPlaceTypeClassifier coalescePlacesFromSourcesOfTruth:sourceOfTruthNames:]
+ -[RTPlaceTypeClassifierExpertFallback initWithDistanceCalculator:learnedLocationStore:locationManager:mapServiceManager:visitManager:placeTypeClassifierMetricsCalculator:]
+ -[RTPlaceTypeClassifierExpertFallback placeTypeClassifierMetricsCalculator]
+ -[RTPlaceTypeClassifierExpertFallback setPlaceTypeClassifierMetricsCalculator:]
+ -[RTPlaceTypeClassifierExpertMaps .cxx_destruct]
+ -[RTPlaceTypeClassifierExpertMaps _convertPinnedPlacesToLearnedPlaces:error:]
+ -[RTPlaceTypeClassifierExpertMaps _fetchPinnedPlacesWithKnownPlacesTypesAndError:]
+ -[RTPlaceTypeClassifierExpertMaps classifyWithError:]
+ -[RTPlaceTypeClassifierExpertMaps initWithLearnedLocationStore:mapsSupportManager:placeTypeClassifierMetricsCalculator:]
+ -[RTPlaceTypeClassifierExpertMaps init]
+ -[RTPlaceTypeClassifierExpertMaps learnedLocationStore]
+ -[RTPlaceTypeClassifierExpertMaps mapsSupportManager]
+ -[RTPlaceTypeClassifierExpertMaps placeTypeClassifierMetricsCalculator]
+ -[RTPlaceTypeClassifierExpertMaps setLearnedLocationStore:]
+ -[RTPlaceTypeClassifierExpertMaps setMapsSupportManager:]
+ -[RTPlaceTypeClassifierExpertMaps setPlaceTypeClassifierMetricsCalculator:]
+ -[RTPlaceTypeClassifierModelMultiClass predictionFromFeatures:completionHandler:]
+ -[RTPlaceTypeClassifierModelMultiClass predictionFromFeatures:options:completionHandler:]
+ -[RTPlaceTypeClassifierModelRanker predictionFromFeatures:completionHandler:]
+ -[RTPlaceTypeClassifierModelRanker predictionFromFeatures:options:completionHandler:]
+ -[RTVisit(RTExtensions) dictionaryOutForBluePOIReplayWithBluePOIQueries:]
+ -[RTVisit(RTExtensions) initWithLearnedVisit:inferredMapItem:finerGranularityInferredMapItem:userPlaceType:userPlaceTypeSource:loiIdentifier:]
+ -[RTWiFiManager _notifyLeechScanResults:]
+ -[RTWiFiManagerNotificationLeechScanResults .cxx_destruct]
+ -[RTWiFiManagerNotificationLeechScanResults initWithScanResults:]
+ -[RTWiFiManagerNotificationLeechScanResults scanResults]
+ GCC_except_table107
+ GCC_except_table120
+ GCC_except_table133
+ GCC_except_table140
+ GCC_except_table148
+ GCC_except_table151
+ GCC_except_table169
+ GCC_except_table187
+ GCC_except_table190
+ GCC_except_table198
+ GCC_except_table199
+ GCC_except_table216
+ GCC_except_table218
+ GCC_except_table223
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table237
+ GCC_except_table239
+ GCC_except_table250
+ GCC_except_table262
+ GCC_except_table270
+ GCC_except_table279
+ GCC_except_table286
+ GCC_except_table292
+ GCC_except_table295
+ GCC_except_table318
+ GCC_except_table396
+ GCC_except_table404
+ GCC_except_table42
+ GCC_except_table85
+ GCC_except_table94
+ GCC_except_table99
+ OBJC_IVAR_$_RTBluePOIQuery._accessPoints
+ OBJC_IVAR_$_RTBluePOIQuery._date
+ OBJC_IVAR_$_RTBluePOIQuery._identifier
+ OBJC_IVAR_$_RTBluePOIQuery._locations
+ OBJC_IVAR_$_RTBluePOIQuery._referenceLocation
+ OBJC_IVAR_$_RTBluePOIQuery._selectedToLabel
+ OBJC_IVAR_$_RTBluePOIQuery._settledState
+ OBJC_IVAR_$_RTPlaceTypeClassifierExpertFallback._placeTypeClassifierMetricsCalculator
+ OBJC_IVAR_$_RTPlaceTypeClassifierExpertMaps._learnedLocationStore
+ OBJC_IVAR_$_RTPlaceTypeClassifierExpertMaps._mapsSupportManager
+ OBJC_IVAR_$_RTPlaceTypeClassifierExpertMaps._placeTypeClassifierMetricsCalculator
+ OBJC_IVAR_$_RTWiFiManagerNotificationLeechScanResults._scanResults
+ _OBJC_CLASS_$_MSCollectionPlaceItem
+ _OBJC_CLASS_$_MSFavoriteItem
+ _OBJC_CLASS_$_MSHistoryItem
+ _OBJC_CLASS_$_RTBluePOIQuery
+ _OBJC_CLASS_$_RTPlaceTypeClassifierExpertMaps
+ _OBJC_CLASS_$_RTWiFiManagerNotificationLeechScanResults
+ _OBJC_CLASS_$__TtC8MapsSync13MapsSyncStore
+ _OBJC_METACLASS_$_RTBluePOIQuery
+ _OBJC_METACLASS_$_RTPlaceTypeClassifierExpertMaps
+ _OBJC_METACLASS_$_RTWiFiManagerNotificationLeechScanResults
+ _RTApplicationManagerExecutableLivTipsApp
+ _RTBluePOIQueryCodingKeyAccessPoints
+ _RTBluePOIQueryCodingKeyDate
+ _RTBluePOIQueryCodingKeyDateAsString
+ _RTBluePOIQueryCodingKeyIdentifier
+ _RTBluePOIQueryCodingKeyLocations
+ _RTBluePOIQueryCodingKeyReferenceLocation
+ _RTBluePOIQueryCodingKeySelectedToLabel
+ _RTBluePOIQueryCodingKeySettledState
+ _RTBluePOIQueryFirstJSONKeyAccessPoints
+ _RTBluePOIQueryFirstJSONKeyDate
+ _RTBluePOIQueryFirstJSONKeyIdentifier
+ _RTBluePOIQueryFirstJSONKeyLocations
+ _RTBluePOIQueryFirstJSONKeyReferenceLocationUncertainty
+ _RTVisitBluePOIReplayJSONKeyBluePOIQueries
+ _RTVisitBluePOIReplayJSONKeyConfidence
+ _RTVisitBluePOIReplayJSONKeyDataPointCount
+ _RTVisitBluePOIReplayJSONKeyDate
+ _RTVisitBluePOIReplayJSONKeyDateAsString
+ _RTVisitBluePOIReplayJSONKeyEntry
+ _RTVisitBluePOIReplayJSONKeyEntryDateAsString
+ _RTVisitBluePOIReplayJSONKeyExit
+ _RTVisitBluePOIReplayJSONKeyExitDateAsString
+ _RTVisitBluePOIReplayJSONKeyLocation
+ _RTVisitBluePOIReplayJSONKeyPlaceInference
+ _RTVisitBluePOIReplayJSONKeyPlaceInferenceConfidence
+ _RTVisitBluePOIReplayJSONKeyPlaceInferenceFinerGranularityMapItem
+ _RTVisitBluePOIReplayJSONKeyPlaceInferenceFinerGranularityMapItemConfidence
+ _RTVisitBluePOIReplayJSONKeyPlaceInferenceLoiIdentifier
+ _RTVisitBluePOIReplayJSONKeyPlaceInferenceMapItem
+ _RTVisitBluePOIReplayJSONKeyPlaceInferencePlaceType
+ _RTVisitBluePOIReplayJSONKeyPlaceInferencePreferredName
+ _RTVisitBluePOIReplayJSONKeyPlaceInferenceReferenceLocation
+ _RTVisitBluePOIReplayJSONKeyPlaceInferenceUserType
+ _RTVisitBluePOIReplayJSONKeyPlaceInferenceUserTypeSource
+ _RTVisitBluePOIReplayJSONKeySource
+ _RTVisitBluePOIReplayJSONKeyType
+ __101+[SMCloudKitZone fetchShareMetadataWithInvitationToken:sessionID:container:queue:qos:withCompletion:]_block_invoke.54
+ __101+[SMCloudKitZone fetchShareMetadataWithInvitationToken:sessionID:container:queue:qos:withCompletion:]_block_invoke_2.55
+ __101-[RTLearnedLocationStore _fetchCountOfVisitsToLocationOfInterestWithIdentifier:dateInterval:handler:]_block_invoke.307
+ __111-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:includePlaceholders:handler:]_block_invoke.374
+ __115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke.271
+ __115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke.273
+ __115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke_2.272
+ __115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke_2.274
+ __119+[RTPlaceDataMetrics calculateMLFeaturesUsingBiomeManager:intervalDictionary:startDate:endDate:createBucketedFeatures:]_block_invoke.1702
+ __143-[RTPlaceTypeClassifierMetricsCalculator _filterLearnedPlaceTypeInferencesWithPlaceType:dateInterval:metricsSource:learnedPlaceTypeInferences:]_block_invoke.218
+ __145+[RTLearnedLocationEngine submitVisitLabelingMetricsForLabelingRetried:labelingSkipped:revGeoCalled:bluePOICalled:unlabeledVisit:visitAge:error:]_block_invoke.794
+ __219-[RTDaemonClientInternal forceProcessWorkoutsClearClusters:clearExistingDistanceMatrix:buildDistanceMatrix:syncClustersToHealhtKit:syncClustersToWatch:filteringDistanceThreshold:topNWorkouts:isSchedulerTriggered:reply:]_block_invoke.770
+ __219-[RTDaemonClientInternal forceProcessWorkoutsClearClusters:clearExistingDistanceMatrix:buildDistanceMatrix:syncClustersToHealhtKit:syncClustersToWatch:filteringDistanceThreshold:topNWorkouts:isSchedulerTriggered:reply:]_block_invoke_2.771
+ __25-[RTDaemonClient restore]_block_invoke.604
+ __27-[RTLifeCycleManager _exit]_block_invoke.519
+ __27-[RTLifeCycleManager _exit]_block_invoke.525
+ __27-[RTLifeCycleManager _exit]_block_invoke.529
+ __27-[RTLifeCycleManager _exit]_block_invoke_2.526
+ __28-[RTLifeCycleManager _start]_block_invoke.510
+ __28-[RTLifeCycleManager _start]_block_invoke.516
+ __37-[SMInitiatorService _onWorkoutPause]_block_invoke.207
+ __40-[SMInitiatorService _onDeletedMessage:]_block_invoke.199
+ __43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.673
+ __44-[RTLearnedLocationStore _clearWithHandler:]_block_invoke.572
+ __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.67
+ __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.70
+ __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.74
+ __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.77
+ __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.78
+ __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.81
+ __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.82
+ __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.85
+ __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.86
+ __45-[SMInitiatorService _onDeletedConversation:]_block_invoke.202
+ __47-[RTClientListener _setupConnection:forClient:]_block_invoke.260
+ __47-[RTLearnedLocationStore _removePlace:handler:]_block_invoke.465
+ __47-[SMClientListener _setupConnection:forClient:]_block_invoke.276
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.157
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.159
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.161
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.163
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.165
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.158
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.160
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.162
+ __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.164
+ __49-[SMInitiatorService _startInitializationProcess]_block_invoke.179
+ __49-[SMInitiatorService _startInitializationProcess]_block_invoke.188
+ __49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.191
+ __50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.647
+ __50-[RTPlaceTypeClassifier getStoredPlacesWithError:]_block_invoke.14
+ __50-[RTPlaceTypeClassifier getStoredPlacesWithError:]_block_invoke.17
+ __51-[RTLearnedLocationEngine _getDailyTrainingMetrics]_block_invoke.704
+ __51-[RTLearnedLocationEngine _teardownTrainingMetrics]_block_invoke.770
+ __53-[RTClientListener handleRestorationForDaemonClient:]_block_invoke.263
+ __53-[RTLearnedLocationStore _fetchLastVisitWithHandler:]_block_invoke.295
+ __53-[RTLearnedLocationStore _fetchPlaceOfVisit:handler:]_block_invoke.210
+ __54-[RTLearnedLocationStore _fetchVisitsToPlace:handler:]_block_invoke.292
+ __54-[RTLearnedLocationStore _removeUnreferencedMapItems:]_block_invoke.576
+ __54-[RTLearnedLocationStore _removeUnreferencedMapItems:]_block_invoke_2.577
+ __55-[RTLearnedLocationEngine _retrainVisitsWithoutPlaces:]_block_invoke.780
+ __55-[RTLearnedLocationEngine trainForReason:mode:handler:]_block_invoke.530
+ __55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.595
+ __55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.613
+ __55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.416
+ __55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.417
+ __55-[SMInitiatorService _fetchSOSReceiversWithCompletion:]_block_invoke.265
+ __56-[SMCloudKitZone saveZoneToDatabase:qos:withCompletion:]_block_invoke.78
+ __56-[SMCloudKitZone saveZoneToDatabase:qos:withCompletion:]_block_invoke_2.79
+ __57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.662
+ __57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.663
+ __57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.126
+ __57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.128
+ __59-[RTLearnedLocationStore _fetchVisitIdentifiersIn:handler:]_block_invoke.315
+ __59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.647
+ __59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.643
+ __59-[SMCloudKitZone fetchZoneFromDatabase:qos:withCompletion:]_block_invoke.70
+ __59-[SMCloudKitZone fetchZoneFromDatabase:qos:withCompletion:]_block_invoke_2.71
+ __60-[RTLearnedLocationStore _fetchPlacesWithPredicate:handler:]_block_invoke.201
+ __60-[RTLearnedLocationStore _fetchVisitWithIdentifier:handler:]_block_invoke.269
+ __60-[SMCloudKitZone deleteZoneFromDatabase:qos:withCompletion:]_block_invoke.86
+ __60-[SMCloudKitZone deleteZoneFromDatabase:qos:withCompletion:]_block_invoke_2.87
+ __60-[SMCloudKitZone saveRecords:toDatabase:qos:withCompletion:]_block_invoke.114
+ __60-[SMCloudKitZone saveRecords:toDatabase:qos:withCompletion:]_block_invoke.115
+ __61-[RTLearnedLocationStore _removeVisitWithIdentifier:handler:]_block_invoke.554
+ __61-[RTPlaceTypeClassifier getClassificationsFromExperts:error:]_block_invoke.91
+ __62-[RTLearnedLocationStore _fetchPlacesWithIdentifiers:handler:]_block_invoke.274
+ __62-[RTPersonalizationPortraitManager feedbackUsedNamedEntities:]_block_invoke.39
+ __62-[SMCloudKitZone fetchRecord:fromDatabase:qos:withCompletion:]_block_invoke.122
+ __62-[SMCloudKitZone fetchRecord:fromDatabase:qos:withCompletion:]_block_invoke_2.123
+ __63-[RTLearnedLocationManager _reconstructTransitionsWithHandler:]_block_invoke.338
+ __63-[RTLearnedLocationManager _reconstructTransitionsWithHandler:]_block_invoke.339
+ __64-[SMCloudKitZone deleteRecords:fromDatabase:qos:withCompletion:]_block_invoke.131
+ __64-[SMCloudKitZone deleteRecords:fromDatabase:qos:withCompletion:]_block_invoke_2.132
+ __65-[RTLearnedLocationStore _fetchPlacesWithType:predicate:handler:]_block_invoke.207
+ __65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.217
+ __66-[RTLearnedLocationStore _fetchMapItemWithMuid:predicate:handler:]_block_invoke.444
+ __66-[RTLearnedLocationStore _removeRecordsExpiredBeforeDate:handler:]_block_invoke.568
+ __66-[SMSafetyCacheZone createRecordsWithParticipants:qos:completion:]_block_invoke.49
+ __67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.592
+ __67-[RTLearnedLocationManager _weeksInLearnedLocationsOfInterestModel]_block_invoke.240
+ __67-[RTLearnedLocationStore _fetchPlaceWithMapItemIdentifier:handler:]_block_invoke.265
+ __67-[SMInitiatorService _endSessionEarlyIfNecessaryWithConfiguration:]_block_invoke.259
+ __68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.478
+ __68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.483
+ __68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.484
+ __68-[RTLearnedLocationStore _fetchPlacesWithMapItem:predicate:handler:]_block_invoke.249
+ __68-[SMSafetyCacheZone updateSafetyCacheRecordWithData:qos:completion:]_block_invoke.63
+ __69-[SMInitiatorService _sendSessionStartMessageWithInvitationTokenMap:]_block_invoke.246
+ __70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.626
+ __70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.627
+ __70-[RTLearnedLocationEngine _saveIdentifiersOfKnownPlaceTypesWithError:]_block_invoke.683
+ __70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke.466
+ __70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke.470
+ __70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke_2.471
+ __70-[SMSafetyCacheZone setupZoneAndShareWithConversation:qos:completion:]_block_invoke.28
+ __70-[SMSafetyCacheZone setupZoneAndShareWithConversation:qos:completion:]_block_invoke.34
+ __70-[SMSafetyCacheZone setupZoneAndShareWithConversation:qos:completion:]_block_invoke.35
+ __71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke.749
+ __71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke_2.750
+ __71-[RTLearnedLocationStore _fetchLastVisitToPlaceWithIdentifier:handler:]_block_invoke.299
+ __72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.713
+ __72-[SMCloudKitZone fetchShareParticipantsWithConversation:qos:completion:]_block_invoke.101
+ __72-[SMCloudKitZone fetchShareParticipantsWithConversation:qos:completion:]_block_invoke_2.102
+ __72-[SMCloudKitZone updateRecord:inDatabase:qos:usingBlock:withCompletion:]_block_invoke.124
+ __73-[RTLearnedLocationStore _fetchLocationOfInterestVisitedLastWithHandler:]_block_invoke.401
+ __73-[RTLearnedLocationStore _fetchLocationsOfInterestWithPlaceType:handler:]_block_invoke.354
+ __74-[RTLearnedLocationEngine _relabelWithRelabeler:relabelerPersister:error:]_block_invoke.642
+ __74-[RTLearnedLocationStore _fetchInferredMapItemForVisitIdentifier:handler:]_block_invoke.399
+ __74-[RTLearnedLocationStore _fetchLocationOfInterestVisitedFirstWithHandler:]_block_invoke.400
+ __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.230
+ __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.234
+ __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.235
+ __75-[RTLearnedLocationEngine _appendVisits:lastVisit:lastTransition:outError:]_block_invoke.785
+ __75-[RTLearnedLocationEngine _appendVisits:lastVisit:lastTransition:outError:]_block_invoke.788
+ __75-[RTLearnedLocationEngine _appendVisits:lastVisit:lastTransition:outError:]_block_invoke_2.789
+ __75-[RTLearnedLocationEngine requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.571
+ __75-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:handler:]_block_invoke.300
+ __75-[SMCloudKitZone createNewInvitationTokensWithConversation:qos:completion:]_block_invoke.147
+ __75-[SMCloudKitZone createNewInvitationTokensWithConversation:qos:completion:]_block_invoke.149
+ __75-[SMCloudKitZone removeShareParticipantsInConversation:qos:withCompletion:]_block_invoke.135
+ __75-[SMCloudKitZone removeShareParticipantsInConversation:qos:withCompletion:]_block_invoke.139
+ __76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.585
+ __76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.586
+ __76-[RTLearnedLocationEngine _appendVisitsToLocationsOfInterestModelWithError:]_block_invoke.782
+ __76-[RTLearnedLocationEngine _requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.576
+ __76-[RTLearnedLocationEngine _submitPlaceTypeClassificationFeatureInputMetrics]_block_invoke.536
+ __76-[RTLearnedLocationStore _fetchStoredMapItemsWithMapItem:predicate:handler:]_block_invoke.236
+ __76-[RTLearnedLocationStore _fetchTransitionWithDestinationIdentifier:handler:]_block_invoke.335
+ __76-[RTLearnedLocationStore _fetchTransitionsBetweenStartDate:endDate:handler:]_block_invoke.329
+ __76-[RTLearnedLocationStore _fetchVisitsWithPredicate:ascending:limit:handler:]_block_invoke.283
+ __77-[RTLearnedLocationManager _fetchFamiliarityIndexResultsWithOptions:handler:]_block_invoke.350
+ __79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.632
+ __79-[SMSafetyCacheZone updateAccessDataRecordWithCacheReleaseTime:qos:completion:]_block_invoke.66
+ __80-[RTLearnedLocationStore _fetchPlacesWithinDistance:location:predicate:handler:]_block_invoke.256
+ __80-[RTPersonalizationPortraitManager fetchLocationNamesStartDate:endDate:handler:]_block_invoke.24
+ __81-[RTPlaceTypeClassifier replaceBusinessMapItemWithReverseGeocodedMapItemForHome:]_block_invoke.23
+ __81-[RTPlaceTypeClassifier replaceBusinessMapItemWithReverseGeocodedMapItemForHome:]_block_invoke.32
+ __82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.599
+ __82-[RTPlaceTypeClassifierExpertMaps _fetchPinnedPlacesWithKnownPlacesTypesAndError:]_block_invoke.8
+ __83-[RTLearnedLocationEngine _recoverKnownPlaceTypesWithPlaceTypeClassifier:outError:]_block_invoke.698
+ __83-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:endDate:handler:]_block_invoke.311
+ __83-[RTLearnedLocationStore _fetchLocationsOfInterestWithinDistance:location:handler:]_block_invoke.350
+ __85-[RTLearnedLocationManager _getAreasGeohashesFamiliarPlacesWithGranularity:outError:]_block_invoke.373
+ __85-[RTLearnedLocationManager _getAreasGeohashesFamiliarPlacesWithGranularity:outError:]_block_invoke.378
+ __88-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:customLabel:handler:]_block_invoke.285
+ __91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.614
+ __91-[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke.194
+ __92+[SMCloudKitZone acceptShareWithShareMetadata:sessionID:container:queue:qos:withCompletion:]_block_invoke.65
+ __92+[SMCloudKitZone acceptShareWithShareMetadata:sessionID:container:queue:qos:withCompletion:]_block_invoke_2.66
+ __92-[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:handler:]_block_invoke.207
+ __92-[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:handler:]_block_invoke.210
+ __93-[RTLearnedLocationManager _fetchDedupedLocationOfInterestIdentifiersWithIdentifier:handler:]_block_invoke.318
+ __94+[SMCloudKitZone acceptShareWithInvitationToken:sessionID:container:queue:qos:withCompletion:]_block_invoke.47
+ __97-[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngineWithPlaceStats:dateInterval:]_block_invoke.410
+ __98-[RTLearnedLocationEngine _fetchCloudCurrentDeviceVisitsBetweenStartDate:endDate:ascending:error:]_block_invoke.439
+ __98-[RTLearnedLocationEngine _fetchCloudCurrentDeviceVisitsBetweenStartDate:endDate:ascending:error:]_block_invoke.443
+ __OBJC_$_CLASS_METHODS_RTBluePOIQuery
+ __OBJC_$_CLASS_METHODS_RTVisit(RTCoreDataTransformable|VisitManager|RTExtensions)
+ __OBJC_$_CLASS_PROP_LIST_RTBluePOIQuery
+ __OBJC_$_INSTANCE_METHODS_RTBluePOIQuery
+ __OBJC_$_INSTANCE_METHODS_RTPlaceTypeClassifierExpertMaps
+ __OBJC_$_INSTANCE_METHODS_RTWiFiManagerNotificationLeechScanResults
+ __OBJC_$_INSTANCE_VARIABLES_RTBluePOIQuery
+ __OBJC_$_INSTANCE_VARIABLES_RTPlaceTypeClassifierExpertMaps
+ __OBJC_$_INSTANCE_VARIABLES_RTWiFiManagerNotificationLeechScanResults
+ __OBJC_$_PROP_LIST_RTBluePOIQuery
+ __OBJC_$_PROP_LIST_RTPlaceTypeClassifierExpertMaps
+ __OBJC_$_PROP_LIST_RTWiFiManagerNotificationLeechScanResults
+ __OBJC_$_PROP_LIST__TtP8MapsSync21MapsSyncStoreDelegate_
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__TtP8MapsSync21MapsSyncStoreDelegate_
+ __OBJC_$_PROTOCOL_METHOD_TYPES__TtP8MapsSync21MapsSyncStoreDelegate_
+ __OBJC_CLASS_PROTOCOLS_$_RTBluePOIQuery
+ __OBJC_CLASS_PROTOCOLS_$_RTMapsSupportManager
+ __OBJC_CLASS_PROTOCOLS_$_RTPinnedPlace
+ __OBJC_CLASS_PROTOCOLS_$_RTPlaceTypeClassifierExpertMaps
+ __OBJC_CLASS_RO_$_RTBluePOIQuery
+ __OBJC_CLASS_RO_$_RTPlaceTypeClassifierExpertMaps
+ __OBJC_CLASS_RO_$_RTWiFiManagerNotificationLeechScanResults
+ __OBJC_LABEL_PROTOCOL_$__TtP8MapsSync21MapsSyncStoreDelegate_
+ __OBJC_METACLASS_RO_$_RTBluePOIQuery
+ __OBJC_METACLASS_RO_$_RTPlaceTypeClassifierExpertMaps
+ __OBJC_METACLASS_RO_$_RTWiFiManagerNotificationLeechScanResults
+ __OBJC_PROTOCOL_$__TtP8MapsSync21MapsSyncStoreDelegate_
+ ___48-[RTMapsSupportManager storeDidChangeWithTypes:]_block_invoke
+ ___64-[RTLearnedLocationEngine sendDiagnosticsToURL:options:handler:]_block_invoke
+ ___65-[RTLearnedLocationStore fetchMapItemWithMuid:predicate:handler:]_block_invoke
+ ___66-[RTLearnedLocationStore _fetchMapItemWithMuid:predicate:handler:]_block_invoke
+ ___77-[RTPlaceTypeClassifierExpertMaps _convertPinnedPlacesToLearnedPlaces:error:]_block_invoke
+ ___77-[RTPlaceTypeClassifierModelRanker predictionFromFeatures:completionHandler:]_block_invoke
+ ___77-[SMSafetyCacheZone initWithSessionID:ownerName:token:defaultsManager:queue:]_block_invoke
+ ___77-[SMSafetyCacheZone initWithSessionID:ownerName:token:defaultsManager:queue:]_block_invoke_2
+ ___80-[RTDaemonClient fetchFinerGranularityInferredMapItemWithVisitIdentifier:reply:]_block_invoke
+ ___80-[RTDaemonClient fetchFinerGranularityInferredMapItemWithVisitIdentifier:reply:]_block_invoke_2
+ ___81-[RTPlaceTypeClassifierModelMultiClass predictionFromFeatures:completionHandler:]_block_invoke
+ ___82-[RTPlaceTypeClassifierExpertMaps _fetchPinnedPlacesWithKnownPlacesTypesAndError:]_block_invoke
+ ___85-[RTPlaceTypeClassifierModelRanker predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___87+[RTPlaceInferenceQueryMO managedObjectWithPlaceInferenceQuery:inManagedObjectContext:]_block_invoke_2
+ ___89-[RTPlaceTypeClassifierModelMultiClass predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___90-[RTLearnedLocationStore fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke
+ ___91-[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke
+ ___92-[RTLearnedLocationManager fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke
+ ___93-[RTLearnedLocationManager _fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke
+ ___93-[RTLearnedLocationManager _fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:]_block_invoke_2
+ ___95-[RTDaemonClientInternal injectVisit:finerGranularityInferredMapItem:locationOfInterest:reply:]_block_invoke
+ ___95-[RTDaemonClientInternal injectVisit:finerGranularityInferredMapItem:locationOfInterest:reply:]_block_invoke_2
+ ___96-[RTLearnedLocationManager addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:]_block_invoke
+ ___97-[RTLearnedLocationManager _addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:]_block_invoke
+ ___97-[RTLearnedLocationManager _addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:]_block_invoke_2
+ ___97-[RTLearnedLocationManager _addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:]_block_invoke_3
+ ___97-[RTLearnedLocationManager _addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:]_block_invoke_4
+ ___97-[RTLearnedLocationManager _addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:]_block_invoke_5
+ ___98-[RTLearnedLocationEngine _fetchCloudCurrentDeviceVisitsBetweenStartDate:endDate:ascending:error:]_block_invoke
+ ___block_descriptor_32_e40_B24?0"RTPinnedPlace"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32bs_e41_v24?0"<MLFeatureProvider>"8"NSError"16l
+ ___block_descriptor_40_e8_32s_e12_B24?08^B16l
+ ___block_descriptor_48_e8_32s40bs_e39_v24?0"RTInferredMapItem"8"NSError"16l
+ ___block_descriptor_48_e8_32s_e64_B24?0"RTLearnedPlaceTypeInferencePlaceStats"8"NSDictionary"16l
+ ___block_descriptor_56_e8_32s40r48r_e39_v24?0"RTInferredMapItem"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs_e39_v24?0"RTInferredMapItem"8"NSError"16l
+ ___block_descriptor_72_e8_32s40r48r56r64r_e53_v40?0"RTPlaceInference"8Q16"NSArray"24"NSError"32l
+ ___chkstk_darwin
+ __block_literal_global.1203
+ __block_literal_global.181
+ __block_literal_global.183
+ __block_literal_global.185
+ __block_literal_global.187
+ __block_literal_global.190
+ __block_literal_global.193
+ __block_literal_global.201
+ __block_literal_global.231
+ __block_literal_global.237
+ __block_literal_global.250
+ __block_literal_global.30
+ __block_literal_global.300
+ __block_literal_global.312
+ __block_literal_global.34
+ __block_literal_global.357
+ __block_literal_global.420
+ __block_literal_global.426
+ __block_literal_global.477
+ __block_literal_global.513
+ __block_literal_global.518
+ __block_literal_global.532
+ __block_literal_global.550
+ __block_literal_global.594
+ __block_literal_global.601
+ __block_literal_global.606
+ __block_literal_global.673
+ __block_literal_global.76
+ __block_literal_global.80
+ __block_literal_global.84
+ __block_literal_global.88
+ __block_literal_global.94
+ __block_literal_global.954
+ _kRTLocationFirstJSONKeyHorizontalUncertainty
+ _kRTLocationFirstJSONKeyLatitude
+ _kRTLocationFirstJSONKeyLongitude
+ _objc_msgSend$_addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:
+ _objc_msgSend$_bluePOIQueryFromFingerprint:fingerprintIdx:referenceLocationArray:selected:endDate:totalAPsCount:error:
+ _objc_msgSend$_convertPinnedPlacesToLearnedPlaces:error:
+ _objc_msgSend$_convertToIdToLearnedPlace:
+ _objc_msgSend$_extractBluePOIQueriesJSONDObjectBetweenStartDate:endDate:error:
+ _objc_msgSend$_extractBluePOIQueriesJSONDObjectForVisit:bluePOIMapItemProvider:
+ _objc_msgSend$_fetchAllFingerprintsBetweenStartDate:endDate:error:
+ _objc_msgSend$_fetchCloudCurrentDeviceVisitsBetweenStartDate:endDate:ascending:error:
+ _objc_msgSend$_fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:
+ _objc_msgSend$_fetchMapItemWithMuid:predicate:handler:
+ _objc_msgSend$_fetchPinnedPlacesWithKnownPlacesTypesAndError:
+ _objc_msgSend$_getClosestLearnedPlacesAtDestination:source:threshold:error:
+ _objc_msgSend$_logExpertClassifications:sourceNames:
+ _objc_msgSend$_mapItemsFromBluePOIQuery:startDate:endDate:error:
+ _objc_msgSend$_refreshMapItemsForLocationsOfInterestWithError:
+ _objc_msgSend$_selectFingerprintsStartDate:endDate:maxQueryAttemps:isTimeWindowFallback:fingerprintsTotalOut:fingerprintsNonZeroAPsTotalOut:error:
+ _objc_msgSend$addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:
+ _objc_msgSend$allPlaceTypes
+ _objc_msgSend$classForMapsSyncClassName:
+ _objc_msgSend$classNameForMapsSyncClass:
+ _objc_msgSend$classNamesForMapsSyncClasses:
+ _objc_msgSend$coalescePlacesFromSourcesOfTruth:sourceOfTruthNames:
+ _objc_msgSend$dataWithBluePOIQueriesBetweenStartDate:endDate:error:
+ _objc_msgSend$dictionaryOutForBluePOIReplayWithBluePOIQueries:
+ _objc_msgSend$fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:
+ _objc_msgSend$getAllBluePOIQuerriesForStartDate:endDate:location:error:
+ _objc_msgSend$getFormattedDateString
+ _objc_msgSend$inferredPlaceTypes
+ _objc_msgSend$initWithDistanceCalculator:learnedLocationStore:locationManager:mapServiceManager:visitManager:placeTypeClassifierMetricsCalculator:
+ _objc_msgSend$initWithFirstJSONDictionary:
+ _objc_msgSend$initWithIdentifier:accessPoints:locations:referenceLocation:settledState:selectedToLabel:date:
+ _objc_msgSend$initWithLearnedLocationStore:mapsSupportManager:placeTypeClassifierMetricsCalculator:
+ _objc_msgSend$initWithLearnedVisit:inferredMapItem:finerGranularityInferredMapItem:userPlaceType:userPlaceTypeSource:loiIdentifier:
+ _objc_msgSend$initWithQueryType:
+ _objc_msgSend$mapsFavoritesPredicateWithHidden:includeNearbyTransit:
+ _objc_msgSend$metadata
+ _objc_msgSend$modelDescription
+ _objc_msgSend$nonInferredPlaceTypes
+ _objc_msgSend$objectsPassingTest:
+ _objc_msgSend$outputToDictionaryReadableDate:
+ _objc_msgSend$outputToFirstJSONDictionary
+ _objc_msgSend$predictionFromFeatures:completionHandler:
+ _objc_msgSend$predictionFromFeatures:options:completionHandler:
+ _objc_msgSend$queryTypeForMapsSyncClass:
+ _objc_msgSend$queryTypeForMapsSyncClassName:
+ _objc_msgSend$routineBluePOIQueryPath
+ _objc_msgSend$scenarioTriggerSettledStateToString:
+ _objc_msgSend$schoolGymEligibleSources
+ _objc_msgSend$selectedToLabel
+ _objc_msgSend$sharedStore
+ _objc_msgSend$storeChangeNotificationClasses
+ _objc_msgSend$storeVisits:finerGranularityInferredMapItems:place:handler:
+ _objc_msgSend$stringForQueryType:
+ _objc_msgSend$stringFromVisitSource:
+ _objc_msgSend$subscribe:
+ _objc_msgSend$userSpecificPlaceTypeSourceToString:
+ _objc_msgSend$userSpecificPlaceTypeToString:
+ _objc_msgSend$writeToFile:options:error:
+ _objc_msgSend$zelkovaKoreaEnabled
- +[RTDeviceMetricManager getDateIntervalFromDictionary:]
- +[RTDeviceMetricManager getDictionaryFromDateInterval:]
- +[RTDeviceMetricManager getMetricsDictionaryForMetricType:intervals:bins:]
- +[RTDeviceMetricManager getReachabilityDefaultStringForTopN:reachability:]
- +[RTDeviceMetricManager getStringForMetricType:topN:]
- +[RTDuetKnowledgeStream duetKnowledgeStreamTypeToDuetEventStream:]
- +[RTDuetKnowledgeStream streamTypeToString:]
- +[RTPlaceDataMetrics calculateMLFeatures:startDate:endDate:createBucketedFeatures:]
- +[RTPlaceTypeClassifierMetricsCalculator schoolEligibleSources]
- -[RTDaemonClientInternal injectVisit:locationOfInterest:reply:]
- -[RTDeviceMetricManager .cxx_destruct]
- -[RTDeviceMetricManager _addToHeapForReachability:endDate:dateInterval:]
- -[RTDeviceMetricManager _addToHeapForReachability:endDate:dateIntervals:]
- -[RTDeviceMetricManager _flippedDateIntervalsFromIntervals:originalDateInterval:error:]
- -[RTDeviceMetricManager _getDeviceMetricsWithError:]
- -[RTDeviceMetricManager _getFromHeapDateIntervalsForReachability:]
- -[RTDeviceMetricManager _getLongestIntervalWithStreamType:topN:dateInterval:flipDateIntervals:error:]
- -[RTDeviceMetricManager _getLongestStationaryMotionIntervalsWithTopN:dateInterval:error:]
- -[RTDeviceMetricManager _onDailyMetricsNotification:]
- -[RTDeviceMetricManager _onReachabilityChanged:]
- -[RTDeviceMetricManager _setup]
- -[RTDeviceMetricManager _submitDeviceMetricsWithError:]
- -[RTDeviceMetricManager defaultsManager]
- -[RTDeviceMetricManager duetKnowledgeStore]
- -[RTDeviceMetricManager getLongestDeviceChargingIntervalsWithTopN:dateInterval:error:]
- -[RTDeviceMetricManager getLongestDeviceLockedIntervalsWithTopN:dateInterval:error:]
- -[RTDeviceMetricManager getLongestDeviceNotChargingIntervalsWithTopN:dateInterval:error:]
- -[RTDeviceMetricManager getLongestStationaryMotionIntervalsWithTopN:dateInterval:error:]
- -[RTDeviceMetricManager getLongestWiFiConnectionIntervalsWithTopN:dateInterval:error:]
- -[RTDeviceMetricManager initWithDefaultsManager:motionActivityManager:reachabilityManager:]
- -[RTDeviceMetricManager motionActivityManager]
- -[RTDeviceMetricManager onDailyMetricsNotification:]
- -[RTDeviceMetricManager onReachabilityChanged:]
- -[RTDeviceMetricManager reachabilityManager]
- -[RTDeviceMetricManager setDefaultsManager:]
- -[RTDeviceMetricManager setDuetKnowledgeStore:]
- -[RTDeviceMetricManager setMotionActivityManager:]
- -[RTDeviceMetricManager setReachabilityManager:]
- -[RTDeviceMetricManager setup]
- -[RTDuetKnowledgeStore .cxx_destruct]
- -[RTDuetKnowledgeStore clearEventsFromStream:completion:]
- -[RTDuetKnowledgeStore executeQuery:completion:]
- -[RTDuetKnowledgeStore init]
- -[RTDuetKnowledgeStore knowledgeStoreQuery]
- -[RTDuetKnowledgeStore knowledgeStore]
- -[RTDuetKnowledgeStore queue]
- -[RTDuetKnowledgeStore requestQueue]
- -[RTDuetKnowledgeStore reset]
- -[RTDuetKnowledgeStore resume]
- -[RTDuetKnowledgeStore saveEvents:completion:]
- -[RTDuetKnowledgeStore setKnowledgeStore:]
- -[RTDuetKnowledgeStore setKnowledgeStoreQuery:]
- -[RTDuetKnowledgeStore setQueue:]
- -[RTDuetKnowledgeStore setRequestQueue:]
- -[RTDuetKnowledgeStream .cxx_destruct]
- -[RTDuetKnowledgeStream _convertDuetEvent:]
- -[RTDuetKnowledgeStream dealloc]
- -[RTDuetKnowledgeStream description]
- -[RTDuetKnowledgeStream enumerateEventsWithinDateInterval:usingBlock:]
- -[RTDuetKnowledgeStream eventStream]
- -[RTDuetKnowledgeStream initWithDuetKnowledgeStore:streamType:]
- -[RTDuetKnowledgeStream initWithStreamType:knowledgeStore:]
- -[RTDuetKnowledgeStream init]
- -[RTDuetKnowledgeStream knowledgeStore]
- -[RTDuetKnowledgeStream purge]
- -[RTDuetKnowledgeStream setEventStream:]
- -[RTDuetKnowledgeStream setKnowledgeStore:]
- -[RTDuetKnowledgeStream streamType]
- -[RTLearnedLocationManager _addVisit:locationOfInterest:handler:]
- -[RTLearnedLocationManager addVisit:locationOfInterest:handler:]
- -[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemForVisit:handler:]
- -[RTPlaceTypeClassifierExpertFallback initWithDistanceCalculator:learnedLocationStore:locationManager:mapServiceManager:visitManager:]
- -[SMDaemonClient fetchSessionReceiptForSessionID:completion:]
- -[SMInitiatorService _fetchAllZonesFromContainerSynchronizerWithHandler:]
- -[SMInitiatorService _fetchAllZonesFromContainerWithHandler:]
- -[SMInitiatorService _fetchSessionReceiptForSessionID:completion:]
- -[SMInitiatorService _initializeSessionReceiptZone]
- -[SMInitiatorService _startFrequentSingleShotFetchAllZonesActivity]
- -[SMInitiatorService _startInfrequentPeriodicFetchAllZonesActivity]
- -[SMInitiatorService _stopFrequentSingleShotFetchAllZonesActivity]
- -[SMInitiatorService fetchSessionReceiptForSessionID:completion:]
- -[SMInitiatorService sessionReceiptZone]
- -[SMInitiatorService setSessionReceiptZone:]
- -[SMSessionReceiptZone .cxx_destruct]
- -[SMSessionReceiptZone _writeSessionReceiptRecord:completion:]
- -[SMSessionReceiptZone checkSessionReceiptFieldsAvailibility:sessionID:]
- -[SMSessionReceiptZone checkSessionReceiptZoneAvailibilityWithCompletion:]
- -[SMSessionReceiptZone fetchSessionReceiptRecordWithSessionID:qos:completion:]
- -[SMSessionReceiptZone initWithQueue:]
- -[SMSessionReceiptZone sessionReceiptZoneAvailable]
- -[SMSessionReceiptZone sessionReceipts]
- -[SMSessionReceiptZone setSessionReceiptZoneAvailable:]
- -[SMSessionReceiptZone setSessionReceipts:]
- -[SMSessionReceiptZone setupZoneWithQos:completion:]
- -[SMSessionReceiptZone writeSessionReceiptRecord:completion:]
- GCC_except_table102
- GCC_except_table109
- GCC_except_table130
- GCC_except_table138
- GCC_except_table163
- GCC_except_table166
- GCC_except_table194
- GCC_except_table207
- GCC_except_table210
- GCC_except_table219
- GCC_except_table221
- GCC_except_table224
- GCC_except_table228
- GCC_except_table248
- GCC_except_table257
- GCC_except_table265
- GCC_except_table274
- GCC_except_table287
- GCC_except_table290
- GCC_except_table311
- GCC_except_table389
- GCC_except_table397
- OBJC_IVAR_$_RTDuetKnowledgeStore._knowledgeStore
- OBJC_IVAR_$_RTDuetKnowledgeStore._knowledgeStoreQuery
- OBJC_IVAR_$_RTDuetKnowledgeStore._queue
- OBJC_IVAR_$_RTDuetKnowledgeStore._requestQueue
- OBJC_IVAR_$_RTDuetKnowledgeStream._eventStream
- OBJC_IVAR_$_RTDuetKnowledgeStream._knowledgeStore
- OBJC_IVAR_$_RTDuetKnowledgeStream._streamType
- OBJC_IVAR_$_RTMapsSupportManager._mapServiceManager
- OBJC_IVAR_$_SMSessionReceiptZone._sessionReceiptZoneAvailable
- OBJC_IVAR_$_SMSessionReceiptZone._sessionReceipts
- _OBJC_CLASS_$_RTDeviceMetricManager
- _OBJC_CLASS_$_RTDuetKnowledgeStore
- _OBJC_CLASS_$_RTDuetKnowledgeStream
- _OBJC_CLASS_$_SMSessionReceipt
- _OBJC_CLASS_$_SMSessionReceiptZone
- _OBJC_CLASS_$__DKEventQuery
- _OBJC_CLASS_$__DKKnowledgeStore
- _OBJC_CLASS_$__DKMotionCategory
- _OBJC_CLASS_$__DKQuery
- _OBJC_CLASS_$__DKSystemEventStreams
- _OBJC_METACLASS_$_RTDeviceMetricManager
- _OBJC_METACLASS_$_RTDuetKnowledgeStore
- _OBJC_METACLASS_$_RTDuetKnowledgeStream
- _OBJC_METACLASS_$_SMSessionReceiptZone
- _RTAnalyticsEventInactivityDeviceMetrics
- _RTDuetKnowledgeStoreDomain
- _RTDuetKnowledgeStreamErrorDomain
- _RTLogFacilityDuet
- __101+[SMCloudKitZone fetchShareMetadataWithInvitationToken:sessionID:container:queue:qos:withCompletion:]_block_invoke.59
- __101+[SMCloudKitZone fetchShareMetadataWithInvitationToken:sessionID:container:queue:qos:withCompletion:]_block_invoke_2.60
- __101-[RTDeviceMetricManager _getLongestIntervalWithStreamType:topN:dateInterval:flipDateIntervals:error:]_block_invoke.75
- __101-[RTLearnedLocationStore _fetchCountOfVisitsToLocationOfInterestWithIdentifier:dateInterval:handler:]_block_invoke.304
- __111-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:includePlaceholders:handler:]_block_invoke.368
- __115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke.266
- __115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke.268
- __115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke_2.267
- __115-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:type:mapItem:mapItemSource:customLabel:handler:]_block_invoke_2.269
- __119+[RTPlaceDataMetrics calculateMLFeaturesUsingBiomeManager:intervalDictionary:startDate:endDate:createBucketedFeatures:]_block_invoke.1706
- __143-[RTPlaceTypeClassifierMetricsCalculator _filterLearnedPlaceTypeInferencesWithPlaceType:dateInterval:metricsSource:learnedPlaceTypeInferences:]_block_invoke.212
- __145+[RTLearnedLocationEngine submitVisitLabelingMetricsForLabelingRetried:labelingSkipped:revGeoCalled:bluePOICalled:unlabeledVisit:visitAge:error:]_block_invoke.771
- __219-[RTDaemonClientInternal forceProcessWorkoutsClearClusters:clearExistingDistanceMatrix:buildDistanceMatrix:syncClustersToHealhtKit:syncClustersToWatch:filteringDistanceThreshold:topNWorkouts:isSchedulerTriggered:reply:]_block_invoke.769
- __219-[RTDaemonClientInternal forceProcessWorkoutsClearClusters:clearExistingDistanceMatrix:buildDistanceMatrix:syncClustersToHealhtKit:syncClustersToWatch:filteringDistanceThreshold:topNWorkouts:isSchedulerTriggered:reply:]_block_invoke_2.770
- __25-[RTDaemonClient restore]_block_invoke.601
- __27-[RTLifeCycleManager _exit]_block_invoke.520
- __27-[RTLifeCycleManager _exit]_block_invoke.526
- __27-[RTLifeCycleManager _exit]_block_invoke.531
- __27-[RTLifeCycleManager _exit]_block_invoke_2.527
- __28-[RTLifeCycleManager _start]_block_invoke.511
- __28-[RTLifeCycleManager _start]_block_invoke.517
- __37-[SMInitiatorService _onWorkoutPause]_block_invoke.220
- __40-[SMInitiatorService _onDeletedMessage:]_block_invoke.212
- __43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.672
- __44-[RTLearnedLocationStore _clearWithHandler:]_block_invoke.565
- __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.40
- __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.46
- __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.49
- __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.53
- __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.56
- __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.57
- __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.60
- __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.64
- __44-[RTPlaceTypeClassifier updatePlaces:error:]_block_invoke.65
- __45-[SMInitiatorService _onDeletedConversation:]_block_invoke.215
- __47-[RTClientListener _setupConnection:forClient:]_block_invoke.258
- __47-[RTLearnedLocationStore _removePlace:handler:]_block_invoke.458
- __47-[SMClientListener _setupConnection:forClient:]_block_invoke.279
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.170
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.172
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.174
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.176
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke.178
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.171
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.173
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.175
- __49-[SMInitiatorService _purgePredating:completion:]_block_invoke_2.177
- __49-[SMInitiatorService _startInitializationProcess]_block_invoke.192
- __49-[SMInitiatorService _startInitializationProcess]_block_invoke.201
- __49-[SMInitiatorService _startInitializationProcess]_block_invoke_2.204
- __50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.644
- __50-[RTPlaceTypeClassifier getStoredPlacesWithError:]_block_invoke.12
- __50-[RTPlaceTypeClassifier getStoredPlacesWithError:]_block_invoke.9
- __51-[RTLearnedLocationEngine _getDailyTrainingMetrics]_block_invoke.683
- __51-[RTLearnedLocationEngine _teardownTrainingMetrics]_block_invoke.747
- __53-[RTClientListener handleRestorationForDaemonClient:]_block_invoke.261
- __53-[RTLearnedLocationStore _fetchLastVisitWithHandler:]_block_invoke.292
- __53-[RTLearnedLocationStore _fetchPlaceOfVisit:handler:]_block_invoke.207
- __54-[RTLearnedLocationStore _fetchVisitsToPlace:handler:]_block_invoke.289
- __54-[RTLearnedLocationStore _removeUnreferencedMapItems:]_block_invoke.569
- __54-[RTLearnedLocationStore _removeUnreferencedMapItems:]_block_invoke_2.570
- __55-[RTLearnedLocationEngine _retrainVisitsWithoutPlaces:]_block_invoke.757
- __55-[RTLearnedLocationEngine trainForReason:mode:handler:]_block_invoke.511
- __55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.588
- __55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.606
- __55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.414
- __55-[RTLearnedPlaceTypeInferenceGenerator fuseInferences:]_block_invoke.415
- __55-[SMInitiatorService _fetchSOSReceiversWithCompletion:]_block_invoke.310
- __56-[SMCloudKitZone saveZoneToDatabase:qos:withCompletion:]_block_invoke.83
- __56-[SMCloudKitZone saveZoneToDatabase:qos:withCompletion:]_block_invoke_2.84
- __57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.643
- __57-[RTLearnedLocationEngine _purgeWithReferenceDate:error:]_block_invoke.644
- __57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.137
- __57-[SMInitiatorService _setupOncePersistenceStackAvailable]_block_invoke.139
- __59-[RTLearnedLocationStore _fetchVisitIdentifiersIn:handler:]_block_invoke.312
- __59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.640
- __59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.636
- __59-[SMCloudKitZone fetchZoneFromDatabase:qos:withCompletion:]_block_invoke.75
- __59-[SMCloudKitZone fetchZoneFromDatabase:qos:withCompletion:]_block_invoke_2.76
- __60-[RTLearnedLocationStore _fetchPlacesWithPredicate:handler:]_block_invoke.198
- __60-[RTLearnedLocationStore _fetchVisitWithIdentifier:handler:]_block_invoke.266
- __60-[SMCloudKitZone deleteZoneFromDatabase:qos:withCompletion:]_block_invoke.91
- __60-[SMCloudKitZone deleteZoneFromDatabase:qos:withCompletion:]_block_invoke_2.92
- __60-[SMCloudKitZone saveRecords:toDatabase:qos:withCompletion:]_block_invoke.120
- __60-[SMCloudKitZone saveRecords:toDatabase:qos:withCompletion:]_block_invoke.121
- __61-[RTLearnedLocationStore _removeVisitWithIdentifier:handler:]_block_invoke.547
- __61-[RTPlaceTypeClassifier getClassificationsFromExperts:error:]_block_invoke.70
- __61-[SMInitiatorService _fetchAllZonesFromContainerWithHandler:]_block_invoke.229
- __62-[RTLearnedLocationStore _fetchPlacesWithIdentifiers:handler:]_block_invoke.268
- __62-[RTPersonalizationPortraitManager feedbackUsedNamedEntities:]_block_invoke.33
- __62-[SMCloudKitZone fetchRecord:fromDatabase:qos:withCompletion:]_block_invoke.128
- __62-[SMCloudKitZone fetchRecord:fromDatabase:qos:withCompletion:]_block_invoke_2.129
- __63-[RTLearnedLocationManager _reconstructTransitionsWithHandler:]_block_invoke.333
- __63-[RTLearnedLocationManager _reconstructTransitionsWithHandler:]_block_invoke.335
- __64-[SMCloudKitZone deleteRecords:fromDatabase:qos:withCompletion:]_block_invoke.137
- __64-[SMCloudKitZone deleteRecords:fromDatabase:qos:withCompletion:]_block_invoke_2.138
- __65-[RTLearnedLocationStore _fetchPlacesWithType:predicate:handler:]_block_invoke.204
- __65-[SMInitiatorService _initializeSessionWithConversation:handler:]_block_invoke.262
- __66-[RTLearnedLocationStore _removeRecordsExpiredBeforeDate:handler:]_block_invoke.561
- __66-[SMInitiatorService _fetchSessionReceiptForSessionID:completion:]_block_invoke.316
- __66-[SMSafetyCacheZone createRecordsWithParticipants:qos:completion:]_block_invoke.44
- __67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.589
- __67-[RTLearnedLocationManager _weeksInLearnedLocationsOfInterestModel]_block_invoke.235
- __67-[RTLearnedLocationStore _fetchPlaceWithMapItemIdentifier:handler:]_block_invoke.262
- __67-[SMInitiatorService _endSessionEarlyIfNecessaryWithConfiguration:]_block_invoke.304
- __67-[SMInitiatorService _startFrequentSingleShotFetchAllZonesActivity]_block_invoke.239
- __67-[SMInitiatorService _startInfrequentPeriodicFetchAllZonesActivity]_block_invoke.250
- __68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.459
- __68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.464
- __68-[RTLearnedLocationEngine _processVisits:forLastLearnedVisit:error:]_block_invoke.465
- __68-[RTLearnedLocationStore _fetchPlacesWithMapItem:predicate:handler:]_block_invoke.246
- __68-[SMSafetyCacheZone updateSafetyCacheRecordWithData:qos:completion:]_block_invoke.56
- __69-[SMInitiatorService _sendSessionStartMessageWithInvitationTokenMap:]_block_invoke.291
- __70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.623
- __70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.624
- __70-[RTLearnedLocationEngine _saveIdentifiersOfKnownPlaceTypesWithError:]_block_invoke.662
- __70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke.447
- __70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke.451
- __70-[RTLearnedLocationEngine _updateUnlabeledVisitsWithPlaceInformation:]_block_invoke_2.452
- __70-[SMSafetyCacheZone setupZoneAndShareWithConversation:qos:completion:]_block_invoke.23
- __70-[SMSafetyCacheZone setupZoneAndShareWithConversation:qos:completion:]_block_invoke.29
- __70-[SMSafetyCacheZone setupZoneAndShareWithConversation:qos:completion:]_block_invoke.30
- __71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke.726
- __71-[RTLearnedLocationEngine performPurgeOfType:referenceDate:completion:]_block_invoke_2.727
- __71-[RTLearnedLocationStore _fetchLastVisitToPlaceWithIdentifier:handler:]_block_invoke.296
- __72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.712
- __72-[SMCloudKitZone fetchShareParticipantsWithConversation:qos:completion:]_block_invoke.106
- __72-[SMCloudKitZone fetchShareParticipantsWithConversation:qos:completion:]_block_invoke_2.107
- __72-[SMCloudKitZone updateRecord:inDatabase:qos:usingBlock:withCompletion:]_block_invoke.130
- __73-[RTLearnedLocationStore _fetchLocationOfInterestVisitedLastWithHandler:]_block_invoke.398
- __73-[RTLearnedLocationStore _fetchLocationsOfInterestWithPlaceType:handler:]_block_invoke.351
- __74-[RTLearnedLocationEngine _relabelWithRelabeler:relabelerPersister:error:]_block_invoke.623
- __74-[RTLearnedLocationStore _fetchInferredMapItemForVisitIdentifier:handler:]_block_invoke.396
- __74-[RTLearnedLocationStore _fetchLocationOfInterestVisitedFirstWithHandler:]_block_invoke.397
- __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.275
- __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.279
- __74-[SMInitiatorService _initializeAndStartSessionWithConfiguration:handler:]_block_invoke.280
- __74-[SMSessionReceiptZone checkSessionReceiptZoneAvailibilityWithCompletion:]_block_invoke.26
- __75-[RTLearnedLocationEngine _appendVisits:lastVisit:lastTransition:outError:]_block_invoke.762
- __75-[RTLearnedLocationEngine _appendVisits:lastVisit:lastTransition:outError:]_block_invoke.765
- __75-[RTLearnedLocationEngine _appendVisits:lastVisit:lastTransition:outError:]_block_invoke_2.766
- __75-[RTLearnedLocationEngine requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.552
- __75-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:handler:]_block_invoke.297
- __75-[SMCloudKitZone createNewInvitationTokensWithConversation:qos:completion:]_block_invoke.153
- __75-[SMCloudKitZone createNewInvitationTokensWithConversation:qos:completion:]_block_invoke.155
- __75-[SMCloudKitZone removeShareParticipantsInConversation:qos:withCompletion:]_block_invoke.141
- __75-[SMCloudKitZone removeShareParticipantsInConversation:qos:withCompletion:]_block_invoke.145
- __76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.582
- __76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.583
- __76-[RTLearnedLocationEngine _appendVisitsToLocationsOfInterestModelWithError:]_block_invoke.759
- __76-[RTLearnedLocationEngine _requestTrainLocationsOfInterestModelWithHandler:]_block_invoke.557
- __76-[RTLearnedLocationEngine _submitPlaceTypeClassificationFeatureInputMetrics]_block_invoke.517
- __76-[RTLearnedLocationStore _fetchStoredMapItemsWithMapItem:predicate:handler:]_block_invoke.233
- __76-[RTLearnedLocationStore _fetchTransitionWithDestinationIdentifier:handler:]_block_invoke.332
- __76-[RTLearnedLocationStore _fetchTransitionsBetweenStartDate:endDate:handler:]_block_invoke.326
- __76-[RTLearnedLocationStore _fetchVisitsWithPredicate:ascending:limit:handler:]_block_invoke.280
- __77-[RTLearnedLocationManager _fetchFamiliarityIndexResultsWithOptions:handler:]_block_invoke.347
- __78-[SMSessionReceiptZone fetchSessionReceiptRecordWithSessionID:qos:completion:]_block_invoke.33
- __79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.629
- __79-[SMSafetyCacheZone updateAccessDataRecordWithCacheReleaseTime:qos:completion:]_block_invoke.59
- __80-[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemForVisit:handler:]_block_invoke.196
- __80-[RTLearnedLocationStore _fetchPlacesWithinDistance:location:predicate:handler:]_block_invoke.253
- __80-[RTPersonalizationPortraitManager fetchLocationNamesStartDate:endDate:handler:]_block_invoke.18
- __81-[RTPlaceTypeClassifier replaceBusinessMapItemWithReverseGeocodedMapItemForHome:]_block_invoke.18
- __81-[RTPlaceTypeClassifier replaceBusinessMapItemWithReverseGeocodedMapItemForHome:]_block_invoke.22
- __82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.596
- __83+[RTPlaceDataMetrics calculateMLFeatures:startDate:endDate:createBucketedFeatures:]_block_invoke.1689
- __83-[RTLearnedLocationEngine _recoverKnownPlaceTypesWithPlaceTypeClassifier:outError:]_block_invoke.677
- __83-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:endDate:handler:]_block_invoke.308
- __83-[RTLearnedLocationStore _fetchLocationsOfInterestWithinDistance:location:handler:]_block_invoke.347
- __85-[RTLearnedLocationManager _getAreasGeohashesFamiliarPlacesWithGranularity:outError:]_block_invoke.370
- __85-[RTLearnedLocationManager _getAreasGeohashesFamiliarPlacesWithGranularity:outError:]_block_invoke.375
- __88-[RTLearnedLocationManager _updateLocationOfInterestWithIdentifier:customLabel:handler:]_block_invoke.280
- __91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.607
- __92+[SMCloudKitZone acceptShareWithShareMetadata:sessionID:container:queue:qos:withCompletion:]_block_invoke.70
- __92+[SMCloudKitZone acceptShareWithShareMetadata:sessionID:container:queue:qos:withCompletion:]_block_invoke_2.71
- __92-[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:handler:]_block_invoke.202
- __92-[RTLearnedLocationManager _fetchHindsightVisitsBetweenStartDate:endDate:ascending:handler:]_block_invoke.205
- __93-[RTLearnedLocationManager _fetchDedupedLocationOfInterestIdentifiersWithIdentifier:handler:]_block_invoke.315
- __94+[SMCloudKitZone acceptShareWithInvitationToken:sessionID:container:queue:qos:withCompletion:]_block_invoke.53
- __97-[RTLearnedPlaceTypeInferenceGenerator inferPlaceTypesFromRuleEngineWithPlaceStats:dateInterval:]_block_invoke.408
- __OBJC_$_CATEGORY_CLASS_METHODS_RTVisit_$_RTCoreDataTransformable
- __OBJC_$_CLASS_METHODS_RTDeviceMetricManager
- __OBJC_$_CLASS_METHODS_RTDuetKnowledgeStream
- __OBJC_$_INSTANCE_METHODS_RTDeviceMetricManager
- __OBJC_$_INSTANCE_METHODS_RTDuetKnowledgeStore
- __OBJC_$_INSTANCE_METHODS_RTDuetKnowledgeStream
- __OBJC_$_INSTANCE_METHODS_SMSessionReceiptZone
- __OBJC_$_INSTANCE_VARIABLES_RTDeviceMetricManager
- __OBJC_$_INSTANCE_VARIABLES_RTDuetKnowledgeStore
- __OBJC_$_INSTANCE_VARIABLES_RTDuetKnowledgeStream
- __OBJC_$_INSTANCE_VARIABLES_SMSessionReceiptZone
- __OBJC_$_PROP_LIST_RTDeviceMetricManager
- __OBJC_$_PROP_LIST_RTDuetKnowledgeStore
- __OBJC_$_PROP_LIST_RTDuetKnowledgeStream
- __OBJC_$_PROP_LIST_SMSessionReceiptZone
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SMInitiatorProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_SMInitiatorProtocol
- __OBJC_CLASS_RO_$_RTDeviceMetricManager
- __OBJC_CLASS_RO_$_RTDuetKnowledgeStore
- __OBJC_CLASS_RO_$_RTDuetKnowledgeStream
- __OBJC_CLASS_RO_$_SMSessionReceiptZone
- __OBJC_LABEL_PROTOCOL_$_SMInitiatorProtocol
- __OBJC_METACLASS_RO_$_RTDeviceMetricManager
- __OBJC_METACLASS_RO_$_RTDuetKnowledgeStore
- __OBJC_METACLASS_RO_$_RTDuetKnowledgeStream
- __OBJC_METACLASS_RO_$_SMSessionReceiptZone
- __OBJC_PROTOCOL_$_SMInitiatorProtocol
- __OBJC_PROTOCOL_REFERENCE_$_SMInitiatorProtocol
- ___101-[RTDeviceMetricManager _getLongestIntervalWithStreamType:topN:dateInterval:flipDateIntervals:error:]_block_invoke
- ___29-[RTDuetKnowledgeStore reset]_block_invoke
- ___29-[RTMapServiceManager _setup]_block_invoke
- ___30-[RTDeviceMetricManager setup]_block_invoke
- ___37-[SMCloudKitZone initWithZone:queue:]_block_invoke
- ___37-[SMCloudKitZone initWithZone:queue:]_block_invoke_2
- ___46-[RTDuetKnowledgeStore saveEvents:completion:]_block_invoke
- ___47-[RTDeviceMetricManager onReachabilityChanged:]_block_invoke
- ___48-[RTDuetKnowledgeStore executeQuery:completion:]_block_invoke
- ___51-[SMInitiatorService _initializeSessionReceiptZone]_block_invoke
- ___52-[RTDeviceMetricManager onDailyMetricsNotification:]_block_invoke
- ___52-[SMSessionReceiptZone setupZoneWithQos:completion:]_block_invoke
- ___57-[RTDuetKnowledgeStore clearEventsFromStream:completion:]_block_invoke
- ___57-[RTDuetKnowledgeStore clearEventsFromStream:completion:]_block_invoke_2
- ___61-[SMInitiatorService _fetchAllZonesFromContainerWithHandler:]_block_invoke
- ___61-[SMSessionReceiptZone writeSessionReceiptRecord:completion:]_block_invoke
- ___62-[SMSessionReceiptZone _writeSessionReceiptRecord:completion:]_block_invoke
- ___63-[RTDaemonClientInternal injectVisit:locationOfInterest:reply:]_block_invoke
- ___63-[RTDaemonClientInternal injectVisit:locationOfInterest:reply:]_block_invoke_2
- ___64-[RTLearnedLocationManager addVisit:locationOfInterest:handler:]_block_invoke
- ___65-[RTLearnedLocationManager _addVisit:locationOfInterest:handler:]_block_invoke
- ___65-[RTLearnedLocationManager _addVisit:locationOfInterest:handler:]_block_invoke_2
- ___65-[RTLearnedLocationManager _addVisit:locationOfInterest:handler:]_block_invoke_3
- ___65-[RTLearnedLocationManager _addVisit:locationOfInterest:handler:]_block_invoke_4
- ___65-[RTLearnedLocationManager _addVisit:locationOfInterest:handler:]_block_invoke_5
- ___65-[SMInitiatorService fetchSessionReceiptForSessionID:completion:]_block_invoke
- ___66-[SMInitiatorService _fetchSessionReceiptForSessionID:completion:]_block_invoke
- ___66-[SMInitiatorService _stopFrequentSingleShotFetchAllZonesActivity]_block_invoke
- ___67-[SMInitiatorService _startFrequentSingleShotFetchAllZonesActivity]_block_invoke
- ___67-[SMInitiatorService _startFrequentSingleShotFetchAllZonesActivity]_block_invoke_2
- ___67-[SMInitiatorService _startInfrequentPeriodicFetchAllZonesActivity]_block_invoke
- ___67-[SMInitiatorService _startInfrequentPeriodicFetchAllZonesActivity]_block_invoke_2
- ___70-[RTDuetKnowledgeStream enumerateEventsWithinDateInterval:usingBlock:]_block_invoke
- ___73-[RTDeviceMetricManager _addToHeapForReachability:endDate:dateIntervals:]_block_invoke
- ___73-[SMInitiatorService _fetchAllZonesFromContainerSynchronizerWithHandler:]_block_invoke
- ___74-[SMSessionReceiptZone checkSessionReceiptZoneAvailibilityWithCompletion:]_block_invoke
- ___78-[SMSessionReceiptZone fetchSessionReceiptRecordWithSessionID:qos:completion:]_block_invoke
- ___80-[RTLearnedLocationStore _fetchFinerGranularityInferredMapItemForVisit:handler:]_block_invoke
- ___83+[RTPlaceDataMetrics calculateMLFeatures:startDate:endDate:createBucketedFeatures:]_block_invoke
- ___84-[RTDeviceMetricManager getLongestDeviceLockedIntervalsWithTopN:dateInterval:error:]_block_invoke
- ___86-[RTDeviceMetricManager getLongestDeviceChargingIntervalsWithTopN:dateInterval:error:]_block_invoke
- ___86-[RTDeviceMetricManager getLongestWiFiConnectionIntervalsWithTopN:dateInterval:error:]_block_invoke
- ___88-[RTDeviceMetricManager getLongestStationaryMotionIntervalsWithTopN:dateInterval:error:]_block_invoke
- ___89-[RTDeviceMetricManager _getLongestStationaryMotionIntervalsWithTopN:dateInterval:error:]_block_invoke
- ___89-[RTDeviceMetricManager getLongestDeviceNotChargingIntervalsWithTopN:dateInterval:error:]_block_invoke
- ___block_descriptor_32_e64_B24?0"RTLearnedPlaceTypeInferencePlaceStats"8"NSDictionary"16l
- ___block_descriptor_40_e8_32bs_e20_v24?0Q8"NSError"16l
- ___block_descriptor_40_e8_32r_e33_v32?0"NSArray"8"NSError"16^B24l
- ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8l
- ___block_descriptor_48_e8_32r40r_e33_v32?0"NSArray"8"NSError"16^B24l
- ___block_descriptor_48_e8_32s40s_e41_B24?0"NSDateInterval"8"NSDictionary"16l
- ___block_descriptor_48_e8_32s_e20_v20?0"NSError"8B16l
- ___block_descriptor_48_e8_32s_e29_v24?0"RTVisit"8"NSError"16l
- ___block_descriptor_56_e8_32s40bs_e20_v20?0"NSError"8B16l
- ___block_descriptor_64_e8_32s40bs48w_e34_v24?0"NSDictionary"8"NSError"16l
- ___block_descriptor_64_e8_32s40r48r56r_e50_v32?0"RTPlaceInference"8"NSArray"16"NSError"24l
- ___block_descriptor_64_e8_32s40s48bs_e30_v24?0"CKRecord"8"NSError"16l
- ___block_descriptor_64_e8_32s40s48bs_e41_v28?0"SMSessionReceipt"8B16"NSError"20l
- ___block_descriptor_72_e8_32s40s48r56r64r_e30_v24?0"NSObject"8"NSError"16l
- ___swift_allocate_value_buffer
- ___swift_project_value_buffer
- __block_literal_global.1167
- __block_literal_global.176
- __block_literal_global.196
- __block_literal_global.198
- __block_literal_global.214
- __block_literal_global.217
- __block_literal_global.25
- __block_literal_global.28
- __block_literal_global.282
- __block_literal_global.295
- __block_literal_global.309
- __block_literal_global.354
- __block_literal_global.38
- __block_literal_global.411
- __block_literal_global.422
- __block_literal_global.458
- __block_literal_global.514
- __block_literal_global.517
- __block_literal_global.519
- __block_literal_global.533
- __block_literal_global.548
- __block_literal_global.55
- __block_literal_global.591
- __block_literal_global.603
- __block_literal_global.63
- __block_literal_global.667
- __block_literal_global.67
- __block_literal_global.944
- _dispatch_queue_create_with_target$V2
- _kRTDeviceMetricCharging
- _kRTDeviceMetricDataConnectivityCell
- _kRTDeviceMetricDataConnectivityNone
- _kRTDeviceMetricDataConnectivityWiFi
- _kRTDeviceMetricNotCharging
- _kRTDeviceMetricScreenLock
- _kRTDeviceMetricStationaryMotion
- _kSMSessionReceiptZoneName
- _objc_msgSend$_addToHeapForReachability:endDate:dateInterval:
- _objc_msgSend$_addToHeapForReachability:endDate:dateIntervals:
- _objc_msgSend$_addVisit:locationOfInterest:handler:
- _objc_msgSend$_convertDuetEvent:
- _objc_msgSend$_fetchAllZonesFromContainerSynchronizerWithHandler:
- _objc_msgSend$_fetchAllZonesFromContainerWithHandler:
- _objc_msgSend$_fetchFinerGranularityInferredMapItemForVisit:handler:
- _objc_msgSend$_fetchSessionReceiptForSessionID:completion:
- _objc_msgSend$_flippedDateIntervalsFromIntervals:originalDateInterval:error:
- _objc_msgSend$_getDeviceMetricsWithError:
- _objc_msgSend$_getFromHeapDateIntervalsForReachability:
- _objc_msgSend$_getLongestIntervalWithStreamType:topN:dateInterval:flipDateIntervals:error:
- _objc_msgSend$_getLongestStationaryMotionIntervalsWithTopN:dateInterval:error:
- _objc_msgSend$_initializeSessionReceiptZone
- _objc_msgSend$_onReachabilityChanged:
- _objc_msgSend$_startFrequentSingleShotFetchAllZonesActivity
- _objc_msgSend$_startInfrequentPeriodicFetchAllZonesActivity
- _objc_msgSend$_stopFrequentSingleShotFetchAllZonesActivity
- _objc_msgSend$_submitDeviceMetricsWithError:
- _objc_msgSend$_writeSessionReceiptRecord:completion:
- _objc_msgSend$addVisit:locationOfInterest:handler:
- _objc_msgSend$calculateMLFeatures:startDate:endDate:createBucketedFeatures:
- _objc_msgSend$checkSessionReceiptFieldsAvailibility:sessionID:
- _objc_msgSend$checkSessionReceiptZoneAvailibilityWithCompletion:
- _objc_msgSend$deleteAllEventsInEventStream:responseQueue:withCompletion:
- _objc_msgSend$deviceIsPluggedInStream
- _objc_msgSend$duetKnowledgeStore
- _objc_msgSend$duetKnowledgeStreamTypeToDuetEventStream:
- _objc_msgSend$endTime
- _objc_msgSend$enumerateEventsWithinDateInterval:usingBlock:
- _objc_msgSend$eventQueryWithPredicate:eventStreams:offset:limit:sortDescriptors:
- _objc_msgSend$executeQuery:completion:
- _objc_msgSend$executeQuery:responseQueue:withCompletion:
- _objc_msgSend$fetchAllZonesFromContainer:database:qos:withCompletion:
- _objc_msgSend$fetchAllZonesFromContainerInProgress
- _objc_msgSend$fetchAllZonesRetried
- _objc_msgSend$fetchSessionReceiptForSessionID:completion:
- _objc_msgSend$fetchSessionReceiptRecordWithSessionID:qos:completion:
- _objc_msgSend$fetchWithCompletionHandler:
- _objc_msgSend$frequentSingleShotFetchAllZonesInProgress
- _objc_msgSend$getDateIntervalFromDictionary:
- _objc_msgSend$getDictionaryFromDateInterval:
- _objc_msgSend$getMetricsDictionaryForMetricType:intervals:bins:
- _objc_msgSend$getReachabilityDefaultStringForTopN:reachability:
- _objc_msgSend$getStringForMetricType:topN:
- _objc_msgSend$initWithDefaultsManager:motionActivityManager:reachabilityManager:
- _objc_msgSend$initWithDistanceCalculator:learnedLocationStore:locationManager:mapServiceManager:visitManager:
- _objc_msgSend$initWithDuetKnowledgeStore:streamType:
- _objc_msgSend$initWithSessionID:sessionType:sessionStartTime:sessionEndTime:receiverHandles:safetyCacheReadStaus:
- _objc_msgSend$initWithStreamType:knowledgeStore:
- _objc_msgSend$keybagIsLockedStream
- _objc_msgSend$knowledgeStore
- _objc_msgSend$knowledgeStoreWithDirectReadOnlyAccess
- _objc_msgSend$motionStream
- _objc_msgSend$predicateForEventsWithStartInDateRangeFrom:to:
- _objc_msgSend$readStatus
- _objc_msgSend$saveObjects:responseQueue:withCompletion:
- _objc_msgSend$schoolEligibleSources
- _objc_msgSend$sessionReceiptZone
- _objc_msgSend$sessionReceiptZoneAvailable
- _objc_msgSend$sessionReceipts
- _objc_msgSend$setFetchAllZonesFromContainerInProgress:
- _objc_msgSend$setFetchAllZonesRetried:
- _objc_msgSend$setFrequentSingleShotFetchAllZonesInProgress:
- _objc_msgSend$setSessionReceiptZoneAvailable:
- _objc_msgSend$wifiConnectionStream
- _swift_arrayDestroy
- _swift_once
CStrings:
+ "#24@0:8@16"
+ "#RemoteControl,Initiator,sessionID:%@,%@,%@,from,%@,fromMe,%d, sourceDeviceId, %@ ,message,%{sensitive}@"
+ "#SafetyCache,%@,%@,received message from %@ could not be converted to SMMessage,messageDict,%{sensitive}@"
+ "#SafetyCache,Initiator,%@,%@, phoneCache location %lu, %{sensitive}@"
+ "#SafetyCache,Initiator,%@,%@, watchCache location %lu, %{sensitive}@"
+ "#SafetyCache,Initiator,%@,%@,received state sync req message for unmatched device identifier,%{sensitive}@"
+ "#SafetyCache,Initiator,%@,%@,sending initiator safety cache update to sessionID, %@, phoneCache, %{sensitive}@"
+ "#SafetyCache,Initiator,%@,%@,sending initiator safety cache update to sessionID, %@, watchCache, %{sensitive}@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,error with fetching location for workout event, %@, location, %{sensitive}@ error, %@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,from,%@,fromMe,%d,message,%{sensitive}@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,messageID:%@,scheduling Key Release for %@ with message %{sensitive}@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,non-active uploadCache updateCache completed %@, cache, %{sensitive}@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,not active device transition state, %{sensitive}@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,parking location is not valid %{sensitive}@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,saving starting location,lat,%{sensitive}.4f,lon,%{sensitive}.4f,hunc,%{sensitive}.1f"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,successfully decrypted safety cache data for,phone,%{sensitive}@,watch,%{sensitive}@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,update lock state %d with location %{sensitive}@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,updating parked car location %{sensitive}@"
+ "#SafetyCache,Initiator,sessionID:%@,%@,%@,uploadCache updateCache completed %@, cache, %{sensitive}@"
+ "#SafetyCache,Receiver,sessionID:%@,%@,%@,from,%@,fromMe,%d,message,%{sensitive}@"
+ "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,conversation:%@,associatedGUID:%@,messsage:%{sensitive}@"
+ "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,handles:%@,messsage:%{sensitive}@"
+ "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,messageGUID:%@,sendDate:%@,conversation:%@,associatedGUID:%@,message:%{sensitive}@"
+ "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,messsage:%{sensitive}@"
+ "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,received message from %@,fromMe,%d,message,%{sensitive}@"
+ "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,received message from %@,message,%{sensitive}@"
+ "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,received message from handle %@,fromMe,%d,message,%{sensitive}@"
+ "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,received session start message send result,guid,%@,success,%d,error,%@,message,%{sensitive}@"
+ "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,sending message to %@,messageDict:%{sensitive}@"
+ "%@, %@, Replacing business map item with reverse geocoded map item for home loi, identifier, %@, original place, %{sensitive}@, updated place, %{sensitive}@,"
+ "%@, %@, Success, YES, options, %@, location, %{sensitive}@, age, %.3f"
+ "%@, %@, adjusting place inference, %{sensitive}@, with fence radius, %f, from session configuration date, %@"
+ "%@, %@, after coalescing, finalIdToClassifications count, %lu"
+ "%@, %@, arrayOfSourcesOfIdToLearnedPlaces count %lu,"
+ "%@, %@, before coalescing, finalIdToClassifications count, %lu"
+ "%@, %@, before coalescing, finalIdToClassifications learnedPlace, %{sensitive}@"
+ "%@, %@, before coalescing, inferredToClosestSourceOfTruth count, %lu, error, %@"
+ "%@, %@, candidate place stat, %@"
+ "%@, %@, case 1.1, snapping inferred %@ to source of truth %@ which are %f meters distance apart, source of truth place, %{sensitive}@, inferred place, %{sensitive}@"
+ "%@, %@, case 1.2, skip snapping inferred %@ to source of truth %@ which are at %f meters distance apart due to placeType mismatch, source of truth place, %{sensitive}@, inferred place, %{sensitive}@"
+ "%@, %@, case 2.2, skipping inferred %@ because all source of truth %@ are not rotten, %{sensitive}@"
+ "%@, %@, couldn't create a placeholder place"
+ "%@, %@, created a placeholder place for maps postalAdress mapItem that was not associated to any existing place, %@"
+ "%@, %@, creating destination directory, %@"
+ "%@, %@, creating session config using handle, %@, destination location, %{sensitive}@"
+ "%@, %@, deduped place inference, %{sensitive}@"
+ "%@, %@, distance calculation error, %@"
+ "%@, %@, distance, %.3f, kSMSuggestionMinimimDistanceBetweenSourceAndDestination, %.3f, suggestion location, %{sensitive}@, destinationLocation, %{sensitive}@"
+ "%@, %@, distance, %@, latestLocationOfTheDevice, %{sensitive}@, learnedLOI.location.location, %{sensitive}@, error, %@"
+ "%@, %@, distance, %@, latestLocationOfTheDevice, %{sensitive}@, nploi.locationOfInterest.location, %{sensitive}@"
+ "%@, %@, distance, %@, latestLocationOfTheDevice, %{sensitive}@, nploisToHome.firstObject.locationOfInterest.location, %{sensitive}@, error, %@"
+ "%@, %@, distance, %@, latestLocationOfTheDevice, %{sensitive}@, routeSummary.destinationMapItem.location, %{sensitive}@"
+ "%@, %@, distance, %@, latestLocationOfTheDevice, %{sensitive}@, sessionConfiguration.destination.location, %{sensitive}@"
+ "%@, %@, distance, %@, suggestion.destinationLocation, %{sensitive}@, sessionConfiguration.destination.location, %{sensitive}@, error, %@"
+ "%@, %@, distanceBetweenCurrentLocationAndNavigationDestination, %.3f, kSMSuggestionProactiveNotificationTearDownDistanceCloseBy, %.3f, latestLocationOfTheDevice, %{sensitive}@, navigationDestination, %{sensitive}@"
+ "%@, %@, distanceBetweenDestinations, %.3f, kSMSuggestionProactiveNotificationTearDownDistanceFromNavigationDestination, %.3f, suggestion location, %{sensitive}@, navigationDestination, %{sensitive}@"
+ "%@, %@, error creating mapItem, %{sensitive}@, error, %@"
+ "%@, %@, error was issued due to wrong data source, %d, error, %@"
+ "%@, %@, failed to create directory, %@, error, %@"
+ "%@, %@, fallBackToClosestFinalClassifications count, %lu, error, %@"
+ "%@, %@, fallback learned place added, %{sensitive}@"
+ "%@, %@, fetched %lu learned location of interest from learned location store of type, %@"
+ "%@, %@, fetched learned LOI, %{sensitive}@, configuration, %{sensitive}@"
+ "%@, %@, fetched, %lu, pinnedPlaces, error, %@"
+ "%@, %@, fetching access points for fingerprint, %@, encountered an error, %@"
+ "%@, %@, fetching all fingerprints encountered an error, %@"
+ "%@, %@, fetching config from last session around currentDateMinusBufferTime, %@, timeIntervalWindow, %.3f, location, %{sensitive}@"
+ "%@, %@, fetching fingerprints for BluePOI encountered an error, %@"
+ "%@, %@, fetching fingerprints from settled points encountered an error, %@"
+ "%@, %@, fetching fingerprints from unsettled points encountered an error, %@"
+ "%@, %@, fetching selected fingerprints encountered an error, %@"
+ "%@, %@, final candidate session destination, %{sensitive}@"
+ "%@, %@, final classifications has home, %@"
+ "%@, %@, final learned place, %{sensitive}@"
+ "%@, %@, final list of classifications doesn't have home, trying to use fallback"
+ "%@, %@, final mostLikelySessionDestination, %{sensitive}@"
+ "%@, %@, finalSourceOfTruth, %{sensitive}@,"
+ "%@, %@, finalSourcesOfTruth count %lu,"
+ "%@, %@, fingerprint, %lu, identifier, %@, start, %@, settled state, %@, number of accessPoints, %lu, number of locations, %lu"
+ "%@, %@, inferred place, %{sensitive}@, closestSourceOfTruthLearnedPlace, %{sensitive}@, distance, %@"
+ "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, mlFeatures, %@, \n\nSkipping place inference in Ranker model because all the longest Biome stream bucketed values are <= 1. It means the stream doesn't exist or the values are less than 10 mins each."
+ "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, mlFeatures, %@, \n\nSkipping place inference in multi class model because all the longest biome stream bucketed values are <= 1. It means the stream doesn't exist or the values are less than 10 mins each."
+ "%@, %@, isUserInActiveSession, %@, recent session state, %{sensitive}@"
+ "%@, %@, launching message extension with configuration, %{sensitive}@"
+ "%@, %@, learned place type, %@, placeInference is null, learned LOI, %{sensitive}@"
+ "%@, %@, learned places count, %lu, error, %@"
+ "%@, %@, learnedPlace, %@"
+ "%@, %@, learnedPlaces have same UUID, %@, type matched, %@, shallBeFolded, %@, mapItem name of source1, %{sensitive}@, mapItem name of source 2, %{sensitive}@, distance between learnedPlaces, %.3f, threshold, %.3f, source1, %@, source2, %@, learnedPlaceFromSource1, %{sensitive}@, learnedPlaceFromSource2, %{sensitive}@, error, %@"
+ "%@, %@, learnedplaces have same UUID, %@, but mismatched type, learnedPlaceFromSource1, %{sensitive}@, learnedPlaceFromSource2, %{sensitive}@"
+ "%@, %@, location not found in learned LOI, %{sensitive}@"
+ "%@, %@, location, %{sensitive}@, fifth hour of today, %@, sunset date, %@"
+ "%@, %@, location, %{sensitive}@, skipped, distance, %@, min threshold, %.3f, max threshold, %.3f"
+ "%@, %@, location, %{sensitive}@, third hour of today, %@, sunrise date, %@"
+ "%@, %@, masquerading location, %{sensitive}@"
+ "%@, %@, masqueradingLocation, %{sensitive}@, error, %@"
+ "%@, %@, mldb token, %@"
+ "%@, %@, no corresponding LOI at this location, %{sensitive}@"
+ "%@, %@, nplois fetched count, %lu, nploisWithoutOnlyVehicleSource count, %lu, only high confidence, %@, nploisWithOnlyHighConfidenceAndWithoutOnlyVehicleSource, %lu, w.r.t the location, %{sensitive}@"
+ "%@, %@, nplois fetched count, %lu, onlyHighConfidence, %@, nplois with only high confidence count, %lu, w.r.t the location, %{sensitive}@"
+ "%@, %@, options, %@, session configurations count, %lu, fetched session configurations, %{sensitive}@, fetch error, %@"
+ "%@, %@, pinned place, %@"
+ "%@, %@, pinned places count, %lu, error, %@"
+ "%@, %@, pinnedPlace, %@, learnedPlace, %@, error, %@"
+ "%@, %@, place inference is nill or it doens't have map item, %@, destinationLearnedLOI, %{sensitive}@"
+ "%@, %@, place type, %@, location, %{sensitive}@"
+ "%@, %@, placeInference is nil, nploi, %{sensitive}@"
+ "%@, %@, posting notification for className, %@, query type, %@"
+ "%@, %@, received visit notification, %{sensitive}@"
+ "%@, %@, registering for pedometer data, startDate, %@, current LOI, %{sensitive}@"
+ "%@, %@, registering for pedometer notifications using startDate, %@, location, %{sensitive}@"
+ "%@, %@, sending finer granularity inferredMapItem, %@, for visit identifier, %@, to client, %@, error, %@"
+ "%@, %@, session configuration for mostLikelySessionDestination exists, %{sensitive}@"
+ "%@, %@, session configuration for place inference exists, %{sensitive}@"
+ "%@, %@, session location, %{sensitive}@, added, distance, %@, min threshold, %.3f, max threshold, %.3f"
+ "%@, %@, setting closest home as mostLikelySessionDestination, %{sensitive}@, distance to home, %.3f"
+ "%@, %@, setting first nploi with high confidence as mostLikelySessionDestination, %{sensitive}@"
+ "%@, %@, setting latestLocationOfTheDevice as fetchedLastLocation, %{sensitive}@"
+ "%@, %@, setting mlFeatures for placeStat, %{sensitive}@, ML Features, %@"
+ "%@, %@, setting navigation session destination as mostLikelySessionDestination, %{sensitive}@"
+ "%@, %@, skip posting notification for className, %@, query type, %@"
+ "%@, %@, source learnedPlace, %{sensitive}@, closest learned place, %{sensitive}@, distance, %@"
+ "%@, %@, source location is set to visit exit location, %{sensitive}@"
+ "%@, %@, sourceName, %@, count %lu,"
+ "%@, %@, sourceName, %@, learnedPlace, %{sensitive}@"
+ "%@, %@, sourceOfTruthName, %@, count %lu,"
+ "%@, %@, startDate, %@, kSMWalkingBoutMaxBreakTime, %.3f, kSMWalkingBoutMultiplierForLOIUncertainty, %.3f, previousPedometerData, %@, loi uncertainty, %.3f, multiplier, %.3f, sigma, %.3f, threshold, %.3f, pedometerData, %@, currentLOI, %{sensitive}@"
+ "%@, %@, states for pedometer data, currentLOI, %{sensitive}@, previousPedometerDataEndDate, %@,"
+ "%@, %@, success, %@, error, %@"
+ "%@, %@, time gap, %.3f, %.3f, earliest visit entry, %@, latest visit exit, %@, placeStat, %@"
+ "%@, %@, trigger type, %@, nploi, %{sensitive}@, sessionConfiguration count, %lu, kSMSuggestionOccasionalUserSessionConfigurationCount, %lu"
+ "%@, %@, trigger type, %@, nploi, %{sensitive}@, sessionConfiguration count, %lu, kSMSuggestionRegularUserSessionConfigurationCount, %lu"
+ "%@, %@, types, %@"
+ "%@, %@, unable to instantiate WiFi access point from dictionary, %@"
+ "%@, %@, unable to instantiate location from dictionary, %@"
+ "%@, %@, unable to instantiate reference location from dictionary, %@"
+ "%@, %@, using existing learned place, %@"
+ "%@, %@, visit cannot be nil"
+ "%@, %@, visit identifier cannot be nil"
+ "%@, %@, writen BluePOI queries file, %@"
+ "%@, _refreshMapItemsForLocationsOfInterestWithError, error, %@"
+ "%@, client, %@, state, %{sensitive}@, canDeviceModifyState, %@, error, %@"
+ "%@, client, %@, state, %{sensitive}@, error, %@"
+ "%@, configuration, %{sensitive}@"
+ "%@, configuration, %{sensitive}@, Trying to start session we already started, mark as success"
+ "%@, current state, %{sensitive}@"
+ "%@, error persisting place inference query, %{sensitive}@, error, %@"
+ "%@, fingerprints from settled points, total count, %lu, non zero AP count, %lu, filtered count, %lu, is time window fallback, %@."
+ "%@, fingerprints from unsettled points, total count, %lu, non zero AP count, %lu, filtered count, %lu, is time window fallback, %@."
+ "%@, input location, %{sensitive}@, idx, %ld"
+ "%@, invalid date range, queryStartDate, %@, queryEndDate, %@"
+ "%@, isRotten, %@, fetched %lu visits, most recent visit, %{sensitive}@, for place, %{sensitive}@, error, %@"
+ "%@, location, %{sensitive}@, startDate, %@, predictionWindow, %.2f, number of weeks in State Model, %{sensitive}f, number of weeks for prediction, %{sensitive}d, sparse mode, %@"
+ "%@, mapItem, %@, error, %@"
+ "%@, pipeline already setup, type, %@"
+ "%@, pipeline does not support realtime visits, %{sensitive}@"
+ "%@,%@,message:%{sensitive}@"
+ "%@,%@,message:%{sensitive}@,associatedGUID:%@,toConversation:%@"
+ "%@,%@,message:%{sensitive}@,messageGUID:%@,associatedGUID:%@,sendDate:%@,toConversation:%@"
+ "%@,%@,message:%{sensitive}@,toConversation:%@"
+ "%lu, sessionManagerState, %{sensitive}@"
+ "%s destinationLocation, %{sensitive}@"
+ "%s, Adding record, %{sensitive}@"
+ "%s, Error-Mismatch activeSessionDetails, %@, sessionManagerState: %{sensitive}@, current device thinks its active and try to perform cacheUpdate; have requested stateUpdate in order to become non-active. Stop cacheUpdate and cacheUpload."
+ "%s, NO, has not transitioned from idle status yet, origin location, %{sensitive}@, last location, %{sensitive}@"
+ "%s, Received event, %@, region, %{sensitive}@, clientIdentifier, %@"
+ "%s, Removing record, %{sensitive}@, Remaining records, %lu"
+ "%s, Session State is not SMSessionStateUnknown, bootstrap not needed, %{sensitive}@"
+ "%s, Watch dog fired, logging fault for prompt state, %{sensitive}@"
+ "%s, activeSessionDetails %@, deviceSessionManagerState, %{sensitive}@, isLocalStateInSync %{Bool}d"
+ "%s, attempting state transition from state, %{sensitive}@, to state, %{sensitive}@"
+ "%s, bootstrapping complete with state, %{sensitive}@, activeDevice %s"
+ "%s, bootstrapping not yet supported, called with configuration, %{sensitive}@"
+ "%s, complete current location fetch, location, %{sensitive}@, error, %@"
+ "%s, configuration, %{sensitive}@"
+ "%s, configuration, %{sensitive}@, monitoringForConfiguration, %@"
+ "%s, current configuration destination, %{sensitive}@, updated configuration destination, %{sensitive}@"
+ "%s, current location fetch failed, %@, current state, %{sensitive}@, error, %@"
+ "%s, current status, %@, session configuration, %{sensitive}@, durationSinceLastStatusChange, %.2f"
+ "%s, effectivePairedDevice, %@, effectivePairedDevice.nearby, %{Bool}d, sessionID, %@, lastSessionIDDuringMagnetBreak, %@, magnetBreakTimer, %{Bool}d, is state active state, %{Bool}d, state, %{sensitive}@"
+ "%s, error in ETA request, source, %{sensitive}@, destination, %{sensitive}@, transportType, %@, error, %d"
+ "%s, estimated location, %{sensitive}@, on date, %@"
+ "%s, expected monitoring state but got unexpected state, %{sensitive}@, activeDevice, %ld"
+ "%s, expected ready state but got unexpected state, %{sensitive}@, activeDevice, %ld"
+ "%s, expectedTravelTime, %f, source, %{sensitive}@, destination, %{sensitive}@, transport type, %@"
+ "%s, isActiveDevice, %{Bool}d, self.handoffRebootReconciliationState, %@,\n activeSessionDetails, %@,\n sessionManagerState, %{sensitive}@"
+ "%s, most recent state, %{sensitive}@, error, %@"
+ "%s, not initializing monitor for inactive state, %{sensitive}@, activeDevice, %d"
+ "%s, options, %@, currentLocation, %{sensitive}@, error, %@"
+ "%s, options, %{sensitive}@"
+ "%s, received state transition message from self, %{sensitive}@"
+ "%s, received state transition message with older state: %{sensitive}@, current: %{sensitive}@"
+ "%s, regionLocation, %{sensitive}@, regionIdentifier, %@, radius, %.3f, destinationType, %@"
+ "%s, registered geofence for region, %{sensitive}@"
+ "%s, request, %{sensitive}@, results count, %lu, error, %@"
+ "%s, session is not in Initializing or Ready, current state, %{sensitive}@"
+ "%s, session is not in Initializing, current state, %{sensitive}@"
+ "%s, sessionManagerState, %{sensitive}@"
+ "%s, source, %{sensitive}@, destination, %{sensitive}@, transportType, %@."
+ "%s, state transition from state, %{sensitive}@, to state, %{sensitive}@, calling _handleMagnetConnect to evaluate if a handoff is needed"
+ "%s, state transition from state, %{sensitive}@, to state, %{sensitive}@, invalid and not allowed for a handoff operation"
+ "%s, state transition originated by a state sync message, %{sensitive}@, to state, %{sensitive}@"
+ "%s, state, %{sensitive}@"
+ "%s, state, %{sensitive}@ only initialize triggers for remote session since active device %d"
+ "%s, state, %{sensitive}@, activeDevice, %d"
+ "%s, state, %{sensitive}@, initiating actions to become a non active device"
+ "%s, state, %{sensitive}@, initiating actions to become an active device"
+ "%s, stateSyncMessage contains invalid transition, stateSyncMessage.state, %{sensitive}@, current.state, %{sensitive}@"
+ "%s, transportType, %@, source, %{sensitive}@, destination, %{sensitive}@, departureDate, %@, distance, %.3f"
+ "%s, triggers muted with distance, %.2f, location, %{sensitive}@, destination, %{sensitive}@"
+ "%s, triggers unmuted with distance, %.2f, location, %{sensitive}@, destination, %{sensitive}@"
+ "%s,loaded sessionManagerStatus %{sensitive}@"
+ "%s,state,%{sensitive}@, disconnected,%{Bool}d"
+ "%{public}@, %{public}@, An error, %@, has occurred when fetching the finer granularity inferred map item for visit, %@"
+ "%{public}@, %{public}@, An error, %@, has occurred when fetching the inferred map item for visit, %@"
+ "%{public}@, %{public}@, An error, %@, has occurred when fetching visits between date, %@ and date, %@, ascending, %@"
+ "%{public}@, %{public}@, No last visit was found. We're unable to extract queries since none exist."
+ "%{public}@, %{public}@, Unable to instantiate the BluePOI map item provider an error has occured, %@"
+ "%{public}@, %{public}@, Unable to retrieve the last visit an error has occured, %@"
+ "%{public}@, %{public}@, fetched visits, %lu"
+ "%{public}@, %{public}@, fetching visits between start date, %@, end date, %@, ascending, %@"
+ "%{public}@, %{public}@, generating Blue POI Queries data"
+ "%{public}@, %{public}@, idx, %lu, visit, %@, query JSON dict, %@"
+ "%{public}@, %{public}@, retrieving Blue POI Queries json objects between start date, %@, end date, %@,"
+ "-[RTPlaceTypeClassifier _convertToIdToLearnedPlace:]"
+ "-[RTPlaceTypeClassifier _logExpertClassifications:sourceNames:]"
+ "-[RTPlaceTypeClassifier coalescePlacesFromExperts:]"
+ "-[RTPlaceTypeClassifier coalescePlacesFromSourcesOfTruth:sourceOfTruthNames:]"
+ "01:29:27"
+ "@68@0:8@16@24@32@40Q48B56@60"
+ "@68@0:8@16Q24@32B40@44^Q52^@60"
+ "@72@0:8@16@24Q32^B40^Q48^Q56^@64"
+ "B24@?0@\"RTPinnedPlace\"8@\"NSDictionary\"16"
+ "B24@?0@8^B16"
+ "BluePOIQueries"
+ "CollectionPlaceItem"
+ "ConstantMonitor"
+ "EventMonitor"
+ "Failed to reverse geocode for the location, %{sensitive}@, reverseGeocodedMapItem, %@, reverseGeocodeError, %@"
+ "FavoriteItem"
+ "Hindsight"
+ "HistoryItem"
+ "Hydrated mapItem, %{sensitive}@ session configuration, %{sensitive}@"
+ "Invalid JSON object for JSON serialization"
+ "Invalid parameter not satisfying: RTScenarioTriggerSettledStateIsValid(settledState)"
+ "Invalid parameter not satisfying: destinationLearnedPlaces"
+ "Invalid parameter not satisfying: expertClassifications (in %s:%d)"
+ "Invalid parameter not satisfying: learnedPlaces (in %s:%d)"
+ "Invalid parameter not satisfying: pinnedPlaces"
+ "Invalid parameter not satisfying: sourceLearnedPlaces"
+ "Invalid parameter not satisfying: sourceNames (in %s:%d)"
+ "Invalid parameter not satisfying: sourceOfTruthNames (in %s:%d)"
+ "LivTips"
+ "MLModelCreatorDefinedKey"
+ "Maps"
+ "Mar  8 2025"
+ "No last visit found."
+ "NoVisitFallback"
+ "QueryTypeCollectionPlaceItem"
+ "QueryTypeFavoriteItem"
+ "QueryTypeHistoryItem"
+ "RTBluePOIQuery"
+ "RTPlaceTypeClassifierExpertMaps"
+ "RTTripSegmentTransitionPreprocessor: fetchLearnedLocationOfInterestForVisitIdentifier fetched learnedLocation: %{sensitive}@"
+ "RTWiFiManagerNotificationLeechScanResults"
+ "Refer to NSJSONSerialization spec for valid JSON objects"
+ "SMSessionManager,%s,currentSessionID,%@,message,%{sensitive}@"
+ "SMWorkoutEventMO,%s,workoutEvent.location,%{sensitive}@,location fetch error,%@"
+ "T@\"NSArray\",C,N"
+ "T@\"NSArray\",C,N,VstoreSubscriptionTypes"
+ "T@\"NSArray\",R,N,G_accolades"
+ "T@\"RTLocation\",R,N,V_referenceLocation"
+ "TB,R,N,G_hasAnyAccolades"
+ "TB,R,N,V_selectedToLabel"
+ "_TtP8MapsSync21MapsSyncStoreDelegate_"
+ "_accolades"
+ "_addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:"
+ "_bluePOIQueryFromFingerprint:fingerprintIdx:referenceLocationArray:selected:endDate:totalAPsCount:error:"
+ "_convertPinnedPlacesToLearnedPlaces:error:"
+ "_convertToIdToLearnedPlace:"
+ "_extractBluePOIQueriesJSONDObjectBetweenStartDate:endDate:error:"
+ "_extractBluePOIQueriesJSONDObjectForVisit:bluePOIMapItemProvider:"
+ "_fetchAllFingerprintsBetweenStartDate:endDate:error:"
+ "_fetchCloudCurrentDeviceVisitsBetweenStartDate:endDate:ascending:error:"
+ "_fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:"
+ "_fetchMapItemWithMuid:predicate:handler:"
+ "_fetchPinnedPlacesWithKnownPlacesTypesAndError:"
+ "_getClosestLearnedPlacesAtDestination:source:threshold:error:"
+ "_hasAnyAccolades"
+ "_logExpertClassifications:sourceNames:"
+ "_mapItemsFromBluePOIQuery:startDate:endDate:error:"
+ "_notifyLeechScanResults:"
+ "_refreshMapItemsForLocationsOfInterestWithError:"
+ "_selectFingerprintsStartDate:endDate:maxQueryAttemps:isTimeWindowFallback:fingerprintsTotalOut:fingerprintsNonZeroAPsTotalOut:error:"
+ "_selectedToLabel"
+ "accolades"
+ "addVisit:finerGranularityInferredMapItem:locationOfInterest:handler:"
+ "allPlaceTypes"
+ "bluePOIQueries"
+ "classForMapsSyncClassName:"
+ "classNameForMapsSyncClass:"
+ "classNamesForMapsSyncClasses:"
+ "coalescePlacesFromSourcesOfTruth:sourceOfTruthNames:"
+ "dataWithBluePOIQueriesBetweenStartDate:endDate:error:"
+ "dateAsString"
+ "destinationLearnedPlaces"
+ "dictionaryOutForBluePOIReplayWithBluePOIQueries:"
+ "entryDateAsString"
+ "exitDateAsString"
+ "fetchFinerGranularityInferredMapItemWithVisitIdentifier:handler:"
+ "fetchFinerGranularityInferredMapItemWithVisitIdentifier:reply:"
+ "fetchMapItemWithMuid:predicate:handler:"
+ "getAllBluePOIQuerriesForStartDate:endDate:location:error:"
+ "getCLLocations"
+ "getFormattedDateString"
+ "hasAnyAccolades"
+ "identifier, %@, number of access points, %lu, number of locations, %lu, referenceLocation, %@, settled state, %@, selected to label, %@, date, %@"
+ "inferredPlaceTypes"
+ "initWithDistanceCalculator:learnedLocationStore:locationManager:mapServiceManager:visitManager:placeTypeClassifierMetricsCalculator:"
+ "initWithFirstJSONDictionary:"
+ "initWithIdentifier:accessPoints:locations:referenceLocation:settledState:selectedToLabel:date:"
+ "initWithLearnedLocationStore:mapsSupportManager:placeTypeClassifierMetricsCalculator:"
+ "initWithLearnedVisit:inferredMapItem:finerGranularityInferredMapItem:userPlaceType:userPlaceTypeSource:loiIdentifier:"
+ "injectVisit:finerGranularityInferredMapItem:locationOfInterest:reply:"
+ "json"
+ "mapsFavoritesPredicateWithHidden:includeNearbyTransit:"
+ "metadata"
+ "mldb_token"
+ "modelDescription"
+ "multiple mapItemMOs with the same identifier"
+ "nil predicate"
+ "nonInferredPlaceTypes"
+ "objectsPassingTest:"
+ "outputToDictionaryReadableDate:"
+ "outputToFirstJSONDictionary"
+ "pinnedPlaces"
+ "predictionFromFeatures:completionHandler:"
+ "predictionFromFeatures:options:completionHandler:"
+ "queryTypeForMapsSyncClass:"
+ "queryTypeForMapsSyncClassName:"
+ "range"
+ "requires a valid muid."
+ "requires an indentifier."
+ "routineBluePOIQueryPath"
+ "scans"
+ "scenarioTriggerSettledStateToString:"
+ "schoolGymEligibleSources"
+ "selectedToLabel"
+ "sending session state, %{sensitive}@, to client, %@"
+ "setStoreSubscriptionTypes:"
+ "sharedStore"
+ "sourceLearnedPlaces"
+ "start bootstrapping pipeline, %{sensitive}@, with locations since %@"
+ "storeChangeNotificationClasses"
+ "storeDidChangeWithTypes:"
+ "storeSubscriptionTypes"
+ "stringForQueryType:"
+ "stringFromVisitSource:"
+ "subscribe:"
+ "unexpected count of LOIs associated to mapItem, %{sensitive}@"
+ "used relabelInferredMapItem, %{sensitive}@, oldCandidate visit identifier, %@, oldCandidate map item identifier, %@, associate, %lu, error, %@"
+ "userSpecificPlaceTypeSourceToString:"
+ "userSpecificPlaceTypeToString:"
+ "v24@0:8@?<v@?@\"RTPlaceInference\"Q@\"NSArray\"@\"NSError\">16"
+ "v24@?0@\"<MLFeatureProvider>\"8@\"NSError\"16"
+ "v40@?0@\"RTPlaceInference\"8Q16@\"NSArray\"24@\"NSError\"32"
+ "v48@0:8@\"RTLocationOfInterestVisit\"16@\"RTInferredMapItem\"24@\"RTLocationOfInterest\"32@?<v@?@\"NSError\">40"
+ "visits count, %lu, local device visits count, %lu, place, %@"
+ "writeToFile:options:error:"
+ "zelkovaKoreaEnabled"
- "#RemoteControl,Initiator,sessionID:%@,%@,%@,from,%@,fromMe,%d, sourceDeviceId, %@ ,message,%@"
- "#SafetyCache,%@,%@,received message from %@ could not be converted to SMMessage,messageDict,%@"
- "#SafetyCache,Initiator,%@,%@, fetchAllZonesFromContainer,error:%@,fetchAllZonesRetried:%d, not retrying"
- "#SafetyCache,Initiator,%@,%@, fetchAllZonesFromContainer,error:%@,fetchAllZonesRetried:%d, retry once more"
- "#SafetyCache,Initiator,%@,%@, fetchAllZonesFromContainerInProgress:%d,Attempt fetching all zones"
- "#SafetyCache,Initiator,%@,%@, fetchAllZonesFromContainerInProgress:%d,early return"
- "#SafetyCache,Initiator,%@,%@, frequentSingleShotFetchAllZonesInProgress:%d,early return"
- "#SafetyCache,Initiator,%@,%@, phoneCache location %lu, %@"
- "#SafetyCache,Initiator,%@,%@, watchCache location %lu, %@"
- "#SafetyCache,Initiator,%@,%@,CloudKit (Fetch) Operation for initialize using PCS Identities, error %@"
- "#SafetyCache,Initiator,%@,%@,Failed to setup Session Receipt Zone with error %@"
- "#SafetyCache,Initiator,%@,%@,Session Receipt Zone fetch Successful"
- "#SafetyCache,Initiator,%@,%@,Session receipt zone does not exist. Setting up Session Receipt Zone"
- "#SafetyCache,Initiator,%@,%@,Setup Session Receipt Zone Successful"
- "#SafetyCache,Initiator,%@,%@,_fetchAllZonesFromContainerSynchronizerWithHandler returned error:%@, inProgress:%d"
- "#SafetyCache,Initiator,%@,%@,_fetchAllZonesFromContainerSynchronizerWithHandler, error:%@, inProgress:%d"
- "#SafetyCache,Initiator,%@,%@,failed to save zone with error %@"
- "#SafetyCache,Initiator,%@,%@,nil self"
- "#SafetyCache,Initiator,%@,%@,periodic fetch all zones xpc fired"
- "#SafetyCache,Initiator,%@,%@,received state sync req message for unmatched device identifier,%@"
- "#SafetyCache,Initiator,%@,%@,schedule periodic fetch all zones xpc activity,interval,%f,grace period,%f"
- "#SafetyCache,Initiator,%@,%@,schedule single shot fetch all zones xpc activity,interval,%f,grace period,%f"
- "#SafetyCache,Initiator,%@,%@,sending initiator safety cache update to sessionID, %@, phoneCache, %@"
- "#SafetyCache,Initiator,%@,%@,sending initiator safety cache update to sessionID, %@, watchCache, %@"
- "#SafetyCache,Initiator,%@,%@,single shot fetch all zones xpc fired"
- "#SafetyCache,Initiator,%@,%@,unregisterActivityWithIdentifier with error %@"
- "#SafetyCache,Initiator,%@,%@,zone saved successfully"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,Failed to fetch session receipt data"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,Fetched all session receipt data successfully"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,Fetched session receipt data"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,Missing fields in session receipt"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,No _sessionReceiptZone Object found"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,error with fetching location for workout event, %@, location, %@ error, %@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,fetching session receipt"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,from,%@,fromMe,%d,message,%@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,messageID:%@,scheduling Key Release for %@ with message %@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,non-active uploadCache updateCache completed %@, cache, %@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,parking location is not valid %@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,saving starting location,lat,%.4f,lon,%.4f,hunc,%.1f"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,session receipt fetch failed with error %@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,session receipt fetch success"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,successfully decrypted safety cache data for,phone,%@,watch,%@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,update lock state %d with location %@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,updating parked car location %@"
- "#SafetyCache,Initiator,sessionID:%@,%@,%@,uploadCache updateCache completed %@, cache, %@"
- "#SafetyCache,Receiver,sessionID:%@,%@,%@,from,%@,fromMe,%d,message,%@"
- "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,conversation:%@,associatedGUID:%@,messsage:%@"
- "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,handles:%@,messsage:%@"
- "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,messageGUID:%@,sendDate:%@,conversation:%@,associatedGUID:%@,message:%@"
- "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,messsage:%@"
- "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,received message from %@,fromMe,%d,message,%@"
- "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,received message from %@,message,%@"
- "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,received message from handle %@,fromMe,%d,message,%@"
- "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,received session start message send result,guid,%@,success,%d,error,%@,message,%@"
- "#SafetyCache,sessionID:%@,%@,%@,messageID:%@,sending message to %@,messageDict:%@"
- "%@, %@, %@, events, %lu, date interval, %@"
- "%@, %@, StreamType, %@, topN, %lu, startDate, %@, endDate, %@, fetchedDateIntervals count, %lu"
- "%@, %@, StreamType, %@, topN, %lu, startDate, %@, endDate, %@, fetchedMotionActivities count, %lu"
- "%@, %@, Success, YES, options, %@, location, %@, age, %.3f"
- "%@, %@, adjusting place inference, %@, with fence radius, %f, from session configuration date, %@"
- "%@, %@, case 1.1, snapping inferred %@ to meCard %@ which are %f meters distance apart, meCard place, %{sensitive}@, inferred place, %{sensitive}@"
- "%@, %@, case 1.2, skip snapping inferred %@ to meCard %@ which are at %f meters distance apart due to placeType mismatch, meCard place, %{sensitive}@, inferred place, %{sensitive}@"
- "%@, %@, case 2.2, skipping inferred %@ because all meCard %@ are not rotten, %{sensitive}@"
- "%@, %@, creating session config using handle, %@, destination location, %@"
- "%@, %@, deduped place inference, %@"
- "%@, %@, distance, %.3f, kSMSuggestionMinimimDistanceBetweenSourceAndDestination, %.3f, suggestion location, %@, destinationLocation, %@"
- "%@, %@, distance, %@, latestLocationOfTheDevice, %@, learnedLOI.location.location, %@, error, %@"
- "%@, %@, distance, %@, latestLocationOfTheDevice, %@, nploi.locationOfInterest.location, %@"
- "%@, %@, distance, %@, latestLocationOfTheDevice, %@, nploisToHome.firstObject.locationOfInterest.location, %@, error, %@"
- "%@, %@, distance, %@, latestLocationOfTheDevice, %@, routeSummary.destinationMapItem.location, %@"
- "%@, %@, distance, %@, latestLocationOfTheDevice, %@, sessionConfiguration.destination.location, %@"
- "%@, %@, distance, %@, suggestion.destinationLocation, %@, sessionConfiguration.destination.location, %@, error, %@"
- "%@, %@, distanceBetweenCurrentLocationAndNavigationDestination, %.3f, kSMSuggestionProactiveNotificationTearDownDistanceCloseBy, %.3f, latestLocationOfTheDevice, %@, navigationDestination, %@"
- "%@, %@, distanceBetweenDestinations, %.3f, kSMSuggestionProactiveNotificationTearDownDistanceFromNavigationDestination, %.3f, suggestion location, %@, navigationDestination, %@"
- "%@, %@, error creating mapItem, %@, error, %@"
- "%@, %@, fetched learned LOI, %@, configuration, %@"
- "%@, %@, fetching config from last session around currentDateMinusBufferTime, %@, timeIntervalWindow, %.3f, location, %@"
- "%@, %@, final candidate session destination, %@"
- "%@, %@, final mostLikelySessionDestination, %@"
- "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, mlFeatures, %@, \n\nSkipping place inference in Ranker model because all the longest duet stream bucketed values are <= 1. It means the stream doesn't exist or the values are less than 10 mins each."
- "%@, %@, inferring for placeType, %@, placeStat, %{sensitive}@, mlFeatures, %@, \n\nSkipping place inference in multi class model because all the longest duet stream bucketed values are <= 1. It means the stream doesn't exist or the values are less than 10 mins each."
- "%@, %@, interval, %@, "
- "%@, %@, isUserInActiveSession, %@, recent session state, %@"
- "%@, %@, launching message extension with configuration, %@"
- "%@, %@, learned place type, %@, placeInference is null, learned LOI, %@"
- "%@, %@, location not found in learned LOI, %@"
- "%@, %@, location, %@, fifth hour of today, %@, sunset date, %@"
- "%@, %@, location, %@, skipped, distance, %@, min threshold, %.3f, max threshold, %.3f"
- "%@, %@, location, %@, third hour of today, %@, sunrise date, %@"
- "%@, %@, masquerading location, %@"
- "%@, %@, masqueradingLocation, %@, error, %@"
- "%@, %@, no corresponding LOI at this location, %@"
- "%@, %@, nplois fetched count, %lu, nploisWithoutOnlyVehicleSource count, %lu, only high confidence, %@, nploisWithOnlyHighConfidenceAndWithoutOnlyVehicleSource, %lu, w.r.t the location, %@"
- "%@, %@, nplois fetched count, %lu, onlyHighConfidence, %@, nplois with only high confidence count, %lu, w.r.t the location, %@"
- "%@, %@, options, %@, session configurations count, %lu, fetched session configurations, %@, fetch error, %@"
- "%@, %@, output intervals count, %lu, "
- "%@, %@, output intervals, %@, "
- "%@, %@, place inference is nill or it doens't have map item, %@, destinationLearnedLOI, %@"
- "%@, %@, place type, %@, location, %@"
- "%@, %@, placeInference is nil, nploi, %@"
- "%@, %@, reachability state, %@"
- "%@, %@, received reachability notification, %@"
- "%@, %@, registering for pedometer data, startDate, %@, current LOI, %@"
- "%@, %@, registering for pedometer notifications using startDate, %@, location, %@"
- "%@, %@, session configuration for mostLikelySessionDestination exists, %@"
- "%@, %@, session configuration for place inference exists, %@"
- "%@, %@, session location, %@, added, distance, %@, min threshold, %.3f, max threshold, %.3f"
- "%@, %@, setting closest home as mostLikelySessionDestination, %@, distance to home, %.3f"
- "%@, %@, setting first nploi with high confidence as mostLikelySessionDestination, %@"
- "%@, %@, setting latestLocationOfTheDevice as fetchedLastLocation, %@"
- "%@, %@, setting mlFeatures for placeStat, %{sensitive}@, mlFeatures, %@, biomeMLFeatures, %@"
- "%@, %@, setting navigation session destination as mostLikelySessionDestination, %@"
- "%@, %@, source location is set to visit exit location, %@"
- "%@, %@, startDate, %@, kSMWalkingBoutMaxBreakTime, %.3f, kSMWalkingBoutMultiplierForLOIUncertainty, %.3f, previousPedometerData, %@, loi uncertainty, %.3f, multiplier, %.3f, sigma, %.3f, threshold, %.3f, pedometerData, %@, currentLOI, %@"
- "%@, %@, states for pedometer data, currentLOI, %@, previousPedometerDataEndDate, %@,"
- "%@, %@, submitting metrics of length, %lu"
- "%@, %@, trigger type, %@, nploi, %@, sessionConfiguration count, %lu, kSMSuggestionOccasionalUserSessionConfigurationCount, %lu"
- "%@, %@, trigger type, %@, nploi, %@, sessionConfiguration count, %lu, kSMSuggestionRegularUserSessionConfigurationCount, %lu"
- "%@, client, %@, state, %@, canDeviceModifyState, %@, error, %@"
- "%@, client, %@, state, %@, error, %@"
- "%@, configuration, %@"
- "%@, configuration, %@, Trying to start session we already started, mark as success"
- "%@, current state, %@"
- "%@, fetched %lu visits, most recent visit, %{sensitive}@, for place, %{sensitive}@, error, %@"
- "%@, fingerprint, %lu, identifier, %@, start, %@, settled state, %@, number of accessPoints, %lu, number of locations, %lu"
- "%@, fingerprints from settled points, total count, %lu, non zero AP count, %lu, filtered count, %lu"
- "%@, fingerprints from unsettled points, total count, %lu, non zero AP count, %lu, filtered count, %lu"
- "%@, input location, %@, idx, %ld"
- "%@, location, %{sensitive}@, startDate, %@, predictionWindow, %.2f, number of weeks in State Model, %{sensitive}f, number of weeks for prediciton, %{sensitive}d, sparse mode, %@"
- "%@, pipline already setup, type, %@"
- "%@, pipline does not support realtime visits, %{sensitive}@"
- "%@,%@,message:%@"
- "%@,%@,message:%@,associatedGUID:%@,toConversation:%@"
- "%@,%@,message:%@,messageGUID:%@,associatedGUID:%@,sendDate:%@,toConversation:%@"
- "%@,%@,message:%@,toConversation:%@"
- "%lu, sessionManagerState, %@"
- "%s destinationLocation, %@"
- "%s, Adding record, %@"
- "%s, Error-Mismatch activeSessionDetails, %@, sessionManagerState: %@, current device thinks its active and try to perform cacheUpdate; have requested stateUpdate in order to become non-active. Stop cacheUpdate and cacheUpload."
- "%s, NO, has not transitioned from idle status yet, origin location, %@, last location, %@"
- "%s, Received event, %@, region, %@, clientIdentifier, %@"
- "%s, Removing record, %@, Remaining records, %lu"
- "%s, Session State is not SMSessionStateUnknown, bootstrap not needed, %@"
- "%s, Watch dog fired, logging fault for prompt state, %@"
- "%s, activeSessionDetails %@, deviceSessionManagerState, %@, isLocalStateInSync %{Bool}d"
- "%s, attempting state transition from state, %@, to state, %@"
- "%s, bootstrapping complete with state, %@, activeDevice %s"
- "%s, bootstrapping not yet supported, called with configuration, %@"
- "%s, complete current location fetch, location, %@, error, %@"
- "%s, configuration, %@"
- "%s, configuration, %@, monitoringForConfiguration, %@"
- "%s, current configuration destination, %@, updated configuration destination, %@"
- "%s, current location fetch failed, %@, current state, %@, error, %@"
- "%s, current status, %@, session configuration, %@, durationSinceLastStatusChange, %.2f"
- "%s, effectivePairedDevice, %@, effectivePairedDevice.nearby, %{Bool}d, sessionID, %@, lastSessionIDDuringMagnetBreak, %@, magnetBreakTimer, %{Bool}d, is state active state, %{Bool}d, state, %@"
- "%s, error in ETA request, source, %@, destination, %@, transportType, %@, error, %d"
- "%s, estimated location, %@, on date, %@"
- "%s, expected monitoring state but got unexpected state, %@, activeDevice, %ld"
- "%s, expected ready state but got unexpected state, %@, activeDevice, %ld"
- "%s, expectedTravelTime, %f, source, %@, destination, %@, transport type, %@"
- "%s, isActiveDevice, %{Bool}d, self.handoffRebootReconciliationState, %@,\n activeSessionDetails, %@,\n sessionManagerState, %@"
- "%s, most recent state, %@, error, %@"
- "%s, not initializing monitor for inactive state, %@, activeDevice, %d"
- "%s, options, %@, currentLocation, %@, error, %@"
- "%s, received state transition message from self, %@"
- "%s, received state transition message with older state: %@, current: %@"
- "%s, regionLocation, %@, regionIdentifier, %@, radius, %.3f, destinationType, %@"
- "%s, registered geofence for region, %@"
- "%s, request, %@, results count, %lu, error, %@"
- "%s, session is not in Initializing or Ready, current state, %@"
- "%s, session is not in Initializing, current state, %@"
- "%s, sessionManagerState, %@"
- "%s, source, %@, destination, %@, transportType, %@."
- "%s, state transition from state, %@, to state, %@, calling _handleMagnetConnect to evaluate if a handoff is needed"
- "%s, state transition from state, %@, to state, %@, invalid and not allowed for a handoff operation"
- "%s, state transition originated by a state sync message, %@, to state, %@"
- "%s, state, %@"
- "%s, state, %@ only initialize triggers for remote session since active device %d"
- "%s, state, %@, activeDevice, %d"
- "%s, state, %@, initiating actions to become a non active device"
- "%s, state, %@, initiating actions to become an active device"
- "%s, stateSyncMessage contains invalid transition, stateSyncMessage.state, %@, current.state, %@"
- "%s, transportType, %@, source, %@, destination, %@, departureDate, %@, distance, %.3f"
- "%s, triggers muted with distance, %.2f, location, %@, destination, %@"
- "%s, triggers unmuted with distance, %.2f, location, %@, destination, %@"
- "%s,loaded sessionManagerStatus %@"
- "%s,state,%@, disconnected,%{Bool}d"
- "+[RTDuetKnowledgeStream duetKnowledgeStreamTypeToDuetEventStream:]"
- "+[RTDuetKnowledgeStream streamTypeToString:]"
- "-[RTBiomeManager _compareEvent1:event2:streamType:]"
- "-[RTDeviceMetricManager _addToHeapForReachability:endDate:dateInterval:]"
- "-[RTDeviceMetricManager _addToHeapForReachability:endDate:dateIntervals:]"
- "-[RTDeviceMetricManager _onDailyMetricsNotification:]"
- "-[RTDuetKnowledgeStream _convertDuetEvent:]"
- "01:34:22"
- "@\"<_DKKnowledgeQuerying>\""
- "@\"RTDuetKnowledgeStore\""
- "@\"SMSessionReceiptZone\""
- "@\"_DKEventStream\""
- "@\"_DKKnowledgeStore\""
- "@52@0:8q16Q24@32B40^@44"
- "B40@0:8Q16@24@32"
- "CoreRoutine.Inactivity.DeviceMetrics"
- "DUET"
- "Dec 18 2024"
- "Failed to reverse geocode for the location, %@, reverseGeocodedMapItem, %@, reverseGeocodeError, %@"
- "Fatal error"
- "FetchAllZoneFromContainer in progress"
- "Hydrated mapItem, %@ session configuration, %@"
- "Insufficient space allocated to copy string contents"
- "Invalid duet stream type, %ld"
- "Invalid duet stream type."
- "Invalid parameter not satisfying: RT_DUET_KNOWLEDGE_STREAM_STREAM_TYPE_VALID(streamType)"
- "Invalid parameter not satisfying: dateIntervals"
- "Invalid parameter not satisfying: dateIntervals (in %s:%d)"
- "Invalid parameter not satisfying: deviceMetricType"
- "Invalid parameter not satisfying: intervals"
- "Invalid parameter not satisfying: knowledgeStore"
- "Invalid parameter not satisfying: originalDateInterval"
- "Invalid parameter not satisfying: sessionReceipt"
- "Knowledge store query fetch error, %@"
- "Missing Fields of Session Receipt data"
- "Motion Activity"
- "Non-nil date interval required"
- "Non-nil date interval required."
- "Object type containing fetched duet results was not an NSArray."
- "RTDefaultsDeviceMetricCurrentReachability"
- "RTDefaultsDeviceMetricCurrentReachabilityStartDate"
- "RTDefaultsDeviceMetricTop%lu%@"
- "RTDefaultsInitiatorServicePeriodicFetchAllZonesDelay"
- "RTDefaultsInitiatorServicePeriodicFetchAllZonesGracePeriod"
- "RTDefaultsInitiatorServicePeriodicFetchAllZonesInterval"
- "RTDefaultsInitiatorServiceRecentCloudKitBootstrapSuccess"
- "RTDefaultsInitiatorServiceSingleShotFetchAllZonesGracePeriod"
- "RTDeviceMetricManager"
- "RTDuetKnowledgeStore"
- "RTDuetKnowledgeStore-requests"
- "RTDuetKnowledgeStoreDomain"
- "RTDuetKnowledgeStoreErrorDomain"
- "RTDuetKnowledgeStream"
- "RTTripSegmentTransitionPreprocessor: fetchLearnedLocationOfInterestForVisitIdentifier fetched learnedLocation: %@"
- "Replacing business map item with reverse geocoded map item for home loi, identifier, %@, original place, %{sensitive}@, updated place, %{sensitive}@,"
- "Returning nil _DKEventStream for RTDuetKnowledgeStreamStreamType. (in %s:%d)"
- "Returning nil for RTDuetKnowledgeStreamStreamType. (in %s:%d)"
- "SMInitiatorProtocol"
- "SMSessionManager,%s,currentSessionID,%@,message,%@"
- "SMSessionReceiptZone"
- "SMWorkoutEventMO,%s,workoutEvent.location,%@,location fetch error,%@"
- "SessionReceiptRecord"
- "SessionReceiptZone"
- "SuggestionsManager"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"<_DKKnowledgeQuerying>\",&,N,V_knowledgeStoreQuery"
- "T@\"NSMutableArray\",&,N,V_sessionReceipts"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_requestQueue"
- "T@\"RTDuetKnowledgeStore\",&,N,V_duetKnowledgeStore"
- "T@\"RTDuetKnowledgeStore\",&,N,V_knowledgeStore"
- "T@\"SMSessionReceiptZone\",&,N,V_sessionReceiptZone"
- "T@\"_DKEventStream\",&,N,V_eventStream"
- "T@\"_DKKnowledgeStore\",&,N,V_knowledgeStore"
- "TB,N,V_sessionReceiptZoneAvailable"
- "Tq,R,N,V_streamType"
- "Unexpectedly found nil while unwrapping an Optional value"
- "Unhandled stream type, %lu (in %s:%d)"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "_addToHeapForReachability:endDate:dateInterval:"
- "_addToHeapForReachability:endDate:dateIntervals:"
- "_addVisit:locationOfInterest:handler:"
- "_convertDuetEvent:"
- "_duetKnowledgeStore"
- "_eventStream"
- "_fetchAllZonesFromContainerSynchronizerWithHandler:"
- "_fetchAllZonesFromContainerWithHandler:"
- "_fetchFinerGranularityInferredMapItemForVisit:handler:"
- "_fetchSessionReceiptForSessionID:completion:"
- "_flippedDateIntervalsFromIntervals:originalDateInterval:error:"
- "_getDeviceMetricsWithError:"
- "_getFromHeapDateIntervalsForReachability:"
- "_getLongestIntervalWithStreamType:topN:dateInterval:flipDateIntervals:error:"
- "_getLongestStationaryMotionIntervalsWithTopN:dateInterval:error:"
- "_initializeSessionReceiptZone"
- "_knowledgeStore"
- "_knowledgeStoreQuery"
- "_onReachabilityChanged:"
- "_requestQueue"
- "_sessionReceiptZone"
- "_sessionReceiptZoneAvailable"
- "_sessionReceipts"
- "_startFrequentSingleShotFetchAllZonesActivity"
- "_startInfrequentPeriodicFetchAllZonesActivity"
- "_stopFrequentSingleShotFetchAllZonesActivity"
- "_streamType"
- "_submitDeviceMetricsWithError:"
- "_writeSessionReceiptRecord:completion:"
- "addVisit:locationOfInterest:handler:"
- "allReceiverHandlesEncrypted"
- "calculateMLFeatures:startDate:endDate:createBucketedFeatures:"
- "cell_connectivity"
- "checkSessionReceiptFieldsAvailibility:sessionID:"
- "checkSessionReceiptZoneAvailibilityWithCompletion:"
- "clearEventsFromStream:completion:"
- "client set stop bit while enumerating duet events, breaking out."
- "com.apple.SafetyMonitor"
- "com.apple.routined.cloudkit.frequentFetchAllZones"
- "com.apple.routined.cloudkit.infrequentFetchAllZones"
- "dateIntervals"
- "deleteAllEventsInEventStream:responseQueue:withCompletion:"
- "deviceIsPluggedInStream"
- "duetKnowledgeStore"
- "duetKnowledgeStreamTypeToDuetEventStream:"
- "endTime"
- "enumerateEventsWithinDateInterval:usingBlock:"
- "eventQueryWithPredicate:eventStreams:offset:limit:sortDescriptors:"
- "eventStream"
- "executeQuery:completion:"
- "executeQuery:responseQueue:withCompletion:"
- "fetchSessionReceiptForSessionID:completion:"
- "fetchSessionReceiptRecordWithSessionID:qos:completion:"
- "fetchWithCompletionHandler:"
- "getDateIntervalFromDictionary:"
- "getDictionaryFromDateInterval:"
- "getLongestDeviceChargingIntervalsWithTopN:dateInterval:error:"
- "getLongestDeviceLockedIntervalsWithTopN:dateInterval:error:"
- "getLongestDeviceNotChargingIntervalsWithTopN:dateInterval:error:"
- "getLongestStationaryMotionIntervalsWithTopN:dateInterval:error:"
- "getLongestWiFiConnectionIntervalsWithTopN:dateInterval:error:"
- "getMetricsDictionaryForMetricType:intervals:bins:"
- "getReachabilityDefaultStringForTopN:reachability:"
- "getStringForMetricType:topN:"
- "initWithDefaultsManager:motionActivityManager:reachabilityManager:"
- "initWithDistanceCalculator:learnedLocationStore:locationManager:mapServiceManager:visitManager:"
- "initWithDuetKnowledgeStore:streamType:"
- "initWithSessionID:sessionType:sessionStartTime:sessionEndTime:receiverHandles:safetyCacheReadStaus:"
- "initWithStreamType:knowledgeStore:"
- "injectVisit:locationOfInterest:reply:"
- "invalid Collection: less than 'count' elements in collection"
- "keybagIsLockedStream"
- "knowledgeStore"
- "knowledgeStoreQuery"
- "knowledgeStoreWithDirectReadOnlyAccess"
- "longest_interval_%lu_device_%@"
- "motionStream"
- "no_connectivity"
- "not_on_charge"
- "onReachabilityChanged:"
- "on_charge"
- "originalDateInterval"
- "predicateForEventsWithStartInDateRangeFrom:to:"
- "purge"
- "query fetch failed for knowledgeStoreWithDirectReadOnlyAccess"
- "readStatus"
- "received error while enumerating duet events, %@, breaking out."
- "requestQueue"
- "safetyCacheReadStatusEncrypted"
- "saveEvents:completion:"
- "saveObjects:responseQueue:withCompletion:"
- "schoolEligibleSources"
- "self is nil"
- "self.%@"
- "sending session state, %@, to client, %@"
- "sessionEndTimeEncrypted"
- "sessionReceiptZone"
- "sessionReceiptZoneAvailable"
- "sessionReceipts"
- "sessionStartTimeEncrypted"
- "sessionTypeEncrypted"
- "setDuetKnowledgeStore:"
- "setEventStream:"
- "setKnowledgeStore:"
- "setKnowledgeStoreQuery:"
- "setRequestQueue:"
- "setSessionReceiptZone:"
- "setSessionReceiptZoneAvailable:"
- "setSessionReceipts:"
- "start bootstraping pipeline, %{sensitive}@, with locations since %@"
- "static_motion"
- "stream, %@, name, %@"
- "streamType"
- "unexpected count of LOIs assocaited to mapItem, %{sensitive}@"
- "used relabelInferredMapItem, %{sensitive}@, oldCandidate visit identifier, %@, oldCandidate map item ientifier, %@, associate, %lu, error, %@"
- "v20@?0@\"NSError\"8B16"
- "v24@0:8@?<v@?@\"RTPlaceInference\"@\"NSArray\"@\"NSError\">16"
- "v24@?0@\"NSObject\"8@\"NSError\"16"
- "v28@?0@\"SMSessionReceipt\"8B16@\"NSError\"20"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSUUID\"@\"SMSessionReceipt\"@\"NSError\">24"
- "v32@?0@\"RTPlaceInference\"8@\"NSArray\"16@\"NSError\"24"
- "v40@0:8@\"RTLocationOfInterestVisit\"16@\"RTLocationOfInterest\"24@?<v@?@\"NSError\">32"
- "visits count, %lu, local device visits count, %lu"
- "wifiConnectionStream"
- "wifi_connectivity"
- "writeSessionReceiptRecord:completion:"

```
