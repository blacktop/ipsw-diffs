## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-6093.0.0.0.0
-  __TEXT.__text: 0x33280c
-  __TEXT.__auth_stubs: 0x36b0
-  __TEXT.__objc_methlist: 0x2f7bc
-  __TEXT.__cstring: 0x34923
-  __TEXT.__const: 0xabd62
-  __TEXT.__oslogstring: 0xc0e3
-  __TEXT.__gcc_except_tab: 0x40e0
+6100.0.0.0.0
+  __TEXT.__text: 0x333b08
+  __TEXT.__auth_stubs: 0x36d0
+  __TEXT.__objc_methlist: 0x2f8cc
+  __TEXT.__cstring: 0x34b43
+  __TEXT.__const: 0xabf22
+  __TEXT.__oslogstring: 0xc1f3
+  __TEXT.__gcc_except_tab: 0x40b0
   __TEXT.__ustring: 0x78
   __TEXT.__dlopen_cstrs: 0x5da
-  __TEXT.__constg_swiftt: 0x2ffc
-  __TEXT.__swift5_typeref: 0x2cad
-  __TEXT.__swift5_fieldmd: 0x2d28
+  __TEXT.__constg_swiftt: 0x2fa4
+  __TEXT.__swift5_typeref: 0x2cf9
+  __TEXT.__swift5_fieldmd: 0x2ce4
   __TEXT.__swift5_builtin: 0x398
-  __TEXT.__swift5_reflstr: 0x1ee2
+  __TEXT.__swift5_reflstr: 0x1e92
   __TEXT.__swift5_assocty: 0xb78
-  __TEXT.__swift5_proto: 0xbe0
-  __TEXT.__swift5_types: 0x408
-  __TEXT.__swift5_capture: 0x77c
+  __TEXT.__swift5_proto: 0xbdc
+  __TEXT.__swift5_types: 0x400
+  __TEXT.__swift5_capture: 0x78c
   __TEXT.__swift_as_entry: 0x14c
   __TEXT.__swift_as_ret: 0x14c
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xf8e8
+  __TEXT.__unwind_info: 0xf940
   __TEXT.__eh_frame: 0x3fe8
   __TEXT.__objc_classname: 0x8970
-  __TEXT.__objc_methname: 0x5d363
-  __TEXT.__objc_methtype: 0xbf15
-  __TEXT.__objc_stubs: 0x2b1c0
-  __DATA_CONST.__got: 0x1b00
-  __DATA_CONST.__const: 0xf4a0
-  __DATA_CONST.__objc_classlist: 0x1aa0
+  __TEXT.__objc_methname: 0x5d543
+  __TEXT.__objc_methtype: 0xbf29
+  __TEXT.__objc_stubs: 0x2b1e0
+  __DATA_CONST.__got: 0x1b10
+  __DATA_CONST.__const: 0xf478
+  __DATA_CONST.__objc_classlist: 0x1aa8
   __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x112a8
+  __DATA_CONST.__objc_selrefs: 0x11318
   __DATA_CONST.__objc_protorefs: 0x608
   __DATA_CONST.__objc_superrefs: 0x1728
   __DATA_CONST.__objc_arraydata: 0x68e8
-  __AUTH_CONST.__auth_got: 0x1b70
-  __AUTH_CONST.__const: 0xb980
-  __AUTH_CONST.__cfstring: 0x31fc0
-  __AUTH_CONST.__objc_const: 0x4faf0
+  __AUTH_CONST.__auth_got: 0x1b80
+  __AUTH_CONST.__const: 0xb950
+  __AUTH_CONST.__cfstring: 0x32020
+  __AUTH_CONST.__objc_const: 0x4fbd8
   __AUTH_CONST.__objc_intobj: 0x4590
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x6d8
-  __AUTH.__objc_data: 0xe9c0
-  __AUTH.__data: 0x1988
+  __AUTH.__objc_data: 0xeaa0
+  __AUTH.__data: 0x1938
   __DATA.__objc_ivar: 0x2dc0
