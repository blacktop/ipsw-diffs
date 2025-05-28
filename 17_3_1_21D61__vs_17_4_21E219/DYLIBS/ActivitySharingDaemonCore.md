## ActivitySharingDaemonCore

> `/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`

```diff

-752.3.0.0.0
-  __TEXT.__text: 0x6cb24
+752.6.0.0.0
+  __TEXT.__text: 0x6e874
   __TEXT.__auth_stubs: 0xe90
-  __TEXT.__objc_methlist: 0x34e0
+  __TEXT.__objc_methlist: 0x34f0
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x29cd
-  __TEXT.__gcc_except_tab: 0xad4
-  __TEXT.__oslogstring: 0xd3f0
-  __TEXT.__unwind_info: 0x17c0
+  __TEXT.__cstring: 0x2a6e
+  __TEXT.__gcc_except_tab: 0xad8
+  __TEXT.__oslogstring: 0xd49b
+  __TEXT.__unwind_info: 0x1828
   __TEXT.__objc_classname: 0xa00
-  __TEXT.__objc_methname: 0xed6d
-  __TEXT.__objc_methtype: 0x2771
-  __TEXT.__objc_stubs: 0xb140
+  __TEXT.__objc_methname: 0xf017
+  __TEXT.__objc_methtype: 0x28d6
+  __TEXT.__objc_stubs: 0xb180
   __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0x3388
+  __DATA_CONST.__const: 0x34a0
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xdbf0
-  __DATA_CONST.__objc_selrefs: 0x2f80
+  __DATA_CONST.__objc_selrefs: 0x2f90
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x5e0
+  __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__cfstring: 0x1a60
-  __AUTH_CONST.__const: 0x960
+  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__const: 0xa40
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_const: 0x1398
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__auth_got: 0x758
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x5d8
-  __DATA.__objc_superrefs: 0x130
   __DATA.__objc_ivar: 0x564
   __DATA.__data: 0xea0
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0xa0
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2104
-  Symbols:   7872
-  CStrings:  3599
+  Functions: 2121
+  Symbols:   7930
+  CStrings:  3615
 
Symbols:
+ -[ASActivityDataManager loadLocalActivityDataIfNeeded]
+ -[ASActivityDataManager periodicUpdateManager:didFailToSaveRecords:activity:]
+ -[ASActivityDataManager periodicUpdateManager:didSaveRecords:activity:]
+ -[ASActivityDataNotificationManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]
+ -[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]
+ -[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:completion:]
+ -[ASCloudKitManager _handleNewPrivateDatabaseRecordChanges:sharedDatabaseRecordChanges:fetchType:activity:cloudKitGroup:]
+ -[ASCloudKitManager _observerQueue_notifyObserversOfEndUpdatesForFetchWithType:activity:cloudKitGroup:]
+ -[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]
+ -[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:group:completion:]
+ -[ASCloudKitManager addParticipantWithCloudKitAddress:toShares:group:completion:]
+ -[ASCloudKitManager fetchAllChangesIfTimeSinceLastFetchIsGreaterThan:priority:activity:group:completion:]
+ -[ASCloudKitManager fetchAllChangesWithPriority:activity:group:completion:]
+ -[ASCloudKitManager fetchOrCreateActivityDataShareWithGroup:activity:completion:]
+ -[ASCloudKitManager fetchShareParticipantWithCloudKitAddress:group:completion:]
+ -[ASCloudKitManager fetchShareWithShareRecordID:activity:group:completion:]
+ -[ASCloudKitManager forceSaveRecordsIntoPrivateDatabaseIgnoringServerChanges:recordIDsToDelete:priority:activity:group:completion:]
+ -[ASCloudKitManager removeParticipantWithCloudKitAddress:fromShares:group:completion:]
+ -[ASCloudKitManager saveRecordsIntoPrivateDatabase:priority:activity:group:completion:]
+ -[ASCloudKitUtility _createRecordZonesWithIDs:priority:useZoneWideSharing:group:completion:]
+ -[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:completion:]
+ -[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]
+ -[ASCloudKitUtility _fetchShareParticipantForLookupInfos:group:completion:]
+ -[ASCloudKitUtility _fetchShareWithShareRecordID:activity:group:completion:]
+ -[ASCloudKitUtility _saveRecordsIntoPrivateDatabase:recordIDsToDelete:savePolicy:priority:activity:group:completion:]
+ -[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:group:completion:]
+ -[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:group:completion:]
+ -[ASCloudKitUtility fetchChangesInPrivateDatabaseWithServerChangeTokenCache:priority:activity:group:completion:]
+ -[ASCloudKitUtility fetchChangesInSharedDatabaseWithServerChangeTokenCache:priority:activity:group:completion:]
+ -[ASCloudKitUtility fetchShareParticipantForEmailAddress:group:completion:]
+ -[ASCloudKitUtility fetchShareWithShareRecordID:activity:group:completion:]
+ -[ASCloudKitUtility forceSaveRecordsIntoPrivateDatabaseIgnoringServerChanges:recordIDsToDelete:priority:activity:group:completion:]
+ -[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]
+ -[ASCloudKitUtility saveRecordsIntoPrivateDatabase:priority:activity:group:completion:]
+ -[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]
+ -[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]
+ -[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:activity:cloudKitGroup:completion:]
+ -[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:activity:cloudKitGroup:completion:].cold.1
+ -[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:activity:cloudKitGroup:completion:].cold.2
+ -[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]
+ -[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:activity:cloudKitGroup:]
+ -[ASCompetitionManager _saveCurrentCompetitionList:archivedCompetitionList:contact:activity:cloudKitGroup:completion:]
+ -[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]
+ -[ASCompetitionManager periodicUpdateManager:didFailToSaveRecords:activity:]
+ -[ASCompetitionManager periodicUpdateManager:didSaveRecords:activity:]
+ -[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]
+ -[ASPeriodicUpdateManager requestImmediateUpdateWithCloudKitGroup:completion:]
+ -[ASRelationshipManager _queue_addPersonWithCloudKitAddress:toShares:cloudKitGroup:completion:]
+ -[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]
+ -[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]
+ -[ASRelationshipManager _queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:]
+ -[ASRelationshipManager _queue_saveRelationship:contact:activity:cloudKitGroup:completion:]
+ -[ASRelationshipManager _queue_saveRelationship:contact:withExtraRecords:activity:cloudKitGroup:completion:]
+ -[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]
+ -[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:]
+ -[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:]
+ -[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:]
+ GCC_except_table104
+ GCC_except_table108
+ GCC_except_table116
+ GCC_except_table135
+ _ASCloudKitGroupCoreDuetTriggered
+ _ASCloudKitGroupCoreDuetTriggered.__group
+ _ASCloudKitGroupCoreDuetTriggered.onceToken
+ _ASCloudKitGroupInitialDownload
+ _ASCloudKitGroupInitialDownload.__group
+ _ASCloudKitGroupInitialDownload.onceToken
+ _ASCloudKitGroupInitialSetup
+ _ASCloudKitGroupInitialSetup.__group
+ _ASCloudKitGroupInitialSetup.onceToken
+ _ASCloudKitGroupPushTriggered
+ _ASCloudKitGroupPushTriggered.__group
+ _ASCloudKitGroupPushTriggered.onceToken
+ _ASCloudKitGroupSharingSetup
+ _ASCloudKitGroupSharingSetup.__group
+ _ASCloudKitGroupSharingSetup.onceToken
+ _ASCloudKitGroupUserActionExplicit
+ _ASCloudKitGroupUserActionExplicit.__group
+ _ASCloudKitGroupUserActionExplicit.onceToken
+ _ASCloudKitGroupUserActionImplicit
+ _ASCloudKitGroupUserActionImplicit.__group
+ _ASCloudKitGroupUserActionImplicit.onceToken
+ _OBJC_CLASS_$_CKOperationGroup
+ ___100-[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:activity:cloudKitGroup:]_block_invoke
+ ___100-[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:activity:cloudKitGroup:]_block_invoke_2
+ ___100-[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:activity:cloudKitGroup:]_block_invoke_3
+ ___100-[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:activity:cloudKitGroup:]_block_invoke_4
+ ___100-[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:activity:cloudKitGroup:]_block_invoke_5
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.295
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.295.cold.1
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.296
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.297
+ ___103-[ASCloudKitManager _observerQueue_notifyObserversOfEndUpdatesForFetchWithType:activity:cloudKitGroup:]_block_invoke
+ ___103-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:completion:]_block_invoke
+ ___103-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:completion:]_block_invoke.282
+ ___103-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:completion:]_block_invoke.282.cold.1
+ ___103-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:completion:]_block_invoke.284
+ ___103-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:completion:]_block_invoke_2
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.347
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.348
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.349
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.352
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.cold.1
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.350
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.350.cold.1
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.cold.1
+ ___105-[ASCloudKitManager fetchAllChangesIfTimeSinceLastFetchIsGreaterThan:priority:activity:group:completion:]_block_invoke
+ ___105-[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:activity:cloudKitGroup:completion:]_block_invoke
+ ___105-[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:activity:cloudKitGroup:completion:]_block_invoke_2
+ ___105-[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:activity:cloudKitGroup:completion:]_block_invoke_3
+ ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.322
+ ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.325
+ ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.326
+ ___106-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:]_block_invoke
+ ___106-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:]_block_invoke.297
+ ___106-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:]_block_invoke_2
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.487
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.488
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.488.cold.1
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke_2
+ ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke.328
+ ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke.331
+ ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke_2.329
+ ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.280
+ ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.282
+ ___108-[ASCloudKitManager _performAndRetryNewAccountTasksWithRetryInterval:shouldCreateSubscriptions:shouldFetch:]_block_invoke.390
+ ___108-[ASRelationshipManager _queue_saveRelationship:contact:withExtraRecords:activity:cloudKitGroup:completion:]_block_invoke
+ ___108-[ASRelationshipManager _queue_saveRelationship:contact:withExtraRecords:activity:cloudKitGroup:completion:]_block_invoke_2
+ ___108-[ASRelationshipManager _queue_saveRelationship:contact:withExtraRecords:activity:cloudKitGroup:completion:]_block_invoke_2.cold.1
+ ___109-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:]_block_invoke
+ ___109-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:]_block_invoke.296
+ ___109-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:]_block_invoke_2
+ ___109-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:]_block_invoke_2.cold.1
+ ___110-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:messageHandledCompletion:]_block_invoke.332
+ ___113-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:group:completion:]_block_invoke
+ ___113-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:group:completion:]_block_invoke.346
+ ___113-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:group:completion:]_block_invoke.346.cold.1
+ ___113-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:group:completion:]_block_invoke.347
+ ___113-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:group:completion:]_block_invoke.cold.1
+ ___114-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.333
+ ___117-[ASCloudKitUtility _saveRecordsIntoPrivateDatabase:recordIDsToDelete:savePolicy:priority:activity:group:completion:]_block_invoke
+ ___117-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke
+ ___117-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.273
+ ___117-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.cold.1
+ ___118-[ASCompetitionManager _saveCurrentCompetitionList:archivedCompetitionList:contact:activity:cloudKitGroup:completion:]_block_invoke
+ ___118-[ASCompetitionManager _saveCurrentCompetitionList:archivedCompetitionList:contact:activity:cloudKitGroup:completion:]_block_invoke_2
+ ___121-[ASCloudKitManager _handleNewPrivateDatabaseRecordChanges:sharedDatabaseRecordChanges:fetchType:activity:cloudKitGroup:]_block_invoke
+ ___122-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke
+ ___122-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.277
+ ___122-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.279
+ ___122-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.280
+ ___122-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke_2
+ ___122-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke_2.278
+ ___122-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke_3
+ ___122-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke_3.cold.1
+ ___130-[ASActivityDataNotificationManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke
+ ___149-[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:group:completion:]_block_invoke
+ ___149-[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:group:completion:]_block_invoke.247
+ ___153-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke
+ ___153-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.334
+ ___153-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.cold.1
+ ___19-[ASXPCClient init]_block_invoke.286
+ ___31-[ASGatewayManager updateState]_block_invoke.255
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.256
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.257
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.258
+ ___39-[ASContactsManager loadCachedContacts]_block_invoke.271
+ ___43-[ASDatabaseClient performWhenDaemonReady:]_block_invoke.262
+ ___46-[ASAsyncTransactionQueue performTransaction:]_block_invoke.242
+ ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke.392
+ ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke_2.393
+ ___48-[ASGatewayManager gatewayStatusWithCompletion:]_block_invoke.252
+ ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.378
+ ___50-[ASCompetitionStore _saveCompetitionLists:owner:]_block_invoke.249
+ ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.290
+ ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.291
+ ___54-[ASActivityDataManager loadLocalActivityDataIfNeeded]_block_invoke
+ ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.257
+ ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.257.cold.1
+ ___58-[ASRelationshipManager _processPersistedMessagesIfNeeded]_block_invoke.335
+ ___60-[ASActivitySharingManager _mainQueue_completeSetupIfNeeded]_block_invoke.278
+ ___60-[ASRelationshipManager _contactStoreDidChangeNotification:]_block_invoke.399
+ ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.356
+ ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.356.cold.1
+ ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.356.cold.2
+ ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.356.cold.3
+ ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.356.cold.4
+ ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.356.cold.5
+ ___64-[ASActivityDataManager achievementStore:didUpdateAchievements:]_block_invoke.277
+ ___64-[ASCloudKitUtility _acceptSharesWithURLs:operation:completion:]_block_invoke.261
+ ___64-[ASCloudKitUtility _acceptSharesWithURLs:operation:completion:]_block_invoke.261.cold.1
+ ___64-[ASCloudKitUtility _acceptSharesWithURLs:operation:completion:]_block_invoke.261.cold.2
+ ___64-[ASFriendListManager updateFriendListWithDeletedWorkoutEvents:]_block_invoke.261
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.349
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.350
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.353
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.353.cold.1
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.354
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke_2
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke_2.351
+ ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.288
+ ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.291
+ ___69-[ASDatabaseClient performWhenDataProtectedByFirstUnlockIsAvailable:]_block_invoke.265
+ ___69-[ASRelationshipManager setMuteEnabled:forFriendWithUUID:completion:]_block_invoke.295
+ ___70-[ASActivityDataNotificationManager _queue_selectWorkoutNotifications]_block_invoke.276
+ ___70-[ASCompetitionManager periodicUpdateManager:didSaveRecords:activity:]_block_invoke
+ ___70-[ASDatabaseClient allCodableDatabaseCompetitionListEntriesWithError:]_block_invoke.304
+ ___71-[ASActivityDataManager periodicUpdateManager:didSaveRecords:activity:]_block_invoke
+ ___72-[ASActivityDataManager _ckQueue_handleDeletedWorkoutEvents:completion:]_block_invoke.327
+ ___73-[ASCompetitionManager completeCompetitionWithFriendWithUUID:completion:]_block_invoke.301
+ ___73-[ASCompetitionManager updateAllActiveCompetitionsWithScores:completion:]_block_invoke.303
+ ___73-[ASCompetitionManager updateAllActiveCompetitionsWithScores:completion:]_block_invoke_2.304
+ ___73-[ASRelationshipManager _queue_reconcileAddressBookAgainstRelationships:]_block_invoke.357
+ ___73-[ASRelationshipManager _queue_reconcileAddressBookAgainstRelationships:]_block_invoke.365
+ ___73-[ASRelationshipManager _queue_reconcileAddressBookAgainstRelationships:]_block_invoke_2.372
+ ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.286
+ ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.287
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.256
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.262
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.258
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.258.cold.1
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.269
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.273
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.276
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.280
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke_2.270
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.313
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.316
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.314
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.317
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.318
+ ___74-[ASRelationshipManager ignoreInviteRequestFromFriendWithUUID:completion:]_block_invoke.321
+ ___75-[ASCloudKitUtility _fetchShareParticipantForLookupInfos:group:completion:]_block_invoke
+ ___75-[ASCloudKitUtility _fetchShareParticipantForLookupInfos:group:completion:]_block_invoke_2
+ ___75-[ASCloudKitUtility fetchShareWithShareRecordID:activity:group:completion:]_block_invoke
+ ___75-[ASCloudKitUtility fetchShareWithShareRecordID:activity:group:completion:]_block_invoke.cold.1
+ ___76-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:completion:]_block_invoke
+ ___76-[ASCloudKitUtility _fetchShareWithShareRecordID:activity:group:completion:]_block_invoke
+ ___76-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:completion:]_block_invoke.282
+ ___76-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:completion:]_block_invoke_2.283
+ ___76-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:completion:]_block_invoke_2.283.cold.1
+ ___76-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:completion:]_block_invoke_3.284
+ ___77-[ASActivityDataManager periodicUpdateManager:didFailToSaveRecords:activity:]_block_invoke
+ ___77-[ASActivityDataNotificationManager _queue_selectGoalCompletionNotifications]_block_invoke.290
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.265
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.265.cold.1
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.265.cold.2
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.265.cold.3
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.268
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.266
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.269
+ ___78-[ASCompetitionManager ignoreCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.270
+ ___78-[ASPeriodicUpdateManager requestImmediateUpdateWithCloudKitGroup:completion:]_block_invoke
+ ___81-[ASCloudKitManager fetchOrCreateActivityDataShareWithGroup:activity:completion:]_block_invoke
+ ___81-[ASCloudKitManager fetchOrCreateActivityDataShareWithGroup:activity:completion:]_block_invoke_2
+ ___81-[ASCloudKitManager fetchOrCreateActivityDataShareWithGroup:activity:completion:]_block_invoke_3
+ ___81-[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:group:completion:]_block_invoke
+ ___81-[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:group:completion:]_block_invoke.265
+ ___81-[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:group:completion:]_block_invoke.265.cold.1
+ ___81-[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:group:completion:]_block_invoke.cold.1
+ ___81-[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:group:completion:]_block_invoke.cold.2
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.24
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.26
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.28
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.29
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.30
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.31
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.25
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_3
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.345
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.345.cold.1
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.346
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.cold.1
+ ___86-[ASCloudKitManager _performNewAccountTasksCreatingSubscriptions:fetching:completion:]_block_invoke.389
+ ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke
+ ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.267
+ ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.267.cold.1
+ ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.cold.1
+ ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.cold.2
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.275
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.276
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.277
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.cold.1
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke_2
+ ___91-[ASRelationshipManager _queue_saveRelationship:contact:activity:cloudKitGroup:completion:]_block_invoke
+ ___92-[ASCloudKitUtility _createRecordZonesWithIDs:priority:useZoneWideSharing:group:completion:]_block_invoke
+ ___92-[ASCloudKitUtility _createRecordZonesWithIDs:priority:useZoneWideSharing:group:completion:]_block_invoke.cold.1
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.278
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.279
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.cold.1
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.cold.2
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke_2
+ ___93-[ASDatabaseClient deletedHealthKitWorkoutsWithinLastNumberOfDays:maxBatchSize:anchor:error:]_block_invoke.278
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.396
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.397
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke_2
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke_2.cold.1
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke_2.cold.2
+ ___95-[ASRelationshipManager _queue_addPersonWithCloudKitAddress:toShares:cloudKitGroup:completion:]_block_invoke
+ ___95-[ASRelationshipManager _queue_addPersonWithCloudKitAddress:toShares:cloudKitGroup:completion:]_block_invoke_2
+ ___95-[ASRelationshipManager _queue_addPersonWithCloudKitAddress:toShares:cloudKitGroup:completion:]_block_invoke_2.cold.1
+ ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.312
+ ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.313
+ ___97-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke
+ ___97-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.338
+ ___97-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.339
+ ___97-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.339.cold.1
+ ___97-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.cold.1
+ ___97-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_2
+ ___97-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_2.340
+ ___97-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3
+ ___97-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.341
+ ___97-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.341.cold.1
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.304
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.306
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.307
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_2.308
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_3.309
+ ___98-[ASActivityDataManager currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:]_block_invoke.301
+ ___ASCloudKitGroupCoreDuetTriggered_block_invoke
+ ___ASCloudKitGroupInitialDownload_block_invoke
+ ___ASCloudKitGroupInitialSetup_block_invoke
+ ___ASCloudKitGroupPushTriggered_block_invoke
+ ___ASCloudKitGroupSharingSetup_block_invoke
+ ___ASCloudKitGroupUserActionExplicit_block_invoke
+ ___ASCloudKitGroupUserActionImplicit_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72bs80r88w_e44_v28?0"CKServerChangeToken"8B16"NSError"20lw88l8s32l8s40l8s48l8r80l8s56l8s64l8s72l8
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs96bs_e44_v36?0B8"NSError"12"CKShare"20"CKShare"28ls88l8s96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs96bs_e63_v44?0B8"NSError"12"CKShare"20"CKShare"28"ASRelationship"36ls32l8s40l8s88l8s96l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8s96l8s72l8s80l8s88l8
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96bs_e20_v20?0B8"NSError"12ls32l8s40l8s96l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e9_B16?0^8ls32l8s40l8s48l8s56l8r96l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80bs_e32_v28?0B8"NSError"12"NSArray"20ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88r96r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r88l8r96l8s72l8s80l8
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_106_e8_32s40s48s56s64s72s80s88bs96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s88l8s96l8s80l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96bs104bs_e39_v28?0B8"NSError"12"ASRelationship"20ls96l8s104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_113_e8_32s40s48s56s64s72s80s88bs96w_e17_v16?0"NSError"8lw96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_116_e8_32s40s48s56s64s72s80s88s96bs104bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96bs104bs_e44_v36?0B8"NSError"12"CKShare"20"CKShare"28ls32l8s40l8s96l8s104l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_120_e8_32s40s48s56s64s72s80s88s96s104bs112bs_e20_v20?0B8"NSError"12ls104l8s112l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112bs120bs_e20_v20?0B8"NSError"12ls32l8s40l8s112l8s120l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_32_e158_v68?0"ASCloudKitManager"8"<ASCloudKitManagerChangesObserver>"16"CKRecordZoneID"24B32"NSArray"36"NSObject<OS_xpc_object>"44"CKOperationGroup"52?<v?>60l
+ ___block_descriptor_56_e8_32s40s48bs_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_66_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls56l8s32l8s40l8s48l8
+ ___block_descriptor_66_e8_32s40s48s56bs_e34_v28?0B8"NSError"12"ASContact"20ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e20_v20?0B8"NSError"12ls56l8s64l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e43_v28?0B8"NSError"12"CKShareParticipant"20ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e12_"NSSet"8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e43_v32?0"CKRecordID"8"ASRelationship"16^B24ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_74_e8_32s40s48s56s64bs_e14_v16?0?<v?>8ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_74_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_74_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_75_e8_32s40s48s56s64bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_75_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls32l8s40l8s64l8s48l8s56l8
+ ___block_descriptor_75_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8r64l8r72l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e14_v16?0?<v?>8ls32l8s40l8s72l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e20_v20?0B8"NSError"12ls72l8s32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72s_e9_B16?0^8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s_e44_v36?0B8"NSError"12"NSArray"20"NSArray"28ls32l8s40l8s48l8s56l8
+ ___block_descriptor_82_e8_32s40s48s56s64s72bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_descriptor_82_e8_32s40s48s56s64s72bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_descriptor_82_e8_32s40s48s56s64s72bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s72l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64bs72bs80bs_e32_v28?0B8"NSError"12"CKShare"20ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80bs_e20_v20?0B8"NSError"12ls32l8s40l8s72l8s80l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s40l8s48l8s56l8s72l8s64l8s80l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e32_v28?0B8"NSError"12"NSArray"20ls32l8s40l8s48l8r72l8r80l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e20_v20?0B8"NSError"12ls80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e40_v32?0"CKRecordZoneID"8"NSArray"16^B24ls32l8s40l8s48l8r80l8s56l8s64l8s72l8
+ ___block_descriptor_90_e8_32s40s48s56s64s72bs80bs_e34_v28?0B8"NSError"12"ASContact"20ls32l8s40l8s48l8s72l8s80l8s56l8s64l8
+ ___block_descriptor_91_e8_32s40s48s56s64s72bs80bs_e32_v28?0B8"NSError"12"CKShare"20ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72bs_e32_v28?0B8"NSError"12"NSArray"20ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s88l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80bs88bs_e5_v8?0ls32l8s40l8s48l8s80l8s88l8s56l8s64l8s72l8
+ ___block_descriptor_99_e8_32s40s48s56s64s72s80bs88bs_e43_v28?0B8"NSError"12"CKShareParticipant"20ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.12
+ ___block_literal_global.17
+ ___block_literal_global.22
+ ___block_literal_global.243
+ ___block_literal_global.244
+ ___block_literal_global.245
+ ___block_literal_global.250
+ ___block_literal_global.27
+ ___block_literal_global.272
+ ___block_literal_global.275
+ ___block_literal_global.279
+ ___block_literal_global.287
+ ___block_literal_global.294
+ ___block_literal_global.300
+ ___block_literal_global.308
+ ___block_literal_global.316
+ ___block_literal_global.32
+ ___block_literal_global.320
+ ___block_literal_global.325
+ ___block_literal_global.337
+ ___block_literal_global.368
+ ___block_literal_global.37
+ ___block_literal_global.374
+ ___block_literal_global.381
+ ___block_literal_global.384
+ ___block_literal_global.389
+ ___block_literal_global.395
+ ___block_literal_global.403
+ ___block_literal_global.407
+ ___block_literal_global.414
+ ___block_literal_global.421
+ ___block_literal_global.424
+ ___block_literal_global.430
+ ___block_literal_global.436
+ ___block_literal_global.439
+ ___block_literal_global.446
+ ___block_literal_global.449
+ ___block_literal_global.459
+ ___block_literal_global.462
+ ___block_literal_global.466
+ ___block_literal_global.469
+ ___block_literal_global.472
+ ___block_literal_global.476
+ ___block_literal_global.478
+ ___block_literal_global.480
+ ___block_literal_global.484
+ ___block_literal_global.589
+ ___block_literal_global.592
+ ___block_literal_global.597
+ __unnamed_array_storage.356
+ __unnamed_array_storage.359
+ __unnamed_array_storage.376
+ _objc_msgSend$_createRecordZonesWithIDs:priority:useZoneWideSharing:group:completion:
+ _objc_msgSend$_fetchAllChangesWithPriority:activity:group:
+ _objc_msgSend$_fetchAllChangesWithPriority:activity:group:completion:
+ _objc_msgSend$_fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:completion:
+ _objc_msgSend$_fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:
+ _objc_msgSend$_fetchShareParticipantForLookupInfos:group:completion:
+ _objc_msgSend$_fetchShareWithShareRecordID:activity:group:completion:
+ _objc_msgSend$_handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:
+ _objc_msgSend$_handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:
+ _objc_msgSend$_handleNewPrivateDatabaseRecordChanges:sharedDatabaseRecordChanges:fetchType:activity:cloudKitGroup:
+ _objc_msgSend$_observerQueue_notifyObserversOfEndUpdatesForFetchWithType:activity:cloudKitGroup:
+ _objc_msgSend$_observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:
+ _objc_msgSend$_queue_addPersonWithCloudKitAddress:toShares:cloudKitGroup:completion:
+ _objc_msgSend$_queue_autoAcceptCompetitionRequestFromContact:activity:cloudKitGroup:completion:
+ _objc_msgSend$_queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:
+ _objc_msgSend$_queue_fetchSharesForRelationship:cloudKitGroup:completion:
+ _objc_msgSend$_queue_performUpdateForActivity:cloudKitGroup:completion:
+ _objc_msgSend$_queue_processRemoteRelationships:activity:cloudKitGroup:completion:
+ _objc_msgSend$_queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:
+ _objc_msgSend$_queue_saveRelationship:contact:activity:cloudKitGroup:completion:
+ _objc_msgSend$_queue_saveRelationship:contact:withExtraRecords:activity:cloudKitGroup:completion:
+ _objc_msgSend$_queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:
+ _objc_msgSend$_queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:group:completion:
+ _objc_msgSend$_queue_updateScoresWithTodaySummary:yesterdaySummary:activity:cloudKitGroup:
+ _objc_msgSend$_saveCurrentCompetitionList:archivedCompetitionList:contact:activity:cloudKitGroup:completion:
+ _objc_msgSend$_saveRecordsIntoPrivateDatabase:recordIDsToDelete:savePolicy:priority:activity:group:completion:
+ _objc_msgSend$_saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:group:completion:
+ _objc_msgSend$addParticipantWithCloudKitAddress:toShares:group:completion:
+ _objc_msgSend$cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:
+ _objc_msgSend$cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:
+ _objc_msgSend$fetchAllChangesIfTimeSinceLastFetchIsGreaterThan:priority:activity:group:completion:
+ _objc_msgSend$fetchAllChangesWithPriority:activity:group:completion:
+ _objc_msgSend$fetchChangesInPrivateDatabaseWithServerChangeTokenCache:priority:activity:group:completion:
+ _objc_msgSend$fetchChangesInSharedDatabaseWithServerChangeTokenCache:priority:activity:group:completion:
+ _objc_msgSend$fetchOrCreateActivityDataShareWithGroup:activity:completion:
+ _objc_msgSend$fetchShareParticipantForEmailAddress:group:completion:
+ _objc_msgSend$fetchShareParticipantWithCloudKitAddress:group:completion:
+ _objc_msgSend$fetchShareWithShareRecordID:activity:group:completion:
+ _objc_msgSend$forceSaveRecordsIntoPrivateDatabaseIgnoringServerChanges:recordIDsToDelete:priority:activity:group:completion:
+ _objc_msgSend$loadLocalActivityDataIfNeeded
+ _objc_msgSend$name
+ _objc_msgSend$periodicUpdateManager:didFailToSaveRecords:activity:
+ _objc_msgSend$periodicUpdateManager:didSaveRecords:activity:
+ _objc_msgSend$removeParticipantWithCloudKitAddress:fromShares:group:completion:
+ _objc_msgSend$requestImmediateUpdateWithCloudKitGroup:completion:
+ _objc_msgSend$saveRecordsIntoPrivateDatabase:priority:activity:group:completion:
+ _objc_msgSend$setGroup:
+ _objc_msgSend$updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:
+ _objc_msgSend$updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:
- -[ASActivityDataManager periodicUpdateManager:didFailToSaveRecords:]
- -[ASActivityDataManager periodicUpdateManager:didSaveRecords:]
- -[ASActivityDataNotificationManager cloudKitManager:didEndUpdatesForFetchWithType:]
- -[ASCloudKitManager _fetchAllChangesWithPriority:activity:]
- -[ASCloudKitManager _fetchAllChangesWithPriority:activity:completion:]
- -[ASCloudKitManager _handleNewPrivateDatabaseRecordChanges:sharedDatabaseRecordChanges:fetchType:]
- -[ASCloudKitManager _observerQueue_notifyObserversOfEndUpdatesForFetchWithType:]
- -[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:]
- -[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:completion:]
- -[ASCloudKitManager addParticipantWithCloudKitAddress:toShares:completion:]
- -[ASCloudKitManager fetchAllChangesIfTimeSinceLastFetchIsGreaterThan:priority:activity:completion:]
- -[ASCloudKitManager fetchAllChangesWithPriority:activity:completion:]
- -[ASCloudKitManager fetchOrCreateActivityDataShareWithCompletion:]
- -[ASCloudKitManager fetchShareParticipantWithCloudKitAddress:completion:]
- -[ASCloudKitManager fetchShareWithShareRecordID:completion:]
- -[ASCloudKitManager forceSaveRecordsIntoPrivateDatabaseIgnoringServerChanges:recordIDsToDelete:priority:activity:completion:]
- -[ASCloudKitManager removeParticpantWithCloudKitAddress:fromShares:completion:]
- -[ASCloudKitManager saveRecordsIntoPrivateDatabase:priority:completion:]
- -[ASCloudKitUtility _createRecordZonesWithIDs:priority:useZoneWideSharing:completion:]
- -[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:completion:]
- -[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:completion:]
- -[ASCloudKitUtility _fetchShareParticipantForLookupInfos:completion:]
- -[ASCloudKitUtility _fetchShareWithShareRecordID:completion:]
- -[ASCloudKitUtility _saveRecordsIntoPrivateDatabase:recordIDsToDelete:savePolicy:priority:activity:completion:]
- -[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:completion:]
- -[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:completion:]
- -[ASCloudKitUtility fetchChangesInPrivateDatabaseWithServerChangeTokenCache:priority:activity:completion:]
- -[ASCloudKitUtility fetchChangesInSharedDatabaseWithServerChangeTokenCache:priority:activity:completion:]
- -[ASCloudKitUtility fetchShareParticipantForEmailAddress:completion:]
- -[ASCloudKitUtility fetchShareWithShareRecordID:completion:]
- -[ASCloudKitUtility forceSaveRecordsIntoPrivateDatabaseIgnoringServerChanges:recordIDsToDelete:priority:activity:completion:]
- -[ASCloudKitUtility removeParticpantWithCloudKitAddress:fromShares:completion:]
- -[ASCloudKitUtility saveRecordsIntoPrivateDatabase:priority:activity:completion:]
- -[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:]
- -[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:]
- -[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:completion:]
- -[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:completion:].cold.1
- -[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:completion:].cold.2
- -[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:]
- -[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:]
- -[ASCompetitionManager _saveCurrentCompetitionList:archivedCompetitionList:contact:completion:]
- -[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:]
- -[ASCompetitionManager periodicUpdateManager:didFailToSaveRecords:]
- -[ASCompetitionManager periodicUpdateManager:didSaveRecords:]
- -[ASPeriodicUpdateManager _queue_performUpdateForActivity:withCompletion:]
- -[ASPeriodicUpdateManager requestImmediateUpdateWithCompletion:]
- -[ASRelationshipManager _queue_addPersonWithCloudKitAddress:toShares:completion:]
- -[ASRelationshipManager _queue_fetchSharesForRelationship:completion:]
- -[ASRelationshipManager _queue_processRemoteRelationships:completion:]
- -[ASRelationshipManager _queue_removeFriendWithUUID:eventType:completion:]
- -[ASRelationshipManager _queue_saveRelationship:contact:completion:]
- -[ASRelationshipManager _queue_saveRelationship:contact:withExtraRecords:completion:]
- -[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:completion:]
- -[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:changesProcessedHandler:]
- -[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:completion:]
- -[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithCompletion:]
- GCC_except_table102
- GCC_except_table106
- GCC_except_table112
- GCC_except_table133
- ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.298
- ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.301
- ___106-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.302
- ___107-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:completion:]_block_invoke
- ___107-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:completion:]_block_invoke.322
- ___107-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:completion:]_block_invoke.322.cold.1
- ___107-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:completion:]_block_invoke.323
- ___107-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:completion:]_block_invoke.cold.1
- ___107-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:completion:]_block_invoke
- ___107-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:completion:]_block_invoke.253
- ___107-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:completion:]_block_invoke.255
- ___107-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:completion:]_block_invoke.256
- ___107-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:completion:]_block_invoke_2
- ___107-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:completion:]_block_invoke_2.254
- ___107-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:completion:]_block_invoke_3
- ___107-[ASCloudKitUtility _fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:completion:]_block_invoke_3.cold.1
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke.304
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke.307
- ___107-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:messageHandledCompletion:]_block_invoke_2.305
- ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.256
- ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.258
- ___108-[ASCloudKitManager _performAndRetryNewAccountTasksWithRetryInterval:shouldCreateSubscriptions:shouldFetch:]_block_invoke.366
- ___110-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:messageHandledCompletion:]_block_invoke.308
- ___111-[ASCloudKitUtility _saveRecordsIntoPrivateDatabase:recordIDsToDelete:savePolicy:priority:activity:completion:]_block_invoke
- ___114-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:messageHandledCompletion:]_block_invoke.309
- ___130-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:changesProcessedHandler:]_block_invoke
- ___130-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:changesProcessedHandler:]_block_invoke.310
- ___130-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:changesProcessedHandler:]_block_invoke.cold.1
- ___143-[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:completion:]_block_invoke
- ___143-[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:completion:]_block_invoke.223
- ___19-[ASXPCClient init]_block_invoke.261
- ___31-[ASGatewayManager updateState]_block_invoke.231
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.232
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.233
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.234
- ___39-[ASContactsManager loadCachedContacts]_block_invoke.247
- ___43-[ASDatabaseClient performWhenDaemonReady:]_block_invoke.238
- ___46-[ASAsyncTransactionQueue performTransaction:]_block_invoke.218
- ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke.368
- ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke_2.369
- ___48-[ASGatewayManager gatewayStatusWithCompletion:]_block_invoke.228
- ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.354
- ___50-[ASCompetitionStore _saveCompetitionLists:owner:]_block_invoke.225
- ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.266
- ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.267
- ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.233
- ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.233.cold.1
- ___58-[ASRelationshipManager _processPersistedMessagesIfNeeded]_block_invoke.311
- ___59-[ASCloudKitManager _fetchAllChangesWithPriority:activity:]_block_invoke
- ___59-[ASCloudKitManager _fetchAllChangesWithPriority:activity:]_block_invoke.325
- ___59-[ASCloudKitManager _fetchAllChangesWithPriority:activity:]_block_invoke.326
- ___59-[ASCloudKitManager _fetchAllChangesWithPriority:activity:]_block_invoke.329
- ___59-[ASCloudKitManager _fetchAllChangesWithPriority:activity:]_block_invoke.329.cold.1
- ___59-[ASCloudKitManager _fetchAllChangesWithPriority:activity:]_block_invoke.330
- ___59-[ASCloudKitManager _fetchAllChangesWithPriority:activity:]_block_invoke_2
- ___59-[ASCloudKitManager _fetchAllChangesWithPriority:activity:]_block_invoke_2.327
- ___60-[ASActivitySharingManager _mainQueue_completeSetupIfNeeded]_block_invoke.254
- ___60-[ASCloudKitUtility fetchShareWithShareRecordID:completion:]_block_invoke
- ___60-[ASCloudKitUtility fetchShareWithShareRecordID:completion:]_block_invoke.cold.1
- ___60-[ASRelationshipManager _contactStoreDidChangeNotification:]_block_invoke.375
- ___61-[ASCloudKitUtility _fetchShareWithShareRecordID:completion:]_block_invoke
- ___61-[ASCompetitionManager periodicUpdateManager:didSaveRecords:]_block_invoke
- ___62-[ASActivityDataManager periodicUpdateManager:didSaveRecords:]_block_invoke
- ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.332
- ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.332.cold.1
- ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.332.cold.2
- ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.332.cold.3
- ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.332.cold.4
- ___63-[ASRelationshipManager _queue_reconcileCloudKitRelationships:]_block_invoke.332.cold.5
- ___64-[ASActivityDataManager achievementStore:didUpdateAchievements:]_block_invoke.253
- ___64-[ASCloudKitUtility _acceptSharesWithURLs:operation:completion:]_block_invoke.237
- ___64-[ASCloudKitUtility _acceptSharesWithURLs:operation:completion:]_block_invoke.237.cold.1
- ___64-[ASCloudKitUtility _acceptSharesWithURLs:operation:completion:]_block_invoke.237.cold.2
- ___64-[ASFriendListManager updateFriendListWithDeletedWorkoutEvents:]_block_invoke.237
- ___64-[ASPeriodicUpdateManager requestImmediateUpdateWithCompletion:]_block_invoke
- ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.264
- ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.267
- ___66-[ASCloudKitManager fetchOrCreateActivityDataShareWithCompletion:]_block_invoke
- ___66-[ASCloudKitManager fetchOrCreateActivityDataShareWithCompletion:]_block_invoke_2
- ___66-[ASCloudKitManager fetchOrCreateActivityDataShareWithCompletion:]_block_invoke_3
- ___68-[ASActivityDataManager periodicUpdateManager:didFailToSaveRecords:]_block_invoke
- ___68-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:]_block_invoke
- ___68-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:]_block_invoke.251
- ___68-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:]_block_invoke.252
- ___68-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:]_block_invoke.253
- ___68-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:]_block_invoke.cold.1
- ___68-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:]_block_invoke_2
- ___68-[ASRelationshipManager _queue_saveRelationship:contact:completion:]_block_invoke
- ___69-[ASCloudKitUtility _fetchShareParticipantForLookupInfos:completion:]_block_invoke
- ___69-[ASCloudKitUtility _fetchShareParticipantForLookupInfos:completion:]_block_invoke_2
- ___69-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:]_block_invoke
- ___69-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:]_block_invoke.254
- ___69-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:]_block_invoke.255
- ___69-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:]_block_invoke.cold.1
- ___69-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:]_block_invoke.cold.2
- ___69-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:]_block_invoke_2
- ___69-[ASDatabaseClient performWhenDataProtectedByFirstUnlockIsAvailable:]_block_invoke.241
- ___69-[ASRelationshipManager setMuteEnabled:forFriendWithUUID:completion:]_block_invoke.271
- ___70-[ASActivityDataNotificationManager _queue_selectWorkoutNotifications]_block_invoke.252
- ___70-[ASCloudKitManager _fetchAllChangesWithPriority:activity:completion:]_block_invoke
- ___70-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:]_block_invoke
- ___70-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:]_block_invoke.249
- ___70-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:]_block_invoke.cold.1
- ___70-[ASDatabaseClient allCodableDatabaseCompetitionListEntriesWithError:]_block_invoke.280
- ___70-[ASRelationshipManager _queue_fetchSharesForRelationship:completion:]_block_invoke
- ___70-[ASRelationshipManager _queue_fetchSharesForRelationship:completion:]_block_invoke.321
- ___70-[ASRelationshipManager _queue_fetchSharesForRelationship:completion:]_block_invoke.321.cold.1
- ___70-[ASRelationshipManager _queue_fetchSharesForRelationship:completion:]_block_invoke.322
- ___70-[ASRelationshipManager _queue_fetchSharesForRelationship:completion:]_block_invoke.cold.1
- ___70-[ASRelationshipManager _queue_processRemoteRelationships:completion:]_block_invoke
- ___70-[ASRelationshipManager _queue_processRemoteRelationships:completion:]_block_invoke.372
- ___70-[ASRelationshipManager _queue_processRemoteRelationships:completion:]_block_invoke.373
- ___70-[ASRelationshipManager _queue_processRemoteRelationships:completion:]_block_invoke_2
- ___70-[ASRelationshipManager _queue_processRemoteRelationships:completion:]_block_invoke_2.cold.1
- ___70-[ASRelationshipManager _queue_processRemoteRelationships:completion:]_block_invoke_2.cold.2
- ___72-[ASActivityDataManager _ckQueue_handleDeletedWorkoutEvents:completion:]_block_invoke.303
- ___73-[ASCompetitionManager completeCompetitionWithFriendWithUUID:completion:]_block_invoke.277
- ___73-[ASCompetitionManager updateAllActiveCompetitionsWithScores:completion:]_block_invoke.279
- ___73-[ASCompetitionManager updateAllActiveCompetitionsWithScores:completion:]_block_invoke_2.280
- ___73-[ASRelationshipManager _queue_reconcileAddressBookAgainstRelationships:]_block_invoke.333
- ___73-[ASRelationshipManager _queue_reconcileAddressBookAgainstRelationships:]_block_invoke.341
- ___73-[ASRelationshipManager _queue_reconcileAddressBookAgainstRelationships:]_block_invoke_2.348
- ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.262
- ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.263
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.232
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.238
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.234
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.234.cold.1
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.245
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.249
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.252
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.256
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke_2.246
- ___74-[ASPeriodicUpdateManager _queue_performUpdateForActivity:withCompletion:]_block_invoke
- ___74-[ASPeriodicUpdateManager _queue_performUpdateForActivity:withCompletion:]_block_invoke.24
- ___74-[ASPeriodicUpdateManager _queue_performUpdateForActivity:withCompletion:]_block_invoke.26
- ___74-[ASPeriodicUpdateManager _queue_performUpdateForActivity:withCompletion:]_block_invoke.28
- ___74-[ASPeriodicUpdateManager _queue_performUpdateForActivity:withCompletion:]_block_invoke.29
- ___74-[ASPeriodicUpdateManager _queue_performUpdateForActivity:withCompletion:]_block_invoke.30
- ___74-[ASPeriodicUpdateManager _queue_performUpdateForActivity:withCompletion:]_block_invoke.31
- ___74-[ASPeriodicUpdateManager _queue_performUpdateForActivity:withCompletion:]_block_invoke_2
- ___74-[ASPeriodicUpdateManager _queue_performUpdateForActivity:withCompletion:]_block_invoke_2.25
- ___74-[ASPeriodicUpdateManager _queue_performUpdateForActivity:withCompletion:]_block_invoke_3
- ___74-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:completion:]_block_invoke
- ___74-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:completion:]_block_invoke.314
- ___74-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:completion:]_block_invoke.315
- ___74-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:completion:]_block_invoke.315.cold.1
- ___74-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:completion:]_block_invoke.cold.1
- ___74-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:completion:]_block_invoke_2
- ___74-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:completion:]_block_invoke_2.316
- ___74-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:completion:]_block_invoke_3
- ___74-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:completion:]_block_invoke_3.317
- ___74-[ASRelationshipManager _queue_removeFriendWithUUID:eventType:completion:]_block_invoke_3.317.cold.1
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.289
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.292
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.290
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.293
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.294
- ___74-[ASRelationshipManager ignoreInviteRequestFromFriendWithUUID:completion:]_block_invoke.297
- ___75-[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:completion:]_block_invoke
- ___75-[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:completion:]_block_invoke.241
- ___75-[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:completion:]_block_invoke.241.cold.1
- ___75-[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:completion:]_block_invoke.cold.1
- ___75-[ASCloudKitUtility addParticipantWithCloudKitAddress:toShares:completion:]_block_invoke.cold.2
- ___76-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:completion:]_block_invoke.258
- ___76-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:completion:]_block_invoke_2.259
- ___76-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:completion:]_block_invoke_2.259.cold.1
- ___76-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:completion:]_block_invoke_3.260
- ___77-[ASActivityDataNotificationManager _queue_selectGoalCompletionNotifications]_block_invoke.266
- ___77-[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:]_block_invoke
- ___77-[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:]_block_invoke_2
- ___77-[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:]_block_invoke_3
- ___77-[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:]_block_invoke_4
- ___77-[ASCompetitionManager _queue_updateScoresWithTodaySummary:yesterdaySummary:]_block_invoke_5
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.241
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.241.cold.1
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.241.cold.2
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.241.cold.3
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.244
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.242
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.245
- ___78-[ASCompetitionManager ignoreCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.246
- ___79-[ASCloudKitUtility removeParticpantWithCloudKitAddress:fromShares:completion:]_block_invoke
- ___79-[ASCloudKitUtility removeParticpantWithCloudKitAddress:fromShares:completion:]_block_invoke.243
- ___79-[ASCloudKitUtility removeParticpantWithCloudKitAddress:fromShares:completion:]_block_invoke.243.cold.1
- ___79-[ASCloudKitUtility removeParticpantWithCloudKitAddress:fromShares:completion:]_block_invoke.cold.1
- ___79-[ASCloudKitUtility removeParticpantWithCloudKitAddress:fromShares:completion:]_block_invoke.cold.2
- ___79-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:]_block_invoke
- ___79-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:]_block_invoke.271
- ___79-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:]_block_invoke.271.cold.1
- ___79-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:]_block_invoke.272
- ___79-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:]_block_invoke.273
- ___81-[ASRelationshipManager _queue_addPersonWithCloudKitAddress:toShares:completion:]_block_invoke
- ___81-[ASRelationshipManager _queue_addPersonWithCloudKitAddress:toShares:completion:]_block_invoke_2
- ___81-[ASRelationshipManager _queue_addPersonWithCloudKitAddress:toShares:completion:]_block_invoke_2.cold.1
- ___82-[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:completion:]_block_invoke
- ___82-[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:completion:]_block_invoke_2
- ___82-[ASCompetitionManager _queue_autoAcceptCompetitionRequestFromContact:completion:]_block_invoke_3
- ___83-[ASActivityDataNotificationManager cloudKitManager:didEndUpdatesForFetchWithType:]_block_invoke
- ___83-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithCompletion:]_block_invoke
- ___83-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithCompletion:]_block_invoke.273
- ___83-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithCompletion:]_block_invoke_2
- ___84-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:]_block_invoke
- ___84-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:]_block_invoke.463
- ___84-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:]_block_invoke.464
- ___84-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:]_block_invoke.464.cold.1
- ___84-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:]_block_invoke_2
- ___85-[ASRelationshipManager _queue_saveRelationship:contact:withExtraRecords:completion:]_block_invoke
- ___85-[ASRelationshipManager _queue_saveRelationship:contact:withExtraRecords:completion:]_block_invoke_2
- ___85-[ASRelationshipManager _queue_saveRelationship:contact:withExtraRecords:completion:]_block_invoke_2.cold.1
- ___86-[ASCloudKitManager _performNewAccountTasksCreatingSubscriptions:fetching:completion:]_block_invoke.365
- ___86-[ASCloudKitUtility _createRecordZonesWithIDs:priority:useZoneWideSharing:completion:]_block_invoke
- ___86-[ASCloudKitUtility _createRecordZonesWithIDs:priority:useZoneWideSharing:completion:]_block_invoke.cold.1
- ___86-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:completion:]_block_invoke
- ___86-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:completion:]_block_invoke.272
- ___86-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:completion:]_block_invoke_2
- ___86-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:completion:]_block_invoke_2.cold.1
- ___90-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:completion:]_block_invoke
- ___90-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:completion:]_block_invoke.323
- ___90-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:completion:]_block_invoke.324
- ___90-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:completion:]_block_invoke.325
- ___90-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:completion:]_block_invoke.328
- ___90-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:completion:]_block_invoke.cold.1
- ___90-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:completion:]_block_invoke_2
- ___90-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:completion:]_block_invoke_2.326
- ___90-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:completion:]_block_invoke_2.326.cold.1
- ___90-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:completion:]_block_invoke_2.cold.1
- ___93-[ASDatabaseClient deletedHealthKitWorkoutsWithinLastNumberOfDays:maxBatchSize:anchor:error:]_block_invoke.254
- ___95-[ASCompetitionManager _saveCurrentCompetitionList:archivedCompetitionList:contact:completion:]_block_invoke
- ___95-[ASCompetitionManager _saveCurrentCompetitionList:archivedCompetitionList:contact:completion:]_block_invoke_2
- ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.288
- ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.289
- ___97-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:completion:]_block_invoke
- ___97-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:completion:]_block_invoke.258
- ___97-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:completion:]_block_invoke.258.cold.1
- ___97-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:completion:]_block_invoke.260
- ___97-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:completion:]_block_invoke_2
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.280
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.282
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.283
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_2.284
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_3.285
- ___98-[ASActivityDataManager currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:]_block_invoke.277
- ___98-[ASCloudKitManager _handleNewPrivateDatabaseRecordChanges:sharedDatabaseRecordChanges:fetchType:]_block_invoke
- ___99-[ASCloudKitManager fetchAllChangesIfTimeSinceLastFetchIsGreaterThan:priority:activity:completion:]_block_invoke
- ___block_descriptor_100_e8_32s40s48s56s64s72s80bs88bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs96bs_e39_v28?0B8"NSError"12"ASRelationship"20ls88l8s96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88bs96bs_e44_v36?0B8"NSError"12"CKShare"20"CKShare"28ls32l8s40l8s88l8s96l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96bs104bs_e20_v20?0B8"NSError"12ls96l8s104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104bs112bs_e20_v20?0B8"NSError"12ls32l8s40l8s104l8s112l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_32_e109_v52?0"ASCloudKitManager"8"<ASCloudKitManagerChangesObserver>"16"CKRecordZoneID"24B32"NSArray"36?<v?>44l
- ___block_descriptor_48_e8_32s40bs_e14_v16?0?<v?>8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e14_v16?0?<v?>8ls32l8s40l8
- ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e12_"NSSet"8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e14_v16?0?<v?>8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e43_v32?0"CKRecordID"8"ASRelationship"16^B24ls32l8s40l8s48l8
- ___block_descriptor_58_e8_32s40s48bs_e14_v16?0?<v?>8ls32l8s40l8s48l8
- ___block_descriptor_58_e8_32s40s48bs_e20_v20?0B8"NSError"12ls48l8s32l8s40l8
- ___block_descriptor_58_e8_32s40s48bs_e34_v28?0B8"NSError"12"ASContact"20ls48l8s32l8s40l8
- ___block_descriptor_58_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs56bs_e20_v20?0B8"NSError"12ls48l8s56l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e43_v28?0B8"NSError"12"CKShareParticipant"20ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56s_e9_B16?0^8ls32l8s40l8s48l8s56l8
- ___block_descriptor_66_e8_32s40s48s56bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8
- ___block_descriptor_66_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s40l8s56l8s48l8
- ___block_descriptor_67_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e32_v28?0B8"NSError"12"NSArray"20ls32l8s40l8r56l8r64l8s48l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8r64l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e14_v16?0?<v?>8ls32l8s40l8s64l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e40_v32?0"CKRecordZoneID"8"NSArray"16^B24ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_72_e8_32s40s48s_e44_v36?0B8"NSError"12"NSArray"20"NSArray"28ls32l8s40l8s48l8
- ___block_descriptor_74_e8_32s40s48s56s64bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_74_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s64l8s56l8
- ___block_descriptor_80_e8_32s40s48s56bs64bs72bs_e32_v28?0B8"NSError"12"CKShare"20ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e20_v20?0B8"NSError"12ls32l8s40l8s64l8s72l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64bs72bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8s72l8
- ___block_descriptor_80_e8_32s40s48s56s64s72s_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_82_e8_32s40s48s56s64bs72bs_e34_v28?0B8"NSError"12"ASContact"20ls32l8s40l8s48l8s64l8s72l8s56l8
- ___block_descriptor_83_e8_32s40s48s56s64bs72bs_e32_v28?0B8"NSError"12"CKShare"20ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_88_e8_32s40s48s56bs64r72w_e44_v28?0"CKServerChangeToken"8B16"NSError"20lw72l8s32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64bs_e32_v28?0B8"NSError"12"NSArray"20ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s80l8s48l8s56l8s64l8s72l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e9_B16?0^8ls32l8s40l8s48l8s56l8r80l8s64l8s72l8
- ___block_descriptor_89_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s40l8s48l8s72l8s80l8s56l8s64l8
- ___block_descriptor_89_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8r80l8s64l8
- ___block_descriptor_90_e8_32s40s48s56s64s72bs80bs_e5_v8?0ls32l8s40l8s48l8s56l8s72l8s80l8s64l8
- ___block_descriptor_91_e8_32s40s48s56s64s72bs80bs_e43_v28?0B8"NSError"12"CKShareParticipant"20ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88bs_e44_v36?0B8"NSError"12"CKShare"20"CKShare"28ls80l8s88l8s32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88bs_e63_v44?0B8"NSError"12"CKShare"20"CKShare"28"ASRelationship"36ls32l8s40l8s80l8s88l8s48l8s56l8s64l8s72l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8s64l8s88l8s72l8s80l8
- ___block_descriptor_96_e8_32s40s48s56s64s72s80s88bs_e20_v20?0B8"NSError"12ls32l8s40l8s88l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_97_e8_32s40s48s56s64s72bs80w_e17_v16?0"NSError"8lw80l8s32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_97_e8_32s40s48s56s64s72bs_e32_v28?0B8"NSError"12"NSArray"20ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_97_e8_32s40s48s56s64s72s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.219
- ___block_literal_global.220
- ___block_literal_global.221
- ___block_literal_global.224
- ___block_literal_global.226
- ___block_literal_global.251
- ___block_literal_global.255
- ___block_literal_global.260
- ___block_literal_global.263
- ___block_literal_global.270
- ___block_literal_global.276
- ___block_literal_global.292
- ___block_literal_global.296
- ___block_literal_global.301
- ___block_literal_global.313
- ___block_literal_global.336
- ___block_literal_global.344
- ___block_literal_global.350
- ___block_literal_global.355
- ___block_literal_global.357
- ___block_literal_global.365
- ___block_literal_global.370
- ___block_literal_global.371
- ___block_literal_global.383
- ___block_literal_global.388
- ___block_literal_global.390
- ___block_literal_global.397
- ___block_literal_global.400
- ___block_literal_global.404
- ___block_literal_global.406
- ___block_literal_global.408
- ___block_literal_global.415
- ___block_literal_global.422
- ___block_literal_global.425
- ___block_literal_global.435
- ___block_literal_global.438
- ___block_literal_global.445
- ___block_literal_global.448
- ___block_literal_global.454
- ___block_literal_global.460
- ___block_literal_global.559
- ___block_literal_global.562
- ___block_literal_global.566
- __unnamed_array_storage.332
- __unnamed_array_storage.335
- __unnamed_array_storage.352
- _objc_msgSend$_createRecordZonesWithIDs:priority:useZoneWideSharing:completion:
- _objc_msgSend$_fetchAllChangesWithPriority:activity:
- _objc_msgSend$_fetchAllChangesWithPriority:activity:completion:
- _objc_msgSend$_fetchChangesInDatabase:serverChangeTokenCache:priority:activity:completion:
- _objc_msgSend$_fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:completion:
- _objc_msgSend$_fetchShareParticipantForLookupInfos:completion:
- _objc_msgSend$_fetchShareWithShareRecordID:completion:
- _objc_msgSend$_handleAcceptedCompetitionFromFriendWithUUID:
- _objc_msgSend$_handleCompetitionRequestFromFriendWithUUID:
- _objc_msgSend$_handleNewPrivateDatabaseRecordChanges:sharedDatabaseRecordChanges:fetchType:
- _objc_msgSend$_observerQueue_notifyObserversOfEndUpdatesForFetchWithType:
- _objc_msgSend$_observerQueue_performNotificationStep:onRecords:dispatchGroup:
- _objc_msgSend$_queue_addPersonWithCloudKitAddress:toShares:completion:
- _objc_msgSend$_queue_autoAcceptCompetitionRequestFromContact:completion:
- _objc_msgSend$_queue_completeCompetitionIfNecessaryForFriendWithUUID:
- _objc_msgSend$_queue_fetchSharesForRelationship:completion:
- _objc_msgSend$_queue_performUpdateForActivity:withCompletion:
- _objc_msgSend$_queue_processRemoteRelationships:completion:
- _objc_msgSend$_queue_removeFriendWithUUID:eventType:completion:
- _objc_msgSend$_queue_saveRelationship:contact:completion:
- _objc_msgSend$_queue_saveRelationship:contact:withExtraRecords:completion:
- _objc_msgSend$_queue_saveRelationshipAndFetchOrCreateShares:contact:completion:
- _objc_msgSend$_queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:completion:
- _objc_msgSend$_queue_updateScoresWithTodaySummary:yesterdaySummary:
- _objc_msgSend$_saveCurrentCompetitionList:archivedCompetitionList:contact:completion:
- _objc_msgSend$_saveRecordsIntoPrivateDatabase:recordIDsToDelete:savePolicy:priority:activity:completion:
- _objc_msgSend$_saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:completion:
- _objc_msgSend$addParticipantWithCloudKitAddress:toShares:completion:
- _objc_msgSend$cloudKitManager:didEndUpdatesForFetchWithType:
- _objc_msgSend$cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:changesProcessedHandler:
- _objc_msgSend$fetchAllChangesIfTimeSinceLastFetchIsGreaterThan:priority:activity:completion:
- _objc_msgSend$fetchAllChangesWithPriority:activity:completion:
- _objc_msgSend$fetchChangesInPrivateDatabaseWithServerChangeTokenCache:priority:activity:completion:
- _objc_msgSend$fetchChangesInSharedDatabaseWithServerChangeTokenCache:priority:activity:completion:
- _objc_msgSend$fetchOrCreateActivityDataShareWithCompletion:
- _objc_msgSend$fetchShareParticipantForEmailAddress:completion:
- _objc_msgSend$fetchShareParticipantWithCloudKitAddress:completion:
- _objc_msgSend$fetchShareWithShareRecordID:completion:
- _objc_msgSend$forceSaveRecordsIntoPrivateDatabaseIgnoringServerChanges:recordIDsToDelete:priority:activity:completion:
- _objc_msgSend$periodicUpdateManager:didFailToSaveRecords:
- _objc_msgSend$periodicUpdateManager:didSaveRecords:
- _objc_msgSend$removeParticpantWithCloudKitAddress:fromShares:completion:
- _objc_msgSend$requestImmediateUpdateWithCompletion:
- _objc_msgSend$saveRecordsIntoPrivateDatabase:priority:activity:completion:
- _objc_msgSend$saveRecordsIntoPrivateDatabase:priority:completion:
- _objc_msgSend$updateRelationshipWithCompetitionEvent:friendUUID:completion:
- _objc_msgSend$updateRelationshipsForCurrentFeatureSupportWithCompletion:
CStrings:
+ "CoreDuetTriggered"
+ "Created record zones in private database: %@, with group %@"
+ "Fetching changes in %lu record zones (database %{public}@, group %{public}@, activity %{public}@)"
+ "Fetching changes in database %{public}@, with group %{public}@ and activity %{public}@"
+ "InitialDownload"
+ "InitialSetup"
+ "PushTriggered"
+ "Retrying activity data load"
+ "Saved %lu records into private database with group %{public}@, activity %{public}@"
+ "SharingSetup"
+ "T@\"NSObject<ACHTemplateSourceDelegate>\",?,W,N"
+ "T@\"NSObject<ACHTemplateSourceDelegate>\",?,W,N,Vdelegate"
+ "T@\"NSString\",?,R,C"
+ "UserActionExplicit"
+ "UserActionImplicit"
+ "_createRecordZonesWithIDs:priority:useZoneWideSharing:group:completion:"
+ "_fetchAllChangesWithPriority:activity:group:"
+ "_fetchAllChangesWithPriority:activity:group:completion:"
+ "_fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:completion:"
+ "_fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:"
+ "_fetchShareParticipantForLookupInfos:group:completion:"
+ "_fetchShareWithShareRecordID:activity:group:completion:"
+ "_handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:"
+ "_handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:"
+ "_handleNewPrivateDatabaseRecordChanges:sharedDatabaseRecordChanges:fetchType:activity:cloudKitGroup:"
+ "_observerQueue_notifyObserversOfEndUpdatesForFetchWithType:activity:cloudKitGroup:"
+ "_observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:"
+ "_queue_addPersonWithCloudKitAddress:toShares:cloudKitGroup:completion:"
+ "_queue_autoAcceptCompetitionRequestFromContact:activity:cloudKitGroup:completion:"
+ "_queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:"
+ "_queue_fetchSharesForRelationship:cloudKitGroup:completion:"
+ "_queue_performUpdateForActivity:cloudKitGroup:completion:"
+ "_queue_processRemoteRelationships:activity:cloudKitGroup:completion:"
+ "_queue_removeFriendWithUUID:eventType:activity:cloudKitGroup:completion:"
+ "_queue_saveRelationship:contact:activity:cloudKitGroup:completion:"
+ "_queue_saveRelationship:contact:withExtraRecords:activity:cloudKitGroup:completion:"
+ "_queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:"
+ "_queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:group:completion:"
+ "_queue_updateScoresWithTodaySummary:yesterdaySummary:activity:cloudKitGroup:"
+ "_saveCurrentCompetitionList:archivedCompetitionList:contact:activity:cloudKitGroup:completion:"
+ "_saveRecordsIntoPrivateDatabase:recordIDsToDelete:savePolicy:priority:activity:group:completion:"
+ "_saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:group:completion:"
+ "addParticipantWithCloudKitAddress:toShares:group:completion:"
+ "cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:"
+ "cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:"
+ "fetchAllChangesIfTimeSinceLastFetchIsGreaterThan:priority:activity:group:completion:"
+ "fetchAllChangesWithPriority:activity:group:completion:"
+ "fetchChangesInPrivateDatabaseWithServerChangeTokenCache:priority:activity:group:completion:"
+ "fetchChangesInSharedDatabaseWithServerChangeTokenCache:priority:activity:group:completion:"
+ "fetchOrCreateActivityDataShareWithGroup:activity:completion:"
+ "fetchShareParticipantForEmailAddress:group:completion:"
+ "fetchShareParticipantWithCloudKitAddress:group:completion:"
+ "fetchShareWithShareRecordID:activity:group:completion:"
+ "forceSaveRecordsIntoPrivateDatabaseIgnoringServerChanges:recordIDsToDelete:priority:activity:group:completion:"
+ "loadLocalActivityDataIfNeeded"
+ "name"
+ "periodicUpdateManager:didFailToSaveRecords:activity:"
+ "periodicUpdateManager:didSaveRecords:activity:"
+ "removeParticipantWithCloudKitAddress:fromShares:group:completion:"
+ "requestImmediateUpdateWithCloudKitGroup:completion:"
+ "saveRecordsIntoPrivateDatabase:priority:activity:group:completion:"
+ "setGroup:"
+ "updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:"
+ "updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:"
+ "v40@0:8@\"ASPeriodicUpdateManager\"16@\"NSArray\"24@\"NSObject<OS_xpc_object>\"32"
+ "v40@0:8q16@24@32"
+ "v52@0:8@16S24@28@36@?44"
+ "v52@0:8@16q24B32@36@?44"
+ "v52@0:8S16@20@28@36@?44"
+ "v56@0:8@\"ASCloudKitManager\"16q24@\"NSObject<OS_xpc_object>\"32@\"CKOperationGroup\"40@?<v@?>48"
+ "v56@0:8@16q24@32@40@?48"
+ "v56@0:8Q16q24@32@40@?48"
+ "v56@0:8q16@24@32@40@?48"
+ "v64@0:8@16@24@32@40@48@?56"
+ "v64@0:8@16@24q32@40@48@?56"
+ "v68@0:8@\"ASCloudKitManager\"16@\"NSArray\"24@\"CKRecordZoneID\"32B40@\"NSObject<OS_xpc_object>\"44@\"CKOperationGroup\"52@?<v@?>60"
+ "v68@0:8@16@24@32B40@44@52@?60"
+ "v68@?0@\"ASCloudKitManager\"8@\"<ASCloudKitManagerChangesObserver>\"16@\"CKRecordZoneID\"24B32@\"NSArray\"36@\"NSObject<OS_xpc_object>\"44@\"CKOperationGroup\"52@?<v@?>60"
+ "v72@0:8@16@24q32q40@48@56@?64"
+ "v76@0:8@16@24@32q40B48@52@60@?68"
+ "v76@0:8@16@24q32q40@48B56@60@?68"
- "Created record zones in private database: %@"
- "Fetching changes in %lu record zones (database %{public}@)"
- "Fetching changes in database %{public}@"
- "Saved %lu records into private database."
- "T@\"NSObject<ACHTemplateSourceDelegate>\",W,N"
- "T@\"NSObject<ACHTemplateSourceDelegate>\",W,N,Vdelegate"
- "_createRecordZonesWithIDs:priority:useZoneWideSharing:completion:"
- "_fetchAllChangesWithPriority:activity:"
- "_fetchAllChangesWithPriority:activity:completion:"
- "_fetchChangesInDatabase:serverChangeTokenCache:priority:activity:completion:"
- "_fetchChangesInZones:inDatabase:serverChangeTokenCache:priority:allowRetry:completion:"
- "_fetchShareParticipantForLookupInfos:completion:"
- "_fetchShareWithShareRecordID:completion:"
- "_handleAcceptedCompetitionFromFriendWithUUID:"
- "_handleCompetitionRequestFromFriendWithUUID:"
- "_handleNewPrivateDatabaseRecordChanges:sharedDatabaseRecordChanges:fetchType:"
- "_observerQueue_notifyObserversOfEndUpdatesForFetchWithType:"
- "_observerQueue_performNotificationStep:onRecords:dispatchGroup:"
- "_queue_addPersonWithCloudKitAddress:toShares:completion:"
- "_queue_autoAcceptCompetitionRequestFromContact:completion:"
- "_queue_completeCompetitionIfNecessaryForFriendWithUUID:"
- "_queue_fetchSharesForRelationship:completion:"
- "_queue_performUpdateForActivity:withCompletion:"
- "_queue_processRemoteRelationships:completion:"
- "_queue_removeFriendWithUUID:eventType:completion:"
- "_queue_saveRelationship:contact:completion:"
- "_queue_saveRelationship:contact:withExtraRecords:completion:"
- "_queue_saveRelationshipAndFetchOrCreateShares:contact:completion:"
- "_queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:completion:"
- "_queue_updateScoresWithTodaySummary:yesterdaySummary:"
- "_saveCurrentCompetitionList:archivedCompetitionList:contact:completion:"
- "_saveRecordsIntoPrivateDatabase:recordIDsToDelete:savePolicy:priority:activity:completion:"
- "_saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:completion:"
- "addParticipantWithCloudKitAddress:toShares:completion:"
- "cloudKitManager:didEndUpdatesForFetchWithType:"
- "cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:changesProcessedHandler:"
- "fetchAllChangesIfTimeSinceLastFetchIsGreaterThan:priority:activity:completion:"
- "fetchAllChangesWithPriority:activity:completion:"
- "fetchChangesInPrivateDatabaseWithServerChangeTokenCache:priority:activity:completion:"
- "fetchChangesInSharedDatabaseWithServerChangeTokenCache:priority:activity:completion:"
- "fetchOrCreateActivityDataShareWithCompletion:"
- "fetchShareParticipantForEmailAddress:completion:"
- "fetchShareParticipantWithCloudKitAddress:completion:"
- "fetchShareWithShareRecordID:completion:"
- "forceSaveRecordsIntoPrivateDatabaseIgnoringServerChanges:recordIDsToDelete:priority:activity:completion:"
- "periodicUpdateManager:didFailToSaveRecords:"
- "periodicUpdateManager:didSaveRecords:"
- "removeParticpantWithCloudKitAddress:fromShares:completion:"
- "requestImmediateUpdateWithCompletion:"
- "saveRecordsIntoPrivateDatabase:priority:activity:completion:"
- "saveRecordsIntoPrivateDatabase:priority:completion:"
- "updateRelationshipWithCompetitionEvent:friendUUID:completion:"
- "updateRelationshipsForCurrentFeatureSupportWithCompletion:"
- "v32@0:8@\"ASPeriodicUpdateManager\"16@\"NSArray\"24"
- "v36@0:8@16S24@?28"
- "v36@0:8S16@20@?28"
- "v40@0:8q16@24@?32"
- "v44@0:8@16q24B32@?36"
- "v48@0:8@16q24@32@?40"
- "v48@0:8Q16q24@32@?40"
- "v52@?0@\"ASCloudKitManager\"8@\"<ASCloudKitManagerChangesObserver>\"16@\"CKRecordZoneID\"24B32@\"NSArray\"36@?<v@?>44"
- "v56@0:8@16@24q32@40@?48"
- "v60@0:8@16@24@32q40B48@?52"
- "v64@0:8@16@24q32q40@48@?56"
- "v68@0:8@16@24q32q40@48B56@?60"

```
