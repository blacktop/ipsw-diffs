## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/Versions/A/HealthDaemon`

```diff

-5200.3.6.0.0
-  __TEXT.__text: 0x7db748
-  __TEXT.__auth_stubs: 0x3270
-  __TEXT.__objc_methlist: 0x3c820
-  __TEXT.__const: 0x1c30c
-  __TEXT.__oslogstring: 0x3cf75
-  __TEXT.__swift5_typeref: 0x323
-  __TEXT.__swift5_fieldmd: 0x1f4
-  __TEXT.__constg_swiftt: 0x4d4
-  __TEXT.__cstring: 0x75cdd
-  __TEXT.__swift5_reflstr: 0x1a0
+5200.4.25.0.0
+  __TEXT.__text: 0x7b09c0
+  __TEXT.__auth_stubs: 0x39e0
+  __TEXT.__objc_methlist: 0x41c64
+  __TEXT.__const: 0x1c5b4
+  __TEXT.__cstring: 0x76458
+  __TEXT.__swift5_typeref: 0x370
+  __TEXT.__swift5_capture: 0x128
+  __TEXT.__constg_swiftt: 0x530
   __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_reflstr: 0x232
+  __TEXT.__swift5_fieldmd: 0x274
+  __TEXT.__swift5_types: 0x30
+  __TEXT.__oslogstring: 0x3d874
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0x28
-  __TEXT.__swift5_capture: 0xa0
-  __TEXT.__gcc_except_tab: 0x37828
+  __TEXT.__swift5_proto: 0x14
+  __TEXT.__gcc_except_tab: 0x37e58
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1bf08
-  __TEXT.__eh_frame: 0x3c0
-  __TEXT.__objc_classname: 0xc559
-  __TEXT.__objc_methname: 0x8a32f
-  __TEXT.__objc_methtype: 0x17212
-  __TEXT.__objc_stubs: 0x4da60
-  __DATA_CONST.__got: 0x4e68
-  __DATA_CONST.__const: 0xbbe8
-  __DATA_CONST.__objc_classlist: 0x2868
+  __TEXT.__unwind_info: 0x1bad0
+  __TEXT.__eh_frame: 0x918
+  __TEXT.__objc_classname: 0xc660
+  __TEXT.__objc_methname: 0x8b753
+  __TEXT.__objc_methtype: 0x174e8
+  __TEXT.__objc_stubs: 0x4e180
+  __DATA_CONST.__got: 0x5048
+  __DATA_CONST.__const: 0xbd78
+  __DATA_CONST.__objc_classlist: 0x28a8
   __DATA_CONST.__objc_catlist: 0x470
-  __DATA_CONST.__objc_protolist: 0x990
+  __DATA_CONST.__objc_protolist: 0x998
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18ca0
+  __DATA_CONST.__objc_selrefs: 0x193e0
   __DATA_CONST.__objc_protorefs: 0x1b0
-  __DATA_CONST.__objc_superrefs: 0x1d80
-  __DATA_CONST.__objc_arraydata: 0x8718
-  __AUTH_CONST.__auth_got: 0x1950
-  __AUTH_CONST.__const: 0x20bb8
-  __AUTH_CONST.__cfstring: 0x3bfe0
-  __AUTH_CONST.__objc_const: 0x82d18
-  __AUTH_CONST.__objc_arrayobj: 0x1ef0
-  __AUTH_CONST.__objc_intobj: 0x43b0
+  __DATA_CONST.__objc_superrefs: 0x1da8
+  __DATA_CONST.__objc_arraydata: 0x8720
+  __AUTH_CONST.__auth_got: 0x1d08
+  __AUTH_CONST.__const: 0x210d8
+  __AUTH_CONST.__cfstring: 0x3c260
+  __AUTH_CONST.__objc_const: 0x7af60
+  __AUTH_CONST.__objc_arrayobj: 0x1f08
+  __AUTH_CONST.__objc_intobj: 0x43c8
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x19908
-  __AUTH.__data: 0xf8
-  __DATA.__objc_ivar: 0x5034
-  __DATA.__data: 0x7580
-  __DATA.__bss: 0x648
+  __AUTH.__objc_data: 0x19b20
+  __AUTH.__data: 0x1c0
+  __DATA.__objc_ivar: 0x50bc
+  __DATA.__data: 0x77b8
   __DATA.__common: 0x24
+  __DATA.__bss: 0x800
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 67FB09C3-EDFC-3E79-9F57-28C79815AA0C
-  Functions: 33297
-  Symbols:   69315
-  CStrings:  42772
+  UUID: 28FBD96D-03B3-3120-92C9-00AC23162BCB
+  Functions: 33138
+  Symbols:   69738
+  CStrings:  42992
 
Symbols:
+ +[HDAuthorizationStatus authorizationStatusForRecordForObjectType:authorizationStatusRecord:clientEntitlements:]
+ +[HDAuthorizationStatusRecord notDerminedReadAuthorizationStatus]
+ +[HDAuthorizationStatusRecord unrestrictedReadAuthorizationStatus]
+ +[HDCloudSyncStateUpdater _updateStateStore:codableCloudState:withMergeState:profile:delegate:error:]
+ +[HDCloudSyncStore _syncStoreForProfile:storeIdentifier:ownerIdentifier:syncIdentity:containerIdentifier:shardPredicate:creationDate:error:]
+ +[HDCloudSyncStore createOrUpdateShardStoresForProfile:throughDate:ownerIdentifier:containerIdentifier:syncIdentity:error:]
+ +[HDCloudSyncStore providesSamplePruningRestrictionPredicate]
+ +[HDCloudSyncStore shardIntervalWithStartDate:endDate:]
+ +[HDCloudSyncStore shardPredicatesForProfile:currentDate:error:]
+ +[HDCloudSyncStore syncStoreForProfile:storeIdentifier:error:]
+ +[HDCloudSyncStore syncStoreForProfile:storeIdentifier:ownerIdentifier:syncIdentity:containerIdentifier:creationDate:error:]
+ +[HDCloudSyncStore syncStoreForProfile:storeIdentifier:ownerIdentifier:syncIdentity:containerIdentifier:error:]
+ +[HDCloudSyncStoreEntity cacheExcludedSyncIdentities:storeIdentifier:database:error:]
+ +[HDCloudSyncStoreEntity cacheExcludedSyncIdentities:storeIdentifier:profile:error:]
+ +[HDCloudSyncStoreEntity cachedExcludedSyncIdentitiesForStoreIdentifier:database:error:]
+ +[HDCloudSyncStoreEntity cachedExcludedSyncIdentitiesForStoreIdentifier:profile:error:]
+ +[HDDataSyncEntity _predicateForDateIntervalStartDate:endDate:]
+ +[HDDataSyncEntity _pruneSyncedObjectsUsingPredicate:limit:profile:error:]
+ +[HDDataSyncEntity _pruningPredicateWithRestrictionPredicates:]
+ +[HDDataSyncEntity _pruningPredicateWithRestrictionPredicates:matchOnlyNilDatesWithoutShardInterval:]
+ +[HDDataSyncEntity pruneSyncedObjectsWithRestrictionPredicates:limit:nowDate:profile:error:]
+ +[HDDataSyncEntity(UnitTesting) unitTest_pruningPredicateWithRestrictionPredicates:]
+ +[HDDatabasePruningShowShim _instantiateStores:profile:error:]
+ +[HDDatabasePruningShowShim _persistentIDForSyncIdentity:profile:error:]
+ +[HDDatabasePruningShowShim _syncStoresInProfile:error:]
+ +[HDDatabasePruningShowShim activeStoresForMaxAnchorWithProfile:referenceDate:error:]
+ +[HDDatabasePruningShowShim activeStoresForRestrictionPredicatesWithProfile:referenceDate:error:]
+ +[HDDatabasePruningShowShim canPerformRecentRecordRollWithProfile:]
+ +[HDDatabasePruningShowShim currentSyncIdentityWithProfile:]
+ +[HDDatabasePruningShowShim datesMatchSampleStartDate:sampleEndDate:shardStartDate:shardEndDate:]
+ +[HDDatabasePruningShowShim deletedSampleInProfile:sampleUUID:error:]
+ +[HDDatabasePruningShowShim deletedSampleSyncEntityClassName]
+ +[HDDatabasePruningShowShim deletedSampleSyncEntityIdentifier]
+ +[HDDatabasePruningShowShim deletedSamplesInProfile:anchor:limit:error:]
+ +[HDDatabasePruningShowShim entitiesInProfile:referenceDate:shouldIncludeEntity:error:]
+ +[HDDatabasePruningShowShim pruningFrozenAnchorRelevanceInterval]
+ +[HDDatabasePruningShowShim recentStoreAnchorRelevanceInterval]
+ +[HDDatabasePruningShowShim syncIdentitiesInProfile:error:]
+ +[HDDatabasePruningShowShim syncStoresInProfile:shouldIncludeEntityIdentifier:error:]
+ +[HDDatabasePruningTask _maximumPruningAnchorWithRestrictionPredicates:]
+ +[HDDeletedSampleEntity deletedSampleInProfile:sampleUUID:error:handler:]
+ +[HDDeletedSampleEntity enumerateDeletedSamplesInProfile:anchor:limit:error:handler:]
+ +[HDDeletedSampleSyncEntity _pruningPredicateWithRestrictionPredicates:]
+ +[HDNanoSyncStore providesSamplePruningRestrictionPredicate]
+ +[HDSyncAnchorEntity frozenAnchorMapPerStoreInProfile:error:]
+ +[HDSyncAnchorEntity latestFrozenAnchorUpdatePerStoreInProfile:error:]
+ +[HDSyncStoreEntity activeStoresForMaxAnchorPruningInProfile:referenceDate:error:]
+ +[HDSyncStoreEntity activeStoresForRestrictionPredictePruningInProfile:referenceDate:error:]
+ +[HDSyncStoreEntity existingSyncStoreEntityWithUUID:ofType:database:error:]
+ +[HDSyncStoreEntity syncStoreEntityWithUUID:type:creationDate:healthDatabase:error:]
+ +[_HDStaticSyncStore providesSamplePruningRestrictionPredicate]
+ -[HDAnalyticsSubmissionCoordinator initWithProfile:]
+ -[HDAuthorizationManager filteredAuthorizedObjectsForClient:anchor:bundleIdentifier:clientEntitlements:error:]
+ -[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]
+ -[HDAuthorizationStatusRecord .cxx_destruct]
+ -[HDAuthorizationStatusRecord authorizationMode]
+ -[HDAuthorizationStatusRecord authorizationPredicate]
+ -[HDAuthorizationStatusRecord authorizationRecord]
+ -[HDAuthorizationStatusRecord authorizationRequest]
+ -[HDAuthorizationStatusRecord authorizationStatus]
+ -[HDAuthorizationStatusRecord canRead]
+ -[HDAuthorizationStatusRecord canWrite]
+ -[HDAuthorizationStatusRecord deletedObjectBaselineAnchor]
+ -[HDAuthorizationStatusRecord description]
+ -[HDAuthorizationStatusRecord disableReading]
+ -[HDAuthorizationStatusRecord disableSharing]
+ -[HDAuthorizationStatusRecord hash]
+ -[HDAuthorizationStatusRecord initWithReadAuthorizationStatus:authorizationRequest:authorizationMode:restrictedBundleIdentifier:restrictedSourceEntities:deletedObjectBaselineAnchor:objectLimitAnchor:objectLimitModifiedDate:]
+ -[HDAuthorizationStatusRecord isAuthorizationDetermined]
+ -[HDAuthorizationStatusRecord isEqual:]
+ -[HDAuthorizationStatusRecord objectLimitAnchor]
+ -[HDAuthorizationStatusRecord objectLimitModifiedDate]
+ -[HDAuthorizationStatusRecord restrictedBundleIdentifier]
+ -[HDAuthorizationStatusRecord restrictedSourceEntities]
+ -[HDClientAuthorizationOracle authorizationStatusRecordForType:error:]
+ -[HDClientAuthorizationOracle authorizationStatusRecordsForTypes:error:]
+ -[HDClientAuthorizationOracle handleObjectAuthorizationRequestsWithPromptHandler:objectType:completion:]
+ -[HDClientAuthorizationOracle hasAuthorizationBypassToReadType:]
+ -[HDCloudSyncCompoundOperation operationsOfType:]
+ -[HDCloudSyncManager canPerformRecentRecordRoll]
+ -[HDCloudSyncOperation operationsOfType:]
+ -[HDCloudSyncPushSequenceOperation excludedSyncIdentities]
+ -[HDCloudSyncPushStoreOperation _recordExcludedSyncIdentitiesFromPushSequenceOperations:]
+ -[HDCloudSyncStore _initWithProfile:storeIdentifier:ownerIdentifier:syncIdentity:containerIdentifier:shardPredicate:provenance:syncEpoch:excludedSyncIdentities:]
+ -[HDCloudSyncStore _isSupportedShardTypeForRestrictionPredicates]
+ -[HDCloudSyncStore init]
+ -[HDCloudSyncStore providesSamplePruningRestrictionPredicate]
+ -[HDCloudSyncStore samplePruningRestrictionPredicateForSyncEntity:error:]
+ -[HDDatabaseControlServer remote_classifiedDeletedSampleInfoWithReferenceDate:anchor:limit:completion:]
+ -[HDDatabaseControlServer remote_deletedSampleDetailWithReferenceDate:matchingPredicatesOnly:sampleUUID:completion:]
+ -[HDDatabaseControlServer remote_deletedSampleInfoWithReferenceDate:completion:]
+ -[HDDatabaseControlServer remote_deletedSamplesDetailWithReferenceDate:matchingPredicatesOnly:anchor:limit:completion:]
+ -[HDDatabaseControlServer remote_pruneSamplesWithReferenceDate:completion:]
+ -[HDDatabaseControlServer remote_showAndDeletedSampleInfoWithReferenceDate:completion:]
+ -[HDDatabaseControlServer remote_showWithReferenceDate:deletedSamplesOnly:completion:]
+ -[HDDatabasePruningShowDeletedSample .cxx_destruct]
+ -[HDDatabasePruningShowDeletedSample creationDate]
+ -[HDDatabasePruningShowDeletedSample endDate]
+ -[HDDatabasePruningShowDeletedSample identifier]
+ -[HDDatabasePruningShowDeletedSample initWithRowID:identifier:creationDate:startDate:endDate:syncIdentity:]
+ -[HDDatabasePruningShowDeletedSample init]
+ -[HDDatabasePruningShowDeletedSample rowID]
+ -[HDDatabasePruningShowDeletedSample startDate]
+ -[HDDatabasePruningShowDeletedSample syncIdentity]
+ -[HDDatabasePruningShowEntity .cxx_destruct]
+ -[HDDatabasePruningShowEntity className]
+ -[HDDatabasePruningShowEntity identifier]
+ -[HDDatabasePruningShowEntity initWithClassName:identifier:supportsPruning:supportsPruningRestrictionPredicates:maximumPruningAnchor:pruningRestrictionPredicates:]
+ -[HDDatabasePruningShowEntity init]
+ -[HDDatabasePruningShowEntity maximumPruningAnchor]
+ -[HDDatabasePruningShowEntity pruningRestrictionPredicates]
+ -[HDDatabasePruningShowEntity supportsPruningRestrictionPredicates]
+ -[HDDatabasePruningShowEntity supportsPruning]
+ -[HDDatabasePruningShowSyncIdentity .cxx_destruct]
+ -[HDDatabasePruningShowSyncIdentity databaseIdentifier]
+ -[HDDatabasePruningShowSyncIdentity hardwareIdentifier]
+ -[HDDatabasePruningShowSyncIdentity initWithPersistentID:hardwareIdentifier:databaseIdentifier:instanceDiscriminator:]
+ -[HDDatabasePruningShowSyncIdentity init]
+ -[HDDatabasePruningShowSyncIdentity instanceDiscriminator]
+ -[HDDatabasePruningShowSyncIdentity persitentID]
+ -[HDDatabasePruningShowSyncStore .cxx_destruct]
+ -[HDDatabasePruningShowSyncStore creationDate]
+ -[HDDatabasePruningShowSyncStore frozenAnchorMap]
+ -[HDDatabasePruningShowSyncStore identifier]
+ -[HDDatabasePruningShowSyncStore initWithPersistentID:identifier:type:creationDate:]
+ -[HDDatabasePruningShowSyncStore initWithPersistentID:identifier:type:creationDate:latestFrozenAnchorDate:frozenAnchorMap:syncIdentity:isSupportedShardType:]
+ -[HDDatabasePruningShowSyncStore init]
+ -[HDDatabasePruningShowSyncStore isSupportedShardType]
+ -[HDDatabasePruningShowSyncStore latestFrozenAnchorDate]
+ -[HDDatabasePruningShowSyncStore persitentID]
+ -[HDDatabasePruningShowSyncStore syncIdentity]
+ -[HDDatabasePruningShowSyncStore type]
+ -[HDDatabasePruningTask _allEntityClasses]
+ -[HDDatabasePruningTask _entityClassSupportsPruning:]
+ -[HDDatabasePruningTask _minimumFrozenAnchorMapForPruningDate:error:]
+ -[HDDatabasePruningTask _pruneObjectsForEntityClass:frozenAnchor:nowDate:limit:error:]
+ -[HDDatabasePruningTask _untypedEntityClasses]
+ -[HDDatabasePruningTask enqueueMaintenanceOperationOnCoordinator:takeAccessibilityAssertion:nowDate:shouldDefer:completion:]
+ -[HDDatabasePruningTask pruneDatabaseWithAccessibilityAssertion:nowDate:prunedObjectLimit:prunedObjectTransactionLimit:shouldDefer:error:]
+ -[HDDefaultAuthorizationSchemaProvider copyWithZone:]
+ -[HDDefaultAuthorizationSchemaProvider filteredAuthorizedObjectsForClient:anchor:bundleIdentifier:clientEntitlements:profile:error:]
+ -[HDDemoDataGenerator _phoneProvenance]
+ -[HDHealthStoreServer remote_startWatchAppWithWorkoutPlanData:completion:]
+ -[HDMaintenanceOperation didTimeOut]
+ -[HDMaintenanceOperation setDidTimeOut:]
+ -[HDMaintenanceOperation setStartedTime:]
+ -[HDMaintenanceOperation setWasCanceled:]
+ -[HDMaintenanceOperation startedTime]
+ -[HDMaintenanceOperation wasCanceled]
+ -[HDMaintenanceWorkCoordinator initWithAnalyticsCoordinator:]
+ -[HDNanoSyncStore providesSamplePruningRestrictionPredicate]
+ -[HDNanoSyncStore samplePruningRestrictionPredicateForSyncEntity:error:]
+ -[HDQueryServer authorizationOracle]
+ -[HDQueryServer authorizationStatusRecordForType:error:]
+ -[HDSamplePruningRestrictionPredicate .cxx_destruct]
+ -[HDSamplePruningRestrictionPredicate endDate]
+ -[HDSamplePruningRestrictionPredicate excludedSyncIdentities]
+ -[HDSamplePruningRestrictionPredicate initWithMaximumAnchor:startDate:endDate:excludedSyncIdentities:]
+ -[HDSamplePruningRestrictionPredicate init]
+ -[HDSamplePruningRestrictionPredicate maximumAnchor]
+ -[HDSamplePruningRestrictionPredicate startDate]
+ -[HDTypedSyncStoreIdentifier .cxx_destruct]
+ -[HDTypedSyncStoreIdentifier identifier]
+ -[HDTypedSyncStoreIdentifier initWithIdentifier:type:]
+ -[HDTypedSyncStoreIdentifier init]
+ -[HDTypedSyncStoreIdentifier type]
+ -[HDVisionPrescriptionAuthorizationSchemaProvider copyWithZone:]
+ -[HDWorkoutBuilderServer _didFinishRecovery]
+ -[HDWorkoutBuilderServer _lock_didUpdateActivities]
+ -[HDWorkoutBuilderServer _recoverAssociatedSeriesBuilders]
+ -[HDWorkoutManager startWatchAppWithWorkoutPlanData:client:completion:]
+ -[HDWorkoutManager(Platform) _startWatchAppWithWorkoutPlanData:client:completion:]
+ -[HKObject(HDExtensions) hk_objectType]
+ -[HKSleepDaySummaryQueryConfiguration(CacheSettings) cacheIdentifier]
+ -[_HDMedicationDoseEventEntityEncoder initWithHealthEntityClass:profile:transaction:purpose:encodingOptions:authorizationFilter:]
+ -[_HDStaticSyncStore providesSamplePruningRestrictionPredicate]
+ -[_HDStaticSyncStore samplePruningRestrictionPredicateForSyncEntity:error:]
+ -[_HKMedicationDoseEventComparisonFilter _predicateForMedicationUUID]
+ -[_HKMedicationDoseEventComparisonFilter _predicateForScheduledDate]
+ GCC_except_table1000
+ GCC_except_table1006
+ GCC_except_table1008
+ GCC_except_table1015
+ GCC_except_table1017
+ GCC_except_table1018
+ GCC_except_table1030
+ GCC_except_table1037
+ GCC_except_table1047
+ GCC_except_table1066
+ GCC_except_table1068
+ GCC_except_table1073
+ GCC_except_table1074
+ GCC_except_table1075
+ GCC_except_table1076
+ GCC_except_table1085
+ GCC_except_table1086
+ GCC_except_table1095
+ GCC_except_table1103
+ GCC_except_table1106
+ GCC_except_table1108
+ GCC_except_table1109
+ GCC_except_table1115
+ GCC_except_table1117
+ GCC_except_table1122
+ GCC_except_table1127
+ GCC_except_table1128
+ GCC_except_table1152
+ GCC_except_table1160
+ GCC_except_table1161
+ GCC_except_table1162
+ GCC_except_table1163
+ GCC_except_table1172
+ GCC_except_table1173
+ GCC_except_table1175
+ GCC_except_table1183
+ GCC_except_table1184
+ GCC_except_table1191
+ GCC_except_table1194
+ GCC_except_table1195
+ GCC_except_table1197
+ GCC_except_table1198
+ GCC_except_table1204
+ GCC_except_table1212
+ GCC_except_table1213
+ GCC_except_table1215
+ GCC_except_table1216
+ GCC_except_table1241
+ GCC_except_table1246
+ GCC_except_table1248
+ GCC_except_table1249
+ GCC_except_table1250
+ GCC_except_table1251
+ GCC_except_table1260
+ GCC_except_table1261
+ GCC_except_table1269
+ GCC_except_table1273
+ GCC_except_table1276
+ GCC_except_table1280
+ GCC_except_table1281
+ GCC_except_table1283
+ GCC_except_table1290
+ GCC_except_table1298
+ GCC_except_table1299
+ GCC_except_table1302
+ GCC_except_table1303
+ GCC_except_table1317
+ GCC_except_table1324
+ GCC_except_table1334
+ GCC_except_table1353
+ GCC_except_table1358
+ GCC_except_table1360
+ GCC_except_table1361
+ GCC_except_table1362
+ GCC_except_table1363
+ GCC_except_table1372
+ GCC_except_table1373
+ GCC_except_table1375
+ GCC_except_table1376
+ GCC_except_table1377
+ GCC_except_table1387
+ GCC_except_table1391
+ GCC_except_table1394
+ GCC_except_table1398
+ GCC_except_table1399
+ GCC_except_table1401
+ GCC_except_table1408
+ GCC_except_table1415
+ GCC_except_table1416
+ GCC_except_table1417
+ GCC_except_table1419
+ GCC_except_table1420
+ GCC_except_table1432
+ GCC_except_table1439
+ GCC_except_table1449
+ GCC_except_table1468
+ GCC_except_table1473
+ GCC_except_table1475
+ GCC_except_table1476
+ GCC_except_table1477
+ GCC_except_table1478
+ GCC_except_table1487
+ GCC_except_table1488
+ GCC_except_table1496
+ GCC_except_table1500
+ GCC_except_table1503
+ GCC_except_table1507
+ GCC_except_table1508
+ GCC_except_table1510
+ GCC_except_table1517
+ GCC_except_table1525
+ GCC_except_table1526
+ GCC_except_table1529
+ GCC_except_table1530
+ GCC_except_table1554
+ GCC_except_table1559
+ GCC_except_table156
+ GCC_except_table1560
+ GCC_except_table1562
+ GCC_except_table1563
+ GCC_except_table1564
+ GCC_except_table1565
+ GCC_except_table1574
+ GCC_except_table1575
+ GCC_except_table1577
+ GCC_except_table158
+ GCC_except_table1594
+ GCC_except_table1596
+ GCC_except_table1597
+ GCC_except_table1600
+ GCC_except_table1613
+ GCC_except_table1614
+ GCC_except_table1615
+ GCC_except_table1617
+ GCC_except_table1618
+ GCC_except_table1646
+ GCC_except_table1648
+ GCC_except_table1650
+ GCC_except_table1651
+ GCC_except_table1652
+ GCC_except_table1653
+ GCC_except_table1662
+ GCC_except_table1679
+ GCC_except_table1680
+ GCC_except_table1682
+ GCC_except_table1683
+ GCC_except_table1685
+ GCC_except_table1686
+ GCC_except_table1703
+ GCC_except_table1704
+ GCC_except_table1705
+ GCC_except_table1717
+ GCC_except_table1724
+ GCC_except_table1734
+ GCC_except_table1751
+ GCC_except_table1756
+ GCC_except_table1758
+ GCC_except_table1760
+ GCC_except_table1761
+ GCC_except_table1762
+ GCC_except_table1763
+ GCC_except_table1772
+ GCC_except_table1773
+ GCC_except_table1775
+ GCC_except_table1776
+ GCC_except_table1793
+ GCC_except_table1794
+ GCC_except_table1796
+ GCC_except_table1797
+ GCC_except_table1800
+ GCC_except_table1815
+ GCC_except_table1816
+ GCC_except_table1817
+ GCC_except_table1828
+ GCC_except_table1835
+ GCC_except_table1845
+ GCC_except_table1862
+ GCC_except_table1867
+ GCC_except_table1869
+ GCC_except_table1871
+ GCC_except_table1872
+ GCC_except_table1873
+ GCC_except_table1874
+ GCC_except_table1883
+ GCC_except_table1900
+ GCC_except_table1901
+ GCC_except_table1903
+ GCC_except_table1904
+ GCC_except_table1906
+ GCC_except_table1915
+ GCC_except_table192
+ GCC_except_table1920
+ GCC_except_table1921
+ GCC_except_table1922
+ GCC_except_table1925
+ GCC_except_table1926
+ GCC_except_table1946
+ GCC_except_table1951
+ GCC_except_table1953
+ GCC_except_table1955
+ GCC_except_table1956
+ GCC_except_table1957
+ GCC_except_table1958
+ GCC_except_table196
+ GCC_except_table1967
+ GCC_except_table1968
+ GCC_except_table1986
+ GCC_except_table1987
+ GCC_except_table1989
+ GCC_except_table1990
+ GCC_except_table1992
+ GCC_except_table2001
+ GCC_except_table2006
+ GCC_except_table2007
+ GCC_except_table2008
+ GCC_except_table2010
+ GCC_except_table2011
+ GCC_except_table2031
+ GCC_except_table2036
+ GCC_except_table2038
+ GCC_except_table2040
+ GCC_except_table2041
+ GCC_except_table2042
+ GCC_except_table2043
+ GCC_except_table2052
+ GCC_except_table2055
+ GCC_except_table2070
+ GCC_except_table2072
+ GCC_except_table2073
+ GCC_except_table2075
+ GCC_except_table2076
+ GCC_except_table2085
+ GCC_except_table2090
+ GCC_except_table2094
+ GCC_except_table2095
+ GCC_except_table2096
+ GCC_except_table2099
+ GCC_except_table2100
+ GCC_except_table2101
+ GCC_except_table2113
+ GCC_except_table212
+ GCC_except_table2120
+ GCC_except_table2130
+ GCC_except_table2152
+ GCC_except_table2154
+ GCC_except_table2156
+ GCC_except_table2157
+ GCC_except_table2158
+ GCC_except_table2159
+ GCC_except_table2168
+ GCC_except_table2169
+ GCC_except_table2171
+ GCC_except_table2172
+ GCC_except_table2183
+ GCC_except_table2190
+ GCC_except_table2192
+ GCC_except_table2193
+ GCC_except_table2197
+ GCC_except_table2203
+ GCC_except_table2212
+ GCC_except_table2213
+ GCC_except_table2214
+ GCC_except_table2216
+ GCC_except_table2217
+ GCC_except_table2218
+ GCC_except_table223
+ GCC_except_table2230
+ GCC_except_table2237
+ GCC_except_table2247
+ GCC_except_table2269
+ GCC_except_table2271
+ GCC_except_table2273
+ GCC_except_table2274
+ GCC_except_table2275
+ GCC_except_table2276
+ GCC_except_table2285
+ GCC_except_table2288
+ GCC_except_table2303
+ GCC_except_table2305
+ GCC_except_table2306
+ GCC_except_table2308
+ GCC_except_table2310
+ GCC_except_table2317
+ GCC_except_table2323
+ GCC_except_table2324
+ GCC_except_table2325
+ GCC_except_table2328
+ GCC_except_table2329
+ GCC_except_table2330
+ GCC_except_table2356
+ GCC_except_table2357
+ GCC_except_table2359
+ GCC_except_table2361
+ GCC_except_table2362
+ GCC_except_table2363
+ GCC_except_table2373
+ GCC_except_table2374
+ GCC_except_table2378
+ GCC_except_table2385
+ GCC_except_table2388
+ GCC_except_table2392
+ GCC_except_table2393
+ GCC_except_table2395
+ GCC_except_table2398
+ GCC_except_table2400
+ GCC_except_table2414
+ GCC_except_table2415
+ GCC_except_table2416
+ GCC_except_table2418
+ GCC_except_table2419
+ GCC_except_table2420
+ GCC_except_table2446
+ GCC_except_table2447
+ GCC_except_table2449
+ GCC_except_table2451
+ GCC_except_table2452
+ GCC_except_table2464
+ GCC_except_table2472
+ GCC_except_table2479
+ GCC_except_table2480
+ GCC_except_table2481
+ GCC_except_table2484
+ GCC_except_table2486
+ GCC_except_table2487
+ GCC_except_table2493
+ GCC_except_table2500
+ GCC_except_table2501
+ GCC_except_table2502
+ GCC_except_table2505
+ GCC_except_table2506
+ GCC_except_table2514
+ GCC_except_table2531
+ GCC_except_table2553
+ GCC_except_table2554
+ GCC_except_table2555
+ GCC_except_table2556
+ GCC_except_table2558
+ GCC_except_table2559
+ GCC_except_table2570
+ GCC_except_table2571
+ GCC_except_table2583
+ GCC_except_table2590
+ GCC_except_table2591
+ GCC_except_table2592
+ GCC_except_table2595
+ GCC_except_table2597
+ GCC_except_table2598
+ GCC_except_table2604
+ GCC_except_table2611
+ GCC_except_table2612
+ GCC_except_table2615
+ GCC_except_table2616
+ GCC_except_table2623
+ GCC_except_table263
+ GCC_except_table2640
+ GCC_except_table2662
+ GCC_except_table2663
+ GCC_except_table2665
+ GCC_except_table2667
+ GCC_except_table2668
+ GCC_except_table268
+ GCC_except_table2680
+ GCC_except_table2688
+ GCC_except_table2695
+ GCC_except_table2696
+ GCC_except_table2697
+ GCC_except_table2700
+ GCC_except_table2702
+ GCC_except_table2703
+ GCC_except_table2709
+ GCC_except_table271
+ GCC_except_table2716
+ GCC_except_table2717
+ GCC_except_table2718
+ GCC_except_table2721
+ GCC_except_table2722
+ GCC_except_table274
+ GCC_except_table2743
+ GCC_except_table2745
+ GCC_except_table2746
+ GCC_except_table2748
+ GCC_except_table2750
+ GCC_except_table2753
+ GCC_except_table2765
+ GCC_except_table2780
+ GCC_except_table2781
+ GCC_except_table2782
+ GCC_except_table2784
+ GCC_except_table2787
+ GCC_except_table2788
+ GCC_except_table2796
+ GCC_except_table2801
+ GCC_except_table2802
+ GCC_except_table2803
+ GCC_except_table2805
+ GCC_except_table2806
+ GCC_except_table2827
+ GCC_except_table2829
+ GCC_except_table2830
+ GCC_except_table2832
+ GCC_except_table2836
+ GCC_except_table2837
+ GCC_except_table2846
+ GCC_except_table2856
+ GCC_except_table2859
+ GCC_except_table2862
+ GCC_except_table2863
+ GCC_except_table2864
+ GCC_except_table2866
+ GCC_except_table2870
+ GCC_except_table2881
+ GCC_except_table2890
+ GCC_except_table2895
+ GCC_except_table2896
+ GCC_except_table2903
+ GCC_except_table2904
+ GCC_except_table2912
+ GCC_except_table2922
+ GCC_except_table2942
+ GCC_except_table2944
+ GCC_except_table2945
+ GCC_except_table2947
+ GCC_except_table2951
+ GCC_except_table296
+ GCC_except_table2961
+ GCC_except_table2965
+ GCC_except_table2967
+ GCC_except_table2975
+ GCC_except_table2978
+ GCC_except_table2981
+ GCC_except_table2982
+ GCC_except_table2983
+ GCC_except_table2986
+ GCC_except_table2988
+ GCC_except_table2989
+ GCC_except_table2996
+ GCC_except_table2999
+ GCC_except_table3007
+ GCC_except_table3009
+ GCC_except_table3010
+ GCC_except_table3017
+ GCC_except_table3018
+ GCC_except_table3025
+ GCC_except_table3035
+ GCC_except_table304
+ GCC_except_table3055
+ GCC_except_table3057
+ GCC_except_table3058
+ GCC_except_table3060
+ GCC_except_table3064
+ GCC_except_table3065
+ GCC_except_table307
+ GCC_except_table3074
+ GCC_except_table308
+ GCC_except_table3084
+ GCC_except_table3087
+ GCC_except_table3090
+ GCC_except_table3091
+ GCC_except_table3095
+ GCC_except_table3097
+ GCC_except_table3098
+ GCC_except_table3106
+ GCC_except_table3111
+ GCC_except_table3112
+ GCC_except_table3113
+ GCC_except_table3116
+ GCC_except_table3117
+ GCC_except_table3139
+ GCC_except_table3141
+ GCC_except_table3142
+ GCC_except_table3144
+ GCC_except_table3148
+ GCC_except_table3170
+ GCC_except_table3173
+ GCC_except_table3176
+ GCC_except_table3177
+ GCC_except_table3180
+ GCC_except_table3183
+ GCC_except_table3184
+ GCC_except_table3193
+ GCC_except_table3198
+ GCC_except_table3199
+ GCC_except_table3200
+ GCC_except_table3202
+ GCC_except_table3203
+ GCC_except_table3225
+ GCC_except_table3227
+ GCC_except_table3228
+ GCC_except_table3230
+ GCC_except_table3234
+ GCC_except_table3235
+ GCC_except_table3244
+ GCC_except_table3254
+ GCC_except_table3257
+ GCC_except_table3260
+ GCC_except_table3261
+ GCC_except_table3265
+ GCC_except_table3267
+ GCC_except_table3268
+ GCC_except_table3276
+ GCC_except_table3281
+ GCC_except_table3282
+ GCC_except_table3286
+ GCC_except_table3287
+ GCC_except_table3295
+ GCC_except_table3302
+ GCC_except_table3312
+ GCC_except_table3332
+ GCC_except_table3334
+ GCC_except_table3335
+ GCC_except_table3336
+ GCC_except_table3337
+ GCC_except_table3341
+ GCC_except_table3351
+ GCC_except_table3354
+ GCC_except_table3355
+ GCC_except_table3365
+ GCC_except_table3368
+ GCC_except_table3371
+ GCC_except_table3372
+ GCC_except_table3376
+ GCC_except_table3378
+ GCC_except_table3379
+ GCC_except_table3387
+ GCC_except_table3393
+ GCC_except_table3394
+ GCC_except_table3396
+ GCC_except_table3397
+ GCC_except_table3404
+ GCC_except_table3411
+ GCC_except_table3421
+ GCC_except_table3441
+ GCC_except_table3443
+ GCC_except_table3444
+ GCC_except_table3446
+ GCC_except_table3450
+ GCC_except_table3451
+ GCC_except_table3460
+ GCC_except_table3470
+ GCC_except_table3473
+ GCC_except_table3476
+ GCC_except_table3477
+ GCC_except_table3481
+ GCC_except_table3483
+ GCC_except_table3484
+ GCC_except_table3492
+ GCC_except_table3497
+ GCC_except_table3498
+ GCC_except_table3499
+ GCC_except_table3502
+ GCC_except_table3503
+ GCC_except_table3522
+ GCC_except_table3524
+ GCC_except_table3526
+ GCC_except_table3527
+ GCC_except_table3529
+ GCC_except_table3532
+ GCC_except_table3534
+ GCC_except_table3543
+ GCC_except_table3544
+ GCC_except_table3546
+ GCC_except_table3554
+ GCC_except_table3558
+ GCC_except_table3561
+ GCC_except_table3563
+ GCC_except_table3565
+ GCC_except_table3566
+ GCC_except_table3568
+ GCC_except_table3575
+ GCC_except_table3577
+ GCC_except_table3582
+ GCC_except_table3583
+ GCC_except_table3584
+ GCC_except_table3586
+ GCC_except_table3587
+ GCC_except_table3606
+ GCC_except_table3608
+ GCC_except_table3610
+ GCC_except_table3611
+ GCC_except_table3615
+ GCC_except_table3616
+ GCC_except_table3617
+ GCC_except_table3618
+ GCC_except_table3627
+ GCC_except_table3628
+ GCC_except_table3640
+ GCC_except_table3644
+ GCC_except_table3647
+ GCC_except_table3648
+ GCC_except_table3657
+ GCC_except_table3659
+ GCC_except_table3664
+ GCC_except_table3665
+ GCC_except_table3666
+ GCC_except_table3670
+ GCC_except_table3683
+ GCC_except_table3690
+ GCC_except_table3700
+ GCC_except_table371
+ GCC_except_table3718
+ GCC_except_table3719
+ GCC_except_table3721
+ GCC_except_table3722
+ GCC_except_table3723
+ GCC_except_table3726
+ GCC_except_table3729
+ GCC_except_table373
+ GCC_except_table3739
+ GCC_except_table3742
+ GCC_except_table3755
+ GCC_except_table3759
+ GCC_except_table376
+ GCC_except_table3762
+ GCC_except_table3763
+ GCC_except_table3772
+ GCC_except_table3774
+ GCC_except_table3779
+ GCC_except_table378
+ GCC_except_table3780
+ GCC_except_table3781
+ GCC_except_table3783
+ GCC_except_table3784
+ GCC_except_table3796
+ GCC_except_table3803
+ GCC_except_table3813
+ GCC_except_table383
+ GCC_except_table3831
+ GCC_except_table3832
+ GCC_except_table3834
+ GCC_except_table3835
+ GCC_except_table3839
+ GCC_except_table3840
+ GCC_except_table3841
+ GCC_except_table3842
+ GCC_except_table3851
+ GCC_except_table3852
+ GCC_except_table3864
+ GCC_except_table3868
+ GCC_except_table3871
+ GCC_except_table3872
+ GCC_except_table3881
+ GCC_except_table3883
+ GCC_except_table3888
+ GCC_except_table3889
+ GCC_except_table3890
+ GCC_except_table3893
+ GCC_except_table3894
+ GCC_except_table3918
+ GCC_except_table3919
+ GCC_except_table3921
+ GCC_except_table3922
+ GCC_except_table3927
+ GCC_except_table3928
+ GCC_except_table3929
+ GCC_except_table393
+ GCC_except_table3939
+ GCC_except_table395
+ GCC_except_table3950
+ GCC_except_table3953
+ GCC_except_table3956
+ GCC_except_table3958
+ GCC_except_table3960
+ GCC_except_table3961
+ GCC_except_table3970
+ GCC_except_table3972
+ GCC_except_table3977
+ GCC_except_table3978
+ GCC_except_table3979
+ GCC_except_table3981
+ GCC_except_table3982
+ GCC_except_table4006
+ GCC_except_table4007
+ GCC_except_table4009
+ GCC_except_table4012
+ GCC_except_table4014
+ GCC_except_table4015
+ GCC_except_table4016
+ GCC_except_table4017
+ GCC_except_table4026
+ GCC_except_table4027
+ GCC_except_table404
+ GCC_except_table407
+ GCC_except_table412
+ GCC_except_table415
+ GCC_except_table418
+ GCC_except_table424
+ GCC_except_table426
+ GCC_except_table433
+ GCC_except_table436
+ GCC_except_table459
+ GCC_except_table466
+ GCC_except_table467
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table485
+ GCC_except_table486
+ GCC_except_table489
+ GCC_except_table493
+ GCC_except_table496
+ GCC_except_table499
+ GCC_except_table500
+ GCC_except_table508
+ GCC_except_table514
+ GCC_except_table515
+ GCC_except_table518
+ GCC_except_table519
+ GCC_except_table527
+ GCC_except_table534
+ GCC_except_table544
+ GCC_except_table568
+ GCC_except_table573
+ GCC_except_table574
+ GCC_except_table583
+ GCC_except_table586
+ GCC_except_table587
+ GCC_except_table596
+ GCC_except_table597
+ GCC_except_table600
+ GCC_except_table604
+ GCC_except_table607
+ GCC_except_table610
+ GCC_except_table611
+ GCC_except_table619
+ GCC_except_table625
+ GCC_except_table628
+ GCC_except_table629
+ GCC_except_table636
+ GCC_except_table643
+ GCC_except_table653
+ GCC_except_table675
+ GCC_except_table682
+ GCC_except_table683
+ GCC_except_table692
+ GCC_except_table693
+ GCC_except_table701
+ GCC_except_table702
+ GCC_except_table705
+ GCC_except_table709
+ GCC_except_table712
+ GCC_except_table715
+ GCC_except_table716
+ GCC_except_table724
+ GCC_except_table730
+ GCC_except_table731
+ GCC_except_table734
+ GCC_except_table735
+ GCC_except_table754
+ GCC_except_table759
+ GCC_except_table764
+ GCC_except_table765
+ GCC_except_table766
+ GCC_except_table776
+ GCC_except_table778
+ GCC_except_table786
+ GCC_except_table793
+ GCC_except_table800
+ GCC_except_table801
+ GCC_except_table807
+ GCC_except_table809
+ GCC_except_table814
+ GCC_except_table818
+ GCC_except_table819
+ GCC_except_table840
+ GCC_except_table842
+ GCC_except_table847
+ GCC_except_table848
+ GCC_except_table849
+ GCC_except_table850
+ GCC_except_table859
+ GCC_except_table860
+ GCC_except_table869
+ GCC_except_table877
+ GCC_except_table880
+ GCC_except_table882
+ GCC_except_table883
+ GCC_except_table889
+ GCC_except_table891
+ GCC_except_table896
+ GCC_except_table901
+ GCC_except_table902
+ GCC_except_table916
+ GCC_except_table923
+ GCC_except_table933
+ GCC_except_table952
+ GCC_except_table954
+ GCC_except_table959
+ GCC_except_table960
+ GCC_except_table961
+ GCC_except_table962
+ GCC_except_table974
+ GCC_except_table975
+ GCC_except_table976
+ GCC_except_table986
+ GCC_except_table994
+ GCC_except_table997
+ GCC_except_table999
+ HDCloudSyncStoreExcludedSyncIdentitiesKey_block_invoke.lookupKey
+ HDCloudSyncStoreExcludedSyncIdentitiesKey_block_invoke_2.updateKey
+ HDCloudSyncStoreExcludedSyncIdentitiesKey_block_invoke_3.lookupKey
+ HDCloudSyncStoreExcludedSyncIdentitiesKey_block_invoke_4.lookupKey
+ HDCloudSyncStoreExcludedSyncIdentitiesKey_block_invoke_5.lookupKey
+ HDCloudSyncStoreExcludedSyncIdentitiesKey_block_invoke_6.lookupKey
+ OBJC_IVAR_$_HDAnalyticsSubmissionCoordinator._primaryProfile
+ OBJC_IVAR_$_HDAuthorizationManager._lock
+ OBJC_IVAR_$_HDAuthorizationStatusRecord._authorizationRecord
+ OBJC_IVAR_$_HDAuthorizationStatusRecord._deletedObjectBaselineAnchor
+ OBJC_IVAR_$_HDAuthorizationStatusRecord._objectLimitAnchor
+ OBJC_IVAR_$_HDAuthorizationStatusRecord._restrictedBundleIdentifier
+ OBJC_IVAR_$_HDAuthorizationStatusRecord._restrictedSourceEntities
+ OBJC_IVAR_$_HDCloudSyncStore._excludedSyncIdentities
+ OBJC_IVAR_$_HDDatabasePruningShowDeletedSample._creationDate
+ OBJC_IVAR_$_HDDatabasePruningShowDeletedSample._endDate
+ OBJC_IVAR_$_HDDatabasePruningShowDeletedSample._identifier
+ OBJC_IVAR_$_HDDatabasePruningShowDeletedSample._rowID
+ OBJC_IVAR_$_HDDatabasePruningShowDeletedSample._startDate
+ OBJC_IVAR_$_HDDatabasePruningShowDeletedSample._syncIdentity
+ OBJC_IVAR_$_HDDatabasePruningShowEntity._className
+ OBJC_IVAR_$_HDDatabasePruningShowEntity._identifier
+ OBJC_IVAR_$_HDDatabasePruningShowEntity._maximumPruningAnchor
+ OBJC_IVAR_$_HDDatabasePruningShowEntity._pruningRestrictionPredicates
+ OBJC_IVAR_$_HDDatabasePruningShowEntity._supportsPruning
+ OBJC_IVAR_$_HDDatabasePruningShowEntity._supportsPruningRestrictionPredicates
+ OBJC_IVAR_$_HDDatabasePruningShowSyncIdentity._databaseIdentifier
+ OBJC_IVAR_$_HDDatabasePruningShowSyncIdentity._hardwareIdentifier
+ OBJC_IVAR_$_HDDatabasePruningShowSyncIdentity._instanceDiscriminator
+ OBJC_IVAR_$_HDDatabasePruningShowSyncIdentity._persitentID
+ OBJC_IVAR_$_HDDatabasePruningShowSyncStore._creationDate
+ OBJC_IVAR_$_HDDatabasePruningShowSyncStore._frozenAnchorMap
+ OBJC_IVAR_$_HDDatabasePruningShowSyncStore._identifier
+ OBJC_IVAR_$_HDDatabasePruningShowSyncStore._isSupportedShardType
+ OBJC_IVAR_$_HDDatabasePruningShowSyncStore._latestFrozenAnchorDate
+ OBJC_IVAR_$_HDDatabasePruningShowSyncStore._persitentID
+ OBJC_IVAR_$_HDDatabasePruningShowSyncStore._syncIdentity
+ OBJC_IVAR_$_HDDatabasePruningShowSyncStore._type
+ OBJC_IVAR_$_HDMaintenanceOperation._didTimeOut
+ OBJC_IVAR_$_HDMaintenanceOperation._wasCanceled
+ OBJC_IVAR_$_HDMaintenanceWorkCoordinator._analyticsCoordinator
+ OBJC_IVAR_$_HDQueryServer._authorizationOracle
+ OBJC_IVAR_$_HDSamplePruningRestrictionPredicate._endDate
+ OBJC_IVAR_$_HDSamplePruningRestrictionPredicate._excludedSyncIdentities
+ OBJC_IVAR_$_HDSamplePruningRestrictionPredicate._maximumAnchor
+ OBJC_IVAR_$_HDSamplePruningRestrictionPredicate._startDate
+ OBJC_IVAR_$_HDTypedSyncStoreIdentifier._identifier
+ OBJC_IVAR_$_HDTypedSyncStoreIdentifier._type
+ OBJC_IVAR_$__HDMedicationDoseEventEntityEncoder._includeMedicationAndScheduledItemDetails
+ _HDDataEntityPropertySyncIdentity
+ _HDDatabaseNewStoreAnchorRelevanceInterval
+ _HDDatabasePruningAccessibilityAssertionTimeout
+ _HDDatabasePruningFrozenAnchorRelevanceInterval
+ _HDDatabasePruningOperationObjectLimit
+ _HDDatabasePruningTransactionObjectLimit
+ _HDInstantiateSyncStore
+ _HDMedicationDoseEventEntityEncodingOptionExcludePrivateMedicationInfo
+ _HDMedicationDoseEventEntityPredicateForLogOrigins
+ _HDMedicationDoseEventEntityPredicateForMedicationUUIDs
+ _HDMedicationDoseEventEntityPredicateForScheduledDates
+ _HDSyncAnchorPropertyFrozenUpdateDate
+ _HDSyncAnchorPropertyStore
+ _HDSyncStoreClassForSyncStoreType
+ _HDWorkoutDataDestinationStateFromWorkoutBuilderServerState
+ _HKLogAttachment
+ _HKLogSummarySharing
+ _HKPredicateKeyPathLogOrigin
+ _HKPredicateKeyPathMedicationUUID
+ _HKPredicateKeyPathScheduledDate
+ _HKWorkoutBuilderConstructionStateFromBuilderServerState
+ _MergedGlobals.24
+ _OBJC_CLASS_$_HDAuthorizationStatusRecord
+ _OBJC_CLASS_$_HDDatabasePruningShow
+ _OBJC_CLASS_$_HDDatabasePruningShowDeletedSample
+ _OBJC_CLASS_$_HDDatabasePruningShowEntity
+ _OBJC_CLASS_$_HDDatabasePruningShowShim
+ _OBJC_CLASS_$_HDDatabasePruningShowSyncIdentity
+ _OBJC_CLASS_$_HDDatabasePruningShowSyncStore
+ _OBJC_CLASS_$_HDSamplePruningRestrictionPredicate
+ _OBJC_CLASS_$_HDTypedSyncStoreIdentifier
+ _OBJC_CLASS_$_HKSleepDaySummaryQueryConfiguration
+ _OBJC_METACLASS_$_HDAuthorizationStatusRecord
+ _OBJC_METACLASS_$_HDDatabasePruningShow
+ _OBJC_METACLASS_$_HDDatabasePruningShowDeletedSample
+ _OBJC_METACLASS_$_HDDatabasePruningShowEntity
+ _OBJC_METACLASS_$_HDDatabasePruningShowShim
+ _OBJC_METACLASS_$_HDDatabasePruningShowSyncIdentity
+ _OBJC_METACLASS_$_HDDatabasePruningShowSyncStore
+ _OBJC_METACLASS_$_HDSamplePruningRestrictionPredicate
+ _OBJC_METACLASS_$_HDTypedSyncStoreIdentifier
+ __102+[HDSampleSyncEntity _predicateForSampleAgeWithMaximumObjectAgeByType:defaultMaxAge:sessionStartDate:]_block_invoke.419
+ __108+[HDCloudSyncStoreEntity storeIdentifiersForOwnerIdentifier:containerIdentifier:syncIdentity:profile:error:]_block_invoke.363
+ __110-[HDAuthorizationManager filteredAuthorizedObjectsForClient:anchor:bundleIdentifier:clientEntitlements:error:]_block_invoke.588
+ __112-[HDDatabasePruningCoordinator _pruneProfilesWithIdentifiers:takeAccessibilityAssertion:shouldDefer:completion:]_block_invoke.313
+ __115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.452
+ __115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.455
+ __115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.459
+ __115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.460
+ __115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke_2.456
+ __124-[HDDatabasePruningTask enqueueMaintenanceOperationOnCoordinator:takeAccessibilityAssertion:nowDate:shouldDefer:completion:]_block_invoke.296
+ __127-[HDClientAuthorizationOracle(Privileged) _queue_beginAuthorizationRequestDelegateTransactionWithSessionIdentifier:completion:]_block_invoke.511
+ __133-[HDClientAuthorizationOracle enqueueAuthorizationRequestToWriteTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke.425
+ __158-[HDClientAuthorizationOracle _queue_enqueueAuthorizationRequestForBundleIdentifier:writeTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke.431
+ __158-[HDClientAuthorizationOracle _queue_enqueueAuthorizationRequestForBundleIdentifier:writeTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke_2.432
+ __189+[HDAuthorizationEntity _setAuthorizationStatuses:authorizationRequests:authorizationModes:sourceEntity:dateModified:syncProvenance:objectAnchor:options:profile:database:transaction:error:]_block_invoke.443
+ __37-[HDCloudSyncPushStoreOperation main]_block_invoke.313
+ __37-[HDDatabase _mergeSecondaryJournals]_block_invoke.572
+ __52-[HDWorkoutBasicDataSource setSampleTypesToCollect:]_block_invoke.405
+ __61-[HDDatabase _mergeSecondaryJournalsWithActivity:completion:]_block_invoke.573
+ __67-[HDDatabasePruningCoordinator performPeriodicActivity:completion:]_block_invoke.304
+ __73+[HDDeletedSampleEntity deletedSampleInProfile:sampleUUID:error:handler:]_block_invoke.325
+ __77-[HDDatabase _performWhenDataProtectedByFirstUnlockIsAvailableOnQueue:block:]_block_invoke.420
+ __77-[HDDatabase _performWhenDataProtectedByFirstUnlockIsAvailableOnQueue:block:]_block_invoke.424
+ __77-[_HDObjectAuthorizationPromptSession endPromptTransactionWithSuccess:error:]_block_invoke.783
+ __78+[HDDeletedSampleEntity insertCodableDeletedSamples:provenance:profile:error:]_block_invoke.344
+ __78+[HDDeletedSampleEntity insertCodableDeletedSamples:provenance:profile:error:]_block_invoke.350
+ __78-[HDCloudSyncStoreEntity updateShardStartDate:endDate:type:transaction:error:]_block_invoke.442
+ __78-[HDDatabase _protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.542
+ __80-[HDCloudSyncPushSequenceOperation _startingSyncAnchorMapForStagingStore:error:]_block_invoke.336
+ __84+[HDCloudSyncStoreEntity persistState:storeUUID:shouldReplace:healthDatabase:error:]_block_invoke.404
+ __84+[HDCloudSyncStoreEntity persistState:storeUUID:shouldReplace:healthDatabase:error:]_block_invoke.412
+ __89-[HDHealthStoreServer remote_requestPerObjectReadAuthorizationForType:filter:completion:]_block_invoke.357
+ __90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.371
+ __90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.374
+ __92+[HDSyncStoreEntity activeStoresForRestrictionPredictePruningInProfile:referenceDate:error:]_block_invoke.365
+ __93+[HDMedicationDoseEventEntity _logPersistedDoseEventOnCommitDatabase:doseEvent:persistentID:]_block_invoke.374
+ __94-[HDWorkoutBasicDataSource _workoutDataDestination:requestsSamplesOfType:from:to:transaction:]_block_invoke.431
+ __96-[HDClientAuthorizationOracle performIfAuthorizedToReadObjects:onQueue:usingBlock:errorHandler:]_block_invoke.346
+ __96-[HDClientAuthorizationOracle performIfAuthorizedToSaveObjects:onQueue:usingBlock:errorHandler:]_block_invoke.357
+ __98-[HDClientAuthorizationOracle performIfAuthorizedToDeleteObjects:onQueue:usingBlock:errorHandler:]_block_invoke.360
+ __98-[HDClientAuthorizationOracle(Privileged) updateDefaultAuthorizationStatusesForSource:completion:]_block_invoke.521
+ __98-[HDClientAuthorizationOracle(Privileged) updateDefaultAuthorizationStatusesForSource:completion:]_block_invoke.525
+ __99-[HDDatabase takeAccessibilityAssertionWithOwnerIdentifier:shouldPerformTransaction:timeout:error:]_block_invoke.550
+ __CLASS_METHODS_HDDatabasePruningShow
+ __DATA_HDDatabasePruningShow
+ __HDAddConceptAuthorizationRecordsTable
+ __HDAddExcludedSyncIdentitiesColumnToCloudSyncStores
+ __INSTANCE_METHODS_HDDatabasePruningShow
+ __METACLASS_DATA_HDDatabasePruningShow
+ __OBJC_$_CATEGORY_HKSleepDaySummaryQueryConfiguration_$_CacheSettings
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_HKSleepDaySummaryQueryConfiguration_$_CacheSettings
+ __OBJC_$_CLASS_METHODS_HDAuthorizationStatusRecord
+ __OBJC_$_CLASS_METHODS_HDDatabasePruningShowShim
+ __OBJC_$_CLASS_METHODS_HDDatabasePruningTask
+ __OBJC_$_CLASS_METHODS__HDStaticSyncStore
+ __OBJC_$_INSTANCE_METHODS_HDAnalyticsSubmissionCoordinator(HealthDaemon|Tinker|MedicalID|HeartDaily|HealthService|Authorization|Attachments|HeartRate|NanoSync|SummarySharing|CloudKitCache|CloudSync|Workout|Database)
+ __OBJC_$_INSTANCE_METHODS_HDAuthorizationStatusRecord
+ __OBJC_$_INSTANCE_METHODS_HDDatabasePruningShowDeletedSample
+ __OBJC_$_INSTANCE_METHODS_HDDatabasePruningShowEntity
+ __OBJC_$_INSTANCE_METHODS_HDDatabasePruningShowSyncIdentity
+ __OBJC_$_INSTANCE_METHODS_HDDatabasePruningShowSyncStore
+ __OBJC_$_INSTANCE_METHODS_HDSamplePruningRestrictionPredicate
+ __OBJC_$_INSTANCE_METHODS_HDTypedSyncStoreIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_HDAuthorizationStatusRecord
+ __OBJC_$_INSTANCE_VARIABLES_HDDatabasePruningShowDeletedSample
+ __OBJC_$_INSTANCE_VARIABLES_HDDatabasePruningShowEntity
+ __OBJC_$_INSTANCE_VARIABLES_HDDatabasePruningShowSyncIdentity
+ __OBJC_$_INSTANCE_VARIABLES_HDDatabasePruningShowSyncStore
+ __OBJC_$_INSTANCE_VARIABLES_HDSamplePruningRestrictionPredicate
+ __OBJC_$_INSTANCE_VARIABLES_HDTypedSyncStoreIdentifier
+ __OBJC_$_INSTANCE_VARIABLES__HDMedicationDoseEventEntityEncoder
+ __OBJC_$_PROP_LIST_HDAuthorizationStatusRecord
+ __OBJC_$_PROP_LIST_HDDatabasePruningShowDeletedSample
+ __OBJC_$_PROP_LIST_HDDatabasePruningShowEntity
+ __OBJC_$_PROP_LIST_HDDatabasePruningShowSyncIdentity
+ __OBJC_$_PROP_LIST_HDDatabasePruningShowSyncStore
+ __OBJC_$_PROP_LIST_HDSamplePruningRestrictionPredicate
+ __OBJC_$_PROP_LIST_HDTypedSyncStoreIdentifier
+ __OBJC_$_PROP_LIST_HKSleepDaySummaryQueryConfiguration_$_CacheSettings
+ __OBJC_$_PROTOCOL_CLASS_METHODS_HDSyncStore
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKTypeProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKTypeProtocol
+ __OBJC_$_PROTOCOL_REFS_HKTypeProtocol
+ __OBJC_CLASS_PROTOCOLS_$_HKObject(HDCodingSupport|HDDataEntity|HDExtensions)
+ __OBJC_CLASS_RO_$_HDAuthorizationStatusRecord
+ __OBJC_CLASS_RO_$_HDDatabasePruningShowDeletedSample
+ __OBJC_CLASS_RO_$_HDDatabasePruningShowEntity
+ __OBJC_CLASS_RO_$_HDDatabasePruningShowShim
+ __OBJC_CLASS_RO_$_HDDatabasePruningShowSyncIdentity
+ __OBJC_CLASS_RO_$_HDDatabasePruningShowSyncStore
+ __OBJC_CLASS_RO_$_HDSamplePruningRestrictionPredicate
+ __OBJC_CLASS_RO_$_HDTypedSyncStoreIdentifier
+ __OBJC_LABEL_PROTOCOL_$_HKTypeProtocol
+ __OBJC_METACLASS_RO_$_HDAuthorizationStatusRecord
+ __OBJC_METACLASS_RO_$_HDDatabasePruningShowDeletedSample
+ __OBJC_METACLASS_RO_$_HDDatabasePruningShowEntity
+ __OBJC_METACLASS_RO_$_HDDatabasePruningShowShim
+ __OBJC_METACLASS_RO_$_HDDatabasePruningShowSyncIdentity
+ __OBJC_METACLASS_RO_$_HDDatabasePruningShowSyncStore
+ __OBJC_METACLASS_RO_$_HDSamplePruningRestrictionPredicate
+ __OBJC_METACLASS_RO_$_HDTypedSyncStoreIdentifier
+ __OBJC_PROTOCOL_$_HKTypeProtocol
+ __ZN6health18TransactionalCacheIyNS_8FilePageEE14_pruneIfNeededENS2_10PruneScopeEmPNS2_10CacheEntryE
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IP16_HDWrappedSourceS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_10shared_ptrIN6health13WriteAheadLog11TransactionEEES9_S9_EENS_4pairIT_T1_EESB_T0_SC_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_10unique_ptrIN6health18TransactionalCacheIyNS5_8FilePageEE10CacheEntryENS_14default_deleteIS9_EEEESD_SD_EENS_4pairIT_T1_EESF_T0_SG_
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__114default_deleteIN6health18TransactionalCacheIyNS1_8FilePageEE10CacheEntryEEclB8ne190102EPS5_
+ __ZNKSt3__114default_deleteINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne190102EPS6_
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne190102IS4_EENS_12basic_stringIcS2_T_EERKS8_
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB8ne190102Ev
+ __ZNKSt3__121__unordered_map_equalIU8__strongP8NSStringNS_17__hash_value_typeIS3_NS_5dequeI19HDRawQuantitySampleNS_9allocatorIS6_EEEEEE13HDStringEqual12HDStringHashLb1EEclB8ne190102ERKSA_RU8__strongKS2_
+ __ZNKSt3__121__unordered_map_equalIU8__strongP8NSStringNS_17__hash_value_typeIS3_xEE13HDStringEqual12HDStringHashLb1EEclB8ne190102ERKS5_RU8__strongKS2_
+ __ZNKSt3__16__loopIcE13__init_repeatB8ne190102ERNS_7__stateIcEE
+ __ZNKSt3__16vectorI13HKRawIntervalIdENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI15HistogramBucketNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI16_HDWrappedSourceNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI19HDRawDistanceSampleNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorI19HDRawQuantitySampleNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS3_EE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsDiscreteE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsPresenceE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EEE16_SampleRemainderENS_9allocatorIS8_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorISB_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorISB_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_SampleRemainderENS_9allocatorIS8_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_SampleRemainderENS_9allocatorIS8_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI22HDStatisticsCumulativeE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI23HDStatisticsPercentilesE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN6health10FileExtentENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN6health13WriteAheadLog9PageEntryENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN6health18DataStoreInspector15DataSeriesEntryENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10shared_ptrIN6health13WriteAheadLog11TransactionEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_10unique_ptrIN6health18TransactionalCacheIyNS2_8FilePageEE10CacheEntryENS_14default_deleteIS6_EEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairIccEENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairImPKcEENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_5tupleIJxU8__strongP15HKDeletedObjectEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_5tupleIJxU8__strongP8HKSampleEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_7__stateIcEENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_9sub_matchINS_11__wrap_iterIPKcEEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_9sub_matchIPKcEENS_9allocatorIS4_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIU8__strongP8HKSourceNS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt9type_infoeqB8ne190102ERKS_
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt16invalid_argumentC1B8ne190102EPKc
+ __ZNSt3__110__function12__value_funcIF21_HDRawLocationDatumV1dS2_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIF21_HDRawLocationDatumV2dS2_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIF27_HDRawQuantitySampleValueV1dS2_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_13match_resultsINS_11__wrap_iterIPKcEENS5_INS_9sub_matchISC_EEEEEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne190102ERKSD_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalES7_EEC2B8ne190102ERKS9_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalES7_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne190102ERKSD_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalES7_EEC2B8ne190102ERKS9_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalES7_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne190102ERKSD_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalES7_EEC2B8ne190102ERKS9_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalES7_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne190102ERKSD_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalES7_EEC2B8ne190102ERKS9_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalES7_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne190102ERKSD_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalES7_EEC2B8ne190102ERKS9_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalES7_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne190102ERKSD_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalES7_EEC2B8ne190102ERKS9_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalES7_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI24HDStatisticsTimeIntervalS3_ERK20HDStatisticsRelativeIS4_EEEC2B8ne190102ERKSC_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI24HDStatisticsTimeIntervalS3_ERK20HDStatisticsRelativeIS4_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI24HDStatisticsTimeIntervalS3_ES6_EEC2B8ne190102ERKS8_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI24HDStatisticsTimeIntervalS3_ES6_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne190102ERKSD_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalES7_EEC2B8ne190102ERKS9_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalES7_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS7_EEEC2B8ne190102ERKSF_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS7_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalES9_EEC2B8ne190102ERKSB_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalES9_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS7_EEEC2B8ne190102ERKSF_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS7_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalES9_EEC2B8ne190102ERKSB_
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalES9_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsDiscreteRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsDiscreteRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsDiscreteRK20HDStatisticsRelativeIS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsDiscreteS4_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsPresenceRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsPresenceRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsPresenceRK20HDStatisticsRelativeIS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK20HDStatisticsPresenceS4_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK22HDStatisticsCumulativeRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK22HDStatisticsCumulativeRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK22HDStatisticsCumulativeRK20HDStatisticsRelativeIS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK22HDStatisticsCumulativeS4_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK22HDStatisticsNoiseLevelRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK22HDStatisticsNoiseLevelRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK22HDStatisticsNoiseLevelRK20HDStatisticsRelativeIS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK22HDStatisticsNoiseLevelS4_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK23HDStatisticsPercentilesRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK23HDStatisticsPercentilesRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK23HDStatisticsPercentilesRK20HDStatisticsRelativeIS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK23HDStatisticsPercentilesS4_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK23HDStatisticsSleepStagesRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK23HDStatisticsSleepStagesRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK23HDStatisticsSleepStagesRK20HDStatisticsRelativeIS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK23HDStatisticsSleepStagesS4_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI20HDStatisticsDiscreteS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI20HDStatisticsPresenceS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI22HDStatisticsCumulativeS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI22HDStatisticsNoiseLevelS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI23HDStatisticsPercentilesS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI23HDStatisticsSleepStagesS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI33HDStatisticsAverageSampleDurationS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersES2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersES2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedIS2_S2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscreteS2_EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresenceS2_EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulativeS2_EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevelS2_EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentilesS2_EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStagesS2_EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDurationS2_EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersES2_EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersES2_EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_S2_EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeIS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalS4_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK33HDStatisticsAverageSampleDurationRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK33HDStatisticsAverageSampleDurationRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK33HDStatisticsAverageSampleDurationRK20HDStatisticsRelativeIS2_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK33HDStatisticsAverageSampleDurationS4_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersERK20HDStatisticsCombinedIS4_24HDStatisticsTimeIntervalEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersERK20HDStatisticsRelativeI20HDStatisticsCombinedIS4_24HDStatisticsTimeIntervalEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersERK20HDStatisticsRelativeIS4_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersES6_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersERK20HDStatisticsCombinedIS4_24HDStatisticsTimeIntervalEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersERK20HDStatisticsRelativeI20HDStatisticsCombinedIS4_24HDStatisticsTimeIntervalEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersERK20HDStatisticsRelativeIS4_EEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFRK42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersES6_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbN6health15BlockAccessFile14IntegrityErrorExxRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbN6health9DataStore14IntegrityErrorENS2_12BlockPointerERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEC2B8ne190102ERKSF_
+ __ZNSt3__110__function12__value_funcIFbN6health9DataStore14IntegrityErrorENS2_12BlockPointerERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRKdRK21_HDRawLocationDatumV0EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRKdRK21_HDRawLocationDatumV1EEC2B8ne190102ERKS8_
+ __ZNSt3__110__function12__value_funcIFbRKdRK21_HDRawLocationDatumV1EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRKdRK21_HDRawLocationDatumV2EEC2B8ne190102ERKS8_
+ __ZNSt3__110__function12__value_funcIFbRKdRK21_HDRawLocationDatumV2EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRKdRK27_HDRawQuantitySampleValueV1EEC2B8ne190102ERKS8_
+ __ZNSt3__110__function12__value_funcIFbRKdRK27_HDRawQuantitySampleValueV1EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRKdS3_EEC2B8ne190102ERKS5_
+ __ZNSt3__110__function12__value_funcIFbRKdS3_EED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRN6health15BlockAccessFile16WriteTransactionEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRN6health17TransactionalFile16WriteTransactionEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRN6health9DataStore16WriteTransactionEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRN6health9DataStore20MutableSampleHistoryI25LocationHistoryBehaviorV1EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRN6health9DataStore20MutableSampleHistoryI25LocationHistoryBehaviorV2EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRN6health9DataStore20MutableSampleHistoryI29QuantitySampleValueBehaviorV0EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbRN6health9DataStore20MutableSampleHistoryI29QuantitySampleValueBehaviorV1EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbvEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbyEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFbyRKyRKN6health8FilePageEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFdddEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKN6health10FileExtentEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKN6health15BlockAccessFile15ReadTransactionEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKN6health17TransactionalFile15ReadTransactionEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore13SampleHistoryI25LocationHistoryBehaviorV0EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore13SampleHistoryI25LocationHistoryBehaviorV1EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore13SampleHistoryI25LocationHistoryBehaviorV2EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore13SampleHistoryI29QuantitySampleValueBehaviorV0EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore13SampleHistoryI29QuantitySampleValueBehaviorV1EEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore15ReadTransactionEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore16ObjectIdentifierENS2_12BlockPointerEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEC2B8ne190102ERKSB_
+ __ZNSt3__110__function12__value_funcIFvRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvxN6health13WriteAheadLog9PageEntryEEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvyEEC2B8ne190102ERKS3_
+ __ZNSt3__110__function12__value_funcIFvyEED2B8ne190102Ev
+ __ZNSt3__110__function12__value_funcIFvyRKN6health8FilePageEEEC2B8ne190102ERKS7_
+ __ZNSt3__110__function12__value_funcIFvyRKN6health8FilePageEEED2B8ne190102Ev
+ __ZNSt3__110shared_ptrINS_13__empty_stateIcEEE5resetB8ne190102IS2_Li0EEEvPT_
+ __ZNSt3__110shared_ptrINS_13__empty_stateIcEEEC2B8ne190102IS2_Li0EEEPT_
+ __ZNSt3__110shared_ptrIhEC2B8ne190102IhNS_14default_deleteIA_hEELi0EEEPT_T0_
+ __ZNSt3__110unique_ptrIN6health9DataStoreENS_14default_deleteIS2_EEE5resetB8ne190102EPS2_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne190102EPSC_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne190102EPSC_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne190102EPSC_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne190102EPSC_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne190102EPSC_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne190102EPSC_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI24HDStatisticsTimeIntervalS7_EEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne190102EPSC_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsDiscreteEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsPresenceEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS8_EEEEPvEENS_22__hash_node_destructorINS_9allocatorISD_EEEEE5resetB8ne190102EPSD_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne190102EPSE_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISG_EEEEE5resetB8ne190102EPSG_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISG_EEEEE5resetB8ne190102EPSG_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsDiscreteEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsPresenceEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI22HDStatisticsCumulativeEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI23HDStatisticsPercentilesEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI23HDStatisticsSleepStagesEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEEEPvEENS_22__hash_node_destructorINS_9allocatorISD_EEEEE5resetB8ne190102EPSD_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEEEPvEENS_22__hash_node_destructorINS_9allocatorISD_EEEEE5resetB8ne190102EPSD_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString22HDStatisticsCumulativeEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString23HDStatisticsPercentilesEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString23HDStatisticsSleepStagesEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString24HDStatisticsTimeIntervalEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString33HDStatisticsAverageSampleDurationEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringxEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIxU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIN6health12InMemoryFileEEEEEPvEENS_22__tree_node_destructorINS6_ISF_EEEEE5resetB8ne190102EPSF_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne190102EPS9_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEEPvEENS_22__tree_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEEPvEENS_22__tree_node_destructorINS_9allocatorISB_EEEEE5resetB8ne190102EPSB_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEEEPvEENS_22__tree_node_destructorINS_9allocatorISA_EEEEE5resetB8ne190102EPSA_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsRelativeI22HDStatisticsNoiseLevelEEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne190102EPS8_
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx22HDStatisticsNoiseLevelEEPvEENS_22__tree_node_destructorINS_9allocatorIS6_EEEEE5resetB8ne190102EPS6_
+ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE19__parse_QUOTED_CHARIPKcEET_S7_S7_
+ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEEC2B8ne190102EPKcNS_15regex_constants18syntax_option_typeE
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIN6health12InMemoryFileEEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKx20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKx20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKx20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKx20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKx20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIKx20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI24HDStatisticsTimeIntervalS6_EEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS7_EEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI23HDStatisticsPercentilesEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI24HDStatisticsTimeIntervalEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString23HDStatisticsPercentilesEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_4pairIU8__strongKP8NSString24HDStatisticsTimeIntervalEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8ne190102INS_7__stateIcEELi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne190102INS_11__wrap_iterIPKcEESA_EEvT_T0_m
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne190102INS_11__wrap_iterIPcEES9_EEvT_T0_m
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne190102IPKcS8_EEvT_T0_m
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne190102IPcS7_EEvT_T0_m
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__insert_from_safe_copyB8ne190102INS_11__wrap_iterIPKcEESA_EENS7_IPcEEmmT_T0_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ENS_24__uninitialized_size_tagEmRKS4_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
+ __ZNSt3__113__nth_elementB8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPdEEEEvT1_S8_S8_T0_
+ __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__113match_resultsINS_11__wrap_iterIPKcEENS_9allocatorINS_9sub_matchIS4_EEEEE8__assignB8ne190102IS3_NS5_INS6_IS3_EEEEEEvS4_S4_RKNS0_IT_T0_EEb
+ __ZNSt3__114__split_bufferINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB8ne190102EPS6_
+ __ZNSt3__114__split_bufferINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB8ne190102EPS6_
+ __ZNSt3__114__split_bufferINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB8ne190102EPS6_
+ __ZNSt3__114__split_bufferINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB8ne190102EPS6_
+ __ZNSt3__114__split_bufferINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EERNS5_IS8_EEED2Ev
+ __ZNSt3__115insert_iteratorINS_3setIyNS_4lessIyEENS_9allocatorIyEEEEEaSB8ne190102ERKy
+ __ZNSt3__116__deque_iteratorI39HDQuantitySampleAttenuationEngineSamplePKS1_RS2_PKS3_lLl102EEpLB8ne190102El
+ __ZNSt3__116__deque_iteratorI39HDQuantitySampleAttenuationEngineSamplePS1_RS1_PS2_lLl102EEpLB8ne190102El
+ __ZNSt3__116__pad_and_outputB8ne190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__116__set_differenceB8ne190102INS_17_ClassicAlgPolicyENS_6__lessIvvEERNS_21__tree_const_iteratorIyPNS_11__tree_nodeIyPvEElEESA_SA_SA_RNS_15insert_iteratorINS_3setIyNS_4lessIyEENS_9allocatorIyEEEEEEEENS_4pairIu14__remove_cvrefIT1_Eu14__remove_cvrefIT5_EEEOSL_OT2_OT3_OT4_OSN_OT0_
+ __ZNSt3__118__for_each_segmentB8ne190102INS_16__deque_iteratorI39HDQuantitySampleAttenuationEngineSamplePKS2_RS3_PKS4_lLl102EEENS_11__copy_implINS_17_ClassicAlgPolicyEE12_CopySegmentIS8_NS1_IS2_PS2_RS2_PSD_lLl102EEEEEEEvT_SI_T0_
+ __ZNSt3__118generate_canonicalB8ne190102IdLm53ENS_26linear_congruential_engineIjLj48271ELj0ELj2147483647EEEEET_RT1_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI13HKRawIntervalIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI15HistogramBucketEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI16_HDWrappedSourceEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI19HDRawDistanceSampleEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI19HDRawQuantitySampleEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsDiscreteE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsPresenceE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSG_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSG_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI22HDStatisticsCumulativeE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI23HDStatisticsPercentilesE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN6health10FileExtentEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN6health13WriteAheadLog9PageEntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_10unique_ptrIN6health18TransactionalCacheIyNS3_8FilePageEE10CacheEntryENS_14default_deleteIS7_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEES7_EEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIccEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairImPKcEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_5tupleIJxU8__strongP15HKDeletedObjectEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_5tupleIJxU8__strongP8HKSampleEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_9sub_matchINS_11__wrap_iterIPKcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_9sub_matchIPKcEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP19HDRawQuantitySampleEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIP39HDQuantitySampleAttenuationEngineSampleEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPN6health12BlockPointerEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPNS_11__thread_idEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPNS_5tupleIJddfEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPNS_7__stateIcEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIlEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIxEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__shared_weak_count16__release_sharedB8ne190102Ev
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE11EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE12EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE14EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE15EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE16EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE17EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE1EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE2EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE3EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE4EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE5EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE6EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE7EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE8EEEvv
+ __ZNSt3__119__throw_regex_errorB8ne190102ILNS_15regex_constants10error_typeE9EEEvv
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
+ __ZNSt3__120__bracket_expressionIcNS_12regex_traitsIcEEE10__add_charB8ne190102Ec
+ __ZNSt3__120__bracket_expressionIcNS_12regex_traitsIcEEE13__add_digraphB8ne190102Ecc
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8HKSource16_HDWrappedSourceEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI22HDStatisticsNoiseLevelEEEPvEEEEEclB8ne190102EPSC_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString22HDStatisticsNoiseLevelEEPvEEEEEclB8ne190102EPSA_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringNS_5dequeI19HDRawQuantitySampleNS1_IS8_EEEEEEPvEEEEEclB8ne190102EPSD_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyN6health18TransactionalCacheIyNS4_8FilePageEE9CacheLineEEEPvEEEEEclB8ne190102EPSB_
+ __ZNSt3__122__lower_bound_onesidedB8ne190102INS_17_ClassicAlgPolicyENS_21__tree_const_iteratorIyPNS_11__tree_nodeIyPvEElEES7_yKNS_10__identityENS_6__lessIvvEEEET0_SC_T1_RKT2_RT4_RT3_
+ __ZNSt3__124__copy_move_unwrap_itersB8ne190102INS_11__copy_implINS_17_ClassicAlgPolicyEEEPK39HDQuantitySampleAttenuationEngineSampleS6_NS_16__deque_iteratorIS4_PS4_RS4_PS8_lLl102EEELi0EEENS_4pairIT0_T2_EESD_T1_SE_
+ __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__124__sort5_maybe_branchlessB8ne190102INS_17_ClassicAlgPolicyERZ51-[HDStatisticsCollectionCalculator orderSourceIDs:]E3$_0PxLi0EEEvT1_S5_S5_S5_S5_T0_
+ __ZNSt3__125__throw_bad_function_callB8ne190102Ev
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZ51-[HDStatisticsCollectionCalculator orderSourceIDs:]E3$_0PxEEbT1_S5_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEbT1_SE_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEbT1_SE_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsDiscreteE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsPresenceE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEbT1_SF_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEbT1_SI_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEbT1_SI_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEbT1_SI_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEbT1_SI_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEbT1_SF_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEbT1_SF_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEbT1_SF_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEbT1_SF_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsCumulativeE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsPercentilesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsDiscreteE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsPresenceE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEbT1_SO_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEbT1_SR_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEbT1_SR_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsDiscreteEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsPresenceEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsCumulativeEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsPercentilesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEbT1_SO_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEbT1_SO_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsCumulativeE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsNoiseLevelE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsPercentilesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsSleepStagesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI24HDStatisticsTimeIntervalE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI33HDStatisticsAverageSampleDurationE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__128__invoke_void_return_wrapperIbLb0EE6__callB8ne190102IJRZN6health9DataStore43accessSampleHistoryWithIdentifierForWritingI25LocationHistoryBehaviorV1EEbRKNS4_16ObjectIdentifierEbNS_8functionIFbRNS4_20MutableSampleHistoryIT_EEEEEEUlRNS4_16WriteTransactionEE_SI_EEEbDpOT_
+ __ZNSt3__128__invoke_void_return_wrapperIvLb1EE6__callB8ne190102IJRZNK6health9DataStore43accessSampleHistoryWithIdentifierForReadingI25LocationHistoryBehaviorV1EEbRKNS4_16ObjectIdentifierENS_8functionIFvRKNS4_13SampleHistoryIT_EEEEEEUlRKNS4_15ReadTransactionEE_SK_EEEvDpOT_
+ __ZNSt3__128__invoke_void_return_wrapperIvLb1EE6__callB8ne190102IJRZNK6health9DataStore43accessSampleHistoryWithIdentifierForReadingI25LocationHistoryBehaviorV2EEbRKNS4_16ObjectIdentifierENS_8functionIFvRKNS4_13SampleHistoryIT_EEEEEEUlRKNS4_15ReadTransactionEE_SK_EEEvDpOT_
+ __ZNSt3__128__invoke_void_return_wrapperIvLb1EE6__callB8ne190102IJRZNK6health9DataStore43accessSampleHistoryWithIdentifierForReadingI29QuantitySampleValueBehaviorV0EEbRKNS4_16ObjectIdentifierENS_8functionIFvRKNS4_13SampleHistoryIT_EEEEEEUlRKNS4_15ReadTransactionEE_SK_EEEvDpOT_
+ __ZNSt3__128__invoke_void_return_wrapperIvLb1EE6__callB8ne190102IJRZNK6health9DataStore43accessSampleHistoryWithIdentifierForReadingI29QuantitySampleValueBehaviorV1EEbRKNS4_16ObjectIdentifierENS_8functionIFvRKNS4_13SampleHistoryIT_EEEEEEUlRKNS4_15ReadTransactionEE_SK_EEEvDpOT_
+ __ZNSt3__134__uninitialized_allocator_relocateB8ne190102INS_9allocatorI15HistogramBucketEES2_EEvRT_PT0_S7_S7_
+ __ZNSt3__138__set_intersection_add_output_if_equalB8ne190102INS_21__tree_const_iteratorIyPNS_11__tree_nodeIyPvEElEES6_NS_15insert_iteratorINS_3setIyNS_4lessIyEENS_9allocatorIyEEEEEEEEvbRT_RT0_RT1_Rb
+ __ZNSt3__13mapIyN6health18DataStoreInspector15DataSeriesEntryENS_4lessIyEENS_9allocatorINS_4pairIKyS3_EEEEEC2B8ne190102ERKSB_
+ __ZNSt3__13setIyNS_4lessIyEENS_9allocatorIyEEEC2B8ne190102ERKS5_
+ __ZNSt3__15dequeI19HDRawQuantitySampleNS_9allocatorIS1_EEED2B8ne190102Ev
+ __ZNSt3__15dequeI39HDQuantitySampleAttenuationEngineSampleNS_9allocatorIS1_EEE18__append_with_sizeB8ne190102INS_16__deque_iteratorIS1_PKS1_RS7_PKS8_lLl102EEEEEvT_m
+ __ZNSt3__15dequeI39HDQuantitySampleAttenuationEngineSampleNS_9allocatorIS1_EEED2B8ne190102Ev
+ __ZNSt3__15dequeIN6health12BlockPointerENS_9allocatorIS2_EEE26__maybe_remove_front_spareB8ne190102Eb
+ __ZNSt3__15dequeIN6health12BlockPointerENS_9allocatorIS2_EEED2B8ne190102Ev
+ __ZNSt3__15dequeINS_11__thread_idENS_9allocatorIS1_EEED2B8ne190102Ev
+ __ZNSt3__15dequeINS_7__stateIcEENS_9allocatorIS2_EEED2B8ne190102Ev
+ __ZNSt3__16vectorI13HKRawIntervalIdENS_9allocatorIS2_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI13HKRawIntervalIdENS_9allocatorIS2_EEE16__init_with_sizeB8ne190102IPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorI13HKRawIntervalIdENS_9allocatorIS2_EEE18__assign_with_sizeB8ne190102IPS2_S7_EEvT_T0_l
+ __ZNSt3__16vectorI16_HDWrappedSourceNS_9allocatorIS1_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorI16_HDWrappedSourceNS_9allocatorIS1_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorI16_HDWrappedSourceNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorI16_HDWrappedSourceNS_9allocatorIS1_EEE9push_backB8ne190102ERKS1_
+ __ZNSt3__16vectorI19HDRawQuantitySampleNS_9allocatorIS1_EEE16__init_with_sizeB8ne190102IPS1_S6_EEvT_T0_m
+ __ZNSt3__16vectorINS_10shared_ptrIN6health13WriteAheadLog11TransactionEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_10shared_ptrIN6health13WriteAheadLog11TransactionEEENS_9allocatorIS5_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN6health18TransactionalCacheIyNS2_8FilePageEE10CacheEntryENS_14default_deleteIS6_EEEENS_9allocatorIS9_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN6health18TransactionalCacheIyNS2_8FilePageEE10CacheEntryENS_14default_deleteIS6_EEEENS_9allocatorIS9_EEE22__base_destruct_at_endB8ne190102EPS9_
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_4pairImPKcEENS_9allocatorIS4_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorINS_4pairImPKcEENS_9allocatorIS4_EEE16__init_with_sizeB8ne190102IPS4_S9_EEvT_T0_m
+ __ZNSt3__16vectorINS_5tupleIJxU8__strongP15HKDeletedObjectEEENS_9allocatorIS5_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorINS_5tupleIJxU8__strongP15HKDeletedObjectEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_5tupleIJxU8__strongP15HKDeletedObjectEEENS_9allocatorIS5_EEE16__init_with_sizeB8ne190102IPS5_SA_EEvT_T0_m
+ __ZNSt3__16vectorINS_5tupleIJxU8__strongP8HKSampleEEENS_9allocatorIS5_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorINS_5tupleIJxU8__strongP8HKSampleEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_5tupleIJxU8__strongP8HKSampleEEENS_9allocatorIS5_EEE16__init_with_sizeB8ne190102IPS5_SA_EEvT_T0_m
+ __ZNSt3__16vectorINS_7__stateIcEENS_9allocatorIS2_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS_9sub_matchINS_11__wrap_iterIPKcEEEENS_9allocatorIS6_EEE16__init_with_sizeB8ne190102IPS6_SB_EEvT_T0_m
+ __ZNSt3__16vectorINS_9sub_matchIPKcEENS_9allocatorIS4_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorINS_9sub_matchIPKcEENS_9allocatorIS4_EEE16__init_with_sizeB8ne190102IPS4_S9_EEvT_T0_m
+ __ZNSt3__16vectorIU8__strongP8HKSourceNS_9allocatorIS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB8ne190102IPdS5_EEvT_T0_m
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE18__assign_with_sizeB8ne190102IPdS5_EEvT_T0_l
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEEC2B8ne190102Em
+ __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne190102IPxS5_EEvT_T0_m
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPdEEEEjT1_S8_S8_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZ51-[HDStatisticsCollectionCalculator orderSourceIDs:]E3$_0PxEEjT1_S5_S5_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEjT1_SE_SE_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEjT1_SE_SE_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsDiscreteE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsPresenceE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEjT1_SF_SF_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEjT1_SI_SI_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEjT1_SI_SI_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEjT1_SI_SI_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEjT1_SI_SI_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEjT1_SF_SF_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEjT1_SF_SF_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEjT1_SF_SF_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEjT1_SF_SF_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsCumulativeE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEjT1_SB_SB_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsPercentilesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEjT1_SB_SB_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsDiscreteE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsPresenceE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEjT1_SO_SO_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEjT1_SR_SR_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEjT1_SR_SR_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsDiscreteEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsPresenceEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsCumulativeEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsPercentilesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEjT1_SO_SO_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEjT1_SO_SO_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsCumulativeE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsNoiseLevelE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsPercentilesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsSleepStagesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI24HDStatisticsTimeIntervalE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI33HDStatisticsAverageSampleDurationE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
+ __ZNSt3__17__sort3B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZ51-[HDStatisticsCollectionCalculator orderSourceIDs:]E3$_0PxEEvT1_S5_S5_S5_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsDiscreteE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsPresenceE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEvT1_SI_SI_SI_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEvT1_SI_SI_SI_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEvT1_SI_SI_SI_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEvT1_SI_SI_SI_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEvT1_SF_SF_SF_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEvT1_SF_SF_SF_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsCumulativeE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEvT1_SB_SB_SB_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsPercentilesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEvT1_SB_SB_SB_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsDiscreteE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsPresenceE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEvT1_SR_SR_SR_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEvT1_SR_SR_SR_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsDiscreteEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsPresenceEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsCumulativeEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsPercentilesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsCumulativeE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsNoiseLevelE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsPercentilesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsSleepStagesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI24HDStatisticsTimeIntervalE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI33HDStatisticsAverageSampleDurationE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
+ __ZNSt3__17__sort4B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsDiscreteE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsPresenceE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_SF_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEvT1_SI_SI_SI_SI_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEvT1_SI_SI_SI_SI_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEvT1_SI_SI_SI_SI_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEvT1_SI_SI_SI_SI_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEvT1_SF_SF_SF_SF_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_SF_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEvT1_SF_SF_SF_SF_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_SF_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsCumulativeE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEvT1_SB_SB_SB_SB_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsPercentilesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEvT1_SB_SB_SB_SB_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsDiscreteE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsPresenceE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_SO_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEvT1_SR_SR_SR_SR_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEvT1_SR_SR_SR_SR_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsDiscreteEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsPresenceEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsCumulativeEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsPercentilesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_SO_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_SO_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsCumulativeE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsNoiseLevelE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsPercentilesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsSleepStagesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI24HDStatisticsTimeIntervalE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI33HDStatisticsAverageSampleDurationE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
+ __ZNSt3__17__sort5B8ne190102INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
+ __ZNSt3__1eqB8ne190102INS_9allocatorIcEEEEbRKNS_12basic_stringIcNS_11char_traitsIcEET_EES9_
+ __ZNSt3__1ssB8ne190102IcNS_11char_traitsIcEEEEDaNS_17basic_string_viewIT_T0_EENS_13type_identityIS7_E4typeE
+ __ZNSt3__1ssB8ne190102IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __ZZNK6health13WriteAheadLog18runReadTransactionENSt3__18functionIFvyEEEENK3$_1clEv
+ __ZZZNK6health17TransactionalFile25readTransactionWithLambdaENSt3__18functionIFvRKNS0_15ReadTransactionEEEEENK3$_0clEyENKUlvE0_clEv
+ ___101+[HDDataSyncEntity _pruningPredicateWithRestrictionPredicates:matchOnlyNilDatesWithoutShardInterval:]_block_invoke
+ ___103-[HDDatabaseControlServer remote_classifiedDeletedSampleInfoWithReferenceDate:anchor:limit:completion:]_block_invoke
+ ___110-[HDAuthorizationManager filteredAuthorizedObjectsForClient:anchor:bundleIdentifier:clientEntitlements:error:]_block_invoke
+ ___112-[HDDatabasePruningCoordinator _pruneProfilesWithIdentifiers:takeAccessibilityAssertion:shouldDefer:completion:]_block_invoke
+ ___112-[HDDatabasePruningCoordinator _pruneProfilesWithIdentifiers:takeAccessibilityAssertion:shouldDefer:completion:]_block_invoke_2
+ ___115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke
+ ___115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke_2
+ ___116-[HDDatabaseControlServer remote_deletedSampleDetailWithReferenceDate:matchingPredicatesOnly:sampleUUID:completion:]_block_invoke
+ ___118-[HDDatabasePruningTask _pruneDatabaseUsingMinAnchorWithNowDate:prunedObjectLimit:prunedObjectTransactionLimit:error:]_block_invoke
+ ___119-[HDDatabaseControlServer remote_deletedSamplesDetailWithReferenceDate:matchingPredicatesOnly:anchor:limit:completion:]_block_invoke
+ ___123+[HDCloudSyncStore createOrUpdateShardStoresForProfile:throughDate:ownerIdentifier:containerIdentifier:syncIdentity:error:]_block_invoke
+ ___123+[HDCloudSyncStore createOrUpdateShardStoresForProfile:throughDate:ownerIdentifier:containerIdentifier:syncIdentity:error:]_block_invoke_2
+ ___124-[HDDatabasePruningTask _pruneDatabaseUsingRestrictionPredicatesWithNowDate:prunedObjectTransactionLimit:shouldDefer:error:]_block_invoke
+ ___124-[HDDatabasePruningTask enqueueMaintenanceOperationOnCoordinator:takeAccessibilityAssertion:nowDate:shouldDefer:completion:]_block_invoke
+ ___132-[HDDefaultAuthorizationSchemaProvider filteredAuthorizedObjectsForClient:anchor:bundleIdentifier:clientEntitlements:profile:error:]_block_invoke
+ ___138-[HDDatabasePruningTask pruneDatabaseWithAccessibilityAssertion:nowDate:prunedObjectLimit:prunedObjectTransactionLimit:shouldDefer:error:]_block_invoke
+ ___140+[HDCloudSyncStore _syncStoreForProfile:storeIdentifier:ownerIdentifier:syncIdentity:containerIdentifier:shardPredicate:creationDate:error:]_block_invoke
+ ___140+[HDCloudSyncStore _syncStoreForProfile:storeIdentifier:ownerIdentifier:syncIdentity:containerIdentifier:shardPredicate:creationDate:error:]_block_invoke_2
+ ___40-[HDCloudSyncPushSequenceOperation main]_block_invoke_2
+ ___56+[HDDatabasePruningShowShim _syncStoresInProfile:error:]_block_invoke
+ ___56+[HDDatabasePruningShowShim _syncStoresInProfile:error:]_block_invoke_2
+ ___56-[HDDatabasePruningTask _instantiateActiveStores:error:]_block_invoke
+ ___59+[HDDatabasePruningShowShim syncIdentitiesInProfile:error:]_block_invoke
+ ___61+[HDSyncAnchorEntity frozenAnchorMapPerStoreInProfile:error:]_block_invoke
+ ___61+[HDSyncAnchorEntity frozenAnchorMapPerStoreInProfile:error:]_block_invoke_2
+ ___62+[HDCloudSyncStore syncStoreForProfile:storeIdentifier:error:]_block_invoke
+ ___62+[HDCloudSyncStore syncStoreForProfile:storeIdentifier:error:]_block_invoke_2
+ ___62+[HDDatabasePruningShowShim _instantiateStores:profile:error:]_block_invoke
+ ___69+[HDDatabasePruningShowShim deletedSampleInProfile:sampleUUID:error:]_block_invoke
+ ___70+[HDSyncAnchorEntity latestFrozenAnchorUpdatePerStoreInProfile:error:]_block_invoke
+ ___70+[HDSyncAnchorEntity latestFrozenAnchorUpdatePerStoreInProfile:error:]_block_invoke_2
+ ___72+[HDDatabasePruningShowShim _persistentIDForSyncIdentity:profile:error:]_block_invoke
+ ___72+[HDDatabasePruningShowShim deletedSamplesInProfile:anchor:limit:error:]_block_invoke
+ ___72-[HDClientAuthorizationOracle authorizationStatusRecordsForTypes:error:]_block_invoke
+ ___73+[HDDeletedSampleEntity deletedSampleInProfile:sampleUUID:error:handler:]_block_invoke
+ ___73+[HDDeletedSampleEntity deletedSampleInProfile:sampleUUID:error:handler:]_block_invoke_2
+ ___75-[HDDatabaseControlServer remote_pruneSamplesWithReferenceDate:completion:]_block_invoke
+ ___75-[HDWorkoutBasicDataSource workoutSession:didChangeToState:fromState:date:]_block_invoke_2
+ ___80-[HDDatabaseControlServer remote_deletedSampleInfoWithReferenceDate:completion:]_block_invoke
+ ___81-[HDDatabasePruningTask _pruningRestrictionPredicatesFromStores:forEntity:error:]_block_invoke
+ ___82+[HDSyncStoreEntity activeStoresForMaxAnchorPruningInProfile:referenceDate:error:]_block_invoke
+ ___82+[HDSyncStoreEntity activeStoresForMaxAnchorPruningInProfile:referenceDate:error:]_block_invoke_2
+ ___82+[HDSyncStoreEntity activeStoresForMaxAnchorPruningInProfile:referenceDate:error:]_block_invoke_3
+ ___84+[HDCloudSyncStoreEntity cacheExcludedSyncIdentities:storeIdentifier:profile:error:]_block_invoke
+ ___84+[HDSyncStoreEntity syncStoreEntityWithUUID:type:creationDate:healthDatabase:error:]_block_invoke
+ ___84+[HDSyncStoreEntity syncStoreEntityWithUUID:type:creationDate:healthDatabase:error:]_block_invoke_2
+ ___85+[HDCloudSyncStoreEntity cacheExcludedSyncIdentities:storeIdentifier:database:error:]_block_invoke
+ ___85+[HDDatabasePruningShowShim syncStoresInProfile:shouldIncludeEntityIdentifier:error:]_block_invoke
+ ___85+[HDDatabasePruningShowShim syncStoresInProfile:shouldIncludeEntityIdentifier:error:]_block_invoke_2
+ ___85+[HDDatabasePruningShowShim syncStoresInProfile:shouldIncludeEntityIdentifier:error:]_block_invoke_3
+ ___85+[HDDatabasePruningShowShim syncStoresInProfile:shouldIncludeEntityIdentifier:error:]_block_invoke_4
+ ___85+[HDDeletedSampleEntity enumerateDeletedSamplesInProfile:anchor:limit:error:handler:]_block_invoke
+ ___85+[HDDeletedSampleEntity enumerateDeletedSamplesInProfile:anchor:limit:error:handler:]_block_invoke_2
+ ___85+[HDDeletedSampleEntity enumerateDeletedSamplesInProfile:anchor:limit:error:handler:]_block_invoke_3
+ ___86-[HDDatabaseControlServer remote_showWithReferenceDate:deletedSamplesOnly:completion:]_block_invoke
+ ___87+[HDCloudSyncStoreEntity cachedExcludedSyncIdentitiesForStoreIdentifier:profile:error:]_block_invoke
+ ___87+[HDDatabasePruningShowShim entitiesInProfile:referenceDate:shouldIncludeEntity:error:]_block_invoke
+ ___87-[HDDatabaseControlServer remote_showAndDeletedSampleInfoWithReferenceDate:completion:]_block_invoke
+ ___88+[HDCloudSyncStoreEntity cachedExcludedSyncIdentitiesForStoreIdentifier:database:error:]_block_invoke
+ ___92+[HDSyncStoreEntity activeStoresForRestrictionPredictePruningInProfile:referenceDate:error:]_block_invoke
+ ___92+[HDSyncStoreEntity activeStoresForRestrictionPredictePruningInProfile:referenceDate:error:]_block_invoke_2
+ ___97+[HDDatabasePruningShowShim activeStoresForRestrictionPredicatesWithProfile:referenceDate:error:]_block_invoke
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88r96r104r112r_e35_B24?0"HDDatabaseTransaction"8^16l
+ ___block_descriptor_32_e26_"NSError"16?0"NSError"8l
+ ___block_descriptor_32_e32_16?0"HDConcreteSyncIdentity"8l
+ ___block_descriptor_32_e37_B16?0"HDAuthorizationStatusRecord"8l
+ ___block_descriptor_32_e44_"NSUUID"16?0"HDTypedSyncStoreIdentifier"8l
+ ___block_descriptor_32_e57_v24?0"<HDSyncStore>"8?<v?"NSUUID""<HDSyncStore>">16l
+ ___block_descriptor_32_e68_"HDTypedSyncStoreIdentifier"16?0"HDDatabasePruningShowSyncStore"8l
+ ___block_descriptor_40_e8_32bs_e45_B24?0"HDSyncEntityIdentifier"8"NSNumber"16l
+ ___block_descriptor_40_e8_32r_e55_v56?0q8"NSUUID"16"NSDate"24"NSDate"32"NSDate"40q48l
+ ___block_descriptor_40_e8_32s_e26_"NSArray"16?0"NSArray"8l
+ ___block_descriptor_40_e8_32s_e55_v56?0q8"NSUUID"16"NSDate"24"NSDate"32"NSDate"40q48l
+ ___block_descriptor_40_e8_32s_e58_v32?0"HKObjectType"8"HDAuthorizationStatusRecord"16^B24l
+ ___block_descriptor_40_e8_32s_e5_B8?0l
+ ___block_descriptor_41_e45_16?0"HDSamplePruningRestrictionPredicate"8l
+ ___block_descriptor_48_e8_32r40r_e58_v32?0"HKObjectType"8"HDAuthorizationStatusRecord"16^B24l
+ ___block_descriptor_48_e8_32r_e60_"HDSamplePruningRestrictionPredicate"16?0"<HDSyncStore>"8lu40l8
+ ___block_descriptor_48_e8_32s40r_e51_"<HDSyncStore>"16?0"HDTypedSyncStoreIdentifier"8l
+ ___block_descriptor_48_e8_32s40s_e18_B16?0"HKSample"8l
+ ___block_descriptor_48_e8_32s40s_e20_v24?0q8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e25_v32?0"HKObject"8Q16^B24l
+ ___block_descriptor_48_e8_32s40s_e27_B16?0"HDSyncStoreEntity"8l
+ ___block_descriptor_48_e8_32s40s_e31_v28?0"NSUUID"8B16"NSError"20l
+ ___block_descriptor_56_e8_32s40s48s_e58_v32?0"HKObjectType"8"HDAuthorizationStatusRecord"16^B24l
+ ___block_descriptor_64_e8_32bs_e35_B24?0"HDDatabaseTransaction"8^16l
+ ___block_descriptor_64_e8_32s40s48s56s_e18_B16?0"HKObject"8l
+ ___block_descriptor_72_e8_32s40r48r56r64r_e35_B24?0"HDDatabaseTransaction"8^16l
+ ___block_descriptor_72_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e14_v16?0?<v?>8l
+ ___block_descriptor_73_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48bs56r_e9_B16?0^8l
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e69_v32?0"<HDAuthorizationSchemaProvider>"8"NSMutableOrderedSet"16^B24l
+ ___block_descriptor_88_e8_32s40s48s56s64bs72r_e72_"HDDatabasePruningShowSyncStore"16?0"HDDatabasePruningShowSyncStore"8l
+ ___block_descriptor_96_e8_32s40s48s56r64r72r_e9_B16?0^8lu88l8
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r112r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r112r
+ ___swift_memcpy0_1
+ __block_literal_global.395
+ __block_literal_global.423
+ __block_literal_global.424
+ __block_literal_global.452
+ __block_literal_global.530
+ __block_literal_global.552
+ __block_literal_global.622
+ __block_literal_global.633
+ __deleteRowsFromDataEntitySubclassTables
+ _associated conformance 9HealthKit10HKDatabaseO7PruningO19DeletedSampleDetailV0A6DaemonE0efG5ErrorOSHAHSQ
+ _objc_msgSend$_instantiateStores:profile:error:
+ _objc_msgSend$_isSupportedShardTypeForRestrictionPredicates
+ _objc_msgSend$_maximumPruningAnchorWithRestrictionPredicates:
+ _objc_msgSend$_minimumFrozenAnchorMapForPruningDate:error:
+ _objc_msgSend$_persistentIDForSyncIdentity:profile:error:
+ _objc_msgSend$_pruningPredicateWithRestrictionPredicates:
+ _objc_msgSend$_setDoseUnit:
+ _objc_msgSend$_startWatchAppWithWorkoutPlanData:client:completion:
+ _objc_msgSend$_syncStoresInProfile:error:
+ _objc_msgSend$_untypedEntityClasses
+ _objc_msgSend$activeStoresForMaxAnchorPruningInProfile:referenceDate:error:
+ _objc_msgSend$activeStoresForRestrictionPredictePruningInProfile:referenceDate:error:
+ _objc_msgSend$authorizationStatusForRecordForObjectType:authorizationStatusRecord:clientEntitlements:
+ _objc_msgSend$authorizationStatusRecordForType:error:
+ _objc_msgSend$authorizationStatusRecordsForTypes:error:
+ _objc_msgSend$cacheExcludedSyncIdentities:storeIdentifier:database:error:
+ _objc_msgSend$cacheExcludedSyncIdentities:storeIdentifier:profile:error:
+ _objc_msgSend$cacheIdentifier
+ _objc_msgSend$cachedExcludedSyncIdentitiesForStoreIdentifier:database:error:
+ _objc_msgSend$canPerformRecentRecordRoll
+ _objc_msgSend$classifiedDeletedSampleInfoWithProfile:referenceDate:anchor:limit:error:
+ _objc_msgSend$compoundPredicateWithPredicate:otherPredicate:otherPredicate:
+ _objc_msgSend$createOrUpdateShardStoresForProfile:throughDate:ownerIdentifier:containerIdentifier:syncIdentity:error:
+ _objc_msgSend$databasePruningTaskShouldUseRestrictionPredicates
+ _objc_msgSend$deletedSampleDetailWithProfile:matchingPredicatesOnly:referenceDate:sampleUUID:error:
+ _objc_msgSend$deletedSampleInProfile:sampleUUID:error:handler:
+ _objc_msgSend$deletedSampleInfoWithProfile:referenceDate:error:
+ _objc_msgSend$deletedSamplesDetailWithProfile:matchingPredicatesOnly:referenceDate:anchor:limit:error:
+ _objc_msgSend$didTimeOut
+ _objc_msgSend$enqueueMaintenanceOperationOnCoordinator:takeAccessibilityAssertion:nowDate:shouldDefer:completion:
+ _objc_msgSend$enqueuedTime
+ _objc_msgSend$enumerateDeletedSamplesInProfile:anchor:limit:error:handler:
+ _objc_msgSend$existingSyncStoreEntityWithUUID:ofType:database:error:
+ _objc_msgSend$filteredAuthorizedObjectsForClient:anchor:bundleIdentifier:clientEntitlements:error:
+ _objc_msgSend$filteredAuthorizedObjectsForClient:anchor:bundleIdentifier:clientEntitlements:profile:error:
+ _objc_msgSend$frozenAnchorMapPerStoreInProfile:error:
+ _objc_msgSend$handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:
+ _objc_msgSend$handleObjectAuthorizationRequestsWithPromptHandler:objectType:completion:
+ _objc_msgSend$hasAuthorizationBypassToReadType:
+ _objc_msgSend$hk_objectType
+ _objc_msgSend$initForBundleIdentifier:sessionIdentifier:objectType:
+ _objc_msgSend$initWithAnalyticsCoordinator:
+ _objc_msgSend$initWithClassName:identifier:supportsPruning:supportsPruningRestrictionPredicates:maximumPruningAnchor:pruningRestrictionPredicates:
+ _objc_msgSend$initWithIdentifier:type:
+ _objc_msgSend$initWithMaximumAnchor:startDate:endDate:excludedSyncIdentities:
+ _objc_msgSend$initWithPersistentID:hardwareIdentifier:databaseIdentifier:instanceDiscriminator:
+ _objc_msgSend$initWithPersistentID:identifier:type:creationDate:
+ _objc_msgSend$initWithPersistentID:identifier:type:creationDate:latestFrozenAnchorDate:frozenAnchorMap:syncIdentity:isSupportedShardType:
+ _objc_msgSend$initWithRowID:identifier:creationDate:startDate:endDate:syncIdentity:
+ _objc_msgSend$isImmediateRequest
+ _objc_msgSend$latestFrozenAnchorUpdatePerStoreInProfile:error:
+ _objc_msgSend$maintenanceCoordinator_reportCoreAnalyticsWithOperationName:database:pendingOperationsCount:activeOperationsCount:timeUntilStart:canceled:timedOut:elapsedTime:isImmediateRequest:async:
+ _objc_msgSend$maximumAnchor
+ _objc_msgSend$operationsOfType:
+ _objc_msgSend$persitentID
+ _objc_msgSend$providesSamplePruningRestrictionPredicate
+ _objc_msgSend$pruneDatabaseWithAccessibilityAssertion:nowDate:prunedObjectLimit:prunedObjectTransactionLimit:shouldDefer:error:
+ _objc_msgSend$pruneSyncedObjectsWithRestrictionPredicates:limit:nowDate:profile:error:
+ _objc_msgSend$samplePruningRestrictionPredicateForSyncEntity:error:
+ _objc_msgSend$setDidTimeOut:
+ _objc_msgSend$shardIntervalWithStartDate:endDate:
+ _objc_msgSend$shardPredicatesForProfile:currentDate:error:
+ _objc_msgSend$showAndDeletedSampleInfoWithProfile:referenceDate:error:
+ _objc_msgSend$showWithProfile:deletedSamplesOnly:referenceDate:error:
+ _objc_msgSend$startWatchAppWithWorkoutPlanData:client:completion:
+ _objc_msgSend$startedTime
+ _objc_msgSend$syncStoreEntityWithUUID:type:creationDate:healthDatabase:error:
+ _objc_msgSend$syncStoreForProfile:storeIdentifier:error:
+ _objc_msgSend$syncStoreForProfile:storeIdentifier:ownerIdentifier:syncIdentity:containerIdentifier:error:
+ _objc_msgSend$target
+ _objc_msgSend$timeIntervalSince1970
+ _objc_msgSend$transactionWithName:
+ _objc_msgSend$wasCanceled
+ _objectdestroyTm
+ _strstr
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getKeyPath
+ _swift_getSingletonMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_initStackObject
+ _swift_initStructMetadata
+ _swift_modifyAtWritableKeyPath
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unexpectedError
+ _symbolic Sb
+ _symbolic So22HDSyncEntityIdentifierC
+ _symbolic _____ 10Foundation4DateV
+ _symbolic _____ 9HealthKit10HKDatabaseO7PruningO
+ _symbolic _____ 9HealthKit10HKDatabaseO7PruningO0A6DaemonE28DateClassificationBoundariesV
+ _symbolic _____ 9HealthKit10HKDatabaseO7PruningO17DeletedSampleInfoV
+ _symbolic _____ 9HealthKit10HKDatabaseO7PruningO19DeletedSampleDetailV
+ _symbolic _____ 9HealthKit10HKDatabaseO7PruningO19DeletedSampleDetailV0A6DaemonE0efG5ErrorO
+ block_copy_helper.4
+ block_copy_helper.9
+ block_descriptor.11
+ block_descriptor.6
+ block_destroy_helper.10
+ block_destroy_helper.5
- +[HDBinarySampleSyncEntity _predicateForSyncSession:]
- +[HDCloudSyncStore createOrUpdateShardStoresForProfile:throughDate:syncCircleName:ownerIdentifier:containerIdentifier:syncIdentity:error:]
- +[HDCloudSyncStore shardPredicatesForProfile:syncCircleName:currentDate:error:]
- +[HDCloudSyncStore syncStoreForProfile:storeIdentifier:syncCircleName:ownerIdentifier:syncIdentity:containerIdentifier:error:]
- +[HDOntologyManifestUpdater _insertAndLogFailureForEntry:registry:]
- +[HDQuantitySampleSyncEntity _predicateForSyncSession:]
- +[HDReadAuthorizationStatus notDerminedReadAuthorizationStatus]
- +[HDReadAuthorizationStatus unrestrictedReadAuthorizationStatus]
- +[HDUserDomainConceptAPIObjectManager _enumerateConceptDeriveAPIObjectAndAddToResults:mutableResults:profile:transaction:error:]
- +[HDUserDomainConceptAPIObjectManager generateAPIObjectForUserDomainConcept:apiObjectOut:profile:error:]
- +[HKUnprocessedBloodOxygenDataSample(HDExtensions) hd_dataEntityClass]
- -[HDAnalyticsSubmissionCoordinator initWithDaemon:]
- -[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:promptHandler:completion:]
- -[HDClientAuthorizationOracle _isAuthorizedToReadDataTypeForObject:anchor:authorizationStatus:]
- -[HDClientAuthorizationOracle handleObjectAuthorizationRequestsWithPromptHandler:completion:]
- -[HDClientAuthorizationOracle readAuthorizationStatusForType:error:]
- -[HDClientAuthorizationOracle readAuthorizationStatusesForTypes:error:]
- -[HDCloudSyncStore _initWithProfile:storeIdentifier:syncCircleName:ownerIdentifier:syncIdentity:containerIdentifier:sharingIdentifier:sharingPredicate:shardPredicate:error:]
- -[HDCloudSyncStore canPush]
- -[HDCloudSyncStore sharingIdentifier]
- -[HDCloudSyncStore sharingPredicate]
- -[HDDemoDataFoodDatabase randomFoodObjectFromArray:]
- -[HDDemoDataGenerator _phoneProveance]
- -[HDHealthStoreServer remote_startWatchAppWithWorkoutPlanData:processIdentifier:completion:]
- -[HDMaintenanceWorkCoordinator init]
- -[HDNanoSyncStore remoteDeviceSupportsUSLegallyCompliantOxygenSaturation]
- -[HDQueryServer readAuthorizationStatusForType:error:]
- -[HDReadAuthorizationStatus .cxx_destruct]
- -[HDReadAuthorizationStatus authorizationMode]
- -[HDReadAuthorizationStatus authorizationPredicate]
- -[HDReadAuthorizationStatus authorizationRecord]
- -[HDReadAuthorizationStatus authorizationRequest]
- -[HDReadAuthorizationStatus authorizationStatus]
- -[HDReadAuthorizationStatus canRead]
- -[HDReadAuthorizationStatus canWrite]
- -[HDReadAuthorizationStatus deletedObjectBaselineAnchor]
- -[HDReadAuthorizationStatus description]
- -[HDReadAuthorizationStatus disableReading]
- -[HDReadAuthorizationStatus disableSharing]
- -[HDReadAuthorizationStatus hash]
- -[HDReadAuthorizationStatus initWithReadAuthorizationStatus:authorizationRequest:authorizationMode:restrictedBundleIdentifier:restrictedSourceEntities:deletedObjectBaselineAnchor:objectLimitAnchor:objectLimitModifiedDate:]
- -[HDReadAuthorizationStatus isAuthorizationDetermined]
- -[HDReadAuthorizationStatus isEqual:]
- -[HDReadAuthorizationStatus objectLimitAnchor]
- -[HDReadAuthorizationStatus objectLimitModifiedDate]
- -[HDReadAuthorizationStatus restrictedBundleIdentifier]
- -[HDReadAuthorizationStatus restrictedSourceEntities]
- -[HDWorkoutManager startWatchAppWithWorkoutPlanData:processIdentifier:completion:]
- -[HDWorkoutManager(Platform) _startWatchAppWithWorkoutPlanData:processIdentifier:completion:]
- -[HKUnprocessedBloodOxygenDataSample(HDCodingSupport) codableRepresentationForSync]
- GCC_except_table1002
- GCC_except_table1004
- GCC_except_table1009
- GCC_except_table1010
- GCC_except_table1011
- GCC_except_table1026
- GCC_except_table1033
- GCC_except_table1043
- GCC_except_table1061
- GCC_except_table1062
- GCC_except_table1064
- GCC_except_table1067
- GCC_except_table1070
- GCC_except_table1072
- GCC_except_table1081
- GCC_except_table1082
- GCC_except_table1090
- GCC_except_table1091
- GCC_except_table1097
- GCC_except_table1099
- GCC_except_table1104
- GCC_except_table1111
- GCC_except_table1113
- GCC_except_table1118
- GCC_except_table1119
- GCC_except_table1120
- GCC_except_table1147
- GCC_except_table1148
- GCC_except_table1150
- GCC_except_table1151
- GCC_except_table1157
- GCC_except_table1167
- GCC_except_table1168
- GCC_except_table1170
- GCC_except_table1178
- GCC_except_table1179
- GCC_except_table1182
- GCC_except_table1185
- GCC_except_table1186
- GCC_except_table1189
- GCC_except_table1193
- GCC_except_table1199
- GCC_except_table1201
- GCC_except_table1207
- GCC_except_table1208
- GCC_except_table1210
- GCC_except_table1234
- GCC_except_table1235
- GCC_except_table1237
- GCC_except_table1238
- GCC_except_table1242
- GCC_except_table1245
- GCC_except_table1254
- GCC_except_table1255
- GCC_except_table1263
- GCC_except_table1264
- GCC_except_table1267
- GCC_except_table1271
- GCC_except_table1272
- GCC_except_table1274
- GCC_except_table1275
- GCC_except_table1286
- GCC_except_table1291
- GCC_except_table1293
- GCC_except_table1296
- GCC_except_table1311
- GCC_except_table1318
- GCC_except_table1328
- GCC_except_table1346
- GCC_except_table1347
- GCC_except_table1349
- GCC_except_table1350
- GCC_except_table1351
- GCC_except_table1354
- GCC_except_table1366
- GCC_except_table1367
- GCC_except_table1369
- GCC_except_table1370
- GCC_except_table1371
- GCC_except_table1381
- GCC_except_table1382
- GCC_except_table1385
- GCC_except_table1389
- GCC_except_table1390
- GCC_except_table1392
- GCC_except_table1393
- GCC_except_table1404
- GCC_except_table1409
- GCC_except_table1411
- GCC_except_table1413
- GCC_except_table1414
- GCC_except_table1426
- GCC_except_table1433
- GCC_except_table1443
- GCC_except_table1461
- GCC_except_table1462
- GCC_except_table1464
- GCC_except_table1465
- GCC_except_table1469
- GCC_except_table1472
- GCC_except_table1481
- GCC_except_table1482
- GCC_except_table1490
- GCC_except_table1491
- GCC_except_table1494
- GCC_except_table1498
- GCC_except_table1499
- GCC_except_table1501
- GCC_except_table1502
- GCC_except_table1513
- GCC_except_table1518
- GCC_except_table1520
- GCC_except_table1523
- GCC_except_table1547
- GCC_except_table1548
- GCC_except_table1550
- GCC_except_table1551
- GCC_except_table1552
- GCC_except_table1553
- GCC_except_table1556
- GCC_except_table1567
- GCC_except_table1568
- GCC_except_table1570
- GCC_except_table1578
- GCC_except_table1579
- GCC_except_table1582
- GCC_except_table1587
- GCC_except_table159
- GCC_except_table1590
- GCC_except_table1601
- GCC_except_table1607
- GCC_except_table1610
- GCC_except_table1611
- GCC_except_table163
- GCC_except_table1634
- GCC_except_table1635
- GCC_except_table1637
- GCC_except_table1638
- GCC_except_table1640
- GCC_except_table1644
- GCC_except_table1654
- GCC_except_table1655
- GCC_except_table1664
- GCC_except_table1667
- GCC_except_table1670
- GCC_except_table1674
- GCC_except_table1677
- GCC_except_table1687
- GCC_except_table1689
- GCC_except_table1696
- GCC_except_table1700
- GCC_except_table1701
- GCC_except_table1726
- GCC_except_table1743
- GCC_except_table1745
- GCC_except_table1747
- GCC_except_table1748
- GCC_except_table1750
- GCC_except_table1752
- GCC_except_table1754
- GCC_except_table1764
- GCC_except_table1765
- GCC_except_table1767
- GCC_except_table1768
- GCC_except_table1769
- GCC_except_table1770
- GCC_except_table1781
- GCC_except_table1784
- GCC_except_table1788
- GCC_except_table1791
- GCC_except_table1801
- GCC_except_table1808
- GCC_except_table1811
- GCC_except_table1812
- GCC_except_table1837
- GCC_except_table1854
- GCC_except_table1856
- GCC_except_table1858
- GCC_except_table1859
- GCC_except_table1861
- GCC_except_table1863
- GCC_except_table1865
- GCC_except_table1875
- GCC_except_table1876
- GCC_except_table1885
- GCC_except_table1888
- GCC_except_table1891
- GCC_except_table1895
- GCC_except_table1898
- GCC_except_table1905
- GCC_except_table191
- GCC_except_table1912
- GCC_except_table1914
- GCC_except_table1917
- GCC_except_table1918
- GCC_except_table1938
- GCC_except_table194
- GCC_except_table1940
- GCC_except_table1942
- GCC_except_table1943
- GCC_except_table1945
- GCC_except_table1947
- GCC_except_table1949
- GCC_except_table1959
- GCC_except_table1960
- GCC_except_table1962
- GCC_except_table1971
- GCC_except_table1974
- GCC_except_table1977
- GCC_except_table1981
- GCC_except_table1984
- GCC_except_table1991
- GCC_except_table1998
- GCC_except_table2000
- GCC_except_table2002
- GCC_except_table2003
- GCC_except_table2023
- GCC_except_table2025
- GCC_except_table2027
- GCC_except_table2028
- GCC_except_table2030
- GCC_except_table2032
- GCC_except_table2034
- GCC_except_table2044
- GCC_except_table2045
- GCC_except_table2047
- GCC_except_table2054
- GCC_except_table2057
- GCC_except_table2060
- GCC_except_table2064
- GCC_except_table2067
- GCC_except_table2079
- GCC_except_table208
- GCC_except_table2082
- GCC_except_table2086
- GCC_except_table2088
- GCC_except_table2091
- GCC_except_table2092
- GCC_except_table2093
- GCC_except_table2104
- GCC_except_table2105
- GCC_except_table2122
- GCC_except_table2140
- GCC_except_table2141
- GCC_except_table2143
- GCC_except_table2144
- GCC_except_table2146
- GCC_except_table2150
- GCC_except_table2160
- GCC_except_table2161
- GCC_except_table2163
- GCC_except_table2164
- GCC_except_table2165
- GCC_except_table2166
- GCC_except_table2167
- GCC_except_table2177
- GCC_except_table218
- GCC_except_table2180
- GCC_except_table2184
- GCC_except_table2187
- GCC_except_table2198
- GCC_except_table2205
- GCC_except_table2208
- GCC_except_table2209
- GCC_except_table2210
- GCC_except_table2221
- GCC_except_table2222
- GCC_except_table2239
- GCC_except_table2257
- GCC_except_table2258
- GCC_except_table2260
- GCC_except_table2261
- GCC_except_table2263
- GCC_except_table2267
- GCC_except_table2277
- GCC_except_table2278
- GCC_except_table2280
- GCC_except_table2287
- GCC_except_table2290
- GCC_except_table2293
- GCC_except_table2297
- GCC_except_table2300
- GCC_except_table2307
- GCC_except_table2314
- GCC_except_table2316
- GCC_except_table2319
- GCC_except_table2320
- GCC_except_table2321
- GCC_except_table2344
- GCC_except_table2345
- GCC_except_table2347
- GCC_except_table2348
- GCC_except_table2350
- GCC_except_table2352
- GCC_except_table2355
- GCC_except_table2365
- GCC_except_table2367
- GCC_except_table2368
- GCC_except_table2369
- GCC_except_table2375
- GCC_except_table2379
- GCC_except_table2382
- GCC_except_table2383
- GCC_except_table2387
- GCC_except_table2389
- GCC_except_table2390
- GCC_except_table2397
- GCC_except_table2404
- GCC_except_table2409
- GCC_except_table2410
- GCC_except_table2433
- GCC_except_table2434
- GCC_except_table2436
- GCC_except_table2437
- GCC_except_table2439
- GCC_except_table2441
- GCC_except_table2442
- GCC_except_table2462
- GCC_except_table2466
- GCC_except_table2469
- GCC_except_table2470
- GCC_except_table2471
- GCC_except_table2474
- GCC_except_table2477
- GCC_except_table2485
- GCC_except_table2490
- GCC_except_table2491
- GCC_except_table2492
- GCC_except_table2496
- GCC_except_table2504
- GCC_except_table2511
- GCC_except_table2539
- GCC_except_table2541
- GCC_except_table2543
- GCC_except_table2544
- GCC_except_table2545
- GCC_except_table2546
- GCC_except_table2548
- GCC_except_table2550
- GCC_except_table2563
- GCC_except_table2564
- GCC_except_table2577
- GCC_except_table258
- GCC_except_table2580
- GCC_except_table2581
- GCC_except_table2582
- GCC_except_table2585
- GCC_except_table2588
- GCC_except_table259
- GCC_except_table2596
- GCC_except_table2601
- GCC_except_table2602
- GCC_except_table2603
- GCC_except_table2605
- GCC_except_table2620
- GCC_except_table2648
- GCC_except_table2650
- GCC_except_table2652
- GCC_except_table2653
- GCC_except_table2655
- GCC_except_table2657
- GCC_except_table2659
- GCC_except_table267
- GCC_except_table2678
- GCC_except_table2682
- GCC_except_table2685
- GCC_except_table2686
- GCC_except_table2687
- GCC_except_table2690
- GCC_except_table2693
- GCC_except_table2701
- GCC_except_table2706
- GCC_except_table2707
- GCC_except_table2708
- GCC_except_table2712
- GCC_except_table2730
- GCC_except_table2732
- GCC_except_table2734
- GCC_except_table2735
- GCC_except_table2737
- GCC_except_table2739
- GCC_except_table2740
- GCC_except_table2742
- GCC_except_table2754
- GCC_except_table2766
- GCC_except_table2769
- GCC_except_table2770
- GCC_except_table2771
- GCC_except_table2776
- GCC_except_table278
- GCC_except_table2783
- GCC_except_table279
- GCC_except_table2790
- GCC_except_table2791
- GCC_except_table2792
- GCC_except_table2795
- GCC_except_table2813
- GCC_except_table2815
- GCC_except_table2817
- GCC_except_table2818
- GCC_except_table2820
- GCC_except_table2822
- GCC_except_table2823
- GCC_except_table2824
- GCC_except_table2843
- GCC_except_table2844
- GCC_except_table2850
- GCC_except_table2851
- GCC_except_table2852
- GCC_except_table2854
- GCC_except_table2857
- GCC_except_table2858
- GCC_except_table2872
- GCC_except_table2878
- GCC_except_table2880
- GCC_except_table2883
- GCC_except_table2900
- GCC_except_table2910
- GCC_except_table2928
- GCC_except_table2930
- GCC_except_table2932
- GCC_except_table2933
- GCC_except_table2935
- GCC_except_table2937
- GCC_except_table2938
- GCC_except_table2939
- GCC_except_table294
- GCC_except_table2953
- GCC_except_table2954
- GCC_except_table2955
- GCC_except_table2963
- GCC_except_table2969
- GCC_except_table2970
- GCC_except_table2971
- GCC_except_table2973
- GCC_except_table2977
- GCC_except_table2984
- GCC_except_table2987
- GCC_except_table2993
- GCC_except_table2994
- GCC_except_table2995
- GCC_except_table2998
- GCC_except_table3013
- GCC_except_table3023
- GCC_except_table3041
- GCC_except_table3043
- GCC_except_table3045
- GCC_except_table3046
- GCC_except_table3048
- GCC_except_table3050
- GCC_except_table3051
- GCC_except_table3052
- GCC_except_table306
- GCC_except_table3071
- GCC_except_table3072
- GCC_except_table3078
- GCC_except_table3079
- GCC_except_table3080
- GCC_except_table3082
- GCC_except_table3085
- GCC_except_table3086
- GCC_except_table3099
- GCC_except_table3100
- GCC_except_table3101
- GCC_except_table3105
- GCC_except_table3125
- GCC_except_table3127
- GCC_except_table3129
- GCC_except_table3130
- GCC_except_table3132
- GCC_except_table3134
- GCC_except_table3135
- GCC_except_table3136
- GCC_except_table3157
- GCC_except_table3164
- GCC_except_table3165
- GCC_except_table3166
- GCC_except_table3168
- GCC_except_table3172
- GCC_except_table3179
- GCC_except_table3186
- GCC_except_table3187
- GCC_except_table3188
- GCC_except_table3211
- GCC_except_table3213
- GCC_except_table3215
- GCC_except_table3216
- GCC_except_table3218
- GCC_except_table3220
- GCC_except_table3221
- GCC_except_table3222
- GCC_except_table3241
- GCC_except_table3242
- GCC_except_table3248
- GCC_except_table3249
- GCC_except_table3250
- GCC_except_table3252
- GCC_except_table3255
- GCC_except_table3256
- GCC_except_table3269
- GCC_except_table3270
- GCC_except_table3271
- GCC_except_table3275
- GCC_except_table3290
- GCC_except_table3300
- GCC_except_table3318
- GCC_except_table3320
- GCC_except_table3322
- GCC_except_table3323
- GCC_except_table3324
- GCC_except_table3325
- GCC_except_table3327
- GCC_except_table3328
- GCC_except_table3329
- GCC_except_table3343
- GCC_except_table3353
- GCC_except_table3356
- GCC_except_table3359
- GCC_except_table3360
- GCC_except_table3361
- GCC_except_table3363
- GCC_except_table3366
- GCC_except_table3367
- GCC_except_table3380
- GCC_except_table3381
- GCC_except_table3382
- GCC_except_table3384
- GCC_except_table3399
- GCC_except_table3409
- GCC_except_table3427
- GCC_except_table3429
- GCC_except_table3431
- GCC_except_table3432
- GCC_except_table3434
- GCC_except_table3436
- GCC_except_table3437
- GCC_except_table3438
- GCC_except_table3457
- GCC_except_table3458
- GCC_except_table3464
- GCC_except_table3465
- GCC_except_table3466
- GCC_except_table3468
- GCC_except_table3471
- GCC_except_table3472
- GCC_except_table3485
- GCC_except_table3486
- GCC_except_table3487
- GCC_except_table3491
- GCC_except_table3509
- GCC_except_table3511
- GCC_except_table3513
- GCC_except_table3514
- GCC_except_table3516
- GCC_except_table3518
- GCC_except_table3519
- GCC_except_table3520
- GCC_except_table3521
- GCC_except_table3530
- GCC_except_table3541
- GCC_except_table3542
- GCC_except_table3545
- GCC_except_table3548
- GCC_except_table3549
- GCC_except_table3550
- GCC_except_table3552
- GCC_except_table3553
- GCC_except_table3556
- GCC_except_table3564
- GCC_except_table3570
- GCC_except_table3571
- GCC_except_table3573
- GCC_except_table3574
- GCC_except_table3592
- GCC_except_table3594
- GCC_except_table3596
- GCC_except_table3597
- GCC_except_table3599
- GCC_except_table3601
- GCC_except_table3602
- GCC_except_table3603
- GCC_except_table3604
- GCC_except_table3614
- GCC_except_table3622
- GCC_except_table3623
- GCC_except_table3626
- GCC_except_table3629
- GCC_except_table3630
- GCC_except_table3631
- GCC_except_table3633
- GCC_except_table3634
- GCC_except_table3652
- GCC_except_table3655
- GCC_except_table3656
- GCC_except_table3676
- GCC_except_table3686
- GCC_except_table370
- GCC_except_table3704
- GCC_except_table3705
- GCC_except_table3707
- GCC_except_table3708
- GCC_except_table3709
- GCC_except_table3710
- GCC_except_table3712
- GCC_except_table3713
- GCC_except_table3714
- GCC_except_table3715
- GCC_except_table372
- GCC_except_table3725
- GCC_except_table3737
- GCC_except_table374
- GCC_except_table3744
- GCC_except_table3745
- GCC_except_table3746
- GCC_except_table3748
- GCC_except_table3749
- GCC_except_table3767
- GCC_except_table3769
- GCC_except_table377
- GCC_except_table3770
- GCC_except_table3782
- GCC_except_table3789
- GCC_except_table379
- GCC_except_table3799
- GCC_except_table3817
- GCC_except_table3818
- GCC_except_table3820
- GCC_except_table3821
- GCC_except_table3823
- GCC_except_table3825
- GCC_except_table3826
- GCC_except_table3827
- GCC_except_table3828
- GCC_except_table3838
- GCC_except_table3846
- GCC_except_table3847
- GCC_except_table3850
- GCC_except_table3853
- GCC_except_table3854
- GCC_except_table3855
- GCC_except_table3857
- GCC_except_table3858
- GCC_except_table3876
- GCC_except_table3879
- GCC_except_table3880
- GCC_except_table3903
- GCC_except_table3904
- GCC_except_table3906
- GCC_except_table3907
- GCC_except_table3909
- GCC_except_table391
- GCC_except_table3911
- GCC_except_table3912
- GCC_except_table3913
- GCC_except_table3914
- GCC_except_table3923
- GCC_except_table3934
- GCC_except_table3935
- GCC_except_table394
- GCC_except_table3942
- GCC_except_table3943
- GCC_except_table3945
- GCC_except_table3946
- GCC_except_table3948
- GCC_except_table3955
- GCC_except_table3962
- GCC_except_table3966
- GCC_except_table3967
- GCC_except_table3990
- GCC_except_table3991
- GCC_except_table3993
- GCC_except_table3994
- GCC_except_table3996
- GCC_except_table3998
- GCC_except_table3999
- GCC_except_table4000
- GCC_except_table4001
- GCC_except_table4011
- GCC_except_table402
- GCC_except_table406
- GCC_except_table409
- GCC_except_table413
- GCC_except_table416
- GCC_except_table423
- GCC_except_table425
- GCC_except_table430
- GCC_except_table434
- GCC_except_table453
- GCC_except_table458
- GCC_except_table463
- GCC_except_table474
- GCC_except_table475
- GCC_except_table483
- GCC_except_table484
- GCC_except_table487
- GCC_except_table490
- GCC_except_table491
- GCC_except_table495
- GCC_except_table498
- GCC_except_table504
- GCC_except_table511
- GCC_except_table512
- GCC_except_table516
- GCC_except_table517
- GCC_except_table525
- GCC_except_table532
- GCC_except_table542
- GCC_except_table560
- GCC_except_table565
- GCC_except_table570
- GCC_except_table581
- GCC_except_table582
- GCC_except_table585
- GCC_except_table594
- GCC_except_table595
- GCC_except_table598
- GCC_except_table601
- GCC_except_table602
- GCC_except_table606
- GCC_except_table609
- GCC_except_table615
- GCC_except_table622
- GCC_except_table623
- GCC_except_table627
- GCC_except_table634
- GCC_except_table641
- GCC_except_table651
- GCC_except_table669
- GCC_except_table674
- GCC_except_table679
- GCC_except_table690
- GCC_except_table691
- GCC_except_table699
- GCC_except_table700
- GCC_except_table703
- GCC_except_table706
- GCC_except_table707
- GCC_except_table711
- GCC_except_table714
- GCC_except_table720
- GCC_except_table727
- GCC_except_table728
- GCC_except_table732
- GCC_except_table733
- GCC_except_table751
- GCC_except_table753
- GCC_except_table755
- GCC_except_table760
- GCC_except_table762
- GCC_except_table772
- GCC_except_table773
- GCC_except_table783
- GCC_except_table784
- GCC_except_table791
- GCC_except_table792
- GCC_except_table804
- GCC_except_table806
- GCC_except_table811
- GCC_except_table812
- GCC_except_table813
- GCC_except_table834
- GCC_except_table836
- GCC_except_table839
- GCC_except_table841
- GCC_except_table844
- GCC_except_table846
- GCC_except_table855
- GCC_except_table856
- GCC_except_table864
- GCC_except_table865
- GCC_except_table871
- GCC_except_table873
- GCC_except_table878
- GCC_except_table885
- GCC_except_table887
- GCC_except_table892
- GCC_except_table893
- GCC_except_table894
- GCC_except_table912
- GCC_except_table919
- GCC_except_table929
- GCC_except_table947
- GCC_except_table948
- GCC_except_table950
- GCC_except_table953
- GCC_except_table956
- GCC_except_table958
- GCC_except_table967
- GCC_except_table968
- GCC_except_table970
- GCC_except_table981
- GCC_except_table982
- GCC_except_table988
- GCC_except_table990
- GCC_except_table995
- HDCloudSyncStorePendingFullSync_block_invoke.lookupKey
- HDCloudSyncStorePendingFullSync_block_invoke_2.updateKey
- HDCloudSyncStorePendingFullSync_block_invoke_3.lookupKey
- HDCloudSyncStorePendingFullSync_block_invoke_4.lookupKey
- HDCloudSyncStorePendingFullSync_block_invoke_5.lookupKey
- HDCloudSyncStorePendingFullSync_block_invoke_6.lookupKey
- OBJC_IVAR_$_HDAnalyticsSubmissionCoordinator._daemon
- OBJC_IVAR_$_HDCloudSyncStore._canPush
- OBJC_IVAR_$_HDCloudSyncStore._sharingIdentifier
- OBJC_IVAR_$_HDCloudSyncStore._sharingPredicate
- OBJC_IVAR_$_HDNanoSyncStore._remoteDeviceSupportsUSLegallyCompliantOxygenSaturation
- OBJC_IVAR_$_HDReadAuthorizationStatus._authorizationRecord
- OBJC_IVAR_$_HDReadAuthorizationStatus._deletedObjectBaselineAnchor
- OBJC_IVAR_$_HDReadAuthorizationStatus._objectLimitAnchor
- OBJC_IVAR_$_HDReadAuthorizationStatus._restrictedBundleIdentifier
- OBJC_IVAR_$_HDReadAuthorizationStatus._restrictedSourceEntities
- _HKCategoryTypeIdentifierUnsuccessfulBloodOxygenSaturationAnalysisEvent
- _MergedGlobals.22
- _NSFileProtectionComplete
- _OBJC_CLASS_$_HDReadAuthorizationStatus
- _OBJC_CLASS_$_HKUnprocessedBloodOxygenDataSample
- _OBJC_METACLASS_$_HDReadAuthorizationStatus
- __100-[HDDatabasePruningCoordinator _pruneProfilesWithIdentifiers:takeAccessibilityAssertion:completion:]_block_invoke.310
- __102+[HDSampleSyncEntity _predicateForSampleAgeWithMaximumObjectAgeByType:defaultMaxAge:sessionStartDate:]_block_invoke.411
- __104-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:promptHandler:completion:]_block_invoke.452
- __104-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:promptHandler:completion:]_block_invoke.455
- __104-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:promptHandler:completion:]_block_invoke.459
- __104-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:promptHandler:completion:]_block_invoke.460
- __104-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:promptHandler:completion:]_block_invoke_2.456
- __108+[HDCloudSyncStoreEntity storeIdentifiersForOwnerIdentifier:containerIdentifier:syncIdentity:profile:error:]_block_invoke.357
- __112-[HDDatabasePruningTask enqueueMaintenanceOperationOnCoordinator:takeAccessibilityAssertion:nowDate:completion:]_block_invoke.295
- __127-[HDClientAuthorizationOracle(Privileged) _queue_beginAuthorizationRequestDelegateTransactionWithSessionIdentifier:completion:]_block_invoke.517
- __133-[HDClientAuthorizationOracle enqueueAuthorizationRequestToWriteTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke.434
- __158-[HDClientAuthorizationOracle _queue_enqueueAuthorizationRequestForBundleIdentifier:writeTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke.440
- __158-[HDClientAuthorizationOracle _queue_enqueueAuthorizationRequestForBundleIdentifier:writeTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke_2.441
- __189+[HDAuthorizationEntity _setAuthorizationStatuses:authorizationRequests:authorizationModes:sourceEntity:dateModified:syncProvenance:objectAnchor:options:profile:database:transaction:error:]_block_invoke.441
- __37-[HDCloudSyncPushStoreOperation main]_block_invoke.312
- __37-[HDDatabase _mergeSecondaryJournals]_block_invoke.569
- __52-[HDWorkoutBasicDataSource setSampleTypesToCollect:]_block_invoke.403
- __61-[HDDatabase _mergeSecondaryJournalsWithActivity:completion:]_block_invoke.570
- __75-[HDWorkoutBasicDataSource workoutSession:didChangeToState:fromState:date:]_block_invoke.445
- __77-[HDDatabase _performWhenDataProtectedByFirstUnlockIsAvailableOnQueue:block:]_block_invoke.417
- __77-[HDDatabase _performWhenDataProtectedByFirstUnlockIsAvailableOnQueue:block:]_block_invoke.421
- __77-[_HDObjectAuthorizationPromptSession endPromptTransactionWithSuccess:error:]_block_invoke.752
- __78+[HDDeletedSampleEntity insertCodableDeletedSamples:provenance:profile:error:]_block_invoke.325
- __78+[HDDeletedSampleEntity insertCodableDeletedSamples:provenance:profile:error:]_block_invoke.331
- __78-[HDCloudSyncStoreEntity updateShardStartDate:endDate:type:transaction:error:]_block_invoke.426
- __78-[HDDatabase _protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.539
- __80-[HDCloudSyncPushSequenceOperation _startingSyncAnchorMapForStagingStore:error:]_block_invoke.332
- __84+[HDCloudSyncStoreEntity persistState:storeUUID:shouldReplace:healthDatabase:error:]_block_invoke.398
- __84+[HDCloudSyncStoreEntity persistState:storeUUID:shouldReplace:healthDatabase:error:]_block_invoke.406
- __89-[HDHealthStoreServer remote_requestPerObjectReadAuthorizationForType:filter:completion:]_block_invoke.358
- __90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.367
- __90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.370
- __93+[HDMedicationDoseEventEntity _logPersistedDoseEventOnCommitDatabase:doseEvent:persistentID:]_block_invoke.371
- __94-[HDWorkoutBasicDataSource _workoutDataDestination:requestsSamplesOfType:from:to:transaction:]_block_invoke.429
- __96-[HDClientAuthorizationOracle performIfAuthorizedToReadObjects:onQueue:usingBlock:errorHandler:]_block_invoke.355
- __96-[HDClientAuthorizationOracle performIfAuthorizedToSaveObjects:onQueue:usingBlock:errorHandler:]_block_invoke.366
- __98-[HDClientAuthorizationOracle performIfAuthorizedToDeleteObjects:onQueue:usingBlock:errorHandler:]_block_invoke.369
- __98-[HDClientAuthorizationOracle(Privileged) updateDefaultAuthorizationStatusesForSource:completion:]_block_invoke.528
- __98-[HDClientAuthorizationOracle(Privileged) updateDefaultAuthorizationStatusesForSource:completion:]_block_invoke.532
- __99-[HDDatabase takeAccessibilityAssertionWithOwnerIdentifier:shouldPerformTransaction:timeout:error:]_block_invoke.547
- __OBJC_$_CATEGORY_HKUnprocessedBloodOxygenDataSample_$_HDCodingSupport
- __OBJC_$_CATEGORY_INSTANCE_METHODS_HKUnprocessedBloodOxygenDataSample_$_HDCodingSupport
- __OBJC_$_CLASS_METHODS_HDReadAuthorizationStatus
- __OBJC_$_CLASS_METHODS_HKUnprocessedBloodOxygenDataSample(HDCodingSupport|HDExtensions)
- __OBJC_$_INSTANCE_METHODS_HDAnalyticsSubmissionCoordinator(Tinker|MedicalID|HeartDaily|HealthService|Authorization|Attachments|HeartRate|NanoSync|SummarySharing|CloudKitCache|CloudSync|Workout|Database)
- __OBJC_$_INSTANCE_METHODS_HDReadAuthorizationStatus
- __OBJC_$_INSTANCE_VARIABLES_HDReadAuthorizationStatus
- __OBJC_$_PROP_LIST_HDReadAuthorizationStatus
- __OBJC_CLASS_RO_$_HDReadAuthorizationStatus
- __OBJC_METACLASS_RO_$_HDReadAuthorizationStatus
- __ZN6health18TransactionalCacheIyNS_8FilePageEE20_removeEntryFromListEPNS2_10CacheEntryE
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100IP16_HDWrappedSourceS5_S5_EENS_4pairIT_T1_EES7_T0_S8_
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPK39HDQuantitySampleAttenuationEngineSampleNS_16__deque_iteratorIS4_PS4_RS4_PS8_lLl102EEELi0EEENS_4pairIT_T0_EESD_SD_SE_
- __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPNS_10shared_ptrIN6health13WriteAheadLog11TransactionEEES9_S9_EENS_4pairIT_T1_EESB_T0_SC_
- __ZNKSt3__111__move_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPNS_10unique_ptrIN6health18TransactionalCacheIyNS5_8FilePageEE10CacheEntryENS_14default_deleteIS9_EEEESD_SD_EENS_4pairIT_T1_EESF_T0_SG_
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__114default_deleteIN6health18TransactionalCacheIyNS1_8FilePageEE10CacheEntryEEclB8ne180100EPS5_
- __ZNKSt3__114default_deleteINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8ne180100EPS6_
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8ne180100IS4_EENS_12basic_stringIcS2_T_EERKS8_
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB8ne180100Ev
- __ZNKSt3__121__unordered_map_equalIU8__strongP8NSStringNS_17__hash_value_typeIS3_NS_5dequeI19HDRawQuantitySampleNS_9allocatorIS6_EEEEEE13HDStringEqual12HDStringHashLb1EEclB8ne180100ERKSA_RU8__strongKS2_
- __ZNKSt3__121__unordered_map_equalIU8__strongP8NSStringNS_17__hash_value_typeIS3_xEE13HDStringEqual12HDStringHashLb1EEclB8ne180100ERKS5_RU8__strongKS2_
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS4_EEEEEENS_16reverse_iteratorIPS7_EEEclB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS4_EEEEEENS_16reverse_iteratorIPS7_EEEclB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS4_EEEEEENS_16reverse_iteratorIPS7_EEEclB8ne180100Ev
- __ZNKSt3__129_AllocatorDestroyRangeReverseINS_9allocatorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS4_EEEEEENS_16reverse_iteratorIPS7_EEEclB8ne180100Ev
- __ZNKSt3__16__loopIcE13__init_repeatB8ne180100ERNS_7__stateIcEE
- __ZNKSt3__16vectorI13HKRawIntervalIdENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI15HistogramBucketNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI16_HDWrappedSourceNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI19HDRawDistanceSampleNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorI19HDRawQuantitySampleNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS3_EE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS7_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsDiscreteE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsPresenceE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EEE16_SampleRemainderENS_9allocatorIS8_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorISB_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_SampleRemainderENS_9allocatorISB_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_SampleRemainderENS_9allocatorIS8_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_SampleRemainderENS_9allocatorIS8_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI22HDStatisticsCumulativeE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI23HDStatisticsPercentilesE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_SampleRemainderENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_SampleRemainderENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN6health10FileExtentENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN6health13WriteAheadLog9PageEntryENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN6health18DataStoreInspector15DataSeriesEntryENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10shared_ptrIN6health13WriteAheadLog11TransactionEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_10unique_ptrIN6health18TransactionalCacheIyNS2_8FilePageEE10CacheEntryENS_14default_deleteIS6_EEEENS_9allocatorIS9_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairIccEENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairImPKcEENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_5tupleIJxU8__strongP15HKDeletedObjectEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_5tupleIJxU8__strongP8HKSampleEEENS_9allocatorIS5_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_7__stateIcEENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_9sub_matchINS_11__wrap_iterIPKcEEEENS_9allocatorIS6_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_9sub_matchIPKcEENS_9allocatorIS4_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIU8__strongP8HKSourceNS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIcNS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIlNS_9allocatorIlEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIxNS_9allocatorIxEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt9exception4whatEv
- __ZNKSt9type_infoeqB8ne180100ERKS_
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt12out_of_rangeC1B8ne180100EPKc
- __ZNSt16invalid_argumentC1B8ne180100EPKc
- __ZNSt3__110__function12__value_funcIF21_HDRawLocationDatumV1dS2_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIF21_HDRawLocationDatumV2dS2_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIF27_HDRawQuantitySampleValueV1dS2_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_13match_resultsINS_11__wrap_iterIPKcEENS5_INS_9sub_matchISC_EEEEEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne180100ERKSD_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalES7_EEC2B8ne180100ERKS9_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalES7_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne180100ERKSD_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalES7_EEC2B8ne180100ERKS9_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalES7_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne180100ERKSD_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalES7_EEC2B8ne180100ERKS9_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalES7_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne180100ERKSD_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalES7_EEC2B8ne180100ERKS9_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalES7_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne180100ERKSD_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalES7_EEC2B8ne180100ERKS9_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalES7_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne180100ERKSD_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalES7_EEC2B8ne180100ERKS9_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalES7_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI24HDStatisticsTimeIntervalS3_ERK20HDStatisticsRelativeIS4_EEEC2B8ne180100ERKSC_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI24HDStatisticsTimeIntervalS3_ERK20HDStatisticsRelativeIS4_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI24HDStatisticsTimeIntervalS3_ES6_EEC2B8ne180100ERKS8_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI24HDStatisticsTimeIntervalS3_ES6_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEEC2B8ne180100ERKSD_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS5_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalES7_EEC2B8ne180100ERKS9_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalES7_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS7_EEEC2B8ne180100ERKSF_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS7_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalES9_EEC2B8ne180100ERKSB_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalES9_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS7_EEEC2B8ne180100ERKSF_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalERK20HDStatisticsRelativeIS7_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalES9_EEC2B8ne180100ERKSB_
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalES9_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsDiscreteRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsDiscreteRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsDiscreteRK20HDStatisticsRelativeIS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsDiscreteS4_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsPresenceRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsPresenceRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsPresenceRK20HDStatisticsRelativeIS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK20HDStatisticsPresenceS4_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK22HDStatisticsCumulativeRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK22HDStatisticsCumulativeRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK22HDStatisticsCumulativeRK20HDStatisticsRelativeIS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK22HDStatisticsCumulativeS4_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK22HDStatisticsNoiseLevelRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK22HDStatisticsNoiseLevelRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK22HDStatisticsNoiseLevelRK20HDStatisticsRelativeIS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK22HDStatisticsNoiseLevelS4_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK23HDStatisticsPercentilesRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK23HDStatisticsPercentilesRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK23HDStatisticsPercentilesRK20HDStatisticsRelativeIS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK23HDStatisticsPercentilesS4_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK23HDStatisticsSleepStagesRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK23HDStatisticsSleepStagesRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK23HDStatisticsSleepStagesRK20HDStatisticsRelativeIS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK23HDStatisticsSleepStagesS4_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI20HDStatisticsDiscreteS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI20HDStatisticsPresenceS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI22HDStatisticsCumulativeS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI22HDStatisticsNoiseLevelS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI23HDStatisticsPercentilesS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI23HDStatisticsSleepStagesS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI33HDStatisticsAverageSampleDurationS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersES2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersES2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsCombinedIS2_S2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscreteS2_EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresenceS2_EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulativeS2_EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevelS2_EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentilesS2_EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStagesS2_EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDurationS2_EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersES2_EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersES2_EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_S2_EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalRK20HDStatisticsRelativeIS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK24HDStatisticsTimeIntervalS4_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK33HDStatisticsAverageSampleDurationRK20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK33HDStatisticsAverageSampleDurationRK20HDStatisticsRelativeI20HDStatisticsCombinedIS2_24HDStatisticsTimeIntervalEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK33HDStatisticsAverageSampleDurationRK20HDStatisticsRelativeIS2_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK33HDStatisticsAverageSampleDurationS4_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersERK20HDStatisticsCombinedIS4_24HDStatisticsTimeIntervalEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersERK20HDStatisticsRelativeI20HDStatisticsCombinedIS4_24HDStatisticsTimeIntervalEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersERK20HDStatisticsRelativeIS4_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersES6_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersERK20HDStatisticsCombinedIS4_24HDStatisticsTimeIntervalEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersERK20HDStatisticsRelativeI20HDStatisticsCombinedIS4_24HDStatisticsTimeIntervalEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersERK20HDStatisticsRelativeIS4_EEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFRK42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersES6_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbN6health15BlockAccessFile14IntegrityErrorExxRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbN6health9DataStore14IntegrityErrorENS2_12BlockPointerERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEC2B8ne180100ERKSF_
- __ZNSt3__110__function12__value_funcIFbN6health9DataStore14IntegrityErrorENS2_12BlockPointerERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRKdRK21_HDRawLocationDatumV0EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRKdRK21_HDRawLocationDatumV1EEC2B8ne180100ERKS8_
- __ZNSt3__110__function12__value_funcIFbRKdRK21_HDRawLocationDatumV1EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRKdRK21_HDRawLocationDatumV2EEC2B8ne180100ERKS8_
- __ZNSt3__110__function12__value_funcIFbRKdRK21_HDRawLocationDatumV2EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRKdRK27_HDRawQuantitySampleValueV1EEC2B8ne180100ERKS8_
- __ZNSt3__110__function12__value_funcIFbRKdRK27_HDRawQuantitySampleValueV1EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRKdS3_EEC2B8ne180100ERKS5_
- __ZNSt3__110__function12__value_funcIFbRKdS3_EED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRN6health15BlockAccessFile16WriteTransactionEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRN6health17TransactionalFile16WriteTransactionEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRN6health9DataStore16WriteTransactionEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRN6health9DataStore20MutableSampleHistoryI25LocationHistoryBehaviorV1EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRN6health9DataStore20MutableSampleHistoryI25LocationHistoryBehaviorV2EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRN6health9DataStore20MutableSampleHistoryI29QuantitySampleValueBehaviorV0EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbRN6health9DataStore20MutableSampleHistoryI29QuantitySampleValueBehaviorV1EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbvEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbyEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFbyRKyRKN6health8FilePageEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFdddEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKN6health10FileExtentEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKN6health15BlockAccessFile15ReadTransactionEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKN6health17TransactionalFile15ReadTransactionEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore13SampleHistoryI25LocationHistoryBehaviorV0EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore13SampleHistoryI25LocationHistoryBehaviorV1EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore13SampleHistoryI25LocationHistoryBehaviorV2EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore13SampleHistoryI29QuantitySampleValueBehaviorV0EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore13SampleHistoryI29QuantitySampleValueBehaviorV1EEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore15ReadTransactionEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKN6health9DataStore16ObjectIdentifierENS2_12BlockPointerEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEEC2B8ne180100ERKSB_
- __ZNSt3__110__function12__value_funcIFvRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvxN6health13WriteAheadLog9PageEntryEEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvyEEC2B8ne180100ERKS3_
- __ZNSt3__110__function12__value_funcIFvyEED2B8ne180100Ev
- __ZNSt3__110__function12__value_funcIFvyRKN6health8FilePageEEEC2B8ne180100ERKS7_
- __ZNSt3__110__function12__value_funcIFvyRKN6health8FilePageEEED2B8ne180100Ev
- __ZNSt3__110shared_ptrINS_13__empty_stateIcEEE5resetB8ne180100IS2_vEEvPT_
- __ZNSt3__110shared_ptrINS_13__empty_stateIcEEEC2B8ne180100IS2_vEEPT_
- __ZNSt3__110shared_ptrIhEC2B8ne180100IhNS_14default_deleteIA_hEEvEEPT_T0_
- __ZNSt3__110unique_ptrIN6health9DataStoreENS_14default_deleteIS2_EEE5resetB8ne180100EPS2_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne180100EPSC_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne180100EPSC_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne180100EPSC_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne180100EPSC_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne180100EPSC_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne180100EPSC_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI24HDStatisticsTimeIntervalS7_EEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne180100EPSB_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISC_EEEEE5resetB8ne180100EPSC_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS8_EEEEPvEENS_22__hash_node_destructorINS_9allocatorISD_EEEEE5resetB8ne180100EPSD_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISE_EEEEE5resetB8ne180100EPSE_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISG_EEEEE5resetB8ne180100EPSG_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEEPvEENS_22__hash_node_destructorINS_9allocatorISG_EEEEE5resetB8ne180100EPSG_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI23HDStatisticsPercentilesEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne180100EPSB_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI24HDStatisticsTimeIntervalEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8ne180100EPSB_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString23HDStatisticsPercentilesEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne180100EPS9_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString24HDStatisticsTimeIntervalEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne180100EPS9_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIN6health12InMemoryFileEEEEEPvEENS_22__tree_node_destructorINS6_ISF_EEEEE5resetB8ne180100EPSF_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne180100EPS9_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEPvEENS_22__tree_node_destructorINS_9allocatorIS9_EEEEE5resetB8ne180100EPS9_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8ne180100EPS8_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEEPvEENS_22__tree_node_destructorINS_9allocatorISB_EEEEE5resetB8ne180100EPSB_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEEPvEENS_22__tree_node_destructorINS_9allocatorISB_EEEEE5resetB8ne180100EPSB_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIx20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEEEPvEENS_22__tree_node_destructorINS_9allocatorISA_EEEEE5resetB8ne180100EPSA_
- __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEEC2B8ne180100EPKcNS_15regex_constants18syntax_option_typeE
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIN6health12InMemoryFileEEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKx20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKx20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKx20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKx20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKx20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIKx20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI24HDStatisticsTimeIntervalS6_EEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS7_EEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI23HDStatisticsPercentilesEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString20HDStatisticsRelativeI24HDStatisticsTimeIntervalEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString23HDStatisticsPercentilesEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_4pairIU8__strongKP8NSString24HDStatisticsTimeIntervalEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8ne180100INS_7__stateIcEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne180100INS_11__wrap_iterIPKcEESA_EEvT_T0_m
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne180100INS_11__wrap_iterIPcEES9_EEvT_T0_m
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne180100IPKcS8_EEvT_T0_m
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE16__init_with_sizeB8ne180100IPcS7_EEvT_T0_m
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE23__insert_from_safe_copyB8ne180100INS_11__wrap_iterIPKcEESA_EENS7_IPcEEmmT_T0_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ENS_24__uninitialized_size_tagEmRKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100ILi0EEEPKc
- __ZNSt3__113__nth_elementB8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPdEEEEvT1_S8_S8_T0_
- __ZNSt3__113__tree_removeB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__113match_resultsINS_11__wrap_iterIPKcEENS_9allocatorINS_9sub_matchIS4_EEEEE8__assignB8ne180100IS3_NS5_INS6_IS3_EEEEEEvS4_S4_RKNS0_IT_T0_EEb
- __ZNSt3__114__split_bufferINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB8ne180100EPS6_
- __ZNSt3__114__split_bufferINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB8ne180100EPS6_
- __ZNSt3__114__split_bufferINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB8ne180100EPS6_
- __ZNSt3__114__split_bufferINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB8ne180100EPS6_
- __ZNSt3__115insert_iteratorINS_3setIyNS_4lessIyEENS_9allocatorIyEEEEEaSB8ne180100ERKy
- __ZNSt3__116__deque_iteratorI39HDQuantitySampleAttenuationEngineSamplePKS1_RS2_PKS3_lLl102EEpLB8ne180100El
- __ZNSt3__116__deque_iteratorI39HDQuantitySampleAttenuationEngineSamplePS1_RS1_PS2_lLl102EEpLB8ne180100El
- __ZNSt3__116__deque_iteratorINS_5tupleIJddfEEEPS2_RS2_PS3_lLl170EEpLB8ne180100El
- __ZNSt3__116__pad_and_outputB8ne180100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__116__set_differenceB8ne180100INS_17_ClassicAlgPolicyENS_6__lessIvvEERNS_21__tree_const_iteratorIyPNS_11__tree_nodeIyPvEElEESA_SA_SA_RNS_15insert_iteratorINS_3setIyNS_4lessIyEENS_9allocatorIyEEEEEEEENS_4pairIu14__remove_cvrefIT1_Eu14__remove_cvrefIT5_EEEOSL_OT2_OT3_OT4_OSN_OT0_
- __ZNSt3__117bad_function_callD0Ev
- __ZNSt3__118__for_each_segmentB8ne180100INS_16__deque_iteratorI39HDQuantitySampleAttenuationEngineSamplePKS2_RS3_PKS4_lLl102EEENS_11__copy_loopINS_17_ClassicAlgPolicyEE12_CopySegmentIS8_NS1_IS2_PS2_RS2_PSD_lLl102EEEEEEEvT_SI_T0_
- __ZNSt3__118generate_canonicalB8ne180100IdLm53ENS_26linear_congruential_engineIjLj48271ELj0ELj2147483647EEEEET_RT1_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI13HKRawIntervalIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI15HistogramBucketEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI16_HDWrappedSourceEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI19HDRawDistanceSampleEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI19HDRawQuantitySampleEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSC_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsDiscreteE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsPresenceE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSG_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSG_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI22HDStatisticsCumulativeE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI23HDStatisticsPercentilesE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_SampleRemainderEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN6health10FileExtentEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN6health13WriteAheadLog9PageEntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_10unique_ptrIN6health18TransactionalCacheIyNS3_8FilePageEE10CacheEntryENS_14default_deleteIS7_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSE_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_4pairIccEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_4pairImPKcEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_5tupleIJxU8__strongP15HKDeletedObjectEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_5tupleIJxU8__strongP8HKSampleEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_9sub_matchINS_11__wrap_iterIPKcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_9sub_matchIPKcEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP19HDRawQuantitySampleEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIP39HDQuantitySampleAttenuationEngineSampleEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPN6health12BlockPointerEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPNS_11__thread_idEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPNS_5tupleIJddfEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPNS_7__stateIcEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIlEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIxEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8ne180100Ev
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE11EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE12EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE14EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE15EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE16EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE17EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE1EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE2EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE3EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE4EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE5EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE6EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE7EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE8EEEvv
- __ZNSt3__119__throw_regex_errorB8ne180100ILNS_15regex_constants10error_typeE9EEEvv
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne180100Ev
- __ZNSt3__120__bracket_expressionIcNS_12regex_traitsIcEEE10__add_charB8ne180100Ec
- __ZNSt3__120__bracket_expressionIcNS_12regex_traitsIcEEE13__add_digraphB8ne180100Ecc
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne180100EPKc
- __ZNSt3__121__unwrap_and_dispatchB8ne180100INS_10__overloadINS_11__move_loopINS_17_ClassicAlgPolicyEEENS_14__move_trivialEEEP16_HDWrappedSourceS8_S8_Li0EEENS_4pairIT0_T2_EESA_T1_SB_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8HKSource16_HDWrappedSourceEEPvEEEEEclB8ne180100EPSA_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString20HDStatisticsRelativeI22HDStatisticsNoiseLevelEEEPvEEEEEclB8ne180100EPSC_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSString22HDStatisticsNoiseLevelEEPvEEEEEclB8ne180100EPSA_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIU8__strongP8NSStringxEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIxU8__strongP8NSStringEEPvEEEEEclB8ne180100EPS9_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeIyN6health18TransactionalCacheIyNS4_8FilePageEE9CacheLineEEEPvEEEEEclB8ne180100EPSB_
- __ZNSt3__124__put_character_sequenceB8ne180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__124__sort5_maybe_branchlessB8ne180100INS_17_ClassicAlgPolicyERZ51-[HDStatisticsCollectionCalculator orderSourceIDs:]E3$_0PxLi0EEEvT1_S5_S5_S5_S5_T0_
- __ZNSt3__125__throw_bad_function_callB8ne180100Ev
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZ51-[HDStatisticsCollectionCalculator orderSourceIDs:]E3$_0PxEEbT1_S5_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEbT1_SE_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEbT1_SE_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEbT1_SE_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsDiscreteE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsPresenceE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEbT1_SF_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEbT1_SG_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEbT1_SI_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEbT1_SI_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEbT1_SI_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEbT1_SI_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEbT1_SF_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEbT1_SF_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEbT1_SF_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEbT1_SF_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsCumulativeE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEbT1_SB_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsPercentilesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEbT1_SB_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEbT1_SB_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEbT1_SN_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsDiscreteE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsPresenceE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEbT1_SO_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEbT1_SP_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEbT1_SR_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEbT1_SR_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsDiscreteEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsPresenceEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsCumulativeEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsPercentilesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEbT1_SO_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEbT1_SO_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsCumulativeE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsNoiseLevelE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsPercentilesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsSleepStagesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI24HDStatisticsTimeIntervalE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI33HDStatisticsAverageSampleDurationE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEbT1_SK_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
- __ZNSt3__127__insertion_sort_incompleteB8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEbT1_SM_T0_
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS5_EEEEEENS_16reverse_iteratorIPS8_EEEEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS5_EEEEEENS_16reverse_iteratorIPS8_EEEEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS5_EEEEEENS_16reverse_iteratorIPS8_EEEEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS5_EEEEEENS_16reverse_iteratorIPS8_EEEEED2B8ne180100Ev
- __ZNSt3__128__invoke_void_return_wrapperIbLb0EE6__callB8ne180100IJRZN6health9DataStore43accessSampleHistoryWithIdentifierForWritingI25LocationHistoryBehaviorV1EEbRKNS4_16ObjectIdentifierEbNS_8functionIFbRNS4_20MutableSampleHistoryIT_EEEEEEUlRNS4_16WriteTransactionEE_SI_EEEbDpOT_
- __ZNSt3__128__invoke_void_return_wrapperIvLb1EE6__callB8ne180100IJRZNK6health9DataStore43accessSampleHistoryWithIdentifierForReadingI25LocationHistoryBehaviorV1EEbRKNS4_16ObjectIdentifierENS_8functionIFvRKNS4_13SampleHistoryIT_EEEEEEUlRKNS4_15ReadTransactionEE_SK_EEEvDpOT_
- __ZNSt3__128__invoke_void_return_wrapperIvLb1EE6__callB8ne180100IJRZNK6health9DataStore43accessSampleHistoryWithIdentifierForReadingI25LocationHistoryBehaviorV2EEbRKNS4_16ObjectIdentifierENS_8functionIFvRKNS4_13SampleHistoryIT_EEEEEEUlRKNS4_15ReadTransactionEE_SK_EEEvDpOT_
- __ZNSt3__128__invoke_void_return_wrapperIvLb1EE6__callB8ne180100IJRZNK6health9DataStore43accessSampleHistoryWithIdentifierForReadingI29QuantitySampleValueBehaviorV0EEbRKNS4_16ObjectIdentifierENS_8functionIFvRKNS4_13SampleHistoryIT_EEEEEEUlRKNS4_15ReadTransactionEE_SK_EEEvDpOT_
- __ZNSt3__128__invoke_void_return_wrapperIvLb1EE6__callB8ne180100IJRZNK6health9DataStore43accessSampleHistoryWithIdentifierForReadingI29QuantitySampleValueBehaviorV1EEbRKNS4_16ObjectIdentifierENS_8functionIFvRKNS4_13SampleHistoryIT_EEEEEEUlRKNS4_15ReadTransactionEE_SK_EEEvDpOT_
- __ZNSt3__13mapIyN6health18DataStoreInspector15DataSeriesEntryENS_4lessIyEENS_9allocatorINS_4pairIKyS3_EEEEEC2B8ne180100ERKSB_
- __ZNSt3__13setIyNS_4lessIyEENS_9allocatorIyEEEC2B8ne180100ERKS5_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS4_EEEEEENS_16reverse_iteratorIPS7_EESB_SB_EET2_RT_T0_T1_SC_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS4_EEEEEENS_16reverse_iteratorIPS7_EESB_SB_EET2_RT_T0_T1_SC_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS4_EEEEEENS_16reverse_iteratorIPS7_EESB_SB_EET2_RT_T0_T1_SC_
- __ZNSt3__142__uninitialized_allocator_move_if_noexceptB8ne180100INS_9allocatorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS4_EEEEEENS_16reverse_iteratorIPS7_EESB_SB_EET2_RT_T0_T1_SC_
- __ZNSt3__15dequeI19HDRawQuantitySampleNS_9allocatorIS1_EEED2B8ne180100Ev
- __ZNSt3__15dequeI39HDQuantitySampleAttenuationEngineSampleNS_9allocatorIS1_EEE18__append_with_sizeB8ne180100INS_16__deque_iteratorIS1_PKS1_RS7_PKS8_lLl102EEEEEvT_m
- __ZNSt3__15dequeI39HDQuantitySampleAttenuationEngineSampleNS_9allocatorIS1_EEED2B8ne180100Ev
- __ZNSt3__15dequeIN6health12BlockPointerENS_9allocatorIS2_EEE26__maybe_remove_front_spareB8ne180100Eb
- __ZNSt3__15dequeIN6health12BlockPointerENS_9allocatorIS2_EEED2B8ne180100Ev
- __ZNSt3__15dequeINS_11__thread_idENS_9allocatorIS1_EEED2B8ne180100Ev
- __ZNSt3__15dequeINS_7__stateIcEENS_9allocatorIS2_EEED2B8ne180100Ev
- __ZNSt3__16vectorI13HKRawIntervalIdENS_9allocatorIS2_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorI13HKRawIntervalIdENS_9allocatorIS2_EEE16__init_with_sizeB8ne180100IPS2_S7_EEvT_T0_m
- __ZNSt3__16vectorI13HKRawIntervalIdENS_9allocatorIS2_EEE18__assign_with_sizeB8ne180100IPS2_S7_EEvT_T0_l
- __ZNSt3__16vectorI13HKRawIntervalIdENS_9allocatorIS2_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS2_RS4_EEPS2_
- __ZNSt3__16vectorI15HistogramBucketNS_9allocatorIS1_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS1_RS3_EE
- __ZNSt3__16vectorI16_HDWrappedSourceNS_9allocatorIS1_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorI16_HDWrappedSourceNS_9allocatorIS1_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorI16_HDWrappedSourceNS_9allocatorIS1_EEE16__init_with_sizeB8ne180100IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorI19HDRawQuantitySampleNS_9allocatorIS1_EEE16__init_with_sizeB8ne180100IPS1_S6_EEvT_T0_m
- __ZNSt3__16vectorINS_10shared_ptrIN6health13WriteAheadLog11TransactionEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10shared_ptrIN6health13WriteAheadLog11TransactionEEENS_9allocatorIS5_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS6_RS8_EE
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics10StatisticsENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS6_RS8_EE
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics17RawQuantitySampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS6_RS8_EE
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics37QuantitySampleAttenuationEngineSampleENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS6_RS8_EE
- __ZNSt3__16vectorINS_10unique_ptrIN10statistics8IntervalENS_14default_deleteIS3_EEEENS_9allocatorIS6_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN6health18TransactionalCacheIyNS2_8FilePageEE10CacheEntryENS_14default_deleteIS6_EEEENS_9allocatorIS9_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_10unique_ptrIN6health18TransactionalCacheIyNS2_8FilePageEE10CacheEntryENS_14default_deleteIS6_EEEENS_9allocatorIS9_EEE22__base_destruct_at_endB8ne180100EPS9_
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEES7_EENS5_IS8_EEE9push_backB8ne180100EOS8_
- __ZNSt3__16vectorINS_4pairImPKcEENS_9allocatorIS4_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorINS_4pairImPKcEENS_9allocatorIS4_EEE16__init_with_sizeB8ne180100IPS4_S9_EEvT_T0_m
- __ZNSt3__16vectorINS_5tupleIJxU8__strongP15HKDeletedObjectEEENS_9allocatorIS5_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorINS_5tupleIJxU8__strongP15HKDeletedObjectEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_5tupleIJxU8__strongP15HKDeletedObjectEEENS_9allocatorIS5_EEE16__init_with_sizeB8ne180100IPS5_SA_EEvT_T0_m
- __ZNSt3__16vectorINS_5tupleIJxU8__strongP15HKDeletedObjectEEENS_9allocatorIS5_EEE18__construct_at_endIPS5_SA_EEvT_T0_m
- __ZNSt3__16vectorINS_5tupleIJxU8__strongP8HKSampleEEENS_9allocatorIS5_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorINS_5tupleIJxU8__strongP8HKSampleEEENS_9allocatorIS5_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_5tupleIJxU8__strongP8HKSampleEEENS_9allocatorIS5_EEE16__init_with_sizeB8ne180100IPS5_SA_EEvT_T0_m
- __ZNSt3__16vectorINS_5tupleIJxU8__strongP8HKSampleEEENS_9allocatorIS5_EEE18__construct_at_endIPS5_SA_EEvT_T0_m
- __ZNSt3__16vectorINS_7__stateIcEENS_9allocatorIS2_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS_9sub_matchINS_11__wrap_iterIPKcEEEENS_9allocatorIS6_EEE16__init_with_sizeB8ne180100IPS6_SB_EEvT_T0_m
- __ZNSt3__16vectorINS_9sub_matchIPKcEENS_9allocatorIS4_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorINS_9sub_matchIPKcEENS_9allocatorIS4_EEE16__init_with_sizeB8ne180100IPS4_S9_EEvT_T0_m
- __ZNSt3__16vectorIU8__strongP8HKSourceNS_9allocatorIS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB8ne180100IPdS5_EEvT_T0_m
- __ZNSt3__16vectorIdNS_9allocatorIdEEE18__assign_with_sizeB8ne180100IPdS5_EEvT_T0_l
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEEC2Em
- __ZNSt3__16vectorIxNS_9allocatorIxEEE16__init_with_sizeB8ne180100IPxS5_EEvT_T0_m
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERNS_6__lessIvvEENS_11__wrap_iterIPdEEEEjT1_S8_S8_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZ51-[HDStatisticsCollectionCalculator orderSourceIDs:]E3$_0PxEEjT1_S5_S5_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEjT1_SE_SE_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEjT1_SE_SE_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEjT1_SE_SE_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsDiscreteE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsPresenceE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEjT1_SF_SF_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEjT1_SG_SG_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEjT1_SI_SI_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEjT1_SI_SI_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEjT1_SI_SI_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEjT1_SI_SI_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEjT1_SF_SF_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEjT1_SF_SF_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEjT1_SF_SF_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEjT1_SF_SF_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsCumulativeE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEjT1_SB_SB_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsPercentilesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEjT1_SB_SB_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEjT1_SB_SB_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEjT1_SN_SN_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsDiscreteE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsPresenceE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEjT1_SO_SO_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEjT1_SP_SP_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEjT1_SR_SR_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEjT1_SR_SR_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsDiscreteEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsPresenceEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsCumulativeEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsPercentilesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEjT1_SO_SO_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEjT1_SO_SO_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsCumulativeE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsNoiseLevelE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsPercentilesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsSleepStagesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI24HDStatisticsTimeIntervalE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI33HDStatisticsAverageSampleDurationE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEjT1_SK_SK_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
- __ZNSt3__17__sort3B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEjT1_SM_SM_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZ51-[HDStatisticsCollectionCalculator orderSourceIDs:]E3$_0PxEEvT1_S5_S5_S5_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsDiscreteE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsPresenceE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEvT1_SI_SI_SI_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEvT1_SI_SI_SI_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEvT1_SI_SI_SI_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEvT1_SI_SI_SI_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEvT1_SF_SF_SF_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEvT1_SF_SF_SF_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsCumulativeE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEvT1_SB_SB_SB_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsPercentilesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEvT1_SB_SB_SB_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsDiscreteE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsPresenceE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEvT1_SR_SR_SR_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEvT1_SR_SR_SR_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsDiscreteEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsPresenceEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsCumulativeEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsPercentilesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsCumulativeE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsNoiseLevelE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsPercentilesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsSleepStagesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI24HDStatisticsTimeIntervalE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI33HDStatisticsAverageSampleDurationE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
- __ZNSt3__17__sort4B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E0_PS8_EEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS7_16_SampleRemainderESA_E_PS8_EEvT1_SE_SE_SE_SE_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsDiscreteE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsPresenceE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E0_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_SF_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNS9_16_SampleRemainderESC_E_PSA_EEvT1_SG_SG_SG_SG_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEvT1_SI_SI_SI_SI_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEvT1_SI_SI_SI_SI_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E0_PSC_EEvT1_SI_SI_SI_SI_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE16_mergeTowardTimeEdEUlRKNSB_16_SampleRemainderESE_E_PSC_EEvT1_SI_SI_SI_SI_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsDiscreteEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsPresenceEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsCumulativeEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsPercentilesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEvT1_SF_SF_SF_SF_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_SF_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E0_PS9_EEvT1_SF_SF_SF_SF_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE16_mergeTowardTimeEdEUlRKNS8_16_SampleRemainderESB_E_PS9_EEvT1_SF_SF_SF_SF_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsCumulativeE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEvT1_SB_SB_SB_SB_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI22HDStatisticsNoiseLevelE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsPercentilesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E0_PS5_EEvT1_SB_SB_SB_SB_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI23HDStatisticsSleepStagesE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI24HDStatisticsTimeIntervalE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI33HDStatisticsAverageSampleDurationE16_mergeTowardTimeEdEUlRKNS4_16_SampleRemainderES7_E_PS5_EEvT1_SB_SB_SB_SB_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E0_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN18HDStatisticsBucketI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE16_mergeTowardTimeEdEUlRKNS6_16_SampleRemainderES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS4_EE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS9_EEEEPU15__autoreleasingP7NSErrorEUlRKS9_SJ_E_PS9_EEvT1_SN_SN_SN_SN_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsDiscreteE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsPresenceE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS5_EEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_SO_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISB_EEEEPU15__autoreleasingP7NSErrorEUlRKSB_SL_E_PSB_EEvT1_SP_SP_SP_SP_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEvT1_SR_SR_SR_SR_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISD_EEEEPU15__autoreleasingP7NSErrorEUlRKSD_SN_E_PSD_EEvT1_SR_SR_SR_SR_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsDiscreteEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsPresenceEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsCumulativeEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsPercentilesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI23HDStatisticsSleepStagesEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI24HDStatisticsTimeIntervalEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI33HDStatisticsAverageSampleDurationEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_SO_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorISA_EEEEPU15__autoreleasingP7NSErrorEUlRKSA_SK_E_PSA_EEvT1_SO_SO_SO_SO_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsCumulativeE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsNoiseLevelE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsPercentilesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI23HDStatisticsSleepStagesE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI24HDStatisticsTimeIntervalE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI33HDStatisticsAverageSampleDurationE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS6_EEEEPU15__autoreleasingP7NSErrorEUlRKS6_SG_E_PS6_EEvT1_SK_SK_SK_SK_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
- __ZNSt3__17__sort5B8ne180100INS_17_ClassicAlgPolicyERZN55_HDConcreteStatisticsCollectionCalculatorImplementationI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersEE18_addPendingSamplesERNS_6vectorI19HDRawQuantitySampleNS_9allocatorIS8_EEEEPU15__autoreleasingP7NSErrorEUlRKS8_SI_E_PS8_EEvT1_SM_SM_SM_SM_T0_
- __ZNSt3__1eqB8ne180100INS_9allocatorIcEEEEbRKNS_12basic_stringIcNS_11char_traitsIcEET_EES9_
- __ZNSt3__1ssB8ne180100IcNS_11char_traitsIcEEEEDaNS_17basic_string_viewIT_T0_EENS_13type_identityIS7_E4typeE
- __ZNSt3__1ssB8ne180100IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
- __ZNSt9exceptionD2Ev
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- __ZTSNSt3__117bad_function_callE
- ___100-[HDDatabasePruningCoordinator _pruneProfilesWithIdentifiers:takeAccessibilityAssertion:completion:]_block_invoke
- ___104+[HDUserDomainConceptAPIObjectManager generateAPIObjectForUserDomainConcept:apiObjectOut:profile:error:]_block_invoke
- ___104-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:promptHandler:completion:]_block_invoke
- ___104-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:promptHandler:completion:]_block_invoke_2
- ___104-[HDDatabasePruningTask _pruneDatabaseWithNowDate:prunedObjectLimit:prunedObjectTransactionLimit:error:]_block_invoke
- ___126-[HDDatabasePruningTask pruneDatabaseWithAccessibilityAssertion:nowDate:prunedObjectLimit:prunedObjectTransactionLimit:error:]_block_invoke
- ___138+[HDCloudSyncStore createOrUpdateShardStoresForProfile:throughDate:syncCircleName:ownerIdentifier:containerIdentifier:syncIdentity:error:]_block_invoke
- ___138+[HDCloudSyncStore createOrUpdateShardStoresForProfile:throughDate:syncCircleName:ownerIdentifier:containerIdentifier:syncIdentity:error:]_block_invoke_2
- ___173-[HDCloudSyncStore _initWithProfile:storeIdentifier:syncCircleName:ownerIdentifier:syncIdentity:containerIdentifier:sharingIdentifier:sharingPredicate:shardPredicate:error:]_block_invoke
- ___173-[HDCloudSyncStore _initWithProfile:storeIdentifier:syncCircleName:ownerIdentifier:syncIdentity:containerIdentifier:sharingIdentifier:sharingPredicate:shardPredicate:error:]_block_invoke_2
- ___71+[HDSyncStoreEntity syncStoreEntityWithUUID:type:healthDatabase:error:]_block_invoke
- ___71+[HDSyncStoreEntity syncStoreEntityWithUUID:type:healthDatabase:error:]_block_invoke_2
- ___71-[HDClientAuthorizationOracle readAuthorizationStatusesForTypes:error:]_block_invoke
- ___80-[HDClientAuthorizationOracle filteredObjectsForReadAuthorization:anchor:error:]_block_invoke
- ___block_descriptor_104_e8_32s40s48s56s64s72s80r88r_e35_B24?0"HDDatabaseTransaction"8^16l
- ___block_descriptor_32_e35_B16?0"HDReadAuthorizationStatus"8l
- ___block_descriptor_40_e8_32s_e56_v32?0"HKObjectType"8"HDReadAuthorizationStatus"16^B24l
- ___block_descriptor_40_ea8_32bs_e5_v8?0l
- ___block_descriptor_48_e8_32r40r_e56_v32?0"HKObjectType"8"HDReadAuthorizationStatus"16^B24l
- ___block_descriptor_48_e8_32s40s_e26_"NSArray"16?0"NSArray"8l
- ___block_descriptor_56_e8_32s40r_e35_B24?0"HDDatabaseTransaction"8^16lu48l8
- ___block_descriptor_56_e8_32s40s48s_e18_B16?0"HKObject"8l
- ___block_descriptor_56_e8_32s40s48s_e56_v32?0"HKObjectType"8"HDReadAuthorizationStatus"16^B24l
- ___block_descriptor_64_e8_32s40s48s56bs_e14_v16?0?<v?>8l
- ___block_descriptor_64_e8_32s40s_e9_B16?0^8l
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s_e35_B24?0"HDDatabaseTransaction"8^16l
- __block_literal_global.357
- __block_literal_global.373
- __block_literal_global.380
- __block_literal_global.391
- __block_literal_global.433
- __block_literal_global.439
- __block_literal_global.527
- __block_literal_global.549
- __block_literal_global.620
- __block_literal_global.630
- __block_literal_global.657
- __isCompanionSyncToUSLegallyCompliantOxygenSaturationDeviceForSyncSession
- _fmod
- _objc_msgSend$_enumerateConceptDeriveAPIObjectAndAddToResults:mutableResults:profile:transaction:error:
- _objc_msgSend$_startWatchAppWithWorkoutPlanData:processIdentifier:completion:
- _objc_msgSend$createOrUpdateShardStoresForProfile:throughDate:syncCircleName:ownerIdentifier:containerIdentifier:syncIdentity:error:
- _objc_msgSend$enqueueMaintenanceOperationOnCoordinator:takeAccessibilityAssertion:nowDate:completion:
- _objc_msgSend$handleObjectAuthorizationRequestsForBundleIdentifier:promptHandler:completion:
- _objc_msgSend$handleObjectAuthorizationRequestsWithPromptHandler:completion:
- _objc_msgSend$initForBundleIdentifier:sessionIdentifier:
- _objc_msgSend$pruneDatabaseWithAccessibilityAssertion:nowDate:error:
- _objc_msgSend$pruneDatabaseWithAccessibilityAssertion:nowDate:prunedObjectLimit:prunedObjectTransactionLimit:error:
- _objc_msgSend$readAuthorizationStatusForType:error:
- _objc_msgSend$readAuthorizationStatusesForTypes:error:
- _objc_msgSend$remoteDeviceSupportsUSLegallyCompliantOxygenSaturation
- _objc_msgSend$shardPredicatesForProfile:syncCircleName:currentDate:error:
- _objc_msgSend$startWatchAppWithWorkoutPlanData:processIdentifier:completion:
- _objc_msgSend$syncStoreForProfile:storeIdentifier:syncCircleName:ownerIdentifier:syncIdentity:containerIdentifier:error:
- _objc_msgSend$unprocessedBloodOxygenDataType
- _strncmp
- _swift_bridgeObjectRetain_n
CStrings:
+ "!!"
+ "%@ LIMIT ?"
+ "%@ object does not comform to the type protocol"
+ "%@: Provider %@: does not respond to the selector for the following object set %@:"
+ "%{public}@: Attempting to take assertions and collection already ended"
+ "%{public}@: Failed to cache excluded sync identities because store is not set."
+ "%{public}@: Failed to cache excluded sync identities with error: %{public}@"
+ "%{public}@: Failed to check whether device has upgraded to sync identity: %{public}@"
+ "%{public}@: Failed to find authorization status record for %ld objects with an error: %@"
+ "%{public}@: Failed to load cached excluded sync identities with error: %{public}@"
+ "%{public}@: Failed to read file from source for URL %{public}@. %{public}@"
+ "%{public}@: Failed to write file to URL %{public}@. %{public}@"
+ "%{public}@: Pruning activity was deferred after pruning %ld objects in %0.2lfs"
+ "%{public}@: Pruning activity was deferred."
+ "%{public}s Setting swim reference to %@"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDBPlusTree.hpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDBlockAccessFile.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDTransactionalFile.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDVirtualFilesystem.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDWriteAheadLog.cpp"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDEncoder.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDFilePage.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDRawBuffer.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDStaticArray.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDTransactionalCache.hpp"
+ "2B `"
+ "@\"<HDSyncStore>\"16@?0@\"HDTypedSyncStoreIdentifier\"8"
+ "@\"HDDatabasePruningShowSyncStore\"16@?0@\"HDDatabasePruningShowSyncStore\"8"
+ "@\"HDSamplePruningRestrictionPredicate\"16@?0@\"<HDSyncStore>\"8"
+ "@\"HDSamplePruningRestrictionPredicate\"32@0:8#16^@24"
+ "@\"HDSyncEntityIdentifier\""
+ "@\"HDTypedSyncStoreIdentifier\"16@?0@\"HDDatabasePruningShowSyncStore\"8"
+ "@\"NSArray\"64@0:8@\"NSOrderedSet\"16@\"NSNumber\"24@\"NSString\"32@\"_HKEntitlements\"40@\"HDProfile\"48^@56"
+ "@\"NSError\"16@?0@\"NSError\"8"
+ "@\"NSNumber\"56@0:8@\"NSArray\"16Q24@\"NSDate\"32@\"HDProfile\"40^@48"
+ "@\"NSUUID\"16@?0@\"HDTypedSyncStoreIdentifier\"8"
+ "@16@?0@\"HDConcreteSyncIdentity\"8"
+ "@16@?0@\"HDSamplePruningRestrictionPredicate\"8"
+ "@48@0:8@16@24@?32^@40"
+ "@48@0:8q16@24@32@40"
+ "@56@0:8@16@24B32B36@40@48"
+ "@56@0:8@16@24q32q40^@48"
+ "@60@0:8@16B24@28q36q44^@52"
+ "@64@0:8@16@24@32@40@48^@56"
+ "@64@0:8q16@24@32@40@48q56"
+ "@80@0:8q16@24@32@40@48@56@64@72"
+ "@`"
+ "ALTER TABLE cloud_sync_stores ADD COLUMN cached_excluded_sync_identities BLOB NULL DEFAULT NULL"
+ "Analytics coordinator unexpectedly nil\n                                                         Operation Name: %@\n                                                         Database Protection: %@\n                                                         Pending Operations Count: %lu\n                                                         Acitve Operations Count: %lu\n                                                         Time Until Start (sec): %.2f\n                                                         Was Canceled: %i\n                                                         Did Time Out: %i\n                                                         Elapsed Time: %.2f\n                                                         Is Immediate Request: %i\n                                                         Async: %i\n"
+ "Attempted to instantiate sync store that is not supported."
+ "B16@?0@\"HDAuthorizationStatusRecord\"8"
+ "B16@?0@\"HDSyncEntityIdentifier\"8"
+ "B16@?0@\"HDSyncStoreEntity\"8"
+ "B24@?0@\"HDSyncEntityIdentifier\"8@\"NSNumber\"16"
+ "B48@0:8@16@24@32@40"
+ "B56@0:8@16q24Q32^@40@?48"
+ "BLOB NULL DEFAULT NULL"
+ "CacheSettings"
+ "Client %@ is not authorized to delete for data type(s) %@"
+ "Client %@ is not authorized to delete for data type(s)."
+ "Client %@ is not authorized to delete objects for data type(s) %@"
+ "Client %@ is not read authorized for objects of data type(s) %@"
+ "Client %@ is not write authorized to save objects for data type(s) %@"
+ "Client %{public}@ is not authorized to delete objects for data type(s)."
+ "Client %{public}@ is not read authorized for data type(s)."
+ "Client %{public}@ is not read authorized for objects of data type(s)."
+ "Client %{public}@ is not write authorized for data type(s)."
+ "Client %{public}@ is not write authorized to save objects for data type(s)."
+ "DEFAULT"
+ "Duplicate values for key: '"
+ "HDAuthorizationStatusRecord"
+ "HDAuthorizationStatusRecord.m"
+ "HDDatabasePruningShow"
+ "HDDatabasePruningShowDeletedSample"
+ "HDDatabasePruningShowEntity"
+ "HDDatabasePruningShowShim"
+ "HDDatabasePruningShowSyncIdentity"
+ "HDDatabasePruningShowSyncStore"
+ "HDMedicationDoseEventEntityEncodingOptionExcludePrivateMedicationInfo"
+ "HDSamplePruningRestrictionPredicate"
+ "HDTypedSyncStoreIdentifier"
+ "HKTypeProtocol"
+ "Long database transaction %{public}@ duration: duration=%{public}@, wait=%{public}@, work=%{public}@, write=%{BOOL}d, protected=%{BOOL}d, priority=%{BOOL}d, cache=%ld, journal=%ld, queue=%{public}s"
+ "SELECT %@ FROM %@ AS ss WHERE EXISTS (SELECT 1 FROM %@ AS sa WHERE ss.%@ == sa.%@ AND sa.%@ > ?)"
+ "SELECT %@, %@ FROM %@ AS ss WHERE ss.%@ > ? OR EXISTS (SELECT 1 FROM %@ AS sa WHERE ss.%@ == sa.%@ AND sa.%@ > ?)"
+ "SELECT %@, %@, %@, MIN(%@) FROM %@ GROUP BY %@, %@, %@"
+ "SELECT %@, MAX(%@) FROM %@ GROUP BY %@"
+ "SELECT o.%@, o.%@, o.%@, s.%@, s.%@, p.%@ FROM %@ AS s INNER JOIN %@ AS o ON s.%@ == o.%@ INNER JOIN %@ AS p ON o.%@ == p.%@ WHERE o.%@ == ? AND o.%@ == ?"
+ "SELECT o.%@, o.%@, o.%@, s.%@, s.%@, p.%@ FROM %@ AS s INNER JOIN %@ AS o ON s.%@ == o.%@ INNER JOIN %@ AS p ON o.%@ == p.%@ WHERE o.%@ > ? AND o.%@ == ? ORDER BY o.%@ ASC"
+ "Starting transaction %{public}@"
+ "Swift/Dictionary.swift"
+ "Swift/NativeDictionary.swift"
+ "T@\"HDClientAuthorizationOracle\",R,W,N,V_authorizationOracle"
+ "T@\"HDSyncEntityIdentifier\",R,N,V_identifier"
+ "T@\"NSDate\",R,N,V_endDate"
+ "T@\"NSDate\",R,N,V_latestFrozenAnchorDate"
+ "T@\"NSDictionary\",R,N,V_frozenAnchorMap"
+ "T@\"NSDictionary\",R,N,V_pruningRestrictionPredicates"
+ "T@\"NSNumber\",R,N,V_isSupportedShardType"
+ "T@\"NSNumber\",R,N,V_maximumAnchor"
+ "T@\"NSNumber\",R,N,V_maximumPruningAnchor"
+ "T@\"NSNumber\",R,N,V_syncIdentity"
+ "T@\"NSNumber\",R,N,V_type"
+ "T@\"NSSet\",R,N,V_excludedSyncIdentities"
+ "T@\"NSString\",R,N,V_className"
+ "T@\"NSString\",R,N,V_instanceDiscriminator"
+ "T@\"NSUUID\",R,N,V_databaseIdentifier"
+ "T@\"NSUUID\",R,N,V_hardwareIdentifier"
+ "T@\"NSUUID\",R,N,V_identifier"
+ "TB,N,V_didTimeOut"
+ "TB,N,V_wasCanceled"
+ "TB,R,N,V_supportsPruning"
+ "TB,R,N,V_supportsPruningRestrictionPredicates"
+ "Td,N,V_startedTime"
+ "Tq,R,N,V_persitentID"
+ "Unable to determine the authorization providers for the objects %@, hence returning nil"
+ "Unable to determine the provider for the object %@"
+ "Unable to determine the provider for this object %@"
+ "Unable to determine the provider for this type %@"
+ "Unable to generate demo data before a person has been set."
+ "[analytics] %{public}@: Failed to retrieve most recent transaction creation date for analytics: %{public}@"
+ "[analytics] Failed to fetch MedicalID for daily analytics with error %{public}@"
+ "[database] %{public}@ Failed to migrate Medical ID before update, error: %{public}@"
+ "[database] %{public}@ Failed to unarchive Medical ID fetched from disk, error: %{public}@"
+ "[database] %{public}@ Medical ID on disk is non-nil but empty, returning nil to the client in this case"
+ "[database] %{public}@ Unarchived MedicalID on disk is nil even though raw data was retrieved."
+ "[database] %{public}@: ConcreteSyncIdentity from received codable is nil %{public}@"
+ "[database] %{public}@: Failed to delete file from path %{public}@ with error %{public}@"
+ "[database] %{public}@: Failed to fetch relationships for associations: %{public}@"
+ "[database] %{public}@: Failed to get persisted entity for workout: %{public}@, %{public}@"
+ "[database] %{public}@: Failed to move file from %{public}@ -> %{public}@ directory with error %{public}@"
+ "[database] %{public}@: No references remaining. Deleting attachment with identifier %{public}@"
+ "[database] %{public}@: No sample relationships found"
+ "[database] %{public}@: No such file error for attachment %{public}@"
+ "[database] %{public}@: Successfully journaled sharing entries."
+ "[database] Error looking up samples associated with %@: %@"
+ "[database] Error writing Medical ID data file at %@, %{public}@"
+ "[database] Expected only a single reference for attachment: %{public}@ and object: %{public}@, found %lu"
+ "[database] Failed to decode Medical ID data: %{public}@"
+ "[database] Failed to fetch MedicalID during database migration with error %{public}@"
+ "[database] Failed to get blood type for Medical ID: %{public}@"
+ "[database] Failed to get date of birth for Medical ID: %{public}@"
+ "[database] Failed to get height for Medical ID: %{public}@"
+ "[database] Failed to get weight for Medical ID: {public}%@"
+ "[database] Failed to migrate Medical ID before update: %{public}@"
+ "[database] Failed to save migrated Medical ID data: %{public}@"
+ "[database] Failed to touch Medical ID sync anchor: %{public}@"
+ "[database] Migrated Medical ID data to version %li"
+ "[database] Migrated Medical ID from %{public}@ to %{public}@"
+ "[database] Obliterating Medical ID with reason: %{public}@"
+ "[database] Server failed to archive Medical ID data: %{public}@"
+ "[query] %{public}@: Delivering relationships to client: %{private}@"
+ "[query] %{public}@: Failed to filter samples for authorization: %{public}@"
+ "[sharing] %{public}@: Attempting to resolve contacts."
+ "[sharing] %{public}@: Contacts changed notification received."
+ "[sharing] %{public}@: Disabling all sharing entries"
+ "[sharing] %{public}@: Error resolving contacts %{public}@."
+ "[sharing] %{public}@: Error retrieving entry with predicate %{public}@."
+ "[sharing] %{public}@: Updating %lu entries."
+ "[sync] Could not synchronize Medical Id flag for watch"
+ "_analyticsCoordinator"
+ "_className"
+ "_didTimeOut"
+ "_includeMedicationAndScheduledItemDetails"
+ "_instantiateStores:profile:error:"
+ "_isSupportedShardType"
+ "_isSupportedShardTypeForRestrictionPredicates"
+ "_latestFrozenAnchorDate"
+ "_maximumAnchor"
+ "_maximumPruningAnchor"
+ "_maximumPruningAnchorWithRestrictionPredicates:"
+ "_minimumFrozenAnchorMapForPruningDate:error:"
+ "_performWhenDataProtectedByFirstUnlockIsAvailableOnQueue"
+ "_persistentIDForSyncIdentity:profile:error:"
+ "_persitentID"
+ "_pruningPredicateWithRestrictionPredicates:"
+ "_pruningRestrictionPredicates"
+ "_setDoseUnit:"
+ "_startWatchAppWithWorkoutPlanData:client:completion:"
+ "_supportsPruning"
+ "_supportsPruningRestrictionPredicates"
+ "_syncStoresInProfile:error:"
+ "_untypedEntityClasses"
+ "_wasCanceled"
+ "activeOperationsCount"
+ "activeStoresForMaxAnchorPruningInProfile:referenceDate:error:"
+ "activeStoresForMaxAnchorWithProfile:referenceDate:error:"
+ "activeStoresForRestrictionPredicatesWithProfile:referenceDate:error:"
+ "activeStoresForRestrictionPredictePruningInProfile:referenceDate:error:"
+ "authorizationStatusForRecordForObjectType:authorizationStatusRecord:clientEntitlements:"
+ "authorizationStatusRecordForType:error:"
+ "authorizationStatusRecordsForTypes:error:"
+ "cacheExcludedSyncIdentities:storeIdentifier:database:error:"
+ "cacheExcludedSyncIdentities:storeIdentifier:profile:error:"
+ "cacheIdentifier"
+ "cachedExcludedSyncIdentitiesForStoreIdentifier:database:error:"
+ "cachedExcludedSyncIdentitiesForStoreIdentifier:profile:error:"
+ "cached_excluded_sync_identities"
+ "canPerformRecentRecordRoll"
+ "canPerformRecentRecordRollWithProfile:"
+ "className"
+ "classifiedDeletedSampleInfoWithProfile:referenceDate:anchor:limit:error:"
+ "com.apple.healthd.maintenance.coordinator"
+ "compoundPredicateWithPredicate:otherPredicate:otherPredicate:"
+ "createOrUpdateShardStoresForProfile:throughDate:ownerIdentifier:containerIdentifier:syncIdentity:error:"
+ "currentSyncIdentityWithProfile:"
+ "databasePruningTaskShouldUseRestrictionPredicates"
+ "datesMatchSampleStartDate:sampleEndDate:shardStartDate:shardEndDate:"
+ "deletedSampleDetailWithProfile:matchingPredicatesOnly:referenceDate:sampleUUID:error:"
+ "deletedSampleInProfile:sampleUUID:error:"
+ "deletedSampleInProfile:sampleUUID:error:handler:"
+ "deletedSampleInfoWithProfile:referenceDate:error:"
+ "deletedSampleSyncEntityClassName"
+ "deletedSampleSyncEntityIdentifier"
+ "deletedSamplesDetailWithProfile:matchingPredicatesOnly:referenceDate:anchor:limit:error:"
+ "deletedSamplesInProfile:anchor:limit:error:"
+ "didTimeOut"
+ "enqueueMaintenanceOperationOnCoordinator:takeAccessibilityAssertion:nowDate:shouldDefer:completion:"
+ "entitiesInProfile:referenceDate:shouldIncludeEntity:error:"
+ "enumerateDeletedSamplesInProfile:anchor:limit:error:handler:"
+ "existingSyncStoreEntityWithUUID:ofType:database:error:"
+ "filteredAuthorizedObjectsForClient:anchor:bundleIdentifier:clientEntitlements:error:"
+ "filteredAuthorizedObjectsForClient:anchor:bundleIdentifier:clientEntitlements:profile:error:"
+ "frozenAnchorMapPerStoreInProfile:error:"
+ "handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:"
+ "handleObjectAuthorizationRequestsWithPromptHandler:objectType:completion:"
+ "hasAuthorizationBypassToReadType:"
+ "hk_objectType"
+ "initForBundleIdentifier:sessionIdentifier:objectType:"
+ "initWithAnalyticsCoordinator:"
+ "initWithClassName:identifier:supportsPruning:supportsPruningRestrictionPredicates:maximumPruningAnchor:pruningRestrictionPredicates:"
+ "initWithIdentifier:type:"
+ "initWithInteger:"
+ "initWithMaximumAnchor:startDate:endDate:excludedSyncIdentities:"
+ "initWithPersistentID:hardwareIdentifier:databaseIdentifier:instanceDiscriminator:"
+ "initWithPersistentID:identifier:type:creationDate:"
+ "initWithPersistentID:identifier:type:creationDate:latestFrozenAnchorDate:frozenAnchorMap:syncIdentity:isSupportedShardType:"
+ "initWithRowID:identifier:creationDate:startDate:endDate:syncIdentity:"
+ "isSupportedShardType"
+ "key value "
+ "latestFrozenAnchorDate"
+ "latestFrozenAnchorUpdatePerStoreInProfile:error:"
+ "lower upper "
+ "maintenanceCoordinator_reportCoreAnalyticsWithOperationName:database:pendingOperationsCount:activeOperationsCount:timeUntilStart:canceled:timedOut:elapsedTime:isImmediateRequest:async:"
+ "maximumAnchor"
+ "maximumPruningAnchor"
+ "operationsOfType:"
+ "pendingOperationsCount"
+ "persitentID"
+ "providesSamplePruningRestrictionPredicate"
+ "pruneDatabaseWithAccessibilityAssertion:nowDate:prunedObjectLimit:prunedObjectTransactionLimit:shouldDefer:error:"
+ "pruneSyncedObjectsWithRestrictionPredicates:limit:nowDate:profile:error:"
+ "pruningFrozenAnchorRelevanceInterval"
+ "pruningRestrictionPredicates"
+ "q56@0:8@\"<HKTypeProtocol>\"16@\"NSString\"24@\"_HKEntitlements\"32@\"HDProfile\"40^@48"
+ "q64@0:8@16@24Q32Q40@?48^@56"
+ "recentStoreAnchorRelevanceInterval"
+ "remote_classifiedDeletedSampleInfoWithReferenceDate:anchor:limit:completion:"
+ "remote_deletedSampleDetailWithReferenceDate:matchingPredicatesOnly:sampleUUID:completion:"
+ "remote_deletedSampleInfoWithReferenceDate:completion:"
+ "remote_deletedSamplesDetailWithReferenceDate:matchingPredicatesOnly:anchor:limit:completion:"
+ "remote_pruneSamplesWithReferenceDate:completion:"
+ "remote_showAndDeletedSampleInfoWithReferenceDate:completion:"
+ "remote_showWithReferenceDate:deletedSamplesOnly:completion:"
+ "remote_startWatchAppWithWorkoutPlanData:completion:"
+ "samplePruningRestrictionPredicateForSyncEntity:error:"
+ "setDidTimeOut:"
+ "setStartedTime:"
+ "setWasCanceled:"
+ "shardIntervalWithStartDate:endDate:"
+ "shardPredicatesForProfile:currentDate:error:"
+ "showAndDeletedSampleInfoWithProfile:referenceDate:error:"
+ "showWithProfile:deletedSamplesOnly:referenceDate:error:"
+ "startWatchAppWithWorkoutPlanData:client:completion:"
+ "startedTime"
+ "storeIdentifier != nil"
+ "supportsPruning"
+ "supportsPruningRestrictionPredicates"
+ "syncIdentitiesInProfile:error:"
+ "syncStoreEntityWithUUID:type:creationDate:healthDatabase:error:"
+ "syncStoreForProfile:storeIdentifier:error:"
+ "syncStoreForProfile:storeIdentifier:ownerIdentifier:syncIdentity:containerIdentifier:creationDate:error:"
+ "syncStoreForProfile:storeIdentifier:ownerIdentifier:syncIdentity:containerIdentifier:error:"
+ "syncStoresInProfile:shouldIncludeEntityIdentifier:error:"
+ "timeIntervalSince1970"
+ "transactionWithName:"
+ "unitTest_pruningPredicateWithRestrictionPredicates:"
+ "unknown"
+ "v24@?0@\"<HDSyncStore>\"8@?<v@?@\"NSUUID\"@\"<HDSyncStore>\">16"
+ "v32@0:8@\"NSDate\"16@?<v@?@\"NSData\"@\"NSError\">24"
+ "v32@?0@\"<HDAuthorizationSchemaProvider>\"8@\"NSMutableOrderedSet\"16^B24"
+ "v32@?0@\"HKObject\"8Q16^B24"
+ "v32@?0@\"HKObjectType\"8@\"HDAuthorizationStatusRecord\"16^B24"
+ "v36@0:8@\"NSDate\"16B24@?<v@?@\"NSData\"@\"NSError\">28"
+ "v40@0:8@?16@24@?32"
+ "v44@0:8@\"NSDate\"16B24@\"NSUUID\"28@?<v@?@\"NSData\"@\"NSError\">36"
+ "v48@0:8@\"NSDate\"16q24q32@?<v@?@\"NSData\"@\"NSError\">40"
+ "v52@0:8@\"NSDate\"16B24q28q36@?<v@?@\"NSData\"@\"NSError\">44"
+ "v52@0:8@16B24@28@?36@?44"
+ "v52@0:8@16B24q28q36@?44"
+ "v56@?0q8@\"NSUUID\"16@\"NSDate\"24@\"NSDate\"32@\"NSDate\"40q48"
+ "v80@0:8@16@24q32q40q48B56B60q64B72B76"
+ "wasCanceled"
+ "\xc1!Q"
- "%{public}@ Failed to migrate Medical ID before update, error: %{public}@"
- "%{public}@ Failed to unarchive Medical ID fetched from disk, error: %{public}@"
- "%{public}@ Medical ID on disk is non-nil but empty, returning nil to the client in this case"
- "%{public}@ Unarchived MedicalID on disk is nil even though raw data was retrieved."
- "%{public}@: Attempting to set samples types and collection already ended"
- "%{public}@: Collection already ended"
- "%{public}@: ConcreteSyncIdentity from received codable is nil %{public}@"
- "%{public}@: Failed to fetch relationships for associations: %{public}@"
- "%{public}@: Failed to find read authorization status for type: %{public}@"
- "%{public}@: Failed to retrieve most recent transaction creation date for analytics: %{public}@"
- "%{public}@: No client source bundle identifier while filtering samples"
- "%{public}@: No sample relationships found"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDBPlusTree.hpp"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDBlockAccessFile.cpp"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDTransactionalFile.cpp"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDVirtualFilesystem.cpp"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/HDWriteAheadLog.cpp"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDEncoder.h"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDFilePage.h"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDRawBuffer.h"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDStaticArray.h"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/HealthKit/HealthKit/HealthDaemon/Database/Migration/HFDtoSQLite/HighFrequencyData/Utility/HDTransactionalCache.hpp"
- "1!"
- "@\"HDSharingPredicate\""
- "@\"NSArray\"48@0:8@\"NSArray\"16@\"HDHealthStoreClient\"24@\"HDProfile\"32^@40"
- "B16@?0@\"HDReadAuthorizationStatus\"8"
- "Client %@ is not delete authorized for data type(s) %@"
- "Client %@ is not delete authorized for data type(s)."
- "Client %@ is not write authorized for data type(s)."
- "Could not synchronize Medical Id flag for watch"
- "Error looking up samples associated with %@: %@"
- "Error writing Medical ID data file at %@, %{public}@"
- "Expected only a single reference for attachment: %{public}@ and object: %{public}@, found %lu"
- "Failed to decode Medical ID data: %{public}@"
- "Failed to fetch MedicalID during database migration with error %{public}@"
- "Failed to fetch MedicalID for daily analytics with error %{public}@"
- "Failed to get blood type for Medical ID: %{public}@"
- "Failed to get date of birth for Medical ID: %{public}@"
- "Failed to get height for Medical ID: %{public}@"
- "Failed to get weight for Medical ID: {public}%@"
- "Failed to migrate Medical ID before update: %{public}@"
- "Failed to save migrated Medical ID data: %{public}@"
- "Failed to touch Medical ID sync anchor: %{public}@"
- "HDCloudSyncPullStoreOperation.m"
- "HDReadAuthorizationStatus"
- "HDReadAuthorizationStatus.m"
- "Insufficient space allocated to copy string contents"
- "Invalid return value form _queue_requiresSyncForSequence:error:; fell out of switch."
- "Long database transaction %{public}@ duration: duration=%{public}@, wait=%{public}@, work=%{public}@, write=%{BOOL}d, protected=%{BOOL}d, priority=%{BOOL}d, cache=%ld, journal=%ld, queue=%s"
- "Migrated Medical ID data to version %li"
- "Migrated Medical ID from %{public}@ to %{public}@"
- "Obliterating Medical ID with reason: %{public}@"
- "Server failed to archive Medical ID data: %{public}@"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "T@\"HDSharingPredicate\",R,N,V_sharingPredicate"
- "T@\"NSString\",R,C,N,V_sharingIdentifier"
- "TB,R,N,V_canPush"
- "TB,R,V_remoteDeviceSupportsUSLegallyCompliantOxygenSaturation"
- "Unable to generate demo data bbefore a person has been set."
- "Unexpected database type (%ld), defaulting to complete protection."
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "User Domain Concept entity was not ever registered for identifier %@"
- "[attachments] %{public}@: Failed to delete file from path %{public}@ with error %{public}@"
- "[attachments] %{public}@: Failed to read file from source for URL %{public}@. %{public}@"
- "[attachments] %{public}@: Failed to write file to URL %{public}@. %{public}@"
- "[attachments] %{public}@: No references remaining. Deleting attachment with identifier %{public}@"
- "[attachments] %{public}@: No such file error for attachment %{public}@"
- "[summary-sharing] %{public}@: Attempting to resolve contacts."
- "[summary-sharing] %{public}@: Contacts changed notification received."
- "[summary-sharing] %{public}@: Disabling all sharing entries"
- "[summary-sharing] %{public}@: Error resolving contacts %{public}@."
- "[summary-sharing] %{public}@: Error retrieving entry with predicate %{public}@."
- "[summary-sharing] %{public}@: Successfully journaled sharing entries."
- "[summary-sharing] %{public}@: Updating %lu entries."
- "_canPush"
- "_enumerateConceptDeriveAPIObjectAndAddToResults:mutableResults:profile:transaction:error:"
- "_remoteDeviceSupportsUSLegallyCompliantOxygenSaturation"
- "_sharingIdentifier"
- "_sharingPredicate"
- "_startWatchAppWithWorkoutPlanData:processIdentifier:completion:"
- "canPush"
- "createOrUpdateShardStoresForProfile:throughDate:syncCircleName:ownerIdentifier:containerIdentifier:syncIdentity:error:"
- "filteredObjectsClientIsAllowedToRead:client:profile:error:"
- "generateAPIObjectForUserDomainConcept:apiObjectOut:profile:error:"
- "handleObjectAuthorizationRequestsForBundleIdentifier:promptHandler:completion:"
- "handleObjectAuthorizationRequestsWithPromptHandler:completion:"
- "initForBundleIdentifier:sessionIdentifier:"
- "invalid Collection: less than 'count' elements in collection"
- "oxygen_saturation_phone_only"
- "readAuthorizationStatusForType:error:"
- "readAuthorizationStatusesForTypes:error:"
- "remoteDeviceSupportsUSLegallyCompliantOxygenSaturation"
- "remote_startWatchAppWithWorkoutPlanData:processIdentifier:completion:"
- "shardPredicatesForProfile:syncCircleName:currentDate:error:"
- "sharingIdentifier"
- "sharingPredicate"
- "startWatchAppWithWorkoutPlanData:processIdentifier:completion:"
- "syncStoreForProfile:storeIdentifier:syncCircleName:ownerIdentifier:syncIdentity:containerIdentifier:error:"
- "unprocessedBloodOxygenDataType"
- "v32@?0@\"HKObjectType\"8@\"HDReadAuthorizationStatus\"16^B24"
- "v36@0:8@\"NSData\"16i24@?<v@?B@\"NSError\">28"
- "v36@0:8@16i24@?28"
- "\xc1!"

```