-  __DATA.__data: 0xce38
-  __DATA.__bss: 0x18340
+  __DATA.__data: 0xce58
+  __DATA.__bss: 0x182c0
   __DATA.__common: 0x9a8
   __DATA_DIRTY.__objc_data: 0x2430
   __DATA_DIRTY.__data: 0x130

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 1A05FFF3-9FBA-3753-BB2A-5D5E703778BD
-  Functions: 23887
-  Symbols:   60695
-  CStrings:  29678
+  UUID: 23C090F1-50E8-3837-83D6-5183510B8B7A
+  Functions: 23917
+  Symbols:   60710
+  CStrings:  29721
 
Symbols:
+ +[HKQuery(HKPredicates) predicateForWorkoutRoutesUsingMetadataForWorkout:]
+ +[HKSleepPeriod sleepPeriodWithDateInterval:segments:isIncomplete:timezoneName:]
+ -[HKAnalyticsEnvironmentDataSource areHealthNotificationsAuthorized]
+ -[HKSleepDaySummary _updatingPeriods:]
+ -[HKSleepDaySummary durationsForStrategyType:]
+ -[HKSleepDaySummary primarySleepPeriodUsingSummaryDurationStrategyType:]
+ -[HKSleepDaySummary summaryFilteredWithOptions:]
+ -[HKSleepDaySummary summaryFilteredWithOptions:strategyType:]
+ -[HKSleepDaySummaryDurationCollection durationsForStrategyType:]
+ -[HKSleepDaySummaryDurationCollection durationsForStrategyType:].cold.1
+ -[HKSleepPeriod timezoneName]
+ GCC_except_table117
+ GCC_except_table58
+ _OBJC_CLASS_$_HKSleepDaySummaryCollection
+ _OBJC_CLASS_$_HKSleepDaySummaryCollectionQuery
+ _OBJC_IVAR_$_HKSleepPeriod._timezoneName
+ _OBJC_METACLASS_$_HKSleepDaySummaryCollection
+ _OBJC_METACLASS_$_HKSleepDaySummaryCollectionQuery
+ __DATA_HKSleepDaySummaryCollection
+ __DATA_HKSleepDaySummaryCollectionQuery
+ __HKPrivateMetadataKeySmoothedRouteWorkoutAssociatedUUID
+ __INSTANCE_METHODS_HKSleepDaySummaryCollection
+ __INSTANCE_METHODS_HKSleepDaySummaryCollectionQuery
+ __IVARS_HKSleepDaySummaryCollection
+ __IVARS_HKSleepDaySummaryCollectionQuery
+ __METACLASS_DATA_HKSleepDaySummaryCollection
+ __METACLASS_DATA_HKSleepDaySummaryCollectionQuery
+ __PROPERTIES_HKSleepDaySummaryCollection
+ __PROPERTIES_HKSleepDaySummaryCollectionQuery
+ ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.385
+ ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.386
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.306
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.314
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.307
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.307.cold.1
+ ___129-[HKHealthStore fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.375
+ ___143-[HKHealthStoreImplementation fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.391
+ ___33-[HKHealthStore dropEntitlement:]_block_invoke.630
+ ___34-[HKHealthStore _supportsFeature:]_block_invoke.533
+ ___34-[HKHealthStore _supportsFeature:]_block_invoke.533.cold.1
+ ___34-[HKWorkoutBuilder discardWorkout]_block_invoke.73
+ ___34-[HKWorkoutBuilder discardWorkout]_block_invoke.73.cold.1
+ ___36-[HKHealthStore restoreEntitlement:]_block_invoke.631
+ ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.255
+ ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.255.cold.1
+ ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.257
+ ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.257.cold.1
+ ___43-[HKWorkoutBuilder _pushCurrentTargetState]_block_invoke.82
+ ___43-[HKWorkoutBuilder _pushCurrentTargetState]_block_invoke.82.cold.1
+ ___43-[HKWorkoutBuilder _recoverWithCompletion:]_block_invoke.258
+ ___43-[HKWorkoutBuilder _recoverWithCompletion:]_block_invoke.258.cold.1
+ ___44-[HKHealthStore authorizationStatusForType:]_block_invoke.402
+ ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.649
+ ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.550
+ ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.550.cold.1
+ ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.650
+ ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke.507
+ ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke_2.508
+ ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.551
+ ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.551.cold.1
+ ___58-[HKHealthStore pluginServiceEndpointForIdentifier:error:]_block_invoke.373
+ ___58-[HKHealthStoreImplementation authorizationStatusForType:]_block_invoke.418
+ ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.593
+ ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.593.cold.1
+ ___61-[HKSleepDaySummary summaryFilteredWithOptions:strategyType:]_block_invoke
+ ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.300
+ ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.301
+ ___66-[HKWorkoutBuilder clientRemote_stateDidChange:startDate:endDate:]_block_invoke.135
+ ___67-[HKHealthStore splitTotalEnergy:startDate:endDate:resultsHandler:]_block_invoke.606
+ ___69-[HKHealthStore recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.387
+ ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.626
+ ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke.512
+ ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke_2.513
+ ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.569
+ ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.569.cold.1
+ ___72-[HKHealthStoreImplementation pluginServiceEndpointForIdentifier:error:]_block_invoke.389
+ ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.611
+ ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.611.cold.1
+ ___79-[HKHealthStore requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.414
+ ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke.304
+ ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke_2.305
+ ___83-[HKHealthStoreImplementation recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.403
+ ___84-[HKHealthStore requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.421
+ ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.645
+ ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.369
+ ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.370
+ ___93-[HKHealthStoreImplementation requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.429
+ ___98-[HKHealthStoreImplementation requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.436
+ ___Block_byref_object_copy_.133
+ ___Block_byref_object_dispose_.134
+ ___block_descriptor_32_e38_"HKSleepPeriod"16?0"HKSleepPeriod"8l
+ ___block_literal_global.127
+ ___block_literal_global.134
+ ___block_literal_global.138
+ ___block_literal_global.142
+ ___block_literal_global.303
+ ___block_literal_global.327
+ ___block_literal_global.342
+ ___block_literal_global.425
+ ___block_literal_global.434
+ ___block_literal_global.440
+ ___block_literal_global.471
+ ___block_literal_global.479
+ ___block_literal_global.486
+ ___block_literal_global.494
+ ___block_literal_global.535
+ ___block_literal_global.537
+ ___block_literal_global.539
+ ___block_literal_global.541
+ ___block_literal_global.550
+ ___block_literal_global.555
+ ___block_literal_global.557
+ ___block_literal_global.559
+ ___block_literal_global.568
+ ___block_literal_global.576
+ ___block_literal_global.582
+ ___block_literal_global.592
+ ___block_literal_global.594
+ ___block_literal_global.600
+ ___block_literal_global.610
+ ___block_literal_global.611
+ ___block_literal_global.615
+ ___block_literal_global.617
+ ___block_literal_global.619
+ ___block_literal_global.621
+ ___block_literal_global.623
+ ___block_literal_global.630
+ ___block_literal_global.632
+ ___block_literal_global.634
+ ___block_literal_global.636
+ ___block_literal_global.638
+ ___block_literal_global.640
+ ___block_literal_global.642
+ _objc_msgSend$_updatingPeriods:
+ _objc_msgSend$durationsForStrategyType:
+ _objc_msgSend$predicateForObjectsWithMetadataKey:allowedValues:
+ _objc_msgSend$primarySleepPeriodUsingSummaryDurationStrategyType:
+ _objc_msgSend$sleepPeriodWithDateInterval:segments:isIncomplete:timezoneName:
+ _objc_msgSend$summaryFilteredWithOptions:
+ _objc_msgSend$summaryFilteredWithOptions:strategyType:
+ _objc_msgSend$timezoneName
+ _symbolic SaySo17HKSleepDaySummaryCGSaySo0abC10CollectionCGIeghgo_
+ _symbolic So22HKSleepDaySummaryQueryCSaySo0abC10CollectionCG______pSgIeghggg_ s5ErrorP
+ _symbolic So22HKSleepDaySummaryQueryCSo7NSArrayCSo7NSErrorCSgIeyBhyyy_
+ _symbolic So32HKSleepDaySummaryCollectionQueryCXDXMT
- +[HKSleepPeriod sleepPeriodWithDateInterval:segments:isIncomplete:]
- -[HKSleepDaySummary _defaultStrategy]
- -[HKSleepDaySummary _filterToPeriod:]
- -[HKSleepDaySummaryDurationCollection durationsForStrategy:]
- -[HKSleepDaySummaryDurationCollection durationsForStrategy:].cold.1
- -[_HKFeatureFlags consistentLogging]
- -[_HKFeatureFlags setConsistentLogging:]
- GCC_except_table124
- GCC_except_table144
- GCC_except_table57
- _OBJC_IVAR_$__HKFeatureFlags._consistentLogging
- __DATA__TtC9HealthKit32HKSleepDaySummaryCollectionQuery
- __IVARS__TtC9HealthKit32HKSleepDaySummaryCollectionQuery
- __METACLASS_DATA__TtC9HealthKit32HKSleepDaySummaryCollectionQuery
- ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.388
- ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.389
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.309
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.317
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.310
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.310.cold.1
- ___129-[HKHealthStore fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.378
- ___143-[HKHealthStoreImplementation fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.394
- ___33-[HKHealthStore dropEntitlement:]_block_invoke.633
- ___34-[HKHealthStore _supportsFeature:]_block_invoke.536
- ___34-[HKHealthStore _supportsFeature:]_block_invoke.536.cold.1
- ___34-[HKWorkoutBuilder discardWorkout]_block_invoke_2
- ___34-[HKWorkoutBuilder discardWorkout]_block_invoke_2.cold.1
- ___36-[HKHealthStore restoreEntitlement:]_block_invoke.634
- ___36-[_HKFeatureFlags consistentLogging]_block_invoke
- ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.254
- ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.254.cold.1
- ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.256
- ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.256.cold.1
- ___43-[HKWorkoutBuilder _pushCurrentTargetState]_block_invoke.81
- ___43-[HKWorkoutBuilder _pushCurrentTargetState]_block_invoke.81.cold.1
- ___43-[HKWorkoutBuilder _recoverWithCompletion:]_block_invoke.257
- ___43-[HKWorkoutBuilder _recoverWithCompletion:]_block_invoke.257.cold.1
- ___44-[HKHealthStore authorizationStatusForType:]_block_invoke.405
- ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.652
- ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.553
- ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.553.cold.1
- ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.653
- ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke.510
- ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke_2.511
- ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.554
- ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.554.cold.1
- ___58-[HKHealthStore pluginServiceEndpointForIdentifier:error:]_block_invoke.376
- ___58-[HKHealthStoreImplementation authorizationStatusForType:]_block_invoke.421
- ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.596
- ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.596.cold.1
- ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.303
- ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.304
- ___66-[HKWorkoutBuilder clientRemote_stateDidChange:startDate:endDate:]_block_invoke.134
- ___67-[HKHealthStore splitTotalEnergy:startDate:endDate:resultsHandler:]_block_invoke.609
- ___69-[HKHealthStore recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.390
- ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.629
- ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke.515
- ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke_2.516
- ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.572
- ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.572.cold.1
- ___72-[HKHealthStoreImplementation pluginServiceEndpointForIdentifier:error:]_block_invoke.392
- ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.614
- ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.614.cold.1
- ___79-[HKHealthStore requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.417
- ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke.307
- ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke_2.308
- ___83-[HKHealthServicesManager _setHealthPeripheralOrServicesStatus:enabled:completion:]_block_invoke_2
- ___83-[HKHealthServicesManager _setHealthPeripheralOrServicesStatus:enabled:completion:]_block_invoke_3
- ___83-[HKHealthStoreImplementation recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.406
- ___84-[HKHealthStore requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.424
- ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.648
- ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.372
- ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.373
- ___93-[HKHealthStoreImplementation requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.432
- ___98-[HKHealthStoreImplementation requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.439
- ___Block_byref_object_copy_.132
- ___Block_byref_object_dispose_.133
- ___block_descriptor_49_e8_32s40bs_e43_v16?0"<HKHealthServicesServerInterface>"8ls32l8s40l8
- ___block_descriptor_57_e8_32s40bs48w_e20_v20?0B8"NSError"12ls40l8w48l8s32l8
- ___block_literal_global.131
- ___block_literal_global.136
- ___block_literal_global.306
- ___block_literal_global.330
- ___block_literal_global.345
- ___block_literal_global.428
- ___block_literal_global.437
- ___block_literal_global.443
- ___block_literal_global.474
- ___block_literal_global.482
- ___block_literal_global.489
- ___block_literal_global.497
- ___block_literal_global.538
- ___block_literal_global.540
- ___block_literal_global.542
- ___block_literal_global.544
- ___block_literal_global.556
- ___block_literal_global.558
- ___block_literal_global.560
- ___block_literal_global.562
- ___block_literal_global.571
- ___block_literal_global.579
- ___block_literal_global.585
- ___block_literal_global.597
- ___block_literal_global.598
- ___block_literal_global.603
- ___block_literal_global.614
- ___block_literal_global.620
- ___block_literal_global.622
- ___block_literal_global.624
- ___block_literal_global.626
- ___block_literal_global.633
- ___block_literal_global.635
- ___block_literal_global.637
- ___block_literal_global.639
- ___block_literal_global.641
- ___block_literal_global.643
- ___block_literal_global.645
- _objc_msgSend$_defaultStrategy
- _objc_msgSend$_filterToPeriod:
- _objc_msgSend$durationsForStrategy:
- _objc_msgSend$primarySleepPeriod
- _objc_msgSend$remote_setEnabledStatus:forPeripheral:withCompletion:
- _objc_msgSend$sleepPeriodWithDateInterval:segments:isIncomplete:
- _objc_msgSend$strategyForType:
- _symbolic SNy_____G 9HealthKit8DayIndexV
- _symbolic SaySo17HKSleepDaySummaryCGSay_____GIeghgo_ 9HealthKit27HKSleepDaySummaryCollectionV
- _symbolic So22HKSleepDaySummaryQueryC
- _symbolic So22HKSleepDaySummaryQueryCSay_____GIeghgg_ 9HealthKit27HKSleepDaySummaryCollectionV
- _symbolic _____ 9HealthKit27HKSleepDaySummaryCollectionV
- _symbolic _____ 9HealthKit32HKSleepDaySummaryCollectionQueryC
- _symbolic _____XDXMT 9HealthKit32HKSleepDaySummaryCollectionQueryC
- _type_layout_string 9HealthKit27HKSleepDaySummaryCollectionV
CStrings:
+ "%{public}@: Enqueing discarding workout"
+ "%{public}@: Enqueing finish workout"
+ "%{public}@: Enqueuing begin collection event"
+ "%{public}@: Enqueuing end collection"
+ "%{public}@: Enqueuing state event %li"
+ ", (incomplete)"
+ ", timezone = %@"
+ "<%@:%p (%@ - %@), segments = %@"
+ "@\"HKSleepPeriod\"16@?0@\"HKSleepPeriod\"8"
+ "@40@0:8{?=qq}16@?32"
+ "@44@0:8@16@24B32@36"
+ "CBPeripheral for identifier %{public}@ does not have UpdateHealth property"
+ "HKSleepDaySummaryCollection"
+ "HKSleepDaySummaryCollectionQuery"
+ "HealthKit_Private.HKSleepDaySummaryCollection"
+ "HealthKit_Private.HKSleepDaySummaryCollectionQuery"
+ "T@\"HKSleepDaySummaryQuery\",N,R,Vquery"
+ "T@\"NSString\",R,C,N,V_timezoneName"
+ "Td,N,R"
+ "Timezone"
+ "_HKPrivateSmoothedRouteWorkoutAssociatedUUID"
+ "_timezoneName"
+ "_updatingPeriods:"
+ "durationsForStrategyType:"
+ "initWithMorningIndexRange:resultsHandler:"
+ "initWithSleepDaySummaries:"
+ "numberOfNonEmptySleepDaySummaries"
+ "predicateForWorkoutRoutesUsingMetadataForWorkout:"
+ "primarySleepPeriodUsingSummaryDurationStrategyType:"
+ "sleepDaySummaries"
+ "sleepPeriodWithDateInterval:segments:isIncomplete:timezoneName:"
+ "summaryFilteredWithOptions:"
+ "summaryFilteredWithOptions:strategyType:"
+ "timezoneName"
+ "totalAwakeDuration"
+ "totalCoreSleepDuration"
+ "totalDeepSleepDuration"
+ "totalInBedDuration"
+ "totalREMSleepDuration"
+ "totalTimeAsleepDuration"
- "<%@:%p (%@ - %@), segments = %@, (incomplete)>"
- "<%@:%p (%@ - %@), segments = %@>"
- "_TtC9HealthKit32HKSleepDaySummaryCollectionQuery"
- "_consistentLogging"
- "_defaultStrategy"
- "_filterToPeriod:"
- "consistentLogging"
- "setConsistentLogging:"
- "sleepPeriodWithDateInterval:segments:isIncomplete:"

```
