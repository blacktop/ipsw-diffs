## HealthDaemon

> `/System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon`

```diff

-6200.3.4.0.0
-  __TEXT.__text: 0x792b08
+6200.3.8.0.0
+  __TEXT.__text: 0x792ad0
   __TEXT.__auth_stubs: 0x4820
-  __TEXT.__objc_methlist: 0x43b44
+  __TEXT.__objc_methlist: 0x43b64
   __TEXT.__const: 0x1df6c
   __TEXT.__dlopen_cstrs: 0x15b
-  __TEXT.__cstring: 0x7d130
+  __TEXT.__cstring: 0x7d138
   __TEXT.__constg_swiftt: 0x14dc
   __TEXT.__swift5_typeref: 0xd9d
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__unwind_info: 0x1cd38
   __TEXT.__eh_frame: 0x2310
   __TEXT.__objc_classname: 0xc5c3
-  __TEXT.__objc_methname: 0x8ed05
-  __TEXT.__objc_methtype: 0x16b61
+  __TEXT.__objc_methname: 0x8ed6c
+  __TEXT.__objc_methtype: 0x16c36
   __TEXT.__objc_stubs: 0x505c0
   __DATA_CONST.__got: 0x5668
   __DATA_CONST.__const: 0x1d2a0

   __DATA_CONST.__objc_catlist: 0x4c0
   __DATA_CONST.__objc_protolist: 0x9b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19f08
+  __DATA_CONST.__objc_selrefs: 0x19f18
   __DATA_CONST.__objc_protorefs: 0x1d8
   __DATA_CONST.__objc_superrefs: 0x1d88
   __DATA_CONST.__objc_arraydata: 0x84a0
   __AUTH_CONST.__auth_got: 0x2428
   __AUTH_CONST.__const: 0x10018
   __AUTH_CONST.__cfstring: 0x3d5e0
-  __AUTH_CONST.__objc_const: 0x7d9a8
+  __AUTH_CONST.__objc_const: 0x7d9b8
   __AUTH_CONST.__objc_arrayobj: 0x1ed8
   __AUTH_CONST.__objc_intobj: 0x3e58
   __AUTH_CONST.__objc_doubleobj: 0x3c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C0B89F1F-85BA-3692-9953-F80C92A776BA
+  UUID: 98FCFE56-E763-30F1-8A8B-82C9FA7834CB
   Functions: 34769
   Symbols:   103917
-  CStrings:  44278
+  CStrings:  44281
 
Symbols:
+ _.str.301
+ _.str.305
+ _.str.311
+ __OBJC_$_PROP_LIST_HDCloudSyncStatusProvider.444
+ ___100+[HDDataTypeSourceOrderEntity _updateOrderedSourcesForType:profile:transaction:error:updateHandler:]_block_invoke.357
+ ___100+[HDDataTypeSourceOrderEntity _updateOrderedSourcesForType:profile:transaction:error:updateHandler:]_block_invoke_2.358
+ ___100-[HDStaticSyncImportTask _queue_importStaticSyncChangesFromDirectory:syncStore:progress:completion:]_block_invoke.476
+ ___101-[HDCloudSyncVerifyAttachmentManagementRecordOperation _modifyCloudKitAndFinishWithManagementRecord:]_block_invoke.308
+ ___102-[HDDaemonSyncEngine _performSyncTransactionForSession:store:anchorRangeMap:transactionContext:error:]_block_invoke.479
+ ___102-[HDDaemonSyncEngine _performSyncTransactionForSession:store:anchorRangeMap:transactionContext:error:]_block_invoke.482
+ ___103-[HDCloudSyncSharedSummaryPushPrepareOperation _pendingAndAcceptedParticipantRecordsInZone:completion:]_block_invoke.308
+ ___103-[HDExtendedDatabaseTransaction initWithDatabase:context:transactionTimeout:continuationTimeout:error:]_block_invoke.328
+ ___103-[HDProtectedDataOperation _notifyDelegateToPerformWorkWithDatabase:accessibilityAssertion:completion:]_block_invoke.369
+ ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.311
+ ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.315
+ ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.323
+ ___104-[HDCloudSyncPullChangeRecordOperation _continuationForFetchedRecord:recordID:inMemoryAsset:fetchError:]_block_invoke.321
+ ___104-[HDCloudSyncPullChangeRecordOperation _continuationForFetchedRecord:recordID:inMemoryAsset:fetchError:]_block_invoke.322
+ ___105-[HDDatabaseValidationTaskServer remote_validateDatabase:clientCompletionHandler:errorHandlerIdentifier:]_block_invoke.302
+ ___105-[HDDatabaseValidationTaskServer remote_validateDatabase:clientCompletionHandler:errorHandlerIdentifier:]_block_invoke.304
+ ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.311
+ ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.314
+ ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.319
+ ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.322
+ ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.324
+ ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke_2.320
+ ___106-[HDActivitySummaryBuilder _enumerateActivitySummariesAndCachesWithPredicate:largestAnchor:error:handler:]_block_invoke.316
+ ___106-[HDBackgroundFeatureDeliveryManager periodicCountryMonitor:didFetchISOCountryCode:countryCodeProvenance:]_block_invoke.349
+ ___106-[HDCloudSyncPipelineStageSharedSummaryAddParticipant _addParticipantWithLookupInfo:ownerName:ownerEmail:]_block_invoke.330
+ ___106-[HDCloudSyncPipelineStageSharedSummaryAddParticipant _addParticipantWithLookupInfo:ownerName:ownerEmail:]_block_invoke.333
+ ___106-[HDCloudSyncPipelineStageSharedSummaryAddParticipant _addParticipantWithLookupInfo:ownerName:ownerEmail:]_block_invoke_2.335
+ ___107-[HDAppSubscriptionManager _updateSubscriptionsBasedOnBARSwitchState:lastLaunchTimes:dataCode:anchor:type:]_block_invoke.329
+ ___107-[HDDemoDataFoodSampleGenerator generateObjectsForDemoPerson:fromTime:toTime:currentDate:objectCollection:]_block_invoke.379
+ ___107-[HDNanoSyncManager _queue_performNextProactiveSyncWithRemainingDevices:accessibilityAssertion:completion:]_block_invoke.723
+ ___108-[HDDatabaseValidationTaskServer remote_validateEntitiesWithClientCompletionHandler:errorHandlerIdentifier:]_block_invoke.306
+ ___108-[HDIngestDeviceKeyValueEntriesOperation _pullDeviceKeyValueEntriesForProfile:repository:transaction:error:]_block_invoke.309
+ ___109-[HDSecondaryDevicePairingAgentTaskServer remote_tearDownHealthSharingWithTinkerDeviceWithNRUUID:completion:]_block_invoke.347
+ ___110-[HDWorkoutEffortRelationshipQueryServer associationsUpdatedForObject:subObject:type:behavior:objects:anchor:]_block_invoke.325
+ ___111+[HDQuantitySampleValueEnumerator orderedQuantityValuesBySeriesForPredicate:transaction:options:error:handler:]_block_invoke.303
+ ___112-[HDDatabasePruningCoordinator _pruneProfilesWithIdentifiers:takeAccessibilityAssertion:shouldDefer:completion:]_block_invoke.325
+ ___113-[HDSeriesQuantityDataAggregator aggregateForState:collector:device:requestedAggregationDate:mode:options:error:]_block_invoke.322
+ ___113-[HDSeriesQuantityDataAggregator aggregateForState:collector:device:requestedAggregationDate:mode:options:error:]_block_invoke_2.323
+ ___115+[HDObjectAuthorizationEntity _setObjectAuthorizationRecords:syncProvenance:syncIdentity:skipErrors:profile:error:]_block_invoke.348
+ ___115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.454
+ ___115-[HDCloudSyncHandleMissingManateeIdentityOperation _deleteZonesForLostManateeIdentitiesInZones:container:database:]_block_invoke.318
+ ___115-[HDCloudSyncHandleMissingManateeIdentityOperation _leaveSharesForLostManateeIdentitiesInZones:container:database:]_block_invoke.323
+ ___116-[HDCloudSyncPushReferenceTombstonesOperation _generateTombstoneRecordsToPushAndReferencesRecordsToDeleteWithError:]_block_invoke.304
+ ___117+[HDLogicalSourceEntity lookUpOrCreateLogicalSourceWithBundleIdentifier:owningAppBundleIdentifier:transaction:error:]_block_invoke.358
+ ___117+[HDLogicalSourceEntity lookUpOrCreateLogicalSourceWithBundleIdentifier:owningAppBundleIdentifier:transaction:error:]_block_invoke_2.362
+ ___119-[HDInsertSharedSummaryTransactionOperation _persistRecordsWithRepository:transactionRecord:summaryRecords:completion:]_block_invoke.333
+ ___120-[HDCloudSyncSharedSummaryPushPruningOperation _findTransactionsToDelete:existingTransactionRecordsByZoneID:completion:]_block_invoke.309
+ ___122-[HDAuthorizationManager handleHealthConceptAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.477
+ ___122-[HDSharingAuthorizationRecipientStoreServer sharingAuthorizationManager:didAddSharingAuthorizations:recipientIdentifier:]_block_invoke.302
+ ___123-[HDDefaultAuthorizationSchemaProvider setAuthorizationStatuses:authorizationModes:bundleIdentifier:options:profile:error:]_block_invoke.323
+ ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.319
+ ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.324
+ ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.326
+ ___123-[HDSecondaryDevicePairingAgentTaskServer remote_requestTinkerSharingOptInWithGuardianDisplayName:NRDeviceUUID:completion:]_block_invoke.308
+ ___125-[HDSharingAuthorizationRecipientStoreServer sharingAuthorizationManager:didRemoveSharingAuthorizations:recipientIdentifier:]_block_invoke.304
+ ___127-[HDClientAuthorizationOracle(Privileged) _queue_beginAuthorizationRequestDelegateTransactionWithSessionIdentifier:completion:]_block_invoke.507
+ ___130+[HDDeviceKeyValueStorageEntryEntity setData:forKey:domain:deviceContextID:syncEntityIdentity:modificationDate:transaction:error:]_block_invoke.355
+ ___133-[HDClientAuthorizationOracle enqueueAuthorizationRequestToWriteTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke.427
+ ___134-[HDAuthorizationManager _authorizationRequestStatusForClientBundleIdentifier:writeTypes:readTypes:updateAuthorizationStatuses:error:]_block_invoke.410
+ ___135-[HDNanoSyncManager _queue_synchronizeWithOptions:restoreMessagesSentHandler:targetSyncStore:reason:accessibilityAssertion:completion:]_block_invoke.515
+ ___135-[HDNanoSyncManager _queue_synchronizeWithOptions:restoreMessagesSentHandler:targetSyncStore:reason:accessibilityAssertion:completion:]_block_invoke.523
+ ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.351
+ ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.352
+ ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.353
+ ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.355
+ ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.356
+ ___151-[HDCloudSyncSharedSummaryParticipantProfileCreationOperation _createProfileWithUUID:contactIdentifier:firstName:lastName:ownerParticipant:completion:]_block_invoke.303
+ ___151-[HDCloudSyncSharedSummaryParticipantProfileCreationOperation _createProfileWithUUID:contactIdentifier:firstName:lastName:ownerParticipant:completion:]_block_invoke_2.304
+ ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke.310
+ ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke.316
+ ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke_2.313
+ ___162+[HDWorkoutZonesAssociationEntity _insertAssociationsForZonesSamplesWithUUIDs:withWorkoutUUID:syncProvenance:syncIdentity:ignoreDeletedObjects:transaction:error:]_block_invoke.344
+ ___185-[HDWorkoutTrainingLoadDataSource _queryEffortSampleValuesForWorkoutUUID:workoutPID:workoutStartDate:workoutEndDate:workoutActivityType:workoutDuration:sourceID:activity:sampleHandler:]_block_invoke.335
+ ___186-[HDCloudSyncSharedSummaryPushOperation createRecordsToSaveWithTransactions:transactionRecords:participantZoneID:participant:authorizationIdentifiers:allRecordsToSave:zoneIDs:taskGroup:]_block_invoke.320
+ ___191+[HDAssociationEntity _insertEntriesWithParentUUID:childUUIDsData:provenance:syncIdentity:type:behavior:deleted:creationDate:destinationSubObjectReference:lastInsertedEntityID:context:error:]_block_invoke.437
+ ___248+[HDDataProvenanceEntity insertOrLookupDataProvenanceForSyncProvenance:syncIdentity:originProductType:originSystemBuild:originOSVersion:localProductType:localSystemBuild:sourceVersion:timeZoneName:sourceID:deviceID:contributorID:transaction:error:]_block_invoke.406
+ ___32-[HDBiomeInterface sleepFocusOn]_block_invoke.307
+ ___35-[HDDeviceQueryServer _queue_start]_block_invoke.306
+ ___35-[HDDeviceQueryServer _queue_start]_block_invoke_2.317
+ ___36-[HDCacheDeleteCoordinator activate]_block_invoke.305
+ ___36-[HDCacheDeleteCoordinator activate]_block_invoke.306
+ ___36-[HDCacheDeleteCoordinator activate]_block_invoke.308
+ ___36-[HDCloudSyncPipelineStagePush main]_block_invoke.313
+ ___37-[HDCloudSyncStateSyncOperation main]_block_invoke.310
+ ___38-[HDDaemon _setupMemoryWarningHandler]_block_invoke.474
+ ___39-[HDCloudSyncCreateZonesOperation main]_block_invoke.308
+ ___39-[HDIDSPersistentDictionary didCancel:]_block_invoke.436
+ ___40-[HDCloudSyncAcceptSharesOperation main]_block_invoke.307
+ ___40-[HDDataProvenanceManager _loadDefaults]_block_invoke.322
+ ___41-[HDCloudSyncPipeline beginWithTaskTree:]_block_invoke.391
+ ___41-[HDCloudSyncPipeline beginWithTaskTree:]_block_invoke.393
+ ___41-[HDCloudSyncPipelineStageStateSync main]_block_invoke.311
+ ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke.377
+ ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke.380
+ ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke_2.379
+ ___42-[HDCloudSyncDeleteSequenceOperation main]_block_invoke.307
+ ___42-[HDCloudSyncDeleteSequenceOperation main]_block_invoke.308
+ ___42-[HDCloudSyncLeaveAllSharesOperation main]_block_invoke.302
+ ___42-[HDCloudSyncPullReferencesOperation main]_block_invoke.307
+ ___42-[HDProfileManager _loadSecondaryProfiles]_block_invoke.342
+ ___43-[HDWorkoutBuilderServer _didUpdateEvents:]_block_invoke.625
+ ___44-[HDCloudSyncPullChangeRecordOperation main]_block_invoke.315
+ ___44-[HDStaticSyncExportTask runWithCompletion:]_block_invoke.328
+ ___45-[HDAppLauncher _queue_launchClientIfNeeded:]_block_invoke.311
+ ___45-[HDCloudSyncLookupParticipantOperation main]_block_invoke.307
+ ___45-[HDCloudSyncPrepareForSharingOperation main]_block_invoke.305
+ ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.307
+ ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.309
+ ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.315
+ ___45-[HDCloudSyncSharedSummaryPushOperation main]_block_invoke.302
+ ___45-[HDHFDataStore _lock_restoreHFDFromArchive:]_block_invoke.412
+ ___45-[HDWorkoutBuilderServer _didUpdateMetadata:]_block_invoke.615
+ ___45-[HDWorkoutRouteDataSource elevationUpdated:]_block_invoke.430
+ ___46-[HDCloudSyncDeleteStoreOnChildOperation main]_block_invoke.304
+ ___46-[HDCloudSyncDisableSyncLocallyOperation main]_block_invoke.304
+ ___46-[HDCloudSyncPushDeviceKeyValueOperation main]_block_invoke.312
+ ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke.316
+ ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke.318
+ ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke_2.322
+ ___46-[HDCloudSyncStatusProvider checkLastSyncDate]_block_invoke.345
+ ___46-[HDDaemon registerDaemonReadyObserver:queue:]_block_invoke.485
+ ___46-[HDSyncIdentityManager profileDidInitialize:]_block_invoke.368
+ ___46-[HDWorkoutSessionServer didBeginNewActivity:]_block_invoke.634
+ ___46-[_HDAWDPeriodicAction _doIfWaitingWithError:]_block_invoke.356
+ ___47-[HDAgeGatingManager _registerForNotifications]_block_invoke.321
+ ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke.306
+ ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke.310
+ ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke_2.308
+ ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke_2.311
+ ___47-[HDCloudSyncPipelineStageContextSyncPush main]_block_invoke.312
+ ___47-[HDWorkoutBuilderServer _didUpdateStatistics:]_block_invoke.664
+ ___47-[HDWorkoutSessionServer _queue_generateError:]_block_invoke.720
+ ___47-[HDWorkoutSessionServer _queue_generateEvent:]_block_invoke.714
+ ___47-[HDWorkoutSessionServer _queue_generateEvent:]_block_invoke.717
+ ___48-[HDCloudSyncPipeline _queue_runStage:taskTree:]_block_invoke.408
+ ___48-[HDCloudSyncPipeline _queue_runStage:taskTree:]_block_invoke.410
+ ___48-[HDWorkoutSessionServer didEndCurrentActivity:]_block_invoke.640
+ ___48-[HDWorkoutSessionServer syncSessionEvent:date:]_block_invoke.684
+ ___49-[HDCloudSyncAddSharingParticipantOperation main]_block_invoke.321
+ ___49-[HDCloudSyncAddSharingParticipantOperation main]_block_invoke.322
+ ___49-[HDCloudSyncMarkAllOwnersDisabledOperation main]_block_invoke.305
+ ___49-[HDCloudSyncRegisterSubscriptionsOperation main]_block_invoke.305
+ ___49-[HDWorkoutSessionServer remoteSessionDidRecover]_block_invoke.685
+ ___50-[HDAppSubscriptionManager profileDidBecomeReady:]_block_invoke.324
+ ___50-[HDCloudSyncPipelineStageDisableSyncLocally main]_block_invoke.301
+ ___50-[HDDaemon registerDaemonActivatedObserver:queue:]_block_invoke.486
+ ___50-[HDDataCollectionManager _dataCollectorBlacklist]_block_invoke.426
+ ___51-[HDQueryManager _lock_executeDatabaseAccessBlocks]_block_invoke.323
+ ___52-[HDCloudSyncSharedSummaryPushPrepareOperation main]_block_invoke.301
+ ___52-[HDDemoDataManager _queue_generateDemoDataIfNeeded]_block_invoke.306
+ ___52-[HDLiveWorkoutDataSource addQuantities:dataSource:]_block_invoke.425
+ ___52-[HDLiveWorkoutDataSource addQuantities:dataSource:]_block_invoke_2.426
+ ___52-[HDSeriesBuilderServer _setClientState:completion:]_block_invoke.333
+ ___52-[HDWorkoutBasicDataSource setSampleTypesToCollect:]_block_invoke.425
+ ___52-[HDWorkoutLocationSmoother _queue_smoothNextSample]_block_invoke.402
+ ___53-[HDCloudSyncResetOperation _deleteZonesWithZoneIDs:]_block_invoke.302
+ ___54-[HDCloudSyncCachedZone recordsForClass:error:filter:]_block_invoke.343
+ ___54-[HDCloudSyncCachedZone recordsForClass:error:filter:]_block_invoke_2.344
+ ___54-[HDDataManager _addTransactionInsertionCommitBlocks:]_block_invoke.332
+ ___54-[HDPeriodicCountryMonitor _processCountryCodeResult:]_block_invoke.357
+ ___55-[HDCloudSyncCachedZone recordForRecordID:class:error:]_block_invoke.353
+ ___55-[HDCloudSyncCachedZone recordForRecordID:class:error:]_block_invoke_2.354
+ ___55-[HDCloudSyncManager _persistErrorRequiringUserAction:]_block_invoke.464
+ ___55-[HDFeatureAvailabilityManager registerObserver:queue:]_block_invoke.422
+ ___55-[HDQueryServer authorizedSamplesForClientWithSamples:]_block_invoke.390
+ ___55-[HDWorkoutBuilderServer remote_addSamples:completion:]_block_invoke.585
+ ___55-[HDWorkoutBuilderServer remote_recoverWithCompletion:]_block_invoke.614
+ ___55-[HDWorkoutSessionServer _queue_startInvalidationTimer]_block_invoke.731
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke.381
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_2.385
+ ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_3.389
+ ___56-[HDWorkoutBuilderServer remote_addMetadata:completion:]_block_invoke.589
+ ___56-[HDWorkoutSessionTaskServer didEndActivity:dataSource:]_block_invoke.444
+ ___57-[HDAppExtensionAssertion assertAndUpdateWithCompletion:]_block_invoke.309
+ ___57-[HDAppExtensionAssertion assertAndUpdateWithCompletion:]_block_invoke.310
+ ___57-[HDAppExtensionAssertion assertAndUpdateWithCompletion:]_block_invoke.312
+ ___57-[HDWorkoutSessionServer endCurrentActivityOnDate:error:]_block_invoke.655
+ ___58-[HDCloudSyncDeleteZonesOperation _deleteZones:container:]_block_invoke.314
+ ___58-[HDCloudSyncDeleteZonesOperation _deleteZones:container:]_block_invoke.316
+ ___58-[HDCloudSyncRemoveInvalidShareParticipantsOperation main]_block_invoke.313
+ ___58-[HDNanoSyncManager _queue_generateWatchActivationSamples]_block_invoke.561
+ ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke.668
+ ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke_2.669
+ ___58-[HDWorkoutSessionTaskServer addWorkoutEvents:dataSource:]_block_invoke.441
+ ___58-[HDWorkoutSessionTaskServer didBeginActivity:dataSource:]_block_invoke.443
+ ___59+[HDConceptIndexer _indexSample:profile:transaction:error:]_block_invoke.404
+ ___59-[HDCloudSyncStatusProvider fetchSyncStatusWithCompletion:]_block_invoke.308
+ ___59-[HDCloudSyncStatusProvider fetchSyncStatusWithCompletion:]_block_invoke.310
+ ___59-[HDFakeDataCollector _lock_setupSwimmingGeneratorsAtTime:]_block_invoke.333
+ ___59-[HDWorkoutBuilderServer remote_removeMetadata:completion:]_block_invoke.594
+ ___59-[HDWorkoutSessionTaskServer remote_recoverWithCompletion:]_block_invoke.427
+ ___60+[HDSampleEntity dateIntervalsForSampleTypes:profile:error:]_block_invoke.406
+ ___60-[HDCloudSyncDeleteStoresOperation _individualZonesToDelete]_block_invoke.306
+ ___60-[HDCloudSyncSubscriptionNotificationHandler _enableAPSPush]_block_invoke.307
+ ___60-[HDMirroredWorkoutSessionServer setTargetState:date:error:]_block_invoke.346
+ ___60-[HDStatisticsCollectionQueryServer _queue_updateStatistics]_block_invoke.387
+ ___60-[HDSummarySharingEntryStoreServer sharingEntriesDidUpdate:]_block_invoke.307
+ ___61-[HDCloudSyncDetectSyncDisabledOperation _disableSyncLocally]_block_invoke.309
+ ___61-[HDCloudSyncManagerPipelineTask mainWithRepositories:error:]_block_invoke.313
+ ___61-[HDDatabase _mergeSecondaryJournalsWithActivity:completion:]_block_invoke.585
+ ___61-[HDDatabaseMigrator(Tigris) _updateOriginVersionsWithError:]_block_invoke.432
+ ___61-[HDWorkoutBuilderServer remote_addWorkoutEvents:completion:]_block_invoke.587
+ ___61-[HDWorkoutSessionServer _queue_generateConfigurationUpdate:]_block_invoke.721
+ ___62-[HDCloudSyncSharedSummarySynchronizeCloudStateOperation main]_block_invoke.307
+ ___62-[HDUserCharacteristicsManager _queue_updateHasWatchOnAccount]_block_invoke.376
+ ___62-[HDWorkoutSessionServer _processTargetStoppingStateWithDate:]_block_invoke.596
+ ___63-[HDHealthStoreServer remote_deleteClientSourceWithCompletion:]_block_invoke.475
+ ___63-[HDStatisticsCollectionQueryServer _queue_useCachedStatistics]_block_invoke.417
+ ___63-[HDWorkoutBuilderServer remote_addWorkoutActivity:completion:]_block_invoke.603
+ ___63-[HDWorkoutSessionTaskServer didDisconnectFromRemoteWithError:]_block_invoke.448
+ ___64-[CMPedometer(HealthDaemon) hd_beginStreamingFromDatum:handler:]_block_invoke.392
+ ___64-[CMPedometer(HealthDaemon) hd_beginStreamingFromDatum:handler:]_block_invoke.394
+ ___64-[HDCloudSyncComputePullTargetsOperation _pullTargetsWithError:]_block_invoke.310
+ ___64-[HDCloudSyncManager cloudSyncRepositoriesForClient:completion:]_block_invoke.435
+ ___64-[HDCloudSyncModifyRecordsOperation _saveRecords:deleteRecords:]_block_invoke.324
+ ___64-[HDFeatureAvailabilityManager _triggerImmediateSyncWithReason:]_block_invoke.421
+ ___64-[HDNanoSyncManager _queue_receiveTinkerOptInRequest:syncStore:]_block_invoke.830
+ ___64-[HDNanoSyncManager _scheduleResetReceivedNanoSyncAnchorsForHFD]_block_invoke.938
+ ___64-[HDNotificationManager postNotificationWithRequest:completion:]_block_invoke.333
+ ___64-[HDPeriodicCountryMonitor _fetchCountryIfNeededWithCompletion:]_block_invoke.341
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.548
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.556
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.561
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.571
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.572
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.552
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.557
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.563
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.560
+ ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.564
+ ___64-[HDWorkoutSessionTaskServer _fetchOrSetupServerWithCompletion:]_block_invoke.460
+ ___65-[HDCloudSyncCoordinator resetAllProfilesWithContext:completion:]_block_invoke.410
+ ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.320
+ ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.336
+ ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke_2.322
+ ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke_2.329
+ ___65-[HDDatabaseCorruptionTTRPrompter _popAlertWithRadarDescription:]_block_invoke.333
+ ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.337
+ ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.338
+ ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke_2.339
+ ___65-[HDSourceOrderManager updateOrderedSources:forObjectType:error:]_block_invoke.318
+ ___65-[HDSyncIdentityManager rollCurrentSyncIdentityWithReason:error:]_block_invoke.362
+ ___65-[HDWorkoutSessionRapportSyncController _sendPendingTransactions]_block_invoke.371
+ ___66+[HDWorkoutCondenser _condenseWorkout:entity:configuration:error:]_block_invoke.353
+ ___66-[HDClientDataCollectionTaskServer remote_registerWithCompletion:]_block_invoke.321
+ ___66-[HDCloudSyncPullReferencesOperation _fetchAttachmentRecordAssets]_block_invoke.317
+ ___66-[HDCloudSyncPullReferencesOperation _fetchAttachmentRecordAssets]_block_invoke.319
+ ___66-[HDCloudSyncStateSyncOperation _pushUpdatedStateRecordsForZones:]_block_invoke.334
+ ___66-[HDCoreMotionDataCollector _queue_forwardCoreMotionData:forType:]_block_invoke.318
+ ___66-[HDCoreMotionDataCollector _queue_forwardCoreMotionData:forType:]_block_invoke.320
+ ___66-[HDHealthStoreServer _holdActiveClientTransactionWithCompletion:]_block_invoke.498
+ ___66-[HDMedicalIDDataManager _triggerSyncForSuccessfulMedicalIDUpdate]_block_invoke.338
+ ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.920
+ ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.921
+ ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.923
+ ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke_2.925
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.857
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.872
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.874
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.880
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.882
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.884
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.886
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.888
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.890
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.885
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.887
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.889
+ ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.891
+ ___66-[HDWorkoutBuilderSampleQueryServer _queue_performHistoricalQuery]_block_invoke.318
+ ___67-[HDCloudSyncAcceptSharesOperation _acceptSharesWithShareMetadata:]_block_invoke.315
+ ___67-[HDMirroredWorkoutSessionServer didDisconnectFromRemoteWithError:]_block_invoke.332
+ ___68-[HDHealthStoreServer remote_setCharacteristic:forDataType:handler:]_block_invoke.483
+ ___68-[HDLocationSeriesSampleEntity freezeWithTransaction:profile:error:]_block_invoke.347
+ ___68-[HDLocationSeriesSampleEntity freezeWithTransaction:profile:error:]_block_invoke.349
+ ___68-[HDNanoSyncManager _queue_recieveStartWorkoutAppRequest:syncStore:]_block_invoke.805
+ ___68-[HDProcessStateManager _lock_registerObserver:forBundleIdentifier:]_block_invoke.319
+ ___68-[HDWorkoutManager recoverAllActiveWorkoutSessionServersWithStates:]_block_invoke.399
+ ___68-[HDWorkoutSessionTaskServer updateWorkoutConfiguration:dataSource:]_block_invoke.442
+ ___69-[HDCloudSyncStateSyncOperation _performStateSyncInZones:completion:]_block_invoke.322
+ ___69-[HDDaemon obliterateAndTerminateProfiles:options:reason:completion:]_block_invoke.373
+ ___70-[HDCloudSyncManager _queue_considerStartingBackstopSyncForThreshold:]_block_invoke.468
+ ___70-[HDDemoDataGenerator _insertIntoDatabaseObjectCollection:fromPerson:]_block_invoke.398
+ ___70-[HDDemoDataGenerator _insertIntoDatabaseObjectCollection:fromPerson:]_block_invoke.401
+ ___70-[HDNanoSyncManager _queue_receiveChangeRequest:syncStore:completion:]_block_invoke.680
+ ___70-[HDSummarySharingEntryIDSManager leaveInvitationWithUUID:completion:]_block_invoke.381
+ ___71-[HDBackgroundObservationServerExtension connectWithCompletionHandler:]_block_invoke.321
+ ___71-[HDCloudSyncCoordinator _queue_syncAllProfilesWithContext:completion:]_block_invoke.387
+ ___71-[HDCloudSyncCoordinator _queue_syncAllProfilesWithContext:completion:]_block_invoke_2.388
+ ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.371
+ ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.372
+ ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.373
+ ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.374
+ ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.375
+ ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.376
+ ___71-[HDSummarySharingEntryIDSManager revokeInvitationWithUUID:completion:]_block_invoke.379
+ ___71-[HDSummarySharingEntryIDSManager revokeInvitationWithUUID:completion:]_block_invoke.380
+ ___71-[HDWorkoutSessionServer stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.673
+ ___72-[HDCloudSyncAccountProvider disableAndDeleteAllSyncDataWithCompletion:]_block_invoke.315
+ ___72-[HDCloudSyncAccountProvider disableAndDeleteAllSyncDataWithCompletion:]_block_invoke.317
+ ___72-[HDCloudSyncCachedZone recordsForClass:epoch:error:enumerationHandler:]_block_invoke.338
+ ___72-[HDCloudSyncCachedZone recordsForClass:epoch:error:enumerationHandler:]_block_invoke_2.339
+ ___72-[HDCloudSyncDeleteStoresOperation _deleteUnifiedZoneStoresInContainer:]_block_invoke.324
+ ___72-[HDCloudSyncDeleteStoresOperation _deleteUnifiedZoneStoresInContainer:]_block_invoke.331
+ ___72-[HDCloudSyncPipeline _queue_waitForCloudKitOperationDelayWithTaskTree:]_block_invoke.415
+ ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.431
+ ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.432
+ ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.434
+ ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.435
+ ___72-[HDMirroredWorkoutSessionServer syncTransitionToState:date:completion:]_block_invoke.336
+ ___72-[HDStatisticsCollectionQueryServer _queue_fetchAndDeliverAllStatistics]_block_invoke.404
+ ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.409
+ ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.410
+ ___73-[HDCloudSyncAccountProvider _performSyncForAccountChangeWithCompletion:]_block_invoke.346
+ ___73-[HDCloudSyncPeriodicActivityScheduler performInitialRestore:completion:]_block_invoke.331
+ ___73-[HDCloudSyncPushReferencesOperation _pushToCloudKitAndFinishForRecords:]_block_invoke.317
+ ___73-[HDCoreMotionDataCollector _queue_beginUpdatesWithTargetCollectionType:]_block_invoke.329
+ ___73-[HDNanoSyncManager _syncQueue_prepareForCompanionChangeWithStore:error:]_block_invoke.605
+ ___73-[HDWorkoutMirroringManager recoverMirroredWorkoutSessionWithCompletion:]_block_invoke.346
+ ___73-[HDWorkoutMirroringManager recoverMirroredWorkoutSessionWithCompletion:]_block_invoke.347
+ ___74+[HDSeriesSampleEntity freezeSeriesWithIdentifier:metadata:profile:error:]_block_invoke.339
+ ___74-[HDAnalyticsSubmissionCoordinator _locked_sendDailyAnalyticsWithTimeout:]_block_invoke.342
+ ___74-[HDAnalyticsSubmissionCoordinator _locked_sendDailyAnalyticsWithTimeout:]_block_invoke.345
+ ___74-[HDAnalyticsSubmissionCoordinator _locked_sendDailyAnalyticsWithTimeout:]_block_invoke_2.347
+ ___74-[HDDataAggregator requestAggregationThroughDate:mode:options:completion:]_block_invoke.308
+ ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.312
+ ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.315
+ ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.316
+ ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.319
+ ___74-[HDWorkoutBuilderServer _lock_recoverPersistedDataWithTransaction:error:]_block_invoke.518
+ ___75-[HDCloudSyncObserverTaskServer _queue_instantiateCloudSyncObserverStatus:]_block_invoke.368
+ ___75-[HDCloudSyncObserverTaskServer _queue_instantiateCloudSyncObserverStatus:]_block_invoke_2.369
+ ___75-[HDCloudSyncUpdateCachedZonesOperation fetchChangesForContainer:database:]_block_invoke.308
+ ___75-[HDCoreMotionDataCollector _didReceiveCoreMotionData:startingDatum:error:]_block_invoke.324
+ ___75-[HDCurrentActivitySummaryHelper _handleSignificantTimeChangeNotification:]_block_invoke.319
+ ___75-[HDWorkoutBasicDataSource workoutSession:didChangeToState:fromState:date:]_block_invoke.452
+ ___75-[HDWorkoutBuilderServer remote_updateActivityWithUUID:endDate:completion:]_block_invoke.611
+ ___76-[HDActiveDataAggregator dataCollector:didCollectSensorData:device:options:]_block_invoke.324
+ ___76-[HDNanoSyncManager _queue_receiveTinkerEndToEndCloudSyncRequest:syncStore:]_block_invoke.904
+ ___76-[HDWorkoutSessionServer didReceiveDataFromRemoteWorkoutSession:completion:]_block_invoke.680
+ ___77+[HDDataEntity insertDataObjects:insertionContext:profile:completionHandler:]_block_invoke.464
+ ___77-[HDDeleteAttachmentReferenceOperation performWithProfile:transaction:error:]_block_invoke.309
+ ___78+[HDDeletedSampleEntity insertCodableDeletedSamples:provenance:profile:error:]_block_invoke.376
+ ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.442
+ ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.447
+ ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.448
+ ___78-[HDCloudSyncRemoveSharingParticipantsOperation _saveUpdatedShares:container:]_block_invoke.308
+ ___78-[HDCloudSyncSeizeAbandonedStoresOperation _markPendingOwnerForSeizureTargets]_block_invoke.323
+ ___78-[HDDatabaseMigrator(Monarch) _fixProvenancesWithZeroSourceOrDeviceWithError:]_block_invoke.626
+ ___78-[HDDatabaseMigrator(Monarch) _fixProvenancesWithZeroSourceOrDeviceWithError:]_block_invoke_2.627
+ ___78-[HDNanoSyncManager _queue_recieveCompanionUserNotificationRequest:syncStore:]_block_invoke.816
+ ___79-[HDCloudSyncManager configureForShareSetupMetadata:acceptedShares:completion:]_block_invoke.476
+ ___79-[HDCloudSyncManager configureForShareSetupMetadata:acceptedShares:completion:]_block_invoke.483
+ ___79-[HDCloudSyncRepairRegistryRecordsOperation _modifyRecordsAndFinish:container:]_block_invoke.307
+ ___79-[HDDatabaseTransaction performWithContext:error:block:inaccessibilityHandler:]_block_invoke.331
+ ___79-[HDPostInstallUpdateManager _triggerMigrationForProfile:protected:completion:]_block_invoke.327
+ ___79-[HDWorkoutBuilderServer remote_updateActivityWithUUID:addMetadata:completion:]_block_invoke.613
+ ___79-[HDWorkoutClusterServer remote_generateRaceRouteClustersWithLimit:completion:]_block_invoke.310
+ ___80-[HDCloudSyncCoordinator _queue_syncProfilesWithIdentifiers:context:completion:]_block_invoke.392
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke.323
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke.344
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_2.324
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_2.347
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_3.334
+ ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_4.338
+ ___80-[HDSecondaryDevicePairingAgentTaskServer _prepareGuardianForSharingForRequest:]_block_invoke.363
+ ___80-[HDWorkoutSessionServer beginNewActivityWithConfiguration:date:metadata:error:]_block_invoke.654
+ ___81-[HDDatabaseMigrator(Emet) _emet_migrateWorkoutEventMetadataToProtobufWithError:]_block_invoke.330
+ ___81-[HDHealthStoreServer remote_setBackgroundDeliveryFrequency:forDataType:handler:]_block_invoke.462
+ ___81-[HDWorkoutSessionRapportSyncController sendRequest:transaction:responseHandler:]_block_invoke.363
+ ___82-[HDCloudSyncManager _primaryContainerIdentifiersForCurrentAccountWithCompletion:]_block_invoke.453
+ ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.550
+ ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.551
+ ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.553
+ ___82-[HDDatabase _old_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.556
+ ___82-[HDWorkoutSessionServer enableAutomaticDetectionForActivityConfigurations:error:]_block_invoke.657
+ ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.607
+ ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.615
+ ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.618
+ ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.619
+ ___83-[HDCloudSyncManager _scheduleResetReceivedCloudSyncAnchorsAndRebaseForHFDRecovery]_block_invoke.376
+ ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke.343
+ ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke.346
+ ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke_2.349
+ ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke_3.351
+ ___83-[HDDeviceKeyValueStoreManager _deleteRemoteEntries:deviceContextByIdentity:error:]_block_invoke.327
+ ___83-[HDWorkoutBuilderServer _addSamples:quantities:dataSource:shouldSavePriorToStart:]_block_invoke.531
+ ___83-[HDWorkoutBuilderServer _addSamples:quantities:dataSource:shouldSavePriorToStart:]_block_invoke_2.533
+ ___84-[HDCloudSyncPreparePushZoneForStoreOperation _createZoneWithIdentifier:forStoreId:]_block_invoke.317
+ ___84-[HDWorkoutLocationSmoother _queue_smoothActivity:activityIndex:forTask:completion:]_block_invoke.409
+ ___84-[HDWorkoutLocationSmoother _queue_smoothActivity:activityIndex:forTask:completion:]_block_invoke.410
+ ___85-[HDWorkoutMirroringManager rapportMessenger:didReceiveRequest:data:responseHandler:]_block_invoke.323
+ ___86-[HDCloudSyncMedicalIDPushOperation _pushMedicalIDRecordToCloudForContainer:database:]_block_invoke.308
+ ___87-[HDCloudSyncFetchRecordsOperation _fetchRecordsWithIDs:container:database:completion:]_block_invoke.307
+ ___87-[HDCloudSyncPushDeviceKeyValueOperation _computeRecordsToSaveAndDeleteWithCompletion:]_block_invoke.318
+ ___87-[HDDataCollectionManager _requestAggregationThroughDate:type:mode:options:completion:]_block_invoke.380
+ ___87-[HDHealthStoreServer remote_requestConceptReadAuthorizationForType:filter:completion:]_block_invoke.375
+ ___87-[HDHealthStoreServer remote_requestConceptReadAuthorizationForType:filter:completion:]_block_invoke.378
+ ___87-[HDInsertSharedSummaryTransactionOperation performWithProfile:transaction:completion:]_block_invoke.303
+ ___87-[HDWorkoutEventsManager requestPendingEventsThroughDate:sessionIdentifier:completion:]_block_invoke.316
+ ___87-[HDWorkoutEventsManager requestPendingEventsThroughDate:sessionIdentifier:completion:]_block_invoke.318
+ ___88-[HDCloudSyncPushDeviceContextOperation _updateRecordsAdd:recordIDsToDelete:completion:]_block_invoke.322
+ ___88-[HDDataCollectionManager _requestAggregationThroughDate:types:mode:options:completion:]_block_invoke.379
+ ___88-[HDWorkoutSessionTaskServer remote_recoverAllActiveSessionsWithStates:date:completion:]_block_invoke.429
+ ___88-[HDWorkoutSessionTaskServer remote_recoverAllActiveSessionsWithStates:date:completion:]_block_invoke.430
+ ___89+[HDUserDomainConceptSyncEntity receiveSyncObjects:version:syncProvenance:profile:error:]_block_invoke.314
+ ___89-[HDCloudSyncComputePushTargetsOperation _pushTargetsForContainer:ownerIdentifier:error:]_block_invoke.317
+ ___89-[HDCloudSyncComputePushTargetsOperation _pushTargetsForContainer:ownerIdentifier:error:]_block_invoke.320
+ ___89-[HDHealthStoreServer remote_fetchModificationDateForCharacteristicWithDataType:handler:]_block_invoke.484
+ ___89-[HDHealthStoreServer remote_requestPerObjectReadAuthorizationForType:filter:completion:]_block_invoke.371
+ ___89-[HDHealthStoreServer remote_requestPerObjectReadAuthorizationForType:filter:completion:]_block_invoke.373
+ ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.582
+ ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.583
+ ___90+[HDLocationSeriesHFDMigrationEntity _migrateSeriesWithKey:toSQLFromStore:database:error:]_block_invoke.323
+ ___90+[HDQuantitySeriesHFDMigrationEntity _migrateSeriesWithKey:toSQLFromStore:database:error:]_block_invoke.310
+ ___90+[HDRaceRouteLocationSeriesEntity createRoutePointsFromWorkout:transaction:profile:error:]_block_invoke.334
+ ___90+[HDRaceRouteLocationSeriesEntity createRoutePointsFromWorkout:transaction:profile:error:]_block_invoke_2.336
+ ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.357
+ ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.361
+ ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.365
+ ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke_2.362
+ ___90-[HDCloudSyncObserverTaskServer remote_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.348
+ ___90-[HDCloudSyncPullChangeRecordOperation _persistFetchedArchiveAsset:protocolVersion:error:]_block_invoke.344
+ ___90-[HDCloudSyncPullChangeRecordOperation _persistFetchedArchiveAsset:protocolVersion:error:]_block_invoke.346
+ ___90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.376
+ ___90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.378
+ ___90-[HDCloudSyncSharedSummaryPushPruningOperation _modifyRecordsAndFinish:recordIDsToDelete:]_block_invoke.318
+ ___90-[HDDataAggregator persistForCollector:usedDatums:source:device:error:persistenceHandler:]_block_invoke.330
+ ___90-[HDDataAggregator persistForCollector:usedDatums:source:device:error:persistenceHandler:]_block_invoke.333
+ ___92+[HDLocationSeriesSampleEntity insertLocationData:seriesIdentifier:assertion:profile:error:]_block_invoke.319
+ ___92-[HDBatchedQueryServer batchObjectsWithEnumerator:includeDeletedObjects:error:batchHandler:]_block_invoke.306
+ ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke.356
+ ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke.357
+ ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke_2.358
+ ___92-[HDCloudSyncCoordinator(CloudSyncJournalMerge) _mergeCloudSyncJournalsForProfile:taskTree:]_block_invoke.310
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.316
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.322
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.323
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.326
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.327
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke_2.318
+ ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke_2.324
+ ___93+[HDMedicationDoseEventEntity _logPersistedDoseEventOnCommitDatabase:doseEvent:persistentID:]_block_invoke.396
+ ___93-[HDAppSubscriptionManager _updateObservationStatusForDataTypeCode:lastAppLaunchTimes:error:]_block_invoke.351
+ ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke.308
+ ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke.311
+ ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke_2.313
+ ___94-[HDIngestDeviceContextsOperation _pullDeviceContextsForProfile:repository:transaction:error:]_block_invoke.308
+ ___94-[HDRestorableAlarmScheduler _queue_notifyClientsOfDueEventsAndScheduleNextFireDateWithError:]_block_invoke.334
+ ___94-[HDWorkoutBasicDataSource _workoutDataDestination:requestsSamplesOfType:from:to:transaction:]_block_invoke.444
+ ___94-[HDWorkoutManager generatePauseOrResumeRequestAllowingBackgroundRuntime:metadata:completion:]_block_invoke.380
+ ___95+[HDAppSubscriptionAppLaunchEntity insertOrUpdateAppSDKVersionToken:forBundleID:profile:error:]_block_invoke.394
+ ___95-[HDCloudSyncPushReferenceTombstonesOperation _modifyCloudWithRecordsToSave:recordIDsToDelete:]_block_invoke.318
+ ___95-[HDDatabaseJournal _mergeJournalChapter:profile:accessibilityAssertion:shouldContinueHandler:]_block_invoke.374
+ ___95-[HDQueryControlServer queryServer:requestsAuthorizationWithContext:promptIfNeeded:completion:]_block_invoke.317
+ ___96-[HDTTRPromptController _presentTTRPromptForErrors:lastPromptBuild:lastPromptDate:currentBuild:]_block_invoke.371
+ ___97+[HDLogicalSourceOrderEntity updateOrderedLogicalSourcesForType:transaction:error:updateHandler:]_block_invoke.360
+ ___97+[HDLogicalSourceOrderEntity updateOrderedLogicalSourcesForType:transaction:error:updateHandler:]_block_invoke_2.361
+ ___97-[HDBackgroundObservationServerExtension notifyExtensionOfUpdateForSampleType:completionHandler:]_block_invoke.326
+ ___97-[HDHealthStoreServer remote_requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.383
+ ___97-[HDSecondaryDevicePairingAgentTaskServer _setupTinkerProfileForRequest:metadata:acceptedShares:]_block_invoke.371
+ ___Block_byref_object_copy_.316
+ ___Block_byref_object_copy_.322
+ ___Block_byref_object_copy_.332
+ ___Block_byref_object_copy_.334
+ ___Block_byref_object_copy_.337
+ ___Block_byref_object_copy_.339
+ ___Block_byref_object_copy_.379
+ ___Block_byref_object_dispose_.317
+ ___Block_byref_object_dispose_.323
+ ___Block_byref_object_dispose_.333
+ ___Block_byref_object_dispose_.335
+ ___Block_byref_object_dispose_.338
+ ___Block_byref_object_dispose_.340
+ ___Block_byref_object_dispose_.380
+ ____HDAddUniquenessChecksumToOriginalFHIRResourceEntity_block_invoke.1349
+ ____HDCopyWorkoutTotalsToPrimaryActivity_block_invoke.611
+ ____HDMigrateCycleTrackingOnboarding_block_invoke.975
+ ____HDMigrateCycleTrackingOnboarding_block_invoke_2.976
+ ____HDUpdateClinicalRecordEntities_block_invoke.901
+ ____HDUpdateClinicalRecordEntities_block_invoke_2.902
+ ____HDUpdateClinicalRecordEntities_block_invoke_3.906
+ ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke.987
+ ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke.991
+ ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke_2.992
+ ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke_3.996
+ ____ZL27_HDHFDataStoreWillOpenStoreP13HDHFDataStore_block_invoke.497
+ ___block_descriptor_56_ea8_32s40r48r_e275_v80?0B8{vector<std::tuple<long long, HKSample *>, std::allocator<std::tuple<long long, HKSample *>>>=^v^v{?=^v}}12{vector<std::tuple<long long, HKDeletedObject *>, std::allocator<std::tuple<long long, HKDeletedObject *>>>=^v^v{?=^v}}36"HKSortedQueryAnchor"60B68"NSError"72lr40l8s32l8r48l8
+ ___block_literal_global.1029
+ ___block_literal_global.1052
+ ___block_literal_global.1067
+ ___block_literal_global.1093
+ ___block_literal_global.1116
+ ___block_literal_global.1157
+ ___block_literal_global.307
+ ___block_literal_global.323
+ ___block_literal_global.337
+ ___block_literal_global.341
+ ___block_literal_global.343
+ ___block_literal_global.347
+ ___block_literal_global.349
+ ___block_literal_global.353
+ ___block_literal_global.355
+ ___block_literal_global.360
+ ___block_literal_global.363
+ ___block_literal_global.380
+ ___block_literal_global.383
+ ___block_literal_global.385
+ ___block_literal_global.386
+ ___block_literal_global.388
+ ___block_literal_global.396
+ ___block_literal_global.403
+ ___block_literal_global.404
+ ___block_literal_global.406
+ ___block_literal_global.408
+ ___block_literal_global.409
+ ___block_literal_global.411
+ ___block_literal_global.416
+ ___block_literal_global.419
+ ___block_literal_global.422
+ ___block_literal_global.426
+ ___block_literal_global.436
+ ___block_literal_global.438
+ ___block_literal_global.442
+ ___block_literal_global.444
+ ___block_literal_global.446
+ ___block_literal_global.448
+ ___block_literal_global.450
+ ___block_literal_global.458
+ ___block_literal_global.470
+ ___block_literal_global.472
+ ___block_literal_global.473
+ ___block_literal_global.475
+ ___block_literal_global.478
+ ___block_literal_global.483
+ ___block_literal_global.485
+ ___block_literal_global.486
+ ___block_literal_global.488
+ ___block_literal_global.489
+ ___block_literal_global.502
+ ___block_literal_global.504
+ ___block_literal_global.506
+ ___block_literal_global.509
+ ___block_literal_global.514
+ ___block_literal_global.524
+ ___block_literal_global.529
+ ___block_literal_global.539
+ ___block_literal_global.558
+ ___block_literal_global.559
+ ___block_literal_global.571
+ ___block_literal_global.578
+ ___block_literal_global.581
+ ___block_literal_global.583
+ ___block_literal_global.594
+ ___block_literal_global.598
+ ___block_literal_global.609
+ ___block_literal_global.617
+ ___block_literal_global.621
+ ___block_literal_global.623
+ ___block_literal_global.627
+ ___block_literal_global.629
+ ___block_literal_global.633
+ ___block_literal_global.634
+ ___block_literal_global.639
+ ___block_literal_global.644
+ ___block_literal_global.645
+ ___block_literal_global.646
+ ___block_literal_global.651
+ ___block_literal_global.658
+ ___block_literal_global.662
+ ___block_literal_global.687
+ ___block_literal_global.688
+ ___block_literal_global.690
+ ___block_literal_global.706
+ ___block_literal_global.718
+ ___block_literal_global.720
+ ___block_literal_global.721
+ ___block_literal_global.722
+ ___block_literal_global.723
+ ___block_literal_global.726
+ ___block_literal_global.734
+ ___block_literal_global.745
+ ___block_literal_global.751
+ ___block_literal_global.780
+ ___block_literal_global.786
+ ___block_literal_global.802
+ ___block_literal_global.814
+ ___block_literal_global.836
+ ___block_literal_global.860
+ ___block_literal_global.901
+ ___block_literal_global.924
+ ___block_literal_global.925
+ ___block_literal_global.940
+ ___block_literal_global.944
+ ___block_literal_global.965
+ ___block_literal_global.988
+ __insertStatementKey.key.504
+ _columnDefinitionsWithCount:.HDDeviceKeyValueStorageEntryEntityColumnDefinitions.393
+ _columnDefinitionsWithCount:.columnDefinitions.405
- _.str.292
- _.str.296
- _.str.302
- __OBJC_$_PROP_LIST_HDCloudSyncStatusProvider.435
- ___100+[HDDataTypeSourceOrderEntity _updateOrderedSourcesForType:profile:transaction:error:updateHandler:]_block_invoke.348
- ___100+[HDDataTypeSourceOrderEntity _updateOrderedSourcesForType:profile:transaction:error:updateHandler:]_block_invoke_2.349
- ___100-[HDStaticSyncImportTask _queue_importStaticSyncChangesFromDirectory:syncStore:progress:completion:]_block_invoke.467
- ___101-[HDCloudSyncVerifyAttachmentManagementRecordOperation _modifyCloudKitAndFinishWithManagementRecord:]_block_invoke.299
- ___102-[HDDaemonSyncEngine _performSyncTransactionForSession:store:anchorRangeMap:transactionContext:error:]_block_invoke.470
- ___102-[HDDaemonSyncEngine _performSyncTransactionForSession:store:anchorRangeMap:transactionContext:error:]_block_invoke.473
- ___103-[HDCloudSyncSharedSummaryPushPrepareOperation _pendingAndAcceptedParticipantRecordsInZone:completion:]_block_invoke.299
- ___103-[HDExtendedDatabaseTransaction initWithDatabase:context:transactionTimeout:continuationTimeout:error:]_block_invoke.319
- ___103-[HDProtectedDataOperation _notifyDelegateToPerformWorkWithDatabase:accessibilityAssertion:completion:]_block_invoke.360
- ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.302
- ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.306
- ___104-[HDCloudSyncDeleteEmptyZonesOperation _validateZonesAreEmptyWithDeletionCandidates:container:database:]_block_invoke.314
- ___104-[HDCloudSyncPullChangeRecordOperation _continuationForFetchedRecord:recordID:inMemoryAsset:fetchError:]_block_invoke.312
- ___104-[HDCloudSyncPullChangeRecordOperation _continuationForFetchedRecord:recordID:inMemoryAsset:fetchError:]_block_invoke.313
- ___105-[HDDatabaseValidationTaskServer remote_validateDatabase:clientCompletionHandler:errorHandlerIdentifier:]_block_invoke.293
- ___105-[HDDatabaseValidationTaskServer remote_validateDatabase:clientCompletionHandler:errorHandlerIdentifier:]_block_invoke.295
- ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.302
- ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.305
- ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.310
- ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.313
- ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke.315
- ___105-[HDInsertSharedSummaryTransactionOperation _saveRecordsAndFinishWithProfile:repository:zone:completion:]_block_invoke_2.311
- ___106-[HDActivitySummaryBuilder _enumerateActivitySummariesAndCachesWithPredicate:largestAnchor:error:handler:]_block_invoke.307
- ___106-[HDBackgroundFeatureDeliveryManager periodicCountryMonitor:didFetchISOCountryCode:countryCodeProvenance:]_block_invoke.340
- ___106-[HDCloudSyncPipelineStageSharedSummaryAddParticipant _addParticipantWithLookupInfo:ownerName:ownerEmail:]_block_invoke.321
- ___106-[HDCloudSyncPipelineStageSharedSummaryAddParticipant _addParticipantWithLookupInfo:ownerName:ownerEmail:]_block_invoke.324
- ___106-[HDCloudSyncPipelineStageSharedSummaryAddParticipant _addParticipantWithLookupInfo:ownerName:ownerEmail:]_block_invoke_2.326
- ___107-[HDAppSubscriptionManager _updateSubscriptionsBasedOnBARSwitchState:lastLaunchTimes:dataCode:anchor:type:]_block_invoke.320
- ___107-[HDDemoDataFoodSampleGenerator generateObjectsForDemoPerson:fromTime:toTime:currentDate:objectCollection:]_block_invoke.370
- ___107-[HDNanoSyncManager _queue_performNextProactiveSyncWithRemainingDevices:accessibilityAssertion:completion:]_block_invoke.714
- ___108-[HDDatabaseValidationTaskServer remote_validateEntitiesWithClientCompletionHandler:errorHandlerIdentifier:]_block_invoke.297
- ___108-[HDIngestDeviceKeyValueEntriesOperation _pullDeviceKeyValueEntriesForProfile:repository:transaction:error:]_block_invoke.300
- ___109-[HDSecondaryDevicePairingAgentTaskServer remote_tearDownHealthSharingWithTinkerDeviceWithNRUUID:completion:]_block_invoke.338
- ___110-[HDWorkoutEffortRelationshipQueryServer associationsUpdatedForObject:subObject:type:behavior:objects:anchor:]_block_invoke.316
- ___111+[HDQuantitySampleValueEnumerator orderedQuantityValuesBySeriesForPredicate:transaction:options:error:handler:]_block_invoke.294
- ___112-[HDDatabasePruningCoordinator _pruneProfilesWithIdentifiers:takeAccessibilityAssertion:shouldDefer:completion:]_block_invoke.316
- ___113-[HDSeriesQuantityDataAggregator aggregateForState:collector:device:requestedAggregationDate:mode:options:error:]_block_invoke.313
- ___113-[HDSeriesQuantityDataAggregator aggregateForState:collector:device:requestedAggregationDate:mode:options:error:]_block_invoke_2.314
- ___115+[HDObjectAuthorizationEntity _setObjectAuthorizationRecords:syncProvenance:syncIdentity:skipErrors:profile:error:]_block_invoke.339
- ___115-[HDAuthorizationManager handleObjectAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.445
- ___115-[HDCloudSyncHandleMissingManateeIdentityOperation _deleteZonesForLostManateeIdentitiesInZones:container:database:]_block_invoke.309
- ___115-[HDCloudSyncHandleMissingManateeIdentityOperation _leaveSharesForLostManateeIdentitiesInZones:container:database:]_block_invoke.314
- ___116-[HDCloudSyncPushReferenceTombstonesOperation _generateTombstoneRecordsToPushAndReferencesRecordsToDeleteWithError:]_block_invoke.295
- ___117+[HDLogicalSourceEntity lookUpOrCreateLogicalSourceWithBundleIdentifier:owningAppBundleIdentifier:transaction:error:]_block_invoke.349
- ___117+[HDLogicalSourceEntity lookUpOrCreateLogicalSourceWithBundleIdentifier:owningAppBundleIdentifier:transaction:error:]_block_invoke_2.353
- ___119-[HDInsertSharedSummaryTransactionOperation _persistRecordsWithRepository:transactionRecord:summaryRecords:completion:]_block_invoke.324
- ___120-[HDCloudSyncSharedSummaryPushPruningOperation _findTransactionsToDelete:existingTransactionRecordsByZoneID:completion:]_block_invoke.300
- ___122-[HDAuthorizationManager handleHealthConceptAuthorizationRequestsForBundleIdentifier:objectType:promptHandler:completion:]_block_invoke.468
- ___122-[HDSharingAuthorizationRecipientStoreServer sharingAuthorizationManager:didAddSharingAuthorizations:recipientIdentifier:]_block_invoke.293
- ___123-[HDDefaultAuthorizationSchemaProvider setAuthorizationStatuses:authorizationModes:bundleIdentifier:options:profile:error:]_block_invoke.314
- ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.308
- ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.310
- ___123-[HDSecondaryDevicePairingAgentTaskServer remote_performEndToEndCloudSyncWithNRDeviceUUID:syncParticipantFirst:completion:]_block_invoke.315
- ___123-[HDSecondaryDevicePairingAgentTaskServer remote_requestTinkerSharingOptInWithGuardianDisplayName:NRDeviceUUID:completion:]_block_invoke.299
- ___125-[HDSharingAuthorizationRecipientStoreServer sharingAuthorizationManager:didRemoveSharingAuthorizations:recipientIdentifier:]_block_invoke.295
- ___127-[HDClientAuthorizationOracle(Privileged) _queue_beginAuthorizationRequestDelegateTransactionWithSessionIdentifier:completion:]_block_invoke.498
- ___130+[HDDeviceKeyValueStorageEntryEntity setData:forKey:domain:deviceContextID:syncEntityIdentity:modificationDate:transaction:error:]_block_invoke.346
- ___133-[HDClientAuthorizationOracle enqueueAuthorizationRequestToWriteTypes:readTypes:authorizationNeededHandler:requestCompletionHandler:]_block_invoke.418
- ___134-[HDAuthorizationManager _authorizationRequestStatusForClientBundleIdentifier:writeTypes:readTypes:updateAuthorizationStatuses:error:]_block_invoke.401
- ___135-[HDNanoSyncManager _queue_synchronizeWithOptions:restoreMessagesSentHandler:targetSyncStore:reason:accessibilityAssertion:completion:]_block_invoke.506
- ___135-[HDNanoSyncManager _queue_synchronizeWithOptions:restoreMessagesSentHandler:targetSyncStore:reason:accessibilityAssertion:completion:]_block_invoke.514
- ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.342
- ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.343
- ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.344
- ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.346
- ___138-[HDSummarySharingEntryIDSManager inviteSharingDataWithIdentifier:firstName:lastName:sharingAuthorizations:userWheelchairMode:completion:]_block_invoke.347
- ___151-[HDCloudSyncSharedSummaryParticipantProfileCreationOperation _createProfileWithUUID:contactIdentifier:firstName:lastName:ownerParticipant:completion:]_block_invoke.294
- ___151-[HDCloudSyncSharedSummaryParticipantProfileCreationOperation _createProfileWithUUID:contactIdentifier:firstName:lastName:ownerParticipant:completion:]_block_invoke_2.295
- ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke.301
- ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke.307
- ___158-[HDCloudSyncSharedSummaryPushOperation performSharedSummaryPushWithTransactions:pendingAndAcceptedParticipants:authorizationIdentifiers:privateMetadataZone:]_block_invoke_2.304
- ___162+[HDWorkoutZonesAssociationEntity _insertAssociationsForZonesSamplesWithUUIDs:withWorkoutUUID:syncProvenance:syncIdentity:ignoreDeletedObjects:transaction:error:]_block_invoke.335
- ___185-[HDWorkoutTrainingLoadDataSource _queryEffortSampleValuesForWorkoutUUID:workoutPID:workoutStartDate:workoutEndDate:workoutActivityType:workoutDuration:sourceID:activity:sampleHandler:]_block_invoke.326
- ___186-[HDCloudSyncSharedSummaryPushOperation createRecordsToSaveWithTransactions:transactionRecords:participantZoneID:participant:authorizationIdentifiers:allRecordsToSave:zoneIDs:taskGroup:]_block_invoke.311
- ___191+[HDAssociationEntity _insertEntriesWithParentUUID:childUUIDsData:provenance:syncIdentity:type:behavior:deleted:creationDate:destinationSubObjectReference:lastInsertedEntityID:context:error:]_block_invoke.428
- ___248+[HDDataProvenanceEntity insertOrLookupDataProvenanceForSyncProvenance:syncIdentity:originProductType:originSystemBuild:originOSVersion:localProductType:localSystemBuild:sourceVersion:timeZoneName:sourceID:deviceID:contributorID:transaction:error:]_block_invoke.397
- ___32-[HDBiomeInterface sleepFocusOn]_block_invoke.298
- ___35-[HDDeviceQueryServer _queue_start]_block_invoke.297
- ___35-[HDDeviceQueryServer _queue_start]_block_invoke_2.308
- ___36-[HDCacheDeleteCoordinator activate]_block_invoke.296
- ___36-[HDCacheDeleteCoordinator activate]_block_invoke.297
- ___36-[HDCacheDeleteCoordinator activate]_block_invoke.299
- ___36-[HDCloudSyncPipelineStagePush main]_block_invoke.304
- ___37-[HDCloudSyncStateSyncOperation main]_block_invoke.301
- ___38-[HDDaemon _setupMemoryWarningHandler]_block_invoke.465
- ___39-[HDCloudSyncCreateZonesOperation main]_block_invoke.299
- ___39-[HDIDSPersistentDictionary didCancel:]_block_invoke.427
- ___40-[HDCloudSyncAcceptSharesOperation main]_block_invoke.298
- ___40-[HDDataProvenanceManager _loadDefaults]_block_invoke.313
- ___41-[HDCloudSyncPipeline beginWithTaskTree:]_block_invoke.382
- ___41-[HDCloudSyncPipeline beginWithTaskTree:]_block_invoke.384
- ___41-[HDCloudSyncPipelineStageStateSync main]_block_invoke.302
- ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke.368
- ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke.371
- ___41-[HDProfile _notifyProfileReadyObservers]_block_invoke_2.370
- ___42-[HDCloudSyncDeleteSequenceOperation main]_block_invoke.298
- ___42-[HDCloudSyncDeleteSequenceOperation main]_block_invoke.299
- ___42-[HDCloudSyncLeaveAllSharesOperation main]_block_invoke.293
- ___42-[HDCloudSyncPullReferencesOperation main]_block_invoke.298
- ___42-[HDProfileManager _loadSecondaryProfiles]_block_invoke.333
- ___43-[HDWorkoutBuilderServer _didUpdateEvents:]_block_invoke.616
- ___44-[HDCloudSyncPullChangeRecordOperation main]_block_invoke.306
- ___44-[HDStaticSyncExportTask runWithCompletion:]_block_invoke.319
- ___45-[HDAppLauncher _queue_launchClientIfNeeded:]_block_invoke.302
- ___45-[HDCloudSyncLookupParticipantOperation main]_block_invoke.298
- ___45-[HDCloudSyncPrepareForSharingOperation main]_block_invoke.296
- ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.298
- ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.300
- ___45-[HDCloudSyncPushDeviceContextOperation main]_block_invoke.306
- ___45-[HDCloudSyncSharedSummaryPushOperation main]_block_invoke.293
- ___45-[HDHFDataStore _lock_restoreHFDFromArchive:]_block_invoke.403
- ___45-[HDWorkoutBuilderServer _didUpdateMetadata:]_block_invoke.606
- ___45-[HDWorkoutRouteDataSource elevationUpdated:]_block_invoke.421
- ___46-[HDCloudSyncDeleteStoreOnChildOperation main]_block_invoke.295
- ___46-[HDCloudSyncDisableSyncLocallyOperation main]_block_invoke.295
- ___46-[HDCloudSyncPushDeviceKeyValueOperation main]_block_invoke.303
- ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke.307
- ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke.309
- ___46-[HDCloudSyncShareToParticipantOperation main]_block_invoke_2.313
- ___46-[HDCloudSyncStatusProvider checkLastSyncDate]_block_invoke.336
- ___46-[HDDaemon registerDaemonReadyObserver:queue:]_block_invoke.476
- ___46-[HDSyncIdentityManager profileDidInitialize:]_block_invoke.359
- ___46-[HDWorkoutSessionServer didBeginNewActivity:]_block_invoke.625
- ___46-[_HDAWDPeriodicAction _doIfWaitingWithError:]_block_invoke.347
- ___47-[HDAgeGatingManager _registerForNotifications]_block_invoke.312
- ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke.297
- ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke.301
- ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke_2.299
- ___47-[HDCloudSyncFinishOwnerTakeoverOperation main]_block_invoke_2.302
- ___47-[HDCloudSyncPipelineStageContextSyncPush main]_block_invoke.303
- ___47-[HDWorkoutBuilderServer _didUpdateStatistics:]_block_invoke.655
- ___47-[HDWorkoutSessionServer _queue_generateError:]_block_invoke.711
- ___47-[HDWorkoutSessionServer _queue_generateEvent:]_block_invoke.705
- ___47-[HDWorkoutSessionServer _queue_generateEvent:]_block_invoke.708
- ___48-[HDCloudSyncPipeline _queue_runStage:taskTree:]_block_invoke.399
- ___48-[HDCloudSyncPipeline _queue_runStage:taskTree:]_block_invoke.401
- ___48-[HDWorkoutSessionServer didEndCurrentActivity:]_block_invoke.631
- ___48-[HDWorkoutSessionServer syncSessionEvent:date:]_block_invoke.675
- ___49-[HDCloudSyncAddSharingParticipantOperation main]_block_invoke.312
- ___49-[HDCloudSyncAddSharingParticipantOperation main]_block_invoke.313
- ___49-[HDCloudSyncMarkAllOwnersDisabledOperation main]_block_invoke.296
- ___49-[HDCloudSyncRegisterSubscriptionsOperation main]_block_invoke.296
- ___49-[HDWorkoutSessionServer remoteSessionDidRecover]_block_invoke.676
- ___50-[HDAppSubscriptionManager profileDidBecomeReady:]_block_invoke.315
- ___50-[HDCloudSyncPipelineStageDisableSyncLocally main]_block_invoke.292
- ___50-[HDDaemon registerDaemonActivatedObserver:queue:]_block_invoke.477
- ___50-[HDDataCollectionManager _dataCollectorBlacklist]_block_invoke.417
- ___51-[HDQueryManager _lock_executeDatabaseAccessBlocks]_block_invoke.314
- ___52-[HDCloudSyncSharedSummaryPushPrepareOperation main]_block_invoke.292
- ___52-[HDDemoDataManager _queue_generateDemoDataIfNeeded]_block_invoke.297
- ___52-[HDLiveWorkoutDataSource addQuantities:dataSource:]_block_invoke.416
- ___52-[HDLiveWorkoutDataSource addQuantities:dataSource:]_block_invoke_2.417
- ___52-[HDSeriesBuilderServer _setClientState:completion:]_block_invoke.324
- ___52-[HDWorkoutBasicDataSource setSampleTypesToCollect:]_block_invoke.416
- ___52-[HDWorkoutLocationSmoother _queue_smoothNextSample]_block_invoke.393
- ___53-[HDCloudSyncResetOperation _deleteZonesWithZoneIDs:]_block_invoke.293
- ___54-[HDCloudSyncCachedZone recordsForClass:error:filter:]_block_invoke.334
- ___54-[HDCloudSyncCachedZone recordsForClass:error:filter:]_block_invoke_2.335
- ___54-[HDDataManager _addTransactionInsertionCommitBlocks:]_block_invoke.323
- ___54-[HDPeriodicCountryMonitor _processCountryCodeResult:]_block_invoke.348
- ___55-[HDCloudSyncCachedZone recordForRecordID:class:error:]_block_invoke.344
- ___55-[HDCloudSyncCachedZone recordForRecordID:class:error:]_block_invoke_2.345
- ___55-[HDCloudSyncManager _persistErrorRequiringUserAction:]_block_invoke.455
- ___55-[HDFeatureAvailabilityManager registerObserver:queue:]_block_invoke.413
- ___55-[HDQueryServer authorizedSamplesForClientWithSamples:]_block_invoke.381
- ___55-[HDWorkoutBuilderServer remote_addSamples:completion:]_block_invoke.576
- ___55-[HDWorkoutBuilderServer remote_recoverWithCompletion:]_block_invoke.605
- ___55-[HDWorkoutSessionServer _queue_startInvalidationTimer]_block_invoke.722
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke.372
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_2.376
- ___56-[HDUserCharacteristicsManager _queue_updateUserProfile]_block_invoke_3.380
- ___56-[HDWorkoutBuilderServer remote_addMetadata:completion:]_block_invoke.580
- ___56-[HDWorkoutSessionTaskServer didEndActivity:dataSource:]_block_invoke.435
- ___57-[HDAppExtensionAssertion assertAndUpdateWithCompletion:]_block_invoke.300
- ___57-[HDAppExtensionAssertion assertAndUpdateWithCompletion:]_block_invoke.301
- ___57-[HDAppExtensionAssertion assertAndUpdateWithCompletion:]_block_invoke.303
- ___57-[HDWorkoutSessionServer endCurrentActivityOnDate:error:]_block_invoke.646
- ___58-[HDCloudSyncDeleteZonesOperation _deleteZones:container:]_block_invoke.305
- ___58-[HDCloudSyncDeleteZonesOperation _deleteZones:container:]_block_invoke.307
- ___58-[HDCloudSyncRemoveInvalidShareParticipantsOperation main]_block_invoke.304
- ___58-[HDNanoSyncManager _queue_generateWatchActivationSamples]_block_invoke.552
- ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke.659
- ___58-[HDWorkoutBuilderServer _updateStatisticsPauseResumeMask]_block_invoke_2.660
- ___58-[HDWorkoutSessionTaskServer addWorkoutEvents:dataSource:]_block_invoke.432
- ___58-[HDWorkoutSessionTaskServer didBeginActivity:dataSource:]_block_invoke.434
- ___59+[HDConceptIndexer _indexSample:profile:transaction:error:]_block_invoke.395
- ___59-[HDCloudSyncStatusProvider fetchSyncStatusWithCompletion:]_block_invoke.299
- ___59-[HDCloudSyncStatusProvider fetchSyncStatusWithCompletion:]_block_invoke.301
- ___59-[HDFakeDataCollector _lock_setupSwimmingGeneratorsAtTime:]_block_invoke.324
- ___59-[HDWorkoutBuilderServer remote_removeMetadata:completion:]_block_invoke.585
- ___59-[HDWorkoutSessionTaskServer remote_recoverWithCompletion:]_block_invoke.418
- ___60+[HDSampleEntity dateIntervalsForSampleTypes:profile:error:]_block_invoke.397
- ___60-[HDCloudSyncDeleteStoresOperation _individualZonesToDelete]_block_invoke.297
- ___60-[HDCloudSyncSubscriptionNotificationHandler _enableAPSPush]_block_invoke.298
- ___60-[HDMirroredWorkoutSessionServer setTargetState:date:error:]_block_invoke.337
- ___60-[HDStatisticsCollectionQueryServer _queue_updateStatistics]_block_invoke.378
- ___60-[HDSummarySharingEntryStoreServer sharingEntriesDidUpdate:]_block_invoke.298
- ___61-[HDCloudSyncDetectSyncDisabledOperation _disableSyncLocally]_block_invoke.300
- ___61-[HDCloudSyncManagerPipelineTask mainWithRepositories:error:]_block_invoke.304
- ___61-[HDDatabase _mergeSecondaryJournalsWithActivity:completion:]_block_invoke.576
- ___61-[HDDatabaseMigrator(Tigris) _updateOriginVersionsWithError:]_block_invoke.423
- ___61-[HDWorkoutBuilderServer remote_addWorkoutEvents:completion:]_block_invoke.578
- ___61-[HDWorkoutSessionServer _queue_generateConfigurationUpdate:]_block_invoke.712
- ___62-[HDCloudSyncSharedSummarySynchronizeCloudStateOperation main]_block_invoke.298
- ___62-[HDUserCharacteristicsManager _queue_updateHasWatchOnAccount]_block_invoke.367
- ___62-[HDWorkoutSessionServer _processTargetStoppingStateWithDate:]_block_invoke.587
- ___63-[HDHealthStoreServer remote_deleteClientSourceWithCompletion:]_block_invoke.466
- ___63-[HDStatisticsCollectionQueryServer _queue_useCachedStatistics]_block_invoke.408
- ___63-[HDWorkoutBuilderServer remote_addWorkoutActivity:completion:]_block_invoke.594
- ___63-[HDWorkoutSessionTaskServer didDisconnectFromRemoteWithError:]_block_invoke.439
- ___64-[CMPedometer(HealthDaemon) hd_beginStreamingFromDatum:handler:]_block_invoke.383
- ___64-[CMPedometer(HealthDaemon) hd_beginStreamingFromDatum:handler:]_block_invoke.385
- ___64-[HDCloudSyncComputePullTargetsOperation _pullTargetsWithError:]_block_invoke.301
- ___64-[HDCloudSyncManager cloudSyncRepositoriesForClient:completion:]_block_invoke.426
- ___64-[HDCloudSyncModifyRecordsOperation _saveRecords:deleteRecords:]_block_invoke.315
- ___64-[HDFeatureAvailabilityManager _triggerImmediateSyncWithReason:]_block_invoke.412
- ___64-[HDNanoSyncManager _queue_receiveTinkerOptInRequest:syncStore:]_block_invoke.821
- ___64-[HDNanoSyncManager _scheduleResetReceivedNanoSyncAnchorsForHFD]_block_invoke.929
- ___64-[HDNotificationManager postNotificationWithRequest:completion:]_block_invoke.324
- ___64-[HDPeriodicCountryMonitor _fetchCountryIfNeededWithCompletion:]_block_invoke.332
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.539
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.544
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.547
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.552
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke.563
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.543
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.548
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_2.554
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.551
- ___64-[HDWorkoutBuilderServer stateMachine:didEnterState:date:error:]_block_invoke_3.555
- ___64-[HDWorkoutSessionTaskServer _fetchOrSetupServerWithCompletion:]_block_invoke.451
- ___65-[HDCloudSyncCoordinator resetAllProfilesWithContext:completion:]_block_invoke.401
- ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.311
- ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke.318
- ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke_2.313
- ___65-[HDCreateWorkoutOperation performWithProfile:transaction:error:]_block_invoke_2.320
- ___65-[HDDatabaseCorruptionTTRPrompter _popAlertWithRadarDescription:]_block_invoke.324
- ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.328
- ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke.329
- ___65-[HDMirroredWorkoutSessionServer syncCurrentActivity:completion:]_block_invoke_2.330
- ___65-[HDSourceOrderManager updateOrderedSources:forObjectType:error:]_block_invoke.309
- ___65-[HDSyncIdentityManager rollCurrentSyncIdentityWithReason:error:]_block_invoke.353
- ___65-[HDWorkoutSessionRapportSyncController _sendPendingTransactions]_block_invoke.362
- ___66+[HDWorkoutCondenser _condenseWorkout:entity:configuration:error:]_block_invoke.344
- ___66-[HDClientDataCollectionTaskServer remote_registerWithCompletion:]_block_invoke.312
- ___66-[HDCloudSyncPullReferencesOperation _fetchAttachmentRecordAssets]_block_invoke.308
- ___66-[HDCloudSyncPullReferencesOperation _fetchAttachmentRecordAssets]_block_invoke.310
- ___66-[HDCloudSyncStateSyncOperation _pushUpdatedStateRecordsForZones:]_block_invoke.325
- ___66-[HDCoreMotionDataCollector _queue_forwardCoreMotionData:forType:]_block_invoke.309
- ___66-[HDCoreMotionDataCollector _queue_forwardCoreMotionData:forType:]_block_invoke.311
- ___66-[HDHealthStoreServer _holdActiveClientTransactionWithCompletion:]_block_invoke.489
- ___66-[HDMedicalIDDataManager _triggerSyncForSuccessfulMedicalIDUpdate]_block_invoke.329
- ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.911
- ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.912
- ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke.914
- ___66-[HDNanoSyncManager _queue_receiveAuthorizationRequest:syncStore:]_block_invoke_2.916
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.848
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.863
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.865
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.866
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.868
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.871
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.873
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.879
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke.881
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.876
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.878
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.880
- ___66-[HDNanoSyncManager _queue_receiveTinkerPairingRequest:syncStore:]_block_invoke_2.882
- ___66-[HDWorkoutBuilderSampleQueryServer _queue_performHistoricalQuery]_block_invoke.309
- ___67-[HDCloudSyncAcceptSharesOperation _acceptSharesWithShareMetadata:]_block_invoke.306
- ___67-[HDMirroredWorkoutSessionServer didDisconnectFromRemoteWithError:]_block_invoke.323
- ___68-[HDHealthStoreServer remote_setCharacteristic:forDataType:handler:]_block_invoke.474
- ___68-[HDLocationSeriesSampleEntity freezeWithTransaction:profile:error:]_block_invoke.338
- ___68-[HDLocationSeriesSampleEntity freezeWithTransaction:profile:error:]_block_invoke.340
- ___68-[HDNanoSyncManager _queue_recieveStartWorkoutAppRequest:syncStore:]_block_invoke.796
- ___68-[HDProcessStateManager _lock_registerObserver:forBundleIdentifier:]_block_invoke.310
- ___68-[HDWorkoutManager recoverAllActiveWorkoutSessionServersWithStates:]_block_invoke.390
- ___68-[HDWorkoutSessionTaskServer updateWorkoutConfiguration:dataSource:]_block_invoke.433
- ___69-[HDCloudSyncStateSyncOperation _performStateSyncInZones:completion:]_block_invoke.313
- ___69-[HDDaemon obliterateAndTerminateProfiles:options:reason:completion:]_block_invoke.364
- ___70-[HDCloudSyncManager _queue_considerStartingBackstopSyncForThreshold:]_block_invoke.459
- ___70-[HDDemoDataGenerator _insertIntoDatabaseObjectCollection:fromPerson:]_block_invoke.389
- ___70-[HDDemoDataGenerator _insertIntoDatabaseObjectCollection:fromPerson:]_block_invoke.392
- ___70-[HDNanoSyncManager _queue_receiveChangeRequest:syncStore:completion:]_block_invoke.671
- ___70-[HDSummarySharingEntryIDSManager leaveInvitationWithUUID:completion:]_block_invoke.372
- ___71-[HDBackgroundObservationServerExtension connectWithCompletionHandler:]_block_invoke.312
- ___71-[HDCloudSyncCoordinator _queue_syncAllProfilesWithContext:completion:]_block_invoke.378
- ___71-[HDCloudSyncCoordinator _queue_syncAllProfilesWithContext:completion:]_block_invoke_2.379
- ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.362
- ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.363
- ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.364
- ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.365
- ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.366
- ___71-[HDSummarySharingEntryIDSManager acceptInvitationWithUUID:completion:]_block_invoke.367
- ___71-[HDSummarySharingEntryIDSManager revokeInvitationWithUUID:completion:]_block_invoke.370
- ___71-[HDSummarySharingEntryIDSManager revokeInvitationWithUUID:completion:]_block_invoke.371
- ___71-[HDWorkoutSessionServer stopMirroringToCompanionDeviceWithCompletion:]_block_invoke.664
- ___72-[HDCloudSyncAccountProvider disableAndDeleteAllSyncDataWithCompletion:]_block_invoke.306
- ___72-[HDCloudSyncAccountProvider disableAndDeleteAllSyncDataWithCompletion:]_block_invoke.308
- ___72-[HDCloudSyncCachedZone recordsForClass:epoch:error:enumerationHandler:]_block_invoke.329
- ___72-[HDCloudSyncCachedZone recordsForClass:epoch:error:enumerationHandler:]_block_invoke_2.330
- ___72-[HDCloudSyncDeleteStoresOperation _deleteUnifiedZoneStoresInContainer:]_block_invoke.315
- ___72-[HDCloudSyncDeleteStoresOperation _deleteUnifiedZoneStoresInContainer:]_block_invoke.322
- ___72-[HDCloudSyncPipeline _queue_waitForCloudKitOperationDelayWithTaskTree:]_block_invoke.406
- ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.422
- ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.423
- ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.425
- ___72-[HDDefaultWorkoutSessionController _queue_collectFinalDataThroughDate:]_block_invoke.426
- ___72-[HDMirroredWorkoutSessionServer syncTransitionToState:date:completion:]_block_invoke.327
- ___72-[HDStatisticsCollectionQueryServer _queue_fetchAndDeliverAllStatistics]_block_invoke.395
- ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.400
- ___72-[HDWorkoutCondenser _performPeriodicActivityWithBatchLimit:completion:]_block_invoke.401
- ___73-[HDCloudSyncAccountProvider _performSyncForAccountChangeWithCompletion:]_block_invoke.337
- ___73-[HDCloudSyncPeriodicActivityScheduler performInitialRestore:completion:]_block_invoke.322
- ___73-[HDCloudSyncPushReferencesOperation _pushToCloudKitAndFinishForRecords:]_block_invoke.308
- ___73-[HDCoreMotionDataCollector _queue_beginUpdatesWithTargetCollectionType:]_block_invoke.320
- ___73-[HDNanoSyncManager _syncQueue_prepareForCompanionChangeWithStore:error:]_block_invoke.596
- ___73-[HDWorkoutMirroringManager recoverMirroredWorkoutSessionWithCompletion:]_block_invoke.337
- ___73-[HDWorkoutMirroringManager recoverMirroredWorkoutSessionWithCompletion:]_block_invoke.338
- ___74+[HDSeriesSampleEntity freezeSeriesWithIdentifier:metadata:profile:error:]_block_invoke.330
- ___74-[HDAnalyticsSubmissionCoordinator _locked_sendDailyAnalyticsWithTimeout:]_block_invoke.333
- ___74-[HDAnalyticsSubmissionCoordinator _locked_sendDailyAnalyticsWithTimeout:]_block_invoke.336
- ___74-[HDAnalyticsSubmissionCoordinator _locked_sendDailyAnalyticsWithTimeout:]_block_invoke_2.338
- ___74-[HDDataAggregator requestAggregationThroughDate:mode:options:completion:]_block_invoke.299
- ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.303
- ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.306
- ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.307
- ___74-[HDPostInstallUpdateManager _postInstallUpdateHandlerDidFire:completion:]_block_invoke.310
- ___74-[HDWorkoutBuilderServer _lock_recoverPersistedDataWithTransaction:error:]_block_invoke.509
- ___75-[HDCloudSyncObserverTaskServer _queue_instantiateCloudSyncObserverStatus:]_block_invoke.359
- ___75-[HDCloudSyncObserverTaskServer _queue_instantiateCloudSyncObserverStatus:]_block_invoke_2.360
- ___75-[HDCloudSyncUpdateCachedZonesOperation fetchChangesForContainer:database:]_block_invoke.299
- ___75-[HDCoreMotionDataCollector _didReceiveCoreMotionData:startingDatum:error:]_block_invoke.315
- ___75-[HDCurrentActivitySummaryHelper _handleSignificantTimeChangeNotification:]_block_invoke.310
- ___75-[HDWorkoutBasicDataSource workoutSession:didChangeToState:fromState:date:]_block_invoke.443
- ___75-[HDWorkoutBuilderServer remote_updateActivityWithUUID:endDate:completion:]_block_invoke.602
- ___76-[HDActiveDataAggregator dataCollector:didCollectSensorData:device:options:]_block_invoke.315
- ___76-[HDNanoSyncManager _queue_receiveTinkerEndToEndCloudSyncRequest:syncStore:]_block_invoke.895
- ___76-[HDWorkoutSessionServer didReceiveDataFromRemoteWorkoutSession:completion:]_block_invoke.671
- ___77+[HDDataEntity insertDataObjects:insertionContext:profile:completionHandler:]_block_invoke.455
- ___77-[HDDeleteAttachmentReferenceOperation performWithProfile:transaction:error:]_block_invoke.300
- ___78+[HDDeletedSampleEntity insertCodableDeletedSamples:provenance:profile:error:]_block_invoke.367
- ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.433
- ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.438
- ___78-[HDAggregateDataCollector _queue_fetchHistoricalDataForcedUpdate:completion:]_block_invoke.439
- ___78-[HDCloudSyncRemoveSharingParticipantsOperation _saveUpdatedShares:container:]_block_invoke.299
- ___78-[HDCloudSyncSeizeAbandonedStoresOperation _markPendingOwnerForSeizureTargets]_block_invoke.314
- ___78-[HDDatabaseMigrator(Monarch) _fixProvenancesWithZeroSourceOrDeviceWithError:]_block_invoke.617
- ___78-[HDDatabaseMigrator(Monarch) _fixProvenancesWithZeroSourceOrDeviceWithError:]_block_invoke_2.618
- ___78-[HDNanoSyncManager _queue_recieveCompanionUserNotificationRequest:syncStore:]_block_invoke.807
- ___79-[HDCloudSyncManager configureForShareSetupMetadata:acceptedShares:completion:]_block_invoke.467
- ___79-[HDCloudSyncManager configureForShareSetupMetadata:acceptedShares:completion:]_block_invoke.474
- ___79-[HDCloudSyncRepairRegistryRecordsOperation _modifyRecordsAndFinish:container:]_block_invoke.298
- ___79-[HDDatabaseTransaction performWithContext:error:block:inaccessibilityHandler:]_block_invoke.322
- ___79-[HDPostInstallUpdateManager _triggerMigrationForProfile:protected:completion:]_block_invoke.318
- ___79-[HDWorkoutBuilderServer remote_updateActivityWithUUID:addMetadata:completion:]_block_invoke.604
- ___79-[HDWorkoutClusterServer remote_generateRaceRouteClustersWithLimit:completion:]_block_invoke.301
- ___80-[HDCloudSyncCoordinator _queue_syncProfilesWithIdentifiers:context:completion:]_block_invoke.383
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke.314
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke.335
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_2.315
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_2.338
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_3.325
- ___80-[HDCloudSyncManager(Analytics) reportDailyAnalyticsWithCoordinator:completion:]_block_invoke_4.329
- ___80-[HDSecondaryDevicePairingAgentTaskServer _prepareGuardianForSharingForRequest:]_block_invoke.354
- ___80-[HDWorkoutSessionServer beginNewActivityWithConfiguration:date:metadata:error:]_block_invoke.645
- ___81-[HDDatabaseMigrator(Emet) _emet_migrateWorkoutEventMetadataToProtobufWithError:]_block_invoke.321
- ___81-[HDHealthStoreServer remote_setBackgroundDeliveryFrequency:forDataType:handler:]_block_invoke.453
- ___81-[HDWorkoutSessionRapportSyncController sendRequest:transaction:responseHandler:]_block_invoke.354
- ___82-[HDCloudSyncManager _primaryContainerIdentifiersForCurrentAccountWithCompletion:]_block_invoke.444
- ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.541
- ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.542
- ___82-[HDDatabase _new_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.544
- ___82-[HDDatabase _old_protectedDataQueue_contentProtectionStateChanged:previousState:]_block_invoke.547
- ___82-[HDWorkoutSessionServer enableAutomaticDetectionForActivityConfigurations:error:]_block_invoke.648
- ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.598
- ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.606
- ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.609
- ___82-[HDWorkoutSessionServer stateMachine:didTransition:fromState:toState:date:error:]_block_invoke.610
- ___83-[HDCloudSyncManager _scheduleResetReceivedCloudSyncAnchorsAndRebaseForHFDRecovery]_block_invoke.367
- ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke.334
- ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke.337
- ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke_2.340
- ___83-[HDCloudSyncPipelineStagePush _computePushAndCleanupOperationForPushStores:error:]_block_invoke_3.342
- ___83-[HDDeviceKeyValueStoreManager _deleteRemoteEntries:deviceContextByIdentity:error:]_block_invoke.318
- ___83-[HDWorkoutBuilderServer _addSamples:quantities:dataSource:shouldSavePriorToStart:]_block_invoke.522
- ___83-[HDWorkoutBuilderServer _addSamples:quantities:dataSource:shouldSavePriorToStart:]_block_invoke_2.524
- ___84-[HDCloudSyncPreparePushZoneForStoreOperation _createZoneWithIdentifier:forStoreId:]_block_invoke.308
- ___84-[HDWorkoutLocationSmoother _queue_smoothActivity:activityIndex:forTask:completion:]_block_invoke.400
- ___84-[HDWorkoutLocationSmoother _queue_smoothActivity:activityIndex:forTask:completion:]_block_invoke.401
- ___85-[HDWorkoutMirroringManager rapportMessenger:didReceiveRequest:data:responseHandler:]_block_invoke.314
- ___86-[HDCloudSyncMedicalIDPushOperation _pushMedicalIDRecordToCloudForContainer:database:]_block_invoke.299
- ___87-[HDCloudSyncFetchRecordsOperation _fetchRecordsWithIDs:container:database:completion:]_block_invoke.298
- ___87-[HDCloudSyncPushDeviceKeyValueOperation _computeRecordsToSaveAndDeleteWithCompletion:]_block_invoke.309
- ___87-[HDDataCollectionManager _requestAggregationThroughDate:type:mode:options:completion:]_block_invoke.371
- ___87-[HDHealthStoreServer remote_requestConceptReadAuthorizationForType:filter:completion:]_block_invoke.366
- ___87-[HDHealthStoreServer remote_requestConceptReadAuthorizationForType:filter:completion:]_block_invoke.369
- ___87-[HDInsertSharedSummaryTransactionOperation performWithProfile:transaction:completion:]_block_invoke.294
- ___87-[HDWorkoutEventsManager requestPendingEventsThroughDate:sessionIdentifier:completion:]_block_invoke.307
- ___87-[HDWorkoutEventsManager requestPendingEventsThroughDate:sessionIdentifier:completion:]_block_invoke.309
- ___88-[HDCloudSyncPushDeviceContextOperation _updateRecordsAdd:recordIDsToDelete:completion:]_block_invoke.313
- ___88-[HDDataCollectionManager _requestAggregationThroughDate:types:mode:options:completion:]_block_invoke.370
- ___88-[HDWorkoutSessionTaskServer remote_recoverAllActiveSessionsWithStates:date:completion:]_block_invoke.420
- ___88-[HDWorkoutSessionTaskServer remote_recoverAllActiveSessionsWithStates:date:completion:]_block_invoke.421
- ___89+[HDUserDomainConceptSyncEntity receiveSyncObjects:version:syncProvenance:profile:error:]_block_invoke.305
- ___89-[HDCloudSyncComputePushTargetsOperation _pushTargetsForContainer:ownerIdentifier:error:]_block_invoke.308
- ___89-[HDCloudSyncComputePushTargetsOperation _pushTargetsForContainer:ownerIdentifier:error:]_block_invoke.311
- ___89-[HDHealthStoreServer remote_fetchModificationDateForCharacteristicWithDataType:handler:]_block_invoke.475
- ___89-[HDHealthStoreServer remote_requestPerObjectReadAuthorizationForType:filter:completion:]_block_invoke.362
- ___89-[HDHealthStoreServer remote_requestPerObjectReadAuthorizationForType:filter:completion:]_block_invoke.364
- ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.573
- ___89-[HDWorkoutBuilderServer remote_setTargetConstructionState:startDate:endDate:completion:]_block_invoke.574
- ___90+[HDLocationSeriesHFDMigrationEntity _migrateSeriesWithKey:toSQLFromStore:database:error:]_block_invoke.314
- ___90+[HDQuantitySeriesHFDMigrationEntity _migrateSeriesWithKey:toSQLFromStore:database:error:]_block_invoke.301
- ___90+[HDRaceRouteLocationSeriesEntity createRoutePointsFromWorkout:transaction:profile:error:]_block_invoke.325
- ___90+[HDRaceRouteLocationSeriesEntity createRoutePointsFromWorkout:transaction:profile:error:]_block_invoke_2.327
- ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.347
- ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.348
- ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.352
- ___90-[HDCloudSyncObserverTaskServer _queue_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke_2.353
- ___90-[HDCloudSyncObserverTaskServer remote_startSyncIfRestoreNotCompletedWithUUID:completion:]_block_invoke.339
- ___90-[HDCloudSyncPullChangeRecordOperation _persistFetchedArchiveAsset:protocolVersion:error:]_block_invoke.335
- ___90-[HDCloudSyncPullChangeRecordOperation _persistFetchedArchiveAsset:protocolVersion:error:]_block_invoke.337
- ___90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.367
- ___90-[HDCloudSyncPushSequenceOperation _pushRecords:recordIDsToDelete:containerID:completion:]_block_invoke.369
- ___90-[HDCloudSyncSharedSummaryPushPruningOperation _modifyRecordsAndFinish:recordIDsToDelete:]_block_invoke.309
- ___90-[HDDataAggregator persistForCollector:usedDatums:source:device:error:persistenceHandler:]_block_invoke.321
- ___90-[HDDataAggregator persistForCollector:usedDatums:source:device:error:persistenceHandler:]_block_invoke.324
- ___92+[HDLocationSeriesSampleEntity insertLocationData:seriesIdentifier:assertion:profile:error:]_block_invoke.310
- ___92-[HDBatchedQueryServer batchObjectsWithEnumerator:includeDeletedObjects:error:batchHandler:]_block_invoke.297
- ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke.347
- ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke.348
- ___92-[HDClientDataCollectionTaskServer dataAggregator:requestsCollectionThroughDate:completion:]_block_invoke_2.349
- ___92-[HDCloudSyncCoordinator(CloudSyncJournalMerge) _mergeCloudSyncJournalsForProfile:taskTree:]_block_invoke.301
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.305
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.307
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.313
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.317
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke.318
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke_2.309
- ___92-[HDCloudSyncUpdateCachedRecordsOperation _fetchChangesForRecordZoneIDs:container:database:]_block_invoke_2.315
- ___93+[HDMedicationDoseEventEntity _logPersistedDoseEventOnCommitDatabase:doseEvent:persistentID:]_block_invoke.387
- ___93-[HDAppSubscriptionManager _updateObservationStatusForDataTypeCode:lastAppLaunchTimes:error:]_block_invoke.342
- ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke.299
- ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke.302
- ___94-[HDActiveDataAggregator _aggregateForCollector:device:requestedAggregationDate:mode:options:]_block_invoke_2.304
- ___94-[HDIngestDeviceContextsOperation _pullDeviceContextsForProfile:repository:transaction:error:]_block_invoke.299
- ___94-[HDRestorableAlarmScheduler _queue_notifyClientsOfDueEventsAndScheduleNextFireDateWithError:]_block_invoke.325
- ___94-[HDWorkoutBasicDataSource _workoutDataDestination:requestsSamplesOfType:from:to:transaction:]_block_invoke.435
- ___94-[HDWorkoutManager generatePauseOrResumeRequestAllowingBackgroundRuntime:metadata:completion:]_block_invoke.371
- ___95+[HDAppSubscriptionAppLaunchEntity insertOrUpdateAppSDKVersionToken:forBundleID:profile:error:]_block_invoke.385
- ___95-[HDCloudSyncPushReferenceTombstonesOperation _modifyCloudWithRecordsToSave:recordIDsToDelete:]_block_invoke.309
- ___95-[HDDatabaseJournal _mergeJournalChapter:profile:accessibilityAssertion:shouldContinueHandler:]_block_invoke.365
- ___95-[HDQueryControlServer queryServer:requestsAuthorizationWithContext:promptIfNeeded:completion:]_block_invoke.308
- ___96-[HDTTRPromptController _presentTTRPromptForErrors:lastPromptBuild:lastPromptDate:currentBuild:]_block_invoke.362
- ___97+[HDLogicalSourceOrderEntity updateOrderedLogicalSourcesForType:transaction:error:updateHandler:]_block_invoke.351
- ___97+[HDLogicalSourceOrderEntity updateOrderedLogicalSourcesForType:transaction:error:updateHandler:]_block_invoke_2.352
- ___97-[HDBackgroundObservationServerExtension notifyExtensionOfUpdateForSampleType:completionHandler:]_block_invoke.317
- ___97-[HDHealthStoreServer remote_requestAuthorizationToShareTypes:readTypes:shouldPrompt:completion:]_block_invoke.374
- ___97-[HDSecondaryDevicePairingAgentTaskServer _setupTinkerProfileForRequest:metadata:acceptedShares:]_block_invoke.362
- ___Block_byref_object_copy_.307
- ___Block_byref_object_copy_.310
- ___Block_byref_object_copy_.313
- ___Block_byref_object_copy_.323
- ___Block_byref_object_copy_.325
- ___Block_byref_object_copy_.330
- ___Block_byref_object_copy_.370
- ___Block_byref_object_dispose_.308
- ___Block_byref_object_dispose_.311
- ___Block_byref_object_dispose_.314
- ___Block_byref_object_dispose_.324
- ___Block_byref_object_dispose_.326
- ___Block_byref_object_dispose_.331
- ___Block_byref_object_dispose_.371
- ____HDAddUniquenessChecksumToOriginalFHIRResourceEntity_block_invoke.1340
- ____HDCopyWorkoutTotalsToPrimaryActivity_block_invoke.602
- ____HDMigrateCycleTrackingOnboarding_block_invoke.966
- ____HDMigrateCycleTrackingOnboarding_block_invoke_2.967
- ____HDUpdateClinicalRecordEntities_block_invoke.892
- ____HDUpdateClinicalRecordEntities_block_invoke_2.893
- ____HDUpdateClinicalRecordEntities_block_invoke_3.897
- ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke.978
- ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke.982
- ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke_2.983
- ____HDUpdateMedicalRecordEntitiesTableWithOrigin_block_invoke_3.987
- ____ZL27_HDHFDataStoreWillOpenStoreP13HDHFDataStore_block_invoke.488
- ___block_descriptor_56_ea8_32s40r48r_e267_v80?0B8{vector<std::tuple<long long, HKSample *>, std::allocator<std::tuple<long long, HKSample *>>>=^v^v^v}12{vector<std::tuple<long long, HKDeletedObject *>, std::allocator<std::tuple<long long, HKDeletedObject *>>>=^v^v^v}36"HKSortedQueryAnchor"60B68"NSError"72lr40l8s32l8r48l8
- ___block_literal_global.1002
- ___block_literal_global.1043
- ___block_literal_global.1058
- ___block_literal_global.1066
- ___block_literal_global.1107
- ___block_literal_global.1130
- ___block_literal_global.294
- ___block_literal_global.296
- ___block_literal_global.297
- ___block_literal_global.298
- ___block_literal_global.300
- ___block_literal_global.301
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.308
- ___block_literal_global.316
- ___block_literal_global.332
- ___block_literal_global.346
- ___block_literal_global.352
- ___block_literal_global.356
- ___block_literal_global.359
- ___block_literal_global.362
- ___block_literal_global.364
- ___block_literal_global.367
- ___block_literal_global.369
- ___block_literal_global.381
- ___block_literal_global.389
- ___block_literal_global.392
- ___block_literal_global.394
- ___block_literal_global.395
- ___block_literal_global.397
- ___block_literal_global.412
- ___block_literal_global.413
- ___block_literal_global.415
- ___block_literal_global.417
- ___block_literal_global.418
- ___block_literal_global.420
- ___block_literal_global.428
- ___block_literal_global.434
- ___block_literal_global.435
- ___block_literal_global.441
- ___block_literal_global.449
- ___block_literal_global.451
- ___block_literal_global.463
- ___block_literal_global.464
- ___block_literal_global.465
- ___block_literal_global.466
- ___block_literal_global.467
- ___block_literal_global.471
- ___block_literal_global.477
- ___block_literal_global.479
- ___block_literal_global.482
- ___block_literal_global.487
- ___block_literal_global.493
- ___block_literal_global.495
- ___block_literal_global.497
- ___block_literal_global.515
- ___block_literal_global.520
- ___block_literal_global.530
- ___block_literal_global.549
- ___block_literal_global.550
- ___block_literal_global.556
- ___block_literal_global.562
- ___block_literal_global.567
- ___block_literal_global.569
- ___block_literal_global.572
- ___block_literal_global.589
- ___block_literal_global.591
- ___block_literal_global.599
- ___block_literal_global.612
- ___block_literal_global.614
- ___block_literal_global.616
- ___block_literal_global.618
- ___block_literal_global.620
- ___block_literal_global.622
- ___block_literal_global.624
- ___block_literal_global.628
- ___block_literal_global.630
- ___block_literal_global.635
- ___block_literal_global.636
- ___block_literal_global.642
- ___block_literal_global.653
- ___block_literal_global.672
- ___block_literal_global.678
- ___block_literal_global.679
- ___block_literal_global.695
- ___block_literal_global.697
- ___block_literal_global.709
- ___block_literal_global.711
- ___block_literal_global.712
- ___block_literal_global.714
- ___block_literal_global.717
- ___block_literal_global.725
- ___block_literal_global.727
- ___block_literal_global.742
- ___block_literal_global.759
- ___block_literal_global.771
- ___block_literal_global.793
- ___block_literal_global.805
- ___block_literal_global.809
- ___block_literal_global.851
- ___block_literal_global.874
- ___block_literal_global.915
- ___block_literal_global.916
- ___block_literal_global.931
- ___block_literal_global.935
- ___block_literal_global.938
- ___block_literal_global.979
- __insertStatementKey.key.495
- _columnDefinitionsWithCount:.HDDeviceKeyValueStorageEntryEntityColumnDefinitions.384
- _columnDefinitionsWithCount:.columnDefinitions.396
Functions:
~ __ZN2PB9PtrVectorIN10statistics8IntervalEE12emplace_backIJRKS2_EEEvDpOT_ : 340 -> 344
~ __ZN2PB9PtrVectorIN10statistics8IntervalEE12emplace_backIJEEEvDpOT_ : 360 -> 364
~ __ZN2PB9PtrVectorIN10statistics17RawQuantitySampleEE12emplace_backIJRKS2_EEEvDpOT_ : 340 -> 344
~ __ZN2PB9PtrVectorIN10statistics10StatisticsEE12emplace_backIJRKS2_EEEvDpOT_ : 340 -> 344
~ __ZN2PB9PtrVectorIN10statistics17RawQuantitySampleEE12emplace_backIJEEEvDpOT_ : 360 -> 364
~ __ZN2PB9PtrVectorIN10statistics10StatisticsEE12emplace_backIJEEEvDpOT_ : 384 -> 388
~ __ZNKSt3__120__shared_ptr_pointerIPhNS_14default_deleteIA_hEENS_9allocatorIhEEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN6health18TransactionalCacheIyNS2_8FilePageEE9CacheLineEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE25__emplace_unique_key_argsIyJRKNS_21piecewise_construct_tENS_5tupleIJRKyEEENSN_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEERKT_DpOT0_ : 1040 -> 1044
~ -[HDSortedSampleIterator initWithQueryDescriptor:includeDeletedObjects:sortDescriptors:anchor:bufferSize:profile:] : 856 -> 840
~ __ZNSt3__16vectorINS_5tupleIJxU8__strongP8HKSampleEEENS_9allocatorIS5_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZN2PB9PtrVectorIN10statistics8IntervalEE12emplace_backIJRS2_EEEvDpOT_ : 340 -> 344
~ __ZNSt3__16vectorI16_HDWrappedSourceNS_9allocatorIS1_EEE7reserveEm : 160 -> 164
~ __ZNSt3__16vectorI16_HDWrappedSourceNS_9allocatorIS1_EEE9push_backB8ne200100ERKS1_ : 292 -> 300
~ ___59-[HDSourceOrderManager addOrderedSource:objectTypes:error:]_block_invoke : 3580 -> 3592
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP8HKSource16_HDWrappedSourceEENS_22__unordered_map_hasherIS4_S6_14HDNSObjectHash15HDNSObjectEqualLb1EEENS_21__unordered_map_equalIS4_S6_S9_S8_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS4_JRKNS_21piecewise_construct_tENS_5tupleIJRU8__strongKS3_EEENSK_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_ : 1184 -> 1180
~ __ZNK22HDStatisticsNoiseLevel23archiveOverlapProcessorEv : 732 -> 744
~ ___144+[_HDSortedSampleIteratorInternalPager getSamplesWithQueryDescriptor:sortDescriptors:anchor:limit:includeDeletedObjects:profile:resultsHandler:]_block_invoke : 940 -> 924
~ __ZNSt3__15dequeIN6health12BlockPointerENS_9allocatorIS2_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__114__split_bufferIPN6health12BlockPointerENS_9allocatorIS3_EEE13emplace_frontIJS3_EEEvDpOT_ : 268 -> 272
~ __ZNKSt3__111basic_regexIcNS_12regex_traitsIcEEE16__match_at_startINS_9allocatorINS_9sub_matchIPKcEEEEEEbS8_S8_RNS_13match_resultsIS8_T_EENS_15regex_constants15match_flag_typeEb : 4216 -> 4180
~ __ZNSt3__15dequeINS_7__stateIcEENS_9allocatorIS2_EEE9push_backEOS2_ : 812 -> 816
~ __ZNKSt3__120__shared_ptr_pointerIPNS_13__empty_stateIcEENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__111basic_regexIcNS_12regex_traitsIcEEE26__parse_bracket_expressionIPKcEET_S7_S7_ : 3336 -> 3328
~ -[HDQuantityDistributionCalculator initWithStartDate:endDate:anchorDate:intervalComponents:histogramBucketAnchor:histogramBucketSize:] : 1324 -> 1268
~ __ZNSt3__16vectorI13HKRawIntervalIdENS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__15dequeINS_5tupleIJddfEEENS_9allocatorIS2_EEE12emplace_backIJRdS7_RfEEERS2_DpOT_ : 516 -> 520
~ __ZN10statistics29QuantityOverlapProcessorStateC2ERKS0_ : 560 -> 568
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIU8__strongP8NSStringxEENS_22__unordered_map_hasherIS4_S5_12HDStringHash13HDStringEqualLb1EEENS_21__unordered_map_equalIS4_S5_S8_S7_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS4_JRKNS_21piecewise_construct_tENS_5tupleIJRU8__strongKS3_EEENSJ_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_ : 632 -> 628
~ __ZNSt3__112__hash_tableINS_17__hash_value_typeIxU8__strongP8NSStringEENS_22__unordered_map_hasherIxS5_NS_4hashIxEENS_8equal_toIxEELb1EEENS_21__unordered_map_equalIxS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIxJRKNS_21piecewise_construct_tENS_5tupleIJRKxEEENSL_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_ : 592 -> 596
~ __ZNK18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEEE28statisticsByBundleIdentifierEv : 1528 -> 1532
~ __ZN2PB9PtrVectorIN10statistics17RawQuantitySampleEE12emplace_backIJS2_EEEvDpOT_ : 412 -> 416
~ __ZN2PB9PtrVectorIN10statistics17RawQuantitySampleEE12emplace_backIJRS2_EEEvDpOT_ : 340 -> 344
~ __ZN2PB9PtrVectorIN10statistics10StatisticsEE12emplace_backIJRS2_EEEvDpOT_ : 340 -> 344
~ __ZNK18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsDiscrete24HDStatisticsTimeIntervalEE28statisticsByBundleIdentifierEv : 1492 -> 1496
~ __ZNK18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEEE28statisticsByBundleIdentifierEv : 1516 -> 1520
~ __ZNK18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsCumulative24HDStatisticsTimeIntervalEE28statisticsByBundleIdentifierEv : 1480 -> 1484
~ __ZNK18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE28statisticsByBundleIdentifierEv : 1604 -> 1608
~ __ZNK18HDStatisticsBucketI20HDStatisticsCombinedI42HDStatisticsTemporalBucketWeightedDiscreteI52HDStatisticsTemporalBucketWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE28statisticsByBundleIdentifierEv : 1532 -> 1536
~ __ZNK18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEEE28statisticsByBundleIdentifierEv : 1576 -> 1580
~ __ZNK18HDStatisticsBucketI20HDStatisticsCombinedI38HDStatisticsTemporallyWeightedDiscreteI48HDStatisticsTemporallyWeightedDiscreteParametersE24HDStatisticsTimeIntervalEE28statisticsByBundleIdentifierEv : 1540 -> 1544
~ __ZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS2_EEE26decodeInternalsWithDecoderEP7NSCoder : 1680 -> 1668
~ __ZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI24HDStatisticsTimeIntervalS1_EE26decodeInternalsWithDecoderEP7NSCoder : 1568 -> 1564
~ __ZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEE26decodeInternalsWithDecoderEP7NSCoder : 1832 -> 1812
~ __ZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEEC2ERKS6_ : 1124 -> 1120
~ __ZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEE26decodeInternalsWithDecoderEP7NSCoder : 1736 -> 1712
~ __ZN18HDStatisticsBucketI20HDStatisticsCombinedI22HDStatisticsNoiseLevel24HDStatisticsTimeIntervalEEC2ERKS4_ : 1056 -> 1052
~ __ZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEE26decodeInternalsWithDecoderEP7NSCoder : 1640 -> 1632
~ __ZN18HDStatisticsBucketI20HDStatisticsRelativeI22HDStatisticsNoiseLevelEEC2ERKS3_ : 980 -> 976
~ __ZN55_HDConcreteStatisticsCollectionCalculatorImplementationI22HDStatisticsNoiseLevelE26decodeInternalsWithDecoderEP7NSCoder : 1536 -> 1524
~ __ZNK18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEEE28statisticsByBundleIdentifierEv : 1516 -> 1520
~ __ZNK18HDStatisticsBucketI20HDStatisticsCombinedI33HDStatisticsAverageSampleDuration24HDStatisticsTimeIntervalEE28statisticsByBundleIdentifierEv : 1480 -> 1484
~ __ZNK55_HDConcreteStatisticsCollectionCalculatorImplementationI33HDStatisticsAverageSampleDurationE29_statisticsFromFinishedBucketERK18HDStatisticsBucketIS0_E : 3136 -> 3140
~ __ZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEE26decodeInternalsWithDecoderEP7NSCoder : 1732 -> 1716
~ __ZN18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEEEC2ERKS6_ : 1192 -> 1208
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZN55_HDConcreteStatisticsCollectionCalculatorImplementationI20HDStatisticsCombinedI23HDStatisticsPercentiles24HDStatisticsTimeIntervalEE26decodeInternalsWithDecoderEP7NSCoder : 1612 -> 1596
~ __ZNK18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEEE28statisticsByBundleIdentifierEv : 1516 -> 1520
~ __ZNK18HDStatisticsBucketI20HDStatisticsCombinedI20HDStatisticsPresence24HDStatisticsTimeIntervalEE28statisticsByBundleIdentifierEv : 1472 -> 1476
~ __ZNK18HDStatisticsBucketI20HDStatisticsRelativeI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEEE28statisticsByBundleIdentifierEv : 1712 -> 1716
~ __ZNK18HDStatisticsBucketI20HDStatisticsCombinedI23HDStatisticsSleepStages24HDStatisticsTimeIntervalEE28statisticsByBundleIdentifierEv : 1644 -> 1648
~ __ZNSt3__16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_10shared_ptrIN6health12InMemoryFileEEEEENS_19__map_value_compareIS7_SC_NS_4lessIS7_EELb1EEENS5_ISC_EEE25__emplace_unique_key_argsIS7_JRKNS_21piecewise_construct_tENS_5tupleIJRKS7_EEENSN_IJEEEEEENS_4pairINS_15__tree_iteratorISC_PNS_11__tree_nodeISC_PvEElEEbEERKT_DpOT0_ : 352 -> 356
~ ___119-[HDRollingBaselineRelativeDataSource _primeBaselineCalculatorWithPriorSamplesForSample:baselineCompatibilityID:error:]_block_invoke : 2336 -> 2328
~ __ZNSt3__15dequeI39HDQuantitySampleAttenuationEngineSampleNS_9allocatorIS1_EEE9push_backERKS1_ : 504 -> 508
~ __ZNSt3__15dequeI39HDQuantitySampleAttenuationEngineSampleNS_9allocatorIS1_EEE18__append_with_sizeB8ne200100INS_16__deque_iteratorIS1_PKS1_RS7_PKS8_lLl102EEEEEvT_m : 1260 -> 1264
CStrings:
+ "T{deque<HDQuantitySampleAttenuationEngineSample, std::allocator<HDQuantitySampleAttenuationEngineSample>>={__split_buffer<HDQuantitySampleAttenuationEngineSample *, std::allocator<HDQuantitySampleAttenuationEngineSample *>>=^^{?}^^{?}^^{?}{?=^^{?}}}Q{?=Q}},N,V_attenuationSamplesWindow"
+ "applicationsDidUpdateMetadata:"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v64@0:8{deque<HDQuantitySampleAttenuationEngineSample, std::allocator<HDQuantitySampleAttenuationEngineSample>>={__split_buffer<HDQuantitySampleAttenuationEngineSample *, std::allocator<HDQuantitySampleAttenuationEngineSample *>>=^^{?}^^{?}^^{?}{?=^^{?}}}Q{?=Q}}16"
+ "v80@?0B8{vector<std::tuple<long long, HKSample *>, std::allocator<std::tuple<long long, HKSample *>>>=^v^v{?=^v}}12{vector<std::tuple<long long, HKDeletedObject *>, std::allocator<std::tuple<long long, HKDeletedObject *>>>=^v^v{?=^v}}36@\"HKSortedQueryAnchor\"60B68@\"NSError\"72"
+ "{HistogramState=\"_dateBuckets\"{vector<HistogramBucket, std::allocator<HistogramBucket>>=\"__begin_\"^{HistogramBucket}\"__end_\"^{HistogramBucket}\"\"{?=\"__cap_\"^{HistogramBucket}}}\"_histogramBucketAnchor\"d\"_histogramBucketSize\"d\"_currentStartDateBucket\"q}"
+ "{deque<HDQuantitySampleAttenuationEngineSample, std::allocator<HDQuantitySampleAttenuationEngineSample>>=\"__map_\"{__split_buffer<HDQuantitySampleAttenuationEngineSample *, std::allocator<HDQuantitySampleAttenuationEngineSample *>>=\"__first_\"^^{?}\"__begin_\"^^{?}\"__end_\"^^{?}\"\"{?=\"__cap_\"^^{?}}}\"__start_\"Q\"\"{?=\"__size_\"Q}}"
+ "{deque<HDQuantitySampleAttenuationEngineSample, std::allocator<HDQuantitySampleAttenuationEngineSample>>={__split_buffer<HDQuantitySampleAttenuationEngineSample *, std::allocator<HDQuantitySampleAttenuationEngineSample *>>=^^{?}^^{?}^^{?}{?=^^{?}}}Q{?=Q}}16@0:8"
+ "{deque<std::tuple<double, double, float>, std::allocator<std::tuple<double, double, float>>>=\"__map_\"{__split_buffer<std::tuple<double, double, float> *, std::allocator<std::tuple<double, double, float> *>>=\"__first_\"^^v\"__begin_\"^^v\"__end_\"^^v\"\"{?=\"__cap_\"^^v}}\"__start_\"Q\"\"{?=\"__size_\"Q}}"
+ "{queue<HDQuantitySampleAttenuationEngineSample, std::deque<HDQuantitySampleAttenuationEngineSample>>={deque<HDQuantitySampleAttenuationEngineSample, std::allocator<HDQuantitySampleAttenuationEngineSample>>={__split_buffer<HDQuantitySampleAttenuationEngineSample *, std::allocator<HDQuantitySampleAttenuationEngineSample *>>=^^{?}^^{?}^^{?}{?=^^{?}}}Q{?=Q}}}56@0:8{?=dddBq}16"
+ "{unique_ptr<_HDStatisticsCollectionCalculatorImplementation, std::default_delete<_HDStatisticsCollectionCalculatorImplementation>>=\"\"{?=\"__ptr_\"^{_HDStatisticsCollectionCalculatorImplementation}}}"
+ "{unique_ptr<health::DataStore, std::default_delete<health::DataStore>>={?=^{DataStore}}}44@0:8@16r^v24B32^@36"
+ "{unordered_map<NSString *, std::deque<HDRawQuantitySample>, HDStringHash, HDStringEqual, std::allocator<std::pair<NSString *const, std::deque<HDRawQuantitySample>>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, HDStringHash, HDStringEqual>, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, HDStringEqual, HDStringHash>, std::allocator<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{unordered_set<long, std::hash<long>, std::equal_to<long>, std::allocator<long>>=\"__table_\"{__hash_table<long, std::hash<long>, std::equal_to<long>, std::allocator<long>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long, void *> *> *>>>=\"\"{?=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long, void *> *> *>>=\"\"{?=\"__size_\"Q}}}}\"\"{?=\"__first_node_\"{__hash_node_base<std::__hash_node<long, void *> *>=\"__next_\"^v}}\"\"{?=\"__size_\"Q}\"\"{?=\"__max_load_factor_\"f}}}"
+ "{vector<_HDWrappedSource, std::allocator<_HDWrappedSource>>=\"__begin_\"^{_HDWrappedSource}\"__end_\"^{_HDWrappedSource}\"\"{?=\"__cap_\"^{_HDWrappedSource}}}"
+ "{vector<std::tuple<long long, HKDeletedObject *>, std::allocator<std::tuple<long long, HKDeletedObject *>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<std::tuple<long long, HKSample *>, std::allocator<std::tuple<long long, HKSample *>>>=\"__begin_\"^v\"__end_\"^v\"\"{?=\"__cap_\"^v}}"
+ "{vector<unsigned char, std::allocator<unsigned char>>=\"__begin_\"*\"__end_\"*\"\"{?=\"__cap_\"*}}"
- "T{deque<HDQuantitySampleAttenuationEngineSample, std::allocator<HDQuantitySampleAttenuationEngineSample>>={__split_buffer<HDQuantitySampleAttenuationEngineSample *, std::allocator<HDQuantitySampleAttenuationEngineSample *>>=^^{?}^^{?}^^{?}^^{?}}QQ},N,V_attenuationSamplesWindow"
- "v64@0:8{deque<HDQuantitySampleAttenuationEngineSample, std::allocator<HDQuantitySampleAttenuationEngineSample>>={__split_buffer<HDQuantitySampleAttenuationEngineSample *, std::allocator<HDQuantitySampleAttenuationEngineSample *>>=^^{?}^^{?}^^{?}^^{?}}QQ}16"
- "v80@?0B8{vector<std::tuple<long long, HKSample *>, std::allocator<std::tuple<long long, HKSample *>>>=^v^v^v}12{vector<std::tuple<long long, HKDeletedObject *>, std::allocator<std::tuple<long long, HKDeletedObject *>>>=^v^v^v}36@\"HKSortedQueryAnchor\"60B68@\"NSError\"72"
- "{HistogramState=\"_dateBuckets\"{vector<HistogramBucket, std::allocator<HistogramBucket>>=\"__begin_\"^{HistogramBucket}\"__end_\"^{HistogramBucket}\"__cap_\"^{HistogramBucket}}\"_histogramBucketAnchor\"d\"_histogramBucketSize\"d\"_currentStartDateBucket\"q}"
- "{deque<HDQuantitySampleAttenuationEngineSample, std::allocator<HDQuantitySampleAttenuationEngineSample>>=\"__map_\"{__split_buffer<HDQuantitySampleAttenuationEngineSample *, std::allocator<HDQuantitySampleAttenuationEngineSample *>>=\"__first_\"^^{?}\"__begin_\"^^{?}\"__end_\"^^{?}\"__cap_\"^^{?}}\"__start_\"Q\"__size_\"Q}"
- "{deque<HDQuantitySampleAttenuationEngineSample, std::allocator<HDQuantitySampleAttenuationEngineSample>>={__split_buffer<HDQuantitySampleAttenuationEngineSample *, std::allocator<HDQuantitySampleAttenuationEngineSample *>>=^^{?}^^{?}^^{?}^^{?}}QQ}16@0:8"
- "{deque<std::tuple<double, double, float>, std::allocator<std::tuple<double, double, float>>>=\"__map_\"{__split_buffer<std::tuple<double, double, float> *, std::allocator<std::tuple<double, double, float> *>>=\"__first_\"^^v\"__begin_\"^^v\"__end_\"^^v\"__cap_\"^^v}\"__start_\"Q\"__size_\"Q}"
- "{queue<HDQuantitySampleAttenuationEngineSample, std::deque<HDQuantitySampleAttenuationEngineSample>>={deque<HDQuantitySampleAttenuationEngineSample, std::allocator<HDQuantitySampleAttenuationEngineSample>>={__split_buffer<HDQuantitySampleAttenuationEngineSample *, std::allocator<HDQuantitySampleAttenuationEngineSample *>>=^^{?}^^{?}^^{?}^^{?}}QQ}}56@0:8{?=dddBq}16"
- "{unique_ptr<_HDStatisticsCollectionCalculatorImplementation, std::default_delete<_HDStatisticsCollectionCalculatorImplementation>>=\"__ptr_\"^{_HDStatisticsCollectionCalculatorImplementation}}"
- "{unique_ptr<health::DataStore, std::default_delete<health::DataStore>>=^{DataStore}}44@0:8@16r^v24B32^@36"
- "{unordered_map<NSString *, std::deque<HDRawQuantitySample>, HDStringHash, HDStringEqual, std::allocator<std::pair<NSString *const, std::deque<HDRawQuantitySample>>>>=\"__table_\"{__hash_table<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, std::__unordered_map_hasher<NSString *, std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, HDStringHash, HDStringEqual>, std::__unordered_map_equal<NSString *, std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, HDStringEqual, HDStringHash>, std::allocator<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NSString *, std::deque<HDRawQuantitySample>>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{unordered_set<long, std::hash<long>, std::equal_to<long>, std::allocator<long>>=\"__table_\"{__hash_table<long, std::hash<long>, std::equal_to<long>, std::allocator<long>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<long, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<long, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<long, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "{vector<_HDWrappedSource, std::allocator<_HDWrappedSource>>=\"__begin_\"^{_HDWrappedSource}\"__end_\"^{_HDWrappedSource}\"__cap_\"^{_HDWrappedSource}}"
- "{vector<std::tuple<long long, HKDeletedObject *>, std::allocator<std::tuple<long long, HKDeletedObject *>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<std::tuple<long long, HKSample *>, std::allocator<std::tuple<long long, HKSample *>>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
- "{vector<unsigned char, std::allocator<unsigned char>>=\"__begin_\"*\"__end_\"*\"__cap_\"*}"

```
