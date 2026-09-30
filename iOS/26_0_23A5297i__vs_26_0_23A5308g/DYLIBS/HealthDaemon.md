## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6100.0.0.0.0
-  __TEXT.__text: 0x77f768
+6105.0.0.0.0
+  __TEXT.__text: 0x782b20
   __TEXT.__auth_stubs: 0x4810
-  __TEXT.__objc_methlist: 0x42e54
+  __TEXT.__objc_methlist: 0x42f0c
   __TEXT.__const: 0x1d624
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x79267
+  __TEXT.__cstring: 0x798bf
   __TEXT.__constg_swiftt: 0x10c8
   __TEXT.__swift5_typeref: 0xc75
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_protos: 0x1c
   __TEXT.__swift5_capture: 0x4f4
-  __TEXT.__oslogstring: 0x418e9
+  __TEXT.__oslogstring: 0x41a35
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x60
-  __TEXT.__gcc_except_tab: 0x380b8
+  __TEXT.__gcc_except_tab: 0x38464
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x1c7b0
+  __TEXT.__unwind_info: 0x1c868
   __TEXT.__eh_frame: 0x2310
-  __TEXT.__objc_classname: 0xc4f4
-  __TEXT.__objc_methname: 0x8e229
-  __TEXT.__objc_methtype: 0x169a3
-  __TEXT.__objc_stubs: 0x50160
-  __DATA_CONST.__got: 0x55f0
-  __DATA_CONST.__const: 0x1d1f8
-  __DATA_CONST.__objc_classlist: 0x2900
+  __TEXT.__objc_classname: 0xc512
+  __TEXT.__objc_methname: 0x8e455
+  __TEXT.__objc_methtype: 0x16a85
+  __TEXT.__objc_stubs: 0x502c0
+  __DATA_CONST.__got: 0x5600
+  __DATA_CONST.__const: 0x1d2d8
+  __DATA_CONST.__objc_classlist: 0x2908
   __DATA_CONST.__objc_catlist: 0x4b8
   __DATA_CONST.__objc_protolist: 0x9b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19ce0
+  __DATA_CONST.__objc_selrefs: 0x19d28
   __DATA_CONST.__objc_protorefs: 0x1d8
-  __DATA_CONST.__objc_superrefs: 0x1d58
-  __DATA_CONST.__objc_arraydata: 0x8458
+  __DATA_CONST.__objc_superrefs: 0x1d60
+  __DATA_CONST.__objc_arraydata: 0x8478
   __AUTH_CONST.__auth_got: 0x2420
-  __AUTH_CONST.__const: 0xf830
-  __AUTH_CONST.__cfstring: 0x3cbc0
-  __AUTH_CONST.__objc_const: 0x7ca68
-  __AUTH_CONST.__objc_arrayobj: 0x1e78
+  __AUTH_CONST.__const: 0xf990
+  __AUTH_CONST.__cfstring: 0x3cd20
+  __AUTH_CONST.__objc_const: 0x7cbe0
+  __AUTH_CONST.__objc_arrayobj: 0x1e90
   __AUTH_CONST.__objc_intobj: 0x3e58
   __AUTH_CONST.__objc_doubleobj: 0x3c0
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0xc848
-  __AUTH.__data: 0x4e8
-  __DATA.__objc_ivar: 0x4360
+  __AUTH.__objc_data: 0xc470
+  __AUTH.__data: 0x4b8
+  __DATA.__objc_ivar: 0x4370
   __DATA.__data: 0x8170
   __DATA.__common: 0x64
-  __DATA.__bss: 0xcd8
-  __DATA_DIRTY.__objc_ivar: 0xe78
-  __DATA_DIRTY.__objc_data: 0xdba0
-  __DATA_DIRTY.__data: 0x170
-  __DATA_DIRTY.__bss: 0x3b8
+  __DATA.__bss: 0xcc8
+  __DATA_DIRTY.__objc_ivar: 0xe7c
+  __DATA_DIRTY.__objc_data: 0xdfc8
+  __DATA_DIRTY.__data: 0x1a0
+  __DATA_DIRTY.__bss: 0x3c8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit
   - /System/Library/Frameworks/AddressBook.framework/AddressBook

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3ABF5EFA-B8BC-392F-A51F-8377E1B7E4C4
-  Functions: 34237
-  Symbols:   103301
-  CStrings:  43921
+  UUID: F3F9A541-CB71-3D79-8AD3-308F8F102325
+  Functions: 34279
+  Symbols:   103411
+  CStrings:  43975
 
