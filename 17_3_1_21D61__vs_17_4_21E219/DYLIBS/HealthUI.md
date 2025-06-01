## HealthUI

> `/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x344a44
-  __TEXT.__auth_stubs: 0x4180
-  __TEXT.__objc_methlist: 0x2e818
-  __TEXT.__const: 0x45b4
-  __TEXT.__cstring: 0x1f017
-  __TEXT.__oslogstring: 0x46f2
+4146.4.18.0.0
+  __TEXT.__text: 0x347364
+  __TEXT.__auth_stubs: 0x41a0
+  __TEXT.__objc_methlist: 0x2e810
+  __TEXT.__const: 0x4594
+  __TEXT.__cstring: 0x1f437
+  __TEXT.__oslogstring: 0x4776
   __TEXT.__ustring: 0x5a
   __TEXT.__gcc_except_tab: 0x1954
   __TEXT.__dlopen_cstrs: 0x411
   __TEXT.__constg_swiftt: 0x21c0
-  __TEXT.__swift5_typeref: 0x1c50
+  __TEXT.__swift5_typeref: 0x1c38
   __TEXT.__swift5_reflstr: 0x15fe
   __TEXT.__swift5_fieldmd: 0x1374
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x4a0
   __TEXT.__swift5_proto: 0x164
   __TEXT.__swift5_types: 0x194
-  __TEXT.__swift5_capture: 0x568
+  __TEXT.__swift5_capture: 0x53c
   __TEXT.__swift5_protos: 0x20
   __TEXT.__objc_const_ax: 0x4104
-  __TEXT.__unwind_info: 0xd158
-  __TEXT.__eh_frame: 0xdf0
+  __TEXT.__unwind_info: 0xd114
+  __TEXT.__eh_frame: 0xdb8
   __TEXT.__objc_classname: 0x8718
-  __TEXT.__objc_methname: 0x761f9
+  __TEXT.__objc_methname: 0x76231
   __TEXT.__objc_methtype: 0xf764
-  __TEXT.__objc_stubs: 0x45980
-  __DATA_CONST.__got: 0x17c8
+  __TEXT.__objc_stubs: 0x45960
+  __DATA_CONST.__got: 0x17b0
   __DATA_CONST.__const: 0x6d68
   __DATA_CONST.__objc_classlist: 0x1d80
   __DATA_CONST.__objc_catlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0x5e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4c218
+  __DATA_CONST.__objc_const: 0x4c1f8
   __DATA_CONST.__objc_selrefs: 0x16598
+  __DATA_CONST.__objc_protorefs: 0x108
+  __DATA_CONST.__objc_classrefs: 0x2220
+  __DATA_CONST.__objc_superrefs: 0x1700
   __DATA_CONST.__objc_arraydata: 0x1c38
   __AUTH_CONST.__objc_const: 0x14668
-  __AUTH_CONST.__cfstring: 0x1b0e0
+  __AUTH_CONST.__cfstring: 0x1b100
   __AUTH_CONST.__objc_arrayobj: 0xc18
-  __AUTH_CONST.__const: 0x45e8
+  __AUTH_CONST.__const: 0x45c0
   __AUTH_CONST.__objc_intobj: 0x2760
   __AUTH_CONST.__objc_doubleobj: 0x280
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x20d0
-  __AUTH.__objc_data: 0xd7a0
-  __AUTH.__data: 0x11b0
-  __DATA.__objc_protorefs: 0x108
-  __DATA.__objc_classrefs: 0x2218
-  __DATA.__objc_superrefs: 0x1700
-  __DATA.__objc_ivar: 0x3c5c
+  __AUTH_CONST.__auth_got: 0x20e0
+  __AUTH.__objc_data: 0xfd78
+  __AUTH.__data: 0x1278
+  __DATA.__objc_ivar: 0x3c58
   __DATA.__objc_data: 0x48
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x5f88
+  __DATA.__data: 0x6330
   __DATA.__bss: 0x2bb0
-  __DATA.__common: 0xc8
-  __DATA_DIRTY.__objc_data: 0x6c28
-  __DATA_DIRTY.__data: 0x550
-  __DATA_DIRTY.__bss: 0x6b8
-  __DATA_DIRTY.__common: 0x20
+  __DATA.__common: 0xc0
+  __DATA_DIRTY.__objc_data: 0x4650
+  __DATA_DIRTY.__data: 0x340
+  __DATA_DIRTY.__bss: 0x500
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClockKit.framework/ClockKit

   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
+  - /System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices
   - /System/Library/PrivateFrameworks/HealthHearing.framework/HealthHearing
   - /System/Library/PrivateFrameworks/HealthKitAdditions.framework/HealthKitAdditions
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FC6F75EF-C776-30A2-AC78-FAF4CC9C3EA0
-  Functions: 21452
-  Symbols:   59922
-  CStrings:  27790
+  UUID: DD7CCF2F-7E3C-3DD9-ACA6-6495667730C6
+  Functions: 21476
+  Symbols:   59933
+  CStrings:  27820
 
Symbols:
+ -[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:].cold.1
+ -[HKSleepDaySummary(HealthUI) hk_overlapsMidnightBasedDateInterval:gregorianCalendar:]
+ _HealthAppAnalyticsAgreementImproveHealthAndAnalytics
+ _MindfulnessAppIconForVisionPro
+ _OBJC_CLASS_$_HealthAppAnalyticsStore
+ __PROTOCOLS__TtC8HealthUI36AudiogramAverageSensitivityChartData.19
+ ___101-[HKRemoteCardioFitnessDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.242
+ ___101-[HKRemoteCardioFitnessDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.252
+ ___102-[HKDataMetadataSubsampleSection _submitCountStandHourQueryForSampleType:aggregateQueryFinishedBlock:]_block_invoke.254
+ ___102-[HKHorizontalSingleLineDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.263
+ ___102-[HKHorizontalTimePeriodDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.269
+ ___102-[HKQuantityDistributionDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.278
+ ___105-[HKHealthStore(HKUIAdditions) _primaryProfileFetchFirstAndLastNamesForInfoWrapper:meContact:completion:]_block_invoke.342
+ ___111-[HKJulianIndexedSevenDayQuantityDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.266
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.277
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.277.cold.1
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.279
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.279.cold.1
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.280
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.280.cold.1
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.281
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.281.cold.1
+ ___38-[HKSourceListDataSource fetchSources]_block_invoke.268
+ ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.269
+ ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.277
+ ___52-[HKSampleTypeUpdateController _createQueryForType:]_block_invoke.267
+ ___53-[HKDataMetadataOxygenSaturationSection queryForData]_block_invoke.270
+ ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.289
+ ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.294
+ ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke_2.295
+ ___56-[HKMedicalIDViewController _refreshMedicalIDInViewMode]_block_invoke.391
+ ___59-[HKDataMetadataViewController _fetchWorkoutRouteLocations]_block_invoke.310
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke.303
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_2.306
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_3.307
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_4.308
+ ___60-[HKTinkerSharingGizmoPermissionController sendOptInRequest]_block_invoke.268
+ ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.280
+ ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.280.cold.1
+ ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.299
+ ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.299.cold.1
+ ___64-[HKObjectDataAccessViewController _refreshAppAuthorizationData]_block_invoke.279
+ ___65-[HKAudioExposureDevicesDataSource _makeDeviceQueryForDeviceType]_block_invoke.246
+ ___65-[HKLevelCategoryDataSource queriesForRequest:completionHandler:]_block_invoke.249
+ ___65-[HKObjectDataAccessViewController switchCellValueChanged:value:]_block_invoke.302
+ ___66-[HKFitnessDiagnosticsRequestViewController _enableDataCollection]_block_invoke_2
+ ___66-[HKFitnessDiagnosticsRequestViewController _enableDataCollection]_block_invoke_3
+ ___66-[HKSourceAuthorizationController _reloadTypeAuthorizationRecords]_block_invoke.258
+ ___66-[_HKIngestSettingsViewController fetchEnabledStatusForPeripheral]_block_invoke.242
+ ___67-[HKFitnessDiagnosticsRequestViewController _disableDataCollection]_block_invoke_2
+ ___67-[HKFitnessDiagnosticsRequestViewController _disableDataCollection]_block_invoke_3
+ ___67-[HKSampleTypeCountDataSource queriesForRequest:completionHandler:]_block_invoke.246
+ ___68-[HKActivitySummaryDataProvider _mainQueueFetchValueWithRetryCount:]_block_invoke.292
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.318
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.318.cold.1
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.338
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.338.cold.1
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.339
+ ___72-[HKHorizontalSingleLineDataSource queriesForRequest:completionHandler:]_block_invoke.249
+ ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.246
+ ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.246.cold.1
+ ___78-[HKLocationFetcher fetchLocationsFromWorkout:workoutActivity:samplesHandler:]_block_invoke.249
+ ___81-[HKJulianIndexedSevenDayQuantityDataSource queriesForRequest:completionHandler:]_block_invoke.250
+ ___85-[HKRouteMapGenerator snapshotWithSize:lineWidth:traitCollection:offsets:completion:]_block_invoke.267
+ ___86-[HKOrganDonationConnectionManager _genericJSONDataTaskWithRequest:completionHandler:]_block_invoke.395
+ ___88-[HKHorizontalTimePeriodDataSource _chartPointsWithDateIntervalsByValue:sourceTimeZone:]_block_invoke.257
+ ___88-[HKWorkoutRouteViewController _internalDebuggingOnly_fetchUnsmoothedRoutesFromDatabase]_block_invoke.439
+ ___89-[HKInsulinDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.364
+ ___90-[HKClinicalSourceAuthorizationController _fetchAllClinicalAuthorizationRecordsWithError:]_block_invoke.243
+ ___92-[HKSleepChartDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.259
+ ___94-[HKQuantityTypeDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.346
+ ___95-[HKBloodPressureDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.288
+ ___95-[HKEmergencyCardNameAndPictureTableItem _checkOrRequestForCameraAccessIfNeededWithCompletion:]_block_invoke.304
+ ___95-[HKLevelCategoryDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.263
+ ___97-[HKBeatToBeatViewController initWithHRVSample:healthStore:displayTypeController:unitController:]_block_invoke.254
+ ___97-[HKSampleTypeCountDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.260
+ ___98-[HKHandwashingEventDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.365
+ ___98-[HKHealthStore(HKUIAdditions) _nonPrimaryProfileFetchFirstAndLastNamesForInfoWrapper:completion:]_block_invoke.346
+ ___98-[HKRecalibrateEstimatesPresentationController _requestAndConfigureHostViewController:completion:]_block_invoke.265
+ ___98-[HKTimePeriodSeriesDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.265
+ ___HKPreprocessingHandlerForUnderwaterDepth_block_invoke.335
+ ___block_literal_global.243
+ ___block_literal_global.248
+ ___block_literal_global.249
+ ___block_literal_global.251
+ ___block_literal_global.253
+ ___block_literal_global.260
+ ___block_literal_global.269
+ ___block_literal_global.271
+ ___block_literal_global.281
+ ___block_literal_global.287
+ ___block_literal_global.298
+ ___block_literal_global.300
+ ___block_literal_global.309
+ ___block_literal_global.310
+ ___block_literal_global.313
+ ___block_literal_global.314
+ ___block_literal_global.318
+ ___block_literal_global.321
+ ___block_literal_global.323
+ ___block_literal_global.324
+ ___block_literal_global.326
+ ___block_literal_global.331
+ ___block_literal_global.332
+ ___block_literal_global.336
+ ___block_literal_global.344
+ ___block_literal_global.357
+ ___block_literal_global.358
+ ___block_literal_global.375
+ ___block_literal_global.383
+ ___block_literal_global.504
+ ___block_literal_global.506
+ ___block_literal_global.509
+ ___block_literal_global.537
+ ___block_literal_global.545
+ ___block_literal_global.551
+ ___block_literal_global.561
+ ___block_literal_global.571
+ ___block_literal_global.584
+ ___block_literal_global.589
+ ___block_literal_global.594
+ ___block_literal_global.599
+ ___block_literal_global.604
+ ___block_literal_global.606
+ ___block_literal_global.622
+ ___block_literal_global.649
+ ___block_literal_global.651
+ ___block_literal_global.653
+ ___block_literal_global.657
+ ___block_literal_global.659
+ ___block_literal_global.661
+ ___block_literal_global.663
+ ___block_literal_global.680
+ ___block_literal_global.685
+ ___block_literal_global.690
+ ___block_literal_global.695
+ ___block_literal_global.707
+ ___block_literal_global.712
+ ___block_literal_global.716
+ ___block_literal_global.717
+ ___block_literal_global.722
+ ___block_literal_global.727
+ __unnamed_array_storage.1082
+ __unnamed_array_storage.1087
+ __unnamed_array_storage.1088
+ __unnamed_array_storage.1094
+ __unnamed_array_storage.1100
+ __unnamed_array_storage.1157
+ __unnamed_array_storage.1196
+ __unnamed_array_storage.1241
+ __unnamed_array_storage.248
+ __unnamed_array_storage.252
+ __unnamed_array_storage.269
+ __unnamed_array_storage.282
+ __unnamed_array_storage.288
+ __unnamed_array_storage.292
+ __unnamed_array_storage.294
+ __unnamed_array_storage.299
+ __unnamed_array_storage.309
+ __unnamed_array_storage.310
+ __unnamed_array_storage.312
+ __unnamed_array_storage.315
+ __unnamed_array_storage.317
+ __unnamed_array_storage.320
+ __unnamed_array_storage.323
+ __unnamed_array_storage.326
+ __unnamed_array_storage.330
+ __unnamed_array_storage.331
+ __unnamed_array_storage.335
+ __unnamed_array_storage.336
+ __unnamed_array_storage.340
+ __unnamed_array_storage.343
+ __unnamed_array_storage.346
+ __unnamed_array_storage.351
+ __unnamed_array_storage.358
+ __unnamed_array_storage.369
+ __unnamed_array_storage.381
+ __unnamed_array_storage.397
+ __unnamed_array_storage.400
+ __unnamed_array_storage.403
+ __unnamed_array_storage.476
+ __unnamed_array_storage.482
+ __unnamed_array_storage.485
+ __unnamed_array_storage.488
+ __unnamed_array_storage.491
+ __unnamed_array_storage.494
+ __unnamed_array_storage.503
+ __unnamed_array_storage.521
+ __unnamed_array_storage.522
+ __unnamed_array_storage.535
+ __unnamed_array_storage.536
+ __unnamed_array_storage.547
+ __unnamed_array_storage.555
+ __unnamed_array_storage.569
+ __unnamed_array_storage.601
+ __unnamed_array_storage.619
+ __unnamed_array_storage.640
+ __unnamed_array_storage.652
+ __unnamed_array_storage.663
+ __unnamed_array_storage.741
+ __unnamed_array_storage.917
+ __unnamed_array_storage.923
+ __unnamed_array_storage.929
+ __unnamed_array_storage.935
+ __unnamed_array_storage.965
+ _block_copy_helper.17
+ _block_copy_helper.20
+ _block_copy_helper.24
+ _block_copy_helper.27
+ _block_descriptor.19
+ _block_descriptor.22
+ _block_descriptor.26
+ _block_descriptor.29
+ _block_destroy_helper.18
+ _block_destroy_helper.21
+ _block_destroy_helper.25
+ _block_destroy_helper.28
+ _kMindfulnessAppBundleIDForVisionPro
+ _objc_msgSend$hk_dayIndexRangeWithCalendar:
+ _objc_msgSend$setUserDidAccept:currentAgreement:completion:
+ _sharedInstance.numberFormatter.321
+ _sharedInstance.onceToken.322
- -[HKDisplayTypeSectionedContextView _findAndInvalidateNearestCollectionViewCell]
- -[HKDisplayTypeSectionedContextView invalidateIntrinsicContentSizeIfWidthDesignationChanged]
- _OBJC_IVAR_$_HKDisplayTypeSectionedContextView._previousWidthDesignation
- __PROTOCOLS__TtC8HealthUI36AudiogramAverageSensitivityChartData.20
- ___101-[HKRemoteCardioFitnessDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.218
- ___101-[HKRemoteCardioFitnessDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.228
- ___102-[HKDataMetadataSubsampleSection _submitCountStandHourQueryForSampleType:aggregateQueryFinishedBlock:]_block_invoke.230
- ___102-[HKHorizontalSingleLineDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.239
- ___102-[HKHorizontalTimePeriodDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.245
- ___102-[HKQuantityDistributionDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.254
- ___105-[HKHealthStore(HKUIAdditions) _primaryProfileFetchFirstAndLastNamesForInfoWrapper:meContact:completion:]_block_invoke.318
- ___111-[HKJulianIndexedSevenDayQuantityDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.242
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.253
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.253.cold.1
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.255
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.255.cold.1
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.256
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.256.cold.1
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.257
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.257.cold.1
- ___38-[HKSourceListDataSource fetchSources]_block_invoke.244
- ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.245
- ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.253
- ___52-[HKSampleTypeUpdateController _createQueryForType:]_block_invoke.243
- ___53-[HKDataMetadataOxygenSaturationSection queryForData]_block_invoke.246
- ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.265
- ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.270
- ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke_2.271
- ___56-[HKMedicalIDViewController _refreshMedicalIDInViewMode]_block_invoke.367
- ___59-[HKDataMetadataViewController _fetchWorkoutRouteLocations]_block_invoke.286
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke.279
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_2.282
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_3.283
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_4.284
- ___60-[HKTinkerSharingGizmoPermissionController sendOptInRequest]_block_invoke.244
- ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.256
- ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.256.cold.1
- ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.275
- ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.275.cold.1
- ___64-[HKObjectDataAccessViewController _refreshAppAuthorizationData]_block_invoke.255
- ___65-[HKAudioExposureDevicesDataSource _makeDeviceQueryForDeviceType]_block_invoke.222
- ___65-[HKLevelCategoryDataSource queriesForRequest:completionHandler:]_block_invoke.225
- ___65-[HKObjectDataAccessViewController switchCellValueChanged:value:]_block_invoke.278
- ___66-[HKSourceAuthorizationController _reloadTypeAuthorizationRecords]_block_invoke.234
- ___66-[_HKIngestSettingsViewController fetchEnabledStatusForPeripheral]_block_invoke.218
- ___67-[HKSampleTypeCountDataSource queriesForRequest:completionHandler:]_block_invoke.222
- ___68-[HKActivitySummaryDataProvider _mainQueueFetchValueWithRetryCount:]_block_invoke.268
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.313
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.313.cold.1
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.314
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.cold.1
- ___72-[HKHorizontalSingleLineDataSource queriesForRequest:completionHandler:]_block_invoke.225
- ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.222
- ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.222.cold.1
- ___78-[HKLocationFetcher fetchLocationsFromWorkout:workoutActivity:samplesHandler:]_block_invoke.225
- ___81-[HKJulianIndexedSevenDayQuantityDataSource queriesForRequest:completionHandler:]_block_invoke.226
- ___85-[HKRouteMapGenerator snapshotWithSize:lineWidth:traitCollection:offsets:completion:]_block_invoke.243
- ___86-[HKOrganDonationConnectionManager _genericJSONDataTaskWithRequest:completionHandler:]_block_invoke.371
- ___88-[HKHorizontalTimePeriodDataSource _chartPointsWithDateIntervalsByValue:sourceTimeZone:]_block_invoke.233
- ___88-[HKWorkoutRouteViewController _internalDebuggingOnly_fetchUnsmoothedRoutesFromDatabase]_block_invoke.414
- ___89-[HKInsulinDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.339
- ___90-[HKClinicalSourceAuthorizationController _fetchAllClinicalAuthorizationRecordsWithError:]_block_invoke.219
- ___92-[HKSleepChartDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.235
- ___94-[HKQuantityTypeDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.322
- ___95-[HKBloodPressureDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.264
- ___95-[HKEmergencyCardNameAndPictureTableItem _checkOrRequestForCameraAccessIfNeededWithCompletion:]_block_invoke.280
- ___95-[HKLevelCategoryDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.239
- ___97-[HKBeatToBeatViewController initWithHRVSample:healthStore:displayTypeController:unitController:]_block_invoke.230
- ___97-[HKSampleTypeCountDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.236
- ___98-[HKHandwashingEventDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.340
- ___98-[HKHealthStore(HKUIAdditions) _nonPrimaryProfileFetchFirstAndLastNamesForInfoWrapper:completion:]_block_invoke.322
- ___98-[HKRecalibrateEstimatesPresentationController _requestAndConfigureHostViewController:completion:]_block_invoke.241
- ___98-[HKTimePeriodSeriesDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.241
- ___HKPreprocessingHandlerForUnderwaterDepth_block_invoke.311
- ___block_literal_global.219
- ___block_literal_global.224
- ___block_literal_global.225
- ___block_literal_global.227
- ___block_literal_global.229
- ___block_literal_global.236
- ___block_literal_global.237
- ___block_literal_global.239
- ___block_literal_global.242
- ___block_literal_global.245
- ___block_literal_global.247
- ___block_literal_global.252
- ___block_literal_global.257
- ___block_literal_global.259
- ___block_literal_global.265
- ___block_literal_global.270
- ___block_literal_global.272
- ___block_literal_global.274
- ___block_literal_global.278
- ___block_literal_global.286
- ___block_literal_global.297
- ___block_literal_global.299
- ___block_literal_global.312
- ___block_literal_global.333
- ___block_literal_global.334
- ___block_literal_global.350
- ___block_literal_global.479
- ___block_literal_global.481
- ___block_literal_global.485
- ___block_literal_global.488
- ___block_literal_global.502
- ___block_literal_global.520
- ___block_literal_global.534
- ___block_literal_global.536
- ___block_literal_global.544
- ___block_literal_global.547
- ___block_literal_global.549
- ___block_literal_global.554
- ___block_literal_global.564
- ___block_literal_global.581
- ___block_literal_global.597
- ___block_literal_global.613
- ___block_literal_global.624
- ___block_literal_global.626
- ___block_literal_global.628
- ___block_literal_global.630
- ___block_literal_global.632
- ___block_literal_global.634
- ___block_literal_global.636
- ___block_literal_global.660
- ___block_literal_global.665
- ___block_literal_global.670
- ___block_literal_global.672
- ___block_literal_global.677
- ___block_literal_global.682
- ___block_literal_global.687
- ___block_literal_global.692
- ___block_literal_global.698
- __unnamed_array_storage.1040
- __unnamed_array_storage.1046
- __unnamed_array_storage.1052
- __unnamed_array_storage.1058
- __unnamed_array_storage.1063
- __unnamed_array_storage.1133
- __unnamed_array_storage.1172
- __unnamed_array_storage.1217
- __unnamed_array_storage.224
- __unnamed_array_storage.228
- __unnamed_array_storage.240
- __unnamed_array_storage.244
- __unnamed_array_storage.245
- __unnamed_array_storage.246
- __unnamed_array_storage.251
- __unnamed_array_storage.257
- __unnamed_array_storage.258
- __unnamed_array_storage.274
- __unnamed_array_storage.276
- __unnamed_array_storage.284
- __unnamed_array_storage.286
- __unnamed_array_storage.287
- __unnamed_array_storage.290
- __unnamed_array_storage.293
- __unnamed_array_storage.295
- __unnamed_array_storage.303
- __unnamed_array_storage.311
- __unnamed_array_storage.316
- __unnamed_array_storage.319
- __unnamed_array_storage.334
- __unnamed_array_storage.345
- __unnamed_array_storage.357
- __unnamed_array_storage.373
- __unnamed_array_storage.376
- __unnamed_array_storage.378
- __unnamed_array_storage.379
- __unnamed_array_storage.440
- __unnamed_array_storage.443
- __unnamed_array_storage.446
- __unnamed_array_storage.449
- __unnamed_array_storage.452
- __unnamed_array_storage.455
- __unnamed_array_storage.458
- __unnamed_array_storage.461
- __unnamed_array_storage.498
- __unnamed_array_storage.511
- __unnamed_array_storage.512
- __unnamed_array_storage.523
- __unnamed_array_storage.531
- __unnamed_array_storage.545
- __unnamed_array_storage.577
- __unnamed_array_storage.595
- __unnamed_array_storage.616
- __unnamed_array_storage.628
- __unnamed_array_storage.639
- __unnamed_array_storage.717
- __unnamed_array_storage.827
- __unnamed_array_storage.833
- __unnamed_array_storage.839
- __unnamed_array_storage.845
- __unnamed_array_storage.941
- _block_copy_helper.18
- _block_copy_helper.22
- _block_copy_helper.25
- _block_copy_helper.29
- _block_descriptor.20
- _block_descriptor.24
- _block_descriptor.27
- _block_descriptor.31
- _block_destroy_helper.19
- _block_destroy_helper.23
- _block_destroy_helper.26
- _block_destroy_helper.30
- _keypath_set.9Tm
- _objc_msgSend$_findAndInvalidateNearestCollectionViewCell
- _objc_msgSend$invalidateIntrinsicContentSizeIfWidthDesignationChanged
- _objc_msgSend$setHealthDataSubmissionAllowed:
- _sharedInstance.numberFormatter.296
- _sharedInstance.onceToken.297
- _symbolic B1
- _symbolic q_
- _symbolic xq_xq_Iegnnrr_
CStrings:
+ "4\x12\x11"
+ "Can't construct Array with count < 0"
+ "Division by zero"
+ "Division results in an overflow"
+ "Failed to create app image for %@ identifier"
+ "Fetching Mindfulness VisionPro app image on %@"
+ "Index out of range"
+ "Insufficient space allocated to copy string contents"
+ "Range requires lowerBound <= upperBound"
+ "Swift/Array.swift"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Range.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,N"
+ "T@\"UIAction\",?,&,N"
+ "TB,?,R,N"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "app image size from loadAppImage: %f %f"
+ "figure.arms.open.and.exclamationmark.magnifyingglass"
+ "hk_dayIndexRangeWithCalendar:"
+ "hk_overlapsMidnightBasedDateInterval:gregorianCalendar:"
+ "invalid Collection: less than 'count' elements in collection"
+ "mindfulness_app_icon"
+ "setUserDidAccept:currentAgreement:completion:"
- "D\x12\x11"
- "T@\"UIAction\",&,N"
- "_findAndInvalidateNearestCollectionViewCell"
- "invalidateIntrinsicContentSizeIfWidthDesignationChanged"
- "list.bullet.clipboard"
- "setHealthDataSubmissionAllowed:"

```
