## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-6100.0.0.0.0
-  __TEXT.__text: 0x333b08
+6105.0.0.0.0
+  __TEXT.__text: 0x332420
   __TEXT.__auth_stubs: 0x36d0
-  __TEXT.__objc_methlist: 0x2f8cc
-  __TEXT.__cstring: 0x34b43
-  __TEXT.__const: 0xabf22
-  __TEXT.__oslogstring: 0xc1f3
-  __TEXT.__gcc_except_tab: 0x40b0
+  __TEXT.__objc_methlist: 0x2f8d4
+  __TEXT.__cstring: 0x34c03
+  __TEXT.__const: 0xabfa2
+  __TEXT.__oslogstring: 0xc203
+  __TEXT.__gcc_except_tab: 0x4064
   __TEXT.__ustring: 0x78
   __TEXT.__dlopen_cstrs: 0x5da
   __TEXT.__constg_swiftt: 0x2fa4

   __TEXT.__swift_as_ret: 0x14c
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0xf940
+  __TEXT.__unwind_info: 0xf8a0
   __TEXT.__eh_frame: 0x3fe8
-  __TEXT.__objc_classname: 0x8970
-  __TEXT.__objc_methname: 0x5d543
+  __TEXT.__objc_classname: 0x8971
+  __TEXT.__objc_methname: 0x5d599
   __TEXT.__objc_methtype: 0xbf29
-  __TEXT.__objc_stubs: 0x2b1e0
-  __DATA_CONST.__got: 0x1b10
-  __DATA_CONST.__const: 0xf478
+  __TEXT.__objc_stubs: 0x2b200
+  __DATA_CONST.__got: 0x1b08
+  __DATA_CONST.__const: 0xf460
   __DATA_CONST.__objc_classlist: 0x1aa8
   __DATA_CONST.__objc_catlist: 0x1c0
   __DATA_CONST.__objc_protolist: 0x7f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11318
+  __DATA_CONST.__objc_selrefs: 0x11330
   __DATA_CONST.__objc_protorefs: 0x608
   __DATA_CONST.__objc_superrefs: 0x1728
   __DATA_CONST.__objc_arraydata: 0x68e8
   __AUTH_CONST.__auth_got: 0x1b80
-  __AUTH_CONST.__const: 0xb950
-  __AUTH_CONST.__cfstring: 0x32020
-  __AUTH_CONST.__objc_const: 0x4fbd8
+  __AUTH_CONST.__const: 0xbfb8
+  __AUTH_CONST.__cfstring: 0x32080
+  __AUTH_CONST.__objc_const: 0x4fc48
   __AUTH_CONST.__objc_intobj: 0x4590
   __AUTH_CONST.__objc_dictobj: 0x488
   __AUTH_CONST.__objc_doubleobj: 0x140
   __AUTH_CONST.__objc_arrayobj: 0x6d8
-  __AUTH.__objc_data: 0xeaa0
+  __AUTH.__objc_data: 0xea50
   __AUTH.__data: 0x1938
-  __DATA.__objc_ivar: 0x2dc0
+  __DATA.__objc_ivar: 0x2dcc
   __DATA.__data: 0xce58
-  __DATA.__bss: 0x182c0
-  __DATA.__common: 0x9a8
-  __DATA_DIRTY.__objc_data: 0x2430
+  __DATA.__bss: 0x182a0
+  __DATA.__common: 0x9a0
+  __DATA_DIRTY.__objc_data: 0x2480
   __DATA_DIRTY.__data: 0x130
-  __DATA_DIRTY.__bss: 0xc90
-  __DATA_DIRTY.__common: 0xd0
+  __DATA_DIRTY.__bss: 0xca8
+  __DATA_DIRTY.__common: 0xd8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 23C090F1-50E8-3837-83D6-5183510B8B7A
-  Functions: 23917
-  Symbols:   60710
-  CStrings:  29721
+  UUID: 2CBA4922-3CDF-3A2B-9478-FECE6B5E8876
+  Functions: 23885
+  Symbols:   60630
+  CStrings:  29739
 
