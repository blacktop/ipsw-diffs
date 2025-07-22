## HealthUI

> `/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI`

```diff

-6093.0.0.0.0
-  __TEXT.__text: 0x3b81dc
-  __TEXT.__auth_stubs: 0x4e80
-  __TEXT.__objc_methlist: 0x39264
-  __TEXT.__const: 0x6f14
-  __TEXT.__cstring: 0x23e77
-  __TEXT.__oslogstring: 0x67a6
-  __TEXT.__gcc_except_tab: 0x23d0
+6100.0.0.0.0
+  __TEXT.__text: 0x3bb520
+  __TEXT.__auth_stubs: 0x4f10
+  __TEXT.__objc_methlist: 0x393dc
+  __TEXT.__const: 0x6f74
+  __TEXT.__cstring: 0x23f77
+  __TEXT.__oslogstring: 0x6b16
+  __TEXT.__gcc_except_tab: 0x2500
   __TEXT.__ustring: 0x56
   __TEXT.__dlopen_cstrs: 0x367
-  __TEXT.__constg_swiftt: 0x39ac
-  __TEXT.__swift5_typeref: 0x27c0
+  __TEXT.__constg_swiftt: 0x3a74
+  __TEXT.__swift5_typeref: 0x27d6
   __TEXT.__swift5_reflstr: 0x20fe
-  __TEXT.__swift5_fieldmd: 0x20bc
+  __TEXT.__swift5_fieldmd: 0x20e8
   __TEXT.__swift5_builtin: 0x26c
   __TEXT.__swift5_assocty: 0x6e0
   __TEXT.__swift5_proto: 0x2a8
-  __TEXT.__swift5_types: 0x2e4
+  __TEXT.__swift5_types: 0x2ec
   __TEXT.__swift5_capture: 0x9c4
   __TEXT.__swift5_protos: 0x40
   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift5_mpenum: 0x34
-  __TEXT.__unwind_info: 0xda40
+  __TEXT.__unwind_info: 0xdad8
   __TEXT.__eh_frame: 0x1e8c
-  __TEXT.__objc_classname: 0x8ec1
-  __TEXT.__objc_methname: 0x7c6a4
-  __TEXT.__objc_methtype: 0x10693
-  __TEXT.__objc_stubs: 0x48a60
-  __DATA_CONST.__got: 0x3368
-  __DATA_CONST.__const: 0x7630
-  __DATA_CONST.__objc_classlist: 0x2030
+  __TEXT.__objc_classname: 0x8f00
+  __TEXT.__objc_methname: 0x7cc49
+  __TEXT.__objc_methtype: 0x106ef
+  __TEXT.__objc_stubs: 0x48cc0
+  __DATA_CONST.__got: 0x3398
+  __DATA_CONST.__const: 0x7790
+  __DATA_CONST.__objc_classlist: 0x2048
   __DATA_CONST.__objc_catlist: 0x298
-  __DATA_CONST.__objc_protolist: 0x660
+  __DATA_CONST.__objc_protolist: 0x668
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17f08
-  __DATA_CONST.__objc_protorefs: 0x158
+  __DATA_CONST.__objc_selrefs: 0x17fd0
+  __DATA_CONST.__objc_protorefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x1818
   __DATA_CONST.__objc_arraydata: 0x1fc8
-  __AUTH_CONST.__auth_got: 0x2750
-  __AUTH_CONST.__const: 0x57f8
+  __AUTH_CONST.__auth_got: 0x2798
+  __AUTH_CONST.__const: 0x5970
   __AUTH_CONST.__cfstring: 0x1e520
-  __AUTH_CONST.__objc_const: 0x62490
+  __AUTH_CONST.__objc_const: 0x62780
   __AUTH_CONST.__objc_arrayobj: 0xf30
   __AUTH_CONST.__objc_intobj: 0x2910
   __AUTH_CONST.__objc_doubleobj: 0x310
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x15800
-  __AUTH.__data: 0x1d38
-  __DATA.__objc_ivar: 0x3f88
-  __DATA.__data: 0x6e50
+  __AUTH.__objc_data: 0x15a18
+  __AUTH.__data: 0x1d88
+  __DATA.__objc_ivar: 0x3fa8
+  __DATA.__data: 0x6e70
   __DATA.__bss: 0x5898
   __DATA.__common: 0x1d8
   __DATA_DIRTY.__objc_data: 0x1e50

   - /System/Library/PrivateFrameworks/NanoResourceGrabber.framework/NanoResourceGrabber
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
+  - /System/Library/PrivateFrameworks/PreferencesExtended.framework/PreferencesExtended
   - /System/Library/PrivateFrameworks/PrintKitUI.framework/PrintKitUI
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet
   - /System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A7CA854D-04A9-334E-BD28-E31BA9E3ACD8
-  Functions: 23834
-  Symbols:   64489
-  CStrings:  29800
+  UUID: 96B5E367-2E03-330C-802F-80BE555E7196
+  Functions: 23891
+  Symbols:   64618
+  CStrings:  29858
 
Symbols:
+ +[HKInteractiveChartAnnotationView annotationCornerRadius]
+ +[HKSleepComparisonDayChartPoint chartPointsForSummaries:daySummaryCollections:context:]
+ +[HKSleepDurationChartPoint chartPointsForSummaries:daySummaryCollections:context:]
+ +[HKSleepPeriodChartPoint chartPointsForSummaries:daySummaryCollections:context:]
+ +[HKSleepStageChartPoint chartPointsForSummaries:daySummaryCollections:context:]
+ +[HKSleepStageDayChartPoint chartPointsForSummaries:daySummaryCollections:context:]
+ +[HKSleepStageDurationChartPoint chartPointsForSummaries:daySummaryCollections:context:]
+ -[HKAxis axisLabelsDependOnPointTransform]
+ -[HKAxisConfiguration axisLabelsDependOnPointTransform]
+ -[HKAxisConfiguration setAxisLabelsDependOnPointTransform:]
+ -[HKLocationFetcher _processQueryResultForRoutes:error:workout:withUpdateHandler:]
+ -[HKLocationFetcher _processQueryResultForRoutes:error:workout:withUpdateHandler:].cold.1
+ -[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]
+ -[HKLocationFetcher resultsQueue]
+ -[HKLocationFetcher setResultsQueue:]
+ -[HKSleepChartDataSource _graphSeriesDataBlockWithSleepDurationChartPointFor:context:]
+ -[HKSleepChartDataSource _graphSeriesDataBlockWithSleepPeriodChartPointFor:context:]
+ -[HKSleepChartDataSource _graphSeriesDataBlockWithSleepStageChartPointFor:context:]
+ -[HKSleepChartDataSource _graphSeriesDataBlockWithSleepStageDurationChartPointFor:context:]
+ -[HKSleepChartDataSource _shouldCreateDataSourceQueryResultsWrapperWith:context:]
+ -[HKSleepChartPointUserInfo initWithSeriesType:sleepDaySummary:sleepDaySummaryCollection:]
+ -[HKSleepChartPointUserInfo sleepDaySummaryCollection]
+ -[HKThrottleCallback _throttleExpirationUnderLock]
+ -[HKThrottleCallback delayInProgressX]
+ -[HKThrottleCallback setDelayInProgressX:]
+ -[HKThrottleCallback setThrottleExpirationQueue:]
+ -[HKThrottleCallback setThrottleExpirationTime:]
+ -[HKThrottleCallback throttleExpirationQueue]
+ -[HKThrottleCallback throttleExpirationTime]
+ -[_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper .cxx_destruct]
+ -[_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper daySummaries]
+ -[_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper daySummaryCollections]
+ -[_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper setDaySummaries:]
+ -[_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper setDaySummaryCollections:]
+ GCC_except_table73
+ GCC_except_table87
+ _OBJC_CLASS_$_HKSleepDaySummaryCollectionQuery
+ _OBJC_CLASS_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
+ _OBJC_CLASS_$__TtC8HealthUI20AudiogramNumericAxis
+ _OBJC_CLASS_$__TtCC8HealthUI20AudiogramNumericAxis25AudiogramAxisScalingRules
+ _OBJC_IVAR_$_HKAxis._axisLabelsDependOnPointTransform
+ _OBJC_IVAR_$_HKAxisConfiguration._axisLabelsDependOnPointTransform
+ _OBJC_IVAR_$_HKLocationFetcher._resultsQueue
+ _OBJC_IVAR_$_HKSleepChartPointUserInfo._sleepDaySummaryCollection
+ _OBJC_IVAR_$_HKThrottleCallback._delayInProgressX
+ _OBJC_IVAR_$_HKThrottleCallback._throttleExpirationQueue
+ _OBJC_IVAR_$_HKThrottleCallback._throttleExpirationTime
+ _OBJC_IVAR_$_HKThrottleCallback._throttleLock
+ _OBJC_IVAR_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper._daySummaries
+ _OBJC_IVAR_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper._daySummaryCollections
+ _OBJC_METACLASS_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
+ _OBJC_METACLASS_$__TtC8HealthUI20AudiogramNumericAxis
+ _OBJC_METACLASS_$__TtCC8HealthUI20AudiogramNumericAxis25AudiogramAxisScalingRules
+ __DATA__TtC8HealthUI20AudiogramNumericAxis
+ __DATA__TtCC8HealthUI20AudiogramNumericAxis25AudiogramAxisScalingRules
+ __INSTANCE_METHODS__TtC8HealthUI20AudiogramNumericAxis
+ __INSTANCE_METHODS__TtCC8HealthUI20AudiogramNumericAxis25AudiogramAxisScalingRules
+ __IVARS__TtCC8HealthUI20AudiogramNumericAxis25AudiogramAxisScalingRules
+ __METACLASS_DATA__TtC8HealthUI20AudiogramNumericAxis
+ __METACLASS_DATA__TtCC8HealthUI20AudiogramNumericAxis25AudiogramAxisScalingRules
+ __OBJC_$_CLASS_METHODS_HKInteractiveChartAnnotationView
+ __OBJC_$_INSTANCE_METHODS_UIViewController(HKAdditions|AdaptiveModalPresentation|HealthUI|HealthUI1)
+ __OBJC_$_INSTANCE_METHODS__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
+ __OBJC_$_INSTANCE_VARIABLES__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
+ __OBJC_$_PROP_LIST__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
+ __OBJC_CLASS_RO_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
+ __OBJC_METACLASS_RO_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
+ __PROTOCOLS__TtCC8HealthUI20AudiogramNumericAxis25AudiogramAxisScalingRules
+ __PROTOCOLS__TtCC8HealthUI20AudiogramNumericAxis25AudiogramAxisScalingRules.7
+ ___101-[HKRemoteCardioFitnessDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.290
+ ___101-[HKRemoteCardioFitnessDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.300
+ ___102-[HKDataMetadataSubsampleSection _submitCountStandHourQueryForSampleType:aggregateQueryFinishedBlock:]_block_invoke.302
+ ___102-[HKHorizontalSingleLineDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.311
+ ___102-[HKHorizontalTimePeriodDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.317
+ ___102-[HKQuantityDistributionDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.326
+ ___105-[HKClinicalSourceAuthorizationController _setAuthorizationStatuses:modes:shouldUpdateAnchor:completion:]_block_invoke.352
+ ___105-[HKHealthStore(HKUIAdditions) _primaryProfileFetchFirstAndLastNamesForInfoWrapper:meContact:completion:]_block_invoke.389
+ ___111-[HKJulianIndexedSevenDayQuantityDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.314
+ ___114-[HKDataMetadataSubsampleSection _exertionFixedValuesDisplayTypeController:unitController:healthStore:completion:]_block_invoke.310
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.329
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.329.cold.1
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.331
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.331.cold.1
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.333
+ ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.333.cold.1
+ ___38-[HKSourceListDataSource fetchSources]_block_invoke.316
+ ___45-[HKMedicationAuthorizationController reload]_block_invoke.304
+ ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.317
+ ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.325
+ ___52-[HKSampleTypeUpdateController _createQueryForType:]_block_invoke.315
+ ___53-[HKDataMetadataOxygenSaturationSection queryForData]_block_invoke.318
+ ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.341
+ ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.346
+ ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke_2.347
+ ___56-[HKMedicalIDViewController _refreshMedicalIDInViewMode]_block_invoke.439
+ ___59-[HKDataMetadataViewController _fetchWorkoutRouteLocations]_block_invoke.358
+ ___60-[HKHealthConceptPickerViewController disallowButtonTapped:]_block_invoke.367
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke.355
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_2.358
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_3.359
+ ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_4.360
+ ___60-[HKTinkerSharingGizmoPermissionController sendOptInRequest]_block_invoke.316
+ ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.316
+ ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.316.cold.1
+ ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.317
+ ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.320
+ ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.324
+ ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.325
+ ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.328
+ ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.328.cold.1
+ ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.351
+ ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.351.cold.1
+ ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke
+ ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke.311
+ ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke.313
+ ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke_2
+ ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke_2.312
+ ___64-[HKLocationFetcher _requeryRoutesForWorkout:withUpdateHandler:]_block_invoke_2.314
+ ___64-[HKObjectDataAccessViewController _refreshAppAuthorizationData]_block_invoke.327
+ ___65-[HKAudioExposureDevicesDataSource _makeDeviceQueryForDeviceType]_block_invoke.294
+ ___65-[HKClinicalSourceAuthorizationController _reloadWithCompletion:]_block_invoke.292
+ ___65-[HKLevelCategoryDataSource queriesForRequest:completionHandler:]_block_invoke.297
+ ___65-[HKObjectDataAccessViewController switchCellValueChanged:value:]_block_invoke.352
+ ___66-[HKSourceAuthorizationController _reloadTypeAuthorizationRecords]_block_invoke.352
+ ___66-[_HKIngestSettingsViewController fetchEnabledStatusForPeripheral]_block_invoke.290
+ ___67-[HKSampleTypeCountDataSource queriesForRequest:completionHandler:]_block_invoke.294
+ ___68-[HKActivitySummaryDataProvider _mainQueueFetchValueWithRetryCount:]_block_invoke.340
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.369
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.369.cold.1
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.389
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.389.cold.1
+ ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.390
+ ___72-[HKHorizontalSingleLineDataSource queriesForRequest:completionHandler:]_block_invoke.297
+ ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.294
+ ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.294.cold.1
+ ___80+[HKSleepStageChartPoint chartPointsForSummaries:daySummaryCollections:context:]_block_invoke
+ ___81+[HKSleepPeriodChartPoint chartPointsForSummaries:daySummaryCollections:context:]_block_invoke
+ ___81-[HKJulianIndexedSevenDayQuantityDataSource queriesForRequest:completionHandler:]_block_invoke.298
+ ___83+[HKSleepDurationChartPoint chartPointsForSummaries:daySummaryCollections:context:]_block_invoke
+ ___85-[HKRouteMapGenerator snapshotWithSize:lineWidth:traitCollection:offsets:completion:]_block_invoke.315
+ ___86-[HKOrganDonationConnectionManager _genericJSONDataTaskWithRequest:completionHandler:]_block_invoke.443
+ ___88+[HKSleepStageDurationChartPoint chartPointsForSummaries:daySummaryCollections:context:]_block_invoke
+ ___88-[HKHorizontalTimePeriodDataSource _chartPointsWithDateIntervalsByValue:sourceTimeZone:]_block_invoke.305
+ ___88-[HKWorkoutRouteViewController _internalDebuggingOnly_fetchUnsmoothedRoutesFromDatabase]_block_invoke.489
+ ___89-[HKInsulinDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.412
+ ___92-[HKSleepChartDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.337
+ ___94-[HKQuantityTypeDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.392
+ ___95-[HKBloodPressureDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.337
+ ___95-[HKEmergencyCardNameAndPictureTableItem _checkOrRequestForCameraAccessIfNeededWithCompletion:]_block_invoke.352
+ ___95-[HKLevelCategoryDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.311
+ ___97-[HKBeatToBeatViewController initWithHRVSample:healthStore:displayTypeController:unitController:]_block_invoke.302
+ ___97-[HKSampleTypeCountDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.308
+ ___98-[HKHandwashingEventDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.413
+ ___98-[HKHealthStore(HKUIAdditions) _nonPrimaryProfileFetchFirstAndLastNamesForInfoWrapper:completion:]_block_invoke.393
+ ___98-[HKRecalibrateEstimatesPresentationController _requestAndConfigureHostViewController:completion:]_block_invoke.313
+ ___98-[HKTimePeriodSeriesDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.313
+ ___block_descriptor_32_e43_q24?0"HKWorkoutRoute"8"HKWorkoutRoute"16l
+ ___block_descriptor_48_e8_32s40s_e32_"HKGraphSeriesDataBlock"16?08ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e85_v48?0"HKAnchoredObjectQuery"8"NSArray"16"NSArray"24"HKQueryAnchor"32"NSError"40lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e20_v24?08"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e34_v32?0"HKSleepDaySummary"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e34_v32?0"HKSleepDaySummary"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40bs48r56r64r_e5_v8?0lr48l8r56l8s32l8s40l8r64l8
+ ___block_descriptor_72_e8_32s40s48bs56r64w_e5_v8?0ls32l8s40l8w64l8r56l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e56_v32?0"HKSleepDaySummaryQuery"8"NSArray"16"NSError"24ls32l8s40l8r56l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e85_v48?0"HKAnchoredObjectQuery"8"NSArray"16"NSArray"24"HKQueryAnchor"32"NSError"40ls32l8s40l8s48l8r64l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8r72l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8s40l8r72l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8r72l8s56l8s64l8
+ ___block_descriptor_89_e8_32s40s48s56s64bs72r80r_e56_v32?0"HKSleepDaySummaryQuery"8"NSArray"16"NSError"24ls32l8s40l8s48l8r72l8r80l8s56l8s64l8
+ ___block_literal_global.291
+ ___block_literal_global.296
+ ___block_literal_global.297
+ ___block_literal_global.298
+ ___block_literal_global.308
+ ___block_literal_global.309
+ ___block_literal_global.317
+ ___block_literal_global.318
+ ___block_literal_global.319
+ ___block_literal_global.325
+ ___block_literal_global.329
+ ___block_literal_global.331
+ ___block_literal_global.337
+ ___block_literal_global.338
+ ___block_literal_global.346
+ ___block_literal_global.348
+ ___block_literal_global.353
+ ___block_literal_global.354
+ ___block_literal_global.355
+ ___block_literal_global.371
+ ___block_literal_global.372
+ ___block_literal_global.376
+ ___block_literal_global.380
+ ___block_literal_global.384
+ ___block_literal_global.389
+ ___block_literal_global.393
+ ___block_literal_global.405
+ ___block_literal_global.406
+ ___block_literal_global.414
+ ___block_literal_global.421
+ ___block_literal_global.432
+ ___block_literal_global.444
+ ___block_literal_global.544
+ ___block_literal_global.558
+ ___block_literal_global.560
+ ___block_literal_global.581
+ ___block_literal_global.589
+ ___block_literal_global.593
+ ___block_literal_global.606
+ ___block_literal_global.611
+ ___block_literal_global.616
+ ___block_literal_global.621
+ ___block_literal_global.626
+ ___block_literal_global.631
+ ___block_literal_global.636
+ ___block_literal_global.641
+ ___block_literal_global.646
+ ___block_literal_global.651
+ ___block_literal_global.656
+ ___block_literal_global.661
+ ___block_literal_global.676
+ ___block_literal_global.692
+ ___block_literal_global.697
+ ___block_literal_global.708
+ ___block_literal_global.710
+ ___block_literal_global.712
+ ___block_literal_global.714
+ ___block_literal_global.716
+ ___block_literal_global.718
+ ___block_literal_global.720
+ ___block_literal_global.722
+ ___block_literal_global.739
+ ___block_literal_global.744
+ ___block_literal_global.749
+ ___block_literal_global.754
+ ___block_literal_global.756
+ ___block_literal_global.761
+ ___block_literal_global.766
+ ___block_literal_global.771
+ ___block_literal_global.776
+ ___block_literal_global.781
+ ___block_literal_global.786
+ ___block_literal_global.788
+ ___block_literal_global.790
+ ___block_literal_global.792
+ ___block_literal_global.794
+ ___block_literal_global.796
+ ___block_literal_global.798
+ ___block_literal_global.800
+ ___block_literal_global.802
+ ___block_literal_global.804
+ ___block_literal_global.806
+ ___block_literal_global.808
+ ___block_literal_global.810
+ ___block_literal_global.812
+ ___block_literal_global.814
+ ___block_literal_global.828
+ ___block_literal_global.936
+ ___block_literal_global.948
+ _clock_gettime_nsec_np
+ _objc_msgSend$_graphSeriesDataBlockWithSleepDurationChartPointFor:context:
+ _objc_msgSend$_graphSeriesDataBlockWithSleepPeriodChartPointFor:context:
+ _objc_msgSend$_graphSeriesDataBlockWithSleepStageChartPointFor:context:
+ _objc_msgSend$_graphSeriesDataBlockWithSleepStageDurationChartPointFor:context:
+ _objc_msgSend$_processQueryResultForRoutes:error:workout:withUpdateHandler:
+ _objc_msgSend$_requeryRoutesForWorkout:withUpdateHandler:
+ _objc_msgSend$_shouldCreateDataSourceQueryResultsWrapperWith:context:
+ _objc_msgSend$annotationCornerRadius
+ _objc_msgSend$axisLabelsDependOnPointTransform
+ _objc_msgSend$chartPointsForSummaries:daySummaryCollections:context:
+ _objc_msgSend$daySummaries
+ _objc_msgSend$daySummaryCollections
+ _objc_msgSend$initWithMorningIndexRange:resultsHandler:
+ _objc_msgSend$initWithSeriesType:sleepDaySummary:sleepDaySummaryCollection:
+ _objc_msgSend$newSleep6MonthView
+ _objc_msgSend$predicateForSamplesWithCorrelationedSample
+ _objc_msgSend$predicateForWorkoutRoutesUsingMetadataForWorkout:
+ _objc_msgSend$setAxisLabelsDependOnPointTransform:
+ _objc_msgSend$setDaySummaries:
+ _objc_msgSend$setDaySummaryCollections:
+ _objc_msgSend$setThrottleExpirationQueue:
+ _objc_msgSend$setThrottleExpirationTime:
+ _objc_msgSend$sleepDaySummaryCollection
+ _objc_msgSend$throttleExpirationQueue
+ _objc_msgSend$throttleExpirationTime
+ _sharedInstance.numberFormatter.369
+ _sharedInstance.onceToken.370
+ _symbolic _____ 8HealthUI20AudiogramNumericAxisC
+ _symbolic _____ 8HealthUI20AudiogramNumericAxisC0cE12ScalingRulesC
+ _symbolic _____SgXw 8HealthUI20AudiogramNumericAxisC
- +[HKSleepComparisonDayChartPoint chartPointsForSummaries:context:]
- +[HKSleepDurationChartPoint chartPointsForSummaries:context:]
- +[HKSleepPeriodChartPoint chartPointsForSummaries:context:]
- +[HKSleepStageChartPoint chartPointsForSummaries:context:]
- +[HKSleepStageDayChartPoint chartPointsForSummaries:context:]
- +[HKSleepStageDurationChartPoint chartPointsForSummaries:context:]
- +[UIColor(HKAdditions) hk_sleepSecondaryColor]
- -[HKSleepChartPointUserInfo initWithSeriesType:sleepDaySummary:]
- -[HKThrottleCallback delayInProgress]
- -[HKThrottleCallback setDelayInProgress:]
- -[HKThrottleCallback setThrottlingQueue:]
- -[HKThrottleCallback throttlingQueue]
- GCC_except_table62
- GCC_except_table71
- GCC_except_table74
- GCC_except_table86
- _OBJC_IVAR_$_HKThrottleCallback._delayInProgress
- _OBJC_IVAR_$_HKThrottleCallback._throttlingQueue
- __OBJC_$_INSTANCE_METHODS_UIViewController(HKAdditions|AdaptiveModalPresentation|HealthUI)
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
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.334
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.334.cold.1
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.335
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.335.cold.1
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.336
- ___126-[HKHealthChartFactory encodeChartQueryDataForTypeIdentifier:forTimeScopes:timeScopeReferenceDate:audience:completionHandler:]_block_invoke.336.cold.1
- ___38-[HKSourceListDataSource fetchSources]_block_invoke.319
- ___42-[HKThrottleCallback executeWithThrottle:]_block_invoke_2
- ___45-[HKMedicationAuthorizationController reload]_block_invoke.307
- ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.320
- ___50-[HKTinkerSharingSyncSetupController setupSharing]_block_invoke.328
- ___52-[HKSampleTypeUpdateController _createQueryForType:]_block_invoke.318
- ___53-[HKDataMetadataOxygenSaturationSection queryForData]_block_invoke.321
- ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.344
- ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke.349
- ___54+[HKSourceListDataSource _builtinIconFetchTransformer]_block_invoke_2.350
- ___56-[HKMedicalIDViewController _refreshMedicalIDInViewMode]_block_invoke.442
- ___58+[HKSleepStageChartPoint chartPointsForSummaries:context:]_block_invoke
- ___59+[HKSleepPeriodChartPoint chartPointsForSummaries:context:]_block_invoke
- ___59-[HKDataMetadataViewController _fetchWorkoutRouteLocations]_block_invoke.361
- ___60-[HKHealthConceptPickerViewController disallowButtonTapped:]_block_invoke.370
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke.358
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_2.361
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_3.362
- ___60-[HKSourceListDataSource _didFetchSources:error:completion:]_block_invoke_4.363
- ___60-[HKTinkerSharingGizmoPermissionController sendOptInRequest]_block_invoke.319
- ___61+[HKSleepDurationChartPoint chartPointsForSummaries:context:]_block_invoke
- ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.296
- ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.cold.1
- ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.331
- ___63+[HKSourceListDataSource _builtinInstallationStatusTransformer]_block_invoke.331.cold.1
- ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.354
- ___64+[HKSourceListDataSource _builtinPurposeStringsFetchTransformer]_block_invoke.354.cold.1
- ___64-[HKObjectDataAccessViewController _refreshAppAuthorizationData]_block_invoke.330
- ___65-[HKAudioExposureDevicesDataSource _makeDeviceQueryForDeviceType]_block_invoke.297
- ___65-[HKClinicalSourceAuthorizationController _reloadWithCompletion:]_block_invoke.295
- ___65-[HKLevelCategoryDataSource queriesForRequest:completionHandler:]_block_invoke.300
- ___65-[HKObjectDataAccessViewController switchCellValueChanged:value:]_block_invoke.355
- ___66+[HKSleepStageDurationChartPoint chartPointsForSummaries:context:]_block_invoke
- ___66-[HKSourceAuthorizationController _reloadTypeAuthorizationRecords]_block_invoke.355
- ___66-[_HKIngestSettingsViewController fetchEnabledStatusForPeripheral]_block_invoke.293
- ___67-[HKSampleTypeCountDataSource queriesForRequest:completionHandler:]_block_invoke.297
- ___68-[HKActivitySummaryDataProvider _mainQueueFetchValueWithRetryCount:]_block_invoke.343
- ___69-[HKLocationFetcher _workoutRoutesQueryForWorkout:withUpdateHandler:]_block_invoke.cold.1
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.372
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.372.cold.1
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.392
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.392.cold.1
- ___72-[HKAppImageManager _enqueueRequestForAppIconForIdentifier:productType:]_block_invoke.393
- ___72-[HKHorizontalSingleLineDataSource queriesForRequest:completionHandler:]_block_invoke.300
- ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.297
- ___75-[HKNanoHostAuthorizationController setRequestRecord:presentationRequests:]_block_invoke.297.cold.1
- ___81-[HKJulianIndexedSevenDayQuantityDataSource queriesForRequest:completionHandler:]_block_invoke.301
- ___85-[HKRouteMapGenerator snapshotWithSize:lineWidth:traitCollection:offsets:completion:]_block_invoke.318
- ___86-[HKOrganDonationConnectionManager _genericJSONDataTaskWithRequest:completionHandler:]_block_invoke.446
- ___88-[HKHorizontalTimePeriodDataSource _chartPointsWithDateIntervalsByValue:sourceTimeZone:]_block_invoke.308
- ___88-[HKWorkoutRouteViewController _internalDebuggingOnly_fetchUnsmoothedRoutesFromDatabase]_block_invoke.492
- ___89-[HKInsulinDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.415
- ___92-[HKSleepChartDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.312
- ___94-[HKQuantityTypeDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.395
- ___95-[HKBloodPressureDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.339
- ___95-[HKEmergencyCardNameAndPictureTableItem _checkOrRequestForCameraAccessIfNeededWithCompletion:]_block_invoke.355
- ___95-[HKLevelCategoryDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.314
- ___97-[HKBeatToBeatViewController initWithHRVSample:healthStore:displayTypeController:unitController:]_block_invoke.305
- ___97-[HKSampleTypeCountDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.311
- ___98-[HKHandwashingEventDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.416
- ___98-[HKHealthStore(HKUIAdditions) _nonPrimaryProfileFetchFirstAndLastNamesForInfoWrapper:completion:]_block_invoke.396
- ___98-[HKRecalibrateEstimatesPresentationController _requestAndConfigureHostViewController:completion:]_block_invoke.316
- ___98-[HKTimePeriodSeriesDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.316
- ___block_descriptor_40_e8_32s_e27_16?0"HKSleepDaySummary"8ls32l8
- ___block_descriptor_40_e8_32s_e32_"HKGraphSeriesDataBlock"16?08ls32l8
- ___block_descriptor_48_e8_32s_e27_16?0"HKSleepDaySummary"8ls32l8
- ___block_descriptor_56_e8_32s40bs48w_e85_v48?0"HKAnchoredObjectQuery"8"NSArray"16"NSArray"24"HKQueryAnchor"32"NSError"40ls40l8w48l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e56_v32?0"HKSleepDaySummaryQuery"8"NSArray"16"NSError"24ls32l8s40l8s48l8
- ___block_literal_global.294
- ___block_literal_global.300
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.312
- ___block_literal_global.314
- ___block_literal_global.322
- ___block_literal_global.323
- ___block_literal_global.324
- ___block_literal_global.328
- ___block_literal_global.332
- ___block_literal_global.334
- ___block_literal_global.340
- ___block_literal_global.341
- ___block_literal_global.349
- ___block_literal_global.351
- ___block_literal_global.363
- ___block_literal_global.365
- ___block_literal_global.367
- ___block_literal_global.377
- ___block_literal_global.379
- ___block_literal_global.381
- ___block_literal_global.383
- ___block_literal_global.387
- ___block_literal_global.392
- ___block_literal_global.396
- ___block_literal_global.408
- ___block_literal_global.409
- ___block_literal_global.417
- ___block_literal_global.427
- ___block_literal_global.435
- ___block_literal_global.447
- ___block_literal_global.547
- ___block_literal_global.555
- ___block_literal_global.557
- ___block_literal_global.587
- ___block_literal_global.592
- ___block_literal_global.596
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
- ___block_literal_global.793
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
- ___block_literal_global.830
- ___block_literal_global.939
- ___block_literal_global.951
- _objc_msgSend$chartPointsForSummaries:context:
- _objc_msgSend$delayInProgress
- _objc_msgSend$initWithSeriesType:sleepDaySummary:
- _objc_msgSend$setDelayInProgress:
- _objc_msgSend$setThrottlingQueue:
- _objc_msgSend$throttlingQueue
- _sharedInstance.numberFormatter.372
- _sharedInstance.onceToken.373
CStrings:
+ "%s: navigation controller was nil, unable to show view controller %s"
+ "@\"HKSleepDaySummaryCollection\""
+ "@\"NSArray\"40@0:8@\"NSArray\"16@\"NSArray\"24@\"HKSleepAnalysisDataSourceContext\"32"
+ "B40@0:8@\"UISearchBar\"16@\"NSArray\"24@\"NSString\"32"
+ "HKThrottleExpirationQueue"
+ "HealthUI.AudiogramAxisScalingRules"
+ "HealthUI/SettingsNavigationProxy.swift"
+ "HealthUI1"
+ "SleepChartDataSource"
+ "T@\"HKSleepDaySummaryCollection\",R,N,V_sleepDaySummaryCollection"
+ "T@\"NSArray\",C,N,V_daySummaries"
+ "T@\"NSArray\",C,N,V_daySummaryCollections"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_resultsQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_throttleExpirationQueue"
+ "TB,N,V_axisLabelsDependOnPointTransform"
+ "TB,N,V_delayInProgressX"
+ "TB,R,N,V_axisLabelsDependOnPointTransform"
+ "Tq,N,V_throttleExpirationTime"
+ "[%{public}@.%{public}@]: Decremented query counter after sleep day summary collection query with %ld collections"
+ "[%{public}@.%{public}@]: Decremented query counter after sleep day summary query"
+ "[%{public}@.%{public}@]: Sleep day summary query returned while at 6 month time scope with %ld summaries"
+ "[%{public}@.%{public}@]: Task completion counter count is 0, returning %ld summaries and %ld collections"
+ "[%{public}@.%{public}@]] Error from sleep day summary collection query: %@, error: %@"
+ "[%{public}@.%{public}@]] No sleep day summary collections returned from query: %@"
+ "[RemoteCharting]_%@_%@: no results were returned from query with error: %@"
+ "[routes] Found %lu routes via associations for workout %{public}@"
+ "[routes] Found %lu routes via metadata for workout %{public}@"
+ "[routes] Found %lu unique routes workout %{public}@"
+ "[routes] Querying for all routes for workout %{public}@"
+ "_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper"
+ "_TtC8HealthUI20AudiogramNumericAxis"
+ "_TtCC8HealthUI20AudiogramNumericAxis25AudiogramAxisScalingRules"
+ "_axisLabelsDependOnPointTransform"
+ "_daySummaries"
+ "_daySummaryCollections"
+ "_delayInProgressX"
+ "_graphSeriesDataBlockWithSleepDurationChartPointFor:context:"
+ "_graphSeriesDataBlockWithSleepPeriodChartPointFor:context:"
+ "_graphSeriesDataBlockWithSleepStageChartPointFor:context:"
+ "_graphSeriesDataBlockWithSleepStageDurationChartPointFor:context:"
+ "_processQueryResultForRoutes:error:workout:withUpdateHandler:"
+ "_requeryRoutesForWorkout:withUpdateHandler:"
+ "_shouldCreateDataSourceQueryResultsWrapperWith:context:"
+ "_sleepDaySummaryCollection"
+ "_throttleExpirationQueue"
+ "_throttleExpirationTime"
+ "_throttleExpirationUnderLock"
+ "_throttleLock"
+ "annotationCornerRadius"
+ "audiogramYAxis"
+ "axisLabelsDependOnPointTransform"
+ "chartPointsForSummaries:daySummaryCollections:context:"
+ "daySummaries"
+ "daySummaryCollections"
+ "delayInProgressX"
+ "hk_showViewController:animated:"
+ "initWithMorningIndexRange:resultsHandler:"
+ "initWithSeriesType:sleepDaySummary:sleepDaySummaryCollection:"
+ "newSleep6MonthView"
+ "predicateForSamplesWithCorrelationedSample"
+ "predicateForWorkoutRoutesUsingMetadataForWorkout:"
+ "q24@?0@\"HKWorkoutRoute\"8@\"HKWorkoutRoute\"16"
+ "results"
+ "resultsQueue"
+ "searchBar:shouldChangeTextInRanges:replacementText:"
+ "setAxisLabelsDependOnPointTransform:"
+ "setDaySummaries:"
+ "setDaySummaryCollections:"
+ "setDelayInProgressX:"
+ "setResultsQueue:"
+ "setThrottleExpirationQueue:"
+ "setThrottleExpirationTime:"
+ "sleepDaySummaryCollection"
+ "throttleExpirationQueue"
+ "throttleExpirationTime"
- "@\"NSArray\"32@0:8@\"NSArray\"16@\"HKSleepAnalysisDataSourceContext\"24"
- "@16@?0@\"HKSleepDaySummary\"8"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_throttlingQueue"
- "TB,N,V_delayInProgress"
- "[RemoteCharting]_%@_%@: no day summaries were returned from query with error: %@"
- "_delayInProgress"
- "_throttlingQueue"
- "chartPointsForSummaries:context:"
- "delayInProgress"
- "hk_sleepSecondaryColor"
- "initWithSeriesType:sleepDaySummary:"
- "setDelayInProgress:"
- "setThrottlingQueue:"
- "sleep_overlay_tint_color"
- "sleep_secondary_color"
- "throttlingQueue"

```
