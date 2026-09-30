## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1062.0.1.0.1
-  __TEXT.__text: 0x5ee0dc
+1067.0.2.0.0
+  __TEXT.__text: 0x60b3bc
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x31038
+  __TEXT.__objc_methlist: 0x310e0
   __TEXT.__const: 0x4658
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x76586
-  __TEXT.__cstring: 0x454a7
+  __TEXT.__oslogstring: 0x768b4
+  __TEXT.__cstring: 0x45669
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c

   __TEXT.__swift5_reflstr: 0x14
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x28af4
+  __TEXT.__gcc_except_tab: 0x28cb8
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xdc78
+  __TEXT.__unwind_info: 0xdcb0
   __TEXT.__eh_frame: 0x390
   __TEXT.__objc_classname: 0x58ca
-  __TEXT.__objc_methname: 0x915e9
-  __TEXT.__objc_methtype: 0xcfa5
-  __TEXT.__objc_stubs: 0x55b00
+  __TEXT.__objc_methname: 0x9184b
+  __TEXT.__objc_methtype: 0xcfd0
+  __TEXT.__objc_stubs: 0x55ba0
   __DATA_CONST.__got: 0x30f8
-  __DATA_CONST.__const: 0xf538
+  __DATA_CONST.__const: 0xf550
   __DATA_CONST.__objc_classlist: 0x1548
   __DATA_CONST.__objc_catlist: 0x3a8
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19428
+  __DATA_CONST.__objc_selrefs: 0x19480
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x1198
-  __DATA_CONST.__objc_arraydata: 0x2a00
+  __DATA_CONST.__objc_arraydata: 0x2a10
   __AUTH_CONST.__auth_got: 0x10d8
-  __AUTH_CONST.__const: 0x3260
-  __AUTH_CONST.__cfstring: 0x28880
+  __AUTH_CONST.__const: 0x3240
+  __AUTH_CONST.__cfstring: 0x28a40
   __AUTH_CONST.__objc_const: 0x50a60
   __AUTH_CONST.__objc_intobj: 0x4608
-  __AUTH_CONST.__objc_arrayobj: 0xe70
+  __AUTH_CONST.__objc_arrayobj: 0xe88
   __AUTH_CONST.__objc_doubleobj: 0xb00
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_floatobj: 0x10

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F78E139F-AD2C-322D-BBE6-B6217C03F8C3
-  Functions: 20187
-  Symbols:   65174
-  CStrings:  40164
+  UUID: 1C850A04-E36F-35AA-A68F-55547CE308D0
+  Functions: 20204
+  Symbols:   65214
+  CStrings:  40218
 
