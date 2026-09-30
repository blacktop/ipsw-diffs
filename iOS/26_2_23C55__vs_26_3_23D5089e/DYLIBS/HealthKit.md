## HealthKit

> `/System/Library/Frameworks/HealthKit.framework/HealthKit`

```diff

-6200.3.10.2.1
-  __TEXT.__text: 0x3494f0
+6200.4.4.0.0
+  __TEXT.__text: 0x3494f4
   __TEXT.__auth_stubs: 0x3790
   __TEXT.__objc_methlist: 0x3043c
   __TEXT.__cstring: 0x36d93
-  __TEXT.__const: 0x11ff02
+  __TEXT.__const: 0x1338f2
   __TEXT.__oslogstring: 0xc773
   __TEXT.__gcc_except_tab: 0x42a4
   __TEXT.__ustring: 0x78

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 034CC1A1-56C8-3E59-9618-5C5A7F69FC1A
+  UUID: 4CD7E499-41C3-3936-AD84-F15542C64016
   Functions: 24376
   Symbols:   61508
   CStrings:  30589
Symbols:
+ ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.388
+ ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.389
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.309
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.317
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.310
+ ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.310.cold.1
+ ___129-[HKHealthStore fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.378
+ ___143-[HKHealthStoreImplementation fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.394
+ ___33-[HKHealthStore dropEntitlement:]_block_invoke.632
+ ___34-[HKHealthStore _supportsFeature:]_block_invoke.533
+ ___34-[HKHealthStore _supportsFeature:]_block_invoke.533.cold.1
+ ___36-[HKHealthStore restoreEntitlement:]_block_invoke.633
+ ___44-[HKHealthStore authorizationStatusForType:]_block_invoke.405
+ ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.651
+ ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.550
+ ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.550.cold.1
+ ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.652
+ ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke.507
+ ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke_2.508
+ ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.551
+ ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.551.cold.1
+ ___58-[HKHealthStore pluginServiceEndpointForIdentifier:error:]_block_invoke.376
+ ___58-[HKHealthStoreImplementation authorizationStatusForType:]_block_invoke.421
+ ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.593
+ ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.593.cold.1
+ ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.303
+ ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.304
+ ___67-[HKHealthStore splitTotalEnergy:startDate:endDate:resultsHandler:]_block_invoke.606
+ ___69-[HKHealthStore recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.390
+ ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.626
+ ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke.512
+ ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke_2.513
+ ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.569
+ ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.569.cold.1
+ ___72-[HKHealthStoreImplementation pluginServiceEndpointForIdentifier:error:]_block_invoke.392
+ ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.611
+ ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.611.cold.1
+ ___79-[HKHealthStore requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.417
+ ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke.307
+ ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke_2.308
+ ___83-[HKHealthStoreImplementation recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.406
+ ___84-[HKHealthStore requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.425
+ ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.645
+ ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.372
+ ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.373
+ ___93-[HKHealthStoreImplementation requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.432
+ ___98-[HKHealthStoreImplementation requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.440
+ ___block_literal_global.306
+ ___block_literal_global.330
+ ___block_literal_global.345
+ ___block_literal_global.429
+ ___block_literal_global.437
+ ___block_literal_global.444
+ ___block_literal_global.471
+ ___block_literal_global.479
+ ___block_literal_global.486
+ ___block_literal_global.494
+ ___block_literal_global.535
+ ___block_literal_global.537
+ ___block_literal_global.539
+ ___block_literal_global.541
+ ___block_literal_global.553
+ ___block_literal_global.555
+ ___block_literal_global.557
+ ___block_literal_global.576
+ ___block_literal_global.582
+ ___block_literal_global.592
+ ___block_literal_global.594
+ ___block_literal_global.595
+ ___block_literal_global.600
+ ___block_literal_global.610
+ ___block_literal_global.611
+ ___block_literal_global.613
+ ___block_literal_global.615
+ ___block_literal_global.617
+ ___block_literal_global.621
+ ___block_literal_global.623
+ ___block_literal_global.634
+ ___block_literal_global.636
+ ___block_literal_global.638
+ ___block_literal_global.640
+ ___block_literal_global.642
- ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.397
- ___100-[HKHealthStoreImplementation fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.398
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.318
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke.326
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.319
- ___110-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithLocalInformation:shouldRequery:queryParams:returnTypes:]_block_invoke_2.319.cold.1
- ___129-[HKHealthStore fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.387
- ___143-[HKHealthStoreImplementation fetchTaskServerEndpointForIdentifier:pluginURL:taskUUID:instanceUUID:configuration:endpointHandler:errorHandler:]_block_invoke.403
- ___33-[HKHealthStore dropEntitlement:]_block_invoke.641
- ___34-[HKHealthStore _supportsFeature:]_block_invoke.542
- ___34-[HKHealthStore _supportsFeature:]_block_invoke.542.cold.1
- ___36-[HKHealthStore restoreEntitlement:]_block_invoke.642
- ___44-[HKHealthStore authorizationStatusForType:]_block_invoke.414
- ___47-[HKHealthStoreImplementation dropEntitlement:]_block_invoke.660
- ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.559
- ___48-[HKHealthStoreImplementation _supportsFeature:]_block_invoke.559.cold.1
- ___50-[HKHealthStoreImplementation restoreEntitlement:]_block_invoke.661
- ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke.516
- ___51-[HKHealthStore _deleteObjects:options:completion:]_block_invoke_2.517
- ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.560
- ___56-[HKHealthStore setWorkoutSessionMirroringStartHandler:]_block_invoke.560.cold.1
- ___58-[HKHealthStore pluginServiceEndpointForIdentifier:error:]_block_invoke.385
- ___58-[HKHealthStoreImplementation authorizationStatusForType:]_block_invoke.430
- ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.602
- ___59-[HKHealthStore _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.602.cold.1
- ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.312
- ___63-[_HKMobileAssetDownloadManager removeMobileAssets:completion:]_block_invoke.313
- ___67-[HKHealthStore splitTotalEnergy:startDate:endDate:resultsHandler:]_block_invoke.615
- ___69-[HKHealthStore recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.399
- ___70-[HKHealthStore clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.635
- ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke.521
- ___70-[HKHealthStore deleteObjectsOfType:predicate:options:withCompletion:]_block_invoke_2.522
- ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.578
- ___70-[HKHealthStoreImplementation setWorkoutSessionMirroringStartHandler:]_block_invoke.578.cold.1
- ___72-[HKHealthStoreImplementation pluginServiceEndpointForIdentifier:error:]_block_invoke.401
- ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.620
- ___73-[HKHealthStoreImplementation _closeTransactionWithTypes:anchor:ackTime:]_block_invoke.620.cold.1
- ___79-[HKHealthStore requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.426
- ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke.316
- ___82-[_HKMobileAssetDownloadManager _queue_fetchAssetsWithQuery:onlyLocal:completion:]_block_invoke_2.317
- ___83-[HKHealthStoreImplementation recalibrateEstimatesForSampleType:atDate:completion:]_block_invoke.415
- ___84-[HKHealthStore requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.434
- ___84-[HKHealthStoreImplementation clientRemote_didCreateRemoteSessionWithConfiguration:]_block_invoke.654
- ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.381
- ___86-[HKHealthStore fetchPluginServiceEndpointForIdentifier:endpointHandler:errorHandler:]_block_invoke.382
- ___93-[HKHealthStoreImplementation requestPerObjectReadAuthorizationForType:predicate:completion:]_block_invoke.441
- ___98-[HKHealthStoreImplementation requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.449
- ___block_literal_global.315
- ___block_literal_global.339
- ___block_literal_global.354
- ___block_literal_global.438
- ___block_literal_global.446
- ___block_literal_global.453
- ___block_literal_global.480
- ___block_literal_global.488
- ___block_literal_global.495
- ___block_literal_global.503
- ___block_literal_global.544
- ___block_literal_global.546
- ___block_literal_global.548
- ___block_literal_global.562
- ___block_literal_global.564
- ___block_literal_global.566
- ___block_literal_global.577
- ___block_literal_global.585
- ___block_literal_global.591
- ___block_literal_global.601
- ___block_literal_global.603
- ___block_literal_global.604
- ___block_literal_global.609
- ___block_literal_global.620
- ___block_literal_global.622
- ___block_literal_global.624
- ___block_literal_global.626
- ___block_literal_global.637
- ___block_literal_global.639
- ___block_literal_global.641
- ___block_literal_global.643
- ___block_literal_global.645
- ___block_literal_global.649
- ___block_literal_global.651
- ___block_literal_global.656
Functions:
~ -[_HKBehavior _setSharedBehaviors] : 284 -> 288

```
