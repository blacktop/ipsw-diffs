## ActivitySharingDaemonCore

> `/System/Library/PrivateFrameworks/ActivitySharingDaemonCore.framework/ActivitySharingDaemonCore`

```diff

-824.7.0.0.0
-  __TEXT.__text: 0x7cef0
-  __TEXT.__auth_stubs: 0xf30
-  __TEXT.__objc_methlist: 0x4764
+851.0.0.0.0
+  __TEXT.__text: 0x7d3e4
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_methlist: 0x4574
   __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x2e07
-  __TEXT.__gcc_except_tab: 0x1050
-  __TEXT.__oslogstring: 0xe8d2
-  __TEXT.__unwind_info: 0x1bf8
-  __TEXT.__objc_classname: 0xa67
-  __TEXT.__objc_methname: 0x1155d
-  __TEXT.__objc_methtype: 0x2cd1
-  __TEXT.__objc_stubs: 0xc3c0
-  __DATA_CONST.__got: 0x9a8
-  __DATA_CONST.__const: 0x3a78
+  __TEXT.__cstring: 0x2f1d
+  __TEXT.__gcc_except_tab: 0xfec
+  __TEXT.__oslogstring: 0xe8fe
+  __TEXT.__unwind_info: 0x1bc8
+  __TEXT.__objc_classname: 0x9fd
+  __TEXT.__objc_methname: 0x113bc
+  __TEXT.__objc_methtype: 0x2a94
+  __TEXT.__objc_stubs: 0xc5c0
+  __DATA_CONST.__got: 0xa30
+  __DATA_CONST.__const: 0x3b60
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x138
+  __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x37b8
+  __DATA_CONST.__objc_selrefs: 0x37b0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x7a8
-  __AUTH_CONST.__const: 0xd80
-  __AUTH_CONST.__cfstring: 0x1d20
-  __AUTH_CONST.__objc_const: 0xe570
+  __AUTH_CONST.__auth_got: 0x780
+  __AUTH_CONST.__const: 0xdc0
+  __AUTH_CONST.__cfstring: 0x1de0
+  __AUTH_CONST.__objc_const: 0xdca0
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x5ec
-  __DATA.__data: 0xea0
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x5d8
+  __DATA.__data: 0xd20
   __DATA.__bss: 0x70
-  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__objc_data: 0xc30
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
+  - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
+  - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
+  - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F8F1AD14-3A8E-37FB-81C3-B8808E10A702
-  Functions: 2359
-  Symbols:   8820
-  CStrings:  4203
+  UUID: 8CF4F1A8-5F2A-370C-A027-B1EC3B62296C
+  Functions: 2358
+  Symbols:   8787
+  CStrings:  4197
 
Symbols:
+ -[ASCompetitionTemplateSource templatesWithCompletion:]
+ -[ASCompetitionTemplateSource templatesWithCompletion:].cold.1
+ -[ASIDSMessageCenter _donateEntries:completion:]
+ -[ASIDSMessageCenter _retrieveFirewallWithCompletion:]
+ -[ASIDSMessageCenter donateAddresses:completion:]
+ -[ASIDSMessageCenter donateAddresses:completion:].cold.1
+ -[ASIDSMessageCenter donatedAddressesWithCompletion:]
+ GCC_except_table111
+ GCC_except_table113
+ GCC_except_table132
+ GCC_except_table147
+ GCC_except_table158
+ GCC_except_table182
+ GCC_except_table245
+ GCC_except_table50
+ GCC_except_table52
+ _ASIDSMessageCenterErrorDomain
+ _ASMessageFromRichMessagePayload
+ _ASSendRichMessagePayloadToDestination.cold.1
+ _ASSendRichMessagePayloadToDestination.cold.2
+ _ASSendRichMessagePayloadToDestination.cold.3
+ _ASSendRichMessagePayloadToDestination.cold.4
+ _FIActivityTypeIsCalorimetryOptimized
+ _IMBalloonPluginIdentifierMessageExtension
+ _IMChatJoinStateDidChangeNotification
+ _IMExtensionPayloadBalloonLayoutClassKey
+ _IMExtensionPayloadBalloonLayoutInfoKey
+ _IMExtensionPayloadBalloonLiveLayoutInfoKey
+ _IMExtensionPayloadLocalizedDescriptionTextKey
+ _IMExtensionPayloadURLKey
+ _NSDefaultRunLoopMode
+ _OBJC_CLASS_$_IDSFirewallEntry
+ _OBJC_CLASS_$_IDSURI
+ _OBJC_CLASS_$_IMAccountController
+ _OBJC_CLASS_$_IMChatRegistry
+ _OBJC_CLASS_$_IMDaemonController
+ _OBJC_CLASS_$_IMMessage
+ _OBJC_CLASS_$_IMServiceImpl
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_NSRunLoop
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke.337
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.338
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.338.cold.1
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_3.339
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.340
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.340.cold.1
+ ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.340.cold.2
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.346
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.346.cold.1
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.347
+ ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.348
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.394
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.395
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.395.cold.1
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_2.396
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.397
+ ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.397.cold.1
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.411
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.412
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.415
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.413
+ ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.413.cold.1
+ ___106-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:]_block_invoke.351
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.589
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.590
+ ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.590.cold.1
+ ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.332
+ ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.334
+ ___108-[ASCloudKitManager _performAndRetryNewAccountTasksWithRetryInterval:shouldCreateSubscriptions:shouldFetch:]_block_invoke.464
+ ___109-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:]_block_invoke.350
+ ___117-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.324
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.378
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.381
+ ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.382
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.384
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.387
+ ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2.385
+ ___126-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.388
+ ___130-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.389
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.413
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.413.cold.1
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.414
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.414.cold.1
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.416
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.416.cold.1
+ ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.417
+ ___149-[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:group:completion:]_block_invoke.301
+ ___153-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.390
+ ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.341
+ ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.341.cold.1
+ ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.343
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.330
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.335
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.337
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.339
+ ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke_2.336
+ ___19-[ASXPCClient init]_block_invoke.337
+ ___31-[ASGatewayManager updateState]_block_invoke.303
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.307
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.308
+ ___39-[ASActivitySharingManager daemonReady]_block_invoke.309
+ ___39-[ASContactsManager loadCachedContacts]_block_invoke.323
+ ___43-[ASDatabaseClient performWhenDaemonReady:]_block_invoke.313
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.294
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.294.cold.1
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.295
+ ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.295.cold.1
+ ___46-[ASAsyncTransactionQueue performTransaction:]_block_invoke.293
+ ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.306
+ ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.306.cold.1
+ ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.307
+ ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke.466
+ ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke_2.467
+ ___48-[ASGatewayManager gatewayStatusWithCompletion:]_block_invoke.300
+ ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke
+ ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.391
+ ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.392
+ ___48-[ASIDSMessageCenter _donateEntries:completion:]_block_invoke.392.cold.1
+ ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.451
+ ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.452
+ ___49-[ASIDSMessageCenter donateAddresses:completion:]_block_invoke
+ ___49-[ASIDSMessageCenter donateAddresses:completion:]_block_invoke.cold.1
+ ___49-[ASIDSMessageCenter donateAddresses:completion:]_block_invoke.cold.2
+ ___50-[ASCompetitionStore _saveCompetitionLists:owner:]_block_invoke.300
+ ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.341
+ ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.342
+ ___53-[ASIDSMessageCenter donatedAddressesWithCompletion:]_block_invoke
+ ___53-[ASIDSMessageCenter donatedAddressesWithCompletion:]_block_invoke.399
+ ___53-[ASIDSMessageCenter donatedAddressesWithCompletion:]_block_invoke_2
+ ___53-[ASIDSMessageCenter donatedAddressesWithCompletion:]_block_invoke_2.cold.1
+ ___53-[ASIDSMessageCenter donatedAddressesWithCompletion:]_block_invoke_2.cold.2
+ ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.311
+ ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.311.cold.1
+ ___54-[ASIDSMessageCenter _retrieveFirewallWithCompletion:]_block_invoke
+ ___54-[ASIDSMessageCenter _retrieveFirewallWithCompletion:]_block_invoke.cold.1
+ ___54-[ASIDSMessageCenter _retrieveFirewallWithCompletion:]_block_invoke.cold.2
+ ___55-[ASCompetitionTemplateSource templatesWithCompletion:]_block_invoke
+ ___55-[ASCompetitionTemplateSource templatesWithCompletion:]_block_invoke.290
+ ___58-[ASRelationshipManager _processPersistedMessagesIfNeeded]_block_invoke.391
+ ___60-[ASActivitySharingManager _mainQueue_completeSetupIfNeeded]_block_invoke.329
+ ___60-[ASRelationshipManager _contactStoreDidChangeNotification:]_block_invoke.426
+ ___64-[ASFriendListManager updateFriendListWithDeletedWorkoutEvents:]_block_invoke.315
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.419
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.420
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.423
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.423.cold.1
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.424
+ ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke_2.421
+ ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.342
+ ___65-[ASIDSMessageCenter _handleMessageSendSuccess:error:identifier:]_block_invoke.372
+ ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke.367
+ ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_2.368
+ ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_3.369
+ ___69-[ASDatabaseClient performWhenDataProtectedByFirstUnlockIsAvailable:]_block_invoke.316
+ ___69-[ASRelationshipManager setMuteEnabled:forFriendWithUUID:completion:]_block_invoke.349
+ ___70-[ASActivityDataNotificationManager _queue_selectWorkoutNotifications]_block_invoke.327
+ ___70-[ASDatabaseClient allCodableDatabaseCompetitionListEntriesWithError:]_block_invoke.355
+ ___72-[ASActivityDataManager _ckQueue_handleDeletedWorkoutEvents:completion:]_block_invoke.379
+ ___73-[ASCompetitionManager completeCompetitionWithFriendWithUUID:completion:]_block_invoke.364
+ ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.337
+ ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.338
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.307
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.313
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.309
+ ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.309.cold.1
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.320
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.327
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.331
+ ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke_2.321
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.368
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.372
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.369
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.373
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.370
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.374
+ ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_4
+ ___74-[ASRelationshipManager ignoreInviteRequestFromFriendWithUUID:completion:]_block_invoke.377
+ ___76-[ASIDSMessageCenter _sendPayload:type:destinations:fromAddress:completion:]_block_invoke.376
+ ___77-[ASActivityDataNotificationManager _queue_selectGoalCompletionNotifications]_block_invoke.341
+ ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.315
+ ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.315.cold.1
+ ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.315.cold.2
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.316.cold.1
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.316.cold.2
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.316.cold.3
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.319
+ ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.320
+ ___78-[ASCompetitionManager ignoreCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.321
+ ___84-[ASCompetitionManager _queue_cleanUpLegacyCompetitionLists:activity:cloudKitGroup:]_block_invoke.355
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.311
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.313
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.320
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.322
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.324
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.312
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.316
+ ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.323
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.408
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.408.cold.1
+ ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.409
+ ___86-[ASCloudKitManager _performNewAccountTasksCreatingSubscriptions:fetching:completion:]_block_invoke.463
+ ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.322
+ ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.322.cold.1
+ ___89-[ASCompetitionManager _queue_cleanUpSecureCloudCompetitionLists:activity:cloudKitGroup:]_block_invoke.360
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.326
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.327
+ ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.328
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.329
+ ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.330
+ ___93-[ASDatabaseClient deletedHealthKitWorkoutsWithinLastNumberOfDays:maxBatchSize:anchor:error:]_block_invoke.329
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.418
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.421
+ ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke_2.422
+ ___96-[ASRelationshipManager saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:]_block_invoke.404
+ ___96-[ASRelationshipManager saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:]_block_invoke.407
+ ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.365
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.360
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.361
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.362
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_2.363
+ ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_3.364
+ ___98-[ASActivityDataManager currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:]_block_invoke.353
+ ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.308
+ ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.316
+ ___ASReconcileRelationshipsAgainstAddressBook_block_invoke_2.323
+ ___ASSendRichMessagePayloadToDestination_block_invoke
+ ___assert_rtn
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs96bs_e20_v20?0B8"NSError"12ls88l8s96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88bs96bs_e20_v20?0B8"NSError"12ls32l8s40l8s88l8s96l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_121_e8_32s40s48s56s64s72s80s88s96bs104bs_e5_v8?0ls32l8s40l8s48l8s96l8s104l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_32_e18_16?0"NSString"8l
+ ___block_descriptor_32_e26_16?0"IDSFirewallEntry"8l
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e33_v24?0"IDSFirewall"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32r_e24_v16?0"NSNotification"8lr32l8
+ ___block_descriptor_40_e8_32s_e25_v32?0"ASFriend"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e41_v32?0"NSArray"8"NSArray"16"NSError"24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e33_v24?0"IDSFirewall"8"NSError"16ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e53_"_HKFitnessFriendAchievement"16?0"ACHAchievement"8ls32l8s40l8
+ ___block_literal_global.294
+ ___block_literal_global.295
+ ___block_literal_global.299
+ ___block_literal_global.301
+ ___block_literal_global.311
+ ___block_literal_global.312
+ ___block_literal_global.319
+ ___block_literal_global.325
+ ___block_literal_global.326
+ ___block_literal_global.330
+ ___block_literal_global.338
+ ___block_literal_global.340
+ ___block_literal_global.345
+ ___block_literal_global.349
+ ___block_literal_global.357
+ ___block_literal_global.362
+ ___block_literal_global.368
+ ___block_literal_global.372
+ ___block_literal_global.377
+ ___block_literal_global.393
+ ___block_literal_global.396
+ ___block_literal_global.402
+ ___block_literal_global.406
+ ___block_literal_global.420
+ ___block_literal_global.455
+ ___block_literal_global.469
+ ___block_literal_global.477
+ ___block_literal_global.481
+ ___block_literal_global.488
+ ___block_literal_global.495
+ ___block_literal_global.502
+ ___block_literal_global.506
+ ___block_literal_global.513
+ ___block_literal_global.516
+ ___block_literal_global.523
+ ___block_literal_global.526
+ ___block_literal_global.533
+ ___block_literal_global.536
+ ___block_literal_global.543
+ ___block_literal_global.550
+ ___block_literal_global.554
+ ___block_literal_global.561
+ ___block_literal_global.564
+ ___block_literal_global.571
+ ___block_literal_global.578
+ ___block_literal_global.582
+ ___block_literal_global.586
+ ___block_literal_global.607
+ ___block_literal_global.653
+ ___block_literal_global.656
+ ___block_literal_global.657
+ _kASLiveBubblesBundleIdentifier
+ _kFZListenerCapChats
+ _objc_msgSend$URIWithUnprefixedURI:
+ _objc_msgSend$_donateEntries:completion:
+ _objc_msgSend$_retrieveFirewallWithCompletion:
+ _objc_msgSend$accountsForService:
+ _objc_msgSend$addListenerID:capabilities:
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$blockUntilConnected
+ _objc_msgSend$chatWithHandle:
+ _objc_msgSend$currentDonatedEntries:
+ _objc_msgSend$currentRunLoop
+ _objc_msgSend$donateAddresses:completion:
+ _objc_msgSend$donateEntries:withCompletion:
+ _objc_msgSend$existingChatWithHandle:
+ _objc_msgSend$hasListenerForID:
+ _objc_msgSend$imHandleWithID:
+ _objc_msgSend$initWithSender:time:text:messageSubject:fileTransferGUIDs:flags:error:guid:subject:balloonBundleID:payloadData:expressiveSendStyleID:
+ _objc_msgSend$initWithURI:
+ _objc_msgSend$isActive
+ _objc_msgSend$join
+ _objc_msgSend$joinState
+ _objc_msgSend$mainQueue
+ _objc_msgSend$retrieveFirewallWithQueue:completion:
+ _objc_msgSend$runMode:beforeDate:
+ _objc_msgSend$sendMessage:
+ _objc_msgSend$serviceWithName:
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$sharedRegistry
+ _objc_msgSend$stringGUID
+ _objc_msgSend$templatesWithCompletion:
+ _objc_msgSend$unprefixedURI
+ _objc_msgSend$uri
- -[ASAchievementManager _removeUnusedTemplatesForFriendWithUUID:templateStore:]
- -[ASAchievementManager _removeUnusedTemplatesForFriendWithUUID:templateStore:].cold.1
- -[ASActivityDataManager achievementStore:didAddAchievements:]
- -[ASActivityDataManager achievementStore:didRemoveAchievements:]
- -[ASActivityDataManager achievementStore:didUpdateAchievements:]
- -[ASActivityDataManager achievementStoreDidFinishInitialFetch:]
- -[ASCompetitionAwardingSource earnedInstancesForHistoricalInterval:databaseContext:]
- -[ASCompetitionTemplateSource _competitionForVictoryTemplate:]
- -[ASCompetitionTemplateSource _competitionForVictoryTemplate:].cold.1
- -[ASCompetitionTemplateSource _friendForVictoryTemplate:]
- -[ASCompetitionTemplateSource _friendForVictoryTemplate:].cold.1
- -[ASCompetitionTemplateSource _friendForVictoryTemplate:].cold.2
- -[ASCompetitionTemplateSource customPlaceholderValuesForTemplate:]
- -[ASCompetitionTemplateSource delegate]
- -[ASCompetitionTemplateSource localizationBundleURLForTemplate:]
- -[ASCompetitionTemplateSource propertyListBundleURLForTemplate:]
- -[ASCompetitionTemplateSource resourceBundleURLForTemplate:]
- -[ASCompetitionTemplateSource resourceBundleURLForTemplate:].cold.1
- -[ASCompetitionTemplateSource runCadence]
- -[ASCompetitionTemplateSource setDelegate:]
- -[ASCompetitionTemplateSource sourceShouldRunForDate:]
- -[ASCompetitionTemplateSource stickerBundleURLForTemplate:]
- -[ASCompetitionTemplateSource templatesForDate:completion:]
- -[ASCompetitionTemplateSource templatesForDate:completion:].cold.1
- GCC_except_table108
- GCC_except_table112
- GCC_except_table120
- GCC_except_table139
- GCC_except_table144
- GCC_except_table155
- GCC_except_table179
- GCC_except_table20
- GCC_except_table242
- GCC_except_table3
- GCC_except_table57
- GCC_except_table59
- _ACHShouldUseNewAwardsSystem
- _ASAchievementLocalizationPathForTemplate
- _ASCompetitionParticipationResourcePath
- _ASCompetitionVictoryPropertyListPathForStyle
- _ASCompetitionVictoryResourcePathForStyle
- _FIIsCategorizedOtherActivityType
- _FILocalizedDayName
- _OBJC_IVAR_$_ASActivityDataManager._achievementStore
- _OBJC_IVAR_$_ASActivityDataManager._useNewAchievementsSystem
- _OBJC_IVAR_$_ASActivityDataNotificationManager._achievementStore
- _OBJC_IVAR_$_ASCompetitionTemplateSource.delegate
- _OBJC_IVAR_$_ASFakingManager._achievementStore
- __AchievementsNotIncludedInAnchorToken
- __OBJC_$_PROP_LIST_ACHDataStorePropertyProviding
- __OBJC_$_PROP_LIST_ACHEarnedInstanceAwarding
- __OBJC_$_PROP_LIST_ACHTemplateSource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACHAchievementStoreObserving
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACHDataStorePropertyProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACHEarnedInstanceAwarding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_ACHTemplateSource
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ACHAchievementStoreObserving
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_ACHTemplateSource
- __OBJC_$_PROTOCOL_METHOD_TYPES_ACHAchievementStoreObserving
- __OBJC_$_PROTOCOL_METHOD_TYPES_ACHDataStorePropertyProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_ACHEarnedInstanceAwarding
- __OBJC_$_PROTOCOL_METHOD_TYPES_ACHTemplateSource
- __OBJC_$_PROTOCOL_REFS_ACHAchievementStoreObserving
- __OBJC_$_PROTOCOL_REFS_ACHDataStorePropertyProviding
- __OBJC_$_PROTOCOL_REFS_ACHEarnedInstanceAwarding
- __OBJC_$_PROTOCOL_REFS_ACHTemplateSource
- __OBJC_CLASS_PROTOCOLS_$_ASCompetitionAwardingSource
- __OBJC_CLASS_PROTOCOLS_$_ASCompetitionTemplateSource
- __OBJC_LABEL_PROTOCOL_$_ACHAchievementStoreObserving
- __OBJC_LABEL_PROTOCOL_$_ACHDataStorePropertyProviding
- __OBJC_LABEL_PROTOCOL_$_ACHEarnedInstanceAwarding
- __OBJC_LABEL_PROTOCOL_$_ACHTemplateSource
- __OBJC_PROTOCOL_$_ACHAchievementStoreObserving
- __OBJC_PROTOCOL_$_ACHDataStorePropertyProviding
- __OBJC_PROTOCOL_$_ACHEarnedInstanceAwarding
- __OBJC_PROTOCOL_$_ACHTemplateSource
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke.334
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.335
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_2.335.cold.1
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_3.336
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.337
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.337.cold.1
- ___100-[ASRelationshipManager setActivityDataVisible:toFriendWithUUID:eventType:cloudKitGroup:completion:]_block_invoke_4.337.cold.2
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.343
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.343.cold.1
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.344
- ___102-[ASCompetitionManager _queue_completeCompetitionIfNecessaryForFriendWithUUID:activity:cloudKitGroup:]_block_invoke.345
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.389
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.390
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke.390.cold.1
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_2.391
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.392
- ___103-[ASRelationshipManager _queue_removeLegacyFriendWithUUID:eventType:activity:cloudKitGroup:completion:]_block_invoke_3.392.cold.1
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.405
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.406
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke.407
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.408
- ___104-[ASRelationshipManager _queue_saveRelationshipAndFetchOrCreateShares:contact:cloudKitGroup:completion:]_block_invoke_2.408.cold.1
- ___106-[ASRelationshipManager updateRelationshipsForCurrentFeatureSupportWithActivity:cloudKitGroup:completion:]_block_invoke.348
- ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.583
- ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.584
- ___107-[ASCloudKitManager _observerQueue_performNotificationStep:onRecords:dispatchGroup:activity:cloudKitGroup:]_block_invoke.584.cold.1
- ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.331
- ___108-[ASActivityDataManager cloudKitManager:didReceiveNewNotificationEvents:moreComing:changesProcessedHandler:]_block_invoke.333
- ___108-[ASCloudKitManager _performAndRetryNewAccountTasksWithRetryInterval:shouldCreateSubscriptions:shouldFetch:]_block_invoke.458
- ___109-[ASRelationshipManager updateRelationshipWithCompetitionEvent:friendUUID:activity:cloudKitGroup:completion:]_block_invoke.347
- ___117-[ASCompetitionManager cloudKitManager:didEndUpdatesForFetchWithType:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.321
- ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.373
- ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.376
- ___122-[ASRelationshipManager messageCenter:didReceiveInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.377
- ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.379
- ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.382
- ___123-[ASRelationshipManager messageCenter:didReceiveInviteResponse:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke_2.380
- ___126-[ASRelationshipManager messageCenter:didReceiveFinalizeHandshake:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.383
- ___130-[ASRelationshipManager messageCenter:didReceiveWithdrawInviteRequest:fromSenderAddress:receiverAddress:messageHandledCompletion:]_block_invoke.384
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.407
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.407.cold.1
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.408
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.408.cold.1
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.410
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.410.cold.1
- ___141-[ASCloudKitManager _queue_startFetchAllChangesOperationWithPriority:activity:changeTokenCache:secureCloudChangeTokenCache:group:completion:]_block_invoke.411
- ___149-[ASCloudKitUtility _saveRecordsIntoPrivateDatabaseCreatingZones:recordIDsToDelete:savePolicy:priority:activity:useZoneWideSharing:group:completion:]_block_invoke.298
- ___153-[ASRelationshipManager cloudKitManager:didReceiveNewRemoteRelationships:fromRecordZoneWithID:moreComing:activity:cloudKitGroup:changesProcessedHandler:]_block_invoke.385
- ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.338
- ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.338.cold.1
- ___155-[ASCloudKitUtility _fetchChangesInDatabase:serverChangeTokenCache:priority:activity:group:additionalZoneIDs:zoneIDsToSkip:fetchConfigurations:completion:]_block_invoke.340
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.327
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.332
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.334
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke.336
- ___165-[ASCloudKitUtility _fetchChangesInZones:additionalZonesToFetch:fetchConfigurations:inDatabase:serverChangeTokenCache:priority:allowRetry:activity:group:completion:]_block_invoke_2.333
- ___19-[ASXPCClient init]_block_invoke.334
- ___31-[ASGatewayManager updateState]_block_invoke.300
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.304
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.305
- ___39-[ASActivitySharingManager daemonReady]_block_invoke.306
- ___39-[ASContactsManager loadCachedContacts]_block_invoke.320
- ___43-[ASDatabaseClient performWhenDaemonReady:]_block_invoke.310
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.292
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.292.cold.1
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.293
- ___45-[ASAchievementManager requestTemplateUpdate]_block_invoke.293.cold.1
- ___46-[ASAsyncTransactionQueue performTransaction:]_block_invoke.290
- ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.303
- ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.303.cold.1
- ___47-[ASPeriodicUpdateManager beginPeriodicUpdates]_block_invoke.304
- ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke.460
- ___48-[ASCloudKitManager _handleAccountStatusChange:]_block_invoke_2.461
- ___48-[ASGatewayManager gatewayStatusWithCompletion:]_block_invoke.297
- ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.445
- ___49-[ASCloudKitManager _handleIncomingNotification:]_block_invoke.446
- ___50-[ASCompetitionStore _saveCompetitionLists:owner:]_block_invoke.297
- ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.338
- ___50-[ASDatabaseClient addSampleObserver:sampleTypes:]_block_invoke.339
- ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.308
- ___54-[ASCloudKitUtility _acceptShareMetadatas:completion:]_block_invoke.308.cold.1
- ___58-[ASRelationshipManager _processPersistedMessagesIfNeeded]_block_invoke.386
- ___59-[ASCompetitionTemplateSource templatesForDate:completion:]_block_invoke
- ___59-[ASCompetitionTemplateSource templatesForDate:completion:]_block_invoke.287
- ___60-[ASActivitySharingManager _mainQueue_completeSetupIfNeeded]_block_invoke.326
- ___60-[ASRelationshipManager _contactStoreDidChangeNotification:]_block_invoke.421
- ___64-[ASActivityDataManager achievementStore:didUpdateAchievements:]_block_invoke
- ___64-[ASActivityDataManager achievementStore:didUpdateAchievements:]_block_invoke.328
- ___64-[ASFriendListManager updateFriendListWithDeletedWorkoutEvents:]_block_invoke.312
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.413
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.414
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.417
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.417.cold.1
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke.418
- ___65-[ASCloudKitManager _fetchAllChangesWithPriority:activity:group:]_block_invoke_2.415
- ___65-[ASCompetitionManager _queue_handleSavedCompetitionListRecords:]_block_invoke.336
- ___65-[ASIDSMessageCenter _handleMessageSendSuccess:error:identifier:]_block_invoke.84
- ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke.364
- ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_2.365
- ___69-[ASCompetitionManager rollCompetitionWithFriendWithUUID:completion:]_block_invoke_3.366
- ___69-[ASDatabaseClient performWhenDataProtectedByFirstUnlockIsAvailable:]_block_invoke.313
- ___69-[ASRelationshipManager setMuteEnabled:forFriendWithUUID:completion:]_block_invoke.346
- ___70-[ASActivityDataNotificationManager _queue_selectWorkoutNotifications]_block_invoke.324
- ___70-[ASDatabaseClient allCodableDatabaseCompetitionListEntriesWithError:]_block_invoke.352
- ___72-[ASActivityDataManager _ckQueue_handleDeletedWorkoutEvents:completion:]_block_invoke.378
- ___73-[ASCompetitionManager completeCompetitionWithFriendWithUUID:completion:]_block_invoke.361
- ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.334
- ___74-[ASActivityDataNotificationManager _queue_selectAchievementNotifications]_block_invoke.335
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.304
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke.310
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.306
- ___74-[ASCompetitionManager sendCompetitionRequestToFriendWithUUID:completion:]_block_invoke_2.306.cold.1
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.317
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.321
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke.328
- ___74-[ASGizmoBulletinPostingManager _postQueuedNotificationRequestsIfPossible]_block_invoke_2.318
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.364
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke.367
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.365
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_2.368
- ___74-[ASRelationshipManager acceptInviteRequestFromFriendWithUUID:completion:]_block_invoke_3.369
- ___74-[ASRelationshipManager ignoreInviteRequestFromFriendWithUUID:completion:]_block_invoke.372
- ___76-[ASIDSMessageCenter _sendPayload:type:destinations:fromAddress:completion:]_block_invoke.88
- ___77-[ASActivityDataNotificationManager _queue_selectGoalCompletionNotifications]_block_invoke.338
- ___78-[ASAchievementManager _removeUnusedTemplatesForFriendWithUUID:templateStore:]_block_invoke
- ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.312
- ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.312.cold.1
- ___78-[ASCloudKitUtility _acceptSharesWithURLs:operation:cloudKitGroup:completion:]_block_invoke.312.cold.2
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.313
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.313.cold.1
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.313.cold.2
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.313.cold.3
- ___78-[ASCompetitionManager acceptCompetitionRequestFromFriendWithUUID:completion:]_block_invoke_2.314
- ___78-[ASCompetitionManager ignoreCompetitionRequestFromFriendWithUUID:completion:]_block_invoke.318
- ___84-[ASCompetitionAwardingSource earnedInstancesForHistoricalInterval:databaseContext:]_block_invoke
- ___84-[ASCompetitionAwardingSource earnedInstancesForHistoricalInterval:databaseContext:]_block_invoke_2
- ___84-[ASCompetitionManager _queue_cleanUpLegacyCompetitionLists:activity:cloudKitGroup:]_block_invoke.352
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.308
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.310
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.312
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.314
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke.316
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.309
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.313
- ___84-[ASPeriodicUpdateManager _queue_performUpdateForActivity:cloudKitGroup:completion:]_block_invoke_2.320
- ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.403
- ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.403.cold.1
- ___84-[ASRelationshipManager _queue_fetchSharesForRelationship:cloudKitGroup:completion:]_block_invoke.404
- ___86-[ASCloudKitManager _performNewAccountTasksCreatingSubscriptions:fetching:completion:]_block_invoke.457
- ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.319
- ___86-[ASCloudKitUtility removeParticipantWithCloudKitAddress:fromShares:group:completion:]_block_invoke.319.cold.1
- ___89-[ASCompetitionManager _queue_cleanUpSecureCloudCompetitionLists:activity:cloudKitGroup:]_block_invoke.357
- ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.323
- ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.324
- ___91-[ASCompetitionManager _handleCompetitionRequestFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.325
- ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.326
- ___92-[ASCompetitionManager _handleAcceptedCompetitionFromFriendWithUUID:activity:cloudKitGroup:]_block_invoke.327
- ___93-[ASDatabaseClient deletedHealthKitWorkoutsWithinLastNumberOfDays:maxBatchSize:anchor:error:]_block_invoke.326
- ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.413
- ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke.416
- ___93-[ASRelationshipManager _queue_processRemoteRelationships:activity:cloudKitGroup:completion:]_block_invoke_2.417
- ___96-[ASRelationshipManager saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:]_block_invoke.399
- ___96-[ASRelationshipManager saveRelationships:extraRecordsToSave:cloudKitGroup:activity:completion:]_block_invoke.402
- ___97-[ASActivityDataManager _workoutsToPushWithYesterdaySnapshot:todaySnapshot:currentWorkoutAnchor:]_block_invoke.363
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.355
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke.357
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_2.359
- ___97-[ASRelationshipManager sendInviteToPersonWithDestination:callerID:serviceIdentifier:completion:]_block_invoke_3.360
- ___98-[ASActivityDataManager currentActivitySummaryHelper:didUpdateTodayActivitySummary:changedFields:]_block_invoke.352
- ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.305
- ___ASReconcileRelationshipsAgainstAddressBook_block_invoke.313
- ___ASReconcileRelationshipsAgainstAddressBook_block_invoke_2.320
- ___block_descriptor_40_e8_32r_e25_v32?0"ASFriend"8Q16^B24lr32l8
- ___block_descriptor_40_e8_32s_e23_B16?0"ASCompetition"8ls32l8
- ___block_descriptor_40_e8_32s_e31_"ACHTemplate"16?0"NSString"8ls32l8
- ___block_descriptor_40_e8_32s_e37_v32?0"NSSet"8"NSSet"16"NSError"24ls32l8
- ___block_descriptor_48_e8_32s40s_e8_v12?0B8ls32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e5_v8?0lr40l8s32l8r48l8
- ___block_descriptor_56_e8_32s40s48s_e53_"_HKFitnessFriendAchievement"16?0"ACHAchievement"8ls32l8s40l8s48l8
- ___block_literal_global.291
- ___block_literal_global.292
- ___block_literal_global.293
- ___block_literal_global.298
- ___block_literal_global.308
- ___block_literal_global.309
- ___block_literal_global.316
- ___block_literal_global.320
- ___block_literal_global.322
- ___block_literal_global.324
- ___block_literal_global.332
- ___block_literal_global.337
- ___block_literal_global.342
- ___block_literal_global.346
- ___block_literal_global.348
- ___block_literal_global.356
- ___block_literal_global.367
- ___block_literal_global.371
- ___block_literal_global.376
- ___block_literal_global.388
- ___block_literal_global.401
- ___block_literal_global.415
- ___block_literal_global.449
- ___block_literal_global.463
- ___block_literal_global.471
- ___block_literal_global.475
- ___block_literal_global.480
- ___block_literal_global.482
- ___block_literal_global.489
- ___block_literal_global.496
- ___block_literal_global.500
- ___block_literal_global.507
- ___block_literal_global.514
- ___block_literal_global.517
- ___block_literal_global.524
- ___block_literal_global.527
- ___block_literal_global.534
- ___block_literal_global.537
- ___block_literal_global.544
- ___block_literal_global.548
- ___block_literal_global.555
- ___block_literal_global.562
- ___block_literal_global.565
- ___block_literal_global.572
- ___block_literal_global.576
- ___block_literal_global.601
- ___block_literal_global.652
- ___block_literal_global.658
- ___block_literal_global.661
- _kASAchievementLocalizedPlaceholderCompetitionEndDayKey
- _kASAchievementLocalizedPlaceholderFriendNameKey
- _objc_msgSend$_competitionForVictoryTemplate:
- _objc_msgSend$_friendForVictoryTemplate:
- _objc_msgSend$achievementWithTemplateUniqueName:
- _objc_msgSend$allAchievements
- _objc_msgSend$currentOrMostRecentCompetition
- _objc_msgSend$delegate
- _objc_msgSend$earnedInstances
- _objc_msgSend$ephemeralAchievementWithTemplateUniqueName:
- _objc_msgSend$hk_isBeforeDate:
- _objc_msgSend$lastDayOfCompetition
- _objc_msgSend$predicate
- _objc_msgSend$removeTemplates:error:
- _objc_msgSend$templateForUniqueName:
- _objc_msgSend$templateSourceDidUpdateAssets:
- _objc_msgSend$templatesForDate:completion:
CStrings:
+ "%@:0000000000:%@"
+ "@16@?0@\"IDSFirewallEntry\"8"
+ "@16@?0@\"NSString\"8"
+ "ASSendMessageUtilities.m"
+ "ASSendRichMessagePayloadToDestination"
+ "F"
+ "Getting achievements to push for today"
+ "IDSMessageCenter added firewall entries %{public}@"
+ "IDSMessageCenter adding firewall entries %{public}@"
+ "IDSMessageCenter donating firewall entries %{public}@, to firewall %{public}@"
+ "IDSMessageCenter failed to create entries for %{public}@"
+ "IDSMessageCenter failed to create firewall entry for %{public}@"
+ "IDSMessageCenter failed to create uri for %{public}@"
+ "IDSMessageCenter failed to donate firewall entries %{public}@, error %{public}@"
+ "IDSMessageCenter failed to get current donated entries"
+ "IDSMessageCenter failed to get current donated entries: %{public}@"
+ "IDSMessageCenter failed to retrieve firewall"
+ "IDSMessageCenter failed to retrieve firewall %{public}@"
+ "MSMessageLiveLayout"
+ "MSMessageTemplateLayout"
+ "RelationshipManager donating address to IDS %@"
+ "URIWithUnprefixedURI:"
+ "_donateEntries:completion:"
+ "_retrieveFirewallWithCompletion:"
+ "accountsForService:"
+ "activeAccount"
+ "addListenerID:capabilities:"
+ "addObserverForName:object:queue:usingBlock:"
+ "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
+ "blockUntilConnected"
+ "chat"
+ "chatWithHandle:"
+ "com.apple.ActivitySharing.IDSMessageCenter"
+ "com.apple.ActivitySharingControl"
+ "currentDonatedEntries:"
+ "currentRunLoop"
+ "donateAddresses:completion:"
+ "donateEntries:withCompletion:"
+ "donatedAddressesWithCompletion:"
+ "existingChatWithHandle:"
+ "handle"
+ "hasListenerForID:"
+ "iMessage"
+ "imHandleWithID:"
+ "initWithSender:time:text:messageSubject:fileTransferGUIDs:flags:error:guid:subject:balloonBundleID:payloadData:expressiveSendStyleID:"
+ "initWithURI:"
+ "invalidateAndWait"
+ "isActive"
+ "join"
+ "joinState"
+ "mainQueue"
+ "retrieveFirewallWithQueue:completion:"
+ "runMode:beforeDate:"
+ "sendMessage:"
+ "service"
+ "serviceWithName:"
+ "sharedInstance"
+ "sharedRegistry"
+ "stringGUID"
+ "templatesWithCompletion:"
+ "unprefixedURI"
+ "uri"
+ "v16@?0@\"NSNotification\"8"
+ "v24@?0@\"IDSFirewall\"8@\"NSError\"16"
+ "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
+ "v64@0:8@16@24Q32Q40@48@56"
+ "\xf0\xe4"
- "!&"
- "@\"ACHAchievementStore\""
- "@\"ACHTemplate\"16@?0@\"NSString\"8"
- "@\"NSDictionary\"16@0:8"
- "@\"NSDictionary\"32@0:8@\"ACHTemplate\"16^@24"
- "@\"NSObject<ACHTemplateSourceDelegate>\""
- "@\"NSObject<ACHTemplateSourceDelegate>\"16@0:8"
- "@\"NSSet\"32@0:8@\"NSDateInterval\"16@\"HDDatabaseTransactionContext\"24"
- "@\"NSSet\"32@0:8@\"NSDateInterval\"16^@24"
- "@\"NSURL\"24@0:8@\"ACHTemplate\"16"
- "ACHAchievementStoreObserving"
- "ACHDataStorePropertyProviding"
- "ACHEarnedInstanceAwarding"
- "ACHTemplateSource"
- "AchievementManager found %lu templates to remove"
- "AchievementManager looking up templates for names: %@"
- "AchievementManager removed unused templates with result: %{BOOL}d, %{public}@"
- "Achievements updated, checking for new today achievements to push"
- "Alerts are currently suppressed, not checking for achievements to push"
- "B24@0:8@\"NSDate\"16"
- "Couldn't find a competition to determine badge style for friend: %{public}@ - %@"
- "Couldn't find friend with UUID: %{public}@"
- "FriendUUID missing from template: %@"
- "Getting achievements to push for today from the new system"
- "Notifying delegate that we updated assets templates: %@"
- "Responding to earned instances for historical interval: %@"
- "Responding to resource bundle for template: %@"
- "T@\"NSArray\",R,N"
- "T@\"NSDictionary\",&,N"
- "T@\"NSObject<ACHTemplateSourceDelegate>\",?,W,N"
- "T@\"NSObject<ACHTemplateSourceDelegate>\",?,W,N,Vdelegate"
- "Tq,R,N"
- "_achievementStore"
- "_competitionForVictoryTemplate:"
- "_friendForVictoryTemplate:"
- "_removeUnusedTemplatesForFriendWithUUID:templateStore:"
- "achievementStore:didAddAchievements:"
- "achievementStore:didRemoveAchievements:"
- "achievementStore:didUpdateAchievements:"
- "achievementStoreDidFinishInitialFetch:"
- "achievementWithTemplateUniqueName:"
- "allAchievements"
- "currentOrMostRecentCompetition"
- "customPlaceholderValuesForTemplate:"
- "customPlaceholderValuesForTemplate:error:"
- "dataStoreDidClearAllProperties:completion:"
- "dataStoreProperties"
- "dataStorePropertyKeys"
- "earnedInstances"
- "earnedInstancesForHistoricalInterval:databaseContext:"
- "earnedInstancesForHistoricalInterval:error:"
- "ephemeralAchievementWithTemplateUniqueName:"
- "hk_isBeforeDate:"
- "lastDayOfCompetition"
- "localizationBundleURLForTemplate:"
- "mobileAssetVersionForTemplate:"
- "predicate"
- "propertyListBundleURLForTemplate:"
- "q24@0:8@\"ACHTemplate\"16"
- "q24@0:8@16"
- "removeTemplates:error:"
- "resourceBundleURLForTemplate:"
- "runCadence"
- "setDataStoreProperties:"
- "sourceShouldRunForDate:"
- "stickerBundleURLForTemplate:"
- "templateForUniqueName:"
- "templateSourceDidUpdateAssets:"
- "templatesForDate:completion:"
- "templatesForDate:databaseContext:completion:"
- "v24@0:8@\"<ACHAchievementStoring>\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSObject<ACHTemplateSourceDelegate>\"16"
- "v32@0:8@\"<ACHAchievementStoring>\"16@\"NSSet\"24"
- "v32@0:8@\"ACHDataStore\"16@?<v@?B>24"
- "v32@0:8@\"NSDate\"16@?<v@?@\"NSSet\"@\"NSSet\"@\"NSError\">24"
- "v32@?0@\"NSSet\"8@\"NSSet\"16@\"NSError\"24"
- "v40@0:8@\"NSDate\"16@\"HDDatabaseTransactionContext\"24@?<v@?@\"NSSet\"@\"NSSet\"@\"NSError\">32"
- "\xf0\xd1$"

```