Symbols:
+ +[HDLocationSeriesSampleEntity insertLocationData:seriesIdentifier:assertion:profile:error:]
+ +[HDQuantitySampleValueEnumerator _enumerateWithEnumerator:endTime:error:sourceHandler:]
+ +[HDQuantitySampleValueEnumerator quantityValuesWithSourceForType:from:to:dataInterval:table:transaction:error:handler:]
+ +[HDWorkoutBuilderAssociatedObjectEntity associateObject:code:timestamp:withBuilder:transaction:error:]
+ -[HDCloudSyncManager dealloc]
+ -[HDDataManager insertDataObjects:sourceEntity:deviceEntity:sourceVersion:creationDate:timeZone:OSVersion:error:]
+ -[HDDataProvenanceManager localDataProvenanceForSourceEntity:version:deviceEntity:timzone:OSVersion:]
+ -[HDHealthStoreServer _queue_insertObjects:sourceEntity:sourceVersionOverride:shouldJournal:skipInsertionFilter:databaseAssertion:error:creationDate:]
+ -[HDHealthStoreServer _saveDataObjects:sourceEntity:sourceVersion:skipInsertionFilter:databaseAssertion:handler:creationDate:]
+ -[HDHealthStoreServer saveSamples:databaseAssertion:withCompletion:]
+ -[HDLocationDataCollector databaseAssertion]
+ -[HDMirroredWorkoutPendingData .cxx_destruct]
+ -[HDMirroredWorkoutPendingData completion]
+ -[HDMirroredWorkoutPendingData data]
+ -[HDMirroredWorkoutPendingData initWithData:completion:]
+ -[HDMirroredWorkoutPendingData setData:]
+ -[HDMirroredWorkoutSessionServer isFirstPartyClient]
+ -[HDWorkoutBuilderEntity _createTemporaryProtectedAssociatedSampleListInTransaction:error:]
+ -[HDWorkoutBuilderEntity associateObject:code:timestamp:transaction:error:]
+ -[HDWorkoutBuilderEntity enumerateAssociatedSampleValuesWithCustomQueryOfType:interval:profile:error:handler:]
+ -[HDWorkoutBuilderServer databaseAssertion]
+ -[HDWorkoutBuilderServer updateActivityWithUUID:addMedatata:dataSource:]
+ -[HDWorkoutLocationSmoother setUnitTest_didSmoothActivityForTask:]
+ -[HDWorkoutLocationSmoother unitTest_didSmoothActivityForTask]
+ _.str.292
+ _.str.296
+ _.str.302
+ _OBJC_CLASS_$_HDMirroredWorkoutPendingData
+ _OBJC_IVAR_$_HDLocationDataCollector._lock
+ _OBJC_IVAR_$_HDLocationDataCollector._lock_databaseAssertion
+ _OBJC_IVAR_$_HDMirroredWorkoutPendingData._completion
+ _OBJC_IVAR_$_HDMirroredWorkoutPendingData._data
+ _OBJC_IVAR_$_HDWorkoutLocationSmoother._unitTest_didSmoothActivityForTask
+ _OBJC_METACLASS_$_HDMirroredWorkoutPendingData
+ __HDAddWorkoutAssociatedObjectSampleTypeColumn
+ __OBJC_$_INSTANCE_METHODS_HDMirroredWorkoutPendingData
+ __OBJC_$_INSTANCE_VARIABLES_HDMirroredWorkoutPendingData
+ __OBJC_$_PROP_LIST_HDCloudSyncStatusProvider.435
+ __OBJC_$_PROP_LIST_HDMirroredWorkoutPendingData
+ __OBJC_CLASS_RO_$_HDMirroredWorkoutPendingData
+ __OBJC_METACLASS_RO_$_HDMirroredWorkoutPendingData
+ ___100+[HDDataTypeSourceOrderEntity _updateOrderedSourcesForType:profile:transaction:error:updateHandler:]_block_invoke.348
+ ___100+[HDDataTypeSourceOrderEntity _updateOrderedSourcesForType:profile:transaction:error:updateHandler:]_block_invoke_2.349
+ ___100-[HDStaticSyncImportTask _queue_importStaticSyncChangesFromDirectory:syncStore:progress:completion:]_block_invoke.467
+ ___101-[HDCloudSyncVerifyAttachmentManagementRecordOperation _modifyCloudKitAndFinishWithManagementRecord:]_block_invoke.299
+ ___102-[HDDaemonSyncEngine _performSyncTransactionForSession:store:anchorRangeMap:transactionContext:error:]_block_invoke.473
+ ___103+[HDWorkoutBuilderAssociatedObjectEntity associateObject:code:timestamp:withBuilder:transaction:error:]_block_invoke
+ ___103+[HDWorkoutBuilderAssociatedObjectEntity associateObject:code:timestamp:withBuilder:transaction:error:]_block_invoke_2
+ ___103-[HDCloudSyncSharedSummaryPushPrepareOperation _pendingAndAcceptedParticipantRecordsInZone:completion:]_block_invoke.299
+ ___103-[HDExtendedDatabaseTransaction initWithDatabase:context:transactionTimeout:continuationTimeout:error:]_block_invoke.319
+ ___103-[HDProtectedDataOperation _notifyDelegateToPerformWorkWithDatabase:accessibilityAssertion:completion:]_block_invoke.360
+ ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.302
+ ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.306
+ ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.314
+ ___104-[HDCloudSyncPullChangeRecordOperation _continuationForFetchedRecord:recordID:inMemoryAsset:fetchError:]_block_invoke.312
+ ___104-[HDCloudSyncPullChangeRecordOperation _continuationForFetchedRecord:recordID:inMemoryAsset:fetchError:]_block_invoke.313
+ ___105-[HDDatabaseValidationTaskServer remote_validateDatabase:clientCompletionHandler:errorHandlerIdentifier:]_block_invoke.293
+ ___105-[HDDatabaseValidationTaskServer remote_validateDatabase:clientCompletionHandler:errorHandlerIdentifier:]_block_invoke.295
+ ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.305
+ ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.313
+ ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.315
+ ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke_2.311
+ ___106-[HDActivitySummaryBuilder _enumerateActivitySummariesAndCachesWithPredicate:largestAnchor:error:handler:]_block_invoke.307
+ ___106-[HDBackgroundFeatureDeliveryManager periodicCountryMonitor:didFetchISOCountryCode:countryCodeProvenance:]_block_invoke.340
+ ___106-[HDCloudSyncPipelineStageSharedSummaryAddParticipant _addParticipantWithLookupInfo:ownerName:ownerEmail:]_block_invoke.324
+ ___106-[HDCloudSyncPipelineStageSharedSummaryAddParticipant _addParticipantWithLookupInfo:ownerName:ownerEmail:]_block_invoke_2.326
+ ___107-[HDAppSubscriptionManager _updateSubscriptionsBasedOnBARSwitchState:lastLaunchTimes:dataCode:anchor:type:]_block_invoke.320
+ ___107-[HDDemoDataFoodSampleGenerator generateObjectsForDemoPerson:fromTime:toTime:currentDate:objectCollection:]_block_invoke.370
+ ___107-[HDNanoSyncManager _queue_performNextProactiveSyncWithRemainingDevices:accessibilityAssertion:completion:]_block_invoke.714
+ ___108-[HDDatabaseValidationTaskServer remote_validateEntitiesWithClientCompletionHandler:errorHandlerIdentifier:]_block_invoke.297
+ ___108-[HDIngestDeviceKeyValueEntriesOperation _pullDeviceKeyValueEntriesForProfile:repository:transaction:error:]_block_invoke.300
+ ___109-[HDSecondaryDevicePairingAgentTaskServer remote_tearDownHealthSharingWithTinkerDeviceWithNRUUID:completion:]_block_invoke.338
+ ___110-[HDWorkoutBuilderEntity enumerateAssociatedSampleValuesWithCustomQueryOfType:interval:profile:error:handler:]_block_invoke
+ ___110-[HDWorkoutBuilderEntity enumerateAssociatedSampleValuesWithCustomQueryOfType:interval:profile:error:handler:]_block_invoke_2
+ ___110-[HDWorkoutEffortRelationshipQueryServer associationsUpdatedForObject:subObject:type:behavior:objects:anchor:]_block_invoke.316
+ ___111+[HDQuantitySampleValueEnumerator orderedQuantityValuesBySeriesForPredicate:transaction:options:error:handler:]_block_invoke.294
+ ___111-[HDWorkoutBuilderStatisticsDataSource collectionCalculator:queryForInterval:error:sampleHandler:mergeHandler:]_block_invoke_2
+ ___112-[HDDatabasePruningCoordinator _pruneProfilesWithIdentifiers:takeAccessibilityAssertion:shouldDefer:completion:]_block_invoke.316
+ ___113-[HDSeriesQuantityDataAggregator aggregateForState:collector:device:requestedAggregationDate:mode:options:error:]_block_invoke.313
+ ___113-[HDSeriesQuantityDataAggregator aggregateForState:collector:device:requestedAggregationDate:mode:options:error:]_block_invoke_2.314
+ ___115+[HDObjectAuthorizationEntity _setObjectAuthorizationRecords:syncProvenance:syncIdentity:skipErrors:profile:error:]_block_invoke.339
+ ___115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.445
+ ___115-[HDCloudSyncHandleMissingManateeIdentityOperation _deleteZonesForLostManateeIdentitiesInZones:container:database:]_block_invoke.309
+ ___115-[HDCloudSyncHandleMissingManateeIdentityOperation _leaveSharesForLostManateeIdentitiesInZones:container:database:]_block_invoke.314
+ ___116-[HDCloudSyncPushReferenceTombstonesOperation _generateTombstoneRecordsToPushAndReferencesRecordsToDeleteWithError:]_block_invoke.295
+ ___117+[HDLogicalSourceEntity lookUpOrCreateLogicalSourceWithBundleIdentifier:owningAppBundleIdentifier:transaction:error:]_block_invoke.349
+ ___117+[HDLogicalSourceEntity lookUpOrCreateLogicalSourceWithBundleIdentifier:owningAppBundleIdentifier:transaction:error:]_block_invoke_2.353
+ ___119-[HDInsertSharedSummaryTransactionOperation _persistRecordsWithRepository:transactionRecord:summaryRecords:completion:]_block_invoke.324
+ ___120+[HDQuantitySampleValueEnumerator quantityValuesWithSourceForType:from:to:dataInterval:table:transaction:error:handler:]_block_invoke
+ ___120+[HDQuantitySampleValueEnumerator quantityValuesWithSourceForType:from:to:dataInterval:table:transaction:error:handler:]_block_invoke_2
+ ___120-[HDCloudSyncSharedSummaryPushPruningOperation _findTransactionsToDelete:existingTransactionRecordsByZoneID:completion:]_block_invoke.300
+ ___122-[HDAuthorizationManager handleHealthConceptAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.468
+ ___122-[HDSharingAuthorizationRecipientStoreServer sharingAuthorizationManager:didAddSharingAuthorizations:recipientIdentifier:]_block_invoke.293
+ ___123-[HDDefaultAuthorizationSchemaProvider setAuthorizationStatuses:authorizationModes:bundleIdentifier:options:profile:error:]_block_invoke.314
+ ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.308
+ ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.310
+ ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.315
+ ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.317
+ ___123-[HDSecondaryDevicePairingAgentTaskServer remote_requestTinkerSharingOptInWithGuardianDisplayName:NRDeviceUUID:completion:]_block_invoke.299
+ ___125-[HDSharingAuthorizationRecipientStoreServer sharingAuthorizationManager:didRemoveSharingAuthorizations:recipientIdentifier:]_block_invoke.295
+ ___126-[HDHealthStoreServer _saveDataObjects:sourceEntity:sourceVersion:skipInsertionFilter:databaseAssertion:handler:creationDate:]_block_invoke
+ ___126-[HDHealthStoreServer _saveDataObjects:sourceEntity:sourceVersion:skipInsertionFilter:databaseAssertion:handler:creationDate:]_block_invoke_2
+ ___127-[HDClientAuthorizationOracle(Privileged) _queue_beginAuthorizationRequestDelegateTransactionWithSessionIdentifier:completion:]_block_invoke.498
+ ___130+[HDDeviceKeyValueStorageEntryEntity setData:forKey:domain:deviceContextID:syncEntityIdentity:modificationDate:transaction:error:]_block_invoke.346
+ ___133-[HDClientAuthorizationOracle enqueueAuthorizationRequestToWriteTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke.418
+ ___134-[HDAuthorizationManager _authorizationRequestStatusForClientBundleIdentifier:writeTypes:readTypes:updateAuthorizationStatuses:error:]_block_invoke.401
+ ___135-[HDNanoSyncManager _queue_synchronizeWithOptions:restoreMessagesSentHandler:targetSyncStore:reason:accessibilityAssertion:completion:]_block_invoke.506
+ ___135-[HDNanoSyncManager _queue_synchronizeWithOptions:restoreMessagesSentHandler:targetSyncStore:reason:accessibilityAssertion:completion:]_block_invoke.514
+ ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.342
+ ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.346
+ ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.347
+ ___150-[HDHealthStoreServer _queue_insertObjects:sourceEntity:sourceVersionOverride:shouldJournal:skipInsertionFilter:databaseAssertion:error:creationDate:]_block_invoke
+ ___150-[HDHealthStoreServer _queue_insertObjects:sourceEntity:sourceVersionOverride:shouldJournal:skipInsertionFilter:databaseAssertion:error:creationDate:]_block_invoke_2
+ ___150-[HDHealthStoreServer _queue_insertObjects:sourceEntity:sourceVersionOverride:shouldJournal:skipInsertionFilter:databaseAssertion:error:creationDate:]_block_invoke_3
+ ___150-[HDHealthStoreServer _queue_insertObjects:sourceEntity:sourceVersionOverride:shouldJournal:skipInsertionFilter:databaseAssertion:error:creationDate:]_block_invoke_4
+ ___151-[HDCloudSyncSharedSummaryParticipantProfileCreationOperation _createProfileWithUUID:contactIdentifier:firstName:lastName:ownerParticipant:completion:]_block_invoke.294
+ ___151-[HDCloudSyncSharedSummaryParticipantProfileCreationOperation _createProfileWithUUID:contactIdentifier:firstName:lastName:ownerParticipant:completion:]_block_invoke_2.295
+ ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke.301
+ ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke.307
+ ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke_2.304
+ ___162+[HDWorkoutZonesAssociationEntity _insertAssociationsForZonesSamplesWithUUIDs:withWorkoutUUID:syncProvenance:syncIdentity:ignoreDeletedObjects:transaction:error:]_block_invoke.335
+ ___185-[HDWorkoutTrainingLoadDataSource _queryEffortSampleValuesForWorkoutUUID:workoutPID:workoutStartDate:workoutEndDate:workoutActivityType:workoutDuration:sourceID:activity:sampleHandler:]_block_invoke.326
+ ___186-[HDCloudSyncSharedSummaryPushOperation createRecordsToSaveWithTransactions:transactionRecords:participantZoneID:participant:authorizationIdentifiers:allRecordsToSave:zoneIDs:taskGroup:]_block_invoke.311
+ ___191+[HDAssociationEntity _insertEntriesWithParentUUID:childUUIDsData:provenance:syncIdentity:type:behavior:deleted:creationDate:destinationSubObjectReference:lastInsertedEntityID:context:error:]_block_invoke.428
+ ___248+[HDDataProvenanceEntity insertOrLookupDataProvenanceForSyncProvenance:syncIdentity:originProductType:originSystemBuild:originOSVersion:localProductType:localSystemBuild:sourceVersion:timeZoneName:sourceID:deviceID:contributorID:transaction:error:]_block_invoke.397
+ ___32-[HDBiomeInterface sleepFocusOn]_block_invoke.298
+ ___35-[HDDeviceQueryServer _queue_start]_block_invoke.297
+ ___35-[HDDeviceQueryServer _queue_start]_block_invoke_2.308
+ ___36-[HDCacheDeleteCoordinator activate]_block_invoke.297
+ ___36-[HDCacheDeleteCoordinator activate]_block_invoke.299
+ ___36-[HDCloudSyncPipelineStagePush main]_block_invoke.304
+ ___37-[HDCloudSyncStateSyncOperation main]_block_invoke.301
+ ___38-[HDDaemon _setupMemoryWarningHandler]_block_invoke.465
+ ___39-[HDCloudSyncCreateZonesOperation main]_block_invoke.299
+ ___39-[HDIDSPersistentDictionary didCancel:]_block_invoke.427
+ ___40-[HDCloudSyncAcceptSharesOperation main]_block_invoke.298
+ ___40-[HDDataProvenanceManager _loadDefaults]_block_invoke.313
+ ___41-[HDCloudSyncPipeline beginWithTaskTree:]_block_invoke.382
+ ___41-[HDCloudSyncPipeline beginWithTaskTree:]_block_invoke.384
+ ___41-[HDCloudSyncPipelineStageStateSync main]_block_invoke.302
+ ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke.371
+ ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke_2.370
+ ___42-[HDCloudSyncDeleteSequenceOperation main]_block_invoke.298
+ ___42-[HDCloudSyncDeleteSequenceOperation main]_block_invoke.299
+ ___42-[HDCloudSyncLeaveAllSharesOperation main]_block_invoke.293
+ ___42-[HDCloudSyncPullReferencesOperation main]_block_invoke.298
+ ___42-[HDProfileManager _loadSecondaryProfiles]_block_invoke.333
+ ___43-[HDWorkoutBuilderServer _didUpdateEvents:]_block_invoke.616
+ ___44-[HDCloudSyncPullChangeRecordOperation main]_block_invoke.306
+ ___44-[HDStaticSyncExportTask runWithCompletion:]_block_invoke.319
+ ___45-[HDAppLauncher _queue_launchClientIfNeeded:]_block_invoke.302
+ ___45-[HDCloudSyncLookupParticipantOperation main]_block_invoke.298
+ ___45-[HDCloudSyncPrepareForSharingOperation main]_block_invoke.296
+ ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.298
+ ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.300
+ ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.306
+ ___45-[HDCloudSyncSharedSummaryPushOperation main]_block_invoke.293
+ ___45-[HDHFDataStore _lock_restoreHFDFromArchive:]_block_invoke.403
+ ___45-[HDWorkoutBuilderServer _didUpdateMetadata:]_block_invoke.606
+ ___45-[HDWorkoutRouteDataSource elevationUpdated:]_block_invoke.421
+ ___45-[HDWorkoutRouteDataSource elevationUpdated:]_block_invoke_3
+ ___46-[HDCloudSyncDeleteStoreOnChildOperation main]_block_invoke.295
+ ___46-[HDCloudSyncDisableSyncLocallyOperation main]_block_invoke.295
+ ___46-[HDCloudSyncPushDeviceKeyValueOperation main]_block_invoke.303
+ ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke.307
+ ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke.309
+ ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke_2.313
+ ___46-[HDCloudSyncStatusProvider checkLastSyncDate]_block_invoke.336
+ ___46-[HDDaemon registerDaemonReadyObserver:queue:]_block_invoke.476
+ ___46-[HDSyncIdentityManager profileDidInitialize:]_block_invoke.359
+ ___46-[HDWorkoutSessionServer didBeginNewActivity:]_block_invoke.625
+ ___46-[_HDAWDPeriodicAction _doIfWaitingWithError:]_block_invoke.347
+ ___47-[HDAgeGatingManager _registerForNotifications]_block_invoke.312
+ ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke.297
+ ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke.301
+ ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke_2.302
+ ___47-[HDCloudSyncPipelineStageContextSyncPush main]_block_invoke.303
+ ___47-[HDWorkoutBuilderServer _didUpdateStatistics:]_block_invoke.655
+ ___47-[HDWorkoutSessionServer _queue_generateError:]_block_invoke.711
+ ___47-[HDWorkoutSessionServer _queue_generateEvent:]_block_invoke.705
+ ___47-[HDWorkoutSessionServer _queue_generateEvent:]_block_invoke.708
+ ___48-[HDCloudSyncPipeline _queue_runStage:taskTree:]_block_invoke.399
+ ___48-[HDCloudSyncPipeline _queue_runStage:taskTree:]_block_invoke.401
+ ___48-[HDWorkoutSessionServer didEndCurrentActivity:]_block_invoke.631
+ ___48-[HDWorkoutSessionServer syncSessionEvent:date:]_block_invoke.675
+ ___49-[HDCloudSyncAddSharingParticipantOperation main]_block_invoke.312
+ ___49-[HDCloudSyncAddSharingParticipantOperation main]_block_invoke.313
+ ___49-[HDCloudSyncMarkAllOwnersDisabledOperation main]_block_invoke.296
+ ___49-[HDCloudSyncRegisterSubscriptionsOperation main]_block_invoke.296
+ ___49-[HDWorkoutSessionServer remoteSessionDidRecover]_block_invoke.676
+ ___50-[HDAppSubscriptionManager profileDidBecomeReady:]_block_invoke.315
+ ___50-[HDCloudSyncPipelineStageDisableSyncLocally main]_block_invoke.292
+ ___50-[HDDaemon registerDaemonActivatedObserver:queue:]_block_invoke.477
+ ___50-[HDDataCollectionManager _dataCollectorBlacklist]_block_invoke.417
+ ___51-[HDQueryManager _lock_executeDatabaseAccessBlocks]_block_invoke.314
+ ___52-[HDCloudSyncSharedSummaryPushPrepareOperation main]_block_invoke.292
+ ___52-[HDDemoDataManager _queue_generateDemoDataIfNeeded]_block_invoke.297
+ ___52-[HDLiveWorkoutDataSource addQuantities:dataSource:]_block_invoke.416
+ ___52-[HDLiveWorkoutDataSource addQuantities:dataSource:]_block_invoke_2.417
+ ___52-[HDSeriesBuilderServer _setClientState:completion:]_block_invoke.324
+ ___52-[HDWorkoutBasicDataSource setSampleTypesToCollect:]_block_invoke.416
+ ___52-[HDWorkoutLocationSmoother _queue_smoothNextSample]_block_invoke.392
+ ___53-[HDCloudSyncResetOperation _deleteZonesWithZoneIDs:]_block_invoke.293
+ ___54-[HDCloudSyncCachedZone recordsForClass:error:filter:]_block_invoke.334
+ ___54-[HDCloudSyncCachedZone recordsForClass:error:filter:]_block_invoke_2.335
+ ___54-[HDDataManager _addTransactionInsertionCommitBlocks:]_block_invoke.323
+ ___54-[HDPeriodicCountryMonitor _processCountryCodeResult:]_block_invoke.348
+ ___55-[HDCloudSyncCachedZone recordForRecordID:class:error:]_block_invoke.344
+ ___55-[HDCloudSyncCachedZone recordForRecordID:class:error:]_block_invoke_2.345
+ ___55-[HDCloudSyncManager _persistErrorRequiringUserAction:]_block_invoke.455
+ ___55-[HDFeatureAvailabilityManager registerObserver:queue:]_block_invoke.413
+ ___55-[HDQueryServer authorizedSamplesForClientWithSamples:]_block_invoke.381
+ ___55-[HDWorkoutBuilderServer remote_addSamples:completion:]_block_invoke.576
+ ___55-[HDWorkoutBuilderServer remote_recoverWithCompletion:]_block_invoke.605
+ ___55-[HDWorkoutLocationSmoother _deleteSamples:completion:]_block_invoke
+ ___55-[HDWorkoutSessionServer _queue_startInvalidationTimer]_block_invoke.722
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke.372
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_2.376
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_3.380
+ ___56-[HDWorkoutBuilderServer remote_addMetadata:completion:]_block_invoke.580
+ ___56-[HDWorkoutLocationSmoother _queue_deleteRoutesForTask:]_block_invoke
+ ___56-[HDWorkoutLocationSmoother _queue_deleteRoutesForTask:]_block_invoke_2
+ ___56-[HDWorkoutSessionTaskServer didEndActivity:dataSource:]_block_invoke.435
+ ___57-[HDAppExtensionAssertion assertAndUpdateWithCompletion:]_block_invoke.301
+ ___57-[HDAppExtensionAssertion assertAndUpdateWithCompletion:]_block_invoke.303
+ ___57-[HDWorkoutSessionServer endCurrentActivityOnDate:error:]_block_invoke.646
+ ___58-[HDCloudSyncDeleteZonesOperation _deleteZones:container:]_block_invoke.305
+ ___58-[HDCloudSyncDeleteZonesOperation _deleteZones:container:]_block_invoke.307
+ ___58-[HDCloudSyncRemoveInvalidShareParticipantsOperation main]_block_invoke.304
+ ___58-[HDNanoSyncManager _queue_generateWatchActivationSamples]_block_invoke.552
+ ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke.659
+ ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke_2.660
+ ___58-[HDWorkoutSessionTaskServer addWorkoutEvents:dataSource:]_block_invoke.432
+ ___58-[HDWorkoutSessionTaskServer didBeginActivity:dataSource:]_block_invoke.434
+ ___59+[HDConceptIndexer _indexSample:profile:transaction:error:]_block_invoke.395
+ ___59-[HDCloudSyncStatusProvider fetchSyncStatusWithCompletion:]_block_invoke.299
+ ___59-[HDCloudSyncStatusProvider fetchSyncStatusWithCompletion:]_block_invoke.301
+ ___59-[HDFakeDataCollector _lock_setupSwimmingGeneratorsAtTime:]_block_invoke.324
+ ___59-[HDWorkoutBuilderServer remote_removeMetadata:completion:]_block_invoke.585
+ ___59-[HDWorkoutSessionTaskServer remote_recoverWithCompletion:]_block_invoke.418
+ ___60+[HDSampleEntity dateIntervalsForSampleTypes:profile:error:]_block_invoke.397
+ ___60-[HDCloudSyncDeleteStoresOperation _individualZonesToDelete]_block_invoke.297
+ ___60-[HDCloudSyncSubscriptionNotificationHandler _enableAPSPush]_block_invoke.298
+ ___60-[HDMirroredWorkoutSessionServer setTargetState:date:error:]_block_invoke.338
+ ___60-[HDStatisticsCollectionQueryServer _queue_updateStatistics]_block_invoke.378
+ ___60-[HDSummarySharingEntryStoreServer sharingEntriesDidUpdate:]_block_invoke.298
+ ___61-[HDCloudSyncDetectSyncDisabledOperation _disableSyncLocally]_block_invoke.300
+ ___61-[HDCloudSyncManagerPipelineTask mainWithRepositories:error:]_block_invoke.304
+ ___61-[HDDatabase _mergeSecondaryJournalsWithActivity:completion:]_block_invoke.576
+ ___61-[HDDatabaseMigrator(Tigris) _updateOriginVersionsWithError:]_block_invoke.423
+ ___61-[HDWorkoutBuilderServer remote_addWorkoutEvents:completion:]_block_invoke.578
+ ___61-[HDWorkoutSessionServer _queue_generateConfigurationUpdate:]_block_invoke.712
+ ___62-[HDCloudSyncSharedSummarySynchronizeCloudStateOperation main]_block_invoke.298
+ ___62-[HDUserCharacteristicsManager _queue_updateHasWatchOnAccount]_block_invoke.367
+ ___62-[HDWorkoutSessionServer _processTargetStoppingStateWithDate:]_block_invoke.587
+ ___63-[HDHealthStoreServer remote_deleteClientSourceWithCompletion:]_block_invoke.466
+ ___63-[HDStatisticsCollectionQueryServer _queue_useCachedStatistics]_block_invoke.408
+ ___63-[HDWorkoutBuilderServer remote_addWorkoutActivity:completion:]_block_invoke.594
+ ___63-[HDWorkoutSessionTaskServer didDisconnectFromRemoteWithError:]_block_invoke.439
+ ___64-[CMPedometer(HealthDaemon) hd_beginStreamingFromDatum:handler:]_block_invoke.383
+ ___64-[CMPedometer(HealthDaemon) hd_beginStreamingFromDatum:handler:]_block_invoke.385
+ ___64-[HDCloudSyncComputePullTargetsOperation _pullTargetsWithError:]_block_invoke.301
+ ___64-[HDCloudSyncManager cloudSyncRepositoriesForClient:completion:]_block_invoke.426
+ ___64-[HDCloudSyncModifyRecordsOperation _saveRecords:deleteRecords:]_block_invoke.315
+ ___64-[HDFeatureAvailabilityManager _triggerImmediateSyncWithReason:]_block_invoke.412
+ ___64-[HDNanoSyncManager _queue_receiveTinkerOptInRequest:syncStore:]_block_invoke.821
+ ___64-[HDNanoSyncManager _scheduleResetReceivedNanoSyncAnchorsForHFD]_block_invoke.929
+ ___64-[HDNotificationManager postNotificationWithRequest:completion:]_block_invoke.324
+ ___64-[HDPeriodicCountryMonitor _fetchCountryIfNeededWithCompletion:]_block_invoke.332
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.544
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.552
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.553
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.562
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.563
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.548
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.554
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.551
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.555
+ ___64-[HDWorkoutSessionTaskServer _fetchOrSetupServerWithCompletion:]_block_invoke.451
+ ___65-[HDCloudSyncCoordinator resetAllProfilesWithContext:completion:]_block_invoke.401
+ ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.311
+ ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.313
+ ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.318
+ ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.327
+ ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke_2.320
+ ___65-[HDDatabaseCorruptionTTRPrompter _popAlertWithRadarDescription:]_block_invoke.324
+ ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.329
+ ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.330
+ ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke_2.331
+ ___65-[HDSourceOrderManager updateOrderedSources:forObjectType:error:]_block_invoke.309
+ ___65-[HDSyncIdentityManager rollCurrentSyncIdentityWithReason:error:]_block_invoke.353
+ ___65-[HDWorkoutSessionRapportSyncController _sendPendingTransactions]_block_invoke.362
+ ___66+[HDWorkoutCondenser _condenseWorkout:entity:configuration:error:]_block_invoke.344
+ ___66-[HDClientDataCollectionTaskServer remote_registerWithCompletion:]_block_invoke.312
+ ___66-[HDCloudSyncPullReferencesOperation _fetchAttachmentRecordAssets]_block_invoke.308
+ ___66-[HDCloudSyncPullReferencesOperation _fetchAttachmentRecordAssets]_block_invoke.310
+ ___66-[HDCloudSyncStateSyncOperation _pushUpdatedStateRecordsForZones:]_block_invoke.325
+ ___66-[HDCoreMotionDataCollector _queue_forwardCoreMotionData:forType:]_block_invoke.309
+ ___66-[HDCoreMotionDataCollector _queue_forwardCoreMotionData:forType:]_block_invoke.311
+ ___66-[HDHealthStoreServer _holdActiveClientTransactionWithCompletion:]_block_invoke.489
+ ___66-[HDMedicalIDDataManager _triggerSyncForSuccessfulMedicalIDUpdate]_block_invoke.329
+ ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.912
+ ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.914
+ ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke_2.916
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.848
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.866
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.871
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.873
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.875
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.877
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.879
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.881
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.876
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.878
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.880
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.882
+ ___66-[HDWorkoutBuilderSampleQueryServer _queue_performHistoricalQuery]_block_invoke.309
+ ___67-[HDCloudSyncAcceptSharesOperation _acceptSharesWithShareMetadata:]_block_invoke.306
+ ___67-[HDMirroredWorkoutSessionServer didDisconnectFromRemoteWithError:]_block_invoke.324
+ ___68-[HDHealthStoreServer remote_setCharacteristic:forDataType:handler:]_block_invoke.474
+ ___68-[HDLocationSeriesSampleEntity freezeWithTransaction:profile:error:]_block_invoke.338
+ ___68-[HDLocationSeriesSampleEntity freezeWithTransaction:profile:error:]_block_invoke.340
+ ___68-[HDNanoSyncManager _queue_recieveStartWorkoutAppRequest:syncStore:]_block_invoke.796
+ ___68-[HDProcessStateManager _lock_registerObserver:forBundleIdentifier:]_block_invoke.310
+ ___68-[HDWorkoutManager recoverAllActiveWorkoutSessionServersWithStates:]_block_invoke.390
+ ___68-[HDWorkoutSessionTaskServer updateWorkoutConfiguration:dataSource:]_block_invoke.433
+ ___69-[HDCloudSyncStateSyncOperation _performStateSyncInZones:completion:]_block_invoke.313
+ ___69-[HDDaemon obliterateAndTerminateProfiles:options:reason:completion:]_block_invoke.364
+ ___70-[HDCloudSyncManager _queue_considerStartingBackstopSyncForThreshold:]_block_invoke.459
+ ___70-[HDDemoDataGenerator _insertIntoDatabaseObjectCollection:fromPerson:]_block_invoke.392
+ ___70-[HDNanoSyncManager _queue_receiveChangeRequest:syncStore:completion:]_block_invoke.671
+ ___70-[HDSummarySharingEntryIDSManager leaveInvitationWithUUID:completion:]_block_invoke.372
+ ___71-[HDBackgroundObservationServerExtension connectWithCompletionHandler:]_block_invoke.312
+ ___71-[HDCloudSyncCoordinator _queue_syncAllProfilesWithContext:completion:]_block_invoke.378
+ ___71-[HDCloudSyncCoordinator _queue_syncAllProfilesWithContext:completion:]_block_invoke_2.379
+ ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.365
+ ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.366
+ ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.367
+ ___71-[HDSummarySharingEntryIDSManager revokeInvitationWithUUID:completion:]_block_invoke.370
+ ___71-[HDSummarySharingEntryIDSManager revokeInvitationWithUUID:completion:]_block_invoke.371
+ ___71-[HDWorkoutSessionServer stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.664
+ ___72-[HDCloudSyncAccountProvider disableAndDeleteAllSyncDataWithCompletion:]_block_invoke.306
+ ___72-[HDCloudSyncAccountProvider disableAndDeleteAllSyncDataWithCompletion:]_block_invoke.308
+ ___72-[HDCloudSyncCachedZone recordsForClass:epoch:error:enumerationHandler:]_block_invoke.329
+ ___72-[HDCloudSyncCachedZone recordsForClass:epoch:error:enumerationHandler:]_block_invoke_2.330
+ ___72-[HDCloudSyncDeleteStoresOperation _deleteUnifiedZoneStoresInContainer:]_block_invoke.315
+ ___72-[HDCloudSyncDeleteStoresOperation _deleteUnifiedZoneStoresInContainer:]_block_invoke.322
+ ___72-[HDCloudSyncPipeline _queue_waitForCloudKitOperationDelayWithTaskTree:]_block_invoke.406
+ ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.418
+ ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.421
+ ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.422
+ ___72-[HDMirroredWorkoutSessionServer syncTransitionToState:date:completion:]_block_invoke.328
+ ___72-[HDStatisticsCollectionQueryServer _queue_fetchAndDeliverAllStatistics]_block_invoke.395
+ ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.400
+ ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.401
+ ___73-[HDCloudSyncAccountProvider _performSyncForAccountChangeWithCompletion:]_block_invoke.337
+ ___73-[HDCloudSyncPeriodicActivityScheduler performInitialRestore:completion:]_block_invoke.322
+ ___73-[HDCloudSyncPushReferencesOperation _pushToCloudKitAndFinishForRecords:]_block_invoke.308
+ ___73-[HDCoreMotionDataCollector _queue_beginUpdatesWithTargetCollectionType:]_block_invoke.320
+ ___73-[HDNanoSyncManager _syncQueue_prepareForCompanionChangeWithStore:error:]_block_invoke.596
+ ___73-[HDWorkoutMirroringManager recoverMirroredWorkoutSessionWithCompletion:]_block_invoke.337
+ ___73-[HDWorkoutMirroringManager recoverMirroredWorkoutSessionWithCompletion:]_block_invoke.338
+ ___74+[HDSeriesSampleEntity freezeSeriesWithIdentifier:metadata:profile:error:]_block_invoke.330
+ ___74-[HDAnalyticsSubmissionCoordinator _locked_sendDailyAnalyticsWithTimeout:]_block_invoke.336
+ ___74-[HDAnalyticsSubmissionCoordinator _locked_sendDailyAnalyticsWithTimeout:]_block_invoke_2.338
+ ___74-[HDDataAggregator requestAggregationThroughDate:mode:options:completion:]_block_invoke.299
+ ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.306
+ ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.310
+ ___74-[HDWorkoutBuilderServer _lock_recoverPersistedDataWithTransaction:error:]_block_invoke.509
+ ___75-[HDCloudSyncObserverTaskServer _queue_instantiateCloudSyncObserverStatus:]_block_invoke.359
+ ___75-[HDCloudSyncObserverTaskServer _queue_instantiateCloudSyncObserverStatus:]_block_invoke_2.360
+ ___75-[HDCloudSyncUpdateCachedZonesOperation fetchChangesForContainer:database:]_block_invoke.299
+ ___75-[HDCoreMotionDataCollector _didReceiveCoreMotionData:startingDatum:error:]_block_invoke.315
+ ___75-[HDCurrentActivitySummaryHelper _handleSignificantTimeChangeNotification:]_block_invoke.310
+ ___75-[HDWorkoutBasicDataSource workoutSession:didChangeToState:fromState:date:]_block_invoke.439
+ ___75-[HDWorkoutBuilderServer remote_updateActivityWithUUID:endDate:completion:]_block_invoke.602
+ ___76-[HDActiveDataAggregator dataCollector:didCollectSensorData:device:options:]_block_invoke.315
+ ___76-[HDNanoSyncManager _queue_receiveTinkerEndToEndCloudSyncRequest:syncStore:]_block_invoke.895
+ ___76-[HDWorkoutSessionServer didReceiveDataFromRemoteWorkoutSession:completion:]_block_invoke.671
+ ___77+[HDDataEntity insertDataObjects:insertionContext:profile:completionHandler:]_block_invoke.455
+ ___77-[HDDeleteAttachmentReferenceOperation performWithProfile:transaction:error:]_block_invoke.300
+ ___78+[HDDeletedSampleEntity insertCodableDeletedSamples:provenance:profile:error:]_block_invoke.367
+ ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.433
+ ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.438
+ ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.439
+ ___78-[HDCloudSyncRemoveSharingParticipantsOperation _saveUpdatedShares:container:]_block_invoke.299
+ ___78-[HDCloudSyncSeizeAbandonedStoresOperation _markPendingOwnerForSeizureTargets]_block_invoke.314
+ ___78-[HDDatabaseMigrator(Monarch) _fixProvenancesWithZeroSourceOrDeviceWithError:]_block_invoke.617
+ ___78-[HDDatabaseMigrator(Monarch) _fixProvenancesWithZeroSourceOrDeviceWithError:]_block_invoke_2.618
+ ___78-[HDNanoSyncManager _queue_recieveCompanionUserNotificationRequest:syncStore:]_block_invoke.807
+ ___79-[HDCloudSyncManager configureForShareSetupMetadata:acceptedShares:completion:]_block_invoke.467
+ ___79-[HDCloudSyncManager configureForShareSetupMetadata:acceptedShares:completion:]_block_invoke.474
+ ___79-[HDCloudSyncRepairRegistryRecordsOperation _modifyRecordsAndFinish:container:]_block_invoke.298
+ ___79-[HDDatabaseTransaction performWithContext:error:block:inaccessibilityHandler:]_block_invoke.322
+ ___79-[HDPostInstallUpdateManager _triggerMigrationForProfile:protected:completion:]_block_invoke.318
+ ___79-[HDWorkoutBuilderServer remote_updateActivityWithUUID:addMetadata:completion:]_block_invoke.604
+ ___79-[HDWorkoutClusterServer remote_generateRaceRouteClustersWithLimit:completion:]_block_invoke.301
+ ___80-[HDCloudSyncCoordinator _queue_syncProfilesWithIdentifiers:context:completion:]_block_invoke.383
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke.314
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke.335
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_2.315
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_2.338
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_3.325
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_4.329
+ ___80-[HDSecondaryDevicePairingAgentTaskServer _prepareGuardianForSharingForRequest:]_block_invoke.354
+ ___80-[HDWorkoutSessionServer beginNewActivityWithConfiguration:date:metadata:error:]_block_invoke.645
+ ___81-[HDDatabaseMigrator(Emet) _emet_migrateWorkoutEventMetadataToProtobufWithError:]_block_invoke.321
+ ___81-[HDHealthStoreServer remote_setBackgroundDeliveryFrequency:forDataType:handler:]_block_invoke.453
+ ___81-[HDWorkoutSessionRapportSyncController sendRequest:transaction:responseHandler:]_block_invoke.354
+ ___82-[HDCloudSyncManager _primaryContainerIdentifiersForCurrentAccountWithCompletion:]_block_invoke.444
+ ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.542
+ ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.544
+ ___82-[HDDatabase _old_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.547
+ ___82-[HDWorkoutSessionServer enableAutomaticDetectionForActivityConfigurations:error:]_block_invoke.648
+ ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.598
+ ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.606
+ ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.609
+ ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.610
+ ___83-[HDCloudSyncManager _scheduleResetReceivedCloudSyncAnchorsAndRebaseForHFDRecovery]_block_invoke.367
+ ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke.337
+ ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke_2.340
+ ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke_3.342
+ ___83-[HDDeviceKeyValueStoreManager _deleteRemoteEntries:deviceContextByIdentity:error:]_block_invoke.318
+ ___83-[HDWorkoutBuilderServer _addSamples:quantities:dataSource:shouldSavePriorToStart:]_block_invoke.522
+ ___83-[HDWorkoutBuilderServer _addSamples:quantities:dataSource:shouldSavePriorToStart:]_block_invoke_2.524
+ ___84-[HDCloudSyncPreparePushZoneForStoreOperation _createZoneWithIdentifier:forStoreId:]_block_invoke.308
+ ___84-[HDWorkoutLocationSmoother _queue_smoothActivity:activityIndex:forTask:completion:]_block_invoke.399
+ ___84-[HDWorkoutLocationSmoother _queue_smoothActivity:activityIndex:forTask:completion:]_block_invoke.400
+ ___85-[HDWorkoutMirroringManager rapportMessenger:didReceiveRequest:data:responseHandler:]_block_invoke.314
+ ___86-[HDCloudSyncMedicalIDPushOperation _pushMedicalIDRecordToCloudForContainer:database:]_block_invoke.299
+ ___87-[HDCloudSyncFetchRecordsOperation _fetchRecordsWithIDs:container:database:completion:]_block_invoke.298
+ ___87-[HDCloudSyncPushDeviceKeyValueOperation _computeRecordsToSaveAndDeleteWithCompletion:]_block_invoke.309
+ ___87-[HDDataCollectionManager _requestAggregationThroughDate:type:mode:options:completion:]_block_invoke.371
+ ___87-[HDHealthStoreServer remote_requestConceptReadAuthorizationForType:filter:completion:]_block_invoke.369
+ ___87-[HDInsertSharedSummaryTransactionOperation performWithProfile:transaction:completion:]_block_invoke.294
+ ___87-[HDWorkoutEventsManager requestPendingEventsThroughDate:sessionIdentifier:completion:]_block_invoke.307
+ ___87-[HDWorkoutEventsManager requestPendingEventsThroughDate:sessionIdentifier:completion:]_block_invoke.309
+ ___88+[HDQuantitySampleValueEnumerator _enumerateWithEnumerator:endTime:error:sourceHandler:]_block_invoke
+ ___88-[HDCloudSyncPushDeviceContextOperation _updateRecordsAdd:recordIDsToDelete:completion:]_block_invoke.313
+ ___88-[HDDataCollectionManager _requestAggregationThroughDate:types:mode:options:completion:]_block_invoke.370
+ ___88-[HDWorkoutSessionTaskServer remote_recoverAllActiveSessionsWithStates:date:completion:]_block_invoke.420
+ ___88-[HDWorkoutSessionTaskServer remote_recoverAllActiveSessionsWithStates:date:completion:]_block_invoke.421
+ ___89+[HDUserDomainConceptSyncEntity receiveSyncObjects:version:syncProvenance:profile:error:]_block_invoke.305
+ ___89-[HDCloudSyncComputePushTargetsOperation _pushTargetsForContainer:ownerIdentifier:error:]_block_invoke.311
+ ___89-[HDHealthStoreServer remote_fetchModificationDateForCharacteristicWithDataType:handler:]_block_invoke.475
+ ___89-[HDHealthStoreServer remote_requestPerObjectReadAuthorizationForType:filter:completion:]_block_invoke.362
+ ___89-[HDHealthStoreServer remote_requestPerObjectReadAuthorizationForType:filter:completion:]_block_invoke.364
+ ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.573
+ ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.574
+ ___90+[HDLocationSeriesHFDMigrationEntity _migrateSeriesWithKey:toSQLFromStore:database:error:]_block_invoke.314
+ ___90+[HDQuantitySeriesHFDMigrationEntity _migrateSeriesWithKey:toSQLFromStore:database:error:]_block_invoke.301
+ ___90+[HDRaceRouteLocationSeriesEntity createRoutePointsFromWorkout:transaction:profile:error:]_block_invoke.325
+ ___90+[HDRaceRouteLocationSeriesEntity createRoutePointsFromWorkout:transaction:profile:error:]_block_invoke_2.327
+ ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.347
+ ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.348
+ ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.352
+ ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.356
+ ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke_2.353
+ ___90-[HDCloudSyncObserverTaskServer remote_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.339
+ ___90-[HDCloudSyncPullChangeRecordOperation _persistFetchedArchiveAsset:protocolVersion:error:]_block_invoke.335
+ ___90-[HDCloudSyncPullChangeRecordOperation _persistFetchedArchiveAsset:protocolVersion:error:]_block_invoke.337
+ ___90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.367
+ ___90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.369
+ ___90-[HDCloudSyncSharedSummaryPushPruningOperation _modifyRecordsAndFinish:recordIDsToDelete:]_block_invoke.309
+ ___90-[HDDataAggregator persistForCollector:usedDatums:source:device:error:persistenceHandler:]_block_invoke.324
+ ___91-[HDWorkoutBuilderEntity _createTemporaryProtectedAssociatedSampleListInTransaction:error:]_block_invoke_4
+ ___92+[HDLocationSeriesSampleEntity insertLocationData:seriesIdentifier:assertion:profile:error:]_block_invoke
+ ___92+[HDLocationSeriesSampleEntity insertLocationData:seriesIdentifier:assertion:profile:error:]_block_invoke.310
+ ___92-[HDBatchedQueryServer batchObjectsWithEnumerator:includeDeletedObjects:error:batchHandler:]_block_invoke.297
+ ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke.347
+ ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke.348
+ ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke_2.349
+ ___92-[HDCloudSyncCoordinator(CloudSyncJournalMerge) _mergeCloudSyncJournalsForProfile:taskTree:]_block_invoke.301
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.305
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.307
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.313
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.317
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.318
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke_2.309
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke_2.315
+ ___92-[HDWorkoutBuilderEntity _simplerSetupForEnumerationOfTypes:interval:profile:error:handler:]_block_invoke
+ ___93+[HDMedicationDoseEventEntity _logPersistedDoseEventOnCommitDatabase:doseEvent:persistentID:]_block_invoke.387
+ ___93-[HDAppSubscriptionManager _updateObservationStatusForDataTypeCode:lastAppLaunchTimes:error:]_block_invoke.342
+ ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke.302
+ ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke_2.304
+ ___94-[HDIngestDeviceContextsOperation _pullDeviceContextsForProfile:repository:transaction:error:]_block_invoke.299
+ ___94-[HDRestorableAlarmScheduler _queue_notifyClientsOfDueEventsAndScheduleNextFireDateWithError:]_block_invoke.325
+ ___94-[HDWorkoutBasicDataSource _workoutDataDestination:requestsSamplesOfType:from:to:transaction:]_block_invoke.431
+ ___94-[HDWorkoutManager generatePauseOrResumeRequestAllowingBackgroundRuntime:metadata:completion:]_block_invoke.371
+ ___95+[HDAppSubscriptionAppLaunchEntity insertOrUpdateAppSDKVersionToken:forBundleID:profile:error:]_block_invoke.385
+ ___95-[HDCloudSyncPushReferenceTombstonesOperation _modifyCloudWithRecordsToSave:recordIDsToDelete:]_block_invoke.309
+ ___95-[HDDatabaseJournal _mergeJournalChapter:profile:accessibilityAssertion:shouldContinueHandler:]_block_invoke.365
+ ___95-[HDQueryControlServer queryServer:requestsAuthorizationWithContext:promptIfNeeded:completion:]_block_invoke.308
+ ___95-[HDWorkoutBuilderEntity _fasterSetupForEnumerationOfTypes:interval:transaction:error:handler:]_block_invoke
+ ___96-[HDTTRPromptController _presentTTRPromptForErrors:lastPromptBuild:lastPromptDate:currentBuild:]_block_invoke.362
+ ___97+[HDLogicalSourceOrderEntity updateOrderedLogicalSourcesForType:transaction:error:updateHandler:]_block_invoke.351
+ ___97+[HDLogicalSourceOrderEntity updateOrderedLogicalSourcesForType:transaction:error:updateHandler:]_block_invoke_2.352
+ ___97-[HDBackgroundObservationServerExtension notifyExtensionOfUpdateForSampleType:completionHandler:]_block_invoke.317
+ ___97-[HDHealthStoreServer remote_requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.374
+ ___97-[HDSecondaryDevicePairingAgentTaskServer _setupTinkerProfileForRequest:metadata:acceptedShares:]_block_invoke.362
+ ___Block_byref_object_copy_.313
+ ___Block_byref_object_copy_.319
+ ___Block_byref_object_copy_.323
+ ___Block_byref_object_copy_.328
+ ___Block_byref_object_copy_.330
+ ___Block_byref_object_copy_.370
+ ___Block_byref_object_dispose_.314
+ ___Block_byref_object_dispose_.320
+ ___Block_byref_object_dispose_.324
+ ___Block_byref_object_dispose_.329
+ ___Block_byref_object_dispose_.331
+ ___Block_byref_object_dispose_.371
+ ____HDAddUniquenessChecksumToOriginalFHIRResourceEntity_block_invoke.1340
+ ____HDCopyWorkoutTotalsToPrimaryActivity_block_invoke.602
+ ____HDMigrateCycleTrackingOnboarding_block_invoke.966
+ ____HDMigrateCycleTrackingOnboarding_block_invoke_2.967
+ ____HDUpdateClinicalRecordEntities_block_invoke.892
+ ____HDUpdateClinicalRecordEntities_block_invoke_2.893
+ ____HDUpdateClinicalRecordEntities_block_invoke_3.897
+ ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke.978
+ ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke.982
+ ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke_2.983
+ ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke_3.987
+ ____ZL27_HDHFDataStoreWillOpenStoreP13HDHFDataStore_block_invoke.488
+ ___block_descriptor_40_e8_32r_e31_v32?0"HKWorkoutRoute"8Q16^B24lr32l8
+ ___block_descriptor_40_ea8_32bs_e27_B64?0q8d16d24d32q40q48^56ls32l8
+ ___block_descriptor_48_e8_32s40bs_e24_B52?0d8d16d24q32B40^44ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e30_B68?0d8d16d24d32d40q48B56^60ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e14_v32?0q8q16d24lr40l8s32l8
+ ___block_descriptor_48_ea8_32s40s_e33_B32?0"NSArray"8"NSArray"16^24ls32l8s40l8
+ ___block_descriptor_56_ea8_32bs40r48r_e23_B32?0"NSUUID"8q16^24lr40l8r48l8s32l8
+ ___block_descriptor_56_ea8_32s40s48bs_e9_B16?0^8ls48l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56bs_e48_B32?0"HDDatabaseTransaction"8"NSString"16^24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_ea8_32s40s48s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80r88r_e72_B32?0"HDStatisticsCollectionCalculator"8"HKQuantityType"16"NSUUID"24ls32l8s40l8s48l8r80l8s56l8r88l8s64l8s72l8
+ ___block_literal_global.1002
+ ___block_literal_global.1011
+ ___block_literal_global.1020
+ ___block_literal_global.1043
+ ___block_literal_global.1058
+ ___block_literal_global.1066
+ ___block_literal_global.1075
+ ___block_literal_global.1084
+ ___block_literal_global.1107
+ ___block_literal_global.1130
+ ___block_literal_global.1139
+ ___block_literal_global.1148
+ ___block_literal_global.296
+ ___block_literal_global.304
+ ___block_literal_global.320
+ ___block_literal_global.334
+ ___block_literal_global.338
+ ___block_literal_global.340
+ ___block_literal_global.344
+ ___block_literal_global.346
+ ___block_literal_global.352
+ ___block_literal_global.357
+ ___block_literal_global.371
+ ___block_literal_global.377
+ ___block_literal_global.382
+ ___block_literal_global.395
+ ___block_literal_global.400
+ ___block_literal_global.401
+ ___block_literal_global.402
+ ___block_literal_global.407
+ ___block_literal_global.413
+ ___block_literal_global.420
+ ___block_literal_global.428
+ ___block_literal_global.429
+ ___block_literal_global.433
+ ___block_literal_global.435
+ ___block_literal_global.437
+ ___block_literal_global.439
+ ___block_literal_global.441
+ ___block_literal_global.443
+ ___block_literal_global.452
+ ___block_literal_global.465
+ ___block_literal_global.467
+ ___block_literal_global.469
+ ___block_literal_global.480
+ ___block_literal_global.481
+ ___block_literal_global.482
+ ___block_literal_global.496
+ ___block_literal_global.500
+ ___block_literal_global.505
+ ___block_literal_global.515
+ ___block_literal_global.520
+ ___block_literal_global.530
+ ___block_literal_global.549
+ ___block_literal_global.550
+ ___block_literal_global.556
+ ___block_literal_global.562
+ ___block_literal_global.565
+ ___block_literal_global.567
+ ___block_literal_global.572
+ ___block_literal_global.574
+ ___block_literal_global.576
+ ___block_literal_global.585
+ ___block_literal_global.589
+ ___block_literal_global.591
+ ___block_literal_global.599
+ ___block_literal_global.600
+ ___block_literal_global.608
+ ___block_literal_global.612
+ ___block_literal_global.614
+ ___block_literal_global.616
+ ___block_literal_global.618
+ ___block_literal_global.620
+ ___block_literal_global.624
+ ___block_literal_global.631
+ ___block_literal_global.635
+ ___block_literal_global.636
+ ___block_literal_global.640
+ ___block_literal_global.642
+ ___block_literal_global.649
+ ___block_literal_global.653
+ ___block_literal_global.672
+ ___block_literal_global.678
+ ___block_literal_global.679
+ ___block_literal_global.681
+ ___block_literal_global.695
+ ___block_literal_global.697
+ ___block_literal_global.711
+ ___block_literal_global.713
+ ___block_literal_global.714
+ ___block_literal_global.717
+ ___block_literal_global.725
+ ___block_literal_global.727
+ ___block_literal_global.736
+ ___block_literal_global.742
+ ___block_literal_global.759
+ ___block_literal_global.771
+ ___block_literal_global.777
+ ___block_literal_global.793
+ ___block_literal_global.805
+ ___block_literal_global.809
+ ___block_literal_global.818
+ ___block_literal_global.827
+ ___block_literal_global.851
+ ___block_literal_global.874
+ ___block_literal_global.883
+ ___block_literal_global.892
+ ___block_literal_global.915
+ ___block_literal_global.916
+ ___block_literal_global.931
+ ___block_literal_global.938
+ ___block_literal_global.947
+ ___block_literal_global.956
+ ___block_literal_global.979
+ ___swift_assignWithCopy_strong
+ ___swift_assignWithTake_strong
+ ___swift_destroy_strong
+ ___swift_initWithCopy_strong
+ ___swift_memcpy8_8
+ ___unnamed_20
+ ___unnamed_27
+ ___unnamed_28
+ __insertStatementKey.key.495
+ _associateObject:code:timestamp:withBuilder:transaction:error:.insertKey
+ _columnDefinitionsWithCount:.HDDeviceKeyValueStorageEntryEntityColumnDefinitions.384
+ _columnDefinitionsWithCount:.columnDefinitions.396
+ _kHKSessionTrackerAppPreferencesDomain
+ _kHKWorkoutMirroringSetting
+ _objc_msgSend$associateObject:code:timestamp:transaction:error:
+ _objc_msgSend$associateObject:code:timestamp:withBuilder:transaction:error:
+ _objc_msgSend$completion
+ _objc_msgSend$enumerateAssociatedSampleValuesWithCustomQueryOfType:interval:profile:error:handler:
+ _objc_msgSend$initWithData:completion:
+ _objc_msgSend$insertDataObjects:sourceEntity:deviceEntity:sourceVersion:creationDate:timeZone:OSVersion:error:
+ _objc_msgSend$insertLocationData:seriesIdentifier:assertion:profile:error:
+ _objc_msgSend$isFirstPartyClient
+ _objc_msgSend$localDataProvenanceForSourceEntity:version:deviceEntity:timzone:OSVersion:
+ _objc_msgSend$quantityValuesWithSourceForType:from:to:dataInterval:table:transaction:error:handler:
+ _objc_msgSend$saveSamples:databaseAssertion:withCompletion:
+ _objc_msgSend$shouldBypassAuthorization
+ _objc_msgSend$unitTest_didSmoothActivityForTask
+ _objc_msgSend$updateActivityWithUUID:addMedatata:dataSource:
+ _objc_msgSend$workoutSavingQueryPerf
+ _objc_msgSend$workoutTempTableChanges
- +[HDLocationSeriesSampleEntity insertLocationData:seriesIdentifier:profile:error:]
- +[HDWorkoutBuilderAssociatedObjectEntity associateObject:timestamp:withBuilder:transaction:error:]
- -[HDDefaultWorkoutSessionController _queue_updateDataObservers]
- -[HDHealthStoreServer _queue_insertObjects:sourceEntity:sourceVersionOverride:shouldJournal:skipInsertionFilter:error:creationDate:]
- -[HDHealthStoreServer _saveDataObjects:sourceEntity:sourceVersion:skipInsertionFilter:handler:creationDate:]
- -[HDHealthStoreServer saveSamples:withCompletion:]
- -[HDWorkoutBuilderEntity associateObject:timestamp:transaction:error:]
- -[HDWorkoutLocationSmoother setUnitTest_didSmoothAcitivityForTask:]
- -[HDWorkoutLocationSmoother unitTest_didSmoothAcitivityForTask]
- _.str.289
- _.str.293
- _.str.299
- _OBJC_IVAR_$_HDWorkoutLocationSmoother._unitTest_didSmoothAcitivityForTask
- __OBJC_$_PROP_LIST_HDCloudSyncStatusProvider.432
- ___100+[HDDataTypeSourceOrderEntity _updateOrderedSourcesForType:profile:transaction:error:updateHandler:]_block_invoke.345
- ___100+[HDDataTypeSourceOrderEntity _updateOrderedSourcesForType:profile:transaction:error:updateHandler:]_block_invoke_2.346
- ___100-[HDStaticSyncImportTask _queue_importStaticSyncChangesFromDirectory:syncStore:progress:completion:]_block_invoke.464
- ___101-[HDCloudSyncVerifyAttachmentManagementRecordOperation _modifyCloudKitAndFinishWithManagementRecord:]_block_invoke.296
- ___102-[HDDaemonSyncEngine _performSyncTransactionForSession:store:anchorRangeMap:transactionContext:error:]_block_invoke.467
- ___103-[HDCloudSyncSharedSummaryPushPrepareOperation _pendingAndAcceptedParticipantRecordsInZone:completion:]_block_invoke.296
- ___103-[HDExtendedDatabaseTransaction initWithDatabase:context:transactionTimeout:continuationTimeout:error:]_block_invoke.316
- ___103-[HDProtectedDataOperation _notifyDelegateToPerformWorkWithDatabase:accessibilityAssertion:completion:]_block_invoke.357
- ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.299
- ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.303
- ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.311
- ___104-[HDCloudSyncPullChangeRecordOperation _continuationForFetchedRecord:recordID:inMemoryAsset:fetchError:]_block_invoke.309
- ___104-[HDCloudSyncPullChangeRecordOperation _continuationForFetchedRecord:recordID:inMemoryAsset:fetchError:]_block_invoke.310
- ___105-[HDDatabaseValidationTaskServer remote_validateDatabase:clientCompletionHandler:errorHandlerIdentifier:]_block_invoke.290
- ___105-[HDDatabaseValidationTaskServer remote_validateDatabase:clientCompletionHandler:errorHandlerIdentifier:]_block_invoke.292
- ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.299
- ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.307
- ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.312
- ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke_2.308
- ___106-[HDActivitySummaryBuilder _enumerateActivitySummariesAndCachesWithPredicate:largestAnchor:error:handler:]_block_invoke.304
- ___106-[HDBackgroundFeatureDeliveryManager periodicCountryMonitor:didFetchISOCountryCode:countryCodeProvenance:]_block_invoke.337
- ___106-[HDCloudSyncPipelineStageSharedSummaryAddParticipant _addParticipantWithLookupInfo:ownerName:ownerEmail:]_block_invoke.318
- ___106-[HDCloudSyncPipelineStageSharedSummaryAddParticipant _addParticipantWithLookupInfo:ownerName:ownerEmail:]_block_invoke_2.323
- ___107-[HDAppSubscriptionManager _updateSubscriptionsBasedOnBARSwitchState:lastLaunchTimes:dataCode:anchor:type:]_block_invoke.317
- ___107-[HDDemoDataFoodSampleGenerator generateObjectsForDemoPerson:fromTime:toTime:currentDate:objectCollection:]_block_invoke.367
- ___107-[HDNanoSyncManager _queue_performNextProactiveSyncWithRemainingDevices:accessibilityAssertion:completion:]_block_invoke.711
- ___108-[HDDatabaseValidationTaskServer remote_validateEntitiesWithClientCompletionHandler:errorHandlerIdentifier:]_block_invoke.294
- ___108-[HDHealthStoreServer _saveDataObjects:sourceEntity:sourceVersion:skipInsertionFilter:handler:creationDate:]_block_invoke
- ___108-[HDHealthStoreServer _saveDataObjects:sourceEntity:sourceVersion:skipInsertionFilter:handler:creationDate:]_block_invoke_2
- ___108-[HDIngestDeviceKeyValueEntriesOperation _pullDeviceKeyValueEntriesForProfile:repository:transaction:error:]_block_invoke.297
- ___109-[HDSecondaryDevicePairingAgentTaskServer remote_tearDownHealthSharingWithTinkerDeviceWithNRUUID:completion:]_block_invoke.335
- ___110-[HDWorkoutEffortRelationshipQueryServer associationsUpdatedForObject:subObject:type:behavior:objects:anchor:]_block_invoke.313
- ___111+[HDQuantitySampleValueEnumerator orderedQuantityValuesBySeriesForPredicate:transaction:options:error:handler:]_block_invoke.291
- ___112-[HDDatabasePruningCoordinator _pruneProfilesWithIdentifiers:takeAccessibilityAssertion:shouldDefer:completion:]_block_invoke.313
- ___113-[HDSeriesQuantityDataAggregator aggregateForState:collector:device:requestedAggregationDate:mode:options:error:]_block_invoke.310
- ___113-[HDSeriesQuantityDataAggregator aggregateForState:collector:device:requestedAggregationDate:mode:options:error:]_block_invoke_2.311
- ___115+[HDObjectAuthorizationEntity _setObjectAuthorizationRecords:syncProvenance:syncIdentity:skipErrors:profile:error:]_block_invoke.336
- ___115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.442
- ___115-[HDCloudSyncHandleMissingManateeIdentityOperation _deleteZonesForLostManateeIdentitiesInZones:container:database:]_block_invoke.306
- ___115-[HDCloudSyncHandleMissingManateeIdentityOperation _leaveSharesForLostManateeIdentitiesInZones:container:database:]_block_invoke.311
- ___116-[HDCloudSyncPushReferenceTombstonesOperation _generateTombstoneRecordsToPushAndReferencesRecordsToDeleteWithError:]_block_invoke.292
- ___117+[HDLogicalSourceEntity lookUpOrCreateLogicalSourceWithBundleIdentifier:owningAppBundleIdentifier:transaction:error:]_block_invoke.346
- ___117+[HDLogicalSourceEntity lookUpOrCreateLogicalSourceWithBundleIdentifier:owningAppBundleIdentifier:transaction:error:]_block_invoke_2.350
- ___119-[HDInsertSharedSummaryTransactionOperation _persistRecordsWithRepository:transactionRecord:summaryRecords:completion:]_block_invoke.321
- ___120-[HDCloudSyncSharedSummaryPushPruningOperation _findTransactionsToDelete:existingTransactionRecordsByZoneID:completion:]_block_invoke.297
- ___122-[HDAuthorizationManager handleHealthConceptAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.465
- ___122-[HDSharingAuthorizationRecipientStoreServer sharingAuthorizationManager:didAddSharingAuthorizations:recipientIdentifier:]_block_invoke.290
- ___123-[HDDefaultAuthorizationSchemaProvider setAuthorizationStatuses:authorizationModes:bundleIdentifier:options:profile:error:]_block_invoke.311
- ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.305
- ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.307
- ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.312
- ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.314
- ___123-[HDSecondaryDevicePairingAgentTaskServer remote_requestTinkerSharingOptInWithGuardianDisplayName:NRDeviceUUID:completion:]_block_invoke.296
- ___125-[HDSharingAuthorizationRecipientStoreServer sharingAuthorizationManager:didRemoveSharingAuthorizations:recipientIdentifier:]_block_invoke.292
- ___127-[HDClientAuthorizationOracle(Privileged) _queue_beginAuthorizationRequestDelegateTransactionWithSessionIdentifier:completion:]_block_invoke.495
- ___130+[HDDeviceKeyValueStorageEntryEntity setData:forKey:domain:deviceContextID:syncEntityIdentity:modificationDate:transaction:error:]_block_invoke.343
- ___132-[HDHealthStoreServer _queue_insertObjects:sourceEntity:sourceVersionOverride:shouldJournal:skipInsertionFilter:error:creationDate:]_block_invoke
- ___132-[HDHealthStoreServer _queue_insertObjects:sourceEntity:sourceVersionOverride:shouldJournal:skipInsertionFilter:error:creationDate:]_block_invoke_2
- ___132-[HDHealthStoreServer _queue_insertObjects:sourceEntity:sourceVersionOverride:shouldJournal:skipInsertionFilter:error:creationDate:]_block_invoke_3
- ___132-[HDHealthStoreServer _queue_insertObjects:sourceEntity:sourceVersionOverride:shouldJournal:skipInsertionFilter:error:creationDate:]_block_invoke_4
- ___133-[HDClientAuthorizationOracle enqueueAuthorizationRequestToWriteTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke.415
- ___134-[HDAuthorizationManager _authorizationRequestStatusForClientBundleIdentifier:writeTypes:readTypes:updateAuthorizationStatuses:error:]_block_invoke.398
- ___135-[HDNanoSyncManager _queue_synchronizeWithOptions:restoreMessagesSentHandler:targetSyncStore:reason:accessibilityAssertion:completion:]_block_invoke.503
- ___135-[HDNanoSyncManager _queue_synchronizeWithOptions:restoreMessagesSentHandler:targetSyncStore:reason:accessibilityAssertion:completion:]_block_invoke.511
- ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.339
- ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.340
- ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.341
- ___151-[HDCloudSyncSharedSummaryParticipantProfileCreationOperation _createProfileWithUUID:contactIdentifier:firstName:lastName:ownerParticipant:completion:]_block_invoke.291
- ___151-[HDCloudSyncSharedSummaryParticipantProfileCreationOperation _createProfileWithUUID:contactIdentifier:firstName:lastName:ownerParticipant:completion:]_block_invoke_2.292
- ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke.298
- ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke.304
- ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke_2.301
- ___162+[HDWorkoutZonesAssociationEntity _insertAssociationsForZonesSamplesWithUUIDs:withWorkoutUUID:syncProvenance:syncIdentity:ignoreDeletedObjects:transaction:error:]_block_invoke.332
- ___185-[HDWorkoutTrainingLoadDataSource _queryEffortSampleValuesForWorkoutUUID:workoutPID:workoutStartDate:workoutEndDate:workoutActivityType:workoutDuration:sourceID:activity:sampleHandler:]_block_invoke.323
- ___186-[HDCloudSyncSharedSummaryPushOperation createRecordsToSaveWithTransactions:transactionRecords:participantZoneID:participant:authorizationIdentifiers:allRecordsToSave:zoneIDs:taskGroup:]_block_invoke.308
- ___191+[HDAssociationEntity _insertEntriesWithParentUUID:childUUIDsData:provenance:syncIdentity:type:behavior:deleted:creationDate:destinationSubObjectReference:lastInsertedEntityID:context:error:]_block_invoke.425
- ___248+[HDDataProvenanceEntity insertOrLookupDataProvenanceForSyncProvenance:syncIdentity:originProductType:originSystemBuild:originOSVersion:localProductType:localSystemBuild:sourceVersion:timeZoneName:sourceID:deviceID:contributorID:transaction:error:]_block_invoke.394
- ___32-[HDBiomeInterface sleepFocusOn]_block_invoke.295
- ___35-[HDDeviceQueryServer _queue_start]_block_invoke.294
- ___35-[HDDeviceQueryServer _queue_start]_block_invoke_2.305
- ___36-[HDCacheDeleteCoordinator activate]_block_invoke.293
- ___36-[HDCacheDeleteCoordinator activate]_block_invoke.294
- ___36-[HDCloudSyncPipelineStagePush main]_block_invoke.301
- ___37-[HDCloudSyncStateSyncOperation main]_block_invoke.298
- ___38-[HDDaemon _setupMemoryWarningHandler]_block_invoke.462
- ___39-[HDCloudSyncCreateZonesOperation main]_block_invoke.296
- ___39-[HDIDSPersistentDictionary didCancel:]_block_invoke.424
- ___40-[HDCloudSyncAcceptSharesOperation main]_block_invoke.295
- ___40-[HDDataProvenanceManager _loadDefaults]_block_invoke.310
- ___41-[HDCloudSyncPipeline beginWithTaskTree:]_block_invoke.379
- ___41-[HDCloudSyncPipeline beginWithTaskTree:]_block_invoke.381
- ___41-[HDCloudSyncPipelineStageStateSync main]_block_invoke.299
- ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke.365
- ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke_2.367
- ___42-[HDCloudSyncDeleteSequenceOperation main]_block_invoke.295
- ___42-[HDCloudSyncDeleteSequenceOperation main]_block_invoke.296
- ___42-[HDCloudSyncLeaveAllSharesOperation main]_block_invoke.290
- ___42-[HDCloudSyncPullReferencesOperation main]_block_invoke.295
- ___42-[HDProfileManager _loadSecondaryProfiles]_block_invoke.330
- ___43-[HDWorkoutBuilderServer _didUpdateEvents:]_block_invoke.611
- ___44-[HDCloudSyncPullChangeRecordOperation main]_block_invoke.303
- ___44-[HDStaticSyncExportTask runWithCompletion:]_block_invoke.316
- ___45-[HDAppLauncher _queue_launchClientIfNeeded:]_block_invoke.299
- ___45-[HDCloudSyncLookupParticipantOperation main]_block_invoke.295
- ___45-[HDCloudSyncPrepareForSharingOperation main]_block_invoke.293
- ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.295
- ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.297
- ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.303
- ___45-[HDCloudSyncSharedSummaryPushOperation main]_block_invoke.290
- ___45-[HDHFDataStore _lock_restoreHFDFromArchive:]_block_invoke.400
- ___45-[HDWorkoutBuilderServer _didUpdateMetadata:]_block_invoke.601
- ___45-[HDWorkoutRouteDataSource elevationUpdated:]_block_invoke.416
- ___46-[HDCloudSyncDeleteStoreOnChildOperation main]_block_invoke.292
- ___46-[HDCloudSyncDisableSyncLocallyOperation main]_block_invoke.292
- ___46-[HDCloudSyncPushDeviceKeyValueOperation main]_block_invoke.300
- ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke.304
- ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke.306
- ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke_2.310
- ___46-[HDCloudSyncStatusProvider checkLastSyncDate]_block_invoke.333
- ___46-[HDDaemon registerDaemonReadyObserver:queue:]_block_invoke.473
- ___46-[HDSyncIdentityManager profileDidInitialize:]_block_invoke.356
- ___46-[HDWorkoutSessionServer didBeginNewActivity:]_block_invoke.620
- ___46-[_HDAWDPeriodicAction _doIfWaitingWithError:]_block_invoke.344
- ___47-[HDAgeGatingManager _registerForNotifications]_block_invoke.309
- ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke.294
- ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke.298
- ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke_2.296
- ___47-[HDCloudSyncPipelineStageContextSyncPush main]_block_invoke.300
- ___47-[HDWorkoutBuilderServer _didUpdateStatistics:]_block_invoke.650
- ___47-[HDWorkoutSessionServer _queue_generateError:]_block_invoke.706
- ___47-[HDWorkoutSessionServer _queue_generateEvent:]_block_invoke.700
- ___47-[HDWorkoutSessionServer _queue_generateEvent:]_block_invoke.703
- ___48-[HDCloudSyncPipeline _queue_runStage:taskTree:]_block_invoke.396
- ___48-[HDCloudSyncPipeline _queue_runStage:taskTree:]_block_invoke.398
- ___48-[HDWorkoutSessionServer didEndCurrentActivity:]_block_invoke.626
- ___48-[HDWorkoutSessionServer syncSessionEvent:date:]_block_invoke.670
- ___49-[HDCloudSyncAddSharingParticipantOperation main]_block_invoke.309
- ___49-[HDCloudSyncAddSharingParticipantOperation main]_block_invoke.310
- ___49-[HDCloudSyncMarkAllOwnersDisabledOperation main]_block_invoke.293
- ___49-[HDCloudSyncRegisterSubscriptionsOperation main]_block_invoke.293
- ___49-[HDWorkoutSessionServer remoteSessionDidRecover]_block_invoke.671
- ___50-[HDAppSubscriptionManager profileDidBecomeReady:]_block_invoke.312
- ___50-[HDCloudSyncPipelineStageDisableSyncLocally main]_block_invoke.289
- ___50-[HDDaemon registerDaemonActivatedObserver:queue:]_block_invoke.474
- ___50-[HDDataCollectionManager _dataCollectorBlacklist]_block_invoke.414
- ___51-[HDQueryManager _lock_executeDatabaseAccessBlocks]_block_invoke.311
- ___52-[HDCloudSyncSharedSummaryPushPrepareOperation main]_block_invoke.289
- ___52-[HDDemoDataManager _queue_generateDemoDataIfNeeded]_block_invoke.294
- ___52-[HDLiveWorkoutDataSource addQuantities:dataSource:]_block_invoke.411
- ___52-[HDLiveWorkoutDataSource addQuantities:dataSource:]_block_invoke_2.412
- ___52-[HDSeriesBuilderServer _setClientState:completion:]_block_invoke.321
- ___52-[HDWorkoutBasicDataSource setSampleTypesToCollect:]_block_invoke.411
- ___52-[HDWorkoutLocationSmoother _queue_smoothNextSample]_block_invoke.386
- ___53-[HDCloudSyncResetOperation _deleteZonesWithZoneIDs:]_block_invoke.290
- ___54-[HDCloudSyncCachedZone recordsForClass:error:filter:]_block_invoke.331
- ___54-[HDCloudSyncCachedZone recordsForClass:error:filter:]_block_invoke_2.332
- ___54-[HDDataManager _addTransactionInsertionCommitBlocks:]_block_invoke.320
- ___54-[HDPeriodicCountryMonitor _processCountryCodeResult:]_block_invoke.345
- ___55-[HDCloudSyncCachedZone recordForRecordID:class:error:]_block_invoke.341
- ___55-[HDCloudSyncCachedZone recordForRecordID:class:error:]_block_invoke_2.342
- ___55-[HDCloudSyncManager _persistErrorRequiringUserAction:]_block_invoke.450
- ___55-[HDFeatureAvailabilityManager registerObserver:queue:]_block_invoke.410
- ___55-[HDQueryServer authorizedSamplesForClientWithSamples:]_block_invoke.378
- ___55-[HDWorkoutBuilderServer remote_addSamples:completion:]_block_invoke.571
- ___55-[HDWorkoutBuilderServer remote_recoverWithCompletion:]_block_invoke.600
- ___55-[HDWorkoutSessionServer _queue_startInvalidationTimer]_block_invoke.717
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke.369
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_2.373
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_3.377
- ___56-[HDWorkoutBuilderServer remote_addMetadata:completion:]_block_invoke.575
- ___56-[HDWorkoutSessionTaskServer didEndActivity:dataSource:]_block_invoke.430
- ___57-[HDAppExtensionAssertion assertAndUpdateWithCompletion:]_block_invoke.297
- ___57-[HDAppExtensionAssertion assertAndUpdateWithCompletion:]_block_invoke.298
- ___57-[HDWorkoutSessionServer endCurrentActivityOnDate:error:]_block_invoke.641
- ___58-[HDCloudSyncDeleteZonesOperation _deleteZones:container:]_block_invoke.302
- ___58-[HDCloudSyncDeleteZonesOperation _deleteZones:container:]_block_invoke.304
- ___58-[HDCloudSyncRemoveInvalidShareParticipantsOperation main]_block_invoke.301
- ___58-[HDNanoSyncManager _queue_generateWatchActivationSamples]_block_invoke.549
- ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke.654
- ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke_2.655
- ___58-[HDWorkoutSessionTaskServer addWorkoutEvents:dataSource:]_block_invoke.427
- ___58-[HDWorkoutSessionTaskServer didBeginActivity:dataSource:]_block_invoke.429
- ___59+[HDConceptIndexer _indexSample:profile:transaction:error:]_block_invoke.392
- ___59-[HDCloudSyncStatusProvider fetchSyncStatusWithCompletion:]_block_invoke.296
- ___59-[HDCloudSyncStatusProvider fetchSyncStatusWithCompletion:]_block_invoke.298
- ___59-[HDFakeDataCollector _lock_setupSwimmingGeneratorsAtTime:]_block_invoke.321
- ___59-[HDWorkoutBuilderServer remote_removeMetadata:completion:]_block_invoke.580
- ___59-[HDWorkoutSessionTaskServer remote_recoverWithCompletion:]_block_invoke.413
- ___60+[HDSampleEntity dateIntervalsForSampleTypes:profile:error:]_block_invoke.394
- ___60-[HDCloudSyncDeleteStoresOperation _individualZonesToDelete]_block_invoke.294
- ___60-[HDCloudSyncSubscriptionNotificationHandler _enableAPSPush]_block_invoke.295
- ___60-[HDMirroredWorkoutSessionServer setTargetState:date:error:]_block_invoke.311
- ___60-[HDStatisticsCollectionQueryServer _queue_updateStatistics]_block_invoke.375
- ___60-[HDSummarySharingEntryStoreServer sharingEntriesDidUpdate:]_block_invoke.295
- ___61-[HDCloudSyncDetectSyncDisabledOperation _disableSyncLocally]_block_invoke.297
- ___61-[HDCloudSyncManagerPipelineTask mainWithRepositories:error:]_block_invoke.301
- ___61-[HDDatabase _mergeSecondaryJournalsWithActivity:completion:]_block_invoke.573
- ___61-[HDDatabaseMigrator(Tigris) _updateOriginVersionsWithError:]_block_invoke.420
- ___61-[HDWorkoutBuilderServer remote_addWorkoutEvents:completion:]_block_invoke.573
- ___61-[HDWorkoutSessionServer _queue_generateConfigurationUpdate:]_block_invoke.707
- ___62-[HDCloudSyncSharedSummarySynchronizeCloudStateOperation main]_block_invoke.295
- ___62-[HDUserCharacteristicsManager _queue_updateHasWatchOnAccount]_block_invoke.364
- ___62-[HDWorkoutSessionServer _processTargetStoppingStateWithDate:]_block_invoke.582
- ___63-[HDHealthStoreServer remote_deleteClientSourceWithCompletion:]_block_invoke.463
- ___63-[HDStatisticsCollectionQueryServer _queue_useCachedStatistics]_block_invoke.405
- ___63-[HDWorkoutBuilderServer remote_addWorkoutActivity:completion:]_block_invoke.589
- ___63-[HDWorkoutSessionTaskServer didDisconnectFromRemoteWithError:]_block_invoke.434
- ___64-[CMPedometer(HealthDaemon) hd_beginStreamingFromDatum:handler:]_block_invoke.380
- ___64-[CMPedometer(HealthDaemon) hd_beginStreamingFromDatum:handler:]_block_invoke.382
- ___64-[HDCloudSyncComputePullTargetsOperation _pullTargetsWithError:]_block_invoke.298
- ___64-[HDCloudSyncManager cloudSyncRepositoriesForClient:completion:]_block_invoke.421
- ___64-[HDCloudSyncModifyRecordsOperation _saveRecords:deleteRecords:]_block_invoke.312
- ___64-[HDFeatureAvailabilityManager _triggerImmediateSyncWithReason:]_block_invoke.409
- ___64-[HDNanoSyncManager _queue_receiveTinkerOptInRequest:syncStore:]_block_invoke.818
- ___64-[HDNanoSyncManager _scheduleResetReceivedNanoSyncAnchorsForHFD]_block_invoke.926
- ___64-[HDNotificationManager postNotificationWithRequest:completion:]_block_invoke.321
- ___64-[HDPeriodicCountryMonitor _fetchCountryIfNeededWithCompletion:]_block_invoke.329
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.534
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.542
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.548
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.557
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.558
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.538
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.549
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.546
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.550
- ___64-[HDWorkoutSessionTaskServer _fetchOrSetupServerWithCompletion:]_block_invoke.446
- ___65-[HDCloudSyncCoordinator resetAllProfilesWithContext:completion:]_block_invoke.398
- ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.308
- ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.315
- ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.324
- ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke_2.310
- ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke_2.317
- ___65-[HDDatabaseCorruptionTTRPrompter _popAlertWithRadarDescription:]_block_invoke.321
- ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.303
- ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.304
- ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke_2.305
- ___65-[HDSourceOrderManager updateOrderedSources:forObjectType:error:]_block_invoke.306
- ___65-[HDSyncIdentityManager rollCurrentSyncIdentityWithReason:error:]_block_invoke.350
- ___65-[HDWorkoutSessionRapportSyncController _sendPendingTransactions]_block_invoke.359
- ___66+[HDWorkoutCondenser _condenseWorkout:entity:configuration:error:]_block_invoke.341
- ___66-[HDClientDataCollectionTaskServer remote_registerWithCompletion:]_block_invoke.309
- ___66-[HDCloudSyncPullReferencesOperation _fetchAttachmentRecordAssets]_block_invoke.305
- ___66-[HDCloudSyncPullReferencesOperation _fetchAttachmentRecordAssets]_block_invoke.307
- ___66-[HDCloudSyncStateSyncOperation _pushUpdatedStateRecordsForZones:]_block_invoke.322
- ___66-[HDCoreMotionDataCollector _queue_forwardCoreMotionData:forType:]_block_invoke.306
- ___66-[HDCoreMotionDataCollector _queue_forwardCoreMotionData:forType:]_block_invoke.308
- ___66-[HDHealthStoreServer _holdActiveClientTransactionWithCompletion:]_block_invoke.486
- ___66-[HDMedicalIDDataManager _triggerSyncForSuccessfulMedicalIDUpdate]_block_invoke.326
- ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.908
- ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.909
- ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke_2.913
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.845
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.860
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.862
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.870
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.872
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.874
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.876
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.878
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.873
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.875
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.877
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.879
- ___66-[HDWorkoutBuilderSampleQueryServer _queue_performHistoricalQuery]_block_invoke.306
- ___67-[HDCloudSyncAcceptSharesOperation _acceptSharesWithShareMetadata:]_block_invoke.303
- ___67-[HDMirroredWorkoutSessionServer didDisconnectFromRemoteWithError:]_block_invoke.298
- ___68-[HDHealthStoreServer remote_setCharacteristic:forDataType:handler:]_block_invoke.471
- ___68-[HDLocationSeriesSampleEntity freezeWithTransaction:profile:error:]_block_invoke.333
- ___68-[HDLocationSeriesSampleEntity freezeWithTransaction:profile:error:]_block_invoke.335
- ___68-[HDNanoSyncManager _queue_recieveStartWorkoutAppRequest:syncStore:]_block_invoke.793
- ___68-[HDProcessStateManager _lock_registerObserver:forBundleIdentifier:]_block_invoke.307
- ___68-[HDWorkoutManager recoverAllActiveWorkoutSessionServersWithStates:]_block_invoke.387
- ___68-[HDWorkoutSessionTaskServer updateWorkoutConfiguration:dataSource:]_block_invoke.428
- ___69-[HDCloudSyncStateSyncOperation _performStateSyncInZones:completion:]_block_invoke.310
- ___69-[HDDaemon obliterateAndTerminateProfiles:options:reason:completion:]_block_invoke.361
- ___70-[HDCloudSyncManager _queue_considerStartingBackstopSyncForThreshold:]_block_invoke.454
- ___70-[HDDemoDataGenerator _insertIntoDatabaseObjectCollection:fromPerson:]_block_invoke.386
- ___70-[HDNanoSyncManager _queue_receiveChangeRequest:syncStore:completion:]_block_invoke.668
- ___70-[HDSummarySharingEntryIDSManager leaveInvitationWithUUID:completion:]_block_invoke.369
- ___71-[HDBackgroundObservationServerExtension connectWithCompletionHandler:]_block_invoke.309
- ___71-[HDCloudSyncCoordinator _queue_syncAllProfilesWithContext:completion:]_block_invoke.375
- ___71-[HDCloudSyncCoordinator _queue_syncAllProfilesWithContext:completion:]_block_invoke_2.376
- ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.359
- ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.360
- ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.361
- ___71-[HDSummarySharingEntryIDSManager revokeInvitationWithUUID:completion:]_block_invoke.367
- ___71-[HDSummarySharingEntryIDSManager revokeInvitationWithUUID:completion:]_block_invoke.368
- ___71-[HDWorkoutSessionServer stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.659
- ___72-[HDCloudSyncAccountProvider disableAndDeleteAllSyncDataWithCompletion:]_block_invoke.303
- ___72-[HDCloudSyncAccountProvider disableAndDeleteAllSyncDataWithCompletion:]_block_invoke.305
- ___72-[HDCloudSyncCachedZone recordsForClass:epoch:error:enumerationHandler:]_block_invoke.326
- ___72-[HDCloudSyncCachedZone recordsForClass:epoch:error:enumerationHandler:]_block_invoke_2.327
- ___72-[HDCloudSyncDeleteStoresOperation _deleteUnifiedZoneStoresInContainer:]_block_invoke.312
- ___72-[HDCloudSyncDeleteStoresOperation _deleteUnifiedZoneStoresInContainer:]_block_invoke.319
- ___72-[HDCloudSyncPipeline _queue_waitForCloudKitOperationDelayWithTaskTree:]_block_invoke.403
- ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.416
- ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.417
- ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.420
- ___72-[HDMirroredWorkoutSessionServer syncTransitionToState:date:completion:]_block_invoke.302
- ___72-[HDStatisticsCollectionQueryServer _queue_fetchAndDeliverAllStatistics]_block_invoke.392
- ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.397
- ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.398
- ___73-[HDCloudSyncAccountProvider _performSyncForAccountChangeWithCompletion:]_block_invoke.334
- ___73-[HDCloudSyncPeriodicActivityScheduler performInitialRestore:completion:]_block_invoke.319
- ___73-[HDCloudSyncPushReferencesOperation _pushToCloudKitAndFinishForRecords:]_block_invoke.305
- ___73-[HDCoreMotionDataCollector _queue_beginUpdatesWithTargetCollectionType:]_block_invoke.317
- ___73-[HDNanoSyncManager _syncQueue_prepareForCompanionChangeWithStore:error:]_block_invoke.593
- ___73-[HDWorkoutMirroringManager recoverMirroredWorkoutSessionWithCompletion:]_block_invoke.334
- ___73-[HDWorkoutMirroringManager recoverMirroredWorkoutSessionWithCompletion:]_block_invoke.335
- ___74+[HDSeriesSampleEntity freezeSeriesWithIdentifier:metadata:profile:error:]_block_invoke.327
- ___74-[HDAnalyticsSubmissionCoordinator _locked_sendDailyAnalyticsWithTimeout:]_block_invoke.330
- ___74-[HDAnalyticsSubmissionCoordinator _locked_sendDailyAnalyticsWithTimeout:]_block_invoke_2.335
- ___74-[HDDataAggregator requestAggregationThroughDate:mode:options:completion:]_block_invoke.296
- ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.300
- ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.304
- ___74-[HDWorkoutBuilderServer _lock_recoverPersistedDataWithTransaction:error:]_block_invoke.504
- ___75-[HDCloudSyncObserverTaskServer _queue_instantiateCloudSyncObserverStatus:]_block_invoke.356
- ___75-[HDCloudSyncObserverTaskServer _queue_instantiateCloudSyncObserverStatus:]_block_invoke_2.357
- ___75-[HDCloudSyncUpdateCachedZonesOperation fetchChangesForContainer:database:]_block_invoke.296
- ___75-[HDCoreMotionDataCollector _didReceiveCoreMotionData:startingDatum:error:]_block_invoke.312
- ___75-[HDCurrentActivitySummaryHelper _handleSignificantTimeChangeNotification:]_block_invoke.307
- ___75-[HDWorkoutBasicDataSource workoutSession:didChangeToState:fromState:date:]_block_invoke.434
- ___75-[HDWorkoutBuilderServer remote_updateActivityWithUUID:endDate:completion:]_block_invoke.597
- ___76-[HDActiveDataAggregator dataCollector:didCollectSensorData:device:options:]_block_invoke.312
- ___76-[HDNanoSyncManager _queue_receiveTinkerEndToEndCloudSyncRequest:syncStore:]_block_invoke.892
- ___76-[HDWorkoutSessionServer didReceiveDataFromRemoteWorkoutSession:completion:]_block_invoke.666
- ___77+[HDDataEntity insertDataObjects:insertionContext:profile:completionHandler:]_block_invoke.452
- ___77-[HDDeleteAttachmentReferenceOperation performWithProfile:transaction:error:]_block_invoke.297
- ___78+[HDDeletedSampleEntity insertCodableDeletedSamples:provenance:profile:error:]_block_invoke.364
- ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.430
- ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.435
- ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.436
- ___78-[HDCloudSyncRemoveSharingParticipantsOperation _saveUpdatedShares:container:]_block_invoke.296
- ___78-[HDCloudSyncSeizeAbandonedStoresOperation _markPendingOwnerForSeizureTargets]_block_invoke.311
- ___78-[HDDatabaseMigrator(Monarch) _fixProvenancesWithZeroSourceOrDeviceWithError:]_block_invoke.614
- ___78-[HDDatabaseMigrator(Monarch) _fixProvenancesWithZeroSourceOrDeviceWithError:]_block_invoke_2.615
- ___78-[HDNanoSyncManager _queue_recieveCompanionUserNotificationRequest:syncStore:]_block_invoke.804
- ___79-[HDCloudSyncManager configureForShareSetupMetadata:acceptedShares:completion:]_block_invoke.462
- ___79-[HDCloudSyncManager configureForShareSetupMetadata:acceptedShares:completion:]_block_invoke.469
- ___79-[HDCloudSyncRepairRegistryRecordsOperation _modifyRecordsAndFinish:container:]_block_invoke.295
- ___79-[HDDatabaseTransaction performWithContext:error:block:inaccessibilityHandler:]_block_invoke.319
- ___79-[HDPostInstallUpdateManager _triggerMigrationForProfile:protected:completion:]_block_invoke.315
- ___79-[HDWorkoutBuilderServer remote_updateActivityWithUUID:addMetadata:completion:]_block_invoke.599
- ___79-[HDWorkoutClusterServer remote_generateRaceRouteClustersWithLimit:completion:]_block_invoke.298
- ___80-[HDCloudSyncCoordinator _queue_syncProfilesWithIdentifiers:context:completion:]_block_invoke.380
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke.311
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke.332
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_2.312
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_2.335
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_3.322
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_4.326
- ___80-[HDSecondaryDevicePairingAgentTaskServer _prepareGuardianForSharingForRequest:]_block_invoke.351
- ___80-[HDWorkoutSessionServer beginNewActivityWithConfiguration:date:metadata:error:]_block_invoke.640
- ___81-[HDDatabaseMigrator(Emet) _emet_migrateWorkoutEventMetadataToProtobufWithError:]_block_invoke.318
- ___81-[HDHealthStoreServer remote_setBackgroundDeliveryFrequency:forDataType:handler:]_block_invoke.450
- ___81-[HDWorkoutSessionRapportSyncController sendRequest:transaction:responseHandler:]_block_invoke.351
- ___82+[HDLocationSeriesSampleEntity insertLocationData:seriesIdentifier:profile:error:]_block_invoke
- ___82+[HDLocationSeriesSampleEntity insertLocationData:seriesIdentifier:profile:error:]_block_invoke_2
- ___82-[HDCloudSyncManager _primaryContainerIdentifiersForCurrentAccountWithCompletion:]_block_invoke.439
- ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.538
- ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.539
- ___82-[HDDatabase _old_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.544
- ___82-[HDWorkoutSessionServer enableAutomaticDetectionForActivityConfigurations:error:]_block_invoke.643
- ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.593
- ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.601
- ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.604
- ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.605
- ___83-[HDCloudSyncManager _scheduleResetReceivedCloudSyncAnchorsAndRebaseForHFDRecovery]_block_invoke.362
- ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke.331
- ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke_2.337
- ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke_3.339
- ___83-[HDDeviceKeyValueStoreManager _deleteRemoteEntries:deviceContextByIdentity:error:]_block_invoke.315
- ___83-[HDWorkoutBuilderServer _addSamples:quantities:dataSource:shouldSavePriorToStart:]_block_invoke.517
- ___83-[HDWorkoutBuilderServer _addSamples:quantities:dataSource:shouldSavePriorToStart:]_block_invoke_2.519
- ___84-[HDCloudSyncPreparePushZoneForStoreOperation _createZoneWithIdentifier:forStoreId:]_block_invoke.305
- ___84-[HDWorkoutLocationSmoother _queue_smoothActivity:activityIndex:forTask:completion:]_block_invoke.393
- ___84-[HDWorkoutLocationSmoother _queue_smoothActivity:activityIndex:forTask:completion:]_block_invoke.394
- ___85-[HDWorkoutMirroringManager rapportMessenger:didReceiveRequest:data:responseHandler:]_block_invoke.311
- ___86-[HDCloudSyncMedicalIDPushOperation _pushMedicalIDRecordToCloudForContainer:database:]_block_invoke.296
- ___87-[HDCloudSyncFetchRecordsOperation _fetchRecordsWithIDs:container:database:completion:]_block_invoke.295
- ___87-[HDCloudSyncPushDeviceKeyValueOperation _computeRecordsToSaveAndDeleteWithCompletion:]_block_invoke.306
- ___87-[HDDataCollectionManager _requestAggregationThroughDate:type:mode:options:completion:]_block_invoke.368
- ___87-[HDHealthStoreServer remote_requestConceptReadAuthorizationForType:filter:completion:]_block_invoke.363
- ___87-[HDInsertSharedSummaryTransactionOperation performWithProfile:transaction:completion:]_block_invoke.291
- ___87-[HDWorkoutEventsManager requestPendingEventsThroughDate:sessionIdentifier:completion:]_block_invoke.304
- ___87-[HDWorkoutEventsManager requestPendingEventsThroughDate:sessionIdentifier:completion:]_block_invoke.306
- ___88-[HDCloudSyncPushDeviceContextOperation _updateRecordsAdd:recordIDsToDelete:completion:]_block_invoke.310
- ___88-[HDDataCollectionManager _requestAggregationThroughDate:types:mode:options:completion:]_block_invoke.367
- ___88-[HDWorkoutSessionTaskServer remote_recoverAllActiveSessionsWithStates:date:completion:]_block_invoke.415
- ___88-[HDWorkoutSessionTaskServer remote_recoverAllActiveSessionsWithStates:date:completion:]_block_invoke.416
- ___89+[HDUserDomainConceptSyncEntity receiveSyncObjects:version:syncProvenance:profile:error:]_block_invoke.302
- ___89-[HDCloudSyncComputePushTargetsOperation _pushTargetsForContainer:ownerIdentifier:error:]_block_invoke.305
- ___89-[HDHealthStoreServer remote_fetchModificationDateForCharacteristicWithDataType:handler:]_block_invoke.472
- ___89-[HDHealthStoreServer remote_requestPerObjectReadAuthorizationForType:filter:completion:]_block_invoke.359
- ___89-[HDHealthStoreServer remote_requestPerObjectReadAuthorizationForType:filter:completion:]_block_invoke.361
- ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.568
- ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.569
- ___90+[HDLocationSeriesHFDMigrationEntity _migrateSeriesWithKey:toSQLFromStore:database:error:]_block_invoke.311
- ___90+[HDQuantitySeriesHFDMigrationEntity _migrateSeriesWithKey:toSQLFromStore:database:error:]_block_invoke.298
- ___90+[HDRaceRouteLocationSeriesEntity createRoutePointsFromWorkout:transaction:profile:error:]_block_invoke.322
- ___90+[HDRaceRouteLocationSeriesEntity createRoutePointsFromWorkout:transaction:profile:error:]_block_invoke_2.324
- ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.344
- ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.345
- ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.349
- ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.353
- ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke_2.350
- ___90-[HDCloudSyncObserverTaskServer remote_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.336
- ___90-[HDCloudSyncPullChangeRecordOperation _persistFetchedArchiveAsset:protocolVersion:error:]_block_invoke.332
- ___90-[HDCloudSyncPullChangeRecordOperation _persistFetchedArchiveAsset:protocolVersion:error:]_block_invoke.334
- ___90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.364
- ___90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.366
- ___90-[HDCloudSyncSharedSummaryPushPruningOperation _modifyRecordsAndFinish:recordIDsToDelete:]_block_invoke.306
- ___90-[HDDataAggregator persistForCollector:usedDatums:source:device:error:persistenceHandler:]_block_invoke.318
- ___92-[HDBatchedQueryServer batchObjectsWithEnumerator:includeDeletedObjects:error:batchHandler:]_block_invoke.294
- ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke.344
- ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke.345
- ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke_2.346
- ___92-[HDCloudSyncCoordinator(CloudSyncJournalMerge) _mergeCloudSyncJournalsForProfile:taskTree:]_block_invoke.298
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.302
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.304
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.310
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.311
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.315
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke_2.306
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke_2.312
- ___93+[HDMedicationDoseEventEntity _logPersistedDoseEventOnCommitDatabase:doseEvent:persistentID:]_block_invoke.384
- ___93-[HDAppSubscriptionManager _updateObservationStatusForDataTypeCode:lastAppLaunchTimes:error:]_block_invoke.339
- ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke.296
- ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke_2.301
- ___94-[HDIngestDeviceContextsOperation _pullDeviceContextsForProfile:repository:transaction:error:]_block_invoke.296
- ___94-[HDRestorableAlarmScheduler _queue_notifyClientsOfDueEventsAndScheduleNextFireDateWithError:]_block_invoke.322
- ___94-[HDWorkoutBasicDataSource _workoutDataDestination:requestsSamplesOfType:from:to:transaction:]_block_invoke.426
- ___94-[HDWorkoutManager generatePauseOrResumeRequestAllowingBackgroundRuntime:metadata:completion:]_block_invoke.368
- ___95+[HDAppSubscriptionAppLaunchEntity insertOrUpdateAppSDKVersionToken:forBundleID:profile:error:]_block_invoke.382
- ___95-[HDCloudSyncPushReferenceTombstonesOperation _modifyCloudWithRecordsToSave:recordIDsToDelete:]_block_invoke.306
- ___95-[HDDatabaseJournal _mergeJournalChapter:profile:accessibilityAssertion:shouldContinueHandler:]_block_invoke.362
- ___95-[HDQueryControlServer queryServer:requestsAuthorizationWithContext:promptIfNeeded:completion:]_block_invoke.305
- ___96-[HDTTRPromptController _presentTTRPromptForErrors:lastPromptBuild:lastPromptDate:currentBuild:]_block_invoke.359
- ___97+[HDLogicalSourceOrderEntity updateOrderedLogicalSourcesForType:transaction:error:updateHandler:]_block_invoke.348
- ___97+[HDLogicalSourceOrderEntity updateOrderedLogicalSourcesForType:transaction:error:updateHandler:]_block_invoke_2.349
- ___97-[HDBackgroundObservationServerExtension notifyExtensionOfUpdateForSampleType:completionHandler:]_block_invoke.314
- ___97-[HDHealthStoreServer remote_requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.371
- ___97-[HDSecondaryDevicePairingAgentTaskServer _setupTinkerProfileForRequest:metadata:acceptedShares:]_block_invoke.359
- ___98+[HDWorkoutBuilderAssociatedObjectEntity associateObject:timestamp:withBuilder:transaction:error:]_block_invoke
- ___98+[HDWorkoutBuilderAssociatedObjectEntity associateObject:timestamp:withBuilder:transaction:error:]_block_invoke_2
- ___Block_byref_object_copy_.304
- ___Block_byref_object_copy_.316
- ___Block_byref_object_copy_.320
- ___Block_byref_object_copy_.322
- ___Block_byref_object_copy_.327
- ___Block_byref_object_copy_.367
- ___Block_byref_object_dispose_.305
- ___Block_byref_object_dispose_.317
- ___Block_byref_object_dispose_.321
- ___Block_byref_object_dispose_.323
- ___Block_byref_object_dispose_.328
- ___Block_byref_object_dispose_.368
- ____HDAddUniquenessChecksumToOriginalFHIRResourceEntity_block_invoke.1337
- ____HDCopyWorkoutTotalsToPrimaryActivity_block_invoke.599
- ____HDMigrateCycleTrackingOnboarding_block_invoke.963
- ____HDMigrateCycleTrackingOnboarding_block_invoke_2.964
- ____HDUpdateClinicalRecordEntities_block_invoke.889
- ____HDUpdateClinicalRecordEntities_block_invoke_2.890
- ____HDUpdateClinicalRecordEntities_block_invoke_3.894
- ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke.975
- ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke.979
- ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke_2.980
- ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke_3.984
- ____ZL27_HDHFDataStoreWillOpenStoreP13HDHFDataStore_block_invoke.485
- ___block_descriptor_40_e8_32bs_e30_B68?0d8d16d24d32d40q48B56^60ls32l8
- ___block_descriptor_40_e8_32s_e11_v24?0q8q16ls32l8
- ___block_descriptor_48_ea8_32bs40r_e20_B24?0"NSUUID"8^16lr40l8s32l8
- ___block_descriptor_48_ea8_32s40s_e21_B24?0"NSArray"8^16ls32l8s40l8
- ___block_descriptor_64_ea8_32s40s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e72_B32?0"HDStatisticsCollectionCalculator"8"HKQuantityType"16"NSUUID"24ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_81_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.1008
- ___block_literal_global.1017
- ___block_literal_global.1040
- ___block_literal_global.1055
- ___block_literal_global.1063
- ___block_literal_global.1072
- ___block_literal_global.1081
- ___block_literal_global.1104
- ___block_literal_global.1127
- ___block_literal_global.1136
- ___block_literal_global.1145
- ___block_literal_global.291
- ___block_literal_global.293
- ___block_literal_global.295
- ___block_literal_global.299
- ___block_literal_global.307
- ___block_literal_global.323
- ___block_literal_global.337
- ___block_literal_global.341
- ___block_literal_global.343
- ___block_literal_global.349
- ___block_literal_global.353
- ___block_literal_global.358
- ___block_literal_global.363
- ___block_literal_global.372
- ___block_literal_global.386
- ___block_literal_global.388
- ___block_literal_global.396
- ___block_literal_global.404
- ___block_literal_global.410
- ___block_literal_global.414
- ___block_literal_global.425
- ___block_literal_global.426
- ___block_literal_global.431
- ___block_literal_global.432
- ___block_literal_global.436
- ___block_literal_global.438
- ___block_literal_global.440
- ___block_literal_global.446
- ___block_literal_global.448
- ___block_literal_global.457
- ___block_literal_global.458
- ___block_literal_global.462
- ___block_literal_global.468
- ___block_literal_global.473
- ___block_literal_global.478
- ___block_literal_global.484
- ___block_literal_global.486
- ___block_literal_global.488
- ___block_literal_global.502
- ___block_literal_global.510
- ___block_literal_global.517
- ___block_literal_global.525
- ___block_literal_global.527
- ___block_literal_global.545
- ___block_literal_global.546
- ___block_literal_global.553
- ___block_literal_global.559
- ___block_literal_global.560
- ___block_literal_global.564
- ___block_literal_global.573
- ___block_literal_global.582
- ___block_literal_global.584
- ___block_literal_global.586
- ___block_literal_global.595
- ___block_literal_global.596
- ___block_literal_global.597
- ___block_literal_global.603
- ___block_literal_global.605
- ___block_literal_global.607
- ___block_literal_global.609
- ___block_literal_global.611
- ___block_literal_global.613
- ___block_literal_global.615
- ___block_literal_global.617
- ___block_literal_global.619
- ___block_literal_global.632
- ___block_literal_global.633
- ___block_literal_global.639
- ___block_literal_global.644
- ___block_literal_global.646
- ___block_literal_global.650
- ___block_literal_global.669
- ___block_literal_global.673
- ___block_literal_global.674
- ___block_literal_global.676
- ___block_literal_global.692
- ___block_literal_global.694
- ___block_literal_global.699
- ___block_literal_global.701
- ___block_literal_global.707
- ___block_literal_global.708
- ___block_literal_global.710
- ___block_literal_global.720
- ___block_literal_global.722
- ___block_literal_global.733
- ___block_literal_global.737
- ___block_literal_global.756
- ___block_literal_global.765
- ___block_literal_global.774
- ___block_literal_global.790
- ___block_literal_global.802
- ___block_literal_global.806
- ___block_literal_global.815
- ___block_literal_global.824
- ___block_literal_global.848
- ___block_literal_global.871
- ___block_literal_global.880
- ___block_literal_global.889
- ___block_literal_global.912
- ___block_literal_global.913
- ___block_literal_global.928
- ___block_literal_global.932
- ___block_literal_global.944
- ___block_literal_global.953
- ___block_literal_global.976
- ___block_literal_global.999
- ___unnamed_16
- ___unnamed_21
- ___unnamed_22
- __insertStatementKey.key.492
- _associateObject:timestamp:withBuilder:transaction:error:.insertKey
- _columnDefinitionsWithCount:.HDDeviceKeyValueStorageEntryEntityColumnDefinitions.381
- _columnDefinitionsWithCount:.columnDefinitions.393
- _objc_msgSend$associateObject:timestamp:transaction:error:
- _objc_msgSend$associateObject:timestamp:withBuilder:transaction:error:
- _objc_msgSend$insertLocationData:seriesIdentifier:profile:error:
- _objc_msgSend$saveSamples:withCompletion:
- _objc_msgSend$unitTest_didSmoothAcitivityForTask
CStrings:
+ "%{public}@: Device doesnt support shared summaries"
+ "%{public}@: Received biolockout notification; ignoring (no passcode)"
+ "(?, %@)"
+ "(?, %@),"
+ "@\"OS_os_log\""
+ "@\"STBackgroundActivitiesStatusDomainBackgroundActivityAttribution\""
+ "@\"_TtC22HealthDaemonFoundation49HDUserNotificationSystemApertureContentDefinition\""
+ "@72@0:8@16@24@32@40{?=qqq}48"
+ "AND (%@.sample_type = %@)"
+ "AND (samples.start_date >= %f) AND (samples.start_date <= %f) AND (samples.end_date >= %f)"
+ "B32@?0@\"HDDatabaseTransaction\"8@\"NSString\"16^@24"
+ "B32@?0@\"NSArray\"8@\"NSArray\"16^@24"
+ "B32@?0@\"NSUUID\"8q16^@24"
+ "B64@?0q8d16d24d32q40q48^@56"
+ "B80@0:8@16@24@32@40@48@56^@64@?72"
+ "B96@0:8@16@24@32@40d48@56{?=qqq}64^@88"
+ "CREATE INDEX %@_dt_idx ON %@ (%@)"
+ "CREATE TABLE workout_builder_associated_objects (workout_builder_id INTEGER NOT NULL REFERENCES workout_builders(rowid) ON DELETE CASCADE, object_uuid BLOB NOT NULL, timestamp REAL NOT NULL, type INTEGER NOT NULL, UNIQUE(workout_builder_id, object_uuid, timestamp, type))"
+ "CREATE TEMPORARY TABLE %@ (%@ BLOB NOT NULL, %@ INTERGER NOT NULL)"
+ "Failed to get the dataInterval for %{public}@ at workout end; will exit existing statistics: %{public}@"
+ "Failed to journal series sample."
+ "HDMirroredWorkoutPendingData"
+ "INSERT INTO %@ (%@, %@) VALUES "
+ "Process \"%@\" (%d) has nil source bundle identifier without auth bypass. Client entitlements: %@"
+ "SELECT                      %@.%@,                      %@.%@,                      %@.%@,                      %@.%@,                      %@.%@,                      %@.%@,                      %@.%@                      FROM %@                      INNER JOIN %@ USING(%@)                      INNER JOIN %@ USING(%@)                      INNER JOIN %@ USING(%@)                      LEFT JOIN %@ USING(%@)                      INNER JOIN %@ ON %@.%@=%@.%@                      WHERE (                      (%@.%@ = %@)                      %@                      %@                      )                      ORDER BY %@.%@ ASC"
+ "SELECT DISTINCT %@, %@ FROM %@ WHERE %@ = ?"
+ "T@\"NSArray\",C,N,V_data"
+ "T@?,C,N,V_unitTest_didSmoothActivityForTask"
+ "WorkoutRouteSmoother"
+ "[mirroring] %{public}@: Adding data to pending."
+ "[routes] Error deleting route samples <%{public}@>, error=%{public}@"
+ "_saveDataObjects:sourceEntity:sourceVersion:skipInsertionFilter:databaseAssertion:handler:creationDate:"
+ "_unitTest_didSmoothActivityForTask"
+ "associateObject:code:timestamp:transaction:error:"
+ "associateObject:code:timestamp:withBuilder:transaction:error:"
+ "enumerateAssociatedSampleValuesWithCustomQueryOfType:interval:profile:error:handler:"
+ "initWithData:completion:"
+ "insertDataObjects:sourceEntity:deviceEntity:sourceVersion:creationDate:timeZone:OSVersion:error:"
+ "insertLocationData:seriesIdentifier:assertion:profile:error:"
+ "isFirstPartyClient"
+ "localDataProvenanceForSourceEntity:version:deviceEntity:timzone:OSVersion:"
+ "q56@0:8@16q24d32@40^@48"
+ "q64@0:8@16q24d32@40@48^@56"
+ "quantityValuesWithSourceForType:from:to:dataInterval:table:transaction:error:handler:"
+ "sample_type"
+ "saveSamples:databaseAssertion:withCompletion:"
+ "setUnitTest_didSmoothActivityForTask:"
+ "unitTest_didSmoothActivityForTask"
+ "updateActivityWithUUID:addMedatata:dataSource:"
+ "v32@?0@\"HKWorkoutRoute\"8Q16^B24"
+ "v32@?0q8q16d24"
+ "v40@0:8@\"NSArray\"16@\"HDAssertion\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@\"NSUUID\"16@\"NSDictionary\"24@\"<HDWorkoutDataSource>\"32"
+ "workoutSavingQueryPerf"
+ "workoutTempTableChanges"
+ "{?=ii}"
- "B24@?0@\"NSArray\"8^@16"
- "SELECT DISTINCT %@ FROM %@ WHERE %@ = ?"
- "Source bundle identifier is nil. Client entitlements: %@"
- "T@?,C,N,V_unitTest_didSmoothAcitivityForTask"
- "[routes] Error deleting route sample %{public}@ with %lu location(s): %{public}@"
- "_saveDataObjects:sourceEntity:sourceVersion:skipInsertionFilter:handler:creationDate:"
- "_unitTest_didSmoothAcitivityForTask"
- "associateObject:timestamp:transaction:error:"
- "associateObject:timestamp:withBuilder:transaction:error:"
- "insertLocationData:seriesIdentifier:profile:error:"
- "q48@0:8@16d24@32^@40"
- "q56@0:8@16d24@32@40^@48"
- "saveSamples:withCompletion:"
- "setUnitTest_didSmoothAcitivityForTask:"
- "unitTest_didSmoothAcitivityForTask"
- "v24@?0q8q16"

```
