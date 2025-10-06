## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1852.6.1.0.0
-  __TEXT.__text: 0x19045c
+1852.19.0.2.0
+  __TEXT.__text: 0x19095c
   __TEXT.__auth_stubs: 0x1460
-  __TEXT.__objc_methlist: 0xff54
-  __TEXT.__cstring: 0x15941
-  __TEXT.__oslogstring: 0x17fff
+  __TEXT.__objc_methlist: 0xff84
+  __TEXT.__cstring: 0x159c5
+  __TEXT.__oslogstring: 0x1801b
   __TEXT.__const: 0x3d8
-  __TEXT.__gcc_except_tab: 0x6150
+  __TEXT.__gcc_except_tab: 0x61a8
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x52ec
-  __TEXT.__objc_classname: 0x2c28
-  __TEXT.__objc_methname: 0x24de3
-  __TEXT.__objc_methtype: 0x6001
-  __TEXT.__objc_stubs: 0x167a0
+  __TEXT.__unwind_info: 0x52f0
+  __TEXT.__objc_classname: 0x2c29
+  __TEXT.__objc_methname: 0x24f19
+  __TEXT.__objc_methtype: 0x6038
+  __TEXT.__objc_stubs: 0x16840
   __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x37c0
+  __DATA_CONST.__const: 0x37e8
   __DATA_CONST.__objc_classlist: 0xc20
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1c618
-  __DATA_CONST.__objc_selrefs: 0x7be0
+  __DATA_CONST.__objc_const: 0x1c628
+  __DATA_CONST.__objc_selrefs: 0x7c08
+  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_classrefs: 0xdf8
+  __DATA_CONST.__objc_superrefs: 0x690
   __DATA_CONST.__objc_arraydata: 0x630
-  __AUTH_CONST.__cfstring: 0x12f00
+  __AUTH_CONST.__cfstring: 0x12fc0
   __AUTH_CONST.__objc_const: 0x8c78
   __AUTH_CONST.__const: 0x1880
   __AUTH_CONST.__objc_intobj: 0x2298

   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0xa40
   __AUTH.__objc_data: 0x4a10
-  __DATA.__objc_protorefs: 0x70
-  __DATA.__objc_classrefs: 0xdf8
-  __DATA.__objc_superrefs: 0x690
-  __DATA.__objc_ivar: 0x179c
-  __DATA.__data: 0x2170
-  __DATA.__bss: 0x3b0
+  __DATA.__objc_ivar: 0x17a0
+  __DATA.__data: 0x2198
+  __DATA.__bss: 0x388
   __DATA.__common: 0x38
   __DATA_DIRTY.__const: 0x18
   __DATA_DIRTY.__objc_data: 0x2f30

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 85430D16-CAF7-3EEE-BAD5-8B452A574D70
-  Functions: 8771
-  Symbols:   27039
-  CStrings:  14136
+  UUID: 36255D1F-D3F6-345D-9BDF-AFA0D3F30F0C
+  Functions: 8777
+  Symbols:   27058
+  CStrings:  14157
 