Symbols:
+ -[HKLiveWorkoutBuilder _lock_updateElapsedTimeCache]
+ -[HKLiveWorkoutBuilder _lock_updateEvents:]
+ -[HKWorkoutBuilder _lock_canAddMetadataInCurrentState]
+ -[HKWorkoutBuilder _lock_endDateForSnapshotWithStartDate:]
+ -[HKWorkoutBuilder _lock_eventsBetweenStartDate:endDate:]
+ -[HKWorkoutBuilder _lock_freezeSeriesBuilders]
+ -[HKWorkoutBuilder _lock_markRecoveryRequired]
+ -[HKWorkoutBuilder _lock_seriesBuilderWithIdentifier:type:]
+ -[HKWorkoutBuilder _lock_startDateForSnapshot]
+ -[HKWorkoutBuilder _lock_updateDevice:]
+ -[HKWorkoutBuilder _lock_updateElapsedTimeCache]
+ -[HKWorkoutBuilder _lock_updateEvents:]
+ -[HKWorkoutBuilder _queue_addMetadata:completion:]
+ -[HKWorkoutBuilder _queue_addSamples:completion:]
+ -[HKWorkoutBuilder _queue_addWorkoutActivity:completion:]
+ -[HKWorkoutBuilder _queue_addWorkoutEvents:completion:]
+ -[HKWorkoutBuilder _queue_beginCollectionWithStartDate:completion:]
+ -[HKWorkoutBuilder _queue_endCollectionWithEndDate:completion:]
+ -[HKWorkoutBuilder _queue_finishWorkoutWithCompletion:]
+ -[HKWorkoutBuilder _queue_removeMetadata:completion:]
+ -[HKWorkoutBuilder _queue_setStatisticsComputationMethod:forType:]
+ -[HKWorkoutBuilder _queue_setStatisticsMergeStrategy:forType:]
+ -[HKWorkoutBuilder _queue_updateActivityWithUUID:addMetadata:completion:]
+ -[HKWorkoutBuilder _queue_updateActivityWithUUID:endDate:completion:]
+ -[HKWorkoutBuilder lock_seriesBuilders]
+ -[HKWorkoutBuilder lock_statisticsByType]
+ -[HKWorkoutBuilder setLock_seriesBuilders:]
+ -[HKWorkoutBuilder setLock_statisticsByType:]
+ -[_HKFeatureFlags workoutSavingQueryPerf]
+ -[_HKFeatureFlags workoutTempTableChanges]
+ GCC_except_table127
+ GCC_except_table144
+ OBJC_IVAR_$_HKWorkoutBuilder._lock
+ _OBJC_IVAR_$_HKLiveWorkoutBuilder._lock_additionalDataSources
+ _OBJC_IVAR_$_HKLiveWorkoutBuilder._lock_dataSource
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_accumulatedElapsedTime
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_activitiesPerUUID
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_constructionStateMachine
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_currentlyRunning
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_lastResumeTimestamp
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_metadata
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_seriesBuilders
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_serverConstructionState
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_statisticsByType
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_workoutEndDate
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_workoutEvents
+ _OBJC_IVAR_$_HKWorkoutBuilder._lock_workoutStartDate
+ _OBJC_IVAR_$_HKWorkoutBuilder._queue
+ _OBJC_IVAR_$__HKFeatureFlags._workoutSavingQueryPerf
+ _OBJC_IVAR_$__HKFeatureFlags._workoutTempTableChanges
+ ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.388
+ ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.389
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.309
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.317
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.310
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.310.cold.1
+ ___129-[HKHealthStore fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.378
+ ___143-[HKHealthStoreImplementation fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.394
+ ___33-[HKHealthStore dropEntitlement:]_block_invoke.633
+ ___34-[HKHealthStore _supportsFeature:]_block_invoke.536
+ ___34-[HKHealthStore _supportsFeature:]_block_invoke.536.cold.1
+ ___36-[HKHealthStore restoreEntitlement:]_block_invoke.634
+ ___38-[HKLiveWorkoutBuilder setDataSource:]_block_invoke_2.cold.1
+ ___39-[HKWorkoutBuilder _lock_updateDevice:]_block_invoke
+ ___39-[HKWorkoutBuilder _lock_updateDevice:]_block_invoke_2
+ ___39-[HKWorkoutBuilder _lock_updateDevice:]_block_invoke_2.cold.1
+ ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.252
+ ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.252.cold.1
+ ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.254
+ ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.254.cold.1
+ ___41-[_HKFeatureFlags workoutSavingQueryPerf]_block_invoke
+ ___42-[_HKFeatureFlags workoutTempTableChanges]_block_invoke
+ ___43-[HKLiveWorkoutBuilder _lock_updateEvents:]_block_invoke
+ ___43-[HKWorkoutBuilder _pushCurrentTargetState]_block_invoke_2.cold.1
+ ___43-[HKWorkoutBuilder _recoverWithCompletion:]_block_invoke.255
+ ___43-[HKWorkoutBuilder _recoverWithCompletion:]_block_invoke.255.cold.1
+ ___44-[HKHealthStore authorizationStatusForType:]_block_invoke.405
+ ___45-[HKLiveWorkoutBuilder connectionInterrupted]_block_invoke_2.cold.1
+ ___46-[HKWorkoutBuilder _lock_freezeSeriesBuilders]_block_invoke
+ ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.652
+ ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.553
+ ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.553.cold.1
+ ___49-[HKLiveWorkoutBuilder setAdditionalDataSources:]_block_invoke_4.cold.1
+ ___49-[HKWorkoutBuilder _queue_addSamples:completion:]_block_invoke
+ ___49-[HKWorkoutBuilder _queue_addSamples:completion:]_block_invoke_2
+ ___49-[HKWorkoutBuilder _queue_addSamples:completion:]_block_invoke_3
+ ___49-[HKWorkoutBuilder _queue_addSamples:completion:]_block_invoke_4
+ ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.653
+ ___50-[HKWorkoutBuilder _queue_addMetadata:completion:]_block_invoke
+ ___50-[HKWorkoutBuilder _queue_addMetadata:completion:]_block_invoke_2
+ ___50-[HKWorkoutBuilder _queue_addMetadata:completion:]_block_invoke_3
+ ___50-[HKWorkoutBuilder _queue_addMetadata:completion:]_block_invoke_4
+ ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke.510
+ ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke_2.511
+ ___52-[HKLiveWorkoutBuilder _lock_updateElapsedTimeCache]_block_invoke
+ ___53-[HKWorkoutBuilder _queue_removeMetadata:completion:]_block_invoke
+ ___53-[HKWorkoutBuilder _queue_removeMetadata:completion:]_block_invoke_2
+ ___53-[HKWorkoutBuilder _queue_removeMetadata:completion:]_block_invoke_3
+ ___53-[HKWorkoutBuilder _queue_removeMetadata:completion:]_block_invoke_4
+ ___54-[HKLiveWorkoutBuilder setShouldCollectWorkoutEvents:]_block_invoke_2.cold.1
+ ___55-[HKWorkoutBuilder _queue_addWorkoutEvents:completion:]_block_invoke
+ ___55-[HKWorkoutBuilder _queue_addWorkoutEvents:completion:]_block_invoke_2
+ ___55-[HKWorkoutBuilder _queue_addWorkoutEvents:completion:]_block_invoke_3
+ ___55-[HKWorkoutBuilder _queue_addWorkoutEvents:completion:]_block_invoke_4
+ ___55-[HKWorkoutBuilder _queue_finishWorkoutWithCompletion:]_block_invoke
+ ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.554
+ ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.554.cold.1
+ ___57-[HKWorkoutBuilder _lock_eventsBetweenStartDate:endDate:]_block_invoke
+ ___57-[HKWorkoutBuilder _queue_addWorkoutActivity:completion:]_block_invoke
+ ___57-[HKWorkoutBuilder _queue_addWorkoutActivity:completion:]_block_invoke_2
+ ___57-[HKWorkoutBuilder _queue_addWorkoutActivity:completion:]_block_invoke_3
+ ___57-[HKWorkoutBuilder _queue_addWorkoutActivity:completion:]_block_invoke_4
+ ___58-[HKHealthStore pluginServiceEndpointForIdentifier:error:]_block_invoke.376
+ ___58-[HKHealthStoreImplementation authorizationStatusForType:]_block_invoke.421
+ ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.596
+ ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.596.cold.1
+ ___62-[HKWorkoutBuilder _queue_setStatisticsMergeStrategy:forType:]_block_invoke
+ ___62-[HKWorkoutBuilder _queue_setStatisticsMergeStrategy:forType:]_block_invoke_2
+ ___62-[HKWorkoutBuilder _queue_setStatisticsMergeStrategy:forType:]_block_invoke_2.cold.1
+ ___63-[HKWorkoutBuilder _queue_endCollectionWithEndDate:completion:]_block_invoke
+ ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.303
+ ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.304
+ ___66-[HKWorkoutBuilder _queue_setStatisticsComputationMethod:forType:]_block_invoke
+ ___66-[HKWorkoutBuilder _queue_setStatisticsComputationMethod:forType:]_block_invoke_2
+ ___66-[HKWorkoutBuilder _queue_setStatisticsComputationMethod:forType:]_block_invoke_2.cold.1
+ ___67-[HKHealthStore splitTotalEnergy:startDate:endDate:resultsHandler:]_block_invoke.609
+ ___67-[HKWorkoutBuilder _queue_beginCollectionWithStartDate:completion:]_block_invoke
+ ___69-[HKHealthStore recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.390
+ ___69-[HKWorkoutBuilder _queue_updateActivityWithUUID:endDate:completion:]_block_invoke
+ ___69-[HKWorkoutBuilder _queue_updateActivityWithUUID:endDate:completion:]_block_invoke_2
+ ___69-[HKWorkoutBuilder _queue_updateActivityWithUUID:endDate:completion:]_block_invoke_3
+ ___69-[HKWorkoutBuilder _queue_updateActivityWithUUID:endDate:completion:]_block_invoke_4
+ ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.629
+ ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke.515
+ ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke_2.516
+ ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.572
+ ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.572.cold.1
+ ___72-[HKHealthStoreImplementation pluginServiceEndpointForIdentifier:error:]_block_invoke.392
+ ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.614
+ ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.614.cold.1
+ ___73-[HKWorkoutBuilder _queue_updateActivityWithUUID:addMetadata:completion:]_block_invoke
+ ___73-[HKWorkoutBuilder _queue_updateActivityWithUUID:addMetadata:completion:]_block_invoke_2
+ ___73-[HKWorkoutBuilder _queue_updateActivityWithUUID:addMetadata:completion:]_block_invoke_3
+ ___73-[HKWorkoutBuilder _queue_updateActivityWithUUID:addMetadata:completion:]_block_invoke_4
+ ___79-[HKHealthStore requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.417
+ ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke.307
+ ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke_2.308
+ ___83-[HKHealthStoreImplementation recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.406
+ ___84-[HKHealthStore requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.424
+ ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.648
+ ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.372
+ ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.373
+ ___89-[HKSleepDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.27
+ ___89-[HKSleepDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.27.cold.1
+ ___93-[HKHealthStoreImplementation requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.432
+ ___98-[HKHealthStoreImplementation requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.439
+ ___block_literal_global.131
+ ___block_literal_global.140
+ ___block_literal_global.306
+ ___block_literal_global.330
+ ___block_literal_global.345
+ ___block_literal_global.428
+ ___block_literal_global.437
+ ___block_literal_global.443
+ ___block_literal_global.474
+ ___block_literal_global.482
+ ___block_literal_global.489
+ ___block_literal_global.497
+ ___block_literal_global.538
+ ___block_literal_global.540
+ ___block_literal_global.542
+ ___block_literal_global.544
+ ___block_literal_global.556
+ ___block_literal_global.558
+ ___block_literal_global.560
+ ___block_literal_global.562
+ ___block_literal_global.571
+ ___block_literal_global.579
+ ___block_literal_global.585
+ ___block_literal_global.597
+ ___block_literal_global.598
+ ___block_literal_global.603
+ ___block_literal_global.614
+ ___block_literal_global.620
+ ___block_literal_global.622
+ ___block_literal_global.624
+ ___block_literal_global.626
+ ___block_literal_global.633
+ ___block_literal_global.635
+ ___block_literal_global.637
+ ___block_literal_global.639
+ ___block_literal_global.641
+ ___block_literal_global.643
+ ___block_literal_global.645
+ ___block_literal_global.76
+ ___block_literal_global.78
+ ___swift_assignWithCopy_strong
+ ___swift_assignWithTake_strong
+ ___swift_destroy_strong
+ ___swift_initWithCopy_strong
+ ___unnamed_22
+ ___unnamed_23
+ _kHKSessionTrackerAppPreferencesDomain
+ _kHKWorkoutMirroringSetting
+ _objc_msgSend$_lock_canAddMetadataInCurrentState
+ _objc_msgSend$_lock_endDateForSnapshotWithStartDate:
+ _objc_msgSend$_lock_eventsBetweenStartDate:endDate:
+ _objc_msgSend$_lock_freezeSeriesBuilders
+ _objc_msgSend$_lock_markRecoveryRequired
+ _objc_msgSend$_lock_seriesBuilderWithIdentifier:type:
+ _objc_msgSend$_lock_startDateForSnapshot
+ _objc_msgSend$_lock_updateDevice:
+ _objc_msgSend$_lock_updateElapsedTimeCache
+ _objc_msgSend$_lock_updateEvents:
+ _objc_msgSend$_queue_addMetadata:completion:
+ _objc_msgSend$_queue_addSamples:completion:
+ _objc_msgSend$_queue_addWorkoutActivity:completion:
+ _objc_msgSend$_queue_addWorkoutEvents:completion:
+ _objc_msgSend$_queue_beginCollectionWithStartDate:completion:
+ _objc_msgSend$_queue_endCollectionWithEndDate:completion:
+ _objc_msgSend$_queue_finishWorkoutWithCompletion:
+ _objc_msgSend$_queue_removeMetadata:completion:
+ _objc_msgSend$_queue_setStatisticsComputationMethod:forType:
+ _objc_msgSend$_queue_setStatisticsMergeStrategy:forType:
+ _objc_msgSend$_queue_updateActivityWithUUID:addMetadata:completion:
+ _objc_msgSend$_queue_updateActivityWithUUID:endDate:completion:
- -[HKLiveWorkoutBuilder _resourceQueue_updateElapsedTimeCache]
- -[HKLiveWorkoutBuilder _resourceQueue_updateEvents:]
- -[HKWorkoutBuilder _resourceQueue_addMetadata:completion:]
- -[HKWorkoutBuilder _resourceQueue_addSamples:completion:]
- -[HKWorkoutBuilder _resourceQueue_addWorkoutActivity:completion:]
- -[HKWorkoutBuilder _resourceQueue_addWorkoutEvents:completion:]
- -[HKWorkoutBuilder _resourceQueue_beginCollectionWithStartDate:completion:]
- -[HKWorkoutBuilder _resourceQueue_canAddMetadataInCurrentState]
- -[HKWorkoutBuilder _resourceQueue_endCollectionWithEndDate:completion:]
- -[HKWorkoutBuilder _resourceQueue_endDateForSnapshotWithStartDate:]
- -[HKWorkoutBuilder _resourceQueue_eventsBetweenStartDate:endDate:]
- -[HKWorkoutBuilder _resourceQueue_finishWorkoutWithCompletion:]
- -[HKWorkoutBuilder _resourceQueue_freezeSeriesBuilders]
- -[HKWorkoutBuilder _resourceQueue_markRecoveryRequired]
- -[HKWorkoutBuilder _resourceQueue_removeMetadata:completion:]
- -[HKWorkoutBuilder _resourceQueue_seriesBuilderWithIdentifier:type:]
- -[HKWorkoutBuilder _resourceQueue_setStatisticsComputationMethod:forType:]
- -[HKWorkoutBuilder _resourceQueue_setStatisticsMergeStrategy:forType:]
- -[HKWorkoutBuilder _resourceQueue_startDateForSnapshot]
- -[HKWorkoutBuilder _resourceQueue_updateActivityWithUUID:addMetadata:completion:]
- -[HKWorkoutBuilder _resourceQueue_updateActivityWithUUID:endDate:completion:]
- -[HKWorkoutBuilder _resourceQueue_updateDevice:]
- -[HKWorkoutBuilder _resourceQueue_updateElapsedTimeCache]
- -[HKWorkoutBuilder _resourceQueue_updateEvents:]
- -[HKWorkoutBuilder resourceQueue]
- -[HKWorkoutBuilder seriesBuilders]
- -[HKWorkoutBuilder setSeriesBuilders:]
- -[HKWorkoutBuilder setStatisticsByType:]
- -[HKWorkoutBuilder statisticsByType]
- GCC_except_table117
- GCC_except_table120
- GCC_except_table184
- GCC_except_table222
- GCC_except_table68
- _OBJC_IVAR_$_HKLiveWorkoutBuilder._additionalDataSources
- _OBJC_IVAR_$_HKLiveWorkoutBuilder._dataSource
- _OBJC_IVAR_$_HKWorkoutBuilder._accumulatedElapsedTime
- _OBJC_IVAR_$_HKWorkoutBuilder._activitiesPerUUID
- _OBJC_IVAR_$_HKWorkoutBuilder._constructionStateMachine
- _OBJC_IVAR_$_HKWorkoutBuilder._currentlyRunning
- _OBJC_IVAR_$_HKWorkoutBuilder._lastResumeTimestamp
- _OBJC_IVAR_$_HKWorkoutBuilder._metadata
- _OBJC_IVAR_$_HKWorkoutBuilder._resourceQueue
- _OBJC_IVAR_$_HKWorkoutBuilder._seriesBuilders
- _OBJC_IVAR_$_HKWorkoutBuilder._serverConstructionState
- _OBJC_IVAR_$_HKWorkoutBuilder._statisticsByType
- _OBJC_IVAR_$_HKWorkoutBuilder._workoutEndDate
- _OBJC_IVAR_$_HKWorkoutBuilder._workoutEvents
- _OBJC_IVAR_$_HKWorkoutBuilder._workoutStartDate
- ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.385
- ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.386
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.306
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.314
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.307
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.307.cold.1
- ___129-[HKHealthStore fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.375
- ___143-[HKHealthStoreImplementation fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.391
- ___27-[HKWorkoutBuilder endDate]_block_invoke
- ___28-[HKWorkoutBuilder metadata]_block_invoke
- ___29-[HKWorkoutBuilder startDate]_block_invoke
- ___31-[HKWorkoutBuilder _setDevice:]_block_invoke
- ___33-[HKHealthStore dropEntitlement:]_block_invoke.630
- ___33-[HKWorkoutBuilder allStatistics]_block_invoke
- ___33-[HKWorkoutBuilder workoutEvents]_block_invoke
- ___34-[HKHealthStore _supportsFeature:]_block_invoke.533
- ___34-[HKHealthStore _supportsFeature:]_block_invoke.533.cold.1
- ___34-[HKLiveWorkoutBuilder dataSource]_block_invoke
- ___36-[HKHealthStore restoreEntitlement:]_block_invoke.631
- ___36-[HKWorkoutBuilder _currentSnapshot]_block_invoke
- ___37-[HKWorkoutBuilder workoutActivities]_block_invoke_2
- ___38-[HKLiveWorkoutBuilder setDataSource:]_block_invoke_3
- ___38-[HKLiveWorkoutBuilder setDataSource:]_block_invoke_3.cold.1
- ___38-[HKWorkoutBuilder elapsedTimeAtDate:]_block_invoke
- ___38-[HKWorkoutBuilder isCurrentlyRunning]_block_invoke
- ___38-[HKWorkoutBuilder statisticsForType:]_block_invoke
- ___39-[HKWorkoutBuilder _currentElapsedTime]_block_invoke
- ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.255
- ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.255.cold.1
- ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.257
- ___41-[HKWorkoutBuilder connectionInterrupted]_block_invoke.257.cold.1
- ___41-[HKWorkoutBuilder seriesBuilderForType:]_block_invoke
- ___43-[HKWorkoutBuilder _pushCurrentTargetState]_block_invoke_3
- ___43-[HKWorkoutBuilder _pushCurrentTargetState]_block_invoke_3.cold.1
- ___43-[HKWorkoutBuilder _recoverWithCompletion:]_block_invoke.258
- ___43-[HKWorkoutBuilder _recoverWithCompletion:]_block_invoke.258.cold.1
- ___44-[HKHealthStore authorizationStatusForType:]_block_invoke.402
- ___45-[HKLiveWorkoutBuilder additionalDataSources]_block_invoke
- ___45-[HKLiveWorkoutBuilder connectionInterrupted]_block_invoke_2.107
- ___45-[HKLiveWorkoutBuilder connectionInterrupted]_block_invoke_2.107.cold.1
- ___46-[HKLiveWorkoutBuilder currentWorkoutActivity]_block_invoke
- ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.649
- ___47-[HKWorkoutBuilder unitTest_setFailureHandler:]_block_invoke
- ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.550
- ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.550.cold.1
- ___48-[HKWorkoutBuilder _resourceQueue_updateDevice:]_block_invoke
- ___48-[HKWorkoutBuilder _resourceQueue_updateDevice:]_block_invoke_2
- ___48-[HKWorkoutBuilder _resourceQueue_updateDevice:]_block_invoke_2.cold.1
- ___48-[HKWorkoutBuilder clientRemote_didEndActivity:]_block_invoke
- ___49-[HKLiveWorkoutBuilder setAdditionalDataSources:]_block_invoke_5
- ___49-[HKLiveWorkoutBuilder setAdditionalDataSources:]_block_invoke_5.cold.1
- ___49-[HKWorkoutBuilder clientRemote_didUpdateEvents:]_block_invoke_2
- ___49-[HKWorkoutBuilder clientRemote_finishedWorkout:]_block_invoke_2
- ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.650
- ___50-[HKLiveWorkoutBuilder shouldCollectWorkoutEvents]_block_invoke
- ___50-[HKWorkoutBuilder clientRemote_didBeginActivity:]_block_invoke
- ___50-[HKWorkoutBuilder clientRemote_didFailWithError:]_block_invoke_5
- ___50-[HKWorkoutBuilder clientRemote_didFinishRecovery]_block_invoke
- ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke.507
- ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke_2.508
- ___51-[HKWorkoutBuilder clientRemote_didUpdateMetadata:]_block_invoke
- ___52-[HKLiveWorkoutBuilder _resourceQueue_updateEvents:]_block_invoke
- ___53-[HKWorkoutBuilder clientRemote_didUpdateActivities:]_block_invoke
- ___53-[HKWorkoutBuilder clientRemote_didUpdateStatistics:]_block_invoke
- ___54-[HKLiveWorkoutBuilder setShouldCollectWorkoutEvents:]_block_invoke_3
- ___54-[HKLiveWorkoutBuilder setShouldCollectWorkoutEvents:]_block_invoke_3.cold.1
- ___55-[HKWorkoutBuilder _resourceQueue_freezeSeriesBuilders]_block_invoke
- ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.551
- ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.551.cold.1
- ___56-[HKWorkoutBuilder unitTest_setRecoveryFinishedHandler:]_block_invoke
- ___57-[HKWorkoutBuilder _resourceQueue_addSamples:completion:]_block_invoke
- ___57-[HKWorkoutBuilder _resourceQueue_addSamples:completion:]_block_invoke_2
- ___57-[HKWorkoutBuilder _resourceQueue_addSamples:completion:]_block_invoke_3
- ___57-[HKWorkoutBuilder _resourceQueue_addSamples:completion:]_block_invoke_4
- ___57-[HKWorkoutBuilder unitTest_setServerStateChangeHandler:]_block_invoke
- ___58-[HKHealthStore pluginServiceEndpointForIdentifier:error:]_block_invoke.373
- ___58-[HKHealthStoreImplementation authorizationStatusForType:]_block_invoke.418
- ___58-[HKWorkoutBuilder _resourceQueue_addMetadata:completion:]_block_invoke
- ___58-[HKWorkoutBuilder _resourceQueue_addMetadata:completion:]_block_invoke_2
- ___58-[HKWorkoutBuilder _resourceQueue_addMetadata:completion:]_block_invoke_3
- ___58-[HKWorkoutBuilder _resourceQueue_addMetadata:completion:]_block_invoke_4
- ___58-[HKWorkoutBuilder clientRemote_didRecoverSeriesBuilders:]_block_invoke
- ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.593
- ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.593.cold.1
- ___59-[HKWorkoutBuilder clientRemote_synchronizeWithCompletion:]_block_invoke
- ___59-[HKWorkoutBuilder unitTest_setDidFinishFinalizingHandler:]_block_invoke
- ___61-[HKLiveWorkoutBuilder _resourceQueue_updateElapsedTimeCache]_block_invoke
- ___61-[HKWorkoutBuilder _resourceQueue_removeMetadata:completion:]_block_invoke
- ___61-[HKWorkoutBuilder _resourceQueue_removeMetadata:completion:]_block_invoke_2
- ___61-[HKWorkoutBuilder _resourceQueue_removeMetadata:completion:]_block_invoke_3
- ___61-[HKWorkoutBuilder _resourceQueue_removeMetadata:completion:]_block_invoke_4
- ___63-[HKWorkoutBuilder _resourceQueue_addWorkoutEvents:completion:]_block_invoke
- ___63-[HKWorkoutBuilder _resourceQueue_addWorkoutEvents:completion:]_block_invoke_2
- ___63-[HKWorkoutBuilder _resourceQueue_addWorkoutEvents:completion:]_block_invoke_3
- ___63-[HKWorkoutBuilder _resourceQueue_addWorkoutEvents:completion:]_block_invoke_4
- ___63-[HKWorkoutBuilder _resourceQueue_finishWorkoutWithCompletion:]_block_invoke
- ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.300
- ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.301
- ___65-[HKWorkoutBuilder _resourceQueue_addWorkoutActivity:completion:]_block_invoke
- ___65-[HKWorkoutBuilder _resourceQueue_addWorkoutActivity:completion:]_block_invoke_2
- ___65-[HKWorkoutBuilder _resourceQueue_addWorkoutActivity:completion:]_block_invoke_3
- ___65-[HKWorkoutBuilder _resourceQueue_addWorkoutActivity:completion:]_block_invoke_4
- ___66-[HKWorkoutBuilder _resourceQueue_eventsBetweenStartDate:endDate:]_block_invoke
- ___66-[HKWorkoutBuilder _restoreRecoveredSeriesBuildersWithCompletion:]_block_invoke_3
- ___66-[HKWorkoutBuilder clientRemote_stateDidChange:startDate:endDate:]_block_invoke.135
- ___67-[HKHealthStore splitTotalEnergy:startDate:endDate:resultsHandler:]_block_invoke.606
- ___69-[HKHealthStore recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.387
- ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.626
- ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke.512
- ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke_2.513
- ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.569
- ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.569.cold.1
- ___70-[HKWorkoutBuilder _resourceQueue_setStatisticsMergeStrategy:forType:]_block_invoke
- ___70-[HKWorkoutBuilder _resourceQueue_setStatisticsMergeStrategy:forType:]_block_invoke_2
- ___70-[HKWorkoutBuilder _resourceQueue_setStatisticsMergeStrategy:forType:]_block_invoke_2.cold.1
- ___71-[HKWorkoutBuilder _resourceQueue_endCollectionWithEndDate:completion:]_block_invoke
- ___72-[HKHealthStoreImplementation pluginServiceEndpointForIdentifier:error:]_block_invoke.389
- ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.611
- ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.611.cold.1
- ___74-[HKWorkoutBuilder _resourceQueue_setStatisticsComputationMethod:forType:]_block_invoke
- ___74-[HKWorkoutBuilder _resourceQueue_setStatisticsComputationMethod:forType:]_block_invoke_2
- ___74-[HKWorkoutBuilder _resourceQueue_setStatisticsComputationMethod:forType:]_block_invoke_2.cold.1
- ___75-[HKWorkoutBuilder _resourceQueue_beginCollectionWithStartDate:completion:]_block_invoke
- ___77-[HKWorkoutBuilder _resourceQueue_updateActivityWithUUID:endDate:completion:]_block_invoke
- ___77-[HKWorkoutBuilder _resourceQueue_updateActivityWithUUID:endDate:completion:]_block_invoke_2
- ___77-[HKWorkoutBuilder _resourceQueue_updateActivityWithUUID:endDate:completion:]_block_invoke_3
- ___77-[HKWorkoutBuilder _resourceQueue_updateActivityWithUUID:endDate:completion:]_block_invoke_4
- ___79-[HKHealthStore requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.414
- ___79-[HKWorkoutBuilder initWithHealthStore:builderConfiguration:builderIdentifier:]_block_invoke
- ___80-[HKWorkoutBuilder clientRemote_didChangeElapsedTimeBasisWithStartDate:endDate:]_block_invoke
- ___81-[HKWorkoutBuilder _resourceQueue_updateActivityWithUUID:addMetadata:completion:]_block_invoke
- ___81-[HKWorkoutBuilder _resourceQueue_updateActivityWithUUID:addMetadata:completion:]_block_invoke_2
- ___81-[HKWorkoutBuilder _resourceQueue_updateActivityWithUUID:addMetadata:completion:]_block_invoke_3
- ___81-[HKWorkoutBuilder _resourceQueue_updateActivityWithUUID:addMetadata:completion:]_block_invoke_4
- ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke.304
- ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke_2.305
- ___83-[HKHealthStoreImplementation recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.403
- ___84-[HKHealthStore requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.421
- ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.645
- ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.369
- ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.370
- ___89-[HKSleepDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.24
- ___89-[HKSleepDaySummaryQuery client_deliverDaySummaries:clearPending:isFinalBatch:queryUUID:]_block_invoke.24.cold.1
- ___93-[HKHealthStoreImplementation requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.429
- ___98-[HKHealthStoreImplementation requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.436
- ___Block_byref_object_copy_.133
- ___Block_byref_object_dispose_.134
- ___block_descriptor_72_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
- ___block_literal_global.138
- ___block_literal_global.142
- ___block_literal_global.303
- ___block_literal_global.327
- ___block_literal_global.342
- ___block_literal_global.425
- ___block_literal_global.434
- ___block_literal_global.440
- ___block_literal_global.471
- ___block_literal_global.479
- ___block_literal_global.486
- ___block_literal_global.494
- ___block_literal_global.535
- ___block_literal_global.537
- ___block_literal_global.539
- ___block_literal_global.541
- ___block_literal_global.550
- ___block_literal_global.555
- ___block_literal_global.557
- ___block_literal_global.559
- ___block_literal_global.568
- ___block_literal_global.576
- ___block_literal_global.582
- ___block_literal_global.592
- ___block_literal_global.594
- ___block_literal_global.600
- ___block_literal_global.610
- ___block_literal_global.611
- ___block_literal_global.615
- ___block_literal_global.617
- ___block_literal_global.619
- ___block_literal_global.621
- ___block_literal_global.623
- ___block_literal_global.630
- ___block_literal_global.632
- ___block_literal_global.634
- ___block_literal_global.636
- ___block_literal_global.638
- ___block_literal_global.640
- ___block_literal_global.642
- ___block_literal_global.79
- ___unnamed_21
- _objc_msgSend$_resourceQueue_addSamples:completion:
- _objc_msgSend$_resourceQueue_addWorkoutActivity:completion:
- _objc_msgSend$_resourceQueue_addWorkoutEvents:completion:
- _objc_msgSend$_resourceQueue_beginCollectionWithStartDate:completion:
- _objc_msgSend$_resourceQueue_canAddMetadataInCurrentState
- _objc_msgSend$_resourceQueue_endCollectionWithEndDate:completion:
- _objc_msgSend$_resourceQueue_endDateForSnapshotWithStartDate:
- _objc_msgSend$_resourceQueue_eventsBetweenStartDate:endDate:
- _objc_msgSend$_resourceQueue_finishWorkoutWithCompletion:
- _objc_msgSend$_resourceQueue_freezeSeriesBuilders
- _objc_msgSend$_resourceQueue_markRecoveryRequired
- _objc_msgSend$_resourceQueue_removeMetadata:completion:
- _objc_msgSend$_resourceQueue_seriesBuilderWithIdentifier:type:
- _objc_msgSend$_resourceQueue_setStatisticsComputationMethod:forType:
- _objc_msgSend$_resourceQueue_setStatisticsMergeStrategy:forType:
- _objc_msgSend$_resourceQueue_startDateForSnapshot
- _objc_msgSend$_resourceQueue_updateActivityWithUUID:addMetadata:completion:
- _objc_msgSend$_resourceQueue_updateActivityWithUUID:endDate:completion:
- _objc_msgSend$_resourceQueue_updateDevice:
- _objc_msgSend$_resourceQueue_updateElapsedTimeCache
- _objc_msgSend$_resourceQueue_updateEvents:
- _xmlFree
CStrings:
+ "@\"HKSleepDaySummaryQuery\""
+ "Event start date: %{public}@ is in future for date: %{public}@"
+ "T@\"NSMutableDictionary\",&,N,V_lock_seriesBuilders"
+ "T@\"NSMutableDictionary\",&,N,V_lock_statisticsByType"
+ "WorkoutMirroringSetting"
+ "WorkoutSavingQueryPerf"
+ "WorkoutTempTableChanges"
+ "_lock_accumulatedElapsedTime"
+ "_lock_activitiesPerUUID"
+ "_lock_additionalDataSources"
+ "_lock_canAddMetadataInCurrentState"
+ "_lock_constructionStateMachine"
+ "_lock_currentlyRunning"
+ "_lock_dataSource"
+ "_lock_endDateForSnapshotWithStartDate:"
+ "_lock_eventsBetweenStartDate:endDate:"
+ "_lock_freezeSeriesBuilders"
+ "_lock_lastResumeTimestamp"
+ "_lock_markRecoveryRequired"
+ "_lock_metadata"
+ "_lock_seriesBuilderWithIdentifier:type:"
+ "_lock_seriesBuilders"
+ "_lock_serverConstructionState"
+ "_lock_startDateForSnapshot"
+ "_lock_statisticsByType"
+ "_lock_updateDevice:"
+ "_lock_updateElapsedTimeCache"
+ "_lock_updateEvents:"
+ "_lock_workoutEndDate"
+ "_lock_workoutEvents"
+ "_lock_workoutStartDate"
+ "_queue_addMetadata:completion:"
+ "_queue_addSamples:completion:"
+ "_queue_addWorkoutActivity:completion:"
+ "_queue_addWorkoutEvents:completion:"
+ "_queue_beginCollectionWithStartDate:completion:"
+ "_queue_endCollectionWithEndDate:completion:"
+ "_queue_finishWorkoutWithCompletion:"
+ "_queue_removeMetadata:completion:"
+ "_queue_setStatisticsComputationMethod:forType:"
+ "_queue_setStatisticsMergeStrategy:forType:"
+ "_queue_updateActivityWithUUID:addMetadata:completion:"
+ "_queue_updateActivityWithUUID:endDate:completion:"
+ "_workoutSavingQueryPerf"
+ "_workoutTempTableChanges"
+ "com.apple.nanolifestyle.sessiontrackerapp"
+ "lock_seriesBuilders"
+ "lock_statisticsByType"
+ "setLock_seriesBuilders:"
+ "setLock_statisticsByType:"
+ "surfacePeriodTimezones"
+ "workoutSavingQueryPerf"
+ "workoutTempTableChanges"
- "Event start date: %{public}@ is in future"
- "T@\"NSMutableDictionary\",&,N,V_seriesBuilders"
- "T@\"NSMutableDictionary\",&,N,V_statisticsByType"
- "_accumulatedElapsedTime"
- "_activitiesPerUUID"
- "_additionalDataSources"
- "_constructionStateMachine"
- "_currentlyRunning"
- "_lastResumeTimestamp"
- "_resourceQueue_addSamples:completion:"
- "_resourceQueue_addWorkoutActivity:completion:"
- "_resourceQueue_addWorkoutEvents:completion:"
- "_resourceQueue_beginCollectionWithStartDate:completion:"
- "_resourceQueue_canAddMetadataInCurrentState"
- "_resourceQueue_endCollectionWithEndDate:completion:"
- "_resourceQueue_endDateForSnapshotWithStartDate:"
- "_resourceQueue_eventsBetweenStartDate:endDate:"
- "_resourceQueue_finishWorkoutWithCompletion:"
- "_resourceQueue_freezeSeriesBuilders"
- "_resourceQueue_markRecoveryRequired"
- "_resourceQueue_removeMetadata:completion:"
- "_resourceQueue_seriesBuilderWithIdentifier:type:"
- "_resourceQueue_setStatisticsComputationMethod:forType:"
- "_resourceQueue_setStatisticsMergeStrategy:forType:"
- "_resourceQueue_startDateForSnapshot"
- "_resourceQueue_updateActivityWithUUID:addMetadata:completion:"
- "_resourceQueue_updateActivityWithUUID:endDate:completion:"
- "_resourceQueue_updateDevice:"
- "_resourceQueue_updateElapsedTimeCache"
- "_resourceQueue_updateEvents:"
- "_seriesBuilders"
- "_serverConstructionState"
- "_statisticsByType"
- "_workoutEndDate"
- "_workoutStartDate"
- "seriesBuilders"
- "setSeriesBuilders:"
- "setStatisticsByType:"
- "statisticsByType"

```
