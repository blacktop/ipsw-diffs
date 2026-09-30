## ActivitySharingDaemonCore

> `/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`

```diff

-2026.2.1.0.0
+2026.2.3.0.0
   __TEXT.__text: 0x7ddb8
   __TEXT.__auth_stubs: 0xee0
-  __TEXT.__objc_methlist: 0x45c4
+  __TEXT.__objc_methlist: 0x45d4
   __TEXT.__const: 0x1d8
   __TEXT.__cstring: 0x2ffc
   __TEXT.__gcc_except_tab: 0x1004
   __TEXT.__oslogstring: 0xea47
   __TEXT.__unwind_info: 0x1be0
   __TEXT.__objc_classname: 0x9fd
-  __TEXT.__objc_methname: 0x114ce
-  __TEXT.__objc_methtype: 0x2ab0
+  __TEXT.__objc_methname: 0x1150e
+  __TEXT.__objc_methtype: 0x2b08
   __TEXT.__objc_stubs: 0xc700
   __DATA_CONST.__got: 0xa38
   __DATA_CONST.__const: 0x3b88

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3808
+  __DATA_CONST.__objc_selrefs: 0x3810
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x780
   __AUTH_CONST.__const: 0xdc0
   __AUTH_CONST.__cfstring: 0x1e40
-  __AUTH_CONST.__objc_const: 0xdd00
+  __AUTH_CONST.__objc_const: 0xdd08
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3FA196E8-0A7F-32F7-8D1B-117BB19A79D0
+  UUID: 85085176-F0A7-3C91-8D08-1D9A6BC16407
   Functions: 2366
   Symbols:   8822
-  CStrings:  4222
+  CStrings:  4225
 
Symbols:
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke.349
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.350
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.350.cold.1
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_3.351
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.352
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.352.cold.1
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.352.cold.2
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.358
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.358.cold.1
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.359
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.360
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.406
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.407
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.407.cold.1
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_2.408
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.409
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.409.cold.1
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.422
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.423
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.424
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.427
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.425
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.425.cold.1
+ ___106-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:]_block_invoke.363
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.601
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.602
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.602.cold.1
+ ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.355
+ ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.357
+ ___108-[ASCloudKitManager _performAndRetryNewAccountTasksWithRetryInterval:shouldCreateSubscriptions:shouldFetch:]_block_invoke.476
+ ___109-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:]_block_invoke.362
+ ___117-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.336
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.390
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.393
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.394
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.396
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.399
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2.397
+ ___126-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.400
+ ___130-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.401
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.425
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.425.cold.1
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.426
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.426.cold.1
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.428
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.428.cold.1
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.429
+ ___149-[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:group:completion:]_block_invoke.313
+ ___153-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.402
+ ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.353
+ ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.353.cold.1
+ ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.355
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.347
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.349
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.351
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke_2.348
+ ___19-[ASXPCClient init]_block_invoke.349
+ ___31-[ASGatewayManager updateState]_block_invoke.315
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.319
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.320
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.321
+ ___39-[ASContactsManager loadCachedContacts]_block_invoke.335
+ ___43-[ASDatabaseClient performWhenDaemonReady:]_block_invoke.326
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.306
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.306.cold.1
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.307
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.307.cold.1
+ ___46-[ASAsyncTransactionQueue performTransaction:]_block_invoke.305
+ ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.318
+ ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.318.cold.1
+ ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.319
+ ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke.478
+ ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke_2.479
+ ___48-[ASGatewayManager gatewayStatusWithCompletion:]_block_invoke.312
+ ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.403
+ ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.404
+ ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.404.cold.1
+ ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.463
+ ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.464
+ ___50-[ASCompetitionStore _saveCompetitionLists:owner:]_block_invoke.312
+ ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.354
+ ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.355
+ ___53-[ASIDSMessageCenter donatedAddressesWithCompletion:]_block_invoke.411
+ ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.323
+ ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.323.cold.1
+ ___55-[ASCompetitionTemplateSource templatesWithCompletion:]_block_invoke.302
+ ___58-[ASRelationshipManager _processPersistedMessagesIfNeeded]_block_invoke.403
+ ___60-[ASActivitySharingManager _mainQueue_completeSetupIfNeeded]_block_invoke.341
+ ___60-[ASRelationshipManager _contactStoreDidChangeNotification:]_block_invoke.438
+ ___64-[ASFriendListManager updateFriendListWithDeletedWorkoutEvents:]_block_invoke.327
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.431
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.432
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.435
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.435.cold.1
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.436
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke_2.433
+ ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.351
+ ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.354
+ ___65-[ASIDSMessageCenter _handleMessageSendSuccess:error:identifier:]_block_invoke.384
+ ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke.379
+ ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_2.380
+ ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_3.381
+ ___69-[ASDatabaseClient performWhenDataProtectedByFirstUnlockIsAvailable:]_block_invoke.329
+ ___69-[ASRelationshipManager setMuteEnabled:forFriendWithUUID:completion:]_block_invoke.361
+ ___70-[ASActivityDataNotificationManager _queue_selectWorkoutNotifications]_block_invoke.339
+ ___70-[ASDatabaseClient allCodableDatabaseCompetitionListEntriesWithError:]_block_invoke.368
+ ___72-[ASActivityDataManager _ckQueue_handleDeletedWorkoutEvents:completion:]_block_invoke.402
+ ___73-[ASCompetitionManager completeCompetitionWithFriendWithUUID:completion:]_block_invoke.376
+ ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.349
+ ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.350
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.319
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.325
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.321
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.321.cold.1
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.332
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.336
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.339
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.343
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke_2.333
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.380
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.384
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.381
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.385
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.382
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.386
+ ___74-[ASRelationshipManager ignoreInviteRequestFromFriendWithUUID:completion:]_block_invoke.389
+ ___76-[ASIDSMessageCenter _sendPayload:type:destinations:fromAddress:completion:]_block_invoke.388
+ ___77-[ASActivityDataNotificationManager _queue_selectGoalCompletionNotifications]_block_invoke.353
+ ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.327
+ ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.327.cold.1
+ ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.327.cold.2
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.328
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.328.cold.1
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.328.cold.2
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.328.cold.3
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.331
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.329
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.332
+ ___78-[ASCompetitionManager ignoreCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.333
+ ___84-[ASCompetitionManager _queue_cleanUpLegacyCompetitionLists:activity:cloudKitGroup:]_block_invoke.367
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.330
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.331
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.332
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.333
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.334
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.335
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.337
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.325
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.329
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.336
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.420
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.420.cold.1
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.421
+ ___86-[ASCloudKitManager _performNewAccountTasksCreatingSubscriptions:fetching:completion:]_block_invoke.475
+ ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.334
+ ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.334.cold.1
+ ___89-[ASCompetitionManager _queue_cleanUpSecureCloudCompetitionLists:activity:cloudKitGroup:]_block_invoke.372
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.338
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.339
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.340
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.341
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.342
+ ___93-[ASDatabaseClient deletedHealthKitWorkoutsWithinLastNumberOfDays:maxBatchSize:anchor:error:]_block_invoke.342
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.430
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.433
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke_2.434
+ ___96-[ASRelationshipManager saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:]_block_invoke.416
+ ___96-[ASRelationshipManager saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:]_block_invoke.419
+ ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.387
+ ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.388
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.370
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.372
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.373
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.374
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_2.375
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_3.376
+ ___98-[ASActivityDataManager currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:]_block_invoke.376
+ ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.321
+ ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.329
+ ___ASReconcileRelationshipsAgainstAddressBook_block_invoke_2.336
+ ___block_literal_global.306
+ ___block_literal_global.307
+ ___block_literal_global.308
+ ___block_literal_global.311
+ ___block_literal_global.313
+ ___block_literal_global.324
+ ___block_literal_global.332
+ ___block_literal_global.335
+ ___block_literal_global.342
+ ___block_literal_global.343
+ ___block_literal_global.347
+ ___block_literal_global.350
+ ___block_literal_global.358
+ ___block_literal_global.364
+ ___block_literal_global.366
+ ___block_literal_global.369
+ ___block_literal_global.371
+ ___block_literal_global.372
+ ___block_literal_global.374
+ ___block_literal_global.395
+ ___block_literal_global.400
+ ___block_literal_global.408
+ ___block_literal_global.414
+ ___block_literal_global.418
+ ___block_literal_global.432
+ ___block_literal_global.467
+ ___block_literal_global.481
+ ___block_literal_global.493
+ ___block_literal_global.500
+ ___block_literal_global.504
+ ___block_literal_global.510
+ ___block_literal_global.514
+ ___block_literal_global.518
+ ___block_literal_global.522
+ ___block_literal_global.525
+ ___block_literal_global.528
+ ___block_literal_global.532
+ ___block_literal_global.535
+ ___block_literal_global.538
+ ___block_literal_global.542
+ ___block_literal_global.545
+ ___block_literal_global.548
+ ___block_literal_global.552
+ ___block_literal_global.558
+ ___block_literal_global.562
+ ___block_literal_global.566
+ ___block_literal_global.570
+ ___block_literal_global.573
+ ___block_literal_global.576
+ ___block_literal_global.580
+ ___block_literal_global.586
+ ___block_literal_global.590
+ ___block_literal_global.592
+ ___block_literal_global.594
+ ___block_literal_global.598
+ ___block_literal_global.619
+ ___block_literal_global.676
+ ___block_literal_global.679
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke.340
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.341
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.341.cold.1
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_3.342
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.343
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.343.cold.1
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.343.cold.2
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.349
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.349.cold.1
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.350
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.351
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.397
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.398
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.398.cold.1
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_2.399
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.400
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.400.cold.1
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.413
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.414
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.415
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.418
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.416
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.416.cold.1
- ___106-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:]_block_invoke.354
- ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.592
- ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.593
- ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.593.cold.1
- ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.346
- ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.348
- ___108-[ASCloudKitManager _performAndRetryNewAccountTasksWithRetryInterval:shouldCreateSubscriptions:shouldFetch:]_block_invoke.467
- ___109-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:]_block_invoke.353
- ___117-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.327
- ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.381
- ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.384
- ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.385
- ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.387
- ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.390
- ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2.388
- ___126-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.391
- ___130-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.392
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.416
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.416.cold.1
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.417
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.417.cold.1
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.419
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.419.cold.1
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.420
- ___149-[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:group:completion:]_block_invoke.304
- ___153-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.393
- ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.344
- ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.344.cold.1
- ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.346
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.333
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.338
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.340
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke_2.339
- ___19-[ASXPCClient init]_block_invoke.340
- ___31-[ASGatewayManager updateState]_block_invoke.306
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.310
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.311
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.312
- ___39-[ASContactsManager loadCachedContacts]_block_invoke.326
- ___43-[ASDatabaseClient performWhenDaemonReady:]_block_invoke.317
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.297
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.297.cold.1
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.298
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.298.cold.1
- ___46-[ASAsyncTransactionQueue performTransaction:]_block_invoke.296
- ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.309
- ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.309.cold.1
- ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.310
- ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke.469
- ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke_2.470
- ___48-[ASGatewayManager gatewayStatusWithCompletion:]_block_invoke.303
- ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.394
- ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.395
- ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.395.cold.1
- ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.454
- ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.455
- ___50-[ASCompetitionStore _saveCompetitionLists:owner:]_block_invoke.303
- ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.345
- ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.346
- ___53-[ASIDSMessageCenter donatedAddressesWithCompletion:]_block_invoke.402
- ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.314
- ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.314.cold.1
- ___55-[ASCompetitionTemplateSource templatesWithCompletion:]_block_invoke.293
- ___58-[ASRelationshipManager _processPersistedMessagesIfNeeded]_block_invoke.394
- ___60-[ASActivitySharingManager _mainQueue_completeSetupIfNeeded]_block_invoke.332
- ___60-[ASRelationshipManager _contactStoreDidChangeNotification:]_block_invoke.429
- ___64-[ASFriendListManager updateFriendListWithDeletedWorkoutEvents:]_block_invoke.318
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.422
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.423
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.426
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.426.cold.1
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.427
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke_2.424
- ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.342
- ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.345
- ___65-[ASIDSMessageCenter _handleMessageSendSuccess:error:identifier:]_block_invoke.375
- ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke.370
- ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_2.371
- ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_3.372
- ___69-[ASDatabaseClient performWhenDataProtectedByFirstUnlockIsAvailable:]_block_invoke.320
- ___69-[ASRelationshipManager setMuteEnabled:forFriendWithUUID:completion:]_block_invoke.352
- ___70-[ASActivityDataNotificationManager _queue_selectWorkoutNotifications]_block_invoke.330
- ___70-[ASDatabaseClient allCodableDatabaseCompetitionListEntriesWithError:]_block_invoke.359
- ___72-[ASActivityDataManager _ckQueue_handleDeletedWorkoutEvents:completion:]_block_invoke.393
- ___73-[ASCompetitionManager completeCompetitionWithFriendWithUUID:completion:]_block_invoke.367
- ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.340
- ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.341
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.310
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.316
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.312
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.312.cold.1
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.323
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.327
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.330
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.334
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke_2.324
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.371
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.375
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.372
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.376
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.373
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.377
- ___74-[ASRelationshipManager ignoreInviteRequestFromFriendWithUUID:completion:]_block_invoke.380
- ___76-[ASIDSMessageCenter _sendPayload:type:destinations:fromAddress:completion:]_block_invoke.379
- ___77-[ASActivityDataNotificationManager _queue_selectGoalCompletionNotifications]_block_invoke.344
- ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.318
- ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.318.cold.1
- ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.318.cold.2
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.319
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.319.cold.1
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.319.cold.2
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.319.cold.3
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.322
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.320
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.323
- ___78-[ASCompetitionManager ignoreCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.324
- ___84-[ASCompetitionManager _queue_cleanUpLegacyCompetitionLists:activity:cloudKitGroup:]_block_invoke.358
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.315
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.317
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.319
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.321
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.322
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.323
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.325
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.316
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.320
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.327
- ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.411
- ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.411.cold.1
- ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.412
- ___86-[ASCloudKitManager _performNewAccountTasksCreatingSubscriptions:fetching:completion:]_block_invoke.466
- ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.325
- ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.325.cold.1
- ___89-[ASCompetitionManager _queue_cleanUpSecureCloudCompetitionLists:activity:cloudKitGroup:]_block_invoke.363
- ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.329
- ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.330
- ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.331
- ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.332
- ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.333
- ___93-[ASDatabaseClient deletedHealthKitWorkoutsWithinLastNumberOfDays:maxBatchSize:anchor:error:]_block_invoke.333
- ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.421
- ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.424
- ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke_2.425
- ___96-[ASRelationshipManager saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:]_block_invoke.407
- ___96-[ASRelationshipManager saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:]_block_invoke.410
- ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.378
- ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.379
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.361
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.363
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.364
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.365
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_2.366
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_3.367
- ___98-[ASActivityDataManager currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:]_block_invoke.367
- ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.312
- ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.320
- ___ASReconcileRelationshipsAgainstAddressBook_block_invoke_2.327
- ___block_literal_global.297
- ___block_literal_global.298
- ___block_literal_global.299
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.315
- ___block_literal_global.323
- ___block_literal_global.326
- ___block_literal_global.329
- ___block_literal_global.330
- ___block_literal_global.333
- ___block_literal_global.334
- ___block_literal_global.341
- ___block_literal_global.344
- ___block_literal_global.349
- ___block_literal_global.354
- ___block_literal_global.355
- ___block_literal_global.360
- ___block_literal_global.365
- ___block_literal_global.382
- ___block_literal_global.386
- ___block_literal_global.396
- ___block_literal_global.399
- ___block_literal_global.409
- ___block_literal_global.423
- ___block_literal_global.458
- ___block_literal_global.472
- ___block_literal_global.480
- ___block_literal_global.484
- ___block_literal_global.491
- ___block_literal_global.495
- ___block_literal_global.501
- ___block_literal_global.505
- ___block_literal_global.509
- ___block_literal_global.513
- ___block_literal_global.519
- ___block_literal_global.523
- ___block_literal_global.526
- ___block_literal_global.529
- ___block_literal_global.533
- ___block_literal_global.536
- ___block_literal_global.539
- ___block_literal_global.543
- ___block_literal_global.546
- ___block_literal_global.549
- ___block_literal_global.553
- ___block_literal_global.557
- ___block_literal_global.561
- ___block_literal_global.567
- ___block_literal_global.571
- ___block_literal_global.574
- ___block_literal_global.577
- ___block_literal_global.581
- ___block_literal_global.585
- ___block_literal_global.589
- ___block_literal_global.610
- ___block_literal_global.661
- ___block_literal_global.667
CStrings:
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"

```