Symbols:
+ +[_CDContact(Predicates) predicateForContactWithContactIdType:]
+ -[_CDContact contactIdType]
+ -[_CDContact initWithIdentifier:type:customIdentifier:displayName:displayType:personId:personIdType:displayImageURL:participantStatus:contactIdType:]
+ -[_CDContact setContactIdType:]
+ -[_CDContactChangeHistoryEventVisitor reset]
+ -[_CDContactChangeHistoryEventVisitor visitEventsWithBatchSize:batchCallback:]
+ -[_CDInteractionStore appendMissingInformationForRecord:fromContact:cacheUpdateRequired:]
+ GCC_except_table71
+ GCC_except_table74
+ _OBJC_IVAR_$__CDContact._contactIdType
+ _OBJC_IVAR_$__CDContactChangeHistoryEventVisitor._count
+ ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.419
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.469
+ ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.477
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.890
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.890.cold.1
+ ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.895
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.575
+ ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.579
+ ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.637
+ ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.101
+ ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.101.cold.1
+ ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.107
+ ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.85
+ ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.85.cold.1
+ ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.92
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.956
+ ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.956.cold.1
+ ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.563
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.671
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.671.cold.1
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.671.cold.2
+ ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.671.cold.3
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.712
+ ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.715
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.643
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.643.cold.1
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.643.cold.2
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.643.cold.3
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.643.cold.4
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.643.cold.5
+ ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.643.cold.6
+ ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.490
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.560
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.560.cold.1
+ ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.614
+ ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.635
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.427
+ ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.427.cold.1
+ ___71-[_DKContactsPrivacyMaintainer handleRecentlyDeletedContactsWithLimit:]_block_invoke
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.696
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.698
+ ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.699
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.687
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.690
+ ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.692
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.549
+ ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.512
+ ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.564
+ ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.564.cold.1
+ ___block_descriptor_64_e8_32s40r48r_e49_v24?0"_CDContactChangeHistoryEventVisitor"8^B16ls32l8r40l8r48l8
+ ___block_literal_global.417
+ ___block_literal_global.431
+ ___block_literal_global.461
+ ___block_literal_global.462
+ ___block_literal_global.464
+ ___block_literal_global.467
+ ___block_literal_global.473
+ ___block_literal_global.479
+ ___block_literal_global.482
+ ___block_literal_global.524
+ ___block_literal_global.527
+ ___block_literal_global.542
+ ___block_literal_global.565
+ ___block_literal_global.578
+ ___block_literal_global.582
+ ___block_literal_global.592
+ ___block_literal_global.595
+ ___block_literal_global.605
+ ___block_literal_global.617
+ ___block_literal_global.621
+ ___block_literal_global.624
+ ___block_literal_global.625
+ ___block_literal_global.630
+ ___block_literal_global.636
+ ___block_literal_global.651
+ ___block_literal_global.654
+ ___block_literal_global.683
+ ___block_literal_global.701
+ ___block_literal_global.753
+ ___block_literal_global.785
+ ___block_literal_global.862
+ ___block_literal_global.866
+ ___block_literal_global.869
+ ___block_literal_global.927
+ ___block_literal_global.96
+ __unnamed_array_storage.1009
+ __unnamed_array_storage.461
+ __unnamed_array_storage.499
+ __unnamed_array_storage.510
+ __unnamed_array_storage.532
+ __unnamed_array_storage.539
+ __unnamed_array_storage.552
+ __unnamed_array_storage.561
+ __unnamed_array_storage.562
+ __unnamed_array_storage.563
+ __unnamed_array_storage.566
+ __unnamed_array_storage.570
+ __unnamed_array_storage.579
+ __unnamed_array_storage.583
+ __unnamed_array_storage.597
+ __unnamed_array_storage.606
+ __unnamed_array_storage.612
+ __unnamed_array_storage.616
+ _contactIdTypeToString
+ _objc_msgSend$appendMissingInformationForRecord:fromContact:cacheUpdateRequired:
+ _objc_msgSend$contactIdType
+ _objc_msgSend$initWithIdentifier:type:customIdentifier:displayName:displayType:personId:personIdType:displayImageURL:participantStatus:contactIdType:
+ _objc_msgSend$setContactBatchCount:
+ _objc_msgSend$setContactIdType:
+ _objc_msgSend$visitEventsWithBatchSize:batchCallback:
+ _sharedInstance.initialized.414
+ _sharedInstance.initialized.455
+ _sharedInstance.sharedInstance.415
+ _sharedInstance.sharedInstance.456
- -[_CDContactChangeHistoryEventVisitor addedContactIdentifiers]
- -[_CDContactChangeHistoryEventVisitor currentHistoryToken]
- -[_CDContactChangeHistoryEventVisitor visitChanges]
- GCC_except_table61
- GCC_except_table73
- GCC_except_table88
- _OBJC_IVAR_$__CDContactChangeHistoryEventVisitor._addedContactIdentifiers
- ___104-[_CDPersistedCoalescingTimer initWithDelay:coalesceData:operation:persistencePath:dataClass:timerName:]_block_invoke.395
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.445
- ___113-[_CDSpotlightItemRecorder initWithInteractionRecorder:knowledgeStore:rateLimitEnforcer:deletionManagerOverride:]_block_invoke.453
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.866
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.866.cold.1
- ___167-[_CDCloudFamilyDataCollectionTask initWithStorage:contactStore:medicalIDStore:activity:sessionPath:dataDirectory:collectionDate:samplingRate:maxBatches:daysPerBatch:]_block_invoke.871
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke.551
- ___38-[_DKBiomeQuery _publisherForStreams:]_block_invoke_2.555
- ___40-[_DKBiomeQuery executeBiomeQueryError:]_block_invoke.613
- ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.100
- ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.100.cold.1
- ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.106
- ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.84
- ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.84.cold.1
- ___48-[CDMonitorManager initWithEventStreams:domain:]_block_invoke.91
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.932
- ___48-[_CDCloudFamilyDataCollectionTask labelMembers]_block_invoke.932.cold.1
- ___51-[_DKSync2Coordinator __performSyncWithCompletion:]_block_invoke.539
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.647
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.647.cold.1
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.647.cold.2
- ___55-[_DKKnowledgeStorage fetchSyncChangesSinceDate:error:]_block_invoke.647.cold.3
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke.688
- ___56-[_DKKnowledgeStorage _databaseChangedWithNotification:]_block_invoke_2.691
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.1
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.2
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.3
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.4
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.5
- ___56-[_DKKnowledgeStorage fetchLocalChangesSinceDate:error:]_block_invoke.619.cold.6
- ___65+[_CDSpotlightItemUtils interactionForSearchableItem:nsUserName:]_block_invoke.466
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.536
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.536.cold.1
- ___66-[_DKKnowledgeStorage saveHistogram:responseQueue:withCompletion:]_block_invoke.590
- ___67-[_DKSync2Coordinator _registerTriggeredSyncActivityWithIsStartup:]_block_invoke.611
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.403
- ___68-[_DKContactsPrivacyMaintainer registerContactDeletionNotifications]_block_invoke.403.cold.1
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.672
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.674
- ___74-[_DKKnowledgeStorage startSyncUpToCloudWithResponseQueue:withCompletion:]_block_invoke.675
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.663
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.666
- ___78-[_DKKnowledgeStorage startSyncDownFromCloudWithResponseQueue:withCompletion:]_block_invoke.668
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.525
- ___86-[_DKCloudUtilities _performUpdateNumberOfSyncedDevicesWithAttempt:completionHandler:]_block_invoke.488
- ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.540
- ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.540.cold.1
- ___block_literal_global.401
- ___block_literal_global.407
- ___block_literal_global.416
- ___block_literal_global.437
- ___block_literal_global.438
- ___block_literal_global.440
- ___block_literal_global.443
- ___block_literal_global.455
- ___block_literal_global.457
- ___block_literal_global.494
- ___block_literal_global.500
- ___block_literal_global.503
- ___block_literal_global.541
- ___block_literal_global.554
- ___block_literal_global.558
- ___block_literal_global.568
- ___block_literal_global.571
- ___block_literal_global.576
- ___block_literal_global.581
- ___block_literal_global.588
- ___block_literal_global.593
- ___block_literal_global.597
- ___block_literal_global.601
- ___block_literal_global.602
- ___block_literal_global.606
- ___block_literal_global.629
- ___block_literal_global.634
- ___block_literal_global.677
- ___block_literal_global.729
- ___block_literal_global.760
- ___block_literal_global.817
- ___block_literal_global.838
- ___block_literal_global.845
- ___block_literal_global.903
- ___block_literal_global.95
- __unnamed_array_storage.437
- __unnamed_array_storage.475
- __unnamed_array_storage.486
- __unnamed_array_storage.508
- __unnamed_array_storage.515
- __unnamed_array_storage.527
- __unnamed_array_storage.528
- __unnamed_array_storage.537
- __unnamed_array_storage.538
- __unnamed_array_storage.542
- __unnamed_array_storage.546
- __unnamed_array_storage.555
- __unnamed_array_storage.559
- __unnamed_array_storage.564
- __unnamed_array_storage.573
- __unnamed_array_storage.582
- __unnamed_array_storage.592
- __unnamed_array_storage.985
- _objc_msgSend$visitChanges
- _sharedInstance.initialized.413
- _sharedInstance.initialized.454
- _sharedInstance.sharedInstance.414
- _sharedInstance.sharedInstance.455
CStrings:
+ "\x13\x11!\x11"
+ "%@ - visitEventsWithBatchSize processed batch with size: %lu, numContactsProcessed: %lu, shouldSaveToken: %@"
+ "%@; %@; %@; %@; displayImageURL=%@; %@"
+ "@\"NSEnumerator\""
+ "@40@0:8@16@24^B32"
+ "@96@0:8@16Q24@32@40Q48@56Q64@72q80q88"
+ "ABRecordId=%@"
+ "CNContactId=%@"
+ "ContactIdType=%@"
+ "None"
+ "Organization"
+ "ParticipantStatus=%@"
+ "Person"
+ "SGRecordId=%@"
+ "T@\"NSString\",?,R,C"
+ "Tq,V_contactIdType"
+ "_contactIdType"
+ "appendMissingInformationForRecord:fromContact:cacheUpdateRequired:"
+ "contactIdType"
+ "contactIdType == %@"
+ "initWithIdentifier:type:customIdentifier:displayName:displayType:personId:personIdType:displayImageURL:participantStatus:contactIdType:"
+ "predicateForContactWithContactIdType:"
+ "setContactBatchCount:"
+ "setContactIdType:"
+ "v24@?0@\"_CDContactChangeHistoryEventVisitor\"8^B16"
+ "visitEventsWithBatchSize:batchCallback:"
- "\x13\x11\""
- "%@ - handleContactDeletionNotification found %lu deleted contact identifiers: %@"
- "%@;%@%@%@;displayImageURL=%@"
- ";ABRecordId=%@"
- ";CNContactId=%@"
- ";ParticipantStatus=%@"
- ";SGRecordId=%@"
- "@\"CNFetchResult\""
- "T@\"NSData\",R,N"
- "_addedContactIdentifiers"
- "addedContactIdentifiers"
- "visitChanges"

```
