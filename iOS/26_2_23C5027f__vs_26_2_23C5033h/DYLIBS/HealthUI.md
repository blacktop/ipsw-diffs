## HealthUI

> `/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI`

```diff

-6200.3.4.0.0
+6200.3.8.0.0
   __TEXT.__text: 0x3d84a4
   __TEXT.__auth_stubs: 0x5190
   __TEXT.__objc_methlist: 0x39e9c
   __TEXT.__const: 0x7584
-  __TEXT.__cstring: 0x24c17
+  __TEXT.__cstring: 0x24c37
   __TEXT.__oslogstring: 0x6c96
   __TEXT.__gcc_except_tab: 0x24d0
   __TEXT.__ustring: 0x56

   __DATA_CONST.__objc_selrefs: 0x18310
   __DATA_CONST.__objc_protorefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x1858
-  __DATA_CONST.__objc_arraydata: 0x2000
+  __DATA_CONST.__objc_arraydata: 0x2020
   __AUTH_CONST.__auth_got: 0x28d8
   __AUTH_CONST.__const: 0x5eb0
-  __AUTH_CONST.__cfstring: 0x1eb40
+  __AUTH_CONST.__cfstring: 0x1eba0
   __AUTH_CONST.__objc_const: 0x63cc0
   __AUTH_CONST.__objc_arrayobj: 0xf30
   __AUTH_CONST.__objc_intobj: 0x2940

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EA53127E-E316-39CC-802E-5C5729140033
+  UUID: C51B3CA6-BEFB-3C22-88CA-86308AE01BA8
   Functions: 24433
   Symbols:   65236
-  CStrings:  30171
+  CStrings:  30177
 
Symbols:
+ ___101-[HKRemoteCardioFitnessDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.302
+ ___101-[HKRemoteCardioFitnessDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.312
+ ___102-[HKDataMetadataSubsampleSection _submitCountStandHourQueryForSampleType:aggregateQueryFinishedBlock:]_block_invoke.314
+ ___102-[HKHorizontalSingleLineDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.323
+ ___102-[HKHorizontalTimePeriodDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.329
+ ___102-[HKQuantityDistributionDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.338
+ ___105-[HKClinicalSourceAuthorizationController _setAuthorizationStatuses:modes:shouldUpdateAnchor:completion:]_block_invoke.364
+ ___105-[HKHealthStore(HKUIAdditions) _primaryProfileFetchFirstAndLastNamesForInfoWrapper:meContact:completion:]_block_invoke.401
+ ___111-[HKJulianIndexedSevenDayQuantityDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.326
+ ___114-[HKDataMetadataSubsampleSection _exertionFixedValuesDisplayTypeController:unitController:healthStore:completion:]_block_invoke.322
+ ___123-[HKBloodPressureClassificationContext updateContextItemForDateInterval:overlayController:timeScope:resolution:completion:]_block_invoke.438
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.341
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.341.cold.1
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.343
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.343.cold.1
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.344
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.344.cold.1
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.345
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.345.cold.1
+ ___38-[HKSourceListDataSource fetchSources]_block_invoke.328
+ ___45-[HKMedicationAuthorizationController reload]_block_invoke.316
+ ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.329
+ ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.337
+ ___52-[HKSampleTypeUpdateController _createQueryForType:]_block_invoke.327
+ ___53-[HKDataMetadataOxygenSaturationSection queryForData]_block_invoke.330
+ ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.353
+ ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.358
+ ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke_2.359
+ ___56-[HKMedicalIDViewController _refreshMedicalIDInViewMode]_block_invoke.451
+ ___59-[HKDataMetadataViewController _fetchWorkoutRouteLocations]_block_invoke.370
+ ___60-[HKHealthConceptPickerViewController disallowButtonTapped:]_block_invoke.379
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke.367
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_2.370
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_3.371
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_4.372
+ ___60-[HKTinkerSharingGizmoPermissionController sendOptInRequest]_block_invoke.328
+ ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.340
+ ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.340.cold.1
+ ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.363
+ ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.363.cold.1
+ ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke.323
+ ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke.325
+ ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke_2.324
+ ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke_2.326
+ ___64-[HKObjectDataAccessViewController _refreshAppAuthorizationData]_block_invoke.339
+ ___65-[HKAudioExposureDevicesDataSource _makeDeviceQueryForDeviceType]_block_invoke.306
+ ___65-[HKClinicalSourceAuthorizationController _reloadWithCompletion:]_block_invoke.304
+ ___65-[HKLevelCategoryDataSource queriesForRequest:completionHandler:]_block_invoke.309
+ ___65-[HKObjectDataAccessViewController switchCellValueChanged:value:]_block_invoke.364
+ ___66-[HKSourceAuthorizationController _reloadTypeAuthorizationRecords]_block_invoke.363
+ ___66-[_HKIngestSettingsViewController fetchEnabledStatusForPeripheral]_block_invoke.302
+ ___67-[HKSampleTypeCountDataSource queriesForRequest:completionHandler:]_block_invoke.306
+ ___68-[HKActivitySummaryDataProvider _mainQueueFetchValueWithRetryCount:]_block_invoke.352
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.381
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.381.cold.1
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.401
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.401.cold.1
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.402
+ ___72-[HKHorizontalSingleLineDataSource queriesForRequest:completionHandler:]_block_invoke.309
+ ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.306
+ ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.306.cold.1
+ ___78-[HKLocationFetcher fetchLocationsFromWorkout:workoutActivity:samplesHandler:]_block_invoke.312
+ ___81-[HKJulianIndexedSevenDayQuantityDataSource queriesForRequest:completionHandler:]_block_invoke.310
+ ___85-[HKRouteMapGenerator snapshotWithSize:lineWidth:traitCollection:offsets:completion:]_block_invoke.327
+ ___86-[HKOrganDonationConnectionManager _genericJSONDataTaskWithRequest:completionHandler:]_block_invoke.455
+ ___88-[HKHorizontalTimePeriodDataSource _chartPointsWithDateIntervalsByValue:sourceTimeZone:]_block_invoke.317
+ ___88-[HKWorkoutRouteViewController _internalDebuggingOnly_fetchUnsmoothedRoutesFromDatabase]_block_invoke.501
+ ___89-[HKInsulinDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.424
+ ___92-[HKSleepChartDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.324
+ ___92-[HKSleepChartDataSource queriesForRequest:useCollectionQueryForSixMonth:completionHandler:]_block_invoke.309
+ ___92-[HKSleepChartDataSource queriesForRequest:useCollectionQueryForSixMonth:completionHandler:]_block_invoke.309.cold.1
+ ___92-[HKSleepChartDataSource queriesForRequest:useCollectionQueryForSixMonth:completionHandler:]_block_invoke.310
+ ___94-[HKQuantityTypeDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.404
+ ___95-[HKBloodPressureDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.349
+ ___95-[HKEmergencyCardNameAndPictureTableItem _checkOrRequestForCameraAccessIfNeededWithCompletion:]_block_invoke.364
+ ___95-[HKLevelCategoryDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.323
+ ___97-[HKBeatToBeatViewController initWithHRVSample:healthStore:displayTypeController:unitController:]_block_invoke.314
+ ___97-[HKSampleTypeCountDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.320
+ ___98-[HKHandwashingEventDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.425
+ ___98-[HKHealthStore(HKUIAdditions) _nonPrimaryProfileFetchFirstAndLastNamesForInfoWrapper:completion:]_block_invoke.405
+ ___98-[HKRecalibrateEstimatesPresentationController _requestAndConfigureHostViewController:completion:]_block_invoke.325
+ ___98-[HKTimePeriodSeriesDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.325
+ ___block_literal_global.303
+ ___block_literal_global.308
+ ___block_literal_global.309
+ ___block_literal_global.310
+ ___block_literal_global.313
+ ___block_literal_global.329
+ ___block_literal_global.330
+ ___block_literal_global.331
+ ___block_literal_global.333
+ ___block_literal_global.337
+ ___block_literal_global.343
+ ___block_literal_global.350
+ ___block_literal_global.366
+ ___block_literal_global.369
+ ___block_literal_global.370
+ ___block_literal_global.371
+ ___block_literal_global.372
+ ___block_literal_global.373
+ ___block_literal_global.376
+ ___block_literal_global.384
+ ___block_literal_global.386
+ ___block_literal_global.389
+ ___block_literal_global.390
+ ___block_literal_global.401
+ ___block_literal_global.405
+ ___block_literal_global.418
+ ___block_literal_global.426
+ ___block_literal_global.433
+ ___block_literal_global.436
+ ___block_literal_global.444
+ ___block_literal_global.460
+ ___block_literal_global.563
+ ___block_literal_global.565
+ ___block_literal_global.593
+ ___block_literal_global.601
+ ___block_literal_global.605
+ ___block_literal_global.618
+ ___block_literal_global.623
+ ___block_literal_global.628
+ ___block_literal_global.633
+ ___block_literal_global.638
+ ___block_literal_global.643
+ ___block_literal_global.648
+ ___block_literal_global.653
+ ___block_literal_global.658
+ ___block_literal_global.663
+ ___block_literal_global.668
+ ___block_literal_global.673
+ ___block_literal_global.688
+ ___block_literal_global.704
+ ___block_literal_global.709
+ ___block_literal_global.720
+ ___block_literal_global.722
+ ___block_literal_global.724
+ ___block_literal_global.726
+ ___block_literal_global.728
+ ___block_literal_global.730
+ ___block_literal_global.732
+ ___block_literal_global.734
+ ___block_literal_global.751
+ ___block_literal_global.756
+ ___block_literal_global.761
+ ___block_literal_global.766
+ ___block_literal_global.768
+ ___block_literal_global.773
+ ___block_literal_global.778
+ ___block_literal_global.783
+ ___block_literal_global.788
+ ___block_literal_global.798
+ ___block_literal_global.800
+ ___block_literal_global.802
+ ___block_literal_global.804
+ ___block_literal_global.806
+ ___block_literal_global.808
+ ___block_literal_global.810
+ ___block_literal_global.812
+ ___block_literal_global.814
+ ___block_literal_global.816
+ ___block_literal_global.818
+ ___block_literal_global.820
+ ___block_literal_global.822
+ ___block_literal_global.824
+ ___block_literal_global.826
+ ___block_literal_global.948
+ ___block_literal_global.960
+ _sharedInstance.numberFormatter.381
+ _sharedInstance.onceToken.382
- ___101-[HKRemoteCardioFitnessDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.293
- ___101-[HKRemoteCardioFitnessDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.303
- ___102-[HKDataMetadataSubsampleSection _submitCountStandHourQueryForSampleType:aggregateQueryFinishedBlock:]_block_invoke.305
- ___102-[HKHorizontalSingleLineDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.314
- ___102-[HKHorizontalTimePeriodDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.320
- ___102-[HKQuantityDistributionDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.329
- ___105-[HKClinicalSourceAuthorizationController _setAuthorizationStatuses:modes:shouldUpdateAnchor:completion:]_block_invoke.355
- ___105-[HKHealthStore(HKUIAdditions) _primaryProfileFetchFirstAndLastNamesForInfoWrapper:meContact:completion:]_block_invoke.392
- ___111-[HKJulianIndexedSevenDayQuantityDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.317
- ___114-[HKDataMetadataSubsampleSection _exertionFixedValuesDisplayTypeController:unitController:healthStore:completion:]_block_invoke.313
- ___123-[HKBloodPressureClassificationContext updateContextItemForDateInterval:overlayController:timeScope:resolution:completion:]_block_invoke.429
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.332
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.332.cold.1
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.334
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.334.cold.1
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.335
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.335.cold.1
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.336
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.336.cold.1
- ___38-[HKSourceListDataSource fetchSources]_block_invoke.319
- ___45-[HKMedicationAuthorizationController reload]_block_invoke.307
- ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.320
- ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.328
- ___52-[HKSampleTypeUpdateController _createQueryForType:]_block_invoke.318
- ___53-[HKDataMetadataOxygenSaturationSection queryForData]_block_invoke.321
- ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.344
- ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.349
- ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke_2.350
- ___56-[HKMedicalIDViewController _refreshMedicalIDInViewMode]_block_invoke.442
- ___59-[HKDataMetadataViewController _fetchWorkoutRouteLocations]_block_invoke.361
- ___60-[HKHealthConceptPickerViewController disallowButtonTapped:]_block_invoke.370
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke.358
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_2.361
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_3.362
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_4.363
- ___60-[HKTinkerSharingGizmoPermissionController sendOptInRequest]_block_invoke.319
- ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.331
- ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.331.cold.1
- ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.354
- ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.354.cold.1
- ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke.314
- ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke.316
- ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke_2.315
- ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke_2.317
- ___64-[HKObjectDataAccessViewController _refreshAppAuthorizationData]_block_invoke.330
- ___65-[HKAudioExposureDevicesDataSource _makeDeviceQueryForDeviceType]_block_invoke.297
- ___65-[HKClinicalSourceAuthorizationController _reloadWithCompletion:]_block_invoke.295
- ___65-[HKLevelCategoryDataSource queriesForRequest:completionHandler:]_block_invoke.300
- ___65-[HKObjectDataAccessViewController switchCellValueChanged:value:]_block_invoke.355
- ___66-[HKSourceAuthorizationController _reloadTypeAuthorizationRecords]_block_invoke.354
- ___66-[_HKIngestSettingsViewController fetchEnabledStatusForPeripheral]_block_invoke.293
- ___67-[HKSampleTypeCountDataSource queriesForRequest:completionHandler:]_block_invoke.297
- ___68-[HKActivitySummaryDataProvider _mainQueueFetchValueWithRetryCount:]_block_invoke.343
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.372
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.372.cold.1
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.392
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.392.cold.1
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.393
- ___72-[HKHorizontalSingleLineDataSource queriesForRequest:completionHandler:]_block_invoke.300
- ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.297
- ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.297.cold.1
- ___78-[HKLocationFetcher fetchLocationsFromWorkout:workoutActivity:samplesHandler:]_block_invoke.303
- ___81-[HKJulianIndexedSevenDayQuantityDataSource queriesForRequest:completionHandler:]_block_invoke.301
- ___85-[HKRouteMapGenerator snapshotWithSize:lineWidth:traitCollection:offsets:completion:]_block_invoke.318
- ___86-[HKOrganDonationConnectionManager _genericJSONDataTaskWithRequest:completionHandler:]_block_invoke.446
- ___88-[HKHorizontalTimePeriodDataSource _chartPointsWithDateIntervalsByValue:sourceTimeZone:]_block_invoke.308
- ___88-[HKWorkoutRouteViewController _internalDebuggingOnly_fetchUnsmoothedRoutesFromDatabase]_block_invoke.492
- ___89-[HKInsulinDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.415
- ___92-[HKSleepChartDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.315
- ___92-[HKSleepChartDataSource queriesForRequest:useCollectionQueryForSixMonth:completionHandler:]_block_invoke.300
- ___92-[HKSleepChartDataSource queriesForRequest:useCollectionQueryForSixMonth:completionHandler:]_block_invoke.300.cold.1
- ___92-[HKSleepChartDataSource queriesForRequest:useCollectionQueryForSixMonth:completionHandler:]_block_invoke.301
- ___94-[HKQuantityTypeDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.395
- ___95-[HKBloodPressureDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.340
- ___95-[HKEmergencyCardNameAndPictureTableItem _checkOrRequestForCameraAccessIfNeededWithCompletion:]_block_invoke.355
- ___95-[HKLevelCategoryDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.314
- ___97-[HKBeatToBeatViewController initWithHRVSample:healthStore:displayTypeController:unitController:]_block_invoke.305
- ___97-[HKSampleTypeCountDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.311
- ___98-[HKHandwashingEventDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.416
- ___98-[HKHealthStore(HKUIAdditions) _nonPrimaryProfileFetchFirstAndLastNamesForInfoWrapper:completion:]_block_invoke.396
- ___98-[HKRecalibrateEstimatesPresentationController _requestAndConfigureHostViewController:completion:]_block_invoke.316
- ___98-[HKTimePeriodSeriesDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.316
- ___block_literal_global.294
- ___block_literal_global.299
- ___block_literal_global.300
- ___block_literal_global.301
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.312
- ___block_literal_global.314
- ___block_literal_global.322
- ___block_literal_global.324
- ___block_literal_global.328
- ___block_literal_global.334
- ___block_literal_global.340
- ___block_literal_global.351
- ___block_literal_global.356
- ___block_literal_global.357
- ___block_literal_global.359
- ___block_literal_global.361
- ___block_literal_global.362
- ___block_literal_global.363
- ___block_literal_global.364
- ___block_literal_global.375
- ___block_literal_global.378
- ___block_literal_global.380
- ___block_literal_global.381
- ___block_literal_global.408
- ___block_literal_global.409
- ___block_literal_global.424
- ___block_literal_global.427
- ___block_literal_global.435
- ___block_literal_global.451
- ___block_literal_global.547
- ___block_literal_global.554
- ___block_literal_global.584
- ___block_literal_global.587
- ___block_literal_global.592
- ___block_literal_global.609
- ___block_literal_global.614
- ___block_literal_global.619
- ___block_literal_global.624
- ___block_literal_global.629
- ___block_literal_global.634
- ___block_literal_global.639
- ___block_literal_global.644
- ___block_literal_global.649
- ___block_literal_global.654
- ___block_literal_global.659
- ___block_literal_global.664
- ___block_literal_global.679
- ___block_literal_global.695
- ___block_literal_global.700
- ___block_literal_global.711
- ___block_literal_global.713
- ___block_literal_global.715
- ___block_literal_global.717
- ___block_literal_global.719
- ___block_literal_global.721
- ___block_literal_global.723
- ___block_literal_global.725
- ___block_literal_global.742
- ___block_literal_global.747
- ___block_literal_global.752
- ___block_literal_global.757
- ___block_literal_global.759
- ___block_literal_global.764
- ___block_literal_global.769
- ___block_literal_global.774
- ___block_literal_global.779
- ___block_literal_global.784
- ___block_literal_global.789
- ___block_literal_global.791
- ___block_literal_global.795
- ___block_literal_global.797
- ___block_literal_global.799
- ___block_literal_global.801
- ___block_literal_global.803
- ___block_literal_global.805
- ___block_literal_global.807
- ___block_literal_global.809
- ___block_literal_global.811
- ___block_literal_global.813
- ___block_literal_global.815
- ___block_literal_global.817
- ___block_literal_global.939
- ___block_literal_global.951
- _sharedInstance.numberFormatter.372
- _sharedInstance.onceToken.373
CStrings:
+ "Spirit"
+ "dyaco"
+ "spirit"

```
