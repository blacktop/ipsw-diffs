## ActivitySharingDaemonCore

> `/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`

```diff

-856.0.0.0.0
-  __TEXT.__text: 0x7d4d8
+2026.0.1.1.1
+  __TEXT.__text: 0x7d4dc
   __TEXT.__auth_stubs: 0xee0
   __TEXT.__objc_methlist: 0x457c
   __TEXT.__const: 0x1d8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B85A9605-4BB5-3154-9964-DACEFAFBF337
+  UUID: 4594388D-4281-3DBF-BE38-9D0B07C05B5E
   Functions: 2358
   Symbols:   8791
   CStrings:  4198
Symbols:
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke.340
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.341
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.341.cold.1
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_3.342
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.343
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.343.cold.1
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.343.cold.2
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.349
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.349.cold.1
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.350
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.351
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.397
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.398
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.398.cold.1
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_2.399
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.400
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.400.cold.1
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.413
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.414
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.418
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.416
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.416.cold.1
+ ___106-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:]_block_invoke.354
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.592
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.593
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.593.cold.1
+ ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.335
+ ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.337
+ ___108-[ASCloudKitManager _performAndRetryNewAccountTasksWithRetryInterval:shouldCreateSubscriptions:shouldFetch:]_block_invoke.467
+ ___109-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:]_block_invoke.353
+ ___117-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.327
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.384
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.385
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.390
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2.388
+ ___126-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.391
+ ___130-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.392
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.417.cold.1
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.419
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.419.cold.1
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.420
+ ___149-[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:group:completion:]_block_invoke.304
+ ___153-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.393
+ ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.344
+ ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.344.cold.1
+ ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.346
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.333
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.338
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.340
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.342
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke_2.339
+ ___19-[ASXPCClient init]_block_invoke.340
+ ___31-[ASGatewayManager updateState]_block_invoke.306
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.310
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.311
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.312
+ ___39-[ASContactsManager loadCachedContacts]_block_invoke.326
+ ___43-[ASDatabaseClient performWhenDaemonReady:]_block_invoke.316
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.297
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.297.cold.1
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.298
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.298.cold.1
+ ___46-[ASAsyncTransactionQueue performTransaction:]_block_invoke.296
+ ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.309
+ ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.309.cold.1
+ ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.310
+ ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke.469
+ ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke_2.470
+ ___48-[ASGatewayManager gatewayStatusWithCompletion:]_block_invoke.303
+ ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.394
+ ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.395
+ ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.395.cold.1
+ ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.454
+ ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.455
+ ___50-[ASCompetitionStore _saveCompetitionLists:owner:]_block_invoke.303
+ ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.344
+ ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.345
+ ___53-[ASIDSMessageCenter donatedAddressesWithCompletion:]_block_invoke.402
+ ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.314
+ ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.314.cold.1
+ ___55-[ASCompetitionTemplateSource templatesWithCompletion:]_block_invoke.293
+ ___58-[ASRelationshipManager _processPersistedMessagesIfNeeded]_block_invoke.394
+ ___60-[ASActivitySharingManager _mainQueue_completeSetupIfNeeded]_block_invoke.332
+ ___60-[ASRelationshipManager _contactStoreDidChangeNotification:]_block_invoke.429
+ ___64-[ASFriendListManager updateFriendListWithDeletedWorkoutEvents:]_block_invoke.318
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.422
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.426
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.426.cold.1
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.427
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke_2.424
+ ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.345
+ ___65-[ASIDSMessageCenter _handleMessageSendSuccess:error:identifier:]_block_invoke.375
+ ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke.370
+ ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_2.371
+ ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_3.372
+ ___69-[ASDatabaseClient performWhenDataProtectedByFirstUnlockIsAvailable:]_block_invoke.319
+ ___69-[ASRelationshipManager setMuteEnabled:forFriendWithUUID:completion:]_block_invoke.352
+ ___70-[ASActivityDataNotificationManager _queue_selectWorkoutNotifications]_block_invoke.330
+ ___70-[ASDatabaseClient allCodableDatabaseCompetitionListEntriesWithError:]_block_invoke.358
+ ___72-[ASActivityDataManager _ckQueue_handleDeletedWorkoutEvents:completion:]_block_invoke.382
+ ___73-[ASCompetitionManager completeCompetitionWithFriendWithUUID:completion:]_block_invoke.367
+ ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.340
+ ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.341
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.310
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.316
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.312
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.312.cold.1
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.323
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.330
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.334
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke_2.324
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.371
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.375
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.372
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.376
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.373
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.377
+ ___74-[ASRelationshipManager ignoreInviteRequestFromFriendWithUUID:completion:]_block_invoke.380
+ ___76-[ASIDSMessageCenter _sendPayload:type:destinations:fromAddress:completion:]_block_invoke.379
+ ___77-[ASActivityDataNotificationManager _queue_selectGoalCompletionNotifications]_block_invoke.344
+ ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.318
+ ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.318.cold.1
+ ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.318.cold.2
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.319.cold.1
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.319.cold.2
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.319.cold.3
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.322
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.323
+ ___78-[ASCompetitionManager ignoreCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.324
+ ___84-[ASCompetitionManager _queue_cleanUpLegacyCompetitionLists:activity:cloudKitGroup:]_block_invoke.358
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.314
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.316
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.323
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.325
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.327
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.315
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.319
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.326
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.411
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.411.cold.1
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.412
+ ___86-[ASCloudKitManager _performNewAccountTasksCreatingSubscriptions:fetching:completion:]_block_invoke.466
+ ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.325
+ ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.325.cold.1
+ ___89-[ASCompetitionManager _queue_cleanUpSecureCloudCompetitionLists:activity:cloudKitGroup:]_block_invoke.363
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.329
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.330
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.331
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.332
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.333
+ ___93-[ASDatabaseClient deletedHealthKitWorkoutsWithinLastNumberOfDays:maxBatchSize:anchor:error:]_block_invoke.332
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.424
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke_2.425
+ ___96-[ASRelationshipManager saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:]_block_invoke.410
+ ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.367
+ ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.368
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.363
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.364
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.365
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_2.366
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_3.367
+ ___98-[ASActivityDataManager currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:]_block_invoke.356
+ ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.312
+ ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.320
+ ___ASReconcileRelationshipsAgainstAddressBook_block_invoke_2.327
+ ___block_literal_global.297
+ ___block_literal_global.298
+ ___block_literal_global.302
+ ___block_literal_global.304
+ ___block_literal_global.315
+ ___block_literal_global.329
+ ___block_literal_global.333
+ ___block_literal_global.334
+ ___block_literal_global.339
+ ___block_literal_global.344
+ ___block_literal_global.348
+ ___block_literal_global.349
+ ___block_literal_global.353
+ ___block_literal_global.355
+ ___block_literal_global.360
+ ___block_literal_global.365
+ ___block_literal_global.371
+ ___block_literal_global.375
+ ___block_literal_global.380
+ ___block_literal_global.399
+ ___block_literal_global.405
+ ___block_literal_global.409
+ ___block_literal_global.423
+ ___block_literal_global.458
+ ___block_literal_global.472
+ ___block_literal_global.480
+ ___block_literal_global.484
+ ___block_literal_global.489
+ ___block_literal_global.491
+ ___block_literal_global.501
+ ___block_literal_global.505
+ ___block_literal_global.507
+ ___block_literal_global.509
+ ___block_literal_global.519
+ ___block_literal_global.529
+ ___block_literal_global.539
+ ___block_literal_global.549
+ ___block_literal_global.553
+ ___block_literal_global.555
+ ___block_literal_global.557
+ ___block_literal_global.567
+ ___block_literal_global.577
+ ___block_literal_global.581
+ ___block_literal_global.583
+ ___block_literal_global.585
+ ___block_literal_global.589
+ ___block_literal_global.610
+ ___block_literal_global.659
+ ___block_literal_global.661
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke.337
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.338
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.338.cold.1
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_3.339
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.340
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.340.cold.1
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.340.cold.2
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.346
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.346.cold.1
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.347
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.348
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.394
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.395
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.395.cold.1
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_2.396
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.397
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.397.cold.1
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.410
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.411
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.412
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.413
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.413.cold.1
- ___106-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:]_block_invoke.351
- ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.589
- ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.590
- ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.590.cold.1
- ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.332
- ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.334
- ___108-[ASCloudKitManager _performAndRetryNewAccountTasksWithRetryInterval:shouldCreateSubscriptions:shouldFetch:]_block_invoke.464
- ___109-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:]_block_invoke.350
- ___117-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.324
- ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.378
- ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.382
- ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.384
- ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2.385
- ___126-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.388
- ___130-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.389
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.413
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.413.cold.1
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.414
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.414.cold.1
- ___149-[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:group:completion:]_block_invoke.301
- ___153-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.390
- ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.341
- ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.341.cold.1
- ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.343
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.330
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.335
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.337
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.339
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke_2.336
- ___19-[ASXPCClient init]_block_invoke.337
- ___31-[ASGatewayManager updateState]_block_invoke.303
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.307
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.308
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.309
- ___39-[ASContactsManager loadCachedContacts]_block_invoke.323
- ___43-[ASDatabaseClient performWhenDaemonReady:]_block_invoke.313
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.294
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.294.cold.1
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.295
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.295.cold.1
- ___46-[ASAsyncTransactionQueue performTransaction:]_block_invoke.293
- ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.306
- ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.306.cold.1
- ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.307
- ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke.466
- ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke_2.467
- ___48-[ASGatewayManager gatewayStatusWithCompletion:]_block_invoke.300
- ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.391
- ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.392
- ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.392.cold.1
- ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.451
- ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.452
- ___50-[ASCompetitionStore _saveCompetitionLists:owner:]_block_invoke.300
- ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.341
- ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.342
- ___53-[ASIDSMessageCenter donatedAddressesWithCompletion:]_block_invoke.399
- ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.311
- ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.311.cold.1
- ___55-[ASCompetitionTemplateSource templatesWithCompletion:]_block_invoke.290
- ___58-[ASRelationshipManager _processPersistedMessagesIfNeeded]_block_invoke.391
- ___60-[ASActivitySharingManager _mainQueue_completeSetupIfNeeded]_block_invoke.329
- ___60-[ASRelationshipManager _contactStoreDidChangeNotification:]_block_invoke.426
- ___64-[ASFriendListManager updateFriendListWithDeletedWorkoutEvents:]_block_invoke.315
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.419
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.420
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.423.cold.1
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.424
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke_2.421
- ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.339
- ___65-[ASIDSMessageCenter _handleMessageSendSuccess:error:identifier:]_block_invoke.372
- ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke.367
- ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_2.368
- ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_3.369
- ___69-[ASDatabaseClient performWhenDataProtectedByFirstUnlockIsAvailable:]_block_invoke.316
- ___69-[ASRelationshipManager setMuteEnabled:forFriendWithUUID:completion:]_block_invoke.349
- ___70-[ASActivityDataNotificationManager _queue_selectWorkoutNotifications]_block_invoke.327
- ___70-[ASDatabaseClient allCodableDatabaseCompetitionListEntriesWithError:]_block_invoke.355
- ___72-[ASActivityDataManager _ckQueue_handleDeletedWorkoutEvents:completion:]_block_invoke.379
- ___73-[ASCompetitionManager completeCompetitionWithFriendWithUUID:completion:]_block_invoke.364
- ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.337
- ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.338
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.307
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.313
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.309
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.309.cold.1
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.320
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.324
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.331
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke_2.321
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.368
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.372
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.369
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.373
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.370
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.374
- ___74-[ASRelationshipManager ignoreInviteRequestFromFriendWithUUID:completion:]_block_invoke.377
- ___76-[ASIDSMessageCenter _sendPayload:type:destinations:fromAddress:completion:]_block_invoke.376
- ___77-[ASActivityDataNotificationManager _queue_selectGoalCompletionNotifications]_block_invoke.341
- ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.315
- ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.315.cold.1
- ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.315.cold.2
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.316
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.316.cold.1
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.316.cold.2
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.316.cold.3
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.317
- ___78-[ASCompetitionManager ignoreCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.321
- ___84-[ASCompetitionManager _queue_cleanUpLegacyCompetitionLists:activity:cloudKitGroup:]_block_invoke.355
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.311
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.313
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.315
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.317
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.319
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.312
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.316
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.323
- ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.408
- ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.408.cold.1
- ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.409
- ___86-[ASCloudKitManager _performNewAccountTasksCreatingSubscriptions:fetching:completion:]_block_invoke.463
- ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.322
- ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.322.cold.1
- ___89-[ASCompetitionManager _queue_cleanUpSecureCloudCompetitionLists:activity:cloudKitGroup:]_block_invoke.360
- ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.326
- ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.327
- ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.328
- ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.329
- ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.330
- ___93-[ASDatabaseClient deletedHealthKitWorkoutsWithinLastNumberOfDays:maxBatchSize:anchor:error:]_block_invoke.329
- ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.418
- ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke_2.422
- ___96-[ASRelationshipManager saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:]_block_invoke.404
- ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.364
- ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.365
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.358
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.360
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.362
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_2.363
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_3.364
- ___98-[ASActivityDataManager currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:]_block_invoke.353
- ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.309
- ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.317
- ___ASReconcileRelationshipsAgainstAddressBook_block_invoke_2.324
- ___block_literal_global.294
- ___block_literal_global.295
- ___block_literal_global.296
- ___block_literal_global.301
- ___block_literal_global.312
- ___block_literal_global.320
- ___block_literal_global.327
- ___block_literal_global.331
- ___block_literal_global.335
- ___block_literal_global.336
- ___block_literal_global.345
- ___block_literal_global.346
- ___block_literal_global.350
- ___block_literal_global.351
- ___block_literal_global.352
- ___block_literal_global.359
- ___block_literal_global.368
- ___block_literal_global.372
- ___block_literal_global.377
- ___block_literal_global.393
- ___block_literal_global.402
- ___block_literal_global.406
- ___block_literal_global.420
- ___block_literal_global.455
- ___block_literal_global.469
- ___block_literal_global.477
- ___block_literal_global.481
- ___block_literal_global.486
- ___block_literal_global.488
- ___block_literal_global.492
- ___block_literal_global.502
- ___block_literal_global.504
- ___block_literal_global.506
- ___block_literal_global.510
- ___block_literal_global.520
- ___block_literal_global.530
- ___block_literal_global.540
- ___block_literal_global.550
- ___block_literal_global.552
- ___block_literal_global.554
- ___block_literal_global.558
- ___block_literal_global.568
- ___block_literal_global.578
- ___block_literal_global.580
- ___block_literal_global.582
- ___block_literal_global.586
- ___block_literal_global.607
- ___block_literal_global.653
- ___block_literal_global.658
Functions:
~ ___53-[ASIDSMessageCenter donatedAddressesWithCompletion:]_block_invoke_2 : 320 -> 324

```
