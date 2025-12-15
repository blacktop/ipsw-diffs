## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1070.0.3.0.0
-  __TEXT.__text: 0x6165a8
+1071.0.1.0.0
+  __TEXT.__text: 0x6169dc
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x315d0
+  __TEXT.__objc_methlist: 0x315e8
   __TEXT.__const: 0x49b0
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x78476
+  __TEXT.__oslogstring: 0x78544
   __TEXT.__cstring: 0x45fec
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18

   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x28e9c
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xdde8
+  __TEXT.__unwind_info: 0xdde0
   __TEXT.__eh_frame: 0x390
   __TEXT.__objc_classname: 0x58d0
-  __TEXT.__objc_methname: 0x933af
-  __TEXT.__objc_methtype: 0xd1a0
-  __TEXT.__objc_stubs: 0x568e0
+  __TEXT.__objc_methname: 0x933e9
+  __TEXT.__objc_methtype: 0xd1af
+  __TEXT.__objc_stubs: 0x56920
   __DATA_CONST.__got: 0x3150
   __DATA_CONST.__const: 0xf6c0
   __DATA_CONST.__objc_classlist: 0x1548
   __DATA_CONST.__objc_catlist: 0x3a8
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19828
+  __DATA_CONST.__objc_selrefs: 0x19838
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x1190
   __DATA_CONST.__objc_arraydata: 0x2b88

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 109BFF4A-F0F5-3756-A710-80269D2AE4C8
-  Functions: 20331
+  UUID: 6F553B4E-572F-38A5-B46E-CF745DDF5173
+  Functions: 20330
   Symbols:   65640
-  CStrings:  40616
+  CStrings:  40623
 