Symbols:
+ +[RTStore exceptionHandlingPolicyToString:]
+ +[RTStore handleCoreDataException:outError:]
+ -[RTFeatureExtractor _fetchLocationsOfInterestWithPlaceTypes:handler:]
+ -[RTFeatureExtractor _getLOIsUUIDsFromVisits:]
+ -[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]
+ -[RTLearnedLocationManager fetchLocationsOfInterestWithIdentifiers:handler:]
+ -[RTLearnedLocationStore _fetchLocationsOfInterestWithIdentifiers:handler:]
+ -[RTLearnedLocationStore _learnedLocationsOfInterestFromLearnedLocationsOfInterestMO:context:includeVisits:includeTransitions:]
+ -[RTLearnedLocationStore bulkFetchMapItemMOsByIdentifiers:context:error:]
+ -[RTLearnedLocationStore fetchLocationsOfInterestWithIdentifiers:handler:]
+ -[RTLearnedLocationStore placeMapItemIdentifiersFromLearnedLocationsOfInterestMO:]
+ -[RTPersistenceMirroringManager _countChangesInTransactionsFromContext:store:startingToken:error:]
+ -[RTPersistenceMirroringManager _fetchHistoryTransactionBatchFromContext:store:fromToken:limit:error:]
+ -[RTPredictedContextManager _createXPCActivityCriteriaWithInterval:gracePeriod:allowBattery:requiresClassA:requiresClassB:delay:]
+ -[RTPredictedContextManager _migrateLegacyTrainPolicyFromInteger:]
+ GCC_except_table168
+ GCC_except_table244
+ GCC_except_table267
+ GCC_except_table274
+ GCC_except_table284
+ GCC_except_table296
+ GCC_except_table299
+ GCC_except_table319
+ GCC_except_table351
+ GCC_except_table437
+ ___101-[RTLearnedLocationStore _fetchCountOfVisitsToLocationOfInterestWithIdentifier:dateInterval:handler:]_block_invoke.286
+ ___119-[RTTripClusterManager purgeClustersDatabaseWithTripClusterStore:tripClusterRouteStore:tripClusterRoadTransitionStore:]_block_invoke.455
+ ___119-[RTTripClusterManager purgeClustersDatabaseWithTripClusterStore:tripClusterRouteStore:tripClusterRoadTransitionStore:]_block_invoke.456
+ ___127-[RTLearnedLocationStore _learnedLocationsOfInterestFromLearnedLocationsOfInterestMO:context:includeVisits:includeTransitions:]_block_invoke
+ ___144-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:includePlaceholders:includeVisits:includeTransitions:handler:]_block_invoke.360
+ ___144-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:includePlaceholders:includeVisits:includeTransitions:handler:]_block_invoke.362
+ ___43-[RTPredictedContextManager _storeRequest:]_block_invoke.493
+ ___47-[RTLearnedLocationStore _removePlace:handler:]_block_invoke.448
+ ___48-[RTFeatureExtractor _getHomeKitHomesWithError:]_block_invoke.449
+ ___53-[RTLearnedLocationStore _fetchLastVisitWithHandler:]_block_invoke.274
+ ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.486
+ ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.489
+ ___54-[RTLearnedLocationStore _fetchVisitsToPlace:handler:]_block_invoke.262
+ ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.445
+ ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.446
+ ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.447
+ ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.448
+ ___55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.572
+ ___59-[RTLearnedLocationStore _fetchVisitIdentifiersIn:handler:]_block_invoke.294
+ ___59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.598
+ ___59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.594
+ ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.188
+ ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.192
+ ___63-[RTTripClusterManager _fetchLearnedRoutesWithOptions:handler:]_block_invoke.427
+ ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.467
+ ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.469
+ ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.470
+ ___66-[RTFeatureExtractor _getCalendarEventsWithDateInterval:outError:]_block_invoke.438
+ ___66-[RTLearnedLocationStore _fetchMapItemWithMuid:predicate:handler:]_block_invoke.428
+ ___66-[RTLearnedLocationStore _removeRecordsExpiredBeforeDate:handler:]_block_invoke.540
+ ___68+[RTMapItemMO updateDatabaseWithMapItem:managedObjectContext:error:]_block_invoke.60
+ ___68-[RTFeatureExtractor _getMapsViewedPlacesWithDateInterval:outError:]_block_invoke.443
+ ___68-[RTFeatureExtractor _getMotionActivitiesWithDateInterval:outError:]_block_invoke.445
+ ___68-[RTLearnedLocationStore _fetchLocationOfInterestWithPlace:handler:]_block_invoke.395
+ ___69-[RTFeatureExtractor _getLocationHistoriesWithDateInterval:outError:]_block_invoke.436
+ ___70-[RTFeatureExtractor _fetchLocationsOfInterestWithPlaceTypes:handler:]_block_invoke
+ ___70-[RTLearnedLocationStore _fetchLocationOfInterestWithMapItem:handler:]_block_invoke.391
+ ___70-[RTLearnedLocationStore _fetchVisitsOverlappingDateInterval:handler:]_block_invoke.273
+ ___71-[RTFeatureExtractor _getLocationsOfInterestWithDateInterval:outError:]_block_invoke.434
+ ___71-[RTLearnedLocationStore _fetchLastVisitToPlaceWithIdentifier:handler:]_block_invoke.278
+ ___73-[RTLearnedLocationStore _fetchLocationOfInterestVisitedLastWithHandler:]_block_invoke.386
+ ___73-[RTLearnedLocationStore _fetchLocationOfInterestWithIdentifier:handler:]_block_invoke.387
+ ___73-[RTLearnedLocationStore _fetchLocationsOfInterestWithPlaceType:handler:]_block_invoke.338
+ ___74-[RTLearnedLocationStore _fetchInferredMapItemForVisitIdentifier:handler:]_block_invoke.384
+ ___74-[RTLearnedLocationStore _fetchLocationOfInterestVisitedFirstWithHandler:]_block_invoke.385
+ ___74-[RTLearnedLocationStore fetchLocationsOfInterestWithIdentifiers:handler:]_block_invoke
+ ___75-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:handler:]_block_invoke.279
+ ___75-[RTLearnedLocationStore _fetchLocationsOfInterestUUIDsVisitedWithHandler:]_block_invoke.363
+ ___75-[RTLearnedLocationStore _fetchLocationsOfInterestWithIdentifiers:handler:]_block_invoke
+ ___75-[RTLearnedLocationStore _fetchLocationsOfInterestWithIdentifiers:handler:]_block_invoke.248
+ ___76-[RTLearnedLocationManager fetchLocationsOfInterestWithIdentifiers:handler:]_block_invoke
+ ___76-[RTLearnedLocationStore _fetchTransitionsBetweenStartDate:endDate:handler:]_block_invoke.308
+ ___76-[RTLearnedLocationStore _fetchVisitsWithPredicate:ascending:limit:handler:]_block_invoke.255
+ ___77-[RTFeatureExtractor _getMapsHistoricalNavigationsWithDateInterval:outError:]_block_invoke.441
+ ___83-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:endDate:handler:]_block_invoke.290
+ ___83-[RTLearnedLocationStore _fetchLocationsOfInterestWithinDistance:location:handler:]_block_invoke.334
+ ___85-[RTTripClusterManager _findRouteFromCurrentLocation:options:queryStartTime:handler:]_block_invoke.352
+ ___86-[RTLearnedLocationStore _fetchVisitsWithIncompletePlacesForCurrentDeviceWithHandler:]_block_invoke.421
+ ___91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.573
+ ___94-[RTLearnedLocationStore _fetchLocationOfInterestTransitionsBetweenStartDate:endDate:handler:]_block_invoke.408
+ ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke
+ ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.421
+ ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.425
+ ___97-[RTFeatureExtractor _getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:]_block_invoke.427
+ ___block_descriptor_66_e8_32s40s48s56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e34_v24?0"NSDictionary"8"NSError"16lr40l8r48l8r56l8r64l8s32l8
+ ___block_descriptor_83_e8_32s40s48s56bs_e32_v16?0"NSManagedObjectContext"8ls32l8s40l8s56l8s48l8
+ ___block_literal_global.251
+ ___block_literal_global.322
+ ___block_literal_global.341
+ ___block_literal_global.409
+ ___block_literal_global.414
+ ___block_literal_global.460
+ ___block_literal_global.619
+ ___block_literal_global.728
+ ___block_literal_global.923
+ _kRTPredictedContextMetricsKeyLastTrainingResultMask
+ _kRTPredictedContextMetricsKeyTrainingTimeSinceLastSuccess
+ _objc_msgSend$_countChangesInTransactionsFromContext:store:startingToken:error:
+ _objc_msgSend$_createXPCActivityCriteriaWithInterval:gracePeriod:allowBattery:requiresClassA:requiresClassB:delay:
+ _objc_msgSend$_fetchHistoryTransactionBatchFromContext:store:fromToken:limit:error:
+ _objc_msgSend$_fetchLocationsOfInterestWithIdentifiers:handler:
+ _objc_msgSend$_getLOIsUUIDsFromVisits:
+ _objc_msgSend$_getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:
+ _objc_msgSend$_learnedLocationsOfInterestFromLearnedLocationsOfInterestMO:context:includeVisits:includeTransitions:
+ _objc_msgSend$_migrateLegacyTrainPolicyFromInteger:
+ _objc_msgSend$bulkFetchMapItemMOsByIdentifiers:context:error:
+ _objc_msgSend$exceptionHandlingPolicyToString:
+ _objc_msgSend$fetchLocationsOfInterestWithIdentifiers:handler:
+ _objc_msgSend$handleCoreDataException:outError:
+ _objc_msgSend$placeMapItemIdentifiersFromLearnedLocationsOfInterestMO:
- -[RTPersistenceMirroringManager _countChangesInTransactionsFromContext:store:predicate:error:]
- -[RTPersistenceMirroringManager _fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:]
- GCC_except_table166
- GCC_except_table204
- GCC_except_table218
- GCC_except_table236
- GCC_except_table240
- GCC_except_table265
- GCC_except_table266
- GCC_except_table272
- GCC_except_table282
- GCC_except_table294
- GCC_except_table297
- GCC_except_table311
- GCC_except_table343
- GCC_except_table421
- ___101-[RTLearnedLocationStore _fetchCountOfVisitsToLocationOfInterestWithIdentifier:dateInterval:handler:]_block_invoke.285
- ___119-[RTTripClusterManager purgeClustersDatabaseWithTripClusterStore:tripClusterRouteStore:tripClusterRoadTransitionStore:]_block_invoke.459
- ___119-[RTTripClusterManager purgeClustersDatabaseWithTripClusterStore:tripClusterRouteStore:tripClusterRoadTransitionStore:]_block_invoke.460
- ___144-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:includePlaceholders:includeVisits:includeTransitions:handler:]_block_invoke.343
- ___144-[RTLearnedLocationStore _fetchLocationsOfInterestVisitedBetweenStartDate:endDate:includePlaceholders:includeVisits:includeTransitions:handler:]_block_invoke_2
- ___43-[RTPredictedContextManager _storeRequest:]_block_invoke.487
- ___46-[RTTripClusterManager computeCloudSyncMetric]_block_invoke.243
- ___46-[RTTripClusterManager computeCloudSyncMetric]_block_invoke.245
- ___46-[RTTripClusterManager computeCloudSyncMetric]_block_invoke.246
- ___47-[RTLearnedLocationStore _removePlace:handler:]_block_invoke.431
- ___48-[RTFeatureExtractor _getHomeKitHomesWithError:]_block_invoke.437
- ___53-[RTLearnedLocationStore _fetchLastVisitWithHandler:]_block_invoke.273
- ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.480
- ___53-[RTPredictedContextManager _filterResult:forClient:]_block_invoke.483
- ___54-[RTLearnedLocationStore _fetchVisitsToPlace:handler:]_block_invoke.261
- ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.455
- ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.456
- ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.457
- ___54-[RTTripClusterManager purgeTripClusterTable:handler:]_block_invoke.458
- ___55-[RTLearnedLocationStore __removeUnreferencedMapItems:]_block_invoke.558
- ___59-[RTLearnedLocationStore _fetchVisitIdentifiersIn:handler:]_block_invoke.293
- ___59-[RTLearnedLocationStore _logCloudStoreWithReason:handler:]_block_invoke.588
- ___59-[RTLearnedLocationStore _logLocalStoreWithReason:handler:]_block_invoke.584
- ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.179
- ___60-[RTStore _fetchReadableObjectsOfType:fetchRequest:handler:]_block_invoke.183
- ___63-[RTTripClusterManager _fetchLearnedRoutesWithOptions:handler:]_block_invoke.431
- ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.457
- ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.458
- ___64-[RTPredictedContextMetricsManager _onDailyMetricsNotification:]_block_invoke.459
- ___64-[RTPredictedContextMetricsManager prepareInferenceEventMetric:]_block_invoke
- ___66-[RTFeatureExtractor _getCalendarEventsWithDateInterval:outError:]_block_invoke.426
- ___66-[RTLearnedLocationStore _fetchMapItemWithMuid:predicate:handler:]_block_invoke.410
- ___66-[RTLearnedLocationStore _removeRecordsExpiredBeforeDate:handler:]_block_invoke.523
- ___68+[RTMapItemMO updateDatabaseWithMapItem:managedObjectContext:error:]_block_invoke.54
- ___68-[RTFeatureExtractor _getMapsViewedPlacesWithDateInterval:outError:]_block_invoke.431
- ___68-[RTFeatureExtractor _getMotionActivitiesWithDateInterval:outError:]_block_invoke.433
- ___68-[RTLearnedLocationStore _fetchLocationOfInterestWithPlace:handler:]_block_invoke.377
- ___69-[RTFeatureExtractor _getLocationHistoriesWithDateInterval:outError:]_block_invoke.424
- ___70-[RTLearnedLocationStore _fetchLocationOfInterestWithMapItem:handler:]_block_invoke.373
- ___70-[RTLearnedLocationStore _fetchVisitsOverlappingDateInterval:handler:]_block_invoke.272
- ___71-[RTFeatureExtractor _getLocationsOfInterestWithDateInterval:outError:]_block_invoke.421
- ___71-[RTLearnedLocationStore _fetchLastVisitToPlaceWithIdentifier:handler:]_block_invoke.277
- ___73-[RTLearnedLocationStore _fetchLocationOfInterestVisitedLastWithHandler:]_block_invoke.368
- ___73-[RTLearnedLocationStore _fetchLocationOfInterestWithIdentifier:handler:]_block_invoke.369
- ___73-[RTLearnedLocationStore _fetchLocationsOfInterestWithPlaceType:handler:]_block_invoke.327
- ___74-[RTLearnedLocationStore _fetchInferredMapItemForVisitIdentifier:handler:]_block_invoke.366
- ___74-[RTLearnedLocationStore _fetchLocationOfInterestVisitedFirstWithHandler:]_block_invoke.367
- ___75-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:handler:]_block_invoke.278
- ___75-[RTLearnedLocationStore _fetchLocationsOfInterestUUIDsVisitedWithHandler:]_block_invoke.345
- ___76-[RTLearnedLocationStore _fetchTransitionsBetweenStartDate:endDate:handler:]_block_invoke.307
- ___76-[RTLearnedLocationStore _fetchVisitsWithPredicate:ascending:limit:handler:]_block_invoke.254
- ___77-[RTFeatureExtractor _getMapsHistoricalNavigationsWithDateInterval:outError:]_block_invoke.429
- ___83-[RTLearnedLocationStore _fetchCountOfVisitsToPlaceWithIdentifier:endDate:handler:]_block_invoke.289
- ___83-[RTLearnedLocationStore _fetchLocationsOfInterestWithinDistance:location:handler:]_block_invoke.323
- ___85-[RTTripClusterManager _findRouteFromCurrentLocation:options:queryStartTime:handler:]_block_invoke.356
- ___86-[RTLearnedLocationStore _fetchVisitsWithIncompletePlacesForCurrentDeviceWithHandler:]_block_invoke.403
- ___91-[RTLearnedLocationStore _fetchEntityAsDictionaryWithEntityName:propertiesToFetch:handler:]_block_invoke.559
- ___94-[RTLearnedLocationStore _fetchLocationOfInterestTransitionsBetweenStartDate:endDate:handler:]_block_invoke.390
- ___94-[RTLearnedLocationStore _learnedLocationsOfInterestFromLearnedLocationsOfInterestMO:context:]_block_invoke
- ___block_descriptor_42_e8_32s_e68_"RTLearnedLocationOfInterest"16?0"RTLearnedLocationOfInterestMO"8ls32l8
- ___block_descriptor_67_e8_32s40s48bs_e32_v16?0"NSManagedObjectContext"8ls32l8s40l8s48l8
- ___block_literal_global.256
- ___block_literal_global.327
- ___block_literal_global.330
- ___block_literal_global.396
- ___block_literal_global.413
- ___block_literal_global.453
- ___block_literal_global.566
- ___block_literal_global.618
- ___block_literal_global.732
- ___block_literal_global.907
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreImage_$_libcoreroutine
- _objc_msgSend$_countChangesInTransactionsFromContext:store:predicate:error:
- _objc_msgSend$_fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:
- _objc_msgSend$_getLocationsOfInterestWithDateInterval:outError:
- _objc_msgSend$fetchTripClusterRoadTransitionsWithOptions:handler:
- _objc_msgSend$initWithInterval:gracePeriod:priority:requireNetworkConnectivity:requireInexpensiveNetworkConnectivity:networkTransferDirection:allowBattery:powerNap:requiresClassB:
- _objc_msgSend$setNumEntriesTripClusterRoadTransitionsMO:
- _objc_msgSend$setNumEntriesTripClusterRouteMO:
- _objc_msgSend$setNumTransactionsTripClusterRoadTransitionsMO:
CStrings:
+ " known place type loi already exists in protoLois"
+ "%@ fetch query timed out, semaPlaceTypeLOIsError, %@"
+ "%@ migrating raw legacyValue, %ld, to %@"
+ "%@, %@, %lu mapItems from %lu identifiers, error, %@"
+ "%@, %@, exception handling policy, %@, exception, %@"
+ "%@, %@, new attempt start date, %@, last attempt start date, %@, last training attempt completion date, %@, last successful training attempt completion date, %@, time since last training attempt, %@, time since last training success, %@"
+ "%@, currentToken, %@, transactionNumber, %lld, transactionCount, %lu"
+ "%@, dateInterval, fetched lois count, %lu, error(s), %@"
+ "%@, dateInterval, fetched with lois with placeType, home lois count, %lu, work lois count, %lu, error(s), %@"
+ "%@, loi fetch request, %@, results count, %lu, error, %@"
+ "%@, placeholder fetch request, %@, results count, %lu, error, %@"
+ "%@, status, %@, locationOfInterest, %@"
+ "%@, visit fetch request, %@, results count, %lu, error, %@"
+ "%@:%@,BatteryStatus,isDeviceCharging,%{public}d,isOnDemandMode,%{public}d,enableTripSegmentProcessing,%{public}d"
+ "-[RTLearnedLocationStore _fetchLocationsOfInterestWithIdentifiers:handler:]"
+ "20:52:23"
+ "@40@0:8@16@24B32B36"
+ "@52@0:8d16d24B32B36B40d44"
+ "@56@0:8@16@24@32Q40^@48"
+ "ExitGracefully"
+ "Invalid parameter not satisfying: identifiers"
+ "Invalid parameter not satisfying: identifiers (in %s:%d)"
+ "LOIsKnownPlaceType"
+ "NSException"
+ "RTDefaultsFeatureExtractorLookbackDurationLOIsKnownPlaceType"
+ "RTDefaultsPredictedContextManagerInferenceRequest"
+ "RTDefaultsPredictedContextManagerLastTrainResult"
+ "RTDefaultsPredictedContextManagerTimeSinceLastInferenceRequestAttempt"
+ "RTDefaultsPredictedContextManagerTimeSinceLastTrainingSuccess"
+ "SELF IN %@"
+ "Sep 15 2025"
+ "ThrowException"
+ "TrainPolicyHighPriority"
+ "Warning: Encountered an unknown or invalid RTPredictedContextManagerTrainPolicy value: %ld. Defaulting to Unknown."
+ "_countChangesInTransactionsFromContext:store:startingToken:error:"
+ "_createXPCActivityCriteriaWithInterval:gracePeriod:allowBattery:requiresClassA:requiresClassB:delay:"
+ "_fetchHistoryTransactionBatchFromContext:store:fromToken:limit:error:"
+ "_fetchLocationsOfInterestVisitedBetweenStartDate"
+ "_fetchLocationsOfInterestWithIdentifiers:handler:"
+ "_getLOIsUUIDsFromVisits:"
+ "_getLocationsOfInterestFromVisitedLOIsUUIDs:includeKnownPlaceType:outError:"
+ "_learnedLocationsOfInterestFromLearnedLocationsOfInterestMO:context:includeVisits:includeTransitions:"
+ "_migrateLegacyTrainPolicyFromInteger:"
+ "attaching known place type in protoLois"
+ "bulkFetchMapItemMOsByIdentifiers:context:error:"
+ "createWithLearnedLocationOfInterestMO:includeVisits:includeTransitions"
+ "exceptionHandlingPolicyToString:"
+ "fetchLocationsOfInterestWithIdentifiers:handler:"
+ "handleCoreDataException:outError:"
+ "lastTrainingResultMask"
+ "mapItemForIdentifier"
+ "placeMapItemIdentifiersFromLearnedLocationsOfInterestMO:"
+ "timeSinceLastTrainingSuccess"
- "%@, %@, last inference request date, %@, current inference request date, %@, time since last inference request, %.2f"
- "%@, %@, new attempt start date, %@, last attempt start date, %@, last training attempt completion date, %@, last successful training attempt completion date, %@, time since last training, %@"
- "%@:%@,BatteryStatus,isDeviceCharging,%{public}d,isOnDemandMode,%{public}d,allowLearning,%{public}d"
- "%@:%@,fetchTripClusterRoadTransition,semaError,%@"
- "%@:%@,fetchTripClusterRoadTransitions,semaError,%@"
- "%@:%@,fetchTripClusterRoute,semaError,%@"
- "21:56:50"
- "@\"RTLearnedLocationOfInterest\"16@?0@\"RTLearnedLocationOfInterestMO\"8"
- "@64@0:8@16@24@32Q40Q48^@56"
- "Aug 25 2025"
- "SUBQUERY(%K, $v, $v.%K >= %@).@count > 0"
- "TrainPolicyHighPriorityOnBattery"
- "TrainPolicyHighPriorityOnCharger"
- "_countChangesInTransactionsFromContext:store:predicate:error:"
- "_fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:"

```