Symbols:
+ -[RTWiFiManager_MobileWiFi _ensureDevicesAvailable]
+ -[RTWiFiManager_MobileWiFi _executeScanWithRequest:callback:]
+ ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.412
+ ___25-[RTDaemonClient restore]_block_invoke.745
+ ___25-[RTDaemonClient restore]_block_invoke.748
+ ___27-[RTLifeCycleManager _exit]_block_invoke.724
+ ___27-[RTLifeCycleManager _exit]_block_invoke.730
+ ___27-[RTLifeCycleManager _exit]_block_invoke.732
+ ___27-[RTLifeCycleManager _exit]_block_invoke_2.731
+ ___28-[RTHealthKitManager _setup]_block_invoke.625
+ ___28-[RTLifeCycleManager _start]_block_invoke.709
+ ___28-[RTLifeCycleManager _start]_block_invoke.715
+ ___28-[RTLifeCycleManager _start]_block_invoke.721
+ ___41-[RTAssetManager _downloadAsset:handler:]_block_invoke.362
+ ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.726
+ ___48-[RTFeatureExtractor _getHomeKitHomesWithError:]_block_invoke.449
+ ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.772
+ ___52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.689
+ ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.670
+ ___57-[SMSessionMetricManager _gatherSessionDestinationStats:]_block_invoke.681
+ ___58-[RTFeatureExtractor _getVisitsWithDateInterval:outError:]_block_invoke.417
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.492
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.499
+ ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.503
+ ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.838
+ ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.584
+ ___61-[RTWiFiManager_MobileWiFi _executeScanWithRequest:callback:]_block_invoke
+ ___62-[RTDaemonClientInternal connection:handleInvocation:isReply:]_block_invoke.494
+ ___63-[RTFeatureExtractor _getTransitionsWithDateInterval:outError:]_block_invoke.419
+ ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.689
+ ___66-[RTFeatureExtractor _getCalendarEventsWithDateInterval:outError:]_block_invoke.438
+ ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.737
+ ___68-[RTFeatureExtractor _getMapsViewedPlacesWithDateInterval:outError:]_block_invoke.443
+ ___68-[RTFeatureExtractor _getMotionActivitiesWithDateInterval:outError:]_block_invoke.445
+ ___69-[RTDaemonClient remoteStatusRegistrar:didReceiveRemoteStatus:error:]_block_invoke.773
+ ___69-[RTFeatureExtractor _getLocationHistoriesWithDateInterval:outError:]_block_invoke.436
+ ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.764
+ ___71-[RTFeatureExtractor _getLocationsOfInterestWithDateInterval:outError:]_block_invoke.434
+ ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.515
+ ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.749
+ ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.557
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.466
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.470
+ ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.481
+ ___76-[RTAssetManager initWithDefaultsManager:assetProcessor:xpcActivityManager:]_block_invoke.301
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.732
+ ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.733
+ ___77-[RTFeatureExtractor _getMapsHistoricalNavigationsWithDateInterval:outError:]_block_invoke.441
+ ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.611
+ ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.768
+ ___79-[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]_block_invoke.801
+ ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.721
+ ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.740
+ ___83-[RTDaemonClient predictedContextRegistrar:didReceivePredictedContextResult:error:]_block_invoke.812
+ ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.676
+ ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.421
+ ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.425
+ ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.427
+ ___block_literal_global.1389
+ ___block_literal_global.361
+ ___block_literal_global.610
+ ___block_literal_global.613
+ ___block_literal_global.616
+ ___block_literal_global.647
+ ___block_literal_global.691
+ ___block_literal_global.712
+ ___block_literal_global.717
+ ___block_literal_global.720
+ ___block_literal_global.723
+ ___block_literal_global.735
+ ___block_literal_global.742
+ ___block_literal_global.747
+ ___block_literal_global.750
+ ___block_literal_global.979
+ _objc_msgSend$_ensureDevicesAvailable
+ _objc_msgSend$_executeScanWithRequest:callback:
- ___103-[SMSuggestionsManager _registerForPedometerNotificationsForLearnedLocationOfInterest:startDate:error:]_block_invoke.421
- ___25-[RTDaemonClient restore]_block_invoke.754
- ___25-[RTDaemonClient restore]_block_invoke.757
- ___27-[RTLifeCycleManager _exit]_block_invoke.739
- ___27-[RTLifeCycleManager _exit]_block_invoke.741
- ___27-[RTLifeCycleManager _exit]_block_invoke.742
- ___27-[RTLifeCycleManager _exit]_block_invoke_2.740
- ___28-[RTHealthKitManager _setup]_block_invoke.634
- ___28-[RTLifeCycleManager _start]_block_invoke.724
- ___28-[RTLifeCycleManager _start]_block_invoke.727
- ___28-[RTLifeCycleManager _start]_block_invoke.730
- ___41-[RTAssetManager _downloadAsset:handler:]_block_invoke.371
- ___41-[RTWiFiManager_MobileWiFi _scheduleScan]_block_invoke
- ___43-[RTDaemonClientInternal setXpcConnection:]_block_invoke.735
- ___47-[RTWiFiManager_MobileWiFi _scheduleActiveScan]_block_invoke
- ___48-[RTFeatureExtractor _getHomeKitHomesWithError:]_block_invoke.458
- ___50-[RTDaemonClient removeVisitWithIdentifier:reply:]_block_invoke.781
- ___50-[RTWiFiManager_MobileWiFi _scheduleScanWithCache]_block_invoke
- ___52-[SMSessionMetricManager onSessionStartedWithState:]_block_invoke.698
- ___54-[RTDaemonClient connection:handleInvocation:isReply:]_block_invoke.679
- ___54-[RTWiFiManager_MobileWiFi _scheduleScanWithChannels:]_block_invoke
- ___57-[SMSessionMetricManager _gatherSessionDestinationStats:]_block_invoke.690
- ___58-[RTFeatureExtractor _getVisitsWithDateInterval:outError:]_block_invoke.426
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.501
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.508
- ___58-[SMSuggestionsManager _suppressSuggestion:context:error:]_block_invoke.512
- ___59-[RTHealthKitManager _dumpWorkoutClusterAtDir:stats:error:]_block_invoke.847
- ___59-[SMSuggestionsManager _isFirstTimeUserOfZelkovaWithError:]_block_invoke.593
- ___62-[RTDaemonClientInternal connection:handleInvocation:isReply:]_block_invoke.503
- ___63-[RTFeatureExtractor _getTransitionsWithDateInterval:outError:]_block_invoke.428
- ___64-[RTDaemonClient fetchPredictedLocationsOfInterestOnDate:reply:]_block_invoke.698
- ___66-[RTFeatureExtractor _getCalendarEventsWithDateInterval:outError:]_block_invoke.447
- ___67-[RTDaemonClient fetchPredictedExitDatesFromLocation:onDate:reply:]_block_invoke.746
- ___68-[RTFeatureExtractor _getMapsViewedPlacesWithDateInterval:outError:]_block_invoke.452
- ___68-[RTFeatureExtractor _getMotionActivitiesWithDateInterval:outError:]_block_invoke.454
- ___69-[RTDaemonClient remoteStatusRegistrar:didReceiveRemoteStatus:error:]_block_invoke.782
- ___69-[RTFeatureExtractor _getLocationHistoriesWithDateInterval:outError:]_block_invoke.445
- ___70-[RTDaemonClient vehicleEventRegistrar:didReceiveVehicleEvents:error:]_block_invoke.773
- ___71-[RTFeatureExtractor _getLocationsOfInterestWithDateInterval:outError:]_block_invoke.443
- ___71-[SMSuggestionsManager _fetchSuggestedSessionConfigurationWithHandler:]_block_invoke.524
- ___72-[RTDaemonClientInternal fetchFusionCandidatesForVisitIdentifier:reply:]_block_invoke.758
- ___72-[SMSuggestionsManager _didInteractInPastWithHandle:timeInterval:error:]_block_invoke.566
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.475
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.479
- ___72-[SMSuggestionsManager _showSuggestionsDetectionUIWithSuggestion:error:]_block_invoke.490
- ___76-[RTAssetManager initWithDefaultsManager:assetProcessor:xpcActivityManager:]_block_invoke.310
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.741
- ___76-[RTDaemonClient scenarioTriggerRegistrar:didReceiveScenarioTriggers:error:]_block_invoke.742
- ___77-[RTFeatureExtractor _getMapsHistoricalNavigationsWithDateInterval:outError:]_block_invoke.450
- ___77-[SMSuggestionsManager _getNPLOIsWithOnlyHighConfidence:location:date:error:]_block_invoke.620
- ___79-[RTDaemonClient addLocationOfInterestOfType:mapItemStorage:customLabel:reply:]_block_invoke.777
- ___79-[RTDaemonClient peopleDiscoveryRegistrar:didReceivePeopleDensityUpdate:error:]_block_invoke.810
- ___80-[RTDaemonClient fetchLocationsOfInterestVisitedBetweenStartDate:endDate:reply:]_block_invoke.730
- ___82-[RTDaemonClient fetchPredictedLocationsOfInterestBetweenStartDate:endDate:reply:]_block_invoke.749
- ___83-[RTDaemonClient predictedContextRegistrar:didReceivePredictedContextResult:error:]_block_invoke.821
- ___97-[RTDaemonClient fetchNextPredictedLocationsOfInterestFromLocation:startDate:timeInterval:reply:]_block_invoke.685
- ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.430
- ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.434
- ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.436
- ___block_literal_global.1398
- ___block_literal_global.370
- ___block_literal_global.622
- ___block_literal_global.625
- ___block_literal_global.656
- ___block_literal_global.700
- ___block_literal_global.721
- ___block_literal_global.726
- ___block_literal_global.729
- ___block_literal_global.732
- ___block_literal_global.744
- ___block_literal_global.748
- ___block_literal_global.751
- ___block_literal_global.756
- ___block_literal_global.759
- ___block_literal_global.988
CStrings:
+ "%@, WiFi scan request, %@"
+ "%@, device, %@, WiFiDeviceClientScanAsync called"
+ "%@, failed to request scan, number of devices, %lu"
+ "%@, no devices available, attempting to recreate WiFi manager connection"
+ "%{public}@, %{public}@, fetched access point count, %lu, fingerprint, %{sensitive}@, end date, %{private}@, error, %{public}@"
+ "06:31:48"
+ "Dec  5 2025"
+ "_ensureDevicesAvailable"
+ "_executeScanWithRequest:callback:"
+ "v32@0:8@16^?24"
- "%{public}@, %{public}@, Fetched access points for fingerprint, %{sensitive}@, end date, %{private}@, error, %{public}@"
- "23:57:09"
- "Nov  8 2025"

```
